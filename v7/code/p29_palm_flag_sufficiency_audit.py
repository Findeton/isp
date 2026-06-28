#!/usr/bin/env python3
"""
Paper 29 receipt: causal Palm-flag sufficiency audit.

This is a finite diagnostic for the causal Palm-flag branch.  It does not prove
the asymptotic Palm theorem.  It asks whether rooted, endpoint-symmetric,
record-intrinsic operators add likelihood information beyond the known scalar /
interval / regularity / matching sectors in the staged/fiber toy.

The rooted operators here are:

1. pair-rooted 3-flags: unordered root pair plus one outside record;
2. pair-rooted 4-flags: unordered root pair plus two outside records;
3. interval-overlap flags: two causal intervals and the sizes of their
   interiors, intersection, and union.

All roots are treated symmetrically; no endpoint orientation or hidden label is
used.
"""

from collections import defaultdict
from itertools import combinations, permutations
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    bit_index,
    build_projected_laws,
    feature_maps,
    has_rel,
    project_log_likelihood,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def fmt(x, digits=30):
    return mp.nstr(mp.mpf(x), digits)


def encode_allowed(bits, n, vertices, allowed_orders):
    k = len(vertices)
    best = None
    for order in allowed_orders:
        key = 0
        for a, old_pos_a in enumerate(order):
            old_a = vertices[old_pos_a]
            for b, old_pos_b in enumerate(order):
                if a == b:
                    continue
                old_b = vertices[old_pos_b]
                if has_rel(bits, n, old_a, old_b):
                    key |= 1 << bit_index(k, a, b)
        if best is None or key < best:
            best = key
    return best


PAIR3_ORDERS = [(0, 1, 2), (1, 0, 2)]
PAIR4_ORDERS = [
    root + tail
    for root in [(0, 1), (1, 0)]
    for tail in [(2, 3), (3, 2)]
]


def pair_rooted3_counts(bits, n):
    counts = defaultdict(int)
    for a, b in combinations(range(n), 2):
        for c in range(n):
            if c == a or c == b:
                continue
            signature = encode_allowed(bits, n, (a, b, c), PAIR3_ORDERS)
            counts[signature] += 1
    return dict(counts)


def pair_rooted4_counts(bits, n):
    counts = defaultdict(int)
    for a, b in combinations(range(n), 2):
        rest = [v for v in range(n) if v != a and v != b]
        for c, d in combinations(rest, 2):
            signature = encode_allowed(bits, n, (a, b, c, d), PAIR4_ORDERS)
            counts[signature] += 1
    return dict(counts)


def interval_vertices(bits, n, x, y):
    return frozenset(
        z
        for z in range(n)
        if z != x and z != y and has_rel(bits, n, x, z) and has_rel(bits, n, z, y)
    )


def bin_small(value, cap):
    return min(value, cap)


def interval_overlap_counts(bits, n):
    intervals = []
    for x in range(n):
        for y in range(n):
            if x != y and has_rel(bits, n, x, y):
                intervals.append(interval_vertices(bits, n, x, y))
    counts = defaultdict(int)
    for left, right in combinations(intervals, 2):
        s1, s2 = sorted((len(left), len(right)))
        inter = len(left & right)
        union = len(left | right)
        key = (
            bin_small(s1, 3),
            bin_small(s2, 3),
            bin_small(inter, 2),
            bin_small(union, 4),
        )
        counts[key] += 1
    return dict(counts)


def add_sparse_count_group(features, P, reps, n, group, builder, prefix):
    by_record = {}
    universe = set()
    for record_key in P:
        counts = builder(reps[record_key], n)
        by_record[record_key] = counts
        universe.update(counts)
    features[group] = defaultdict(dict)
    for key in sorted(universe):
        name = f"{prefix}_{key}"
        for record_key in P:
            features[group][name][record_key] = by_record[record_key].get(key, 0)


print("=" * 80)
print("Paper 29 causal Palm-flag sufficiency audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, Q, reps = build_projected_laws(n, weight_base=3)
features = feature_maps(P, reps, n)
add_sparse_count_group(features, P, reps, n, "palm_pair3", pair_rooted3_counts, "pair3")
add_sparse_count_group(features, P, reps, n, "palm_pair4", pair_rooted4_counts, "pair4")
add_sparse_count_group(features, P, reps, n, "palm_overlap", interval_overlap_counts, "overlap")

families = [
    ("known", ["scalar", "interval", "regularity", "matching"]),
    ("known+palm3", ["scalar", "interval", "regularity", "matching", "palm_pair3"]),
    (
        "known+palm3+palm4",
        ["scalar", "interval", "regularity", "matching", "palm_pair3", "palm_pair4"],
    ),
    (
        "known+palm3+palm4+overlap",
        [
            "scalar",
            "interval",
            "regularity",
            "matching",
            "palm_pair3",
            "palm_pair4",
            "palm_overlap",
        ],
    ),
    ("known+flags3", ["scalar", "interval", "regularity", "matching", "flags3"]),
]

results = {}
print(f"N={n} classes={len(P)}")
print(
    "feature counts: "
    f"palm3={len(features['palm_pair3'])} "
    f"palm4={len(features['palm_pair4'])} "
    f"overlap={len(features['palm_overlap'])}"
)
for label, groups in families:
    result = project_log_likelihood(P, Q, features, groups)
    results[label] = result
    print(
        f"{label:<32} rank={result['rank']:>4} "
        f"R2={fmt(result['r2'], 24)} "
        f"res_norm={fmt(result['residual_norm'], 24)} "
        f"max_abs={fmt(result['max_abs_residual'], 24)}"
    )

known = results["known"]
palm3 = results["known+palm3"]
palm34 = results["known+palm3+palm4"]
palm_all = results["known+palm3+palm4+overlap"]
flags3 = results["known+flags3"]

check(
    "rooted Palm feature families are nonempty",
    len(features["palm_pair3"]) > 0
    and len(features["palm_pair4"]) > 0
    and len(features["palm_overlap"]) > 0,
    f"counts={len(features['palm_pair3'])},{len(features['palm_pair4'])},{len(features['palm_overlap'])}",
)
check(
    "pair-rooted 3-flags improve over known sectors",
    palm3["r2"] > known["r2"],
    f"known={fmt(known['r2'], 18)} palm3={fmt(palm3['r2'], 18)}",
)
check(
    "higher rooted/overlap Palm features do not decrease captured likelihood",
    palm_all["r2"] >= palm34["r2"] >= palm3["r2"],
    f"palm3={fmt(palm3['r2'], 18)} palm34={fmt(palm34['r2'], 18)} all={fmt(palm_all['r2'], 18)}",
)
check(
    "Palm features give a material but incomplete improvement",
    palm_all["r2"] - known["r2"] > mp.mpf("0.075") and palm_all["r2"] < mp.mpf("0.90"),
    f"known={fmt(known['r2'], 18)} palm_all={fmt(palm_all['r2'], 24)} rank={palm_all['rank']}",
)
check(
    "Palm features are comparable to unrooted flags3 but not declared final",
    palm_all["r2"] > known["r2"] and flags3["r2"] > known["r2"],
    f"palm_all={fmt(palm_all['r2'], 18)} flags3={fmt(flags3['r2'], 18)}",
)

print("\n=== Palm-flag status ===")
print(
    "Rooted, endpoint-symmetric Palm flags add real projected-likelihood "
    "information beyond the known sectors, but the audited rooted family does "
    "not close the staged/fiber likelihood.  This supports causal Palm-flag "
    "geometry as a record-intrinsic carrier, not as a finished sufficiency "
    "theorem."
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
