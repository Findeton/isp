#!/usr/bin/env python3
"""
Paper 29 receipt: N=9 active-mask minimal cover.

The N=9 active scan showed that a greedy local flag cover closes all known-lite
score-polynomial conflict pairs in eight steps.  This receipt asks the exact
finite set-cover question on the active masks:

    What is the smallest number of induced 3-, 4-, and 5-flag operators that
    separates every known-lite score-polynomial conflict pair at N=9?

The base sector is "known-lite": scalar + interval + degree-regularity
features, excluding matching counts.  This receipt therefore proves a finite
known-lite cover theorem, not the final physical law.
"""

from collections import defaultdict
from fractions import Fraction
import math
import sys
from time import perf_counter

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    canon_bits,
    degree_moments,
    flag_counts,
    fmt_frac,
    height,
    interval_counts,
    permutation_order_bits,
    perms,
    relation_count,
    width,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def build_score_polynomials(n):
    p_counts = defaultdict(int)
    polys = defaultdict(lambda: [0 for _ in range(n + 1)])
    reps = {}
    start = perf_counter()
    total = math.factorial(n)
    for idx, pi in enumerate(perms(n), start=1):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        p_counts[key] += 1
        cut = n // 2
        score = sum(1 for x, y in enumerate(pi) if (x < cut) == (y < cut))
        polys[key][score] += 1
        if idx % 100000 == 0:
            print(
                f"  enumerated {idx}/{total} permutations; classes={len(p_counts)}; "
                f"elapsed={perf_counter() - start:.2f}s"
            )
    P = {key: Fraction(count, total) for key, count in p_counts.items()}
    return P, dict(polys), dict(p_counts), reps, perf_counter() - start


def normalized_poly(poly, count):
    return tuple(Fraction(coeff, count) for coeff in poly)


def known_lite_features(bits, n):
    intervals = interval_counts(bits, n)
    _deg1, deg2, deg3, dmax, dmin = degree_moments(bits, n)
    return (
        relation_count(bits, n),
        height(bits, n),
        width(bits, n),
        tuple(intervals[:5]),
        sum(intervals[5:]),
        deg2,
        deg3,
        dmax,
        dmin,
        dmax - dmin,
    )


def known_lite_conflicts(P, reps, normalized, n):
    atoms = defaultdict(list)
    for key, bits in reps.items():
        atoms[known_lite_features(bits, n)].append(key)
    conflicts = []
    bad_atoms = 0
    bad_mass = Fraction(0)
    for keys in atoms.values():
        first = normalized[keys[0]]
        if any(normalized[key] != first for key in keys[1:]):
            bad_atoms += 1
            bad_mass += sum(P[key] for key in keys)
            for idx, left in enumerate(keys):
                for right in keys[idx + 1 :]:
                    if normalized[left] != normalized[right]:
                        conflicts.append((left, right))
    return atoms, conflicts, bad_atoms, bad_mass


def active_flag_values(reps, keys, n):
    values = {}
    universe = set()
    start = perf_counter()
    for idx, key in enumerate(keys, start=1):
        bits = reps[key]
        row = {}
        for k in (3, 4, 5):
            counts = flag_counts(bits, n, k)
            for flag_key, count in counts.items():
                name = f"flags{k}:flag{k}_{flag_key}"
                row[name] = count
                universe.add(name)
        values[key] = row
        if idx % 30000 == 0:
            print(
                f"  flag rows {idx}/{len(keys)}; universe={len(universe)}; "
                f"elapsed={perf_counter() - start:.2f}s"
            )
    return values, sorted(universe), perf_counter() - start


def build_masks(conflicts, values, universe):
    masks = {}
    for name in universe:
        mask = 0
        for idx, (left, right) in enumerate(conflicts):
            if values[left].get(name, 0) != values[right].get(name, 0):
                mask |= 1 << idx
        if mask:
            masks[name] = mask
    return masks


def reduce_dominated(names, masks):
    kept = []
    for name in names:
        mask = masks[name]
        dominated = False
        for other in names:
            if other == name:
                continue
            other_mask = masks[other]
            if mask != other_mask and (mask | other_mask) == other_mask:
                dominated = True
                break
        if not dominated:
            kept.append(name)
    return kept


