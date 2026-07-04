#!/usr/bin/env python3
"""
q2_sj_vacuum.py — v8 paper 9 §4: the Sorkin–Johnston vacuum on the sealed record
order, 2D diamond demonstrations.

Construction [IMPORT: Johnston 2009; Sorkin 2011; Afshordi–Aslanbeigi–Sorkin 2012]:
  Pauli–Jordan:  Delta = K_R - K_A = K_R - K_R^T   (K_R the retarded propagator)
  i Delta is Hermitian; its nonzero spectrum comes in +/- pairs
  SJ two-point function:  W = pos(i Delta) = (i Delta + |i Delta|)/2
  Defining properties: W is PSD; W - conj(W) = i Delta; W conj(W) = 0
  (equivalently Im W = Delta/2, and W is the positive spectral part).

Held-out scoring: massless 2D center-region log law. The continuum massless
Wightman two-point function behaves as -(1/4 pi) ln(Du Dv) + const on timelike
pairs; in the diamond's center region the SJ state approaches the Minkowski form
[IMPORT: AAS 2012] — scored here as a fitted log-slope against -(1/4 pi), on
center-region timelike pairs, on RAW matrix elements: the discrete W entries
approximate the continuum W(x, y) directly (unit-norm eigenvectors supply the
1/rho measure), so the slope fit is on raw elements vs ln(Du Dv).

Scale/covariance (record-native, paper 9's owned statements): the construction is
a function of C alone (given m^2/rho), so it inherits q1's weight-0 grading and
boost invariance verbatim — re-checked here end-to-end on W.

Float discipline: float64 measurement landscape (eigendecompositions);
analytic anchor 1/(4 pi) mpmath dps = 50. Seed: default_rng(20260702).
Tolerances measured-and-disclosed (DEMONSTRATED grade).
"""

import numpy as np
from mpmath import mp, pi as mppi

mp.dps = 50
rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


def sprinkle_diamond(N):
    uv = rng.random((N, 2))
    C = (uv[None, :, 0] > uv[:, None, 0]) & (uv[None, :, 1] > uv[:, None, 1])
    return uv, C

def retarded_massive(C, m2_over_rho):
    Phi = 0.5 * C.astype(np.float64)
    b = -m2_over_rho
    N = C.shape[0]
    return Phi @ np.linalg.inv(np.eye(N) - b * Phi)

def sj_state(K):
    """W = positive spectral part of i(K - K^T)."""
    iDelta = 1j * (K - K.T)
    lam, V = np.linalg.eigh(iDelta)
    pos = lam > 0
    W = (V[:, pos] * lam[pos]) @ V[:, pos].conj().T
    return iDelta, W, lam


# ------------------------------------------------ CHECK 1: spectral structure
print("CHECK 1: Pauli–Jordan spectral structure (massless, N = 400)")
N = 400
uv, C = sprinkle_diamond(N)
K0 = 0.5 * C.astype(np.float64)
iD, W, lam = sj_state(K0)
herm = np.max(np.abs(iD - iD.conj().T))
srt = np.sort(lam)
npos = int((lam > 1e-9).sum())
nneg = int((lam < -1e-9).sum())
pair = np.max(np.abs(srt[:nneg][::-1] + srt[-npos:])) if npos == nneg else np.inf
ok = herm < 1e-12 and npos == nneg and pair < 1e-9 * max(1.0, srt[-1])
check("i Delta Hermitian; nonzero spectrum exactly +/- paired", ok,
      f"{npos} + / {nneg} - modes; pairing residual {pair:.2e}")

# ------------------------------------------------ CHECK 2: SJ defining identities
print("CHECK 2: the SJ defining identities")
r1 = np.max(np.abs((W - W.conj()) - iD))
r2 = np.max(np.abs(W @ W.conj()))
scale = np.max(np.abs(W))
evW = np.linalg.eigvalsh(W)
ok = r1 < 1e-10 * max(scale, 1) and evW.min() > -1e-10 * scale
check("W - conj(W) = i Delta exactly; W PSD", ok,
      f"identity residual {r1:.2e}, min eig {evW.min():.2e}")
ok = r2 < 1e-8 * scale ** 2
check("ground-state condition W conj(W) = 0", ok, f"residual {r2:.2e}")
imres = np.max(np.abs(np.imag(W) - 0.5 * (K0 - K0.T)))
ok = imres < 1e-10
check("Im W = Delta/2 (the commutator is state-independent)", ok,
      f"residual {imres:.2e}")

# --------------------------------- CHECK 3: eigenvalue scaling with N (kernel -> operator)
print("CHECK 3: Pauli–Jordan eigenvalue scaling")
# the discrete matrix approximates rho x (continuum integral operator): at fixed
# geometry, lambda_max should scale linearly with N
lmaxes = {}
for Nv in (200, 400, 800):
    accs = []
    for _ in range(6):
        uvv, Cv = sprinkle_diamond(Nv)
        iDv = 1j * (0.5 * Cv.astype(np.float64) - 0.5 * Cv.T.astype(np.float64))
        accs.append(np.max(np.linalg.eigvalsh(iDv)))
    lmaxes[Nv] = float(np.mean(accs))
