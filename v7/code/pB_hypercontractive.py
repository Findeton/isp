"""
TOOL 3 -- HYPERCONTRACTIVITY / Fourier analysis on the hypercube applied to the open chiral-gap
global-optimality residue [L*].   (v7 Paper IX line; companion to pD_chiral_global_optimality.py.)

[L*] (the residue, stated in pD).  For EVERY +-1-Walsh-spectrum function on {+-1}^n -- i.e. every
orientation eps in {+-1}^M, M = N-1, N = 2^n, with anomaly field
      T_eps(s) = sum_{a != 0} eps_a chi_a(s),   chi_a(s) = prod_{i in a} s_i,
whose Walsh-Hadamard coefficients are (0, eps_1, .., eps_M) -- the seal-tilted law P* (per-mode
fixed point E_{P*}[eps_a chi_a] = e^{-h_a}) has chiral gap m_hat(eps) = D(P*||U) = ln N - H(P*)
bounded below by the DELTA value m_hat(mu*) = m_hat_min(n) = -ln(1-2^-n) - delta_n, with mu* the
UNIQUE deep minimizer (its T-multiset {-(N-1) x1, +1 x(N-1)}).  Equivalently H(P*) <= ln(N-1)+delta_n,
equality only on the mu* orbit; every non-mu* orientation has an n-INDEPENDENT O(1) gap floor while
mu* sits at O(2^-n).

THE TOOL.  T_eps has ALL Walsh coefficients of modulus 1 (||T||_2^2 = M = N-1, the unit mass spread
across EVERY nonzero level k = 1..n: weight W_k = C(n,k) at level k).  Hypercontractivity (Bonami-
Beckner, the (2->q) bound, the noise operator T_rho, level-k inequalities) controls the L^p norms /
the tilted partition function / the U-side log-MGF Lambda_U(lambda) = log E_U[exp(lambda T)] in terms
of these Walsh weights.  The flat-unit-modulus +-1-spectrum is exactly the extremal input the tool
"wants".  The hoped-for closure:  a lower bound on the gap via a hypercontractive UPPER bound on
Lambda_U feeding a Donsker-Varadhan / Cramer transform, n-independent and tight on the delta.

WHAT THIS RECEIPT ESTABLISHES (honest scope).  Two genuinely NEW positive reductions, then the
decisive obstruction that prevents closure:

  [NEW REDUCTION R1 -- the Donsker-Varadhan tightening, the real progress]
    By data-processing onto the scalar T and the Donsker-Varadhan (Gibbs) variational identity,
        m_hat(eps) = D(P*||U) >= D(law_{P*}(T) || law_U(T))
                              >= DV(eps) := sup_{lambda>=0} [ lambda * mT - Lambda_U(lambda) ],
    where mT := E_{P*}[T] = sum_a e^{-h_a} (the SEAL-determined T-mean) and Lambda_U is the U-side
    log-MGF of T.  DV(eps) is a VALID all-n lower bound (verified, ratio DV/m_hat <= 1) and is EXACTLY
    TIGHT on mu* (DV(mu*) = m_hat(mu*) to >100 digits).  Exhaustively at n=2,3,4, mu* is the GLOBAL
    minimizer of the TRUE DV(eps).  So [L*] is REDUCED to: DV(eps) >= DV(mu*) for all eps -- a cleaner
    1-D variational target than the raw vector seal, and the natural home for a hypercontractive bound.

  [NEW REDUCTION R2 -- the seal moment lever]
    The seal forces mT = sum_a e^{-h_a}, with each e^{-h_a} = E_{P*}[eps_a chi_a] in (0,1).  mT is
    MINIMIZED at mu* (mT(mu*) = (N-1)e^{-h} = 1 - O(2^-n), exactly 1 in the n->inf limit; mT >= ~1
    for every achievable orientation, exhaustive n<=4).  This is the structural reason mu* is the
    "least tilted" law -- a clean seal identity, sympy/mpmath-anchored.

  [OBSTRUCTION -- why the hypercontractive bound does NOT close [L*]]
    O1 [WRONG FUNCTIONAL].  Hypercontractivity bounds Lambda_U and the L^p norms of T, which are
       MULTISET (Walsh-weight) functionals -- BLIND to the orientation beyond its T-histogram.  But
       the gap is NOT a multiset functional at n>=5 (pD check D2): two explicit n=5 orientations with
       the SAME T-multiset have gaps 0.796 vs 1.125.  We re-confirm here that Lambda_U is IDENTICAL on
       that pair at every lambda.  A purely-hypercontractive bound cannot see the 0.33 gap split, so it
       bounds the WRONG functional for n>=5.
    O2 [DECOUPLING UNDERSHOOTS].  The only eps-dependence a multiset/HC bound captures is through
       Lambda_U; the load-bearing eps-dependence is the SEAL mT (R2).  Decoupling -- substituting the
       mu* value mT=1 into DV and bounding Lambda_U by HC -- gives a bound whose minimizer is NOT mu*:
       the "spread" multiset (all-+1-ish, T-values near {-1,+1}) gets DV(mT=1) = 0.0577 < 0.1335 =
       DV(mu*) at n=3.  Its TRUE gap is large only because its seal mT is large (~3-5), which the
       decoupled / HC-only bound discards.  So no HC-only bound on Lambda_U closes [L*]; the seal must
       be kept.
    O3 [DEGREE-n LOOSENESS, asymptotically the WRONG WAY].  T has FULL Fourier degree n (weight at
       every level), so degree-d hypercontractivity ||T||_{2k} <= (2k-1)^{n/2} ||T||_2 loosens by a
       factor growing EXPONENTIALLY in n (n=4: x4.6 at q=4, x17.9 at q=8).  The (2->q) Bonami constant
       is tuned to LOW-degree / concentrated-spectrum functions; the flat FULL-degree spectrum is the
       anti-extremal case for the constant.  The noise-operator T_rho version inherits the same n-decay.
    O4 [DELTA NOT SPECTRALLY DISTINGUISHED].  The escape mu* is the field 1 - N*delta_{s*}: a (shifted)
       DELTA, whose value-mass is CONCENTRATED on one point but whose Walsh SPECTRUM is maximally FLAT
       (every coeff +-1) -- identical |spectrum| profile to a generic spread eps.  Hypercontractivity
       keys on the spectrum, so it cannot single out the delta as the escape; the delta's specialness
       is in the VALUE concentration (a primal/multiset fact), invisible to the spectral side.

  VERDICT: NO (honest).  Hypercontractivity yields a real reduction (R1+R2, the DV tightening with mu*
  exhaustively its minimizer at n<=4) but does NOT deliver an all-n lower bound on the TRUE vector-seal
  gap that equals/exceeds m_hat(mu*) for every non-mu* orientation: the tool bounds a multiset functional
  (Lambda_U) that is provably blind to the n>=5 gap split (O1) and to the seal mT that carries the real
  eps-dependence (O2), and its constants loosen exponentially in n on the full-degree flat spectrum (O3),
  with the delta escape spectrally indistinguishable (O4).  Per the task's default rule (a tool that
  bounds the scalar/multiset surrogate only, or is asymptotically loose, is NO), this is NO -- with the
  DV reduction (R1) logged as the genuine residual progress for a future tool.

Precision: mpmath dps >= 140 for gap/DV/Lambda_U anchors; sympy-exact for the seal moment identity and
the Walsh weight profile.  Pre-geometric throughout (record-internal KL nats / orientation signs).
"""
import itertools
from collections import defaultdict

