#!/usr/bin/env python3
"""
Paper 29 receipt: N=8 transfer and nullspace growth.

N=7 showed that known+four exactly determines the same-half score polynomial
while leaving one rare two-record atom unresolved.  This receipt asks whether
that phenomenon transfers to N=8.

It checks:

1. the same fixed four operators still determine the same-half score polynomial;
2. the same fixed four close the base-3 projected likelihood;
3. the unresolved nullspace grows from one rare pair to a still-small rare
   collection;
4. the literal operator order is not canonical, because a fresh greedy search
   at N=8 finds different first operators.

All finite probabilities and score polynomials are exact Fractions.
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
    same_block_score,
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


def partition_atoms(P, features, feature_names):
    atoms = defaultdict(list)
    for key in P:
        atom = tuple(feature_mapping(features, name)[key] for name in feature_names)
        atoms[atom].append(key)
    return atoms


def second_moment(P, Q):
    return sum((Q[key] * Q[key]) / P[key] for key in P if Q[key] != 0)


def capture_from_names(P, Q, features, feature_names):
    p_atoms = defaultdict(Fraction)
    q_atoms = defaultdict(Fraction)
    for key in P:
        atom = tuple(feature_mapping(features, name)[key] for name in feature_names)
        p_atoms[atom] += P[key]
        q_atoms[atom] += Q[key]
    return sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms), len(p_atoms)


def build_score_polynomials(n):
    p_counts = defaultdict(int)
    polys = defaultdict(lambda: [0 for _ in range(n + 1)])
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        score = same_block_score(pi)
        p_counts[key] += 1
        polys[key][score] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    return P, dict(polys), dict(p_counts), reps


def normalized_poly(poly, count):
    return tuple(Fraction(coeff, count) for coeff in poly)


def polynomial_violations(P, features, feature_names, normalized):
    atoms = partition_atoms(P, features, feature_names)
    bad = []
    for atom, keys in atoms.items():
        first = normalized[keys[0]]
        if any(normalized[key] != first for key in keys[1:]):
            bad.append((atom, keys))
    return atoms, bad


def conditional_variance(P, atoms, mapping):
    total = Fraction(0)
    active_atoms = []
    for atom, keys in atoms.items():
        if len(keys) == 1:
            continue
        first = mapping[keys[0]]
        if all(mapping[key] == first for key in keys[1:]):
            continue
        p_atom = sum(P[key] for key in keys)
        sum_x = sum(P[key] * mapping[key] for key in keys)
        sum_x2 = sum(P[key] * mapping[key] * mapping[key] for key in keys)
        var_mass = sum_x2 - (sum_x * sum_x) / p_atom
        total += var_mass
        active_atoms.append((atom, keys, var_mass))
    return total, active_atoms


def greedy_steps(P, Q, features, known_features, candidate_features, steps=6):
    selected = list(known_features)
    remaining = list(candidate_features)
    s_full = second_moment(P, Q)
    rows = []
    for step in range(1, steps + 1):
        best = None
        for candidate in remaining:
            s_g, atom_count = capture_from_names(P, Q, features, selected + [candidate])
            if best is None or s_g > best["s_g"]:
                best = {"name": candidate, "s_g": s_g, "atom_count": atom_count}
        selected.append(best["name"])
        remaining = [candidate for candidate in remaining if candidate != best["name"]]
        capture = (best["s_g"] - 1) / (s_full - 1)
        rows.append((step, best["name"], capture, best["atom_count"]))
    return rows


print("=" * 80)
print("Paper 29 N=8 transfer and nullspace growth")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 8
P, Q, reps = build_projected_laws(n)
features = feature_maps(P, reps, n)
_P_poly, polys, p_counts, _reps_poly = build_score_polynomials(n)
normalized = {key: normalized_poly(polys[key], p_counts[key]) for key in P}

known_features = []
for group in ["scalar", "interval", "regularity", "matching"]:
    for feature_name in sorted(features[group]):
        known_features.append(f"{group}:{feature_name}")

fixed_four = [
    "flags3:flag3_36",
    "flags4:flag4_206",
    "flags5:flag5_17288",
    "flags4:flag4_0",
]

candidate_features = []
for group in ["flags3", "flags4", "flags5"]:
    for feature_name in sorted(features[group]):
        candidate_features.append(f"{group}:{feature_name}")

s_full = second_moment(P, Q)
s_known, known_atom_count = capture_from_names(P, Q, features, known_features)
s_fixed, fixed_atom_count = capture_from_names(P, Q, features, known_features + fixed_four)
known_capture = (s_known - 1) / (s_full - 1)
fixed_capture = (s_fixed - 1) / (s_full - 1)

fixed_atoms, fixed_poly_bad = polynomial_violations(
    P, features, known_features + fixed_four, normalized
)
unresolved_atoms = [keys for keys in fixed_atoms.values() if len(keys) > 1]
unresolved_mass = sum(P[key] for keys in unresolved_atoms for key in keys)
max_unresolved_size = max(len(keys) for keys in unresolved_atoms)

invisible_flags = []
for name in candidate_features:
    if name in fixed_four:
        continue
    mapping = feature_mapping(features, name)
    variance, active_atoms = conditional_variance(P, fixed_atoms, mapping)
    if variance:
        invisible_flags.append((variance, name, len(active_atoms)))
invisible_flags.sort(reverse=True, key=lambda row: (row[0], row[1]))

greedy = greedy_steps(P, Q, features, known_features, candidate_features, steps=6)

print(f"N={n} record classes={len(P)}")
print(f"S_full={fmt_frac(s_full, 36)}")
print(f"known capture={fmt_frac(known_capture, 30)} atoms={known_atom_count}/{len(P)}")
print(f"fixed-four capture={fmt_frac(fixed_capture, 30)} atoms={fixed_atom_count}/{len(P)}")
print(f"fixed-four polynomial bad atoms={len(fixed_poly_bad)}")
print(
    f"unresolved atoms={len(unresolved_atoms)} max_size={max_unresolved_size} "
    f"mass={fmt_frac(unresolved_mass, 36)}"
)
print(f"invisible local flags={len(invisible_flags)}")
print("top invisible flags:")
for variance, name, active_count in invisible_flags[:8]:
    print(f"  {name} variance={fmt_frac(variance, 30)} active_atoms={active_count}")

print("fresh greedy:")
for step, name, capture, atom_count in greedy:
    print(f"  step={step} {name} capture={fmt_frac(capture, 30)} atoms={atom_count}/{len(P)}")

check(
    "fixed four transfer to exact N=8 same-half likelihood",
    fixed_capture == 1 and len(fixed_poly_bad) == 0,
    f"capture={fmt_frac(fixed_capture, 24)} poly_bad={len(fixed_poly_bad)}",
)
check(
    "known sectors are already strong but not exact at N=8",
    known_capture < 1 and known_capture > Fraction(999, 1000),
    f"known_capture={fmt_frac(known_capture, 24)}",
)
check(
    "N=8 fixed-four nullspace remains rare",
    unresolved_mass < Fraction(1, 100),
    f"unresolved_mass={fmt_frac(unresolved_mass, 30)} atoms={len(unresolved_atoms)}",
)
check(
    "literal greedy operator order is not stable from N=7 to N=8",
    greedy[0][1] != fixed_four[0],
    f"first_N8={greedy[0][1]} first_N7={fixed_four[0]}",
)
check(
    "fresh greedy reaches exact capture with bounded small operator count",
    any(capture == 1 for _step, _name, capture, _atoms in greedy[:6]),
    "captures=" + ", ".join(fmt_frac(row[2], 8) for row in greedy),
)

print("\n=== N=8 status ===")
print(
    "The fixed four operators transfer strongly: they determine the same-half "
    "projected polynomial at N=8 and close the base-3 likelihood.  But their "
    "literal greedy priority is not stable, and the unresolved nullspace grows "
    "from one rare pair to a small rare family.  The law target is therefore a "
    "bounded controlled local-operator filtration, not a canonical four-name list."
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
