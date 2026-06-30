#!/usr/bin/env python3
"""
Paper 36 receipt: indivisible W-history prediction campaign.

Target:

    take the Barandes/ISP lesson seriously: Pr(W_{N+1}|W_N) is not the right
    fundamental object.  The effective click law should be the projection of a
    finite indivisible history/cylinder law.

This receipt builds the exact deletion-cylinder law

    R_8 -> R_7 -> R_6 -> R_5 -> R_4

under the audited 2D permutation-order measure, projects R_4,R_5,R_6,R_7 to the
scalar-work panels W_4,W_5,W_6,W_7, and asks how well histories of increasing
length predict the next selected shadow S_8.

All probabilities and TV distances are exact Fractions.  Decimal precision is
set to 140 for reporting/transcendental compatibility only.
"""

from collections import defaultdict
from decimal import getcontext
from fractions import Fraction
from itertools import combinations
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
sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(60000)

SELECTED_PAIRS = (
    (912, 25104),
    (17288, 525076),
    (24576, 540672),
)
SELECTED_METRIC = (5, 5, 3)

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def universe(n):
    counts = defaultdict(int)
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        counts[key] += 1
        reps.setdefault(key, bits)
    dist = {key: Fraction(count, math.factorial(n)) for key, count in counts.items()}
    return dict(counts), reps, dist


def delete_deck(bits, n):
    row = defaultdict(int)
    for deleted in range(n):
        subset = tuple(v for v in range(n) if v != deleted)
        child_key = canon_bits(restrict_bits(bits, n, subset), n - 1)
        row[child_key] += 1
    return dict(row)


def build_decks(reps_by_n, n_min, n_max):
    decks = {}
    reverse = {}
    for n in range(n_min + 1, n_max + 1):
        rows = defaultdict(dict)
        decks[n] = {}
        for key, bits in reps_by_n[n].items():
            deck = delete_deck(bits, n)
            decks[n][key] = deck
            for child_key, multiplicity in deck.items():
                rows[child_key][key] = multiplicity
        reverse[n - 1] = dict(rows)
    return decks, reverse


RAW_TO_CANON_CACHE = {}
SUBSET_PAIR_CACHE = {}


def raw_to_canon(k):
    if k not in RAW_TO_CANON_CACHE:
        RAW_TO_CANON_CACHE[k] = {
            permutation_order_bits(pi): canon_bits(permutation_order_bits(pi), k)
            for pi in perms(k)
        }
    return RAW_TO_CANON_CACHE[k]


def subset_pair_maps(n, k):
    maps = []
    for subset in combinations(range(n), k):
        pairs = []
        for a, old_a in enumerate(subset):
            for b, old_b in enumerate(subset):
                if a != b:
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
        size = bin(mask).count("1")
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


def build_features(reps_by_n, n_min, n_max):
    features = {}
    for n in range(n_min, n_max + 1):
        known = {}
        flags5 = {}
        for key, bits in reps_by_n[n].items():
            known[key] = known_tuple(bits, n)
            flags5[key] = fast_flag_counts(bits, n, 5)
        features[n] = {"known": known, "flags5": flags5}
    return features


def selected_parts(n, key):
    flags = features_by_n[n]["flags5"][key]
    vals = []
    for left, right in SELECTED_PAIRS:
        left_value = flags.get(left, 0)
        right_value = flags.get(right, 0)
        vals.append((left_value + right_value, left_value - right_value))
    even_total = sum(even for even, _odd in vals)
    q_odd = sum(weight * odd * odd for weight, (_even, odd) in zip(SELECTED_METRIC, vals))
    return features_by_n[n]["known"][key], (even_total, q_odd), tuple(vals)


def selected_shadow(n, key):
    known, metric, _vals = selected_parts(n, key)
    return ("S", n, known, metric)


def shadow_atoms(n):
    atoms = defaultdict(list)
    for key in reps_by_n[n]:
        atoms[selected_shadow(n, key)].append(key)
    return dict(atoms)


def aggregate_delete_profile(n, keys):
    row = defaultdict(int)
    for key in keys:
        for child_key, multiplicity in decks_by_n[n][key].items():
            row[selected_shadow(n - 1, child_key)] += multiplicity
    return tuple(sorted(row.items()))


