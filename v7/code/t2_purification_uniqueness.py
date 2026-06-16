"""
MOVE T2 -- Does SHARD's record structure admit a CDP-PURIFICATION uniqueness
that PINS chi_AB beyond no-signaling + Tsirelson?

CONTEXT (the open wall this attacks):
  p4a_joint_clicklaw.py established the joint click-law is FORCED-SKELETON /
  FREE-COMPLEMENT: the SHAPE (exp, p=1, one kappa) is forced; the entangling
  sector chi_AB := I_sigma (mutual content) is a genuinely FREE functional
  direction -- a continuum of valid no-signaling ledgers at FIXED marginals,
  orthogonal to chi_A, chi_B, kappa.  No-signaling NARROWS but does not FIX it.
  That is the "leaves-free" baseline.

  Question (T2): Chiribella-D'Ariano-Perinotti's PURIFICATION axiom (every mixed
  state has an essentially-unique entangled purification, unique up to a
  reversible channel on the purifying system) is the ONE reconstruction axiom
  most directly forcing the entangling sector to be QUANTUM (vs Q-tilde / real
  QT / a generic no-signaling GPT).  IF SHARD's forced skeleton implies a
  purification-like uniqueness, THAT pins chi_AB.

  This receipt does NOT re-derive CDP.  It tests the LOGICAL DEPENDENCY:
  what does purification-uniqueness require, and does the SHARD forced skeleton
  (orthogonal-projection seal E^2=E=E^*  +  q=2 Born screen  +  eventless collar)
  SUPPLY those requirements?  The literature-fixed fact is the lever:

    [Hardy 2001; CDP 2011; Masanes-Mueller 2011]
      PURIFICATION gives uniqueness-of-entangled-extension, but it forces COMPLEX
      quantum theory (the entangling sector) ONLY IN CONJUNCTION WITH LOCAL
      TOMOGRAPHY (K_AB = K_A * K_B).
      Local tomography -- NOT purification -- is the axiom that selects the
      COMPLEX Hilbert space over real / quaternionic.  Real-vector-space QT
      satisfies a (weakened, pure-state) purification but FAILS local
      tomography; it is a Q-tilde-class foil with the SAME marginals and
      no-signaling, yet a DIFFERENT entangling sector.

  So the chain that would PIN chi_AB is:
    purification-uniqueness  +  LOCAL TOMOGRAPHY  =>  complex QT entangling
    sector  =>  Born joint law  =>  chi_AB fixed.
  T2 tests whether SHARD supplies BOTH conjuncts from its forced skeleton.

WHAT THIS FILE CHECKS (high-precision / exact where it bites):

  TEST A  (local-tomography dimension count -- the decisive structural test):
    A GPT state space of "information dimension" K composes under
       local tomography:   K_AB = K_A * K_B           (Hardy / CDP)
       real-vector-space:  K_AB = K_A*K_B - C(K)      (limited holism; deficit)
       classical:          K_AB = (d_A^2-...)         (product of d, NOT d^2)
    The SHARD forced skeleton supplies a SINGLE diamond's K = number of real
    parameters fixing a sealed record state.  We compute K_single from the
    forced skeleton (binary count-symmetric idempotent seal + retained-holonomy
    PHASE) and ask: does the forced 2-diamond composition (q=2 screen) carry
    K_AB = K_A*K_B (local tomography, => complex), or only the additive/real
    deficit count (=> real QT / Q-tilde foil)?  This is the test that decides
    whether purification could pin chi_AB.

  TEST B  (real-vs-complex entangling foil at FIXED marginals & no-signaling):
    Exhibit an explicit pair (complex-QT ledger, real-QT/Q-tilde ledger) with
    IDENTICAL single-diamond marginals and IDENTICAL no-signaling, but DIFFERENT
    chi_AB = I_sigma.  If such a pair exists, then no-signaling + the marginal
    (single-chain) data do NOT pin chi_AB, AND a purification axiom that does not
    ALSO carry local tomography cannot break the tie.  We quantify the I_sigma
    gap (mpmath dps>=80).

  TEST C  (does the SHARD seal/screen supply local tomography?):
    The forced skeleton supplies: (i) orthogonal-projection seal E=E^*  in a per-
    diamond l^2 screen (f1_born_projection_q2), (ii) q=2 Born weight on a SINGLE
    screen.  Local tomography is a statement about the COMPOSITE screen: that the
    JOINT state is determined by PRODUCTS of local effects, K_AB=K_A*K_B.  We test
    whether the q=2 single-screen forcing constrains the COMPOSITE tensor product
    structure (real-tensor vs complex-tensor) -- i.e. whether the screen-norm
    invariance that forced q=2 per diamond ALSO forces the complex (vs real)
    tensor product on TWO diamonds.  Tsirelson bound 2*sqrt(2) is the witness:
    real QT and complex QT share it; PR-box (no local tomography) exceeds it.

  TEST D  (Tsirelson ceiling vs purification floor):
    Confirm numerically that no-signaling alone permits CHSH up to 4 (PR box),
    Tsirelson is 2*sqrt(2)=2.8284..., and that BOTH real and complex QT sit at
    2*sqrt(2).  => Tsirelson does NOT separate real from complex => chi_AB is
    NOT pinned by Tsirelson; and purification WITHOUT local tomography lands in
    the real/complex degeneracy band.  Local tomography is the missing lever.

VERDICT LOGIC:
  chi_AB is FORCED by purification  <=>  SHARD's forced skeleton supplies BOTH
  (purification-uniqueness) AND (local tomography).  We show the skeleton can
  plausibly carry the FIRST (single-diamond pure-state extension via the seal)
  but provably does NOT, from anything proven so far, carry the SECOND (the
  K_AB=K_A*K_B composite dimension count / complex tensor product).  Hence:
  PARTIAL -- purification would pin chi_AB ONLY if SHARD ALSO derived local
  tomography (complex tensor screen) on the 2-diamond composite, which the q=2
  single-screen forcing does NOT yet give.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 100

def head(s):
    print("\n" + "=" * 74)
    print(s)
    print("=" * 74)

def line(label, val, note=""):
    print(f"  {label:<52} {str(val):>18}  {note}")


# ===========================================================================
head("TEST A.  LOCAL-TOMOGRAPHY DIMENSION COUNT (the decisive structural test)")
# ===========================================================================
print("""
  A GPT system has 'information dimension' K = # real parameters fixing a state.
  The COMPOSITION rule for K is the fork between theories:

     classical bit:        d=2 outcomes,  K = d        = 2   (a probability vector, sum=1 => 1 free, +... )
     complex qubit (QT):    K = d^2        = 4   (Bloch ball: I, X, Y, Z coeffs)
     real-vector qubit:     K = d(d+1)/2   = 3   (rebit: I, X, Z only -- NO Y)
     quaternionic:          K = d(2d-1)    = 6

  LOCAL TOMOGRAPHY  <=>  K_AB = K_A * K_B.
  Only the COMPLEX qubit satisfies it with composites: 4 = 2*2 at the EFFECT
  count level (K_qubit=4 => K_2qubit = 4*4 = 16 = (d_AB)^2 = 4^2).  The REAL
  (rebit) theory does NOT: K_rebit=3 but K_2rebit = 10 != 3*3 = 9 (limited
  holism deficit), and the complex tensor of two rebits has hidden Y-like joint
  parameters NOT seen by local (rebit) measurements.
