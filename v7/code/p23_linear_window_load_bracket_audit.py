#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: linear-window load/bracket audit.

The interval-size moment projection can wash out at the largest tested critical
scale.  This receipt follows the next opening: do not only ask how large sampled
intervals are; ask how their interiors distribute load across records and
across interval-size bands.  This is still order-visible: it uses only the
transitive relation and open interval masks.

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

    def interval_mask(self, x, y):
        return self.future[x] & self.past[y]


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


def quantile(sorted_values, numerator, denominator):
    if not sorted_values:
        return mp.mpf(0)
    index = (len(sorted_values) - 1) * numerator // denominator
    return sorted_values[index]


def moments(values):
    if not values:
        return [mp.mpf(0)] * 6
    mean = sum(values) / len(values)
    denom = max(1, len(values) - 1)
    var = sum((value - mean) ** 2 for value in values) / denom
    ordered = sorted(values)
    return [
        mean,
        var,
        quantile(ordered, 1, 2),
        quantile(ordered, 9, 10),
        quantile(ordered, 99, 100),
        ordered[-1],
    ]


def effective_support(loads):
    total = sum(loads)
    square = sum(value * value for value in loads)
    if total == 0 or square == 0:
        return mp.mpf(0)
    return mp.mpf(total * total) / (square * len(loads))


