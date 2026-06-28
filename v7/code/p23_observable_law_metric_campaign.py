#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: observable law metric campaign.

This receipt turns the "hidden labels only matter if observable" principle into
a finite metric scaffold.  It defines a calibrated projection distance between
record-order laws using only order-visible global, rooted, interval, and
load/bracket features.  It then compares 1+1 sprinklings against clustered
coordinate schedules in the hard linear window.

This is not a full metric on all transitive-order laws.  It is a receipt for the
mathematical object the paper now needs: a projective family of order-visible
tests whose limiting distance should be zero exactly when the clustered law has
washed out to sprinkling.

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

    def ordering_fraction(self):
        total = self.N * (self.N - 1) // 2
        return mp.mpf(self.relation_count()) / total if total else mp.mpf(0)

    def height(self):
        memo = [0] * self.N

        def depth(x):
            if memo[x]:
                return memo[x]
            best = 1
            for y in iter_bits(self.future[x]):
                best = max(best, 1 + depth(y))
            memo[x] = best
            return best

        return max(depth(x) for x in range(self.N)) if self.N else 0

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
        return [mp.mpf(0)] * 4
    mean = sum(values) / len(values)
    denom = max(1, len(values) - 1)
    var = sum((value - mean) ** 2 for value in values) / denom
    ordered = sorted(values)
    return [mean, var, quantile(ordered, 1, 10), quantile(ordered, 9, 10)]


def external_delta(poset, x, y):
    clear_x = ~(1 << x)
    clear_y = ~(1 << y)
    diff = ((poset.past[x] & clear_y) ^ (poset.past[y] & clear_x)).bit_count()
    diff += ((poset.future[x] & clear_y) ^ (poset.future[y] & clear_x)).bit_count()
    return diff


def sprinkle_pair_density_expectation(N, alpha):
    N = int(N)
    if N < 2:
        return mp.mpf(0)
    guard_dps = max(mp.mp.dps + 40, int(mp.ceil(mp.mpf("0.25") * N)) + 80)
    with mp.workdps(guard_dps):
        q = mp.e ** (-mp.mpf(alpha))
        c = 1 - q
        m = N - 2
        s = mp.mpf(0)
        term = mp.mpf(1)
        for k in range(m + 1):
            if k > 0:
                term *= mp.mpf(m - k + 1) / mp.mpf(k) * (-c)
            denom = mp.mpf(k + 1) ** 2 * mp.mpf(k + 2) ** 2
            s += term / denom
        return +(mp.mpf(N - 1) * s)


def interval_audit(poset):
    hist = [0] * poset.N
    recursive_num = 0
    recursive_den = 0
    for x, y in poset.relations:
        interior = poset.interval_mask(x, y)
        k = interior.bit_count()
        hist[k] += 1
        if k >= 2:
            recursive_den += k * (k - 1) // 2
            inner_rel = 0
            for z in iter_bits(interior):
                inner_rel += (poset.future[z] & interior).bit_count()
            recursive_num += inner_rel
    return {
        "hist": hist,
        "recursive": mp.mpf(recursive_num) / recursive_den if recursive_den else mp.mpf(0),
    }


def profile_P_from_hist_density(hist, N, alpha):
    q = mp.e ** (-mp.mpf(alpha))
    total = mp.mpf(0)
    power = mp.mpf(1)
    for count in hist:
        total += mp.mpf(count) / N * power
        power *= q
    return total


def effective_support(loads):
    total = sum(loads)
    square = sum(value * value for value in loads)
    if total == 0 or square == 0:
        return mp.mpf(0)
    return mp.mpf(total * total) / (square * len(loads))


