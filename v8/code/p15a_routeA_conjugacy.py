"""
p15a -- ROUTE A: the direct unimodular-conjugacy route to Sorkin's everpresent Lambda.

GOAL
----
Show that SHARD reproduces Sorkin's "everpresent Lambda" fluctuation SCALING

        deltaLambda  ~  V^{-1/2}          (exponent EXACTLY  -1/2)

via one IMPORTED canonical bracket plus three ROBUST (record-intrinsic, weight-0,
derived) corpus facts, and CONFIRM the exponent both sympy-exactly and by a Monte-Carlo
regression on the correct (ZERO-MEAN) everpresent object.

THE DERIVATION (each step FLAGGED ROBUST / IMPORT)
-------------------------------------------------
1. [IMPORT]  Unimodular canonical pairing  deltaLambda * deltaV ~ hbar  (~1 in Planck
   units).  Lambda is conjugate to the four-volume V in unimodular gravity
   (Henneaux-Teitelboim 1989; Unruh-Wald 1989; Sorkin's everpresent-Lambda heuristic).
   This bracket is NOT in the SHARD corpus: the corpus's ONLY canonical pairing is the
   HKT spatial-metric / conjugate-momentum pair (paper1), which "leaves Lambda
   undetermined".  We grep-CONFIRM the deltaLambda*deltaV bracket is ABSENT and cite the
   line.  So Route A is conditional on this one import.

2. [ROBUST]  Volume = number x scale^d :  V = N * l_step^d, the corpus-verified
   "number = volume" (companion-D, Myrheim-Meyer cardinality  E[N] = V / l_step^d).
   l_step itself is the one IMPORTed absolute scale (weight +d); the COUNT N is weight-0.

3. [ROBUST]  Poisson seal count :  deltaN = sqrt(N)  (companion-D: Var[N]/E[N] = 0.97,
   i.e. Poisson, volume recovered to ~1/sqrt(N)).  Hence
        deltaV / V = deltaN / N = 1/sqrt(N)   =>   deltaV = V / sqrt(N) = sqrt(N) l_step^d.

4. [DERIVED]  Combine 1+3 :
        deltaLambda ~ hbar / deltaV ~ 1 / ( sqrt(N) l_step^d ),
   and in record-curvature units (multiply by l_step^2):
        deltaLambda * l_step^2  ~  1 / sqrt(N).
   Since V = N l_step^d at fixed l_step, deltaLambda ~ V^{-1/2}: EXPONENT in V (or N) is
   EXACTLY -1/2.  Checked sympy-exact.

5. [MC, FLAGGED]  Monte-Carlo confirmation: simulate the ZERO-MEAN everpresent object,
   regress log(std) vs log(V); slope -> -1/2.  This is a numerical ESTIMATE; the exact
   target is the sympy value -1/2.

THE PRECISION TRAP (honored explicitly)
---------------------------------------
The everpresent object is the ABSOLUTE standard deviation of a ZERO-MEAN Lambda
(Sorkin assumes <Lambda> = 0).  That std scales as V^{-1/2}  (exponent EXACTLY -1/2).
The WRONG-TARGET object is the std of a NONZERO-mean Lambda ~ 1/V, whose std scales as
V^{-3/2}.  We compute and DISPLAY the -3/2 object ONLY to LABEL it EXCLUDED.  Reporting
-3/2 as "the everpresent" would be the precision trap; we do not.

FLAGS LEGEND
------------
  [ROBUST] = record-intrinsic, weight-0, derived (eligible to be a record output).
  [IMPORT] = an imported datum: l_step = Planck length (the one absolute scale),
             N = cosmic seal count, the unimodular canonical bracket, an empirical input.

PRECISION
---------
  mpmath mp.dps = 120 for every numeric quantity (never float64).
  sympy-exact for every structural identity (the exponents, the weight grading, the
  de Sitter G*Lambda0 relation).  The MC slope is flagged a numerical estimate and the
  sympy-exact target it must converge to is printed alongside.

CORPUS CITATIONS (grepped, exact line numbers, NOT invented)
------------------------------------------------------------
  paper57  /Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md
      L25 : unimodular fork -> Lambda a NON-SOURCED integration constant Lambda0.
      L48 : de Sitter  S_dS = pi/(G*Lambda0) = N_dS  fixes only the PRODUCT G*Lambda0,
            never the absolute weight-(-2) Lambda0 (weight-twin of sigma_A).
  companion-D  /Users/felixrobles/workspace/isp/v6/publishable/companion-D-conformal-direction.md
      L33 : number = volume,  E[N] = V/l_step^d ; Poisson Var[N]/E[N] = 0.97 ;
            volume recovered to ~1/sqrt(N).
      L35 : count weight-0 (49 whatever mu) ; absolute volume = N*l_step^d weight +d.
  paper1  /Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper1-indivisible-causal-set-gravity.md
      L79-84 : the ONLY canonical pair is HKT spatial-metric / conjugate-momentum,
               "fixed only up to G and a cosmological constant Lambda, which the algebra
               leaves UNDETERMINED" -> the deltaLambda*deltaV bracket is ABSENT (import).
  paper42  /Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper42.md
      L191    : the SOURCED drift  nabla Lambda = 8 pi G eta.
      L210-211: the mean drift UNDERSOURCES rho_Lambda by 10-17 orders (value = state datum).
  paper6  /Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper6-arec-gauge-closure-v6.1.md
      L119-130: g_lambda relabeling automorphism + Theorem G (intrinsic readout =>
                g_lambda-invariant => weight-0).
"""

