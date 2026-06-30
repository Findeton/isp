#!/usr/bin/env python3
"""
Paper 34 receipt: boundary-work potential campaign.

Target:

    derive psi_{P_N}, the record-intrinsic boundary-work potential whose
    commitment minimizer gives h_{P_N}.

Paper 33 showed that deletion equations, multi-delete, full decks, low-order
features, flags, and commitment alone do not close the click law.  This receipt
attacks the next object directly.

Finite test:

1. Use the selected Paper 30 dual-sector/quadratic shadow at N=6,7,8.
2. Extract the exact atom-average effective h on the N=7 shadow.
3. Try to replace the shadow atom id by smaller boundary-work descriptors:
   metric-only, known-only, deletion drift, insertion drift, and combined drift.
4. Ask whether those descriptors determine h and preserve the exact forward
   h-transform from N=6 to N=7.
5. Re-run the commitment-alone falsifier: without a physical psi, arbitrary
   positive h targets can be made stationary.

All record/deck/TV calculations are exact integer/Fraction arithmetic. Decimal
precision is 140 for logs/roots/reporting.
"""

from collections import defaultdict
from decimal import Decimal, getcontext
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
sys.setrecursionlimit(50000)

ONE = Decimal(1)
TWO = Decimal(2)
TOL = Decimal("1e-110")

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


def tanh(x):
    e2 = (TWO * x).exp()
    return (e2 - ONE) / (e2 + ONE)


def bisect_root(f, lo, hi, steps=480):
    flo = f(lo)
    fhi = f(hi)
    if flo * fhi > 0:
        raise ValueError(f"root not bracketed: {flo}, {fhi}")
    for _ in range(steps):
        mid = (lo + hi) / TWO
        fm = f(mid)
        if flo * fm < 0:
            hi = mid
            fhi = fm
        else:
            lo = mid
            flo = fm
    return (lo + hi) / TWO


def universe(n):
    counts = defaultdict(int)
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        counts[key] += 1
        reps.setdefault(key, bits)
    dist = {key: Fraction(count, math.factorial(n)) for key, count in counts.items()}
    return dict(counts), reps, dist


def delete_deck(bits, n):
    row = defaultdict(int)
    for deleted in range(n):
        subset = tuple(v for v in range(n) if v != deleted)
        child_key = canon_bits(restrict_bits(bits, n, subset), n - 1)
        row[child_key] += 1
    return dict(row)


def build_reverse(reps_by_n, n_min, n_max):
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


def build_features(reps_by_n, n_min, n_max):
    features = {}
    for n in range(n_min, n_max + 1):
        known = {}
        flags5 = {}
        for key, bits in reps_by_n[n].items():
            known[key] = known_tuple(bits, n)
            flags5[key] = fast_flag_counts(bits, n, 5)
        features[n] = {"known": known, "flags5": flags5}
    return features


def selected_parts(n, key):
    flags = features_by_n[n]["flags5"][key]
    vals = []
    for left, right in SELECTED_PAIRS:
        left_value = flags.get(left, 0)
        right_value = flags.get(right, 0)
        vals.append((left_value + right_value, left_value - right_value))
    even_total = sum(even for even, _odd in vals)
    q_odd = sum(weight * odd * odd for weight, (_even, odd) in zip(SELECTED_METRIC, vals))
    known = features_by_n[n]["known"][key]
    return known, (even_total, q_odd), tuple(vals)


def selected_color(n, key):
    known, metric, _vals = selected_parts(n, key)
    return ("selected", known, metric)


def metric_descriptor(n, key):
    _known, metric, _vals = selected_parts(n, key)
    return ("metric", metric)


def known_descriptor(n, key):
    known, _metric, _vals = selected_parts(n, key)
    return ("known", known)


def atoms_from_record_descriptor(keys, descriptor_fn):
    atoms = defaultdict(list)
    for key in keys:
        atoms[descriptor_fn(key)].append(key)
    return atoms


def shadow_atoms(n):
    return atoms_from_record_descriptor(reps_by_n[n], lambda key: selected_color(n, key))


def atom_h_by_shadow(n):
    out = {}
    atoms = shadow_atoms(n)
    for color, keys in atoms.items():
        out[color] = Fraction(sum(counts_by_n[n][key] for key in keys), len(keys))
    return out, atoms


