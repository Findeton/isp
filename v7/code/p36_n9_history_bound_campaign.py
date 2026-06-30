#!/usr/bin/env python3
"""
Paper 36 receipt: exact N=9 history-bound follow-up.

Target:

    Paper 36 found that predicting S8 from the scalar-work panel saturates at
    the suffix W5,W6,W7.  This receipt asks whether that "three-panel" result
    persists one size higher, or whether the least sufficient causal history
    changes at N=9.

The receipt builds the exact deletion-history law

    R_9 -> R_8 -> R_7 -> R_6 -> R_5

under the audited 2D permutation-order measure, projects the children to
scalar-work panels W5,W6,W7,W8, and predicts the parent selected shadow S9.

All probabilities are exact integer/Fraction calculations.  Decimal precision
is set to 140 for reporting only.
"""

from collections import defaultdict
from decimal import getcontext
from fractions import Fraction
from itertools import combinations
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
sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(100000)

SELECTED_PAIRS = (
    (912, 25104),
    (17288, 525076),
    (24576, 540672),
)
SELECTED_METRIC = (5, 5, 3)

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def universe(n):
    counts = defaultdict(int)
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        counts[key] += 1
        reps.setdefault(key, bits)
    return dict(counts), reps


def delete_deck(bits, n):
    row = defaultdict(int)
    for deleted in range(n):
        subset = tuple(v for v in range(n) if v != deleted)
        child_key = canon_bits(restrict_bits(bits, n, subset), n - 1)
        row[child_key] += 1
    return dict(row)


def build_decks(reps_by_n, n_min, n_max):
    decks = {}
    reverse = {}
    for n in range(n_min + 1, n_max + 1):
        rows = defaultdict(dict)
        decks[n] = {}
        for key, bits in reps_by_n[n].items():
            deck = delete_deck(bits, n)
            decks[n][key] = deck
            for child_key, multiplicity in deck.items():
                rows[child_key][key] = multiplicity
        reverse[n - 1] = dict(rows)
    return decks, reverse


RAW_TO_CANON_CACHE = {}
SUBSET_PAIR_CACHE = {}


def raw_to_canon(k):
    if k not in RAW_TO_CANON_CACHE:
        RAW_TO_CANON_CACHE[k] = {
            permutation_order_bits(pi): canon_bits(permutation_order_bits(pi), k)
            for pi in perms(k)
        }
    return RAW_TO_CANON_CACHE[k]


def subset_pair_maps(n, k):
    maps = []
    for subset in combinations(range(n), k):
        pairs = []
        for a, old_a in enumerate(subset):
            for b, old_b in enumerate(subset):
                if a != b:
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
        size = bin(mask).count("1")
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
    return (
        relation_count(bits, n),
        height(bits, n),
        fast_width_from_masks(masks, n),
        tuple(interval_counts(bits, n)),
        degree_moments(bits, n),
        tuple(matching_counts_from_masks(masks, n)[1:]),
    )


def selected_signature(n, key):
    bits = reps_by_n[n][key]
    flags = fast_flag_counts(bits, n, 5)
    vals = []
    for left, right in SELECTED_PAIRS:
        left_value = flags.get(left, 0)
        right_value = flags.get(right, 0)
        vals.append((left_value + right_value, left_value - right_value))
    even_total = sum(even for even, _odd in vals)
    q_odd = sum(weight * odd * odd for weight, (_even, odd) in zip(SELECTED_METRIC, vals))
    return ("S", n, known_tuple(bits, n), (even_total, q_odd))


def build_shadow_ids(n):
    signature_to_id = {}
    record_to_shadow = {}
    shadow_atoms = defaultdict(list)
    for key in reps_by_n[n]:
        signature = selected_signature(n, key)
        sid = signature_to_id.setdefault(signature, len(signature_to_id))
        record_to_shadow[key] = sid
        shadow_atoms[sid].append(key)
    return record_to_shadow, dict(shadow_atoms), len(signature_to_id)


