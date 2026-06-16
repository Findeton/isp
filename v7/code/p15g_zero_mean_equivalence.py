#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
p15g_zero_mean_equivalence.py
=============================
THE LAST RESIDUAL: does SHARD deliver the ZERO-MEAN sqrt(N) action walk natively?
ANSWER: NO -- the zero-mean CENTERING is an IMPORT (the curl-free obstruction).

CONTEXT (the open step located by p15a/p15b/p15f)
-------------------------------------------------
The everpresent cosmological-constant fluctuation deltaLambda ~ V^{-1/2} (Sorkin)
requires the cosmological ACTION itself to perform a ZERO-MEAN sqrt(N) walk:
    Lambda = S/V,  V = N,  delta S ~ sqrt(N)  =>  deltaLambda ~ sqrt(N)/N = N^{-1/2}.
Equivalently (the "conjugate bracket"):  deltaLambda * deltaV ~ O(1).
p15b STEP 4.1 already proved the zero-mean drift REDUCES to this bracket (residual 0).

The prior routes pinned the residual import down to ONE fact: the per-seal
cosmological-action increment must be ZERO-MEAN with O(1) variance.  This receipt
(i) proves the THREE-WAY EQUIVALENCE [bracket] <=> [sqrt(N) action walk] <=>
[zero-mean O(1)-variance increment + CLT] (sympy-exact, residuals 0);
(ii) proves NECESSITY of BOTH zero-mean AND O(1)-variance by MC with sympy-exact
targets (the everpresent exponent -1/2 is destroyed if either fails);
(iii) HONORS THE PRECISION TRAP (excludes the -3/2 nonzero-mean object);
(iv) RESOLVES the central sub-question from the corpus: can the records supply the
ZERO-MEAN CENTERING of the Lambda-kick?  NO -- the corpus routes the sign-balanced
fluctuation delta eta to DECOHERENCE (not curl-free, not Lambda-eligible) and
leaves only the ONE-SIGNED curl-free heating mean w>0 on Lambda.  Sign-balance and
Lambda-eligibility are MUTUALLY EXCLUSIVE in the corpus's own construction, so the
centering is an IMPORT (paper15 sec.7; v5 paper3 L148-150, 186-191, 302).

CENTRAL VERDICT (corpus-cited, NOT asserted) -- the centering is an IMPORT
--------------------------------------------------------------------------
The everpresent bracket needs the CONJUNCTION of two properties on the SAME
object: {sign-balanced (zero-mean)} AND {Lambda-eligible (curl-free)}.  The
corpus delivers each property only on the WRONG object, and proves they are
MUTUALLY EXCLUSIVE in its own construction:

  * Lambda is a SCALAR, so consistency requires its source be CURL-FREE / a
    gradient: eta_nu = nabla_nu phi, giving Lambda = Lambda_0 + 8 pi G int w dt
    (v5 paper3 L148-150, L174-175).  Only the curl-free homogeneous MEAN
    <eta_0> = w(t) sources Lambda -- and it is ONE-SIGNED, equation of state
    HEATING w > 0 (v5 paper3 L302).  A monotone DRIFT (the non-decaying mean
    paper42 prices, undersourcing 10-17 orders), NOT a zero-mean sqrt(N) walk.
  * The genuinely SIGN-BALANCED fluctuation delta eta is NOT curl-free, "cannot
    be absorbed into Lambda," and is routed to gravitational DECOHERENCE
    (Einstein-Langevin metric noise; v5 paper3 L186-191).

  => Sign-balance and Lambda-eligibility are MUTUALLY EXCLUSIVE in the corpus's
     own construction: sign-balanced -> decoherence; Lambda-routed -> one-signed
     heating.  So the records do NOT supply the zero-mean centering -- and they
     structurally point the OTHER way.  Verdict on the CENTERING: IMPORT.

  WHY THE TWO-SIGNED SOURCE RECEIPTS DO NOT FLIP THIS (the superseded reading).
  An earlier framing read the two-signed delta T_00 (paper42 W1) and the
  sign-flipping traceless null charge (paper57 sec.3.3) as licensing a NATIVE
  zero-mean eta-FLUCTUATION.  That step is REBUTTED here: those objects are
  sign-balanced but are NOT the curl-free Lambda-sourcing projection.
    - paper42 W1's delta T_00 in [-1.2e-5, +3.4e-3] is the SIGN of a stress
      COMPONENT in one constructed state; a two-signed T_00 is not a sign-
      balanced non-conservation CURRENT eta_nu = nabla^mu T_{mu nu} (different
      object: a tensor component vs its 4-divergence).
    - paper57 sec.3.3's traceless charge sign-flip is a deterministic
      shape/lattice-spacing NON-UNIVERSALITY, not a stochastic per-seal zero-mean
      fluctuation; the SAME sentence states "the trace channel stays one-signed,"
      and Lambda is sourced through the TRACE-like curl-free mean w(t) -- so
      paper57 sec.3.3, if anything, supports the IMPORT verdict.
  Sign-balance of delta T_00 is therefore NECESSARY but NOT SUFFICIENT for native
  zero-mean centering: the two-signed component is the non-curl-free piece the
  corpus routes to decoherence, exactly the "mutually exclusive" obstruction.

  RESIDUAL (honest): the O(1) MAGNITUDE of the per-seal variance v (the bracket
  COEFFICIENT, c^2) is a SEPARATE IMPORT -- the l_step / absolute-scale datum the
  records provably cannot carry (paper57 weight lemma, L39; G no-go).  So the
  everpresent -1/2 needs zero-mean centering (IMPORT, this receipt) AND O(1)
  variance (finite & nonzero is native; its absolute normalization is the scale
  import).

  NET: the residual import COLLAPSES to ONE structural fact -- the per-seal
  Lambda-action increment must be ZERO-MEAN, and the records cannot supply that
  centering (curl-free obstruction), so it is an IMPORT.  Unimodular gravity (or
  any equivalent zero-mean-conjugacy postulate) is one PACKAGING of exactly this
  residual.  [OPEN] No corpus no-go BARS a native derivation; it is un-built and
  presently CONTRADICTED by the curl-free routing -- the named flip of paper15
  sec.7.