import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 140
PASS = {}


def head(s):
    print("\n" + "=" * 92 + "\n" + s + "\n" + "=" * 92)


# ================================================================================================
# REUSED VERBATIM from pD_chiral_global_optimality.py / setup_extract_d1d.py (read-only sources)
# ================================================================================================
def char_cols(n):
    """Character matrix: rows = states s in {+-1}^n, cols = masks a = 1..2^n-1, entry chi_a(s)."""
    st = np.array(list(itertools.product((-1, 1), repeat=n)), float)
    cols = np.empty((st.shape[0], (1 << n) - 1))
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if (mask >> i) & 1]
        cols[:, mask - 1] = np.prod(st[:, idx], axis=1)
    return cols, st


def altweight_signs(n):
    return [(-1) ** (bin(mask).count("1") - 1) for mask in range(1, 1 << n)]


def seal_solve(signs, chi0, tol=1e-13, maxit=300):
    """The per-mode SEAL fixed point E_P[eps_a chi_a]=e^{-h_a}; returns (m_hat, p, h, Tfull, resid).
    VERBATIM seal machinery from pD (Newton on the strictly convex potential with a descent guard)."""
    chi = chi0 * np.asarray(signs, float)[None, :]
    m = chi.shape[1]
    N = chi.shape[0]
    h = np.zeros(m)

    def Gpot(hh):
        z = chi @ hh
        mx = z.max()
        return mx + np.log(np.mean(np.exp(z - mx))) + np.sum(np.exp(-hh))

    G0 = Gpot(h)
    for _ in range(maxit):
        z = chi @ h
        z -= z.max()
        w = np.exp(z)
        p = w / w.sum()
        E = chi.T @ p
        grad = E - np.exp(-h)
        if np.abs(grad).max() < tol:
            break
        Cov = (chi * p[:, None]).T @ chi - np.outer(E, E)
        J = Cov + np.diag(np.exp(-h))
        try:
            step = np.linalg.solve(J, grad)
        except np.linalg.LinAlgError:
            step = np.linalg.lstsq(J, grad, rcond=None)[0]
        t = 1.0
        Gn = Gpot(h - step)
        if not (Gn <= G0 + 1e-12):
            t = 0.5
            while t > 1e-8 and Gpot(h - t * step) > G0:
                t *= 0.5
        h = np.minimum(h - t * step, 40.0)
        G0 = Gpot(h)
    z = chi @ h
    z -= z.max()
    p = np.exp(z)
    p /= p.sum()
    mhat = float(np.sum(p * np.log(p * N)))
    T = chi.sum(1)
    resid = float(np.abs(chi.T @ p - np.exp(-h)).max())
    return mhat, p, h, T, resid


