#!/usr/bin/env python3
"""
q1_propagator_dalembertian.py — v8 paper 9 §2–§3: the free-scalar first rung on the
sealed record order — retarded propagators (Johnston) and the discrete
d'Alembertian (Sorkin/Benincasa–Dowker), 2D demonstrations.

Methodology (papers 4 §1 / 7 / 8): the record order is built from a coordinate
sprinkling ONLY to test order-only construction — every propagator/operator below
is a function of the causal matrix C and the count alone; coordinates are held out
as scoring ground truth (proper times, continuum comparisons).

Conventions. Unit diamond in lightcone coords (u,v) in [0,1]^2, order = coordinate
dominance; physical coords t = (u+v)/sqrt2, x = (v-u)/sqrt2 (a rotation: volume 1,
rho = N). Proper time between causal pairs: tau = sqrt(2 Du Dv). The BDG limit is
Box in the MOSTLY-PLUS convention: Box_mp f = -2 f_uv in these coordinates.

Constructions [IMPORT: Johnston 2008/2009; Sorkin 2007; Benincasa–Dowker 2010]:
  massless 2D retarded:  K0 = (1/2) C                       (exact in expectation)
  massive  2D retarded:  K_m = Phi (I - b Phi)^(-1),  Phi = (1/2)C,  b = -m^2/rho
  continuum anchors:     G0 = 1/2 inside the cone;  G_m = (1/2) J0(m tau)
  2D BDG d'Alembertian:  B f(x) = (4/l^2) [ -f(x)/2 + (S1 - 2 S2 + S3)(f) ],
                         S_k = sum of f over the k-th past layer, l^2 = 1/rho

Record-native content checked here (paper 9's owned statements):
  (i)  weight-0 grading: K_m = F(C; m^2/rho) exactly — the free-field sector adds
       no scale beyond the walled l_step (paper 3): bit-identical under
       (m, rho) -> (mu m, mu^2 rho) at fixed C;
  (ii) boost invariance: the construction is order-only, so a boost of the
       held-out coordinates leaves C — hence K — bit-identical.

Float discipline: sprinkling/estimation landscape float64 (a measurement);
analytic anchors (J0, layer coefficients) mpmath dps = 50.
Seed: default_rng(20260702). Tolerances are measured-and-disclosed (this is a
DEMONSTRATED-grade receipt, not a proof).
"""

import numpy as np
from mpmath import mp, besselj

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


# --------------------------------------------------------------- sprinkling
def sprinkle_diamond(N):
    uv = rng.random((N, 2))
    C = (uv[None, :, 0] > uv[:, None, 0]) & (uv[None, :, 1] > uv[:, None, 1])
    return uv, C

def retarded_massless(C):
    return 0.5 * C.astype(np.float64)

def retarded_massive(C, m2_over_rho):
    Phi = 0.5 * C.astype(np.float64)
    b = -m2_over_rho
    N = C.shape[0]
    return Phi @ np.linalg.inv(np.eye(N) - b * Phi)


# --------------------------------------- CHECK 1: massless retarded = C/2 exact
print("CHECK 1: massless 2D retarded propagator")
N = 400
uv, C = sprinkle_diamond(N)
K0 = retarded_massless(C)
ok = np.all(K0[C] == 0.5) and np.all(K0[~C] == 0.0)
check("K0 = (1/2)C: 1/2 on causal pairs, 0 elsewhere [EXHIBIT: definitional "
      "on the discrete side; the physics content is the continuum identification]", ok,
      f"{int(C.sum())} causal pairs at N = {N}")

# ------------------------------------- CHECK 2: massive propagator vs (1/2)J0
print("CHECK 2: massive 2D retarded propagator vs the continuum (1/2)J0(m tau)")
m = 4.0
SEEDS = 20
NN = 400
rho = float(NN)
bins = np.linspace(0.05, 1.30, 11)
acc = [[] for _ in bins[:-1]]
for _ in range(SEEDS):
    uv, C = sprinkle_diamond(NN)
    Km = retarded_massive(C, m * m / rho)
    ii, jj = np.nonzero(C)
    taus = np.sqrt(2.0 * (uv[jj, 0] - uv[ii, 0]) * (uv[jj, 1] - uv[ii, 1]))
    vals = Km[ii, jj]
    idx = np.digitize(taus, bins) - 1
    for k in range(len(bins) - 1):
        sel = idx == k
        if sel.sum():
            acc[k].append(vals[sel].mean())
ok = True
worst = 0.0
print("      tau_mid   K_m(binned)   (1/2)J0(m tau)")
for k in range(len(bins) - 1):
    tau_mid = 0.5 * (bins[k] + bins[k + 1])
    target = float(0.5 * besselj(0, m * tau_mid))
    got = float(np.mean(acc[k]))
    err = abs(got - target)
    worst = max(worst, err)
    print(f"      {tau_mid:.3f}     {got:+.4f}       {target:+.4f}")
    if err > 0.04:
        ok = False
