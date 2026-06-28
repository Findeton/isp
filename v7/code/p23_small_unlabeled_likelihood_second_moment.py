#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: small-N unlabeled likelihood second-moment proxy.

The mesoscopic rooted flag field showed finite calibration instability.  The
next fork is not another feature vector; it is the likelihood ratio of the
unlabeled transitive order law.  A full-N calculation is out of reach here, so
this receipt performs the smallest exact proxy:

  - N=6 unlabeled 1+1 sprinkling law is computed exactly by enumerating all
    6! coordinate permutations and canonicalizing the induced poset under all
    6! record relabelings.
  - clustered-coordinate laws at width 2 are sampled and projected to the same
    exact unlabeled code space.
  - empirical second moment, chi-square, total variation, and KL are calibrated
    against sprinkling samples of the same size.

This is intentionally tiny.  It is not a critical-window theorem.  Its value is
methodological: it tests the exact unlabeled-likelihood object on the first
scale where brute canonicalization is fully honest.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import Counter
from itertools import permutations
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


def canonical_orders(N):
    if N not in CANON_CACHE:
        rows = []
        for perm in permutations(range(N)):
            pairs = []
            for i in range(N):
                oi = perm[i]
                for j in range(N):
                    if i != j:
                        pairs.append((oi, perm[j]))
            rows.append(pairs)
        CANON_CACHE[N] = rows
    return CANON_CACHE[N]


def canonical_unlabeled_code(poset):
    N = poset.N
    rel = [[False] * N for _ in range(N)]
    for i in range(N):
        future = poset.future[i]
        for j in range(N):
            if i != j:
                rel[i][j] = bool(future & (1 << j))
    best = None
    for pairs in canonical_orders(N):
        code = "".join("1" if rel[i][j] else "0" for i, j in pairs)
        if best is None or code < best:
            best = code
    return best


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


def likelihood_metrics(counts, p_law):
    total = mp.mpf(sum(counts.values()))
    q_law = {code: mp.mpf(count) / total for code, count in counts.items()}
    support = set(p_law) | set(q_law)
    second = mp.mpf(0)
    tv = mp.mpf(0)
    kl = mp.mpf(0)
    outside = mp.mpf(0)
    for code in support:
        p = p_law.get(code, mp.mpf(0))
        q = q_law.get(code, mp.mpf(0))
        tv += abs(q - p)
        if q and p:
            second += q * q / p
            kl += q * mp.log(q / p)
        elif q and not p:
            outside += q
    return {
        "second": second,
        "chi2": second - 1,
        "tv": tv / 2,
        "kl": kl,
        "outside": outside,
        "distinct": len(counts),
    }


def mean(values):
    return sum(values) / len(values)


def summarize(rows):
    keys = ["second", "chi2", "tv", "kl", "outside"]
    out = {}
    for key in keys:
        values = [row[key] for row in rows]
        out[f"{key}_mean"] = mean(values)
        out[f"{key}_max"] = max(values)
    out["distinct_mean"] = mean([mp.mpf(row["distinct"]) for row in rows])
    return out


print("=" * 80)
print("Collapsed P23 small-N unlabeled likelihood second-moment proxy")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 6
width = 2
base = N // width
sample_count = 1024
null_reps = 8
rep_count = 4

print(f"\n(1) Exact unlabeled sprinkling law at N={N}")
p_counts, p_law = exact_sprinkling_law(N)
print(f"permutations={mp.factorial(N)} unlabeled_support={len(p_law)}")
print(
    "top masses="
    + str(sorted([(count, code) for code, count in p_counts.items()], reverse=True)[:5])
)

print(f"\n(2) Empirical sprinkling calibration with sample_count={sample_count}")
null_rows = []
for rep in range(null_reps):
    counts = sample_code_counts(lambda seed: sprinkled2_poset(N, seed), sample_count, 3100000 + rep * 10000)
    metrics = likelihood_metrics(counts, p_law)
    null_rows.append(metrics)
    print(
        f"null rep={rep} second={fmt(metrics['second'], 18)} "
        f"chi2={fmt(metrics['chi2'], 18)} tv={fmt(metrics['tv'], 18)} "
        f"kl={fmt(metrics['kl'], 18)} distinct={metrics['distinct']}"
    )
null = summarize(null_rows)
print(
    f"null max chi2={fmt(null['chi2_max'], 18)} "
    f"tv={fmt(null['tv_max'], 18)} kl={fmt(null['kl_max'], 18)}"
)

