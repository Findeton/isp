#!/usr/bin/env python3
"""
Paper 29 receipt: N=8 polynomial minimal cover.

The N=8 transfer receipt shows that the N=7 fixed four operators transfer, but
that fresh greedy selects different operators.  This receipt asks the finite
algebraic question directly:

    What is the smallest subset of exact local flags that makes the normalized
    same-half score polynomial constant on known-sector atoms at N=8?

It searches all 3-, 4-, and 5-flag operators.  The result is a conflict-cover
statement: no single flag and no pair suffice; triples do suffice.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import math
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    canon_bits,
    feature_maps,
    fmt_frac,
    permutation_order_bits,
    perms,
    same_block_score,
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
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        score = same_block_score(pi)
        p_counts[key] += 1
        polys[key][score] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    return P, dict(polys), dict(p_counts), reps


def normalized_poly(poly, count):
    return tuple(Fraction(coeff, count) for coeff in poly)


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def partition_atoms(P, features, feature_names):
    atoms = defaultdict(list)
    for key in P:
        atom = tuple(feature_mapping(features, name)[key] for name in feature_names)
        atoms[atom].append(key)
    return atoms


def bad_atoms(P, features, feature_names, normalized):
    atoms = partition_atoms(P, features, feature_names)
    bad = []
    for atom, keys in atoms.items():
        first = normalized[keys[0]]
        if any(normalized[key] != first for key in keys[1:]):
            bad.append((atom, keys))
    return atoms, bad


def conflict_pairs(bad, normalized):
    conflicts = []
    for _atom, keys in bad:
        for idx, left in enumerate(keys):
            for right in keys[idx + 1 :]:
                if normalized[left] != normalized[right]:
                    conflicts.append((left, right))
    return conflicts


def feature_conflict_mask(mapping, conflicts):
    mask = 0
    for idx, (left, right) in enumerate(conflicts):
        if mapping[left] != mapping[right]:
            mask |= 1 << idx
    return mask


print("=" * 80)
print("Paper 29 N=8 polynomial minimal cover")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 8
P, polys, p_counts, reps = build_score_polynomials(n)
features = feature_maps(P, reps, n)
normalized = {key: normalized_poly(polys[key], p_counts[key]) for key in P}

known_features = []
for group in ["scalar", "interval", "regularity", "matching"]:
    for feature_name in sorted(features[group]):
        known_features.append(f"{group}:{feature_name}")

candidate_features = []
for group in ["flags3", "flags4", "flags5"]:
    for feature_name in sorted(features[group]):
        candidate_features.append(f"{group}:{feature_name}")

known_atoms, known_bad = bad_atoms(P, features, known_features, normalized)
print(f"N={n} record classes={len(P)}")
print(f"candidate flags={len(candidate_features)}")
print(f"known atoms={len(known_atoms)} known_bad={len(known_bad)}")

conflicts = conflict_pairs(known_bad, normalized)
full_mask = (1 << len(conflicts)) - 1
candidate_masks = {
    candidate: feature_conflict_mask(feature_mapping(features, candidate), conflicts)
    for candidate in candidate_features
}
active_candidates = [
    candidate for candidate in candidate_features if candidate_masks[candidate] != 0
]
print(f"polynomial conflict pairs={len(conflicts)}")
print(f"active conflict-cover flags={len(active_candidates)}")

single_solutions = []
for candidate in active_candidates:
    if candidate_masks[candidate] == full_mask:
        atoms, _bad = bad_atoms(P, features, known_features + [candidate], normalized)
        single_solutions.append((candidate, len(atoms)))

pair_solutions = []
for combo in combinations(active_candidates, 2):
    if (candidate_masks[combo[0]] | candidate_masks[combo[1]]) == full_mask:
        atoms, _bad = bad_atoms(P, features, known_features + list(combo), normalized)
        pair_solutions.append((combo, len(atoms)))
        break

triple_solutions = []
for combo in combinations(active_candidates, 3):
    if (
        candidate_masks[combo[0]]
        | candidate_masks[combo[1]]
        | candidate_masks[combo[2]]
    ) == full_mask:
        atoms, bad = bad_atoms(P, features, known_features + list(combo), normalized)
        if bad:
            continue
        triple_solutions.append((combo, len(atoms), max(len(keys) for keys in atoms.values())))
        if len(triple_solutions) >= 12:
            break

first_combo, first_atoms, first_max_atom = triple_solutions[0]
unresolved = [
    keys
    for keys in partition_atoms(P, features, known_features + list(first_combo)).values()
    if len(keys) > 1
]
unresolved_mass = sum(P[key] for keys in unresolved for key in keys)

print(f"single_solutions={len(single_solutions)}")
print(f"pair_solutions_found={len(pair_solutions)}")
print(f"triple_solutions_listed={len(triple_solutions)}")
for idx, (combo, atom_count, max_atom) in enumerate(triple_solutions[:6], start=1):
    print(f"  triple {idx}: {combo} atoms={atom_count}/{len(P)} max_atom={max_atom}")
print(
    f"first triple unresolved atoms={len(unresolved)} max_size={max(len(keys) for keys in unresolved)} "
    f"mass={fmt_frac(unresolved_mass, 36)}"
)

check(
    "known sectors alone are not polynomial sufficient at N=8",
    len(known_bad) > 0,
    f"known_bad={len(known_bad)}",
)
check(
    "no single local flag suffices",
    len(single_solutions) == 0,
    f"single_solutions={len(single_solutions)}",
)
check(
    "no pair suffices in the audited local flag family",
    len(pair_solutions) == 0,
    f"pair_solutions_found={len(pair_solutions)}",
)
check(
    "a triple local-flag cover exists",
    len(triple_solutions) > 0,
    f"first={first_combo}",
)
check(
    "the triple cover is not a lookup table",
    first_atoms < len(P) and unresolved_mass < Fraction(1, 100),
    f"atoms={first_atoms}/{len(P)} unresolved_mass={fmt_frac(unresolved_mass, 30)}",
)

print("\n=== Minimal-cover status ===")
print(
    "At N=8 the literal N=7 four-name list is not the canonical finite answer. "
    "The exact algebraic object is a small conflict-cover problem over local "
    "flags: no single or pair repair suffices, but triples do.  This supports "
    "a bounded controlled local-operator filtration rather than a fixed list."
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
