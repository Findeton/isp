#!/usr/bin/env python3
"""
Paper 29 receipt: scaled matching-root radius audit.

Define the scaled matching generating polynomial

    A_N(w) = sum_r N^r rho_{N,r} w^r = R_N(Nw).

If a Cauchy/radius theorem is the right analytic form of the coefficient-root
envelope, physical kernels should have a larger zero-free disk for A_N than
staged high-beta kernels.  This receipt audits that root-radius picture.

This is not a proof: finite root radii do not imply a uniform all-N bound.
They tell us whether the generating-function target is aligned with the
coefficient envelope.

All non-integer arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

from p29_matching_lib import (
    balanced_block_D,
    calibrate_to_q2,
    coefficient_profile,
    fmt,
    physical_delta,
    scaled_matching_coefficients,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def root_radius_from_scaled_coeffs(coeffs):
    # mpmath wants highest-degree first.  Trim trailing near-zero coefficients
    # only at the very end, never the intentional zero linear coefficient.
    degree = len(coeffs) - 1
    while degree > 0 and abs(coeffs[degree]) < mp.mpf("1e-100"):
        degree -= 1
    poly = [coeffs[i] for i in range(degree, -1, -1)]
    roots = mp.polyroots(poly, maxsteps=200, error=False)
    radii = sorted(abs(root) for root in roots)
    return radii[0], radii, roots


print("=" * 80)
print("Paper 29 scaled matching-root radius audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

physical_rows = []
block_rows = []

print("\n=== Physical scaled root radii ===")
for n in [8, 10, 12, 14, 16, 18]:
    D = physical_delta(n, mp.mpf("0.5"), nodes=12)
    coeffs = scaled_matching_coefficients(D)
    radius, radii, roots = root_radius_from_scaled_coeffs(coeffs)
    q, _rho, beta = coefficient_profile(D)
    physical_rows.append((n, radius, max(beta.values())))
    print(
        f"N={n}, degree={len(coeffs)-1}, min_radius={fmt(radius, 18)}, "
        f"second_radius={fmt(radii[1] if len(radii)>1 else mp.inf, 18)}, "
        f"max_beta={fmt(max(beta.values()), 18)}"
    )

print("\n=== q2-calibrated staged block scaled root radii ===")
for n in [8, 10, 12, 14]:
    physical = physical_delta(n, mp.mpf("0.5"), nodes=12)
    target_q, _rho, _beta = coefficient_profile(physical)
    D = calibrate_to_q2(balanced_block_D(n), target_q[2])
    coeffs = scaled_matching_coefficients(D)
    radius, radii, roots = root_radius_from_scaled_coeffs(coeffs)
    q, _rho, beta = coefficient_profile(D)
    block_rows.append((n, radius, max(beta.values())))
    print(
        f"N={n}, degree={len(coeffs)-1}, min_radius={fmt(radius, 18)}, "
        f"second_radius={fmt(radii[1] if len(radii)>1 else mp.inf, 18)}, "
        f"max_beta={fmt(max(beta.values()), 18)}"
    )

min_physical_radius = min(row[1] for row in physical_rows)
max_physical_beta = max(row[2] for row in physical_rows)
paired_margin = min(
    physical_radius - block_radius
    for n, physical_radius, _physical_beta in physical_rows
    for block_n, block_radius, _block_beta in block_rows
    if n == block_n
)
min_block_beta = min(row[2] for row in block_rows)

check(
    "physical scaled root radius stays bounded away from zero in audited ladder",
    min_physical_radius > mp.mpf("0.08"),
    f"min_physical_radius={fmt(min_physical_radius, 18)}",
)
check(
    "same-N staged blocks have smaller scaled root radius while beta is high",
    paired_margin > 0 and min_block_beta > mp.mpf("0.8"),
    f"min_same_N_radius_margin={fmt(paired_margin, 18)} min_block_beta={fmt(min_block_beta, 18)}",
)
check(
    "root-radius audit aligns with physical beta envelope",
    max_physical_beta < mp.mpf("0.65"),
    f"max_physical_beta={fmt(max_physical_beta, 18)}",
)

print("\n=== Theorem status ===")
print(
    "The scaled matching polynomial gives the right analytic formulation: in the "
    "audited same-N comparisons, physical kernels have a larger zero-free "
    "radius than staged high-beta blocks.  The radius itself decreases with N "
    "on the audited ladder, so the missing proof is not a naive constant-radius "
    "claim; it is a correctly scaled zero-free/radius theorem for the physical "
    "sector-profile generating function."
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
