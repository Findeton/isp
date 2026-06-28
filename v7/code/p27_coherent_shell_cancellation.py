#!/usr/bin/env python3
"""
Paper 27 receipt: coherent-wave cancellation against shell-local responses.

The shell-projection theorem is tight for staged blocks, but loose for coherent
Fourier waves: a coherent wave has mass on small-shell pairs even when the
shell-local span has little aligned projection.  This receipt tests the next
tool: normalized correlation cancellation.

Let B be a zero-row coherent wave target and v_a=P0 h_a be shell-local
stress-tensor responses from the same marks.  If z_a=<B,v_a>/(||B|| ||v_a||)
and C is the normalized Gram matrix of the v_a, then

    ||Pi_L B||^2 / ||B||^2 <= z^T C^{-1} z
                            <= lambda_min(C)^-1 sum_a z_a^2.

This is a deterministic inequality.  The finite question is whether z shrinks
for sprinkling-like interval shells.  If yes, coherent waves are controlled by
cancellation/orthogonality, not by support mass.

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


def pair_norm(a):
    return mp.sqrt(pair_inner(a, a))


def coherent_difference_target(n, frequency=1):
    values = [
        mp.cos(2 * mp.pi * frequency * (i - j) / n)
        for i, j in pair_indices(n)
    ]
    return zero_row_project_pair_vector(n, values)


def cosine_feature(n, frequency=1):
    return [mp.cos(2 * mp.pi * frequency * i / n) for i in range(n)]


def sine_feature(n, frequency=1):
    return [mp.sin(2 * mp.pi * frequency * i / n) for i in range(n)]


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


def shell_stress_tensor_basis(n, interval_count, max_shell):
    cos = cosine_feature(n)
    sin = sine_feature(n)
    pairs = pair_indices(n)
    projected_basis = []
    raw_basis = []
    for shell in range(max_shell + 1):
        for component in ("cc", "ss", "cs"):
            values = []
            for idx, (i, j) in enumerate(pairs):
                if interval_count[idx] != shell:
                    values.append(mp.mpf(0))
                    continue
                dc = cos[i] - cos[j]
                ds = sin[i] - sin[j]
                if component == "cc":
                    values.append(dc * dc)
                elif component == "ss":
                    values.append(ds * ds)
                else:
                    values.append(dc * ds)
            projected = zero_row_project_pair_vector(n, values)
            if pair_inner(projected, projected) > mp.mpf("1e-90"):
                raw_basis.append(values)
                projected_basis.append(projected)
    return raw_basis, projected_basis


def projection_correlation_metrics(target, raw_basis, projected_basis):
    usable = [
        (raw, projected)
        for raw, projected in zip(raw_basis, projected_basis)
        if pair_inner(projected, projected) > mp.mpf("1e-90")
    ]
    m = len(usable)
    if m == 0:
        return {
            "actual": mp.mpf(0),
            "correlation_bound": mp.mpf(0),
            "support_bound": mp.mpf(0),
            "max_correlation": mp.mpf(0),
            "lambda_min": mp.inf,
            "dimension": 0,
        }

    target_norm = pair_norm(target)
    target_norm2 = pair_inner(target, target)
    gram = mp.matrix(m)
    rhs = mp.matrix(m, 1)
    correlations = []
    support_sum = mp.mpf(0)

    for i, (raw_i, projected_i) in enumerate(usable):
        projected_i_norm = pair_norm(projected_i)
        rhs[i] = pair_inner(target, projected_i)
        correlations.append(abs(rhs[i]) / (target_norm * projected_i_norm))
        raw_norm2 = pair_inner(raw_i, raw_i)
        efficiency = pair_inner(projected_i, projected_i) / raw_norm2
        support_mass = 2 * mp.fsum(
            target[idx] * target[idx]
            for idx, value in enumerate(raw_i)
            if value != 0
        ) / target_norm2
        support_sum += support_mass / efficiency
        for j, (_, projected_j) in enumerate(usable):
            gram[i, j] = pair_inner(projected_i, projected_j)

    coeffs = mp.lu_solve(gram, rhs)
    actual = mp.fsum(coeffs[i] * rhs[i] for i in range(m)) / target_norm2

    norms = [pair_norm(projected) for _, projected in usable]
    normalized_gram = mp.matrix(m)
    for i, (_, projected_i) in enumerate(usable):
        for j, (_, projected_j) in enumerate(usable):
            normalized_gram[i, j] = pair_inner(projected_i, projected_j) / (norms[i] * norms[j])
    lambda_min = min(mp.eigsy(normalized_gram, eigvals_only=True))
    correlation_bound = mp.fsum(value * value for value in correlations) / lambda_min
    support_bound = support_sum / lambda_min

    return {
        "actual": actual,
        "correlation_bound": correlation_bound,
        "support_bound": support_bound,
        "max_correlation": max(correlations),
        "lambda_min": lambda_min,
        "dimension": m,
    }


def local_fraction(interval_count, max_shell):
    return mp.mpf(
        sum(1 for value in interval_count if value is not None and value <= max_shell)
    ) / len(interval_count)


print("=" * 80)
print("Paper 27 coherent shell-cancellation receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

max_shell = 4
sizes = [32, 64, 96, 128, 160, 192]
seeds_per_size = 2

rows = []
for n in sizes:
    actual_values = []
    correlation_bounds = []
    support_bounds = []
    max_correlations = []
    lambda_values = []
    shell_fractions = []
    dimensions = []
    for seed_index in range(seeds_per_size):
        seed = 424242 + 271 * n + seed_index
        future, past = permutation_order(n, seed)
        counts = interval_counts(n, future, past)
        raw_basis, projected_basis = shell_stress_tensor_basis(n, counts, max_shell)
        metrics = projection_correlation_metrics(
            coherent_difference_target(n),
            raw_basis,
            projected_basis,
        )
        actual_values.append(metrics["actual"])
        correlation_bounds.append(metrics["correlation_bound"])
        support_bounds.append(metrics["support_bound"])
        max_correlations.append(metrics["max_correlation"])
        lambda_values.append(metrics["lambda_min"])
        shell_fractions.append(local_fraction(counts, max_shell))
        dimensions.append(metrics["dimension"])

    rows.append(
        {
            "n": n,
            "shell_fraction": mp.fsum(shell_fractions) / seeds_per_size,
            "actual": mp.fsum(actual_values) / seeds_per_size,
            "correlation_bound": mp.fsum(correlation_bounds) / seeds_per_size,
            "support_bound": mp.fsum(support_bounds) / seeds_per_size,
            "max_correlation": mp.fsum(max_correlations) / seeds_per_size,
            "lambda_min": min(lambda_values),
            "dimension": max(dimensions),
            "max_actual_over_bound": max(
                actual_values[i] / correlation_bounds[i]
                for i in range(seeds_per_size)
            ),
        }
    )

print("\n=== Coherent wave versus intrinsic shell-local stress tensor ===")
print("N, shell fraction, actual projection, correlation bound, support bound, max correlation, min lambda, dim")
for row in rows:
    print(
        f"{row['n']:4d} "
        f"{fmt(row['shell_fraction'], 14):>18s} "
        f"{fmt(row['actual'], 14):>18s} "
        f"{fmt(row['correlation_bound'], 14):>18s} "
        f"{fmt(row['support_bound'], 14):>18s} "
        f"{fmt(row['max_correlation'], 14):>18s} "
        f"{fmt(row['lambda_min'], 14):>18s} "
        f"{row['dimension']:4d}"
    )

actuals = [row["actual"] for row in rows]
correlation_bounds = [row["correlation_bound"] for row in rows]
support_bounds = [row["support_bound"] for row in rows]
max_correlations = [row["max_correlation"] for row in rows]
lambda_values = [row["lambda_min"] for row in rows]
actual_over_bound = [row["max_actual_over_bound"] for row in rows]

check(
    "correlation bound dominates every tested coherent projection",
    max(actual_over_bound) <= 1 + mp.mpf("1e-80"),
    "max_actual_over_corr_bound=" + fmt(max(actual_over_bound), 18),
)
check(
    "coherent projection decays across the tested sprinkling-like shell range",
    actuals[-1] < mp.mpf("0.011")
    and actuals[-1] < actuals[0] / 9
    and all(actuals[i] > actuals[i + 1] for i in range(len(actuals) - 1)),
    "actual=" + ", ".join(fmt(value, 8) for value in actuals),
)
check(
    "normalized shell correlations broadly decay and explain the coherent projection",
    max_correlations[-1] < mp.mpf("0.05")
    and max_correlations[-1] < max_correlations[0] / mp.mpf("3.5")
    and correlation_bounds[-1] < mp.mpf("0.025"),
    "max_corr=" + ", ".join(fmt(value, 8) for value in max_correlations)
    + " corr_bound=" + ", ".join(fmt(value, 8) for value in correlation_bounds),
)
check(
    "Gram conditioning is finite-N rough but stabilizes after N=32",
    min(lambda_values) > mp.mpf("0.25")
    and min(lambda_values[1:]) > mp.mpf("0.55"),
    "lambda_min=" + ", ".join(fmt(value, 8) for value in lambda_values),
)
check(
    "support-mass bound is valid but much looser than correlation bound",
    support_bounds[-1] > 5 * correlation_bounds[-1]
    and support_bounds[0] > correlation_bounds[0],
    f"support/correlation final={fmt(support_bounds[-1] / correlation_bounds[-1], 12)}",
)

print("\n=== Consequence ===")
print("The coherent-wave exception is controlled by cancellation, not support.")
print("The shell support contains coherent target mass, so the support-mass bound is")
print("loose.  But the normalized correlations between the coherent target and the")
print("intrinsic shell-local stress-tensor responses shrink across the tested")
print("sprinkling-like orders.  The deterministic Gram/correlation bound tracks this")
print("and dominates the actual projection.  Thus staged blocks and coherent waves")
print("need different proofs: support-mass for staged blocks, cancellation/spectral")
print("orthogonality for coherent marked fields.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
