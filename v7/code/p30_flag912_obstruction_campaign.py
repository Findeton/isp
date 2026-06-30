#!/usr/bin/env python3
"""
Paper 30 receipt: decode and audit the flag5_912 obstruction.

The backward-then-forward campaign found that adding one operator,

    flags5:flag5_912

to the fixed N=8 one-hole cover makes all k=1..4 boundary histograms visible
at N=8 while staying non-lookup there.  This receipt asks whether that is a
coincidental flag id or a structurally identifiable boundary obstruction.

All quantities are exact integer/Fraction counts.  If mpmath is available it
is set to dps=140 for decimal formatting; otherwise no floating arithmetic is
used.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import math
import sys

from p29_projected_likelihood_basis_audit import (
    canon_bits,
    degree_moments,
    flag_counts,
    fmt_frac,
    has_rel,
    height,
    interval_counts,
    matching_count,
    permutation_order_bits,
    perms,
    relation_count,
    relation_edges,
    restrict_bits,
    same_block_score,
    width,
)

try:
    import mpmath as mp

    mp.mp.dps = 140
    PRECISION_LINE = f"mp.dps = {mp.mp.dps}"
except ModuleNotFoundError:
    PRECISION_LINE = (
        "exact integer/Fraction arithmetic; mpmath unavailable; "
        "no floating arithmetic used"
    )

sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(10000)

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def delete_positions(pi, positions):
    removed_positions = set(positions)
    remaining_values = [value for idx, value in enumerate(pi) if idx not in removed_positions]
    rank = {value: idx for idx, value in enumerate(sorted(remaining_values))}
    return tuple(rank[value] for value in remaining_values)


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


def multihole_histograms(n, k, counts, fibers):
    hist = {key: defaultdict(int) for key in fibers}
    for key, fiber in fibers.items():
        for pi in fiber:
            parent_score = same_block_score(pi)
            for positions in combinations(range(n), k):
                child = delete_positions(pi, positions)
                a = same_block_score(child)
                b = parent_score - a
                hist[key][(a, b)] += 1
    denom = math.comb(n, k)
    return {
        key: tuple(sorted((item, Fraction(count, denom * counts[key])) for item, count in row.items()))
        for key, row in hist.items()
    }


def light_feature_maps(P, reps, n):
    features = {
        "scalar": defaultdict(dict),
        "interval": defaultdict(dict),
        "regularity": defaultdict(dict),
        "matching": defaultdict(dict),
        "flags3": defaultdict(dict),
        "flags4": defaultdict(dict),
        "flags5": defaultdict(dict),
    }
    flag_keys = {3: set(), 4: set(), 5: set()}
    flag_by_record = {}
    for key, bits in reps.items():
        edges = relation_edges(bits, n)
        rel = relation_count(bits, n)
        h = height(bits, n)
        w = width(bits, n)
        intervals = interval_counts(bits, n)
        _deg1, deg2, deg3, dmax, dmin = degree_moments(bits, n)
        m2 = matching_count(edges, 2)
        m3 = matching_count(edges, 3)

        features["scalar"]["relations"][key] = rel
        features["scalar"]["height"][key] = h
        features["scalar"]["width"][key] = w
        for idx, value in enumerate(intervals[:5]):
            features["interval"][f"interval_{idx}"][key] = value
        features["interval"]["interval_tail_ge5"][key] = sum(intervals[5:])
        features["regularity"]["degree_sum2"][key] = deg2
        features["regularity"]["degree_sum3"][key] = deg3
        features["regularity"]["degree_max"][key] = dmax
        features["regularity"]["degree_min"][key] = dmin
        features["regularity"]["degree_range"][key] = dmax - dmin
        features["matching"]["matching_2"][key] = m2
        features["matching"]["matching_3"][key] = m3

        flag_by_record[key] = {}
        for flag_size in [3, 4, 5]:
            counts = flag_counts(bits, n, flag_size)
            flag_by_record[key][flag_size] = counts
            flag_keys[flag_size].update(counts)

    for flag_size in [3, 4, 5]:
        bucket = features[f"flags{flag_size}"]
        for flag_key in sorted(flag_keys[flag_size]):
            name = f"flag{flag_size}_{flag_key}"
            for record_key in P:
                bucket[name][record_key] = flag_by_record[record_key][flag_size].get(flag_key, 0)
    return features


def feature_names(features, groups):
    return [
        f"{group}:{feature_name}"
        for group in groups
        for feature_name in sorted(features[group])
    ]


def known_feature_names(features):
    return feature_names(features, ["scalar", "interval", "regularity", "matching"])


def n8_cover_feature_names(features):
    return known_feature_names(features) + [
        "flags3:flag3_36",
        "flags5:flag5_549376",
        "flags4:flag4_2176",
        "flags4:flag4_206",
        "flags5:flag5_24576",
    ]


def valid_names(features, names):
    out = []
    for name in names:
        group, feature = name.split(":", 1)
        if group in features and feature in features[group]:
            out.append(name)
    return out


def feature_value(features, name, key):
    group, feature = name.split(":", 1)
    return features[group][feature].get(key, 0)


def compress(raw):
    palette = {value: idx for idx, value in enumerate(sorted(set(raw.values())))}
    return {key: palette[value] for key, value in raw.items()}


def colors_from_features(P, features, names):
    return compress({
        key: tuple(feature_value(features, name, key) for name in names)
        for key in P
    })


def atoms_from_colors(colors):
    atoms = defaultdict(list)
    for key, color in colors.items():
        atoms[color].append(key)
    return atoms


def conflict_pairs(colors, invariant):
    atoms = atoms_from_colors(colors)
    conflicts = []
    for keys in atoms.values():
        for idx, left in enumerate(keys):
            for right in keys[idx + 1 :]:
                if invariant[left] != invariant[right]:
                    conflicts.append((left, right))
    return conflicts


def conflict_count(colors, invariant):
    return len(conflict_pairs(colors, invariant)), len(atoms_from_colors(colors))


def all_five_record_keys():
    return sorted({
        canon_bits(permutation_order_bits(pi), 5)
        for pi in perms(5)
    })


def relations(bits, n=5):
    return [
        (i, j)
        for i in range(n)
        for j in range(n)
        if i != j and has_rel(bits, n, i, j)
    ]


def covers(bits, n=5):
    out = []
    for i, j in relations(bits, n):
        if not any(
            k != i and k != j and has_rel(bits, n, i, k) and has_rel(bits, n, k, j)
            for k in range(n)
        ):
            out.append((i, j))
    return out


def minima(bits, n=5):
    return [
        i
        for i in range(n)
        if not any(has_rel(bits, n, j, i) for j in range(n) if j != i)
    ]


def maxima(bits, n=5):
    return [
        i
        for i in range(n)
        if not any(has_rel(bits, n, i, j) for j in range(n) if j != i)
    ]


def vertex_profiles(bits, n=5):
    profiles = []
    for i in range(n):
        lower = sum(1 for j in range(n) if has_rel(bits, n, j, i))
        upper = sum(1 for j in range(n) if has_rel(bits, n, i, j))
        incomparable = n - 1 - lower - upper
        profiles.append((lower, upper, incomparable))
    return tuple(sorted(profiles))


def descriptor(bits):
    return (
        relation_count(bits, 5),
        height(bits, 5),
        width(bits, 5),
        tuple(interval_counts(bits, 5)),
        vertex_profiles(bits, 5),
        len(minima(bits, 5)),
        len(maxima(bits, 5)),
        len(covers(bits, 5)),
    )


def coarse_descriptor(bits):
    return (
        relation_count(bits, 5),
        height(bits, 5),
        width(bits, 5),
        tuple(interval_counts(bits, 5)),
        len(minima(bits, 5)),
        len(maxima(bits, 5)),
        len(covers(bits, 5)),
    )


def flag_mapping(features, flag_name):
    group, feature = flag_name.split(":", 1)
    return features[group][feature]


print("=" * 80)
print("Paper 30 flag5_912 obstruction campaign")
print("=" * 80)
print(PRECISION_LINE)

target_flags = [912, 24606, 17304]
all_keys = all_five_record_keys()

print("\n" + "=" * 80)
print("Decode the three multi-hole repair flags")
print("=" * 80)
for key in target_flags:
    print(f"flag5_{key}")
    print(f"  relations={relations(key)}")
    print(f"  cover_edges={covers(key)}")
    print(
        "  "
        f"height={height(key, 5)} width={width(key, 5)} "
        f"relations={relation_count(key, 5)} intervals={interval_counts(key, 5)} "
        f"minima={minima(key)} maxima={maxima(key)} profiles={vertex_profiles(key)}"
    )

same_full = [key for key in all_keys if descriptor(key) == descriptor(912)]
same_coarse = [key for key in all_keys if coarse_descriptor(key) == coarse_descriptor(912)]
print("\nstructural uniqueness:")
print(f"  all five-record types={len(all_keys)}")
print(f"  same coarse descriptor as flag5_912={same_coarse}")
print(f"  same full descriptor as flag5_912={same_full}")

records = {}
counts_by_n = {}
reps_by_n = {}
fibers_by_n = {}
features_by_n = {}
hist_by_n_k = {7: {}, 8: {}}

for n in [7, 8]:
    P, counts, reps, fibers = build_score_data(n)
    records[n] = P
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    fibers_by_n[n] = fibers
    features_by_n[n] = light_feature_maps(P, reps, n)
    for k in [1, 2, 3, 4]:
        hist_by_n_k[n][k] = multihole_histograms(n, k, counts, fibers)

base_colors = {}
for n in [7, 8]:
    base_colors[n] = colors_from_features(
        records[n],
        features_by_n[n],
        valid_names(features_by_n[n], n8_cover_feature_names(features_by_n[n])),
    )

candidate_repairs = [
    "flags5:flag5_24606",
    "flags5:flag5_912",
    "flags5:flag5_17304",
]

print("\n" + "=" * 80)
print("Base conflicts and separation by the three repair flags at N=8")
print("=" * 80)
separation = {}
for k in [1, 2, 3, 4]:
    pairs = conflict_pairs(base_colors[8], hist_by_n_k[8][k])
    separation[k] = {}
    print(f"k={k} base_conflicts={len(pairs)}")
    for flag in candidate_repairs:
        mapping = flag_mapping(features_by_n[8], flag)
        separated = sum(1 for left, right in pairs if mapping[left] != mapping[right])
        separation[k][flag] = separated
        print(f"  {flag:<22} separates={separated}/{len(pairs)}")

print("\n" + "=" * 80)
print("Single-extra repair scan at N=8")
print("=" * 80)
single_solvers = []
single_rows = []
all_candidates = feature_names(features_by_n[8], ["flags3", "flags4", "flags5"])
for extra in all_candidates:
    colors = colors_from_features(
        records[8],
        features_by_n[8],
        valid_names(features_by_n[8], n8_cover_feature_names(features_by_n[8]) + [extra]),
    )
    counts = {k: conflict_count(colors, hist_by_n_k[8][k])[0] for k in [1, 2, 3, 4]}
    atoms = conflict_count(colors, hist_by_n_k[8][1])[1]
    if all(value == 0 for value in counts.values()) and atoms < len(records[8]):
        single_solvers.append((extra, atoms))
    if extra in candidate_repairs:
        single_rows.append((extra, atoms, counts))

for extra, atoms, counts in single_rows:
    print(
        f"{extra:<22} atoms={atoms:>6}/{len(records[8])} "
        + " ".join(f"k{k}={counts[k]:>3}" for k in [1, 2, 3, 4])
    )
print(f"single nonlookup solvers={single_solvers}")

print("\n" + "=" * 80)
print("Scale warning for the unique repair")
print("=" * 80)
scale_rows = {}
for n in [7, 8]:
    colors = colors_from_features(
        records[n],
        features_by_n[n],
        valid_names(features_by_n[n], n8_cover_feature_names(features_by_n[n]) + ["flags5:flag5_912"]),
    )
    row = {
        "atoms": conflict_count(colors, hist_by_n_k[n][1])[1],
        "conflicts": {k: conflict_count(colors, hist_by_n_k[n][k])[0] for k in [1, 2, 3, 4]},
    }
    scale_rows[n] = row
    print(
        f"N={n} atoms={row['atoms']}/{len(records[n])} "
        + " ".join(f"k{k}={row['conflicts'][k]}" for k in [1, 2, 3, 4])
    )

check(
    "flag5_912 is structurally identifiable, not just an opaque id",
    same_full == [912],
    f"same_full={same_full}",
)
check(
    "coarse descriptors are insufficient and need the local profile",
    len(same_coarse) > 1 and 912 in same_coarse,
    f"same_coarse={same_coarse}",
)
check(
    "flag5_912 is the only single nonlookup flags3/4/5 repair at N=8",
    single_solvers == [("flags5:flag5_912", 14790)],
    f"single_solvers={single_solvers}",
)
check(
    "flag5_912 separates every base multi-hole conflict at N=8",
    all(separation[k]["flags5:flag5_912"] == len(conflict_pairs(base_colors[8], hist_by_n_k[8][k])) for k in [2, 3, 4]),
    ", ".join(
        f"k{k}={separation[k]['flags5:flag5_912']}/{len(conflict_pairs(base_colors[8], hist_by_n_k[8][k]))}"
        for k in [2, 3, 4]
    ),
)
check(
    "flag5_912 repairs N=8 without lookup but repairs N=7 by lookup",
    scale_rows[8]["atoms"] < len(records[8]) and scale_rows[7]["atoms"] == len(records[7]),
    f"N8={scale_rows[8]['atoms']}/{len(records[8])} N7={scale_rows[7]['atoms']}/{len(records[7])}",
)

print("\n=== Campaign status ===")
print(
    "flag5_912 is not merely a numerical label.  It is the unique five-record "
    "type with a lopsided height-2 hinge profile in the audited 2D-permutation "
    "flag universe, and it is the only single local flag that repairs all "
    "k=1..4 multi-hole boundary histograms at N=8 without lookup.  Its N=7 "
    "lookup collapse keeps the result finite and scoped, but the obstruction "
    "itself is structurally sharp."
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
