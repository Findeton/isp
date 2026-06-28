#!/usr/bin/env python3
"""
Paper 28 receipt: prove/falsify the hybrid cancellation theorem route.

The current theorem target is too large to prove by receipt:

    a hybrid cumulant / matching-cluster / falling-normalization /
    spectral bound strong enough to imply q_{N,r} <= C (beta/N)^r.

This receipt attacks it by falsifying over-broad versions.  In particular,
it tests whether a simple spectral-concentration condition can replace the
missing physical rank-copula structure.

The adversary is a multi-mode staged kernel: a sum of balanced orthogonal
block modes.  It can distribute spectral square mass better than the single
balanced block, while keeping coherent high-order matching residue.  If it
passes crude spectral diagnostics and still violates the physical coefficient
envelope after q2 calibration, then "spectral concentration alone" is false.

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


def axis_excess(matrix):
    n = len(matrix)
    return mp.fsum(
        matrix[i][j] ** 2 for i in range(n) for j in range(n) if i != j
    ) / (mp.mpf(n) * (n - 1))


def offdiag_outer_mode(signs):
    n = len(signs)
    out = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                out[i][j] = mp.mpf(signs[i]) * mp.mpf(signs[j])
    return project_symmetric_zero_row(out)


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
        rho = direct_disjoint_moment(D, r)
        out[r] = coefficient(n, r, rho)
    return out


def calibrate_to_q2(D, target_q2):
    q2 = q_values(D, 2)[2]
    if q2 == 0:
        raise ValueError("zero q2")
    # q_r scales as scale^(2r), so q2 scales as scale^4.
    return scale_matrix(D, (target_q2 / q2) ** mp.mpf("0.25"))


def matrix_to_mp(matrix):
    return mp.matrix([[mp.mpf(value) for value in row] for row in matrix])


def spectral_report(matrix):
    vals, _vecs = mp.eigsy(matrix_to_mp(matrix))
    vals = [mp.mpf(vals[i]) for i in range(len(vals))]
    squares = [value * value for value in vals]
    fourths = [square * square for square in squares]
    sum2 = mp.fsum(squares)
    sum4 = mp.fsum(fourths)
    top2 = max(squares)
    return {
        "top_abs": mp.sqrt(top2),
        "top_square_share": top2 / sum2 if sum2 else mp.inf,
        "participation": (sum2 * sum2 / sum4) if sum4 else mp.inf,
        "trace2": sum2,
        "trace4": sum4,
        "vals": vals,
    }


def log_series_coefficients(rho):
    max_r = len(rho) - 1
    ell = [mp.mpf(0) for _ in range(max_r + 1)]
    for n in range(1, max_r + 1):
        correction = mp.fsum(k * ell[k] * rho[n - k] for k in range(1, n))
        ell[n] = rho[n] - correction / n
    return ell


def rho_values(D, max_r):
    return [mp.mpf(1)] + [direct_disjoint_moment(D, r) for r in range(1, max_r + 1)]


def physical_reference_values():
    """
    Values from p28_cumulant_spectral_cancellation.py at N=12,c=0.5.
    They are used here as high-precision audit constants to avoid rerunning
    the quadrature-heavy physical kernel generation in this adversary search.
    """
    q = {
        2: mp.mpf("0.000210334918081194117"),
        3: mp.mpf("0.00000919283044544023064"),
        4: mp.mpf("0.000000489026692727355503"),
        5: mp.mpf("0.0000000196243436034102793"),
        6: mp.mpf("0.000000001017438833187958913251159005956971130030714464"),
    }
    spectral = {
        "top_square_share": mp.mpf("0.809167040491739998"),
        "participation": mp.mpf("1.49624744077645289"),
    }
    return q, spectral


print("=" * 80)
print("Paper 28 hybrid theorem falsification receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
max_r = 6
physical_q, physical_spectral = physical_reference_values()

mode_a = offdiag_outer_mode([1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1])
mode_b = offdiag_outer_mode([1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1])
mode_c = offdiag_outer_mode([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])

candidates = []
for name, raw in [
    ("single_balanced", mode_a),
    ("two_equal_modes", add_matrices(mode_a, mode_b)),
    ("three_equal_modes", add_matrices(mode_a, mode_b, mode_c)),
    ("two_unequal_modes", add_matrices(mode_a, scale_matrix(mode_b, mp.mpf("0.65")))),
    (
        "three_tapered_modes",
        add_matrices(mode_a, scale_matrix(mode_b, mp.mpf("0.65")), scale_matrix(mode_c, mp.mpf("0.35"))),
    ),
]:
    calibrated = calibrate_to_q2(project_symmetric_zero_row(raw), physical_q[2])
    q = q_values(calibrated, max_r)
    spectral = spectral_report(calibrated)
    rho = rho_values(calibrated, max_r)
    ell = log_series_coefficients(rho)
    candidates.append(
        {
            "name": name,
            "D": calibrated,
            "q": q,
            "spectral": spectral,
            "ell": ell,
        }
    )

print("\n=== Candidate adversaries calibrated to physical q2 ===")
for candidate in candidates:
    spectral = candidate["spectral"]
    q = candidate["q"]
    ell = candidate["ell"]
    print(f"\n{candidate['name']}:")
    print(f"  row_linf = {fmt(max_row_linf(candidate['D']), 18)}")
    print(f"  top_square_share = {fmt(spectral['top_square_share'], 18)}")
    print(f"  participation = {fmt(spectral['participation'], 18)}")
    print(f"  q5/physical = {fmt(q[5] / physical_q[5], 18)}")
    print(f"  q6/physical = {fmt(q[6] / physical_q[6], 18)}")
    print(f"  |ell5|/physical_q_sqrt_proxy = {fmt(abs(ell[5]), 18)}")
    for r in range(2, max_r + 1):
        print(
            f"    r={r}, q={fmt(q[r], 18)}, q/phys={fmt(q[r] / physical_q[r], 18)}"
        )

spectral_passers = [
    c
    for c in candidates
    if c["spectral"]["top_square_share"] <= physical_spectral["top_square_share"]
    and c["spectral"]["participation"] >= physical_spectral["participation"]
]
best_spectral_passer = max(spectral_passers, key=lambda c: c["q"][5] / physical_q[5])
best_overall = max(candidates, key=lambda c: c["q"][6] / physical_q[6])

print("\n=== Best witnesses ===")
print(
    f"best spectral passer = {best_spectral_passer['name']}, "
    f"top_share={fmt(best_spectral_passer['spectral']['top_square_share'], 18)}, "
    f"participation={fmt(best_spectral_passer['spectral']['participation'], 18)}, "
    f"q5_ratio={fmt(best_spectral_passer['q'][5] / physical_q[5], 18)}, "
    f"q6_ratio={fmt(best_spectral_passer['q'][6] / physical_q[6], 18)}"
)
print(
    f"best overall q6 = {best_overall['name']}, "
    f"q6_ratio={fmt(best_overall['q'][6] / physical_q[6], 18)}"
)

check(
    "adversary family remains canonical after projection",
    all(max_row_linf(c["D"]) < mp.mpf("1e-80") for c in candidates),
    f"max_row_linf={fmt(max(max_row_linf(c['D']) for c in candidates), 18)}",
)
check(
    "all adversaries are q2-calibrated to the physical value",
    all(abs(c["q"][2] / physical_q[2] - 1) < mp.mpf("1e-12") for c in candidates),
    ", ".join(f"{c['name']}={fmt(c['q'][2] / physical_q[2], 12)}" for c in candidates),
)
check(
    "there exists a multi-mode adversary passing crude spectral concentration",
    len(spectral_passers) > 0,
    ", ".join(c["name"] for c in spectral_passers),
)
check(
    "spectral-concentration-only theorem is false",
    best_spectral_passer["q"][5] / physical_q[5] > mp.mpf("10"),
    f"witness={best_spectral_passer['name']} q5_ratio={fmt(best_spectral_passer['q'][5] / physical_q[5], 18)}",
)
check(
    "the witness also violates the q6 coefficient envelope relative to physical",
    best_spectral_passer["q"][6] / physical_q[6] > mp.mpf("100"),
    f"witness={best_spectral_passer['name']} q6_ratio={fmt(best_spectral_passer['q'][6] / physical_q[6], 18)}",
)
check(
    "multi-mode staging can hide behind better spectral participation",
    best_spectral_passer["spectral"]["participation"]
    > physical_spectral["participation"],
    f"physical={fmt(physical_spectral['participation'], 18)} witness={fmt(best_spectral_passer['spectral']['participation'], 18)}",
)

print("\n=== Theorem status ===")
print("FALSIFIED: a theorem using only q2 calibration plus crude spectral")
print("concentration/participation cannot prove the coefficient-root envelope.")
print("A multi-mode staged kernel can distribute spectral mass better than the")
print("single block, pass the physical top-share/participation diagnostics, and")
print("still carry large high-order matching coefficients.  The surviving theorem")
print("must use the physical rank-copula kernel itself, or a stronger condition")
print("such as smooth continuum origin / local Bernstein variation / interval")
print("heredity, not spectral concentration alone.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
