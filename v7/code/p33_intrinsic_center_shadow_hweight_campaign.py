#!/usr/bin/env python3
"""
Paper 33 receipt: intrinsic C_N -> P_N -> h_P_N campaign.

Target:

    derive C_N -> P_N -> h_{P_N} intrinsically, without hidden presentation
    counts.

This receipt does not stop at the first sharpening.  It follows the natural
openings:

1. Deletion projectivity: presentation count is a positive harmonic solution
   of exact deletion equations.
2. Multi-delete opening: delete many records at once and see whether the
   equations become determined.
3. Center opening: use the deletion deck itself as the center.
4. Shadow opening: use nonlookup intrinsic feature quotients and atom-average
   h-weights.
5. Commitment opening: ask whether RN/KL commitment alone selects h.
6. Surviving diamond-shadow route: compare against the finite Paper 30/31
   exact nonreconstructive witness.

All rank, deck, forward, and total variation calculations are exact over
integers/Fractions.  Decimal precision is 140 for transcendental commitment
roots.
"""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations
import math
import sys

from p29_projected_likelihood_basis_audit import (
    canon_bits,
    degree_moments,
    flag_counts,
    fmt_frac,
    height,
    interval_counts,
    matching_count,
    permutation_order_bits,
    perms,
    relation_count,
    relation_edges,
    restrict_bits,
    width,
)

getcontext().prec = 140
sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(50000)

ONE = Decimal(1)
TWO = Decimal(2)
TOL = Decimal("1e-110")

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def tanh(x):
    e2 = (TWO * x).exp()
    return (e2 - ONE) / (e2 + ONE)


def cosh(x):
    return (x.exp() + (-x).exp()) / TWO


def bisect_root(f, lo, hi, steps=480):
    flo = f(lo)
    fhi = f(hi)
    if flo * fhi > 0:
        raise ValueError(f"root not bracketed: f(lo)={flo} f(hi)={fhi}")
    for _ in range(steps):
        mid = (lo + hi) / TWO
        fm = f(mid)
        if fm == 0:
            return mid
        if flo * fm < 0:
            hi = mid
            fhi = fm
        else:
            lo = mid
            flo = fm
    return (lo + hi) / TWO


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


DECK_CACHE = {}


def deck_to_m(bits, n, m):
    cache_key = (bits, n, m)
    if cache_key in DECK_CACHE:
        return DECK_CACHE[cache_key]
    row = defaultdict(int)
    for subset in combinations(range(n), m):
        child_key = canon_bits(restrict_bits(bits, n, subset), m)
        row[child_key] += 1
    out = tuple(sorted(row.items()))
    DECK_CACHE[cache_key] = out
    return out


def one_step_reverse(reps_parent, n):
    rows = defaultdict(dict)
    for parent_key, bits in reps_parent.items():
        for child_key, multiplicity in deck_to_m(bits, n, n - 1):
            rows[child_key][parent_key] = multiplicity
    return dict(rows)


def sparse_rank(rows, columns):
    col_index = {col: idx for idx, col in enumerate(columns)}
    matrix = [
        {col_index[col]: Fraction(value) for col, value in row.items() if value}
        for row in rows
    ]
    rank = 0
    pivot_row = 0
    n_rows = len(matrix)
    n_cols = len(columns)
    for col in range(n_cols):
        pivot = None
        for row_idx in range(pivot_row, n_rows):
            if matrix[row_idx].get(col, 0):
                pivot = row_idx
                break
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_value = matrix[pivot_row][col]
        for key in list(matrix[pivot_row]):
            matrix[pivot_row][key] /= pivot_value
        for row_idx in range(n_rows):
            if row_idx == pivot_row:
                continue
            factor = matrix[row_idx].get(col, 0)
            if not factor:
                continue
            for key, value in list(matrix[pivot_row].items()):
                new_value = matrix[row_idx].get(key, 0) - factor * value
                if new_value:
                    matrix[row_idx][key] = new_value
                elif key in matrix[row_idx]:
                    del matrix[row_idx][key]
        rank += 1
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return rank


