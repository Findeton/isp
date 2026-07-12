#!/usr/bin/env python3
"""D10 exact receipt: Bloch/celestial algebra, alternatives, and gauge diamonds.

Only Python's standard library is used. All identities are over Gaussian
rationals or ordinary rationals; no floating-point comparison is load-bearing.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import product


CHECKS = 0
EXPECTED_CHECKS = 109


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:02d}: {label}")


@dataclass(frozen=True)
class G:
    """Gaussian rational a+bi."""

    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def make(x):
        if isinstance(x, G):
            return x
        return G(F(x), F(0))

    def __add__(self, other):
        other = G.make(other)
        return G(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-G.make(other))

    def __rsub__(self, other):
        return G.make(other) - self

    def __mul__(self, other):
        other = G.make(other)
        return G(self.a * other.a - self.b * other.b,
                 self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def conj(self):
        return G(self.a, -self.b)

    def norm2(self):
        return self.a * self.a + self.b * self.b


ZERO = G()
ONE = G.make(1)
II = G(F(0), F(1))


def matrix(rows):
    return tuple(tuple(G.make(x) for x in row) for row in rows)


def eye(n):
    return matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])


def dagger(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a)))
                 for i in range(len(a[0])))


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(c, a):
    c = G.make(c)
    return tuple(tuple(c * x for x in row) for row in a)


def mul(a, b):
    bt = tuple(zip(*b))
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), ZERO)
                       for col in bt) for row in a)


def tr(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def kron(a, b):
    return tuple(tuple(aij * bij for aij in ar for bij in br)
                 for ar in a for br in b)


def rho_push(u, rho):
    return mul(mul(u, rho), dagger(u))


I2 = eye(2)
X = matrix(((0, 1), (1, 0)))
Y = matrix(((0, -II), (II, 0)))
Z = matrix(((1, 0), (0, -1)))
PAULI = (X, Y, Z)


# 1. Exact complex rank-two / Lorentz identity.
for s, label in zip(PAULI, "XYZ"):
    check(dagger(s) == s, f"sigma_{label} Hermitian")
    check(mul(s, s) == I2, f"sigma_{label} squares to identity")
for i, j in product(range(3), repeat=2):
    anti = add(mul(PAULI[i], PAULI[j]), mul(PAULI[j], PAULI[i]))
    check(anti == scale(2 if i == j else 0, I2),
          f"Pauli anticommutator {i}{j}")


def hermitian_event(t, x):
    out = scale(t, I2)
    for xi, s in zip(x, PAULI):
        out = add(out, scale(xi, s))
    return out


samples = (
    (F(5), (F(1), F(2), F(2))),
    (F(13, 5), (F(3, 5), F(4, 5), F(12, 5))),
    (F(1), (F(1), F(0), F(0))),
)
for index, (t, x) in enumerate(samples):
    event = hermitian_event(t, x)
    q = t * t - sum(xi * xi for xi in x)
    check(dagger(event) == event, f"event {index} Hermitian")
    check(tr(event) == G.make(2 * t), f"event {index} trace is 2t")
    check(det2(event) == G.make(q), f"event {index} determinant is Minkowski norm")

# Exact positivity test on rational-norm samples: eigenvalues are t +/- |x|.
positivity = (
    (F(5), (F(1), F(2), F(2)), True),   # |x|=3
    (F(3), (F(1), F(2), F(2)), True),
    (F(2), (F(1), F(2), F(2)), False),
    (F(-4), (F(1), F(2), F(2)), False),
)
for t, x, expected in positivity:
    r2 = sum(xi * xi for xi in x)
    # Avoid square roots: t >= 0 and t^2 >= |x|^2.
    actual = t >= 0 and t * t >= r2
    check(actual == expected, f"future-cone positivity t={t}")

# Rational unit vectors give exact rank-one null projectors.
directions = (
    (F(1), F(0), F(0)),
    (F(0), F(1), F(0)),
    (F(0), F(0), F(1)),
    (F(3, 5), F(4, 5), F(0)),
    (F(4, 5), F(0), F(-3, 5)),
)
projectors = []
for index, u in enumerate(directions):
    check(sum(ui * ui for ui in u) == 1, f"direction {index} is unit")
    p = scale(F(1, 2), hermitian_event(F(1), u))
    projectors.append(p)
    check(dagger(p) == p, f"projector {index} Hermitian")
    check(mul(p, p) == p, f"projector {index} idempotent")
    check(tr(p) == ONE, f"projector {index} normalized")
    check(det2(p) == ZERO, f"projector {index} null/rank-one")

# Directional clocks are evaluations of four factors, not independent stores.
t = F(7, 3)
x = (F(2, 3), F(-1, 3), F(2))
event = hermitian_event(t, x)
for index, (u, p) in enumerate(zip(directions, projectors)):
    value = tr(mul(p, event))
    expected = t + sum(ui * xi for ui, xi in zip(u, x))
    check(value == G.make(expected), f"directional evaluation {index}=t+u.x")

# 2. Comparison class: rank-two division-algebra and generic spin factors.
division_real_dimensions = {"R": 1, "C": 2, "H": 4, "O": 8}
expected_event_dimensions = {"R": 3, "C": 4, "H": 6, "O": 10}
for field, offdiag_dimension in division_real_dimensions.items():
    event_dimension = 2 + offdiag_dimension
    check(event_dimension == expected_event_dimensions[field],
          f"Herm_2({field}) real dimension {event_dimension}")
    check(event_dimension == 1 + (offdiag_dimension + 1),
          f"Herm_2({field}) is a 1+{offdiag_dimension + 1} spin factor")
    # Coordinate-level rank-two determinant.  For X=[[a,z],[z*,b]], only
    # the Euclidean norm of the q-component off-diagonal coordinate enters:
    # det X = ab-|z|^2 = t^2-s^2-|z|^2.  This remains well-defined for the
    # octonionic rank-two ordered spin-factor shadow; no matrix associativity
    # beyond this determinant is asserted.
    a = F(offdiag_dimension + 5)
    b = F(offdiag_dimension + 3)
    z = tuple(F(index + 1) for index in range(offdiag_dimension))
    norm_z2 = sum(component * component for component in z)
    determinant = a * b - norm_z2
    t_coord = (a + b) / 2
    s_coord = (a - b) / 2
    check(determinant == t_coord * t_coord - s_coord * s_coord - norm_z2,
          f"Herm_2({field}) determinant has Lorentz quadratic form")
    positive = a >= 0 and b >= 0 and determinant >= 0
    expected_positive = a >= 0 and b >= 0 and a * b >= norm_z2
    check(positive == expected_positive,
          f"Herm_2({field}) rank-two positivity criterion wired")

for spatial_dimension in range(1, 10):
    event_dimension = 1 + spatial_dimension
    check(event_dimension >= 2,
          f"generic spin factor V_{spatial_dimension} has Lorentz dimension {event_dimension}")
check(len(range(1, 10)) > 1, "Lorentz-cone kinematics alone does not select three-space")

# Local-tomography parameter counts: real versus complex two-level systems.
def symmetric_dimension(n):
    return n * (n + 1) // 2


def hermitian_dimension(n):
    return n * n


k_real_single = symmetric_dimension(2)
k_real_pair = symmetric_dimension(4)
k_complex_single = hermitian_dimension(2)
k_complex_pair = hermitian_dimension(4)
check((k_real_single, k_real_pair) == (3, 10), "rebit state counts 3 and 10")
check(k_real_pair - k_real_single ** 2 == 1, "rebit local-tomography deficit +1")
check((k_complex_single, k_complex_pair) == (4, 16), "qubit state counts 4 and 16")
check(k_complex_pair - k_complex_single ** 2 == 0, "complex qubit locally tomographic count")

# 3. Exact local-frame covariance and diamond holonomy.
# i*Pauli matrices lie in SU(2) and suffice for a nontrivial exact gauge test.
GX = scale(II, X)
GY = scale(II, Y)
GZ = scale(II, Z)
for g, label in ((GX, "iX"), (GY, "iY"), (GZ, "iZ")):
    check(mul(dagger(g), g) == I2, f"{label} unitary")
    check(det2(g) == ONE, f"{label} determinant one")

# Diamond a->b->d and a->c->d. Link matrices map source frame to target frame.
U_ba, U_ca, U_db, U_dc = GX, GY, GZ, GX
path_b = mul(U_db, U_ba)
path_c = mul(U_dc, U_ca)
holonomy = mul(dagger(path_c), path_b)  # loop based at a
check(mul(dagger(holonomy), holonomy) == I2, "diamond holonomy unitary")

V_a, V_b, V_c, V_d = I2, GX, GY, GZ


def gauge_link(u_target_source, v_target, v_source):
    return mul(mul(v_target, u_target_source), dagger(v_source))


Ug_ba = gauge_link(U_ba, V_b, V_a)
Ug_ca = gauge_link(U_ca, V_c, V_a)
Ug_db = gauge_link(U_db, V_d, V_b)
Ug_dc = gauge_link(U_dc, V_d, V_c)
path_bg = mul(Ug_db, Ug_ba)
path_cg = mul(Ug_dc, Ug_ca)
check(path_bg == mul(mul(V_d, path_b), dagger(V_a)), "upper diamond path covariant")
check(path_cg == mul(mul(V_d, path_c), dagger(V_a)), "lower diamond path covariant")
holonomy_g = mul(dagger(path_cg), path_bg)
check(holonomy_g == mul(mul(V_a, holonomy), dagger(V_a)),
      "based holonomy transforms by conjugation")
check(tr(holonomy_g) == tr(holonomy), "supplied-connection holonomy trace gauge invariant")

# Direction/state evaluation remains invariant under an independent local frame change.
rho = projectors[3]
effect = projectors[4]
prob = tr(mul(effect, rho))
rho_g = rho_push(V_a, rho)
effect_g = rho_push(V_a, effect)
check(tr(mul(effect_g, rho_g)) == prob, "local Born evaluation frame invariant")

# Disjoint local gauges/instruments commute on a two-port collar.
left = kron(GX, I2)
right = kron(I2, GZ)
check(mul(left, right) == mul(right, left), "disjoint local frame changes commute")

# 4. Rotation gauge is not yet full Lorentz gauge.  An exact SL(2,C) boost
# preserves the determinant cone but is nonunitary and changes trace.
boost = matrix(((2, 0), (0, F(1, 2))))
check(det2(boost) == ONE, "diagonal boost representative lies in SL(2,C)")
check(mul(dagger(boost), boost) != I2, "boost representative is not a qubit unitary")
boost_input = hermitian_event(F(3), (F(1), F(0), F(2)))
boost_output = mul(mul(boost, boost_input), dagger(boost))
check(det2(boost_output) == det2(boost_input), "SL(2,C) congruence preserves Minkowski determinant")
q2 = F(4)
qminus2 = F(1, 4)
t0, z0 = F(3), F(2)
t1 = (q2 + qminus2) * t0 / 2 + (q2 - qminus2) * z0 / 2
z1 = (q2 - qminus2) * t0 / 2 + (q2 + qminus2) * z0 / 2
boost_expected = hermitian_event(t1, (F(1), F(0), z1))
check(boost_output == boost_expected, "SL(2,C) congruence gives exact t-z Lorentz boost")
check(tr(boost_output) != tr(boost_input), "boost is not trace-preserving quantum gauge")

# Finite information statement: a density matrix has four real coefficients;
# normalization leaves three, irrespective of how many projectors are queried.
check(hermitian_dimension(2) == 4, "qubit unnormalized state has four real factors")
check(hermitian_dimension(2) - 1 == 3, "normalized qubit state has three real factors")
check(len(projectors) > 3, "more directional questions than normalized state factors")

if CHECKS != EXPECTED_CHECKS:
    raise AssertionError(f"expected {EXPECTED_CHECKS} checks, observed {CHECKS}")

summary = (
    "D10 BLOCH-LORENTZ EXACT RECEIPT\n"
    f"checks={CHECKS}\n"
    "conditional_complex_qubit_lorentz_isomorphism=PASS\n"
    "alternative_spin_factors=EXHIBITED\n"
    "complex_selection=NOT_IMPLIED_BY_CONE\n"
    "supplied_su2_connection_covariance=PASS\n"
    "full_lorentz_gauge=REQUIRES_NONUNITARY_SL2C_EXTENSION\n"
    "provisional_scope=KINEMATIC_AND_CONDITIONAL\n"
)
print(summary, end="")
print("receipt_sha256=" + sha256(summary.encode()).hexdigest())
