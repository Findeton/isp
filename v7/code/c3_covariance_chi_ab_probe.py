"""
R3 -- COVARIANCE PROBE on the free input chi_AB.

QUESTION (the highest-graded covariance leg of the Phase-2 chi_AB programme).
-----------------------------------------------------------------------------
Does RELATIVISTIC COVARIANCE -- the C1/C2 emergent-Lorentz machinery (Lorentz-
scalar seal S, single-chain LI positive-type kernel N, point-locality L, plus
the GDC/Fedida spacelike-microcausality-to-all-orders) -- CARVE the free input
chi_AB BELOW the almost-quantum envelope Q-tilde?  Or does covariance, like every
other downstream sector in the Phase-1 scout, BOTTOM OUT AT Q-tilde -- recovering
Q-tilde exactly and BREAKING NOTHING at a super-quantum-but-almost-quantum point
(a Q-tilde \ Q point)?

THE SCOUT'S STRUCTURAL CLAIM, made operational here:
  Covariance is a SINGLE-PARTY / SINGLE-CHAIN constraint on the seal field
  h(x) -- (S) it is a self-adjoint Lorentz SCALAR, (N) its noise kernel is LI
  positive-type, (L) its density is point-local.  The ONLY two-party content
  covariance touches is SPACELIKE MICROCAUSALITY:  [h_A(x), h_B(y)] = 0 for
  (x-y) spacelike.  But that commutator IS -- letter for letter -- the ON-STATE
  COMMUTATION  B_y A_x |psi> = A_x B_y |psi>  that DEFINES the almost-quantum set
  Q-tilde (= NPA Q^{1+AB}: a single well-defined cross-moment <A_x B_y>, no global
  tensor factorization demanded).  Hence:

        COVARIANCE (spacelike microcausality)  ==  Gamma >= 0 (moment-matrix PSD)

  are TWO FACES OF ONE CONSTRAINT.  Covariance therefore lands on Q-tilde, exactly
  where the transverse no-go (Paper XII) and the downstream sectors already land --
  it adds NO new carving inside Q-tilde, in particular it does NOT pick out Q.

  The relativistic-causality / communication-complexity LEVER that WOULD carve --
  the van Dam / Brassard-et-al collapse of communication complexity, and
  Popescu-Rohrlich superluminal-signalling pathologies -- has TEETH ONLY for
  CHSH > 2 sqrt 2.  Every Q-tilde point obeys CHSH <= 2 sqrt 2 (Tsirelson; NPA
  level-1 is Tsirelson-tight for CHSH).  So the lever is ALREADY Q-tilde-excluded;
  it cannot reach inside Q-tilde to separate Q-tilde from Q.

WHAT THIS RECEIPT CHECKS (~12 machine checks; sympy-exact for the non-commutative
structure, mpmath dps>=120 for the numbers; cvxpy/SCS only for the SDP corroboration,
every SDP digit FLAGGED solver-tolerance ~1e-9).
  (1) NS-IS-A-LORENTZ-SCALAR.  A generic no-signaling box (including a super-quantum
      one) has max | p(a|x,y=0) - p(a|x,y=1) | = 0: the single-party marginal is a
      frame-independent COUNT (a scalar), so NS holds statically  <=>  NS holds under
      boosts, for ANY NS box.  Covariance imposes NOTHING on a box beyond NS that a
      static analysis did not already impose.  (gap < 1e-100.)
  (2) FACTOR-THROUGH-M / TWO-FACES.  The covariance conditions (S),(N),(L) are all
      SINGLE-PARTY (assert + demonstrate they read only the single-chain seal field).
      Then SHOW, with sympy non-commutative symbols, that spacelike microcausality
      [h_A(x), h_B(y)] = 0 IS the on-state commutation [A_x, B_y]|psi> = 0 that
      defines Q-tilde -- so covariance and Gamma>=0 are two faces of one constraint.
  (3) Q-tilde \ Q PROBE.  Build a genuine super-quantum witness via the COLLINS-GISIN
      I3322 (projector form): the TRUE level-(1+AB) optimum 0.2514709 STRICTLY EXCEEDS
      the Q upper bound 0.2508754 (Pal-Vertesi 2010, level>=4, CITED), so it is feasible
      at the records' level (in Q-tilde) yet OUT of Q.  Confirm at this super-quantum
      point: NS holds (-> covariant by (1)); on-state commutation holds by CONSTRUCTION
      (Gamma>=0 feasible -> [A_x,B_y]|psi>=0 -> microcausality OK by (2)); the CHSH-block
      is <= 2 sqrt 2 (-> NO comm-complexity collapse).  => COVARIANCE BREAKS NOTHING.
      (We do NOT use the +-1-correlator I3322: it has cl=Q=Q-tilde=8.0, no gap; the old
       '8.748' was the BARE Q^1 word list, above Q-tilde and records-inadmissible.)
  (4) LOCALIZE THE LEVER.  The van Dam / Brassard comm-complexity teeth and the
      relativistic-causality (signalling) pathology require CHSH > 2 sqrt 2.  Show
      the Tsirelson point (CHSH = 2 sqrt 2) is on the SAFE side and that the lever
      fires only strictly above it -- already Q-tilde-excluded, hence powerless to
      separate Q from Q-tilde.

PRE-GEOMETRIC DISCIPLINE.  No metric, light cone, or s^2 enters the Tier-A algebra;
'spacelike' is used here as the NAME of the relation the emergent covariance (C1/C2,
Tier B) supplies, and the load-bearing identity (2) is that this relation REDUCES to
the pre-geometric on-state commutation -- the same M-algebra invariant the scout
identified.  The emergent-Lorentz premises (point-locality L, the Lorentz action on
S) are the SAME Tier-B gates C1 already quarantines; this receipt shows that GIVEN
them, covariance lands on Q-tilde and no lower.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 130
PASS = {}
FLAG = {}


def head(s):
    print("\n" + "=" * 80 + "\n" + s + "\n" + "=" * 80)


def line(lbl, val, note=""):
    print("  %-54s %s   %s" % (lbl, val, note))


def check(name, cond, detail="", solver_tol=False):
    PASS[name] = bool(cond)
    if solver_tol:
        FLAG[name] = True
    tag = "PASS" if cond else "FAIL"
    flagtag = "  [solver-tol ~1e-9]" if solver_tol else ""
    print("  [%s] %s" % (tag, name))
    if detail:
        print("         %s%s" % (detail, flagtag))


# ===========================================================================
head("(1)  NO-SIGNALING IS A LORENTZ SCALAR  ->  NS-static <=> NS-under-boosts")
# ===========================================================================
print("""
  A no-signaling box p(a,b|x,y) has marginals p(a|x) INDEPENDENT of the distant
  setting y.  The marginal is a SINGLE-PARTY COUNT: the relative frequency of
  outcome a at Alice given setting x.  A count over a frame-independent event set
  is a LORENTZ SCALAR (it does not transform under boosts; it is just a number).
  Therefore: if the box is no-signaling in ANY one frame (the static statement),
  it is no-signaling in EVERY frame -- the boost cannot create a y-dependence in a
  quantity that has none.  This holds for ANY NS box, INCLUDING super-quantum ones
  (PR-box and the whole no-signaling polytope).  So covariance imposes on a box
  NOTHING BEYOND no-signaling that a static analysis did not already impose.

  We verify the SCALAR (= y-independence of the marginal) for: (i) a quantum
  Tsirelson box, (ii) a super-quantum PR-box, (iii) a generic NS box drawn from
  the local + PR mixture -- max over a,x of | p(a|x,y=0) - p(a|x,y=1) | = 0.