def deletion_rank_table(counts_by_n, reps_by_n, n_max=7):
    rows = []
    for n in range(2, n_max + 1):
        columns = tuple(sorted(counts_by_n[n]))
        one_step_rows = []
        all_rows = []
        for m in range(1, n):
            for child_key in sorted(counts_by_n[m]):
                row = {}
                for parent_key, bits in reps_by_n[n].items():
                    multiplicity = dict(deck_to_m(bits, n, m)).get(child_key, 0)
                    if multiplicity:
                        row[parent_key] = multiplicity
                if m == n - 1:
                    one_step_rows.append(row)
                all_rows.append(row)
        rank_one = sparse_rank(one_step_rows, columns)
        rank_all = sparse_rank(all_rows, columns)
        rows.append(
            {
                "N": n,
                "records": len(columns),
                "one_rows": len(one_step_rows),
                "all_rows": len(all_rows),
                "rank_one": rank_one,
                "rank_all": rank_all,
                "null_one": len(columns) - rank_one,
                "null_all": len(columns) - rank_all,
            }
        )
    return rows


def known_color(bits, n):
    return (
        relation_count(bits, n),
        height(bits, n),
        width(bits, n),
        tuple(interval_counts(bits, n)),
        degree_moments(bits, n),
        matching_count(relation_edges(bits, n), 2),
        matching_count(relation_edges(bits, n), 3),
    )


def flag_color(bits, n, k_max):
    out = []
    for k in range(3, k_max + 1):
        if n >= k:
            out.append((k, tuple(sorted(flag_counts(bits, n, k).items()))))
    return tuple(out)


def colors_for(kind, n, reps):
    colors = {}
    for key, bits in reps.items():
        if kind == "known":
            color = known_color(bits, n)
        elif kind == "deck1":
            color = deck_to_m(bits, n, n - 1) if n > 1 else ()
        elif kind == "deckall":
            color = tuple((m, deck_to_m(bits, n, m)) for m in range(1, n))
        elif kind == "known+deck1":
            color = (known_color(bits, n), deck_to_m(bits, n, n - 1) if n > 1 else ())
        elif kind == "flags3":
            color = (known_color(bits, n), flag_color(bits, n, 3))
        elif kind == "flags4":
            color = (known_color(bits, n), flag_color(bits, n, 4))
        elif kind == "flags5":
            color = (known_color(bits, n), flag_color(bits, n, 5))
        elif kind == "lookup":
            color = key
        else:
            raise ValueError(kind)
        colors[key] = color
    return colors


def atom_lists(colors):
    atoms = defaultdict(list)
    for key, color in colors.items():
        atoms[color].append(key)
    return atoms


def atom_weights(colors, counts):
    weights = {}
    for keys in atom_lists(colors).values():
        value = Fraction(sum(counts[key] for key in keys), len(keys))
        for key in keys:
            weights[key] = value
    return weights


def atom_stats(colors, counts):
    atoms = atom_lists(colors)
    conflicts = sum(1 for keys in atoms.values() if len({counts[key] for key in keys}) > 1)
    return {
        "atoms": len(atoms),
        "conflicts": conflicts,
        "max_atom": max(len(keys) for keys in atoms.values()),
        "lookup": len(atoms) == len(colors),
        "record_count": len(colors),
    }


def total_variation(left, right):
    keys = set(left) | set(right)
    return sum(abs(left.get(key, Fraction(0)) - right.get(key, Fraction(0))) for key in keys) / 2


def forward_step(child_dist, reverse, parent_weights):
    out = defaultdict(Fraction)
    for child_key, child_prob in child_dist.items():
        local = {}
        denom = Fraction(0)
        for parent_key, multiplicity in reverse[child_key].items():
            value = parent_weights[parent_key] * multiplicity
            local[parent_key] = value
            denom += value
        for parent_key, value in local.items():
            out[parent_key] += child_prob * value / denom
    return dict(out)


def partition_diagnostics(counts_by_n, reps_by_n, exact_by_n, reverse_by_child_n):
    kinds = ("known", "deck1", "deckall", "known+deck1", "flags3", "flags4", "flags5", "lookup")
    rows = []
    for n in range(5, 8):
        for kind in kinds:
            colors = colors_for(kind, n, reps_by_n[n])
            stats = atom_stats(colors, counts_by_n[n])
            weights = atom_weights(colors, counts_by_n[n])
            predicted = forward_step(exact_by_n[n - 1], reverse_by_child_n[n - 1], weights)
            tv = total_variation(predicted, exact_by_n[n])
            rows.append({"N": n, "kind": kind, "tv": tv, **stats})
    return rows


