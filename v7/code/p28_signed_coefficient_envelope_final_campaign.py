#!/usr/bin/env python3
"""
Paper 28 receipt: signed coefficient-root envelope final campaign.

Target under attack:

    q_{N,r}(D_phys) <= C (beta/N)^r

for the physical density-matched rank-copula, uniformly in N,r in the
bounded-width window.

This receipt does two different jobs and keeps them separate:

1. It extends the physical finite table to all matching orders on a deeper
   N ladder at c=0.5.

2. It falsifies broad proof routes.  The exact signed Möbius/falling-factor
   algebra, row-zero canonicality, and with-replacement leading cancellation
   are not sufficient: q2-calibrated canonical adversaries satisfy those
   structural properties while violating the root envelope.

Therefore this receipt cannot prove the physical theorem.  Its pass/fail
outcome is sharper:

    * finite physical evidence still supports the envelope;
    * current broad algebraic/structural gates are insufficient;
    * the remaining theorem must use a physical rank-copula identity/regularity
      beyond row-zero, exact expansion, and finite low-order calibration.

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


def pair_entries(D):
    n = len(D)
    entries = []
    for i in range(n):
        for j in range(n):
            if i != j:
                entries.append(((1 << i) | (1 << j), D[i][j]))
    return entries


def disjoint_moments(D):
    n = len(D)
    entries = pair_entries(D)
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


def coefficient(n, r, rho):
    return mp.mpf(math.comb(n // 2, r)) * rho * rho


def coefficient_profile(D):
    n = len(D)
    rho = disjoint_moments(D)
    q = {r: coefficient(n, r, rho[r]) for r in rho}
    beta = {r: mp.mpf(n) * mp.power(abs(q[r]), mp.mpf(1) / r) for r in q if r >= 2}
    return q, rho, beta


def pressure_density_from_q(n, q):
    zN = mp.mpf(1) + mp.fsum(q[r] * (mp.mpf(n) ** r) for r in q if r >= 2)
    return mp.log(zN) / n


def tail_after_q2(q):
    q2 = q.get(2, mp.mpf(0))
    if q2 == 0:
        return mp.inf
    return mp.fsum(q[r] for r in q if r >= 3) / q2


def calibrate_to_q2(D, target_q2):
    q, _rho, _beta = coefficient_profile(D)
    return scale_matrix(D, (target_q2 / q[2]) ** mp.mpf("0.25"))


def balanced_block_D(n):
    half = n // 2
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                same = (i < half and j < half) or (i >= half and j >= half)
                matrix[i][j] = mp.mpf(1) if same else mp.mpf(-1)
    return project_symmetric_zero_row(matrix)


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


def offdiag_outer_mode(signs):
    n = len(signs)
    out = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                out[i][j] = mp.mpf(signs[i]) * mp.mpf(signs[j])
    return project_symmetric_zero_row(out)


def matrix_to_mp(matrix):
    return mp.matrix([[mp.mpf(value) for value in row] for row in matrix])


def spectral_report(matrix):
    vals, _vecs = mp.eigsy(matrix_to_mp(matrix))
    vals = [mp.mpf(vals[i]) for i in range(len(vals))]
    squares = [value * value for value in vals]
    fourths = [square * square for square in squares]
    sum2 = mp.fsum(squares)
    sum4 = mp.fsum(fourths)
    return {
        "top_square_share": max(squares) / sum2 if sum2 else mp.inf,
        "participation": (sum2 * sum2 / sum4) if sum4 else mp.inf,
    }


print("=" * 80)
print("Paper 28 signed coefficient-root envelope final campaign")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 12
c = mp.mpf("0.5")
physical_sizes = [8, 10, 12, 14, 16, 18]
physical_rows = []
max_physical_beta = mp.mpf(0)
max_physical_tail = mp.mpf(0)

print("\n=== Physical all-order coefficient table at c=0.5 ===")
for n in physical_sizes:
    D = physical_delta(n, c, nodes)
    q, rho, beta = coefficient_profile(D)
    pressure = pressure_density_from_q(n, q)
    tail = tail_after_q2(q)
    max_physical_tail = max(max_physical_tail, tail)
    print(
        f"\nN={n}, row_linf={fmt(max_row_linf(D), 12)}, "
        f"pressure={fmt(pressure, 18)}, tail={fmt(tail, 18)}"
    )
    for r in range(2, n // 2 + 1):
        max_physical_beta = max(max_physical_beta, beta[r])
        physical_rows.append((n, r, q[r], rho[r], beta[r]))
        print(f"  r={r}, rho={fmt(rho[r], 18)}, q={fmt(q[r], 18)}, beta={fmt(beta[r], 18)}")

check(
    "physical all-order finite ladder passes beta<=0.65",
    max_physical_beta <= mp.mpf("0.65"),
    f"max_beta={fmt(max_physical_beta, 18)}",
)
check(
    "physical c=0.5 matching tail stays below one over the deeper ladder",
    max_physical_tail < 1,
    f"max_tail={fmt(max_physical_tail, 18)}",
)

print("\n=== Broad structural proof-route no-go adversaries ===")
n = 12
physical12 = physical_delta(n, c, nodes)
physical_q, _physical_rho, physical_beta = coefficient_profile(physical12)
physical_spectral = spectral_report(physical12)

adversary_raw = {
    "balanced_block": balanced_block_D(n),
    "fourier_rank_one": outer_kernel(fourier_vector(n, 1, "cos")),
    "three_mode_fourier": add_matrices(
        outer_kernel(fourier_vector(n, 1, "cos")),
        scale_matrix(outer_kernel(fourier_vector(n, 1, "sin")), mp.mpf("0.5")),
        scale_matrix(outer_kernel(fourier_vector(n, 2, "cos")), mp.mpf("0.25")),
    ),
}
mode_a = offdiag_outer_mode([1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1])
mode_b = offdiag_outer_mode([1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1])
mode_c = offdiag_outer_mode([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])
adversary_raw.update(
    {
        "staged_two_equal_modes": add_matrices(mode_a, mode_b),
        "staged_two_unequal_modes": add_matrices(mode_a, scale_matrix(mode_b, mp.mpf("0.65"))),
        "staged_three_tapered_modes": add_matrices(
            mode_a,
            scale_matrix(mode_b, mp.mpf("0.65")),
            scale_matrix(mode_c, mp.mpf("0.35")),
        ),
    }
)
adversary_rows = []
for name, raw in adversary_raw.items():
    D = calibrate_to_q2(raw, physical_q[2])
    q, rho, beta = coefficient_profile(D)
    pressure = pressure_density_from_q(n, q)
    tail = tail_after_q2(q)
    spectral = spectral_report(D)
    max_beta = max(beta.values())
    adversary_rows.append((name, max_beta, pressure, tail, spectral))
    print(
        f"\n{name}: row_linf={fmt(max_row_linf(D), 12)}, "
        f"max_beta={fmt(max_beta, 18)}, pressure={fmt(pressure, 18)}, tail={fmt(tail, 18)}, "
        f"top_share={fmt(spectral['top_square_share'], 18)}, participation={fmt(spectral['participation'], 18)}"
    )
    for r in range(2, n // 2 + 1):
        print(
            f"  r={r}, q/physical={fmt(q[r] / physical_q[r], 18)}, "
            f"beta={fmt(beta[r], 18)}"
        )

check(
    "q2-calibrated canonical adversaries can violate beta<=0.65",
    max(row[1] for row in adversary_rows) > mp.mpf("0.65"),
    f"max_adversary_beta={fmt(max(row[1] for row in adversary_rows), 18)}",
)
check(
    "exact signed algebra plus row-zero is insufficient",
    max(row[1] for row in adversary_rows if row[0] == "balanced_block") > mp.mpf("0.65"),
    "balanced_block is canonical and q2-calibrated",
)
check(
    "smooth Fourier origin plus q2 calibration is insufficient",
    max(row[1] for row in adversary_rows if row[0] == "fourier_rank_one") > mp.mpf("0.65"),
    "rank_one_fourier violates high-order beta",
)
check(
    "crude spectral participation is insufficient",
    any(
        row[4]["participation"] >= physical_spectral["participation"] and row[1] > mp.mpf("0.65")
        for row in adversary_rows
    ),
    f"physical_participation={fmt(physical_spectral['participation'], 18)}",
)

print("\n=== Theorem status ===")
print("FINITE SUPPORT: the physical c=0.5 all-order ladder through N=18")
print("passes the beta<=0.65 envelope.  FULL FALSIFICATION OF BROAD ROUTES:")
print("row-zero, exact signed expansion, q2 calibration, smooth Fourier origin,")
print("and crude spectral participation are not sufficient.  The remaining theorem")
print("must use a sharper physical rank-copula identity/regularity, or the record")
print("law must promote explicit subset/global sectors.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
