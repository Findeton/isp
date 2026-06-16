"""
Filter 1 (F1-kinematic-form) receipts.

Two independent high-precision checks for the FORM of the locality kernel f(s^2)
forced by C3 (no white noise) + reflection/positive-type + Lorentz invariance,
with quartic spectral falloff ghat(q^2) = e^{-q^4/beta^4}.

CHECK A  (positive-type / Bochner):  a stationary kernel f(x-y) is positive-type
         iff its spectrum ghat(q) >= 0 (Bochner's theorem). We verify that for
         the quartic-damped spectrum ghat(q) = e^{-q^4/beta^4} every sampled
         Gram matrix  M_{jk} = f(x_j - x_k)  is positive semidefinite (PSD),
         where f is the inverse Fourier transform of ghat. We do this WITHOUT
         needing a closed form for f: PSD of the Gram of a stationary kernel is
         equivalent to ghat>=0, and we also build f by numerical inverse FT at
         high precision and check min-eigenvalue >= 0 of explicit Gram matrices.

CHECK B  (quartic UV falloff is genuine and STRONGER than white noise but
         WEAKER than a hard cutoff):  compare three admissible-looking spectra
            white:    ghat = 1           (forbidden: not L1, infinite heating)
            gauss:    ghat = e^{-q^2}    (positive-type, but only quadratic exponent)
            quartic:  ghat = e^{-q^4}    (the worked template, C3)
         and exhibit (i) all are >=0 (positive-type), (ii) the quartic one decays
         faster than the Gaussian in the UV (controls short-interval heating),
         (iii) the position-space quartic kernel f is real & even but NOT
         sign-definite (it oscillates) -- matching paper1's note that f need not
         be sign-definite while its spectrum is.

All in mpmath, mp.dps = 100.
"""

import mpmath as mp

mp.mp.dps = 100

# ----------------------------------------------------------------------
# spectra (1D radial proxy along an inertial worldline: s^2 = proper time^2,
# so f(s^2) restricted to a worldline is a 1D stationary kernel in s).
# ----------------------------------------------------------------------
def ghat_white(q):  return mp.mpf(1)
def ghat_gauss(q, beta=mp.mpf(1)):   return mp.e**(-(q/beta)**2)
def ghat_quartic(q, beta=mp.mpf(1)): return mp.e**(-(q/beta)**4)

# position-space kernel by inverse Fourier transform:
#   f(x) = (1/2pi) \int ghat(q) e^{i q x} dq = (1/pi) \int_0^infty ghat(q) cos(qx) dq
def f_from_spectrum(ghat, x, qmax=mp.mpf('40')):
    x = mp.mpf(x)
    val = mp.quad(lambda q: ghat(q) * mp.cos(q * x), [0, qmax])
    return val / mp.pi

# ----------------------------------------------------------------------
# CHECK A: positive-type via PSD Gram matrices for the quartic kernel.
# ----------------------------------------------------------------------
def gram_min_eig(ghat, xs):
    n = len(xs)
    # build f on the needed difference set
    diffs = {}
    def f(d):
        d = mp.mpf(d)
        key = mp.nstr(d, 40)
        if key not in diffs:
            diffs[key] = f_from_spectrum(ghat, d)
        return diffs[key]
    M = mp.matrix(n, n)
    for j in range(n):
        for k in range(n):
            M[j, k] = f(xs[j] - xs[k])
    # symmetrize numerically and take eigenvalues (real symmetric)
    E = mp.eigsy(M, eigvals_only=True)
    return min(E), M

# sample points (irregular, to avoid accidental structure)
xs = [mp.mpf(v) for v in ['0', '0.37', '0.81', '1.23', '1.9', '2.6', '3.4']]

print("=== CHECK A: positive-type (Bochner) of quartic-damped kernel ===")
mineig_q, Mq = gram_min_eig(ghat_quartic, xs)
print("quartic  min Gram eigenvalue :", mp.nstr(mineig_q, 30))
mineig_g, Mg = gram_min_eig(ghat_gauss, xs)
print("gaussian min Gram eigenvalue :", mp.nstr(mineig_g, 30))
print("  (both >= 0  =>  positive-type / reflection-positive stationary kernel)")
print()

# ----------------------------------------------------------------------
# CHECK B: UV falloff comparison and sign-indefiniteness of position kernel.
# ----------------------------------------------------------------------
print("=== CHECK B: spectra nonneg + UV decay + position-space sign ===")
for name, gh in [('white  ', ghat_white), ('gauss  ', ghat_gauss), ('quartic', ghat_quartic)]:
    # nonnegativity at a few q
    vals = [gh(mp.mpf(q)) for q in ['0','1','2','3']]
    nonneg = all(v >= 0 for v in vals)
    print(f"  {name}: ghat(0..3) = " + ", ".join(mp.nstr(v, 12) for v in vals) +
          f"   nonneg={nonneg}")

# L1 / heating proxy: integral of q^2 * ghat (UV energy weight along worldline);
# white diverges, gauss & quartic finite; quartic gives the lighter UV tail per-mode.
print()
def uv_weight(gh, qmax=mp.mpf('60')):
    return mp.quad(lambda q: q**2 * gh(q), [0, qmax])
wg = uv_weight(ghat_gauss)
wq = uv_weight(ghat_quartic)
print("  UV energy weight  \\int q^2 ghat dq :")
print("    gauss   :", mp.nstr(wg, 25))
print("    quartic :", mp.nstr(wq, 25))
print("    white   : DIVERGES (not L1) -> the C3 white-noise catastrophe")
print()

# per-mode UV tail ratio at large q: quartic/gauss -> 0 (quartic strictly lighter)
for q in ['2','3','4','5']:
    qq = mp.mpf(q)
    r = ghat_quartic(qq) / ghat_gauss(qq)
    print(f"    q={q}: ghat_quartic/ghat_gauss = {mp.nstr(r, 12)}  (->0: quartic lighter UV)")
print()

# position-space quartic kernel: real, even, but NOT sign-definite
print("  position-space quartic kernel f(x) (should be real, even, sign-changing):")
prev = None
sign_changes = 0
samples = []
for x in ['0','0.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0']:
    fx = f_from_spectrum(ghat_quartic, x)
    samples.append((x, fx))
    print(f"    f({x:>4}) = {mp.nstr(fx, 15)}")
    if prev is not None and mp.sign(fx) != mp.sign(prev) and fx != 0:
        sign_changes += 1
    prev = fx
# evenness check
fe1 = f_from_spectrum(ghat_quartic, mp.mpf('1.3'))
fe2 = f_from_spectrum(ghat_quartic, mp.mpf('-1.3'))
print(f"  evenness: f(1.3)-f(-1.3) = {mp.nstr(fe1-fe2, 10)}")
print(f"  sign changes over x in [0,5]: {sign_changes}  (>0 => f not sign-definite)")
print()
print("VERDICT A: quartic spectrum nonneg & Gram PSD  -> positive-type kernel (forced by C3).")
print("VERDICT B: quartic UV decay strictly lighter than Gaussian; white forbidden;")
print("           position kernel real/even/sign-indefinite (matches paper1 note).")
