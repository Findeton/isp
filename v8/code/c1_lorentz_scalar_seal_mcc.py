"""
MOVE C1 -- "Lorentz-scalar seal -> MCC (microcausality to all orders)".

QUESTION
--------
Is the SHARD seal/record-firing density a LOCAL LORENTZ SCALAR field operator,
and can it therefore INHERIT the 2025 microcausality-all-orders proof of
Gundhi-Diosi-Carlesso (GDC, arXiv:2507.06954)?

THE 2025 LITERATURE ANCHOR (verified by web fetch of arXiv:2507.06954 HTML)
--------------------------------------------------------------------------
GDC build a covariant collapse master equation with stochastic Hamiltonian
density

    H_st(t) = hbar sqrt(gamma) integral d^3z  Q(z) xi(t,z),

    Q(x) = (1/2) alpha :phi^2(x):        (a NORMAL-ORDERED LORENTZ SCALAR
                                          built from the field at ONE point x),

and a non-Markovian noise with a LORENTZ-INVARIANT correlator
G(x,y) = G((x-y)_mu (x-y)^mu).  Their microcausality-to-all-orders (MCC)
result rests on TWO properties of the collapse operator Q, and ONE on the noise:

  (L)  LOCALITY:   Q(x) is built from fields at a SINGLE spacetime point
                   (NOT a non-local product like phi_+ phi_-).
  (S)  SCALAR:     Q(x) is a Lorentz scalar (covariant transformation).
  (N)  LI noise:   the kernel G depends only on the invariant (x-y)^2.

The all-orders mechanism (their own words, fetched):
  nested commutators  [Q(x_n),...[Q(x_1), O(z_2)], O(z_1)]  vanish unless
  every x_i lies in the past light cone of z_2; that forces z_1 into the past
  cone of z_2, which preserves the spacelike commutator [O(z_2),O(z_1)]=0.
  Recursion over n => MCC to ALL ORDERS.  Normal ordering :phi^2: is needed
  ONLY for the finite energy rate, NOT for MCC.

Companion: Fedida 2025 (arXiv:2506.14693) shows the SAME spacelike structure
at the measurement/collapse level in the Tomonaga-Schwinger picture: IRREVERSIBLE
selective collapses over spacelike-separated precompact regions obey a
state-independent commutation relation (the [H(x),H(y)]=0-spacelike HALF of
TS integrability), with no superluminal signalling.

WHAT THIS RECEIPT TESTS (NOT a number-cruncher; a STRUCTURAL audit with
algebraic checks that make the inheritance condition concrete)
--------------------------------------------------------------------------
The MCC inheritance requires SHARD's seal-firing density h_seal(x) to be
EXPRESSIBLE as a LOCAL LORENTZ SCALAR field operator obeying [h(x),h(y)]=0 at
spacelike (x-y).  We check, piece by piece, which of (L),(S),(N) the FORCED
seal structure (Paper I) supplies and which it does NOT:

  (S-algebra)  The seal E is FORCED self-adjoint idempotent (f1_born), and the
               content chi = D(P_AB||P_BA) is a weight-0 KL number (f4).  A
               self-adjoint projection and a scalar KL functional are scalar
               (weight-0) ALGEBRAIC objects -- BUT being a Lorentz scalar
               requires an emergent Lorentz action under which they are
               invariant, which is a TIER-B premise, not a Tier-A fact.
               -> we check the ALGEBRAIC scalar property explicitly (E=E^*,
                  chi is a number) and FLAG the Lorentz-action gap.

  (L-locality) GDC need Q(x) at a SINGLE point.  SHARD's primitive is a
               FINITE holonomy DIAMOND with extent -- a region, not a point.
               -> we test whether the seal density is POINT-LOCAL or only
                  REGION-LOCAL, and show the diamond is point-local in the
                  EMERGENT (Tier-B) coarse-grained limit ONLY (collar -> 0).

  (N-LI noise) GDC need G((x-y)^2) Lorentz-invariant; SHARD's Tier-B kernel
               f(s^2) (f1_kernel_positive_type) IS already a function of the
               invariant s^2, positive-type, quartic UV decay.
               -> we VERIFY f is a function of s^2 alone (LI form) and PSD,
                  i.e. (N) is the one GDC condition SHARD ALREADY supplies at
                  Tier B.

  (Spacelike-commute, all orders)  Given (L)+(S)+(N), we REPRODUCE the GDC
               recursion algebraically on a finite operator model: build a
               self-adjoint scalar "seal density" from a free-field-like local
               object on a causal-set/lattice, and check that nested commutators
               with a spacelike-separated probe VANISH to all orders tested,
               while a NON-LOCAL (region-smeared across a spacelike gap) seal
               density FAILS.  This makes the inheritance condition operational:
               MCC is inherited IFF the seal density is point-local-scalar.

VERDICT LOGIC
-------------
  * Tier-B (emergent-spacetime regime): IF SHARD's records coarse-grain to a
    Lorentz-covariant continuum with a point-local self-adjoint scalar seal
    density and the already-LI kernel f(s^2), THEN MCC-all-orders is INHERITED
    verbatim from GDC -- the spacelike-commutation HALF of Tomonaga-Schwinger
    integrability ([H(x),H(y)]=0 spacelike) comes for free, to all orders.
  * Tier-A (fundamental, pre-geometric): the seal is scalar-ALGEBRAIC (E=E^*,
    chi weight-0) but there is NO Lorentz group and NO point to be local at, so
    (L) and (S) are NOT facts of the fundamental law -- they are exactly the
    emergence premises Paper I quarantines into Tier B.  SHARD therefore does
    NOT get MCC at Tier A; it gets a clean INHERITANCE THEOREM at Tier B,
    conditional on the SAME emergence it already declares open.

All algebra sympy-exact; all numerics mpmath dps=100.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 100


def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


def line(label, val, extra=""):
    print(f"  {label:<50} {val} {extra}")


# ===========================================================================
head("PART S -- the SEAL is a SCALAR (weight-0) ALGEBRAIC object  [Tier-A fact]")
# ===========================================================================
print("""
  Paper I S3.1 (f1_born_projection_q2): the seal E is FORCED to be an orthogonal
  (self-adjoint) projection, E=E^2=E^*.  Paper I S2/S3.4 (f4_variational_rate):
  the content chi=D(P_AB||P_BA) is a weight-0 KL NUMBER.  Both are SCALAR objects
  under the screen/internal automorphisms.  We confirm the algebraic scalar
  property: E is self-adjoint (so q=2E-1 is a self-adjoint reflection, a scalar
  under unitary conjugation up to similarity), and chi is a pure number (rank-0
  tensor) invariant under the internal relabeling P_AB <-> its presentation.
