#!/usr/bin/env python3
"""
w3p_records_exact.py — v12 W3': RECORDS KILL THE DEFECT.

Pin: v12/note-w3p-records-kill-defect-pin.md (STRICT, frozen before this
file existed).  Binding specification: v12 paper 0 v2.1 sec.1 T3' (the
record defined INDEPENDENTLY of the defect: stable variable, mutually
exclusive values = orthogonal record sectors, correlated with the
alternatives, available under the declared future dynamics; claims only
under RECORD-PRESERVING operations; no claim after erasure), T2' (the
three-defect distinction Delta^B / D_210 / d_div), sec.4 W3', sec.5
(non-claims); v12/LOG.md #1-#8; bc/LOG.md #4 (M-1); v11/LOG.md #14, #21.

THE FIVE PARTS
  A  THE THEOREM at finite dimension.  A stable record of {C_r} plus
     record-preserving subsequent dynamics forces the induced law on
     the cut algebra to be DIVISIBLE with the canonical divisor: the
     actual residual D_210 = Gam_20 - Gam_21 Gam_10 vanishes there.
     Two named hypotheses, both of them T3's own definitional clauses
     made computable:
        (H-corr)  PERFECT CORRELATION / SEPARATION — distinct LIVE
                  alternatives at the cut lie in distinct record
                  sectors (the record says which alternative occurred);
        (H-avail) AVAILABILITY / PERSISTENCE — distinct record sectors
                  lead to disjoint sets of later configurations (the
                  record can still be read after the later dynamics).
     The proof is written in the note; the receipt gates its instances
     TERMWISE (every interference cross-term is checked to vanish
     individually, not merely in the sum), plus exact two-step and
     three-step worked examples, a declared census, the load-bearing
     tests of each hypothesis, and the quantitative
     approximately-correlated bound.
  B  THE INSTANCE: bc #4's M-1 biconditional ("legitimate division
     event <=> the process divides at it") on the committed Bell model,
     derived as an instance.  The model is REBUILT INDEPENDENTLY from
     the committed specification (git object cbb7279; the bc working
     tree is dirty with frozen partial edits and is never read) and
     ANCHORED on the committed constants.  The theorem's prediction —
     the cut divides iff some declared record structure satisfies
     (H-corr) and (H-avail) — is then gated against the committed
     divisibility census at all 12 (setting pair, frame) cells.
  C  THE GLOBAL CASE: the multi-cut corollary (records at every cut =>
     the whole chain is Chapman-Kolmogorov), proven by induction in the
     note and gated on exact 3-step and 4-step chains; v11's
     total-factuality arc stated as this corollary's global SHAPE and
     CITED to v11 LOG #14/#21 — v11 is frozen, nothing is re-run.
  D  THE CONVERSE, scoped.  The implication ladder
        records => medium decoherence => Delta^B = 0 => D_210 = 0
        => d_div = 0
     with all three reverse implications refuted by exact receipted
     counterexamples; the decoherent-histories antecedent (medium
     decoherence <=> generalized records, pure states) CITED as the
     known result it is, never claimed.
  E  THE NEGATIVE CONTROL (the eraser): the same record, the same
     initial states, the same first leg — only the later operation
     changes, from record-preserving to coherently record-erasing —
     and the defect RETURNS, maximally (D_210 entries +-1/2 and
     d_div > 0 by an exact argument).  (H-avail) is load-bearing, not
     decorative.  A second eraser is run inside the Bell model itself.

ENGRAVED CONSTRAINTS (paper 0 v2.1 sec.5, carried into every gate)
  * NO CLAIM ABOUT NATURE.  Everything here is a statement about
    declared finite-dimensional models.
  * Delta^B, D_210 and d_div are three different objects (T2'); this
    receipt never equates them and gates their separation itself.
  * The record is defined INDEPENDENTLY of any defect (T3'), and every
    record structure used here is declared before its defect is
    computed.
  * NO CLAIM after record erasure or under sector-recombining
    operations — part E is exactly that boundary, exhibited.
  * Lean: NONE.  W3'-PROVEN and W3'-KILLED are both reportable
    outcomes; the KILL condition is checked and printed explicitly.

HOUSE RULES OBSERVED
  * Exact arithmetic end to end.  fractions.Fraction for rationals; the
    cyclotomic fields Q(zeta_16) and Q(zeta_12) (class Cyc: canonical
    representation modulo Phi_N, so tuple equality IS field equality)
    for every algebraic quantity, including the Bell model's
    cos(pi/8); the real quadratic field Q(sqrt 2) (class Q2) for the
    exact ranks.  No float in any substantive path; no tolerance
    anywhere.
  * Anchors exit 1 and nothing else does.  Substantive negatives exit 0.
  * Antecedents cited at the gate where they are used.
  * Determinism: fixed lexicographic enumeration everywhere; no
    randomness, no hashing, no float.
"""

import sys
import time
from fractions import Fraction as Fr

T0 = time.time()


def el():
    return "%7.1fs" % (time.time() - T0)


def hr(c="="):
    print(c * 78)


def head(title):
    hr()
    print(title)
    hr()


