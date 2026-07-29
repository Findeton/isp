"""
v13 GW1 repair diagnostics.

Not a GW1 STEP 1-5 receipt: STEP 0 does not pass, so no closure relation is
solved anywhere here.  This file backs the two numeric statements the census
makes that no committed script prints:

  PART A -- the split of the record-native family into its TWO committed rules.
            (A1) pointwise-additive (code/v6_task2f_nogo_confirm.py:38-47):
                 state = threshold field T, J[N]: T -> T + s*N(x).  Invertible;
                 the pinned two-cell is formable and equals I.
            (A2) recomputed-height (code/v6_task2d_bracket_closure.py:30-36,
                 code/v6_task2f_nogo_confirm.py:56-58): state = down-set D,
                 J[N]: D -> D u {e : ha(e,D) < s*N(e)}.  A set union: monotone,
                 non-injective, no inverse.  Exhaustive down-set census on small
                 posets, swept over s.

  PART B -- the root cause of the disclosed v6_p2c PART 2 re-run drift.
            Reproduces code/v6_p2c_flow_drift.py PART 2 exactly (same seed, same
            construction) and instruments the slice-graph Laplacian consumed at
            its line 73 (`Lap = ...; _, V = eigh(Lap)`; `return V[:, 1]`):
            connected components, Laplacian nullity, spectrum; a 1e-13 symmetric
            perturbation sweep on the degenerate trial; and a 40-trial population
            reference at a declared seed.

Substrate: 1+1 flat sprinkling, 4000 events, slab |t| < 0.09, |x| < 2.2, kNN = 8
(all exactly as committed).  Caps: 60 perturbation draws, 40 population trials.
Anchors on committed numbers exit 1; substantive negatives exit 0.
Runtime ~ 20 s under code/.venv/bin/python3.13.
"""
import itertools
import sys

import numpy as np
from numpy.linalg import eigh
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

FAIL = []


def anchor(name, got, want, tol):
    ok = abs(got - want) <= tol
    print(f"    ANCHOR {name}: got {got:+.4f}  want {want:+.4f}  tol {tol}  -> {'OK' if ok else 'FAIL'}")
    if not ok:
        FAIL.append(name)


k = 1.3
N1 = lambda xx: 1.0 + 0.6 * np.cos(k * xx)
N2 = lambda xx: 1.0 + 0.6 * np.sin(k * xx)


def order_matrix(P):
    t, x = P[:, 0], P[:, 1]
    n = len(P)
    R = np.zeros((n, n), dtype=np.float32)
    for i in range(n):
        dt = t - t[i]
        R[i] = ((dt > 0) & (dt > np.abs(x - x[i]))).astype(np.float32)
    return R


# =====================================================================
# PART A1 -- pointwise-additive rule: invertible, two-cell = I
# =====================================================================
print("=" * 78)
print("A1  pointwise-additive rule (v6_task2f:38-47): T -> T + s*N(x)")
print("=" * 78)
rng = np.random.default_rng(2)
s = 8.0
for Nev in [2000, 4000, 8000]:
    P = np.column_stack([rng.uniform(-3.0, 3.0, Nev), rng.uniform(-3.0, 3.0, Nev)])
    R = order_matrix(P)
    x = P[:, 1]
    h = R.sum(axis=0)
    tau0 = np.quantile(h, 0.45)
    D0 = h <= tau0
    Dback = h <= (tau0 + s * N1(x) - s * N1(x))          # J[-N] J[+N]
    inv_ok = bool(np.array_equal(Dback, D0))
    D_NM = h <= (tau0 + s * N1(x) + s * N2(x))           # J[M|N] J[N]
    D_MN = h <= (tau0 + s * N2(x) + s * N1(x))           # J[N|M] J[M]
    sym = int(np.sum(D_NM ^ D_MN))
    print(f"  N={Nev:5d}  J[-N]J[+N] = id bitwise: {inv_ok}   "
          f"two-cell state difference (bits) = {sym}")
    if not inv_ok or sym != 0:
        FAIL.append(f"A1-N{Nev}")
print("  the three maps are additive translations of T, so Omega[N,M] = translation by")
print("  (sN + sM - sM - sN) = 0: the pinned two-cell is FORMABLE and equals I exactly.")

# =====================================================================
# PART A2 -- recomputed-height rule: non-injective, no inverse
# =====================================================================
print()
print("=" * 78)
print("A2  recomputed-height rule (v6_task2d:30-36): D -> D u {e : ha(e,D) < s*N(e)}")
print("=" * 78)


def step(D, R, x, lap, ss):
    notD = (~D).astype(np.float32)
    ha = R.T @ notD
    return D | ((~D) & (ha < lap(x) * ss))