def aggregate_insert_profile(n, keys):
    row = defaultdict(int)
    for key in keys:
        for parent_key, multiplicity in reverse_by_n[n].get(key, {}).items():
            row[selected_shadow(n + 1, parent_key)] += multiplicity
    return tuple(sorted(row.items()))


def scalar_work_by_record(n):
    out = {}
    for shadow, keys in shadow_atoms(n).items():
        representative = keys[0]
        _known, metric, _vals = selected_parts(n, representative)
        delete_profile = aggregate_delete_profile(n, keys)
        insert_profile = aggregate_insert_profile(n, keys)
        delete_scalar = (
            len(delete_profile),
            sum(count for _child, count in delete_profile),
            sum(count * count for _child, count in delete_profile),
        )
        insert_scalar = (
            len(insert_profile),
            sum(count for _parent, count in insert_profile),
            sum(count * count for _parent, count in insert_profile),
        )
        work = ("W", n, metric, len(keys), delete_scalar, insert_scalar)
        for key in keys:
            out[key] = work
    return out


def build_cylinder():
    joint = defaultdict(Fraction)
    W4 = scalar_work_by_record(4)
    W5 = scalar_work_by_record(5)
    W6 = scalar_work_by_record(6)
    W7 = scalar_work_by_record(7)
    for r8, p8 in exact_by_n[8].items():
        y8 = selected_shadow(8, r8)
        for r7, d8 in decks_by_n[8][r8].items():
            p7 = p8 * Fraction(d8, 8)
            w7 = W7[r7]
            for r6, d7 in decks_by_n[7][r7].items():
                p6 = p7 * Fraction(d7, 7)
                w6 = W6[r6]
                for r5, d6 in decks_by_n[6][r6].items():
                    p5 = p6 * Fraction(d6, 6)
                    w5 = W5[r5]
                    for r4, d5 in decks_by_n[5][r5].items():
                        joint[(W4[r4], w5, w6, w7, y8)] += p5 * Fraction(d5, 5)
    return dict(joint)


def marginal(joint, indices):
    out = defaultdict(Fraction)
    for key, prob in joint.items():
        out[tuple(key[i] for i in indices)] += prob
    return dict(out)


def conditional_distributions(joint, context_indices, target_index=-1):
    rows = defaultdict(lambda: defaultdict(Fraction))
    totals = defaultdict(Fraction)
    for key, prob in joint.items():
        context = tuple(key[i] for i in context_indices)
        target = key[target_index]
        rows[context][target] += prob
        totals[context] += prob
    return {
        context: {target: value / totals[context] for target, value in dist.items()}
        for context, dist in rows.items()
    }, dict(totals)


COND_CACHE = {}


def cached_conditional_distributions(joint, context_indices):
    context_indices = tuple(context_indices)
    if context_indices not in COND_CACHE:
        COND_CACHE[context_indices] = conditional_distributions(joint, context_indices)
    return COND_CACHE[context_indices]


def tv_dist(left, right):
    keys = set(left) | set(right)
    return sum(abs(left.get(key, Fraction(0)) - right.get(key, Fraction(0))) for key in keys) / 2


def expected_refinement_tv(joint, fine_indices, coarse_indices):
    fine_cond, fine_totals = cached_conditional_distributions(joint, fine_indices)
    coarse_cond, _coarse_totals = cached_conditional_distributions(joint, coarse_indices)
    total = Fraction(0)
    for fine_ctx, fine_dist in fine_cond.items():
        coarse_ctx = tuple(fine_ctx[fine_indices.index(idx)] for idx in coarse_indices)
        total += fine_totals[fine_ctx] * tv_dist(fine_dist, coarse_cond[coarse_ctx])
    return total


def expected_uncertainty(joint, context_indices):
    cond, totals = cached_conditional_distributions(joint, context_indices)
    residual = Fraction(0)
    avg_support = Fraction(0)
    max_support = 0
    contexts_multi = 0
    for ctx, dist in cond.items():
        support = len(dist)
        max_support = max(max_support, support)
        contexts_multi += int(support > 1)
        avg_support += totals[ctx] * support
        residual += totals[ctx] * (1 - max(dist.values()))
    return {
        "contexts": len(cond),
        "multi_contexts": contexts_multi,
        "avg_support": avg_support,
        "max_support": max_support,
        "bayes_residual": residual,
    }


