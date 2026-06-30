#!/usr/bin/env python3
"""
Paper 30 receipt: six effective-weight campaigns.

The forward-extension receipt showed that exact projective growth is obtained
by the hidden presentation count

    pres(R) * D(parent, child),

but pure record-deck growth fails.  This receipt asks whether increasingly rich
record-intrinsic filtrations can supply an effective substitute for pres(R).

For a filtration P_N, define the exact nonparametric effective weight

    W_P(R) = average pres(S) over records S in the same P_N-atom as R.

This is the best atom-local presentation-count predictor in the simplest
conditional-mean sense.  It is exact rational arithmetic; no fitted real
coefficients are used.  The six campaigns are:

1. constant atom: deck-only baseline.
2. known sectors: scalar/interval/regularity/matching.
3. known + hinge sector: flag5_912, flag5_664.
4. known + residual-active sector: 912, 664, 525184, 25360, 924.
5. known + all five-record flags.
6. full record type: lookup/fiber oracle.

All probabilities, weights, and total variation distances are exact Fractions.
Decimal printing uses mpmath at dps=140 when available, otherwise the helper
fallback from Paper 29.
"""

from collections import defaultdict
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

try:
    import mpmath as mp

    mp.mp.dps = 140
    PRECISION_LINE = f"mp.dps = {mp.mp.dps}"
except ModuleNotFoundError:
    PRECISION_LINE = (
        "exact Fraction arithmetic; decimal reporting through helper fallback; "
        "no floating arithmetic used for checks"
    )

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
        child = restrict_bits(bits, n, subset)
        child_key = canon_bits(child, n - 1)
        deck[child_key] += 1
    return dict(deck)


def build_reverse(reps_by_n, n_min, n_max):
    reverse = {}
    for n in range(n_min, n_max):
        parent_n = n + 1
        rows = defaultdict(dict)
        for parent_key, bits in reps_by_n[parent_n].items():
            deck = delete_deck(bits, parent_n)
            for child_key, multiplicity in deck.items():
                rows[child_key][parent_key] = multiplicity
        reverse[n] = dict(rows)
        print(
            f"  extension N={n}->{parent_n}: children={len(reverse[n])} "
            f"parents={len(reps_by_n[parent_n])}"
        )
    return reverse


def all_flag_keys(k):
    keys = set()
    for pi in perms(k):
        bits = permutation_order_bits(pi)
        keys.add(canon_bits(bits, k))
    return tuple(sorted(keys))


FLAG5_KEYS = all_flag_keys(5)
HINGE_SECTORS = (912, 664)
RESIDUAL_SECTORS = (912, 664, 525184, 25360, 924)
RAW_TO_CANON_CACHE = {}


def raw_to_canon(k):
    if k not in RAW_TO_CANON_CACHE:
        RAW_TO_CANON_CACHE[k] = {
            permutation_order_bits(pi): canon_bits(permutation_order_bits(pi), k)
            for pi in perms(k)
        }
    return RAW_TO_CANON_CACHE[k]


def subset_pair_maps(n, k=5):
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


SUBSET_PAIR_CACHE = {}


def fast_flag_counts_k(bits, n, k):
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


def fast_flag5_counts(bits, n):
    return fast_flag_counts_k(bits, n, 5)


def comparability_masks(bits, n):
    comp_masks = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if has_rel(bits, n, i, j) or has_rel(bits, n, j, i):
                comp_masks[i] |= 1 << j
                comp_masks[j] |= 1 << i
    return comp_masks


def fast_width_from_masks(comp_masks, n):
    best = 0
    for mask in range(1 << n):
        size = mask.bit_count()
        if size <= best:
            continue
        ok = True
        remaining = mask
        while remaining:
            v_bit = remaining & -remaining
            v = v_bit.bit_length() - 1
            if comp_masks[v] & mask:
                ok = False
                break
            remaining ^= v_bit
        if ok:
            best = size
    return best


def fast_matching_counts_from_masks(comp_masks, n):
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

        v_bit = mask & -mask
        v = v_bit.bit_length() - 1
        rest = mask ^ v_bit
        out = list(rec(rest))

        available = comp_masks[v] & rest
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
    comp_masks = comparability_masks(bits, n)
    matchings = fast_matching_counts_from_masks(comp_masks, n)
    return (
        relation_count(bits, n),
        height(bits, n),
        fast_width_from_masks(comp_masks, n),
        tuple(interval_counts(bits, n)),
        degree_moments(bits, n),
        tuple(matchings[1:]),
    )


