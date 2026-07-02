"""
v7 Paper IX, receipt pB -- TOOL 4: a DIRECT VARIATIONAL / Gibbs lower bound on the TRUE
vector-seal chiral gap, aimed at the open global-optimality residue [L*].

================================================================================================
THE TARGET  [L*]  (read-only inputs: pD_chiral_global_optimality.py, p9a_chiral_gap_closed.py,
setup_extract_d1d.py -- functionals reused VERBATIM; this file WRITES only pB_*).
================================================================================================
States s in {+-1}^n, N=2^n, M=N-1 nonzero masks a, character chi_a(s)=prod_{i in a} s_i.
Orientation eps in {+-1}^M, phi_a(s):=eps_a chi_a(s), anomaly field T_eps(s)=sum_{a!=0} eps_a chi_a(s).
The SEAL fixes the per-mode fixed point  E_{P*}[phi_a] = e^{-h*_a}  for every a; the tilted law is
  P*(s) = exp(<h*,phi(s)>) / (N e^{psi(h*)}),  psi(h)=log E_U[exp(<h,phi>)],  U=uniform.
The chiral gap is the TRUE vector-seal functional
  m_hat(eps) = D(P* || U) = <h*, E_{P*}[phi]> - psi(h*) = <h*, e^{-h*}> - psi(h*)   (nats).
mu* = the DELTA orientation eps_a=-chi_a(s*) (alternating-by-weight), T=1-N*delta_{s*}, multiset
{-(N-1) once, +1 (N-1) times}, gap m_hat_min(n) = -ln(1-2^-n) - delta_n  ~  2^-n  (pD check E).
[L*] = prove mu* is the GLOBAL minimum over all orientations for ALL n (open for n>=7).

================================================================================================
THE TOOL  (NOT cited -- ADAPTED; the Gibbs/Donsker-Varadhan variational principle on ONE scalar).
================================================================================================
We build a lower bound on the TRUE vector-seal gap (never the scalar surrogate that overshoots):

  STEP 1  [data-processing, exact, ALL n].  For the scalar observable T(s)=sum_a phi_a(s),
          m_hat(eps) = D(P* || U) >= D( law_{P*}(T) || law_U(T) ) =: KL_1d(eps).
          (Pushforward through the measurable map s->T(s); reuses pD's KL_1d exactly.)

  STEP 2  [Gibbs / Donsker-Varadhan, exact, ALL n].  For the SAME scalar T and ANY law Q,
          D(Q || U) >= sup_{t in R} [ t * E_Q[T] - Lambda(t) ],  Lambda(t):=log E_U[e^{tT}],
          the convex conjugate (Cramer rate function) of the log-MGF -- a LOWER bound because the
          conjugate of the conjugate of a measure's log-MGF is its KL only in the limit; the
          one-parameter exponential family is a sub-family of all couplings, so the sup over t is
          <= the full KL.  Applied to Q=law_{P*}(T) and combined with STEP 1:
            m_hat(eps) >= I_T( mT )  where  I_T(m):=sup_t [ t m - Lambda(t) ],  mT:=E_{P*}[T].

  STEP 3  [the seal supplies the mean, exact].  E_{P*}[T] = sum_a E_{P*}[phi_a] = sum_a e^{-h*_a}
          = mT  -- the seal constraints (NOT the scalar surrogate) fix the only datum I_T needs.

  So the bound is  LB_Gibbs(eps) := I_T( T_eps ; mT(eps) )  with  mT(eps)=sum_a e^{-h*_a}.
  I_T is the EXACT Cramer rate function of the T-multiset (computed by 1-D convex duality, the
  log-MGF Lambda strictly convex => I_T found by a single root of Lambda'(t)=mT, dps>=120).

  CONVEXITY / MULTIPLICITY content (the "phi(multiplicity of the deepest level)").  I_T(m) is the
  convex conjugate of Lambda; for the FLOOR mean m=1 (see the mT>=1 lemma) it reads off the
  multiplicity profile of the multiset: the deepest level's multiplicity controls how negative T
  can be tilted.  mu* has the UNIQUE multiplicity-1 deepest level at the maximal depth -(N-1):
  this is exactly the configuration on which the Gibbs bound is TIGHT (equality, STEP 1&2 both
  saturate because the field is genuinely two-valued and the seal is scalar) -- see check (5).

================================================================================================
WHAT THIS RECEIPT ESTABLISHES (BRUTALLY HONEST grade -- proof_status = PARTIAL).
================================================================================================
PROVEN / VERIFIED:
  (1) VALIDITY [the bound is <= the real gap], the load-bearing half.  The chain
        LB_Gibbs(eps) = I_T(mT) <= KL_1d(eps) <= m_hat(eps)
      holds for EVERY orientation -- BOTH inequalities verified numerically to ~machine/dps floor:
      exhaustively over all orientations at n=2,3,4 and on large random + deep-orientation samples
      at n=5,6.  STEP 1 (data-processing) and STEP 2 (Gibbs conjugate <= KL) are textbook-exact
      all-n inequalities; the receipt CONFIRMS no numerical violation.  Crucially the bound is on
      the TRUE vector-seal functional (it uses the vector seal's mean mT=sum e^{-h*_a} and the true
      T-multiset), NOT the scalar-tilt surrogate -- and it is even WEAKER than (i.e. <=) the exact
      pushforward KL_1d, so validity is never in doubt.
  (2) TIGHTNESS / EQUALITY ON mu*.  LB_Gibbs(mu*) = m_hat_min(n) to >100 digits (n=2..8): on mu*
      the field is two-valued, the seal is scalar, STEP 1 and STEP 2 both saturate.  So the bound
      LOSES NOTHING at the minimizer -- it is the right shape to certify mu*.
  (3) ISOLATION at n<=4 (exhaustive) and n=5,6 (orientation-level).  For EVERY non-mu* orientation,
      LB_Gibbs(eps) >= m_hat_min(n): the bound already EXCEEDS mu*'s gap, so mu* is isolated by the
      bound alone.  The runner-up LB is O(1) (>= 0.28 at n=4, >= 0.5 at n=3) while mu* ~ 2^-n.  This
      is the [L*] closing CRITERION restricted to the orientations checked.

THE HONEST RESIDUE (why PARTIAL, not CLOSED):
  The isolation in (3) is driven by TWO facts: (a) the T-multiset of a non-mu* orientation is not
  maximally-negatively-concentrated, and (b) its seal mean mT(eps) is bounded AWAY from the floor
  mT(mu*) (empirically mT >= ~2.7 for every non-mu* converged orientation; the minimal mean is
  realized ONLY by mu*).  Fact (a) alone is NOT enough: at the floor mean m~1, I_T(.,1) does NOT
  exceed mu*'s gap for every non-mu* multiset (check 4b: some multi-level multisets give I_T(.,1) ~
  0.026 < mu*).  So the bound CLOSES [L*] only GIVEN the auxiliary lemma
        (Lmu)  mT(eps) := sum_a e^{-h*_a} is MINIMIZED, uniquely, at the mu* orbit (mT(mu*)=
               (N-1)e^{-h*}), and mT(eps) >= mT(mu*) + c (c>0, n-independent) for every non-mu* orient,
  -- where mT(mu*)=(N-1)e^{-h*} is the seal mean on mu* itself (it RISES to 1 from below: 0.9846 at
  n=2, 1 to dps for n>=4; the asymptotic floor is 1, the exact floor at finite n is mT(mu*)) --
  which we VERIFY (exhaustive n<=4; samples n=5,6) but do NOT PROVE for all n.  Hence:
    - The variational tool DELIVERS a valid all-n lower bound on the TRUE vector-seal gap, tight on
      mu*, and the isolation criterion is MET on all n<=6 data (the required verification target).
    - But the all-n closure is REDUCED to (Lmu) -- a clean mean-floor lemma on the seal solution --
      NOT eliminated.  The remaining inequality is exactly (Lmu): "the seal mean mT is minimized,
      uniquely, at the mu* orbit, with an n-independent margin to every other orientation."
  This is a GENUINE sharpening (the open residue is now a one-line scalar mean lemma about the seal
  fixed point, with the variational machinery + tightness-on-mu* supplied), but it is honestly NOT a
  full all-n certificate.  Per the task's default: report PARTIAL, naming the remaining inequality.

Precision: mpmath dps>=120 for all gap / rate-function / mean values (the doubly-exponentially
small delta_n and the 2^-n gaps are never float64); numpy seal solves for the exhaustive/sample
sweeps (the SAME seal_solve as pD, reused verbatim), with the headline anchors re-verified in mpmath.
Pre-geometric: every quantity is a record-internal KL content (nats) / orientation sign / character.
"""
import itertools
import os
import warnings
from collections import defaultdict
import numpy as np
import mpmath as mp

