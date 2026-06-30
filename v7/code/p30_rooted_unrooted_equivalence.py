#!/usr/bin/env python3
"""
Paper 30 receipt: rooted/unrooted cover equivalence.

The rooted boundary cover and unrooted cover receipts found equal cover sizes
and identical transfer behavior.  This receipt checks whether the audited
rooted covers are just coordinate changes of the unrooted covers at the record
partition level.

All finite counts are exact integers/Fractions.  Decimal reporting uses
mpmath with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
import math
import sys

from p29_projected_likelihood_basis_audit import (
    canon_bits,
    feature_maps,
    fmt_frac,
    permutation_order_bits,
    perms,
    relabel_bits,
    restrict_bits,
    same_block_score,
)

sys.stdout.reconfigure(line_buffering=True)
try:
    import mpmath as mp

    mp.mp.dps = 140
    PRECISION_LINE = f"mp.dps = {mp.mp.dps}"
except ModuleNotFoundError:
    mp = None
    PRECISION_LINE = (
        "exact integer/Fraction arithmetic; mpmath unavailable; "
        "no floating arithmetic used"
    )

checks = []
ROOTED_CANON_CACHE = {}


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def build_records(n):
    p_counts = defaultdict(int)
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        p_counts[key] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    return P, reps


def rooted_canon(bits, k, root):
    cache_key = (k, bits, root)
    if cache_key in ROOTED_CANON_CACHE:
        return ROOTED_CANON_CACHE[cache_key]
    others = [idx for idx in range(k) if idx != root]
    best = None
    for tail in permutations(others):
        key = relabel_bits(bits, k, (root,) + tail)
        if best is None or key < best:
            best = key
    ROOTED_CANON_CACHE[cache_key] = best
    return best


def rooted_flag_counts(bits, n, k):
    counts = defaultdict(int)
    vertices = tuple(range(n))
    for root in vertices:
        for rest in combinations((v for v in vertices if v != root), k - 1):
            sub_bits = restrict_bits(bits, n, (root,) + rest)
            counts[rooted_canon(sub_bits, k, 0)] += 1
    return dict(counts)


def rooted_feature_maps(P, reps, n, ks=(2, 3, 4, 5)):
    rooted_by_record = {}
    all_keys = {k: set() for k in ks}
    for key in P:
        rooted_by_record[key] = {}
        bits = reps[key]
        for k in ks:
            counts = rooted_flag_counts(bits, n, k)
            rooted_by_record[key][k] = counts
            all_keys[k].update(counts)
    features = {f"root{k}": defaultdict(dict) for k in ks}
    for k in ks:
        for rooted_key in sorted(all_keys[k]):
            name = f"root{k}_{rooted_key}"
            for record_key in P:
                features[f"root{k}"][name][record_key] = rooted_by_record[record_key][k].get(rooted_key, 0)
    return features


def feature_names(features, groups):
    names = []
    for group in groups:
        for feature_name in sorted(features[group]):
            names.append(f"{group}:{feature_name}")
    return names


def feature_value(features, name, key):
    group, feature = name.split(":", 1)
    return features.get(group, {}).get(feature, {}).get(key, 0)


def partition(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atoms[tuple(feature_value(features, name, key) for name in names)].append(key)
    return {frozenset(keys) for keys in atoms.values()}


unrooted_n7 = [
    "flags3:flag3_36",
    "flags4:flag4_2062",
    "flags4:flag4_192",
    "flags5:flag5_525184",
]
unrooted_n8 = [
    "flags3:flag3_36",
    "flags5:flag5_549376",
    "flags4:flag4_2176",
    "flags4:flag4_206",
    "flags5:flag5_24576",
]
rooted_n7 = [
    "root3:root3_36",
    "root4:root4_212",
    "root4:root4_192",
    "root5:root5_142",
]
rooted_n8 = [
    "root3:root3_36",
    "root5:root5_33952",
    "root4:root4_2176",
    "root4:root4_206",
    "root5:root5_160",
]

print("=" * 80)
print("Paper 30 rooted/unrooted cover equivalence")
print("=" * 80)
print(PRECISION_LINE)

results = {}
for n, unrooted_cover, rooted_cover in [(7, unrooted_n7, rooted_n7), (8, unrooted_n8, rooted_n8)]:
    print("\n" + "=" * 80)
    print(f"N={n} partition comparison")
    print("=" * 80)
    P, reps = build_records(n)
    base = feature_maps(P, reps, n)
    roots = rooted_feature_maps(P, reps, n)
    features = {**base, **roots}
    known = feature_names(base, ["scalar", "interval", "regularity", "matching"])
    part_unrooted = partition(P, features, known + unrooted_cover)
    part_rooted = partition(P, features, known + rooted_cover)
    part_both = partition(P, features, known + unrooted_cover + rooted_cover)
    same = part_unrooted == part_rooted
    print(f"unrooted atoms={len(part_unrooted)} rooted atoms={len(part_rooted)} both atoms={len(part_both)}")
    print(f"same_partition={same}")
    if not same:
        only_u = len(part_unrooted - part_rooted)
        only_r = len(part_rooted - part_unrooted)
        print(f"partition differences: unrooted_only_atoms={only_u} rooted_only_atoms={only_r}")
    results[n] = {
        "same": same,
        "unrooted_atoms": len(part_unrooted),
        "rooted_atoms": len(part_rooted),
        "both_atoms": len(part_both),
    }

check(
    "rooted and unrooted audited covers induce the same partition at N=7",
    results[7]["same"],
    f"atoms={results[7]['unrooted_atoms']}/{results[7]['rooted_atoms']}",
)
check(
    "rooted and unrooted audited covers induce the same partition at N=8",
    results[8]["same"],
    f"atoms={results[8]['unrooted_atoms']}/{results[8]['rooted_atoms']}",
)
check(
    "adding rooted to unrooted does not refine audited cover partitions",
    results[7]["both_atoms"] == results[7]["unrooted_atoms"]
    and results[8]["both_atoms"] == results[8]["unrooted_atoms"],
    f"N7 both={results[7]['both_atoms']} N8 both={results[8]['both_atoms']}",
)

print("\n=== Equivalence status ===")
print(
    "The audited rooted covers are not a smaller theorem; they are coordinate "
    "translations of the unrooted Hbar covers at the partition level.  This "
    "clarifies the invariant: the finite cover is a partition of record space, "
    "and rooted/unrooted flags are two coordinate systems for the same partition "
    "in the audited window."
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
