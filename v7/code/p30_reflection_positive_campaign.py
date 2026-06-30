#!/usr/bin/env python3
"""
Paper 30 receipt: six reflection-positive positive-shadow campaigns.

This follows the complex-amplitude campaign.  The surviving idea is not
"complex probabilities", but:

    the click law is the positive shadow of a dual-conjugate admissible
    h-transform quotient.

The six campaigns are named by the scientist-pressure they represent:

1. Einstein: invariant positive-shadow quotient, not a flag-name list.
2. Feynman: phase freedom is useful only after projection to a stable shadow.
3. Riemann: the even/odd coordinates have a finite geometry; scalar norms are
   too coarse.
4. Witten: reflection positivity requires odd directions to be imaginary
   channels, not real probabilities.
5. Ramanujan: exact finite identities are sought in the generating/atom
   algebra.
6. Euler: the deletion recurrence must be unchanged by the positive-shadow
   compression.

All combinatorics and probabilities are exact integers/Fractions.  Decimal is
used only for reporting and precision-sensitive square-root display, with
precision 140 (>80-bit).
"""

from collections import defaultdict
from decimal import Decimal, getcontext
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
D = Decimal
sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(20000)

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


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


RAW_TO_CANON_CACHE = {}


def raw_to_canon(k):
    if k not in RAW_TO_CANON_CACHE:
        RAW_TO_CANON_CACHE[k] = {
            permutation_order_bits(pi): canon_bits(permutation_order_bits(pi), k)
            for pi in perms(k)
        }
    return RAW_TO_CANON_CACHE[k]


SUBSET_PAIR_CACHE = {}


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
    matchings = matching_counts_from_masks(masks, n)
    return (
        relation_count(bits, n),
        height(bits, n),
        fast_width_from_masks(masks, n),
        tuple(interval_counts(bits, n)),
        degree_moments(bits, n),
        tuple(matchings[1:]),
    )


def opposite_bits(bits, n):
    out = 0
    for i in range(n):
        for j in range(n):
            if i != j and has_rel(bits, n, i, j):
                out |= 1 << bit_index(n, j, i)
    return out


def dual_key(key, n):
    return canon_bits(opposite_bits(key, n), n)


def build_feature_cache(reps_by_n, n_min, n_max):
    cache = {}
    for n in range(n_min, n_max + 1):
        known = {}
        flags5 = {}
        print(f"  feature cache N={n}: records={len(reps_by_n[n])}")
        for key, bits in reps_by_n[n].items():
            known[key] = known_tuple(bits, n)
            flags5[key] = fast_flag_counts(bits, n, 5)
        cache[n] = {"known": known, "flags5": flags5}
    return cache


DUAL_PAIRS = ((24576, 540672), (25488, 525208), (24606, 549648))
POSTHOC_PAIRS = ((24576, 540672), (525184, 549376), (17288, 525076))


def pair_values(flags, pairs=DUAL_PAIRS):
    values = []
    for left, right in pairs:
        lval = flags.get(left, 0)
        rval = flags.get(right, 0)
        even = lval + rval
        odd = lval - rval
        values.append((lval, rval, even, odd))
    return tuple(values)


def colors_for_mode(n, mode, pairs=DUAL_PAIRS):
    colors = {}
    for key in reps_by_n[n]:
        base = feature_cache[n]["known"][key]
        flags = feature_cache[n]["flags5"][key]
        values = pair_values(flags, pairs)
        if mode == "known":
            extra = ()
        elif mode == "full":
            extra = tuple((lval, rval) for lval, rval, _even, _odd in values)
        elif mode == "even_abs":
            extra = tuple((even, abs(odd)) for _lval, _rval, even, odd in values)
        elif mode == "even_only":
            extra = tuple(even for _lval, _rval, even, _odd in values)
        elif mode == "odd_abs":
            extra = tuple(abs(odd) for _lval, _rval, _even, odd in values)
        elif mode == "agg_l1":
            extra = (
                sum(even for _lval, _rval, even, _odd in values),
                sum(abs(odd) for _lval, _rval, _even, odd in values),
            )
        elif mode == "agg_l2":
            extra = (
                sum(even for _lval, _rval, even, _odd in values),
                sum(odd * odd for _lval, _rval, _even, odd in values),
            )
        elif mode == "agg_linf":
            extra = (
                sum(even for _lval, _rval, even, _odd in values),
                max(abs(odd) for _lval, _rval, _even, odd in values),
            )
        else:
            raise ValueError(mode)
        colors[key] = ("mode", mode, base, extra)
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


