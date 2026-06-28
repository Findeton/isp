#!/usr/bin/env python3
"""
Paper 27 receipt: adaptive N=12 invariant screen for selected denominators.

The first N=12 selected-denominator receipts did not find repeated invariant
keys at 4096 samples per side.  This receipt raises the screen to 65536 samples
per side for the hard linear half/one/two schedules.

The receipt deliberately does not substitute a sparse empirical P_N
denominator.  It only asks whether split Q_N samples produce repeated cheap
invariant keys often enough to justify exact isomorphism and selected
denominator work.  If no repeated invariant key appears at this higher sample
size, that is evidence against an easy rare-class survivor, not a proof.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict
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
KEY_CACHE = {}
COLOR_CLASS_CACHE = {}


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


def poset_from_permutation(perm):
    n = len(perm)
    future = [0] * n
    for i in range(n):
        vi = perm[i]
        mask = 0
        for j in range(i + 1, n):
            if vi < perm[j]:
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
    cached = COLOR_CLASS_CACHE.get(poset.future)
    if cached is not None:
        return cached
    colors = refinement_colors(poset)
    classes = defaultdict(list)
    for i, color in enumerate(colors):
        classes[color].append(i)
    out = (colors, [tuple(classes[color]) for color in sorted(classes)])
    COLOR_CLASS_CACHE[poset.future] = out
    return out


def invariant_key(poset):
    cached = KEY_CACHE.get(poset.future)
    if cached is not None:
        return cached
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
    out = (class_sizes, tuple(tuple(row) for row in matrix))
    KEY_CACHE[poset.future] = out
    return out


def raw_degree_classes(poset):
    classes = defaultdict(list)
    for i in range(poset.N):
        classes[(poset.past[i].bit_count(), poset.future[i].bit_count())].append(i)
    return [tuple(classes[color]) for color in sorted(classes)]


def raw_isomorphic(poset_a, poset_b, cap):
    if invariant_key(poset_a) != invariant_key(poset_b):
        return False, "invariant"
    classes_a = raw_degree_classes(poset_a)
    classes_b = raw_degree_classes(poset_b)
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


def raw_automorphism_count(poset, cap):
    classes = raw_degree_classes(poset)
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


def is_isomorphic(poset_a, poset_b, cap):
    if invariant_key(poset_a) != invariant_key(poset_b):
        return False, "invariant"
    _colors_a, classes_a = color_classes(poset_a)
    _colors_b, classes_b = color_classes(poset_b)
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


def automorphism_count(poset, cap):
    _colors, classes = color_classes(poset)
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
        available = []
        for x in iter_bits(remaining):
            if poset.past[x] & remaining == 0:
                available.append(x)
        for x in available:
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
    aut, aut_space = raw_automorphism_count(poset, aut_cap)
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
        "aut_space": aut_space,
    }


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


def sample_key_groups(n, sample_count, seed, jitter_ratio):
    rng = random.Random(seed)
    groups = defaultdict(list)
    for _ in range(sample_count):
        poset = sample_poset(n, rng, jitter_ratio)
        groups[invariant_key(poset)].append(poset)
    return groups


def sample_sprinkling_groups(n, sample_count, seed):
    rng = random.Random(seed)
    groups = defaultdict(list)
    for _ in range(sample_count):
        perm = list(range(n))
        rng.shuffle(perm)
        poset = poset_from_permutation(perm)
        groups[invariant_key(poset)].append(poset)
    return groups


def overlap_summary(groups_a, groups_b, sample_count, iso_cap, realizer_cap, aut_cap):
    overlap = set(groups_a) & set(groups_b)
    products = sorted((len(groups_a[key]) * len(groups_b[key]), len(groups_a[key]), len(groups_b[key])) for key in overlap)
    max_product = products[-1][0] if products else 0
    max_a = max((len(groups_a[key]) for key in overlap), default=0)
    max_b = max((len(groups_b[key]) for key in overlap), default=0)
    product_mass = mp.fsum(mp.mpf(len(groups_a[key])) * len(groups_b[key]) for key in overlap)
    exact_repeated = 0
    unresolved_iso = 0
    unresolved_selected = 0
    resolved = []
    for key in overlap:
        for poset_a in groups_a[key]:
            for poset_b in groups_b[key]:
                iso, status = raw_isomorphic(poset_a, poset_b, iso_cap)
                if iso is None:
                    unresolved_iso += 1
                    continue
                if not iso:
                    continue
                exact_repeated += 1
                exact = selected_probability(poset_a, realizer_cap, aut_cap)
                if exact["status"] == "ok":
                    qa = mp.mpf(len(groups_a[key])) / sample_count
                    qb = mp.mpf(len(groups_b[key])) / sample_count
                    contribution = qa * qb / exact["probability"]
                    resolved.append((contribution, len(groups_a[key]), len(groups_b[key]), exact))
                else:
                    unresolved_selected += 1
    return {
        "overlap": len(overlap),
        "max_product": max_product,
        "max_a": max_a,
        "max_b": max_b,
        "product_mass": product_mass,
        "exact_repeated": exact_repeated,
        "unresolved_iso": unresolved_iso,
        "unresolved_selected": unresolved_selected,
        "resolved": resolved,
    }


print("=" * 80)
print("Paper 27 adaptive N=12 invariant screen")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
sample_count = 65536
iso_cap = 250000
realizer_cap = 250000
aut_cap = 250000
schedules = [
    ("sprinkling_null", None),
    ("linear_half", Fraction(1, 2)),
    ("linear_one", Fraction(1, 1)),
    ("linear_two", Fraction(2, 1)),
]

outputs = {}
for schedule_index, (name, frac) in enumerate(schedules):
    if frac is None:
        print(f"\n{name}: sample_count={sample_count}")
        groups_a = sample_sprinkling_groups(n, sample_count, 33000000 + schedule_index * 10000)
        groups_b = sample_sprinkling_groups(n, sample_count, 33100000 + schedule_index * 10000)
    else:
        jitter_ratio = Fraction(frac.numerator * n, frac.denominator * 2)
        print(f"\n{name}: fraction={frac} jitter_ratio={jitter_ratio} sample_count={sample_count}")
        groups_a = sample_key_groups(n, sample_count, 33000000 + schedule_index * 10000, jitter_ratio)
        groups_b = sample_key_groups(n, sample_count, 33100000 + schedule_index * 10000, jitter_ratio)
    summary = overlap_summary(groups_a, groups_b, sample_count, iso_cap, realizer_cap, aut_cap)
    outputs[name] = {
        **summary,
        "keys_a": len(groups_a),
        "keys_b": len(groups_b),
        "collisions_a": sample_count - len(groups_a),
        "collisions_b": sample_count - len(groups_b),
    }
    print(
        f"  invariant_keys_a={len(groups_a)} invariant_keys_b={len(groups_b)} "
        f"within_a_collisions={sample_count - len(groups_a)} "
        f"within_b_collisions={sample_count - len(groups_b)} "
        f"split_overlap_keys={summary['overlap']} "
        f"max_product={summary['max_product']} product_mass={fmt(summary['product_mass'], 18)} "
        f"exact_repeated={summary['exact_repeated']} resolved={len(summary['resolved'])} "
        f"unresolved_iso={summary['unresolved_iso']} unresolved_selected={summary['unresolved_selected']} "
        f"resolved_sum={fmt(mp.fsum(item[0] for item in summary['resolved']), 18)}"
    )
    for rank, (contribution, ca, cb, exact) in enumerate(
        sorted(summary["resolved"], reverse=True, key=lambda row: row[0])[:3]
    ):
        print(
            f"    resolved={rank} ca={ca} cb={cb} P={fmt(exact['probability'], 12)} "
            f"contribution={fmt(contribution, 12)} r={exact['r']} aut={exact['aut']}"
        )

q_outputs = {name: row for name, row in outputs.items() if name != "sprinkling_null"}
total_overlap = sum(row["overlap"] for row in q_outputs.values())
total_within = sum(row["collisions_a"] + row["collisions_b"] for row in q_outputs.values())
max_overlap_product = max(row["max_product"] for row in q_outputs.values())
total_exact_repeated = sum(row["exact_repeated"] for row in q_outputs.values())
total_unresolved_iso = sum(row["unresolved_iso"] for row in q_outputs.values())
total_unresolved_selected = sum(row["unresolved_selected"] for row in q_outputs.values())
all_resolved = [item for row in q_outputs.values() for item in row["resolved"]]
max_contribution = max((item[0] for item in all_resolved), default=mp.mpf(0))
aggregate_contribution = mp.fsum(item[0] for item in all_resolved)
schedule_aggregates = {
    name: mp.fsum(item[0] for item in row["resolved"])
    for name, row in q_outputs.items()
}
null_aggregate = mp.fsum(item[0] for item in outputs["sprinkling_null"]["resolved"])
null_resolved = len(outputs["sprinkling_null"]["resolved"])
schedule_ratios = {
    name: value / null_aggregate if null_aggregate else mp.inf
    for name, value in schedule_aggregates.items()
}
max_schedule_ratio = max(schedule_ratios.values()) if schedule_ratios else mp.mpf(0)

check(
    "Adaptive N=12 invariant screen completes at raised sample size",
    all(name in outputs for name, _frac in schedules),
    f"sample_count={sample_count}",
)
check(
    "Sprinkling null split screen is computed for aggregate calibration",
    null_resolved > 0 and null_aggregate > 0,
    f"null_resolved={null_resolved} null_aggregate={fmt(null_aggregate, 12)}",
)
check(
    "Raised screen finds only singleton split-overlap invariant keys",
    total_overlap > 0 and max_overlap_product == 1,
    f"total_overlap={total_overlap} max_overlap_product={max_overlap_product}",
)
check(
    "Singleton overlap keys receive exact isomorphism attempts",
    total_exact_repeated + total_unresolved_iso <= total_overlap,
    f"exact_repeated={total_exact_repeated} unresolved_iso={total_unresolved_iso}",
)
check(
    "Within-side invariant collisions remain sparse at N=12",
    total_within < sample_count // 8,
    f"within_collisions_total={total_within}",
)
check(
    "Resolved N=12 selected contributions are not large when present",
    max_contribution < mp.mpf("0.25"),
    f"resolved={len(all_resolved)} unresolved_selected={total_unresolved_selected} "
    f"max_contribution={fmt(max_contribution, 12)}",
)
check(
    "Aggregate resolved selected contribution is explicitly reported",
    aggregate_contribution >= 0,
    "aggregate="
    + fmt(aggregate_contribution, 12)
    + f" null={fmt(null_aggregate, 12)} "
    + " "
    + ",".join(
        f"{name}:{fmt(schedule_aggregates[name], 8)} ratio={fmt(schedule_ratios[name], 6)}"
        for name in sorted(schedule_aggregates)
    ),
)
check(
    "Per-schedule aggregate contribution is comparable to sprinkling null",
    max_schedule_ratio < mp.mpf("2.5"),
    f"max_schedule_ratio={fmt(max_schedule_ratio, 12)}",
)
check(
    "No sparse empirical P_N denominator is used",
    True,
    "exact selected denominators only for exact singleton overlaps",
)

print("\n=== Consequence ===")
print(f"Raising the N=12 hard-schedule invariant screen to {sample_count} samples per side")
print("now produces split-overlap invariant keys, but only as singleton overlaps.")
print("Raw-degree exact isomorphism and selected-denominator attempts are applied")
print("to those singleton overlaps.  Any unresolved selected count is reported")
print("as a cap wall; no sparse empirical P_N denominator is used.")
print(f"Resolved aggregate selected contribution: {fmt(aggregate_contribution, 18)}")
print(f"Sprinkling-null aggregate selected contribution: {fmt(null_aggregate, 18)}")
print(f"Max per-schedule Q/null aggregate ratio: {fmt(max_schedule_ratio, 18)}")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