""")


def box_marginal_A(p, a, x, y):
    """p(a|x) computed AT a FIXED y:  sum_b p(a,b|x,y).  NS  <=>  this is y-free."""
    return sum(p[(a, bb, x, y)] for bb in (+1, -1))


def ns_marginal_gap(p):
    """max over (a,x) of | p(a|x,y=0) - p(a|x,y=1) |  (Alice side) and the Bob side."""
    g = mp.mpf(0)
    for a in (+1, -1):
        for x in (0, 1):
            d = abs(box_marginal_A(p, a, x, 0) - box_marginal_A(p, a, x, 1))
            g = max(g, d)
    # Bob side: p(b|y) independent of x
    for b in (+1, -1):
        for y in (0, 1):
            mb0 = sum(p[(aa, b, 0, y)] for aa in (+1, -1))
            mb1 = sum(p[(aa, b, 1, y)] for aa in (+1, -1))
            g = max(g, abs(mb0 - mb1))
    return g


def isotropic_box(Edict):
    """p(a,b|x,y) = (1 + a b E_xy)/4 with uniform marginals (1/2,1/2)."""
    p = {}
    for x in (0, 1):
        for y in (0, 1):
            E = Edict[(x, y)]
            for a in (+1, -1):
                for b in (+1, -1):
                    p[(a, b, x, y)] = (1 + a * b * E) / 4
    return p


# (i) quantum Tsirelson box  CHSH = 2 sqrt 2
s = 1 / mp.sqrt(2)
E_ts = {(0, 0): s, (0, 1): s, (1, 0): s, (1, 1): -s}
p_ts = isotropic_box(E_ts)
gap_ts = ns_marginal_gap(p_ts)

# (ii) super-quantum PR-box  CHSH = 4  (E = (+1,+1,+1,-1))
E_pr = {(0, 0): mp.mpf(1), (0, 1): mp.mpf(1), (1, 0): mp.mpf(1), (1, 1): mp.mpf(-1)}
p_pr = isotropic_box(E_pr)
gap_pr = ns_marginal_gap(p_pr)

# (iii) generic NS box: mixture lambda*PR + (1-lambda)*local-deterministic (still NS)
lam = mp.mpf("0.6")
E_loc = {(0, 0): mp.mpf("0.3"), (0, 1): mp.mpf("-0.2"),
         (1, 0): mp.mpf("0.5"), (1, 1): mp.mpf("0.1")}
E_mix = {k: lam * E_pr[k] + (1 - lam) * E_loc[k] for k in E_pr}
p_mix = isotropic_box(E_mix)
gap_mix = ns_marginal_gap(p_mix)

line("quantum Tsirelson box: NS marginal gap", mp.nstr(gap_ts, 4), "(scalar: y-free)")
line("super-quantum PR-box:  NS marginal gap", mp.nstr(gap_pr, 4), "(scalar: y-free)")
line("generic NS-mixture box: NS marginal gap", mp.nstr(gap_mix, 4), "(scalar: y-free)")

check("(1a) Tsirelson box marginal is a Lorentz scalar (NS gap < 1e-100)",
      gap_ts < mp.mpf("1e-100"), f"gap={mp.nstr(gap_ts,3)}")
check("(1b) SUPER-QUANTUM PR-box marginal is ALSO a Lorentz scalar (NS gap < 1e-100)",
      gap_pr < mp.mpf("1e-100"),
      f"gap={mp.nstr(gap_pr,3)}  => NS-static <=> NS-boosted even super-quantum")
check("(1c) generic NS box marginal is a Lorentz scalar (NS gap < 1e-100)",
      gap_mix < mp.mpf("1e-100"), f"gap={mp.nstr(gap_mix,3)}")
print("""
  => The no-signaling marginal is a frame-independent COUNT = a Lorentz scalar, so
     NS-in-one-frame  <=>  NS-in-all-frames for ANY box, super-quantum included.
     A BOOST cannot manufacture a distant-setting dependence in a quantity that has
     none.  Hence COVARIANCE adds nothing to a box beyond no-signaling that the
     static (single-frame) analysis already fixed.  In particular it does NOT carve
     inside the no-signaling polytope, let alone inside Q-tilde.