def aggregate_delete_profile(n, keys):
    row = defaultdict(int)
    for key in keys:
        for child_key, multiplicity in decks_by_n[n][key].items():
            row[shadow_id_by_n[n - 1][child_key]] += multiplicity
    return tuple(sorted(row.items()))


def aggregate_insert_profile(n, keys):
    row = defaultdict(int)
    for key in keys:
        for parent_key, multiplicity in reverse_by_n[n].get(key, {}).items():
            row[shadow_id_by_n[n + 1][parent_key]] += multiplicity
    return tuple(sorted(row.items()))


def scalar_work_ids(n):
    signature_to_id = {}
    record_to_work = {}
    for sid, keys in shadow_atoms_by_n[n].items():
        representative = keys[0]
        signature = selected_signature(n, representative)
        metric = signature[-1]
        delete_profile = aggregate_delete_profile(n, keys)
        insert_profile = aggregate_insert_profile(n, keys)
        delete_scalar = (
            len(delete_profile),
            sum(count for _child, count in delete_profile),
            sum(count * count for _child, count in delete_profile),
        )
        insert_scalar = (
            len(insert_profile),
            sum(count for _parent, count in insert_profile),
            sum(count * count for _parent, count in insert_profile),
        )
        work_signature = ("W", n, metric, len(keys), delete_scalar, insert_scalar)
        wid = signature_to_id.setdefault(work_signature, len(signature_to_id))
        for key in keys:
            record_to_work[key] = wid
    return record_to_work, len(signature_to_id)


HISTORY_CACHE = {}


def history_counts(n, key, depth):
    if depth == 0:
        return {(): 1}
    cache_key = (n, key, depth)
    if depth <= 3 and cache_key in HISTORY_CACHE:
        return HISTORY_CACHE[cache_key]
    out = defaultdict(int)
    child_n = n - 1
    for child_key, multiplicity in decks_by_n[n][key].items():
        child_work = work_id_by_n[child_n][child_key]
        for child_history, child_count in history_counts(child_n, child_key, depth - 1).items():
            out[child_history + (child_work,)] += multiplicity * child_count
    out = dict(out)
    if depth <= 3:
        HISTORY_CACHE[cache_key] = out
    return out


def add_row(rows, context, target, weight):
    rows[context][target] += weight


def build_context_rows():
    specs = {
        "W8": (3,),
        "W7,W8": (2, 3),
        "W6,W7,W8": (1, 2, 3),
        "W5,W6,W7,W8": (0, 1, 2, 3),
    }
    rows_by_name = {name: defaultdict(lambda: defaultdict(int)) for name in specs}
    total_weight = 0
    total_paths = math.prod(range(6, 10))
    for parent_key, fiber_count in counts_by_n[9].items():
        target = shadow_id_by_n[9][parent_key]
        histories = history_counts(9, parent_key, 4)
        for history, path_count in histories.items():
            weight = fiber_count * path_count
            total_weight += weight
            for name, indices in specs.items():
                context = tuple(history[i] for i in indices)
                add_row(rows_by_name[name], context, target, weight)
    expected_total = math.factorial(9) * total_paths
    return specs, rows_by_name, total_weight, expected_total


def row_total(row):
    return sum(row.values())


def tv_rows(left, right):
    left_total = row_total(left)
    right_total = row_total(right)
    keys = set(left) | set(right)
    return sum(
        abs(Fraction(left.get(key, 0), left_total) - Fraction(right.get(key, 0), right_total))
        for key in keys
    ) / 2


def same_distribution(left, right):
    left_total = row_total(left)
    right_total = row_total(right)
    if set(left) != set(right):
        return False
    return all(left[key] * right_total == right[key] * left_total for key in left)


