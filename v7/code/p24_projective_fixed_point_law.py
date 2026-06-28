#!/usr/bin/env python3
"""
Receipt for v7 Paper XXIV: projective fixed-point search for the record law.

Paper XXIII ended at the "full finite-dimensional law" wall.  This receipt
turns that wall into a computable inverse target: a finite-density sprinkling is
projectively consistent under deletion.  If m records are sampled uniformly from
an N-record sprinkling and the induced order is kept, the result has the same
law as a fresh m-record sprinkling.

The receipt tests whether the strongest Paper XXIII clustered adversary survives
this multiscale induced-suborder audit.  All asserted non-integer arithmetic
uses mpmath with dps=140.  Poset statistics are integer bitset counts; no
float64 arithmetic is used for asserted quantities.
"""

import random

import mpmath as mp

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
        band_intervals = 0
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
                    band_intervals += 1
                    band_mass += k
                    for z in iter_bits(interior):
                        loads[z] += 1

        load_l2 = sum(v * v for v in loads)
        if band_mass and load_l2:
            eff = mp.mpf(band_mass) ** 2 / load_l2
            max_load_ratio = mp.mpf(max(loads)) / (mp.mpf(band_mass) / self.N)
        else:
            eff = mp.mpf(0)
            max_load_ratio = mp.mpf(0)
        return {
            "hist": hist,
            "recursive_r": (
                mp.mpf(recursive_num) / recursive_den if recursive_den else mp.mpf(0)
            ),
            "effective_support_ratio": eff / self.N if self.N else mp.mpf(0),
            "max_load_ratio": max_load_ratio,
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


def induced_hidden_cluster_stats(labels, vertices):
    counts = {}
    for old in vertices:
        label = labels[old]
        counts[label] = counts.get(label, 0) + 1
    retained_pairs = sum(v * (v - 1) // 2 for v in counts.values())
    total_pairs = len(vertices) * (len(vertices) - 1) // 2
    occupied = len(counts)
    max_multiplicity = max(counts.values()) if counts else 0
    return {
        "retained_pair_fraction": (
            mp.mpf(retained_pairs) / total_pairs if total_pairs else mp.mpf(0)
        ),
        "occupied_cluster_fraction": mp.mpf(occupied) / len(vertices) if vertices else 0,
        "max_multiplicity": max_multiplicity,
    }


def sprinkle_pair_density_expectation(N, alpha):
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


def external_near_twin_count(poset, threshold):
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


def small_interval_endpoint_stats(poset, k_max):
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
        return {
            "density": mp.mpf(0),
            "max_ratio": mp.mpf(0),
            "eff_ratio": mp.mpf(0),
        }
    mean = mp.mpf(total_load) / poset.N
    load_l2 = sum(v * v for v in loads)
    eff = mp.mpf(total_load) ** 2 / load_l2 if load_l2 else mp.mpf(0)
    return {
        "density": mp.mpf(relation_count) / poset.N,
        "max_ratio": mp.mpf(max(loads)) / mean,
        "eff_ratio": eff / poset.N,
    }


def signature(poset):
    audit = poset.interval_audit(load_k_min=max(3, poset.N // 32))
    alpha = mp.log(2)
    p_log2 = profile_P_from_hist_density(audit["hist"], poset.N, alpha)
    p_expected = sprinkle_pair_density_expectation(poset.N, alpha)
    endpoint = small_interval_endpoint_stats(poset, max(1, poset.N // 96))
    near_threshold = max(2, poset.N // 48)
    return {
        "r": poset.ordering_fraction(),
        "height_ratio": height_scale_ratio(poset),
        "recursive_r": audit["recursive_r"],
        "p_log2_ratio": p_log2 / p_expected if p_expected else mp.mpf(0),
        "load_eff": audit["effective_support_ratio"],
        "endpoint_max": endpoint["max_ratio"],
        "near_fraction": external_near_twin_count(poset, near_threshold),
    }


SIGNATURE_KEYS = [
    "r",
    "height_ratio",
    "recursive_r",
    "p_log2_ratio",
    "load_eff",
    "endpoint_max",
    "near_fraction",
]


def mean_signature(signatures):
    return {
        key: sum(sig[key] for sig in signatures) / len(signatures)
        for key in signatures[0]
    }


def signature_moments(signatures):
    mean = mean_signature(signatures)
    std = {}
    if len(signatures) <= 1:
        std = {key: mp.mpf(0) for key in signatures[0]}
    else:
        for key in signatures[0]:
            var = sum((sig[key] - mean[key]) ** 2 for sig in signatures) / (
                len(signatures) - 1
            )
            std[key] = mp.sqrt(var)
    return {"mean": mean, "std": std}


def signature_distance(mean_a, mean_b):
    total = mp.mpf(0)
    for key in SIGNATURE_KEYS:
        a = mean_a[key]
        b = mean_b[key]
        eps = mp.mpf("1e-40")
        if key in {"r", "height_ratio", "recursive_r", "p_log2_ratio", "load_eff", "endpoint_max"}:
            total += abs(mp.log((a + eps) / (b + eps)))
        else:
            total += abs(mp.log((a + eps) / (b + eps)))
    return total


def moment_distance(moments_a, moments_b):
    total = signature_distance(moments_a["mean"], moments_b["mean"])
    eps = mp.mpf("1e-40")
    for key in ["r", "height_ratio", "recursive_r", "p_log2_ratio", "near_fraction"]:
        a = moments_a["std"][key]
        b = moments_b["std"][key]
        total += abs(mp.log((a + eps) / (b + eps)))
    return total


def sample_induced_signatures(poset, sizes, sample_count, seed, labels=None):
    rng = random.Random(seed)
    out = {}
    hidden = {}
    for size in sizes:
        sigs = []
        hidden_rows = []
        for _ in range(sample_count):
            vertices = rng.sample(range(poset.N), size)
            induced = induced_subposet(poset, vertices)
            sigs.append(signature(induced))
            if labels is not None:
                hidden_rows.append(induced_hidden_cluster_stats(labels, vertices))
        out[size] = mean_signature(sigs)
        if labels is not None:
            hidden[size] = {
                key: sum(row[key] for row in hidden_rows) / len(hidden_rows)
                for key in hidden_rows[0]
            }
    return out, hidden


def fresh_sprinkling_signatures(sizes, sample_count, seed0):
    out = {}
    for size in sizes:
        sigs = []
        for i in range(sample_count):
            sigs.append(signature(sprinkled2_poset(size, seed0 + 1009 * size + i)))
        out[size] = mean_signature(sigs)
    return out


def sample_interval_signatures(poset, bands, per_band, seed):
    rng = random.Random(seed)
    out = {}
    sizes = {}
    for label, lo, hi in bands:
        intervals = []
        for x in range(poset.N):
            for y in iter_bits(poset.future[x]):
                k = (poset.future[x] & poset.past[y]).bit_count()
                if lo <= k <= hi:
                    intervals.append((x, y, k))
        chosen = rng.sample(intervals, per_band) if len(intervals) > per_band else intervals
        sigs = []
        ks = []
        for x, y, k in chosen:
            sigs.append(signature(induced_subposet(poset, interval_vertices(poset, x, y))))
            ks.append(k)
        out[label] = mean_signature(sigs)
        sizes[label] = ks
    return out, sizes


def sample_interval_signature_moments(poset, bands, per_band, seed):
    rng = random.Random(seed)
    out = {}
    sizes = {}
    for label, lo, hi in bands:
        intervals = []
        for x in range(poset.N):
            for y in iter_bits(poset.future[x]):
                k = (poset.future[x] & poset.past[y]).bit_count()
                if lo <= k <= hi:
                    intervals.append((x, y, k))
        chosen = rng.sample(intervals, per_band) if len(intervals) > per_band else intervals
        sigs = []
        ks = []
        for x, y, k in chosen:
            sigs.append(signature(induced_subposet(poset, interval_vertices(poset, x, y))))
            ks.append(k)
        out[label] = signature_moments(sigs)
        sizes[label] = ks
    return out, sizes


def fresh_matching_size_interval_targets(size_map, seed0):
    out = {}
    for label, interval_sizes in size_map.items():
        sigs = []
        for i, size in enumerate(interval_sizes):
            sigs.append(signature(sprinkled2_poset(size, seed0 + 1009 * size + i)))
        out[label] = mean_signature(sigs)
    return out


def fresh_matching_size_interval_moments(size_map, seed0):
    out = {}
    for label, interval_sizes in size_map.items():
        sigs = []
        for i, size in enumerate(interval_sizes):
            sigs.append(signature(sprinkled2_poset(size, seed0 + 1009 * size + i)))
        out[label] = signature_moments(sigs)
    return out


def projective_score(candidate_by_size, target_by_size):
    total = mp.mpf(0)
    pieces = {}
    for size in sorted(target_by_size):
        dist = signature_distance(candidate_by_size[size], target_by_size[size])
        pieces[size] = dist
        total += dist
    return total, pieces


def labeled_score(candidate_by_label, target_by_label):
    total = mp.mpf(0)
    pieces = {}
    for label in target_by_label:
        dist = signature_distance(candidate_by_label[label], target_by_label[label])
        pieces[label] = dist
        total += dist
    return total, pieces


def labeled_moment_score(candidate_by_label, target_by_label):
    total = mp.mpf(0)
    pieces = {}
    for label in target_by_label:
        dist = moment_distance(candidate_by_label[label], target_by_label[label])
        pieces[label] = dist
        total += dist
    return total, pieces


def print_signature_table(title, by_size, target=None):
    print(title)
    cols = ["r", "dmm", "height_ratio", "recursive_r", "p_log2_ratio", "near_fraction"]
    print("| m | " + " | ".join(cols) + (" | D_to_fresh |" if target else " |"))
    print("|---:|" + "|".join(["---:" for _ in cols]) + ("|---:|" if target else "|"))
    for size in sorted(by_size):
        row = by_size[size]
        if target:
            dist = signature_distance(row, target[size])
            suffix = f" | {fmt(dist, 16)} |"
        else:
            suffix = " |"
        printable = dict(row)
        printable["dmm"] = mm_inv(row["r"])
        vals = " | ".join(fmt(printable[col], 16) for col in cols)
        print(f"| {size} | {vals}{suffix}")


def full_size_summary(poset):
    sig = signature(poset)
    return (
        f"N={poset.N} r={fmt(sig['r'], 18)} dMM={fmt(mm_inv(sig['r']), 18)} "
        f"H/(2sqrtN)={fmt(sig['height_ratio'], 18)} "
        f"Theta={fmt(sig['recursive_r'], 18)} "
        f"P_log2_ratio={fmt(sig['p_log2_ratio'], 18)} "
        f"near={fmt(sig['near_fraction'], 18)}"
    )


print("=" * 80)
print("P24 projective fixed-point law receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 384
sizes = [48, 96, 192]
sample_count = 8
interval_bands = [("24-47", 24, 47), ("48-95", 48, 95), ("96-191", 96, 191)]

spr = sprinkled2_poset(N, 910246)
cluster, cluster_meta = clustered_jittered_fiber_poset(96, 4, 16008, 3, 1)
fresh_full = mean_signature([signature(sprinkled2_poset(N, 340000 + i)) for i in range(4)])
spr_full_sig = signature(spr)
cluster_full_sig = signature(cluster)

print("\n(1) Full-size starting point")
print("sprinkling:        ", full_size_summary(spr))
print("cluster candidate: ", full_size_summary(cluster))

fresh = fresh_sprinkling_signatures(sizes, sample_count, 270000)
spr_projective, _ = sample_induced_signatures(spr, sizes, sample_count, 271000)
cluster_projective, cluster_hidden = sample_induced_signatures(
    cluster, sizes, sample_count, 272000, labels=cluster_meta["labels"]
)

spr_score, spr_pieces = projective_score(spr_projective, fresh)
cluster_score, cluster_pieces = projective_score(cluster_projective, fresh)

print("\n(2) Fresh sprinkling calibration")
print_signature_table("Fresh m-record sprinklings:", fresh)

print("\n(3) Projective deletion audit")
print_signature_table("Induced suborders of the fixed sprinkling:", spr_projective, fresh)
print_signature_table("Induced suborders of the clustered candidate:", cluster_projective, fresh)
print("sprinkling projective score =", fmt(spr_score, 24), spr_pieces)
print("cluster projective score    =", fmt(cluster_score, 24), cluster_pieces)

print("\nHidden labels, diagnostic only:")
for size in sizes:
    row = cluster_hidden[size]
    print(
        f"m={size}: retained hidden-pair fraction={fmt(row['retained_pair_fraction'], 18)} "
        f"occupied_cluster_fraction={fmt(row['occupied_cluster_fraction'], 18)} "
        f"max_multiplicity_mean={fmt(row['max_multiplicity'], 18)}"
    )

check(
    "A fixed sprinkling is deletion-projective within finite sampled calibration",
    spr_score < mp.mpf("1.25"),
    f"score={fmt(spr_score, 20)}",
)
check(
    "Deletion-projective mean signatures are too weak to reject the clustered candidate",
    cluster_score < mp.mpf("1.20") * spr_score,
    f"cluster={fmt(cluster_score, 20)}, spr={fmt(spr_score, 20)}",
)

print("\n(4) Causally selected interval fixed-point audit")
spr_interval, spr_interval_sizes = sample_interval_signatures(spr, interval_bands, 8, 280000)
spr_interval_target = fresh_matching_size_interval_targets(spr_interval_sizes, 281000)
cluster_interval, cluster_interval_sizes = sample_interval_signatures(
    cluster, interval_bands, 8, 282000
)
cluster_interval_target = fresh_matching_size_interval_targets(cluster_interval_sizes, 283000)
spr_interval_score, spr_interval_pieces = labeled_score(
    spr_interval, spr_interval_target
)
cluster_interval_score, cluster_interval_pieces = labeled_score(
    cluster_interval, cluster_interval_target
)
print_signature_table("Sprinkling interval interiors:", spr_interval, spr_interval_target)
print_signature_table(
    "Clustered-candidate interval interiors:", cluster_interval, cluster_interval_target
)
print(
    "sprinkling interval fixed-point score =",
    fmt(spr_interval_score, 24),
    spr_interval_pieces,
)
print(
    "cluster interval fixed-point score    =",
    fmt(cluster_interval_score, 24),
    cluster_interval_pieces,
)
check(
    "Causally selected interval recursion is sharper than random deletion",
    cluster_interval_score > mp.mpf("1.20") * spr_interval_score,
    f"cluster={fmt(cluster_interval_score, 20)}, spr={fmt(spr_interval_score, 20)}",
)

print("\n(5) Follow-up search: can jitter tune away the interval defect?")
search_rows = []
for jitter_num in [1, 2, 3, 4, 5, 6]:
    for seed in range(16000, 16012):
        cand, meta = clustered_jittered_fiber_poset(96, 4, seed, jitter_num, 1)
        sig = signature(cand)
        dmm = mm_inv(sig["r"])
        if abs(dmm - 2) > mp.mpf("0.25"):
            continue
        if abs(sig["height_ratio"] - 1) > mp.mpf("0.22"):
            continue
        if abs(sig["p_log2_ratio"] - 1) > mp.mpf("0.08"):
            continue
        cand_interval, cand_interval_sizes = sample_interval_signatures(
            cand, interval_bands, 4, 300000 + 997 * jitter_num + seed
        )
        cand_target = fresh_matching_size_interval_targets(
            cand_interval_sizes, 310000 + 997 * jitter_num + seed
        )
        score, pieces = labeled_score(cand_interval, cand_target)
        global_score = signature_distance(sig, fresh_full)
        combined_score = score + 2 * global_score
        _, cand_hidden = sample_induced_signatures(
            cand, [96], 3, 320000 + 997 * jitter_num + seed, labels=meta["labels"]
        )
        hidden96 = cand_hidden[96]["retained_pair_fraction"]
        search_rows.append(
            (
                score,
                combined_score,
                global_score,
                hidden96,
                jitter_num,
                seed,
                sig,
                dmm,
                pieces,
                cand_interval,
                cand_target,
            )
        )

search_rows.sort(key=lambda row: row[0])
(
    best_score,
    best_combined_score,
    best_global_score,
    best_hidden96,
    best_jitter,
    best_seed,
    best_sig,
    best_dmm,
    best_pieces,
    best_interval,
    best_target,
) = search_rows[0]
spr_global_score = signature_distance(spr_full_sig, fresh_full)
cluster_global_score = signature_distance(cluster_full_sig, fresh_full)
spr_combined_score = spr_interval_score + 2 * spr_global_score
cluster_combined_score = cluster_interval_score + 2 * cluster_global_score
combined_rows = sorted(search_rows, key=lambda row: row[1])
(
    best_joint_interval_score,
    best_joint_combined_score,
    best_joint_global_score,
    best_joint_hidden96,
    best_joint_jitter,
    best_joint_seed,
    best_joint_sig,
    best_joint_dmm,
    best_joint_pieces,
    best_joint_interval,
    best_joint_target,
) = combined_rows[0]
print(
    "best interval-only tuned cluster: "
    f"jitter={best_jitter}/1 seed={best_seed} interval_score={fmt(best_score, 24)} "
    f"global_score={fmt(best_global_score, 24)} "
    f"combined_score={fmt(best_combined_score, 24)} "
    f"hidden_pair_fraction_m96={fmt(best_hidden96, 24)}"
)
print(
    "full-size interval-only best: "
    f"dMM={fmt(best_dmm, 18)} Hratio={fmt(best_sig['height_ratio'], 18)} "
    f"P_ratio={fmt(best_sig['p_log2_ratio'], 18)} near={fmt(best_sig['near_fraction'], 18)}"
)
print_signature_table("Best tuned cluster interval profile:", best_interval, best_target)
print(
    "best joint tuned cluster: "
    f"jitter={best_joint_jitter}/1 seed={best_joint_seed} "
    f"interval_score={fmt(best_joint_interval_score, 24)} "
    f"global_score={fmt(best_joint_global_score, 24)} "
    f"combined_score={fmt(best_joint_combined_score, 24)} "
    f"hidden_pair_fraction_m96={fmt(best_joint_hidden96, 24)}"
)
print(
    "full-size joint best: "
    f"dMM={fmt(best_joint_dmm, 18)} Hratio={fmt(best_joint_sig['height_ratio'], 18)} "
    f"P_ratio={fmt(best_joint_sig['p_log2_ratio'], 18)} near={fmt(best_joint_sig['near_fraction'], 18)}"
)
print(
    "combined calibration: "
    f"spr={fmt(spr_combined_score, 24)} "
    f"original_cluster={fmt(cluster_combined_score, 24)} "
    f"best_joint={fmt(best_joint_combined_score, 24)}"
)

check(
    "Interval-only recursion can be tuned below the fixed-sprinkling interval calibration",
    best_score < spr_interval_score,
    f"best={fmt(best_score, 20)}, spr={fmt(spr_interval_score, 20)}",
)
check(
    "Mean combined global-plus-interval scoring is still too weak in this bounded search",
    best_joint_combined_score < spr_combined_score,
    f"best_joint={fmt(best_joint_combined_score, 20)}, spr={fmt(spr_combined_score, 20)}",
)
check(
    "The original clustered candidate is disfavored by the combined global-plus-interval action",
    cluster_combined_score > spr_combined_score,
    f"cluster={fmt(cluster_combined_score, 20)}, spr={fmt(spr_combined_score, 20)}",
)
check(
    "Best bounded tuned candidate still retains hidden cluster multiplicity",
    best_hidden96 > mp.mpf("0.002"),
    f"hidden_pair_fraction_m96={fmt(best_hidden96, 20)}",
)

print("\n(6) Fluctuation/bracket follow-up")
best_joint_poset, _ = clustered_jittered_fiber_poset(
    96, 4, best_joint_seed, best_joint_jitter, 1
)
spr_moments, spr_moment_sizes = sample_interval_signature_moments(
    spr, interval_bands, 12, 350000
)
spr_moment_target = fresh_matching_size_interval_moments(spr_moment_sizes, 351000)
cluster_moments, cluster_moment_sizes = sample_interval_signature_moments(
    cluster, interval_bands, 12, 352000
)
cluster_moment_target = fresh_matching_size_interval_moments(
    cluster_moment_sizes, 353000
)
best_moments, best_moment_sizes = sample_interval_signature_moments(
    best_joint_poset, interval_bands, 12, 354000
)
best_moment_target = fresh_matching_size_interval_moments(best_moment_sizes, 355000)
spr_moment_score, spr_moment_pieces = labeled_moment_score(
    spr_moments, spr_moment_target
)
cluster_moment_score, cluster_moment_pieces = labeled_moment_score(
    cluster_moments, cluster_moment_target
)
best_moment_score, best_moment_pieces = labeled_moment_score(
    best_moments, best_moment_target
)
print(
    "interval fluctuation scores: "
    f"spr={fmt(spr_moment_score, 24)} "
    f"original_cluster={fmt(cluster_moment_score, 24)} "
    f"best_mean_tuned={fmt(best_moment_score, 24)}"
)
print("spr moment pieces:", spr_moment_pieces)
print("original cluster moment pieces:", cluster_moment_pieces)
print("best mean-tuned moment pieces:", best_moment_pieces)
check(
    "Fluctuation/bracket data are independent information beyond mean interval signatures",
    abs(best_moment_score - best_joint_interval_score) > mp.mpf("0.25"),
    f"moment={fmt(best_moment_score, 20)}, mean_interval={fmt(best_joint_interval_score, 20)}",
)

print("\n(7) Candidate law object")
print("Define the finite projective action")
print("A_B(C) = sum_{bands B} w_B D(Law(C restricted to I(x,y) | |I| in B), Pi_|I|),")
print("where I(x,y) is a causal interval and Pi_k is the calibrated k-record")
print("sprinkling law.  Random deletion alone is too geometry-blind; causal")
print("interval recursion is the sharper fixed-point target.  In the limit over")
print("all bands and all finite interval observables, this is the full")
print("finite-dimensional record law.  Mean signatures are also too weak:")
print("the action must include fluctuation/bracket terms, i.e. the law of")
print("record-count variance across intervals, not only average interval content.")
print("A compact click law would be a small action/compensator whose minimizers")
print("make both the mean fixed-point defects and bracket defects small at every scale.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