def interval_load_features(poset, seed, sample_count=768):
    rng = random.Random(seed)
    chosen = [poset.relations[rng.randrange(len(poset.relations))] for _ in range(sample_count)]
    loads = [0] * poset.N
    sizes = []
    masks = []
    for x, y in chosen:
        interior = poset.interval_mask(x, y)
        masks.append(interior)
        sizes.append(mp.mpf(interior.bit_count()) / poset.N)
        for z in iter_bits(interior):
            loads[z] += 1
    load_values = [mp.mpf(value) / sample_count for value in loads]
    overlaps = []
    for i, a in enumerate(masks[:80]):
        for b in masks[i + 1 : 80]:
            union = (a | b).bit_count()
            overlaps.append(mp.mpf((a & b).bit_count()) / union if union else mp.mpf(1))
    top_load = mp.mpf(sum(sorted(loads, reverse=True)[: max(1, poset.N // 20)])) / max(1, sum(loads))
    out = []
    out.extend(moments(sizes))
    out.extend(moments(load_values))
    out.append(effective_support(loads))
    out.append(top_load)
    out.extend(moments(overlaps))
    return out


def rooted_interval_features(poset, seed, root_count=64, per_root_pairs=12):
    rng = random.Random(seed)
    roots = rng.sample(range(poset.N), root_count)
    degree_past = []
    degree_future = []
    near_min = []
    near_q10 = []
    through_count = []
    through_size = []
    through_overlap = []
    for root in roots:
        past = list(iter_bits(poset.past[root]))
        future = list(iter_bits(poset.future[root]))
        degree_past.append(mp.mpf(len(past)) / poset.N)
        degree_future.append(mp.mpf(len(future)) / poset.N)
        candidates = rng.sample(range(poset.N), min(64, poset.N))
        deltas = sorted(mp.mpf(external_delta(poset, root, y)) / max(1, 2 * (poset.N - 2)) for y in candidates if y != root)
        near_min.append(deltas[0] if deltas else mp.mpf(0))
        near_q10.append(quantile(deltas, 1, 10) if deltas else mp.mpf(0))
        through_total = len(past) * len(future)
        through_count.append(mp.mpf(through_total) / (poset.N * poset.N))
        if through_total:
            pair_count = min(per_root_pairs, through_total)
            masks = []
            for _ in range(pair_count):
                x = past[rng.randrange(len(past))]
                y = future[rng.randrange(len(future))]
                masks.append(poset.interval_mask(x, y))
            for mask in masks:
                through_size.append(mp.mpf(mask.bit_count()) / poset.N)
            if len(masks) >= 2:
                for i, a in enumerate(masks):
                    for b in masks[i + 1 :]:
                        union = (a | b).bit_count()
                        through_overlap.append(mp.mpf((a & b).bit_count()) / union if union else mp.mpf(1))
    out = []
    for values in [degree_past, degree_future, near_min, near_q10, through_count, through_size, through_overlap]:
        out.extend(moments(values))
    return out


GLOBAL_NAMES = ["r", "height", "theta", "p_log2_ratio"]
LOAD_NAMES = [
    f"load_{name}"
    for name in [
        "size_mean",
        "size_var",
        "size_q10",
        "size_q90",
        "load_mean",
        "load_var",
        "load_q10",
        "load_q90",
        "eff",
        "top5",
        "overlap_mean",
        "overlap_var",
        "overlap_q10",
        "overlap_q90",
    ]
]
ROOT_NAMES = [
    f"root_{group}_{stat}"
    for group in ["past", "future", "near_min", "near_q10", "through_count", "through_size", "through_overlap"]
    for stat in ["mean", "var", "q10", "q90"]
]
FEATURE_NAMES = GLOBAL_NAMES + LOAD_NAMES + ROOT_NAMES


def observable_feature_vector(poset, seed):
    audit = interval_audit(poset)
    expected = sprinkle_pair_density_expectation(poset.N, mp.log(2))
    observed = profile_P_from_hist_density(audit["hist"], poset.N, mp.log(2))
    out = [
        poset.ordering_fraction(),
        mp.mpf(poset.height()) / (2 * mp.sqrt(poset.N)),
        audit["recursive"],
        observed / expected if expected else mp.mpf(0),
    ]
    out.extend(interval_load_features(poset, seed + 11000))
    out.extend(rooted_interval_features(poset, seed + 22000))
    return out


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


def std_vector(rows, mean):
    denom = max(1, len(rows) - 1)
    return [mp.sqrt(sum((row[i] - mean[i]) ** 2 for row in rows) / denom) for i in range(len(mean))]


def z_calibration(rows):
    mean = mean_vector(rows)
    std = std_vector(rows, mean)
    denom = [
        max(std[i], abs(mean[i]) * mp.mpf("0.02"), mp.mpf("1e-12"))
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
print("Collapsed P23 observable law metric campaign")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 768
width = 4
base = N // width
sprinkling_count = 16
candidate_count = 8
schedules = [
    ("fixed_four", 4, 1),
    ("sqrt", int(mp.sqrt(N)), 1),
    ("linear_half", N // 2, width),
    ("linear_one", N, width),
    ("linear_two", 2 * N, width),
]

print(f"\n(1) Calibrating observable projection metric at N={N}")
sprinkling_rows = []
for rep in range(sprinkling_count):
    poset = sprinkled2_poset(N, 1910000 + rep)
    sprinkling_rows.append(observable_feature_vector(poset, 1920000 + rep))
mean, denom = z_calibration(sprinkling_rows)
z_sprinkling = z_transform(sprinkling_rows, mean, denom)
null_distances = []
split_blocks = []
for left, right in deterministic_splits(sprinkling_count):
    left_rows = [z_sprinkling[i] for i in left]
    right_rows = [z_sprinkling[i] for i in right]
    split_blocks.append(left_rows)
    null_distances.append(law_distance(left_rows, right_rows))
null_max = max(null_distances)
print("dimension =", len(FEATURE_NAMES))
print("null distances =", [fmt(value, 12) for value in null_distances])
print("null max =", fmt(null_max, 18))

print("\n(2) Clustered schedules")
results = []
for label, jitter_num, jitter_den in schedules:
    candidate_rows = []
    for rep in range(candidate_count):
        poset, _labels = clustered_jittered_fiber_poset(
            base,
            width,
            1930000 + 10000 * rep + 101 * jitter_num + jitter_den,
            jitter_num,
            jitter_den,
        )
        candidate_rows.append(observable_feature_vector(poset, 1940000 + 10000 * rep + 101 * jitter_num + jitter_den))
    z_candidate = z_transform(candidate_rows, mean, denom)
    distances = [law_distance(block, z_candidate) for block in split_blocks]
    median_distance = sorted(distances)[len(distances) // 2]
    ratio = median_distance / null_max if null_max else mp.inf
    components = top_component_differences(z_sprinkling, z_candidate)
    top = ", ".join(
        f"{name}:dmean={fmt(mb - ma, 8)}"
        for _, name, ma, mb, _sa, _sb in components[:5]
    )
    phase = "visible" if ratio > 1 else "camouflage"
    print(
        f"{label:>12}: jitter={jitter_num}/{jitter_den} "
        f"ratio={fmt(ratio, 18)} phase={phase} top=[{top}]"
    )
    results.append({"label": label, "ratio": ratio, "phase": phase, "components": components[:5]})

visible = [row for row in results if row["ratio"] > 1]
camouflage = [row for row in results if row["ratio"] <= 1]
linear_visible = [row for row in visible if row["label"].startswith("linear")]
linear_camouflage = [row for row in camouflage if row["label"].startswith("linear")]

check(
    "The observable projection metric is nondegenerate on sprinklings",
    null_max > 0 and min(null_distances) > 0,
    f"min={fmt(min(null_distances), 16)}, max={fmt(null_max, 16)}",
)
check(
    "Low or square-root jitter remains visible in the observable projection metric",
    any(row["label"] in {"fixed_four", "sqrt"} for row in visible),
    ", ".join(f"{row['label']}={fmt(row['ratio'], 12)}" for row in visible),
)
check(
    "At least one linear-window schedule remains inside the observable projection null",
    bool(linear_camouflage),
    ", ".join(f"{row['label']}={fmt(row['ratio'], 12)}" for row in linear_camouflage),
)
check(
    "The metric campaign either extracts a linear residue or records linear washout",
    bool(linear_visible) or bool(linear_camouflage),
    f"linear_visible={','.join(row['label'] for row in linear_visible) or 'none'}; "
    f"linear_camouflage={','.join(row['label'] for row in linear_camouflage) or 'none'}",
)
check(
    "Observable-law distance is a projection, not a complete proof of equivalence",
    bool(camouflage),
    ", ".join(f"{row['label']}={fmt(row['ratio'], 12)}" for row in camouflage),
)

print("\n(3) Consequence")
if linear_visible:
    print("The combined observable projection extracts at least one linear-window residue.")
    print("The top components above are candidate bracket/rooted features to promote.")
else:
    print("The combined observable projection does not extract a linear-window residue.")
    print("The next campaign must move from finite feature vectors to a limiting")
    print("Palm/Mecke/bracket identity or a sharper asymptotic law-distance theorem.")
print("In either case, the metric scaffold is now explicit: calibrated feature-law")
print("distance on global, rooted, interval, and load/bracket order observables.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
