#!/usr/bin/env python3
"""
Paper 29 receipt: admissibility norm audit.

The washout/sector-promotion bound says that rare unresolved atoms are harmless
only when the projected likelihood stays controlled on them:

    residual_G(L) <= E_P[L^2 1_U] <= P(U) sup_U L^2.

This script promotes that inequality into an audit norm:

    A_2(G,L)   = E_P[L^2 1_U],
    A_inf(G,L) = P(U) sup_U L^2,

where U is the union of non-singleton atoms of the committed filtration G.

The audit compares:

1. same-half hidden score laws, which are exactly captured by the audited
   covers;
2. moderate local flag spikes, which can create residue and therefore prove
   that locality alone is not the admissibility criterion;
3. direct atom spikes, which concentrate likelihood on U and force sector
   promotion or exclusion.

All finite probabilities are exact Fractions.  Decimal reporting uses mpmath
with dps=140.
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


def q_from_record_score(P, score_by_key, base):
    weights = {key: base ** score_by_key[key] for key in P}
    normalizer = sum(P[key] * weights[key] for key in P)
    return {key: P[key] * weights[key] / normalizer for key in P}


def q_from_target(P, target_key, base):
    weights = {key: (base if key == target_key else 1) for key in P}
    normalizer = sum(P[key] * weights[key] for key in P)
    return {key: P[key] * weights[key] / normalizer for key in P}


def audit_law(P, Q, atoms):
    U = [key for keys in atoms.values() if len(keys) > 1 for key in keys]
    L = {key: Q[key] / P[key] for key in P}
    S_full = second_moment(P, Q)
    S_G = projected_second_moment(P, Q, atoms)
    residual = S_full - S_G
    eps = sum(P[key] for key in U)
    A2 = sum(P[key] * L[key] * L[key] for key in U)
    supU = max((L[key] for key in U), default=Fraction(0))
    Ainf = eps * supU * supU
    qU = sum(Q[key] for key in U)
    capture = (S_G - 1) / (S_full - 1) if S_full != 1 else Fraction(1)
    return {
        "U": U,
        "S_full": S_full,
        "S_G": S_G,
        "residual": residual,
        "eps": eps,
        "A2": A2,
        "Ainf": Ainf,
        "qU": qU,
        "capture": capture,
        "supU": supU,
    }


def run_case(n, cover_names, local_flag_name, target_base):
    P, Q_same, reps = build_projected_laws(n, weight_base=3)
    features = feature_maps(P, reps, n)
    known = feature_names(features, ["scalar", "interval", "regularity", "matching"])
    atoms = partition_atoms(P, features, known + cover_names)
    U = [key for keys in atoms.values() if len(keys) > 1 for key in keys]
    target_key = U[0]
    local_score = feature_mapping(features, local_flag_name)

    laws = {
        "same_half_base3": Q_same,
        f"local_{local_flag_name}_base2": q_from_record_score(P, local_score, 2),
        f"local_{local_flag_name}_base10": q_from_record_score(P, local_score, 10),
        f"target_atom_base{target_base}": q_from_target(P, target_key, target_base),
    }

    print("\n" + "=" * 80)
    print(f"N={n} admissibility norm audit")
    print("=" * 80)
    print(f"record classes={len(P)}")
    print(f"cover={cover_names}")
    print(f"atoms={len(atoms)}/{len(P)}")
    print(f"unresolved_count={len(U)} unresolved_mass={fmt_frac(sum(P[key] for key in U), 36)}")
    print(f"target_key={target_key}")
    print(f"local_flag={local_flag_name}")
    print(
        "law | residual | capture | eps=P(U) | qU=Q(U) | A2=E[L^2 1_U] | "
        "Ainf=P(U)sup_U L^2"
    )

    reports = {}
    for name, Q in laws.items():
        report = audit_law(P, Q, atoms)
        reports[name] = report
        print(
            f"{name:<32} "
            f"res={fmt_frac(report['residual'], 24)} "
            f"cap={fmt_frac(report['capture'], 24)} "
            f"eps={fmt_frac(report['eps'], 18)} "
            f"qU={fmt_frac(report['qU'], 24)} "
            f"A2={fmt_frac(report['A2'], 24)} "
            f"Ainf={fmt_frac(report['Ainf'], 24)}"
        )

    return reports


print("=" * 80)
print("Paper 29 admissibility norm audit")
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

n7 = run_case(7, fixed_four, "flags5:flag5_920", 10_000)
n8_fixed = run_case(8, fixed_four, "flags5:flag5_920", 1_000_000)
n8_triple = run_case(8, first_n8_triple, "flags5:flag5_16904", 1_000_000)

all_reports = list(n7.values()) + list(n8_fixed.values()) + list(n8_triple.values())

check(
    "admissibility inequality holds for every audited law",
    all(r["residual"] <= r["A2"] <= r["Ainf"] for r in all_reports),
    "residual <= A2 <= Ainf",
)
check(
    "same-half law is exactly captured by the audited covers",
    n7["same_half_base3"]["residual"] == 0
    and n8_fixed["same_half_base3"]["residual"] == 0
    and n8_triple["same_half_base3"]["residual"] == 0,
    "same_half residuals are zero",
)
check(
    "moderate local spikes remain below atom-target sector scale",
    n7["local_flags5:flag5_920_base10"]["residual"]
    < n7["target_atom_base10000"]["residual"]
    and n8_fixed["local_flags5:flag5_920_base10"]["residual"]
    < n8_fixed["target_atom_base1000000"]["residual"],
    "local base10 residuals < atom target residuals",
)
check(
    "direct atom targets concentrate substantial Q mass on unresolved atoms",
    n7["target_atom_base10000"]["qU"] > Fraction(3, 4)
    and n8_fixed["target_atom_base1000000"]["qU"] > Fraction(9, 10)
    and n8_triple["target_atom_base1000000"]["qU"] > Fraction(9, 10),
    "target qU exceeds sector-promotion threshold",
)
check(
    "locality alone is not an admissibility criterion",
    n8_fixed["local_flags5:flag5_920_base2"]["A2"] > Fraction(1, 10),
    f"N8 fixed-cover local A2={fmt_frac(n8_fixed['local_flags5:flag5_920_base2']['A2'], 30)}",
)
check(
    "promoting a local separator into the cover can wash it out",
    n8_triple["local_flags5:flag5_16904_base2"]["residual"] == 0
    and n8_triple["local_flags5:flag5_16904_base10"]["residual"] == 0,
    "N8 triple contains the audited separator flag",
)

print("\n=== Admissibility-norm status ===")
print(
    "A_G(L) = E[L^2 1_U] is the finite norm that separates washout from "
    "sector promotion.  Same-half laws are captured exactly by the audited "
    "covers. Locality alone is not enough: a local spike can have nontrivial "
    "A_G under the wrong cover.  If the relevant separator is promoted into "
    "the cover, the residue can wash out.  Direct atom targets concentrate Q "
    "mass on U and must be promoted or excluded."
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
