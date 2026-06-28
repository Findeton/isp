#!/usr/bin/env python3
"""
Receipt for v7 Paper XXV: calibrated interval-compensator bracket action.

Paper XXIV found that interval means and crude moment scores can be tuned by
clustered coordinate adversaries.  This receipt takes the next step: calibrate a
finite covariance kernel for interval observables on independent 1+1
sprinklings, whiten candidate interval-observable residuals, and score both the
compensator mean and the bracket matrix.

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
        if band_mass and load_l2:
            eff = mp.mpf(band_mass) ** 2 / load_l2
        else:
            eff = mp.mpf(0)
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
        "base_N": base_N,
        "width": width,
        "seed": seed,
        "jitter": f"{jitter_num}/{jitter_den}",
        "span_over_spacing": mp.mpf(jitter_num) / jitter_den,
        "labels": labels,
    }


def induced_subposet(poset, vertices):
    vertices = list(vertices)
    old_to_new = {old: new for new, old in enumerate(vertices)}
    vertex_mask = 0
    for old in vertices:
        vertex_mask |= 1 << old
    future = [0] * len(vertices)
    for new_x, old_x in enumerate(vertices):
        induced = poset.future[old_x] & vertex_mask
        mask = 0
        for old_y in iter_bits(induced):
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
        for k in range(0, m + 1):
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


FEATURES = [
    "r",
    "height_ratio",
    "recursive_r",
    "p_log2_ratio",
    "endpoint_max",
    "near_fraction",
]


def feature_vector(poset):
    audit = poset.interval_audit(load_k_min=max(3, poset.N // 32))
    p_expected = sprinkle_pair_density_expectation(poset.N, mp.log(2))
    p_observed = profile_P_from_hist_density(audit["hist"], poset.N, mp.log(2))
    return [
        poset.ordering_fraction(),
        height_scale_ratio(poset),
        audit["recursive_r"],
        p_observed / p_expected if p_expected else mp.mpf(0),
        small_interval_endpoint_max(poset, max(1, poset.N // 96)),
        external_near_twin_fraction(poset, max(2, poset.N // 48)),
    ]


def full_signature(poset):
    features = feature_vector(poset)
    return {
        name: value for name, value in zip(FEATURES, features)
    } | {"dmm": mm_inv(features[0])}


def intervals_in_band(poset, lo, hi):
    intervals = []
    for x in range(poset.N):
        for y in iter_bits(poset.future[x]):
            k = (poset.future[x] & poset.past[y]).bit_count()
            if lo <= k <= hi:
                intervals.append((x, y, k))
    return intervals


def sample_interval_feature_vectors(poset, bands, per_band, seed):
    rng = random.Random(seed)
    out = {}
    sizes = {}
    for label, lo, hi in bands:
        intervals = intervals_in_band(poset, lo, hi)
        chosen = rng.sample(intervals, per_band) if len(intervals) > per_band else intervals
        rows = []
        ks = []
        for x, y, k in chosen:
            rows.append(feature_vector(induced_subposet(poset, interval_vertices(poset, x, y))))
            ks.append(k)
        out[label] = rows
        sizes[label] = ks
    return out, sizes


def mean_vector(rows):
    d = len(rows[0])
    return [sum(row[i] for row in rows) / len(rows) for i in range(d)]


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
    ridge = max(avg_diag * mp.mpf("1e-6"), mp.mpf("1e-18"))
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


def calibrate_bracket(bands, N, seeds, per_band):
    rows_by_band = {label: [] for label, _, _ in bands}
    for seed in seeds:
        poset = sprinkled2_poset(N, seed)
        sampled, _ = sample_interval_feature_vectors(poset, bands, per_band, seed + 100000)
        for label in rows_by_band:
            rows_by_band[label].extend(sampled[label])

    calibration = {}
    for label, rows in rows_by_band.items():
        mean = mean_vector(rows)
        cov = covariance_matrix(rows, mean)
        calibration[label] = {
            "rows": rows,
            "mean": mean,
            "cov": cov,
            "chol": cholesky(cov),
        }
    return calibration


def bracket_score(poset, calibration, bands, per_band, seed):
    sampled, sizes = sample_interval_feature_vectors(poset, bands, per_band, seed)
    d = len(FEATURES)
    total_mean = mp.mpf(0)
    total_bracket = mp.mpf(0)
    band_details = {}
    for label, rows in sampled.items():
        cal = calibration[label]
        whitened = []
        for row in rows:
            centered = [row[i] - cal["mean"][i] for i in range(d)]
            whitened.append(solve_lower(cal["chol"], centered))
        mean_z = mean_vector(whitened)
        second = [[mp.mpf(0) for _ in range(d)] for _ in range(d)]
        for z in whitened:
            for i in range(d):
                for j in range(d):
                    second[i][j] += z[i] * z[j] / len(whitened)
        mean_score = sum(value * value for value in mean_z)
        bracket = mp.mpf(0)
        for i in range(d):
            for j in range(d):
                target = mp.mpf(1) if i == j else mp.mpf(0)
                bracket += (second[i][j] - target) ** 2
        bracket /= d * d
        total_mean += mean_score
        total_bracket += bracket
        band_details[label] = {
            "mean_score": mean_score,
            "bracket_score": bracket,
            "sizes": sizes[label],
            "mean_z_norm": mp.sqrt(mean_score),
        }
    return {
        "mean_score": total_mean,
        "bracket_score": total_bracket,
        "total": total_mean + total_bracket,
        "bands": band_details,
    }


def hidden_interval_cluster_fraction(poset, labels, bands, per_band, seed):
    rng = random.Random(seed)
    values = {}
    for label, lo, hi in bands:
        intervals = intervals_in_band(poset, lo, hi)
        chosen = rng.sample(intervals, per_band) if len(intervals) > per_band else intervals
        pair_fracs = []
        max_mults = []
        for x, y, _ in chosen:
            counts = {}
            for old in interval_vertices(poset, x, y):
                counts[labels[old]] = counts.get(labels[old], 0) + 1
            k = sum(counts.values())
            total_pairs = k * (k - 1) // 2
            same_pairs = sum(v * (v - 1) // 2 for v in counts.values())
            pair_fracs.append(mp.mpf(same_pairs) / total_pairs if total_pairs else mp.mpf(0))
            max_mults.append(max(counts.values()) if counts else 0)
        values[label] = {
            "pair_fraction": sum(pair_fracs) / len(pair_fracs),
            "max_multiplicity": mp.mpf(sum(max_mults)) / len(max_mults),
        }
    return values


def print_score(name, score):
    print(
        f"{name}: total={fmt(score['total'], 18)} "
        f"mean={fmt(score['mean_score'], 18)} "
        f"bracket={fmt(score['bracket_score'], 18)}"
    )
    for label, detail in score["bands"].items():
        print(
            f"  {label}: mean={fmt(detail['mean_score'], 18)} "
            f"bracket={fmt(detail['bracket_score'], 18)} "
            f"mean_z_norm={fmt(detail['mean_z_norm'], 18)} "
            f"sizes={detail['sizes']}"
        )


def print_full(name, poset):
    sig = full_signature(poset)
    print(
        f"{name}: N={poset.N} r={fmt(sig['r'], 18)} "
        f"dMM={fmt(sig['dmm'], 18)} Hratio={fmt(sig['height_ratio'], 18)} "
        f"Theta={fmt(sig['recursive_r'], 18)} "
        f"P_ratio={fmt(sig['p_log2_ratio'], 18)} "
        f"near={fmt(sig['near_fraction'], 18)}"
    )


print("=" * 80)
print("P25 calibrated interval-compensator bracket action")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 384
bands = [("24-47", 24, 47), ("48-95", 48, 95), ("96-191", 96, 191)]

print("\n(1) Calibrating interval-observable covariance on independent sprinklings")
calibration = calibrate_bracket(
    bands=bands,
    N=N,
    seeds=[450000, 450001, 450002, 450003, 450004],
    per_band=10,
)
for label, cal in calibration.items():
    print(f"{label}: calibration rows={len(cal['rows'])}")
    for name, value in zip(FEATURES, cal["mean"]):
        print(f"  mean {name} = {fmt(value, 18)}")

print("\n(2) Baselines and Paper XXIII adversaries")
spr_test = sprinkled2_poset(N, 910246)
original_cluster, original_meta = clustered_jittered_fiber_poset(96, 4, 16008, 3, 1)
mean_tuned_cluster, mean_tuned_meta = clustered_jittered_fiber_poset(96, 4, 16002, 6, 1)
print_full("fixed sprinkling", spr_test)
print_full("Paper XXIII cluster", original_cluster)
print_full("Paper XXIV mean-tuned cluster", mean_tuned_cluster)

spr_score = bracket_score(spr_test, calibration, bands, per_band=12, seed=460000)
original_score = bracket_score(original_cluster, calibration, bands, per_band=12, seed=460001)
mean_tuned_score = bracket_score(mean_tuned_cluster, calibration, bands, per_band=12, seed=460002)
print_score("fixed sprinkling bracket action", spr_score)
print_score("Paper XXIII cluster bracket action", original_score)
print_score("Paper XXIV mean-tuned bracket action", mean_tuned_score)

check(
    "The original clustered adversary is disfavored by the calibrated bracket action",
    original_score["total"] > spr_score["total"],
    f"cluster={fmt(original_score['total'], 20)}, spr={fmt(spr_score['total'], 20)}",
)
check(
    "The Paper XXIV mean-tuned adversary is still visible to the calibrated bracket action",
    mean_tuned_score["total"] > spr_score["total"],
    f"mean_tuned={fmt(mean_tuned_score['total'], 20)}, spr={fmt(spr_score['total'], 20)}",
)

print("\nHidden interval-cluster diagnostics, not part of the law")
for name, poset, meta in [
    ("Paper XXIII cluster", original_cluster, original_meta),
    ("Paper XXIV mean-tuned", mean_tuned_cluster, mean_tuned_meta),
]:
    hidden = hidden_interval_cluster_fraction(poset, meta["labels"], bands, 8, 461000)
    print(name)
    for label, row in hidden.items():
        print(
            f"  {label}: hidden_pair_fraction={fmt(row['pair_fraction'], 18)} "
            f"max_multiplicity={fmt(row['max_multiplicity'], 18)}"
        )

print("\n(3) Hostile search against the calibrated bracket action")
search_rows = []
for jitter_num in range(2, 9):
    for seed in range(16000, 16010):
        candidate, meta = clustered_jittered_fiber_poset(96, 4, seed, jitter_num, 1)
        sig = full_signature(candidate)
        if abs(sig["dmm"] - 2) > mp.mpf("0.30"):
            continue
        if abs(sig["height_ratio"] - 1) > mp.mpf("0.25"):
            continue
        if abs(sig["p_log2_ratio"] - 1) > mp.mpf("0.10"):
            continue
        score = bracket_score(candidate, calibration, bands, per_band=5, seed=470000 + 101 * jitter_num + seed)
        hidden = hidden_interval_cluster_fraction(candidate, meta["labels"], bands, 4, 480000 + seed)
        hidden_96 = hidden["48-95"]["pair_fraction"]
        search_rows.append((score["total"], score, jitter_num, seed, sig, hidden_96, candidate, meta))

search_rows.sort(key=lambda row: row[0])
best_total, best_score, best_jitter, best_seed, best_sig, best_hidden_96, best_candidate, best_meta = search_rows[0]
print(
    f"best bracket-tuned cluster: jitter={best_jitter}/1 seed={best_seed} "
    f"total={fmt(best_total, 24)} hidden_48_95={fmt(best_hidden_96, 24)}"
)
print(
    f"full-size best: dMM={fmt(best_sig['dmm'], 18)} "
    f"Hratio={fmt(best_sig['height_ratio'], 18)} "
    f"P_ratio={fmt(best_sig['p_log2_ratio'], 18)} "
    f"near={fmt(best_sig['near_fraction'], 18)}"
)
print_score("best bracket-tuned cluster bracket action", best_score)

spr_search_calibration_score = bracket_score(spr_test, calibration, bands, per_band=5, seed=470000)
print_score("fixed sprinkling search-resolution bracket action", spr_search_calibration_score)

check(
    "A bounded bracket-tuned clustered adversary still exists at this receipt resolution",
    best_score["total"] < spr_search_calibration_score["total"],
    f"best={fmt(best_score['total'], 20)}, spr_search={fmt(spr_search_calibration_score['total'], 20)}",
)
check(
    "The bracket-tuned winner keeps hidden clustered multiplicity diagnostically",
    best_hidden_96 > mp.mpf("0.004"),
    f"hidden_48_95={fmt(best_hidden_96, 20)}",
)

print("\n(4) Follow-up: add global full-size bracket context")
fresh_full_features = [feature_vector(sprinkled2_poset(N, 490000 + i)) for i in range(8)]
full_mean = mean_vector(fresh_full_features)
full_cov = covariance_matrix(fresh_full_features, full_mean)
full_chol = cholesky(full_cov)


def full_global_score(poset):
    z = solve_lower(full_chol, [a - b for a, b in zip(feature_vector(poset), full_mean)])
    return sum(value * value for value in z)


spr_global = full_global_score(spr_test)
original_global = full_global_score(original_cluster)
mean_tuned_global = full_global_score(mean_tuned_cluster)
best_global = full_global_score(best_candidate)
print(
    "global whitened scores: "
    f"spr={fmt(spr_global, 18)} "
    f"original={fmt(original_global, 18)} "
    f"mean_tuned={fmt(mean_tuned_global, 18)} "
    f"best_bracket_tuned={fmt(best_global, 18)}"
)
combined_spr = spr_search_calibration_score["total"] + spr_global
combined_best = best_score["total"] + best_global
print(
    "combined search-resolution score: "
    f"spr={fmt(combined_spr, 18)} "
    f"best_bracket_tuned={fmt(combined_best, 18)}"
)
check(
    "Global full-size context is independent of the interval bracket score",
    abs(best_global - spr_global) > mp.mpf("0.5"),
    f"best_global={fmt(best_global, 20)}, spr_global={fmt(spr_global, 20)}",
)

print("\n(5) Consequence")
print("The calibrated interval bracket catches the previous Paper XXIV mean-tuned cluster,")
print("but a new bracket-tuned clustered adversary remains at the tested finite resolution.")
print("Therefore the bracket action is a real advance but not yet a law.  The next target")
print("must include the joint global-and-interval covariance field, with larger calibration")
print("and adversarial optimization over processes rather than a small jitter grid.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
