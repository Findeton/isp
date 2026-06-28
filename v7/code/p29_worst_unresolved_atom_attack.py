#!/usr/bin/env python3
"""
Paper 29 receipt: worst unresolved atom attack.

For a committed filtration G with a non-singleton atom A and a target record
x in A, the atom-spike laws

    Q_b(R) proportional to P(R) b^{1_{R=x}}

have a sharp limiting residual:

    lim_{b->infty} E_P[(L_b - E[L_b|G])^2]
      = 1/P(x) - 1/P(A).

This is the finite adversarial theorem behind the washout/sector-promotion
fork: rare unresolved atoms are not harmless unless the projected likelihood
on them is controlled by an admissibility bound.
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


def projected_second_moment(P, Q, atoms):
    p_atoms = defaultdict(Fraction)
    q_atoms = defaultdict(Fraction)
    for atom, keys in atoms.items():
        for key in keys:
            p_atoms[atom] += P[key]
            q_atoms[atom] += Q[key]
    return sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms)


def second_moment(P, Q):
    return sum((Q[key] * Q[key]) / P[key] for key in P)


def q_atom_spike(P, target, base):
    weights = {key: (base if key == target else 1) for key in P}
    normalizer = sum(P[key] * weights[key] for key in P)
    return {key: P[key] * weights[key] / normalizer for key in P}


def attack_summary(n, cover_names, label):
    P, _Q, reps = build_projected_laws(n, weight_base=3)
    features = feature_maps(P, reps, n)
    known = feature_names(features, ["scalar", "interval", "regularity", "matching"])
    atoms = partition_atoms(P, features, known + cover_names)
    unresolved = [keys for keys in atoms.values() if len(keys) > 1]
    rows = []
    for keys in unresolved:
        p_atom = sum(P[key] for key in keys)
        for key in keys:
            limit = Fraction(1, 1) / P[key] - Fraction(1, 1) / p_atom
            projected_limit = Fraction(1, 1) / p_atom
            full_limit = Fraction(1, 1) / P[key]
            rows.append((limit, key, p_atom, P[key], full_limit, projected_limit, len(keys)))
    rows.sort(reverse=True, key=lambda row: (row[0], -row[3]))
    worst = rows[0]
    target = worst[1]
    Q_big = q_atom_spike(P, target, 10**6)
    S_full = second_moment(P, Q_big)
    S_G = projected_second_moment(P, Q_big, atoms)
    residual_big = S_full - S_G
    capture_big = (S_G - 1) / (S_full - 1)
    unresolved_mass = sum(P[key] for keys in unresolved for key in keys)
    print("\n" + "=" * 80)
    print(f"{label}: worst unresolved atom attack")
    print("=" * 80)
    print(f"N={n} classes={len(P)} atoms={len(atoms)}/{len(P)}")
    print(f"unresolved_atoms={len(unresolved)} unresolved_mass={fmt_frac(unresolved_mass, 36)}")
    print(f"worst_target={target} atom_size={worst[6]}")
    print(f"P(x)={fmt_frac(worst[3], 36)} P(A)={fmt_frac(worst[2], 36)}")
    print(f"limit_full_second={fmt_frac(worst[4], 36)}")
    print(f"limit_projected_second={fmt_frac(worst[5], 36)}")
    print(f"limit_residual={fmt_frac(worst[0], 36)}")
    print(
        f"base=1e6 residual={fmt_frac(residual_big, 36)} "
        f"capture={fmt_frac(capture_big, 30)}"
    )
    return {
        "label": label,
        "n": n,
        "rows": rows,
        "limit": worst[0],
        "base_residual": residual_big,
        "capture": capture_big,
        "unresolved_mass": unresolved_mass,
        "unresolved_count": len(unresolved),
    }


print("=" * 80)
print("Paper 29 worst unresolved atom attack")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

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

n7 = attack_summary(7, fixed_four, "N=7 fixed four")
n8_fixed = attack_summary(8, fixed_four, "N=8 fixed four")
n8_triple = attack_summary(8, first_n8_triple, "N=8 first minimal triple")

check(
    "N=7 fixed-four limiting residual is large",
    n7["limit"] == 1260,
    f"limit={fmt_frac(n7['limit'], 30)}",
)
check(
    "N=8 fixed-four limiting residual is larger",
    n8_fixed["limit"] == 15120,
    f"limit={fmt_frac(n8_fixed['limit'], 30)}",
)
check(
    "N=8 first-triple limiting residual is larger still",
    n8_triple["limit"] == 20160,
    f"limit={fmt_frac(n8_triple['limit'], 30)}",
)
check(
    "finite high-base residual already realizes sector-scale attack",
    all(row["base_residual"] > row["limit"] * Fraction(9, 10) for row in [n7, n8_fixed, n8_triple]),
    "base=1e6 residuals exceed 90% of exact limits",
)
check(
    "atom-spike capture remains far from exact",
    n7["capture"] < Fraction(3, 5)
    and n8_fixed["capture"] < Fraction(3, 10)
    and n8_triple["capture"] < Fraction(3, 5),
    "captures=" + ", ".join(fmt_frac(row["capture"], 18) for row in [n7, n8_fixed, n8_triple]),
)

print("\n=== Worst-atom status ===")
print(
    "The adversarial formula is exact: any non-singleton committed atom can be "
    "weaponized by a projected atom-spike law.  Projection alone does not remove "
    "this; a physical theorem needs an admissibility bound or sector promotion."
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
