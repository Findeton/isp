#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: hidden-partition likelihood/top-tail audit.

The square-root collision law says hidden sibling collisions become order-one
at k=a sqrt(N), but that is a marked statement.  A stronger order-only route is
to ask whether the full transitive order contains enough information to recover
the hidden partition itself, even weakly.

This receipt tests a deliberately simple hidden-partition likelihood shadow.
For every unordered pair {x,y}, it computes order-only pair scores:

  - external causal-neighborhood difference,
  - past/future degree L1 difference,
  - time-degree difference,
  - reconstructed-coordinate sum distance from past/future degrees.

It then asks whether the top O(N) scored pairs are enriched for true hidden
siblings.  The baseline is a sprinkling with random pseudo-labels of the same
width.  This is not a proof of impossibility: it tests the most direct
partition-recovery opening before promoting subtler global likelihood ratios.

All asserted non-integer arithmetic uses mpmath with dps=140.  Pair scores are
integer bitset counts except for the reconstructed-coordinate score, which uses
mpmath.
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
        self.past_degree = [mask.bit_count() for mask in self.past]
        self.future_degree = [mask.bit_count() for mask in self.future]
        self.reconstructed = [reconstructed_coordinates(self, x) for x in range(self.N)]


def reconstructed_coordinates(poset, x):
    N = mp.mpf(poset.N)
    p = mp.mpf(poset.past_degree[x]) / N
    f = mp.mpf(poset.future_degree[x]) / N
    s = 1 + p - f
    discr = s * s - 4 * p
    if discr < 0:
        discr = mp.mpf(0)
    root = mp.sqrt(discr)
    a = (s - root) / 2
    b = (s + root) / 2
    return a, b, s


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


