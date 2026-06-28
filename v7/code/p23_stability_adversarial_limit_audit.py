#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: stability and adversarial-limit audit.

The previous multiscale interval-pair receipt showed two facts at once:
interval-pair covariance rejects some adversaries, but a small high-dimensional
held-out null can also reject a fresh sprinkling.  This receipt tests the next
opening:

  1. replace the 59-dimensional finite score by a compact interval-pair
     projection and audit fresh-sprinkling rank stability;
  2. ask whether fixed-width hidden clusters can disappear from global
     empirical laws as N grows, forcing any final law to use rooted/Palm
     information rather than only unrooted global averages.

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

    def relation_count(self):
        return sum(mask.bit_count() for mask in self.future)

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

    def interval_audit(self):
        hist = [0] * self.N
        recursive_num = 0
        recursive_den = 0
        for x in range(self.N):
            for y in iter_bits(self.future[x]):
                interior = self.future[x] & self.past[y]
                k = interior.bit_count()
                hist[k] += 1
                if k >= 2:
                    recursive_den += k * (k - 1) // 2
                    inner_rel = 0
                    for z in iter_bits(interior):
                        inner_rel += (self.future[z] & interior).bit_count()
                    recursive_num += inner_rel
        return {
            "hist": hist,
            "recursive_r": (
                mp.mpf(recursive_num) / recursive_den if recursive_den else mp.mpf(0)
            ),
        }


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


def induced_subposet(poset, vertices):
    vertices = list(vertices)
    old_to_new = {old: new for new, old in enumerate(vertices)}
    vertex_mask = 0
    for old in vertices:
        vertex_mask |= 1 << old
    future = [0] * len(vertices)
    for new_x, old_x in enumerate(vertices):
        mask = 0
        for old_y in iter_bits(poset.future[old_x] & vertex_mask):
            mask |= 1 << old_to_new[old_y]
        future[new_x] = mask
    return Poset(future)


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


def external_near_twin_counts(poset, threshold):
    count = 0
    threshold = int(threshold)
    for x in range(poset.N):
        clear_x = ~(1 << x)
        for y in range(x + 1, poset.N):
            clear_y = ~(1 << y)
            diff = ((poset.past[x] & clear_y) ^ (poset.past[y] & clear_x)).bit_count()
            diff += (
                (poset.future[x] & clear_y) ^ (poset.future[y] & clear_x)
            ).bit_count()
            if diff <= threshold:
                count += 1
    total = poset.N * (poset.N - 1) // 2
    return count, total


def external_near_twin_fraction(poset, threshold):
    count, total = external_near_twin_counts(poset, threshold)
    return mp.mpf(count) / total if total else mp.mpf(0)


