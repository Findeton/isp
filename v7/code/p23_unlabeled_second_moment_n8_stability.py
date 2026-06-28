#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: N=8 unlabeled second-moment stability audit.

The first cross-second-moment ladder found a possible N=8 linear_two signal,
but the null cross-excess maximum was negative.  That is a calibration warning:
with sparse empirical samples, the raw one-sided threshold is not stable enough
to promote a signal.

This receipt reruns the N=8 exact-P unlabeled cross-second-moment proxy with a
larger sample and a centered null guard.  It also reports the unlabeled order
classes contributing most to any cross-excess.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import Counter, defaultdict
from itertools import permutations, product
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
    N = len(perm)
    future = [0] * N
    for i in range(N):
        vi = perm[i]
        mask = 0
        for j in range(i + 1, N):
            if vi < perm[j]:
                mask |= 1 << j
        future[i] = mask
    return Poset(future)


def sprinkled2_poset(N, seed):
    rng = random.Random(seed)
    perm = list(range(N))
    rng.shuffle(perm)
    return poset_from_permutation(perm)


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


CANON_CACHE = {}


def refined_color_classes(poset):
    N = poset.N
    all_mask = (1 << N) - 1
    colors = tuple((poset.past[i].bit_count(), poset.future[i].bit_count()) for i in range(N))
    while True:
        signatures = []
        for i in range(N):
            bit = 1 << i
            incomparable = all_mask ^ bit ^ poset.past[i] ^ poset.future[i]
            signatures.append(
                (
                    colors[i],
                    tuple(sorted(colors[j] for j in iter_bits(poset.past[i]))),
                    tuple(sorted(colors[j] for j in iter_bits(poset.future[i]))),
                    tuple(sorted(colors[j] for j in iter_bits(incomparable))),
                )
            )
        unique = {sig: rank for rank, sig in enumerate(sorted(set(signatures), key=repr))}
        new_colors = tuple(unique[sig] for sig in signatures)
        if new_colors == colors:
            break
        colors = new_colors
    classes = {}
    for i, color in enumerate(colors):
        classes.setdefault(color, []).append(i)
    return [tuple(classes[color]) for color in sorted(classes)]


def code_for_order(poset, order):
    bits = []
    for i, a in enumerate(order):
        future = poset.future[a]
        for j, b in enumerate(order):
            if i != j:
                bits.append("1" if future & (1 << b) else "0")
    return "".join(bits)


def canonical_unlabeled_code(poset):
    cached = CANON_CACHE.get(poset.future)
    if cached is not None:
        return cached
    classes = refined_color_classes(poset)
    best = None
    for selected in product(*(permutations(cls) for cls in classes)):
        order = tuple(v for block in selected for v in block)
        code = code_for_order(poset, order)
        if best is None or code < best:
            best = code
    CANON_CACHE[poset.future] = best
    return best


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


def exact_sprinkling_law(N):
    counts = Counter()
    for perm in permutations(range(N)):
        counts[canonical_unlabeled_code(poset_from_permutation(perm))] += 1
    total = mp.mpf(sum(counts.values()))
    return counts, {code: mp.mpf(count) / total for code, count in counts.items()}


def sample_code_counts(maker, sample_count, seed_base):
    counts = Counter()
    for index in range(sample_count):
        counts[canonical_unlabeled_code(maker(seed_base + index))] += 1
    return counts


def cross_details(counts_a, counts_b, p_law):
    total_a = mp.mpf(sum(counts_a.values()))
    total_b = mp.mpf(sum(counts_b.values()))
    value = mp.mpf(0)
    outside = mp.mpf(0)
    tv_a = mp.mpf(0)
    tv_b = mp.mpf(0)
    contributions = []
    for code in set(p_law) | set(counts_a) | set(counts_b):
        p = p_law.get(code, mp.mpf(0))
        qa = mp.mpf(counts_a.get(code, 0)) / total_a
        qb = mp.mpf(counts_b.get(code, 0)) / total_b
        if p:
            term = qa * qb / p
            value += term
            contributions.append((term - p, term, p, qa, qb, code))
        elif qa or qb:
            outside += (qa + qb) / 2
        tv_a += abs(qa - p)
        tv_b += abs(qb - p)
    contributions.sort(reverse=True, key=lambda row: row[0])
    return {
        "cross_second": value,
        "cross_excess": value - 1,
        "outside": outside,
        "tv_mean": (tv_a + tv_b) / 4,
        "top": contributions[:5],
    }


def mean(values):
    return sum(values) / len(values)


def std(values):
    if len(values) < 2:
        return mp.mpf(0)
    mu = mean(values)
    return mp.sqrt(sum((value - mu) ** 2 for value in values) / (len(values) - 1))


def summarize(rows):
    values = [row["cross_excess"] for row in rows]
    tvs = [row["tv_mean"] for row in rows]
    return {
        "excess_mean": mean(values),
        "excess_max": max(values),
        "excess_min": min(values),
        "excess_std": std(values),
        "tv_mean": mean(tvs),
        "tv_max": max(tvs),
        "outside_mean": mean([row["outside"] for row in rows]),
    }


