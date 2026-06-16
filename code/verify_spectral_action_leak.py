"""
The ONE place the corpus flags as conjectural and a hostile reviewer would press:
the Chamseddine-Connes SPECTRAL ACTION route to G.

Spectral action:  Tr f(D/Lambda) ~ ... + (1/(16 pi G)) integral R sqrt(g)  with
  1/(16 pi G) = f_2 * Lambda^2 / (something) ,  f_2 = integral_0^inf u f(u) du
where Lambda is the spectral cutoff (inverse length, weight -1) and f the cutoff
test function.

The corpus' claim (paper57 sec 2):
  (i)  the dimensionless content f_2 is PLAUSIBLY record-intrinsic IF the
       eventless-collar Gibbs profile at beta=2pi is the test function;
  (ii) BUT the naive collar profile e^{-2pi u} gives f_2 = 1/(2pi)^2, not 1/(2pi),
       so the quoted G*Lambda^2 = 3 pi^2 does NOT follow;
  (iii) and CRUCIALLY: even if f_2 is record-intrinsic, the cutoff Lambda is the
       SAME missing label (an inverse length the records can only build as 1/l).

We (A) verify f_2 for the collar profile exactly (sympy + mpmath dps>=80);
   (B) test the LEAK: even granting a record-intrinsic f_2, does Lambda being
       'the spectral cutoff' ever become weight-0?  If Lambda = 1/l (records'
       only inverse length) then G = f_2/Lambda^2 ~ f_2 * l^2 : G is weight +2,
       NOT fixed; if Lambda is an EXTERNAL energy scale E_G (a configuration),
       then G is pinned to the external scale, not to records. Either way no leak.
"""
import sympy as sp
import mpmath as mp

print("="*72)
print("SPECTRAL-ACTION f_2 (the [CONJECTURED] route) - exact check")
print("="*72)

u = sp.symbols('u', positive=True)

# (A) collar Gibbs profile f(u) = e^{-2 pi u} (the proved beta=2pi modular weight)
f_collar = sp.exp(-2*sp.pi*u)
f2_collar = sp.integrate(u*f_collar, (u, 0, sp.oo))
print(f"\n collar profile f(u)=e^(-2pi u):")
print(f"   f_2 = integral_0^inf u e^(-2pi u) du = {sp.simplify(f2_collar)}")
print(f"   = 1/(2pi)^2 = {sp.nsimplify(f2_collar)} -> the corpus' stated value")
# confirm it is NOT 1/(2pi):
is_quarter_pi2 = sp.simplify(f2_collar - 1/(2*sp.pi)**2) == 0
print(f"   equals 1/(2pi)^2 ? {is_quarter_pi2}   (so 'G Lambda^2 = 3 pi^2' does NOT follow)")

# high precision cross-check
mp.mp.dps = 90
f2_num = mp.quad(lambda x: x*mp.e**(-2*mp.pi*x), [0, mp.inf])
print(f"   mpmath dps90: f_2 = {mp.nstr(f2_num,30)}")
print(f"   1/(2pi)^2    = {mp.nstr(1/(2*mp.pi)**2,30)}")
print(f"   diff = {mp.nstr(abs(f2_num - 1/(2*mp.pi)**2),6)}  (machine-zero)")

# What G*Lambda^2 the corpus' often-quoted 3 pi^2 needs vs what the collar gives:
# Chamseddine-Connes: 1/(16 pi G) = f_2 Lambda^2 / (2 pi^2)  (the a_2 normalization)
# => G Lambda^2 = (2 pi^2)/(16 pi f_2) = pi/(8 f_2)
GLam2_collar = sp.simplify(sp.pi/(8*f2_collar))
print(f"\n with CC normalization 1/(16piG)=f_2 Lambda^2/(2pi^2):")
print(f"   G*Lambda^2 = pi/(8 f_2) = {GLam2_collar}  (collar f_2)")
print(f"   the quoted '3 pi^2' requires f_2 = {sp.simplify(sp.pi/(8*3*sp.pi**2))} "
      f"= 1/(24 pi), which the collar does NOT give.")
print("   => the SPECIFIC dimensionless value is NOT pinned by the naive profile.")

# ----------------------------------------------------------------------
# (B) THE LEAK TEST: grant a record-intrinsic f_2. Is Lambda weight-0?
# ----------------------------------------------------------------------
print("\n" + "="*72)
print("LEAK TEST: even with record-intrinsic f_2, can G be fixed?")
print("="*72)
G, Lam, l, f2, cnum = sp.symbols('G Lambda l f_2 c_num', positive=True)
# G = (pi/8) / (f_2 Lambda^2)  (weight of RHS: f_2 weight 0, Lambda weight -1)
G_expr = (sp.pi/8)/(f2*Lam**2)
print(f"\n G = (pi/8)/(f_2 Lambda^2). weight check: f_2(0) + Lambda(-1)*2 = -2")
print(f"   => G has weight +2 (since 1/Lambda^2 is +2). CONSISTENT with G weight +2.")
# Case 1: records' only inverse length, Lambda = c_num/l  (weight -1):
G_case1 = sp.simplify(G_expr.subs(Lam, cnum/l))
l_exp = sp.degree(sp.numer(G_case1), l) - sp.degree(sp.denom(G_case1), l)
print(f"\n CASE 1 (Lambda = c_num/l, records' only inverse length):")
print(f"   G = {G_case1}")
print(f"   residual power of l = {l_exp}  (G ~ l^2 : G is FREE, slides with gauge l)")
print(f"   => even with f_2 record-intrinsic, G is NOT fixed (l is the modulus).")
# Case 2: Lambda = external physical energy scale E_G (e.g. tau_G = hbar/E_G):
EG = sp.Symbol('E_G', positive=True)   # EXTERNAL, weight -1 but NOT a record number
G_case2 = sp.simplify(G_expr.subs(Lam, EG))
print(f"\n CASE 2 (Lambda = external scale E_G, e.g. a lab/Penrose energy):")
print(f"   G = {G_case2}")
print(f"   => G is pinned to the EXTERNAL E_G, not to the records. Not intrinsic.")

print("\n" + "="*72)
print("SPECTRAL-ACTION VERDICT:")
print("  - f_2 dimensionless value is NOT uniquely pinned by the collar profile")
print("    (naive profile gives 1/(2pi)^2, not the value '3 pi^2' needs).")
print("  - EVEN granting a record-intrinsic f_2, the cutoff Lambda is the SAME")
print("    missing inverse-length label: Lambda=1/l => G~l^2 (free, gauge);")
print("    Lambda=external => G pinned to an external scale, not records.")
print("  => NO LEAK. The no-go survives the spectral-action route.")
print("="*72)
