#!/usr/bin/env python3
"""
u2_growth_vs_equilibrium.py — design note 8 gate G1: irreversible growth vs
j2's equilibrium attractor, two arms.

THE QUESTION (note 8 §4 G1): paper 13 §3 measured that equilibrium driven
search under paper 11's combined r+link misfit action parks at a dense
third-class compromise (endpoint r ~ 0.78, H = 16-19, dim <= 2 NO) — an
action-value success and a landscape/sampling failure. Growth is the
ISP-native alternative: elements arrive one at a time (the commit sequence
is a linear extension by construction), moves are chosen at arrival, and
NOTHING is ever revisited — indivisibility as a sampling mode.

THE TELESCOPE (Arm A's exactness lemma, verified in CHECK 1): under growth,
every new element is MAXIMAL at arrival, so a related pair's interval is
complete the moment its top element lands and its action charge never changes
afterwards. Hence S telescopes exactly over arrivals: the misfit-increment
functional Phi = dS is EXACT and cheap (O(|down| * t^2) vectorized per
candidate) — the primary functional of note 8 §3(a) at full fidelity, no
surrogate.

MAIN-LOOP PREDICTION, RECORDED BEFORE FIRST RUN (pre-registration): the bare
r+link action has a DEGENERATE GLOBAL MINIMUM — S(antichain) = 0 identically
(both terms charge only related pairs) — which equilibrium search never
reached because its kernel densifies (j2's beta = 0 control: r = 0.99
near-chain) and the entropy of the proposal landscape competes. Growth with
argmin-dS (beta = inf) is predicted to head TOWARD the sparse degenerate
direction (low r, pathology-class endpoints), INVERTING j2's dense failure
mode rather than reproducing it — i.e. the misfit action lacks a
comparability-forcing (abundance) term in BOTH sampling modes, and growth
localizes the missing term more sharply than equilibrium did. Escape
(in-cell endpoints) is NOT predicted for the bare action. The prediction is
falsifiable by the run; either verdict is recorded.

ARM A (general-order growth, exact Phi): n = 64 (the 128 arm was
planned here and not run — corrected 2026-07-05 to match execution, per the
paper-17 round-1 review; the scale extension rides the successor campaign's
growth bench); per arrival K = 12
candidate down-sets from a transitive-percolation kernel (per-candidate
p ~ loguniform(1/t, 0.6), Bernoulli ancestors, downward closure; one empty
candidate always included — DISCLOSED kernel choice, ablated in CHECK 5);
beta in {0, 1, beta* = 16 ln 2, inf}; endpoints classified with j2's own
instrument (r, height, capped dim <= 2 oracle with honest UNDECIDED, action
decomposition) against a same-n sprinkling ensemble and j2's published
attractor descriptors (r ~ 0.78; sprinkling S = 175.6 +/- 6.2 at n = 64).
n = 64 is BELOW the link-term crossover (paper 11 §3.3; paper 13 §3's scale
disclosure travels verbatim): this arm probes small-n minimizers under
growth, exactly comparable to j2's small-n equilibrium probe — asymptotic
selection is not claimed by either.

ARM B (record-native two-clock growth, victim-selection law): the churn web
with the u1-validated uniform-victim kernel, victim chosen by Gibbs(beta)
over Phi_rank(s) = chi-rank fraction of slot s (kill-the-leader at
beta = inf). TEACHING-TO-THE-TEST DISCLOSURE: Phi_rank acts directly on the
chi ordering that T2 scores; the dispersion layer (T3) and T1 are the
independent guards, and all three are reported. G3 rides this arm, with a
main-loop correction caught at the exploration pass: for fixed-event-rate
laws the MEAN lifetime is budget-pinned by accounting (the note's
"endogenous L" is distribution-level only here; rate-level endogenization
is a different design, deferred) — CHECK 7 states the identity.

GATE DISCIPLINE: gates marked [pinned-post-exploration] were set from the
disclosed same-date single exploration pass of this receipt on this stream
(the substituted endpoint screens' gates are themselves post-exploration — paper 17 §9 items 3/10; the note's pre-authorization covered the registered trajectory form, not run); all other gates
are the note's. Conventions: default_rng(20260703); float64 landscapes;
M0 = 8; beta* = 16 ln 2 = 11.0904.
"""

import numpy as np

rng = np.random.default_rng(20260703)

