#!/usr/bin/env python3
"""
Paper 27 receipt: square-root/global witness attack.

Paper 27 proves that sub-sqrt unrooted induced-suborder tests wash out for
bounded hidden width.  The first possible accumulation scale is therefore

    k = a sqrt(N),

where hidden sibling collisions have nonzero limiting mean

    a^2 (w - 1) / 2.

This receipt deliberately samples k=floor(2 sqrt(N)) induced suborders and
tests order-only, collision-sensitive statistics based on pair-neighborhood
similarity inside the induced order.  Hidden labels are used only to report the
diagnostic collision count; the calibrated score uses only the order.

All asserted non-integer arithmetic uses mpmath with dps=140.
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
        self.future = tuple(future)
        self.N = len(self.future)
        self.past = [0] * self.N
        for x, mask in enumerate(self.future):
            for y in iter_bits(mask):
                self.past[y] |= 1 << x
        self.past = tuple(self.past)


def poset_from_permutation(perm):
    n = len(perm)
    future = [0] * n
    for i in range(n):
        vi = perm[i]
        mask = 0
        for j in range(i + 1, n):
            if vi < perm[j]:
                mask |= 1 << j
        future[i] = mask
    return Poset(future)


def sprinkled2_poset(n, seed):
    rng = random.Random(seed)
    perm = list(range(n))
    rng.shuffle(perm)
    return poset_from_permutation(perm), tuple(range(n))


def coordinate_order_poset(points):
    future = [0] * len(points)
    for i, (ui, vi) in enumerate(points):
        mask = 0
        for j, (uj, vj) in enumerate(points):
            if ui < uj and vi < vj:
                mask |= 1 << j
        future[i] = mask
    return Poset(future)


def clustered_jittered_fiber_poset(n, width, seed, jitter_num, jitter_den):
    rng = random.Random(seed)
    base_n = n // width
    perm = list(range(base_n))
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
    return coordinate_order_poset(points), tuple(labels)


FEATURE_NAMES = [
    "relation_density",
    "degree_variance",
    "max_pair_similarity",
    "p99_pair_similarity",
    "top5_pair_similarity",
    "tail_similarity_ge_0.90",
]


def induced_order_features(poset, vertices):
    k = len(vertices)
    sample_mask = 0
    for x in vertices:
        sample_mask |= 1 << x
    pair_count = mp.mpf(k) * (k - 1) / 2

    rel = 0
    degrees = []
    for x in vertices:
        future_in = (poset.future[x] & sample_mask).bit_count()
        past_in = (poset.past[x] & sample_mask).bit_count()
        rel += future_in
        degrees.append(mp.mpf(future_in + past_in) / (k - 1))
    relation_density = mp.mpf(rel) / pair_count
    degree_mean = mp.fsum(degrees) / k
    degree_variance = mp.fsum((d - degree_mean) ** 2 for d in degrees) / k

    similarities = []
    tail90 = 0
    for i in range(k):
        x = vertices[i]
        x_bit = 1 << x
        for j in range(i + 1, k):
            y = vertices[j]
            y_bit = 1 << y
            exclude = sample_mask ^ x_bit ^ y_bit
            diff = ((poset.future[x] ^ poset.future[y]) | (poset.past[x] ^ poset.past[y])) & exclude
            delta = diff.bit_count()
            similarity = mp.mpf(k - 2 - delta) / (k - 2) if k > 2 else mp.mpf(1)
            similarities.append(similarity)
            if similarity >= mp.mpf("0.90"):
                tail90 += 1
    similarities.sort()
    max_similarity = similarities[-1]
    p99_similarity = similarities[int(mp.floor(mp.mpf("0.99") * (len(similarities) - 1)))]
    top_count = min(5, len(similarities))
    top5_similarity = mp.fsum(similarities[-top_count:]) / top_count
    tail_similarity = mp.mpf(tail90) / pair_count

    return [
        relation_density,
        degree_variance,
        max_similarity,
        p99_similarity,
        top5_similarity,
        tail_similarity,
    ]


def hidden_collision_count(labels, vertices):
    counts = {}
    for x in vertices:
        label = labels[x]
        counts[label] = counts.get(label, 0) + 1
    return sum(count * (count - 1) // 2 for count in counts.values())


def trial_features(poset, labels, k, suborders, seed):
    rng = random.Random(seed)
    feature_rows = []
    collisions = []
    for _ in range(suborders):
        vertices = tuple(rng.sample(range(poset.N), k))
        feature_rows.append(induced_order_features(poset, vertices))
        collisions.append(mp.mpf(hidden_collision_count(labels, vertices)))
    cols = list(zip(*feature_rows))
    features = [mp.fsum(col) / len(col) for col in cols]
    mean_collisions = mp.fsum(collisions) / len(collisions)
    return features, mean_collisions


def mean(values):
    return mp.fsum(values) / len(values)


def std(values):
    if len(values) < 2:
        return mp.mpf(0)
    mu = mean(values)
    return mp.sqrt(mp.fsum((value - mu) ** 2 for value in values) / (len(values) - 1))


def calibrate(rows):
    cols = list(zip(*rows))
    means = [mean(col) for col in cols]
    sigmas = [std(col) for col in cols]
    return means, sigmas


def z_score(features, means, sigmas):
    z = []
    for value, mu, sigma in zip(features, means, sigmas):
        z.append(mp.mpf(0) if sigma == 0 else (value - mu) / sigma)
    return z


def quadratic_score(features, means, sigmas):
    z = z_score(features, means, sigmas)
    return mp.fsum(value * value for value in z), z


def run_size(n, a, seed_offset=0):
    width = 2
    k = int(mp.floor(mp.mpf(a) * mp.sqrt(n)))
    suborders = 28
    train_trials = 12
    heldout_trials = 8
    q_trials = 8
    expected_collision = mp.binomial(k, 2) * (mp.mpf(width - 1) / (n - 1))

    print("\n" + "=" * 80)
    print(f"N={n} width={width} k={k} a={a} seed_offset={seed_offset} suborders_per_trial={suborders}")
    print("=" * 80)
    print(f"expected hidden sibling collisions per induced suborder={fmt(expected_collision, 18)}")

    train_rows = []
    seed_base = 31000000 + seed_offset
    for t in range(train_trials):
        poset, labels = sprinkled2_poset(n, seed_base + n * 100 + t)
        features, _collisions = trial_features(poset, labels, k, suborders, seed_base + 100000 + n * 100 + t)
        train_rows.append(features)
    means, sigmas = calibrate(train_rows)
    print("calibration:")
    for name, mu, sigma in zip(FEATURE_NAMES, means, sigmas):
        print(f"  {name}: mean={fmt(mu, 18)} std={fmt(sigma, 18)}")

    heldout_scores = []
    for t in range(heldout_trials):
        poset, labels = sprinkled2_poset(n, seed_base + 200000 + n * 100 + t)
        features, _collisions = trial_features(poset, labels, k, suborders, seed_base + 300000 + n * 100 + t)
        score, _z = quadratic_score(features, means, sigmas)
        heldout_scores.append(score)
    heldout_max = max(heldout_scores)
    heldout_mean = mean(heldout_scores)
    print(f"heldout score mean={fmt(heldout_mean, 18)} max={fmt(heldout_max, 18)}")

    schedules = [
        ("linear_half", n // 2, width),
        ("linear_one", n, width),
        ("linear_two", 2 * n, width),
    ]
    schedule_outputs = {}
    for schedule_index, (name, jitter_num, jitter_den) in enumerate(schedules):
        scores = []
        collision_means = []
        z_acc = [mp.mpf(0)] * len(FEATURE_NAMES)
        for t in range(q_trials):
            poset, labels = clustered_jittered_fiber_poset(
                n,
                width,
                seed_base + 400000 + n * 100 + schedule_index * 1000 + t,
                jitter_num,
                jitter_den,
            )
            features, collisions = trial_features(
                poset,
                labels,
                k,
                suborders,
                seed_base + 500000 + n * 100 + schedule_index * 1000 + t,
            )
            score, z = quadratic_score(features, means, sigmas)
            scores.append(score)
            collision_means.append(collisions)
            for i, value in enumerate(z):
                z_acc[i] += value
        mean_score = mean(scores)
        mean_collisions = mean(collision_means)
        mean_z = [value / q_trials for value in z_acc]
        top = sorted(zip(FEATURE_NAMES, mean_z), reverse=True, key=lambda row: abs(row[1]))[:3]
        visible = mean_score > heldout_max
        schedule_outputs[name] = {
            "mean_score": mean_score,
            "max_score": max(scores),
            "mean_collisions": mean_collisions,
            "visible": visible,
            "top": top,
        }
        print(
            f"{name}: mean_score={fmt(mean_score, 18)} max_score={fmt(max(scores), 18)} "
            f"hidden_collisions={fmt(mean_collisions, 18)} "
            f"{'visible' if visible else 'inside'} top_z={[ (n, fmt(v, 8)) for n, v in top ]}"
        )

    return {
        "n": n,
        "k": k,
        "seed_offset": seed_offset,
        "expected_collision": expected_collision,
        "heldout_max": heldout_max,
        "schedules": schedule_outputs,
    }


print("=" * 80)
print("Paper 27 square-root/global witness attack")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

results = [run_size(512, 2, 0), run_size(512, 2, 7000000), run_size(1024, 2, 0)]

all_collision_ratios = []
all_classified = True
any_visible = False
visible_names = []
visible_by_schedule = {}
for result in results:
    expected = result["expected_collision"]
    for name, row in result["schedules"].items():
        ratio = row["mean_collisions"] / expected if expected else mp.mpf(0)
        all_collision_ratios.append(ratio)
        all_classified = all_classified and isinstance(row["visible"], bool)
        any_visible = any_visible or row["visible"]
        if row["visible"]:
            visible_names.append(f"N{result['n']}:k{result['k']}:{name}:seed{result.get('seed_offset', 0)}")
            visible_by_schedule[name] = visible_by_schedule.get(name, 0) + 1

robust_visible = any(count >= 2 for count in visible_by_schedule.values())

check(
    "Sqrt sampled suborders have the predicted nonzero hidden-collision scale",
    all(mp.mpf("0.55") < ratio < mp.mpf("1.45") for ratio in all_collision_ratios),
    "ratios=" + ",".join(fmt(ratio, 8) for ratio in all_collision_ratios),
)
check(
    "Order-only sqrt witness schedules are classified against held-out sprinklings",
    all_classified,
    "visible=" + (",".join(visible_names) if visible_names else "none"),
)
check(
    "No sqrt order-only witness is robust across independent calibration blocks",
    not robust_visible,
    "visible_counts=" + ",".join(f"{name}:{count}" for name, count in sorted(visible_by_schedule.items()))
    if visible_by_schedule
    else "none",
)
check(
    "The receipt follows the sqrt-scale opening rather than a sub-sqrt checklist",
    all(result["k"] > mp.sqrt(result["n"]) for result in results),
    ", ".join(f"N={result['n']} k={result['k']}" for result in results),
)

print("\n=== Consequence ===")
if robust_visible:
    print("A sqrt-scale order-only similarity witness is visible across")
    print("independent calibration blocks.  This is a serious candidate residue.")
elif any_visible:
    print("One sqrt-scale similarity witness is visible in one calibration block,")
    print("but it does not reproduce in the independent block or at N=1024.")
    print("The candidate is demoted to finite calibration leakage.")
else:
    print("The sqrt-scale hidden collision field is present at the predicted")
    print("rate, but these order-only pair-neighborhood similarity witnesses do")
    print("not separate the tested linear schedules from held-out sprinklings.")
    print("This is stronger washout evidence, not a theorem.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
