#!/usr/bin/env python3
"""
Paper 27 receipt: linear-window theorem fork.

The exact P_8 likelihood receipt points toward washout for width-2 linear
jitter, but a direct coupling of the marked coordinate ranks to iid ranks is
too strong.  This receipt records the theorem-shaped facts:

  1. The coordinate-marked rank process has a positive sibling bracket B(c)
     for every finite linear mixing ratio c.  Therefore marked-rank total
     variation/coupling to iid ranks is the wrong proof target.

  2. The sibling mass is sparse in unrooted order statistics.  A uniformly
     sampled k-record induced suborder sees any hidden sibling collision with
     probability at most binom(k,2)(w-1)/(N-1).  Thus every k_N=o(sqrt(N))
     unrooted induced-suborder test is asymptotically blind, after the
     no-collision rank-kernel convergence.

  3. The first possible accumulation scale is k ~ a sqrt(N), with expected
     hidden sibling collisions a^2(w-1)/2.  Any remaining order-only witness
     must therefore be sqrt-scale, global, or a genuinely unlabeled
     likelihood/selected-class effect.

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
    """Antiderivative of P(E <= z), E uniform[-c,c]."""
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
    """B(c)=Var(E[F_c(S+E)|S]) for two siblings sharing S."""
    c = mp.mpf(c)
    total = mp.mpf(0)
    points = split_points(c)
    for left, right in zip(points[:-1], points[1:]):
        total += mp.quad(lambda s: (conditional_rank_mean(s, c) - mp.mpf("0.5")) ** 2, [left, right])
    return +total


def marked_rank_nvar(width, c):
    return mp.mpf(1) / 12 + (mp.mpf(width) - 1) * sibling_bracket(c)


def sibling_pair_fraction(N, width):
    return (mp.mpf(width) - 1) / (mp.mpf(N) - 1)


def collision_bound(N, k, width):
    return mp.binomial(k, 2) * sibling_pair_fraction(N, width)


def sqrt_collision_mean(a, width):
    return (mp.mpf(a) ** 2) * (mp.mpf(width) - 1) / 2


print("=" * 80)
print("Paper 27 linear-window theorem-fork receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n(1) Marked coordinate sibling bracket")
cs = [mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4"), mp.mpf("8"), mp.mpf("16")]
bracket_rows = []
for c in cs:
    b = sibling_bracket(c)
    nvar_w2 = marked_rank_nvar(2, c)
    nvar_w4 = marked_rank_nvar(4, c)
    bracket_rows.append((c, b, nvar_w2, nvar_w4))
    print(
        f"c={fmt(c, 8)} B(c)={fmt(b, 40)} "
        f"NVar_w2={fmt(nvar_w2, 40)} NVar_w4={fmt(nvar_w4, 40)}"
    )

print("\n(2) Unrooted hidden sibling dilution")
for width in [2, 4, 8]:
    values = []
    for exponent in [4, 6, 8, 10]:
        N = mp.mpf(10) ** exponent
        values.append((N, sibling_pair_fraction(N, width)))
    print(f"width={width}: " + ", ".join(f"N=1e{int(mp.log10(N))}: {fmt(v, 12)}" for N, v in values))

print("\n(3) Growing-window collision bounds")
width = 2
Ns = [mp.mpf(10) ** p for p in [4, 5, 6, 7, 8]]
betas = [mp.mpf("0.25"), mp.mpf("0.40"), mp.mpf("0.49"), mp.mpf("0.50"), mp.mpf("0.60")]
table = {}
for beta in betas:
    rows = []
    print(f"\nbeta={fmt(beta, 6)}")
    for N in Ns:
        k = mp.floor(N**beta)
        bound = collision_bound(N, k, width)
        rows.append((N, k, bound))
        print(f"N={fmt(N, 8)} k={fmt(k, 12)} collision<={fmt(bound, 18)}")
    table[beta] = rows

print("\n(4) Square-root accumulation scale")
for width in [2, 4, 8]:
    for a in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")]:
        print(f"width={width} a={fmt(a, 4)} mean_collisions={fmt(sqrt_collision_mean(a, width), 18)}")

b_values = [row[1] for row in bracket_rows]
check(
    "Finite linear mixing has positive marked coordinate Palm bracket",
    all(b > 0 for b in b_values),
    f"B(1)={fmt(next(b for c, b, *_ in bracket_rows if c == 1), 18)}",
)
check(
    "Strong mixing reduces but does not erase finite-c marked residue",
    all(b_values[i] > b_values[i + 1] for i in range(2, len(b_values) - 1))
    and b_values[-1] > 0,
    f"B(16)={fmt(b_values[-1], 18)}",
)
check(
    "Direct marked-rank iid coupling is too strong as a proof of order washout",
    marked_rank_nvar(2, 1) - mp.mpf(1) / 12 > mp.mpf("1e-4"),
    f"NVar_w2(c=1)-iid={fmt(marked_rank_nvar(2, 1) - mp.mpf(1)/12, 18)}",
)
check(
    "Unrooted hidden sibling pair mass is O(1/N)",
    sibling_pair_fraction(mp.mpf(10) ** 8, 2) < mp.mpf("2e-8")
    and sibling_pair_fraction(mp.mpf(10) ** 8, 8) < mp.mpf("1e-7"),
    f"w2={fmt(sibling_pair_fraction(mp.mpf(10)**8, 2), 18)} "
    f"w8={fmt(sibling_pair_fraction(mp.mpf(10)**8, 8), 18)}",
)
check(
    "Sub-sqrt induced-suborder collision bounds decrease across tested N",
    all(
        all(table[beta][i][2] > table[beta][i + 1][2] for i in range(len(Ns) - 1))
        for beta in [mp.mpf("0.25"), mp.mpf("0.40"), mp.mpf("0.49")]
    ),
    f"beta=.49 final={fmt(table[mp.mpf('0.49')][-1][2], 18)}",
)
check(
    "Critical and supercritical windows are not covered by the local washout bound",
    table[mp.mpf("0.50")][-1][2] > mp.mpf("0.49")
    and table[mp.mpf("0.60")][-1][2] > table[mp.mpf("0.60")][0][2],
    f"critical_final={fmt(table[mp.mpf('0.50')][-1][2], 18)} "
    f"super_final={fmt(table[mp.mpf('0.60')][-1][2], 18)}",
)
check(
    "Square-root samples have nonzero limiting hidden-collision mass",
    sqrt_collision_mean(1, 2) == mp.mpf("0.5") and sqrt_collision_mean(1, 4) == mp.mpf("1.5"),
    f"w2,a1={fmt(sqrt_collision_mean(1, 2), 18)} w4,a1={fmt(sqrt_collision_mean(1, 4), 18)}",
)

print("\n=== Consequence ===")
print("The theorem path splits.  A direct marked-rank coupling to iid ranks")
print("is false at finite linear mixing ratio because sibling rank brackets")
print("remain positive.  But that residue is sparse in unrooted order data:")
print("sub-sqrt induced-suborder tests miss it with high probability.  Any")
print("remaining order-only witness must live at sqrt scale or above, or in")
print("the exact unlabeled likelihood/selected-class denominator.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
