#!/usr/bin/env python3
"""
Paper 28 receipt: physical missed-residue cancellation campaign.

The proper-interval no-go showed that arbitrary bounded residue on
endpoint-spanning 2r-subsets is too large.  The only surviving local-interval
route is therefore a physical signed-cancellation theorem for the actual
rank-copula kernel D_N.

This receipt defines the missed contribution exactly:

    rho_miss(N,r;D)
      =
    (1 / binom(N,2r))
    sum_{|S|=2r, {0,N-1} subset S} rho_{S,r}(D).

It then tests whether the physical density-matched rank-copula has the
required all-order envelope on this missed contribution, and compares it with
smooth Fourier and staged/block adversaries calibrated to the physical q2.

The receipt also proves a finite decomposition identity for the missed
coefficient:

    rho_N,r = rho_miss + rho_seen,

where rho_seen is the contribution from subsets contained in at least one
proper contiguous interval.  This is exact double counting, not asymptotics.

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


def pair_entries(D, subset=None):
    n = len(D)
    vertices = range(n) if subset is None else subset
    entries = []
    for i in vertices:
        for j in vertices:
            if i != j:
                entries.append(((1 << i) | (1 << j), D[i][j]))
    return entries


def disjoint_moment_on_vertices(D, vertices, r):
    m = len(vertices)
    if r == 0:
        return mp.mpf(1)
    entries = pair_entries(D, vertices)
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


def missed_seen_rho(D, r):
    n = len(D)
    k = 2 * r
    denom = mp.mpf(math.comb(n, k))
    miss_sum = mp.mpf(0)
    seen_sum = mp.mpf(0)
    miss_abs_sum = mp.mpf(0)
    miss_count = 0
    seen_count = 0
    for subset in combinations(range(n), k):
        local = disjoint_moment_on_vertices(D, subset, r)
        if subset[0] == 0 and subset[-1] == n - 1:
            miss_sum += local
            miss_abs_sum += abs(local)
            miss_count += 1
        else:
            seen_sum += local
            seen_count += 1
    return {
        "miss": miss_sum / denom,
        "seen": seen_sum / denom,
        "miss_abs": miss_abs_sum / denom,
        "miss_count": miss_count,
        "seen_count": seen_count,
        "total_count": int(denom),
    }


def coefficient(n, r, rho):
    return mp.mpf(math.comb(n // 2, r)) * rho * rho


def beta_from_rho(n, r, rho):
    q = coefficient(n, r, rho)
    if q == 0:
        return mp.mpf(0)
    return mp.mpf(n) * mp.power(abs(q), mp.mpf(1) / r)


def q_values(D, max_r):
    n = len(D)
    out = {}
    rho = {}
    for r in range(2, max_r + 1):
        rho[r] = global_rho(D, r)
        out[r] = coefficient(n, r, rho[r])
    return out, rho


def calibrate_to_q2(D, target_q2):
    q, _rho = q_values(D, 2)
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


print("=" * 80)
print("Paper 28 physical missed-residue cancellation campaign")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 12
c = mp.mpf("0.5")
sizes = [8, 10, 12, 14]
max_r_by_n = {8: 4, 10: 5, 12: 6, 14: 6}

physical_rows = []
max_decomp_error = mp.mpf(0)
max_phys_miss_beta = mp.mpf(0)
max_phys_abs_beta = mp.mpf(0)
max_phys_miss_fraction = mp.mpf(0)
bad_phys_envelope = []

print("\n=== Physical missed residue ===")
for n in sizes:
    D = physical_delta(n, c, nodes)
    print(f"\nN={n}, c={fmt(c, 8)}, row_linf={fmt(max_row_linf(D), 18)}")
    for r in range(2, max_r_by_n[n] + 1):
        total_rho = global_rho(D, r)
        parts = missed_seen_rho(D, r)
        decomp_error = abs(total_rho - parts["miss"] - parts["seen"])
        max_decomp_error = max(max_decomp_error, decomp_error)
        beta_total = beta_from_rho(n, r, total_rho)
        beta_miss = beta_from_rho(n, r, parts["miss"])
        beta_abs = beta_from_rho(n, r, parts["miss_abs"])
        max_phys_miss_beta = max(max_phys_miss_beta, beta_miss)
        max_phys_abs_beta = max(max_phys_abs_beta, beta_abs)
        fraction = abs(parts["miss"]) / abs(total_rho) if total_rho else mp.inf
        max_phys_miss_fraction = max(max_phys_miss_fraction, fraction)
        if beta_miss > mp.mpf("0.65"):
            bad_phys_envelope.append((n, r, beta_miss))
        physical_rows.append((n, r, beta_total, beta_miss, beta_abs, fraction))
        print(
            f"  r={r}, miss_count={parts['miss_count']}/{parts['total_count']}, "
            f"rho_total={fmt(total_rho, 18)}, rho_miss={fmt(parts['miss'], 18)}, "
            f"rho_miss_abs={fmt(parts['miss_abs'], 18)}, "
            f"miss/total={fmt(fraction, 18)}, "
            f"beta_total={fmt(beta_total, 18)}, beta_miss={fmt(beta_miss, 18)}, "
            f"beta_abs={fmt(beta_abs, 18)}"
        )

check(
    "missed plus seen contribution exactly reconstructs global rho",
    max_decomp_error < mp.mpf("1e-80"),
    f"max_decomp_error={fmt(max_decomp_error, 18)}",
)
check(
    "physical signed missed residue passes the audited beta/N envelope",
    not bad_phys_envelope,
    f"max_beta_miss={fmt(max_phys_miss_beta, 18)}",
)
check(
    "physical absolute missed residue is not enough for the envelope",
    max_phys_abs_beta > mp.mpf("0.65"),
    f"max_beta_abs={fmt(max_phys_abs_beta, 18)}",
)
check(
    "physical missed residue is sometimes a substantial signed part of total rho",
    max_phys_miss_fraction > mp.mpf("0.1"),
    f"max_fraction={fmt(max_phys_miss_fraction, 18)}",
)

print("\n=== Adversarial comparison at N=12 ===")
n = 12
phys = physical_delta(n, c, nodes)
phys_q, _phys_rho = q_values(phys, 6)
target_q2 = phys_q[2]
adversaries = {
    "balanced_block": calibrate_to_q2(balanced_block_D(n), target_q2),
    "fourier_rank_one": calibrate_to_q2(outer_kernel(fourier_vector(n, 1, "cos")), target_q2),
    "fourier_three_mode": calibrate_to_q2(
        add_matrices(
            outer_kernel(fourier_vector(n, 1, "cos")),
            scale_matrix(outer_kernel(fourier_vector(n, 1, "sin")), mp.mpf("0.5")),
            scale_matrix(outer_kernel(fourier_vector(n, 2, "cos")), mp.mpf("0.25")),
        ),
        target_q2,
    ),
}

adversary_large = []
for name, D in adversaries.items():
    print(f"\n{name}:")
    for r in range(2, 7):
        parts = missed_seen_rho(D, r)
        beta_miss = beta_from_rho(n, r, parts["miss"])
        print(
            f"  r={r}, rho_miss={fmt(parts['miss'], 18)}, "
            f"beta_miss={fmt(beta_miss, 18)}"
        )
        if beta_miss > mp.mpf("0.65"):
            adversary_large.append((name, r, beta_miss))

check(
    "q2-calibrated adversaries can have large missed-residue beta",
    len(adversary_large) > 0,
    f"largest={fmt(max(item[2] for item in adversary_large), 18)}",
)

print("\n=== Theorem status ===")
print("FINITE STATUS: the actual audited physical signed missed residue passes")
print("the beta/N envelope through the tested grid, while the absolute missed")
print("residue and q2-calibrated adversaries do not.  Therefore cancellation is")
print("real in the physical kernel and cannot be replaced by an absolute bound.")
print("But this receipt does not prove the all-N all-r theorem.  The remaining")
print("target is an analytic identity explaining the signed cancellation.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
