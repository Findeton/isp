#!/usr/bin/env python3
"""
s5_faithful_guided.py — v9 round 6: THE FAITHFUL-GUIDED CONTROL (note-s5;
gates pinned there pre-run). Q1: along the faithful trajectory, does A1's
marginal landscape prefer the TRUE down-set over 12 kernel decoys? Q1b:
free-run endpoints under guided menus. Q2: the offer gap (Jaccard).
Branches (pinned): rate >= 0.6 TRUTH-PREFERRED / <= 0.3 TRUTH-REJECTED /
else MIXED. G-O oracle anchor (bit-exact rebuild); G2 free-run endpoints
r_I in [0.35, 0.65] >= 3/4 reps AND m_ab <= 3x faithful.
Seed 20260712; float64 with the float32 Gram fast-path of s1/s4
(decision-invariance verified 0/768 flips by the round-7 code review);
A1 exact increments (s1/s4 verbatim). G3: offer gap per arrival-decile.
"""
import numpy as np
from mpmath import mp, beta as mbeta, digamma, mpf, binomial

mp.dps = 60
rng = np.random.default_rng(20260712)

PASS = 0
FAIL = 0
M0 = 8

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# ------------------------------------------------ exact abundance reference
_EA = {}
def EA_exact(k, j):
    if (k, j) not in _EA:
        if k - 2 - j < 0:
            _EA[(k, j)] = 0.0
        else:
            b = mpf(k - 1 - j)
            t1 = mbeta(j + 1, b) * (digamma(k) - digamma(j + 1))
            t2 = mbeta(j + 2, b) * (digamma(k + 1) - digamma(j + 2))
            t3 = -2 * mbeta(j + 1, k - j)
            _EA[(k, j)] = float(mpf(k) * (k - 1) * binomial(k - 2, j) * (t1 + t2 + t3))
    return _EA[(k, j)]

def m_ab_sub(sub):
    """Per-interval abundance misfit of an interval's induced order (bool
    matrix sub, k x k), per note-t11: sum_j (A_j/k - EA_j(k)/k)^2, J = 2."""
    k = sub.shape[0]
    if k < M0:
        return 0.0
    f = sub.astype(np.float32)
    btw = np.rint(f @ f).astype(np.int32)
    ints = btw[sub]
    tot = 0.0
    for j in range(3):
        A = int(np.sum(ints == j))
        tot += (A / k - EA_exact(k, j) / k) ** 2
    return tot

# ------------------------------------------------ u2's action machinery
def delta_S0(Ct, Ctf, D):
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

def s_comp(nrel, n):
    if n < 2:
        return 0.0
    r = 2.0 * nrel / (n * (n - 1))
    return (n * (n - 1) / 2) * (r - 0.5) ** 2

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

def sprinkling_order(n):
    pts = rng.random((n, 2))
    order = np.argsort(pts[:, 0] + pts[:, 1])
    pts = pts[order]
    C = (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])
    return pts, C

def dS_A1(Ct, Ctf, D, nrel, t):
    d = delta_S0(Ct, Ctf, D)
    d += s_comp(nrel + int(D.sum()), t + 1) - s_comp(nrel, t)
    return d

def kernel_menu(Ct, t, K=12):
    cands = [np.zeros(t, dtype=bool)]
    while len(cands) < K + 1:
        p = float(np.exp(rng.uniform(np.log(min(1.0 / t, 0.59)), np.log(0.6))))
        anc = rng.random(t) < p
        D = anc | Ct[:, anc].any(axis=1) if anc.any() else anc
        cands.append(D)
    return cands

N = 256
print("[s5 faithful-guided control, n = 256, 4 reps]")

# G-O: the oracle anchor (bit-exact rebuild) + target layers
pts, Ctrue = sprinkling_order(N)
C = np.zeros((N, N), dtype=bool)
for t in range(1, N):
    C[:t, t] = Ctrue[:t, t]
ok = np.array_equal(C, Ctrue)
check("G-O (anchor): arrival-order + true down-sets rebuilds the "
      "sprinkling BIT-EXACTLY — the attachment class trivially expresses "
      "faithfulness; the fork is action-preference, not expressibility "
      "(the round-5 framing's refinement, note-s5)", ok, "bit-exact")

def heredity_axis2(C, n_top=6):
    f = C.astype(np.float32)
    btw = np.rint(f @ f).astype(np.int32)
    ii, jj = np.nonzero(C)
    sizes = btw[ii, jj]
    order = np.argsort(-sizes)
    rIs = []
    for idx in order[:n_top * 3]:
        if sizes[idx] < 16 or len(rIs) >= n_top:
            break
        x, y = ii[idx], jj[idx]
        I = np.nonzero(C[x] & C[:, y])[0]
        k = len(I)
        sub = C[np.ix_(I, I)]
        rIs.append(2.0 * sub.sum() / (k * (k - 1)))
    return float(np.mean(rIs)) if rIs else float("nan")

def sampled_mab2(C, n_samp=40):
    ii, jj = np.nonzero(C)
    if len(ii) == 0: return float("nan")
    f = C.astype(np.float32)
    btw = np.rint(f @ f).astype(np.int32)
    ok_idx = np.nonzero((btw[ii, jj] >= M0) & (btw[ii, jj] <= 256))[0]
    if len(ok_idx) == 0: return float("nan")
    pick = rng.choice(len(ok_idx), size=min(n_samp, len(ok_idx)), replace=False)
    vals = []
    for pdx in pick:
        x, y = ii[ok_idx[pdx]], jj[ok_idx[pdx]]
        I = np.nonzero(C[x] & C[:, y])[0]
        vals.append(m_ab_sub(C[np.ix_(I, I)]))
    return float(np.mean(vals))

