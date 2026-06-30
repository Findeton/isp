#!/usr/bin/env python3
"""
Paper 30 receipt: quadratic-norm uniqueness campaign.

The previous receipt found an exact finite collapse:

    full dual-orbit data (F_j, F_j*)_{j=1..3}

has the same h-transform weights and recurrence as the smaller quotient

    E_total = sum_j (F_j + F_j*)
    Q_odd   = sum_j (F_j - F_j*)^2

for N=5..9 in the audited 2D permutation-order sector.

This campaign asks whether that is accidental or theorem-shaped.  It runs six
attacks:

1. exhaustive low-N scan among all dual triples from flag5 sectors, followed
   by full N=9 audits of the low-N frontier and descriptor-preserving siblings;
2. invariant family scan: L1/L2/Linf/product/cube alternatives;
3. O(3)-style symmetry audit by permuting the three odd axes;
4. deletion/recurrence preservation of the quadratic quotient;
5. hostile collision audit: records merged by (E_total,Q_odd);
6. exact classification of successful triples by descriptors.

All core quantities are exact integers/Fractions. Decimal is used only for
reporting at precision 140 (>80-bit).
"""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations, product
import math
import sys

from p29_projected_likelihood_basis_audit import (
    bit_index,
    canon_bits,
    degree_moments,
    fmt_frac,
    has_rel,
    height,
    interval_counts,
    permutation_order_bits,
    perms,
    relation_count,
    restrict_bits,
)

getcontext().prec = 140
D = Decimal
sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(20000)

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def build_record_universe(n):
    counts = defaultdict(int)
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        counts[key] += 1
    dist = {key: Fraction(count, math.factorial(n)) for key, count in counts.items()}
    print(f"  built N={n}: permutations={math.factorial(n)} records={len(counts)}")
    return dict(counts), reps, dist


def delete_deck(bits, n):
    deck = defaultdict(int)
    for deleted in range(n):
        subset = tuple(v for v in range(n) if v != deleted)
        child_bits = restrict_bits(bits, n, subset)
        child_key = canon_bits(child_bits, n - 1)
        deck[child_key] += 1
    return dict(deck)


def build_decks_and_reverse(reps_by_n, n_min, n_max):
    decks = {}
    reverse = {}
    for child_n in range(n_min, n_max):
        parent_n = child_n + 1
        rows = defaultdict(dict)
        decks[parent_n] = {}
        for parent_key, bits in reps_by_n[parent_n].items():
            deck = delete_deck(bits, parent_n)
            decks[parent_n][parent_key] = deck
            for child_key, multiplicity in deck.items():
                rows[child_key][parent_key] = multiplicity
        reverse[child_n] = dict(rows)
        print(
            f"  extension N={child_n}->{parent_n}: children={len(rows)} "
            f"parents={len(reps_by_n[parent_n])}"
        )
    return decks, reverse


RAW_TO_CANON_CACHE = {}


def raw_to_canon(k):
    if k not in RAW_TO_CANON_CACHE:
        RAW_TO_CANON_CACHE[k] = {
            permutation_order_bits(pi): canon_bits(permutation_order_bits(pi), k)
            for pi in perms(k)
        }
    return RAW_TO_CANON_CACHE[k]


def all_flag_keys(k):
    return tuple(sorted(set(raw_to_canon(k).values())))


SUBSET_PAIR_CACHE = {}


def subset_pair_maps(n, k):
    maps = []
    for subset in combinations(range(n), k):
        pairs = []
        for a, old_a in enumerate(subset):
            for b, old_b in enumerate(subset):
                if a == b:
                    continue
                pairs.append((bit_index(n, old_a, old_b), bit_index(k, a, b)))
        maps.append(tuple(pairs))
    return tuple(maps)


def fast_flag_counts(bits, n, k):
    if n < k:
        return {}
    cache_key = (n, k)
    if cache_key not in SUBSET_PAIR_CACHE:
        SUBSET_PAIR_CACHE[cache_key] = subset_pair_maps(n, k)
    raw_canon = raw_to_canon(k)
    counts = defaultdict(int)
    for pair_map in SUBSET_PAIR_CACHE[cache_key]:
        raw = 0
        for source_pos, target_pos in pair_map:
            if (bits >> source_pos) & 1:
                raw |= 1 << target_pos
        counts[raw_canon[raw]] += 1
    return dict(counts)