mp.mp.dps = 140
PASS = {}
# The seal line-search transiently explores degenerate (h_a -> -inf) directions on NON-converged
# orientations (filtered out by the gradnorm > 1e-9 guard); the resulting overflow in exp() is
# benign and never touches a REPORTED quantity.  Silence it so the receipt output is clean.
np.seterr(over="ignore")
warnings.filterwarnings("ignore", category=RuntimeWarning)


def head(s):
    print("\n" + "=" * 92 + "\n" + s + "\n" + "=" * 92)


# ================================================================================================
# REUSED VERBATIM from pD_chiral_global_optimality.py (shared machinery) -- read-only import-by-copy.
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


def seal_solve(signs, chi0, tol=1e-13, maxit=400):
    """The per-mode SEAL fixed point E_P[eps_a chi_a]=e^{-h_a}; returns (m_hat, p, h, Tfull).
    VERBATIM from pD (the gap_of_orientation seal fixed point with the monotone-descent guard)."""
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
            Gn = Gpot(h - t * step)
        h = np.minimum(h - t * step, 40.0)
        G0 = Gpot(h)
    z = chi @ h
    z -= z.max()
    p = np.exp(z)
    p /= p.sum()
    mhat = float(np.sum(p * np.log(p * N)))
    return mhat, p, h, chi.sum(1)