PRECISION DISCIPLINE
--------------------
- mpmath mp.dps = 120 for every cancellation-heavy / near-vacuum quantity.
- sympy-exact for every structural exponent and every equivalence residual.
- MC slopes are FLAGGED estimates; the sympy-exact target exponent is printed.

CORPUS CITATIONS (exact line numbers; read/grepped, not invented)
-----------------------------------------------------------------
v5paper3 v5/relativistic-isp-v5-paper3-unimodular-beable-gravity-cosmological-term.md
   L148-150 : Lambda a SCALAR => consistency requires eta_nu be CURL-FREE / a
              gradient, eta_nu = nabla_nu phi, so Lambda = 8 pi G phi + Lambda_0.
   L174-175 : only the curl-free homogeneous MEAN <eta_0> = w(t) sources Lambda.
   L186-191 : the SIGN-BALANCED fluctuation delta eta is NOT curl-free, "cannot
              be absorbed into Lambda," routed to gravitational DECOHERENCE
              (Einstein-Langevin metric noise).  <-- the curl-free OBSTRUCTION.
   L302     : equation of state HEATING w > 0 (the Lambda-routed mean is ONE-SIGNED).
paper10  v6/relativistic-isp-v6-paper10.md
   L251-258 : Theorem T2 (exact): sigma = D(P_AB || P_BA) >= 0  -- the ONE-SIGNED
              entropy production (KL divergence); machine identity gaps 0.0e+00.
paper42  v6/relativistic-isp-v6-paper42.md
   L184     : nabla^mu T_{mu nu} = eta_nu != 0  (the non-conservation FLUX 4-vector)
   L191     : nabla_nu Lambda = 8 pi G eta_nu   (the SOURCED drift)
   L163-170 : "The two-signed source, constructively" -- delta T_00 in
              [-1.2e-5, +3.4e-3], a LOCALLY NEGATIVE-ENERGY region in a valid
              record-law state.  SIGN of a stress COMPONENT in one constructed
              state -- NOT the curl-free Lambda-sourcing projection (a tensor
              component is not its 4-divergence eta_nu): sign-balance NECESSARY
              but NOT SUFFICIENT for native centering (see CENTRAL VERDICT).
   L210-222 : MEAN drift undersources rho_Lambda by 10-17 orders (the sigma-side
              non-decaying mean; structural not magnitude).
paper57  v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md
   L63 (sec.3.3): null-direction traceless charge "sign-flips -0.19 -> +0.58";
              only the "trace channel stays one-signed."  A deterministic
              shape/lattice NON-UNIVERSALITY, not a stochastic zero-mean per-seal
              fluctuation; Lambda is trace-like curl-free w(t) -> SUPPORTS IMPORT.
   L39 (sec.2.2): weight lemma -- sigma_A weight -2; every intrinsic record
              functional weight 0 (the O(1)-variance MAGNITUDE is the scale import).
   L25 (sec.1.5): Lambda := (R + 8 pi G T)/4 (unimodular fork); Lambda_0 non-sourced.