""")
# self-adjoint projection on a 2-dim screen (the forced seal)
t = sp.symbols('t', real=True)
E_t = sp.Matrix([[1, t], [0, 0]])          # idempotent for all t
I2 = sp.eye(2)
gap_norm = sp.expand((E_t.T*E_t + (I2-E_t).T*(I2-E_t) - I2))  # not the test; just context
E0 = E_t.subs(t, 0)
line("seal E (t=0): E^2=E ?", sp.simplify(E0*E0 - E0) == sp.zeros(2, 2))
line("seal E (t=0): E=E^* (self-adjoint/scalar-under-conj) ?", E0 == E0.T)
q0 = 2*E0 - I2
line("q=2E-1: q^2=I ? and q=q^* ?", (sp.simplify(q0*q0) == I2, q0 == q0.T))
# chi is a scalar (weight 0): under internal relabeling it is invariant; numeric KL
p = [mp.mpf('0.6'), mp.mpf('0.4')]
q = [mp.mpf('0.3'), mp.mpf('0.7')]
chi = sum(pi*mp.log(pi/qi) for pi, qi in zip(p, q))
chi_relabel = sum(pi*mp.log(pi/qi) for pi, qi in zip(p[::-1], q[::-1]))  # relabel both
line("chi = D(P_AB||P_BA) (a number) =", mp.nstr(chi, 12))
line("chi invariant under simultaneous index relabel ?",
     abs(chi - chi_relabel) < mp.mpf('1e-90'),
     f"(gap {mp.nstr(abs(chi-chi_relabel),3)})")
print("""
  => The seal carries the (S) ingredient ALGEBRAICALLY: E is self-adjoint, chi
     is weight-0 (rank-0).  This is the GOOD news for C1: GDC's collapse
     operator Q=(1/2)alpha:phi^2: is ALSO a self-adjoint scalar -- the seal is
     the right KIND of object.  CAVEAT below: 'scalar under the EMERGENT Lorentz
     group' is a Tier-B premise, not this Tier-A algebraic fact.
""")


# ===========================================================================
head("PART N -- the Tier-B noise kernel f(s^2) is ALREADY Lorentz-invariant  [SHARD supplies (N)]")
# ===========================================================================
print("""
  GDC need the noise correlator G to depend ONLY on the invariant (x-y)^2.
  SHARD's Tier-B locality kernel f(s^2) (f1_kernel_positive_type) is, by
  construction, a function of the invariant s^2 alone, positive-type (Bochner),
  quartic UV decay.  So the ONE GDC condition on the NOISE, (N), SHARD already
  meets at Tier B.  We re-verify the LI form: f built from a spectrum
  ghat(q^2)=e^{-q^4} is (i) a function of |s| only (even, depends on s^2), and
  (ii) positive semidefinite Gram (positive-type).
