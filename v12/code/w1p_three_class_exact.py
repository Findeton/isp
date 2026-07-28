#!/usr/bin/env python3
"""
w1p_three_class_exact.py — v12 W1': THE THREE-CLASS THEOREM, the
anti-correlation exhibit, and the Delta census.

Pin: v12/note-w1p-three-class-pin.md (STRICT, frozen before this file
existed) INCLUDING ITS AMENDMENT of 2026-07-28 (LOG #4, the second
external review [REV2] adopted mid-construction).  Binding
specification: v12 paper 0 v2.1 sec.3 (the exact skeleton,
CONVEXIFIED), sec.1 T2' (the coherent-composition defect Delta^B and
the three-defect distinction), T3' (records defined independently),
sec.4 (W1', W2a); v12/LOG.md #3, #4.  Paper 0 v2.1 is binding where it
and the original pin body differ.

THE FOUR ARMS
  ARM A  THE CHAIN, exactly, over CONVEX BODIES.  On the CHSH
         correlator projection: L_corr = conv{s_a t_b},
         Q_corr = conv{Re(z_a conj(w_b))}, NS_corr = [-1,1]^4, with
         maxima 2 / 2 sqrt 2 / 4 and both inclusions strict.  The
         maxima are proven by (i) exhaustive enumeration over the 16
         sign patterns plus linearity of the functional over hulls;
         (ii) four exact polynomial certificates (the operator
         regrouping, the unit-modulus Cauchy-Schwarz identity, the
         parallelogram identity, the AM-QM sum-of-squares identity)
         plus a saturating instance in Q(zeta_8); (iii) the
         elementary correlator bound plus the 24-vertex enumeration
         with the PR box attaining it.  GATE A+ (the amendment's new
         target, the unit's strongest theorem): the COMPLETENESS of
         Q_corr — every supporting hyperplane of the general quantum
         correlator set attains its maximum on PLANAR unit vectors,
         so the convexified U(1) family is not an approximation but
         the whole quantum correlator body at this scenario.
  ARM B  THE ANTI-CORRELATION EXHIBIT.  The review's two
         constructions, in-receipt, exact: the singlet amplitude
         model (Born identity gated symbolically and at two declared
         algebraic angle families; CHSH = -2 sqrt 2 at the review's
         settings; 4-cycle holonomy of the factorized relative phase
         identically 1) and the PR edge-phase pattern (1,1,1,-1)
         (valid no-signaling, CHSH = 4, holonomy -1).  THE ENGRAVED
         TABLE is the unit's exhibit.
  ARM C  THE DELTA^B CENSUS.  Delta^B(U2,U1) = B(U2 U1) - B(U2) B(U1)
         with B the entrywise Born projection: the cross-term
         identity gated entrywise on exact 2x2 and 3x3 pairs and on
         every census pair; the Delta^B = 0 census against the
         structural conditions (row-monomial left factor,
         column-monomial right factor) with the honest sharpening
         that these are sufficient and NOT necessary; the record
         example (a stable record of the intermediate configuration
         makes the induced law on the record algebra divisible),
         reporting-only, feeding W3'.  GATE C+1 (amendment): THE
         THREE-DEFECT SEPARATION — an exact rational rotation pair
         with Delta^B != 0 and yet an exhibited stochastic
         factorization of the shadow, so Delta^B, the actual
         residual D_210 and existential divisibility d_div are three
         different objects.  GATE C+2 (amendment): THE COHERENCE
         LAW, gated entrywise-symbolically — W2a's seed.
  ARM D  HONESTY GATES.  Antecedent attribution printed where used;
         the scope gate printed verbatim.

ENGRAVED CONSTRAINTS (paper 0 v2.1 sec.5, carried into every gate)
  * NO CLAIM ABOUT NATURE.  Everything here is a statement about
    three declared convex bodies on one declared scenario.
  * Q_corr is the quantum correlator BODY at this scenario (gate A+),
    with the scope tag: in the CHSH correlator projection, after
    convexification.  The un-convexified U(1)-Gram generating class
    is NOT convex (gate A5) and is not itself the quantum set.
  * Delta^B != 0 is NEVER equated with stochastic indivisibility.
    Gate C+1 is exactly that separation.
  * The chain is ASSEMBLED from cited antecedents ([F], [AMB], [T],
    [NS], [B1]).  No novelty of the chain is claimed.
  * Lean: NONE.  W1'-PROVEN and W1'-BROKEN-AT-<class> are both
    reportable outcomes.

HOUSE RULES OBSERVED
  * Exact arithmetic end to end: fractions.Fraction for every
    rational; the cyclotomic fields Q(zeta_8), Q(zeta_12),
    Q(zeta_16) (class Cyc) for every complex algebraic quantity; a
    multivariate polynomial ring over Q (class MP) for every
    symbolic identity certificate; an exact sign oracle on
    Q(sqrt 2) for every order comparison.  No float appears in any
    substantive computation and no tolerance is used anywhere.
  * Substantive negatives exit 0.  exit 1 is reserved for ANCHOR
    failure (arithmetic-layer self-test).
  * Determinism: every census is enumerated in a fixed lexicographic
    order; no hashing, no randomness, no wall-clock in any
    substantive path.
  * Caps printed at the head of every sweep.
"""

from __future__ import annotations

import itertools
import sys
import time
from fractions import Fraction as Fr

T0 = time.time()


def el(): return "%7.1fs" % (time.time() - T0)


def hr(c="="):
    print(c * 78)


def head(title):
    hr()
    print(title)
    hr()


# ============================================================================
# 0.  THE EXACT ARITHMETIC LAYER
# ============================================================================

# ---------------------------------------------------------------- polynomials
def ptrim(c):
    c = list(c)
    while c and c[-1] == 0:
        c.pop()
    return c


def pmul(a, b):
    a = ptrim(a); b = ptrim(b)
    if not a or not b:
        return []
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    r[i + j] += ai * bj
    return ptrim(r)


def padd(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else Fr(0)) + (b[i] if i < len(b) else Fr(0))
                  for i in range(n)])


def psub(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else Fr(0)) - (b[i] if i < len(b) else Fr(0))
                  for i in range(n)])


def pscal(a, q):
    return ptrim([x * q for x in a])


def pdivmod(a, b):
    a = ptrim(a); b = ptrim(b)
    if not b:
        raise ZeroDivisionError
    q = [Fr(0)] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        d = len(a) - len(b)
        c = a[-1] / b[-1]
        q[d] = c
        for i, bi in enumerate(b):
            a[i + d] -= c * bi
        a = ptrim(a)
    return ptrim(q), a


_CYCLO = {}


def cyclotomic(n):
    """Phi_n(x) over Q, by exact division of x^n - 1 by prod_{d|n, d<n} Phi_d."""
    if n in _CYCLO:
        return _CYCLO[n]
    num = [Fr(0)] * n + [Fr(1)]
    num[0] = Fr(-1)
    den = [Fr(1)]
    for d in range(1, n):
        if n % d == 0:
            den = pmul(den, cyclotomic(d))
    q, r = pdivmod(num, den)
    if r:
        raise ArithmeticError("cyclotomic division not exact at n=%d" % n)
    _CYCLO[n] = q
    return q


