#!/usr/bin/env python3
"""
Paper 29 receipt: sector shape without amplitude is not enough.

The sector-signature audit found that top-sector share and centroid separate
audited physical kernels from staged blocks.  This receipt closes a tempting
overstatement:

    "sector shape alone is the law."

It is not.  Scaling D by s leaves sector shares and centroids unchanged, while
lambda_{N,r} and beta grow.  Therefore the theorem must be an amplitude-
normalized sector-profile envelope: sector shape plus coefficient scale, or
equivalently direct control of lambda_{N,r}.

All non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict
from itertools import permutations, product
import math
import sys

import mpmath as mp

from p29_matching_lib import (
    coefficient_profile,
    falling,
    fmt,
    physical_delta,
    scale_matrix,
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
    return {v: sectors.get(v, mp.mpf(0)) for v in range(2, 6)}


def signature(sectors):
    absolute = mp.fsum(abs(value) for value in sectors.values())
    top_share = abs(sectors[5]) / absolute
    centroid = mp.fsum(v * abs(sectors[v]) for v in sectors) / absolute
    total = mp.fsum(sectors.values())
    return top_share, centroid, total


def lambda_r(D, r):
    a = scaled_matching_coefficients(D)[r]
    return mp.power(abs(a) / mp.sqrt(mp.factorial(r)), mp.mpf(1) / r)


print("=" * 80)
print("Paper 29 sector shape/amplitude no-go")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
base = physical_delta(n, mp.mpf("0.5"), nodes=12)

rows = []
print("\n=== Scaling physical sector shape ===")
for s in [mp.mpf("1"), mp.mpf("1.5"), mp.mpf("2")]:
    D = scale_matrix(base, s)
    sectors = r5_sector_contributions(D)
    top, centroid, total = signature(sectors)
    lam5 = lambda_r(D, 5)
    q, _rho, beta = coefficient_profile(D)
    rows.append((s, top, centroid, lam5, max(beta.values())))
    print(
        f"scale={fmt(s, 8)}, top={fmt(top, 18)}, centroid={fmt(centroid, 18)}, "
        f"lambda5={fmt(lam5, 18)}, max_beta={fmt(max(beta.values()), 18)}"
    )

top_drift = max(abs(row[1] - rows[0][1]) for row in rows)
centroid_drift = max(abs(row[2] - rows[0][2]) for row in rows)
lambda_ratio = rows[-1][3] / rows[0][3]
beta_ratio = rows[-1][4] / rows[0][4]

check(
    "sector top-share is invariant under scaling",
    top_drift < mp.mpf("1e-100"),
    f"top_drift={fmt(top_drift, 18)}",
)
check(
    "sector centroid is invariant under scaling",
    centroid_drift < mp.mpf("1e-100"),
    f"centroid_drift={fmt(centroid_drift, 18)}",
)
check(
    "lambda scales linearly with kernel amplitude",
    abs(lambda_ratio - 2) < mp.mpf("1e-80"),
    f"lambda_ratio={fmt(lambda_ratio, 18)}",
)
check(
    "beta scales quadratically with kernel amplitude",
    abs(beta_ratio - 4) < mp.mpf("1e-80"),
    f"beta_ratio={fmt(beta_ratio, 18)}",
)

print("\n=== Theorem status ===")
print(
    "Sector shape alone is insufficient.  The theorem must be amplitude "
    "normalized, either by lower-order record coefficients or directly by a "
    "lambda_{N,r} sector-profile envelope."
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
