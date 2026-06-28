#!/usr/bin/env python3
"""
Paper 29 receipt: deck-ambiguity certificate.

Receipt 20 found that the N=7 staged/fiber toy has exactly one unresolved
atom after known sectors plus 4-flags.  This receipt follows that opening:
it extracts the two records in the ambiguous atom and identifies the exact
5-flag deck entries that separate them.

The point is not that the finite witness is the physical law.  The point is
that the remaining projected-likelihood residue is a concrete induced-suborder
witness, not a vague failure of scalar diagnostics.

All finite probabilities are exact Fractions.  Decimal reporting uses mpmath
with dps=140.
"""

from collections import defaultdict
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    build_projected_laws,
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


def partition_key(features, record_key, group_names):
    values = []
    for group_name in group_names:
        for _feature_name, mapping in sorted(features[group_name].items()):
            values.append(mapping[record_key])
    return tuple(values)


def partition_members(P, features, group_names):
    members = defaultdict(list)
    for record_key in P:
        members[partition_key(features, record_key, group_names)].append(record_key)
    return dict(members)


def likelihoods(P, Q):
    return {key: Q[key] / P[key] for key in P}


def flag_key_from_name(name):
    return int(name.split("_", 1)[1])


def describe_record(bits, n, L):
    return {
        "relations": relation_count(bits, n),
        "height": height(bits, n),
        "width": width(bits, n),
        "intervals": interval_counts(bits, n)[:5],
        "L": L,
    }


def describe_flag(flag_key):
    return {
        "relations": relation_count(flag_key, 5),
        "height": height(flag_key, 5),
        "width": width(flag_key, 5),
        "intervals": interval_counts(flag_key, 5)[:4],
    }


print("=" * 80)
print("Paper 29 deck-ambiguity certificate")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, Q, reps = build_projected_laws(n)
features = feature_maps(P, reps, n)
L = likelihoods(P, Q)
known_plus_4 = ["scalar", "interval", "regularity", "matching", "flags3", "flags4"]
members = partition_members(P, features, known_plus_4)
ambiguous_atoms = [keys for keys in members.values() if len(keys) > 1]

print(f"ambiguous atom count = {len(ambiguous_atoms)}")
pair = ambiguous_atoms[0]
print(f"ambiguous atom size = {len(pair)}")

for idx, key in enumerate(pair, start=1):
    desc = describe_record(reps[key], n, L[key])
    print(
        f"record {idx}: rel={desc['relations']} h={desc['height']} w={desc['width']} "
        f"L={fmt_frac(desc['L'], 30)} intervals={desc['intervals']}"
    )

differences = []
for name, mapping in sorted(features["flags5"].items()):
    a = mapping[pair[0]]
    b = mapping[pair[1]]
    if a != b:
        flag_key = flag_key_from_name(name)
        differences.append((name, flag_key, a, b, a - b, describe_flag(flag_key)))

print(f"5-flag separating entries = {len(differences)}")
for name, flag_key, a, b, delta, desc in differences:
    print(
        f"  {name}: counts=({a},{b}) delta={delta} "
        f"flag_rel={desc['relations']} flag_h={desc['height']} "
        f"flag_w={desc['width']} flag_intervals={desc['intervals']}"
    )

likelihood_gap = abs(L[pair[0]] - L[pair[1]])
print(f"likelihood_gap = {fmt_frac(likelihood_gap, 30)}")

check(
    "there is exactly one known-plus-4-flag ambiguity at N=7",
    len(ambiguous_atoms) == 1 and len(pair) == 2,
    f"ambiguous_atoms={len(ambiguous_atoms)} size={len(pair)}",
)
check(
    "ambiguous records agree on scalar interval regularity matching and 4-flags",
    partition_key(features, pair[0], known_plus_4) == partition_key(features, pair[1], known_plus_4),
    "same known+4 key",
)
check(
    "the ambiguity has nonzero projected likelihood residue",
    likelihood_gap > 0,
    f"gap={fmt_frac(likelihood_gap, 24)}",
)
check(
    "5-flags give a finite separating certificate",
    len(differences) > 0,
    f"separating_5_flags={len(differences)}",
)

print("\n=== Certificate status ===")
print(
    "The last N=7 residue after known sectors plus 4-flags is separated by a "
    "finite 5-flag deck witness.  Thus the residual is not an unnamed mystery: "
    "it lives in the next induced-suborder layer."
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
