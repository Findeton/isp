#!/usr/bin/env python3
"""
Paper 28 receipt: exact Möbius/falling-factor 2-core expansion.

The previous receipt showed that raw graph-homomorphism activity is not the
right norm.  This receipt writes the actual algebra.

For m=2r endpoints, the distinct-endpoint sum is

    sum_distinct f(x_1,...,x_m)
      =
    sum_{pi in Partitions(m)} mu(pi) sum_{x constant on pi} f(x),

where

    mu(pi) = prod_{B in pi} (-1)^{|B|-1} (|B|-1)!.

For canonical kernels, all leaf quotient graphs vanish by row-zero sums, and
loops vanish by the absent diagonal.  The surviving terms are exactly the
2-core terms, but with the Möbius signs and falling-factor normalization.

This receipt verifies that the exact Möbius/falling-factor 2-core expansion
reproduces the direct without-replacement disjoint moment.  It then compares
the physical rank-copula to the q2-calibrated staged block.  The separating
object is the signed exact expansion, not raw positive graph activity.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from itertools import permutations, product
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


def scale_matrix(D, scale):
    scale = mp.mpf(scale)
    return [[scale * value for value in row] for row in D]


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


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


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


def mobius_from_adjacency(adj):
    out = mp.mpf(1)
    for degree in [sum(row) for row in adj]:
        out *= (-1) ** (degree - 1) * math.factorial(degree - 1)
    return out


def two_core_shape_counts(r):
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


def homomorphism_average(D, adj):
    n = len(D)
    v = len(adj)
    edges = graph_edges(adj)
    total = mp.mpf(0)
    count = mp.mpf(n) ** v
    for assignment in product(range(n), repeat=v):
        product_value = mp.mpf(1)
        for i, j in edges:
            product_value *= D[assignment[i]][assignment[j]]
        total += product_value
    return total / count


def mobius_terms(D, r):
    n = len(D)
    terms = []
    total = mp.mpf(0)
    abs_total = mp.mpf(0)
    for code, count in two_core_shape_counts(r).items():
        adj = decode_adjacency(code)
        v = len(adj)
        mu = mobius_from_adjacency(adj)
        H = homomorphism_average(D, adj)
        weight = mp.mpf(count) * mu * (mp.mpf(n) ** v) / falling(n, 2 * r)
        term = weight * H
        total += term
        abs_total += abs(term)
        terms.append({"code": code, "count": count, "mu": mu, "v": v, "H": H, "weight": weight, "term": term})
    return total, abs_total, terms


def direct_disjoint_moment(D, r):
    n = len(D)
    entries = []
    for i in range(n):
        for j in range(n):
            if i != j:
                entries.append(((1 << i) | (1 << j), D[i][j]))
    dp = {0: mp.mpf(1)}
    for depth in range(1, r + 1):
        next_dp = {}
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                key = used | mask
                next_dp[key] = next_dp.get(key, mp.mpf(0)) + value * edge_value
        dp = next_dp
    return mp.fsum(dp.values()) / falling(n, 2 * r)


def coefficient(n, r, rho):
    return mp.mpf(math.comb(n // 2, r)) * rho * rho


print("=" * 80)
print("Paper 28 exact Möbius/falling-factor 2-core expansion")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
nodes = 12
max_r = 5
block_scale = mp.mpf("0.410498227581451253")

physical = physical_delta(n, mp.mpf("0.5"), nodes)
block_base, block_original_A = normalize_A_one(balanced_block_D(n))
block = scale_matrix(block_base, block_scale)

print("\n=== Kernel checks ===")
print(f"physical row_linf = {fmt(max_row_linf(physical), 18)}")
print(f"q2-calibrated block row_linf = {fmt(max_row_linf(block), 18)}")

rows = []
max_expansion_error = mp.mpf(0)

print("\n=== Exact expansion by order ===")
for family, D in [("physical", physical), ("q2_block", block)]:
    for r in range(2, max_r + 1):
        mobius_value, abs_value, terms = mobius_terms(D, r)
        direct_value = direct_disjoint_moment(D, r)
        expansion_error = abs(mobius_value - direct_value)
        max_expansion_error = max(max_expansion_error, expansion_error)
        q = coefficient(n, r, direct_value)
        cancellation_ratio = abs_value / abs(mobius_value) if mobius_value else mp.inf
        rows.append(
            {
                "family": family,
                "r": r,
                "rho": direct_value,
                "q": q,
                "abs_value": abs_value,
                "cancellation_ratio": cancellation_ratio,
                "terms": len(terms),
            }
        )
        print(
            f"{family},r={r},rho={fmt(direct_value, 18)},"
            f"q={fmt(q, 18)},terms={len(terms)},"
            f"abs/signed={fmt(cancellation_ratio, 18)},"
            f"expansion_error={fmt(expansion_error, 8)}"
        )

physical_by_r = {row["r"]: row for row in rows if row["family"] == "physical"}
block_by_r = {row["r"]: row for row in rows if row["family"] == "q2_block"}

print("\n=== Physical vs staged exact ratios ===")
q_ratios = {}
cancellation_advantages = {}
for r in range(2, max_r + 1):
    q_ratios[r] = block_by_r[r]["q"] / physical_by_r[r]["q"]
    cancellation_advantages[r] = (
        physical_by_r[r]["cancellation_ratio"] / block_by_r[r]["cancellation_ratio"]
    )
    print(
        f"r={r} q_block/q_phys={fmt(q_ratios[r], 18)} "
        f"cancellation_phys/block={fmt(cancellation_advantages[r], 18)}"
    )

check(
    "both kernels remain canonical after projection",
    max_row_linf(physical) < mp.mpf("1e-80") and max_row_linf(block) < mp.mpf("1e-80"),
    f"physical={fmt(max_row_linf(physical), 18)} block={fmt(max_row_linf(block), 18)}",
)
check(
    "Möbius/falling-factor expansion reproduces direct disjoint moments",
    max_expansion_error < mp.mpf("1e-70"),
    f"max_expansion_error={fmt(max_expansion_error, 18)}",
)
check(
    "q2 calibration matches the physical two-factor coefficient",
    abs(q_ratios[2] - 1) < mp.mpf("1e-12"),
    f"q2_ratio={fmt(q_ratios[2], 18)}",
)
check(
    "exact coefficients expose staged high-order coherence",
    q_ratios[5] > mp.mpf("200"),
    f"q5_ratio={fmt(q_ratios[5], 18)}",
)
check(
    "physical exact expansion has much stronger cancellation at r=5",
    cancellation_advantages[5] > mp.mpf("20"),
    f"cancellation_advantage_r5={fmt(cancellation_advantages[5], 18)}",
)
check(
    "staged coefficient ratios grow monotonically after q2",
    q_ratios[2] < q_ratios[3] < q_ratios[4] < q_ratios[5],
    ", ".join(f"r{r}={fmt(q_ratios[r], 12)}" for r in range(2, max_r + 1)),
)

print("\n=== Theorem correction ===")
print("The correct activity object is the exact signed Möbius/falling-factor")
print("2-core expansion.  It reproduces the direct without-replacement moment,")
print("and it reveals that the physical kernel suppresses high-order coefficients")
print("through much stronger cancellation than the q2-calibrated staged block.")
print("The missing analytic lemma must prove stable cancellation of this exact")
print("signed expansion for the physical rank-copula, not merely bound positive")
print("graph activities.")

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
