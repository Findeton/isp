#!/usr/bin/env python3
"""
Paper 29 receipt: omitted local flag spike scan.

The admissibility norm audit showed that locality alone is not admissibility.
This receipt makes the hostile local version systematic: for a committed cover
G, scan every omitted induced 3-, 4-, and 5-flag score

    Q_F(R) proportional to P(R) 2^{count_F(R)}

and measure the projected residual, A2 norm, and Q mass on the unresolved
non-singleton atoms U.

The purpose is to separate two notions:

1. local flag algebra: projective and record-intrinsic;
2. admissible local score: only harmless if its residue is controlled or its
   separator is promoted into G.
"""

from collections import defaultdict
from fractions import Fraction
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    build_projected_laws,
    feature_maps,
    fmt_frac,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def feature_names(features, groups):
    names = []
    for group in groups:
        for feature_name in sorted(features[group]):
            names.append(f"{group}:{feature_name}")
    return names


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def partition_atoms(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atoms[tuple(feature_mapping(features, name)[key] for name in names)].append(key)
    return atoms


def q_from_record_score(P, score_by_key, base):
    weights = {key: base ** score_by_key[key] for key in P}
    normalizer = sum(P[key] * weights[key] for key in P)
    return {key: P[key] * weights[key] / normalizer for key in P}


def second_moment(P, Q):
    return sum((Q[key] * Q[key]) / P[key] for key in P)


def projected_second_moment(P, Q, atoms):
    p_atoms = defaultdict(Fraction)
    q_atoms = defaultdict(Fraction)
    for atom, keys in atoms.items():
        for key in keys:
            p_atoms[atom] += P[key]
            q_atoms[atom] += Q[key]
    return sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms)


def scan_cover(P, features, cover, label, base=2):
    known = feature_names(features, ["scalar", "interval", "regularity", "matching"])
    atoms = partition_atoms(P, features, known + cover)
    U = [key for keys in atoms.values() if len(keys) > 1 for key in keys]
    eps = sum(P[key] for key in U)
    candidates = [
        name
        for name in feature_names(features, ["flags3", "flags4", "flags5"])
        if name not in cover
    ]
    rows = []
    for name in candidates:
        score = feature_mapping(features, name)
        Q = q_from_record_score(P, score, base)
        L = {key: Q[key] / P[key] for key in P}
        S_full = second_moment(P, Q)
        S_G = projected_second_moment(P, Q, atoms)
        residual = S_full - S_G
        A2 = sum(P[key] * L[key] * L[key] for key in U)
        qU = sum(Q[key] for key in U)
        supU = max((L[key] for key in U), default=Fraction(0))
        Ainf = eps * supU * supU
        rows.append((residual, A2, qU, Ainf, name, S_full))
    rows.sort(reverse=True, key=lambda row: (row[0], row[1], row[2], row[4]))
    print("\n" + "=" * 80)
    print(f"{label}: omitted local flag spike scan")
    print("=" * 80)
    print(f"atoms={len(atoms)}/{len(P)} unresolved_records={len(U)} eps={fmt_frac(eps, 36)}")
    print(f"candidate_omitted_flags={len(candidates)} base={base}")
    print("top omitted local spikes:")
    for residual, A2, qU, Ainf, name, S_full in rows[:12]:
        print(
            f"  {name:<24} residual={fmt_frac(residual, 24)} "
            f"A2={fmt_frac(A2, 24)} qU={fmt_frac(qU, 24)} "
            f"Ainf={fmt_frac(Ainf, 24)} S_full={fmt_frac(S_full, 24)}"
        )
    return {
        "label": label,
        "rows": rows,
        "eps": eps,
        "unresolved_records": len(U),
        "atoms": len(atoms),
    }


print("=" * 80)
print("Paper 29 omitted local flag spike scan")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

P8, _Q8, reps8 = build_projected_laws(8, weight_base=3)
features8 = feature_maps(P8, reps8, 8)

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

fixed = scan_cover(P8, features8, fixed_four, "N=8 fixed four", base=2)
triple = scan_cover(P8, features8, first_n8_triple, "N=8 first minimal triple", base=2)

top_fixed = fixed["rows"][0]
top_triple = triple["rows"][0]

check(
    "fixed-four cover has omitted local spike with nontrivial admissibility norm",
    top_fixed[1] > Fraction(9, 10),
    f"top={top_fixed[4]} A2={fmt_frac(top_fixed[1], 30)}",
)
check(
    "first N=8 triple has omitted local spike with sector-scale residual",
    top_triple[0] > 1000,
    f"top={top_triple[4]} residual={fmt_frac(top_triple[0], 30)}",
)
check(
    "first N=8 triple omitted local spike concentrates Q on unresolved atoms",
    top_triple[2] > Fraction(9, 10),
    f"top={top_triple[4]} qU={fmt_frac(top_triple[2], 30)}",
)
check(
    "flag5_926 attack appears in first-triple scan",
    any(name == "flags5:flag5_926" and residual > 1000 for residual, _A2, _qU, _Ainf, name, _S in triple["rows"]),
    "flag5_926 is a sector-scale omitted local score",
)
check(
    "admissibility norm dominates residual for top omitted spikes",
    top_fixed[0] <= top_fixed[1] <= top_fixed[3]
    and top_triple[0] <= top_triple[1] <= top_triple[3],
    "residual <= A2 <= Ainf",
)

print("\n=== Omitted-local-spike status ===")
print(
    "Omitted local flags can be hostile.  Bounded flag size and record locality "
    "do not imply admissibility.  The cover must either include the relevant "
    "separator, make its A2 residue small, or promote the residue as a sector."
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
