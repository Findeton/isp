#!/usr/bin/env python3
"""
Paper 29 receipt: boundary-histogram minimal cover.

The rooted deletion recurrence receipt shows that the compressed score-loss
histogram

    H_R(a,b) = P(deleted child has score a and score loss b | parent record R)

reconstructs the normalized score polynomial Wbar_R.  It is therefore a
natural bridge object for deletion/insertion transfer.  This receipt asks the
next finite question:

    how many ordinary local flags are needed to make H_R constant on known
    sector atoms?

This is a stricter target than Wbar sufficiency.  All finite counts are exact
integers/Fractions.  Decimal reporting uses mpmath with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import math
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    build_projected_laws,
    canon_bits,
    feature_maps,
    fmt_frac,
    permutation_order_bits,
    perms,
    same_block_score,
)

sys.setrecursionlimit(10000)
sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

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
    polys = defaultdict(lambda: [0 for _ in range(n + 1)])
    reps = {}
    fibers = defaultdict(list)
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        fibers[key].append(pi)
        p_counts[key] += 1
        polys[key][same_block_score(pi)] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    norm_poly = {
        key: tuple(Fraction(coeff, p_counts[key]) for coeff in polys[key])
        for key in p_counts
    }
    return P, dict(polys), norm_poly, dict(p_counts), reps, dict(fibers)


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


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def partition_atoms(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atoms[tuple(feature_mapping(features, name)[key] for name in names)].append(key)
    return atoms


def bad_atoms(P, features, names, invariant):
    atoms = partition_atoms(P, features, names)
    bad = []
    for atom, keys in atoms.items():
        buckets = defaultdict(list)
        for key in keys:
            buckets[invariant[key]].append(key)
        if len(buckets) > 1:
            bad.append((atom, keys))
    return atoms, bad


def conflict_pairs(bad, invariant):
    conflicts = []
    for _atom, keys in bad:
        for idx, left in enumerate(keys):
            for right in keys[idx + 1 :]:
                if invariant[left] != invariant[right]:
                    conflicts.append((left, right))
    return conflicts


def feature_conflict_mask(mapping, conflicts):
    mask = 0
    for idx, (left, right) in enumerate(conflicts):
        if mapping[left] != mapping[right]:
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
    max_gain = max(mask.bit_count() for mask in (masks[name] for name in candidates))

    coverers = defaultdict(list)
    for name in candidates:
        mask = masks[name]
        m = mask
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


print("=" * 80)
print("Paper 29 boundary-histogram minimal cover")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

summaries = {}
for n in [7, 8]:
    print("\n" + "=" * 80)
    print(f"N={n} Hbar conflict cover")
    print("=" * 80)
    P, polys, norm_poly, counts, reps, fibers = build_score_data(n)
    H = boundary_histograms(n, counts, fibers)
    features = feature_maps(P, reps, n)
    known = feature_names(features, ["scalar", "interval", "regularity", "matching"])
    candidates = feature_names(features, ["flags3", "flags4", "flags5"])
    atoms, bad = bad_atoms(P, features, known, H)
    conflicts = conflict_pairs(bad, H)
    full_mask = (1 << len(conflicts)) - 1
    masks = {name: feature_conflict_mask(feature_mapping(features, name), conflicts) for name in candidates}
    active = [name for name in candidates if masks[name]]
    print(f"classes={len(P)} known_atoms={len(atoms)} H_bad={len(bad)} H_conflicts={len(conflicts)}")
    print(f"candidate_flags={len(candidates)} active_flags={len(active)}")
    solution, reduced = exact_cover(active, masks, full_mask)
    if solution is None:
        print("no local flag cover found in flags3/4/5")
        solution = []
    else:
        solution_atoms, solution_bad = bad_atoms(P, features, known + solution, H)
        unresolved = [keys for keys in solution_atoms.values() if len(keys) > 1]
        unresolved_mass = sum(P[key] for keys in unresolved for key in keys)
        print(f"reduced_candidates={len(reduced)}")
        print(f"minimal_or_certified_solution_size={len(solution)}")
        print(f"solution={solution}")
        print(
            f"solution_atoms={len(solution_atoms)}/{len(P)} H_bad_after={len(solution_bad)} "
            f"unresolved_mass={fmt_frac(unresolved_mass, 36)}"
        )
    summaries[n] = {
        "classes": len(P),
        "known_bad": len(bad),
        "conflicts": len(conflicts),
        "active": len(active),
        "solution": solution,
        "solution_size": len(solution),
        "covered": solution is not None,
    }

check(
    "known sectors do not determine Hbar at N=7 or N=8",
    summaries[7]["known_bad"] > 0 and summaries[8]["known_bad"] > 0,
    f"N7={summaries[7]['known_bad']} N8={summaries[8]['known_bad']}",
)
check(
    "a local flag cover of Hbar exists at N=7",
    summaries[7]["covered"] and summaries[7]["solution_size"] > 0,
    f"size={summaries[7]['solution_size']} solution={summaries[7]['solution']}",
)
check(
    "a local flag cover of Hbar exists at N=8",
    summaries[8]["covered"] and summaries[8]["solution_size"] > 0,
    f"size={summaries[8]['solution_size']} solution={summaries[8]['solution']}",
)
check(
    "Hbar cover is no easier than Wbar cover at N=8",
    summaries[8]["solution_size"] >= 3,
    f"Hbar_size={summaries[8]['solution_size']}",
)

print("\n=== Boundary-cover status ===")
print(
    "The compressed deletion boundary Hbar is a stricter finite target than "
    "Wbar, but it is still locally coverable in the audited window.  This keeps "
    "the recurrence path alive while showing that boundary-transfer stability "
    "requires more than the finite Wbar covers alone."
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
