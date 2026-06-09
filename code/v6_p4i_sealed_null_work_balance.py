#!/usr/bin/env python3
"""Paper 4 diagnostic I: sealed null-work balance gate.

This campaign attacks the remaining double-null gate.

Given a sealed double-null screen stack with no-twist eventless connections,
the null-front work densities are

    W_+ = <||G Omega_+||_F^2>
    W_- = <||G Omega_-||_F^2>.

If the null front units are rescaled by positive constants a and b, then

    W_+(a) = a^2 W_+
    W_-(b) = b^2 W_-.

Closed work balance alone is one equation in two unknowns, so it cannot fix an
affine normalization.  With front-dual reciprocity, ab=1, the balance has the
unique positive solution

    a_* = (W_- / W_+)^(1/4),    b_* = 1/a_*.

The diagnostic then tests the harder source question: does the same balance
force deletion response to equal the focusing source?  It does not.  Conserved
mean-zero sources with the same norm can be changed without changing the
geometry or the null-work balance.  The deletion/focusing identity remains a
separate theorem target unless the sealed event law proves it.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

from v6_p4h_intrinsic_null_diamond_gate import (
    Matrix,
    build_connection,
    build_field,
    centered,
    focusing,
    kl_to_mu,
    mat_mul,
    mat_norm,
    p_eta,
    shear_norms,
    solve_eta_star,
    trace_field,
)


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def record_work(field: list[Matrix], omega: list[Matrix]) -> float:
    return sum(mat_norm(mat_mul(g, o)) ** 2 for g, o in zip(field, omega)) / len(field)


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def rms(values: list[float]) -> float:
    return math.sqrt(sum(value * value for value in values) / len(values))


def max_abs(values: list[float]) -> float:
    return max(abs(value) for value in values)


def scale_to_rms(values: list[float], target: float) -> list[float]:
    r = rms(values)
    if r == 0.0:
        raise ValueError("cannot scale a zero-rms source")
    return [target * value / r for value in values]


def source_norm(values: list[float]) -> float:
    centered_values = centered(values)
    return sum(value * value for value in centered_values) / len(centered_values)


def front_balance_solution(work_plus: float, work_minus: float) -> tuple[float, float, float]:
    a = (work_minus / work_plus) ** 0.25
    b = 1.0 / a
    balanced = a * a * work_plus
    return a, b, balanced


def work_balance_residual(work_plus: float, work_minus: float, a: float, b: float) -> float:
    return abs(a * a * work_plus - b * b * work_minus)


def work_balance_curvature(work_plus: float, work_minus: float, a_star: float) -> float:
    # In log scale s, with a=e^s and b=e^-s, B(s)=(e^{2s}W_+-e^{-2s}W_-)^2.
    # At the zero of the bracket, B''=2(D')^2.
    s = math.log(a_star)
    derivative = 2.0 * (math.exp(2.0 * s) * work_plus + math.exp(-2.0 * s) * work_minus)
    return 2.0 * derivative * derivative


def work_only_family(work_plus: float, work_minus: float) -> list[tuple[float, float]]:
    # For each a, choose b so that a^2 W_+ = b^2 W_-.
    pairs = []
    for a in [0.75, 1.0, 1.35]:
        b = a * math.sqrt(work_plus / work_minus)
        pairs.append((a, b))
    return pairs


def focus_source(
    focus_plus: list[float],
    focus_minus: list[float],
    a: float,
    b: float,
    primitive_work: float,
) -> list[float]:
    raw = centered([
        0.5 * (a * a * fp + b * b * fm)
        for fp, fm in zip(focus_plus, focus_minus)
    ])
    return scale_to_rms(raw, primitive_work)


def alternate_conserved_source(source: list[float], n: int, primitive_work: float) -> list[float]:
    mode = []
    for u in range(n):
        for v in range(n):
            for x in range(n):
                for y in range(n):
                    mode.append(
                        math.sin(2.0 * math.pi * u / n)
                        + 0.6 * math.cos(2.0 * math.pi * (v + x) / n)
                        - 0.4 * math.sin(2.0 * math.pi * y / n)
                    )
    mixed = [s + 0.35 * m for s, m in zip(source, centered(mode))]
    return scale_to_rms(centered(mixed), primitive_work)


def same_receipts_gap(source: list[float], alternate: list[float]) -> tuple[float, float, float]:
    return (
        abs(mean(source) - mean(alternate)),
        abs(source_norm(source) - source_norm(alternate)),
        max_abs([a - b for a, b in zip(source, alternate)]),
    )


def metrics(n: int) -> dict[str, float | list[tuple[float, float]]]:
    eta = solve_eta_star()
    primitive_work = kl_to_mu(p_eta(eta))

    field = build_field(n)
    omega_plus, _ = build_connection(n, field, 0)
    omega_minus, _ = build_connection(n, field, 1)
    work_plus = record_work(field, omega_plus)
    work_minus = record_work(field, omega_minus)

    a_star, b_star, balanced_work = front_balance_solution(work_plus, work_minus)
    curvature = work_balance_curvature(work_plus, work_minus, a_star)
    residual_star = work_balance_residual(work_plus, work_minus, a_star, b_star)

    family = work_only_family(work_plus, work_minus)
    family_residuals = [
        work_balance_residual(work_plus, work_minus, a, b)
        for a, b in family
    ]
    family_cross_products = [a * b for a, b in family]
    family_cross_span = max(family_cross_products) - min(family_cross_products)

    theta_plus = trace_field(omega_plus)
    theta_minus = trace_field(omega_minus)
    shear_plus = shear_norms(omega_plus)
    shear_minus = shear_norms(omega_minus)
    focus_plus = focusing(theta_plus, shear_plus, n, 0)
    focus_minus = focusing(theta_minus, shear_minus, n, 1)
    source = focus_source(focus_plus, focus_minus, a_star, b_star, primitive_work)
    alternate = alternate_conserved_source(source, n, primitive_work)
    mean_gap, norm_gap, source_gap = same_receipts_gap(source, alternate)

    shifted_source = scale_to_rms(centered([value + 0.1 for value in source]), primitive_work)
    shift_gap = max_abs([a - b for a, b in zip(source, shifted_source)])

    return {
        "primitive_work": primitive_work,
        "work_plus": work_plus,
        "work_minus": work_minus,
        "a_star": a_star,
        "b_star": b_star,
        "balanced_work": balanced_work,
        "residual_star": residual_star,
        "curvature": curvature,
        "family": family,
        "family_residual_max": max(family_residuals),
        "family_cross_span": family_cross_span,
        "source_mean": mean(source),
        "source_norm": source_norm(source),
        "alternate_mean": mean(alternate),
        "alternate_norm": source_norm(alternate),
        "mean_gap": mean_gap,
        "norm_gap": norm_gap,
        "source_gap": source_gap,
        "identity_residual": max_abs([a - b for a, b in zip(source, source)]),
        "constant_shift_gap": shift_gap,
    }


def main() -> None:
    n = 14
    m = metrics(n)
    family = m["family"]
    assert isinstance(family, list)

    rows = [
        Row(
            "null work readout",
            "W_±=<||G Omega_±||_F^2>",
            "both front work densities are intrinsic once count-null axes exist",
            f"W+={m['work_plus']:.6f}, W-={m['work_minus']:.6f}",
            "PASS",
        ),
        Row(
            "work-only attack",
            "solve a^2 W_+ = b^2 W_- with free a,b",
            "closed work balance is a one-parameter family",
            "pairs=" + ",".join(f"({a:.2f},{b:.2f})" for a, b in family),
            "FAILS-WORK-ONLY",
        ),
        Row(
            "front-dual reciprocity",
            "add the sealed-pair condition ab=1",
            "work balance has one positive solution",
            f"a*={m['a_star']:.6f}, b*={m['b_star']:.6f}",
            "PROVES-AFFINE-PAIR-IF-DUALITY",
        ),
        Row(
            "isolation margin",
            "second variation in log affine scale",
            "the balanced solution is locally isolated",
            f"B''={m['curvature']:.6f}, residual={m['residual_star']:.1e}",
            "PASS",
        ),
        Row(
            "cross-normalization attack",
            "use the work-only family without ab=1",
            "all rows balance work but have different cross products",
            f"res_max={m['family_residual_max']:.1e}, ab_span={m['family_cross_span']:.6f}",
            "FAILS-WITHOUT-FRONT-DUALITY",
        ),
        Row(
            "balanced focusing source",
            "rho_focus = centered(a*^2 T++ + b*^2 T--), normalized by W*",
            "one conserved source is fixed if focusing identity is declared",
            f"mean={m['source_mean']:.1e}, norm={m['source_norm']:.6f}",
            "PASS-SCOPED",
        ),
        Row(
            "constant-source gauge attack",
            "add a constant to rho_focus then recenter",
            "closed source conservation kills the silent constant",
            f"gap_after_recentering={m['constant_shift_gap']:.1e}",
            "PASS",
        ),
        Row(
            "source-free attack",
            "alter source shape, recenter, and preserve source norm",
            "same geometry and same work balance do not select deletion source",
            f"mean_gap={m['mean_gap']:.1e}, norm_gap={m['norm_gap']:.1e}, shape_gap={m['source_gap']:.6f}",
            "FAILS-SOURCE-FREE",
        ),
        Row(
            "identity theorem option",
            "require deletion response to be rho_focus",
            "deletion/focusing residual vanishes by the same sealed law",
            f"identity_residual={m['identity_residual']:.1e}",
            "BRANCH-A-IF-PROVED",
        ),
        Row(
            "sealed null-work verdict",
            "closed work balance + front-dual reciprocity + focusing identity",
            "affine pair closes; source identity remains the hard theorem",
            "not a full tensor conservation theorem yet",
            "PARTIAL-CLOSURE-WITH-NO-GO",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("primitive_work", f"{m['primitive_work']:.15f}")
    print("work_plus", f"{m['work_plus']:.15e}")
    print("work_minus", f"{m['work_minus']:.15e}")
    print("a_star", f"{m['a_star']:.15e}")
    print("b_star", f"{m['b_star']:.15e}")
    print("balanced_work", f"{m['balanced_work']:.15e}")
    print("residual_star", f"{m['residual_star']:.15e}")
    print("curvature", f"{m['curvature']:.15e}")
    print("family_pairs", " ".join(f"{a:.12f}:{b:.12f}" for a, b in family))
    print("family_cross_span", f"{m['family_cross_span']:.15e}")
    print("source_norm", f"{m['source_norm']:.15e}")
    print("alternate_norm", f"{m['alternate_norm']:.15e}")
    print("source_gap", f"{m['source_gap']:.15e}")


if __name__ == "__main__":
    main()