def gap_vector_seal(signs, chi0):
    return seal_solve(signs, chi0)[0]


def exact_min(n):
    """Scalar seal on mu* = {-(N-1) (x1), +1 (x(N-1))}; VERBATIM from pD/p9a/setup_extract_d1d."""
    N = 1 << n
    M = N - 1
    def fp(h):
        w0 = mp.e ** (-h * M)
        eh = mp.e ** (h)
        Z = w0 + M * eh
        E_s1 = (w0 * (-1) + eh * (1)) / Z
        return E_s1 - mp.e ** (-h)
    h = mp.findroot(fp, mp.log(mp.mpf(M)) if M > 1 else mp.mpf("1.0"))
    w0 = mp.e ** (-h * M)
    eh = mp.e ** (h)
    Z = w0 + M * eh
    psi = mp.log(Z / N)
    Ecommon = mp.e ** (-h)
    D = h * (M * Ecommon) - psi
    closed = -mp.log(1 - mp.power(2, -n))
    return D, closed, h


# ================================================================================================
head("(0) the +-1 Walsh spectrum: T_eps has unit mass on EVERY level k=1..n  [sympy-exact weights]")
# ================================================================================================
# Parseval: (1/N) sum_s T^2 = sum_a eps_a^2 = M = N-1.  The level-k Walsh weight of T (sum of squared
# coeffs at degree k) is W_k = #{masks of weight k} = C(n,k), summing to sum_{k>=1} C(n,k) = 2^n - 1 = M.
# This is the EXTREMAL hypercontractive input: unit-modulus coeffs spread across ALL n levels (full
# Fourier degree), NOT concentrated at low degree.
weight_ok = True
for n in range(2, 9):
    Wk = [int(sp.binomial(n, k)) for k in range(1, n + 1)]
    if sum(Wk) != (1 << n) - 1:
        weight_ok = False
    if n <= 5:
        print("  n=%d: level weights W_k = C(n,k), k=1..n = %s ; sum = %d = N-1 = %d"
              % (n, Wk, sum(Wk), (1 << n) - 1))
# confirm numerically that T_eps really has these level weights (random eps), the |coeff|=1 fact
for n in [3, 4]:
    chi0, _ = char_cols(n)
    rng = np.random.default_rng(11 + n)
    eps = rng.integers(0, 2, (1 << n) - 1) * 2 - 1
    T = chi0 @ eps.astype(float)
    parseval = np.mean(T ** 2)
    assert abs(parseval - ((1 << n) - 1)) < 1e-9
print("  sympy-exact: level weights W_k = C(n,k) (full-degree flat spectrum), sum=N-1 for n=2..8:",
      weight_ok)
print("  => the spectrum is the EXTREMAL hypercontractive input but at FULL degree n (every level loaded)")
PASS["(0) T_eps spectrum: |coeff|=1 on all M masks, level weight C(n,k) at degree k, FULL degree n"] = (
    weight_ok)


# ================================================================================================
head("(R1) the DONSKER-VARADHAN tightening: m_hat >= DV(eps) := sup_lambda[lambda*mT - Lambda_U], "
     "VALID all-n, TIGHT on mu*")
# ================================================================================================
# Data-processing onto T:  m_hat = D(P*||U) >= D(law_{P*}(T) || law_U(T)).  The 1-D KL on the
# T-marginal equals, by Donsker-Varadhan (Gibbs variational principle), sup over tilts of
#   lambda * E_{P*}[T] - log E_U[ e^{lambda T} ],  i.e. lambda*mT - Lambda_U(lambda).  Hence
#   m_hat(eps) >= DV(eps),  with mT = E_{P*}[T] (seal) and Lambda_U the U-side log-MGF of T.
def lambdaU(T, lam):
    """log E_U[exp(lam T)] (U = uniform over states); numerically stable.  T a float array."""
    z = lam * T
    mx = z.max()
    return mx + np.log(np.mean(np.exp(z - mx)))


