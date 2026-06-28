#!/usr/bin/env python3
"""
Paper 29 receipt: cover transfer matrix.

This receipt turns the "covers drift" claim into a finite transfer matrix.
For N=6,7,8 it computes score-polynomial conflict counts after applying:

1. no local cover;
2. the N=7 fixed-four cover;
3. the first N=8 minimal triple;
4. their union;
5. the scoped N=9 known-lite seven-flag witness, restricted to the flags that
   exist at the smaller N.

The result distinguishes deletion-natural local algebra from stable sufficient
operator names: some covers transfer upward, some fail downward, and union
covers can close both audited sizes.  This is an exact finite shadow of the
desired deletion/insertion recurrence.
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
        p_counts[key] += 1
        polys[key][same_block_score(pi)] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    return P, dict(polys), dict(p_counts), reps


def normalized_poly(poly, count):
    return tuple(Fraction(coeff, count) for coeff in poly)


def feature_names(features, groups):
    names = []
    for group in groups:
        for feature_name in sorted(features[group]):
            names.append(f"{group}:{feature_name}")
    return names


def feature_value(features, name, key):
    group, feature = name.split(":", 1)
    return features.get(group, {}).get(feature, {}).get(key, 0)


def partition_atoms(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atoms[tuple(feature_value(features, name, key) for name in names)].append(key)
    return atoms


def bad_atoms_and_conflicts(P, features, names, normalized):
    atoms = partition_atoms(P, features, names)
    bad = []
    conflicts = []
    bad_mass = Fraction(0)
    for atom, keys in atoms.items():
        polys = defaultdict(list)
        for key in keys:
            polys[normalized[key]].append(key)
        if len(polys) <= 1:
            continue
        bad.append((atom, keys))
        bad_mass += sum(P[key] for key in keys)
        for left_idx, left in enumerate(keys):
            for right in keys[left_idx + 1 :]:
                if normalized[left] != normalized[right]:
                    conflicts.append((left, right))
    unresolved_mass = sum(P[key] for keys in atoms.values() if len(keys) > 1 for key in keys)
    return {
        "atoms": len(atoms),
        "bad_atoms": len(bad),
        "conflicts": len(conflicts),
        "bad_mass": bad_mass,
        "unresolved_mass": unresolved_mass,
    }


fixed_four = [
    "flags3:flag3_36",
    "flags4:flag4_206",
    "flags5:flag5_17288",
    "flags4:flag4_0",
]
first_n8_triple = [
    "flags4:flag4_192",
    "flags4:flag4_2248",
    "flags5:flag5_16904",
]
n9_known_lite_witness = [
    "flags3:flag3_36",
    "flags5:flag5_16904",
    "flags5:flag5_25104",
    "flags5:flag5_8704",
    "flags4:flag4_14",
    "flags4:flag4_2248",
    "flags5:flag5_25488",
]

cover_sets = {
    "none": [],
    "N7_fixed_four": fixed_four,
    "N8_first_triple": first_n8_triple,
    "fixed_union_triple": sorted(set(fixed_four + first_n8_triple)),
    "N9_known_lite_7": n9_known_lite_witness,
}

print("=" * 80)
print("Paper 29 cover transfer matrix")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

matrix = {}
for n in [6, 7, 8]:
    P, polys, counts, reps = build_score_polynomials(n)
    features = feature_maps(P, reps, n)
    known = feature_names(features, ["scalar", "interval", "regularity", "matching"])
    normalized = {key: normalized_poly(polys[key], counts[key]) for key in P}
    print("\n" + "=" * 80)
    print(f"N={n} transfer rows")
    print("=" * 80)
    matrix[n] = {}
    for label, cover in cover_sets.items():
        result = bad_atoms_and_conflicts(P, features, known + cover, normalized)
        matrix[n][label] = result
        print(
            f"{label:<20} atoms={result['atoms']:>6}/{len(P):<6} "
            f"bad_atoms={result['bad_atoms']:>5} conflicts={result['conflicts']:>7} "
            f"bad_mass={fmt_frac(result['bad_mass'], 24)} "
            f"unresolved_mass={fmt_frac(result['unresolved_mass'], 24)}"
        )


check(
    "N=7 fixed four close N=7 conflicts",
    matrix[7]["N7_fixed_four"]["conflicts"] == 0,
    f"conflicts={matrix[7]['N7_fixed_four']['conflicts']}",
)
check(
    "N=7 fixed four transfer upward to N=8",
    matrix[8]["N7_fixed_four"]["conflicts"] == 0,
    f"conflicts={matrix[8]['N7_fixed_four']['conflicts']}",
)
check(
    "N=8 first triple closes N=8 but not N=7",
    matrix[8]["N8_first_triple"]["conflicts"] == 0
    and matrix[7]["N8_first_triple"]["conflicts"] > 0,
    f"N8={matrix[8]['N8_first_triple']['conflicts']} N7={matrix[7]['N8_first_triple']['conflicts']}",
)
check(
    "union cover closes both N=7 and N=8",
    matrix[7]["fixed_union_triple"]["conflicts"] == 0
    and matrix[8]["fixed_union_triple"]["conflicts"] == 0,
    f"N7={matrix[7]['fixed_union_triple']['conflicts']} N8={matrix[8]['fixed_union_triple']['conflicts']}",
)
check(
    "N=9 known-lite witness transfers down for the audited score but is not comparable",
    matrix[7]["N9_known_lite_7"]["conflicts"] == 0
    and matrix[8]["N9_known_lite_7"]["conflicts"] == 0,
    f"N7={matrix[7]['N9_known_lite_7']['conflicts']} N8={matrix[8]['N9_known_lite_7']['conflicts']}",
)

print("\n=== Cover-transfer status ===")
print(
    "Finite covers transfer asymmetrically.  The N=7 fixed four close the audited "
    "N=8 score conflicts, while the first N=8 minimal triple does not close N=7. "
    "The scoped N=9 known-lite witness transfers down for this audited score, "
    "but it is not a comparable physical cover because the N=9 base sector was "
    "known-lite.  The recurrence target is a transfer rule for residual conflict "
    "hypergraphs, not fixed operator names."
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
