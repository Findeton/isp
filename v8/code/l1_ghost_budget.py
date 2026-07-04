#!/usr/bin/env python3
"""
l1_ghost_budget.py — v8 paper 15 §2: certificate v2, the spectral ghost, and
the exact scoping of the tomography guarantee (2+1D).

THE THEORY (paper 15 §2, with the Logan/discrete-tomography imports):
  * Point-REARRANGEMENT ghosts (discrete-tomography switching components) are
    not soundness threats: a rearranged point set is a real embedding, so the
    harmonic condition still passes BECAUSE THE ORDER IS STILL FAITHFUL — the
    certificate is not fooled, the input just isn't a counterexample.
  * The true adversary is a SPECTRAL DENSITY ghost: modulate the sprinkling
    density by 1 + a cos(q.x) with q purely spatial. Its k-th shadow marginal
    is fiber-averaged: leakage ~ a/(q sin(angle to the nearest direction)) —
    INVISIBLE to a K-direction certificate iff q >~ 1/sin(grid spacing) ~ K
    (Logan's finite-angle principle). And ANY high-q mode is CDF-blind: its
    effect on every anchored-box count is <= ~a/q, in 3D as well as in every
    shadow. THE CLOSED LOOP: modes invisible to the K-direction certificate
    have q >~ K, hence 3D anchored-box discrepancy <= ~a/K — the certificate
    controls the DISCREPANCY metric at all scales; what it provably cannot
    control (and no finite-K discrepancy certificate can) is SPECTRAL
    uniformity below wavelength ~1/K. The guarantee is thereby scoped exactly.
  * CERTIFICATE v2 adds condition (iii): the harmonic reconstruction must
    REALIZE the input order (agreement >= 0.98) — closing the round-14 m2 gap
    (order-realization was measured but never required).

CHECKS: v2 on faithful P (all three conditions, one order); the spectral ghost
(matched-filter z >> 5 — the density is REALLY non-uniform) passing K = 8 AND
K = 16 shadows at floor AND carrying an UNCHANGED 3D discrepancy (the scoping
theorem's content, measured); the low-frequency control ghost (q ~ 8, off-grid)
CAUGHT by the K = 8 certificate (low-frequency non-uniformity cannot hide —
the budget is high-frequency-only).

Float discipline: float64; default_rng(20260702). DEMONSTRATED grade; the
scoping statements' proofs are in-paper (elementary Fourier/geometry).
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


def sprinkle_3d(N, density=None):
    """Rejection-sample the diamond, optionally with density 1 + modulation."""
    pts = np.empty((0, 3))
    while len(pts) < N:
        m = 6 * (N - len(pts)) + 64
        t = rng.uniform(-1, 1, m)
        x = rng.uniform(-1, 1, m)
        y = rng.uniform(-1, 1, m)
        keep = np.hypot(x, y) <= 1 - np.abs(t)
        cand = np.column_stack([t, x, y])[keep]
        if density is not None:
            w = density(cand)
            keep2 = rng.random(len(cand)) < w / w.max()
            cand = cand[keep2]
        pts = np.vstack([pts, cand])
    return pts[:N]

def order_3d(P):
    dt = P[None, :, 0] - P[:, None, 0]
    dr = np.hypot(P[None, :, 1] - P[:, None, 1], P[None, :, 2] - P[:, None, 2])
    return (dt > 0) & (dt > dr)

def u_coord(P, theta):
    return P[:, 0] - P[:, 1] * np.cos(theta) - P[:, 2] * np.sin(theta)

M_REF = 200_000
REF = sprinkle_3d(M_REF)

def certify_shadow(uv_pts, theta, ref=REF):
    ru = u_coord(ref, theta)
    rv = u_coord(ref, theta + np.pi)
    N = len(uv_pts)
    au = np.searchsorted(np.sort(ru), uv_pts[:, 0]) / len(ref)
    av = np.searchsorted(np.sort(rv), uv_pts[:, 1]) / len(ref)
    cu = np.searchsorted(np.sort(ru), ru) / len(ref)
    cv = np.searchsorted(np.sort(rv), rv) / len(ref)
    order = np.argsort(au)
    su, sv = au[order], av[order]
    ordr = np.argsort(cu)
    tu, tv = cu[ordr], cv[ordr]
    corners = np.linspace(0.05, 1.0, 40)
    vgrid = np.linspace(0.05, 1.0, 40)
    best = 0.0
    for a in corners:
        k_sh = np.searchsorted(su, a, side="right")
        k_rf = np.searchsorted(tu, a, side="right")
        sh_v = np.sort(sv[:k_sh])
        rf_v = np.sort(tv[:k_rf])
        emp = np.searchsorted(sh_v, vgrid, side="right") / N
        tgt = np.searchsorted(rf_v, vgrid, side="right") / len(ref)
        best = max(best, float(np.abs(emp - tgt).max()))
    return best

def shadow_scores(P, K):
    thetas = np.arange(K) * np.pi / K
    return [certify_shadow(np.column_stack(
        [u_coord(P, th), u_coord(P, th + np.pi)]), th) for th in thetas]

def floor_max(N, K, reps=3):
    out = []
    for _ in range(reps):
        sub = REF[rng.choice(len(REF), N, replace=False)]
        out.append(max(shadow_scores(sub, K)))
    return float(np.mean(out))

def harmonic_recon(P, K=8):
    thetas = np.arange(2 * K) * np.pi / K
    N = len(P)
    U = np.empty((N, 2 * K))
    for k_, th in enumerate(thetas):
        ref_sorted = np.sort(u_coord(REF, th))
        ranks = np.argsort(np.argsort(u_coord(P, th)))
        q = (ranks + 0.5) / N
        U[:, k_] = ref_sorted[np.clip((q * len(ref_sorted)).astype(int), 0,
                                      len(ref_sorted) - 1)]
    A = np.column_stack([np.ones(2 * K), np.cos(thetas), np.sin(thetas)])
    coef, _, _, _ = np.linalg.lstsq(A, U.T, rcond=None)
    resid = float(np.sqrt(np.mean((A @ coef - U.T) ** 2)))
    R = np.column_stack([coef[0], -coef[1], -coef[2]])
    return R, resid

def certificate_v2(P, K=8):
    """(i) max shadow wD* < 1.3x max-floor; (ii) harmonic resid < 0.05;
    (iii) reconstruction realizes the order at agreement >= 0.98."""
    N = len(P)
    fl = floor_max(N, K)
    ws = shadow_scores(P, K)
    R, resid = harmonic_recon(P, K)
    agree = float((order_3d(R) == order_3d(P)).mean())
    return dict(max_w=max(ws), floor=fl, resid=resid, agree=agree,
                passes=(max(ws) < 1.3 * fl and resid < 0.05 and agree >= 0.98))


# --------------------------------------- CHECK 1: v2 on faithful input
print("CHECK 1: certificate v2 (with condition (iii)) on faithful P")
N = 1200
P = sprinkle_3d(N)
c = certificate_v2(P)
check("faithful P carries the FULL v2 certificate — (i) shadows at floor, "
      "(ii) harmonic, (iii) order-realizing reconstruction — jointly, one order",
      c["passes"], f"max wD* {c['max_w']:.4f} vs 1.3x floor {1.3*c['floor']:.4f}; "
      f"resid {c['resid']:.4f}; agreement {c['agree']:.4f}")

# --------------------------------------- CHECK 2: the spectral ghost
print("CHECK 2: the spectral ghost — really non-uniform, certificate-invisible")
Q = 120.0
theta_g = np.pi / 16 + np.pi / 8          # bisector of the K = 8 grid
qvec = Q * np.array([np.cos(theta_g), np.sin(theta_g)])
A_G = 0.6
def ghost_density(pts):
    return 1 + A_G * np.cos(pts[:, 1] * qvec[0] + pts[:, 2] * qvec[1])
PG = sprinkle_3d(N, density=ghost_density)
# (a) matched filter: the density really is modulated
phase = PG[:, 1] * qvec[0] + PG[:, 2] * qvec[1]
a_hat = 2.0 * float(np.mean(np.cos(phase)))
z_matched = abs(a_hat) / np.sqrt(2.0 / N)
ok = z_matched > 5
check("the ghost's density is REALLY non-uniform: matched-filter amplitude "
      "recovers the modulation at > 5 sigma", ok,
      f"a_hat = {a_hat:.3f} (injected 0.6 pre-chord-weighting), z = {z_matched:.1f}")

# (b) invisible to K = 8 AND K = 16 certificates
cg8 = certificate_v2(PG, K=8)
ws16 = shadow_scores(PG, 16)
fl16 = floor_max(N, 16)
ok = cg8["passes"] and max(ws16) < 1.3 * fl16
check("the ghost PASSES the full v2 certificate at K = 8 AND its shadows pass "
      "at K = 16 — high-frequency modes are CDF-blind in every direction "
      "(<= a/q per anchored box), exactly as the scoping theorem says", ok,
      f"K=8: max wD* {cg8['max_w']:.4f} vs {1.3*cg8['floor']:.4f}, resid "
      f"{cg8['resid']:.4f}, agree {cg8['agree']:.4f}; K=16 max {max(ws16):.4f} "
      f"vs {1.3*fl16:.4f}")

# (c) the 3D anchored-box discrepancy is UNCHANGED (the certified metric is
# genuinely controlled; the ghost lives below its resolution)
def disc3(Pp, boxes=400):
    N_ = len(Pp)
    best = 0.0
    V_diam = 2 * np.pi / 3
    for _ in range(boxes):
        c0 = sprinkle_3d(1)[0]
        r = rng.uniform(0.1, 0.5)
        inside = (np.abs(Pp[:, 0] - c0[0]) < r) & \
                 (np.hypot(Pp[:, 1] - c0[1], Pp[:, 2] - c0[2]) < r)
        # reference volume fraction via REF
        ref_in = (np.abs(REF[:, 0] - c0[0]) < r) & \
                 (np.hypot(REF[:, 1] - c0[1], REF[:, 2] - c0[2]) < r)
        best = max(best, abs(inside.mean() - ref_in.mean()))
    return best
d_clean = disc3(P)
d_ghost = disc3(PG)
ok = d_ghost < 1.5 * d_clean
check("the ghost's 3D box discrepancy is UNCHANGED vs clean (within 1.5x) — "
      "shadow-invisible modes cannot create large-scale volume defect (the "
      "closed loop: invisibility forces q >~ K, and q >~ K forces box effects "
      "<= a/q)", ok, f"clean {d_clean:.4f} vs ghost {d_ghost:.4f}")

# --------------------------------------- CHECK 3: the low-frequency control
print("CHECK 3: the low-frequency control — slow modes CANNOT hide")
Q_LO = 6.0
qlo = Q_LO * np.array([np.cos(theta_g), np.sin(theta_g)])
def lo_density(pts):
    return 1 + A_G * np.cos(pts[:, 1] * qlo[0] + pts[:, 2] * qlo[1])
PL = sprinkle_3d(N, density=lo_density)
cl8 = certificate_v2(PL, K=8)
ok = not cl8["passes"] and cl8["max_w"] > 2.0 * cl8["floor"]
check("the SAME amplitude at low frequency (q = 6, off-grid) is CAUGHT by the "
      "K = 8 certificate (max shadow wD* > 2x floor) — the ghost budget is "
      "high-frequency-only; low-frequency non-uniformity cannot hide from "
      "even 8 directions", ok,
      f"max wD* = {cl8['max_w']:.4f} vs floor {cl8['floor']:.4f}")

# --------------------------------------- CHECK 4 (post-review m9): condition
# (iii) shown LOAD-BEARING — the separator adversary: lift the extension family
# from a DIFFERENT faithful configuration P'. Conditions (i)+(ii) pass trivially
# (the family IS faithful-configuration data), but the reconstruction realizes
# P', not P — (iii) must catch it, or (iii) is decoration.
print("CHECK 4: the separator adversary — (iii) bears load")
P2 = sprinkle_3d(N)
K_ = 8
thetas_ = np.arange(2 * K_) * np.pi / K_
U2 = np.empty((N, 2 * K_))
for k_, th in enumerate(thetas_):
    ref_sorted = np.sort(u_coord(REF, th))
    ranks = np.argsort(np.argsort(u_coord(P2, th)))    # P-prime's family
    q = (ranks + 0.5) / N
    U2[:, k_] = ref_sorted[np.clip((q * len(ref_sorted)).astype(int), 0,
                                   len(ref_sorted) - 1)]
A_ = np.column_stack([np.ones(2 * K_), np.cos(thetas_), np.sin(thetas_)])
coef2, _, _, _ = np.linalg.lstsq(A_, U2.T, rcond=None)
resid2 = float(np.sqrt(np.mean((A_ @ coef2 - U2.T) ** 2)))
R2 = np.column_stack([coef2[0], -coef2[1], -coef2[2]])
ws2 = [certify_shadow(np.column_stack(
    [u_coord(P2, th), u_coord(P2, th + np.pi)]), th)
    for th in thetas_[:K_]]
agree_vs_P = float((order_3d(R2) == order_3d(P)).mean())
cond_i = max(ws2) < 1.3 * floor_max(N, K_)
cond_ii = resid2 < 0.05
cond_iii = agree_vs_P >= 0.98
ok = cond_i and cond_ii and not cond_iii
check("the lifted family passes (i) and (ii) — it is real faithful data — but "
      "FAILS (iii) against the actual input order P (agreement far below 0.98): "
      "condition (iii) is what stops certificate theft between orders; it "
      "bears exactly the load the paper claims", ok,
      f"(i) max wD* {max(ws2):.4f}; (ii) resid {resid2:.4f}; (iii) agreement "
      f"vs P = {agree_vs_P:.3f} => REJECTED")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