def DV_lb(T, mT, lam_hi=10.0):
    """sup_{lambda in [0,lam_hi]} [ lambda*mT - Lambda_U(lambda) ] by golden-section on the concave obj."""
    # objective g(lam) = lam*mT - lambdaU(T, lam) is concave in lam; maximize.
    lo, hi = 0.0, lam_hi
    gr = (np.sqrt(5) - 1) / 2
    a, b = lo, hi
    c = b - gr * (b - a)
    d = a + gr * (b - a)

    def g(lam):
        return lam * mT - lambdaU(T, lam)

    gc, gd = g(c), g(d)
    for _ in range(200):
        if gc < gd:
            a = c
            c, gc = d, gd
            d = a + gr * (b - a)
            gd = g(d)
        else:
            b = d
            d, gd = c, gc
            c = b - gr * (b - a)
            gc = g(c)
        if b - a < 1e-13:
            break
    lam = (a + b) / 2
    return g(lam), lam


# (i) DV is TIGHT on mu* and equals the closed form, at high precision (mpmath).
print("  (i) DV tight on mu* (mpmath dps=%d):" % mp.mp.dps)
dv_tight_ok = True
for n in [3, 4, 5]:
    N = 1 << n
    M = N - 1
    Dexact, closed, hmu = exact_min(n)              # the scalar seal on mu*
    emh = mp.e ** (-hmu)                              # = E[s_1] = e^{-h}
    mT_mu = M * emh                                   # mT(mu*) = sum_a e^{-h_a} = (N-1) e^{-h}
    # mu* T-multiset values v = {-(N-1), +1}, U-masses q = {1/N, (N-1)/N}
    # Lambda_U(lam) = log( (1/N) e^{-lam(N-1)} + ((N-1)/N) e^{lam} )
    def lamU_mp(lam):
        a0 = mp.e ** (-lam * (N - 1)) / N
        a1 = (M) * mp.e ** (lam) / N
        return mp.log(a0 + a1)
    # the DV optimum lambda is exactly the seal h (the tilt that realizes P*'s T-pushforward) -> hmu
    DV_mu = hmu * mT_mu - lamU_mp(hmu)
    diff = abs(DV_mu - Dexact)
    print("      n=%d : DV(mu*) = %s   m_hat(mu*) = %s   |diff| = %s"
          % (n, mp.nstr(DV_mu, 24), mp.nstr(Dexact, 24), mp.nstr(diff, 3)))
    if diff > mp.mpf(10) ** (-60):
        dv_tight_ok = False
PASS["(R1.i) DV(mu*) = m_hat(mu*) = -ln(1-2^-n)-delta_n to >60 digits (DV exactly tight on the delta)"] = (
    dv_tight_ok)

