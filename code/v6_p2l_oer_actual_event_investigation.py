"""
v6 Paper 2 Part II §5.24: actual-event OER investigation.

This diagnostic asks whether the positive OER theorem in §5.23 is likely to be
the right target for the actual interacting event law. It separates:

1. strict symmetric OER: the deletion response is the equal role ray;
2. generalized OER: the deletion response is a fixed positive role vector;
3. failures where ACV, deletion response, or beta convergence is lost.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from v6_p2j_lr_decisive_tests import (
    acv_actual_event_law_audit,
    acv_collar_jacobian,
    detector_threshold_closure_case,
    fisher_width_selection_receipt,
)
from v6_p2k_one_event_response import analytic_beta_from_blur


ROLE_COUNT = 4
U_DELETE = [0.5, 0.5, 0.5, 0.5]


@dataclass
class EventLawSequence:
    case: str
    fixed_by_event_law: bool
    jacobians: list[list[list[float]]]
    internal_couplings: list[float]


@dataclass
class OERInvestigation:
    case: str
    fixed: bool
    strict_symmetric: bool
    generalized_oer: bool
    acv: bool
    cost: bool
    sym_spread_n: float
    dir_drift: float
    kappa_source_n: float
    beta_n: float
    beta_span: float
    schur_margin_n: float
    verdict: str


def common_private_jacobian(
    common: float,
    private: list[float],
    residual: float = 0.0,
) -> list[list[float]]:
    if len(private) != ROLE_COUNT:
        raise ValueError("private must have four role entries")
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


def max_pair_step(vectors: list[list[float]]) -> float:
    if len(vectors) < 2:
        return 0.0
    steps = []
    for a, b in zip(vectors[:-1], vectors[1:]):
        steps.append(max(abs(a[i] - b[i]) for i in range(ROLE_COUNT)))
    return max(steps)


def evaluate_sequence(seq: EventLawSequence) -> OERInvestigation:
    _, _, gamma, _, _, _, _, _ = detector_threshold_closure_case(1.70, 2.40, 1.00)
    acv_flags = []
    cost_flags = []
    betas = []
    directions = []
    strict_flags = []
    kappa_source_n = 0.0
    schur_margin_n = 0.0
    sym_spread_n = 0.0

    for jacobian, coupling in zip(seq.jacobians, seq.internal_couplings):
        _, _, _, _, _, eps_j, _, schur_margin, acv_passes = (
            acv_actual_event_law_audit(jacobian, 0.80, coupling)
        )
        d = deletion_vector(jacobian)
        safe_d = [x - 4.0 * eps_j for x in d]
        kappa_source = safe_d[1]
        blur_cost = gamma * max(kappa_source, 0.0)
        width, _, _, cost_passes = fisher_width_selection_receipt(blur_cost)
        beta_grid = 1.0 / width if width > 1e-15 else 0.0
        beta_exact = analytic_beta_from_blur(blur_cost)

        acv_flags.append(acv_passes and min(safe_d) > 0.0)
        cost_flags.append(cost_passes)
        betas.append(beta_exact if beta_exact > 0.0 else beta_grid)
        directions.append(normalize(safe_d))
        spread = max(safe_d) - min(safe_d)
        strict_flags.append(spread <= 0.02)
        kappa_source_n = kappa_source
        schur_margin_n = schur_margin
        sym_spread_n = spread

    beta_span = max(betas) - min(betas) if betas else float("inf")
    dir_drift = max_pair_step(directions)
    acv = all(acv_flags)
    cost = all(cost_flags)
    strict = acv and cost and all(strict_flags) and beta_span <= 0.05
    generalized = (
        seq.fixed_by_event_law
        and acv
        and cost
        and kappa_source_n > 0.0
        and dir_drift <= 0.035
        and beta_span <= 0.05
    )
    verdict = "PASS" if generalized else "FAIL"
    return OERInvestigation(
        case=seq.case,
        fixed=seq.fixed_by_event_law,
        strict_symmetric=strict,
        generalized_oer=generalized,
        acv=acv,
        cost=cost,
        sym_spread_n=sym_spread_n,
        dir_drift=dir_drift,
        kappa_source_n=kappa_source_n,
        beta_n=betas[-1] if betas else 0.0,
        beta_span=beta_span,
        schur_margin_n=schur_margin_n,
        verdict=verdict,
    )


def investigation_sequences() -> list[EventLawSequence]:
    couplings = [0.040, 0.030, 0.020, 0.015]
    symmetric = common_private_jacobian(0.030, [0.900, 0.900, 0.900, 0.900])
    stable_anisotropic = common_private_jacobian(0.030, [0.820, 0.900, 0.960, 1.020])
    common_heavy = common_private_jacobian(0.300, [0.200, 0.200, 0.200, 0.200])
    weak_source = common_private_jacobian(0.030, [0.900, 0.050, 0.900, 0.900])
    split_source = acv_collar_jacobian(source_redundant=True)

    drift_private = [
        [0.820, 0.900, 0.960, 1.020],
        [0.820, 0.760, 0.960, 1.020],
        [0.820, 0.560, 0.960, 1.020],
        [0.820, 0.360, 0.960, 1.020],
    ]

    return [
        EventLawSequence("strict symmetric", True, [symmetric for _ in couplings], couplings),
        EventLawSequence(
            "stable anisotropic",
            True,
            [stable_anisotropic for _ in couplings],
            couplings,
        ),
        EventLawSequence(
            "anisotropic free",
            False,
            [stable_anisotropic for _ in couplings],
            couplings,
        ),
        EventLawSequence(
            "source drift",
            True,
            [common_private_jacobian(0.030, p) for p in drift_private],
            couplings,
        ),
        EventLawSequence("common-heavy", True, [common_heavy for _ in couplings], couplings),
        EventLawSequence("weak source", True, [weak_source for _ in couplings], couplings),
        EventLawSequence("split-source", False, [split_source for _ in couplings], couplings),
    ]


def print_investigation(rows: list[OERInvestigation]) -> None:
    print("actual-event OER investigation")
    print("------------------------------")
    print(
        "case                 fixed  strict  genOER  ACV   cost  "
        "sym_spread  dir_drift  kappa_S  beta_N  beta_span  schur_N  verdict"
    )
    for row in rows:
        print(
            f"{row.case:20s}  "
            f"{('yes' if row.fixed else 'no'):5s}  "
            f"{('PASS' if row.strict_symmetric else 'FAIL'):6s}  "
            f"{('PASS' if row.generalized_oer else 'FAIL'):6s}  "
            f"{('PASS' if row.acv else 'FAIL'):4s}  "
            f"{('PASS' if row.cost else 'FAIL'):4s}  "
            f"{row.sym_spread_n:10.4f}  "
            f"{row.dir_drift:9.4f}  "
            f"{row.kappa_source_n:7.4f}  "
            f"{row.beta_n:6.4f}  "
            f"{row.beta_span:9.4f}  "
            f"{row.schur_margin_n:7.4f}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [evaluate_sequence(seq) for seq in investigation_sequences()]
    print("=" * 120)
    print("v6 Paper 2 Part II §5.24: actual-event OER investigation")
    print("=" * 120)
    print_investigation(rows)
    print("VERDICT")
    print("-------")
    print("strict symmetric OER is sufficient but not necessary.")
    print("stable anisotropic source-record response fails strict symmetry but")
    print("passes generalized OER because the deletion vector, source amplitude,")
    print("ACV margin, and beta are fixed by the event law.")
    print("free amplitude, source drift, common-heavy coupling, weak source, and")
    print("split-source response each fail one required theorem input.")


if __name__ == "__main__":
    main()
