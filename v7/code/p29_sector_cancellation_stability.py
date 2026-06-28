#!/usr/bin/env python3
"""
Paper 29 receipt: sector-cancellation stability.

The exact 2-core sector decomposition found strong physical signed
cancellation at N=12,c=0.5,r=5.  This receipt asks whether that was a
one-point accident or a usable theorem by itself.  It repeats the exact r=5
sector decomposition on a small bounded-width physical grid and compares it
with q2-calibrated staged blocks.

This is still finite evidence, not an all-N proof.  Its job is to decide
whether a scalar cancellation-factor theorem is viable.  The answer is no:
sector cancellation is real, but the scalar cancellation factor is not a
separator.

All non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict
from itertools import permutations, product
import math
import sys

import mpmath as mp

from p29_matching_lib import (
    balanced_block_D,
    calibrate_to_q2,
    coefficient_profile,
    falling,
    fmt,
    physical_delta,
    scaled_matching_coefficients,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def set_partitions(items):
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


def adjacency_from_partition(r, partition):
    block_of = {}
    for block_index, block in enumerate(partition):
        for endpoint in block:
            block_of[endpoint] = block_index
    v = len(partition)
    adj = [[0 for _ in range(v)] for _ in range(v)]
    degrees = [0 for _ in range(v)]
    for edge in range(r):
        a = block_of[2 * edge]
        b = block_of[2 * edge + 1]
        if a == b:
            return None
        adj[a][b] += 1
        adj[b][a] += 1
        degrees[a] += 1
        degrees[b] += 1
    if min(degrees) < 2:
        return None
    return adj


def canonical_adjacency(adj):
    v = len(adj)
    best = None
    for perm in permutations(range(v)):
        flat = tuple(adj[perm[i]][perm[j]] for i in range(v) for j in range(i + 1, v))
        if best is None or flat < best:
            best = flat
    return (v, best)


def decode_adjacency(code):
    v, flat = code
    adj = [[0 for _ in range(v)] for _ in range(v)]
    cursor = 0
    for i in range(v):
        for j in range(i + 1, v):
            adj[i][j] = flat[cursor]
            adj[j][i] = flat[cursor]
            cursor += 1
    return adj


def mobius_partition(partition):
    out = mp.mpf(1)
    for block in partition:
        size = len(block)
        out *= (-1) ** (size - 1) * math.factorial(size - 1)
    return out


def shape_mobius_counts(r):
    counts = defaultdict(mp.mpf)
    seen = set()
    for partition in set_partitions(range(2 * r)):
        partition = canonical_partition(partition)
        if partition in seen:
            continue
        seen.add(partition)
        adj = adjacency_from_partition(r, partition)
        if adj is None:
            continue
        counts[canonical_adjacency(adj)] += mobius_partition(partition)
    return dict(counts)


SHAPE_COUNTS_R5 = shape_mobius_counts(5)


def hom_sum(D, adj):
    n = len(D)
    v = len(adj)
    edges = []
    for i in range(v):
        for j in range(i + 1, v):
            for _ in range(adj[i][j]):
                edges.append((i, j))
    total = mp.mpf(0)
    for assignment in product(range(n), repeat=v):
        value = mp.mpf(1)
        for i, j in edges:
            value *= D[assignment[i]][assignment[j]]
            if value == 0:
                break
        total += value
    return total


def r5_sector_contributions(D):
    n = len(D)
    scale = (mp.mpf(n) ** 5) / falling(n, 10)
    sectors = defaultdict(mp.mpf)
    for code, mu_count in SHAPE_COUNTS_R5.items():
        adj = decode_adjacency(code)
        sectors[len(adj)] += scale * mu_count * hom_sum(D, adj)
    return dict(sectors)


def cancellation_factor(sectors):
    total = mp.fsum(sectors.values())
    absolute = mp.fsum(abs(value) for value in sectors.values())
    return absolute / max(mp.mpf("1e-80"), abs(total)), total, absolute


print("=" * 80)
print("Paper 29 sector-cancellation stability")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

physical_rows = []
print("\n=== Physical bounded-width grid, r=5 ===")
for n in [10, 12, 14]:
    for c in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")]:
        D = physical_delta(n, c, nodes=12)
        scaled = scaled_matching_coefficients(D)
        sectors = r5_sector_contributions(D)
        cancel, total, absolute = cancellation_factor(sectors)
        error = abs(total - scaled[5])
        q, _rho, beta = coefficient_profile(D)
        physical_rows.append((n, c, cancel, max(beta.values()), error))
        print(
            f"N={n}, c={fmt(c, 6)}, exact={fmt(scaled[5], 18)}, "
            f"sector_total={fmt(total, 18)}, error={fmt(error, 8)}, "
            f"cancel={fmt(cancel, 18)}, max_beta={fmt(max(beta.values()), 18)}"
        )

print("\n=== q2-calibrated staged blocks, r=5 ===")
block_rows = []
for n in [10, 12, 14]:
    physical = physical_delta(n, mp.mpf("0.5"), nodes=12)
    target_q, _rho, _beta = coefficient_profile(physical)
    block = calibrate_to_q2(balanced_block_D(n), target_q[2])
    sectors = r5_sector_contributions(block)
    cancel, total, absolute = cancellation_factor(sectors)
    q, _rho, beta = coefficient_profile(block)
    block_rows.append((n, cancel, max(beta.values())))
    print(
        f"N={n}, exact={fmt(scaled_matching_coefficients(block)[5], 18)}, "
        f"sector_total={fmt(total, 18)}, cancel={fmt(cancel, 18)}, "
        f"max_beta={fmt(max(beta.values()), 18)}"
    )

max_error = max(row[4] for row in physical_rows)
min_physical_cancel = min(row[2] for row in physical_rows)
max_physical_beta = max(row[3] for row in physical_rows)
max_block_cancel = max(row[1] for row in block_rows)
min_block_beta = min(row[2] for row in block_rows)

check(
    "r=5 sector expansion reconstructs physical grid",
    max_error < mp.mpf("1e-75"),
    f"max_error={fmt(max_error, 18)}",
)
check(
    "physical r=5 cancellation is real across bounded-width grid",
    min_physical_cancel > mp.mpf("10"),
    f"min_physical_cancel={fmt(min_physical_cancel, 18)}",
)
check(
    "scalar cancellation factor is falsified as a separator",
    max_block_cancel > min_physical_cancel and min_block_beta > mp.mpf("0.8"),
    f"max_block_cancel={fmt(max_block_cancel, 18)} min_block_beta={fmt(min_block_beta, 18)}",
)
check(
    "stable cancellation coexists with bounded physical beta",
    max_physical_beta < mp.mpf("0.65"),
    f"max_physical_beta={fmt(max_physical_beta, 18)}",
)

print("\n=== Theorem status ===")
print(
    "The physical r=5 sector cancellation is real on the audited bounded-width "
    "grid, but the scalar cancellation factor is not a theorem: staged blocks "
    "can overlap it while keeping high beta.  The next target must use the full "
    "signed sector profile, not a single cancellation number."
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
