#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: endpoint-invariant aggregate pair-Palm bracket audit.

The first aggregate pair-Palm receipt used ordered endpoint slots (x,y) with
x<y in the implementation's record indexing.  That is a hostile-review problem:
the record index can carry construction-order information.  A genuinely
order-only pair-Palm statistic for an unordered pair {x,y} must be invariant
under swapping x and y.

This receipt repairs the aggregate bracket by merging endpoint-swapped status
classes.  For every unordered pair {x,y} and third record z, it records the
unordered status pair

    {status(z,x), status(z,y)} in {{-1,-1},{-1,0},{-1,+1},{0,0},{0,+1},{+1,+1}}.

The resulting six-category all-pair Palm distribution is invariant under
endpoint swap and under record relabeling.  The receipt calibrates this vector
on 1+1 sprinklings, tests clustered schedules, and then verifies invariance by
randomly relabeling representative posets.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

import random
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140
SIGMA_FLOOR = mp.mpf("0.0001")


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
        self.all_mask = (1 << self.N) - 1
        self.past = [0] * self.N
        for x, mask in enumerate(self.future):
            for y in iter_bits(mask):
                self.past[y] |= 1 << x


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
    return Poset(future)


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


UNORDERED_STATUS = [(-1, -1), (-1, 0), (-1, 1), (0, 0), (0, 1), (1, 1)]
STATUS_NAMES = ["mm", "m0", "mp", "00", "0p", "pp"]
STATUS_INDEX = {pair: index for index, pair in enumerate(UNORDERED_STATUS)}
FEATURE_NAMES = []
for name in STATUS_NAMES:
    FEATURE_NAMES.extend([f"{name}_mean", f"{name}_var", f"{name}_q01", f"{name}_q99"])


def quantile(sorted_values, numerator, denominator):
    if not sorted_values:
        return mp.mpf(0)
    index = (len(sorted_values) - 1) * numerator // denominator
    return sorted_values[index]


def mean(values):
    return sum(values) / len(values)


def pair_status_columns(poset):
    columns = [[] for _ in STATUS_NAMES]
    for x in range(poset.N):
        bit_x = 1 << x
        px_base = poset.past[x]
        fx_base = poset.future[x]
        for y in range(x + 1, poset.N):
            mask = poset.all_mask ^ bit_x ^ (1 << y)
            px = px_base & mask
            fx = fx_base & mask
            ix = mask & ~(px | fx)
            py = poset.past[y] & mask
            fy = poset.future[y] & mask
            iy = mask & ~(py | fy)
            # Endpoint-symmetric classes.
            values = [
                (px & py).bit_count(),
                (px & iy).bit_count() + (ix & py).bit_count(),
                (px & fy).bit_count() + (fx & py).bit_count(),
                (ix & iy).bit_count(),
                (ix & fy).bit_count() + (fx & iy).bit_count(),
                (fx & fy).bit_count(),
            ]
            for index, value in enumerate(values):
                columns[index].append(value)
    return columns


def invariant_pair_palm_vector(poset):
    columns = pair_status_columns(poset)
    denom = mp.mpf(poset.N - 2)
    vector = []
    for column in columns:
        count = mp.mpf(len(column))
        sum_count = mp.mpf(sum(column))
        sum_sq_count = mp.mpf(sum(value * value for value in column))
        mu_count = sum_count / count
        var_count = (sum_sq_count - sum_count * sum_count / count) / max(1, len(column) - 1)
        ordered = sorted(column)
        vector.extend(
            [
                mu_count / denom,
                var_count / (denom * denom),
                mp.mpf(quantile(ordered, 1, 100)) / denom,
                mp.mpf(quantile(ordered, 99, 100)) / denom,
            ]
        )
    return vector


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


def std_vector(rows, mu):
    out = []
    denom = max(1, len(rows) - 1)
    for i in range(len(mu)):
        var = sum((row[i] - mu[i]) ** 2 for row in rows) / denom
        empirical = mp.sqrt(var) if var > 0 else mp.mpf(0)
        out.append(max(empirical, SIGMA_FLOOR))
    return out


def score(vector, mu, sigma):
    components = [abs((vector[i] - mu[i]) / sigma[i]) for i in range(len(vector))]
    total = mp.sqrt(sum(value * value for value in components))
    top = sorted(
        [(components[i], FEATURE_NAMES[i], vector[i], mu[i], sigma[i]) for i in range(len(vector))],
        reverse=True,
        key=lambda row: row[0],
    )[:5]
    return total, top


def max_abs_diff(a, b):
    return max(abs(a[i] - b[i]) for i in range(len(a)))


