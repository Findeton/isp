"""
FILTER 3 -- SELF-CONSISTENCY UNDER REFINEMENT.  v7 Long March, Paper 1, Tier A.

This is the SHARD-native closer: the pre-geometric record CLICK-LAW constrained by
the refinement fixed point.  Records ONLY.  No spacetime, no Lorentz invariance,
no light cone, no metric interval s^2.  The only "time" is the COMMIT ORDER (the
succession of seals).

PART 1 (machinery validation).  Reproduce the ONE-DIAMOND constants
    eta_* = 1.090344354879492,  theta_* = 0.797003794162878,  W_* = 0.364784952089976
from the KL=Fisher self-consistency condition (paper4 s5):
      D(P_eta || mu_D)  =  Var_{P_eta}(q) = J(eta),
i.e.    eta tanh eta - log cosh eta  =  1 - tanh^2 eta.
sympy-exact structure + mpmath dps>=100 root.

PART 2 (the extension).  TWO-DIAMOND SEALING DYNAMICS.  Given one sealed diamond,
the law for WHEN/WHETHER the NEXT diamond seals.  Built from paper4's retained-
holonomy LINEAR composition + screen-isometry (the q=2 packet) and the Gell-Mann--
Hartle decoherence-functional bridge (paper56 s4.2):
   a SEAL = a point where the decoherence functional D(alpha,alpha') DIAGONALIZES
   (medium decoherence) <=> Chapman-Kolmogorov composes across it <=> it is a
   REFINEMENT point of the seal order.  "Inserting an intermediate diamond must
   compose consistently."

PART 3 (the decisive question).  Does two-diamond refinement-consistency FORCE the
SHAPE of the seal-rate functional?  We derive the functional relation the survival
content / hazard MUST satisfy, and state EXACTLY what is forced and what is free
(modulo the one no-go scale).

PART 4 (recovery limits).  Constant-hazard (exponential) and accumulating-hazard
(Gaussian-onset) as solutions of the SAME self-consistent law -- does the
refinement condition pick one out, or admit both?

HIGH PRECISION throughout: mpmath mp.dps = 120, sympy-exact where exact.
Pre-geometric: every quantity below is a record-internal pure number (the
accumulated holonomy content chi is a KL divergence, weight-0; the commit order
is the only succession).  No length, no proper time, no s^2 ever appears.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 120

QUOTED_ETA   = mp.mpf("1.090344354879492")
QUOTED_THETA = mp.mpf("0.797003794162878")
QUOTED_W     = mp.mpf("0.364784952089976")


def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


def line(label, val, extra=""):
    print(f"  {label:<50} {val} {extra}")


# ===========================================================================
head("PART 1.  ONE-DIAMOND CONSTANTS from KL=Fisher self-consistency (paper4 s5)")
# ===========================================================================
print("""
  Single-diamond law (paper4 s5): the idempotent contrast q in {-1,+1} carries the
  exponential tilt of the count-dual eventless base mu_D=(1/2,1/2):

        P_eta(q) = e^{eta q} / (2 cosh eta).

  KL content of the committed event vs its eventless repair Pi_0 P_eta = mu_D:
        D(P_eta || mu_D) = eta tanh eta - log cosh eta.       (= eta E[q] - psi)
  Fisher capacity of the same holonomy contrast (log-partition Hessian):
        J(eta) = Var_{P_eta}(q) = d^2 psi/d eta^2 = 1 - tanh^2 eta.

  SELF-CONSISTENCY PRINCIPLE (the independent law, NOT an FDT identity):
        KL content accumulated  ==  Fisher capacity of the contrast
        D(P_eta || mu_D) = J(eta)
  <=>   eta tanh eta - log cosh eta  =  1 - tanh^2 eta.