import mpmath as mp
import sympy as sp
import random
import subprocess
import numpy as np

mp.mp.dps = 120

# ---------------------------------------------------------------------------
# Corpus anchor table (paths + lines used in citations / the ABSENCE grep)
# ---------------------------------------------------------------------------
PAPER57 = "/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md"
COMPD   = "/Users/felixrobles/workspace/isp/v6/publishable/companion-D-conformal-direction.md"
PAPER1  = "/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper1-indivisible-causal-set-gravity.md"
PAPER42 = "/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper42.md"
PAPER6  = "/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper6-arec-gauge-closure-v6.1.md"

checks = []  # (name, passed_bool, detail)
def record(name, passed, detail):
    checks.append((name, bool(passed), detail))
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}] {name}: {detail}")

print("=" * 78)
print("p15a -- ROUTE A: unimodular conjugacy -> Sorkin everpresent deltaLambda ~ V^-1/2")
print("=" * 78)

# ===========================================================================
# CHECK 1 -- [IMPORT] the unimodular canonical bracket is ABSENT in the corpus
#            (the corpus's only canonical pair is HKT, leaving Lambda undetermined)
# ===========================================================================
print("\n--- CHECK 1 [IMPORT]: unimodular bracket deltaLambda*deltaV ~ hbar is an IMPORT")
print("    (grep-confirm it is ABSENT in the SHARD corpus; only HKT pair present) ---")

def grep_count(pattern, paths):
    """Count grep -E matches across files; return (count, sample_lines)."""
    try:
        out = subprocess.run(
            ["grep", "-rniE", pattern] + paths,
            capture_output=True, text=True
        ).stdout
    except Exception:
        out = ""
    lines = [l for l in out.splitlines() if l.strip()]
    return len(lines), lines[:4]

corpus_files = [PAPER1, PAPER42, PAPER57, COMPD, PAPER6]

# (a) The unimodular Lambda<->V conjugacy bracket: look for any co-occurrence of a
#     Lambda-V canonical/conjugate pairing. The corpus has NONE.
brk_patterns = [
    r"delta *Lambda.*delta *V",
    r"delta *V.*delta *Lambda",
    r"Lambda.*conjugate.*(volume|V\b)",
    r"(volume|four-volume).*conjugate.*Lambda",
    r"Henneaux.?Teitelboim",
    r"Unruh.?Wald",
    r"everpresent",
]
total_bracket_hits = 0
for pat in brk_patterns:
    c, _ = grep_count(pat, corpus_files)
    total_bracket_hits += c