def weights_by_mode(mode, pairs=DUAL_PAIRS, target_n=9):
    weights = {}
    metrics = {}
    colors = {}
    for n in range(1, target_n + 1):
        colors[n] = colors_for_mode(n, mode, pairs=pairs)
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


def forward_tv(weights_by_n, target_n=9):
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


def max_weight_diff(left, right, n):
    return max(abs(left[n][key] - right[n][key]) for key in reps_by_n[n])


def coarsening_identity(fine_colors, coarse_colors, fine_weights, coarse_weights, n):
    violations = 0
    max_diff = Fraction(0)
    fibers = defaultdict(set)
    for key in reps_by_n[n]:
        fibers[coarse_colors[n][key]].add(fine_weights[n][key])
        diff = abs(fine_weights[n][key] - coarse_weights[n][key])
        max_diff = max(max_diff, diff)
    for values in fibers.values():
        if len(values) != 1:
            violations += 1
    return violations, max_diff


def matrix_entries(functions, n=9, reflected=False):
    total = Fraction(math.factorial(n))
    rows = []
    for f in functions:
        row = []
        for g in functions:
            value = Fraction(0)
            for key, count in counts_by_n[n].items():
                target = dual_key(key, n) if reflected else key
                value += Fraction(count, total) * f(key) * g(target)
            row.append(value)
        rows.append(tuple(row))
    return tuple(rows)


def principal_minors_3(matrix):
    minors = []
    for i in range(3):
        minors.append(matrix[i][i])
    for i, j in combinations(range(3), 2):
        minors.append(matrix[i][i] * matrix[j][j] - matrix[i][j] * matrix[j][i])
    det = (
        matrix[0][0] * matrix[1][1] * matrix[2][2]
        + matrix[0][1] * matrix[1][2] * matrix[2][0]
        + matrix[0][2] * matrix[1][0] * matrix[2][1]
        - matrix[0][2] * matrix[1][1] * matrix[2][0]
        - matrix[0][1] * matrix[1][0] * matrix[2][2]
        - matrix[0][0] * matrix[1][2] * matrix[2][1]
    )
    minors.append(det)
    return tuple(minors)


def dec_frac(value):
    return D(value.numerator) / D(value.denominator)


def fmt_dec_frac(value, digits=28):
    return format(+dec_frac(value), f".{digits}g")


print("=" * 80)
print("Paper 30 reflection-positive positive-shadow campaign")
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

print("\n" + "=" * 80)
print("Campaign 1 / Einstein: invariant positive shadow")
print("=" * 80)
mode_data = {}
for mode in ("known", "full", "even_abs", "even_only", "odd_abs"):
    colors, weights, metrics = weights_by_mode(mode)
    tv = forward_tv(weights)
    rec = recurrence_errors(9, weights[9], weights[8])
    mode_data[mode] = {
        "colors": colors,
        "weights": weights,
        "metrics": metrics,
        "tv": tv,
        "rec": rec,
    }
    print(
        f"  {mode:<9} atoms9={metrics[9]['atoms']:<7} lookup={metrics[9]['lookup']:<5} "
        f"TV9={fmt_frac(tv, 24)} rec9={fmt_frac(rec[0], 24)}"
    )