check(f"bin-averaged K_m tracks (1/2)J0(m tau), m = {m}, 10 bins x {SEEDS} seeds, "
      f"|err| <= 0.04 per bin (measured tolerance; bin-center vs bin-mean offset "
      f"included)", ok, f"worst bin |err| = {worst:.4f}")

# --------------------------------- CHECK 3: weight-0 grading, bit-identical
print("CHECK 3: the weight-0 grading (record-native)")
uv, C = sprinkle_diamond(300)
K_a = retarded_massive(C, (2.0 ** 2) / 300.0)
K_b = retarded_massive(C, (4.0 ** 2) / 1200.0)
ok = np.array_equal(K_a, K_b)
check("K_m bit-identical under (m, rho) -> (2m, 4rho) at fixed C [EXHIBIT: the "
      "construction's signature carries only m^2/rho — the grading is definitional]", ok)

# --------------------------------------------- CHECK 4: boost invariance
print("CHECK 4: boost invariance (order-only construction)")
lam = np.exp(0.8)
uv_b = np.column_stack([uv[:, 0] * lam, uv[:, 1] / lam])
C_b = (uv_b[None, :, 0] > uv_b[:, None, 0]) & (uv_b[None, :, 1] > uv_b[:, None, 1])
ok = np.array_equal(C, C_b) and np.array_equal(
    retarded_massive(C, 4.0 / 300), retarded_massive(C_b, 4.0 / 300))
check("boosted coordinates (rapidity 0.8) -> identical C -> bit-identical K_m", ok)

# --------------------------------------- CHECK 5: BDG d'Alembertian, three layers
# Signature note: the BDG limit is Box in the MOSTLY-PLUS convention; in our
# (u, v) coordinates Box_mp f = -2 d^2 f/(du dv).
print("CHECK 5: 2D BDG d'Alembertian — exact expectation, discrete pairing, fluctuations")
from scipy import integrate
import sympy as sp

# (5-pre) the three moment identities that make the limit work, sympy-exact,
# and the smeared-weight generating-function identity (added after round-1 review:
# the paper cites these as receipt-checked)
z, epss, mus = sp.symbols("z varepsilon mu", positive=True)
Ker = sp.exp(-z) * (1 - 2 * z + z ** 2 / 2)
M0 = sp.integrate(Ker, (z, 0, sp.oo))
M1 = sp.integrate(Ker * z, (z, 0, sp.oo))
CK = -sp.integrate(Ker * sp.log(z), (z, 0, sp.oo))
ok = M0 == 0 and M1 == 0 and sp.simplify(CK - sp.Rational(1, 2)) == 0
check("kernel moments: M0 = 0, M1 = 0, -Int K ln z = 1/2 [sympy-exact]", ok)
nsym = sp.symbols("n", integer=True, nonnegative=True)
w_sym = (1 - epss) ** nsym * (1 - 2 * epss * nsym / (1 - epss)
         + epss ** 2 * nsym * (nsym - 1) / (2 * (1 - epss) ** 2))
gen = sp.summation(w_sym * sp.exp(-mus) * mus ** nsym / sp.factorial(nsym),
                   (nsym, 0, sp.oo))
tgt_gen = sp.exp(-epss * mus) * (1 - 2 * epss * mus + (epss * mus) ** 2 / 2)
ok = sp.simplify(sp.expand(gen - tgt_gen)) == 0
check("smeared weights: sum_n w(n) Poisson(n; mu) = e^{-eps mu}(1 - 2 eps mu + "
      "(eps mu)^2/2) [sympy-exact]", ok)

ctrB, s2b = (0.6, 0.6), 0.02
def f_uv(u, v):
    return np.exp(-((u - ctrB[0]) ** 2 + (v - ctrB[1]) ** 2) / (2 * s2b))

def boxf_mp(u, v):
    return -2.0 * ((u - ctrB[0]) * (v - ctrB[1]) / (s2b * s2b)) * f_uv(u, v)

# (5a) the exact finite-rho expectation of the UNSMEARED operator at a point,
# via the Poisson kernel K(z) = e^-z (1 - 2z + z^2/2), converging to Box_mp f
def EB_exact(rho, x):
    xu, xv = x
    def K(z):
        return np.exp(-z) * (1 - 2 * z + 0.5 * z * z)
    def inner(a):
        g = lambda z: K(z) * f_uv(xu - a, xv - z / (rho * a))
        val, _ = integrate.quad(g, 0, min(60.0, rho * a * xv), limit=200)
        return val / (rho * a)
    val, _ = integrate.quad(inner, 1e-10, xu, limit=400)
    return 4 * rho * (-0.5 * f_uv(xu, xv) + rho * val)

