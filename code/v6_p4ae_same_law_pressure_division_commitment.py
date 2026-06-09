#!/usr/bin/env python3
"""Paper 4 diagnostic AE: same-law pressure and division commitment.

The v1-v5 audit points to the strongest remaining route:

  P^{hist} should come from a cofinal same-law finite pressure, or from a
  division-event / record-commitment process whose waiting law fixes the
  closed-history coefficients.

This script tests that route on the one-coefficient parity family.  It gives
the renewal/self-commitment idea its best finite chance: a simple fixed-point
commitment equation does select a nonzero eta.  The campaign then asks whether
the scale, waiting-law shape, and commitment units are intrinsic.  They are not
fixed by the current corpus, so the route is conditional rather than closed.
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


def atanh(x: float) -> float:
    x = max(min(x, 1.0 - 1e-15), -1.0 + 1e-15)
    return 0.5 * math.log((1.0 + x) / (1.0 - x))


def pressure(eta: float, s: float) -> float:
    return math.log(math.cosh(eta + s)) - math.log(math.cosh(eta))


def pressure_prime_zero(eta: float) -> float:
    return math.tanh(eta)


def pressure_second_zero(eta: float) -> float:
    return 1.0 / (math.cosh(eta) ** 2)


def eta_from_theta(theta: float) -> float:
    return atanh(theta)


def poisson_theta(window: float, tau: float) -> float:
    return math.exp(-window / tau)


def deterministic_theta(window: float, tau: float) -> float:
    return max(0.0, 1.0 - window / tau)


def solve_fixed_point_poisson(r: float) -> float:
    """Solve eta = atanh(exp(-r eta)) for eta > 0."""
    best_eta = 0.0
    best_gap = float("inf")
    for k in range(1, 200000):
        eta = 6.0 * k / 200000.0
        gap = abs(eta - eta_from_theta(math.exp(-r * eta)))
        if gap < best_gap:
            best_gap = gap
            best_eta = eta
    return best_eta


def solve_fixed_point_deterministic(r: float) -> float:
    """Solve eta = atanh(max(0, 1 - r eta)) for eta > 0."""
    best_eta = 0.0
    best_gap = float("inf")
    for k in range(1, 200000):
        eta = 3.0 * k / 200000.0
        theta = max(0.0, 1.0 - r * eta)
        gap = abs(eta - eta_from_theta(theta))
        if gap < best_gap:
            best_gap = gap
            best_eta = eta
    return best_eta


def likelihood_eta(growth: float, threshold: float, window: float = 1.0) -> float:
    """Commit when growth*t^2=threshold, then use Poisson no-division survival."""
    tau = math.sqrt(threshold / growth)
    return eta_from_theta(poisson_theta(window, tau))


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    eta_a = 0.3316471087051321
    eta_b = 0.9504793805965235
    mean_a = pressure_prime_zero(eta_a)
    mean_b = pressure_prime_zero(eta_b)
    curv_a = pressure_second_zero(eta_a)
    curv_b = pressure_second_zero(eta_b)
    pressure_recon_gap = max(abs(eta_from_theta(mean_a) - eta_a), abs(eta_from_theta(mean_b) - eta_b))

    window = 0.40
    tau_a = 1.00
    tau_b = 1.80
    eta_tau_a = eta_from_theta(poisson_theta(window, tau_a))
    eta_tau_b = eta_from_theta(poisson_theta(window, tau_b))

    eta_poisson = eta_from_theta(poisson_theta(window, tau_a))
    eta_det = eta_from_theta(deterministic_theta(window, tau_a))
    same_mean_gap = abs(eta_poisson - eta_det)

    eta_growth_a = likelihood_eta(growth=1.0, threshold=1.0)
    eta_growth_b = likelihood_eta(growth=4.0, threshold=1.0)
    growth_gap = abs(eta_growth_a - eta_growth_b)

    eta_fp_r1 = solve_fixed_point_poisson(1.0)
    eta_fp_r2 = solve_fixed_point_poisson(2.0)
    eta_fp_gap = abs(eta_fp_r1 - eta_fp_r2)

    eta_fp_det_r1 = solve_fixed_point_deterministic(1.0)
    eta_fp_det_r2 = solve_fixed_point_deterministic(2.0)
    fp_shape_gap = abs(eta_fp_r1 - eta_fp_det_r1)

    theta_fp_r1 = math.tanh(eta_fp_r1)
    tau_fp_r1 = 1.0 / eta_fp_r1
    info_at_tau = eta_fp_r1 * eta_fp_r1 * tau_fp_r1 * tau_fp_r1

    rows = [
        Row(
            "same-law pressure identity",
            "Psi_eta(s)=log E_eta exp(sH)",
            "pressure derivatives reconstruct supplied eta but do not select it",
            f"meanA={mean_a:.6f}, meanB={mean_b:.6f}, recon={pressure_recon_gap:.1e}",
            "READOUT-NOT-SELECTION",
        ),
        Row(
            "pressure curvature",
            "compare susceptibilities at two eta values",
            "finite curvature exists for both laws but does not choose between them",
            f"curvA={curv_a:.6f}, curvB={curv_b:.6f}",
            "BOUND-NOT-LAW",
        ),
        Row(
            "supplied renewal waiting time",
            "Poisson no-division survival over the same window",
            "eta is selected only after tau is supplied",
            f"eta_tau1={eta_tau_a:.6f}, eta_tau2={eta_tau_b:.6f}",
            "BRANCH-B-TAU",
        ),
        Row(
            "same mean, different waiting law",
            "Poisson versus deterministic divisions with same mean tau",
            "the full waiting-law shape matters, not just division density",
            f"eta_poisson={eta_poisson:.6f}, eta_det={eta_det:.6f}, gap={same_mean_gap:.6f}",
            "BRANCH-B-PSI",
        ),
        Row(
            "likelihood-zero commitment",
            "commit at canonical likelihood threshold with different growth rates",
            "the threshold can be canonical while the information-growth scale remains free",
            f"eta_g1={eta_growth_a:.6f}, eta_g4={eta_growth_b:.6f}, gap={growth_gap:.6f}",
            "SCALE-STILL-FREE",
        ),
        Row(
            "self-consistent commitment",
            "solve eta=atanh(exp(-r eta))",
            "a nonzero eta is selected for fixed dimensionless r",
            f"r1_eta={eta_fp_r1:.6f}, theta={theta_fp_r1:.6f}, info_tau={info_at_tau:.6f}",
            "PASS-CONDITIONAL",
        ),
        Row(
            "commitment scale attack",
            "change only the dimensionless commitment ratio r",
            "the selected eta moves, so r must be intrinsic",
            f"eta_r1={eta_fp_r1:.6f}, eta_r2={eta_fp_r2:.6f}, gap={eta_fp_gap:.6f}",
            "BRANCH-B-SCALE",
        ),
        Row(
            "commitment shape attack",
            "Poisson versus deterministic self-commitment",
            "the selected eta moves when the division waiting-law class changes",
            f"eta_poisson={eta_fp_r1:.6f}, eta_det={eta_fp_det_r1:.6f}, gap={fp_shape_gap:.6f}",
            "BRANCH-B-SHAPE",
        ),
        Row(
            "division-law verdict",
            "same-law pressure + renewal + likelihood + self-consistency",
            "this is the right law-shape, but closure requires intrinsic r and waiting law",
            "P_hist closed only if division law is derived",
            "CONDITIONAL-ONLY",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "eta_a": eta_a,
        "eta_b": eta_b,
        "pressure_mean_a": mean_a,
        "pressure_mean_b": mean_b,
        "pressure_curvature_a": curv_a,
        "pressure_curvature_b": curv_b,
        "pressure_reconstruction_gap": pressure_recon_gap,
        "window": window,
        "tau_a": tau_a,
        "tau_b": tau_b,
        "eta_tau_a": eta_tau_a,
        "eta_tau_b": eta_tau_b,
        "eta_poisson_same_mean": eta_poisson,
        "eta_deterministic_same_mean": eta_det,
        "same_mean_waiting_shape_gap": same_mean_gap,
        "eta_growth_1": eta_growth_a,
        "eta_growth_4": eta_growth_b,
        "growth_scale_gap": growth_gap,
        "eta_fixed_point_r1": eta_fp_r1,
        "eta_fixed_point_r2": eta_fp_r2,
        "fixed_point_scale_gap": eta_fp_gap,
        "eta_fixed_point_det_r1": eta_fp_det_r1,
        "eta_fixed_point_det_r2": eta_fp_det_r2,
        "fixed_point_shape_gap": fp_shape_gap,
        "theta_fixed_point_r1": theta_fp_r1,
        "tau_fixed_point_r1": tau_fp_r1,
        "info_at_tau_r1": info_at_tau,
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")


if __name__ == "__main__":
    main()
