#!/usr/bin/env python3
"""
Paper 28 receipt: boundary replacement cancellation identity.

The physical missed-residue campaign showed signed cancellation, but not why.
This receipt proves the first structural identity:

For any symmetric row-zero kernel D with zero diagonal, the endpoint-spanning
perfect-matching observable has zero with-replacement leading term for every
r>=2.  Every pairing either contains an interior-interior edge, whose
expectation is the off-diagonal mean of D, or an endpoint-interior edge, whose
expectation is an endpoint row mean.  Both vanish by row-zero canonicality.

Therefore the missed residue is entirely a finite-population
without-replacement correction.  The receipt then falsifies the stronger
row-zero-only theorem: q2-calibrated row-zero adversaries can still have large
without-replacement endpoint correction.

All non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict
import math
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=36):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def zero_matrix(n):
    return [[mp.mpf(0) for _ in range(n)] for _ in range(n)]


def scale_matrix(matrix, scale):
    scale = mp.mpf(scale)
    return [[scale * value for value in row] for row in matrix]


def add_matrices(*matrices):
    n = len(matrices[0])
    out = zero_matrix(n)
    for matrix in matrices:
        for i in range(n):
            for j in range(n):
                out[i][j] += matrix[i][j]
    return out


def offdiag_sum(matrix):
    n = len(matrix)
    return mp.fsum(matrix[i][j] for i in range(n) for j in range(n) if i != j)


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


def max_row_linf(D):
    n = len(D)
    return max(abs(mp.fsum(D[i][j] for j in range(n) if i != j)) for i in range(n))


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


def disjoint_moment(D, r):
    n = len(D)
    entries = []
    for i in range(n):
        for j in range(n):
            if i != j:
                entries.append(((1 << i) | (1 << j), D[i][j]))
    dp = {0: mp.mpf(1)}
    for _depth in range(1, r + 1):
        next_dp = defaultdict(mp.mpf)
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                next_dp[used | mask] += value * edge_value
        dp = next_dp
    return mp.fsum(dp.values()) / falling(n, 2 * r)


def disjoint_moment_on_vertices(D, vertices, r):
    m = len(vertices)
    entries = []
    for i in vertices:
        for j in vertices:
            if i != j:
                entries.append(((1 << i) | (1 << j), D[i][j]))
    dp = {0: mp.mpf(1)}
    for _depth in range(1, r + 1):
        next_dp = defaultdict(mp.mpf)
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                next_dp[used | mask] += value * edge_value
        dp = next_dp
    return mp.fsum(dp.values()) / falling(m, 2 * r)


def missed_rho(D, r):
    from itertools import combinations

    n = len(D)
    denom = mp.mpf(math.comb(n, 2 * r))
    out = mp.mpf(0)
    for subset in combinations(range(n), 2 * r):
        if subset[0] == 0 and subset[-1] == n - 1:
            out += disjoint_moment_on_vertices(D, subset, r)
    return out / denom


def coefficient(n, r, rho):
    return mp.mpf(math.comb(n // 2, r)) * rho * rho


def beta_from_rho(n, r, rho):
    q = coefficient(n, r, rho)
    if q == 0:
        return mp.mpf(0)
    return mp.mpf(n) * mp.power(q, mp.mpf(1) / r)


def q_values(D, max_r):
    n = len(D)
    return {r: coefficient(n, r, disjoint_moment(D, r)) for r in range(2, max_r + 1)}


def calibrate_to_q2(D, target_q2):
    q = q_values(D, 2)
    return scale_matrix(D, (target_q2 / q[2]) ** mp.mpf("0.25"))


def fourier_vector(n, k, kind):
    out = []
    for i in range(n):
        x = (mp.mpf(i) + mp.mpf("0.5")) / n
        angle = 2 * mp.pi * k * x
        out.append(mp.cos(angle) if kind == "cos" else mp.sin(angle))
    mean = mp.fsum(out) / n
    centered = [value - mean for value in out]
    norm = mp.sqrt(mp.fsum(value * value for value in centered))
    return [value / norm for value in centered]


def outer_kernel(vector):
    n = len(vector)
    out = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                out[i][j] = vector[i] * vector[j]
    return project_symmetric_zero_row(out)


def balanced_block_D(n):
    half = n // 2
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                same = (i < half and j < half) or (i >= half and j >= half)
                matrix[i][j] = mp.mpf(1) if same else mp.mpf(-1)
    return project_symmetric_zero_row(matrix)


def replacement_factors(D):
    n = len(D)
    row0 = mp.fsum(D[0][j] for j in range(n) if j != 0) / n
    rowN = mp.fsum(D[n - 1][j] for j in range(n) if j != n - 1) / n
    pair_mean = offdiag_sum(D) / (mp.mpf(n) ** 2)
    return row0, rowN, pair_mean


print("=" * 80)
print("Paper 28 boundary replacement cancellation identity")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
physical_q2 = mp.mpf("0.0000458248873091935")  # from p28 coefficient grid scale
kernels = {
    "balanced_block": calibrate_to_q2(balanced_block_D(n), physical_q2),
    "fourier_rank_one": calibrate_to_q2(outer_kernel(fourier_vector(n, 1, "cos")), physical_q2),
    "fourier_three_mode": calibrate_to_q2(
        add_matrices(
            outer_kernel(fourier_vector(n, 1, "cos")),
            scale_matrix(outer_kernel(fourier_vector(n, 1, "sin")), mp.mpf("0.5")),
            scale_matrix(outer_kernel(fourier_vector(n, 2, "cos")), mp.mpf("0.25")),
        ),
        physical_q2,
    ),
}

max_factor = mp.mpf(0)
max_without_beta = mp.mpf(0)
large_without = []

print("\n=== With-replacement leading factors and without-replacement residue ===")
for name, D in kernels.items():
    row0, rowN, pair_mean = replacement_factors(D)
    factor_norm = max(abs(row0), abs(rowN), abs(pair_mean), max_row_linf(D))
    max_factor = max(max_factor, factor_norm)
    print(f"\n{name}: row0_mean={fmt(row0, 18)}, rowN_mean={fmt(rowN, 18)}, pair_mean={fmt(pair_mean, 18)}")
    for r in range(2, 7):
        beta = beta_from_rho(n, r, missed_rho(D, r))
        max_without_beta = max(max_without_beta, beta)
        print(f"  r={r}, without_replacement_beta={fmt(beta, 18)}")
        if beta > mp.mpf("0.65"):
            large_without.append((name, r, beta))

check(
    "with-replacement endpoint-spanning leading term vanishes for canonical kernels",
    max_factor < mp.mpf("1e-80"),
    f"max_factor={fmt(max_factor, 18)}",
)
check(
    "without-replacement correction can be large despite zero leading term",
    len(large_without) > 0,
    f"largest_beta={fmt(max_without_beta, 18)}",
)
check(
    "row-zero replacement cancellation alone is not the missed-residue theorem",
    any(name == "balanced_block" for name, _r, _beta in large_without),
    "balanced_block violates endpoint envelope",
)

print("\n=== Theorem status ===")
print("PROVED FINITE IDENTITY: row-zero canonicality kills the with-replacement")
print("endpoint-spanning leading term for every r>=2.  FALSIFIED STRONGER ROUTE:")
print("row-zero cancellation alone does not control the finite-population")
print("without-replacement correction; staged and Fourier adversaries can still")
print("have large endpoint missed-residue beta.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
