#!/usr/bin/env python3
"""
l3_four_dimensional.py — v8 paper 15 §4: 3+1 proper — the tomography stack on
M^{1+3}: the disk-section law, the celestial SPHERE, spherical-harmonic
reconstruction, and the v2 certificate in four dimensions.

Everything transfers by design: shadows are projections onto timelike 2-planes
indexed by n in S^2; the target density becomes the DISK-SECTION law
rho(t, s) ∝ (1-|t|)^2 - s^2 (area of the ball cross-section); one copula
serves all directions (rotational symmetry); the harmonic condition becomes
degree-<=1 SPHERICAL harmonics — u_n(x) = t - n.x is affine in n, and the four
coefficients ARE (t, x, y, z); the celestial S^2 is recovered by MDS on
inversion distances (a 3D embedding: shell + spectrum + angular consistency).

Direction set: a Fibonacci hemisphere of 12 directions (+ antipodes for the
24 signed profiles). N = 900 (paper-8-style onset discipline: 4D readouts need
more records; disclosed). Float64; default_rng(20260702). DEMONSTRATED grade.
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


def sprinkle_4d(N):
    pts = np.empty((0, 4))
    while len(pts) < N:
        m = 10 * (N - len(pts)) + 128
        t = rng.uniform(-1, 1, m)
        xyz = rng.uniform(-1, 1, (m, 3))
        keep = np.linalg.norm(xyz, axis=1) <= 1 - np.abs(t)
        pts = np.vstack([pts, np.column_stack([t, xyz])[keep]])
    return pts[:N]

def order_4d(P):
    dt = P[None, :, 0] - P[:, None, 0]
    dr = np.linalg.norm(P[None, :, 1:] - P[:, None, 1:], axis=2)
    return (dt > 0) & (dt > dr)

def fibonacci_hemisphere(K):
    """K quasi-uniform directions on the upper hemisphere."""
    out = []
    ga = np.pi * (3 - np.sqrt(5))
    for i in range(K):
        z = (i + 0.5) / K              # upper hemisphere z in (0, 1)
        r = np.sqrt(1 - z * z)
        phi = ga * i
        out.append([r * np.cos(phi), r * np.sin(phi), z])
    return np.array(out)

def u_coord4(P, n):
    return P[:, 0] - P[:, 1:] @ n

K_DIR = 12
DIRS = fibonacci_hemisphere(K_DIR)

M_REF = 150_000
REF = sprinkle_4d(M_REF)

# --------------------------------------- CHECK 1: the disk-section law
print("CHECK 1: the 4D shadow's target density is the disk-section law")
s_ref = REF[:, 1]                      # projection onto n = e_x
t_ref = REF[:, 0]
tb = np.linspace(-0.6, 0.6, 7)
sb = np.linspace(-0.6, 0.6, 7)
H, _, _ = np.histogram2d(t_ref, s_ref, bins=[tb, sb])
pred = np.zeros_like(H)
for i in range(len(tb) - 1):
    for j in range(len(sb) - 1):
        tm = 0.5 * (tb[i] + tb[i + 1]); sm = 0.5 * (sb[j] + sb[j + 1])
        v = (1 - abs(tm)) ** 2 - sm ** 2
        pred[i, j] = v if v > 0 else 0.0     # disk AREA ∝ R^2 - s^2
H = H / H.sum(); pred = pred / pred.sum()
tv_dist = 0.5 * float(np.abs(H - pred).sum())
ok = tv_dist < 0.03
check("projected 4D density matches the disk-section law (1-|t|)^2 - s^2 "
      "(TV < 0.03 on the central grid)", ok, f"TV = {tv_dist:.4f}")

# --------------------------------------- CHECK 2: the certifier in 4D
print("CHECK 2: the weighted certifier, 4D shadows vs controls")
def certify_shadow4(uv_pts, n, ref=REF):
    ru = np.sort(u_coord4(ref, n))
    rv = np.sort(u_coord4(ref, -n))
    N = len(uv_pts)
    au = np.searchsorted(ru, uv_pts[:, 0]) / len(ref)
    av = np.searchsorted(rv, uv_pts[:, 1]) / len(ref)
    cu = np.searchsorted(ru, u_coord4(ref, n)) / len(ref)
    cv = np.searchsorted(rv, u_coord4(ref, -n)) / len(ref)
    order = np.argsort(au)
    su, sv = au[order], av[order]
    ordr = np.argsort(cu)
    tu, tv_ = cu[ordr], cv[ordr]
    corners = np.linspace(0.05, 1.0, 40)
    vgrid = np.linspace(0.05, 1.0, 40)
    best = 0.0
    for a in corners:
        k_sh = np.searchsorted(su, a, side="right")
        k_rf = np.searchsorted(tu, a, side="right")
        sh_v = np.sort(sv[:k_sh])
        rf_v = np.sort(tv_[:k_rf])
        emp = np.searchsorted(sh_v, vgrid, side="right") / N
        tgt = np.searchsorted(rf_v, vgrid, side="right") / len(ref)
        best = max(best, float(np.abs(emp - tgt).max()))
    return best

N = 900
P = sprinkle_4d(N)
C4 = order_4d(P)
ws_true = [certify_shadow4(np.column_stack(
    [u_coord4(P, n), u_coord4(P, -n)]), n) for n in DIRS]
floors = []
for _ in range(10):    # 10 replicates (was 3, then 6): the max-statistic floor
                       # carries ~10% replicate noise; margin printed in-check
    sub = REF[rng.choice(len(REF), N, replace=False)]
    floors.append(max(certify_shadow4(np.column_stack(
        [u_coord4(sub, n), u_coord4(sub, -n)]), n) for n in DIRS))
fl = float(np.mean(floors))
# garbage control: random linear extension pair (via random topological order)
def random_extension(C):
    n_ = C.shape[0]
    indeg = C.sum(axis=0).astype(int)
    avail = [i for i in range(n_) if indeg[i] == 0]
    out = []
    ind = indeg.copy()
    succ = [np.nonzero(C[i])[0] for i in range(n_)]
    while avail:
        v = avail.pop(rng.integers(0, len(avail)))
        out.append(v)
        for w_ in succ[v]:
            ind[w_] -= 1
            if ind[w_] == 0:
                avail.append(int(w_))
    r = np.empty(n_, dtype=int)
    for k_, v in enumerate(out):
        r[v] = k_
    return r.astype(float)
# post-review M1 repair: the garbage extensions must be QUANTILE-MAPPED through
# the target marginals before scoring (the draft fed raw rank integers into a
# value-expecting certifier — a unit mismatch that scored EVERYTHING ~0.975,
# true shadows included; the "18x" was an artifact and is retracted)
def ranks_to_values(r, n_dir):
    ref_sorted = np.sort(u_coord4(REF, n_dir))
    q = (np.argsort(np.argsort(r)) + 0.5) / len(r)
    return ref_sorted[np.clip((q * len(ref_sorted)).astype(int), 0,
                              len(ref_sorted) - 1)]
g1 = ranks_to_values(random_extension(C4), DIRS[0])
g2 = ranks_to_values(random_extension(C4), -DIRS[0])
wg = certify_shadow4(np.column_stack([g1, g2]), DIRS[0])
margin = (1.35 * fl - max(ws_true)) / fl
ok = max(ws_true) < 1.35 * fl and wg > 1.5 * max(ws_true)
check("all 12 true 4D shadows pass at the max-calibrated floor (gate 1.35x, "
      "10-replicate calibration; the pass margin vs floor noise is printed, "
      "not hidden); FAIRLY-SCORED garbage (quantile-mapped) fails above the "
      "true band — the honest gap, replacing the retracted 18x artifact", ok,
      f"max wD* = {max(ws_true):.4f} vs 1.35x floor {1.35*fl:.4f} (margin "
      f"{margin:+.2f} floors); garbage {wg:.4f} = {wg/max(ws_true):.1f}x true")

# --------------------------------------- CHECK 3: spherical-harmonic recon
print("CHECK 3: degree-<=1 spherical-harmonic reconstruction of (t, x, y, z)")
DIRS_ALL = np.vstack([DIRS, -DIRS])
U_rec = np.empty((N, 2 * K_DIR))
for k_, n in enumerate(DIRS_ALL):
    ref_sorted = np.sort(u_coord4(REF, n))
    ranks = np.argsort(np.argsort(u_coord4(P, n)))
    q = (ranks + 0.5) / N
    U_rec[:, k_] = ref_sorted[np.clip((q * len(ref_sorted)).astype(int), 0,
                                      len(ref_sorted) - 1)]
A = np.column_stack([np.ones(2 * K_DIR), DIRS_ALL])
coef, _, _, _ = np.linalg.lstsq(A, U_rec.T, rcond=None)
R = np.column_stack([coef[0], -coef[1], -coef[2], -coef[3]])
resid = float(np.sqrt(np.mean((A @ coef - U_rec.T) ** 2)))
cs = [float(np.corrcoef(R[:, i], P[:, i])[0, 1]) for i in range(4)]
agree = float((order_4d(R) == C4).mean())
ok = resid < 0.05 and all(c > 0.99 for c in cs) and agree > 0.99
check("profiles are affine in n (residual < 0.05); the four coefficients "
      "reconstruct (t, x, y, z) at > 0.99 each; the rebuilt order agrees "
      "> 99% — the first ORACLE-FAMILY 4D reconstruction in this program "
      "(the intrinsic-finder 4D run is the named next step, NOT claimed here)", ok,
      f"resid = {resid:.4f}; corr = " + "/".join(f"{c:.4f}" for c in cs)
      + f"; agreement = {agree:.4f}")

# --------------------------------------- CHECK 4: the celestial SPHERE
print("CHECK 4: the celestial S^2 from inversion distances")
def kendall_fast(a, b):
    # O(n log n) inversion count via mergesort on b permuted by a's order
    seq = b[np.argsort(a, kind="stable")]
    n_ = len(seq)
    def sort_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        L, cl = sort_count(arr[:mid])
        Rr, cr = sort_count(arr[mid:])
        merged = np.empty(len(arr))
        i = j = k2 = 0
        inv = cl + cr
        while i < len(L) and j < len(Rr):
            if L[i] <= Rr[j]:
                merged[k2] = L[i]; i += 1
            else:
                merged[k2] = Rr[j]; j += 1
                inv += len(L) - i
            k2 += 1
        merged[k2:] = np.concatenate([L[i:], Rr[j:]])
        return merged, inv
    _, inv = sort_count(seq)
    return inv / (n_ * (n_ - 1) / 2)

exts = [np.argsort(np.argsort(u_coord4(P, n))) for n in DIRS_ALL]
K2 = len(DIRS_ALL)
D = np.zeros((K2, K2))
for i in range(K2):
    for j in range(i + 1, K2):
        D[i, j] = D[j, i] = kendall_fast(exts[i].astype(float),
                                         exts[j].astype(float))
J = np.eye(K2) - np.ones((K2, K2)) / K2
B = -0.5 * J @ (D ** 2) @ J
w_eig, V = np.linalg.eigh(B)
XYZ = V[:, -3:] * np.sqrt(np.maximum(w_eig[-3:], 0))
rad = np.linalg.norm(XYZ, axis=1)
rad_cv = float(np.std(rad) / np.mean(rad))
spec_ratio = float(abs(w_eig[-4]) / w_eig[-3])   # |4th|/3rd: abs() so a
# negative 4th eigenvalue cannot pass the gate trivially (pre-review guard)
# angular consistency: MDS pairwise angles vs true angles between directions
def angmat(V_):
    Vn = V_ / np.linalg.norm(V_, axis=1, keepdims=True)
    return np.arccos(np.clip(Vn @ Vn.T, -1, 1))
ang_true = angmat(DIRS_ALL)
ang_mds = angmat(XYZ)
iu = np.triu_indices(K2, 1)
ang_corr = float(np.corrcoef(ang_true[iu], ang_mds[iu])[0, 1])
ok = rad_cv < 0.12 and spec_ratio < 0.35 and ang_corr > 0.95
check("MDS of the 24 extensions' inversion distances is a 2-SPHERE: shell "
      "(radius CV < 0.12), 3-dimensional spectrum (4th/3rd eigenvalue < 0.35), "
      "and the angular geometry matches the true celestial angles (corr > "
      "0.95) — the celestial sphere recovered from order data, 3+1", ok,
      f"radius CV = {rad_cv:.3f}; spectral drop = {spec_ratio:.3f}; "
      f"angle corr = {ang_corr:.4f}")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
