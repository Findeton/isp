#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: overlap-graph component mgf bound.

For width 2, compare two hidden matchings H,H'.  Their union decomposes into
alternating components.  The cycle-tax receipt showed that the total component
count K_N has mean (1/2) log(N/2)+O(1).

This receipt records the exact probability-generating function:

    E[z^K_m] = prod_{j=0}^{m-1} (z+2j)/(1+2j),      m=N/2.

Thus a fixed nonshared-component factor b>1 creates polynomial growth
approximately m^{(b-1)/2}, while a factor b_m=1+O(1/log m) has bounded mgf.

This is the clean sufficient condition for the cycle-neutrality side of the
local factor theorem: nonshared alternating components must carry factor
1+O(1/log N), preferably 1+o(1/log N), unless a full cycle-tax action is kept.

All arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def odd_double_factorial(n):
    if n <= 0:
        return mp.mpf(1)
    out = mp.mpf(1)
    for value in range(n, 0, -2):
        out *= value
    return out


def component_mean(m, k):
    if k == 1:
        connected = mp.mpf(1)
    else:
        connected = mp.power(2, k - 1) * mp.factorial(k - 1)
    return (
        mp.binomial(m, k)
        * connected
        * odd_double_factorial(2 * m - 2 * k - 1)
        / odd_double_factorial(2 * m - 1)
    )


def total_component_mean_by_components(m):
    return mp.fsum(component_mean(m, k) for k in range(1, m + 1))


def component_mgf(m, z):
    return mp.nprod(lambda j: (z + 2 * j) / (1 + 2 * j), [0, m - 1])


def component_mgf_closed(m, z):
    return mp.gamma(m + z / 2) * mp.gamma(mp.mpf("0.5")) / (mp.gamma(z / 2) * mp.gamma(m + mp.mpf("0.5")))


def component_mgf_finite(m, z):
    out = mp.mpf(1)
    for j in range(m):
        out *= (z + 2 * j) / (1 + 2 * j)
    return out


def mean_from_mgf_derivative(m):
    return mp.fsum(mp.mpf(1) / (2 * j + 1) for j in range(m))


print("=" * 80)
print("Collapsed P23 overlap-graph component mgf bound")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\nMean check")
for m in [8, 16, 64, 256]:
    mean_components = total_component_mean_by_components(m)
    mean_mgf = mean_from_mgf_derivative(m)
    print(f"m={m}: component_sum={fmt(mean_components, 24)} mgf_derivative={fmt(mean_mgf, 24)}")

print("\nFixed component factor b=1.1")
fixed_rows = []
for m in [64, 256, 1024, 4096, 16384, 65536, 262144, 1048576]:
    value = component_mgf_closed(mp.mpf(m), mp.mpf("1.1"))
    fixed_rows.append((m, value))
    print(f"m={m}: E[1.1^K]={fmt(value, 24)} scaled={fmt(value / (mp.mpf(m) ** mp.mpf('0.05')), 24)}")

print("\nLog-neutral factor b_m=1+2/log(m)")
neutral_rows = []
for m in [64, 256, 1024, 4096, 16384, 65536]:
    b_m = 1 + mp.mpf(2) / mp.log(m)
    value = component_mgf_closed(mp.mpf(m), b_m)
    neutral_rows.append((m, b_m, value))
    print(f"m={m}: b_m={fmt(b_m, 18)} E[b_m^K]={fmt(value, 24)}")

print("\nStrict-neutral factor b_m=1+1/log(m)^2")
strict_rows = []
for m in [64, 256, 1024, 4096, 16384, 65536]:
    b_m = 1 + 1 / (mp.log(m) ** 2)
    value = component_mgf_closed(mp.mpf(m), b_m)
    strict_rows.append((m, b_m, value))
    print(f"m={m}: b_m={fmt(b_m, 18)} E[b_m^K]={fmt(value, 24)}")

check(
    "Component mgf derivative matches the exact component mean",
    all(abs(total_component_mean_by_components(m) - mean_from_mgf_derivative(m)) < mp.mpf("1e-80") for m in [8, 16, 64]),
    "",
)
check(
    "Fixed nonshared-component factor grows with m",
    fixed_rows[-1][1] > fixed_rows[0][1] * mp.mpf("1.5"),
    f"m=64:{fmt(fixed_rows[0][1], 10)} m=1048576:{fmt(fixed_rows[-1][1], 10)}",
)
check(
    "Fixed factor growth matches the polynomial exponent scale",
    all(mp.mpf("0.8") < value / (mp.mpf(m) ** mp.mpf("0.05")) < mp.mpf("2.0") for m, value in fixed_rows),
    "b=1.1 gives exponent (b-1)/2=0.05",
)
check(
    "Log-neutral component factors have bounded tested mgf",
    max(value for _m, _b, value in neutral_rows) < mp.mpf("6"),
    "b_m=1+2/log(m)",
)
check(
    "Strict-neutral component factors tend back toward one",
    strict_rows[-1][2] < strict_rows[0][2],
    f"m=64:{fmt(strict_rows[0][2], 10)} m=65536:{fmt(strict_rows[-1][2], 10)}",
)

print("\n=== Consequence ===")
print("A fixed factor per nonshared alternating component is too expensive:")
print("it gives polynomial growth.  The boundedness theorem needs either")
print("cycle-neutrality b_N=1+O(1/log N), strict neutrality b_N=1+o(1/log N),")
print("or an explicit cycle-tax term in the record law.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
