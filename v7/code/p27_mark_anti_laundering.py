#!/usr/bin/env python3
"""
Paper 27 receipt: anti-laundering tests for the marked sector.

The previous receipt showed that explicit marks can rescue genuine coherent
waves, but arbitrary marks can also hide staged/block geometry.  This receipt
tests the next constraint: marks are not free labels.  If marks project away a
geometric kernel, the law must charge their own action/complexity and must not
allow marks to be chosen after seeing the geometry.

Finite diagnostics:

  * scaled Dirichlet action of marks on the rank circle;
  * Fourier tail and Fourier projection of block labels;
  * exact small-N pair-kernel projection fractions;
  * smooth steep marks that approximate a block without O(N) exact-step
    action, but pay a large finite action and spectral tail.

This is a hostile finite receipt, not a theorem.  The result is a constraint on
the law form: sectoral projection must be coupled to mark action and an
anti-laundering admissibility rule.

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


def norm2(feature):
    return mp.fsum(value * value for value in feature)


def orthonormal_features(features):
    out = []
    for feature in features:
        v = center(feature)
        for basis in out:
            coeff = mp.fsum(v[i] * basis[i] for i in range(len(v)))
            v = [v[i] - coeff * basis[i] for i in range(len(v))]
        n2 = norm2(v)
        if n2 > mp.mpf("1e-90"):
            nrm = mp.sqrt(n2)
            out.append([value / nrm for value in v])
    return out


def feature_energy(features):
    """Scaled rank-circle Dirichlet action of an orthonormal feature set."""
    ortho = orthonormal_features(features)
    if not ortho:
        return mp.mpf(0)
    n = len(ortho[0])
    return mp.fsum(
        (mp.mpf(n) ** 2)
        * mp.fsum((feature[(i + 1) % n] - feature[i]) ** 2 for i in range(n))
        for feature in ortho
    )


def fourier_features(n, max_frequency):
    features = []
    for k in range(1, max_frequency + 1):
        features.append([mp.cos(2 * mp.pi * k * i / n) for i in range(n)])
        features.append([mp.sin(2 * mp.pi * k * i / n) for i in range(n)])
    return features


def block_feature(n):
    return [mp.mpf(1) if i < n // 2 else mp.mpf(-1) for i in range(n)]


def soft_block_feature(n, beta):
    return [mp.tanh(mp.mpf(beta) * mp.sin(2 * mp.pi * i / n)) for i in range(n)]


def linear_projection_fraction(feature, features):
    f = center(feature)
    total = norm2(f)
    if total == 0:
        return mp.mpf(0)
    return mp.fsum(
        mp.fsum(f[i] * basis[i] for i in range(len(f))) ** 2
        for basis in orthonormal_features(features)
    ) / total


def feature_alignment(a, b):
    ca = center(a)
    cb = center(b)
    denom = norm2(ca) * norm2(cb)
    if denom == 0:
        return mp.mpf(0)
    return (mp.fsum(ca[i] * cb[i] for i in range(len(ca))) ** 2) / denom


def fourier_tail(feature, max_frequency):
    return max(mp.mpf(0), 1 - linear_projection_fraction(feature, fourier_features(len(feature), max_frequency)))


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


def pair_kernel_from_feature(feature):
    f = center(feature)
    n = len(f)
    values = [f[i] * f[j] for i, j in pair_indices(n)]
    return zero_row_project_pair_vector(n, values)


def pair_basis_from_features(features):
    ortho = orthonormal_features(features)
    if not ortho:
        return []
    n = len(ortho[0])
    basis = []
    for a in range(len(ortho)):
        for b in range(a, len(ortho)):
            values = []
            for i, j in pair_indices(n):
                if a == b:
                    values.append(ortho[a][i] * ortho[a][j])
                else:
                    values.append(ortho[a][i] * ortho[b][j] + ortho[b][i] * ortho[a][j])
            projected = zero_row_project_pair_vector(n, values)
            if pair_inner(projected, projected) > mp.mpf("1e-90"):
                basis.append(projected)
    return basis


def pair_projection_fraction(target, features):
    basis = pair_basis_from_features(features)
    if not basis:
        return mp.mpf(0)
    m = len(basis)
    gram = mp.matrix(m)
    rhs = mp.matrix(m, 1)
    for i, bi in enumerate(basis):
        rhs[i] = pair_inner(target, bi)
        for j, bj in enumerate(basis):
            gram[i, j] = pair_inner(bi, bj)
    coeffs = mp.lu_solve(gram, rhs)
    projected_norm = mp.fsum(coeffs[i] * rhs[i] for i in range(m))
    return projected_norm / pair_inner(target, target)


print("=" * 80)
print("Paper 27 mark anti-laundering receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

sizes = [16, 32, 64, 128]
beta = mp.mpf(8)

energy_rows = []
for n in sizes:
    block = block_feature(n)
    soft = soft_block_feature(n, beta)
    e_fourier1 = feature_energy(fourier_features(n, 1))
    e_block = feature_energy([block])
    e_soft = feature_energy([soft])
    align_soft = feature_alignment(block, soft)
    tail_block_4 = fourier_tail(block, 4)
    tail_soft_4 = fourier_tail(soft, 4)
    tail_soft_8 = fourier_tail(soft, 8)
    energy_rows.append(
        {
            "n": n,
            "e_fourier1": e_fourier1,
            "e_block": e_block,
            "e_soft": e_soft,
            "align_soft": align_soft,
            "tail_block_4": tail_block_4,
            "tail_soft_4": tail_soft_4,
            "tail_soft_8": tail_soft_8,
        }
    )

print("\n=== Mark action and spectral leakage ===")
print("N, E(cos1,sin1), E(exact block), E(soft beta=8), align(soft,block), tail4(block), tail4(soft), tail8(soft)")
for row in energy_rows:
    print(
        f"{row['n']:3d} "
        f"{fmt(row['e_fourier1'], 14):>18s} "
        f"{fmt(row['e_block'], 14):>18s} "
        f"{fmt(row['e_soft'], 14):>18s} "
        f"{fmt(row['align_soft'], 14):>18s} "
        f"{fmt(row['tail_block_4'], 14):>18s} "
        f"{fmt(row['tail_soft_4'], 14):>18s} "
        f"{fmt(row['tail_soft_8'], 14):>18s}"
    )

band_rows = []
n_band = 64
block_64 = block_feature(n_band)
for k in [1, 2, 4, 8, 16]:
    features = fourier_features(n_band, k)
    band_rows.append(
        {
            "k": k,
            "linear_fraction": linear_projection_fraction(block_64, features),
            "pair_lower": linear_projection_fraction(block_64, features) ** 2,
            "energy": feature_energy(features),
            "tail": fourier_tail(block_64, k),
        }
    )

print("\n=== Fourier-band laundering ladder at N=64 ===")
print("K, linear block fraction, pair-kernel lower proxy, mark energy, remaining Fourier tail")
for row in band_rows:
    print(
        f"{row['k']:3d} "
        f"{fmt(row['linear_fraction'], 14):>18s} "
        f"{fmt(row['pair_lower'], 14):>18s} "
        f"{fmt(row['energy'], 14):>18s} "
        f"{fmt(row['tail'], 14):>18s}"
    )

pair_rows = []
for n, ks in [(16, [1, 4, 6]), (24, [1, 4, 8])]:
    target = pair_kernel_from_feature(block_feature(n))
    for k in ks:
        pair_rows.append(
            {
                "n": n,
                "kind": f"fourier K={k}",
                "fraction": pair_projection_fraction(target, fourier_features(n, k)),
                "energy": feature_energy(fourier_features(n, k)),
            }
        )
    pair_rows.append(
        {
            "n": n,
            "kind": "soft beta=8",
            "fraction": pair_projection_fraction(target, [soft_block_feature(n, beta)]),
            "energy": feature_energy([soft_block_feature(n, beta)]),
        }
    )
    pair_rows.append(
        {
            "n": n,
            "kind": "exact block",
            "fraction": pair_projection_fraction(target, [block_feature(n)]),
            "energy": feature_energy([block_feature(n)]),
        }
    )

print("\n=== Exact small-N pair-kernel projection fractions ===")
print("N, marks, projected block-pair fraction, mark energy")
for row in pair_rows:
    print(
        f"{row['n']:3d} "
        f"{row['kind']:>14s} "
        f"{fmt(row['fraction'], 14):>18s} "
        f"{fmt(row['energy'], 14):>18s}"
    )

block_energy = [row["e_block"] for row in energy_rows]
fourier1_energy = [row["e_fourier1"] for row in energy_rows]
soft_energy = [row["e_soft"] for row in energy_rows]
soft_align = [row["align_soft"] for row in energy_rows]
soft_tail4 = [row["tail_soft_4"] for row in energy_rows]
block_tail4 = [row["tail_block_4"] for row in energy_rows]

band_fraction = [row["linear_fraction"] for row in band_rows]
band_energy = [row["energy"] for row in band_rows]
band_tail = [row["tail"] for row in band_rows]

pair_fraction_by_key = {(row["n"], row["kind"]): row["fraction"] for row in pair_rows}
block_growth_ratio = block_energy[-1] / block_energy[0]

check(
    "exact block labels can erase block geometry only with growing exact-step action",
    abs(block_growth_ratio - mp.mpf(8)) < mp.mpf("1e-80")
    and all(block_energy[i] < block_energy[i + 1] for i in range(len(block_energy) - 1)),
    "E_block=" + ", ".join(fmt(value, 10) for value in block_energy)
    + " growth=" + fmt(block_growth_ratio, 10),
)
check(
    "low Fourier field marks have bounded action over tested N",
    max(fourier1_energy) < mp.mpf(80),
    "max_E_fourier1=" + fmt(max(fourier1_energy), 14),
)
check(
    "smooth steep marks strongly align with block but pay large finite action",
    soft_align[-1] > mp.mpf("0.96")
    and soft_energy[-1] > mp.mpf(100)
    and soft_energy[-1] < block_energy[-1],
    f"N128_align={fmt(soft_align[-1], 14)} E_soft={fmt(soft_energy[-1], 14)} E_block={fmt(block_energy[-1], 14)}",
)
check(
    "spectral tail detects nontrivial blocklike content in steep marks",
    max(soft_tail4) > mp.mpf("0.04") and min(block_tail4) > mp.mpf("0.07"),
    "max_soft_tail4=" + fmt(max(soft_tail4), 14) + " min_block_tail4=" + fmt(min(block_tail4), 14),
)
check(
    "Fourier bands launder the block only by increasing bandwidth and action",
    band_fraction[0] < mp.mpf("0.82")
    and band_fraction[3] > mp.mpf("0.95")
    and band_energy[3] > 20 * band_energy[0]
    and band_tail[3] < band_tail[0],
    f"K1_frac={fmt(band_fraction[0], 14)} K8_frac={fmt(band_fraction[3], 14)} "
    f"E8/E1={fmt(band_energy[3] / band_energy[0], 14)}",
)
check(
    "exact small-N pair projections show the same laundering ladder",
    pair_fraction_by_key[(16, "fourier K=1")] < mp.mpf("0.70")
    and pair_fraction_by_key[(16, "fourier K=6")] > mp.mpf("0.94")
    and pair_fraction_by_key[(24, "fourier K=8")] > mp.mpf("0.93"),
    f"N16K1={fmt(pair_fraction_by_key[(16, 'fourier K=1')], 14)} "
    f"N16K6={fmt(pair_fraction_by_key[(16, 'fourier K=6')], 14)} "
    f"N24K8={fmt(pair_fraction_by_key[(24, 'fourier K=8')], 14)}",
)
check(
    "single smooth steep mark partially launders pair geometry but does not make projection free",
    pair_fraction_by_key[(24, "soft beta=8")] > mp.mpf("0.80")
    and pair_fraction_by_key[(24, "soft beta=8")] < mp.mpf("0.90")
    and feature_energy([soft_block_feature(24, beta)]) > feature_energy(fourier_features(24, 1)),
    f"N24_soft_pair={fmt(pair_fraction_by_key[(24, 'soft beta=8')], 14)} "
    f"E_soft/E_fourier1={fmt(feature_energy([soft_block_feature(24, beta)]) / feature_energy(fourier_features(24, 1)), 14)}",
)
check(
    "free post-hoc marks would make block geometry admissible, so admissibility is essential",
    pair_fraction_by_key[(16, "exact block")] > mp.mpf("0.999999999999")
    and pair_fraction_by_key[(24, "exact block")] > mp.mpf("0.999999999999"),
    f"N16_exact={fmt(pair_fraction_by_key[(16, 'exact block')], 14)} "
    f"N24_exact={fmt(pair_fraction_by_key[(24, 'exact block')], 14)}",
)

print("\n=== Consequence ===")
print("The hostile result is not a clean ban on marks.  Correct low-frequency")
print("marks can be cheap and legitimate.  Exact block marks erase block geometry")
print("but pay action growing like N.  Fourier bands and smooth steep marks can")
print("launder a large part of block geometry only by spending bandwidth/action.")
print("Therefore the click law cannot allow arbitrary post-hoc marks, and it also")
print("cannot reject every high-alignment field.  The necessary object is a joint")
print("geometry-plus-mark action with an admissibility rule: marks must be generated")
print("by an independent/projective field law before geometry projection, and their")
print("projection credit must be charged to their own action/complexity.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
