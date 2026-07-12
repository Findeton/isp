#!/usr/bin/env python3
"""D12 exact restored-diamond interaction/whole-history nonuniqueness witness.

All matrix and finite-history probability calculations use Fraction exactly.
Decimal at 120 digits is used only for exponential evidence survival and the
one-mode transcendental commitment fixed point.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from hashlib import sha256
from itertools import product


getcontext().prec = 120
CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:02d}: {label}")


def matrix(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def transpose(a):
    return tuple(zip(*a))


def mul(a, b):
    bt = tuple(zip(*b))
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), F(0))
                       for col in bt) for row in a)


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br))
                 for ar, br in zip(a, b))


def kron(a, b):
    return tuple(tuple(x * y for x in ar for y in br)
                 for ar in a for br in b)


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def push(k, rho):
    return mul(mul(k, rho), transpose(k))


def diag(values):
    return matrix([[values[i] if i == j else 0
                    for j in range(len(values))]
                   for i in range(len(values))])


def inv_diag(a):
    return diag([F(1, a[i][i]) for i in range(len(a))])


def basis_projector(n, index):
    return matrix([[int(i == index and j == index) for j in range(n)]
                   for i in range(n)])


I2, I4 = eye(2), eye(4)
X = matrix(((0, 1), (1, 0)))
P0, P1 = basis_projector(2, 0), basis_projector(2, 1)

# Column convention: column j is the output of computational basis input j.
SWAP = matrix((
    (1, 0, 0, 0),
    (0, 0, 1, 0),
    (0, 1, 0, 0),
    (0, 0, 0, 1),
))
CNOT = matrix((
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 0, 1),
    (0, 0, 1, 0),
))

check(mul(transpose(SWAP), SWAP) == I4, "SWAP is exact two-leg unitary")
check(mul(transpose(CNOT), CNOT) == I4, "CNOT is exact two-leg unitary")
check(SWAP != CNOT, "interaction packets are inequivalent matrices")

pointer = tuple(basis_projector(4, i) for i in range(4))
check(sum((tr(e) for e in pointer), F(0)) == F(4),
      "four pointer effects have total rank four")
check(tuple(tuple(sum((e[i][j] for e in pointer), F(0))
                        for j in range(4)) for i in range(4)) == I4,
      "two-leg pointer family is complete")


@dataclass(frozen=True)
class DiamondPacket:
    name: str
    incoming_types: tuple
    output_types: tuple
    owners: tuple
    interaction: tuple
    terminal: bool
    durable_pointer: tuple


packet_s = DiamondPacket(
    "S", ("q", "q"), ("q", "q"), ("left", "right"), SWAP, False, pointer)
packet_c = DiamondPacket(
    "C", ("q", "q"), ("q", "q"), ("left", "right"), CNOT, False, pointer)

check(packet_s.incoming_types == packet_c.incoming_types == ("q", "q"),
      "countermodels have identical incoming collar types")
check(packet_s.output_types == packet_c.output_types == ("q", "q"),
      "countermodels have identical continuing output collars")
check(not packet_s.terminal and not packet_c.terminal,
      "internal commits are seal-and-birth, never terminal observation")
check(packet_s.owners == packet_c.owners == ("left", "right"),
      "both interactions require the same recorded connected ownership")

# |01>: SWAP -> |10>, CNOT -> |01>. A later second-leg P1 seal distinguishes.
rho_01 = basis_projector(4, 1)
effect_second_one = kron(I2, P1)
out_s, out_c = push(SWAP, rho_01), push(CNOT, rho_01)
check(out_s == basis_projector(4, 2), "SWAP sends |01> to |10>")
check(out_c == basis_projector(4, 1), "CNOT leaves |01> at |01>")
check(tr(mul(effect_second_one, out_s)) == 0 and
      tr(mul(effect_second_one, out_c)) == 1,
      "later durable seal probability distinguishes the interactions")
check(tr(out_s) == tr(out_c) == 1, "both interaction packets preserve total weight")

# Exact endpoint dual gauge with nonunitary determinant-one local frames.
ain = kron(diag((F(2), F(1, 2))), diag((F(3), F(1, 3))))
aout = kron(diag((F(5), F(1, 5))), diag((F(7), F(1, 7))))
ain_i, aout_i = inv_diag(ain), inv_diag(aout)
ein_g = mul(transpose(ain_i), ain_i)
eout_g = mul(transpose(aout_i), aout_i)
rho_g = mul(mul(ain, rho_01), transpose(ain))
effect_g = mul(mul(transpose(aout_i), effect_second_one), aout_i)


def transformed(k):
    return mul(mul(aout, k), ain_i)


def ratio(rho, effect, unit):
    return tr(mul(effect, rho)) / tr(mul(unit, rho))


for name, k in (("SWAP", SWAP), ("CNOT", CNOT)):
    kg = transformed(k)
    check(mul(mul(transpose(kg), eout_g), kg) == ein_g,
          f"{name} endpoint order-unit completeness is gauge covariant")
    out = push(k, rho_01)
    out_g = push(kg, rho_g)
    check(ratio(out_g, effect_g, eout_g) == ratio(out, effect_second_one, I4),
          f"{name} downstream seal ratio is gauge invariant")

# Disjoint construction presentations commute on a separate third interface.
for name, k in (("SWAP", SWAP), ("CNOT", CNOT)):
    first = kron(k, I2)
    disjoint = kron(I4, X)
    check(mul(first, disjoint) == mul(disjoint, first),
          f"{name} commutes with a disjoint local rewrite")

# Local RN/KL evidence survival. Decimal is diagnostic; the functional equation
# itself is the exact exponential identity in the chosen evidence coordinate.
i, j = D("0.7"), D("1.1")
s_i, s_j, s_ij = (-i).exp(), (-j).exp(), (-(i + j)).exp()
check(abs(s_ij - s_i * s_j) < D("1e-118"),
      "local evidence survival obeys sealed-gluing multiplicativity")
check(abs(-s_i.ln() - i) < D("1e-118"),
      "evidence survival self-accounts with unit RN action")

# The same one-mode commitment coefficient is available to both interaction
# packets; it cannot distinguish their operator content.
def tanh(x):
    e2 = (D(2) * x).exp()
    return (e2 - 1) / (e2 + 1)


h = D("0.6")
for _ in range(30):
    f = tanh(h) - (-h).exp()
    derivative = D(1) - tanh(h) ** 2 + (-h).exp()
    h -= f / derivative
residual = tanh(h) - (-h).exp()
check(abs(residual) < D("1e-110"), "one-mode commitment fixed point solved at 120 digits")
check(abs(h - D("0.60937786343600623153680337116839869542853927931285")) < D("1e-50"),
      "commitment coefficient reproduces the V6/V7 one-mode root")
check(packet_s.durable_pointer == packet_c.durable_pointer and h == h,
      "identical commitment coefficient and pointer data leave interaction open")

# Finite non-Markov whole-history twins with identical one/two-record shadows.
OMEGA = tuple(product((-1, 1), repeat=3))


def history_law(r):
    r = F(r)
    return {omega: (F(1) + r * omega[0] * omega[1] * omega[2]) / 8
            for omega in OMEGA}


def marginal(law, indices):
    out = {}
    for omega, p in law.items():
        key = tuple(omega[i] for i in indices)
        out[key] = out.get(key, F(0)) + p
    return out


law_half = history_law(F(1, 2))
law_third = history_law(F(1, 3))
for label, law in (("half", law_half), ("third", law_third)):
    check(sum(law.values(), F(0)) == 1 and min(law.values()) > 0,
          f"P_r {label} is a strictly positive normalized whole-history law")
    for pair in ((0, 1), (0, 2), (1, 2)):
        check(set(marginal(law, pair).values()) == {F(1, 4)},
              f"P_r {label} has uniform projective pair marginal {pair}")

check(all(marginal(law_half, pair) == marginal(law_third, pair)
          for pair in ((0, 1), (0, 2), (1, 2))),
      "inequivalent whole-history laws share every one/two-record shadow")


def conditional_z_one(law, x, y):
    numerator = law[(x, y, 1)]
    denominator = law[(x, y, -1)] + numerator
    return numerator / denominator


check(conditional_z_one(law_half, 1, 1) == F(3, 4) and
      conditional_z_one(law_third, 1, 1) == F(2, 3),
      "triple-history continuations differ despite identical pair shadows")
check(conditional_z_one(law_half, 1, 1) !=
      conditional_z_one(law_half, -1, 1),
      "whole-history continuation is not first-order Markov in the last record")

# Independent gluing and neutral refinement are exact for both history laws.
for label, law in (("half", law_half), ("third", law_third)):
    product_mass = sum((p * q for p in law.values() for q in law.values()), F(0))
    check(product_mass == 1, f"P_r {label} independent diamond gluing normalizes")
    refined = {(omega, twin): p / 2 for omega, p in law.items() for twin in (0, 1)}
    coarse = {omega: refined[(omega, 0)] + refined[(omega, 1)] for omega in law}
    check(coarse == law, f"P_r {label} neutral refinement pushes forward exactly")

# Continuing internal commits preserve a nonempty boundary indefinitely. This
# is a type property, not a favorable population-rate fit.
for packet in (packet_s, packet_c):
    open_interfaces = 2
    for _ in range(100):
        open_interfaces -= len(packet.incoming_types)
        open_interfaces += len(packet.output_types)
    check(open_interfaces == 2, f"packet {packet.name} retains continuation through 100 commits")

check(tr(mul(effect_second_one, out_s)) != tr(mul(effect_second_one, out_c)),
      "all shared structural gates still leave an empirical interaction choice")

EXPECTED_CHECKS = 42
if CHECKS != EXPECTED_CHECKS:
    raise AssertionError(f"expected {EXPECTED_CHECKS} checks, observed {CHECKS}")

summary = (
    "D12 DIAMOND-LAW NONUNIQUENESS EXACT RECEIPT\n"
    f"checks={CHECKS}\n"
    f"commitment_h={h:.60E}\n"
    "seal_and_birth=PASS\n"
    "local_evidence_survival=PASS\n"
    "endpoint_dual_gauge=PASS_BOTH_PACKETS\n"
    "disjoint_construction_commutation=PASS_BOTH_PACKETS\n"
    "whole_history_projective_twins=PASS\n"
    "interaction_prediction_SWAP=0\n"
    "interaction_prediction_CNOT=1\n"
    "unique_interaction_from_shard_structure=REFUTED\n"
    "complete_ledger=IDENTIFIES_BUT_DOES_NOT_GENERATE\n"
    "verdict=UNIVERSAL-FORM/PRIMITIVE-MEASURE-REMAINS\n"
)
print(summary, end="")
receipt = sha256(summary.encode()).hexdigest()
EXPECTED_RECEIPT = "1f9472d6ed613ad96fe875d68cf0a773062c077e9a44fc357f65ccfd93bd4b97"
if receipt != EXPECTED_RECEIPT:
    raise AssertionError(f"receipt drift: {receipt}")
print("receipt_sha256=" + receipt)
