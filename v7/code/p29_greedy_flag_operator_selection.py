#!/usr/bin/env python3
"""
Paper 29 receipt: greedy flag-operator selection.

Coarse geometric flag families were too lossy, while exact decks were too
atom-like.  Quadratic interactions improved the linear action but did not close
the gap.  This receipt asks a sharper compression question:

    Is the projected likelihood residue carried by a small subset of exact
    local flag operators?

Starting from the known scalar/interval/regularity/matching filtration at N=7,
it greedily adds individual exact 3-, 4-, and 5-flag count operators to maximize
the exact martingale second moment S_G.  It reports the selected operators and
the captured chi-square fraction after each step.

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


def capture_from_features(P, Q, selected):
    p_atoms = defaultdict(Fraction)
    q_atoms = defaultdict(Fraction)
    counts = defaultdict(int)
    for record_key in P:
        atom = tuple(mapping[record_key] for _name, mapping in selected)
        p_atoms[atom] += P[record_key]
        q_atoms[atom] += Q[record_key]
        counts[atom] += 1
    s_g = sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms)
    return s_g, len(p_atoms), max(counts.values())


def flag_bits(name):
    return int(name.split("_", 1)[1])


def flag_size(name):
    return int(name.split("_", 1)[0].replace("flag", ""))


def describe_flag(name):
    k = flag_size(name)
    bits = flag_bits(name)
    return (
        f"{name} rel={relation_count(bits, k)} h={height(bits, k)} "
        f"w={width(bits, k)} intervals={interval_counts(bits, k)[:4]}"
    )


print("=" * 80)
print("Paper 29 greedy flag-operator selection")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7
P, Q, reps = build_projected_laws(n)
features = feature_maps(P, reps, n)
s_full = second_moment(P, Q)

known_groups = ["scalar", "interval", "regularity", "matching"]
base = []
for group in known_groups:
    for name, mapping in sorted(features[group].items()):
        base.append((f"{group}:{name}", mapping))

candidates = []
for group in ["flags3", "flags4", "flags5"]:
    for name, mapping in sorted(features[group].items()):
        candidates.append((f"{group}:{name}", mapping))

selected = list(base)
base_s, base_atoms, _base_max_atom = capture_from_features(P, Q, selected)
print(f"N={n} record classes={len(P)} S_full={fmt_frac(s_full, 42)}")
print(
    f"base known capture={fmt_frac((base_s - 1) / (s_full - 1), 24)} "
    f"atoms={base_atoms}/{len(P)}"
)

rows = []
remaining = list(candidates)
for step in range(1, 13):
    best = None
    for candidate in remaining:
        s_g, atoms, max_atom = capture_from_features(P, Q, selected + [candidate])
        if best is None or s_g > best["S"]:
            best = {"candidate": candidate, "S": s_g, "atoms": atoms, "max_atom": max_atom}
    selected.append(best["candidate"])
    remaining = [candidate for candidate in remaining if candidate[0] != best["candidate"][0]]
    captured = (best["S"] - 1) / (s_full - 1)
    rows.append((step, best, captured))
    print(
        f"step={step:02d} capture={fmt_frac(captured, 24)} "
        f"atoms={best['atoms']}/{len(P)} max_atom={best['max_atom']} "
        f"selected={describe_flag(best['candidate'][0].split(':', 1)[1])}"
    )

final_capture = rows[-1][2]
first_capture = rows[0][2]
selected_flag_sizes = [flag_size(row[1]["candidate"][0].split(":", 1)[1]) for row in rows]
count_5 = sum(1 for size in selected_flag_sizes if size == 5)

check(
    "a small greedy subset improves over known sectors",
    first_capture > (base_s - 1) / (s_full - 1),
    f"first_capture={fmt_frac(first_capture, 20)} base={fmt_frac((base_s - 1) / (s_full - 1), 20)}",
)
check(
    "four greedy operators already close the exact likelihood gap",
    rows[3][2] == 1,
    f"step4_capture={fmt_frac(rows[3][2], 24)}",
)
check(
    "greedy selection reaches for higher-order flags",
    count_5 >= 1,
    f"selected_5_flags={count_5}",
)
check(
    "predictive sufficiency arrives before full atom reconstruction",
    rows[3][1]["atoms"] < len(P) and rows[8][1]["atoms"] == len(P),
    f"step4_atoms={rows[3][1]['atoms']} step9_atoms={rows[8][1]['atoms']} classes={len(P)}",
)

print("\n=== Greedy status ===")
print(
    "A tiny exact-flag operator subset closes the finite predictive likelihood "
    "before it reconstructs all record atoms.  This is a stronger opening than "
    "the full deck theorem: the target may be predictive sufficiency, not full "
    "record reconstruction."
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