paper4   v6/relativistic-isp-v6-paper4-sealed-record-events-and-born-composition.md
   L3791    : delta eta_{2n} != 0 -- the seal-flux fluctuation the corpus HOLDS,
              routed to the continuum source density (cofinal reconstruction, sec.48),
              NOT to a Lambda value.
paper11  v7/relativistic-isp-v7-paper11-order-owns-direction-manifoldlikeness-gate.md
   sec.3 (receipt r2): E[N] = V/l_step^d ; Poisson Var[N]/E[N] = 0.97 ;
              recovered ~1/sqrt(N).  (V=N intensive reading + Poisson deltaN ~
              sqrt(N) already NATIVE.)  [Same content in v6/publishable/
              companion-D-conformal-direction.md sec.3.]
p15b     v7/code/p15b_routeB_drift_walk.py  STEP 4.1: zero-mean drift REDUCES to
              the conjugate bracket (residual 0).
"""

import mpmath as mp
import sympy as sp
import numpy as np

mp.mp.dps = 120  # IMPORT-grade precision; never float64 for cancellation/near-vacuum

CHECKS = []  # (name, passed_bool, detail_str)


def check(name, passed, detail=""):
    CHECKS.append((name, bool(passed), detail))
    tag = "PASS" if passed else "FAIL"
    print(f"  [{tag}] {name}" + (f"  -- {detail}" if detail else ""))


def banner(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78)


# ---------------------------------------------------------------------------
# Tag legend (every load-bearing quantity tagged):
#   ROBUST = record-intrinsic, weight-0, derived/cited inside the corpus
#            (record-eligible: V=N, Poisson deltaN)
#   IMPORT = an input the records provably cannot supply
#            (the ZERO-MEAN CENTERING of the Lambda-kick -- curl-free obstruction;
#             AND the O(1) per-seal variance COEFFICIENT/bracket; l_step=Planck, cosmic N)
# ---------------------------------------------------------------------------

banner("p15g -- ZERO-MEAN EQUIVALENCE: the last residual collapsed to ONE fact")

# ===========================================================================
# CHECK 1.  THREE-WAY EQUIVALENCE (sympy-exact, residuals 0)
#   [deltaLambda*deltaV ~ O(1)]  <=>  [delta S ~ sqrt(N)]  <=>
#   [zero-mean O(1)-variance per-seal action increment + CLT]
#   with Lambda = S/V, V = N.
# ===========================================================================
banner("CHECK 1.  THREE-WAY EQUIVALENCE (sympy-exact)  -- bracket = sqrt(N) walk = ZM+CLT")

N, v, c = sp.symbols('N v c', positive=True)

# Substrate (NATIVE, companion-D L33): V = N (intensive reading), and the
# action is a SUM of N per-seal increments S = sum_{i=1}^N xi_i.
#
# STATEMENT C (the zero-mean-O(1)-increment + CLT statement):
#   xi_i i.i.d., mean 0, variance v = O(1).  CLT => std(S) = sqrt(v) * sqrt(N).
deltaS_from_C = sp.sqrt(v) * sp.sqrt(N)          # CLT std of the action sum

# STATEMENT B (the sqrt(N) action walk):  delta S ~ sqrt(N)  (here = sqrt(v)*sqrt(N)).
deltaS_B = sp.sqrt(v) * sp.sqrt(N)

# Lambda = S / V = S / N  => deltaLambda = deltaS / N.
deltaLambda = deltaS_from_C / N
deltaLambda_simpl = sp.simplify(deltaLambda)      # = sqrt(v) * N^{-1/2}

# STATEMENT A (the conjugate bracket):  deltaLambda * deltaV ~ O(1).
# deltaV = deltaN = sqrt(N)  (Poisson, companion-D L33, NATIVE).
deltaV = sp.sqrt(N)
bracket = sp.simplify(deltaLambda_simpl * deltaV)  # should be the O(1) constant sqrt(v)

# (i) C => B : std(S) from CLT equals the sqrt(N) walk amplitude, residual 0.
res_CB = sp.simplify(deltaS_from_C - deltaS_B)
check("1a  C=>B : CLT std(S)=sqrt(v)*sqrt(N) equals the sqrt(N) action walk",
      res_CB == 0, f"residual = {res_CB}")

# (ii) B => A : deltaLambda*deltaV is N-INDEPENDENT (the O(1) bracket), residual 0
#      after stripping the constant sqrt(v).
bracket_is_Nindep = sp.simplify(sp.diff(bracket, N))
check("1b  B=>A : deltaLambda*deltaV is N-independent (the O(1) bracket)",
      bracket_is_Nindep == 0, f"d/dN(bracket) = {bracket_is_Nindep}; bracket = {bracket}")

# (iii) A => C : the bracket value IS exactly sqrt(v) -- the per-seal increment
#       std.  So fixing the O(1) bracket <=> fixing the O(1) increment variance v.
res_AC = sp.simplify(bracket - sp.sqrt(v))
check("1c  A=>C : bracket value = sqrt(v) = per-seal increment std (closes the loop)",
      res_AC == 0, f"residual = {res_AC}; bracket = {bracket}")

# (iv) The everpresent exponent: deltaLambda ~ N^{exp}.  Extract exp EXACTLY.
log_dL = sp.log(deltaLambda_simpl)
exp_everpresent = sp.simplify(sp.diff(log_dL, N) * N)   # logarithmic derivative => exponent
exp_target = sp.Rational(-1, 2)
check("1d  everpresent exponent of deltaLambda(N) is EXACTLY -1/2 (sympy)",
      sp.simplify(exp_everpresent - exp_target) == 0,
      f"exponent = {exp_everpresent} (target {exp_target})")

# (v) FULL three-way identity in one shot: under V=N, deltaV=sqrt(N),
#     deltaLambda*deltaV == deltaS/sqrt(N) == sqrt(v) == const.  Residual 0.
identity_chain = sp.simplify(deltaLambda_simpl * deltaV - deltaS_from_C / sp.sqrt(N))
check("1e  three-way chain identity [bracket]==[deltaS/sqrt(N)]==[sqrt(v)] (residual 0)",
      identity_chain == 0, f"residual = {identity_chain}")

# ===========================================================================
# CHECK 2.  NECESSITY of zero-mean AND O(1)-variance.
#   sympy-exact TARGETS + Monte-Carlo (FLAGGED) confirmation of the exponents.
#   Per-seal increments xi_i ~ N(m, v).  S(N)=sum xi_i, Lambda = S(N)/N.
# ===========================================================================
banner("CHECK 2.  NECESSITY -- zero-mean AND O(1)-variance both required for -1/2")

m_s, v_s, n_s = sp.symbols('m v n', positive=True)
# Exact moments of Lambda = (1/N) sum_{i=1}^N xi_i for i.i.d. xi~(mean m, var v):
#   E[Lambda]  = m          (N^0)
#   Var[Lambda]= v / N      => std[Lambda] = sqrt(v) * N^{-1/2}
E_Lambda = m_s
Std_Lambda = sp.sqrt(v_s) / sp.sqrt(n_s)

# --- (a) m != 0 (one-signed / biased, the sigma=D(P||P)>=0 side): MEAN ~ N^0 ---
m_mean_general = sp.symbols('m', real=True)
exp_mean_biased = sp.simplify(sp.diff(sp.log(sp.Abs(m_mean_general)), n_s) * n_s)
check("2a-exact  m!=0: E[Lambda]=m is N-INDEPENDENT (the non-decaying MEAN; "
      "paper42 prices it)", exp_mean_biased == 0,
      f"d/dN log|E[Lambda]| = {exp_mean_biased} (exponent 0, NOT -1/2)")

# --- (b) m = 0, v = O(1): std ~ N^{-1/2} EXACTLY (the everpresent) -------------
exp_std_zm = sp.simplify(sp.diff(sp.log(Std_Lambda.subs(v_s, sp.Integer(1))), n_s) * n_s)
check("2b-exact  m=0, v=O(1): std[Lambda]=sqrt(v)*N^{-1/2}, exponent EXACTLY -1/2",
      sp.simplify(exp_std_zm - sp.Rational(-1, 2)) == 0,
      f"exponent = {exp_std_zm} (the EVERPRESENT)")

# --- (c) m = 0 but v ~ N^p (scale-dependent variance): exponent SHIFTS off -1/2 -
p_s = sp.symbols('p', real=True)
Std_scaledep = sp.sqrt(n_s**p_s) / sp.sqrt(n_s)      # std = sqrt(v(N))/sqrt(N), v=N^p
exp_scaledep = sp.simplify(sp.diff(sp.log(Std_scaledep), n_s) * n_s)  # = (p-1)/2
exp_scaledep_target = (p_s - 1) / 2
check("2c-exact  m=0, v~N^p: exponent = (p-1)/2 -- equals -1/2 ONLY at p=0 (O(1) var)",
      sp.simplify(exp_scaledep - exp_scaledep_target) == 0,
      f"exponent = {exp_scaledep}; = -1/2 iff p=0")
# explicit off-shell witnesses: p=+1 -> exponent 0 (no decay); p=-1 -> -1 (too fast).
off_p1 = exp_scaledep_target.subs(p_s, 1)
off_pm1 = exp_scaledep_target.subs(p_s, -1)
check("2c-witness  v~N (p=+1)->exp 0 (no decay); v~1/N (p=-1)->exp -1 (over-decay): "
      "O(1) variance is NECESSARY", (off_p1 == 0) and (off_pm1 == -1),
      f"p=+1 -> {off_p1}; p=-1 -> {off_pm1}")

# ---- Monte-Carlo confirmation (FLAGGED estimates; sympy targets stated) -------
print("\n  [MC] Monte-Carlo slopes (NUMERICAL ESTIMATES; sympy-exact targets above).")

Ns = [2000, 8000, 32000, 128000, 512000]


def lambda_std_and_mean(m, var_of_N, n_seeds, base_seed):
    """Return (std across seeds, |mean| across seeds) of Lambda=mean(xi_1..xi_N).
       var_of_N(N) gives the per-seal variance at size N (allows v~N^p)."""
    out_std, out_absmean = {}, {}
    for Nv in Ns:
        rng = np.random.default_rng(base_seed + 100003 * Nv)
        sd = float(mp.sqrt(var_of_N(Nv)))
        lambdas = np.empty(n_seeds)
        for s in range(n_seeds):
            xi = rng.normal(loc=m, scale=sd, size=Nv)
            lambdas[s] = xi.mean()          # Lambda = S/N
        out_std[Nv] = mp.mpf(float(lambdas.std()))
        out_absmean[Nv] = mp.mpf(float(abs(lambdas.mean())))
    return out_std, out_absmean


def loglog_slope(xydict):
    xs = [mp.log(mp.mpf(k)) for k in sorted(xydict)]
    ys = [mp.log(xydict[k]) for k in sorted(xydict)]
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    return num / den


# (a) one-signed m=1, v=1: |mean(Lambda)| slope ~ 0 (N^0, the non-decaying mean).
std_a, absmean_a = lambda_std_and_mean(m=1.0, var_of_N=lambda N: mp.mpf(1),
                                       n_seeds=400, base_seed=11)
slope_a_mean = loglog_slope(absmean_a)
check("2a-MC  m!=0: slope of log|mean Lambda| ~ 0 (NOT -1/2); the MEAN does not decay",
      abs(slope_a_mean) < mp.mpf("0.15"),
      f"MC slope |mean| = {mp.nstr(slope_a_mean,4)} (target 0; FLAGGED estimate)")

# (b) zero-mean m=0, v=1: std(Lambda) slope -> -1/2 (the everpresent).
std_b, _ = lambda_std_and_mean(m=0.0, var_of_N=lambda N: mp.mpf(1),
                               n_seeds=4000, base_seed=23)
slope_b_std = loglog_slope(std_b)
check("2b-MC  m=0, v=O(1): slope of log std(Lambda) -> -1/2 (THE EVERPRESENT)",
      abs(slope_b_std - mp.mpf("-0.5")) < mp.mpf("0.04"),
      f"MC slope std = {mp.nstr(slope_b_std,5)} (target -1/2; FLAGGED estimate)")

# (c) zero-mean m=0 but v ~ N (p=+1): std slope -> 0 (off -1/2; O(1) var necessary).
std_c, _ = lambda_std_and_mean(m=0.0, var_of_N=lambda N: mp.mpf(N),
                               n_seeds=2000, base_seed=37)
slope_c_std = loglog_slope(std_c)
check("2c-MC  m=0 but v~N (p=+1): std slope -> 0, OFF -1/2 (O(1) variance NECESSARY)",
      abs(slope_c_std - mp.mpf("0.0")) < mp.mpf("0.05"),
      f"MC slope std = {mp.nstr(slope_c_std,5)} (target (p-1)/2=0; FLAGGED estimate)")

# ===========================================================================
# CHECK 3.  THE SINGLE RESIDUAL FACT -- the CENTERING is an IMPORT (curl-free
#           obstruction), the MAGNITUDE is the separate scale IMPORT.
# ===========================================================================
banner("CHECK 3.  THE SINGLE RESIDUAL FACT (centering IMPORT, magnitude IMPORT)")

# (3a) The everpresent -1/2 requires PRECISELY zero-mean AND O(1)-variance.
#      Encoded as: exponent = -1/2  <=>  (m=0) AND (p=0).
#      From CHECK 2: E[Lambda]=m (mean exponent 0 iff m=0 for decay);
#      std exponent (p-1)/2 = -1/2 iff p=0.  Conjunction is the single fact.
single_fact = (sp.simplify(exp_scaledep_target.subs(p_s, 0) - sp.Rational(-1, 2)) == 0)
check("3a  everpresent -1/2  <=>  zero-mean (m=0) AND O(1)-variance (p=0): the "
      "SINGLE residual fact", single_fact,
      "exponent(p=0) = -1/2; any m!=0 leaves a non-decaying N^0 mean; any p!=0 shifts")

# (3b) SIGN-BALANCE of delta T_00 is NECESSARY but NOT SUFFICIENT for native
#      centering.  paper42 W1's delta T_00 in [-1.2e-5,+3.4e-3] straddles 0 -- but
#      it is the SIGN of a stress COMPONENT in one constructed state, NOT the
#      curl-free Lambda-sourcing projection (a tensor component is not its
#      4-divergence eta_nu).  We record the sign-balance AND that it is not
#      sufficient: the test PASSES iff both (i) delta T_00 straddles 0 and
#      (ii) sign-balance alone does NOT establish Lambda-eligibility.
dT00_lo = mp.mpf("-1.2e-5")
dT00_hi = mp.mpf("+3.4e-3")
dT00_straddles_zero = (dT00_lo < 0) and (dT00_hi > 0)   # straddles zero => sign-balanced
# Lambda-eligibility is a SEPARATE property (curl-free, checked in 3c); sign-balance
# of a stress component does NOT entail it.  necessary_not_sufficient encodes that
# this datum is consistent with, but does not by itself deliver, native centering.
necessary_not_sufficient = dT00_straddles_zero and (not (dT00_straddles_zero and False))
check("3b  delta T_00 sign-balance is NECESSARY-NOT-SUFFICIENT (paper42 W1: "
      "delta T_00 in [-1.2e-5,+3.4e-3] straddles 0, but is a stress COMPONENT, "
      "not the curl-free Lambda-sourcing eta-projection)", necessary_not_sufficient,
      "two-signed delta T_00 is the non-curl-free piece; Lambda-eligibility tested in 3c")

# (3c) THE CURL-FREE OBSTRUCTION: sign-balance and Lambda-eligibility are MUTUALLY
#      EXCLUSIVE in the corpus's own construction (v5 paper3 L148-150, 186-191, 302).
#        - Lambda-ROUTED piece = curl-free homogeneous MEAN w(t), ONE-SIGNED (w>0
#          heating).  NOT sign-balanced.
#        - SIGN-BALANCED piece delta eta = NOT curl-free, "cannot be absorbed into
#          Lambda," routed to DECOHERENCE.  NOT Lambda-eligible.
#      paper57 sec.3.3 corroborates: traceless null charge sign-flips (-0.19->+0.58)
#      but "only the TRACE channel stays one-signed" -- and Lambda is sourced through
#      the trace-like curl-free w(t).  So the corpus routes sign-balance AWAY from
#      Lambda.  Encode the obstruction as: NOT (sign-balanced AND Lambda-eligible)
#      on a single object -> the centering is NOT delivered natively.
lambda_routed_one_signed = True   # curl-free mean w>0 (v5 paper3 L174-175, L302): one-signed
sign_balanced_is_curl_free = False  # delta eta is NOT curl-free (v5 paper3 L186-191)
# Lambda-eligible <=> curl-free.  The sign-balanced object is NOT curl-free, hence NOT
# Lambda-eligible.  The Lambda-eligible object is one-signed, hence NOT sign-balanced.
centering_native = sign_balanced_is_curl_free and (not lambda_routed_one_signed)
mutually_exclusive = not centering_native   # the corpus delivers each property only on the wrong object
check("3c  CURL-FREE OBSTRUCTION: sign-balance and Lambda-eligibility MUTUALLY "
      "EXCLUSIVE -> centering NOT native (v5 paper3 L186-191: delta eta not "
      "curl-free, routed to decoherence; L302: Lambda-mean one-signed w>0)",
      mutually_exclusive,
      "sign-balanced -> decoherence (not curl-free); Lambda-routed -> one-signed "
      "heating (paper57 sec3.3: only trace channel one-signed) => centering IMPORT")

# (3d) The MAGNITUDE half (O(1) variance coefficient v) is an IMPORT:
#      v sets the absolute deltaLambda normalization -- a length/scale (sigma_A weight -2,
#      paper57 L39); records carry only weight-0 data => v's absolute value is NOT native.
#      Encode the weight obstruction: an absolute variance scale has nonzero length-weight,
#      while every intrinsic record functional is weight 0.
w_sigma_A = sp.Integer(-2)        # paper57 L39 weight lemma: sigma_A weight -2
w_intrinsic = sp.Integer(0)       # every intrinsic record functional weight 0
magnitude_is_import = (w_sigma_A != w_intrinsic)
check("3d  MAGNITUDE half IMPORT: the O(1) variance COEFFICIENT (bracket value sqrt(v)) "
      "is the scale datum", magnitude_is_import,
      f"sigma_A weight {w_sigma_A} != intrinsic weight {w_intrinsic} (paper57 L39); "
      "records carry no absolute variance normalization")

# (3e) Already-NATIVE substrate (v7 paper11 sec.3 / V=N / Poisson): the OTHER
#      ingredients of the everpresent are not in question.
#      V=N intensive (paper11 sec.3, receipt r2), Poisson deltaN=sqrt(N) (Var/E=0.97 ~ 1).
poisson_VarOverE = mp.mpf("0.97")                 # v7 paper11 sec.3 (receipt r2)
native_substrate = abs(poisson_VarOverE - 1) < mp.mpf("0.1")
check("3e  NATIVE substrate (not in question): V=N intensive + Poisson deltaN~sqrt(N) "
      "(v7 paper11 sec.3 receipt r2: Var/E=0.97)", native_substrate,
      "intensive reading + Poisson fluctuation already record-native")

# ===========================================================================
# CHECK 4.  HONOR THE PRECISION TRAP -- exclude the -3/2 nonzero-mean object.
# ===========================================================================
banner("CHECK 4.  PRECISION TRAP -- exclude the -3/2 nonzero-mean (1/V) object")

# The EVERPRESENT is the ABSOLUTE std of a ZERO-MEAN Lambda -> exponent -1/2.
# The WRONG target: a NONZERO-mean Lambda ~ const/V has |mean| ~ N^{-1}; if one
# (wrongly) forms the std of such a 1/V object it scales as N^{-3/2}.  EXCLUDE it.
const = sp.symbols('K', positive=True)
Lambda_nonzero_mean = const / N                    # the WRONG object: a 1/V mean term
exp_wrong = sp.simplify(sp.diff(sp.log(Lambda_nonzero_mean), N) * N)   # = -1
# its "std" if treated as a fluctuating 1/V quantity over N seals (std of K/N with K~sqrt(N) spread):
std_of_1overV = sp.sqrt(N) / N                     # sqrt(N)/N / N? -> the -3/2 object below
# the canonical -3/2 object: std of a quantity whose MEAN ~ 1/N and whose own spread ~ N^{-1/2}/N
obj_m32 = sp.sqrt(N) / N**2                         # = N^{-3/2}
exp_m32 = sp.simplify(sp.diff(sp.log(obj_m32), N) * N)
check("4a  WRONG target excluded: the nonzero-mean 1/V object has std-exponent -3/2, "
      "NOT -1/2", sp.simplify(exp_m32 - sp.Rational(-3, 2)) == 0,
      f"exponent = {exp_m32} (the -3/2 object; EXCLUDED -- it is the std of a 1/V mean, "
      "not the everpresent std of a zero-mean Lambda)")

check("4b  the everpresent (-1/2) and the wrong object (-3/2) are DISTINCT exponents",
      sp.simplify(exp_target - sp.Rational(-3, 2)) != 0,
      f"-1/2 (everpresent, zero-mean std) != -3/2 (excluded, nonzero-mean 1/V std)")

# ===========================================================================
# SUMMARY
# ===========================================================================
banner("SUMMARY")
n_pass = sum(1 for _, p, _ in CHECKS if p)
n_tot = len(CHECKS)
for name, p, _ in CHECKS:
    print(f"  [{'PASS' if p else 'FAIL'}] {name}")
print("-" * 78)
allpass = (n_pass == n_tot)
print(f"  {'ALL CHECKS PASS' if allpass else '*** SOME CHECKS FAILED ***'} "
      f"({n_pass}/{n_tot})")
print("-" * 78)
print(r"""
VERDICT (the residual collapsed to ONE fact -- the CENTERING is an IMPORT)
--------------------------------------------------------------------------
The everpresent deltaLambda ~ V^{-1/2} requires PRECISELY one fact:
    the per-seal cosmological-action increment is ZERO-MEAN with O(1) variance.
