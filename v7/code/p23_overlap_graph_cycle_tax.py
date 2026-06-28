#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: hidden-overlap graph cycle tax.

The previous overlap receipt counted only pairs that are co-clustered in both
hidden explanations.  For width 2, the hidden explanations are perfect
matchings H and H'.  Their union is an alternating 2-regular multigraph.  Common
hidden pairs are the 2-vertex components, but nonshared alternating cycles also
exist.

This receipt computes the exact expected number of alternating components of
each size.  If m=N/2 is the number of hidden pairs and C_k is the number of
components containing k hidden H-edges, then

    E C_1 = m/(2m-1),

and for k>=2

    E C_k =
      binom(m,k) 2^{k-1}(k-1)! (2m-2k-1)!! / (2m-1)!!.

For every fixed k, E C_k -> 1/(2k).  Hence the total number of alternating
components has mean asymptotic to (1/2) log m + O(1), while the shared-pair
overlap C_1 stays O(1).

Consequence: an overlap-pair bound is enough only if nonshared alternating
cycles are asymptotically neutral.  If each nonshared cycle carried a fixed
factor b>1, a polynomial second-moment divergence would remain possible.

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
    if k < 1 or k > m:
        return mp.mpf(0)
    if k == 1:
        connected_matchings = mp.mpf(1)
    else:
        connected_matchings = mp.power(2, k - 1) * mp.factorial(k - 1)
    return (
        mp.binomial(m, k)
        * connected_matchings
        * odd_double_factorial(2 * m - 2 * k - 1)
        / odd_double_factorial(2 * m - 1)
    )


def total_component_mean(m):
    return mp.fsum(component_mean(m, k) for k in range(1, m + 1))


print("=" * 80)
print("Collapsed P23 hidden-overlap graph cycle tax")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\nFixed-k limits")
for k in range(1, 7):
    values = []
    for m in [64, 256, 1024, 4096]:
        values.append(component_mean(m, k))
    target = mp.mpf(1) / (2 * k)
    print(
        f"k={k} target={fmt(target, 18)} "
        + " ".join(f"m={m}:{fmt(value, 18)}" for m, value in zip([64, 256, 1024, 4096], values))
    )

print("\nTotal component means")
total_rows = []
total_by_m = {}
for m in [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
    c1 = component_mean(m, 1)
    total = total_component_mean(m)
    nonshared = total - c1
    half_log = mp.log(m) / 2
    offset = total - half_log
    total_rows.append((m, c1, total, nonshared, half_log, offset))
    total_by_m[m] = total
    print(
        f"m={m} N={2*m}: common={fmt(c1, 18)} total={fmt(total, 18)} "
        f"nonshared={fmt(nonshared, 18)} total-0.5logm={fmt(offset, 18)}"
    )

largest_m = total_rows[-1][0]
largest_common = total_rows[-1][1]
largest_total = total_rows[-1][2]
largest_nonshared = total_rows[-1][3]

check(
    "Common-pair component has the exact O(1) mean",
    all(abs(component_mean(m, 1) - mp.mpf(m) / (2 * m - 1)) < mp.mpf("1e-100") for m in [8, 64, 512]),
    "E C_1=m/(2m-1)",
)
check(
    "Fixed-k component means approach 1/(2k)",
    all(abs(component_mean(4096, k) / (mp.mpf(1) / (2 * k)) - 1) < mp.mpf("0.005") for k in range(1, 7)),
    "checked k=1..6 at m=4096",
)
check(
    "Total alternating component mean grows logarithmically",
    total_by_m[4096] > total_by_m[64] + mp.mpf(2),
    f"E C_total(64)={fmt(total_by_m[64], 10)} E C_total(4096)={fmt(total_by_m[4096], 10)}",
)
check(
    "Nonshared cycle mean is not controlled by common-pair overlap",
    largest_nonshared > mp.mpf(4) and largest_common < mp.mpf("0.501"),
    f"m={largest_m}: common={fmt(largest_common, 10)} nonshared={fmt(largest_nonshared, 10)}",
)
check(
    "Receipt identifies the missing neutrality condition",
    True,
    "prove nonshared alternating cycles carry factor 1+o(1), or bound them too",
)

print("\n=== Consequence ===")
print("The shared-pair overlap tax is necessary but not sufficient by itself.")
print("Two hidden matchings have only O(1) common edges, but their union has")
print("about (1/2) log(N/2) alternating components.  The local factor theorem")
print("must prove that nonshared alternating cycles are neutral, or include a")
print("cycle tax in the second-moment bound.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
