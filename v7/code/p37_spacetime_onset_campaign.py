#!/usr/bin/env python3
"""Paper 37 long campaign: first finite spacetime-onset audit.

This receipt uses the audited permutation-order deletion cylinders and builds a
first crude finite GR-facing packet from record-intrinsic data only:

    relation count, height, width, interval profile, degree moments,
    matching profile, and layer profile.

It then compares click prediction and GR-packet prediction under W-history,
G-history, joint WG-history, and raw deletion-history panels.

The purpose is not to derive the final law.  It is to test the Paper 37 phase
claim on actual finite cylinders:

    click panels can be meaningful before a stable GR/spacetime packet is
    licensed, and the spacetime phase requires a joint non-reconstructive
    panel rather than W alone.

All counts and residuals are exact Fractions.
"""

from __future__ import annotations

from collections import defaultdict
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


sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(160000)

SELECTED_PAIRS = (
    (912, 25104),
    (17288, 525076),
    (24576, 540672),
)
SELECTED_METRIC = (5, 5, 3)

checks: list[tuple[str, bool, str]] = []


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


def layer_profile(bits, n):
    ranks = [1] * n
    for _ in range(n):
        changed = False
        for i in range(n):
            for j in range(n):
                if i != j and has_rel(bits, n, i, j) and ranks[j] < ranks[i] + 1:
                    ranks[j] = ranks[i] + 1
                    changed = True
        if not changed:
            break
    counts = defaultdict(int)
    for r in ranks:
        counts[r] += 1
    return tuple(sorted(counts.items()))


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


def build_features(reps_by_n, n_min, n_max):
    features = {}
    for n in range(n_min, n_max + 1):
        known = {}
        flags5 = {}
        geom = {}
        for key, bits in reps_by_n[n].items():
            masks = comparability_masks(bits, n)
            interval_profile = tuple(interval_counts(bits, n))
            known[key] = (
                relation_count(bits, n),
                height(bits, n),
                fast_width_from_masks(masks, n),
                interval_profile,
                degree_moments(bits, n),
                tuple(matching_counts_from_masks(masks, n)[1:]),
            )
            flags5[key] = fast_flag_counts(bits, n, 5)
            geom[key] = (
                "G",
                n,
                relation_count(bits, n),
                height(bits, n),
                fast_width_from_masks(masks, n),
                interval_profile,
                degree_moments(bits, n),
                tuple(matching_counts_from_masks(masks, n)[1:]),
                layer_profile(bits, n),
            )
        features[n] = {"known": known, "flags5": flags5, "geom": geom}
    return features


def selected_signature(n, key):
    flags = features_by_n[n]["flags5"][key]
    vals = []
    for left, right in SELECTED_PAIRS:
        left_value = flags.get(left, 0)
        right_value = flags.get(right, 0)
        vals.append((left_value + right_value, left_value - right_value))
    even_total = sum(even for even, _odd in vals)
    q_odd = sum(weight * odd * odd for weight, (_even, odd) in zip(SELECTED_METRIC, vals))
    return ("S", n, features_by_n[n]["known"][key], (even_total, q_odd))


def build_ids(n, signature_fn):
    signature_to_id = {}
    record_to_id = {}
    atoms = defaultdict(list)
    for key in reps_by_n[n]:
        signature = signature_fn(n, key)
        sid = signature_to_id.setdefault(signature, len(signature_to_id))
        record_to_id[key] = sid
        atoms[sid].append(key)
    return record_to_id, dict(atoms), len(signature_to_id)


def geom_signature(n, key):
    return features_by_n[n]["geom"][key]


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


def panel_value(kind, child_n, child_key):
    if kind == "W":
        return work_id_by_n[child_n][child_key]
    if kind == "G":
        return geom_id_by_n[child_n][child_key]
    if kind == "WG":
        return (work_id_by_n[child_n][child_key], geom_id_by_n[child_n][child_key])
    if kind == "R":
        return child_key
    raise ValueError(kind)


def history_counts(n, key, depth, kind):
    """Return compressed child histories for one panel kind."""
    if depth == 0:
        return {(): 1}
    cache_key = (kind, n, key, depth)
    if depth <= 4 and cache_key in HISTORY_CACHE:
        return HISTORY_CACHE[cache_key]
    out = defaultdict(int)
    child_n = n - 1
    for child_key, multiplicity in decks_by_n[n][key].items():
        child_panel = panel_value(kind, child_n, child_key)
        for child_history, child_count in history_counts(child_n, child_key, depth - 1, kind).items():
            out[child_history + (child_panel,)] += multiplicity * child_count
    out = dict(out)
    if depth <= 4:
        HISTORY_CACHE[cache_key] = out
    return out


