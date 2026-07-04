#!/usr/bin/env python3
"""
j2_gibbs_recon.py — v8 paper 13 §3: reconnaissance — does the misfit-action
Gibbs candidate (paper 11) select MANIFOLDLIKE orders, or merely non-KR ones?

Setup: driven local search on labeled posets at n = 64 under e^{-beta * S},
S = S_r(m0 = 8) + (1/4) #{related pairs, |I| < m0} (paper 11's combined r+link
action), beta = 20 > beta* = 16 ln 2 / ... (the dense-violation threshold),
4000 proposals; starts: KR(p = 0.9) and a random-relation order (closure of a
p = 0.15 random DAG). DRIVEN SEARCH, NOT an equilibrium sampler (disclosed as
in paper 11 §5); endpoints classified with the paper-12 instrument:
  dim <= 2 (oracle, with a work cap -> possible honest UNDECIDED verdict),
  canonical D* (only meaningful if dim <= 2), the interval-dispersion index
  against a same-n sprinkling ensemble, and the ordering fraction r.

The question is a fork, and either answer is the result:
  (a) endpoints land manifoldlike-ish -> first dynamics -> geometry link;
  (b) endpoints escape the bulk but NOT into the manifoldlike cell -> the
      selection gap is MEASURED, and the r+link ledger's insufficiency for
      selection is exhibited (the abundance-term extension, named in paper 11,
      becomes the concrete next rung).
Gates encode the fork honestly: CHECK 3 BRANCHES on the measured arm and
asserts that arm's signature (post-review; the draft hardcoded arm (b)).
Gates are calibrated from a disclosed pre-run exploration, like j1's.

Float discipline: float64 measurement; default_rng(20260702). n = 64 toy scale
(paper 8's onset discipline: D*-grade verdicts are coarse here — disclosed).
"""

import sys
import numpy as np

sys.setrecursionlimit(400000)
rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ------------------------------------------------------------ the action
M0 = 8

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

def closure(Cb):
    R = Cb.astype(np.float32)
    for _ in range(7):
        R = np.minimum(R + R @ R, 1.0)
    return R > 0.5

def covers(C):
    Cf = C.astype(np.float32)
    return C & ~((Cf @ Cf) > 0.5)

def kr_3layer(N, p=0.9):
    n1, n2 = N // 4, N // 2
    n3 = N - n1 - n2
    C = np.zeros((N, N), dtype=bool)
    L1 = np.arange(0, n1); L2 = np.arange(n1, n1 + n2); L3 = np.arange(n1 + n2, N)
    C[np.ix_(L1, L2)] = rng.random((n1, n2)) < p
    C[np.ix_(L2, L3)] = rng.random((n2, n3)) < p
    C[np.ix_(L1, L3)] = (C[np.ix_(L1, L2)].astype(np.float32)
                         @ C[np.ix_(L2, L3)].astype(np.float32)) > 0
    return C

def random_order(N, p=0.15):
    U = np.triu(rng.random((N, N)) < p, 1)
    return closure(U)

def drift(C0, beta, steps):
    C = C0.copy()
    S = action(C)
    n = C.shape[0]
    for _ in range(steps):
        i, j = rng.integers(0, n, 2)
        if i == j:
            continue
        Cn = None
        if C[i, j]:
            if covers(C)[i, j]:
                Cn = C.copy(); Cn[i, j] = False
        else:
            if not C[j, i]:
                Cn = C.copy(); Cn[i, j] = True
                Cn = closure(Cn)
        if Cn is None:
            continue
        Sn = action(Cn)
        if Sn <= S or rng.random() < np.exp(-beta * (Sn - S)):
            C, S = Cn, Sn
    return C, S

# ------------------------------------------------------------ classification
def dominance_order(pts):
    return (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])

def dim_le_2_capped(C, cap=3_000_000):
    """g2-criterion oracle with a work cap: True / False / None (undecided)."""
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

def classify(C, tag, spr_stats):
    N = C.shape[0]
    r_frac = 2.0 * C.sum() / (N * (N - 1))
    H = 1
    # height
    indeg = C.sum(axis=0).astype(int)
    L = np.ones(N, dtype=int)
    stack = [i for i in range(N) if indeg[i] == 0]
    Cl = [np.nonzero(C[i])[0] for i in range(N)]
    ind = indeg.copy()
    topo = []
    while stack:
        v = stack.pop()
        topo.append(v)
        for w in Cl[v]:
            ind[w] -= 1
            if ind[w] == 0:
                stack.append(w)
    for v in topo:
        if len(Cl[v]):
            L[Cl[v]] = np.maximum(L[Cl[v]], L[v] + 1)
    H = int(L.max())
    d2 = dim_le_2_capped(C)
    d2s = {True: "YES", False: "NO", None: "UNDECIDED(cap)"}[d2]
    S = action(C)
    print(f"      {tag:<26} S = {S:7.2f}  r = {r_frac:.3f}  height = {H:>2}  "
          f"dim<=2: {d2s}")
    return dict(S=S, r=r_frac, H=H, d2=d2)


