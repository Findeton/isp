#!/usr/bin/env python3
"""
k3_decoration_probe.py — v8 paper 14 §4: the decoration route's first rung —
does cross-chain coupling structure carry transverse geometry?

THE POSIT STACK (Attack 2, disclosed): records are DECORATED orders — chains
(worldline surrogates) with cross-chain coupling. SHARD's candidate carrier for
the missing transverse dimensions is the coupling structure (chi_AB, collar
sharing — paper 2's tensor locus). Before ANY record-native construction, the
principle must survive its geometric sanity test: ON FAITHFUL INPUT, does the
order-only cross-chain coupling statistic recover the held-out transverse
geometry? (If not, the decoration route dies here; if yes, the route's burden
moves to the record-native identification of the coupling — [POSITED].)

DESIGN (2+1D): sprinkle a 3D diamond; extract chains greedily (longest-chain
DP, keep length >= 8); coupling w(c, c') = cross-comparability fraction between
the chains' elements (ORDER-ONLY); dissimilarity 1 - w; classical MDS -> 2D;
score against the held-out chain-mean transverse positions via Procrustes
(rotation/reflection/scale-invariant correlation). Controls: (i) the coupling
must decrease with true transverse distance (the mechanism), (ii) a shuffled-
coupling control must destroy the recovery (the geometry lives in w, not in
the pipeline).

Float discipline: float64; default_rng(20260702). DEMONSTRATED grade.
"""

import numpy as np

rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


def sprinkle_3d(N):
    pts = np.empty((0, 3))
    while len(pts) < N:
        m = 4 * (N - len(pts)) + 64
        t = rng.uniform(-1, 1, m)
        x = rng.uniform(-1, 1, m)
        y = rng.uniform(-1, 1, m)
        keep = np.hypot(x, y) <= 1 - np.abs(t)
        pts = np.vstack([pts, np.column_stack([t, x, y])[keep]])
    return pts[:N]

def order_3d(P):
    dt = P[None, :, 0] - P[:, None, 0]
    dr = np.hypot(P[None, :, 1] - P[:, None, 1], P[None, :, 2] - P[:, None, 2])
    return (dt > 0) & (dt > dr)

def longest_chain(C, alive):
    """DP longest chain among alive elements; returns the chain as an index list."""
    idx = np.nonzero(alive)[0]
    if len(idx) == 0:
        return []
    sub = C[np.ix_(idx, idx)]
    n = len(idx)
    indeg = sub.sum(axis=0).astype(int)
    L = np.ones(n, dtype=int)
    par = -np.ones(n, dtype=int)
    stack = [i for i in range(n) if indeg[i] == 0]
    ind = indeg.copy()
    succ = [np.nonzero(sub[i])[0] for i in range(n)]
    topo = []
    while stack:
        v = stack.pop()
        topo.append(v)
        for w_ in succ[v]:
            if L[v] + 1 > L[w_]:
                L[w_] = L[v] + 1
                par[w_] = v
            ind[w_] -= 1
            if ind[w_] == 0:
                stack.append(int(w_))
    end = int(np.argmax(L))
    chain = []
    v = end
    while v != -1:
        chain.append(int(idx[v]))
        v = int(par[v])
    return chain[::-1]

# --------------------------------------------------------- build the probe
print("CHECK 1: chain extraction on faithful 3D input")
N = 600
P = sprinkle_3d(N)
C = order_3d(P)
alive = np.ones(N, dtype=bool)
chains = []
while True:
    ch = longest_chain(C, alive)
    if len(ch) < 8 or len(chains) >= 28:
        break
    chains.append(ch)
    alive[ch] = False
M = len(chains)
lens = [len(c) for c in chains]
ok = M >= 16 and min(lens) >= 8
check(f"greedy longest-chain decomposition yields a usable worldline-surrogate "
      f"fleet (M = {M} chains, lengths {min(lens)}-{max(lens)})", ok,
      f"covering {sum(lens)}/{N} elements")

# --------------------------------------------------------- the coupling
print("CHECK 2: the coupling mechanism — w decreases with transverse distance")
W = np.zeros((M, M))
for i in range(M):
    for j in range(i + 1, M):
        ci, cj = chains[i], chains[j]
        cross = C[np.ix_(ci, cj)].sum() + C[np.ix_(cj, ci)].sum()
        W[i, j] = W[j, i] = cross / (len(ci) * len(cj))
tpos = np.array([[P[c, 1].mean(), P[c, 2].mean()] for c in chains])
dt_true = np.hypot(tpos[:, 0, None] - tpos[None, :, 0],
                   tpos[:, 1, None] - tpos[None, :, 1])
iu = np.triu_indices(M, 1)
def spearman(a, b):
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    return float(np.corrcoef(ra, rb)[0, 1])
rho = spearman(W[iu], -dt_true[iu])
ok = rho > 0.6
check("cross-comparability fraction w(c, c') decreases with the held-out "
      "transverse distance (Spearman(w, -d) > 0.6) — the mechanism exists",
      ok, f"Spearman = {rho:.3f} over {len(iu[0])} chain pairs")

# --------------------------------------------------------- MDS recovery
print("CHECK 3: transverse geometry recovered by MDS + Procrustes")
DIS = 1.0 - W
np.fill_diagonal(DIS, 0.0)
J = np.eye(M) - np.ones((M, M)) / M
B = -0.5 * J @ (DIS ** 2) @ J
w_eig, V = np.linalg.eigh(B)
XY = V[:, -2:] * np.sqrt(np.maximum(w_eig[-2:], 0))

def procrustes_corr(A, Bm):
    A = A - A.mean(0); Bm = Bm - Bm.mean(0)
    U, s_, Vt = np.linalg.svd(A.T @ Bm)
    R = U @ Vt
    A_rot = A @ R
    return float(np.corrcoef(A_rot.ravel(), Bm.ravel())[0, 1])

pc = procrustes_corr(XY, tpos)
ok = pc > 0.8
check("MDS of the ORDER-ONLY coupling dissimilarity recovers the transverse "
      "plane (Procrustes correlation > 0.8 against held-out chain positions) — "
      "the decoration principle survives its geometric sanity test", ok,
      f"Procrustes corr = {pc:.3f} (M = {M} chains)")

# --------------------------------------------------------- shuffled control
print("CHECK 4: the shuffled-coupling control")
perm = rng.permutation(len(iu[0]))
Wp = np.zeros_like(W)
vals = W[iu][perm]
Wp[iu] = vals
Wp = Wp + Wp.T
DISp = 1.0 - Wp
np.fill_diagonal(DISp, 0.0)
Bp = -0.5 * J @ (DISp ** 2) @ J
wp, Vp = np.linalg.eigh(Bp)
XYp = Vp[:, -2:] * np.sqrt(np.maximum(wp[-2:], 0))
pcp = procrustes_corr(XYp, tpos)
ok = abs(pcp) < 0.4 and pc - abs(pcp) > 0.4
check("shuffling the coupling entries destroys the recovery (the geometry "
      "lives in w, not in the MDS pipeline)", ok,
      f"shuffled Procrustes corr = {pcp:.3f} vs real {pc:.3f}")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