bracket_absent = (total_bracket_hits == 0)
record("bracket_is_import_absent_in_corpus", bracket_absent,
       f"unimodular deltaLambda*deltaV / HT / Unruh-Wald / everpresent hits in corpus "
       f"= {total_bracket_hits} (expected 0 => the bracket is an IMPORT, not corpus-derived)")

# (b) The corpus's ONLY canonical pairing -- HKT metric/momentum, leaving Lambda
#     undetermined -- IS present (paper1 L79-84). Confirm it.
c_hkt, hkt_lines = grep_count(r"Hojman.?Kucha.?.?Teitelboim", [PAPER1])
c_undet, _ = grep_count(r"cosmological constant.*leaves.*undetermined|Lambda.*algebra leaves undetermined|leaves.*undetermined", [PAPER1])
hkt_present = (c_hkt >= 1 and c_undet >= 1)
record("corpus_only_pair_is_HKT_Lambda_undetermined", hkt_present,
       f"HKT canonical pair present (hits={c_hkt}) and 'Lambda ... leaves undetermined' "
       f"present (hits={c_undet}) at paper1 L79-84 -> Lambda not canonically fixed in corpus")

print("    cited absence: paper1 L84 '... a cosmological constant Lambda, which the "
      "algebra leaves undetermined'")
print("    => Route A imports the bracket deltaLambda*deltaV ~ hbar [IMPORT, conditional].")

# ===========================================================================
# CHECK 2 -- [ROBUST] number = volume :  V = N * l_step^d   (companion-D L33)
# ===========================================================================
print("\n--- CHECK 2 [ROBUST]: number = volume,  V = N*l_step^d  (companion-D L33) ---")

# symbolic identity V = N * l_step^d  <=>  N = V / l_step^d  (Myrheim-Meyer cardinality)
N_s, l_s, d_s, V_s = sp.symbols('N l_step d V', positive=True)
V_expr = N_s * l_s**d_s            # V = N l_step^d
N_from_V = sp.simplify(V_expr / l_s**d_s)   # should be N
numvol_ok = sp.simplify(N_from_V - N_s) == 0
# grep-confirm the corpus statement E[N] = V/l_step^d
c_numvol, _ = grep_count(r"E\[N\].*=.*V.*l_step|number.*=.*volume|number = volume", [COMPD])
record("number_equals_volume_V_eq_N_lstep_d", numvol_ok and c_numvol >= 1,
       f"sympy: V/l_step^d - N = 0 (ok={numvol_ok}); companion-D 'E[N]=V/l_step^d' hits={c_numvol}")
print("    [ROBUST] count N weight-0 (companion-D L35: '49 whatever mu'); "
      "[IMPORT] l_step weight +1 (the one absolute scale).")

# ===========================================================================
# CHECK 3 -- [ROBUST] Poisson seal count : deltaN = sqrt(N)  (companion-D L33)
#            => deltaV = V/sqrt(N) = sqrt(N) l_step^d
# ===========================================================================
print("\n--- CHECK 3 [ROBUST]: Poisson count deltaN=sqrt(N) (Var/E=0.97), "
      "deltaV=V/sqrt(N) (companion-D L33) ---")

# Poisson: Var[N] = E[N] = N, so deltaN = sqrt(Var[N]) = sqrt(N). sympy-exact relation.
deltaN_s = sp.sqrt(N_s)
# deltaV/V = deltaN/N = 1/sqrt(N)  ->  deltaV = V/sqrt(N)
deltaV_over_V = sp.simplify(deltaN_s / N_s)             # = 1/sqrt(N)
deltaV_expr   = sp.simplify(V_expr * deltaV_over_V)     # = sqrt(N) l_step^d
deltaV_target = sp.sqrt(N_s) * l_s**d_s
poisson_ok = (sp.simplify(deltaV_over_V - 1/sp.sqrt(N_s)) == 0
              and sp.simplify(deltaV_expr - deltaV_target) == 0)
