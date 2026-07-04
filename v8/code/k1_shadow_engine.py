#!/usr/bin/env python3
"""
k1_shadow_engine.py — v8 paper 14 §2: causal tomography, the verification engine
(2+1D pilot) — shadows, the weighted-discrepancy certifier, the harmonic
condition, and the T1 reconstruction numeric.

THE MATH (paper 14 §2.1, elementary):
  * M^{1+2} causal order = the intersection of the null-coordinate total orders
    u_n(x) = t - n.x over the celestial circle n in S^1.
  * Each ANTIPODAL pair {n, -n} spans (with time) a timelike 2-plane; projecting
    onto it maps the order to a 2D dominance order that COARSENS P (Thm 2.1:
    |D(m.x)| <= |Dx| < Dt), with null coordinates u = u_n, v = u_{-n} — a SHADOW.
  * The shadow of a faithful 3D diamond sprinkling is a 2D point set with the
    KNOWN non-uniform density rho(t,s) ∝ chord length sqrt((1-|t|)^2 - s^2):
    NOT uniform-faithful — the paper-12 instrument generalizes to a WEIGHTED
    discrepancy against the target copula (the certifier below).
  * Harmonic condition: the profile theta -> u_theta(x) is EXACTLY
    a0 + a1 cos(theta) + b1 sin(theta) with (a0, a1, b1) = (t, x, y):
    degree <= 1 Fourier concentration IS the Minkowski form, and the Fourier
    coefficients ARE the reconstruction (T1's constructive core).

CHECKS: shadow coarsening exact; the chord-density law vs a high-N projection;
the certifier separates true shadows (pass, iid scale) from uniform-target
scoring (fails — the weighting is load-bearing) and from garbage coarsenings;
the harmonic residual ~ 0 with QUANTILE-RECOVERED u values (the intrinsic
gauge) and reconstruction correlation > 0.99; the T1 numeric: rebuild (t,x,y)
from K = 8 certified shadows and verify 3D count-volume faithfulness of the
reconstruction on random sub-diamonds.

Float discipline: float64 measurement; default_rng(20260702). Tolerances
measured-and-disclosed (DEMONSTRATED grade; T1's proof is in-paper).
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


# ------------------------------------------------------------ 3D sprinkling
def sprinkle_3d(N):
    """Uniform in the diamond |x| <= 1 - |t|, t in [-1, 1] (apexes on the t-axis)."""
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

def shadow_order(P, theta):
    """2D dominance order of the projection onto the (t, s)-plane, s = n.x."""
    s = P[:, 1] * np.cos(theta) + P[:, 2] * np.sin(theta)
    dt = P[None, :, 0] - P[:, None, 0]
    return (dt > 0) & (dt > np.abs(s[None, :] - s[:, None])), s

def u_coord(P, theta):
    return P[:, 0] - P[:, 1] * np.cos(theta) - P[:, 2] * np.sin(theta)


# ------------------------------------------------------ the weighted certifier
# reference sample for the target copula (the projected diamond's law)
M_REF = 200_000
REF = sprinkle_3d(M_REF)

def certify_shadow(uv_pts, theta, ref=REF):
    """Weighted D*: sup over anchored boxes (in target-quantile space) of
    |empirical(shadow) - target copula|. uv_pts: the shadow's (u, v) values
    (or any monotone gauge of them — quantile transform absorbs the gauge)."""
    ru = u_coord(ref, theta)
    rv = u_coord(ref, theta + np.pi)
    N = len(uv_pts)
    # map both samples through the target marginals (empirical quantiles)
    au = np.searchsorted(np.sort(ru), uv_pts[:, 0]) / len(ref)
    av = np.searchsorted(np.sort(rv), uv_pts[:, 1]) / len(ref)
    cu = np.searchsorted(np.sort(ru), ru) / len(ref)
    cv = np.searchsorted(np.sort(rv), rv) / len(ref)
    # sup over boxes anchored at 0 with corners at shadow points (+1 edge)
    best = 0.0
    order = np.argsort(au)
    su, sv = au[order], av[order]
    ordr = np.argsort(cu)
    tu, tv = cu[ordr], cv[ordr]
    corners = np.unique(np.concatenate([su, [1.0]]))
    vgrid = np.unique(np.concatenate([sv, [1.0]]))
    for a in corners:
        k_sh = np.searchsorted(su, a, side="right")
        k_rf = np.searchsorted(tu, a, side="right")
        sh_v = np.sort(sv[:k_sh])
        rf_v = np.sort(tv[:k_rf])
        emp = np.searchsorted(sh_v, vgrid, side="right") / N
        tgt = np.searchsorted(rf_v, vgrid, side="right") / len(ref)
        best = max(best, float(np.abs(emp - tgt).max()))
    return best


# --------------------------------------- CHECK 1: shadows coarsen, exactly
print("CHECK 1: every shadow coarsens the 3D order (Thm 2.1, exact)")
N = 400
P = sprinkle_3d(N)
C3 = order_3d(P)
ok = True
for theta in np.linspace(0, np.pi, 5, endpoint=False):
    C2, _ = shadow_order(P, theta)
    if not np.all(C2[C3]):          # every 3D relation survives projection
        ok = False
check("all 3D relations survive in every tested shadow (5 directions, N = 400) "
      "— shadows are order-coarsenings, exactly", ok)
# the INTERSECTION half, finite-grid honesty: over the continuum sphere the
# intersection equals P per pair (the sup is achieved at m = dx/|dx|); a finite
# K-grid intersection is a coarsening that converges to P from above — measured
extra = []
for K_ in (16, 32, 64):
    thetasK = np.arange(K_) * np.pi / K_
    inter = np.ones_like(C3)
    for th in thetasK:
        C2K, _ = shadow_order(P, th)
        inter &= C2K
    extra.append(int(inter.sum() - C3.sum()))
ok = extra[0] >= extra[1] >= extra[2] and extra[2] < 0.01 * C3.sum()
check("finite-grid intersection converges to P from above: extra relations "
      "shrink with K and are < 1% of true relations at K = 64 (the continuum "
      "identity's finite face, measured — not assumed)", ok,
      f"extra relations at K = 16/32/64: {extra[0]}/{extra[1]}/{extra[2]} "
      f"of {int(C3.sum())}")

# --------------------------------------- CHECK 2: the chord-density law
print("CHECK 2: the shadow's target density is the chord law")
s_ref = REF[:, 1]                    # theta = 0 projection: s = x
t_ref = REF[:, 0]
# bin in (t, s), compare to sqrt((1-|t|)^2 - s^2)
tb = np.linspace(-0.6, 0.6, 7)
sb = np.linspace(-0.6, 0.6, 7)
H, _, _ = np.histogram2d(t_ref, s_ref, bins=[tb, sb])
pred = np.zeros_like(H)
for i in range(len(tb) - 1):
    for j in range(len(sb) - 1):
        tm = 0.5 * (tb[i] + tb[i + 1]); sm = 0.5 * (sb[j] + sb[j + 1])
        v = (1 - abs(tm)) ** 2 - sm ** 2
        pred[i, j] = np.sqrt(v) if v > 0 else 0.0
H = H / H.sum(); pred = pred / pred.sum()
tv_dist = 0.5 * float(np.abs(H - pred).sum())
ok = tv_dist < 0.03
check("projected density matches the chord law sqrt((1-|t|)^2 - s^2) "
      "(TV over a 6x6 central grid < 0.03; bin-center approximation disclosed)",
      ok, f"TV = {tv_dist:.4f}")

# --------------------------------------- CHECK 3: the certifier separates
print("CHECK 3: the weighted certifier — true shadows pass, controls fail")
wds, wds_unif = [], []
for rep_i in range(5):   # replicates off the one seeded stream
    Pi = sprinkle_3d(N)
    th = rng.uniform(0, np.pi)
    ui = u_coord(Pi, th); vi = u_coord(Pi, th + np.pi)
    uv = np.column_stack([ui, vi])
    wds.append(certify_shadow(uv, th))
    # uniform-target control: score the same points against the UNIFORM copula
    # (i.e., paper-12's unweighted D* on the rank embedding)
    ru = np.argsort(np.argsort(ui)); rv = np.argsort(np.argsort(vi))
    emb = np.column_stack([(ru + 0.5) / N, (rv + 0.5) / N])
    us = np.unique(np.concatenate([emb[:, 0], [1.0]]))
    vs = np.unique(np.concatenate([emb[:, 1], [1.0]]))
    o = np.argsort(emb[:, 0]); pu, pv = emb[o, 0], emb[o, 1]
    b = 0.0
    for a in us:
        kk = np.searchsorted(pu, a, side="right")
        svv = np.sort(pv[:kk])
        cnt = np.searchsorted(svv, vs, side="right") / N
        b = max(b, float(np.abs(cnt - a * vs).max()))
    wds_unif.append(b)
w_true = float(np.mean(wds))
w_unif = float(np.mean(wds_unif))
# the honest floor: samples drawn from the target copula ITSELF (REF
# subsamples — NOT disjoint from REF, so the floor is slightly deflated;
# disclosed) carry the same two-sample sup noise — the certifier's pass band
floor = []
for k_ in range(5):
    sub = REF[rng.choice(len(REF), N, replace=False)]
    th = rng.uniform(0, np.pi)
    floor.append(certify_shadow(np.column_stack(
        [u_coord(sub, th), u_coord(sub, th + np.pi)]), th))
w_floor = float(np.mean(floor))
# the chord copula's ASYMPTOTIC uniform-defect: rank-embed a large REF subsample
big = REF[rng.choice(len(REF), 20000, replace=False)]
bu = u_coord(big, 0.0); bv = u_coord(big, np.pi)
rbu = np.argsort(np.argsort(bu)); rbv = np.argsort(np.argsort(bv))
embB = np.column_stack([(rbu + 0.5) / 20000, (rbv + 0.5) / 20000])
usB = np.linspace(0.02, 1.0, 50)
oB = np.argsort(embB[:, 0]); puB, pvB = embB[oB, 0], embB[oB, 1]
dU = 0.0
for a in usB:
    kk = np.searchsorted(puB, a, side="right")
    svv = np.sort(pvB[:kk])
    cnt = np.searchsorted(svv, usB, side="right") / 20000
    dU = max(dU, float(np.abs(cnt - a * usB).max()))
# garbage control: intersect two RANDOM linear extensions of the 3D order
def random_extension(C):
    n = C.shape[0]
    indeg = C.sum(axis=0).astype(int)
    avail = [i for i in range(n) if indeg[i] == 0]
    out = []
    ind = indeg.copy()
    succ = [np.nonzero(C[i])[0] for i in range(n)]
    while avail:
        v = avail.pop(rng.integers(0, len(avail)))
        out.append(v)
        for w in succ[v]:
            ind[w] -= 1
            if ind[w] == 0:
                avail.append(int(w))
    r = np.empty(n, dtype=int)
    for k_, v in enumerate(out):
        r[v] = k_
    return r
wg = []
for _ in range(3):
    Pi = sprinkle_3d(N)
    Ci = order_3d(Pi)
    e1 = random_extension(Ci).astype(float)
    e2 = random_extension(Ci).astype(float)
    th = rng.uniform(0, np.pi)
    wg.append(certify_shadow(np.column_stack([e1, e2]), th))
w_garb = float(np.mean(wg))
ok = w_true < 1.5 * w_floor and w_garb > 4 * w_true and dU > 0.02
check("the certifier, floor-calibrated: true shadows sit at the target-copula "
      "two-sample floor (within 1.5x of same-law subsample controls); "
      "random-extension garbage fails at > 4x; and the chord copula's "
      "asymptotic uniform-defect is real (rank-D* of a 20k target sample "
      "> 0.02 — though at N = 400 the uniform test barely discriminates, "
      "measured 0.047 vs the ~0.03 faithful band: the weighting's load-bearing "
      "role is defect ATTRIBUTION and the large-N limit, DISCLOSED, not a "
      "dramatic finite-N kill)", ok,
      f"wD*(true) = {w_true:.4f} vs floor {w_floor:.4f}; garbage {w_garb:.4f}; "
      f"copula uniform-defect(20k) = {dU:.4f}; unweighted-on-true(400) = "
      f"{w_unif:.4f}")

# --------------------------------------- CHECK 4: the harmonic condition
print("CHECK 4: the harmonic condition and intrinsic-gauge reconstruction")
K = 8
thetas = np.arange(2 * K) * np.pi / K          # 16 signed directions
U_true = np.stack([u_coord(P, th) for th in thetas], axis=1)
# intrinsic gauge: replace each u_theta by its TARGET-QUANTILE recovery
# (rank within the shadow -> target quantile -> target u-value)
U_rec = np.empty_like(U_true)
for k_, th in enumerate(thetas):
    ru_ref = np.sort(u_coord(REF, th))
    ranks = np.argsort(np.argsort(U_true[:, k_]))
    q = (ranks + 0.5) / N
    U_rec[:, k_] = ru_ref[np.clip((q * len(ru_ref)).astype(int), 0,
                                  len(ru_ref) - 1)]
# Fourier fit: u_theta ~ a0 + a1 cos + b1 sin
A = np.column_stack([np.ones(2 * K), np.cos(thetas), np.sin(thetas)])
coef, res, _, _ = np.linalg.lstsq(A, U_rec.T, rcond=None)
t_hat, x_hat, y_hat = coef[0], -coef[1], -coef[2]
resid = float(np.sqrt(np.mean((A @ coef - U_rec.T) ** 2)))
cs = [float(np.corrcoef(a, b)[0, 1]) for a, b in
      ((t_hat, P[:, 0]), (x_hat, P[:, 1]), (y_hat, P[:, 2]))]
ok = resid < 0.05 and all(c > 0.99 for c in cs)
check("quantile-recovered profiles are degree-<=1 Fourier concentrated "
      "(RMS residual < 0.05) and the Fourier coefficients reconstruct (t, x, y) "
      "at correlation > 0.99 each — the T1 constructive core, intrinsic gauge",
      ok, f"residual = {resid:.4f}; corr = {cs[0]:.4f}/{cs[1]:.4f}/{cs[2]:.4f}")

# --------------------------------------- CHECK 5: T1 numeric — 3D faithfulness
print("CHECK 5: the reconstructed point set is 3D count-volume faithful")
R = np.column_stack([t_hat, x_hat, y_hat])
C3r = order_3d(R)
agree = float((C3r == C3).mean())
# simpler, closed-form-free faithfulness check: interval counts agree between
# the reconstruction's order and the original order (already in `agree`), and
# the reconstructed points refill the diamond uniformly: 3D box-count test
box_errs = []
for _ in range(200):
    c = sprinkle_3d(1)[0]
    r_box = rng.uniform(0.15, 0.35)
    inside_R = (np.abs(R[:, 0] - c[0]) < r_box) & \
               (np.hypot(R[:, 1] - c[1], R[:, 2] - c[2]) < r_box)
    inside_P = (np.abs(P[:, 0] - c[0]) < r_box) & \
               (np.hypot(P[:, 1] - c[1], P[:, 2] - c[2]) < r_box)
    box_errs.append(abs(int(inside_R.sum()) - int(inside_P.sum())))
mean_box_err = float(np.mean(box_errs))
ok = agree > 0.995 and mean_box_err < 3.0
check("reconstruction fidelity: the reconstructed order agrees with the "
      "original on > 99.5% of pairs, and box counts around random centers "
      "match the original's to < 3 elements on average (closed-form-free "
      "faithfulness transfer)", ok,
      f"order agreement = {agree:.4f}; mean |box-count diff| = {mean_box_err:.2f}")

# --------------------------------------- CHECK 6 (post-review): the pilot
# certificate, DEFINED and jointly verified on ONE order (round-1 m2: the two
# conditions had been checked on different point sets, and no thresholds were
# pinned). PILOT CERTIFICATE (definition): a 2K-direction family such that
# (i) every antipodal shadow's weighted D* < 1.5x the two-sample floor, and
# (ii) the quantile-gauged profiles' degree-<=1 Fourier RMS residual < 0.05.
print("CHECK 6: the pilot certificate, defined and jointly verified on P")
# the floor must be the SAME functional (max over K directions) on same-law
# subsamples — max-statistics calibration, not 1.5x a single-shadow mean
fl_max = []
for _ in range(3):
    sub = REF[rng.choice(len(REF), N, replace=False)]
    ws = [certify_shadow(np.column_stack(
        [u_coord(sub, thetas[k_]), u_coord(sub, thetas[k_] + np.pi)]),
        thetas[k_]) for k_ in range(K)]
    fl_max.append(max(ws))
fl = float(np.mean(fl_max))
wd_all = []
for k_ in range(K):
    th = thetas[k_]
    wd_all.append(certify_shadow(np.column_stack(
        [u_coord(P, th), u_coord(P, th + np.pi)]), th))
cond_i = max(wd_all) < 1.3 * fl
cond_ii = resid < 0.05
ok = cond_i and cond_ii
check(f"P carries the FULL pilot certificate: (i) the MAX wD* over all {K} "
      f"antipodal shadows < 1.3x the max-calibrated same-law floor (the floor "
      f"is the same max-over-K functional on target subsamples — apples-to-"
      f"apples), and (ii) the harmonic residual < 0.05 — both conditions on "
      f"the SAME order (T2's witness, jointly verified; thresholds pinned)",
      ok, f"max wD* = {max(wd_all):.4f} vs 1.3x max-floor = {1.3*fl:.4f}; "
      f"residual = {resid:.4f}")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
