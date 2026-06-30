#!/usr/bin/env python3
"""
Paper 30 receipt: harmonic quotient campaign.

This is the next campaign after the effective-weight audit.  It tests the
reframing:

    the click law is the minimal admissible record-intrinsic h-transform of
    the deletion graph.

The exact hidden h-function in the 2D audited model is pres(R), the number of
permutation presentations projecting to committed record R.  For a
record-intrinsic filtration P_N, we use the exact conditional/atom-average
approximation

    h_P(R) = E[pres(R) | P_N](R).

The first campaign block runs six attacks:

1. harmonic theorem target: exact and quotient recurrence errors;
2. recurrence-defect generator: greedy sectors selected from 7->8;
3. admissibility: nonlookup, unresolved pairs, and residue;
4. lumpability: deletion/insertion profile conflicts;
5. blind prediction: use 7->8 selected sectors to predict N=9;
6. incidence framing: exact oracle identity and quotient defect.

It then runs an admissibility-functional scan plus six parallel hostile attacks:
minimax, MDL, cross-level stability, dual-orbit closure, Pareto/KKT support,
and directional deletion/insertion drift.  The strongest opening, dual closure,
is followed immediately by a direct dual-orbit recurrence generator.

All combinatorial quantities and probabilities are exact integers/Fractions.
Decimal reporting uses the Paper 29 helper.
"""

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


HINGE = (912, 664)
RESIDUAL = (912, 664, 525184, 25360, 924)
FLAG5_KEYS = all_flag_keys(5)


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


def colors_for_sectors(n, sectors=(), include_known=True, full_type=False, constant=False):
    if constant:
        return {key: ("constant",) for key in reps_by_n[n]}
    if full_type:
        return {key: ("type", key) for key in reps_by_n[n]}
    colors = {}
    for key in reps_by_n[n]:
        base = feature_cache[n]["known"][key] if include_known else ()
        flags = feature_cache[n]["flags5"][key]
        colors[key] = ("sectors", base, tuple(flags.get(sector, 0) for sector in sectors))
    return colors


def all_flag_profile_colors(n, k):
    flag_keys = all_flag_keys(k)
    colors = {}
    for key, bits in reps_by_n[n].items():
        counts = fast_flag_counts(bits, n, k)
        colors[key] = tuple(counts.get(flag_key, 0) for flag_key in flag_keys)
    return colors


def atom_weights(colors, counts):
    atom_counts = defaultdict(int)
    atom_sizes = defaultdict(int)
    for key, color in colors.items():
        atom_counts[color] += counts[key]
        atom_sizes[color] += 1
    return {
        key: Fraction(atom_counts[color], atom_sizes[color])
        for key, color in colors.items()
    }


