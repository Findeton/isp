#!/usr/bin/env python3
"""
Paper 27 receipt: physical matching-pressure scaling and tuned adversaries.

The previous receipt identified the normalized matching tail

    T_N(D) = (sum_{r >= 3} q_r(D)) / q_2(D)

as a better candidate regularity object than one-pair energy, q2, or stable
rank.  This receipt follows the two next openings and then tests whether the
tail alone survives.  It does not: a wide-jitter small-N physical corner and a
tuned four-block force the stronger pressure-density diagnostic.

  1. Extend the physical density-matched rank-copula audit in N and c.
  2. Search tuned staged/fiber adversaries: fixed multiblocks, hierarchical
     blocks, and physical-plus-block mixtures.

The pressure diagnostic also records

    p_N(D) = log Z_N(D;N) / N,

because raw log Z_N(D;N) grows with N even for physical kernels.

This is not a theorem.  It is a high-precision finite campaign designed to
decide what the theorem should try to prove.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict
import math
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
    for depth in range(1, n // 2 + 1):
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


def matching_metrics(D):
    n = len(D)
    D1, original_A = normalize_A_one(D)
    moments = disjoint_moments(D1)
    coeffs = {
        r: mp.mpf(math.comb(n // 2, r)) * rho * rho
        for r, rho in moments.items()
    }
    q2 = coeffs.get(2, mp.mpf(0))
    tail = mp.fsum(coeffs[r] for r in coeffs if r >= 3)
    tail_ratio = tail / q2 if q2 else mp.inf
    zN = 1 + mp.fsum(coeffs[r] * (mp.mpf(n) ** r) for r in coeffs if r >= 2)
    logZN = mp.log(zN)
    formula_q2 = mp.mpf(math.comb(n // 2, 2)) * (
        2 / ((mp.mpf(n) - 2) * (mp.mpf(n) - 3))
    ) ** 2
    return {
        "original_A": original_A,
        "D": D1,
        "coeffs": coeffs,
        "q2": q2,
        "formula_q2": formula_q2,
        "tail_ratio": tail_ratio,
        "logZN": logZN,
        "pressure_density": logZN / n,
        "row_linf": max_row_linf(D1),
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


def hierarchical_D(n, weight):
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            half_same = (i < n // 2 and j < n // 2) or (i >= n // 2 and j >= n // 2)
            quarter_same = (4 * i) // n == (4 * j) // n
            matrix[i][j] = (mp.mpf(1) if half_same else mp.mpf(-1)) + mp.mpf(weight) * (
                mp.mpf(1) if quarter_same else mp.mpf(-1) / 3
            )
    return project_symmetric_zero_row(matrix)


def cosine_D(n, frequency):
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = mp.cos(2 * mp.pi * frequency * (i - j) / n)
    return project_symmetric_zero_row(matrix)


def combine_projected(D0, D1, lam):
    n = len(D0)
    A0, _ = normalize_A_one(D0)
    A1, _ = normalize_A_one(D1)
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = A0[i][j] + mp.mpf(lam) * A1[i][j]
    return project_symmetric_zero_row(matrix)


print("=" * 80)
print("Paper 27 physical pressure scaling and tuned-adversary receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 10
sizes = [8, 10, 12, 14]
cs = [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")]
physical_rows = []
adversary_rows = []
max_row_after = mp.mpf(0)
max_q2_error = mp.mpf(0)

print("\n(1) Physical rank-copula pressure scaling")
for c in cs:
    print("\n" + "=" * 80)
    print(f"c={fmt(c, 8)}")
    print("=" * 80)
    for n in sizes:
        metrics = matching_metrics(physical_delta_D(n, c, nodes))
        max_row_after = max(max_row_after, metrics["row_linf"])
        max_q2_error = max(max_q2_error, abs(metrics["q2"] - metrics["formula_q2"]))
        row = {"n": n, "c": c, **metrics}
        physical_rows.append(row)
        print(
            f"N={n} T={fmt(metrics['tail_ratio'], 18)} "
            f"logZN/N={fmt(metrics['pressure_density'], 18)} "
            f"q2={fmt(metrics['q2'], 12)} "
            f"qmax={fmt(max(metrics['coeffs'].values()), 12)}"
        )

print("\n(2) Tuned fixed-block and hierarchical adversaries")
for n in sizes:
    print("\n" + "=" * 80)
    print(f"N={n}")
    print("=" * 80)
    candidates = []
    for blocks in [2, 3, 4]:
        candidates.append((f"block{blocks}", block_D(n, blocks), "fixed-block"))
    for weight in [mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")]:
        candidates.append((f"hier_w{fmt(weight,4)}", hierarchical_D(n, weight), "hierarchical"))
    candidates.append(("cos1", cosine_D(n, 1), "structured"))
    candidates.append(("cos2", cosine_D(n, 2 if n > 6 else 1), "structured"))
    for name, D, family in candidates:
        if axis_excess(D) == 0:
            continue
        metrics = matching_metrics(D)
        max_row_after = max(max_row_after, metrics["row_linf"])
        max_q2_error = max(max_q2_error, abs(metrics["q2"] - metrics["formula_q2"]))
        adversary_rows.append({"n": n, "name": name, "family": family, **metrics})
        print(
            f"{name:10s} family={family:12s} "
            f"T={fmt(metrics['tail_ratio'], 18)} "
            f"logZN/N={fmt(metrics['pressure_density'], 18)}"
        )

print("\n(3) Physical-plus-block contamination threshold")
contamination_rows = []
for n in sizes:
    physical = physical_delta_D(n, mp.mpf("0.5"), nodes)
    block = block_D(n, 2)
    print("\n" + "=" * 80)
    print(f"N={n}")
    print("=" * 80)
    for lam in [mp.mpf("0"), mp.mpf("0.05"), mp.mpf("0.10"), mp.mpf("0.125"), mp.mpf("0.15"), mp.mpf("0.20"), mp.mpf("0.25"), mp.mpf("0.50")]:
        metrics = matching_metrics(combine_projected(physical, block, lam))
        max_row_after = max(max_row_after, metrics["row_linf"])
        max_q2_error = max(max_q2_error, abs(metrics["q2"] - metrics["formula_q2"]))
        contamination_rows.append({"n": n, "lambda": lam, **metrics})
        print(
            f"lambda={fmt(lam, 8)} T={fmt(metrics['tail_ratio'], 18)} "
            f"logZN/N={fmt(metrics['pressure_density'], 18)}"
        )

physical_by_c = {
    c: [row for row in physical_rows if row["c"] == c]
    for c in cs
}
physical_max_tail = max(row["tail_ratio"] for row in physical_rows)
physical_max_density = max(row["pressure_density"] for row in physical_rows)
physical_max_tail_excluding_wide_corner = max(
    row["tail_ratio"]
    for row in physical_rows
    if not (row["n"] == 8 and row["c"] == mp.mpf("4"))
)
physical_c05 = physical_by_c[mp.mpf("0.5")]
fixed_block_rows = [row for row in adversary_rows if row["family"] in ("fixed-block", "hierarchical")]
fixed_block_min_tail = min(row["tail_ratio"] for row in fixed_block_rows)
fixed_block_min_density = min(row["pressure_density"] for row in fixed_block_rows)
structured_max_tail = max(row["tail_ratio"] for row in adversary_rows if row["family"] == "structured")
structured_max_density = max(row["pressure_density"] for row in adversary_rows if row["family"] == "structured")
worst_physical = max(physical_rows, key=lambda row: row["tail_ratio"])
stealth_fixed = min(fixed_block_rows, key=lambda row: row["tail_ratio"])
stealth_fixed_density = min(fixed_block_rows, key=lambda row: row["pressure_density"])

thresholds = {}
density_thresholds = {}
for n in sizes:
    seq = [row for row in contamination_rows if row["n"] == n]
    crossing = next((row["lambda"] for row in seq if row["tail_ratio"] > physical_max_tail), None)
    thresholds[n] = crossing
    density_crossing = next(
        (row["lambda"] for row in seq if row["pressure_density"] > physical_max_density),
        None,
    )
    density_thresholds[n] = density_crossing

print("\n=== Summary ===")
print(
    "physical c=0.5 T sequence = "
    + ", ".join(fmt(row["tail_ratio"], 18) for row in physical_c05)
)
print(f"physical_max_tail = {fmt(physical_max_tail, 18)}")
print(f"physical_max_tail_excluding_wide_corner = {fmt(physical_max_tail_excluding_wide_corner, 18)}")
print(f"physical_max_logZN_over_N = {fmt(physical_max_density, 18)}")
print(f"fixed_block_min_tail = {fmt(fixed_block_min_tail, 18)}")
print(f"fixed_block_min_logZN_over_N = {fmt(fixed_block_min_density, 18)}")
print(f"structured_max_tail = {fmt(structured_max_tail, 18)}")
print(f"structured_max_logZN_over_N = {fmt(structured_max_density, 18)}")
print(
    "worst physical = "
    f"N={worst_physical['n']} c={fmt(worst_physical['c'], 8)} "
    f"T={fmt(worst_physical['tail_ratio'], 18)}"
)
print(
    "stealthiest fixed adversary = "
    f"N={stealth_fixed['n']} {stealth_fixed['name']} "
    f"T={fmt(stealth_fixed['tail_ratio'], 18)}"
)
print(
    "least-pressure fixed adversary = "
    f"N={stealth_fixed_density['n']} {stealth_fixed_density['name']} "
    f"logZN/N={fmt(stealth_fixed_density['pressure_density'], 18)}"
)
print(
    "tail crossings above physical envelope = "
    + ", ".join(f"N={n}: {fmt(thresholds[n], 12) if thresholds[n] is not None else 'none'}" for n in sizes)
)
print(
    "density crossings above physical envelope = "
    + ", ".join(
        f"N={n}: {fmt(density_thresholds[n], 12) if density_thresholds[n] is not None else 'none'}"
        for n in sizes
    )
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
    "physical c=0.5 tail decreases over tested N",
    all(physical_c05[i]["tail_ratio"] > physical_c05[i + 1]["tail_ratio"] for i in range(len(physical_c05) - 1)),
    ", ".join(fmt(row["tail_ratio"], 12) for row in physical_c05),
)
check(
    "physical wide-jitter corner is the only tested tail above one",
    physical_max_tail > mp.mpf("1")
    and physical_max_tail_excluding_wide_corner < mp.mpf("0.7"),
    f"physical_max_tail={fmt(physical_max_tail, 12)} "
    f"excluding_corner={fmt(physical_max_tail_excluding_wide_corner, 12)}",
)
check(
    "all physical pressure densities stay below 0.7",
    physical_max_density < mp.mpf("0.7"),
    f"physical_max_density={fmt(physical_max_density, 12)}",
)
check(
    "tail alone fails against tuned fixed blocks",
    fixed_block_min_tail < physical_max_tail,
    f"fixed_min_tail={fmt(fixed_block_min_tail, 12)} physical_max_tail={fmt(physical_max_tail, 12)}",
)
check(
    "pressure density separates fixed macroscopic staged adversaries",
    fixed_block_min_density > physical_max_density,
    f"fixed_min_density={fmt(fixed_block_min_density, 12)} physical_max_density={fmt(physical_max_density, 12)}",
)
check(
    "structured Fourier adversaries can violate both pressure diagnostics",
    structured_max_tail > physical_max_tail and structured_max_density > physical_max_density,
    f"structured_tail={fmt(structured_max_tail, 12)} structured_density={fmt(structured_max_density, 12)}",
)
check(
    "pressure density detects N=12 contamination at finite threshold",
    density_thresholds[12] is not None
    and density_thresholds[12] > mp.mpf("0.10")
    and density_thresholds[12] <= mp.mpf("0.20"),
    f"N12_density_crossing={fmt(density_thresholds[12], 12)}",
)

print("\n=== Consequence ===")
print("The physical rank-copula tail decreases with N at c=0.5, but tail alone")
print("is not the final law: a wide-jitter N=8 corner raises the physical tail,")
print("and a tuned four-block can have low tail.  Pressure density logZ_N(D;N)/N")
print("is stronger in this finite audit: it keeps the tested physical kernels")
print("below 0.7 while every fixed macroscopic staged block sits above that")
print("envelope.  Fourier-like structured kernels can still violate the pressure")
print("envelope, so the next theory question is whether such coherent wave")
print("kernels are admissible matterlike structure or another non-manifold stage.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