def sufficiency_report(full_rows, full_to_coarse):
    representative = {}
    total_cells = set()
    conflict_cells = set()
    full_contexts = 0
    for full_context, full_row in full_rows.items():
        full_contexts += 1
        coarse_context = full_to_coarse(full_context)
        total_cells.add(coarse_context)
        previous = representative.setdefault(coarse_context, full_row)
        if previous is not full_row and not same_distribution(previous, full_row):
            conflict_cells.add(coarse_context)
    return {
        "sufficient": len(conflict_cells) == 0,
        "coarse_cells": len(total_cells),
        "conflict_cells": len(conflict_cells),
        "full_contexts": full_contexts,
    }


def bayes_residual(rows):
    total = sum(row_total(row) for row in rows.values())
    return sum(row_total(row) - max(row.values()) for row in rows.values()) / Fraction(total)


def avg_support(rows):
    total = sum(row_total(row) for row in rows.values())
    return sum(row_total(row) * len(row) for row in rows.values()) / Fraction(total)


def max_support(rows):
    return max(len(row) for row in rows.values())


def tower_count_error(fine_rows, coarse_rows, fine_to_coarse):
    grouped = defaultdict(lambda: defaultdict(int))
    for fine_context, row in fine_rows.items():
        coarse_context = fine_to_coarse(fine_context)
        for target, count in row.items():
            grouped[coarse_context][target] += count
    mismatches = 0
    for coarse_context, row in coarse_rows.items():
        if dict(row) != dict(grouped[coarse_context]):
            mismatches += 1
    return mismatches


def suffix_mapper(full_indices, coarse_indices):
    def mapper(full_context):
        return tuple(full_context[full_indices.index(idx)] for idx in coarse_indices)

    return mapper


print("=" * 80)
print("Paper 36 exact N=9 history-bound follow-up")
print("=" * 80)
print(f"Decimal precision: prec={getcontext().prec}")