xeval = (0.75, 0.75)
target_pt = boxf_mp(*xeval)
rows = [(rho, EB_exact(float(rho), xeval)) for rho in (512, 2048, 8192, 32768)]
print("      rho       E_rho[Bf]    Box_mp f =", f"{target_pt:.3f}")
for rho, e in rows:
    print(f"      {rho:<8}  {e:9.3f}")
errs = [abs(e - target_pt) / abs(target_pt) for _, e in rows]
ok = errs[0] < 0.10 and all(e < 0.01 for e in errs[1:])
check("exact finite-rho expectation converges to Box_mp f: < 10% at rho = 512, "
      "inside the 1% band from rho = 2048 on (the ~0.3% plateau is the finite-"
      "diamond boundary residual, which does not vanish with rho; semi-analytic, "
      "no matrices)", ok,
      f"rel errs {', '.join(f'{e:.4f}' for e in errs)}")

# (5b) the SMEARED discrete operator B_eps [IMPORT: Sorkin's damped/smeared form],
# weights w(n) = (1-eps)^n [1 - 2 eps n/(1-eps) + eps^2 n(n-1)/(2(1-eps)^2)],
# B_eps f = 4 eps rho [ -f/2 + eps sum w(n) f ]; in expectation = unsmeared at
# rho_eff = eps rho. Scored as a VOLUME PAIRING <g, B_eps f>/rho vs <g, Box_mp f>
# (point evaluations do not self-average; the pairing does).
gctr, s2g = (0.78, 0.78), 0.004
def g_uv(u, v):
    return np.exp(-((u - gctr[0]) ** 2 + (v - gctr[1]) ** 2) / (2 * s2g))

tgt, _ = integrate.dblquad(lambda v, u: g_uv(u, v) * boxf_mp(u, v),
                           0, 1, 0, 1, epsabs=1e-10)
NB, EPS, SEEDS_B = 2048, 0.125, 40
vals = []
for _ in range(SEEDS_B):
    uvB, CB = sprinkle_diamond(NB)
    fv = f_uv(uvB[:, 0], uvB[:, 1])
    gv = g_uv(uvB[:, 0], uvB[:, 1])
    Cf = CB.astype(np.float32)
    btw = np.rint(Cf @ Cf).astype(np.float64)
    w = (1 - EPS) ** btw * (1 - 2 * EPS * btw / (1 - EPS)
                            + EPS * EPS * btw * (btw - 1) / (2 * (1 - EPS) ** 2))
    w = np.where(CB, w, 0.0)
    Bfx = 4 * EPS * NB * (-0.5 * fv + EPS * (w.T @ fv))
    vals.append(float((gv * Bfx).sum() / NB))
mean_p, sem_p = float(np.mean(vals)), float(np.std(vals) / np.sqrt(SEEDS_B))
ok = abs(mean_p - tgt) <= max(0.25 * abs(tgt), 2 * sem_p) and \
     mean_p * tgt > 0 and abs(mean_p) > 3 * sem_p
check(f"smeared pairing <g, B_eps f>/rho (N = {NB}, eps = {EPS}, {SEEDS_B} seeds) "
      f"matches the continuum <g, Box_mp f> within max(25%, 2 SEM), sign at > 3 SEM",
      ok, f"mean = {mean_p:.4f} +/- {sem_p:.4f}, target = {tgt:.4f}")

# (5c) fluctuation honesty: UNSMEARED point evaluations do not self-average
def bdg_point(C, between, fvals, x, rho):
    past = C[:, x]
    nb = between[:, x]
    s1 = fvals[past & (nb == 0)].sum()
    s2 = fvals[past & (nb == 1)].sum()
    s3 = fvals[past & (nb == 2)].sum()
    return (4.0 * rho) * (-0.5 * fvals[x] + (s1 - 2.0 * s2 + s3))

stds = {}
for NBv in (128, 512):
    pts = []
    for _ in range(30):
        uvB, CB = sprinkle_diamond(NBv)
        fv = f_uv(uvB[:, 0], uvB[:, 1])
        Cf = CB.astype(np.float32)
        btw = np.rint(Cf @ Cf).astype(np.int32)
        xe = int(np.argmin((uvB[:, 0] - xeval[0]) ** 2 + (uvB[:, 1] - xeval[1]) ** 2))
        pts.append(bdg_point(CB, btw, fv, xe, float(NBv)))
    stds[NBv] = float(np.std(pts))
ok = stds[512] > 0.5 * stds[128]
check("fluctuation honesty: per-sprinkling std of the UNSMEARED point value does "
      "NOT decay with N (the known BDG fluctuation problem — the smeared form "
      "above is the standard cure [IMPORT])", ok,
      f"std(N=128) = {stds[128]:.1f}, std(N=512) = {stds[512]:.1f}")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