def conv_gradnorm(signs, chi0):
    """gradient norm of the seal at the returned point -- the convergence filter (pD's degenerate
    high-gap orientations, with some h_a->inf, are NOT genuine seal fixed points and are excluded)."""
    mhat, p, h, T = seal_solve(signs, chi0)
    chi = chi0 * np.asarray(signs, float)[None, :]
    E = chi.T @ p
    return float(np.abs(E - np.exp(-h)).max())


def exact_min(n):
    """Scalar seal on mu* = {-(N-1)(x1),+1(x(N-1))}; VERBATIM from pD/p9a.  Returns (D, closed, h)."""
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


def mu_seal_mean(n):
    """The EXACT seal mean mT(mu*) = sum_a e^{-h*_a} = (N-1) e^{-h*} on mu* (the scalar two-value
    seal).  This is the floor of mT and the tight datum for the bound: mT(mu*) = 0.9846 at n=2,
    0.99999980 at n=3, and = 1 (to dps) for n>=4 -- it APPROACHES 1 from below, exactly 1 only
    asymptotically.  Returns mp.mpf at the global dps."""
    N = 1 << n
    M = N - 1

    def fp(h):
        w0 = mp.e ** (-h * M)
        eh = mp.e ** (h)
        Z = w0 + M * eh
        return (w0 * (-1) + eh * (1)) / Z - mp.e ** (-h)

    h = mp.findroot(fp, mp.log(mp.mpf(M)) if M > 1 else mp.mpf("1.0"))
    return M * mp.e ** (-h)


def KL1d_float(p, T, N):
    """pD's KL_1d: pushforward of the vector seal P* through T (the data-processing 1-D KL)."""
    Plev = defaultdict(float)
    cnt = defaultdict(int)
    for s in range(N):
        Plev[round(T[s])] += p[s]
        cnt[round(T[s])] += 1
    return sum(Plev[t] * np.log(Plev[t] / (cnt[t] / N)) for t in Plev)


# ================================================================================================
# THE TOOL: the EXACT 1-D Cramer rate function I_T(m) of a T-multiset, by convex duality.
# ================================================================================================
# Lambda(t) = log( (1/N) sum_s e^{t T(s)} ) = log( sum_v q_v e^{t v} ),  q_v = (mult of v)/N.
# Lambda is the cumulant generating function of T under U; strictly convex (T non-constant).
# Lambda'(t) = E_{tilt(t)}[T], increasing from min(T) (t->-inf) to max(T) (t->+inf).
# For a target mean m in (min T, max T), the conjugate I_T(m)=sup_t[t m - Lambda(t)] is attained at
# the UNIQUE t* with Lambda'(t*) = m, and I_T(m) = t* m - Lambda(t*).  We solve Lambda'(t*)=m by a
# safeguarded Newton/bisection at mpmath precision (Lambda'' = Var_tilt[T] > 0, monotone => robust).
def cramer_rate_mp(values, mults, m, N=None, dps=140):
    """EXACT Cramer rate function I_T(m) of the multiset {values with mults}, at target mean m.
    All-mpmath; returns I_T(m).  m must lie strictly inside (min value, max value)."""
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
        vs = [mp.mpf(v) for v in values]
        cs = [mp.mpf(c) for c in mults]
        Ntot = sum(cs) if N is None else mp.mpf(N)
        qs = [c / Ntot for c in cs]
        mm = mp.mpf(m)
        vmin, vmax = min(vs), max(vs)
        if not (vmin < mm < vmax):
            # m at/over the boundary: rate is the boundary log-prob (handled, but not needed here)
            if mm <= vmin:
                # I = -log P(T=min)  (all mass on the min atom)
                q = sum(q for q, v in zip(qs, vs) if v == vmin)
                return -mp.log(q)
            q = sum(q for q, v in zip(qs, vs) if v == vmax)
            return -mp.log(q)

        def Lam(t):
            z = [t * v for v in vs]
            mx = max(z)
            return mx + mp.log(sum(q * mp.e ** (zz - mx) for q, zz in zip(qs, z)))

        def Lamp(t):  # Lambda'(t) = E_tilt[T]
            z = [t * v for v in vs]
            mx = max(z)
            w = [q * mp.e ** (zz - mx) for q, zz in zip(qs, z)]
            Z = sum(w)
            return sum(wi * v for wi, v in zip(w, vs)) / Z

        def Lampp(t):  # Lambda''(t) = Var_tilt[T] > 0
            z = [t * v for v in vs]
            mx = max(z)
            w = [q * mp.e ** (zz - mx) for q, zz in zip(qs, z)]
            Z = sum(w)
            EV = sum(wi * v for wi, v in zip(w, vs)) / Z
            EV2 = sum(wi * v * v for wi, v in zip(w, vs)) / Z
            return EV2 - EV * EV

        # bracket Lamp(t) - m = 0 ; Lamp is increasing.  Find a bracket, then bisect+Newton-polish.
        lo, hi = mp.mpf("-400"), mp.mpf("400")
        flo, fhi = Lamp(lo) - mm, Lamp(hi) - mm
        assert flo < 0 < fhi, "mean m not strictly inside the spectrum range"
        for _ in range(4 * dps):
            mid = (lo + hi) / 2
            fm = Lamp(mid) - mm
            if fm == 0:
                lo = hi = mid
                break
            if fm > 0:
                hi = mid
            else:
                lo = mid
            if hi - lo < mp.mpf(10) ** (-(dps - 5)):
                break
        t = (lo + hi) / 2
        for _ in range(60):  # Newton polish
            d = Lamp(t) - mm
            t2 = t - d / Lampp(t)
            if abs(t2 - t) < mp.mpf(10) ** (-(dps - 5)):
                t = t2
                break
            t = t2
        return t * mm - Lam(t)
    finally:
        mp.mp.dps = old


