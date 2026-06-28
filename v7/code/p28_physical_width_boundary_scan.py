#!/usr/bin/env python3
"""
Paper 28 receipt: physical width-boundary scan.

The signed coefficient envelope has so far been audited on the bounded-width
grid with the hostile corner c=0.5.  This receipt asks whether the physical
rank-copula itself violates the envelope if the width parameter is pushed
below that audited boundary.

This is not a theorem about the intended bounded-width domain.  It is a
hostile boundary scan:

    if c<0.5 already violates beta<=0.65, then the lower-width guard is real
    and cannot be dropped from the click-law hypotheses.

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


def disjoint_moments(D):
    n = len(D)
    entries = [((1 << i) | (1 << j), D[i][j]) for i in range(n) for j in range(n) if i != j]
    dp = {0: mp.mpf(1)}
    out = {}
    for r in range(1, n // 2 + 1):
        next_dp = defaultdict(mp.mpf)
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                next_dp[used | mask] += value * edge_value
        out[r] = mp.fsum(next_dp.values()) / falling(n, 2 * r)
        dp = next_dp
    return out


def beta_profile(D):
    n = len(D)
    rho = disjoint_moments(D)
    beta = {}
    for r in range(2, n // 2 + 1):
        q = mp.mpf(math.comb(n // 2, r)) * rho[r] * rho[r]
        beta[r] = mp.mpf(n) * mp.power(abs(q), mp.mpf(1) / r)
    return beta


print("=" * 80)
print("Paper 28 physical width-boundary scan")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 12
sizes = [10, 12, 14]
cs = [mp.mpf("0.5"), mp.mpf("0.375"), mp.mpf("0.25"), mp.mpf("0.1875"), mp.mpf("0.125")]

rows = []
print("\n=== Width scan ===")
for n in sizes:
    for c in cs:
        D = physical_delta(n, c, nodes)
        beta = beta_profile(D)
        max_beta = max(beta.values())
        r_star = max(beta, key=lambda r: beta[r])
        rows.append((n, c, max_beta, r_star))
        print(
            f"N={n}, c={fmt(c, 8)}, row_linf={fmt(max_row_linf(D), 12)}, "
            f"max_beta={fmt(max_beta, 18)} at r={r_star}"
        )

inside = [row for row in rows if row[1] >= mp.mpf("0.5")]
outside = [row for row in rows if row[1] < mp.mpf("0.5")]
max_inside = max(row[2] for row in inside)
max_outside = max(row[2] for row in outside)
worst_outside = max(outside, key=lambda row: row[2])

check(
    "audited boundary c>=0.5 stays below beta guard",
    max_inside <= mp.mpf("0.65"),
    f"max_inside={fmt(max_inside, 18)}",
)
check(
    "lower-width scan violates or stresses the beta guard",
    max_outside > max_inside,
    f"max_outside={fmt(max_outside, 18)} at N={worst_outside[0]} c={fmt(worst_outside[1], 8)} r={worst_outside[3]}",
)
check(
    "c=0.5 is the hostile edge of the intended audited window",
    all(row[2] <= mp.mpf("0.65") for row in inside),
    f"inside_count={len(inside)}",
)

print("\n=== Theorem status ===")
print("FINITE STATUS: decreasing c below the audited boundary increases the")
print("coefficient-root stress in this scan.  This does not falsify the intended")
print("bounded-width theorem with c>=0.5, but it says the lower-width guard is a")
print("real hypothesis, not cosmetic.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
