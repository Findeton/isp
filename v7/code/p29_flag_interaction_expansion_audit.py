#!/usr/bin/env python3
"""
Paper 29 receipt: flag interaction expansion audit.

The operator-family audit showed that coarse geometric grouping of flags is
too lossy, while exact flag decks are too atom-like.  This receipt follows the
next opening: perhaps the compact law is not linear in flag counts, but an
operator-product expansion in low-order local types.

For the N=7 staged/fiber toy, it adds:

  * quadratic products of exact 3-flag counts;
  * interactions between known sectors and exact 3-flag counts;
  * quadratic products of exact 4-flag counts.

The exact martingale partition is unchanged by deterministic products of an
existing feature vector, but the linear/action projection of log L may improve.
That distinguishes "need nonlinear action" from "need new information".

All finite probabilities are exact Fractions.  Decimal reporting uses mpmath
with dps=140.
"""

import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    build_projected_laws,
    feature_maps,
    fmt,
    project_log_likelihood,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def product_group(features, group_a, group_b, record_keys, name, triangular=False):
    out = {}
    items_a = sorted(features[group_a].items())
    items_b = sorted(features[group_b].items())
    for i, (name_a, map_a) in enumerate(items_a):
        start = i if triangular and group_a == group_b else 0
        for j, (name_b, map_b) in enumerate(items_b[start:], start=start):
            feature_name = f"{name}:{name_a}*{name_b}"
            out[feature_name] = {
                key: map_a[key] * map_b[key]
                for key in record_keys
            }
    return out


def run_projection(P, Q, features, label, groups):
    result = project_log_likelihood(P, Q, features, groups)
    feature_count = sum(len(features[group]) for group in groups)
    print(
        f"{label:<32} features={feature_count:>4} rank={result['rank']:>4} "
        f"R2={fmt(result['r2'], 24)} residual_norm={fmt(result['residual_norm'], 24)} "
        f"max_abs={fmt(result['max_abs_residual'], 24)}"
    )
    return result


print("=" * 80)
print("Paper 29 flag interaction expansion audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, Q, reps = build_projected_laws(n)
features = feature_maps(P, reps, n)
record_keys = list(P)

known_groups = ["scalar", "interval", "regularity", "matching"]
features["flags3_quad"] = product_group(features, "flags3", "flags3", record_keys, "q33", triangular=True)
features["known_flags3_cross"] = {}
for group in known_groups:
    features[f"{group}_flags3_cross"] = product_group(
        features, group, "flags3", record_keys, f"{group}x3", triangular=False
    )
    features["known_flags3_cross"].update(features[f"{group}_flags3_cross"])
features["flags4_quad"] = product_group(features, "flags4", "flags4", record_keys, "q44", triangular=True)

rows = {}
specs = [
    ("known", known_groups),
    ("flags3", ["flags3"]),
    ("known+flags3", known_groups + ["flags3"]),
    ("flags3+quad", ["flags3", "flags3_quad"]),
    ("known+flags3+quad", known_groups + ["flags3", "flags3_quad"]),
    ("known+flags3+cross", known_groups + ["flags3", "known_flags3_cross"]),
    (
        "known+flags3+quad+cross",
        known_groups + ["flags3", "flags3_quad", "known_flags3_cross"],
    ),
    ("flags4", ["flags4"]),
    ("flags4+quad", ["flags4", "flags4_quad"]),
    ("known+flags4", known_groups + ["flags3", "flags4"]),
    ("known+flags5", known_groups + ["flags3", "flags4", "flags5"]),
]

for label, groups in specs:
    rows[label] = run_projection(P, Q, features, label, groups)

check(
    "quadratic 3-flag products improve the linear flag action",
    rows["flags3+quad"]["r2"] > rows["flags3"]["r2"],
    f"linear={fmt(rows['flags3']['r2'], 20)} quad={fmt(rows['flags3+quad']['r2'], 20)}",
)
check(
    "known-by-3-flag interactions improve over known plus linear 3-flags",
    rows["known+flags3+cross"]["r2"] > rows["known+flags3"]["r2"],
    f"linear={fmt(rows['known+flags3']['r2'], 20)} cross={fmt(rows['known+flags3+cross']['r2'], 20)}",
)
check(
    "quadratic 4-flag products improve over linear 4-flags",
    rows["flags4+quad"]["r2"] > rows["flags4"]["r2"],
    f"linear={fmt(rows['flags4']['r2'], 20)} quad={fmt(rows['flags4+quad']['r2'], 20)}",
)
check(
    "quadratic interaction action is still not an exact compact law",
    rows["known+flags3+quad+cross"]["r2"] < mp.mpf("0.9"),
    f"R2={fmt(rows['known+flags3+quad+cross']['r2'], 24)}",
)
check(
    "full known plus 5-flag linear action still beats low-order interactions",
    rows["known+flags5"]["r2"] > rows["known+flags3+quad+cross"]["r2"],
    "known5={k5} interaction={ix}".format(
        k5=fmt(rows["known+flags5"]["r2"], 20),
        ix=fmt(rows["known+flags3+quad+cross"]["r2"], 20),
    ),
)

print("\n=== Interaction status ===")
print(
    "Low-order operator products are real: quadratic and cross terms improve "
    "the linear action.  But they do not close the gap.  The audited toy still "
    "requires either higher-order products, higher flags, or a principled "
    "renormalized operator basis."
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
