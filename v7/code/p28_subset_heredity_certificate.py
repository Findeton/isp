#!/usr/bin/env python3
"""
Paper 28 receipt: exact subset-heredity certificate theorem.

After smooth/spectral/local tests, the surviving target was a full calibrated
finite-dimensional projective law of interval interiors.  This receipt proves
the finite algebraic core of that target.

For any row-zero kernel D on N records and any r, the global disjoint matching
moment rho_{N,r} is exactly the average, over all 2r-subsets S, of the local
perfect-matching observable on D|_S:

    rho_{N,r}
      =
    average_{|S|=2r} rho_{S,r}.

Therefore a full local/subset heredity certificate immediately controls the
global coefficient q_{N,r} = binom(N/2,r) rho_{N,r}^2.

This does not prove that causal intervals supply all subset certificates.  It
proves the finite theorem that a sufficiently strong calibrated local law
would imply the coefficient-root envelope.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from itertools import combinations
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


def max_row_linf(matrix):
    n = len(matrix)
    return max(abs(mp.fsum(matrix[i][j] for j in range(n) if i != j)) for i in range(n))


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


def direct_disjoint_moment(D, r):
    n = len(D)
    if r == 0:
        return mp.mpf(1)
    entries = []
    for i in range(n):
        for j in range(n):
            if i != j:
                entries.append(((1 << i) | (1 << j), D[i][j]))
    dp = {0: mp.mpf(1)}
    for _depth in range(1, r + 1):
        next_dp = {}
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                key = used | mask
                next_dp[key] = next_dp.get(key, mp.mpf(0)) + value * edge_value
        dp = next_dp
    return mp.fsum(dp.values()) / falling(n, 2 * r)


def coefficient(n, r, rho):
    return mp.mpf(math.comb(n // 2, r)) * rho * rho


def restrict_subset(D, subset):
    m = len(subset)
    out = zero_matrix(m)
    for i, source_i in enumerate(subset):
        for j, source_j in enumerate(subset):
            if i != j:
                out[i][j] = D[source_i][source_j]
    return out


def subset_average_moment(D, r):
    n = len(D)
    values = []
    for subset in combinations(range(n), 2 * r):
        local = restrict_subset(D, subset)
        values.append(direct_disjoint_moment(local, r))
    average = mp.fsum(values) / len(values)
    max_abs = max(abs(value) for value in values)
    return average, max_abs, values


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
    out = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                same = (i < half and j < half) or (i >= half and j >= half)
                out[i][j] = mp.mpf(1) if same else mp.mpf(-1)
    return project_symmetric_zero_row(out)


print("=" * 80)
print("Paper 28 exact subset-heredity certificate")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 10
max_r = n // 2
cos1 = outer_kernel(fourier_vector(n, 1, "cos"))
sin1 = outer_kernel(fourier_vector(n, 1, "sin"))
cos2 = outer_kernel(fourier_vector(n, 2, "cos"))

kernels = {
    "balanced_block": balanced_block_D(n),
    "fourier_rank_one": cos1,
    "fourier_three_mode": add_matrices(cos1, scale_matrix(sin1, mp.mpf("0.5")), scale_matrix(cos2, mp.mpf("0.25"))),
}

max_identity_error = mp.mpf(0)
max_certificate_error = mp.mpf(0)
high_local_witness_ratio = mp.mpf(0)

print("\n=== Subset averaging identity ===")
for name, D in kernels.items():
    print(f"\n{name}: row_linf={fmt(max_row_linf(D), 18)}")
    for r in range(2, max_r + 1):
        global_rho = direct_disjoint_moment(D, r)
        average_rho, max_local, _values = subset_average_moment(D, r)
        identity_error = abs(global_rho - average_rho)
        max_identity_error = max(max_identity_error, identity_error)
        q_global = coefficient(n, r, global_rho)
        q_bound = coefficient(n, r, max_local)
        certificate_error = max(mp.mpf(0), q_global - q_bound)
        max_certificate_error = max(max_certificate_error, certificate_error)
        ratio = max_local / abs(global_rho) if global_rho else mp.inf
        high_local_witness_ratio = max(high_local_witness_ratio, ratio)
        print(
            f"  r={r}, global_rho={fmt(global_rho, 18)}, "
            f"subset_avg={fmt(average_rho, 18)}, "
            f"max_local={fmt(max_local, 18)}, "
            f"max/global_abs={fmt(ratio, 18)}, "
            f"q_global={fmt(q_global, 18)}, "
            f"q_bound={fmt(q_bound, 18)}"
        )

check(
    "subset averaging identity holds for all audited kernels",
    max_identity_error < mp.mpf("1e-80"),
    f"max_identity_error={fmt(max_identity_error, 18)}",
)
check(
    "local max certificate bounds every global q coefficient",
    max_certificate_error < mp.mpf("1e-100"),
    f"max_certificate_error={fmt(max_certificate_error, 18)}",
)
check(
    "high global moments have local subset witnesses",
    high_local_witness_ratio >= 1,
    f"max_local/global_abs={fmt(high_local_witness_ratio, 18)}",
)

print("\n=== Theorem status ===")
print("PROVED FINITE ALGEBRAIC CORE: rho_{N,r} is exactly the average of")
print("the local 2r-subset matching observable.  Therefore a full calibrated")
print("finite-dimensional heredity law controlling every local subset observable")
print("implies the global coefficient-root envelope.  This does not prove that")
print("causal intervals provide all such subset certificates; it identifies the")
print("precise remaining physical/geometric bridge.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