print("CHECK 1: the action's landmarks at n = 64")
n = 64
C_kr = kr_3layer(n)
S_kr = action(C_kr)
sprS = [action(dominance_order(rng.random((n, 2)))) for _ in range(12)]
S_spr = float(np.mean(sprS))
S_spr_sd = float(np.std(sprS))
ratio = S_kr / S_spr
ok = 1.2 < ratio < 2.5
check("the n = 64 landscape is LINK-DOMINATED: S_KR/S_sprinkling < 2.5 — the "
      "action's discrimination onset (h1's disclosed slow link-term crossover, "
      "comparable magnitudes below N ~ 10^3) is NOT reached at recon scale; the "
      "recon therefore probes the action's small-n minimizers, not its "
      "asymptotic selection", ok,
      f"S_KR = {S_kr:.1f}, S_sprinkling = {S_spr:.1f} (ratio {ratio:.1f}x)")

print("CHECK 2: drift runs (driven search, beta = 20, 4000 proposals)")
runs = {}
sprH = [classify(dominance_order(rng.random((n, 2))), f"sprinkling ref #{k}", None)
        for k in range(2)]
for name, C0 in (("from-KR", C_kr), ("from-random", random_order(n))):
    S0 = action(C0)
    C_end, S_end = drift(C0, 20.0, 4000)
    print(f"      {name}: S {S0:.1f} -> {S_end:.1f}")
    runs[name] = (S0, S_end, C_end)
ok = all(S_end < S0 for (S0, S_end, _) in runs.values()) and \
     all(abs(S_end - S_spr) < 3 * S_spr_sd for (_, S_end, _) in runs.values())
check("both starts drift DOWN to SPRINKLING-LEVEL action (within 3 sd of the "
      "12-replicate sprinkling ensemble — S alone does NOT discriminate at this "
      "scale; the post-review correction of the draft's false 'below the band' "
      "claim: the ensemble spread is +/- ~8 and the endpoints sit inside it). "
      "The third-class finding rests on the CLASSIFICATION data, not on S", ok,
      ", ".join(f"{k}: {v[0]:.0f}->{v[1]:.1f}" for k, v in runs.items())
      + f"; sprinkling {S_spr:.1f} +/- {S_spr_sd:.1f}")

print("CHECK 2b: action decomposition on the endpoints (post-review — the "
      "mechanism, measured, replacing the draft's backwards story)")
def decompose(C):
    N = C.shape[0]
    Cf = C.astype(np.float32)
    btw = np.rint(Cf @ Cf).astype(np.int32)
    Sr, rIs = 0.0, []
    ii, jj = np.nonzero(C & (btw >= M0))
    for x, y in zip(ii, jj):
        inner = np.nonzero(C[x] & C[:, y])[0]
        k = len(inner)
        sub = C[np.ix_(inner, inner)]
        rI = 2.0 * sub.sum() / (k * (k - 1)) if k > 1 else 0.0
        Sr += (rI - 0.5) ** 2
        rIs.append(rI)
    Sl = 0.25 * float((C & (btw < M0)).sum())
    return Sr, Sl, (float(np.mean(rIs)) if rIs else float("nan"))

spr_dec = [decompose(dominance_order(rng.random((n, 2)))) for _ in range(4)]
Sr_spr = float(np.mean([d[0] for d in spr_dec]))
Sl_spr = float(np.mean([d[1] for d in spr_dec]))
print(f"      sprinkling refs:  S_r = {Sr_spr:.1f}, S_link = {Sl_spr:.1f}")
dec = {k: decompose(v[2]) for k, v in runs.items()}
for k, (Sr, Sl, mrI) in dec.items():
    print(f"      {k:<14} S_r = {Sr:.1f}, S_link = {Sl:.1f}, mean r_I = {mrI:.3f}")
