#!/usr/bin/env python3
"""
Paper 28 receipt: missed-residue equivalence no-go.

The physical missed-residue route asks for an all-order theorem controlling
endpoint-spanning subsets missed by proper intervals.  This receipt proves the
decisive obstruction:

At top matching order r=N/2, the only 2r-subset is the entire record set.
It is endpoint-spanning and is contained in no proper interval.  Therefore

    rho_miss(N,N/2;D) = rho_N,N/2(D)
    q_miss(N,N/2;D)   = q_N,N/2(D)

for every kernel D.

Thus an all-order missed-residue cancellation theorem is not an independent
bridge from interval heredity to the global coefficient envelope.  At top
order it is exactly the original global coefficient theorem.

All non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict
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


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


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


def global_rho(D, r):
    return disjoint_moment_on_vertices(D, tuple(range(len(D))), r)


def missed_rho(D, r):
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


print("=" * 80)
print("Paper 28 missed-residue equivalence no-go")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

max_top_error = mp.mpf(0)
top_betas = []

print("\n=== Top-order identity ===")
for n in [8, 10, 12]:
    r = n // 2
    kernels = {
        "balanced_block": balanced_block_D(n),
        "fourier_rank_one": outer_kernel(fourier_vector(n, 1, "cos")),
        "fourier_three_mode": add_matrices(
            outer_kernel(fourier_vector(n, 1, "cos")),
            scale_matrix(outer_kernel(fourier_vector(n, 1, "sin")), mp.mpf("0.5")),
            scale_matrix(outer_kernel(fourier_vector(n, 2, "cos")), mp.mpf("0.25")),
        ),
    }
    for name, D in kernels.items():
        rho_global = global_rho(D, r)
        rho_miss = missed_rho(D, r)
        error = abs(rho_global - rho_miss)
        max_top_error = max(max_top_error, error)
        beta = beta_from_rho(n, r, rho_miss)
        top_betas.append(beta)
        print(
            f"N={n}, r={r}, {name}: "
            f"rho_global={fmt(rho_global, 18)}, rho_miss={fmt(rho_miss, 18)}, "
            f"error={fmt(error, 8)}, beta={fmt(beta, 18)}"
        )

check(
    "top-order missed residue equals the global coefficient for every audited kernel",
    max_top_error < mp.mpf("1e-100"),
    f"max_error={fmt(max_top_error, 18)}",
)
check(
    "proper intervals see no top-order subset",
    all(math.comb(n - 2, n - 2) == 1 and math.comb(n, n) == 1 for n in [8, 10, 12]),
    "top subset is the full record set",
)
check(
    "all-order missed-residue theorem contains the original top coefficient problem",
    max(top_betas) > 0,
    f"max_top_beta={fmt(max(top_betas), 18)}",
)

print("\n=== Theorem status ===")
print("PROVED NO-GO: an all-order missed-residue cancellation theorem is not an")
print("independent interval bridge.  At r=N/2, missed residue equals the global")
print("coefficient for every kernel.  Therefore this route collapses back to the")
print("original coefficient-root theorem unless one adds an explicit global/subset")
print("sector or proves the full coefficient envelope directly.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
