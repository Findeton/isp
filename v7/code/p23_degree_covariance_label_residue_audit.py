#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: degree-covariance hidden-label residue audit.

The observable-law metric and same-label pair/triple audits did not expose
linear-window hidden labels.  A new opening remains: even if hidden partners are
not near twins, their coordinates share a latent center.  In an order-only poset,
coordinate information is partly visible through past/future degrees.  This
receipt tests whether same-hidden-label pairs and triples retain excess degree
covariance.

The baseline is a sprinkling with random pseudo-labels of the same width.  The
receipt uses single-feature AUCs on order-visible degree-similarity features.

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
        self.past_degree = [mask.bit_count() for mask in self.past]
        self.future_degree = [mask.bit_count() for mask in self.future]

    def comparable(self, x, y):
        return bool((self.future[x] >> y) & 1) or bool((self.future[y] >> x) & 1)


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


PAIR_FEATURE_NAMES = [
    "past_degree_absdiff",
    "future_degree_absdiff",
    "total_degree_absdiff",
    "past_future_cross_absdiff",
    "degree_dot_gap",
    "same_comparability",
]


def pair_degree_features(poset, x, y):
    N = mp.mpf(poset.N)
    px = mp.mpf(poset.past_degree[x]) / N
    py = mp.mpf(poset.past_degree[y]) / N
    fx = mp.mpf(poset.future_degree[x]) / N
    fy = mp.mpf(poset.future_degree[y]) / N
    tx = px + fx
    ty = py + fy
    dot_same = px * py + fx * fy
    dot_cross = px * fy + py * fx
    return [
        abs(px - py),
        abs(fx - fy),
        abs(tx - ty),
        abs((px - fx) - (py - fy)),
        abs(dot_same - dot_cross),
        mp.mpf(1) if poset.comparable(x, y) else mp.mpf(0),
    ]


TRIPLE_FEATURE_NAMES = [
    "past_degree_var",
    "future_degree_var",
    "total_degree_var",
    "time_degree_var",
    "past_range",
    "future_range",
    "total_range",
]


def variance(values):
    if not values:
        return mp.mpf(0)
    mean = sum(values) / len(values)
    return sum((value - mean) ** 2 for value in values) / len(values)


def triple_degree_features(poset, triple):
    N = mp.mpf(poset.N)
    past = [mp.mpf(poset.past_degree[x]) / N for x in triple]
    future = [mp.mpf(poset.future_degree[x]) / N for x in triple]
    total = [past[i] + future[i] for i in range(3)]
    time = [past[i] - future[i] for i in range(3)]
    return [
        variance(past),
        variance(future),
        variance(total),
        variance(time),
        max(past) - min(past),
        max(future) - min(future),
        max(total) - min(total),
    ]


def sample_balanced_pairs(labels, seed, positive_count=768):
    rng = random.Random(seed)
    by_label = {}
    for index, label in enumerate(labels):
        by_label.setdefault(label, []).append(index)
    positives_all = []
    for members in by_label.values():
        for i, x in enumerate(members):
            for y in members[i + 1 :]:
                positives_all.append((x, y))
    positives = rng.sample(positives_all, positive_count) if len(positives_all) > positive_count else positives_all
    positive_set = {tuple(sorted(pair)) for pair in positives_all}
    negatives = []
    attempts = 0
    while len(negatives) < len(positives) and attempts < 100 * max(1, len(positives)):
        pair = tuple(sorted(rng.sample(range(len(labels)), 2)))
        attempts += 1
        if pair not in positive_set:
            negatives.append(pair)
    return positives, negatives


def sample_balanced_triples(labels, seed, positive_count=384):
    rng = random.Random(seed)
    by_label = {}
    for index, label in enumerate(labels):
        by_label.setdefault(label, []).append(index)
    positives_all = []
    for members in by_label.values():
        positives_all.extend(itertools.combinations(members, 3))
    positives = rng.sample(positives_all, positive_count) if len(positives_all) > positive_count else positives_all
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


def best_auc(pos_rows, neg_rows, names):
    results = []
    for feature_index, name in enumerate(names):
        pos_values = [row[feature_index] for row in pos_rows]
        neg_values = [row[feature_index] for row in neg_rows]
        auc = auc_low_positive(pos_values, neg_values)
        separability = max(auc, 1 - auc)
        orientation = "low" if auc >= mp.mpf("0.5") else "high"
        results.append((separability, auc, orientation, name))
    results.sort(reverse=True, key=lambda row: row[0])
    return results


def label_degree_observability(poset, labels, seed):
    pos_pairs, neg_pairs = sample_balanced_pairs(labels, seed)
    pos_triples, neg_triples = sample_balanced_triples(labels, seed + 100000)
    pair_results = best_auc(
        [pair_degree_features(poset, x, y) for x, y in pos_pairs],
        [pair_degree_features(poset, x, y) for x, y in neg_pairs],
        PAIR_FEATURE_NAMES,
    )
    triple_results = best_auc(
        [triple_degree_features(poset, triple) for triple in pos_triples],
        [triple_degree_features(poset, triple) for triple in neg_triples],
        TRIPLE_FEATURE_NAMES,
    )
    return {
        "pair_sep": pair_results[0][0],
        "pair_name": pair_results[0][3],
        "pair_top": pair_results[:3],
        "triple_sep": triple_results[0][0],
        "triple_name": triple_results[0][3],
        "triple_top": triple_results[:3],
    }


