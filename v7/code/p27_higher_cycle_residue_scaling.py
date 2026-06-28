#!/usr/bin/env python3
"""
Paper 27 receipt: higher-cycle residue scaling.

The previous receipt proved exact two-factor nonshared neutrality and found a
small nonzero three-factor cycle residue.  This receipt pushes the same labeled
permutation model to disjoint r-factor moments for r=2..5:

    rho_r = E[g_1 ... g_r],

where the domain edges are disjoint and

    g_e(pi) = N(N-1) delta(pi(a), pi(b)).

The moments are computed by a subset dynamic program over disjoint ordered
image-pairs.  For a width-2 matching with M=N/2 hidden pairs, the reported
aggregate audit is

    binom(M,r) rho_r^2.

This is not a full polymer/cluster-expansion proof.  It is a hostile finite
audit of whether higher cycles begin to grow coherently after the exact
two-factor cancellation.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict
import math
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


def A_anti(z, c):
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 2 / (4 * c)
    return z


def marginal_cdf(x, c):
    return A_anti(x, c) - A_anti(mp.mpf(x) - 1, c)


def legendre_nodes(n, left, right):
    xs, ws = mp.gauss_quadrature(n, "legendre")
    mid = (mp.mpf(left) + mp.mpf(right)) / 2
    half = (mp.mpf(right) - mp.mpf(left)) / 2
    return [(mid + half * xs[i], half * ws[i]) for i in range(n)]


def clamp_unit(x):
    if x < 0:
        return mp.mpf(0)
    if x > 1:
        return mp.mpf(1)
    return x


def rank_kernel_values(n, low, high):
    between = high - low
    above = 1 - high
    fact = mp.mpf(math.factorial(n - 2))
    out = []
    for a in range(n - 1):
        low_pow = low**a
        for b in range(a + 1, n):
            coeff = fact / (
                mp.mpf(math.factorial(a))
                * mp.mpf(math.factorial(b - a - 1))
                * mp.mpf(math.factorial(n - 1 - b))
            )
            value = coeff * low_pow * (between ** (b - a - 1)) * (above ** (n - 1 - b))
            out.append((a, b, value))
    return out


def q_axis_matrix(n, c, nodes):
    c = mp.mpf(c)
    s_nodes = legendre_nodes(nodes, 0, 1)
    e0_nodes = legendre_nodes(nodes, -c, c)
    e1_nodes = legendre_nodes(nodes + 1, -c, c)
    matrix = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    density_factor = 1 / (4 * c * c)
    for s, ws in s_nodes:
        for e0, we0 in e0_nodes:
            r0 = clamp_unit(marginal_cdf(s + e0, c))
            for e1, we1 in e1_nodes:
                r1 = clamp_unit(marginal_cdf(s + e1, c))
                weight = ws * we0 * we1 * density_factor
                if r0 < r1:
                    for a, b, value in rank_kernel_values(n, r0, r1):
                        matrix[a][b] += weight * value
                elif r1 < r0:
                    for b, a, value in rank_kernel_values(n, r1, r0):
                        matrix[a][b] += weight * value
    return matrix


def offdiag_sum(matrix):
    n = len(matrix)
    return mp.fsum(matrix[i][j] for i in range(n) for j in range(n) if i != j)


def sym_normalize_project(matrix):
    n = len(matrix)
    sym = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                sym[i][j] = (matrix[i][j] + matrix[j][i]) / 2
    total = offdiag_sum(sym)
    for i in range(n):
        for j in range(n):
            if i != j:
                sym[i][j] /= total

    m = mp.mpf(n) * (n - 1)
    u = 1 / m
    delta = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                delta[i][j] = sym[i][j] - u

    row = [mp.fsum(delta[i][j] for j in range(n) if i != j) for i in range(n)]
    total_row = mp.fsum(row)
    correction_constant = -total_row / ((n - 2) * (n - 1))
    corrected_delta = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                h = (row[i] + row[j]) / (n - 2) + correction_constant
                corrected_delta[i][j] = delta[i][j] - h

    row_after = [
        mp.fsum(corrected_delta[i][j] for j in range(n) if i != j)
        for i in range(n)
    ]
    return corrected_delta, max(abs(value) for value in row_after)


def axis_excess(delta):
    n = len(delta)
    return mp.mpf(n) * (n - 1) * mp.fsum(
        delta[i][j] ** 2 for i in range(n) for j in range(n) if i != j
    )


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


def pair_entries(delta):
    n = len(delta)
    scale = mp.mpf(n) * (n - 1)
    entries = []
    for i in range(n):
        for j in range(n):
            if i != j:
                entries.append(((1 << i) | (1 << j), scale * delta[i][j]))
    return entries


def disjoint_moments(delta, max_r):
    n = len(delta)
    max_possible = min(max_r, n // 2)
    entries = pair_entries(delta)
    dp = {0: mp.mpf(1)}
    out = {}
    for depth in range(1, max_possible + 1):
        next_dp = defaultdict(mp.mpf)
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                next_dp[used | mask] += value * edge_value
        total = mp.fsum(next_dp.values())
        out[depth] = total / falling(n, 2 * depth)
        dp = next_dp
    return out


def aggregate_matching_residue(n, r, moment):
    hidden_pairs = n // 2
    if hidden_pairs < r:
        return mp.mpf(0)
    return mp.mpf(math.comb(hidden_pairs, r)) * moment * moment


print("=" * 80)
print("Paper 27 higher-cycle residue scaling receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 16
sizes = [8, 10, 12]
cs = [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")]
max_r = 5
rows = {}
max_row_after = mp.mpf(0)

for c in cs:
    print("\n" + "=" * 80)
    print(f"c={fmt(c, 8)}")
    print("=" * 80)
    for n in sizes:
        raw = q_axis_matrix(n, c, nodes)
        delta, row_after = sym_normalize_project(raw)
        max_row_after = max(max_row_after, row_after)
        A = axis_excess(delta)
        moments = disjoint_moments(delta, max_r)
        print(f"\nN={n} A={fmt(A, 18)}")
        for r in range(2, max_r + 1):
            if r not in moments:
                continue
            moment = moments[r]
            aggregate = aggregate_matching_residue(n, r, moment)
            rows[(n, c, r)] = {
                "moment": moment,
                "aggregate": aggregate,
                "A": A,
            }
            print(
                f"  r={r} rho={fmt(moment, 18)} "
                f"agg=binom(M,r)rho^2={fmt(aggregate, 18)}"
            )

max_aggregate_by_r = {
    r: max(abs(row["aggregate"]) for key, row in rows.items() if key[2] == r)
    for r in range(2, max_r + 1)
}
max_aggregate_by_c = {
    c: max(abs(row["aggregate"]) for key, row in rows.items() if key[1] == c)
    for c in cs
}
hard_case_sequence = [max_aggregate_by_r[r] for r in range(2, max_r + 1)]

check(
    "Zero-row projection is enforced",
    max_row_after < mp.mpf("1e-80"),
    f"max_row_after={fmt(max_row_after, 18)}",
)
check(
    "Higher-cycle aggregate residues remain small in tested range",
    max(max_aggregate_by_r.values()) < mp.mpf("0.001"),
    ", ".join(f"r={r} maxAgg={fmt(max_aggregate_by_r[r], 12)}" for r in range(2, max_r + 1)),
)
check(
    "Hardest aggregate by r decreases after the two-factor term",
    all(hard_case_sequence[i] > hard_case_sequence[i + 1] for i in range(len(hard_case_sequence) - 1)),
    ", ".join(f"r={r} maxAgg={fmt(max_aggregate_by_r[r], 12)}" for r in range(2, max_r + 1)),
)
check(
    "Cycle aggregates fall rapidly with mixing c",
    max_aggregate_by_c[mp.mpf("4")] < max_aggregate_by_c[mp.mpf("2")]
    and max_aggregate_by_c[mp.mpf("2")] < max_aggregate_by_c[mp.mpf("1")]
    and max_aggregate_by_c[mp.mpf("1")] < max_aggregate_by_c[mp.mpf("0.5")],
    ", ".join(f"c={fmt(c,4)} maxAgg={fmt(max_aggregate_by_c[c], 12)}" for c in cs),
)
check(
    "No tested higher cycle beats the two-factor aggregate",
    all(max_aggregate_by_r[r] < max_aggregate_by_r[2] for r in range(3, max_r + 1)),
    f"r2={fmt(max_aggregate_by_r[2], 12)} "
    + ", ".join(f"r{r}={fmt(max_aggregate_by_r[r], 12)}" for r in range(3, max_r + 1)),
)

print("\n=== Consequence ===")
print("The finite higher-cycle audit does not find coherent growth after the")
print("two-factor term.  The r=3,4,5 aggregate residues are nonzero but smaller")
print("than the already tiny two-factor aggregate in the tested range, and all")
print("fall rapidly with c.  This supports a cluster-expansion style proof target:")
print("bound the r-cycle aggregate by a summable sequence controlled by A_N(c)")
print("and the falling-factorial geometry of disjoint images.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
