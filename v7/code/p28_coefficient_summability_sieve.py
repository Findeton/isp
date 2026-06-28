#!/usr/bin/env python3
"""
Paper 28 receipt: coefficient-level polymer summability sieve.

Paper 28 separated two objects:

    pressure density:      N^{-1} log Z_N(D; N),
    washout summability:   Z_N(D; 1) - 1 = sum_r q_r(D).

This receipt attacks the second object directly for the physical
density-matched rank-copula residue.  It does not prove the theorem.  It
extracts the theorem shape:

    q_{N,r} <= C (beta / N)^r

on the actual, unnormalized coefficient scale.  Such an envelope immediately
gives Z_N(1)-1 = O(N^{-2}) and therefore coefficient-level washout.

The receipt also checks the hostile opening: a staged block calibrated to the
same q_2 scale can still carry a larger high-order profile.  That is why the
law needs both coefficient-level summability and sectoral pressure/regularity.

All asserted non-integer arithmetic uses mpmath with dps=140.
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


def axis_excess(D):
    n = len(D)
    return mp.fsum(D[i][j] ** 2 for i in range(n) for j in range(n) if i != j) / (
        mp.mpf(n) * (n - 1)
    )


def normalize_A_one(D):
    A = axis_excess(D)
    if A == 0:
        raise ValueError("zero matrix")
    scale = 1 / mp.sqrt(A)
    n = len(D)
    return [[scale * D[i][j] for j in range(n)] for i in range(n)], A


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


def balanced_block_D(n):
    half = n // 2
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                same = (i < half and j < half) or (i >= half and j >= half)
                matrix[i][j] = mp.mpf(1) if same else mp.mpf(-1)
    return project_symmetric_zero_row(matrix)


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


def disjoint_moments(D, max_r=None):
    n = len(D)
    if max_r is None:
        max_r = n // 2
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


def coefficient_profile(D, max_r=None):
    n = len(D)
    moments = disjoint_moments(D, max_r=max_r)
    coeffs = {}
    for r, rho in moments.items():
        coeffs[r] = mp.mpf(math.comb(n // 2, r)) * rho * rho
    return coeffs, moments


def profile_stats(n, coeffs):
    z1_minus_1 = mp.fsum(coeffs[r] for r in coeffs if r >= 2)
    beta_eff = max(
        (mp.mpf(n) * (abs(coeffs[r]) ** (mp.mpf(1) / r)) for r in coeffs if r >= 2),
        default=mp.mpf(0),
    )
    tail_after_2 = mp.fsum(coeffs[r] for r in coeffs if r >= 3)
    q2 = coeffs.get(2, mp.mpf(0))
    tail_fraction = tail_after_2 / z1_minus_1 if z1_minus_1 else mp.mpf(0)
    return {
        "z1_minus_1": z1_minus_1,
        "n2_z1": mp.mpf(n) ** 2 * z1_minus_1,
        "beta_eff": beta_eff,
        "q2": q2,
        "tail_after_2": tail_after_2,
        "tail_fraction": tail_fraction,
    }


def scale_coeffs(coeffs, scale):
    return {r: coeffs[r] * (scale ** (2 * r)) for r in coeffs}


print("=" * 80)
print("Paper 28 coefficient-level polymer summability sieve")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 12
sizes = [8, 10, 12, 14, 16]
cs = [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")]
max_r = 6

rows = []
max_row_after = mp.mpf(0)

print("\n=== Physical coefficient profiles ===")
for n in sizes:
    local_cs = cs if n <= 14 else [mp.mpf("0.5")]
    for c in local_cs:
        D = physical_delta(n, c, nodes)
        max_row_after = max(max_row_after, max_row_linf(D))
        coeffs, moments = coefficient_profile(D, max_r=max_r)
        stats = profile_stats(n, coeffs)
        row = {
            "n": n,
            "c": c,
            "coeffs": coeffs,
            **stats,
        }
        rows.append(row)
        coeff_text = " ".join(
            f"q{r}={fmt(coeffs[r], 12)}" for r in sorted(coeffs) if r >= 2
        )
        print(
            f"N={n:2d} c={fmt(c, 6):>8s} "
            f"Z1-1={fmt(stats['z1_minus_1'], 18)} "
            f"N^2Z={fmt(stats['n2_z1'], 18)} "
            f"beta_eff={fmt(stats['beta_eff'], 18)} "
            f"tailFrac={fmt(stats['tail_fraction'], 18)} "
            f"{coeff_text}"
        )

max_beta = max(row["beta_eff"] for row in rows)
max_n2_z1 = max(row["n2_z1"] for row in rows)
max_tail_fraction = max(row["tail_fraction"] for row in rows)
worst_beta = max(rows, key=lambda row: row["beta_eff"])
worst_n2z = max(rows, key=lambda row: row["n2_z1"])

c05_rows = [row for row in rows if row["c"] == mp.mpf("0.5")]
c05_rows.sort(key=lambda row: row["n"])

print("\n=== Envelope summary ===")
print(f"max_row_after = {fmt(max_row_after, 18)}")
print(
    "max beta_eff = "
    f"N={worst_beta['n']} c={fmt(worst_beta['c'], 6)} beta={fmt(max_beta, 18)}"
)
print(
    "max N^2(Z1-1) = "
    f"N={worst_n2z['n']} c={fmt(worst_n2z['c'], 6)} value={fmt(max_n2_z1, 18)}"
)
print(f"max tail fraction after q2 = {fmt(max_tail_fraction, 18)}")
print(
    "c=0.5 Z1 ladder = "
    + ", ".join(f"N={row['n']}:{fmt(row['z1_minus_1'], 14)}" for row in c05_rows)
)

print("\n=== Calibrated staged-block stress test ===")
target = next(row for row in rows if row["n"] == 12 and row["c"] == mp.mpf("0.5"))
block_D, block_original_A = normalize_A_one(balanced_block_D(12))
block_coeffs_A1, _ = coefficient_profile(block_D, max_r=6)
physical_q2 = target["q2"]
block_q2_A1 = block_coeffs_A1[2]
scale_to_physical_q2 = (physical_q2 / block_q2_A1) ** mp.mpf("0.25")
block_coeffs_scaled = scale_coeffs(block_coeffs_A1, scale_to_physical_q2)
block_stats_scaled = profile_stats(12, block_coeffs_scaled)
physical_stats = profile_stats(12, target["coeffs"])

print(f"physical N=12 c=0.5 q2 = {fmt(physical_q2, 18)}")
print(f"A=1 block q2 = {fmt(block_q2_A1, 18)}")
print(f"block scale matching physical q2 = {fmt(scale_to_physical_q2, 18)}")
print(f"physical Z1-1 = {fmt(physical_stats['z1_minus_1'], 18)}")
print(f"calibrated block Z1-1 = {fmt(block_stats_scaled['z1_minus_1'], 18)}")
print(f"physical beta_eff = {fmt(physical_stats['beta_eff'], 18)}")
print(f"calibrated block beta_eff = {fmt(block_stats_scaled['beta_eff'], 18)}")
for r in sorted(block_coeffs_scaled):
    if r < 2:
        continue
    phys = target["coeffs"].get(r, mp.mpf(0))
    block = block_coeffs_scaled[r]
    ratio = block / phys if phys else mp.inf
    print(f"r={r} calibrated_block/physical = {fmt(ratio, 18)}")

envelope_beta = mp.mpf("0.65")
envelope_C = mp.mpf("1")
envelope_violations = []
for row in rows:
    n = mp.mpf(row["n"])
    for r, q in row["coeffs"].items():
        if r < 2:
            continue
        bound = envelope_C * (envelope_beta / n) ** r
        if q > bound:
            envelope_violations.append((row["n"], row["c"], r, q, bound))

check(
    "physical zero-row projection is enforced",
    max_row_after < mp.mpf("1e-80"),
    f"max_row_after={fmt(max_row_after, 18)}",
)
check(
    "finite physical profiles fit a beta/N coefficient envelope",
    not envelope_violations,
    f"C={fmt(envelope_C)} beta={fmt(envelope_beta)} max_beta_eff={fmt(max_beta, 18)}",
)
check(
    "physical Z_N(1)-1 has bounded N^2 scale in the audited grid",
    max_n2_z1 < mp.mpf("0.05"),
    f"max_N2Z={fmt(max_n2_z1, 18)}",
)
check(
    "physical c=0.5 Z_N(1)-1 decreases over the N ladder",
    all(c05_rows[i]["z1_minus_1"] > c05_rows[i + 1]["z1_minus_1"] for i in range(len(c05_rows) - 1)),
    ", ".join(fmt(row["z1_minus_1"], 12) for row in c05_rows),
)
check(
    "higher physical coefficients are a small correction to q2",
    max_tail_fraction < mp.mpf("0.07"),
    f"max_tail_fraction={fmt(max_tail_fraction, 18)}",
)
check(
    "q2-calibrated staged block carries larger high-order mass",
    block_stats_scaled["tail_after_2"] > 5 * physical_stats["tail_after_2"],
    f"block_tail={fmt(block_stats_scaled['tail_after_2'], 18)} "
    f"physical_tail={fmt(physical_stats['tail_after_2'], 18)}",
)
check(
    "finite Z1 alone is weaker than the coefficient envelope",
    block_stats_scaled["z1_minus_1"] < 2 * physical_stats["z1_minus_1"]
    and block_stats_scaled["beta_eff"] > 5 * physical_stats["beta_eff"],
    f"block_Z/physical_Z={fmt(block_stats_scaled['z1_minus_1'] / physical_stats['z1_minus_1'], 18)} "
    f"block_beta/physical_beta={fmt(block_stats_scaled['beta_eff'] / physical_stats['beta_eff'], 18)}",
)
check(
    "q2 calibration alone does not guarantee the beta/N envelope",
    block_stats_scaled["beta_eff"] > envelope_beta,
    f"block_beta={fmt(block_stats_scaled['beta_eff'], 18)} beta_guard={fmt(envelope_beta)}",
)

print("\n=== Theorem shape extracted ===")
print("If one can prove q_{N,r} <= C (beta/N)^r for the physical rank-copula")
print("with beta bounded independently of N and c in the admissible window, then")
print("Z_N(1)-1 is O(N^-2) and the labeled coefficient-level washout follows.")
print("The finite receipt supports this theorem shape but does not prove it.")
print("The q2-calibrated block stress test says the proof cannot use q2 alone;")
print("it needs canonical-kernel/U-statistic degeneracy plus a regularity condition")
print("that excludes coherent staged/fiber contractions.")

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
