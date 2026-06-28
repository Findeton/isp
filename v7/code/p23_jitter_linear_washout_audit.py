#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: linear/superlinear jitter washout audit.

The exponent audit showed that fixed and square-root jitter schedules do not
give a clean universal boundary.  This receipt follows the next opening: if the
rank-mixing radius is genuinely linear or superlinear in N, does the hidden
cluster cease to be order-visible and collapse back into the ordinary sprinkling
poset law?

Notation in the paper:
  P_N          = 1+1 sprinkling order law at N records.
  Q_N(w, j)   = width-w jittered clustered coordinate order law.

The receipt compares Q_N against calibrated P_N shadows using exact full
three-record induced-pattern densities, global interval-profile features, and
rooted near-neighborhood features.  It is a finite washout audit, not an
asymptotic theorem.

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
        self.outdeg = [mask.bit_count() for mask in self.future]
        self.indeg = [mask.bit_count() for mask in self.past]

    def relation_count(self):
        return sum(self.outdeg)

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

    def interval_histogram(self):
        hist = [0] * self.N
        for x in range(self.N):
            for y in iter_bits(self.future[x]):
                hist[(self.future[x] & self.past[y]).bit_count()] += 1
        return hist


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


def exact_triple_counts(poset):
    N = poset.N
    relation_count = poset.relation_count()
    chain = sum(poset.indeg[y] * poset.outdeg[y] for y in range(N))

    future_relation_sum = 0
    for x in range(N):
        for y in iter_bits(poset.future[x]):
            future_relation_sum += poset.outdeg[y]
    vee = sum(f * (f - 1) // 2 for f in poset.outdeg) - future_relation_sum

    past_relation_sum = 0
    for z in range(N):
        for y in iter_bits(poset.past[z]):
            past_relation_sum += poset.indeg[y]
    wedge = sum(p * (p - 1) // 2 for p in poset.indeg) - past_relation_sum

    one_relation = relation_count * (N - 2) - 3 * chain - 2 * (vee + wedge)
    total = N * (N - 1) * (N - 2) // 6
    antichain = total - chain - vee - wedge - one_relation
    return {
        "antichain": antichain,
        "one_relation": one_relation,
        "vee": vee,
        "wedge": wedge,
        "chain": chain,
        "total": total,
    }


def exact_triple_densities(poset):
    counts = exact_triple_counts(poset)
    total = counts["total"]
    order = ["antichain", "one_relation", "vee", "wedge", "chain"]
    return [mp.mpf(counts[name]) / total for name in order], counts


def external_delta(poset, x, y):
    clear_x = ~(1 << x)
    clear_y = ~(1 << y)
    diff = ((poset.past[x] & clear_y) ^ (poset.past[y] & clear_x)).bit_count()
    diff += ((poset.future[x] & clear_y) ^ (poset.future[y] & clear_x)).bit_count()
    return diff


def rooted_near_features(poset, seed, root_count):
    rng = random.Random(seed)
    roots = rng.sample(range(poset.N), min(root_count, poset.N))
    tau = max(2, poset.N // 48)
    near_sum = mp.mpf(0)
    soft_sum = mp.mpf(0)
    min_sum = mp.mpf(0)
    for root in roots:
        deltas = [external_delta(poset, root, y) for y in range(poset.N) if y != root]
        near_sum += mp.mpf(sum(1 for delta in deltas if delta <= tau)) / poset.N
        soft_sum += sum(mp.e ** (-mp.mpf(delta) / (tau + 1)) for delta in deltas) / poset.N
        min_sum += mp.mpf(min(deltas)) / poset.N if deltas else mp.mpf(0)
    denom = len(roots)
    return [near_sum / denom, soft_sum / denom, min_sum / denom]


FEATURE_NAMES = [
    "r",
    "height_ratio",
    "p_log2_ratio",
    "tri_antichain",
    "tri_one_relation",
    "tri_vee",
    "tri_wedge",
    "tri_chain",
    "root_near",
    "root_soft",
    "root_min_delta",
]


def audit_vector(poset, seed):
    hist = poset.interval_histogram()
    expected = sprinkle_pair_density_expectation(poset.N, mp.log(2))
    observed = profile_P_from_hist_density(hist, poset.N, mp.log(2))
    triple, counts = exact_triple_densities(poset)
    vector = [
        poset.ordering_fraction(),
        height_scale_ratio(poset),
        observed / expected if expected else mp.mpf(0),
    ]
    vector.extend(triple)
    vector.extend(rooted_near_features(poset, seed, max(8, min(16, poset.N // 32))))
    return vector, counts


def mean_vector(rows):
    return [sum(row[i] for row in rows) / len(rows) for i in range(len(rows[0]))]


def std_vector(rows, mean):
    denom = max(1, len(rows) - 1)
    out = []
    for i in range(len(mean)):
        var = sum((row[i] - mean[i]) ** 2 for row in rows) / denom
        out.append(mp.sqrt(var))
    return out


def score_against(rows, candidate):
    mean = mean_vector(rows)
    std = std_vector(rows, mean)
    score = mp.mpf(0)
    components = []
    for name, value, mu, sigma in zip(FEATURE_NAMES, candidate, mean, std):
        ridge = max(abs(mu) * mp.mpf("0.02"), mp.mpf("1e-12"))
        denom = max(sigma, ridge)
        z = (value - mu) / denom
        score += z * z
        components.append((abs(z), name, z, value, mu, denom))
    components.sort(reverse=True, key=lambda item: item[0])
    return score, components


def same_label_observability(poset, labels):
    tau = max(2, poset.N // 48)
    count = 0
    near = 0
    delta_sum = mp.mpf(0)
    for x in range(poset.N):
        for y in range(x + 1, poset.N):
            if labels[x] != labels[y]:
                continue
            count += 1
            delta = external_delta(poset, x, y)
            delta_sum += mp.mpf(delta) / poset.N
            if delta <= tau:
                near += 1
    return {
        "pair_mass": mp.mpf(count) / (poset.N * (poset.N - 1) // 2),
        "same_near": mp.mpf(near) / count if count else mp.mpf(0),
        "same_delta": delta_sum / count if count else mp.mpf(0),
    }


def phase_name(score_ratio, same_near):
    if score_ratio > 10:
        return "separated"
    if score_ratio > 1:
        return "visible"
    if same_near > mp.mpf("0.25"):
        return "camouflage-with-near-labels"
    return "finite-camouflage"


print("=" * 80)
print("Collapsed P23 linear/superlinear jitter washout audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

Ns = [192, 384, 768]
widths = [2, 4, 8]
sprinkling_count = 5


def schedule_effective(label, N):
    N = mp.mpf(N)
    if label == "fixed_4":
        return 4
    if label == "sqrt_two":
        return max(1, int(mp.nint(2 * mp.sqrt(N))))
    if label == "linear_24":
        return max(1, int(mp.nint(N / 24)))
    if label == "linear_12":
        return max(1, int(mp.nint(N / 12)))
    if label == "linear_6":
        return max(1, int(mp.nint(N / 6)))
    if label == "linear_3":
        return max(1, int(mp.nint(N / 3)))
    if label == "linear_1":
        return max(1, int(mp.nint(N)))
    if label == "super_2":
        return max(1, int(mp.nint(2 * N)))
    raise ValueError(label)


schedule_labels = [
    "fixed_4",
    "sqrt_two",
    "linear_24",
    "linear_12",
    "linear_6",
    "linear_3",
    "linear_1",
    "super_2",
]

all_results = []
partition_ok = True
calibration_by_N = {}

for N in Ns:
    print(f"\n(1) Calibrating sprinkling null at N={N}")
    sprinkling_rows = []
    holdout_rows = []
    for index in range(sprinkling_count):
        poset = sprinkled2_poset(N, 1310000 + 1000 * N + index)
        row, counts = audit_vector(poset, 1320000 + 1000 * N + index)
        partition_ok = partition_ok and sum(
            counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]
        ) == counts["total"]
        sprinkling_rows.append(row)
    for index in range(2):
        poset = sprinkled2_poset(N, 1330000 + 1000 * N + index)
        row, counts = audit_vector(poset, 1340000 + 1000 * N + index)
        partition_ok = partition_ok and sum(
            counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]
        ) == counts["total"]
        holdout_rows.append(row)
    holdout_scores = [score_against(sprinkling_rows, row)[0] for row in holdout_rows]
    holdout_max = max(holdout_scores)
    calibration_by_N[N] = {
        "rows": sprinkling_rows,
        "holdout_scores": holdout_scores,
        "holdout_max": holdout_max,
    }
    print("holdout scores =", [fmt(score, 12) for score in holdout_scores])

for width in widths:
    print(f"\n(2) Testing clustered coordinate laws under linear/superlinear mixing, w={width}")
    for N in Ns:
        scale_result = {
            "width": width,
            "N": N,
            "holdout_max": calibration_by_N[N]["holdout_max"],
            "candidates": [],
        }
        print(f"\nN={N}, w={width}")
        for label in schedule_labels:
            effective_int = schedule_effective(label, N)
            jitter_num = effective_int
            jitter_den = width
            candidate, labels = clustered_jittered_fiber_poset(
                N // width,
                width,
                18000 + 17 * N + 311 * width + 29 * effective_int,
                jitter_num,
                jitter_den,
            )
            row, counts = audit_vector(candidate, 1350000 + 1000 * N + 37 * width + effective_int)
            partition_ok = partition_ok and sum(
                counts[name] for name in ["antichain", "one_relation", "vee", "wedge", "chain"]
            ) == counts["total"]
            score, components = score_against(calibration_by_N[N]["rows"], row)
            observable = same_label_observability(candidate, labels)
            score_ratio = score / calibration_by_N[N]["holdout_max"]
            effective = mp.mpf(width) * mp.mpf(jitter_num) / mp.mpf(jitter_den)
            scaled_sqrt = effective / mp.sqrt(N)
            scaled_linear = effective / N
            top = ", ".join(f"{name}:z={fmt(z, 6)}" for _, name, z, *_ in components[:3])
            phase = phase_name(score_ratio, observable["same_near"])
            print(
                f"{label:>10} eff={fmt(effective, 8)} eff/sqrtN={fmt(scaled_sqrt, 8)} "
                f"eff/N={fmt(scaled_linear, 8)} ratio={fmt(score_ratio, 18)} "
                f"same_near={fmt(observable['same_near'], 18)} "
                f"same_delta={fmt(observable['same_delta'], 18)} phase={phase} top=[{top}]"
            )
            scale_result["candidates"].append(
                {
                    "label": label,
                    "effective": effective,
                    "scaled_sqrt": scaled_sqrt,
                    "scaled_linear": scaled_linear,
                    "score": score,
                    "score_ratio": score_ratio,
                    "same_near": observable["same_near"],
                    "same_delta": observable["same_delta"],
                    "phase": phase,
                    "top": components[:3],
                }
            )
        all_results.append(scale_result)

print("\n(3) Washout table")
for result in all_results:
    print(f"N={result['N']}, w={result['width']}:")
    for candidate in result["candidates"]:
        print(
            f"  {candidate['label']:>10} eff={fmt(candidate['effective'], 6):>8} "
            f"eff/sqrtN={fmt(candidate['scaled_sqrt'], 6):>10} "
            f"ratio={fmt(candidate['score_ratio'], 10):>14} "
            f"same_near={fmt(candidate['same_near'], 8):>12} "
            f"phase={candidate['phase']}"
        )


def rows_for(width=None, N=None, label=None):
    rows = all_results
    if width is not None:
        rows = [row for row in rows if row["width"] == width]
    if N is not None:
        rows = [row for row in rows if row["N"] == N]
    if label is None:
        return rows
    out = []
    for row in rows:
        for candidate in row["candidates"]:
            if candidate["label"] == label:
                out.append((row, candidate))
    return out


largest_N = max(Ns)
fixed4_largest = [candidate["score_ratio"] for _, candidate in rows_for(N=largest_N, label="fixed_4")]
linear1_largest = [candidate["score_ratio"] for _, candidate in rows_for(N=largest_N, label="linear_1")]
super2_largest = [candidate["score_ratio"] for _, candidate in rows_for(N=largest_N, label="super_2")]
linear1_near_largest = [candidate["same_near"] for _, candidate in rows_for(N=largest_N, label="linear_1")]
super2_near_largest = [candidate["same_near"] for _, candidate in rows_for(N=largest_N, label="super_2")]

monotone_tail_relief = []
for row in all_results:
    ordered = sorted(row["candidates"], key=lambda candidate: candidate["effective"])
    near_values = [candidate["same_near"] for candidate in ordered]
    monotone_tail_relief.append(
        all(near_values[i] >= near_values[i + 1] for i in range(len(near_values) - 1))
    )

linear_camouflage_by_width = []
for width in widths:
    rows = rows_for(width=width, N=largest_N)
    candidates = [candidate for row in rows for candidate in row["candidates"]]
    camouflage_labels = [
        candidate["label"]
        for candidate in candidates
        if (candidate["label"].startswith("linear") or candidate["label"] == "super_2")
        and candidate["score_ratio"] <= 1
    ]
    linear_camouflage_by_width.append((width, camouflage_labels))

phase_changes = []
for width in widths:
    for label in schedule_labels:
        phases = [candidate["phase"] for _, candidate in rows_for(width=width, label=label)]
        if len(set(phases)) > 1:
            phase_changes.append((width, label, phases))

check(
    "Exact three-record pattern densities partition every audited poset",
    partition_ok,
    "all antichain/one-relation/vee/wedge/chain counts sum to C(N,3)",
)
check(
    "Same-label near-twin visibility is not a monotone one-parameter curve in finite samples",
    not all(monotone_tail_relief),
    ", ".join(f"N={row['N']} w={row['width']} monotone={monotone_tail_relief[i]}" for i, row in enumerate(all_results)),
)
check(
    "Fixed small jitter remains order-visible at the largest tested scale",
    all(ratio > 1 for ratio in fixed4_largest),
    ", ".join(f"w={widths[i]} fixed_4={fmt(ratio, 10)}" for i, ratio in enumerate(fixed4_largest)),
)
check(
    "Linear-scale jitter can enter finite camouflage at the largest tested scale",
    all(labels for _, labels in linear_camouflage_by_width),
    "; ".join(f"w={w}:{','.join(labels)}" for w, labels in linear_camouflage_by_width),
)
check(
    "Linear and superlinear mixing erase order-visible same-label near twins at the largest scale",
    all(value <= mp.mpf("0.02") for value in linear1_near_largest + super2_near_largest),
    ", ".join(
        f"w={widths[i]} linear_1_near={fmt(linear1_near_largest[i], 10)} super_2_near={fmt(super2_near_largest[i], 10)}"
        for i in range(len(widths))
    ),
)
check(
    "Superlinear mixing is not automatically a better finite match than linear mixing",
    any(super2_largest[i] > linear1_largest[i] for i in range(len(widths))),
    ", ".join(
        f"w={widths[i]} linear_1={fmt(linear1_largest[i], 10)} super_2={fmt(super2_largest[i], 10)}"
        for i in range(len(widths))
    ),
)
check(
    "At least one linear or superlinear schedule changes phase across tested N",
    any(label.startswith("linear") or label == "super_2" for _, label, _ in phase_changes),
    "; ".join(f"w={w} {label}:{'/'.join(phases)}" for w, label, phases in phase_changes[:8]),
)

print("\n(4) Consequence")
print("The washout audit distinguishes order-visible clustering from invisible")
print("implementation history.  Fixed small jitter leaves rooted/order-pattern")
print("defects at the largest tested scale.  Linear-scale jitter can erase")
print("same-label near twins and enter the finite sprinkling null, but increasing")
print("the mixing further is not monotone evidence of a better finite match.")
print("The theorem target should distinguish two cases: order-visible hidden")
print("clusters, which the click law must penalize, and fully washed-out hidden")
print("generators whose record order is just the sprinkling law.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
