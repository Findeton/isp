#!/usr/bin/env python3
"""
Paper 27 receipt: Fourier/coherent-wave boundary.

Section 22 left one sharp ambiguity: Fourier/coherent-wave kernels can violate
the same matching-pressure diagnostics that reject staged blocks.  This receipt
asks whether that means pressure density is wrong, or whether coherent waves
must be treated as a separate matter/mark sector rather than as geometry.

The audit compares:

  * physical density-matched rank-copula kernels;
  * fixed staged blocks;
  * pure Fourier difference kernels;
  * Fourier bands with several modes;
  * deterministic random Fourier spectra.

It reports the pressure density

    p_N(D) = N^-1 log Z_N(D;N),

the matching tail T_N(D), and the spectral effective rank of D.  The matching
coefficients are computed by a symmetric matching-polynomial recursion:

    rho_r = r! 2^r S_r / (N)_{2r},

where S_r is the weighted undirected matching sum of size r.

This is not a theorem.  It is a hostile finite audit of the coherent-wave
boundary case exposed by the pressure-density campaign.  A high-pressure random
Fourier spectrum is a meaningful failure of the naive "all waves are safe"
story.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from functools import lru_cache
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


def max_row_linf(D):
    n = len(D)
    return max(abs(mp.fsum(D[i][j] for j in range(n) if i != j)) for i in range(n))


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


def matching_sums(D):
    n = len(D)
    full = (1 << n) - 1

    @lru_cache(maxsize=None)
    def rec(mask):
        if mask == 0:
            return (mp.mpf(1),)
        first_bit = mask & -mask
        i = first_bit.bit_length() - 1
        rest = mask ^ first_bit
        base = list(rec(rest))
        out = base + [mp.mpf(0)]
        remaining = rest
        while remaining:
            bit = remaining & -remaining
            j = bit.bit_length() - 1
            sub = rec(rest ^ bit)
            weight = D[i][j]
            if len(out) < len(sub) + 1:
                out.extend(mp.mpf(0) for _ in range(len(sub) + 1 - len(out)))
            for r, value in enumerate(sub):
                out[r + 1] += weight * value
            remaining ^= bit
        return tuple(out)

    return rec(full)


def matching_metrics(D):
    n = len(D)
    D1, original_A = normalize_A_one(D)
    sums = matching_sums(D1)
    coeffs = {}
    moments = {}
    for r in range(1, min(len(sums), n // 2 + 1)):
        rho = mp.mpf(math.factorial(r)) * (mp.mpf(2) ** r) * sums[r] / falling(n, 2 * r)
        moments[r] = rho
        coeffs[r] = mp.mpf(math.comb(n // 2, r)) * rho * rho
    q2 = coeffs.get(2, mp.mpf(0))
    tail = mp.fsum(coeffs[r] for r in coeffs if r >= 3)
    tail_ratio = tail / q2 if q2 else mp.inf
    zN = 1 + mp.fsum(coeffs[r] * (mp.mpf(n) ** r) for r in coeffs if r >= 2)
    formula_q2 = mp.mpf(math.comb(n // 2, 2)) * (
        2 / ((mp.mpf(n) - 2) * (mp.mpf(n) - 3))
    ) ** 2
    return {
        "D": D1,
        "original_A": original_A,
        "moments": moments,
        "coeffs": coeffs,
        "q2": q2,
        "formula_q2": formula_q2,
        "tail_ratio": tail_ratio,
        "pressure_density": mp.log(zN) / n,
        "row_linf": max_row_linf(D1),
    }


def spectral_metrics(D):
    n = len(D)
    eigenvalues = mp.eigsy(mp.matrix(D), eigvals_only=True)
    weights = [value * value for value in eigenvalues]
    total = mp.fsum(weights)
    probs = [weight / total for weight in weights if weight > 0]
    entropy = -mp.fsum(p * mp.log(p) for p in probs)
    effective_rank = mp.e**entropy
    top2 = mp.fsum(sorted(probs, reverse=True)[:2])
    return {
        "effective_rank": effective_rank,
        "top2_energy": top2,
    }


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


def block_D(n, blocks):
    matrix = zero_matrix(n)
    labels = [(blocks * i) // n for i in range(n)]
    off = -1 / mp.mpf(blocks - 1)
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = mp.mpf(1) if labels[i] == labels[j] else off
    return project_symmetric_zero_row(matrix)


def cosine_D(n, frequency):
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = mp.cos(2 * mp.pi * frequency * (i - j) / n)
    return project_symmetric_zero_row(matrix)


def fourier_band_D(n, width):
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            value = mp.mpf(0)
            for frequency in range(1, width + 1):
                value += mp.cos(2 * mp.pi * frequency * (i - j) / n)
            matrix[i][j] = value
    return project_symmetric_zero_row(matrix)


def random_fourier_D(n, width, seed):
    rng = random.Random(seed)
    coeffs = [mp.mpf(rng.randrange(-5, 6)) for _ in range(width)]
    if all(coeff == 0 for coeff in coeffs):
        coeffs[0] = mp.mpf(1)
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            value = mp.mpf(0)
            for idx, coeff in enumerate(coeffs, start=1):
                value += coeff * mp.cos(2 * mp.pi * idx * (i - j) / n)
            matrix[i][j] = value
    return project_symmetric_zero_row(matrix)


print("=" * 80)
print("Paper 27 Fourier/coherent-wave boundary receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 10
sizes = [8, 10, 12, 14, 16]
rows = []
max_row_after = mp.mpf(0)
max_q2_error = mp.mpf(0)

for n in sizes:
    print("\n" + "=" * 80)
    print(f"N={n}")
    print("=" * 80)
    kernels = [
        ("physical_c0.5", physical_delta_D(n, mp.mpf("0.5"), nodes) if n <= 14 else None, "physical"),
        ("block2", block_D(n, 2), "block"),
        ("block4", block_D(n, 4), "block"),
        ("cos1", cosine_D(n, 1), "pure-fourier"),
        ("cos2", cosine_D(n, 2), "pure-fourier"),
        ("band2", fourier_band_D(n, 2), "band"),
        ("band3", fourier_band_D(n, 3), "band"),
        ("randband3a", random_fourier_D(n, 3, 100 + n), "random-band"),
        ("randband4a", random_fourier_D(n, 4, 200 + n), "random-band"),
    ]
    for name, D, family in kernels:
        if D is None or axis_excess(D) == 0:
            continue
        metrics = matching_metrics(D)
        spectral = spectral_metrics(metrics["D"])
        max_row_after = max(max_row_after, metrics["row_linf"])
        max_q2_error = max(max_q2_error, abs(metrics["q2"] - metrics["formula_q2"]))
        row = {
            "n": n,
            "name": name,
            "family": family,
            **{k: v for k, v in metrics.items() if k != "D"},
            **spectral,
        }
        rows.append(row)
        print(
            f"{name:14s} family={family:12s} "
            f"T={fmt(metrics['tail_ratio'], 12)} "
            f"p={fmt(metrics['pressure_density'], 12)} "
            f"erank={fmt(spectral['effective_rank'], 12)} "
            f"top2={fmt(spectral['top2_energy'], 12)}"
        )

physical_max_pressure = max(row["pressure_density"] for row in rows if row["family"] == "physical")
pure_fourier_max_pressure = max(row["pressure_density"] for row in rows if row["family"] == "pure-fourier")
band_min_pressure = min(row["pressure_density"] for row in rows if row["family"] == "band")
block_min_pressure = min(row["pressure_density"] for row in rows if row["family"] == "block")
random_band_max_pressure = max(row["pressure_density"] for row in rows if row["family"] == "random-band")
random_band_min_pressure = min(row["pressure_density"] for row in rows if row["family"] == "random-band")
cos1_sequence = [row for row in rows if row["name"] == "cos1"]
band3_sequence = [row for row in rows if row["name"] == "band3"]
pure_fourier_min_erank = min(row["effective_rank"] for row in rows if row["family"] == "pure-fourier")
band_max_erank = max(row["effective_rank"] for row in rows if row["family"] == "band")
random_band_max_erank = max(row["effective_rank"] for row in rows if row["family"] == "random-band")
worst_wave = max((row for row in rows if row["family"] in ("pure-fourier", "band", "random-band")), key=lambda row: row["pressure_density"])
best_band = min((row for row in rows if row["family"] == "band"), key=lambda row: row["pressure_density"])

print("\n=== Summary ===")
print(f"physical_max_pressure = {fmt(physical_max_pressure, 18)}")
print(f"pure_fourier_max_pressure = {fmt(pure_fourier_max_pressure, 18)}")
print(f"band_min_pressure = {fmt(band_min_pressure, 18)}")
print(f"block_min_pressure = {fmt(block_min_pressure, 18)}")
print(f"random_band_max_pressure = {fmt(random_band_max_pressure, 18)}")
print(f"random_band_min_pressure = {fmt(random_band_min_pressure, 18)}")
print(f"pure_fourier_min_erank = {fmt(pure_fourier_min_erank, 18)}")
print(f"band_max_erank = {fmt(band_max_erank, 18)}")
print(f"random_band_max_erank = {fmt(random_band_max_erank, 18)}")
print(
    "cos1 pressure sequence = "
    + ", ".join(f"N={row['n']}:{fmt(row['pressure_density'], 12)}" for row in cos1_sequence)
)
print(
    "band3 pressure sequence = "
    + ", ".join(f"N={row['n']}:{fmt(row['pressure_density'], 12)}" for row in band3_sequence)
)
print(
    "worst wave = "
    f"N={worst_wave['n']} {worst_wave['name']} p={fmt(worst_wave['pressure_density'], 18)}"
)
print(
    "best Fourier band = "
    f"N={best_band['n']} {best_band['name']} p={fmt(best_band['pressure_density'], 18)}"
)

check(
    "zero-row projection is enforced",
    max_row_after < mp.mpf("1e-80"),
    f"max_row_after={fmt(max_row_after, 18)}",
)
check(
    "universal q2 coefficient is reproduced",
    max_q2_error < mp.mpf("1e-80"),
    f"max_q2_error={fmt(max_q2_error, 18)}",
)
check(
    "pure Fourier modes can exceed the physical pressure envelope",
    pure_fourier_max_pressure > physical_max_pressure,
    f"pure_fourier_max={fmt(pure_fourier_max_pressure, 12)} physical_max={fmt(physical_max_pressure, 12)}",
)
check(
    "Fourier bands can fall back below the block pressure floor",
    band_min_pressure < block_min_pressure,
    f"band_min={fmt(band_min_pressure, 12)} block_min={fmt(block_min_pressure, 12)}",
)
check(
    "spectral spreading increases effective rank",
    band_max_erank > pure_fourier_min_erank and random_band_max_erank > pure_fourier_min_erank,
    f"pure_min={fmt(pure_fourier_min_erank, 12)} band_max={fmt(band_max_erank, 12)} "
    f"rand_max={fmt(random_band_max_erank, 12)}",
)
check(
    "cos1 pressure is not a finite N=8 accident",
    cos1_sequence[-1]["pressure_density"] > cos1_sequence[0]["pressure_density"],
    f"N8={fmt(cos1_sequence[0]['pressure_density'], 12)} "
    f"N16={fmt(cos1_sequence[-1]['pressure_density'], 12)}",
)
check(
    "random Fourier spectra straddle the staged-block pressure floor",
    random_band_min_pressure < block_min_pressure and random_band_max_pressure > block_min_pressure,
    f"random_min={fmt(random_band_min_pressure, 12)} random_max={fmt(random_band_max_pressure, 12)} "
    f"block_min={fmt(block_min_pressure, 12)}",
)

print("\n=== Consequence ===")
print("The Fourier boundary is real.  Pure low-frequency coherent modes can")
print("exceed the physical pressure envelope and the effect is not confined to")
print("N=8.  Fourier bands can fall below the staged-block floor when spectral")
print("mass is spread, but random Fourier spectra can also exceed that floor.")
print("Therefore pressure density should not be a naked ban on coherent modes,")
print("nor should all coherent modes be admitted.  The likely rule is sectoral:")
print("geometry kernels must stay subcritical, while coherent wave structure is")
print("admissible only with explicit matter/mark degrees of freedom and")
print("spectral-spread or field-energy bookkeeping.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
