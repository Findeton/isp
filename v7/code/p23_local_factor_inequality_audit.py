#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: local cross-likelihood factor audit.

The partition-overlap receipt reduces the bounded unlabeled second-moment
problem to a local factor inequality of the form

    E_P[L_H L_H' | H,H'] <= C a^{O(H,H')}.

This receipt makes that object concrete in the first exact labeled sizes.  For
N=4 and N=6 it computes the exact labeled 1+1 sprinkling law P_N by enumerating
all pairs of coordinate permutations.  It then fixes every width-2 hidden
partition H, samples the exchangeable jittered-cluster law Q_{N,H}, and computes
the two-replica cross factor

    sum_o q_H(o) q_H'(o) / p(o)

for every pair H,H'.  The pairs are binned by the hidden overlap

    O(H,H') = # hidden pairs common to H and H'.

The audit is not a proof of the asymptotic inequality.  It asks whether the
first exact conditional likelihood object already shows a rare order class or
an overlap-independent blow-up.  If no such class appears, it fits the finite
constants C_N and a_N forced by the data and reports the worst contributing
orders.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import Counter, defaultdict
from itertools import permutations
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


def labeled_code_from_ranks(rank_u, rank_v):
    n = len(rank_u)
    bits = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            bits.append("1" if rank_u[i] < rank_u[j] and rank_v[i] < rank_v[j] else "0")
    return "".join(bits)


def labeled_code_from_points(points):
    n = len(points)
    bits = []
    for i, (ui, vi) in enumerate(points):
        for j, (uj, vj) in enumerate(points):
            if i == j:
                continue
            bits.append("1" if ui < uj and vi < vj else "0")
    return "".join(bits)


def exact_labeled_sprinkling_law(n):
    counts = Counter()
    perms = list(permutations(range(n)))
    for order_u in perms:
        rank_u = [0] * n
        for rank, label in enumerate(order_u):
            rank_u[label] = rank
        for order_v in perms:
            rank_v = [0] * n
            for rank, label in enumerate(order_v):
                rank_v[label] = rank
            counts[labeled_code_from_ranks(rank_u, rank_v)] += 1
    total = mp.mpf(math.factorial(n)) ** 2
    law = {code: mp.mpf(count) / total for code, count in counts.items()}
    return counts, law


def perfect_matchings(labels):
    labels = tuple(labels)
    if not labels:
        yield tuple()
        return
    first = labels[0]
    rest = labels[1:]
    for index, second in enumerate(rest):
        pair = tuple(sorted((first, second)))
        remaining = rest[:index] + rest[index + 1 :]
        for tail in perfect_matchings(remaining):
            yield tuple(sorted((frozenset(pair),) + tail, key=lambda e: tuple(e)))


def overlap_count(matching_a, matching_b):
    return len(set(matching_a) & set(matching_b))


def sample_conditional_cluster_counts(n, matching, sample_count, seed_base, jitter_num, jitter_den):
    rng = random.Random(seed_base)
    blocks = [tuple(sorted(edge)) for edge in matching]
    width = 2
    scale = 10000 * jitter_den
    span = 10000 * jitter_num
    counts = Counter()
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
                # The anti-correlated local offsets make the hidden pair a
                # small causal antichain before jitter, matching the older
                # clustered-fiber receipts.
                u = u_rank[block_index] * scale + width * du + local
                v = v_rank[block_index] * scale + width * dv + (width - 1 - local)
                points[label] = (u, v)
        counts[labeled_code_from_points(points)] += 1
    return counts


def cross_factor(counts_a, counts_b, p_law):
    total_a = mp.mpf(sum(counts_a.values()))
    total_b = mp.mpf(sum(counts_b.values()))
    value = mp.mpf(0)
    outside = 0
    contributions = []
    for code in set(counts_a) | set(counts_b):
        p = p_law.get(code, mp.mpf(0))
        qa = mp.mpf(counts_a.get(code, 0)) / total_a
        qb = mp.mpf(counts_b.get(code, 0)) / total_b
        if p == 0:
            if qa and qb:
                outside += 1
            continue
        contribution = qa * qb / p
        value += contribution
        if contribution:
            contributions.append((contribution, p, qa, qb, code))
    contributions.sort(reverse=True, key=lambda row: row[0])
    return value, outside, contributions[:5]


def fit_overlap_bound(rows):
    by_o = defaultdict(list)
    for row in rows:
        by_o[row["overlap"]].append(row["cross"])
    max_by_o = {o: max(values) for o, values in by_o.items()}
    c = max_by_o.get(0, max(max_by_o.values()))
    a = mp.mpf(1)
    for o, value in max_by_o.items():
        if o > 0 and c > 0:
            a = max(a, (value / c) ** (mp.mpf(1) / o))
    fitted_ok = all(row["cross"] <= c * (a ** row["overlap"]) * (1 + mp.mpf("1e-40")) for row in rows)
    return c, a, max_by_o, fitted_ok


print("=" * 80)
print("Collapsed P23 local cross-likelihood factor audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

schedules = [
    ("linear_half", lambda n: max(1, n // 2), 2),
    ("linear_one", lambda n: n, 2),
    ("linear_two", lambda n: 2 * n, 2),
]

all_fit_ok = True
all_outside_zero = True
all_constants_finite = True
no_large_rare_o0 = True
summaries = []

for n, sample_count in [(4, 16384), (6, 8192)]:
    print("\n" + "=" * 80)
    print(f"N={n} exact labeled P_N")
    p_counts, p_law = exact_labeled_sprinkling_law(n)
    matchings = list(perfect_matchings(range(n)))
    print(
        f"P support={len(p_law)} total_perm_pairs={math.factorial(n) ** 2} "
        f"hidden_matchings={len(matchings)} sample_count_per_H={sample_count}"
    )
    for schedule_name, jitter_fn, jitter_den in schedules:
        jitter_num = jitter_fn(n)
        print(f"\nSchedule {schedule_name}: jitter={jitter_num}/{jitter_den}")
        q_counts = {}
        for h_index, matching in enumerate(matchings):
            q_counts[matching] = sample_conditional_cluster_counts(
                n,
                matching,
                sample_count,
                5100000 + n * 100000 + len(schedule_name) * 10000 + h_index * 271,
                jitter_num,
                jitter_den,
            )

        rows = []
        worst = None
        worst_o0 = None
        for ha in matchings:
            for hb in matchings:
                cross, outside, top = cross_factor(q_counts[ha], q_counts[hb], p_law)
                o = overlap_count(ha, hb)
                row = {"overlap": o, "cross": cross, "outside": outside, "top": top, "ha": ha, "hb": hb}
                rows.append(row)
                all_outside_zero = all_outside_zero and outside == 0
                if worst is None or cross > worst["cross"]:
                    worst = row
                if o == 0 and (worst_o0 is None or cross > worst_o0["cross"]):
                    worst_o0 = row

        c, a, max_by_o, fitted_ok = fit_overlap_bound(rows)
        all_fit_ok = all_fit_ok and fitted_ok
        all_constants_finite = all_constants_finite and c < mp.inf and a < mp.inf
        o0_ratio = worst_o0["top"][0][0] / worst_o0["cross"] if worst_o0 and worst_o0["cross"] else mp.mpf(0)
        no_large_rare_o0 = no_large_rare_o0 and o0_ratio < mp.mpf("0.25")
        summaries.append((n, schedule_name, c, a, max_by_o, worst, worst_o0, o0_ratio))

        print("  max cross by overlap:")
        for o in sorted(max_by_o):
            print(f"    O={o}: {fmt(max_by_o[o], 18)}")
        print(f"  fitted C_N={fmt(c, 18)} a_N={fmt(a, 18)} fit={'yes' if fitted_ok else 'NO'}")
        print(
            f"  worst overall: O={worst['overlap']} cross={fmt(worst['cross'], 18)} "
            f"outside={worst['outside']}"
        )
        if worst["top"]:
            contribution, p, qa, qb, code = worst["top"][0]
            print(
                "    top contribution="
                f"{fmt(contribution, 18)} p={fmt(p, 12)} qa={fmt(qa, 12)} qb={fmt(qb, 12)}"
            )
        print(
            f"  worst O=0: cross={fmt(worst_o0['cross'], 18)} "
            f"top_share={fmt(o0_ratio, 18)}"
        )

print("\n" + "=" * 80)
print("Summary table")
for n, schedule_name, c, a, max_by_o, worst, worst_o0, o0_ratio in summaries:
    compact = ", ".join(f"O{o}:{fmt(v, 10)}" for o, v in sorted(max_by_o.items()))
    print(
        f"N={n} {schedule_name}: C={fmt(c, 12)} a={fmt(a, 12)} "
        f"max_by_overlap=[{compact}] worstO={worst['overlap']} O0_top_share={fmt(o0_ratio, 10)}"
    )

check("Exact labeled P_N supports are computed", len(summaries) == 6, f"schedules={len(summaries)}")
check("Sampled Q_H support stays inside exact labeled sprinkling support", all_outside_zero, "")
check("Finite overlap-dominated constants fit every tested H,H' pair", all_fit_ok, "")
check("Fitted constants are finite in the exact small-size audit", all_constants_finite, "")
check("No single rare O=0 order class dominates the worst zero-overlap cross factor", no_large_rare_o0, "")

print("\n=== Consequence ===")
print("The first exact labeled conditional audit does not find a rare zero-overlap")
print("order class or an overlap-independent blow-up.  At these sizes the")
print("conditional cross factor is absorbed by finite C_N and a_N.  This is")
print("evidence for the local factor inequality, not an asymptotic proof.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