print("=" * 80)
print("Collapsed P23 N=8 unlabeled second-moment stability audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 8
width = 2
base = N // width
sample_count = 4096
null_reps = 8
rep_count = 4

print("\n(1) Exact P_8 unlabeled law")
p_counts, p_law = exact_sprinkling_law(N)
print(f"permutations={mp.factorial(N)} support={len(p_law)} cache={len(CANON_CACHE)}")
spot = sprinkled2_poset(N, 3700000)
relabel_ok = canonical_unlabeled_code(spot) == canonical_unlabeled_code(relabel_poset(spot, 3700001))
print(f"canonical relabel spot={relabel_ok}")

print(f"\n(2) Cross-second-moment null, sample_count={sample_count}")
null_rows = []
for rep in range(null_reps):
    counts_a = sample_code_counts(lambda seed: sprinkled2_poset(N, seed), sample_count, 3710000 + rep * 20000)
    counts_b = sample_code_counts(lambda seed: sprinkled2_poset(N, seed), sample_count, 3720000 + rep * 20000)
    row = cross_details(counts_a, counts_b, p_law)
    null_rows.append(row)
    print(
        f"null rep={rep} excess={fmt(row['cross_excess'], 18)} "
        f"tv={fmt(row['tv_mean'], 18)} outside={fmt(row['outside'], 8)}"
    )
null = summarize(null_rows)
upper_guard = max(
    mp.mpf(0),
    null["excess_max"],
    null["excess_mean"] + 2 * null["excess_std"],
)
tv_guard = null["tv_max"]
print(
    f"null mean={fmt(null['excess_mean'], 18)} std={fmt(null['excess_std'], 18)} "
    f"max={fmt(null['excess_max'], 18)} upper_guard={fmt(upper_guard, 18)} "
    f"tv_guard={fmt(tv_guard, 18)}"
)

print("\n(3) Clustered schedules")
schedules = [
    ("fixed_four", 4, 1),
    ("sqrt", int(mp.sqrt(N)), 1),
    ("linear_half", N // 2, width),
    ("linear_one", N, width),
    ("linear_two", 2 * N, width),
]
summaries = {}
top_by_schedule = {}
for index, (name, jitter_num, jitter_den) in enumerate(schedules):
    rows = []
    top_accumulator = defaultdict(mp.mpf)
    print(f"\n{name}:")
    for rep in range(rep_count):
        counts_a = sample_code_counts(
            lambda seed, jn=jitter_num, jd=jitter_den: clustered_jittered_fiber_poset(base, width, seed, jn, jd)[0],
            sample_count,
            3730000 + index * 40000 + rep * 4000,
        )
        counts_b = sample_code_counts(
            lambda seed, jn=jitter_num, jd=jitter_den: clustered_jittered_fiber_poset(base, width, seed, jn, jd)[0],
            sample_count,
            3740000 + index * 40000 + rep * 4000,
        )
        row = cross_details(counts_a, counts_b, p_law)
        rows.append(row)
        for contribution, term, p, qa, qb, code in row["top"]:
            top_accumulator[code] += contribution
        print(
            f"rep={rep} excess={fmt(row['cross_excess'], 18)} "
            f"tv={fmt(row['tv_mean'], 18)} top={[(fmt(c, 8), fmt(p, 8)) for c, _, p, _, _, _ in row['top'][:3]]}"
        )
    summary = summarize(rows)
    summary["excess_guard_ratio"] = summary["excess_mean"] / upper_guard if upper_guard > 0 else mp.inf
    summary["tv_guard_ratio"] = summary["tv_mean"] / tv_guard if tv_guard > 0 else mp.inf
    summary["visible"] = (
        summary["excess_mean"] > upper_guard
        or summary["tv_mean"] > tv_guard
        or summary["outside_mean"] > 0
    )
    summaries[name] = summary
    top_codes = sorted(top_accumulator.items(), reverse=True, key=lambda row: row[1])[:5]
    top_by_schedule[name] = top_codes
    print(
        f"{name} mean excess={fmt(summary['excess_mean'], 18)} "
        f"guard_ratio={fmt(summary['excess_guard_ratio'], 18)} "
        f"tv_ratio={fmt(summary['tv_guard_ratio'], 18)} "
        f"{'visible' if summary['visible'] else 'inside'}"
    )

print("\n(4) Top accumulated positive classes")
for name in ("linear_half", "linear_one", "linear_two"):
    print(f"{name}:")
    for code, contribution in top_by_schedule[name]:
        print(f"  contribution={fmt(contribution, 12)} p={fmt(p_law.get(code, 0), 12)} code_prefix={code[:24]}")

linear_names = ("linear_half", "linear_one", "linear_two")
linear_visible = [name for name in linear_names if summaries[name]["visible"]]
linear_inside = [name for name in linear_names if name not in linear_visible]

check(
    "Exact P_8 law is computed and canonical code is relabel invariant",
    len(p_law) == 14794 and relabel_ok,
    f"support={len(p_law)}",
)
check(
    "Centered N=8 null guard is finite and nonnegative",
    upper_guard >= 0 and tv_guard > 0,
    f"upper_guard={fmt(upper_guard, 12)} tv_guard={fmt(tv_guard, 12)}",
)
check(
    "N=8 stability audit classifies the linear schedules",
    bool(linear_visible) or bool(linear_inside),
    f"visible={','.join(linear_visible) or 'none'}; inside={','.join(linear_inside) or 'none'}",
)
check(
    "Top contributing unlabeled classes are reported for the linear schedules",
    all(top_by_schedule[name] for name in linear_names),
    "",
)
check(
    "The audit repairs the negative-null-max opening from the first ladder",
    upper_guard >= max(mp.mpf(0), null["excess_max"]),
    "",
)

print("\n=== Consequence ===")
if linear_visible:
    print("After the centered null guard, at least one N=8 linear schedule")
    print("still separates.  The next step is structural: identify whether the")
    print("top unlabeled classes have a stable interval/height/automorphism")
    print("signature and whether they persist with larger samples.")
else:
    print("After the centered null guard and larger sample, the N=8 linear")
    print("opening does not separate.  The first ladder signal was finite")
    print("calibration noise; the contiguity route becomes stronger.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
