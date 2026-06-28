#!/usr/bin/env python3
"""
Paper 29 receipt: rare-spike amplification.

Known+four misses one rare two-record atom at N=7.  This receipt tilts only by
one local flag that separates that atom, flag5_920, and asks how the miss scales
as the hidden weight base grows.

The result distinguishes two regimes:

1. bounded/regular score strengths, where the missed residue is tiny;
2. unbounded local-flag score strengths, which might have amplified the miss.

The hostile outcome is that this local-flag amplification still does not defeat
known+four: most of the flag5_920 likelihood is carried by sectors already
resolved by known+four.  This narrows the genuine adversary from "large local
flag" to "directly target the unresolved atom."

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


def capture_from_names(P, Q, features, feature_names):
    p_atoms = defaultdict(Fraction)
    q_atoms = defaultdict(Fraction)
    for record_key in P:
        atom = tuple(feature_mapping(features, name)[record_key] for name in feature_names)
        p_atoms[atom] += P[record_key]
        q_atoms[atom] += Q[record_key]
    return sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms)


def second_moment(P, Q):
    return sum((Q[key] * Q[key]) / P[key] for key in P if Q[key] != 0)


def build_law_from_record_score(n, score_by_record, base):
    p_counts = defaultdict(int)
    q_counts = defaultdict(int)
    reps = {}
    total_weight = 0
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        score = score_by_record[key]
        weight = base**score
        p_counts[key] += 1
        q_counts[key] += weight
        total_weight += weight
    total_p = math.factorial(n)
    P = {key: Fraction(count, total_p) for key, count in p_counts.items()}
    Q = {key: Fraction(q_counts[key], total_weight) for key in p_counts}
    return P, Q, reps


print("=" * 80)
print("Paper 29 rare-spike amplification")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P0, _Q0, reps = build_projected_laws(n)
features = feature_maps(P0, reps, n)

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
repair_features = fixed_features + ["flags5:flag5_920"]

score_by_record = features["flags5"]["flag5_920"]
bases = [2, 3, 5, 10, 50, 100, 1000]
rows = []

for base in bases:
    P, Q, _reps = build_law_from_record_score(n, score_by_record, base)
    s_full = second_moment(P, Q)
    s_known = capture_from_names(P, Q, features, known_features)
    s_fixed = capture_from_names(P, Q, features, fixed_features)
    s_repair = capture_from_names(P, Q, features, repair_features)
    known_capture = (s_known - 1) / (s_full - 1)
    fixed_capture = (s_fixed - 1) / (s_full - 1)
    repair_capture = (s_repair - 1) / (s_full - 1)
    rows.append((base, s_full, known_capture, fixed_capture, repair_capture))
    print(
        f"base={base:<4} S_full={fmt_frac(s_full, 36)} "
        f"known={fmt_frac(known_capture, 24)} "
        f"fixed_four={fmt_frac(fixed_capture, 24)} "
        f"+flag5_920={fmt_frac(repair_capture, 24)}"
    )

check(
    "bounded rare-spike weights leave small fixed-four miss",
    rows[0][3] > Fraction(99, 1000) and rows[1][3] > Fraction(999, 1000),
    f"base2={fmt_frac(rows[0][3], 24)} base3={fmt_frac(rows[1][3], 24)}",
)
check(
    "unbounded local-flag weights still do not amplify the fixed-four miss",
    rows[-1][3] > Fraction(999999, 1000000),
    f"base1000_fixed_capture={fmt_frac(rows[-1][3], 24)}",
)
check(
    "adding the separating local flag repairs every audited base",
    all(row[4] == 1 for row in rows),
    "+flag5_920 capture=" + ", ".join(fmt_frac(row[4], 8) for row in rows),
)
check(
    "known sectors alone are insufficient for the spiky score",
    rows[-1][2] < rows[-1][3],
    f"known={fmt_frac(rows[-1][2], 24)} fixed={fmt_frac(rows[-1][3], 24)}",
)

print("\n=== Rare-spike status ===")
print(
    "Amplifying an ordinary local flag that separates the unresolved atom does "
    "not defeat known+four, even at large audited bases.  The failure mode is "
    "narrower: a law must directly target the unresolved atom rather than merely "
    "raise a local flag correlated with it.  This strengthens the regular "
    "local-operator reading and confines the adversary to atom-spiky laws."
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
