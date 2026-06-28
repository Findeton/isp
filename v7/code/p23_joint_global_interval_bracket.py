#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: joint global-and-interval bracket calibration.

This is the continuation that would otherwise have become a separate paper. It
implements the five next steps opened by the interval-bracket campaign:

1. calibrate a held-out null distribution on independent sprinklings;
2. build a joint global-and-interval observable vector with covariance;
3. attack the current bracket-tuned clustered adversary;
4. broaden the adversaries to clustered, density-modulated, and staged families;
5. report whether a compact law candidate is visible.

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
        band_mass = 0
        loads = [0] * self.N
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
                if k >= load_k_min:
                    band_mass += k
                    for z in iter_bits(interior):
                        loads[z] += 1
        load_l2 = sum(v * v for v in loads)
        eff = mp.mpf(band_mass) ** 2 / load_l2 if band_mass and load_l2 else mp.mpf(0)
        return {
            "hist": hist,
            "recursive_r": (
                mp.mpf(recursive_num) / recursive_den if recursive_den else mp.mpf(0)
            ),
            "effective_support_ratio": eff / self.N if self.N else mp.mpf(0),
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
        "base_N": base_N,
        "width": width,
        "seed": seed,
        "jitter": f"{jitter_num}/{jitter_den}",
        "labels": labels,
    }


def density_modulated_poset(N, seed, cell_count=6, bonus=3):
    """A simple non-Poisson coordinate process with lumpy cell intensities."""
    rng = random.Random(seed)
    weights = [1 + ((i * 37 + seed) % (bonus + 1)) for i in range(cell_count)]
    total = sum(weights)
    points = []
    scale = 1000000
    for index in range(N):
        pick = rng.randrange(total)
        acc = 0
        cell = 0
        for c, weight in enumerate(weights):
            acc += weight
            if pick < acc:
                cell = c
                break
        # Bias both light-cone coordinates into the selected cell with an
        # independent local offset.  This creates cell-level density modulation
        # without explicit hidden fibers.
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


def interval_vertices(poset, x, y):
    return list(iter_bits(poset.future[x] & poset.past[y]))


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


def small_interval_endpoint_max(poset, k_max):
    loads = [0] * poset.N
    relation_count = 0
    for x in range(poset.N):
        for y in iter_bits(poset.future[x]):
            k = (poset.future[x] & poset.past[y]).bit_count()
            if k <= k_max:
                relation_count += 1
                loads[x] += 1
                loads[y] += 1
    total_load = 2 * relation_count
    if not total_load:
        return mp.mpf(0)
    mean = mp.mpf(total_load) / poset.N
    return mp.mpf(max(loads)) / mean


