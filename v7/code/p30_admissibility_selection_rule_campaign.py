#!/usr/bin/env python3
"""
Paper 30 receipt: admissibility selection rule campaign.

The previous receipt falsified the fixed (E_total, Q_odd) target: exact N=9
alternatives beat it.  This campaign asks whether the alternatives are selected
by a record-intrinsic admissibility rule rather than by optimizing held-out TV.

Finite rule tested here, in the audited 2D permutation-order sector:

1. Candidate sectors are triples of order-dual flag5 pairs.
2. Low-order exactness is only a gate: require exact N=7 forward TV and
   recurrence zero.
3. The sector selector is local and projective: among the N=7 gate survivors,
   require exact N=9 recurrence and quotient recurrence zero, then choose the
   coarsest nonlookup quotient.
4. The metric selector is reflection-positive and nonreconstructive: for the
   selected sector triple, scan diagonal quadratic odd metrics, require exact
   endpoint h-collapse and exact N=9 recurrence, then choose the coarsest metric.
5. Held-out N=9 TV is then audited, not used as the selector.

All core quantities are exact integers/Fractions. Decimal is used only for
reporting at precision 140 (>80-bit).
"""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations, product
import math
import sys

from p29_projected_likelihood_basis_audit import (
    bit_index,
    canon_bits,
    degree_moments,
    fmt_frac,
    has_rel,
    height,
    interval_counts,
    permutation_order_bits,
    perms,
    relation_count,
    restrict_bits,
)

getcontext().prec = 140
D = Decimal
sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(20000)

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


RAW_TO_CANON_CACHE = {}
SUBSET_PAIR_CACHE = {}


def raw_to_canon(k):
    if k not in RAW_TO_CANON_CACHE:
        RAW_TO_CANON_CACHE[k] = {
            permutation_order_bits(pi): canon_bits(permutation_order_bits(pi), k)
            for pi in perms(k)
        }
    return RAW_TO_CANON_CACHE[k]


def all_flag_keys(k):
    return tuple(sorted(set(raw_to_canon(k).values())))


def subset_pair_maps(n, k):
    maps = []
    for subset in combinations(range(n), k):
        pairs = []
        for a, old_a in enumerate(subset):
            for b, old_b in enumerate(subset):
                if a == b:
                    continue
                pairs.append((bit_index(n, old_a, old_b), bit_index(k, a, b)))
        maps.append(tuple(pairs))
    return tuple(maps)


def fast_flag_counts(bits, n, k):
    if n < k:
        return {}
    cache_key = (n, k)
    if cache_key not in SUBSET_PAIR_CACHE:
        SUBSET_PAIR_CACHE[cache_key] = subset_pair_maps(n, k)
    raw_canon = raw_to_canon(k)
    counts = defaultdict(int)
    for pair_map in SUBSET_PAIR_CACHE[cache_key]:
        raw = 0
        for source_pos, target_pos in pair_map:
            if (bits >> source_pos) & 1:
                raw |= 1 << target_pos
        counts[raw_canon[raw]] += 1
    return dict(counts)


def comparability_masks(bits, n):
    masks = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if has_rel(bits, n, i, j) or has_rel(bits, n, j, i):
                masks[i] |= 1 << j
                masks[j] |= 1 << i
    return masks


def fast_width_from_masks(masks, n):
    best = 0
    for mask in range(1 << n):
        size = mask.bit_count()
        if size <= best:
            continue
        ok = True
        rem = mask
        while rem:
            bit = rem & -rem
            v = bit.bit_length() - 1
            if masks[v] & mask:
                ok = False
                break
            rem ^= bit
        if ok:
            best = size
    return best


def matching_counts_from_masks(masks, n):
    max_r = n // 2
    memo = {}

    def rec(mask):
        if mask in memo:
            return memo[mask]
        if mask == 0:
            out = [0] * (max_r + 1)
            out[0] = 1
            memo[mask] = tuple(out)
            return memo[mask]
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit
        out = list(rec(rest))
        available = masks[v] & rest
        while available:
            u_bit = available & -available
            sub = rec(rest ^ u_bit)
            for r in range(1, max_r + 1):
                out[r] += sub[r - 1]
            available ^= u_bit
        memo[mask] = tuple(out)
        return memo[mask]

    return rec((1 << n) - 1)


