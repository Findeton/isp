#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: overlap-graph cycle-neutrality signature audit.

The cycle-tax receipt showed that common hidden pairs are not the whole
two-replica overlap graph.  For width 2, two hidden explanations are perfect
matchings.  Their union decomposes into alternating components.  The live
boundedness theorem needs nonshared alternating cycles to be neutral, or else a
cycle tax must be included in the second moment.

This receipt tests the next finite shadow.  At exact unlabeled P_8 it fixes all
105 hidden matchings H, samples the conditional clustered law Q_H, and computes

    sum_o q_H(o) q_H'(o) / p(o)

for every pair H,H'.  Cross factors are grouped by the full overlap-graph
signature, e.g.:

    (4,)      one nonshared alternating 8-cycle;
    (2, 2)    two nonshared alternating 4-cycles;
    (1, 3)    one common pair plus one nonshared 6-cycle.

If nonshared cycles carried a stable factor, signatures with more nonshared
components should separate from the single-cycle signatures at zero common
overlap.  This finite audit instead checks whether zero-common signatures stay
near the null scale.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import Counter, defaultdict
from itertools import permutations, product
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


def coordinate_order_poset(points):
    future = [0] * len(points)
    for i, (ui, vi) in enumerate(points):
        mask = 0
        for j, (uj, vj) in enumerate(points):
            if ui < uj and vi < vj:
                mask |= 1 << j
        future[i] = mask
    return Poset(future)


CANON_CACHE = {}


def refined_color_classes(poset):
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
            break
        colors = new_colors
    classes = {}
    for i, color in enumerate(colors):
        classes.setdefault(color, []).append(i)
    return [tuple(classes[color]) for color in sorted(classes)]


def code_for_order(poset, order):
    bits = []
    for i, a in enumerate(order):
        future = poset.future[a]
        for j, b in enumerate(order):
            if i != j:
                bits.append("1" if future & (1 << b) else "0")
    return "".join(bits)


def canonical_unlabeled_code(poset):
    cached = CANON_CACHE.get(poset.future)
    if cached is not None:
        return cached
    classes = refined_color_classes(poset)
    best = None
    for selected in product(*(permutations(cls) for cls in classes)):
        order = tuple(v for block in selected for v in block)
        code = code_for_order(poset, order)
        if best is None or code < best:
            best = code
    CANON_CACHE[poset.future] = best
    return best


def exact_unlabeled_sprinkling_law(n):
    counts = Counter()
    for perm in permutations(range(n)):
        counts[canonical_unlabeled_code(poset_from_permutation(perm))] += 1
    total = mp.mpf(sum(counts.values()))
    return {code: mp.mpf(count) / total for code, count in counts.items()}


def perfect_matchings(labels):
    labels = tuple(labels)
    if not labels:
        yield tuple()
        return
    first = labels[0]
    rest = labels[1:]
    for index, second in enumerate(rest):
        pair = frozenset((first, second))
        remaining = rest[:index] + rest[index + 1 :]
        for tail in perfect_matchings(remaining):
            yield tuple(sorted((pair,) + tail, key=lambda e: tuple(e)))


def overlap_graph_signature(matching_a, matching_b, n):
    set_a = set(matching_a)
    set_b = set(matching_b)
    adj = [[] for _ in range(n)]
    for edge in set_a | set_b:
        x, y = tuple(edge)
        adj[x].append(y)
        adj[y].append(x)
    seen = [False] * n
    parts = []
    for start in range(n):
        if seen[start]:
            continue
        stack = [start]
        seen[start] = True
        vertices = []
        while stack:
            x = stack.pop()
            vertices.append(x)
            for y in adj[x]:
                if not seen[y]:
                    seen[y] = True
                    stack.append(y)
        vertex_set = set(vertices)
        h_edges = sum(1 for edge in set_a if edge <= vertex_set)
        parts.append(h_edges)
    return tuple(sorted(parts))


def common_pair_count(signature):
    return sum(1 for part in signature if part == 1)


def nonshared_component_count(signature):
    return sum(1 for part in signature if part > 1)


def sample_conditional_unlabeled_counts(n, matching, sample_count, seed_base, jitter_num, jitter_den):
    rng = random.Random(seed_base)
    blocks = [tuple(sorted(edge)) for edge in matching]
    width = 2
    scale = 10000 * jitter_den
    span = 10000 * jitter_num
    counts = Counter()
    tie = n + 1
    for _ in range(sample_count):
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
        counts[canonical_unlabeled_code(coordinate_order_poset(points))] += 1
    return counts


