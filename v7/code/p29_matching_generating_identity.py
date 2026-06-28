#!/usr/bin/env python3
"""
Paper 29 receipt: exact physical matching generating identity.

The normalized disjoint-pair moment rho_{N,r} is not a mysterious new
coefficient.  For a symmetric zero-diagonal kernel D, let m_{N,r}(D) be the
ordinary weighted sum over unordered r-matchings of the complete graph on N
vertices, counted with the edge-ordering convention used by the dynamic
program in this receipt.  Then

    rho_{N,r}(D) = 2^r m_{N,r}(D) / (N)_{2r}.

If m_{N,r} is defined with each unordered edge set counted once instead,
the equivalent formula is 2^r r! m_{N,r} / (N)_{2r}.

Consequently the click-law coefficient is the Hadamard-square/binomial
transform

    q_{N,r}(D) = binom(floor(N/2), r) rho_{N,r}(D)^2.

This receipt proves the finite algebra by direct independent computations on
physical and adversarial kernels.  All non-integer arithmetic uses mpmath with
dps=140.
"""

import math
import sys

import mpmath as mp

from p29_matching_lib import (
    add_matrices,
    balanced_block_D,
    calibrate_to_q2,
    coefficient_profile,
    disjoint_moments,
    fmt,
    fourier_vector,
    max_row_linf,
    outer_kernel,
    physical_delta,
    rho_from_unordered_matching,
    scale_matrix,
    unordered_matching_sums,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


print("=" * 80)
print("Paper 29 exact matching generating identity")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
physical = physical_delta(n, mp.mpf("0.5"), nodes=12)
target_q2, _target_rho, _target_beta = coefficient_profile(physical)
cos1 = outer_kernel(fourier_vector(n, 1, "cos"))
sin1 = outer_kernel(fourier_vector(n, 1, "sin"))
cos2 = outer_kernel(fourier_vector(n, 2, "cos"))

kernels = {
    "physical_c0.5": physical,
    "balanced_block_q2_calibrated": calibrate_to_q2(balanced_block_D(n), target_q2[2]),
    "fourier_three_mode_q2_calibrated": calibrate_to_q2(
        add_matrices(cos1, scale_matrix(sin1, mp.mpf("0.5")), scale_matrix(cos2, mp.mpf("0.25"))),
        target_q2[2],
    ),
}

max_identity_error = mp.mpf(0)
max_q_error = mp.mpf(0)
max_rho1 = mp.mpf(0)
max_beta = mp.mpf(0)

for name, D in kernels.items():
    print(f"\n{name}: row_linf={fmt(max_row_linf(D), 18)}")
    rho_direct = disjoint_moments(D)
    unordered = unordered_matching_sums(D)
    q, rho_profile, beta = coefficient_profile(D)
    max_beta = max(max_beta, max(beta.values()))
    max_rho1 = max(max_rho1, abs(rho_direct[1]))
    for r in range(0, n // 2 + 1):
        rho_matching = rho_from_unordered_matching(n, r, unordered[r])
        identity_error = abs(rho_direct[r] - rho_matching)
        max_identity_error = max(max_identity_error, identity_error)
        if r >= 1:
            q_from_identity = mp.mpf(math.comb(n // 2, r)) * rho_matching * rho_matching
            q_error = abs(q[r] - q_from_identity)
            max_q_error = max(max_q_error, q_error)
        else:
            q_error = mp.mpf(0)
        print(
            f"  r={r}, unordered_m={fmt(unordered[r], 18)}, "
            f"rho_direct={fmt(rho_direct[r], 18)}, "
            f"rho_matching={fmt(rho_matching, 18)}, "
            f"identity_error={fmt(identity_error, 8)}, q_error={fmt(q_error, 8)}"
        )

check(
    "unordered matching identity reproduces directed disjoint moments",
    max_identity_error < mp.mpf("1e-100"),
    f"max_identity_error={fmt(max_identity_error, 18)}",
)
check(
    "binomial Hadamard-square q transform is exact",
    max_q_error < mp.mpf("1e-100"),
    f"max_q_error={fmt(max_q_error, 18)}",
)
check(
    "row-zero kernels have zero first matching moment",
    max_rho1 < mp.mpf("1e-100"),
    f"max_abs_rho1={fmt(max_rho1, 18)}",
)
check(
    "campaign includes both benign and hostile coefficient regimes",
    max_beta > mp.mpf("1"),
    f"max_beta={fmt(max_beta, 18)}",
)

print("\n=== Theorem status ===")
print(
    "The exact finite object is the ordinary weighted matching polynomial, "
    "followed by falling-factor normalization and the q Hadamard-square/binomial "
    "transform.  The remaining proof cannot change coefficients by changing "
    "language; it must bound this matching generating object."
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
