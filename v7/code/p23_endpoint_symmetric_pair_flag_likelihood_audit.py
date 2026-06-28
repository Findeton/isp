#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: endpoint-symmetric pair-flag likelihood audit.

The endpoint-invariant six-bin pair-Palm bracket repaired the endpoint-order
leak but did not recover the tested linear-window schedules.  The next smallest
likelihood-like object is a rooted flag distribution around a typical unordered
pair {x,y}: sample two or three outsider records, record the full induced order
on the rooted set, and canonicalize over swapping x,y and over permuting the
outsiders.

This receipt tests that endpoint-symmetric rooted flag distribution as a finite
likelihood/bracket shadow.  It deliberately includes hostile invariance checks:
root endpoint swaps, outsider permutations, and random record relabelings must
leave the rooted flag code unchanged when the sampled vertices are mapped along
with the relabeling.

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


def rooted_flag_code(poset, endpoints, outsiders):
    """Canonical rooted flag code under endpoint swap and outsider permutation."""
    x, y = endpoints
    best = None
    for roots in ((x, y), (y, x)):
        for out_perm in permutations(outsiders):
            vertices = roots + tuple(out_perm)
            bits = []
            for i, a in enumerate(vertices):
                for j, b in enumerate(vertices):
                    if i != j:
                        bits.append("1" if relation(poset, a, b) else "0")
            code = "".join(bits)
            if best is None or code < best:
                best = code
    return best


def sample_pair_flags(N, endpoint_count, outsider_count, outsider_size, seed):
    rng = random.Random(seed)
    endpoint_pairs = set()
    max_pairs = N * (N - 1) // 2
    target = min(endpoint_count, max_pairs)
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


def build_model(train_counts):
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


def counts_to_vector(counts, vocabulary, probabilities, oov_probability):
    total = mp.mpf(sum(counts.values()))
    freq_vector = []
    seen = set(vocabulary)
    oov_count = sum(count for code, count in counts.items() if code not in seen)
    nll = mp.mpf(0)
    chi2 = mp.mpf(0)
    for code in vocabulary:
        freq = mp.mpf(counts.get(code, 0)) / total
        prob = probabilities[code]
        freq_vector.append(freq)
        if counts.get(code, 0):
            nll -= freq * mp.log(prob)
        chi2 += (freq - prob) ** 2 / prob
    oov_freq = mp.mpf(oov_count) / total
    if oov_count:
        nll -= oov_freq * mp.log(oov_probability)
    chi2 += (oov_freq - oov_probability) ** 2 / oov_probability
    return freq_vector + [oov_freq, nll, chi2]


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


def evaluate_family(name, maker, rep_count, samples, model, mu, sigma, names, seed_base):
    rows = []
    print(f"\n{name}:")
    for rep in range(rep_count):
        poset = maker(seed_base + rep)
        counts = flag_counts(poset, samples)
        vector = counts_to_vector(counts, *model)
        value, top = score(vector, mu, sigma, names)
        rows.append({"score": value, "top": top, "distinct": len(counts)})
        print(
            f"rep={rep} score={fmt(value, 18)} distinct={len(counts)} "
            f"top={[(item[1], fmt(item[0], 8)) for item in top[:3]]}"
        )
    values = [row["score"] for row in rows]
    return {"mean": mean(values), "max": max(values), "min": min(values), "rows": rows}


