#!/usr/bin/env python3
"""
Paper 26 receipt: quadratic record-action audit.

This receipt imports one idea from finite-action/quadratic-gravity thinking:
mean defects can cancel, but squared defects cannot.  It builds a finite,
order-only quadratic action from calibrated sprinkling features:

  - relation density;
  - height ratio;
  - three interval Laplace samples P_alpha;
  - interval-shape/Weyl proxy: mean squared deviation of internal interval
    relation density from the 1+1 sprinkling value 1/2;
  - near-external-twin tail.

The receipt tests the action on gross non-manifold adversaries and on the
linear-jitter clustered adversary that earlier Paper 23 receipts found hard.
It is a finite stress test, not a continuum action.

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
        self.outdeg = tuple(mask.bit_count() for mask in self.future)
        self.indeg = tuple(mask.bit_count() for mask in self.past)

    def relation_count(self):
        return sum(self.outdeg)

    def height(self):
        memo = [0] * self.N

        def depth(x):
            if memo[x]:
                return memo[x]
            best = 1
            for y in iter_bits(self.future[x]):
                best = max(best, 1 + depth(y))
            memo[x] = best
            return best

        return max(depth(x) for x in range(self.N)) if self.N else 0


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
    return poset_from_permutation(perm)


def chain_poset(n):
    return Poset([sum(1 << j for j in range(i + 1, n)) for i in range(n)])


def antichain_poset(n):
    return Poset([0] * n)


def layered_poset(sizes):
    offsets = []
    total = 0
    for size in sizes:
        offsets.append(total)
        total += size
    future = [0] * total
    for layer, start in enumerate(offsets):
        end = start + sizes[layer]
        mask = 0
        for later_start, later_size in zip(offsets[layer + 1 :], sizes[layer + 1 :]):
            for y in range(later_start, later_start + later_size):
                mask |= 1 << y
        for x in range(start, end):
            future[x] = mask
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


def clustered_jittered_fiber_poset(base_n, width, seed, jitter_num, jitter_den):
    rng = random.Random(seed)
    perm = list(range(base_n))
    rng.shuffle(perm)
    scale = 10000 * jitter_den
    span = 10000 * jitter_num
    points = []
    for i, vi in enumerate(perm):
        for local in range(width):
            du = rng.randint(-span, span) if span else 0
            dv = rng.randint(-span, span) if span else 0
            u = i * scale + width * du + local
            v = vi * scale + width * dv + (width - 1 - local)
            points.append((u, v))
    return coordinate_order_poset(points)


def external_delta(poset, x, y):
    clear_x = ~(1 << x)
    clear_y = ~(1 << y)
    diff = ((poset.past[x] & clear_y) ^ (poset.past[y] & clear_x)).bit_count()
    diff += ((poset.future[x] & clear_y) ^ (poset.future[y] & clear_x)).bit_count()
    return diff


def interval_internal_relation_density(poset, mask):
    m = mask.bit_count()
    if m < 2:
        return None
    rel = 0
    for x in iter_bits(mask):
        rel += (poset.future[x] & mask).bit_count()
    return mp.mpf(rel) / (mp.mpf(m) * (m - 1) / 2)


FEATURE_NAMES = [
    "relation_density",
    "height_ratio",
    "P_alpha_0.25",
    "P_alpha_1",
    "P_alpha_4",
    "interval_weyl_proxy",
    "near_twin_tail_4",
]


def feature_vector(poset):
    n = poset.N
    pair_count = mp.mpf(n) * (n - 1) / 2
    relation_density = mp.mpf(poset.relation_count()) / pair_count
    height_ratio = mp.mpf(poset.height()) / (2 * mp.sqrt(n))

    p_alpha = {mp.mpf("0.25"): mp.mpf(0), mp.mpf("1"): mp.mpf(0), mp.mpf("4"): mp.mpf(0)}
    weyl_terms = []
    for x in range(n):
        for y in iter_bits(poset.future[x]):
            interval = poset.future[x] & poset.past[y]
            m = interval.bit_count()
            for alpha in p_alpha:
                p_alpha[alpha] += mp.e ** (-alpha * m) / n
            if m >= 4:
                rho = interval_internal_relation_density(poset, interval)
                if rho is not None:
                    weyl_terms.append((rho - mp.mpf("0.5")) ** 2)
    interval_weyl = mp.fsum(weyl_terms) / len(weyl_terms) if weyl_terms else mp.mpf(0)

    near_twins = 0
    for x in range(n):
        for y in range(x + 1, n):
            if external_delta(poset, x, y) <= 4:
                near_twins += 1
    near_twin_tail = mp.mpf(near_twins) / pair_count

    return [
        relation_density,
        height_ratio,
        p_alpha[mp.mpf("0.25")],
        p_alpha[mp.mpf("1")],
        p_alpha[mp.mpf("4")],
        interval_weyl,
        near_twin_tail,
    ]


def mean(values):
    return mp.fsum(values) / len(values)


def std(values):
    mu = mean(values)
    return mp.sqrt(mp.fsum((value - mu) ** 2 for value in values) / (len(values) - 1))


def calibrate(rows):
    cols = list(zip(*rows))
    means = [mean(col) for col in cols]
    sigmas = [std(col) for col in cols]
    return means, sigmas


def z_vector(vec, means, sigmas):
    out = []
    for value, mu, sigma in zip(vec, means, sigmas):
        if sigma == 0:
            out.append(mp.mpf(0))
        else:
            out.append((value - mu) / sigma)
    return out


def quadratic_action(zs):
    return mp.fsum(z * z for z in zs)


print("=" * 80)
print("Paper 26 quadratic record-action audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 72
null_reps = 48
heldout_reps = 12
print(f"N={n} null_reps={null_reps} heldout_reps={heldout_reps}")

null_rows = [feature_vector(sprinkled2_poset(n, 100000 + i)) for i in range(null_reps)]
means, sigmas = calibrate(null_rows)
print("\nCalibration")
for name, mu, sigma in zip(FEATURE_NAMES, means, sigmas):
    print(f"  {name}: mean={fmt(mu, 18)} std={fmt(sigma, 18)}")

heldout_actions = []
for i in range(heldout_reps):
    vec = feature_vector(sprinkled2_poset(n, 200000 + i))
    action = quadratic_action(z_vector(vec, means, sigmas))
    heldout_actions.append(action)
heldout_max = max(heldout_actions)
heldout_mean = mean(heldout_actions)
print(f"\nHeldout sprinkling action mean={fmt(heldout_mean, 18)} max={fmt(heldout_max, 18)}")

adversaries = {
    "chain": chain_poset(n),
    "antichain": antichain_poset(n),
    "three_layer_KR": layered_poset([n // 4, n // 2, n - n // 4 - n // 2]),
    "six_staged_blocks": layered_poset([n // 6] * 6),
    "cluster_fixed": clustered_jittered_fiber_poset(n // 2, 2, 300000, 2, 1),
    "cluster_linear_half": clustered_jittered_fiber_poset(n // 2, 2, 300001, n // 2, 2),
    "cluster_linear_one": clustered_jittered_fiber_poset(n // 2, 2, 300002, n, 2),
}

results = {}
print("\nAdversaries")
for name, poset in adversaries.items():
    vec = feature_vector(poset)
    zs = z_vector(vec, means, sigmas)
    action = quadratic_action(zs)
    results[name] = (vec, zs, action)
    top = sorted(zip(FEATURE_NAMES, zs), reverse=True, key=lambda row: abs(row[1]))[:3]
    print(f"  {name}: action={fmt(action, 18)} top_z={[ (k, fmt(v, 8)) for k, v in top ]}")

chain_z = results["chain"][1]
anti_z = results["antichain"][1]
rel_idx = FEATURE_NAMES.index("relation_density")
w = -anti_z[rel_idx] / (chain_z[rel_idx] - anti_z[rel_idx])
linear_cancel = w * chain_z[rel_idx] + (1 - w) * anti_z[rel_idx]
quadratic_mixture = w * results["chain"][2] + (1 - w) * results["antichain"][2]
print("\nLinear-cancellation check")
print(
    f"  weight_chain={fmt(w, 18)} relation_linear_mix={fmt(linear_cancel, 18)} "
    f"quadratic_mixture={fmt(quadratic_mixture, 18)}"
)

gross_names = ["chain", "antichain", "three_layer_KR", "six_staged_blocks"]
gross_min = min(results[name][2] for name in gross_names)
linear_half_action = results["cluster_linear_half"][2]
linear_one_action = results["cluster_linear_one"][2]

check(
    "Heldout sprinklings have finite calibrated quadratic action",
    heldout_max < mp.mpf("80"),
    f"heldout_max={fmt(heldout_max, 12)}",
)
check(
    "Gross non-manifold adversaries are strongly penalized",
    gross_min > 10 * heldout_max,
    f"gross_min={fmt(gross_min, 12)} heldout_max={fmt(heldout_max, 12)}",
)
check(
    "Linear relation-density cancellation leaves large quadratic action",
    abs(linear_cancel) < mp.mpf("1e-80") and quadratic_mixture > 10 * heldout_max,
    f"quadratic_mixture={fmt(quadratic_mixture, 12)}",
)
check(
    "Linear-jitter clustered schedules are not falsely promoted as solved",
    linear_half_action < gross_min and linear_one_action < gross_min,
    f"half={fmt(linear_half_action, 12)} one={fmt(linear_one_action, 12)} gross_min={fmt(gross_min, 12)}",
)
check(
    "Interval Weyl proxy participates in at least one gross rejection",
    max(abs(results[name][1][FEATURE_NAMES.index("interval_weyl_proxy")]) for name in gross_names)
    > mp.mpf("5"),
    "",
)

print("\n=== Consequence ===")
print("A quadratic record action catches gross non-manifold/staged orders and")
print("prevents simple signed-defect cancellation.  It does not by itself solve")
print("the washed-out linear-jitter adversary; that remains a full-law/selected")
print("likelihood problem.  This is compatible with the quadratic-gravity lesson:")
print("use finite squared defects as a selection principle, but do not confuse")
print("a finite projection with the record law.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