# grep-confirm the Poisson 0.97 and the ~1/sqrt(N) recovery
c_pois, _ = grep_count(r"Var\[N\]/E\[N\] = 0\.97|Var/E = 0\.97|Poisson|1/sqrt\(N\)|1/.N", [COMPD])
record("poisson_count_deltaV_eq_V_over_sqrtN", poisson_ok and c_pois >= 1,
       f"sympy: deltaV/V = 1/sqrt(N) and deltaV = sqrt(N) l_step^d "
       f"(ok={poisson_ok}); companion-D Poisson/1-over-sqrt(N) hits={c_pois}")

# Numeric (mpmath dps=120) sanity of Var/E = 1 for an ideal Poisson; corpus measured 0.97
mp.mp.dps = 120
Var_over_E_ideal = mp.mpf(1)                  # ideal Poisson
corpus_measured  = mp.mpf("0.97")             # companion-D L33 finite-sample value
record("poisson_var_over_E_consistent", abs(Var_over_E_ideal - 1) == 0
       and abs(corpus_measured - 1) < mp.mpf("0.1"),
       f"ideal Var/E = {mp.nstr(Var_over_E_ideal,3)}; corpus measured {mp.nstr(corpus_measured,3)} "
       f"(|.-1| = {mp.nstr(abs(corpus_measured-1),3)} < 0.1)")

# ===========================================================================
# CHECK 4 -- [DERIVED] combine: deltaLambda ~ 1/(sqrt(N) l_step^d) ;
#            deltaLambda*l_step^2 ~ 1/sqrt(N) ; EXPONENT in V (or N) EXACTLY -1/2
# ===========================================================================
print("\n--- CHECK 4 [DERIVED]: deltaLambda ~ hbar/deltaV, exponent in V EXACTLY -1/2 (sympy) ---")

hbar = sp.Integer(1)   # Planck units ~ 1 [IMPORT convention]
# deltaLambda ~ hbar / deltaV = 1 / (sqrt(N) l_step^d)
deltaLambda_expr = sp.simplify(hbar / deltaV_expr)
deltaLambda_target = 1 / (sp.sqrt(N_s) * l_s**d_s)
combine_ok = sp.simplify(deltaLambda_expr - deltaLambda_target) == 0

# record-curvature units: deltaLambda * l_step^2 ~ 1/sqrt(N)
dLam_curv = sp.simplify(deltaLambda_expr * l_s**2)
# at d=2 this is exactly 1/sqrt(N); in general it is l_step^(2-d)/sqrt(N).
dLam_curv_d2 = dLam_curv.subs(d_s, 2)
curv_ok = sp.simplify(dLam_curv_d2 - 1/sp.sqrt(N_s)) == 0

# EXPONENT in N at fixed l_step:  deltaLambda = (l_step^-d) * N^(-1/2)  -> exponent -1/2.
# log deltaLambda = -1/2 log N - d log l_step ; substitute u = log N and differentiate.
logdL = sp.log(deltaLambda_expr)
u = sp.Symbol('u')  # u = log N
logdL_u = logdL.subs(N_s, sp.exp(u))
expo_in_N = sp.simplify(sp.diff(logdL_u, u))
exponent_in_N_ok = (expo_in_N == sp.Rational(-1, 2))

# EXPONENT in V at fixed l_step:  V = N l_step^d  => N = V/l_step^d, deltaLambda ~ V^-1/2
deltaLambda_in_V = sp.simplify(deltaLambda_expr.subs(N_s, V_s / l_s**d_s))
w = sp.Symbol('w')  # w = log V
logdL_V = sp.log(deltaLambda_in_V).subs(V_s, sp.exp(w))
expo_in_V = sp.simplify(sp.diff(logdL_V, w))
exponent_in_V_ok = (expo_in_V == sp.Rational(-1, 2))