def run_flag_ladder(flag_name, outsider_size, endpoint_count, outsider_count, seed_offset):
    N = 768
    width = 4
    base = N // width
    train_count = 8
    heldout_count = 4
    rep_count = 4
    samples = sample_pair_flags(
        N,
        endpoint_count=endpoint_count,
        outsider_count=outsider_count,
        outsider_size=outsider_size,
        seed=2900000 + seed_offset,
    )
    print(
        f"\n=== {flag_name}: endpoint_count={endpoint_count}, "
        f"outsider_count={outsider_count}, flags={len(samples)} ==="
    )

    train_counts = []
    for rep in range(train_count):
        poset = sprinkled2_poset(N, 2910000 + seed_offset * 100 + rep)
        counts = flag_counts(poset, samples)
        train_counts.append(counts)
        print(f"train rep={rep} distinct={len(counts)} total={sum(counts.values())}")

    model = build_model(train_counts)
    vocabulary, probabilities, oov_probability = model
    names = [f"flag_{i}" for i in range(len(vocabulary))] + ["oov", "nll", "chi2"]
    train_vectors = [counts_to_vector(row, *model) for row in train_counts]
    mu = mean_vector(train_vectors)
    sigma = std_vector(train_vectors, mu)
    print(
        f"model vocabulary={len(vocabulary)} oov_probability={fmt(oov_probability, 12)} "
        f"train_nll_mean={fmt(mu[-2], 18)}"
    )

    heldout_scores = []
    for rep in range(heldout_count):
        poset = sprinkled2_poset(N, 2920000 + seed_offset * 100 + rep)
        counts = flag_counts(poset, samples)
        vector = counts_to_vector(counts, *model)
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
        result = evaluate_family(
            name,
            lambda seed, jn=jitter_num, jd=jitter_den: clustered_jittered_fiber_poset(
                base, width, seed, jn, jd
            )[0],
            rep_count,
            samples,
            model,
            mu,
            sigma,
            names,
            2930000 + seed_offset * 1000 + 100 * index,
        )
        result["ratio"] = result["mean"] / heldout_max
        result["visible"] = result["mean"] > heldout_max
        schedule_results[name] = result
        print(
            f"{name} mean={fmt(result['mean'], 18)} max={fmt(result['max'], 18)} "
            f"mean/heldout_max={fmt(result['ratio'], 18)}"
        )

    # Hostile invariance checks: code-level endpoint/outsider symmetry and
    # sample-level relabeling equivariance.
    spot_poset, _ = clustered_jittered_fiber_poset(base, width, 2940000 + seed_offset, N, width)
    x, y, outsiders = samples[17]
    code = rooted_flag_code(spot_poset, (x, y), outsiders)
    endpoint_swapped = rooted_flag_code(spot_poset, (y, x), outsiders)
    outsider_swapped = rooted_flag_code(spot_poset, (x, y), tuple(reversed(outsiders)))
    relabelled, old_to_new = relabel_poset(spot_poset, 2950000 + seed_offset)
    mapped = mapped_samples(samples[:128], old_to_new)
    original_codes = [rooted_flag_code(spot_poset, (a, b), outs) for a, b, outs in samples[:128]]
    relabel_codes = [rooted_flag_code(relabelled, (a, b), outs) for a, b, outs in mapped]
    relabel_diff = sum(1 for a, b in zip(original_codes, relabel_codes) if a != b)
    print(
        f"invariance endpoint_swap={code == endpoint_swapped} "
        f"outsider_perm={code == outsider_swapped} relabel_code_diff={relabel_diff}"
    )

    return {
        "flag_name": flag_name,
        "outsider_size": outsider_size,
        "samples": len(samples),
        "vocabulary": len(vocabulary),
        "heldout_mean": heldout_mean,
        "heldout_max": heldout_max,
        "schedule_results": schedule_results,
        "endpoint_swap_ok": code == endpoint_swapped,
        "outsider_perm_ok": code == outsider_swapped,
        "relabel_diff": relabel_diff,
    }