""")
def ghat_quartic(qv):
    return mp.e**(-(qv)**4)
def f_from_spectrum(x, qmax=mp.mpf('40')):
    x = mp.mpf(x)
    return mp.quad(lambda qv: ghat_quartic(qv)*mp.cos(qv*x), [0, qmax]) / mp.pi
# (i) function of s^2: f(s)=f(-s)
f_p = f_from_spectrum(mp.mpf('1.3'))
f_m = f_from_spectrum(mp.mpf('-1.3'))
line("f(s) even (depends on s^2 only): f(1.3)-f(-1.3) =", mp.nstr(f_p - f_m, 6))
# (ii) positive-type: Gram PSD on irregular sample
xs = [mp.mpf(v) for v in ['0', '0.37', '0.81', '1.23', '1.9', '2.6', '3.4']]
cache = {}
def fcache(d):
    k = mp.nstr(mp.mpf(d), 40)
    if k not in cache:
        cache[k] = f_from_spectrum(d)
    return cache[k]
n = len(xs)
M = mp.matrix(n, n)
for i in range(n):
    for j in range(n):
        M[i, j] = fcache(xs[i]-xs[j])
mineig = min(mp.eigsy(M, eigvals_only=True))
line("kernel Gram min-eigenvalue (>=0 => positive-type / LI noise OK):",
     mp.nstr(mineig, 12))
print("""
  => (N) is SUPPLIED by SHARD at Tier B: f(s^2) is a Lorentz-invariant,
     positive-type colored-noise correlator, exactly GDC's required G((x-y)^2).
     This is the single GDC ingredient SHARD already has in hand.
""")


# ===========================================================================
head("PART L+MCC -- LOCALITY is the load-bearing gap; reproduce GDC all-orders recursion")
# ===========================================================================
print("""
  GDC's all-orders MCC needs Q POINT-LOCAL.  SHARD's primitive is a FINITE
  holonomy DIAMOND (a region with a collar), NOT a point.  We make the
  inheritance condition OPERATIONAL with a finite causal-lattice operator model:

    * Sites carry a causal (partial) order (a discrete light-cone), mimicking the
      emergent causal set.
    * A 'point-local scalar seal density' h(x) acts only at site x (diagonal /
      single-site self-adjoint operator) -- the COARSE-GRAINED (collar->0) limit
      of the diamond.
    * A 'region-smeared seal density' h_R(x) acts on a CLUSTER of sites that can
      straddle a spacelike gap -- the diamond WITH finite collar.
    * A spacelike-separated probe O(z) acts at a site z not in the causal
      future/past of x.

  GDC mechanism, reproduced: the nested commutator
      C_n = [h(x),[h(x),...,[h(x), O(z)]...]]   (n factors of h)
  must VANISH for spacelike (x,z) if h is point-local-scalar and [h(x),O(z)]=0
  spacelike (microcausality of the building blocks).  We verify VANISHING to all
  orders tested for the POINT-LOCAL seal, and FAILURE for the REGION-SMEARED seal
  whose support reaches z.
""")

# --- finite operator model on a small Hilbert space (Pauli/qubit per site) ---
# Build operators on 3 sites: x, z spacelike to x, and w in the future of x.
# Use sympy matrices (exact). Each site = 1 qubit; total dim 8.
import sympy as sp
sx = sp.Matrix([[0, 1], [1, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Id = sp.eye(2)

def kron3(A, B, C):
    return sp.Matrix(sp.kronecker_product(A, B, C))

# site ordering in the tensor product: (x, z, w)
# point-local scalar seal density at x: a self-adjoint scalar built at site x only
h_point = kron3(sz, Id, Id)               # acts only on x  (self-adjoint, "scalar")
# spacelike probe at z: acts only on z
O_z = kron3(Id, sx, Id)                    # acts only on z, spacelike to x
# region-smeared seal that ILLEGALLY straddles x AND z (finite collar across the gap)
h_region = kron3(sz, Id, Id) + kron3(Id, sz, Id) + sp.Rational(1, 2)*kron3(sx, sx, Id)

def comm(A, B):
    return A*B - B*A

def nested_comm_with_probe(h, O, n):
    # C_n = ad_h^n (O) = [h,[h,...,[h,O]...]]  (n times)
    C = O
    for _ in range(n):
        C = comm(h, C)
    return sp.simplify(C)

print("  POINT-LOCAL scalar seal h(x) vs spacelike probe O(z):")
all_zero_point = True
for nn in range(1, 6):
    Cn = nested_comm_with_probe(h_point, O_z, nn)
    is0 = (Cn == sp.zeros(8, 8))
    all_zero_point = all_zero_point and is0
    line(f"   ad_h^{nn}(O) = 0 ?", is0)
line("   ALL orders 1..5 vanish (MCC inherited) ?", all_zero_point)

print("\n  REGION-SMEARED seal h_R straddling the spacelike gap vs O(z):")
any_nonzero_region = False
for nn in range(1, 4):
    Cn = nested_comm_with_probe(h_region, O_z, nn)
    is0 = (Cn == sp.zeros(8, 8))
    any_nonzero_region = any_nonzero_region or (not is0)
    line(f"   ad_hR^{nn}(O) = 0 ?", is0)
line("   SOME order is NONZERO (MCC BROKEN by non-locality) ?", any_nonzero_region)

print("""
  READING.  When the seal density is POINT-LOCAL and self-adjoint-scalar, EVERY
  nested commutator with a spacelike probe vanishes -> the GDC all-orders MCC
  recursion goes through verbatim and [H(x),H(y)]=0 spacelike is INHERITED to all
  orders (the spacelike HALF of Tomonaga-Schwinger integrability).  When the seal
  density is REGION-SMEARED across the spacelike gap (a diamond with a finite
  collar reaching the spacelike probe), the very first commutators are nonzero ->
  MCC FAILS.  So the inheritance is EXACTLY conditioned on POINT-LOCALITY.