def build_rows(parent_n, depth, modes=("W", "G", "WG", "R"), suffixes=(1, 2, 3, 4)):
    rows = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
    total_weight_by_mode = {}
    for mode in modes:
        total_weight = 0
        for parent_key, fiber_count in counts_by_n[parent_n].items():
            click_target = shadow_id_by_n[parent_n][parent_key]
            geom_target = geom_id_by_n[parent_n][parent_key]
            joint_target = (click_target, geom_target)
            histories = history_counts(parent_n, parent_key, depth, mode)
            for history, path_count in histories.items():
                weight = fiber_count * path_count
                total_weight += weight
                for suffix_len in suffixes:
                    context = tuple(history[-suffix_len:])
                    panel = f"{mode}{suffix_len}"
                    rows[panel]["click"][context][click_target] += weight
                    rows[panel]["geom"][context][geom_target] += weight
                    rows[panel]["joint"][context][joint_target] += weight
        total_weight_by_mode[mode] = total_weight
    expected = math.factorial(parent_n) * math.prod(range(parent_n - depth + 1, parent_n + 1))
    return rows, total_weight_by_mode, expected


def row_total(row):
    return sum(row.values())


def bayes_residual(rows):
    total = sum(row_total(row) for row in rows.values())
    return sum(row_total(row) - max(row.values()) for row in rows.values()) / Fraction(total)


def avg_support(rows):
    total = sum(row_total(row) for row in rows.values())
    return sum(row_total(row) * len(row) for row in rows.values()) / Fraction(total)


def max_support(rows):
    return max(len(row) for row in rows.values())


def complexity(rows, full_rows):
    return Fraction(len(rows), len(full_rows))


def panel_report(rows_by_panel, panel, full_panel):
    click_rows = rows_by_panel[panel]["click"]
    geom_rows = rows_by_panel[panel]["geom"]
    joint_rows = rows_by_panel[panel]["joint"]
    full_rows = rows_by_panel[full_panel]["joint"]
    comp = complexity(joint_rows, full_rows)
    click_res = bayes_residual(click_rows)
    geom_res = bayes_residual(geom_rows)
    joint_res = bayes_residual(joint_rows)
    pre_action = click_res + Fraction(1, 100) * comp
    total_action = click_res + geom_res + Fraction(1, 100) * comp
    return {
        "panel": panel,
        "contexts": len(joint_rows),
        "complexity": comp,
        "click": click_res,
        "geom": geom_res,
        "joint": joint_res,
        "pre_action": pre_action,
        "total_action": total_action,
        "click_support": avg_support(click_rows),
        "geom_support": avg_support(geom_rows),
        "max_click_support": max_support(click_rows),
        "max_geom_support": max_support(geom_rows),
    }


def print_report(parent_n, reports, modes=("W", "G", "WG", "R"), suffixes=(1, 2, 3, 4)):
    print("\n" + "=" * 80)
    print(f"N={parent_n}: panel residuals")
    print("=" * 80)
    order = [f"{m}{d}" for d in suffixes for m in modes]
    for panel in order:
        row = reports[panel]
        print(
            f"  {panel:<4} contexts={row['contexts']:<7} "
            f"comp={fmt_frac(row['complexity'], 12):>16} "
            f"click={fmt_frac(row['click'], 18):>22} "
            f"geom={fmt_frac(row['geom'], 18):>22} "
            f"joint={fmt_frac(row['joint'], 18):>22} "
            f"pre={fmt_frac(row['pre_action'], 18):>22} "
            f"total={fmt_frac(row['total_action'], 18):>22}"
        )


def campaign_for(parent_n, depth=4, modes=("W", "G", "WG", "R"), suffixes=(1, 2, 3, 4)):
    print("\n" + "=" * 80)
    print(f"Building exact N={parent_n} joint click/GR history rows")
    print("=" * 80)
    HISTORY_CACHE.clear()
    rows, total_weight_by_mode, expected = build_rows(parent_n, depth, modes=modes, suffixes=suffixes)
    for mode in modes:
        print(f"  total path weight {mode}={total_weight_by_mode[mode]}")
    print(f"  expected path weight={expected}")
    full_panel = f"R{depth}" if f"R{depth}" in rows else f"{modes[-1]}{max(suffixes)}"
    reports = {
        panel: panel_report(rows, panel, full_panel)
        for panel in rows
    }
    print_report(parent_n, reports, modes=modes, suffixes=suffixes)
    pre_winner = min(reports.values(), key=lambda r: (r["pre_action"], r["complexity"], r["panel"]))
    total_winner = min(reports.values(), key=lambda r: (r["total_action"], r["complexity"], r["panel"]))
    geom_winner = min(reports.values(), key=lambda r: (r["geom"], r["complexity"], r["panel"]))
    print("\n  winners:")
    print(f"    pre-click     {pre_winner['panel']} action={fmt_frac(pre_winner['pre_action'], 24)}")
    print(f"    geom          {geom_winner['panel']} residual={fmt_frac(geom_winner['geom'], 24)}")
    print(f"    click+geom    {total_winner['panel']} action={fmt_frac(total_winner['total_action'], 24)}")
    return rows, reports, total_weight_by_mode, expected, pre_winner, geom_winner, total_winner


print("=" * 80)
print("Paper 37 spacetime-onset finite campaign")
print("=" * 80)

