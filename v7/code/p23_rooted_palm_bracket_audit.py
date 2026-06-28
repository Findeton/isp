#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: rooted/Palm bracket audit.

The previous adversarial-limit receipt showed that fixed-width hidden clusters
have unrooted pair mass O(1/N), while a typical rooted record still has O(1)
hidden partners.  This receipt tests the next projection directly: sample a
root record first, then audit the causal neighborhood, near-external-distance
tail, and intervals through the root.

The receipt is intentionally hostile to the rooted proposal.  It tests fixed
hidden widths, a larger width, and records when order-only rooted diagnostics
are useful but still incomplete.

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


def rooted_interval_stats(poset, root, rng, max_pairs=40):
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


def rooted_row(poset, root, rng):
    N = poset.N
    tau = max(2, N // 48)
    deltas = [external_delta(poset, root, y) for y in range(N) if y != root]
    deltas.sort()
    near_1 = sum(1 for d in deltas if d <= tau)
    near_2 = sum(1 for d in deltas if d <= 2 * tau)
    near_4 = sum(1 for d in deltas if d <= 4 * tau)
    soft_1 = sum(mp.e ** (-mp.mpf(d) / (tau + 1)) for d in deltas)
    soft_2 = sum(mp.e ** (-mp.mpf(d) / (2 * tau + 1)) for d in deltas)
    near_mask = 0
    for y in range(N):
        if y != root and external_delta(poset, root, y) <= 2 * tau:
            near_mask |= 1 << y
    intervals = rooted_interval_stats(poset, root, rng)
    return [
        mp.mpf(poset.past[root].bit_count()) / (N - 1),
        mp.mpf(poset.future[root].bit_count()) / (N - 1),
        mp.mpf((poset.past[root] | poset.future[root]).bit_count()) / (N - 1),
        mp.mpf(near_1) / N,
        mp.mpf(near_2) / N,
        mp.mpf(near_4) / N,
        soft_1 / N,
        soft_2 / N,
        mp.mpf(deltas[0]) / N,
        mp.mpf(sum(deltas[: min(4, len(deltas))])) / (N * min(4, len(deltas))),
        relation_fraction_on_mask(poset, near_mask),
        mp.mpf(near_mask.bit_count()) / N,
    ] + intervals


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


def rooted_palm_vector(poset, root_count, seed):
    rng = random.Random(seed)
    roots = rng.sample(range(poset.N), min(root_count, poset.N))
    rows = [rooted_row(poset, root, rng) for root in roots]
    means = mean_vector(rows)
    denom = max(1, len(rows) - 1)
    variances = [
        sum((row[i] - means[i]) ** 2 for row in rows) / denom
        for i in range(len(means))
    ]
    return list(global_feature_vector(poset)) + means + variances


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


def calibrate_rooted_action(N, train_seeds, heldout_seeds, root_count):
    rows = [
        rooted_palm_vector(sprinkled2_poset(N, seed), root_count, seed + 2100000)
        for seed in train_seeds
    ]
    mean = mean_vector(rows)
    cov = covariance_matrix(rows, mean)
    L = cholesky(cov)

    def score_poset(poset, seed):
        row = rooted_palm_vector(poset, root_count, seed)
        z = solve_lower(L, [row[i] - mean[i] for i in range(len(mean))])
        return sum(value * value for value in z)

    heldout = [
        score_poset(sprinkled2_poset(N, seed), seed + 2200000)
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


def same_cluster_pair_fraction(N, width):
    if N % width != 0:
        raise ValueError("N must be divisible by width")
    return mp.mpf(width - 1) / (N - 1)


def hidden_partner_root_mean(width):
    return mp.mpf(width - 1)


def same_label_delta_stats(poset, labels):
    tau = max(2, poset.N // 48)
    count = 0
    near_1 = 0
    near_2 = 0
    delta_sum = mp.mpf(0)
    for x in range(poset.N):
        for y in range(x + 1, poset.N):
            if labels[x] != labels[y]:
                continue
            count += 1
            delta = external_delta(poset, x, y)
            delta_sum += mp.mpf(delta) / poset.N
            if delta <= tau:
                near_1 += 1
            if delta <= 2 * tau:
                near_2 += 1
    if count == 0:
        return {
            "mean_delta": mp.mpf(0),
            "near_1_fraction": mp.mpf(0),
            "near_2_fraction": mp.mpf(0),
        }
    return {
        "mean_delta": delta_sum / count,
        "near_1_fraction": mp.mpf(near_1) / count,
        "near_2_fraction": mp.mpf(near_2) / count,
    }


print("=" * 80)
print("Collapsed P23 rooted/Palm bracket audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 384
root_count = 20
action = calibrate_rooted_action(
    N,
    train_seeds=list(range(910000, 910024)),
    heldout_seeds=list(range(920000, 920016)),
    root_count=root_count,
)
heldout = action["heldout"]
print("\n(1) Rooted/Palm held-out calibration")
print("dimension =", action["dimension"])
print("heldout =", [fmt(x, 12) for x in heldout])
print("heldout max =", fmt(heldout[-1], 18))
check(
    "Rooted/Palm held-out null is nondegenerate",
    heldout[-1] > heldout[0] and heldout[0] > 0,
    f"min={fmt(heldout[0], 16)}, max={fmt(heldout[-1], 16)}",
)

probe_scores = []
for i, seed in enumerate(range(930000, 930008)):
    score = action["score_poset"](sprinkled2_poset(N, seed), seed + 2300000)
    rank = rank_against_null(score, heldout)
    probe_scores.append(score)
    print(f"probe sprinkling {i}: score={fmt(score, 16)} rank={fmt(rank, 12)}")
probe_outside = sum(1 for score in probe_scores if score > heldout[-1])
check(
    "Rooted/Palm projection gives a bounded fresh-sprinkling rank audit",
    probe_outside <= 2,
    f"outside={probe_outside}/8",
)

print("\n(2) Width sweep adversaries")
width_results = []
for width, jitter, seed in [(2, 2, 16002), (4, 2, 16002), (8, 2, 16002), (16, 2, 16002)]:
    poset, labels = clustered_jittered_fiber_poset(N // width, width, seed, jitter, 1)
    score, rank = score_candidate(action, f"width={width} jitter={jitter}", poset, 940000 + width)
    gf = global_feature_vector(poset)
    pair_mass = same_cluster_pair_fraction(N, width)
    root_hidden = hidden_partner_root_mean(width)
    label_stats = same_label_delta_stats(poset, labels)
    width_results.append(
        {
            "width": width,
            "score": score,
            "rank": rank,
            "pair_mass": pair_mass,
            "root_hidden": root_hidden,
            "dmm": mm_inv(gf[0]),
            "height_ratio": gf[1],
            "theta": gf[2],
            "p_ratio": gf[3],
            "same_mean_delta": label_stats["mean_delta"],
            "same_near_1": label_stats["near_1_fraction"],
            "same_near_2": label_stats["near_2_fraction"],
        }
    )
    print(
        f"  globals: dMM={fmt(mm_inv(gf[0]), 18)} Hratio={fmt(gf[1], 18)} "
        f"Theta={fmt(gf[2], 18)} P={fmt(gf[3], 18)} "
        f"pair_mass={fmt(pair_mass, 18)} root_hidden={fmt(root_hidden, 18)} "
        f"same_delta_mean={fmt(label_stats['mean_delta'], 18)} "
        f"same_near_tau={fmt(label_stats['near_1_fraction'], 18)}"
    )

print("\n(3) Scaling summary")
for result in width_results:
    print(
        f"width={result['width']}: rank={fmt(result['rank'], 12)} "
        f"score/max={fmt(result['score'] / heldout[-1], 18)} "
        f"pair_mass={fmt(result['pair_mass'], 18)} "
        f"root_hidden={fmt(result['root_hidden'], 18)} "
        f"same_delta={fmt(result['same_mean_delta'], 18)} "
        f"same_near_tau={fmt(result['same_near_1'], 18)}"
    )

fixed_width = [r for r in width_results if r["width"] in {2, 4}]
large_width = [r for r in width_results if r["width"] in {8, 16}]
check(
    "Finite rooted/Palm action does not reject the jittered width sweep",
    all(r["score"] <= heldout[-1] for r in width_results),
    ", ".join(
        f"w={r['width']} rank={fmt(r['rank'], 12)} score/max={fmt(r['score'] / heldout[-1], 12)}"
        for r in width_results
    ),
)
check(
    "Fixed small hidden widths can remain inside the finite rooted/Palm null",
    any(r["score"] <= heldout[-1] for r in fixed_width),
    ", ".join(
        f"w={r['width']} rank={fmt(r['rank'], 12)} score/max={fmt(r['score'] / heldout[-1], 12)}"
        for r in fixed_width
    ),
)
check(
    "Jittered hidden labels are not the same as order-visible near twins",
    any(r["same_near_1"] < mp.mpf("0.25") and r["root_hidden"] >= 7 for r in width_results),
    ", ".join(
        f"w={r['width']} same_near_tau={fmt(r['same_near_1'], 12)} same_delta={fmt(r['same_mean_delta'], 12)}"
        for r in width_results
    ),
)
check(
    "Rooted hidden multiplicity grows while global pair mass can stay small",
    width_results[0]["pair_mass"] < mp.mpf("0.01")
    and width_results[0]["root_hidden"] == 1
    and width_results[2]["pair_mass"] < mp.mpf("0.02")
    and width_results[2]["root_hidden"] == 7,
    ", ".join(
        f"w={r['width']} pair_mass={fmt(r['pair_mass'], 12)} root_hidden={fmt(r['root_hidden'], 12)}"
        for r in width_results
    ),
)
check(
    "Rooted/Palm audit is necessary but not yet a complete click law",
    all(r["score"] <= heldout[-1] for r in width_results)
    and any(r["same_near_1"] < mp.mpf("0.25") for r in large_width),
    "the tested rooted score does not reject the jittered width sweep",
)

print("\n(4) Consequence")
print("This finite rooted/Palm projection is stable on fresh sprinklings, but it")
print("does not reject the tested jittered width sweep.  Jitter can make hidden")
print("construction labels cease to look like order-visible near twins.")
print("The next target is therefore not just rooted features; it is a rooted")
print("process-level law that distinguishes order-visible hidden multiplicity from")
print("labels that have washed out into an ordinary clustered point process.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
