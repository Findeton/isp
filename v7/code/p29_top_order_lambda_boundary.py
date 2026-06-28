#!/usr/bin/env python3
"""
Paper 29 receipt: physical top-order lambda boundary.

The factorial-normalized profile audit found that the hostile physical point is
the top matching order r=N/2 at c=0.5.  This receipt computes only that
top-order coefficient, so the ladder can go deeper than the all-order audits.
It falsifies the conservative lambda<sqrt(2) boundary and checks whether the
actual finite falling-factor beta remains controlled.

For N=2r,

    rho_{N,r} = 2^r r! Haf(D) / N!,
    lambda_{N,r} = (|N^r rho_{N,r}| / sqrt(r!))^(1/r).

The perfect-matching sum Haf(D) is computed by a first-free-vertex dynamic
program.  All non-integer arithmetic uses mpmath with dps=140.
"""

from functools import lru_cache
import math
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


def perfect_matching_sum(D):
    n = len(D)

    @lru_cache(maxsize=None)
    def rec(mask):
        if mask == 0:
            return mp.mpf(1)
        first_bit = mask & -mask
        i = first_bit.bit_length() - 1
        rest = mask ^ first_bit
        total = mp.mpf(0)
        m = rest
        while m:
            bit = m & -m
            j = bit.bit_length() - 1
            total += D[i][j] * rec(rest ^ bit)
            m ^= bit
        return total

    return rec((1 << n) - 1)


def top_lambda(D):
    n = len(D)
    r = n // 2
    haf = perfect_matching_sum(D)
    rho = (mp.mpf(2) ** r) * mp.factorial(r) * haf / mp.factorial(n)
    lam = mp.power(abs((mp.mpf(n) ** r) * rho) / mp.sqrt(mp.factorial(r)), mp.mpf(1) / r)
    beta = mp.mpf(n) * mp.power(abs(rho * rho), mp.mpf(1) / r)
    return haf, rho, lam, beta


print("=" * 80)
print("Paper 29 physical top-order lambda boundary")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

sqrt2 = mp.sqrt(2)
rows = []
print("\n=== c=0.5 top-order ladder ===")
for n in range(8, 24, 2):
    D = physical_delta(n, mp.mpf("0.5"), nodes=12)
    haf, rho, lam, beta = top_lambda(D)
    rows.append((n, lam, beta, rho))
    print(
        f"N={n}, r={n//2}, lambda_top={fmt(lam, 24)}, "
        f"sqrt2-lambda={fmt(sqrt2-lam, 24)}, beta_top={fmt(beta, 24)}, "
        f"rho={fmt(rho, 12)}"
    )

max_lam = max(row[1] for row in rows)
last_lam = rows[-1][1]
last_gap = sqrt2 - last_lam
monotone = all(rows[i][1] < rows[i + 1][1] for i in range(len(rows) - 1))

print("\n=== Simple boundary fits ===")
tail = rows[-4:]
xs = [mp.mpf(1) / row[0] for row in tail]
ys = [sqrt2 - row[1] for row in tail]

# Least-squares fit gap = a/N + b/N^2 on the last four points.
s11 = mp.fsum(x * x for x in xs)
s12 = mp.fsum(x**3 for x in xs)
s22 = mp.fsum(x**4 for x in xs)
t1 = mp.fsum(x * y for x, y in zip(xs, ys))
t2 = mp.fsum((x**2) * y for x, y in zip(xs, ys))
det = s11 * s22 - s12 * s12
a = (t1 * s22 - t2 * s12) / det
b = (s11 * t2 - s12 * t1) / det
fit_errors = [abs((a / row[0] + b / (row[0] ** 2)) - (sqrt2 - row[1])) for row in tail]
print(f"fit gap ~= a/N + b/N^2 with a={fmt(a, 24)}, b={fmt(b, 24)}")
print(f"max_tail_fit_error={fmt(max(fit_errors), 24)}")

# Extrapolated sign is a stress test, not a theorem.
for n in [24, 32, 64, 128]:
    pred = sqrt2 - (a / n + b / (n * n))
    print(f"predicted lambda_top N={n}: {fmt(pred, 24)}, gap={fmt(sqrt2-pred, 24)}")

print("\n=== Consistency with all-order receipt at N<=18 ===")
max_all_order_error = mp.mpf(0)
for n, lam, _beta, _rho in rows:
    if n > 18:
        continue
    D = physical_delta(n, mp.mpf("0.5"), nodes=12)
    q, rho, beta = coefficient_profile(D)
    r = n // 2
    lam_all = mp.power(abs((mp.mpf(n) ** r) * rho[r]) / mp.sqrt(mp.factorial(r)), mp.mpf(1) / r)
    err = abs(lam - lam_all)
    max_all_order_error = max(max_all_order_error, err)
    print(f"N={n}, top_only={fmt(lam, 18)}, all_order={fmt(lam_all, 18)}, err={fmt(err, 8)}")

check(
    "top-order lambda is monotone increasing on audited c=0.5 ladder",
    monotone,
    f"max_lambda={fmt(max_lam, 24)}",
)
crossing = [row for row in rows if row[1] > sqrt2]
max_beta = max(row[2] for row in rows)

check(
    "conservative sqrt(2) lambda boundary is falsified by top order",
    len(crossing) >= 2 and crossing[0][0] == 20,
    f"first_crossing_N={crossing[0][0] if crossing else 'none'} max_lambda={fmt(max_lam, 24)}",
)
check(
    "actual top-order beta remains controlled after sqrt(2) crossing",
    max_beta < mp.mpf("0.65"),
    f"max_beta={fmt(max_beta, 24)}",
)
check(
    "top-order receipt agrees with all-order receipt through N=18",
    max_all_order_error < mp.mpf("1e-100"),
    f"max_all_order_error={fmt(max_all_order_error, 18)}",
)

print("\n=== Theorem status ===")
print(
    "The conservative lambda<sqrt(2) boundary is false: top order crosses it "
    "at N=20.  The coefficient-root envelope itself is not falsified, because "
    "the exact falling-factor beta remains below 0.65 through N=22.  The next "
    "target is therefore the finite-falling top-order beta boundary, not the "
    "sqrt(2) shortcut."
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