def comparability_masks(bits, n):
    masks = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if has_rel(bits, n, i, j) or has_rel(bits, n, j, i):
                masks[i] |= 1 << j
                masks[j] |= 1 << i
    return masks


def fast_width_from_masks(masks, n):
    best = 0
    for mask in range(1 << n):
        size = mask.bit_count()
        if size <= best:
            continue
        ok = True
        rem = mask
        while rem:
            bit = rem & -rem
            v = bit.bit_length() - 1
            if masks[v] & mask:
                ok = False
                break
            rem ^= bit
        if ok:
            best = size
    return best


def matching_counts_from_masks(masks, n):
    max_r = n // 2
    memo = {}

    def rec(mask):
        if mask in memo:
            return memo[mask]
        if mask == 0:
            out = [0] * (max_r + 1)
            out[0] = 1
            memo[mask] = tuple(out)
            return memo[mask]
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit
        out = list(rec(rest))
        available = masks[v] & rest
        while available:
            u_bit = available & -available
            sub = rec(rest ^ u_bit)
            for r in range(1, max_r + 1):
                out[r] += sub[r - 1]
            available ^= u_bit
        memo[mask] = tuple(out)
        return memo[mask]

    return rec((1 << n) - 1)


def known_tuple(bits, n):
    masks = comparability_masks(bits, n)
    matchings = matching_counts_from_masks(masks, n)
    return (
        relation_count(bits, n),
        height(bits, n),
        fast_width_from_masks(masks, n),
        tuple(interval_counts(bits, n)),
        degree_moments(bits, n),
        tuple(matchings[1:]),
    )


def opposite_bits(bits, n):
    out = 0
    for i in range(n):
        for j in range(n):
            if i != j and has_rel(bits, n, i, j):
                out |= 1 << bit_index(n, j, i)
    return out


def dual_key(key, n):
    return canon_bits(opposite_bits(key, n), n)


def build_feature_cache(reps_by_n, n_min, n_max):
    cache = {}
    for n in range(n_min, n_max + 1):
        known = {}
        flags5 = {}
        print(f"  feature cache N={n}: records={len(reps_by_n[n])}")
        for key, bits in reps_by_n[n].items():
            known[key] = known_tuple(bits, n)
            flags5[key] = fast_flag_counts(bits, n, 5)
        cache[n] = {"known": known, "flags5": flags5}
    return cache


def dual_orbits():
    seen = set()
    out = []
    for sector in FLAG5_KEYS:
        if sector in seen:
            continue
        d = dual_key(sector, 5)
        orbit = tuple(sorted({sector, d}))
        seen.update(orbit)
        if len(orbit) == 2:
            out.append(orbit)
    return tuple(out)


TARGET_PAIRS = ((24576, 540672), (25488, 525208), (24606, 549648))
TARGET_PAIR_SET = frozenset(TARGET_PAIRS)


def same_pair_set(pairs, target=TARGET_PAIR_SET):
    return frozenset(pairs) == target


def pair_values(flags, pairs):
    values = []
    for left, right in pairs:
        lval = flags.get(left, 0)
        rval = flags.get(right, 0)
        even = lval + rval
        odd = lval - rval
        values.append((even, odd))
    return tuple(values)


def pair_descriptor(pair):
    left, right = pair
    left_bits = left
    right_bits = right

    def desc(bits):
        covers = 0
        n = 5
        for i in range(n):
            for j in range(n):
                if i == j or not has_rel(bits, n, i, j):
                    continue
                if not any(
                    k != i and k != j and has_rel(bits, n, i, k) and has_rel(bits, n, k, j)
                    for k in range(n)
                ):
                    covers += 1
        masks = comparability_masks(bits, n)
        return (
            relation_count(bits, n),
            height(bits, n),
            fast_width_from_masks(masks, n),
            covers,
        )

    return tuple(sorted((desc(left_bits), desc(right_bits))))


