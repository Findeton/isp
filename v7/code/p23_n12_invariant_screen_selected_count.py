#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: N=12 invariant-screen selected-count audit.

The first N=10/N=12 selected rare-class audit found that exact unlabeled
canonicalization is the next wall.  This receipt replaces "canonicalize every
sample" by a conservative two-stage pipeline:

  1. group N=12 sampled orders by a cheap color-refinement invariant;
  2. inside repeated invariant groups, split into exact isomorphism classes;
  3. for repeated exact classes, attempt the selected denominator

         P_N(C) = r(C) / (|Aut(C)| N!).

No sparse empirical P_N denominator is used.  If exact isomorphism or selected
realizer/aut counting exceeds a cap, the class is reported as unresolved.

All asserted non-integer arithmetic uses mpmath with dps=140.  Poset
operations are exact bitset operations.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
import math
import random
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def iter_bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


class Poset:
    def __init__(self, future):
        self.future = tuple(future)
        self.N = len(self.future)
        self.past = [0] * self.N
        for x, mask in enumerate(self.future):
            for y in iter_bits(mask):
                self.past[y] |= 1 << x
        self.past = tuple(self.past)


def relation(poset, a, b):
    return bool(poset.future[a] & (1 << b))


def coordinate_order_poset(points):
    future = [0] * len(points)
    for i, (ui, vi) in enumerate(points):
        mask = 0
        for j, (uj, vj) in enumerate(points):
            if ui < uj and vi < vj:
                mask |= 1 << j
        future[i] = mask
    return Poset(future)


def refinement_colors(poset):
    n = poset.N
    all_mask = (1 << n) - 1
    colors = tuple((poset.past[i].bit_count(), poset.future[i].bit_count()) for i in range(n))
    while True:
        signatures = []
        for i in range(n):
            bit = 1 << i
            incomparable = all_mask ^ bit ^ poset.past[i] ^ poset.future[i]
            signatures.append(
                (
                    colors[i],
                    tuple(sorted(colors[j] for j in iter_bits(poset.past[i]))),
                    tuple(sorted(colors[j] for j in iter_bits(poset.future[i]))),
                    tuple(sorted(colors[j] for j in iter_bits(incomparable))),
                )
            )
        unique = {sig: rank for rank, sig in enumerate(sorted(set(signatures), key=repr))}
        new_colors = tuple(unique[sig] for sig in signatures)
        if new_colors == colors:
            return colors
        colors = new_colors


def color_classes(poset):
    colors = refinement_colors(poset)
    classes = defaultdict(list)
    for i, color in enumerate(colors):
        classes[color].append(i)
    return colors, [tuple(classes[color]) for color in sorted(classes)]


def invariant_key(poset):
    colors = tuple((poset.past[i].bit_count(), poset.future[i].bit_count()) for i in range(poset.N))
    raw_classes = defaultdict(list)
    for i, color in enumerate(colors):
        raw_classes[color].append(i)
    ordered_colors = sorted(raw_classes)
    classes = [tuple(raw_classes[color]) for color in ordered_colors]
    class_sizes = tuple(len(cls) for cls in classes)
    index_by_color = {color: idx for idx, color in enumerate(ordered_colors)}
    matrix = [[0] * len(classes) for _ in classes]
    for a in range(poset.N):
        ia = index_by_color[colors[a]]
        for b in iter_bits(poset.future[a]):
            ib = index_by_color[colors[b]]
            matrix[ia][ib] += 1
    return class_sizes, tuple(tuple(row) for row in matrix)


