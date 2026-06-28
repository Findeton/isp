#!/usr/bin/env python3
"""
Paper 29 receipt: effective action projection identity.

This receipt follows the Witten/Noether opening.  If a hidden refinement
induces a record law Q while the baseline record law is P, then any committed
feature filtration G has a forced effective record law:

    Q_G(R) = P(R) E_P[dQ/dP | G](R).

Equivalently, the effective action S_eff = -log E[L | G] is the result of
integrating out hidden or unresolved record details inside each G-atom.

For finite record spaces this has an exact information-geometric identity:

    D(Q || P) = D(Q || Q_G) + D(Q_G || P).

The receipt checks the identity on the N=7 staged/fiber record quotient for
the known-sector filtration, the known+four greedy filtration, and the full
record atom filtration.

All finite probabilities are exact Fractions.  Logarithms and KL sums use
mpmath with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    build_projected_laws,
    feature_maps,
    fmt,
    fmt_frac,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def mp_from_fraction(value):
    return mp.mpf(value.numerator) / mp.mpf(value.denominator)


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def atom_partition(P, features, feature_names):
    atoms = defaultdict(list)
    for key in P:
        if feature_names == ["full_atom"]:
            atom = key
        else:
            atom = tuple(feature_mapping(features, name)[key] for name in feature_names)
        atoms[atom].append(key)
    return atoms


def projected_law(P, Q, atoms):
    QG = {}
    atom_stats = {}
    for atom, keys in atoms.items():
        p_atom = sum(P[key] for key in keys)
        q_atom = sum(Q[key] for key in keys)
        likelihood = q_atom / p_atom
        atom_stats[atom] = (p_atom, q_atom, likelihood, len(keys))
        for key in keys:
            QG[key] = P[key] * likelihood
    return QG, atom_stats


def kl(A, B):
    total = mp.mpf("0")
    for key in A:
        if A[key] == 0:
            continue
        total += mp_from_fraction(A[key]) * mp.log(mp_from_fraction(A[key] / B[key]))
    return total


def second_moment(P, Q):
    return sum((Q[key] * Q[key]) / P[key] for key in P if Q[key] != 0)


def describe_filtration(label, P, Q, features, feature_names):
    atoms = atom_partition(P, features, feature_names)
    QG, atom_stats = projected_law(P, Q, atoms)
    d_qp = kl(Q, P)
    d_q_qg = kl(Q, QG)
    d_qg_p = kl(QG, P)
    gap = abs(d_qp - d_q_qg - d_qg_p)
    s_g = second_moment(P, QG)
    max_atom_size = max(len(keys) for keys in atoms.values())
    print(
        f"{label}: atoms={len(atoms)}/{len(P)} max_atom={max_atom_size} "
        f"D(Q||P)={fmt(d_qp, 36)} D(Q||Q_G)={fmt(d_q_qg, 36)} "
        f"D(Q_G||P)={fmt(d_qg_p, 36)} gap={fmt(gap, 8)} "
        f"S_G={fmt_frac(s_g, 36)}"
    )
    return {
        "label": label,
        "atoms": atoms,
        "QG": QG,
        "atom_stats": atom_stats,
        "D_QP": d_qp,
        "D_Q_QG": d_q_qg,
        "D_QG_P": d_qg_p,
        "gap": gap,
        "S_G": s_g,
        "max_atom_size": max_atom_size,
    }


print("=" * 80)
print("Paper 29 effective action projection identity")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, Q, reps = build_projected_laws(n)
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

known = describe_filtration("known", P, Q, features, known_features)
known_four = describe_filtration("known+four", P, Q, features, known_features + four_features)
full = describe_filtration("full_atom", P, Q, features, ["full_atom"])

total_mass_known_four = sum(known_four["QG"].values())
max_q_gap_known_four = max(abs(Q[key] - known_four["QG"][key]) for key in P)

check(
    "effective projected law is normalized",
    total_mass_known_four == 1,
    f"mass={fmt_frac(total_mass_known_four, 30)}",
)
check(
    "KL Pythagorean identity holds for all audited filtrations",
    max(known["gap"], known_four["gap"], full["gap"]) < mp.mpf("1e-120"),
    "max_gap=" + fmt(max(known["gap"], known_four["gap"], full["gap"]), 12),
)
check(
    "information captured is monotone under refinement",
    known["D_QG_P"] <= known_four["D_QG_P"] <= full["D_QG_P"],
    f"D_known={fmt(known['D_QG_P'], 24)} D_four={fmt(known_four['D_QG_P'], 24)} D_full={fmt(full['D_QG_P'], 24)}",
)
check(
    "known+four is exact for the staged/fiber base-3 law",
    max_q_gap_known_four == 0 and known_four["D_Q_QG"] < mp.mpf("1e-120"),
    f"max_q_gap={fmt_frac(max_q_gap_known_four, 30)} residual_KL={fmt(known_four['D_Q_QG'], 12)}",
)
check(
    "known sectors alone leave positive unresolved action",
    known["D_Q_QG"] > mp.mpf("1e-6"),
    f"known_residual_KL={fmt(known['D_Q_QG'], 24)}",
)

print("\n=== Effective-action status ===")
print(
    "For every committed feature filtration G, the projected record law Q_G is "
    "the unique effective action obtained by integrating out unresolved record "
    "details inside G-atoms.  The KL identity separates captured record action "
    "from residual hidden/record action exactly.  In the staged/fiber N=7 toy, "
    "known+four captures all of Q, while known sectors alone leave positive "
    "residual action."
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