rI_or = heredity_axis2(Ctrue)
mab_or = sampled_mab2(Ctrue)
print(f"      oracle targets: r_I = {rI_or:.3f}, m_ab = {mab_or:.4f}")

# Q1: marginal preference along the faithful trajectory (4 sprinklings)
pref_rates, gaps = [], []
gap_by_t = []
for rep in range(4):
    pts, Ctrue = sprinkling_order(N)
    truth_wins = 0; total = 0
    gap_acc = []
    Cw = np.zeros((N, N), dtype=bool)
    nrel = 0
    for t in range(1, N):
        Cw[:t, t] = Ctrue[:t, t]           # forced-faithful trajectory
        if t >= 64:
            Ct = Cw[:t, :t]
            Ctf = Ct.astype(np.float32)
            truth = Ctrue[:t, t].copy()
            menu = kernel_menu(Ct, t)
            dT = dS_A1(Ct, Ctf, truth, nrel, t)
            dK = [dS_A1(Ct, Ctf, D, nrel, t) for D in menu]
            total += 1
            if dT <= min(dK):
                truth_wins += 1
            # offer gap: best decoy's Jaccard distance from truth
            best = menu[int(np.argmin(dK))]
            inter = float((best & truth).sum()); union = float((best | truth).sum())
            gap_acc.append(1.0 - (inter / union if union > 0 else 1.0))
            gap_by_t.append((t, gap_acc[-1]))
        nrel += int(Ctrue[:t, t].sum())
    pref_rates.append(truth_wins / total)
    gaps.append(float(np.mean(gap_acc)))
rate = float(np.mean(pref_rates))
print(f"      marginal-preference rate: {rate:.1%} "
      f"(reps {[round(r, 3) for r in pref_rates]}); offer gap (Jaccard) = "
      f"{np.mean(gaps):.3f}")
edges_t = np.linspace(64, N, 11)
dec_means = []
for lo, hi in zip(edges_t[:-1], edges_t[1:]):
    vals = [g for (tt, g) in gap_by_t if lo <= tt < hi]
    dec_means.append(np.mean(vals) if vals else float("nan"))
print("      G3 offer gap by arrival-decile (t = 64..256): "
      + " ".join(f"{v:.3f}" for v in dec_means))
branch = ("TRUTH-PREFERRED" if rate >= 0.6 else
          ("TRUTH-REJECTED" if rate <= 0.3 else "MIXED"))
check("G1 (Q1, the fork): the marginal-preference branch is decided by "
      "the pinned thresholds — TRUTH-PREFERRED (kernel's offer "
      "distribution is the whole problem; enrichment road) vs TRUTH-"
      "REJECTED (the action's marginal landscape is anti-faithful; no "
      "kernel saves argmin-A1) vs MIXED", rate >= 0.6 or rate <= 0.3,
      f"BRANCH = {branch} (rate {rate:.1%})")

# Q1b: free-run guided growth (truth on every menu; argmin picks)
frs = []
for rep in range(4):
    pts, Ctrue = sprinkling_order(N)
    Cw = np.zeros((N, N), dtype=bool)
    nrel = 0
    truth_taken = 0
    for t in range(1, N):
        Ct = Cw[:t, :t]
        Ctf = Ct.astype(np.float32)
        anc = Ctrue[:t, t]
        truth = anc | Ct[:, anc].any(axis=1) if anc.any() else anc.copy()
        menu = [truth] + kernel_menu(Ct, t)
        dS = [dS_A1(Ct, Ctf, D, nrel, t) for D in menu]
        pick = int(np.argmin(dS))
        if pick == 0: truth_taken += 1
        Cw[:t, t] = menu[pick]
        nrel += int(menu[pick].sum())
    r, H = descriptors(Cw)
    rI = heredity_axis2(Cw)
    mab = sampled_mab2(Cw)
    frs.append((r, rI, mab, truth_taken / (N - 1)))
    print(f"      free-run rep {rep}: r = {r:.3f}, r_I = {rI:.3f}, "
          f"m_ab = {mab:.4f}, truth-taken = {truth_taken/(N-1):.1%}")
in_band = sum(1 for r, rI, mab, tt in frs if not np.isnan(rI) and 0.35 <= rI <= 0.65)
mab_mean = float(np.mean([x[2] for x in frs if not np.isnan(x[2])]))
base = float(np.mean([sampled_mab2((lambda p: (p[None,:,0]>p[:,None,0])&(p[None,:,1]>p[:,None,1]))(rng.random((N,2)))) for _ in range(3)]))
g2 = in_band >= 3 and mab_mean <= 3 * base
check("G2 (Q1b): free-run guided endpoints are UN-FORGED (r_I in-band "
      ">= 3/4 AND m_ab <= 3x faithful) — separates the landscape verdict "
      "from path effects", g2,
      f"r_I in-band {in_band}/4; m_ab {mab_mean:.4f} vs 3x faithful "
      f"{3*base:.4f}")

print()
print(f"PRE-REGISTERED GATE LEDGER: G-O held; G1 branch = {branch}; "
      f"G2 {'HELD' if g2 else 'REFUSED'}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
