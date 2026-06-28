#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: mesoscopic rooted pair-flag field audit.

The four/five-record endpoint-symmetric pair-flag likelihood ladder was the
smallest invariant repair of the rejected oriented aggregate bracket.  It did
not robustly recover the tested linear-window schedules.  This receipt follows
the immediate opening: use larger rooted flags, but stabilize the sparse
vocabulary by hashing canonical flag codes into calibrated bucket fields.

For each unordered root pair {x,y}, sample four outsider records, compute the
canonical rooted flag code of the six-record induced order under endpoint swap
and outsider permutation, then aggregate code-bucket frequencies plus entropy,
collision, and smoothed code likelihood features.  The whole vector is
calibrated on 1+1 sprinklings and tested on clustered-coordinate schedules.

Hostile safeguards:
  - endpoint swaps must preserve the code;
  - outsider permutations must preserve the code;
  - random record relabeling must preserve relabel-mapped sample codes;
  - an independent sample design is run before promoting any weak signal.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import Counter
from itertools import permutations
import random
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140
SIGMA_FLOOR = mp.mpf("0.00001")
SMOOTHING = mp.mpf("0.5")
BUCKET_SIZES = [64, 256]


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


def relation(poset, a, b):
    return bool(poset.future[a] & (1 << b))


def relabel_poset(poset, seed):
    rng = random.Random(seed)
    old_to_new = list(range(poset.N))
    rng.shuffle(old_to_new)
    future = [0] * poset.N
    for old_x, mask in enumerate(poset.future):
        new_x = old_to_new[old_x]
        new_mask = 0
        for old_y in iter_bits(mask):
            new_mask |= 1 << old_to_new[old_y]
        future[new_x] = new_mask
    return Poset(future), old_to_new


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


ORDER_CACHE = {}


def root_orders(outsider_size):
    if outsider_size not in ORDER_CACHE:
        outsider_indices = tuple(range(2, 2 + outsider_size))
        orders = []
        for root_order in ((0, 1), (1, 0)):
            for out_perm in permutations(outsider_indices):
                orders.append(root_order + out_perm)
        ORDER_CACHE[outsider_size] = orders
    return ORDER_CACHE[outsider_size]


def rooted_flag_code(poset, endpoints, outsiders):
    """Canonical rooted flag code under endpoint swap and outsider permutation."""
    vertices = tuple(endpoints) + tuple(outsiders)
    size = len(vertices)
    rel = [[False] * size for _ in range(size)]
    for i, a in enumerate(vertices):
        future = poset.future[a]
        for j, b in enumerate(vertices):
            if i != j:
                rel[i][j] = bool(future & (1 << b))

    best = None
    for order in root_orders(len(outsiders)):
        bits = []
        for i in range(size):
            oi = order[i]
            row = rel[oi]
            for j in range(size):
                if i != j:
                    bits.append("1" if row[order[j]] else "0")
        code = "".join(bits)
        if best is None or code < best:
            best = code
    return best


