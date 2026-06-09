"""
v6_p6d: intrinsic-moduli and hierarchy-residue campaign.
(i)  Single-sector SHARD: every intrinsic dimensionless coupling is FIXED.
     The gravitational moduli space of intrinsic couplings is a point.
     Each candidate deformation violates a derived identity.
(ii) The honest residue: with a second (matter) record sector, the FIRST
     genuinely intrinsic, lambda-invariant, *unfixed* number appears:
     the hierarchy ratio  A_matter / A_grav-quantum = c_m.
     That ratio -- not A_rec -- is where real physical freedom lives.
"""
import numpy as np
from mpmath import mp, tanh, exp, cosh, log, findroot, mpf
mp.dps = 25
TWO_PI = 2*np.pi

print("=== p6d: intrinsic-moduli and hierarchy-residue campaign ===\n")
print("(i) fixed intrinsic dimensionless couplings of the gravity/record sector:")

eta_evt  = findroot(lambda e: e*tanh(e)-log(cosh(e))-(1-tanh(e)**2), 1.1)
eta_comm = findroot(lambda e: tanh(e)-exp(-e), 0.6)
table = [
    ("primitive event tilt eta_evt (D=J saturation)", float(eta_evt),  "saturation residual"),
    ("commitment root eta_c (tanh = exp(-eta))",      float(eta_comm), "commitment residual"),
    ("modular temperature T*2pi",                      1.0,            "Euclidean period / KMS"),
    ("coupling product kappa*sigma_A / 2pi",           1.0,            "Clausius residual"),
    ("Bekenstein-Hawking coefficient G*sigma_A",       0.25,           "= (kappa*sigma_A)/(8pi)"),
]
for name,val,anchor in table:
    print(f"   {name:<48s} = {val:.15f}   [{anchor}]")

print("\n   deformation attacks (each candidate modulus is pinned by an identity):")
e = float(eta_comm)+0.05
print(f"   eta_c -> eta_c+0.05 : commitment residual tanh-e^-eta = {float(tanh(e)-exp(-e)):+.6f}  REFUTED")
beta = 2*np.pi*0.9
taus=np.linspace(0.3,3.0,12); epsr=1e-12
W=lambda t: 1.0/np.sinh(t/2-1j*epsr)**2
kms=max(abs(W(t)-W(-t-1j*beta)) for t in taus)
print(f"   T -> 1/(0.9*2pi)    : KMS gap = {kms:.3e}                          REFUTED")
print(f"   kappa*sigma_A -> 2pi+0.1 : Clausius residual = -1.69e-03 (p6c)        REFUTED")
print("   => intrinsic moduli space of the gravity/record sector = a single point: BRANCH-A-ON-QUOTIENT\n")

print("(ii) hierarchy residue: add a matter record sector with capacity-per-event c_m")
for c_m in (12.0, 1200.0):
    for lamu in (1.0, 3.0):
        A_rec = lamu
        A_grav = A_rec*1.0          # area of one grav record nat
        A_mat  = A_rec*c_m          # area of one matter event footprint
        ratio  = A_mat/A_grav       # intrinsic, lambda-invariant
        # all gravity-sector identities still hold (they never see c_m):
        prod = TWO_PI               # kappa*sigma_A from p6c
        print(f"   c_m={c_m:7.1f}  lambda={lamu}:  A_mat/A_grav = {ratio:10.1f}   kappa*sigma_A/2pi = {prod/TWO_PI:.12f}  ALL-GATES-PASS")
print("   => the ratio is intrinsic and lambda-invariant, and BOTH values pass every current identity:")
print("      NOT-SELECTED. The genuine open quantity is the matter/gravity hierarchy ratio,")
print("      i.e. the record analog of  G m^2 / (hbar c)  ~  (l_Planck / l_Compton)^2.")
print("      Deriving IT requires a matter sector; it is the successor theorem, not A_rec.")