def colors_for_pairs(n, pairs, mode):
    colors = {}
    for key in reps_by_n[n]:
        base = feature_cache[n]["known"][key]
        flags = feature_cache[n]["flags5"][key]
        vals = pair_values(flags, pairs)
        if mode == "full":
            extra = tuple((flags.get(a, 0), flags.get(b, 0)) for a, b in pairs)
        elif mode == "even_abs":
            extra = tuple((even, abs(odd)) for even, odd in vals)
        elif mode == "agg_l2":
            extra = (sum(even for even, _odd in vals), sum(odd * odd for _even, odd in vals))
        elif mode == "agg_l1":
            extra = (sum(even for even, _odd in vals), sum(abs(odd) for _even, odd in vals))
        elif mode == "agg_linf":
            extra = (sum(even for even, _odd in vals), max(abs(odd) for _even, odd in vals))
        elif mode == "weighted_l2_a":
            weights = (1, 2, 3)
            extra = (sum(even for even, _odd in vals), sum(w * odd * odd for w, (_even, odd) in zip(weights, vals)))
        elif mode == "weighted_l2_b":
            weights = (1, 1, 2)
            extra = (sum(even for even, _odd in vals), sum(w * odd * odd for w, (_even, odd) in zip(weights, vals)))
        else:
            raise ValueError(mode)
        colors[key] = ("pairs", mode, base, extra)
    return colors


def colors_for_weighted_l2(n, pairs, weights_tuple):
    colors = {}
    for key in reps_by_n[n]:
        base = feature_cache[n]["known"][key]
        flags = feature_cache[n]["flags5"][key]
        vals = pair_values(flags, pairs)
        extra = (
            sum(even for even, _odd in vals),
            sum(w * odd * odd for w, (_even, odd) in zip(weights_tuple, vals)),
        )
        colors[key] = ("pairs", "weighted_l2_family", weights_tuple, base, extra)
    return colors


def atom_weights(colors, counts):
    atom_counts = defaultdict(int)
    atom_sizes = defaultdict(int)
    for key, color in colors.items():
        atom_counts[color] += counts[key]
        atom_sizes[color] += 1
    return {key: Fraction(atom_counts[colors[key]], atom_sizes[colors[key]]) for key in colors}


def atom_metrics(colors):
    atoms = defaultdict(list)
    for key, color in colors.items():
        atoms[color].append(key)
    return {
        "atoms": len(atoms),
        "lookup": len(atoms) == len(colors),
        "max_atom": max(len(keys) for keys in atoms.values()),
    }


def model_for_pairs(pairs, mode, target_n=9):
    colors = {}
    weights = {}
    metrics = {}
    for n in range(1, target_n + 1):
        colors[n] = colors_for_pairs(n, pairs, mode)
        weights[n] = atom_weights(colors[n], counts_by_n[n])
        metrics[n] = atom_metrics(colors[n])
    return colors, weights, metrics


def model_for_pair_levels(pairs, mode, levels):
    colors = {}
    weights = {}
    metrics = {}
    for n in levels:
        colors[n] = colors_for_pairs(n, pairs, mode)
        weights[n] = atom_weights(colors[n], counts_by_n[n])
        metrics[n] = atom_metrics(colors[n])
    return colors, weights, metrics


def model_for_weighted_l2(pairs, weights_tuple, levels):
    colors = {}
    weights = {}
    metrics = {}
    for n in levels:
        colors[n] = colors_for_weighted_l2(n, pairs, weights_tuple)
        weights[n] = atom_weights(colors[n], counts_by_n[n])
        metrics[n] = atom_metrics(colors[n])
    return colors, weights, metrics


def total_variation(left, right):
    keys = set(left) | set(right)
    return sum(abs(left.get(key, Fraction(0)) - right.get(key, Fraction(0))) for key in keys) / 2


def forward_step(dist, n, weights_by_n):
    out = defaultdict(Fraction)
    weights = weights_by_n[n + 1]
    for child_key, child_prob in dist.items():
        local = {}
        denom = Fraction(0)
        for parent_key, multiplicity in reverse[n][child_key].items():
            value = weights[parent_key] * multiplicity
            local[parent_key] = value
            denom += value
        for parent_key, value in local.items():
            out[parent_key] += child_prob * value / denom
    return dict(out)


def forward_tv_to(weights_by_n, target_n=9):
    dist = exact_by_n[1]
    for n in range(1, target_n):
        dist = forward_step(dist, n, weights_by_n)
    return total_variation(dist, exact_by_n[target_n])