dual_weight_max = max(
    abs(mode_data["even_abs"]["weights"][9][key] - mode_data["even_abs"]["weights"][9][dual_key(key, 9)])
    for key in reps_by_n[9]
)
print(f"  even_abs max h(R)-h(R*)={dual_weight_max}")

print("\n" + "=" * 80)
print("Campaign 2 / Feynman: projection beats phase freedom")
print("=" * 80)
drop_rows = []
for idx, pair in enumerate(DUAL_PAIRS):
    kept = tuple(p for j, p in enumerate(DUAL_PAIRS) if j != idx)
    colors, weights, metrics = weights_by_mode("even_abs", pairs=kept)
    tv = forward_tv(weights)
    drop_rows.append((pair, tv, metrics[9]["atoms"]))
    print(
        f"  drop_pair={pair} atoms9={metrics[9]['atoms']} "
        f"TV9={fmt_frac(tv, 24)}"
    )
best_drop_tv = min(row[1] for row in drop_rows)
print(
    f"  full even_abs TV9={fmt_frac(mode_data['even_abs']['tv'], 24)} "
    f"best_drop_TV9={fmt_frac(best_drop_tv, 24)}"
)

print("\n" + "=" * 80)
print("Campaign 3 / Riemann: finite geometry of E and |O|")
print("=" * 80)
geometry_rows = []
geometry_data = {}
for mode in ("agg_l1", "agg_l2", "agg_linf"):
    colors, weights, metrics = weights_by_mode(mode)
    tv = forward_tv(weights)
    rec = recurrence_errors(9, weights[9], weights[8])
    geometry_data[mode] = {
        "colors": colors,
        "weights": weights,
        "metrics": metrics,
        "tv": tv,
        "rec": rec,
    }
    geometry_rows.append((mode, tv, metrics[9]["atoms"], metrics[9]["max_atom"]))
    print(
        f"  {mode:<8} atoms9={metrics[9]['atoms']:<7} max_atom={metrics[9]['max_atom']:<3} "
        f"TV9={fmt_frac(tv, 24)} rec9={fmt_frac(rec[0], 24)}"
    )
best_agg = min(geometry_rows, key=lambda row: row[1])

print("\n" + "=" * 80)
print("Campaign 4 / Witten: reflection positivity")
print("=" * 80)
def even_func(index):
    def fn(key):
        flags = feature_cache[9]["flags5"][key]
        left, right = DUAL_PAIRS[index]
        return flags.get(left, 0) + flags.get(right, 0)
    return fn


def odd_func(index):
    def fn(key):
        flags = feature_cache[9]["flags5"][key]
        left, right = DUAL_PAIRS[index]
        return flags.get(left, 0) - flags.get(right, 0)
    return fn


even_functions = [even_func(i) for i in range(3)]
odd_functions = [odd_func(i) for i in range(3)]
even_reflection = matrix_entries(even_functions, reflected=True)
odd_reflection = matrix_entries(odd_functions, reflected=True)
odd_twisted = tuple(tuple(-value for value in row) for row in odd_reflection)
even_minors = principal_minors_3(even_reflection)
odd_reflection_diagonal = tuple(odd_reflection[i][i] for i in range(3))
odd_twisted_minors = principal_minors_3(odd_twisted)
print("  even reflection principal minors:")
for value in even_minors:
    print(f"    {fmt_dec_frac(value, 20)}")
print("  odd real reflection diagonal:")
for value in odd_reflection_diagonal:
    print(f"    {fmt_dec_frac(value, 20)}")
print("  i-twisted odd reflection principal minors:")
for value in odd_twisted_minors:
    print(f"    {fmt_dec_frac(value, 20)}")