def weights_from_counts(counts):
    total = mp.mpf(sum(counts.values()))
    return {code: mp.mpf(count) / total for code, count in counts.items()}


def cross_factor(weights_a, weights_b, p_inv):
    if len(weights_a) > len(weights_b):
        weights_a, weights_b = weights_b, weights_a
    value = mp.mpf(0)
    for code, qa in weights_a.items():
        qb = weights_b.get(code)
        if qb is not None:
            value += qa * qb * p_inv[code]
    return value


print("=" * 80)
print("Collapsed P23 overlap-graph cycle-neutrality signature audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 8
sample_count = 1024
matchings = list(perfect_matchings(range(n)))
print(f"N={n} matchings={len(matchings)} sample_count_per_H={sample_count}")
p_law = exact_unlabeled_sprinkling_law(n)
p_inv = {code: 1 / p for code, p in p_law.items()}
print(f"exact unlabeled P_8 support={len(p_law)}")

schedules = [
    ("linear_half", n // 2, 2),
    ("linear_one", n, 2),
    ("linear_two", 2 * n, 2),
]

all_support_ok = True
zero_common_means_near_null = True
two_cycle_mean_neutral = True
signature_coverage_ok = True
rows_for_claim = []

for schedule_index, (schedule_name, jitter_num, jitter_den) in enumerate(schedules):
    print(f"\nSchedule {schedule_name}: jitter={jitter_num}/{jitter_den}")
    q_counts = {}
    q_weights = {}
    for h_index, matching in enumerate(matchings):
        counts = sample_conditional_unlabeled_counts(
            n,
            matching,
            sample_count,
            5400000 + schedule_index * 500000 + h_index * 1009,
            jitter_num,
            jitter_den,
        )
        all_support_ok = all_support_ok and all(code in p_law for code in counts)
        q_counts[matching] = counts
        q_weights[matching] = weights_from_counts(counts)

    groups = defaultdict(list)
    group_means = {}
    for ha in matchings:
        for hb in matchings:
            signature = overlap_graph_signature(ha, hb, n)
            value = cross_factor(q_weights[ha], q_weights[hb], p_inv)
            groups[signature].append(value)

    print("  signature summary:")
    for signature in sorted(groups, key=lambda s: (common_pair_count(s), s)):
        values = groups[signature]
        mean = mp.fsum(values) / len(values)
        group_means[signature] = mean
        maximum = max(values)
        minimum = min(values)
        rows_for_claim.append((schedule_name, signature, len(values), minimum, mean, maximum))
        print(
            f"    sig={signature} count={len(values)} common={common_pair_count(signature)} "
            f"nonshared={nonshared_component_count(signature)} "
            f"min={fmt(minimum, 12)} mean={fmt(mean, 12)} max={fmt(maximum, 12)}"
        )
        if common_pair_count(signature) == 0:
            zero_common_means_near_null = zero_common_means_near_null and abs(mean - 1) < mp.mpf("0.01")

    ratio_22_4 = group_means[(2, 2)] / group_means[(4,)]
    two_cycle_mean_neutral = two_cycle_mean_neutral and abs(ratio_22_4 - 1) < mp.mpf("0.01")
    print(f"  zero-common comparison: mean(2,2)/mean(4)={fmt(ratio_22_4, 18)}")

signature_coverage_ok = set(signature for _, signature, *_ in rows_for_claim) == {
    (4,),
    (2, 2),
    (1, 3),
    (1, 1, 2),
    (1, 1, 1, 1),
}

check("Exact unlabeled P_8 law and all hidden matchings are used", len(p_law) == 14794 and len(matchings) == 105, "")
check("Conditional samples stay inside exact unlabeled P_8 support", all_support_ok, "")
check("All width-2 overlap graph signatures at N=8 are covered", signature_coverage_ok, "")
check("Zero-common signature means stay near the null scale", zero_common_means_near_null, "|mean-1| < 0.01")
check("Two zero-common cycles do not show a larger mean factor than one zero-common cycle", two_cycle_mean_neutral, "|mean(2,2)/mean(4)-1| < 0.01")

print("\n=== Consequence ===")
print("At exact unlabeled P_8, the zero-common signatures (4,) and (2,2)")
print("remain close to the null scale, and two nonshared cycles are not worse")
print("than one.  This is finite evidence for cycle neutrality, not a proof.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