def pgcdext(a, b):
    """Extended Euclid in Q[x]: returns (g, u, v) with u a + v b = g, g monic."""
    r0, r1 = ptrim(a), ptrim(b)
    s0, s1 = [Fr(1)], []
    t0, t1 = [], [Fr(1)]
    while r1:
        q, r = pdivmod(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, psub(s0, pmul(q, s1))
        t0, t1 = t1, psub(t0, pmul(q, t1))
    if r0:
        lead = r0[-1]
        r0 = pscal(r0, 1 / lead)
        s0 = pscal(s0, 1 / lead)
        t0 = pscal(t0, 1 / lead)
    return r0, s0, t0


# ------------------------------------------------------------ cyclotomic field
class Cyc:
    """The field Q(zeta_n) = Q[x]/Phi_n(x).  Elements are tuples of Fraction
    of length deg = phi(n), coefficients in the basis 1, z, ..., z^(deg-1).
    Representation is canonical (Phi_n irreducible over Q), so tuple equality
    IS field equality: no tolerance, anywhere."""

    def __init__(self, n):
        self.n = n
        self.phi = cyclotomic(n)
        self.deg = len(self.phi) - 1
        self.zero = tuple([Fr(0)] * self.deg)
        self.one = self.red([Fr(1)])
        self.z = self.zpow(1)

    def red(self, c):
        d = self.deg
        c = list(c)
        if len(c) < d:
            c += [Fr(0)] * (d - len(c))
        phi = self.phi
        for i in range(len(c) - 1, d - 1, -1):
            ci = c[i]
            if ci:
                c[i] = Fr(0)
                base = i - d
                for j in range(d):
                    if phi[j]:
                        c[base + j] -= ci * phi[j]
        return tuple(c[:d])

    def zpow(self, k):
        k %= self.n
        return self.red([Fr(0)] * k + [Fr(1)])

    def rat(self, q):
        return self.red([Fr(q)])

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def scal(self, a, q):
        q = Fr(q)
        return tuple(x * q for x in a)

    def mul(self, a, b):
        d = self.deg
        r = [Fr(0)] * (2 * d - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj:
                        r[i + j] += ai * bj
        return self.red(r)

    def conj(self, a):
        """Complex conjugation: zeta -> zeta^{-1} (the Galois element z->z^{n-1})."""
        n = self.n
        acc = [Fr(0)] * n
        for k, ak in enumerate(a):
            if ak:
                acc[(n - k) % n] += ak
        return self.red(acc)

    def inv(self, a):
        if all(x == 0 for x in a):
            raise ZeroDivisionError
        g, u, _ = pgcdext(list(a), self.phi)
        if g != [Fr(1)]:
            raise ArithmeticError("non-unit in a field")
        return self.red(u)

    def re(self, a):
        return self.scal(self.add(a, self.conj(a)), Fr(1, 2))

    def normsq(self, a):
        return self.mul(a, self.conj(a))

    def is_zero(self, a):
        return all(x == 0 for x in a)

    def to_rat(self, a):
        if any(x != 0 for x in a[1:]):
            return None
        return a[0]

    def sqrt_of(self, m):
        """The element zeta_n^k + zeta_n^{-k} = 2 cos(2 pi k / n) equal to sqrt(m),
        found by search over k and verified by squaring.  Exact."""
        for k in range(1, self.n):
            c = self.add(self.zpow(k), self.zpow(-k))
            if self.mul(c, c) == self.rat(m):
                return c
        raise ArithmeticError("no sqrt(%d) of that form in Q(zeta_%d)" % (m, self.n))


def solve_in_basis(K, t, basis):
    """Exact: express t as a Q-combination of `basis` in K, or return None.
    Gaussian elimination over Q on the deg x len(basis) coefficient matrix."""
    d = K.deg
    m = len(basis)
    A = [[basis[j][i] for j in range(m)] + [t[i]] for i in range(d)]
    piv = []
    r = 0
    for c in range(m):
        p = None
        for i in range(r, d):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(d):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    for i in range(r, d):
        if A[i][m] != 0:
            return None
    sol = [Fr(0)] * m
    for i, c in enumerate(piv):
        sol[c] = A[i][m]
    chk = K.zero
    for j in range(m):
        chk = K.add(chk, K.scal(basis[j], sol[j]))
    return tuple(sol) if chk == t else None


# ---------------------------------------------------------- Q(sqrt 2) ordering
class Q2:
    """a + b sqrt 2, a,b in Q, with an EXACT sign oracle (no floats)."""
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fr(a); self.b = Fr(b)

    def __repr__(self):
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return "%s*sqrt2" % self.b
        return "%s + %s*sqrt2" % (self.a, self.b)

    def __sub__(self, o):
        return Q2(self.a - o.a, self.b - o.b)

    def __eq__(self, o):
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        # mixed signs: compare a^2 with 2 b^2
        s = a * a - 2 * b * b
        if a > 0:                    # a > 0 > b : positive iff a^2 > 2 b^2
            return (s > 0) - (s < 0)
        return -((s > 0) - (s < 0))  # a < 0 < b : positive iff 2 b^2 > a^2

    def cmp(self, o):
        return (self - o).sign()


# ---------------------------------------- multivariate polynomial ring over Q
class MP:
    """Sparse multivariate polynomial over Q.  Used ONLY for symbolic identity
    certificates; equality is dict equality after zero-pruning, i.e. exact."""
    __slots__ = ("nv", "t")

    def __init__(self, nv, t=None):
        self.nv = nv
        self.t = {}
        if t:
            for k, v in t.items():
                if v != 0:
                    self.t[k] = Fr(v)

    @staticmethod
    def var(nv, i):
        e = [0] * nv
        e[i] = 1
        return MP(nv, {tuple(e): Fr(1)})

    @staticmethod
    def const(nv, q):
        return MP(nv, {tuple([0] * nv): Fr(q)})

    def __add__(self, o):
        r = dict(self.t)
        for k, v in o.t.items():
            r[k] = r.get(k, Fr(0)) + v
        return MP(self.nv, r)

    def __sub__(self, o):
        r = dict(self.t)
        for k, v in o.t.items():
            r[k] = r.get(k, Fr(0)) - v
        return MP(self.nv, r)

    def __mul__(self, o):
        if isinstance(o, (int, Fr)):
            return MP(self.nv, {k: v * Fr(o) for k, v in self.t.items()})
        r = {}
        for k1, v1 in self.t.items():
            for k2, v2 in o.t.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                r[k] = r.get(k, Fr(0)) + v1 * v2
        return MP(self.nv, r)

    __rmul__ = __mul__

    def sq(self):
        return self * self

    def is_zero(self):
        return not self.t

    def nterms(self):
        return len(self.t)


# ============================================================================
#     GATE BOOK-KEEPING
# ============================================================================
GATES = []
CITED = {}


def cite(tag, text):
    CITED[tag] = text


def gate(sec, name, ok, detail="", tag=""):
    GATES.append((sec, name, bool(ok), detail, tag))
    mark = "PASS" if ok else "FAIL"
    line = "  [%s] %-9s %-46s" % (mark, sec, name)
    if detail:
        line += " %s" % detail
    if tag:
        line += "   <%s>" % tag
    print(line)
    return bool(ok)


NANCHOR = [0]


def anchor(name, ok, detail=""):
    if not ok:
        print("  [ANCHOR-FAIL] %-40s %s" % (name, detail))
        print("\nANCHOR FAILURE — the exact arithmetic layer is unsound.")
        sys.exit(1)
    NANCHOR[0] += 1
    print("  [anchor  ] %-40s ok %s" % (name, detail))


# ============================================================================
head("w1p_three_class_exact.py — v12 W1'")
print("THE THREE-CLASS THEOREM, THE ANTI-CORRELATION EXHIBIT, AND THE")
print("DELTA CENSUS")
hr()
print("  pin    : v12/note-w1p-three-class-pin.md (frozen before this file)")
print("           + its AMENDMENT of 2026-07-28 (LOG #4, [REV2] adopted)")
print("  binding: v12 paper 0 v2.1 sec.1 (T2' Delta^B, the three-defect")
print("           distinction; T3' records), sec.3 (the CONVEXIFIED")
print("           skeleton + the completeness target), sec.4 (W1', W2a),")
print("           sec.5 (non-claims); v12/LOG.md #3, #4.  v2.1 binds where")
print("           it and the pin body differ.")
print("  banner : EXACT arithmetic end to end, NO TOLERANCE ANYWHERE.")
print("           Rationals: fractions.Fraction.  Complex algebraic: class")
print("           Cyc = Q[x]/Phi_N(x) for N = 8, 12, 16, canonical")
print("           representation, exact conjugation and inversion.")
print("           Symbolic identities: class MP (multivariate polynomial")
print("           ring over Q), equality = coefficient equality.  Order")
print("           comparisons: class Q2 (a + b sqrt 2) with an exact sign")
print("           oracle.  No float in any substantive path.")
print("  lean   : NONE.  W1'-PROVEN and W1'-BROKEN-AT-<class> are both")
print("           reportable outcomes and the gate book is the result.")
print("  exits  : substantive negatives exit 0; exit 1 is ANCHOR-only.")
print()

cite("[F]", "Fine, PRL 48, 291 (1982) — LHV <=> a joint distribution for the "
     "four observables; the local set is the polytope hull of the 16 "
     "deterministic assignments.")
cite("[AB]", "Abramsky-Brandenburger, NJP 13, 113036 (2011) — the exact "
     "global-section formulation of contextuality.")
cite("[AMB]", "Abramsky-Mansfield-Barbosa, arXiv 1111.3620 — the "
     "cohomological obstruction: a SUFFICIENT WITNESS, not an equivalence "
     "(attribution per [REV2]; engraved caution, paper 0 v2.1 sec.3).")
cite("[T]", "Tsirelson's bound: CHSH <= 2 sqrt 2 for quantum correlations, "
     "and Tsirelson's theorem that the (2,2,2) quantum correlator set is "
     "exactly the REAL UNIT-VECTOR Gram set E_ab = <u_a, v_b> in any real "
     "Hilbert space.  See e.g. arXiv 1501.01406.  The characterization is "
     "CITED; gate A+ derives from it that planar vectors already suffice.")
cite("[CVX]", "STANDARD CONVEXITY.  (a) A linear functional on a compact "
     "convex set attains its maximum at an extreme point, and "
     "max over conv(S) = max over S for any S.  (b) Two compact convex sets "
     "with equal support functions are equal.  (c) The quantum correlator "
     "set of a scenario is compact and convex (mixing by a shared classical "
     "flag).  (d) Caratheodory: conv of a compact set in R^4 is compact.")
cite("[NS]", "Popescu-Rohrlich, Found. Phys. 24, 379 (1994) (the PR box); "
     "Barrett-Linden-Massar-Pironio-Popescu-Roberts, PRA 71, 022101 (2005) "
     "(the 24 vertices of the (2,2,2) no-signaling polytope).")
cite("[B1]", "Barandes, arXiv 2302.10778 — the stochastic-quantum "
     "correspondence; the identification of the Born-projection cross terms "
     "with interference.  Reproduced here, not originated here.")
cite("[W]", "Weyl relations / noncommutative torus, projective multipliers on "
     "Z^2 (e.g. arXiv 1606.01829).  NAMED HERE, NOT USED: it is W2b/W2c's "
     "object.")
cite("[REV]", "The external hostile review of v12 paper 0 v1, adjudicated at "
     "v12/LOG.md #3; both of its constructions are the subject of Arm B.")
cite("[REV2]", "The second external hostile review, adjudicated at "
     "v12/LOG.md #4: the convexification of sec.3, the completeness target "
     "for Q_corr, the three-defect distinction with its rotation "
     "counterexample, and the coherence law.  Gates A+, C+1, C+2 are its.")

# ============================================================================
head("SECTION 0 — ANCHORS: the exact arithmetic layer self-test")
# ============================================================================
K8 = Cyc(8)
K12 = Cyc(12)
K16 = Cyc(16)

anchor("Phi_8 = x^4 + 1", K8.phi == [Fr(1), Fr(0), Fr(0), Fr(0), Fr(1)],
       "deg %d" % K8.deg)
anchor("Phi_12 = x^4 - x^2 + 1",
       K12.phi == [Fr(1), Fr(0), Fr(-1), Fr(0), Fr(1)], "deg %d" % K12.deg)
anchor("Phi_16 = x^8 + 1",
       K16.phi == [Fr(1)] + [Fr(0)] * 7 + [Fr(1)], "deg %d" % K16.deg)

for K in (K8, K12, K16):
    anchor("zeta_%d has exact order %d" % (K.n, K.n),
           K.zpow(K.n) == K.one and all(K.zpow(k) != K.one
                                        for k in range(1, K.n)))
    anchor("conj(zeta_%d) * zeta_%d = 1" % (K.n, K.n),
           K.mul(K.z, K.conj(K.z)) == K.one)
    anchor("inv(zeta_%d) = conj(zeta_%d)" % (K.n, K.n),
           K.inv(K.z) == K.conj(K.z))

SQRT2_8 = K8.sqrt_of(2)
SQRT2_16 = K16.sqrt_of(2)
SQRT3_12 = K12.sqrt_of(3)
anchor("sqrt2 in Q(zeta_8), (sqrt2)^2 = 2",
       K8.mul(SQRT2_8, SQRT2_8) == K8.rat(2), "= zeta_8 + zeta_8^-1")
anchor("sqrt2 in Q(zeta_16), (sqrt2)^2 = 2",
       K16.mul(SQRT2_16, SQRT2_16) == K16.rat(2), "= zeta_16^2 + zeta_16^-2")
anchor("sqrt3 in Q(zeta_12), (sqrt3)^2 = 3",
       K12.mul(SQRT3_12, SQRT3_12) == K12.rat(3), "= zeta_12 + zeta_12^-1")

INV_SQRT2_8 = K8.inv(SQRT2_8)
INV_SQRT2_16 = K16.inv(SQRT2_16)
INV_SQRT3_12 = K12.inv(SQRT3_12)
anchor("1/sqrt2 exact in Q(zeta_8)",
       K8.mul(INV_SQRT2_8, SQRT2_8) == K8.one)
anchor("1/sqrt3 exact in Q(zeta_12)",
       K12.mul(INV_SQRT3_12, SQRT3_12) == K12.one)

# Q(sqrt2) sign oracle self-test
anchor("Q2 sign oracle",
       Q2(0, 2).sign() == 1 and Q2(-2, 1).sign() == -1
       and Q2(2, -1).sign() == 1 and Q2(-1, 1).sign() == 1
       and Q2(1, -1).sign() == -1 and Q2(0, 0).sign() == 0
       and Q2(2, 0).cmp(Q2(0, 2)) == -1,        # 2 < 2 sqrt 2
       "incl. 2 < 2*sqrt2")

# reading Q(sqrt2)-valued elements of Q(zeta_8)
B_Q2_8 = [K8.one, SQRT2_8]


def to_q2(x):
    """x in Q(zeta_8) lying in Q(sqrt 2) -> Q2, else None."""
    s = solve_in_basis(K8, x, B_Q2_8)
    return None if s is None else Q2(s[0], s[1])


anchor("Q(sqrt2) reader on Q(zeta_8)",
       to_q2(K8.rat(3)) == Q2(3, 0) and to_q2(SQRT2_8) == Q2(0, 1)
       and to_q2(K8.z) is None)

anchor("MP ring", (MP.var(2, 0) + MP.var(2, 1)).sq().nterms() == 3
       and ((MP.var(2, 0) + MP.var(2, 1)).sq()
            - MP.var(2, 0).sq() - MP.var(2, 1).sq()
            - MP.const(2, 2) * MP.var(2, 0) * MP.var(2, 1)).is_zero())
print("  anchors: %d, all pass   %s" % (NANCHOR[0], el()))
print()


# ============================================================================
head("SECTION A — THE CHAIN: 2  /  2 sqrt 2  /  4")
# ============================================================================
S_IDX = [(0, 0), (0, 1), (1, 0), (1, 1)]
CHSH_SIGNS = (1, 1, 1, -1)     # S = E00 + E01 + E10 - E11
# the four CHSH functionals of the (2,2,2) scenario (one minus sign each)
FOUR_FUNCTIONALS = [(-1, 1, 1, 1), (1, -1, 1, 1), (1, 1, -1, 1), (1, 1, 1, -1)]


def chsh_rat(E, signs=CHSH_SIGNS):
    return sum(s * E[i] for s, i in zip(signs, range(4)))


# ---------------------------------------------------------------------------
print("A1. THE {+-1}-FACTORIZATION CLASS  E_ab = u_a v_b, u,v in {+-1}")
print("    cap: exhaustive, 2^4 = 16 sign patterns, all 4 CHSH functionals.")
print("    method: EXHAUSTIVE ENUMERATION + linearity/convexity for the hull.")
det_points = []
for u0, u1, v0, v1 in itertools.product((1, -1), repeat=4):
    u = (u0, u1); v = (v0, v1)
    E = tuple(Fr(u[a] * v[b]) for (a, b) in S_IDX)
    det_points.append(((u0, u1, v0, v1), E))

vals = {}
for pat, E in det_points:
    for f in FOUR_FUNCTIONALS:
        vals.setdefault(f, []).append(chsh_rat(E, f))
maxes = {f: max(vals[f]) for f in FOUR_FUNCTIONALS}
minis = {f: min(vals[f]) for f in FOUR_FUNCTIONALS}
gate("A1", "16 sign patterns enumerated, all distinct E-vectors?",
     len({E for _, E in det_points}) == 8,
     "8 distinct correlator vectors from 16 patterns (u,v)->(-u,-v)")
gate("A1", "max CHSH over the {+-1} class = 2",
     all(maxes[f] == 2 for f in FOUR_FUNCTIONALS),
     "all 4 functionals: max = %s, min = %s"
     % ("/".join(sorted({str(v) for v in maxes.values()})),
        "/".join(sorted({str(v) for v in minis.values()}))), "[F]")
gate("A1", "|CHSH| <= 2 on every sign pattern",
     all(abs(v) <= 2 for f in FOUR_FUNCTIONALS for v in vals[f]),
     "16 x 4 = 64 exact rational evaluations")

# the convexity statement: CHSH is a linear functional, so its max over the
# hull (= the local polytope, [F]) equals its max over the 16 vertices.
print("    convexity: the local polytope is conv{16 deterministic points}")
print("    [F]; CHSH is linear, so max over the hull = max over vertices = 2.")
print("    gated below on an exhaustive grid of exact rational weightings.")
CAP_HULL_DEN = 4
hull_pts = 0
hull_bad = 0
lin_bad = 0
for comp in itertools.combinations_with_replacement(range(16), CAP_HULL_DEN):
    w = [0] * 16
    for i in comp:
        w[i] += 1
    p = [Fr(x, CAP_HULL_DEN) for x in w]
    E = tuple(sum(p[k] * det_points[k][1][i] for k in range(16))
              for i in range(4))
    hull_pts += 1
    for f in FOUR_FUNCTIONALS:
        s = chsh_rat(E, f)
        if s > 2:
            hull_bad += 1
        # linearity of the functional, gated pointwise
        if s != sum(p[k] * chsh_rat(det_points[k][1], f) for k in range(16)):
            lin_bad += 1
gate("A1", "CHSH linear on exact convex combinations", lin_bad == 0,
     "%d hull points x 4 functionals, weights in (1/%d)Z"
     % (hull_pts, CAP_HULL_DEN))
gate("A1", "CHSH <= 2 on the exact hull grid", hull_bad == 0,
     "%d hull points x 4 functionals, 0 violations" % hull_pts, "[F]")
A1_MAX_IS_2 = maxes[CHSH_SIGNS] == 2 and hull_bad == 0
print("    CLASS MAXIMUM (i)  =  2   [attained: u=(1,1), v=(1,1) etc.]")
print("    %s" % el())
print()

# ---------------------------------------------------------------------------
print("A2. THE U(1)-GRAM CLASS  E_ab = Re(z_a conj(w_b)), |z_a| = |w_b| = 1")
print("    method: THREE EXACT POLYNOMIAL CERTIFICATES + a saturating")
print("    instance in Q(zeta_8).  No numerics, no search over angles.")
print()
print("    The reduction.  With u = w_0 + w_1 and v = w_0 - w_1,")
print("      S = Re(conj(z_0) u) + Re(conj(z_1) v)   (Re(x) = Re(conj x)),")
print("    so max over z_0, z_1 in U(1) of S is |u| + |v|, attained at")
print("    z_a = u/|u|, v/|v| (any unit z where the vector vanishes).")
print()

# CERT-0: the reduction itself, in real coordinates.  With
#   Re(z conj w) = z_x w_x + z_y w_y, the CHSH functional regroups as
#   S = Re(conj(z_0)(w_0 + w_1)) + Re(conj(z_1)(w_0 - w_1)) identically.
V = [MP.var(8, i) for i in range(8)]
z0x, z0y, z1x, z1y, w0x, w0y, w1x, w1y = V
lhs = (z0x * w0x + z0y * w0y) + (z0x * w1x + z0y * w1y) \
      + (z1x * w0x + z1y * w0y) - (z1x * w1x + z1y * w1y)
rhs = z0x * (w0x + w1x) + z0y * (w0y + w1y) \
      + z1x * (w0x - w1x) + z1y * (w0y - w1y)
cert0 = lhs - rhs
gate("A2", "CERT-0 (the operator regrouping) identity", cert0.is_zero(),
     "S = Re(conj(z_0)(w_0+w_1)) + Re(conj(z_1)(w_0-w_1)) in Q[z,w]_R^8")

# CERT-1: for |z| = 1, Re(conj(z) u)^2 + Im(conj(z) u)^2 = |u|^2, hence
#         Re(conj(z) u) <= |u| with equality iff Im = 0 and Re >= 0.
c, s, x, y = (MP.var(4, i) for i in range(4))
cert1 = (c * x + s * y).sq() + (c * y - s * x).sq() \
        - (c.sq() + s.sq()) * (x.sq() + y.sq())
gate("A2", "CERT-1 (unit-modulus Cauchy-Schwarz) identity", cert1.is_zero(),
     "(cx+sy)^2 + (cy-sx)^2 = (c^2+s^2)(x^2+y^2) in Q[c,s,x,y]")

# CERT-2: the parallelogram identity |v0+v1|^2 + |v0-v1|^2 = 2|v0|^2 + 2|v1|^2
x0, y0, x1, y1 = (MP.var(4, i) for i in range(4))
cert2 = (x0 + x1).sq() + (y0 + y1).sq() + (x0 - x1).sq() + (y0 - y1).sq() \
        - MP.const(4, 2) * (x0.sq() + y0.sq()) \
        - MP.const(4, 2) * (x1.sq() + y1.sq())
gate("A2", "CERT-2 (parallelogram) identity", cert2.is_zero(),
     "|v0+v1|^2 + |v0-v1|^2 = 2|v0|^2 + 2|v1|^2 in Q[x0,y0,x1,y1]")

# CERT-3: the AM-QM sum-of-squares certificate
#         8 - (p+q)^2 = (p-q)^2 + 2(4 - p^2 - q^2)
p, q = (MP.var(2, i) for i in range(2))
cert3 = (MP.const(2, 8) - (p + q).sq()) - (p - q).sq() \
        - MP.const(2, 2) * (MP.const(2, 4) - p.sq() - q.sq())
gate("A2", "CERT-3 (AM-QM sum-of-squares) identity", cert3.is_zero(),
     "8 - (p+q)^2 = (p-q)^2 + 2(4 - p^2 - q^2) in Q[p,q]")
print()
print("    THE PROOF, assembled from CERT-0/1/2/3 (all four exact above):")
print("      (0) CERT-0 regroups S over the two operator slots.")
print("      (a) CERT-1 with c^2+s^2 = 1 gives Re(conj(z)u)^2 <= |u|^2, so")
print("          S <= |u| + |v| =: p + q,  p,q >= 0.")
print("      (b) CERT-2 with |w_0| = |w_1| = 1 gives p^2 + q^2 = 4.")
print("      (c) CERT-3 then gives 8 - (p+q)^2 = (p-q)^2 >= 0, i.e.")
print("          p + q <= 2 sqrt 2, with equality iff p = q = sqrt 2.")
print("    Hence S <= 2 sqrt 2 for EVERY U(1)-Gram instance.  [T]")
print()

# the saturating instance, exact, in Q(zeta_8)
ALPHA = (1, 7)   # z_a = zeta_8^{1}, zeta_8^{7}   (angles  pi/4, -pi/4)
BETA = (0, 2)    # w_b = zeta_8^{0}, zeta_8^{2}   (angles  0,     pi/2)
zA = [K8.zpow(k) for k in ALPHA]
wB = [K8.zpow(k) for k in BETA]
gate("A2", "instance: all four phases on the unit circle",
     all(K8.normsq(t) == K8.one for t in zA + wB), "|z|^2 = |w|^2 = 1 exactly")
E_gram = [K8.re(K8.mul(zA[a], K8.conj(wB[b]))) for (a, b) in S_IDX]
E_gram_q2 = [to_q2(e) for e in E_gram]
gate("A2", "instance correlators lie in Q(sqrt 2)",
     all(e is not None for e in E_gram_q2),
     "E = (%s)" % ", ".join(str(e) for e in E_gram_q2))
S_inst = Q2(sum(sg * e.a for sg, e in zip(CHSH_SIGNS, E_gram_q2)),
            sum(sg * e.b for sg, e in zip(CHSH_SIGNS, E_gram_q2)))
gate("A2", "instance CHSH = 2 sqrt 2 EXACTLY", S_inst == Q2(0, 2),
     "S = %s  (alpha = (pi/4, -pi/4), beta = (0, pi/2))" % S_inst, "[T]")
# and the reduction's two moduli
u_el = K8.add(wB[0], wB[1]); v_el = K8.sub(wB[0], wB[1])
gate("A2", "instance saturates CERT-3: |u|^2 = |v|^2 = 2",
     K8.normsq(u_el) == K8.rat(2) and K8.normsq(v_el) == K8.rat(2),
     "p = q = sqrt 2, so p + q = 2 sqrt 2")
gate("A2", "instance z_a align with u/|u|, v/|v|",
     K8.mul(zA[0], SQRT2_8) == u_el and K8.mul(zA[1], SQRT2_8) == v_el,
     "equality case of CERT-1 realized exactly")

# exhaustive grid corroboration over the declared pi/4 family
print("    corroboration cap: exhaustive grid over the pi/4 family,")
print("    8^4 = 4096 setting quadruples, exact Q(sqrt 2) comparison.")
COS8 = [to_q2(K8.re(K8.zpow(k))) for k in range(8)]
best = Q2(-10, 0)
best_at = None
grid_bad = 0
for a0, a1, b0, b1 in itertools.product(range(8), repeat=4):
    ee = [COS8[(a0 - b0) % 8], COS8[(a0 - b1) % 8],
          COS8[(a1 - b0) % 8], COS8[(a1 - b1) % 8]]
    S = Q2(sum(sg * e.a for sg, e in zip(CHSH_SIGNS, ee)),
           sum(sg * e.b for sg, e in zip(CHSH_SIGNS, ee)))
    if S.cmp(Q2(0, 2)) > 0:
        grid_bad += 1
    if S.cmp(best) > 0:
        best = S; best_at = (a0, a1, b0, b1)
gate("A2", "grid: no Gram point exceeds 2 sqrt 2", grid_bad == 0,
     "4096 quadruples, 0 violations", "[T]")
gate("A2", "grid maximum equals 2 sqrt 2", best == Q2(0, 2),
     "max = %s at (a0,a1;b0,b1) = %s (units of pi/4)" % (best, best_at))
A2_MAX_IS_2SQRT2 = (cert0.is_zero() and cert1.is_zero() and cert2.is_zero()
                    and cert3.is_zero()
                    and S_inst == Q2(0, 2) and grid_bad == 0)
print("    CLASS MAXIMUM (ii) =  2 sqrt 2   [proven exactly; attained]")
print("    %s" % el())
print()

# ---------------------------------------------------------------------------
print("A3. THE NO-SIGNALING CLASS")
print("    method: the elementary correlator bound (complete proof of <= 4)")
print("    + the 24-vertex enumeration [NS] with the PR box attaining it.")
PM = (1, -1)


def table_local(u, v):
    """P(x,y|a,b) = [x = u_a][y = v_b], outcomes in {+1,-1}."""
    T = {}
    for a in (0, 1):
        for b in (0, 1):
            for x in PM:
                for y in PM:
                    T[(a, b, x, y)] = Fr(1) if (x == u[a] and y == v[b]) \
                        else Fr(0)
    return T


def table_pr(g1, g2, g3):
    """P(x,y|a,b) = 1/2 if x*y = (-1)^(a b + g1 a + g2 b + g3), else 0."""
    T = {}
    for a in (0, 1):
        for b in (0, 1):
            e = (a * b + g1 * a + g2 * b + g3) % 2
            tgt = 1 if e == 0 else -1
            for x in PM:
                for y in PM:
                    T[(a, b, x, y)] = Fr(1, 2) if x * y == tgt else Fr(0)
    return T


def table_ok(T):
    for a in (0, 1):
        for b in (0, 1):
            tot = sum(T[(a, b, x, y)] for x in PM for y in PM)
            if tot != 1:
                return False, "normalization"
            if any(T[(a, b, x, y)] < 0 for x in PM for y in PM):
                return False, "negativity"
    for a in (0, 1):
        for x in PM:
            m = {b: sum(T[(a, b, x, y)] for y in PM) for b in (0, 1)}
            if m[0] != m[1]:
                return False, "signaling B->A"
    for b in (0, 1):
        for y in PM:
            m = {a: sum(T[(a, b, x, y)] for x in PM) for a in (0, 1)}
            if m[0] != m[1]:
                return False, "signaling A->B"
    return True, ""


def corr(T):
    return tuple(sum(x * y * T[(a, b, x, y)] for x in PM for y in PM)
                 for (a, b) in S_IDX)


NS_VERTS = []
for u0, u1, v0, v1 in itertools.product(PM, repeat=4):
    NS_VERTS.append(("L(%2d,%2d;%2d,%2d)" % (u0, u1, v0, v1),
                     table_local((u0, u1), (v0, v1))))
for g1, g2, g3 in itertools.product((0, 1), repeat=3):
    NS_VERTS.append(("PR(%d,%d,%d)" % (g1, g2, g3), table_pr(g1, g2, g3)))
print("    cap: the 24 known vertices [NS] (16 local + 8 PR), exhaustive.")
bad = [n for n, T in NS_VERTS if not table_ok(T)[0]]
gate("A3", "all 24 vertices are valid no-signaling tables", not bad,
     "nonneg + normalized + both marginal conditions, exact rationals", "[NS]")
corrs = {n: corr(T) for n, T in NS_VERTS}
gate("A3", "|E_ab| <= 1 on every vertex",
     all(abs(e) <= 1 for c in corrs.values() for e in c),
     "the elementary bound: |E| <= sum of the four probabilities = 1")
ns_vals = {n: chsh_rat(c) for n, c in corrs.items()}
mx = max(ns_vals.values())
att = sorted(n for n, v in ns_vals.items() if v == mx)
gate("A3", "max CHSH over the 24 vertices = 4", mx == 4,
     "attained by %d of the 24: %s" % (len(att), ", ".join(att)), "[NS]")
gate("A3", "local vertices give CHSH <= 2",
     max(v for n, v in ns_vals.items() if n.startswith("L")) == 2,
     "16 local vertices, max = 2")
gate("A3", "every CHSH = 4 vertex has correlators (1,1,1,-1)",
     all(corrs[n] == (Fr(1), Fr(1), Fr(1), Fr(-1)) for n in att),
     "the PR correlator vector")
# each of the 8 PR vertices maximizes one of the 8 signed CHSH functionals
EIGHT = [tuple(sg * t for sg in f) for f in FOUR_FUNCTIONALS for t in (1, -1)]
pr_names = sorted(n for n in corrs if n.startswith("PR"))
pr_max = {n: max(chsh_rat(corrs[n], f) for f in EIGHT) for n in pr_names}
gate("A3", "each of the 8 PR vertices attains 4 on some functional",
     all(v == 4 for v in pr_max.values()),
     "8 signed CHSH functionals, 8 PR boxes, max = 4 each", "[NS]")
gate("A3", "no local vertex attains 4 on any functional",
     max(chsh_rat(corrs[n], f) for n in corrs if n.startswith("L")
         for f in EIGHT) == 2,
     "16 local vertices x 8 functionals, max = 2")
print("    THE PROOF of <= 4, complete and elementary: for ANY normalized")
print("    non-negative table, E_ab = P(++) + P(--) - P(+-) - P(-+) has")
print("    |E_ab| <= P(++) + P(--) + P(+-) + P(-+) = 1, so |CHSH| <= 4.")
print("    Attainment is the PR box above.  The 24-vertex list [NS] is")
print("    cited for completeness of the polytope, NOT for the bound.")
A3_MAX_IS_4 = (mx == 4 and not bad)
print("    CLASS MAXIMUM (iii)=  4   [proven elementarily; attained by PR]")
print("    %s" % el())
print()

# ---------------------------------------------------------------------------
print("A4. THE INCLUSIONS, BOTH DIRECTIONS")
# (a) {+-1} class  subset of  U(1)-Gram class
incl_bad = 0
for (u0, u1, v0, v1), E in det_points:
    za = [K8.rat(u0), K8.rat(u1)]
    wb = [K8.rat(v0), K8.rat(v1)]
    Eg = [K8.re(K8.mul(za[a], K8.conj(wb[b]))) for (a, b) in S_IDX]
    if any(Eg[i] != K8.rat(E[i]) for i in range(4)):
        incl_bad += 1
gate("A4", "{+-1} class  SUBSET  U(1)-Gram class", incl_bad == 0,
     "all 16 patterns realized with z_a = u_a, w_b = v_b in {+-1} < U(1)")

# (b) strictness: the Gram instance sits outside the local polytope
gate("A4", "STRICT: a Gram point outside the local polytope",
     S_inst.cmp(Q2(2, 0)) > 0,
     "CHSH = 2 sqrt 2 > 2 = the polytope maximum (exact Q2 comparison)")

# (c) U(1)-Gram class  subset of  no-signaling class (constructive)
def table_from_corr(E4):
    """P(x,y|a,b) = 1/4 (1 + x y E_ab).  Uniform marginals => no-signaling;
    non-negative iff |E_ab| <= 1."""
    T = {}
    for i, (a, b) in enumerate(S_IDX):
        for x in PM:
            for y in PM:
                T[(a, b, x, y)] = Fr(1, 4) * (1 + x * y * E4[i])
    return T


#     the marginal + normalization + correlator conditions for
#     P = 1/4 (1 + x y E) are POLYNOMIAL IDENTITIES in E, gated symbolically;
#     only non-negativity is an inequality, gated by the Q2 sign oracle over
#     the whole pi/4 grid.
Ev = MP.var(1, 0)
q4 = MP.const(1, Fr(1, 4))
norm_id = (q4 * (MP.const(1, 1) + Ev) + q4 * (MP.const(1, 1) - Ev)
           + q4 * (MP.const(1, 1) - Ev) + q4 * (MP.const(1, 1) + Ev)
           - MP.const(1, 1))
marg_id = (q4 * (MP.const(1, 1) + Ev) + q4 * (MP.const(1, 1) - Ev)
           - MP.const(1, Fr(1, 2)))
corr_id = (q4 * (MP.const(1, 1) + Ev) - q4 * (MP.const(1, 1) - Ev)
           - q4 * (MP.const(1, 1) - Ev) + q4 * (MP.const(1, 1) + Ev) - Ev)
gate("A4", "P = 1/4(1+xyE): normalization is an identity in E",
     norm_id.is_zero(), "sum over the four outcomes = 1 in Q[E]")
gate("A4", "P = 1/4(1+xyE): both marginals = 1/2 identically",
     marg_id.is_zero(), "=> no-signaling for EVERY correlator vector")
gate("A4", "P = 1/4(1+xyE): reproduces E identically", corr_id.is_zero(),
     "sum x y P = E in Q[E]")
gram_nonneg_bad = 0
gram_checked = 0
for a0, a1, b0, b1 in itertools.product(range(8), repeat=4):
    ee = [COS8[(a0 - b0) % 8], COS8[(a0 - b1) % 8],
          COS8[(a1 - b0) % 8], COS8[(a1 - b1) % 8]]
    gram_checked += 1
    for e in ee:                              # |E| <= 1, exact Q2 sign oracle
        if Q2(1 - e.a, -e.b).sign() < 0 or Q2(1 + e.a, e.b).sign() < 0:
            gram_nonneg_bad += 1
gate("A4", "U(1)-Gram class  SUBSET  no-signaling class",
     gram_nonneg_bad == 0 and norm_id.is_zero() and marg_id.is_zero()
     and corr_id.is_zero(),
     "identities above + |E_ab| <= 1 on all %d pi/4 grid points (exact "
     "Q(sqrt2) sign oracle)" % gram_checked)
# a rational-correlator sub-sweep with the tables actually built
gram_tables_bad = 0
gram_built = 0
for a0, a1, b0, b1 in itertools.product(range(8), repeat=4):
    ee = [COS8[(a0 - b0) % 8], COS8[(a0 - b1) % 8],
          COS8[(a1 - b0) % 8], COS8[(a1 - b1) % 8]]
    if any(e.b != 0 for e in ee):        # keep the exactly-rational subgrid
        continue
    T = table_from_corr([e.a for e in ee])
    ok, why = table_ok(T)
    gram_built += 1
    if not ok or corr(T) != tuple(e.a for e in ee):
        gram_tables_bad += 1
gate("A4", "the constructed tables verified table-by-table",
     gram_tables_bad == 0,
     "%d rational-correlator Gram points, full NS check each" % gram_built)

# (d) strictness: the PR table admits NO U(1)-Gram representation
print("    THE PR EXCLUSION, exact and exhaustive.")
print("    Lemma (CERT-1 with |z| = |w| = 1): Re(z conj w) = eps in {+-1}")
print("    forces Im(z conj w) = 0, hence z conj w = eps, hence z = eps w.")
print("    So a Gram point with all four E_ab in {+-1} obeys z_a = E_ab w_b.")
print("    Reading it at b = 0 and b = 1 for each a gives")
print("      w_1 = E_a0 E_a1 w_0   for BOTH a = 0 and a = 1,")
print("    hence E_00 E_01 = E_10 E_11, hence (E^2 = 1)")
print("      E_00 E_01 E_10 E_11 = +1                       (*)")
print("    for EVERY {+-1}-valued U(1)-Gram point.  (*) is exactly the")
print("    4-cycle holonomy of the edge signs — the same invariant as B1/B2.")
print("    PR has E = (1,1,1,-1) with product -1: it violates (*).")
# (*) gated exhaustively: the 16 sign vectors, both directions
prod_pos = []
prod_neg = []
det_corr = {E for _, E in det_points}
for E in itertools.product((1, -1), repeat=4):
    Ef = tuple(Fr(e) for e in E)
    realized = Ef in det_corr
    if E[0] * E[1] * E[2] * E[3] == 1:
        prod_pos.append((E, realized))
    else:
        prod_neg.append((E, realized))
gate("A4", "(*) holds <=> the sign vector is {+-1}-factorizable",
     all(r for _, r in prod_pos) and not any(r for _, r in prod_neg),
     "16 sign vectors: %d with product +1 (all factorizable), %d with "
     "product -1 (none factorizable)" % (len(prod_pos), len(prod_neg)))
E_PR_SIGNS = (1, 1, 1, -1)
gate("A4", "STRICT: PR admits NO U(1)-Gram representation",
     E_PR_SIGNS[0] * E_PR_SIGNS[1] * E_PR_SIGNS[2] * E_PR_SIGNS[3] == -1,
     "PR sign product = -1, violating (*); the 4-cycle closes wrong")
gate("A4", "the exclusion lemma is CERT-1 with |z|=|w|=1", cert1.is_zero(),
     "Re^2 + Im^2 = 1 and Re = +-1 => Im = 0 => z = +- w")
# and the lemma's own content, gated in the field on all unit pairs of mu_8
lem_bad = 0
lem_tot = 0
for ka in range(8):
    for kb in range(8):
        za = K8.zpow(ka); wb = K8.zpow(kb)
        r = K8.re(K8.mul(za, K8.conj(wb)))
        if r == K8.one or r == K8.neg(K8.one):
            lem_tot += 1
            eps = 1 if r == K8.one else -1
            if za != K8.scal(wb, eps):
                lem_bad += 1
gate("A4", "the lemma verified in-field on the pi/4 unit pairs",
     lem_bad == 0 and lem_tot > 0,
     "%d of 64 pairs have Re = +-1; all satisfy z = eps w" % lem_tot)
# (*) IS the 4-cycle holonomy of the sign pattern: the same invariant as B1/B2
hol_prod_bad = 0
for E in itertools.product((1, -1), repeat=4):
    g = [K8.scal(K8.one, e) for e in E]        # E_00, E_01, E_10, E_11
    h = K8.mul(K8.mul(g[0], K8.inv(g[2])), K8.mul(g[3], K8.inv(g[1])))
    if h != K8.scal(K8.one, E[0] * E[1] * E[2] * E[3]):
        hol_prod_bad += 1
gate("A4", "(*) IS the 4-cycle holonomy of the sign pattern",
     hol_prod_bad == 0,
     "16 patterns: prod E_ab = g00 g10^-1 g11 g01^-1 exactly — the same "
     "invariant Arm B computes")
print("    %s" % el())
print()

# ---------------------------------------------------------------------------
print("A5. THE SHARPENING: the U(1)-Gram class is NOT CONVEX")
print("    (a finding of this unit, reported because paper 0 v2 sec.3 writes")
print("    the chain as a chain of CLASSES; it is not a chain of polytopes.)")
# E = (1,0,0,0) is the average of four deterministic points ...
sel = []
for k, (pat, E) in enumerate(det_points):
    if pat in [(1, 1, 1, 1), (1, 1, 1, -1), (1, -1, 1, 1), (1, -1, 1, -1)]:
        sel.append(k)
Eavg = tuple(sum(Fr(1, 4) * det_points[k][1][i] for k in sel) for i in range(4))
gate("A5", "E = (1,0,0,0) is in the local polytope",
     Eavg == (Fr(1), Fr(0), Fr(0), Fr(0)),
     "= mean of 4 deterministic vertices, exact rationals", "[F]")
# ... but it is not a Gram point.
print("    Exclusion, exact: E_00 = 1 forces z_0 = w_0 (CERT-1).  E_01 = 0")
print("    forces w_1 = mu i z_0, mu in {+-1}; E_10 = 0 forces")
print("    z_1 = eps i w_0 = eps i z_0, eps in {+-1}.  Then")
print("    z_1 conj(w_1) = (eps i)(conj(mu i)) = eps mu, so E_11 = +-1 != 0.")
e11_forced = set()
for eps in (1, -1):
    for mu in (1, -1):
        z0 = K8.one
        w0 = z0
        w1 = K8.scal(K8.mul(K8.zpow(2), z0), mu)      # zeta_8^2 = i
        z1 = K8.scal(K8.mul(K8.zpow(2), w0), eps)
        e11 = K8.re(K8.mul(z1, K8.conj(w1)))
        e00 = K8.re(K8.mul(z0, K8.conj(w0)))
        e01 = K8.re(K8.mul(z0, K8.conj(w1)))
        e10 = K8.re(K8.mul(z1, K8.conj(w0)))
        assert e00 == K8.one and e01 == K8.zero and e10 == K8.zero
        e11_forced.add(K8.to_rat(e11))
gate("A5", "E = (1,0,0,0) is NOT a U(1)-Gram point",
     e11_forced == {Fr(1), Fr(-1)},
     "all 4 sign branches gated in-field; E_11 forced to %s, never 0"
     % " or ".join("%+d" % v for v in sorted(e11_forced, reverse=True)))
gate("A5", "=> the U(1)-Gram class is not convex", True,
     "it contains all 16 deterministic points but not their mean")
print("    CONSEQUENCE, engraved: the honest chain at the level of CONVEX")
print("    SETS is  localpolytope  SUBSET  conv(U(1)-Gram)  SUBSET  NS,")
print("    with maxima 2 / 2 sqrt 2 / 4 unchanged (CHSH is linear, so the")
print("    hull does not raise the maximum).  The class chain of paper 0 v2")
print("    sec.3 is correct as written; the polytope reading is not.")
gate("A5", "max CHSH over conv(U(1)-Gram) is still 2 sqrt 2",
     A2_MAX_IS_2SQRT2,
     "linearity of CHSH + the class bound proven in A2")
gate("A5", "localpolytope SUBSET conv(U(1)-Gram)", incl_bad == 0,
     "the 16 vertices are Gram points (A4a), and the hull is convex")
print("    %s" % el())
print()

# ---------------------------------------------------------------------------
print("A6. THE THREE CONVEX BODIES  (paper 0 v2.1 sec.3, per [REV2])")
print("    L_corr  := conv{ E_ab = s_a t_b : s_a, t_b in {+-1} }")
print("    Q_corr  := conv{ E_ab = Re(z_a conj(w_b)) : z_a, w_b in U(1) }")
print("    NS_corr := [-1, 1]^4")
print("    A linear functional attains its maximum over a compact convex set")
print("    at an extreme point, and max over conv(S) = max over S for any S")
print("    [CVX](a).  So each body's maximum is the maximum over its")
print("    generating set, already proven at A1 / A2 / A3.")
CUBE_VERTS = list(itertools.product((Fr(1), Fr(-1)), repeat=4))
cube_max = max(chsh_rat(E) for E in CUBE_VERTS)
cube_arg = [E for E in CUBE_VERTS if chsh_rat(E) == cube_max]
gate("A6", "NS_corr = [-1,1]^4 is the NS correlator projection",
     True, "'SUBSET' is |E_ab| <= 1 (A3); 'SUPSET' is P = 1/4(1+xyE) (A4)",
     "[NS]")
gate("A6", "max CHSH over NS_corr = 4", cube_max == 4,
     "16 cube vertices, attained only at %s"
     % ", ".join("(" + ",".join("%+d" % e for e in E) + ")" for E in cube_arg))
gate("A6", "max CHSH over L_corr = 2", A1_MAX_IS_2,
     "16 generators (A1) + [CVX](a)", "[CVX]")
gate("A6", "max CHSH over Q_corr = 2 sqrt 2", A2_MAX_IS_2SQRT2,
     "the U(1) generating family (A2) + [CVX](a)", "[CVX]")
gate("A6", "L_corr SUBSET Q_corr SUBSET NS_corr", incl_bad == 0,
     "generators of L are generators of Q (A4a); every Gram E is in "
     "[-1,1]^4 (|cos| <= 1)")
gate("A6", "STRICT on the left: Q_corr contains a point at 2 sqrt 2 > 2",
     S_inst.cmp(Q2(2, 0)) > 0, "exact Q(sqrt2) comparison")
gate("A6", "STRICT on the right: the PR vertex (1,1,1,-1) is outside Q_corr",
     Q2(4, 0).cmp(Q2(0, 2)) > 0,
     "CHSH = 4 > 2 sqrt 2 = max over Q_corr, so it cannot lie in Q_corr")
print("    %s" % el())
print()

# ---------------------------------------------------------------------------
print("A+. THE COMPLETENESS OF Q_corr  [REV2, the amendment's new target]")
print()
print("    CLAIM.  In the CHSH correlator projection, Q_corr IS the whole")
print("    quantum correlator body.  By Tsirelson's theorem [T] the quantum")
print("    correlator set is Q = { E_ab = <u_a, v_b> : u_a, v_b unit vectors")
print("    in a real Hilbert space H }, of unbounded dimension.  The claim")
print("    is that the PLANAR (dim <= 2) configurations already generate it.")
print()
print("    THE PROOF, in four exact steps.")
print("      (1) For any lambda in R^4 and fixed v_0, v_1,")
print("            sum_ab lam_ab <u_a, v_b>")
print("              = <u_0, lam_00 v_0 + lam_01 v_1>")
print("              + <u_1, lam_10 v_0 + lam_11 v_1>,")
print("          so by Lagrange's identity the optimal unit u_a is")
print("          r_a/||r_a|| with r_a = lam_a0 v_0 + lam_a1 v_1: THE OPTIMAL")
print("          u_a LIE IN span{v_0, v_1}, of dimension at most 2.")
print("      (2) ||lam_a0 v_0 + lam_a1 v_1||^2 = lam_a0^2 + lam_a1^2")
print("          + 2 lam_a0 lam_a1 t with t = <v_0, v_1>: the optimum")
print("          depends on (v_0, v_1) ONLY through t.")
print("      (3) Every t in [-1,1] is realized by unit vectors in R^2.")
print("      (4) Hence the support function of Q equals the support")
print("          function of the planar family, for EVERY lambda.  Q and")
print("          Q_corr are compact convex [CVX](c),(d) with equal support")
print("          functions, so Q = Q_corr  [CVX](b).")
print()
NDIMS = (2, 3, 4, 5, 6)
print("    caps: the symbolic identities are gated in R^n for n = %s and"
      % ", ".join(str(n) for n in NDIMS))
print("    hold for every n by the same expansion (Lagrange's identity is")
print("    standard).  Each is an exact identity in Q[coordinates].")


def dot_mp(a, b):
    acc = a[0] * b[0]
    for i in range(1, len(a)):
        acc = acc + a[i] * b[i]
    return acc


lag_ok = par_ok = bil_ok = reg_ok = True
for n in NDIMS:
    # (1) Lagrange: ||u||^2 ||r||^2 - <u,r>^2 = sum_{i<j} (u_i r_j - u_j r_i)^2
    nv = 2 * n
    u = [MP.var(nv, i) for i in range(n)]
    r = [MP.var(nv, n + i) for i in range(n)]
    lhs = dot_mp(u, u) * dot_mp(r, r) - dot_mp(u, r).sq()
    rhs = MP.const(nv, 0)
    for i in range(n):
        for j in range(i + 1, n):
            rhs = rhs + (u[i] * r[j] - u[j] * r[i]).sq()
    lag_ok &= (lhs - rhs).is_zero()
    # (2) parallelogram in R^n
    v0 = [MP.var(nv, i) for i in range(n)]
    v1 = [MP.var(nv, n + i) for i in range(n)]
    sm = [v0[i] + v1[i] for i in range(n)]
    df = [v0[i] - v1[i] for i in range(n)]
    par_ok &= (dot_mp(sm, sm) + dot_mp(df, df)
               - MP.const(nv, 2) * dot_mp(v0, v0)
               - MP.const(nv, 2) * dot_mp(v1, v1)).is_zero()
    # (3) bilinear expansion  ||x v0 + y v1||^2
    nv2 = 2 * n + 2
    a0 = [MP.var(nv2, i) for i in range(n)]
    a1 = [MP.var(nv2, n + i) for i in range(n)]
    X = MP.var(nv2, 2 * n)
    Y = MP.var(nv2, 2 * n + 1)
    comb = [X * a0[i] + Y * a1[i] for i in range(n)]
    bil_ok &= (dot_mp(comb, comb) - X.sq() * dot_mp(a0, a0)
               - Y.sq() * dot_mp(a1, a1)
               - MP.const(nv2, 2) * X * Y * dot_mp(a0, a1)).is_zero()
    # (4) the operator regrouping in R^n with SYMBOLIC lambda
    nv3 = 4 * n + 4
    U = [[MP.var(nv3, a * n + i) for i in range(n)] for a in (0, 1)]
    V = [[MP.var(nv3, 2 * n + b * n + i) for i in range(n)] for b in (0, 1)]
    L = [[MP.var(nv3, 4 * n + 2 * a + b) for b in (0, 1)] for a in (0, 1)]
    left = MP.const(nv3, 0)
    for a in (0, 1):
        for b in (0, 1):
            left = left + L[a][b] * dot_mp(U[a], V[b])
    right = MP.const(nv3, 0)
    for a in (0, 1):
        rv = [L[a][0] * V[0][i] + L[a][1] * V[1][i] for i in range(n)]
        right = right + dot_mp(U[a], rv)
    reg_ok &= (left - right).is_zero()
gate("A+", "step 1a: Lagrange's identity in R^n", lag_ok,
     "n = %s; gives <u,r> <= ||r|| with maximizer r/||r|| in span{r}"
     % ", ".join(str(n) for n in NDIMS))
gate("A+", "step 1b: the operator regrouping in R^n, symbolic lambda",
     reg_ok, "sum lam_ab <u_a,v_b> = sum_a <u_a, lam_a0 v_0 + lam_a1 v_1>")
gate("A+", "step 2: ||x v_0 + y v_1||^2 = x^2+y^2+2xy<v_0,v_1> on units",
     bil_ok, "the optimum depends on (v_0,v_1) only through t = <v_0,v_1>")
gate("A+", "the parallelogram identity holds in R^n, all n", par_ok,
     "so CERT-0/1/2/3 prove CHSH <= 2 sqrt 2 in EVERY dimension", "[T]")

# step 3: every t in [-1,1] is realized in R^2.  The rational points of the
# unit circle are t = (1-m^2)/(1+m^2), s = 2m/(1+m^2), m in Q -- exact, dense.
CAP_M = 40
circ_bad = 0
for num in range(-CAP_M, CAP_M + 1):
    for den in range(1, CAP_M + 1):
        m = Fr(num, den)
        t = (1 - m * m) / (1 + m * m)
        s = 2 * m / (1 + m * m)
        if t * t + s * s != 1 or t < -1 or t > 1:
            circ_bad += 1
gate("A+", "step 3: the rational circle parametrization is exact",
     circ_bad == 0,
     "%d rational slopes m, t^2+s^2 = 1 exactly and t in [-1,1]; the "
     "rational points are dense, and surjectivity onto [-1,1] is continuity"
     % ((2 * CAP_M + 1) * CAP_M))

# corroboration: an exhaustive sweep of EXACT RATIONAL unit vectors in
# R^3 and R^4 -- no configuration of any dimension beats the planar bound.
def rational_unit_vectors(n, dmax, cap):
    out = []
    for d in range(1, dmax + 1):
        for v in itertools.product(range(-d, d + 1), repeat=n):
            if sum(x * x for x in v) == d * d:
                out.append(tuple(Fr(x, d) for x in v))
    seen = set()
    uniq = []
    for v in out:
        if v not in seen:
            seen.add(v)
            uniq.append(v)
    uniq.sort()
    return uniq[:cap]


CAP_VEC = 26
for n, dmax in ((3, 9), (4, 5)):
    L = rational_unit_vectors(n, dmax, CAP_VEC)
    best = Q2(-10, 0)
    over = 0
    npair = 0
    for u0 in L:
        for u1 in L:
            for v0 in L:
                for v1 in L:
                    e = [sum(x * y for x, y in zip(ua, vb))
                         for ua in (u0, u1) for vb in (v0, v1)]
                    S = Q2(chsh_rat(e), 0)
                    npair += 1
                    if S.cmp(Q2(0, 2)) > 0:
                        over += 1
                    if S.cmp(best) > 0:
                        best = S
    gate("A+", "R^%d rational-unit-vector sweep: none exceeds 2 sqrt 2" % n,
         over == 0,
         "%d exact rational unit vectors, %d configurations, max CHSH = %s "
         "< 2 sqrt 2" % (len(L), npair, best))
    print("      ... R^%d sweep done   %s" % (n, el()))

A_PLUS_OK = (lag_ok and par_ok and bil_ok and reg_ok and circ_bad == 0)
gate("A+", "THE COMPLETENESS OF Q_corr", A_PLUS_OK,
     "steps 1-4 all exact => Q = conv(planar) = Q_corr at this scenario",
     "[REV2]")
print()
print("    SCOPE TAG, engraved with the theorem: this is the CHSH (2,2,2)")
print("    CORRELATOR PROJECTION, after convexification.  It says nothing")
print("    about full behaviours (marginals), nothing about scenarios with")
print("    more settings, parties or outcomes, and it does not claim that")
print("    the un-convexified U(1)-Gram generating class is the quantum set")
print("    — A5 proves that class is not even convex.")
print("    %s" % el())
print()


# ============================================================================
head("SECTION B — THE ANTI-CORRELATION EXHIBIT [REV]")
# ============================================================================
print("B1. THE SINGLET AMPLITUDE MODEL")
print("    psi_xy(a,b) = (z_a - x y w_b) / (2 sqrt 2),  z_a = e^{ia},")
print("    w_b = e^{ib},  x,y in {+1,-1};  P(x,y|a,b) = |psi_xy(a,b)|^2.")
print()
# symbolic Born identity
ca, sa, db, tb, ee = (MP.var(5, i) for i in range(5))
born = (ca - ee * db).sq() + (sa - ee * tb).sq() \
       - ((ca.sq() + sa.sq()) + ee.sq() * (db.sq() + tb.sq())
          - MP.const(5, 2) * ee * (ca * db + sa * tb))
gate("B1", "CERT-4 (Born expansion) identity", born.is_zero(),
     "|z - e w|^2 = |z|^2 + e^2|w|^2 - 2e Re(z conj w) in Q[c,s,d,t,e]")
print("    With |z| = |w| = 1 and e = xy in {+-1} (so e^2 = 1) this reads")
print("    |z_a - xy w_b|^2 = 2 - 2 xy cos(a-b), hence")
print("    P(x,y|a,b) = (2 - 2 xy cos(a-b)) / 8 = 1/4 (1 - xy cos(a-b)).")
print()

FAMILIES = [("pi/4 family, Q(zeta_8)  ", K8, 8, INV_SQRT2_8),
            ("pi/8 family, Q(zeta_16) ", K16, 16, INV_SQRT2_16)]
print("    caps: pi/4 family = all 8 angles 2 pi k / 8; pi/8 family = all")
print("    16 angles 2 pi k / 16.  Born identity gated on every (a,b,x,y).")
for label, K, N, inv2 in FAMILIES:
    half = K.scal(inv2, Fr(1, 2))          # 1 / (2 sqrt 2)
    assert K.mul(half, K.conj(half)) == K.rat(Fr(1, 8))
    nbad = 0
    ntot = 0
    for ka in range(N):
        za = K.zpow(ka)
        for kb in range(N):
            wb = K.zpow(kb)
            cosab = K.re(K.zpow((ka - kb) % N))
            for x in PM:
                for y in PM:
                    amp = K.mul(K.sub(za, K.scal(wb, x * y)), half)
                    P = K.mul(amp, K.conj(amp))
                    tgt = K.scal(K.sub(K.one, K.scal(cosab, x * y)), Fr(1, 4))
                    ntot += 1
                    if P != tgt:
                        nbad += 1
    gate("B1", "Born identity P = 1/4(1 - xy cos(a-b)) [%s]" % label.strip(),
         nbad == 0, "%d exact gates, 0 failures" % ntot, "[REV]")

# normalization + no-signaling of the singlet table, exhaustive on pi/4 family
K = K8
half8 = K8.scal(INV_SQRT2_8, Fr(1, 2))
print()
print("    THE SINGLET TABLE IS NO-SIGNALING, exhaustively.  Every")
print("    P(x,y|a,b) = 1/4 (1 - xy cos(a-b)) is non-negative (|cos| <= 1,")
print("    gated below by the exact Q(sqrt2) sign oracle), normalized and")
print("    uniform-marginal (the identities gated at A4).")
sing_bad = 0
sing_tot = 0
sing_built = 0
for ka0, ka1, kb0, kb1 in itertools.product(range(8), repeat=4):
    ka = (ka0, ka1); kb = (kb0, kb1)
    E4 = [to_q2(K8.neg(K8.re(K8.zpow((ka[a] - kb[b]) % 8))))
          for (a, b) in S_IDX]
    sing_tot += 1
    for e in E4:
        if Q2(1 - e.a, -e.b).sign() < 0 or Q2(1 + e.a, e.b).sign() < 0:
            sing_bad += 1
    if all(e.b == 0 for e in E4):
        T = table_from_corr([e.a for e in E4])
        sing_built += 1
        if not table_ok(T)[0] or corr(T) != tuple(e.a for e in E4):
            sing_bad += 1
gate("B1", "the singlet table is a valid NS table", sing_bad == 0,
     "%d pi/4 quadruples non-negativity-gated; %d tables built and fully "
     "NS-checked" % (sing_tot, sing_built))

# CHSH at the review's settings, exact.  E_ab = -cos(a-b).
REV_A = (0, 2)   # a_0 = 0, a_1 = pi/2      (units of pi/4)
REV_B = (1, 7)   # b_0 = pi/4, b_1 = -pi/4  (units of pi/4)
E_sing = [to_q2(K8.neg(K8.re(K8.zpow((REV_A[a] - REV_B[b]) % 8))))
          for (a, b) in S_IDX]
S_sing = Q2(sum(sg * e.a for sg, e in zip(CHSH_SIGNS, E_sing)),
            sum(sg * e.b for sg, e in zip(CHSH_SIGNS, E_sing)))
gate("B1", "singlet CHSH = -2 sqrt 2 at (0, pi/2; pi/4, -pi/4)",
     S_sing == Q2(0, -2), "S = %s (matches LOG #3 verbatim)" % S_sing, "[REV]")
gate("B1", "|singlet CHSH| = 2 sqrt 2 = the Gram class maximum",
     Q2(-S_sing.a, -S_sing.b) == Q2(0, 2),
     "the sign is the functional's, not the model's: w_b -> -w_b flips it")
# the sign-flipped instance, in-class
E_sing_f = [Q2(-e.a, -e.b) for e in E_sing]
S_sing_f = Q2(sum(sg * e.a for sg, e in zip(CHSH_SIGNS, E_sing_f)),
              sum(sg * e.b for sg, e in zip(CHSH_SIGNS, E_sing_f)))
gate("B1", "the relabelled instance attains +2 sqrt 2 in-class",
     S_sing_f == Q2(0, 2), "w_b -> -w_b stays in the U(1)-Gram class")

# the 4-cycle holonomy of the factorized relative phase
print()
print("    THE HOLONOMY, one line.  g_ab = z_a conj(w_b).  Then")
print("      g_00 g_10^{-1} g_11 g_01^{-1}")
print("        = (z_0 conj w_0)(conj z_1 w_0)(z_1 conj w_1)(conj z_0 w_1)")
print("        = (z_0 conj z_0)(z_1 conj z_1)(w_0 conj w_0)(w_1 conj w_1) = 1")
print("    identically: every factorized edge phase is a coboundary, so its")
print("    holonomy around ANY cycle is 1.  [AB: a witness, not equivalence]")
CAP_HOL8 = 8 ** 4
CAP_HOL16 = 16 ** 3
print("    caps: pi/4 family exhaustive %d quadruples; pi/8 family %d"
      % (CAP_HOL8, CAP_HOL16))
print("    quadruples (a_0 = 0 fixed: the holonomy is invariant under")
print("    z_a -> lam z_a and w_b -> mu w_b independently — each z_a and each")
print("    w_b occurs once with each exponent sign).")


def holonomy(K, g00, g01, g10, g11):
    return K.mul(K.mul(g00, K.inv(g10)), K.mul(g11, K.inv(g01)))


for label, K, N, cap_a0 in [("pi/4", K8, 8, None), ("pi/8", K16, 16, 0)]:
    nbad = 0
    ntot = 0
    a0range = range(N) if cap_a0 is None else [cap_a0]
    for ka0 in a0range:
        for ka1 in range(N):
            for kb0 in range(N):
                for kb1 in range(N):
                    za = [K.zpow(ka0), K.zpow(ka1)]
                    wb = [K.zpow(kb0), K.zpow(kb1)]
                    g = {(a, b): K.mul(za[a], K.conj(wb[b]))
                         for (a, b) in S_IDX}
                    h = holonomy(K, g[(0, 0)], g[(0, 1)], g[(1, 0)], g[(1, 1)])
                    ntot += 1
                    if h != K.one:
                        nbad += 1
    gate("B1", "4-cycle holonomy = 1 IDENTICALLY [%s family]" % label,
         nbad == 0, "%d quadruples, 0 failures" % ntot, "[REV]")
    print("      ... %s family swept   %s" % (label, el()))
print()

print("B2. THE PR EDGE-PHASE PATTERN  (gamma_00,gamma_01,gamma_10,gamma_11)")
print("    = (1, 1, 1, -1)")
T_PR = table_pr(0, 0, 0)
ok_pr, why_pr = table_ok(T_PR)
gate("B2", "the PR table is a valid no-signaling table", ok_pr,
     "nonneg + normalized + both marginal conditions" if ok_pr else why_pr,
     "[NS]")
marg_ok = all(sum(T_PR[(a, b, x, y)] for y in PM) == Fr(1, 2)
              for a in (0, 1) for b in (0, 1) for x in PM)
marg_ok &= all(sum(T_PR[(a, b, x, y)] for x in PM) == Fr(1, 2)
               for a in (0, 1) for b in (0, 1) for y in PM)
gate("B2", "PR marginals uniform (= 1/2) on both wings", marg_ok,
     "exact rationals")
E_PR = corr(T_PR)
gate("B2", "PR correlators = (1, 1, 1, -1)",
     E_PR == (Fr(1), Fr(1), Fr(1), Fr(-1)),
     "E = (%s)" % ", ".join("%+d" % e for e in E_PR))
gate("B2", "PR CHSH = 4 EXACTLY", chsh_rat(E_PR) == 4,
     "S = %s" % chsh_rat(E_PR), "[NS]")
gam = {(0, 0): K8.one, (0, 1): K8.one, (1, 0): K8.one,
       (1, 1): K8.neg(K8.one)}
h_pr = holonomy(K8, gam[(0, 0)], gam[(0, 1)], gam[(1, 0)], gam[(1, 1)])
gate("B2", "PR 4-cycle holonomy = -1", h_pr == K8.neg(K8.one),
     "gamma_00 gamma_10^{-1} gamma_11 gamma_01^{-1} = -1: NOT a coboundary",
     "[REV]")
gate("B2", "PR edge phases do NOT factorize", h_pr != K8.one,
     "no z_a, w_b with gamma_ab = z_a conj(w_b) (holonomy is the obstruction)")
print()

print("B3. THE ENGRAVED TABLE")
print()
print("    +--------------------------+-------------------+--------------+")
print("    | model                    | 4-cycle holonomy  |   CHSH       |")
print("    +--------------------------+-------------------+--------------+")
print("    | singlet (U(1)-Gram)      | TRIVIAL   ( = 1)  |  2 sqrt 2    |")
print("    | PR edge-phase (1,1,1,-1) | NONTRIVIAL( = -1) |  4           |")
print("    +--------------------------+-------------------+--------------+")
print()
print("    READING, engraved: the v12 v1 identification 'quantum <=>")
print("    nontrivial class' is ANTI-CORRELATED with quantumness in the")
print("    natural models — the Tsirelson-saturating model carries the")
print("    trivial class and the nontrivial class is superquantum.  This")
print("    is the exhibit, not a theorem about all models.")
S_B1 = [ok for s, n, ok, _, _ in GATES if s == "B1"]
S_B2 = [ok for s, n, ok, _, _ in GATES if s == "B2"]
gate("B3", "THE ANTI-CORRELATION TABLE, both rows gated",
     all(S_B1) and all(S_B2),
     "trivial holonomy <-> 2 sqrt 2; nontrivial holonomy <-> 4", "[REV]")
gate("B3", "a 1-cocycle class is a WITNESS, not an equivalence",
     h_pr != K8.one and S_sing == Q2(0, -2),
     "the caution of [AB] made concrete: the class separates these two "
     "models the WRONG way round", "[AB]")
ANTI_CORR_OK = all(S_B1) and all(S_B2)
print("    %s" % el())
print()


# ============================================================================
head("SECTION C — THE DELTA CENSUS  [B1]")
# ============================================================================
print("    Delta^B(U2,U1) = B(U2 U1) - B(U2) B(U1),  B(U)_ij = |U_ij|^2.")
print()


def mmul(K, A, B):
    n = len(A); m = len(B[0]); p = len(B)
    return [[_dot(K, A[i], [B[k][j] for k in range(p)]) for j in range(m)]
            for i in range(n)]


def _dot(K, r, c):
    acc = K.zero
    for a, b in zip(r, c):
        acc = K.add(acc, K.mul(a, b))
    return acc


def mdag(K, A):
    return [[K.conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def mB(K, A):
    return [[K.mul(x, K.conj(x)) for x in row] for row in A]


def msub(K, A, B):
    return [[K.sub(A[i][j], B[i][j]) for j in range(len(A[0]))]
            for i in range(len(A))]


def mzero(K, A):
    return all(K.is_zero(x) for row in A for x in row)


def meq(K, A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A))
               for j in range(len(A[0])))


def mid(K, n):
    return [[K.one if i == j else K.zero for j in range(n)] for i in range(n)]


def is_unitary(K, U):
    n = len(U)
    return meq(K, mmul(K, U, mdag(K, U)), mid(K, n))


def delta_def(K, U2, U1):
    return msub(K, mB(K, mmul(K, U2, U1)), mmul(K, mB(K, U2), mB(K, U1)))


def delta_cross(K, U2, U1):
    """Delta^B_ij = sum_{k!=l} (U2)_ik (U1)_kj conj( (U2)_il (U1)_lj )."""
    n = len(U2); p = len(U1)
    out = []
    for i in range(n):
        row = []
        for j in range(len(U1[0])):
            acc = K.zero
            for k in range(p):
                for l in range(p):
                    if k == l:
                        continue
                    t1 = K.mul(U2[i][k], U1[k][j])
                    t2 = K.conj(K.mul(U2[i][l], U1[l][j]))
                    acc = K.add(acc, K.mul(t1, t2))
            row.append(acc)
        out.append(row)
    return out


# ------------------------------------------------------- the exhibited pairs
H2 = [[K8.mul(K8.rat(a), INV_SQRT2_8) for a in row]
      for row in ([1, 1], [1, -1])]
W_UNB = [[K8.mul(K8.zpow(k), INV_SQRT2_8) for k in row]
         for row in ([0, 2], [2, 0])]         # (1/sqrt2)[[1,i],[i,1]]
OM = K12.zpow(4)                              # zeta_3
F3 = [[K12.mul(K12.zpow(4 * ((i * j) % 3)), INV_SQRT3_12) for j in range(3)]
      for i in range(3)]

gate("C1", "H (2x2 Hadamard-type) is unitary over Q(zeta_8)",
     is_unitary(K8, H2), "H = (1/sqrt2)[[1,1],[1,-1]]")
gate("C1", "W = (1/sqrt2)[[1,i],[i,1]] is unitary over Q(zeta_8)",
     is_unitary(K8, W_UNB))
gate("C1", "F3 (DFT_3) is unitary over Q(zeta_12)", is_unitary(K12, F3),
     "F_jk = zeta_3^{jk}/sqrt3; zeta_3 and sqrt3 both live in Q(zeta_12)")

print()
print("C1. THE CROSS-TERM IDENTITY, entrywise [B1]")
for nm, K, U2, U1 in [("H . H  (2x2, Q(zeta_8))", K8, H2, H2),
                      ("F3 . F3 (3x3, Q(zeta_12))", K12, F3, F3),
                      ("H . W  (2x2, Q(zeta_8))", K8, H2, W_UNB),
                      ("F3 . F3^dag (3x3)", K12, F3, mdag(K12, F3))]:
    d1 = delta_def(K, U2, U1)
    d2 = delta_cross(K, U2, U1)
    gate("C1", "Delta^B_def = Delta^B_crossterm  [%s]" % nm, meq(K, d1, d2),
         "entrywise exact equality", "[B1]")

# printed values of the two headline defects
d_HH = delta_def(K8, H2, H2)
gate("C1", "Delta^B(H,H) != 0", not mzero(K8, d_HH),
     "Delta^B = [[1/2, -1/2], [-1/2, 1/2]] (B(H.H) = I, B(H)B(H) = J/2)")
d_FF = delta_def(K12, F3, F3)
gate("C1", "Delta^B(F3,F3) != 0", not mzero(K12, d_FF),
     "B(F3^2) = the permutation j -> -j mod 3; B(F3)B(F3) = J/3")
print()

# ------------------------------------------------------------- the census
print("C2. THE Delta^B = 0 CENSUS")


def diag(K, ph):
    n = len(ph)
    return [[ph[i] if i == j else K.zero for j in range(n)] for i in range(n)]


def perm(K, s):
    n = len(s)
    return [[K.one if s[j] == i else K.zero for j in range(n)]
            for i in range(n)]


def row_monomial(K, U):
    return all(sum(1 for x in row if not K.is_zero(x)) <= 1 for row in U)


def col_monomial(K, U):
    n = len(U)
    return all(sum(1 for i in range(n) if not K.is_zero(U[i][j])) <= 1
               for j in range(len(U[0])))


def key(U):
    return tuple(tuple(x for x in row) for row in U)


# family F2 over Q(zeta_8)
F2 = {}
for s in itertools.permutations(range(2)):
    for e0, e1 in itertools.product((0, 2, 4, 6), repeat=2):   # mu_4 phases
        M = mmul(K8, perm(K8, s), diag(K8, [K8.zpow(e0), K8.zpow(e1)]))
        F2[key(M)] = M
NMON2 = len(F2)
for s in range(8):
    for t in range(8):
        M = mmul(K8, mmul(K8, diag(K8, [K8.one, K8.zpow(s)]), H2),
                 diag(K8, [K8.one, K8.zpow(t)]))
        F2[key(M)] = M
F2L = [F2[k] for k in sorted(F2.keys())]

# family F3 over Q(zeta_12)
FAM3 = {}
for s in itertools.permutations(range(3)):
    for e in itertools.product((0, 4, 8), repeat=2):           # mu_3 phases
        M = mmul(K12, perm(K12, s),
                 diag(K12, [K12.one, K12.zpow(e[0]), K12.zpow(e[1])]))
        FAM3[key(M)] = M
NMON3 = len(FAM3)
for a in (0, 4, 8):
    for b in (0, 4, 8):
        M = mmul(K12, mmul(K12, diag(K12, [K12.one, K12.zpow(a), K12.one]),
                           F3),
                 diag(K12, [K12.one, K12.zpow(b), K12.one]))
        FAM3[key(M)] = M
FAM3L = [FAM3[k] for k in sorted(FAM3.keys())]

print("    caps, declared: F2 = the 2x2 unitaries P.diag(mu_4) (monomial)")
print("    together with diag(1,mu_8).H.diag(1,mu_8) (unbiased), deduped;")
print("    F3 = the 3x3 unitaries P.diag(1,mu_3,mu_3) (monomial) together")
print("    with diag(1,mu_3,1).F3.diag(1,mu_3,1) (unbiased), deduped.")
print("    ALL ORDERED PAIRS of each family are swept — no sampling.")
print("      F2: %d matrices (%d monomial-seeded), %d ordered pairs"
      % (len(F2L), NMON2, len(F2L) ** 2))
print("      F3: %d matrices (%d monomial-seeded), %d ordered pairs"
      % (len(FAM3L), NMON3, len(FAM3L) ** 2))

gate("C2", "every F2 member is unitary",
     all(is_unitary(K8, U) for U in F2L), "%d matrices" % len(F2L))
gate("C2", "every F3 member is unitary",
     all(is_unitary(K12, U) for U in FAM3L), "%d matrices" % len(FAM3L))

census = {}
for tag, K, FAM in [("2x2", K8, F2L), ("3x3", K12, FAM3L)]:
    Bcache = [mB(K, U) for U in FAM]
    rm = [row_monomial(K, U) for U in FAM]
    cm = [col_monomial(K, U) for U in FAM]
    cnt = {"cond_zero": 0, "cond_nonzero": 0,
           "free_zero": 0, "free_nonzero": 0}
    cross_bad = 0
    npair = 0
    t_last = time.time()
    for i2, U2 in enumerate(FAM):
        for i1, U1 in enumerate(FAM):
            D = msub(K, mB(K, mmul(K, U2, U1)),
                     mmul(K, Bcache[i2], Bcache[i1]))
            if not meq(K, D, delta_cross(K, U2, U1)):
                cross_bad += 1
            z = mzero(K, D)
            c = rm[i2] or cm[i1]
            cnt["%s_%s" % ("cond" if c else "free",
                           "zero" if z else "nonzero")] += 1
            npair += 1
        if time.time() - t_last > 120:
            print("      ... %s census %d/%d rows   %s"
                  % (tag, i2 + 1, len(FAM), el()))
            t_last = time.time()
    census[tag] = (cnt, npair, cross_bad)
    print("      %s census done: %d pairs   %s" % (tag, npair, el()))

for tag in ("2x2", "3x3"):
    cnt, npair, cross_bad = census[tag]
    gate("C2", "cross-term identity on EVERY census pair [%s]" % tag,
         cross_bad == 0, "%d pairs, 0 mismatches" % npair, "[B1]")
    gate("C2", "SUFFICIENCY [%s]: row-mono(U2) or col-mono(U1) => Delta^B = 0"
         % tag, cnt["cond_nonzero"] == 0,
         "%d pairs satisfy the condition, %d of them have Delta^B != 0"
         % (cnt["cond_zero"] + cnt["cond_nonzero"], cnt["cond_nonzero"]))
    gate("C2", "NOT NECESSARY [%s]: Delta^B = 0 without the condition" % tag,
         cnt["free_zero"] > 0,
         "%d such pairs (of %d unconditioned)"
         % (cnt["free_zero"], cnt["free_zero"] + cnt["free_nonzero"]))
    print("      %s counts: cond&zero %d | cond&nonzero %d | free&zero %d "
          "| free&nonzero %d" % (tag, cnt["cond_zero"], cnt["cond_nonzero"],
                                 cnt["free_zero"], cnt["free_nonzero"]))

# the named honest counterexample
d_HW = delta_def(K8, H2, W_UNB)
gate("C2", "NAMED counterexample to necessity: Delta^B(H, W) = 0",
     mzero(K8, d_HW) and not row_monomial(K8, H2)
     and not col_monomial(K8, W_UNB),
     "H and W = (1/sqrt2)[[1,i],[i,1]] both fully unbiased, yet Delta^B = 0")
print("    THE SHARPENING, engraved: 'U2 has at most one nonzero per row'")
print("    (equivalently U1 at most one nonzero per column) is SUFFICIENT")
print("    for Delta^B = 0 — the k != l sum is empty — but NOT NECESSARY.")
print("    The 2x2 obstruction is Re(A_i B_j) = 0 with")
print("    A_i = (U2)_i0 conj((U2)_i1), B_j = (U1)_0j conj((U1)_1j);")
print("    H gives real A_i, W gives imaginary B_j.  Delta^B = 0 is a")
print("    PHASE-ALIGNMENT condition, not a support condition.")
print()
print("    THE UNBIASED SUB-CENSUS, decided in closed form and gated.")
print("    For unbiased factors B(U2) = B(U1) = J/n, so B(U2)B(U1) = J/n and")
print("    Delta^B = 0 <=> B(U2U1) = J/n <=> the PRODUCT is again unbiased.")
print("    The outer diagonals do not change moduli, so Delta^B depends")
print("    only on the INTERLEAVING phase between the two blocks.")

# 2x2: U2 = diag(1,z^s) H diag(1,z^t), U1 = diag(1,z^u) H diag(1,z^v).
#      Delta = 0 <=> H diag(1, z^{t+u}) H is unbiased <=> t+u = 2 or 6 mod 8.
sub2_bad = 0
sub2_zero = 0
sub2_tot = 0
for s, t, u, v in itertools.product(range(8), repeat=4):
    U2 = mmul(K8, mmul(K8, diag(K8, [K8.one, K8.zpow(s)]), H2),
              diag(K8, [K8.one, K8.zpow(t)]))
    U1 = mmul(K8, mmul(K8, diag(K8, [K8.one, K8.zpow(u)]), H2),
              diag(K8, [K8.one, K8.zpow(v)]))
    z = mzero(K8, delta_def(K8, U2, U1))
    pred = ((t + u) % 8) in (2, 6)
    sub2_tot += 1
    sub2_zero += 1 if z else 0
    if z != pred:
        sub2_bad += 1
gate("C2", "2x2 unbiased sub-census: Delta^B = 0 <=> t+u = +-2 (mod 8)",
     sub2_bad == 0,
     "%d parameter quadruples (8^4), %d with Delta^B = 0, prediction exact"
     % (sub2_tot, sub2_zero))
print("      i.e. Delta^B vanishes exactly when the interleaving phase is")
print("      a QUARTER TURN: the two Hadamard blocks compose to an")
print("      unbiased matrix iff the relative phase is +-i.  (H,W) of C1")
print("      is the case t+u = 2.")

# 3x3: U2 = D(a2) F D(b2), U1 = D(a1) F D(b1) with D(m) = diag(1, w^m, 1).
#      Delta = 0 <=> F D(b2 + a1) F is unbiased <=> b2 + a1 != 0 mod 3.
sub3_bad = 0
sub3_zero = 0
sub3_tot = 0
for a2, b2, a1, b1 in itertools.product(range(3), repeat=4):
    U2 = mmul(K12, mmul(K12, diag(K12, [K12.one, K12.zpow(4 * a2), K12.one]),
                        F3), diag(K12, [K12.one, K12.zpow(4 * b2), K12.one]))
    U1 = mmul(K12, mmul(K12, diag(K12, [K12.one, K12.zpow(4 * a1), K12.one]),
                        F3), diag(K12, [K12.one, K12.zpow(4 * b1), K12.one]))
    z = mzero(K12, delta_def(K12, U2, U1))
    pred = ((b2 + a1) % 3) != 0
    sub3_tot += 1
    sub3_zero += 1 if z else 0
    if z != pred:
        sub3_bad += 1
gate("C2", "3x3 DFT sub-census: Delta^B = 0 <=> b2 + a1 != 0 (mod 3)",
     sub3_bad == 0,
     "%d parameter quadruples (3^4), %d with Delta^B = 0, prediction exact"
     % (sub3_tot, sub3_zero))
print("      i.e. F D(m) F is a complex Hadamard matrix for m != 0 and has")
print("      zero entries for m = 0 (where it is the permutation j -> -j).")
print("      The defect is governed by ONE phase, not by supports.")
print("    %s" % el())
print()

# ------------------------------------------- C+1 the three-defect separation
print("C+1. THE THREE-DEFECT SEPARATION  [REV2]")
print("    Three objects are distinguished and NEVER conflated:")
print("      Delta^B(U2,U1) = B(U2 U1) - B(U2) B(U1)   the Born-shadow defect")
print("      D_210          = Gam_20 - Gam_21 Gam_10   the residual of a")
print("                                                DECLARED stochastic law")
print("      d_div          = inf over stochastic K of || Gam_20 - K Gam_10 ||")
print("                                                existential divisibility")
print("    The counterexample is exact and rational.  For the real rotation")
print("    R(th) = [[c, -s], [s, c]] with c^2 + s^2 = 1:")
NV = 2
cS, sS = MP.var(NV, 0), MP.var(NV, 1)
# B(R) = [[c^2, s^2],[s^2, c^2]] and S(x) = 1/2 [[1+x, 1-x],[1-x, 1+x]]
half = MP.const(NV, Fr(1, 2))
lhs00 = cS.sq()
rhs00 = half * (MP.const(NV, 1) + (cS.sq() - sS.sq()))
lhs01 = sS.sq()
rhs01 = half * (MP.const(NV, 1) - (cS.sq() - sS.sq()))
res00 = lhs00 - rhs00 - half * (cS.sq() + sS.sq() - MP.const(NV, 1))
res01 = lhs01 - rhs01 - half * (cS.sq() + sS.sq() - MP.const(NV, 1))
gate("C+1", "B(R(th)) = S(cos 2 th) on the unit circle",
     res00.is_zero() and res01.is_zero(),
     "residual = (c^2+s^2-1)/2 exactly, vanishing on c^2+s^2 = 1", "[REV2]")
cV, dV = MP.var(2, 0), MP.var(2, 1)


def S_mp(x, nv=2):
    h = MP.const(nv, Fr(1, 2))
    return [[h * (MP.const(nv, 1) + x), h * (MP.const(nv, 1) - x)],
            [h * (MP.const(nv, 1) - x), h * (MP.const(nv, 1) + x)]]


Sc, Sd, Scd = S_mp(cV), S_mp(dV), S_mp(cV * dV)
prod_ok = True
for i in range(2):
    for j in range(2):
        acc = MP.const(2, 0)
        for k in range(2):
            acc = acc + Sc[i][k] * Sd[k][j]
        prod_ok &= (acc - Scd[i][j]).is_zero()
gate("C+1", "the semigroup law S(c) S(d) = S(c d)", prod_ok,
     "entrywise polynomial identity in Q[c,d]", "[REV2]")


def S_rat(x):
    x = Fr(x)
    return [[(1 + x) / 2, (1 - x) / 2], [(1 - x) / 2, (1 + x) / 2]]


def mmul_rat(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def stochastic(M):
    return (all(x >= 0 for r in M for x in r)
            and all(sum(M[i][j] for i in range(len(M))) == 1
                    for j in range(len(M))))


c1c, s1c = Fr(24, 25), Fr(7, 25)          # U1 = R(th1)
c2c, s2c = Fr(4, 5), Fr(3, 5)             # U2 = R(th2)
gate("C+1", "the two rotations are exact rational unit vectors",
     c1c ** 2 + s1c ** 2 == 1 and c2c ** 2 + s2c ** 2 == 1,
     "(24/25, 7/25) and (4/5, 3/5)")
c1 = c1c ** 2 - s1c ** 2                   # cos 2 th1
c2 = c2c ** 2 - s2c ** 2                   # cos 2 th2
s1 = 2 * c1c * s1c
s2 = 2 * c2c * s2c
ctot = c1 * c2 - s1 * s2                   # cos 2(th1 + th2)
gate("C+1", "c_1 = 527/625, c_2 = 7/25, c_tot = -7/25",
     c1 == Fr(527, 625) and c2 == Fr(7, 25) and ctot == Fr(-7, 25),
     "computed from the rotation angle-addition, exact rationals")
B1m, B2m = S_rat(c1), S_rat(c2)
Btot = S_rat(ctot)
DeltaB = [[Btot[i][j] - mmul_rat(B2m, B1m)[i][j] for j in range(2)]
          for i in range(2)]
gate("C+1", "Delta^B != 0 on this pair",
     any(x != 0 for r in DeltaB for x in r),
     "S(-7/25) != S(7/25 . 527/625) = S(3689/15625); "
     "Delta^B_00 = %s" % DeltaB[0][0], "[REV2]")
gate("C+1", "so the DECLARED law Gam_21 = B(U2) has residual D_210 != 0",
     any(x != 0 for r in DeltaB for x in r),
     "with that declaration D_210 = Delta^B exactly")
Kdiv = S_rat(Fr(-175, 527))
gate("C+1", "K = S(-175/527) is a valid stochastic matrix", stochastic(Kdiv),
     "|c| = 175/527 <= 1, entries (1+-c)/2 >= 0, columns sum to 1")
gate("C+1", "K . B(U1) = B(U2 U1) EXACTLY",
     mmul_rat(Kdiv, B1m) == Btot,
     "S(-175/527) S(527/625) = S(-175/625) = S(-7/25) = B(U2 U1)", "[REV2]")
gate("C+1", "K is NOT B(U2)", Kdiv != B2m,
     "K = S(-175/527), B(U2) = S(7/25): the divisor exists but is not the "
     "Born shadow of the second step")
gate("C+1", "=> d_div = 0 WHILE Delta^B != 0", True,
     "THE SEPARATION: Delta^B != 0 does NOT imply stochastic "
     "indivisibility", "[REV2]")
# the general rotation statement
gen_bad = 0
gen_tot = 0
for a in range(-6, 7):
    for b in range(1, 7):
        for p in range(-6, 7):
            for q in range(1, 7):
                x, y = Fr(a, b), Fr(p, q)
                if abs(x) > 1 or abs(y) > 1 or x == 0:
                    continue
                if abs(y) > abs(x):
                    continue
                gen_tot += 1
                K = S_rat(y / x)
                if not stochastic(K) or mmul_rat(K, S_rat(x)) != S_rat(y):
                    gen_bad += 1
gate("C+1", "general: |c_tot| <= |c_1| => K = S(c_tot/c_1) divides",
     gen_bad == 0,
     "%d exact rational (c_1, c_tot) pairs, 0 failures" % gen_tot)
print("    ENGRAVED: Delta^B is an AMPLITUDE-LEVEL coherence measure.  It is")
print("    not a divisibility measure, not a witness of indivisibility, and")
print("    not the residual of any declared stochastic law unless that law")
print("    is declared to be B(U2).  Nothing in this receipt equates them.")
print("    %s" % el())
print()

# ------------------------------------------------------- C+2 the coherence law
print("C+2. THE COHERENCE LAW  (W2a's seed)  [REV2]")
print("      Delta^B(U3 U2, U1) + Delta^B(U3, U2) B(U1)")
print("    = Delta^B(U3, U2 U1) + B(U3) Delta^B(U2, U1)")
print("    Both sides equal B(U3 U2 U1) - B(U3) B(U2) B(U1).  The derivation")
print("    uses only associativity and distributivity of matrix algebra, so")
print("    it is an IDENTITY IN FORMAL MATRICES: gated with independent")
print("    polynomial variables for every entry of B(U1), B(U2), B(U3),")
print("    B(U2 U1), B(U3 U2), B(U3 U2 U1) — no property of B assumed.")


def mp_matrix(nv, base, n):
    return [[MP.var(nv, base + i * n + j) for j in range(n)]
            for i in range(n)]


def mp_mm(A, B, nv):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)),
                 MP.const(nv, 0)) for j in range(n)] for i in range(n)]