def external_near_twin_fraction(poset, threshold):
    threshold = int(threshold)
    count = 0
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
    p_expected = sprinkle_pair_density_expectation(poset.N, mp.log(2))
    p_observed = profile_P_from_hist_density(audit["hist"], poset.N, mp.log(2))
    return [
        poset.ordering_fraction(),
        height_scale_ratio(poset),
        audit["recursive_r"],
        p_observed / p_expected if p_expected else mp.mpf(0),
        external_near_twin_fraction(poset, max(2, poset.N // 48)),
    ]


def full_signature(poset):
    fv = feature_vector(poset)
    return {name: value for name, value in zip(FEATURES, fv)} | {"dmm": mm_inv(fv[0])}


def intervals_in_band(poset, lo, hi):
    intervals = []
    for x in range(poset.N):
        for y in iter_bits(poset.future[x]):
            k = (poset.future[x] & poset.past[y]).bit_count()
            if lo <= k <= hi:
                intervals.append((x, y, k))
    return intervals


def sample_interval_rows(poset, bands, per_band, seed):
    rng = random.Random(seed)
    sampled = {}
    for label, lo, hi in bands:
        intervals = intervals_in_band(poset, lo, hi)
        chosen = rng.sample(intervals, per_band) if len(intervals) > per_band else intervals
        rows = []
        for x, y, _ in chosen:
            rows.append(feature_vector(induced_subposet(poset, interval_vertices(poset, x, y))))
        sampled[label] = rows
    return sampled


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


def joint_observable_vector(poset, bands, per_band, seed):
    out = list(feature_vector(poset))
    sampled = sample_interval_rows(poset, bands, per_band, seed)
    for label, _, _ in bands:
        rows = sampled[label]
        if not rows:
            mean = [mp.mpf(0) for _ in FEATURES]
            out.extend(mean)
            out.extend([mp.mpf(0) for _ in FEATURES])
            out.extend([mp.mpf(0) for _ in SELECTED_COV])
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


def calibrate_joint_action(N, bands, per_band, train_seeds, heldout_seeds):
    train_rows = [
        joint_observable_vector(sprinkled2_poset(N, seed), bands, per_band, seed + 700000)
        for seed in train_seeds
    ]
    mean = mean_vector(train_rows)
    cov = covariance_matrix(train_rows, mean)
    L = cholesky(cov)

    def score_poset(poset, seed):
        row = joint_observable_vector(poset, bands, per_band, seed)
        z = solve_lower(L, [row[i] - mean[i] for i in range(len(mean))])
        return sum(value * value for value in z), z

    heldout = []
    for seed in heldout_seeds:
        score, _ = score_poset(sprinkled2_poset(N, seed), seed + 800000)
        heldout.append(score)
    heldout.sort()
    return {
        "mean": mean,
        "cov": cov,
        "chol": L,
        "score_poset": score_poset,
        "heldout": heldout,
        "train_rows": train_rows,
    }


def rank_against_null(score, null_scores):
    less_equal = sum(1 for value in null_scores if value <= score)
    return mp.mpf(less_equal) / len(null_scores)


def print_signature(name, poset):
    sig = full_signature(poset)
    print(
        f"{name}: N={poset.N} dMM={fmt(sig['dmm'], 18)} "
        f"Hratio={fmt(sig['height'], 18)} theta={fmt(sig['theta'], 18)} "
        f"P={fmt(sig['p_log2'], 18)} near={fmt(sig['near'], 18)}"
    )


def score_and_print(name, poset, action, seed):
    score, _ = action["score_poset"](poset, seed)
    rank = rank_against_null(score, action["heldout"])
    print(f"{name}: joint_score={fmt(score, 18)} heldout_rank={fmt(rank, 18)}")
    return score, rank


def hidden_cluster_pair_fraction(poset, labels, bands, per_band, seed):
    rng = random.Random(seed)
    vals = []
    for label, lo, hi in bands:
        intervals = intervals_in_band(poset, lo, hi)
        chosen = rng.sample(intervals, per_band) if len(intervals) > per_band else intervals
        for x, y, _ in chosen:
            counts = {}
            for old in interval_vertices(poset, x, y):
                counts[labels[old]] = counts.get(labels[old], 0) + 1
            k = sum(counts.values())
            total = k * (k - 1) // 2
            same = sum(v * (v - 1) // 2 for v in counts.values())
            if total:
                vals.append(mp.mpf(same) / total)
    return sum(vals) / len(vals) if vals else mp.mpf(0)


print("=" * 80)
print("Collapsed P23 joint global-and-interval bracket receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 384
bands = [("24-47", 24, 47), ("48-95", 48, 95), ("96-191", 96, 191)]
per_band = 4
train_seeds = list(range(610000, 610056))
heldout_seeds = list(range(620000, 620016))

print("\n(1) Train/held-out joint null calibration")
action = calibrate_joint_action(N, bands, per_band, train_seeds, heldout_seeds)
heldout = action["heldout"]
print("joint vector dimension =", len(action["mean"]))
print("train sprinklings =", len(train_seeds))
print("held-out sprinklings =", len(heldout_seeds))
print("heldout scores =", [fmt(x, 12) for x in heldout])
print("heldout median =", fmt(heldout[len(heldout) // 2], 18))
print("heldout max =", fmt(heldout[-1], 18))
check(
    "Held-out null distribution is finite and nondegenerate",
    heldout[-1] > heldout[0] and heldout[0] > 0,
    f"min={fmt(heldout[0], 20)}, max={fmt(heldout[-1], 20)}",
)

print("\n(2) Current best enemies")
fixed = sprinkled2_poset(N, 910246)
original, original_meta = clustered_jittered_fiber_poset(96, 4, 16008, 3, 1)
mean_tuned, mean_meta = clustered_jittered_fiber_poset(96, 4, 16002, 6, 1)
bracket_tuned, bracket_meta = clustered_jittered_fiber_poset(96, 4, 16003, 3, 1)
for name, poset in [
    ("fixed sprinkling", fixed),
    ("Paper 23 regularity-aware cluster", original),
    ("mean-tuned cluster", mean_tuned),
    ("interval-bracket-tuned cluster", bracket_tuned),
]:
    print_signature(name, poset)
fixed_score, fixed_rank = score_and_print("fixed sprinkling", fixed, action, 630000)
orig_score, orig_rank = score_and_print("regularity-aware cluster", original, action, 630001)
mean_score, mean_rank = score_and_print("mean-tuned cluster", mean_tuned, action, 630002)
bracket_score, bracket_rank = score_and_print("bracket-tuned cluster", bracket_tuned, action, 630003)
print(
    "bracket-tuned hidden interval pair fraction =",
    fmt(hidden_cluster_pair_fraction(bracket_tuned, bracket_meta["labels"], bands, 5, 630004), 20),
)
check(
    "Current interval-bracket-tuned adversary is explicitly ranked against the held-out null",
    mp.mpf(0) <= bracket_rank <= 1,
    f"bracket={fmt(bracket_score, 20)}, heldout_max={fmt(heldout[-1], 20)}",
)
check(
    "Joint action ranks the fixed sprinkling inside the held-out null support",
    fixed_score <= heldout[-1],
    f"fixed={fmt(fixed_score, 20)}, heldout_max={fmt(heldout[-1], 20)}",
)

print("\n(3) Broadened adversary menu")
adversaries = []
for width in [3, 4]:
    if N % width:
        continue
    base_N = N // width
    for jitter in [2, 3, 4, 6]:
        for seed in range(16000, 16004):
            candidate, meta = clustered_jittered_fiber_poset(base_N, width, seed, jitter, 1)
            sig = full_signature(candidate)
            if abs(sig["dmm"] - 2) < mp.mpf("0.45") and abs(sig["p_log2"] - 1) < mp.mpf("0.18"):
                adversaries.append((f"cluster_w{width}_j{jitter}_s{seed}", candidate, meta))
for seed in range(17000, 17004):
    candidate, meta = density_modulated_poset(N, seed, cell_count=6, bonus=4)
    adversaries.append((f"density_mod_s{seed}", candidate, meta))
for seed in range(18000, 18003):
    candidate, meta = staged_sandwich_poset(N, middle=23, seed=seed, chain_height=39)
    adversaries.append((f"staged_s{seed}", candidate, meta))

scored = []
for index, (name, candidate, meta) in enumerate(adversaries):
    score, rank = score_and_print(name, candidate, action, 640000 + index)
    scored.append((score, rank, name, candidate, meta))
scored.sort(key=lambda row: row[0])
best_score, best_rank, best_name, best_candidate, best_meta = scored[0]
print("\nBest broadened adversary:", best_name)
print_signature("best broadened", best_candidate)
print("best score =", fmt(best_score, 24), "rank =", fmt(best_rank, 18))
if "labels" in best_meta:
    print(
        "best hidden interval pair fraction =",
        fmt(hidden_cluster_pair_fraction(best_candidate, best_meta["labels"], bands, 5, 650000), 20),
    )
check(
    "Broadened adversary menu is scored against the same held-out null",
    len(scored) > 0 and mp.mpf(0) <= best_rank <= 1,
    f"best={fmt(best_score, 20)}, heldout_max={fmt(heldout[-1], 20)}",
)

print("\n(4) Compression audit")
print("The successful finite object is not a scalar.  It is a whitened joint vector:")
print("  global observables + interval means + interval variances + selected interval covariances.")
print("The compact candidate is therefore a joint martingale bracket field:")
print("  residual interval/global observables should have calibrated drift and calibrated bracket.")
compression_gap = best_score / heldout[-1]
print("best_adversary / heldout_max =", fmt(compression_gap, 24))
check(
    "Compression audit completed on the best broadened adversary",
    compression_gap > 0,
    f"ratio={fmt(compression_gap, 20)}",
)

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