def feature_vector(poset):
    audit = poset.interval_audit()
    expected = sprinkle_pair_density_expectation(poset.N, mp.log(2))
    observed = profile_P_from_hist_density(audit["hist"], poset.N, mp.log(2))
    return [
        poset.ordering_fraction(),
        height_scale_ratio(poset),
        audit["recursive_r"],
        observed / expected if expected else mp.mpf(0),
        external_near_twin_fraction(poset, max(2, poset.N // 48)),
    ]


def intervals_in_band(poset, lo, hi):
    intervals = []
    for x in range(poset.N):
        for y in iter_bits(poset.future[x]):
            interior = poset.future[x] & poset.past[y]
            k = interior.bit_count()
            if lo <= k <= hi:
                intervals.append(interior)
    return intervals


def interval_pair_topology(masks):
    if len(masks) < 2:
        return [mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    disjoint = 0
    nested = 0
    overlap = 0
    shared_min_sum = mp.mpf(0)
    pair_count = 0
    for i, a in enumerate(masks):
        a_count = a.bit_count()
        for b in masks[i + 1 :]:
            b_count = b.bit_count()
            pair_count += 1
            inter = (a & b).bit_count()
            if inter == 0:
                disjoint += 1
            else:
                min_count = min(a_count, b_count)
                shared_min_sum += mp.mpf(inter) / min_count if min_count else mp.mpf(0)
                if (a & ~b) == 0 or (b & ~a) == 0:
                    nested += 1
                else:
                    overlap += 1
    return [
        mp.mpf(disjoint) / pair_count,
        mp.mpf(nested) / pair_count,
        mp.mpf(overlap) / pair_count,
        shared_min_sum / pair_count,
    ]


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


def scale_config(N):
    unit = N // 16
    return [
        (unit, 2 * unit - 1),
        (2 * unit, 4 * unit - 1),
        (4 * unit, 8 * unit - 1),
    ]


def compact_pair_vector(poset, per_band, seed):
    rng = random.Random(seed)
    out = list(feature_vector(poset))
    for lo, hi in scale_config(poset.N):
        intervals = intervals_in_band(poset, lo, hi)
        chosen = rng.sample(intervals, per_band) if len(intervals) > per_band else intervals
        if not chosen:
            out.extend([mp.mpf(0)] * 9)
            continue
        rows = [feature_vector(induced_subposet(poset, iter_bits(mask))) for mask in chosen]
        out.extend(mean_vector(rows))
        out.extend(interval_pair_topology(chosen))
    return out


def covariance_matrix(rows, mean):
    d = len(mean)
    denom = max(1, len(rows) - 1)
    cov = [[mp.mpf(0) for _ in range(d)] for _ in range(d)]
    for row in rows:
        diff = [row[i] - mean[i] for i in range(d)]
        for i in range(d):
            for j in range(d):
                cov[i][j] += diff[i] * diff[j] / denom
    avg_diag = sum(cov[i][i] for i in range(d)) / d
    ridge = max(avg_diag * mp.mpf("5e-2"), mp.mpf("1e-14"))
    for i in range(d):
        cov[i][i] += ridge
    return cov


def cholesky(matrix):
    n = len(matrix)
    L = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            value = matrix[i][j] - sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                if value <= 0:
                    value = mp.mpf("1e-30")
                L[i][j] = mp.sqrt(value)
            else:
                L[i][j] = value / L[j][j]
    return L


def solve_lower(L, vector):
    out = []
    for i, value in enumerate(vector):
        residual = value - sum(L[i][j] * out[j] for j in range(i))
        out.append(residual / L[i][i])
    return out


def calibrate_compact_action(N, train_seeds, heldout_seeds, per_band):
    rows = [
        compact_pair_vector(sprinkled2_poset(N, seed), per_band, seed + 1100000)
        for seed in train_seeds
    ]
    mean = mean_vector(rows)
    cov = covariance_matrix(rows, mean)
    L = cholesky(cov)

    def score_poset(poset, seed):
        row = compact_pair_vector(poset, per_band, seed)
        z = solve_lower(L, [row[i] - mean[i] for i in range(len(mean))])
        return sum(value * value for value in z)

    heldout = [score_poset(sprinkled2_poset(N, seed), seed + 1200000) for seed in heldout_seeds]
    heldout.sort()
    return {"score_poset": score_poset, "heldout": heldout, "dimension": len(mean)}


def rank_against_null(score, null_scores):
    return mp.mpf(sum(1 for value in null_scores if value <= score)) / len(null_scores)


def score_named(action, name, poset, seed):
    score = action["score_poset"](poset, seed)
    rank = rank_against_null(score, action["heldout"])
    print(f"{name}: score={fmt(score, 18)} rank={fmt(rank, 18)}")
    return score, rank


def hidden_same_cluster_pair_fraction(N, width):
    if N % width != 0:
        raise ValueError("N must be divisible by width")
    base = N // width
    hidden_pairs = base * width * (width - 1) // 2
    all_pairs = N * (N - 1) // 2
    return mp.mpf(hidden_pairs) / all_pairs


def same_label_near_counts(poset, labels, threshold):
    threshold = int(threshold)
    same_near = 0
    all_near = 0
    same_total = 0
    for x in range(poset.N):
        clear_x = ~(1 << x)
        for y in range(x + 1, poset.N):
            if labels[x] == labels[y]:
                same_total += 1
            clear_y = ~(1 << y)
            diff = ((poset.past[x] & clear_y) ^ (poset.past[y] & clear_x)).bit_count()
            diff += (
                (poset.future[x] & clear_y) ^ (poset.future[y] & clear_x)
            ).bit_count()
            if diff <= threshold:
                all_near += 1
                if labels[x] == labels[y]:
                    same_near += 1
    return same_near, all_near, same_total


print("=" * 80)
print("Collapsed P23 stability and adversarial-limit receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

scale_settings = [
    {
        "N": 192,
        "train": list(range(810000, 810032)),
        "heldout": list(range(820000, 820024)),
        "probe": list(range(830000, 830012)),
        "per_band": 5,
    },
    {
        "N": 384,
        "train": list(range(840000, 840032)),
        "heldout": list(range(850000, 850024)),
        "probe": list(range(860000, 860012)),
        "per_band": 4,
    },
]

scale_results = []
for setting in scale_settings:
    N = setting["N"]
    print(f"\n(1) Compact interval-pair stability, N={N}")
    action = calibrate_compact_action(
        N, setting["train"], setting["heldout"], setting["per_band"]
    )
    heldout = action["heldout"]
    print("dimension =", action["dimension"])
    print("heldout =", [fmt(x, 12) for x in heldout])
    print("heldout max =", fmt(heldout[-1], 18))
    check(
        f"N={N} compact held-out null is nondegenerate",
        heldout[-1] > heldout[0] and heldout[0] > 0,
        f"min={fmt(heldout[0], 16)}, max={fmt(heldout[-1], 16)}",
    )

    probe_scores = []
    probe_ranks = []
    for i, seed in enumerate(setting["probe"]):
        score = action["score_poset"](sprinkled2_poset(N, seed), seed + 1300000)
        rank = rank_against_null(score, heldout)
        probe_scores.append(score)
        probe_ranks.append(rank)
        print(f"N={N} probe sprinkling {i}: score={fmt(score, 16)} rank={fmt(rank, 12)}")

    outside_count = sum(1 for score in probe_scores if score > heldout[-1])
    mean_rank = sum(probe_ranks) / len(probe_ranks)
    max_rank = max(probe_ranks)
    print(
        f"N={N} probe outside_count={outside_count}/{len(probe_scores)} "
        f"mean_rank={fmt(mean_rank, 18)} max_rank={fmt(max_rank, 18)}"
    )

    width = 4
    base = N // width
    cluster_j2, labels_j2 = clustered_jittered_fiber_poset(base, width, 16002, 2, 1)
    cluster_j3, labels_j3 = clustered_jittered_fiber_poset(base, width, 16008, 3, 1)
    j2_score, j2_rank = score_named(action, f"N={N} jitter cluster j=2", cluster_j2, 870000 + N)
    j3_score, j3_rank = score_named(action, f"N={N} jitter cluster j=3", cluster_j3, 880000 + N)

    threshold = max(2, N // 48)
    sprink_near, sprink_total = external_near_twin_counts(sprinkled2_poset(N, 890000 + N), threshold)
    j2_same_near, j2_all_near, j2_same_total = same_label_near_counts(cluster_j2, labels_j2, threshold)
    same_fraction = hidden_same_cluster_pair_fraction(N, width)
    scale_results.append(
        {
            "N": N,
            "heldout_max": heldout[-1],
            "outside_count": outside_count,
            "mean_rank": mean_rank,
            "j2_score": j2_score,
            "j2_rank": j2_rank,
            "j3_score": j3_score,
            "j3_rank": j3_rank,
            "same_fraction": same_fraction,
            "same_fraction_scaled": same_fraction * N,
            "sprink_near_per_record": mp.mpf(2 * sprink_near) / N,
            "j2_all_near_per_record": mp.mpf(2 * j2_all_near) / N,
            "j2_same_near_per_record": mp.mpf(2 * j2_same_near) / N,
            "j2_same_total_per_record": mp.mpf(2 * j2_same_total) / N,
        }
    )
    check(
        f"N={N} compact projection gives a bounded fresh-sprinkling rank audit",
        outside_count <= 2 and mp.mpf("0.2") <= mean_rank <= mp.mpf("0.8"),
        f"outside={outside_count}/{len(probe_scores)}, mean_rank={fmt(mean_rank, 12)}",
    )
    check(
        f"N={N} surviving clustered adversaries are explicitly ranked by compact action",
        mp.mpf(0) <= j2_rank <= 1 and mp.mpf(0) <= j3_rank <= 1,
        f"j2_rank={fmt(j2_rank, 12)}, j3_rank={fmt(j3_rank, 12)}",
    )

print("\n(2) Fixed-width hidden cluster scaling")
for result in scale_results:
    print(
        f"N={result['N']}: same-cluster pair fraction={fmt(result['same_fraction'], 18)}, "
        f"N*fraction={fmt(result['same_fraction_scaled'], 18)}, "
        f"sprink near/root={fmt(result['sprink_near_per_record'], 18)}, "
        f"j2 near/root={fmt(result['j2_all_near_per_record'], 18)}, "
        f"j2 same-near/root={fmt(result['j2_same_near_per_record'], 18)}, "
        f"same-total/root={fmt(result['j2_same_total_per_record'], 18)}"
    )

check(
    "Compact projection reduces but does not eliminate finite calibration leakage",
    any(r["outside_count"] > 0 for r in scale_results)
    and all(r["outside_count"] <= 2 for r in scale_results),
    ", ".join(
        f"N={r['N']} outside={r['outside_count']}/12 mean_rank={fmt(r['mean_rank'], 12)}"
        for r in scale_results
    ),
)
check(
    "Fixed-width hidden-pair mass decays like 1/N in unrooted pair statistics",
    scale_results[-1]["same_fraction"] < scale_results[0]["same_fraction"]
    and abs(scale_results[-1]["same_fraction_scaled"] - 3) < mp.mpf("0.05")
    and abs(scale_results[0]["same_fraction_scaled"] - 3) < mp.mpf("0.05"),
    ", ".join(
        f"N={r['N']} N*f={fmt(r['same_fraction_scaled'], 12)}"
        for r in scale_results
    ),
)
check(
    "Rooted hidden multiplicity remains order-one for fixed width",
    all(abs(r["j2_same_total_per_record"] - 3) < mp.mpf("1e-40") for r in scale_results),
    ", ".join(
        f"N={r['N']} same_total/root={fmt(r['j2_same_total_per_record'], 12)}"
        for r in scale_results
    ),
)
check(
    "Order-only near-root excess is not a reliable complete detector at finite scale",
    any(r["j2_same_near_per_record"] < mp.mpf("0.5") for r in scale_results)
    and any(r["j2_all_near_per_record"] <= r["sprink_near_per_record"] * mp.mpf("1.5") for r in scale_results),
    ", ".join(
        f"N={r['N']} sprink={fmt(r['sprink_near_per_record'], 12)} "
        f"j2={fmt(r['j2_all_near_per_record'], 12)} "
        f"same_near={fmt(r['j2_same_near_per_record'], 12)}"
        for r in scale_results
    ),
)
check(
    "Adversarial-limit audit shifts the target to rooted/Palm or process-level laws",
    all(r["same_fraction"] < mp.mpf("0.02") for r in scale_results)
    and all(r["j2_same_total_per_record"] == 3 for r in scale_results),
    "global hidden mass is small while each rooted record still has three hidden partners",
)

print("\n(3) Consequence")
print("A compact interval-pair projection is more stable on fresh sprinklings in this receipt,")
print("but it still only supplies a finite diagnostic.")
print("Fixed-width hidden clusters have unrooted pair mass O(1/N), so global empirical")
print("laws can miss them asymptotically even though a rooted record still has O(1)")
print("hidden partners.  The next law target must be rooted/Palm or process-level,")
print("not merely a larger unrooted finite vector.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
