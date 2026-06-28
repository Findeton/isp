#!/usr/bin/env python3
"""
Paper 29 receipt: targeted rare-atom amplification.

The ordinary local-flag amplification receipt shows that a large weight on
flag5_920 still does not defeat known+four.  This receipt tests the genuinely
hostile branch: weight one exact record atom inside the single unresolved
known+four atom at N=7.

This is intentionally spiky.  It is not a natural coordinate score.  Its role
is to prove scope: the four-operator certificate is not universal over all
projected laws, and an admissibility/regularity condition is needed if this
kind of atom-targeting law is to be rejected rather than promoted.

All finite probabilities are exact Fractions.  Decimal reporting uses mpmath
with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
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


def atom_partition(P, features, feature_names):
    atoms = defaultdict(list)
    for key in P:
        atom = tuple(feature_mapping(features, name)[key] for name in feature_names)
        atoms[atom].append(key)
    return atoms


def capture_from_names(P, Q, features, feature_names):
    p_atoms = defaultdict(Fraction)
    q_atoms = defaultdict(Fraction)
    for key in P:
        atom = tuple(feature_mapping(features, name)[key] for name in feature_names)
        p_atoms[atom] += P[key]
        q_atoms[atom] += Q[key]
    return sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms)


def second_moment(P, Q):
    return sum((Q[key] * Q[key]) / P[key] for key in P if Q[key] != 0)


def build_targeted_law(n, target_key, base):
    p_counts = defaultdict(int)
    q_counts = defaultdict(int)
    reps = {}
    total_weight = 0
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        weight = base if key == target_key else 1
        p_counts[key] += 1
        q_counts[key] += weight
        total_weight += weight
    total_p = math.factorial(n)
    P = {key: Fraction(count, total_p) for key, count in p_counts.items()}
    Q = {key: Fraction(q_counts[key], total_weight) for key in p_counts}
    return P, Q, reps


print("=" * 80)
print("Paper 29 targeted rare-atom amplification")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P0, _Q0, reps0 = build_projected_laws(n)
features = feature_maps(P0, reps0, n)

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
fixed_features = known_features + four_features
repair_features = fixed_features + ["flags4:flag4_14"]

atoms = atom_partition(P0, features, fixed_features)
unresolved = [keys for keys in atoms.values() if len(keys) > 1]
target_key = unresolved[0][0]
unresolved_mass = sum(P0[key] for key in unresolved[0])

print(f"N={n} record classes={len(P0)}")
print(f"unresolved_atoms={len(unresolved)} unresolved_size={len(unresolved[0])}")
print(f"unresolved_null_mass={fmt_frac(unresolved_mass, 36)}")
print(f"target_key={target_key}")

bases = [2, 3, 5, 10, 50, 100, 1000, 10000]
rows = []

for base in bases:
    P, Q, _reps = build_targeted_law(n, target_key, base)
    s_full = second_moment(P, Q)
    s_known = capture_from_names(P, Q, features, known_features)
    s_fixed = capture_from_names(P, Q, features, fixed_features)
    s_repair = capture_from_names(P, Q, features, repair_features)
    known_capture = (s_known - 1) / (s_full - 1)
    fixed_capture = (s_fixed - 1) / (s_full - 1)
    repair_capture = (s_repair - 1) / (s_full - 1)
    rows.append((base, s_full, known_capture, fixed_capture, repair_capture))
    print(
        f"base={base:<5} S_full={fmt_frac(s_full, 36)} "
        f"known={fmt_frac(known_capture, 24)} "
        f"fixed_four={fmt_frac(fixed_capture, 24)} "
        f"+flag4_14={fmt_frac(repair_capture, 24)}"
    )

check(
    "fixed four miss the targeted atom at every audited base",
    all(row[3] < Fraction(3, 4) for row in rows),
    "fixed_captures=" + ", ".join(fmt_frac(row[3], 8) for row in rows),
)
check(
    "targeted second moment grows under amplification",
    rows[-1][1] > rows[0][1] * 1000,
    f"base2={fmt_frac(rows[0][1], 18)} base10000={fmt_frac(rows[-1][1], 18)}",
)
check(
    "one explicit local separator repairs the targeted atom",
    all(row[4] == 1 for row in rows),
    "+flag4_14 captures=" + ", ".join(fmt_frac(row[4], 8) for row in rows),
)
check(
    "known sectors are even weaker than fixed four",
    all(row[2] < row[3] for row in rows),
    "base3 known/fixed=" + fmt_frac(rows[1][2], 12) + "/" + fmt_frac(rows[1][3], 12),
)

print("\n=== Targeted amplification status ===")
print(
    "A deliberately atom-spiky projected law defeats the literal fixed-four "
    "certificate at all audited weights and can drive the second moment large. "
    "Adding a separator flag repairs it.  Thus the four operators are not a "
    "universal law; atom-spiky residues require sector promotion or an "
    "admissibility/regularity exclusion."
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