def downsets_of(R, n):
    anc = [set(np.where(R[:, j] > 0)[0]) for j in range(n)]
    out = []
    for bits in itertools.product([False, True], repeat=n):
        D = np.array(bits)
        live = set(np.where(D)[0])
        if all((not D[j]) or anc[j] <= live for j in range(n)):
            out.append(D)
    return out


print(f"  {'|V|':>4} {'s':>5} | {'down-sets':>9} {'images':>7} {'collisions':>10} | injective")
for n, ss in [(9, 3.0), (10, 3.0), (11, 3.0), (12, 3.0)]:
    r = np.random.default_rng(7)
    P = np.column_stack([r.uniform(-3, 3, n), r.uniform(-3, 3, n)])
    R = order_matrix(P)
    x = P[:, 1]
    ds = downsets_of(R, n)
    img = {}
    for D in ds:
        img.setdefault(tuple(step(D, R, x, N1, ss).tolist()), []).append(0)
    coll = sum(len(v) - 1 for v in img.values())
    inj = len(img) == len(ds)
    print(f"  {n:>4} {ss:>5.2f} | {len(ds):>9} {len(img):>7} {coll:>10} | {inj}")
    if inj:
        FAIL.append(f"A2-inj-{n}")

r = np.random.default_rng(7)
P = np.column_stack([r.uniform(-3, 3, 12), r.uniform(-3, 3, 12)])
R = order_matrix(P)
x = P[:, 1]
ds = downsets_of(R, 12)
print("  s-sweep at |V| = 12 (non-injectivity is not a large-s artifact):")
for ss in [0.25, 0.5, 1.0, 2.0, 3.0, 6.0]:
    img = {}
    for D in ds:
        img.setdefault(tuple(step(D, R, x, N1, ss).tolist()), []).append(0)
    coll = sum(len(v) - 1 for v in img.values())
    grows = sum(1 for D in ds if step(D, R, x, N1, ss).sum() > D.sum())
    print(f"    s={ss:5.2f}  images={len(img):4d}  collisions={coll:4d}  "
          f"strictly-growing down-sets {grows}/{len(ds)}")
    if len(img) == len(ds):
        FAIL.append(f"A2-sweep-{ss}")

# =====================================================================
# PART B -- v6_p2c PART 2 drift: root cause
# =====================================================================
print()
print("=" * 78)
print("B  v6_p2c PART 2 reproduced and instrumented (seed 0, the committed loop)")
print("=" * 78)

Nl = lambda xx: 1.0 + 0.6 * np.cos(k * xx)
Ml = lambda xx: 1.0 + 0.6 * np.sin(k * xx)
d1 = lambda f, xx, hh=1e-4: (f(xx + hh) - f(xx - hh)) / (2 * hh)
xi = lambda xx: Nl(xx) * d1(Ml, xx) - Ml(xx) * d1(Nl, xx)


def build_W(P, R, A, delta):
    notslab = (P[:, 0] >= delta).astype(np.float32)
    ha = R.T @ notslab
    nA = len(A)
    Mt = np.full((nA, nA), np.inf)
    for ia, a in enumerate(A):
        Ra = R[a] > 0
        for ib in range(ia + 1, nA):
            cf = Ra & (R[A[ib]] > 0)
            if cf.any():
                Mt[ia, ib] = Mt[ib, ia] = ha[cf].min()
    np.fill_diagonal(Mt, 0.0)
    W = np.zeros((nA, nA))
    for i in range(nA):
        nb = [j for j in np.argsort(Mt[i]) if np.isfinite(Mt[i, j]) and j != i][:8]
        for j in nb:
            w = np.exp(-Mt[i, j] / (np.median([Mt[i, q] for q in nb]) + 1e-9))
            W[i, j] = W[j, i] = max(W[i, j], w)
    return W


def frame_grad(u, vals, kf=10):
    g = np.zeros_like(vals)
    for i in range(len(u)):
        nb = np.argsort(np.abs(u - u[i]))[:kf]
        g[i] = np.polyfit(u[nb], vals[nb], 1)[0]
    return g


def score(u, xt):
    if np.corrcoef(u, xt)[0, 1] < 0:
        u = -u
    Nv, Mv = Nl(xt), Ml(xt)
    Delta = Mv * frame_grad(u, Nv) - Nv * frame_grad(u, Mv)
    xitrue = xi(xt)
    cc = np.corrcoef(Delta, -xitrue)[0, 1]
    hi = np.abs(xitrue) > np.median(np.abs(xitrue))
    enr = np.mean(np.abs(Delta)[hi]) / (np.mean(np.abs(Delta)) + 1e-12)
    return cc, enr


