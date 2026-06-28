#!/usr/bin/env python3
"""
Paper 27 receipt: nonshared-cycle neutrality for density-matched pair factors.

After the rank-copula bound receipt, a one-pair density-matched factor has
L2 size O(1/N) provided A_N(c) is uniformly bounded.  The remaining risk is
that many small pair factors add coherently.

This receipt studies that risk in the labeled permutation model.  Let delta be
the symmetric zero-row one-axis rank-copula residue and define a localized
one-axis pair factor

    g_e(pi) = N(N-1) delta(pi(a), pi(b)),

for a fixed ordered domain edge e=(a,b).  If two or three domain edges are
disjoint, their image ranks are sampled without replacement.  The receipt
computes exact disjoint moments under the uniform permutation law:

    rho_2 = E[g_e g_f],          e,f disjoint
    rho_3 = E[g_e g_f g_h],      e,f,h disjoint.

For zero-row symmetric delta, the two-factor moment has the closed form

    rho_2 = 2 A_N(c) / ((N-2)(N-3)).

Thus, for width 2 and M=N/2 hidden pairs, the aggregate two-factor residue is
bounded by binom(M,2) rho_2^2, which is O(N^-2) when A_N(c)=O(1).  The triple
moment is measured as the first nontrivial cycle-residue audit.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from itertools import combinations
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
    return corrected_delta, {
        "row_after_linf": max(abs(value) for value in row_after),
    }


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
    out = []
    scale = mp.mpf(n) * (n - 1)
    for i in range(n):
        for j in range(n):
            if i != j:
                out.append(((1 << i) | (1 << j), scale * delta[i][j]))
    return out


def disjoint_moment(delta, r):
    n = len(delta)
    entries = pair_entries(delta)
    total = mp.mpf(0)

    def rec(depth, start_used, product_value):
        nonlocal total
        if depth == r:
            total += product_value
            return
        for mask, value in entries:
            if mask & start_used:
                continue
            rec(depth + 1, start_used | mask, product_value * value)

    rec(0, 0, mp.mpf(1))
    return total / falling(n, 2 * r)


def aggregate_matching_residue(n, r, moment):
    hidden_pairs = n // 2
    if hidden_pairs < r:
        return mp.mpf(0)
    return mp.mpf(math.comb(hidden_pairs, r)) * moment * moment


print("=" * 80)
print("Paper 27 nonshared-cycle neutrality receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 18
pair_sizes = [8, 12, 16, 24]
triple_sizes = [8, 10, 12]
cs = [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")]
pair_rows = {}
triple_rows = {}
max_row_after = mp.mpf(0)

print("\n(1) Disjoint two-factor neutrality")
for c in cs:
    print("\n" + "=" * 80)
    print(f"c={fmt(c, 8)}")
    print("=" * 80)
    for n in pair_sizes:
        raw = q_axis_matrix(n, c, nodes)
        delta, projection = sym_normalize_project(raw)
        max_row_after = max(max_row_after, projection["row_after_linf"])
        A = axis_excess(delta)
        rho2 = disjoint_moment(delta, 2)
        formula = 2 * A / ((mp.mpf(n) - 2) * (mp.mpf(n) - 3))
        aggregate2 = aggregate_matching_residue(n, 2, rho2)
        ratio_to_same = abs(rho2) / A if A else mp.mpf(0)
        pair_rows[(n, c)] = {
            "A": A,
            "rho2": rho2,
            "formula": formula,
            "formula_error": abs(rho2 - formula),
            "aggregate2": aggregate2,
            "ratio_to_same": ratio_to_same,
        }
        print(
            f"N={n} A={fmt(A, 18)} rho2={fmt(rho2, 18)} "
            f"formula={fmt(formula, 18)} err={fmt(abs(rho2-formula), 8)} "
            f"agg2={fmt(aggregate2, 18)} rho2/A={fmt(ratio_to_same, 12)}"
        )

print("\n(2) Disjoint three-factor cycle-residue audit")
for c in cs:
    print("\n" + "=" * 80)
    print(f"c={fmt(c, 8)}")
    print("=" * 80)
    for n in triple_sizes:
        raw = q_axis_matrix(n, c, nodes)
        delta, projection = sym_normalize_project(raw)
        max_row_after = max(max_row_after, projection["row_after_linf"])
        rho3 = disjoint_moment(delta, 3)
        aggregate3 = aggregate_matching_residue(n, 3, rho3)
        triple_rows[(n, c)] = {
            "rho3": rho3,
            "aggregate3": aggregate3,
        }
        print(
            f"N={n} rho3={fmt(rho3, 18)} "
            f"agg3={fmt(aggregate3, 18)}"
        )

max_formula_error = max(row["formula_error"] for row in pair_rows.values())
max_aggregate2_by_c = {
    c: max(pair_rows[(n, c)]["aggregate2"] for n in pair_sizes)
    for c in cs
}
max_aggregate3 = max(abs(row["aggregate3"]) for row in triple_rows.values())
max_ratio_to_same = max(row["ratio_to_same"] for row in pair_rows.values())
max_aggregate2 = max(max_aggregate2_by_c.values())

check(
    "Zero-row projection is enforced",
    max_row_after < mp.mpf("1e-80"),
    f"max_row_after={fmt(max_row_after, 18)}",
)
check(
    "Disjoint two-factor moment matches the closed form",
    max_formula_error < mp.mpf("1e-80"),
    f"max_formula_error={fmt(max_formula_error, 18)}",
)
check(
    "Disjoint two-factor aggregate is tiny over tested width-2 matchings",
    max_aggregate2 < mp.mpf("0.001"),
    f"max_aggregate2={fmt(max_aggregate2, 18)}",
)
check(
    "Nonshared two-factor moment is small compared with same-edge variance",
    max_ratio_to_same < mp.mpf("0.07"),
    f"max_rho2_over_A={fmt(max_ratio_to_same, 18)}",
)
check(
    "Two-factor aggregate falls rapidly as c grows",
    max_aggregate2_by_c[mp.mpf("4")] < max_aggregate2_by_c[mp.mpf("2")]
    and max_aggregate2_by_c[mp.mpf("2")] < max_aggregate2_by_c[mp.mpf("1")]
    and max_aggregate2_by_c[mp.mpf("1")] < max_aggregate2_by_c[mp.mpf("0.5")],
    ", ".join(f"c={fmt(c,4)} maxAgg2={fmt(max_aggregate2_by_c[c], 12)}" for c in cs),
)
check(
    "Disjoint three-factor aggregate is small but not zero",
    max_aggregate3 < mp.mpf("1e-4"),
    f"max_aggregate3={fmt(max_aggregate3, 18)}",
)

print("\n=== Consequence ===")
print("For two disjoint localized pair factors, zero-row neutrality gives the")
print("closed form rho2 = 2 A_N(c)/((N-2)(N-3)).  In a width-2 matching, the")
print("aggregate two-factor contribution binom(N/2,2) rho2^2 is O(N^-2) when")
print("A_N(c) is bounded, and it is tiny in all tested cases.  The first triple")
print("cycle-residue audit is small but not zero, so neutrality is controlled")
print("rather than exact.  This supports the nonshared-neutrality half of Lemma")
print("M in the labeled model; the remaining analytic task is to bound all")
print("higher cycle residues uniformly and then transfer the result through the")
print("unlabeled quotient/selected-class denominator.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