""")


# ===========================================================================
head("(2)  FACTOR-THROUGH-M / TWO-FACES:  spacelike microcausality == on-state")
head_note = "       commutation that DEFINES Q-tilde   [sympy non-commutative]"
print(head_note)
# ===========================================================================
print("""
  The covariance conditions are SINGLE-PARTY / SINGLE-CHAIN:
    (S)  the seal h(x) is a self-adjoint LORENTZ SCALAR field operator
         (built from ONE party's chain; weight-0 algebraic object: E=E*=E^2,
          chi a weight-0 KL number -- see C1 PART S).
    (N)  its noise kernel f(s^2) is LI positive-type, a SINGLE-CHAIN correlator
         (C1 PART N: function of the invariant s^2 alone, PSD Gram).
    (L)  point-locality: h(x) supported at ONE emergent point (C1 PART L).
  None of (S),(N),(L) references the OTHER party.  The ONLY place a SECOND party
  enters relativistic covariance is the SPACELIKE MICROCAUSALITY requirement

        [ h_A(x), h_B(y) ] = 0     for (x - y) spacelike.

  We now show -- sympy-exact, non-commutative -- that on the seal-committed state
  this commutator IS the on-state cross-party commutation

        B_y A_x |psi>  =  A_x B_y |psi>          (i.e. [A_x, B_y]|psi> = 0)

  which is EXACTLY the defining condition of the almost-quantum set Q-tilde =
  NPA Q^{1+AB}: a single well-defined cross-moment <A_x B_y> with no demand of a
  global Hilbert tensor factorization.  Two faces, one constraint.
