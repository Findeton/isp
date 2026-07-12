#!/usr/bin/env python3
"""D12 exact one-diamond precursor retained after hostile scope downgrade.

This is an implementation of the maximal universal form, not a claim that one
interaction angle has been derived.  All amplitudes and probabilities lie in
Q(sqrt(2), i); no floating point is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import product


CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:02d}: {label}")


@dataclass(frozen=True)
class Q2:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def make(x):
        return x if isinstance(x, Q2) else Q2(F(x), F(0))

    def __add__(self, other):
        other = Q2.make(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Q2.make(other))

    def __rsub__(self, other):
        return Q2.make(other) - self

    def __mul__(self, other):
        other = Q2.make(other)
        return Q2(self.a * other.a + 2 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Q2.make(other)
        den = other.a * other.a - 2 * other.b * other.b
        if den == 0:
            raise ZeroDivisionError
        return Q2((self.a * other.a - 2 * self.b * other.b) / den,
                  (self.b * other.a - self.a * other.b) / den)


@dataclass(frozen=True)
class C2:
    re: Q2 = Q2()
    im: Q2 = Q2()

    @staticmethod
    def make(x):
        if isinstance(x, C2):
            return x
        if isinstance(x, Q2):
            return C2(x, Q2())
        return C2(Q2.make(x), Q2())

    def __add__(self, other):
        other = C2.make(other)
        return C2(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C2(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-C2.make(other))

    def __rsub__(self, other):
        return C2.make(other) - self

    def __mul__(self, other):
        other = C2.make(other)
        return C2(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = C2.make(other)
        den = other.re * other.re + other.im * other.im
        if den == Q2():
            raise ZeroDivisionError
        return C2((self.re * other.re + self.im * other.im) / den,
                  (self.im * other.re - self.re * other.im) / den)

    def conj(self):
        return C2(self.re, -self.im)


ZERO, ONE = C2(), C2.make(1)
II = C2(Q2(), Q2.make(1))
ROOT_HALF = Q2(F(0), F(1, 2))


def matrix(rows):
    return tuple(tuple(C2.make(x) for x in row) for row in rows)


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def dagger(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a)))
                 for i in range(len(a[0])))


def mul(a, b):
    bt = tuple(zip(*b))
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), ZERO)
                       for col in bt) for row in a)


def mv(a, v):
    return tuple(sum((x * y for x, y in zip(row, v)), ZERO) for row in a)


def inner(v, w):
    return sum((x.conj() * y for x, y in zip(v, w)), ZERO)


def kron(a, b):
    return tuple(tuple(x * y for x in ar for y in br)
                 for ar in a for br in b)


def projector(n, index):
    return matrix([[int(i == index and j == index) for j in range(n)]
                   for i in range(n)])


def iswap(cosine, sine):
    c, s = C2.make(cosine), II * sine
    return matrix(((1, 0, 0, 0),
                   (0, c, s, 0),
                   (0, s, c, 0),
                   (0, 0, 0, 1)))


I2, I4 = eye(2), eye(4)
P0, P1 = projector(2, 0), projector(2, 1)
FIRST = (kron(P0, I2), kron(P1, I2))
SECOND = (kron(I2, P0), kron(I2, P1))
HADAMARD = matrix(((ROOT_HALF, ROOT_HALF),
                   (ROOT_HALF, -ROOT_HALF)))
FRAME = kron(HADAMARD, HADAMARD)


@dataclass(frozen=True)
class SealedDiamond:
    name: str
    interaction: tuple
    incoming: tuple = ("q", "q")
    outgoing: tuple = ("q", "q")
    owners: tuple = ("left", "right")
    terminal: bool = False

    def class_operator(self, first_record, second_record):
        # Physical order: interaction, durable second-leg record, then a later
        # durable first-leg record.  Matrix multiplication reads right-to-left.
        return mul(FIRST[first_record],
                   mul(SECOND[second_record], self.interaction))


QUARTER = SealedDiamond("theta=pi/4", iswap(ROOT_HALF, ROOT_HALF))
HALF = SealedDiamond("theta=pi/2", iswap(0, 1))
PSI = (ZERO, ONE, ZERO, ZERO)  # |01>
HISTORIES = tuple(product((0, 1), repeat=2))


def branch_vector(diamond, history, psi=PSI, first=FIRST, second=SECOND):
    f, s = history
    k = mul(first[f], mul(second[s], diamond.interaction))
    return mv(k, psi)


def decoherence(diamond, left, right):
    return inner(branch_vector(diamond, left), branch_vector(diamond, right))


def law(diamond):
    return {history: decoherence(diamond, history, history)
            for history in HISTORIES}


for diamond in (QUARTER, HALF):
    check(mul(dagger(diamond.interaction), diamond.interaction) == I4,
          f"{diamond.name} local process is unitary")
    check(diamond.incoming == diamond.outgoing and not diamond.terminal,
          f"{diamond.name} commit is typed seal-and-birth, not death")
    diagonal = law(diamond)
    check(sum(diagonal.values(), ZERO) == ONE,
          f"{diamond.name} exhaustive whole-history masses normalize")
    check(all(decoherence(diamond, a, b) == ZERO
              for a in HISTORIES for b in HISTORIES if a != b),
          f"{diamond.name} durable pointer histories decohere exactly")

law_q, law_h = law(QUARTER), law(HALF)
check(law_q[(0, 1)] == C2.make(F(1, 2)) and
      law_q[(1, 0)] == C2.make(F(1, 2)),
      "quarter-iSWAP has two exact continuing record histories")
check(law_h[(1, 0)] == ONE and
      sum((p for h, p in law_h.items() if h != (1, 0)), ZERO) == ZERO,
      "half-iSWAP has one exact continuing record history")

# Deleting the later first-leg observation is physical coarse graining, not a
# change to the internal future law.
for diamond in (QUARTER, HALF):
    fine = law(diamond)
    evolved = mv(diamond.interaction, PSI)
    for second_record in (0, 1):
        coarse = sum((fine[(first_record, second_record)]
                      for first_record in (0, 1)), ZERO)
        direct_vec = mv(SECOND[second_record], evolved)
        direct = inner(direct_vec, direct_vec)
        check(coarse == direct,
              f"{diamond.name} later-record deletion pushes forward exactly for seal {second_record}")

# The next-click law is a disintegration of the whole-history measure.
coarse_q = {
    s: sum((law_q[(f, s)] for f in (0, 1)), ZERO) for s in (0, 1)
}
check(law_q[(0, 1)] / coarse_q[1] == ONE and
      law_q[(1, 0)] / coarse_q[0] == ONE,
      "conditional next records are recovered by exact disintegration")
support_q = tuple(h for h, p in law_q.items() if p != ZERO)
check(support_q == ((0, 1), (1, 0)),
      "licensed extension support is the nonzero support of the supplied process")

# Integrated frame covariance: transform state, interaction, and every pointer
# effect together, then reconstruct the entire diagonal history law.
check(mul(dagger(FRAME), FRAME) == I4, "Hadamard two-leg frame is exact unitary")
for diamond in (QUARTER, HALF):
    transformed = SealedDiamond(
        diamond.name + " framed",
        mul(FRAME, mul(diamond.interaction, dagger(FRAME))),
    )
    psi_g = mv(FRAME, PSI)
    first_g = tuple(mul(FRAME, mul(p, dagger(FRAME))) for p in FIRST)
    second_g = tuple(mul(FRAME, mul(p, dagger(FRAME))) for p in SECOND)
    framed_law = {}
    for history in HISTORIES:
        v = branch_vector(transformed, history, psi_g, first_g, second_g)
        framed_law[history] = inner(v, v)
    check(framed_law == law(diamond),
          f"{diamond.name} complete whole-history law is frame invariant")

# Disjoint physical diamonds have no relative commit order.  Their auxiliary
# linearizations agree exactly; overlapping operations are not quotiented.
for diamond in (QUARTER, HALF):
    on_left = kron(diamond.interaction, I4)
    on_right = kron(I4, diamond.interaction)
    check(mul(on_left, on_right) == mul(on_right, on_left),
          f"{diamond.name} disjoint construction orders are one gauge fiber")

# A primitive non-Markov whole-history law fits the same disintegration API;
# it need not factor through the latest record.
OMEGA = tuple(product((-1, 1), repeat=3))


def nonmarkov_law(r):
    return {h: (F(1) + F(r) * h[0] * h[1] * h[2]) / 8 for h in OMEGA}


nm = nonmarkov_law(F(1, 2))
cond_plus = nm[(1, 1, 1)] / (nm[(1, 1, -1)] + nm[(1, 1, 1)])
cond_minus = nm[(-1, 1, 1)] / (nm[(-1, 1, -1)] + nm[(-1, 1, 1)])
check(cond_plus == F(3, 4) and cond_minus == F(1, 4),
      "whole-history disintegration retains non-Markov dependence on the sealed past")

# Continuation is structural: every positive internal history emits the same
# two typed output collars.  No global population race is involved.
for diamond in (QUARTER, HALF):
    live = len(diamond.outgoing)
    for _ in range(256):
        live -= len(diamond.incoming)
        live += len(diamond.outgoing)
    check(live == 2, f"{diamond.name} equal-arity metadata stays two for 256 bookkeeping steps")

check(law_q != law_h,
      "the one-cell witness works but does not select its primitive interaction")

EXPECTED_CHECKS = 25
if CHECKS != EXPECTED_CHECKS:
    raise AssertionError(f"expected {EXPECTED_CHECKS} checks, observed {CHECKS}")

summary = (
    "D12 ONE-DIAMOND PRECURSOR EXACT RECEIPT\n"
    f"checks={CHECKS}\n"
    "arithmetic=Q(sqrt(2),i)\n"
    "typed_seal_and_birth=DECLARED_METADATA_ONLY\n"
    "pointer_decoherence=PASS_ONE_DIAMOND\n"
    "pointer_coarse_graining=PASS_ONE_DIAMOND\n"
    "conditional_ratio=PASS_FINITE_WITNESS\n"
    "basis_covariance=PASS_ONE_GLOBAL_CIRCUIT_FRAME\n"
    "construction=PASS_DISJOINT_OPERATOR_COMMUTATION_ONLY\n"
    "nonmarkov=SEPARATE_CLASSICAL_WITNESS\n"
    "continuation=EQUAL_ARITY_METADATA_ONLY\n"
    "primitive_interaction_selection=OPEN\n"
    "verdict=ONE_CELL_PRECURSOR_REPLACED_BY_MULTIDIAMOND_EXECUTABLE\n"
)
print(summary, end="")
receipt = sha256(summary.encode()).hexdigest()
EXPECTED_RECEIPT = "bf05e72d6f806f674c6d2a9b7621f3e78bb37c905987b83f62f3a3180209f172"
if receipt != EXPECTED_RECEIPT:
    raise AssertionError(f"receipt drift: {receipt}")
print("receipt_sha256=" + receipt)
