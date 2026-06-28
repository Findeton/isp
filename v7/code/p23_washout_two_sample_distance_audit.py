#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: two-sample washout distance audit.

The linear/superlinear washout audit found single clustered samples that sit
inside the finite sprinkling null after large rank mixing.  This receipt tests
the next hostile question: is that just one-sample luck, or do repeated
washed-out clustered samples look close to repeated sprinklings under the same
exact-pattern/rooted feature law?

Notation in the paper:
  P_N          = 1+1 sprinkling order law at N records.
  Q_N(w, j)   = width-w jittered clustered coordinate order law.

The receipt compares empirical laws with an energy distance after calibrating
the feature coordinates on repeated sprinklings.  It is a finite two-sample
projection, not an asymptotic theorem.

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
        self.outdeg = [mask.bit_count() for mask in self.future]
        self.indeg = [mask.bit_count() for mask in self.past]

    def relation_count(self):
        return sum(self.outdeg)

    def ordering_fraction(self):
        total = self.N * (self.N - 1) // 2
        return mp.mpf(self.relation_count()) / total if total else mp.mpf(0)

    def height(self):
        memo = [0] * self.N
        visiting = [False] * self.N

        def depth(x):
            if memo[x]:
                return memo[x]
            if visiting[x]:
                raise ValueError("cycle detected")
            visiting[x] = True
            best = 1
            for y in iter_bits(self.future[x]):
                best = max(best, 1 + depth(y))
            visiting[x] = False
            memo[x] = best
            return best

        return max(depth(x) for x in range(self.N)) if self.N else 0

    def interval_histogram(self):
        hist = [0] * self.N
        for x in range(self.N):
            for y in iter_bits(self.future[x]):
                hist[(self.future[x] & self.past[y]).bit_count()] += 1
        return hist


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


def mm_f(d):
    d = mp.mpf(d)
    return mp.gamma(d + 1) * mp.gamma(d / 2) / (2 * mp.gamma(3 * d / 2))


def mm_inv(r):
    r = mp.mpf(r)
    if r <= 0:
        return mp.inf
    if r >= 1:
        return mp.mpf(1)
    lo = mp.mpf(1)
    hi = mp.mpf(64)
    for _ in range(180):
        mid = (lo + hi) / 2
        if mm_f(mid) > r:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


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


def profile_P_from_hist_density(hist, N, alpha):
    q = mp.e ** (-mp.mpf(alpha))
    total = mp.mpf(0)
    power = mp.mpf(1)
    for count in hist:
        total += mp.mpf(count) / N * power
        power *= q
    return total


def height_scale_ratio(poset):
    return mp.mpf(poset.height()) / (2 * mp.sqrt(poset.N)) if poset.N else mp.mpf(0)


