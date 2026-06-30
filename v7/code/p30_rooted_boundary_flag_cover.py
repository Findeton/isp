#!/usr/bin/env python3
"""
Paper 30 receipt: rooted boundary flag cover.

Paper 29 found the compressed deletion-boundary object

    Hbar_R(a,b) = P(child score = a, score loss = b | parent record R)

and showed that ordinary unrooted local flags cover Hbar conflicts at N=7,8,
but with drifting covers.  The obvious critique is that Hbar is a rooted
deletion-boundary object, while ordinary induced flags are unrooted.

This receipt builds rooted induced-suborder flags: choose a root vertex v,
choose k-1 other vertices, record the induced k-suborder with v distinguished,
and aggregate these rooted types over all roots.  These are still committed
record observables; the root is summed over and is not a hidden trajectory.

All finite counts are exact integers/Fractions.  Decimal reporting uses
mpmath with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
import math
import sys

from p29_projected_likelihood_basis_audit import (
    bit_index,
    canon_bits,
    feature_maps,
    fmt_frac,
    has_rel,
    permutation_order_bits,
    perms,
    relabel_bits,
    restrict_bits,
    same_block_score,
)

sys.setrecursionlimit(10000)
sys.stdout.reconfigure(line_buffering=True)
try:
    import mpmath as mp

    mp.mp.dps = 140
    PRECISION_LINE = f"mp.dps = {mp.mp.dps}"
except ModuleNotFoundError:
    mp = None
    PRECISION_LINE = (
        "exact integer/Fraction arithmetic; mpmath unavailable; "
        "no floating arithmetic used"
    )

checks = []
ROOTED_CANON_CACHE = {}


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def delete_position(pi, i):
    removed = pi[i]
    return tuple(value - (1 if value > removed else 0) for j, value in enumerate(pi) if j != i)


def build_score_data(n):
    p_counts = defaultdict(int)
    reps = {}
    fibers = defaultdict(list)
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        fibers[key].append(pi)
        p_counts[key] += 1
    P = {key: Fraction(count, math.factorial(n)) for key, count in p_counts.items()}
    return P, dict(p_counts), reps, dict(fibers)


def boundary_histograms(n, counts, fibers):
    hist = {key: defaultdict(int) for key in fibers}
    for key, fiber in fibers.items():
        for pi in fiber:
            parent_score = same_block_score(pi)
            for i in range(n):
                child = delete_position(pi, i)
                a = same_block_score(child)
                b = parent_score - a
                hist[key][(a, b)] += 1
    return {
        key: tuple(sorted((item, Fraction(count, n * counts[key])) for item, count in row.items()))
        for key, row in hist.items()
    }


def rooted_canon(bits, k, root):
    cache_key = (k, bits, root)
    if cache_key in ROOTED_CANON_CACHE:
        return ROOTED_CANON_CACHE[cache_key]
    others = [idx for idx in range(k) if idx != root]
    best = None
    for tail in permutations(others):
        order = (root,) + tail
        key = relabel_bits(bits, k, order)
        if best is None or key < best:
            best = key
    ROOTED_CANON_CACHE[cache_key] = best
    return best


def rooted_flag_counts(bits, n, k):
    counts = defaultdict(int)
    vertices = tuple(range(n))
    for root in vertices:
        for rest in combinations((v for v in vertices if v != root), k - 1):
            subset = (root,) + rest
            sub_bits = restrict_bits(bits, n, subset)
            key = rooted_canon(sub_bits, k, 0)
            counts[key] += 1
    return dict(counts)


def rooted_feature_maps(P, reps, n, ks=(2, 3, 4, 5)):
    rooted_by_record = {}
    all_keys = {k: set() for k in ks}
    for key in P:
        rooted_by_record[key] = {}
        bits = reps[key]
        for k in ks:
            counts = rooted_flag_counts(bits, n, k)
            rooted_by_record[key][k] = counts
            all_keys[k].update(counts)

    features = {f"root{k}": defaultdict(dict) for k in ks}
    for k in ks:
        for rooted_key in sorted(all_keys[k]):
            name = f"root{k}_{rooted_key}"
            for record_key in P:
                features[f"root{k}"][name][record_key] = rooted_by_record[record_key][k].get(rooted_key, 0)
    return features


def feature_names(features, groups):
    names = []
    for group in groups:
        for feature_name in sorted(features[group]):
            names.append(f"{group}:{feature_name}")
    return names


def feature_mapping(features, name):
    group, feature = name.split(":", 1)
    return features[group][feature]


def partition_atoms(P, features, names):
    atoms = defaultdict(list)
    for key in P:
        atoms[tuple(feature_mapping(features, name)[key] for name in names)].append(key)
    return atoms


def bad_atoms(P, features, names, invariant):
    atoms = partition_atoms(P, features, names)
    bad = []
    for atom, keys in atoms.items():
        buckets = defaultdict(list)
        for key in keys:
            buckets[invariant[key]].append(key)
        if len(buckets) > 1:
            bad.append((atom, keys))
    return atoms, bad


def conflict_pairs(bad, invariant):
    conflicts = []
    for _atom, keys in bad:
        for idx, left in enumerate(keys):
            for right in keys[idx + 1 :]:
                if invariant[left] != invariant[right]:
                    conflicts.append((left, right))
    return conflicts


def feature_conflict_mask(mapping, conflicts):
    mask = 0
    for idx, (left, right) in enumerate(conflicts):
        if mapping[left] != mapping[right]:
            mask |= 1 << idx
    return mask


def remove_dominated(candidates, masks):
    kept = []
    for candidate in sorted(candidates, key=lambda name: masks[name].bit_count(), reverse=True):
        mask = masks[candidate]
        if any(mask | masks[other] == masks[other] for other in kept):
            continue
        kept.append(candidate)
    return kept


def greedy_cover(candidates, masks, full_mask):
    uncovered = full_mask
    chosen = []
    while uncovered:
        best = max(candidates, key=lambda name: (masks[name] & uncovered).bit_count())
        gain = (masks[best] & uncovered).bit_count()
        if gain == 0:
            return None
        chosen.append(best)
        uncovered &= ~masks[best]
    return chosen


def exact_cover(candidates, masks, full_mask):
    active = [name for name in candidates if masks[name]]
    union = 0
    for name in active:
        union |= masks[name]
    if union != full_mask:
        return None, active

    reduced = remove_dominated(active, masks)
    greedy = greedy_cover(reduced, masks, full_mask)
    best = list(greedy) if greedy else list(reduced)
    max_gain = max(masks[name].bit_count() for name in reduced)

    coverers = defaultdict(list)
    for name in reduced:
        m = masks[name]
        while m:
            bit = (m & -m).bit_length() - 1
            coverers[bit].append(name)
            m &= m - 1
    for bit in coverers:
        coverers[bit].sort(key=lambda name: masks[name].bit_count(), reverse=True)

    seen = {}

    def choose_bit(uncovered):
        best_bit = None
        best_options = None
        m = uncovered
        while m:
            bit = (m & -m).bit_length() - 1
            options = [name for name in coverers[bit] if masks[name] & uncovered]
            if best_options is None or len(options) < len(best_options):
                best_bit = bit
                best_options = options
                if len(options) == 1:
                    break
            m &= m - 1
        return best_bit, best_options

    def search(uncovered, chosen):
        nonlocal best
        if not uncovered:
            if len(chosen) < len(best):
                best = list(chosen)
            return
        if len(chosen) >= len(best) - 1:
            return
        lower = (uncovered.bit_count() + max_gain - 1) // max_gain
        if len(chosen) + lower >= len(best):
            return
        state = (uncovered, len(chosen))
        if seen.get(state, 10**9) <= len(chosen):
            return
        seen[state] = len(chosen)
        _bit, options = choose_bit(uncovered)
        for name in sorted(options, key=lambda item: (masks[item] & uncovered).bit_count(), reverse=True):
            if name in chosen:
                continue
            search(uncovered & ~masks[name], chosen + [name])

    search(full_mask, [])
    return best, reduced


def cover_report(label, P, features, known, candidate_names, H):
    atoms, bad = bad_atoms(P, features, known, H)
    conflicts = conflict_pairs(bad, H)
    full_mask = (1 << len(conflicts)) - 1
    masks = {name: feature_conflict_mask(feature_mapping(features, name), conflicts) for name in candidate_names}
    active = [name for name in candidate_names if masks[name]]
    solution, reduced = exact_cover(active, masks, full_mask)
    if solution is None:
        return {
            "label": label,
            "bad": len(bad),
            "conflicts": len(conflicts),
            "active": len(active),
            "reduced": len(reduced),
            "solution": [],
            "solution_size": None,
            "unresolved_mass": None,
            "atoms": len(atoms),
        }
    solution_atoms, solution_bad = bad_atoms(P, features, known + solution, H)
    unresolved = [keys for keys in solution_atoms.values() if len(keys) > 1]
    unresolved_mass = sum(P[key] for keys in unresolved for key in keys)
    return {
        "label": label,
        "bad": len(bad),
        "conflicts": len(conflicts),
        "active": len(active),
        "reduced": len(reduced),
        "solution": solution,
        "solution_size": len(solution),
        "unresolved_mass": unresolved_mass,
        "atoms": len(solution_atoms),
        "after_bad": len(solution_bad),
    }


print("=" * 80)
print("Paper 30 rooted boundary flag cover")
print("=" * 80)
print(PRECISION_LINE)

summaries = {}
for n in [7, 8]:
    print("\n" + "=" * 80)
    print(f"N={n} rooted boundary cover")
    print("=" * 80)
    P, counts, reps, fibers = build_score_data(n)
    H = boundary_histograms(n, counts, fibers)
    base_features = feature_maps(P, reps, n)
    root_features = rooted_feature_maps(P, reps, n)
    all_features = {**base_features, **root_features}
    known = feature_names(base_features, ["scalar", "interval", "regularity", "matching"])
    unrooted_candidates = feature_names(base_features, ["flags3", "flags4", "flags5"])
    rooted_candidates = feature_names(root_features, ["root2", "root3", "root4", "root5"])
    mixed_candidates = unrooted_candidates + rooted_candidates

    unrooted = cover_report("unrooted", P, all_features, known, unrooted_candidates, H)
    rooted = cover_report("rooted", P, all_features, known, rooted_candidates, H)
    mixed = cover_report("mixed", P, all_features, known, mixed_candidates, H)
    summaries[n] = {"unrooted": unrooted, "rooted": rooted, "mixed": mixed}

    for report in [unrooted, rooted, mixed]:
        mass = "NA" if report["unresolved_mass"] is None else fmt_frac(report["unresolved_mass"], 30)
        print(
            f"{report['label']:<9} H_bad={report['bad']:>5} H_conf={report['conflicts']:>7} "
            f"active={report['active']:>4} reduced={report['reduced']:>4} "
            f"cover_size={report['solution_size']} atoms={report.get('atoms')} "
            f"unresolved_mass={mass}"
        )
        print(f"  solution={report['solution']}")

check(
    "rooted flags cover Hbar at N=7 and N=8",
    summaries[7]["rooted"]["solution_size"] is not None
    and summaries[8]["rooted"]["solution_size"] is not None,
    f"N7={summaries[7]['rooted']['solution_size']} N8={summaries[8]['rooted']['solution_size']}",
)
check(
    "rooted features are competitive with unrooted features",
    summaries[7]["rooted"]["solution_size"] <= summaries[7]["unrooted"]["solution_size"]
    and summaries[8]["rooted"]["solution_size"] <= summaries[8]["unrooted"]["solution_size"],
    (
        f"N7 rooted/unrooted={summaries[7]['rooted']['solution_size']}/"
        f"{summaries[7]['unrooted']['solution_size']} "
        f"N8 rooted/unrooted={summaries[8]['rooted']['solution_size']}/"
        f"{summaries[8]['unrooted']['solution_size']}"
    ),
)
check(
    "mixed rooted plus unrooted cover does not need more operators",
    summaries[7]["mixed"]["solution_size"] <= summaries[7]["unrooted"]["solution_size"]
    and summaries[8]["mixed"]["solution_size"] <= summaries[8]["unrooted"]["solution_size"],
    (
        f"N7 mixed={summaries[7]['mixed']['solution_size']} "
        f"N8 mixed={summaries[8]['mixed']['solution_size']}"
    ),
)
check(
    "rooted covers remain non-lookup",
    summaries[7]["rooted"]["atoms"] < len(build_score_data(7)[0])
    and summaries[8]["rooted"]["atoms"] < len(build_score_data(8)[0]),
    (
        f"N7 atoms={summaries[7]['rooted']['atoms']} "
        f"N8 atoms={summaries[8]['rooted']['atoms']}"
    ),
)

print("\n=== Rooted-cover status ===")
print(
    "Rooted deletion flags directly target the boundary nature of Hbar.  They "
    "cover the audited Hbar conflicts without promoting the full boundary tensor. "
    "The next hostile question is transfer: whether rooted covers drift less "
    "than unrooted covers across N."
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
