#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: split-sample diagonal artifact audit.

The previous exact-P8 component audit saw a large same-hidden-matching
"identity" spike.  This receipt hostile-tests whether that spike belongs to
the true unlabeled likelihood, or to the empirical plug-in estimator

    sum_o q_hat_H(o)^2 / p(o)

that reuses the same finite histogram on both sides.

For each hidden matching H it draws two independent conditional histograms
q_hat_H^A and q_hat_H^B.  It compares:

    reuse(H)      = sum_o q_hat_H^A(o) q_hat_H^A(o) / p(o),
    split_same(H) = sum_o q_hat_H^A(o) q_hat_H^B(o) / p(o),
    split_diff(H,H') for H != H'.

If the large diagonal was real, split_same should remain large.  If it was a
finite-histogram self-collision artifact, split_same should fall back to the
same scale as split_diff.

The conceptual theorem behind the test is simple.  If the conditional labeled
cluster law is equivariant under record relabeling, then after quotienting to
unlabeled orders every hidden matching has the same law q_H = q.  Hence the
true cross factor is independent of H,H':

    sum_o q_H(o) q_H'(o) / p(o) = sum_o q(o)^2 / p(o).

So hidden-identity rarity cannot by itself prove washout.  The actual target
is the direct unlabeled likelihood second moment of the one clustered law.

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


def exact_zero_jitter_counts(n, matching):
    blocks = [tuple(sorted(edge)) for edge in matching]
    width = 2
    scale = 10000
    counts = Counter()
    for u_block_order in permutations(range(len(blocks))):
        for v_block_order in permutations(range(len(blocks))):
            u_rank = [0] * len(blocks)
            v_rank = [0] * len(blocks)
            for rank, block_index in enumerate(u_block_order):
                u_rank[block_index] = rank
            for rank, block_index in enumerate(v_block_order):
                v_rank[block_index] = rank
            for local_bits in product((0, 1), repeat=len(blocks)):
                points = [None] * n
                for block_index, block in enumerate(blocks):
                    local_order = block if local_bits[block_index] == 0 else tuple(reversed(block))
                    for local, label in enumerate(local_order):
                        u = u_rank[block_index] * scale + local
                        v = v_rank[block_index] * scale + (width - 1 - local)
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


def mean(values):
    return mp.fsum(values) / len(values)


print("=" * 80)
print("Collapsed P23 split-sample diagonal artifact audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 8
sample_count = 1024
matchings = list(perfect_matchings(range(n)))
p_law = exact_unlabeled_sprinkling_law(n)
p_inv = {code: 1 / p for code, p in p_law.items()}
print(f"N={n} exact_P_support={len(p_law)} matchings={len(matchings)} sample_count_per_half={sample_count}")

print("\nExact sharp-cluster baseline")
sharp_counts = exact_zero_jitter_counts(n, matchings[0])
sharp_weights = weights_from_counts(sharp_counts)
sharp_second = cross_factor(sharp_weights, sharp_weights, p_inv)
print(
    f"  zero-jitter exact outcomes={sum(sharp_counts.values())} "
    f"support={len(sharp_counts)} second={fmt(sharp_second, 18)} "
    f"chi2={fmt(sharp_second - 1, 18)}"
)

schedules = [
    ("linear_half", n // 2, 2),
    ("linear_one", n, 2),
    ("linear_two", 2 * n, 2),
]

all_support_ok = True
all_reuse_spikes = True
all_split_same_near_diff = True
all_split_near_null = True
all_signature_flat = True
all_linear_below_sharp = True

for schedule_index, (schedule_name, jitter_num, jitter_den) in enumerate(schedules):
    print(f"\nSchedule {schedule_name}: jitter={jitter_num}/{jitter_den}")
    weights_a = {}
    weights_b = {}
    for h_index, matching in enumerate(matchings):
        counts_a = sample_conditional_unlabeled_counts(
            n,
            matching,
            sample_count,
            6200000 + schedule_index * 700000 + h_index * 2003,
            jitter_num,
            jitter_den,
        )
        counts_b = sample_conditional_unlabeled_counts(
            n,
            matching,
            sample_count,
            6400000 + schedule_index * 700000 + h_index * 2011,
            jitter_num,
            jitter_den,
        )
        all_support_ok = all_support_ok and all(code in p_law for code in counts_a)
        all_support_ok = all_support_ok and all(code in p_law for code in counts_b)
        weights_a[matching] = weights_from_counts(counts_a)
        weights_b[matching] = weights_from_counts(counts_b)

    reuse_values = [cross_factor(weights_a[h], weights_a[h], p_inv) for h in matchings]
    split_same_values = [cross_factor(weights_a[h], weights_b[h], p_inv) for h in matchings]

    diff_groups = defaultdict(list)
    for ha in matchings:
        for hb in matchings:
            if ha == hb:
                continue
            signature = overlap_graph_signature(ha, hb, n)
            diff_groups[signature].append(cross_factor(weights_a[ha], weights_b[hb], p_inv))

    reuse_mean = mean(reuse_values)
    split_same_mean = mean(split_same_values)
    diff_mean = mean([value for values in diff_groups.values() for value in values])
    diff_signature_means = {signature: mean(values) for signature, values in diff_groups.items()}
    max_signature_gap = max(abs(value - diff_mean) for value in diff_signature_means.values())
    split_same_gap = abs(split_same_mean - diff_mean)

    print(f"  reuse same histogram mean      = {fmt(reuse_mean, 18)}")
    print(f"  split same H mean              = {fmt(split_same_mean, 18)}")
    print(f"  split different H mean         = {fmt(diff_mean, 18)}")
    print(f"  reuse/split_same               = {fmt(reuse_mean / split_same_mean, 18)}")
    print(f"  |split_same - split_diff|      = {fmt(split_same_gap, 18)}")
    print(f"  max signature gap from diff    = {fmt(max_signature_gap, 18)}")
    for signature in sorted(diff_signature_means):
        print(f"    split_diff mean {signature}: {fmt(diff_signature_means[signature], 18)}")

    all_reuse_spikes = all_reuse_spikes and reuse_mean / split_same_mean > mp.mpf("5")
    all_split_same_near_diff = all_split_same_near_diff and split_same_gap < mp.mpf("0.08")
    all_split_near_null = all_split_near_null and abs(split_same_mean - 1) < mp.mpf("0.08") and abs(diff_mean - 1) < mp.mpf("0.08")
    all_signature_flat = all_signature_flat and max_signature_gap < mp.mpf("0.08")
    all_linear_below_sharp = all_linear_below_sharp and abs(split_same_mean - 1) < (sharp_second - 1) / 4

check("Exact P_8 support and all matchings are used", len(p_law) == 14794 and len(matchings) == 105, "")
check("Conditional samples remain inside exact P_8 support", all_support_ok, "")
check("Exact zero-jitter clustered law has a real unlabeled likelihood excess", sharp_second > mp.mpf("2"), f"second={fmt(sharp_second, 12)}")
check("Same-histogram reuse creates a large artificial diagonal spike", all_reuse_spikes, "reuse/split_same > 5")
check("Split same-H diagonal returns to split different-H scale", all_split_same_near_diff, "|split_same - split_diff| < 0.08")
check("Split estimates stay near the null second-moment scale", all_split_near_null, "split means within 0.08 of 1")
check("Non-identical overlap signatures are flat under split estimation", all_signature_flat, "signature gaps < 0.08")
check("Linear-jitter split likelihood is much closer to null than zero-jitter clustering", all_linear_below_sharp, "")

print("\n=== Consequence ===")
print("The large exact-P8 'identity' spike is not promoted by this audit.")
print("It appears when the same finite empirical histogram is used twice.")
print("With independent halves, the same-H diagonal falls back to the same")
print("scale as different-H cross factors.  The hidden-matching diagonal-rarity")
print("route is therefore the wrong theorem target unless a non-empirical")
print("calculation finds a real same-H excess.")
print("The exact zero-jitter clustered law still has a real excess, so the")
print("test is not blind: it distinguishes sharp clustering from linear")
print("jitter washout.")
print("The honest target is now the direct unlabeled likelihood second moment")
print("of the clustered law itself, estimated by split samples or proved by an")
print("equivariant quotient argument plus a law-distance bound.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
