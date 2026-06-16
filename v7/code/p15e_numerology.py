#!/usr/bin/env python3
"""
p15e_numerology.py  --  CANONICAL receipt: SHARD vs the Sorkin everpresent-Lambda numerology.

THE CLAIM UNDER TEST
--------------------
Sorkin's causal-set "everpresent Lambda": a unimodular / number-volume substrate
fluctuates the cosmological constant by

      deltaLambda  ~  1 / sqrt(V)        (V = spacetime 4-volume in fundamental units)

With V = the 4-volume of the cosmic past lightcone ~ 10^240 Planck-4-volumes,
this gives deltaLambda ~ 10^(-121.86) in Planck units, matching the OBSERVED
Lambda ~ 10^(-122). SHARD's records (number = volume, Myrheim-Meyer) carry the
SAME substrate, so SHARD REPRODUCES this number.

THE HONESTY CORE (what this receipt makes algebraically explicit)
-----------------------------------------------------------------
The "10^-120 hit" is NOT a derived number. With the single cosmic length R_H,
the natural cosmic 4-volume is V = R_H^4, and then

      deltaLambda = 1/sqrt(V) = 1/sqrt(R_H^4) = 1/R_H^2 = Lambda_obs   EXACTLY.

So the entire numerology collapses to ONE measured ratio,  R_H / l_p ~ 10^60.
The exponent (-1/2 scaling, and 4 = spacetime dimension) is ROBUST / structural.
The MAGNITUDE 10^(-120) is IMPORT-gated, doubly-then-triply:
   IMPORT-1  l_step = Planck length  (sets the 1/l_p^2 weight-(-2) absolute unit)
   IMPORT-2  the cosmic count N ~ 10^240  (= V in l_p^4; sets how big sqrt(V) is)
   IMPORT-3  H0 (measured)  -> R_H = c/H0  (the one length the whole thing rides on)
=> SORKIN NUMEROLOGY REPRODUCED, NOT IMPROVED.

THE PRECISION TRAP (honored below, machine-checked)
---------------------------------------------------
The everpresent object is the ABSOLUTE STANDARD DEVIATION of a ZERO-MEAN Lambda
(Sorkin posits <Lambda> = 0 from unimodular conjugacy). That std scales as
V^(-1/2): exponent EXACTLY -1/2. We do NOT report the std of a NONZERO-mean
Lambda ~ 1/V; THAT object scales as V^(-3/2) and is the WRONG TARGET. Both are
computed; the -3/2 object is displayed ONLY to be explicitly EXCLUDED.

PRECISION: mpmath mp.dps = 120 for all magnitudes; sympy-exact for every
structural identity (the -1/2 exponent, the 4 = dim collapse, the de Sitter
relation, the weight grading). A Monte-Carlo slope of the std scaling is given
ONLY as a numerical cross-check and is FLAGGED as such, with its sympy-exact
target -1/2 printed alongside.

FLAGS:  [ROBUST] = record-intrinsic / weight-0 / structural-exact.
        [IMPORT] = a measured scale (l_step=Planck), the cosmic count N, or H0.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 120

CHECKS = []  # (label, passed_bool)
def check(label, cond):
    CHECKS.append((label, bool(cond)))
    print("  [%s] %s" % ("PASS" if cond else "FAIL", label))
    return bool(cond)

L = "=" * 80
l = "-" * 80
print(L)
print("p15e :: SHARD vs Sorkin everpresent-Lambda numerology  ::  dps =", mp.mp.dps)
print(L)

# =====================================================================
# 0. STRUCTURAL IDENTITIES  (sympy-EXACT, no floats)  --  [ROBUST]
# =====================================================================
print("\n" + l)
print("0. STRUCTURAL / ALGEBRAIC IDENTITIES   (sympy-exact)        [ROBUST]")
print(l)

V, RH, lp, N, d = sp.symbols('V R_H l_p N d', positive=True)
c0 = sp.Symbol('c0', positive=True)
lV = sp.Symbol('lV', real=True)   # lV = log(V); exponent = d log(std)/d log(V) = d/dlV

# (i) EVERPRESENT: std of a ZERO-MEAN Lambda = c0 / sqrt(V).  std(V) = c0 * exp(-lV/2).
std_zero_in_lV = c0 * sp.exp(-sp.Rational(1, 2) * lV)
exp_zero_mean = sp.simplify(sp.diff(sp.log(std_zero_in_lV), lV))
print("EVERPRESENT (zero-mean std)  ~ V^(d log std/d log V) , exponent =",
      exp_zero_mean, " (target -1/2)")
check("everpresent exponent is EXACTLY -1/2 (sympy)", exp_zero_mean == sp.Rational(-1, 2))

# (ii) WRONG-TARGET object: std of a NONZERO-mean Lambda ~ 1/V.
#      If Lambda ~ A/V with fixed relative spread, its absolute std ~ B/V * (1/sqrt(V))
#      ... but the canonical "wrong target" people accidentally quote is the std of
#      the MEAN-shifted quantity scaling as V^(-3/2). Show it and EXCLUDE it.
std_wrong_in_lV = c0 * sp.exp(-sp.Rational(3, 2) * lV)
exp_wrong = sp.simplify(sp.diff(sp.log(std_wrong_in_lV), lV))
print("WRONG-TARGET (nonzero-mean Lambda~1/V) exponent =", exp_wrong,
      " <- EXCLUDED, not the everpresent")
check("wrong-target exponent is -3/2 and != -1/2 (excluded)",
      (exp_wrong == sp.Rational(-3, 2)) and (exp_wrong != sp.Rational(-1, 2)))

# (iii) THE COLLAPSE: with V = R_H^4 (single cosmic length, spacetime dim 4),
#       deltaLambda = 1/sqrt(V) = 1/sqrt(R_H^4) = R_H^(-2). Exact in sympy.
deltaLambda_of_RH = sp.simplify(1 / sp.sqrt(RH**4))
print("deltaLambda = 1/sqrt(R_H^4) =", deltaLambda_of_RH, " (= 1/R_H^2 = Lambda_obs)")
check("1/sqrt(R_H^4) == R_H^(-2)  (algebraic collapse, EXACT)",
      sp.simplify(deltaLambda_of_RH - RH**(-2)) == 0)

# (iv) general dim: V = R_H^d -> deltaLambda = R_H^(-d/2). de Sitter / curvature
#      Lambda_obs ~ 1/R_H^2. Match deltaLambda = Lambda_obs  <=>  d/2 = 2  <=> d = 4.
match_eq = sp.Eq(sp.Rational(1, 2) * d, 2)         # d/2 (from 1/sqrt(R_H^d)) == 2
d_sol = sp.solve(match_eq, d)
print("Match deltaLambda(=R_H^{-d/2}) == Lambda_obs(=R_H^{-2})  =>  d =", d_sol)
check("numerology requires spacetime dimension d == 4 (sympy-exact)", d_sol == [4])

# (v) de Sitter relation (curvature route): Lambda_obs ~ 3 H0^2 / c^2 in length^-2
#     and R_H = c/H0  =>  Lambda_obs ~ 3 / R_H^2  ~  R_H^(-2). Exponent of R_H:
H0s, cs = sp.symbols('H0 c', positive=True)
lRH = sp.Symbol('lRH', real=True)              # lRH = log(R_H)
Lam_dS = 3 * H0s**2 / cs**2
Lam_dS_in_RH = sp.simplify(Lam_dS.subs(H0s, cs / RH))   # substitute H0 = c/R_H -> 3/R_H^2
print("de Sitter:  Lambda_obs = 3 H0^2/c^2 =", Lam_dS_in_RH, " (~ R_H^{-2})")
# express as fn of lRH = log(R_H):  3/R_H^2 = 3 * exp(-2 lRH)
Lam_dS_in_lRH = 3 * sp.exp(-2 * lRH)
exp_dS = sp.simplify(sp.diff(sp.log(Lam_dS_in_lRH), lRH))
print("de Sitter exponent of R_H =", exp_dS, " (target -2)")
check("de Sitter Lambda_obs ~ R_H^(-2) (exponent -2, exact)", exp_dS == -2)

# (vi) weight grading (paper6 Theorem G / paper57 no-go), symbolic:
#      deltaLambda_abs = (1/l_p^2) * (1/sqrt(N)).  weight(deltaLambda_abs) = -2.
#      deltaLambda * l_p^2 = 1/sqrt(N): weight 0.  Confirm by power of l_p.
# |deltaLambda|_abs = (1/l_p^2)*(1/sqrt(N)); weight = power of l_p = d log/d log(l_p).
llp = sp.Symbol('llp', real=True)              # llp = log(l_p); N independent of l_p
abs_dLam_in_llp = sp.exp(-2 * llp) * (1 / sp.sqrt(N))   # ~ l_p^(-2)
w_abs = sp.simplify(sp.diff(sp.log(abs_dLam_in_llp), llp))
# deltaLambda * l_p^2 = 1/sqrt(N): no l_p -> weight 0.
w_dimless = sp.simplify(sp.diff(sp.log(1 / sp.sqrt(N)), llp))
print("weight(|deltaLambda|_abs) =", w_abs, "  weight(deltaLambda * l_p^2) =", w_dimless)
check("absolute deltaLambda is weight -2 (gated on l_step); ratio weight 0",
      (w_abs == -2) and (w_dimless == 0))

# =====================================================================
# 1. IMPORTS  (measured numbers)  --  [IMPORT]
# =====================================================================
print("\n" + l)
print("1. IMPORTS  (measured / scale inputs)                        [IMPORT]")
print(l)

# [IMPORT-1] l_step = Planck length & time (the SHARD scale, IF l_step = Planck)
l_p = mp.mpf('1.616255e-35')      # m   Planck length      [IMPORT-1: l_step=Planck]
t_p = mp.mpf('5.391247e-44')      # s   Planck time         [IMPORT-1]
c   = mp.mpf('299792458')         # m/s exact
print("[IMPORT-1 l_step=Planck]  l_p = %s m   t_p = %s s" %
      (mp.nstr(l_p, 7), mp.nstr(t_p, 7)))

# [IMPORT-3] H0 (measured) -> R_H, T_H
H0_kmsMpc = mp.mpf('67.4')                     # km/s/Mpc  Planck 2018  [IMPORT-3: H0]
Mpc_m     = mp.mpf('3.0856775814913673e22')    # m
H0 = H0_kmsMpc * mp.mpf('1000') / Mpc_m        # s^-1
R_H = c / H0                                    # m
T_H = 1 / H0                                    # s
print("[IMPORT-3 H0]             H0 = %s s^-1  ->  R_H = %s m,  T_H = %s s" %
      (mp.nstr(H0, 6), mp.nstr(R_H, 6), mp.nstr(T_H, 6)))

# Dimensionless cosmic length in Planck units (this IS the one ratio):
Lr = R_H / l_p                                 # = R_H/l_p ~ 10^60   [IMPORT, derived from above]
log10_Lr = mp.log10(Lr)
print("R_H / l_p = %s  = 10^%s   <== THE ONE MEASURED RATIO" %
      (mp.nstr(Lr, 8), mp.nstr(log10_Lr, 8)))

# =====================================================================
# 2. COSMIC 4-VOLUME  V = N  (in Planck units)  --  [IMPORT-2: cosmic N]
# =====================================================================
print("\n" + l)
print("2. COSMIC 4-VOLUME  V = N seal-count  (Planck units)   [IMPORT-2 cosmic N]")
print(l)
# Two O(1) conventions; the EXPONENT is convention-independent (ROBUST).
V_box  = Lr**3 * (c * T_H / l_p)               # naive box  R_H^3 * (cT_H)
V_R4   = Lr**4                                  # single-length 4-radius R_H^4
for nm, Vv in [("box  R_H^3*(cT_H)", V_box), ("R_H^4 (single length)", V_R4)]:
    print("V[%-22s] = %s l_p^4  = 10^%s  = N seals" %
          (nm, mp.nstr(Vv, 6), mp.nstr(mp.log10(Vv), 8)))
N = V_R4
log10_N = mp.log10(N)
check("V in l_p^4 ~ 10^240-ish: log10(N) in (243,244) [cosmic 4-volume]",
      243 < log10_N < 244)
check("both O(1) conventions give the SAME exponent (|dlog10|<1e-90) -> ROBUST",
      abs(mp.log10(V_box) - mp.log10(V_R4)) < mp.mpf('1e-90'))

# =====================================================================
# 3. SORKIN EVERPRESENT:  deltaLambda = 1/sqrt(V) = 1/sqrt(N)  (Planck) [the prediction]
# =====================================================================
print("\n" + l)
print("3. SORKIN EVERPRESENT  deltaLambda = 1/sqrt(V) = 1/sqrt(N)  (Planck units)")
print(l)
deltaLambda = 1 / mp.sqrt(N)                    # curvature units 1/l_p^2 (Planck)
log10_dLam = mp.log10(deltaLambda)
print("sqrt(N) = 10^%s   ->   deltaLambda = 10^%s   (Planck, units 1/l_p^2)" %
      (mp.nstr(mp.log10(mp.sqrt(N)), 8), mp.nstr(log10_dLam, 8)))
print("  TAG: SCALING exponent -1/2  [ROBUST];  MAGNITUDE 10^%s  [IMPORT-gated]" %
      mp.nstr(log10_dLam, 5))

# =====================================================================
# 4. OBSERVED Lambda  (de Sitter / curvature route)  --  [IMPORT]
# =====================================================================
print("\n" + l)
print("4. OBSERVED Lambda  ~ 1/R_H^2  (de Sitter curvature)        [IMPORT]")
print(l)
Lam_obs = Lr**(-2)                              # (l_p/R_H)^2, Planck units 1/l_p^2
log10_Lam_obs = mp.log10(Lam_obs)
print("Lambda_obs ~ (l_p/R_H)^2 = 10^%s   (Planck, units 1/l_p^2)" %
      mp.nstr(log10_Lam_obs, 8))

# =====================================================================
# 5. THE COMPARISON: predicted vs observed log10 ratio (~0)
# =====================================================================
print("\n" + l)
print("5. PREDICTED vs OBSERVED   (log10 ratio ~ 0)")
print(l)
ratio = deltaLambda / Lam_obs
log10_ratio = mp.log10(ratio)
print("deltaLambda = 10^%s   Lambda_obs = 10^%s" %
      (mp.nstr(log10_dLam, 8), mp.nstr(log10_Lam_obs, 8)))
print("log10( deltaLambda / Lambda_obs ) = %s   (target 0)" % mp.nstr(log10_ratio, 12))
check("predicted == observed: |log10 ratio| < 1e-90 (EXACT collapse for V=R_H^4)",
      abs(log10_ratio) < mp.mpf('1e-90'))

# the exact algebraic reason, numerically confirmed:
print("\nWHY (exact): 1/sqrt(R_H^4)=R_H^-2=Lambda_obs.  sqrt(V)=R_H^2/l_p^2=10^%s," %
      mp.nstr(2 * log10_Lr, 7))
print("i.e. sqrt(V) = (R_H/l_p)^2.  The '10^120' IS just (10^60)^2 = (R_H/l_p)^2.")
check("sqrt(N) == (R_H/l_p)^2 numerically (10^120 = (10^60)^2)",
      abs(mp.log10(mp.sqrt(N)) - 2 * log10_Lr) < mp.mpf('1e-90'))

# =====================================================================
# 6. THE PRECISION TRAP:  zero-mean std (RIGHT)  vs  V^(-3/2) (WRONG)
#    -- both numeric, slopes from a high-precision finite difference,
#       targets are the sympy-exact -1/2 and -3/2.
# =====================================================================
print("\n" + l)
print("6. PRECISION TRAP: everpresent = ZERO-MEAN std ~ V^(-1/2) [RIGHT]")
print("                   vs nonzero-mean Lambda~1/V std ~ V^(-3/2) [WRONG, EXCLUDED]")
print(l)
# Analytic slope check (mpmath finite difference at two volumes 10x apart).
V1 = N
V2 = N * mp.mpf('10')
std_zero_1, std_zero_2 = 1 / mp.sqrt(V1), 1 / mp.sqrt(V2)          # RIGHT target
std_wrong_1, std_wrong_2 = V1**mp.mpf('-1.5'), V2**mp.mpf('-1.5')  # WRONG target
slope_right = (mp.log10(std_zero_2) - mp.log10(std_zero_1)) / (mp.log10(V2) - mp.log10(V1))
slope_wrong = (mp.log10(std_wrong_2) - mp.log10(std_wrong_1)) / (mp.log10(V2) - mp.log10(V1))
print("analytic d log10(std)/d log10(V):  RIGHT(zero-mean) = %s  (target -1/2 = -0.5)" %
      mp.nstr(slope_right, 20))
print("                                    WRONG(~1/V)      = %s  (target -3/2 = -1.5)" %
      mp.nstr(slope_wrong, 20))
check("RIGHT everpresent slope == -1/2 exactly (zero-mean std) [ROBUST]",
      abs(slope_right - mp.mpf('-0.5')) < mp.mpf('1e-90'))
check("WRONG object slope == -3/2 (displayed only to EXCLUDE it)",
      abs(slope_wrong - mp.mpf('-1.5')) < mp.mpf('1e-90'))
check("RIGHT and WRONG targets are distinct (-1/2 != -3/2)",
      slope_right != slope_wrong)

# Monte-Carlo cross-check of the -1/2 scaling (FLAGGED numerical estimate).
print("\n  [NUMERICAL ESTIMATE, FLAGGED] Monte-Carlo: empirical std of a ZERO-MEAN")
print("  unimodular fluctuation across volumes V_k; fitted slope -> sympy-exact -1/2.")
import random
random.seed(20260616)
logV_pts, log_std_pts = [], []
for k in range(2, 7):                       # V = 10^k fundamental cells
    Vk = 10**k
    trials = 4000
    # zero-mean unit-variance increments; everpresent Lambda ~ sum / V  with the
    # Sorkin scaling: fluctuation amplitude of MEAN of Vk zero-mean unit steps
    # = 1/sqrt(Vk). Estimate std of (sum/sqrt(Vk))/sqrt(Vk) = sum/Vk over trials.
    vals = []
    for _ in range(trials):
        s = 0.0
        # cheap zero-mean sampler: +/-1 steps
        for _ in range(Vk if Vk <= 1000 else 1000):
            s += 1.0 if random.random() < 0.5 else -1.0
        neff = Vk if Vk <= 1000 else 1000
        vals.append(s / neff)               # mean of zero-mean steps ~ 1/sqrt(neff)
    m = sum(vals) / len(vals)
    var = sum((v - m) ** 2 for v in vals) / (len(vals) - 1)
    std = var ** 0.5
    import math
    logV_pts.append(math.log10(min(Vk, 1000)))
    log_std_pts.append(math.log10(std))
# least-squares slope
npts = len(logV_pts)
mx = sum(logV_pts) / npts
my = sum(log_std_pts) / npts
slope_mc = (sum((logV_pts[i] - mx) * (log_std_pts[i] - my) for i in range(npts))
            / sum((logV_pts[i] - mx) ** 2 for i in range(npts)))
print("  MC fitted slope = %.4f   (numerical; converges to sympy-exact -1/2)" % slope_mc)
check("MC slope estimate near -1/2 (|slope+0.5|<0.12, NUMERICAL/FLAGGED)",
      abs(slope_mc - (-0.5)) < 0.12)

# =====================================================================
# 7. WEIGHT GRADING & IMPORT LEDGER  (the no-go reconciliation)
# =====================================================================
print("\n" + l)
print("7. WEIGHT GRADING / IMPORT LEDGER   (paper57 no-go, paper6 Theorem G)")
print(l)
dimless_fluct = 1 / mp.sqrt(N)                 # deltaLambda * l_p^2  (weight 0)
print("deltaLambda * l_p^2 = 1/sqrt(N) = 10^%s   [ROBUST weight-0 pure number]" %
      mp.nstr(mp.log10(dimless_fluct), 8))
print("|deltaLambda|_absolute = (1/l_p^2)/sqrt(N)        [IMPORT-gated weight-(-2)]")
print("""
LEDGER  (what is ROBUST vs what is IMPORT):
  SCALING exponent  -1/2 of zero-mean std .......... [ROBUST]  (structural, sympy)
  spacetime dim d = 4 in V = R_H^4 ................. [ROBUST]  (sympy, forces d=4)
  de Sitter Lambda_obs ~ R_H^(-2) .................. [ROBUST]  (sympy exponent -2)
  weight-0 ratio  deltaLambda*l_p^2 = 1/sqrt(N) .... [ROBUST]  (no-go-ALLOWED)
  ------------------------------------------------------------------------------
  MAGNITUDE 10^(-121.86):
    l_step = Planck (the 1/l_p^2 absolute unit) ..... [IMPORT-1]  (doubly-gated)
    cosmic count N ~ 10^240 (= V/l_p^4) ............. [IMPORT-2]  (triply-gated)
    H0 measured -> R_H = c/H0 (the one length) ...... [IMPORT-3]
  => |deltaLambda|_physical is weight-(-2) -> GATED on all three IMPORTS.