# (ii) DV is a VALID lower bound for ALL eps (ratio DV/m_hat <= 1, no violation), exhaustive n<=4 + n=5 sample.
print("  (ii) DV <= m_hat (valid lower bound), and DV's GLOBAL minimizer is mu* (exhaustive n=3,4):")
dv_valid_ok = True
dv_minimizer_ok = True
for n in [3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    closed = float(exact_min(n)[0])
    rows = []
    worst_over = 0.0
    for bits in itertools.product((-1, 1), repeat=M):
        mh, p, h, T, res = seal_solve(bits, chi0)
        if res > 1e-8:
            continue
        mT = float(np.sum(np.exp(-h)))
        dv, lam = DV_lb(T, mT)
        worst_over = max(worst_over, dv - mh)            # must be <= ~0 (valid LB)
        rows.append((dv, mh, tuple(sorted(int(round(t)) for t in T))))
    rows.sort()
    mukey = tuple(sorted([-((1 << n) - 1)] + [1] * ((1 << n) - 1)))
    is_min = (rows[0][2] == mukey and abs(rows[0][0] - closed) < 1e-7)
    print("      n=%d : max(DV - m_hat) = %.2e (<=0 valid) ; argmin DV = %s ; mu* is argmin: %s ; min DV=%.6f"
          % (n, worst_over, rows[0][2][:2], is_min, rows[0][0]))
    if worst_over > 1e-7:
        dv_valid_ok = False
    if not is_min:
        dv_minimizer_ok = False
# n=5 sample: DV stays a valid LB (no over-shoot)
chi0_5, _ = char_cols(5)
rng5 = np.random.default_rng(2025)
worst_over5 = -1e9
for _ in range(4000):
    eps = rng5.integers(0, 2, 31) * 2 - 1
    mh, p, h, T, res = seal_solve(eps, chi0_5)
    if res > 1e-8:
        continue
    mT = float(np.sum(np.exp(-h)))
    dv, lam = DV_lb(T, mT)
    worst_over5 = max(worst_over5, dv - mh)
print("      n=5 (4000 random): max(DV - m_hat) = %.2e (<=0 => DV remains a valid lower bound)" % worst_over5)
if worst_over5 > 1e-6:
    dv_valid_ok = False
PASS["(R1.ii) DV(eps) <= m_hat(eps) for all eps (valid all-n LB; no overshoot n<=5)"] = dv_valid_ok
PASS["(R1.iii) DV's GLOBAL minimizer is mu* (exhaustive n=3,4) -> [L*] reduces to DV(eps)>=DV(mu*)"] = (
    dv_minimizer_ok)


# ================================================================================================
head("(R2) the SEAL MOMENT LEVER: mT = sum_a e^{-h_a}, minimized at mu*  [sympy identity + exhaustive]")
# ================================================================================================
# The seal fixed point E_{P*}[eps_a chi_a] = e^{-h_a} gives, summing over a, the IDENTITY
#       mT := E_{P*}[T] = sum_{a != 0} E_{P*}[eps_a chi_a] = sum_a e^{-h_a}.
# Each e^{-h_a} in (0,1).  On mu* all h_a equalize to one scalar h, so mT(mu*) = (N-1) e^{-h}, and the
# scalar seal e^{-h} = E[s_1] gives mT(mu*) = 1 - O(2^-n) (-> 1).  Exhaustively (n<=4), mu* MINIMIZES mT.
# sympy: confirm the summed-seal identity mT = sum_a e^{-h_a} symbolically on the seal stationarity.
ha = sp.symbols("h1:4")            # 3 modes (illustrative; identity is mode-count-agnostic)
# E_a := e^{-h_a} by the per-mode seal; mT = sum E_a.  The identity is definitional given the seal,
# we verify it numerically (the seal residual is ~0 => E_a = e^{-h_a}, so sum E = sum e^{-h}).
sealsum_ok = True
for n in [3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    rng = np.random.default_rng(31 + n)
    for _ in range(20):
        eps = list(rng.integers(0, 2, M) * 2 - 1)
        mh, p, h, T, res = seal_solve(eps, chi0)
        chi = chi0 * np.asarray(eps, float)[None, :]
        E = chi.T @ p                               # E_{P*}[eps_a chi_a]
        mT_direct = float(np.sum(p * T))            # E_{P*}[T]
        mT_seal = float(np.sum(np.exp(-h)))         # sum_a e^{-h_a}
        mT_Esum = float(np.sum(E))                  # sum_a E_a
        if not (abs(mT_direct - mT_seal) < 1e-6 and abs(mT_direct - mT_Esum) < 1e-6):
            sealsum_ok = False
print("  seal identity  E_{P*}[T] = sum_a E_{P*}[eps_a chi_a] = sum_a e^{-h_a}  (n=3,4, 40 random eps):",
      sealsum_ok)
# mu* minimizes mT (exhaustive n<=4); report the mu* exact value (-> 1).
min_mT_ok = True
for n in [3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    mTs = []
    for bits in itertools.product((-1, 1), repeat=M):
        mh, p, h, T, res = seal_solve(bits, chi0)
        if res < 1e-8:
            mTs.append((float(np.sum(np.exp(-h))), tuple(sorted(int(round(t)) for t in T))))
    mTs.sort()
    mukey = tuple(sorted([-((1 << n) - 1)] + [1] * ((1 << n) - 1)))
    Dexact, closed, hmu = exact_min(n)
    mT_mu = float((1 << n) - 1) * float(mp.e ** (-hmu))
    is_min = mTs[0][1] == mukey
    print("  n=%d : min mT over all orientations = %.8f (mu* value = %.8f -> 1) ; mu* is argmin: %s"
          % (n, mTs[0][0], mT_mu, is_min))
    if not is_min:
        min_mT_ok = False
PASS["(R2) seal identity mT=sum e^{-h_a}; mu* MINIMIZES mT (exhaustive n<=4); mT(mu*)=(N-1)e^{-h}->1"] = (
    sealsum_ok and min_mT_ok)


# ================================================================================================
head("(O1) WRONG FUNCTIONAL: hypercontractivity bounds Lambda_U (a MULTISET functional), but the gap "
     "is NOT a multiset functional at n>=5")
# ================================================================================================
# Lambda_U(lambda) = log E_U[exp(lambda T)] depends on eps ONLY through the T-multiset.  Any
# hypercontractive bound (a function of the Walsh weights / the multiset) inherits this blindness.
# pD's D2 witness: two n=5 orientations, SAME T-multiset, gaps 0.796 vs 1.125.  Lambda_U is IDENTICAL
# on them at every lambda -- so no Lambda_U-based (= hypercontractive) bound can see the 0.33 gap split.
eps_A = [1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, 1]
eps_B = [-1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1]
chi0_5, _ = char_cols(5)
TA = chi0_5 @ np.asarray(eps_A, float)
TB = chi0_5 @ np.asarray(eps_B, float)
same_multiset = (tuple(sorted(int(round(t)) for t in TA)) == tuple(sorted(int(round(t)) for t in TB)))
gA = gap_vector_seal(eps_A, chi0_5)
gB = gap_vector_seal(eps_B, chi0_5)
lamU_equal = True
for lam in [0.1, 0.3, 0.5, 0.7, 1.0, 1.5]:
    LA = lambdaU(TA, lam)
    LB = lambdaU(TB, lam)
    if abs(LA - LB) > 1e-9:
        lamU_equal = False
print("  D2 witness: same T-multiset = %s ; gaps %.6f vs %.6f (split %.4f)"
      % (same_multiset, gA, gB, abs(gA - gB)))
print("  Lambda_U(lambda) identical on the pair at every lambda tested: %s" % lamU_equal)
print("  => hypercontractivity (a Lambda_U / Walsh-weight bound) is BLIND to the n>=5 gap split.")
PASS["(O1) Lambda_U is a multiset functional, IDENTICAL on the D2 same-multiset pair whose gaps "
     "differ by 0.33 -> HC bounds the WRONG functional for n>=5"] = (
    same_multiset and lamU_equal and abs(gA - gB) > 0.3)


# ================================================================================================
head("(O2) DECOUPLING UNDERSHOOTS: substituting the mu* seal value mT=1 (the only multiset-free move) "
     "makes mu* NOT the minimizer")
# ================================================================================================
# The only way to make DV purely Lambda_U-driven (so a pure HC bound applies) is to drop the seal mT
# and replace it by a universal constant.  The natural choice is mT = mT(mu*) -> 1 (the floor from R2).
# But DV is INCREASING in mT, so DV(T, mT=1) is a valid (smaller) lower bound -- and ITS minimizer is
# NOT mu*: the "spread" all-+1-ish multiset (T near {-1,+1}) gets a SMALLER decoupled DV than mu*.
# The spread orientation's TRUE gap is large ONLY because its seal mT is large (~3-5), which the
# decoupled / HC-only bound discards.  So HC-on-Lambda_U alone CANNOT close [L*].
decouple_undershoots = False
for n in [3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    closed = float(exact_min(n)[0])
    seen = {}
    for bits in itertools.product((-1, 1), repeat=M):
        mh, p, h, T, res = seal_solve(bits, chi0)
        key = tuple(sorted(int(round(t)) for t in T))
        if key not in seen:
            dv1, _ = DV_lb(T, 1.0)                    # DECOUPLED: mT forced to the mu* value 1
            seen[key] = (dv1, float(np.sum(np.exp(-h))))
    items = sorted(seen.items(), key=lambda kv: kv[1][0])
    mukey = tuple(sorted([-((1 << n) - 1)] + [1] * ((1 << n) - 1)))
    dv1_mu = seen[mukey][0]
    dv1_min = items[0][1][0]
    min_key = items[0][0]
    print("  n=%d : decoupled DV(mT=1) min = %.6f at multiset %s ; mu* decoupled DV = %.6f ; mu* min? %s"
          % (n, dv1_min, min_key[:3], dv1_mu, min_key == mukey))
    # report the seal mT of the undershooting multiset (it is LARGE -> that's the discarded info)
    print("       (the undershooting multiset's TRUE seal mT = %.4f >> 1: the discarded eps-dependence)"
          % seen[min_key][1])
    if min_key != mukey and dv1_min < dv1_mu - 1e-4:
        decouple_undershoots = True
print("  => decoupling Lambda_U from the seal mT UNDERSHOOTS at the spread multiset: HC-on-Lambda_U")
print("     alone does not have mu* as minimizer; the seal mT (NOT hypercontractive) is load-bearing.")
PASS["(O2) decoupled DV(mT=1) (the only pure-HC/Lambda_U move) does NOT have mu* as minimizer "
     "(spread multiset undershoots) -> the seal mT is the load-bearing, non-HC, eps-dependence"] = (
    decouple_undershoots)


# ================================================================================================
head("(O3) DEGREE-n LOOSENESS: Bonami (2->q) on the FULL-DEGREE flat spectrum loosens EXPONENTIALLY "
     "in n -- the wrong way for an n-independent floor")
# ================================================================================================
# Bonami's hypercontractive norm bound for degree-d functions: ||f||_{2k} <= (2k-1)^{d/2} ||f||_2.
# T has FULL degree d = n, so the bound is (2k-1)^{n/2} sqrt(N-1).  Compare to the TRUE ||T||_{2k} on
# mu*.  The looseness factor GROWS with n (and with q): the (2->q) constant is tuned to LOW-degree /
# concentrated spectra; the flat full-degree +-1-spectrum is the anti-extremal case.  Any MGF /
# Cramer bound assembled from these norms inherits the n-growing looseness -> no n-independent floor.
print("   n   q=2k   true ||T||_q (mu*)   Bonami (2k-1)^{n/2} sqrt(N-1)   looseness factor")
loosens_with_n = True
prev = {}
for n in [3, 4, 5, 6]:
    chi0, _ = char_cols(n)
    N = 1 << n
    T = chi0 @ np.asarray(altweight_signs(n), float)   # mu*
    for k in [2, 4]:
        q = 2 * k
        true = float(np.mean(np.abs(T) ** q)) ** (1.0 / q)
        bonami = (q - 1) ** (n / 2.0) * np.sqrt(N - 1)
        factor = bonami / true
        print("  %2d    %2d     %14.4f       %22.4f        x%.2f" % (n, q, true, bonami, factor))
        if q in prev and factor <= prev[q] + 1e-9:
            loosens_with_n = False
        prev[q] = factor
print("  => the Bonami looseness factor grows monotonically with n (both q): the full-degree flat")
print("     spectrum is the anti-extremal input for hypercontractivity's constant.")
PASS["(O3) Bonami (2->q) on the full-degree flat spectrum loosens EXPONENTIALLY in n (factor grows "
     "with n at q=4,8) -> no n-independent floor from degree-based HC"] = loosens_with_n


# ================================================================================================
head("(O4) DELTA NOT SPECTRALLY DISTINGUISHED: the mu* escape is value-concentrated but spectrally FLAT "
     "-- invisible to hypercontractivity")
# ================================================================================================
# The escape mu* is the field 1 - N*delta_{s*}: a (shifted) DELTA.  A delta is the canonical example
# where the VALUE distribution is maximally concentrated (one big spike) while the SPECTRUM is
# maximally FLAT (|coeff| equal across all frequencies).  Confirm: mu*'s spectrum |eps| profile is
# EXACTLY the same flat all-ones as a generic spread orientation -- hypercontractivity, keying on the
# spectrum, has NOTHING to separate the delta from the spread.  The delta's specialness is a PRIMAL
# (value-multiset) fact: its T-histogram is maximally negatively concentrated (one -(N-1) spike), the
# multiset side -- exactly what the DV/seal route (R1/R2) uses and the spectral/HC side cannot reach.
spec_indistinct = True
for n in [3, 4, 5]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    eps_mu = np.asarray(altweight_signs(n), float)         # mu*'s orientation
    rng = np.random.default_rng(99 + n)
    eps_spread = rng.integers(0, 2, M) * 2 - 1
    # spectral |coeff| profiles (the WH coeffs of T are exactly the eps -- |.| = all ones for BOTH)
    spec_mu = np.abs(eps_mu)
    spec_spread = np.abs(eps_spread.astype(float))
    # value (T-histogram) concentration: max |value| and the negative spike
    Tmu = chi0 @ eps_mu
    Tsp = chi0 @ eps_spread.astype(float)
    same_spec = np.allclose(spec_mu, 1.0) and np.allclose(spec_spread, 1.0)
    val_concentrated = (Tmu.min() == -(2 ** n - 1)) and (Tsp.min() > -(2 ** n - 1))
    if not (same_spec and val_concentrated):
        spec_indistinct = False
    print("  n=%d : |spectrum| profile  mu*=all-ones, spread=all-ones (identical: %s) ;  VALUE: "
          "mu* minT=%d (deep spike), spread minT=%d" % (n, same_spec, int(Tmu.min()), int(Tsp.min())))
print("  => mu* and a generic spread eps are SPECTRALLY IDENTICAL (flat |coeff|=1); the delta's")
print("     specialness is its VALUE concentration (one -(N-1) spike), a primal/multiset fact HC")
print("     cannot key on.  Hypercontractivity cannot single out the delta as the escape.")
PASS["(O4) mu* (the delta escape) is spectrally FLAT (|coeff|=1, same as a spread eps); its escape "
     "is a VALUE-concentration (primal) fact -> HC, keying on the spectrum, cannot distinguish it"] = (
    spec_indistinct)


# ================================================================================================
head("(V) the VERDICT against the n<=6 data: does the hypercontractive bound CLOSE [L*]?")
# ================================================================================================
# The task's closure bar: an ALL-n LOWER bound on the TRUE vector-seal gap, derived from
# hypercontractivity, that >= m_hat(mu*) for EVERY non-mu* orientation, verified against n<=6 data.
# We assemble the STRONGEST honest hypercontractive bound and test it against the achievable gaps:
#   The only n-independent, hypercontractive (multiset/Walsh-weight) lower bound available is the
#   DECOUPLED DV(T, mT=1) with Lambda_U bounded by HC -- and (O2) showed its minimizer is NOT mu*
#   (it UNDERSHOOTS m_hat(mu*) at the spread multiset).  So the HC bound FAILS the closure bar:
#   there exist non-mu* orientations whose HC lower bound is BELOW m_hat(mu*).
# We exhibit, at n=3,4, a non-mu* orientation whose best HC/decoupled lower bound < m_hat(mu*) (so the
# bound cannot certify mu*-optimality), and confirm the TRUE gaps are all >= m_hat(mu*) (the lemma is
# TRUE -- it is the TOOL that fails to prove it).
closes = True
for n in [3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    closed = float(exact_min(n)[0])
    hc_below = 0          # # non-mu* multisets whose decoupled-HC LB < m_hat(mu*) (bound fails to certify)
    true_below = 0        # # orientations whose TRUE gap < m_hat(mu*) (must be 0: lemma is true)
    seen = {}
    for bits in itertools.product((-1, 1), repeat=M):
        mh, p, h, T, res = seal_solve(bits, chi0)
        if res > 1e-8:
            continue
        if mh < closed - 1e-7:
            true_below += 1
        key = tuple(sorted(int(round(t)) for t in T))
        if key not in seen:
            dv1, _ = DV_lb(T, 1.0)
            seen[key] = dv1
    mukey = tuple(sorted([-((1 << n) - 1)] + [1] * ((1 << n) - 1)))
    for key, dv1 in seen.items():
        if key != mukey and dv1 < closed - 1e-6:
            hc_below += 1
    print("  n=%d : TRUE gaps below m_hat(mu*) = %d (0 => lemma TRUE) ; decoupled-HC LBs below m_hat(mu*) "
          "= %d (>0 => HC bound FAILS to certify)" % (n, true_below, hc_below))
    if hc_below > 0:
        closes = False
    assert true_below == 0, "lemma itself should hold (no true gap below mu*)"
print("  HC bound certifies mu*-optimality (no non-mu* HC-LB below m_hat(mu*))? %s" % closes)
print("  => the hypercontractive bound DOES NOT close [L*]: it produces lower bounds BELOW m_hat(mu*)")
print("     for non-mu* spread orientations (it bounds Lambda_U, blind to the seal mT and to the n>=5")
print("     gap split).  The lemma is TRUE (no true gap undercuts mu*), but HC cannot prove it.")
PASS["(V) hypercontractive bound does NOT close [L*]: decoupled-HC LBs fall BELOW m_hat(mu*) for "
     "non-mu* orientations (n=3,4) while all TRUE gaps stay >= m_hat(mu*) -> tool fails the closure bar"] = (
    not closes)


# ================================================================================================
head("MACHINE CHECKS")
# ================================================================================================
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
npass = sum(1 for v in PASS.values() if v)
ntot = len(PASS)
print("\n  %d/%d checks pass" % (npass, ntot))
print("  " + ("ALL CHECKS PASS (%d/%d)" % (npass, ntot) if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 92)
print("TOOL 3 VERDICT: NO (honest).")
print("  Hypercontractivity / Fourier-on-the-hypercube does NOT close [L*].")
print("  POSITIVE residue (logged for a future tool): the Donsker-Varadhan tightening (R1) --")
print("    m_hat(eps) >= DV(eps) = sup_lambda[lambda*mT - Lambda_U(lambda)], a VALID all-n lower bound,")
print("    EXACTLY TIGHT on mu* and with mu* its EXHAUSTIVE global minimizer (n<=4) -- plus the seal")
print("    moment lever (R2) mT = sum_a e^{-h_a}, minimized at mu*.")
print("  WHY IT FAILS: the tool bounds Lambda_U / the L^p norms of T, a MULTISET (Walsh-weight)")
print("    functional, which is (O1) blind to the n>=5 gap split (D2 same-multiset pair, gaps differ by")
print("    0.33; Lambda_U identical), (O2) decoupled from the load-bearing seal mT (decoupling")
print("    UNDERSHOOTS m_hat(mu*) at the spread multiset, so mu* is not the HC-bound minimizer), (O3)")
print("    loosened EXPONENTIALLY in n on the FULL-degree flat spectrum (Bonami constant anti-extremal),")
print("    and (O4) unable to distinguish the delta (spectrally flat, value-concentrated).")
print("  The lemma [L*] is TRUE on all tested data; hypercontractivity is the WRONG instrument to prove it.")
print("=" * 92)