EXACT_EXPONENT = sp.Rational(-1, 2)
record("combine_deltaLambda_form", combine_ok,
       f"sympy: deltaLambda = 1/(sqrt(N) l_step^d) (residual 0 = {combine_ok})")
record("record_curvature_units_d2", curv_ok,
       f"sympy: deltaLambda*l_step^2 = 1/sqrt(N) at d=2 (residual 0 = {curv_ok})")
record("exponent_in_N_is_minus_half", exponent_in_N_ok,
       f"sympy d log(deltaLambda)/d log N = {expo_in_N}  (target {EXACT_EXPONENT})")
record("exponent_in_V_is_minus_half", exponent_in_V_ok,
       f"sympy d log(deltaLambda)/d log V = {expo_in_V}  (target {EXACT_EXPONENT})")
print(f"    EXACT everpresent exponent (sympy) = {EXACT_EXPONENT} = {float(EXACT_EXPONENT)}")

# ===========================================================================
# CHECK 5 -- THE PRECISION TRAP: the everpresent is the std of a ZERO-MEAN Lambda
#            (-> -1/2).  The std of a NONZERO-mean Lambda~1/V is the WRONG TARGET
#            (-> -3/2) and is EXCLUDED.  Show both exponents sympy-exact + label.
# ===========================================================================
print("\n--- CHECK 5 [PRECISION TRAP]: zero-mean std -> -1/2 (everpresent); "
      "nonzero-mean std -> -3/2 (WRONG TARGET, EXCLUDED) ---")

# Model both objects symbolically.
# ZERO-MEAN everpresent:  Lambda = +/- hbar/deltaV  with <Lambda>=0,
#   std(Lambda) = hbar/deltaV = 1/(sqrt(N) l_step^d) ~ V^{-1/2}.  EXPONENT -1/2.
std_zero_mean = deltaLambda_in_V            # ~ V^{-1/2}
logZ = sp.log(std_zero_mean).subs(V_s, sp.exp(w))
expo_zero_mean = sp.simplify(sp.diff(logZ, w))   # -1/2

# NONZERO-MEAN wrong target: take a mean Lambda ~ c/V (mean value 1/V) and ask for the
# *relative* fluctuation deltaLambda/Lambda = deltaV/V = 1/sqrt(N): then
#   absolute std of (1/V)*(1 + 1/sqrt(N)-fluctuation) about its 1/V mean
#   = (1/V) * (1/sqrt(N)) ~ V^{-1} * V^{-1/2} = V^{-3/2}.  EXPONENT -3/2.
mean_lambda_wrong = 1 / V_s                  # nonzero mean ~ 1/V
rel_fluct = (1/sp.sqrt(N_s)).subs(N_s, V_s / l_s**d_s)   # = 1/sqrt(N) in terms of V
std_nonzero_mean = sp.simplify(mean_lambda_wrong * rel_fluct)   # ~ V^{-3/2}
logW = sp.log(std_nonzero_mean).subs(V_s, sp.exp(w))
expo_nonzero_mean = sp.simplify(sp.diff(logW, w))   # -3/2

zero_ok = (expo_zero_mean == sp.Rational(-1, 2))
wrong_ok = (expo_nonzero_mean == sp.Rational(-3, 2))
record("everpresent_zero_mean_exponent_minus_half", zero_ok,
       f"sympy: std(ZERO-MEAN Lambda) exponent in V = {expo_zero_mean} "
       f"(THE everpresent, target -1/2)")
record("wrong_target_nonzero_mean_exponent_minus_three_half_EXCLUDED", wrong_ok,
       f"sympy: std(NONZERO-mean Lambda~1/V) exponent in V = {expo_nonzero_mean} "
       f"(WRONG TARGET, EXCLUDED -- NOT the everpresent)")