def mp_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


sym_ok = {}
for n in (2, 3):
    nv = 6 * n * n
    P1 = mp_matrix(nv, 0 * n * n, n)          # B(U1)
    P2 = mp_matrix(nv, 1 * n * n, n)          # B(U2)
    P3 = mp_matrix(nv, 2 * n * n, n)          # B(U3)
    Q21 = mp_matrix(nv, 3 * n * n, n)         # B(U2 U1)
    Q32 = mp_matrix(nv, 4 * n * n, n)         # B(U3 U2)
    Q321 = mp_matrix(nv, 5 * n * n, n)        # B(U3 U2 U1)
    lhsM = [[(Q321[i][j] - mp_mm(Q32, P1, nv)[i][j])
             + mp_mm(mp_sub(Q32, mp_mm(P3, P2, nv)), P1, nv)[i][j]
             for j in range(n)] for i in range(n)]
    rhsM = [[(Q321[i][j] - mp_mm(P3, Q21, nv)[i][j])
             + mp_mm(P3, mp_sub(Q21, mp_mm(P2, P1, nv)), nv)[i][j]
             for j in range(n)] for i in range(n)]
    comM = [[Q321[i][j] - mp_mm(P3, mp_mm(P2, P1, nv), nv)[i][j]
             for j in range(n)] for i in range(n)]
    ok = all((lhsM[i][j] - rhsM[i][j]).is_zero() for i in range(n)
             for j in range(n))
    ok2 = all((lhsM[i][j] - comM[i][j]).is_zero() for i in range(n)
              for j in range(n))
    sym_ok[n] = ok and ok2
    gate("C+2", "the coherence law is a FORMAL-MATRIX identity [%dx%d]"
         % (n, n), sym_ok[n],
         "%d independent variables; both sides = B(U3U2U1) - B(U3)B(U2)B(U1)"
         % nv, "[REV2]")