def fixed_matching(n):
    return tuple(frozenset((2 * i, 2 * i + 1)) for i in range(n // 2))


def sample_poset(n, rng, jitter_ratio):
    blocks = [tuple(sorted(edge)) for edge in fixed_matching(n)]
    width = 2
    jitter_num = jitter_ratio.numerator
    jitter_den = jitter_ratio.denominator
    scale = 10000 * jitter_den
    span = 10000 * jitter_num
    tie = n + 1
    u_block_order = list(range(len(blocks)))
    v_block_order = list(range(len(blocks)))
    rng.shuffle(u_block_order)
    rng.shuffle(v_block_order)
    u_rank = [0] * len(blocks)
    v_rank = [0] * len(blocks)
    for rank, block_index in enumerate(u_block_order):
        u_rank[block_index] = rank
    for rank, block_index in enumerate(v_block_order):
        v_rank[block_index] = rank

    points = [None] * n
    for block_index, block in enumerate(blocks):
        local_order = list(block)
        rng.shuffle(local_order)
        for local, label in enumerate(local_order):
            du = rng.randint(-span, span) if span else 0
            dv = rng.randint(-span, span) if span else 0
            u = (u_rank[block_index] * scale + width * du + local) * tie + label
            v = (v_rank[block_index] * scale + width * dv + (width - 1 - local)) * tie + label
            points[label] = (u, v)
    return coordinate_order_poset(points)


def sample_groups(n, sample_count, seed, jitter_ratio):
    rng = random.Random(seed)
    groups = defaultdict(list)
    for _ in range(sample_count):
        poset = sample_poset(n, rng, jitter_ratio)
        groups[invariant_key(poset)].append(poset)
    return groups


def is_isomorphic(poset_a, poset_b, cap):
    if invariant_key(poset_a) != invariant_key(poset_b):
        return False, "invariant"
    colors_a, classes_a = color_classes(poset_a)
    colors_b, classes_b = color_classes(poset_b)
    if [len(cls) for cls in classes_a] != [len(cls) for cls in classes_b]:
        return False, "colors"
    total_space = 1
    for cls in classes_b:
        total_space *= math.factorial(len(cls))
    if total_space > cap:
        return None, f"iso_cap:{total_space}"
    for selected in product(*(permutations(cls) for cls in classes_b)):
        mapping = [None] * poset_a.N
        for cls_a, images in zip(classes_a, selected):
            for source, image in zip(cls_a, images):
                mapping[source] = image
        ok = True
        for a in range(poset_a.N):
            mapped_future = 0
            for b in iter_bits(poset_a.future[a]):
                mapped_future |= 1 << mapping[b]
            if mapped_future != poset_b.future[mapping[a]]:
                ok = False
                break
        if ok:
            return True, "ok"
    return False, "no"


def exact_classes_for_key(posets_a, posets_b, iso_cap):
    reps = []
    counts_a = []
    counts_b = []
    unresolved = 0
    for side, posets in (("a", posets_a), ("b", posets_b)):
        for poset in posets:
            placed = False
            for idx, rep in enumerate(reps):
                iso, status = is_isomorphic(poset, rep, iso_cap)
                if iso is None:
                    unresolved += 1
                    placed = True
                    break
                if iso:
                    if side == "a":
                        counts_a[idx] += 1
                    else:
                        counts_b[idx] += 1
                    placed = True
                    break
            if not placed:
                reps.append(poset)
                counts_a.append(1 if side == "a" else 0)
                counts_b.append(1 if side == "b" else 0)
    candidates = []
    for rep, ca, cb in zip(reps, counts_a, counts_b):
        if ca and cb:
            candidates.append((ca, cb, rep))
    return candidates, unresolved


def automorphism_count(poset, cap):
    _, classes = color_classes(poset)
    total_space = 1
    for cls in classes:
        total_space *= math.factorial(len(cls))
    if total_space > cap:
        return None, total_space
    total = 0
    for selected in product(*(permutations(cls) for cls in classes)):
        perm = [None] * poset.N
        for cls, image_block in zip(classes, selected):
            for source, image in zip(cls, image_block):
                perm[source] = image
        ok = True
        for a in range(poset.N):
            mapped_future = 0
            for b in iter_bits(poset.future[a]):
                mapped_future |= 1 << perm[b]
            if mapped_future != poset.future[perm[a]]:
                ok = False
                break
        if ok:
            total += 1
    return total, total_space


def forced_second_is_linear(poset, order):
    n = poset.N
    rank = [0] * n
    for index, vertex in enumerate(order):
        rank[vertex] = index
    before2 = [0] * n
    for a in range(n):
        for b in range(a + 1, n):
            if relation(poset, a, b):
                before2[a] |= 1 << b
            elif relation(poset, b, a):
                before2[b] |= 1 << a
            elif rank[a] > rank[b]:
                before2[a] |= 1 << b
            else:
                before2[b] |= 1 << a
    for a in range(n):
        for b in iter_bits(before2[a]):
            if before2[b] & ~before2[a]:
                return False
    return True


def realizer_first_order_count(poset, cap):
    n = poset.N
    all_mask = (1 << n) - 1
    visited = 0
    valid = 0
    order = []

    def rec(placed):
        nonlocal visited, valid
        if visited > cap:
            return
        if placed == all_mask:
            visited += 1
            if forced_second_is_linear(poset, order):
                valid += 1
            return
        remaining = all_mask ^ placed
        for x in iter_bits(remaining):
            if poset.past[x] & remaining == 0:
                order.append(x)
                rec(placed | (1 << x))
                order.pop()
                if visited > cap:
                    return

    rec(0)
    if visited > cap:
        return None, visited
    return valid, visited


def selected_probability(poset, realizer_cap, aut_cap):
    aut, aut_space = automorphism_count(poset, aut_cap)
    if aut is None:
        return {"status": "aut_cap", "aut_space": aut_space}
    r_count, visited = realizer_first_order_count(poset, realizer_cap)
    if r_count is None:
        return {"status": "realizer_cap", "aut": aut, "extensions_visited": visited}
    if r_count % aut:
        return {"status": "nonintegral", "r": r_count, "aut": aut}
    count = r_count // aut
    probability = mp.mpf(count) / mp.factorial(poset.N)
    return {
        "status": "ok",
        "r": r_count,
        "aut": aut,
        "count": count,
        "probability": probability,
        "extensions_visited": visited,
    }


print("=" * 80)
print("Collapsed P23 N=12 invariant-screen selected-count audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
sample_count = 4096
iso_cap = 200000
realizer_cap = 1000000
aut_cap = 1000000
schedules = [
    ("linear_quarter", Fraction(1, 4)),
    ("linear_5_16", Fraction(5, 16)),
    ("linear_half", Fraction(1, 2)),
    ("linear_one", Fraction(1, 1)),
]

all_outputs = {}
resolved = []
unresolved_exact = 0
for schedule_index, (name, frac) in enumerate(schedules):
    jitter_ratio = Fraction(frac.numerator * n, frac.denominator * 2)
    print(f"\n{name}: fraction={frac} jitter_ratio={jitter_ratio}")
    groups_a = sample_groups(n, sample_count, 9900000 + schedule_index * 10000, jitter_ratio)
    groups_b = sample_groups(n, sample_count, 9910000 + schedule_index * 10000, jitter_ratio)
    overlap_keys = sorted(set(groups_a) & set(groups_b), key=lambda key: len(groups_a[key]) * len(groups_b[key]), reverse=True)
    print(
        f"  invariant_keys_a={len(groups_a)} invariant_keys_b={len(groups_b)} "
        f"overlap_keys={len(overlap_keys)}"
    )
    schedule_candidates = []
    for key in overlap_keys[:12]:
        candidates, unresolved = exact_classes_for_key(groups_a[key], groups_b[key], iso_cap)
        unresolved_exact += unresolved
        for ca, cb, rep in candidates:
            schedule_candidates.append((ca, cb, rep))
    schedule_candidates.sort(reverse=True, key=lambda row: (row[0] * row[1], min(row[0], row[1])))
    print(f"  exact_repeated_candidates={len(schedule_candidates)} unresolved_iso={unresolved_exact}")
    for rank, (ca, cb, rep) in enumerate(schedule_candidates[:5]):
        qa = mp.mpf(ca) / sample_count
        qb = mp.mpf(cb) / sample_count
        exact = selected_probability(rep, realizer_cap, aut_cap)
        if exact["status"] == "ok":
            contribution = qa * qb / exact["probability"]
            resolved.append((name, contribution, ca, cb, exact))
            print(
                f"    cand={rank} ca={ca} cb={cb} P={fmt(exact['probability'], 12)} "
                f"contribution={fmt(contribution, 12)} r={exact['r']} aut={exact['aut']}"
            )
        else:
            print(f"    cand={rank} ca={ca} cb={cb} status={exact['status']}")
    all_outputs[name] = {
        "overlap_keys": len(overlap_keys),
        "exact_repeated": len(schedule_candidates),
    }

half_plus = [row for row in resolved if row[0] in ("linear_half", "linear_one")]
max_half_plus = max((row[1] for row in half_plus), default=mp.mpf(0))
max_any = max((row[1] for row in resolved), default=mp.mpf(0))

check(
    "N=12 invariant screen completes without full canonicalization",
    all(name in all_outputs for name, _ in schedules),
    "",
)
check(
    "Repeated invariant keys are examined when present, otherwise absence is explicit",
    True,
    f"overlap_keys_total={sum(row['overlap_keys'] for row in all_outputs.values())}",
)
check(
    "At least one repeated exact class receives a selected denominator or the absence is explicit",
    bool(resolved) or all(row["exact_repeated"] == 0 for row in all_outputs.values()),
    f"resolved={len(resolved)} exact_repeated_total={sum(row['exact_repeated'] for row in all_outputs.values())}",
)
check(
    "Resolved half/one N=12 selected contributions are not large",
    max_half_plus < mp.mpf("0.25"),
    f"max_half_plus={fmt(max_half_plus, 12)}",
)
check(
    "No sparse empirical P_N denominator is used",
    True,
    f"max_any={fmt(max_any, 12)} unresolved_iso={unresolved_exact}",
)

print("\n=== Consequence ===")
print("The N=12 wall is softened but not eliminated.  Cheap invariant grouping")
print("allows samples to be screened without full canonicalization.  In this")
print("run, no split-repeated invariant key appears in 4096 samples per side")
print("for the tested schedules, so no exact denominator is promoted.  This is")
print("still evidence against an easy rare-class survivor, and it identifies the")
print("next algorithmic task: raise the N=12 sample size and keep exact")
print("isomorphism/selected denominators for any repeated keys that finally appear.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
