#!/usr/bin/env python3
"""Dependency-free exact D13 finite-kernel nonselection witness.

Arithmetic is in Q(sqrt(2), i), copied into this self-contained receipt rather
than relying on an undeclared SymPy environment.  The theorem is deliberately
narrow: it refutes unique selection of a local unitary interaction kernel on a
fixed operational diamond interval.  It does not prove a universal diamond
category, Lorentz covariance, or a fundamental action for nature.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "v10" / "data" / "d13-finite-kernel-no-go-exact.json"
EXPECTED_CHECKS = 21
EXPECTED_SEMANTIC_SHA256 = "4eb19b0eb34bdc9cd910029cb3d4c22bb47d8d847e0fe12353a7b5eac69f2852"
CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:03d}: {label}")


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
        return Q2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Q2.make(other)
        den = other.a * other.a - 2 * other.b * other.b
        if den == 0:
            raise ZeroDivisionError
        return Q2(
            (self.a * other.a - 2 * self.b * other.b) / den,
            (self.b * other.a - self.a * other.b) / den,
        )

    def text(self):
        return f"({self.a})+({self.b})*sqrt(2)"


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
        return C2(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = C2.make(other)
        den = other.re * other.re + other.im * other.im
        if den == Q2():
            raise ZeroDivisionError
        return C2(
            (self.re * other.re + self.im * other.im) / den,
            (self.im * other.re - self.re * other.im) / den,
        )

    def conj(self):
        return C2(self.re, -self.im)

    def norm2(self):
        return self.re * self.re + self.im * self.im

    def text(self):
        return f"{self.re.text()}+i*{self.im.text()}"


ZERO, ONE = C2(), C2.make(1)
HALF = C2.make(F(1, 2))
II = C2(Q2(), Q2.make(1))
ROOT_HALF = C2.make(Q2(F(0), F(1, 2)))


def matrix(rows):
    return tuple(tuple(C2.make(x) for x in row) for row in rows)


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def dagger(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a))) for i in range(len(a[0])))


def mul(a, b):
    bt = tuple(zip(*b))
    return tuple(
        tuple(sum((x * y for x, y in zip(row, col)), ZERO) for col in bt)
        for row in a
    )


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(x, a):
    return tuple(tuple(C2.make(x) * y for y in row) for row in a)


def mv(a, v):
    return tuple(sum((x * y for x, y in zip(row, v)), ZERO) for row in a)


def inner(v, w):
    return sum((x.conj() * y for x, y in zip(v, w)), ZERO)


def outer(v, w):
    return tuple(tuple(x * y.conj() for y in w) for x in v)


def trace(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def kron(a, b):
    return tuple(tuple(x * y for x in ar for y in br) for ar in a for br in b)


def basis(n, j):
    return tuple(ONE if i == j else ZERO for i in range(n))


def projector(n, j):
    v = basis(n, j)
    return outer(v, v)


def iswap(cosine, sine):
    c, s = C2.make(cosine), II * sine
    return matrix(((1, 0, 0, 0), (0, c, s, 0), (0, s, c, 0), (0, 0, 0, 1)))


def reduced_second_qubit(rho):
    # Basis index = 2*a+b.  Trace over a.
    return tuple(
        tuple(sum((rho[2 * a + b][2 * a + bp] for a in range(2)), ZERO) for bp in range(2))
        for b in range(2)
    )


def sealed_vector(system_vector):
    # |j> -> |j>_system |j>_record |live=1>_collar.
    out = [ZERO] * 32
    for j, amp in enumerate(system_vector):
        out[(j * 4 + j) * 2 + 1] = amp
    return tuple(out)


def sealed_record_distribution(v):
    return tuple(
        sum((v[(s * 4 + r) * 2 + c].norm2() for s in range(4) for c in range(2)), Q2())
        for r in range(4)
    )


def sealed_collar_distribution(v):
    return tuple(
        sum((v[(s * 4 + r) * 2 + c].norm2() for s in range(4) for r in range(4)), Q2())
        for c in range(2)
    )


def apply_system_to_sealed(u, v):
    out = [ZERO] * 32
    for so in range(4):
        for si in range(4):
            for r in range(4):
                for c in range(2):
                    out[(so * 4 + r) * 2 + c] += u[so][si] * v[(si * 4 + r) * 2 + c]
    return tuple(out)


def repeat_read_vector(v):
    # Append a fresh four-level readout in |0>, then apply controlled modular
    # addition from the sealed record: |r>|q> -> |r>|q+r mod 4>.
    out = [ZERO] * (32 * 4)
    for old_index, amp in enumerate(v):
        record = (old_index // 2) % 4
        out[old_index * 4 + record] = amp
    return tuple(out)


def repeat_read_joint(v):
    out = [[Q2() for _ in range(4)] for _ in range(4)]
    for old_index in range(32):
        record = (old_index // 2) % 4
        for reread in range(4):
            out[record][reread] += v[old_index * 4 + reread].norm2()
    return tuple(tuple(row) for row in out)


def memory_copy_unitary():
    # Four bits ordered X,M,Y,Z.  Apply CNOT X->M and then CNOT M->Z.
    rows = [[0 for _ in range(16)] for _ in range(16)]
    for x in range(2):
        for m in range(2):
            for y in range(2):
                for zbit in range(2):
                    source = ((x * 2 + m) * 2 + y) * 2 + zbit
                    m1 = m ^ x
                    z1 = zbit ^ m1
                    target = ((x * 2 + m1) * 2 + y) * 2 + z1
                    rows[target][source] = 1
    return matrix(rows)


def main():
    i2, i4 = eye(2), eye(4)
    h = matrix(((ROOT_HALF, ROOT_HALF), (ROOT_HALF, -ROOT_HALF)))
    z = matrix(((1, 0), (0, -1)))
    phase = matrix(((1, 0), (0, II)))
    swap = matrix(((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)))
    number = matrix(((0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 2)))
    x_ex = matrix(((0, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 0)))
    uq = iswap(ROOT_HALF, ROOT_HALF)
    uh = iswap(0, 1)

    check(mul(dagger(uq), uq) == i4 and mul(dagger(uh), uh) == i4,
          "both fixed-interval kernels are unitary")
    check(mul(x_ex, number) == mul(number, x_ex) and mul(x_ex, swap) == mul(swap, x_ex),
          "generator respects excitation number and exchange")
    check(mul(uq, uq) == uh, "shared-screen matrix composition is exact")
    check(mul(kron(uq, i4), kron(i4, uh)) == mul(kron(i4, uh), kron(uq, i4)),
          "one disjoint tensor-factor schedule cell commutes")
    z_first = kron(z, i2)
    check(mul(uq, z_first) != mul(z_first, uq), "one overlap control is order-sensitive")

    ket10 = basis(4, 2)
    rho = outer(ket10, ket10)
    effect10 = projector(4, 2)
    gin, gout = kron(h, phase), kron(phase, h)
    kp = mul(mul(gout, uq), dagger(gin))
    rhop = mul(mul(gin, rho), dagger(gin))
    ep = mul(mul(gout, effect10), dagger(gout))
    p = trace(mul(effect10, mul(mul(uq, rho), dagger(uq))))
    pp = trace(mul(ep, mul(mul(kp, rhop), dagger(kp))))
    check(p == pp, "independent input/output unitary frame covariance is exact")

    evolved = mv(uq, ket10)
    sealed = sealed_vector(evolved)
    columns = tuple(sealed_vector(basis(4, j)) for j in range(4))
    check(all(inner(columns[j], columns[k]) == (ONE if j == k else ZERO)
              for j in range(4) for k in range(4)), "seal-and-birth map is an isometry")
    record_dist = sealed_record_distribution(sealed)
    check(record_dist == (Q2(), Q2(F(1, 2)), Q2(F(1, 2)), Q2()),
          "orthogonal record branches are exactly exclusive")
    check(sum(record_dist, Q2()) == Q2.make(1), "record probabilities normalize")

    ket01 = basis(4, 1)
    plus_plus = tuple(ROOT_HALF * ROOT_HALF for _ in range(4))
    qpsi, hpsi = mv(uq, ket01), mv(uh, plus_plus)
    qdet = qpsi[0] * qpsi[3] - qpsi[1] * qpsi[2]
    hdet = hpsi[0] * hpsi[3] - hpsi[1] * hpsi[2]
    check(qdet.norm2() == Q2(F(1, 4)) and hdet.norm2() == Q2(F(1, 4)),
          "both kernels have an exact maximal-entanglement witness")
    ph = trace(mul(effect10, mul(mul(uh, rho), dagger(uh))))
    check(p == HALF and ph == ZERO,
          "fixed operational interval gives inequivalent probabilities one-half and zero")

    # Interference: H.H returns |0>; dephasing between the two H gates gives 1/2.
    ket0 = basis(2, 0)
    coherent = mv(h, mv(h, ket0))
    coherent_p0 = coherent[0].norm2()
    after_h = mv(h, ket0)
    incoherent_p0 = sum((after_h[j].norm2() * h[0][j].norm2() for j in range(2)), Q2())
    check(coherent_p0 == Q2.make(1) and incoherent_p0 == Q2(F(1, 2)),
          "coherent path sum differs exactly from inserted-record probability sum")

    # No signalling cell: a local unitary on A leaves B's reduced state unchanged.
    bell = (ROOT_HALF, ZERO, ZERO, ROOT_HALF)
    bell_rho = outer(bell, bell)
    local_h = kron(h, i2)
    bell_after = mul(mul(local_h, bell_rho), dagger(local_h))
    check(reduced_second_qubit(bell_rho) == reduced_second_qubit(bell_after),
          "one entangled disjoint-laboratory no-signalling cell passes")

    # Open-system projective dephasing channel.
    p0, p1 = projector(2, 0), projector(2, 1)
    check(add(mul(dagger(p0), p0), mul(dagger(p1), p1)) == i2,
          "Kraus completeness for the exact dephasing limit")
    plus = (ROOT_HALF, ROOT_HALF)
    plus_rho = outer(plus, plus)
    dephased = add(mul(mul(p0, plus_rho), p0), mul(mul(p1, plus_rho), p1))
    check(trace(dephased) == ONE and dephased == matrix(((F(1, 2), 0), (0, F(1, 2)))),
          "open-system limit is normalized and positive in its eigenbasis")
    check(p == HALF and C2.make(record_dist[2]) == p and p * p != p,
          "instrument trace equals sealed branch mass with no second Born weighting")

    # Sealed record is inaccessible to later licensed system-only kernels.
    later = apply_system_to_sealed(kron(h, i2), sealed)
    check(sealed_record_distribution(later) == record_dist,
          "sealed record distribution persists under later system-only interaction")
    reread = repeat_read_joint(repeat_read_vector(later))
    check(all(reread[r][q] == (record_dist[r] if r == q else Q2())
              for r in range(4) for q in range(4)),
          "fresh controlled repeat read agrees with the sealed record exactly")
    check(sealed_collar_distribution(sealed) == (Q2(), Q2.make(1)),
          "every internal seal emits one declared live output collar")

    # Visible non-Markov witness executed as an exact reversible circuit.
    umem = memory_copy_unitary()
    rho_mem_in = scale(HALF, add(outer(basis(16, 0), basis(16, 0)),
                                 outer(basis(16, 8), basis(16, 8))))
    rho_mem_out = mul(mul(umem, rho_mem_in), dagger(umem))
    histories = {}
    for x in range(2):
        for y in range(2):
            for zbit in range(2):
                histories[(x, y, zbit)] = sum(
                    (rho_mem_out[((x * 2 + m) * 2 + y) * 2 + zbit]
                                [((x * 2 + m) * 2 + y) * 2 + zbit]
                     for m in range(2)), ZERO)
    den1 = sum((mass for (x, y, _), mass in histories.items() if x == 1 and y == 0), ZERO)
    den0 = sum((mass for (x, y, _), mass in histories.items() if x == 0 and y == 0), ZERO)
    p_z1_y0_x1 = histories[(1, 0, 1)] / den1
    p_z1_y0_x0 = histories[(0, 0, 1)] / den0
    check(mul(dagger(umem), umem) == eye(16)
          and p_z1_y0_x1 == ONE and p_z1_y0_x0 == ZERO,
          "executed reversible CNOT memory circuit yields exact visible non-Markov history")

    check(CHECKS + 1 == EXPECTED_CHECKS, "pre-final check count is frozen")
    if CHECKS != EXPECTED_CHECKS:
        raise AssertionError((CHECKS, EXPECTED_CHECKS))

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    semantic = {
        "schema": "d13-finite-kernel-no-go-exact-v2",
        "arithmetic": "Python standard library Q(sqrt(2),i); no external dependencies",
        "scope": "fixed operational diamond interval; finite local unitary kernels",
        "checks_passed": CHECKS,
        "predictions": {"theta_pi_over_4": "1/2", "theta_pi_over_2": "0"},
        "visible_memory_conditionals": {"P(z=1|y=0,x=1)": "1", "P(z=1|y=0,x=0)": "0"},
        "verdict": "FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED",
    }
    semantic_payload = json.dumps(semantic, sort_keys=True, separators=(",", ":"))
    semantic_hash = sha256(semantic_payload.encode()).hexdigest()
    if EXPECTED_SEMANTIC_SHA256 != "TO_BE_FROZEN" and semantic_hash != EXPECTED_SEMANTIC_SHA256:
        raise AssertionError((semantic_hash, EXPECTED_SEMANTIC_SHA256))
    packet = dict(semantic)
    packet["semantic_sha256"] = semantic_hash
    packet["source_sha256"] = source_hash
    payload = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    OUT.write_text(payload, encoding="utf-8")
    print(f"CHECKS PASSED: {CHECKS}/{EXPECTED_CHECKS}")
    print(f"SEMANTIC SHA256: {semantic_hash}")
    print(f"SOURCE SHA256: {source_hash}")
    print("VERDICT: FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED")


if __name__ == "__main__":
    main()
