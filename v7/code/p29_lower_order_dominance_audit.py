#!/usr/bin/env python3
"""
Paper 29 receipt: lower-order dominance audit.

The top-order beta ladder remains subcritical through N=22, but the click-law
coefficient envelope needs all r.  This receipt asks whether the all-order
physical beta profile through N=18 is dominated by the top order.

It finds a narrower truth: the maximum beta is near the top, but not always at
the top.  The proof cannot simply bound r=N/2 and declare victory; it needs a
bulk/top split or a monotone majorant with a small finite top correction.

All non-integer arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

from p29_matching_lib import coefficient_profile, fmt, physical_delta

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


print("=" * 80)
print("Paper 29 lower-order dominance audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

rows = []
max_margin_over_top = mp.mpf(0)
max_gap_from_top = 0
max_beta = mp.mpf(0)
top_is_max_count = 0

print("\n=== All-order physical beta profile at c=0.5 ===")
for n in range(8, 20, 2):
    D = physical_delta(n, mp.mpf("0.5"), nodes=12)
    q, rho, beta = coefficient_profile(D)
    r_top = n // 2
    r_star = max(beta, key=lambda r: beta[r])
    beta_star = beta[r_star]
    beta_top = beta[r_top]
    margin = beta_star - beta_top
    max_margin_over_top = max(max_margin_over_top, margin)
    max_gap_from_top = max(max_gap_from_top, r_top - r_star)
    max_beta = max(max_beta, beta_star)
    if r_star == r_top:
        top_is_max_count += 1
    rows.append((n, r_star, beta_star, beta_top))
    print(
        f"N={n}, r_star={r_star}, beta_star={fmt(beta_star, 22)}, "
        f"r_top={r_top}, beta_top={fmt(beta_top, 22)}, "
        f"star_minus_top={fmt(margin, 18)}"
    )

print("\n=== Local profile around the maximum ===")
for n, r_star, _beta_star, _beta_top in rows[-3:]:
    D = physical_delta(n, mp.mpf("0.5"), nodes=12)
    _q, _rho, beta = coefficient_profile(D)
    lo = max(2, r_star - 2)
    hi = min(n // 2, r_star + 2)
    print(f"N={n}: " + ", ".join(f"r={r}: {fmt(beta[r], 12)}" for r in range(lo, hi + 1)))

check(
    "all audited beta values remain below working guard",
    max_beta < mp.mpf("0.65"),
    f"max_beta={fmt(max_beta, 22)}",
)
check(
    "top order alone is falsified as exact maximum rule",
    top_is_max_count < len(rows),
    f"top_is_max_count={top_is_max_count}/{len(rows)} max_margin={fmt(max_margin_over_top, 18)}",
)
check(
    "maximum stays within two orders of top in audited ladder",
    max_gap_from_top <= 2,
    f"max_gap_from_top={max_gap_from_top}",
)
check(
    "top-order envelope is close but not exact",
    max_margin_over_top > 0 and max_margin_over_top < mp.mpf("0.04"),
    f"max_margin_over_top={fmt(max_margin_over_top, 18)}",
)

print("\n=== Theorem status ===")
print(
    "Top order is not an exact dominance theorem: the maximum beta sits one or "
    "two orders below top in several audited cases.  The surviving proof target "
    "is a near-top/bulk split, not a top-only proof."
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