""")

# -- sympy-exact construction of the two sides -------------------------------
eta = sp.symbols('eta', positive=True)
psi = sp.log(2*sp.cosh(eta)) - sp.log(2)              # log partition (mu-relative)
Eq_mean = sp.tanh(eta)                                 # E_eta[q] = psi'
KL = eta*sp.tanh(eta) - sp.log(sp.cosh(eta))           # D(P_eta || mu)
J = sp.diff(psi, eta, 2)                                # Fisher = psi''
J_simpl = sp.simplify(J)
line("psi(eta) = log(2 cosh eta) - log 2", "")
line("E_eta[q] = psi'(eta)", sp.simplify(sp.diff(psi, eta)))
line("D(P_eta||mu) = eta tanh eta - log cosh eta", "(KL content)")
line("J(eta) = psi''(eta) = Var(q)", J_simpl, "(Fisher capacity)")
# confirm the FDT relation d E[q]/d eta = Var(q) (automatic, NOT the principle)
fdt = sp.simplify(sp.diff(Eq_mean, eta) - J_simpl)
line("FDT check  d E[q]/d eta - Var(q)", fdt, "(0 = automatic; NOT the principle)")

# -- the self-consistency equation and its high-precision root ---------------
def balance(x):
    x = mp.mpf(x)
    th = mp.tanh(x)
    return x*th - mp.log(mp.cosh(x)) - (1 - th**2)

# bracket and solve to full precision
eta_star = mp.findroot(balance, mp.mpf("1.09"))
theta_star = mp.tanh(eta_star)
W_star = 1 - theta_star**2          # = J(eta_*) = Var = the saturated content
# cross-check W_star also equals the KL at the root
W_star_kl = eta_star*theta_star - mp.log(mp.cosh(eta_star))

print()
line("eta_*   (root of balance)", mp.nstr(eta_star, 40))
line("theta_* = tanh eta_*", mp.nstr(theta_star, 40))
line("W_* = J_* = 1 - tanh^2 eta_*", mp.nstr(W_star, 40))
line("W_* via KL (independent formula)", mp.nstr(W_star_kl, 40))
line("residual  balance(eta_*)", mp.nstr(balance(eta_star), 6))
line("residual  W_*(Fisher) - W_*(KL)", mp.nstr(W_star - W_star_kl, 6))

print()
print("  -- comparison to quoted digits --")
line("eta_* - quoted",   mp.nstr(eta_star - QUOTED_ETA, 6))
line("theta_* - quoted", mp.nstr(theta_star - QUOTED_THETA, 6))
line("W_* - quoted",     mp.nstr(W_star - QUOTED_W, 6))

ok1 = (abs(eta_star - QUOTED_ETA) < mp.mpf("1e-15")
       and abs(theta_star - QUOTED_THETA) < mp.mpf("1e-15")
       and abs(W_star - QUOTED_W) < mp.mpf("1e-15"))
line("PART 1 reproduces the quoted constants to <1e-15 ?", ok1)

# uniqueness of the nonzero root (eta=0 is the trivial degenerate solution)
b0 = balance(mp.mpf("0"))   # = -(1) at eta=0 -> KL=0, J=1 -> balance=-1 <0
line("balance(0) (eta=0 is the degenerate branch)", mp.nstr(b0, 6),
     "(<0: no nonzero-content event)")
# show balance crosses zero exactly once for eta>0 by scanning sign
scan = [balance(mp.mpf(k)/10) for k in range(1, 30)]
signchanges = sum(1 for i in range(len(scan)-1) if scan[i]*scan[i+1] < 0)
line("sign changes of balance on (0,3]", signchanges, "(unique nonzero root)")


# ===========================================================================
head("PART 2.  TWO-DIAMOND SEALING: refinement-consistency setup (pre-geometric)")
# ===========================================================================
print("""
  Object: one sealed diamond D1 has committed (eta_*, theta_*, W_* fixed).  The
  question is the law for the NEXT seal D2.  Between D1 and D2 the record carries
  an UNSEALED retained holonomy (paper4 s8: linear retained-holonomy composition,
  amplitudes add c0, c1=e^{i phi} c0; the q=2 screen-isometry packet).  No seal
  has committed the relative phase yet.

  DECOHERENCE-FUNCTIONAL BRIDGE (paper56 s4.2, the Tier-1 functor at kinematic
  level).  Coarse-grain the inter-seal history into record/pointer alternatives
  alpha=(a_1,...,a_n).  The Gell-Mann--Hartle decoherence functional is

      D(alpha, alpha') = Tr[ P_{a_n}...P_{a_1} rho P_{a'_1}...P_{a'_n} ]

  with projectors evolved by the inter-seal holonomy U_k.  A SEAL is the place
  where D DIAGONALIZES (medium decoherence: off-diagonal interference -> 0).  The
  biconditional (a THEOREM of consistent-histories consistency):

     Chapman-Kolmogorov composes across t'  (Gamma(t2,t0)=Gamma(t2,t')Gamma(t',t0))
       <=>  off-diagonal (interference) part of D vanishes at t'  (medium decoherence)
       <=>  t' is a SEAL (a refinement point of the seal order).

  This is EXACTLY the self-consistency-under-refinement condition for sealing:
  "inserting an intermediate diamond must compose consistently" = "the inserted
  point is a place where D is diagonal" = "Chapman-Kolmogorov holds there".

  The record-internal state variable is the ACCUMULATED HOLONOMY CONTENT
      chi  =  total committed entropy content along the commit order
           =  int (rate of D(P_AB||P_BA) accrual)        (paper10 T2; F4 sibling)
  a weight-0 PURE NUMBER (a KL divergence), NOT a length or a proper time.  The
  SURVIVAL functional of the unsealed coherence between seals is
      S(chi)  =  |off-diagonal of D|  =  |retained holonomy overlap|  in [0,1],
  with S(0)=1 (no content committed yet => fully coherent => fully refinable) and
  S decreasing in chi (committing content seals the holonomy).  The SEAL-RATE /
  hazard functional is the chi-derivative of -log S:
      lambda(chi) := -d log S / d chi      (the seal hazard per unit content).
""")

# ---------------------------------------------------------------------------
head("PART 2b.  THE REFINEMENT-COMPOSITION CONSTRAINT (Chapman-Kolmogorov on S)")
# ---------------------------------------------------------------------------
print("""
  Insert an intermediate diamond D' splitting the content interval chi = chi1 + chi2
  (chi1 = D1->D', chi2 = D'->D2).  Self-consistency under refinement DEMANDS:
  inserting the intermediate seal must COMPOSE -- the diagonalized decoherence
  functional must factor through the intermediate diagonal record.  In transition-
  matrix language (paper56 s4.2) this is Chapman-Kolmogorov:

      Gamma(chi1+chi2)  =  Gamma(chi2) . Gamma(chi1)      across the inserted seal.

  On the surviving OFF-DIAGONAL coherence content the composed contraction is the
  product of the two sub-contractions (the cross-terms vanish at the inserted
  diagonal point -- that is what "it is a seal" means).  Hence on S:

      S(chi1 + chi2)  =  S(chi1) . S(chi2)        for ALL chi1, chi2 >= 0.    (*)

  (*) is the Cauchy MULTIPLICATIVE functional equation.  With S(0)=1, S in [0,1]
  monotone (and measurable -- S is a physical contraction), the ONLY solutions are

      S(chi) = exp(- kappa chi),     kappa >= 0  a constant.

  Therefore the SEAL HAZARD PER UNIT CONTENT is FORCED CONSTANT in chi:
      lambda(chi) = -d log S/d chi = kappa = const.
  The seal law is LINEAR-IN-CONTENT: the committed entropy content seals the
  holonomy at a CONSTANT rate per unit content.  This is the Tier-A click-law
  SHAPE, and it is forced up to the one constant kappa (the no-go scale).
""")

# Verify the Cauchy multiplicative equation forces the exponential (sympy).
chi, chi1, chi2, kappa = sp.symbols('chi chi1 chi2 kappa', nonnegative=True)
S = sp.Function('S')
# differentiate S(x+y)=S(x)S(y) wrt y at y=0:  S'(x) = S(x) S'(0)  => S=exp(S'(0) x)
# show the exponential satisfies (*) exactly, and that it is the unique smooth sol.
S_exp = sp.exp(-kappa*chi)
lhs = S_exp.subs(chi, chi1+chi2)
rhs = S_exp.subs(chi, chi1) * S_exp.subs(chi, chi2)
resid_cauchy = sp.simplify(lhs - rhs)
line("S=exp(-kappa chi) satisfies S(x+y)=S(x)S(y) ? residual", resid_cauchy)
# the hazard is the constant kappa
hazard = sp.simplify(-sp.diff(sp.log(S_exp), chi))
line("lambda(chi) = -d log S/d chi", hazard, "(CONSTANT in content chi -- FORCED)")
# uniqueness: any S solving (*) with S(0)=1 has log S additive -> linear -> exp
g = sp.Function('g')
print("  uniqueness: g:=log S satisfies g(x+y)=g(x)+g(y) (Cauchy additive);")
print("  with monotone/measurable S the only solution is g(chi) = -kappa chi.")

# numeric demonstration at high precision: a non-multiplicative survival law
# FAILS the refinement composition, an exponential one PASSES, for arbitrary split.
def S_good(c, k):   # exponential -- refinement-consistent
    return mp.e**(-mp.mpf(k)*mp.mpf(c))
def S_bad(c, k):    # gaussian-in-content -- NOT refinement-consistent in chi
    return mp.e**(-mp.mpf(k)*mp.mpf(c)**2)
k = mp.mpf("0.4")
c1, c2 = mp.mpf("0.3"), mp.mpf("0.55")
good_gap = S_good(c1+c2, k) - S_good(c1, k)*S_good(c2, k)
bad_gap  = S_bad(c1+c2, k)  - S_bad(c1, k)*S_bad(c2, k)
print()
line("EXP survival  S(c1+c2)-S(c1)S(c2)", mp.nstr(good_gap, 6), "(=0: refinement-consistent)")
line("GAUSS-in-chi  S(c1+c2)-S(c1)S(c2)", mp.nstr(bad_gap, 6), "(!=0: FAILS refinement in chi)")


# ===========================================================================
head("PART 3.  WHAT IS FORCED vs FREE  (the decisive question, honest)")
# ===========================================================================
print("""
  FORCED by two-diamond refinement-consistency (Tier-A click-law SHAPE):

  [FORCED-1]  The survival content is MULTIPLICATIVE in the accumulated holonomy
              content chi:  S(chi1+chi2)=S(chi1)S(chi2)  =>  S = exp(-kappa chi).
              Equivalently the seal hazard PER UNIT CONTENT is CONSTANT:
              lambda(chi) = kappa.  The whole-history seal law is the constant-
              hazard-in-content (Poisson-in-content) law.  This is the unique
              self-consistent SHAPE: it is forced, not chosen.

  [FORCED-2]  Monotonicity:  kappa >= 0  (a committed seal can only CONTRACT the
              unsealed holonomy -- S non-increasing).  This is the same
              seal-irreversibility / CP-divisibility floor the F4 sibling found:
              int K >= 0  <=>  lambda >= 0  <=>  no revivals.  Refinement-
              consistency in content and CP-divisibility are the SAME condition.

  [FORCED-3]  Additivity of content over independent composition: chi(D1 x D2)=
              chi(D1)+chi(D2) (paper4 s34: A_{D1xD2}=A_{D1}+A_{D2}), consistent
              with (FORCED-1).  The content chi is the RIGHT clock variable; the
              law is local-in-content.

  FREE (modulo nothing record-internal can fix it -- the ONE no-go scale):

  [FREE-1]    The single constant kappa.  Refinement fixes the FUNCTIONAL FORM
              (exponential-in-content) but NOT the absolute rate.  kappa is the
              content->commit-order conversion: how much commit-order "ticks" one
              unit of weight-0 content buys.  This is exactly the F4 / paper-XI
              one-free-scale no-go: chi (a KL divergence) is weight-0 and
              record-internal, but turning it into a RATE needs one unit that the
              records do not carry (do-delete C6).

  [FREE-2 -> RESOLVED]  The chi-PROFILE of the content itself, chi(tau) as a
              function of the *external* parameter the records do NOT see, is NOT
              constrained by Tier A and MUST NOT be (pre-geometric: there is no
              tau).  In the commit-order/content variable chi -- the ONLY intrinsic
              succession -- the hazard is forced constant.  Any non-constant
              hazard 'lambda(tau)' is purely an artifact of a Tier-B reparam
              chi=chi(tau); it carries NO Tier-A content.  See PART 4.

  VERDICT (honest):  F3 FORCES the Tier-A click-law SHAPE in the intrinsic
  content variable -- uniquely, as exp(-kappa chi) / constant-hazard-in-content --
  up to the single no-go scale kappa.  It does NOT, and pre-geometrically MUST
  NOT, force a profile in any external parameter (none exists at Tier A).  This is
  the best possible Tier-A outcome: unique-modulo-one-no-go-scale.
""")

# Make the "forced shape" claim quantitative: among the power-law survival
# family S=exp(-kappa chi^p), ONLY p=1 satisfies refinement multiplicativity.
print("  -- power-law survival family S=exp(-kappa chi^p): which p is refinement-consistent? --")
p = sp.symbols('p', positive=True)
Sp = sp.exp(-kappa*chi**p)
lhsp = Sp.subs(chi, chi1+chi2)
rhsp = Sp.subs(chi, chi1)*Sp.subs(chi, chi2)
# multiplicativity <=> (chi1+chi2)^p = chi1^p + chi2^p for all chi1,chi2 <=> p=1
mult_eq = sp.simplify(sp.log(lhsp) - sp.log(rhsp))   # = -kappa[(c1+c2)^p - c1^p - c2^p]
line("log S(c1+c2) - log S(c1) - log S(c2)", mult_eq)
# evaluate the bracket at a test point for several p; zero only at p=1
for pv in ["0.5", "1.0", "1.5", "2.0"]:
    val = ((c1+c2)**mp.mpf(pv) - c1**mp.mpf(pv) - c2**mp.mpf(pv))
    tag = "  <- REFINEMENT-CONSISTENT (p=1)" if abs(val) < mp.mpf("1e-90") else ""
    line(f"   p={pv}:  (c1+c2)^p - c1^p - c2^p", mp.nstr(val, 12), tag)


# ===========================================================================
head("PART 4.  RECOVERY LIMITS -- does self-consistency pick exp or gauss?")
# ===========================================================================
print("""
  The corpus knows two seal-hazard regimes (paper56, F4):
    (A) CONSTANT hazard lambda_0  ->  exponential coherence   |rho01| = e^{-lambda_0 T}
    (B) RAMP hazard a t           ->  Gaussian onset          |rho01| = e^{-a T^2/2}
  where T is an EXTERNAL (Tier-B) commit-order parameter.  The Tier-A law forced a
  CONSTANT hazard in the INTRINSIC content variable chi:  S = e^{-kappa chi}.
  The two regimes are then NOT two different Tier-A laws -- they are the SAME
  Tier-A law read through two different Tier-B content profiles chi(T):
""")

T, a, lam0, kap = sp.symbols('T a lambda_0 kappa', positive=True)

# (A) exponential: chi(T) linear in T  <=> content accrues at constant external rate
chi_A = lam0/kap * T                       # so that kappa*chi_A = lam0 T
SA = sp.exp(-kap*chi_A)
line("(A) profile chi(T)=lambda_0 T/kappa  => S=e^{-kappa chi}", sp.simplify(SA),
     "= e^{-lambda_0 T}  EXPONENTIAL")
assert sp.simplify(SA - sp.exp(-lam0*T)) == 0

# (B) gaussian-onset: chi(T) QUADRATIC in T  <=> content accrues at a LINEARLY
#     RAMPING external rate d chi/dT ~ T (the F4 'fixed arrow acceleration')
chi_B = a/(2*kap) * T**2                    # so that kappa*chi_B = a T^2/2
SB = sp.exp(-kap*chi_B)
line("(B) profile chi(T)=a T^2/(2 kappa)  => S=e^{-kappa chi}", sp.simplify(SB),
     "= e^{-a T^2/2}  GAUSSIAN ONSET")
assert sp.simplify(SB - sp.exp(-a*T**2/2)) == 0

print("""
  So the constant-hazard (exponential) and accumulating-hazard (Gaussian-onset)
  cases are BOTH self-consistent: they are ONE Tier-A law (constant hazard in chi,
  S=e^{-kappa chi}) composed with two Tier-B content PROFILES chi(T):
       chi(T) linear     -> exponential   (content accrues at constant rate)
       chi(T) quadratic   -> Gaussian onset (content accrues at a ramping rate).
  REFINEMENT-CONSISTENCY DOES NOT PICK ONE OUT.  It cannot: the profile chi(T)
  lives in T, an external (Tier-B) parameter the records do not carry, and Tier A
  is pre-geometric (there is no T).  What Tier A DOES force is the SHAPE in chi:
  constant hazard per unit content, monotone (kappa>=0).  The 'choice' between
  exponential and Gaussian is the Tier-B choice of how content is laid down along
  an emergent parameter -- exactly the F4 result (the toys are constraint choices
  on the profile), now seen as ONE forced Tier-A law under reparametrization.
""")

# high-precision numeric receipt: both profiles, same Tier-A S(chi), verified
mp.mp.dps = 120
kap_n = mp.mpf("0.7"); lam0_n = mp.mpf("0.45"); a_n = mp.mpf("0.9")
for Tn in [mp.mpf("0.5"), mp.mpf("1.3"), mp.mpf("2.7")]:
    chiA = lam0_n/kap_n*Tn
    chiB = a_n/(2*kap_n)*Tn**2
    SA_n = mp.e**(-kap_n*chiA);  expo = mp.e**(-lam0_n*Tn)
    SB_n = mp.e**(-kap_n*chiB);  gaus = mp.e**(-a_n*Tn**2/2)
    line(f"T={float(Tn)}: |S_A - e^-lam0 T|", mp.nstr(abs(SA_n-expo), 6))
    line(f"T={float(Tn)}: |S_B - e^-aT^2/2|", mp.nstr(abs(SB_n-gaus), 6))

# CP-divisibility / refinement-monotonicity gate (Tier A): kappa>=0 forces
# monotone S -- the no-revival floor, identical to the F4 running-integral gate.
print()
line("Tier-A monotonicity gate: kappa>=0 forces S non-increasing", "(no revival)",
     "= F4 int K>=0 = CP-divisible")
print("""
  A revival (S increasing on a sub-interval) would mean S(chi1+chi2) > S(chi1)S(chi2)
  for some split, i.e. a FAILURE of refinement-multiplicativity (*) -- inserting an
  intermediate seal would not compose.  So at Tier A a revival is exactly an
  unrefinable, non-composing inserted point: NOT a seal.  Refinement-consistency
  therefore re-derives the F4 / paper56 no-revival no-go as a structural Tier-A
  statement, with NO appeal to geometry, spectra, or s^2.
""")


# ===========================================================================
head("CANONICAL OUTPUT BLOCK  (F3 self-consistency receipt)")
# ===========================================================================
print(f"""
  one-diamond constants (reproduced, dps=120):
    eta_*   = {mp.nstr(eta_star, 25)}
    theta_* = {mp.nstr(theta_star, 25)}
    W_*=J_* = {mp.nstr(W_star, 25)}
    residual |balance(eta_*)|          = {mp.nstr(abs(balance(eta_star)), 4)}
    residual |W_Fisher - W_KL|         = {mp.nstr(abs(W_star - W_star_kl), 4)}
    max |const - quoted|               = {mp.nstr(max(abs(eta_star-QUOTED_ETA),
                                                      abs(theta_star-QUOTED_THETA),
                                                      abs(W_star-QUOTED_W)), 4)}

  two-diamond refinement-consistency:
    constraint  S(chi1+chi2) = S(chi1) S(chi2)   (Chapman-Kolmogorov / D diagonalizes)
    FORCED      S(chi) = exp(-kappa chi),  hazard lambda(chi) = kappa = const-in-content
    FORCED      kappa >= 0  (monotone / CP-divisible / no-revival)
    UNIQUE p    only p=1 in S=exp(-kappa chi^p) is refinement-consistent
    FREE        the single scale kappa (one no-go scale; chi is weight-0)

  recovery limits (both are ONE Tier-A law under a Tier-B profile chi(T)):
    chi(T) linear     -> S=e^{{-lambda_0 T}}   exponential      (residuals ~ 0)
    chi(T) quadratic  -> S=e^{{-a T^2/2}}      Gaussian onset   (residuals ~ 0)
    refinement does NOT pick one: the profile is Tier-B; Tier-A forces only the
    constant-hazard-in-chi SHAPE.

  STATUS: F3 FORCES the Tier-A click-law SHAPE (constant hazard in the intrinsic
  holonomy-content variable, S=exp(-kappa chi)) UNIQUELY up to the one no-go scale
  kappa.  Pre-geometric throughout: chi is a record-internal KL pure number; no
  spacetime, metric, light cone, or s^2 was used.  The open Tier-A residue is the
  single scale kappa (provably record-free) and -- pushed upstream by paper4 s34-42
  -- the intrinsic supply of the content rate d chi (the complete closed-holonomy
  cochain), which sets chi but not its commit-order conversion kappa.
""")

head("DONE.")
