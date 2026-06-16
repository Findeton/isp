#!/usr/bin/env python3
"""
SCOUT S-NUMEROLOGY: Sorkin everpresent-Lambda numerology vs SHARD record substrate.

Question: does V ~ cosmic-4-volume -> deltaLambda ~ 1/sqrt(V) reproduce the
OBSERVED Lambda ~ 10^-122 (Planck)? And what is ROBUST (weight-0 scaling)
vs an IMPORT (l_step = Planck, the cosmic N)?

All structural quantities exact / mpmath dps=120. Inputs that are EMPIRICAL or
SCALE-IMPORTS are flagged [IMPORT]. Pure-number / weight-0 results flagged [ROBUST].
"""
import mpmath as mp
mp.mp.dps = 120

print("="*78)
print("SCOUT S-NUMEROLOGY :: Sorkin everpresent-Lambda  ::  dps =", mp.mp.dps)
print("="*78)

# -------------------------------------------------------------------------
# PHYSICAL CONSTANTS (CODATA-ish; these are MEASURED inputs -> [IMPORT])
# We work in Planck units (l_p = t_p = 1) at the end; SI only to anchor.
# -------------------------------------------------------------------------
# Planck length / time (SI)  -- [IMPORT: the scale, = SHARD's l_step IF l_step=Planck]
l_p   = mp.mpf('1.616255e-35')      # m   (Planck length)
t_p   = mp.mpf('5.391247e-44')      # s   (Planck time)
c     = mp.mpf('299792458')         # m/s (exact)

# Cosmology (MEASURED -> [IMPORT])
H0_kmsMpc = mp.mpf('67.4')          # km/s/Mpc  (Planck 2018)
Mpc_m     = mp.mpf('3.0856775814913673e22')  # m
H0 = H0_kmsMpc * mp.mpf('1000') / Mpc_m      # s^-1
print("\n[IMPORT] H0 =", mp.nstr(H0,6), "s^-1")

# Hubble radius and Hubble time
R_H = c / H0          # m   (Hubble radius)
T_H = 1 / H0          # s   (Hubble time)
print("[IMPORT] Hubble radius R_H =", mp.nstr(R_H,6), "m  =", mp.nstr(R_H/l_p,6), "l_p")
print("[IMPORT] Hubble time   T_H =", mp.nstr(T_H,6), "s  =", mp.nstr(T_H/t_p,6), "t_p")

# -------------------------------------------------------------------------
# THE COSMIC 4-VOLUME in Planck units.
# Sorkin's V ~ (spacetime 4-volume of the causal past) ~ R_H^3 * (c*T_H) in
# Planck units, up to O(1) geometric factors. The "number = volume" identity
# (Myrheim-Meyer E[N] = V/l_step^d) makes V (in l_p^4) = N, the seal count.
# We compute several O(1)-factor conventions to show the EXPONENT is robust
# and only the O(1) prefactor / which-radius choice moves the last digit.
# -------------------------------------------------------------------------
print("\n" + "-"*78)
print("COSMIC 4-VOLUME  V  (in Planck units l_p^4 = N seal count)")
print("-"*78)

# dimensionless Planck-unit lengths
Lr = R_H / l_p          # Hubble radius in l_p
Lt = c*T_H / l_p        # Hubble time*c in l_p (= R_H/l_p too since R_H=c/H0)
print("R_H / l_p          =", mp.nstr(Lr, 8), " (= 10^%s)" % mp.nstr(mp.log10(Lr),6))
print("c*T_H / l_p        =", mp.nstr(Lt, 8), " (= 10^%s)" % mp.nstr(mp.log10(Lt),6))