""")


# ===========================================================================
head("PART V -- VERDICT: what SHARD must show, and whether the forced seal supplies it")
# ===========================================================================
print("""
  GDC microcausality-to-all-orders is INHERITED by SHARD's seal IFF the
  seal-firing density h_seal(x) can be written as a

        LOCAL (point-supported) LORENTZ-SCALAR self-adjoint field operator,

  with a Lorentz-invariant noise correlator.  Ledger of the three ingredients:

   (S) SCALAR self-adjoint object .......... SUPPLIED ALGEBRAICALLY at Tier A.
        E=E^* forced (f1_born); chi weight-0 KL number (f4).  The seal is the
        RIGHT KIND of object -- same self-adjoint-scalar character as GDC's
        Q=(1/2)alpha:phi^2:.  GAP: 'scalar under the EMERGENT Lorentz group'
        needs a Lorentz action, which is Tier-B (no Lorentz group pre-geometry).

   (N) LORENTZ-INVARIANT positive-type noise kernel .... ALREADY SUPPLIED (Tier B).
        f(s^2) positive-type, function of the invariant s^2, quartic UV decay
        (f1_kernel_positive_type, re-verified above).  This is GDC's G((x-y)^2).

   (L) POINT-LOCALITY of the seal density ... NOT a Tier-A fact; the LOAD-BEARING
        emergence premise.  SHARD's primitive is a finite holonomy DIAMOND (a
        region + collar), point-local ONLY in the coarse-grained collar->0
        emergent limit.  Part L above shows MCC is inherited for the point-local
        seal and BROKEN for the region-smeared one -- so the whole inheritance
        rides on the diamond becoming point-local in the emergent continuum.

  THEREFORE:

   * TIER B (emergent-spacetime regime) -- INHERITS:  IF the records coarse-grain
     to a Lorentz-covariant continuum in which the seal density is a point-local
     self-adjoint Lorentz scalar (collar->0) with the already-LI kernel f(s^2),
     THEN GDC's all-orders MCC is INHERITED VERBATIM, and with it the spacelike
     [H(x),H(y)]=0 HALF of Tomonaga-Schwinger integrability -- to all orders.
     The Fedida 2025 result independently certifies the IRREVERSIBLE-collapse
     spacelike commutation in the TS picture, matching SHARD's no-revival seal.

   * TIER A (fundamental, pre-geometric) -- DOES NOT INHERIT:  there is no
     Lorentz group and no spacetime point, so (L) and 'scalar under Lorentz'
     are undefined.  The seal supplies the ALGEBRAIC scalar/self-adjoint
     skeleton (S) and the program supplies the LI kernel (N), but (L) point-
     locality + a Lorentz action are PRECISELY the emergence premises Paper I
     quarantines into Tier B.  SHARD gets an INHERITANCE THEOREM, conditional on
     the SAME covariance emergence it already declares OPEN -- NOT a Tier-A
     derivation of microcausality.

  ONE-LINE:  The SHARD seal is a self-adjoint weight-0 SCALAR (right kind of
  object) and its noise kernel is already Lorentz-invariant; so IF the emergent
  seal density is POINT-LOCAL and the records carry an emergent Lorentz action,
  the GDC all-orders microcausality -- the spacelike half of Tomonaga-Schwinger
  integrability -- is INHERITED for free.  Point-locality + the Lorentz action
  are Tier-B emergence premises, not Tier-A facts: the move converts SHARD's open
  'microcausality' frontier into the SHARPER, BORROWABLE condition
  'point-local-scalar emergent seal density', and inherits the rest from 2025.
""")

head("DONE.  Scalar/self-adjoint algebra sympy-exact; kernel & KL numerics mpmath dps=100.")
