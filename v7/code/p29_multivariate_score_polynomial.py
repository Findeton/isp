#!/usr/bin/env python3
"""
Paper 29 receipt: multivariate projected score polynomial.

The score-polynomial receipt proved sufficiency for one hidden score.  This
receipt asks whether the same known+four filtration determines a multivariate
projected partition function for several natural coordinate scores at once.

For each record R define

    W_R(u) = sum_{pi -> R} prod_i u_i ** s_i(pi),

where the natural score vector uses same-half, diagonal-band,
anti-diagonal-band, parity-match, lower-left, and central-square counts.  A
filtration G is multivariate sufficient iff the normalized coefficient table
W_R/|fiber(R)| is identical inside every G-atom.

The receipt then adds one deliberately hostile coordinate: an indicator for the
single unresolved atom left by known+four.  Natural coordinates should pass;
the targeted atom coordinate should fail in exactly that one place.

All coefficient tables are exact integer/Fraction dictionaries.  This is a
finite algebraic identity, not a floating-point fit.
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


def diagonal_band(pi):
    return sum(1 for x, y in enumerate(pi) if abs(x - y) <= 1)


def anti_diagonal_band(pi):
    n = len(pi)
    return sum(1 for x, y in enumerate(pi) if abs(x + y - (n - 1)) <= 1)


def lower_left(pi):
    n = len(pi)
    cut = n // 2
    return sum(1 for x, y in enumerate(pi) if x < cut and y < cut)


def central_square(pi):
    n = len(pi)
    lo = n // 3
    hi = n - lo
    return sum(1 for x, y in enumerate(pi) if lo <= x < hi and lo <= y < hi)


def parity_match(pi):
    return sum(1 for x, y in enumerate(pi) if (x - y) % 2 == 0)


SCORE_FNS = [
    ("same_half", same_block_score),
    ("diagonal", diagonal_band),
    ("anti_diagonal", anti_diagonal_band),
    ("parity", parity_match),
    ("lower_left", lower_left),
    ("central_square", central_square),
]


def build_multivariate_polys(n, target_key=None):
    p_counts = defaultdict(int)
    polys = defaultdict(lambda: defaultdict(int))
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        score_values = [fn(pi) for _name, fn in SCORE_FNS]
        if target_key is not None:
            score_values.append(1 if key == target_key else 0)
        score_vector = tuple(score_values)
        p_counts[key] += 1
        polys[key][score_vector] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    return P, dict(polys), dict(p_counts), reps


def normalized_table(poly, count):
    return tuple(sorted((monomial, Fraction(coeff, count)) for monomial, coeff in poly.items()))


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def partition_atoms(P, features, feature_names):
    atoms = defaultdict(list)
    for record_key in P:
        atom = tuple(feature_mapping(features, name)[record_key] for name in feature_names)
        atoms[atom].append(record_key)
    return atoms


def violations(P, features, feature_names, normalized):
    atoms = partition_atoms(P, features, feature_names)
    bad = []
    for atom, keys in atoms.items():
        first = normalized[keys[0]]
        if any(normalized[key] != first for key in keys[1:]):
            bad.append((atom, keys))
    return atoms, bad


def table_at_bases(norm_table, bases):
    total = Fraction(0)
    for monomial, coeff in norm_table:
        weight = Fraction(1)
        for exponent, base in zip(monomial, bases):
            weight *= Fraction(base) ** exponent
        total += coeff * weight
    return total


print("=" * 80)
print("Paper 29 multivariate score polynomial")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, polys, p_counts, reps = build_multivariate_polys(n)
features = feature_maps(P, reps, n)
normalized = {key: normalized_table(polys[key], p_counts[key]) for key in P}

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

known_atoms, known_bad = violations(P, features, known_features, normalized)
four_atoms, four_bad = violations(P, features, known_features + four_features, normalized)

unresolved_atoms = [keys for keys in four_atoms.values() if len(keys) > 1]
target_key = unresolved_atoms[0][0]
P_target, polys_target, p_counts_target, _reps_target = build_multivariate_polys(
    n, target_key=target_key
)
normalized_target = {
    key: normalized_table(polys_target[key], p_counts_target[key])
    for key in P_target
}
_target_known_atoms, target_known_bad = violations(
    P_target, features, known_features, normalized_target
)
target_four_atoms, target_four_bad = violations(
    P_target, features, known_features + four_features, normalized_target
)

monomial_counts = [len(polys[key]) for key in P]
print(f"N={n} record classes={len(P)}")
print("scores=" + ", ".join(name for name, _fn in SCORE_FNS))
print(f"known atoms={len(known_atoms)} multivariate-bad atoms={len(known_bad)}")
print(f"known+four atoms={len(four_atoms)} multivariate-bad atoms={len(four_bad)}")
print(f"known+four unresolved atoms={len(unresolved_atoms)}")
print(f"natural+target known+four bad atoms={len(target_four_bad)}")
print(f"monomial count min={min(monomial_counts)} max={max(monomial_counts)}")

audited_bases = [
    (2, 3, 5, 7, 11, 13),
    (3, 3, 3, 3, 3, 3),
    (5, 2, 2, 3, 7, 11),
]

for bases in audited_bases:
    max_gap = Fraction(0)
    for _atom, keys in four_atoms.items():
        values = [table_at_bases(normalized[key], bases) for key in keys]
        max_gap = max(max_gap, max(values) - min(values))
    print(f"bases={bases} max known+four within-atom gap={fmt_frac(max_gap, 30)}")

check(
    "known sectors alone are not multivariate polynomial sufficient",
    len(known_bad) > 0,
    f"known_bad={len(known_bad)}",
)
check(
    "known plus four is multivariate polynomial sufficient",
    len(four_bad) == 0,
    f"four_bad={len(four_bad)} atoms={len(four_atoms)}",
)
check(
    "multivariate identity implies all audited base evaluations",
    all(
        table_at_bases(normalized[keys[0]], bases) == table_at_bases(normalized[key], bases)
        for bases in audited_bases
        for keys in four_atoms.values()
        for key in keys
    ),
    "audited_base_vectors=3",
)
check(
    "predictive sufficiency still precedes full atom reconstruction",
    len(four_atoms) == len(P) - 1,
    f"atoms={len(four_atoms)} classes={len(P)}",
)
check(
    "adding the targeted atom coordinate breaks exactly the unresolved atom",
    len(target_four_bad) == 1 and target_four_bad[0][1] == unresolved_atoms[0],
    f"target_four_bad={len(target_four_bad)} target_known_bad={len(target_known_bad)}",
)

print("\n=== Multivariate status ===")
print(
    "Known+four does not merely determine one hidden score polynomial.  In this "
    "N=7 toy it determines the joint projected partition function for six "
    "natural coordinate scores simultaneously.  Adding a deliberate unresolved "
    "atom coordinate breaks exactly one atom.  This strengthens the regular "
    "hidden-score reading while keeping the atom-spike warning precise."
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