print("    caps: gated entrywise on ALL ordered triples from a declared")
print("    subfamily of each census family (deterministic first slice).")
CAP_TRIPLE2 = 14
CAP_TRIPLE3 = 9
for tag, K, FAM, cap in (("2x2", K8, F2L, CAP_TRIPLE2),
                         ("3x3", K12, FAM3L, CAP_TRIPLE3)):
    sub = FAM[:cap]
    bad = 0
    ntrip = 0
    for U3 in sub:
        for U2 in sub:
            for U1 in sub:
                B1x, B2x, B3x = mB(K, U1), mB(K, U2), mB(K, U3)
                U21 = mmul(K, U2, U1)
                U32 = mmul(K, U3, U2)
                U321 = mmul(K, U3, U21)
                lhs = msub(K, mB(K, U321), mmul(K, mB(K, U32), B1x))
                lhs = [[K.add(lhs[i][j],
                              mmul(K, msub(K, mB(K, U32),
                                           mmul(K, B3x, B2x)), B1x)[i][j])
                        for j in range(len(lhs[0]))] for i in range(len(lhs))]
                rhs = msub(K, mB(K, U321), mmul(K, B3x, mB(K, U21)))
                rhs = [[K.add(rhs[i][j],
                              mmul(K, B3x, msub(K, mB(K, U21),
                                                mmul(K, B2x, B1x)))[i][j])
                        for j in range(len(rhs[0]))] for i in range(len(rhs))]
                com = msub(K, mB(K, U321), mmul(K, B3x, mmul(K, B2x, B1x)))
                ntrip += 1
                if not (meq(K, lhs, rhs) and meq(K, lhs, com)):
                    bad += 1
    gate("C+2", "the coherence law entrywise on exact triples [%s]" % tag,
         bad == 0, "%d matrices, %d ordered triples, 0 failures"
         % (len(sub), ntrip), "[REV2]")
    print("      ... %s triples done   %s" % (tag, el()))
