#!/usr/bin/env python3
"""
Paper 27 receipt: rank-copula bound scaling for density-matched Lemma M.

The previous receipt showed that unlabeled projection only mildly contracts the
density-matched one-pair Palm residue.  The remaining theorem path is therefore
rank-copula smallness plus nonshared-cycle neutrality.

This receipt isolates the one-axis rank copula

    q_axis(a,b) = P(two ordered siblings have ranks a,b)

after marginal matching.  Write

    q_axis = u + delta,       u = 1 / (N(N-1)) on a != b.

After symmetrizing and projecting away numerical row-margin error, delta lies
in the symmetric zero-row ordered-pair representation.  Then the labeled
two-axis one-pair likelihood has the exact representation-theoretic target

    S_N^label - 1 = A_N(c)^2 / d_N,

where

    A_N(c) = N(N-1) sum_{a != b} delta(a,b)^2,
    d_N    = N(N-3)/2.

Thus a uniform bound on A_N(c) implies the one-pair local factor has L2 norm
O(1/N).  This is the analytic core of density-matched Lemma M; the remaining
many-pair task is nonshared-cycle neutrality.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from itertools import permutations
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

    corrected = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                corrected[i][j] = u + corrected_delta[i][j]

    row_after = [
        mp.fsum(corrected_delta[i][j] for j in range(n) if i != j)
        for i in range(n)
    ]
    sym_linf = max(abs(sym[i][j] - sym[j][i]) for i in range(n) for j in range(n) if i != j)
    row_before_linf = max(abs(value) for value in row)
    row_after_linf = max(abs(value) for value in row_after)
    projection_linf = max(
        abs(corrected[i][j] - sym[i][j]) for i in range(n) for j in range(n) if i != j
    )
    return corrected, corrected_delta, {
        "total_before": total,
        "sym_linf": sym_linf,
        "row_before_linf": row_before_linf,
        "row_after_linf": row_after_linf,
        "projection_linf": projection_linf,
    }


def axis_excess_from_delta(delta):
    n = len(delta)
    m = mp.mpf(n) * (n - 1)
    return m * mp.fsum(delta[i][j] ** 2 for i in range(n) for j in range(n) if i != j)


def representation_dimension(n):
    return mp.mpf(n) * (n - 3) / 2


def formula_labeled_excess(axis_excess, n):
    return axis_excess**2 / representation_dimension(n)


def palm_weight_for_perm(perm, q_axis):
    n = len(perm)
    total = mp.mpf(0)
    for a in range(n):
        for b in range(n):
            if a != b:
                total += q_axis[a][b] * q_axis[perm[a]][perm[b]]
    return total / mp.mpf(math.factorial(n - 2))


def exact_labeled_excess(n, q_axis):
    factorial_n = mp.mpf(math.factorial(n))
    square_sum = mp.mpf(0)
    total = mp.mpf(0)
    for perm in permutations(range(n)):
        q = palm_weight_for_perm(perm, q_axis)
        total += q
        square_sum += q * q
    return factorial_n * square_sum - 1, total


def linf_distance(a, b):
    n = len(a)
    return max(abs(a[i][j] - b[i][j]) for i in range(n) for j in range(n) if i != j)


print("=" * 80)
print("Paper 27 rank-copula bound scaling receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

small_sizes = [5, 6, 7, 8]
scaling_sizes = [8, 12, 16, 24]
cs = [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")]
nodes_low = 16
nodes_high = 22
rows = {}
exact_rows = {}

print("\n(1) Axis-copula scaling")
for c in cs:
    print("\n" + "=" * 80)
    print(f"c={fmt(c, 8)}")
    print("=" * 80)
    previous_axis = None
    for n in scaling_sizes:
        raw_low = q_axis_matrix(n, c, nodes_low)
        raw_high = q_axis_matrix(n, c, nodes_high)
        conv = linf_distance(raw_low, raw_high)
        corrected, delta, projection = sym_normalize_project(raw_high)
        axis_excess = axis_excess_from_delta(delta)
        labeled_bound = formula_labeled_excess(axis_excess, n)
        rows[(n, c)] = {
            "axis_excess": axis_excess,
            "labeled_bound": labeled_bound,
            "conv": conv,
            **projection,
        }
        trend = "" if previous_axis is None else f" ratio_prev={fmt(axis_excess / previous_axis, 12)}"
        previous_axis = axis_excess
        print(
            f"N={n} A_N={fmt(axis_excess, 18)} "
            f"bound=A^2/d={fmt(labeled_bound, 18)} "
            f"N^2*bound={fmt((mp.mpf(n)**2) * labeled_bound, 18)} "
            f"row_before={fmt(projection['row_before_linf'], 8)} "
            f"proj={fmt(projection['projection_linf'], 8)} conv={fmt(conv, 8)}{trend}"
        )

print("\n(2) Exact permutation identity check")
for c in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")]:
    print(f"\nc={fmt(c, 8)}")
    for n in small_sizes:
        raw = q_axis_matrix(n, c, nodes_high)
        corrected, delta, _projection = sym_normalize_project(raw)
        axis_excess = axis_excess_from_delta(delta)
        formula = formula_labeled_excess(axis_excess, n)
        exact, total = exact_labeled_excess(n, corrected)
        diff = abs(exact - formula)
        exact_rows[(n, c)] = {"formula": formula, "exact": exact, "diff": diff, "total": total}
        print(
            f"N={n} exact={fmt(exact, 18)} formula={fmt(formula, 18)} "
            f"diff={fmt(diff, 8)} q_total={fmt(total, 18)}"
        )

max_axis_by_c = {
    c: max(rows[(n, c)]["axis_excess"] for n in scaling_sizes)
    for c in cs
}
max_formula_diff = max(row["diff"] for row in exact_rows.values())
max_total_error = max(abs(row["total"] - 1) for row in exact_rows.values())
max_row_after = max(rows[(n, c)]["row_after_linf"] for n in scaling_sizes for c in cs)
max_projection = max(rows[(n, c)]["projection_linf"] for n in scaling_sizes for c in cs)
max_conv = max(rows[(n, c)]["conv"] for n in scaling_sizes for c in cs)
max_n2_bound_by_c = {
    c: max((mp.mpf(n) ** 2) * rows[(n, c)]["labeled_bound"] for n in scaling_sizes)
    for c in cs
}

check(
    "Margin projection enforces zero row sums",
    max_row_after < mp.mpf("1e-80"),
    f"max_row_after={fmt(max_row_after, 18)}",
)
check(
    "Margin correction is controlled and explicitly reported",
    max_projection < mp.mpf("0.006"),
    f"max_projection_linf={fmt(max_projection, 18)}",
)
check(
    "Node-doubling convergence is adequate for scaling receipt",
    max_conv < mp.mpf("0.002"),
    f"max_linf_delta={fmt(max_conv, 18)}",
)
check(
    "Representation formula matches exact permutation second moment at N<=8",
    max_formula_diff < mp.mpf("1e-70") and max_total_error < mp.mpf("1e-70"),
    f"max_formula_diff={fmt(max_formula_diff, 18)} max_total_error={fmt(max_total_error, 18)}",
)
check(
    "Axis copula excess is bounded over tested N for each c",
    all(max_axis_by_c[c] < mp.mpf("0.6") for c in cs),
    ", ".join(f"c={fmt(c,4)} maxA={fmt(max_axis_by_c[c], 12)}" for c in cs),
)
check(
    "Axis copula excess falls rapidly as c grows",
    max_axis_by_c[mp.mpf("4")] < max_axis_by_c[mp.mpf("2")]
    and max_axis_by_c[mp.mpf("2")] < max_axis_by_c[mp.mpf("1")]
    and max_axis_by_c[mp.mpf("1")] < max_axis_by_c[mp.mpf("0.5")],
    ", ".join(f"c={fmt(c,4)} maxA={fmt(max_axis_by_c[c], 12)}" for c in cs),
)
check(
    "Formula bound gives O(N^-2) one-pair labeled excess when A_N is bounded",
    all(max_n2_bound_by_c[c] < mp.mpf("2.0") for c in cs),
    ", ".join(f"c={fmt(c,4)} maxN2={fmt(max_n2_bound_by_c[c], 12)}" for c in cs),
)

print("\n=== Consequence ===")
print("The density-matched one-axis copula has bounded tested A_N(c), and the")
print("two-axis one-pair labeled second moment is exactly A_N(c)^2 / d_N after")
print("projecting numerical row-margin error away.  This gives a theorem-shaped")
print("route for Lemma M: prove a uniform analytic bound on A_N(c), ideally with")
print("decay in c, then combine it with nonshared-cycle neutrality.  The quotient")
print("projection is no longer the main mechanism; representation dimension is.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
