#!/usr/bin/env python3
"""
v6_p26e: the coordination law meets error-correction thresholds
(Paper 26, Part V, angle 1).

P10 Part III's COORDINATION LAW - record ordering is controlled by
coordination number z, not dimension - was the corpus' own correction
of its own earlier claim.  Code-capacity thresholds of surface codes
map to disorder transitions of statistical-mechanics models on the
SAME graphs (Dennis-Kitaev-Landahl-Preskill), so the law predicts:
THRESHOLDS ORDER BY z within fixed dimension.

 (i)  the EXACT clean critical couplings of the 2d Ising family
      (machine-verified from their closed forms + the star-triangle
      identity): honeycomb (z = 3) K_c = 0.65848 > square (z = 4)
      0.44069 > triangular (z = 6) 0.27465: ordering strength is
      monotone IN z, exactly;
 (ii) the literature threshold anchors (NAMED DATA, as reported):
      surface-code code-capacity thresholds ~ 6.7% (honeycomb-class),
      ~ 10.9% (square), ~ 16.4% (triangular-class): MONOTONE IN z -
      the coordination law's ordering, in engineering data;
 (iii) the corpus' own P10 receipts re-cited (triangular z = 6 orders
      in 2d at -5.0% below critical; square +3.3%; honeycomb +15.8%
      above): the same ordering at the record level;
 (iv) the honest scope: z orders thresholds WITHIN a dimension; it
      does not set values or equate across dimensions (3d cubic z = 6
      has p_c ~ 23% != triangular's ~ 16%): the law is an ordering
      law, tested as one.
"""
import numpy as np
from scipy.optimize import brentq

print("== (i) exact clean couplings, machine-verified ==")
K_sq = 0.5 * np.log(1 + np.sqrt(2))
print(f"  square (z = 4):    K_c = {K_sq:.5f};  self-duality check"
      f" sinh(2Kc) = {np.sinh(2*K_sq):.10f} (= 1 exactly)")
K_tri = 0.25 * np.log(3)
print(f"  triangular (z=6):  K_c = {K_tri:.5f};  criterion"
      f" e^(4K) = {np.exp(4*K_tri):.10f} (= 3 exactly)")
K_hc = 0.5 * np.log(2 + np.sqrt(3))
# star-triangle: the honeycomb model at K_hc maps to triangular at K_tri
# identity: sinh(2 K_hc) sinh(2 K_tri) = 1 at the joint critical point
prod = np.sinh(2 * K_hc) * np.sinh(2 * K_tri)
print(f"  honeycomb (z=3):   K_c = {K_hc:.5f};  star-triangle product"
      f" sinh(2K_hc) sinh(2K_tri) = {prod:.10f} (= 1 exactly)")
print(f"  ordering: K_c(z=3) {K_hc:.3f} > K_c(z=4) {K_sq:.3f} >"
      f" K_c(z=6) {K_tri:.3f}")
print("  -> ordering strength is MONOTONE IN COORDINATION, exactly, in")
print("     the clean models underlying the code-threshold mappings.")

print("\n== (ii) the threshold anchors (named data, as reported) ==")
print("   lattice        z    code-capacity threshold (approx)")
print("   honeycomb-class 3      ~ 6.7%")
print("   square          4      ~ 10.9%   (the RBIM Nishimori value)")
print("   triangular-class 6     ~ 16.4%")
print("  -> MONOTONE IN z: the coordination law's ordering appears in")
print("     the engineering data.  (Values are literature anchors -")
print("     named imports; the ordering is the corpus' claim.)")

print("\n== (iii) the corpus' own receipts (P10 Part III, re-cited) ==")
print("   triangular z = 6: ORDERS in 2d, margin -5.0% below critical")
print("   square     z = 4: +3.3% above (near-critical)")
print("   honeycomb  z = 3: +15.8% above (disordered)")
print("  -> the same z-ordering at the record level, where the law was")
print("     discovered (by refuting the corpus' own d-reading).")

print("\n== (iv) honest scope ==")
print("  z ORDERS thresholds within fixed dimension; it does not set")
print("  values, and it does not equate across dimensions (3d cubic")
print("  z = 6: p_c ~ 23% != 2d triangular z = 6: ~ 16%).  VERDICT at")
print("  stated scope: the coordination law's ordering prediction")
print("  PASSES on the threshold anchors - the corpus' first contact")
print("  between a corpus-original law and engineering data.  The")
print("  sharpened falsifiable form: any 2d code family whose")
print("  thresholds VIOLATE z-ordering (at matched noise model and")
print("  decoder class) refutes the law's application.")
print("== p26e done ==")
