#!/usr/bin/env python3
"""
Paper 30 receipt: rooted boundary cover transfer.

The first Paper 30 receipt showed rooted boundary flags cover Hbar with the
same cover sizes as unrooted flags at N=7 and N=8.  This receipt asks the
important transfer question: do rooted covers drift less?

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


def delete_position(pi, i):
    removed = pi[i]
    return tuple(value - (1 if value > removed else 0) for j, value in enumerate(pi) if j != i)


def build_score_data(n):
    p_counts = defaultdict(int)
    reps = {}
    fibers = defaultdict(list)
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        fibers[key].append(pi)
        p_counts[key] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    return P, dict(p_counts), reps, dict(fibers)


def boundary_histograms(n, counts, fibers):
    hist = {key: defaultdict(int) for key in fibers}
    for key, fiber in fibers.items():
        for pi in fiber:
            parent_score = same_block_score(pi)
            for i in range(n):
                child = delete_position(pi, i)
                a = same_block_score(child)
                b = parent_score - a
                hist[key][(a, b)] += 1
    return {
        key: tuple(sorted((item, Fraction(count, n * counts[key])) for item, count in row.items()))
        for key, row in hist.items()
    }


def rooted_canon(bits, k, root):
    cache_key = (k, bits, root)
    if cache_key in ROOTED_CANON_CACHE:
        return ROOTED_CANON_CACHE[cache_key]
    others = [idx for idx in range(k) if idx != root]
    best = None
    for tail in permutations(others):
        order = (root,) + tail
        key = relabel_bits(bits, k, order)
        if best is None or key < best:
            best = key
    ROOTED_CANON_CACHE[cache_key] = best
    return best


def rooted_flag_counts(bits, n, k):
    counts = defaultdict(int)
    vertices = tuple(range(n))
    for root in vertices:
        for rest in combinations((v for v in vertices if v != root), k - 1):
            subset = (root,) + rest
            sub_bits = restrict_bits(bits, n, subset)
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


def partition_atoms(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atoms[tuple(feature_value(features, name, key) for name in names)].append(key)
    return atoms


def bad_rows(P, features, names, H):
    atoms = partition_atoms(P, features, names)
    bad_atoms = 0
    conflicts = 0
    bad_mass = Fraction(0)
    unresolved_mass = Fraction(0)
    for keys in atoms.values():
        if len(keys) > 1:
            unresolved_mass += sum(P[key] for key in keys)
        buckets = defaultdict(list)
        for key in keys:
            buckets[H[key]].append(key)
        if len(buckets) <= 1:
            continue
        bad_atoms += 1
        bad_mass += sum(P[key] for key in keys)
        for idx, left in enumerate(keys):
            for right in keys[idx + 1 :]:
                if H[left] != H[right]:
                    conflicts += 1
    return {
        "atoms": len(atoms),
        "bad_atoms": bad_atoms,
        "conflicts": conflicts,
        "bad_mass": bad_mass,
        "unresolved_mass": unresolved_mass,
    }


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

cover_sets = {
    "unrooted_N7": unrooted_n7,
    "unrooted_N8": unrooted_n8,
    "rooted_N7": rooted_n7,
    "rooted_N8": rooted_n8,
    "rooted_union": sorted(set(rooted_n7 + rooted_n8)),
    "mixed_union": sorted(set(unrooted_n7 + unrooted_n8 + rooted_n7 + rooted_n8)),
}

print("=" * 80)
print("Paper 30 rooted boundary cover transfer")
print("=" * 80)
print(PRECISION_LINE)

matrix = {}
for n in [7, 8]:
    print("\n" + "=" * 80)
    print(f"N={n} rooted Hbar transfer")
    print("=" * 80)
    P, counts, reps, fibers = build_score_data(n)
    H = boundary_histograms(n, counts, fibers)
    base_features = feature_maps(P, reps, n)
    root_features = rooted_feature_maps(P, reps, n)
    features = {**base_features, **root_features}
    known = feature_names(base_features, ["scalar", "interval", "regularity", "matching"])
    matrix[n] = {}
    for label, cover in cover_sets.items():
        row = bad_rows(P, features, known + cover, H)
        matrix[n][label] = row
        print(
            f"{label:<14} atoms={row['atoms']:>6}/{len(P):<6} "
            f"H_bad={row['bad_atoms']:>5} H_conf={row['conflicts']:>7} "
            f"bad_mass={fmt_frac(row['bad_mass'], 24)} "
            f"unresolved_mass={fmt_frac(row['unresolved_mass'], 24)}"
        )

check(
    "rooted N7 and N8 covers close their native levels",
    matrix[7]["rooted_N7"]["conflicts"] == 0 and matrix[8]["rooted_N8"]["conflicts"] == 0,
    f"N7={matrix[7]['rooted_N7']['conflicts']} N8={matrix[8]['rooted_N8']['conflicts']}",
)
check(
    "rooted covers drift across N",
    matrix[8]["rooted_N7"]["conflicts"] > 0 or matrix[7]["rooted_N8"]["conflicts"] > 0,
    (
        f"N7cover_on_N8={matrix[8]['rooted_N7']['conflicts']} "
        f"N8cover_on_N7={matrix[7]['rooted_N8']['conflicts']}"
    ),
)
check(
    "rooted drift is not worse than unrooted drift in audited transfer",
    matrix[8]["rooted_N7"]["conflicts"] <= matrix[8]["unrooted_N7"]["conflicts"]
    and matrix[7]["rooted_N8"]["conflicts"] <= matrix[7]["unrooted_N8"]["conflicts"],
    (
        f"N8 rooted/unrooted={matrix[8]['rooted_N7']['conflicts']}/"
        f"{matrix[8]['unrooted_N7']['conflicts']} "
        f"N7 rooted/unrooted={matrix[7]['rooted_N8']['conflicts']}/"
        f"{matrix[7]['unrooted_N8']['conflicts']}"
    ),
)
check(
    "rooted union closes both audited levels",
    matrix[7]["rooted_union"]["conflicts"] == 0 and matrix[8]["rooted_union"]["conflicts"] == 0,
    f"N7={matrix[7]['rooted_union']['conflicts']} N8={matrix[8]['rooted_union']['conflicts']}",
)
check(
    "mixed union remains non-lookup at N=8",
    matrix[8]["mixed_union"]["atoms"] < 14794,
    f"atoms={matrix[8]['mixed_union']['atoms']}",
)

print("\n=== Rooted-transfer status ===")
print(
    "Rooted boundary flags do not eliminate cover drift, but they are not worse "
    "than unrooted flags in the audited transfer and their union closes both "
    "levels.  The likely invariant is still controlled drift of a rooted "
    "operator family, not fixed rooted names."
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