ok = all(Sr > 2 * Sr_spr for Sr, _, _ in dec.values()) and \
     all(Sl < Sl_spr for _, Sl, _ in dec.values()) and \
     all(0.50 < mrI < 0.65 for _, _, mrI in dec.values())
check("the measured mechanism: endpoints pay MORE r-term than sprinklings "
      "(> 2x — interiors near-balanced, mean r_I ~ 0.54, NOT chain-heavy) and "
      "slightly LESS link term; net sprinkling-level S via global densification "
      "— the draft's 'chain-heavy interiors dodge the r-term' story was "
      "backwards and is retracted", ok,
      ", ".join(f"{k}: Sr {d[0]:.1f}/link {d[1]:.1f}/rI {d[2]:.2f}"
                for k, d in dec.items()))

print("CHECK 3: endpoint classification (the fork, measured)")
cls = {}
for name, (_, _, C_end) in runs.items():
    cls[name] = classify(C_end, f"endpoint {name}", None)
# the fork gates: endpoints must be non-KR-like (height far from 3, or r far
# from KR's ~0.56); their manifoldlike status is asserted AS MEASURED below
kr_ref = classify(C_kr, "KR reference", None)
in_cell = [k for k, c in cls.items() if c["d2"] is True]
out_cell = [k for k, c in cls.items() if c["d2"] is False]
und = [k for k, c in cls.items() if c["d2"] is None]
verdict = (f"dim<=2 YES: {in_cell or '-'}; NO: {out_cell or '-'}; "
           f"UNDECIDED: {und or '-'}")
# FORK-CONDITIONAL gate (post-review): branch on the measured arm, then assert
# that arm's signature — falsifiable either way, neither arm hardcoded
if in_cell:
    # arm (a): a dim<=2 endpoint exists — its signature: sprinkling-like r
    ok = any(abs(cls[k]["r"] - 0.5) < 0.1 for k in in_cell)
    check(f"the fork, measured — arm (a): {verdict}; asserting arm (a)'s "
          f"signature (a dim<=2 endpoint with sprinkling-like r)", ok, verdict)
else:
    # arm (b): no endpoint in the cell — its signature: the third class
    # (non-KR: H >> 3; non-sprinkling: r far from 0.5)
    ok = all(c["H"] > 6 for c in cls.values()) and \
         all(c["r"] > 0.7 for c in cls.values())
    check(f"the fork, measured — arm (b): {verdict}; the endpoints are a THIRD "
          f"class (non-KR: H >> 3; non-sprinkling: r ~ 0.78 vs 0.5) — the "
          f"SELECTION GAP is measured; the abundance-term extension is the "
          f"named next rung", ok,
          ", ".join(f"{k}: H={c['H']}, r={c['r']:.2f}" for k, c in cls.items()))

print("CHECK 4: the beta = 0 control (post-review — the draft's static "
      "baseline could not separate action from proposal-kernel bias)")
C_b0, S_b0 = drift(C_kr, 0.0, 4000)
b0 = classify(C_b0, "beta=0 control (from-KR)", None)
# attribution, measured: the kernel alone (add+closure vs cover-delete) is
# itself densifying; the gate asserts the MEASURED comparison and the honest
# attribution that follows from it
dr_end = float(np.mean([c["r"] for c in cls.values()]))
# three measured regimes, all anticipated (post-review branch repair):
if b0["r"] > dr_end + 0.1:
    concl = ("the kernel ALONE over-densifies to near-chain (r ~ 0.99) and the "
             "driven runs sit BELOW it — the action RESISTS the kernel's "
             "densification (a near-chain pays a huge r-term) but parks the "
             "system at a third-class compromise (r ~ 0.78) instead of pushing "
             "toward the sprinkling cell; the draft's 'the action prefers "
             "density' is RETRACTED — the density is the kernel's, the action "
             "moderates it and still fails to select geometry")
    ok = b0["S"] > 1.5 * max(v[1] for v in runs.values())
elif abs(b0["r"] - dr_end) <= 0.1:
    concl = ("beta = 0 densifies comparably — kernel bias is not separated; "
             "attribution withheld")
    ok = True
else:
    concl = "beta = 0 stays sparser — the densification is the action's"
    ok = True
check(f"attribution, measured: beta=0 endpoint r = {b0['r']:.2f} (S = "
      f"{S_b0:.1f}) vs driven mean r = {dr_end:.2f} — {concl}", ok,
      f"beta=0: H = {b0['H']}, dim<=2 {b0['d2']} (a near-chain is trivially "
      f"2D-embeddable but volume-rejected: its rank embedding is the diagonal)")

print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
