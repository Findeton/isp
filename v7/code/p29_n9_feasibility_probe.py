#!/usr/bin/env python3
"""
Paper 29 receipt: N=9 feasibility probe.

Full N=9 local-flag cover search is a heavier problem than the N=8 receipts.
This script does the cautious next step:

1. exactly enumerate the N=9 projected record quotient for permutation orders;
2. exactly compute the normalized same-half hidden score polynomial on each
   record class;
3. exactly compute a lightweight known-sector partition
   (scalar + interval + degree-regularity, excluding matching counts);
4. deterministically sample induced 3-, 4-, and 5-flag extraction cost on the
   most massive classes.

This is a feasibility receipt, not an N=9 proof of controlled cover size.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import math
import sys
from time import perf_counter

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    canon_bits,
    degree_moments,
    flag_counts,
    fmt_frac,
    height,
    interval_counts,
    permutation_order_bits,
    perms,
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


def build_score_polynomials(n):
    p_counts = defaultdict(int)
    polys = defaultdict(lambda: [0 for _ in range(n + 1)])
    reps = {}
    start = perf_counter()
    total = math.factorial(n)
    for idx, pi in enumerate(perms(n), start=1):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        p_counts[key] += 1
        cut = n // 2
        score = sum(1 for x, y in enumerate(pi) if (x < cut) == (y < cut))
        polys[key][score] += 1
        if idx % 50000 == 0:
            print(
                f"  enumerated {idx}/{total} permutations; classes={len(p_counts)}; "
                f"elapsed={perf_counter() - start:.2f}s"
            )
    P = {key: Fraction(count, total) for key, count in p_counts.items()}
    return P, dict(polys), dict(p_counts), reps, perf_counter() - start


def normalized_poly(poly, count):
    return tuple(Fraction(coeff, count) for coeff in poly)


def known_lite_features(bits, n):
    intervals = interval_counts(bits, n)
    deg1, deg2, deg3, dmax, dmin = degree_moments(bits, n)
    return (
        relation_count(bits, n),
        height(bits, n),
        width(bits, n),
        tuple(intervals[:5]),
        sum(intervals[5:]),
        deg2,
        deg3,
        dmax,
        dmin,
        dmax - dmin,
    )


def known_lite_bad_atoms(P, reps, normalized, n):
    atoms = defaultdict(list)
    start = perf_counter()
    for key, bits in reps.items():
        atoms[known_lite_features(bits, n)].append(key)
    bad = []
    conflict_pairs = 0
    max_bad_size = 0
    for atom, keys in atoms.items():
        first = normalized[keys[0]]
        if any(normalized[key] != first for key in keys[1:]):
            bad.append((atom, keys))
            max_bad_size = max(max_bad_size, len(keys))
            for idx, left in enumerate(keys):
                for right in keys[idx + 1 :]:
                    if normalized[left] != normalized[right]:
                        conflict_pairs += 1
    bad_mass = sum(P[key] for _atom, keys in bad for key in keys)
    return {
        "atoms": atoms,
        "bad": bad,
        "bad_mass": bad_mass,
        "conflict_pairs": conflict_pairs,
        "max_bad_size": max_bad_size,
        "elapsed": perf_counter() - start,
    }


def flag_sample(reps, n, sample_size=1024):
    keys = sorted(reps, key=lambda key: key.bit_count())[:sample_size]
    observed = {3: set(), 4: set(), 5: set()}
    total_counts = {3: 0, 4: 0, 5: 0}
    start = perf_counter()
    for key in keys:
        bits = reps[key]
        for k in (3, 4, 5):
            counts = flag_counts(bits, n, k)
            observed[k].update(counts)
            total_counts[k] += sum(counts.values())
    return {
        "sample_size": len(keys),
        "observed": observed,
        "total_counts": total_counts,
        "elapsed": perf_counter() - start,
    }


print("=" * 80)
print("Paper 29 N=9 feasibility probe")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 9
P, polys, p_counts, reps, build_elapsed = build_score_polynomials(n)
normalized = {key: normalized_poly(polys[key], p_counts[key]) for key in P}

print("\nExact N=9 quotient:")
print(f"  permutations={math.factorial(n)}")
print(f"  record classes={len(P)}")
print(f"  build_elapsed={build_elapsed:.2f}s")
print(f"  max_class_count={max(p_counts.values())}")
print(f"  min_class_count={min(p_counts.values())}")

known = known_lite_bad_atoms(P, reps, normalized, n)
print("\nKnown-lite sector conflict landscape:")
print(f"  atoms={len(known['atoms'])}/{len(P)}")
print(f"  bad_atoms={len(known['bad'])}")
print(f"  bad_mass={fmt_frac(known['bad_mass'], 36)}")
print(f"  conflict_pairs={known['conflict_pairs']}")
print(f"  max_bad_atom_size={known['max_bad_size']}")
print(f"  feature_elapsed={known['elapsed']:.2f}s")

sample = flag_sample(reps, n, sample_size=1024)
print("\nDeterministic flag-extraction sample:")
print(f"  sample_size={sample['sample_size']}")
for k in (3, 4, 5):
    print(
        f"  k={k}: observed_flag_types={len(sample['observed'][k])} "
        f"total_induced_counts={sample['total_counts'][k]}"
    )
print(f"  sample_elapsed={sample['elapsed']:.2f}s")

check(
    "N=9 exact quotient enumeration completed",
    len(P) > 14794,
    f"classes={len(P)}",
)
check(
    "known-lite sectors are not score-polynomial sufficient at N=9",
    len(known["bad"]) > 0,
    f"bad_atoms={len(known['bad'])}",
)
check(
    "known-lite conflict landscape is finite enough to audit",
    known["conflict_pairs"] > 0 and known["conflict_pairs"] < 10_000_000,
    f"conflict_pairs={known['conflict_pairs']}",
)
check(
    "flag extraction sample sees nontrivial local algebra",
    all(len(sample["observed"][k]) > 1 for k in (3, 4, 5)),
    "observed=" + ", ".join(f"k{k}:{len(sample['observed'][k])}" for k in (3, 4, 5)),
)
check(
    "N=9 full cover search should be staged, not blind",
    len(P) > 50_000 and known["conflict_pairs"] > 1_000,
    f"classes={len(P)} conflicts={known['conflict_pairs']}",
)

print("\n=== N=9 feasibility status ===")
print(
    "N=9 exact quotient enumeration is feasible, but the conflict landscape is "
    "large enough that a full local-flag cover search should be staged. The "
    "next step is a targeted active-flag scan over known-lite conflict pairs, "
    "not blind enumeration of every cover combination."
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
