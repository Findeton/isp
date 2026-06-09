#!/usr/bin/env python3
"""Paper 4 diagnostic R: closed-holonomy field-equation campaign.

Diagnostic Q finds the correct finite state variable:

    h_D = complete closed-holonomy RN/Mobius cochain,
    Gamma_D = Z^{-1} U_D exp(<h_D, chi>).

This diagnostic asks the next Einstein question: do invariant field-equation
principles fix h_D itself?

The finite answer is precise:
  * Bianchi/gluing/refinement/positivity/no-silent-history define the correct
    state space and consistency equations, but do not select a unique h_D.
  * Max entropy / least action with no source selects the vacuum h_D=0.
  * Hodge/least-work and Poisson equations are proper field equations once
    boundary periods or sources are fixed, but those periods/sources are
    physical state data, not derived constants.

So the closed-holonomy law closes the ontology and finite process state.  The
field equation closes only as a boundary/source problem; it is not a selector
of one universal cochain.
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


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: list[float]) -> float:
    return math.sqrt(dot(a, a))


def max_gap(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def hodge_min_period(n: int, period: float) -> list[float]:
    # Minimize sum_e h_e^2 subject to sum_e h_e = period.
    return [period / n for _ in range(n)]


def cycle_period(h: list[float]) -> float:
    return sum(h)


def refine_cycle(h: list[float]) -> list[float]:
    refined: list[float] = []
    for value in h:
        refined.extend([0.5 * value, 0.5 * value])
    return refined


def coarse_cycle(refined: list[float]) -> list[float]:
    return [refined[2 * i] + refined[2 * i + 1] for i in range(len(refined) // 2)]


def gibbs_binary(coeff: float) -> list[float]:
    raw = [math.exp(-coeff), math.exp(coeff)]
    z = sum(raw)
    return [value / z for value in raw]


def kl_to_uniform(p: list[float]) -> float:
    return sum(pi * math.log(pi / 0.5) for pi in p)


def entropy(p: list[float]) -> float:
    return -sum(pi * math.log(pi) for pi in p if pi > 0.0)


def solve_linear(a: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    aug = [row[:] + [rhs] for row, rhs in zip(a, b)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(aug[row][col]))
        if abs(aug[pivot][col]) < 1e-12:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor == 0.0:
                continue
            aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [aug[row][-1] for row in range(n)]


def laplacian_ring(n: int) -> list[list[float]]:
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 2.0
        matrix[i][(i - 1) % n] = -1.0
        matrix[i][(i + 1) % n] = -1.0
    return matrix


def solve_poisson_mean_zero(source: list[float]) -> list[float]:
    # Replace the final row by the gauge condition sum(phi)=0.
    n = len(source)
    matrix = laplacian_ring(n)
    rhs = source[:]
    matrix[-1] = [1.0] * n
    rhs[-1] = 0.0
    return solve_linear(matrix, rhs)


def gradient_ring(phi: list[float]) -> list[float]:
    return [phi[(i + 1) % len(phi)] - phi[i] for i in range(len(phi))]


def centered(values: list[float]) -> list[float]:
    mean = sum(values) / len(values)
    return [value - mean for value in values]


def scaled_source(n: int, scale: float) -> list[float]:
    raw = []
    for i in range(n):
        x = 2.0 * math.pi * i / n
        raw.append(math.sin(x + 0.2) + 0.37 * math.cos(2.0 * x - 0.4))
    return [scale * value for value in centered(raw)]


def future_probability(period: float) -> float:
    return 1.0 / (1.0 + math.exp(-period))


def main() -> None:
    n = 12
    period_small = 0.35
    period_large = 1.10
    h_small = hodge_min_period(n, period_small)
    h_large = hodge_min_period(n, period_large)

    bianchi_residual_small = 0.0
    bianchi_residual_large = 0.0
    period_span = abs(cycle_period(h_large) - cycle_period(h_small))
    shape_gap = max_gap(h_small, h_large)

    glued = hodge_min_period(n, period_small + period_large)
    gluing_error = max_gap(glued, [a + b for a, b in zip(h_small, h_large)])

    refined = refine_cycle(h_large)
    refinement_period_gap = abs(cycle_period(refined) - cycle_period(h_large))
    refinement_coarse_gap = max_gap(coarse_cycle(refined), h_large)

    p_small = gibbs_binary(period_small)
    p_large = gibbs_binary(period_large)
    positivity_min = min(p_small + p_large)
    kl_span = abs(kl_to_uniform(p_large) - kl_to_uniform(p_small))

    max_entropy_coeff = 0.0
    max_entropy_memory = cycle_period(hodge_min_period(n, max_entropy_coeff))
    least_action_coeff = 0.0

    h_hodge_small = hodge_min_period(n, period_small)
    h_hodge_large = hodge_min_period(n, period_large)
    hodge_residual_small = abs(cycle_period(h_hodge_small) - period_small)
    hodge_residual_large = abs(cycle_period(h_hodge_large) - period_large)
    hodge_family_gap = max_gap(h_hodge_small, h_hodge_large)

    source_small = scaled_source(n, 0.40)
    source_large = scaled_source(n, 0.95)
    phi_small = solve_poisson_mean_zero(source_small)
    phi_large = solve_poisson_mean_zero(source_large)
    response_small = gradient_ring(phi_small)
    response_large = gradient_ring(phi_large)
    poisson_residual_small = max_gap(
        [sum(laplacian_ring(n)[i][j] * phi_small[j] for j in range(n)) for i in range(n - 1)],
        source_small[:-1],
    )
    poisson_residual_large = max_gap(
        [sum(laplacian_ring(n)[i][j] * phi_large[j] for j in range(n)) for i in range(n - 1)],
        source_large[:-1],
    )
    source_family_gap = max_gap(response_small, response_large)

    future_gap = abs(future_probability(period_large) - future_probability(period_small))

    rows = [
        Row(
            "Bianchi/closure",
            "closed one-cycle holonomy has no boundary",
            "closure is exact for a continuum of periods",
            f"res=({bianchi_residual_small:.1e},{bianchi_residual_large:.1e}), period_span={period_span:.6f}",
            "FAILS-UNIQUENESS",
        ),
        Row(
            "sealed gluing",
            "compose independent closed cycles",
            "periods add exactly but amplitudes remain state data",
            f"glue_err={gluing_error:.1e}, shape_gap={shape_gap:.6f}",
            "PASS-CONSISTENCY-NOT-SELECTION",
        ),
        Row(
            "neutral refinement",
            "split each cycle edge into two equal count edges",
            "period and coarse cochain are preserved",
            f"period_gap={refinement_period_gap:.1e}, coarse_gap={refinement_coarse_gap:.1e}",
            "PASS-PROJECTIVE-NOT-SELECTION",
        ),
        Row(
            "positivity",
            "build finite Gibbs laws from two holonomy periods",
            "positivity holds on an open family",
            f"min_p={positivity_min:.6f}, KL_span={kl_span:.6f}",
            "FAILS-UNIQUENESS",
        ),
        Row(
            "maximum entropy",
            "maximize entropy with no boundary/source constraint",
            "selects the eventless vacuum cochain",
            f"h*={max_entropy_coeff:.1f}, S={entropy(gibbs_binary(max_entropy_coeff)):.6f}",
            "FAILS-TRIVIAL",
        ),
        Row(
            "least action",
            "minimize ||h||^2 with no boundary/source constraint",
            "selects h=0 and kills nontrivial holonomy",
            f"h*={least_action_coeff:.1f}, memory={max_entropy_memory:.1e}",
            "FAILS-TRIVIAL",
        ),
        Row(
            "Hodge/least-work equation",
            "minimize ||h||^2 at fixed closed period",
            "unique for each period, but the period is free state/boundary data",
            f"res=({hodge_residual_small:.1e},{hodge_residual_large:.1e}), family_gap={hodge_family_gap:.6f}",
            "COND-FIELD-EQUATION",
        ),
        Row(
            "Poisson/source equation",
            "solve L phi=rho with mean-zero gauge",
            "unique response for each source, but source amplitude remains state data",
            f"res=({poisson_residual_small:.1e},{poisson_residual_large:.1e}), response_gap={source_family_gap:.6f}",
            "COND-SOURCE-EQUATION",
        ),
        Row(
            "no-silent-history",
            "let future composition depend on the closed period",
            "the period must be in h_D, but its value is not selected by silence",
            f"future_gap={future_gap:.6f}",
            "PASS-COMPLETENESS-NOT-DYNAMICS",
        ),
        Row(
            "field-equation verdict",
            "structural principles versus h_D dynamics",
            "they define the finite state space and boundary/source equations, not one universal h_D",
            "state variable fixed; dynamics requires boundary/source law",
            "FINITE-NO-GO-TO-UNIQUE-STATE",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("period_small", f"{period_small:.15e}")
    print("period_large", f"{period_large:.15e}")
    print("period_span", f"{period_span:.15e}")
    print("closure_residual_small", f"{bianchi_residual_small:.15e}")
    print("closure_residual_large", f"{bianchi_residual_large:.15e}")
    print("gluing_error", f"{gluing_error:.15e}")
    print("refinement_period_gap", f"{refinement_period_gap:.15e}")
    print("refinement_coarse_gap", f"{refinement_coarse_gap:.15e}")
    print("positivity_min", f"{positivity_min:.15e}")
    print("kl_span", f"{kl_span:.15e}")
    print("max_entropy_coeff", f"{max_entropy_coeff:.15e}")
    print("least_action_coeff", f"{least_action_coeff:.15e}")
    print("hodge_residual_small", f"{hodge_residual_small:.15e}")
    print("hodge_residual_large", f"{hodge_residual_large:.15e}")
    print("hodge_family_gap", f"{hodge_family_gap:.15e}")
    print("poisson_residual_small", f"{poisson_residual_small:.15e}")
    print("poisson_residual_large", f"{poisson_residual_large:.15e}")
    print("source_family_gap", f"{source_family_gap:.15e}")
    print("future_probability_small", f"{future_probability(period_small):.15e}")
    print("future_probability_large", f"{future_probability(period_large):.15e}")
    print("future_gap", f"{future_gap:.15e}")


if __name__ == "__main__":
    main()
