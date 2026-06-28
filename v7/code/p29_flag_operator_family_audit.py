#!/usr/bin/env python3
"""
Paper 29 receipt: flag operator-family audit.

The previous receipt showed that exact induced-suborder decks can reconstruct
the finite staged/fiber toy, but that exact decks are too close to a lookup
table.  This receipt tests the next natural rescue:

    group flags into geometric/operator families.

For each induced k-suborder flag, we build compressed families such as

    (relation count, height, width)
    (relation count, height, width, interval profile)
    (relation count, height, width, interval profile, degree moments)

and compare them against exact flag decks.  The audit reports both exact
martingale capture and weighted linear/action R^2 for log L.

All finite probabilities are exact Fractions.  Decimal reporting uses mpmath
with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    build_projected_laws,
    degree_moments,
    feature_maps,
    fmt,
    fmt_frac,
    height,
    interval_counts,
    project_log_likelihood,
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
        "max_atom": max(len(value) for value in members.values()),
        "ambiguous": sum(1 for value in members.values() if len(value) > 1),
    }


def flag_bits_from_name(name):
    return int(name.split("_", 1)[1])


def descriptor(bits, k, mode):
    rel = relation_count(bits, k)
    h = height(bits, k)
    w = width(bits, k)
    if mode == "rhw":
        return rel, h, w
    intervals = tuple(interval_counts(bits, k))
    if mode == "rhw_interval":
        return rel, h, w, intervals
    deg = degree_moments(bits, k)
    if mode == "rhw_interval_degree":
        return rel, h, w, intervals, deg
    raise ValueError(mode)


def add_grouped_flag_features(features, record_keys, k, mode):
    source = features[f"flags{k}"]
    grouped = defaultdict(lambda: {key: 0 for key in record_keys})
    for flag_name, mapping in source.items():
        bits = flag_bits_from_name(flag_name)
        desc = descriptor(bits, k, mode)
        grouped[f"flag{k}_{mode}_{desc}"]
        for record_key, count in mapping.items():
            grouped[f"flag{k}_{mode}_{desc}"][record_key] += count
    return dict(grouped)


def audit_row(P, Q, features, label, group_names):
    s_full = second_moment(P, Q)
    exact = martingale_capture(P, Q, features, group_names)
    linear = project_log_likelihood(P, Q, features, group_names)
    capture = (exact["S"] - 1) / (s_full - 1)
    atom_fraction = Fraction(exact["atom_count"], len(P))
    feature_count = sum(len(features[group]) for group in group_names)
    print(
        f"{label:<34} features={feature_count:>4} atoms={exact['atom_count']:>5}/{len(P)} "
        f"atom_frac={fmt_frac(atom_fraction, 18)} max_atom={exact['max_atom']:>3} "
        f"capture={fmt_frac(capture, 24)} linear_rank={linear['rank']:>3} "
        f"linear_R2={fmt(linear['r2'], 24)}"
    )
    return {
        "capture": capture,
        "atom_fraction": atom_fraction,
        "exact": exact,
        "linear": linear,
        "feature_count": feature_count,
    }


print("=" * 80)
print("Paper 29 flag operator-family audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, Q, reps = build_projected_laws(n)
features = feature_maps(P, reps, n)
record_keys = list(P)
for mode in ["rhw", "rhw_interval", "rhw_interval_degree"]:
    for k in [3, 4, 5]:
        features[f"geom{k}_{mode}"] = add_grouped_flag_features(features, record_keys, k, mode)

s_full = second_moment(P, Q)
print(f"N={n} record classes={len(P)} S_full={fmt_frac(s_full, 42)}")

known = ["scalar", "interval", "regularity", "matching"]
rows = {}
specs = [
    ("known", known),
    ("rhw_345", ["geom3_rhw", "geom4_rhw", "geom5_rhw"]),
    ("known+rhw_345", known + ["geom3_rhw", "geom4_rhw", "geom5_rhw"]),
    ("intgeom_345", ["geom3_rhw_interval", "geom4_rhw_interval", "geom5_rhw_interval"]),
    (
        "known+intgeom_345",
        known + ["geom3_rhw_interval", "geom4_rhw_interval", "geom5_rhw_interval"],
    ),
    (
        "degreegeom_345",
        ["geom3_rhw_interval_degree", "geom4_rhw_interval_degree", "geom5_rhw_interval_degree"],
    ),
    (
        "known+degreegeom_345",
        known
        + ["geom3_rhw_interval_degree", "geom4_rhw_interval_degree", "geom5_rhw_interval_degree"],
    ),
    ("exact_flags3", ["flags3"]),
    ("exact_flags4", ["flags4"]),
    ("exact_flags5", ["flags5"]),
    ("known+exact_flags3", known + ["flags3"]),
    ("known+exact_flags4", known + ["flags3", "flags4"]),
    ("known+exact_flags5", known + ["flags3", "flags4", "flags5"]),
]

for label, groups in specs:
    rows[label] = audit_row(P, Q, features, label, groups)

check(
    "coarse rhw families compress strongly but miss most residue",
    rows["known+rhw_345"]["atom_fraction"] < Fraction(3, 4)
    and rows["known+rhw_345"]["capture"] < Fraction(4, 5),
    "capture={c} atom_fraction={a}".format(
        c=fmt_frac(rows["known+rhw_345"]["capture"], 20),
        a=fmt_frac(rows["known+rhw_345"]["atom_fraction"], 20),
    ),
)
check(
    "interval geometry families improve over known sectors",
    rows["known+intgeom_345"]["capture"] > rows["known"]["capture"],
    "known={k} intgeom={g}".format(
        k=fmt_frac(rows["known"]["capture"], 20),
        g=fmt_frac(rows["known+intgeom_345"]["capture"], 20),
    ),
)
check(
    "degree-refined geometry is still not enough as a compact law",
    rows["known+degreegeom_345"]["capture"] < Fraction(95, 100),
    "capture={c} atom_fraction={a}".format(
        c=fmt_frac(rows["known+degreegeom_345"]["capture"], 20),
        a=fmt_frac(rows["known+degreegeom_345"]["atom_fraction"], 20),
    ),
)
check(
    "exact flags outperform all audited grouped operator families",
    rows["known+exact_flags3"]["capture"] > rows["known+degreegeom_345"]["capture"],
    "exact3={e} degreegeom={g}".format(
        e=fmt_frac(rows["known+exact_flags3"]["capture"], 20),
        g=fmt_frac(rows["known+degreegeom_345"]["capture"], 20),
    ),
)
check(
    "grouped operator-family linear action remains below exact flag linear action",
    rows["known+degreegeom_345"]["linear"]["r2"] < rows["known+exact_flags5"]["linear"]["r2"],
    "grouped_R2={r} exact_flag_R2={e}".format(
        r=fmt(rows["known+degreegeom_345"]["linear"]["r2"], 20),
        e=fmt(rows["known+exact_flags5"]["linear"]["r2"], 20),
    ),
)

print("\n=== Operator-family status ===")
print(
    "Simple geometric grouping of flags is informative but not enough.  The "
    "audited likelihood is sensitive to finer induced-suborder type than "
    "relation/height/width/interval/degree summaries.  A predictive law needs "
    "a renormalized operator basis or decay theorem, not only coarse geometric "
    "flag families."
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