VERDICT: SHARD REPRODUCES the Sorkin numerology, it does NOT improve it.
  10^(-120) is algebraically  (R_H/l_p)^(-2),  ONE measured ratio (R_H/l_p~10^60).
  The records are ELIGIBLE to carry the weight-0 ratio 1/sqrt(N); the absolute
  magnitude is import-gated, exactly as paper57's scale no-go demands.
""")

# =====================================================================
# 8. SUMMARY
# =====================================================================
print(L)
npass = sum(1 for _, ok in CHECKS if ok)
ntot = len(CHECKS)
print("CHECKS:  %d / %d PASS" % (npass, ntot))
for lab, ok in CHECKS:
    print("   [%s] %s" % ("PASS" if ok else "FAIL", lab))
print(l)
print("KEY NUMBERS (Planck units):")
print("  R_H / l_p                 = 10^%s   [IMPORT-3]   (the one ratio)" % mp.nstr(log10_Lr, 7))
print("  cosmic 4-volume N         = 10^%s   [IMPORT-2]" % mp.nstr(log10_N, 7))
print("  deltaLambda = 1/sqrt(N)   = 10^%s   [IMPORT-gated magnitude]" % mp.nstr(log10_dLam, 7))
print("  Lambda_observed           = 10^%s   [IMPORT]" % mp.nstr(log10_Lam_obs, 7))
print("  log10(predicted/observed) = %s   ~ 0  [ROBUST collapse]" % mp.nstr(log10_ratio, 8))
print("  everpresent std exponent  = %s        [ROBUST sympy-exact]" % str(sp.Rational(-1, 2)))
print(L)
if npass == ntot:
    print("ALL CHECKS PASS  (%d/%d).  dps = %d." % (npass, ntot, mp.mp.dps))
else:
    print("SOME CHECKS FAILED  (%d/%d)." % (npass, ntot))
print(L)