PASS = 0
FAIL = 0
M0 = 8
BETA_STAR = 16 * np.log(2)

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ----------------------------------------------- j2's action + instruments
def action(C):
    N = C.shape[0]
    Cf = C.astype(np.float32)
    btw = np.rint(Cf @ Cf).astype(np.int32)
    S = 0.0
    ii, jj = np.nonzero(C & (btw >= M0))
    for x, y in zip(ii, jj):
        inner = np.nonzero(C[x] & C[:, y])[0]
        k = len(inner)
        sub = C[np.ix_(inner, inner)]
        r = 2.0 * sub.sum() / (k * (k - 1)) if k > 1 else 0.0
        S += (r - 0.5) ** 2
    S += 0.25 * float((C & (btw < M0)).sum())
    return S

def dominance_order(pts):
    return (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])

def dim_le_2_capped(C, cap=3_000_000):
    N = C.shape[0]
    nodes = list(range(N))
    incomp = [(i, j) for i in range(N) for j in range(i + 1, N)
              if not (C[i, j] or C[j, i])]
    if not incomp:
        return True
    adj = set()
    for (a, b) in incomp:
        adj.add((a, b)); adj.add((b, a))
    direction = {}
    work = [0]

    def force(a, b):
        changed = []
        stack = [(a, b)]
        while stack:
            work[0] += 1
            if work[0] > cap:
                raise TimeoutError
            x, y = stack.pop()
            key = frozenset((x, y))
            if key in direction:
                if direction[key] != (x, y):
                    for k in changed: del direction[k]
                    return None
                continue
            direction[key] = (x, y); changed.append(key)
            for z in nodes:
                if z == x or z == y: continue
                kyz = frozenset((y, z))
                if kyz in direction and direction[kyz] == (y, z):
                    if (x, z) in adj: stack.append((x, z))
                    else:
                        for k in changed: del direction[k]
                        return None
                kzx = frozenset((z, x))
                if kzx in direction and direction[kzx] == (z, x):
                    if (z, y) in adj: stack.append((z, y))
                    else:
                        for k in changed: del direction[k]
                        return None
        return changed

    elist = list(incomp)
    import sys
    sys.setrecursionlimit(100000)
    def bt(ei):
        if ei == len(elist): return True
        a, b = elist[ei]
        if frozenset((a, b)) in direction: return bt(ei + 1)
        for (x, y) in ((a, b), (b, a)):
            ch = force(x, y)
            if ch is not None:
                if bt(ei + 1): return True
                for k in ch:
                    if k in direction: del direction[k]
        return False
    try:
        return bt(0)
    except TimeoutError:
        return None
    except RecursionError:
        return None

def descriptors(C):
    N = C.shape[0]
    r_frac = 2.0 * C.sum() / (N * (N - 1))
    indeg = C.sum(axis=0).astype(int)
    L = np.ones(N, dtype=int)
    Cl = [np.nonzero(C[i])[0] for i in range(N)]
    ind = indeg.copy()
    stack = [i for i in range(N) if ind[i] == 0]
    topo = []
    while stack:
        v = stack.pop(); topo.append(v)
        for w in Cl[v]:
            ind[w] -= 1
            if ind[w] == 0: stack.append(w)
    for v in topo:
        if len(Cl[v]): L[Cl[v]] = np.maximum(L[Cl[v]], L[v] + 1)
    return float(r_frac), int(L.max())

# ----------------------------------------------- Arm A: exact-Phi growth
def delta_S(Ct, Ctf, D):
    """Exact action increment of adding a maximal element with down-set D
    (bool over the t existing elements). New pairs are exactly (x, new) for
    x in D; interior(x) = D & up(x); charge per j2's action verbatim."""
    if not D.any():
        return 0.0
    Didx = np.nonzero(D)[0]
    Mmat = (Ct[Didx, :] & D[None, :]).astype(np.float32)
    k = Mmat.sum(1)
    edges = ((Mmat @ Ctf) * Mmat).sum(1)
    denom = np.maximum(k * (k - 1), 1.0)
    r = 2.0 * edges / denom
    charge = np.where(k >= M0, (r - 0.5) ** 2, 0.25)
    return float(charge.sum())

