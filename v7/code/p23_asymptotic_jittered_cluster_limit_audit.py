#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: asymptotic jittered-cluster limit audit.

The previous finite Mecke/Palm shadow rejected a gross density-modulated process
but not the jittered hidden-width sweep.  This receipt asks the next question:
does the jittered clustered process converge to the same order law as a 1+1
sprinkling, or does an order-visible asymptotic difference remain?

The audit uses exact full three-record induced-pattern densities, not sampled
small-pattern one-offs, together with global order and interval-profile
features.  It tests N=192,384,768 and a fixed-width jitter sweep.

All asserted non-integer arithmetic uses mpmath with dps=140.  Poset statistics
are integer bitset counts; no float64 arithmetic is used for asserted values.
"""

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


print("=" * 80)
print("Collapsed P23 asymptotic jittered-cluster limit audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

Ns = [192, 384, 768]
sprinkling_count = 5
jitters = [0, 1, 2, 4]
width = 4
all_results = []
partition_ok = True

for N in Ns:
    print(f"\n(1) Scale N={N}")
    sprinkling_rows = []
    holdout_rows = []
    for index in range(sprinkling_count):
        poset = sprinkled2_poset(N, 1110000 + 1000 * N + index)
        row, counts = audit_vector(poset, 1120000 + 1000 * N + index)
        partition_ok = partition_ok and sum(counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]) == counts["total"]
        sprinkling_rows.append(row)
    for index in range(2):
        poset = sprinkled2_poset(N, 1130000 + 1000 * N + index)
        row, counts = audit_vector(poset, 1140000 + 1000 * N + index)
        partition_ok = partition_ok and sum(counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]) == counts["total"]
        holdout_rows.append(row)

    holdout_scores = [score_against(sprinkling_rows, row)[0] for row in holdout_rows]
    print("holdout scores =", [fmt(score, 12) for score in holdout_scores])
    print("sprinkling mean r =", fmt(mean_vector(sprinkling_rows)[0], 18))
    scale_result = {"N": N, "holdout_max": max(holdout_scores), "candidates": []}

    for jitter in jitters:
        candidate, labels = clustered_jittered_fiber_poset(N // width, width, 16002 + N, jitter, 1)
        row, counts = audit_vector(candidate, 1150000 + 1000 * N + jitter)
        partition_ok = partition_ok and sum(counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]) == counts["total"]
        score, components = score_against(sprinkling_rows, row)
        observable = same_label_observability(candidate, labels)
        top = ", ".join(
            f"{name}:z={fmt(z, 6)}" for _, name, z, *_ in components[:3]
        )
        print(
            f"jitter={jitter}: score={fmt(score, 18)} "
            f"score/holdout={fmt(score / scale_result['holdout_max'], 18)} "
            f"same_near={fmt(observable['same_near'], 18)} "
            f"same_delta={fmt(observable['same_delta'], 18)} top=[{top}]"
        )
        scale_result["candidates"].append(
            {
                "jitter": jitter,
                "score": score,
                "score_ratio": score / scale_result["holdout_max"],
                "same_near": observable["same_near"],
                "same_delta": observable["same_delta"],
                "top_components": components[:3],
            }
        )
    all_results.append(scale_result)

print("\n(2) Scaling table")
for result in all_results:
    row = [f"N={result['N']}"]
    for candidate in result["candidates"]:
        row.append(f"j{candidate['jitter']}={fmt(candidate['score_ratio'], 10)}")
    print("  " + ", ".join(row))

j0_ratios = [r["candidates"][0]["score_ratio"] for r in all_results]
j4_ratios = [r["candidates"][-1]["score_ratio"] for r in all_results]
j4_same_near = [r["candidates"][-1]["same_near"] for r in all_results]

check(
    "Exact three-record pattern densities partition every audited poset",
    partition_ok,
    "all antichain/one-relation/vee/wedge/chain counts sum to C(N,3)",
)
check(
    "Low-jitter hidden fibers remain order-visible in the scaling audit",
    all(ratio > 1 for ratio in j0_ratios),
    ", ".join(f"N={r['N']} j0_ratio={fmt(r['candidates'][0]['score_ratio'], 12)}" for r in all_results),
)
check(
    "High jitter reduces same-label near-twin visibility",
    all(value < mp.mpf("0.25") for value in j4_same_near),
    ", ".join(f"N={r['N']} j4_same_near={fmt(r['candidates'][-1]['same_near'], 12)}" for r in all_results),
)
check(
    "High-jitter clustered orders are not eliminated by this finite asymptotic projection",
    any(ratio <= 1 for ratio in j4_ratios) or any(j4_ratios[i] < j0_ratios[i] for i in range(len(j4_ratios))),
    ", ".join(f"N={r['N']} j4_ratio={fmt(r['candidates'][-1]['score_ratio'], 12)}" for r in all_results),
)
check(
    "Scaling audit leaves a phase-boundary problem rather than a completed law",
    all(j0_ratios[i] > j4_ratios[i] for i in range(len(j0_ratios))),
    ", ".join(
        f"N={r['N']} j0={fmt(r['candidates'][0]['score_ratio'], 8)} j4={fmt(r['candidates'][-1]['score_ratio'], 8)}"
        for r in all_results
    ),
)

print("\n(3) Consequence")
print("Exact triple-pattern and interval-profile scaling separates low-jitter hidden")
print("fibers strongly, but high jitter washes out much of the order-visible hidden")
print("label structure.  The surviving problem is a phase-boundary/asymptotic one:")
print("determine whether high-jitter clustered coordinate processes converge to the")
print("same order law as sprinkling or retain a persistent higher-order signature.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
