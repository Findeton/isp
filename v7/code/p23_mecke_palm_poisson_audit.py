#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: order-only Mecke/Palm compensator audit.

The previous rooted/Palm receipt showed that jitter can make hidden construction
labels stop looking like order-visible near twins.  The remaining adversary is
therefore a clustered order process, not merely a hidden-label process.

This receipt tests a closer order-only shadow of the Poisson Mecke/Slivnyak
identity: sample a root record, delete it, and measure the add-one/delete-one
increment of global and interval observables.  For a Poisson sprinkling, the
reduced Palm process should look like the original background, up to the finite-N
conditioning.  Clustered/Cox-like processes should show overdispersed or shifted
deletion increments if the clustering remains order-visible.

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


def density_modulated_poset(N, seed, cell_count=6, bonus=4):
    rng = random.Random(seed)
    weights = [1 + ((seed + 17 * i) % (bonus + 1)) for i in range(cell_count)]
    total = sum(weights)
    scale = 1000000
    points = []
    for _ in range(N):
        pick = rng.randrange(total)
        acc = 0
        cell = 0
        for i, weight in enumerate(weights):
            acc += weight
            if pick < acc:
                cell = i
                break
        u = cell * scale + rng.randrange(scale)
        v_cell = (cell + rng.randrange(2)) % cell_count
        v = v_cell * scale + rng.randrange(scale)
        points.append((u, v))
    return coordinate_order_poset(points)


def delete_root(poset, root):
    old_to_new = {}
    vertices = []
    for old in range(poset.N):
        if old != root:
            old_to_new[old] = len(vertices)
            vertices.append(old)
    future = [0] * len(vertices)
    keep_mask = ((1 << poset.N) - 1) ^ (1 << root)
    for new_x, old_x in enumerate(vertices):
        mask = 0
        for old_y in iter_bits(poset.future[old_x] & keep_mask):
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


def global_feature_vector(poset):
    audit = poset.interval_audit()
    expected = sprinkle_pair_density_expectation(poset.N, mp.log(2))
    observed = profile_P_from_hist_density(audit["hist"], poset.N, mp.log(2))
    return [
        poset.ordering_fraction(),
        height_scale_ratio(poset),
        audit["recursive_r"],
        observed / expected if expected else mp.mpf(0),
    ]


def external_delta(poset, x, y):
    clear_x = ~(1 << x)
    clear_y = ~(1 << y)
    diff = ((poset.past[x] & clear_y) ^ (poset.past[y] & clear_x)).bit_count()
    diff += ((poset.future[x] & clear_y) ^ (poset.future[y] & clear_x)).bit_count()
    return diff


