#!/usr/bin/env python3
"""
Paper 29 receipt: cycle determinant surrogate.

For canonical row-zero kernels, the without-replacement matching coefficient
has a partition-lattice expansion.  Its leading fixed-r contribution comes
from 2-regular quotient graphs: cycles.  The exponential formula for cycles
predicts the reciprocal determinant surrogate

    C_N(z;D) = det(I + 2 z D/N)^(-1).

Equivalently,

    log C_N(z;D) = -Tr log(I + 2 z D/N)
                 = sum_{k>=1} (-1)^k 2^k Tr((D/N)^k) z^k / k.

If this is the right asymptotic shadow, then the scaled coefficients

    a_{N,r} = N^r rho_{N,r}

should start by following the coefficients of C_N(z;D) for low fixed r.  This
receipt tests and falsifies the stronger claim that the naive determinant is
already the full finite object.  The opening it leaves is a labelled cycle-index
determinant with the exact falling-factor inflation and non-cycle remainder.

All non-integer arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

from p29_matching_lib import (
    add_matrices,
    balanced_block_D,
    calibrate_to_q2,
    coefficient_profile,
    fmt,
    fourier_vector,
    max_row_linf,
    outer_kernel,
    physical_delta,
    reciprocal_determinant_coefficients,
    scale_matrix,
    scaled_matching_coefficients,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def relative_error(actual, predicted):
    denom = max(mp.mpf("1e-80"), abs(actual), abs(predicted))
    return abs(actual - predicted) / denom


print("=" * 80)
print("Paper 29 cycle determinant surrogate")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

sizes = [8, 10, 12, 14, 16, 18]
fixed_r_cap = 6
physical_rows = []
max_physical_fixed_error = mp.mpf(0)
max_physical_r2_error = mp.mpf(0)
max_physical_r3_error = mp.mpf(0)

print("\n=== Physical c=0.5: scaled rho versus det(I+2zD/N)^-1 ===")
for n in sizes:
    D = physical_delta(n, mp.mpf("0.5"), nodes=12)
    scaled = scaled_matching_coefficients(D)
    det_coeff, traces, _log_coeff = reciprocal_determinant_coefficients(D, n // 2)
    row_errors = []
    print(f"\nN={n}, row_linf={fmt(max_row_linf(D), 12)}")
    for r in range(2, min(fixed_r_cap, n // 2) + 1):
        err = relative_error(scaled[r], det_coeff[r])
        row_errors.append(err)
        max_physical_fixed_error = max(max_physical_fixed_error, err)
        if r == 2:
            max_physical_r2_error = max(max_physical_r2_error, err)
        if r == 3:
            max_physical_r3_error = max(max_physical_r3_error, err)
        print(
            f"  r={r}, N^r rho={fmt(scaled[r], 18)}, "
            f"det_coeff={fmt(det_coeff[r], 18)}, rel_error={fmt(err, 18)}"
        )
    physical_rows.append((n, max(row_errors), row_errors[-1]))

first_r2_error = relative_error(
    scaled_matching_coefficients(physical_delta(8, mp.mpf("0.5"), nodes=12))[2],
    reciprocal_determinant_coefficients(physical_delta(8, mp.mpf("0.5"), nodes=12), 4)[0][2],
)
last_r2_error = relative_error(
    scaled_matching_coefficients(physical_delta(18, mp.mpf("0.5"), nodes=12))[2],
    reciprocal_determinant_coefficients(physical_delta(18, mp.mpf("0.5"), nodes=12), 9)[0][2],
)

print("\n=== Adversarial calibration at N=12 ===")
n = 12
physical = physical_delta(n, mp.mpf("0.5"), nodes=12)
target_q, _rho, _beta = coefficient_profile(physical)
cos1 = outer_kernel(fourier_vector(n, 1, "cos"))
sin1 = outer_kernel(fourier_vector(n, 1, "sin"))
cos2 = outer_kernel(fourier_vector(n, 2, "cos"))
adversaries = {
    "balanced_block": calibrate_to_q2(balanced_block_D(n), target_q[2]),
    "rank_one_fourier": calibrate_to_q2(cos1, target_q[2]),
    "three_mode_fourier": calibrate_to_q2(
        add_matrices(cos1, scale_matrix(sin1, mp.mpf("0.5")), scale_matrix(cos2, mp.mpf("0.25"))),
        target_q[2],
    ),
}

max_adversary_fixed_error = mp.mpf(0)
for name, D in adversaries.items():
    scaled = scaled_matching_coefficients(D)
    det_coeff, _traces, _log_coeff = reciprocal_determinant_coefficients(D, n // 2)
    q, _rho, beta = coefficient_profile(D)
    print(f"\n{name}: max_beta={fmt(max(beta.values()), 18)}")
    for r in range(2, n // 2 + 1):
        err = relative_error(scaled[r], det_coeff[r])
        max_adversary_fixed_error = max(max_adversary_fixed_error, err)
        print(
            f"  r={r}, N^r rho={fmt(scaled[r], 18)}, "
            f"det_coeff={fmt(det_coeff[r], 18)}, rel_error={fmt(err, 18)}"
        )

check(
    "naive reciprocal determinant has the correct r=2 convergence direction",
    last_r2_error < first_r2_error and last_r2_error < mp.mpf("0.4"),
    f"r2_error_N8={fmt(first_r2_error, 18)} r2_error_N18={fmt(last_r2_error, 18)}",
)
check(
    "naive reciprocal determinant is falsified as the full finite coefficient object",
    max_physical_fixed_error > mp.mpf("0.95"),
    f"max_fixed_error={fmt(max_physical_fixed_error, 18)}",
)
check(
    "determinant surrogate is universal, not a physical theorem by itself",
    max_adversary_fixed_error < mp.mpf("2.0"),
    f"max_adversary_fixed_error={fmt(max_adversary_fixed_error, 18)}",
)
check(
    "high beta adversaries remain high beta despite determinant asymptotics",
    max(max(coefficient_profile(D)[2].values()) for D in adversaries.values()) > mp.mpf("0.8"),
    "determinant form alone does not select physical kernels",
)

print("\n=== Theorem status ===")
print(
    "The reciprocal determinant is the right spectral shadow at the first "
    "cycle level, but the naive determinant is not the full finite object.  "
    "The next theorem must include labelled cycle-index multiplicities, exact "
    "falling-factor inflation, and the non-cycle finite-population remainder."
)

print("\n" + "=" * 80)
failed = False
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
    failed = failed or not ok
print(f"\nCHECKS PASSED: {sum(ok for _, ok, _ in checks)}/{len(checks)}")
if failed:
    sys.exit(1)
print("DONE.")