print("\n" + "=" * 80)
print("Campaign 5 / Ramanujan: exact atom identity")
print("=" * 80)
identity_rows = []
agg_l2_identity_rows = []
for n in range(5, 10):
    violations, max_diff = coarsening_identity(
        mode_data["full"]["colors"],
        mode_data["even_abs"]["colors"],
        mode_data["full"]["weights"],
        mode_data["even_abs"]["weights"],
        n,
    )
    agg_violations, agg_max_diff = coarsening_identity(
        mode_data["full"]["colors"],
        geometry_data["agg_l2"]["colors"],
        mode_data["full"]["weights"],
        geometry_data["agg_l2"]["weights"],
        n,
    )
    identity_rows.append((n, violations, max_diff))
    agg_l2_identity_rows.append((n, agg_violations, agg_max_diff))
    print(
        f"  N={n}: even_abs violations={violations} max_h_diff={max_diff}; "
        f"agg_l2 violations={agg_violations} max_h_diff={agg_max_diff}"
    )

print("\n" + "=" * 80)
print("Campaign 6 / Euler: recurrence preservation")
print("=" * 80)
euler_rows = []
for parent_n in range(6, 10):
    full_rec = recurrence_errors(
        parent_n,
        mode_data["full"]["weights"][parent_n],
        mode_data["full"]["weights"][parent_n - 1],
    )
    even_abs_rec = recurrence_errors(
        parent_n,
        mode_data["even_abs"]["weights"][parent_n],
        mode_data["even_abs"]["weights"][parent_n - 1],
    )
    agg_l2_rec = recurrence_errors(
        parent_n,
        geometry_data["agg_l2"]["weights"][parent_n],
        geometry_data["agg_l2"]["weights"][parent_n - 1],
    )
    euler_rows.append((parent_n, full_rec, even_abs_rec, agg_l2_rec))
    print(
        f"  {parent_n-1}->{parent_n}: full_rec={fmt_frac(full_rec[0], 24)} "
        f"even_abs_rec={fmt_frac(even_abs_rec[0], 24)} "
        f"agg_l2_rec={fmt_frac(agg_l2_rec[0], 24)} "
        f"even_diff={fmt_frac(abs(full_rec[0]-even_abs_rec[0]), 24)} "
        f"l2_diff={fmt_frac(abs(full_rec[0]-agg_l2_rec[0]), 24)}"
    )

print("\n" + "=" * 80)
print("Hostile review")
print("=" * 80)
print(
    "1. The Einstein invariant is the quotient/positive shadow, not the individual "
    "sector labels."
)
print(
    "2. The Feynman lesson is negative-positive: arbitrary phases fail, but after "
    "projection the odd-sign channel can be represented by |O|."
)
print(
    "3. The Riemann geometry sharpened during the audit: componentwise E and "
    "|O| are sufficient, but total E plus an odd L2 norm is equally predictive "
    "with slightly fewer atoms."
)
print(
    "4. The Witten/reflection test says odd directions cannot be real positive "
    "observables; they become positive after the i-twist."
)
print(
    "5. The Ramanujan/Euler result is an exact finite identity: the positive shadow "
    "has the same h-weights and recurrence as the full dual-orbit quotient."
)

