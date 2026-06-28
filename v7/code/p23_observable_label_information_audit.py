#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: observable hidden-label information audit.

The previous campaign narrowed the critical window to a philosophical but
mathematical point: a hidden cluster matters only insofar as its hidden label is
recoverable from the observable record order.  This receipt tests that idea
directly on clustered-coordinate generators.

It does not train a black-box classifier.  For balanced same-hidden-label and
different-label pair samples, it computes order-only pair features and asks how
well a single feature can separate the two classes.  The baseline is a sprinkling
with random pseudo-labels of the same width.  If the clustered labels are no more
separable than pseudo-labels, then the hidden implementation label has washed out
in this finite projection.  If they separate strongly, the hidden cluster leaves
an order-visible residue.

All asserted non-integer arithmetic uses mpmath with dps=140.  Poset statistics
are integer bitset counts; no float64 arithmetic is used for asserted values.
"""

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


def external_delta(poset, x, y):
    clear_x = ~(1 << x)
    clear_y = ~(1 << y)
    diff = ((poset.past[x] & clear_y) ^ (poset.past[y] & clear_x)).bit_count()
    diff += ((poset.future[x] & clear_y) ^ (poset.future[y] & clear_x)).bit_count()
    return diff


def jaccard(mask_a, mask_b):
    union = (mask_a | mask_b).bit_count()
    if union == 0:
        return mp.mpf(1)
    return mp.mpf((mask_a & mask_b).bit_count()) / union


FEATURE_NAMES = [
    "external_delta",
    "past_jaccard",
    "future_jaccard",
    "causal_agreement",
    "comparable",
    "interval_size",
]


def pair_features(poset, x, y):
    delta = external_delta(poset, x, y)
    denom = max(1, 2 * (poset.N - 2))
    return [
        mp.mpf(delta) / denom,
        jaccard(poset.past[x] & ~(1 << y), poset.past[y] & ~(1 << x)),
        jaccard(poset.future[x] & ~(1 << y), poset.future[y] & ~(1 << x)),
        mp.mpf(1) - mp.mpf(delta) / denom,
        mp.mpf(1) if poset.comparable(x, y) else mp.mpf(0),
        mp.mpf(poset.interval_size_unordered(x, y)) / poset.N,
    ]


def sample_balanced_pairs(labels, seed, positive_count=512):
    rng = random.Random(seed)
    by_label = {}
    for index, label in enumerate(labels):
        by_label.setdefault(label, []).append(index)
    positives_all = []
    for members in by_label.values():
        for i, x in enumerate(members):
            for y in members[i + 1 :]:
                positives_all.append((x, y))
    positives = (
        rng.sample(positives_all, positive_count)
        if len(positives_all) > positive_count
        else positives_all
    )
    positive_set = {tuple(sorted(pair)) for pair in positives_all}
    negatives = []
    attempts = 0
    while len(negatives) < len(positives) and attempts < 50 * max(1, len(positives)):
        x = rng.randrange(len(labels))
        y = rng.randrange(len(labels))
        attempts += 1
        if x == y:
            continue
        pair = tuple(sorted((x, y)))
        if pair in positive_set:
            continue
        negatives.append(pair)
    return positives, negatives


def auc_low_positive(positive_values, negative_values):
    wins = mp.mpf(0)
    total = mp.mpf(len(positive_values) * len(negative_values))
    if total == 0:
        return mp.mpf("0.5")
    for pos in positive_values:
        for neg in negative_values:
            if pos < neg:
                wins += 1
            elif pos == neg:
                wins += mp.mpf("0.5")
    return wins / total


def label_observability(poset, labels, seed):
    positives, negatives = sample_balanced_pairs(labels, seed)
    pos_rows = [pair_features(poset, x, y) for x, y in positives]
    neg_rows = [pair_features(poset, x, y) for x, y in negatives]
    feature_results = []
    for feature_index, name in enumerate(FEATURE_NAMES):
        pos_values = [row[feature_index] for row in pos_rows]
        neg_values = [row[feature_index] for row in neg_rows]
        auc = auc_low_positive(pos_values, neg_values)
        separability = max(auc, 1 - auc)
        orientation = "low" if auc >= mp.mpf("0.5") else "high"
        feature_results.append((separability, auc, orientation, name))
    feature_results.sort(reverse=True, key=lambda row: row[0])
    best_sep, best_auc, best_orientation, best_name = feature_results[0]
    delta_result = next(row for row in feature_results if row[3] == "external_delta")
    return {
        "best_sep": best_sep,
        "best_auc": best_auc,
        "best_orientation": best_orientation,
        "best_name": best_name,
        "delta_sep": delta_result[0],
        "delta_auc": delta_result[1],
        "positive_count": len(positives),
        "negative_count": len(negatives),
        "top": feature_results[:3],
    }


def mean(values):
    return sum(values) / len(values)


def summarize(rows):
    best = [row["best_sep"] for row in rows]
    delta = [row["delta_sep"] for row in rows]
    return {
        "best_mean": mean(best),
        "best_max": max(best),
        "best_min": min(best),
        "delta_mean": mean(delta),
        "top_names": [row["best_name"] for row in rows],
    }


print("=" * 80)
print("Collapsed P23 observable hidden-label information audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 768
width = 4
base = N // width
rep_count = 10

print(f"\n(1) Pseudo-label null at N={N}, width={width}")
null_rows = []
for rep in range(rep_count):
    poset = sprinkled2_poset(N, 1710000 + rep)
    labels = pseudo_labels(N, width, 1720000 + rep)
    row = label_observability(poset, labels, 1730000 + rep)
    null_rows.append(row)
    print(
        f"null rep={rep} best={row['best_name']} sep={fmt(row['best_sep'], 16)} "
        f"delta_sep={fmt(row['delta_sep'], 16)} pairs={row['positive_count']}"
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
            base, width, 1740000 + 10000 * rep + 101 * jitter_num + jitter_den, jitter_num, jitter_den
        )
        row = label_observability(poset, labels, 1750000 + 10000 * rep + 101 * jitter_num + jitter_den)
        rows.append(row)
        top = ", ".join(
            f"{feature}:{fmt(sep, 8)}:{orientation}"
            for sep, _auc, orientation, feature in row["top"]
        )
        print(
            f"rep={rep} best={row['best_name']} sep={fmt(row['best_sep'], 16)} "
            f"delta_sep={fmt(row['delta_sep'], 16)} top=[{top}]"
        )
    summary = summarize(rows)
    schedule_results[name] = {"rows": rows, "summary": summary}
    print(
        f"{name} mean_best={fmt(summary['best_mean'], 18)} "
        f"max={fmt(summary['best_max'], 18)} min={fmt(summary['best_min'], 18)} "
        f"delta_mean={fmt(summary['delta_mean'], 18)}"
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

check(
    "Pseudo-label null has near-random order-only separability",
    null_summary["best_max"] < mp.mpf("0.7"),
    f"best_mean={fmt(null_summary['best_mean'], 16)}, best_max={fmt(null_summary['best_max'], 16)}",
)
check(
    "Locked or small-jitter hidden clusters leave order-visible label residue",
    schedule_results["locked"]["summary"]["best_mean"] > mp.mpf("0.9")
    and schedule_results["fixed_four"]["summary"]["best_mean"] > null_guard,
    f"locked={fmt(schedule_results['locked']['summary']['best_mean'], 16)}, "
    f"fixed_four={fmt(schedule_results['fixed_four']['summary']['best_mean'], 16)}, guard={fmt(null_guard, 16)}",
)
check(
    "At least one linear-window schedule washes hidden labels to pseudo-label separability",
    any(name.startswith("linear") for name in washed),
    ", ".join(f"{name}={fmt(result['summary']['best_mean'], 12)}" for name, result in washed.items()),
)
check(
    "At least one non-locked schedule remains order-visible in this finite projection",
    any(name != "locked" for name in visible),
    ", ".join(f"{name}={fmt(result['summary']['best_mean'], 12)}" for name, result in visible.items()),
)
check(
    "The observable-label audit splits hidden implementation from record-law residue",
    bool(visible) and bool(washed),
    f"visible={','.join(sorted(visible))}; washed={','.join(sorted(washed))}",
)

print("\n(3) Consequence")
print("A hidden cluster is not automatically a record-law defect.  In low-jitter")
print("regimes, same-hidden-label pairs are recoverable from order-only features,")
print("so the hidden construction leaves a residue.  In washed regimes, the hidden")
print("label behaves like an independent pseudo-label in this finite projection.")
print("The click-law target should therefore penalize observable residue, not")
print("unobservable implementation history.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