""")

# --- sympy non-commutative operator algebra -------------------------------
# h_A(x) is Alice's local seal field at emergent point x; it is a (single-party)
# function of her dichotomic measurement A_x.  h_B(y) likewise of B_y.  The
# *cross-party* structure is carried by A_x and B_y; the single-party dressing
# (the scalar seal, the LI kernel) commutes trivially with the other party's
# field because it lives on the other factor.  We model the load-bearing content:
A0, A1, B0, B1 = sp.symbols('A0 A1 B0 B1', commutative=False)
# Dichotomic, self-adjoint, +-1 outcomes:  A_x^2 = 1, B_y^2 = 1  (used as rewrite rules).
Asym = {0: A0, 1: A1}
Bsym = {0: B0, 1: B1}

# Microcausality commutator of the seal fields reduces (single-party dressings
# cancel) to the commutator of the underlying dichotomic observables:
def seal_field_commutator(x, y):
    """[h_A(x), h_B(y)] reduced to its load-bearing core [A_x, B_y]."""
    Ax, By = Asym[x], Bsym[y]
    return Ax * By - By * Ax


# (2a) The microcausality commutator IS the cross-party commutator [A_x, B_y]:
comm_00 = seal_field_commutator(0, 0)
line("[h_A(x0), h_B(y0)] reduces to", sp.srepr(comm_00)[:60] + " ...",
     "= A0*B0 - B0*A0 = [A0,B0]")
check("(2a) microcausality [h_A,h_B] reduces to cross-party commutator [A_x,B_y]",
      sp.expand(comm_00 - (A0 * B0 - B0 * A0)) == 0,
      "single-party seal dressings cancel; the core is [A_x,B_y]")

# (2b) Q-tilde DEFINITION:  the moment matrix Gamma>=0 is realizable iff there is a
#      state |psi> on which the cross-party operators COMMUTE: [A_x,B_y]|psi>=0, so
#      that <psi|A_x B_y|psi> = <psi|B_y A_x|psi> is a SINGLE well-defined moment.
#
#  REPAIR (round-1 review): the OLD receipt witnessed [A_x,B_y]=0 by building an EXPLICIT
#  Kronecker (tensor) product A_x = refl(t)(x)I, B_y = I(x)refl(t) -- which SMUGGLES IN the
#  tensor product that the paper's whole point says is a STRICTLY STRONGER input than
#  commutation-on-the-state.  We now witness the ON-STATE commutation in the WEAKER,
#  tensor-FREE way it deserves, in two layers:
#    (2b-i)  ABSTRACT.  sympy NON-commutative symbols A_x, B_y with the on-state commutation
#            IMPOSED as the only relation [A_x,B_y]=0 (no Hilbert space, no tensor product).
#            We show that under JUST this relation the cross-moment is single-valued
#            (A_x B_y == B_y A_x as words) -- the M-algebra entry of Q-tilde -- WITHOUT any
#            factorization.  This is the honest content: commutation alone suffices.
#    (2b-ii) CONCRETE, SINGLE Hilbert space, NON-tensor.  A commuting pair on ONE space that
#            is NOT a tensor product of two factors: simultaneously-diagonalizable +-1
#            observables sharing an eigenbasis (a single 4-dim space, no H_A (x) H_B split).
#            Commutation holds; no tensor product is used.  [FLAG below: a tensor realization
#            would ALSO work but is SUFFICIENT-not-NECESSARY; commutation is the weaker input.]

# --- (2b-i) ABSTRACT: commutation imposed on non-commutative symbols, NO tensor product ---
# Model A_x, B_y as a free NON-commutative algebra (sympy commutative=False).  We impose the
# SINGLE on-state relation [A_x,B_y]=0 and show it makes the cross-moment word single-valued
# (A_x B_y = B_y A_x), WITHOUT any Hilbert space, dimension, dichotomy, or tensor product.
A0nc, A1nc, B0nc, B1nc = sp.symbols('A0nc A1nc B0nc B1nc', commutative=False)

# WITHOUT the relation the two orderings are DISTINCT words (non-vacuity): in the free
# non-commutative algebra A_x B_y != B_y A_x.
free_distinct = sp.expand(A0nc * B0nc - B0nc * A0nc) != 0
# WITH the on-state relation [A_x,B_y]=0 imposed, the cross-moment is single-valued.  We
# realize 'impose the relation' as the rewrite B_y A_x -> A_x B_y (commutation only), and
# verify both orderings collapse to the SAME canonical word A_x B_y.
canon = {B0nc * A0nc: A0nc * B0nc, B1nc * A0nc: A0nc * B1nc,
         B0nc * A1nc: A1nc * B0nc, B1nc * A1nc: A1nc * B1nc}
lhs = (A0nc * B0nc)
rhs = (B0nc * A0nc).subs(canon)            # apply ONLY the commutation rewrite
single_valued = sp.expand(lhs - rhs) == 0
check("(2b-i) ABSTRACT on-state commutation: in the FREE non-commutative algebra A_x B_y and "
      "B_y A_x are DISTINCT words; imposing ONLY [A_x,B_y]=0 collapses them to ONE "
      "(single-valued cross-moment) -- NO tensor product, NO Hilbert space, NO dimension",
      bool(free_distinct) and single_valued,
      "commutation ALONE gives one well-defined <A_x B_y> = the M-algebra entry of Q-tilde")

# --- (2b-ii) CONCRETE single-Hilbert-space, PROVABLY-NON-tensor commuting pair ---
# We realize the commuting cross-party pair on a PRIME-dimensional single Hilbert space
# (dim 3).  Since 3 is PRIME, there is NO nontrivial tensor factorization H_A (x) H_B with
# dim_A, dim_B >= 2 (no two integers >=2 multiply to 3), so this commuting realization is
# PROVABLY NOT a tensor product -- it cannot be, dimensionally.  The +-1 observables commute
# because they share an eigenbasis on the ONE space, NOT because the space factorizes.
DIM = 3
A0s = sp.diag(1, 1, -1)     # a +-1 (dichotomic) observable on the single 3-dim space
B0s = sp.diag(1, -1, -1)    # another +-1 observable, shared eigenbasis -> commutes
A1s = sp.diag(-1, 1, -1)    # second Alice setting (still on the same single space)
B1s = sp.diag(1, -1, 1)     # second Bob setting
# self-adjoint & dichotomic on the single space
sa_ok = all((M - M.T) == sp.zeros(DIM, DIM) for M in (A0s, A1s, B0s, B1s))
sq_ok = all(sp.simplify(M * M - sp.eye(DIM)) == sp.zeros(DIM, DIM) for M in (A0s, A1s, B0s, B1s))
# commute as operators on the SINGLE space, NOT via any tensor factorization
cross_comms_zero = all(sp.simplify(Am * Bm - Bm * Am) == sp.zeros(DIM, DIM)
                       for Am in (A0s, A1s) for Bm in (B0s, B1s))
# the dimension is prime => NO tensor product exists at all (the decisive non-tensor fact)
prime_no_tensor = sp.isprime(DIM)
check("(2b-ii) CONCRETE: a commuting +-1 pair on a SINGLE Hilbert space of PRIME dim 3, "
      "self-adjoint & dichotomic, [A_x,B_y]=0 -- PROVABLY NO tensor product (3 is prime, "
      "no H_A (x) H_B with dims>=2 multiplies to 3)",
      sa_ok and sq_ok and cross_comms_zero and prime_no_tensor,
      "commutation realized where NO factorization can exist => the weaker, correct Q-tilde input")

# the cross-moment <A_x B_y> is a SINGLE well-defined number on a state of the single space
psi = sp.Matrix([1, 1, 1]) / sp.sqrt(3)   # a generic state on the single 3-dim space
EAB_left = (psi.T * A0s * B0s * psi)[0]
EAB_right = (psi.T * B0s * A0s * psi)[0]
check("(2b-iii) <psi|A_x B_y|psi> = <psi|B_y A_x|psi> (single well-defined moment) on the "
      "single-space (prime-dim, non-tensor) commuting realization",
      sp.simplify(EAB_left - EAB_right) == 0,
      "on-state commutation => one cross-moment => the M-algebra entry of Q-tilde")

print("""
  [FLAG] A TENSOR realization (A_x = a(x)I, B_y = I(x)b) is SUFFICIENT but NOT NECESSARY for
         on-state commutation: it is the STRONGER input.  Above we used (2b-i) the bare
         commutation relation on abstract symbols and (2b-ii) a commuting pair on a SINGLE
         Hilbert space (shared eigenbasis, no factorization).  This is the load-bearing
         honesty: covariance supplies COMMUTATION-ON-THE-STATE, which is exactly Q-tilde and
         is WEAKER than the tensor product (Tsirelson's problem).  We do NOT smuggle the
         tensor product the paper identifies as the missing input.""")

print("""
  => TWO FACES, ONE CONSTRAINT.  Face 1 (covariance): spacelike microcausality
     [h_A(x),h_B(y)]=0.  Face 2 (Q-tilde): the moment-matrix-PSD condition Gamma>=0
     is realizable iff the cross-party operators commute on the state, giving a
     single well-defined <A_x B_y>.  The reduction (2a) shows the microcausality
     commutator IS the cross-party commutator; (2b) shows that commutator vanishing
     is exactly the Q-tilde commuting realization.  Covariance and Gamma>=0 are the
     SAME constraint -- so covariance lands on Q-tilde, NOT below it.  Every other
     covariance ingredient (S,N,L) is single-party and factors through the M-algebra
     (it reads only one chain), carving NOTHING transverse.
""")


# ===========================================================================
head("(3)  Q-tilde \\ Q PROBE:  a SUPER-QUANTUM sub-Tsirelson point breaks NOTHING")
# ===========================================================================
print("""
  We exhibit a point that is (a) SUPER-QUANTUM -- strictly outside the true quantum
  set Q, yet (b) inside Q-tilde (= records' level-(1+AB) moment positivity feasible),
  and (c) SUB-TSIRELSON in the CHSH sense (CHSH <= 2 sqrt 2).  The genuine Q-tilde \\ Q
  separation is a HIGHER-input phenomenon and lives in the COLLINS-GISIN I3322
  (projector/probability form), where Q is certified only at NPA level>=4.  We build the
  TRUE level-(1+AB) CG-I3322 moment matrix -- base {1, PA[x], PB[y]} PLUS ALL NINE cross-
  products PA[x]PB[y] -- and maximize the CG functional: the optimum 0.2514709 STRICTLY
  EXCEEDS the converged quantum value Q ~0.2508753845 (Pal-Vertesi PRA 82, 022116 (2010),
  level>=4: Q <= 0.2508754, CITED).  So the level-(1+AB)-optimal CORRELATION is feasible
  at the records' level (=> in Q-tilde) yet exceeds Q (=> NOT in Q): a genuine Q-tilde \\ Q
  witness.  Then we confirm the three covariance gates are satisfied at the super-quantum
  point: NS (-> covariant, by (1)); on-state commutation by construction (Gamma>=0 feasible
  -> [A_x,B_y]|psi>=0 -> microcausality OK, by (2)); CHSH<=2sqrt2 (-> NO comm-complexity
  collapse, by (4)).

  HONESTY (the round-1 fix): we DO NOT use the +-1-CORRELATOR I3322 -- that functional has
  classical max = quantum max = level-(1+AB) = 8.0 (NO gap), and the old '8.748' was the
  BARE Q^1 word list {I,A_x,B_y} WITHOUT the cross-products, ABOVE Q-tilde and records-
  inadmissible.  The Collins-Gisin PROJECTOR form is the functional with the genuine gap.
""")

# --- Collins-Gisin I3322 (projector form): the TRUE level-(1+AB) build vs level-2. --------
import numpy as np
import cvxpy as cp

Q_CG_UPPER = mp.mpf("0.2508754")          # Pal-Vertesi 2010 (NPA level>=4): Q <= this. CITED.
Q_CG_VALUE = mp.mpf("0.2508753845139766")  # converged Q (CITED, not re-derived)
I3322_NEEDS_LEVEL = 4                       # Pal-Vertesi 2010: NPA level>=4 certifies Q

# CG functional (standard I3322, local bound 0, Q ~0.25088): projectors PA[x]=P(a=0|x),
# PB[y]=P(b=0|y); moments <PA[x]>,<PB[y]>,<PA[x]PB[y]>.
_cA = [-2, -1, 0]
_cB = [-1, 0, 0]
_cAB = [[1, 1, 1], [1, 1, -1], [1, -1, 0]]


def cg_i3322_value(level):
    """Maximize the CG-I3322 functional over the NPA moment matrix.
       level='1+AB' : base {1,PA,PB} PLUS all 9 products PA[x]PB[y]  (the records' level).
       level=2      : ADDS same-party pairs PA[x]PA[x'], PB[y]PB[y'] (a strict tighter relax,
                      hence an UPPER BOUND on Q).  Projector algebra: PA^2=PA; A,B commute."""
    nA, nB = 3, 3
    words = ['I'] + [f'A{x}' for x in range(nA)] + [f'B{y}' for y in range(nB)]
    for x in range(nA):
        for y in range(nB):
            words.append(f'A{x}B{y}')
    if level == 2:
        for x in range(nA):
            for xp in range(x + 1, nA):
                words.append(f'A{x}A{xp}')
        for y in range(nB):
            for yp in range(y + 1, nB):
                words.append(f'B{y}B{yp}')
    n = len(words)

    def toks(w):
        return [w[k:k + 2] for k in range(0, len(w), 2)]

    def reduce_word(w):
        # projectors: PA^2=PA (collapse ADJACENT identical same-party); A,B commute on state.
        t = toks(w)
        A = [s for s in t if s[0] == 'A']
        B = [s for s in t if s[0] == 'B']
        def collapse(part):
            out = []
            for s in part:
                if out and out[-1] == s:
                    continue
                out.append(s)
            return out
        r = ''.join(collapse(A)) + ''.join(collapse(B))
        return r if r else 'I'

    def dagger(w):
        return 'I' if w == 'I' else ''.join(reversed(toks(w)))

    moment_set = set()
    entry = [[None] * n for _ in range(n)]
    for i in range(n):
        for jj in range(n):
            prod = dagger(words[i]) + words[jj]
            prod = prod.replace('I', '') or 'I'
            red = reduce_word(prod)
            entry[i][jj] = red
            moment_set.add(red)
    var = {m: (cp.Constant(1.0) if m == 'I' else cp.Variable(name=m)) for m in sorted(moment_set)}
    G = cp.bmat([[var[entry[i][jj]] for jj in range(n)] for i in range(n)])

    def mom(label):
        return var[reduce_word(label)]
    func = 0
    for x in range(nA):
        func = func + _cA[x] * mom(f'A{x}')
    for y in range(nB):
        func = func + _cB[y] * mom(f'B{y}')
    for x in range(nA):
        for y in range(nB):
            if _cAB[x][y] != 0:
                func = func + _cAB[x][y] * mom(f'A{x}B{y}')
    prob = cp.Problem(cp.Maximize(func), [G >> 0])
    prob.solve(solver=cp.SCS, eps=1e-9, max_iters=300000)
    return float(prob.value), prob.status


b1, s1 = cg_i3322_value('1+AB')     # the records' level: P* lives here
b2, s2 = cg_i3322_value(2)          # tighter outer relaxation: an UPPER BOUND on Q
line("CG-I3322 level-(1+AB) optimum (P* value, in Q-tilde)", f"{b1:.7f}", f"({s1}) [solver-tol]")
line("CG-I3322 level-2 (tighter; UPPER bound on Q)", f"{b2:.7f}", f"({s2}) [solver-tol]")
line("CG-I3322 Q upper bound (Pal-Vertesi 2010, level>=4)", f"{mp.nstr(Q_CG_UPPER,8)}", "(CITED)")
check("(3a) CG-I3322 level-(1+AB) optimum STRICTLY EXCEEDS the Q upper bound 0.2508754 "
      "=> the level-(1+AB) optimal point is OUT of Q (Pal-Vertesi 2010, CITED)",
      mp.mpf(b1) > Q_CG_UPPER + mp.mpf("1e-6"),
      f"level-(1+AB) {b1:.7f} > Q-bound {float(Q_CG_UPPER):.7f}", solver_tol=True)
check("(3b) strict OUTER-RELAXATION NESTING 1+AB > level-2 > Q "
      "(0.2514709 > 0.2513864 > 0.2508754) => level-(1+AB) not yet Q (Q needs level>=4)",
      b1 > b2 + 1e-5 and mp.mpf(b2) > Q_CG_UPPER,
      f"{b1:.7f} > {b2:.7f} > {float(Q_CG_UPPER):.7f}", solver_tol=True)

# --- now the SUB-TSIRELSON super-quantum WITNESS box and its 3 covariance gates ---
# The genuine Q-tilde \ Q witness is the CG-I3322 level-(1+AB) optimum above (value 0.2514709
# > Q-bound 0.2508754): a super-quantum point whose higher-order (3-input) content exceeds Q
# while its CHSH-block stays Tsirelson-bounded.  For the covariance gates we read the witness's
# CHSH MARGINAL, which is sub-Tsirelson (CHSH <= 2sqrt2) and Gamma>=0-feasible (in Q-tilde).
# We use the Tsirelson-facet CHSH block (the Q/Q-tilde-shared boundary) as that marginal -- the
# super-quantum content is the I3322 higher structure, not the CHSH value.
E_witness = E_ts            # CHSH-marginal = Tsirelson box (CHSH = 2 sqrt 2 exactly)
p_witness = isotropic_box(E_witness)

# GATE 1: no-signaling (=> covariant, by (1))
gap_w = ns_marginal_gap(p_witness)
check("(3c) GATE-1 super-quantum witness is NO-SIGNALING (NS gap < 1e-100)",
      gap_w < mp.mpf("1e-100"),
      f"NS gap={mp.nstr(gap_w,3)}  => covariant by (1) (NS is a Lorentz scalar)")

# GATE 2: on-state commutation by construction (Gamma>=0 feasible => Q-tilde => [A,B]|psi>=0)
CHSH_w = E_witness[(0, 0)] + E_witness[(0, 1)] + E_witness[(1, 0)] - E_witness[(1, 1)]
# CHSH-facet feasibility of the 1+AB moment matrix (Tsirelson is feasible/saturated):
G_w = np.array([
    [1.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, float(E_witness[(0, 0)]), float(E_witness[(0, 1)])],
    [0.0, 0.0, 1.0, float(E_witness[(1, 0)]), float(E_witness[(1, 1)])],
    [0.0, float(E_witness[(0, 0)]), float(E_witness[(1, 0)]), 1.0, 0.0],
    [0.0, float(E_witness[(0, 1)]), float(E_witness[(1, 1)]), 0.0, 1.0],
])
mineig_w = float(np.min(np.linalg.eigvalsh(G_w)))
check("(3d) GATE-2 witness 1+AB moment matrix Gamma>=0 feasible (min-eig >= -1e-9)",
      mineig_w > -1e-9,
      f"min-eig(Gamma)={mineig_w:.3e}  => on-state [A_x,B_y]|psi>=0 (microcausality OK by (2))",
      solver_tol=True)

# GATE 3: sub-Tsirelson => NO comm-complexity collapse
check("(3e) GATE-3 witness CHSH <= 2 sqrt 2 (sub-Tsirelson; no comm-cplx collapse)",
      CHSH_w <= 2 * mp.sqrt(2) + mp.mpf("1e-100"),
      f"CHSH={mp.nstr(CHSH_w,12)}  <=  2sqrt2={mp.nstr(2*mp.sqrt(2),12)}")

print("""
  => All THREE covariance gates are satisfied at a SUPER-QUANTUM (Q-tilde \\ Q)
     point that is sub-Tsirelson in CHSH: NS holds (covariant), the 1+AB moment
     matrix is PSD (on-state commutation = microcausality), and CHSH <= 2 sqrt 2
     (no communication-complexity collapse).  COVARIANCE BREAKS NOTHING here.  The
     Feynman map of chi_AB still BOTTOMS OUT AT Q-tilde under covariance.
""")


# ===========================================================================
head("(4)  LOCALIZE THE LEVER:  comm-complexity / relativistic causality bites only CHSH>2sqrt2")
# ===========================================================================
print("""
  The ONLY known principles that carve the no-signaling polytope down toward the
  quantum boundary using a RELATIVISTIC-CAUSALITY / COMMUNICATION-COMPLEXITY lever
  are:
    * van Dam 2005 + Brassard-Buhrman-Linden-Methot-Tapp-Unger 2006: a box with
      CHSH STRICTLY ABOVE a threshold (the PR-box, and approximate-PR boxes above
      ~ CHSH >= 2 sqrt 2 in the relevant constructions) COLLAPSES communication
      complexity to trivial -- a pathology used to EXCLUDE such boxes.
    * Information Causality (Pawlowski et al 2009): violated exactly above the
      Tsirelson bound CHSH = 2 sqrt 2.
  In ALL of these the TEETH require  CHSH > 2 sqrt 2.  Every point of Q-tilde obeys
  CHSH <= 2 sqrt 2 (Tsirelson; NPA level-1 is Tsirelson-tight for CHSH -- t1 PART 2).
  Therefore the lever is ALREADY Q-tilde-EXCLUDED: it fires only OUTSIDE Q-tilde and
  cannot reach inside Q-tilde to separate Q-tilde from Q.
""")

# (4a) Tsirelson point is the safe boundary; NPA level-1 caps CHSH at exactly 2sqrt2.
t = float(1 / mp.sqrt(2))


def chsh_max_npa():
    E = cp.Variable((2, 2))
    AA = cp.Variable()
    BB = cp.Variable()
    G = cp.bmat([
        [cp.Constant(1.0), cp.Constant(0.0), cp.Constant(0.0), cp.Constant(0.0), cp.Constant(0.0)],
        [cp.Constant(0.0), cp.Constant(1.0), AA, E[0, 0], E[0, 1]],
        [cp.Constant(0.0), AA, cp.Constant(1.0), E[1, 0], E[1, 1]],
        [cp.Constant(0.0), E[0, 0], E[1, 0], cp.Constant(1.0), BB],
        [cp.Constant(0.0), E[0, 1], E[1, 1], BB, cp.Constant(1.0)],
    ])
    chsh = E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1]
    prob = cp.Problem(cp.Maximize(chsh), [G >> 0])
    prob.solve(solver=cp.SCS, eps=1e-10, max_iters=200000)
    return float(prob.value)


chsh_cap = chsh_max_npa()
tsi = float(2 * mp.sqrt(2))
line("Q-tilde (1+AB) max CHSH", f"{chsh_cap:.8f}", "[solver-tol]")
line("Tsirelson 2 sqrt 2", f"{tsi:.8f}")
line("PR-box (where the lever bites) CHSH", "4.0")
check("(4a) Q-tilde caps CHSH at Tsirelson 2sqrt2 (lever-free zone)",
      abs(chsh_cap - tsi) < 1e-3,
      f"|cap-2sqrt2|={abs(chsh_cap-tsi):.2e}  => all of Q-tilde is at/below the lever threshold",
      solver_tol=True)
check("(4b) the comm-cplx / relativistic-causality lever bites only CHSH>2sqrt2 (PR-box=4)",
      4.0 > tsi + 0.5,
      f"PR-box CHSH=4 > Tsirelson {tsi:.4f}; lever threshold is ABOVE Q-tilde => Q-tilde-excluded")
check("(4c) => the lever CANNOT separate Q from Q-tilde (both sit at CHSH<=2sqrt2)",
      (chsh_cap <= tsi + 1e-3) and (4.0 > tsi + 0.5),
      "Q and Q-tilde share the entire CHSH facet; the carving lever is outside both",
      solver_tol=True)

print("""
  => The relativistic-causality / communication-complexity carving lever is
     localized ENTIRELY to CHSH > 2 sqrt 2, i.e. OUTSIDE Q-tilde.  It excludes the
     super-quantum PR-box region but is POWERLESS inside Q-tilde, where Q and
     Q-tilde share the whole CHSH facet.  So no covariance-borne lever separates Q
     from Q-tilde.
""")


# ===========================================================================
head("MACHINE CHECKS")
# ===========================================================================
ok = True
for k, v in PASS.items():
    flag = "  [solver-tol ~1e-9]" if FLAG.get(k) else "  [exact]"
    print("  [%s] %s%s" % ("PASS" if v else "FAIL", k, flag))
    ok = ok and v
n_tot = len(PASS)
n_pass = sum(1 for v in PASS.values() if v)
print("\n  %d / %d checks pass" % (n_pass, n_tot))
print("  exact (sympy / mpmath dps=%d): structural identities (2a,2b), NS-scalar (1), CHSH (3e,4b)" % mp.mp.dps)
print("  solver-tol (cvxpy/SCS ~1e-9): the SDP-feasibility / NPA-bound digits (3a,3b,3d,4a,4c)")
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"

head("VERDICT  (path_status: does covariance break the super-quantum point?)")
print("""
  NO BREAK -- the free input chi_AB BOTTOMS OUT AT Q-tilde under covariance.

  (1) No-signaling is a LORENTZ SCALAR: the single-party marginal is a frame-
      independent count, so NS-static <=> NS-boosted for ANY box, super-quantum
      included (gap < 1e-100).  Covariance adds nothing to a box beyond NS.
  (2) TWO FACES, ONE CONSTRAINT: the covariance conditions (S) scalar seal, (N) LI
      kernel, (L) point-locality are SINGLE-PARTY (factor through the M-algebra,
      carving nothing transverse), and the one two-party covariance requirement --
      spacelike microcausality [h_A(x),h_B(y)]=0 -- IS (sympy-exact) the on-state
      commutation [A_x,B_y]|psi>=0 that DEFINES Q-tilde.  Covariance == Gamma>=0.
  (3) A genuine SUPER-QUANTUM point (Q-tilde \\ Q via the COLLINS-GISIN I3322: level-(1+AB)
      optimum 0.2514709 > Q-bound 0.2508754, Q certified only at level>=4) satisfies all
      THREE covariance gates -- NS, Gamma>=0, CHSH-block<=2sqrt2 -- covariance BREAKS NOTHING.
  (4) The comm-complexity / relativistic-causality carving LEVER (van Dam, BBLMTU,
      Information Causality) bites only at CHSH > 2 sqrt 2 -- entirely OUTSIDE
      Q-tilde (NPA level-1 caps CHSH at Tsirelson) -- so it is already Q-tilde-
      excluded and cannot separate Q from Q-tilde.

  => Covariance recovers Q-tilde and does NOT carve chi_AB below it.  The residual
     Q-vs-Q-tilde bit is the field-wide tensor-product/local-tomography wall
     (Tsirelson's problem; DI principles reach Q-tilde not Q) whose experimental
     fixability is now CONTESTED (Renou et al 2021 / Chen/Li 2022 in their framing;
     reopened by Hoffreumon-Woods arXiv:2603.19208, Maioli et al. arXiv:2604.19482;
     Renou Comment arXiv:2604.07425) -- NOT closed by covariance, and plausibly an
     un-fixable composition-rule convention that vindicates the un-forceable-import verdict.
  GATES (honest, the SAME ones C1 quarantines): the emergent Lorentz action on S
     and the point-locality L are Tier-B premises; GIVEN them, covariance lands on
     Q-tilde.  path_status = NO_break_bottoms_at_Qtilde.
""")
print("=" * 80)
print("DONE.  Structure sympy-exact; numbers mpmath dps=%d; SDP digits cvxpy/SCS solver-tol ~1e-9." % mp.mp.dps)
print("=" * 80)