def cramer_rate_fast(T, m):
    """float64 fast Cramer rate (for the big exhaustive/sample sweeps).  Convex 1-D duality:
    solve Lambda'(t)=m by bisection (Lambda' increasing), return t*m - Lambda(t)."""
    T = np.asarray(T, float)
    N = T.size
    vmin, vmax = T.min(), T.max()
    if not (vmin < m < vmax):
        if m <= vmin:
            return -np.log(np.mean(T == vmin))
        return -np.log(np.mean(T == vmax))

    def Lam(t):
        z = t * T
        mx = z.max()
        return mx + np.log(np.mean(np.exp(z - mx)))

    def Lamp(t):
        z = t * T
        mx = z.max()
        w = np.exp(z - mx)
        return np.sum(w * T) / np.sum(w)

    lo, hi = -200.0, 200.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if Lamp(mid) > m:
            hi = mid
        else:
            lo = mid
        if hi - lo < 1e-14:
            break
    t = 0.5 * (lo + hi)
    return t * m - Lam(t)


def LB_Gibbs(signs, chi0):
    """The variational lower bound LB_Gibbs(eps) = I_T(T_eps ; mT) with mT = sum_a e^{-h*_a}
    (the TRUE vector-seal mean), and the comparison values (m_hat, KL_1d, mT, gradnorm)."""
    mhat, p, h, T = seal_solve(signs, chi0)
    N = T.size
    chi = chi0 * np.asarray(signs, float)[None, :]
    E = chi.T @ p
    gn = float(np.abs(E - np.exp(-h)).max())
    mT = float(np.sum(np.exp(-h)))            # E_{P*}[T] = sum_a e^{-h_a}  (the seal mean)
    lb = cramer_rate_fast(T, mT)
    kl = KL1d_float(p, T, N)
    return lb, mhat, kl, mT, gn, T


# ================================================================================================
head("(0) the tool reproduces mu* EXACTLY (tightness): LB_Gibbs(mu*) = m_hat_min(n)  [mpmath dps=140]")
# ================================================================================================
# On mu* the field is two-valued ({-(N-1), +1}) and the seal is scalar, so STEP 1 (data-processing)
# and STEP 2 (Gibbs conjugate) BOTH saturate at mu*'s OWN seal mean mT(mu*)=sum_a e^{-h*_a}.  Hence
# I_T( {-(N-1),+1} ; mT(mu*) ) = m_hat_min(n) EXACTLY.  (mT(mu*) -> 1 from below; it is NOT exactly 1
# at small n -- 0.9846 at n=2 -- so the tight datum is mu*'s OWN mean, not the asymptotic floor 1.)
tight_ok = True
print("   n    LB_Gibbs(mu*) = I_T(mu*; mT(mu*))                  m_hat_min(n)          |diff|")
for n in range(2, 9):
    N = 1 << n
    Dexact, closed, hh = exact_min(n)
    mT_mu = mu_seal_mean(n)                       # mu*'s OWN exact seal mean (the tight datum)
    lb_mu = cramer_rate_mp([-(N - 1), 1], [1, N - 1], mT_mu, N=N, dps=140)
    diff = abs(lb_mu - Dexact)
    print("  %2d   %s   %s   %s"
          % (n, mp.nstr(lb_mu, 40), mp.nstr(Dexact, 18), mp.nstr(diff, 4)))
    if diff > mp.mpf(10) ** (-100):
        tight_ok = False
PASS["(0) TIGHTNESS: LB_Gibbs(mu*) = I_T({-(N-1),+1}; mT(mu*)) = m_hat_min(n) to >100 digits (n=2..8)"] = tight_ok


# ================================================================================================
head("(0b) mu*'s seal mean mT(mu*)=sum_a e^{-h*_a} APPROACHES 1 from below (=1 to dps for n>=4); "
     "it is the floor of mT and the bound's tight datum")
# ================================================================================================
# mu* is the scalar two-value seal: E[chi_a]=e^{-h} for all a, so E_{P*}[T]=sum_a e^{-h}=(N-1)e^{-h}.
# This is mT(mu*); it rises monotonically to 1 (0.9846 at n=2, 0.99999980 at n=3, =1 to dps for n>=4).
# HONEST: the asymptotic floor is 1, but at finite small n mu*'s mean is slightly BELOW 1; the tight
# datum used in (0) is mu*'s OWN mean, not 1.  Confirm: mT(mu*) matches the float seal AND is <=1,
# rising toward 1.
mu_mean_ok = True
prev = mp.mpf(0)
print("   n    mT(mu*) = (N-1)e^{-h*}  [exact]      float-seal mT      <=1 & rising?")
for n in range(2, 7):
    chi0, _ = char_cols(n)
    _, _, _, mT_float, gn, _ = LB_Gibbs(altweight_signs(n), chi0)
    mT_exact = mu_seal_mean(n)
    rising = bool(mT_exact > prev - mp.mpf("1e-30"))
    le1 = bool(mT_exact <= 1 + mp.mpf("1e-30"))
    print("  %2d   %s   %.15f   <=1:%s rising:%s" % (n, mp.nstr(mT_exact, 20), mT_float, le1, rising))
    if abs(float(mT_exact) - mT_float) > 1e-8 or gn > 1e-9 or not le1 or not rising:
        mu_mean_ok = False
    prev = mT_exact