def range_prediction_rows(joint):
    specs = [
        ("current W7", (3,)),
        ("history W6,W7", (2, 3)),
        ("history W5,W6,W7", (1, 2, 3)),
        ("history W4,W5,W6,W7", (0, 1, 2, 3)),
    ]
    rows = {}
    for name, indices in specs:
        rows[name] = expected_uncertainty(joint, indices)
    return rows


def context_label(indices):
    names = {0: "W4", 1: "W5", 2: "W6", 3: "W7"}
    return ",".join(names[i] for i in indices)


def tower_tv_error(joint, fine_indices, coarse_indices):
    fine_cond, fine_totals = cached_conditional_distributions(joint, fine_indices)
    coarse_cond, coarse_totals = cached_conditional_distributions(joint, coarse_indices)
    aggregate = defaultdict(lambda: defaultdict(Fraction))
    for fine_ctx, fine_dist in fine_cond.items():
        coarse_ctx = tuple(fine_ctx[fine_indices.index(idx)] for idx in coarse_indices)
        weight = fine_totals[fine_ctx] / coarse_totals[coarse_ctx]
        for target, prob in fine_dist.items():
            aggregate[coarse_ctx][target] += weight * prob
    return max(tv_dist(aggregate[ctx], coarse_cond[ctx]) for ctx in coarse_cond)


def all_context_subsets():
    out = []
    for mask in range(1, 1 << 4):
        out.append(tuple(i for i in range(4) if (mask >> i) & 1))
    return out


def path_kernel_normalization_error(joint, context_indices):
    cond, _totals = cached_conditional_distributions(joint, context_indices)
    return max(abs(sum(dist.values()) - 1) for dist in cond.values())


def is_sufficient_against_full_history(joint, full_indices, context_indices):
    full_cond, _full_totals = cached_conditional_distributions(joint, full_indices)
    seen = {}
    for full_ctx, dist in full_cond.items():
        coarse_ctx = tuple(full_ctx[full_indices.index(idx)] for idx in context_indices)
        signature = tuple(sorted(dist.items()))
        previous = seen.setdefault(coarse_ctx, signature)
        if previous != signature:
            return False
    return True


print("=" * 80)
print("Paper 36 indivisible W-history prediction campaign")
print("=" * 80)
print(f"Decimal precision: prec={getcontext().prec}")

