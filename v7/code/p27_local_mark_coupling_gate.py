#!/usr/bin/env python3
"""
Paper 27 receipt: local mark-coupling gate.

The projective mark-field receipt showed that exact hidden partition labels fail
finite-action refinement, while smooth/domain-wall-like fields can be legitimate
paid-for marks.  A sharper loophole remains:

    If a legitimate field mark is allowed to subtract arbitrary global pair
    products f(i) f(j) from geometry, then even a domain wall can launder a
    staged block.

This receipt tests the repair.  Mark projection credit should be local: fields
may affect geometry through local stress-like responses, not through arbitrary
global same-side/opposite-side pair products unless a separate nonlocal sector
is explicitly paid for.

Finite diagnostics:

  * global pair-product projection of a block mark erases a block exactly;
  * endpoint-additive local stress vanishes in the zero-row geometry subspace;
  * local wall-stress pair kernels project only O(N^-2) of the global block;
  * the same local-vs-global split holds for a coherent cosine kernel.

This is a hostile finite receipt, not a theorem.  It upgrades the candidate
law: marks must be projectively admissible, and their allowed geometry coupling
must be local or separately charged as a nonlocal interaction.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def center(feature):
    mean = mp.fsum(feature) / len(feature)
    return [mp.mpf(value) - mean for value in feature]


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


def product_kernel(feature_a, feature_b=None):
    if feature_b is None:
        feature_b = feature_a
        same = True
    else:
        same = False
    a = center(feature_a)
    b = center(feature_b)
    n = len(a)
    if same:
        values = [a[i] * a[j] for i, j in pair_indices(n)]
    else:
        values = [a[i] * b[j] + b[i] * a[j] for i, j in pair_indices(n)]
    return zero_row_project_pair_vector(n, values)


def additive_kernel(stress):
    s = center(stress)
    n = len(s)
    values = [s[i] + s[j] for i, j in pair_indices(n)]
    return zero_row_project_pair_vector(n, values)


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


def block_feature(n):
    return [mp.mpf(1) if i < n // 2 else mp.mpf(-1) for i in range(n)]


def cosine_feature(n, frequency=1):
    return [mp.cos(2 * mp.pi * frequency * i / n) for i in range(n)]


def sine_feature(n, frequency=1):
    return [mp.sin(2 * mp.pi * frequency * i / n) for i in range(n)]


def cosine_difference_kernel(n, frequency=1):
    values = [
        mp.cos(2 * mp.pi * frequency * (i - j) / n)
        for i, j in pair_indices(n)
    ]
    return zero_row_project_pair_vector(n, values)


def local_stress(feature):
    n = len(feature)
    return [
        (mp.mpf(n) ** 2) * (feature[(i + 1) % n] - feature[i]) ** 2
        for i in range(n)
    ]


def thicken(stress, radius):
    n = len(stress)
    return [
        mp.fsum(stress[(i + delta) % n] for delta in range(-radius, radius + 1))
        for i in range(n)
    ]


print("=" * 80)
print("Paper 27 local mark-coupling gate receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

sizes = [32, 64, 128, 256]
rows = []
for n in sizes:
    block = block_feature(n)
    block_target = product_kernel(block)
    block_stress = local_stress(block)
    local_fractions = []
    for radius in [0, 1, 2, 4, 8, 16]:
        if radius < n // 4:
            thickened = thicken(block_stress, radius)
            local_fractions.append((radius, projection_fraction(block_target, [product_kernel(thickened)])))

    cos = cosine_feature(n)
    sin = sine_feature(n)
    cos_target = cosine_difference_kernel(n)
    cos_stress = local_stress(cos)

    rows.append(
        {
            "n": n,
            "block_global": projection_fraction(block_target, [product_kernel(block)]),
            "block_additive": projection_fraction(block_target, [additive_kernel(block_stress)]),
            "block_local_max": max(value for _, value in local_fractions),
            "block_local_scaled": (mp.mpf(n) ** 2) * max(value for _, value in local_fractions),
            "block_local_fractions": local_fractions,
            "cos_global": projection_fraction(cos_target, [product_kernel(cos), product_kernel(sin)]),
            "cos_local": projection_fraction(cos_target, [product_kernel(cos_stress), additive_kernel(cos_stress)]),
            "cos_local_scaled": (mp.mpf(n) ** 2)
            * projection_fraction(cos_target, [product_kernel(cos_stress), additive_kernel(cos_stress)]),
        }
    )

print("\n=== Local versus global coupling ===")
print("N, block global product, block additive stress, max local wall-stress product, N^2 local, cos global, cos local stress, N^2 cos local")
for row in rows:
    print(
        f"{row['n']:4d} "
        f"{fmt(row['block_global'], 14):>18s} "
        f"{fmt(row['block_additive'], 14):>18s} "
        f"{fmt(row['block_local_max'], 14):>18s} "
        f"{fmt(row['block_local_scaled'], 14):>18s} "
        f"{fmt(row['cos_global'], 14):>18s} "
        f"{fmt(row['cos_local'], 14):>18s} "
        f"{fmt(row['cos_local_scaled'], 14):>18s}"
    )

print("\n=== Block wall-stress radius ladder ===")
print("N, radius, projection fraction")
for row in rows:
    for radius, value in row["block_local_fractions"]:
        print(f"{row['n']:4d} {radius:4d} {fmt(value, 18):>24s}")

block_global = [row["block_global"] for row in rows]
block_additive = [row["block_additive"] for row in rows]
block_local = [row["block_local_max"] for row in rows]
block_local_scaled = [row["block_local_scaled"] for row in rows]
cos_global = [row["cos_global"] for row in rows]
cos_local = [row["cos_local"] for row in rows]
cos_local_scaled = [row["cos_local_scaled"] for row in rows]

check(
    "global pair-product mark projection erases block geometry exactly",
    min(block_global) > mp.mpf("0.999999999999"),
    "block_global=" + ", ".join(fmt(value, 8) for value in block_global),
)
check(
    "endpoint-additive local stress has zero zero-row geometry projection",
    max(abs(value) for value in block_additive) < mp.mpf("1e-80"),
    "block_additive=" + ", ".join(fmt(value, 8) for value in block_additive),
)
check(
    "local wall-stress product projection decays like O(N^-2)",
    all(block_local[i] > block_local[i + 1] for i in range(len(block_local) - 1))
    and max(block_local_scaled) < mp.mpf("2.1")
    and min(block_local_scaled) > mp.mpf("1.9"),
    "N2_local=" + ", ".join(fmt(value, 10) for value in block_local_scaled),
)
check(
    "global Fourier product erases coherent cosine geometry exactly",
    min(cos_global) > mp.mpf("0.999999999999"),
    "cos_global=" + ", ".join(fmt(value, 8) for value in cos_global),
)
check(
    "local cosine stress does not launder global coherent pair geometry",
    all(cos_local[i] > cos_local[i + 1] for i in range(len(cos_local) - 1))
    and max(cos_local_scaled) < mp.mpf("2.5")
    and min(cos_local_scaled) > mp.mpf("2.0"),
    "N2_cos_local=" + ", ".join(fmt(value, 10) for value in cos_local_scaled),
)
check(
    "local coupling separates admissible marks from nonlocal projection credit",
    block_local[-1] < mp.mpf("0.00004") and cos_local[-1] < mp.mpf("0.00004"),
    f"block_local_256={fmt(block_local[-1], 14)} cos_local_256={fmt(cos_local[-1], 14)}",
)

print("\n=== Consequence ===")
print("Projective finite-action marks are still not enough if the projection map is")
print("allowed to be arbitrary and global.  A block mark f can erase a block through")
print("the nonlocal product f(i)f(j), but its local stress has essentially no")
print("zero-row geometry projection: the tested projection is O(N^-2).  The same")
print("split appears for coherent cosine structure.  Therefore the mark law needs a")
print("second gate: admissible marks may receive only local/stress-type geometry")
print("coupling, unless a separate nonlocal interaction sector is explicitly")
print("included and charged.  This keeps legitimate fields without letting them")
print("silently define hidden global staging.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
