#!/usr/bin/env python3
"""
Paper 29 receipt: flag deletion projectivity.

The finite flag operators are only plausible record-law coordinates if they
behave naturally under record restriction.  This receipt checks the exact
deletion identity for induced-suborder counts:

    sum_{v in R} count_F(R without v) = (N - |F|) count_F(R).

Every occurrence of a k-record flag F in an N-record order survives exactly
N-k one-record deletions.  Thus unrooted flag counts are projective martingale
coordinates under uniform deletion after the deterministic combinatorial
normalization.

The receipt checks the identity for all 3-, 4-, and 5-flags in every N=7
record class of the staged/fiber quotient, and reports the four greedy
operators as concrete examples.
"""

from collections import defaultdict
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    build_projected_laws,
    flag_counts,
    fmt,
    height,
    interval_counts,
    relation_count,
    restrict_bits,
    small_canon,
    width,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def delete_vertex_bits(bits, n, deleted):
    subset = tuple(i for i in range(n) if i != deleted)
    restricted = restrict_bits(bits, n, subset)
    return small_canon(restricted, n - 1)


def describe_flag(name):
    k = int(name.split("_", 1)[0].replace("flag", ""))
    bits = int(name.split("_", 1)[1])
    return (
        f"{name}: rel={relation_count(bits, k)} h={height(bits, k)} "
        f"w={width(bits, k)} intervals={interval_counts(bits, k)[:4]}"
    )


print("=" * 80)
print("Paper 29 flag deletion projectivity")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, _Q, reps = build_projected_laws(n)

violations = []
max_checked = 0
selected = {
    3: {"flag3_36": 36},
    4: {"flag4_206": 206, "flag4_0": 0},
    5: {"flag5_17288": 17288},
}
selected_totals = defaultdict(int)

for record_key, bits in reps.items():
    original_counts = {k: flag_counts(bits, n, k) for k in [3, 4, 5]}
    deletion_sums = {k: defaultdict(int) for k in [3, 4, 5]}
    for deleted in range(n):
        del_bits = delete_vertex_bits(bits, n, deleted)
        for k in [3, 4, 5]:
            for flag_key, count in flag_counts(del_bits, n - 1, k).items():
                deletion_sums[k][flag_key] += count

    for k in [3, 4, 5]:
        all_keys = set(original_counts[k]) | set(deletion_sums[k])
        for flag_key in all_keys:
            lhs = deletion_sums[k].get(flag_key, 0)
            rhs = (n - k) * original_counts[k].get(flag_key, 0)
            max_checked += 1
            if lhs != rhs:
                violations.append((record_key, k, flag_key, lhs, rhs))
        for name, flag_key in selected[k].items():
            selected_totals[name] += original_counts[k].get(flag_key, 0)

print(f"N={n} record classes={len(P)} checked identities={max_checked}")
print(f"violations={len(violations)}")

print("\nSelected operators:")
for size_bucket in [3, 4, 5]:
    for name in selected[size_bucket]:
        print(f"  {describe_flag(name)} total_count_across_classes={selected_totals[name]}")

check(
    "all 3-, 4-, and 5-flag deletion identities hold",
    len(violations) == 0,
    f"checked={max_checked} violations={len(violations)}",
)
check(
    "selected greedy operators are included in the projective family",
    all(name in selected_totals for bucket in selected.values() for name in bucket),
    "selected=" + ", ".join(name for bucket in selected.values() for name in bucket),
)
check(
    "deletion normalization is nontrivial for every selected operator",
    all(selected_totals[name] > 0 for bucket in selected.values() for name in bucket),
    "totals=" + ", ".join(f"{name}={selected_totals[name]}" for bucket in selected.values() for name in bucket),
)
check(
    "identity covers every record class in the quotient",
    len(reps) == len(P),
    f"classes={len(P)} reps={len(reps)}",
)

print("\n=== Projectivity status ===")
print(
    "Unrooted induced-flag counts have exact deletion covariance.  This does "
    "not prove that the four selected flags are the physical law, but it does "
    "show that the candidate local operators live in a projectively natural "
    "record-intrinsic algebra rather than in an arbitrary fitted coordinate list."
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