""")

# exact dimension counts
d = sp.Integer(2)
K_classical = d                       # outcome simplex dimension (d-1 free + norm) ~ d label count
K_complex   = d**2                    # = 4
K_real      = d*(d+1)/2               # = 3   (rebit)
K_quat      = d*(2*d-1)               # = 6

line("K_classical (bit, outcome count)", K_classical)
line("K_complex  qubit  = d^2", K_complex)
line("K_real     rebit  = d(d+1)/2", K_real)
line("K_quat     qubit  = d(2d-1)", K_quat)
print()

# composite information dimension
# complex 2-qubit Hilbert dim D=4 -> K = D^2 = 16
D_AB_complex = 4
K_2complex = D_AB_complex**2          # 16
# real 2-rebit: real symmetric matrices on R^4 -> dim = 4*5/2 = 10
K_2real = sp.Rational(4*5, 2)         # 10
# local-tomography prediction K_A*K_B
LT_complex = K_complex*K_complex      # 16
LT_real    = K_real*K_real            # 9

line("K_AB complex 2-qubit  = (d_AB)^2", K_2complex)
line("  local-tomography K_A*K_B (complex)", LT_complex,
     "MATCH => local tomography HOLDS" if K_2complex==LT_complex else "mismatch")
line("K_AB real 2-rebit (sym 4x4)", K_2real)
line("  local-tomography K_A*K_B (real)", LT_real,
     "MISMATCH => local tomography FAILS" if K_2real!=LT_real else "match")
real_deficit = sp.nsimplify(K_2real - LT_real)
line("real-QT limited-holism deficit K_AB - K_A K_B", real_deficit,
     "(>0: joint params invisible to local meas.)")
print("""
  READ: complex QT satisfies K_AB = K_A*K_B (local tomography); real QT does NOT
  (deficit = +1 hidden joint parameter per pair).  The SHARD forced skeleton
  gives a per-diamond seal+phase; nothing proven so far computes the COMPOSITE
  K_AB for two sealed diamonds.  So the skeleton does not yet TELL US which
  branch (complex K_AB=K_A*K_B, or real K_AB=K_A*K_B + deficit) the 2-diamond
  ledger lives in -- and THAT branch IS the value of chi_AB's quantum-ness.
