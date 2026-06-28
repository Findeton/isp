#!/usr/bin/env python3
"""
Paper 29 receipt: rooted deletion score recurrence.

The previous campaign identified the score-boundary tensor as the bridge from
finite conflict covers to a projective law.  This receipt attacks that bridge
directly.

For a hidden permutation pi at size N, deleting position i gives a child
permutation d_i pi at size N-1.  Let

    R = rho_N(pi)
    A = rho_{N-1}(d_i pi)
    a = s_{N-1}(d_i pi)
    b = s_N(pi) - s_{N-1}(d_i pi)

The raw boundary tensor is

    B_N^down(R,A;a,b)
      = # {(pi,i): rho_N(pi)=R, rho_{N-1}(d_i pi)=A,
                    s_{N-1}(d_i pi)=a, Delta_i^-(pi)=b}.

It must reconstruct the hidden-fiber score polynomial:

    N W_{N,R}(u) = sum_A sum_{a,b} B_N^down(R,A;a,b) u^{a+b}.

The compatible Barandes/Shard interpretation is crucial: this is not a
physical divisible time process.  It is a deletion/decomposition identity on
finite committed records and hidden presentations.

All finite counts are exact integers/Fractions.  Decimal reporting uses
mpmath with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
import math
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    build_projected_laws,
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


def delete_position(pi, i):
    removed = pi[i]
    return tuple(value - (1 if value > removed else 0) for j, value in enumerate(pi) if j != i)


def build_score_data(n):
    p_counts = defaultdict(int)
    polys = defaultdict(lambda: [0 for _ in range(n + 1)])
    reps = {}
    fibers = defaultdict(list)
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        fibers[key].append(pi)
        p_counts[key] += 1
        polys[key][same_block_score(pi)] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    normalized_poly = {
        key: tuple(Fraction(coeff, p_counts[key]) for coeff in polys[key])
        for key in p_counts
    }
    return P, dict(polys), normalized_poly, dict(p_counts), reps, dict(fibers)


def boundary_tensor(n):
    Pn, polys_n, norm_n, counts_n, reps_n, fibers_n = build_score_data(n)
    Pm, polys_m, norm_m, counts_m, reps_m, fibers_m = build_score_data(n - 1)
    raw = {key: defaultdict(int) for key in Pn}
    loss_hist = {key: defaultdict(int) for key in Pn}
    child_score_counts = defaultdict(int)
    insertion_mass = defaultdict(int)

    for child_key, child_fiber in fibers_m.items():
        for sigma in child_fiber:
            child_score_counts[(child_key, same_block_score(sigma))] += 1

    for parent_key, fiber in fibers_n.items():
        for pi in fiber:
            parent_score = same_block_score(pi)
            for i in range(n):
                child = delete_position(pi, i)
                child_key = canon_bits(permutation_order_bits(child), n - 1)
                a = same_block_score(child)
                b = parent_score - a
                raw[parent_key][(child_key, a, b)] += 1
                loss_hist[parent_key][(a, b)] += 1
                insertion_mass[(child_key, a)] += 1

    raw_signature = {
        key: tuple(sorted((item, count) for item, count in tensor.items()))
        for key, tensor in raw.items()
    }
    raw_normalized_signature = {
        key: tuple(sorted((item, Fraction(count, n * counts_n[key])) for item, count in tensor.items()))
        for key, tensor in raw.items()
    }
    hist_signature = {
        key: tuple(sorted((item, Fraction(count, n * counts_n[key])) for item, count in hist.items()))
        for key, hist in loss_hist.items()
    }
    return {
        "P": Pn,
        "polys": polys_n,
        "norm": norm_n,
        "counts": counts_n,
        "reps": reps_n,
        "features": feature_maps(Pn, reps_n, n),
        "child_counts": counts_m,
        "child_score_counts": dict(child_score_counts),
        "insertion_mass": dict(insertion_mass),
        "raw": raw,
        "raw_signature": raw_signature,
        "raw_normalized_signature": raw_normalized_signature,
        "hist_signature": hist_signature,
    }


def feature_names(features, groups):
    names = []
    for group in groups:
        for feature_name in sorted(features[group]):
            names.append(f"{group}:{feature_name}")
    return names


def feature_value(features, name, key):
    group, feature = name.split(":", 1)
    return features.get(group, {}).get(feature, {}).get(key, 0)


def atoms_for_names(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atoms[tuple(feature_value(features, name, key) for name in names)].append(key)
    return atoms


def bad_atoms(atoms, invariant):
    bad = 0
    conflicts = 0
    for keys in atoms.values():
        buckets = defaultdict(list)
        for key in keys:
            buckets[invariant[key]].append(key)
        if len(buckets) > 1:
            bad += 1
            for i, left in enumerate(keys):
                for right in keys[i + 1 :]:
                    if invariant[left] != invariant[right]:
                        conflicts += 1
    return bad, conflicts


def recurrence_errors(n, data):
    errors = 0
    max_gap = 0
    for key, poly in data["polys"].items():
        from_boundary = [0 for _ in range(n + 1)]
        for (child_key, a, b), count in data["raw"][key].items():
            from_boundary[a + b] += count
        target = [n * coeff for coeff in poly]
        if from_boundary != target:
            errors += 1
            gap = max(abs(from_boundary[i] - target[i]) for i in range(n + 1))
            max_gap = max(max_gap, gap)
    return errors, max_gap


def insertion_errors(n, data):
    errors = 0
    max_gap = 0
    for child_score_key, count in data["child_score_counts"].items():
        observed = data["insertion_mass"].get(child_score_key, 0)
        target = n * n * count
        if observed != target:
            errors += 1
            max_gap = max(max_gap, abs(observed - target))
    return errors, max_gap


def hist_reconstruct_errors(n, data):
    errors = 0
    for key, norm_poly in data["norm"].items():
        hist_poly = [Fraction(0) for _ in range(n + 1)]
        for (a, b), weight in data["hist_signature"][key]:
            hist_poly[a + b] += weight
        if tuple(hist_poly) != norm_poly:
            errors += 1
    return errors


def group_report(label, data, names):
    atoms = atoms_for_names(data["P"], data["features"], names)
    poly_bad, poly_conflicts = bad_atoms(atoms, data["norm"])
    hist_bad, hist_conflicts = bad_atoms(atoms, data["hist_signature"])
    tensor_bad, tensor_conflicts = bad_atoms(atoms, data["raw_normalized_signature"])
    print(
        f"{label:<28} atoms={len(atoms):>6}/{len(data['P']):<6} "
        f"W_bad={poly_bad:>5} W_conf={poly_conflicts:>7} "
        f"H_bad={hist_bad:>5} H_conf={hist_conflicts:>7} "
        f"B_bad={tensor_bad:>5} B_conf={tensor_conflicts:>7}"
    )
    return {
        "atoms": len(atoms),
        "poly_bad": poly_bad,
        "poly_conflicts": poly_conflicts,
        "hist_bad": hist_bad,
        "hist_conflicts": hist_conflicts,
        "tensor_bad": tensor_bad,
        "tensor_conflicts": tensor_conflicts,
    }


print("=" * 80)
print("Paper 29 rooted deletion score recurrence")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

fixed_four = [
    "flags3:flag3_36",
    "flags4:flag4_206",
    "flags5:flag5_17288",
    "flags4:flag4_0",
]
first_n8_triple = [
    "flags4:flag4_192",
    "flags4:flag4_2248",
    "flags5:flag5_16904",
]

reports = {}
for n in [6, 7, 8]:
    print("\n" + "=" * 80)
    print(f"N={n} boundary recurrence")
    print("=" * 80)
    data = boundary_tensor(n)
    rec_errors, rec_gap = recurrence_errors(n, data)
    ins_errors, ins_gap = insertion_errors(n, data)
    hist_errors = hist_reconstruct_errors(n, data)
    boundary_types = sorted({(a, b) for sig in data["hist_signature"].values() for (a, b), _w in sig})
    raw_atoms = len(set(data["raw_normalized_signature"].values()))
    hist_atoms = len(set(data["hist_signature"].values()))
    poly_atoms = len(set(data["norm"].values()))
    print(f"classes={len(data['P'])} permutations={math.factorial(n)}")
    print(f"boundary (a,b) types={boundary_types}")
    print(f"unique Wbar={poly_atoms} unique Hbar={hist_atoms} unique Bbar={raw_atoms}")
    print(f"recurrence_errors={rec_errors} recurrence_max_gap={rec_gap}")
    print(f"insertion_mass_errors={ins_errors} insertion_max_gap={ins_gap}")
    print(f"hist_reconstruct_errors={hist_errors}")

    known = feature_names(data["features"], ["scalar", "interval", "regularity", "matching"])
    rows = {}
    rows["known"] = group_report("known", data, known)
    rows["known+flags3"] = group_report(
        "known+flags3", data, known + feature_names(data["features"], ["flags3"])
    )
    rows["known+flags3+flags4"] = group_report(
        "known+flags3+flags4",
        data,
        known + feature_names(data["features"], ["flags3", "flags4"]),
    )
    rows["known+fixed_four"] = group_report("known+fixed_four", data, known + fixed_four)
    if n == 8:
        rows["known+N8_triple"] = group_report("known+N8_triple", data, known + first_n8_triple)
    reports[n] = {
        "rec_errors": rec_errors,
        "ins_errors": ins_errors,
        "hist_errors": hist_errors,
        "boundary_types": boundary_types,
        "poly_atoms": poly_atoms,
        "hist_atoms": hist_atoms,
        "raw_atoms": raw_atoms,
        "rows": rows,
        "classes": len(data["P"]),
    }

check(
    "raw boundary tensor reconstructs N W_R for N=6,7,8",
    all(reports[n]["rec_errors"] == 0 for n in reports),
    ", ".join(f"N{n}={reports[n]['rec_errors']}" for n in reports),
)
check(
    "deletion and insertion masses agree for every child score sector",
    all(reports[n]["ins_errors"] == 0 for n in reports),
    ", ".join(f"N{n}={reports[n]['ins_errors']}" for n in reports),
)
check(
    "compressed score-loss histogram reconstructs Wbar exactly",
    all(reports[n]["hist_errors"] == 0 for n in reports),
    ", ".join(f"N{n}={reports[n]['hist_errors']}" for n in reports),
)
check(
    "boundary histogram is less reconstructive than the full boundary tensor at N=7",
    reports[7]["hist_atoms"] < reports[7]["raw_atoms"] <= reports[7]["classes"],
    f"H={reports[7]['hist_atoms']} B={reports[7]['raw_atoms']} classes={reports[7]['classes']}",
)
check(
    "known sectors do not determine the boundary histogram at N=7",
    reports[7]["rows"]["known"]["hist_bad"] > 0,
    f"H_bad={reports[7]['rows']['known']['hist_bad']}",
)
check(
    "flags refine boundary uncertainty at N=7",
    reports[7]["rows"]["known"]["hist_bad"]
    > reports[7]["rows"]["known+flags3"]["hist_bad"]
    >= reports[7]["rows"]["known+flags3+flags4"]["hist_bad"],
    (
        f"H_bad={reports[7]['rows']['known']['hist_bad']}->"
        f"{reports[7]['rows']['known+flags3']['hist_bad']}->"
        f"{reports[7]['rows']['known+flags3+flags4']['hist_bad']}"
    ),
)
check(
    "fixed four close Wbar but not the full boundary tensor at N=7",
    reports[7]["rows"]["known+fixed_four"]["poly_bad"] == 0
    and reports[7]["rows"]["known+fixed_four"]["tensor_bad"] > 0,
    (
        f"W_bad={reports[7]['rows']['known+fixed_four']['poly_bad']} "
        f"B_bad={reports[7]['rows']['known+fixed_four']['tensor_bad']}"
    ),
)
check(
    "first N=8 triple closes Wbar at N=8 but not the boundary tensor",
    reports[8]["rows"]["known+N8_triple"]["poly_bad"] == 0
    and reports[8]["rows"]["known+N8_triple"]["tensor_bad"] > 0,
    (
        f"W_bad={reports[8]['rows']['known+N8_triple']['poly_bad']} "
        f"B_bad={reports[8]['rows']['known+N8_triple']['tensor_bad']}"
    ),
)

print("\n=== Recurrence status ===")
print(
    "The rooted deletion score-boundary tensor is exact and has a compressed "
    "score-loss histogram that reconstructs Wbar.  But the full boundary tensor "
    "contains more information than the finite score polynomial, and the known "
    "local covers that close Wbar do not close the full boundary tensor.  The "
    "next theorem must therefore target the compressed boundary needed for "
    "likelihood transfer, or explicitly promote extra boundary data."
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
