#!/usr/bin/env python3
"""
Paper 27 receipt: matching/free-energy separator.

The previous receipt showed that zero-row neutrality plus bounded one-pair
energy is too weak: a balanced staged block passes the exact two-factor test
but creates coherent high-order matching residue.

This receipt promotes the full matching/free-energy object to the diagnostic.
For a symmetric zero-row ordered-pair matrix D, first normalize

    A(D) = (1/(N(N-1))) sum_{i != j} D_ij^2 = 1.

Then compute disjoint matching coefficients

    q_r(D) = binom(N/2,r) rho_r(D)^2,
    rho_r(D) = (1/(N)_{2r}) sum_{all endpoints distinct} prod_k D_{a_k b_k}.

The two-factor coefficient q_2 is universal under this normalization.  The
new proposed regularity object is therefore the normalized matching tail

    T_N(D) = (sum_{r >= 3} q_r(D)) / q_2(D),

or equivalently the generating/free-energy function

    Z_N(D;z) = 1 + sum_{r >= 2} q_r(D) z^r.

The receipt tests physical rank-copula kernels, staged blocks, multiblocks,
hierarchical blocks, Fourier kernels, sparse blocks, projected random kernels,
and physical-plus-block mixtures.

It also runs a focused N=12 contamination scan.  If a tiny block admixture
stays below the physical envelope, the result should not be oversold as an
"any trace of staging" detector.  It is a macroscopic staged/fiber detector.

This is not a theorem.  It is a hostile finite campaign to see whether the
matching tail is a better law-candidate than any one- or two-factor scalar.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict
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


def matching_coefficients(D):
    n = len(D)
    moments = disjoint_moments(D)
    coeffs = {}
    for r, rho in moments.items():
        coeffs[r] = mp.mpf(math.comb(n // 2, r)) * rho * rho
    return coeffs, moments


def matching_metrics(D):
    n = len(D)
    D1, original_A = normalize_A_one(D)
    coeffs, moments = matching_coefficients(D1)
    q2 = coeffs.get(2, mp.mpf(0))
    tail = mp.fsum(coeffs[r] for r in coeffs if r >= 3)
    tail_ratio = tail / q2 if q2 else mp.inf
    max_tail_ratio = max((coeffs[r] / q2 for r in coeffs if r >= 3), default=mp.mpf(0))
    z1 = 1 + mp.fsum(coeffs[r] for r in coeffs if r >= 2)
    zN = 1 + mp.fsum(coeffs[r] * (mp.mpf(n) ** r) for r in coeffs if r >= 2)
    formula_q2 = mp.mpf(math.comb(n // 2, 2)) * (
        2 / ((mp.mpf(n) - 2) * (mp.mpf(n) - 3))
    ) ** 2
    return {
        "D": D1,
        "original_A": original_A,
        "coeffs": coeffs,
        "moments": moments,
        "q2": q2,
        "formula_q2": formula_q2,
        "tail": tail,
        "tail_ratio": tail_ratio,
        "max_tail_ratio": max_tail_ratio,
        "logZ1": mp.log(z1),
        "logZN": mp.log(zN),
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


def balanced_block_D(n):
    half = n // 2
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                same = (i < half and j < half) or (i >= half and j >= half)
                matrix[i][j] = mp.mpf(1) if same else mp.mpf(-1)
    return project_symmetric_zero_row(matrix)


def multiblock_D(n, blocks):
    matrix = zero_matrix(n)
    labels = [(blocks * i) // n for i in range(n)]
    off = -1 / mp.mpf(blocks - 1)
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = mp.mpf(1) if labels[i] == labels[j] else off
    return project_symmetric_zero_row(matrix)


def hierarchical_D(n):
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            half_same = (i < n // 2 and j < n // 2) or (i >= n // 2 and j >= n // 2)
            quarter_same = (4 * i) // n == (4 * j) // n
            matrix[i][j] = (mp.mpf(1) if half_same else mp.mpf(-1)) + (
                mp.mpf("0.5") if quarter_same else mp.mpf("-0.5")
            )
    return project_symmetric_zero_row(matrix)


def cosine_D(n, frequency):
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = mp.cos(2 * mp.pi * frequency * (i - j) / n)
    return project_symmetric_zero_row(matrix)


def sparse_cycle_blocks_D(n):
    matrix = zero_matrix(n)
    for base in range(0, n - 3, 4):
        edges = [
            (base, base + 1, 1),
            (base + 1, base, 1),
            (base, base + 2, -1),
            (base + 2, base, -1),
            (base + 1, base + 3, -1),
            (base + 3, base + 1, -1),
            (base + 2, base + 3, 1),
            (base + 3, base + 2, 1),
        ]
        for i, j, value in edges:
            matrix[i][j] = mp.mpf(value)
    return project_symmetric_zero_row(matrix)


def random_projected_D(n, seed):
    rng = random.Random(seed)
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(i + 1, n):
            value = mp.mpf(rng.randrange(-7, 8))
            matrix[i][j] = value
            matrix[j][i] = value
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


def suite(n):
    out = [
        ("block2", balanced_block_D(n), "hostile"),
        ("block4", multiblock_D(n, 4), "hostile"),
        ("hierarchical", hierarchical_D(n), "hostile"),
        ("cos1", cosine_D(n, 1), "structured"),
        ("cos2", cosine_D(n, 2 if n > 6 else 1), "structured"),
        ("sparse4", sparse_cycle_blocks_D(n), "structured"),
        ("rand11", random_projected_D(n, 11 + n), "random"),
        ("rand29", random_projected_D(n, 29 + n), "random"),
    ]
    if n <= 12:
        physical = physical_delta_D(n, mp.mpf("0.5"), 12)
        block = balanced_block_D(n)
        out.extend(
            [
                ("physical_c0.5", physical, "physical"),
                ("physical_c1", physical_delta_D(n, mp.mpf("1"), 12), "physical"),
                ("physical_c2", physical_delta_D(n, mp.mpf("2"), 12), "physical"),
                ("mix_phys_block_0.05", combine_projected(physical, block, mp.mpf("0.05")), "mixture"),
                ("mix_phys_block_0.10", combine_projected(physical, block, mp.mpf("0.10")), "mixture"),
                ("mix_phys_block_0.25", combine_projected(physical, block, mp.mpf("0.25")), "mixture"),
            ]
        )
    return out


print("=" * 80)
print("Paper 27 matching/free-energy separator receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

sizes = [8, 10, 12]
rows = []
max_row_after = mp.mpf(0)
max_q2_error = mp.mpf(0)

for n in sizes:
    print("\n" + "=" * 80)
    print(f"N={n}")
    print("=" * 80)
    for name, D, family in suite(n):
        if axis_excess(D) == 0:
            continue
        metrics = matching_metrics(D)
        max_row_after = max(max_row_after, metrics["row_linf"])
        max_q2_error = max(max_q2_error, abs(metrics["q2"] - metrics["formula_q2"]))
        row = {
            "n": n,
            "name": name,
            "family": family,
            **{k: v for k, v in metrics.items() if k != "D"},
        }
        rows.append(row)
        coeff_detail = ", ".join(
            f"q{r}={fmt(metrics['coeffs'][r], 6)}" for r in sorted(metrics["coeffs"]) if r >= 2
        )
        print(
            f"{name:22s} family={family:10s} "
            f"T={fmt(metrics['tail_ratio'], 12)} "
            f"maxTail/q2={fmt(metrics['max_tail_ratio'], 12)} "
            f"logZ1={fmt(metrics['logZ1'], 12)} "
            f"logZN={fmt(metrics['logZN'], 12)} "
            f"{coeff_detail}"
        )

def max_where(predicate, key):
    return max((row[key] for row in rows if predicate(row)), default=mp.mpf(0))


def min_where(predicate, key):
    values = [row[key] for row in rows if predicate(row)]
    return min(values) if values else mp.inf


physical_max_tail = max_where(lambda row: row["family"] == "physical", "tail_ratio")
hostile_min_tail = min_where(lambda row: row["family"] == "hostile", "tail_ratio")
block2_max_tail = max_where(lambda row: row["name"] == "block2", "tail_ratio")
physical_max_logZN = max_where(lambda row: row["family"] == "physical", "logZN")
hostile_min_logZN = min_where(lambda row: row["family"] == "hostile", "logZN")
structured_max_tail = max_where(lambda row: row["family"] == "structured", "tail_ratio")
random_max_tail = max_where(lambda row: row["family"] == "random", "tail_ratio")

mixture_rows = [
    row for row in rows if row["n"] == 12 and row["name"].startswith("mix_phys_block")
]
mixture_tail_sequence = [row["tail_ratio"] for row in sorted(mixture_rows, key=lambda row: row["name"])]

worst_tail = max(rows, key=lambda row: row["tail_ratio"])
worst_logZN = max(rows, key=lambda row: row["logZN"])
best_physical = max((row for row in rows if row["family"] == "physical"), key=lambda row: row["tail_ratio"])

print("\n=== Separator summary ===")
print(f"physical_max_tail = {fmt(physical_max_tail, 18)}")
print(f"hostile_min_tail = {fmt(hostile_min_tail, 18)}")
print(f"block2_max_tail = {fmt(block2_max_tail, 18)}")
print(f"structured_max_tail = {fmt(structured_max_tail, 18)}")
print(f"random_max_tail = {fmt(random_max_tail, 18)}")
print(f"physical_max_logZN = {fmt(physical_max_logZN, 18)}")
print(f"hostile_min_logZN = {fmt(hostile_min_logZN, 18)}")
print(
    "worst_tail = "
    f"N={worst_tail['n']} {worst_tail['name']} T={fmt(worst_tail['tail_ratio'], 18)}"
)
print(
    "worst_logZN = "
    f"N={worst_logZN['n']} {worst_logZN['name']} logZN={fmt(worst_logZN['logZN'], 18)}"
)
print(
    "largest physical tail = "
    f"N={best_physical['n']} {best_physical['name']} T={fmt(best_physical['tail_ratio'], 18)}"
)
print(
    "N=12 mixture tail sequence = "
    + ", ".join(fmt(value, 18) for value in mixture_tail_sequence)
)

scan_lambdas = [
    mp.mpf("0"),
    mp.mpf("0.05"),
    mp.mpf("0.10"),
    mp.mpf("0.125"),
    mp.mpf("0.15"),
    mp.mpf("0.20"),
    mp.mpf("0.25"),
    mp.mpf("0.50"),
]
scan_physical = physical_delta_D(12, mp.mpf("0.5"), 12)
scan_block = balanced_block_D(12)
scan_rows = []
for lam in scan_lambdas:
    mixed = combine_projected(scan_physical, scan_block, lam)
    metrics = matching_metrics(mixed)
    scan_rows.append((lam, metrics["tail_ratio"], metrics["logZN"]))

crossing = next((lam for lam, tail, _ in scan_rows if tail > physical_max_tail), None)
print("N=12 block-contamination scan against global physical envelope:")
for lam, tail, logZN in scan_rows:
    print(f"  lambda={fmt(lam, 8)} T={fmt(tail, 18)} logZN={fmt(logZN, 18)}")
print(f"first lambda above physical envelope = {fmt(crossing, 18) if crossing is not None else 'none'}")

check(
    "zero-row projection is enforced",
    max_row_after < mp.mpf("1e-80"),
    f"max_row_after={fmt(max_row_after, 18)}",
)
check(
    "universal two-factor coefficient is reproduced",
    max_q2_error < mp.mpf("1e-80"),
    f"max_q2_error={fmt(max_q2_error, 18)}",
)
check(
    "matching tail separates staged blocks from physical kernels in this audit",
    hostile_min_tail > physical_max_tail,
    f"hostile_min_tail={fmt(hostile_min_tail, 12)} physical_max_tail={fmt(physical_max_tail, 12)}",
)
check(
    "balanced two-block has large matching-tail amplification",
    block2_max_tail > mp.mpf("50"),
    f"block2_max_tail={fmt(block2_max_tail, 12)}",
)
check(
    "physical kernels remain subcritical by tail ratio",
    physical_max_tail < mp.mpf("5"),
    f"physical_max_tail={fmt(physical_max_tail, 12)}",
)
check(
    "physical kernels remain below hostile pressure at z=N",
    hostile_min_logZN > physical_max_logZN,
    f"hostile_min_logZN={fmt(hostile_min_logZN, 12)} physical_max_logZN={fmt(physical_max_logZN, 12)}",
)
check(
    "random projected matrices are not automatically rejected like staged blocks",
    random_max_tail < hostile_min_tail,
    f"random_max_tail={fmt(random_max_tail, 12)} hostile_min_tail={fmt(hostile_min_tail, 12)}",
)
check(
    "physical-plus-block tail increases with block contamination at N=12",
    all(scan_rows[i][1] < scan_rows[i + 1][1] for i in range(len(scan_rows) - 1)),
    ", ".join(fmt(value, 12) for _, value, _ in scan_rows),
)
check(
    "small staged admixture can remain below the finite physical envelope",
    scan_rows[2][1] < physical_max_tail and scan_rows[-2][1] > physical_max_tail,
    f"lambda0.10={fmt(scan_rows[2][1], 12)} "
    f"lambda0.25={fmt(scan_rows[-2][1], 12)} "
    f"physical_envelope={fmt(physical_max_tail, 12)}",
)

print("\n=== Consequence ===")
print("The finite separator that survives this audit is not q2, A, or stable")
print("rank.  It is the matching tail/free-energy profile.  In the tested range")
print("the physical rank-copula stays below the staged block tail, while the")
print("balanced and hierarchical staged kernels are rejected by high-order")
print("matching coefficients even though q2 is universal.  The contamination")
print("scan also shows that tiny staged admixtures can sit below the finite")
print("physical envelope, so the candidate law should be phrased as a")
print("macroscopic staged/fiber regularity condition, not as an infinitesimal")
print("trace detector.  This suggests subcritical matching pressure, or a")
print("projective finite-dimensional law whose coefficients imply that pressure")
print("bound.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