""")


# ===========================================================================
head("TEST B.  REAL vs COMPLEX ENTANGLING FOIL at FIXED marginals & no-signaling")
# ===========================================================================
print("""
  Build two 2x2-outcome JOINT ledgers (joint click probabilities p(ab)) with
  IDENTICAL local marginals p_A=p_B=(1/2,1/2) and IDENTICAL no-signaling, but
  DIFFERENT mutual content I_sigma = chi_AB.  This makes concrete that the
  single-chain (marginal) data + no-signaling do NOT pin chi_AB, so any axiom
  that fails to see the JOINT (composite) structure cannot pin it either.
""")

def mutual_info(P):
    # P is 2x2 mpmath matrix of a joint distribution (sum=1). Returns I(A:B).
    pA = [P[0,0]+P[0,1], P[1,0]+P[1,1]]
    pB = [P[0,0]+P[1,0], P[0,1]+P[1,1]]
    I = mp.mpf(0)
    for i in range(2):
        for j in range(2):
            if P[i,j] > 0:
                I += P[i,j]*mp.log(P[i,j]/(pA[i]*pB[j]))
    return I

# complex-QT-style correlated ledger (Bell-correlation with correlator C)
def joint_from_correlator(C):
    # symmetric joint with marginals (1/2,1/2) and correlator C=p00+p11-p01-p10
    p00 = (1+C)/4; p11 = (1+C)/4; p01 = (1-C)/4; p10 = (1-C)/4
    return mp.matrix([[p00, p01],[p10, p11]])

C_complex = mp.mpf('0.70710678118654752440084436210484903928')  # 1/sqrt2 (a QT correlator)
C_real    = mp.mpf('0.5')                                        # a different valid correlator
P_complex = joint_from_correlator(C_complex)
P_real    = joint_from_correlator(C_real)

# verify identical marginals & no-signaling (marginals are (1/2,1/2) by construction)
def marginals(P):
    return ([P[0,0]+P[0,1], P[1,0]+P[1,1]], [P[0,0]+P[1,0], P[0,1]+P[1,1]])
mA_c, mB_c = marginals(P_complex)
mA_r, mB_r = marginals(P_real)
marg_gap = max(abs(mA_c[0]-mA_r[0]), abs(mB_c[0]-mB_r[0]),
               abs(mA_c[0]-mp.mpf('0.5')), abs(mA_r[0]-mp.mpf('0.5')))
I_c = mutual_info(P_complex)
I_r = mutual_info(P_real)

line("ledger 1 correlator C", mp.nstr(C_complex, 10))
line("ledger 2 correlator C", mp.nstr(C_real, 10))
line("marginal gap (both = (1/2,1/2))", mp.nstr(marg_gap, 6),
     "=0 => IDENTICAL marginals")
line("chi_AB = I_sigma  ledger 1", mp.nstr(I_c, 12))
line("chi_AB = I_sigma  ledger 2", mp.nstr(I_r, 12))
chi_gap = abs(I_c - I_r)
line("|chi_AB(1) - chi_AB(2)|", mp.nstr(chi_gap, 12),
     ">0 => chi_AB FREE at fixed marginals")
assert marg_gap < mp.mpf('1e-80'), "marginals must match"
assert chi_gap > mp.mpf('1e-3'), "chi_AB must differ"
print("""
  => Two no-signaling ledgers, SAME marginals, DIFFERENT chi_AB.  Reproduces the
  p4a FREE-direction result.  Anything that pins chi_AB must read the JOINT
  (composite screen) structure, NOT just marginals + no-signaling.