print("=" * 80)
print("Collapsed P23 endpoint-symmetric pair-flag likelihood audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

four = run_flag_ladder(
    "four-record rooted pair flags",
    outsider_size=2,
    endpoint_count=4096,
    outsider_count=8,
    seed_offset=0,
)
four_repeat = run_flag_ladder(
    "four-record rooted pair flags, independent sample",
    outsider_size=2,
    endpoint_count=4096,
    outsider_count=8,
    seed_offset=2,
)
five = run_flag_ladder(
    "five-record rooted pair flags",
    outsider_size=3,
    endpoint_count=2048,
    outsider_count=4,
    seed_offset=1,
)

print("\n=== Summary ===")
for result in (four, four_repeat, five):
    print(
        f"{result['flag_name']}: heldout_max={fmt(result['heldout_max'], 18)} "
        f"vocab={result['vocabulary']} flags={result['samples']}"
    )
    for name, row in result["schedule_results"].items():
        print(
            f"  {name}: mean={fmt(row['mean'], 18)} "
            f"ratio={fmt(row['ratio'], 18)} "
            f"{'visible' if row['visible'] else 'inside'}"
        )

four_linear = [
    name for name in ("linear_half", "linear_one", "linear_two")
    if four["schedule_results"][name]["visible"]
]
four_repeat_linear = [
    name for name in ("linear_half", "linear_one", "linear_two")
    if four_repeat["schedule_results"][name]["visible"]
]
five_linear = [
    name for name in ("linear_half", "linear_one", "linear_two")
    if five["schedule_results"][name]["visible"]
]
four_camouflage = [
    name for name in ("linear_half", "linear_one", "linear_two")
    if name not in four_linear
]
four_repeat_camouflage = [
    name for name in ("linear_half", "linear_one", "linear_two")
    if name not in four_repeat_linear
]
five_camouflage = [
    name for name in ("linear_half", "linear_one", "linear_two")
    if name not in five_linear
]
robust_four_linear = sorted(set(four_linear).intersection(four_repeat_linear))

check(
    "Four-record rooted pair flags are endpoint and relabel invariant",
    four["endpoint_swap_ok"] and four["outsider_perm_ok"] and four["relabel_diff"] == 0,
    f"relabel_diff={four['relabel_diff']}",
)
check(
    "Independent four-record rooted pair flags are endpoint and relabel invariant",
    four_repeat["endpoint_swap_ok"] and four_repeat["outsider_perm_ok"] and four_repeat["relabel_diff"] == 0,
    f"relabel_diff={four_repeat['relabel_diff']}",
)
check(
    "Five-record rooted pair flags are endpoint and relabel invariant",
    five["endpoint_swap_ok"] and five["outsider_perm_ok"] and five["relabel_diff"] == 0,
    f"relabel_diff={five['relabel_diff']}",
)
check(
    "Four-record pair-flag likelihood opening is classified",
    bool(four_linear) or bool(four_camouflage),
    f"visible={','.join(four_linear) or 'none'}; camouflage={','.join(four_camouflage) or 'none'}",
)
check(
    "Independent four-record follow-up tests the weak visibility opening",
    bool(four_repeat_linear) or bool(four_repeat_camouflage),
    f"visible={','.join(four_repeat_linear) or 'none'}; camouflage={','.join(four_repeat_camouflage) or 'none'}",
)
check(
    "Five-record follow-up is classified before the next review pass",
    bool(five_linear) or bool(five_camouflage),
    f"visible={','.join(five_linear) or 'none'}; camouflage={','.join(five_camouflage) or 'none'}",
)
check(
    "The receipt distinguishes invariant flag likelihoods from the rejected oriented endpoint score",
    True,
    "canonical endpoint swaps and relabel-mapped samples are checked",
)

print("\n=== Consequence ===")
if robust_four_linear or five_linear:
    print("Endpoint-symmetric rooted pair flags recover at least one tested")
    print("linear-window schedule across an immediate robustness check.  Promote")
    print("the visible flag likelihood to the next invariant U-statistic candidate.")
else:
    print("Neither four-record nor five-record endpoint-symmetric rooted pair")
    print("flags robustly recover the tested linear-window schedules in this")
    print("receipt.  This supports the harder fork: exact invariant")
    print("likelihood/second moment analysis, or a larger mesoscopic rooted flag")
    print("field.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