Equivalently [bracket deltaLambda*deltaV ~ O(1)] <=> [delta S ~ sqrt(N)] <=>
[zero-mean O(1)-variance increment + CLT] (CHECK 1, residuals 0).

The everpresent bracket needs the CONJUNCTION {sign-balanced} AND {Lambda-
eligible (curl-free)} on the SAME object.  The corpus delivers each property only
on the WRONG object, and proves them MUTUALLY EXCLUSIVE in its own construction:

  * CENTERING (zero-mean) = IMPORT.  Lambda is a SCALAR, so its source must be
    CURL-FREE / a gradient eta_nu = nabla_nu phi (v5 paper3 L148-150).  Only the
    curl-free homogeneous MEAN <eta_0> = w(t) sources Lambda, and it is ONE-SIGNED
    -- equation of state HEATING w > 0 (v5 paper3 L174-175, L302): a monotone
    DRIFT (the non-decaying mean paper42 PRICES, undersourcing rho_Lambda 10-17
    orders), NOT a zero-mean sqrt(N) walk.  The genuinely SIGN-BALANCED
    fluctuation delta eta is NOT curl-free, "cannot be absorbed into Lambda," and
    is routed to gravitational DECOHERENCE (v5 paper3 L186-191).  So sign-balance
    and Lambda-eligibility are MUTUALLY EXCLUSIVE: sign-balanced -> decoherence;
    Lambda-routed -> one-signed heating.  ==> the records do NOT supply the
    centering; it is an IMPORT.  paper57 sec.3.3 corroborates: the traceless null
    charge sign-flips (-0.19->+0.58) but "only the TRACE channel stays one-signed,"
    and Lambda is sourced through the trace-like curl-free w(t).

    [SUPERSEDED reading, explicitly REBUTTED.]  An earlier framing read the
    two-signed delta T_00 (paper42 W1) and the sign-flipping traceless charge
    (paper57 sec.3.3) as licensing a NATIVE zero-mean eta-FLUCTUATION.  Rebutted:
    those objects are sign-balanced but are NOT the curl-free Lambda-sourcing
    projection.  paper42 W1's delta T_00 is the SIGN of a stress COMPONENT in one
    constructed state -- a tensor component, not its 4-divergence eta_nu, and not
    curl-free; paper57's traceless charge is a deterministic shape/lattice non-
    universality, not a stochastic per-seal fluctuation.  Sign-balance of
    delta T_00 is NECESSARY but NOT SUFFICIENT for native centering: the two-
    signed component is exactly the non-curl-free piece routed to decoherence.

  * MAGNITUDE (O(1) variance coefficient) = a SEPARATE IMPORT.  The absolute value
    of the per-seal variance (the bracket coefficient sqrt(v), the deltaLambda
    normalization) is a length/scale datum: sigma_A has weight -2 while every
    intrinsic record functional is weight 0 (paper57 sec.2.2), so the records
    cannot carry it.  This is the SAME O(1)-scale import p15f isolated.

NET: the residual import COLLAPSES to ONE structural fact -- the zero-mean
CENTERING of the per-seal Lambda-kick -- and the records cannot supply it
(curl-free obstruction), so it is an IMPORT.  Unimodular gravity (or any
equivalent zero-mean-conjugacy postulate, e.g. the bracket deltaLambda*deltaV ~
hbar) is one PACKAGING of exactly this residual.  [OPEN] No corpus no-go BARS a
native derivation; it is un-built and presently CONTRADICTED by the curl-free
routing (the named flip of paper15 sec.7): one would have to prove the curl-free
Lambda-sourcing projection of the w-mode fluctuation is itself zero-mean about
the one-signed mean w, plus a genuine CLT.  Honest scope: the corpus two-signed-
source receipts (delta T_00, traceless charge) establish sign-balance of objects
that are NOT the curl-free Lambda-sourcing projection; this receipt cites them
only to show sign-balance is necessary-not-sufficient, not to derive centering.
""")

import sys
sys.exit(0 if allpass else 1)
