#!/usr/bin/env python3
"""
Paper 29 receipt: flag-deck reconstruction audit.

The controlled projection martingale receipt proved that once a committed
sector filtration G is chosen, the optimal predictor is forced:

    L_G = E[L | G].

This receipt asks the next Euler/Riemann question: do induced-suborder decks
look like a controlled reconstruction hierarchy, or just a disguised lookup
table?

For the finite staged/fiber toy on unlabeled 2D permutation orders, it audits:

  * pure k-flag decks;
  * known sectors plus k-flag decks;
  * ambiguity counts and residual concentration in the unresolved atoms.

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
    height,
    interval_counts,
    relation_count,
    width,
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
        for _feature_name, mapping in sorted(features[group_name].items()):
            values.append(mapping[record_key])
    return tuple(values)


def capture(P, Q, features, group_names):
    p_atoms = defaultdict(Fraction)
    q_atoms = defaultdict(Fraction)
    members = defaultdict(list)
    for record_key in P:
        atom = partition_key(features, record_key, group_names)
        p_atoms[atom] += P[record_key]
        q_atoms[atom] += Q[record_key]
        members[atom].append(record_key)

    s_g = sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms)
    l_g = {atom: q_atoms[atom] / p_atoms[atom] for atom in p_atoms}
    l = {key: Q[key] / P[key] for key in P}
    residual_by_atom = {}
    for atom, keys in members.items():
        residual_by_atom[atom] = sum(P[key] * (l[key] - l_g[atom]) ** 2 for key in keys)

    ambiguous = {atom: keys for atom, keys in members.items() if len(keys) > 1}
    max_atom = max(len(keys) for keys in members.values())
    return {
        "groups": "+".join(group_names),
        "S": s_g,
        "P_atoms": dict(p_atoms),
        "Q_atoms": dict(q_atoms),
        "members": dict(members),
        "L_G": l_g,
        "residual_by_atom": residual_by_atom,
        "ambiguous": ambiguous,
        "atom_count": len(p_atoms),
        "max_atom": max_atom,
    }


def atom_report(P, Q, reps, row, n, limit=3):
    l = {key: Q[key] / P[key] for key in P}
    ranked = sorted(
        (
            row["residual_by_atom"][atom],
            atom,
            row["members"][atom],
            row["P_atoms"][atom],
            row["Q_atoms"][atom],
        )
        for atom in row["ambiguous"]
    )
    ranked.reverse()
    lines = []
    for residual, atom, keys, p_mass, q_mass in ranked[:limit]:
        key_summaries = []
        for key in keys[:4]:
            bits = reps[key]
            key_summaries.append(
                "rel={rel},h={h},w={w},L={L},int={ints}".format(
                    rel=relation_count(bits, n),
                    h=height(bits, n),
                    w=width(bits, n),
                    L=fmt_frac(l[key], 18),
                    ints=interval_counts(bits, n)[:5],
                )
            )
        lines.append(
            {
                "residual": residual,
                "size": len(keys),
                "P": p_mass,
                "Q": q_mass,
                "summaries": key_summaries,
            }
        )
    return lines


def run_n(n):
    print("\n" + "=" * 80)
    print(f"Flag-deck reconstruction audit, N={n}")
    print("=" * 80)
    P, Q, reps = build_projected_laws(n)
    features = feature_maps(P, reps, n)
    s_full = second_moment(P, Q)
    print(f"record classes = {len(P)}")
    print(f"S_full = {fmt_frac(s_full, 42)}")

    known = ["scalar", "interval", "regularity", "matching"]
    filtrations = [
        ("flags3", ["flags3"]),
        ("flags4", ["flags4"]),
        ("flags5", ["flags5"]),
        ("known", known),
        ("known+flags3", known + ["flags3"]),
        ("known+flags4", known + ["flags3", "flags4"]),
        ("known+flags5", known + ["flags3", "flags4", "flags5"]),
    ]

    rows = {}
    for label, groups in filtrations:
        row = capture(P, Q, features, groups)
        rows[label] = row
        captured = (row["S"] - 1) / (s_full - 1)
        residual = s_full - row["S"]
        print(
            f"{label:<16} atoms={row['atom_count']:>5} "
            f"ambiguous={len(row['ambiguous']):>5} max_atom={row['max_atom']:>3} "
            f"capture={fmt_frac(captured, 24)} residual={fmt_frac(residual, 30)}"
        )

    selected = "known+flags4" if n == 7 else "flags4"
    print(f"\nTop ambiguous atoms for {selected}:")
    for item in atom_report(P, Q, reps, rows[selected], n):
        print(
            f"  size={item['size']} residual={fmt_frac(item['residual'], 30)} "
            f"P={fmt_frac(item['P'], 24)} Q={fmt_frac(item['Q'], 24)}"
        )
        for summary in item["summaries"]:
            print(f"    {summary}")

    return {
        "n": n,
        "classes": len(P),
        "S_full": s_full,
        "rows": rows,
    }


print("=" * 80)
print("Paper 29 flag-deck reconstruction audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

summaries = [run_n(6), run_n(7)]

n6 = summaries[0]["rows"]
n7 = summaries[1]["rows"]

check(
    "pure 4-flag deck reconstructs the N=6 audited quotient",
    n6["flags4"]["atom_count"] == summaries[0]["classes"] and len(n6["flags4"]["ambiguous"]) == 0,
    f"atoms={n6['flags4']['atom_count']} classes={summaries[0]['classes']}",
)
check(
    "pure 5-flag deck reconstructs the N=7 audited quotient",
    n7["flags5"]["atom_count"] == summaries[1]["classes"] and len(n7["flags5"]["ambiguous"]) == 0,
    f"atoms={n7['flags5']['atom_count']} classes={summaries[1]['classes']}",
)
check(
    "pure 4-flag deck is not exact at N=7",
    n7["flags4"]["atom_count"] < summaries[1]["classes"] and len(n7["flags4"]["ambiguous"]) > 0,
    f"atoms={n7['flags4']['atom_count']} ambiguous={len(n7['flags4']['ambiguous'])}",
)
check(
    "known plus 4-flags leaves exactly one N=7 ambiguity",
    n7["known+flags4"]["atom_count"] == summaries[1]["classes"] - 1
    and len(n7["known+flags4"]["ambiguous"]) == 1
    and n7["known+flags4"]["max_atom"] == 2,
    f"atoms={n7['known+flags4']['atom_count']} ambiguous={len(n7['known+flags4']['ambiguous'])}",
)
check(
    "known plus 5-flags reconstructs the N=7 likelihood exactly",
    n7["known+flags5"]["S"] == summaries[1]["S_full"],
    f"residual={fmt_frac(summaries[1]['S_full'] - n7['known+flags5']['S'], 24)}",
)

print("\n=== Reconstruction status ===")
print(
    "The audited toy supports a sharper target than a scalar action: induced "
    "suborder decks behave like a reconstruction filtration.  In the N=7 "
    "quotient, known+4-flags leave a single two-record ambiguity with tiny "
    "likelihood residue, and 5-flags reconstruct exactly.  This is finite "
    "evidence for a flag-deck/projection theorem, not yet an asymptotic proof."
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