r21 = lmaxes[400] / lmaxes[200]
r42 = lmaxes[800] / lmaxes[400]
ok = 1.85 < r21 < 2.15 and 1.85 < r42 < 2.15
check("lambda_max(i Delta) doubles with N (matrix = rho x continuum operator), "
      "ratio in (1.85, 2.15)", ok, f"ratios {r21:.3f}, {r42:.3f}")

# --------------------------------- CHECK 4: the center-region massless log law
print("CHECK 4: held-out scoring — the center-region log law (massless)")
# continuum: Re W(x,y) = -(1/4 pi) ln(Du Dv) + const on timelike pairs (center
# region of the diamond, where the SJ state approaches the Minkowski form [AAS])
slopes = []
for _ in range(8):
    uvv, Cv = sprinkle_diamond(500)
    _, Wv, _ = sj_state(0.5 * Cv.astype(np.float64))
    ctr = (np.abs(uvv[:, 0] - 0.5) < 0.22) & (np.abs(uvv[:, 1] - 0.5) < 0.22)
    idxs = np.nonzero(ctr)[0]
    xs, ys, zs = [], [], []
    for a_i in range(len(idxs)):
        for b_i in range(a_i + 1, len(idxs)):
            i, j = idxs[a_i], idxs[b_i]
            if Cv[i, j] or Cv[j, i]:
                duv = abs(uvv[i, 0] - uvv[j, 0]) * abs(uvv[i, 1] - uvv[j, 1])
                if duv > 1e-6:
                    xs.append(np.log(duv))
                    ys.append(np.real(Wv[i, j]))
    if len(xs) > 50:
        sl, _ = np.polyfit(xs, ys, 1)
        slopes.append(sl)
slope = float(np.mean(slopes))
target = float(-1 / (4 * mppi))
ok = abs(slope - target) < 0.35 * abs(target) and slope < 0
check("fitted Re W vs ln(Du Dv) slope on center timelike pairs = -(1/4 pi) "
      "within 35% (measured tolerance; 8 seeds x N = 500)", ok,
      f"slope = {slope:.4f}, target = {target:.4f}")

# --------------------------------- CHECK 5: weight-0 grading + boost, end-to-end on W
print("CHECK 5: record-native grading and covariance, end-to-end on W")
uvv, Cv = sprinkle_diamond(300)
_, Wa, _ = sj_state(retarded_massive(Cv, 4.0 / 300.0))
_, Wb, _ = sj_state(retarded_massive(Cv, 16.0 / 1200.0))
ok = np.array_equal(Wa, Wb)
check("W bit-identical under (m, rho) -> (2m, 4rho) at fixed C [EXHIBIT: "
      "definitional via the m^2/rho signature]", ok)
lamb = np.exp(0.8)
uv_b = np.column_stack([uvv[:, 0] * lamb, uvv[:, 1] / lamb])
C_b = (uv_b[None, :, 0] > uv_b[:, None, 0]) & (uv_b[None, :, 1] > uv_b[:, None, 1])
_, Wc, _ = sj_state(retarded_massive(C_b, 4.0 / 300.0))
ok = np.array_equal(Wa, Wc)
check("W bit-identical under a rapidity-0.8 boost of the held-out coordinates", ok)

# --------------------------------- CHECK 6: the massive SJ state exists and is tame
print("CHECK 6: massive SJ state (m^2/rho = 0.04)")
uvv, Cv = sprinkle_diamond(400)
iDm, Wm, lamm = sj_state(retarded_massive(Cv, 0.04))
evWm = np.linalg.eigvalsh(Wm)
r1m = np.max(np.abs((Wm - Wm.conj()) - iDm))
ok = evWm.min() > -1e-9 * np.max(np.abs(Wm)) and r1m < 1e-9 * np.max(np.abs(Wm))
check("massive W PSD and satisfies the defining identity", ok,
      f"min eig {evWm.min():.2e}, residual {r1m:.2e}")
# mass gap direction: the massive PJ top eigenvalue sits BELOW the massless one
# (the correlator is suppressed by the mass) — direction check, same sprinkling
lam0 = np.max(np.linalg.eigvalsh(1j * (0.5 * Cv - 0.5 * Cv.T).astype(complex)))
ok = np.max(lamm) < lam0
check("mass suppresses the top Pauli–Jordan mode (lambda_max(m) < lambda_max(0), "
      "same sprinkling) [direction EXHIBIT — follows from resolvent contraction; "
      "not evidence of massive-correlator physics]", ok,
      f"{np.max(lamm):.2f} < {lam0:.2f}")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
