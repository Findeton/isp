#!/usr/bin/env python3
"""
Paper 28 receipt: physical missed-residue parameter audit.

The first physical missed-residue campaign showed real signed cancellation at
c=0.5.  This receipt checks whether that is a one-corner accident or stable
across the bounded-width parameter grid used in the coefficient sieve.

It evaluates

    beta_miss(N,r,c) = N q_miss(N,r,c)^(1/r)

for the signed endpoint-spanning contribution and compares it with the same
quantity built from the absolute endpoint-spanning local moments.

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


def physical_delta(n, c, nodes):
    c = mp.mpf(c)
    matrix = zero_matrix(n)
    density_factor = 1 / (4 * c * c)
    for s, ws in legendre_nodes(nodes, 0, 1):
        for e0, we0 in legendre_nodes(nodes, -c, c):
            r0 = clamp_unit(marginal_cdf(s + e0, c))
            for e1, we1 in legendre_nodes(nodes + 1, -c, c):
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
    total = offdiag_sum(sym)
    uniform = 1 / (mp.mpf(n) * (n - 1))
    residue = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                probability = sym[i][j] / total
                residue[i][j] = mp.mpf(n) * (n - 1) * (probability - uniform)
    return project_symmetric_zero_row(residue)


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


def missed_signed_abs(D, r):
    n = len(D)
    denom = mp.mpf(math.comb(n, 2 * r))
    signed = mp.mpf(0)
    absolute = mp.mpf(0)
    for subset in combinations(range(n), 2 * r):
        if subset[0] != 0 or subset[-1] != n - 1:
            continue
        local = disjoint_moment_on_vertices(D, subset, r)
        signed += local
        absolute += abs(local)
    return signed / denom, absolute / denom


def beta_from_rho(n, r, rho):
    q = mp.mpf(math.comb(n // 2, r)) * rho * rho
    if q == 0:
        return mp.mpf(0)
    return mp.mpf(n) * mp.power(q, mp.mpf(1) / r)


print("=" * 80)
print("Paper 28 physical missed-residue parameter audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 12
sizes = [8, 10, 12]
cs = [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")]
max_r_by_n = {8: 4, 10: 5, 12: 6}

max_signed_beta = mp.mpf(0)
max_abs_beta = mp.mpf(0)
signed_records = []
abs_records = []

print("\n=== Parameter grid ===")
for n in sizes:
    for c in cs:
        D = physical_delta(n, c, nodes)
        print(f"\nN={n}, c={fmt(c, 8)}, row_linf={fmt(max_row_linf(D), 12)}")
        for r in range(2, max_r_by_n[n] + 1):
            signed, absolute = missed_signed_abs(D, r)
            beta_signed = beta_from_rho(n, r, signed)
            beta_abs = beta_from_rho(n, r, absolute)
            max_signed_beta = max(max_signed_beta, beta_signed)
            max_abs_beta = max(max_abs_beta, beta_abs)
            signed_records.append((n, c, r, beta_signed))
            abs_records.append((n, c, r, beta_abs))
            print(
                f"  r={r}, beta_signed={fmt(beta_signed, 18)}, "
                f"beta_abs={fmt(beta_abs, 18)}, "
                f"rho_signed={fmt(signed, 12)}"
            )

worst_signed = max(signed_records, key=lambda item: item[3])
worst_abs = max(abs_records, key=lambda item: item[3])

check(
    "signed physical missed residue passes beta<=0.65 over audited parameter grid",
    max_signed_beta <= mp.mpf("0.65"),
    f"max={fmt(max_signed_beta, 18)} at N={worst_signed[0]} c={fmt(worst_signed[1], 8)} r={worst_signed[2]}",
)
check(
    "absolute physical missed residue violates beta<=0.65 over audited grid",
    max_abs_beta > mp.mpf("0.65"),
    f"max={fmt(max_abs_beta, 18)} at N={worst_abs[0]} c={fmt(worst_abs[1], 8)} r={worst_abs[2]}",
)
check(
    "signed and absolute missed residues are sharply separated",
    max_abs_beta / max_signed_beta > 3,
    f"ratio={fmt(max_abs_beta / max_signed_beta, 18)}",
)

print("\n=== Theorem status ===")
print("FINITE STATUS: physical signed missed-residue cancellation is stable over")
print("the audited N,c grid, while absolute control fails badly.  This supports")
print("a signed cancellation theorem and falsifies any proof route based on")
print("positive or absolute interval residue bounds.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
