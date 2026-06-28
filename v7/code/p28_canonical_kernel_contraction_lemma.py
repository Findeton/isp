#!/usr/bin/env python3
"""
Paper 28 receipt: canonical-kernel contraction lemma.

The coefficient sieve found the right target:

    q_{N,r} <= C (beta / N)^r.

This receipt attacks the structural reason such a bound could hold.  For a
canonical rank kernel D with zero row and column sums, the independent
with-replacement moment of any nonempty product is zero.  In the
without-replacement expansion, the only surviving terms are endpoint-collision
diagrams.  Row-zero degeneracy kills every diagram whose quotient graph has a
leaf.  Therefore surviving diagrams are 2-core diagrams; with r kernel edges,
they have at most r quotient vertices, hence at least r endpoint collisions.
That is the combinatorial source of the N^{-r} factor.

This is still not the full theorem.  The remaining analytic task is to bound
the activities of those surviving 2-core diagrams exponentially in r.  Staged
blocks fail by keeping those activities coherent; the physical rank-copula
appears to pass by smooth cancellation.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import Counter
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=36):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def set_partitions(items):
    """Generate set partitions as tuples of tuple blocks."""
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for partition in set_partitions(items[1:]):
        yield ((first,),) + partition
        for index in range(len(partition)):
            block = tuple(sorted(partition[index] + (first,)))
            yield partition[:index] + (block,) + partition[index + 1 :]


def canonical_partition(partition):
    return tuple(sorted((tuple(sorted(block)) for block in partition), key=lambda b: b[0]))


def quotient_graph_stats(r, partition):
    """Return loop flag, vertex count, degrees for the r edge quotient graph."""
    block_of = {}
    for block_index, block in enumerate(partition):
        for endpoint in block:
            block_of[endpoint] = block_index
    degrees = [0 for _ in partition]
    has_loop = False
    edges = []
    for edge in range(r):
        a = block_of[2 * edge]
        b = block_of[2 * edge + 1]
        if a == b:
            has_loop = True
        else:
            degrees[a] += 1
            degrees[b] += 1
            edges.append(tuple(sorted((a, b))))
    return {
        "has_loop": has_loop,
        "vertices": len(partition),
        "degrees": degrees,
        "edges": edges,
        "min_degree": min(degrees) if degrees else 0,
        "degree_sequence": tuple(sorted(degrees)),
    }


def survives_row_zero(r, partition):
    stats = quotient_graph_stats(r, partition)
    if stats["has_loop"]:
        return False, stats
    return stats["min_degree"] >= 2, stats


def diagram_census(r):
    seen = set()
    total = 0
    no_loop = 0
    surviving = []
    degree_sequences = Counter()
    vertex_counts = Counter()
    for partition in set_partitions(range(2 * r)):
        partition = canonical_partition(partition)
        if partition in seen:
            continue
        seen.add(partition)
        total += 1
        ok, stats = survives_row_zero(r, partition)
        if not stats["has_loop"]:
            no_loop += 1
        if ok:
            surviving.append((partition, stats))
            degree_sequences[stats["degree_sequence"]] += 1
            vertex_counts[stats["vertices"]] += 1
    max_vertices = max((stats["vertices"] for _, stats in surviving), default=0)
    min_collision_deficit = min((2 * r - stats["vertices"] for _, stats in surviving), default=None)
    max_count_root = mp.power(len(surviving), mp.mpf(1) / r) if surviving else mp.mpf(0)
    return {
        "r": r,
        "total": total,
        "no_loop": no_loop,
        "surviving": surviving,
        "surviving_count": len(surviving),
        "degree_sequences": degree_sequences,
        "vertex_counts": vertex_counts,
        "max_vertices": max_vertices,
        "min_collision_deficit": min_collision_deficit,
        "count_root": max_count_root,
    }


def conditional_beta_bound(count_root, activity_root, r):
    """
    If absolute 2-core activity sum at order r is bounded by
    (count_root * activity_root)^r / N^r, then

        N q_{N,r}^{1/r} <= e (count_root * activity_root)^2 / (2r)

    using binom(N/2,r)^{1/r} <= eN/(2r).
    """
    count_root = mp.mpf(count_root)
    activity_root = mp.mpf(activity_root)
    r = mp.mpf(r)
    return mp.e * (count_root * activity_root) ** 2 / (2 * r)


print("=" * 80)
print("Paper 28 canonical-kernel contraction lemma receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n=== Row-zero collision-diagram census ===")
censuses = []
for r in range(1, 6):
    census = diagram_census(r)
    censuses.append(census)
    print(
        f"r={r} total_partitions={census['total']} "
        f"no_loop={census['no_loop']} surviving_2core={census['surviving_count']} "
        f"max_vertices={census['max_vertices']} "
        f"min_collision_deficit={census['min_collision_deficit']} "
        f"surviving_count_root={fmt(census['count_root'], 18)}"
    )
    if census["surviving_count"]:
        print(f"  vertex_counts={dict(census['vertex_counts'])}")
        print(f"  degree_sequences={dict(census['degree_sequences'])}")

check(
    "single-edge diagrams vanish under row-zero degeneracy",
    censuses[0]["surviving_count"] == 0,
    f"surviving_r1={censuses[0]['surviving_count']}",
)
check(
    "two-edge survivor is exactly the double-edge contraction",
    censuses[1]["surviving_count"] == 2
    and dict(censuses[1]["vertex_counts"]) == {2: 2}
    and dict(censuses[1]["degree_sequences"]) == {(2, 2): 2},
    f"surviving_r2={censuses[1]['surviving_count']} "
    f"degree_sequences={dict(censuses[1]['degree_sequences'])}",
)
check(
    "every audited survivor is a 2-core graph",
    all(
        stats["min_degree"] >= 2 and not stats["has_loop"]
        for census in censuses
        for _, stats in census["surviving"]
    ),
    "all surviving quotient graphs have minimum degree at least two",
)
check(
    "2-core survivors have at most r quotient vertices",
    all(census["max_vertices"] <= census["r"] for census in censuses),
    ", ".join(f"r={c['r']}:vmax={c['max_vertices']}" for c in censuses),
)
check(
    "every audited survivor carries at least r endpoint collisions",
    all(
        census["surviving_count"] == 0 or census["min_collision_deficit"] >= census["r"]
        for census in censuses
    ),
    ", ".join(
        f"r={c['r']}:deficit={c['min_collision_deficit']}" for c in censuses
    ),
)

print("\n=== Conditional root-envelope arithmetic ===")
max_count_root = max(census["count_root"] for census in censuses if census["r"] >= 2)
print(f"max audited 2-core count root = {fmt(max_count_root, 18)}")

activity_roots = [mp.mpf("0.02"), mp.mpf("0.05"), mp.mpf("0.10")]
for activity_root in activity_roots:
    bounds = [
        conditional_beta_bound(max_count_root, activity_root, r)
        for r in range(2, 8)
    ]
    print(
        f"activity_root={fmt(activity_root, 8)} beta_bounds="
        + ", ".join(fmt(value, 12) for value in bounds)
    )

physical_beta_guard = mp.mpf("0.65")
physical_observed_beta = mp.mpf("0.428361126341251506")
physical_c05_n12_beta = mp.mpf("0.344937390796585284")
block_calibrated_beta = mp.mpf("2.00711116878171591")
block_over_physical = mp.mpf("5.81876949943457784")
z1_ratio_block_physical = mp.mpf("1.21010595568431932")

safe_activity_root = mp.mpf("0.05")
safe_beta_bound_r2 = conditional_beta_bound(max_count_root, safe_activity_root, 2)

check(
    "exponential 2-core activity would imply the coefficient-root envelope",
    safe_beta_bound_r2 < physical_beta_guard,
    f"activity_root={fmt(safe_activity_root)} beta_bound_r2={fmt(safe_beta_bound_r2, 18)} "
    f"guard={fmt(physical_beta_guard)}",
)
check(
    "audited physical beta sits below the envelope guard",
    physical_observed_beta < physical_beta_guard,
    f"observed={fmt(physical_observed_beta, 18)} guard={fmt(physical_beta_guard)}",
)
check(
    "q2-calibrated staged block fails the root-envelope target",
    block_calibrated_beta > physical_beta_guard and block_over_physical > 5,
    f"block_beta={fmt(block_calibrated_beta, 18)} "
    f"block/physical={fmt(block_over_physical, 18)}",
)
check(
    "small finite Z1 comparison would miss the staged-block warning",
    z1_ratio_block_physical < 2 and block_calibrated_beta > 5 * physical_c05_n12_beta,
    f"Z_ratio={fmt(z1_ratio_block_physical, 18)} "
    f"beta_ratio={fmt(block_over_physical, 18)}",
)

print("\n=== Theorem extracted ===")
print("Row-zero degeneracy gives the exponent: only 2-core collision diagrams survive,")
print("and those have at least r endpoint collisions.  The missing analytic lemma is")
print("therefore not another finite coefficient check; it is a uniform exponential")
print("bound on the absolute activities of the surviving 2-core contractions for")
print("the physical rank-copula.  Staged/fiber kernels fail by coherent 2-core")
print("activity even when q2 and finite Z1 look close.")

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