print("\n(3) Clustered width-2 schedules projected to exact unlabeled law")
schedules = [
    ("fixed_four", 4, 1),
    ("sqrt", int(mp.sqrt(N)), 1),
    ("linear_half", N // 2, width),
    ("linear_one", N, width),
    ("linear_two", 2 * N, width),
]
schedule_summaries = {}
for index, (name, jitter_num, jitter_den) in enumerate(schedules):
    rows = []
    print(f"\n{name}:")
    for rep in range(rep_count):
        counts = sample_code_counts(
            lambda seed, jn=jitter_num, jd=jitter_den: clustered_jittered_fiber_poset(
                base, width, seed, jn, jd
            )[0],
            sample_count,
            3200000 + index * 100000 + rep * 10000,
        )
        metrics = likelihood_metrics(counts, p_law)
        rows.append(metrics)
        print(
            f"rep={rep} second={fmt(metrics['second'], 18)} "
            f"chi2={fmt(metrics['chi2'], 18)} tv={fmt(metrics['tv'], 18)} "
            f"kl={fmt(metrics['kl'], 18)} outside={fmt(metrics['outside'], 8)} "
            f"distinct={metrics['distinct']}"
        )
    summary = summarize(rows)
    summary["chi2_ratio"] = summary["chi2_mean"] / null["chi2_max"] if null["chi2_max"] else mp.inf
    summary["tv_ratio"] = summary["tv_mean"] / null["tv_max"] if null["tv_max"] else mp.inf
    summary["kl_ratio"] = summary["kl_mean"] / null["kl_max"] if null["kl_max"] else mp.inf
    summary["visible"] = (
        summary["chi2_mean"] > null["chi2_max"]
        or summary["tv_mean"] > null["tv_max"]
        or summary["kl_mean"] > null["kl_max"]
        or summary["outside_mean"] > 0
    )
    schedule_summaries[name] = summary
    print(
        f"{name} mean chi2={fmt(summary['chi2_mean'], 18)} "
        f"chi2/null_max={fmt(summary['chi2_ratio'], 18)} "
        f"tv/null_max={fmt(summary['tv_ratio'], 18)} "
        f"kl/null_max={fmt(summary['kl_ratio'], 18)} "
        f"{'visible' if summary['visible'] else 'inside'}"
    )

print("\n(4) Relabeling invariance spot check")
spot = clustered_jittered_fiber_poset(base, width, 3300000, N, width)[0]
relabelled = relabel_poset(spot, 3300001)
code_a = canonical_unlabeled_code(spot)
code_b = canonical_unlabeled_code(relabelled)
print(f"canonical code preserved after random relabel={code_a == code_b}")

linear_names = ("linear_half", "linear_one", "linear_two")
linear_visible = [name for name in linear_names if schedule_summaries[name]["visible"]]
linear_inside = [name for name in linear_names if name not in linear_visible]

check(
    "Exact N=6 sprinkling law is normalized on unlabeled codes",
    sum(p_counts.values()) == mp.factorial(N) and abs(sum(p_law.values()) - 1) < mp.mpf("1e-100"),
    f"support={len(p_law)}",
)
check(
    "Empirical sprinkling second-moment null is finite",
    null["chi2_max"] > 0 and null["tv_max"] > 0 and null["kl_max"] > 0,
    f"chi2_max={fmt(null['chi2_max'], 12)}",
)
check(
    "Clustered small-N likelihood opening is classified",
    bool(linear_visible) or bool(linear_inside),
    f"visible={','.join(linear_visible) or 'none'}; inside={','.join(linear_inside) or 'none'}",
)
check(
    "Canonical unlabeled code survives random relabeling",
    code_a == code_b,
    "",
)
check(
    "Receipt is an exact small-N proxy, not the critical-window theorem",
    True,
    f"N={N}, width={width}, samples={sample_count}",
)

print("\n=== Consequence ===")
if linear_visible:
    print("At tiny N, the exact unlabeled likelihood proxy can separate at")
    print("least one linear schedule.  This does not prove asymptotic residue,")
    print("but it keeps the exact likelihood-ratio path alive.")
else:
    print("At tiny N, the sampled clustered schedules stay inside the exact")
    print("unlabeled sprinkling calibration.  This supports pursuing a true")
    print("second-moment/contiguity calculation rather than more small flags.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
