#!/usr/bin/env python3
"""
Paper 29 receipt: greedy operator robustness audit.

The previous receipt found that, for the N=7 staged/fiber toy with weight
base 3, four greedy exact flag operators close the projected likelihood gap
before full atom reconstruction.  This receipt checks whether that is a
fragile coincidence of one adversary strength.

It repeats the greedy exact-martingale selection for weight bases 2, 3, and 5.

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
        f"{name}:r{relation_count(bits, k)}h{height(bits, k)}"
        f"w{width(bits, k)}i{interval_counts(bits, k)[:3]}"
    )


def greedy_run(weight_base, steps=4):
    n = 7
    P, Q, reps = build_projected_laws(n, weight_base=weight_base)
    features = feature_maps(P, reps, n)
    s_full = second_moment(P, Q)
    known_groups = ["scalar", "interval", "regularity", "matching"]
    selected = []
    for group in known_groups:
        for name, mapping in sorted(features[group].items()):
            selected.append((f"{group}:{name}", mapping))
    candidates = []
    for group in ["flags3", "flags4", "flags5"]:
        for name, mapping in sorted(features[group].items()):
            candidates.append((f"{group}:{name}", mapping))

    base_s, base_atoms, _ = capture_from_features(P, Q, selected)
    rows = []
    remaining = list(candidates)
    for step in range(1, steps + 1):
        best = None
        for candidate in remaining:
            s_g, atoms, max_atom = capture_from_features(P, Q, selected + [candidate])
            if best is None or s_g > best["S"]:
                best = {"candidate": candidate, "S": s_g, "atoms": atoms, "max_atom": max_atom}
        selected.append(best["candidate"])
        remaining = [candidate for candidate in remaining if candidate[0] != best["candidate"][0]]
        capture = (best["S"] - 1) / (s_full - 1) if s_full != 1 else Fraction(1)
        rows.append((step, best, capture))

    base_capture = (base_s - 1) / (s_full - 1) if s_full != 1 else Fraction(1)
    return {
        "weight_base": weight_base,
        "P": P,
        "Q": Q,
        "S_full": s_full,
        "base_capture": base_capture,
        "base_atoms": base_atoms,
        "rows": rows,
    }


print("=" * 80)
print("Paper 29 greedy operator robustness")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

audits = [greedy_run(base) for base in [2, 3, 5]]

for audit in audits:
    print(
        f"\nweight_base={audit['weight_base']} "
        f"S_full={fmt_frac(audit['S_full'], 30)} "
        f"known_capture={fmt_frac(audit['base_capture'], 24)} atoms={audit['base_atoms']}/1956"
    )
    for step, best, capture in audit["rows"]:
        flag_name = best["candidate"][0].split(":", 1)[1]
        print(
            f"  step={step} capture={fmt_frac(capture, 24)} "
            f"atoms={best['atoms']}/1956 max_atom={best['max_atom']} "
            f"{describe_flag(flag_name)}"
        )

step4_captures = [audit["rows"][3][2] for audit in audits]
step1_captures = [audit["rows"][0][2] for audit in audits]
step4_atoms = [audit["rows"][3][1]["atoms"] for audit in audits]

check(
    "first greedy flag captures at least 99 percent for all audited strengths",
    min(step1_captures) > Fraction(99, 100),
    "step1=" + ", ".join(fmt_frac(value, 18) for value in step1_captures),
)
check(
    "four greedy flags close the exact likelihood gap for all audited strengths",
    all(value == 1 for value in step4_captures),
    "step4=" + ", ".join(fmt_frac(value, 18) for value in step4_captures),
)
check(
    "four greedy flags do not fully reconstruct record atoms in all audited strengths",
    all(atoms < 1956 for atoms in step4_atoms),
    "step4_atoms=" + ", ".join(str(value) for value in step4_atoms),
)

print("\n=== Robustness status ===")
print(
    "The finite predictive-sufficiency phenomenon is robust across the audited "
    "staged/fiber strengths: a tiny exact local operator set closes the "
    "projected likelihood gap before full atom reconstruction.  The next "
    "theorem should target predictive sufficiency, not full deck reconstruction."
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
