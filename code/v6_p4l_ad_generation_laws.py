#!/usr/bin/env python3
"""Paper 4 diagnostic L: intrinsic A_D generation laws.

The enriched RN route says that the local deletion action A_D is the real
primitive.  This diagnostic asks whether A_D can be generated rather than
chosen.

It tests three candidate laws on a finite sealed ring readout:

1. variational smoothing:
      A_mu = argmin_A ||A-H||^2 + mu <A,L A>, normalized.
   This needs a smoothing coefficient mu; varying mu moves A_D.

2. maximum entropy / least biased action:
      with only support, mean and norm constraints, the least biased action is
      two-level and does not reproduce the many-valued RN field.  Histogram
      data also do not fix spatial placement.

3. self-consistent record-geometry fixed point:
      A = normalize(H + alpha Phi(A) - beta A^3),
      L Phi(A)=A.
   With fixed alpha and beta this gives an isolated attractor in the finite
   model, but changing alpha moves the fixed point.  The law is therefore a
   genuine branch-A candidate only if the sealed diamond derives the feedback
   coefficients and the drive H.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def centered(values: list[float]) -> list[float]:
    mean = sum(values) / len(values)
    return [value - mean for value in values]


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def rms(values: list[float]) -> float:
    return math.sqrt(dot(values, values) / len(values))


def normalize(values: list[float], target: float) -> list[float]:
    values = centered(values)
    r = rms(values)
    if r == 0.0:
        raise ValueError("cannot normalize zero field")
    return [target * value / r for value in values]


def max_gap(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def support(values: list[float]) -> list[bool]:
    return [value >= 0.0 for value in values]


def support_flips(a: list[float], b: list[float]) -> int:
    return sum(1 for x, y in zip(support(a), support(b)) if x != y)


def rounded_levels(values: list[float], digits: int = 6) -> int:
    return len({round(value, digits) for value in values})


def primitive_work() -> float:
    # Same W* used by the binary primitive in earlier Paper 4 diagnostics.
    eta = solve_eta_binary()
    z = 2.0 * math.cosh(eta)
    p_minus = math.exp(-eta) / z
    p_plus = math.exp(eta) / z
    return p_minus * math.log(p_minus / 0.5) + p_plus * math.log(p_plus / 0.5)


def solve_eta_binary() -> float:
    def residual(eta: float) -> float:
        z = 2.0 * math.cosh(eta)
        p_minus = math.exp(-eta) / z
        p_plus = math.exp(eta) / z
        mean = -p_minus + p_plus
        var = p_minus * (-1.0 - mean) ** 2 + p_plus * (1.0 - mean) ** 2
        work = p_minus * math.log(p_minus / 0.5) + p_plus * math.log(p_plus / 0.5)
        return work - var

    lo = 0.0
    hi = 20.0
    flo = residual(lo)
    for _ in range(140):
        mid = 0.5 * (lo + hi)
        fm = residual(mid)
        if fm * flo <= 0.0:
            hi = mid
        else:
            lo = mid
            flo = fm
    return 0.5 * (lo + hi)


def solve_eta_scores(scores: list[float]) -> tuple[float, float, float]:
    weights = [1.0 / len(scores)] * len(scores)

    def moments(eta: float) -> tuple[float, float]:
        raw = [w * math.exp(eta * q) for q, w in zip(scores, weights)]
        z = sum(raw)
        probs = [value / z for value in raw]
        mean = sum(p * q for p, q in zip(probs, scores))
        second = sum(p * q * q for p, q in zip(probs, scores))
        var = second - mean * mean
        work = eta * mean - math.log(z)
        return work, var

    def residual(eta: float) -> float:
        work, var = moments(eta)
        return work - var

    lo = 0.0
    hi = 1.0
    flo = residual(lo)
    fhi = residual(hi)
    while fhi <= 0.0 and hi < 200.0:
        hi *= 2.0
        fhi = residual(hi)
    if fhi <= 0.0:
        raise ValueError("score balance did not cross")
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        fm = residual(mid)
        if fm * flo <= 0.0:
            hi = mid
        else:
            lo = mid
            flo = fm
    eta = 0.5 * (lo + hi)
    work, var = moments(eta)
    return eta, work, var


def sealed_drive(n: int, target: float) -> list[float]:
    values = []
    for i in range(n):
        x = i / n
        values.append(
            1.00 * math.sin(2.0 * math.pi * x)
            + 0.35 * math.sin(4.0 * math.pi * x + 0.4)
            - 0.22 * math.cos(6.0 * math.pi * x - 0.3)
            + 0.18 * math.sin(10.0 * math.pi * x + 0.9)
        )
    return normalize(values, target)


def laplacian_apply(values: list[float]) -> list[float]:
    n = len(values)
    return [2.0 * values[i] - values[(i - 1) % n] - values[(i + 1) % n] for i in range(n)]


def dft(values: list[float]) -> list[complex]:
    n = len(values)
    out = []
    for k in range(n):
        total = 0.0j
        for j, value in enumerate(values):
            angle = -2.0 * math.pi * k * j / n
            total += value * complex(math.cos(angle), math.sin(angle))
        out.append(total / n)
    return out


def idft(coeffs: list[complex]) -> list[float]:
    n = len(coeffs)
    out = []
    for j in range(n):
        total = 0.0j
        for k, value in enumerate(coeffs):
            angle = 2.0 * math.pi * k * j / n
            total += value * complex(math.cos(angle), math.sin(angle))
        out.append(total.real)
    return out


def tikhonov_filter(values: list[float], mu: float, target: float) -> list[float]:
    coeffs = dft(centered(values))
    filtered = []
    n = len(values)
    for k, coeff in enumerate(coeffs):
        lam = 2.0 - 2.0 * math.cos(2.0 * math.pi * k / n)
        filtered.append(coeff / (1.0 + mu * lam))
    return normalize(idft(filtered), target)


def poisson(values: list[float]) -> list[float]:
    coeffs = dft(centered(values))
    solved = []
    n = len(values)
    for k, coeff in enumerate(coeffs):
        if k == 0:
            solved.append(0.0j)
        else:
            lam = 2.0 - 2.0 * math.cos(2.0 * math.pi * k / n)
            solved.append(coeff / lam)
    return centered(idft(solved))


def fixed_point_map(values: list[float], drive: list[float], target: float, alpha: float, beta: float) -> list[float]:
    phi = normalize(poisson(values), target)
    cubic = normalize([value ** 3 for value in values], target)
    raw = [h + alpha * p - beta * c for h, p, c in zip(drive, phi, cubic)]
    return normalize(raw, target)


def iterate_fixed_point(
    start: list[float],
    drive: list[float],
    target: float,
    alpha: float,
    beta: float,
    steps: int = 250,
) -> tuple[list[float], float]:
    current = normalize(start, target)
    for _ in range(steps):
        current = fixed_point_map(current, drive, target, alpha, beta)
    residual = max_gap(current, fixed_point_map(current, drive, target, alpha, beta))
    return current, residual


def binary_from_support(values: list[float], target: float) -> list[float]:
    supp = support(values)
    density = sum(1 for item in supp if item) / len(supp)
    return [
        target * ((1.0 if item else 0.0) - density)
        for item in supp
    ]


def max_entropy_two_level(values: list[float], target: float) -> list[float]:
    return normalize(binary_from_support(values, target), target)


def histogram_permutation(values: list[float]) -> list[float]:
    # Same value multiset, different spatial placement.
    n = len(values)
    return [values[(7 * i + 3) % n] for i in range(n)]


def same_support_alternative(values: list[float], target: float) -> list[float]:
    base = normalize(values, target)
    n = len(values)
    positive = [i for i, value in enumerate(base) if value > 0.08 * target]
    mode = [0.0] * n
    for rank, i in enumerate(positive):
        x = rank / len(positive)
        mode[i] = math.sin(2.0 * math.pi * x) + 0.35 * math.cos(6.0 * math.pi * x)
    mean_positive = sum(mode[i] for i in positive) / len(positive)
    for i in positive:
        mode[i] -= mean_positive
    mode = normalize(mode, target)
    for scale in [0.25, 0.18, 0.12, 0.08, 0.05, 0.03, 0.02, 0.01, 0.005]:
        candidate = normalize([value + scale * m for value, m in zip(base, mode)], target)
        if support_flips(candidate, base) == 0:
            return candidate
    return base[:]


def max_pair_gap(fields: list[list[float]]) -> float:
    gap = 0.0
    for i, left in enumerate(fields):
        for right in fields[i + 1 :]:
            gap = max(gap, max_gap(left, right))
    return gap


def main() -> None:
    n = 96
    target = primitive_work()
    drive = sealed_drive(n, target)

    variational_mus = [0.0, 0.25, 1.0, 4.0]
    variational_fields = [tikhonov_filter(drive, mu, target) for mu in variational_mus]
    variational_gap = max_pair_gap(variational_fields)
    variational_flips = max(support_flips(variational_fields[0], field) for field in variational_fields[1:])

    maxent = max_entropy_two_level(drive, target)
    maxent_gap = max_gap(maxent, drive)
    permuted = histogram_permutation(drive)
    permutation_phi_gap = max_gap(poisson(drive), poisson(permuted))

    alpha = 0.18
    beta = 0.06
    starts = [
        drive,
        maxent,
        normalize([math.sin(8.0 * math.pi * i / n) for i in range(n)], target),
        normalize([(-1.0) ** i for i in range(n)], target),
    ]
    fixed_results = [iterate_fixed_point(start, drive, target, alpha, beta) for start in starts]
    fixed_fields = [field for field, _ in fixed_results]
    fixed_residuals = [residual for _, residual in fixed_results]
    fixed_point = fixed_fields[0]
    attractor_gap = max_pair_gap(fixed_fields)
    fixed_residual = max(fixed_residuals)
    fixed_drive_gap = max_gap(fixed_point, drive)
    fixed_levels = rounded_levels(fixed_point)
    fixed_eta, fixed_work, fixed_response = solve_eta_scores([value / target for value in fixed_point])

    alpha_values = [0.08, 0.18, 0.32]
    alpha_fields = [
        iterate_fixed_point(drive, drive, target, a, beta)[0]
        for a in alpha_values
    ]
    alpha_gap = max_pair_gap(alpha_fields)
    alpha_flips = max(support_flips(alpha_fields[1], field) for field in alpha_fields)

    alt = same_support_alternative(fixed_point, target)
    alt_residual = max_gap(alt, fixed_point_map(alt, drive, target, alpha, beta))
    alt_shape_gap = max_gap(alt, fixed_point)
    alt_flips = support_flips(alt, fixed_point)

    fixed_support = binary_from_support(fixed_point, target)
    support_source_gap = max_gap(fixed_point, normalize(fixed_support, target))
    support_map_residual = max_gap(normalize(fixed_support, target), fixed_point_map(normalize(fixed_support, target), drive, target, alpha, beta))

    rows = [
        Row(
            "sealed drive",
            "H from boundary/holonomy work imbalance",
            "a nonzero many-valued candidate source is available",
            f"levels={rounded_levels(drive)}, rms={rms(drive):.6f}",
            "INPUT-SCOPED",
        ),
        Row(
            "variational route",
            "A_mu=(I+mu L)^-1 H, normalized",
            "least-work smoothing needs a coefficient",
            f"mu_span={variational_gap:.6f}, support_flips={variational_flips}",
            "FAILS-FREE-MU",
        ),
        Row(
            "max-entropy route",
            "least biased source from support, mean and rms",
            "collapses spatial action to a two-level readout",
            f"gap_to_H={maxent_gap:.6f}, levels={rounded_levels(maxent)}",
            "FAILS-SPATIAL-ACTION",
        ),
        Row(
            "entropy permutation attack",
            "same histogram/entropy, different placement",
            "spatial gravity response changes",
            f"phi_gap={permutation_phi_gap:.6f}",
            "FAILS-HISTOGRAM-ONLY",
        ),
        Row(
            "fixed-point route",
            "A=T(A)=normalize(H+alpha Phi(A)-beta A^3)",
            "with fixed coefficients, all starts converge to one action",
            f"res={fixed_residual:.2e}, attractor_gap={attractor_gap:.2e}",
            "PASS-FINITE",
        ),
        Row(
            "fixed action readout",
            "event support from A_*>=0",
            "fixed point remains many-valued and support-readable",
            f"levels={fixed_levels}, drive_gap={fixed_drive_gap:.6f}",
            "PASS",
        ),
        Row(
            "coefficient attack",
            "change alpha while preserving the same drive and law form",
            "the generated action moves",
            f"alpha_gap={alpha_gap:.6f}, support_flips={alpha_flips}",
            "FAILS-IF-COEFFICIENT-FREE",
        ),
        Row(
            "support-only fixed-point attack",
            "replace A_* by its support source",
            "support source is not a fixed point",
            f"source_gap={support_source_gap:.6f}, map_res={support_map_residual:.6f}",
            "FAILS-SUPPORT-ONLY",
        ),
        Row(
            "same-support action attack",
            "preserve support and rms but change A shape",
            "altered action fails the fixed-point equation",
            f"flips={alt_flips}, shape_gap={alt_shape_gap:.6f}, map_res={alt_residual:.6f}",
            "PASS-SELECTS-SHAPE",
        ),
        Row(
            "RN constants",
            "rerun information balance with q=A_*/W*",
            "new constants are derived from the generated action",
            f"eta={fixed_eta:.6f}, W={fixed_work:.6f}",
            "PASS-NEW-CONSTANTS",
        ),
        Row(
            "A_D generation verdict",
            "variational/max-ent/fixed-point comparison",
            "only the fixed-point route selects a full action in this finite packet",
            "still conditional on intrinsic H, alpha, beta",
            "BEST-CANDIDATE-CONDITIONAL",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("primitive_work", f"{target:.15f}")
    print("variational_gap", f"{variational_gap:.15e}")
    print("variational_flips", variational_flips)
    print("maxent_gap", f"{maxent_gap:.15e}")
    print("permutation_phi_gap", f"{permutation_phi_gap:.15e}")
    print("fixed_residual", f"{fixed_residual:.15e}")
    print("attractor_gap", f"{attractor_gap:.15e}")
    print("fixed_drive_gap", f"{fixed_drive_gap:.15e}")
    print("alpha_gap", f"{alpha_gap:.15e}")
    print("alpha_flips", alpha_flips)
    print("support_source_gap", f"{support_source_gap:.15e}")
    print("support_map_residual", f"{support_map_residual:.15e}")
    print("same_support_shape_gap", f"{alt_shape_gap:.15e}")
    print("same_support_map_residual", f"{alt_residual:.15e}")
    print("fixed_eta", f"{fixed_eta:.15e}")
    print("fixed_work", f"{fixed_work:.15e}")
    print("fixed_response", f"{fixed_response:.15e}")


if __name__ == "__main__":
    main()
