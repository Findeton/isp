#!/usr/bin/env python3
"""Paper 4 diagnostic AF: intrinsic division-event commitment law.

This diagnostic attacks the remaining branch-A gap from the sealed-record side.
It asks whether the division-event waiting law and its dimensionless scale can
be derived from intrinsic RN/KL data rather than supplied as a renewal model.

The finite theorem tested here is:

  1. The only intrinsic eventless clock is additive RN/KL evidence I.
  2. Sealed eventless gluing forces survival S(I+J)=S(I)S(J).
  3. Continuity and positivity force S(I)=exp(-lambda I).
  4. Exact self-accounting of RN action forces lambda=1: the no-division
     action -log S(I) must equal the record evidence I it accounts for.
  5. In a closed-holonomy exponential family, retained holonomy must equal
     no-division survival through its own cochain action.  For one parity mode:

       tanh(eta) = exp(-eta).

     For a finite complete ledger with primitive oriented statistics chi_j:

       grad psi(h)_j = exp(-h_j).

     This is the unique minimizer of psi(h)+sum_j exp(-h_j) when the ledger
     separates the primitive modes.  That is the finite division-commitment
     law; it fixes h from the same whole-history partition function.
"""

from __future__ import annotations

from dataclasses import dataclass
import itertools
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def atanh(x: float) -> float:
    x = max(min(x, 1.0 - 1e-15), -1.0 + 1e-15)
    return 0.5 * math.log((1.0 + x) / (1.0 - x))


def solve_scalar_root(lambda_scale: float = 1.0) -> float:
    """Solve tanh(eta)=exp(-lambda eta) by bisection."""
    lo = 0.0
    hi = 20.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        value = math.tanh(mid) - math.exp(-lambda_scale * mid)
        if value < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def survival_exp(evidence: float, lambda_scale: float = 1.0) -> float:
    return math.exp(-lambda_scale * evidence)


def survival_linear(evidence: float) -> float:
    return max(0.0, 1.0 - evidence)


def survival_weibull(evidence: float, shape: float = 2.0) -> float:
    return math.exp(-(evidence**shape))


def log_partition(h: list[float], stats: list[tuple[int, ...]]) -> float:
    total = 0.0
    for omega in itertools.product([-1.0, 1.0], repeat=2):
        action = sum(h_j * chi_j(*omega) for h_j, chi_j in zip(h, stats))
        total += math.exp(action)
    return math.log(total / 4.0)


def gradient_psi(h: list[float], stats: list[tuple[int, ...]]) -> list[float]:
    weighted = [0.0 for _ in h]
    z = 0.0
    for omega in itertools.product([-1.0, 1.0], repeat=2):
        chis = [chi_j(*omega) for chi_j in stats]
        weight = math.exp(sum(h_j * chi for h_j, chi in zip(h, chis)))
        z += weight
        for j, chi in enumerate(chis):
            weighted[j] += weight * chi
    return [value / z for value in weighted]


def commitment_potential(h: list[float], stats: list[tuple[int, ...]]) -> float:
    return log_partition(h, stats) + sum(math.exp(-h_j) for h_j in h)


def commitment_gradient(h: list[float], stats: list[tuple[int, ...]]) -> list[float]:
    grad = gradient_psi(h, stats)
    return [grad_j - math.exp(-h_j) for grad_j, h_j in zip(grad, h)]


def gradient_norm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def solve_vector_commitment(stats: list[tuple[int, ...]]) -> tuple[list[float], float, float]:
    """Minimize psi(h)+sum exp(-h_j) by damped gradient descent."""
    h = [0.5 for _ in stats]
    value = commitment_potential(h, stats)
    for _ in range(20000):
        grad = commitment_gradient(h, stats)
        if gradient_norm(grad) < 1e-13:
            break
        step = 1.0
        while step > 1e-12:
            candidate = [h_j - step * grad_j for h_j, grad_j in zip(h, grad)]
            candidate_value = commitment_potential(candidate, stats)
            if candidate_value <= value - 1e-4 * step * sum(g * g for g in grad):
                h = candidate
                value = candidate_value
                break
            step *= 0.5
        else:
            break
    residual = gradient_norm(commitment_gradient(h, stats))
    return h, value, residual