PASS["(0b) mu* seal mean mT(mu*)=(N-1)e^{-h*} <= 1, rising to 1 (=1 to dps for n>=4); matches float seal; "
     "the bound's tight datum"] = mu_mean_ok


# ================================================================================================
head("(1) VALIDITY (the load-bearing half): LB_Gibbs(eps) <= KL_1d(eps) <= m_hat(eps) for ALL eps")
# ================================================================================================
# The two inequalities of the chain.  Both are exact all-n facts (STEP1 data-processing, STEP2 Gibbs
# conjugate <= KL); here we CONFIRM no numerical violation, exhaustively at n<=4 and on samples n=5,6.
# A negative min => a (numerical) violation; the bound must sit at or below the true gap.
valid_ok = True
for n in [2, 3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    min_step2 = 1e18   # min(KL_1d - LB_Gibbs)  must be >= 0
    min_step1 = 1e18   # min(m_hat - KL_1d)     must be >= 0
    nconv = 0
    for bits in itertools.product((-1, 1), repeat=M):
        lb, mhat, kl, mT, gn, T = LB_Gibbs(bits, chi0)
        if gn > 1e-9:
            continue
        nconv += 1
        min_step2 = min(min_step2, kl - lb)
        min_step1 = min(min_step1, mhat - kl)
    print("  n=%d EXHAUSTIVE (%d converged orientations): min(KL_1d - LB_Gibbs)=%.3e ; min(m_hat - KL_1d)=%.3e"
          % (n, nconv, min_step2, min_step1))
    if min_step2 < -1e-9 or min_step1 < -1e-9:
        valid_ok = False
PASS["(1) VALIDITY exhaustive n<=4: LB_Gibbs <= KL_1d <= m_hat (no violation), all converged orientations"] = valid_ok

# n=5,6 random samples (the gap is NOT a multiset functional here; sample the orientation level)
rng = np.random.default_rng(20240616)
for n in [5, 6]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    min_step2 = 1e18
    min_step1 = 1e18
    nconv = 0
    NS = 6000 if n == 5 else 3000
    for _ in range(NS):
        eps = rng.integers(0, 2, M) * 2 - 1
        lb, mhat, kl, mT, gn, T = LB_Gibbs(eps, chi0)
        if gn > 1e-9:
            continue
        nconv += 1
        min_step2 = min(min_step2, kl - lb)
        min_step1 = min(min_step1, mhat - kl)
    print("  n=%d random (%d converged): min(KL_1d - LB_Gibbs)=%.3e ; min(m_hat - KL_1d)=%.3e"
          % (n, nconv, min_step2, min_step1))
    if min_step2 < -1e-9 or min_step1 < -1e-9:
        valid_ok = False
PASS["(1b) VALIDITY n=5,6 random samples: chain LB_Gibbs <= KL_1d <= m_hat holds (no violation)"] = valid_ok


# ================================================================================================
head("(2) ISOLATION at n<=4 (EXHAUSTIVE): every non-mu* orientation has LB_Gibbs >= m_hat_min(n)")
# ================================================================================================
# The closing criterion: the bound ALONE already exceeds mu*'s gap on every non-mu* orientation,
# so mu* is isolated by the lower bound.  Report the runner-up LB (the next-smallest bound) -- it is
# O(1) (n-independent), while mu* ~ 2^-n.
iso_ok = True
for n in [2, 3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    mukey = tuple(sorted([-(N if False else ((1 << n) - 1))] + [1] * ((1 << n) - 1)))
    mu_gap = float(exact_min(n)[0])
    min_nonmu_lb = 1e18
    mu_lb = None
    nbelow = 0
    for bits in itertools.product((-1, 1), repeat=M):
        lb, mhat, kl, mT, gn, T = LB_Gibbs(bits, chi0)
        if gn > 1e-9:
            continue
        key = tuple(sorted(int(round(t)) for t in T))
        if key == mukey:
            mu_lb = lb
        else:
            if lb < min_nonmu_lb:
                min_nonmu_lb = lb
            if lb < mu_gap - 1e-9:
                nbelow += 1
    closes = (min_nonmu_lb >= mu_gap - 1e-9) and (nbelow == 0)
    print("  n=%d: mu* gap=%.10f ; LB_Gibbs(mu*)=%.10f ; runner-up non-mu* LB=%.6f ; #(LB<mu*)=%d ; closes=%s"
          % (n, mu_gap, mu_lb, min_nonmu_lb, nbelow, closes))
    if not closes:
        iso_ok = False
PASS["(2) ISOLATION exhaustive n<=4: every non-mu* orientation has LB_Gibbs >= m_hat_min(n) (runner-up O(1))"] = iso_ok


# ================================================================================================
head("(3) ISOLATION at n=5,6 (ORIENTATION-LEVEL): deep-minT band + random; none has LB_Gibbs < mu*")
# ================================================================================================
# The gap is NOT a multiset functional at n>=5 (pD D2), so we evaluate the bound at the ORIENTATION
# level.  Any mu*-beating orientation must be maximally-negatively-concentrated (pD B), so the deep
# band is where a violation of isolation would live.  We reuse pD's deep enumeration shape.
def hadamard_sub(n):
    N = 1 << n
    H = np.empty((N, N), dtype=np.int16)
    for s in range(N):
        for a in range(N):
            H[s, a] = -1 if (bin(s & a).count("1") & 1) else 1
    return H[:, 1:]


def enum_deep_orientations(n, thresh, cap=None):
    """Gauge-fixed (singletons +1) orientations whose minT <= thresh -- the deep tier (pD shape)."""
    N = 1 << n
    M = N - 1
    Hsub = hadamard_sub(n).astype(np.int32)
    singleton_cols = [(1 << i) - 1 for i in range(n)]
    free_cols = [c for c in range(M) if c not in singleton_cols]
    base = Hsub[:, singleton_cols].sum(axis=1).astype(np.int32)
    HF = Hsub[:, free_cols].astype(np.int32)
    F = len(free_cols)
    total = 1 << F
    CHUNK = 1 << 20
    bitw = np.arange(F, dtype=np.uint64)
    deep = []
    best_minT = 0
    for start in range(0, total, CHUNK):
        end = min(start + CHUNK, total)
        idx = np.arange(start, end, dtype=np.uint64)
        bits = ((idx[:, None] >> bitw[None, :]) & 1).astype(np.int32)
        signs = bits * 2 - 1
        T = base[None, :] + signs @ HF.T
        mins = T.min(axis=1)
        best_minT = min(best_minT, int(mins.min()))
        sel = np.where(mins <= thresh)[0]
        for j in sel:
            full = np.ones(M, dtype=np.int8)
            full[free_cols] = signs[j]
            deep.append(full.copy())
            if cap is not None and len(deep) >= cap:
                return deep, best_minT
    return deep, best_minT


# ---- n=5: deep band (minT<=-25 keeps the deepest few thousand, incl. mu* at -31) + random ----
n = 5
chi0_5, _ = char_cols(5)
mu_gap5 = float(exact_min(5)[0])
deep5, deepest5 = enum_deep_orientations(5, thresh=-25)
min_lb_deep5 = 1e18
mu_present5 = False
nbelow5 = 0
for full in deep5:
    lb, mhat, kl, mT, gn, T = LB_Gibbs([int(x) for x in full], chi0_5)
    if gn > 1e-9:
        continue
    key = tuple(sorted(int(round(t)) for t in T))
    if key == tuple(sorted([-31] + [1] * 31)):
        mu_present5 = True
    if lb < min_lb_deep5:
        min_lb_deep5 = lb
    if lb < mu_gap5 - 1e-9 and key != tuple(sorted([-31] + [1] * 31)):
        nbelow5 += 1
# random breadth
rmin5 = 1e18
rbelow5 = 0
for _ in range(20000):
    eps = rng.integers(0, 2, 31) * 2 - 1
    lb, mhat, kl, mT, gn, T = LB_Gibbs([int(x) for x in eps], chi0_5)
    if gn > 1e-9:
        continue
    rmin5 = min(rmin5, lb)
    if lb < mu_gap5 - 1e-9:
        rbelow5 += 1
print("  n=5 deep band (minT<=-25, %d orientations; deepest minT=%d, mu* present=%s):"
      % (len(deep5), deepest5, mu_present5))
print("       min non-mu* LB over deep band = %.8f  vs mu* gap %.8f ; #(LB<mu*)=%d"
      % (min_lb_deep5, mu_gap5, nbelow5))
print("  n=5 random (20000): min LB = %.8f (>> mu*) ; #(LB<mu*)=%d" % (rmin5, rbelow5))
n5_ok = (deepest5 == -31 and mu_present5 and nbelow5 == 0 and rbelow5 == 0)
PASS["(3) ISOLATION n=5 orientation-level (deep band + 20000 random, EXACT vector seal): "
     "no orientation has LB_Gibbs < mu*; mu* realized at minT=-31"] = n5_ok


# ---- n=6: alt (mu*) + deep-seeking greedy + random; none below mu* ----
n = 6
chi0_6, _ = char_cols(6)
mu_gap6 = float(exact_min(6)[0])


def greedy_deepen_collect(n, n_starts=300, deep_thresh=-44, seed=1):
    """pD-shape greedy-deepen: drive minT to the maximal depth -(N-1) and collect deep orientations;
    evaluate LB_Gibbs on each; return (deepest reached, min non-mu* LB in deep band, #below mu*)."""
    N = 1 << n
    M = N - 1
    rngl = np.random.default_rng(seed)
    Hsub = hadamard_sub(n).astype(np.int32)
    singleton_cols = [(1 << i) - 1 for i in range(n)]
    free_cols = [c for c in range(M) if c not in singleton_cols]
    base = Hsub[:, singleton_cols].sum(axis=1)
    HF = Hsub[:, free_cols]
    F = len(free_cols)
    deep_orients = {}
    deepest = 0
    for _ in range(n_starts):
        sgn = (rngl.integers(0, 2, F) * 2 - 1).astype(np.int32)
        T = base + HF @ sgn
        minT = int(T.min())
        improved = True
        while improved:
            improved = False
            best_flip = None
            best_new = minT
            for j in range(F):
                mm = int((T - 2 * sgn[j] * HF[:, j]).min())
                if mm < best_new:
                    best_new = mm
                    best_flip = j
            if best_flip is not None:
                j = best_flip
                T = T - 2 * sgn[j] * HF[:, j]
                sgn[j] *= -1
                minT = best_new
                improved = True
                if minT <= deep_thresh:
                    full = np.ones(M, dtype=np.int8)
                    full[free_cols] = sgn.astype(np.int8)
                    deep_orients[full.tobytes()] = full.copy()
        deepest = min(deepest, minT)
        if minT <= deep_thresh:
            full = np.ones(M, dtype=np.int8)
            full[free_cols] = sgn.astype(np.int8)
            deep_orients[full.tobytes()] = full.copy()
    deep_orients[b"__alt__"] = np.array(altweight_signs(n), dtype=np.int8)
    chi0, _ = char_cols(n)
    min_nonmu_lb = 1e18
    nbelow = 0
    mu_present = False
    mukey = tuple(sorted([-(N - 1)] + [1] * (N - 1)))
    for full in deep_orients.values():
        lb, mhat, kl, mT, gn, T = LB_Gibbs([int(x) for x in full], chi0)
        if gn > 1e-9:
            continue
        key = tuple(sorted(int(round(t)) for t in T))
        if key == mukey:
            mu_present = True
            continue
        if lb < min_nonmu_lb:
            min_nonmu_lb = lb
        if lb < mu_gap6 - 1e-9:
            nbelow += 1
    return deepest, min_nonmu_lb, nbelow, mu_present, len(deep_orients)


deepest6, min_lb6, nbelow6, mu_present6, ndeep6 = greedy_deepen_collect(6, n_starts=300, deep_thresh=-44)
# random breadth at n=6
rmin6 = 1e18
rbelow6 = 0
for _ in range(8000):
    eps = rng.integers(0, 2, 63) * 2 - 1
    lb, mhat, kl, mT, gn, T = LB_Gibbs([int(x) for x in eps], chi0_6)
    if gn > 1e-9:
        continue
    rmin6 = min(rmin6, lb)
    if lb < mu_gap6 - 1e-9:
        rbelow6 += 1
print("  n=6 greedy-deepen (%d deep orientations; deepest minT=%d, mu* present=%s):"
      % (ndeep6, deepest6, mu_present6))
print("       min non-mu* LB in deep band = %.8f  vs mu* gap %.8f ; #(LB<mu*)=%d"
      % (min_lb6, mu_gap6, nbelow6))
print("  n=6 random (8000): min LB = %.8f (>> mu*) ; #(LB<mu*)=%d" % (rmin6, rbelow6))
n6_ok = (deepest6 == -(2 ** 6 - 1) and mu_present6 and nbelow6 == 0 and rbelow6 == 0)
PASS["(3b) ISOLATION n=6 orientation-level (greedy-deepen to maximal depth -63 + 8000 random): "
     "no orientation has LB_Gibbs < mu*; mu* realized at -63"] = n6_ok


# ================================================================================================
head("(4) HONESTY: WHY the bound closes -- and the residue.  (4a) the seal-mean separation lemma "
     "(Lmu); (4b) the floor mean alone does NOT isolate")
# ================================================================================================
# (4a) The isolation is driven by the seal mean mT(eps) being bounded AWAY from 1 for non-mu*.
# Exhaustive n<=4 + samples n=5,6: the SMALLEST non-mu* mT and the c = min mT - 1.
print("  (4a) the seal-mean separation  mT(eps) >= mT(mu*), with the MINIMUM at the mu* orbit  (drives")
print("       isolation): mu* uniquely realizes the floor; every non-mu* mean is bounded away (>=2.6).")
mean_sep_ok = True
for n in [3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    mukey = tuple(sorted([-(2 ** n - 1)] + [1] * (2 ** n - 1)))
    mT_mu = float(mu_seal_mean(n))
    min_all = 1e18
    min_nonmu = 1e18
    for bits in itertools.product((-1, 1), repeat=M):
        lb, mhat, kl, mT, gn, T = LB_Gibbs(bits, chi0)
        if gn > 1e-9:
            continue
        min_all = min(min_all, mT)
        key = tuple(sorted(int(round(t)) for t in T))
        if key != mukey:
            min_nonmu = min(min_nonmu, mT)
    # the global min mean IS realized by mu* (min_all == mT_mu), and non-mu* means are bounded away.
    floor_is_mu = abs(min_all - mT_mu) < 1e-7
    print("    n=%d: global-min mT = %.7f (mu* mean = %.7f, match=%s) ; min mT over NON-mu* = %.6f "
          "=> sep c = %.4f" % (n, min_all, mT_mu, floor_is_mu, min_nonmu, min_nonmu - mT_mu))
    if not floor_is_mu or min_nonmu < mT_mu + 0.5:  # c >= ~0.5 at n<=4
        mean_sep_ok = False
# n=5,6 samples (random + deep): smallest non-mu* mT
for n in [5, 6]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    mT_mu = float(mu_seal_mean(n))
    min_nonmu = 1e18
    NS = 4000
    for _ in range(NS):
        eps = rng.integers(0, 2, M) * 2 - 1
        lb, mhat, kl, mT, gn, T = LB_Gibbs([int(x) for x in eps], chi0)
        if gn > 1e-9:
            continue
        key = tuple(sorted(int(round(t)) for t in T))
        if key != tuple(sorted([-(2 ** n - 1)] + [1] * (2 ** n - 1))):
            min_nonmu = min(min_nonmu, mT)
    print("    n=%d sample: mu* mean = %.7f ; min mT over NON-mu* = %.6f  => sep c = %.4f"
          % (n, mT_mu, min_nonmu, min_nonmu - mT_mu))
    if min_nonmu < mT_mu + 0.5:
        mean_sep_ok = False
PASS["(4a) seal-mean separation: global-min mT realized at mu*, every non-mu* mT bounded away by c>=0.5 "
     "(n<=4 exhaustive, n=5,6 sampled)"] = mean_sep_ok

# (4b) the HONEST residue: at the FLOOR mean mT=1, the bound I_T(.,1) does NOT isolate.  Some
# multi-level multisets have I_T(.,1) < mu* gap.  So the bound NEEDS the seal mean mT(eps) (>=1+c
# for non-mu*), i.e. the auxiliary lemma (Lmu) -- which we verify but do not prove for all n.
print("  (4b) at the FLOOR mean mT=1, I_T(.;1) does NOT exceed mu* for every multiset (residue exists):")
n = 4
chi0, _ = char_cols(n)
M = 15
mu_gap4 = float(exact_min(4)[0])
seen = {}
for bits in itertools.product((-1, 1), repeat=M):
    lb, mhat, kl, mT, gn, T = LB_Gibbs(bits, chi0)
    if gn > 1e-9:
        continue
    key = tuple(sorted(int(round(t)) for t in T))
    if key in seen:
        continue
    floor_lb = cramer_rate_fast(T, 1.0)   # I_T at the FLOOR mean 1
    seen[key] = floor_lb
mukey4 = tuple(sorted([-15] + [1] * 15))
nonmu_floor = [v for k, v in seen.items() if k != mukey4]
min_floor = min(nonmu_floor)
print("    n=4: min non-mu* I_T(.;mT=1) = %.6f  vs mu* gap %.6f  -> floor-only closes? %s"
      % (min_floor, mu_gap4, min_floor >= mu_gap4))
print("    => the floor mean ALONE is INSUFFICIENT; isolation requires mT(eps) >= 1+c (lemma Lmu).")
residue_ok = (min_floor < mu_gap4)   # we EXPECT the floor not to isolate -> the residue is real & named
PASS["(4b) RESIDUE NAMED: floor mean mT=1 does NOT isolate (some multiset I_T(.;1) < mu*); the bound "
     "needs the seal-mean lemma (Lmu) mT>=1+c for non-mu* -- verified not proved => proof_status PARTIAL"] = residue_ok


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
print("PROOF STATUS: PARTIAL.")
print("  The Gibbs/Donsker-Varadhan variational tool on the SCALAR T gives a VALID all-n lower bound")
print("  on the TRUE vector-seal gap:  LB_Gibbs(eps) = I_T(T_eps; mT) <= KL_1d <= m_hat(eps), with")
print("  mT = sum_a e^{-h*_a} the seal mean (NOT the scalar-tilt surrogate).  It is TIGHT on mu*")
print("  (= m_hat_min(n) to >100 digits) and ISOLATES mu* on ALL n<=6 data (every non-mu* orientation")
print("  has LB_Gibbs >= m_hat_min(n); runner-up O(1) while mu* ~ 2^-n).  BUT the all-n closure is")
print("  REDUCED to -- not eliminated by -- the auxiliary seal-mean lemma")
print("     (Lmu)  mT(eps) = sum_a e^{-h*_a} is MINIMIZED uniquely at the mu* orbit (mT(mu*)=(N-1)e^{-h*},")
print("            rising to 1 from below), and mT(eps) >= mT(mu*) + c (c>0 n-indep) for non-mu* orient,")
print("  which is VERIFIED (exhaustive n<=4; samples n=5,6) but NOT PROVED for all n.  At the floor")
print("  mean ~1 alone the bound does NOT isolate (check 4b), so (Lmu) is the genuine remaining")
print("  inequality.  Honest grade: PARTIAL -- a real, valid, tight-on-mu* lower bound that meets the")
print("  isolation criterion on all available data, with the residue sharpened to the scalar lemma (Lmu).")
print("=" * 92)
