#!/usr/bin/env python3
"""
Paper 29 receipt: admissibility candidate norms.

Projection covariance is not an admissibility condition.  This receipt tests
three finite candidates for what an admissibility theorem must control:

1. unresolved A2 mass for a proposed committed filtration;
2. bounded local coefficient size;
3. promotion of the record-visible separator.

The audit shows that bounded local coefficient size alone is not enough:
the omitted local flag score flag5_926 at base 2 has a small coefficient
but a sector-scale unresolved A2 under the first N=8 minimal triple.  Adding
that flag to the committed filtration makes its projected residual exactly
zero.  Direct atom spikes require sector/full-atom promotion.
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


def feature_value(features, name, key):
    group, feature = name.split(":", 1)
    return features.get(group, {}).get(feature, {}).get(key, 0)


def partition_atoms(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atoms[tuple(feature_value(features, name, key) for name in names)].append(key)
    return atoms


def full_atom_partition(P):
    return {("record", key): [key] for key in P}


def q_from_record_score(P, score_by_key, base):
    weights = {key: base ** score_by_key[key] for key in P}
    normalizer = sum(P[key] * weights[key] for key in P)
    return {key: P[key] * weights[key] / normalizer for key in P}


def q_atom_spike(P, target, base):
    weights = {key: (base if key == target else 1) for key in P}
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


def residual(P, Q, atoms):
    return second_moment(P, Q) - projected_second_moment(P, Q, atoms)


def unresolved_keys(atoms):
    return [key for keys in atoms.values() if len(keys) > 1 for key in keys]


def a2_q_u(P, Q, atoms):
    U = unresolved_keys(atoms)
    L = {key: Q[key] / P[key] for key in P}
    A2 = sum(P[key] * L[key] * L[key] for key in U)
    qU = sum(Q[key] for key in U)
    return A2, qU, len(U)


def worst_atom_target(P, atoms):
    rows = []
    for keys in atoms.values():
        if len(keys) <= 1:
            continue
        p_atom = sum(P[key] for key in keys)
        for key in keys:
            limit = Fraction(1, 1) / P[key] - Fraction(1, 1) / p_atom
            rows.append((limit, key, p_atom, P[key], len(keys)))
    rows.sort(reverse=True, key=lambda row: (row[0], -row[3]))
    return rows[0]


print("=" * 80)
print("Paper 29 admissibility candidate norms")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 8
P, _Q, reps = build_projected_laws(n, weight_base=3)
features = feature_maps(P, reps, n)

known = feature_names(features, ["scalar", "interval", "regularity", "matching"])
first_n8_triple = [
    "flags4:flag4_192",
    "flags4:flag4_2248",
    "flags5:flag5_16904",
]
committed = known + first_n8_triple
atoms = partition_atoms(P, features, committed)

local_flag = "flags5:flag5_926"
local_score = feature_mapping(features, local_flag)
Q_local = q_from_record_score(P, local_score, 2)
local_before = residual(P, Q_local, atoms)
local_A2, local_qU, local_U_count = a2_q_u(P, Q_local, atoms)
promoted_atoms = partition_atoms(P, features, committed + [local_flag])
local_after = residual(P, Q_local, promoted_atoms)

worst_limit, target, p_atom, p_target, atom_size = worst_atom_target(P, atoms)
Q_atom = q_atom_spike(P, target, 10**6)
atom_before = residual(P, Q_atom, atoms)
atom_A2, atom_qU, atom_U_count = a2_q_u(P, Q_atom, atoms)
atom_after_full = residual(P, Q_atom, full_atom_partition(P))

print(f"N={n} classes={len(P)} committed_atoms={len(atoms)}/{len(P)}")
print(f"committed cover={first_n8_triple}")
print("\nlocal omitted flag score:")
print(f"  flag={local_flag} coefficient_log={mp.nstr(mp.log(2), 30)}")
print(f"  unresolved_records={local_U_count}")
print(f"  residual_before={fmt_frac(local_before, 36)}")
print(f"  A2_before={fmt_frac(local_A2, 36)}")
print(f"  Q(U)_before={fmt_frac(local_qU, 36)}")
print(f"  residual_after_promoting_flag={fmt_frac(local_after, 36)}")

print("\ndirect atom spike:")
print(f"  target={target} atom_size={atom_size}")
print(f"  P(x)={fmt_frac(p_target, 36)} P(A)={fmt_frac(p_atom, 36)}")
print(f"  exact_limit={fmt_frac(worst_limit, 36)}")
print(f"  base=1e6 residual_before={fmt_frac(atom_before, 36)}")
print(f"  base=1e6 A2_before={fmt_frac(atom_A2, 36)}")
print(f"  base=1e6 Q(U)_before={fmt_frac(atom_qU, 36)}")
print(f"  residual_after_full_atom_promotion={fmt_frac(atom_after_full, 36)}")

check(
    "bounded local coefficient size alone is not admissibility",
    local_A2 > 1000 and local_qU > Fraction(9, 10),
    f"log_coeff=log2 A2={fmt_frac(local_A2, 30)} qU={fmt_frac(local_qU, 30)}",
)
check(
    "promoting the omitted local separator kills its residual",
    local_after == 0,
    f"residual_after={fmt_frac(local_after, 30)}",
)
check(
    "direct atom spike has sector-scale unresolved A2",
    atom_A2 > worst_limit * Fraction(9, 10) and atom_qU > Fraction(9, 10),
    f"A2={fmt_frac(atom_A2, 30)} qU={fmt_frac(atom_qU, 30)}",
)
check(
    "full record-sector promotion kills atom-spike residual",
    atom_after_full == 0,
    f"residual_after_full={fmt_frac(atom_after_full, 30)}",
)
check(
    "A2 dominates projected residual in both hostile cases",
    local_before <= local_A2 and atom_before <= atom_A2,
    f"local_res={fmt_frac(local_before, 18)} atom_res={fmt_frac(atom_before, 18)}",
)

print("\n=== Admissibility status ===")
print(
    "The finite admissibility candidates split cleanly.  Projection and locality "
    "do not exclude hostile likelihoods; bounded coefficient size is also "
    "insufficient.  What works finitely is filtration-relative: large A2 residue "
    "requires promoting the separator/sector or rejecting the likelihood class."
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
