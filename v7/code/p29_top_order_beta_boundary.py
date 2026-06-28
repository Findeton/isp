#!/usr/bin/env python3
"""
Paper 29 receipt: physical top-order beta boundary.

The top-order lambda receipt falsifies the conservative lambda<sqrt(2)
shortcut.  The coefficient-root envelope uses the exact finite falling factor:

    beta_{N,r} = N q_{N,r}^{1/r}
               = lambda_{N,r}^2 ((N/2)_r)^(1/r) / N.

For top order r=N/2 this falling factor is far below 1/2, so lambda may exceed
sqrt(2) while beta remains subcritical.  This receipt audits the top-order beta
ladder and tests whether naive tail fits are reliable enough to prove the
limiting boundary.  They are not.

All non-integer arithmetic uses mpmath with dps=140.
"""

from functools import lru_cache
import sys

import mpmath as mp

from p29_matching_lib import fmt, physical_delta

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


def top_profile(D):
    n = len(D)
    r = n // 2
    haf = perfect_matching_sum(D)
    rho = (mp.mpf(2) ** r) * mp.factorial(r) * haf / mp.factorial(n)
    lam = mp.power(abs((mp.mpf(n) ** r) * rho) / mp.sqrt(mp.factorial(r)), mp.mpf(1) / r)
    beta = mp.mpf(n) * mp.power(abs(rho * rho), mp.mpf(1) / r)
    falling_factor = mp.power(mp.factorial(r), mp.mpf(1) / r) / n
    beta_from_lam = lam * lam * falling_factor
    return rho, lam, beta, beta_from_lam, falling_factor


print("=" * 80)
print("Paper 29 physical top-order beta boundary")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

rows = []
print("\n=== c=0.5 top-order beta ladder ===")
for n in range(8, 24, 2):
    D = physical_delta(n, mp.mpf("0.5"), nodes=12)
    rho, lam, beta, beta_from_lam, falling_factor = top_profile(D)
    rows.append((n, lam, beta, falling_factor))
    print(
        f"N={n}, r={n//2}, lambda={fmt(lam, 22)}, "
        f"falling_factor={fmt(falling_factor, 22)}, "
        f"beta_top={fmt(beta, 22)}, identity_error={fmt(abs(beta-beta_from_lam), 8)}"
    )

max_identity_error = max(abs(row[2] - row[1] * row[1] * row[3]) for row in rows)
max_beta = max(row[2] for row in rows)
monotone_beta = all(rows[i][2] < rows[i + 1][2] for i in range(len(rows) - 1))

print("\n=== Limit fits for top beta ===")
tail = rows[-5:]
x = [mp.mpf(1) / row[0] for row in tail]
y = [row[2] for row in tail]

def fit_constant_plus(order):
    # beta ~= L + a/N + b/N^2 for order=2, or L+a/N for order=1.
    if order == 1:
        s0 = mp.mpf(len(x))
        s1 = mp.fsum(x)
        s2 = mp.fsum(xx * xx for xx in x)
        t0 = mp.fsum(y)
        t1 = mp.fsum(xx * yy for xx, yy in zip(x, y))
        det = s0 * s2 - s1 * s1
        L = (t0 * s2 - t1 * s1) / det
        a = (s0 * t1 - s1 * t0) / det
        return L, a, mp.mpf(0)
    s = [[mp.mpf(0) for _ in range(3)] for _ in range(3)]
    t = [mp.mpf(0) for _ in range(3)]
    for xx, yy in zip(x, y):
        vec = [mp.mpf(1), xx, xx * xx]
        for i in range(3):
            t[i] += vec[i] * yy
            for j in range(3):
                s[i][j] += vec[i] * vec[j]
    M = mp.matrix(s)
    b = mp.matrix(t)
    sol = mp.lu_solve(M, b)
    return sol[0], sol[1], sol[2]

L1, a1, _ = fit_constant_plus(1)
L2, a2, b2 = fit_constant_plus(2)
print(f"linear-in-1/N fit L={fmt(L1, 22)}, a={fmt(a1, 22)}")
print(f"quadratic-in-1/N fit L={fmt(L2, 22)}, a={fmt(a2, 22)}, b={fmt(b2, 22)}")
for n in [24, 32, 64, 128]:
    pred1 = L1 + a1 / n
    pred2 = L2 + a2 / n + b2 / (n * n)
    print(f"N={n}, pred_linear={fmt(pred1, 22)}, pred_quadratic={fmt(pred2, 22)}")

check(
    "top beta identity from lambda and falling factor holds",
    max_identity_error < mp.mpf("1e-100"),
    f"max_identity_error={fmt(max_identity_error, 18)}",
)
check(
    "top beta is monotone increasing on audited c=0.5 ladder",
    monotone_beta,
    f"max_beta={fmt(max_beta, 22)}",
)
check(
    "top beta remains below the working beta guard through N=22",
    max_beta < mp.mpf("0.65"),
    f"max_beta={fmt(max_beta, 22)}",
)
check(
    "naive tail fits are unstable and cannot prove subcriticality",
    max(L1, L2) > mp.mpf("0.65"),
    f"L1={fmt(L1, 22)} L2={fmt(L2, 22)}",
)

print("\n=== Theorem status ===")
print(
    "The sqrt(2) lambda shortcut is false, but the actual top-order beta "
    "boundary remains subcritical through N=22.  Naive tail fits are unstable "
    "and cannot prove the limiting boundary.  The next theorem needs an "
    "analytic top-order saddle or a rigorous finite-falling majorant, then a "
    "lower-order dominance argument."
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
