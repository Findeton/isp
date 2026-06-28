#!/usr/bin/env python3
"""
Paper 29 receipt: washout versus sector-promotion bound.

Once a committed filtration G is fixed, the exact predictive miss is

    E_P[(L - E[L|G])^2] = sum_G P(G) Var_P(L | G).

If all non-singleton G-atoms have total P-mass eps, then residue can only
matter when the likelihood is large on those rare atoms.  This gives the
finite washout/sector-promotion rule:

    residual <= E_P[L^2 1_U] <= P(U) sup_U L^2.

If the right side goes to zero, rare residue washes out.  If it persists or
diverges, it must be promoted as a record sector or excluded by admissibility.

This receipt compares three laws on the N=7 staged/fiber quotient:

1. the same-half hidden score;
2. a local record-flag spike, Q proportional to base^flag5_920;
3. a direct unresolved-atom spike.

All finite probabilities are exact Fractions.
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
    for _atom, keys in atoms.items():
        for key in keys:
            p_atoms[_atom] += P[key]
            q_atoms[_atom] += Q[key]
    return sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms)


def likelihood(P, Q):
    return {key: Q[key] / P[key] for key in P}


def residual_report(P, Q, atoms, unresolved_keys):
    L = likelihood(P, Q)
    S_full = second_moment(P, Q)
    S_G = projected_second_moment(P, Q, atoms)
    residual = S_full - S_G
    eps = sum(P[key] for key in unresolved_keys)
    u_second = sum(P[key] * L[key] * L[key] for key in unresolved_keys)
    sup_u = max(L[key] for key in unresolved_keys)
    envelope = eps * sup_u * sup_u
    q_u = sum(Q[key] for key in unresolved_keys)
    return {
        "S_full": S_full,
        "S_G": S_G,
        "capture": (S_G - 1) / (S_full - 1) if S_full != 1 else Fraction(1),
        "residual": residual,
        "eps": eps,
        "u_second": u_second,
        "sup_u": sup_u,
        "envelope": envelope,
        "q_u": q_u,
    }


def q_from_record_score(P, score_by_key, base):
    weights = {key: base ** score_by_key[key] for key in P}
    normalizer = sum(P[key] * weights[key] for key in P)
    return {key: P[key] * weights[key] / normalizer for key in P}


def q_from_target(P, target_key, base):
    weights = {key: (base if key == target_key else 1) for key in P}
    normalizer = sum(P[key] * weights[key] for key in P)
    return {key: P[key] * weights[key] / normalizer for key in P}


print("=" * 80)
print("Paper 29 washout versus sector-promotion bound")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, Q_same_half, reps = build_projected_laws(n, weight_base=3)
features = feature_maps(P, reps, n)

known = []
for group in ["scalar", "interval", "regularity", "matching"]:
    for feature_name in sorted(features[group]):
        known.append(f"{group}:{feature_name}")

fixed_four = [
    "flags3:flag3_36",
    "flags4:flag4_206",
    "flags5:flag5_17288",
    "flags4:flag4_0",
]
atoms = partition_atoms(P, features, known + fixed_four)
unresolved_atoms = [keys for keys in atoms.values() if len(keys) > 1]
unresolved_keys = [key for keys in unresolved_atoms for key in keys]
target_key = unresolved_keys[0]

flag_name = "flags5:flag5_920"
flag_score = feature_mapping(features, flag_name)

print(f"N={n} classes={len(P)}")
print(f"known+four atoms={len(atoms)}/{len(P)}")
print(
    f"unresolved atoms={len(unresolved_atoms)} unresolved_mass="
    f"{fmt_frac(sum(P[key] for key in unresolved_keys), 36)}"
)
print(f"target_key={target_key}")

same_report = residual_report(P, Q_same_half, atoms, unresolved_keys)
print("\nsame-half hidden score, base=3")
for name in ["S_full", "capture", "residual", "q_u", "u_second", "envelope"]:
    print(f"  {name}={fmt_frac(same_report[name], 36)}")

rows = []
for base in [2, 10, 1000, 10000]:
    Q_local = q_from_record_score(P, flag_score, base)
    Q_target = q_from_target(P, target_key, base)
    local = residual_report(P, Q_local, atoms, unresolved_keys)
    target = residual_report(P, Q_target, atoms, unresolved_keys)
    rows.append((base, local, target))

print("\nbase | local flag residual/capture/q_U/envelope | atom target residual/capture/q_U/envelope")
for base, local, target in rows:
    print(
        f"{base:<5} "
        f"local res={fmt_frac(local['residual'], 24)} cap={fmt_frac(local['capture'], 24)} "
        f"qU={fmt_frac(local['q_u'], 24)} env={fmt_frac(local['envelope'], 24)} | "
        f"target res={fmt_frac(target['residual'], 24)} cap={fmt_frac(target['capture'], 24)} "
        f"qU={fmt_frac(target['q_u'], 24)} env={fmt_frac(target['envelope'], 24)}"
    )

local_1000 = rows[2][1]
target_10000 = rows[3][2]

check(
    "residual identity is controlled by rare unresolved atoms for same-half",
    same_report["residual"] == 0 and same_report["u_second"] >= same_report["residual"],
    f"residual={fmt_frac(same_report['residual'], 30)}",
)
check(
    "finite washout bound holds for every audited law",
    all(
        row[1]["residual"] <= row[1]["u_second"] <= row[1]["envelope"]
        and row[2]["residual"] <= row[2]["u_second"] <= row[2]["envelope"]
        for row in rows
    ),
    "residual <= U_second <= eps sup_U^2",
)
check(
    "local flag amplification washes out under known+four in the audited range",
    local_1000["residual"] < Fraction(1, 10**12),
    f"base1000_residual={fmt_frac(local_1000['residual'], 30)}",
)
check(
    "direct atom amplification produces sector-scale residue",
    target_10000["residual"] > 100,
    f"base10000_residual={fmt_frac(target_10000['residual'], 30)}",
)
check(
    "atom target concentrates Q mass on the unresolved atom",
    target_10000["q_u"] > Fraction(3, 4),
    f"q_U={fmt_frac(target_10000['q_u'], 30)}",
)

print("\n=== Washout/sector-promotion status ===")
print(
    "For a filtration with rare non-singleton atoms, the miss is exactly a rare-atom "
    "conditional variance and is bounded by the likelihood mass living on those "
    "atoms.  Ordinary local-flag amplification washes out in the audited case, "
    "while direct atom targeting makes the rare atom carry sector-scale likelihood. "
    "That is the finite form of the admissibility fork: wash out, or promote."
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