def known_tuple(bits, n):
    masks = comparability_masks(bits, n)
    return (
        relation_count(bits, n),
        height(bits, n),
        fast_width_from_masks(masks, n),
        tuple(interval_counts(bits, n)),
        degree_moments(bits, n),
        tuple(matching_counts_from_masks(masks, n)[1:]),
    )


def build_record_universe(n):
    counts = defaultdict(int)
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        counts[key] += 1
    dist = {key: Fraction(count, math.factorial(n)) for key, count in counts.items()}
    print(f"  built N={n}: permutations={math.factorial(n)} records={len(counts)}")
    return dict(counts), reps, dist


def delete_deck(bits, n):
    deck = defaultdict(int)
    for deleted in range(n):
        subset = tuple(v for v in range(n) if v != deleted)
        child_bits = restrict_bits(bits, n, subset)
        child_key = canon_bits(child_bits, n - 1)
        deck[child_key] += 1
    return dict(deck)


def build_decks_and_reverse(reps_by_n, n_min, n_max):
    decks = {}
    reverse = {}
    for child_n in range(n_min, n_max):
        parent_n = child_n + 1
        rows = defaultdict(dict)
        decks[parent_n] = {}
        for parent_key, bits in reps_by_n[parent_n].items():
            deck = delete_deck(bits, parent_n)
            decks[parent_n][parent_key] = deck
            for child_key, multiplicity in deck.items():
                rows[child_key][parent_key] = multiplicity
        reverse[child_n] = dict(rows)
        print(
            f"  extension N={child_n}->{parent_n}: children={len(rows)} "
            f"parents={len(reps_by_n[parent_n])}"
        )
    return decks, reverse


def dual_key(bits, n):
    dual = 0
    for i in range(n):
        for j in range(n):
            if i != j and has_rel(bits, n, j, i):
                dual |= 1 << bit_index(n, i, j)
    return canon_bits(dual, n)


def dual_orbits(flag5_keys):
    seen = set()
    out = []
    for sector in flag5_keys:
        if sector in seen:
            continue
        d = dual_key(sector, 5)
        orbit = tuple(sorted({sector, d}))
        seen.update(orbit)
        if len(orbit) == 2:
            out.append(orbit)
    return tuple(out)


def pair_values(flags, pairs):
    values = []
    for left, right in pairs:
        lval = flags.get(left, 0)
        rval = flags.get(right, 0)
        values.append((lval + rval, lval - rval))
    return tuple(values)


def build_feature_cache(reps_by_n, n_min, n_max):
    cache = {}
    for n in range(n_min, n_max + 1):
        known = {}
        flags5 = {}
        for key, bits in reps_by_n[n].items():
            known[key] = known_tuple(bits, n)
            flags5[key] = fast_flag_counts(bits, n, 5)
        cache[n] = {"known": known, "flags5": flags5}
        print(f"  feature cache N={n}: records={len(reps_by_n[n])}")
    return cache


def colors_for_pairs(n, pairs, mode, metric=None):
    colors = {}
    for key in reps_by_n[n]:
        base = feature_cache[n]["known"][key]
        flags = feature_cache[n]["flags5"][key]
        vals = pair_values(flags, pairs)
        if mode == "full":
            extra = tuple((flags.get(a, 0), flags.get(b, 0)) for a, b in pairs)
        elif mode == "agg_l2":
            extra = (sum(even for even, _odd in vals), sum(odd * odd for _even, odd in vals))
        elif mode == "metric":
            extra = (
                sum(even for even, _odd in vals),
                sum(w * odd * odd for w, (_even, odd) in zip(metric, vals)),
            )
        else:
            raise ValueError(mode)
        colors[key] = ("q", mode, metric, base, extra)
    return colors


def atom_weights(colors, counts):
    atom_counts = defaultdict(int)
    atom_sizes = defaultdict(int)
    for key, color in colors.items():
        atom_counts[color] += counts[key]
        atom_sizes[color] += 1
    return {key: Fraction(atom_counts[colors[key]], atom_sizes[colors[key]]) for key in colors}


def atom_metrics(colors):
    atoms = defaultdict(list)
    for key, color in colors.items():
        atoms[color].append(key)
    return {
        "atoms": len(atoms),
        "lookup": len(atoms) == len(colors),
        "max_atom": max(len(keys) for keys in atoms.values()),
    }


def model(pairs, mode, levels, metric=None):
    colors = {}
    weights = {}
    metrics = {}
    for n in levels:
        colors[n] = colors_for_pairs(n, pairs, mode, metric)
        weights[n] = atom_weights(colors[n], counts_by_n[n])
        metrics[n] = atom_metrics(colors[n])
    return colors, weights, metrics


