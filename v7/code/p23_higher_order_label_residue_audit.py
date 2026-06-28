#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: higher-order hidden-label residue audit.

The observable-label receipt found that linear-window hidden labels are not
recoverable by simple order-visible pair features.  This receipt follows the
next hostile opening: maybe pair information washes out, but same-hidden-label
triples still leave an order-visible residue.

It compares all-same-label triples against all-distinct-label triples using
only order-visible triple features, and calibrates against a sprinkling with
random pseudo-labels of the same width.  It intentionally uses single-feature
AUCs rather than a trained black-box classifier, so a positive result is an
interpretable residue and a negative result is only a finite projection failure.

All asserted non-integer arithmetic uses mpmath with dps=140.  Poset statistics
are integer bitset counts; no float64 arithmetic is used for asserted values.
"""

import itertools
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
        self.future = list(future)
        self.N = len(self.future)
        self.past = [0] * self.N
        for x, mask in enumerate(self.future):
            for y in iter_bits(mask):
                self.past[y] |= 1 << x

    def comparable(self, x, y):
        return bool((self.future[x] >> y) & 1) or bool((self.future[y] >> x) & 1)

    def interval_size_unordered(self, x, y):
        if (self.future[x] >> y) & 1:
            return (self.future[x] & self.past[y]).bit_count()
        if (self.future[y] >> x) & 1:
            return (self.future[y] & self.past[x]).bit_count()
        return 0

    def relation_count_on_vertices(self, vertices):
        count = 0
        vertex_mask = 0
        for vertex in vertices:
            vertex_mask |= 1 << vertex
        for x in vertices:
            count += (self.future[x] & vertex_mask).bit_count()
        return count


def sprinkled2_poset(N, seed):
    rng = random.Random(seed)
    perm = list(range(N))
    rng.shuffle(perm)
    future = [0] * N
    for i in range(N):
        vi = perm[i]
        mask = 0
        for j in range(i + 1, N):
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


def clustered_jittered_fiber_poset(base_N, width, seed, jitter_num, jitter_den):
    rng = random.Random(seed)
    perm = list(range(base_N))
    rng.shuffle(perm)
    scale = 10000 * jitter_den
    span = 10000 * jitter_num
    points = []
    labels = []
    for i, vi in enumerate(perm):
        for local in range(width):
            du = rng.randint(-span, span) if span else 0
            dv = rng.randint(-span, span) if span else 0
            u = i * scale + width * du + local
            v = vi * scale + width * dv + (width - 1 - local)
            points.append((u, v))
            labels.append(i)
    return coordinate_order_poset(points), labels


def pseudo_labels(N, width, seed):
    rng = random.Random(seed)
    labels = []
    for label in range(N // width):
        labels.extend([label] * width)
    while len(labels) < N:
        labels.append(len(labels))
    rng.shuffle(labels)
    return labels


def jaccard(mask_a, mask_b):
    union = (mask_a | mask_b).bit_count()
    if union == 0:
        return mp.mpf(1)
    return mp.mpf((mask_a & mask_b).bit_count()) / union


def multi_jaccard(masks):
    if not masks:
        return mp.mpf(1)
    intersection = masks[0]
    union = 0
    for mask in masks:
        intersection &= mask
        union |= mask
    union_count = union.bit_count()
    if union_count == 0:
        return mp.mpf(1)
    return mp.mpf(intersection.bit_count()) / union_count


def external_delta(poset, x, y):
    clear_x = ~(1 << x)
    clear_y = ~(1 << y)
    diff = ((poset.past[x] & clear_y) ^ (poset.past[y] & clear_x)).bit_count()
    diff += ((poset.future[x] & clear_y) ^ (poset.future[y] & clear_x)).bit_count()
    return diff


def longest_chain_three(poset, vertices):
    rel = [[False] * 3 for _ in range(3)]
    for i, x in enumerate(vertices):
        for j, y in enumerate(vertices):
            if i != j and ((poset.future[x] >> y) & 1):
                rel[i][j] = True
    best = 1
    for i in range(3):
        for j in range(3):
            if rel[i][j]:
                best = max(best, 2)
                for k in range(3):
                    if rel[j][k]:
                        best = max(best, 3)
    return best


FEATURE_NAMES = [
    "relation_count",
    "height",
    "delta_mean",
    "delta_min",
    "delta_max",
    "delta_var",
    "past_pair_jaccard_mean",
    "future_pair_jaccard_mean",
    "past_triple_jaccard",
    "future_triple_jaccard",
    "interval_mean",
    "interval_max",
]


def triple_features(poset, triple):
    vertices = list(triple)
    pairs = list(itertools.combinations(vertices, 2))
    denom = max(1, 2 * (poset.N - 2))
    deltas = [mp.mpf(external_delta(poset, x, y)) / denom for x, y in pairs]
    delta_mean = sum(deltas) / len(deltas)
    delta_var = sum((value - delta_mean) ** 2 for value in deltas) / len(deltas)
    past_pair_j = []
    future_pair_j = []
    intervals = []
    for x, y in pairs:
        past_pair_j.append(jaccard(poset.past[x] & ~(1 << y), poset.past[y] & ~(1 << x)))
        future_pair_j.append(jaccard(poset.future[x] & ~(1 << y), poset.future[y] & ~(1 << x)))
        intervals.append(mp.mpf(poset.interval_size_unordered(x, y)) / poset.N)
    triple_mask = 0
    for x in vertices:
        triple_mask |= 1 << x
    past_masks = [poset.past[x] & ~triple_mask for x in vertices]
    future_masks = [poset.future[x] & ~triple_mask for x in vertices]
    return [
        mp.mpf(poset.relation_count_on_vertices(vertices)) / 3,
        mp.mpf(longest_chain_three(poset, vertices)) / 3,
        delta_mean,
        min(deltas),
        max(deltas),
        delta_var,
        sum(past_pair_j) / len(past_pair_j),
        sum(future_pair_j) / len(future_pair_j),
        multi_jaccard(past_masks),
        multi_jaccard(future_masks),
        sum(intervals) / len(intervals),
        max(intervals),
    ]


def sample_balanced_triples(labels, seed, positive_count=256):
    rng = random.Random(seed)
    by_label = {}
    for index, label in enumerate(labels):
        by_label.setdefault(label, []).append(index)
    positives_all = []
    for members in by_label.values():
        positives_all.extend(itertools.combinations(members, 3))
    positives = (
        rng.sample(positives_all, positive_count)
        if len(positives_all) > positive_count
        else positives_all
    )
    negatives = []
    attempts = 0
    while len(negatives) < len(positives) and attempts < 100 * max(1, len(positives)):
        triple = tuple(sorted(rng.sample(range(len(labels)), 3)))
        attempts += 1
        if len({labels[x] for x in triple}) == 3:
            negatives.append(triple)
    return positives, negatives


def auc_low_positive(positive_values, negative_values):
    total = mp.mpf(len(positive_values) * len(negative_values))
    if total == 0:
        return mp.mpf("0.5")
    wins = mp.mpf(0)
    for pos in positive_values:
        for neg in negative_values:
            if pos < neg:
                wins += 1
            elif pos == neg:
                wins += mp.mpf("0.5")
    return wins / total


def triple_label_observability(poset, labels, seed):
    positives, negatives = sample_balanced_triples(labels, seed)
    pos_rows = [triple_features(poset, triple) for triple in positives]
    neg_rows = [triple_features(poset, triple) for triple in negatives]
    feature_results = []
    for feature_index, name in enumerate(FEATURE_NAMES):
        pos_values = [row[feature_index] for row in pos_rows]
        neg_values = [row[feature_index] for row in neg_rows]
        auc = auc_low_positive(pos_values, neg_values)
        separability = max(auc, 1 - auc)
        orientation = "low" if auc >= mp.mpf("0.5") else "high"
        feature_results.append((separability, auc, orientation, name))
    feature_results.sort(reverse=True, key=lambda row: row[0])
    return {
        "best_sep": feature_results[0][0],
        "best_name": feature_results[0][3],
        "positive_count": len(positives),
        "negative_count": len(negatives),
        "top": feature_results[:4],
    }


def mean(values):
    return sum(values) / len(values)


def summarize(rows):
    values = [row["best_sep"] for row in rows]
    return {
        "best_mean": mean(values),
        "best_max": max(values),
        "best_min": min(values),
        "top_names": [row["best_name"] for row in rows],
    }


print("=" * 80)
print("Collapsed P23 higher-order hidden-label residue audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 768
width = 4
base = N // width
rep_count = 6

print(f"\n(1) Pseudo-label triple null at N={N}, width={width}")
null_rows = []
for rep in range(rep_count):
    poset = sprinkled2_poset(N, 1810000 + rep)
    labels = pseudo_labels(N, width, 1820000 + rep)
    row = triple_label_observability(poset, labels, 1830000 + rep)
    null_rows.append(row)
    print(
        f"null rep={rep} best={row['best_name']} sep={fmt(row['best_sep'], 16)} "
        f"triples={row['positive_count']}"
    )
null_summary = summarize(null_rows)
null_guard = null_summary["best_max"] + mp.mpf("0.05")
print(
    f"null best_mean={fmt(null_summary['best_mean'], 18)} "
    f"best_max={fmt(null_summary['best_max'], 18)} guard={fmt(null_guard, 18)}"
)

print("\n(2) Clustered schedules")
schedules = [
    ("locked", 0, 1),
    ("fixed_four", 4, 1),
    ("sqrt", int(mp.sqrt(N)), 1),
    ("linear_half", N // 2, width),
    ("linear_one", N, width),
    ("linear_two", 2 * N, width),
]
schedule_results = {}
for name, jitter_num, jitter_den in schedules:
    rows = []
    print(f"\n{name}: jitter={jitter_num}/{jitter_den}")
    for rep in range(rep_count):
        poset, labels = clustered_jittered_fiber_poset(
            base,
            width,
            1840000 + 10000 * rep + 101 * jitter_num + jitter_den,
            jitter_num,
            jitter_den,
        )
        row = triple_label_observability(
            poset, labels, 1850000 + 10000 * rep + 101 * jitter_num + jitter_den
        )
        rows.append(row)
        top = ", ".join(
            f"{feature}:{fmt(sep, 8)}:{orientation}"
            for sep, _auc, orientation, feature in row["top"]
        )
        print(
            f"rep={rep} best={row['best_name']} sep={fmt(row['best_sep'], 16)} "
            f"top=[{top}]"
        )
    summary = summarize(rows)
    schedule_results[name] = {"rows": rows, "summary": summary}
    print(
        f"{name} mean_best={fmt(summary['best_mean'], 18)} "
        f"max={fmt(summary['best_max'], 18)} min={fmt(summary['best_min'], 18)}"
    )

visible = {
    name: result
    for name, result in schedule_results.items()
    if result["summary"]["best_mean"] > null_guard
}
washed = {
    name: result
    for name, result in schedule_results.items()
    if result["summary"]["best_mean"] <= null_guard
}
linear_names = {"linear_half", "linear_one", "linear_two"}
linear_visible = sorted(name for name in visible if name in linear_names)
linear_washed = sorted(name for name in washed if name in linear_names)

check(
    "Pseudo-label triple null has near-random order-only separability",
    null_summary["best_max"] < mp.mpf("0.7"),
    f"best_mean={fmt(null_summary['best_mean'], 16)}, best_max={fmt(null_summary['best_max'], 16)}",
)
check(
    "Locked or fixed-jitter same-label triples leave higher-order residue",
    schedule_results["locked"]["summary"]["best_mean"] > mp.mpf("0.9")
    and schedule_results["fixed_four"]["summary"]["best_mean"] > null_guard,
    f"locked={fmt(schedule_results['locked']['summary']['best_mean'], 16)}, "
    f"fixed_four={fmt(schedule_results['fixed_four']['summary']['best_mean'], 16)}, guard={fmt(null_guard, 16)}",
)
check(
    "Linear-window schedules remain pseudo-label-like in this triple projection",
    len(linear_washed) == len(linear_names),
    ", ".join(f"{name}={fmt(schedule_results[name]['summary']['best_mean'], 12)}" for name in sorted(linear_names)),
)
check(
    "The triple audit does not close the higher-order gap",
    len(linear_visible) == 0 and bool(washed),
    f"linear_visible={','.join(linear_visible) or 'none'}; washed={','.join(sorted(washed))}",
)
check(
    "The residue boundary remains between square-root and linear mixing in this projection",
    schedule_results["sqrt"]["summary"]["best_mean"] > null_guard
    and all(schedule_results[name]["summary"]["best_mean"] <= null_guard for name in linear_names),
    f"sqrt={fmt(schedule_results['sqrt']['summary']['best_mean'], 16)}, guard={fmt(null_guard, 16)}",
)

print("\n(3) Consequence")
print("The pair-invisible linear schedules do not become visible again under this")
print("finite triple-feature projection.  This does not prove full washout.")
print("It says the next residue, if present, must be a richer rooted, interval,")
print("mesoscopic, or process-level bracket object rather than a simple")
print("same-label pair/triple classifier.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
