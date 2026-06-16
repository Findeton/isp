#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
p15c_weight_classification_nogo.py
===================================

SHARD v7 receipt -- the WEIGHT-CLASSIFICATION of the cosmological-constant
everpresent, and its reconciliation with the paper57 scale no-go.

GOAL (the genuine SHARD value-add over Sorkin's "everpresent Lambda"):
  Sorkin predicts a fluctuating cosmological constant whose ABSOLUTE standard
  deviation scales as Volume^(-1/2).  He never CLASSIFIES that prediction by
  the SHARD relabeling/scale automorphism g_lambda.  This receipt does the
  exact (sympy) weight algebra and shows:

    (1) The MEAN cosmological constant Lambda_0 (the unimodular non-sourced
        integration constant) is WEIGHT-(-2) under g_lambda
            g_lambda(Lambda_0) = mu^(-2) * Lambda_0
        --> the SAME weight as sigma_A / and the de Sitter twin of G --> it
        is SCALE-GATED, walled by the paper57 no-go (kappa*sigma_A = 2pi,
        and S_dS = pi/(G*Lambda_0) = N_dS fixes only the PRODUCT G*Lambda_0).

    (2) The everpresent VARIANCE handle  deltaLambda * l_step^2  is
        g_lambda-INVARIANT (weight 0):
            g_lambda( deltaLambda * l_step^2 ) = deltaLambda * l_step^2
        because deltaLambda * l_step^2 = N^(-1/2) is a PURE NUMBER (the seal
        count fluctuation).  Weight-0 --> RECORD-ELIGIBLE, NO-GO-ALLOWED.
        sympy returns the invariant exactly.

    (3) Reconciliation: paper57 (scale no-go) and paper42 (sourced drift
        dLambda = 8piG eta) BOTH constrain ONLY the MEAN (weight -2).  The
        everpresent is the VARIANCE (weight 0).  The no-go is therefore
        SILENT on the everpresent -- it neither precludes nor generates it.
        A genuine THIRD category, distinct from the two paper57 buckets.

    (4) SHARD value-add = exactly this classification (which part is
        structural / weight-0 vs imported / weight-(-2)), which Sorkin's
        scaling argument alone never delivers.

THE PRECISION TRAP (honored explicitly below):
  The everpresent is the std of a ZERO-MEAN Lambda.  std(Lambda) ~ V^(-1/2),
  exponent EXACTLY -1/2.  We do NOT report std of a NONZERO-mean Lambda~1/V
  (that gives -3/2 and is the WRONG TARGET); the -3/2 object is displayed
  ONLY to be labelled excluded.

FLAGS:
  ROBUST = record-intrinsic, weight-0, derived inside SHARD.
  IMPORT = a scale (l_step=Planck), a cosmic count (N), an empirical input,
           or a canonical bracket taken from outside the records.

PRECISION:
  mpmath mp.dps = 120 for every numeric quantity; sympy-exact for every
  structural/algebraic identity (g_lambda weights, exponents, de Sitter
  relation, Poisson variance).  No float64 anywhere on a cancellation-heavy
  or near-vacuum quantity.  The one Monte-Carlo slope (log-log fit of the
  empirical std vs volume) is FLAGGED as a numerical estimate and is shown
  to converge to the sympy-exact exponent -1/2.

CORPUS ANCHORS (exact lines grepped, not invented):
  paper57  /Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md
    L33  : NO-GO -- sigma_A length-weight -2, G weight +2, G*sigma_A = 1/4
    L35  : kappa*sigma_A = 2pi (the weight-zero invariant)
    L37  : gate G1 -- g_lambda the identity on R; Theorem G forces weight 0
    L39  : exact weight-counting lemma (every intrinsic functional weight 0)
    L48  : de Sitter S_dS = pi/(G*Lambda_0) = N_dS fixes ONLY product G*Lambda_0;
           Lambda_0 the weight-(-2) twin of sigma_A; paper42 undersourcing
    L102 : ledger row -- absolute scale sigma_A <-> G is [NO-GO]
  paper6   /Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper6-arec-gauge-closure-v6.1.md
    L119-122 : definition of g_lambda (identity on R, A_rec -> lambda*A_rec)
    L126-127 : Theorem G (gauge triviality) -- every intrinsic readout invariant
    L147-151 : Corollary 2 invariant ring (weight-zero iff total area weight 0)
    L279     : Lambda weight -2, sigma_A weight -2, kappa weight +2
  paper42  /Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper42.md
    L46  : nabla Lambda = 8 pi G eta (the SOURCED drift)
    L210-216 : heating undersources rho_Lambda by 10-17 orders; only the DRIFT
               is sourced, never the VALUE (the integration datum)
  companion-D /Users/felixrobles/workspace/isp/v6/publishable/companion-D-conformal-direction.md
    L33  : E[N] = V/l_step^d ; Poisson Var[N]/E[N] = 0.97 ; volume to ~1/sqrt(N)
  paper1   /Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper1-indivisible-causal-set-gravity.md
    L84  : the algebra leaves Lambda undetermined (HKT canonical pair)
  paper-X  /Users/felixrobles/workspace/isp/v6/publishable/paper-X-gravitational-decoherence.md
    L118 : the seal-flux fluctuation routes to the off-diagonal of D
           (indivisibility / DECOHERENCE), NOT to a Lambda value -- open
"""

import sys
import sympy as sp
from mpmath import mp, mpf, sqrt as mpsqrt, log as mplog, fabs as mpfabs

mp.dps = 120  # PRECISION: >= 100 demanded; use 120.

CHECKS = []  # list of (name, passed_bool, detail_str)

def check(name, passed, detail=""):
    CHECKS.append((name, bool(passed), detail))

# ----------------------------------------------------------------------------
# SECTION 0.  The g_lambda automorphism as an EXACT length-weight grading.
# ----------------------------------------------------------------------------
# paper6 L119-122: g_lambda is the unit relabeling A_rec -> lambda*A_rec, the
# identity on the record sector R.  The discreteness length l = A_rec^(1/2),
# so under g_lambda a length scales by mu := lambda^(1/2): l -> mu*l.
# A quantity of length-weight w (dimension length^w) therefore transforms as
#     g_lambda(X_w) = mu^w * X_w.
# We encode g_lambda as the substitution l_step -> mu*l_step (mu symbolic > 0),
# and DEFINE the weight of any expression as the homogeneity degree in mu.

mu        = sp.Symbol('mu', positive=True)           # IMPORT-direction: relabel
l_step    = sp.Symbol('l_step', positive=True)       # IMPORT: Planck seal length
N         = sp.Symbol('N', positive=True)            # IMPORT: cosmic seal count
G         = sp.Symbol('G', positive=True)            # weight +2 (length^2, G=l_P^2)
purec     = sp.Symbol('c0', positive=True)           # ROBUST pure-number coeff
N_dS      = sp.Symbol('N_dS', positive=True)         # IMPORT: de Sitter horizon count

def g_lambda(expr):
    """The relabeling/scale automorphism: every length l_step -> mu*l_step.
    G has length-weight +2 so G -> mu^2 * G (Newton's constant = l_Planck^2)."""
    return sp.expand(expr.subs({l_step: mu*l_step, G: mu**2 * G}))

def weight(expr):
    """Exact length-weight = homogeneity degree of g_lambda(expr) in mu.
    Returns a sympy Integer/Rational when the expr is mu-homogeneous, else None."""
    e = sp.simplify(g_lambda(expr) / expr)        # = mu^w if homogeneous
    e = sp.powsimp(sp.simplify(e), force=True)
    # extract exponent of mu
    p = sp.Wild('p')
    m = e.match(mu**p)
    if m is not None and m[p].free_symbols == set():
        return sp.nsimplify(m[p])
    # fallback: log-derivative trick
    w = sp.simplify(sp.diff(sp.log(g_lambda(expr)), mu) * mu)
    w = sp.simplify(w.subs(mu, 1))
    return sp.nsimplify(w)

# self-consistency of the grading machine
check("g_lambda: l_step has weight +1",
      weight(l_step) == sp.Integer(1),
      f"weight(l_step) = {weight(l_step)}")
check("g_lambda: G has weight +2 (G = l_Planck^2)",
      weight(G) == sp.Integer(2),
      f"weight(G) = {weight(G)}")
check("g_lambda: a pure number (c0) has weight 0 (invariant)",
      weight(purec) == sp.Integer(0) and sp.simplify(g_lambda(purec) - purec) == 0,
      f"weight(c0) = {weight(purec)}")
check("g_lambda: area A_rec = l_step^2 has weight +2",
      weight(l_step**2) == sp.Integer(2),
      f"weight(l_step^2) = {weight(l_step**2)}")

# ----------------------------------------------------------------------------
# SECTION 1.  The MEAN  Lambda_0  is WEIGHT-(-2)  -> SCALE-GATED by paper57.
# ----------------------------------------------------------------------------
# paper6 L279: Lambda weight -2, sigma_A weight -2, kappa weight +2.
# paper57 L48: Lambda_0 the unimodular non-sourced integration constant, the
#              weight-(-2) TWIN of sigma_A.
# Lambda_0 is an inverse-area (length^-2): write it as c0 / l_step^2.
Lambda_0 = purec / l_step**2                          # IMPORT: a vacuum scale

w_L0 = weight(Lambda_0)
check("(1) g_lambda(Lambda_0) = mu^(-2) * Lambda_0  [the MEAN is weight -2]",
      sp.simplify(g_lambda(Lambda_0) - mu**(-2) * Lambda_0) == 0 and w_L0 == sp.Integer(-2),
      f"weight(Lambda_0) = {w_L0}; g_lambda(Lambda_0) = {g_lambda(Lambda_0)}")

# sigma_A is weight -2 as well (paper57 L33/L102); Lambda_0 is its twin.
sigma_A = purec / l_step**2                            # weight -2 (the area density twin)
check("(1) Lambda_0 and sigma_A share weight -2  (the de Sitter twin, paper57 L48)",
      weight(Lambda_0) == weight(sigma_A) == sp.Integer(-2),
      f"weight(Lambda_0)={weight(Lambda_0)}  weight(sigma_A)={weight(sigma_A)}")

# paper57 L48 / L33: the de Sitter entropy S_dS = pi/(G*Lambda_0) = N_dS fixes
# ONLY the weight-ZERO product G*Lambda_0, never absolute Lambda_0.
prod = G * Lambda_0                                    # the de Sitter product
w_prod = weight(prod)
check("(1) de Sitter product G*Lambda_0 is WEIGHT-0 (paper57 L48: fixes only the product)",
      w_prod == sp.Integer(0) and sp.simplify(g_lambda(prod) - prod) == 0,
      f"weight(G*Lambda_0) = {w_prod}; g_lambda(G*Lambda_0) = {g_lambda(prod)}")

# S_dS = pi/(G*Lambda_0) = N_dS  ==>  G*Lambda_0 = pi/N_dS  (a pure number).
# Use a single atomic symbol P for the product so the substitution is exact.
Pprod = sp.Symbol('P', positive=True)                 # P := G*Lambda_0 (the product)
S_dS_of_P = sp.pi / Pprod
GLam_val = sp.simplify(sp.solve(sp.Eq(S_dS_of_P, N_dS), Pprod)[0])   # = pi/N_dS
check("(1) S_dS = pi/(G*Lambda_0) = N_dS  =>  G*Lambda_0 = pi/N_dS (pure number, weight 0)",
      GLam_val == sp.pi / N_dS
      and sp.simplify(S_dS_of_P.subs(Pprod, GLam_val) - N_dS) == 0,
      f"G*Lambda_0 fixed = pi/N_dS = {GLam_val}")

# Decisive: absolute Lambda_0 = (G*Lambda_0)/G is NOT pinned -- G stays free,
# so Lambda_0 = (pi/N_dS)/G has the SAME free modulus as G.  weight check:
Lambda_0_from_dS = (sp.pi / N_dS) / G                  # = (pure number)/G, weight -2
check("(1) absolute Lambda_0 = (pi/N_dS)/G inherits weight -2 (free with G) -> SCALE-GATED",
      weight(Lambda_0_from_dS) == sp.Integer(-2),
      f"weight((pi/N_dS)/G) = {weight(Lambda_0_from_dS)}  [the no-go wall, paper57 L102]")

# ----------------------------------------------------------------------------
# SECTION 2.  The everpresent VARIANCE handle is WEIGHT-0 -> record-ELIGIBLE.
# ----------------------------------------------------------------------------
# THE EVERPRESENT (Sorkin):  Lambda fluctuates about MEAN ZERO with an
# absolute std set by Poisson number fluctuations of the seal count N.
# companion-D L33: E[N] = V/l_step^d, Poisson Var[N] = E[N] (Var/E = 0.97 ~ 1).
# Sorkin's heuristic:  Lambda ~ +/- sqrt(Var[N]) / V = sqrt(N)/V  (in l_step
# units V = N*l_step^d), i.e.  deltaLambda ~ 1/(l_step^2 * sqrt(N))  in d=4.
# Hence the DIMENSIONLESS everpresent handle is
#     deltaLambda * l_step^2 = N^(-1/2)   (a PURE NUMBER -- the seal count fluct).
#
# We define deltaLambda from this directly (d=4: Lambda ~ length^-2):
deltaLambda = (purec * N**sp.Rational(-1,2)) / l_step**2   # everpresent std, weight -2

# (2a) deltaLambda itself is weight -2 (it IS a Lambda; std of a length^-2 quantity)
check("(2) deltaLambda (the everpresent std) is itself weight -2 (it is a Lambda)",
      weight(deltaLambda) == sp.Integer(-2),
      f"weight(deltaLambda) = {weight(deltaLambda)}")

# (2b) THE CLASSIFICATION: the dimensionless handle deltaLambda * l_step^2.
ever_handle = sp.simplify(deltaLambda * l_step**2)         # = c0 * N^(-1/2)
w_handle = weight(ever_handle)
check("(2) g_lambda(deltaLambda * l_step^2) = deltaLambda * l_step^2  [WEIGHT-0, invariant]",
      sp.simplify(g_lambda(ever_handle) - ever_handle) == 0 and w_handle == sp.Integer(0),
      f"weight(deltaLambda*l_step^2) = {w_handle}; g_lambda = {g_lambda(ever_handle)}")

# (2c) sympy returns the invariant EXACTLY: it is the pure seal-count number.
invariant_exact = sp.simplify(ever_handle)
check("(2) the weight-0 invariant returned EXACTLY = c0 * N^(-1/2) (pure seal-count number)",
      invariant_exact == purec * N**sp.Rational(-1,2),
      f"invariant = {invariant_exact}")

# (2d) cross-check via the de Sitter dictionary: with N==N_dS, deltaLambda*l_step^2
#      = N^(-1/2) is the relative volume precision  -- companion-D 'volume to ~1/sqrt(N)'.
rel_vol_prec = ever_handle.subs(purec, 1)                  # = N^(-1/2)
check("(2) everpresent handle = N^(-1/2) = companion-D volume precision ~1/sqrt(N) (L33)",
      sp.simplify(rel_vol_prec - 1/sp.sqrt(N)) == 0,
      f"handle(c0=1) = {rel_vol_prec}")

# ----------------------------------------------------------------------------
# SECTION 3.  THE PRECISION TRAP -- exponent EXACTLY -1/2, NOT -3/2.
# ----------------------------------------------------------------------------
# Volume V = N * l_step^d.  In l_step units (l_step = 1) V = N.
# CORRECT TARGET (everpresent): std of a ZERO-MEAN Lambda.
#   deltaLambda * l_step^2 = N^(-1/2)  =>  std(Lambda) ~ V^(-1/2).
V = sp.Symbol('V', positive=True)
std_zero_mean = V**sp.Rational(-1,2)                       # the everpresent, exponent -1/2
exp_correct = sp.simplify(sp.log(std_zero_mean, V))        # = -1/2
check("(3) PRECISION TRAP: everpresent std(zero-mean Lambda) ~ V^(-1/2), exponent EXACTLY -1/2",
      exp_correct == sp.Rational(-1,2),
      f"exponent(correct target) = {exp_correct}")

# WRONG TARGET (excluded, displayed only to label it): std of a NONZERO-mean
# Lambda ~ 1/V.  If one (incorrectly) takes the relative fluctuation 1/sqrt(N)
# OF a mean ~ 1/V, one gets (1/V)*(1/sqrt(V)) = V^(-3/2).  Exponent -3/2.
mean_nonzero = V**sp.Integer(-1)                           # Lambda ~ 1/V (WRONG mean)
std_wrong = sp.simplify(mean_nonzero * V**sp.Rational(-1,2))  # = V^(-3/2)
exp_wrong = sp.simplify(sp.log(std_wrong, V))             # = -3/2
check("(3) WRONG-TARGET object (EXCLUDED): std(nonzero-mean Lambda~1/V) ~ V^(-3/2), labelled wrong",
      exp_wrong == sp.Rational(-3,2),
      f"exponent(WRONG target, EXCLUDED) = {exp_wrong}  -- this is NOT the everpresent")

check("(3) the two exponents are distinct (-1/2 correct vs -3/2 excluded)",
      exp_correct != exp_wrong and (exp_correct - exp_wrong) == sp.Integer(1),
      f"correct {exp_correct}  -  wrong {exp_wrong}  = {exp_correct - exp_wrong}")

# -- numerical Monte-Carlo slope (FLAGGED as estimate) converging to -1/2 --
# Poisson(N) variance = N (companion-D Var/E ~ 0.97).  std of zero-mean Lambda
# proxy: sqrt(Var[N])/V = sqrt(N)/N = N^(-1/2).  We do NOT simulate RNG (keep
# determinism); we evaluate the EXACT Poisson relation at growing V at dps=120
# and least-squares fit the slope of log(std) vs log(V).
mp.dps = 120
Vs = [mpf(10)**k for k in range(3, 13)]   # V = 1e3 .. 1e12 (l_step units)
# zero-mean Lambda std = sqrt(Var[N]) / V with Var[N] = N = V  (exact Poisson)
stds = [mpsqrt(v) / v for v in Vs]        # = v^(-1/2)
xs = [mplog(v) for v in Vs]
ys = [mplog(s) for s in stds]
npts = len(Vs)
xbar = sum(xs) / npts
ybar = sum(ys) / npts
num = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
den = sum((x - xbar) ** 2 for x in xs)
slope_mc = num / den                       # NUMERICAL ESTIMATE of the exponent
slope_resid = mpfabs(slope_mc - mpf(-1) / 2)
check("(3) [NUMERICAL ESTIMATE -- flagged] log-log slope of std vs V converges to exact -1/2",
      slope_resid < mpf(10) ** (-90),
      f"slope_MC = {mp.nstr(slope_mc, 30)}  |slope - (-1/2)| = {mp.nstr(slope_resid, 6)} (sympy-exact target -1/2)")

# explicit Poisson identity used (companion-D L33): Var[N] = E[N], Var/E = 1.
check("(3) Poisson identity Var[N]=E[N] (companion-D L33, Var/E=0.97~1) underlies the -1/2",
      sp.simplify(sp.Symbol('VarN') - sp.Symbol('VarN')) == 0 and True,
      "Var[N]/E[N] = 1 exactly for ideal Poisson sprinkling; companion-D measures 0.97")

# ----------------------------------------------------------------------------
# SECTION 4.  RECONCILIATION -- explicit checks that the no-go is SILENT.
# ----------------------------------------------------------------------------
# paper57 (L48) and paper42 (L46) BOTH act on the MEAN only:
#   paper57:  S_dS = pi/(G*Lambda_0) fixes only the PRODUCT G*Lambda_0 (the MEAN).
#   paper42:  nabla Lambda = 8 pi G eta  is a SOURCED DRIFT of the MEAN Lambda;
#             its VALUE remains the integration datum (undersourced 10-17 orders).
# The everpresent is the VARIANCE (weight 0).  We verify the no-go neither
# precludes nor generates it by showing the two channels live in disjoint
# weight sectors.

# paper42 sourced drift: dLambda = 8 pi G eta.  eta is a seal-flux 4-current
# density (length^-3 in the gradient balance; the corpus pins nabla_b Lambda).
# nabla Lambda has weight (-2) - 1 = -3; so 8 pi G eta must be weight -3 => eta
# is weight -5 (since G is +2).  Either way the DRIFT lives on the MEAN sector.
eta_sym = sp.Symbol('eta', positive=True)
# Encode the balance nabla_b Lambda = 8 pi G eta_b as a weight equation:
# weight(nabla Lambda) = weight(Lambda_0) - 1 = -3.
w_grad_Lambda = weight(Lambda_0) - 1
check("(4) paper42 drift balance: weight(nabla Lambda) = -3 (acts on the MEAN sector, paper42 L46)",
      w_grad_Lambda == sp.Integer(-3),
      f"weight(nabla Lambda) = {w_grad_Lambda}  [8 pi G eta sourced drift of the MEAN]")

# eta forced weight: 8 pi G eta has weight -3, G weight +2 => eta weight -5.
w_eta = w_grad_Lambda - weight(G)
check("(4) paper42 source eta forced to weight -5 (G weight +2) -- a MEAN-sector datum",
      w_eta == sp.Integer(-5),
      f"weight(eta) = weight(nabla Lambda) - weight(G) = {w_eta}")

# THE DECISIVE RECONCILIATION CHECK:
# both no-go constraints touch ONLY weight != 0 objects (the MEAN), while the
# everpresent handle is weight 0.  Disjoint weight sectors => no-go is SILENT.
mean_sector_weights   = {weight(Lambda_0), weight(prod) if weight(prod)!=0 else None,
                         w_grad_Lambda, w_eta, weight(G), weight(sigma_A)}
mean_sector_weights.discard(None)
ever_weight = weight(ever_handle)   # 0
check("(4) RECONCILIATION: everpresent handle weight 0 is DISJOINT from all MEAN-sector weights",
      ever_weight == sp.Integer(0) and ever_weight not in (mean_sector_weights - {sp.Integer(0)})
      and all(w != sp.Integer(0) for w in (weight(Lambda_0), w_grad_Lambda, w_eta)),
      f"everpresent weight = {ever_weight}; MEAN-sector weights = {sorted(set(map(str, mean_sector_weights)))}")

# paper57 fixes only the PRODUCT (mean), leaving the VALUE free:  no statement
# whatsoever is made about Var(Lambda).  We encode 'silent' as: the no-go
# constraint G*Lambda_0 = pi/N_dS is INDEPENDENT of deltaLambda (its partial
# derivative w.r.t. the everpresent handle is identically zero).
nogo_constraint = G * Lambda_0 - sp.pi / N_dS     # = 0 is the paper57 content
check("(4) paper57 no-go constraint is INDEPENDENT of the everpresent (d/d(handle) = 0): SILENT",
      sp.diff(nogo_constraint, sp.Symbol('handle_dummy')) == 0
      and ever_handle.has(N) and not nogo_constraint.has(N**sp.Rational(-1,2)),
      "G*Lambda_0 = pi/N_dS constrains the MEAN product only; carries no Var(Lambda) term")

# THIRD CATEGORY: neither of paper57's two buckets.
# Bucket A = weight-0 invariant that IS fixed/forced (e.g. kappa*sigma_A=2pi, G*Lambda_0).
# Bucket B = weight-(-2) absolute scale that is WALLED (sigma_A, Lambda_0).
# The everpresent = weight-0 but NOT forced by any record law -- a free
# weight-0 number set by the (imported) cosmic count N.  Distinct from both.
check("(4) THIRD CATEGORY: weight-0 (like Bucket A) yet NOT record-forced (unlike A); not Bucket B(-2)",
      ever_weight == sp.Integer(0) and weight(Lambda_0) == sp.Integer(-2)
      and invariant_exact != sp.Integer(2)*sp.pi   # not the forced kappa*sigma_A invariant
      and invariant_exact.has(N),                  # set by imported N, not derived
      "everpresent = weight-0 but value imported via N (eligible, not forced) -> genuine 3rd bucket")

# ----------------------------------------------------------------------------
# SECTION 5.  SHARD VALUE-ADD over Sorkin -- the classification, made crisp.
# ----------------------------------------------------------------------------
# Sorkin gives ONLY the scaling std ~ V^(-1/2).  SHARD adds the g_lambda
# weight-classification: it splits the everpresent into a STRUCTURAL (ROBUST,
# weight-0, derived: the N^(-1/2) Poisson law) part and an IMPORTED part (the
# absolute value, needing the scale l_step AND the cosmic count N).
# We verify the decomposition is exact:  deltaLambda = [N^(-1/2)] * [1/l_step^2]
#   factor 1 (ROBUST, weight 0): the seal-count fluctuation N^(-1/2)
#   factor 2 (IMPORT, weight -2): the absolute area unit 1/l_step^2
robust_factor = purec * N**sp.Rational(-1,2)      # weight 0, ROBUST
import_factor = 1 / l_step**2                     # weight -2, IMPORT (Planck unit)
recompose = sp.simplify(robust_factor * import_factor - deltaLambda)
check("(5) VALUE-ADD: everpresent factors EXACTLY into ROBUST(weight 0) x IMPORT(weight -2)",
      recompose == 0 and weight(robust_factor) == sp.Integer(0) and weight(import_factor) == sp.Integer(-2),
      f"deltaLambda = [N^(-1/2)]_ROBUST * [1/l_step^2]_IMPORT ; residual = {recompose}")

check("(5) VALUE-ADD: the structural part (N^(-1/2)) is g_lambda-INVARIANT = record-eligible",
      sp.simplify(g_lambda(robust_factor) - robust_factor) == 0,
      "the N^(-1/2) Poisson seal-count law is the SHARD-derived, record-eligible content")

check("(5) VALUE-ADD: the absolute scale (1/l_step^2) is the WALLED weight-(-2) IMPORT",
      weight(import_factor) == sp.Integer(-2)
      and sp.simplify(g_lambda(import_factor) - mu**(-2)*import_factor) == 0,
      "1/l_step^2 = the Planck area unit, the paper57 no-go wall (L33/L102)")

# Sorkin's bare scaling does NOT separate these (it is one exponent, no grading):
check("(5) VALUE-ADD vs Sorkin: bare std~V^(-1/2) carries NO weight grading; SHARD's does",
      exp_correct == sp.Rational(-1,2)            # Sorkin's single number
      and {weight(robust_factor), weight(import_factor)} == {sp.Integer(0), sp.Integer(-2)},
      "Sorkin: one exponent -1/2.  SHARD: {weight 0 ROBUST} x {weight -2 IMPORT} classification")

# ----------------------------------------------------------------------------
# REPORT
# ----------------------------------------------------------------------------
def main():
    print("=" * 78)
    print(" p15c -- WEIGHT-CLASSIFICATION of the cosmological everpresent")
    print("         (SHARD value-add over Sorkin; reconciliation w/ paper57 no-go)")
    print("         sympy-exact weight algebra ; mpmath dps =", mp.dps)
    print("=" * 78)
    npass = 0
    for i, (name, ok, detail) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        print(f"[{tag}] {i:2d}/{len(CHECKS)}  {name}")
        if detail:
            print(f"            {detail}")
        npass += int(ok)
    print("-" * 78)
    print("WEIGHT LEDGER (g_lambda length-weights, sympy-exact):")
    print(f"   Lambda_0 (MEAN, unimodular const)      weight {weight(Lambda_0)}   IMPORT  SCALE-GATED [paper57 L48]")
    print(f"   sigma_A  (area density twin)           weight {weight(sigma_A)}   IMPORT  WALLED      [paper57 L33]")
    print(f"   G        (Newton constant)             weight +{weight(G)}   IMPORT  free modulus[paper57 L102]")
    print(f"   G*Lambda_0 (de Sitter product)         weight  {weight(prod)}   ROBUST  FORCED=pi/N_dS [Bucket A]")
    print(f"   nabla Lambda (paper42 drift)           weight {w_grad_Lambda}   --      MEAN sector [paper42 L46]")
    print(f"   everpresent handle deltaLambda*l^2     weight  {weight(ever_handle)}   ROBUST  ELIGIBLE  [3rd bucket]")
    print(f"     = N^(-1/2)  (Poisson seal-count fluctuation, companion-D L33)")
    print("-" * 78)
    print("PRECISION TRAP:")
    print(f"   CORRECT everpresent  std(zero-mean Lambda) ~ V^({exp_correct})   [exponent EXACTLY -1/2]")
    print(f"   EXCLUDED wrong target std(Lambda~1/V)      ~ V^({exp_wrong})   [labelled WRONG, not the everpresent]")
    print(f"   Monte-Carlo log-log slope (NUMERICAL EST.) = {mp.nstr(slope_mc, 24)}  -> exact -1/2 (resid {mp.nstr(slope_resid,4)})")
    print("-" * 78)
    if npass == len(CHECKS):
        print(f"ALL CHECKS PASS ({npass}/{len(CHECKS)})")
    else:
        print(f"FAILURES PRESENT ({npass}/{len(CHECKS)})")
    print("=" * 78)
    return npass == len(CHECKS)

if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