# ============================================================================
# 0.  THE EXACT ARITHMETIC LAYER
# ============================================================================

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
    """Phi_n(x) over Q, by exact division of x^n - 1 by prod_{d|n,d<n} Phi_d."""
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
    r0, r1 = ptrim(a), ptrim(b)
    s0, s1 = [Fr(1)], []
    while r1:
        q, r = pdivmod(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, psub(s0, pmul(q, s1))
    if r0:
        lead = r0[-1]
        r0 = pscal(r0, 1 / lead)
        s0 = pscal(s0, 1 / lead)
    return r0, s0


class Cyc:
    """Q(zeta_n) = Q[x]/Phi_n(x).  Elements are tuples of Fraction of length
    deg = phi(n) in the basis 1, z, ..., z^(deg-1).  Phi_n is irreducible over
    Q [GAUSS], so the representation is CANONICAL: tuple equality IS field
    equality and there is no tolerance anywhere."""

    def __init__(self, n):
        self.n = n
        self.phi = cyclotomic(n)
        self.deg = len(self.phi) - 1
        self.zero = tuple([Fr(0)] * self.deg)
        self.one = self.red([Fr(1)])

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
        """Complex conjugation zeta -> zeta^{-1} (the Galois element z->z^{n-1})."""
        n = self.n
        acc = [Fr(0)] * n
        for k, ak in enumerate(a):
            if ak:
                acc[(n - k) % n] += ak
        return self.red(acc)

    def re(self, a):
        return self.scal(self.add(a, self.conj(a)), Fr(1, 2))

    def normsq(self, a):
        return self.mul(a, self.conj(a))

    def inv(self, a):
        if all(x == 0 for x in a):
            raise ZeroDivisionError
        g, u = pgcdext(list(a), self.phi)
        if g != [Fr(1)]:
            raise ArithmeticError("non-unit in a field")
        return self.red(u)

    def is_zero(self, a):
        return all(x == 0 for x in a)

    def to_rat(self, a):
        if any(x != 0 for x in a[1:]):
            return None
        return a[0]

    def cos(self, k, m):
        """cos(k*pi/m) as (z^j + z^-j)/2 with z = zeta_n, requires 2m | n."""
        assert self.n % (2 * m) == 0
        j = k * (self.n // (2 * m))
        return self.scal(self.add(self.zpow(j), self.zpow(-j)), Fr(1, 2))

    def sin(self, k, m):
        """sin(k*pi/m) = (z^j - z^-j)/(2 i) with i = z^{n/4}, requires 4 | n."""
        assert self.n % 4 == 0 and self.n % (2 * m) == 0
        j = k * (self.n // (2 * m))
        num = self.sub(self.zpow(j), self.zpow(-j))
        return self.scal(self.mul(num, self.zpow(-self.n // 4)), Fr(1, 2))


class Q2:
    """The real quadratic field Q(sqrt 2): pairs (a, b) meaning a + b sqrt 2.
    Used only for the exact ranks of the Bell model's transition matrices."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(self, o):
        return Q2(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return Q2(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def inv(self):
        d = self.a * self.a - 2 * self.b * self.b
        if d == 0:
            raise ZeroDivisionError
        return Q2(self.a / d, -self.b / d)

    def __repr__(self):
        return "(%s%+s r2)" % (self.a, self.b)


# ---------------------------------------------------------------- matrices
def mzeros(K, n, m=None):
    m = n if m is None else m
    return [[K.zero] * m for _ in range(n)]


def mid(K, n):
    return [[K.one if i == j else K.zero for j in range(n)] for i in range(n)]


def mmul(K, A, B):
    """Sparsity-aware exact product."""
    n, k, m = len(A), len(B), len(B[0])
    out = [[K.zero] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        nz = [(t, Ai[t]) for t in range(k) if not K.is_zero(Ai[t])]
        if not nz:
            continue
        row = out[i]
        for t, v in nz:
            Bt = B[t]
            for j in range(m):
                w = Bt[j]
                if not K.is_zero(w):
                    row[j] = K.add(row[j], K.mul(v, w))
    return out


def mdag(K, A):
    return [[K.conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def mB(K, A):
    """The entrywise Born projection B(U)_ij = |U_ij|^2."""
    return [[K.normsq(A[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def msub(K, A, B):
    return [[K.sub(A[i][j], B[i][j]) for j in range(len(A[0]))]
            for i in range(len(A))]


def mzero(K, A):
    return all(K.is_zero(x) for row in A for x in row)


def meq(K, A, B):
    return mzero(K, msub(K, A, B))


def is_unitary(K, U):
    n = len(U)
    return meq(K, mmul(K, mdag(K, U), U), mid(K, n))


def kron(K, A, B):
    na, ma, nb, mb = len(A), len(A[0]), len(B), len(B[0])
    out = mzeros(K, na * nb, ma * mb)
    for i in range(na):
        for j in range(ma):
            if K.is_zero(A[i][j]):
                continue
            for p in range(nb):
                for q in range(mb):
                    if not K.is_zero(B[p][q]):
                        out[i * nb + p][j * mb + q] = K.mul(A[i][j], B[p][q])
    return out


def madd(K, A, B):
    return [[K.add(A[i][j], B[i][j]) for j in range(len(A[0]))]
            for i in range(len(A))]


def sum_field(K, xs):
    s = K.zero
    for x in xs:
        s = K.add(s, x)
    return s


def to_rat_matrix(K, A):
    out = []
    for row in A:
        r = []
        for x in row:
            q = K.to_rat(x)
            if q is None:
                return None
            r.append(q)
        out.append(r)
    return out


def stochastic_rat(M):
    n, m = len(M), len(M[0])
    if any(M[i][j] < 0 for i in range(n) for j in range(m)):
        return False
    return all(sum(M[i][j] for i in range(n)) == 1 for j in range(m))


def rat_mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def rat_rank_q2(M):
    """Exact rank over Q(sqrt 2) by Gauss-Jordan."""
    A = [row[:] for row in M]
    n, m = len(A), len(A[0])
    r = 0
    for c in range(m):
        p = None
        for i in range(r, n):
            if not A[i][c].is_zero():
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c].inv()
        A[r] = [x * pv for x in A[r]]
        for i in range(n):
            if i != r and not A[i][c].is_zero():
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(m)]
        r += 1
        if r == n:
            break
    return r


# ============================================================================
#     GATE BOOK-KEEPING
# ============================================================================
GATES = []
CITED = {}
DECLARATIVE = []


def cite(tag, text):
    CITED[tag] = text


def gate(sec, name, ok, detail="", tag=""):
    GATES.append((sec, name, bool(ok), detail, tag))
    mark = "PASS" if ok else "FAIL"
    line = "  [%s] %-6s %-52s" % (mark, sec, name)
    if detail:
        line += " %s" % detail
    if tag:
        line += "   <%s>" % tag
    print(line)
    return bool(ok)


NANCHOR = [0]


def anchor(name, ok, detail=""):
    if not ok:
        print("  [ANCHOR-FAIL] %-46s %s" % (name, detail))
        print("\nANCHOR FAILURE — a committed constant did not reproduce, or "
              "the exact arithmetic layer is unsound.")
        sys.exit(1)
    NANCHOR[0] += 1
    print("  [anchor] %-52s ok %s" % (name, detail))


# ============================================================================
head("w3p_records_exact.py — v12 W3'")
print("RECORDS KILL THE DEFECT: the T3' theorem at finite dimension, the")
print("bc M-1 instance, the global corollary shape, the scoped converse,")
print("and the eraser negative control")
hr()
print("  pin    : v12/note-w3p-records-kill-defect-pin.md (frozen before")
print("           this file existed)")
print("  binding: v12 paper 0 v2.1 sec.1 T3' (the record defined")
print("           INDEPENDENTLY of the defect) and T2' (the three-defect")
print("           distinction), sec.4 W3', sec.5 (non-claims);")
print("           v12/LOG.md #1-#8; bc/LOG.md #4; v11/LOG.md #14, #21.")
print("  banner : EXACT arithmetic end to end, NO TOLERANCE ANYWHERE.")
print("           Rationals: fractions.Fraction.  Algebraic: class Cyc =")
print("           Q[x]/Phi_N(x) for N = 16 and 12, canonical")
print("           representation, exact conjugation and inversion; the")
print("           Bell model's cos(pi/8) and sin(pi/8) live in Q(zeta_16).")
print("           Exact ranks: class Q2 = Q(sqrt 2).  No float anywhere.")
print("  lean   : NONE.  W3'-PROVEN and W3'-KILLED are both reportable")
print("           outcomes; the KILL condition is evaluated and printed.")
print("  exits  : substantive negatives exit 0; exit 1 is ANCHOR-only.")
print()

cite("[B1]", "Barandes, The Stochastic-Quantum Correspondence, "
     "arXiv:2302.10778 — the Born projection Gamma = |U|^{o2} and the "
     "identification of its composition failure with interference.")
cite("[B3]", "Barandes, Quantum Systems as Indivisible Stochastic "
     "Processes, arXiv:2507.21192 — division events (p.29), the law of "
     "total probability (eqs. 19-20), Theta(t<-0) (eq. 25).")
cite("[GMH]", "Gell-Mann and Hartle, Phys. Rev. D 47, 3345 (1993) — "
     "for a PURE initial state a set of histories medium-decoheres IFF "
     "generalized records exist.  CITED as known; never re-derived and "
     "never claimed as this unit's.")
cite("[GAUSS]", "Phi_n is irreducible over Q — standard; it makes the "
     "Cyc representation canonical, hence tuple equality = field "
     "equality.")
cite("[W1']", "v12/note-w1p-three-class.md, TERMINAL at v12 LOG #7 — the "
     "cross-term identity, the Delta^B = 0 census (phase alignment, NOT "
     "support), the three-defect separation C+1, and the record example "
     "of its sec.8 which is this unit's declared seed.")
cite("[BC2]", "bc/note-bc2-bell-two-frames.md and bc/code/"
     "bc2_two_frames_exact.py at git object cbb7279 (the COMMITTED "
     "state; the bc working tree is dirty with frozen partial edits and "
     "is never read here), with bc/LOG.md #2 and #4.")
cite("[V11]", "v11/LOG.md #14 (U1 TERMINAL) and #21 (U1b TERMINAL) — "
     "cited only; v11 is frozen and nothing of it is re-run.")

# ---------------------------------------------------------------- anchors
K16 = Cyc(16)
K12 = Cyc(12)

anchor("Phi_16 = x^8 + 1", K16.phi == [Fr(1)] + [Fr(0)] * 7 + [Fr(1)],
       "deg %d" % K16.deg)
anchor("Phi_12 = x^4 - x^2 + 1",
       K12.phi == [Fr(1), Fr(0), Fr(-1), Fr(0), Fr(1)], "deg %d" % K12.deg)
_r2 = K16.add(K16.zpow(2), K16.zpow(-2))
anchor("sqrt 2 in Q(zeta_16): (z^2 + z^-2)^2 = 2",
       K16.mul(_r2, _r2) == K16.rat(2), "z^2 - z^6")
_c8 = K16.cos(1, 8)
anchor("cos(pi/8): 8c^4 - 8c^2 + 1 = 0 exactly in Q(zeta_16)",
       K16.is_zero(K16.add(
           K16.sub(K16.scal(K16.mul(K16.mul(_c8, _c8), K16.mul(_c8, _c8)), 8),
                   K16.scal(K16.mul(_c8, _c8), 8)), K16.one)),
       "the Bell model's field is a subfield of Q(zeta_16)")
anchor("cos^2 + sin^2 = 1 at k*pi/8, k = 0..7",
       all(K16.add(K16.mul(K16.cos(k, 8), K16.cos(k, 8)),
                   K16.mul(K16.sin(k, 8), K16.sin(k, 8))) == K16.one
           for k in range(8)), "8 identities")
_w3 = K12.zpow(4)
anchor("zeta_3 in Q(zeta_12): 1 + w + w^2 = 0",
       K12.is_zero(K12.add(K12.add(K12.one, _w3), K12.mul(_w3, _w3))),
       "w = z^4")
anchor("Q2 arithmetic: (1+sqrt2)(-1+sqrt2) = 1",
       (Q2(1, 1) * Q2(-1, 1) - Q2(1, 0)).is_zero(), "and inversion exact")
print()


# ---------------------------------------------------------------- helpers
def had(K):
    """H = (1/sqrt 2) [[1,1],[1,-1]] over Q(zeta_16)."""
    h = K.scal(K.add(K.zpow(2), K.zpow(-2)), Fr(1, 2))   # 1/sqrt2 = sqrt2/2
    return [[h, h], [h, K.neg(h)]]


def dft(K, n, root):
    """The n-point DFT with the declared primitive root."""
    inv = K.scal(K.one, Fr(1, 1))
    # 1/sqrt(n) is not always in the field; use the unnormalized form scaled
    # by a rational when n is a perfect square, else keep the field element.
    powers = [K.one]
    for k in range(1, n):
        powers.append(K.mul(powers[-1], root))
    M = [[powers[(i * j) % n] for j in range(n)] for i in range(n)]
    return M, inv


def f3(K):
    """The normalized 3-point DFT over Q(zeta_12); entries w^{ij}/sqrt3.
    sqrt 3 is in Q(zeta_12): sqrt3 = z + z^-1 = 2 cos(pi/6)."""
    w = K.zpow(4)
    s3 = K.add(K.zpow(1), K.zpow(-1))
    inv3 = K.scal(s3, Fr(1, 3))                       # 1/sqrt3 = sqrt3/3
    powers = [K.one, w, K.mul(w, w)]
    return [[K.mul(powers[(i * j) % 3], inv3) for j in range(3)]
            for i in range(3)]


def cross_terms(K, U2, U1, i, j):
    """The interference cross-terms of [B1] at entry (i, j):
       Delta^B_ij = 2 Re sum_{k<l} (U2)_ik (U1)_kj conj((U2)_il (U1)_lj)."""
    n = len(U1)
    out = []
    for k in range(n):
        for l in range(k + 1, n):
            t = K.mul(K.mul(U2[i][k], U1[k][j]),
                      K.conj(K.mul(U2[i][l], U1[l][j])))
            out.append(((k, l), t))
    return out


def delta_B(K, U2, U1):
    return msub(K, mB(K, mmul(K, U2, U1)), mmul(K, mB(K, U2), mB(K, U1)))


def cnot(K, ctrl, targ, nq):
    """CNOT on nq qubits, big-endian index."""
    n = 2 ** nq
    M = [[K.zero] * n for _ in range(n)]
    for j in range(n):
        bits = [(j >> (nq - 1 - q)) & 1 for q in range(nq)]
        if bits[ctrl] == 1:
            bits[targ] ^= 1
        i = 0
        for q in range(nq):
            i = i * 2 + bits[q]
        M[i][j] = K.one
    return M


def on_qubit(K, G, q, nq):
    """The one-qubit gate G acting on qubit q of nq (big-endian)."""
    M = [[K.one]]
    for t in range(nq):
        M = kron(K, M, G if t == q else mid(K, 2))
    return M


def sectors_of(part):
    """part: a list giving each configuration's record sector label."""
    s = {}
    for k, lab in enumerate(part):
        s.setdefault(lab, []).append(k)
    return s


def h_avail(K, U2, part):
    """(H-avail) AVAILABILITY: no later configuration receives amplitude from
    two different record sectors — the record is still readable afterwards.
    Returns (bool, witness)."""
    n = len(U2)
    for i in range(n):
        labs = set()
        for k in range(n):
            if not K.is_zero(U2[i][k]):
                labs.add(part[k])
                if len(labs) > 1:
                    return False, (i, sorted(labs)[:2])
    return True, None


def h_corr(K, U1, part):
    """(H-corr) PERFECT CORRELATION: in each column of the first leg, at most
    one LIVE alternative per record sector — the record says which alternative
    occurred.  Returns (bool, witness)."""
    n = len(U1)
    m = len(U1[0])
    for j in range(m):
        seen = {}
        for k in range(n):
            if not K.is_zero(U1[k][j]):
                lab = part[k]
                if lab in seen:
                    return False, (j, seen[lab], k, lab)
                seen[lab] = k
    return True, None


# ============================================================================
head("PART A — THE THEOREM AT FINITE DIMENSION")
print("""
  THE RECORD, DEFINED FIRST AND INDEPENDENTLY OF ANY DEFECT (v2.1 T3').
  A record of the alternatives {C_r} at a cut is a variable R whose
  values label MUTUALLY EXCLUSIVE record sectors (an orthogonal
  resolution {P_r} of the identity), PERFECTLY OR APPROXIMATELY
  CORRELATED with those alternatives, and AVAILABLE under the declared
  future dynamics.  No Delta and no divisibility appears in the
  definition, so the theorem below is falsifiable rather than
  definitional.

  THE TWO HYPOTHESES, which are T3's own clauses made computable.
  Write the declared laws in [B1]'s unistochastic form: the cut
  alternatives are the configurations k, the first leg is
  Gam_10 = B(U1), the declared middle leg is the canonical divisor
  Gam_21 = B(U2), and Gam_20 = B(U2 U1).  Fix a record structure: a
  partition of the configurations into record sectors.

    (H-corr)  PERFECT CORRELATION / SEPARATION.  For every initial
              configuration j, the LIVE alternatives at the cut (the
              k with (U1)_kj =/= 0) lie in pairwise DISTINCT record
              sectors.  The record determines which alternative
              occurred: that is what 'perfectly correlated with those
              alternatives' means.

    (H-avail) AVAILABILITY / PERSISTENCE.  For every later
              configuration i, all cut configurations k feeding it
              ((U2)_ik =/= 0) lie in ONE record sector.  The record
              value is still recoverable after the later dynamics:
              that is what 'available under the declared future
              dynamics' and 'record-PRESERVING operations' mean.

  THEOREM (proved in the note; gated termwise below).  (H-corr) and
  (H-avail) together imply that EVERY interference cross-term at the
  cut vanishes INDIVIDUALLY, hence Delta^B(U2, U1) = 0 and

      Gam_20  =  Gam_21 Gam_10  exactly,   i.e.   D_210 = 0

  on the cut algebra, with the canonical divisor Gam_21 = B(U2).
  A SECOND, INDEPENDENT SUFFICIENT MECHANISM (the reading route):
  if the record is physically READ at the cut — the channel is
  U2 . D . U1 with D the pinching onto the record sectors — then
  D_210 = 0 for ANY later dynamics whatever, provided the record
  sectors separate the alternatives.  Both routes are gated.
""")

# ---------------------------------------------------------------- A1
print("A1. THE PROOF'S OWN STEPS, GATED (not merely its conclusion)")
cite("[B1x]", "the cross-term identity Delta^B_ij = 2 Re sum_{k<l} "
     "(U2)_ik (U1)_kj conj((U2)_il (U1)_lj) — [B1]'s identification, "
     "re-derived and gated here independently of [W1'].")

H2 = had(K16)
X2 = [[K16.zero, K16.one], [K16.one, K16.zero]]
I2 = mid(K16, 2)
Z2 = [[K16.one, K16.zero], [K16.zero, K16.neg(K16.one)]]
S2 = [[K16.one, K16.zero], [K16.zero, K16.zpow(4)]]           # diag(1, i)
T2 = [[K16.one, K16.zero], [K16.zero, K16.zpow(2)]]           # diag(1, zeta_8)
F3 = f3(K12)
I3 = mid(K12, 3)
P3 = [[K12.one if (i - j) % 3 == 1 else K12.zero for j in range(3)]
      for i in range(3)]

gate("A1", "H is unitary over Q(zeta_16)", is_unitary(K16, H2),
     "exact")
gate("A1", "F3 is unitary over Q(zeta_12)", is_unitary(K12, F3), "exact")

_ident_bad = 0
_ident_n = 0
for K, U2, U1, nm in [(K16, H2, H2, "H,H"), (K16, mmul(K16, H2, S2), H2,
                                             "HS,H"),
                      (K12, F3, F3, "F3,F3"),
                      (K12, mmul(K12, F3, P3), F3, "F3P,F3")]:
    n = len(U1)
    D = delta_B(K, U2, U1)
    for i in range(n):
        for j in range(n):
            s = K.zero
            for _, t in cross_terms(K, U2, U1, i, j):
                s = K.add(s, K.re(t))
            s = K.scal(s, 2)
            _ident_n += 1
            if not K.is_zero(K.sub(D[i][j], s)):
                _ident_bad += 1
gate("A1", "the cross-term identity holds entrywise", _ident_bad == 0,
     "%d entries over 4 declared pairs, 0 failures" % _ident_n, "[B1x]")

# ---------------------------------------------------------------- A2
print()
print("A2. THE TWO-STEP WORKED EXAMPLE, ROUTE 1 (the record is READ):")
print("    the [W1'] sec.8 seed, re-derived here from scratch")


def pinch(K, rho, part):
    """D(rho) = sum_r P_r rho P_r, the reading of the record."""
    n = len(rho)
    return [[rho[i][j] if part[i] == part[j] else K.zero for j in range(n)]
            for i in range(n)]


def shadow_chain(K, Us, parts):
    """rho_0 = |j><j|, evolve by Us[0], read (pinch by parts[0]), evolve by
    Us[1], read, ... ; return the matrix of final-configuration
    probabilities.  parts[t] = None means no reading at that cut."""
    n = len(Us[0])
    out = [[K.zero] * n for _ in range(n)]
    for j in range(n):
        rho = [[K.zero] * n for _ in range(n)]
        rho[j][j] = K.one
        for t, U in enumerate(Us):
            rho = mmul(K, mmul(K, U, rho), mdag(K, U))
            if t < len(parts) and parts[t] is not None:
                rho = pinch(K, rho, parts[t])
        for i in range(n):
            out[i][j] = rho[i][i]
    return out


for nm, K, U2, U1 in [("H . H  (2x2, Q(zeta_16))", K16, H2, H2),
                      ("F3 . F3 (3x3, Q(zeta_12))", K12, F3, F3)]:
    n = len(U1)
    fine = list(range(n))                     # the finest record: singletons
    BB = mmul(K, mB(K, U2), mB(K, U1))
    sh_read = shadow_chain(K, [U1, U2], [fine, None])
    sh_free = shadow_chain(K, [U1, U2], [None, None])
    gate("A2", "shadow WITHOUT the reading = B(U2 U1)  [%s]" % nm,
         meq(K, sh_free, mB(K, mmul(K, U2, U1))),
         "the density-matrix route reproduces the Born projection")
    gate("A2", "shadow WITH the reading = B(U2) B(U1) EXACTLY  [%s]" % nm,
         meq(K, sh_read, BB), "THE DECOHERENCE IDENTITY")
    gate("A2", "D_210 = 0 on the cut algebra  [%s]" % nm,
         mzero(K, msub(K, sh_read, BB)),
         "canonical divisor Gam_21 = B(U2)")
    gate("A2", "and the defect is NONZERO without the reading  [%s]" % nm,
         not mzero(K, msub(K, sh_free, BB)),
         "so the identity is not vacuous on this example")
    R = to_rat_matrix(K, sh_read)
    gate("A2", "the read shadow is a genuine stochastic matrix  [%s]" % nm,
         R is not None and stochastic_rat(R),
         "rational, non-negative, columns sum to 1 exactly")

print("    THE READING ROUTE ALSO NEEDS (H-corr): reading a record that")
print("    does NOT separate the alternatives does not restore divisibility.")
_coarse = shadow_chain(K16, [on_qubit(K16, H2, 0, 2), on_qubit(K16, H2, 0, 2)],
                       [[0, 1, 0, 1], None])
_finer = shadow_chain(K16, [on_qubit(K16, H2, 0, 2), on_qubit(K16, H2, 0, 2)],
                      [[0, 1, 2, 3], None])
_BBc = mmul(K16, mB(K16, on_qubit(K16, H2, 0, 2)),
            mB(K16, on_qubit(K16, H2, 0, 2)))
gate("A2", "reading a COARSE, non-separating record leaves D_210 =/= 0",
     not meq(K16, _coarse, _BBc),
     "U1 = U2 = H(x)I, record = qubit 1: the pinching keeps the branch "
     "coherences alive")
gate("A2", "while reading the FINE record on the same data gives D_210 = 0",
     meq(K16, _finer, _BBc), "the separating record is what does the work")

# ---------------------------------------------------------------- A3
print()
print("A3. THE TWO-STEP WORKED EXAMPLE, ROUTE 2 (the record is PRESERVED")
print("    and SEPARATING — NO reading anywhere, no decoherence applied):")
print("    a branch qubit and a record qubit, dim 4, basis |b,r> = 2b + r.")


CN01 = cnot(K16, 0, 1, 2)
H_b = on_qubit(K16, H2, 0, 2)
U1_rec = mmul(K16, CN01, H_b)                 # make the record of the branch
U2_pre = H_b                                  # acts on the branch only
part_rec = [0, 1, 0, 1]                       # record = qubit 1 (the r value)

gate("A3", "U1 (branch Hadamard then CNOT into the record) is unitary",
     is_unitary(K16, U1_rec), "dim 4")
gate("A3", "U2 = H on the branch is unitary", is_unitary(K16, U2_pre),
     "dim 4")
ok_c, w_c = h_corr(K16, U1_rec, part_rec)
ok_a, w_a = h_avail(K16, U2_pre, part_rec)
gate("A3", "(H-corr) holds: the record separates the live alternatives",
     ok_c, "checked column by column, 4 columns")
gate("A3", "(H-avail) holds: no later configuration merges two sectors",
     ok_a, "checked row by row, 4 rows")

_term_bad = 0
_term_n = 0
for i in range(4):
    for j in range(4):
        for _, t in cross_terms(K16, U2_pre, U1_rec, i, j):
            _term_n += 1
            if not K16.is_zero(t):
                _term_bad += 1
gate("A3", "THE PROOF STEP: every cross-term vanishes INDIVIDUALLY",
     _term_bad == 0, "%d terms, 0 nonzero" % _term_n, "[B1x]")
gate("A3", "hence Delta^B(U2, U1) = 0 with NO decoherence applied",
     mzero(K16, delta_B(K16, U2_pre, U1_rec)),
     "the record alone kills the defect")
gate("A3", "D_210 = 0: B(U2 U1) = B(U2) B(U1) exactly",
     meq(K16, mB(K16, mmul(K16, U2_pre, U1_rec)),
         mmul(K16, mB(K16, U2_pre), mB(K16, U1_rec))),
     "canonical divisor")
_col0 = [K16.to_rat(mB(K16, mmul(K16, U2_pre, U1_rec))[i][0])
         for i in range(4)]
gate("A3", "the composed law's column 0 is (1/4, 1/4, 1/4, 1/4)",
     _col0 == [Fr(1, 4)] * 4, "exact")

print("    THE CONTRAST (the record removed, everything else identical):")
U1_norec = H_b                                # no CNOT: no record is made
ok_c2, w_c2 = h_corr(K16, U1_norec, part_rec)
gate("A3", "without the CNOT (H-corr) FAILS", not ok_c2,
     "witness column/sector %s" % (w_c2,))
gate("A3", "and Delta^B is nonzero there",
     not mzero(K16, delta_B(K16, U2_pre, U1_norec)),
     "the defect survives when no record is made")

# ---------------------------------------------------------------- A4
print()
print("A4. THE THREE-STEP WORKED EXAMPLES (both routes)")

# route 1: reading at both cuts.  The third leg is chosen NON-unbiased so
# that the unread chain genuinely differs (with three unbiased legs both
# sides collapse to the flat matrix and the non-vacuity check is empty).
ROT35 = [[K16.rat(Fr(3, 5)), K16.rat(Fr(-4, 5))],
         [K16.rat(Fr(4, 5)), K16.rat(Fr(3, 5))]]
for nm, K, U, U3x in [("H,H,R(3/5,4/5) (2x2)", K16, H2, ROT35),
                      ("F3,F3,P3 (3x3)", K12, F3, P3)]:
    n = len(U)
    fine = list(range(n))
    U1, U2, U3 = U, U, U3x
    B1, B2, B3 = mB(K, U1), mB(K, U2), mB(K, U3)
    prod = mmul(K, B3, mmul(K, B2, B1))
    sh = shadow_chain(K, [U1, U2, U3], [fine, fine, None])
    gate("A4", "3-step READ shadow = B(U3) B(U2) B(U1)  [%s]" % nm,
         meq(K, sh, prod), "records at both cuts")
    gate("A4", "CK at cut 1: B(U3 U2 . D . U1) factorizes  [%s]" % nm,
         meq(K, shadow_chain(K, [U1, mmul(K, U3, U2)], [fine, None]),
             mmul(K, mB(K, mmul(K, U3, U2)), B1)),
         "D_210 = 0 at the first cut")
    gate("A4", "CK at cut 2  [%s]" % nm,
         meq(K, sh, mmul(K, B3, shadow_chain(K, [U1, U2], [fine, None]))),
         "D_321 = 0 at the second cut")
    gate("A4", "and the unread 3-step shadow DIFFERS  [%s]" % nm,
         not meq(K, shadow_chain(K, [U1, U2, U3], [None, None]), prod),
         "non-vacuous")

# route 2: a growing record, dim 8, no reading at all
CN01_3 = cnot(K16, 0, 1, 3)
CN02_3 = cnot(K16, 0, 2, 3)
Hb3 = on_qubit(K16, H2, 0, 3)
V1 = mmul(K16, CN01_3, Hb3)                   # record 1 written
V2 = mmul(K16, CN02_3, Hb3)                   # record 2 written
V3 = Hb3                                      # branch only
part_r1 = [(k >> 1) & 1 for k in range(8)]            # record qubit 1
part_r12 = [((k >> 1) & 1) * 2 + (k & 1) for k in range(8)]   # both records
part_r2 = [k & 1 for k in range(8)]

gate("A4", "V1, V2, V3 unitary (dim 8)",
     is_unitary(K16, V1) and is_unitary(K16, V2) and is_unitary(K16, V3),
     "exact")
c1, _ = h_corr(K16, V1, part_r1)
a1, _ = h_avail(K16, mmul(K16, V3, V2), part_r1)
gate("A4", "cut 1 with record r1: (H-corr) and (H-avail) hold", c1 and a1,
     "the later dynamics V3 V2 never merges r1 sectors")
V21 = mmul(K16, V2, V1)
c2, _ = h_corr(K16, V21, part_r12)
a2, _ = h_avail(K16, V3, part_r12)
gate("A4", "cut 2 with the GROWN record (r1, r2): both hypotheses hold",
     c2 and a2, "4 sectors, 8 columns")
gate("A4", "3-step NO-READING chain: B(V3 V2 V1) = B(V3) B(V2) B(V1)",
     meq(K16, mB(K16, mmul(K16, V3, V21)),
         mmul(K16, mB(K16, V3), mmul(K16, mB(K16, V2), mB(K16, V1)))),
     "records at both cuts, no decoherence anywhere")
gate("A4", "and it divides at cut 1 as well",
     mzero(K16, delta_B(K16, mmul(K16, V3, V2), V1)), "D_210 = 0")
gate("A4", "and at cut 2", mzero(K16, delta_B(K16, V3, V21)), "D_321 = 0")

# a 4-step chain, for the induction
CN03_4 = cnot(K16, 0, 3, 4)
CN02_4 = cnot(K16, 0, 2, 4)
CN01_4 = cnot(K16, 0, 1, 4)
Hb4 = on_qubit(K16, H2, 0, 4)
W1 = mmul(K16, CN01_4, Hb4)
W2 = mmul(K16, CN02_4, Hb4)
W3 = mmul(K16, CN03_4, Hb4)
W4 = Hb4
_lhs = mB(K16, mmul(K16, W4, mmul(K16, W3, mmul(K16, W2, W1))))
_rhs = mmul(K16, mB(K16, W4), mmul(K16, mB(K16, W3),
                                   mmul(K16, mB(K16, W2), mB(K16, W1))))
gate("A4", "4-step chain (dim 16, records at three cuts): full CK",
     meq(K16, _lhs, _rhs), "the induction of part C, gated")
print("    (%s)" % el())

# ---------------------------------------------------------------- A5
print()
print("A5. THE DECLARED CENSUS: hypotheses declared first, defect second")

ONE_Q = [("I", I2), ("X", X2), ("H", H2), ("Z", Z2), ("S", S2), ("T", T2)]

CAND2_4, CAND1_4 = [], []
for nm, G in ONE_Q:
    CAND2_4.append(("%s(x)I" % nm, on_qubit(K16, G, 0, 2)))
    CAND2_4.append(("I(x)%s" % nm, on_qubit(K16, G, 1, 2)))
CAND2_4.append(("CNOT01", CN01))
CAND2_4.append(("CNOT10", cnot(K16, 1, 0, 2)))
CAND2_4.append(("H(x)I.CNOT01", mmul(K16, H_b, CN01)))
CAND2_4.append(("CNOT01.H(x)I", mmul(K16, CN01, H_b)))
for nm, G in ONE_Q:
    CAND1_4.append(("%s(x)I" % nm, on_qubit(K16, G, 0, 2)))
    CAND1_4.append(("CNOT01.%s(x)I" % nm,
                    mmul(K16, CN01, on_qubit(K16, G, 0, 2))))
    CAND1_4.append(("CNOT01.I(x)%s" % nm,
                    mmul(K16, CN01, on_qubit(K16, G, 1, 2))))
CAND1_4.append(("CNOT01", CN01))
CAND1_4.append(("H(x)H", mmul(K16, on_qubit(K16, H2, 0, 2),
                              on_qubit(K16, H2, 1, 2))))

_bad_unit = [nm for nm, M in CAND2_4 + CAND1_4 if not is_unitary(K16, M)]
gate("A5", "every census matrix is unitary (dim 4)", not _bad_unit,
     "%d matrices, failures %s" % (len(CAND2_4) + len(CAND1_4), _bad_unit))

_cens = {"hyp_and_zero": 0, "hyp_and_nonzero": 0, "nohyp_and_zero": 0,
         "nohyp_and_nonzero": 0}
_cens_viol = []
_cens_conv = []
for n2, U2 in CAND2_4:
    for n1, U1 in CAND1_4:
        hc, _ = h_corr(K16, U1, part_rec)
        ha, _ = h_avail(K16, U2, part_rec)
        z = mzero(K16, delta_B(K16, U2, U1))
        if hc and ha:
            _cens["hyp_and_zero" if z else "hyp_and_nonzero"] += 1
            if not z:
                _cens_viol.append((n2, n1))
        else:
            _cens["nohyp_and_zero" if z else "nohyp_and_nonzero"] += 1
            if z:
                _cens_conv.append((n2, n1))
gate("A5", "THE THEOREM ON THE dim-4 CENSUS: hypotheses ==> Delta^B = 0",
     not _cens_viol,
     "%d pairs; %d satisfy both hypotheses, all with Delta^B = 0; "
     "violations %s" % (len(CAND2_4) * len(CAND1_4),
                        _cens["hyp_and_zero"], _cens_viol))
gate("A5", "the census is non-vacuous in both cells",
     _cens["hyp_and_zero"] > 0 and _cens["nohyp_and_nonzero"] > 0,
     "hyp+zero %d, nohyp+nonzero %d" % (_cens["hyp_and_zero"],
                                        _cens["nohyp_and_nonzero"]))
gate("A5", "THE CONVERSE FAILS ALREADY HERE: Delta^B = 0 without records",
     len(_cens_conv) > 0,
     "%d pairs with Delta^B = 0 and the record hypotheses FAILING; "
     "first witness (U2, U1) = %s" % (len(_cens_conv), _cens_conv[0]),
     "[W1']")


def sum_gate(K, ctrl, targ, nt, d=3):
    """|a, b> -> |a, b + a mod d> on nt trits (big-endian)."""
    n = d ** nt
    M = [[K.zero] * n for _ in range(n)]
    for j in range(n):
        tr = [(j // (d ** (nt - 1 - q))) % d for q in range(nt)]
        tr[targ] = (tr[targ] + tr[ctrl]) % d
        i = 0
        for q in range(nt):
            i = i * d + tr[q]
        M[i][j] = K.one
    return M


def on_trit(K, G, q, nt, d=3):
    M = [[K.one]]
    for t in range(nt):
        M = kron(K, M, G if t == q else mid(K, d))
    return M


SUM01 = sum_gate(K12, 0, 1, 2)
F3_0 = on_trit(K12, F3, 0, 2)
F3_1 = on_trit(K12, F3, 1, 2)
P3_0 = on_trit(K12, P3, 0, 2)
P3_1 = on_trit(K12, P3, 1, 2)
part_trit = [k % 3 for k in range(9)]                 # record = the 2nd trit

CAND2_9 = [("I", mid(K12, 9)), ("F3(x)I", F3_0), ("P3(x)I", P3_0),
           ("I(x)F3", F3_1), ("I(x)P3", P3_1), ("SUM01", SUM01),
           ("F3(x)I.P3(x)I", mmul(K12, F3_0, P3_0)),
           ("SUM01.F3(x)I", mmul(K12, SUM01, F3_0))]
CAND1_9 = [("F3(x)I", F3_0), ("SUM01.F3(x)I", mmul(K12, SUM01, F3_0)),
           ("I(x)F3", F3_1), ("SUM01.I(x)F3", mmul(K12, SUM01, F3_1)),
           ("P3(x)I", P3_0), ("SUM01", SUM01),
           ("SUM01.P3(x)I", mmul(K12, SUM01, P3_0)),
           ("F3(x)F3", mmul(K12, F3_0, F3_1))]
_bad_unit9 = [nm for nm, M in CAND2_9 + CAND1_9 if not is_unitary(K12, M)]
gate("A5", "every census matrix is unitary (dim 9)", not _bad_unit9,
     "%d matrices, failures %s" % (len(CAND2_9) + len(CAND1_9), _bad_unit9))

_cens9 = {"hz": 0, "hn": 0, "nz": 0, "nn": 0}
_viol9, _conv9 = [], []
for n2, U2 in CAND2_9:
    for n1, U1 in CAND1_9:
        hc, _ = h_corr(K12, U1, part_trit)
        ha, _ = h_avail(K12, U2, part_trit)
        z = mzero(K12, delta_B(K12, U2, U1))
        if hc and ha:
            _cens9["hz" if z else "hn"] += 1
            if not z:
                _viol9.append((n2, n1))
        else:
            _cens9["nz" if z else "nn"] += 1
            if z:
                _conv9.append((n2, n1))
gate("A5", "THE THEOREM ON THE dim-9 CENSUS: hypotheses ==> Delta^B = 0",
     not _viol9,
     "%d pairs; %d satisfy both hypotheses, all with Delta^B = 0; "
     "violations %s" % (len(CAND2_9) * len(CAND1_9), _cens9["hz"], _viol9))
gate("A5", "dim-9 census non-vacuous in both cells",
     _cens9["hz"] > 0 and _cens9["nn"] > 0,
     "hyp+zero %d, nohyp+nonzero %d" % (_cens9["hz"], _cens9["nn"]))


def set_partitions(n):
    """All set partitions of {0..n-1}, as label lists, lexicographic."""
    if n == 0:
        return [[]]
    out = []
    for p in set_partitions(n - 1):
        m = (max(p) + 1) if p else 0
        for lab in range(m + 1):
            out.append(p + [lab])
    return out


PARTS4 = set_partitions(4)
_all_viol, _all_hyp, _all_conv = [], 0, 0
for part in PARTS4:
    for n2, U2 in CAND2_4:
        ha, _ = h_avail(K16, U2, part)
        for n1, U1 in CAND1_4:
            hc, _ = h_corr(K16, U1, part)
            z = mzero(K16, delta_B(K16, U2, U1))
            if hc and ha:
                _all_hyp += 1
                if not z:
                    _all_viol.append((part, n2, n1))
            elif z:
                _all_conv += 1
gate("A5", "OVER ALL %d SET PARTITIONS of the dim-4 configuration space"
     % len(PARTS4), not _all_viol,
     "%d (partition, U2, U1) triples; %d satisfy both hypotheses, all with "
     "Delta^B = 0; violations %s"
     % (len(PARTS4) * len(CAND2_4) * len(CAND1_4), _all_hyp, _all_viol))
print("    (%s)" % el())

print()
print("A5b. THE PROOF'S COMBINATORIAL CORE, VERIFIED EXHAUSTIVELY AT n = 3")
print("     The theorem is a SUPPORT argument, so it can be checked over")
print("     ALL support patterns, with no reference to amplitudes: all")
print("     2^9 = 512 supports for U1, all 512 for U2, all 5 set partitions")
print("     of the 3 configurations — no sampling, no declared cap.")


def supp_matrix(mask, n):
    return [[(mask >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]


def s_corr(S, part, n):
    for j in range(n):
        seen = set()
        for k in range(n):
            if S[k][j]:
                if part[k] in seen:
                    return False
                seen.add(part[k])
    return True


def s_avail(S, part, n):
    for i in range(n):
        labs = set()
        for k in range(n):
            if S[i][k]:
                labs.add(part[k])
                if len(labs) > 1:
                    return False
    return True


def core_holds(S2, S1, n):
    """Every interference cross-term slot has a zero factor."""
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if not (S2[i][k] and S1[k][j]):
                    continue
                for l in range(k + 1, n):
                    if S2[i][l] and S1[l][j]:
                        return False
    return True


_N3 = 3
_ALLS3 = [supp_matrix(m, _N3) for m in range(2 ** (_N3 * _N3))]
PARTS3 = set_partitions(_N3)
_core_bad = []
_core_pairs = 0
_core_sizes = []
for part in PARTS3:
    C = [S for S in _ALLS3 if s_corr(S, part, _N3)]
    A = [S for S in _ALLS3 if s_avail(S, part, _N3)]
    _core_sizes.append((len(C), len(A)))
    for _S2 in A:
        for _S1 in C:
            _core_pairs += 1
            if not core_holds(_S2, _S1, _N3):
                _core_bad.append(part)
                break
        if _core_bad:
            break
    if _core_bad:
        break
gate("A5b", "THE CORE, EXHAUSTIVE at n = 3: hypotheses ==> every "
     "cross-term slot is empty", not _core_bad,
     "%d admissible (partition, U2-support, U1-support) triples over all "
     "512 x 512 supports and all %d partitions; per-partition "
     "(|corr|, |avail|) = %s; violations %s"
     % (_core_pairs, len(PARTS3), _core_sizes, _core_bad))
_core_conv = 0
for part in PARTS3:
    for _S2 in _ALLS3[:64]:
        for _S1 in _ALLS3[:64]:
            if not (s_corr(_S1, part, _N3) and s_avail(_S2, part, _N3)) \
                    and core_holds(_S2, _S1, _N3):
                _core_conv += 1
gate("A5b", "the core's converse fails combinatorially too", _core_conv > 0,
     "%d support pairs in a declared 64x64 corner have empty cross-terms "
     "without satisfying the hypotheses" % _core_conv)

print()
print("A5c. THE TWO KNOWN MONOMIAL SUFFICIENCY CONDITIONS ARE THE THEOREM")
print("     AT ITS TWO EXTREME RECORD STRUCTURES ([W1'] sec.5's structural")
print("     conditions: a row-monomial left factor, a column-monomial right")
print("     factor).  Verified over ALL 512 supports at n = 3.")
_fine3 = list(range(_N3))
_triv3 = [0] * _N3


def row_monomial(S, n):
    return all(sum(S[i]) <= 1 for i in range(n))


def col_monomial(S, n):
    return all(sum(S[k][j] for k in range(n)) <= 1 for j in range(n))


gate("A5c", "(H-avail) at the FINEST record <=> U2 is row-monomial",
     all(s_avail(S, _fine3, _N3) == row_monomial(S, _N3) for S in _ALLS3),
     "all 512 supports, both directions")
gate("A5c", "(H-corr) at the FINEST record is automatic",
     all(s_corr(S, _fine3, _N3) for S in _ALLS3), "all 512 supports")
gate("A5c", "(H-corr) at the TRIVIAL record <=> U1 is column-monomial",
     all(s_corr(S, _triv3, _N3) == col_monomial(S, _N3) for S in _ALLS3),
     "all 512 supports, both directions")
gate("A5c", "(H-avail) at the TRIVIAL record is automatic",
     all(s_avail(S, _triv3, _N3) for S in _ALLS3), "all 512 supports")
_mid_only = []
for part in PARTS4:
    for n2, U2 in CAND2_4:
        S2m = [[0 if K16.is_zero(U2[i][j]) else 1 for j in range(4)]
               for i in range(4)]
        if row_monomial(S2m, 4):
            continue
        ha, _ = h_avail(K16, U2, part)
        if not ha:
            continue
        for n1, U1 in CAND1_4:
            S1m = [[0 if K16.is_zero(U1[i][j]) else 1 for j in range(4)]
                   for i in range(4)]
            if col_monomial(S1m, 4):
                continue
            hc, _ = h_corr(K16, U1, part)
            if hc:
                _mid_only.append((n2, n1))
gate("A5c", "and the INTERMEDIATE record structures are strictly stronger",
     len(_mid_only) > 0,
     "%d dim-4 pairs where NEITHER monomial condition holds yet a middle "
     "record structure gives Delta^B = 0; first %s"
     % (len(_mid_only), _mid_only[0] if _mid_only else None))
print("    (%s)" % el())

# ---------------------------------------------------------------- A6
print()
print("A6. EACH HYPOTHESIS IS LOAD-BEARING, EXACTLY")

ok_a6a, w_a6a = h_avail(K16, U2_pre, part_rec)
ok_c6a, w_c6a = h_corr(K16, U1_norec, part_rec)
gate("A6", "(H-corr) DROPPED: (H-avail) still holds, (H-corr) fails",
     ok_a6a and not ok_c6a,
     "U1 = H(x)I, U2 = H(x)I, record = qubit 1; witness %s" % (w_c6a,))
_d6 = delta_B(K16, U2_pre, U1_norec)
gate("A6", "and the defect SURVIVES: Delta^B =/= 0",
     not mzero(K16, _d6),
     "entry (0,0) = %s" % (K16.to_rat(_d6[0][0]),))
_x = mmul(K16, on_qubit(K16, H2, 1, 2), CN01)      # merges the record sectors
ok_a6b, w_a6b = h_avail(K16, _x, part_rec)
ok_c6b, _ = h_corr(K16, U1_rec, part_rec)
gate("A6", "(H-avail) DROPPED, exhibit 1: (H-corr) holds, (H-avail) fails",
     ok_c6b and not ok_a6b,
     "U2 = (I(x)H).CNOT01 merges the two record sectors; witness %s"
     % (w_a6b,))
gate("A6", "yet Delta^B = 0 THERE — a NEGATIVE, reported not hidden",
     mzero(K16, delta_B(K16, _x, U1_rec)),
     "dropping a hypothesis does not by ITSELF restore the defect: the "
     "hypotheses are sufficient, never claimed necessary ([W1']: "
     "Delta^B = 0 is phase alignment, strictly weaker than any support "
     "condition)")
_x2 = mmul(K16, H_b, CN01)                          # the eraser of part E
ok_a6c, w_a6c = h_avail(K16, _x2, part_rec)
gate("A6", "(H-avail) DROPPED, exhibit 2 (the eraser): the defect RETURNS",
     (not ok_a6c) and not mzero(K16, delta_B(K16, _x2, U1_rec)),
     "U2 = (H(x)I).CNOT01 coherently erases the record; part E computes "
     "the returned D_210 exactly")

# ---------------------------------------------------------------- A7
print()
print("A7. THE KILL CONDITION, EVALUATED HONESTLY")
print("    KILL = 'a stable record with surviving D_210 ON ITS OWN ALGEBRA")
print("    under record-preserving dynamics'.  A6's first instance has a")
print("    stable, preserved record AND a surviving D_210 — so the phrase")
print("    'on its own algebra' is load-bearing and is tested here.")


def lumpable(K, M, part):
    """Strong lumpability of a stochastic matrix over the record partition:
    sum over a target sector is constant across each source sector."""
    n = len(M)
    secs = sectors_of(part)
    labs = sorted(secs)
    for sl in labs:
        for tl in labs:
            vals = set()
            for j in secs[sl]:
                s = Fr(0)
                for i in secs[tl]:
                    q = K.to_rat(M[i][j])
                    if q is None:
                        return False, None
                    s += q
                vals.add(s)
            if len(vals) > 1:
                return False, None
    L = [[None] * len(labs) for _ in range(len(labs))]
    for a, sl in enumerate(labs):
        j = secs[sl][0]
        for b, tl in enumerate(labs):
            L[b][a] = sum(K.to_rat(M[i][j]) for i in secs[tl])
    return True, L


_B1a = mB(K16, U1_norec)
_B2a = mB(K16, U2_pre)
_B20a = mB(K16, mmul(K16, U2_pre, U1_norec))
_l1, L1 = lumpable(K16, _B1a, part_rec)
_l2, L2 = lumpable(K16, _B2a, part_rec)
_l3, L3 = lumpable(K16, _B20a, part_rec)
gate("A7", "all three legs ARE strongly lumpable onto the record algebra",
     _l1 and _l2 and _l3, "so the record's own law is well defined")
gate("A7", "the record's OWN law is the identity and DIVIDES exactly",
     L1 == [[Fr(1), Fr(0)], [Fr(0), Fr(1)]] and L3 == rat_mm(L2, L1),
     "D_210 = 0 on the record algebra: L_20 = L_21 L_10")
gate("A7", "while the surviving residual lives on the BRANCH algebra",
     not mzero(K16, msub(K16, _B20a, mmul(K16, _B2a, _B1a))),
     "of which R is NOT a record — (H-corr) fails there (A6)")
print("    VERDICT ON THE KILL: it does NOT fire on this instance.  The")
print("    residual survives on an algebra the record is not a record OF.")
print("    The honest content: T3's clause 'perfectly correlated with those")
print("    alternatives' is NOT decoration — it is the hypothesis (H-corr),")
print("    and without it a stable, preserved record leaves D_210 alive on")
print("    the alternatives it fails to separate.")

# ---------------------------------------------------------------- A8
print()
print("A8. 'APPROXIMATELY CORRELATED' MADE QUANTITATIVE (exact, rational)")
print("    THE STABILITY BOUND, proven in the note:")
print("      sum_i |D_210(i|j)|  <=  sum_r Gam_10(r|j) ||sig_{r|j} - sig_r||_1")
print("    A declared classical family: the cut carries a record value r and")
print("    an UNRECORDED residue m; the later readout reads m.")

_appr_rows = []
_appr_bad = 0
for e in [Fr(1, 4), Fr(1, 8), Fr(1, 16), Fr(1, 32), Fr(1, 64), Fr(0)]:
    G10 = [[Fr(1, 2), Fr(1, 2) - e],          # k = (r=0,m=0)
           [Fr(0), e],                        # k = (r=0,m=1)
           [Fr(1, 2), Fr(1, 2) - e],          # k = (r=1,m=0)
           [Fr(0), e]]                        # k = (r=1,m=1)
    G2 = [[Fr(1), Fr(0), Fr(1), Fr(0)],       # reads m
          [Fr(0), Fr(1), Fr(0), Fr(1)]]
    G20 = rat_mm(G2, G10)
    Grec10 = [[Fr(1, 2), Fr(1, 2)], [Fr(1, 2), Fr(1, 2)]]
    Ghat21 = [[Fr(1), Fr(1)], [Fr(0), Fr(0)]]     # built from j = 0
    D210 = [[G20[i][j] - rat_mm(Ghat21, Grec10)[i][j] for j in range(2)]
            for i in range(2)]
    lhs = max(sum(abs(D210[i][j]) for i in range(2)) for j in range(2))
    bound = 4 * e
    _appr_rows.append((e, lhs, bound))
    if not (lhs <= bound):
        _appr_bad += 1
gate("A8", "the stability bound holds on the declared family",
     _appr_bad == 0,
     "6 values of the deviation; (e, LHS, bound) = %s"
     % [(str(a), str(b), str(c)) for a, b, c in _appr_rows])
gate("A8", "the bound is TIGHT (equality at every point of the family)",
     all(b == c for _, b, c in _appr_rows), "not merely an inequality")
gate("A8", "an EXACT record (deviation 0) gives D_210 = 0 exactly",
     _appr_rows[-1][1] == 0, "the theorem's exact case is the limit")


# ============================================================================
head("PART B — THE INSTANCE: bc #4's M-1 ON THE COMMITTED BELL MODEL")
print("""
  THE MODEL, REBUILT INDEPENDENTLY from the committed specification
  [BC2] (git object cbb7279; the bc WORKING TREE is dirty with frozen
  partial edits and is never read).  Configuration space
  C = (qA, qB, pA, pB), |C| = 2*2*3*3 = 36, index
  i = ((qA*2 + qB)*3 + pA)*3 + pB, initial configuration j0 = 0.
  U_prep carries j0 to the singlet; U_X(theta) = sum_s Pi^theta_s (x)
  Sh^{n(s)} with Sh the 3-cycle r -> + -> - -> r and n(+) = 1,
  n(-) = 2.  Frames F1 = (prep, A, B) and F2 = (prep, B, A), target
  times 0..3, division events {0, 2, 3}, second-leg operator U_B in F1
  and U_A in F2 ([B3] eq. 25, p.29).  Everything is real orthogonal and
  lives in Q(cos(pi/8)) < Q(zeta_16).

  M-1 ([BC2], bc/LOG.md #4): the declared intermediate division event
  VIOLATES the law of total probability ([B3] eqs. 19-20) at SP-C/D/F —
  on this model "legitimate division event <=> the process divides at
  it".  W3' derives that biconditional as an instance: the cut divides
  exactly where a DECLARED RECORD STRUCTURE satisfies (H-corr) and
  (H-avail), and the reading of the record REPAIRS every illegitimate
  cut.
""")

NC = 36


def cfg(i):
    return ((i // 18) % 2, (i // 9) % 2, (i // 3) % 3, i % 3)


SH = [[K16.zero, K16.zero, K16.one],
      [K16.one, K16.zero, K16.zero],
      [K16.zero, K16.one, K16.zero]]
SH2 = mmul(K16, SH, SH)
I2c = mid(K16, 2)
I3c = mid(K16, 3)
I9c = mid(K16, 9)


def proj_pair(theta):
    """Pi_+ and Pi_- for the coplanar direction theta (degrees); the
    half-angle theta/2 is k*pi/8 with k = theta/45."""
    assert theta % 45 == 0
    k = theta // 45
    ct, st = K16.cos(k, 8), K16.sin(k, 8)
    vp = [ct, st]
    vm = [K16.neg(st), ct]
    Pp = [[K16.mul(vp[i], vp[j]) for j in range(2)] for i in range(2)]
    Pm = [[K16.mul(vm[i], vm[j]) for j in range(2)] for i in range(2)]
    return Pp, Pm


def U_meas(theta, wing):
    Pp, Pm = proj_pair(theta)
    out = mzeros(K16, NC)
    for P, sh in ((Pp, SH), (Pm, SH2)):
        if wing == "A":
            spin, ptr = kron(K16, P, I2c), kron(K16, sh, I3c)
        else:
            spin, ptr = kron(K16, I2c, P), kron(K16, I3c, sh)
        out = madd(K16, out, kron(K16, spin, ptr))
    return out


R2H = K16.scal(K16.add(K16.zpow(2), K16.zpow(-2)), Fr(1, 2))    # 1/sqrt2
_z = K16.zero
PREP4 = [[_z, R2H, R2H, _z],
         [R2H, _z, _z, R2H],
         [K16.neg(R2H), _z, _z, R2H],
         [_z, R2H, K16.neg(R2H), _z]]
U_PREP = kron(K16, PREP4, I9c)

SETTINGS = [("SP-A", 0, 45), ("SP-B", 0, 135), ("SP-C", 90, 45),
            ("SP-D", 90, 135), ("SP-E", 0, 0), ("SP-F", 45, 45)]
UA = {a: U_meas(a, "A") for a in sorted({s[1] for s in SETTINGS})}
UB = {b: U_meas(b, "B") for b in sorted({s[2] for s in SETTINGS})}


def real_matrix(K, M):
    return all(K.conj(x) == x for row in M for x in row)


_ops = [("U_prep", U_PREP)] + [("U_A(%d)" % a, U) for a, U in sorted(UA.items())] \
    + [("U_B(%d)" % b, U) for b, U in sorted(UB.items())]
anchor("every Bell operator is real and exactly orthogonal",
       all(real_matrix(K16, M) and is_unitary(K16, M) for _, M in _ops),
       "%d operators, U^T U = I entry by entry" % len(_ops))
anchor("[U_A(a), U_B(b)] = 0 at all operator pairs",
       all(meq(K16, mmul(K16, UA[a], UB[b]), mmul(K16, UB[b], UA[a]))
           for a in UA for b in UB),
       "%d pairs" % (len(UA) * len(UB)))
anchor("U_prep's j0 column is exactly the singlet",
       K16.is_zero(PREP4[0][0]) and PREP4[1][0] == R2H
       and PREP4[2][0] == K16.neg(R2H) and K16.is_zero(PREP4[3][0]),
       "(0, 1/sqrt2, -1/sqrt2, 0) on (00, 01, 10, 11)")

FR = {}
for nm, a, b in SETTINGS:
    for fr in ("F1", "F2"):
        first, second = (UA[a], UB[b]) if fr == "F1" else (UB[b], UA[a])
        Th2 = mmul(K16, first, U_PREP)
        Th3 = mmul(K16, second, Th2)
        FR[(nm, fr)] = {"first": first, "second": second, "Th2": Th2,
                        "Th3": Th3, "G20": mB(K16, Th2),
                        "G30": mB(K16, Th3), "G32": mB(K16, second),
                        "a": a, "b": b}
print("  Bell model built for all 6 setting pairs x 2 frames (%s)" % el())

# ------ anchor: the singlet statistics -----------------------------------
_qm_bad = []
for nm, a, b in SETTINGS:
    kk = (a - b) // 45 * 2 // 2                       # (a-b)/22.5 in pi/8 units
    kk = (a - b) * 2 // 45
    cd = K16.cos(kk, 8)
    for fr in ("F1", "F2"):
        p3 = [FR[(nm, fr)]["G30"][i][0] for i in range(NC)]
        joint = {}
        for al in (1, -1):
            for be in (1, -1):
                s = K16.zero
                for i in range(NC):
                    _, _, pA, pB = cfg(i)
                    oA = {1: 1, 2: -1}.get(pA)
                    oB = {1: 1, 2: -1}.get(pB)
                    if oA == al and oB == be:
                        s = K16.add(s, p3[i])
                joint[(al, be)] = s
                want = K16.scal(K16.sub(K16.one, K16.scal(cd, al * be)),
                                Fr(1, 4))
                if not K16.is_zero(K16.sub(s, want)):
                    _qm_bad.append((nm, fr, al, be))
        for al in (1, -1):
            mA = K16.add(joint[(al, 1)], joint[(al, -1)])
            mBw = K16.add(joint[(1, al)], joint[(-1, al)])
            if K16.to_rat(mA) != Fr(1, 2) or K16.to_rat(mBw) != Fr(1, 2):
                _qm_bad.append((nm, fr, "marginal", al))
anchor("the exact singlet outcome law reproduces in both frames",
       not _qm_bad,
       "P(al,be) = (1 - al be cos(a-b))/4 and both marginals 1/2; "
       "%d exact identities" % (len(SETTINGS) * 2 * 8))

# ------ anchor: the committed divisibility census ------------------------
COMMITTED_DIFF = {"SP-A": (0, 0), "SP-B": (0, 0), "SP-C": (576, 576),
                  "SP-D": (576, 576), "SP-E": (0, 0), "SP-F": (576, 576)}
COMMITTED_RANK = {"SP-A": (18, 18), "SP-B": (18, 18), "SP-C": (9, 18),
                  "SP-D": (9, 18), "SP-E": (18, 18), "SP-F": (18, 18)}

_diff = {}
for nm, a, b in SETTINGS:
    row = []
    for fr in ("F1", "F2"):
        F = FR[(nm, fr)]
        prod = mmul(K16, F["G32"], F["G20"])
        d = sum(1 for i in range(NC) for j in range(NC)
                if not K16.is_zero(K16.sub(prod[i][j], F["G30"][i][j])))
        row.append(d)
        F["prod"] = prod
        F["divides"] = (d == 0)
    _diff[nm] = tuple(row)
anchor("the committed divisibility census reproduces exactly",
       _diff == COMMITTED_DIFF,
       "Gam(3<-2)Gam(2<-0) vs Gam(3<-0) differing entries per (SP, F1, F2): "
       "%s" % _diff)


def to_q2(K, x):
    c = x
    if any(c[t] != 0 for t in (1, 3, 4, 5, 7)) or c[2] != -c[6]:
        return None
    return Q2(c[0], c[2])


_rank = {}
_conv_bad = 0
for nm, a, b in SETTINGS:
    rr = []
    for fr in ("F1", "F2"):
        M = FR[(nm, fr)]["G20"]
        Q = [[to_q2(K16, M[i][j]) for j in range(NC)] for i in range(NC)]
        if any(x is None for row in Q for x in row):
            _conv_bad += 1
            rr.append(-1)
        else:
            rr.append(rat_rank_q2(Q))
    _rank[nm] = tuple(rr)
gate("B0", "every Gam(2<-0) entry lies in Q(sqrt 2), exactly",
     _conv_bad == 0, "12 matrices, 1296 entries each")
anchor("the committed exact ranks of Gam(2<-0) reproduce",
       _rank == COMMITTED_RANK,
       "%s (full rank would be 36) — [B3] eq. 22's hypothesis fails"
       % _rank)

_cert = []
for nm, a, b in SETTINGS:
    # Alice's division event is t = 2 in F1 (prep, A, B) and t = 3 in F2.
    pA_F1 = [FR[(nm, "F1")]["G20"][i][0] for i in range(NC)]
    pA_F2 = [FR[(nm, "F2")]["G30"][i][0] for i in range(NC)]
    rdy1 = K16.to_rat(sum_field(K16, [pA_F1[i] for i in range(NC)
                                      if cfg(i)[3] == 0]))
    rdy2 = K16.to_rat(sum_field(K16, [pA_F2[i] for i in range(NC)
                                      if cfg(i)[3] == 0]))
    _cert.append((nm, rdy1, rdy2))
anchor("the basis-free 1-vs-0 pointer certificate reproduces",
       all(r1 == 1 and r2 == 0 for _, r1, r2 in _cert),
       "Pr[pointer B still ready] AT ALICE'S DIVISION EVENT = 1 in F1 "
       "(t = 2) and 0 in F2 (t = 3), at all six setting pairs")
print()

# ------ the declared record structures -----------------------------------
print("B1. THE DECLARED RECORD STRUCTURES (declared before any defect is")
print("    computed, per T3'), and the two hypotheses evaluated on each")

COORD = ["qA", "qB", "pA", "pB"]


def coord_part(sub):
    """The record structure that reads exactly the declared coordinates."""
    out = []
    for k in range(NC):
        c = cfg(k)
        out.append(tuple(c[t] for t in sub))
    labs = {v: i for i, v in enumerate(sorted(set(out)))}
    return [labs[v] for v in out]


RECORD_STRUCTURES = []
for _m in range(16):
    _sub = tuple(t for t in range(4) if (_m >> t) & 1)
    _nm = "RS-%02d {%s}" % (_m, ",".join(COORD[t] for t in _sub) or "-")
    RECORD_STRUCTURES.append((_nm, coord_part(_sub)))
PARTS = RECORD_STRUCTURES
print("    THE DECLARED FAMILY: all 16 record structures that read a SUBSET")
print("    of the four configuration coordinates (qA, qB, pA, pB) — from")
print("    the trivial one-sector structure {} to the finest {qA,qB,pA,pB}.")
_sizes_ok = True
for _m in range(16):
    _sub = tuple(t for t in range(4) if (_m >> t) & 1)
    _want = 1
    for t in _sub:
        _want *= 2 if t < 2 else 3
    _p = PARTS[_m][1]
    if len(set(_p)) != _want or sorted(set(_p)) != list(range(_want)):
        _sizes_ok = False
gate("B1", "the 16 declared record structures are genuine partitions",
     _sizes_ok and len(PARTS) == 16,
     "sector counts %s (1 .. 36)" % [len(set(p)) for _, p in PARTS])

_pres_bad = []
for a in sorted(UA):
    for s in range(3):
        P = [[K16.one if (i == j and cfg(i)[2] == s) else K16.zero
              for j in range(NC)] for i in range(NC)]
        for b in sorted(UB):
            if not meq(K16, mmul(K16, UB[b], P), mmul(K16, P, UB[b])):
                _pres_bad.append((b, s))
gate("B1", "Bob's operator commutes with EVERY pointer-A sector projector",
     not _pres_bad,
     "[U_B(b), P^A_s] = 0 for all b and s — Alice's record is preserved "
     "by Bob's measurement, exactly")

_pred = {}
for nm, a, b in SETTINGS:
    for fr in ("F1", "F2"):
        F = FR[(nm, fr)]
        wins = []
        for pn, part in PARTS:
            hc, _ = h_corr(K16, F["Th2"], part)
            ha, _ = h_avail(K16, F["second"], part)
            if hc and ha:
                wins.append(pn.split(" ", 1)[1])
        _pred[(nm, fr)] = wins
        F["wins"] = wins

_mismatch = []
for nm, a, b in SETTINGS:
    for i, fr in enumerate(("F1", "F2")):
        predicted = len(_pred[(nm, fr)]) > 0
        actual = FR[(nm, fr)]["divides"]
        if predicted and not actual:
            _mismatch.append(("FALSE POSITIVE", nm, fr))
        if actual and not predicted:
            _mismatch.append(("no record found", nm, fr))
gate("B2", "THE THEOREM'S DIRECTION: a record structure ==> the cut divides",
     not any(m[0] == "FALSE POSITIVE" for m in _mismatch),
     "no false positive in 12 (setting pair, frame) cells")
gate("B2", "AND THE BICONDITIONAL HOLDS ON THIS MODEL, 12/12 cells",
     not _mismatch,
     "divides <=> some declared record structure satisfies (H-corr) and "
     "(H-avail); MEASURED over the declared family, not proven in general")
for nm, a, b in SETTINGS:
    print("      %-5s a=%3d b=%3d | F1 %-9s wins %-22s | F2 %-9s wins %s"
          % (nm, a, b,
             "DIVIDES" if FR[(nm, "F1")]["divides"] else "indivisible",
             ",".join(_pred[(nm, "F1")]) or "-",
             "DIVIDES" if FR[(nm, "F2")]["divides"] else "indivisible",
             ",".join(_pred[(nm, "F2")]) or "-"))
print("    THE MECHANISM, exact: in F1 at a = 0 Alice's measurement is a")
print("    CONFIGURATION PERMUTATION, so the two singlet branches leave the")
print("    cut in DIFFERENT pointer-A sectors and Bob — who never touches")
print("    pointer A — cannot bring them back to one configuration.  At")
print("    a = 45 or 90 the pointer still records Alice's OUTCOME, but two")
print("    live alternatives share a pointer sector: (H-corr) fails, the")
print("    cross-terms survive, and the law does not divide.")

# ------ B3: the reading repairs the illegitimate cuts --------------------
print()
print("B3. THE READING REPAIRS EVERY ILLEGITIMATE DIVISION EVENT")
_rep_bad, _rep_diff = [], {}
for nm, a, b in SETTINGS:
    for fr in ("F1", "F2"):
        F = FR[(nm, fr)]
        v = [F["Th2"][i][0] for i in range(NC)]
        rho = [[K16.mul(v[i], K16.conj(v[j])) for j in range(NC)]
               for i in range(NC)]
        rho = [[rho[i][j] if i == j else K16.zero for j in range(NC)]
               for i in range(NC)]
        out = mmul(K16, mmul(K16, F["second"], rho), mdag(K16, F["second"]))
        col = [out[i][i] for i in range(NC)]
        want = [F["prod"][i][0] for i in range(NC)]
        if any(not K16.is_zero(K16.sub(col[i], want[i])) for i in range(NC)):
            _rep_bad.append((nm, fr))
        d = sum(1 for i in range(NC) for j in range(NC)
                if not K16.is_zero(K16.sub(F["prod"][i][j], F["G30"][i][j])))
        _rep_diff[(nm, fr)] = d
gate("B3", "the READ model's law = Gam(3<-2) Gam(2<-0) (density-matrix route)",
     not _rep_bad,
     "j0 column recomputed through rho -> pinch -> conjugate at all 12 cells")
gate("B3", "so the READ model satisfies the LTP at EVERY declared cut",
     True, "by construction: reading is the pinching onto the record sectors",
     "[B3]")
gate("B3", "and it differs from the UNREAD model exactly at SP-C/D/F",
     all((_rep_diff[(nm, fr)] > 0) == (not FR[(nm, fr)]["divides"])
         for nm, _, _ in SETTINGS for fr in ("F1", "F2")),
     "differing entries %s"
     % {k: v for k, v in sorted(_rep_diff.items()) if v})
print("    M-1 DERIVED: [B3]'s law of total probability at a declared")
print("    division event IS D_210 = 0 with the canonical divisor, so")
print("    'legitimate division event <=> the process divides at it' is the")
print("    definition made explicit; W3' supplies the missing WHY — the")
print("    legitimate cuts are exactly the RECORD cuts, and reading the")
print("    record at an illegitimate cut makes it legitimate.")

# ------ B4: the eraser inside the Bell model -----------------------------
print()
print("B4. AN ERASER INSIDE THE BELL MODEL (feeds part E)")
print("    A first, FAILED attempt, reported: undoing only Alice's")
print("    measurement, second leg U_B(45) U_A(0)^T, is NOT an eraser —")
print("    U_A(0) is a configuration PERMUTATION, so un-permuting relabels")
print("    the record instead of recombining it, and the defect stays 0.")
_Fa = FR[("SP-A", "F1")]
UAt = mdag(K16, UA[0])
_second_perm = mmul(K16, UB[45], UAt)
_perm_wins = [pn.split(" ", 1)[1] for pn, part in PARTS
              if h_corr(K16, _Fa["Th2"], part)[0]
              and h_avail(K16, _second_perm, part)[0]]
gate("B4", "the permutation 'eraser' leaves record structures intact",
     len(_perm_wins) > 0,
     "wins %s — a permutation merges no sectors, so it erases nothing"
     % _perm_wins)
gate("B4", "and the defect stays 0 there, as the theorem then requires",
     mzero(K16, delta_B(K16, _second_perm, _Fa["Th2"])),
     "reported as the negative it is")
print("    THE GENUINE ERASER: the exact time-reverse of the first leg,")
print("    second = Theta(2<-0)^T, which recombines the two branches onto")
print("    one configuration.")
second_er = mdag(K16, _Fa["Th2"])
_er_wins = []
for pn, part in PARTS:
    hc, _ = h_corr(K16, _Fa["Th2"], part)
    ha, _ = h_avail(K16, second_er, part)
    if hc and ha:
        _er_wins.append(pn.split(" ", 1)[1])
gate("B4", "the coherent eraser destroys EVERY declared record structure",
     not _er_wins,
     "second leg Theta(2<-0)^T at SP-A/F1; wins %s" % (_er_wins or "none"))
_G30_er = mB(K16, mmul(K16, second_er, _Fa["Th2"]))
_prod_er = mmul(K16, mB(K16, second_er), _Fa["G20"])
_der = sum(1 for i in range(NC) for j in range(NC)
           if not K16.is_zero(K16.sub(_prod_er[i][j], _G30_er[i][j])))
gate("B4", "and the DEFECT RETURNS at a cut that divided", _der > 0,
     "%d differing entries where the un-erased cut had 0" % _der)
print("    (%s)" % el())


# ============================================================================
head("PART C — THE GLOBAL CASE (the multi-cut corollary; v11 CITED ONLY)")
print("""
  COROLLARY (proved by induction in the note, gated on exact chains in
  A4).  If at EVERY cut of a chain the record structure in force
  satisfies (H-corr) for the composite first leg and (H-avail) for the
  composite later leg, then the whole chain is Chapman-Kolmogorov: the
  law over the record grain is a product of its legs, and D vanishes at
  every cut simultaneously.  TOTAL FACTUALITY — every alternative
  recorded, at every cut, with no erasure — is the corollary's global
  shape: the finest record structure at every cut, preserved forever.
""")
gate("C1", "the induction's base and two steps, gated (A4)",
     True, "3-step and 4-step chains, exact, both routes",
     "declarative: re-asserts A4's gates")
print("  v11's MEASURED STATUS, cited and NOT re-run (v11 is frozen):")
print("   * [V11] LOG #14 (U1 TERMINAL): at every division-event cut with a")
print("     biting test the law DIVIDES; the fifteen indivisibility")
print("     verdicts are at NON-division cuts.  Carried caveat, from that")
print("     same entry: the renewal-grain divisible verdicts there were")
print("     DEGENERATE-divisible (a column-constant transfer), so they")
print("     corroborate the corollary only weakly.")
print("   * [V11] LOG #21 (U1b TERMINAL): at the record grain no two-sided")
print("     test exists in the reachable class — 'the record-grain question")
print("     is not closed, it is UNASKED below depth 15'.  So v11")
print("     CORROBORATES the corollary where it can ask and does NOT test")
print("     it where it cannot.  No v11 number is claimed here.")
gate("C2", "v11 is cited, not re-run: no v11 file is read by this receipt",
     True, "the corollary's global shape is stated, not measured here",
     "declarative")


# ============================================================================
head("PART D — THE CONVERSE, SCOPED")
print("""
  THE IMPLICATION LADDER (the top link is this unit's theorem; the
  bottom links are gated separations):

     records (H-corr & H-avail)
        ==> medium decoherence at the cut
        ==> Delta^B = 0
        ==> D_210 = 0 with the canonical divisor
        ==> d_div = 0.

  NONE of the reverse implications holds.  Each failure is exhibited
  exactly below.  The one true converse in the literature is [GMH]'s —
  for a PURE initial state, medium decoherence <=> generalized records —
  and it is CITED as the known result it is, never claimed here.
""")

# D0: records => medium decoherence (the top link, gated)
_md_bad = 0
_md_n = 0
for i in range(4):
    for j in range(4):
        for (k, l), t in cross_terms(K16, U2_pre, U1_rec, i, j):
            _md_n += 1
            if not K16.is_zero(t):
                _md_bad += 1
gate("D0", "records ==> MEDIUM decoherence (every branch overlap vanishes)",
     _md_bad == 0,
     "%d overlaps on the A3 instance, 0 nonzero — not merely their real "
     "part, the overlaps themselves" % _md_n, "[GMH]")

# D1: d_div = 0 without D_210 = 0, and divisibility without any record
print()
print("D1. DIVISIBILITY WITHOUT A RECORD (the C+1 rotation pair, rebuilt)")


def S_rat(c):
    return [[Fr(1 + c, 2) if isinstance(c, int) else (1 + c) / 2,
             (1 - c) / 2], [(1 - c) / 2, (1 + c) / 2]]


def S_of(c):
    c = Fr(c)
    return [[(1 + c) / 2, (1 - c) / 2], [(1 - c) / 2, (1 + c) / 2]]


def R_of(K, c, s):
    c, s = Fr(c), Fr(s)
    return [[K.rat(c), K.rat(-s)], [K.rat(s), K.rat(c)]]


c1, s1 = Fr(24, 25), Fr(7, 25)
c2, s2 = Fr(4, 5), Fr(3, 5)
U1r = R_of(K16, c1, s1)
U2r = R_of(K16, c2, s2)
gate("D1", "both rotations are exact rational orthogonal matrices",
     is_unitary(K16, U1r) and is_unitary(K16, U2r),
     "(24/25, 7/25) and (4/5, 3/5)")
_B1r = to_rat_matrix(K16, mB(K16, U1r))
_B2r = to_rat_matrix(K16, mB(K16, U2r))
_B20r = to_rat_matrix(K16, mB(K16, mmul(K16, U2r, U1r)))
cos2_1 = c1 * c1 - s1 * s1
cos2_2 = c2 * c2 - s2 * s2
cos2_t = cos2_1 * cos2_2 - (2 * c1 * s1) * (2 * c2 * s2)
gate("D1", "B(R(th)) = S(cos 2th) on both factors",
     _B1r == S_of(cos2_1) and _B2r == S_of(cos2_2),
     "c1 = %s, c2 = %s" % (cos2_1, cos2_2))
gate("D1", "c_tot = -7/25 and B(U2 U1) = S(c_tot)",
     cos2_t == Fr(-7, 25) and _B20r == S_of(cos2_t), "exact")
_D1r = [[_B20r[i][j] - rat_mm(_B2r, _B1r)[i][j] for j in range(2)]
        for i in range(2)]
gate("D1", "Delta^B =/= 0: entry (0,0) = -4032/15625",
     _D1r[0][0] == Fr(-4032, 15625),
     "the actual residual D_210 with the canonical divisor is nonzero too",
     "[W1']")
Kdiv = S_of(Fr(-175, 527))
gate("D1", "K = S(-175/527) is a genuine stochastic matrix",
     stochastic_rat(Kdiv), "entries >= 0, columns sum to 1")
gate("D1", "K B(U1) = B(U2 U1) EXACTLY, and K =/= B(U2)",
     rat_mm(Kdiv, _B1r) == _B20r and Kdiv != _B2r,
     "so d_div = 0 while D_210 =/= 0 — the ladder's bottom link is strict")
_rec_win = []
for pn, part in [("finest", [0, 1]), ("trivial", [0, 0])]:
    hc, _ = h_corr(K16, U1r, part)
    ha, _ = h_avail(K16, U2r, part)
    if hc and ha:
        _rec_win.append(pn)
gate("D1", "NO record structure exists at this cut (both partitions of 2)",
     not _rec_win,
     "the finest fails (H-avail) since U2 is not monomial; the trivial "
     "fails (H-corr) since both alternatives are live")
_mdbad = [(i, j, k, l) for i in range(2) for j in range(2)
          for (k, l), t in cross_terms(K16, U2r, U1r, i, j)
          if not K16.is_zero(t)]
gate("D1", "and medium decoherence FAILS here (branch overlaps nonzero)",
     len(_mdbad) > 0,
     "%d nonzero overlaps; by [GMH] (pure state) NO generalized records "
     "exist for this history set" % len(_mdbad), "[GMH]")
print("    CONCLUSION: divisibility does NOT imply a record.  The converse")
print("    is FALSE at the divisibility level.")

# D2: Delta^B = 0 without medium decoherence
print()
print("D2. Delta^B = 0 WITHOUT MEDIUM DECOHERENCE (phase alignment)")
_align = None
_famA = [("H", H2), ("HS", mmul(K16, H2, S2)), ("HT", mmul(K16, H2, T2)),
         ("SH", mmul(K16, S2, H2)), ("TH", mmul(K16, T2, H2)),
         ("HZ", mmul(K16, H2, Z2)), ("XH", mmul(K16, X2, H2))]
for n2, V2 in _famA:
    for n1, V1 in _famA:
        if mzero(K16, delta_B(K16, V2, V1)):
            terms = [t for i in range(2) for j in range(2)
                     for _, t in cross_terms(K16, V2, V1, i, j)]
            if any(not K16.is_zero(t) for t in terms):
                _align = (n2, n1, V2, V1)
                break
    if _align:
        break
gate("D2", "a witness exists: Delta^B = 0 with NONZERO branch overlaps",
     _align is not None,
     "witness (U2, U1) = (%s, %s) from the declared family"
     % (_align[0], _align[1]) if _align else "none in the declared family",
     "[W1']")
if _align:
    n2, n1, V2, V1 = _align
    _win = []
    for pn, part in [("finest", [0, 1]), ("trivial", [0, 0])]:
        hc, _ = h_corr(K16, V1, part)
        ha, _ = h_avail(K16, V2, part)
        if hc and ha:
            _win.append(pn)
    gate("D2", "the witness carries NO record structure either", not _win,
         "Delta^B = 0 is phase alignment, not a record")
    _pert_bad = 0
    _pert_n = 0
    for k in range(1, 8):
        Dph = [[K16.zpow(k), K16.zero], [K16.zero, K16.one]]
        _pert_n += 1
        if not mzero(K16, delta_B(K16, mmul(K16, V2, Dph), V1)):
            _pert_bad += 1
    gate("D2", "and its Delta^B = 0 is UNSTABLE under declared phase kicks",
         _pert_bad > 0,
         "%d of %d diagonal phase insertions break it" % (_pert_bad, _pert_n))
_pert_rec = 0
for k in range(1, 8):
    Dph = [[K16.zpow(k), K16.zero, K16.zero, K16.zero],
           [K16.zero, K16.one, K16.zero, K16.zero],
           [K16.zero, K16.zero, K16.zpow((3 * k) % 16), K16.zero],
           [K16.zero, K16.zero, K16.zero, K16.one]]
    if not mzero(K16, delta_B(K16, mmul(K16, U2_pre, Dph),
                              mmul(K16, Dph, U1_rec))):
        _pert_rec += 1
gate("D2", "whereas the RECORD-killed defect is STABLE under the same kicks",
     _pert_rec == 0,
     "7 declared phase insertions, Delta^B stays exactly 0 — the record "
     "hypotheses are support conditions and phases cannot break them")

# D3: the all-readouts converse forces trivial branching
print()
print("D3. THE ALL-READOUTS CONVERSE: it forces the branching to be TRIVIAL")
print("    Re<phi|M|phi> = 0 for every unit phi  <=>  M + M^dag = 0, and")
print("    M + M^dag = |C><C| - sum_k |c_k><c_k| with c_k = U2 Pi_k U1 |j>,")
print("    C = sum_k c_k = U2 U1 |j>.  Since the c_k are orthogonal, the")
print("    right side vanishes iff at most one c_k is nonzero — i.e. iff")
print("    column j of U1 is MONOMIAL: no branching at all.")
_id_bad = 0
for K, U2, U1, n in [(K16, H2, H2, 2), (K16, mmul(K16, H2, S2), H2, 2),
                     (K12, F3, F3, 3), (K12, mmul(K12, F3, P3), F3, 3)]:
    for j in range(n):
        cs = []
        for k in range(n):
            cs.append([K.mul(U2[i][k], U1[k][j]) for i in range(n)])
        C = [K.zero] * n
        for c in cs:
            C = [K.add(C[i], c[i]) for i in range(n)]
        lhs = [[K.zero] * n for _ in range(n)]
        for k in range(n):
            for l in range(n):
                if k == l:
                    continue
                for p in range(n):
                    for q in range(n):
                        lhs[p][q] = K.add(lhs[p][q],
                                          K.mul(cs[k][p], K.conj(cs[l][q])))
        rhs = [[K.sub(K.mul(C[p], K.conj(C[q])),
                      sum_field(K, [K.mul(cs[k][p], K.conj(cs[k][q]))
                                    for k in range(n)]))
                for q in range(n)] for p in range(n)]
        if not meq(K, lhs, rhs):
            _id_bad += 1
gate("D3", "the operator identity M + M^dag = |C><C| - sum_k |c_k><c_k|",
     _id_bad == 0, "gated on 4 declared pairs, every initial configuration")
_wit = [(nm, mzero(K16, delta_B(K16, V, H2))) for nm, V in _famA]
gate("D3", "a non-monomial column admits a readout with Delta^B =/= 0",
     any(not z for _, z in _wit),
     "U1 = H; witnesses among the declared V family: %s"
     % [nm for nm, z in _wit if not z][:3])
_mono = [[K16.zero, K16.one], [K16.one, K16.zero]]
gate("D3", "a monomial column gives Delta^B = 0 for EVERY declared readout",
     all(mzero(K16, delta_B(K16, V, _mono)) for _, V in _famA),
     "%d readouts" % len(_famA))
print("    SCOPE: the strong converse (canonical divisibility for all")
print("    readouts) delivers records only VACUOUSLY.  The honest converse")
print("    is [GMH]'s, at the decoherence-functional level, and it is not")
print("    ours: v12 supplies the translation into Barandes division")
print("    events, nothing more.")


# ============================================================================
head("PART E — THE NEGATIVE CONTROL: THE ERASER RESTORES THE DEFECT")
print("""
  The same record, the same initial configurations, the same first leg
  U1 = CNOT . (H (x) I).  ONLY the later operation changes:

     PRESERVING:  U2  = H (x) I          (acts on the branch alone)
     ERASING:     U2' = (H (x) I) . CNOT (coherently undoes the record)

  T3' claims nothing after erasure; this control shows the clause is
  load-bearing rather than decorative.
""")
U2_er = mmul(K16, H_b, CN01)
gate("E1", "U2' is unitary and (H-corr) still holds for U1",
     is_unitary(K16, U2_er) and h_corr(K16, U1_rec, part_rec)[0],
     "the record is still MADE; only its availability changes")
ok_ae, w_ae = h_avail(K16, U2_er, part_rec)
gate("E1", "(H-avail) FAILS for the eraser", not ok_ae,
     "a later configuration receives from both record sectors: %s" % (w_ae,))
G10e = to_rat_matrix(K16, mB(K16, U1_rec))
G21e = to_rat_matrix(K16, mB(K16, U2_er))
G20e = to_rat_matrix(K16, mB(K16, mmul(K16, U2_er, U1_rec)))
gate("E1", "the erased composite law is the IDENTITY (the branch returns)",
     G20e == [[Fr(1) if i == j else Fr(0) for j in range(4)]
              for i in range(4)],
     "coherent erasure recovers the initial configuration exactly")
D210e = [[G20e[i][j] - rat_mm(G21e, G10e)[i][j] for j in range(4)]
         for i in range(4)]
gate("E1", "D_210 RETURNS, maximally: every entry is +-1/2 or 0",
     not all(x == 0 for row in D210e for x in row)
     and all(abs(x) in (Fr(0), Fr(1, 2)) for row in D210e for x in row),
     "entries %s" % [[str(x) for x in row] for row in D210e])
gate("E1", "and d_div > 0 too: columns 0 and 2 of Gam_10 are EQUAL",
     [G10e[i][0] for i in range(4)] == [G10e[i][2] for i in range(4)],
     "so K Gam_10 has equal columns 0, 2 for EVERY stochastic K, while "
     "Gam_20 = I does not: no divisor exists, by an exact argument and "
     "not by a search")
_lb = sum(abs(Fr(1) if i == 0 else Fr(0)) for i in range(4))
gate("E1", "the exact ell^1 floor: min_K ||Gam_20 - K Gam_10||_1 = 2",
     True,
     "on columns 0 and 2 alone: (1-v0)+v1+v2+v3 + v0+v1+(1-v2)+v3 = 2 for "
     "every probability vector v — computed by hand, gated as arithmetic",
     "declarative")
gate("E1", "the PRESERVING leg on the same data still has D_210 = 0",
     mzero(K16, delta_B(K16, U2_pre, U1_rec)),
     "the ONLY difference between the two runs is the later operation")


# ============================================================================
head("PART F — ANTECEDENTS, DISCLOSURES, THE KILL, THE VERDICT")

print("  ANTECEDENTS, cited at the gates that use them:")
for t in sorted(CITED):
    txt = CITED[t]
    print("    %-8s %s" % (t, txt[:66]))
    for k in range(66, len(txt), 66):
        print("             %s" % txt[k:k + 66])
print()

print("  SCOPE, engraved (v2.1 sec.5 and T3'):")
print("   * No claim about nature.  Declared finite-dimensional models only.")
print("   * The record is defined independently of the defect and declared")
print("     before any defect is computed, at every instance here.")
print("   * The theorem's hypotheses are SUPPORT conditions.  [W1'] proved")
print("     Delta^B = 0 is a PHASE-ALIGNMENT condition, strictly weaker;")
print("     records are therefore ONE way to kill the defect, not the only")
print("     way — D2 exhibits the other way and shows it is unstable.")
print("   * Delta^B, D_210 and d_div stay three different objects (T2').")
print("     Every divisibility statement here names its divisor.")
print("   * NO claim after erasure or under sector-recombining operations;")
print("     part E is that boundary, exhibited rather than assumed.")
print("   * The bc instance's biconditional is PROVEN in one direction and")
print("     MEASURED in the other over a declared 16-member family of record")
print("     structures at 12 cells.  It is not a general converse.")
print("   * v11 is cited, never re-run; [GMH] is cited, never re-derived.")
print()

_decl = [g for g in GATES if "declarative" in (g[4] or "")]
print("  DISCLOSURES:")
print("   * %d of the %d gates are DECLARATIVE (they print a stated scope or"
      % (len(_decl), len(GATES)))
print("     re-assert an already-gated fact rather than computing something")
print("     new): %s" % ([g[1][:34] for g in _decl],))
print("   * the Bell model is REBUILT here from the committed specification;")
print("     no bc code is imported and no bc working-tree file is read.")
print("   * the exact ranks are computed over Q(sqrt 2) after an exactness-")
print("     checked conversion (gate B0), not over Q(zeta_16).")
print()

fails = [g for g in GATES if not g[2]]
KILL = False
KILL_WHY = ("a stable record (H-corr and H-avail both holding) with "
            "D_210 =/= 0 on its own algebra under record-preserving dynamics")
_kill_hits = []
for n2, U2 in CAND2_4:
    for n1, U1 in CAND1_4:
        if h_corr(K16, U1, part_rec)[0] and h_avail(K16, U2, part_rec)[0]:
            if not mzero(K16, delta_B(K16, U2, U1)):
                _kill_hits.append((n2, n1))
for n2, U2 in CAND2_9:
    for n1, U1 in CAND1_9:
        if h_corr(K12, U1, part_trit)[0] and h_avail(K12, U2, part_trit)[0]:
            if not mzero(K12, delta_B(K12, U2, U1)):
                _kill_hits.append((n2, n1))
for nm, a, b in SETTINGS:
    for fr in ("F1", "F2"):
        if FR[(nm, fr)]["wins"] and not FR[(nm, fr)]["divides"]:
            _kill_hits.append((nm, fr))
KILL = len(_kill_hits) > 0

hr()
print("  THE KILL CONDITION: %s" % KILL_WHY)
print("  searched over: the dim-4 census (%d pairs), the dim-9 census (%d "
      "pairs)," % (len(CAND2_4) * len(CAND1_4), len(CAND2_9) * len(CAND1_9)))
print("  and the Bell model's 12 cells x 16 declared record structures.")
print("  AND, at n = 3, EXHAUSTIVELY over all 512 x 512 support patterns and")
print("  all 5 partitions (A5b): the hypotheses are monotone in the support,")
print("  so that check covers EVERY pair of 3x3 matrices, with any")
print("  amplitudes whatever — at n = 3 no counterexample exists at all.")
print("  RESULT: %s" % ("FIRED — %s" % _kill_hits[:3] if KILL
                        else "NOT FIRED.  No instance found."))
hr()
print()

npass = sum(1 for g in GATES if g[2])
print("  gates: %d run, %d pass, %d fail" % (len(GATES), npass, len(fails)))
print("  anchors: %d, all exit-1 (a committed constant or the arithmetic "
      "layer)" % NANCHOR[0])
if fails:
    print("  FAILING GATES:")
    for g in fails:
        print("    [%s] %s %s" % (g[0], g[1], g[3]))
print()

if KILL:
    VERDICT = "W3'-KILLED"
elif fails:
    VERDICT = "W3'-BROKEN-AT-GATE"
else:
    VERDICT = "W3'-PROVEN"

hr()
print("  VERDICT: %s" % VERDICT)
hr()
print()
print("  THE THEOREM: at finite dimension, a record of the alternatives at a")
print("  cut — mutually exclusive sectors (H-orth), perfectly correlated")
print("  with the alternatives (H-corr), available under the declared future")
print("  dynamics (H-avail) — forces D_210 = 0 on the cut algebra with the")
print("  CANONICAL divisor.  The proof is a support argument on the")
print("  interference cross-terms and is gated TERMWISE, not merely in its")
print("  conclusion.  A second sufficient route: if the record is physically")
print("  READ at the cut, the same conclusion holds for ANY later dynamics.")
print("  Approximate records give approximate divisibility, with an exact")
print("  and TIGHT total-variation bound (A8).  The two known monomial")
print("  sufficiency conditions are this theorem at its two EXTREME record")
print("  structures (A5c), and the intermediate structures are strictly")
print("  stronger than both.")
print()
print("  THE INSTANCE: on the committed Bell model the theorem's prediction")
print("  matches the committed divisibility census at all 12 cells, and the")
print("  reading of the record repairs every illegitimate division event —")
print("  so bc #4's M-1 biconditional reads: a legitimate division event is")
print("  a RECORD event.")
print()
print("  THE CONVERSE: FALSE at the divisibility level (D1) and at the")
print("  Delta^B level (D2); vacuous in its all-readouts form (D3).  The")
print("  true converse is [GMH]'s, cited.")
print()
print("  THE ERASER: the same record, the same first leg, one changed later")
print("  operation — and D_210 returns at +-1/2 with no divisor at all.")
print("  (H-avail) is load-bearing.")
print()
print("  determinism: fixed lexicographic enumeration everywhere; no")
print("  randomness, no hashing, no float in any substantive path.")
print("  runtime: %s" % el())
hr()
sys.exit(0)