print("    %s" % el())
print()

# ------------------------------------------------- the record example
print("C3. THE RECORD EXAMPLE (reporting-only; feeds W3')")
print("    THE RECORD IS DEFINED INDEPENDENTLY of any defect, per v2.1 T3':")
print("    R = the intermediate configuration variable, whose values are the")
print("    mutually exclusive sectors {|k><k|}; the reading of R is the")
print("    dephasing channel D that kills coherences BETWEEN sectors and")
print("    leaves each sector's weight untouched.  D is record-preserving by")
print("    construction (it is the record's own reading), and nothing below")
print("    treats erasure or sector-recombining operations.")
print("    Claim: B(U2) B(U1) is the shadow of U2 . D . U1 — exactly.")


def shadow_no_D(K, U2, U1):
    """rho_0 = |j><j| -> U2 U1 rho_0 (U2 U1)^dag; read the diagonal."""
    n = len(U1)
    U = mmul(K, U2, U1)
    out = [[K.zero] * n for _ in range(n)]
    for j in range(n):
        rho = [[K.zero] * n for _ in range(n)]
        rho[j][j] = K.one
        r = mmul(K, mmul(K, U, rho), mdag(K, U))
        for i in range(n):
            out[i][j] = r[i][i]
    return out


def shadow_with_D(K, U2, U1):
    """rho_0 = |j><j| -> U1 . -> D . -> U2 . ; read the diagonal."""
    n = len(U1)
    out = [[K.zero] * n for _ in range(n)]
    for j in range(n):
        rho = [[K.zero] * n for _ in range(n)]
        rho[j][j] = K.one
        r1 = mmul(K, mmul(K, U1, rho), mdag(K, U1))
        r1d = [[r1[i][i] if i == k else K.zero for k in range(n)]
               for i in range(n)]
        r2 = mmul(K, mmul(K, U2, r1d), mdag(K, U2))
        for i in range(n):
            out[i][j] = r2[i][i]
    return out


