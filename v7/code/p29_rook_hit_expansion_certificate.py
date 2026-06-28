#!/usr/bin/env python3
"""
Paper 29 receipt: rook/hit expansion certificate.

For the same-half hidden score s(pi), the projected score polynomial over a
record R is

    W_R(t) = sum_{pi -> R} t ** s(pi).

Writing t = 1 + z gives

    W_R(1+z) = sum_k H_{R,k} z ** k,

where H_{R,k} = sum_{pi -> R} binom(s(pi), k).  Thus H_{R,k} counts hidden
permutations over R together with k selected nonattacking hits in the hidden
same-half board.  This is the conditional rook/hit expansion of the projected
partition function.

The receipt checks that the binomial transform reproduces the polynomial
exactly and that normalized hit-coefficient vectors are constant on known+four
atoms, but not on known-sector atoms.
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


def binom(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)


def build_score_and_hit_tables(n):
    p_counts = defaultdict(int)
    score_coeffs = defaultdict(lambda: [0 for _ in range(n + 1)])
    hit_coeffs = defaultdict(lambda: [0 for _ in range(n + 1)])
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        score = same_block_score(pi)
        p_counts[key] += 1
        score_coeffs[key][score] += 1
        for k in range(score + 1):
            hit_coeffs[key][k] += binom(score, k)
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    return P, dict(score_coeffs), dict(hit_coeffs), dict(p_counts), reps


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def partition_atoms(P, features, feature_names):
    atoms = defaultdict(list)
    for record_key in P:
        atom = tuple(feature_mapping(features, name)[record_key] for name in feature_names)
        atoms[atom].append(record_key)
    return atoms


def normalized_vector(coeffs, count):
    return tuple(Fraction(value, count) for value in coeffs)


def violations(P, atoms, normalized):
    bad = []
    for atom, keys in atoms.items():
        first = normalized[keys[0]]
        if any(normalized[key] != first for key in keys[1:]):
            bad.append((atom, keys))
    return bad


def eval_score(coeffs, t):
    total = 0
    power = 1
    for coeff in coeffs:
        total += coeff * power
        power *= t
    return total


def eval_hit(coeffs, t):
    z = t - 1
    total = 0
    power = 1
    for coeff in coeffs:
        total += coeff * power
        power *= z
    return total


print("=" * 80)
print("Paper 29 rook/hit expansion certificate")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, score_coeffs, hit_coeffs, p_counts, reps = build_score_and_hit_tables(n)
features = feature_maps(P, reps, n)

known_features = []
for group in ["scalar", "interval", "regularity", "matching"]:
    for feature_name in sorted(features[group]):
        known_features.append(f"{group}:{feature_name}")

four_features = [
    "flags3:flag3_36",
    "flags4:flag4_206",
    "flags5:flag5_17288",
    "flags4:flag4_0",
]

known_atoms = partition_atoms(P, features, known_features)
four_atoms = partition_atoms(P, features, known_features + four_features)
normalized_hit = {
    key: normalized_vector(hit_coeffs[key], p_counts[key])
    for key in P
}

known_bad = violations(P, known_atoms, normalized_hit)
four_bad = violations(P, four_atoms, normalized_hit)

transform_errors = []
for key in P:
    for t in [0, 1, 2, 3, 5, 11]:
        if eval_score(score_coeffs[key], t) != eval_hit(hit_coeffs[key], t):
            transform_errors.append((key, t))
            break

print(f"N={n} record classes={len(P)}")
print(f"known atoms={len(known_atoms)} hit-vector-bad atoms={len(known_bad)}")
print(f"known+four atoms={len(four_atoms)} hit-vector-bad atoms={len(four_bad)}")
print(f"binomial-transform errors={len(transform_errors)}")

if known_bad:
    atom, keys = known_bad[0]
    print(
        "first known violation: "
        f"atom_size={len(keys)} normalized_hit_values="
        + "; ".join(str(normalized_hit[key]) for key in keys[:3])
    )

check(
    "score polynomial equals rook/hit expansion",
    len(transform_errors) == 0,
    f"errors={len(transform_errors)}",
)
check(
    "known sectors alone are not hit-coefficient sufficient",
    len(known_bad) > 0,
    f"known_bad={len(known_bad)}",
)
check(
    "known plus four is hit-coefficient sufficient",
    len(four_bad) == 0,
    f"four_bad={len(four_bad)} atoms={len(four_atoms)}",
)
check(
    "hit sufficiency precedes full atom reconstruction",
    len(four_atoms) == len(P) - 1,
    f"atoms={len(four_atoms)} classes={len(P)}",
)

print("\n=== Rook/hit status ===")
print(
    "The same-half projected partition function is exactly a conditional "
    "rook/hit polynomial over hidden fibers.  Known+four makes the normalized "
    "hit-coefficient vector constant on sector atoms.  This gives an algebraic "
    "interpretation of the finite score-polynomial identity."
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