def build_feature_cache(reps_by_n, n_min, n_max):
    cache = {}
    for n in range(n_min, n_max + 1):
        known = {}
        flags5 = {}
        print(f"  feature cache N={n}: records={len(reps_by_n[n])}")
        for key, bits in reps_by_n[n].items():
            known[key] = known_tuple(bits, n)
            flags5[key] = fast_flag5_counts(bits, n)
        cache[n] = {"known": known, "flags5": flags5}
    return cache


def color_for_model(model, key, n, feature_cache):
    if model == "constant_deck":
        return ("constant",)
    if model == "full_type_oracle":
        return ("type", key)

    base = feature_cache[n]["known"][key]
    if model == "known_sectors":
        return ("known", base)

    flags5 = feature_cache[n]["flags5"][key]
    if model == "known_plus_hinge_sector":
        return ("hinge", base, tuple(flags5.get(sector, 0) for sector in HINGE_SECTORS))
    if model == "known_plus_residual_active":
        return ("residual", base, tuple(flags5.get(sector, 0) for sector in RESIDUAL_SECTORS))
    if model == "known_plus_all_flags5":
        return ("all5", base, tuple(flags5.get(sector, 0) for sector in FLAG5_KEYS))
    raise ValueError(f"unknown model: {model}")


def colors_for_model(model, reps, n, feature_cache):
    return {
        key: color_for_model(model, key, n, feature_cache)
        for key, bits in reps.items()
    }


def atom_stats(colors, counts):
    atom_counts = defaultdict(int)
    atom_sizes = defaultdict(int)
    for key, color in colors.items():
        atom_counts[color] += counts[key]
        atom_sizes[color] += 1
    weights = {
        key: Fraction(atom_counts[color], atom_sizes[color])
        for key, color in colors.items()
    }
    atom_number = len(atom_counts)
    max_atom_size = max(atom_sizes.values())
    singleton_atoms = sum(1 for size in atom_sizes.values() if size == 1)
    lookup = atom_number == len(colors)
    return {
        "weights": weights,
        "atoms": atom_number,
        "max_atom_size": max_atom_size,
        "singleton_atoms": singleton_atoms,
        "lookup": lookup,
    }


def total_variation(left, right):
    keys = set(left) | set(right)
    return sum(abs(left.get(key, Fraction(0)) - right.get(key, Fraction(0))) for key in keys) / 2


def forward_step(dist, n, weights_by_n, reverse):
    out = defaultdict(Fraction)
    weights = weights_by_n[n + 1]
    for child_key, child_prob in dist.items():
        if child_prob == 0:
            continue
        parents = reverse[n].get(child_key, {})
        denom = Fraction(0)
        local_weights = {}
        for parent_key, multiplicity in parents.items():
            value = weights[parent_key] * multiplicity
            if value:
                local_weights[parent_key] = value
                denom += value
        if denom == 0:
            continue
        for parent_key, value in local_weights.items():
            out[parent_key] += child_prob * value / denom
    return dict(out)


def run_forward(seed, seed_n, n_max, weights_by_n, reverse):
    dists = {seed_n: dict(seed)}
    current = dict(seed)
    for n in range(seed_n, n_max):
        current = forward_step(current, n, weights_by_n, reverse)
        dists[n + 1] = current
    return dists


def expectation(dist, values):
    return sum(prob * values.get(key, 0) for key, prob in dist.items())


def sector_values(reps, n, sectors):
    values = {sector: {} for sector in sectors}
    for key, bits in reps.items():
        counts = fast_flag5_counts(bits, n)
        for sector in sectors:
            values[sector][key] = counts.get(sector, 0)
    return values


def model_label(model):
    return {
        "constant_deck": "constant/deck",
        "known_sectors": "known sectors",
        "known_plus_hinge_sector": "known + hinge",
        "known_plus_residual_active": "known + residual-active",
        "known_plus_all_flags5": "known + all flag5",
        "full_type_oracle": "full type/oracle",
    }[model]


def within_atom_presentation_residue(colors, counts):
    atom_counts = defaultdict(int)
    atom_members = defaultdict(list)
    for key, color in colors.items():
        atom_counts[color] += counts[key]
        atom_members[color].append(key)
    total = sum(counts.values())
    residue = Fraction(0)
    for color, members in atom_members.items():
        mean = Fraction(atom_counts[color], len(members))
        for key in members:
            residue += abs(Fraction(counts[key]) - mean)
    return residue / total


