#!/usr/bin/env python3
"""
Paper 28 receipt: recursive interval heredity campaign.

Previous receipts falsified:

  * spectral concentration alone;
  * smooth low-frequency origin plus order-one local variation.

The smooth + crude spectral test was not falsified by the finite Fourier
search.  The next target is recursive interval heredity: a candidate kernel
should not merely look controlled globally; its contiguous rank windows should
renormalize to the same calibrated finite-dimensional profile as physical
rank-copula kernels of that smaller size.

This receipt tests the strongest surviving Fourier witnesses from the smooth
campaign.  It restricts them to contiguous windows, projects to row-zero
canonical form, calibrates q2 to the physical window q2, and audits the
higher-q profile.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

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


def offdiag_sum(matrix):
    n = len(matrix)
    return mp.fsum(matrix[i][j] for i in range(n) for j in range(n) if i != j)


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
            value = coeff * low_pow * (between ** (b - a - 1)) * (
                above ** (n - 1 - b)
            )
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


def q_values(D, max_r):
    n = len(D)
    out = {}
    for r in range(2, max_r + 1):
        out[r] = coefficient(n, r, direct_disjoint_moment(D, r))
    return out


def calibrate_to_q2(D, target_q2):
    q = q_values(D, 2)
    if q[2] == 0:
        raise ValueError("zero q2")
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


def restrict_window(D, start, size):
    raw = zero_matrix(size)
    for i in range(size):
        for j in range(size):
            if i != j:
                raw[i][j] = D[start + i][start + j]
    return project_symmetric_zero_row(raw)


def q_profile_error(candidate, physical, size):
    max_r = size // 2
    phys_q = q_values(physical, max_r)
    calibrated = calibrate_to_q2(candidate, phys_q[2])
    cand_q = q_values(calibrated, max_r)
    ratios = {r: cand_q[r] / phys_q[r] for r in range(2, max_r + 1)}
    log_error = max(abs(mp.log(ratios[r])) for r in ratios if ratios[r] > 0)
    return ratios, log_error


print("=" * 80)
print("Paper 28 recursive interval heredity campaign")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
c = mp.mpf("0.5")
nodes = 12
physical12 = physical_delta(n, c, nodes)
physical_by_size = {size: physical_delta(size, c, nodes) for size in [8, 10, 12]}

vectors = {
    "cos1": fourier_vector(n, 1, "cos"),
    "sin1": fourier_vector(n, 1, "sin"),
    "cos2": fourier_vector(n, 2, "cos"),
    "sin2": fourier_vector(n, 2, "sin"),
}

candidate_raw = {
    "fourier_cos1_local_bad": outer_kernel(vectors["cos1"]),
    "fourier_joint_survivor": add_matrices(
        outer_kernel(vectors["cos1"]), scale_matrix(outer_kernel(vectors["sin1"]), mp.mpf("0.5"))
    ),
    "fourier_spectral_survivor": add_matrices(
        outer_kernel(vectors["cos1"]), scale_matrix(outer_kernel(vectors["sin2"]), mp.mpf("0.5"))
    ),
}

grid = [mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.75"), mp.mpf("1.0"), mp.mpf("1.5")]
for a in grid:
    for b in grid:
        for c_grid in [mp.mpf("0"), mp.mpf("0.5"), mp.mpf("1.0")]:
            if a == 0 and b == 0 and c_grid == 0:
                continue
            candidate_raw[f"grid_a{fmt(a,3)}_b{fmt(b,3)}_c{fmt(c_grid,3)}"] = add_matrices(
                outer_kernel(vectors["cos1"]),
                scale_matrix(outer_kernel(vectors["sin1"]), a),
                scale_matrix(outer_kernel(vectors["cos2"]), b),
                scale_matrix(outer_kernel(vectors["sin2"]), c_grid),
            )

physical12_q = q_values(physical12, n // 2)
candidates = {
    name: calibrate_to_q2(raw, physical12_q[2]) for name, raw in candidate_raw.items()
}

print("\n=== Global profiles ===")
global_rows = {}
for name, D in candidates.items():
    q = q_values(D, n // 2)
    ratios = {r: q[r] / physical12_q[r] for r in range(2, n // 2 + 1)}
    global_rows[name] = ratios
    if name.startswith("fourier_"):
        print(f"\n{name}:")
        print(f"  row_linf = {fmt(max_row_linf(D), 18)}")
        for r, ratio in ratios.items():
            print(f"  r={r}, q/physical={fmt(ratio, 18)}")

print("\n=== Recursive window profile errors ===")
window_rows = {}
for name, D in candidates.items():
    worst = {"error": mp.mpf("-1"), "size": None, "start": None, "ratios": None}
    if name.startswith("fourier_"):
        print(f"\n{name}:")
    for size in [8, 10]:
        for start in range(0, n - size + 1):
            window = restrict_window(D, start, size)
            ratios, error = q_profile_error(window, physical_by_size[size], size)
            if error > worst["error"]:
                worst = {"error": error, "size": size, "start": start, "ratios": ratios}
        if name.startswith("fourier_"):
            print(
                f"  size={size}, worst_so_far_error={fmt(worst['error'], 18)} "
                f"at start={worst['start']}"
            )
    window_rows[name] = worst
    ratio_text = ", ".join(
        f"r{r}={fmt(value, 12)}" for r, value in sorted(worst["ratios"].items())
    )
    if name.startswith("fourier_"):
        print(
            f"  worst window size={worst['size']} start={worst['start']} "
            f"log_error={fmt(worst['error'], 18)} ratios=({ratio_text})"
        )

worst_survivor_name = max(
    ["fourier_joint_survivor", "fourier_spectral_survivor"],
    key=lambda name: window_rows[name]["error"],
)

screened = []
for name in candidates:
    q5 = global_rows[name][5]
    q6 = global_rows[name][6]
    error = window_rows[name]["error"]
    screened.append((name, q5, q6, error))

best_window_passer = min(screened, key=lambda row: row[3])
best_high_q_under_one = max(
    [row for row in screened if row[3] <= mp.mpf("1.0")],
    key=lambda row: row[2],
    default=None,
)
high_q_candidates = [row for row in screened if row[1] > 10 or row[2] > 100]
high_q_min_error = min(row[3] for row in high_q_candidates)

print("\n=== Grid heredity screen summary ===")
print(
    f"best window passer = {best_window_passer[0]}, "
    f"log_error={fmt(best_window_passer[3], 18)}, "
    f"q5_ratio={fmt(best_window_passer[1], 18)}, "
    f"q6_ratio={fmt(best_window_passer[2], 18)}"
)
if best_high_q_under_one is None:
    print("no candidate with heredity log_error <= 1.0 has high q6 in the audited grid")
else:
    print(
        f"best q6 under log_error<=1 = {best_high_q_under_one[0]}, "
        f"log_error={fmt(best_high_q_under_one[3], 18)}, "
        f"q5_ratio={fmt(best_high_q_under_one[1], 18)}, "
        f"q6_ratio={fmt(best_high_q_under_one[2], 18)}"
    )
print(f"min heredity error among high-q candidates = {fmt(high_q_min_error, 18)}")

check(
    "candidate kernels remain canonical after projection",
    all(max_row_linf(D) < mp.mpf("1e-80") for D in candidates.values()),
    f"max_row_linf={fmt(max(max_row_linf(D) for D in candidates.values()), 18)}",
)
check(
    "global smooth survivors are q2 calibrated",
    all(abs(global_rows[name][2] - 1) < mp.mpf("1e-12") for name in candidates),
    f"count={len(candidates)} max_error={fmt(max(abs(global_rows[name][2] - 1) for name in candidates), 18)}",
)
check(
    "recursive heredity rejects the locally bad Fourier mode",
    window_rows["fourier_cos1_local_bad"]["error"] > mp.mpf("2.0"),
    f"log_error={fmt(window_rows['fourier_cos1_local_bad']['error'], 18)}",
)
check(
    "recursive heredity rejects at least one smooth spectral survivor",
    window_rows[worst_survivor_name]["error"] > mp.mpf("1.0"),
    f"witness={worst_survivor_name} log_error={fmt(window_rows[worst_survivor_name]['error'], 18)}",
)
check(
    "audited high-q Fourier candidates fail the recursive heredity screen",
    high_q_min_error > mp.mpf("1.0"),
    f"min_high_q_error={fmt(high_q_min_error, 18)}",
)
check(
    "no audited heredity passer has a large coefficient explosion",
    best_high_q_under_one is None
    or (best_high_q_under_one[1] < mp.mpf("10") and best_high_q_under_one[2] < mp.mpf("100")),
    "none" if best_high_q_under_one is None else (
        f"witness={best_high_q_under_one[0]} q5={fmt(best_high_q_under_one[1], 18)} "
        f"q6={fmt(best_high_q_under_one[2], 18)}"
    ),
)

print("\n=== Theorem status ===")
print("NOT FALSIFIED HERE: recursive contiguous-window heredity rejects every")
print("audited high-q low-frequency Fourier candidate.  This is still only a")
print("finite proxy, not a theorem.  The next target is the full calibrated")
print("finite-dimensional projective law of interval interiors.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
