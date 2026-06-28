#!/usr/bin/env python3
"""
Paper 29 receipt: external mathematics compatibility campaigns.

This receipt stress-tests seven outside mathematical analogies against the
finite staged/fiber record quotient, while keeping the Barandes/Shard rule:
hidden rewrites are proof/gauge structure, not physical divisible evolution.

The campaigns are:

1. algebraic statistics / Markov bases;
2. incidence Hopf algebras / decomposition spaces;
3. Gibbs/non-Gibbs projection and quasilocality;
4. Weisfeiler-Leman / coherent configurations;
5. flag algebras / poset limits;
6. modular/noncongruence forms;
7. Tutte deletion-contraction universality.

All finite counts are exact integers/Fractions.  Decimal reporting uses
mpmath with dps=140.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations
import math
import sys

import mpmath as mp

from p29_projected_likelihood_basis_audit import (
    canon_bits,
    feature_maps,
    fmt_frac,
    has_rel,
    permutation_order_bits,
    perms,
    restrict_bits,
    same_block_score,
    small_canon,
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


def delete_vertex_bits(bits, n, v):
    subset = tuple(i for i in range(n) if i != v)
    return restrict_bits(bits, n, subset)


def build_score_polynomials(n):
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
    normalized = {
        key: tuple(Fraction(coeff, p_counts[key]) for coeff in polys[key])
        for key in p_counts
    }
    return P, dict(polys), normalized, dict(p_counts), reps, dict(fibers)


def feature_names(features, groups):
    names = []
    for group in groups:
        for feature_name in sorted(features[group]):
            names.append(f"{group}:{feature_name}")
    return names


def feature_value(features, name, key):
    group, feature = name.split(":", 1)
    return features.get(group, {}).get(feature, {}).get(key, 0)


def partition_atoms(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atoms[tuple(feature_value(features, name, key) for name in names)].append(key)
    return atoms


def bad_atom_count(P, features, names, normalized):
    bad = 0
    conflicts = 0
    atoms = partition_atoms(P, features, names)
    for keys in atoms.values():
        seen = defaultdict(list)
        for key in keys:
            seen[normalized[key]].append(key)
        if len(seen) > 1:
            bad += 1
            for i, left in enumerate(keys):
                for right in keys[i + 1 :]:
                    if normalized[left] != normalized[right]:
                        conflicts += 1
    return len(atoms), bad, conflicts


def adjacent_swap_components(fiber):
    index = {pi: idx for idx, pi in enumerate(fiber)}
    graph = [[] for _ in fiber]
    for idx, pi in enumerate(fiber):
        row = list(pi)
        for i in range(len(pi) - 1):
            swapped = list(row)
            swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
            swapped = tuple(swapped)
            j = index.get(swapped)
            if j is not None:
                graph[idx].append(j)
                graph[j].append(idx)
    seen = [False for _ in fiber]
    sizes = []
    for start in range(len(fiber)):
        if seen[start]:
            continue
        seen[start] = True
        q = deque([start])
        size = 0
        while q:
            node = q.popleft()
            size += 1
            for nxt in graph[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    q.append(nxt)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def deletion_deck(bits, n):
    return tuple(sorted(small_canon(delete_vertex_bits(bits, n, v), n - 1) for v in range(n)))


def interval_counts_after_delete_identity(P, reps, n, k):
    flag_keys = set()
    counts_by_record = {}
    for key, bits in reps.items():
        counts = defaultdict(int)
        for subset in combinations(range(n), k):
            counts[small_canon(restrict_bits(bits, n, subset), k)] += 1
        counts_by_record[key] = counts
        flag_keys.update(counts)

    violations = 0
    for key, bits in reps.items():
        child_keys = [canon_bits(delete_vertex_bits(bits, n, v), n - 1) for v in range(n)]
        for flag in flag_keys:
            lhs = 0
            for child in child_keys:
                child_bits = None
                # Reconstruct child counts directly from the restricted child bits,
                # because the child need not appear as a representative key here.
                # This keeps the identity independent of representative choices.
                # The simple route is to recompute from each deleted suborder.
            # The recompute loop below replaces the placeholder above.
    violations = 0
    for key, bits in reps.items():
        parent_counts = counts_by_record[key]
        child_accum = Counter()
        for v in range(n):
            child_bits = delete_vertex_bits(bits, n, v)
            for subset in combinations(range(n - 1), k):
                child_accum[small_canon(restrict_bits(child_bits, n - 1, subset), k)] += 1
        for flag in flag_keys:
            if child_accum[flag] != (n - k) * parent_counts.get(flag, 0):
                violations += 1
    return len(flag_keys), violations


print("=" * 80)
print("Paper 29 external mathematics compatibility campaigns")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

P7, polys7, norm7, counts7, reps7, fibers7 = build_score_polynomials(7)
features7 = feature_maps(P7, reps7, 7)
known7 = feature_names(features7, ["scalar", "interval", "regularity", "matching"])
fixed_four = [
    "flags3:flag3_36",
    "flags4:flag4_206",
    "flags5:flag5_17288",
    "flags4:flag4_0",
]

print("\nCampaign 1: algebraic statistics / Markov bases")
component_rows = []
for key, fiber in fibers7.items():
    if len(fiber) <= 1:
        continue
    comps = adjacent_swap_components(fiber)
    if len(comps) > 1:
        component_rows.append((len(fiber), len(comps), comps[:5], key))
component_rows.sort(reverse=True)
worst_fiber = component_rows[0]
print(
    "adjacent same-fiber presentation moves: "
    f"disconnected_fibers={len(component_rows)} worst_size={worst_fiber[0]} "
    f"worst_components={worst_fiber[1]} top_component_sizes={worst_fiber[2]}"
)
check(
    "naive adjacent hidden rewrites are not a physical Markov basis",
    len(component_rows) > 0,
    f"disconnected_fibers={len(component_rows)}",
)
check(
    "fiber sums remain indivisible record objects",
    all(sum(poly) == counts7[key] for key, poly in polys7.items()),
    f"records={len(P7)}",
)

print("\nCampaign 2: incidence Hopf / decomposition-space recurrence")
P6, polys6, norm6, counts6, reps6, fibers6 = build_score_polynomials(6)
lhs = {key: [6 * coeff for coeff in polys6[key]] for key in polys6}
rhs = {key: [0 for _ in range(7)] for key in polys6}
boundary_types = set()
for key, fiber in fibers6.items():
    for pi in fiber:
        for i in range(6):
            child = delete_position(pi, i)
            a = same_block_score(child)
            b = same_block_score(pi) - a
            boundary_types.add((a, b))
            rhs[key][a + b] += 1
recurrence_errors = sum(1 for key in lhs if lhs[key] != rhs[key])
print(f"boundary types={len(boundary_types)} recurrence_errors={recurrence_errors}")
check(
    "rooted deletion score-boundary recurrence reconstructs N W_R",
    recurrence_errors == 0,
    f"boundary_types={len(boundary_types)}",
)

print("\nCampaign 3: Gibbs/non-Gibbs projection and quasilocality")
atoms_known_four = partition_atoms(P7, features7, known7 + fixed_four)
non_singletons = [keys for keys in atoms_known_four.values() if len(keys) > 1]
target_atom = non_singletons[0]
target = target_atom[0]
base = 10_000
weights = {key: (base if key == target else 1) for key in P7}
normalizer = sum(P7[key] * weights[key] for key in P7)
L = {key: Fraction(weights[key], 1) / normalizer for key in P7}
atom_l_values = [L[key] for key in target_atom]
atom_oscillation = max(atom_l_values) - min(atom_l_values)
same_half_bad = bad_atom_count(P7, features7, known7 + fixed_four, norm7)[1]
print(
    f"known+four bad atoms for same-half score={same_half_bad} "
    f"atom_spike_oscillation={fmt_frac(atom_oscillation, 36)}"
)
check(
    "same-half law is quasilocal relative to known+four in the finite toy",
    same_half_bad == 0,
    f"bad_atoms={same_half_bad}",
)
check(
    "atom spike is non-quasilocal relative to the same filtration",
    atom_oscillation > 1000,
    f"oscillation={fmt_frac(atom_oscillation, 30)}",
)

print("\nCampaign 4: Weisfeiler-Leman / coherent-configuration refinement")
atoms_known, bad_known, conflicts_known = bad_atom_count(P7, features7, known7, norm7)
atoms_flag3, bad_flag3, conflicts_flag3 = bad_atom_count(
    P7, features7, known7 + feature_names(features7, ["flags3"]), norm7
)
atoms_flag34, bad_flag34, conflicts_flag34 = bad_atom_count(
    P7, features7, known7 + feature_names(features7, ["flags3", "flags4"]), norm7
)
print(
    f"bad_atoms known={bad_known}, +flags3={bad_flag3}, +flags3+flags4={bad_flag34}; "
    f"conflicts known={conflicts_known}, +flags3={conflicts_flag3}, +flags3+flags4={conflicts_flag34}"
)
check(
    "flag refinement behaves like a canonical WL-style refinement ladder",
    bad_known > bad_flag3 >= bad_flag34,
    f"bad={bad_known}->{bad_flag3}->{bad_flag34}",
)

print("\nCampaign 5: flag algebras / poset limits")
flag_count, flag_violations = interval_counts_after_delete_identity(P7, reps7, 7, 3)
print(f"3-flag types={flag_count} deletion_identity_violations={flag_violations}")
check(
    "induced flag densities are deletion-projective coordinates",
    flag_violations == 0,
    f"flag_types={flag_count}",
)

print("\nCampaign 6: modular/noncongruence forms")
P8, polys8, norm8, counts8, reps8, fibers8 = build_score_polynomials(8)
features8 = feature_maps(P8, reps8, 8)
known8 = feature_names(features8, ["scalar", "interval", "regularity", "matching"])
n8_triple = [
    "flags4:flag4_192",
    "flags4:flag4_2248",
    "flags5:flag5_16904",
]
_atoms7_fixed, bad7_fixed, _ = bad_atom_count(P7, features7, known7 + fixed_four, norm7)
_atoms8_fixed, bad8_fixed, _ = bad_atom_count(P8, features8, known8 + fixed_four, norm8)
_atoms7_triple, bad7_triple, _ = bad_atom_count(P7, features7, known7 + n8_triple, norm7)
_atoms8_triple, bad8_triple, _ = bad_atom_count(P8, features8, known8 + n8_triple, norm8)
print(
    f"fixed_four bad N7={bad7_fixed} N8={bad8_fixed}; "
    f"N8_triple bad N7={bad7_triple} N8={bad8_triple}"
)
check(
    "finite q-polynomial certificates do not yet form a Hecke-like stable basis",
    bad7_fixed == 0 and bad8_fixed == 0 and bad8_triple == 0 and bad7_triple > 0,
    f"triple_bad_N7={bad7_triple}",
)

print("\nCampaign 7: Tutte universality")
deck_groups = defaultdict(list)
for key, bits in reps7.items():
    deck_groups[deletion_deck(bits, 7)].append(key)
deck_bad = []
for deck, keys in deck_groups.items():
    polys = {norm7[key] for key in keys}
    if len(polys) > 1:
        deck_bad.append((len(keys), len(polys), keys[:3]))
deck_bad.sort(reverse=True)
print(
    f"deletion_deck_groups={len(deck_groups)} score-bad deck groups={len(deck_bad)} "
    f"largest_bad_group={deck_bad[0] if deck_bad else None}"
)
check(
    "full vertex-deletion deck is too strong to be a controlled Tutte-style law",
    len(deck_groups) == len(P7) and bad_known > 0,
    f"deck_groups={len(deck_groups)} records={len(P7)} known_bad_atoms={bad_known}",
)
check(
    "deletion-deck universality remains scoped rather than falsified",
    len(deck_bad) == 0,
    f"bad_deck_groups={len(deck_bad)}",
)

print("\n=== Seven-campaign status ===")
print(
    "The compatible imports are proof/gauge structures, not physical hidden "
    "time steps.  Algebraic-statistical fibers, decomposition recurrences, "
    "quasilocality tests, WL-style refinement, and flag-density limits all "
    "make direct contact with Paper 29.  Modular and Tutte analogies remain "
    "weaker: they are useful hostile tests for stable operator recurrence and "
    "deletion universality.  The full deletion deck is too reconstructive to be "
    "a controlled law, while coarse graph/Tutte-like sectors are too weak."
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
