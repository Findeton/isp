#!/usr/bin/env python3
"""
Paper 28 receipt: smooth/local theorem campaign.

After the spectral-only theorem was falsified, the next target was:

    maybe q2 calibration + smooth continuum origin + local variation control
    is enough to force the coefficient-root envelope.

This receipt attacks that broader smooth/local target.  It constructs
low-frequency Fourier kernels on the rank lattice.  These are smooth
continuum-origin kernels rather than staged block kernels.  They are projected
to the same row-zero canonical class and calibrated to the physical q2 value.

If such smooth kernels have no worse local variation than the physical
rank-copula but still have much larger high-order q_r, then smoothness/local
variation alone is also false.  The surviving target must include the actual
physical rank-copula shape or a stronger recursive/calibrated law, not merely
smooth continuum origin.

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
    rho = {}
    for r in range(2, max_r + 1):
        rho[r] = direct_disjoint_moment(D, r)
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


def local_metrics(D):
    n = len(D)
    first = mp.mpf(0)
    second = mp.mpf(0)
    count_first = 0
    count_second = 0
    max_abs = mp.mpf(0)
    for i in range(n):
        for j in range(n):
            if i != j:
                max_abs = max(max_abs, abs(D[i][j]))
            if i + 1 < n and i != j and i + 1 != j:
                first += abs(D[i + 1][j] - D[i][j])
                count_first += 1
            if j + 1 < n and i != j and i != j + 1:
                first += abs(D[i][j + 1] - D[i][j])
                count_first += 1
            if i + 2 < n and i != j and i + 1 != j and i + 2 != j:
                second += abs(D[i + 2][j] - 2 * D[i + 1][j] + D[i][j])
                count_second += 1
            if j + 2 < n and i != j and i != j + 1 and i != j + 2:
                second += abs(D[i][j + 2] - 2 * D[i][j + 1] + D[i][j])
                count_second += 1
    return {
        "first_tv": first / count_first,
        "second_tv": second / count_second,
        "max_abs": max_abs,
    }


def matrix_to_mp(matrix):
    return mp.matrix([[mp.mpf(value) for value in row] for row in matrix])


def spectral_report(D):
    vals, _vecs = mp.eigsy(matrix_to_mp(D))
    vals = [mp.mpf(vals[i]) for i in range(len(vals))]
    squares = [value * value for value in vals]
    fourths = [square * square for square in squares]
    sum2 = mp.fsum(squares)
    sum4 = mp.fsum(fourths)
    top2 = max(squares)
    return {
        "top_square_share": top2 / sum2,
        "participation": sum2 * sum2 / sum4,
    }


print("=" * 80)
print("Paper 28 smooth/local theorem campaign")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
max_r = 6
physical = physical_delta(n, mp.mpf("0.5"), 12)
physical_q, physical_rho = q_values(physical, max_r)
physical_local = local_metrics(physical)
physical_spectral = spectral_report(physical)

vectors = {
    "cos1": fourier_vector(n, 1, "cos"),
    "sin1": fourier_vector(n, 1, "sin"),
    "cos2": fourier_vector(n, 2, "cos"),
    "sin2": fourier_vector(n, 2, "sin"),
}

seed_candidates = [
    ("fourier_cos1", outer_kernel(vectors["cos1"])),
    ("fourier_sin1", outer_kernel(vectors["sin1"])),
    ("fourier_two_mode", add_matrices(outer_kernel(vectors["cos1"]), outer_kernel(vectors["sin1"]))),
    (
        "fourier_tapered_low",
        add_matrices(
            outer_kernel(vectors["cos1"]),
            scale_matrix(outer_kernel(vectors["sin1"]), mp.mpf("0.75")),
            scale_matrix(outer_kernel(vectors["cos2"]), mp.mpf("0.35")),
        ),
    ),
]

raw_candidates = list(seed_candidates)
grid = [mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.75"), mp.mpf("1.0"), mp.mpf("1.5")]
for a in grid:
    for b in grid:
        for c in [mp.mpf("0"), mp.mpf("0.5"), mp.mpf("1.0")]:
            if a == 0 and b == 0 and c == 0:
                continue
            raw = add_matrices(
                outer_kernel(vectors["cos1"]),
                scale_matrix(outer_kernel(vectors["sin1"]), a),
                scale_matrix(outer_kernel(vectors["cos2"]), b),
                scale_matrix(outer_kernel(vectors["sin2"]), c),
            )
            raw_candidates.append((f"grid_a{fmt(a,3)}_b{fmt(b,3)}_c{fmt(c,3)}", raw))

rows = []
print("\n=== Physical reference ===")
print(f"row_linf = {fmt(max_row_linf(physical), 18)}")
print(f"first_tv = {fmt(physical_local['first_tv'], 18)}")
print(f"second_tv = {fmt(physical_local['second_tv'], 18)}")
print(f"top_square_share = {fmt(physical_spectral['top_square_share'], 18)}")
print(f"participation = {fmt(physical_spectral['participation'], 18)}")
for r in range(2, max_r + 1):
    print(f"  r={r}, q={fmt(physical_q[r], 18)}")

print("\n=== Smooth Fourier adversaries calibrated to physical q2 ===")
for name, raw in raw_candidates:
    D = calibrate_to_q2(raw, physical_q[2])
    q, rho = q_values(D, max_r)
    local = local_metrics(D)
    spectral = spectral_report(D)
    row = {"name": name, "D": D, "q": q, "rho": rho, "local": local, "spectral": spectral}
    rows.append(row)
    if name in {candidate_name for candidate_name, _raw in seed_candidates}:
        print(f"\n{name}:")
        print(f"  row_linf = {fmt(max_row_linf(D), 18)}")
        print(f"  first_tv/physical = {fmt(local['first_tv'] / physical_local['first_tv'], 18)}")
        print(f"  second_tv/physical = {fmt(local['second_tv'] / physical_local['second_tv'], 18)}")
        print(f"  top_square_share = {fmt(spectral['top_square_share'], 18)}")
        print(f"  participation = {fmt(spectral['participation'], 18)}")
        for r in range(2, max_r + 1):
            print(
                f"    r={r}, q={fmt(q[r], 18)}, q/phys={fmt(q[r] / physical_q[r], 18)}"
            )

local_passers = [
    row
    for row in rows
    if row["local"]["first_tv"] <= mp.mpf("2.5") * physical_local["first_tv"]
    and row["local"]["second_tv"] <= mp.mpf("2.5") * physical_local["second_tv"]
]
best_local = max(local_passers, key=lambda row: row["q"][6] / physical_q[6])

smooth_spectral_passers = [
    row
    for row in rows
    if row["spectral"]["top_square_share"] <= physical_spectral["top_square_share"]
    and row["spectral"]["participation"] >= physical_spectral["participation"]
]
best_smooth_spectral = max(
    smooth_spectral_passers, key=lambda row: row["q"][6] / physical_q[6]
)

smooth_joint_passers = [
    row
    for row in smooth_spectral_passers
    if row["local"]["first_tv"] <= mp.mpf("2.5") * physical_local["first_tv"]
    and row["local"]["second_tv"] <= mp.mpf("2.5") * physical_local["second_tv"]
]
best_joint = max(smooth_joint_passers, key=lambda row: row["q"][6] / physical_q[6])

print("\n=== Best smooth witnesses ===")
print(
    f"best order-one local passer = {best_local['name']}, "
    f"q5_ratio={fmt(best_local['q'][5] / physical_q[5], 18)}, "
    f"q6_ratio={fmt(best_local['q'][6] / physical_q[6], 18)}, "
    f"first_tv_ratio={fmt(best_local['local']['first_tv'] / physical_local['first_tv'], 18)}, "
    f"second_tv_ratio={fmt(best_local['local']['second_tv'] / physical_local['second_tv'], 18)}"
)
print(
    f"best smooth spectral passer = {best_smooth_spectral['name']}, "
    f"q5_ratio={fmt(best_smooth_spectral['q'][5] / physical_q[5], 18)}, "
    f"q6_ratio={fmt(best_smooth_spectral['q'][6] / physical_q[6], 18)}"
)
print(
    f"best joint local+spectral passer = {best_joint['name']}, "
    f"q5_ratio={fmt(best_joint['q'][5] / physical_q[5], 18)}, "
    f"q6_ratio={fmt(best_joint['q'][6] / physical_q[6], 18)}, "
    f"first_tv_ratio={fmt(best_joint['local']['first_tv'] / physical_local['first_tv'], 18)}, "
    f"second_tv_ratio={fmt(best_joint['local']['second_tv'] / physical_local['second_tv'], 18)}, "
    f"top_share={fmt(best_joint['spectral']['top_square_share'], 18)}, "
    f"participation={fmt(best_joint['spectral']['participation'], 18)}"
)

check(
    "smooth adversaries remain canonical after projection",
    all(max_row_linf(row["D"]) < mp.mpf("1e-80") for row in rows),
    f"max_row_linf={fmt(max(max_row_linf(row['D']) for row in rows), 18)}",
)
check(
    "smooth adversaries are q2-calibrated to physical",
    all(abs(row["q"][2] / physical_q[2] - 1) < mp.mpf("1e-12") for row in rows),
    f"count={len(rows)} max_error={fmt(max(abs(row['q'][2] / physical_q[2] - 1) for row in rows), 18)}",
)
check(
    "there exists a Fourier adversary with order-one local variation",
    len(local_passers) > 0,
    f"count={len(local_passers)}",
)
check(
    "smooth order-one local-variation theorem is false",
    best_local["q"][5] / physical_q[5] > mp.mpf("10"),
    f"witness={best_local['name']} q5_ratio={fmt(best_local['q'][5] / physical_q[5], 18)}",
)
check(
    "the smooth local witness also violates q6 strongly",
    best_local["q"][6] / physical_q[6] > mp.mpf("100"),
    f"witness={best_local['name']} q6_ratio={fmt(best_local['q'][6] / physical_q[6], 18)}",
)
check(
    "there exists a smooth Fourier adversary passing crude spectral diagnostics",
    len(smooth_spectral_passers) > 0,
    f"count={len(smooth_spectral_passers)}",
)
check(
    "smooth spectral theorem is not strongly falsified by q5 in this search",
    best_smooth_spectral["q"][5] / physical_q[5] < mp.mpf("10"),
    f"witness={best_smooth_spectral['name']} q5_ratio={fmt(best_smooth_spectral['q'][5] / physical_q[5], 18)}",
)
check(
    "smooth joint local+spectral theorem survives this finite search",
    best_joint["q"][5] / physical_q[5] < mp.mpf("10")
    and best_joint["q"][6] / physical_q[6] < mp.mpf("100"),
    f"witness={best_joint['name']} q5_ratio={fmt(best_joint['q'][5] / physical_q[5], 18)} "
    f"q6_ratio={fmt(best_joint['q'][6] / physical_q[6], 18)}",
)

print("\n=== Theorem status ===")
print("FALSIFIED: q2 calibration plus smooth low-frequency continuum origin plus")
print("order-one local variation bounds is not enough.  Low-frequency Fourier")
print("kernels can have modest local variation and still carry much larger")
print("high-order matching coefficients.  NOT FALSIFIED HERE: adding crude")
print("spectral diffusion to the smooth/local test.  The next target is therefore")
print("smooth + spectral + recursive interval heredity / calibrated finite-")
print("dimensional shape, not generic smoothness alone.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
