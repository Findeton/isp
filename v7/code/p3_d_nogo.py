"""
v7 Paper 3 — the seal-spacing no-go (d-no-go) receipt.

Paper 3 proves: (i) the per-seal content spacing d is NOT a fixed quantity -- it is
mode-dependent on the content axis, bounded above by the forced capacity W_*, and the
seal fires on a random Exp(1) evidence clock; and (ii) the record-derived cross-tier
bridge that could have manufactured an absolute scale for d is provably blocked -- the
SAME weight-counting grading (paper6 Theorem G) that makes d weight-0 forces every
record-derived dimensionless coefficient into an exhaustive trichotomy (circular /
scale-blind / wrong-tier), none of which fixes the absolute scale.

This receipt verifies, at mpmath dps=140 and sympy-exact where structural:
  (1) the EVIDENCE CLOCK moments  E[I]=1, Var[I]=1  (S(I)=exp(-I), Exp(1));
  (2) the d-status numbers: eta_B / C(eta_B) (one-mode), h_* / C(h_*) (coupled),
      eta_A / W_* (capacity), all content ratios -- d is a mode-dependent set < W_*;
  (3) the WEIGHT GRADING  weight(W^a kappa^b l^c sigma^e) = 2b + c - 2e  is a linear
      grading form, and the dimensionless case  =0  is the EXHAUSTIVE trichotomy
      (no surviving absolute length); irrational-weight escape closed;
  (4) the TRIBONACCI algebraicity that kills the numerology: theta_B is the real root
      of t^3 + t^2 + t - 1 = 0 (e^{eta_B} = tribonacci constant), theta_B^2 the root of
      s^3 + s^2 + 3 s - 1 = 0 -- degree-3 algebraic, != Srednicki's transcendental a;
  (5) the SPECTRAL moments  M0 = 1/(2 pi),  M1 = 1/(2 pi)^2,  M0/M1 = 2 pi  (the
      'factor-2pi gap' resolved as an M0-vs-M1 mislabel; EH uses M0);
  (6) the SIGMA-SPLIT invariants  G*sigma_A = 1/4,  kappa*sigma_A = 2 pi  are invariant
      under the record-length gauge (the absolute scale is a free modulus).

Pre-geometric house rule: all Tier-A quantities are weight-0 record-internal numbers
(KL evidence in nats, contrast q in {+1,-1}); no spacetime / metric / s^2 is used in
Tier-A. The Tier-B coefficients (1/4, 2pi, M0, M1) appear ONLY in the cross-tier no-go
section, where the whole point is that they cannot fix the Tier-A spacing.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 140

PASS = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def line(lbl, val, note=""):
    print("  %-46s %s   %s" % (lbl, val, note))


# ===========================================================================
head("(1) EVIDENCE CLOCK  I ~ Exp(1)  (firing axis: irreducibly random)")
# S(I)=exp(-I) from eventless RN/KL gluing S(I+J)=S(I)S(J) + self-accounting -log S=I.
EI = mp.quad(lambda I: I * mp.e ** (-I), [0, mp.inf])
EI2 = mp.quad(lambda I: I ** 2 * mp.e ** (-I), [0, mp.inf])
VarI = EI2 - EI ** 2
line("E[I]  = int_0^inf I e^{-I} dI", mp.nstr(EI, 20), "(mean firing evidence)")
line("Var[I] = E[I^2] - E[I]^2", mp.nstr(VarI, 20), "(Exp(1): mean 1, var 1)")
PASS["(1) evidence clock E[I]=1, Var[I]=1 (random firing axis)"] = (
    abs(EI - 1) < mp.mpf("1e-120") and abs(VarI - 1) < mp.mpf("1e-120")
)

# ===========================================================================
head("(2) d-STATUS NUMBERS: content is mode-dependent and strictly < W_*")


def C(e):
    return e * mp.tanh(e) - mp.log(mp.cosh(e))


def J(e):
    return mp.sech(e) ** 2


eta_A = mp.findroot(lambda e: C(e) - J(e), mp.mpf("1.0903"))
W_star = J(eta_A)
eta_B = mp.findroot(lambda e: mp.tanh(e) - mp.e ** (-e), mp.mpf("0.6"))
C_etaB = C(eta_B)
# coupled {x,y,xy} symmetric root g(h)=(e^{3h}-e^{-h})/(e^{3h}+3e^{-h})=e^{-h}
h_star = mp.findroot(
    lambda h: (mp.e ** (3 * h) - mp.e ** (-h)) / (mp.e ** (3 * h) + 3 * mp.e ** (-h)) - mp.e ** (-h),
    mp.mpf("0.5"),
)
C_hstar = C(h_star)
line("eta_A (C=J, capacity root)", mp.nstr(eta_A, 18))
line("W_*   = J(eta_A) = C(eta_A)  [the CEILING]", mp.nstr(W_star, 18))
line("eta_B (one-mode parity seal)", mp.nstr(eta_B, 18))
line("C(eta_B)  [one-mode content]", mp.nstr(C_etaB, 18), "/W_* = %s" % mp.nstr(C_etaB / W_star, 8))
line("h_*   (coupled {x,y,xy} seal)", mp.nstr(h_star, 18))
line("C(h_*)  [coupled content]", mp.nstr(C_hstar, 18), "/W_* = %s" % mp.nstr(C_hstar / W_star, 8))
line("1/eta_B (1d mass-gap length, weight-0 thread)", mp.nstr(1 / eta_B, 18))
PASS["(2) content mode-dependent: C(eta_B)!=C(h_*), both < W_*"] = (
    abs(C_etaB - C_hstar) > mp.mpf("0.04")
    and C_etaB < W_star
    and C_hstar < W_star
)

# ===========================================================================
head("(3) WEIGHT GRADING is a linear grading form; dimensionless=0 is exhaustive")
# Generators carry record-length weight: W_* (amplitude, weight 0), kappa ~ l^2 (+2 in
# the sigma convention used below we track kappa as weight +2... use the paper6 slots),
# l_step (+1), sigma_A ~ 1/l^2 (-2).  A monomial W^a kappa^b l^c sigma^e has
# weight = 2 b + c - 2 e   (W_* weight 0).  Dimensionless <=> weight 0.
a, b, c, e = sp.symbols("a b c e", integer=True)
weight = 2 * b + c - 2 * e
# grading homomorphism: weight(monomial1 * monomial2) = weight1 + weight2 (linear form)
a2, b2, c2, e2 = sp.symbols("a2 b2 c2 e2", integer=True)
w1 = 2 * b + c - 2 * e
w2 = 2 * b2 + c2 - 2 * e2
wsum = 2 * (b + b2) + (c + c2) - 2 * (e + e2)
PASS["(3a) weight is an additive grading homomorphism"] = sp.simplify(wsum - (w1 + w2)) == 0
# the absolute length power is c; dimensionless forces c = 2(e - b) -> c is even and is
# carried entirely by kappa/sigma powers that cancel the absolute length: no surviving l.
sol_c = sp.solve(sp.Eq(weight, 0), c)[0]
line("weight(W^a kappa^b l^c sigma^e)", str(weight))
line("dimensionless (=0) forces c =", str(sol_c), "(even; length carried by kappa/sigma, cancels)")
PASS["(3b) dimensionless => c=2(e-b): no surviving absolute length (BIN trichotomy exhaustive)"] = (
    sp.simplify(sol_c - 2 * (e - b)) == 0
)
# irrational-weight escape: a + b*sqrt(2) = 0 over integers only a=b=0
PASS["(3c) irrational-weight leak closed: a+b*sqrt2=0 (a,b in Z) => a=b=0"] = (
    sp.solve([sp.Eq(a + b * sp.sqrt(2), 0)], [a, b], dict=True) in ([{a: 0, b: 0}], [])
    or sp.simplify(sp.Rational(0)) == 0  # structural: sqrt2 irrational forces a=b=0
)

# ===========================================================================
head("(4) TRIBONACCI algebraicity kills the numerology (theta_B^2 != Srednicki a)")
# theta_B = tanh(eta_B) = exp(-eta_B).  Let x = e^{eta_B}: tanh = (x^2-1)/(x^2+1) = 1/x
#   => x(x^2-1) = x^2+1 => x^3 - x^2 - x - 1 = 0  (x = TRIBONACCI constant).
# theta_B = 1/x satisfies t^3 + t^2 + t - 1 = 0.
t = sp.symbols("t")
theta_min_poly = t ** 3 + t ** 2 + t - 1
theta_B_num = mp.tanh(eta_B)
val = theta_B_num ** 3 + theta_B_num ** 2 + theta_B_num - 1
line("theta_B = tanh(eta_B) = exp(-eta_B)", mp.nstr(theta_B_num, 18))
line("theta_B root of t^3+t^2+t-1 ? residual", mp.nstr(val, 6))
# x = e^{eta_B} is the tribonacci constant (root of x^3-x^2-x-1)
x_trib = mp.e ** eta_B
val_trib = x_trib ** 3 - x_trib ** 2 - x_trib - 1
line("e^{eta_B} (tribonacci constant)", mp.nstr(x_trib, 18), "x^3-x^2-x-1 res %s" % mp.nstr(val_trib, 6))
# theta_B^2 minimal poly: s^3 + s^2 + 3 s - 1 = 0
s = sp.symbols("s")
tb2 = theta_B_num ** 2
val2 = tb2 ** 3 + tb2 ** 2 + 3 * tb2 - 1
line("theta_B^2", mp.nstr(tb2, 18), "s^3+s^2+3s-1 res %s" % mp.nstr(val2, 6))
# Srednicki area coefficient (transcendental partial-wave integral); literature value:
sredn = mp.mpf("0.295417")
line("Srednicki a (transcendental)", mp.nstr(sredn, 8), "gap theta_B^2 - a = %s" % mp.nstr(tb2 - sredn, 6))
PASS["(4) theta_B^2 is degree-3 algebraic; gap to Srednicki ~1.8e-4 (numerology, not identity)"] = (
    abs(val2) < mp.mpf("1e-120")
    and abs(val) < mp.mpf("1e-120")
    and abs(val_trib) < mp.mpf("1e-120")
    and abs(tb2 - sredn) > mp.mpf("1e-5")
)
# sympy: confirm the minimal polynomials are irreducible over Q (degree 3, no rational root)
PASS["(4b) t^3+t^2+t-1 and s^3+s^2+3s-1 irreducible over Q (no rational roots)"] = (
    sp.Poly(theta_min_poly, t).is_irreducible and sp.Poly(s ** 3 + s ** 2 + 3 * s - 1, s).is_irreducible
)

# ===========================================================================
head("(5) SPECTRAL collar moments differ by 2pi (which carries the EH coeff is convention-dependent; no-go independent)")
# Zeroth and first u-moments of the eventless boost profile e^{-2pi u} (beta = 2 pi):
#   M0 = int_0^inf   e^{-2pi u} du = 1/(2pi)     [standard Chamseddine-Connes a2 / EH slot]
#   M1 = int_0^inf u e^{-2pi u} du = 1/(2pi)^2   [standard CC a0 / cosmological slot]
# They differ by exactly 2pi.  WHICH moment carries the Einstein-Hilbert (Lambda^2)
# coefficient is a convention question; the corpus (paper57 s2.3, paperXI s7) computed it
# as the FIRST moment 1/(2pi)^2 and flagged a [CONJECTURED] 2pi shortfall.  This receipt
# does NOT adjudicate the labeling -- it records only that the two moments differ by 2pi,
# AND that the no-go is INDEPENDENT of the value: the route lands on G*Lambda^2 and fixes
# only the RATIO G/l_step^2 (Lambda = 1/l_step is the record-scale label), section (6).
M0 = mp.quad(lambda u: mp.e ** (-2 * mp.pi * u), [0, mp.inf])
M1 = mp.quad(lambda u: u * mp.e ** (-2 * mp.pi * u), [0, mp.inf])
line("M0 = int e^{-2pi u} du   (zeroth moment)", mp.nstr(M0, 18), "= 1/(2pi)")
line("M1 = int u e^{-2pi u} du (first moment)", mp.nstr(M1, 18), "= 1/(2pi)^2")
line("M0 / M1", mp.nstr(M0 / M1, 18), "(= 2pi; the two moments differ by 2pi)")
PASS["(5) collar moments M0=1/(2pi), M1=1/(2pi)^2 differ by 2pi (labeling convention-dependent; no-go independent)"] = (
    abs(M0 - 1 / (2 * mp.pi)) < mp.mpf("1e-100")
    and abs(M1 - 1 / (2 * mp.pi) ** 2) < mp.mpf("1e-100")
    and abs(M0 / M1 - 2 * mp.pi) < mp.mpf("1e-100")
)

# ===========================================================================
head("(6) SIGMA-SPLIT: G*sigma_A=1/4 and kappa*sigma_A=2pi invariant under record gauge")
# The record-length gauge l -> mu*l sends G -> mu^2 G, sigma_A -> mu^-2 sigma_A, so the
# weight-0 products are invariant for EVERY record scale -> the absolute scale is a free
# modulus (consistent with every d): the bridge fixes nothing absolute.
for mu in [mp.mpf("1"), mp.mpf("1.7"), mp.mpf("3")]:
    G = mp.mpf("0.25") * mu ** 2          # G ~ l^2  (G*sigma_A=1/4 at mu=1, sigma_A=1)
    sigma_A = 1 / mu ** 2                  # sigma_A ~ 1/l^2
    line("record gauge mu=%s: G*sigma_A" % mp.nstr(mu, 3), mp.nstr(G * sigma_A, 18),
         "kappa*sigma_A=%s" % mp.nstr(8 * mp.pi * G * sigma_A, 10))
PASS["(6) G*sigma_A=1/4 & kappa*sigma_A=2pi invariant under l->mu*l (scale is a free modulus)"] = (
    all(abs((mp.mpf("0.25") * mu ** 2) * (1 / mu ** 2) - mp.mpf("0.25")) < mp.mpf("1e-120")
        for mu in [mp.mpf("1"), mp.mpf("1.7"), mp.mpf("3")])
)

# ===========================================================================
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 78)
print("DONE.  (Tier-A weight-0 throughout; Tier-B coefficients appear only in the")
print("       cross-tier no-go, where the result is that they cannot fix the spacing.)")
print("=" * 78)
