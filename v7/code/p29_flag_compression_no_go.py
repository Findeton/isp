#!/usr/bin/env python3
"""
Paper 29 receipt: flag compression no-go.

Receipts 19-21 show that induced-suborder decks repair the staged/fiber
projected likelihood in the finite toy.  This receipt performs the hostile
compression audit: is the repair a genuine compact action, or mostly a
lookup-table refinement of record atoms?

For N=7 it compares:

  * exact martingale capture by the sector sigma-field;
  * atom count as a fraction of all record classes;
  * weighted linear projection R^2 of log L onto the same feature counts.

If exact capture is near one while linear R^2 remains far from one and the
atom fraction is close to one, the "flag solution" is not yet a predictive
law.  It is a reconstruction filtration awaiting coefficient decay,
renormalization, or compression.

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
    project_log_likelihood,
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


def martingale_capture(P, Q, features, group_names):
    p_atoms = defaultdict(Fraction)
    q_atoms = defaultdict(Fraction)
    members = defaultdict(list)
    for record_key in P:
        atom = partition_key(features, record_key, group_names)
        p_atoms[atom] += P[record_key]
        q_atoms[atom] += Q[record_key]
        members[atom].append(record_key)
    s_g = sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms)
    return {
        "S": s_g,
        "atom_count": len(p_atoms),
        "max_atom": max(len(keys) for keys in members.values()),
        "ambiguous": sum(1 for keys in members.values() if len(keys) > 1),
    }


def audit_row(P, Q, features, label, groups):
    s_full = second_moment(P, Q)
    exact = martingale_capture(P, Q, features, groups)
    linear = project_log_likelihood(P, Q, features, groups)
    capture = (exact["S"] - 1) / (s_full - 1)
    atom_fraction = Fraction(exact["atom_count"], len(P))
    print(
        f"{label:<18} atoms={exact['atom_count']:>5}/{len(P)} "
        f"atom_frac={fmt_frac(atom_fraction, 18)} max_atom={exact['max_atom']:>3} "
        f"ambig={exact['ambiguous']:>5} exact_capture={fmt_frac(capture, 24)} "
        f"linear_rank={linear['rank']:>3} linear_R2={fmt(linear['r2'], 24)}"
    )
    return {
        "label": label,
        "groups": groups,
        "exact": exact,
        "linear": linear,
        "capture": capture,
        "atom_fraction": atom_fraction,
    }


print("=" * 80)
print("Paper 29 flag compression no-go")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, Q, reps = build_projected_laws(n)
features = feature_maps(P, reps, n)
s_full = second_moment(P, Q)
print(f"N={n} record classes={len(P)} S_full={fmt_frac(s_full, 42)}")

known = ["scalar", "interval", "regularity", "matching"]
rows = {}
for label, groups in [
    ("flags3", ["flags3"]),
    ("flags4", ["flags4"]),
    ("flags5", ["flags5"]),
    ("known", known),
    ("known+flags3", known + ["flags3"]),
    ("known+flags4", known + ["flags3", "flags4"]),
    ("known+flags5", known + ["flags3", "flags4", "flags5"]),
]:
    rows[label] = audit_row(P, Q, features, label, groups)

check(
    "exact known-plus-3 flag capture is high but atom-heavy",
    rows["known+flags3"]["capture"] > Fraction(99, 100)
    and rows["known+flags3"]["atom_fraction"] > Fraction(95, 100),
    "capture={c} atom_fraction={a}".format(
        c=fmt_frac(rows["known+flags3"]["capture"], 20),
        a=fmt_frac(rows["known+flags3"]["atom_fraction"], 20),
    ),
)
check(
    "linear known-plus-5 flag action still misses substantial log-likelihood variance",
    rows["known+flags5"]["linear"]["r2"] < mp.mpf("0.9"),
    f"linear_R2={fmt(rows['known+flags5']['linear']['r2'], 24)}",
)
check(
    "exact known-plus-4 flag capture is near lookup-table resolution",
    rows["known+flags4"]["atom_fraction"] > Fraction(999, 1000)
    and rows["known+flags4"]["capture"] > Fraction(999999, 1000000),
    "capture={c} atom_fraction={a}".format(
        c=fmt_frac(rows["known+flags4"]["capture"], 24),
        a=fmt_frac(rows["known+flags4"]["atom_fraction"], 24),
    ),
)
check(
    "pure 3-flag deck gives nontrivial compression but not a full law",
    rows["flags3"]["capture"] > Fraction(9, 10)
    and rows["flags3"]["capture"] < Fraction(99, 100)
    and rows["flags3"]["atom_fraction"] < Fraction(4, 5),
    "capture={c} atom_fraction={a}".format(
        c=fmt_frac(rows["flags3"]["capture"], 20),
        a=fmt_frac(rows["flags3"]["atom_fraction"], 20),
    ),
)

print("\n=== Compression status ===")
print(
    "The finite flag repair is real but not yet a compact law.  Exact flag "
    "martingales can become nearly atom-resolving, while the corresponding "
    "linear/action projection of log L still misses visible variance.  The "
    "next theorem must control martingale increments or coefficient decay; "
    "finite deck exactness alone is too close to a lookup table."
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