def aggregate_child_profile(n, keys, child_colors):
    row = defaultdict(int)
    for key in keys:
        for child_key, multiplicity in decks_by_n[n][key].items():
            row[child_colors[child_key]] += multiplicity
    return tuple(sorted(row.items()))


def aggregate_parent_profile(n, keys, parent_colors):
    row = defaultdict(int)
    for key in keys:
        for parent_key, multiplicity in reverse_by_n[n].get(key, {}).items():
            row[parent_colors[parent_key]] += multiplicity
    return tuple(sorted(row.items()))


def descriptor_by_shadow_atom(n, mode):
    h_atom, atoms = atom_h_by_shadow(n)
    selected_colors_by_n = {
        level: {key: selected_color(level, key) for key in reps_by_n[level]}
        for level in (n - 1, n, n + 1)
        if level in reps_by_n
    }
    descriptors = {}
    for color, keys in atoms.items():
        representative = keys[0]
        metric = metric_descriptor(n, representative)
        known = known_descriptor(n, representative)
        delete_profile = ()
        insert_profile = ()
        if n - 1 in reps_by_n:
            delete_profile = aggregate_child_profile(n, keys, selected_colors_by_n[n - 1])
        if n + 1 in reps_by_n:
            insert_profile = aggregate_parent_profile(n, keys, selected_colors_by_n[n + 1])
        size = len(keys)
        if mode == "shadow":
            desc = color
        elif mode == "metric":
            desc = metric
        elif mode == "known":
            desc = known
        elif mode == "atom_size":
            desc = ("size", size)
        elif mode == "delete":
            desc = ("delete", delete_profile)
        elif mode == "insert":
            desc = ("insert", insert_profile)
        elif mode == "delete_insert":
            desc = ("delete_insert", delete_profile, insert_profile)
        elif mode == "metric_delete_insert":
            desc = ("metric_delete_insert", metric, delete_profile, insert_profile)
        elif mode == "known_metric_delete_insert":
            desc = ("known_metric_delete_insert", known, metric, delete_profile, insert_profile)
        else:
            raise ValueError(mode)
        descriptors[color] = desc
    return descriptors, h_atom, atoms


def descriptor_stats(n, mode):
    descriptors, h_atom, atoms = descriptor_by_shadow_atom(n, mode)
    desc_to_h = defaultdict(set)
    desc_to_colors = defaultdict(list)
    for color, desc in descriptors.items():
        desc_to_h[desc].add(h_atom[color])
        desc_to_colors[desc].append(color)
    conflicts = sum(1 for values in desc_to_h.values() if len(values) > 1)
    max_h_values = max(len(values) for values in desc_to_h.values())
    max_shadow_atoms = max(len(colors) for colors in desc_to_colors.values())
    return {
        "mode": mode,
        "cells": len(desc_to_h),
        "shadow_atoms": len(h_atom),
        "records": len(reps_by_n[n]),
        "h_conflicts": conflicts,
        "max_h_values": max_h_values,
        "max_shadow_atoms": max_shadow_atoms,
        "descriptors": descriptors,
        "h_atom": h_atom,
        "atoms": atoms,
        "desc_to_colors": desc_to_colors,
    }


def descriptor_weights_on_records(n, mode):
    stats = descriptor_stats(n, mode)
    desc_records = defaultdict(list)
    for color, keys in stats["atoms"].items():
        desc = stats["descriptors"][color]
        desc_records[desc].extend(keys)
    desc_weight = {
        desc: Fraction(sum(counts_by_n[n][key] for key in keys), len(keys))
        for desc, keys in desc_records.items()
    }
    weights = {}
    for color, keys in stats["atoms"].items():
        desc = stats["descriptors"][color]
        for key in keys:
            weights[key] = desc_weight[desc]
    return weights, stats


def total_variation(left, right):
    keys = set(left) | set(right)
    return sum(abs(left.get(key, Fraction(0)) - right.get(key, Fraction(0))) for key in keys) / 2


