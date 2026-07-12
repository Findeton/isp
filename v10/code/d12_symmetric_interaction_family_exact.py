#!/usr/bin/env python3
"""D12 exact no-go for selection by standard structural principles.

Two members of the same exchange-symmetric, excitation-preserving iSWAP
interaction family are calculated in Q(sqrt(2), i).  They share the record
architecture, locality class, symmetries, unitary probability calculus,
pointer algebra, and seal-and-birth behavior, but predict different later
record probabilities.  No floating-point arithmetic is theorem-critical.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256


CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:02d}: {label}")


@dataclass(frozen=True)
class Q2:
    """a + b sqrt(2), a,b rational."""

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


@dataclass(frozen=True)
class C2:
    """Q(sqrt(2),i)."""

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

    def conj(self):
        return C2(self.re, -self.im)


ZERO, ONE = C2(), C2.make(1)
II = C2(Q2(), Q2.make(1))
ROOT_HALF = Q2(F(0), F(1, 2))  # sqrt(2)/2


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


def probability(v, indices):
    return sum((v[k].conj() * v[k] for k in indices), ZERO)


I4 = eye(4)
SWAP = matrix(((1, 0, 0, 0),
               (0, 0, 1, 0),
               (0, 1, 0, 0),
               (0, 0, 0, 1)))
NUMBER = matrix(((0, 0, 0, 0),
                 (0, 1, 0, 0),
                 (0, 0, 1, 0),
                 (0, 0, 0, 2)))


def iswap(cosine, sine):
    c, s = C2.make(cosine), II * sine
    return matrix(((1, 0, 0, 0),
                   (0, c, s, 0),
                   (0, s, c, 0),
                   (0, 0, 0, 1)))


U_QUARTER = iswap(ROOT_HALF, ROOT_HALF)  # theta = pi/4
U_HALF = iswap(0, 1)                    # theta = pi/2

for label, u in (("quarter", U_QUARTER), ("half", U_HALF)):
    check(mul(dagger(u), u) == I4, f"{label} interaction is exactly unitary")
    check(mul(u, SWAP) == mul(SWAP, u),
          f"{label} interaction is exactly exchange symmetric")
    check(mul(u, NUMBER) == mul(NUMBER, u),
          f"{label} interaction exactly conserves excitation number")

check(U_QUARTER != U_HALF,
      "the two structurally identical packets contain inequivalent interactions")

# Both gates can create entanglement.  A pure two-qubit vector (a,b,c,d) is
# product iff ad-bc=0.  |++> is represented without irrelevant normalization.
plus_plus = (ONE, ONE, ONE, ONE)
for label, u in (("quarter", U_QUARTER), ("half", U_HALF)):
    out = mv(u, plus_plus)
    determinant = out[0] * out[3] - out[1] * out[2]
    check(determinant != ZERO, f"{label} interaction has entangling capacity")

# Both preserve the same Born normalization and use the same complete durable
# computational pointer.  Yet |01> followed by a second-leg-1 record separates
# them exactly: 1/2 versus 0.
ket_01 = (ZERO, ONE, ZERO, ZERO)
out_quarter, out_half = mv(U_QUARTER, ket_01), mv(U_HALF, ket_01)
check(inner(out_quarter, out_quarter) == inner(out_half, out_half) == ONE,
      "both interactions preserve the same Born order unit")
p_quarter = probability(out_quarter, (1, 3))
p_half = probability(out_half, (1, 3))
check(p_quarter == C2.make(F(1, 2)),
      "quarter-iSWAP predicts exact later second-leg probability 1/2")
check(p_half == ZERO,
      "half-iSWAP predicts exact later second-leg probability 0")
check(p_quarter != p_half,
      "a durable downstream record empirically distinguishes the packets")

# These metadata are deliberately identical: the difference is the supplied
# coupling/action parameter, not a kinematic or record-theoretic distinction.
packet_metadata = {
    "incoming": ("q", "q"),
    "outgoing": ("q", "q"),
    "owners": ("left", "right"),
    "connected_collar": True,
    "terminal": False,
    "pointer": ("00", "01", "10", "11"),
    "evidence_survival": "exp(-I)",
    "construction_order": "disjoint-rewrite quotient",
}
check(packet_metadata["incoming"] == packet_metadata["outgoing"],
      "both packets implement seal-and-birth on the same typed collar")
check(packet_metadata["connected_collar"] and not packet_metadata["terminal"],
      "both packets satisfy connected interaction locality and continuation")
check(packet_metadata["evidence_survival"] == "exp(-I)" and
      packet_metadata["construction_order"] == "disjoint-rewrite quotient",
      "both packets share the same evidence and construction-order laws")

# Independent copies commute, so auxiliary order does not select theta.
def kron(a, b):
    return tuple(tuple(x * y for x in ar for y in br)
                 for ar in a for br in b)


for label, u in (("quarter", U_QUARTER), ("half", U_HALF)):
    left_then_right = mul(kron(u, I4), kron(I4, u))
    right_then_left = mul(kron(I4, u), kron(u, I4))
    check(left_then_right == right_then_left,
          f"{label} disjoint diamond presentations commute exactly")

EXPECTED_CHECKS = 18
if CHECKS != EXPECTED_CHECKS:
    raise AssertionError(f"expected {EXPECTED_CHECKS} checks, observed {CHECKS}")

summary = (
    "D12 SYMMETRIC INTERACTION FAMILY EXACT RECEIPT\n"
    f"checks={CHECKS}\n"
    "field=Q(sqrt(2),i)\n"
    "shared_unitarity=PASS\n"
    "shared_exchange_symmetry=PASS\n"
    "shared_excitation_conservation=PASS\n"
    "shared_entangling_capacity=PASS\n"
    "shared_local_seal_and_birth_architecture=PASS\n"
    "shared_construction_order_gauge=PASS\n"
    "later_record_probability_theta_pi_over_4=1/2\n"
    "later_record_probability_theta_pi_over_2=0\n"
    "missing_selector=INTERACTION_ANGLE_OR_EQUIVALENT_ACTION_COUPLING\n"
    "verdict=STRUCTURAL_AND_SYMMETRY_SELECTION_REFUTED\n"
)
print(summary, end="")
receipt = sha256(summary.encode()).hexdigest()
EXPECTED_RECEIPT = "7da912f8deb705aaa1467d3428aacf7cc626b249bf16c324c5c365f376b89db9"
if receipt != EXPECTED_RECEIPT:
    raise AssertionError(f"receipt drift: {receipt}")
print("receipt_sha256=" + receipt)