def atom_metrics(colors, counts):
    atoms = defaultdict(list)
    for key, color in colors.items():
        atoms[color].append(key)
    record_total = len(colors)
    pair_total = record_total * (record_total - 1) // 2
    unresolved_pairs = sum(len(keys) * (len(keys) - 1) // 2 for keys in atoms.values())
    singleton_atoms = sum(1 for keys in atoms.values() if len(keys) == 1)
    max_atom = max(len(keys) for keys in atoms.values())
    residue = within_atom_presentation_residue(colors, counts)
    return {
        "atoms": len(atoms),
        "lookup": len(atoms) == record_total,
        "singletons": singleton_atoms,
        "max_atom": max_atom,
        "unresolved_pair_fraction": Fraction(unresolved_pairs, pair_total) if pair_total else Fraction(0),
        "residue": residue,
    }


def within_atom_presentation_residue(colors, counts):
    atoms = defaultdict(list)
    atom_count = defaultdict(int)
    for key, color in colors.items():
        atoms[color].append(key)
        atom_count[color] += counts[key]
    total = sum(counts.values())
    residue = Fraction(0)
    for color, keys in atoms.items():
        mean = Fraction(atom_count[color], len(keys))
        for key in keys:
            residue += abs(Fraction(counts[key]) - mean)
    return residue / total


def recurrence_errors(parent_n, parent_colors, child_colors):
    child_n = parent_n - 1
    parent_h = atom_weights(parent_colors, counts_by_n[parent_n])
    child_h = atom_weights(child_colors, counts_by_n[child_n])
    exact_error = Fraction(0)
    quotient_error = Fraction(0)
    total_child = math.factorial(child_n)
    for child_key, child_count in counts_by_n[child_n].items():
        z = Fraction(0)
        for parent_key, multiplicity in reverse[child_n][child_key].items():
            z += parent_h[parent_key] * multiplicity
        target_exact = Fraction(child_count * parent_n * parent_n)
        target_quotient = child_h[child_key] * parent_n * parent_n
        exact_error += Fraction(child_count, total_child) * abs(z - target_exact) / target_exact
        quotient_error += Fraction(child_count, total_child) * abs(z - target_quotient) / target_quotient
    return exact_error, quotient_error


def profile_conflicts(colors, profiles):
    groups = defaultdict(lambda: defaultdict(int))
    for key, color in colors.items():
        groups[color][profiles[key]] += 1
    bad = 0
    pairs = 0
    for profile_counts in groups.values():
        if len(profile_counts) <= 1:
            continue
        bad += 1
        total = sum(profile_counts.values())
        same = sum(count * (count - 1) // 2 for count in profile_counts.values())
        pairs += total * (total - 1) // 2 - same
    return bad, pairs


def deletion_conflicts(n, parent_colors, child_colors):
    profiles = {}
    for key, bits in reps_by_n[n].items():
        row = defaultdict(int)
        for child_key, multiplicity in decks[n][key].items():
            row[child_colors[child_key]] += multiplicity
        profiles[key] = tuple(sorted(row.items()))
    return profile_conflicts(parent_colors, profiles)


def insertion_conflicts(n, child_colors, parent_colors):
    profiles = {}
    for key in reps_by_n[n]:
        row = defaultdict(int)
        for parent_key, multiplicity in reverse[n].get(key, {}).items():
            row[parent_colors[parent_key]] += multiplicity
        profiles[key] = tuple(sorted(row.items()))
    return profile_conflicts(child_colors, profiles)


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


def forward_tv_n9(sectors=(), include_known=True, full_type=False, constant=False):
    weights_by_n = {}
    for n in range(1, 10):
        colors = colors_for_sectors(
            n, sectors=sectors, include_known=include_known, full_type=full_type, constant=constant
        )
        weights_by_n[n] = atom_weights(colors, counts_by_n[n])
    dist = exact_by_n[1]
    for n in range(1, 9):
        dist = forward_step(dist, n, weights_by_n)
    return total_variation(dist, exact_by_n[9])


def greedy_sector_generator(parent_n, base_sectors=(), rounds=5):
    selected = list(base_sectors)
    history = []
    for _round in range(rounds):
        best = None
        child_n = parent_n - 1
        for sector in FLAG5_KEYS:
            if sector in selected:
                continue
            trial = tuple(selected + [sector])
            parent_colors = colors_for_sectors(parent_n, sectors=trial)
            child_colors = colors_for_sectors(child_n, sectors=trial)
            exact_error, quotient_error = recurrence_errors(parent_n, parent_colors, child_colors)
            row = (exact_error, quotient_error, sector, trial)
            if best is None or row < best:
                best = row
        selected = list(best[3])
        history.append(best)
        print(
            f"  greedy round {len(history)}: add flag5_{best[2]} "
            f"exact_error={fmt_frac(best[0], 24)} quotient_error={fmt_frac(best[1], 24)}"
        )
        if best[0] == 0 and best[1] == 0:
            print("  stopping: exact training recurrence defect is zero")
            break
    return tuple(selected), history


def top_single_sectors(parent_n, base_sectors=(), limit=12):
    rows = []
    child_n = parent_n - 1
    for sector in FLAG5_KEYS:
        if sector in base_sectors:
            continue
        trial = tuple(base_sectors + (sector,))
        parent_colors = colors_for_sectors(parent_n, sectors=trial)
        child_colors = colors_for_sectors(child_n, sectors=trial)
        exact_error, quotient_error = recurrence_errors(parent_n, parent_colors, child_colors)
        rows.append((exact_error, quotient_error, sector))
    rows.sort()
    for exact_error, quotient_error, sector in rows[:limit]:
        print(
            f"  flag5_{sector:<7} exact_error={fmt_frac(exact_error, 24)} "
            f"quotient_error={fmt_frac(quotient_error, 24)}"
        )
    return rows


def exact_preimage_failures():
    failures = []
    for child_n in range(1, 9):
        parent_n = child_n + 1
        for child_key, child_count in counts_by_n[child_n].items():
            z = 0
            for parent_key, multiplicity in reverse[child_n][child_key].items():
                z += counts_by_n[parent_n][parent_key] * multiplicity
            target = child_count * parent_n * parent_n
            if z != target:
                failures.append((child_n, child_key, z, target))
    return failures


def cover_edges(bits, n=5):
    covers = []
    for i in range(n):
        for j in range(n):
            if i == j or not has_rel(bits, n, i, j):
                continue
            if not any(
                k != i and k != j and has_rel(bits, n, i, k) and has_rel(bits, n, k, j)
                for k in range(n)
            ):
                covers.append((i, j))
    return covers


def sector_descriptor(sector):
    bits = sector
    n = 5
    covers = cover_edges(bits, n)
    profiles = []
    for v in range(n):
        lower = sum(1 for u in range(n) if has_rel(bits, n, u, v))
        upper = sum(1 for u in range(n) if has_rel(bits, n, v, u))
        incomparable = n - 1 - lower - upper
        profiles.append((lower, upper, incomparable))
    masks = comparability_masks(bits, n)
    return {
        "rel": relation_count(bits, n),
        "height": height(bits, n),
        "width": fast_width_from_masks(masks, n),
        "covers": len(covers),
        "profiles": tuple(sorted(profiles)),
    }


COMPONENT_CACHE = {}


def pair_total(n):
    records = len(reps_by_n[n])
    return records * (records - 1) // 2


def drift_norm(parent_n, parent_colors, child_colors):
    child_n = parent_n - 1
    d_bad, d_pairs = deletion_conflicts(parent_n, parent_colors, child_colors)
    i_bad, i_pairs = insertion_conflicts(child_n, child_colors, parent_colors)
    denom_parent = pair_total(parent_n)
    denom_child = pair_total(child_n)
    value = Fraction(d_pairs, denom_parent) + Fraction(i_pairs, denom_child)
    return {
        "value": value,
        "d_bad": d_bad,
        "d_pairs": d_pairs,
        "i_bad": i_bad,
        "i_pairs": i_pairs,
    }


def quotient_components(parent_n, sectors):
    sectors = tuple(sectors)
    cache_key = (parent_n, sectors)
    if cache_key in COMPONENT_CACHE:
        return COMPONENT_CACHE[cache_key]
    child_n = parent_n - 1
    parent_colors = colors_for_sectors(parent_n, sectors=sectors)
    child_colors = colors_for_sectors(child_n, sectors=sectors)
    exact_rec, quotient_rec = recurrence_errors(parent_n, parent_colors, child_colors)
    drift = drift_norm(parent_n, parent_colors, child_colors)
    metrics = atom_metrics(parent_colors, counts_by_n[parent_n])
    comp = {
        "exact_rec": exact_rec,
        "quotient_rec": quotient_rec,
        "drift": drift["value"],
        "d_pairs": drift["d_pairs"],
        "i_pairs": drift["i_pairs"],
        "density": metrics["residue"],
        "resolution": Fraction(metrics["atoms"], len(reps_by_n[parent_n])),
        "atoms": metrics["atoms"],
        "lookup": metrics["lookup"],
        "max_atom": metrics["max_atom"],
    }
    COMPONENT_CACHE[cache_key] = comp
    return comp


def normalized_score(comp, base, weights):
    if comp["lookup"]:
        return Fraction(10**12)
    total = Fraction(0)
    for key, weight in weights.items():
        if weight == 0:
            continue
        denom = base[key]
        if denom == 0:
            continue
        total += Fraction(weight) * comp[key] / denom
    return total


def greedy_admissibility(parent_n, weights, max_rounds=5):
    selected = ()
    base = quotient_components(parent_n, ())
    current = base
    current_score = normalized_score(current, base, weights)
    history = []
    for _round in range(max_rounds):
        best = None
        for sector in FLAG5_KEYS:
            if sector in selected:
                continue
            trial = tuple(selected + (sector,))
            comp = quotient_components(parent_n, trial)
            score = normalized_score(comp, base, weights)
            row = (score, comp["exact_rec"], comp["drift"], comp["density"], comp["resolution"], sector, trial, comp)
            if best is None or row < best:
                best = row
        if best is None or best[0] >= current_score:
            break
        selected = best[6]
        current = best[7]
        current_score = best[0]
        history.append(best)
    return selected, current, current_score, history


def heldout_report(sectors):
    comp9 = quotient_components(9, tuple(sectors))
    tv9 = forward_tv_n9(sectors=tuple(sectors))
    metrics9 = atom_metrics(colors_for_sectors(9, sectors=tuple(sectors)), counts_by_n[9])
    return {
        "tv9": tv9,
        "comp9": comp9,
        "metrics9": metrics9,
    }


def forward_tv(target_n, sectors=(), include_known=True, full_type=False, constant=False):
    weights_by_n = {}
    for n in range(1, target_n + 1):
        colors = colors_for_sectors(
            n,
            sectors=tuple(sectors),
            include_known=include_known,
            full_type=full_type,
            constant=constant,
        )
        weights_by_n[n] = atom_weights(colors, counts_by_n[n])
    dist = exact_by_n[1]
    for n in range(1, target_n):
        dist = forward_step(dist, n, weights_by_n)
    return total_variation(dist, exact_by_n[target_n])


def normalized_components(parent_n, sectors, base):
    comp = quotient_components(parent_n, tuple(sectors))
    def ratio(key):
        return comp[key] / base[key] if base[key] else Fraction(0)

    return {
        "exact_rec": ratio("exact_rec"),
        "drift": ratio("drift"),
        "density": ratio("density"),
        "resolution": comp["resolution"],
        "d_pairs": Fraction(comp["d_pairs"], base["d_pairs"]) if base["d_pairs"] else Fraction(0),
        "i_pairs": Fraction(comp["i_pairs"], base["i_pairs"]) if base["i_pairs"] else Fraction(0),
        "raw": comp,
    }


def greedy_custom(parent_n, score_fn, max_rounds=5):
    selected = ()
    current = quotient_components(parent_n, selected)
    current_score = score_fn(selected, current)
    history = []
    for _round in range(max_rounds):
        best = None
        for sector in FLAG5_KEYS:
            if sector in selected:
                continue
            trial = tuple(selected + (sector,))
            comp = quotient_components(parent_n, trial)
            score = score_fn(trial, comp)
            row = (score, comp["exact_rec"], comp["drift"], comp["density"], comp["resolution"], sector, trial, comp)
            if best is None or row < best:
                best = row
        if best is None or best[0] >= current_score:
            break
        selected = best[6]
        current = best[7]
        current_score = best[0]
        history.append(best)
    return selected, current, current_score, history


def opposite_bits(bits, n):
    out = 0
    for i in range(n):
        for j in range(n):
            if i != j and has_rel(bits, n, i, j):
                out |= 1 << bit_index(n, j, i)
    return out


def dual_sector(sector):
    return canon_bits(opposite_bits(sector, 5), 5)


def dual_closure(sectors):
    out = set(sectors)
    for sector in sectors:
        out.add(dual_sector(sector))
    return tuple(sorted(out))


def jaccard(left, right):
    left = set(left)
    right = set(right)
    if not left and not right:
        return Fraction(1)
    return Fraction(len(left & right), len(left | right))


def dual_orbits():
    seen = set()
    orbits = []
    for sector in FLAG5_KEYS:
        if sector in seen:
            continue
        orbit = tuple(sorted({sector, dual_sector(sector)}))
        seen.update(orbit)
        orbits.append(orbit)
    return tuple(orbits)


def greedy_dual_orbit_generator(parent_n, max_rounds=5):
    orbits = dual_orbits()
    selected = ()
    current = quotient_components(parent_n, selected)
    current_score = (current["exact_rec"], current["quotient_rec"], current["drift"], current["density"])
    history = []
    for _round in range(max_rounds):
        best = None
        for orbit in orbits:
            if set(orbit) <= set(selected):
                continue
            trial = tuple(sorted(set(selected) | set(orbit)))
            comp = quotient_components(parent_n, trial)
            row = (
                comp["exact_rec"],
                comp["quotient_rec"],
                comp["drift"],
                comp["density"],
                len(trial),
                orbit,
                trial,
                comp,
            )
            if best is None or row < best:
                best = row
        if best is None or best[:4] >= current_score:
            break
        selected = best[6]
        current = best[7]
        current_score = best[:4]
        history.append(best)
        if current["exact_rec"] == 0 and current["quotient_rec"] == 0:
            break
    return selected, current, history


def pareto_front(rows, objective_keys):
    front = []
    for row in rows:
        dominated = False
        for other in rows:
            if other is row:
                continue
            if all(other[key] <= row[key] for key in objective_keys) and any(
                other[key] < row[key] for key in objective_keys
            ):
                dominated = True
                break
        if not dominated:
            front.append(row)
    return front


print("=" * 80)
print("Paper 30 harmonic quotient campaign")
print("=" * 80)
print("exact integer/Fraction arithmetic; no floating arithmetic in checks")

n_min = 1
n_max = 9
counts_by_n = {}
reps_by_n = {}
exact_by_n = {}

print("\n" + "=" * 80)
print("Exact record universes")
print("=" * 80)
for n in range(n_min, n_max + 1):
    counts, reps, dist = build_record_universe(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    exact_by_n[n] = dist

print("\n" + "=" * 80)
print("Deletion graph")
print("=" * 80)
decks, reverse = build_decks_and_reverse(reps_by_n, n_min, n_max)

print("\n" + "=" * 80)
print("Feature cache")
print("=" * 80)
feature_cache = build_feature_cache(reps_by_n, n_min, n_max)

MODEL_SECTORS = {
    "constant": (),
    "known": (),
    "hinge": HINGE,
    "residual": RESIDUAL,
}

model_colors = {
    "constant": {n: colors_for_sectors(n, constant=True) for n in range(1, 10)},
    "known": {n: colors_for_sectors(n, sectors=()) for n in range(1, 10)},
    "hinge": {n: colors_for_sectors(n, sectors=HINGE) for n in range(1, 10)},
    "residual": {n: colors_for_sectors(n, sectors=RESIDUAL) for n in range(1, 10)},
    "all5": {n: colors_for_sectors(n, sectors=FLAG5_KEYS) for n in range(1, 10)},
    "oracle": {n: colors_for_sectors(n, full_type=True) for n in range(1, 10)},
}

print("\n" + "=" * 80)
print("1. Harmonic theorem target")
print("=" * 80)
recurrence_rows = {}
for name in ["constant", "known", "hinge", "residual", "all5", "oracle"]:
    exact_error, quotient_error = recurrence_errors(
        9, model_colors[name][9], model_colors[name][8]
    )
    recurrence_rows[name] = (exact_error, quotient_error)
    print(
        f"  {name:<9} exact_error={fmt_frac(exact_error, 24):>28} "
        f"quotient_error={fmt_frac(quotient_error, 24):>28}"
    )

print("\n" + "=" * 80)
print("2. Recurrence-defect generator")
print("=" * 80)
print("Top one-sector recurrence repairs from known sectors, trained on 7->8:")
top_n8 = top_single_sectors(8, base_sectors=(), limit=12)
generated_sectors, generator_history = greedy_sector_generator(8, base_sectors=(), rounds=5)
print(f"  generated_from_7_to_8={generated_sectors}")
print("  generated sector descriptors:")
for sector in generated_sectors:
    desc = sector_descriptor(sector)
    print(
        f"    flag5_{sector:<7} rel={desc['rel']} h={desc['height']} "
        f"w={desc['width']} covers={desc['covers']} profiles={desc['profiles']}"
    )
generated_tv9 = forward_tv_n9(sectors=generated_sectors)
known_tv9 = forward_tv_n9(sectors=())
hinge_tv9 = forward_tv_n9(sectors=HINGE)
residual_tv9 = forward_tv_n9(sectors=RESIDUAL)
print(f"  TV_N9 known              = {fmt_frac(known_tv9, 24)}")
print(f"  TV_N9 generated blind    = {fmt_frac(generated_tv9, 24)}")
print(f"  TV_N9 hinge              = {fmt_frac(hinge_tv9, 24)}")
print(f"  TV_N9 residual-active    = {fmt_frac(residual_tv9, 24)}")

model_colors["generated"] = {
    n: colors_for_sectors(n, sectors=generated_sectors) for n in range(1, 10)
}
generated_recurrence = recurrence_errors(9, model_colors["generated"][9], model_colors["generated"][8])
recurrence_rows["generated"] = generated_recurrence
print(
    f"  generated 8->9 exact_error={fmt_frac(generated_recurrence[0], 24)} "
    f"quotient_error={fmt_frac(generated_recurrence[1], 24)}"
)

print("\n" + "=" * 80)
print("3. Admissibility metrics")
print("=" * 80)
admissibility = {}
for name in ["constant", "known", "hinge", "residual", "generated", "all5", "oracle"]:
    metrics = atom_metrics(model_colors[name][9], counts_by_n[9])
    admissibility[name] = metrics
    print(
        f"  {name:<9} atoms={metrics['atoms']:<7} lookup={metrics['lookup']:<5} "
        f"max_atom={metrics['max_atom']:<7} "
        f"unresolved_pair_fraction={fmt_frac(metrics['unresolved_pair_fraction'], 18):>22} "
        f"density_residue={fmt_frac(metrics['residue'], 24):>28}"
    )

print("\n" + "=" * 80)
print("4. Approximate lumpability")
print("=" * 80)
lumpability = {}
for name in ["known", "hinge", "residual", "generated", "all5"]:
    d_bad, d_pairs = deletion_conflicts(9, model_colors[name][9], model_colors[name][8])
    i_bad, i_pairs = insertion_conflicts(8, model_colors[name][8], model_colors[name][9])
    lumpability[name] = (d_bad, d_pairs, i_bad, i_pairs)
    print(
        f"  {name:<9} D9_bad={d_bad:<7} D9_pairs={d_pairs:<8} "
        f"I8_bad={i_bad:<7} I8_pairs={i_pairs:<8}"
    )

print("\n" + "=" * 80)
print("5. Blind prediction and reconstruction threshold")
print("=" * 80)
flag_threshold = {}
for k in (3, 4, 5):
    colors = all_flag_profile_colors(9, k)
    metrics = atom_metrics(colors, counts_by_n[9])
    flag_threshold[k] = metrics
    print(
        f"  all flag{k} profile: atoms={metrics['atoms']:<7} "
        f"lookup={metrics['lookup']} max_atom={metrics['max_atom']}"
    )
generated_metrics = atom_metrics(colors_for_sectors(9, sectors=generated_sectors), counts_by_n[9])
print(
    f"  generated blind sectors atoms_N9={generated_metrics['atoms']} "
    f"lookup={generated_metrics['lookup']} max_atom={generated_metrics['max_atom']}"
)

print("\n" + "=" * 80)
print("6. Incidence identity and quotient defect")
print("=" * 80)
identity_failures = exact_preimage_failures()
print(f"  exact oracle preimage failures={len(identity_failures)}")
print(
    "  quotient defect is measured by exact_error and quotient_error above; "
    "all5/oracle vanish because they are lookup/oracle, not because they are "
    "admissible physical laws."
)

print("\n" + "=" * 80)
print("7. Admissibility functional scan")
print("=" * 80)
weight_grid = {
    "rec_only": {"exact_rec": 1, "drift": 0, "density": 0, "resolution": 0},
    "rec_density": {"exact_rec": 1, "drift": 0, "density": 1, "resolution": 0},
    "rec_drift": {"exact_rec": 1, "drift": 1, "density": 0, "resolution": 0},
    "rec_recon": {"exact_rec": 1, "drift": 0, "density": 0, "resolution": 1},
    "balanced": {"exact_rec": 1, "drift": 1, "density": 1, "resolution": 1},
    "drift_heavy": {"exact_rec": 1, "drift": 4, "density": 1, "resolution": 1},
    "density_heavy": {"exact_rec": 1, "drift": 1, "density": 4, "resolution": 1},
    "recon_heavy": {"exact_rec": 1, "drift": 1, "density": 1, "resolution": 4},
}
functional_rows = []
for label, weights in weight_grid.items():
    sectors, train_comp, train_score, history = greedy_admissibility(8, weights, max_rounds=5)
    heldout = heldout_report(sectors)
    row = {
        "label": label,
        "sectors": sectors,
        "train_exact_rec": train_comp["exact_rec"],
        "train_drift": train_comp["drift"],
        "train_density": train_comp["density"],
        "train_resolution": train_comp["resolution"],
        "score": train_score,
        "tv9": heldout["tv9"],
        "exact_rec9": heldout["comp9"]["exact_rec"],
        "drift9": heldout["comp9"]["drift"],
        "density9": heldout["comp9"]["density"],
        "resolution9": heldout["comp9"]["resolution"],
        "lookup9": heldout["metrics9"]["lookup"],
        "atoms9": heldout["metrics9"]["atoms"],
        "history": history,
    }
    functional_rows.append(row)
    print(f"\n  regime={label} weights={weights}")
    if history:
        for idx, step in enumerate(history, start=1):
            sector = step[5]
            comp = step[7]
            print(
                f"    step {idx}: add flag5_{sector:<7} "
                f"train_rec={fmt_frac(comp['exact_rec'], 18)} "
                f"train_drift={fmt_frac(comp['drift'], 18)} "
                f"train_density={fmt_frac(comp['density'], 18)} "
                f"train_resolution={fmt_frac(comp['resolution'], 18)}"
            )
    else:
        print("    no improving nonlookup sector")
    print(
        f"    selected={sectors} atoms9={row['atoms9']} lookup9={row['lookup9']} "
        f"TV9={fmt_frac(row['tv9'], 24)} rec9={fmt_frac(row['exact_rec9'], 24)} "
        f"drift9={fmt_frac(row['drift9'], 24)} density9={fmt_frac(row['density9'], 24)}"
    )

baseline_rows = []
for label, sectors in [
    ("known", ()),
    ("hinge", HINGE),
    ("residual", RESIDUAL),
    ("generated", generated_sectors),
]:
    heldout = heldout_report(sectors)
    baseline_rows.append(
        {
            "label": label,
            "sectors": tuple(sectors),
            "tv9": heldout["tv9"],
            "exact_rec9": heldout["comp9"]["exact_rec"],
            "drift9": heldout["comp9"]["drift"],
            "density9": heldout["comp9"]["density"],
            "resolution9": heldout["comp9"]["resolution"],
            "lookup9": heldout["metrics9"]["lookup"],
            "atoms9": heldout["metrics9"]["atoms"],
        }
    )

all_rows = []
seen = set()
for row in functional_rows + baseline_rows:
    key = row["sectors"]
    if key in seen:
        continue
    seen.add(key)
    all_rows.append(row)

front = pareto_front(
    [row for row in all_rows if not row["lookup9"]],
    ("tv9", "exact_rec9", "drift9", "density9", "resolution9"),
)
front.sort(key=lambda row: (row["tv9"], row["exact_rec9"], row["drift9"]))
print("\n  held-out nonlookup Pareto front:")
for row in front:
    print(
        f"    {row['label']:<14} sectors={row['sectors']} atoms9={row['atoms9']} "
        f"TV9={fmt_frac(row['tv9'], 18)} rec9={fmt_frac(row['exact_rec9'], 18)} "
        f"drift9={fmt_frac(row['drift9'], 18)} density9={fmt_frac(row['density9'], 18)} "
        f"resolution9={fmt_frac(row['resolution9'], 18)}"
    )

best_tv_row = min((row for row in all_rows if not row["lookup9"]), key=lambda row: row["tv9"])
best_drift_row = min((row for row in all_rows if not row["lookup9"]), key=lambda row: row["drift9"])
best_balanced_rows = [row for row in functional_rows if row["label"] == "balanced"]
best_balanced = best_balanced_rows[0]

print("\n" + "=" * 80)
print("8. Six parallel attacks on the admissibility principle")
print("=" * 80)

print("\n8.1 Minimax robustness attack")
base8 = quotient_components(8, ())


def minimax_score(sectors, comp):
    if comp["lookup"]:
        return Fraction(10**12)
    norms = normalized_components(8, sectors, base8)
    return max(norms["exact_rec"], norms["drift"], norms["density"], norms["resolution"])


minimax_sectors, minimax_comp, minimax_score_value, minimax_history = greedy_custom(
    8, minimax_score, max_rounds=5
)
minimax_heldout = heldout_report(minimax_sectors)
print(f"  minimax_sectors={minimax_sectors}")
for idx, step in enumerate(minimax_history, start=1):
    print(
        f"    step {idx}: add flag5_{step[5]} train_score={fmt_frac(step[0], 18)} "
        f"train_rec={fmt_frac(step[7]['exact_rec'], 18)} train_drift={fmt_frac(step[7]['drift'], 18)}"
    )
print(
    f"  heldout TV9={fmt_frac(minimax_heldout['tv9'], 24)} "
    f"rec9={fmt_frac(minimax_heldout['comp9']['exact_rec'], 24)} "
    f"drift9={fmt_frac(minimax_heldout['comp9']['drift'], 24)} "
    f"atoms9={minimax_heldout['metrics9']['atoms']} lookup={minimax_heldout['metrics9']['lookup']}"
)

print("\n8.2 MDL/complexity attack")
mdl_rows = []
for alpha in (Fraction(0), Fraction(1, 16), Fraction(1, 4), Fraction(1), Fraction(4)):
    def mdl_score(sectors, comp, alpha=alpha):
        if comp["lookup"]:
            return Fraction(10**12)
        norms = normalized_components(8, sectors, base8)
        complexity = comp["resolution"] + Fraction(len(sectors), len(FLAG5_KEYS))
        return norms["exact_rec"] + norms["drift"] + norms["density"] + alpha * complexity

    sectors, comp, score_value, history = greedy_custom(8, mdl_score, max_rounds=5)
    heldout = heldout_report(sectors)
    row = {
        "alpha": alpha,
        "sectors": sectors,
        "history": history,
        "tv9": heldout["tv9"],
        "rec9": heldout["comp9"]["exact_rec"],
        "drift9": heldout["comp9"]["drift"],
        "density9": heldout["comp9"]["density"],
        "atoms9": heldout["metrics9"]["atoms"],
        "lookup9": heldout["metrics9"]["lookup"],
    }
    mdl_rows.append(row)
    print(
        f"  alpha={fmt_frac(alpha, 8):>10} sectors={sectors} atoms9={row['atoms9']} "
        f"TV9={fmt_frac(row['tv9'], 18)} rec9={fmt_frac(row['rec9'], 18)} "
        f"drift9={fmt_frac(row['drift9'], 18)}"
    )

print("\n8.3 Cross-level stability attack")
stability_rows = []
stability_regimes = {
    "rec_only": {"exact_rec": 1, "drift": 0, "density": 0, "resolution": 0},
    "balanced": {"exact_rec": 1, "drift": 1, "density": 1, "resolution": 1},
    "drift_heavy": {"exact_rec": 1, "drift": 4, "density": 1, "resolution": 1},
}
for label, weights in stability_regimes.items():
    sectors7, _comp7, _score7, _hist7 = greedy_admissibility(7, weights, max_rounds=5)
    sectors8, _comp8, _score8, _hist8 = greedy_admissibility(8, weights, max_rounds=5)
    tv8 = forward_tv(8, sectors=sectors7)
    tv9 = forward_tv(9, sectors=sectors8)
    row = {
        "label": label,
        "sectors7": sectors7,
        "sectors8": sectors8,
        "jaccard": jaccard(sectors7, sectors8),
        "tv8": tv8,
        "tv9": tv9,
    }
    stability_rows.append(row)
    print(
        f"  {label:<12} sectors6to7={sectors7} sectors7to8={sectors8} "
        f"jaccard={fmt_frac(row['jaccard'], 8)} TV8={fmt_frac(tv8, 18)} TV9={fmt_frac(tv9, 18)}"
    )

print("\n8.4 Dual-orbit closure attack")
dual_rows = []
for label, sectors in [
    ("generated", generated_sectors),
    ("residual", RESIDUAL),
    ("best_drift", best_drift_row["sectors"]),
    ("balanced", best_balanced["sectors"]),
]:
    closed = dual_closure(sectors)
    heldout = heldout_report(closed)
    row = {
        "label": label,
        "sectors": sectors,
        "closed": closed,
        "tv9": heldout["tv9"],
        "rec9": heldout["comp9"]["exact_rec"],
        "drift9": heldout["comp9"]["drift"],
        "density9": heldout["comp9"]["density"],
        "atoms9": heldout["metrics9"]["atoms"],
        "lookup9": heldout["metrics9"]["lookup"],
    }
    dual_rows.append(row)
    print(
        f"  {label:<10} sectors={sectors} dual_closed={closed} atoms9={row['atoms9']} "
        f"lookup={row['lookup9']} TV9={fmt_frac(row['tv9'], 18)} drift9={fmt_frac(row['drift9'], 18)}"
    )

print("\n8.4b Dual-orbit recurrence-generator follow-up")
orbit_generated_sectors, orbit_generated_train, orbit_generated_history = greedy_dual_orbit_generator(
    8, max_rounds=5
)
orbit_generated_heldout = heldout_report(orbit_generated_sectors)
generated_dual_row = next(row for row in dual_rows if row["label"] == "generated")
print(f"  orbit_generated_sectors={orbit_generated_sectors}")
if orbit_generated_history:
    for idx, step in enumerate(orbit_generated_history, start=1):
        orbit = step[5]
        trial = step[6]
        comp = step[7]
        print(
            f"    step {idx}: add_orbit={orbit} sectors={trial} "
            f"train_rec={fmt_frac(comp['exact_rec'], 18)} "
            f"train_quotient={fmt_frac(comp['quotient_rec'], 18)} "
            f"train_drift={fmt_frac(comp['drift'], 18)} "
            f"train_density={fmt_frac(comp['density'], 18)}"
        )
else:
    print("    no improving dual orbit")
print(
    f"  heldout atoms9={orbit_generated_heldout['metrics9']['atoms']} "
    f"lookup={orbit_generated_heldout['metrics9']['lookup']} "
    f"TV9={fmt_frac(orbit_generated_heldout['tv9'], 24)} "
    f"rec9={fmt_frac(orbit_generated_heldout['comp9']['exact_rec'], 24)} "
    f"drift9={fmt_frac(orbit_generated_heldout['comp9']['drift'], 24)} "
    f"density9={fmt_frac(orbit_generated_heldout['comp9']['density'], 24)}"
)
print(
    f"  posthoc_generated_dual_closure atoms9={generated_dual_row['atoms9']} "
    f"lookup={generated_dual_row['lookup9']} TV9={fmt_frac(generated_dual_row['tv9'], 24)} "
    f"rec9={fmt_frac(generated_dual_row['rec9'], 24)} "
    f"drift9={fmt_frac(generated_dual_row['drift9'], 24)} "
    f"density9={fmt_frac(generated_dual_row['density9'], 24)}"
)

print("\n8.5 Pareto/KKT support attack")
support_counts = defaultdict(int)
support_examples = {}
support_values = (0, 1, 2, 4, 8)
known_front_base = {
    "tv9": known_tv9,
    "exact_rec9": quotient_components(9, ())["exact_rec"],
    "drift9": quotient_components(9, ())["drift"],
    "density9": quotient_components(9, ())["density"],
}
for wr in support_values:
    for wc in support_values:
        for wd in support_values:
            for wden in support_values:
                if wr == wc == wd == wden == 0:
                    continue
                best = None
                for row in front:
                    score = Fraction(0)
                    if wr:
                        score += wr * row["tv9"] / known_front_base["tv9"]
                    if wc:
                        score += wc * row["exact_rec9"] / known_front_base["exact_rec9"]
                    if wd:
                        score += wd * row["drift9"] / known_front_base["drift9"]
                    if wden:
                        score += wden * row["density9"] / known_front_base["density9"]
                    # mild penalty for high resolution; absolute because resolution is already [0,1]
                    score += row["resolution9"]
                    item = (score, row["label"], row)
                    if best is None or item < best:
                        best = item
                support_counts[best[1]] += 1
                support_examples.setdefault(best[1], (wr, wc, wd, wden, best[0], best[2]))
for label, count in sorted(support_counts.items(), key=lambda x: (-x[1], x[0])):
    wr, wc, wd, wden, score, row = support_examples[label]
    print(
        f"  supported {label:<14} count={count:<4} example_weights=(tv={wr},rec={wc},drift={wd},density={wden}) "
        f"sectors={row['sectors']}"
    )

print("\n8.6 Directional deletion/insertion drift attack")
directional_rows = []
directional_specs = {
    "D_only": ("d_pairs",),
    "I_only": ("i_pairs",),
    "D_plus_I": ("d_pairs", "i_pairs"),
}
for label, keys in directional_specs.items():
    def directional_score(sectors, comp, keys=keys):
        if comp["lookup"]:
            return Fraction(10**12)
        norms = normalized_components(8, sectors, base8)
        score = norms["exact_rec"]
        for key in keys:
            score += norms[key]
        return score

    sectors, comp, score_value, history = greedy_custom(8, directional_score, max_rounds=5)
    heldout = heldout_report(sectors)
    row = {
        "label": label,
        "sectors": sectors,
        "tv9": heldout["tv9"],
        "rec9": heldout["comp9"]["exact_rec"],
        "d_pairs9": heldout["comp9"]["d_pairs"],
        "i_pairs9": heldout["comp9"]["i_pairs"],
        "drift9": heldout["comp9"]["drift"],
        "atoms9": heldout["metrics9"]["atoms"],
        "lookup9": heldout["metrics9"]["lookup"],
    }
    directional_rows.append(row)
    print(
        f"  {label:<8} sectors={sectors} atoms9={row['atoms9']} TV9={fmt_frac(row['tv9'], 18)} "
        f"Dpairs9={row['d_pairs9']} Ipairs9={row['i_pairs9']} drift9={fmt_frac(row['drift9'], 18)}"
    )

print("\n" + "=" * 80)
print("Hostile review")
print("=" * 80)
print(
    "1. The harmonic h-transform framing is exact for the oracle h=pres.  "
    "The real problem is finding an admissible quotient h_P that is close "
    "without becoming lookup."
)
print(
    "2. Recurrence-defect generation is not identical to the boundary-residue "
    "generator.  Its blind 7->8 sector list must be judged by held-out N=9 "
    "performance, not by resemblance to earlier hand-named sectors."
)
print(
    "3. All-flag5 remains a useful reconstruction threshold and identity source, "
    "but it is disqualified as a law-level algebra."
)
print(
    "4. The admissibility scan does not collapse to one magic flag list.  "
    "Different weights expose a Pareto frontier: recurrence prediction, drift, "
    "density accuracy, and reconstruction pressure are genuinely distinct."
)
print(
    "5. The dual opening is real.  Posthoc dual closure improves the generated "
    "quotient, and direct dual-orbit generation improves it again.  The surviving "
    "rule is symmetry-constrained recurrence generation, not a fixed sector list."
)

check(
    "oracle h=pres satisfies exact incidence preimage identity",
    not identity_failures and recurrence_rows["oracle"][0] == 0,
    f"failures={len(identity_failures)} oracle_exact_error={fmt_frac(recurrence_rows['oracle'][0], 18)}",
)
check(
    "residual-active h has lower exact recurrence error than hinge and known",
    recurrence_rows["residual"][0] < recurrence_rows["hinge"][0] < recurrence_rows["known"][0],
    (
        f"known={fmt_frac(recurrence_rows['known'][0], 18)} "
        f"hinge={fmt_frac(recurrence_rows['hinge'][0], 18)} "
        f"residual={fmt_frac(recurrence_rows['residual'][0], 18)}"
    ),
)
check(
    "recurrence-defect generator improves held-out N=9 prediction over known sectors",
    generated_tv9 < known_tv9 and not generated_metrics["lookup"],
    f"generated={fmt_frac(generated_tv9, 24)} known={fmt_frac(known_tv9, 24)}",
)
check(
    "recurrence-defect generated algebra beats residual-active on held-out N=9",
    generated_tv9 < residual_tv9 and recurrence_rows["generated"][0] < recurrence_rows["residual"][0],
    (
        f"TV generated={fmt_frac(generated_tv9, 24)} residual={fmt_frac(residual_tv9, 24)}; "
        f"rec generated={fmt_frac(recurrence_rows['generated'][0], 18)} "
        f"residual={fmt_frac(recurrence_rows['residual'][0], 18)}"
    ),
)
check(
    "admissibility frontier rejects all5 lookup but accepts residual nonlookup",
    admissibility["all5"]["lookup"] and not admissibility["residual"]["lookup"],
    f"all5_lookup={admissibility['all5']['lookup']} residual_atoms={admissibility['residual']['atoms']}",
)
check(
    "density residue decreases through known, hinge, residual",
    admissibility["residual"]["residue"]
    < admissibility["hinge"]["residue"]
    < admissibility["known"]["residue"]
    < admissibility["constant"]["residue"],
    (
        f"constant={fmt_frac(admissibility['constant']['residue'], 18)} "
        f"known={fmt_frac(admissibility['known']['residue'], 18)} "
        f"hinge={fmt_frac(admissibility['hinge']['residue'], 18)} "
        f"residual={fmt_frac(admissibility['residual']['residue'], 18)}"
    ),
)
check(
    "residual-active improves deletion lumpability over known sectors",
    lumpability["residual"][1] < lumpability["known"][1],
    f"known_D9_pairs={lumpability['known'][1]} residual_D9_pairs={lumpability['residual'][1]}",
)
check(
    "finite reconstruction threshold occurs at flag5 in audited N=9 sector",
    not flag_threshold[3]["lookup"] and not flag_threshold[4]["lookup"] and flag_threshold[5]["lookup"],
    (
        f"flag3_atoms={flag_threshold[3]['atoms']} "
        f"flag4_atoms={flag_threshold[4]['atoms']} "
        f"flag5_atoms={flag_threshold[5]['atoms']}"
    ),
)
check(
    "quotient recurrence improves strongly but is not exact before lookup",
    recurrence_rows["residual"][1] > 0 and recurrence_rows["all5"][1] == 0,
    (
        f"residual_quotient={fmt_frac(recurrence_rows['residual'][1], 18)} "
        f"all5_quotient={fmt_frac(recurrence_rows['all5'][1], 18)}"
    ),
)
check(
    "admissibility scan finds a nonlookup held-out improver over residual-active",
    best_tv_row["tv9"] < residual_tv9 and not best_tv_row["lookup9"],
    (
        f"best={best_tv_row['label']} TV={fmt_frac(best_tv_row['tv9'], 24)} "
        f"residual={fmt_frac(residual_tv9, 24)}"
    ),
)
check(
    "admissibility scan exposes a real Pareto tradeoff rather than one winner",
    len(front) >= 2 and best_tv_row["sectors"] != best_drift_row["sectors"],
    (
        f"front_size={len(front)} best_tv={best_tv_row['label']} "
        f"best_drift={best_drift_row['label']}"
    ),
)
check(
    "balanced functional remains nonlookup and improves known-sector held-out prediction",
    (not best_balanced["lookup9"]) and best_balanced["tv9"] < known_tv9,
    (
        f"balanced_sectors={best_balanced['sectors']} "
        f"TV={fmt_frac(best_balanced['tv9'], 24)} known={fmt_frac(known_tv9, 24)}"
    ),
)
check(
    "dual closure of recurrence-generated quotient is nonlookup and improves its held-out TV",
    (not generated_dual_row["lookup9"]) and generated_dual_row["tv9"] < generated_tv9,
    (
        f"generated={fmt_frac(generated_tv9, 24)} "
        f"dual_closed={fmt_frac(generated_dual_row['tv9'], 24)} "
        f"closed_sectors={generated_dual_row['closed']}"
    ),
)
check(
    "dual-orbit generator is nonlookup and beats known-sector held-out prediction",
    (not orbit_generated_heldout["metrics9"]["lookup"]) and orbit_generated_heldout["tv9"] < known_tv9,
    (
        f"orbit_generated={fmt_frac(orbit_generated_heldout['tv9'], 24)} "
        f"known={fmt_frac(known_tv9, 24)} sectors={orbit_generated_sectors}"
    ),
)
check(
    "dual-orbit generation beats posthoc dual closure on held-out TV",
    orbit_generated_heldout["tv9"] < generated_dual_row["tv9"]
    and orbit_generated_heldout["comp9"]["exact_rec"] < generated_dual_row["rec9"],
    (
        f"orbit_generated_TV={fmt_frac(orbit_generated_heldout['tv9'], 24)} "
        f"posthoc_closed_TV={fmt_frac(generated_dual_row['tv9'], 24)} "
        f"orbit_rec={fmt_frac(orbit_generated_heldout['comp9']['exact_rec'], 24)} "
        f"closed_rec={fmt_frac(generated_dual_row['rec9'], 24)}"
    ),
)

print("\n=== Campaign status ===")
print(
    "The harmonic quotient framing survives the exact N<=9 audit.  It turns the "
    "hidden law into an h-transform problem on the deletion graph.  The "
    "admissibility functional campaign finds strong nonlookup held-out "
    "predictors, and the dual-orbit follow-up improves the best predictor again.  "
    "The final law is a dual-symmetric Pareto/admissibility principle rather "
    "than a single hand-named sector list."
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
