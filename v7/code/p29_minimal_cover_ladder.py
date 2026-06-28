#!/usr/bin/env python3
"""
Paper 29 receipt: minimal conflict-cover ladder.

The N=7 and N=8 receipts showed two facts that pull in opposite directions:

1. tiny local flag sets can make the normalized same-half hidden score
   polynomial constant on known-sector atoms;
2. the literal operator representatives drift.

This receipt turns that into a finite ladder for N=6,7,8.  For each N it
computes the known-sector polynomial conflicts and searches exact 3-, 4-, and
5-flag operators for a smallest conflict cover.

All score polynomials and probabilities are exact Fractions.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
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


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def build_score_polynomials(n):
    p_counts = defaultdict(int)
    polys = defaultdict(lambda: [0 for _ in range(n + 1)])
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        p_counts[key] += 1
        polys[key][same_block_score(pi)] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    return P, dict(polys), dict(p_counts), reps


def normalized_poly(poly, count):
    return tuple(Fraction(coeff, count) for coeff in poly)


def feature_names(features, groups):
    names = []
    for group in groups:
        for feature_name in sorted(features[group]):
            names.append(f"{group}:{feature_name}")
    return names


def partition_atoms(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atom = tuple(feature_mapping(features, name)[key] for name in names)
        atoms[atom].append(key)
    return atoms


def bad_atoms(P, features, names, normalized):
    atoms = partition_atoms(P, features, names)
    bad = []
    for atom, keys in atoms.items():
        first = normalized[keys[0]]
        if any(normalized[key] != first for key in keys[1:]):
            bad.append((atom, keys))
    return atoms, bad


def conflict_pairs(bad, normalized):
    conflicts = []
    for _atom, keys in bad:
        for idx, left in enumerate(keys):
            for right in keys[idx + 1 :]:
                if normalized[left] != normalized[right]:
                    conflicts.append((left, right))
    return conflicts


def conflict_mask(mapping, conflicts):
    mask = 0
    for idx, (left, right) in enumerate(conflicts):
        if mapping[left] != mapping[right]:
            mask |= 1 << idx
    return mask


def first_covers(active, masks, full_mask, size, limit=8):
    rows = []
    for combo in combinations(active, size):
        mask = 0
        for name in combo:
            mask |= masks[name]
            if mask == full_mask:
                break
        if mask == full_mask:
            rows.append(combo)
            if len(rows) >= limit:
                break
    return rows


def cover_mass(P, features, known, cover):
    atoms = partition_atoms(P, features, known + list(cover))
    unresolved = [keys for keys in atoms.values() if len(keys) > 1]
    mass = sum(P[key] for keys in unresolved for key in keys)
    max_size = max((len(keys) for keys in unresolved), default=1)
    return len(atoms), len(unresolved), max_size, mass


def analyze_n(n):
    P, polys, p_counts, reps = build_score_polynomials(n)
    features = feature_maps(P, reps, n)
    normalized = {key: normalized_poly(polys[key], p_counts[key]) for key in P}
    known = feature_names(features, ["scalar", "interval", "regularity", "matching"])
    candidates = feature_names(features, ["flags3", "flags4", "flags5"])

    known_atoms, known_bad = bad_atoms(P, features, known, normalized)
    conflicts = conflict_pairs(known_bad, normalized)
    print("\n" + "=" * 80)
    print(f"N={n} minimal same-half polynomial conflict cover")
    print("=" * 80)
    print(f"record classes={len(P)}")
    print(f"known atoms={len(known_atoms)} known_bad={len(known_bad)}")
    print(f"candidate local flags={len(candidates)} conflict pairs={len(conflicts)}")

    if not conflicts:
        print("minimal_cover_size=0")
        return {
            "n": n,
            "classes": len(P),
            "known_bad": 0,
            "minimal_size": 0,
            "covers": [()],
            "first_stats": (len(known_atoms), 0, 1, Fraction(0)),
        }

    full_mask = (1 << len(conflicts)) - 1
    masks = {
        name: conflict_mask(feature_mapping(features, name), conflicts)
        for name in candidates
    }
    active = [name for name in candidates if masks[name] != 0]
    print(f"active conflict-cover flags={len(active)}")

    covers = []
    minimal_size = None
    for size in range(1, 6):
        covers = first_covers(active, masks, full_mask, size)
        print(f"size={size} covers_listed={len(covers)}")
        if covers:
            minimal_size = size
            break

    first = covers[0]
    atoms, unresolved, max_size, mass = cover_mass(P, features, known, first)
    print(f"minimal_cover_size={minimal_size}")
    for idx, cover in enumerate(covers[:6], start=1):
        atoms_i, unresolved_i, max_size_i, mass_i = cover_mass(P, features, known, cover)
        print(
            f"  cover {idx}: {cover} atoms={atoms_i}/{len(P)} "
            f"unresolved={unresolved_i} max_atom={max_size_i} mass={fmt_frac(mass_i, 36)}"
        )

    return {
        "n": n,
        "classes": len(P),
        "known_bad": len(known_bad),
        "minimal_size": minimal_size,
        "covers": covers,
        "first_stats": (atoms, unresolved, max_size, mass),
    }


print("=" * 80)
print("Paper 29 minimal conflict-cover ladder")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

results = [analyze_n(n) for n in (6, 7, 8)]

sizes = {row["n"]: row["minimal_size"] for row in results}
known_bad = {row["n"]: row["known_bad"] for row in results}
mass8 = results[2]["first_stats"][3]

check(
    "N=6 known sectors are already same-half polynomial sufficient",
    sizes[6] == 0 and known_bad[6] == 0,
    f"size={sizes[6]} known_bad={known_bad[6]}",
)
check(
    "N=7 requires a nontrivial local cover",
    sizes[7] == 4,
    f"size={sizes[7]} known_bad={known_bad[7]}",
)
check(
    "N=8 requires a nontrivial but smaller local cover",
    sizes[8] == 3,
    f"size={sizes[8]} known_bad={known_bad[8]}",
)
check(
    "minimal covers remain tiny through the audited ladder",
    max(sizes.values()) <= 4,
    f"sizes={sizes}",
)
check(
    "N=8 first minimal cover is not a lookup table",
    mass8 < Fraction(1, 100),
    f"unresolved_mass={fmt_frac(mass8, 30)}",
)

print("\n=== Ladder status ===")
print(
    "The exact finite ladder rejects a fixed-name law but supports a controlled "
    "conflict-cover target. Known sectors close N=6, N=7 needs four local flags, "
    "and N=8 needs three. The cover size stays tiny while representatives drift."
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
