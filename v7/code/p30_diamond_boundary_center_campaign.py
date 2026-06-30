#!/usr/bin/env python3
"""
Paper 30 receipt: diamond-boundary center campaign.

Campaign T rebased the finite admissibility rule on the older sealed-diamond
picture: hidden structure is licensed only when its projected likelihood leaves
record-visible boundary residue.  This receipt tests the finite version of that
claim in the audited 2D permutation-order sector.

Tested finite rule:

1. Build the N=9 compressed multi-hole boundary residual after the committed
   N=8 boundary cover plus the coarse hinge-sector correction.
2. Mark an order-dual flag5 orbit as boundary-licensed only if its
   dual-even/quadratic-dual-odd signature separates at least one residual
   boundary conflict pair.
3. Test the stronger "flag coordinates cover the whole diamond center" target.
   The campaign falsifies that stronger target in the audited window: the full
   residual edge graph is closed by the diamond center itself, but not by any
   combination of the tested order-dual flag5 coordinate directions.
4. Run the Campaign S low-order/projective recurrence/coarseness selector using
   only boundary-licensed dual orbits.
5. Audit, only after selection, whether the chosen sectors and the selected
   quadratic odd metric still give the exact held-out N=9 forward law.

All core counts are exact integers/Fractions. Decimal is used only for reporting
at precision 140 (>80-bit).
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
    same_block_score,
)

getcontext().prec = 140
D = Decimal
sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(30000)

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


def delete_positions(pi, positions):
    removed_positions = set(positions)
    remaining_values = [value for idx, value in enumerate(pi) if idx not in removed_positions]
    rank = {value: idx for idx, value in enumerate(sorted(remaining_values))}
    return tuple(rank[value] for value in remaining_values)


def build_record_universe(n):
    counts = defaultdict(int)
    reps = {}
    fibers = defaultdict(list)
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        counts[key] += 1
        fibers[key].append(pi)
    dist = {key: Fraction(count, math.factorial(n)) for key, count in counts.items()}
    print(f"  built N={n}: permutations={math.factorial(n)} records={len(counts)}")
    return dict(counts), reps, dist, dict(fibers)


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


def build_feature_cache(reps_by_n, n_min, n_max):
    cache = {}
    for n in range(n_min, n_max + 1):
        known = {}
        flags = {3: {}, 4: {}, 5: {}}
        for key, bits in reps_by_n[n].items():
            known[key] = known_tuple(bits, n)
            for k in (3, 4, 5):
                flags[k][key] = fast_flag_counts(bits, n, k)
        cache[n] = {"known": known, "flags": flags}
        print(f"  feature cache N={n}: records={len(reps_by_n[n])}")
    return cache


def pair_values(flags5, pairs):
    values = []
    for left, right in pairs:
        lval = flags5.get(left, 0)
        rval = flags5.get(right, 0)
        values.append((lval + rval, lval - rval))
    return tuple(values)


def colors_for_pairs(n, pairs, mode, metric=None):
    colors = {}
    for key in reps_by_n[n]:
        base = feature_cache[n]["known"][key]
        flags5 = feature_cache[n]["flags"][5][key]
        vals = pair_values(flags5, pairs)
        if mode == "full":
            extra = tuple((flags5.get(a, 0), flags5.get(b, 0)) for a, b in pairs)
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


def multihole_histograms_all(n, ks, counts, fibers):
    hist_by_k = {k: {key: defaultdict(int) for key in fibers} for k in ks}
    combos_by_k = {k: tuple(combinations(range(n), k)) for k in ks}
    for key, fiber in fibers.items():
        for pi in fiber:
            parent_score = same_block_score(pi)
            for k, combos in combos_by_k.items():
                row = hist_by_k[k][key]
                for positions in combos:
                    child = delete_positions(pi, positions)
                    a = same_block_score(child)
                    b = parent_score - a
                    row[(a, b)] += 1
    out = {}
    for k in ks:
        denom = math.comb(n, k)
        out[k] = {
            key: tuple(sorted((item, Fraction(count, denom * counts[key])) for item, count in row.items()))
            for key, row in hist_by_k[k].items()
        }
        print(f"  built N={n} k={k} boundary histogram")
    return out


def atoms_from_colors(colors):
    atoms = defaultdict(list)
    for key, color in colors.items():
        atoms[color].append(key)
    return atoms


def boundary_base_colors(n):
    colors = {}
    for key in reps_by_n[n]:
        flags = feature_cache[n]["flags"]
        flags3 = flags[3][key]
        flags4 = flags[4][key]
        flags5 = flags[5][key]
        colors[key] = (
            feature_cache[n]["known"][key],
            flags3.get(36, 0),
            flags5.get(549376, 0),
            flags4.get(2176, 0),
            flags4.get(206, 0),
            flags5.get(24576, 0),
            flags5.get(912, 0) + flags5.get(664, 0),
        )
    return colors


def boundary_conflict_pairs(colors, hist_by_k, ks):
    pair_to_ks = defaultdict(set)
    for k in ks:
        atoms = atoms_from_colors(colors)
        for keys in atoms.values():
            buckets = defaultdict(list)
            for key in keys:
                buckets[hist_by_k[k][key]].append(key)
            if len(buckets) <= 1:
                continue
            for idx, left in enumerate(keys):
                for right in keys[idx + 1 :]:
                    if hist_by_k[k][left] != hist_by_k[k][right]:
                        pair = (left, right) if left < right else (right, left)
                        pair_to_ks[pair].add(k)
    return pair_to_ks


def boundary_profile(key, hist_by_k, ks):
    return tuple((k, hist_by_k[k][key]) for k in ks)


def diamond_center_colors(colors, hist_by_k, ks):
    return {
        key: (colors[key], boundary_profile(key, hist_by_k, ks))
        for key in colors
    }


def center_conflict_count(colors, hist_by_k, ks):
    conflicts = 0
    for k in ks:
        for keys in atoms_from_colors(colors).values():
            buckets = defaultdict(int)
            for key in keys:
                buckets[hist_by_k[k][key]] += 1
            if len(buckets) <= 1:
                continue
            total_pairs = len(keys) * (len(keys) - 1) // 2
            same_pairs = sum(size * (size - 1) // 2 for size in buckets.values())
            conflicts += total_pairs - same_pairs
    return conflicts


def graph_summary(conflict_pairs):
    vertices = set()
    adjacency = defaultdict(set)
    for left, right in conflict_pairs:
        vertices.add(left)
        vertices.add(right)
        adjacency[left].add(right)
        adjacency[right].add(left)
    seen = set()
    components = []
    for vertex in sorted(vertices):
        if vertex in seen:
            continue
        stack = [vertex]
        seen.add(vertex)
        comp = []
        while stack:
            current = stack.pop()
            comp.append(current)
            for nxt in adjacency[current]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        components.append(tuple(sorted(comp)))
    return {
        "vertices": len(vertices),
        "edges": len(conflict_pairs),
        "components": len(components),
        "component_sizes": tuple(sorted((len(c) for c in components), reverse=True)),
    }


def dual_signature(key, orbit):
    flags5 = feature_cache[9]["flags"][5][key]
    left, right = orbit
    odd = flags5.get(left, 0) - flags5.get(right, 0)
    return (flags5.get(left, 0) + flags5.get(right, 0), odd * odd)


def boundary_activation(orbit, conflict_pairs):
    separated = 0
    touched_ks = set()
    for (left, right), ks in conflict_pairs.items():
        if dual_signature(left, orbit) != dual_signature(right, orbit):
            separated += 1
            touched_ks.update(ks)
    return separated, tuple(sorted(touched_ks))


def edge_cover_for_orbit(orbit, edge_ids):
    covered = set()
    for pair, edge_id in edge_ids.items():
        left, right = pair
        if dual_signature(left, orbit) != dual_signature(right, orbit):
            covered.add(edge_id)
    return frozenset(covered)


def minimal_covers(cover_by_orbit, target_edges):
    orbits = tuple(orbit for orbit, cover in cover_by_orbit.items() if cover)
    for size in range(1, len(orbits) + 1):
        rows = []
        for combo in combinations(orbits, size):
            covered = frozenset().union(*(cover_by_orbit[orbit] for orbit in combo))
            if covered == target_edges:
                rows.append(combo)
        if rows:
            return size, tuple(rows)
    return None, tuple()


def sector_feature_rows(n, pairs):
    rows = {}
    for key in reps_by_n[n]:
        base = feature_cache[n]["known"][key]
        flags5 = feature_cache[n]["flags"][5][key]
        vals = pair_values(flags5, pairs)
        full_extra = tuple((flags5.get(a, 0), flags5.get(b, 0)) for a, b in pairs)
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


SELECTED_CAMPAIGN_S = (
    (912, 25104),
    (17288, 525076),
    (24576, 540672),
)

print("=" * 80)
print("Paper 30 diamond-boundary center campaign")
print("=" * 80)
print(f"Decimal precision: prec={getcontext().prec}")

counts_by_n = {}
reps_by_n = {}
exact_by_n = {}
fibers_by_n = {}

print("\n" + "=" * 80)
print("Exact record universes")
print("=" * 80)
for n in range(1, 10):
    counts, reps, dist, fibers = build_record_universe(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    exact_by_n[n] = dist
    fibers_by_n[n] = fibers

print("\n" + "=" * 80)
print("Deletion graph")
print("=" * 80)
decks, reverse = build_decks_and_reverse(reps_by_n, 1, 9)

print("\n" + "=" * 80)
print("Feature cache")
print("=" * 80)
feature_cache = build_feature_cache(reps_by_n, 1, 9)
ORBITS = dual_orbits(all_flag_keys(5))
print(f"  order-dual flag5 orbits={len(ORBITS)}")

print("\n" + "=" * 80)
print("1. N=9 diamond-boundary residual")
print("=" * 80)
ks = (1, 2, 3, 4)
hist9 = multihole_histograms_all(9, ks, counts_by_n[9], fibers_by_n[9])
base9 = boundary_base_colors(9)
conflict_pairs = boundary_conflict_pairs(base9, hist9, ks)
center9 = diamond_center_colors(base9, hist9, ks)
center_conflicts = center_conflict_count(center9, hist9, ks)
graph = graph_summary(conflict_pairs)
print(
    f"  base atoms={len(set(base9.values()))}/{len(base9)} "
    f"diamond_center_atoms={len(set(center9.values()))}/{len(center9)} "
    f"unique_residual_pairs={len(conflict_pairs)} "
    f"graph_vertices={graph['vertices']} components={graph['components']} "
    f"component_sizes={graph['component_sizes']} "
    f"center_conflicts={center_conflicts} "
    f"per_k={{{', '.join(str(k) + ':' + str(sum(1 for v in conflict_pairs.values() if k in v)) for k in ks)}}}"
)

print("\n" + "=" * 80)
print("2. Boundary licensing of order-dual flag5 orbits")
print("=" * 80)
activation_rows = []
for orbit in ORBITS:
    separated, touched = boundary_activation(orbit, conflict_pairs)
    activation_rows.append(
        {
            "orbit": orbit,
            "separated": separated,
            "touched": touched,
        }
    )
activation_rows.sort(key=lambda row: (-row["separated"], row["orbit"]))
licensed_orbits = tuple(row["orbit"] for row in activation_rows if row["separated"] > 0)
print(f"  licensed_orbits={len(licensed_orbits)}/{len(ORBITS)}")
for rank, row in enumerate(activation_rows[:12], start=1):
    print(
        f"  license-rank={rank:<2} orbit={row['orbit']} "
        f"separates={row['separated']} ks={row['touched']}"
    )

selected_activation = {
    orbit: next(row for row in activation_rows if row["orbit"] == orbit)
    for orbit in SELECTED_CAMPAIGN_S
}
for orbit, row in selected_activation.items():
    print(
        f"  Campaign-S orbit {orbit}: separates={row['separated']} ks={row['touched']}"
    )

print("\n" + "=" * 80)
print("2b. Diamond-first residual graph cover")
print("=" * 80)
edge_ids = {
    pair: edge_id
    for edge_id, pair in enumerate(sorted(conflict_pairs))
}
target_edges = frozenset(edge_ids.values())
cover_by_orbit = {
    orbit: edge_cover_for_orbit(orbit, edge_ids)
    for orbit in ORBITS
}
licensed_cover_by_orbit = {
    orbit: cover
    for orbit, cover in cover_by_orbit.items()
    if cover
}
min_cover_size, min_covers = minimal_covers(licensed_cover_by_orbit, target_edges)
campaign_s_cover = frozenset().union(
    *(cover_by_orbit[orbit] for orbit in SELECTED_CAMPAIGN_S)
)
print(
    f"  residual_edges={len(target_edges)} "
    f"licensed_edge_separators={len(licensed_cover_by_orbit)} "
    f"min_cover_size={min_cover_size} min_cover_count={len(min_covers)}"
)
print(f"  Campaign-S edge cover={tuple(sorted(campaign_s_cover))}")
for rank, combo in enumerate(min_covers[:12], start=1):
    print(f"  min-cover-rank={rank:<2} cover={combo}")

print("\n" + "=" * 80)
print("3. Low-order gate restricted to boundary-licensed orbits")
print("=" * 80)
low_rows = []
for pairs in combinations(licensed_orbits, 3):
    _colors, weights, metrics = model(pairs, "agg_l2", range(1, 8))
    tv7 = forward_tv_to(weights, 7)
    rec7 = recurrence_errors(7, weights[7], weights[6])
    if tv7 == 0 and rec7[0] == 0 and rec7[1] == 0:
        low_rows.append(
            {
                "pairs": pairs,
                "tv7": tv7,
                "rec7": rec7[0],
                "qrec7": rec7[1],
                "atoms7": metrics[7]["atoms"],
            }
        )
low_rows.sort(key=lambda row: (-row["atoms7"], row["pairs"]))
print(f"  low_gate_count={len(low_rows)} from licensed_triples={math.comb(len(licensed_orbits), 3)}")
for rank, row in enumerate(low_rows[:8], start=1):
    marker = "Campaign-S" if row["pairs"] == SELECTED_CAMPAIGN_S else ""
    print(f"  low-rank={rank:<2} {marker:<10} atoms7={row['atoms7']} pairs={row['pairs']}")

print("\n" + "=" * 80)
print("4. Projective recurrence/coarseness selector inside licensed set")
print("=" * 80)
sector_rows = []
for idx, row in enumerate(low_rows, start=1):
    pairs = row["pairs"]
    _colors, weights, metrics = model(pairs, "agg_l2", (8, 9))
    rec9 = recurrence_errors(9, weights[9], weights[8])
    if rec9[0] == 0 and rec9[1] == 0 and not metrics[9]["lookup"]:
        sector_rows.append(
            {
                "pairs": pairs,
                "rec9": rec9[0],
                "qrec9": rec9[1],
                "atoms9": metrics[9]["atoms"],
                "lookup9": metrics[9]["lookup"],
            }
        )
    if idx % 32 == 0 or idx == len(low_rows):
        print(f"    recurrence gate audited: {idx}/{len(low_rows)}")
sector_rows.sort(key=lambda row: (row["atoms9"], row["pairs"]))
selected_sector = sector_rows[0] if sector_rows else None
print(f"  recurrence_gate_count={len(sector_rows)}")
for rank, row in enumerate(sector_rows[:10], start=1):
    marker = "SELECTED" if row is selected_sector else ""
    print(
        f"  sector-rank={rank:<2} {marker:<8} atoms9={row['atoms9']} "
        f"pairs={row['pairs']}"
    )

print("\n" + "=" * 80)
print("5. Held-out audit and odd metric selector")
print("=" * 80)
if selected_sector is None:
    selected_pairs = ()
    selected_tv9 = Fraction(1)
    selected_rec9 = (Fraction(1), Fraction(1))
    metric_rows = []
    selected_metric = None
    metric_tv9 = Fraction(1)
    metric_rec9 = (Fraction(1), Fraction(1))
    metric_metrics = {9: {"lookup": True, "atoms": 0}}
else:
    selected_pairs = selected_sector["pairs"]
    selected_colors, selected_weights, selected_metrics = model(selected_pairs, "agg_l2", range(1, 10))
    selected_tv9 = forward_tv_to(selected_weights, 9)
    selected_rec9 = recurrence_errors(9, selected_weights[9], selected_weights[8])
    print(f"  selected_pairs={selected_pairs}")
    print(
        f"  unweighted atoms9={selected_metrics[9]['atoms']} "
        f"TV9={fmt_frac(selected_tv9, 30)} "
        f"rec9={fmt_frac(selected_rec9[0], 30)} qrec9={fmt_frac(selected_rec9[1], 30)}"
    )

    selected_rows = {n: sector_feature_rows(n, selected_pairs) for n in (8, 9)}
    full_colors = {n: colors_from_sector_rows(selected_rows[n], "full") for n in (8, 9)}
    full_weights = {n: atom_weights(full_colors[n], counts_by_n[n]) for n in (8, 9)}
    full_rec9 = recurrence_errors(9, full_weights[9], full_weights[8])
    print(
        f"  selected full-sector rec9={fmt_frac(full_rec9[0], 30)} "
        f"qrec9={fmt_frac(full_rec9[1], 30)}"
    )

    metric_rows = []
    seen_metrics = set()
    for raw_weights in product(range(0, 7), repeat=3):
        metric = normalize_weights(raw_weights)
        if metric is None or metric in seen_metrics:
            continue
        seen_metrics.add(metric)
        colors = {n: colors_from_sector_rows(selected_rows[n], "metric", metric) for n in (8, 9)}
        weights = {n: atom_weights(colors[n], counts_by_n[n]) for n in (8, 9)}
        metrics = {n: atom_metrics(colors[n]) for n in (8, 9)}
        identities = [
            coarsening_identity(full_colors, colors, full_weights, weights, n)
            for n in (8, 9)
        ]
        collapse_ok = all(violations == 0 and maxdiff == 0 for violations, maxdiff in identities)
        if collapse_ok:
            metric_rows.append(
                {
                    "metric": metric,
                    "atoms9": metrics[9]["atoms"],
                    "max_atom9": metrics[9]["max_atom"],
                }
            )
    metric_rows.sort(key=lambda row: (row["atoms9"], row["metric"]))
    selected_metric = metric_rows[0] if metric_rows else None
    print(f"  admissible_metric_count={len(metric_rows)}")
    for rank, row in enumerate(metric_rows[:8], start=1):
        marker = "SELECTED" if row is selected_metric else ""
        print(
            f"  metric-rank={rank:<2} {marker:<8} metric={row['metric']} "
            f"atoms9={row['atoms9']} max_atom9={row['max_atom9']}"
        )

    if selected_metric is None:
        metric_tv9 = Fraction(1)
        metric_rec9 = (Fraction(1), Fraction(1))
        metric_metrics = {9: {"lookup": True, "atoms": 0}}
    else:
        metric = selected_metric["metric"]
        metric_colors, metric_weights, metric_metrics = model(
            selected_pairs,
            "metric",
            range(1, 10),
            metric=metric,
        )
        metric_tv9 = forward_tv_to(metric_weights, 9)
        metric_rec9 = recurrence_errors(9, metric_weights[9], metric_weights[8])
        print(
            f"  selected_metric={metric} atoms9={metric_metrics[9]['atoms']} "
            f"TV9={fmt_frac(metric_tv9, 30)} "
            f"rec9={fmt_frac(metric_rec9[0], 30)} qrec9={fmt_frac(metric_rec9[1], 30)}"
        )

print("\n" + "=" * 80)
print("Hostile review")
print("=" * 80)
print(
    "1. Boundary licensing is not allowed to inspect held-out TV. It only asks "
    "whether a dual orbit separates residual multi-hole boundary conflicts."
)
print(
    "2. A licensed orbit is not automatically physical. Boundary activation is "
    "a necessary gate; recurrence and coarseness do the physical selection."
)
print(
    "3. The stronger coordinate-cover target fails: the diamond center closes "
    "all residual edges, but the tested dual-flag coordinate library does not. "
    "The selected quotient is a positive h-transform shadow of the center, not "
    "a reconstruction of the center."
)
print(
    "4. The receipt is finite and sector-scoped: it audits N<=9 permutation-order "
    "records, order-dual flag5 orbits, and diagonal quadratic odd metrics."
)

check(
    "diamond-boundary residual is nontrivial after the current cover",
    len(conflict_pairs) > 0,
    f"residual_pairs={len(conflict_pairs)}",
)
check(
    "diamond-first center closes the residual without becoming lookup",
    center_conflicts == 0 and len(set(base9.values())) < len(set(center9.values())) < len(center9),
    (
        f"base_atoms={len(set(base9.values()))} center_atoms={len(set(center9.values()))} "
        f"records={len(center9)} center_conflicts={center_conflicts}"
    ),
)
check(
    "boundary licensing is selective but nonempty",
    0 < len(licensed_orbits) < len(ORBITS),
    f"licensed={len(licensed_orbits)} total={len(ORBITS)}",
)
check(
    "dual-flag coordinate library does not reconstruct the full diamond center",
    min_cover_size is None and len(licensed_cover_by_orbit) > 0,
    (
        f"residual_edges={len(target_edges)} "
        f"licensed_edge_separators={len(licensed_cover_by_orbit)} "
        f"min_cover_size={min_cover_size}"
    ),
)
check(
    "Campaign-S dual sectors are boundary-licensed before final TV is audited",
    all(row["separated"] > 0 for row in selected_activation.values()),
    ", ".join(f"{orbit}:{row['separated']}" for orbit, row in selected_activation.items()),
)
check(
    "Campaign-S dual sectors are a proper nonreconstructive shadow of the diamond center",
    0 < len(campaign_s_cover) < len(target_edges),
    f"covered={len(campaign_s_cover)}/{len(target_edges)}",
)
check(
    "licensed recurrence/coarseness selector recovers the Campaign-S sector triple",
    selected_sector is not None and selected_sector["pairs"] == SELECTED_CAMPAIGN_S,
    f"selected={selected_pairs}",
)
check(
    "selected licensed sector has exact held-out N=9 forward law under audit",
    selected_tv9 == 0 and selected_rec9[0] == 0 and selected_rec9[1] == 0,
    f"TV9={fmt_frac(selected_tv9, 24)} rec9={fmt_frac(selected_rec9[0], 24)}",
)
check(
    "metric selector recovers the Campaign-S odd quadratic metric",
    selected_metric is not None and selected_metric["metric"] == (5, 5, 3),
    f"selected_metric={None if selected_metric is None else selected_metric['metric']}",
)
check(
    "selected licensed metric preserves exact held-out N=9 forward law",
    metric_tv9 == 0 and metric_rec9[0] == 0 and metric_rec9[1] == 0,
    (
        f"metric={None if selected_metric is None else selected_metric['metric']} "
        f"TV9={fmt_frac(metric_tv9, 24)} rec9={fmt_frac(metric_rec9[0], 24)}"
    ),
)
check(
    "selected licensed metric remains nonlookup",
    selected_metric is not None and not metric_metrics[9]["lookup"],
    f"metric_atoms={metric_metrics[9]['atoms']} records={len(reps_by_n[9])}",
)

print("\n=== Campaign status ===")
print(
    "The diamond-first version changes the interpretation.  The coarsest "
    "diamond boundary center closes the exact residual graph directly.  The "
    "tested dual-flag coordinate library cannot reconstruct that full center, "
    "which is good for non-reconstruction and falsifies the naive flag-cover "
    "reading.  The selected quotient is instead a boundary-activated, "
    "projectively selected positive h-transform shadow of the sealed record "
    "diamond center."
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
