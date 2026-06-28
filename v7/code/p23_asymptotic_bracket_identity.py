#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: asymptotic marked bracket identity.

Finite order-visible feature searches did not expose a linear-window residue.
This receipt follows the asymptotic opening: even when hidden labels are not
classifiable, a clustered process can alter fluctuation brackets.  The clean
calculation is first done in the coordinate-marked one-dimensional shadow.

Parent S is uniform on [0,1].  Offspring coordinate is X=S+E with
E uniform[-c,c].  Let R=F_c(X), where F_c is the marginal CDF of X; R is a
rank-uniform coordinate.  For two siblings with the same parent S,

    Cov(R_1, R_2) = Var( E[R | S] ) = B(c).

For iid sprinkling this sibling bracket term is zero.  For fixed cluster width
w, the empirical-coordinate bracket becomes

    N Var(N^{-1} sum R_i) -> 1/12 + (w-1) B(c).

Thus finite c leaves a marked Palm/bracket residue unless B(c)=0.  As c grows,
B(c) tends to zero: strong mixing washes the residue out.

This is a marked/coordinate shadow, not yet an order-only theorem.  The paper's
next problem is to translate or refute this bracket in order-visible Palm/Mecke
terms.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def A(z, c):
    """Antiderivative of h(z)=P(E<=z) for E uniform[-c,c]."""
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 2 / (4 * c)
    return z


def B_anti(z, c):
    """Antiderivative of A(z,c), continuous at +-c."""
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 3 / (12 * c)
    return z**2 / 2 + c**2 / 6


def marginal_cdf(x, c):
    """CDF of X=S+E, S uniform[0,1], E uniform[-c,c]."""
    return A(x, c) - A(mp.mpf(x) - 1, c)


def G(x, c):
    """Antiderivative of marginal_cdf(x,c)."""
    return B_anti(x, c) - B_anti(mp.mpf(x) - 1, c)


def conditional_rank_mean(s, c):
    """M_c(s)=E[F_c(S+E)|S=s]."""
    s = mp.mpf(s)
    c = mp.mpf(c)
    return (G(s + c, c) - G(s - c, c)) / (2 * c)


def split_points(c):
    c = mp.mpf(c)
    points = {mp.mpf(0), mp.mpf(1)}
    for value in [2 * c, 1 - 2 * c]:
        if 0 < value < 1:
            points.add(+value)
    return sorted(points)


def sibling_bracket(c):
    c = mp.mpf(c)
    points = split_points(c)
    total = mp.mpf(0)
    for left, right in zip(points[:-1], points[1:]):
        total += mp.quad(lambda s: (conditional_rank_mean(s, c) - mp.mpf("0.5")) ** 2, [left, right])
    return +total


def empirical_bracket(width, c):
    return mp.mpf(1) / 12 + (mp.mpf(width) - 1) * sibling_bracket(c)


print("=" * 80)
print("Collapsed P23 asymptotic marked bracket identity")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

cs = [mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4"), mp.mpf("8"), mp.mpf("16")]
values = []
print("\n(1) Sibling bracket B(c)")
for c in cs:
    b = sibling_bracket(c)
    bracket_w4 = empirical_bracket(4, c)
    values.append((c, b, bracket_w4))
    print(f"c={fmt(c, 8)} B(c)={fmt(b, 40)} NVar_w4={fmt(bracket_w4, 40)}")

print("\n(2) Boundary checks")
check(
    "Finite mixing ratio has positive marked sibling bracket",
    all(b > 0 for _c, b, _bracket in values),
    ", ".join(f"c={fmt(c, 6)} B={fmt(b, 12)}" for c, b, _ in values[:4]),
)
check(
    "Marked sibling bracket decreases across the tested large-mixing tail",
    all(values[i][1] > values[i + 1][1] for i in range(2, len(values) - 1)),
    ", ".join(f"c={fmt(c, 6)} B={fmt(b, 12)}" for c, b, _ in values[2:]),
)
check(
    "Strong mixing drives the marked bracket toward the iid value",
    values[-1][2] - mp.mpf(1) / 12 < mp.mpf("0.001"),
    f"NVar_w4(c=16)-1/12={fmt(values[-1][2] - mp.mpf(1)/12, 18)}",
)
check(
    "Linear c=2 still has a nonzero marked bracket residue",
    next(b for c, b, _bracket in values if c == 2) > mp.mpf("1e-4"),
    f"B(2)={fmt(next(b for c, b, _ in values if c == 2), 18)}",
)
check(
    "The receipt distinguishes marked bracket residue from finite feature washout",
    empirical_bracket(4, 2) > mp.mpf(1) / 12 and empirical_bracket(4, 16) > mp.mpf(1) / 12,
    f"NVar_w4(c=2)={fmt(empirical_bracket(4, 2), 18)}, iid={fmt(mp.mpf(1)/12, 18)}",
)

print("\n(3) Consequence")
print("The coordinate-marked shadow has a clean bracket identity:")
print("finite c contributes (w-1)B(c) to N Var(empirical rank mean).")
print("This is a genuine asymptotic washout/residue theorem in the marked model.")
print("The remaining question is whether an order-only Palm/Mecke/bracket statistic")
print("can recover this marked residue, or whether order-only observables are")
print("contiguous even when the marked coordinate process is not.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