def top_mass(loads, numerator, denominator):
    total = sum(loads)
    if total == 0:
        return mp.mpf(0)
    count = max(1, len(loads) * numerator // denominator)
    return mp.mpf(sum(sorted(loads, reverse=True)[:count])) / total


def overlap_features(masks, sample_limit):
    if len(masks) < 2:
        return [mp.mpf(0)] * 4
    chosen = masks[:sample_limit]
    overlaps = []
    nested = 0
    disjoint = 0
    for i, a in enumerate(chosen):
        for b in chosen[i + 1 :]:
            inter = (a & b).bit_count()
            if inter == 0:
                disjoint += 1
                overlaps.append(mp.mpf(0))
                continue
            union = (a | b).bit_count()
            overlaps.append(mp.mpf(inter) / union)
            if (a & ~b) == 0 or (b & ~a) == 0:
                nested += 1
    pair_count = len(chosen) * (len(chosen) - 1) // 2
    ordered = sorted(overlaps)
    return [
        sum(overlaps) / len(overlaps),
        quantile(ordered, 9, 10),
        mp.mpf(nested) / pair_count,
        mp.mpf(disjoint) / pair_count,
    ]


def load_bracket_feature_vector(poset, seed, sample_count=1536):
    rng = random.Random(seed)
    N = poset.N
    if not poset.relations:
        return [mp.mpf(0)] * len(FEATURE_NAMES)

    chosen = [poset.relations[rng.randrange(len(poset.relations))] for _ in range(sample_count)]
    sizes = []
    masks = []
    all_load = [0] * N
    band_loads = [[0] * N for _ in range(3)]
    band_counts = [0, 0, 0]

    for x, y in chosen:
        interior = poset.interval_mask(x, y)
        k = interior.bit_count()
        masks.append(interior)
        sizes.append(k)
        if k <= N // 16:
            band = 0
        elif k <= N // 4:
            band = 1
        else:
            band = 2
        band_counts[band] += 1
        for z in iter_bits(interior):
            all_load[z] += 1
            band_loads[band][z] += 1

    size_values = [mp.mpf(k) / N for k in sizes]
    load_values = [mp.mpf(value) / sample_count for value in all_load]
    out = [
        mp.mpf(poset.relation_count()) / (N * (N - 1) // 2),
        mp.mpf(sum(band_counts[0:1])) / sample_count,
        mp.mpf(sum(band_counts[1:2])) / sample_count,
        mp.mpf(sum(band_counts[2:3])) / sample_count,
    ]
    out.extend(moments(size_values))
    out.extend(moments(load_values))
    out.append(effective_support(all_load))
    out.append(top_mass(all_load, 1, 100))
    out.append(top_mass(all_load, 1, 10))

    for loads in band_loads:
        values = [mp.mpf(value) / sample_count for value in loads]
        stats = moments(values)
        out.extend([stats[1], stats[3], stats[5], effective_support(loads), top_mass(loads, 1, 20)])

    out.extend(overlap_features(masks, 96))
    return out


FEATURE_NAMES = (
    ["relation_density", "band_small", "band_mid", "band_large"]
    + [f"size_{name}" for name in ["mean", "var", "q50", "q90", "q99", "max"]]
    + [f"load_{name}" for name in ["mean", "var", "q50", "q90", "q99", "max"]]
    + ["load_eff", "load_top1pct", "load_top10pct"]
    + [
        f"{band}_{name}"
        for band in ["small", "mid", "large"]
        for name in ["load_var", "load_q90", "load_max", "load_eff", "load_top5pct"]
    ]
    + ["overlap_mean", "overlap_q90", "overlap_nested", "overlap_disjoint"]
)


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


def std_vector(rows, mean):
    denom = max(1, len(rows) - 1)
    out = []
    for i in range(len(mean)):
        out.append(mp.sqrt(sum((row[i] - mean[i]) ** 2 for row in rows) / denom))
    return out


def z_calibration(rows):
    mean = mean_vector(rows)
    std = std_vector(rows, mean)
    denom = [
        max(std[i], abs(mean[i]) * mp.mpf("0.015"), mp.mpf("1e-12"))
        for i in range(len(mean))
    ]
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
print("Collapsed P23 linear-window load/bracket audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

Ns = [384, 768]
widths = [2, 4, 8]
effective_scales = [
    ("linear_half", mp.mpf("0.5")),
    ("linear_one", mp.mpf("1.0")),
    ("linear_two", mp.mpf("2.0")),
]
sprinkling_count = 16
candidate_count = 8

all_results = []

for N in Ns:
    print(f"\n(1) Calibrating load/bracket law at N={N}")
    sprinkling_rows = []
    for rep in range(sprinkling_count):
        poset = sprinkled2_poset(N, 1610000 + 1000 * N + rep)
        sprinkling_rows.append(
            load_bracket_feature_vector(poset, 1620000 + 1000 * N + rep)
        )
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
    print("dimension =", len(FEATURE_NAMES))
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
                    1630000 + 1000 * N + 101 * width + 17 * effective + rep,
                    effective,
                    width,
                )
                candidate_rows.append(
                    load_bracket_feature_vector(
                        candidate, 1640000 + 1000 * N + 101 * width + 17 * effective + rep
                    )
                )
            z_candidate = z_transform(candidate_rows, mean, denom)
            distances = [law_distance(block, z_candidate) for block in split_blocks]
            median_distance = sorted(distances)[len(distances) // 2]
            ratio = median_distance / null_max if null_max else mp.inf
            components = top_component_differences(z_sprinkling, z_candidate)
            top = ", ".join(
                f"{name}:dmean={fmt(mb - ma, 8)}"
                for _, name, ma, mb, _sa, _sb in components[:4]
            )
            phase = "bracket-visible" if ratio > 1 else "bracket-camouflage"
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
                    "components": components[:4],
                }
            )

visible = [row for row in all_results if row["ratio"] > 1]
camouflage = [row for row in all_results if row["ratio"] <= 1]
visible_768 = [row for row in all_results if row["N"] == 768 and row["ratio"] > 1]
camouflage_768 = [row for row in all_results if row["N"] == 768 and row["ratio"] <= 1]
mixed_by_width = []
for N in Ns:
    for width in widths:
        phases = {row["phase"] for row in all_results if row["N"] == N and row["width"] == width}
        if len(phases) > 1:
            mixed_by_width.append((N, width, phases))

check(
    "The load/bracket projection has a nonempty finite camouflage set",
    bool(camouflage),
    ", ".join(f"N={r['N']} w={r['width']} {r['label']} ratio={fmt(r['ratio'], 8)}" for r in camouflage[:6]),
)
check(
    "The load/bracket projection has a nonempty finite visible set",
    bool(visible),
    ", ".join(f"N={r['N']} w={r['width']} {r['label']} ratio={fmt(r['ratio'], 8)}" for r in visible[:6]),
)
check(
    "At N=768 the finite load/bracket projection is not a complete classifier",
    bool(camouflage_768),
    ", ".join(f"w={r['width']} {r['label']} ratio={fmt(r['ratio'], 8)}" for r in camouflage_768[:6]),
)
check(
    "At N=768 the finite load/bracket projection still sees some residue",
    bool(visible_768),
    ", ".join(f"w={r['width']} {r['label']} ratio={fmt(r['ratio'], 8)}" for r in visible_768[:6]),
)
check(
    "Critical-window bracket visibility depends on width and mixing scale",
    bool(mixed_by_width),
    "; ".join(f"N={N} w={w} phases={','.join(sorted(phases))}" for N, w, phases in mixed_by_width),
)

print("\n(2) Consequence")
if visible_768:
    print("Adding load/bracket fields restores some N=768 visibility after")
    print("interval-size moments alone washed out, but camouflage cases remain.")
else:
    print("Even the finite load/bracket projection fails to restore N=768")
    print("visibility in this campaign; the target must move to a sharper")
    print("process-level bracket or an asymptotic theorem rather than a finite score.")
print("Either way, the linear window is narrower than a hidden-fiber problem:")
print("the relevant question is whether the induced order process itself has the")
print("same bracket law as sprinkling.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