counts_by_n = {}
reps_by_n = {}
for n in range(4, 10):
    counts, reps = universe(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    print(f"  built N={n}: records={len(counts)} permutations={math.factorial(n)}")

decks_by_n, reverse_by_n = build_decks(reps_by_n, 4, 9)

shadow_id_by_n = {}
shadow_atoms_by_n = {}
shadow_count_by_n = {}
for n in range(4, 10):
    record_to_shadow, shadow_atoms, shadow_count = build_shadow_ids(n)
    shadow_id_by_n[n] = record_to_shadow
    shadow_atoms_by_n[n] = shadow_atoms
    shadow_count_by_n[n] = shadow_count
    print(f"  shadow atoms N={n}: {shadow_count}")

work_id_by_n = {}
work_count_by_n = {}
for n in range(5, 9):
    record_to_work, work_count = scalar_work_ids(n)
    work_id_by_n[n] = record_to_work
    work_count_by_n[n] = work_count
    print(f"  scalar-work cells N={n}: {work_count}")

print("\n" + "=" * 80)
print("1. Exact N=9 history cylinder")
print("=" * 80)
specs, rows_by_name, total_weight, expected_total = build_context_rows()
print(f"  cached child history states={len(HISTORY_CACHE)}")
print(f"  total path weight={total_weight}")
print(f"  expected path weight={expected_total}")

full_name = "W5,W6,W7,W8"
full_rows = rows_by_name[full_name]
sufficiency_rows = {}
for name, indices in specs.items():
    mapper = suffix_mapper(specs[full_name], indices)
    sufficiency_rows[name] = sufficiency_report(full_rows, mapper)

print("\n" + "=" * 80)
print("2. N=9 history-bound sufficiency")
print("=" * 80)
for name in ("W8", "W7,W8", "W6,W7,W8", "W5,W6,W7,W8"):
    rows = rows_by_name[name]
    report = sufficiency_rows[name]
    print(
        f"  suffix {name:<12} contexts={len(rows):<7} "
        f"exact={str(report['sufficient']):<5} "
        f"conflict_cells={report['conflict_cells']:<7} "
        f"avg_support={fmt_frac(avg_support(rows), 18):>22} "
        f"max_support={max_support(rows):<6} "
        f"bayes_residual={fmt_frac(bayes_residual(rows), 30)}"
    )

shortest_exact = next(
    name
    for name in ("W8", "W7,W8", "W6,W7,W8", "W5,W6,W7,W8")
    if sufficiency_rows[name]["sufficient"]
)

print("\n" + "=" * 80)
print("3. Calibration/tower checks")
print("=" * 80)
tower_4_to_3 = tower_count_error(
    rows_by_name["W5,W6,W7,W8"],
    rows_by_name["W6,W7,W8"],
    suffix_mapper(specs["W5,W6,W7,W8"], specs["W6,W7,W8"]),
)
tower_3_to_2 = tower_count_error(
    rows_by_name["W6,W7,W8"],
    rows_by_name["W7,W8"],
    suffix_mapper(specs["W6,W7,W8"], specs["W7,W8"]),
)
tower_2_to_1 = tower_count_error(
    rows_by_name["W7,W8"],
    rows_by_name["W8"],
    suffix_mapper(specs["W7,W8"], specs["W8"]),
)
print(f"  tower count mismatches W5..W8 -> W6..W8 = {tower_4_to_3}")
print(f"  tower count mismatches W6..W8 -> W7,W8  = {tower_3_to_2}")
print(f"  tower count mismatches W7,W8 -> W8      = {tower_2_to_1}")

print("\n" + "=" * 80)
print("4. N=10 feasibility boundary")
print("=" * 80)
print(
    "  exact N=10 brute force would start from 10! = "
    f"{math.factorial(10)} hidden presentations before canonical aggregation."
)
print(
    "  The exact N=9 result is therefore the last safe brute-force audit in this "
    "receipt style; N=10 needs dynamic generation, sampling, or a theorem."
)

check(
    "N=9 exact path cylinder has expected total weight",
    total_weight == expected_total,
    f"weight={total_weight}",
)
check(
    "N=9 current W8 alone is not sufficient",
    not sufficiency_rows["W8"]["sufficient"],
    f"conflicts={sufficiency_rows['W8']['conflict_cells']}",
)
check(
    "N=9 two-panel suffix is not sufficient",
    not sufficiency_rows["W7,W8"]["sufficient"],
    f"conflicts={sufficiency_rows['W7,W8']['conflict_cells']}",
)
check(
    "N=9 three-panel suffix is tested explicitly",
    "W6,W7,W8" in sufficiency_rows,
    (
        f"exact={sufficiency_rows['W6,W7,W8']['sufficient']} "
        f"conflicts={sufficiency_rows['W6,W7,W8']['conflict_cells']}"
    ),
)
check(
    "N=9 least exact suffix is identified",
    shortest_exact in {"W6,W7,W8", "W5,W6,W7,W8"},
    f"shortest_exact={shortest_exact}",
)
check(
    "N=9 calibrated residual kernels obey tower identities",
    tower_4_to_3 == 0 and tower_3_to_2 == 0 and tower_2_to_1 == 0,
    f"tower_mismatches=({tower_4_to_3}, {tower_3_to_2}, {tower_2_to_1})",
)
check(
    "N=10 is beyond this brute-force campaign style",
    math.factorial(10) > math.factorial(9),
    f"9!={math.factorial(9)} 10!={math.factorial(10)}",
)

print("\n=== Campaign verdict ===")
if shortest_exact == "W6,W7,W8":
    print(
        "The three-panel finite sufficiency pattern survives one exact size higher: "
        "W6,W7,W8 is already sufficient for S9 relative to W5..W8."
    )
else:
    print(
        "The three-panel pattern fails one exact size higher: S9 needs the longer "
        "W5,W6,W7,W8 suffix in this audited scalar-work projection."
    )
print(
    "Either way, the law cannot be 'always three' without proof.  The object to "
    "derive is the controlled memory-range function m_N(P,S), with N=10 requiring "
    "a non-brute-force method."
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