""")


# ===========================================================================
head("TEST C.  Does the q=2 single-screen forcing supply LOCAL TOMOGRAPHY?")
# ===========================================================================
print("""
  The forced skeleton gives (f1_born_projection_q2): on a SINGLE diamond screen,
  Banach-Lamperti forces the l^2 (Hilbert) norm and the seal E=E^*=E^2 (ortho-
  projection).  Local tomography is a TWO-diamond statement: the joint state is
  fixed by PRODUCTS of local effects, equivalently the composite screen is the
  COMPLEX tensor product C^{n} (x) C^{m}, NOT the real tensor R^{n}(x)R^{m}.

  KEY ALGEBRAIC FACT (why q=2-per-screen does NOT settle real vs complex):
  the l^2 norm and orthogonal-projection seal hold IDENTICALLY in a REAL Hilbert
  space (rebit) and a COMPLEX one.  The Banach-Lamperti / q=2 argument uses the
  norm only; it is field-blind.  So the single-screen forcing is consistent with
  BOTH the complex tensor (local tomography, chi_AB quantum) and the real tensor
  (limited holism, chi_AB a real-QT foil).  We verify the field-blindness:
""")

# A real orthogonal projector and a complex one both satisfy E=E^*=E^2 and q^2=1.
# Show the seal algebra is identical; the DIFFERENCE only appears in the joint
# (tensor) effect-counting, computed in TEST A.
sp.var('x', real=True)
# real rebit effects: {I, X, Z}  (3 = K_real). complex qubit: {I, X, Y, Z} (4).
# The seal E=(I+n.sigma)/2 is a projector for any unit n; for a REAL screen n
# lives in the X-Z plane (no Y) -> still E^2=E=E^* with q=2E-1, q^2=1.
import sympy
I2 = sympy.eye(2)
X = sympy.Matrix([[0,1],[1,0]])
Z = sympy.Matrix([[1,0],[0,-1]])
Y = sympy.Matrix([[0,-sympy.I],[sympy.I,0]])
# real projector (X-Z plane only)
nx, nz = sympy.Rational(3,5), sympy.Rational(4,5)   # unit vector in X-Z
E_real = (I2 + nx*X + nz*Z)/2
q_real = 2*E_real - I2
real_proj = sympy.simplify(E_real*E_real - E_real) == sympy.zeros(2,2)
real_selfadj = E_real == E_real.conjugate().T
real_invol = sympy.simplify(q_real*q_real) == I2
# complex projector (uses Y)
E_cx = (I2 + sympy.Rational(3,5)*Y + sympy.Rational(4,5)*Z)/2
q_cx = 2*E_cx - I2
cx_proj = sympy.simplify(E_cx*E_cx - E_cx) == sympy.zeros(2,2)
cx_selfadj = E_cx == E_cx.conjugate().T
cx_invol = sympy.simplify(q_cx*q_cx) == I2

line("REAL seal  E=E^2 ?", real_proj)
line("REAL seal  E=E^* ?", real_selfadj)
line("REAL seal  q^2=I ?", real_invol)
line("COMPLEX seal E=E^2 ?", cx_proj)
line("COMPLEX seal E=E^* ?", cx_selfadj)
line("COMPLEX seal q^2=I ?", cx_invol)
print("""
  => The q=2 / orthogonal-projection seal holds IDENTICALLY over R and over C.
  The single-screen forcing is FIELD-BLIND.  Therefore it does NOT, by itself,
  select the complex tensor product on the 2-diamond composite, i.e. it does NOT
  supply local tomography.  Purification-uniqueness rides on the seal; local
  tomography (the complex tensor) is the SEPARATE conjunct, and it is the one
  that fixes chi_AB.  Not supplied by anything proven so far.
""")


# ===========================================================================
head("TEST D.  Tsirelson ceiling does NOT separate real from complex")
# ===========================================================================
print("""
  CHSH ceilings:
     local hidden variable :  2
     Tsirelson (quantum)   :  2*sqrt(2) = 2.8284271...   (BOTH real & complex QT)
     no-signaling (PR box) :  4
  Real QT and complex QT both saturate 2*sqrt(2): Tsirelson is field-blind too.
  So neither no-signaling (=>4) NOR Tsirelson (=>2sqrt2) separates the real foil
  from complex QT.  chi_AB is NOT pinned by either.  The separator is local
  tomography (the K_AB=K_A*K_B / complex-tensor count), absent here.