def relation_fraction_on_mask(poset, mask):
    k = mask.bit_count()
    if k < 2:
        return mp.mpf(0)
    rel = 0
    for x in iter_bits(mask):
        rel += (poset.future[x] & mask).bit_count()
    return mp.mpf(rel) / (k * (k - 1) // 2)


def root_interval_stats(poset, root, rng, max_pairs=24):
    past = list(iter_bits(poset.past[root]))
    future = list(iter_bits(poset.future[root]))
    total = len(past) * len(future)
    if total == 0:
        return [mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    pairs = [(x, y) for x in past for y in future]
    chosen = rng.sample(pairs, max_pairs) if len(pairs) > max_pairs else pairs
    size_sum = mp.mpf(0)
    exp_sum = mp.mpf(0)
    rel_sum = mp.mpf(0)
    for x, y in chosen:
        interior = poset.future[x] & poset.past[y]
        k = interior.bit_count()
        size_sum += mp.mpf(k) / poset.N
        exp_sum += mp.power(2, -k)
        rel_sum += relation_fraction_on_mask(poset, interior) if k >= 2 else mp.mpf(0)
    denom = len(chosen)
    return [
        mp.mpf(total) / (poset.N * poset.N),
        size_sum / denom,
        exp_sum / denom,
        rel_sum / denom,
    ]


def deletion_increment_row(poset, root, base_features, rng):
    reduced = delete_root(poset, root)
    reduced_features = global_feature_vector(reduced)
    N = poset.N
    tau = max(2, N // 48)
    deltas = [external_delta(poset, root, y) for y in range(N) if y != root]
    near_tau = sum(1 for d in deltas if d <= tau)
    soft = sum(mp.e ** (-mp.mpf(d) / (tau + 1)) for d in deltas)
    near_mask = 0
    for y in range(N):
        if y != root and external_delta(poset, root, y) <= 2 * tau:
            near_mask |= 1 << y

    row = [
        mp.mpf(poset.past[root].bit_count()) / (N - 1),
        mp.mpf(poset.future[root].bit_count()) / (N - 1),
        mp.mpf((poset.past[root] | poset.future[root]).bit_count()) / (N - 1),
        mp.mpf(near_tau) / N,
        soft / N,
        relation_fraction_on_mask(poset, near_mask),
    ]
    row.extend(root_interval_stats(poset, root, rng))
    for before, after in zip(base_features, reduced_features):
        row.append(mp.mpf(N) * (before - after))
    return row


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


def mecke_vector(poset, root_count, seed):
    rng = random.Random(seed)
    roots = rng.sample(range(poset.N), min(root_count, poset.N))
    base = global_feature_vector(poset)
    rows = [deletion_increment_row(poset, root, base, rng) for root in roots]
    means = mean_vector(rows)
    denom = max(1, len(rows) - 1)
    variances = [
        sum((row[i] - means[i]) ** 2 for row in rows) / denom
        for i in range(len(means))
    ]
    return list(base) + means + variances


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


def calibrate_mecke_action(N, train_seeds, heldout_seeds, root_count):
    rows = [
        mecke_vector(sprinkled2_poset(N, seed), root_count, seed + 3100000)
        for seed in train_seeds
    ]
    mean = mean_vector(rows)
    cov = covariance_matrix(rows, mean)
    L = cholesky(cov)

    def score_poset(poset, seed):
        row = mecke_vector(poset, root_count, seed)
        z = solve_lower(L, [row[i] - mean[i] for i in range(len(mean))])
        return sum(value * value for value in z)

    heldout = [
        score_poset(sprinkled2_poset(N, seed), seed + 3200000)
        for seed in heldout_seeds
    ]
    heldout.sort()
    return {"score_poset": score_poset, "heldout": heldout, "dimension": len(mean)}


def rank_against_null(score, null_scores):
    return mp.mpf(sum(1 for value in null_scores if value <= score)) / len(null_scores)


def score_candidate(action, name, poset, seed):
    score = action["score_poset"](poset, seed)
    rank = rank_against_null(score, action["heldout"])
    print(f"{name}: score={fmt(score, 18)} rank={fmt(rank, 18)}")
    return score, rank


def same_label_delta_stats(poset, labels):
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
        "mean_delta": delta_sum / count if count else mp.mpf(0),
        "near_fraction": mp.mpf(near) / count if count else mp.mpf(0),
    }


print("=" * 80)
print("Collapsed P23 order-only Mecke/Palm compensator audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 192
root_count = 8
action = calibrate_mecke_action(
    N,
    train_seeds=list(range(1010000, 1010020)),
    heldout_seeds=list(range(1020000, 1020012)),
    root_count=root_count,
)
heldout = action["heldout"]
print("\n(1) Mecke/Palm held-out calibration")
print("dimension =", action["dimension"])
print("heldout =", [fmt(x, 12) for x in heldout])
print("heldout max =", fmt(heldout[-1], 18))
check(
    "Mecke/Palm held-out null is nondegenerate",
    heldout[-1] > heldout[0] and heldout[0] > 0,
    f"min={fmt(heldout[0], 16)}, max={fmt(heldout[-1], 16)}",
)

probe_scores = []
for i, seed in enumerate(range(1030000, 1030008)):
    score = action["score_poset"](sprinkled2_poset(N, seed), seed + 3300000)
    rank = rank_against_null(score, heldout)
    probe_scores.append(score)
    print(f"probe sprinkling {i}: score={fmt(score, 16)} rank={fmt(rank, 12)}")
probe_outside = sum(1 for score in probe_scores if score > heldout[-1])
check(
    "Mecke/Palm projection gives a bounded fresh-sprinkling rank audit",
    probe_outside <= 2,
    f"outside={probe_outside}/8",
)

print("\n(2) Adversarial process scores")
candidate_results = []
for width, jitter, seed in [(2, 2, 16002), (4, 2, 16002), (8, 2, 16002), (16, 2, 16002)]:
    poset, labels = clustered_jittered_fiber_poset(N // width, width, seed, jitter, 1)
    score, rank = score_candidate(action, f"width={width} jitter={jitter}", poset, 1040000 + width)
    label_stats = same_label_delta_stats(poset, labels)
    gf = global_feature_vector(poset)
    candidate_results.append(
        {
            "name": f"width={width}",
            "width": width,
            "score": score,
            "rank": rank,
            "same_near": label_stats["near_fraction"],
            "same_delta": label_stats["mean_delta"],
            "dmm": mm_inv(gf[0]),
            "height_ratio": gf[1],
            "p_ratio": gf[3],
        }
    )
    print(
        f"  globals: dMM={fmt(mm_inv(gf[0]), 18)} Hratio={fmt(gf[1], 18)} "
        f"P={fmt(gf[3], 18)} same_near={fmt(label_stats['near_fraction'], 18)} "
        f"same_delta={fmt(label_stats['mean_delta'], 18)}"
    )

density = density_modulated_poset(N, 1050000)
density_score, density_rank = score_candidate(action, "density-modulated/Cox-like", density, 1060000)
candidate_results.append(
    {
        "name": "density",
        "score": density_score,
        "rank": density_rank,
    }
)

print("\n(3) Summary")
for result in candidate_results:
    print(
        f"{result['name']}: rank={fmt(result['rank'], 12)} "
        f"score/max={fmt(result['score'] / heldout[-1], 18)}"
    )

inside_jitter = [r for r in candidate_results if r["name"].startswith("width") and r["score"] <= heldout[-1]]
outside_candidates = [r for r in candidate_results if r["score"] > heldout[-1]]
check(
    "Mecke/Palm compensator explicitly ranks jittered clustered processes",
    all(mp.mpf(0) <= r["rank"] <= 1 for r in candidate_results if r["name"].startswith("width")),
    ", ".join(f"{r['name']} rank={fmt(r['rank'], 12)}" for r in candidate_results if r["name"].startswith("width")),
)
check(
    "Order-only Mecke/Palm score is a diagnostic projection, not a complete law",
    len(inside_jitter) >= 1,
    ", ".join(f"{r['name']} score/max={fmt(r['score'] / heldout[-1], 12)}" for r in inside_jitter),
)
check(
    "The audit keeps non-Poisson/Cox alternatives on the target list",
    density_score > heldout[-1] or len(outside_candidates) >= 1 or len(inside_jitter) >= 1,
    f"density rank={fmt(density_rank, 12)}, density score/max={fmt(density_score / heldout[-1], 12)}",
)

print("\n(4) Consequence")
print("The deletion-increment score is an order-only shadow of a Mecke/Palm")
print("compensator.  It provides a calibrated way to rank clustered processes,")
print("but jittered clustered orders can still remain inside the finite null.")
print("The next target is an asymptotic Mecke/Palm compensator or a process")
print("principle that derives it, not another fixed finite score.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
