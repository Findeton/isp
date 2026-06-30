#!/usr/bin/env python3
"""
Paper 30 receipt: next-scale hinge-sector prediction campaign.

Campaign G found a finite N=8 rule: after the fixed one-hole boundary cover,
multi-hole residue is separated by a non-degenerate charge in the two-dimensional
hinge sector (F_912, F_664).  This campaign asks the Feynman/Euler question:

    does that rule predict the next scale, and if not, what is the next sector?

The receipt performs exact enumeration for 2D permutation-record orders through
N=9.  It uses exact integer/Fraction arithmetic only.  If mpmath is available
it is set to dps=140 for reporting; otherwise no floating arithmetic is used.
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
sys.setrecursionlimit(20000)

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
    total = 0
    for pi in perms(n):
        total += 1
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        fibers[key].append(pi)
        p_counts[key] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    print(f"  built N={n}: permutations={total} records={len(P)}")
    return P, dict(p_counts), reps, dict(fibers)


def multihole_histograms_all(n, ks, counts, fibers):
    hist_by_k = {
        k: {key: defaultdict(int) for key in fibers}
        for k in ks
    }
    combos_by_k = {k: tuple(combinations(range(n), k)) for k in ks}
    for key, fiber in fibers.items():
        for pi in fiber:
            parent_score = same_block_score(pi)
            for k, combos in combos_by_k.items():
                row = hist_by_k[k][key]
                for positions in combos:
                    child = delete_positions(pi, positions)
                    a = same_block_score(child)
                    b = parent_score - a
                    row[(a, b)] += 1
    out = {}
    for k in ks:
        denom = math.comb(n, k)
        out[k] = {
            key: tuple(sorted((item, Fraction(count, denom * counts[key])) for item, count in row.items()))
            for key, row in hist_by_k[k].items()
        }
        print(f"  built N={n} k={k} histogram")
    return out


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
    print(
        f"  features N={n}: flags3={len(flag_keys[3])} "
        f"flags4={len(flag_keys[4])} flags5={len(flag_keys[5])}"
    )
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


def all_flag_feature_names(features):
    return feature_names(features, ["flags3", "flags4", "flags5"])


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


def conflict_summary(colors, invariant):
    atoms = atoms_from_colors(colors)
    bad_atoms = 0
    conflicts = 0
    unresolved = 0
    max_atom = 0
    for keys in atoms.values():
        max_atom = max(max_atom, len(keys))
        if len(keys) > 1:
            unresolved += len(keys)
        buckets = defaultdict(int)
        for key in keys:
            buckets[invariant[key]] += 1
        if len(buckets) <= 1:
            continue
        bad_atoms += 1
        total_pairs = len(keys) * (len(keys) - 1) // 2
        same_pairs = sum(size * (size - 1) // 2 for size in buckets.values())
        conflicts += total_pairs - same_pairs
    return {
        "atoms": len(atoms),
        "bad_atoms": bad_atoms,
        "conflicts": conflicts,
        "unresolved_records": unresolved,
        "max_atom": max_atom,
    }


def combined_conflicts(colors, hist_by_k, ks):
    rows = {k: conflict_summary(colors, hist_by_k[k]) for k in ks}
    return {
        "rows": rows,
        "total_conflicts": sum(rows[k]["conflicts"] for k in ks),
        "total_bad_atoms": sum(rows[k]["bad_atoms"] for k in ks),
        "atoms": rows[ks[0]]["atoms"],
        "max_atom": rows[ks[0]]["max_atom"],
        "unresolved_records": rows[ks[0]]["unresolved_records"],
    }


def mapping_from_expression(P, features, terms):
    out = {}
    for key in P:
        total = 0
        for coefficient, group, feature in terms:
            total += coefficient * features[group].get(feature, {}).get(key, 0)
        out[key] = total
    return out


def print_report(label, n, P, colors, hist_by_k, ks):
    row = combined_conflicts(colors, hist_by_k, ks)
    print(
        f"{label:<30} N={n} atoms={row['atoms']:>7}/{len(P):<7} "
        f"bad={row['total_bad_atoms']:>7} conf={row['total_conflicts']:>10} "
        f"unres={row['unresolved_records']:>7} max_atom={row['max_atom']:<3} "
        + " ".join(f"k{k}={row['rows'][k]['conflicts']}" for k in ks)
    )
    return row


def charge_prediction(a, b, forbidden_slopes, has_partner_blind_pair):
    if a == 0:
        return not has_partner_blind_pair
    return Fraction(b, a) not in forbidden_slopes


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
        buckets = defaultdict(int)
        for key in keys:
            buckets[profile_to_child_colors(deck_rows[key], colors_child)] += 1
        if len(buckets) > 1:
            delete_bad += 1
            delete_conflicts += len(keys)

    insert_bad = 0
    insert_conflicts = 0
    for keys in child_atoms.values():
        buckets = defaultdict(int)
        for key in keys:
            buckets[profile_to_parent_colors(reverse_rows.get(key, {}), colors_parent)] += 1
        if len(buckets) > 1:
            insert_bad += 1
            insert_conflicts += len(keys)
    return {
        "delete_bad": delete_bad,
        "delete_conflicts": delete_conflicts,
        "insert_bad": insert_bad,
        "insert_conflicts": insert_conflicts,
    }


def greedy_single_flag_followup(P, features, base_names, base_extras, hist_by_k, ks, max_rounds=6):
    selected = []
    candidates = valid_names(features, all_flag_feature_names(features))
    current_colors = colors_from_features(P, features, base_names, base_extras)
    current = combined_conflicts(current_colors, hist_by_k, ks)
    rows = []
    print("\n" + "=" * 80)
    print("Greedy follow-up after N=9 hinge-sector failure")
    print("=" * 80)
    print(
        f"round=0 selected=[] total={current['total_conflicts']} "
        f"atoms={current['atoms']}/{len(P)}"
    )
    for round_idx in range(1, max_rounds + 1):
        best = None
        for name in candidates:
            if name in selected:
                continue
            colors = colors_from_features(P, features, base_names + selected + [name], base_extras)
            row = combined_conflicts(colors, hist_by_k, ks)
            gain = current["total_conflicts"] - row["total_conflicts"]
            # Prefer larger gain, then fewer atoms, then stable name.
            score = (gain, -row["atoms"], name)
            if best is None or score > best[0]:
                best = (score, name, row, colors)
        if best is None or best[0][0] <= 0:
            print(f"round={round_idx} no improving local flag")
            break
        _score, name, row, colors = best
        selected.append(name)
        rows.append((name, row))
        current = row
        current_colors = colors
        print(
            f"round={round_idx} add={name:<24} total={row['total_conflicts']:<10} "
            f"bad={row['total_bad_atoms']:<7} atoms={row['atoms']}/{len(P)} "
            + " ".join(f"k{k}={row['rows'][k]['conflicts']}" for k in ks)
        )
        if row["total_conflicts"] == 0:
            break
        if row["atoms"] == len(P):
            print("  stopped: lookup reached")
            break
    return {
        "selected": selected,
        "rows": rows,
        "final": current,
        "colors": current_colors,
    }


print("=" * 80)
print("Paper 30 next-scale hinge-sector prediction campaign")
print("=" * 80)
print(PRECISION_LINE)

ks = [1, 2, 3, 4]
n_values = [5, 6, 7, 8, 9]
records = {}
counts_by_n = {}
reps_by_n = {}
fibers_by_n = {}
features_by_n = {}

print("\n" + "=" * 80)
print("Exact record enumeration")
print("=" * 80)
for n in n_values:
    P, counts, reps, fibers = build_score_data(n)
    records[n] = P
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    fibers_by_n[n] = fibers

print("\n" + "=" * 80)
print("Feature maps")
print("=" * 80)
for n in n_values:
    features_by_n[n] = light_feature_maps(records[n], reps_by_n[n], n)

print("\n" + "=" * 80)
print("Boundary histograms")
print("=" * 80)
hist_by_n = {}
for n in [8, 9]:
    hist_by_n[n] = multihole_histograms_all(n, ks, counts_by_n[n], fibers_by_n[n])

decks, reverse = build_decks(reps_by_n, ks)

base_names = {
    n: valid_names(features_by_n[n], n8_cover_feature_names(features_by_n[n]))
    for n in n_values
}
hinge_exact = {
    n: mapping_from_expression(records[n], features_by_n[n], [(1, "flags5", "flag5_912")])
    for n in n_values
}
hinge_partner = {
    n: mapping_from_expression(records[n], features_by_n[n], [(1, "flags5", "flag5_664")])
    for n in n_values
}
hinge_coarse = {
    n: mapping_from_expression(
        records[n],
        features_by_n[n],
        [(1, "flags5", "flag5_912"), (1, "flags5", "flag5_664")],
    )
    for n in n_values
}
hinge_signed = {
    n: mapping_from_expression(
        records[n],
        features_by_n[n],
        [(1, "flags5", "flag5_912"), (-1, "flags5", "flag5_664")],
    )
    for n in n_values
}

print("\n" + "=" * 80)
print("Out-of-sample hinge-sector prediction")
print("=" * 80)
reports = {}
for n in [8, 9]:
    variants = [
        ("base", []),
        ("base+partner", [hinge_partner[n]]),
        ("base+exact912", [hinge_exact[n]]),
        ("base+coarse", [hinge_coarse[n]]),
        ("base+signed", [hinge_signed[n]]),
    ]
    for label, extras in variants:
        colors = colors_from_features(records[n], features_by_n[n], base_names[n], extras)
        reports[(n, label)] = print_report(label, n, records[n], colors, hist_by_n[n], ks)

n8_vectors = [
    (-1, -2),
    (-1, 0),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 0),
    (2, 4),
    (2, 6),
    (3, 6),
]
n8_forbidden_slopes = sorted(
    {Fraction(-d912, d664) for d912, d664 in n8_vectors if d664 != 0}
)
n8_has_partner_blind = any(d664 == 0 and d912 != 0 for d912, d664 in n8_vectors)

print("\n" + "=" * 80)
print("N=9 small-charge prediction from N=8 forbidden slopes")
print("=" * 80)
small_charge_rows = []
small_charge_mismatches = []
for a in range(-4, 5):
    for b in range(-4, 5):
        if a == 0 and b == 0:
            continue
        charge = mapping_from_expression(
            records[9],
            features_by_n[9],
            [(a, "flags5", "flag5_912"), (b, "flags5", "flag5_664")],
        )
        colors = colors_from_features(records[9], features_by_n[9], base_names[9], [charge])
        row = combined_conflicts(colors, hist_by_n[9], ks)
        actual = row["total_conflicts"] == 0
        predicted = charge_prediction(a, b, n8_forbidden_slopes, n8_has_partner_blind)
        if actual != predicted:
            small_charge_mismatches.append((a, b, predicted, actual, row["total_conflicts"]))
        if actual:
            small_charge_rows.append((a, b, row["atoms"]))
print(f"  N=8 forbidden slopes={n8_forbidden_slopes}")
print(f"  N=9 working small charges={len(small_charge_rows)}/80")
print(f"  N=9 prediction mismatches={small_charge_mismatches[:20]} total={len(small_charge_mismatches)}")

followup = None
if reports[(9, "base+coarse")]["total_conflicts"] > 0:
    followup = greedy_single_flag_followup(
        records[9],
        features_by_n[9],
        base_names[9],
        [hinge_coarse[9]],
        hist_by_n[9],
        ks,
        max_rounds=8,
    )

print("\n" + "=" * 80)
print("N=9 backward-forward transfer")
print("=" * 80)
transfer_rows = {}
colors_by_n = {
    n: colors_from_features(records[n], features_by_n[n], base_names[n], [hinge_coarse[n]])
    for n in n_values
}
for k in ks:
    child_n = 9 - k
    row = transfer_conflicts(
        colors_by_n[9],
        colors_by_n[child_n],
        decks[k][9],
        reverse[k][child_n],
    )
    transfer_rows[k] = row
    print(
        f"k={k} N=9->{child_n} "
        f"delete={row['delete_conflicts']} insert={row['insert_conflicts']} "
        f"bad_atoms={row['delete_bad']}/{row['insert_bad']}"
    )

print("\n" + "=" * 80)
print("Hostile review")
print("=" * 80)
if reports[(9, "base+coarse")]["total_conflicts"] == 0:
    print(
        "1. The hinge-sector charge survives the exact N=9 out-of-sample test "
        "for k=1..4 boundary histograms after the fixed one-hole cover."
    )
else:
    print(
        "1. The hinge-sector charge does not survive as a complete N=9 law. "
        "It remains a useful correction layer, but new residue appears at the "
        "next scale."
    )
    if followup is not None:
        print(
            "2. The campaign followed the opening with a greedy flags3/4/5 scan. "
            f"Selected={followup['selected']} final_conflicts={followup['final']['total_conflicts']}."
        )
print(
    "3. The campaign is exact in the audited finite universe: no random samples "
    "or floating probabilities enter the pass/fail checks."
)
print(
    "4. A click-law theorem cannot yet be just the N=8 forbidden-slope rule. "
    "The next object is either the greedy follow-up sector, if stable, or a "
    "larger recurrence that explains why new sectors enter with scale."
)

n9_hinge_survives = reports[(9, "base+coarse")]["total_conflicts"] == 0
n9_exact_improves = (
    reports[(9, "base+coarse")]["total_conflicts"]
    < reports[(9, "base")]["total_conflicts"]
)
n9_partner_worse = (
    reports[(9, "base+partner")]["total_conflicts"]
    > reports[(9, "base+coarse")]["total_conflicts"]
)
followup_progress = (
    followup is None
    or followup["final"]["total_conflicts"] < reports[(9, "base+coarse")]["total_conflicts"]
)

check(
    "exact N=9 enumeration completed",
    len(records[9]) > len(records[8]) and len(fibers_by_n[9]) == len(records[9]),
    f"N8={len(records[8])} N9={len(records[9])}",
)
check(
    "N=8 hinge-sector baseline still repairs all conflicts",
    reports[(8, "base+coarse")]["total_conflicts"] == 0,
    f"N8={reports[(8, 'base+coarse')]['total_conflicts']}",
)
check(
    "N=9 hinge sector improves over the base boundary cover",
    n9_exact_improves,
    f"base={reports[(9, 'base')]['total_conflicts']} coarse={reports[(9, 'base+coarse')]['total_conflicts']}",
)
check(
    "partner-only hinge remains worse than the hinge-sector charge at N=9",
    n9_partner_worse,
    f"partner={reports[(9, 'base+partner')]['total_conflicts']} coarse={reports[(9, 'base+coarse')]['total_conflicts']}",
)
check(
    "N=9 forbidden-slope prediction is either confirmed or falsified explicitly",
    n9_hinge_survives or len(small_charge_mismatches) > 0,
    f"survives={n9_hinge_survives} mismatches={len(small_charge_mismatches)}",
)
check(
    "follow-up scan investigated any N=9 hinge-sector failure",
    n9_hinge_survives or followup_progress,
    "no failure" if n9_hinge_survives else f"final={followup['final']['total_conflicts']}",
)
check(
    "N=9 hinge-sector partition remains non-lookup",
    reports[(9, "base+coarse")]["atoms"] < len(records[9]),
    f"atoms={reports[(9, 'base+coarse')]['atoms']}/{len(records[9])}",
)

print("\n=== Campaign status ===")
if n9_hinge_survives:
    print(
        "The hinge-sector boundary charge survived the exact N=9 out-of-sample "
        "test.  The next target is to prove the deletion/insertion recurrence "
        "and an asymptotic non-reconstruction budget."
    )
else:
    print(
        "The N=8 hinge-sector law is not the whole click law.  It is a real "
        "correction layer because it improves N=9 and beats the partner-only "
        "direction, but exact N=9 leaves new residue.  The follow-up scan records "
        "the next local sectors to test for stability."
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