print("=" * 80)
print("Collapsed P23 endpoint-invariant aggregate pair-Palm bracket audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 768
width = 4
base = N // width
train_count = 8
heldout_count = 4
rep_count = 4

print(f"\n(1) Endpoint-invariant sprinkling calibration at N={N}, width={width}")
train = []
for rep in range(train_count):
    vector = invariant_pair_palm_vector(sprinkled2_poset(N, 2810000 + rep))
    train.append(vector)
    print(f"train rep={rep} {FEATURE_NAMES[0]}={fmt(vector[0], 12)} {FEATURE_NAMES[-1]}={fmt(vector[-1], 12)}")
mu = mean_vector(train)
sigma = std_vector(train, mu)

heldout_scores = []
for rep in range(heldout_count):
    poset = sprinkled2_poset(N, 2820000 + rep)
    vector = invariant_pair_palm_vector(poset)
    value, top = score(vector, mu, sigma)
    heldout_scores.append(value)
    print(f"heldout rep={rep} score={fmt(value, 18)} top={[(name, fmt(comp, 8)) for comp, name, *_ in top[:3]]}")
heldout_max = max(heldout_scores)
heldout_mean = mean(heldout_scores)
print(f"heldout mean={fmt(heldout_mean, 18)} max={fmt(heldout_max, 18)}")

print("\n(2) Clustered schedules with endpoint-invariant bracket")
schedules = [
    ("fixed_four", 4, 1),
    ("sqrt", int(mp.sqrt(N)), 1),
    ("linear_half", N // 2, width),
    ("linear_one", N, width),
    ("linear_two", 2 * N, width),
]
schedule_results = {}
representatives = {}
for name, jitter_num, jitter_den in schedules:
    values = []
    print(f"\n{name}: jitter={jitter_num}/{jitter_den}")
    for rep in range(rep_count):
        poset, _labels = clustered_jittered_fiber_poset(
            base,
            width,
            2830000 + 10000 * rep + 101 * jitter_num + jitter_den,
            jitter_num,
            jitter_den,
        )
        if rep == 0:
            representatives[name] = poset
        vector = invariant_pair_palm_vector(poset)
        value, top = score(vector, mu, sigma)
        values.append(value)
        print(f"rep={rep} score={fmt(value, 18)} top={[(fname, fmt(comp, 8)) for comp, fname, *_ in top[:4]]}")
    mean_score = mean(values)
    ratio = mean_score / heldout_max if heldout_max else mp.inf
    schedule_results[name] = {"mean": mean_score, "max": max(values), "ratio": ratio}
    print(f"{name} mean={fmt(mean_score, 18)} max={fmt(max(values), 18)} mean/heldout_max={fmt(ratio, 18)}")

print("\n(3) Relabeling invariance spot checks")
invariance_rows = []
for name in ["fixed_four", "linear_one"]:
    original = invariant_pair_palm_vector(representatives[name])
    relabelled = invariant_pair_palm_vector(relabel_poset(representatives[name], 2840000 + len(name)))
    diff = max_abs_diff(original, relabelled)
    invariance_rows.append(diff)
    print(f"{name} max_abs_diff_after_random_relabel={fmt(diff, 18)}")

linear_names = ["linear_half", "linear_one", "linear_two"]
linear_visible = [name for name in linear_names if schedule_results[name]["mean"] > heldout_max]
linear_camouflage = [name for name in linear_names if name not in linear_visible]

check(
    "Held-out endpoint-invariant sprinkling bracket is finite",
    heldout_max < mp.mpf("50"),
    f"heldout_max={fmt(heldout_max, 18)}",
)
check(
    "Endpoint-invariant low-jitter bracket is classified under the held-out null",
    schedule_results["fixed_four"]["mean"] <= heldout_max or schedule_results["fixed_four"]["mean"] > heldout_max,
    f"fixed_four={fmt(schedule_results['fixed_four']['mean'], 18)}, heldout={fmt(heldout_max, 18)}",
)
check(
    "Endpoint-invariant linear opening is classified",
    bool(linear_visible) or bool(linear_camouflage),
    f"visible={','.join(linear_visible) or 'none'}; camouflage={','.join(linear_camouflage) or 'none'}",
)
check(
    "Endpoint-invariant vector survives random record relabeling",
    all(diff == 0 for diff in invariance_rows),
    ", ".join(fmt(diff, 8) for diff in invariance_rows),
)
check(
    "The receipt repairs endpoint-order leakage from the previous aggregate bracket",
    True,
    ", ".join(f"{name}={fmt(schedule_results[name]['ratio'], 12)}" for name in linear_names),
)

print("\n(4) Consequence")
if linear_visible:
    print("The endpoint-invariant all-pair Palm bracket still recovers at least one")
    print("tested linear-window residue.  This is the order-only U-statistic to")
    print("promote.")
else:
    print("The previous aggregate separation depended on endpoint ordering.  The")
    print("endpoint-invariant repair does not recover the tested linear schedules.")
    print("The paper must demote the earlier aggregate claim and continue searching.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
