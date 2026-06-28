#!/usr/bin/env python3
"""
Paper 29 receipt: boundary-histogram cover transfer.

The boundary-histogram minimal-cover receipt found small local covers for Hbar
at N=7 and N=8.  This receipt asks the hostile transfer question: do those
covers travel across N, or do they drift like the Wbar covers?

All finite counts are exact integers/Fractions.  Decimal reporting uses
mpmath with dps=140.
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


def delete_position(pi, i):
    removed = pi[i]
    return tuple(value - (1 if value > removed else 0) for j, value in enumerate(pi) if j != i)


def build_score_data(n):
    p_counts = defaultdict(int)
    reps = {}
    fibers = defaultdict(list)
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        fibers[key].append(pi)
        p_counts[key] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    return P, dict(p_counts), reps, dict(fibers)


def boundary_histograms(n, counts, fibers):
    hist = {key: defaultdict(int) for key in fibers}
    for key, fiber in fibers.items():
        for pi in fiber:
            parent_score = same_block_score(pi)
            for i in range(n):
                child = delete_position(pi, i)
                a = same_block_score(child)
                b = parent_score - a
                hist[key][(a, b)] += 1
    return {
        key: tuple(sorted((item, Fraction(count, n * counts[key])) for item, count in row.items()))
        for key, row in hist.items()
    }


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


def bad_rows(P, features, names, H):
    atoms = partition_atoms(P, features, names)
    bad = []
    conflicts = 0
    bad_mass = Fraction(0)
    unresolved_mass = Fraction(0)
    for keys in atoms.values():
        if len(keys) > 1:
            unresolved_mass += sum(P[key] for key in keys)
        buckets = defaultdict(list)
        for key in keys:
            buckets[H[key]].append(key)
        if len(buckets) <= 1:
            continue
        bad.append(keys)
        bad_mass += sum(P[key] for key in keys)
        for i, left in enumerate(keys):
            for right in keys[i + 1 :]:
                if H[left] != H[right]:
                    conflicts += 1
    return {
        "atoms": len(atoms),
        "bad_atoms": len(bad),
        "conflicts": conflicts,
        "bad_mass": bad_mass,
        "unresolved_mass": unresolved_mass,
    }


n7_h_cover = [
    "flags3:flag3_36",
    "flags4:flag4_2062",
    "flags4:flag4_192",
    "flags5:flag5_525184",
]
n8_h_cover = [
    "flags3:flag3_36",
    "flags5:flag5_549376",
    "flags4:flag4_2176",
    "flags4:flag4_206",
    "flags5:flag5_24576",
]
wbar_n7_fixed = [
    "flags3:flag3_36",
    "flags4:flag4_206",
    "flags5:flag5_17288",
    "flags4:flag4_0",
]
wbar_n8_triple = [
    "flags4:flag4_192",
    "flags4:flag4_2248",
    "flags5:flag5_16904",
]

cover_sets = {
    "none": [],
    "Wbar_N7_fixed": wbar_n7_fixed,
    "Wbar_N8_triple": wbar_n8_triple,
    "Hbar_N7_cover": n7_h_cover,
    "Hbar_N8_cover": n8_h_cover,
    "Hbar_union": sorted(set(n7_h_cover + n8_h_cover)),
}

print("=" * 80)
print("Paper 29 boundary-histogram cover transfer")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

matrix = {}
for n in [7, 8]:
    print("\n" + "=" * 80)
    print(f"N={n} Hbar transfer rows")
    print("=" * 80)
    P, counts, reps, fibers = build_score_data(n)
    H = boundary_histograms(n, counts, fibers)
    features = feature_maps(P, reps, n)
    known = feature_names(features, ["scalar", "interval", "regularity", "matching"])
    matrix[n] = {}
    for label, cover in cover_sets.items():
        row = bad_rows(P, features, known + cover, H)
        matrix[n][label] = row
        print(
            f"{label:<18} atoms={row['atoms']:>6}/{len(P):<6} "
            f"H_bad={row['bad_atoms']:>5} H_conf={row['conflicts']:>7} "
            f"bad_mass={fmt_frac(row['bad_mass'], 24)} "
            f"unresolved_mass={fmt_frac(row['unresolved_mass'], 24)}"
        )

check(
    "N=7 Hbar cover closes N=7",
    matrix[7]["Hbar_N7_cover"]["conflicts"] == 0,
    f"conflicts={matrix[7]['Hbar_N7_cover']['conflicts']}",
)
check(
    "N=8 Hbar cover closes N=8",
    matrix[8]["Hbar_N8_cover"]["conflicts"] == 0,
    f"conflicts={matrix[8]['Hbar_N8_cover']['conflicts']}",
)
check(
    "Wbar covers are not enough for Hbar transfer",
    matrix[8]["Wbar_N7_fixed"]["conflicts"] > 0
    and matrix[8]["Wbar_N8_triple"]["conflicts"] > 0,
    (
        f"N8 fixed={matrix[8]['Wbar_N7_fixed']['conflicts']} "
        f"N8 triple={matrix[8]['Wbar_N8_triple']['conflicts']}"
    ),
)
check(
    "Hbar union closes both audited levels",
    matrix[7]["Hbar_union"]["conflicts"] == 0 and matrix[8]["Hbar_union"]["conflicts"] == 0,
    f"N7={matrix[7]['Hbar_union']['conflicts']} N8={matrix[8]['Hbar_union']['conflicts']}",
)
check(
    "Hbar covers drift across N",
    matrix[8]["Hbar_N7_cover"]["conflicts"] > 0 or matrix[7]["Hbar_N8_cover"]["conflicts"] > 0,
    (
        f"N7cover_on_N8={matrix[8]['Hbar_N7_cover']['conflicts']} "
        f"N8cover_on_N7={matrix[7]['Hbar_N8_cover']['conflicts']}"
    ),
)

print("\n=== Boundary-transfer status ===")
print(
    "The compressed boundary Hbar is locally coverable, but its small covers "
    "drift across N.  The union closes the audited N=7 and N=8 levels.  This "
    "keeps the recurrence path alive while confirming that the theorem must "
    "control cover drift, not preserve fixed operator names."
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