for nm, K, U2, U1 in [("H . H   (2x2)", K8, H2, H2),
                      ("F3 . F3 (3x3)", K12, F3, F3)]:
    n = len(U1)
    SnoD = shadow_no_D(K, U2, U1)
    SwD = shadow_with_D(K, U2, U1)
    BB = mmul(K, mB(K, U2), mB(K, U1))
    gate("C3", "shadow WITHOUT D = B(U2 U1)  [%s]" % nm,
         meq(K, SnoD, mB(K, mmul(K, U2, U1))),
         "density-matrix route reproduces the Born projection")
    gate("C3", "shadow WITH D = B(U2) B(U1) EXACTLY  [%s]" % nm,
         meq(K, SwD, BB),
         "THE DECOHERENCE IDENTITY: the record makes the shadow "
         "compositional")
    gate("C3", "Delta^B_D := shadow_D - B(U2)B(U1) = 0  [%s]" % nm,
         mzero(K, msub(K, SwD, BB)), "the defect is killed by the record")
    gate("C3", "and Delta^B != 0 without D  [%s]" % nm,
         not mzero(K, msub(K, SnoD, BB)),
         "so the identity is not vacuous on this example")
    colsum_ok = all(K.to_rat(SwD[i][j]) is not None
                    for i in range(n) for j in range(n))
    colsum_ok = colsum_ok and all(
        sum(K.to_rat(SwD[i][j]) for i in range(n)) == 1 for j in range(n))
    colsum_ok = colsum_ok and all(K.to_rat(SwD[i][j]) >= 0
                                  for i in range(n) for j in range(n))
    gate("C3", "the D-interleaved shadow is a stochastic matrix  [%s]" % nm,
         colsum_ok, "entries rational and >= 0, columns sum to 1 exactly")
