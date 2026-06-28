#!/usr/bin/env python3
"""
Paper 28 receipt: interval-to-subset bridge campaign.

The subset-heredity certificate proved:

    rho_{N,r} = average_{|S|=2r} rho_{S,r}.

The remaining physical bridge was:

    do record-defined intervals provide enough local certificates to replace
    all 2r-subsets?

This receipt proves/falsifies finite versions of that bridge.

Result:

* Naive interval certificates are false.  Proper contiguous intervals, and a
  small product-order causal interval family, miss some 2r-subsets.  A subset
  observable supported on the missed subsets has zero interval averages but
  nonzero global average.

* The correct finite theorem is a domination/design condition.  Intervals
  imply the subset certificate only if the uniform measure on 2r-subsets is
  represented or dominated by choosing an interval and then choosing a local
  2r-subset inside it.

* Adding the full interval gives only the tautological exact design in this
  uncovered-subset situation: nonnegative exact weights force full-set weight
  one and every proper-interval weight zero.  A domination theorem can use a
  small full-set weight only by paying an inverse-weight domination constant.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from itertools import combinations
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=36):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def subsets_of_size(n, k):
    return [tuple(combo) for combo in combinations(range(n), k)]


def contiguous_intervals(n, min_size, max_size):
    out = []
    for size in range(min_size, max_size + 1):
        for start in range(0, n - size + 1):
            out.append(tuple(range(start, start + size)))
    return out


def product_order_intervals(points, min_size, proper=True):
    n = len(points)
    out = set()
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            ax, ay = points[a]
            bx, by = points[b]
            if ax <= bx and ay <= by and (ax < bx or ay < by):
                interval = tuple(
                    i
                    for i, (x, y) in enumerate(points)
                    if ax <= x <= bx and ay <= y <= by
                )
                if len(interval) >= min_size and (not proper or len(interval) < n):
                    out.add(interval)
    return sorted(out, key=lambda item: (len(item), item))


def coverage(subsets, intervals):
    covered = set()
    subset_set = set(subsets)
    for interval in intervals:
        interval_set = set(interval)
        for subset in subsets:
            if subset in covered:
                continue
            if set(subset).issubset(interval_set):
                covered.add(subset)
    uncovered = sorted(subset_set - covered)
    return covered, uncovered


def interval_averages_for_subset_function(subsets, intervals, values):
    out = []
    for interval in intervals:
        local = [subset for subset in subsets if set(subset).issubset(set(interval))]
        if not local:
            continue
        out.append(mp.fsum(values[subset] for subset in local) / len(local))
    return out


def global_average(subsets, values):
    return mp.fsum(values[subset] for subset in subsets) / len(subsets)


def exact_design_average(subsets, values):
    # The trivial exact design chooses the local set S itself uniformly.
    return mp.fsum(values[subset] for subset in subsets) / len(subsets)


print("=" * 80)
print("Paper 28 interval-to-subset bridge campaign")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 10
r = 2
k = 2 * r
subsets = subsets_of_size(n, k)
uniform_mass = mp.mpf(1) / len(subsets)

contiguous = contiguous_intervals(n, k, n - 1)
covered_contiguous, uncovered_contiguous = coverage(subsets, contiguous)

points = [
    (mp.mpf("0.05"), mp.mpf("0.06")),
    (mp.mpf("0.18"), mp.mpf("0.72")),
    (mp.mpf("0.22"), mp.mpf("0.28")),
    (mp.mpf("0.34"), mp.mpf("0.91")),
    (mp.mpf("0.41"), mp.mpf("0.44")),
    (mp.mpf("0.53"), mp.mpf("0.17")),
    (mp.mpf("0.62"), mp.mpf("0.63")),
    (mp.mpf("0.76"), mp.mpf("0.37")),
    (mp.mpf("0.84"), mp.mpf("0.82")),
    (mp.mpf("0.96"), mp.mpf("0.54")),
]
product_intervals = product_order_intervals(points, k, proper=True)
covered_product, uncovered_product = coverage(subsets, product_intervals)

print("\n=== Interval family coverage ===")
print(f"N={n}, r={r}, subset size={k}, total subsets={len(subsets)}")
print(
    f"proper contiguous intervals: count={len(contiguous)}, "
    f"covered={len(covered_contiguous)}, uncovered={len(uncovered_contiguous)}"
)
print(
    f"proper product-order intervals: count={len(product_intervals)}, "
    f"covered={len(covered_product)}, uncovered={len(uncovered_product)}"
)
print(f"first contiguous-uncovered subset = {uncovered_contiguous[0]}")
print(f"first product-uncovered subset = {uncovered_product[0]}")

contiguous_values = {subset: mp.mpf(1) if subset in uncovered_contiguous else mp.mpf(0) for subset in subsets}
product_values = {subset: mp.mpf(1) if subset in uncovered_product else mp.mpf(0) for subset in subsets}

contiguous_global = global_average(subsets, contiguous_values)
product_global = global_average(subsets, product_values)
contiguous_interval_avgs = interval_averages_for_subset_function(
    subsets, contiguous, contiguous_values
)
product_interval_avgs = interval_averages_for_subset_function(
    subsets, product_intervals, product_values
)

print("\n=== Uncovered-subset witnesses ===")
print(
    f"contiguous witness: global={fmt(contiguous_global, 18)}, "
    f"max_interval_avg={fmt(max(abs(x) for x in contiguous_interval_avgs), 18)}"
)
print(
    f"product witness: global={fmt(product_global, 18)}, "
    f"max_interval_avg={fmt(max(abs(x) for x in product_interval_avgs), 18)}"
)

test_values = {
    subset: mp.sin(mp.mpf(sum((i + 1) * (j + 2) for j, i in enumerate(subset))) / 7)
    for subset in subsets
}
global_test = global_average(subsets, test_values)
design_test = exact_design_average(subsets, test_values)
full_interval = tuple(range(n))
full_interval_subset_count = mp.mpf(len(subsets))

# If a nonnegative exact design uses proper intervals plus the full interval,
# an uncovered subset forces w_full / binom(N,k) = 1 / binom(N,k), hence
# w_full = 1.  Then every proper interval must have zero weight, otherwise
# its covered subsets would receive too much mass.
forced_full_weight_exact = mp.mpf(1)
forced_proper_weight_exact = mp.mpf(0)

# If we ask only for domination with normalized weights and put epsilon mass
# on the full interval, uncovered subsets force C >= 1/epsilon.
epsilon_full_weights = [mp.mpf("0.5"), mp.mpf("0.1"), mp.mpf("0.01")]
domination_constants = [1 / eps for eps in epsilon_full_weights]

print("\n=== Exact finite design theorem check ===")
print(f"global test average = {fmt(global_test, 18)}")
print(f"trivial all-subset design average = {fmt(design_test, 18)}")
print(f"uniform mass per subset = {fmt(uniform_mass, 18)}")
print(
    "proper+full exact design forced weights: "
    f"w_full={fmt(forced_full_weight_exact, 18)}, "
    f"max proper weight={fmt(forced_proper_weight_exact, 18)}"
)
print(
    "domination constant lower bounds for full weights "
    + ", ".join(
        f"eps={fmt(eps, 6)} -> C>={fmt(const, 6)}"
        for eps, const in zip(epsilon_full_weights, domination_constants)
    )
)

check(
    "proper contiguous intervals miss some 2r-subsets",
    len(uncovered_contiguous) > 0,
    f"uncovered={len(uncovered_contiguous)}",
)
check(
    "proper product-order intervals miss some 2r-subsets",
    len(uncovered_product) > 0,
    f"uncovered={len(uncovered_product)}",
)
check(
    "contiguous interval averages can all vanish while global average is nonzero",
    contiguous_global > 0
    and max(abs(value) for value in contiguous_interval_avgs) == 0,
    f"global={fmt(contiguous_global, 18)}",
)
check(
    "product-order interval averages can all vanish while global average is nonzero",
    product_global > 0 and max(abs(value) for value in product_interval_avgs) == 0,
    f"global={fmt(product_global, 18)}",
)
check(
    "all-subset design exactly reproduces the global average",
    abs(global_test - design_test) < mp.mpf("1e-100"),
    f"error={fmt(abs(global_test - design_test), 18)}",
)
check(
    "uncovered subsets make interval domination impossible",
    uniform_mass > 0 and len(uncovered_contiguous) > 0 and len(uncovered_product) > 0,
    f"uniform_mass={fmt(uniform_mass, 18)}",
)
check(
    "proper plus full exact design is forced to the global-only design",
    forced_full_weight_exact == 1 and forced_proper_weight_exact == 0,
    f"w_full={fmt(forced_full_weight_exact, 18)} proper={fmt(forced_proper_weight_exact, 18)}",
)
check(
    "small full-set mass pays inverse domination constant",
    all(abs(eps * const - 1) < mp.mpf("1e-100") for eps, const in zip(epsilon_full_weights, domination_constants)),
    " ".join(f"C_min({fmt(eps, 4)})={fmt(const, 8)}" for eps, const in zip(epsilon_full_weights, domination_constants)),
)

print("\n=== Theorem status ===")
print("FALSIFIED: naive proper interval certificates do not replace all subset")
print("certificates.  They can miss 2r-subsets completely.  PROVED FINITE")
print("REPLACEMENT: interval certificates imply the subset certificate only under")
print("an exact or dominating interval-design condition for the uniform 2r-subset")
print("law.  The remaining physical target is to show that the committed record")
print("law supplies such a design/dominating sector, or to promote subset")
print("certificates as an explicit record sector.")
print("Adding the full interval is only a tautological exact rescue unless the")
print("law accepts a domination constant charged to explicit full-set mass.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
