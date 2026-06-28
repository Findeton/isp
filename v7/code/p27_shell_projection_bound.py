#!/usr/bin/env python3
"""
Paper 27 receipt: shell-local projection bound.

This receipt turns the previous intrinsic-shell diagnostic into the first small
linear-algebra lemma.

Let H be the zero-row pair-kernel space.  Let B in H be a dense geometry
residue, and let h_a be raw shell-local marked response vectors supported on
small interval shells.  Write v_a = P0 h_a for their zero-row projections.

For L = span{v_a}, the projection fraction obeys the deterministic bound

    ||Pi_L B||^2 / ||B||^2
      <= lambda_min(C)^-1
         sum_a mass_B(supp h_a) / eff_a,

where C is the normalized Gram matrix of the nonzero v_a and

    eff_a = ||P0 h_a||^2 / ||h_a||^2.

The proof is just Cauchy-Schwarz plus Gram conditioning:

    <B,v_a> = <B,h_a>

because B is zero-row, then each normalized coordinate is bounded by the B-mass
inside the raw support divided by the zero-row efficiency.

This is not the final manifold theorem, but it gives the desired spine:
small shell support plus nondegenerate zero-row efficiency plus controlled Gram
conditioning prevents shell-local marks from erasing dense staged geometry.

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


def product_kernel(feature):
    f = center(feature)
    n = len(f)
    return zero_row_project_pair_vector(n, [f[i] * f[j] for i, j in pair_indices(n)])


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


def shell_raw_basis(n, interval_count, feature, max_shell):
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
        basis.append(values)
    return basis


def local_fraction(interval_count, max_shell):
    local = sum(1 for value in interval_count if value is not None and value <= max_shell)
    total = len(interval_count)
    return mp.mpf(local) / total


def projection_and_bound(target, raw_basis):
    n = int((1 + mp.sqrt(1 + 8 * len(target))) / 2)
    projected = []
    raw_kept = []
    efficiencies = []
    for raw in raw_basis:
        raw_norm = pair_inner(raw, raw)
        if raw_norm <= mp.mpf("1e-90"):
            continue
        v = zero_row_project_pair_vector(n, raw)
        v_norm = pair_inner(v, v)
        if v_norm <= mp.mpf("1e-90"):
            continue
        raw_kept.append(raw)
        projected.append(v)
        efficiencies.append(v_norm / raw_norm)

    m = len(projected)
    if m == 0:
        return {
            "actual": mp.mpf(0),
            "bound": mp.mpf(0),
            "lambda_min": mp.inf,
            "sum_term": mp.mpf(0),
            "min_efficiency": mp.inf,
            "dimension": 0,
        }

    gram = mp.matrix(m)
    rhs = mp.matrix(m, 1)
    for i, vi in enumerate(projected):
        rhs[i] = pair_inner(target, vi)
        for j, vj in enumerate(projected):
            gram[i, j] = pair_inner(vi, vj)
    coeffs = mp.lu_solve(gram, rhs)
    target_norm = pair_inner(target, target)
    actual = mp.fsum(coeffs[i] * rhs[i] for i in range(m)) / target_norm

    norms = [mp.sqrt(pair_inner(v, v)) for v in projected]
    normalized_gram = mp.matrix(m)
    for i in range(m):
        for j in range(m):
            normalized_gram[i, j] = pair_inner(projected[i], projected[j]) / (norms[i] * norms[j])
    lambda_min = min(mp.eigsy(normalized_gram, eigvals_only=True))

    sum_term = mp.mpf(0)
    for raw, efficiency in zip(raw_kept, efficiencies):
        support_mass = 2 * mp.fsum(
            target[idx] * target[idx]
            for idx, value in enumerate(raw)
            if value != 0
        ) / target_norm
        sum_term += support_mass / efficiency

    bound = sum_term / lambda_min
    return {
        "actual": actual,
        "bound": bound,
        "lambda_min": lambda_min,
        "sum_term": sum_term,
        "min_efficiency": min(efficiencies),
        "dimension": m,
    }


print("=" * 80)
print("Paper 27 shell-local projection bound receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

max_shell = 4
sizes = [32, 64, 96, 128, 160, 192]
seeds_per_size = 2

sprinkling_rows = []
for n in sizes:
    block_actual = []
    block_bound = []
    cos_actual = []
    cos_bound = []
    shell_fraction = []
    lambda_min_values = []
    efficiency_values = []
    for seed_index in range(seeds_per_size):
        seed = 314159 + 1613 * n + seed_index
        future, past = permutation_order(n, seed)
        counts = interval_counts(n, future, past)
        block = block_feature(n)
        cos = cosine_feature(n)
        block_metrics = projection_and_bound(
            product_kernel(block),
            shell_raw_basis(n, counts, block, max_shell),
        )
        cos_metrics = projection_and_bound(
            product_kernel(cos),
            shell_raw_basis(n, counts, cos, max_shell),
        )
        block_actual.append(block_metrics["actual"])
        block_bound.append(block_metrics["bound"])
        cos_actual.append(cos_metrics["actual"])
        cos_bound.append(cos_metrics["bound"])
        shell_fraction.append(local_fraction(counts, max_shell))
        lambda_min_values.append(min(block_metrics["lambda_min"], cos_metrics["lambda_min"]))
        efficiency_values.append(min(block_metrics["min_efficiency"], cos_metrics["min_efficiency"]))

    sprinkling_rows.append(
        {
            "n": n,
            "shell_fraction": mp.fsum(shell_fraction) / seeds_per_size,
            "block_actual": mp.fsum(block_actual) / seeds_per_size,
            "block_bound": mp.fsum(block_bound) / seeds_per_size,
            "cos_actual": mp.fsum(cos_actual) / seeds_per_size,
            "cos_bound": mp.fsum(cos_bound) / seeds_per_size,
            "min_lambda": min(lambda_min_values),
            "min_efficiency": min(efficiency_values),
            "max_actual_over_bound": max(
                max(block_actual[i] / block_bound[i], cos_actual[i] / cos_bound[i])
                for i in range(seeds_per_size)
            ),
        }
    )

print("\n=== Seeded sprinkling-like shell projection bound ===")
print("N, shell fraction, block actual, block bound, cos actual, cos bound, min lambda, min efficiency")
for row in sprinkling_rows:
    print(
        f"{row['n']:4d} "
        f"{fmt(row['shell_fraction'], 14):>18s} "
        f"{fmt(row['block_actual'], 14):>18s} "
        f"{fmt(row['block_bound'], 14):>18s} "
        f"{fmt(row['cos_actual'], 14):>18s} "
        f"{fmt(row['cos_bound'], 14):>18s} "
        f"{fmt(row['min_lambda'], 14):>18s} "
        f"{fmt(row['min_efficiency'], 14):>18s}"
    )

layer_rows = []
for n in [32, 64, 128, 192]:
    future, past = two_layer_order(n)
    counts = interval_counts(n, future, past)
    block = block_feature(n)
    metrics = projection_and_bound(
        product_kernel(block),
        shell_raw_basis(n, counts, block, max_shell),
    )
    layer_rows.append(
        {
            "n": n,
            "shell_fraction": local_fraction(counts, max_shell),
            "actual": metrics["actual"],
            "bound": metrics["bound"],
            "lambda_min": metrics["lambda_min"],
            "min_efficiency": metrics["min_efficiency"],
        }
    )

print("\n=== Two-layer shell projection bound ===")
print("N, shell fraction, actual, bound, lambda_min, min efficiency")
for row in layer_rows:
    print(
        f"{row['n']:4d} "
        f"{fmt(row['shell_fraction'], 14):>18s} "
        f"{fmt(row['actual'], 14):>18s} "
        f"{fmt(row['bound'], 14):>18s} "
        f"{fmt(row['lambda_min'], 14):>18s} "
        f"{fmt(row['min_efficiency'], 14):>18s}"
    )

block_actuals = [row["block_actual"] for row in sprinkling_rows]
block_bounds = [row["block_bound"] for row in sprinkling_rows]
cos_actuals = [row["cos_actual"] for row in sprinkling_rows]
cos_bounds = [row["cos_bound"] for row in sprinkling_rows]
shell_fractions = [row["shell_fraction"] for row in sprinkling_rows]
max_actual_over_bound = max(row["max_actual_over_bound"] for row in sprinkling_rows)
layer_actuals = [row["actual"] for row in layer_rows]
layer_shell_fractions = [row["shell_fraction"] for row in layer_rows]

check(
    "deterministic projection bound dominates every tested actual projection",
    max_actual_over_bound <= 1 + mp.mpf("1e-80"),
    "max_actual_over_bound=" + fmt(max_actual_over_bound, 18),
)
check(
    "sprinkling-like shell support fraction decreases over tested range",
    shell_fractions[-1] < mp.mpf("0.15")
    and all(shell_fractions[i] > shell_fractions[i + 1] for i in range(len(shell_fractions) - 1)),
    "shell_fraction=" + ", ".join(fmt(value, 8) for value in shell_fractions),
)
check(
    "block projection and bound both shrink with sprinkling-like shells",
    block_actuals[-1] < mp.mpf("0.05")
    and block_bounds[-1] < mp.mpf("0.06")
    and all(block_actuals[i] > block_actuals[i + 1] for i in range(len(block_actuals) - 1)),
    "block_actual=" + ", ".join(fmt(value, 8) for value in block_actuals)
    + " block_bound=" + ", ".join(fmt(value, 8) for value in block_bounds),
)
check(
    "cosine actual projection shrinks but the support-mass bound is loose",
    cos_actuals[-1] < mp.mpf("0.05")
    and cos_actuals[-1] < cos_actuals[0] / 3
    and cos_bounds[-1] > mp.mpf("0.10"),
    "cos_actual=" + ", ".join(fmt(value, 8) for value in cos_actuals)
    + " cos_bound=" + ", ".join(fmt(value, 8) for value in cos_bounds),
)
check(
    "two-layer dense shell adversary saturates projection and fails shell gate",
    min(layer_actuals) > mp.mpf("0.999999999999")
    and min(layer_shell_fractions) > mp.mpf("0.49"),
    "layer_actual=" + ", ".join(fmt(value, 8) for value in layer_actuals)
    + " layer_shell=" + ", ".join(fmt(value, 8) for value in layer_shell_fractions),
)

print("\n=== Consequence ===")
print("The first small theorem is a deterministic projection inequality.  A")
print("shell-local span can erase a dense target only through the target's mass on")
print("the local shell support, amplified by zero-row efficiency and Gram")
print("conditioning.  For the staged block target the bound is tight and shrinks")
print("with the shell fraction.  For coherent cosine structure the same bound is")
print("valid but loose, because shell support contains target mass even when the")
print("local span has little aligned projection.  On the two-layer order the shell")
print("fraction is O(1), so the bound and actual projection both allow laundering.")
print("Thus the record law needs the paired condition already identified: intrinsic")
print("local response plus calibrated shell-density regularity.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