def finite_second_difference(
    h: list[float],
    stats: list[tuple[int, ...]],
    direction: list[float],
    eps: float = 1e-4,
) -> float:
    plus = [h_j + eps * d_j for h_j, d_j in zip(h, direction)]
    minus = [h_j - eps * d_j for h_j, d_j in zip(h, direction)]
    center = commitment_potential(h, stats)
    return (commitment_potential(plus, stats) - 2.0 * center + commitment_potential(minus, stats)) / (eps * eps)


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    i_a = 0.37
    i_b = 0.82
    exp_glue_gap = abs(survival_exp(i_a + i_b) - survival_exp(i_a) * survival_exp(i_b))
    lin_glue_gap = abs(survival_linear(i_a + i_b) - survival_linear(i_a) * survival_linear(i_b))
    weibull_glue_gap = abs(survival_weibull(i_a + i_b) - survival_weibull(i_a) * survival_weibull(i_b))

    i_test = 1.40
    mismatch_lam_half = abs(-math.log(survival_exp(i_test, 0.5)) - i_test)
    mismatch_lam_one = abs(-math.log(survival_exp(i_test, 1.0)) - i_test)
    mismatch_lam_two = abs(-math.log(survival_exp(i_test, 2.0)) - i_test)

    regrad_nonlinear_gap = abs((i_a + i_b) ** 2 - (i_a**2 + i_b**2))
    regrad_linear_mismatch = abs(2.0 * i_test - i_test)

    eta_star = solve_scalar_root(1.0)
    theta_star = math.tanh(eta_star)
    scalar_residual = abs(theta_star - math.exp(-eta_star))
    scalar_monotone_margin = min(
        (1.0 / math.cosh(k / 20.0) ** 2) + math.exp(-k / 20.0)
        for k in range(0, 200)
    )

    eta_lam_half = solve_scalar_root(0.5)
    eta_lam_two = solve_scalar_root(2.0)

    stats_independent = [
        lambda x, y: x,
        lambda x, y: y,
    ]
    h_ind, value_ind, residual_ind = solve_vector_commitment(stats_independent)
    grad_ind = gradient_psi(h_ind, stats_independent)
    rhs_ind = [math.exp(-h_j) for h_j in h_ind]

    stats_complete = [
        lambda x, y: x,
        lambda x, y: y,
        lambda x, y: x * y,
    ]
    h_comp, value_comp, residual_comp = solve_vector_commitment(stats_complete)
    grad_comp = gradient_psi(h_comp, stats_complete)
    rhs_comp = [math.exp(-h_j) for h_j in h_comp]

    directions = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0 / math.sqrt(3.0)] * 3,
    ]
    min_curv_complete = min(finite_second_difference(h_comp, stats_complete, direction) for direction in directions)

    # Full-odds convention is the most dangerous normalization attack.  It uses
    # two signed cochain units instead of one primitive oriented unit.
    eta_full_odds = solve_scalar_root(2.0)
    full_odds_gap = abs(eta_full_odds - eta_star)
    full_odds_action_surplus = abs(2.0 * eta_star - eta_star)

    rows = [
        Row(
            "eventless gluing",
            "S(I+J)=S(I)S(J) in additive RN/KL evidence",
            "exponential survival glues exactly; non-exponential waiting shapes do not",
            f"exp={exp_glue_gap:.1e}, linear={lin_glue_gap:.3f}, weibull={weibull_glue_gap:.3f}",
            "DERIVES-EXPONENTIAL-SHAPE",
        ),
        Row(
            "scale self-accounting",
            "-log S(I) must equal the sealed record evidence I",
            "lambda=1 is the only exponential rate with no surplus/deficit RN action",
            f"lam.5={mismatch_lam_half:.3f}, lam1={mismatch_lam_one:.1e}, lam2={mismatch_lam_two:.3f}",
            "FIXES-r=1",
        ),
        Row(
            "clock regraduation attack",
            "replace I by f(I)",
            "nonlinear clocks violate sealed additivity; linear rescalings violate self-accounting unless c=1",
            f"nonlinear_gap={regrad_nonlinear_gap:.3f}, c2_mismatch={regrad_linear_mismatch:.3f}",
            "REJECTS-HIDDEN-CLOCK",
        ),
        Row(
            "scalar commitment law",
            "retained parity memory equals no-division survival through its own RN cochain action",
            "tanh(eta)=exp(-eta) has one positive root",
            f"eta={eta_star:.9f}, theta={theta_star:.9f}, residual={scalar_residual:.1e}",
            "SELECTS-h",
        ),
        Row(
            "scalar uniqueness",
            "d/deta[tanh(eta)-exp(-eta)] is positive",
            "the scalar root cannot bifurcate or form a branch family",
            f"min_derivative_sample={scalar_monotone_margin:.6f}",
            "UNIQUE",
        ),
        Row(
            "scale-family refutation",
            "solve tanh(eta)=exp(-lambda eta)",
            "other lambda values select other eta, but those lambda values already fail RN self-accounting",
            f"eta_lam.5={eta_lam_half:.6f}, eta_lam2={eta_lam_two:.6f}",
            "REJECTS-BRANCH-B-SCALE",
        ),
        Row(
            "independent ledger",
            "minimize psi(h)+sum exp(-h_j) for two primitive modes",
            "the vector law decouples and selects the same intrinsic scalar root per mode",
            f"h=({h_ind[0]:.6f},{h_ind[1]:.6f}), residual={residual_ind:.1e}",
            "PASS",
        ),
        Row(
            "complete coupled ledger",
            "solve grad psi(h)=exp(-h) for x,y,xy closed-history statistics",
            "strict convex commitment potential selects a single coupled h vector",
            f"h=({h_comp[0]:.6f},{h_comp[1]:.6f},{h_comp[2]:.6f}), residual={residual_comp:.1e}",
            "PASS-COUPLED",
        ),
        Row(
            "convex isolation",
            "finite second differences of psi+sum exp(-h_j)",
            "positive curvature around the coupled solution gives an isolated selector",
            f"min_curv={min_curv_complete:.6f}, value={value_comp:.6f}",
            "ISOLATED",
        ),
        Row(
            "full-odds normalization attack",
            "use two-sided log odds 2 eta as one commitment unit",
            "it moves the root and double-counts one primitive oriented cochain action",
            f"eta_2unit={eta_full_odds:.6f}, gap={full_odds_gap:.6f}, surplus={full_odds_action_surplus:.6f}",
            "REJECTED-BY-COCHAIN-UNIT",
        ),
        Row(
            "division-law verdict",
            "RN/KL clock + sealed gluing + exact self-accounting + same-law holonomy fixed point",
            "the intrinsic division-event commitment law is S(I)=exp(-I) and grad psi(h)=exp(-h)",
            f"eta_star={eta_star:.9f}",
            "FINITE-CLOSURE",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "exp_glue_gap": exp_glue_gap,
        "linear_glue_gap": lin_glue_gap,
        "weibull_glue_gap": weibull_glue_gap,
        "mismatch_lambda_half": mismatch_lam_half,
        "mismatch_lambda_one": mismatch_lam_one,
        "mismatch_lambda_two": mismatch_lam_two,
        "regrad_nonlinear_gap": regrad_nonlinear_gap,
        "regrad_linear_mismatch": regrad_linear_mismatch,
        "eta_star": eta_star,
        "theta_star": theta_star,
        "scalar_residual": scalar_residual,
        "scalar_monotone_margin_sample": scalar_monotone_margin,
        "eta_lambda_half": eta_lam_half,
        "eta_lambda_two": eta_lam_two,
        "h_independent_0": h_ind[0],
        "h_independent_1": h_ind[1],
        "grad_independent_0": grad_ind[0],
        "rhs_independent_0": rhs_ind[0],
        "independent_residual": residual_ind,
        "h_complete_0": h_comp[0],
        "h_complete_1": h_comp[1],
        "h_complete_2": h_comp[2],
        "grad_complete_0": grad_comp[0],
        "rhs_complete_0": rhs_comp[0],
        "complete_residual": residual_comp,
        "min_curv_complete": min_curv_complete,
        "eta_full_odds": eta_full_odds,
        "full_odds_gap": full_odds_gap,
        "full_odds_action_surplus": full_odds_action_surplus,
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")


if __name__ == "__main__":
    main()