def one_trial(rg):
    P = np.column_stack([rg.uniform(-3.0, 3.0, 4000), rg.uniform(-3.0, 3.0, 4000)])
    R = order_matrix(P)
    delta = 0.18
    A = np.where(np.abs(P[:, 0]) < delta / 2)[0]
    A = A[np.abs(P[A, 1]) < 2.2]
    W = build_W(P, R, A, delta)
    Lap = np.diag(W.sum(1)) - W
    ncomp, _ = connected_components(csr_matrix(W > 0), directed=False)
    vals, V = eigh(Lap)
    cc, enr = score(V[:, 1], P[A, 1])
    return dict(A=A, xt=P[A, 1], W=W, Lap=Lap, vals=vals, ncomp=ncomp, cc=cc, enr=enr)


rg = np.random.default_rng(0)
trials = []
for t in range(5):
    r = one_trial(rg)
    trials.append(r)
    nullity = int(np.sum(np.abs(r["vals"]) < 1e-9))
    print(f"  trial {t}: |A|={len(r['A']):3d}  components={r['ncomp']}  nullity={nullity}  "
          f"lam0={r['vals'][0]:+.3e}  lam1={r['vals'][1]:+.3e}  lam2={r['vals'][2]:+.3e}  "
          f"corr={r['cc']:+.4f}  enrich={r['enr']:.3f}")
base = np.array([r["cc"] for r in trials])
basee = np.array([r["enr"] for r in trials])
print(f"  campaign mean corr {base.mean():+.4f}   per-trial sd {base.std(ddof=0):.4f}   "
      f"mean enrichment {basee.mean():.4f}")
anchor("v6_p2c PART2 mean corr", base.mean(), 0.540, 5e-3)
anchor("v6_p2c PART2 mean enrichment", basee.mean(), 1.26, 5e-3)

print()
print("  trial 0, 1e-13 symmetric perturbation of the Laplacian, 60 draws:")
t0 = trials[0]
prng = np.random.default_rng(12345)
pert = []
for _ in range(60):
    E = prng.standard_normal(t0["Lap"].shape) * 1e-13
    E = 0.5 * (E + E.T)
    _, V = eigh(t0["Lap"] + E)
    pert.append(score(V[:, 1], t0["xt"])[0])
pert = np.array(pert)
means = (pert + base[1:].sum()) / 5.0
print(f"    unperturbed {t0['cc']:+.4f}   perturbed range [{pert.min():+.4f}, {pert.max():+.4f}]  "
      f"sd {pert.std():.4f}")
print(f"    induced campaign-mean range [{means.min():.4f}, {means.max():.4f}]   "
      f"covers the recorded 0.63: {bool(means.min() <= 0.63 <= means.max())}")
if not (means.min() <= 0.63 <= means.max()):
    FAIL.append("B-cover")

print()
print("  population reference, 40 independent trials (seed 20260728):")
rg2 = np.random.default_rng(20260728)
pc, pe, pk = [], [], []
for t in range(40):
    r = one_trial(rg2)
    pc.append(r["cc"])
    pe.append(r["enr"])
    pk.append(r["ncomp"])
pc, pe, pk = np.array(pc), np.array(pe), np.array(pk)
con = pk == 1
print(f"    corr       mean {pc.mean():+.4f}  sd {pc.std(ddof=1):.4f}  SE {pc.std(ddof=1)/np.sqrt(40):.4f}")
print(f"    enrichment mean {pe.mean():.4f}  sd {pe.std(ddof=1):.4f}  SE {pe.std(ddof=1)/np.sqrt(40):.4f}")
print(f"    disconnected slice graphs {int((~con).sum())}/40; connected-only corr mean "
      f"{pc[con].mean():+.4f} sd {pc[con].std(ddof=1):.4f}; disconnected corr "
      f"{np.array2string(pc[~con], precision=3)}")
camp_e = [pe[i * 5:(i + 1) * 5].mean() for i in range(8)]
camp_c = [pc[i * 5:(i + 1) * 5].mean() for i in range(8)]
print(f"    eight disjoint 5-trial campaigns: corr {np.array2string(np.array(camp_c), precision=3)}")
print(f"                                      enr  {np.array2string(np.array(camp_e), precision=3)}")
print(f"    recorded enrichment 1.38 exceeds all eight: {all(1.38 > c for c in camp_e)} "
      f"(max {max(camp_e):.3f})")

print()
print("=" * 78)
if FAIL:
    print("ANCHOR/STRUCTURE FAILURES:", ", ".join(FAIL))
    sys.exit(1)
print("all anchors hold; the two-rule split and the drift root cause are as reported.")
print("=" * 78)
