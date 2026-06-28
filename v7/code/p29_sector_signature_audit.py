#!/usr/bin/env python3
"""
Paper 29 receipt: sector-signature audit.

The scalar cancellation factor is not a separator.  This receipt follows the
opening by inspecting the full r=5 sector signature:

    S_v,  v=2,3,4,5,

where S_v is the exact signed 2-core contribution with v quotient vertices.
It records absolute top-sector share, low-sector share, centroid, and signed
residue fraction.  The goal is not to prove the theorem, but to check whether
the sector profile contains information that the scalar cancellation factor
throws away.

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
    return {v: sectors.get(v, mp.mpf(0)) for v in range(2, 6)}


def signature(sectors):
    total = mp.fsum(sectors.values())
    absolute = mp.fsum(abs(value) for value in sectors.values())
    top_share = abs(sectors[5]) / absolute
    low_share = (abs(sectors[2]) + abs(sectors[3])) / absolute
    centroid = mp.fsum(v * abs(sectors[v]) for v in sectors) / absolute
    residue_fraction = abs(total) / absolute
    return top_share, low_share, centroid, residue_fraction, total, absolute


print("=" * 80)
print("Paper 29 sector-signature audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

rows = []
print("\n=== Physical sector signatures ===")
for n, c in [(10, mp.mpf("0.5")), (12, mp.mpf("0.5")), (14, mp.mpf("0.5")), (14, mp.mpf("4"))]:
    D = physical_delta(n, c, nodes=12)
    sectors = r5_sector_contributions(D)
    top, low, centroid, residue, total, absolute = signature(sectors)
    q, _rho, beta = coefficient_profile(D)
    rows.append(("physical", n, c, top, low, centroid, residue, max(beta.values())))
    print(
        f"physical N={n} c={fmt(c, 6)} top={fmt(top, 18)} low={fmt(low, 18)} "
        f"centroid={fmt(centroid, 18)} residue={fmt(residue, 18)} "
        f"max_beta={fmt(max(beta.values()), 18)} sectors={{{', '.join(f'{v}: {fmt(sectors[v], 8)}' for v in sectors)}}}"
    )

print("\n=== Staged-block sector signatures ===")
for n in [10, 12, 14]:
    physical = physical_delta(n, mp.mpf("0.5"), nodes=12)
    target_q, _rho, _beta = coefficient_profile(physical)
    D = calibrate_to_q2(balanced_block_D(n), target_q[2])
    sectors = r5_sector_contributions(D)
    top, low, centroid, residue, total, absolute = signature(sectors)
    q, _rho, beta = coefficient_profile(D)
    rows.append(("block", n, mp.mpf("0.5"), top, low, centroid, residue, max(beta.values())))
    print(
        f"block N={n} top={fmt(top, 18)} low={fmt(low, 18)} "
        f"centroid={fmt(centroid, 18)} residue={fmt(residue, 18)} "
        f"max_beta={fmt(max(beta.values()), 18)} sectors={{{', '.join(f'{v}: {fmt(sectors[v], 8)}' for v in sectors)}}}"
    )

physical_top_max = max(row[3] for row in rows if row[0] == "physical")
block_top_min = min(row[3] for row in rows if row[0] == "block")
physical_centroid_max = max(row[5] for row in rows if row[0] == "physical")
block_centroid_min = min(row[5] for row in rows if row[0] == "block")
physical_beta_max = max(row[7] for row in rows if row[0] == "physical")
block_beta_min = min(row[7] for row in rows if row[0] == "block")

check(
    "top-sector share separates audited physical rows from staged blocks",
    physical_top_max < block_top_min,
    f"physical_top_max={fmt(physical_top_max, 18)} block_top_min={fmt(block_top_min, 18)}",
)
check(
    "absolute-sector centroid separates audited physical rows from staged blocks",
    physical_centroid_max < block_centroid_min,
    f"physical_centroid_max={fmt(physical_centroid_max, 18)} block_centroid_min={fmt(block_centroid_min, 18)}",
)
check(
    "sector signature separation aligns with beta separation",
    physical_beta_max < mp.mpf("0.65") and block_beta_min > mp.mpf("0.8"),
    f"physical_beta_max={fmt(physical_beta_max, 18)} block_beta_min={fmt(block_beta_min, 18)}",
)

print("\n=== Theorem status ===")
print(
    "A scalar cancellation factor failed, but the audited r=5 sector profile "
    "separates physical rows from staged blocks: physical mass sits less in the "
    "top quotient-vertex sector and has a lower absolute-sector centroid.  The "
    "next theorem target is a sector-profile envelope, not just cancellation."
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
