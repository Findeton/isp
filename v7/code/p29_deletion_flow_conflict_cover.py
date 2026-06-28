#!/usr/bin/env python3
"""
Paper 29 receipt: deletion flow of local conflict covers.

The previous receipts found that the literal sufficient flag names drift between
N=7 and N=8.  This receipt checks the distinction between:

1. the local flag algebra, which should be projectively natural under deletion;
2. finite sufficiency covers, which may drift inside that algebra.

For every N=8 record class and every induced 3-, 4-, and 5-flag, it verifies
the exact deletion identity

    sum_v count_F(R \\ v) = (N - |F|) count_F(R).

It then compares the N=7 fixed four cover and the first N=8 minimal triple
across both sizes.
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
    restrict_bits,
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
    out = []
    for group in groups:
        for feature_name in sorted(features[group]):
            out.append(f"{group}:{feature_name}")
    return out


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def feature_value(features, name, key):
    group, feature = name.split(":", 1)
    return features.get(group, {}).get(feature, {}).get(key, 0)


def partition_atoms(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atom = tuple(feature_value(features, name, key) for name in names)
        atoms[atom].append(key)
    return atoms


def polynomial_bad_count(P, features, names, normalized):
    atoms = partition_atoms(P, features, names)
    bad = 0
    for keys in atoms.values():
        first = normalized[keys[0]]
        if any(normalized[key] != first for key in keys[1:]):
            bad += 1
    return len(atoms), bad


def deletion_keys(bits, n):
    out = []
    for deleted in range(n):
        subset = tuple(v for v in range(n) if v != deleted)
        out.append(canon_bits(restrict_bits(bits, n, subset), n - 1))
    return out


print("=" * 80)
print("Paper 29 deletion flow of local conflict covers")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

P7, polys7, counts7, reps7 = build_score_polynomials(7)
P8, polys8, counts8, reps8 = build_score_polynomials(8)
features7 = feature_maps(P7, reps7, 7)
features8 = feature_maps(P8, reps8, 8)
normalized7 = {key: normalized_poly(polys7[key], counts7[key]) for key in P7}
normalized8 = {key: normalized_poly(polys8[key], counts8[key]) for key in P8}

known7 = feature_names(features7, ["scalar", "interval", "regularity", "matching"])
known8 = feature_names(features8, ["scalar", "interval", "regularity", "matching"])
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

flag_names8 = feature_names(features8, ["flags3", "flags4", "flags5"])
delete_cache = {key: deletion_keys(bits, 8) for key, bits in reps8.items()}

identity_count = 0
violations = []
for name in flag_names8:
    group, _feature = name.split(":", 1)
    k = int(group.replace("flags", ""))
    expected_factor = 8 - k
    mapping8 = feature_mapping(features8, name)
    for key, count8 in mapping8.items():
        deletion_sum = sum(feature_value(features7, name, key7) for key7 in delete_cache[key])
        identity_count += 1
        if deletion_sum != expected_factor * count8:
            violations.append((name, key, deletion_sum, expected_factor * count8))
            if len(violations) >= 5:
                break
    if violations:
        break

atoms7_fixed, bad7_fixed = polynomial_bad_count(
    P7, features7, known7 + fixed_four, normalized7
)
atoms8_fixed, bad8_fixed = polynomial_bad_count(
    P8, features8, known8 + fixed_four, normalized8
)
atoms7_triple, bad7_triple = polynomial_bad_count(
    P7, features7, known7 + first_n8_triple, normalized7
)
atoms8_triple, bad8_triple = polynomial_bad_count(
    P8, features8, known8 + first_n8_triple, normalized8
)

unresolved7_triple = [
    keys
    for keys in partition_atoms(P7, features7, known7 + first_n8_triple).values()
    if len(keys) > 1
]
mass7_triple = sum(P7[key] for keys in unresolved7_triple for key in keys)

print(f"N=8 classes={len(P8)} N=7 classes={len(P7)}")
print(f"checked deletion identities={identity_count}")
print(f"violations={len(violations)}")
print("cross-size polynomial sufficiency:")
print(f"  N=7 fixed four: atoms={atoms7_fixed}/{len(P7)} bad={bad7_fixed}")
print(f"  N=8 fixed four: atoms={atoms8_fixed}/{len(P8)} bad={bad8_fixed}")
print(f"  N=7 first N=8 triple: atoms={atoms7_triple}/{len(P7)} bad={bad7_triple}")
print(f"  N=8 first N=8 triple: atoms={atoms8_triple}/{len(P8)} bad={bad8_triple}")
print(
    f"  N=7 first N=8 triple unresolved_mass={fmt_frac(mass7_triple, 36)} "
    f"unresolved_atoms={len(unresolved7_triple)}"
)

check(
    "all audited N=8 to N=7 flag deletion identities hold",
    len(violations) == 0,
    f"checked={identity_count}",
)
check(
    "N=7 fixed four are polynomial sufficient at N=7",
    bad7_fixed == 0,
    f"atoms={atoms7_fixed}/{len(P7)}",
)
check(
    "N=7 fixed four transfer upward to N=8 for this score",
    bad8_fixed == 0,
    f"atoms={atoms8_fixed}/{len(P8)}",
)
check(
    "first N=8 minimal triple is sufficient at N=8",
    bad8_triple == 0,
    f"atoms={atoms8_triple}/{len(P8)}",
)
check(
    "first N=8 minimal triple is not sufficient at N=7",
    bad7_triple > 0,
    f"bad={bad7_triple} unresolved_mass={fmt_frac(mass7_triple, 30)}",
)

print("\n=== Deletion-flow status ===")
print(
    "The induced-flag algebra itself is deletion-natural, but finite sufficient "
    "covers are not fixed objects under size change.  N=7's fixed four transfer "
    "upward for the audited score, while an N=8 minimal triple does not project "
    "back to N=7 sufficiency.  The invariant is a projective local algebra with "
    "controlled covers, not immutable operator names."
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
