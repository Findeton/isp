#!/usr/bin/env python3
"""
Paper 29 receipt: labelled cycle-index correction.

The naive reciprocal determinant det(I+2zD/N)^(-1) is too small because it is
an unlabelled spectral shadow.  The exact Möbius/falling-factor expansion first
requires labelled 2-regular quotient diagrams and the exact finite
normalization (N)_{2r}.

This receipt enumerates the 2-regular quotient partitions for r<=5, computes
their labelled cycle-index contribution, and compares it with the exact
matching coefficient

    a_{N,r} = N^r rho_{N,r}.

The result is intentionally not a full proof: the 2-regular cycle-index term
is the leading object, while lower-vertex non-cycle 2-core diagrams form a real
finite-population remainder.

All non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict, deque
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
    trace_powers_scaled,
)

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def set_partitions_k(n, k):
    blocks = []

    def rec(item):
        if item == n:
            if len(blocks) == k:
                yield tuple(tuple(block) for block in blocks)
            return
        remaining = n - item
        if len(blocks) > k or len(blocks) + remaining < k:
            return
        for block in blocks:
            block.append(item)
            yield from rec(item + 1)
            block.pop()
        if len(blocks) < k:
            blocks.append([item])
            yield from rec(item + 1)
            blocks.pop()

    blocks.append([0])
    yield from rec(1)


def component_lengths_from_partition(r, partition):
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
    if any(degree != 2 for degree in degrees):
        return None

    seen = [False for _ in range(v)]
    lengths = []
    for start in range(v):
        if seen[start]:
            continue
        q = deque([start])
        seen[start] = True
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for other in range(v):
                if adj[node][other] and not seen[other]:
                    seen[other] = True
                    q.append(other)
        lengths.append(count)
    return tuple(sorted(lengths))


def cycle_shape_counts(r):
    counts = defaultdict(int)
    for partition in set_partitions_k(2 * r, r):
        lengths = component_lengths_from_partition(r, partition)
        if lengths is not None:
            counts[lengths] += 1
    return dict(counts)


def cycle_index_scaled_coefficient(D, r):
    n = len(D)
    counts = cycle_shape_counts(r)
    traces_scaled = trace_powers_scaled(D, r)
    # hom(D, cycle length ell) = Tr(D^ell) = N^ell Tr((D/N)^ell).
    # The scaled coefficient N^r/(N)_{2r} times hom products is therefore
    # N^(2r)/(N)_{2r} times the product of scaled traces.
    inflation = (mp.mpf(n) ** (2 * r)) / falling(n, 2 * r)
    total = mp.mpf(0)
    sign = (-1) ** r
    for shape, count in counts.items():
        product = mp.mpf(1)
        for length in shape:
            product *= traces_scaled[length]
        total += count * sign * product
    return inflation * total, counts


def relative_error(actual, predicted):
    denom = max(mp.mpf("1e-80"), abs(actual), abs(predicted))
    return abs(actual - predicted) / denom


print("=" * 80)
print("Paper 29 labelled cycle-index correction")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n=== Universal labelled cycle shapes ===")
for r in range(2, 6):
    counts = cycle_shape_counts(r)
    print(f"r={r}: {counts}")

max_r2_error = mp.mpf(0)
max_physical_improvement = mp.mpf(0)
max_residue_ratio = mp.mpf(0)

print("\n=== Physical c=0.5: exact coefficient versus labelled 2-regular contribution ===")
for n in [10, 12, 14, 16]:
    D = physical_delta(n, mp.mpf("0.5"), nodes=12)
    scaled = scaled_matching_coefficients(D)
    print(f"\nN={n}")
    for r in range(2, min(5, n // 2) + 1):
        cycle_coeff, _counts = cycle_index_scaled_coefficient(D, r)
        err = relative_error(scaled[r], cycle_coeff)
        residue = scaled[r] - cycle_coeff
        residue_ratio = abs(residue) / max(mp.mpf("1e-80"), abs(scaled[r]))
        max_residue_ratio = max(max_residue_ratio, residue_ratio)
        if r == 2:
            max_r2_error = max(max_r2_error, err)
        if r >= 3:
            # The labelled cycle term should be much closer than the naive
            # determinant, but not exact.
            max_physical_improvement = max(max_physical_improvement, 1 - err)
        print(
            f"  r={r}, exact={fmt(scaled[r], 18)}, "
            f"cycle_index={fmt(cycle_coeff, 18)}, "
            f"residue={fmt(residue, 18)}, rel_error={fmt(err, 18)}"
        )

print("\n=== Staged block: cycle-index still does not select physicality ===")
n = 12
physical = physical_delta(n, mp.mpf("0.5"), nodes=12)
target_q, _rho, _beta = coefficient_profile(physical)
block = calibrate_to_q2(balanced_block_D(n), target_q[2])
scaled = scaled_matching_coefficients(block)
q, _rho, beta = coefficient_profile(block)
for r in range(2, 6):
    cycle_coeff, _counts = cycle_index_scaled_coefficient(block, r)
    err = relative_error(scaled[r], cycle_coeff)
    print(
        f"  r={r}, exact={fmt(scaled[r], 18)}, "
        f"cycle_index={fmt(cycle_coeff, 18)}, rel_error={fmt(err, 18)}"
    )

check(
    "labelled cycle index is exact at r=2",
    max_r2_error < mp.mpf("1e-80"),
    f"max_r2_error={fmt(max_r2_error, 18)}",
)
check(
    "labelled cycle index captures a real part of higher physical coefficients",
    max_physical_improvement > mp.mpf("0.2"),
    f"best_improvement_fraction={fmt(max_physical_improvement, 18)}",
)
check(
    "non-cycle 2-core finite-population residue is real",
    max_residue_ratio > mp.mpf("0.1"),
    f"max_residue_ratio={fmt(max_residue_ratio, 18)}",
)
check(
    "cycle-index correction alone does not eliminate staged-block obstruction",
    max(beta.values()) > mp.mpf("1"),
    f"block_max_beta={fmt(max(beta.values()), 18)}",
)

print("\n=== Theorem status ===")
print(
    "The correct generating object is not the naive determinant.  It is a "
    "cycle-index/Fredholm-determinant leading term plus an exact signed "
    "finite-population 2-core remainder.  The missing theorem must bound both."
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