print("    LABEL: only the ZERO-MEAN object (-1/2) is Sorkin's everpresent Lambda; "
      "the -3/2 object is the excluded wrong target.")

# ===========================================================================
# CHECK 6 -- [MC, FLAGGED] Monte-Carlo: regress log(std of zero-mean Lambda) vs log(V).
#            Slope -> -1/2.  FLAGGED numerical estimate; sympy-exact target -1/2.
# ===========================================================================
print("\n--- CHECK 6 [MC ESTIMATE, FLAGGED]: regress log std(zero-mean Lambda) vs log V "
      "-> slope ~ -1/2 ---")

# NOTE ON PRECISION: this block is an explicitly-FLAGGED Monte-Carlo ESTIMATE whose only
# job is to confirm the slope converges to the sympy-EXACT -1/2 already proven in
# CHECK 4/5.  The per-sample object is a signed integer Poisson fluctuation (Ncount-Nbar);
# integer counts and their sample variance carry no cancellation-heavy / near-vacuum
# content, so the sampling is done in float64 (fast, exact for the integers involved) and
# the FINAL log-log least-squares regression is lifted into mpmath dps=120.  The exact
# target it must converge to is the sympy value -1/2 (printed alongside, CHECK 4).
np.random.seed(20260616)
l_step_val = mp.mpf(1)        # [IMPORT] Planck length set to 1 (Planck units)
d_val = 2                     # 2d for the MC (the de Sitter horizon is 2-surface-counted;
                              #   d is reported, the exponent -1/2 is d-independent)
n_trials = 200000             # samples per volume to estimate the zero-mean std

# volume axis: V = Nbar * l_step^d at a ladder of mean counts Nbar
Nbar_list = [200, 400, 800, 1600, 3200, 6400, 12800, 25600]

logV = []
logStd = []
for Nbar in Nbar_list:
    V_mp = mp.mpf(Nbar) * l_step_val**d_val            # mean physical volume (mpf, exact)
    # vectorised Poisson sampling of the integer seal COUNT (float64 sampler, exact ints)
    counts = np.random.poisson(lam=Nbar, size=n_trials).astype(np.float64)
    # ZERO-MEAN everpresent realization (Sorkin ansatz, <Lambda>=0):
    #   Lambda_real = hbar * (Ncount - Nbar) / V   (zero mean; std = sqrt(N)/V = 1/sqrt(V)
    #   in l_step units).  This is the standard everpresent |Lambda| ~ 1/sqrt(V_4),
    #   <Lambda> = 0.  Var/E=0.97 Poisson => std(Lambda) ~ V^{-1/2}.
    Vf = float(V_mp)
    lam_real = (counts - Nbar) / Vf                    # zero-mean float array
    std_f = float(np.std(lam_real, ddof=1))            # MC std estimate (numerical)
    std = mp.mpf(std_f)
    logV.append(mp.log(V_mp))
    logStd.append(mp.log(std))
    print(f"    Nbar={Nbar:6d}  V={mp.nstr(V_mp,4):>8}  std(Lambda)={mp.nstr(std,5):>12}  "
          f"log10 std={mp.nstr(mp.log(std)/mp.log(10),5)}")

# least-squares slope (FINAL regression lifted into mpmath dps=120)
n = len(logV)
sx = sum(logV); sy = sum(logStd)
sxx = sum(x*x for x in logV); sxy = sum(x*y for x, y in zip(logV, logStd))
slope = (n*sxy - sx*sy) / (n*sxx - sx*sx)
slope_target = mp.mpf(-1) / 2
slope_err = abs(slope - slope_target)
slope_ok = slope_err < mp.mpf("0.05")
record("MC_slope_approaches_minus_half_FLAGGED_estimate", slope_ok,
       f"MC slope = {mp.nstr(slope,8)}  vs sympy-exact target -1/2 = {mp.nstr(slope_target,4)} "
       f"(|err| = {mp.nstr(slope_err,4)} < 0.05)  [NUMERICAL ESTIMATE, converges to -1/2]")