def exact_triple_counts(poset):
    N = poset.N
    relation_count = poset.relation_count()
    chain = sum(poset.indeg[y] * poset.outdeg[y] for y in range(N))

    future_relation_sum = 0
    for x in range(N):
        for y in iter_bits(poset.future[x]):
            future_relation_sum += poset.outdeg[y]
    vee = sum(f * (f - 1) // 2 for f in poset.outdeg) - future_relation_sum

    past_relation_sum = 0
    for z in range(N):
        for y in iter_bits(poset.past[z]):
            past_relation_sum += poset.indeg[y]
    wedge = sum(p * (p - 1) // 2 for p in poset.indeg) - past_relation_sum

    one_relation = relation_count * (N - 2) - 3 * chain - 2 * (vee + wedge)
    total = N * (N - 1) * (N - 2) // 6
    antichain = total - chain - vee - wedge - one_relation
    return {
        "antichain": antichain,
        "one_relation": one_relation,
        "vee": vee,
        "wedge": wedge,
        "chain": chain,
        "total": total,
    }


def exact_triple_densities(poset):
    counts = exact_triple_counts(poset)
    total = counts["total"]
    order = ["antichain", "one_relation", "vee", "wedge", "chain"]
    return [mp.mpf(counts[name]) / total for name in order], counts


def external_delta(poset, x, y):
    clear_x = ~(1 << x)
    clear_y = ~(1 << y)
    diff = ((poset.past[x] & clear_y) ^ (poset.past[y] & clear_x)).bit_count()
    diff += ((poset.future[x] & clear_y) ^ (poset.future[y] & clear_x)).bit_count()
    return diff


def rooted_near_features(poset, seed, root_count):
    rng = random.Random(seed)
    roots = rng.sample(range(poset.N), min(root_count, poset.N))
    tau = max(2, poset.N // 48)
    near_sum = mp.mpf(0)
    soft_sum = mp.mpf(0)
    min_sum = mp.mpf(0)
    for root in roots:
        deltas = [external_delta(poset, root, y) for y in range(poset.N) if y != root]
        near_sum += mp.mpf(sum(1 for delta in deltas if delta <= tau)) / poset.N
        soft_sum += sum(mp.e ** (-mp.mpf(delta) / (tau + 1)) for delta in deltas) / poset.N
        min_sum += mp.mpf(min(deltas)) / poset.N if deltas else mp.mpf(0)
    denom = len(roots)
    return [near_sum / denom, soft_sum / denom, min_sum / denom]


FEATURE_NAMES = [
    "r",
    "height_ratio",
    "p_log2_ratio",
    "tri_antichain",
    "tri_one_relation",
    "tri_vee",
    "tri_wedge",
    "tri_chain",
    "root_near",
    "root_soft",
    "root_min_delta",
]


def audit_vector(poset, seed):
    hist = poset.interval_histogram()
    expected = sprinkle_pair_density_expectation(poset.N, mp.log(2))
    observed = profile_P_from_hist_density(hist, poset.N, mp.log(2))
    triple, counts = exact_triple_densities(poset)
    vector = [
        poset.ordering_fraction(),
        height_scale_ratio(poset),
        observed / expected if expected else mp.mpf(0),
    ]
    vector.extend(triple)
    vector.extend(rooted_near_features(poset, seed, max(8, min(16, poset.N // 32))))
    return vector, counts


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


def std_vector(rows, mean):
    denom = max(1, len(rows) - 1)
    out = []
    for i in range(len(mean)):
        var = sum((row[i] - mean[i]) ** 2 for row in rows) / denom
        out.append(mp.sqrt(var))
    return out


def score_against(rows, candidate):
    mean = mean_vector(rows)
    std = std_vector(rows, mean)
    score = mp.mpf(0)
    components = []
    for name, value, mu, sigma in zip(FEATURE_NAMES, candidate, mean, std):
        ridge = max(abs(mu) * mp.mpf("0.02"), mp.mpf("1e-12"))
        denom = max(sigma, ridge)
        z = (value - mu) / denom
        score += z * z
        components.append((abs(z), name, z, value, mu, denom))
    components.sort(reverse=True, key=lambda item: item[0])
    return score, components


def same_label_observability(poset, labels):
    tau = max(2, poset.N // 48)
    count = 0
    near = 0
    delta_sum = mp.mpf(0)
    for x in range(poset.N):
        for y in range(x + 1, poset.N):
            if labels[x] != labels[y]:
                continue
            count += 1
            delta = external_delta(poset, x, y)
            delta_sum += mp.mpf(delta) / poset.N
            if delta <= tau:
                near += 1
    return {
        "pair_mass": mp.mpf(count) / (poset.N * (poset.N - 1) // 2),
        "same_near": mp.mpf(near) / count if count else mp.mpf(0),
        "same_delta": delta_sum / count if count else mp.mpf(0),
    }


def phase_name(score_ratio, same_near):
    if score_ratio > 10:
        return "separated"
    if score_ratio > 1:
        return "visible"
    if same_near > mp.mpf("0.25"):
        return "camouflage-with-near-labels"
    return "finite-camouflage"


print("=" * 80)
print("Collapsed P23 two-sample washout distance audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

Ns = [384, 768]
widths = [2, 4, 8]
schedules = ["fixed_4", "linear_1", "super_2"]
sprinkling_count = 16
candidate_count = 8


def schedule_effective(label, N):
    if label == "fixed_4":
        return 4
    if label == "linear_1":
        return int(N)
    if label == "super_2":
        return int(2 * N)
    raise ValueError(label)


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
    splits = [
        (indices[: count // 2], indices[count // 2 :]),
        (indices[::2], indices[1::2]),
        ([0, 1, 4, 5, 8, 9, 12, 13], [2, 3, 6, 7, 10, 11, 14, 15]),
        ([0, 2, 5, 7, 8, 10, 13, 15], [1, 3, 4, 6, 9, 11, 12, 14]),
    ]
    return splits


all_results = []
partition_ok = True

for N in Ns:
    print(f"\n(1) Empirical sprinkling law at N={N}")
    sprinkling_rows = []
    for index in range(sprinkling_count):
        poset = sprinkled2_poset(N, 1410000 + 1000 * N + index)
        row, counts = audit_vector(poset, 1420000 + 1000 * N + index)
        partition_ok = partition_ok and sum(
            counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]
        ) == counts["total"]
        sprinkling_rows.append(row)

    mean, denom = z_calibration(sprinkling_rows)
    z_sprinkling = z_transform(sprinkling_rows, mean, denom)
    null_energies = []
    split_blocks = []
    for left, right in deterministic_splits(sprinkling_count):
        left_rows = [z_sprinkling[i] for i in left]
        right_rows = [z_sprinkling[i] for i in right]
        split_blocks.append(left_rows)
        null_energies.append(law_distance(left_rows, right_rows))
    null_max = max(null_energies)
    null_med = sorted(null_energies)[len(null_energies) // 2]
    print("null law distances =", [fmt(value, 12) for value in null_energies])

    for width in widths:
        print(f"\nN={N}, w={width}")
        for label in schedules:
            effective = schedule_effective(label, N)
            candidate_rows = []
            same_near_values = []
            for rep in range(candidate_count):
                candidate, labels = clustered_jittered_fiber_poset(
                    N // width,
                    width,
                    19000 + 19 * N + 313 * width + 41 * effective + rep,
                    effective,
                    width,
                )
                row, counts = audit_vector(candidate, 1430000 + 1000 * N + 37 * width + effective + rep)
                partition_ok = partition_ok and sum(
                    counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]
                ) == counts["total"]
                candidate_rows.append(row)
                same_near_values.append(same_label_observability(candidate, labels)["same_near"])
            z_candidate = z_transform(candidate_rows, mean, denom)
            candidate_energies = [law_distance(block, z_candidate) for block in split_blocks]
            median_energy = sorted(candidate_energies)[len(candidate_energies) // 2]
            min_energy = min(candidate_energies)
            ratio = median_energy / null_max if null_max else mp.inf
            min_ratio = min_energy / null_max if null_max else mp.inf
            same_near_mean = sum(same_near_values) / len(same_near_values)
            phase = "two-sample-visible" if ratio > 1 else "two-sample-camouflage"
            print(
                f"{label:>8} eff/N={fmt(mp.mpf(effective)/N, 8)} "
                f"lawdist_med={fmt(median_energy, 18)} ratio={fmt(ratio, 18)} "
                f"min_ratio={fmt(min_ratio, 18)} same_near_mean={fmt(same_near_mean, 18)} "
                f"phase={phase}"
            )
            all_results.append(
                {
                    "N": N,
                    "width": width,
                    "label": label,
                    "effective": mp.mpf(effective),
                    "energy_ratio": ratio,
                    "min_ratio": min_ratio,
                    "same_near_mean": same_near_mean,
                    "phase": phase,
                    "null_max": null_max,
                    "null_med": null_med,
                }
            )


def result_for(N, width, label):
    for result in all_results:
        if result["N"] == N and result["width"] == width and result["label"] == label:
            return result
    raise KeyError((N, width, label))


fixed_visible = [result for result in all_results if result["label"] == "fixed_4" and result["energy_ratio"] > 1]
washed_camouflage_768 = [
    result
    for result in all_results
    if result["N"] == 768 and result["label"] in {"linear_1", "super_2"} and result["energy_ratio"] <= 1
]
washed_near_768 = [
    result["same_near_mean"]
    for result in all_results
    if result["N"] == 768 and result["label"] in {"linear_1", "super_2"}
]
mixed_outcomes = [
    result
    for result in all_results
    if result["label"] in {"linear_1", "super_2"} and result["energy_ratio"] > 1
]

check(
    "Exact three-record pattern densities partition every audited poset",
    partition_ok,
    "all antichain/one-relation/vee/wedge/chain counts sum to C(N,3)",
)
check(
    "Fixed small jitter is two-sample visible in at least one tested case",
    bool(fixed_visible),
    ", ".join(f"N={r['N']} w={r['width']} ratio={fmt(r['energy_ratio'], 8)}" for r in fixed_visible[:6]),
)
check(
    "At N=768 at least one linear/superlinear washed family is inside the two-sample null",
    bool(washed_camouflage_768),
    ", ".join(f"w={r['width']} {r['label']} ratio={fmt(r['energy_ratio'], 8)}" for r in washed_camouflage_768[:6]),
)
check(
    "Washed families at N=768 have negligible same-label near-twin visibility",
    all(value <= mp.mpf("0.02") for value in washed_near_768),
    ", ".join(fmt(value, 10) for value in washed_near_768),
)
check(
    "Large mixing is not a theorem-level guarantee in this finite projection",
    bool(mixed_outcomes),
    ", ".join(f"N={r['N']} w={r['width']} {r['label']} ratio={fmt(r['energy_ratio'], 8)}" for r in mixed_outcomes[:6]),
)

print("\n(2) Consequence")
print("The two-sample audit supports the split suggested by the washout test.")
print("Some large-mixing clustered generators are close to sprinkling under this")
print("finite empirical law, and their same-label near-twin signature is gone.")
print("But large mixing is not a theorem: some linear/superlinear cases remain")
print("two-sample visible.  The click-law target should be stated in terms of")
print("the induced record law, not the hidden generative label.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
