"""
v6 Paper 2 Part II §5.25: generalized OER bounds.

This diagnostic asks the final A-Scale question in bounds form:

Can the actual event law force the source component of the deletion vector, or
can that component vary while ACV, cost, and same support still pass?
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from v6_p2j_lr_decisive_tests import (
    acv_actual_event_law_audit,
    detector_threshold_closure_case,
    fisher_width_selection_receipt,
)
from v6_p2k_one_event_response import analytic_beta_from_blur


ROLE_COUNT = 4
U_DELETE = [0.5, 0.5, 0.5, 0.5]


@dataclass
class BoundsSequence:
    case: str
    fixed_by_event_law: bool
    common: list[float]
    private: list[list[float]]
    residual: list[float]
    internal_couplings: list[float]


@dataclass
class BoundsResult:
    case: str
    fixed: bool
    acv: bool
    cost: bool
    acv_bound_min: float
    source_bound_min: float
    source_kappa_n: float
    beta_n: float
    beta_span: float
    direction_drift: float
    schur_margin_n: float
    verdict: str


@dataclass
class SourceFamilyRow:
    source_private: float
    acv_bound: float
    source_bound: float
    source_kappa: float
    beta: float
    acv: bool
    cost: bool


def role_jacobian(common: float, private: list[float], residual: float) -> list[list[float]]:
    if len(private) != ROLE_COUNT:
        raise ValueError("private response must have four role entries")
    j = [[common + residual for _ in range(ROLE_COUNT)] for _ in range(ROLE_COUNT)]
    for i in range(ROLE_COUNT):
        j[i][i] = common + private[i]
    return j


def deletion_vector(jacobian: list[list[float]]) -> list[float]:
    return [
        sum(row[i] * U_DELETE[i] for i in range(ROLE_COUNT))
        for row in jacobian
    ]


def normalize(v: list[float]) -> list[float]:
    n = sqrt(sum(x * x for x in v))
    if n <= 1e-15:
        return [0.0 for _ in v]
    return [x / n for x in v]


def direction_drift(vectors: list[list[float]]) -> float:
    if len(vectors) < 2:
        return 0.0
    out = 0.0
    for a, b in zip(vectors[:-1], vectors[1:]):
        out = max(out, max(abs(a[i] - b[i]) for i in range(ROLE_COUNT)))
    return out


def analytic_bounds(
    common: float,
    private: list[float],
    residual: float,
    eps_j: float,
) -> tuple[float, float]:
    """Conservative ACV and source-deletion lower bounds.

    For J = diag(p_i) + c 11^T + residual off-row terms:
    sigma-lambda-4eps >= p_min - 2c - 3r - 4eps;
    d_source-4eps >= 1/2 p_source + 2c - 3r/2 - 4eps.
    """
    p_min = min(private)
    p_source = private[1]
    acv_bound = p_min - 2.0 * common - 3.0 * residual - 4.0 * eps_j
    source_bound = 0.5 * p_source + 2.0 * common - 1.5 * residual - 4.0 * eps_j
    return acv_bound, source_bound


def beta_from_source_kappa(gamma: float, source_kappa: float) -> tuple[float, bool]:
    blur_cost = gamma * max(source_kappa, 0.0)
    width, _, _, cost_passes = fisher_width_selection_receipt(blur_cost)
    beta_grid = 1.0 / width if width > 1e-15 else 0.0
    beta_exact = analytic_beta_from_blur(blur_cost)
    return beta_exact if beta_exact > 0.0 else beta_grid, cost_passes


def evaluate_sequence(seq: BoundsSequence) -> BoundsResult:
    _, _, gamma, _, _, _, _, _ = detector_threshold_closure_case(1.70, 2.40, 1.00)
    acv_flags = []
    cost_flags = []
    betas = []
    directions = []
    acv_bounds = []
    source_bounds = []
    source_kappa_n = 0.0
    schur_margin_n = 0.0

    for common, private, residual, coupling in zip(
        seq.common,
        seq.private,
        seq.residual,
        seq.internal_couplings,
    ):
        jacobian = role_jacobian(common, private, residual)
        _, _, _, _, _, eps_j, _, schur_margin, acv_passes = (
            acv_actual_event_law_audit(jacobian, 0.80, coupling)
        )
        d = deletion_vector(jacobian)
        safe_d = [x - 4.0 * eps_j for x in d]
        source_kappa = safe_d[1]
        beta, cost_passes = beta_from_source_kappa(gamma, source_kappa)
        acv_bound, source_bound = analytic_bounds(common, private, residual, eps_j)

        acv_flags.append(acv_passes and acv_bound > 0.0 and source_bound > 0.0)
        cost_flags.append(cost_passes)
        betas.append(beta)
        directions.append(normalize(safe_d))
        acv_bounds.append(acv_bound)
        source_bounds.append(source_bound)
        source_kappa_n = source_kappa
        schur_margin_n = schur_margin

    beta_span = max(betas) - min(betas) if betas else float("inf")
    drift = direction_drift(directions)
    acv = all(acv_flags)
    cost = all(cost_flags)
    passes = (
        seq.fixed_by_event_law
        and acv
        and cost
        and min(source_bounds) > 0.0
        and beta_span <= 0.05
        and drift <= 0.04
    )
    return BoundsResult(
        case=seq.case,
        fixed=seq.fixed_by_event_law,
        acv=acv,
        cost=cost,
        acv_bound_min=min(acv_bounds) if acv_bounds else 0.0,
        source_bound_min=min(source_bounds) if source_bounds else 0.0,
        source_kappa_n=source_kappa_n,
        beta_n=betas[-1] if betas else 0.0,
        beta_span=beta_span,
        direction_drift=drift,
        schur_margin_n=schur_margin_n,
        verdict="PASS" if passes else "FAIL",
    )


def sequence_cases() -> list[BoundsSequence]:
    couplings = [0.040, 0.030, 0.020, 0.015]
    return [
        BoundsSequence(
            "derived generalized",
            True,
            [0.034, 0.032, 0.031, 0.030],
            [
                [0.800, 0.880, 0.950, 1.000],
                [0.810, 0.890, 0.955, 1.010],
                [0.820, 0.895, 0.958, 1.018],
                [0.820, 0.900, 0.960, 1.020],
            ],
            [0.020, 0.012, 0.006, 0.003],
            couplings,
        ),
        BoundsSequence(
            "role isotropic",
            True,
            [0.030 for _ in couplings],
            [[0.900, 0.900, 0.900, 0.900] for _ in couplings],
            [0.000 for _ in couplings],
            couplings,
        ),
        BoundsSequence(
            "free source amp",
            False,
            [0.030 for _ in couplings],
            [[0.820, 0.900, 0.960, 1.020] for _ in couplings],
            [0.003 for _ in couplings],
            couplings,
        ),
        BoundsSequence(
            "source drift",
            True,
            [0.030 for _ in couplings],
            [
                [0.820, 0.900, 0.960, 1.020],
                [0.820, 0.750, 0.960, 1.020],
                [0.820, 0.550, 0.960, 1.020],
                [0.820, 0.350, 0.960, 1.020],
            ],
            [0.003 for _ in couplings],
            couplings,
        ),
        BoundsSequence(
            "common dominated",
            True,
            [0.250 for _ in couplings],
            [[0.300, 0.300, 0.300, 0.300] for _ in couplings],
            [0.020 for _ in couplings],
            couplings,
        ),
        BoundsSequence(
            "weak source",
            True,
            [0.030 for _ in couplings],
            [[0.820, 0.050, 0.960, 1.020] for _ in couplings],
            [0.003 for _ in couplings],
            couplings,
        ),
        BoundsSequence(
            "residual drift",
            True,
            [0.030 for _ in couplings],
            [[0.900, 0.900, 0.900, 0.900] for _ in couplings],
            [0.000, 0.080, 0.160, 0.220],
            couplings,
        ),
    ]


def source_amplitude_family() -> list[SourceFamilyRow]:
    _, _, gamma, _, _, _, _, _ = detector_threshold_closure_case(1.70, 2.40, 1.00)
    rows = []
    common = 0.030
    residual = 0.003
    coupling = 0.015
    for source_private in [0.350, 0.550, 0.750, 0.950, 1.200]:
        private = [0.820, source_private, 0.960, 1.020]
        jacobian = role_jacobian(common, private, residual)
        _, _, _, _, _, eps_j, _, _, acv_passes = (
            acv_actual_event_law_audit(jacobian, 0.80, coupling)
        )
        d = deletion_vector(jacobian)
        source_kappa = d[1] - 4.0 * eps_j
        beta, cost_passes = beta_from_source_kappa(gamma, source_kappa)
        acv_bound, source_bound = analytic_bounds(common, private, residual, eps_j)
        rows.append(
            SourceFamilyRow(
                source_private=source_private,
                acv_bound=acv_bound,
                source_bound=source_bound,
                source_kappa=source_kappa,
                beta=beta,
                acv=acv_passes and acv_bound > 0.0 and source_bound > 0.0,
                cost=cost_passes,
            )
        )
    return rows


def print_bounds(rows: list[BoundsResult]) -> None:
    print("generalized OER bound scan")
    print("--------------------------")
    print(
        "case                 fixed  ACV   cost  acv_lb  source_lb  "
        "kappa_S  beta_N  beta_span  dir_drift  schur_N  verdict"
    )
    for row in rows:
        print(
            f"{row.case:20s}  "
            f"{('yes' if row.fixed else 'no'):5s}  "
            f"{('PASS' if row.acv else 'FAIL'):4s}  "
            f"{('PASS' if row.cost else 'FAIL'):4s}  "
            f"{row.acv_bound_min:7.4f}  "
            f"{row.source_bound_min:9.4f}  "
            f"{row.source_kappa_n:7.4f}  "
            f"{row.beta_n:6.4f}  "
            f"{row.beta_span:9.4f}  "
            f"{row.direction_drift:9.4f}  "
            f"{row.schur_margin_n:7.4f}  "
            f"{row.verdict}"
        )
    print()


def print_source_family(rows: list[SourceFamilyRow]) -> None:
    print("same-support source-amplitude family")
    print("------------------------------------")
    print("p_source  acv_lb  source_lb  kappa_S  beta    ACV   cost")
    for row in rows:
        print(
            f"{row.source_private:8.3f}  "
            f"{row.acv_bound:7.4f}  "
            f"{row.source_bound:9.4f}  "
            f"{row.source_kappa:7.4f}  "
            f"{row.beta:6.4f}  "
            f"{('PASS' if row.acv else 'FAIL'):4s}  "
            f"{('PASS' if row.cost else 'FAIL'):4s}"
        )
    betas = [row.beta for row in rows]
    kappas = [row.source_kappa for row in rows]
    print(f"source kappa span = {max(kappas) - min(kappas):.4f}")
    print(f"beta span = {max(betas) - min(betas):.4f}")
    print()


def main() -> None:
    rows = [evaluate_sequence(case) for case in sequence_cases()]
    family = source_amplitude_family()
    print("=" * 108)
    print("v6 Paper 2 Part II §5.25: generalized OER bounds")
    print("=" * 108)
    print_bounds(rows)
    print_source_family(family)
    print("VERDICT")
    print("-------")
    print("derived generalized OER passes when common, private, residual,")
    print("and Schur terms are fixed by the event law and converge.")
    print("The same-support source-amplitude family keeps the visible margins")
    print("positive while moving kappa_S and beta; without an event-law bound")
    print("on p_source, beta is still a branch-B parameter.")


if __name__ == "__main__":
    main()
