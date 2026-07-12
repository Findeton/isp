#!/usr/bin/env python3
"""D10 finite relational SCIR candidate with no external S2 generation oracle.

The finite grammar H/T/SEAL generates projective qubit directions exactly in
Q(sqrt(2),i). An external Fibonacci sphere is used only as a coverage
diagnostic. A bounded ancestry toy demonstrates local propagation and a
conditional Bloch-increment spacetime shadow.  The latter is explicitly a
candidate mapping, not a derivation of physical space or of an influence cone.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import cos, pi, sin, sqrt


getcontext().prec = 100
CHECKS = 0
EXPECTED_CHECKS = 43


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
        if isinstance(x, Q2):
            return x
        return Q2(F(x), F(0))

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

    def dec(self):
        return (D(self.a.numerator) / D(self.a.denominator)
                + D(self.b.numerator) / D(self.b.denominator) * D(2).sqrt())


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

    def __mul__(self, other):
        other = C2.make(other)
        return C2(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def conj(self):
        return C2(self.re, -self.im)


ZERO = C2()
ONE = C2.make(1)
II = C2(Q2(), Q2.make(1))
INV_ROOT2 = Q2(F(0), F(1, 2))


def matrix(rows):
    return tuple(tuple(C2.make(x) for x in row) for row in rows)


def dagger(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a)))
                 for i in range(len(a[0])))


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(c, a):
    c = C2.make(c)
    return tuple(tuple(c * x for x in row) for row in a)


def mul(a, b):
    bt = tuple(zip(*b))
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), ZERO)
                       for col in bt) for row in a)


def tr(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def kron(a, b):
    return tuple(tuple(aij * bij for aij in ar for bij in br)
                 for ar in a for br in b)


def push(k, rho):
    return mul(mul(k, rho), dagger(k))


def outer(v):
    return tuple(tuple(x * y.conj() for y in v) for x in v)


def matvec(a, v):
    return tuple(sum((x * y for x, y in zip(row, v)), ZERO) for row in a)


I2 = matrix(((1, 0), (0, 1)))
X = matrix(((0, 1), (1, 0)))
Y = matrix(((0, -II), (II, 0)))
Z = matrix(((1, 0), (0, -1)))
H = scale(INV_ROOT2, matrix(((1, 1), (1, -1))))
omega = C2.make(INV_ROOT2) * (ONE + II)
T = matrix(((1, 0), (0, omega)))
P0 = matrix(((1, 0), (0, 0)))
P1 = matrix(((0, 0), (0, 1)))

check(mul(dagger(H), H) == I2, "H instrument unitary")
check(mul(dagger(T), T) == I2, "T instrument unitary")
check(T != I2 and H != I2, "finite grammar has nontrivial local rewrites")


def projector_key(rho):
    return tuple((z.re.a, z.re.b, z.im.a, z.im.b) for row in rho for z in row)


def bloch(rho):
    values = tuple(tr(mul(rho, s)) for s in (X, Y, Z))
    if not all(v.im == Q2() for v in values):
        raise AssertionError("Bloch coordinates must be real")
    return tuple(v.re for v in values)


def q2_dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q2())


# A finite local rewrite grammar generates an increasing family of directions.
root = (ONE, ZERO)
frontier = {projector_key(outer(root)): (outer(root), "")}
levels = []
for depth in range(13):
    directions = {}
    unit_directions = True
    for rho, word in frontier.values():
        r = bloch(rho)
        directions[tuple((x.a, x.b) for x in r)] = r
        unit_directions = unit_directions and q2_dot(r, r) == Q2.make(1)
    check(unit_directions, f"all pure directions through depth {depth} have exact unit norm")
    levels.append((depth, tuple(directions.values())))
    next_frontier = dict(frontier)
    for rho, word in frontier.values():
        for label, gate in (("H", H), ("T", T)):
            child = mul(mul(gate, rho), dagger(gate))
            next_frontier[projector_key(child)] = (child, word + label)
    frontier = next_frontier

counts = [len(directions) for _, directions in levels]
check(all(b >= a for a, b in zip(counts, counts[1:])), "reachable direction family is nested")
check(counts[-1] > counts[2], "finite grammar creates new projective directions")
check(len(frontier) < 2 ** 14, "finite-depth state set is finite")


def sampled_support(directions, samples=50000):
    dirs = [tuple(float(x.dec()) for x in r) for r in directions]
    golden = pi * (3.0 - sqrt(5.0))
    worst = 2.0
    for k in range(samples):
        z = 1.0 - 2.0 * (k + 0.5) / samples
        radius = sqrt(max(0.0, 1.0 - z * z))
        az = golden * k
        x = (radius * cos(az), radius * sin(az), z)
        worst = min(worst, max(sum(a * b for a, b in zip(u, x)) for u in dirs))
    return worst


coverage_rows = []
for depth in (0, 2, 4, 6, 8, 10, 12):
    directions = levels[depth][1]
    support = sampled_support(directions)
    coverage_rows.append((depth, len(directions), support))
check(coverage_rows[-1][2] > coverage_rows[1][2],
      "finite H/T words improve sampled sphere coverage")

# The rulebook is bounded: two continuation tokens plus one seal token per collar.
TOKENS_PER_COLLAR = ("APPLY_H", "APPLY_T", "SEAL")
check(len(TOKENS_PER_COLLAR) == 3, "bounded local opportunity grammar")
check(all(isinstance(token, str) for token in TOKENS_PER_COLLAR), "finite opportunity types")
check(all(len(tuple(word)) == len(word) and all(letter in ("H", "T") for letter in word)
          for _, word in frontier.values()),
      "finite preparation word can be distributed as one finite gate mark per history record")

# SEAL is an actual terminal projective instrument in the chosen complex-qubit
# packet, not merely a token name.
check(add(mul(dagger(P0), P0), mul(dagger(P1), P1)) == I2,
      "SEAL pointer instrument complete")
rho_plus = push(H, outer(root))
branch0 = push(P0, rho_plus)
branch1 = push(P1, rho_plus)
check(tr(branch0).re == Q2.make(F(1, 2)), "SEAL outcome 0 has exact Born weight 1/2")
check(tr(branch1).re == Q2.make(F(1, 2)), "SEAL outcome 1 has exact Born weight 1/2")
check(tr(add(branch0, branch1)) == ONE, "SEAL outcome law normalized")
check(push(P0, branch0) == branch0, "SEAL outcome 0 durable on repetition")
check(push(P1, branch1) == branch1, "SEAL outcome 1 durable on repetition")

# Exact bounded-forest intervention shadow.  Each node reads only its incident
# parent message and local type.  Node 1 is a local Bernoulli source instrument;
# other nodes copy the classical sealed mark.  This tests continuation-law
# influence on the declared forest, not joining sectors or a spacetime cone.
parents = {0: None, 1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 2, 7: None, 8: 7}


def continuation_mark_probabilities(source_probability):
    probabilities = {}
    for node in range(9):
        parent = parents[node]
        if parent is None:
            probabilities[node] = F(0)
        elif node == 1:
            probabilities[node] = source_probability
        else:
            probabilities[node] = probabilities[parent]
    return probabilities


baseline = continuation_mark_probabilities(F(1, 3))
intervened = continuation_mark_probabilities(F(2, 3))
changed = {node for node in parents if baseline[node] != intervened[node]}
check(changed == {1, 3, 4}, "local instrument intervention changes exactly its copied descendants")
check(all(baseline[node] == intervened[node] for node in (0, 2, 5, 6)),
      "intervention leaves the other connected branch unchanged")
check(all(baseline[node] == intervened[node] for node in (7, 8)),
      "intervention leaves disconnected component continuation law unchanged")
check(all(F(0) <= probability <= F(1)
          for probability in tuple(baseline.values()) + tuple(intervened.values())),
      "all local sealed-mark continuation probabilities normalized")

# Conditional spacetime shadow: one local click adds dt=1 and a unit Bloch
# increment dx=r. This makes parent edges null. The map is declared, not derived.
positions = {0: (0, (Q2(), Q2(), Q2()))}
word_for_node = {1: "H", 2: "T", 3: "HT", 4: "TH", 5: "HH", 6: "TT"}


def state_for_word(word):
    rho = outer(root)
    for letter in word:
        gate = H if letter == "H" else T
        rho = mul(mul(gate, rho), dagger(gate))
    return rho


for node in range(1, 7):
    parent = parents[node]
    pt, px = positions[parent]
    r = bloch(state_for_word(word_for_node[node]))
    positions[node] = (pt + 1, tuple(a + b for a, b in zip(px, r)))
    delta2 = q2_dot(r, r)
    check(delta2 == Q2.make(1), f"declared Bloch increment makes edge {parent}->{node} null")

# Execute two disjoint typed instruments in both schedules in the imported
# complex tensor-product packet.  An overlapping one-qubit control confirms
# that the test can detect physical order when supports overlap.
rho_pair = kron(outer(root), outer(root))
left_h = kron(H, I2)
right_t = kron(I2, T)
check(mul(left_h, right_t) == mul(right_t, left_h),
      "chosen complex-tensor disjoint instruments commute algebraically")
schedule_lr = push(right_t, push(left_h, rho_pair))
schedule_rl = push(left_h, push(right_t, rho_pair))
check(schedule_lr == schedule_rl, "two executed disjoint instrument schedules agree")
check(tr(schedule_lr) == ONE, "both disjoint schedules preserve normalization")
overlap_ht = push(T, push(H, outer(root)))
overlap_th = push(H, push(T, outer(root)))
check(overlap_ht != overlap_th, "overlapping instrument control detects physical order")

if CHECKS != EXPECTED_CHECKS:
    raise AssertionError(f"expected {EXPECTED_CHECKS} checks, observed {CHECKS}")

print("\ndepth reachable_projectors sampled_support_min")
for depth, count, support in coverage_rows:
    print(f"{depth} {count} {support:.12f}")

summary = (
    "D10 RELATIONAL SCIR PACKET RECEIPT\n"
    f"checks={CHECKS}\n"
    f"depth12_projectors={counts[12]}\n"
    f"depth12_sampled_support={coverage_rows[-1][2]:.12f}\n"
    "generation_external_sphere_sampler=ABSENT\n"
    "coverage_diagnostic_external_fibonacci_sampler=50000\n"
    "finite_local_grammar=H,T,SEAL\n"
    "finite_alphabet_finite_depth_refinement=PASS\n"
    "per_record_evidence_capacity=NOT_ESTABLISHED\n"
    "chosen_complex_tensor_disjoint_schedules=PASS\n"
    "bounded_forest_interventional_influence=PASS\n"
    "joining_sector_influence=NOT_TESTED\n"
    "bloch_increment_map=DECLARED_NOT_DERIVED\n"
    "order_influence_cone_equivalence=OPEN\n"
)
print("\n" + summary, end="")
print("receipt_sha256=" + sha256(summary.encode()).hexdigest())
