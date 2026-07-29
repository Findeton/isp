#!/usr/bin/env python3
"""
exact.py -- the shared exact-arithmetic layer for the reproduction bundle of

    "Interference as the Composition Defect of Stochastic Shadows:
     Records, Gauge, and the Loop Signature of Indivisible Stochastic
     Processes"

Every number the paper prints is produced with the arithmetic in this file.
There is no float in any substantive path and no tolerance anywhere.

Contents
  * Q                 -- fractions.Fraction, re-exported.
  * Cyc               -- the cyclotomic field Q(zeta_n) = Q[x]/Phi_n(x), with
                         a canonical representation modulo Phi_n, so tuple
                         equality IS field equality.
  * Q2                -- the real quadratic field Q(sqrt 2) with an exact
                         sign oracle (no order comparison is ever made by
                         floating-point means).
  * matrix helpers    -- multiplication, adjoint, unitarity test, the Born
                         projection B(U) = |U|^{o2}, over any of the above.
  * MP                -- a multivariate polynomial ring over Q, for the
                         identities the paper proves symbolically.
  * integer lattices  -- Hermite normal form, rank, and the surjectivity
                         test used for the cycle-lattice statements.
  * graph helpers     -- cycle rank, spanning forest, fundamental cycles.
  * receipts          -- the anchor harness: exit 1 iff a computed number
                         disagrees with the number printed in the paper.
"""

from __future__ import annotations

import sys
import time
from fractions import Fraction as Q

__all__ = [
    "Q", "Cyc", "Q2", "MP", "T0", "el", "hr", "head",
    "mat_mul", "mat_adj", "mat_eq", "born", "bornq", "to_q2", "to_q3",
    "is_unitary", "mat_id",
    "hnf_rows", "lattice_rank", "lattice_is_full", "smith_rank",
    "cycle_rank", "spanning_forest", "Receipts",
]

T0 = time.time()


def el():
    return "%7.1fs" % (time.time() - T0)


def hr(c="-"):
    print(c * 74)


def head(title):
    hr("=")
    print(title)
    hr("=")


# ---------------------------------------------------------------------------
# univariate polynomials over Q (support for the cyclotomic fields)
# ---------------------------------------------------------------------------
def _ptrim(c):
    c = list(c)
    while c and c[-1] == 0:
        c.pop()
    return c