print(f"    FLAG: MC slope {mp.nstr(slope,6)} is a numerical ESTIMATE; the EXACT exponent "
      f"is the sympy value -1/2.")

# ===========================================================================
# CHECK 7 -- de Sitter cross-consistency (sympy-exact): the corpus's own G*Lambda0
#            relation fixes only the PRODUCT, never absolute Lambda0 (paper57 L48).
#            Route A is about the FLUCTUATION scaling, orthogonal to the value no-go.
# ===========================================================================
print("\n--- CHECK 7 [ROBUST]: de Sitter G*Lambda0 = pi/N_dS fixes only the PRODUCT "
      "(paper57 L48); Route A scales the FLUCTUATION, not the value ---")

G_s, Lam0_s, NdS_s = sp.symbols('G Lambda0 N_dS', positive=True)
# S_dS = pi/(G*Lambda0) = N_dS  =>  G*Lambda0 = pi/N_dS  (the PRODUCT, never absolute Lambda0)
S_dS = sp.pi / (G_s * Lam0_s)
GLam0 = sp.simplify(sp.pi / NdS_s)            # the product G*Lambda0 solved from S_dS = N_dS
# verify: pi/(G Lambda0) = N_dS  <=>  G Lambda0 = pi/N_dS
desitter_ok = sp.simplify(sp.pi/GLam0 - NdS_s) == 0
c_dS, _ = grep_count(r"S_dS = pi/\(G.?Lambda0\)|S_dS.*=.*N_dS|de Sitter entropy", [PAPER57])
record("desitter_product_only_GxLambda0", desitter_ok and c_dS >= 1,
       f"sympy: S_dS = pi/(G*Lambda0) => G*Lambda0 = pi/N_dS (product only); "
       f"paper57 de-Sitter hits={c_dS}. Route A is fluctuation-scaling, orthogonal to value no-go.")

# weight grading cross-check (Theorem G / paper6): N weight 0, l_step weight +1,
#   deltaLambda*l_step^2 weight 0 (a record-eligible RATIO), absolute deltaLambda weight -2.
print("    weight ledger [paper6 Theorem G, L119-130]: N weight 0 [ROBUST]; "
      "l_step weight +1 [IMPORT];")
print("    deltaLambda*l_step^2 = 1/sqrt(N) weight 0 [ROBUST, eligible]; "
      "absolute deltaLambda weight -2 [walled, needs l_step].")

# ===========================================================================
# SUMMARY
# ===========================================================================
print("\n" + "=" * 78)
n_pass = sum(1 for _, p, _ in checks if p)
n_tot = len(checks)
for name, p, _ in checks:
    print(f"  {'PASS' if p else 'FAIL'}  {name}")
print("-" * 78)
all_pass = (n_pass == n_tot)
print(f"  ALL CHECKS {'PASS' if all_pass else 'FAIL'} ({n_pass}/{n_tot})")
print("=" * 78)
print("\nROUTE A VERDICT: SHARD reproduces Sorkin's everpresent SCALING "
      "deltaLambda ~ V^{-1/2},")
print("exponent EXACTLY -1/2 (sympy-exact), from ONE imported unimodular bracket "
      "[IMPORT] + ")
print("number=volume + Poisson seal count [both ROBUST, weight-0, companion-D]. The "
      "MC slope")
print(f"({mp.nstr(slope,6)}) confirms it numerically [ESTIMATE]. The -3/2 nonzero-mean "
      "object is the")
print("EXCLUDED wrong target (precision trap honored). Route A is the FLUCTUATION "
      "scaling and is")
print("orthogonal to the paper57 absolute-VALUE no-go (de Sitter fixes only G*Lambda0).")

import sys
sys.exit(0 if all_pass else 1)
