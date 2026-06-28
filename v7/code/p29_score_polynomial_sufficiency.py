#!/usr/bin/env python3
"""
Paper 29 receipt: score-polynomial sufficiency theorem.

The greedy robustness audit found that the same four local flag operators close
the exact likelihood gap for staged/fiber weight bases 2, 3, and 5.  This
receipt follows the Ramanujan/Euler opening: maybe the agreement is not three
numerical coincidences, but an exact polynomial identity.

For every unlabeled record class R in the N=7 toy, define the hidden-score
polynomial

    W_R(t) = sum_{permutations pi projecting to R} t^{s(pi)},

where s(pi) is the same-half staged/fiber score.  The projected likelihood for
weight base t is proportional to W_R(t) / |fiber(R)|.

Therefore a record-sector filtration G is predictively sufficient for every
weight base t iff W_R(t)/|fiber(R)| is identical for all records R in each
G-atom.

This receipt proves that known sectors plus the four greedy operators satisfy
that polynomial identity at N=7, before full atom reconstruction.

All finite counts are exact integers/Fractions.  Decimal reporting uses mpmath
with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
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


def partition_key(features, record_key, feature_names):
    return tuple(feature_mapping(features, name)[record_key] for name in feature_names)


def sufficiency_violations(features, P, normalized, feature_names):
    atoms = defaultdict(list)
    for record_key in P:
        atoms[partition_key(features, record_key, feature_names)].append(record_key)
    violations = []
    for atom, keys in atoms.items():
        first = normalized[keys[0]]
        bad = [key for key in keys[1:] if normalized[key] != first]
        if bad:
            violations.append((atom, keys))
    return atoms, violations


def evaluate_poly(norm_poly, base):
    total = Fraction(0)
    power = Fraction(1)
    for coeff in norm_poly:
        total += coeff * power
        power *= base
    return total


print("=" * 80)
print("Paper 29 score-polynomial sufficiency")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, polys, p_counts, reps = build_score_polynomials(n)
features = feature_maps(P, reps, n)
normalized = {key: normalized_poly(polys[key], p_counts[key]) for key in P}

known_features = []
for group in ["scalar", "interval", "regularity", "matching"]:
    for feature_name in sorted(features[group]):
        known_features.append(f"{group}:{feature_name}")

greedy_features = [
    "flags3:flag3_36",
    "flags4:flag4_206",
    "flags5:flag5_17288",
    "flags4:flag4_0",
]

full_features = known_features + greedy_features
atoms, violations = sufficiency_violations(features, P, normalized, full_features)

print(f"N={n} record classes={len(P)}")
print(f"known feature count={len(known_features)}")
print(f"greedy feature count={len(greedy_features)}")
print(f"full feature atom count={len(atoms)}")
print(f"violation count={len(violations)}")

for base in [2, 3, 5]:
    max_gap = Fraction(0)
    for _atom, keys in atoms.items():
        values = [evaluate_poly(normalized[key], Fraction(base)) for key in keys]
        gap = max(values) - min(values)
        max_gap = max(max_gap, gap)
    print(f"base={base} max within-atom normalized polynomial gap={fmt_frac(max_gap, 30)}")

removal_failures = {}
for removed in greedy_features:
    reduced = [name for name in full_features if name != removed]
    _atoms_reduced, violations_reduced = sufficiency_violations(features, P, normalized, reduced)
    removal_failures[removed] = len(violations_reduced)
    print(f"remove {removed}: polynomial-violating atoms={len(violations_reduced)}")

known_atoms, known_violations = sufficiency_violations(features, P, normalized, known_features)
print(f"known-only atom count={len(known_atoms)}")
print(f"known-only polynomial-violating atoms={len(known_violations)}")

check(
    "known plus four greedy operators gives exact score-polynomial sufficiency",
    len(violations) == 0,
    f"atoms={len(atoms)} violations={len(violations)}",
)
check(
    "score-polynomial sufficiency holds for all audited bases as a corollary",
    all(
        evaluate_poly(normalized[keys[0]], Fraction(base))
        == evaluate_poly(normalized[key], Fraction(base))
        for base in [2, 3, 5]
        for keys in atoms.values()
        for key in keys
    ),
    "bases=2,3,5",
)
check(
    "each greedy operator is necessary within this four-operator certificate",
    all(count > 0 for count in removal_failures.values()),
    "removal violations=" + ", ".join(f"{name}={count}" for name, count in removal_failures.items()),
)
check(
    "known sectors alone are not polynomially sufficient",
    len(known_violations) > 0,
    f"known_violations={len(known_violations)}",
)
check(
    "predictive sufficiency occurs before full atom reconstruction",
    len(atoms) == len(P) - 1,
    f"atoms={len(atoms)} classes={len(P)}",
)

print("\n=== Polynomial status ===")
print(
    "The four greedy operators are not merely a fit at bases 2, 3, and 5.  "
    "They make the normalized hidden-score polynomial W_R(t)/|fiber(R)| "
    "constant on every remaining sector atom.  Thus the finite staged/fiber "
    "family is predictively sufficient for all weight bases t in this N=7 toy."
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