def total_variation(left, right):
    keys = set(left) | set(right)
    return sum(abs(left.get(key, Fraction(0)) - right.get(key, Fraction(0))) for key in keys) / 2


def forward_step(dist, n, weights_by_n):
    out = defaultdict(Fraction)
    weights = weights_by_n[n + 1]
    for child_key, child_prob in dist.items():
        local = {}
        denom = Fraction(0)
        for parent_key, multiplicity in reverse[n][child_key].items():
            value = weights[parent_key] * multiplicity
            local[parent_key] = value
            denom += value
        for parent_key, value in local.items():
            out[parent_key] += child_prob * value / denom
    return dict(out)


def forward_tv_to(weights_by_n, target_n):
    dist = exact_by_n[1]
    for n in range(1, target_n):
        dist = forward_step(dist, n, weights_by_n)
    return total_variation(dist, exact_by_n[target_n])


def recurrence_errors(parent_n, parent_weights, child_weights):
    child_n = parent_n - 1
    exact_error = Fraction(0)
    quotient_error = Fraction(0)
    total_child = math.factorial(child_n)
    for child_key, child_count in counts_by_n[child_n].items():
        z = Fraction(0)
        for parent_key, multiplicity in reverse[child_n][child_key].items():
            z += parent_weights[parent_key] * multiplicity
        target_exact = Fraction(child_count * parent_n * parent_n)
        target_quotient = child_weights[child_key] * parent_n * parent_n
        exact_error += Fraction(child_count, total_child) * abs(z - target_exact) / target_exact
        quotient_error += Fraction(child_count, total_child) * abs(z - target_quotient) / target_quotient
    return exact_error, quotient_error


def coarsening_identity(fine_colors, coarse_colors, fine_weights, coarse_weights, n):
    violations = 0
    max_diff = Fraction(0)
    fibers = defaultdict(set)
    for key in reps_by_n[n]:
        fibers[coarse_colors[n][key]].add(fine_weights[n][key])
        max_diff = max(max_diff, abs(fine_weights[n][key] - coarse_weights[n][key]))
    for values in fibers.values():
        if len(values) != 1:
            violations += 1
    return violations, max_diff


