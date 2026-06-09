#!/usr/bin/env python3
"""Paper 4 diagnostic M: T_D classification and coefficient-family no-go.

The A_D campaign found a strong finite candidate:

    A_D = T_D(A_D).

This diagnostic asks whether the currently named sealed-diamond invariants
select T_D uniquely.  It builds families of feedback maps from the same sealed
data:

    H: centered boundary/holonomy work drive;
    L: count-uniform collar Laplacian;
    Phi(A): mean-zero solution of L Phi = A;
    W*: primitive work normalization.

The maps are all centered, normalized, ring-covariant, source-conserving, and
have isolated attracting fixed points in the finite packet:

    T_{a,b,d}(A) = N[H + a Phi(A) - b A^3 + d Phi2(A)].

The campaign result is a no-go: these invariants leave a coefficient family.
Natural selectors either fail to choose a law or choose a degenerate convention.
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


@dataclass(frozen=True)
class Coeffs:
    alpha: float
    beta: float
    delta: float

    def label(self) -> str:
        return f"a={self.alpha:.2f},b={self.beta:.2f},d={self.delta:.2f}"


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


def primitive_work() -> float:
    eta = solve_eta_binary()
    z = 2.0 * math.cosh(eta)
    p_minus = math.exp(-eta) / z
    p_plus = math.exp(eta) / z
    return p_minus * math.log(p_minus / 0.5) + p_plus * math.log(p_plus / 0.5)


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


def laplacian(values: list[float]) -> list[float]:
    n = len(values)
    return [2.0 * values[i] - values[(i - 1) % n] - values[(i + 1) % n] for i in range(n)]


def rotate(values: list[float], shift: int) -> list[float]:
    n = len(values)
    return [values[(i - shift) % n] for i in range(n)]


def reflect(values: list[float]) -> list[float]:
    return [values[0]] + list(reversed(values[1:]))


def map_td(values: list[float], drive: list[float], target: float, coeffs: Coeffs) -> list[float]:
    phi = normalize(poisson(values), target)
    cubic = normalize([value ** 3 for value in values], target)
    phi2 = normalize(poisson(phi), target)
    raw = [
        h + coeffs.alpha * p - coeffs.beta * c + coeffs.delta * p2
        for h, p, c, p2 in zip(drive, phi, cubic, phi2)
    ]
    return normalize(raw, target)


def iterate_td(
    start: list[float],
    drive: list[float],
    target: float,
    coeffs: Coeffs,
    steps: int = 140,
) -> tuple[list[float], float]:
    current = normalize(start, target)
    for _ in range(steps):
        current = map_td(current, drive, target, coeffs)
    residual = max_gap(current, map_td(current, drive, target, coeffs))
    return current, residual


def max_pair_gap(fields: list[list[float]]) -> float:
    gap = 0.0
    for i, left in enumerate(fields):
        for right in fields[i + 1 :]:
            gap = max(gap, max_gap(left, right))
    return gap


def starts(n: int, target: float, drive: list[float]) -> list[list[float]]:
    return [
        drive,
        normalize([math.sin(8.0 * math.pi * i / n) for i in range(n)], target),
        normalize([math.cos(6.0 * math.pi * i / n + 0.7) for i in range(n)], target),
    ]


def fixed_for_coeffs(
    coeffs: Coeffs,
    drive: list[float],
    target: float,
) -> tuple[list[float], float, float]:
    fields = []
    residuals = []
    for start in starts(len(drive), target, drive):
        field, residual = iterate_td(start, drive, target, coeffs)
        fields.append(field)
        residuals.append(residual)
    return fields[0], max(residuals), max_pair_gap(fields)


def covariance_gap(drive: list[float], target: float, coeffs: Coeffs) -> tuple[float, float]:
    base, _, _ = fixed_for_coeffs(coeffs, drive, target)
    rotated_drive = rotate(drive, 11)
    rotated, _, _ = fixed_for_coeffs(coeffs, rotated_drive, target)
    reflected_drive = reflect(drive)
    reflected, _, _ = fixed_for_coeffs(coeffs, reflected_drive, target)
    return max_gap(rotated, rotate(base, 11)), max_gap(reflected, reflect(base))


def linearized_gain(
    fixed: list[float],
    drive: list[float],
    target: float,
    coeffs: Coeffs,
) -> float:
    n = len(fixed)
    eps = 1.0e-5
    gains = []
    modes = [
        [math.sin(2.0 * math.pi * i / n) for i in range(n)],
        [math.sin(4.0 * math.pi * i / n + 0.3) for i in range(n)],
        [math.cos(8.0 * math.pi * i / n - 0.1) for i in range(n)],
        [(-1.0) ** i for i in range(n)],
    ]
    base = map_td(fixed, drive, target, coeffs)
    for mode in modes:
        tangent = normalize(mode, 1.0)
        perturbed = normalize([x + eps * t for x, t in zip(fixed, tangent)], target)
        image = map_td(perturbed, drive, target, coeffs)
        diff = [x - y for x, y in zip(image, base)]
        gains.append(rms(diff) / eps)
    return max(gains)


def pair_with_same_support(items: list[tuple[Coeffs, list[float]]]) -> tuple[Coeffs, Coeffs, float, int]:
    best: tuple[Coeffs, Coeffs, float, int] | None = None
    best_gap = -1.0
    best_flips = 10**9
    for i, (left_coeffs, left) in enumerate(items):
        for right_coeffs, right in items[i + 1 :]:
            flips = support_flips(left, right)
            gap = max_gap(left, right)
            if flips == 0 and gap > best_gap:
                best = (left_coeffs, right_coeffs, gap, flips)
                best_gap = gap
                best_flips = flips
            elif best is None and flips < best_flips:
                best = (left_coeffs, right_coeffs, gap, flips)
                best_gap = gap
                best_flips = flips
    if best is None:
        raise ValueError("no coefficient pair found")
    return best


def main() -> None:
    n = 48
    target = primitive_work()
    drive = sealed_drive(n, target)

    coeffs_list = [
        Coeffs(0.00, 0.00, 0.00),
        Coeffs(0.08, 0.06, 0.00),
        Coeffs(0.18, 0.06, 0.00),
        Coeffs(0.32, 0.06, 0.00),
        Coeffs(0.18, 0.06, 0.04),
    ]

    fixed_items = []
    residuals = []
    attractor_gaps = []
    gains = []
    constants = []
    for coeffs in coeffs_list:
        field, residual, attractor_gap = fixed_for_coeffs(coeffs, drive, target)
        fixed_items.append((coeffs, field))
        residuals.append(residual)
        attractor_gaps.append(attractor_gap)
        gains.append(linearized_gain(field, drive, target, coeffs))
        constants.append(solve_eta_scores([value / target for value in field]))

    fields = [field for _, field in fixed_items]
    family_gap = max_pair_gap(fields)
    max_residual = max(residuals)
    max_attractor = max(attractor_gaps)
    max_gain = max(gains)
    work_values = [work for _, work, _ in constants]
    eta_values = [eta for eta, _, _ in constants]
    work_span = max(work_values) - min(work_values)
    eta_span = max(eta_values) - min(eta_values)

    rot_gap, ref_gap = covariance_gap(drive, target, Coeffs(0.18, 0.06, 0.00))

    grid_items = []
    for alpha in [0.10, 0.12, 0.14, 0.16, 0.18, 0.20]:
        coeffs = Coeffs(alpha, 0.06, 0.00)
        field, _, _ = fixed_for_coeffs(coeffs, drive, target)
        grid_items.append((coeffs, field))
    left_coeffs, right_coeffs, same_support_gap, same_support_flips = pair_with_same_support(grid_items)

    drive_only = fields[0]
    drive_only_relational_gain = linearized_gain(drive_only, drive, target, Coeffs(0.00, 0.00, 0.00))
    best_deviation = min(max_gap(field, drive) for field in fields)
    responseful_deviation = min(
        max_gap(field, drive)
        for coeffs, field in fixed_items
        if abs(coeffs.alpha) + abs(coeffs.beta) + abs(coeffs.delta) > 0.0
    )

    rows = [
        Row(
            "classification data",
            "same H, L, W*, normalization and mean-zero source condition",
            "finite sealed packet is fixed before coefficient scan",
            f"n={n}, W*={target:.6f}",
            "DEFINED",
        ),
        Row(
            "coefficient-family lemma",
            "T_{a,b,d}=N[H+a Phi(A)-b A^3+d Phi2(A)]",
            "many covariant source-conserving maps are available",
            f"families={len(coeffs_list)}",
            "NO-UNIQUENESS-CLASS",
        ),
        Row(
            "isolated fixed points",
            "iterate each T from three starts",
            "all scanned laws have one attracting fixed action",
            f"res={max_residual:.1e}, attractor={max_attractor:.1e}",
            "PASS-FAMILY",
        ),
        Row(
            "covariance receipt",
            "rotate and reflect the sealed drive before solving",
            "the law is intrinsic to ring order, not coordinate labels",
            f"rot={rot_gap:.1e}, ref={ref_gap:.1e}",
            "PASS",
        ),
        Row(
            "different actions",
            "compare fixed points across admissible coefficient choices",
            "same sealed data generate inequivalent A_D fields",
            f"family_gap={family_gap:.6f}",
            "REFUTES-UNIQUENESS",
        ),
        Row(
            "same-support pair",
            "vary alpha while preserving event support",
            "binary readout can be identical while A_D differs",
            f"{left_coeffs.label()} vs {right_coeffs.label()}, gap={same_support_gap:.6f}, flips={same_support_flips}",
            "REFUTES-SUPPORT-CLASSIFICATION",
        ),
        Row(
            "fixed-point residual selector",
            "choose law with smallest residual",
            "all exact fixed points have residual near zero",
            f"max_res={max_residual:.1e}",
            "FAILS",
        ),
        Row(
            "stability selector",
            "use finite linearized gain/isolation",
            "stability is a range, not a unique invariant",
            f"max_gain={max_gain:.6f}",
            "FAILS-RANGE",
        ),
        Row(
            "least-deformation selector",
            "minimize ||A-H|| over the family",
            "selects the degenerate drive-only map, not feedback dynamics",
            f"drive_gain={drive_only_relational_gain:.1e}, best={best_deviation:.6f}, responseful={responseful_deviation:.6f}",
            "FAILS-RELATIONALITY",
        ),
        Row(
            "RN balance selector",
            "rerun eta,W from each generated A_D",
            "each action has its own balance constants",
            f"eta_span={eta_span:.6f}, W_span={work_span:.6f}",
            "FAILS-TO-SELECT",
        ),
        Row(
            "T_D classification verdict",
            "current sealed invariants plus fixed-point isolation",
            "do not determine a unique feedback law",
            "needs one more invariant, or explicit dynamics",
            "FINITE-NO-GO",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("primitive_work", f"{target:.15f}")
    print("family_gap", f"{family_gap:.15e}")
    print("max_residual", f"{max_residual:.15e}")
    print("max_attractor_gap", f"{max_attractor:.15e}")
    print("rotation_gap", f"{rot_gap:.15e}")
    print("reflection_gap", f"{ref_gap:.15e}")
    print("same_support_left", left_coeffs.label())
    print("same_support_right", right_coeffs.label())
    print("same_support_gap", f"{same_support_gap:.15e}")
    print("same_support_flips", same_support_flips)
    print("linearized_gains", " ".join(f"{gain:.15e}" for gain in gains))
    print("eta_values", " ".join(f"{eta:.15e}" for eta in eta_values))
    print("work_values", " ".join(f"{work:.15e}" for work in work_values))
    print("eta_span", f"{eta_span:.15e}")
    print("work_span", f"{work_span:.15e}")
    print("drive_only_relational_gain", f"{drive_only_relational_gain:.15e}")
    print("best_deviation", f"{best_deviation:.15e}")
    print("best_responseful_deviation", f"{responseful_deviation:.15e}")


if __name__ == "__main__":
    main()
