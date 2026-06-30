#!/usr/bin/env python3
"""
Paper 30 receipt: why the lopsided hinge works.

Campaign F found that adding flags5:flag5_912 to the fixed N=8 one-hole
boundary cover repairs every audited k=1..4 multi-hole boundary histogram at
N=8 while remaining non-lookup.  This receipt asks the next hostile question:

    is the repair a magic finite id, a coarser shape count, or a genuine
    boundary-charge mechanism?

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


def record_delete_deck(bits, n, k):
    deck = defaultdict(int)
    vertices = tuple(range(n))
    for deleted in combinations(vertices, k):
        deleted_set = set(deleted)
        subset = tuple(v for v in vertices if v not in deleted_set)
        child_bits = restrict_bits(bits, n, subset)
        child_key = canon_bits(child_bits, n - k)
        deck[child_key] += 1
    return dict(deck)


def build_decks(reps_by_n, ks):
    decks = {k: {} for k in ks}
    reverse = {k: defaultdict(lambda: defaultdict(lambda: defaultdict(int))) for k in ks}
    for k in ks:
        for n, reps in reps_by_n.items():
            if n - k not in reps_by_n:
                continue
            decks[k][n] = {}
            for key, bits in reps.items():
                deck = record_delete_deck(bits, n, k)
                decks[k][n][key] = deck
                for child_key, count in deck.items():
                    reverse[k][n - k][child_key][key] += count
    reverse_out = {
        k: {
            n: {child_key: dict(parent_rows) for child_key, parent_rows in rows.items()}
            for n, rows in reverse[k].items()
        }
        for k in ks
    }
    return decks, reverse_out


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


def colors_from_features(P, features, names, extras=None):
    extras = extras or []
    return compress({
        key: (
            tuple(feature_value(features, name, key) for name in names),
            tuple(mapping[key] for mapping in extras),
        )
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
    for atom, keys in atoms.items():
        for idx, left in enumerate(keys):
            for right in keys[idx + 1 :]:
                if invariant[left] != invariant[right]:
                    conflicts.append((atom, left, right))
    return conflicts


def conflict_count(colors, invariant):
    return len(conflict_pairs(colors, invariant)), len(atoms_from_colors(colors))


def all_hists_agree(keys, hist_by_k):
    for left in keys:
        for right in keys:
            if any(hist_by_k[k][left] != hist_by_k[k][right] for k in hist_by_k):
                return False
    return True


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


def transfer_conflicts(colors_parent, colors_child, deck_rows, reverse_rows):
    parent_atoms = atoms_from_colors(colors_parent)
    child_atoms = atoms_from_colors(colors_child)
    delete_bad = 0
    delete_conflicts = 0
    for keys in parent_atoms.values():
        buckets = defaultdict(list)
        for key in keys:
            buckets[profile_to_child_colors(deck_rows[key], colors_child)].append(key)
        if len(buckets) > 1:
            delete_bad += 1
            delete_conflicts += sum(len(v) for v in buckets.values())

    insert_bad = 0
    insert_conflicts = 0
    for keys in child_atoms.values():
        buckets = defaultdict(list)
        for key in keys:
            buckets[profile_to_parent_colors(reverse_rows.get(key, {}), colors_parent)].append(key)
        if len(buckets) > 1:
            insert_bad += 1
            insert_conflicts += sum(len(v) for v in buckets.values())
    return {
        "delete_bad": delete_bad,
        "delete_conflicts": delete_conflicts,
        "insert_bad": insert_bad,
        "insert_conflicts": insert_conflicts,
    }


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


def all_five_record_keys():
    return sorted({
        canon_bits(permutation_order_bits(pi), 5)
        for pi in perms(5)
    })


def mapping_from_flags(features, n, flag_keys, signed=None):
    signed = signed or {}
    out = {}
    for key in next(iter(features["flags5"].values())):
        total = 0
        for flag_key in flag_keys:
            total += features["flags5"].get(f"flag5_{flag_key}", {}).get(key, 0)
        for flag_key, coefficient in signed.items():
            total += coefficient * features["flags5"].get(f"flag5_{flag_key}", {}).get(key, 0)
        out[key] = total
    return out


def mapping_from_expression(P, features, terms):
    out = {}
    for key in P:
        total = 0
        for coefficient, group, feature in terms:
            total += coefficient * features[group].get(feature, {}).get(key, 0)
        out[key] = total
    return out


def print_color_report(label, P, colors, hist_by_k):
    atoms = atoms_from_colors(colors)
    nontriv = [keys for keys in atoms.values() if len(keys) > 1]
    max_atom = max(len(keys) for keys in atoms.values())
    conflict_counts = {k: conflict_count(colors, hist_by_k[k])[0] for k in hist_by_k}
    print(
        f"{label:<28} atoms={len(atoms):>6}/{len(P):<6} "
        f"nontriv_atoms={len(nontriv):>4} max_atom={max_atom:<2} "
        + " ".join(f"k{k}={conflict_counts[k]:>3}" for k in sorted(hist_by_k))
    )
    return {
        "atoms": len(atoms),
        "nontriv_atoms": len(nontriv),
        "max_atom": max_atom,
        "conflicts": conflict_counts,
    }


def same_partition(colors_left, colors_right):
    keys = sorted(colors_left)
    return all(
        (colors_left[a] == colors_left[b]) == (colors_right[a] == colors_right[b])
        for idx, a in enumerate(keys)
        for b in keys[idx + 1 :]
    )


def fraction_label(frac):
    if frac.denominator == 1:
        return str(frac.numerator)
    return f"{frac.numerator}/{frac.denominator}"


def charge_prediction(a, b, forbidden_slopes, has_partner_blind_pair):
    if a == 0:
        return not has_partner_blind_pair
    return Fraction(b, a) not in forbidden_slopes


print("=" * 80)
print("Paper 30 lopsided-hinge mechanism campaign")
print("=" * 80)
print(PRECISION_LINE)

ks = [1, 2, 3, 4]
records = {}
counts_by_n = {}
reps_by_n = {}
fibers_by_n = {}
features_by_n = {}
hist_by_n_k = {7: {}, 8: {}}

for n in [3, 4, 5, 6, 7, 8]:
    P, counts, reps, fibers = build_score_data(n)
    records[n] = P
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    fibers_by_n[n] = fibers
    features_by_n[n] = light_feature_maps(P, reps, n)
    if n in [7, 8]:
        for k in ks:
            hist_by_n_k[n][k] = multihole_histograms(n, k, counts, fibers)

decks, reverse = build_decks(reps_by_n, ks)

all_flag5 = all_five_record_keys()
full_hinge_keys = [key for key in all_flag5 if descriptor(key) == descriptor(912)]
coarse_hinge_keys = [key for key in all_flag5 if coarse_descriptor(key) == coarse_descriptor(912)]
print("\n" + "=" * 80)
print("Structural hinge classes")
print("=" * 80)
print(f"full lopsided-hinge descriptor keys={full_hinge_keys}")
print(f"coarse height-2 hinge descriptor keys={coarse_hinge_keys}")
for key in coarse_hinge_keys:
    print(
        f"  flag5_{key:<5} relations={relations(key)} profiles={vertex_profiles(key)}"
    )

base_names = {
    n: valid_names(features_by_n[n], n8_cover_feature_names(features_by_n[n]))
    for n in [7, 8]
}

base_colors = {
    n: colors_from_features(records[n], features_by_n[n], base_names[n])
    for n in [7, 8]
}
hinge_exact = {
    n: mapping_from_flags(features_by_n[n], n, [912])
    for n in [7, 8]
}
hinge_coarse = {
    n: mapping_from_flags(features_by_n[n], n, coarse_hinge_keys)
    for n in [7, 8]
}
hinge_partner = {
    n: mapping_from_flags(features_by_n[n], n, [664])
    for n in [7, 8]
}
hinge_signed = {
    n: mapping_from_expression(
        records[n],
        features_by_n[n],
        [(1, "flags5", "flag5_912"), (-1, "flags5", "flag5_664")],
    )
    for n in [7, 8]
}

print("\n" + "=" * 80)
print("Can coarser structural hinge memories replace the exact lopsided hinge?")
print("=" * 80)
reports = {}
color_variants = {}
for n in [7, 8]:
    hist_by_k = hist_by_n_k[n]
    color_variants[(n, "base")] = base_colors[n]
    reports[(n, "base")] = print_color_report(
        f"N={n} base",
        records[n],
        base_colors[n],
        hist_by_k,
    )
    color_variants[(n, "partner")] = colors_from_features(
        records[n], features_by_n[n], base_names[n], [hinge_partner[n]]
    )
    reports[(n, "partner")] = print_color_report(
        f"N={n} base+flag664",
        records[n],
        color_variants[(n, "partner")],
        hist_by_k,
    )
    color_variants[(n, "coarse")] = colors_from_features(
        records[n], features_by_n[n], base_names[n], [hinge_coarse[n]]
    )
    reports[(n, "coarse")] = print_color_report(
        f"N={n} base+coarse-sum",
        records[n],
        color_variants[(n, "coarse")],
        hist_by_k,
    )
    color_variants[(n, "signed")] = colors_from_features(
        records[n], features_by_n[n], base_names[n], [hinge_signed[n]]
    )
    reports[(n, "signed")] = print_color_report(
        f"N={n} base+signed",
        records[n],
        color_variants[(n, "signed")],
        hist_by_k,
    )
    color_variants[(n, "exact")] = colors_from_features(
        records[n], features_by_n[n], base_names[n], [hinge_exact[n]]
    )
    reports[(n, "exact")] = print_color_report(
        f"N={n} base+flag912",
        records[n],
        color_variants[(n, "exact")],
        hist_by_k,
    )

print("\npartition comparison at N=8:")
for left, right in [("exact", "coarse"), ("exact", "signed"), ("coarse", "signed")]:
    print(
        f"  {left} vs {right}: "
        f"{'same partition' if same_partition(color_variants[(8, left)], color_variants[(8, right)]) else 'different partitions'}"
    )

print("\n" + "=" * 80)
print("Conflict-pair charge carried by flag5_912")
print("=" * 80)
charge_rows = {}
all_charge_vectors = []
for k in [2, 3, 4]:
    pairs = conflict_pairs(base_colors[8], hist_by_n_k[8][k])
    diff_hist = defaultdict(int)
    coarse_diff_hist = defaultdict(int)
    partner_diff_hist = defaultdict(int)
    signed_diff_hist = defaultdict(int)
    examples = []
    for atom, left, right in pairs:
        diff = hinge_exact[8][left] - hinge_exact[8][right]
        coarse_diff = hinge_coarse[8][left] - hinge_coarse[8][right]
        partner_diff = hinge_partner[8][left] - hinge_partner[8][right]
        signed_diff = hinge_signed[8][left] - hinge_signed[8][right]
        all_charge_vectors.append((diff, partner_diff))
        diff_hist[diff] += 1
        coarse_diff_hist[coarse_diff] += 1
        partner_diff_hist[partner_diff] += 1
        signed_diff_hist[signed_diff] += 1
        if len(examples) < 3:
            examples.append((left, right, diff, coarse_diff, partner_diff, signed_diff))
    charge_rows[k] = {
        "pairs": len(pairs),
        "diff_hist": dict(sorted(diff_hist.items())),
        "coarse_diff_hist": dict(sorted(coarse_diff_hist.items())),
        "partner_diff_hist": dict(sorted(partner_diff_hist.items())),
        "signed_diff_hist": dict(sorted(signed_diff_hist.items())),
        "examples": examples,
    }
    print(f"k={k} pairs={len(pairs)}")
    print(f"  flag912 diff histogram  = {charge_rows[k]['diff_hist']}")
    print(f"  coarse diff histogram   = {charge_rows[k]['coarse_diff_hist']}")
    print(f"  flag664 diff histogram  = {charge_rows[k]['partner_diff_hist']}")
    print(f"  signed diff histogram   = {charge_rows[k]['signed_diff_hist']}")
    for left, right, diff, coarse_diff, partner_diff, signed_diff in examples:
        print(
            "  example "
            f"{left}->{right}: 912={diff} coarse={coarse_diff} "
            f"664={partner_diff} signed={signed_diff}"
        )

unique_vectors = sorted(set(all_charge_vectors))
forbidden_slopes = sorted({
    Fraction(-d912, d664)
    for d912, d664 in unique_vectors
    if d664 != 0
})
has_partner_blind_pair = any(d664 == 0 and d912 != 0 for d912, d664 in unique_vectors)
print("\nlinear hinge-sector charge criterion:")
print(f"  unique (delta flag912, delta flag664) vectors = {unique_vectors}")
print(
    "  for a charge a*flag912 + b*flag664, avoid "
    f"a=0 when partner-blind pairs exist ({has_partner_blind_pair}), and avoid "
    "b/a in {" + ", ".join(fraction_label(x) for x in forbidden_slopes) + "}"
)
print("  exact flag912 uses (a,b)=(1,0)")
print("  coarse sum uses (a,b)=(1,1)")
print("  signed difference uses (a,b)=(1,-1)")
print("  partner flag664 uses (a,b)=(0,1), which fails")

print("\n" + "=" * 80)
print("Small integer charge scan")
print("=" * 80)
small_charge_rows = []
prediction_mismatches = []
charge_only_report = {}
for a in range(-4, 5):
    for b in range(-4, 5):
        if a == 0 and b == 0:
            continue
        charge = mapping_from_expression(
            records[8],
            features_by_n[8],
            [(a, "flags5", "flag5_912"), (b, "flags5", "flag5_664")],
        )
        colors = colors_from_features(records[8], features_by_n[8], base_names[8], [charge])
        conflicts = {k: conflict_count(colors, hist_by_n_k[8][k])[0] for k in ks}
        atoms = conflict_count(colors, hist_by_n_k[8][1])[1]
        actual = all(value == 0 for value in conflicts.values())
        predicted = charge_prediction(a, b, forbidden_slopes, has_partner_blind_pair)
        if actual != predicted:
            prediction_mismatches.append((a, b, predicted, actual, conflicts))
        if actual:
            small_charge_rows.append((a, b, atoms, conflicts))

for a, b, atoms, conflicts in small_charge_rows[:20]:
    print(
        f"  works (a,b)=({a:>2},{b:>2}) atoms={atoms}/{len(records[8])} "
        + " ".join(f"k{k}={conflicts[k]}" for k in ks)
    )
print(f"  working small charges={len(small_charge_rows)}/80")
print(f"  prediction mismatches={prediction_mismatches}")

for label, charge in [
    ("flag912 only", hinge_exact[8]),
    ("coarse sector only", hinge_coarse[8]),
    ("signed sector only", hinge_signed[8]),
]:
    colors = colors_from_features(records[8], features_by_n[8], [], [charge])
    charge_only_report[label] = {
        "atoms": conflict_count(colors, hist_by_n_k[8][1])[1],
        "conflicts": {k: conflict_count(colors, hist_by_n_k[8][k])[0] for k in ks},
    }
    print(
        f"  {label:<20} atoms={charge_only_report[label]['atoms']:>4}/{len(records[8])} "
        + " ".join(f"k{k}={charge_only_report[label]['conflicts'][k]:>7}" for k in ks)
    )

print("\n" + "=" * 80)
print("Does flag5_912 merely reconstruct records?")
print("=" * 80)
augmented_colors = {
    n: colors_from_features(records[n], features_by_n[n], base_names[n], [hinge_exact[n]])
    for n in [7, 8]
}
atoms8 = atoms_from_colors(augmented_colors[8])
nontriv8 = [keys for keys in atoms8.values() if len(keys) > 1]
print(f"N=8 nontrivial augmented atoms={len(nontriv8)}")
for idx, keys in enumerate(sorted(nontriv8, key=lambda row: (-len(row), row))[:8], 1):
    masses = [counts_by_n[8][key] for key in keys]
    print(
        f"  atom {idx}: size={len(keys)} total_perm_mass={sum(masses)}/40320 "
        f"all_k_hist_agree={all_hists_agree(keys, hist_by_n_k[8])}"
    )
    for key in keys[:4]:
        bits = reps_by_n[8][key]
        print(
            f"    key={key} rel={relation_count(bits,8)} h={height(bits,8)} "
            f"w={width(bits,8)} intervals={interval_counts(bits,8)[:6]} "
            f"flag912={hinge_exact[8][key]}"
        )

print("\n" + "=" * 80)
print("Backward-forward transfer drift after adding flag5_912")
print("=" * 80)
transfer_rows = {}
for k in ks:
    child_n = 8 - k
    if child_n not in records:
        continue
    parent_colors = augmented_colors[8]
    child_colors = colors_from_features(
        records[child_n],
        features_by_n[child_n],
        valid_names(features_by_n[child_n], n8_cover_feature_names(features_by_n[child_n])),
        [
            mapping_from_flags(features_by_n[child_n], child_n, [912])
            if child_n >= 5
            else {key: 0 for key in records[child_n]}
        ],
    )
    row = transfer_conflicts(
        parent_colors,
        child_colors,
        decks[k][8],
        reverse[k][child_n],
    )
    transfer_rows[k] = row
    print(
        f"k={k} N=8->{child_n} "
        f"delete={row['delete_conflicts']} insert={row['insert_conflicts']} "
        f"bad_atoms={row['delete_bad']}/{row['insert_bad']}"
    )

print("\n" + "=" * 80)
print("Hostile review")
print("=" * 80)
print(
    "1. The first hostile guess was wrong in a useful way: exact flag5_912 is "
    "not the only working structural memory.  The coarse two-flag hinge-sector "
    "sum and the signed hinge-sector difference also repair the audited N=8 "
    "residue."
)
print(
    "2. The real object is therefore a hinge-sector charge, not a magic flag "
    "id.  The partner component flag5_664 alone is blind to one conflict pair, "
    "but any tested non-degenerate charge with a flag5_912 component avoids the "
    "blind direction."
)
print(
    "3. The witness is conditional: hinge-sector charges repair the multi-hole "
    "residue only after the fixed N=8 one-hole boundary cover has already "
    "removed the large boundary ambiguity."
)
print(
    "4. It is not a full lookup at N=8: residual nontrivial atoms remain, and "
    "they agree on every audited k=1..4 boundary histogram.  That is exactly "
    "the non-reconstructive behavior wanted from an admissible record law."
)
print(
    "5. It becomes lookup at N=7, so the theorem cannot demand one finite "
    "operator budget that is uniformly non-lookup at every small N.  The law "
    "needs an asymptotic or scale-dependent non-reconstruction envelope."
)

check(
    "full structural hinge descriptor is unique",
    full_hinge_keys == [912],
    f"full={full_hinge_keys}",
)
check(
    "coarse hinge descriptor is too broad",
    set(coarse_hinge_keys) == {664, 912},
    f"coarse={coarse_hinge_keys}",
)
check(
    "exact lopsided hinge repairs all audited N=8 multi-hole conflicts",
    all(reports[(8, "exact")]["conflicts"][k] == 0 for k in ks),
    str(reports[(8, "exact")]["conflicts"]),
)
check(
    "coarse hinge-sector sum also repairs all audited N=8 conflicts",
    all(reports[(8, "coarse")]["conflicts"][k] == 0 for k in ks),
    str(reports[(8, "coarse")]["conflicts"]),
)
check(
    "signed hinge-sector charge also repairs all audited N=8 conflicts",
    all(reports[(8, "signed")]["conflicts"][k] == 0 for k in ks),
    str(reports[(8, "signed")]["conflicts"]),
)
check(
    "partner hinge flag664 alone does not replace flag912",
    any(reports[(8, "partner")]["conflicts"][k] > 0 for k in ks),
    str(reports[(8, "partner")]["conflicts"]),
)
check(
    "flag912 carries nonzero charge on every base N=8 k=2..4 conflict pair",
    all(0 not in charge_rows[k]["diff_hist"] for k in [2, 3, 4]),
    ", ".join(f"k{k}={charge_rows[k]['diff_hist']}" for k in [2, 3, 4]),
)
check(
    "the hinge-sector has a finite forbidden-slope separation rule",
    has_partner_blind_pair and Fraction(0, 1) not in forbidden_slopes and Fraction(1, 1) not in forbidden_slopes,
    "forbidden={" + ", ".join(fraction_label(x) for x in forbidden_slopes) + "}",
)
check(
    "forbidden-slope rule predicts all small integer charges in [-4,4]^2",
    not prediction_mismatches,
    f"working={len(small_charge_rows)} mismatches={prediction_mismatches}",
)
check(
    "hinge-sector charge is conditional and does not solve boundary memory alone",
    all(
        any(row["conflicts"][k] > 0 for k in ks)
        for row in charge_only_report.values()
    ),
    str(charge_only_report),
)
check(
    "flag912 is non-reconstructive at N=8",
    reports[(8, "exact")]["atoms"] < len(records[8]) and len(nontriv8) > 0,
    f"atoms={reports[(8, 'exact')]['atoms']}/{len(records[8])} nontriv={len(nontriv8)}",
)
check(
    "remaining N=8 nontrivial atoms agree on all audited multi-hole histograms",
    all(all_hists_agree(keys, hist_by_n_k[8]) for keys in nontriv8),
    f"nontriv_atoms={len(nontriv8)}",
)

print("\n=== Campaign status ===")
print(
    "The hinge result sharpened during the campaign.  The exact lopsided "
    "height-2 hinge is not the only working memory; the broader two-component "
    "hinge sector works through a finite separation rule on conflict-pair "
    "charge vectors.  The failed direction is the partner-only component, "
    "which is blind to one audited conflict.  The theorem target should "
    "therefore be a boundary-charge law over a small hinge sector, not a rule "
    "hard-coded to one flag id."
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