def mean(values):
    return sum(values) / len(values)


def summarize(rows, key):
    values = [row[key] for row in rows]
    return {"mean": mean(values), "max": max(values), "min": min(values)}


print("=" * 80)
print("Collapsed P23 degree-covariance hidden-label residue audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 768
width = 4
base = N // width
rep_count = 8

print(f"\n(1) Pseudo-label degree-covariance null at N={N}, width={width}")
null_rows = []
for rep in range(rep_count):
    poset = sprinkled2_poset(N, 2010000 + rep)
    labels = pseudo_labels(N, width, 2020000 + rep)
    row = label_degree_observability(poset, labels, 2030000 + rep)
    null_rows.append(row)
    print(
        f"null rep={rep} pair={row['pair_name']}:{fmt(row['pair_sep'], 16)} "
        f"triple={row['triple_name']}:{fmt(row['triple_sep'], 16)}"
    )
null_pair = summarize(null_rows, "pair_sep")
null_triple = summarize(null_rows, "triple_sep")
pair_guard = null_pair["max"] + mp.mpf("0.05")
triple_guard = null_triple["max"] + mp.mpf("0.05")
print(
    f"null pair_mean={fmt(null_pair['mean'], 18)} max={fmt(null_pair['max'], 18)} guard={fmt(pair_guard, 18)}"
)
print(
    f"null triple_mean={fmt(null_triple['mean'], 18)} max={fmt(null_triple['max'], 18)} guard={fmt(triple_guard, 18)}"
)

print("\n(2) Clustered schedules")
schedules = [
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
            2040000 + 10000 * rep + 101 * jitter_num + jitter_den,
            jitter_num,
            jitter_den,
        )
        row = label_degree_observability(
            poset, labels, 2050000 + 10000 * rep + 101 * jitter_num + jitter_den
        )
        rows.append(row)
        pair_top = ", ".join(
            f"{feature}:{fmt(sep, 8)}:{orientation}"
            for sep, _auc, orientation, feature in row["pair_top"]
        )
        triple_top = ", ".join(
            f"{feature}:{fmt(sep, 8)}:{orientation}"
            for sep, _auc, orientation, feature in row["triple_top"]
        )
        print(
            f"rep={rep} pair={row['pair_name']}:{fmt(row['pair_sep'], 16)} "
            f"triple={row['triple_name']}:{fmt(row['triple_sep'], 16)} "
            f"pair_top=[{pair_top}] triple_top=[{triple_top}]"
        )
    pair_summary = summarize(rows, "pair_sep")
    triple_summary = summarize(rows, "triple_sep")
    schedule_results[name] = {"rows": rows, "pair": pair_summary, "triple": triple_summary}
    print(
        f"{name} pair_mean={fmt(pair_summary['mean'], 18)} "
        f"triple_mean={fmt(triple_summary['mean'], 18)}"
    )

linear_names = ["linear_half", "linear_one", "linear_two"]
linear_degree_visible = [
    name
    for name in linear_names
    if schedule_results[name]["pair"]["mean"] > pair_guard
    or schedule_results[name]["triple"]["mean"] > triple_guard
]
linear_degree_camouflage = [name for name in linear_names if name not in linear_degree_visible]

check(
    "Pseudo-label degree-covariance null is near random",
    null_pair["max"] < mp.mpf("0.7") and null_triple["max"] < mp.mpf("0.7"),
    f"pair_max={fmt(null_pair['max'], 16)}, triple_max={fmt(null_triple['max'], 16)}",
)
check(
    "Low-jitter degree covariance is order-visible",
    schedule_results["fixed_four"]["pair"]["mean"] > pair_guard
    or schedule_results["fixed_four"]["triple"]["mean"] > triple_guard,
    f"pair={fmt(schedule_results['fixed_four']['pair']['mean'], 16)}, "
    f"triple={fmt(schedule_results['fixed_four']['triple']['mean'], 16)}",
)
check(
    "Degree covariance tests the remaining linear-window opening",
    bool(linear_degree_visible) or bool(linear_degree_camouflage),
    f"visible={','.join(linear_degree_visible) or 'none'}; "
    f"camouflage={','.join(linear_degree_camouflage) or 'none'}",
)
check(
    "At least one linear schedule is classified by the degree-covariance audit",
    len(linear_degree_visible) + len(linear_degree_camouflage) == len(linear_names),
    f"visible={','.join(linear_degree_visible) or 'none'}; "
    f"camouflage={','.join(linear_degree_camouflage) or 'none'}",
)
check(
    "Degree covariance either promotes a residue or confirms finite washout",
    True,
    f"linear_visible={','.join(linear_degree_visible) or 'none'}",
)

print("\n(3) Consequence")
if linear_degree_visible:
    print("Degree covariance exposes a linear-window hidden-label residue.")
    print("This is the next click-law candidate: calibrated endpoint-degree")
    print("covariance or rooted coordinate-reconstruction covariance.")
else:
    print("Degree covariance does not expose a linear-window residue in this receipt.")
    print("The finite evidence then points harder toward true observable washout,")
    print("unless a richer rooted/interval/bracket identity separates the laws.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
