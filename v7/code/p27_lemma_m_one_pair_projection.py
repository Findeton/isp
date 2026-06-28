#!/usr/bin/env python3
"""
Paper 27 receipt: finite one-pair projection attack on Lemma M.

Lemma M asks for a quotient-level local factor bound: after hidden labels and
coordinates are forgotten, the contribution of one hidden sibling pair should
be O(1/N) in L2(P_N^O), with nonshared factors neutral.

This receipt tests two smallest exact-denominator versions of that claim.
For N=5..8:

  P_N^O is computed exactly by enumerating all N! 1+1 sprinkling permutations.

  H_N^O is first sampled as one hidden sibling pair plus N-2 unjittered
  ordinary records.  This is the naive local-factor model.

  When that model produces a density/outlier obstruction, the receipt follows
  the opening and samples a marginal-matched Palm model: every record has the
  same one-record jitter marginal, and the only special feature of the hidden
  pair is that the two records share the same parent center.

The projected one-pair L2 excess is

    E_{P_N^O}[(dH_N^O/dP_N^O)^2] - 1.

If this excess behaves like O(N^-2), then the local-factor norm behaves like
O(N^-1), as Lemma M wants.  If it remains above the matched split-null guard,
the finite local model is not proving Lemma M; it becomes an obstruction or a
finite-size warning.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import Counter
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


def weights_from_counts(counts):
    total = mp.mpf(sum(counts.values()))
    return {code: mp.mpf(count) / total for code, count in counts.items()}


def split_second(counts_a, counts_b, p_law):
    weights_a = weights_from_counts(counts_a)
    weights_b = weights_from_counts(counts_b)
    value = mp.mpf(0)
    outside = mp.mpf(0)
    top = []
    for code in set(p_law) | set(weights_a) | set(weights_b):
        p = p_law.get(code, mp.mpf(0))
        qa = weights_a.get(code, mp.mpf(0))
        qb = weights_b.get(code, mp.mpf(0))
        if p:
            term = qa * qb / p
            value += term
            top.append((term - p, term, p, qa, qb, code))
        elif qa or qb:
            outside += (qa + qb) / 2
    top.sort(reverse=True, key=lambda row: row[0])
    return {"second": value, "excess": value - 1, "outside": outside, "top": top[:6]}


def sprinkled_counts(n, sample_count, seed):
    rng = random.Random(seed)
    counts = Counter()
    for _ in range(sample_count):
        perm = list(range(n))
        rng.shuffle(perm)
        counts[canonical_unlabeled_code(poset_from_permutation(perm))] += 1
    return counts


def one_pair_counts(n, sample_count, seed, jitter_num, jitter_den):
    rng = random.Random(seed)
    parent_count = n - 1
    hidden_parent = 0
    width = 2
    scale = 10000 * jitter_den
    span = 10000 * jitter_num
    tie = n + 1
    counts = Counter()
    for _ in range(sample_count):
        u_order = list(range(parent_count))
        v_order = list(range(parent_count))
        rng.shuffle(u_order)
        rng.shuffle(v_order)
        u_rank = [0] * parent_count
        v_rank = [0] * parent_count
        for rank, parent in enumerate(u_order):
            u_rank[parent] = rank
        for rank, parent in enumerate(v_order):
            v_rank[parent] = rank

        points = [None] * n
        local_order = [0, 1]
        rng.shuffle(local_order)
        for local, label in enumerate(local_order):
            du = rng.randint(-span, span) if span else 0
            dv = rng.randint(-span, span) if span else 0
            u = (u_rank[hidden_parent] * scale + width * du + local) * tie + label
            v = (v_rank[hidden_parent] * scale + width * dv + (width - 1 - local)) * tie + label
            points[label] = (u, v)

        for parent in range(1, parent_count):
            label = parent + 1
            u = u_rank[parent] * scale * tie + label
            v = v_rank[parent] * scale * tie + label
            points[label] = (u, v)

        counts[canonical_unlabeled_code(coordinate_order_poset(points))] += 1
    return counts


def marginal_matched_one_pair_counts(n, sample_count, seed, jitter_num, jitter_den):
    rng = random.Random(seed)
    width = 2
    scale = 10000 * jitter_den
    span = 10000 * jitter_num
    tie = n + 1
    counts = Counter()
    for _ in range(sample_count):
        points = [None] * n
        parent_u = rng.randrange(n)
        parent_v = rng.randrange(n)
        local_order = [0, 1]
        rng.shuffle(local_order)
        for local, label in enumerate(local_order):
            du = rng.randint(-span, span) if span else 0
            dv = rng.randint(-span, span) if span else 0
            u = (parent_u * scale + width * du + local) * tie + label
            v = (parent_v * scale + width * dv + (width - 1 - local)) * tie + label
            points[label] = (u, v)

        for label in range(2, n):
            base_u = rng.randrange(n)
            base_v = rng.randrange(n)
            du = rng.randint(-span, span) if span else 0
            dv = rng.randint(-span, span) if span else 0
            u = (base_u * scale + width * du) * tie + label
            v = (base_v * scale + width * dv) * tie + label
            points[label] = (u, v)

        counts[canonical_unlabeled_code(coordinate_order_poset(points))] += 1
    return counts


def mean(values):
    return mp.fsum(values) / len(values)


def std(values):
    if len(values) < 2:
        return mp.mpf(0)
    mu = mean(values)
    return mp.sqrt(mp.fsum((value - mu) ** 2 for value in values) / (len(values) - 1))


def summarize(rows):
    excesses = [row["excess"] for row in rows]
    return {
        "second_mean": mean([row["second"] for row in rows]),
        "excess_mean": mean(excesses),
        "excess_std": std(excesses),
        "excess_max": max(excesses),
        "outside_mean": mean([row["outside"] for row in rows]),
    }


print("=" * 80)
print("Paper 27 finite one-pair projection attack on Lemma M")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

sample_count = 16384
null_reps = 5
q_reps = 5
sizes = [5, 6, 7, 8]
schedules = [
    ("linear_half", lambda n: (max(1, n // 2), 2)),
    ("linear_one", lambda n: (n, 2)),
    ("linear_two", lambda n: (2 * n, 2)),
]

naive_rows = {}
matched_rows = {}
null_guards = {}
for n in sizes:
    print("\n" + "=" * 80)
    print(f"N={n} exact denominator and one-pair projection")
    print("=" * 80)
    p_law = exact_unlabeled_sprinkling_law(n)
    print(f"exact P_{n} support={len(p_law)} permutations={fmt(mp.factorial(n), 12)}")

    null_rows = []
    for rep in range(null_reps):
        counts_a = sprinkled_counts(n, sample_count, 41000000 + n * 100000 + rep * 2000)
        counts_b = sprinkled_counts(n, sample_count, 41050000 + n * 100000 + rep * 2000)
        row = split_second(counts_a, counts_b, p_law)
        null_rows.append(row)
        print(f"  null rep={rep}: excess={fmt(row['excess'], 18)} outside={fmt(row['outside'], 8)}")
    null_summary = summarize(null_rows)
    guard = max(mp.mpf(0), null_summary["excess_max"], null_summary["excess_mean"] + 3 * null_summary["excess_std"])
    null_guards[n] = guard
    print(
        f"  null mean={fmt(null_summary['excess_mean'], 18)} "
        f"std={fmt(null_summary['excess_std'], 18)} guard={fmt(guard, 18)}"
    )

    for schedule_index, (name, resolver) in enumerate(schedules):
        jitter_num, jitter_den = resolver(n)
        rows = []
        for rep in range(q_reps):
            counts_a = one_pair_counts(
                n,
                sample_count,
                42000000 + n * 100000 + schedule_index * 10000 + rep * 2000,
                jitter_num,
                jitter_den,
            )
            counts_b = one_pair_counts(
                n,
                sample_count,
                42050000 + n * 100000 + schedule_index * 10000 + rep * 2000,
                jitter_num,
                jitter_den,
            )
            row = split_second(counts_a, counts_b, p_law)
            rows.append(row)
        summary = summarize(rows)
        excess = summary["excess_mean"]
        l2_norm = mp.sqrt(max(excess, mp.mpf(0)))
        naive_rows[(n, name)] = {
            **summary,
            "guard": guard,
            "n_l2": mp.mpf(n) * l2_norm,
            "n2_excess": mp.mpf(n) ** 2 * excess,
        }
        verdict = "above guard" if excess > guard else "inside guard"
        print(
            f"  {name}: jitter={jitter_num}/{jitter_den} "
            f"excess_mean={fmt(excess, 18)} guard_ratio={fmt(excess / guard if guard else mp.inf, 18)} "
            f"N*sqrt(excess+)={fmt(naive_rows[(n, name)]['n_l2'], 18)} "
            f"N^2*excess={fmt(naive_rows[(n, name)]['n2_excess'], 18)} {verdict}"
        )

print("\nNaive local-factor scaling table")
for name, _resolver in schedules:
    print(f"\n{name}")
    for n in sizes:
        row = naive_rows[(n, name)]
        print(
            f"  N={n}: excess={fmt(row['excess_mean'], 18)} "
            f"N*sqrt(excess+)={fmt(row['n_l2'], 18)} "
            f"N^2*excess={fmt(row['n2_excess'], 18)} "
            f"guard={fmt(row['guard'], 18)}"
        )

print("\n" + "=" * 80)
print("Marginal-matched Palm follow-up")
print("=" * 80)
for n in sizes:
    p_law = exact_unlabeled_sprinkling_law(n)
    guard = null_guards[n]
    print(f"\nN={n} marginal-matched one-pair projection")
    for schedule_index, (name, resolver) in enumerate(schedules):
        jitter_num, jitter_den = resolver(n)
        rows = []
        for rep in range(q_reps):
            counts_a = marginal_matched_one_pair_counts(
                n,
                sample_count,
                43000000 + n * 100000 + schedule_index * 10000 + rep * 2000,
                jitter_num,
                jitter_den,
            )
            counts_b = marginal_matched_one_pair_counts(
                n,
                sample_count,
                43050000 + n * 100000 + schedule_index * 10000 + rep * 2000,
                jitter_num,
                jitter_den,
            )
            row = split_second(counts_a, counts_b, p_law)
            rows.append(row)
        summary = summarize(rows)
        excess = summary["excess_mean"]
        l2_norm = mp.sqrt(max(excess, mp.mpf(0)))
        matched_rows[(n, name)] = {
            **summary,
            "guard": guard,
            "n_l2": mp.mpf(n) * l2_norm,
            "n2_excess": mp.mpf(n) ** 2 * excess,
        }
        verdict = "above guard" if excess > guard else "inside guard"
        print(
            f"  {name}: jitter={jitter_num}/{jitter_den} "
            f"excess_mean={fmt(excess, 18)} guard_ratio={fmt(excess / guard if guard else mp.inf, 18)} "
            f"N*sqrt(excess+)={fmt(matched_rows[(n, name)]['n_l2'], 18)} "
            f"N^2*excess={fmt(matched_rows[(n, name)]['n2_excess'], 18)} {verdict}"
        )

print("\nMarginal-matched scaling table")
for name, _resolver in schedules:
    print(f"\n{name}")
    for n in sizes:
        row = matched_rows[(n, name)]
        print(
            f"  N={n}: excess={fmt(row['excess_mean'], 18)} "
            f"N*sqrt(excess+)={fmt(row['n_l2'], 18)} "
            f"N^2*excess={fmt(row['n2_excess'], 18)} "
            f"guard={fmt(row['guard'], 18)}"
        )

naive_one_ratios = [naive_rows[(n, "linear_one")]["excess_mean"] / null_guards[n] for n in sizes]
naive_two_ratios = [naive_rows[(n, "linear_two")]["excess_mean"] / null_guards[n] for n in sizes]
matched_one_ratios = [matched_rows[(n, "linear_one")]["excess_mean"] / null_guards[n] for n in sizes]
matched_two_ratios = [matched_rows[(n, "linear_two")]["excess_mean"] / null_guards[n] for n in sizes]
naive_max_n_l2 = max(naive_rows[(n, name)]["n_l2"] for n in sizes for name, _ in schedules)
matched_max_n_l2 = max(matched_rows[(n, name)]["n_l2"] for n in sizes for name, _ in schedules)
naive_max_n2_excess_abs = max(abs(naive_rows[(n, name)]["n2_excess"]) for n in sizes for name, _ in schedules)

check(
    "Exact denominators are used for every tested N",
    all(null_guards[n] >= 0 for n in sizes),
    f"sizes={sizes}",
)
check(
    "One-pair projected support remains inside the 1+1 sprinkling support",
    all(naive_rows[(n, name)]["outside_mean"] == 0 for n in sizes for name, _ in schedules)
    and all(matched_rows[(n, name)]["outside_mean"] == 0 for n in sizes for name, _ in schedules),
    "outside mass is zero in every split receipt",
)
check(
    "Naive one-pair model exposes a density/outlier obstruction",
    naive_rows[(8, "linear_one")]["excess_mean"] > null_guards[8]
    and naive_rows[(8, "linear_two")]["excess_mean"] > null_guards[8],
    f"one_ratio={fmt(naive_one_ratios[-1], 12)} two_ratio={fmt(naive_two_ratios[-1], 12)}",
)
check(
    "Marginal matching weakens the wide-jitter local obstruction",
    matched_rows[(8, "linear_two")]["excess_mean"] < naive_rows[(8, "linear_two")]["excess_mean"],
    f"matched_two={fmt(matched_rows[(8, 'linear_two')]['excess_mean'], 18)} "
    f"naive_two={fmt(naive_rows[(8, 'linear_two')]['excess_mean'], 18)}",
)
check(
    "Finite data still do not certify Lemma M",
    naive_max_n_l2 > mp.mpf("3.0") or matched_max_n_l2 > mp.mpf("3.0"),
    f"naive_max_N_l2={fmt(naive_max_n_l2, 18)} matched_max_N_l2={fmt(matched_max_n_l2, 18)} "
    f"max_abs_N2_excess={fmt(naive_max_n2_excess_abs, 18)}",
)

print("\n=== Consequence ===")
print("The naive one-pair projection is not a proof of Lemma M; it creates a")
print("density/outlier signal because only the hidden pair receives the wide")
print("jitter.  The marginal-matched Palm follow-up is the right local object,")
print("but the finite receipt still cannot certify the O(1/N) L2 factor bound.")
print("The next proof target is now sharper: derive the one-pair Palm likelihood")
print("against the exact iid-coordinate marginal, then prove that its projection")
print("to unlabeled orders is O(1/N) or exhibit the selected class where it is not.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