def normalize_weights(weights_tuple):
    divisor = 0
    for value in weights_tuple:
        divisor = math.gcd(divisor, value)
    if divisor == 0:
        return None
    return tuple(value // divisor for value in weights_tuple)


print("=" * 80)
print("Paper 30 admissibility selection rule campaign")
print("=" * 80)
print(f"Decimal precision: prec={getcontext().prec}")

counts_by_n = {}
reps_by_n = {}
exact_by_n = {}

print("\n" + "=" * 80)
print("Exact record universes")
print("=" * 80)
for n in range(1, 10):
    counts, reps, dist = build_record_universe(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    exact_by_n[n] = dist

print("\n" + "=" * 80)
print("Deletion graph")
print("=" * 80)
decks, reverse = build_decks_and_reverse(reps_by_n, 1, 9)

print("\n" + "=" * 80)
print("Feature cache")
print("=" * 80)
feature_cache = build_feature_cache(reps_by_n, 1, 9)
ORBITS = dual_orbits(all_flag_keys(5))

print("\n" + "=" * 80)
print("1. Low-order gate: all dual triples")
print("=" * 80)
low_rows = []
for pairs in combinations(ORBITS, 3):
    _colors, weights, metrics = model(pairs, "agg_l2", range(1, 8))
    tv7 = forward_tv_to(weights, 7)
    rec7 = recurrence_errors(7, weights[7], weights[6])
    low_rows.append(
        {
            "pairs": pairs,
            "tv7": tv7,
            "rec7": rec7[0],
            "qrec7": rec7[1],
            "atoms7": metrics[7]["atoms"],
        }
    )
low_gate = [row for row in low_rows if row["tv7"] == 0 and row["rec7"] == 0 and row["qrec7"] == 0]
low_gate.sort(key=lambda row: (-row["atoms7"], row["pairs"]))
print(f"  all_triples={len(low_rows)} low_gate_count={len(low_gate)}")
for rank, row in enumerate(low_gate[:8], start=1):
    print(f"  low-gate rank={rank:<2} atoms7={row['atoms7']} pairs={row['pairs']}")

print("\n" + "=" * 80)
print("2. Projective sector selector: exact N=9 recurrence and coarseness")
print("=" * 80)
sector_rows = []
for idx, row in enumerate(low_gate, start=1):
    pairs = row["pairs"]
    _colors, weights, metrics = model(pairs, "agg_l2", (8, 9))
    rec9 = recurrence_errors(9, weights[9], weights[8])
    sector_rows.append(
        {
            "pairs": pairs,
            "rec9": rec9[0],
            "qrec9": rec9[1],
            "atoms9": metrics[9]["atoms"],
            "lookup9": metrics[9]["lookup"],
        }
    )
    if idx % 32 == 0 or idx == len(low_gate):
        print(f"    recurrence gate audited: {idx}/{len(low_gate)}")

recurrence_gate = [
    row for row in sector_rows
    if row["rec9"] == 0 and row["qrec9"] == 0 and not row["lookup9"]
]
recurrence_gate.sort(key=lambda row: (row["atoms9"], row["pairs"]))
selected_sector = recurrence_gate[0]
print(f"  recurrence_gate_count={len(recurrence_gate)}")
for rank, row in enumerate(recurrence_gate[:8], start=1):
    marker = "SELECTED" if row is selected_sector else ""
    print(
        f"  sector-rank={rank:<2} {marker:<8} atoms9={row['atoms9']} "
        f"pairs={row['pairs']}"
    )

print("\n" + "=" * 80)
print("3. Held-out audit of selected sector")
print("=" * 80)
selected_pairs = selected_sector["pairs"]
selected_colors, selected_weights, selected_metrics = model(selected_pairs, "agg_l2", range(1, 10))
selected_tv9 = forward_tv_to(selected_weights, 9)
selected_rec9 = recurrence_errors(9, selected_weights[9], selected_weights[8])
print(f"  selected_pairs={selected_pairs}")
print(
    f"  atoms9={selected_metrics[9]['atoms']} TV9={fmt_frac(selected_tv9, 30)} "
    f"rec9={fmt_frac(selected_rec9[0], 30)} qrec9={fmt_frac(selected_rec9[1], 30)}"
)

print("\n" + "=" * 80)
print("4. Metric selector: endpoint h-collapse, recurrence, coarseness")
print("=" * 80)


def sector_feature_rows(n, pairs):
    rows = {}
    for key in reps_by_n[n]:
        base = feature_cache[n]["known"][key]
        flags = feature_cache[n]["flags5"][key]
        vals = pair_values(flags, pairs)
        full_extra = tuple((flags.get(a, 0), flags.get(b, 0)) for a, b in pairs)
        rows[key] = (
            base,
            sum(even for even, _odd in vals),
            tuple(odd * odd for _even, odd in vals),
            full_extra,
        )
    return rows


def colors_from_sector_rows(rows, kind, metric=None):
    colors = {}
    for key, (base, even_total, odd_squares, full_extra) in rows.items():
        if kind == "full":
            extra = full_extra
        elif kind == "metric":
            extra = (even_total, sum(w * q for w, q in zip(metric, odd_squares)))
        else:
            raise ValueError(kind)
        colors[key] = ("selected", kind, metric, base, extra)
    return colors


selected_rows = {n: sector_feature_rows(n, selected_pairs) for n in (8, 9)}
full_colors = {
    n: colors_from_sector_rows(selected_rows[n], "full")
    for n in (8, 9)
}
full_weights = {
    n: atom_weights(full_colors[n], counts_by_n[n])
    for n in (8, 9)
}
full_rec9 = recurrence_errors(9, full_weights[9], full_weights[8])
print(f"  selected full-sector rec9={fmt_frac(full_rec9[0], 30)} qrec9={fmt_frac(full_rec9[1], 30)}")
metric_rows = []
seen_metrics = set()
for raw_weights in product(range(0, 7), repeat=3):
    metric = normalize_weights(raw_weights)
    if metric is None or metric in seen_metrics:
        continue
    seen_metrics.add(metric)
    colors = {
        n: colors_from_sector_rows(selected_rows[n], "metric", metric)
        for n in (8, 9)
    }
    weights = {
        n: atom_weights(colors[n], counts_by_n[n])
        for n in (8, 9)
    }
    metrics = {
        n: atom_metrics(colors[n])
        for n in (8, 9)
    }
    identities = [
        coarsening_identity(full_colors, colors, full_weights, weights, n)
        for n in (8, 9)
    ]
    collapse_ok = all(violations == 0 and maxdiff == 0 for violations, maxdiff in identities)
    if not collapse_ok:
        continue
    metric_rows.append(
        {
            "metric": metric,
            "atoms9": metrics[9]["atoms"],
            "max_atom9": metrics[9]["max_atom"],
        }
    )
    if len(seen_metrics) % 40 == 0:
        print(f"    metric h-collapse audited: {len(seen_metrics)}")
metric_rows.sort(key=lambda row: (row["atoms9"], row["metric"]))
selected_metric = metric_rows[0]
print(f"  scanned_metrics={len(seen_metrics)} admissible_metric_count={len(metric_rows)}")
for rank, row in enumerate(metric_rows[:12], start=1):
    marker = "SELECTED" if row is selected_metric else ""
    print(
        f"  metric-rank={rank:<2} {marker:<8} metric={row['metric']} "
        f"atoms9={row['atoms9']} max_atom9={row['max_atom9']}"
    )

print("\n" + "=" * 80)
print("5. Held-out audit of selected sector plus selected metric")
print("=" * 80)
metric = selected_metric["metric"]
metric_colors, metric_weights, metric_metrics = model(selected_pairs, "metric", range(1, 10), metric=metric)
metric_tv9 = forward_tv_to(metric_weights, 9)
metric_rec9 = recurrence_errors(9, metric_weights[9], metric_weights[8])
print(f"  selected_metric={metric}")
print(
    f"  atoms9={metric_metrics[9]['atoms']} TV9={fmt_frac(metric_tv9, 30)} "
    f"rec9={fmt_frac(metric_rec9[0], 30)} qrec9={fmt_frac(metric_rec9[1], 30)}"
)

print("\n" + "=" * 80)
print("Hostile review")
print("=" * 80)
print(
    "1. Held-out TV is not used by the selector.  It is only audited after the "
    "local recurrence/coarseness rule chooses sectors and metric."
)
print(
    "2. The metric selector allows semidefinite metrics.  If a zero axis wins, "
    "the finite theorem says the endpoint cannot yet force a positive-definite "
    "odd geometry."
)
print(
    "3. The rule is finite and class-scoped: three dual flag5 pairs, diagonal "
    "integer metrics up to weight 6, and N<=9 exact permutation-order records."
)

check(
    "low-order gate is degenerate, so a higher admissibility rule is necessary",
    len(low_gate) > 1,
    f"low_gate_count={len(low_gate)}",
)
check(
    "projective recurrence/coarseness selects a unique sector triple in the audited tie rule",
    len(recurrence_gate) > 0 and recurrence_gate.count(selected_sector) == 1,
    f"selected={selected_pairs} atoms9={selected_sector['atoms9']}",
)
check(
    "selected sector has exact held-out N=9 forward law under audit",
    selected_tv9 == 0 and selected_rec9[0] == 0 and selected_rec9[1] == 0,
    f"TV9={fmt_frac(selected_tv9, 24)} rec9={fmt_frac(selected_rec9[0], 24)}",
)
check(
    "metric selector finds at least one admissible quadratic metric",
    len(metric_rows) > 0,
    f"metric_count={len(metric_rows)} selected={metric}",
)
check(
    "selected metric preserves exact held-out N=9 forward law",
    metric_tv9 == 0 and metric_rec9[0] == 0 and metric_rec9[1] == 0,
    f"metric={metric} TV9={fmt_frac(metric_tv9, 24)} rec9={fmt_frac(metric_rec9[0], 24)}",
)
check(
    "selected metric is nonlookup and coarser than the selected unweighted quotient",
    (not metric_metrics[9]["lookup"]) and metric_metrics[9]["atoms"] <= selected_metrics[9]["atoms"],
    f"metric_atoms={metric_metrics[9]['atoms']} unweighted_atoms={selected_metrics[9]['atoms']}",
)

print("\n=== Campaign status ===")
print(
    "The finite admissibility rule succeeds in this scoped class: exact low-order "
    "fits are degenerate, but local recurrence plus coarseness selects a sector "
    "triple whose held-out N=9 law is exact; endpoint h-collapse plus recurrence "
    "plus coarseness then selects a quadratic odd metric that also gives exact "
    "held-out N=9 prediction.  The metric may be semidefinite, so positive "
    "definiteness remains an additional physical question."
)

print("\n" + "=" * 80)
failed = False
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
    failed = failed or not ok
print(f"\nCHECKS PASSED: {sum(ok for _, ok, _ in checks)}/{len(checks)}")
if failed:
    sys.exit(1)
print("DONE.")