def forward_tv(weights_by_n):
    return forward_tv_to(weights_by_n, 9)


def recurrence_errors(parent_n, parent_weights, child_weights):
    child_n = parent_n - 1
    exact_error = Fraction(0)
    quotient_error = Fraction(0)
    total_child = math.factorial(child_n)
    for child_key, child_count in counts_by_n[child_n].items():
        z = Fraction(0)
        for parent_key, multiplicity in reverse[child_n][child_key].items():
            z += parent_weights[parent_key] * multiplicity
        target_exact = Fraction(child_count * parent_n * parent_n)
        target_quotient = child_weights[child_key] * parent_n * parent_n
        exact_error += Fraction(child_count, total_child) * abs(z - target_exact) / target_exact
        quotient_error += Fraction(child_count, total_child) * abs(z - target_quotient) / target_quotient
    return exact_error, quotient_error


def coarsening_identity(fine_colors, coarse_colors, fine_weights, coarse_weights, n):
    violations = 0
    max_diff = Fraction(0)
    fibers = defaultdict(set)
    for key in reps_by_n[n]:
        fibers[coarse_colors[n][key]].add(fine_weights[n][key])
        max_diff = max(max_diff, abs(fine_weights[n][key] - coarse_weights[n][key]))
    for values in fibers.values():
        if len(values) != 1:
            violations += 1
    return violations, max_diff


def child_profile(colors_parent, colors_child, n):
    profile = {}
    for key in reps_by_n[n]:
        row = defaultdict(int)
        for child_key, multiplicity in decks[n][key].items():
            row[colors_child[child_key]] += multiplicity
        profile[key] = tuple(sorted(row.items()))
    return profile


