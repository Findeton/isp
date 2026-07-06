#!/usr/bin/env python3
"""
ml1_seal_field_toy.py — v9 round 3, Tier-7 rung 1 (PLAN T7.1): the seal-
field coupling toy. A Gaussian field on the record order's comparability
graph, coupled at seals; the derived two-party object chi_AB^derived =
cross-chain covariance of field-modulated content. THE QUESTION: does a
FIELD-MEDIATED record-side quantity (an independent random object whose
covariance is order-mediated — new degrees of freedom, the matter-locus
mechanism in miniature) carry the transverse geometry?

PRE-REGISTERED GATES (PLAN T7.1; both directions live):
  G1 field sanity: graph-covariance decays with hop distance on the
     comparability graph (Spearman < -0.5).
  G2 chi_AB^derived decays with TRANSVERSE distance (Spearman < -0.5) —
     the geometric content, without any geometry in the construction.
  G3 the geometry face: MDS(chi_AB^derived) closes the transverse plane at
     Procrustes >= 0.85 (w-benchmark printed beside; the M6 caveat is
     SOFTENED, not removed: the field is order-mediated).
  G4 shuffle void: shuffled chi_AB destroys the closure (per-fleet z > 3
     vs a 24-draw shuffle null).
KILL (PLAN T7.1): G1/G2 fail => the field-mediation shape is wrong —
redirect to rung 3 directly. Grade ceiling [SCOUT -> DEMONSTRATED-toy].
Construction (SECOND EXECUTION, iteration disclosed): the first execution
mediated the field on the FULL COMPARABILITY graph and G2-G4 REFUSED
(Spearman -0.03, Procrustes 0.15) with G1 passing — diagnosis: the
comparability graph is a small-world (any two chains meet through common
ancestors in ~2 hops), so Laplacian-inverse covariance is nearly flat
across chain pairs and the transverse signal washes out. THE RECORDED
NEGATIVE (kept as an arm below): full-causal-graph mediation carries no
geometry — a genuine constraint on rung-3 designs: THE MATTER COUPLING
MUST BE LOCAL (cover-grade). The executed construction: field ~
N(0, (L_Hasse + 0.1 I)^-1) on the HASSE diagram (covering relations only
— the local links); pure field coupling (content c_i = 1 + phi_i; the
first run's sigma-modulation added independent noise, dropped); chi_AB = the
EXACT cross-chain covariance of the coupled content — analytically equal
to the chain-averaged field covariance mean_{i in A, j in B} Cov[i, j]
(THIRD-EXECUTION estimator correction, disclosed: the R = 96 Monte-Carlo
covariance layer was pure estimator noise — Procrustes 0.50 at R = 96 —
and the toy has the analytic value available; the |abs| rectifier is
dropped with it). Iteration ledger, all recorded, WITH THE ROUND-3 REVIEW'S CORRECTION:
(1) comparability-graph + MC estimator REFUSED (Spearman -0.03) [logged,
unreceipted]; (2) Hasse + MC partially closed (0.50, shuffle-z 4.4)
[logged, unreceipted]; (3) Hasse + exact = an executed arm; (4) THE
REVIEW'S 2x2 CELL, adopted as an executed arm: comparability + exact
ALSO CLOSES (Procrustes ~0.999) — the first draft changed graph and
estimator together and mis-attributed the failure to the graph. THE
"COUPLING MUST BE LOCAL" CONSTRAINT IS RETRACTED; the supported form:
full-causal mediation carries the geometry at ~7x SMALLER relative
amplitude (std/mean ~0.14% vs Hasse ~1%), so LOCALITY BUYS PER-
REALIZATION ESTIMABILITY (finite-sample robustness), not geometry-in-
principle. GATE PROVENANCE (review M2, disclosed): PLAN T7.1 registered
(i) hop-decay, (ii) E_cl-shaped magnitude structure, (iii) Procrustes
>= 0.85; the executed G2 (transverse-distance decay) and G4 (shuffle)
are substitutions/additions; gate (ii) — the magnitude-structure gate —
is DEFERRED to rung 2 with reason (the toy's field is Gaussian by
construction; the magnitude question is live only for the derived-field-
into-n3 form). Seed 20260707; float64.
"""
import numpy as np