def grow(n, beta, K=12, include_empty=True):
    """Sequential irreversible growth: at each arrival, K candidate down-sets
    from the transitive-percolation kernel; move chosen by Gibbs(beta) over
    the EXACT dS (beta None => argmin; beta 0 => uniform over candidates)."""
    C = np.zeros((n, n), dtype=bool)
    S = 0.0
    dS_picked = []
    for t in range(1, n):
        Ct = C[:t, :t]
        Ctf = Ct.astype(np.float32)
        cands = []
        if include_empty:
            cands.append(np.zeros(t, dtype=bool))
        while len(cands) < K:
            p = float(np.exp(rng.uniform(np.log(min(1.0 / t, 0.59)), np.log(0.6))))
            anc = rng.random(t) < p
            D = anc | Ct[:, anc].any(axis=1) if anc.any() else anc
            cands.append(D)
        dS = np.array([delta_S(Ct, Ctf, D) for D in cands])
        if beta is None:
            pick = int(np.argmin(dS))
        elif beta == 0:
            pick = int(rng.integers(len(cands)))
        else:
            w = np.exp(-beta * (dS - dS.min())); w /= w.sum()
            pick = int(rng.choice(len(cands), p=w))
        C[:t, t] = cands[pick]
        S += dS[pick]
        dS_picked.append(dS[pick])
    return C, S, dS_picked

# ----------------------------------------------- Arm B: victim-selection web
def web_law(N, M, L, beta_v):
    """Two-clock churn web, uniform race (C1), continuous increments (route
    B), churn events at prob 1/L per commit; victim by Gibbs(beta_v) over
    Phi_rank(s) = chi-rank fraction (beta_v None => kill-the-leader;
    0 => uniform victim = the u1-validated kernel)."""
    chi_acc = np.zeros(M)
    chi = np.zeros(N)
    own = np.zeros(M, dtype=np.int64); born = np.zeros(M, dtype=np.int64)
    lifetimes = []
    for t in range(N):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(0.109551)
        own[c] += 1
        chi[t] = chi_acc[c]
        if rng.random() < 1.0 / L:
            if beta_v is None:
                v = int(np.argmax(chi_acc))
            elif beta_v == 0:
                v = int(rng.integers(M))
            else:
                fr = np.argsort(np.argsort(chi_acc)) / (M - 1.0)
                w = np.exp(beta_v * fr); w /= w.sum()
                v = int(rng.choice(M, p=w))
            lifetimes.append(int(own[v] - born[v]))
            chi_acc[v] = 0.0; born[v] = own[v]
    return np.arange(N), chi, lifetimes

def star_disc(pts):
    N = len(pts)
    us = np.unique(np.concatenate([pts[:, 0], [1.0]]))
    vs = np.unique(np.concatenate([pts[:, 1], [1.0]]))
    order = np.argsort(pts[:, 0], kind="stable")
    pu = pts[order, 0]; pv = pts[order, 1]
    best = 0.0
    for a in us:
        ko = np.searchsorted(pu, a, "left"); kc = np.searchsorted(pu, a, "right")
        so = np.sort(pv[:ko]); sc = np.sort(pv[:kc])
        co = np.searchsorted(so, vs, "left") / N
        cc = np.searchsorted(sc, vs, "right") / N
        vol = a * vs
        best = max(best, float(np.abs(co - vol).max()), float(np.abs(cc - vol).max()))
    return best

def rank_embed2(b, chi):
    N = len(b)
    r1 = np.argsort(np.argsort(b)); r2 = np.argsort(np.argsort(chi))
    return np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])

def spearman_ties(x, y):
    def avg_rank(v):
        o = np.argsort(v, kind="stable"); r = np.empty(len(v)); r[o] = np.arange(len(v))
        vals, inv = np.unique(v, return_inverse=True)
        sums = np.bincount(inv, weights=r); cnts = np.bincount(inv)
        return (sums / cnts)[inv]
    return float(np.corrcoef(avg_rank(x), avg_rank(y))[0, 1])

def interval_fano(b_, c_, kmin=10):
    pts_ = np.column_stack([np.asarray(b_, dtype=float), c_])
    Np = len(pts_)
    C = dominance_order(pts_)
    r1 = np.argsort(np.argsort(pts_[:, 0]))
    r2 = np.argsort(np.argsort(pts_[:, 1]))
    Cf = C.astype(np.float32)
    btw = np.rint(Cf @ Cf).astype(np.int32)
    ii, jj = np.nonzero(C)
    dr1 = (r1[jj] - r1[ii]).astype(float)
    dr2 = (r2[jj] - r2[ii]).astype(float)
    exp_k = (dr1 - 1) * (dr2 - 1) / Np
    sel = exp_k >= kmin
    resid = btw[ii, jj][sel] - exp_k[sel]
    return float(np.mean(resid ** 2 / exp_k[sel]))


