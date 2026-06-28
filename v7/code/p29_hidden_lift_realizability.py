#!/usr/bin/env python3
"""
Paper 29 receipt: hidden lift realizability.

Projection alone cannot exclude hostile projected laws.  If Q << P on the
committed record space, then for any hidden fiber sizes m_R we can define

    P_tilde(R,a) = P(R) / m_R,
    Q_tilde(R,a) = Q(R) / m_R,

so that the hidden likelihood is fiber-constant and

    E_{P_tilde}[L_tilde | R] = dQ/dP.

The vertical residue is exactly zero.  Therefore atom spikes and local spikes
are not ruled out by saying "they are hidden"; they are projected record laws
and require an admissibility bound, operator promotion, or sector promotion.
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


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def q_from_target(P, target_key, base):
    weights = {key: (base if key == target_key else 1) for key in P}
    normalizer = sum(P[key] * weights[key] for key in P)
    return {key: P[key] * weights[key] / normalizer for key in P}


def q_from_record_score(P, score_by_key, base):
    weights = {key: base ** score_by_key[key] for key in P}
    normalizer = sum(P[key] * weights[key] for key in P)
    return {key: P[key] * weights[key] / normalizer for key in P}


def second_moment(P, Q):
    return sum((Q[key] * Q[key]) / P[key] for key in P)


def lift_laws(P, Q):
    P_tilde = {}
    Q_tilde = {}
    fibers = {}
    for key in P:
        # Deliberately nonuniform fiber sizes to show the theorem does not rely
        # on a regular hidden presentation.
        m = 1 + (abs(int(key)) % 4)
        fibers[key] = m
        for a in range(m):
            hidden = (key, a)
            P_tilde[hidden] = P[key] / m
            Q_tilde[hidden] = Q[key] / m
    return P_tilde, Q_tilde, fibers


def projection_report(P, Q, label):
    P_tilde, Q_tilde, fibers = lift_laws(P, Q)
    L = {key: Q[key] / P[key] for key in P}
    L_tilde = {hidden: Q_tilde[hidden] / P_tilde[hidden] for hidden in P_tilde}
    conditional = {}
    vertical_square = Fraction(0)
    for key, m in fibers.items():
        cond = sum(P_tilde[(key, a)] * L_tilde[(key, a)] for a in range(m)) / P[key]
        conditional[key] = cond
        for a in range(m):
            eta = L_tilde[(key, a)] - L[key]
            vertical_square += P_tilde[(key, a)] * eta * eta
    p_push = defaultdict(Fraction)
    q_push = defaultdict(Fraction)
    for (key, _a), mass in P_tilde.items():
        p_push[key] += mass
    for (key, _a), mass in Q_tilde.items():
        q_push[key] += mass
    max_cond_gap = max(abs(conditional[key] - L[key]) for key in P)
    max_p_gap = max(abs(p_push[key] - P[key]) for key in P)
    max_q_gap = max(abs(q_push[key] - Q[key]) for key in P)
    S_record = second_moment(P, Q)
    S_hidden = second_moment(P_tilde, Q_tilde)
    print("\n" + "=" * 80)
    print(f"{label}: hidden lift realizability")
    print("=" * 80)
    print(f"records={len(P)} hidden_atoms={len(P_tilde)}")
    print(f"S_record={fmt_frac(S_record, 36)}")
    print(f"S_hidden={fmt_frac(S_hidden, 36)}")
    print(f"max_conditional_gap={fmt_frac(max_cond_gap, 36)}")
    print(f"max_pushforward_P_gap={fmt_frac(max_p_gap, 36)}")
    print(f"max_pushforward_Q_gap={fmt_frac(max_q_gap, 36)}")
    print(f"vertical_square={fmt_frac(vertical_square, 36)}")
    return {
        "label": label,
        "records": len(P),
        "hidden_atoms": len(P_tilde),
        "S_record": S_record,
        "S_hidden": S_hidden,
        "max_cond_gap": max_cond_gap,
        "max_p_gap": max_p_gap,
        "max_q_gap": max_q_gap,
        "vertical_square": vertical_square,
    }


print("=" * 80)
print("Paper 29 hidden lift realizability")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

P7, _Q7, reps7 = build_projected_laws(7, weight_base=3)
features7 = feature_maps(P7, reps7, 7)
target7 = next(iter(P7))
Q_atom7 = q_from_target(P7, target7, 10_000)
Q_local7 = q_from_record_score(P7, feature_mapping(features7, "flags5:flag5_920"), 2)

atom = projection_report(P7, Q_atom7, "N=7 atom spike")
local = projection_report(P7, Q_local7, "N=7 local flag spike")

reports = [atom, local]

check(
    "fiber-constant hidden lift projects exactly to P and Q",
    all(r["max_p_gap"] == 0 and r["max_q_gap"] == 0 for r in reports),
    "pushforward gaps are zero",
)
check(
    "record likelihood is the conditional hidden likelihood",
    all(r["max_cond_gap"] == 0 for r in reports),
    "conditional gaps are zero",
)
check(
    "fiber-constant lift has zero vertical residue",
    all(r["vertical_square"] == 0 for r in reports),
    "vertical square is zero",
)
check(
    "hidden and record second moments agree",
    all(r["S_hidden"] == r["S_record"] for r in reports),
    "S_hidden=S_record",
)
check(
    "hostile projected laws still have valid hidden lifts",
    atom["S_record"] > 100 and local["S_record"] > 1,
    f"atom_S={fmt_frac(atom['S_record'], 18)} local_S={fmt_frac(local['S_record'], 18)}",
)

print("\n=== Hidden-lift status ===")
print(
    "Every dominated projected law has a fiber-constant hidden realization with "
    "zero vertical residue.  Hostile atom/local spikes are therefore not excluded "
    "by projection alone; admissibility must be an extra physical constraint."
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
