#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: jitter scaling phase diagram.

The previous asymptotic audit found a phase-boundary hint: high jitter can pass
small finite projections and then separate at larger N.  This receipt maps that
phenomenon directly for a fixed hidden width and several jitter scales.

Notation in the paper:
  P_N          = 1+1 sprinkling order law at N records.
  Q_N(w, j)   = width-w jittered clustered coordinate order law.

The receipt compares Q_N against calibrated P_N shadows using exact full
three-record induced-pattern densities, global interval-profile features, and
rooted near-neighborhood features.  It is a finite phase diagram, not an
asymptotic theorem.

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
print("Collapsed P23 jitter scaling phase diagram")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

Ns = [192, 384, 768]
sprinkling_count = 5
width = 4
jitter_settings = [
    ("locked", 0, 1),
    ("micro", 1, 4),
    ("unit", 1, 1),
    ("two", 2, 1),
    ("four", 4, 1),
    ("eight", 8, 1),
]

all_results = []
partition_ok = True

for N in Ns:
    print(f"\n(1) Scale N={N}, width={width}")
    sprinkling_rows = []
    holdout_rows = []
    for index in range(sprinkling_count):
        poset = sprinkled2_poset(N, 1210000 + 1000 * N + index)
        row, counts = audit_vector(poset, 1220000 + 1000 * N + index)
        partition_ok = partition_ok and sum(
            counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]
        ) == counts["total"]
        sprinkling_rows.append(row)
    for index in range(2):
        poset = sprinkled2_poset(N, 1230000 + 1000 * N + index)
        row, counts = audit_vector(poset, 1240000 + 1000 * N + index)
        partition_ok = partition_ok and sum(
            counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]
        ) == counts["total"]
        holdout_rows.append(row)
    holdout_scores = [score_against(sprinkling_rows, row)[0] for row in holdout_rows]
    holdout_max = max(holdout_scores)
    print("holdout scores =", [fmt(score, 12) for score in holdout_scores])
    scale_result = {"N": N, "holdout_max": holdout_max, "candidates": []}
    for label, jitter_num, jitter_den in jitter_settings:
        candidate, labels = clustered_jittered_fiber_poset(
            N // width, width, 17000 + 13 * N + jitter_num * 17 + jitter_den, jitter_num, jitter_den
        )
        row, counts = audit_vector(candidate, 1250000 + 1000 * N + jitter_num * 17 + jitter_den)
        partition_ok = partition_ok and sum(
            counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]
        ) == counts["total"]
        score, components = score_against(sprinkling_rows, row)
        observable = same_label_observability(candidate, labels)
        score_ratio = score / holdout_max
        effective = mp.mpf(width) * mp.mpf(jitter_num) / mp.mpf(jitter_den)
        top = ", ".join(f"{name}:z={fmt(z, 6)}" for _, name, z, *_ in components[:3])
        phase = phase_name(score_ratio, observable["same_near"])
        print(
            f"{label} j={jitter_num}/{jitter_den} eff={fmt(effective, 8)} "
            f"ratio={fmt(score_ratio, 18)} same_near={fmt(observable['same_near'], 18)} "
            f"same_delta={fmt(observable['same_delta'], 18)} phase={phase} top=[{top}]"
        )
        scale_result["candidates"].append(
            {
                "label": label,
                "jitter_num": jitter_num,
                "jitter_den": jitter_den,
                "effective": effective,
                "score": score,
                "score_ratio": score_ratio,
                "same_near": observable["same_near"],
                "same_delta": observable["same_delta"],
                "phase": phase,
                "top": components[:3],
            }
        )
    all_results.append(scale_result)

print("\n(2) Phase table")
for result in all_results:
    print(f"N={result['N']}:")
    for candidate in result["candidates"]:
        print(
            f"  {candidate['label']:>6} eff={fmt(candidate['effective'], 6):>8} "
            f"ratio={fmt(candidate['score_ratio'], 10):>14} "
            f"same_near={fmt(candidate['same_near'], 8):>12} "
            f"phase={candidate['phase']}"
        )

by_label = {
    label: [result["candidates"][i] for result in all_results]
    for i, (label, _, _) in enumerate(jitter_settings)
}

locked_ratios = [candidate["score_ratio"] for candidate in by_label["locked"]]
four_ratios = [candidate["score_ratio"] for candidate in by_label["four"]]
eight_ratios = [candidate["score_ratio"] for candidate in by_label["eight"]]
near_by_scale_is_decreasing = []
for result in all_results:
    near_values = [candidate["same_near"] for candidate in result["candidates"]]
    near_by_scale_is_decreasing.append(
        all(near_values[i] >= near_values[i + 1] for i in range(len(near_values) - 1))
    )

phase_changes = []
for label, candidates in by_label.items():
    phases = [candidate["phase"] for candidate in candidates]
    if len(set(phases)) > 1:
        phase_changes.append((label, phases))

check(
    "Exact three-record pattern densities partition every audited poset",
    partition_ok,
    "all antichain/one-relation/vee/wedge/chain counts sum to C(N,3)",
)
check(
    "Locked hidden fibers are separated at every tested scale",
    all(ratio > 10 for ratio in locked_ratios),
    ", ".join(f"N={r['N']} locked={fmt(by_label['locked'][i]['score_ratio'], 12)}" for i, r in enumerate(all_results)),
)
check(
    "Same-label near-twin visibility decreases as jitter scale increases",
    all(near_by_scale_is_decreasing),
    ", ".join(f"N={r['N']} monotone={near_by_scale_is_decreasing[i]}" for i, r in enumerate(all_results)),
)
check(
    "At least one high-jitter schedule has finite camouflage at small N and separates later",
    any(
        candidates[0]["score_ratio"] <= 1
        and candidates[1]["score_ratio"] <= 1
        and candidates[-1]["score_ratio"] > 1
        for candidates in [by_label["two"], by_label["four"], by_label["eight"]]
    ),
    ", ".join(
        f"{label}: {fmt(candidates[0]['score_ratio'], 8)}->{fmt(candidates[1]['score_ratio'], 8)}->{fmt(candidates[-1]['score_ratio'], 8)}"
        for label, candidates in [("two", by_label["two"]), ("four", by_label["four"]), ("eight", by_label["eight"])]
    ),
)
check(
    "The tested diagram has a nontrivial phase boundary rather than one universal score cutoff",
    len(phase_changes) >= 1,
    "; ".join(f"{label}:{'/'.join(phases)}" for label, phases in phase_changes),
)
check(
    "No tested fixed-jitter schedule proves full washout across all scales",
    all(any(candidate["score_ratio"] > 1 for candidate in candidates) for candidates in by_label.values()),
    ", ".join(
        f"{label} max_ratio={fmt(max(c['score_ratio'] for c in candidates), 12)}"
        for label, candidates in by_label.items()
    ),
)

print("\n(3) Consequence")
print("The phase diagram separates three finite regimes: locked hidden fibers are")
print("strongly order-visible, moderate/high jitter can camouflage at small N, and")
print("the same fixed jitter can reappear as an exact-pattern/rooted defect at")
print("larger N.  None of the tested fixed-jitter schedules proves full washout.")
print("The next mathematical target is a scaling theorem for Q_N(w, j_N) versus")
print("P_N, with the critical curve expressed in order-visible invariants.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