# Convention A: V = (R_H/l_p)^3 * (cT_H/l_p)   [naive box]
V_A = Lr**3 * Lt
# Convention B: V = (R_H/l_p)^4                  [Hubble 4-radius, single length]
V_B = Lr**4
# Convention C: causal-diamond / horizon 4-volume ~ (pi^2/24?) -- we take a
#   representative O(1) factor f to show insensitivity. Use f = pi^2/24 (the
#   1+1 Alexandrov interval volume normalization, illustrative) and f=1.
for name, V in [("A: Lr^3 * Lt", V_A), ("B: Lr^4", V_B)]:
    print("V_%s = %s  (= 10^%s l_p^4)  -> N = %s seals"
          % (name, mp.nstr(V,6), mp.nstr(mp.log10(V),7), mp.nstr(V,4)))

# -------------------------------------------------------------------------
# SORKIN: deltaLambda ~ 1/sqrt(V) = 1/sqrt(N)  (Planck units, l_p=1)
# -------------------------------------------------------------------------
print("\n" + "-"*78)
print("SORKIN PREDICTION  deltaLambda ~ 1/sqrt(V) = 1/sqrt(N)   (Planck units)")
print("-"*78)
for name, V in [("A: Lr^3*Lt", V_A), ("B: Lr^4", V_B)]:
    dLam = 1/mp.sqrt(V)
    print("conv %-12s  sqrt(V) = 10^%s   deltaLambda = 10^%s (Planck)"
          % (name, mp.nstr(mp.log10(mp.sqrt(V)),7), mp.nstr(mp.log10(dLam),7)))

# -------------------------------------------------------------------------
# OBSERVED Lambda for comparison.
# rho_Lambda ~ (2.3e-3 eV)^4  -> Lambda in Planck units.
# Lambda (curvature, units 1/l_p^2 in Planck) = 8 pi G rho_Lambda / c^4 expressed
# dimensionlessly = rho_Lambda / rho_Planck * O(1). Cleanest: Lambda_obs ~ 1/R_H^2
# in length^-2, i.e. in Planck units Lambda_obs ~ (l_p/R_H)^2 = Lr^-2.
# Also the energy-density route:
# -------------------------------------------------------------------------
print("\n" + "-"*78)
print("OBSERVED Lambda  (for comparison)")
print("-"*78)

# Route 1: Lambda ~ 1/R_H^2 (curvature dimension), in Planck units = Lr^-2
Lam_obs_curv = Lr**(-2)
print("Lambda_obs (curvature ~ 1/R_H^2)  = 10^%s (Planck, units 1/l_p^2)"
      % mp.nstr(mp.log10(Lam_obs_curv),7))

# Route 2: dimensionless vacuum energy fraction rho_Lambda/rho_Planck
# rho_Lambda_obs ~ Omega_L * rho_crit ; rho_crit = 3 H0^2 c^2/(8 pi G).
# rho_Planck = c^7/(hbar G^2). The ratio is ~ (H0 t_p)^2 ~ Lr^-2 again.
# So both routes give ~ 10^(-2*log10 Lr). Consistent.
rho_ratio = Lr**(-2)   # ~ (l_p / R_H)^2
print("rho_Lambda/rho_Planck ~ (l_p/R_H)^2 = 10^%s  (dimensionless vac frac)"
      % mp.nstr(mp.log10(rho_ratio),7))

# -------------------------------------------------------------------------
# THE COMPARISON  (Sorkin deltaLambda vs observed Lambda)
# Note: Sorkin's deltaLambda is the curvature-dimension Lambda (1/l_p^2),
# = 1/sqrt(V) with V in l_p^4. The OBSERVED Lambda(curvature) ~ 1/R_H^2.
# -------------------------------------------------------------------------
print("\n" + "="*78)
print("THE HIT?  Sorkin deltaLambda(1/sqrt V)  vs  observed Lambda(1/R_H^2)")
print("="*78)
for name, V in [("A: Lr^3*Lt", V_A), ("B: Lr^4", V_B)]:
    dLam = 1/mp.sqrt(V)                 # curvature units 1/l_p^2
    ratio = dLam / Lam_obs_curv
    print("conv %-12s  deltaLambda=10^%s  Lambda_obs=10^%s  ratio=10^%s"
          % (name, mp.nstr(mp.log10(dLam),6), mp.nstr(mp.log10(Lam_obs_curv),6),
             mp.nstr(mp.log10(ratio),6)))

