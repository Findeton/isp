#!/usr/bin/env python3
"""
Paper 29 receipt: exact 2-core sector decomposition.

The labelled cycle-index receipt showed that the 2-regular cycle sector alone
overshoots the physical coefficients at r=4,5.  This receipt follows the
opening: decompose the exact Möbius/falling-factor expansion by quotient
vertex count v.

For r directed pair factors and a partition pi of the 2r endpoints, the exact
contribution is

    mu(pi) * hom_D(G_pi) / (N)_{2r}.

After scaling by N^r, row-zero and zero diagonal leave only 2-core quotient
graphs.  The v=r sector is the labelled cycle-index term.  The v<r sectors are
the finite-population remainder.  This receipt computes the exact sector sum
for r<=5 and verifies that it reconstructs N^r rho_{N,r}.

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
        code = canonical_adjacency(adj)
        counts[code] += mobius_partition(partition)
    return dict(counts)


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


def exact_sector_contributions(D, r):
    n = len(D)
    counts = shape_mobius_counts(r)
    scale = (mp.mpf(n) ** r) / falling(n, 2 * r)
    sectors = defaultdict(mp.mpf)
    abs_sectors = defaultdict(mp.mpf)
    shape_count = defaultdict(int)
    for code, mu_count in counts.items():
        adj = decode_adjacency(code)
        v = len(adj)
        h = hom_sum(D, adj)
        contribution = scale * mu_count * h
        sectors[v] += contribution
        abs_sectors[v] += abs(contribution)
        shape_count[v] += 1
    return dict(sectors), dict(abs_sectors), dict(shape_count)


def cancellation_factor(sectors):
    total = mp.fsum(sectors.values())
    absolute = mp.fsum(abs(value) for value in sectors.values())
    return absolute / max(mp.mpf("1e-80"), abs(total))


print("=" * 80)
print("Paper 29 exact 2-core sector decomposition")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
physical = physical_delta(n, mp.mpf("0.5"), nodes=12)
target_q, _rho, _beta = coefficient_profile(physical)
block = calibrate_to_q2(balanced_block_D(n), target_q[2])

kernels = {
    "physical_c0.5": physical,
    "balanced_block_q2_calibrated": block,
}

max_reconstruction_error = mp.mpf(0)
physical_cancellation_r5 = mp.mpf(0)
block_cancellation_r5 = mp.mpf(0)
cycle_overshoot_r5 = mp.mpf(0)

for name, D in kernels.items():
    scaled = scaled_matching_coefficients(D)
    q, _rho, beta = coefficient_profile(D)
    print(f"\n{name}: max_beta={fmt(max(beta.values()), 18)}")
    for r in range(2, 6):
        sectors, abs_sectors, shape_count = exact_sector_contributions(D, r)
        reconstructed = mp.fsum(sectors.values())
        error = abs(reconstructed - scaled[r])
        max_reconstruction_error = max(max_reconstruction_error, error)
        cancel = cancellation_factor(sectors)
        if name == "physical_c0.5" and r == 5:
            physical_cancellation_r5 = cancel
            cycle_overshoot_r5 = abs(sectors.get(r, mp.mpf(0))) / abs(scaled[r])
        if name == "balanced_block_q2_calibrated" and r == 5:
            block_cancellation_r5 = cancel
        print(
            f"  r={r}, exact={fmt(scaled[r], 18)}, "
            f"reconstructed={fmt(reconstructed, 18)}, "
            f"error={fmt(error, 8)}, cancellation={fmt(cancel, 18)}"
        )
        for v in sorted(sectors):
            print(
                f"    v={v}, shapes={shape_count[v]}, "
                f"signed={fmt(sectors[v], 18)}, abs_sector={fmt(abs_sectors[v], 18)}"
            )

check(
    "sector expansion reconstructs exact scaled coefficients",
    max_reconstruction_error < mp.mpf("1e-80"),
    f"max_reconstruction_error={fmt(max_reconstruction_error, 18)}",
)
check(
    "physical r=5 cycle sector is cancelled by lower-v sectors",
    cycle_overshoot_r5 > mp.mpf("10"),
    f"cycle_abs/exact_abs={fmt(cycle_overshoot_r5, 18)}",
)
check(
    "physical cancellation is much stronger than staged-block cancellation at r=5",
    physical_cancellation_r5 > 5 * block_cancellation_r5,
    f"physical={fmt(physical_cancellation_r5, 18)} block={fmt(block_cancellation_r5, 18)}",
)
check(
    "positive sector bounds are impossible for the physical proof",
    physical_cancellation_r5 > mp.mpf("50"),
    f"physical_cancellation_r5={fmt(physical_cancellation_r5, 18)}",
)

print("\n=== Theorem status ===")
print(
    "The generating object is now exact through r=5: a signed 2-core sector "
    "sum.  The physical kernel is not small because every sector is small; it "
    "is small because large cycle and lower-vertex sectors cancel.  The missing "
    "theorem is therefore stable sector cancellation, not a positive activity "
    "bound and not a bare determinant bound."
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
