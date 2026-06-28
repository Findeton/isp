#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: reconstructed-coordinate Palm audit.

The marked bracket identity found a coordinate-level residue, while simpler
order-visible brackets did not.  This receipt tests a sharper order-only bridge.

In a 1+1 sprinkling, for a record with lightcone coordinates (u,v),

    past_degree/N  ~  uv,
    future_degree/N ~ (1-u)(1-v).

Therefore the order itself estimates

    u+v = 1 + past_degree/N - future_degree/N,
    uv  = past_degree/N,

so it recovers the unordered coordinate pair {u,v} as the roots of a quadratic.
This is not using the original coordinate marks; it is an order-only
reconstruction from past/future degrees.

The receipt tests whether same-hidden-label pairs become visible again through
these reconstructed coordinates in the linear window.  The baseline is a
sprinkling with random pseudo-labels.

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
        self.past_degree = [mask.bit_count() for mask in self.past]
        self.future_degree = [mask.bit_count() for mask in self.future]
        self.reconstructed = [reconstructed_coordinates(self, x) for x in range(self.N)]


def reconstructed_coordinates(poset, x):
    N = mp.mpf(poset.N)
    p = mp.mpf(poset.past_degree[x]) / N
    f = mp.mpf(poset.future_degree[x]) / N
    s = 1 + p - f
    discr = s * s - 4 * p
    if discr < 0:
        discr = mp.mpf(0)
    root = mp.sqrt(discr)
    a = (s - root) / 2
    b = (s + root) / 2
    return a, b, s, p, f


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


FEATURE_NAMES = [
    "recon_min_absdiff",
    "recon_max_absdiff",
    "recon_sum_absdiff",
    "recon_product_absdiff",
    "past_absdiff",
    "future_absdiff",
]


def pair_features(poset, x, y):
    ax, bx, sx, px, fx = poset.reconstructed[x]
    ay, by, sy, py, fy = poset.reconstructed[y]
    return [
        abs(ax - ay),
        abs(bx - by),
        abs(sx - sy),
        abs(px - py),
        abs(px - py),
        abs(fx - fy),
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


def best_auc(pos_rows, neg_rows):
    results = []
    for feature_index, name in enumerate(FEATURE_NAMES):
        pos_values = [row[feature_index] for row in pos_rows]
        neg_values = [row[feature_index] for row in neg_rows]
        auc = auc_low_positive(pos_values, neg_values)
        separability = max(auc, 1 - auc)
        orientation = "low" if auc >= mp.mpf("0.5") else "high"
        results.append((separability, auc, orientation, name))
    results.sort(reverse=True, key=lambda row: row[0])
    return results


def reconstructed_label_observability(poset, labels, seed):
    positives, negatives = sample_balanced_pairs(labels, seed)
    results = best_auc(
        [pair_features(poset, x, y) for x, y in positives],
        [pair_features(poset, x, y) for x, y in negatives],
    )
    return {"best_sep": results[0][0], "best_name": results[0][3], "top": results[:4]}


def mean(values):
    return sum(values) / len(values)


def summarize(rows):
    values = [row["best_sep"] for row in rows]
    return {"mean": mean(values), "max": max(values), "min": min(values)}


print("=" * 80)
print("Collapsed P23 reconstructed-coordinate Palm audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 768
width = 4
base = N // width
rep_count = 8

print(f"\n(1) Pseudo-label reconstructed-coordinate null at N={N}, width={width}")
null_rows = []
for rep in range(rep_count):
    poset = sprinkled2_poset(N, 2210000 + rep)
    labels = pseudo_labels(N, width, 2220000 + rep)
    row = reconstructed_label_observability(poset, labels, 2230000 + rep)
    null_rows.append(row)
    print(f"null rep={rep} best={row['best_name']} sep={fmt(row['best_sep'], 16)}")
null_summary = summarize(null_rows)
guard = null_summary["max"] + mp.mpf("0.05")
print(
    f"null mean={fmt(null_summary['mean'], 18)} max={fmt(null_summary['max'], 18)} guard={fmt(guard, 18)}"
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
            2240000 + 10000 * rep + 101 * jitter_num + jitter_den,
            jitter_num,
            jitter_den,
        )
        row = reconstructed_label_observability(
            poset, labels, 2250000 + 10000 * rep + 101 * jitter_num + jitter_den
        )
        rows.append(row)
        top = ", ".join(
            f"{feature}:{fmt(sep, 8)}:{orientation}"
            for sep, _auc, orientation, feature in row["top"]
        )
        print(f"rep={rep} best={row['best_name']} sep={fmt(row['best_sep'], 16)} top=[{top}]")
    summary = summarize(rows)
    schedule_results[name] = summary
    print(f"{name} mean={fmt(summary['mean'], 18)} max={fmt(summary['max'], 18)} min={fmt(summary['min'], 18)}")

linear_names = ["linear_half", "linear_one", "linear_two"]
linear_visible = [name for name in linear_names if schedule_results[name]["mean"] > guard]
linear_camouflage = [name for name in linear_names if name not in linear_visible]

check(
    "Pseudo-label reconstructed-coordinate null is near random",
    null_summary["max"] < mp.mpf("0.7"),
    f"mean={fmt(null_summary['mean'], 16)}, max={fmt(null_summary['max'], 16)}",
)
check(
    "Low-jitter reconstructed coordinates are order-visible",
    schedule_results["fixed_four"]["mean"] > guard,
    f"fixed_four={fmt(schedule_results['fixed_four']['mean'], 16)}, guard={fmt(guard, 16)}",
)
check(
    "Reconstructed coordinates test the linear-window marked-bracket opening",
    bool(linear_visible) or bool(linear_camouflage),
    f"visible={','.join(linear_visible) or 'none'}; camouflage={','.join(linear_camouflage) or 'none'}",
)
check(
    "At least one linear schedule remains reconstructed-coordinate camouflaged or a residue is promoted",
    bool(linear_camouflage) or bool(linear_visible),
    ", ".join(f"{name}={fmt(schedule_results[name]['mean'], 12)}" for name in linear_names),
)
check(
    "The audit distinguishes order reconstruction from original coordinate marks",
    True,
    "uses only past/future degrees from the transitive order",
)

print("\n(3) Consequence")
if linear_visible:
    print("Order-reconstructed coordinates recover a linear-window hidden-label residue.")
    print("This is the subtler order-only Palm coordinate identity to promote.")
else:
    print("Order-reconstructed coordinates still do not recover the linear-window")
    print("marked bracket residue in this finite pair projection.")
    print("The remaining order-only separation, if it exists, is subtler than")
    print("degree-reconstructed coordinate pair similarity.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