# =========================== CHECK 1: the telescope exactness lemma
print("CHECK 1: growth telescope — summed exact increments == j2's action()")
n0 = 48
C0, S_tel, _ = grow(n0, beta=0)
S_dir = action(C0)
ok = abs(S_tel - S_dir) < 1e-6
check("S telescopes exactly over arrivals (every pair's interval is complete "
      "at its top element's arrival — maximality) — the exact-Phi arm is "
      "validated against j2's action verbatim", ok,
      f"telescope {S_tel:.6f} vs direct {S_dir:.6f}")

# =========================== CHECK 2: the sprinkling reference + j2 anchors
print("CHECK 2: same-n sprinkling ensemble + the j2 anchors (n = 64)")
n = 64
spr = []
for _ in range(12):
    Cs = dominance_order(rng.random((n, 2)))
    r_, H_ = descriptors(Cs)
    spr.append((action(Cs), r_, H_))
S_spr = float(np.mean([s[0] for s in spr])); S_sd = float(np.std([s[0] for s in spr]))
r_spr = float(np.mean([s[1] for s in spr])); r_sd = float(np.std([s[1] for s in spr]))
H_spr = float(np.mean([s[2] for s in spr])); H_sd = float(np.std([s[2] for s in spr]))
print(f"      sprinkling n = 64: S = {S_spr:.1f} +/- {S_sd:.1f}, r = {r_spr:.3f} "
      f"+/- {r_sd:.3f}, H = {H_spr:.1f} +/- {H_sd:.1f}")
ok = abs(S_spr - 175.6) < 4 * max(S_sd, 6.2)
check("fresh-stream sprinkling S reproduces j2's published ensemble "
      "(175.6 +/- 6.2) within 4 combined sd", ok, f"S = {S_spr:.1f}")

# =========================== CHECK 3: the beta grid at n = 64 (Arm A core)
print("CHECK 3: Arm A — growth endpoints across beta, n = 64, 3 replicates")
print("      arm                     S        r       H    dim<=2")
res = {}
for tag, beta in (("beta=0 (kernel ctrl)", 0), ("beta=1", 1.0),
                  ("beta*=11.09", BETA_STAR), ("beta=inf (argmin)", None)):
    rows = []
    for _ in range(3):
        C, S, _ = grow(n, beta)
        r_, H_ = descriptors(C)
        d2 = dim_le_2_capped(C)
        rows.append((S, r_, H_, d2))
    S_m = float(np.mean([x[0] for x in rows]))
    r_m = float(np.mean([x[1] for x in rows]))
    H_m = float(np.mean([x[2] for x in rows]))
    d2s = ",".join({True: "Y", False: "N", None: "U"}[x[3]] for x in rows)
    res[tag] = (S_m, r_m, H_m, [x[3] for x in rows])
    print(f"      {tag:<22} {S_m:7.2f}  {r_m:.3f}  {H_m:5.1f}   {d2s}")

# [pinned-post-exploration] the exploration pass measured: beta = 0 kernel
# S = 187.8, r = 0.601, H = 19.7; the beta axis collapses FAST — already at
# beta = 1 the endpoints are deeply sparse (S = 29.7, r = 0.059), beta* gives
# a near-antichain (S = 0.58, r = 0.001, H = 2), and beta = inf reaches the
# EXACT degenerate minimum: S = 0.000, r = 0.000, H = 1 — the literal
# antichain, the pre-registered prediction realized at full strength, and
# the OPPOSITE sign of j2's equilibrium attractor (r ~ 0.78 dense).
ok = (res["beta=inf (argmin)"][1] < 0.25 and
      res["beta=inf (argmin)"][0] < 0.15 * S_spr and
      res["beta=0 (kernel ctrl)"][1] > 0.4)
check("THE PREDICTION HOLDS: argmin growth drives toward the action's "
      "degenerate sparse minimum (r < 0.25, S < 0.15x sprinkling) while the "
      "beta = 0 kernel sits mid-density — growth INVERTS j2's dense failure "
      "mode; the bare r+link action lacks a comparability-forcing term in "
      "BOTH sampling modes", ok,
      f"r: {res['beta=0 (kernel ctrl)'][1]:.2f} -> "
      f"{res['beta=inf (argmin)'][1]:.2f}; S: "
      f"{res['beta=0 (kernel ctrl)'][0]:.1f} -> {res['beta=inf (argmin)'][0]:.2f}")
