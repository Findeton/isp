#!/usr/bin/env python3
"""
Paper 30 receipt: backward-then-forward multi-hole campaign.

The previous Paper 30 receipts used one-record deletion.  This campaign tests
the user's stronger idea: records are configurational, so the discovery loop
should delete small sets of records, keep only compressed boundary memory, and
then test forward insertion consistency.

All reported quantities are exact integer/Fraction counts.  If mpmath is
available it is set to dps=140 for decimal formatting; otherwise no floating
arithmetic is used.
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
    denom_factor = math.comb(n, k)
    return {
        key: tuple(sorted((item, Fraction(count, denom_factor * counts[key])) for item, count in row.items()))
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
            n: {
                child_key: dict(parent_rows)
                for child_key, parent_rows in rows.items()
            }
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
    names = []
    for group in groups:
        for feature_name in sorted(features[group]):
            names.append(f"{group}:{feature_name}")
    return names


def valid_names(features, names):
    out = []
    for name in names:
        group, feature = name.split(":", 1)
        if group in features and feature in features[group]:
            out.append(name)
    return out


def known_feature_names(features):
    return feature_names(features, ["scalar", "interval", "regularity", "matching"])


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


def all_flag_feature_names(features):
    return feature_names(features, ["flags3", "flags4", "flags5"])


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


def invariant_conflicts(P, colors, invariant):
    atoms = atoms_from_colors(colors)
    bad = 0
    conflicts = 0
    unresolved_mass = Fraction(0)
    for keys in atoms.values():
        if len(keys) > 1:
            unresolved_mass += sum(P[key] for key in keys)
        buckets = defaultdict(list)
        for key in keys:
            buckets[invariant[key]].append(key)
        if len(buckets) <= 1:
            continue
        bad += 1
        for idx, left in enumerate(keys):
            for right in keys[idx + 1 :]:
                if invariant[left] != invariant[right]:
                    conflicts += 1
    return {
        "atoms": len(atoms),
        "bad": bad,
        "conflicts": conflicts,
        "unresolved_mass": unresolved_mass,
    }


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


def transfer_conflicts(P, colors_parent, colors_child, deck_rows, reverse_rows):
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


def conflict_pairs(colors, invariant):
    atoms = atoms_from_colors(colors)
    conflicts = []
    for keys in atoms.values():
        for idx, left in enumerate(keys):
            for right in keys[idx + 1 :]:
                if invariant[left] != invariant[right]:
                    conflicts.append((left, right))
    return conflicts


def feature_conflict_mask(mapping, conflicts):
    mask = 0
    for idx, (left, right) in enumerate(conflicts):
        if mapping.get(left, 0) != mapping.get(right, 0):
            mask |= 1 << idx
    return mask


def greedy_cover(candidates, masks, full_mask):
    uncovered = full_mask
    chosen = []
    while uncovered:
        best = max(candidates, key=lambda name: (masks[name] & uncovered).bit_count())
        gain = (masks[best] & uncovered).bit_count()
        if gain == 0:
            return None
        chosen.append(best)
        uncovered &= ~masks[best]
    return chosen


def remove_dominated(candidates, masks):
    kept = []
    ordered = sorted(candidates, key=lambda name: masks[name].bit_count(), reverse=True)
    for candidate in ordered:
        mask = masks[candidate]
        if any(mask | masks[other] == masks[other] for other in kept):
            continue
        kept.append(candidate)
    return kept


def exact_cover(candidates, masks, full_mask):
    candidates = [name for name in candidates if masks[name]]
    if not candidates:
        return None, []
    union = 0
    for name in candidates:
        union |= masks[name]
    if union != full_mask:
        return None, []
    candidates = remove_dominated(candidates, masks)
    greedy = greedy_cover(candidates, masks, full_mask)
    best = list(greedy) if greedy is not None else list(candidates)
    max_gain = max(masks[name].bit_count() for name in candidates)
    coverers = defaultdict(list)
    for name in candidates:
        m = masks[name]
        while m:
            bit = (m & -m).bit_length() - 1
            coverers[bit].append(name)
            m &= m - 1
    for bit in coverers:
        coverers[bit].sort(key=lambda name: masks[name].bit_count(), reverse=True)

    visited = {}

    def choose_bit(uncovered):
        best_bit = None
        best_options = None
        m = uncovered
        while m:
            bit = (m & -m).bit_length() - 1
            options = [name for name in coverers[bit] if masks[name] & uncovered]
            if best_options is None or len(options) < len(best_options):
                best_bit = bit
                best_options = options
                if len(options) == 1:
                    break
            m &= m - 1
        return best_bit, best_options

    def search(uncovered, chosen):
        nonlocal best
        if not uncovered:
            if len(chosen) < len(best):
                best = list(chosen)
            return
        if len(chosen) >= len(best) - 1:
            return
        lower = (uncovered.bit_count() + max_gain - 1) // max_gain
        if len(chosen) + lower >= len(best):
            return
        state = (uncovered, len(chosen))
        if visited.get(state, 10**9) <= len(chosen):
            return
        visited[state] = len(chosen)
        _bit, options = choose_bit(uncovered)
        options = sorted(options, key=lambda name: (masks[name] & uncovered).bit_count(), reverse=True)
        for name in options:
            if name in chosen:
                continue
            search(uncovered & ~masks[name], chosen + [name])

    search(full_mask, [])
    return best, candidates


def run_cover_search(P, features, base_colors, invariant, label):
    conflicts = conflict_pairs(base_colors, invariant)
    full_mask = (1 << len(conflicts)) - 1
    candidates = valid_names(features, all_flag_feature_names(features))
    masks = {
        name: feature_conflict_mask(features[name.split(":", 1)[0]][name.split(":", 1)[1]], conflicts)
        for name in candidates
    }
    active = [name for name in candidates if masks[name]]
    print(
        f"{label:<18} conflicts={len(conflicts):>7} candidates={len(candidates):>4} active={len(active):>4}"
    )
    if not conflicts:
        return []
    solution, reduced = exact_cover(active, masks, full_mask)
    if solution is None:
        print(f"  no exact local flags3/4/5 cover found")
        return None
    print(f"  reduced={len(reduced)} cover_size={len(solution)} solution={solution}")
    return solution


print("=" * 80)
print("Paper 30 backward-then-forward multi-hole campaign")
print("=" * 80)
print(PRECISION_LINE)

n_min = 3
n_max = 8
ks = [1, 2, 3, 4]

records = {}
counts_by_n = {}
reps_by_n = {}
fibers_by_n = {}
features_by_n = {}
hist_by_k_n = {k: {} for k in ks}

for n in range(n_min, n_max + 1):
    P, counts, reps, fibers = build_score_data(n)
    records[n] = P
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    fibers_by_n[n] = fibers
    features_by_n[n] = light_feature_maps(P, reps, n)
    for k in ks:
        if n > k:
            hist_by_k_n[k][n] = multihole_histograms(n, k, counts, fibers)

decks, reverse = build_decks(reps_by_n, ks)

colors_known = {
    n: colors_from_features(records[n], features_by_n[n], known_feature_names(features_by_n[n]))
    for n in records
}
colors_n8_cover = {
    n: colors_from_features(records[n], features_by_n[n], valid_names(features_by_n[n], n8_cover_feature_names(features_by_n[n])))
    for n in records
}

summary = {}
print("\n" + "=" * 80)
print("Backward compressed boundary visibility and forward drift")
print("=" * 80)
for k in ks:
    summary[k] = {}
    for n in [7, 8]:
        if n <= k:
            continue
        child_n = n - k
        known_h = invariant_conflicts(records[n], colors_known[n], hist_by_k_n[k][n])
        cover_h = invariant_conflicts(records[n], colors_n8_cover[n], hist_by_k_n[k][n])
        known_t = transfer_conflicts(
            records[n],
            colors_known[n],
            colors_known[child_n],
            decks[k][n],
            reverse[k][child_n],
        )
        cover_t = transfer_conflicts(
            records[n],
            colors_n8_cover[n],
            colors_n8_cover[child_n],
            decks[k][n],
            reverse[k][child_n],
        )
        summary[k][n] = {
            "known_h": known_h,
            "cover_h": cover_h,
            "known_t": known_t,
            "cover_t": cover_t,
        }
        print(
            f"k={k} N={n} "
            f"known_H={known_h['conflicts']:>7} "
            f"cover_H={cover_h['conflicts']:>7} "
            f"known_D/I={known_t['delete_conflicts']:>5}/{known_t['insert_conflicts']:<5} "
            f"cover_D/I={cover_t['delete_conflicts']:>5}/{cover_t['insert_conflicts']:<5} "
            f"cover_atoms={cover_h['atoms']:>6}/{len(records[n]):<6} "
            f"unres={fmt_frac(cover_h['unresolved_mass'], 18)}"
        )

print("\n" + "=" * 80)
print("Local cover searches opened by multi-hole conflicts")
print("=" * 80)
cover_search_results = {}
for k in [2, 3, 4]:
    n = 8
    cover_search_results[k] = run_cover_search(
        records[n],
        features_by_n[n],
        colors_n8_cover[n],
        hist_by_k_n[k][n],
        f"k={k} N={n}",
    )


def augmented_cover_feature_names(features, cover_results):
    names = n8_cover_feature_names(features)
    for result in cover_results.values():
        if result is None:
            continue
        names.extend(result)
    # stable de-duplication
    out = []
    seen = set()
    for name in names:
        if name not in seen:
            out.append(name)
            seen.add(name)
    return out


def colors_for_extra_flags(extra_flags):
    return {
        n: colors_from_features(
            records[n],
            features_by_n[n],
            valid_names(features_by_n[n], n8_cover_feature_names(features_by_n[n]) + list(extra_flags)),
        )
        for n in records
    }


extra_flag_by_k = {
    k: tuple(cover_search_results[k] or ())
    for k in [2, 3, 4]
}
all_extra_flags = tuple(
    name
    for k in [2, 3, 4]
    for name in extra_flag_by_k[k]
)

colors_augmented = {
    n: colors_from_features(
        records[n],
        features_by_n[n],
        valid_names(features_by_n[n], augmented_cover_feature_names(features_by_n[n], cover_search_results)),
    )
    for n in records
}

print("\n" + "=" * 80)
print("Augmented multi-hole memory after following cover openings")
print("=" * 80)
augmented_summary = {}
for k in ks:
    augmented_summary[k] = {}
    for n in [7, 8]:
        if n <= k:
            continue
        child_n = n - k
        aug_h = invariant_conflicts(records[n], colors_augmented[n], hist_by_k_n[k][n])
        aug_t = transfer_conflicts(
            records[n],
            colors_augmented[n],
            colors_augmented[child_n],
            decks[k][n],
            reverse[k][child_n],
        )
        augmented_summary[k][n] = {"h": aug_h, "t": aug_t}
        print(
            f"k={k} N={n} "
            f"aug_H={aug_h['conflicts']:>7} "
            f"aug_D/I={aug_t['delete_conflicts']:>5}/{aug_t['insert_conflicts']:<5} "
            f"aug_atoms={aug_h['atoms']:>6}/{len(records[n]):<6} "
            f"unres={fmt_frac(aug_h['unresolved_mass'], 18)}"
        )

print("\n" + "=" * 80)
print("Non-lookup subset sweep for multi-hole additions")
print("=" * 80)
subset_rows = []
twolevel_rows = []
for size in range(len(all_extra_flags) + 1):
    for subset in combinations(all_extra_flags, size):
        colors_subset = colors_for_extra_flags(subset)
        h_conf = {}
        for k in ks:
            h_conf[k] = invariant_conflicts(records[8], colors_subset[8], hist_by_k_n[k][8])["conflicts"]
        atoms = invariant_conflicts(records[8], colors_subset[8], hist_by_k_n[1][8])["atoms"]
        total_conf = sum(h_conf.values())
        nonlookup = atoms < len(records[8])
        twolevel_conf = 0
        atoms_by_n = {}
        nonlookup_both = True
        for n in [7, 8]:
            atoms_by_n[n] = invariant_conflicts(records[n], colors_subset[n], hist_by_k_n[1][n])["atoms"]
            nonlookup_both = nonlookup_both and atoms_by_n[n] < len(records[n])
            for k in ks:
                if n > k:
                    twolevel_conf += invariant_conflicts(records[n], colors_subset[n], hist_by_k_n[k][n])["conflicts"]
        subset_rows.append(
            {
                "subset": subset,
                "atoms": atoms,
                "h_conf": h_conf,
                "total_conf": total_conf,
                "nonlookup": nonlookup,
            }
        )
        twolevel_rows.append(
            {
                "subset": subset,
                "atoms_by_n": atoms_by_n,
                "total_conf": twolevel_conf,
                "nonlookup_both": nonlookup_both,
            }
        )
        print(
            f"extras={list(subset)!s:<66} atoms={atoms:>6}/{len(records[8])} "
            f"nonlookup={str(nonlookup):<5} "
            + " ".join(f"k{k}={h_conf[k]:>4}" for k in ks)
            + f" total={total_conf:>5}"
        )

nonlookup_rows = [row for row in subset_rows if row["nonlookup"]]
best_nonlookup = min(nonlookup_rows, key=lambda row: (row["total_conf"], len(row["subset"]), row["atoms"]))
full_row = next(row for row in subset_rows if set(row["subset"]) == set(all_extra_flags))
twolevel_nonlookup = [row for row in twolevel_rows if row["nonlookup_both"]]
best_twolevel_nonlookup = min(
    twolevel_nonlookup,
    key=lambda row: (row["total_conf"], len(row["subset"]), row["atoms_by_n"][7] + row["atoms_by_n"][8]),
)
twolevel_exact_nonlookup = [row for row in twolevel_nonlookup if row["total_conf"] == 0]

colors_best = colors_for_extra_flags(best_nonlookup["subset"])
best_summary = {}
print("\n" + "=" * 80)
print("Weakest non-lookup multi-hole memory selected by subset sweep")
print("=" * 80)
print(f"best_extras={list(best_nonlookup['subset'])} atoms_N8={best_nonlookup['atoms']}/{len(records[8])}")
for k in ks:
    best_summary[k] = {}
    for n in [7, 8]:
        if n <= k:
            continue
        child_n = n - k
        best_h = invariant_conflicts(records[n], colors_best[n], hist_by_k_n[k][n])
        best_t = transfer_conflicts(
            records[n],
            colors_best[n],
            colors_best[child_n],
            decks[k][n],
            reverse[k][child_n],
        )
        best_summary[k][n] = {"h": best_h, "t": best_t}
        print(
            f"k={k} N={n} "
            f"best_H={best_h['conflicts']:>7} "
            f"best_D/I={best_t['delete_conflicts']:>5}/{best_t['insert_conflicts']:<5} "
            f"best_atoms={best_h['atoms']:>6}/{len(records[n]):<6} "
            f"unres={fmt_frac(best_h['unresolved_mass'], 18)}"
        )

print("\n" + "=" * 80)
print("Best two-level non-lookup subset")
print("=" * 80)
print(
    f"best_twolevel_extras={list(best_twolevel_nonlookup['subset'])} "
    f"total_conf={best_twolevel_nonlookup['total_conf']} "
    f"atoms_N7={best_twolevel_nonlookup['atoms_by_n'][7]}/{len(records[7])} "
    f"atoms_N8={best_twolevel_nonlookup['atoms_by_n'][8]}/{len(records[8])}"
)

check(
    "single-hole fixed N8 cover makes Hbar visible at N=7 and N=8",
    summary[1][7]["cover_h"]["conflicts"] == 0 and summary[1][8]["cover_h"]["conflicts"] == 0,
    f"N7={summary[1][7]['cover_h']['conflicts']} N8={summary[1][8]['cover_h']['conflicts']}",
)
check(
    "two-hole deletion exposes new joint residue beyond the single-hole cover",
    summary[2][8]["cover_h"]["conflicts"] > 0,
    f"k2_N8_conflicts={summary[2][8]['cover_h']['conflicts']}",
)
check(
    "three-hole deletion exposes new joint residue beyond the single-hole cover",
    summary[3][8]["cover_h"]["conflicts"] > 0,
    f"k3_N8_conflicts={summary[3][8]['cover_h']['conflicts']}",
)
check(
    "four-hole deletion is tested as the next multi-record opening",
    8 in summary[4] and summary[4][8]["cover_h"]["conflicts"] >= 0,
    f"k4_N8_conflicts={summary[4][8]['cover_h']['conflicts']}",
)
check(
    "fixed N8 cover still controls k=2 drift relative to known sectors",
    summary[2][8]["cover_t"]["delete_conflicts"] < summary[2][8]["known_t"]["delete_conflicts"]
    and summary[2][8]["cover_t"]["insert_conflicts"] < summary[2][8]["known_t"]["insert_conflicts"],
    (
        f"D {summary[2][8]['known_t']['delete_conflicts']}->{summary[2][8]['cover_t']['delete_conflicts']} "
        f"I {summary[2][8]['known_t']['insert_conflicts']}->{summary[2][8]['cover_t']['insert_conflicts']}"
    ),
)
check(
    "multi-hole residue requires new local operators or a stronger boundary memory",
    cover_search_results[2] is not None or cover_search_results[3] is not None or cover_search_results[4] is not None,
    (
        f"k2_cover={'none' if cover_search_results[2] is None else len(cover_search_results[2])} "
        f"k3_cover={'none' if cover_search_results[3] is None else len(cover_search_results[3])} "
        f"k4_cover={'none' if cover_search_results[4] is None else len(cover_search_results[4])}"
    ),
)
check(
    "augmented multi-hole memory makes k=1..4 Hbar visible at N=8",
    all(augmented_summary[k][8]["h"]["conflicts"] == 0 for k in ks),
    "conflicts=" + ", ".join(f"k{k}:{augmented_summary[k][8]['h']['conflicts']}" for k in ks),
)
check(
    "full augmented multi-hole memory becomes lookup and is rejected",
    augmented_summary[1][8]["h"]["atoms"] == len(records[8]),
    f"atoms={augmented_summary[1][8]['h']['atoms']}/{len(records[8])}",
)
check(
    "best non-lookup subset solves k=1..4 at N=8",
    best_nonlookup["total_conf"] == 0,
    (
        f"best={list(best_nonlookup['subset'])} total={best_nonlookup['total_conf']} "
        f"atoms={best_nonlookup['atoms']}/{len(records[8])}"
    ),
)
check(
    "best non-lookup subset also solves k=1..4 at N=7",
    all(best_summary[k][7]["h"]["conflicts"] == 0 for k in ks if 7 > k),
    "conflicts=" + ", ".join(
        f"k{k}:{best_summary[k][7]['h']['conflicts']}" for k in ks if 7 > k
    ),
)
check(
    "no subset solves k=1..4 at both N=7 and N=8 while non-lookup at both",
    len(twolevel_exact_nonlookup) == 0,
    (
        "exact_nonlookup_both="
        + str([list(row["subset"]) for row in twolevel_exact_nonlookup])
    ),
)
check(
    "two-level non-lookup guard blocks improvement in tested subset family",
    best_twolevel_nonlookup["total_conf"] == next(row for row in twolevel_rows if not row["subset"])["total_conf"],
    (
        f"base={next(row for row in twolevel_rows if not row['subset'])['total_conf']} "
        f"best={best_twolevel_nonlookup['total_conf']}"
    ),
)

print("\n=== Campaign status ===")
print(
    "The backward-then-forward idea is real and sharper than the one-hole "
    "filtration.  The fixed N=8 one-hole cover predicts the one-hole boundary "
    "law at N=7,8, but multi-hole deletions expose additional joint residue.  "
    "Following the openings adds a small number of local flag operators.  The "
    "full addition becomes lookup and is rejected, but the subset sweep finds "
    "a weaker non-lookup-at-N=8 multi-hole memory that solves k=1..4 at N=7,8 "
    "in the audited window, although it becomes lookup at N=7.  If non-lookup "
    "is demanded at both levels, the tested subset family cannot improve the "
    "base residue.  That supports the configurational view and sharpens the "
    "target: the click law should be a weakest sufficient multi-hole boundary "
    "memory with an explicit scale-dependent non-reconstruction budget, not a "
    "full closure under every refinement and not an over-strict all-level "
    "non-lookup veto."
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
