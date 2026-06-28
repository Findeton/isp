#!/usr/bin/env python3
"""
Paper 27 receipt: order-intrinsic local response gate.

The previous receipt used external rank-neighbor stress to show that local
mark coupling cannot launder a global block.  This receipt removes the external
rank-neighbor notion.  Locality is now order-intrinsic:

    a pair is local when it is comparable and has small interval cardinality.

For a mark f and shell k, the allowed local response proxy is

    1_{x<y, |I(x,y)|=k} (f(x)-f(y))^2,

zero-row projected in the same pair-kernel geometry space.  This is still only
a finite proxy for L(F), but it is built from the record order and mark values,
not from coordinate/rank adjacency.

Hostile checks:

  * on seeded 1+1 sprinkling-like permutation orders, small interval shells are
    sparse and their mark-stress span has decreasing projection on dense global
    block/cosine pair products;
  * a genuinely shell-local marked response projects to itself;
  * on a two-layer staged order, links are dense, so shell-local stress can
    launder the layer block exactly.  This is not a failure of the test; it
    proves that local response admissibility must be coupled to shell-density
    manifold regularity.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

import random
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def pair_indices(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def center(feature):
    mean = mp.fsum(feature) / len(feature)
    return [mp.mpf(value) - mean for value in feature]


def zero_row_project_pair_vector(n, values):
    pairs = pair_indices(n)
    row = [mp.mpf(0) for _ in range(n)]
    for value, (i, j) in zip(values, pairs):
        row[i] += value
        row[j] += value
    total_row = mp.fsum(row)
    correction_constant = -total_row / ((n - 2) * (n - 1))
    out = []
    for value, (i, j) in zip(values, pairs):
        correction = (row[i] + row[j]) / (n - 2) + correction_constant
        out.append(value - correction)
    return out


def pair_inner(a, b):
    return 2 * mp.fsum(a[i] * b[i] for i in range(len(a)))


def projection_fraction(target, basis):
    usable = [vector for vector in basis if pair_inner(vector, vector) > mp.mpf("1e-90")]
    if not usable:
        return mp.mpf(0)
    m = len(usable)
    gram = mp.matrix(m)
    rhs = mp.matrix(m, 1)
    for i, bi in enumerate(usable):
        rhs[i] = pair_inner(target, bi)
        for j, bj in enumerate(usable):
            gram[i, j] = pair_inner(bi, bj)
    coeffs = mp.lu_solve(gram, rhs)
    projected_norm = mp.fsum(coeffs[i] * rhs[i] for i in range(m))
    return projected_norm / pair_inner(target, target)


def product_kernel(feature):
    f = center(feature)
    n = len(f)
    values = [f[i] * f[j] for i, j in pair_indices(n)]
    return zero_row_project_pair_vector(n, values)


def cosine_product_kernel(n):
    feature = [mp.cos(2 * mp.pi * i / n) for i in range(n)]
    return product_kernel(feature)


def block_feature(n):
    return [mp.mpf(1) if i < n // 2 else mp.mpf(-1) for i in range(n)]


def cosine_feature(n):
    return [mp.cos(2 * mp.pi * i / n) for i in range(n)]


def permutation_order(n, seed):
    rng = random.Random(seed)
    perm = list(range(n))
    rng.shuffle(perm)
    future = [0 for _ in range(n)]
    past = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] < perm[j]:
                future[i] |= 1 << j
                past[j] |= 1 << i
    return future, past


def two_layer_order(n):
    half = n // 2
    future = [0 for _ in range(n)]
    past = [0 for _ in range(n)]
    for i in range(half):
        for j in range(half, n):
            future[i] |= 1 << j
            past[j] |= 1 << i
    return future, past


def interval_counts(n, future, past):
    out = []
    for i, j in pair_indices(n):
        if (future[i] >> j) & 1:
            out.append((future[i] & past[j]).bit_count())
        elif (future[j] >> i) & 1:
            out.append((future[j] & past[i]).bit_count())
        else:
            out.append(None)
    return out


def shell_stress_basis(n, interval_count, feature, max_shell):
    f = center(feature)
    basis = []
    pairs = pair_indices(n)
    for shell in range(max_shell + 1):
        values = []
        for idx, (i, j) in enumerate(pairs):
            if interval_count[idx] == shell:
                values.append((f[i] - f[j]) ** 2)
            else:
                values.append(mp.mpf(0))
        basis.append(zero_row_project_pair_vector(n, values))
    return basis


def shell_local_count(interval_count, max_shell):
    return sum(1 for value in interval_count if value is not None and value <= max_shell)


def comparable_count(interval_count):
    return sum(1 for value in interval_count if value is not None)


print("=" * 80)
print("Paper 27 order-intrinsic local response gate receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

max_shell = 4
sizes = [32, 64, 96, 128, 160, 192]
seeds_per_size = 3

sprinkling_rows = []
for n in sizes:
    block_fracs = []
    cos_fracs = []
    self_fracs = []
    local_counts = []
    comparable_counts = []
    for seed_index in range(seeds_per_size):
        seed = 271828 + 1009 * n + seed_index
        future, past = permutation_order(n, seed)
        counts = interval_counts(n, future, past)
        block = block_feature(n)
        cos = cosine_feature(n)
        block_basis = shell_stress_basis(n, counts, block, max_shell)
        cos_basis = shell_stress_basis(n, counts, cos, max_shell)
        block_fracs.append(projection_fraction(product_kernel(block), block_basis))
        cos_fracs.append(projection_fraction(cosine_product_kernel(n), cos_basis))
        local_target = zero_row_project_pair_vector(
            n,
            [
                mp.fsum(basis[idx] for basis in block_basis)
                for idx in range(len(block_basis[0]))
            ],
        )
        self_fracs.append(projection_fraction(local_target, block_basis))
        local_counts.append(shell_local_count(counts, max_shell))
        comparable_counts.append(comparable_count(counts))

    pair_total = n * (n - 1) // 2
    sprinkling_rows.append(
        {
            "n": n,
            "local_mean": mp.fsum(local_counts) / seeds_per_size,
            "local_fraction": mp.fsum(local_counts) / (seeds_per_size * pair_total),
            "comparable_fraction": mp.fsum(comparable_counts) / (seeds_per_size * pair_total),
            "block_projection_mean": mp.fsum(block_fracs) / seeds_per_size,
            "block_projection_max": max(block_fracs),
            "cos_projection_mean": mp.fsum(cos_fracs) / seeds_per_size,
            "self_projection_min": min(self_fracs),
        }
    )

print("\n=== Seeded sprinkling-like order-intrinsic shells ===")
print("N, mean local shell count, local shell fraction, comparable fraction, block projection mean, block projection max, cos projection mean, local self min")
for row in sprinkling_rows:
    print(
        f"{row['n']:4d} "
        f"{fmt(row['local_mean'], 14):>18s} "
        f"{fmt(row['local_fraction'], 14):>18s} "
        f"{fmt(row['comparable_fraction'], 14):>18s} "
        f"{fmt(row['block_projection_mean'], 14):>18s} "
        f"{fmt(row['block_projection_max'], 14):>18s} "
        f"{fmt(row['cos_projection_mean'], 14):>18s} "
        f"{fmt(row['self_projection_min'], 14):>18s}"
    )

layer_rows = []
for n in [32, 64, 128, 192]:
    future, past = two_layer_order(n)
    counts = interval_counts(n, future, past)
    block = block_feature(n)
    basis = shell_stress_basis(n, counts, block, max_shell)
    pair_total = n * (n - 1) // 2
    layer_rows.append(
        {
            "n": n,
            "local_count": shell_local_count(counts, max_shell),
            "local_fraction": mp.mpf(shell_local_count(counts, max_shell)) / pair_total,
            "comparable_fraction": mp.mpf(comparable_count(counts)) / pair_total,
            "block_projection": projection_fraction(product_kernel(block), basis),
        }
    )

print("\n=== Dense two-layer local-shell adversary ===")
print("N, local shell count, local shell fraction, comparable fraction, block projection")
for row in layer_rows:
    print(
        f"{row['n']:4d} "
        f"{row['local_count']:8d} "
        f"{fmt(row['local_fraction'], 14):>18s} "
        f"{fmt(row['comparable_fraction'], 14):>18s} "
        f"{fmt(row['block_projection'], 14):>18s}"
    )

local_fractions = [row["local_fraction"] for row in sprinkling_rows]
block_projection_means = [row["block_projection_mean"] for row in sprinkling_rows]
cos_projection_means = [row["cos_projection_mean"] for row in sprinkling_rows]
self_projection_mins = [row["self_projection_min"] for row in sprinkling_rows]
layer_local_fractions = [row["local_fraction"] for row in layer_rows]
layer_block_projections = [row["block_projection"] for row in layer_rows]

check(
    "sprinkling-like small interval shells are sparse and become sparser",
    bool(local_fractions[-1] < mp.mpf("0.15"))
    and local_fractions[0] > local_fractions[-1]
    and all(local_fractions[i] > local_fractions[i + 1] for i in range(len(local_fractions) - 1)),
    "local_fraction=" + ", ".join(fmt(value, 8) for value in local_fractions),
)
check(
    "intrinsic shell-local mark stress has decreasing projection on global block products",
    block_projection_means[-1] < mp.mpf("0.04")
    and block_projection_means[0] > mp.mpf("0.14")
    and all(block_projection_means[i] > block_projection_means[i + 1] for i in range(len(block_projection_means) - 1)),
    "block_proj_mean=" + ", ".join(fmt(value, 8) for value in block_projection_means),
)
check(
    "intrinsic shell-local mark stress also weakens on coherent cosine products",
    bool(cos_projection_means[-1] < mp.mpf("0.03"))
    and cos_projection_means[0] > mp.mpf("0.10")
    and cos_projection_means[-1] < cos_projection_means[0] / 3,
    "cos_proj_mean=" + ", ".join(fmt(value, 8) for value in cos_projection_means),
)
check(
    "genuinely shell-local marked responses remain in the intrinsic local span",
    min(self_projection_mins) > mp.mpf("0.999999999999"),
    "self_min=" + ", ".join(fmt(value, 8) for value in self_projection_mins),
)
check(
    "two-layer orders make intrinsic local shells dense",
    min(layer_local_fractions) > mp.mpf("0.49"),
    "layer_local_fraction=" + ", ".join(fmt(value, 8) for value in layer_local_fractions),
)
check(
    "dense shell locality can launder staging and must be rejected by shell regularity",
    min(layer_block_projections) > mp.mpf("0.999999999999"),
    "layer_block_projection=" + ", ".join(fmt(value, 8) for value in layer_block_projections),
)

print("\n=== Consequence ===")
print("Order-intrinsic locality can be defined by interval shells.  On seeded")
print("sprinkling-like orders, small shells are sparse, local marked responses stay")
print("inside the allowed local span, and dense global block/cosine products have")
print("decreasing projection onto that span.  But this only works together with a")
print("shell-density regularity law: in a two-layer order every cross-layer pair is")
print("a link, so the local shell is globally dense and can launder the layer block.")
print("Thus L(F) should be intrinsic shell-local response plus a manifoldlike shell")
print("sparsity/interval-profile gate, not shell-local response alone.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
