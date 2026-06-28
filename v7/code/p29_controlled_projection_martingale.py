#!/usr/bin/env python3
"""
Paper 29 receipt: controlled projection martingale law.

This receipt proves and audits the finite predictive law suggested by the
projection-sufficiency invariant.

For a record law P, a hidden-pushforward law Q, and likelihood L=dQ/dP, every
chosen record-sector sigma-field G has a unique optimal predictor

    L_G = E_P[L | G] = Q(G-atom) / P(G-atom).

The captured second moment S_G=E_P[L_G^2] is monotone under refinement, and

    E_P[(L - L_G)^2] = S_full - S_G.

Thus a controlled click-law representation is not an arbitrary feature fit. It
is a projective likelihood martingale over a chosen sector filtration. The
missing physical theorem becomes: find a sector filtration whose increments
are controlled, summable, or compressible.

The finite audit reuses the staged/fiber projected-likelihood toy from receipt
18 and computes exact rational martingale captures for scalar, interval,
regularity, matching, and induced-suborder flag filtrations.

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


def second_moment(P, Q):
    return sum((Q[key] * Q[key]) / P[key] for key in P if Q[key] != 0)


def partition_key(features, record_key, group_names):
    if not group_names:
        return ("intercept",)
    values = []
    for group_name in group_names:
        for feature_name, mapping in sorted(features[group_name].items()):
            values.append(mapping[record_key])
    return tuple(values)


def partition_masses(P, Q, features, group_names):
    p_atoms = defaultdict(Fraction)
    q_atoms = defaultdict(Fraction)
    members = defaultdict(list)
    for record_key in P:
        atom = partition_key(features, record_key, group_names)
        p_atoms[atom] += P[record_key]
        q_atoms[atom] += Q[record_key]
        members[atom].append(record_key)
    return dict(p_atoms), dict(q_atoms), dict(members)


def martingale_capture(P, Q, features, group_names):
    p_atoms, q_atoms, members = partition_masses(P, Q, features, group_names)
    s_g = sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms)
    l_g = {atom: q_atoms[atom] / p_atoms[atom] for atom in p_atoms}
    l = {key: Q[key] / P[key] for key in P}
    residual = sum(P[key] * (l[key] - l_g[partition_key(features, key, group_names)]) ** 2 for key in P)
    max_atom_size = max(len(value) for value in members.values())
    atom_count = len(p_atoms)
    return {
        "groups": "+".join(group_names) if group_names else "intercept",
        "S": s_g,
        "residual": residual,
        "atom_count": atom_count,
        "max_atom_size": max_atom_size,
        "members": members,
        "L_G": l_g,
    }


def atom_increment_stats(prev, current):
    increment = current["S"] - prev["S"]
    return increment


def run_n(n):
    print("\n" + "=" * 80)
    print(f"Controlled projection martingale audit, N={n}")
    print("=" * 80)
    P, Q, reps = build_projected_laws(n)
    features = feature_maps(P, reps, n)
    s_full = second_moment(P, Q)
    print(f"record classes = {len(P)}")
    print(f"S_full = {fmt_frac(s_full, 42)}")

    nested = [
        [],
        ["scalar"],
        ["scalar", "interval"],
        ["scalar", "interval", "regularity"],
        ["scalar", "interval", "regularity", "matching"],
        ["scalar", "interval", "regularity", "matching", "flags3"],
        ["scalar", "interval", "regularity", "matching", "flags3", "flags4"],
        ["scalar", "interval", "regularity", "matching", "flags3", "flags4", "flags5"],
        [
            "scalar",
            "interval",
            "regularity",
            "matching",
            "flags3",
            "flags4",
            "flags5",
            "full_type",
        ],
    ]
    rows = []
    previous = None
    for groups in nested:
        row = martingale_capture(P, Q, features, groups)
        rows.append(row)
        captured = (row["S"] - 1) / (s_full - 1) if s_full != 1 else Fraction(1)
        residual = row["residual"]
        increment = row["S"] - (previous["S"] if previous is not None else Fraction(0))
        print(
            f"{row['groups']:<72} atoms={row['atom_count']:>5} "
            f"max_atom={row['max_atom_size']:>4} "
            f"S_G={fmt_frac(row['S'], 30)} "
            f"capture={fmt_frac(captured, 24)} "
            f"residual={fmt_frac(residual, 30)} "
            f"increment={fmt_frac(increment, 24)}"
        )
        previous = row

    known = rows[4]
    flag5 = rows[7]
    full_type = rows[8]
    return {
        "n": n,
        "S_full": s_full,
        "rows": rows,
        "known": known,
        "flag5": flag5,
        "full_type": full_type,
    }


print("=" * 80)
print("Paper 29 controlled projection martingale law")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

summaries = [run_n(6), run_n(7)]

monotone_ok = True
pythagoras_ok = True
for summary in summaries:
    last_s = Fraction(0)
    for row in summary["rows"]:
        monotone_ok = monotone_ok and row["S"] >= last_s
        last_s = row["S"]
        pythagoras_ok = pythagoras_ok and row["residual"] == summary["S_full"] - row["S"]

known_capture = [
    (summary["known"]["S"] - 1) / (summary["S_full"] - 1)
    for summary in summaries
]
flag5_capture = [
    (summary["flag5"]["S"] - 1) / (summary["S_full"] - 1)
    for summary in summaries
]
full_residual_max = max(summary["full_type"]["residual"] for summary in summaries)

check(
    "sector refinement gives a monotone likelihood martingale",
    monotone_ok,
    "monotone S_G in both audited N",
)
check(
    "finite Pythagorean residual identity is exact",
    pythagoras_ok,
    "residual = S_full - S_G exactly",
)
check(
    "known sectors are not stably complete in the largest audited quotient",
    known_capture[-1] < Fraction(95, 100),
    "known captures=" + ", ".join(fmt_frac(value, 20) for value in known_capture),
)
check(
    "flag refinement captures more residue in the largest audited quotient",
    flag5_capture[-1] > known_capture[-1],
    "flag5 captures=" + ", ".join(fmt_frac(value, 20) for value in flag5_capture),
)
check(
    "full record-type sector captures the likelihood exactly",
    full_residual_max == 0,
    f"max_full_residual={fmt_frac(full_residual_max, 20)}",
)

print("\n=== Predictive law status ===")
print(
    "The finite predictive law is proven: every controlled sector filtration "
    "defines an optimal likelihood martingale L_G=E[L|G].  The unknown physical "
    "content is no longer the predictor formula; it is the choice of a "
    "projective controlled filtration whose martingale increments decay, "
    "summably compress, or expose a stable missing sector."
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
