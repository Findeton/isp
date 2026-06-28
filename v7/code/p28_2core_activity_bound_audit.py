#!/usr/bin/env python3
"""
Paper 28 receipt: 2-core activity bound audit.

The canonical-kernel receipt explained the N^{-r} exponent: row-zero
degeneracy kills leaf diagrams, leaving only 2-core endpoint-collision
diagrams.  This receipt attacks the next question:

    what activity norm should be bounded on those surviving 2-core diagrams?

A naive maximum over individual graph contractions is not enough.  More
surprisingly, a naive multiplicity-weighted homomorphism activity is also not
the right separator.  The q2-calibrated staged block is dangerous in the exact
disjoint coefficient, but not in these raw 2-core activity summaries.  Therefore
this audit compares:

  * max individual 2-core activity root;
  * multiplicity-weighted signed 2-core activity root;
  * multiplicity-weighted absolute 2-core activity root.

Then it compares those raw summaries with the exact coefficient-root envelope.
The conclusion is a correction: the missing theorem must control the exact
Möbius/falling-factor 2-core expansion, not raw graph homomorphism activity.

It uses the actual physical rank-copula residue at N=12,c=0.5 and the staged
block calibrated to the same physical q2 scale.

This is not a proof of the activity theorem.  It is a hostile finite audit of
which activity norm the theorem must control.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from itertools import permutations
import math
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


def zero_matrix(n):
    return [[mp.mpf(0) for _ in range(n)] for _ in range(n)]


def offdiag_sum(matrix):
    n = len(matrix)
    return mp.fsum(matrix[i][j] for i in range(n) for j in range(n) if i != j)


def project_symmetric_zero_row(matrix):
    n = len(matrix)
    sym = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                sym[i][j] = (mp.mpf(matrix[i][j]) + mp.mpf(matrix[j][i])) / 2

    row = [mp.fsum(sym[i][j] for j in range(n) if i != j) for i in range(n)]
    total_row = mp.fsum(row)
    correction_constant = -total_row / ((n - 2) * (n - 1))
    out = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                h = (row[i] + row[j]) / (n - 2) + correction_constant
                out[i][j] = sym[i][j] - h
    return out


def max_row_linf(D):
    n = len(D)
    return max(abs(mp.fsum(D[i][j] for j in range(n) if i != j)) for i in range(n))


def axis_excess(D):
    n = len(D)
    return mp.fsum(D[i][j] ** 2 for i in range(n) for j in range(n) if i != j) / (
        mp.mpf(n) * (n - 1)
    )


def normalize_A_one(D):
    A = axis_excess(D)
    if A == 0:
        raise ValueError("zero matrix")
    scale = 1 / mp.sqrt(A)
    return scale_matrix(D, scale), A


def A_anti(z, c):
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 2 / (4 * c)
    return z


def marginal_cdf(x, c):
    return A_anti(x, c) - A_anti(mp.mpf(x) - 1, c)


def legendre_nodes(n, left, right):
    xs, ws = mp.gauss_quadrature(n, "legendre")
    mid = (mp.mpf(left) + mp.mpf(right)) / 2
    half = (mp.mpf(right) - mp.mpf(left)) / 2
    return [(mid + half * xs[i], half * ws[i]) for i in range(n)]


def clamp_unit(x):
    if x < 0:
        return mp.mpf(0)
    if x > 1:
        return mp.mpf(1)
    return x


def rank_kernel_values(n, low, high):
    between = high - low
    above = 1 - high
    fact = mp.mpf(math.factorial(n - 2))
    out = []
    for a in range(n - 1):
        low_pow = low**a
        for b in range(a + 1, n):
            coeff = fact / (
                mp.mpf(math.factorial(a))
                * mp.mpf(math.factorial(b - a - 1))
                * mp.mpf(math.factorial(n - 1 - b))
            )
            value = coeff * low_pow * (between ** (b - a - 1)) * (above ** (n - 1 - b))
            out.append((a, b, value))
    return out


def physical_delta(n, c, nodes):
    c = mp.mpf(c)
    matrix = zero_matrix(n)
    density_factor = 1 / (4 * c * c)
    for s, ws in legendre_nodes(nodes, 0, 1):
        for e0, we0 in legendre_nodes(nodes, -c, c):
            r0 = clamp_unit(marginal_cdf(s + e0, c))
            for e1, we1 in legendre_nodes(nodes + 1, -c, c):
                r1 = clamp_unit(marginal_cdf(s + e1, c))
                weight = ws * we0 * we1 * density_factor
                if r0 < r1:
                    for a, b, value in rank_kernel_values(n, r0, r1):
                        matrix[a][b] += weight * value
                elif r1 < r0:
                    for b, a, value in rank_kernel_values(n, r1, r0):
                        matrix[a][b] += weight * value

    sym = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                sym[i][j] = (matrix[i][j] + matrix[j][i]) / 2
    total = offdiag_sum(sym)
    uniform = 1 / (mp.mpf(n) * (n - 1))
    residue = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                probability = sym[i][j] / total
                residue[i][j] = mp.mpf(n) * (n - 1) * (probability - uniform)
    return project_symmetric_zero_row(residue)


def balanced_block_D(n):
    half = n // 2
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                same = (i < half and j < half) or (i >= half and j >= half)
                matrix[i][j] = mp.mpf(1) if same else mp.mpf(-1)
    return project_symmetric_zero_row(matrix)


def scale_matrix(D, scale):
    scale = mp.mpf(scale)
    return [[scale * value for value in row] for row in D]


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


def two_core_shapes(r):
    seen = set()
    out = {}
    for partition in set_partitions(range(2 * r)):
        partition = canonical_partition(partition)
        if partition in seen:
            continue
        seen.add(partition)
        adj = adjacency_from_partition(r, partition)
        if adj is None:
            continue
        code = canonical_adjacency(adj)
        out[code] = out.get(code, 0) + 1
    return out


def graph_edges(adj):
    edges = []
    for i in range(len(adj)):
        for j in range(i + 1, len(adj)):
            for _ in range(adj[i][j]):
                edges.append((i, j))
    return edges


def graph_activity(D, adj):
    n = len(D)
    v = len(adj)
    edges = graph_edges(adj)
    signed = mp.mpf(0)
    absolute = mp.mpf(0)
    count = mp.mpf(0)
    for assignment in permutations(range(n), v):
        product = mp.mpf(1)
        for i, j in edges:
            product *= D[assignment[i]][assignment[j]]
        signed += product
        absolute += abs(product)
        count += 1
    return signed / count, absolute / count


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


def pair_entries(D):
    n = len(D)
    entries = []
    for i in range(n):
        for j in range(n):
            if i != j:
                entries.append(((1 << i) | (1 << j), D[i][j]))
    return entries


def disjoint_moments(D, max_r):
    n = len(D)
    entries = pair_entries(D)
    dp = {0: mp.mpf(1)}
    out = {}
    for depth in range(1, min(max_r, n // 2) + 1):
        next_dp = {}
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                key = used | mask
                next_dp[key] = next_dp.get(key, mp.mpf(0)) + value * edge_value
        total = mp.fsum(next_dp.values())
        out[depth] = total / falling(n, 2 * depth)
        dp = next_dp
    return out


def coefficient_profile(D, max_r):
    n = len(D)
    moments = disjoint_moments(D, max_r)
    coeffs = {}
    for r, rho in moments.items():
        coeffs[r] = mp.mpf(math.comb(n // 2, r)) * rho * rho
    return coeffs


def beta_eff(n, coeffs):
    return max(
        mp.mpf(n) * (abs(coeffs[r]) ** (mp.mpf(1) / r))
        for r in coeffs
        if r >= 2
    )


def activity_rows(D, max_r):
    rows = []
    for r in range(2, max_r + 1):
        shapes = two_core_shapes(r)
        signed_total = mp.mpf(0)
        abs_total = mp.mpf(0)
        max_signed_root = mp.mpf(0)
        max_abs_root = mp.mpf(0)
        max_signed_multiplicity = 0
        max_abs_multiplicity = 0
        for code, multiplicity in shapes.items():
            signed, absolute = graph_activity(D, decode_adjacency(code))
            signed_root = abs(signed) ** (mp.mpf(1) / r)
            abs_root = absolute ** (mp.mpf(1) / r)
            if signed_root > max_signed_root:
                max_signed_root = signed_root
                max_signed_multiplicity = multiplicity
            if abs_root > max_abs_root:
                max_abs_root = abs_root
                max_abs_multiplicity = multiplicity
            signed_total += multiplicity * signed
            abs_total += multiplicity * absolute
        rows.append(
            {
                "r": r,
                "shape_count": len(shapes),
                "partition_count": sum(shapes.values()),
                "max_signed_root": max_signed_root,
                "max_abs_root": max_abs_root,
                "weighted_signed_root": abs(signed_total) ** (mp.mpf(1) / r),
                "weighted_abs_root": abs_total ** (mp.mpf(1) / r),
                "max_signed_multiplicity": max_signed_multiplicity,
                "max_abs_multiplicity": max_abs_multiplicity,
            }
        )
    return rows


print("=" * 80)
print("Paper 28 2-core activity bound audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
nodes = 12
max_r = 5
coefficient_max_r = 6
block_scale = mp.mpf("0.410498227581451253")

physical = physical_delta(n, mp.mpf("0.5"), nodes)
block_base, block_original_A = normalize_A_one(balanced_block_D(n))
block = scale_matrix(block_base, block_scale)

print("\n=== Kernel checks ===")
print(f"physical row_linf = {fmt(max_row_linf(physical), 18)}")
print(f"q2-calibrated block row_linf = {fmt(max_row_linf(block), 18)}")
print(f"block scale = {fmt(block_scale, 18)}")
print(f"block original A = {fmt(block_original_A, 18)}")

physical_rows = activity_rows(physical, max_r)
block_rows = activity_rows(block, max_r)
physical_coeffs = coefficient_profile(physical, coefficient_max_r)
block_coeffs = coefficient_profile(block, coefficient_max_r)
physical_beta = beta_eff(n, physical_coeffs)
block_beta = beta_eff(n, block_coeffs)

print("\n=== 2-core activities by order ===")
print("family,r,shapes,partitions,max_signed_root,max_abs_root,weighted_signed_root,weighted_abs_root")
for family, rows in [("physical", physical_rows), ("q2_block", block_rows)]:
    for row in rows:
        print(
            f"{family},{row['r']},{row['shape_count']},{row['partition_count']},"
            f"{fmt(row['max_signed_root'], 18)},"
            f"{fmt(row['max_abs_root'], 18)},"
            f"{fmt(row['weighted_signed_root'], 18)},"
            f"{fmt(row['weighted_abs_root'], 18)}"
        )

max_individual_ratio = max(
    physical_rows[index]["max_abs_root"] / block_rows[index]["max_abs_root"]
    for index in range(len(physical_rows))
)
weighted_abs_block_over_physical_r5 = (
    block_rows[-1]["weighted_abs_root"] / physical_rows[-1]["weighted_abs_root"]
)
weighted_signed_block_over_physical_r5 = (
    block_rows[-1]["weighted_signed_root"] / physical_rows[-1]["weighted_signed_root"]
)
block_weighted_growth = block_rows[-1]["weighted_abs_root"] / block_rows[0]["weighted_abs_root"]
physical_weighted_growth = physical_rows[-1]["weighted_abs_root"] / physical_rows[0]["weighted_abs_root"]

print("\n=== Separation summary ===")
print(f"max individual physical/block abs-root ratio = {fmt(max_individual_ratio, 18)}")
print(f"r=5 weighted abs block/physical = {fmt(weighted_abs_block_over_physical_r5, 18)}")
print(f"r=5 weighted signed block/physical = {fmt(weighted_signed_block_over_physical_r5, 18)}")
print(f"block weighted abs growth r2->r5 = {fmt(block_weighted_growth, 18)}")
print(f"physical weighted abs growth r2->r5 = {fmt(physical_weighted_growth, 18)}")
print(f"exact physical beta_eff = {fmt(physical_beta, 18)}")
print(f"exact q2-calibrated block beta_eff = {fmt(block_beta, 18)}")
for r in range(2, coefficient_max_r + 1):
    ratio = block_coeffs[r] / physical_coeffs[r] if physical_coeffs[r] else mp.inf
    print(f"exact coefficient ratio block/physical r={r}: {fmt(ratio, 18)}")

check(
    "both kernels remain canonical after projection",
    max_row_linf(physical) < mp.mpf("1e-80") and max_row_linf(block) < mp.mpf("1e-80"),
    f"physical={fmt(max_row_linf(physical), 18)} block={fmt(max_row_linf(block), 18)}",
)
check(
    "2-core shape census is small compared with survivor partitions",
    physical_rows[-1]["shape_count"] == 11 and physical_rows[-1]["partition_count"] == 5120,
    f"r5_shapes={physical_rows[-1]['shape_count']} r5_partitions={physical_rows[-1]['partition_count']}",
)
check(
    "individual graph activity is not the separator",
    max_individual_ratio > 1,
    f"max_physical_over_block_individual_abs_root={fmt(max_individual_ratio, 18)}",
)
check(
    "raw multiplicity-weighted activity is also not the separator",
    weighted_abs_block_over_physical_r5 < 1,
    f"r5_weighted_abs_block/physical={fmt(weighted_abs_block_over_physical_r5, 18)}",
)
check(
    "raw signed accumulation also misses the staged block at r=5",
    weighted_signed_block_over_physical_r5 < 1,
    f"r5_weighted_signed_block/physical={fmt(weighted_signed_block_over_physical_r5, 18)}",
)
check(
    "raw staged weighted activity does not grow faster across audited orders",
    block_weighted_growth < physical_weighted_growth,
    f"block_growth={fmt(block_weighted_growth, 18)} physical_growth={fmt(physical_weighted_growth, 18)}",
)
check(
    "exact coefficient-root envelope still separates the staged block",
    block_beta > 5 * physical_beta,
    f"block_beta={fmt(block_beta, 18)} physical_beta={fmt(physical_beta, 18)}",
)

print("\n=== Theorem correction ===")
print("The activity theorem should not bound raw graph homomorphism activities.")
print("In this audit, neither individual 2-core activity nor naive")
print("multiplicity-weighted activity separates the physical kernel from the")
print("q2-calibrated staged block.  The exact coefficient-root envelope still")
print("separates them sharply.  The missing analytic lemma must therefore control")
print("the exact Möbius/falling-factor 2-core expansion, not merely graph-by-graph")
print("or positive weighted homomorphism activities.")

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
