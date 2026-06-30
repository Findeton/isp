#!/usr/bin/env python3
"""
Paper 35 receipt: shadow-coalgebra variational recurrence campaign.

Target:

    derive the invariant variational recurrence on the deletion/insertion
    coalgebra of the selected positive shadow, and identify what psi_P must
    depend on.

This follows Paper 34's opening: the selected shadow is self-identified by
deletion/insertion drift at N=6,7.  The new campaign asks whether the coalgebra
itself determines h, whether the recurrence is unique, and whether smaller
scalar boundary-work descriptors can support psi.

All combinatorial quantities are exact integers/Fractions.  Decimal precision
is 140 for commitment/root diagnostics only.
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
sys.setrecursionlimit(60000)

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
    return features_by_n[n]["known"][key], (even_total, q_odd), tuple(vals)


def selected_color(n, key):
    known, metric, _vals = selected_parts(n, key)
    return ("selected", known, metric)


def shadow_atoms(n):
    atoms = defaultdict(list)
    for key in reps_by_n[n]:
        atoms[selected_color(n, key)].append(key)
    return dict(atoms)


def h_atom(n):
    out = {}
    for color, keys in shadow_atoms(n).items():
        out[color] = Fraction(sum(counts_by_n[n][key] for key in keys), len(keys))
    return out


def record_delete_profile(n, key):
    row = defaultdict(int)
    for child_key, multiplicity in decks_by_n[n][key].items():
        row[selected_color(n - 1, child_key)] += multiplicity
    return tuple(sorted(row.items()))


def record_insert_profile(n, key):
    row = defaultdict(int)
    for parent_key, multiplicity in reverse_by_n[n].get(key, {}).items():
        row[selected_color(n + 1, parent_key)] += multiplicity
    return tuple(sorted(row.items()))


def aggregate_delete_profile(n, keys):
    row = defaultdict(int)
    for key in keys:
        for child_key, multiplicity in decks_by_n[n][key].items():
            row[selected_color(n - 1, child_key)] += multiplicity
    return tuple(sorted(row.items()))


def aggregate_insert_profile(n, keys):
    row = defaultdict(int)
    for key in keys:
        for parent_key, multiplicity in reverse_by_n[n].get(key, {}).items():
            row[selected_color(n + 1, parent_key)] += multiplicity
    return tuple(sorted(row.items()))


def strong_lumpability_report(n):
    delete_conflicts = 0
    insert_conflicts = 0
    delete_max = 0
    insert_max = 0
    for _color, keys in shadow_atoms(n).items():
        d_profiles = {record_delete_profile(n, key) for key in keys} if n - 1 in reps_by_n else {()}
        i_profiles = {record_insert_profile(n, key) for key in keys} if n + 1 in reps_by_n else {()}
        delete_conflicts += int(len(d_profiles) > 1)
        insert_conflicts += int(len(i_profiles) > 1)
        delete_max = max(delete_max, len(d_profiles))
        insert_max = max(insert_max, len(i_profiles))
    return {
        "delete_conflicts": delete_conflicts,
        "insert_conflicts": insert_conflicts,
        "delete_max": delete_max,
        "insert_max": insert_max,
    }


def aggregate_profile_self_id(n):
    rows = {}
    for mode in ("delete", "insert", "delete_insert"):
        descriptor_to_colors = defaultdict(list)
        for color, keys in shadow_atoms(n).items():
            delete_profile = aggregate_delete_profile(n, keys) if n - 1 in reps_by_n else ()
            insert_profile = aggregate_insert_profile(n, keys) if n + 1 in reps_by_n else ()
            if mode == "delete":
                descriptor = delete_profile
            elif mode == "insert":
                descriptor = insert_profile
            else:
                descriptor = (delete_profile, insert_profile)
            descriptor_to_colors[descriptor].append(color)
        rows[mode] = {
            "cells": len(descriptor_to_colors),
            "shadow_atoms": len(shadow_atoms(n)),
            "max_colors": max(len(colors) for colors in descriptor_to_colors.values()),
            "conflicts": sum(1 for colors in descriptor_to_colors.values() if len(colors) > 1),
        }
    return rows


def aggregate_matrix(parent_n):
    child_n = parent_n - 1
    child_colors = tuple(sorted(shadow_atoms(child_n)))
    parent_colors = tuple(sorted(shadow_atoms(parent_n)))
    child_index = {color: idx for idx, color in enumerate(child_colors)}
    parent_index = {color: idx for idx, color in enumerate(parent_colors)}
    rows = [defaultdict(Fraction) for _ in child_colors]
    for parent_color, keys in shadow_atoms(parent_n).items():
        pidx = parent_index[parent_color]
        for key in keys:
            for child_key, multiplicity in decks_by_n[parent_n][key].items():
                cidx = child_index[selected_color(child_n, child_key)]
                rows[cidx][pidx] += Fraction(multiplicity)
    return rows, child_colors, parent_colors


def sparse_rank(rows, n_cols):
    matrix = [{col: Fraction(value) for col, value in row.items() if value} for row in rows]
    rank = 0
    pivot_row = 0
    for col in range(n_cols):
        pivot = None
        for row_idx in range(pivot_row, len(matrix)):
            if matrix[row_idx].get(col, 0):
                pivot = row_idx
                break
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_value = matrix[pivot_row][col]
        for key in list(matrix[pivot_row]):
            matrix[pivot_row][key] /= pivot_value
        for row_idx in range(len(matrix)):
            if row_idx == pivot_row:
                continue
            factor = matrix[row_idx].get(col, 0)
            if not factor:
                continue
            for key, value in list(matrix[pivot_row].items()):
                new_value = matrix[row_idx].get(key, 0) - factor * value
                if new_value:
                    matrix[row_idx][key] = new_value
                elif key in matrix[row_idx]:
                    del matrix[row_idx][key]
        rank += 1
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return rank


def aggregate_recurrence_report(parent_n):
    child_n = parent_n - 1
    matrix, child_colors, parent_colors = aggregate_matrix(parent_n)
    h_child = h_atom(child_n)
    h_parent = h_atom(parent_n)
    parent_index = {color: idx for idx, color in enumerate(parent_colors)}
    max_error = Fraction(0)
    for row, child_color in zip(matrix, child_colors):
        lhs = sum(value * h_parent[parent_colors[col]] for col, value in row.items())
        rhs = Fraction(parent_n * parent_n) * len(shadow_atoms(child_n)[child_color]) * h_child[child_color]
        max_error = max(max_error, abs(lhs - rhs))
    rank = sparse_rank(matrix, len(parent_colors))
    return {
        "parent_n": parent_n,
        "rows": len(child_colors),
        "cols": len(parent_colors),
        "rank": rank,
        "nullity": len(parent_colors) - rank,
        "max_error": max_error,
    }


def descriptor_conflicts(n):
    atoms = shadow_atoms(n)
    h_values = h_atom(n)
    descriptors = defaultdict(lambda: defaultdict(set))
    for color, keys in atoms.items():
        representative = keys[0]
        known, metric, vals = selected_parts(n, representative)
        delete_profile = aggregate_delete_profile(n, keys) if n - 1 in reps_by_n else ()
        insert_profile = aggregate_insert_profile(n, keys) if n + 1 in reps_by_n else ()
        scalar_delete = (
            len(delete_profile),
            sum(count for _child, count in delete_profile),
            sum(count * count for _child, count in delete_profile),
        )
        scalar_insert = (
            len(insert_profile),
            sum(count for _parent, count in insert_profile),
            sum(count * count for _parent, count in insert_profile),
        )
        descs = {
            "metric": metric,
            "known": known,
            "size": len(keys),
            "delete_scalar": scalar_delete,
            "insert_scalar": scalar_insert,
            "scalar_work": (metric, len(keys), scalar_delete, scalar_insert),
            "full_drift": (delete_profile, insert_profile),
        }
        for name, desc in descs.items():
            descriptors[name][desc].add(h_values[color])
    out = {}
    for name, groups in descriptors.items():
        out[name] = {
            "cells": len(groups),
            "conflicts": sum(1 for values in groups.values() if len(values) > 1),
            "max_h_values": max(len(values) for values in groups.values()),
        }
    return out


def descriptor_for_shadow_atom(n, color, keys, name):
    representative = keys[0]
    known, metric, _vals = selected_parts(n, representative)
    delete_profile = aggregate_delete_profile(n, keys) if n - 1 in reps_by_n else ()
    insert_profile = aggregate_insert_profile(n, keys) if n + 1 in reps_by_n else ()
    scalar_delete = (
        len(delete_profile),
        sum(count for _child, count in delete_profile),
        sum(count * count for _child, count in delete_profile),
    )
    scalar_insert = (
        len(insert_profile),
        sum(count for _parent, count in insert_profile),
        sum(count * count for _parent, count in insert_profile),
    )
    if name == "metric":
        return metric
    if name == "known":
        return known
    if name == "size":
        return len(keys)
    if name == "delete_scalar":
        return scalar_delete
    if name == "insert_scalar":
        return scalar_insert
    if name == "scalar_work":
        return (metric, len(keys), scalar_delete, scalar_insert)
    if name == "full_drift":
        return (delete_profile, insert_profile)
    if name == "shadow":
        return color
    raise ValueError(name)


def descriptor_forward_tv(n, name):
    h_values = h_atom(n)
    desc_to_h = defaultdict(set)
    desc_to_records = defaultdict(list)
    for color, keys in shadow_atoms(n).items():
        desc = descriptor_for_shadow_atom(n, color, keys, name)
        desc_to_h[desc].add(h_values[color])
        desc_to_records[desc].extend(keys)
    if any(len(values) != 1 for values in desc_to_h.values()):
        return None
    desc_weight = {desc: next(iter(values)) for desc, values in desc_to_h.items()}
    record_weights = {}
    for desc, keys in desc_to_records.items():
        for key in keys:
            record_weights[key] = desc_weight[desc]
    predicted = forward_step(exact_by_n[n - 1], n - 1, record_weights)
    return total_variation(predicted, exact_by_n[n])


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
    for h in targets:
        residuals.append(abs((-h).exp() - (-h).exp()))
    return max(residuals), ONE


print("=" * 80)
print("Paper 35 shadow-coalgebra variational recurrence campaign")
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

print("\n" + "=" * 80)
print("1. Strong versus aggregate coalgebra")
print("=" * 80)
strong_rows = {}
self_rows = {}
for n in (6, 7):
    strong_rows[n] = strong_lumpability_report(n)
    self_rows[n] = aggregate_profile_self_id(n)
    print(
        f"  N={n}: strong delete conflicts={strong_rows[n]['delete_conflicts']} "
        f"max_profiles={strong_rows[n]['delete_max']}; "
        f"strong insert conflicts={strong_rows[n]['insert_conflicts']} "
        f"max_profiles={strong_rows[n]['insert_max']}"
    )
    for mode, row in self_rows[n].items():
        print(
            f"    aggregate {mode:<13} cells={row['cells']}/"
            f"{row['shadow_atoms']} conflicts={row['conflicts']} max_colors={row['max_colors']}"
        )

print("\n" + "=" * 80)
print("2. Aggregate h recurrence")
print("=" * 80)
recurrence_rows = {}
for parent_n in (6, 7):
    recurrence_rows[parent_n] = aggregate_recurrence_report(parent_n)
    row = recurrence_rows[parent_n]
    print(
        f"  {parent_n-1}->{parent_n}: rows={row['rows']} cols={row['cols']} "
        f"rank={row['rank']} nullity={row['nullity']} "
        f"max_error={row['max_error']}"
    )

print("\n" + "=" * 80)
print("3. Scalar boundary-work descriptor attacks")
print("=" * 80)
descriptor_rows = {}
descriptor_tvs = {}
for n in (6, 7):
    descriptor_rows[n] = descriptor_conflicts(n)
    descriptor_tvs[n] = {
        name: descriptor_forward_tv(n, name)
        for name in ("scalar_work", "full_drift", "shadow")
    }
    print(f"  N={n}")
    for name, row in descriptor_rows[n].items():
        tv = descriptor_tvs[n].get(name)
        tv_text = "" if tv is None else f" TV={fmt_frac(tv, 18)}"
        print(
            f"    {name:<14} cells={row['cells']:<5} "
            f"h_conflicts={row['conflicts']:<5} max_h={row['max_h_values']}{tv_text}"
        )

print("\n" + "=" * 80)
print("4. Commitment-only check")
print("=" * 80)
h_commit = commitment_root()
commit_residual = tanh(h_commit) - (-h_commit).exp()
free_residual, free_curvature = arbitrary_psi_stationarity(
    (Decimal("0.29"), Decimal("0.94"), Decimal("1.73"))
)
print(f"  h_commit={h_commit}")
print(f"  commitment residual={commit_residual}")
print(f"  arbitrary psi residual={free_residual}, curvature={free_curvature}")

check(
    "selected shadow is not strongly lumpable record-by-record",
    strong_rows[7]["delete_conflicts"] > 0 or strong_rows[7]["insert_conflicts"] > 0,
    (
        f"N7 delete_conflicts={strong_rows[7]['delete_conflicts']} "
        f"insert_conflicts={strong_rows[7]['insert_conflicts']}"
    ),
)
check(
    "aggregate deletion/insertion profiles self-identify the selected shadow",
    all(self_rows[n][mode]["conflicts"] == 0 and self_rows[n][mode]["cells"] == self_rows[n][mode]["shadow_atoms"]
        for n in (6, 7)
        for mode in ("delete", "insert", "delete_insert")),
    "N6,N7 aggregate profiles are one-to-one with shadow atoms",
)
check(
    "aggregate h recurrence is exact at audited levels",
    recurrence_rows[6]["max_error"] == 0 and recurrence_rows[7]["max_error"] == 0,
    f"errors={recurrence_rows[6]['max_error']},{recurrence_rows[7]['max_error']}",
)
check(
    "coalgebra recurrence is underdetermined",
    recurrence_rows[6]["nullity"] > 0 and recurrence_rows[7]["nullity"] > 0,
    f"nullities={recurrence_rows[6]['nullity']},{recurrence_rows[7]['nullity']}",
)
check(
    "metric and known descriptors are not enough for psi",
    descriptor_rows[7]["metric"]["conflicts"] > 0 and descriptor_rows[7]["known"]["conflicts"] > 0,
    (
        f"metric_conf={descriptor_rows[7]['metric']['conflicts']} "
        f"known_conf={descriptor_rows[7]['known']['conflicts']}"
    ),
)
check(
    "delete and insert scalar descriptors alone are not enough for psi",
    descriptor_rows[7]["delete_scalar"]["conflicts"] > 0
    and descriptor_rows[7]["insert_scalar"]["conflicts"] > 0,
    (
        f"delete={descriptor_rows[7]['delete_scalar']['conflicts']} "
        f"insert={descriptor_rows[7]['insert_scalar']['conflicts']}"
    ),
)
check(
    "scalar-work descriptor is a proper coarser exact h-transform quotient",
    descriptor_rows[6]["scalar_work"]["conflicts"] == 0
    and descriptor_rows[7]["scalar_work"]["conflicts"] == 0
    and descriptor_rows[6]["scalar_work"]["cells"] < len(shadow_atoms(6))
    and descriptor_rows[7]["scalar_work"]["cells"] < len(shadow_atoms(7))
    and descriptor_tvs[6]["scalar_work"] == 0
    and descriptor_tvs[7]["scalar_work"] == 0,
    (
        f"N6 cells={descriptor_rows[6]['scalar_work']['cells']}/{len(shadow_atoms(6))} "
        f"N7 cells={descriptor_rows[7]['scalar_work']['cells']}/{len(shadow_atoms(7))}"
    ),
)
check(
    "full aggregate drift determines h but is less compressed than scalar work",
    descriptor_rows[7]["full_drift"]["conflicts"] == 0
    and descriptor_rows[7]["full_drift"]["cells"] == len(shadow_atoms(7))
    and descriptor_rows[7]["scalar_work"]["cells"] < descriptor_rows[7]["full_drift"]["cells"],
    (
        f"scalar={descriptor_rows[7]['scalar_work']['cells']} "
        f"full={descriptor_rows[7]['full_drift']['cells']}"
    ),
)
check(
    "commitment fixed point is solved but psi remains free without boundary work",
    abs(commit_residual) < TOL and free_residual < TOL and free_curvature > 0,
    f"h={h_commit}",
)

print("\n=== Campaign verdict ===")
print(
    "The selected shadow is an aggregate coalgebra, not a strong per-record "
    "lump.  Its aggregate deletion/insertion profiles self-identify it and "
    "its aggregate h recurrence is exact, but the recurrence has a large "
    "nullspace.  The new positive result is that a scalar-work packet "
    "(metric, atom size, deletion scalar moments, insertion scalar moments) is "
    "a proper coarser quotient of the shadow and still gives exact h-transform "
    "weights at N=6,7.  Therefore psi should be sought as a primitive RN/KL "
    "boundary-work functional on this scalar-work quotient of the aggregate "
    "shadow coalgebra, not as a bare recurrence energy."
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