counts_by_n = {}
reps_by_n = {}
exact_by_n = {}
for n in range(3, 9):
    counts, reps, dist = universe(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    exact_by_n[n] = dist
    print(f"  built N={n}: records={len(counts)} permutations={math.factorial(n)}")

decks_by_n, reverse_by_n = build_decks(reps_by_n, 3, 8)
features_by_n = build_features(reps_by_n, 3, 8)

print("\n" + "=" * 80)
print("1. Exact W-history cylinder")
print("=" * 80)
joint = build_cylinder()
total_mass = sum(joint.values())
print(f"  cylinder atoms={len(joint)} total_mass={total_mass}")

print("\n" + "=" * 80)
print("2. Non-Markov memory tests")
print("=" * 80)
tv_w6 = expected_refinement_tv(joint, (2, 3), (3,))
tv_w5 = expected_refinement_tv(joint, (1, 2, 3), (2, 3))
tv_w4 = expected_refinement_tv(joint, (0, 1, 2, 3), (1, 2, 3))
tv_full_vs_current = expected_refinement_tv(joint, (0, 1, 2, 3), (3,))
print(f"  E TV[P(S8|W6,W7), P(S8|W7)]       = {fmt_frac(tv_w6, 30)}")
print(f"  E TV[P(S8|W5,W6,W7), P(S8|W6,W7)] = {fmt_frac(tv_w5, 30)}")
print(f"  E TV[P(S8|W4..W7), P(S8|W5..W7)]  = {fmt_frac(tv_w4, 30)}")
print(f"  E TV[P(S8|W4..W7), P(S8|W7)]      = {fmt_frac(tv_full_vs_current, 30)}")

print("\n" + "=" * 80)
print("3. Effective stochastic residual by history length")
print("=" * 80)
prediction_rows = range_prediction_rows(joint)
for name, row in prediction_rows.items():
    print(
        f"  {name:<20} contexts={row['contexts']:<5} "
        f"multi={row['multi_contexts']:<5} "
        f"avg_support={fmt_frac(row['avg_support'], 18):>22} "
        f"max_support={row['max_support']:<5} "
        f"bayes_residual={fmt_frac(row['bayes_residual'], 30)}"
    )

res_current = prediction_rows["current W7"]["bayes_residual"]
res_mid = prediction_rows["history W6,W7"]["bayes_residual"]
res_full = prediction_rows["history W5,W6,W7"]["bayes_residual"]
res_deep = prediction_rows["history W4,W5,W6,W7"]["bayes_residual"]

check(
    "cylinder law is exactly normalized",
    total_mass == 1,
    f"mass={total_mass}",
)
check(
    "current-panel Markov prediction fails",
    tv_w6 > 0,
    f"memory_tv={fmt_frac(tv_w6, 24)}",
)
check(
    "older W-history adds information until exact W4 saturation",
    tv_w5 > 0 and tv_w4 == 0,
    (
        f"additional_tv_w5={fmt_frac(tv_w5, 24)} "
        f"saturation_tv_w4={fmt_frac(tv_w4, 24)}"
    ),
)
check(
    "longer W-history improves Bayes prediction until saturation",
    res_deep == res_full and res_full < res_mid < res_current,
    (
        f"res_current={fmt_frac(res_current, 18)} "
        f"res_mid={fmt_frac(res_mid, 18)} "
        f"res_full={fmt_frac(res_full, 18)} "
        f"res_deep={fmt_frac(res_deep, 18)}"
    ),
)
check(
    "finite history still leaves stochastic residual",
    res_deep > 0 and prediction_rows["history W4,W5,W6,W7"]["multi_contexts"] > 0,
    (
        f"res_deep={fmt_frac(res_deep, 24)} "
        f"multi={prediction_rows['history W4,W5,W6,W7']['multi_contexts']}"
    ),
)
check(
    "effective randomness is residual of uncomputed history, not fundamental dice",
    res_deep < res_current and tv_full_vs_current > 0,
    (
        f"res_drop={fmt_frac(res_current - res_deep, 24)} "
        f"full_vs_current={fmt_frac(tv_full_vs_current, 24)}"
    ),
)

print("\n" + "=" * 80)
print("4. Campaign A: history bound and minimal sufficient suffix")
print("=" * 80)
full_context = (0, 1, 2, 3)
suffixes = [(3,), (2, 3), (1, 2, 3), (0, 1, 2, 3)]
suffix_rows = []
for context in suffixes:
    loss = expected_refinement_tv(joint, full_context, context)
    row = expected_uncertainty(joint, context)
    suffix_rows.append((context, loss, row["bayes_residual"]))
    print(
        f"  suffix {context_label(context):<14} "
        f"loss_vs_full={fmt_frac(loss, 30):>34} "
        f"bayes_residual={fmt_frac(row['bayes_residual'], 30)}"
    )
shortest_zero_suffix = next(context for context, loss, _res in suffix_rows if loss == 0)

subset_rows = []
for context in all_context_subsets():
    sufficient = is_sufficient_against_full_history(joint, full_context, context)
    subset_rows.append((context, sufficient, len(context)))
sufficient_subsets = [context for context, sufficient, _size in subset_rows if sufficient]
min_sufficient_size = min(len(context) for context in sufficient_subsets)
min_sufficient_subsets = [
    context for context in sufficient_subsets if len(context) == min_sufficient_size
]
print(
    f"  all-subset sufficient contexts min_size={min_sufficient_size}: "
    f"{', '.join(context_label(context) for context in min_sufficient_subsets)}"
)

check(
    "shortest causal suffix is W5,W6,W7",
    shortest_zero_suffix == (1, 2, 3),
    f"shortest_zero_suffix={context_label(shortest_zero_suffix)}",
)
check(
    "full-history sufficiency can be achieved without W4",
    (1, 2, 3) in sufficient_subsets,
    f"sufficient={context_label((1, 2, 3))}",
)

print("\n" + "=" * 80)
print("5. Campaign B: bounded experiment randomness as calibrated residual")
print("=" * 80)
tower_full_to_sat = tower_tv_error(joint, full_context, (1, 2, 3))
tower_sat_to_mid = tower_tv_error(joint, (1, 2, 3), (2, 3))
tower_mid_to_current = tower_tv_error(joint, (2, 3), (3,))
print(f"  tower TV full -> W5,W6,W7 = {fmt_frac(tower_full_to_sat, 30)}")
print(f"  tower TV W5,W6,W7 -> W6,W7 = {fmt_frac(tower_sat_to_mid, 30)}")
print(f"  tower TV W6,W7 -> W7       = {fmt_frac(tower_mid_to_current, 30)}")

check(
    "bounded residual kernels obey exact tower calibration",
    tower_full_to_sat == 0 and tower_sat_to_mid == 0 and tower_mid_to_current == 0,
    (
        f"tower_errors=({fmt_frac(tower_full_to_sat, 8)}, "
        f"{fmt_frac(tower_sat_to_mid, 8)}, {fmt_frac(tower_mid_to_current, 8)})"
    ),
)
check(
    "bounded residual remains nontrivial after sufficient W-history",
    res_deep > 0 and prediction_rows["history W4,W5,W6,W7"]["avg_support"] > 1,
    (
        f"residual={fmt_frac(res_deep, 24)} "
        f"avg_support={fmt_frac(prediction_rows['history W4,W5,W6,W7']['avg_support'], 16)}"
    ),
)

print("\n" + "=" * 80)
print("6. Campaign C: finite path-sum / path-integral shadow")
print("=" * 80)
path_norm_current = path_kernel_normalization_error(joint, (3,))
path_norm_sat = path_kernel_normalization_error(joint, (1, 2, 3))
path_norm_full = path_kernel_normalization_error(joint, full_context)
print(f"  max normalization error K(S8|W7)       = {fmt_frac(path_norm_current, 30)}")
print(f"  max normalization error K(S8|W5..W7)  = {fmt_frac(path_norm_sat, 30)}")
print(f"  max normalization error K(S8|W4..W7)  = {fmt_frac(path_norm_full, 30)}")

check(
    "finite path-sum kernels are exactly normalized",
    path_norm_current == 0 and path_norm_sat == 0 and path_norm_full == 0,
    (
        f"norm_errors=({fmt_frac(path_norm_current, 8)}, "
        f"{fmt_frac(path_norm_sat, 8)}, {fmt_frac(path_norm_full, 8)})"
    ),
)
check(
    "path-sum coarse graining reproduces the calibrated residual law",
    tower_sat_to_mid == 0 and tower_mid_to_current == 0,
    "coarse kernels are exact sums of finer history kernels",
)

print("\n" + "=" * 80)
print("7. Campaign D: least boundary-work selector")
print("=" * 80)
print("  action(context) = loss_vs_full + admissible suffix cost")
for context, loss, residual in suffix_rows:
    cost = len(context)
    exact = "yes" if loss == 0 else "no"
    print(
        f"  suffix {context_label(context):<14} "
        f"cost={cost:<2} exact={exact:<3} "
        f"loss={fmt_frac(loss, 30):>34} "
        f"residual={fmt_frac(residual, 30)}"
    )
zero_suffixes = [context for context, loss, _res in suffix_rows if loss == 0]
least_exact_suffix = min(zero_suffixes, key=len)
check(
    "least exact causal boundary-work suffix selects W5,W6,W7",
    least_exact_suffix == (1, 2, 3),
    f"least_exact_suffix={context_label(least_exact_suffix)}",
)
check(
    "least-action analogue is scoped to prediction, not ontic determinism",
    res_full > 0 and suffix_rows[2][1] == 0,
    (
        f"selected_loss={fmt_frac(suffix_rows[2][1], 8)} "
        f"selected_residual={fmt_frac(res_full, 24)}"
    ),
)

print("\n=== Campaign verdict ===")
print(
    "The W-panel is not Markov.  Adding W6 to W7 changes the predicted S8 law, "
    "adding W5 changes it again, and adding W4 is exactly neutral once W5,W6,W7 "
    "are known.  Longer W histories reduce, but do not eliminate, the effective "
    "stochastic residual; in this audited window they saturate at W5..W7.  This supports the ISP "
    "interpretation: the click law is a projection of an indivisible finite "
    "history law.  Practical stochastic modelling should treat uncomputed older "
    "history as a calibrated residual kernel, not as fundamental randomness."
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