ok = not any(abs(res[t][1] - 0.78) < 0.08 and res[t][2] >= 12
             for t in res)
check("NO arm reproduces j2's dense equilibrium attractor (r ~ 0.78, tall) — "
      "the dense compromise is a property of the equilibrium kernel/landscape "
      "pair, unreachable by monotone growth from below at any tested beta", ok)

# =========================== CHECK 4: the G1 trichotomy verdict, stated
print("CHECK 4: the G1 trichotomy verdict at n = 64 (note 8 §4)")
# escape = in sprinkling class (r, H within 3 sd, dim<=2 not-NO);
# capture = j2 attractor class (r >= 0.7 tall); pathology = r <= 0.15 or H <= 2.
verdicts = {}
for t in res:
    S_m, r_m, H_m, d2l = res[t]
    if abs(r_m - r_spr) < 3 * r_sd and abs(H_m - H_spr) < 3 * H_sd and \
       all(d is not False for d in d2l):
        v = "ESCAPE"
    elif r_m >= 0.7 and H_m >= 12:
        v = "CAPTURE"
    elif r_m <= 0.15 or H_m <= 2:
        v = "PATHOLOGY(sparse)"
    else:
        v = "OTHER"
    verdicts[t] = v
    print(f"      {t:<22} -> {v}")
# [pinned-post-exploration]: beta in {1, beta*, inf} ALL land
# PATHOLOGY(sparse) — the collapse onset is below beta = 1 — and beta = 0 is
# OTHER (mid-density kernel class); no ESCAPE, no CAPTURE anywhere on the
# grid: the third outcome, in the sparse direction, as pre-registered.
ok = (verdicts["beta=inf (argmin)"].startswith("PATHOLOGY") and
      "CAPTURE" not in verdicts.values() and
      "ESCAPE" not in verdicts.values())
check("the trichotomy resolves to the third outcome (sparse pathology at "
      "beta = inf; neither escape nor capture on the grid) — the measured "
      "G1 verdict: the sampling mode changes WHICH degenerate class wins, "
      "not whether one does; the missing abundance term is now localized "
      "from both sides", ok, "; ".join(f"{k}: {v}" for k, v in verdicts.items()))

# =========================== CHECK 5: kernel ablation (the empty candidate)
print("CHECK 5: kernel ablation — remove the empty candidate (n = 64, beta = inf)")
rows = []
for _ in range(3):
    C, S, _ = grow(n, None, include_empty=False)
    r_, H_ = descriptors(C)
    rows.append((S, r_))
S_ne = float(np.mean([x[0] for x in rows])); r_ne = float(np.mean([x[1] for x in rows]))
print(f"      no-empty argmin: S = {S_ne:.2f}, r = {r_ne:.3f} "
      f"(with-empty: S = {res['beta=inf (argmin)'][0]:.2f}, "
      f"r = {res['beta=inf (argmin)'][1]:.3f})")
# [pinned-post-exploration]: removing the empty candidate does NOT rescue the
# arm — argmin still selects the sparsest proposals (measured S = 8.33,
# r = 0.017): the sparse pull is the ACTION's, not the kernel's escape hatch.
ok = r_ne < 0.3
check("the sparse drift survives the kernel ablation — the degenerate pull "
      "is attributable to the action (its minimum), not to the empty-move "
      "escape hatch (note 8 §5 risk 1 discharged for this arm)", ok,
      f"r = {r_ne:.3f}")

# =========================== CHECK 6: Arm B — victim-selection laws, N = 512
print("CHECK 6: Arm B — Phi_rank victim selection at N = 512, M = 32, L = 2")
N, M, L = 512, 32, 2
faith = [star_disc(rank_embed2(*(lambda p: (p[:, 0], p[:, 1]))(rng.random((N, 2)))))
         for _ in range(20)]
Df, Dsd = float(np.mean(faith)), float(np.std(faith))
ens = [interval_fano(np.argsort(np.argsort(p[:, 0])), p[:, 1])
       for p in (rng.random((N, 2)) for _ in range(16))]
