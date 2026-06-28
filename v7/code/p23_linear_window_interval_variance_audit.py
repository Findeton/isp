#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: linear-window interval variance audit.

Fixed unrooted k-patterns wash out in the bounded-width linear critical window.
The next possible residue is mesoscopic: interval/rectangle counts and their
brackets.  This receipt uses only order-visible data.  It samples comparable
endpoint pairs x<y and records |I(x,y)|/N, then compares the empirical law of
those interval-size features for sprinklings and linear-window clustered
coordinate generators.

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
        self.relations = [(x, y) for x in range(self.N) for y in iter_bits(self.future[x])]

    def relation_count(self):
        return len(self.relations)

    def interval_size(self, x, y):
        return (self.future[x] & self.past[y]).bit_count()


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


def sample_interval_sizes(poset, seed, sample_count):
    rng = random.Random(seed)
    if not poset.relations:
        return []
    out = []
    for _ in range(sample_count):
        x, y = poset.relations[rng.randrange(len(poset.relations))]
        out.append(poset.interval_size(x, y))
    return out


def quantile(sorted_values, numerator, denominator):
    if not sorted_values:
        return mp.mpf(0)
    index = (len(sorted_values) - 1) * numerator // denominator
    return sorted_values[index]


def interval_feature_vector(poset, seed, sample_count=768):
    sizes = sample_interval_sizes(poset, seed, sample_count)
    N = mp.mpf(poset.N)
    values = [mp.mpf(size) / N for size in sizes]
    mean = sum(values) / len(values)
    centered = [value - mean for value in values]
    var = sum(value * value for value in centered) / (len(values) - 1)
    third = sum(value ** 3 for value in centered) / len(values)
    fourth = sum(value ** 4 for value in centered) / len(values)
    ordered = sorted(values)
    low = sum(1 for value in values if value <= mp.mpf("0.02")) / mp.mpf(len(values))
    high = sum(1 for value in values if value >= mp.mpf("0.25")) / mp.mpf(len(values))
    return [
        mp.mpf(poset.relation_count()) / (poset.N * (poset.N - 1) // 2),
        mean,
        var,
        third,
        fourth,
        quantile(ordered, 1, 10),
        quantile(ordered, 1, 2),
        quantile(ordered, 9, 10),
        low,
        high,
    ]


FEATURE_NAMES = [
    "relation_density",
    "interval_mean",
    "interval_var",
    "interval_third",
    "interval_fourth",
    "interval_q10",
    "interval_q50",
    "interval_q90",
    "interval_low_mass",
    "interval_high_mass",
]


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


def std_vector(rows, mean):
    denom = max(1, len(rows) - 1)
    out = []
    for i in range(len(mean)):
        var = sum((row[i] - mean[i]) ** 2 for row in rows) / denom
        out.append(mp.sqrt(var))
    return out


def z_calibration(rows):
    mean = mean_vector(rows)
    std = std_vector(rows, mean)
    denom = [max(std[i], abs(mean[i]) * mp.mpf("0.02"), mp.mpf("1e-12")) for i in range(len(mean))]
    return mean, denom


def z_transform(rows, mean, denom):
    return [[(value - mean[i]) / denom[i] for i, value in enumerate(row)] for row in rows]


def empirical_profile(rows):
    means = mean_vector(rows)
    stds = std_vector(rows, means)
    return means, stds


def law_distance(rows_a, rows_b):
    means_a, stds_a = empirical_profile(rows_a)
    means_b, stds_b = empirical_profile(rows_b)
    mean_part = sum((a - b) ** 2 for a, b in zip(means_a, means_b))
    spread_part = sum((a - b) ** 2 for a, b in zip(stds_a, stds_b))
    return mp.sqrt(mean_part + mp.mpf("0.25") * spread_part)


def deterministic_splits(count):
    indices = list(range(count))
    return [
        (indices[: count // 2], indices[count // 2 :]),
        (indices[::2], indices[1::2]),
        ([0, 1, 4, 5, 8, 9, 12, 13], [2, 3, 6, 7, 10, 11, 14, 15]),
        ([0, 2, 5, 7, 8, 10, 13, 15], [1, 3, 4, 6, 9, 11, 12, 14]),
    ]


def top_component_differences(rows_a, rows_b):
    means_a, stds_a = empirical_profile(rows_a)
    means_b, stds_b = empirical_profile(rows_b)
    out = []
    for name, ma, mb, sa, sb in zip(FEATURE_NAMES, means_a, means_b, stds_a, stds_b):
        out.append((abs(ma - mb), name, ma, mb, sa, sb))
    return sorted(out, reverse=True, key=lambda item: item[0])


print("=" * 80)
print("Collapsed P23 linear-window interval variance audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

Ns = [384, 768]
widths = [2, 4, 8]
effective_scales = [("linear_half", mp.mpf("0.5")), ("linear_one", mp.mpf("1.0")), ("linear_two", mp.mpf("2.0"))]
sprinkling_count = 16
candidate_count = 8

all_results = []

for N in Ns:
    print(f"\n(1) Calibrating interval law at N={N}")
    sprinkling_rows = []
    for rep in range(sprinkling_count):
        poset = sprinkled2_poset(N, 1510000 + 1000 * N + rep)
        sprinkling_rows.append(interval_feature_vector(poset, 1520000 + 1000 * N + rep))
    mean, denom = z_calibration(sprinkling_rows)
    z_sprinkling = z_transform(sprinkling_rows, mean, denom)
    split_blocks = []
    null_distances = []
    for left, right in deterministic_splits(sprinkling_count):
        left_rows = [z_sprinkling[i] for i in left]
        right_rows = [z_sprinkling[i] for i in right]
        split_blocks.append(left_rows)
        null_distances.append(law_distance(left_rows, right_rows))
    null_max = max(null_distances)
    print("null distances =", [fmt(value, 12) for value in null_distances])

    for width in widths:
        print(f"\nN={N}, width={width}")
        for label, multiplier in effective_scales:
            effective = int(mp.nint(multiplier * N))
            candidate_rows = []
            for rep in range(candidate_count):
                candidate, _labels = clustered_jittered_fiber_poset(
                    N // width,
                    width,
                    1530000 + 1000 * N + 101 * width + 17 * effective + rep,
                    effective,
                    width,
                )
                candidate_rows.append(interval_feature_vector(candidate, 1540000 + 1000 * N + 101 * width + 17 * effective + rep))
            z_candidate = z_transform(candidate_rows, mean, denom)
            distances = [law_distance(block, z_candidate) for block in split_blocks]
            median_distance = sorted(distances)[len(distances) // 2]
            ratio = median_distance / null_max if null_max else mp.inf
            components = top_component_differences(z_sprinkling, z_candidate)
            top = ", ".join(
                f"{name}:dmean={fmt(mb - ma, 8)}"
                for _, name, ma, mb, _sa, _sb in components[:3]
            )
            phase = "interval-visible" if ratio > 1 else "interval-camouflage"
            print(
                f"{label:>11} eff/N={fmt(mp.mpf(effective)/N, 8)} "
                f"ratio={fmt(ratio, 18)} phase={phase} top=[{top}]"
            )
            all_results.append(
                {
                    "N": N,
                    "width": width,
                    "label": label,
                    "ratio": ratio,
                    "phase": phase,
                    "components": components[:3],
                }
            )

visible = [row for row in all_results if row["ratio"] > 1]
camouflage = [row for row in all_results if row["ratio"] <= 1]
visible_768 = [row for row in all_results if row["N"] == 768 and row["ratio"] > 1]
mixed_by_width = []
for N in Ns:
    for width in widths:
        phases = {row["phase"] for row in all_results if row["N"] == N and row["width"] == width}
        if len(phases) > 1:
            mixed_by_width.append((N, width, phases))

check(
    "Mesoscopic interval-size law sees at least one linear-window clustered family",
    bool(visible),
    ", ".join(f"N={r['N']} w={r['width']} {r['label']} ratio={fmt(r['ratio'], 8)}" for r in visible[:6]),
)
check(
    "The interval-size projection is not a complete critical-window classifier",
    bool(camouflage),
    ", ".join(f"N={r['N']} w={r['width']} {r['label']} ratio={fmt(r['ratio'], 8)}" for r in camouflage[:6]),
)
check(
    "At the largest tested scale interval-size moments can wash out all tested linear-window residue",
    not bool(visible_768),
    ", ".join(
        f"w={r['width']} {r['label']} ratio={fmt(r['ratio'], 8)}"
        for r in sorted(
            [row for row in all_results if row["N"] == 768],
            key=lambda item: item["ratio"],
            reverse=True,
        )[:6]
    ),
)
check(
    "Critical-window visibility depends on width and mixing scale, not only fixed patterns",
    bool(mixed_by_width),
    "; ".join(f"N={N} w={w} phases={','.join(sorted(phases))}" for N, w, phases in mixed_by_width),
)

print("\n(2) Consequence")
print("Fixed unrooted k-patterns wash out in the linear window, but mesoscopic")
print("interval-size fluctuation data can still see some smaller-scale clustered families.")
print("At the largest tested scale in this receipt, however, interval-size moments")
print("alone wash out on every tested linear-window family.  The next object must")
print("therefore be a load/covariance/bracket field, not a larger list of size")
print("moments.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
