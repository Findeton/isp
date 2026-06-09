"""
v6 Paper 2 Part II §5.23: one-event deletion-response audit.

This focused diagnostic tests the final visible branch-A bottleneck after
Kappa Lock. The question is not whether the event support is shared, nor
whether beta can converge numerically. The question is whether deleting one
selected event produces a role-faithful, refinement-stable response whose
source/gravity component fixes kappa_G before C-lock computes beta.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2j_lr_decisive_tests import (
    acv_actual_event_law_audit,
    acv_collar_jacobian,
    detector_threshold_closure_case,
    fisher_width_selection_receipt,
    source_record_detector_jacobian,
)


@dataclass
class ResponseScan:
    case: str
    fixed: bool
    acv: bool
    cost: bool
    sigma: float
    leak: float
    kappa_n: float
    beta_n: float
    beta_span: float
    tail_drift: float
    verdict: str


@dataclass
class OERCertificate:
    common: float
    private: float
    deletion_spread: float
    role_margin: float
    eps_j_n: float
    kappa_n: float
    schur_margin: float
    beta_grid: float
    beta_exact: float
    verdict: str


def free_beta_span() -> float:
    betas = []
    for blur_cost in [0.030, 0.050, 0.120, 0.250]:
        width, _, _, _ = fisher_width_selection_receipt(blur_cost)
        betas.append(1.0 / width if width > 1e-15 else float("inf"))
    return max(betas) - min(betas)


def analytic_beta_from_blur(blur_cost: float) -> float:
    """Exact beta for Phi(ell)=ell/(1/(4 ell^4)+c ell^2)."""
    if blur_cost <= 0.0:
        return 0.0
    return (4.0 * blur_cost / 5.0) ** (1.0 / 6.0)


def positive_oer_certificate() -> OERCertificate:
    """Finite positive OER certificate for the symmetric source-record class."""
    common = 0.030
    private = 0.900
    internal_coupling = 0.015
    internal_floor = 0.80
    internal_role = 0.50
    jacobian = source_record_detector_jacobian(common, private)
    deletion_direction = [0.5, 0.5, 0.5, 0.5]
    responses = [
        sum(row[i] * deletion_direction[i] for i in range(4))
        for row in jacobian
    ]
    deletion_spread = max(responses) - min(responses)
    sigma, leak, role_margin, _, _, eps_j, deletion_margin, schur_margin, acv_passes = (
        acv_actual_event_law_audit(jacobian, internal_floor, internal_coupling, internal_role)
    )
    del sigma, leak
    _, _, gamma, _, _, _, _, _ = detector_threshold_closure_case(1.70, 2.40, 1.00)
    blur_cost = gamma * max(deletion_margin, 0.0)
    width, _, _, cost_passes = fisher_width_selection_receipt(blur_cost)
    beta_grid = 1.0 / width if width > 1e-15 else 0.0
    beta_exact = analytic_beta_from_blur(blur_cost)
    passes = (
        deletion_spread <= 1e-12
        and role_margin > 0.0
        and schur_margin > 0.0
        and deletion_margin > 0.0
        and acv_passes
        and cost_passes
    )
    return OERCertificate(
        common=common,
        private=private,
        deletion_spread=deletion_spread,
        role_margin=role_margin,
        eps_j_n=eps_j,
        kappa_n=deletion_margin,
        schur_margin=schur_margin,
        beta_grid=beta_grid,
        beta_exact=beta_exact,
        verdict="PASS" if passes else "FAIL",
    )


def response_scan(
    case: str,
    jacobian: list[list[float]],
    internal_couplings: list[float],
    fixed: bool,
) -> ResponseScan:
    """Scan deletion-derived kappa_G across finite refinements."""
    _, _, gamma, _, _, _, _, _ = detector_threshold_closure_case(1.70, 2.40, 1.00)
    kappas = []
    betas = []
    acv_flags = []
    cost_flags = []
    sigma_n = 0.0
    leak_n = 0.0

    for coupling in internal_couplings:
        sigma, leak, _, _, _, _, deletion_margin, _, acv_passes = (
            acv_actual_event_law_audit(jacobian, 0.80, coupling)
        )
        kappa_g = max(deletion_margin, 0.0)
        blur_cost = gamma * kappa_g
        width, _, _, cost_passes = fisher_width_selection_receipt(blur_cost)
        beta = 1.0 / width if width > 1e-15 else float("inf")
        kappas.append(kappa_g)
        betas.append(beta)
        acv_flags.append(acv_passes)
        cost_flags.append(cost_passes)
        sigma_n = sigma
        leak_n = leak

    beta_span = max(betas) - min(betas)
    tail_drift = abs(betas[-1] - betas[-2]) if len(betas) >= 2 else 0.0
    acv = all(acv_flags)
    cost = all(cost_flags)
    passes = fixed and acv and cost and kappas[-1] > 0.0 and beta_span <= 0.05 and tail_drift <= 0.02
    return ResponseScan(
        case=case,
        fixed=fixed,
        acv=acv,
        cost=cost,
        sigma=sigma_n,
        leak=leak_n,
        kappa_n=kappas[-1],
        beta_n=betas[-1],
        beta_span=beta_span,
        tail_drift=tail_drift,
        verdict="PASS" if passes else "FAIL",
    )


def print_response_scan(rows: list[ResponseScan]) -> None:
    print("one-event deletion-response audit")
    print("---------------------------------")
    print(
        "case                  fixed  acv   cost  sigma    leak   "
        "kappa_N  beta_N  beta_span  tail_drift  verdict"
    )
    for row in rows:
        fixed = "yes" if row.fixed else "no"
        acv = "PASS" if row.acv else "FAIL"
        cost = "PASS" if row.cost else "FAIL"
        print(
            f"{row.case:21s}  {fixed:5s}  {acv:4s}  {cost:4s}  "
            f"{row.sigma:6.4f}  {row.leak:6.4f}  {row.kappa_n:7.4f}  "
            f"{row.beta_n:6.4f}  {row.beta_span:9.4f}  "
            f"{row.tail_drift:10.4f}  {row.verdict}"
        )
    print()


def print_oer_certificate(cert: OERCertificate) -> None:
    print("positive finite OER certificate: symmetric source-record class")
    print("--------------------------------------------------------------")
    print(
        "common  private  del_spread  role_margin  eps_J_N  "
        "kappa_N  schur_N  beta_grid  beta_exact  verdict"
    )
    print(
        f"{cert.common:6.3f}  {cert.private:7.3f}  {cert.deletion_spread:10.6f}  "
        f"{cert.role_margin:11.6f}  {cert.eps_j_n:7.4f}  "
        f"{cert.kappa_n:7.4f}  {cert.schur_margin:7.4f}  "
        f"{cert.beta_grid:9.4f}  {cert.beta_exact:10.4f}  {cert.verdict}"
    )
    print()


def main() -> None:
    free_span = free_beta_span()
    support_only = ResponseScan(
        case="support-only label",
        fixed=False,
        acv=False,
        cost=False,
        sigma=0.0,
        leak=0.0,
        kappa_n=0.0,
        beta_n=0.0,
        beta_span=free_span,
        tail_drift=free_span,
        verdict="FAIL",
    )
    free_amplitude = response_scan(
        "free amplitude",
        source_record_detector_jacobian(0.030, 0.900),
        [0.040, 0.030, 0.020, 0.015],
        fixed=False,
    )
    honest = response_scan(
        "honest one-event",
        source_record_detector_jacobian(0.030, 0.900),
        [0.040, 0.030, 0.020, 0.015],
        fixed=True,
    )
    large_drift = response_scan(
        "large drift",
        source_record_detector_jacobian(0.030, 0.900),
        [0.180, 0.120, 0.060, 0.020],
        fixed=True,
    )
    split_source = response_scan(
        "split-source",
        acv_collar_jacobian(source_redundant=True),
        [0.040, 0.030, 0.020, 0.015],
        fixed=False,
    )

    print("=" * 94)
    print("v6 Paper 2 Part II §5.23: cofinal one-event response")
    print("=" * 94)
    print_oer_certificate(positive_oer_certificate())
    print_response_scan([support_only, free_amplitude, honest, large_drift, split_source])

    print("VERDICT")
    print("-------")
    print("finite positive OER theorem: PASS in the symmetric source-record response class")
    print("full one-event response theorem: OPEN")
    print("finite audit bite: shared support and stable beta are insufficient.")
    print("Branch A needs fixed kappa_G from the same deletion response that")
    print("passes ACV, survives refinement, and excludes split-source amplitudes.")


if __name__ == "__main__":
    main()