mu_f, sd_f = float(np.mean(ens)), float(np.std(ens))
print(f"      band {Df:.4f} +/- {Dsd:.4f}; fano ensemble {mu_f:.3f} +/- {sd_f:.3f}")
print("      law                D*       ratio   |rho|    fano     z     L_eff")
brows = {}
for tag, bv in (("beta_v=0 (uniform)", 0), ("beta_v=4", 4.0),
                ("beta_v=inf (leader)", None)):
    ds, rs, fs, lts = [], [], [], []
    for _ in range(6):
        b, c, lt = web_law(N, M, L, bv)
        ds.append(star_disc(rank_embed2(b, c)))
        rs.append(spearman_ties(b, c))
        fs.append(interval_fano(b, c))
        lts += lt
    D_, rho_, f_ = float(np.mean(ds)), float(np.mean(np.abs(rs))), float(np.mean(fs))
    z_ = abs(f_ - mu_f) / max(sd_f, 1e-12)
    Le = float(np.mean(lts))
    brows[tag] = (D_, rho_, f_, z_, Le)
    print(f"      {tag:<18} {D_:.4f}  {D_/Df:5.2f}x  {rho_:.3f}   {f_:.3f}  "
          f"{z_:5.1f}   {Le:.2f}")
# [pinned-post-exploration]: the exploration pass measured a DIRECTIONAL
# improvement on ALL THREE layers from uniform to kill-the-leader —
# D* 1.50x -> 1.29x, |rho| 0.122 -> 0.057, z 1.9 -> 0.6 — magnitude ~1
# band-sd on D* at 6 seeds (single stream; DISCLOSED as directional, not
# certified), with no layer degraded anywhere on the beta_v grid.
ok = all(v[0] < 2.0 * Df and v[1] < 0.15 for v in brows.values())
check("all victim-selection laws remain in the corner's range (D* < 2x band, "
      "|rho| < 0.15) — cell membership is robust across beta_v", ok)
lead, unif = brows["beta_v=inf (leader)"], brows["beta_v=0 (uniform)"]
ok = lead[0] <= unif[0] and lead[1] <= unif[1] and lead[3] <= unif[3]
check("kill-the-leader improves (weakly) on EVERY layer vs the uniform "
      "kernel — the first measured beta_v > 0 selection signal, directional "
      "grade (magnitude ~1 sd on D* at this seed count, disclosed; a "
      "certification claim would need the N = 2048 / more-seed retest)", ok,
      f"D* {unif[0]/Df:.2f}x -> {lead[0]/Df:.2f}x; |rho| {unif[1]:.3f} -> "
      f"{lead[1]:.3f}; z {unif[3]:.1f} -> {lead[3]:.1f}")

# =========================== CHECK 7: G3 — endogenous lifetime accounting
print("CHECK 7: G3 — the realized-lifetime law under Phi_rank")
lam0, lamL = brows["beta_v=0 (uniform)"][4], brows["beta_v=inf (leader)"][4]
ok = abs(lam0 - L) < 0.6
check("uniform victim reproduces L_eff = L (the exogenous anchor)", ok,
      f"L_eff = {lam0:.2f}")
# HONESTY CORRECTION (main-loop, caught at the exploration pass): the note's
# G3 phrasing "endogenous lifetime" over-claims for THIS law class — with the
# churn-EVENT rate fixed at 1/L per commit, the mean lifetime in own-commit
# units is pinned by accounting (deaths ~ N/L over N commits, so
# E[L_eff] ~ L/(1 + LM/N) for EVERY victim law; measured 1.73 and 1.92, both
# ~ the identity's value). What the victim law shapes is the lifetime
# DISTRIBUTION at fixed mean. Full endogenization of L needs law-driven
# event RATES — a different (and corpus-riskier, C1-adjacent) design,
# deferred and named. The gate below asserts the identity, not a selection.
ok = 1.0 <= lamL <= 4.0 and abs(lamL - lam0) < 1.0
check("the accounting identity holds: E[L_eff] is budget-pinned near L for "
      "every victim law (the victim choice reshapes the lifetime "
      "distribution, not its mean) — the note's G3 'endogenous L' claim is "
      "CORRECTED to distribution-level for fixed-event-rate laws", ok,
      f"L_eff uniform {lam0:.2f}, leader {lamL:.2f} (identity ~ "
      f"{L/(1+L*M/N):.2f} completed-lineage value; windowed census "
      f"length-bias per j5 applies)")

# ------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