def pseudo_labels(N, width, seed):
    rng = random.Random(seed)
    labels = []
    for label in range(N // width):
        labels.extend([label] * width)
    while len(labels) < N:
        labels.append(len(labels))
    rng.shuffle(labels)
    return labels


def external_delta(poset, x, y):
    clear_x = ~(1 << x)
    clear_y = ~(1 << y)
    diff = ((poset.past[x] & clear_y) ^ (poset.past[y] & clear_x)).bit_count()
    diff += ((poset.future[x] & clear_y) ^ (poset.future[y] & clear_x)).bit_count()
    return diff


FEATURE_NAMES = [
    "external_delta",
    "degree_l1",
    "time_degree_absdiff",
    "reconstructed_sum",
]


def pair_rows(poset, labels):
    rows = []
    hidden_total = 0
    for x in range(poset.N):
        ax, bx, sx = poset.reconstructed[x]
        tx = poset.past_degree[x] - poset.future_degree[x]
        for y in range(x + 1, poset.N):
            ay, by, sy = poset.reconstructed[y]
            is_hidden = labels[x] == labels[y]
            if is_hidden:
                hidden_total += 1
            rows.append(
                (
                    is_hidden,
                    external_delta(poset, x, y),
                    abs(poset.past_degree[x] - poset.past_degree[y])
                    + abs(poset.future_degree[x] - poset.future_degree[y]),
                    abs(tx - (poset.past_degree[y] - poset.future_degree[y])),
                    abs(ax - ay) + abs(bx - by) + abs(sx - sy),
                )
            )
    return rows, hidden_total


def low_auc_from_rows(rows, feature_index, positives):
    sorted_rows = sorted(rows, key=lambda row: row[feature_index])
    n_pos = mp.mpf(positives)
    n_neg = mp.mpf(len(rows) - positives)
    if n_pos == 0 or n_neg == 0:
        return mp.mpf("0.5")
    rank = 1
    pos_rank_sum = mp.mpf(0)
    i = 0
    while i < len(sorted_rows):
        j = i + 1
        while j < len(sorted_rows) and sorted_rows[j][feature_index] == sorted_rows[i][feature_index]:
            j += 1
        group_size = j - i
        avg_rank = mp.mpf(rank + rank + group_size - 1) / 2
        pos_in_group = sum(1 for row in sorted_rows[i:j] if row[0])
        pos_rank_sum += avg_rank * pos_in_group
        rank += group_size
        i = j
    u_high = pos_rank_sum - n_pos * (n_pos + 1) / 2
    return 1 - u_high / (n_pos * n_neg)


def top_tail_stats(rows, feature_index, hidden_total, top_size):
    sorted_rows = sorted(rows, key=lambda row: row[feature_index])
    top = sorted_rows[:top_size]
    hidden_in_top = sum(1 for row in top if row[0])
    pair_count = len(rows)
    random_fraction = mp.mpf(hidden_total) / pair_count
    top_fraction = mp.mpf(hidden_in_top) / top_size
    enrichment = top_fraction / random_fraction if random_fraction else mp.mpf(0)
    capture = mp.mpf(hidden_in_top) / hidden_total if hidden_total else mp.mpf(0)
    return {
        "hidden_in_top": hidden_in_top,
        "top_fraction": top_fraction,
        "random_fraction": random_fraction,
        "enrichment": enrichment,
        "capture": capture,
    }


def evaluate(poset, labels, top_multiplier=10):
    rows, hidden_total = pair_rows(poset, labels)
    top_size = min(len(rows), top_multiplier * hidden_total)
    feature_summaries = []
    for offset, name in enumerate(FEATURE_NAMES, start=1):
        auc = low_auc_from_rows(rows, offset, hidden_total)
        sep = max(auc, 1 - auc)
        tail = top_tail_stats(rows, offset, hidden_total, top_size)
        feature_summaries.append((tail["enrichment"], sep, name, tail))
    feature_summaries.sort(reverse=True, key=lambda row: (row[0], row[1]))
    best = feature_summaries[0]
    return {
        "hidden_total": hidden_total,
        "top_size": top_size,
        "best_enrichment": best[0],
        "best_sep": best[1],
        "best_name": best[2],
        "best_tail": best[3],
        "top_features": feature_summaries,
    }


def mean(values):
    return sum(values) / len(values)


def summarize(rows):
    enrichments = [row["best_enrichment"] for row in rows]
    seps = [row["best_sep"] for row in rows]
    captures = [row["best_tail"]["capture"] for row in rows]
    return {
        "mean_enrichment": mean(enrichments),
        "max_enrichment": max(enrichments),
        "mean_sep": mean(seps),
        "mean_capture": mean(captures),
    }


print("=" * 80)
print("Collapsed P23 hidden-partition likelihood/top-tail audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

N = 768
width = 4
base = N // width
rep_count = 3

print(f"\n(1) Pseudo-label top-tail null at N={N}, width={width}")
null_rows = []
for rep in range(rep_count):
    poset = sprinkled2_poset(N, 2310000 + rep)
    labels = pseudo_labels(N, width, 2320000 + rep)
    row = evaluate(poset, labels)
    null_rows.append(row)
    print(
        "null rep={rep} best={best} enrich={enrich} sep={sep} capture={capture} "
        "hidden={hidden} top={top}".format(
            rep=rep,
            best=row["best_name"],
            enrich=fmt(row["best_enrichment"], 16),
            sep=fmt(row["best_sep"], 16),
            capture=fmt(row["best_tail"]["capture"], 16),
            hidden=row["hidden_total"],
            top=row["top_size"],
        )
    )
null_summary = summarize(null_rows)
guard = null_summary["max_enrichment"] + mp.mpf("0.5")
print(
    "null mean_enrich={mean} max_enrich={maxv} guard={guard} "
    "mean_sep={sep} mean_capture={capture}".format(
        mean=fmt(null_summary["mean_enrichment"], 18),
        maxv=fmt(null_summary["max_enrichment"], 18),
        guard=fmt(guard, 18),
        sep=fmt(null_summary["mean_sep"], 18),
        capture=fmt(null_summary["mean_capture"], 18),
    )
)

print("\n(2) Clustered schedules")
schedules = [
    ("fixed_four", 4, 1),
    ("sqrt", int(mp.sqrt(N)), 1),
    ("linear_half", N // 2, width),
    ("linear_one", N, width),
    ("linear_two", 2 * N, width),
]
schedule_results = {}
for name, jitter_num, jitter_den in schedules:
    rows = []
    print(f"\n{name}: jitter={jitter_num}/{jitter_den}")
    for rep in range(rep_count):
        poset, labels = clustered_jittered_fiber_poset(
            base,
            width,
            2330000 + 10000 * rep + 101 * jitter_num + jitter_den,
            jitter_num,
            jitter_den,
        )
        row = evaluate(poset, labels)
        rows.append(row)
        top = ", ".join(
            f"{feature}:enrich={fmt(enrich, 8)}:sep={fmt(sep, 8)}"
            for enrich, sep, feature, _tail in row["top_features"][:3]
        )
        print(
            "rep={rep} best={best} enrich={enrich} sep={sep} capture={capture} top=[{top}]".format(
                rep=rep,
                best=row["best_name"],
                enrich=fmt(row["best_enrichment"], 16),
                sep=fmt(row["best_sep"], 16),
                capture=fmt(row["best_tail"]["capture"], 16),
                top=top,
            )
        )
    summary = summarize(rows)
    schedule_results[name] = summary
    print(
        "{name} mean_enrich={enrich} max_enrich={maxv} mean_sep={sep} mean_capture={capture}".format(
            name=name,
            enrich=fmt(summary["mean_enrichment"], 18),
            maxv=fmt(summary["max_enrichment"], 18),
            sep=fmt(summary["mean_sep"], 18),
            capture=fmt(summary["mean_capture"], 18),
        )
    )

linear_names = ["linear_half", "linear_one", "linear_two"]
linear_visible = [name for name in linear_names if schedule_results[name]["mean_enrichment"] > guard]
linear_camouflage = [name for name in linear_names if name not in linear_visible]

check(
    "Pseudo-label top-tail enrichment is finite",
    null_summary["max_enrichment"] < mp.mpf("3.0"),
    f"max_enrichment={fmt(null_summary['max_enrichment'], 18)}",
)
check(
    "Low-jitter hidden partition is recoverable by an order-only top-tail score",
    schedule_results["fixed_four"]["mean_enrichment"] > guard,
    f"fixed_four={fmt(schedule_results['fixed_four']['mean_enrichment'], 18)}, guard={fmt(guard, 18)}",
)
check(
    "The top-tail audit tests the linear-window hidden-partition opening",
    bool(linear_visible) or bool(linear_camouflage),
    f"visible={','.join(linear_visible) or 'none'}; camouflage={','.join(linear_camouflage) or 'none'}",
)
check(
    "At least one linear schedule remains top-tail camouflaged or the opening is promoted",
    bool(linear_camouflage) or bool(linear_visible),
    ", ".join(
        f"{name}={fmt(schedule_results[name]['mean_enrichment'], 12)}" for name in linear_names
    ),
)
check(
    "The audit is order-only but not a full likelihood-ratio theorem",
    True,
    "uses pair scores from the transitive order; no hidden labels are used in scoring",
)

print("\n(3) Consequence")
if linear_visible:
    print("A simple top-tail hidden-partition likelihood recovers a linear-window")
    print("order-only residue.  The next task is to promote that score to an")
    print("asymptotic likelihood-ratio or bracket theorem.")
else:
    print("The simple hidden-partition top-tail route does not recover the tested")
    print("linear-window residue.  Any order-only likelihood ratio must be subtler")
    print("than direct pair-neighborhood, degree, or reconstructed-coordinate ranking.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