def profile_conflicts(colors, profile):
    groups = defaultdict(lambda: defaultdict(int))
    for key, color in colors.items():
        groups[color][profile[key]] += 1
    bad = 0
    pairs = 0
    for profiles in groups.values():
        if len(profiles) <= 1:
            continue
        bad += 1
        total = sum(profiles.values())
        same = sum(count * (count - 1) // 2 for count in profiles.values())
        pairs += total * (total - 1) // 2 - same
    return bad, pairs


def dec_frac(value):
    return D(value.numerator) / D(value.denominator)


def fmt_dec_frac(value, digits=28):
    return format(+dec_frac(value), f".{digits}g")


print("=" * 80)
print("Paper 30 quadratic-norm uniqueness campaign")
print("=" * 80)
print(f"Decimal precision: prec={getcontext().prec}")

counts_by_n = {}
reps_by_n = {}
exact_by_n = {}

print("\n" + "=" * 80)
print("Exact record universes")
print("=" * 80)
for n in range(1, 10):
    counts, reps, dist = build_record_universe(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    exact_by_n[n] = dist

print("\n" + "=" * 80)
print("Deletion graph")
print("=" * 80)
decks, reverse = build_decks_and_reverse(reps_by_n, 1, 9)

print("\n" + "=" * 80)
print("Feature cache")
print("=" * 80)
feature_cache = build_feature_cache(reps_by_n, 1, 9)
FLAG5_KEYS = all_flag_keys(5)
ORBITS = dual_orbits()

print("\n" + "=" * 80)
print("Baseline target model")
print("=" * 80)
full_colors, full_weights, full_metrics = model_for_pairs(TARGET_PAIRS, "full")
target_colors, target_weights, target_metrics = model_for_pairs(TARGET_PAIRS, "agg_l2")
target_tv = forward_tv(target_weights)
target_rec = recurrence_errors(9, target_weights[9], target_weights[8])
print(f"  target_pairs={TARGET_PAIRS}")
print(
    f"  agg_l2 atoms9={target_metrics[9]['atoms']} TV9={fmt_frac(target_tv, 24)} "
    f"rec9={fmt_frac(target_rec[0], 24)}"
)

print("\n" + "=" * 80)
print("1. Exhaustive low-N dual-triple scan and N=9 frontier audit")
print("=" * 80)
low_rows = []
for pairs in combinations(ORBITS, 3):
    colors, weights, metrics = model_for_pairs(pairs, "agg_l2", target_n=7)
    tv = forward_tv_to(weights, 7)
    rec = recurrence_errors(7, weights[7], weights[6])
    low_rows.append(
        {
            "pairs": pairs,
            "tv": tv,
            "rec": rec[0],
            "atoms": metrics[7]["atoms"],
            "lookup": metrics[7]["lookup"],
        }
    )
low_rows.sort(key=lambda row: (row["tv"], row["rec"], -row["atoms"], row["pairs"]))
target_low_tv = next(row["tv"] for row in low_rows if same_pair_set(row["pairs"]))
for rank, row in enumerate(low_rows[:12], start=1):
    marker = "TARGET" if same_pair_set(row["pairs"]) else ""
    print(
        f"  low-rank={rank:<2} {marker:<6} pairs={row['pairs']} atoms7={row['atoms']} "
        f"TV7={fmt_frac(row['tv'], 24)} rec7={fmt_frac(row['rec'], 24)}"
    )
target_low_rank = next(idx for idx, row in enumerate(low_rows, start=1) if same_pair_set(row["pairs"]))
same_low_tv_rows = [row for row in low_rows if row["tv"] == target_low_tv]
print(f"  target_low_rank={target_low_rank} same_low_TV_count={len(same_low_tv_rows)}")

target_descriptors = tuple(pair_descriptor(pair) for pair in TARGET_PAIRS)
descriptor_siblings = []
for pair_a in ORBITS:
    for pair_b in ORBITS:
        for pair_c in ORBITS:
            pairs = (pair_a, pair_b, pair_c)
            if len(set(pairs)) != 3:
                continue
            if tuple(pair_descriptor(pair) for pair in pairs) == target_descriptors:
                descriptor_siblings.append(pairs)
descriptor_siblings = tuple(sorted(set(descriptor_siblings)))
print(f"  descriptor_sibling_count={len(descriptor_siblings)}")

zero_frontier_pairs = {row["pairs"] for row in same_low_tv_rows}
print("  exact local N=9 recurrence scan over the N=7 zero-TV frontier...")
local_frontier_rows = []
for idx, pairs in enumerate(sorted(zero_frontier_pairs), start=1):
    _colors, weights, metrics = model_for_pair_levels(pairs, "agg_l2", (8, 9))
    rec = recurrence_errors(9, weights[9], weights[8])
    local_frontier_rows.append(
        {
            "pairs": pairs,
            "rec": rec[0],
            "qrec": rec[1],
            "atoms": metrics[9]["atoms"],
        }
    )
    if idx % 32 == 0 or idx == len(zero_frontier_pairs):
        print(f"    local recurrence candidates audited: {idx}/{len(zero_frontier_pairs)}")
local_frontier_rows.sort(key=lambda row: (row["rec"], row["qrec"], -row["atoms"], row["pairs"]))
for rank, row in enumerate(local_frontier_rows[:12], start=1):
    marker = "TARGET" if same_pair_set(row["pairs"]) else ""
    print(
        f"  local-rank={rank:<2} {marker:<6} pairs={row['pairs']} atoms9={row['atoms']} "
        f"rec9={fmt_frac(row['rec'], 24)} qrec9={fmt_frac(row['qrec'], 24)}"
    )
target_local_rank = next(
    idx for idx, row in enumerate(local_frontier_rows, start=1) if same_pair_set(row["pairs"])
)
print(f"  target_local_rank_in_zero_frontier={target_local_rank}")

frontier_pairs = {TARGET_PAIRS}
for row in low_rows[:24]:
    frontier_pairs.add(row["pairs"])
for row in local_frontier_rows[:24]:
    frontier_pairs.add(row["pairs"])
for pairs in descriptor_siblings:
    frontier_pairs.add(pairs)

triple_rows = []
for pairs in sorted(frontier_pairs):
    colors, weights, metrics = model_for_pairs(pairs, "agg_l2")
    tv = forward_tv(weights)
    rec = recurrence_errors(9, weights[9], weights[8])
    triple_rows.append(
        {
            "pairs": pairs,
            "tv": tv,
            "rec": rec[0],
            "atoms": metrics[9]["atoms"],
            "lookup": metrics[9]["lookup"],
            "descriptor_sibling": pairs in descriptor_siblings,
        }
    )
triple_rows.sort(key=lambda row: (row["tv"], row["rec"], -row["atoms"], row["pairs"]))
for rank, row in enumerate(triple_rows[:16], start=1):
    marker = "TARGET" if same_pair_set(row["pairs"]) else ""
    sibling = "sibling" if row["descriptor_sibling"] else ""
    print(
        f"  N9-rank={rank:<2} {marker:<6} {sibling:<7} pairs={row['pairs']} atoms9={row['atoms']} "
        f"TV9={fmt_frac(row['tv'], 24)} rec9={fmt_frac(row['rec'], 24)}"
    )
target_rank = next(idx for idx, row in enumerate(triple_rows, start=1) if same_pair_set(row["pairs"]))
same_tv_rows = [row for row in triple_rows if row["tv"] == target_tv]
descriptor_beaters = [
    row for row in triple_rows
    if row["descriptor_sibling"] and (row["tv"], row["rec"]) < (target_tv, target_rec[0])
]
print(
    f"  N9_frontier_count={len(triple_rows)} target_N9_rank={target_rank} "
    f"same_frontier_TV_count={len(same_tv_rows)} descriptor_beaters={len(descriptor_beaters)}"
)

print("\n" + "=" * 80)
print("2. Invariant family scan")
print("=" * 80)
mode_rows = []
for mode in ("agg_l1", "agg_l2", "agg_linf", "weighted_l2_a", "weighted_l2_b", "even_abs"):
    colors, weights, metrics = model_for_pairs(TARGET_PAIRS, mode)
    tv = forward_tv(weights)
    rec = recurrence_errors(9, weights[9], weights[8])
    identity = coarsening_identity(full_colors, colors, full_weights, weights, 9)
    mode_rows.append((mode, tv, rec[0], metrics[9]["atoms"], identity))
    print(
        f"  {mode:<13} atoms9={metrics[9]['atoms']:<7} TV9={fmt_frac(tv, 24)} "
        f"rec9={fmt_frac(rec[0], 24)} violations={identity[0]} maxdiff={identity[1]}"
    )

print("\n" + "=" * 80)
print("2b. Weighted quadratic metric family")
print("=" * 80)


def normalize_weights(weights_tuple):
    divisor = 0
    for value in weights_tuple:
        divisor = math.gcd(divisor, value)
    if divisor == 0:
        return None
    return tuple(value // divisor for value in weights_tuple)


weighted_family_rows = []
seen_weight_metrics = set()
for raw_weights in product(range(0, 7), repeat=3):
    weights_tuple = normalize_weights(raw_weights)
    if weights_tuple is None or weights_tuple in seen_weight_metrics:
        continue
    seen_weight_metrics.add(weights_tuple)
    colors, weights_by_n, metrics = model_for_weighted_l2(TARGET_PAIRS, weights_tuple, (8, 9))
    identities = [
        coarsening_identity(full_colors, colors, full_weights, weights_by_n, n)
        for n in (8, 9)
    ]
    ok = all(violations == 0 and maxdiff == 0 for violations, maxdiff in identities)
    weighted_family_rows.append(
        {
            "weights": weights_tuple,
            "ok": ok,
            "atoms": metrics[9]["atoms"],
            "max_atom": metrics[9]["max_atom"],
            "rec": None,
            "qrec": None,
            "identity": identities[-1],
        }
    )
    if len(seen_weight_metrics) % 40 == 0:
        print(f"    weight metrics audited: {len(seen_weight_metrics)}")

weighted_ok_rows = [row for row in weighted_family_rows if row["ok"]]
weighted_ok_rows.sort(key=lambda row: (row["atoms"], row["weights"]))
weighted_family_rows.sort(key=lambda row: (not row["ok"], row["atoms"], row["weights"]))
for row in weighted_ok_rows[:20]:
    _colors, weights_by_n, _metrics = model_for_weighted_l2(TARGET_PAIRS, row["weights"], (8, 9))
    rec = recurrence_errors(9, weights_by_n[9], weights_by_n[8])
    row["rec"] = rec[0]
    row["qrec"] = rec[1]
print(f"  scanned_weight_metrics={len(weighted_family_rows)} exact_hcollapse_metrics={len(weighted_ok_rows)}")
for row in weighted_ok_rows[:12]:
    marker = "UNWEIGHTED" if row["weights"] == (1, 1, 1) else ""
    rec_text = fmt_frac(row["rec"], 24) if row["rec"] is not None else "not-audited"
    print(
        f"  ok {marker:<10} weights={row['weights']} atoms9={row['atoms']} max_atom={row['max_atom']} "
        f"rec9={rec_text}"
    )
unweighted_metric_rank = next(
    idx for idx, row in enumerate(weighted_ok_rows, start=1) if row["weights"] == (1, 1, 1)
)
best_weighted_metric = weighted_ok_rows[0]
print(
    f"  unweighted_metric_rank={unweighted_metric_rank} "
    f"best_metric={best_weighted_metric['weights']} best_atoms={best_weighted_metric['atoms']}"
)

print("\n" + "=" * 80)
print("3. O(3)-style permutation audit")
print("=" * 80)
permuted_ok = True
for permuted in (
    (TARGET_PAIRS[0], TARGET_PAIRS[2], TARGET_PAIRS[1]),
    (TARGET_PAIRS[1], TARGET_PAIRS[0], TARGET_PAIRS[2]),
    (TARGET_PAIRS[1], TARGET_PAIRS[2], TARGET_PAIRS[0]),
    (TARGET_PAIRS[2], TARGET_PAIRS[0], TARGET_PAIRS[1]),
    (TARGET_PAIRS[2], TARGET_PAIRS[1], TARGET_PAIRS[0]),
):
    colors, weights, metrics = model_for_pairs(permuted, "agg_l2")
    tv = forward_tv(weights)
    ok = tv == target_tv and metrics[9]["atoms"] == target_metrics[9]["atoms"]
    permuted_ok = permuted_ok and ok
    print(
        f"  permuted={permuted} ok={ok} atoms={metrics[9]['atoms']} TV9={fmt_frac(tv, 24)}"
    )

print("\n" + "=" * 80)
print("4. Deletion/recurrence preservation")
print("=" * 80)
rec_rows = []
drift_rows = []
for parent_n in range(6, 10):
    full_rec = recurrence_errors(parent_n, full_weights[parent_n], full_weights[parent_n - 1])
    agg_rec = recurrence_errors(parent_n, target_weights[parent_n], target_weights[parent_n - 1])
    rec_rows.append((parent_n, full_rec, agg_rec))
    full_profile = child_profile(full_colors[parent_n], full_colors[parent_n - 1], parent_n)
    agg_profile = child_profile(target_colors[parent_n], target_colors[parent_n - 1], parent_n)
    full_drift = profile_conflicts(full_colors[parent_n], full_profile)
    agg_drift = profile_conflicts(target_colors[parent_n], agg_profile)
    drift_rows.append((parent_n, full_drift, agg_drift))
    print(
        f"  {parent_n-1}->{parent_n}: full_rec={fmt_frac(full_rec[0], 24)} "
        f"agg_rec={fmt_frac(agg_rec[0], 24)} full_Dpairs={full_drift[1]} agg_Dpairs={agg_drift[1]}"
    )

print("\n" + "=" * 80)
print("5. Hostile collision audit")
print("=" * 80)
collision_rows = []
for n in range(5, 10):
    violations, maxdiff = coarsening_identity(full_colors, target_colors, full_weights, target_weights, n)
    metric = target_metrics[n]
    collision_rows.append((n, violations, maxdiff, metric))
    print(
        f"  N={n}: atoms={metric['atoms']} max_atom={metric['max_atom']} "
        f"violations={violations} maxdiff={maxdiff}"
    )

print("\n" + "=" * 80)
print("6. Successful triple descriptors")
print("=" * 80)
successful_rows = [row for row in triple_rows if row["tv"] == target_tv]
for row in successful_rows[:12]:
    descriptors = tuple(pair_descriptor(pair) for pair in row["pairs"])
    print(f"  pairs={row['pairs']} descriptors={descriptors}")

print("\n" + "=" * 80)
print("Hostile review")
print("=" * 80)
print(
    "1. The receipt no longer claims a brute-force full N=9 uniqueness theorem "
    "over every flag5 triple.  It makes the finite statement actually audited: "
    "all triples are scanned at N=7, then the low-N frontier and all "
    "descriptor-preserving siblings are audited at full N=9."
)
print(
    "2. The quadratic form is theorem-shaped, but the Euclidean metric is not "
    "forced by this finite data.  Several weighted quadratic metrics preserve "
    "the exact h-collapse; L1 and Linf do not."
)
print(
    "3. The O(3)-style statement is finite and modest: permutation of the three "
    "axes is gauge, while unequal weights are a metric gauge/family rather than "
    "a falsification of the quadratic sector."
)
print(
    "4. The collapse preserves h-weights and recurrence exactly, but deletion "
    "drift may still change because the quotient is coarser.  That is admissible "
    "only if controlled."
)

best_row = triple_rows[0]
target_row = next(row for row in triple_rows if same_pair_set(row["pairs"]))

check(
    "all-triple low-N scan completed and target is in audited N=9 frontier",
    target_low_rank > 0 and any(same_pair_set(row["pairs"]) for row in triple_rows),
    f"target_low_rank={target_low_rank} frontier_count={len(triple_rows)}",
)
check(
    "N=9 frontier falsifies target-as-best and exposes exact alternatives",
    best_row["tv"] == 0 and target_rank > 1,
    f"best={best_row['pairs']} target_rank={target_rank} best_TV={fmt_frac(best_row['tv'], 18)}",
)
check(
    "no descriptor-preserving sibling beats the target at full N=9",
    len(descriptor_beaters) == 0,
    f"descriptor_sibling_count={len(descriptor_siblings)} beaters={len(descriptor_beaters)} best={best_row['pairs']}",
)
check(
    "target triple is nonlookup and below full dual-orbit atom count",
    (not target_metrics[9]["lookup"]) and target_metrics[9]["atoms"] < full_metrics[9]["atoms"],
    f"target_atoms={target_metrics[9]['atoms']} full_atoms={full_metrics[9]['atoms']}",
)
check(
    "weighted quadratic h-collapse is a metric family, not unique Euclidean L2",
    len(weighted_ok_rows) > 1 and unweighted_metric_rank > 1 and best_weighted_metric["atoms"] <= target_metrics[9]["atoms"],
    f"ok_metrics={len(weighted_ok_rows)} unweighted_rank={unweighted_metric_rank} "
    f"best={best_weighted_metric['weights']}:{best_weighted_metric['atoms']}",
)
check(
    "L1 and Linf aggregates are worse than odd L2",
    all(tv > target_tv for mode, tv, _rec, _atoms, _identity in mode_rows if mode in ("agg_l1", "agg_linf")),
    "; ".join(f"{mode}:{fmt_frac(tv, 18)}" for mode, tv, _rec, _atoms, _identity in mode_rows),
)
check(
    "permuting the three odd axes is gauge for agg_l2",
    permuted_ok,
    "all tested permutations preserve atoms and TV",
)
check(
    "agg_l2 preserves full dual-orbit recurrence exactly at all audited levels",
    all(full_rec == agg_rec for _n, full_rec, agg_rec in rec_rows),
    "; ".join(f"{n}:{full_rec[0]-agg_rec[0]}" for n, full_rec, agg_rec in rec_rows),
)
check(
    "agg_l2 h-collapse is exact on every audited level N=5..9",
    all(violations == 0 and maxdiff == 0 for _n, violations, maxdiff, _metric in collision_rows),
    "; ".join(f"N{n}:v{violations}:d{maxdiff}" for n, violations, maxdiff, _metric in collision_rows),
)
check(
    "coarsening is real: agg_l2 merges records at N=9",
    target_metrics[9]["max_atom"] > 1,
    f"max_atom={target_metrics[9]['max_atom']}",
)
check(
    "target triple descriptor class is nonempty and recorded",
    bool(successful_rows),
    f"successful_count={len(successful_rows)}",
)

print("\n=== Campaign status ===")
print(
    "The quadratic-norm target is not the final law.  The receipt exhausts all "
    "dual triples at N=7, audits the resulting local frontier at N=9, and finds "
    "exact zero-TV alternatives that beat the old target.  What survives is "
    "sharper and more abstract: a dual-even plus quadratic dual-odd sector, with "
    "a finite metric gauge/family and an additional physical selection principle "
    "still required."
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