def forward_step(child_dist, child_n, parent_weights):
    out = defaultdict(Fraction)
    for child_key, child_prob in child_dist.items():
        local = {}
        denom = Fraction(0)
        for parent_key, multiplicity in reverse_by_n[child_n][child_key].items():
            value = parent_weights[parent_key] * multiplicity
            local[parent_key] = value
            denom += value
        for parent_key, value in local.items():
            out[parent_key] += child_prob * value / denom
    return dict(out)


def commitment_root():
    return bisect_root(lambda h: tanh(h) - (-h).exp(), Decimal(0), Decimal(2))


def arbitrary_psi_stationarity(targets):
    residuals = []
    min_curvature = None
    for h in targets:
        # psi'(x) = exp(-h) + (x-h), so psi''(x)=1.
        derivative = (-h).exp() - (-h).exp()
        curvature = ONE
        residuals.append(abs(derivative))
        min_curvature = curvature if min_curvature is None else min(min_curvature, curvature)
    return max(residuals), min_curvature


print("=" * 80)
print("Paper 34 boundary-work potential campaign")
print("=" * 80)
print(f"Decimal precision: prec={getcontext().prec}")

counts_by_n = {}
reps_by_n = {}
exact_by_n = {}
for n in range(5, 9):
    counts, reps, dist = universe(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    exact_by_n[n] = dist
    print(f"  built N={n}: records={len(counts)} permutations={math.factorial(n)}")

decks_by_n, reverse_by_n = build_reverse(reps_by_n, 5, 8)
features_by_n = build_features(reps_by_n, 5, 8)

modes = (
    "metric",
    "known",
    "atom_size",
    "delete",
    "insert",
    "delete_insert",
    "metric_delete_insert",
    "known_metric_delete_insert",
    "shadow",
)


def scan_level(n):
    rows = []
    print(f"\n  Level N={n}, forward {n-1}->{n}")
    for mode in modes:
        weights, stats = descriptor_weights_on_records(n, mode)
        tv = total_variation(forward_step(exact_by_n[n - 1], n - 1, weights), exact_by_n[n])
        row = {**stats, "tv": tv}
        rows.append(row)
        print(
            f"    {mode:<28} cells={stats['cells']:>5}/{stats['shadow_atoms']:<5} "
            f"records={stats['records']:<5} h_conf={stats['h_conflicts']:<4} "
            f"max_h={stats['max_h_values']:<3} max_shadow={stats['max_shadow_atoms']:<3} "
            f"TV={fmt_frac(tv, 24)}"
        )
    return rows


print("\n" + "=" * 80)
print("1. Extract h on selected positive shadow")
print("=" * 80)
rows_by_level = {}
for level in (6, 7):
    shadow_weights, shadow_stats = descriptor_weights_on_records(level, "shadow")
    shadow_tv = total_variation(
        forward_step(exact_by_n[level - 1], level - 1, shadow_weights),
        exact_by_n[level],
    )
    print(
        f"  N={level}: selected shadow atoms={shadow_stats['shadow_atoms']}/"
        f"{len(reps_by_n[level])} TV={fmt_frac(shadow_tv, 30)}"
    )

print("\n" + "=" * 80)
print("2. Boundary-work descriptor scans")
print("=" * 80)
for level in (6, 7):
    rows_by_level[level] = scan_level(level)

print("\n" + "=" * 80)
print("3. Commitment-only falsifier")
print("=" * 80)
h_commit = commitment_root()
commit_residual = tanh(h_commit) - (-h_commit).exp()
targets = (Decimal("0.41"), Decimal("0.83"), Decimal("1.97"))
free_residual, free_curvature = arbitrary_psi_stationarity(targets)
print(f"  h_commit={h_commit}")
print(f"  residual={commit_residual}")
print(f"  arbitrary targets={targets}")
print(f"  arbitrary psi residual={free_residual}, min_curvature={free_curvature}")

rows = rows_by_level[7]
row_by_mode = {row["mode"]: row for row in rows}
row6_by_mode = {row["mode"]: row for row in rows_by_level[6]}
exact_subshadow_modes = [
    row["mode"]
    for row in rows
    if row["tv"] == 0 and row["cells"] < row["shadow_atoms"]
]
nonlookup_exact_modes = [
    row["mode"]
    for row in rows
    if row["tv"] == 0 and row["cells"] < Fraction(9, 10) * row["records"]
]
best_nonshadow = min((row for row in rows if row["mode"] != "shadow"), key=lambda row: row["tv"])
drift_modes = ("delete", "insert", "delete_insert", "metric_delete_insert", "known_metric_delete_insert")
drift_self_identifies_7 = all(
    row_by_mode[mode]["cells"] == row_by_mode["shadow"]["cells"]
    and row_by_mode[mode]["tv"] == 0
    for mode in drift_modes
)
drift_self_identifies_6 = all(
    row6_by_mode[mode]["cells"] == row6_by_mode["shadow"]["cells"]
    and row6_by_mode[mode]["tv"] == 0
    for mode in drift_modes
)

check(
    "selected positive shadow gives exact audited 6->7 h-transform",
    row_by_mode["shadow"]["tv"] == 0 and row_by_mode["shadow"]["cells"] < len(reps_by_n[7]),
    (
        f"atoms={row_by_mode['shadow']['cells']}/{len(reps_by_n[7])}, "
        f"TV={fmt_frac(row_by_mode['shadow']['tv'], 24)}"
    ),
)
check(
    "metric-only boundary descriptor does not determine h",
    row_by_mode["metric"]["h_conflicts"] > 0 and row_by_mode["metric"]["tv"] > 0,
    (
        f"h_conf={row_by_mode['metric']['h_conflicts']} "
        f"TV={fmt_frac(row_by_mode['metric']['tv'], 18)}"
    ),
)
check(
    "deletion drift exactly identifies the selected shadow at N=7",
    row_by_mode["delete"]["cells"] == row_by_mode["shadow"]["cells"]
    and row_by_mode["delete"]["h_conflicts"] == 0
    and row_by_mode["delete"]["tv"] == 0,
    (
        f"cells={row_by_mode['delete']['cells']}/{row_by_mode['shadow']['cells']} "
        f"TV={fmt_frac(row_by_mode['delete']['tv'], 18)}"
    ),
)
check(
    "insertion drift exactly identifies the selected shadow at N=7",
    row_by_mode["insert"]["cells"] == row_by_mode["shadow"]["cells"]
    and row_by_mode["insert"]["h_conflicts"] == 0
    and row_by_mode["insert"]["tv"] == 0,
    (
        f"cells={row_by_mode['insert']['cells']}/{row_by_mode['shadow']['cells']} "
        f"TV={fmt_frac(row_by_mode['insert']['tv'], 18)}"
    ),
)
check(
    "combined drift is not a coarser psi descriptor",
    not exact_subshadow_modes,
    f"exact_subshadow_modes={exact_subshadow_modes}",
)
check(
    "drift self-identifies the shadow at both audited levels",
    drift_self_identifies_6 and drift_self_identifies_7,
    (
        f"N6 shadow_cells={row6_by_mode['shadow']['cells']} "
        f"N7 shadow_cells={row_by_mode['shadow']['cells']}"
    ),
)
check(
    "all exact nonlookup descriptors are shadow-equivalent drift descriptors",
    all(row_by_mode[mode]["cells"] == row_by_mode["shadow"]["cells"] for mode in nonlookup_exact_modes),
    f"exact_nonlookup_modes={nonlookup_exact_modes}",
)
check(
    "commitment fixed point is solved at high precision",
    abs(commit_residual) < TOL and h_commit > 0,
    f"h={h_commit}",
)
check(
    "commitment alone cannot identify psi",
    free_residual < TOL and free_curvature > 0,
    "strictly convex psi can be centered on arbitrary targets",
)

print("\n=== Campaign verdict ===")
print(
    "The boundary-work potential was not derived, but the campaign found a "
    "stronger bridge than expected.  Metric and known descriptors are too "
    "coarse.  Deletion and insertion drift, however, exactly self-identify the "
    "selected shadow at both audited levels while staying nonlookup at the "
    "record level.  Thus psi should probably live on this deletion/insertion "
    "coalgebra of the shadow, not on a smaller scalar boundary-work descriptor. "
    "Commitment supplies the exponential term; the missing theorem is the "
    "record-intrinsic boundary-work functional on that drift-stable shadow."
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
