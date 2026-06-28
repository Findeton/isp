#!/usr/bin/env python3
"""
Paper 27 receipt: cluster-expansion bound audit.

The previous receipt found nonzero but rapidly decreasing higher-cycle residues
for the physical density-matched rank copula.  This receipt asks a sharper
question: is the decay merely a special feature of that physical kernel, or is
it already forced by the zero-row matching geometry?

For a symmetric zero-row matrix D on ordered off-diagonal rank pairs, normalized
by

    A = (1/(N(N-1))) sum_{i != j} D_ij^2 = 1,

the disjoint r-factor residue is

    rho_r(D) = (1/(N)_{2r}) sum_{all endpoints distinct} prod_k D_{a_k b_k}.

The naive universal cluster-expansion hope would say that N^r |rho_r| should
remain bounded for fixed r, and the width-2 aggregate

    binom(N/2,r) rho_r(D)^2

should decay like O(N^-r), using only the zero-row condition.  The receipt
tests this on:

  * the physical density-matched rank copula, rescaled to A=1;
  * balanced block matrices;
  * projected Fourier/cosine kernels;
  * repeated sparse signed-cycle blocks;
  * deterministic projected pseudo-random symmetric matrices.

This is not a theorem.  It is a hostile finite search for a zero-row matrix
family that breaks the proposed zero-row-only cluster expansion.  A found
failure is a successful receipt: it means the record law needs an additional
regularity/spectral/mixing condition, not just zero-row neutrality plus
bounded one-pair energy.

The same run also reports spectral concentration.  The balanced block failure
has very small stable rank; random projected matrices have larger stable rank
and do not show comparable coherent residues.  But the physical rank-copula can
also have small stable rank without the same explosion.  Thus stable rank is a
symptom, not the final condition.  The better object is a matching/free-energy
or full generating-function regularity condition.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict
import math
import random
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


def zero_matrix(n):
    return [[mp.mpf(0) for _ in range(n)] for _ in range(n)]


def project_symmetric_zero_row(matrix):
    n = len(matrix)
    sym = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                sym[i][j] = (mp.mpf(matrix[i][j]) + mp.mpf(matrix[j][i])) / 2

    row = [mp.fsum(sym[i][j] for j in range(n) if i != j) for i in range(n)]
    total_row = mp.fsum(row)
    correction_constant = -total_row / ((n - 2) * (n - 1))
    out = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                h = (row[i] + row[j]) / (n - 2) + correction_constant
                out[i][j] = sym[i][j] - h
    return out


def axis_excess_from_D(D):
    n = len(D)
    return mp.fsum(D[i][j] ** 2 for i in range(n) for j in range(n) if i != j) / (
        mp.mpf(n) * (n - 1)
    )


def normalize_A_one(D):
    A = axis_excess_from_D(D)
    if A == 0:
        raise ValueError("cannot normalize zero matrix")
    scale = 1 / mp.sqrt(A)
    n = len(D)
    return [[scale * D[i][j] for j in range(n)] for i in range(n)], A


def max_row_linf(D):
    n = len(D)
    return max(abs(mp.fsum(D[i][j] for j in range(n) if i != j)) for i in range(n))


def spectral_metrics(D):
    n = len(D)
    matrix = mp.matrix(D)
    eigenvalues = mp.eigsy(matrix, eigvals_only=True)
    op_norm = max(abs(value) for value in eigenvalues)
    frob_squared = mp.fsum(D[i][j] ** 2 for i in range(n) for j in range(n))
    stable_rank = frob_squared / (op_norm * op_norm) if op_norm else mp.inf
    return {
        "op_norm": op_norm,
        "op_over_n": op_norm / n,
        "stable_rank": stable_rank,
    }


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


def pair_entries(D):
    n = len(D)
    entries = []
    for i in range(n):
        for j in range(n):
            if i != j:
                entries.append(((1 << i) | (1 << j), D[i][j]))
    return entries


def disjoint_moments(D, max_r):
    n = len(D)
    max_possible = min(max_r, n // 2)
    entries = pair_entries(D)
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


def physical_delta_D(n, c, nodes):
    c = mp.mpf(c)
    s_nodes = legendre_nodes(nodes, 0, 1)
    e0_nodes = legendre_nodes(nodes, -c, c)
    e1_nodes = legendre_nodes(nodes + 1, -c, c)
    matrix = zero_matrix(n)
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

    sym = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                sym[i][j] = (matrix[i][j] + matrix[j][i]) / 2

    total = mp.fsum(sym[i][j] for i in range(n) for j in range(n) if i != j)
    prob = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                prob[i][j] = sym[i][j] / total

    uniform = 1 / (mp.mpf(n) * (n - 1))
    residue = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                residue[i][j] = mp.mpf(n) * (n - 1) * (prob[i][j] - uniform)
    return project_symmetric_zero_row(residue)


def balanced_block_D(n):
    half = n // 2
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            same = (i < half and j < half) or (i >= half and j >= half)
            matrix[i][j] = mp.mpf(1) if same else mp.mpf(-1)
    return project_symmetric_zero_row(matrix)


def cosine_D(n, frequency):
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                angle = 2 * mp.pi * frequency * (i - j) / n
                matrix[i][j] = mp.cos(angle)
    return project_symmetric_zero_row(matrix)


def sparse_cycle_blocks_D(n):
    matrix = zero_matrix(n)
    for base in range(0, n - 3, 4):
        edges = [
            (base, base + 1, 1),
            (base + 1, base, 1),
            (base, base + 2, -1),
            (base + 2, base, -1),
            (base + 1, base + 3, -1),
            (base + 3, base + 1, -1),
            (base + 2, base + 3, 1),
            (base + 3, base + 2, 1),
        ]
        for i, j, value in edges:
            matrix[i][j] = mp.mpf(value)
    return project_symmetric_zero_row(matrix)


def random_projected_D(n, seed):
    rng = random.Random(seed)
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(i + 1, n):
            value = mp.mpf(rng.randrange(-7, 8))
            matrix[i][j] = value
            matrix[j][i] = value
    return project_symmetric_zero_row(matrix)


def matrix_suite(n):
    out = [
        ("block", balanced_block_D(n)),
        ("cos1", cosine_D(n, 1)),
        ("cos2", cosine_D(n, 2 if n > 6 else 1)),
        ("sparse4", sparse_cycle_blocks_D(n)),
        ("rand11", random_projected_D(n, 11 + n)),
        ("rand29", random_projected_D(n, 29 + n)),
    ]
    if n <= 12:
        out.append(("physical_c0.5", physical_delta_D(n, mp.mpf("0.5"), 12)))
    return out


print("=" * 80)
print("Paper 27 cluster-expansion bound audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

sizes = [8, 10, 12, 14]
max_r = 5
rows = []
max_row_after = mp.mpf(0)
max_formula_error = mp.mpf(0)

for n in sizes:
    print("\n" + "=" * 80)
    print(f"N={n}")
    print("=" * 80)
    for name, raw_D in matrix_suite(n):
        if axis_excess_from_D(raw_D) == 0:
            continue
        D, original_A = normalize_A_one(raw_D)
        spectral = spectral_metrics(D)
        max_row_after = max(max_row_after, max_row_linf(D))
        moments = disjoint_moments(D, max_r)
        print(
            f"\n{name} original_A={fmt(original_A, 18)} "
            f"op/N={fmt(spectral['op_over_n'], 12)} "
            f"stable_rank={fmt(spectral['stable_rank'], 12)}"
        )
        for r in range(2, max_r + 1):
            if r not in moments:
                continue
            rho = moments[r]
            aggregate = aggregate_matching_residue(n, r, rho)
            scaled_rho = (mp.mpf(n) ** r) * abs(rho)
            scaled_aggregate = (mp.mpf(n) ** r) * abs(aggregate)
            if r == 2:
                formula = 2 / ((mp.mpf(n) - 2) * (mp.mpf(n) - 3))
                max_formula_error = max(max_formula_error, abs(rho - formula))
            rows.append(
                {
                    "n": n,
                    "name": name,
                    "r": r,
                    "rho": rho,
                    "aggregate": aggregate,
                    "scaled_rho": scaled_rho,
                    "scaled_aggregate": scaled_aggregate,
                    "stable_rank": spectral["stable_rank"],
                    "op_over_n": spectral["op_over_n"],
                }
            )
            print(
                f"  r={r} rho={fmt(rho, 14)} "
                f"N^r|rho|={fmt(scaled_rho, 14)} "
                f"N^r*agg={fmt(scaled_aggregate, 14)}"
            )

max_scaled_by_r = {
    r: max(row["scaled_rho"] for row in rows if row["r"] == r)
    for r in range(2, max_r + 1)
}
max_scaled_aggregate_by_r = {
    r: max(row["scaled_aggregate"] for row in rows if row["r"] == r)
    for r in range(2, max_r + 1)
}
worst = max(rows, key=lambda row: row["scaled_rho"])
worst_aggregate = max(rows, key=lambda row: row["scaled_aggregate"])
max_block_stable_rank = max(row["stable_rank"] for row in rows if row["name"] == "block")
min_random_stable_rank = min(
    row["stable_rank"] for row in rows if row["name"].startswith("rand")
)
max_physical_stable_rank = max(
    row["stable_rank"] for row in rows if row["name"] == "physical_c0.5"
)

print("\n=== Max scaled residues ===")
for r in range(2, max_r + 1):
    print(
        f"r={r} max N^r|rho|={fmt(max_scaled_by_r[r], 14)} "
        f"max N^r*agg={fmt(max_scaled_aggregate_by_r[r], 14)}"
    )
print(
    "worst scaled rho: "
    f"N={worst['n']} family={worst['name']} r={worst['r']} "
    f"value={fmt(worst['scaled_rho'], 18)}"
)
print(
    "worst scaled aggregate: "
    f"N={worst_aggregate['n']} family={worst_aggregate['name']} r={worst_aggregate['r']} "
    f"value={fmt(worst_aggregate['scaled_aggregate'], 18)}"
)
print(f"max block stable rank = {fmt(max_block_stable_rank, 18)}")
print(f"min random stable rank = {fmt(min_random_stable_rank, 18)}")
print(f"max physical stable rank = {fmt(max_physical_stable_rank, 18)}")

check(
    "zero-row projection is enforced after A-normalization",
    max_row_after < mp.mpf("1e-80"),
    f"max_row_after={fmt(max_row_after, 18)}",
)
check(
    "two-factor formula holds for every hostile matrix",
    max_formula_error < mp.mpf("1e-80"),
    f"max_formula_error={fmt(max_formula_error, 18)}",
)
check(
    "zero-row-only cluster bound is false in hostile search",
    max_scaled_by_r[5] > mp.mpf("10000"),
    ", ".join(f"r={r}:{fmt(max_scaled_by_r[r], 8)}" for r in range(2, max_r + 1)),
)
check(
    "balanced block creates coherent high-order matching residue",
    worst["name"] == "block" and worst["r"] == 5,
    f"worst={worst['name']} r={worst['r']} value={fmt(worst['scaled_rho'], 12)}",
)
physical_scaled_aggregate = max(
    row["scaled_aggregate"] for row in rows if row["name"] == "physical_c0.5"
)
check(
    "physical rank-copula remains far below hostile block aggregate",
    physical_scaled_aggregate < mp.mpf("100"),
    f"physical_max_scaled_aggregate={fmt(physical_scaled_aggregate, 12)}",
)
check(
    "block obstruction has collapsed stable rank",
    max_block_stable_rank < mp.mpf("2"),
    f"max_block_stable_rank={fmt(max_block_stable_rank, 12)}",
)
check(
    "random projected controls have larger stable rank",
    min_random_stable_rank > max_block_stable_rank,
    f"min_random_stable_rank={fmt(min_random_stable_rank, 12)} "
    f"max_block_stable_rank={fmt(max_block_stable_rank, 12)}",
)
check(
    "stable rank alone is not the final separator",
    max_physical_stable_rank < mp.mpf("1.5") and physical_scaled_aggregate < mp.mpf("100"),
    f"physical_stable_rank={fmt(max_physical_stable_rank, 12)} "
    f"physical_scaled_aggregate={fmt(physical_scaled_aggregate, 12)}",
)
check(
    "two-factor neutrality misses the high-order obstruction",
    max_scaled_aggregate_by_r[2] < mp.mpf("2") and max_scaled_aggregate_by_r[5] > mp.mpf("1000"),
    ", ".join(
        f"r={r}:{fmt(max_scaled_aggregate_by_r[r], 8)}" for r in range(2, max_r + 1)
    ),
)

print("\n=== Consequence ===")
print("Zero-row neutrality and bounded one-pair energy are not enough.  The")
print("balanced block matrix passes the exact two-factor formula but creates")
print("large coherent high-order matching residues.  Spectral concentration")
print("is a symptom, but not a sufficient separator, because the physical")
print("rank-copula can also have low stable rank without the same explosion.")
print("The next proof target must control the matching/free-energy generating")
print("function itself, or derive that control from a full finite-dimensional")
print("record law that excludes macroscopic staged/fiber blocks.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