rng = np.random.default_rng(20260707)
PASS = FAIL = 0
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
        t = rng.uniform(-1, 1, m); x = rng.uniform(-1, 1, m); y = rng.uniform(-1, 1, m)
        keep = np.hypot(x, y) <= 1 - np.abs(t)
        pts = np.vstack([pts, np.column_stack([t, x, y])[keep]])
    return pts[:N]

def order_3d(P):
    dt = P[None, :, 0] - P[:, None, 0]
    dr = np.hypot(P[None, :, 1] - P[:, None, 1], P[None, :, 2] - P[:, None, 2])
    return (dt > 0) & (dt > dr)

def longest_chain(C, alive):
    idx = np.nonzero(alive)[0]
    if len(idx) == 0: return []
    sub = C[np.ix_(idx, idx)]
    n = len(idx)
    indeg = sub.sum(axis=0).astype(int)
    Lv = np.ones(n, dtype=int); par = -np.ones(n, dtype=int)
    stack = [i for i in range(n) if indeg[i] == 0]
    ind = indeg.copy()
    succ = [np.nonzero(sub[i])[0] for i in range(n)]
    while stack:
        v = stack.pop()
        for w_ in succ[v]:
            if Lv[v] + 1 > Lv[w_]:
                Lv[w_] = Lv[v] + 1; par[w_] = v
            ind[w_] -= 1
            if ind[w_] == 0: stack.append(int(w_))
    end = int(np.argmax(Lv)); ch = []
    v = end
    while v != -1:
        ch.append(int(idx[v])); v = int(par[v])
    return ch[::-1]

def spearman(a, b):
    def ar(v):
        o = np.argsort(v, kind="stable"); r = np.empty(len(v)); r[o] = np.arange(len(v))
        vals, inv = np.unique(v, return_inverse=True)
        s = np.bincount(inv, weights=r); c = np.bincount(inv)
        return (s / c)[inv]
    return float(np.corrcoef(ar(a), ar(b))[0, 1])

def mds_xy(AFF):
    M = len(AFF)
    DIS = AFF.max() - AFF
    np.fill_diagonal(DIS, 0.0)
    J = np.eye(M) - np.ones((M, M)) / M
    B = -0.5 * J @ (DIS ** 2) @ J
    ev, V = np.linalg.eigh(B)
    return V[:, -2:] * np.sqrt(np.maximum(ev[-2:], 0))

def procrustes_corr(A, Bm):
    A = A - A.mean(0); Bm = Bm - Bm.mean(0)
    U, s_, Vt = np.linalg.svd(A.T @ Bm)
    return float(np.corrcoef((A @ (U @ Vt)).ravel(), Bm.ravel())[0, 1])

N = 600
P = sprinkle_3d(N)
C = order_3d(P)
alive = np.ones(N, dtype=bool)
chains = []
while True:
    ch = longest_chain(C, alive)
    if len(ch) < 8 or len(chains) >= 24: break
    chains.append(ch); alive[ch] = False
M = len(chains)
tpos = np.array([[P[c, 1].mean(), P[c, 2].mean()] for c in chains])
print(f"[fleet: M = {M} chains on N = {N}]")

# the mediation graphs: comparability (the recorded-negative arm) and
# Hasse (the executed arm — covers only: x < y with empty open interval)
Cf32 = C.astype(np.float32)
btw_full = np.rint(Cf32 @ Cf32).astype(np.int32)
Hasse = C & (btw_full == 0)
A_comp = (C | C.T).astype(np.float64)
A_g = (Hasse | Hasse.T).astype(np.float64)
deg = A_g.sum(1)
Lg = np.diag(deg) - A_g
Cov = np.linalg.inv(Lg + 0.1 * np.eye(N))
Ch = np.linalg.cholesky(Cov + 1e-10 * np.eye(N))

# G1: covariance decays with hop distance (sample pairs; BFS hops on graph)
from collections import deque
def hops_from(s, adj):
    d = np.full(N, -1); d[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] < 0:
                d[w] = d[v] + 1; q.append(w)
    return d
adj = [np.nonzero(A_g[i])[0] for i in range(N)]
src_nodes = rng.choice(N, 8, replace=False)
cov_s, hop_s = [], []
for s in src_nodes:
    d = hops_from(s, adj)
    tgt = rng.choice(N, 40, replace=False)
    for t_ in tgt:
        if d[t_] > 0:
            cov_s.append(Cov[s, t_]); hop_s.append(d[t_])