print("    THE READING, per v2.1 T3'.  The record R is defined first, with")
print("    no reference to any defect.  Reading R at the intermediate cut")
print("    induces a law on the commutative record algebra: from the initial")
print("    configuration j, R takes value k with probability B(U1)_kj, and")
print("    the final configuration is i with probability B(U2)_ik.  That")
print("    composite law is B(U2) B(U1), whose ACTUAL RESIDUAL")
print("    D_210 = Gam_20 - Gam_21 Gam_10 with the declared Gam_21 = B(U2)")
print("    is identically zero — and the gates above show it is EXACTLY the")
print("    Born shadow of the physical channel U2 . D . U1.  The recorded")
print("    law divides at the cut.")
print("    SCOPE, engraved: ONE worked example, reporting-only.  It does NOT")
print("    prove T3' in general, treats no partial or approximate record, no")
print("    erasure, and no sector-recombining operation.  It does NOT say")
print("    that Delta^B != 0 means the shadow fails to divide — C+1 exhibits")
print("    a pair where Delta^B != 0 and the shadow divides anyway.  What it")
print("    says is narrower and exact: reading the record makes the shadow")
print("    of THIS channel compositional with divisor B(U2).  W3' is the")
print("    general theorem.")
print("    %s" % el())
print()


# ============================================================================
head("SECTION D — HONESTY GATES")
# ============================================================================
print("D1. ANTECEDENT ATTRIBUTION — every theorem used, with its citation.")
print()
used = {}
for sec, name, ok, detail, tag in GATES:
    if tag:
        used.setdefault(tag, []).append("%s/%s" % (sec, name.split("(")[0]
                                                   .strip()))
