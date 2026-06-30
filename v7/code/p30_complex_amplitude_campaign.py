#!/usr/bin/env python3
"""
Paper 30 receipt: complex amplitude campaign.

This campaign asks whether the e^{-kx}/Feynman-path-integral intuition helps
the current Paper 30 frontier:

    the click law is a dual-symmetric minimal admissible h-transform quotient
    of the record deletion graph.

The campaign keeps the physical law positive.  Complex numbers are tested only
as a possible amplitude layer whose record-projected shadow is real and
nonnegative.

Six attacks are run:

1. dual-conjugation audit: does the current dual-orbit quotient behave like a
   real shadow of a conjugation-symmetric amplitude?
2. even/odd compression audit: can the dual-orbit quotient be compressed to
   even magnitudes, as a |amplitude|^2 law would suggest?
3. normalized deletion-path interference: do phases across multiple deletion
   paths improve the h-transform, or do they destabilize it?
4. hidden-presentation phase audit: literal Feynman phases over hidden
   presentations are tested as an oracle/no-go.
5. complex Laplace probe: real decay e^{-kx} is compared with complex
   continuation e^{-(k+i omega)x} as a diagnostic, not as a probability.
6. hostile review: arbitrary complex phases are rejected unless they are
   record-intrinsic, dual-compatible, projectively stable, positive after
   projection, and non-reconstructive.

Exact combinatorial objects use integers/Fractions.  Phase calculations use
Decimal arithmetic at precision 140 (>80-bit precision), with roots of unity
represented by Decimal square roots.
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
ZERO = D(0)
ONE = D(1)
TWO = D(2)
sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(20000)

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def dec_frac(value):
    return D(value.numerator) / D(value.denominator)


def fmt_dec(value, digits=30):
    if value is None:
        return "ZERO-DENOM"
    return format(+value, f".{digits}g")


def c_add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def c_mul(left, right):
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def c_conj(value):
    return (value[0], -value[1])


def c_abs2(value):
    return value[0] * value[0] + value[1] * value[1]


def c_abs(value):
    return c_abs2(value).sqrt()


def c_pow_int(base, exponent):
    if exponent < 0:
        return c_conj(c_pow_int(base, -exponent))
    out = (ONE, ZERO)
    power = base
    n = exponent
    while n:
        if n & 1:
            out = c_mul(out, power)
        power = c_mul(power, power)
        n >>= 1
    return out


SQRT2 = TWO.sqrt()
SQRT3 = D(3).sqrt()
SQRT6 = D(6).sqrt()

ROOTS = {
    "0": (ONE, ZERO),
    "pi/12": ((SQRT6 + SQRT2) / D(4), (SQRT6 - SQRT2) / D(4)),
    "pi/8": (((TWO + SQRT2).sqrt()) / TWO, ((TWO - SQRT2).sqrt()) / TWO),
    "pi/6": (SQRT3 / TWO, ONE / TWO),
    "pi/4": (SQRT2 / TWO, SQRT2 / TWO),
    "pi/3": (ONE / TWO, SQRT3 / TWO),
    "pi/2": (ZERO, ONE),
    "pi": (-ONE, ZERO),
}


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


def all_flag_keys(k):
    return tuple(sorted(set(raw_to_canon(k).values())))


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


def colors_for_pair_mode(n, pairs, mode):
    colors = {}
    for key in reps_by_n[n]:
        base = feature_cache[n]["known"][key]
        flags = feature_cache[n]["flags5"][key]
        if mode == "known":
            extra = ()
        elif mode == "full":
            extra = tuple((flags.get(a, 0), flags.get(b, 0)) for a, b in pairs)
        elif mode == "even_abs":
            extra = tuple(
                (flags.get(a, 0) + flags.get(b, 0), abs(flags.get(a, 0) - flags.get(b, 0)))
                for a, b in pairs
            )
        elif mode == "even_only":
            extra = tuple(flags.get(a, 0) + flags.get(b, 0) for a, b in pairs)
        elif mode == "odd_abs":
            extra = tuple(abs(flags.get(a, 0) - flags.get(b, 0)) for a, b in pairs)
        else:
            raise ValueError(mode)
        colors[key] = ("pairmode", base, extra)
    return colors


def atom_weights(colors, counts):
    atom_counts = defaultdict(int)
    atom_sizes = defaultdict(int)
    for key, color in colors.items():
        atom_counts[color] += counts[key]
        atom_sizes[color] += 1
    return {key: Fraction(atom_counts[colors[key]], atom_sizes[colors[key]]) for key in colors}


def atom_metrics(colors, counts):
    atoms = defaultdict(list)
    for key, color in colors.items():
        atoms[color].append(key)
    return {
        "atoms": len(atoms),
        "lookup": len(atoms) == len(colors),
        "max_atom": max(len(keys) for keys in atoms.values()),
    }


def total_variation_frac(left, right):
    keys = set(left) | set(right)
    return sum(abs(left.get(key, Fraction(0)) - right.get(key, Fraction(0))) for key in keys) / 2


def forward_step_frac(dist, n, weights_by_n):
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


def quotient_tv(pair_mode, pairs, target_n=9):
    weights_by_n = {}
    metrics_by_n = {}
    for n in range(1, target_n + 1):
        colors = colors_for_pair_mode(n, pairs, pair_mode)
        weights_by_n[n] = atom_weights(colors, counts_by_n[n])
        metrics_by_n[n] = atom_metrics(colors, counts_by_n[n])
    dist = exact_by_n[1]
    for n in range(1, target_n):
        dist = forward_step_frac(dist, n, weights_by_n)
    return total_variation_frac(dist, exact_by_n[target_n]), metrics_by_n[target_n], weights_by_n


def deletion_phase_deck(bits, n):
    deck = defaultdict(list)
    for deleted in range(n):
        lower = sum(1 for u in range(n) if u != deleted and has_rel(bits, n, u, deleted))
        upper = sum(1 for u in range(n) if u != deleted and has_rel(bits, n, deleted, u))
        q = upper - lower
        subset = tuple(v for v in range(n) if v != deleted)
        child_bits = restrict_bits(bits, n, subset)
        child_key = canon_bits(child_bits, n - 1)
        deck[child_key].append(q)
    return dict(deck)


def build_phase_decks(reps_by_n, n_min, n_max):
    out = {}
    for parent_n in range(n_min + 1, n_max + 1):
        rows = {}
        for parent_key, bits in reps_by_n[parent_n].items():
            rows[parent_key] = deletion_phase_deck(bits, parent_n)
        out[parent_n] = rows
    return out


def edge_effective_multiplicity(q_values, root):
    if len(q_values) == 1:
        return ONE
    amp = (ZERO, ZERO)
    for q in q_values:
        amp = c_add(amp, c_pow_int(root, q))
    return c_abs2(amp) / D(len(q_values))


def forward_step_phase(dist, n, weights_by_n_dec, root):
    out = defaultdict(lambda: ZERO)
    weights = weights_by_n_dec[n + 1]
    for child_key, child_prob in dist.items():
        local = {}
        denom = ZERO
        for parent_key, _multiplicity in reverse[n][child_key].items():
            q_values = phase_decks[n + 1][parent_key][child_key]
            eff = edge_effective_multiplicity(q_values, root)
            value = weights[parent_key] * eff
            local[parent_key] = value
            denom += value
        if denom == 0:
            return None
        for parent_key, value in local.items():
            out[parent_key] += child_prob * value / denom
    return dict(out)


def total_variation_mp(left, right):
    keys = set(left) | set(right)
    total = ZERO
    for key in keys:
        total += abs(left.get(key, ZERO) - dec_frac(right.get(key, Fraction(0))))
    return total / 2


def phase_forward_tv(weights_by_n_frac, root, target_n=9):
    weights_by_n_dec = {
        n: {key: dec_frac(value) for key, value in weights.items()}
        for n, weights in weights_by_n_frac.items()
    }
    dist = {next(iter(exact_by_n[1])): ONE}
    for n in range(1, target_n):
        dist = forward_step_phase(dist, n, weights_by_n_dec, root)
        if dist is None:
            return None
    return total_variation_mp(dist, exact_by_n[target_n])


def inversion_count(pi):
    total = 0
    for i in range(len(pi)):
        for j in range(i + 1, len(pi)):
            total += int(pi[i] > pi[j])
    return total


def descent_count(pi):
    return sum(1 for i in range(len(pi) - 1) if pi[i] > pi[i + 1])


def hidden_phase_weights(root, statistic):
    weights_by_n = {}
    for n in range(1, 10):
        amps = defaultdict(lambda: (ZERO, ZERO))
        for pi in perms(n):
            bits = permutation_order_bits(pi)
            key = canon_bits(bits, n)
            score = statistic(pi)
            amps[key] = c_add(amps[key], c_pow_int(root, score))
        weights = {}
        for key, amp in amps.items():
            # Normalized so theta=0 recovers the exact hidden h=pres.
            weights[key] = c_abs2(amp) / D(counts_by_n[n][key])
        weights_by_n[n] = weights
    return weights_by_n


def forward_step_mp(dist, n, weights_by_n):
    out = defaultdict(lambda: ZERO)
    weights = weights_by_n[n + 1]
    for child_key, child_prob in dist.items():
        local = {}
        denom = ZERO
        for parent_key, multiplicity in reverse[n][child_key].items():
            value = weights[parent_key] * D(multiplicity)
            local[parent_key] = value
            denom += value
        if denom == 0:
            return None
        for parent_key, value in local.items():
            out[parent_key] += child_prob * value / denom
    return dict(out)


def hidden_phase_forward_tv(root, statistic):
    weights_by_n = hidden_phase_weights(root, statistic)
    dist = {next(iter(exact_by_n[1])): ONE}
    for n in range(1, 9):
        dist = forward_step_mp(dist, n, weights_by_n)
        if dist is None:
            return None
    return total_variation_mp(dist, exact_by_n[9])


def complex_laplace_by_mode(mode, pairs, kappa, root, n=9):
    values = {}
    for key in reps_by_n[n]:
        flags = feature_cache[n]["flags5"][key]
        x = ZERO
        y = 0
        for a, b in pairs:
            left = flags.get(a, 0)
            right = flags.get(b, 0)
            x += D(left + right)
            y += left - right
        if mode == "even":
            values[key] = ((-kappa * x).exp(), ZERO)
        elif mode == "naive_complex":
            decay = ((-kappa * x).exp(), ZERO)
            # e^{-(k+i theta)x} e^{i theta y} = e^{-kx} e^{i theta(y-x)}
            values[key] = c_mul(decay, c_pow_int(root, y - int(x)))
        elif mode == "dual_complex":
            decay = ((-kappa * x).exp(), ZERO)
            # Dual-compatible form: even channel decays, odd channel carries phase.
            values[key] = c_mul(decay, c_pow_int(root, y))
        else:
            raise ValueError(mode)
    return values


def laplace_dual_conjugation_error(pairs, kappa, root, mode):
    values = complex_laplace_by_mode(mode, pairs, kappa, root)
    worst = ZERO
    for key, value in values.items():
        dk = dual_key(key, 9)
        diff = (values[dk][0] - value[0], values[dk][1] + value[1])
        err = c_abs(diff)
        worst = max(worst, err)
    return worst


def residue_diversity(statistic, modulus, n=9):
    residues = defaultdict(set)
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        residues[key].add(statistic(pi) % modulus)
    max_size = max(len(values) for values in residues.values())
    bad = sum(1 for values in residues.values() if len(values) > 1)
    return max_size, bad


print("=" * 80)
print("Paper 30 complex amplitude campaign")
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
print("Root-deletion phase decks")
print("=" * 80)
phase_decks = build_phase_decks(reps_by_n, 1, 9)
print("  built root-profile phase decks for N=2..9")

DUAL_ORBIT_PAIRS = ((24576, 540672), (25488, 525208), (24606, 549648))
POSTHOC_PAIRS = ((24576, 540672), (525184, 549376), (17288, 525076))
RAW_GENERATED_TV = Fraction(
    0
) + Fraction(
    786431148040827196598617,
    10**28,
)  # decimal receipt value, used only as a loose comparison target

print("\n" + "=" * 80)
print("1. Dual-conjugation and quotient-shadow audit")
print("=" * 80)
known_tv, known_metrics, _known_weights = quotient_tv("known", DUAL_ORBIT_PAIRS)
full_tv, full_metrics, full_weights = quotient_tv("full", DUAL_ORBIT_PAIRS)
posthoc_tv, posthoc_metrics, _posthoc_weights = quotient_tv("full", POSTHOC_PAIRS)
print(
    f"  known TV9={fmt_frac(known_tv, 24)} atoms={known_metrics['atoms']} "
    f"lookup={known_metrics['lookup']}"
)
print(
    f"  direct dual-orbit full TV9={fmt_frac(full_tv, 24)} atoms={full_metrics['atoms']} "
    f"lookup={full_metrics['lookup']}"
)
print(
    f"  posthoc dual closure TV9={fmt_frac(posthoc_tv, 24)} atoms={posthoc_metrics['atoms']} "
    f"lookup={posthoc_metrics['lookup']}"
)

dual_weight_errors = []
for key, value in full_weights[9].items():
    dual_weight_errors.append(abs(value - full_weights[9][dual_key(key, 9)]))
max_dual_weight_error = max(dual_weight_errors)
print(f"  max exact h_P(R)-h_P(R*) error={max_dual_weight_error}")

print("\n" + "=" * 80)
print("2. Even/odd compression audit")
print("=" * 80)
compression_rows = []
for mode in ("even_abs", "even_only", "odd_abs"):
    tv, metrics, weights = quotient_tv(mode, DUAL_ORBIT_PAIRS)
    row = (mode, tv, metrics, weights)
    compression_rows.append(row)
    print(
        f"  mode={mode:<9} TV9={fmt_frac(tv, 24)} atoms={metrics['atoms']} "
        f"lookup={metrics['lookup']} max_atom={metrics['max_atom']}"
    )
even_abs_tv = next(tv for mode, tv, _metrics, _weights in compression_rows if mode == "even_abs")

print("\n" + "=" * 80)
print("3. Normalized deletion-path interference audit")
print("=" * 80)
theta_rows = []
theta_specs = [
    ("0", ROOTS["0"]),
    ("pi/12", ROOTS["pi/12"]),
    ("pi/8", ROOTS["pi/8"]),
    ("pi/6", ROOTS["pi/6"]),
    ("pi/4", ROOTS["pi/4"]),
    ("pi/3", ROOTS["pi/3"]),
    ("pi/2", ROOTS["pi/2"]),
    ("pi", ROOTS["pi"]),
]
for label, root in theta_specs:
    tv = phase_forward_tv(full_weights, root)
    theta_rows.append((label, root, tv))
    print(f"  theta={label:<5} TV9={fmt_dec(tv, 32)}")
phase_zero_tv = theta_rows[0][2]
best_phase_row = min(theta_rows, key=lambda row: row[2])
print(
    f"  best deletion-path phase theta={best_phase_row[0]} "
    f"TV9={fmt_dec(best_phase_row[2], 32)}"
)

print("\n" + "=" * 80)
print("4. Hidden-presentation phase audit")
print("=" * 80)
hidden_rows = []
for stat_label, statistic in (("inversions", inversion_count), ("descents", descent_count)):
    for theta_label, root in (
        ("0", ROOTS["0"]),
        ("pi/6", ROOTS["pi/6"]),
        ("pi/3", ROOTS["pi/3"]),
        ("pi/2", ROOTS["pi/2"]),
        ("pi", ROOTS["pi"]),
    ):
        tv = hidden_phase_forward_tv(root, statistic)
        hidden_rows.append((stat_label, theta_label, tv))
        tv_text = "ZERO-DENOM" if tv is None else fmt_dec(tv, 32)
        print(f"  hidden_stat={stat_label:<10} theta={theta_label:<4} TV9={tv_text}")
hidden_zero_rows = [row for row in hidden_rows if row[1] == "0" and row[2] is not None]
hidden_nonzero_rows = [row for row in hidden_rows if row[1] != "0" and row[2] is not None]
best_hidden_nonzero = min(hidden_nonzero_rows, key=lambda row: row[2])
best_descent_nonzero = min(
    (row for row in hidden_nonzero_rows if row[0] == "descents"),
    key=lambda row: row[2],
)
inv_mod12_max, inv_mod12_bad = residue_diversity(inversion_count, 12, n=9)
desc_mod12_max, desc_mod12_bad = residue_diversity(descent_count, 12, n=9)
print(
    f"  best nonzero hidden phase: stat={best_hidden_nonzero[0]} "
    f"theta={best_hidden_nonzero[1]} TV9={fmt_dec(best_hidden_nonzero[2], 32)}"
)
print(
    f"  residue diversity mod 12: inversions max={inv_mod12_max} bad_records={inv_mod12_bad}; "
    f"descents max={desc_mod12_max} bad_records={desc_mod12_bad}"
)

print("\n" + "=" * 80)
print("5. Complex Laplace probe")
print("=" * 80)
naive_laplace_error = laplace_dual_conjugation_error(
    DUAL_ORBIT_PAIRS, D("0.03125"), ROOTS["pi/6"], "naive_complex"
)
dual_laplace_error = laplace_dual_conjugation_error(
    DUAL_ORBIT_PAIRS, D("0.03125"), ROOTS["pi/6"], "dual_complex"
)
print(
    "  naive probe L=e^{-(k+i theta)x}e^{i theta y}: "
    f"max dual-conjugation error={fmt_dec(naive_laplace_error, 32)}"
)
print(
    "  dual-compatible probe L=e^{-kx}e^{i theta y}: "
    f"max dual-conjugation error={fmt_dec(dual_laplace_error, 32)}"
)
print(
    "  interpretation: the even channel should decay; the dual-odd channel may "
    "carry phase.  Complexifying the even decay channel violates dual conjugation."
)

print("\n" + "=" * 80)
print("Hostile review")
print("=" * 80)
print(
    "1. Complex probabilities are rejected.  The tested object is an amplitude "
    "whose record-projected shadow is positive."
)
print(
    "2. The useful signal is dual conjugation: dual-orbit sectors behave like "
    "real and imaginary channels of a conjugation-symmetric amplitude."
)
print(
    "3. Literal deletion-path interference did not beat the zero-phase h-transform "
    "in the tested root-profile phase family.  This rejects the naive path-sum "
    "import, not the amplitude idea."
)
print(
    "4. Hidden-presentation phases split into gauge and non-gauge cases.  Inversion "
    "phase is constant on committed records in the audited sector, so it changes "
    "only an unobservable phase.  Descent phase is not record-intrinsic and "
    "destabilizes the law."
)
print(
    "5. The surviving rule is: complex structure is admissible only if it descends "
    "to a dual-symmetric, record-intrinsic, nonlookup h-transform quotient."
)

tol = D("1e-80")

check(
    "direct dual-orbit quotient remains nonlookup and beats known sectors",
    (not full_metrics["lookup"]) and full_tv < known_tv,
    f"full={fmt_frac(full_tv, 24)} known={fmt_frac(known_tv, 24)} atoms={full_metrics['atoms']}",
)
check(
    "dual-orbit quotient has exact dual-invariant positive shadow",
    max_dual_weight_error == 0,
    f"max_error={max_dual_weight_error}",
)
check(
    "even-absolute compression is nonlookup and improves known sectors",
    even_abs_tv < known_tv and not next(m for mode, _tv, m, _w in compression_rows if mode == "even_abs")["lookup"],
    f"even_abs={fmt_frac(even_abs_tv, 24)} known={fmt_frac(known_tv, 24)}",
)
check(
    "even-absolute compression keeps the full dual-orbit prediction with fewer atoms",
    even_abs_tv == full_tv
    and next(m for mode, _tv, m, _w in compression_rows if mode == "even_abs")["atoms"] < full_metrics["atoms"],
    (
        f"even_abs_TV={fmt_frac(even_abs_tv, 24)} full_TV={fmt_frac(full_tv, 24)} "
        f"even_abs_atoms={next(m for mode, _tv, m, _w in compression_rows if mode == 'even_abs')['atoms']} "
        f"full_atoms={full_metrics['atoms']}"
    ),
)
check(
    "zero phase deletion interference reproduces the real h-transform",
    abs(phase_zero_tv - dec_frac(full_tv)) < tol,
    f"phase_zero={fmt_dec(phase_zero_tv, 32)} real={fmt_frac(full_tv, 24)}",
)
check(
    "tested nonzero deletion-path phases do not improve the direct dual-orbit quotient",
    best_phase_row[0] == "0",
    f"best_theta={best_phase_row[0]} best_TV={fmt_dec(best_phase_row[2], 32)}",
)
check(
    "hidden zero phase reproduces exact oracle growth",
    all(row[2] is not None and row[2] < tol for row in hidden_zero_rows),
    "; ".join(f"{row[0]}={fmt_dec(row[2], 8)}" for row in hidden_zero_rows),
)
check(
    "inversion hidden phase is pure gauge on committed records mod 12",
    inv_mod12_max == 1 and inv_mod12_bad == 0 and best_hidden_nonzero[0] == "inversions",
    (
        f"inv_mod12_max={inv_mod12_max} inv_bad={inv_mod12_bad} "
        f"best_hidden={best_hidden_nonzero[0]}:{best_hidden_nonzero[1]}"
    ),
)
check(
    "non-gauge descent hidden phase destabilizes relative to record-intrinsic quotient",
    desc_mod12_bad > 0 and best_descent_nonzero[2] > dec_frac(full_tv),
    (
        f"desc_mod12_max={desc_mod12_max} desc_bad={desc_mod12_bad} "
        f"best_descent={fmt_dec(best_descent_nonzero[2], 32)} full_dual={fmt_frac(full_tv, 24)}"
    ),
)
check(
    "naive complexification of even decay violates dual conjugation",
    naive_laplace_error > D("1e-6"),
    f"naive_error={fmt_dec(naive_laplace_error, 32)}",
)
check(
    "dual-compatible odd-channel phase is dual-conjugate at high precision",
    dual_laplace_error < tol,
    f"dual_error={fmt_dec(dual_laplace_error, 32)}",
)

print("\n=== Campaign status ===")
print(
    "The complex/Feynman idea is compatible with Paper 30 only as an amplitude "
    "language behind a positive record-projected h-transform.  The finite audit "
    "supports dual-conjugate sector pairs and rejects naive free phases as the "
    "missing click law."
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
