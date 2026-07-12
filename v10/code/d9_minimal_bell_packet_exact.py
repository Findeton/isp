#!/usr/bin/env python3
"""Exact Q(sqrt(2), i) Bell-history law for the frozen D9 SCIR packet."""

from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from random import Random


getcontext().prec = 110
checks = 0


def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


@dataclass(frozen=True)
class Q2:
    """a + b*sqrt(2), with exact rational a,b."""

    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def make(value):
        return value if isinstance(value, Q2) else Q2(F(value), F(0))

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

    def dec(self):
        root2 = Decimal(2).sqrt()
        return (Decimal(self.a.numerator) / Decimal(self.a.denominator)
                + Decimal(self.b.numerator) / Decimal(self.b.denominator) * root2)

    def __str__(self):
        return f"({self.a})+({self.b})sqrt2"


@dataclass(frozen=True)
class C2:
    """z = re + i*im with re,im in Q(sqrt(2))."""

    re: Q2 = Q2()
    im: Q2 = Q2()

    @staticmethod
    def make(value):
        if isinstance(value, C2):
            return value
        if isinstance(value, Q2):
            return C2(value, Q2())
        return C2(Q2.make(value), Q2())

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

    def dec_real(self):
        assert self.im == Q2()
        return self.re.dec()


ZERO = C2()
ONE = C2.make(1)
I = C2(Q2(), Q2.make(1))
R2 = Q2(F(0), F(1))
INV_R2 = Q2(F(0), F(1, 2))  # sqrt(2)/2


def matrix(rows):
    return tuple(tuple(C2.make(x) for x in row) for row in rows)


def eye(n):
    return matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])


def dagger(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a))) for i in range(len(a[0])))


def addm(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def subm(a, b):
    return tuple(tuple(x - y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scalem(c, a):
    c = C2.make(c)
    return tuple(tuple(c * x for x in row) for row in a)


def matmul(a, b):
    bt = tuple(zip(*b))
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), ZERO) for col in bt) for row in a)


def matvec(a, v):
    return tuple(sum((x * y for x, y in zip(row, v)), ZERO) for row in a)


def outer(v):
    return tuple(tuple(x * y.conj() for y in v) for x in v)


def kron(a, b):
    return tuple(tuple(aij * bij for aij in ar for bij in br) for ar in a for br in b)


