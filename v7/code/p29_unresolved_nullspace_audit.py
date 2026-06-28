#!/usr/bin/env python3
"""
Paper 29 receipt: unresolved nullspace audit.

The adversarial score-family audit shows that known sectors plus the four
greedy operators leave exactly one two-record atom unresolved at N=7.  This
receipt asks whether that is a broad hidden nullspace or a rare-pair spike.

For every remaining exact 3-, 4-, and 5-flag operator, compute the exact
conditional variance

    E_P[ Var_P(O | G) ],

where G is the known-sector plus four-greedy-operator filtration.  Since G has
1955 atoms for 1956 records, all invisible variation should be concentrated on
one atom if the finite certificate is genuinely narrow.

All finite probabilities are exact Fractions.  Decimal reporting uses mpmath
with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    build_projected_laws,
    degree_moments,
    feature_maps,
    fmt_frac,
    height,
    interval_counts,
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


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def second_moment(P, Q):
    return sum((Q[key] * Q[key]) / P[key] for key in P if Q[key] != 0)


def partition_atoms(P, features, feature_names):
    atoms = defaultdict(list)
    for record_key in P:
        atom = tuple(feature_mapping(features, name)[record_key] for name in feature_names)
        atoms[atom].append(record_key)
    return atoms


def conditional_variance(P, atoms, mapping):
    total = Fraction(0)
    active_atoms = []
    for atom, keys in atoms.items():
        if len(keys) == 1:
            continue
        p_atom = sum(P[key] for key in keys)
        first = mapping[keys[0]]
        if all(mapping[key] == first for key in keys[1:]):
            continue
        sum_x = sum(P[key] * mapping[key] for key in keys)
        sum_x2 = sum(P[key] * mapping[key] * mapping[key] for key in keys)
        var_mass = sum_x2 - (sum_x * sum_x) / p_atom
        total += var_mass
        active_atoms.append((atom, keys, var_mass))
    return total, active_atoms


def describe_record(bits, n):
    return (
        f"rel={relation_count(bits, n)} h={height(bits, n)} w={width(bits, n)} "
        f"intervals={interval_counts(bits, n)[:6]} degree={degree_moments(bits, n)}"
    )


print("=" * 80)
print("Paper 29 unresolved nullspace audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, Q, reps = build_projected_laws(n)
features = feature_maps(P, reps, n)

known_features = []
for group in ["scalar", "interval", "regularity", "matching"]:
    for feature_name in sorted(features[group]):
        known_features.append(f"{group}:{feature_name}")

fixed_greedy = [
    "flags3:flag3_36",
    "flags4:flag4_206",
    "flags5:flag5_17288",
    "flags4:flag4_0",
]

G_features = known_features + fixed_greedy
atoms = partition_atoms(P, features, G_features)
unresolved_atoms = [(atom, keys) for atom, keys in atoms.items() if len(keys) > 1]

candidate_features = []
for group in ["flags3", "flags4", "flags5"]:
    for feature_name in sorted(features[group]):
        name = f"{group}:{feature_name}"
        if name not in fixed_greedy:
            candidate_features.append(name)

rows = []
for name in candidate_features:
    mapping = feature_mapping(features, name)
    variance, active_atoms = conditional_variance(P, atoms, mapping)
    if variance:
        rows.append((variance, name, active_atoms))

rows.sort(reverse=True, key=lambda row: (row[0], row[1]))

s_full = second_moment(P, Q)
print(f"N={n} record classes={len(P)}")
print(f"S_full={fmt_frac(s_full, 36)}")
print(f"G atom count={len(atoms)}/{len(P)}")
print(f"unresolved atoms={len(unresolved_atoms)}")
print(f"positive invisible flag operators={len(rows)}")

if unresolved_atoms:
    _atom, keys = unresolved_atoms[0]
    print("\nUnresolved pair:")
    for key in keys:
        print(f"  key={key} P={fmt_frac(P[key], 30)} {describe_record(reps[key], n)}")

print("\nTop invisible local flags:")
for variance, name, active_atoms in rows[:12]:
    _atom, keys, _var_mass = active_atoms[0]
    values = [feature_mapping(features, name)[key] for key in keys]
    print(f"  {name} variance={fmt_frac(variance, 36)} values={values}")

top_names = [name for _variance, name, _active_atoms in rows[:12]]
active_atom_counts = {len(active_atoms) for _variance, _name, active_atoms in rows}

check(
    "known plus four has exactly one unresolved two-record atom",
    len(unresolved_atoms) == 1 and len(unresolved_atoms[0][1]) == 2,
    f"unresolved={len(unresolved_atoms)} size={len(unresolved_atoms[0][1]) if unresolved_atoms else 0}",
)
check(
    "invisible flag variation is concentrated on that atom",
    active_atom_counts == {1},
    f"active_atom_counts={sorted(active_atom_counts)}",
)
check(
    "there are local flags that separate the unresolved atom",
    len(rows) > 0,
    f"positive_flags={len(rows)}",
)
check(
    "flag4_14 is an explicit low-order separator",
    "flags4:flag4_14" in [name for _variance, name, _active_atoms in rows],
    "separator=flags4:flag4_14",
)
check(
    "the unresolved nullspace is rare under the null law",
    sum(P[key] for key in unresolved_atoms[0][1]) < Fraction(1, 1000),
    f"mass={fmt_frac(sum(P[key] for key in unresolved_atoms[0][1]), 30)}",
)

print("\n=== Nullspace status ===")
print(
    "The hidden variation missed by known sectors plus the four greedy operators "
    "is not broad in the N=7 toy.  It is concentrated on one rare two-record "
    "atom, and ordinary local flags such as flag4_14 separate it.  This supports "
    "the scoped theorem target: regular hidden scores may wash out this rare "
    "nullspace, while spiky rare-atom scores must be promoted or rejected."
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
