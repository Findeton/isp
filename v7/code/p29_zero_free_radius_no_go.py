#!/usr/bin/env python3
"""
Paper 29 receipt: zero-free radius alone is not enough.

The previous receipt gives an exact coefficient-profile bridge.  This receipt
closes a tempting but false shortcut:

    "If A_N(w) has no roots near zero, then the coefficient-root envelope follows."

That is false as a polynomial theorem.  A high-degree polynomial can have every
root outside a fixed disk and still have large middle coefficients.  The
missing theorem must control the coefficient/sector profile or a Cauchy
majorant, not merely the nearest zero.

All non-integer arithmetic uses mpmath with dps=140.
"""

import math
import sys

import mpmath as mp

from p29_matching_lib import fmt, falling

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def fake_beta_from_scaled_coeff(n, r, a_r):
    rho = mp.mpf(a_r) / (mp.mpf(n) ** r)
    q = mp.mpf(math.comb(n // 2, r)) * rho * rho
    return mp.mpf(n) * mp.power(abs(q), mp.mpf(1) / r)


def lambda_from_scaled_coeff(r, a_r):
    return mp.power(abs(a_r) / mp.sqrt(mp.factorial(r)), mp.mpf(1) / r)


print("=" * 80)
print("Paper 29 zero-free radius no-go")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 80
d = n // 2
gamma = mp.mpf("0.5")

# A(w)=(1+w/gamma)^d has all roots at -gamma.
coeffs = [mp.mpf(math.comb(d, r)) / (gamma ** r) for r in range(d + 1)]
r_star = max(range(2, d + 1), key=lambda r: fake_beta_from_scaled_coeff(n, r, coeffs[r]))
max_beta = fake_beta_from_scaled_coeff(n, r_star, coeffs[r_star])
lambda_star = lambda_from_scaled_coeff(r_star, coeffs[r_star])

print("\n=== Fixed zero-free radius counterexample ===")
print(f"N={n}, degree={d}, all roots=-{fmt(gamma, 8)}")
print(
    f"max_fake_beta={fmt(max_beta, 18)} at r={r_star}, "
    f"lambda={fmt(lambda_star, 18)}"
)

sqrt2 = mp.sqrt(2)

print("\n=== Exact profile factor comparison ===")
factor_star = mp.power(falling(d, r_star), mp.mpf(1) / r_star) / n
identity_beta = lambda_star * lambda_star * factor_star
print(
    f"falling_factor={fmt(factor_star, 18)}, "
    f"lambda^2*factor={fmt(identity_beta, 18)}"
)

check(
    "polynomial has fixed zero-free radius by construction",
    gamma == mp.mpf("0.5"),
    f"root_radius={fmt(gamma, 18)}",
)
check(
    "fixed zero-free radius permits large coefficient-root stress",
    max_beta > mp.mpf("10"),
    f"max_fake_beta={fmt(max_beta, 18)}",
)
check(
    "large stress is detected by factorial-normalized lambda",
    lambda_star > sqrt2,
    f"lambda={fmt(lambda_star, 18)} sqrt2={fmt(sqrt2, 18)}",
)
check(
    "lambda identity still reconstructs the fake beta",
    abs(identity_beta - max_beta) < mp.mpf("1e-80"),
    f"identity_error={fmt(abs(identity_beta - max_beta), 18)}",
)

print("\n=== Theorem status ===")
print(
    "A zero-free disk for A_N(w) is not enough.  The theorem must control a "
    "majorant or, more intrinsically here, the factorial-normalized sector "
    "profile lambda_{N,r}.  Root location is useful only after the correct "
    "profile bound is present."
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
