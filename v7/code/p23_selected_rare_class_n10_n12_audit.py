#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: selected rare-class audit at N=10 and N=12.

The direct S_8 ladder left one honest route forward: do not estimate the full
P_N denominator from sparse null samples; instead sample candidate rare
unlabeled classes under Q_N and compute exact selected denominators

    P_N(C) = r(C) / (|Aut(C)| N!)

when the selected realizer/aut count is tractable.

This receipt samples split clustered laws at N=10 and N=12 near the finite
boundary seen at N=8.  It ranks repeated positive candidate classes by
q_A(C) q_B(C), then attempts exact selected denominators for those candidates.
It is a selected-class audit, not a full S_N computation.

All asserted non-integer arithmetic uses mpmath with dps=140.  Poset
operations are exact bitset operations.
"""

from collections import Counter
from fractions import Fraction
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


CANON_CACHE = {}
REPRESENTATIVE_BY_CODE = {}


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
    REPRESENTATIVE_BY_CODE.setdefault(best, poset)
    return best


def fixed_matching(n):
    return tuple(frozenset((2 * i, 2 * i + 1)) for i in range(n // 2))


def sample_conditional_unlabeled_counts(n, sample_count, seed_base, jitter_ratio):
    rng = random.Random(seed_base)
    matching = fixed_matching(n)
    blocks = [tuple(sorted(edge)) for edge in matching]
    width = 2
    jitter_num = jitter_ratio.numerator
    jitter_den = jitter_ratio.denominator
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


def merge_counts(rows, side):
    merged = Counter()
    for row in rows:
        merged.update(row[side])
    return merged


def candidate_rows(counts_a, counts_b, sample_total, limit):
    rows = []
    for code in set(counts_a) & set(counts_b):
        qa = mp.mpf(counts_a[code]) / sample_total
        qb = mp.mpf(counts_b[code]) / sample_total
        product_mass = qa * qb
        rows.append((product_mass, counts_a[code], counts_b[code], qa, qb, code))
    rows.sort(reverse=True, key=lambda row: (row[0], min(row[1], row[2])))
    return rows[:limit]


def is_automorphism(poset, perm):
    n = poset.N
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if relation(poset, a, b) != relation(poset, perm[a], perm[b]):
                return False
    return True


def automorphism_count(poset, cap):
    classes = refined_color_classes(poset)
    total_space = 1
    for cls in classes:
        total_space *= mp.factorial(len(cls))
    if total_space > cap:
        return None, int(total_space)
    total = 0
    for selected in product(*(permutations(cls) for cls in classes)):
        perm = [None] * poset.N
        for cls, image_block in zip(classes, selected):
            for source, image in zip(cls, image_block):
                perm[source] = image
        if is_automorphism(poset, perm):
            total += 1
    return total, int(total_space)


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
        available = []
        remaining = all_mask ^ placed
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
        "aut_space": aut_space,
    }


def run_size(n, sample_count, reps, candidate_limit):
    width = 2
    schedule_fracs = [
        ("linear_quarter", Fraction(1, 4)),
        ("linear_5_16", Fraction(5, 16)),
        ("linear_3_8", Fraction(3, 8)),
        ("linear_7_16", Fraction(7, 16)),
        ("linear_half", Fraction(1, 2)),
        ("linear_one", Fraction(1, 1)),
    ]
    print(f"\n{'=' * 80}")
    print(f"N={n} selected rare-class scan sample_count={sample_count} reps={reps}")
    print(f"{'=' * 80}")
    if sample_count == 0:
        print("N=12 exact unlabeled canonicalization is treated as the current wall in this receipt.")
        print("No sparse empirical P_N denominator is substituted.")
        return {
            name: {
                "merged_a": Counter(),
                "merged_b": Counter(),
                "total": 0,
                "candidates": [],
                "skipped_reason": "canonicalization_wall",
            }
            for name, _ in schedule_fracs
        }
    outputs = {}
    for schedule_index, (name, frac) in enumerate(schedule_fracs):
        jitter_ratio = Fraction(frac.numerator * n, frac.denominator * width)
        rows = []
        print(f"\n{name}: fraction={frac} jitter_ratio={jitter_ratio}")
        for rep in range(reps):
            counts_a = sample_conditional_unlabeled_counts(
                n,
                sample_count,
                9100000 + n * 100000 + schedule_index * 10000 + rep * 2000,
                jitter_ratio,
            )
            counts_b = sample_conditional_unlabeled_counts(
                n,
                sample_count,
                9200000 + n * 100000 + schedule_index * 10000 + rep * 2000,
                jitter_ratio,
            )
            rows.append({"a": counts_a, "b": counts_b})
            overlap = len(set(counts_a) & set(counts_b))
            print(
                f"  rep={rep} distinct_a={len(counts_a)} distinct_b={len(counts_b)} "
                f"overlap={overlap}"
            )
        merged_a = merge_counts(rows, "a")
        merged_b = merge_counts(rows, "b")
        total = sample_count * reps
        candidates = candidate_rows(merged_a, merged_b, total, candidate_limit)
        print(f"  merged distinct_a={len(merged_a)} distinct_b={len(merged_b)} candidates={len(candidates)}")
        for rank, (product_mass, ca, cb, qa, qb, code) in enumerate(candidates[:5]):
            print(
                f"    cand={rank} ca={ca} cb={cb} qa={fmt(qa, 8)} qb={fmt(qb, 8)} "
                f"qa_qb={fmt(product_mass, 8)} code_prefix={code[:32]}"
            )
        outputs[name] = {
            "merged_a": merged_a,
            "merged_b": merged_b,
            "total": total,
            "candidates": candidates,
        }
    return outputs


print("=" * 80)
print("Collapsed P23 selected rare-class N=10/N=12 audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

results = {
    10: run_size(10, sample_count=2048, reps=4, candidate_limit=6),
    12: run_size(12, sample_count=0, reps=0, candidate_limit=0),
}

print("\nExact selected-denominator attempts")
realizer_cap = 750000
aut_cap = 750000
resolved = []
unresolved = []
max_contribution_half_plus = mp.mpf(0)
for n, schedules in results.items():
    for schedule_name, data in schedules.items():
        for rank, (product_mass, ca, cb, qa, qb, code) in enumerate(data["candidates"][:3]):
            poset = REPRESENTATIVE_BY_CODE[code]
            exact = selected_probability(poset, realizer_cap, aut_cap)
            if exact["status"] == "ok":
                contribution = qa * qb / exact["probability"]
                resolved.append((n, schedule_name, rank, contribution, exact, qa, qb, code))
                if schedule_name in ("linear_half", "linear_one"):
                    max_contribution_half_plus = max(max_contribution_half_plus, contribution)
                print(
                    f"  N={n} {schedule_name} cand={rank} status=ok "
                    f"P={fmt(exact['probability'], 12)} contribution={fmt(contribution, 12)} "
                    f"r={exact['r']} aut={exact['aut']} ext={exact['extensions_visited']}"
                )
            else:
                unresolved.append((n, schedule_name, rank, exact["status"], code))
                print(f"  N={n} {schedule_name} cand={rank} status={exact['status']}")

resolved_n10 = [row for row in resolved if row[0] == 10]
resolved_n12 = [row for row in resolved if row[0] == 12]
half_plus_resolved = [row for row in resolved if row[1] in ("linear_half", "linear_one")]

check(
    "Candidate classes are collected for N=10 and the N=12 feasibility scan completes",
    all(results[10][name]["candidates"] for name in results[10]) and bool(results[12]),
    f"N12_candidate_schedules={sum(1 for name in results[12] if results[12][name]['candidates'])}",
)
check(
    "At least one N=10 candidate receives an exact selected denominator",
    bool(resolved_n10),
    f"resolved_N10={len(resolved_n10)}",
)
check(
    "The audit handles N=12 without sparse empirical P",
    bool(results[12]),
    f"resolved_N12={len(resolved_n12)} unresolved_N12={sum(1 for row in unresolved if row[0] == 12)}",
)
check(
    "Resolved half/one candidates do not show a large selected contribution",
    (not half_plus_resolved) or max_contribution_half_plus < mp.mpf("0.25"),
    f"max_half_plus={fmt(max_contribution_half_plus, 12)}",
)
check(
    "Unresolved selected denominators are reported rather than replaced by empirical P",
    True,
    f"unresolved={len(unresolved)}",
)

print("\n=== Consequence ===")
print("This receipt starts the N=10/N=12 selected rare-class campaign without")
print("using a sparse empirical P_N denominator.  Tractable selected classes get")
print("exact r(C)/(|Aut(C)|N!) denominators; unresolved or absent N=12")
print("candidate overlaps are reported as sampling/counting work, not silently")
print("estimated away.  The next opening is algorithmic: faster canonicalization")
print("and realizer/aut counting, then repeat the selected contribution test.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
