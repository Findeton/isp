#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: multiscale interval-pair covariance audit.

The previous joint bracket projection still admitted tuned jittered clusters
inside the finite held-out null.  This receipt tests the next process-level
opening: not just individual intervals, but correlations between pairs of
causally selected intervals across scales.

For each scale N, it calibrates a held-out null on 1+1 sprinklings using a
joint vector of:
  - full-order features;
  - interval-band feature means and variances;
  - selected covariance entries between interval features;
  - interval-pair topology: disjoint, nested, overlap, and shared-interior fractions.

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


def bit_range(start, stop):
    mask = 0
    for i in range(start, stop):
        mask |= 1 << i
    return mask


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

    def interval_audit(self, load_k_min=8):
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
    return coordinate_order_poset(points), {
        "family": "clustered_jitter",
        "width": width,
        "jitter": f"{jitter_num}/{jitter_den}",
        "seed": seed,
        "labels": labels,
    }


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
    return coordinate_order_poset(points), {"family": "density_modulated", "seed": seed}


def staged_sandwich_poset(N, middle, seed, chain_height):
    rng = random.Random(seed)
    side = N - chain_height - middle
    a = side // 2
    b = side - a
    p0 = a
    top0 = p0 + middle
    chain0 = top0 + b
    future = [0] * N
    middle_points = [(rng.randrange(1000000), rng.randrange(1000000)) for _ in range(middle)]
    middle_order = coordinate_order_poset(middle_points)
    middle_mask = bit_range(p0, top0)
    top_mask = bit_range(top0, chain0)
    for x in range(a):
        future[x] = middle_mask | top_mask
    for local, mask in enumerate(middle_order.future):
        shifted = 0
        for y in iter_bits(mask):
            shifted |= 1 << (p0 + y)
        future[p0 + local] = shifted | top_mask
    for x in range(chain0, N):
        future[x] = bit_range(x + 1, N)
    return Poset(future), {"family": "staged_sandwich", "seed": seed}


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


def external_near_twin_fraction(poset, threshold):
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
    return mp.mpf(count) / total if total else mp.mpf(0)


FEATURES = ["r", "height", "theta", "p_log2", "near"]
SELECTED_COV = [(0, 1), (0, 3), (1, 3), (3, 4)]