def _pmul(a, b):
    a = _ptrim(a); b = _ptrim(b)
    if not a or not b:
        return []
    r = [Q(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    r[i + j] += ai * bj
    return _ptrim(r)


def _psub(a, b):
    n = max(len(a), len(b))
    return _ptrim([(a[i] if i < len(a) else Q(0)) - (b[i] if i < len(b) else Q(0))
                   for i in range(n)])


def _pscal(a, q):
    return _ptrim([x * q for x in a])


def _pdivmod(a, b):
    a = _ptrim(a); b = _ptrim(b)
    if not b:
        raise ZeroDivisionError
    q = [Q(0)] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        d = len(a) - len(b)
        c = a[-1] / b[-1]
        q[d] = c
        for i, bi in enumerate(b):
            a[i + d] -= c * bi
        a = _ptrim(a)
    return _ptrim(q), a


_CYCLO = {}


def cyclotomic(n):
    """Phi_n(x) over Q, by exact division of x^n - 1 by the lower Phi_d."""
    if n in _CYCLO:
        return _CYCLO[n]
    num = [Q(0)] * n + [Q(1)]
    num[0] = Q(-1)
    den = [Q(1)]
    for d in range(1, n):
        if n % d == 0:
            den = _pmul(den, cyclotomic(d))
    q, r = _pdivmod(num, den)
    if r:
        raise ArithmeticError("cyclotomic division not exact at n=%d" % n)
    _CYCLO[n] = q
    return q


def _pgcdext(a, b):
    r0, r1 = _ptrim(a), _ptrim(b)
    s0, s1 = [Q(1)], []
    while r1:
        qq, r = _pdivmod(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, _psub(s0, _pmul(qq, s1))
    if r0:
        lead = r0[-1]
        r0 = _pscal(r0, 1 / lead)
        s0 = _pscal(s0, 1 / lead)
    return r0, s0


# ---------------------------------------------------------------------------
# the cyclotomic field Q(zeta_n)
# ---------------------------------------------------------------------------
class Cyc:
    """Q(zeta_n) = Q[x]/Phi_n(x).  Elements are tuples of Fraction of length
    phi(n) in the basis 1, z, ..., z^{phi(n)-1}.  Phi_n is irreducible over Q,
    so the representation is canonical and tuple equality IS field equality."""

    def __init__(self, n):
        self.n = n
        self.phi = cyclotomic(n)
        self.deg = len(self.phi) - 1
        self.zero = tuple([Q(0)] * self.deg)
        self.one = self.red([Q(1)])

    def red(self, c):
        d = self.deg
        c = list(c)
        if len(c) < d:
            c += [Q(0)] * (d - len(c))
        phi = self.phi
        for i in range(len(c) - 1, d - 1, -1):
            ci = c[i]
            if ci:
                c[i] = Q(0)
                base = i - d
                for j in range(d):
                    if phi[j]:
                        c[base + j] -= ci * phi[j]
        return tuple(c[:d])

    def zpow(self, k):
        k %= self.n
        return self.red([Q(0)] * k + [Q(1)])

    def rat(self, q):
        return self.red([Q(q)])

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def scal(self, a, q):
        q = Q(q)
        return tuple(x * q for x in a)

    def mul(self, a, b):
        d = self.deg
        r = [Q(0)] * (2 * d - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj:
                        r[i + j] += ai * bj
        return self.red(r)

    def conj(self, a):
        """complex conjugation zeta -> zeta^{-1}."""
        n = self.n
        acc = [Q(0)] * n
        for k, ak in enumerate(a):
            if ak:
                acc[(n - k) % n] += ak
        return self.red(acc)

    def inv(self, a):
        if all(x == 0 for x in a):
            raise ZeroDivisionError
        g, u = _pgcdext(list(a), self.phi)
        if g != [Q(1)]:
            raise ArithmeticError("non-unit in a field")
        return self.red(u)

    def re(self, a):
        return self.scal(self.add(a, self.conj(a)), Q(1, 2))

    def normsq(self, a):
        """|a|^2 = a * conj(a); rational for every a in a cyclotomic field
        whose value is returned as a field element."""
        return self.mul(a, self.conj(a))

    def absq(self, a):
        """|a|^2 as a Fraction (raises if the result is not rational)."""
        t = self.normsq(a)
        if any(x != 0 for x in t[1:]):
            raise ArithmeticError("modulus square is not rational")
        return t[0]

    def is_zero(self, a):
        return all(x == 0 for x in a)

    def to_rat(self, a):
        if any(x != 0 for x in a[1:]):
            return None
        return a[0]

    def sqrt_of(self, m):
        """the element zeta^k + zeta^{-k} = 2 cos(2 pi k/n) equal to sqrt(m),
        found by search and certified by squaring."""
        for k in range(1, self.n):
            c = self.add(self.zpow(k), self.zpow(-k))
            if self.mul(c, c) == self.rat(m):
                return c
        raise ArithmeticError("no sqrt(%d) of that form in Q(zeta_%d)" % (m, self.n))


# ---------------------------------------------------------------------------
# a general algebraic number field Q[x]/(f), f monic irreducible over Q
# ---------------------------------------------------------------------------
class NF:
    """Q[x]/(f) for a monic irreducible f.  Used for the totally real quartic
    field Q(cos pi/8) = Q[x]/(x^4 - x^2 + 1/8), which carries every entry of
    the composite two-measurement model.  The field is real, so complex
    conjugation is the identity and |a|^2 = a^2."""

    def __init__(self, f, name="x"):
        self.f = _ptrim([Q(c) for c in f])
        self.deg = len(self.f) - 1
        self.name = name
        self.zero = tuple([Q(0)] * self.deg)
        self.one = self.red([Q(1)])
        self.real = True

    def red(self, c):
        d = self.deg
        c = list(c)
        if len(c) < d:
            c += [Q(0)] * (d - len(c))
        f = self.f
        for i in range(len(c) - 1, d - 1, -1):
            ci = c[i]
            if ci:
                c[i] = Q(0)
                base = i - d
                for j in range(d):
                    if f[j]:
                        c[base + j] -= ci * f[j]
        return tuple(c[:d])

    def xpow(self, k):
        return self.red([Q(0)] * k + [Q(1)])

    def rat(self, q):
        return self.red([Q(q)])

    def poly(self, coeffs):
        return self.red([Q(c) for c in coeffs])

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def scal(self, a, q):
        q = Q(q)
        return tuple(x * q for x in a)

    def mul(self, a, b):
        d = self.deg
        r = [Q(0)] * (2 * d - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj:
                        r[i + j] += ai * bj
        return self.red(r)

    def conj(self, a):
        return a

    def re(self, a):
        return a

    def normsq(self, a):
        return self.mul(a, a)

    def inv(self, a):
        if all(x == 0 for x in a):
            raise ZeroDivisionError
        g, u = _pgcdext(list(a), self.f)
        if g != [Q(1)]:
            raise ArithmeticError("non-unit in a field")
        return self.red(u)

    def is_zero(self, a):
        return all(x == 0 for x in a)

    def to_rat(self, a):
        if any(x != 0 for x in a[1:]):
            return None
        return a[0]


def cos_pi8_field():
    """Q(cos pi/8) = Q[x]/(x^4 - x^2 + 1/8), with x = cos(pi/8)."""
    return NF([Q(1, 8), 0, Q(-1), 0, Q(1)], "cos(pi/8)")


def q8_to_q2(K, a):
    """An element of Q(cos pi/8) that lies in Q(sqrt 2), as a Q2.
    x^2 = (2 + sqrt 2)/4, so c0 + c2 x^2 = (c0 + c2/2) + (c2/4) sqrt 2."""
    c0, c1, c2, c3 = a
    if c1 != 0 or c3 != 0:
        raise ArithmeticError("element is not in Q(sqrt 2): %s" % (a,))
    return Q2(c0 + c2 / 2, c2 / 4)


__all__ += ["NF", "cos_pi8_field", "q8_to_q2"]


# ---------------------------------------------------------------------------
# Q(sqrt 2) with an exact sign oracle
# ---------------------------------------------------------------------------
class Q2:
    """a + b sqrt 2, a, b in Q.  Comparison is decided by exact integer
    reasoning (squaring with a sign case split), never numerically."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Q(a)
        self.b = Q(b)

    def __add__(self, o):
        o = _q2(o)
        return Q2(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        o = _q2(o)
        return Q2(self.a - o.a, self.b - o.b)

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __mul__(self, o):
        o = _q2(o)
        return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__
    __radd__ = __add__

    def __eq__(self, o):
        o = _q2(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def __repr__(self):
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return "%s*sqrt2" % self.b
        return "%s%s%s*sqrt2" % (self.a, "+" if self.b > 0 else "-", abs(self.b))

    def sign(self):
        """exact sign of a + b sqrt 2."""
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        # opposite signs: compare a^2 with 2 b^2
        lhs = a * a
        rhs = 2 * b * b
        if lhs == rhs:
            return 0
        bigger_a = lhs > rhs
        return (1 if bigger_a else -1) * (1 if a > 0 else -1)

    def __lt__(self, o):
        return (self - _q2(o)).sign() < 0

    def __le__(self, o):
        return (self - _q2(o)).sign() <= 0

    def __gt__(self, o):
        return (self - _q2(o)).sign() > 0

    def __ge__(self, o):
        return (self - _q2(o)).sign() >= 0


def _q2(x):
    if isinstance(x, Q2):
        return x
    return Q2(Q(x), 0)


Q2.SQRT2 = Q2(0, 1)


# ---------------------------------------------------------------------------
# matrices over a Cyc field
# ---------------------------------------------------------------------------
def mat_mul(K, A, B):
    n = len(A); m = len(B[0]); p = len(B)
    out = [[K.zero] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Oi = out[i]
        for k in range(p):
            a = Ai[k]
            if K.is_zero(a):
                continue
            Bk = B[k]
            for j in range(m):
                b = Bk[j]
                if not K.is_zero(b):
                    Oi[j] = K.add(Oi[j], K.mul(a, b))
    return out


def mat_adj(K, A):
    n = len(A); m = len(A[0])
    return [[K.conj(A[i][j]) for i in range(n)] for j in range(m)]


def mat_id(K, n):
    return [[K.one if i == j else K.zero for j in range(n)] for i in range(n)]


def mat_eq(A, B):
    return A == B


def is_unitary(K, A):
    n = len(A)
    P = mat_mul(K, mat_adj(K, A), A)
    return P == mat_id(K, n)


def born(K, A):
    """B(U) = |U|^{o2}, entrywise modulus square, as FIELD elements.

    The modulus square of a single entry of the reference families is
    rational, but the modulus square of an entry of a PRODUCT need not be
    (e.g. |1 + zeta_8|^2 = 2 + sqrt 2), so the Born projection is carried in
    the field and never coerced."""
    return [[K.normsq(x) for x in row] for row in A]


def bornq(K, A):
    """B(U) with an assertion that every entry is rational."""
    return [[K.absq(x) for x in row] for row in A]


def to_q2(K8, x):
    """A real element of Q(zeta_8) written exactly as a + b sqrt 2.
    Basis 1, z, z^2, z^3 with z^4 = -1; conjugation sends z -> -z^3, so
    reality forces the z^2 coefficient to vanish and a3 = -a1, and then
    x = a0 + a1 (z + z^{-1}) = a0 + a1 sqrt 2."""
    a0, a1, a2, a3 = x
    if a2 != 0 or a3 != -a1:
        raise ArithmeticError("element of Q(zeta_8) is not real: %s" % (x,))
    return Q2(a0, a1)


def to_q3(K12, x):
    """A real element of Q(zeta_12) written exactly as (a, b) meaning
    a + b sqrt 3.  Basis 1, z, z^2, z^3 with z^4 = z^2 - 1; conjugation is
    z -> z - z^3, z^2 -> 1 - z^2, z^3 -> -z^3, so reality forces a2 = 0 and
    a1 = -2 a3, and then x = a0 - a3 sqrt 3 since sqrt 3 = 2z - z^3."""
    a0, a1, a2, a3 = x
    if a2 != 0 or a1 != -2 * a3:
        raise ArithmeticError("element of Q(zeta_12) is not real: %s" % (x,))
    return (a0, -a3)


def rmat_mul(A, B):
    """multiplication of rational (Fraction) matrices."""
    n = len(A); p = len(B); m = len(B[0])
    out = [[Q(0)] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]; Oi = out[i]
        for k in range(p):
            a = Ai[k]
            if a:
                Bk = B[k]
                for j in range(m):
                    if Bk[j]:
                        Oi[j] += a * Bk[j]
    return out


__all__.append("rmat_mul")


# ---------------------------------------------------------------------------
# a small multivariate polynomial ring over Q (for symbolic identities)
# ---------------------------------------------------------------------------
class MP:
    """Sparse multivariate polynomials over Q: dict from exponent tuples
    (keyed by variable name) to Fraction coefficients.  Equality is exact."""

    __slots__ = ("d",)

    def __init__(self, d=None):
        self.d = dict(d) if d else {}
        self._trim()

    def _trim(self):
        for k in [k for k, v in self.d.items() if v == 0]:
            del self.d[k]

    @staticmethod
    def var(name):
        return MP({((name, 1),): Q(1)})

    @staticmethod
    def const(c):
        c = Q(c)
        return MP({(): c}) if c else MP()

    def __add__(self, o):
        o = o if isinstance(o, MP) else MP.const(o)
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = d.get(k, Q(0)) + v
        return MP(d)

    __radd__ = __add__

    def __neg__(self):
        return MP({k: -v for k, v in self.d.items()})

    def __sub__(self, o):
        o = o if isinstance(o, MP) else MP.const(o)
        return self + (-o)

    def __rsub__(self, o):
        return (MP.const(o) if not isinstance(o, MP) else o) + (-self)

    def __mul__(self, o):
        o = o if isinstance(o, MP) else MP.const(o)
        d = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                m = {}
                for nm, e in k1:
                    m[nm] = m.get(nm, 0) + e
                for nm, e in k2:
                    m[nm] = m.get(nm, 0) + e
                key = tuple(sorted(m.items()))
                d[key] = d.get(key, Q(0)) + v1 * v2
        return MP(d)

    __rmul__ = __mul__

    def __eq__(self, o):
        o = o if isinstance(o, MP) else MP.const(o)
        return self.d == o.d

    def is_zero(self):
        return not self.d


# ---------------------------------------------------------------------------
# integer lattices
# ---------------------------------------------------------------------------
def hnf_rows(rows, ncols):
    """Row-style Hermite normal form of the integer matrix `rows`.
    Returns the list of nonzero rows of an echelon basis of the row lattice."""
    M = [list(r) for r in rows if any(r)]
    res = []
    col = 0
    r0 = 0
    while col < ncols and r0 < len(M):
        # find pivot: smallest nonzero absolute value in this column
        piv = None
        for i in range(r0, len(M)):
            if M[i][col]:
                if piv is None or abs(M[i][col]) < abs(M[piv][col]):
                    piv = i
        if piv is None:
            col += 1
            continue
        M[r0], M[piv] = M[piv], M[r0]
        again = True
        while again:
            again = False
            p = M[r0][col]
            for i in range(r0 + 1, len(M)):
                if M[i][col]:
                    q = M[i][col] // p
                    if q:
                        M[i] = [a - q * b for a, b in zip(M[i], M[r0])]
                    if M[i][col]:
                        M[r0], M[i] = M[i], M[r0]
                        again = True
                        break
        if M[r0][col] < 0:
            M[r0] = [-a for a in M[r0]]
        r0 += 1
        col += 1
    return [r for r in M[:r0] if any(r)]


def lattice_rank(rows, ncols):
    return len(hnf_rows(rows, ncols))


def lattice_is_full(rows, ncols):
    """True iff the integer row lattice of `rows` is all of Z^ncols."""
    H = hnf_rows(rows, ncols)
    if len(H) != ncols:
        return False
    for i in range(ncols):
        if H[i][i] != 1:
            return False
    return True


def smith_rank(rows, ncols):
    """rational rank of an integer matrix, by exact Gaussian elimination."""
    M = [[Q(x) for x in r] for r in rows]
    rank = 0
    col = 0
    nrow = len(M)
    while col < ncols and rank < nrow:
        piv = None
        for i in range(rank, nrow):
            if M[i][col]:
                piv = i
                break
        if piv is None:
            col += 1
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][col]
        M[rank] = [x / pv for x in M[rank]]
        for i in range(nrow):
            if i != rank and M[i][col]:
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[rank])]
        rank += 1
        col += 1
    return rank


# ---------------------------------------------------------------------------
# graphs
# ---------------------------------------------------------------------------
def spanning_forest(nv, edges):
    """edges: list of (u,v).  Returns (tree_edge_index_set, ncomponents,
    parent_map) using union-find."""
    par = list(range(nv))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    tree = set()
    for idx, (u, v) in enumerate(edges):
        ru, rv = find(u), find(v)
        if ru != rv:
            par[ru] = rv
            tree.add(idx)
    comps = len({find(x) for x in range(nv)})
    return tree, comps


def cycle_rank(nv, edges):
    tree, comps = spanning_forest(nv, edges)
    return len(edges) - nv + comps


# ---------------------------------------------------------------------------
# the receipts / anchor harness
# ---------------------------------------------------------------------------
class Receipts:
    """Collects (label, computed, expected) triples.  `expected` is the value
    PRINTED IN THE PAPER; a mismatch is the only way this bundle exits 1."""

    def __init__(self, section):
        self.section = section
        self.rows = []

    def anchor(self, label, computed, expected):
        ok = (computed == expected)
        self.rows.append((label, computed, expected, ok))
        return ok

    def report(self, quiet=False):
        npass = sum(1 for r in self.rows if r[3])
        nfail = len(self.rows) - npass
        if not quiet:
            hr("=")
            print("RECEIPTS -- %s" % self.section)
            hr("=")
            w = max((len(r[0]) for r in self.rows), default=10)
            for label, comp, exp, ok in self.rows:
                mark = "ok  " if ok else "FAIL"
                if ok:
                    print("  %s  %-*s  %s" % (mark, w, label, _fmt(comp)))
                else:
                    print("  %s  %-*s  computed %s  !=  paper %s"
                          % (mark, w, label, _fmt(comp), _fmt(exp)))
            hr("-")
            print("  %s : %d anchors, %d pass, %d fail   [%s]"
                  % (self.section, len(self.rows), npass, nfail, el()))
        return npass, nfail

    def finish(self):
        npass, nfail = self.report()
        sys.exit(1 if nfail else 0)


def _fmt(x):
    s = repr(x)
    return s if len(s) <= 110 else s[:107] + "..."
