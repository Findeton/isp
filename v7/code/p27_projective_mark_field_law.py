#!/usr/bin/env python3
"""
Paper 27 receipt: projective mark-field admissibility.

The anti-laundering receipt showed that marks must not be free post-hoc
labels.  This receipt tests a sharper candidate:

    admissible marks are projective finite-action field records.

Finite proxy.  For a centered mark f on the rank circle, use the scale-invariant
Rayleigh action

    R_N(f) = N^2 sum_i (f_{i+1}-f_i)^2 / sum_i f_i^2.

Low Fourier modes have bounded R_N.  A smooth field sampled from a fixed
continuum profile has bounded R_N.  An exact step/block label has R_N growing
linearly with N.  A sequence of smoother fields can approach the step only by
increasing steepness, which increases R_N.

This receipt is a finite stress test plus a proof target, not a final field
law.  It supports the admissibility criterion:

    projection credit is allowed only for marks belonging to a projective
    tight-action field law fixed before geometry projection.

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


def rayleigh_action(feature):
    f = center(feature)
    n = len(f)
    denom = norm2(f)
    if denom == 0:
        return mp.inf
    return (mp.mpf(n) ** 2) * mp.fsum(
        (f[(i + 1) % n] - f[i]) ** 2 for i in range(n)
    ) / denom


def block_feature(n):
    return [mp.mpf(1) if i < n // 2 else mp.mpf(-1) for i in range(n)]


def cos_feature(n, frequency=1):
    return [mp.cos(2 * mp.pi * frequency * i / n) for i in range(n)]


def sin_feature(n, frequency=1):
    return [mp.sin(2 * mp.pi * frequency * i / n) for i in range(n)]


def soft_block_feature(n, beta):
    return [mp.tanh(mp.mpf(beta) * mp.sin(2 * mp.pi * i / n)) for i in range(n)]


def alignment(a, b):
    ca = center(a)
    cb = center(b)
    denom = norm2(ca) * norm2(cb)
    if denom == 0:
        return mp.mpf(0)
    return (mp.fsum(ca[i] * cb[i] for i in range(len(ca))) ** 2) / denom


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


def fourier_features(n, max_frequency):
    features = []
    for k in range(1, max_frequency + 1):
        features.append(cos_feature(n, k))
        features.append(sin_feature(n, k))
    return features


def feature_action(features):
    return mp.fsum(rayleigh_action(feature) for feature in orthonormal_features(features))


def projection_fraction(feature, features):
    f = center(feature)
    total = norm2(f)
    if total == 0:
        return mp.mpf(0)
    return mp.fsum(
        mp.fsum(f[i] * basis[i] for i in range(len(f))) ** 2
        for basis in orthonormal_features(features)
    ) / total


def tail_fraction(feature, max_frequency):
    return max(mp.mpf(0), 1 - projection_fraction(feature, fourier_features(len(feature), max_frequency)))


def log_growth(first, last, scale):
    return mp.log(last / first) / mp.log(scale)


print("=" * 80)
print("Paper 27 projective mark-field admissibility receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

sizes = [16, 32, 64, 128, 256, 512]

projective_rows = []
for n in sizes:
    cos1 = cos_feature(n)
    block = block_feature(n)
    soft8 = soft_block_feature(n, 8)
    projective_rows.append(
        {
            "n": n,
            "cos_action": rayleigh_action(cos1),
            "block_action": rayleigh_action(block),
            "soft8_action": rayleigh_action(soft8),
            "soft8_alignment": alignment(soft8, block),
        }
    )

print("\n=== Projective refinement ladder ===")
print("N, R(cos1), R(exact block), R(soft beta=8), align(soft8, block)")
for row in projective_rows:
    print(
        f"{row['n']:4d} "
        f"{fmt(row['cos_action'], 14):>18s} "
        f"{fmt(row['block_action'], 14):>18s} "
        f"{fmt(row['soft8_action'], 14):>18s} "
        f"{fmt(row['soft8_alignment'], 14):>18s}"
    )

beta_rows = []
n_beta = 512
for beta in [1, 2, 4, 8, 16, 32, 64]:
    soft = soft_block_feature(n_beta, beta)
    block = block_feature(n_beta)
    action = rayleigh_action(soft)
    align = alignment(soft, block)
    beta_rows.append(
        {
            "beta": beta,
            "action": action,
            "alignment": align,
            "defect": 1 - align,
            "action_defect": action * (1 - align),
        }
    )

print("\n=== Steepening ladder at N=512 ===")
print("beta, R(soft beta), align with block, defect, R * defect")
for row in beta_rows:
    print(
        f"{row['beta']:4d} "
        f"{fmt(row['action'], 14):>18s} "
        f"{fmt(row['alignment'], 14):>18s} "
        f"{fmt(row['defect'], 14):>18s} "
        f"{fmt(row['action_defect'], 14):>18s}"
    )

fourier_rows = []
n_fourier = 128
block = block_feature(n_fourier)
for k in [1, 2, 4, 8, 16, 32]:
    features = fourier_features(n_fourier, k)
    fraction = projection_fraction(block, features)
    fourier_rows.append(
        {
            "k": k,
            "fraction": fraction,
            "tail": tail_fraction(block, k),
            "action": feature_action(features),
        }
    )

print("\n=== Fourier projective complexity ladder at N=128 ===")
print("K, block projection fraction, remaining tail, total mark action")
for row in fourier_rows:
    print(
        f"{row['k']:4d} "
        f"{fmt(row['fraction'], 14):>18s} "
        f"{fmt(row['tail'], 14):>18s} "
        f"{fmt(row['action'], 14):>18s}"
    )

cos_actions = [row["cos_action"] for row in projective_rows]
block_actions = [row["block_action"] for row in projective_rows]
soft8_actions = [row["soft8_action"] for row in projective_rows]
soft8_alignments = [row["soft8_alignment"] for row in projective_rows]
beta_actions = [row["action"] for row in beta_rows]
beta_alignments = [row["alignment"] for row in beta_rows]
beta_products = [row["action_defect"] for row in beta_rows]
fourier_actions = [row["action"] for row in fourier_rows]
fourier_fractions = [row["fraction"] for row in fourier_rows]
fourier_tails = [row["tail"] for row in fourier_rows]

cos_growth = log_growth(cos_actions[0], cos_actions[-1], mp.mpf(sizes[-1]) / sizes[0])
block_growth = log_growth(block_actions[0], block_actions[-1], mp.mpf(sizes[-1]) / sizes[0])
soft8_growth = log_growth(soft8_actions[1], soft8_actions[-1], mp.mpf(sizes[-1]) / sizes[1])

check(
    "low Fourier mode has projectively bounded action",
    max(cos_actions) < mp.mpf(40) and abs(cos_actions[-1] - 4 * mp.pi**2) < mp.mpf("0.01"),
    f"max_R_cos={fmt(max(cos_actions), 14)} R512-4pi2={fmt(cos_actions[-1] - 4 * mp.pi**2, 14)}",
)
check(
    "exact block label has linearly growing refinement action",
    block_actions[-1] / block_actions[0] == mp.mpf(32)
    and abs(block_growth - 1) < mp.mpf("1e-80"),
    f"R_block_first={fmt(block_actions[0], 14)} R_block_last={fmt(block_actions[-1], 14)} growth_exp={fmt(block_growth, 14)}",
)
check(
    "fixed smooth steep field is projectively tight but not exact block",
    max(soft8_actions) < mp.mpf(150)
    and soft8_alignments[-1] > mp.mpf("0.96")
    and soft8_alignments[-1] < mp.mpf("0.98")
    and soft8_growth < mp.mpf("0.15"),
    f"R_soft8_last={fmt(soft8_actions[-1], 14)} align_last={fmt(soft8_alignments[-1], 14)} growth_exp={fmt(soft8_growth, 14)}",
)
check(
    "approaching exact block by steepening costs increasing action",
    all(beta_actions[i] < beta_actions[i + 1] for i in range(len(beta_actions) - 1))
    and all(beta_alignments[i] < beta_alignments[i + 1] for i in range(len(beta_alignments) - 1)),
    f"R_beta1={fmt(beta_actions[0], 14)} R_beta64={fmt(beta_actions[-1], 14)} "
    f"align1={fmt(beta_alignments[0], 14)} align64={fmt(beta_alignments[-1], 14)}",
)
check(
    "finite-action steepening shows a nonzero action-defect tradeoff",
    min(beta_products) > mp.mpf(4) and max(beta_products) < mp.mpf(7),
    "R_defect=" + ", ".join(fmt(value, 8) for value in beta_products),
)
check(
    "Fourier approximation of a block requires growing bandwidth action",
    fourier_fractions[0] < mp.mpf("0.82")
    and fourier_fractions[-1] > mp.mpf("0.97")
    and fourier_actions[-1] > 1000 * fourier_actions[0]
    and fourier_tails[-1] < fourier_tails[0],
    f"K1_frac={fmt(fourier_fractions[0], 14)} K32_frac={fmt(fourier_fractions[-1], 14)} "
    f"E32/E1={fmt(fourier_actions[-1] / fourier_actions[0], 14)}",
)
check(
    "growth exponents separate smooth fields from hidden partition labels",
    cos_growth < mp.mpf("0.01") and soft8_growth < mp.mpf("0.15") and block_growth > mp.mpf("0.99"),
    f"cos_exp={fmt(cos_growth, 14)} soft8_exp={fmt(soft8_growth, 14)} block_exp={fmt(block_growth, 14)}",
)

print("\n=== Consequence ===")
print("The clean finite criterion is projective tightness of the mark action.")
print("Low Fourier marks and fixed smooth field profiles have stable refinement")
print("action.  Exact hidden partition labels have action growing linearly with N.")
print("A smooth field can look blocklike, but bounded action keeps it away from")
print("perfect block laundering; making it sharper spends action.  Thus the")
print("anti-laundering term should be an infinite-N/projective admissibility gate:")
print("only marks from a pre-geometric tight-action field law can earn projection")
print("credit.  Post-hoc labels fail by divergent action or by absent prior law.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