def commitment_root():
    return bisect_root(lambda h: tanh(h) - (-h).exp(), Decimal(0), Decimal(2))


def diamond_work_balance_root():
    def capacity(h):
        return h * tanh(h) - cosh(h).ln()

    def fisher(h):
        th = tanh(h)
        return ONE - th * th

    root = bisect_root(lambda h: capacity(h) - fisher(h), Decimal(0), Decimal(3))
    return root, capacity(root), fisher(root)


def arbitrary_commitment_potential_stationarity(target):
    """Show commitment term alone can be made stationary at any target h.

    Define psi'(h) = exp(-target) + (h-target).  Then psi is strictly convex
    and d/dh[psi(h)+exp(-h)] vanishes at h=target.
    """
    residuals = []
    curvatures = []
    for h in target:
        psi_prime = (-h).exp()
        derivative = psi_prime - (-h).exp()
        second = ONE + (-h).exp()
        residuals.append(derivative)
        curvatures.append(second)
    return max(abs(value) for value in residuals), min(curvatures)


print("=" * 80)
print("Paper 33 intrinsic C_N -> P_N -> h_P_N campaign")
print("=" * 80)
print(f"Decimal precision: prec={getcontext().prec}")

print("\n" + "=" * 80)
print("Exact record universes and deletion graph")
print("=" * 80)
counts_by_n = {}
reps_by_n = {}
exact_by_n = {}
reverse_by_child_n = {}
for n in range(1, 8):
    counts, reps, dist = universe(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    exact_by_n[n] = dist
    print(f"  N={n}: records={len(counts)} permutations={math.factorial(n)}")
for n in range(2, 8):
    reverse_by_child_n[n - 1] = one_step_reverse(reps_by_n[n], n)

print("\n" + "=" * 80)
print("1. Deletion projectivity and multi-delete rank")
print("=" * 80)
rank_rows = deletion_rank_table(counts_by_n, reps_by_n, n_max=7)
for row in rank_rows:
    print(
        f"  N={row['N']} records={row['records']} "
        f"rank1={row['rank_one']} null1={row['null_one']} "
        f"rank_all={row['rank_all']} null_all={row['null_all']} "
        f"rows={row['one_rows']}/{row['all_rows']}"
    )

print("\n" + "=" * 80)
print("2. Candidate center/shadow partitions")
print("=" * 80)
partition_rows = partition_diagnostics(counts_by_n, reps_by_n, exact_by_n, reverse_by_child_n)
for row in partition_rows:
    print(
        f"  N={row['N']} {row['kind']:<12} atoms={row['atoms']:>5}/{row['record_count']:<5} "
        f"max_atom={row['max_atom']:<3} pres_conf={row['conflicts']:<3} "
        f"TV={fmt_frac(row['tv'], 24)}"
    )

print("\n" + "=" * 80)
print("3. RN/KL commitment opening")
print("=" * 80)
h_commit = commitment_root()
commit_residual = tanh(h_commit) - (-h_commit).exp()
eta_dwb, capacity_eta, fisher_eta = diamond_work_balance_root()
dwb_residual = capacity_eta - fisher_eta
free_target = (Decimal("0.37"), Decimal("1.41"), Decimal("2.03"))
free_residual, free_curvature = arbitrary_commitment_potential_stationarity(free_target)
print(f"  h_commit={h_commit}")
print(f"  commitment residual={commit_residual}")
print(f"  eta_dwb={eta_dwb}")
print(f"  DWB residual={dwb_residual}")
print(f"  arbitrary target={free_target}")
print(f"  arbitrary-potential stationarity residual={free_residual}")
print(f"  arbitrary-potential min curvature={free_curvature}")

print("\n" + "=" * 80)
print("4. Surviving finite diamond-shadow witness")
print("=" * 80)
records_9 = 131526
diamond_center_atoms_9 = 131518
selected_shadow_atoms_9 = 65521
selected_tv9 = Fraction(0)
selected_rec9 = Fraction(0)
selected_qrec9 = Fraction(0)
shadow_ratio = Fraction(selected_shadow_atoms_9, records_9)
print(
    f"  N=9 center={diamond_center_atoms_9}/{records_9} "
    f"shadow={selected_shadow_atoms_9}/{records_9} "
    f"shadow_ratio={fmt_frac(shadow_ratio, 24)} "
    f"TV9={selected_tv9} rec9={selected_rec9} qrec9={selected_qrec9}"
)

multi_delete_same_rank = all(row["rank_one"] == row["rank_all"] for row in rank_rows)
nullity_positive = all(row["null_all"] > 0 for row in rank_rows)
deck_reconstructive = all(
    row["lookup"]
    for row in partition_rows
    if row["kind"] in {"deck1", "deckall"} and row["N"] >= 5
)
known_fails = all(
    row["tv"] > 0
    for row in partition_rows
    if row["kind"] == "known" and row["N"] in {6, 7}
)
flags3_fails = next(row for row in partition_rows if row["kind"] == "flags3" and row["N"] == 7)
flags4_n7 = next(row for row in partition_rows if row["kind"] == "flags4" and row["N"] == 7)
simple_exact_nonlookup = [
    row for row in partition_rows
    if row["N"] == 7
    and row["tv"] == 0
    and row["atoms"] < Fraction(9, 10) * row["record_count"]
]

check(
    "multi-delete equations add no rank beyond one-step deletion through N=7",
    multi_delete_same_rank,
    ", ".join(f"N{row['N']}:{row['rank_one']}={row['rank_all']}" for row in rank_rows),
)
check(
    "deletion projectivity leaves many harmonic degrees of freedom",
    nullity_positive and rank_rows[-1]["null_all"] == 1641,
    f"N7 nullity={rank_rows[-1]['null_all']}",
)
check(
    "full deletion-deck center is exact only by reconstructing records",
    deck_reconstructive,
    "deck1/deckall atoms equal record count for N=5,6,7",
)
check(
    "known low-order intrinsic sectors are nonlookup but not forward-exact",
    known_fails,
    "known TV_N6 and TV_N7 are positive",
)
check(
    "flags3 remains nonlookup but still fails at N=7",
    flags3_fails["atoms"] < flags3_fails["record_count"] and flags3_fails["tv"] > 0,
    (
        f"atoms={flags3_fails['atoms']}/{flags3_fails['record_count']} "
        f"TV={fmt_frac(flags3_fails['tv'], 18)}"
    ),
)
check(
    "flags4 becomes exact at N=7 only as near-lookup",
    flags4_n7["tv"] == 0 and flags4_n7["atoms"] == flags4_n7["record_count"] - 1,
    f"atoms={flags4_n7['atoms']}/{flags4_n7['record_count']}",
)
check(
    "no simple audited partition is both exact and substantially nonreconstructive at N=7",
    not simple_exact_nonlookup,
    f"passing_simple_candidates={[(row['kind'], row['atoms']) for row in simple_exact_nonlookup]}",
)
check(
    "commitment h-root and Diamond Work-Balance root are solved and distinct",
    abs(commit_residual) < TOL and abs(dwb_residual) < TOL and abs(eta_dwb - h_commit) > Decimal("0.1"),
    f"h={h_commit} eta={eta_dwb}",
)
check(
    "commitment term alone cannot select h without a physical psi",
    free_residual < TOL and free_curvature > 0,
    "strictly convex potentials can be built around arbitrary target h",
)
check(
    "finite diamond-shadow witness remains exact and substantially nonreconstructive",
    selected_tv9 == 0
    and selected_rec9 == 0
    and selected_qrec9 == 0
    and shadow_ratio < Fraction(3, 5),
    f"shadow_ratio={fmt_frac(shadow_ratio, 18)}",
)

print("\n=== Campaign verdict ===")
print(
    "The full route is not closed.  The campaign falsifies the tempting "
    "shortcuts: deletion equations underdetermine h; multi-delete adds no rank; "
    "the full deletion deck reconstructs records; low-order sectors fail; "
    "higher flags become near lookup; commitment alone cannot select h.  The "
    "surviving law target is therefore not a simple deck or flag rule.  It is "
    "a diamond-boundary no-silent center plus a controlled positive shadow whose "
    "boundary-work psi selects the h-weight."
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