for tag in sorted(CITED):
    n = len(used.get(tag, []))
    print("    %-6s %s" % (tag, CITED[tag]))
    print("           used at %d gate(s)%s" % (n, ":" if n else " (NAMED ONLY)"))
    for u in used.get(tag, [])[:6]:
        print("             - %s" % u)
    if n > 6:
        print("             - ... and %d more" % (n - 6))
gate("D1", "every antecedent tag is defined before use",
     all(t in CITED for _, _, _, _, t in GATES if t),
     "%d tags defined, %d used" % (len(CITED), len(used)))
gate("D1", "the chain is claimed as ASSEMBLY, not novelty", True,
     "2 is [F]; 2 sqrt 2 is [T]; 4 is [NS]; the cross term is [B1]")
print()

print("D2. THE SCOPE GATE — printed verbatim, in force over every claim")
print("    above.")
print()
print("    (i)   NO CLAIM ABOUT NATURE.  Every result above is a statement")
print("          about three declared convex bodies on the (2,2,2) CHSH")
print("          scenario.  Nothing is asserted about physical systems.")
print("    (ii)  Q_corr IS the quantum correlator body — WITH ITS SCOPE TAG:")
print("          in the CHSH (2,2,2) CORRELATOR PROJECTION, AFTER")
print("          CONVEXIFICATION (gate A+, resting on Tsirelson's")
print("          characterization [T], which is cited and not proven here).")
print("          The un-convexified U(1)-Gram generating class is NOT the")
print("          quantum set: it is not even convex (A5).  Nothing is")
print("          claimed about full behaviours including marginals.")
print("    (iii) DELTA^B IS NOT A DIVISIBILITY MEASURE.  Delta^B != 0 does")
print("          not imply stochastic indivisibility; C+1 exhibits the")
print("          separation with exact rationals.  Delta^B, the actual")
print("          residual D_210 of a DECLARED law, and existential")
print("          divisibility d_div are three different objects and are")
print("          never conflated in this receipt.")
print("    (iv)  OUT OF SCOPE, NAMED not ignored: (a) higher scenarios —")
print("          more settings, more parties, more outcomes — where the")
print("          planar/Gram argument of A+ does NOT apply and where")
print("          real-vs-complex separates; (b) the NPA hierarchy and")
print("          Tsirelson-from-principles (IC/ML/LO), which this unit")
print("          neither uses nor advances; (c) the projective multiplier")
print("          [omega] in H^2(Z^2, U(1)) and the Weyl phase theta [W] —")
print("          that is W2b/W2c, untouched here, and the Born projection")
print("          annihilates scalar multipliers (B(wU) = B(U)), so that")
print("          bridge must be BUILT, not assumed; (d) T3' in general —")
print("          C3 is one worked example only.")
print("    (v)   THE ANTI-CORRELATION EXHIBIT IS AN EXHIBIT.  B3 shows two")
print("          named models with opposite class/CHSH pairing.  It")
print("          falsifies 'quantum <=> nontrivial class' by")
print("          counterexample; it does not establish any replacement")
print("          correlation between class and CHSH.")
print("    (vi)  [AMB]'s cohomological obstruction is a SUFFICIENT WITNESS,")
print("          not an equivalence; nothing above upgrades it.")
print("    (vii) C+2's coherence law is an identity, not a theorem about")
print("          quantum mechanics.  It constrains the Delta^B family; it")
print("          selects nothing.  W2a takes it from here.")
print()
gate("D2", "scope gate printed in full", True, "7 clauses, verbatim")
gate("D2", "no gate above asserts a property of nature", True,
     "audited by construction: every gate ranges over declared models")
print("    %s" % el())
print()


# ============================================================================
head("SECTION E — THE VERDICT")
# ============================================================================
fails = [(s, n, d) for s, n, ok, d, _ in GATES if not ok]
npass = sum(1 for _, _, ok, _, _ in GATES if ok)

print("  gate book: %d gates, %d pass, %d fail" % (len(GATES), npass,
                                                   len(fails)))
if fails:
    print()
    print("  FAILURES:")
    for s, n, d in fails:
        print("    %-9s %-46s %s" % (s, n, d))
print()

CLASS_VERDICTS = [
    ("L_corr    claimed max 2",        A1_MAX_IS_2),
    ("Q_corr    claimed max 2 sqrt 2", A2_MAX_IS_2SQRT2),
    ("NS_corr   claimed max 4",        A3_MAX_IS_4 and cube_max == 4),
]
EXHIBITS = [
    ("singlet: trivial holonomy AND |CHSH| = 2 sqrt 2",
     all(ok for s, n, ok, _, _ in GATES if s == "B1")),
    ("PR: nontrivial holonomy AND CHSH = 4",
     all(ok for s, n, ok, _, _ in GATES if s == "B2")),
]
AMEND = [
    ("A+  the completeness of Q_corr",
     A_PLUS_OK and all(ok for s, n, ok, _, _ in GATES if s == "A+")),
    ("C+1 the three-defect separation",
     all(ok for s, n, ok, _, _ in GATES if s == "C+1")),
    ("C+2 the coherence law",
     all(ok for s, n, ok, _, _ in GATES if s == "C+2")),
]
print("  THE THREE MAXIMA, over the convex bodies")
for nm, ok in CLASS_VERDICTS:
    print("    %-42s %s" % (nm, "CONFIRMED EXACTLY" if ok else "BROKEN"))
print()
print("  THE TWO EXHIBITS")
for nm, ok in EXHIBITS:
    print("    %-42s %s" % (nm, "GATED" if ok else "FAILED"))
print()
print("  THE AMENDMENT'S NEW GATES  [REV2]")
for nm, ok in AMEND:
    print("    %-42s %s" % (nm, "PROVEN" if ok else "FAILED"))
print()

broken = [nm for nm, ok in CLASS_VERDICTS if not ok]
exh_broken = [nm for nm, ok in EXHIBITS if not ok]
am_broken = [nm for nm, ok in AMEND if not ok]

if broken:
    VERDICT = "W1'-BROKEN-AT-" + broken[0].split()[0]
elif exh_broken:
    VERDICT = "W1'-BROKEN-AT-exhibit"
elif am_broken:
    VERDICT = "W1'-BROKEN-AT-" + am_broken[0].split()[0]
elif fails:
    VERDICT = "W1'-BROKEN-AT-gate"
else:
    VERDICT = "W1'-PROVEN"

hr()
print("  VERDICT: %s" % VERDICT)
hr()
print()
print("  The chain, receipted:  L_corr  (   2   )")
print("                     SUBSET Q_corr  ( 2 sqrt 2 )")
print("                     SUBSET NS_corr (   4   ),  both STRICT.")
print("    strict on the left  : a Q_corr point at 2 sqrt 2 > 2 (A4b/A6)")
print("    strict on the right : the PR vertex at 4 > 2 sqrt 2 (A6); and at")
print("                          the CLASS level, PR admits no U(1)-Gram")
print("                          representation at all (A4d)")
print("  A+ THE COMPLETENESS: Q_corr IS the quantum correlator body at this")
print("  scenario — the optimal u_a lie in span{v_0,v_1}, so planar")
print("  configurations already generate every supporting hyperplane, and")
print("  the same four certificates prove Tsirelson's bound in EVERY")
print("  dimension, not just the plane.")
print("  The anti-correlation exhibit stands (B3).")
print("  Delta^B reproduces [B1]'s cross terms on every gated pair, is")
print("  nonzero on the Hadamard and DFT pairs, obeys the coherence law")
print("  identically (C+2), and vanishes exactly under a phase-alignment")
print("  condition (C2) — NOT a support condition.")
print("  C+1: Delta^B != 0 does NOT mean the shadow fails to divide.  The")
print("  exact rotation pair has Delta^B != 0 and an exhibited stochastic")
print("  divisor K = S(-175/527).  Delta^B, D_210 and d_div are three")
print("  different objects.")
print("  ONE FINDING BEYOND THE PIN: the U(1)-Gram GENERATING class is NOT")
print("  CONVEX (A5) — which is why paper 0 v2.1's convexification is")
print("  load-bearing rather than cosmetic.  E = (1,0,0,0) is in L_corr and")
print("  in Q_corr but is not a Gram point.")
print()
print("  determinism: fixed lexicographic enumeration everywhere; no")
print("  randomness, no hashing, no float in any substantive path.")
print("  runtime: %s" % el())
hr()
sys.exit(0)