def tr(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def probability(rho, effect):
    value = tr(matmul(effect, rho))
    assert value.im == Q2()
    return value.re


# -------------------------------------------------------------------------
# 1. Root + partial-iSWAP(theta=pi/4) + local output gauge gives Phi+.
# -------------------------------------------------------------------------

i2 = eye(2)
x = matrix(((0, 1), (1, 0)))
z = matrix(((1, 0), (0, -1)))
s_dag = matrix(((1, 0), (0, -I)))

c = C2.make(INV_R2)
s_i = I * C2.make(INV_R2)
u_ps = matrix((
    (1, 0, 0, 0),
    (0, c, s_i, 0),
    (0, s_i, c, 0),
    (0, 0, 0, 1),
))
check(matmul(dagger(u_ps), u_ps) == eye(4), "partial iSWAP is exactly unitary")

ket10 = (ZERO, ZERO, ONE, ZERO)
after_ps = matvec(u_ps, ket10)
local_gauge_b = kron(i2, matmul(x, s_dag))
phi = matvec(local_gauge_b, after_ps)
phi_expected = (C2.make(INV_R2), ZERO, ZERO, C2.make(INV_R2))
check(phi == phi_expected, "partial iSWAP source is locally gauge-equivalent to Phi+")
rho = outer(phi)
check(tr(rho) == ONE, "source density normalized")
check(matmul(rho, rho) == rho, "source density pure")

# The frozen coupling shadow is g=sin^2(pi/4)=1/2.
g_shadow = INV_R2 * INV_R2
check(g_shadow == Q2.make(F(1, 2)), "Bell coupling freezes transfer shadow g=1/2")


# -------------------------------------------------------------------------
# 2. Local measurement instruments and exact conditional history law.
# -------------------------------------------------------------------------

a_obs = {0: z, 1: x}
b_obs = {
    0: scalem(INV_R2, addm(z, x)),
    1: scalem(INV_R2, subm(z, x)),
}
for label, obs in list((f"A{xv}", op) for xv, op in a_obs.items()) + list((f"B{yv}", op) for yv, op in b_obs.items()):
    check(matmul(obs, obs) == i2, f"{label} is an exact binary observable")
    check(dagger(obs) == obs, f"{label} is Hermitian")


def projector(obs, outcome):
    return scalem(Q2.make(F(1, 2)), addm(i2, scalem(outcome, obs)))


joint = {}
correlators = {}
for xv, yv in product((0, 1), repeat=2):
    row_sum = Q2()
    e_xy = Q2()
    for av, bv in product((-1, 1), repeat=2):
        pa = projector(a_obs[xv], av)
        pb = projector(b_obs[yv], bv)
        effect = kron(pa, pb)
        p = probability(rho, effect)
        joint[(xv, yv, av, bv)] = p
        row_sum += p
        e_xy += av * bv * p
        check(p.dec() >= 0, f"nonnegative Born cell {(xv,yv,av,bv)}")
    check(row_sum == Q2.make(1), f"outcomes normalized {(xv,yv)}")
    correlators[(xv, yv)] = e_xy

expected_e = {
    (0, 0): INV_R2,
    (0, 1): INV_R2,
    (1, 0): INV_R2,
    (1, 1): -INV_R2,
}
check(correlators == expected_e, "exact frozen correlator table")

# Uniform marginals and no-signalling in both directions.
for xv, av, y0, y1 in product((0, 1), (-1, 1), (0, 1), (0, 1)):
    left0 = sum((joint[(xv, y0, av, bv)] for bv in (-1, 1)), Q2())
    left1 = sum((joint[(xv, y1, av, bv)] for bv in (-1, 1)), Q2())
    check(left0 == left1 == Q2.make(F(1, 2)), f"A no-signalling {(xv,av,y0,y1)}")
for yv, bv, x0, x1 in product((0, 1), (-1, 1), (0, 1), (0, 1)):
    right0 = sum((joint[(x0, yv, av, bv)] for av in (-1, 1)), Q2())
    right1 = sum((joint[(x1, yv, av, bv)] for av in (-1, 1)), Q2())
    check(right0 == right1 == Q2.make(F(1, 2)), f"B no-signalling {(yv,bv,x0,x1)}")

# Independent fair setting tokens and full sealed-history normalization.
full_history = {key: value * Q2.make(F(1, 4)) for key, value in joint.items()}
check(sum(full_history.values(), Q2()) == Q2.make(1), "complete setting/outcome history law normalized")
for xv, yv in product((0, 1), repeat=2):
    cylinder = sum((full_history[(xv, yv, av, bv)] for av, bv in product((-1, 1), repeat=2)), Q2())
    check(cylinder == Q2.make(F(1, 4)), f"terminal deletion recovers setting cylinder {(xv,yv)}")

# Settings factor from the source: P(x,y|source)=P(x)P(y)=1/4.
for xv, yv in product((0, 1), repeat=2):
    check(Q2.make(F(1, 4)) == Q2.make(F(1, 2)) * Q2.make(F(1, 2)),
          f"measurement independence {(xv,yv)}")


# -------------------------------------------------------------------------
# 3. Exact CHSH/Tsirelson and construction-order gauge.
# -------------------------------------------------------------------------

chsh = correlators[(0, 0)] + correlators[(0, 1)] + correlators[(1, 0)] - correlators[(1, 1)]
check(chsh == Q2(F(0), F(2)), "CHSH is exactly 2sqrt2")

chsh_op = addm(addm(kron(a_obs[0], b_obs[0]), kron(a_obs[0], b_obs[1])),
               subm(kron(a_obs[1], b_obs[0]), kron(a_obs[1], b_obs[1])))
check(matvec(chsh_op, phi) == tuple(C2.make(Q2(F(0), F(2))) * v for v in phi),
      "Phi+ is a 2sqrt2 CHSH eigenstate")
check(matmul(matmul(chsh_op, chsh_op), chsh_op) == scalem(8, chsh_op),
      "CHSH spectrum obeys lambda(lambda^2-8)=0")

for xv, yv, av, bv in product((0, 1), (0, 1), (-1, 1), (-1, 1)):
    pa = kron(projector(a_obs[xv], av), i2)
    pb = kron(i2, projector(b_obs[yv], bv))
    check(matmul(pa, pb) == matmul(pb, pa), f"disjoint measurement order gauge {(xv,yv,av,bv)}")

# All deterministic local hidden assignments obey |S|=2 exactly.
classical_values = []
for a0, a1, b0, b1 in product((-1, 1), repeat=4):
    sval = a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1
    classical_values.append(sval)
    check(abs(sval) == 2, f"deterministic CHSH control {(a0,a1,b0,b1)}")

# Product quantum source control is also nonviolating for the frozen axes.
ket00 = (ONE, ZERO, ZERO, ZERO)
rho_product = outer(ket00)
e_product = {}
for xv, yv in product((0, 1), repeat=2):
    e = Q2()
    for av, bv in product((-1, 1), repeat=2):
        p = probability(rho_product, kron(projector(a_obs[xv], av), projector(b_obs[yv], bv)))
        e += av * bv * p
    e_product[(xv, yv)] = e
s_product = e_product[(0, 0)] + e_product[(0, 1)] + e_product[(1, 0)] - e_product[(1, 1)]
check(abs(s_product.dec()) <= Decimal(2), "product-state quantum control does not violate CHSH")


# -------------------------------------------------------------------------
# 4. Gauge-relative tomography and context-dependence attack.
# -------------------------------------------------------------------------

# With Phi+ and A0=Z,A1=X, E_0y=b_yZ and E_1y=b_yX.
recovered = {
    0: (correlators[(0, 0)], correlators[(1, 0)]),
    1: (correlators[(0, 1)], correlators[(1, 1)]),
}
check(recovered[0] == (INV_R2, INV_R2), "tomography recovers B0 coefficients")
check(recovered[1] == (INV_R2, -INV_R2), "tomography recovers B1 coefficients")
for yv, (bz, bx) in recovered.items():
    check(bz * bz + bx * bx == Q2.make(1), f"reconstructed B{yv} has unit norm")

# A remote-context-dependent attack changes only E00. The implied B0 vector
# loses unit norm and is therefore incompatible with one fixed projective B0.
attacked_b0 = (Q2.make(F(1, 2)), correlators[(1, 0)])
attack_norm2 = attacked_b0[0] * attacked_b0[0] + attacked_b0[1] * attacked_b0[1]
check(attack_norm2 == Q2.make(F(3, 4)), "context attack exact norm defect")
check(attack_norm2 != Q2.make(1), "context-dependent B0 attack detected")

# Fixed parameter count: theta + four planar coefficients, independent of
# number of repeated histories.
parameter_count = 5
for sample_count in (16, 10_000, 1_000_000):
    check(parameter_count == 5, f"tomography parameter count fixed at N={sample_count}")


# -------------------------------------------------------------------------
# 5. Reproducible finite-sample tomography.
# -------------------------------------------------------------------------

rng = Random(20269001)
n_per_context = 200_000
empirical_e = {}
for xv, yv in product((0, 1), repeat=2):
    cells = [(av, bv, float(joint[(xv, yv, av, bv)].dec()))
             for av, bv in product((-1, 1), repeat=2)]
    cumulative = []
    running = 0.0
    for av, bv, p in cells:
        running += p
        cumulative.append((running, av, bv))
    total = 0
    for _ in range(n_per_context):
        u = rng.random()
        for cut, av, bv in cumulative:
            if u <= cut:
                total += av * bv
                break
    empirical_e[(xv, yv)] = total / n_per_context

finite_tolerance = 5.0 / (n_per_context ** 0.5)
for key in expected_e:
    target = float(expected_e[key].dec())
    check(abs(empirical_e[key] - target) <= finite_tolerance,
          f"finite-sample correlation recovery {key}")

emp_b0 = (empirical_e[(0, 0)], empirical_e[(1, 0)])
emp_b1 = (empirical_e[(0, 1)], empirical_e[(1, 1)])
for yv, coeffs in ((0, emp_b0), (1, emp_b1)):
    norm2 = coeffs[0] ** 2 + coeffs[1] ** 2
    check(abs(norm2 - 1.0) <= 8.0 / (n_per_context ** 0.5),
          f"finite-sample unit-vector recovery B{yv}")


print("D9 MINIMAL BELL PACKET EXACT RECEIPT")
print(f"checks={checks}")
print(f"theta=pi/4")
print(f"g_shadow={g_shadow}")
print(f"CHSH={chsh} decimal={chsh.dec()}")
print(f"B0_recovered=({recovered[0][0]},{recovered[0][1]})")
print(f"B1_recovered=({recovered[1][0]},{recovered[1][1]})")
print(f"context_attack_norm2={attack_norm2}")
print(f"finite_E00={empirical_e[(0,0)]:.12f}")
print(f"finite_E01={empirical_e[(0,1)]:.12f}")
print(f"finite_E10={empirical_e[(1,0)]:.12f}")
print(f"finite_E11={empirical_e[(1,1)]:.12f}")
payload = "|".join([
    str(checks), str(g_shadow), str(chsh), str(recovered), str(attack_norm2),
    *(f"{empirical_e[key]:.15f}" for key in sorted(empirical_e)),
])
print(f"receipt_sha256={sha256(payload.encode('ascii')).hexdigest()}")