rho1 = spearman(np.array(cov_s), np.array(hop_s))
check("G1: the field's graph covariance decays with hop distance "
      "(Spearman < -0.5) — the mediation structure exists", rho1 < -0.5,
      f"Spearman = {rho1:+.3f} over {len(cov_s)} pairs")

# the derived chi_AB: the EXACT cross-chain coupled-content covariance
# (= chain-averaged field covariance; the analytic value of what the MC
# layer estimated — iteration 3, disclosed in the docstring)
chi_AB = np.zeros((M, M))
for i in range(M):
    for j in range(M):
        if i != j:
            chi_AB[i, j] = Cov[np.ix_(chains[i], chains[j])].mean()

iu = np.triu_indices(M, 1)
dt_true = np.hypot(tpos[:, 0, None] - tpos[None, :, 0], tpos[:, 1, None] - tpos[None, :, 1])
rho2 = spearman(chi_AB[iu], dt_true[iu])
check("G2 (Hasse-mediated): chi_AB^derived decays with the held-out "
      "TRANSVERSE distance (Spearman < -0.5) — the LOCAL field-mediated "
      "record side carries the geometric signal (the comparability-graph "
      "arm's recorded negative: -0.03)", rho2 < -0.5,
      f"Spearman = {rho2:+.3f}")

# G3: geometry closure + w benchmark
W = np.zeros((M, M))
for i in range(M):
    for j in range(i + 1, M):
        ci, cj = chains[i], chains[j]
        cross = C[np.ix_(ci, cj)].sum() + C[np.ix_(cj, ci)].sum()
        W[i, j] = W[j, i] = cross / (len(ci) * len(cj))
pc_w = procrustes_corr(mds_xy(W), tpos)
pc_f = procrustes_corr(mds_xy(chi_AB), tpos)
check("G3: MDS(chi_AB^derived) closes the transverse plane at Procrustes "
      ">= 0.85 (the matter-locus mechanism in miniature; M6 caveat "
      "softened — the field is order-mediated but an independent random "
      "object)", pc_f >= 0.85,
      f"derived-field {pc_f:.3f} vs w-benchmark {pc_w:.3f} (cost {pc_w-pc_f:+.3f})")

# the review's 2x2 cell: comparability graph + exact estimator (M1/M3)
Lc = np.diag(A_comp.sum(1)) - A_comp
Covc = np.linalg.inv(Lc + 0.1 * np.eye(N))
chi_c = np.zeros((M, M))
for i in range(M):
    for j in range(M):
        if i != j:
            chi_c[i, j] = Covc[np.ix_(chains[i], chains[j])].mean()
pc_c = procrustes_corr(mds_xy(chi_c), tpos)
amp_h = float(np.std(chi_AB[iu]) / np.mean(chi_AB[iu]))
amp_c = float(np.std(chi_c[iu]) / np.mean(chi_c[iu]))
check("the 2x2 cell (comparability + exact): full-causal mediation ALSO "
      "closes the geometry — the iteration-1 failure was the ESTIMATOR'S, "
      "not the graph's; the retained constraint is amplitude: locality "
      "buys ~7x relative signal (per-realization estimability), not "
      "geometry-in-principle (the review's correction, adopted)",
      pc_c >= 0.85 and amp_h > 2 * amp_c,
      f"comp+exact Procrustes = {pc_c:.3f}; rel-amp Hasse {amp_h:.3f} vs "
      f"comp {amp_c:.4f} ({amp_h/amp_c:.0f}x)")

# G4: shuffle void with 24-draw null
nulls = []
for _ in range(24):
    perm = rng.permutation(len(iu[0]))
    As = np.zeros_like(chi_AB)
    As[iu] = chi_AB[iu][perm]
    As = As + As.T
    nulls.append(procrustes_corr(mds_xy(As), tpos))
mu0, s0 = float(np.mean(nulls)), float(np.std(nulls, ddof=1))
z = (pc_f - mu0) / s0
check("G4: the shuffle void — the real closure exceeds the 24-draw shuffle "
      "null by > 3 sd (the geometry lives in the derived coupling)", z > 3,
      f"z = {z:.1f} (null {mu0:+.3f} +/- {s0:.3f})")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