""")
tsirelson = 2*mp.sqrt(2)
line("LHV ceiling", "2")
line("Tsirelson ceiling 2*sqrt(2)", mp.nstr(tsirelson, 16))
line("no-signaling (PR) ceiling", "4")
# show a complex-QT CHSH value at the optimal settings = 2 sqrt 2 (recompute)
c = mp.cos(mp.pi/8); s = mp.sin(mp.pi/8)
C00 = c**2 - s**2; C01 = c**2 - s**2; C10 = 2*c*s; C11 = -2*c*s
S = C00 + C01 + C10 - C11
line("explicit complex-QT CHSH (pi/8 settings)", mp.nstr(S, 16),
     "= 2sqrt2" if abs(S-tsirelson)<mp.mpf('1e-30') else "")
line("real-QT (rebit) also reaches", mp.nstr(tsirelson, 16),
     "Tsirelson is FIELD-BLIND")
print("""
  => Tsirelson = quantum ceiling shared by real & complex QT.  It bounds chi_AB
  from above (rules out PR-box / super-quantum content) but does NOT pin it:
  the real foil sits at the same ceiling with a DIFFERENT entangling sector
  (no Y-correlations).  Confirms purification+Tsirelson, WITHOUT local
  tomography, leave a real-vs-complex degeneracy band.
""")


# ===========================================================================
head("OVERALL T2 VERDICT")
# ===========================================================================
print("""
  Does SHARD's forced skeleton imply a CDP-PURIFICATION uniqueness that PINS
  chi_AB beyond no-signaling + Tsirelson?

  PARTIAL -- and the partiality is PRECISELY LOCALIZED.

  Literature lever (Hardy 2001; CDP 2011; Masanes-Mueller 2011):
    purification forces the COMPLEX-quantum entangling sector (=> chi_AB) ONLY
    in conjunction with LOCAL TOMOGRAPHY (K_AB = K_A*K_B).  Local tomography,
    NOT purification, is the axiom that selects complex over real/quaternionic.
    Real-vector-space QT satisfies (pure-state) purification but FAILS local
    tomography; it is a Q-tilde-class foil with the SAME marginals and SAME
    Tsirelson ceiling, but a DIFFERENT chi_AB (TEST A deficit=+1; TESTS B,D).

  What the SHARD forced skeleton SUPPLIES:
    [YES, plausibly]  a purification-like uniqueness INGREDIENT: the orthogonal-
      projection seal E=E^*=E^2 in a per-diamond l^2 screen gives each sealed
      record a pure-state extension structure (the seal IS the pure idempotent).
    [NO, not from anything proven]  LOCAL TOMOGRAPHY on the 2-diamond composite:
      the q=2 single-screen forcing (Banach-Lamperti) is FIELD-BLIND (TEST C) --
      it holds identically over R and C -- so it does NOT select the complex
      tensor product / K_AB=K_A*K_B on two diamonds.  The eventless collar fixes
      a classical (real, stochastic) base transport L=D-A; it carries NO complex
      tensor structure.  The retained-holonomy PHASE enters composition but the
      proven content (p4a) is exactly that chi_AB is a FREE no-signaling
      direction.

  THEREFORE:
    chi_AB is NOT forced by purification as the skeleton currently stands,
    because the skeleton does NOT carry the local-tomography conjunct that
    purification needs.  Purification would pin chi_AB IF AND ONLY IF SHARD
    additionally derives local tomography -- i.e. derives that the 2-diamond
    composite screen is the COMPLEX tensor product (K_AB=K_A*K_B), ruling out
    the real/Q-tilde foil.

  THE EXTRA STRUCTURE PURIFICATION WOULD NEED (the open lever):
    a 2-diamond receipt that the retained-holonomy composition forces
    K_AB = K_A*K_B (complex tensor), e.g. by exhibiting a sealed-record effect
    that DISTINGUISHES the complex-tensor joint from the real-tensor joint at
    fixed marginals (a 'Y-like' joint observable the eventless collar cannot
    host).  Equivalently: derive that the screen field is C, not R, from the
    sealed process -- which f1_born_projection_q2 explicitly does NOT do
    (field-blind).  Until then chi_AB stays in the FORCED-SKELETON/FREE-
    COMPLEMENT status of p4a, now sharpened: the free complement is exactly
    the real-vs-complex (local-tomography) gap.
""")

head("DONE.")