counts_by_n = {}
reps_by_n = {}
for n in range(3, 10):
    counts, reps = universe(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    print(f"  built N={n}: records={len(counts)} permutations={math.factorial(n)}")

decks_by_n, reverse_by_n = build_decks(reps_by_n, 3, 9)
features_by_n = build_features(reps_by_n, 3, 9)

shadow_id_by_n = {}
shadow_atoms_by_n = {}
shadow_count_by_n = {}
geom_id_by_n = {}
geom_atoms_by_n = {}
geom_count_by_n = {}

for n in range(3, 10):
    shadow_ids, shadow_atoms, shadow_count = build_ids(n, selected_signature)
    geom_ids, geom_atoms, geom_count = build_ids(n, geom_signature)
    shadow_id_by_n[n] = shadow_ids
    shadow_atoms_by_n[n] = shadow_atoms
    shadow_count_by_n[n] = shadow_count
    geom_id_by_n[n] = geom_ids
    geom_atoms_by_n[n] = geom_atoms
    geom_count_by_n[n] = geom_count
    print(f"  packet counts N={n}: shadow={shadow_count} geom={geom_count}")

work_id_by_n = {}
work_count_by_n = {}
for n in range(4, 9):
    work_ids, work_count = scalar_work_ids(n)
    work_id_by_n[n] = work_ids
    work_count_by_n[n] = work_count
    print(f"  scalar-work cells N={n}: {work_count}")

rows8, reports8, weight8, expected8, pre8, geom8, total8 = campaign_for(
    8,
    modes=("W", "G", "WG", "R"),
    suffixes=(1, 2, 3, 4),
)
rows9, reports9, weight9, expected9, pre9, geom9, total9 = campaign_for(
    9,
    depth=1,
    modes=("W", "G"),
    suffixes=(1,),
)

print("\n" + "=" * 80)
print("Campaign adversary verdicts")
print("=" * 80)

check(
    "N=8 exact path weight",
    all(value == expected8 for value in weight8.values()),
    f"{weight8}",
)
check(
    "N=9 exact nonreconstructive path weight",
    all(value == expected9 for value in weight9.values()),
    f"{weight9}",
)

check(
    "N=8 W-history is not enough for the first GR packet",
    reports8["W4"]["geom"] > reports8["WG4"]["geom"],
    f"W4_geom={fmt_frac(reports8['W4']['geom'], 24)} WG4_geom={fmt_frac(reports8['WG4']['geom'], 24)}",
)
check(
    "N=9 W-history is not enough for the first GR packet",
    reports9["W1"]["geom"] > reports9["G1"]["geom"],
    f"W1_geom={fmt_frac(reports9['W1']['geom'], 24)} G1_geom={fmt_frac(reports9['G1']['geom'], 24)}",
)
check(
    "N=8 pre-click winner is non-raw/nonreconstructive",
    not pre8["panel"].startswith("R"),
    f"pre_winner={pre8['panel']}",
)
check(
    "N=9 pre-click winner is non-raw/nonreconstructive",
    not pre9["panel"].startswith("R"),
    f"pre_winner={pre9['panel']}",
)
check(
    "N=8 joint action prefers adding GR-facing data over W-only history",
    total8["total_action"] < reports8["W4"]["total_action"],
    f"winner={total8['panel']} W4_total={fmt_frac(reports8['W4']['total_action'], 24)}",
)
check(
    "N=9 joint action prefers adding GR-facing data over W-only history",
    total9["total_action"] < reports9["W1"]["total_action"],
    f"winner={total9['panel']} W1_total={fmt_frac(reports9['W1']['total_action'], 24)}",
)
check(
    "N=8 full raw history is reconstructive and more complex than WG history",
    reports8["R4"]["complexity"] > reports8["WG4"]["complexity"],
    f"R4_comp={fmt_frac(reports8['R4']['complexity'], 18)} WG4_comp={fmt_frac(reports8['WG4']['complexity'], 18)}",
)
check(
    "N=9 exact audit stays in nonreconstructive W/G panels",
    "R1" not in reports9 and "WG1" not in reports9 and "G1" in reports9,
    f"panels={','.join(sorted(reports9))}",
)
check(
    "first GR packet exposes an onset distinction",
    reports8["W4"]["geom"] > 0 and reports9["W1"]["geom"] > 0,
    f"N8={fmt_frac(reports8['W4']['geom'], 18)} N9={fmt_frac(reports9['W1']['geom'], 18)}",
)

print("\n=== Interpretation ===")
print(
    "The first intrinsic GR packet is not carried by scalar-work history alone. "
    "Adding GR-facing order/count/layer data lowers the GR residual at N=8 and "
    "N=9, while raw deletion histories are still more reconstructive.  This "
    "supports the phase-scoped Paper 37 picture: the pre-spacetime click panel "
    "and the spacetime-licensed joint panel need not be identical."
)
print(
    "The receipt does not prove spacetime onset. It proves the next finite "
    "object to study: a non-reconstructive WG/center quotient with an intrinsic "
    "GR packet and a real no-hidden-presentation complexity penalty."
)

failed = False
print("\n" + "=" * 80)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
    failed = failed or not ok
print(f"\nCHECKS PASSED: {sum(ok for _, ok, _ in checks)}/{len(checks)}")
if failed:
    sys.exit(1)
print("DONE.")
