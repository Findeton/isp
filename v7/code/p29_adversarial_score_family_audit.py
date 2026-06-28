#!/usr/bin/env python3
"""
Paper 29 receipt: adversarial score-family audit.

The score-polynomial receipt proves that four local flag operators are exactly
predictively sufficient for the N=7 same-half staged/fiber family.  This
receipt follows the hostile Feynman/Euler opening:

    Are those four operators universal, or are they tuned to that hidden score?

We keep the same projected record space, same exact finite arithmetic, and the
same candidate local flag-operator family.  Then we replace the hidden score by
several nearby coordinate scores on permutations and by one deliberately
hostile unresolved-atom score.  For each score family we check:

1. whether the same four operators make the normalized score polynomial
   constant on each sector atom;
2. how much of the base-3 projected likelihood second moment they capture;
3. which four operators a fresh greedy search selects for that score.

All finite probabilities and score polynomials are exact integers/Fractions.
Decimal reporting uses mpmath with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
import math
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
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


def build_counts(n, score_fn):
    p_counts = defaultdict(int)
    q_weight_counts = defaultdict(int)
    polys = defaultdict(lambda: [0 for _ in range(n + 1)])
    reps = {}
    total_q_weight = 0
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        score = score_fn(pi)
        weight = 3**score
        p_counts[key] += 1
        q_weight_counts[key] += weight
        polys[key][score] += 1
        total_q_weight += weight

    total_p = math.factorial(n)
    p_law = {key: Fraction(count, total_p) for key, count in p_counts.items()}
    q_law = {key: Fraction(q_weight_counts[key], total_q_weight) for key in p_counts}
    return p_law, q_law, dict(polys), dict(p_counts), reps


def second_moment(p_law, q_law):
    return sum((q_law[key] * q_law[key]) / p_law[key] for key in p_law)


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def capture_from_names(p_law, q_law, features, feature_names):
    p_atoms = defaultdict(Fraction)
    q_atoms = defaultdict(Fraction)
    counts = defaultdict(int)
    for record_key in p_law:
        atom = tuple(feature_mapping(features, name)[record_key] for name in feature_names)
        p_atoms[atom] += p_law[record_key]
        q_atoms[atom] += q_law[record_key]
        counts[atom] += 1
    s_g = sum((q_atoms[atom] * q_atoms[atom]) / p_atoms[atom] for atom in p_atoms)
    return s_g, len(p_atoms), max(counts.values())


def normalized_polys(polys, p_counts):
    return {
        key: tuple(Fraction(coeff, p_counts[key]) for coeff in poly)
        for key, poly in polys.items()
    }


def polynomial_violations(p_law, features, feature_names, normalized):
    atoms = defaultdict(list)
    for record_key in p_law:
        atom = tuple(feature_mapping(features, name)[record_key] for name in feature_names)
        atoms[atom].append(record_key)

    violations = []
    for atom, keys in atoms.items():
        first = normalized[keys[0]]
        if any(normalized[key] != first for key in keys[1:]):
            violations.append((atom, keys))
    return atoms, violations


def greedy_four(p_law, q_law, features, known_features, candidate_features):
    selected = list(known_features)
    remaining = list(candidate_features)
    rows = []
    for step in range(4):
        best = None
        for candidate in remaining:
            s_g, atom_count, max_atom = capture_from_names(
                p_law, q_law, features, selected + [candidate]
            )
            if best is None or s_g > best["s_g"]:
                best = {
                    "name": candidate,
                    "s_g": s_g,
                    "atom_count": atom_count,
                    "max_atom": max_atom,
                }
        selected.append(best["name"])
        remaining = [candidate for candidate in remaining if candidate != best["name"]]
        rows.append(best)
    return selected, rows


def same_half(pi):
    return same_block_score(pi)


def diagonal_band(pi):
    return sum(1 for x, y in enumerate(pi) if abs(x - y) <= 1)


def anti_diagonal_band(pi):
    n = len(pi)
    return sum(1 for x, y in enumerate(pi) if abs(x + y - (n - 1)) <= 1)


def parity_match(pi):
    return sum(1 for x, y in enumerate(pi) if (x - y) % 2 == 0)


def lower_left(pi):
    n = len(pi)
    cut = n // 2
    return sum(1 for x, y in enumerate(pi) if x < cut and y < cut)


def central_square(pi):
    n = len(pi)
    lo = n // 3
    hi = n - lo
    return sum(1 for x, y in enumerate(pi) if lo <= x < hi and lo <= y < hi)


print("=" * 80)
print("Paper 29 adversarial score-family audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 7

control_p, _control_q, _control_polys, _control_counts, reps = build_counts(n, same_half)
features = feature_maps(control_p, reps, n)

known_features = []
for group in ["scalar", "interval", "regularity", "matching"]:
    for feature_name in sorted(features[group]):
        known_features.append(f"{group}:{feature_name}")

fixed_greedy = [
    "flags3:flag3_36",
    "flags4:flag4_206",
    "flags5:flag5_17288",
    "flags4:flag4_0",
]

fixed_atoms = defaultdict(list)
for record_key in control_p:
    atom = tuple(
        feature_mapping(features, name)[record_key]
        for name in known_features + fixed_greedy
    )
    fixed_atoms[atom].append(record_key)
unresolved_pairs = [keys for keys in fixed_atoms.values() if len(keys) > 1]
target_key = unresolved_pairs[0][0]


def targeted_unresolved_atom(pi):
    bits = permutation_order_bits(pi)
    key = canon_bits(bits, len(pi))
    return 1 if key == target_key else 0

candidate_features = []
for group in ["flags3", "flags4", "flags5"]:
    for feature_name in sorted(features[group]):
        candidate_features.append(f"{group}:{feature_name}")

print(f"N={n} record classes={len(control_p)}")
print(f"known feature count={len(known_features)}")
print(f"candidate exact-flag operators={len(candidate_features)}")
print("fixed four=" + ", ".join(fixed_greedy))
print(f"unresolved fixed-four atoms={len(unresolved_pairs)}")

score_families = [
    ("same_half_control", same_half, "natural"),
    ("diagonal_band", diagonal_band, "natural"),
    ("anti_diagonal_band", anti_diagonal_band, "natural"),
    ("parity_match", parity_match, "natural"),
    ("lower_left", lower_left, "natural"),
    ("central_square", central_square, "natural"),
    ("targeted_unresolved_atom", targeted_unresolved_atom, "hostile"),
]

summaries = []

for score_name, score_fn, score_kind in score_families:
    p_law, q_law, polys, p_counts, _reps = build_counts(n, score_fn)
    normalized = normalized_polys(polys, p_counts)
    s_full = second_moment(p_law, q_law)
    known_s, known_atoms, _ = capture_from_names(p_law, q_law, features, known_features)

    fixed_features = known_features + fixed_greedy
    fixed_s, fixed_atoms, fixed_max_atom = capture_from_names(
        p_law, q_law, features, fixed_features
    )
    _fixed_poly_atoms, fixed_poly_bad = polynomial_violations(
        p_law, features, fixed_features, normalized
    )

    greedy_features, greedy_rows = greedy_four(
        p_law, q_law, features, known_features, candidate_features
    )
    greedy_s, greedy_atoms, greedy_max_atom = capture_from_names(
        p_law, q_law, features, greedy_features
    )
    _greedy_poly_atoms, greedy_poly_bad = polynomial_violations(
        p_law, features, greedy_features, normalized
    )

    known_capture = (known_s - 1) / (s_full - 1) if s_full != 1 else Fraction(1)
    fixed_capture = (fixed_s - 1) / (s_full - 1) if s_full != 1 else Fraction(1)
    greedy_capture = (greedy_s - 1) / (s_full - 1) if s_full != 1 else Fraction(1)
    selected_flags = greedy_features[len(known_features) :]

    summaries.append(
        {
            "name": score_name,
            "known_capture": known_capture,
            "fixed_capture": fixed_capture,
            "greedy_capture": greedy_capture,
            "fixed_bad": len(fixed_poly_bad),
            "greedy_bad": len(greedy_poly_bad),
            "fixed_atoms": fixed_atoms,
            "greedy_atoms": greedy_atoms,
            "fixed_max_atom": fixed_max_atom,
            "greedy_max_atom": greedy_max_atom,
            "selected": selected_flags,
            "kind": score_kind,
        }
    )

    print("\n---", score_name, "---")
    print(f"S_full={fmt_frac(s_full, 36)}")
    print(
        "known capture="
        f"{fmt_frac(known_capture, 24)} atoms={known_atoms}/{len(p_law)}"
    )
    print(
        "fixed-four capture="
        f"{fmt_frac(fixed_capture, 24)} atoms={fixed_atoms}/{len(p_law)} "
        f"max_atom={fixed_max_atom} polynomial_bad_atoms={len(fixed_poly_bad)}"
    )
    print(
        "fresh-greedy capture="
        f"{fmt_frac(greedy_capture, 24)} atoms={greedy_atoms}/{len(p_law)} "
        f"max_atom={greedy_max_atom} polynomial_bad_atoms={len(greedy_poly_bad)}"
    )
    print("fresh-greedy flags=" + ", ".join(selected_flags))

control = summaries[0]
natural_alternatives = [row for row in summaries[1:] if row["kind"] == "natural"]
hostile = [row for row in summaries if row["kind"] == "hostile"][0]
broken_natural_fixed = [row for row in natural_alternatives if row["fixed_bad"] > 0]
different_greedy = [row for row in natural_alternatives if row["selected"] != fixed_greedy]
not_closed_by_greedy = [row for row in summaries if row["greedy_bad"] > 0]
known_complete = [row for row in summaries if row["known_capture"] == 1]

check(
    "control score keeps the score-polynomial certificate",
    control["fixed_bad"] == 0 and control["fixed_capture"] == 1,
    f"fixed_bad={control['fixed_bad']} fixed_capture={fmt_frac(control['fixed_capture'], 24)}",
)
check(
    "fixed four operators survive audited natural coordinate scores",
    len(broken_natural_fixed) == 0,
    "natural_fixed_bad="
    + ", ".join(f"{row['name']}={row['fixed_bad']}" for row in natural_alternatives),
)
check(
    "literal fixed four are not universal over all projected laws",
    hostile["fixed_bad"] > 0 and hostile["fixed_capture"] < 1,
    f"hostile_bad={hostile['fixed_bad']} hostile_capture={fmt_frac(hostile['fixed_capture'], 24)}",
)
check(
    "fresh greedy flags are score-dependent",
    len(different_greedy) > 0,
    "different=" + ", ".join(row["name"] for row in different_greedy),
)
check(
    "fresh four-flag greedy repair closes all audited score polynomials",
    len(not_closed_by_greedy) == 0,
    "not_closed=" + ", ".join(row["name"] for row in not_closed_by_greedy),
)
check(
    "some natural residues are already known-sector complete",
    len(known_complete) > 0,
    "known_complete=" + ", ".join(row["name"] for row in known_complete),
)

print("\n=== Adversarial status ===")
print(
    "The same four local operators are an exact polynomial certificate for the "
    "same-half staged/fiber score and survived the audited natural coordinate "
    "tilts.  They are still not a universal law: a targeted law on the single "
    "remaining unresolved atom breaks them.  The robust object is therefore not "
    "the literal four-operator list.  It is the projection rule: derive the "
    "controlled local-operator filtration that makes the projected likelihood "
    "polynomial constant on sector atoms."
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