def deletion_profile(bits, n, child_colors):
    row = defaultdict(int)
    for child_key, multiplicity in delete_deck(bits, n).items():
        row[child_colors[child_key]] += multiplicity
    return tuple(sorted(row.items()))


def insertion_profile(parent_row, parent_colors):
    row = defaultdict(int)
    for parent_key, multiplicity in parent_row.items():
        row[parent_colors[parent_key]] += multiplicity
    return tuple(sorted(row.items()))


def profile_conflicts_by_color(colors, profiles):
    groups = defaultdict(lambda: defaultdict(int))
    for key, color in colors.items():
        groups[color][profiles[key]] += 1
    bad_atoms = 0
    pair_conflicts = 0
    for profile_counts in groups.values():
        if len(profile_counts) <= 1:
            continue
        bad_atoms += 1
        total = sum(profile_counts.values())
        same = sum(count * (count - 1) // 2 for count in profile_counts.values())
        pair_conflicts += total * (total - 1) // 2 - same
    return bad_atoms, pair_conflicts


def deletion_transfer_conflicts(model, n):
    parent_colors = colors_by_model[model][n]
    child_colors = colors_by_model[model][n - 1]
    profiles = {
        key: deletion_profile(bits, n, child_colors)
        for key, bits in reps_by_n[n].items()
    }
    return profile_conflicts_by_color(parent_colors, profiles)


def insertion_transfer_conflicts(model, n):
    child_colors = colors_by_model[model][n]
    parent_colors = colors_by_model[model][n + 1]
    profiles = {
        key: insertion_profile(reverse[n].get(key, {}), parent_colors)
        for key in reps_by_n[n]
    }
    return profile_conflicts_by_color(child_colors, profiles)


def recurrence_error(model, child_n):
    parent_n = child_n + 1
    weights = weights_by_model[model][parent_n]
    error = Fraction(0)
    total_child_presentations = math.factorial(child_n)
    for child_key, child_count in counts_by_n[child_n].items():
        z = Fraction(0)
        for parent_key, multiplicity in reverse[child_n][child_key].items():
            z += weights[parent_key] * multiplicity
        target = child_count * parent_n * parent_n
        local_relative = abs(z - target) / target
        error += Fraction(child_count, total_child_presentations) * local_relative
    return error


def flag_reconstruction_atoms(k, n):
    keys = tuple(sorted(set(raw_to_canon(k).values())))
    colors = {}
    for key, bits in reps_by_n[n].items():
        counts = fast_flag_counts_k(bits, n, k)
        colors[key] = tuple(counts.get(flag_key, 0) for flag_key in keys)
    return atom_stats(colors, counts_by_n[n])


print("=" * 80)
print("Paper 30 effective-weight six-campaign audit")
print("=" * 80)
print(PRECISION_LINE)
print(f"flag5_types={len(FLAG5_KEYS)}")

n_min = 1
n_max = 9
counts_by_n = {}
reps_by_n = {}
exact_by_n = {}

print("\n" + "=" * 80)
print("Exact record universes")
print("=" * 80)
for n in range(n_min, n_max + 1):
    counts, reps, exact = build_record_universe(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    exact_by_n[n] = exact

print("\n" + "=" * 80)
print("Extension decks")
print("=" * 80)
reverse = build_reverse(reps_by_n, n_min, n_max)

print("\n" + "=" * 80)
print("Shared feature cache")
print("=" * 80)
feature_cache = build_feature_cache(reps_by_n, n_min, n_max)

models = (
    "constant_deck",
    "known_sectors",
    "known_plus_hinge_sector",
    "known_plus_residual_active",
    "known_plus_all_flags5",
    "full_type_oracle",
)

print("\n" + "=" * 80)
print("Filtration atoms and effective weights")
print("=" * 80)
weights_by_model = {}
stats_by_model = {}
colors_by_model = {}
for model in models:
    weights_by_model[model] = {}
    stats_by_model[model] = {}
    colors_by_model[model] = {}
    print(f"\n{model_label(model)}")
    for n in range(n_min, n_max + 1):
        colors = colors_for_model(model, reps_by_n[n], n, feature_cache)
        colors_by_model[model][n] = colors
        stats = atom_stats(colors, counts_by_n[n])
        weights_by_model[model][n] = stats["weights"]
        stats_by_model[model][n] = stats
        print(
            f"  N={n:<2} atoms={stats['atoms']:<7} "
            f"records={len(reps_by_n[n]):<7} "
            f"singletons={stats['singleton_atoms']:<7} "
            f"max_atom={stats['max_atom_size']:<5} "
            f"lookup={stats['lookup']}"
        )

print("\n" + "=" * 80)
print("Forward growth with partition-averaged W_eff")
print("=" * 80)
seed = exact_by_n[1]
results = {}
for model in models:
    dists = run_forward(seed, 1, n_max, weights_by_model[model], reverse)
    results[model] = dists
    print(f"\n{model_label(model)}")
    for n in range(1, n_max + 1):
        tv = total_variation(dists[n], exact_by_n[n])
        print(
            f"  N={n:<2} TV={fmt_frac(tv, 24):>28} "
            f"support={len(dists[n]):>7}/{len(exact_by_n[n]):<7}"
        )

print("\n" + "=" * 80)
print("Boundary-sector expectation error at N=8")
print("=" * 80)
sector_set = tuple(dict.fromkeys(HINGE_SECTORS + RESIDUAL_SECTORS))
sector_map8 = sector_values(reps_by_n[8], 8, sector_set)
sector_error_by_model = {}
for model in models:
    errors = {}
    print(f"\n{model_label(model)}")
    for sector in sector_set:
        got = expectation(results[model][8], sector_map8[sector])
        want = expectation(exact_by_n[8], sector_map8[sector])
        delta = got - want
        errors[sector] = abs(delta)
        print(
            f"  flag5_{sector:<6} delta={fmt_frac(delta, 18):>22} "
            f"got={fmt_frac(got, 18):>22} exact={fmt_frac(want, 18):>22}"
        )
    sector_error_by_model[model] = errors

print("\n" + "=" * 80)
print("Hostile review")
print("=" * 80)
print(
    "1. The full-type/oracle campaign is not a candidate law.  It is a guardrail: "
    "it proves the forward formula is correct when W_eff equals exact hidden "
    "presentation multiplicity."
)
print(
    "2. The constant/deck campaign is the opposite guardrail.  It is fully "
    "record-intrinsic and non-reconstructive, but it cannot reproduce P_N."
)
print(
    "3. The middle four campaigns are the meaningful search region.  They use "
    "only record-intrinsic partition data, then ask whether the atom-average "
    "effective fiber weight is strong enough to drive the forward law."
)
print(
    "4. If a middle campaign improves the N=9 total variation while remaining "
    "non-lookup, the finite evidence supports the residual-active W_eff idea. "
    "If it fails, the theorem must either enrich the boundary filtration or "
    "change the effective-weight functional."
)
print(
    "5. A too-rich local language can also fail by success: if its atoms become "
    "full record lookup, then exact forward reproduction is not evidence for a "
    "physical law.  It has merely reconstructed the hidden presentation count."
)

tv9 = {model: total_variation(results[model][9], exact_by_n[9]) for model in models}
constant_tv9 = tv9["constant_deck"]
oracle_tv9 = tv9["full_type_oracle"]
best_nonlookup = min(
    (tv, model)
    for model, tv in tv9.items()
    if model != "full_type_oracle" and not stats_by_model[model][9]["lookup"]
)

print("\n" + "=" * 80)
print("Campaign summary")
print("=" * 80)
for model in models:
    stats9 = stats_by_model[model][9]
    print(
        f"{model_label(model):<28} "
        f"TV_N9={fmt_frac(tv9[model], 24):>28} "
        f"atoms_N9={stats9['atoms']:<7} "
        f"lookup_N9={stats9['lookup']}"
    )
print(
    f"\nbest_nonlookup={model_label(best_nonlookup[1])} "
    f"TV_N9={fmt_frac(best_nonlookup[0], 24)}"
)

print("\n" + "=" * 80)
print("Six independent scientist-lens campaigns")
print("=" * 80)

print("\n1. Einstein lens: invariant admissibility frontier")
print(
    "  Exactness is not the invariant; exactness plus non-reconstruction is. "
    "The audited frontier separates nonlookup approximants from lookup oracles."
)
admissible_models = [
    model for model in models if not stats_by_model[model][9]["lookup"]
]
for model in admissible_models:
    print(
        f"  {model_label(model):<28} "
        f"atoms_N9={stats_by_model[model][9]['atoms']:<7} "
        f"TV_N9={fmt_frac(tv9[model], 24)}"
    )

print("\n2. Feynman lens: held-out predictive stress")
known_tv9 = tv9["known_sectors"]
hinge_tv9 = tv9["known_plus_hinge_sector"]
residual_tv9 = tv9["known_plus_residual_active"]
print(
    "  The hinge package was discovered before the exact N=9 repair sectors. "
    "It is the cleanest finite held-out test in this receipt."
)
print(f"  known sectors TV_N9        = {fmt_frac(known_tv9, 24)}")
print(f"  known + hinge TV_N9        = {fmt_frac(hinge_tv9, 24)}")
print(f"  residual-active TV_N9      = {fmt_frac(residual_tv9, 24)}")
print(
    f"  hinge improvement factor   = {fmt_frac(known_tv9 / hinge_tv9, 18)}"
)
print(
    "  residual-active is stronger, but it uses N=9 residue and is therefore "
    "a repair target, not a blind prediction."
)

print("\n3. Riemann lens: intrinsic volume-density residue")
volume_residue = {}
for model in [
    "constant_deck",
    "known_sectors",
    "known_plus_hinge_sector",
    "known_plus_residual_active",
    "known_plus_all_flags5",
]:
    value = within_atom_presentation_residue(
        colors_by_model[model][9], counts_by_n[9]
    )
    volume_residue[model] = value
    print(f"  {model_label(model):<28} residue_N9={fmt_frac(value, 24)}")
print(
    "  This is the amount of hidden presentation density still invisible inside "
    "the filtration atoms.  Residual-active sectors remove most of the volume "
    "ambiguity without becoming lookup."
)

print("\n4. Witten lens: stable subalgebra under projection")
transfer_rows = {}
for model in [
    "known_sectors",
    "known_plus_hinge_sector",
    "known_plus_residual_active",
    "known_plus_all_flags5",
]:
    del_bad, del_pairs = deletion_transfer_conflicts(model, 9)
    ins_bad, ins_pairs = insertion_transfer_conflicts(model, 8)
    transfer_rows[model] = (del_bad, del_pairs, ins_bad, ins_pairs)
    print(
        f"  {model_label(model):<28} "
        f"D9_bad={del_bad:<7} D9_pairs={del_pairs:<9} "
        f"I8_bad={ins_bad:<7} I8_pairs={ins_pairs:<9}"
    )
print(
    "  Lookup is projectively stable for the wrong reason.  The admissible "
    "subalgebra must reduce drift without collapsing to singleton atoms."
)

print("\n5. Ramanujan lens: flag reconstruction threshold")
flag_threshold = {}
for k in (3, 4, 5):
    stats = flag_reconstruction_atoms(k, 9)
    flag_threshold[k] = stats
    print(
        f"  all flag{k} profile at N=9: atoms={stats['atoms']:<7} "
        f"records={len(reps_by_n[9]):<7} lookup={stats['lookup']}"
    )
print(
    "  The exact finite surprise is that the five-record profile alone is "
    "already reconstructive at N=9.  That makes all-flag5 a useful identity "
    "source, but not an admissible physical law."
)

print("\n6. Euler lens: local recurrence error")
recurrence_rows = {}
for model in [
    "constant_deck",
    "known_sectors",
    "known_plus_hinge_sector",
    "known_plus_residual_active",
    "known_plus_all_flags5",
    "full_type_oracle",
]:
    value = recurrence_error(model, 8)
    recurrence_rows[model] = value
    print(f"  {model_label(model):<28} recurrence_error_8_to_9={fmt_frac(value, 24)}")
print(
    "  This measures the local failure of the projected preimage identity "
    "before normalization into a forward distribution."
)

check(
    "constant partition equals a nonzero deck-only failure",
    constant_tv9 > 0,
    f"TV_N9={fmt_frac(constant_tv9, 24)}",
)
check(
    "full type/oracle reproduces exact P_N",
    oracle_tv9 == 0,
    f"TV_N9={fmt_frac(oracle_tv9, 24)}",
)
check(
    "known-sector W_eff is not already exact",
    tv9["known_sectors"] > 0,
    f"TV_N9={fmt_frac(tv9['known_sectors'], 24)}",
)
check(
    "residual-active W_eff stays non-lookup at N=9",
    not stats_by_model["known_plus_residual_active"][9]["lookup"],
    (
        f"atoms={stats_by_model['known_plus_residual_active'][9]['atoms']}/"
        f"{len(exact_by_n[9])}"
    ),
)
check(
    "at least one nonlookup filtration improves on constant deck growth",
    best_nonlookup[0] < constant_tv9,
    (
        f"best={model_label(best_nonlookup[1])} "
        f"{fmt_frac(best_nonlookup[0], 24)} < constant "
        f"{fmt_frac(constant_tv9, 24)}"
    ),
)
check(
    "all-flag5 W_eff collapses to lookup and is rejected as non-reconstructive",
    stats_by_model["known_plus_all_flags5"][9]["lookup"],
    (
        f"atoms={stats_by_model['known_plus_all_flags5'][9]['atoms']}/"
        f"{len(exact_by_n[9])}"
    ),
)
check(
    "Einstein frontier: best exact models are lookup, best admissible model is residual-active",
    best_nonlookup[1] == "known_plus_residual_active"
    and stats_by_model["known_plus_all_flags5"][9]["lookup"],
    (
        f"best_nonlookup={model_label(best_nonlookup[1])}; "
        f"all5_lookup={stats_by_model['known_plus_all_flags5'][9]['lookup']}"
    ),
)
check(
    "Feynman held-out hinge package improves known-sector prediction",
    hinge_tv9 < known_tv9 and not stats_by_model["known_plus_hinge_sector"][9]["lookup"],
    f"{fmt_frac(hinge_tv9, 24)} < {fmt_frac(known_tv9, 24)}",
)
check(
    "Riemann volume-density residue decreases along the residual-active ladder",
    volume_residue["known_plus_residual_active"]
    < volume_residue["known_plus_hinge_sector"]
    < volume_residue["known_sectors"]
    < volume_residue["constant_deck"],
    (
        "constant -> known -> hinge -> residual = "
        f"{fmt_frac(volume_residue['constant_deck'], 18)}, "
        f"{fmt_frac(volume_residue['known_sectors'], 18)}, "
        f"{fmt_frac(volume_residue['known_plus_hinge_sector'], 18)}, "
        f"{fmt_frac(volume_residue['known_plus_residual_active'], 18)}"
    ),
)
check(
    "Witten projection drift is reduced by residual-active sectors but lookup remains separate",
    transfer_rows["known_plus_residual_active"][1]
    < transfer_rows["known_sectors"][1]
    and transfer_rows["known_plus_all_flags5"][1] == 0,
    (
        f"D9_pairs known={transfer_rows['known_sectors'][1]} "
        f"residual={transfer_rows['known_plus_residual_active'][1]} "
        f"all5={transfer_rows['known_plus_all_flags5'][1]}"
    ),
)
check(
    "Ramanujan finite flag threshold: all flag5 reconstructs at N=9",
    flag_threshold[5]["lookup"],
    f"atoms={flag_threshold[5]['atoms']}/{len(reps_by_n[9])}",
)
check(
    "Euler recurrence error decreases along the residual-active ladder and vanishes for oracle",
    recurrence_rows["known_plus_residual_active"]
    < recurrence_rows["known_plus_hinge_sector"]
    < recurrence_rows["known_sectors"]
    < recurrence_rows["constant_deck"]
    and recurrence_rows["full_type_oracle"] == 0,
    (
        "constant -> known -> hinge -> residual -> oracle = "
        f"{fmt_frac(recurrence_rows['constant_deck'], 18)}, "
        f"{fmt_frac(recurrence_rows['known_sectors'], 18)}, "
        f"{fmt_frac(recurrence_rows['known_plus_hinge_sector'], 18)}, "
        f"{fmt_frac(recurrence_rows['known_plus_residual_active'], 18)}, "
        f"{fmt_frac(recurrence_rows['full_type_oracle'], 18)}"
    ),
)

print("\n=== Campaign status ===")
print(
    "The six campaigns turn W_eff into an exact finite object.  The full-type "
    "oracle proves what the missing weight would do; the constant deck model "
    "proves why a naive local forward law is insufficient; the intermediate "
    "filtrations measure how much effective presentation multiplicity is "
    "already visible to record-intrinsic local sectors."
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
