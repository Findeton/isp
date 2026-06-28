#!/usr/bin/env python3
"""
Paper 29 receipt: factorial-normalized profile envelope implication.

Let

    a_{N,r} = N^r rho_{N,r},
    lambda_{N,r} = (|a_{N,r}| / sqrt(r!))^(1/r).

Then, for even N and 1<=r<=N/2,

    N q_{N,r}^{1/r}
      =
    lambda_{N,r}^2 * ((N/2)_r)^(1/r) / N.

This is not an asymptotic estimate.  It is an exact algebraic bridge from a
factorial-normalized coefficient/sector-profile envelope to the click-law
coefficient-root envelope.

Consequently, if lambda_{N,r} <= Lambda uniformly, then

    q_{N,r} <= (Lambda^2/(2N))^r.

The bound is conservative at high r because ((N/2)_r)^(1/r)/N is much smaller
than 1/2 near top matching order.

All non-integer arithmetic uses mpmath with dps=140.
"""

import math
import sys

import mpmath as mp

from p29_matching_lib import (
    add_matrices,
    balanced_block_D,
    calibrate_to_q2,
    coefficient_profile,
    falling,
    fmt,
    fourier_vector,
    outer_kernel,
    physical_delta,
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


def lambda_profile(D):
    n = len(D)
    scaled = scaled_matching_coefficients(D)
    out = {}
    for r in range(2, n // 2 + 1):
        out[r] = mp.power(abs(scaled[r]) / mp.sqrt(mp.factorial(r)), mp.mpf(1) / r)
    return out


def beta_from_lambda(n, r, lam):
    half = n // 2
    factor = mp.power(falling(half, r), mp.mpf(1) / r) / n
    return lam * lam * factor


print("=" * 80)
print("Paper 29 factorial-normalized profile envelope implication")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

max_identity_error = mp.mpf(0)
max_physical_lambda = mp.mpf(0)
max_physical_beta = mp.mpf(0)
max_physical_conservative_beta = mp.mpf(0)

print("\n=== Physical profile audit ===")
for c in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")]:
    sizes = [8, 10, 12, 14, 16, 18] if c == mp.mpf("0.5") else [8, 10, 12, 14]
    for n in sizes:
        D = physical_delta(n, c, nodes=12)
        q, rho, beta = coefficient_profile(D)
        lambdas = lambda_profile(D)
        for r, lam in lambdas.items():
            identity_beta = beta_from_lambda(n, r, lam)
            max_identity_error = max(max_identity_error, abs(identity_beta - beta[r]))
            max_physical_lambda = max(max_physical_lambda, lam)
            max_physical_beta = max(max_physical_beta, beta[r])
            max_physical_conservative_beta = max(max_physical_conservative_beta, lam * lam / 2)
        r_star = max(lambdas, key=lambda r: lambdas[r])
        b_star = max(beta, key=lambda r: beta[r])
        print(
            f"N={n}, c={fmt(c, 6)}, max_lambda={fmt(lambdas[r_star], 18)} at r={r_star}, "
            f"max_beta={fmt(beta[b_star], 18)} at r={b_star}, "
            f"conservative_beta_from_lambda={fmt(lambdas[r_star]**2/2, 18)}"
        )

print("\n=== q2-calibrated adversary profile audit ===")
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

min_bad_lambda = mp.inf
max_good_lambda = mp.mpf(0)
for name, D in adversaries.items():
    q, _rho, beta = coefficient_profile(D)
    lambdas = lambda_profile(D)
    r_star = max(lambdas, key=lambda r: lambdas[r])
    b_star = max(beta, key=lambda r: beta[r])
    if max(beta.values()) > mp.mpf("0.65"):
        min_bad_lambda = min(min_bad_lambda, lambdas[r_star])
    else:
        max_good_lambda = max(max_good_lambda, lambdas[r_star])
    print(
        f"{name}: max_lambda={fmt(lambdas[r_star], 18)} at r={r_star}, "
        f"max_beta={fmt(beta[b_star], 18)} at r={b_star}"
    )

sqrt2 = mp.sqrt(2)

check(
    "exact lambda-beta bridge holds on audited grid",
    max_identity_error < mp.mpf("1e-100"),
    f"max_identity_error={fmt(max_identity_error, 18)}",
)
check(
    "audited physical profile stays below sqrt(2)",
    max_physical_lambda < sqrt2,
    f"max_physical_lambda={fmt(max_physical_lambda, 18)} sqrt2={fmt(sqrt2, 18)}",
)
check(
    "sqrt(2) profile envelope would imply beta<=1 conservatively",
    max_physical_conservative_beta < mp.mpf("1"),
    f"max_conservative_beta={fmt(max_physical_conservative_beta, 18)}",
)
check(
    "high-beta q2-calibrated adversaries violate the sqrt(2) profile threshold",
    min_bad_lambda > sqrt2,
    f"min_bad_lambda={fmt(min_bad_lambda, 18)}",
)
check(
    "low-beta smooth multi-mode adversary remains below the bad threshold",
    max_good_lambda < sqrt2,
    f"max_good_lambda={fmt(max_good_lambda, 18)}",
)

print("\n=== Theorem status ===")
print(
    "The coefficient-root envelope is exactly equivalent to controlling the "
    "factorial-normalized scaled coefficients lambda_{N,r}, with the finite "
    "falling factor included.  The audited physical kernels satisfy the "
    "sqrt(2) conservative threshold; staged high-beta adversaries do not.  "
    "The remaining proof is therefore a sector-profile theorem for lambda, "
    "not a raw root-radius theorem."
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