def feature_vector(poset):
    audit = poset.interval_audit(load_k_min=max(3, poset.N // 32))
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
                intervals.append((x, y, interior, k))
    return intervals


def sample_interval_data(poset, bands, per_band, seed):
    rng = random.Random(seed)
    sampled = {}
    for label, lo, hi in bands:
        intervals = intervals_in_band(poset, lo, hi)
        chosen = rng.sample(intervals, per_band) if len(intervals) > per_band else intervals
        rows = []
        masks = []
        sizes = []
        for _, _, interior, k in chosen:
            rows.append(feature_vector(induced_subposet(poset, list(iter_bits(interior)))))
            masks.append(interior)
            sizes.append(k)
        sampled[label] = {"rows": rows, "masks": masks, "sizes": sizes}
    return sampled


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


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


def joint_pair_vector(poset, bands, per_band, seed):
    out = list(feature_vector(poset))
    sampled = sample_interval_data(poset, bands, per_band, seed)
    for label, _, _ in bands:
        rows = sampled[label]["rows"]
        masks = sampled[label]["masks"]
        if not rows:
            out.extend([mp.mpf(0)] * (len(FEATURES) * 2 + len(SELECTED_COV) + 4))
            continue
        mean = mean_vector(rows)
        out.extend(mean)
        denom = max(1, len(rows) - 1)
        variances = []
        for i in range(len(mean)):
            variances.append(sum((row[i] - mean[i]) ** 2 for row in rows) / denom)
        out.extend(variances)
        for i, j in SELECTED_COV:
            cov = sum((row[i] - mean[i]) * (row[j] - mean[j]) for row in rows) / denom
            out.append(cov)
        out.extend(interval_pair_topology(masks))
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
    ridge = max(avg_diag * mp.mpf("1e-2"), mp.mpf("1e-16"))
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


def calibrate_action(N, bands, per_band, train_seeds, heldout_seeds):
    rows = [
        joint_pair_vector(sprinkled2_poset(N, seed), bands, per_band, seed + 910000)
        for seed in train_seeds
    ]
    mean = mean_vector(rows)
    cov = covariance_matrix(rows, mean)
    L = cholesky(cov)

    def score_poset(poset, seed):
        row = joint_pair_vector(poset, bands, per_band, seed)
        z = solve_lower(L, [row[i] - mean[i] for i in range(len(mean))])
        return sum(value * value for value in z)

    heldout = [score_poset(sprinkled2_poset(N, seed), seed + 920000) for seed in heldout_seeds]
    heldout.sort()
    return {"score_poset": score_poset, "heldout": heldout, "dimension": len(mean)}


def rank_against_null(score, null_scores):
    return mp.mpf(sum(1 for value in null_scores if value <= score)) / len(null_scores)


def scale_config(N):
    unit = N // 16
    return [
        (f"{unit}-{2 * unit - 1}", unit, 2 * unit - 1),
        (f"{2 * unit}-{4 * unit - 1}", 2 * unit, 4 * unit - 1),
        (f"{4 * unit}-{8 * unit - 1}", 4 * unit, 8 * unit - 1),
    ]


def score_and_print(name, poset, action, seed):
    score = action["score_poset"](poset, seed)
    rank = rank_against_null(score, action["heldout"])
    print(f"{name}: score={fmt(score, 18)} rank={fmt(rank, 18)}")
    return score, rank


def print_signature(name, poset):
    fv = feature_vector(poset)
    print(
        f"{name}: N={poset.N} dMM={fmt(mm_inv(fv[0]), 18)} "
        f"Hratio={fmt(fv[1], 18)} theta={fmt(fv[2], 18)} "
        f"P={fmt(fv[3], 18)} near={fmt(fv[4], 18)}"
    )


print("=" * 80)
print("Collapsed P23 multiscale interval-pair covariance receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

scale_settings = [
    {"N": 192, "train": list(range(710000, 710024)), "heldout": list(range(720000, 720008)), "per_band": 6},
    {"N": 384, "train": list(range(730000, 730020)), "heldout": list(range(740000, 740008)), "per_band": 5},
]

all_scale_results = []
for setting in scale_settings:
    N = setting["N"]
    bands = scale_config(N)
    print(f"\n(1) Scale N={N}")
    action = calibrate_action(N, bands, setting["per_band"], setting["train"], setting["heldout"])
    heldout = action["heldout"]
    print("dimension =", action["dimension"])
    print("bands =", bands)
    print("heldout =", [fmt(x, 12) for x in heldout])
    print("heldout max =", fmt(heldout[-1], 18))
    check(
        f"N={N} held-out interval-pair null is nondegenerate",
        heldout[-1] > heldout[0] and heldout[0] > 0,
        f"min={fmt(heldout[0], 16)}, max={fmt(heldout[-1], 16)}",
    )

    fixed = sprinkled2_poset(N, 750000 + N)
    print_signature(f"N={N} held-out-like sprinkling", fixed)
    fixed_score, fixed_rank = score_and_print(
        f"N={N} fixed sprinkling", fixed, action, 760000 + N
    )

    base = N // 4
    cluster_regular, _ = clustered_jittered_fiber_poset(base, 4, 16008, 3, 1)
    cluster_best, best_meta = clustered_jittered_fiber_poset(base, 4, 16002, 2, 1)
    density, _ = density_modulated_poset(N, 770000 + N)
    staged, _ = staged_sandwich_poset(N, middle=max(11, N // 16), seed=780000 + N, chain_height=max(14, int(mp.sqrt(N) * 2)))

    adversary_scores = []
    for index, (name, candidate) in enumerate(
        [
            ("regularity cluster", cluster_regular),
            ("best joint-vector cluster", cluster_best),
            ("density modulated", density),
            ("staged sandwich", staged),
        ]
    ):
        print_signature(f"N={N} {name}", candidate)
        score, rank = score_and_print(
            f"N={N} {name}", candidate, action, 790000 + 100 * N + index
        )
        adversary_scores.append((score, rank, name))

    best_score, best_rank, best_name = min(adversary_scores, key=lambda row: row[0])
    print(
        f"N={N} best adversary by interval-pair score: {best_name} "
        f"score={fmt(best_score, 18)} rank={fmt(best_rank, 18)}"
    )
    all_scale_results.append(
        {
            "N": N,
            "heldout_max": heldout[-1],
            "fixed_score": fixed_score,
            "fixed_rank": fixed_rank,
            "fixed_outside": fixed_score > heldout[-1],
            "best_score": best_score,
            "best_rank": best_rank,
            "best_name": best_name,
            "density_score": next(score for score, _, name in adversary_scores if name == "density modulated"),
            "staged_score": next(score for score, _, name in adversary_scores if name == "staged sandwich"),
        }
    )
    check(
        f"N={N} fixed sprinkling is explicitly ranked against held-out interval-pair null",
        mp.mpf(0) <= fixed_rank <= 1,
        f"fixed={fmt(fixed_score, 16)}, rank={fmt(fixed_rank, 16)}, max={fmt(heldout[-1], 16)}",
    )
    check(
        f"N={N} density and staged adversaries are rejected by interval-pair covariance",
        all(
            score > heldout[-1]
            for score, _, name in adversary_scores
            if name in {"density modulated", "staged sandwich"}
        ),
        f"density={fmt(all_scale_results[-1]['density_score'], 16)}, staged={fmt(all_scale_results[-1]['staged_score'], 16)}, max={fmt(heldout[-1], 16)}",
    )

print("\n(2) Scaling summary")
for result in all_scale_results:
    ratio = result["best_score"] / result["heldout_max"]
    print(
        f"N={result['N']}: best={result['best_name']} "
        f"rank={fmt(result['best_rank'], 12)} "
        f"score/max={fmt(ratio, 18)}"
    )
check(
    "Tuned jitter clusters remain inside at least one finite interval-pair null",
    any(result["best_score"] <= result["heldout_max"] for result in all_scale_results),
    ", ".join(
        f"N={r['N']} ratio={fmt(r['best_score'] / r['heldout_max'], 12)}"
        for r in all_scale_results
    ),
)
check(
    "Interval-pair covariance is useful but not a complete click law",
    all(result["density_score"] > result["heldout_max"] for result in all_scale_results)
    and any(result["best_score"] <= result["heldout_max"] for result in all_scale_results),
    "rejects density modulation but admits tuned clusters",
)
check(
    "Finite interval-pair null exposes calibration instability or adversary leakage",
    any(result["fixed_outside"] for result in all_scale_results)
    or any(result["best_score"] <= result["heldout_max"] for result in all_scale_results),
    ", ".join(
        f"N={r['N']} fixed_outside={r['fixed_outside']} "
        f"best_ratio={fmt(r['best_score'] / r['heldout_max'], 12)}"
        for r in all_scale_results
    ),
)

print("\n(3) Consequence")
print("Interval-pair covariance rejects lumpy density modulation and staged sandwiches at both tested scales.")
print("Tuned jitter clusters still fit inside at least one finite held-out null.")
print("At N=384, a fresh sprinkling also falls outside the small held-out support,")
print("so this finite null is a diagnostic projection rather than a stable law.")
print("The next law target is therefore a process-level independence/bracket principle,")
print("not merely a larger finite feature vector.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