print("""
KEY IDENTITY (why it works): with V = Lr^4 (conv B, single length R_H),
  deltaLambda = 1/sqrt(V) = 1/sqrt(Lr^4) = Lr^-2 = 1/R_H^2 = Lambda_obs  EXACTLY.
So Sorkin's 1/sqrt(V) collapses ALGEBRAICALLY to 1/R_H^2 when V=R_H^4. The
'10^-120 ~ observed' numerology is the statement sqrt(V)=R_H^2/l_p^2=10^120,
i.e. R_H/l_p = 10^60. This is ONE measured ratio (the universe's size in
Planck units), NOT a derived number.
""")

# -------------------------------------------------------------------------
# WEIGHT ANALYSIS (the no-go reconciliation)
# -------------------------------------------------------------------------
print("="*78)
print("WEIGHT ANALYSIS  (no-go reconciliation, paper57/paper6 Theorem G)")
print("="*78)
print("""
 deltaLambda * l_step^2  =  1/sqrt(N)         <- WEIGHT-0 (pure number, seal count)
 deltaLambda (absolute)  =  (1/l_step^2)/sqrt(N) <- WEIGHT-(-2): needs l_step=Planck IMPORT
 N (= V/l_step^4)         =  weight-0 integer    <- but its VALUE 10^240 is the cosmic IMPORT

 Paper57 no-go bars: absolute weight-(-2) data (Lambda_0's VALUE, sigma_A, G, l_step).
 Paper57 no-go ALLOWS: weight-0 ratios / pure numbers.
 => deltaLambda*l_step^2 ~ 1/sqrt(N) is weight-0  -> NO-GO-ALLOWED (eligible).
 => |deltaLambda|_physical = 10^-122  -> weight-(-2)  -> GATED on l_step=Planck import.
""")
N_A = V_A; N_B = V_B
print("weight-0 fluctuation 1/sqrt(N):  conv B  1/sqrt(N) = 10^%s  (pure number)"
      % mp.nstr(mp.log10(1/mp.sqrt(N_B)),7))
print("  -> this pure number IS the prediction the records are eligible to carry.")
print("  -> its value still needs N (cosmic IMPORT) to be 10^240.")

# -------------------------------------------------------------------------
# What does SHARD ADD beyond Sorkin? (the honest accounting)
# -------------------------------------------------------------------------
print("\n" + "="*78)
print("DOES SHARD ADD ANYTHING, OR JUST REPRODUCE SORKIN?")
print("="*78)
print("""
 Reproduces (identical to Sorkin): N=V Myrheim-Meyer (companion-D r2), Poisson
   Var/E=0.97 (companion-D r2), unimodular conjugacy deltaLambda*deltaV~G
   (paper57 sec1.5), V=N*l_step^4. The 1/sqrt(V) SCALING and the 10^-120
   numerology are SORKIN'S, reproduced not improved.

 SHARD-NATIVE ADDITIONS (candidate, to be priced by other scouts):
  (1) The corpus has its OWN sourced drift dLambda = 8piG eta (paper42 W2):
      the MEAN drift undersources by 10-17 orders, but if eta (seal flux) is
      Poisson the ACCUMULATED Lambda is a random walk ~sqrt(N_steps) -> a
      SHARD-internal mechanism that would GENERATE the 1/sqrt(V) spread from
      the corpus's own term, not import Sorkin's conjugacy. [route B - other scout]
  (2) The weight-grading (paper6 Theorem G) gives a SHARPER no-go statement
      than Sorkin had: the MEAN is provably un-sourced (weight-(-2)), while the
      FLUCTUATION-in-record-units is weight-0 and eligible. Sorkin asserts the
      everpresent value; SHARD CLASSIFIES which part is structural vs imported.
""")
print("="*78)
print("PRELIMINARY scout receipt complete. dps=%d. All exponents float-safe" % mp.mp.dps)
print("(log10 of measured ratios); structural identities exact.")
print("="*78)