def bit_indices(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def greedy_cover(full_mask, names, masks):
    remaining = full_mask
    selected = []
    while remaining:
        best = max(names, key=lambda name: (remaining & masks[name]).bit_count())
        gain_mask = remaining & masks[best]
        if not gain_mask:
            break
        selected.append(best)
        remaining &= ~gain_mask
    return selected, remaining


def exact_cover(full_mask, names, masks, max_depth):
    conflict_to_names = defaultdict(list)
    for name in names:
        for idx in bit_indices(masks[name]):
            conflict_to_names[idx].append(name)
    for idx in conflict_to_names:
        conflict_to_names[idx].sort(key=lambda name: masks[name].bit_count(), reverse=True)

    all_union = 0
    for name in names:
        all_union |= masks[name]
    if (full_mask | all_union) != all_union:
        return None, 0

    max_cover = max(mask.bit_count() for mask in masks.values())
    memo = set()
    calls = 0
    start = perf_counter()

    def choose_conflict(remaining):
        best_idx = None
        best_options = None
        probe = remaining
        while probe:
            low = probe & -probe
            idx = low.bit_length() - 1
            options = [
                name for name in conflict_to_names[idx] if masks[name] & remaining
            ]
            if best_options is None or len(options) < len(best_options):
                best_idx = idx
                best_options = options
                if len(best_options) == 1:
                    break
            probe ^= low
        return best_idx, best_options or []

    def dfs(remaining, depth, chosen):
        nonlocal calls
        calls += 1
        if remaining == 0:
            return list(chosen)
        if depth == 0:
            return None
        if (remaining.bit_count() + max_cover - 1) // max_cover > depth:
            return None
        key = (remaining, depth)
        if key in memo:
            return None

        _idx, options = choose_conflict(remaining)
        options = sorted(
            options,
            key=lambda name: (remaining & masks[name]).bit_count(),
            reverse=True,
        )
        for name in options:
            gain = remaining & masks[name]
            if not gain:
                continue
            result = dfs(remaining & ~gain, depth - 1, chosen + (name,))
            if result is not None:
                return result
        memo.add(key)
        return None

    for depth in range(1, max_depth + 1):
        print(f"  exact search depth={depth}")
        result = dfs(full_mask, depth, ())
        print(
            f"    depth={depth} done calls={calls} memo={len(memo)} "
            f"elapsed={perf_counter() - start:.2f}s"
        )
        if result is not None:
            return result, calls
    return None, calls


print("=" * 80)
print("Paper 29 N=9 active-mask minimal cover")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 9
P, polys, p_counts, reps, build_elapsed = build_score_polynomials(n)
normalized = {key: normalized_poly(polys[key], p_counts[key]) for key in P}
atoms, conflicts, bad_atoms, bad_mass = known_lite_conflicts(P, reps, normalized, n)
conflict_keys = sorted({key for pair in conflicts for key in pair})
values, universe, flag_elapsed = active_flag_values(reps, conflict_keys, n)
masks = build_masks(conflicts, values, universe)
names = sorted(masks, key=lambda name: masks[name].bit_count(), reverse=True)
reduced = reduce_dominated(names, masks)
full_mask = (1 << len(conflicts)) - 1
greedy, greedy_remaining = greedy_cover(full_mask, names, masks)

print("\nN=9 known-lite active cover setup:")
print(f"  record classes={len(P)}")
print(f"  known-lite atoms={len(atoms)}/{len(P)}")
print(f"  bad_atoms={bad_atoms}")
print(f"  bad_mass={fmt_frac(bad_mass, 36)}")
print(f"  conflict_pairs={len(conflicts)}")
print(f"  conflict_records={len(conflict_keys)}")
print(f"  active_flags={len(names)} reduced_flags={len(reduced)}")
print(f"  quotient_elapsed={build_elapsed:.2f}s flag_elapsed={flag_elapsed:.2f}s")
print(f"  greedy_size={len(greedy)} greedy_remaining={greedy_remaining.bit_count()}")
print("  greedy=" + ", ".join(greedy))

solution, calls = exact_cover(full_mask, reduced, masks, max_depth=len(greedy))

if solution is None:
    print("exact_solution=None")
else:
    covered = 0
    for name in solution:
        covered |= masks[name]
    print(f"exact_solution_size={len(solution)}")
    print("exact_solution=" + ", ".join(solution))
    print(f"exact_solution_remaining={(full_mask & ~covered).bit_count()}")
print(f"exact_search_calls={calls}")

check(
    "greedy active cover closes all known-lite conflicts",
    greedy_remaining == 0,
    f"greedy_size={len(greedy)}",
)
check(
    "exact active-mask search found a cover",
    solution is not None,
    "solution_size=" + (str(len(solution)) if solution else "None"),
)
check(
    "exact cover is no larger than greedy cover",
    solution is not None and len(solution) <= len(greedy),
    f"exact={len(solution) if solution else 'None'} greedy={len(greedy)}",
)
check(
    "solution covers every conflict pair",
    solution is not None
    and (full_mask & ~sum((masks[name] for name in []), 0)) == full_mask
    and (lambda m: (full_mask & ~m) == 0)(
        __import__("functools").reduce(lambda a, b: a | b, (masks[name] for name in solution), 0)
    ),
    f"conflicts={len(conflicts)}",
)
check(
    "known-lite qualifier remains essential",
    bad_mass > Fraction(1, 2),
    f"bad_mass={fmt_frac(bad_mass, 24)}",
)

print("\n=== N=9 active minimal-cover status ===")
print(
    "The exact active-mask search turns the greedy N=9 known-lite closure into "
    "a finite cover certificate.  This still does not prove the full physical "
    "record law, because the base partition is known-lite, but it strongly "
    "supports a small controlled local cover at the next size."
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