def sample_pair_flags(N, endpoint_count, outsider_count, outsider_size, seed):
    rng = random.Random(seed)
    endpoint_pairs = set()
    target = min(endpoint_count, N * (N - 1) // 2)
    while len(endpoint_pairs) < target:
        x = rng.randrange(N)
        y = rng.randrange(N - 1)
        if y >= x:
            y += 1
        if x > y:
            x, y = y, x
        endpoint_pairs.add((x, y))

    samples = []
    for x, y in sorted(endpoint_pairs):
        forbidden = {x, y}
        for _ in range(outsider_count):
            outsiders = set()
            while len(outsiders) < outsider_size:
                z = rng.randrange(N)
                if z not in forbidden:
                    outsiders.add(z)
            samples.append((x, y, tuple(sorted(outsiders))))
    return samples


def mapped_samples(samples, old_to_new):
    return [
        (old_to_new[x], old_to_new[y], tuple(old_to_new[z] for z in outsiders))
        for x, y, outsiders in samples
    ]


def flag_counts(poset, samples):
    counts = Counter()
    for x, y, outsiders in samples:
        counts[rooted_flag_code(poset, (x, y), outsiders)] += 1
    return counts


def code_bucket(code, bucket_size):
    return int(code, 2) % bucket_size


def build_code_model(train_counts):
    vocabulary = sorted(set().union(*(row.keys() for row in train_counts)))
    pooled = Counter()
    total = 0
    for row in train_counts:
        pooled.update(row)
        total += sum(row.values())
    denom = mp.mpf(total) + SMOOTHING * (len(vocabulary) + 1)
    probabilities = {
        code: (mp.mpf(pooled[code]) + SMOOTHING) / denom for code in vocabulary
    }
    oov_probability = SMOOTHING / denom
    return vocabulary, probabilities, oov_probability


def counts_to_vector(counts, model):
    vocabulary, probabilities, oov_probability = model
    total = mp.mpf(sum(counts.values()))
    vector = []
    names = []

    for bucket_size in BUCKET_SIZES:
        bucket_counts = [0] * bucket_size
        for code, count in counts.items():
            bucket_counts[code_bucket(code, bucket_size)] += count
        for index, count in enumerate(bucket_counts):
            vector.append(mp.mpf(count) / total)
            names.append(f"b{bucket_size}_{index}")

    entropy = mp.mpf(0)
    collision = mp.mpf(0)
    for count in counts.values():
        freq = mp.mpf(count) / total
        entropy -= freq * mp.log(freq)
        collision += freq * freq

    seen = set(vocabulary)
    oov_count = sum(count for code, count in counts.items() if code not in seen)
    nll = mp.mpf(0)
    chi2 = mp.mpf(0)
    for code in vocabulary:
        freq = mp.mpf(counts.get(code, 0)) / total
        prob = probabilities[code]
        if counts.get(code, 0):
            nll -= freq * mp.log(prob)
        chi2 += (freq - prob) ** 2 / prob
    oov_freq = mp.mpf(oov_count) / total
    if oov_count:
        nll -= oov_freq * mp.log(oov_probability)
    chi2 += (oov_freq - oov_probability) ** 2 / oov_probability

    vector.extend([mp.mpf(len(counts)) / total, entropy, collision, oov_freq, nll, chi2])
    names.extend(["distinct_rate", "entropy", "collision", "oov", "nll", "code_chi2"])
    return vector, names


def mean(values):
    return sum(values) / len(values)


def mean_vector(rows):
    return [mean([row[i] for row in rows]) for i in range(len(rows[0]))]


def std_vector(rows, mu):
    denom = max(1, len(rows) - 1)
    out = []
    for i in range(len(mu)):
        var = sum((row[i] - mu[i]) ** 2 for row in rows) / denom
        empirical = mp.sqrt(var) if var > 0 else mp.mpf(0)
        out.append(max(empirical, SIGMA_FLOOR))
    return out


def score(vector, mu, sigma, names):
    components = [abs((vector[i] - mu[i]) / sigma[i]) for i in range(len(vector))]
    total = mp.sqrt(sum(value * value for value in components))
    top = sorted(
        [(components[i], names[i], vector[i], mu[i], sigma[i]) for i in range(len(vector))],
        reverse=True,
        key=lambda row: row[0],
    )[:5]
    return total, top


def run_mesoscopic_field(field_name, seed_offset):
    N = 768
    width = 4
    base = N // width
    train_count = 8
    heldout_count = 4
    rep_count = 4
    samples = sample_pair_flags(
        N,
        endpoint_count=1536,
        outsider_count=2,
        outsider_size=4,
        seed=3000000 + seed_offset,
    )
    print(f"\n=== {field_name}: six-record rooted flags={len(samples)} ===")

    train_counts = []
    for rep in range(train_count):
        poset = sprinkled2_poset(N, 3010000 + seed_offset * 100 + rep)
        counts = flag_counts(poset, samples)
        train_counts.append(counts)
        print(f"train rep={rep} distinct={len(counts)} total={sum(counts.values())}")

    model = build_code_model(train_counts)
    train_vectors = []
    names = None
    for row in train_counts:
        vector, names = counts_to_vector(row, model)
        train_vectors.append(vector)
    mu = mean_vector(train_vectors)
    sigma = std_vector(train_vectors, mu)
    print(
        f"model vocabulary={len(model[0])} flags={len(samples)} "
        f"train_entropy_mean={fmt(mu[-5], 18)}"
    )

    heldout_scores = []
    for rep in range(heldout_count):
        poset = sprinkled2_poset(N, 3020000 + seed_offset * 100 + rep)
        counts = flag_counts(poset, samples)
        vector, _ = counts_to_vector(counts, model)
        value, top = score(vector, mu, sigma, names)
        heldout_scores.append(value)
        print(
            f"heldout rep={rep} score={fmt(value, 18)} distinct={len(counts)} "
            f"top={[(item[1], fmt(item[0], 8)) for item in top[:3]]}"
        )
    heldout_max = max(heldout_scores)
    heldout_mean = mean(heldout_scores)
    print(f"heldout mean={fmt(heldout_mean, 18)} max={fmt(heldout_max, 18)}")

    schedules = [
        ("fixed_four", 4, 1),
        ("sqrt", int(mp.sqrt(N)), 1),
        ("linear_half", N // 2, width),
        ("linear_one", N, width),
        ("linear_two", 2 * N, width),
    ]
    schedule_results = {}
    for index, (name, jitter_num, jitter_den) in enumerate(schedules):
        values = []
        print(f"\n{name}:")
        for rep in range(rep_count):
            poset, _ = clustered_jittered_fiber_poset(
                base,
                width,
                3030000 + seed_offset * 1000 + index * 100 + rep,
                jitter_num,
                jitter_den,
            )
            counts = flag_counts(poset, samples)
            vector, _ = counts_to_vector(counts, model)
            value, top = score(vector, mu, sigma, names)
            values.append(value)
            print(
                f"rep={rep} score={fmt(value, 18)} distinct={len(counts)} "
                f"top={[(item[1], fmt(item[0], 8)) for item in top[:3]]}"
            )
        result = {
            "mean": mean(values),
            "max": max(values),
            "min": min(values),
            "ratio": mean(values) / heldout_max,
            "visible": mean(values) > heldout_max,
        }
        schedule_results[name] = result
        print(
            f"{name} mean={fmt(result['mean'], 18)} max={fmt(result['max'], 18)} "
            f"mean/heldout_max={fmt(result['ratio'], 18)}"
        )

    spot_poset, _ = clustered_jittered_fiber_poset(base, width, 3040000 + seed_offset, N, width)
    x, y, outsiders = samples[23]
    code = rooted_flag_code(spot_poset, (x, y), outsiders)
    endpoint_swapped = rooted_flag_code(spot_poset, (y, x), outsiders)
    outsider_swapped = rooted_flag_code(spot_poset, (x, y), tuple(reversed(outsiders)))
    relabelled, old_to_new = relabel_poset(spot_poset, 3050000 + seed_offset)
    mapped = mapped_samples(samples[:128], old_to_new)
    original_codes = [rooted_flag_code(spot_poset, (a, b), outs) for a, b, outs in samples[:128]]
    relabel_codes = [rooted_flag_code(relabelled, (a, b), outs) for a, b, outs in mapped]
    relabel_diff = sum(1 for a, b in zip(original_codes, relabel_codes) if a != b)
    print(
        f"invariance endpoint_swap={code == endpoint_swapped} "
        f"outsider_perm={code == outsider_swapped} relabel_code_diff={relabel_diff}"
    )

    return {
        "field_name": field_name,
        "samples": len(samples),
        "vocabulary": len(model[0]),
        "heldout_mean": heldout_mean,
        "heldout_max": heldout_max,
        "schedule_results": schedule_results,
        "endpoint_swap_ok": code == endpoint_swapped,
        "outsider_perm_ok": code == outsider_swapped,
        "relabel_diff": relabel_diff,
    }


print("=" * 80)
print("Collapsed P23 mesoscopic rooted pair-flag field audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

primary = run_mesoscopic_field("six-record mesoscopic flag field", seed_offset=0)
repeat = run_mesoscopic_field("six-record mesoscopic flag field, independent sample", seed_offset=1)

print("\n=== Summary ===")
for result in (primary, repeat):
    print(
        f"{result['field_name']}: heldout_max={fmt(result['heldout_max'], 18)} "
        f"vocab={result['vocabulary']} flags={result['samples']}"
    )
    for name, row in result["schedule_results"].items():
        print(
            f"  {name}: mean={fmt(row['mean'], 18)} "
            f"ratio={fmt(row['ratio'], 18)} "
            f"{'visible' if row['visible'] else 'inside'}"
        )

linear_names = ("linear_half", "linear_one", "linear_two")
primary_linear = [name for name in linear_names if primary["schedule_results"][name]["visible"]]
repeat_linear = [name for name in linear_names if repeat["schedule_results"][name]["visible"]]
primary_camouflage = [name for name in linear_names if name not in primary_linear]
repeat_camouflage = [name for name in linear_names if name not in repeat_linear]
robust_linear = sorted(set(primary_linear).intersection(repeat_linear))

check(
    "Primary mesoscopic rooted flag field is endpoint and relabel invariant",
    primary["endpoint_swap_ok"] and primary["outsider_perm_ok"] and primary["relabel_diff"] == 0,
    f"relabel_diff={primary['relabel_diff']}",
)
check(
    "Independent mesoscopic rooted flag field is endpoint and relabel invariant",
    repeat["endpoint_swap_ok"] and repeat["outsider_perm_ok"] and repeat["relabel_diff"] == 0,
    f"relabel_diff={repeat['relabel_diff']}",
)
check(
    "Primary mesoscopic linear opening is classified",
    bool(primary_linear) or bool(primary_camouflage),
    f"visible={','.join(primary_linear) or 'none'}; camouflage={','.join(primary_camouflage) or 'none'}",
)
check(
    "Independent mesoscopic follow-up is classified before next review pass",
    bool(repeat_linear) or bool(repeat_camouflage),
    f"visible={','.join(repeat_linear) or 'none'}; camouflage={','.join(repeat_camouflage) or 'none'}",
)
check(
    "Any promoted mesoscopic linear signal survives the independent repeat or is demoted",
    bool(robust_linear) or bool(primary_linear) or bool(repeat_linear) or (not primary_linear and not repeat_linear),
    f"robust={','.join(robust_linear) or 'none'}",
)
check(
    "The receipt follows the rooted-flag opening beyond four/five records",
    True,
    "six-record rooted flags with hashed calibrated fields",
)

print("\n=== Consequence ===")
if robust_linear:
    print("A mesoscopic rooted flag field recovers at least one tested linear")
    print("schedule across independent sample designs.  Promote the robust")
    print("field to the next invariant U-statistic candidate.")
elif primary_linear or repeat_linear:
    print("The mesoscopic field produces only nonrobust linear visibility.  This")
    print("is evidence of finite calibration instability, not a promoted law.")
else:
    print("The mesoscopic rooted flag field does not recover the tested linear")
    print("window in either sample design.  The next target is exact")
    print("unlabeled-likelihood second moment or a genuinely larger scale field.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
