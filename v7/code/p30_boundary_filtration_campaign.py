#!/usr/bin/env python3
"""
Paper 30 receipt: record-intrinsic boundary filtration campaign.

This receipt attacks the nontrivial existence target:

    find record-intrinsic partitions P_N such that Hbar_N is measurable
    and deletion/insertion moves them with controlled drift.

The test is deliberately not allowed to use hidden labels, hidden permutation
identity, or Hbar lookup as a generator.  It starts from committed record
features and refines them by record-level deletion and insertion profiles.

All counts/probabilities are exact integers/Fractions.  Decimal reporting uses
mpmath with dps=140 when available; otherwise no floating arithmetic is used.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import math
import sys

from p29_projected_likelihood_basis_audit import (
    canon_bits,
    fmt_frac,
    degree_moments,
    flag_counts,
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


def feature_names(features, groups):
    names = []
    for group in groups:
        for feature_name in sorted(features[group]):
            names.append(f"{group}:{feature_name}")
    return names


def feature_value(features, name, key):
    group, feature = name.split(":", 1)
    return features.get(group, {}).get(feature, {}).get(key, 0)


def colors_from_features(P, features, names):
    raw = {
        key: tuple(feature_value(features, name, key) for name in names)
        for key in P
    }
    return compress(raw)


def compress(raw):
    palette = {value: idx for idx, value in enumerate(sorted(set(raw.values())))}
    return {key: palette[value] for key, value in raw.items()}


def atoms_from_colors(colors):
    atoms = defaultdict(list)
    for key, color in colors.items():
        atoms[color].append(key)
    return atoms


def hbar_conflicts(P, colors, H):
    atoms = atoms_from_colors(colors)
    bad = 0
    conflicts = 0
    unresolved_mass = Fraction(0)
    bad_mass = Fraction(0)
    for keys in atoms.values():
        if len(keys) > 1:
            unresolved_mass += sum(P[key] for key in keys)
        buckets = defaultdict(list)
        for key in keys:
            buckets[H[key]].append(key)
        if len(buckets) <= 1:
            continue
        bad += 1
        bad_mass += sum(P[key] for key in keys)
        for idx, left in enumerate(keys):
            for right in keys[idx + 1 :]:
                if H[left] != H[right]:
                    conflicts += 1
    return {
        "atoms": len(atoms),
        "bad": bad,
        "conflicts": conflicts,
        "bad_mass": bad_mass,
        "unresolved_mass": unresolved_mass,
    }


def record_delete_deck(bits, n):
    deck = defaultdict(int)
    vertices = tuple(range(n))
    for deleted in vertices:
        subset = tuple(v for v in vertices if v != deleted)
        child_bits = restrict_bits(bits, n, subset)
        child_key = canon_bits(child_bits, n - 1)
        deck[child_key] += 1
    return dict(deck)


def build_record_decks(reps_by_n):
    decks = {}
    reverse = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for n, reps in reps_by_n.items():
        if n <= min(reps_by_n):
            continue
        decks[n] = {}
        for key, bits in reps.items():
            deck = record_delete_deck(bits, n)
            decks[n][key] = deck
            for child_key, count in deck.items():
                reverse[n - 1][child_key][key] += count
    reverse_out = {
        n: {
            child_key: dict(parent_rows)
            for child_key, parent_rows in rows.items()
        }
        for n, rows in reverse.items()
    }
    return decks, reverse_out


def profile_to_child_colors(deck, child_colors):
    row = defaultdict(int)
    for child_key, count in deck.items():
        row[child_colors[child_key]] += count
    return tuple(sorted(row.items()))


def profile_to_parent_colors(row, parent_colors):
    out = defaultdict(int)
    for parent_key, count in row.items():
        out[parent_colors[parent_key]] += count
    return tuple(sorted(out.items()))


def refine_deletion(colors_by_n, decks, n_min, n_max):
    raw_by_n = {}
    for n, colors in colors_by_n.items():
        raw = {}
        for key, color in colors.items():
            if n == n_min:
                raw[key] = (color,)
            else:
                raw[key] = (
                    color,
                    profile_to_child_colors(decks[n][key], colors_by_n[n - 1]),
                )
        raw_by_n[n] = raw
    return {n: compress(raw_by_n[n]) for n in raw_by_n}


def refine_bidirectional(colors_by_n, decks, reverse, n_min, n_max):
    raw_by_n = {}
    for n, colors in colors_by_n.items():
        raw = {}
        for key, color in colors.items():
            child_profile = ()
            parent_profile = ()
            if n > n_min:
                child_profile = profile_to_child_colors(decks[n][key], colors_by_n[n - 1])
            if n < n_max:
                parent_profile = profile_to_parent_colors(reverse[n].get(key, {}), colors_by_n[n + 1])
            raw[key] = (color, child_profile, parent_profile)
        raw_by_n[n] = raw
    return {n: compress(raw_by_n[n]) for n in raw_by_n}


def deletion_transfer_conflicts(colors_by_n, decks, n_min):
    out = {}
    for n, colors in colors_by_n.items():
        if n == n_min:
            continue
        atoms = atoms_from_colors(colors)
        bad = 0
        conflicts = 0
        for keys in atoms.values():
            buckets = defaultdict(list)
            for key in keys:
                sig = profile_to_child_colors(decks[n][key], colors_by_n[n - 1])
                buckets[sig].append(key)
            if len(buckets) > 1:
                bad += 1
                conflicts += sum(len(v) for v in buckets.values())
        out[n] = (bad, conflicts)
    return out


def insertion_transfer_conflicts(colors_by_n, reverse, n_max):
    out = {}
    for n, colors in colors_by_n.items():
        if n == n_max:
            continue
        atoms = atoms_from_colors(colors)
        bad = 0
        conflicts = 0
        for keys in atoms.values():
            buckets = defaultdict(list)
            for key in keys:
                sig = profile_to_parent_colors(reverse[n].get(key, {}), colors_by_n[n + 1])
                buckets[sig].append(key)
            if len(buckets) > 1:
                bad += 1
                conflicts += sum(len(v) for v in buckets.values())
        out[n] = (bad, conflicts)
    return out


def refine_delete_only(colors_by_n, decks, n_min, n_max):
    raw_by_n = {}
    for n, colors in colors_by_n.items():
        raw = {}
        for key, color in colors.items():
            child_profile = ()
            if n > n_min:
                child_profile = profile_to_child_colors(decks[n][key], colors_by_n[n - 1])
            raw[key] = (color, child_profile)
        raw_by_n[n] = raw
    return {n: compress(raw_by_n[n]) for n in raw_by_n}


def known_feature_names(features):
    return feature_names(features, ["scalar", "interval", "regularity", "matching"])


def n7_cover_feature_names(features):
    names = known_feature_names(features)
    names += [
        "flags3:flag3_36",
        "flags4:flag4_2062",
        "flags4:flag4_192",
        "flags5:flag5_525184",
    ]
    return names


def n8_cover_feature_names(features):
    names = known_feature_names(features)
    names += [
        "flags3:flag3_36",
        "flags5:flag5_549376",
        "flags4:flag4_2176",
        "flags4:flag4_206",
        "flags5:flag5_24576",
    ]
    return names


def union_feature_names(features):
    names = known_feature_names(features)
    names += [
        "flags3:flag3_36",
        "flags4:flag4_2062",
        "flags4:flag4_192",
        "flags5:flag5_525184",
        "flags5:flag5_549376",
        "flags4:flag4_2176",
        "flags4:flag4_206",
        "flags5:flag5_24576",
    ]
    return names


def valid_names(features, names):
    out = []
    for name in names:
        group, feature = name.split(":", 1)
        if group in features and feature in features[group]:
            out.append(name)
    return out


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
        for k in [3, 4, 5]:
            counts = flag_counts(bits, n, k)
            flag_by_record[key][k] = counts
            flag_keys[k].update(counts)

    for k in [3, 4, 5]:
        bucket = features[f"flags{k}"]
        for flag_key in sorted(flag_keys[k]):
            name = f"flag{k}_{flag_key}"
            for record_key in P:
                bucket[name][record_key] = flag_by_record[record_key][k].get(flag_key, 0)
    return features


CONTEXT_CACHE = {}


def build_context(n_min=5, n_max=8):
    cache_key = (n_min, n_max)
    if cache_key in CONTEXT_CACHE:
        return CONTEXT_CACHE[cache_key]
    records = {}
    reps_by_n = {}
    H_by_n = {}
    for n in range(n_min, n_max + 1):
        P, counts, reps, fibers = build_score_data(n)
        records[n] = P
        reps_by_n[n] = reps
        H_by_n[n] = boundary_histograms(n, counts, fibers)
    decks, reverse = build_record_decks(reps_by_n)
    features_by_n = {n: light_feature_maps(records[n], reps_by_n[n], n) for n in records}
    context = {
        "records": records,
        "reps": reps_by_n,
        "H": H_by_n,
        "decks": decks,
        "reverse": reverse,
        "features": features_by_n,
        "n_min": n_min,
        "n_max": n_max,
    }
    CONTEXT_CACHE[cache_key] = context
    return context


def run_campaign(base_label, base_color_builder, context, rounds=8, mode="bidirectional"):
    print("\n" + "=" * 80)
    print(f"Filtration campaign: {base_label} [{mode}]")
    print("=" * 80)

    records = context["records"]
    H_by_n = context["H"]
    decks = context["decks"]
    reverse = context["reverse"]
    features_by_n = context["features"]
    n_min = context["n_min"]
    n_max = context["n_max"]
    colors = {
        n: base_color_builder(records[n], features_by_n[n], n)
        for n in records
    }

    reports = []
    for t in range(rounds + 1):
        row = {"round": t}
        for n in [7, 8]:
            row[n] = hbar_conflicts(records[n], colors[n], H_by_n[n])
        d_conf = deletion_transfer_conflicts(colors, decks, n_min)
        i_conf = insertion_transfer_conflicts(colors, reverse, n_max)
        row["delete_conflicts"] = d_conf
        row["insert_conflicts"] = i_conf
        reports.append(row)
        print(
            f"round={t:<2} "
            f"N7 atoms={row[7]['atoms']:>5}/{len(records[7]):<5} "
            f"Hconf={row[7]['conflicts']:>6} "
            f"unres={fmt_frac(row[7]['unresolved_mass'], 18):>20} | "
            f"N8 atoms={row[8]['atoms']:>6}/{len(records[8]):<6} "
            f"Hconf={row[8]['conflicts']:>7} "
            f"unres={fmt_frac(row[8]['unresolved_mass'], 18):>20} | "
            f"D8={d_conf.get(8, (0, 0))[1]:>6} "
            f"I7={i_conf.get(7, (0, 0))[1]:>6}"
        )
        if t < rounds:
            if mode == "none":
                pass
            elif mode == "delete":
                colors = refine_delete_only(colors, decks, n_min, n_max)
            elif mode == "bidirectional":
                colors = refine_bidirectional(colors, decks, reverse, n_min, n_max)
            else:
                raise ValueError(f"unknown refinement mode: {mode}")
    return {
        "records": records,
        "reps": context["reps"],
        "H": H_by_n,
        "decks": decks,
        "reverse": reverse,
        "features": features_by_n,
        "reports": reports,
        "final_colors": colors,
    }


def base_known(P, features, n):
    return colors_from_features(P, features, known_feature_names(features))


def base_n7_cover(P, features, n):
    names = valid_names(features, n7_cover_feature_names(features))
    return colors_from_features(P, features, names)


def base_n8_cover(P, features, n):
    names = valid_names(features, n8_cover_feature_names(features))
    return colors_from_features(P, features, names)


def base_hbar_union(P, features, n):
    names = valid_names(features, union_feature_names(features))
    return colors_from_features(P, features, names)


print("=" * 80)
print("Paper 30 record-intrinsic boundary filtration campaign")
print("=" * 80)
print(PRECISION_LINE)

context = build_context()
known = run_campaign(
    "known sectors + bidirectional record deletion/insertion refinement",
    base_known,
    context,
    rounds=4,
    mode="bidirectional",
)
n7_static = run_campaign("N7 Hbar-cover flags as fixed family", base_n7_cover, context, rounds=0, mode="none")
n8_static = run_campaign("N8 Hbar-cover flags as fixed family", base_n8_cover, context, rounds=0, mode="none")
n8_delete = run_campaign(
    "N8 Hbar-cover flags + deletion-only boundary refinement",
    base_n8_cover,
    context,
    rounds=2,
    mode="delete",
)
union_static = run_campaign("N7+N8 cover union as fixed family", base_hbar_union, context, rounds=0, mode="none")
union_bidir = run_campaign(
    "N7+N8 cover union + one bidirectional refinement",
    base_hbar_union,
    context,
    rounds=1,
    mode="bidirectional",
)

known_final = known["reports"][-1]
n8_static_final = n8_static["reports"][-1]
n8_delete_final = n8_delete["reports"][-1]
union_static_final = union_static["reports"][-1]
union_bidir_final = union_bidir["reports"][-1]

check(
    "known-sector bidirectional refinement improves but does not solve N=7",
    0 < known_final[7]["conflicts"] < known["reports"][0][7]["conflicts"],
    f"{known['reports'][0][7]['conflicts']} -> {known_final[7]['conflicts']}",
)
check(
    "known-sector bidirectional refinement improves but does not solve N=8",
    0 < known_final[8]["conflicts"] < known["reports"][0][8]["conflicts"],
    f"{known['reports'][0][8]['conflicts']} -> {known_final[8]['conflicts']}",
)
check(
    "fixed N8 cover family makes Hbar measurable at N=7 and N=8",
    n8_static_final[7]["conflicts"] == 0 and n8_static_final[8]["conflicts"] == 0,
    f"N7={n8_static_final[7]['conflicts']} N8={n8_static_final[8]['conflicts']}",
)
check(
    "fixed N8 cover family is non-lookup at N=7 and N=8",
    n8_static_final[7]["atoms"] < len(n8_static["records"][7])
    and n8_static_final[8]["atoms"] < len(n8_static["records"][8]),
    (
        f"N7={n8_static_final[7]['atoms']}/{len(n8_static['records'][7])} "
        f"N8={n8_static_final[8]['atoms']}/{len(n8_static['records'][8])}"
    ),
)
check(
    "fixed N8 cover family has controlled drift relative to known baseline",
    n8_static_final["delete_conflicts"].get(8, (0, 0))[1]
    < known["reports"][0]["delete_conflicts"].get(8, (0, 0))[1]
    and n8_static_final["insert_conflicts"].get(7, (0, 0))[1]
    < known["reports"][0]["insert_conflicts"].get(7, (0, 0))[1],
    (
        f"D8 {known['reports'][0]['delete_conflicts'].get(8, (0, 0))[1]} -> "
        f"{n8_static_final['delete_conflicts'].get(8, (0, 0))[1]}, "
        f"I7 {known['reports'][0]['insert_conflicts'].get(7, (0, 0))[1]} -> "
        f"{n8_static_final['insert_conflicts'].get(7, (0, 0))[1]}"
    ),
)
check(
    "deletion-only closure of fixed N8 cover becomes lookup and is rejected",
    n8_delete["reports"][0][8]["atoms"] < len(n8_delete["records"][8])
    and n8_delete_final[8]["atoms"] == len(n8_delete["records"][8]),
    (
        f"N8 static={n8_delete['reports'][0][8]['atoms']}; "
        f"after delete={n8_delete_final[8]['atoms']}/{len(n8_delete['records'][8])}"
    ),
)
check(
    "naive bidirectional closure of cover union becomes lookup and is rejected",
    union_static_final[8]["atoms"] < len(union_static["records"][8])
    and union_bidir_final[8]["atoms"] == len(union_bidir["records"][8]),
    (
        f"union static N8={union_static_final[8]['atoms']}; "
        f"after bidir={union_bidir_final[8]['atoms']}/{len(union_bidir['records'][8])}"
    ),
)

print("\n=== Campaign status ===")
print(
    "Pure known-sector deletion/insertion refinement is record-intrinsic and "
    "stabilizes transfer, but it does not make Hbar measurable.  A fixed "
    "N=8 local Hbar-cover family is a stronger non-lookup finite witness: it "
    "makes Hbar measurable at both audited levels and has small finite drift.  "
    "Deletion-only and full bidirectional closure both remove drift by collapsing "
    "to record lookup in the audited window.  The admissible theorem must "
    "therefore control drift without closing under all refinements."
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