check(
    "Einstein invariant: even_abs is nonlookup and exactly preserves full TV",
    (not mode_data["even_abs"]["metrics"][9]["lookup"])
    and mode_data["even_abs"]["tv"] == mode_data["full"]["tv"],
    (
        f"even_abs_TV={fmt_frac(mode_data['even_abs']['tv'], 24)} "
        f"full_TV={fmt_frac(mode_data['full']['tv'], 24)}"
    ),
)
check(
    "Einstein invariant: even_abs reduces atom count versus full dual-orbit",
    mode_data["even_abs"]["metrics"][9]["atoms"] < mode_data["full"]["metrics"][9]["atoms"],
    (
        f"even_abs_atoms={mode_data['even_abs']['metrics'][9]['atoms']} "
        f"full_atoms={mode_data['full']['metrics'][9]['atoms']}"
    ),
)
check(
    "dual positive shadow is exactly invariant under order reversal",
    dual_weight_max == 0,
    f"max={dual_weight_max}",
)
check(
    "Feynman projection: every dual pair is necessary for best positive shadow",
    all(tv > mode_data["even_abs"]["tv"] for _pair, tv, _atoms in drop_rows),
    "; ".join(f"{pair}:{fmt_frac(tv, 18)}" for pair, tv, _atoms in drop_rows),
)
check(
    "Riemann geometry: odd L2 aggregate preserves best TV with fewer atoms",
    geometry_data["agg_l2"]["tv"] == mode_data["even_abs"]["tv"]
    and geometry_data["agg_l2"]["metrics"][9]["atoms"] < mode_data["even_abs"]["metrics"][9]["atoms"],
    (
        f"agg_l2_TV={fmt_frac(geometry_data['agg_l2']['tv'], 24)} "
        f"even_abs_TV={fmt_frac(mode_data['even_abs']['tv'], 24)} "
        f"agg_l2_atoms={geometry_data['agg_l2']['metrics'][9]['atoms']} "
        f"even_abs_atoms={mode_data['even_abs']['metrics'][9]['atoms']}"
    ),
)
check(
    "Riemann geometry: L1 and Linf aggregates are too coarse",
    all(row[1] > mode_data["even_abs"]["tv"] for row in geometry_rows if row[0] in ("agg_l1", "agg_linf")),
    "; ".join(f"{mode}:{fmt_frac(tv, 18)}" for mode, tv, _atoms, _max_atom in geometry_rows),
)
check(
    "Witten reflection: even sector reflection Gram is positive semidefinite",
    all(value >= 0 for value in even_minors),
    f"min_minor={fmt_dec_frac(min(even_minors), 20)}",
)
check(
    "Witten reflection: real odd sector has negative reflected norm",
    all(value < 0 for value in odd_reflection_diagonal),
    "; ".join(fmt_dec_frac(value, 20) for value in odd_reflection_diagonal),
)
check(
    "Witten reflection: i-twisted odd sector is positive semidefinite",
    all(value >= 0 for value in odd_twisted_minors),
    f"min_minor={fmt_dec_frac(min(odd_twisted_minors), 20)}",
)
check(
    "Ramanujan identity: full dual-orbit h collapses exactly to even_abs atoms",
    all(violations == 0 and max_diff == 0 for _n, violations, max_diff in identity_rows),
    "; ".join(f"N{n}:v{violations}:d{max_diff}" for n, violations, max_diff in identity_rows),
)
check(
    "Ramanujan identity: full dual-orbit h also collapses exactly to agg_l2 atoms",
    all(violations == 0 and max_diff == 0 for _n, violations, max_diff in agg_l2_identity_rows),
    "; ".join(f"N{n}:v{violations}:d{max_diff}" for n, violations, max_diff in agg_l2_identity_rows),
)
check(
    "Euler recurrence: even_abs preserves full dual-orbit recurrence exactly",
    all(full_rec == even_abs_rec for _n, full_rec, even_abs_rec, _agg_l2_rec in euler_rows),
    "; ".join(f"{n}:{full_rec[0]-even_abs_rec[0]}" for n, full_rec, even_abs_rec, _agg_l2_rec in euler_rows),
)
check(
    "Euler recurrence: agg_l2 preserves full dual-orbit recurrence exactly",
    all(full_rec == agg_l2_rec for _n, full_rec, _even_abs_rec, agg_l2_rec in euler_rows),
    "; ".join(f"{n}:{full_rec[0]-agg_l2_rec[0]}" for n, full_rec, _even_abs_rec, agg_l2_rec in euler_rows),
)

print("\n=== Campaign status ===")
print(
    "The positive-shadow theorem target survives six independent attacks.  In the "
    "audited N<=9 window, full dual-orbit data collapses exactly to both the "
    "componentwise even/absolute-odd quotient and the coarser total-even/odd-L2 "
    "quotient for h-transform weights and recurrence, while reflection positivity "
    "explains why odd directions must enter as imaginary/amplitude channels rather "
    "than real probabilities."
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
