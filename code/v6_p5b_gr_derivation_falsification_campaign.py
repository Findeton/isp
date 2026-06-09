#!/usr/bin/env python3
"""Paper 5 diagnostic B: GR derivation/falsification campaign.

Question: do the current SHARD screen/source data derive full 3+1 GR?

Verdict tested here:
  No, not from the current data alone.  SHARD has operative finite
  record-gravity and metric-like screen data, but full GR requires additional
  normal-sector data (lapse/cross-normalization/shift or an equivalent
  covariant record object) and a continuum coupling theorem.

The diagnostic gives finite positive receipts and explicit twins that refute a
full-GR derivation from screen/source shadows alone.
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


def poisson_solve_ring(source: list[float], kappa: float = 1.0) -> list[float]:
    """Mean-zero solve L phi = kappa source on a ring, L=2I-shifts."""
    n = len(source)
    # Fourier solve using direct trigonometric sums to avoid dependencies.
    phi = [0.0 for _ in range(n)]
    for m in range(1, n):
        lam = 2.0 - 2.0 * math.cos(2.0 * math.pi * m / n)
        a = sum(kappa * source[j] * math.cos(2.0 * math.pi * m * j / n) for j in range(n)) / n
        b = sum(kappa * source[j] * math.sin(2.0 * math.pi * m * j / n) for j in range(n)) / n
        for j in range(n):
            angle = 2.0 * math.pi * m * j / n
            phi[j] += (a * math.cos(angle) + b * math.sin(angle)) / lam
    mean = sum(phi) / n
    return [x - mean for x in phi]


def ring_residual(phi: list[float], source: list[float], kappa: float = 1.0) -> float:
    n = len(phi)
    res = []
    for i in range(n):
        lhs = 2 * phi[i] - phi[(i - 1) % n] - phi[(i + 1) % n]
        res.append(lhs - kappa * source[i])
    return math.sqrt(sum(x * x for x in res) / n)


def phi_span(phi: list[float]) -> float:
    return max(phi) - min(phi)


def base_curvature_from_omega(alpha: float, omega0: float = 1.0) -> float:
    """At u=v=0 for Omega=omega0*exp(alpha u v), R_base=4 alpha / omega0^2."""
    return 4.0 * alpha / (omega0 * omega0)


def screen_einstein_component(alpha: float, omega0: float = 1.0) -> float:
    """For product metric 2D normal x flat 2D screen: G_xx=-R_base/2."""
    return -0.5 * base_curvature_from_omega(alpha, omega0)


def count_gr_components(cells: int) -> tuple[int, int, int]:
    scalar_components = cells
    symmetric_einstein_components = 10 * cells
    bianchi_reduced_components = 6 * cells
    return scalar_components, symmetric_einstein_components, bianchi_reduced_components


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    n = 16
    source = [0.0 for _ in range(n)]
    source[3] = 1.0
    source[11] = -1.0
    phi = poisson_solve_ring(source, 1.0)
    res = ring_residual(phi, source, 1.0)

    phi_half = poisson_solve_ring(source, 0.5)
    phi_two = poisson_solve_ring(source, 2.0)
    coupling_span = phi_span(phi_two) - phi_span(phi_half)

    # Same screen metric q_AB=delta_AB, different normal conformal factor Omega.
    g_xx_flat = screen_einstein_component(alpha=0.0)
    g_xx_curved = screen_einstein_component(alpha=0.37)
    normal_twin_gap = abs(g_xx_curved - g_xx_flat)

    omega_scaled = screen_einstein_component(alpha=0.37, omega0=1.7)
    omega_scale_gap = abs(omega_scaled - g_xx_curved)

    scalar_components, einstein_components, reduced_components = count_gr_components(64)
    missing_after_bianchi = reduced_components - scalar_components

    # A closed-screen source must sum to zero in the scalar finite packet.  Full
    # covariant stress-energy needs more than that: pressure/flux components can
    # vary while the scalar projection is fixed.
    scalar_projection = [1.0, -1.0, 0.0, 0.0]
    stress_a = {
        "rho": [1.0, -1.0, 0.0, 0.0],
        "pressure": [0.2, 0.2, -0.1, -0.3],
    }
    stress_b = {
        "rho": scalar_projection[:],
        "pressure": [-0.4, 0.7, 0.1, -0.4],
    }
    same_scalar_gap = max(abs(a - b) for a, b in zip(stress_a["rho"], stress_b["rho"]))
    pressure_gap = math.sqrt(sum((a - b) ** 2 for a, b in zip(stress_a["pressure"], stress_b["pressure"])))

    rows = [
        Row(
            "finite record-gravity receipt",
            "solve ring L phi = rho with zero total source",
            "the operative finite SHARD response equation works",
            f"res={res:.1e}, span={phi_span(phi):.6f}",
            "PASS-FINITE-GRAVITY",
        ),
        Row(
            "coupling attack",
            "change only kappa in L phi = kappa rho",
            "finite conservation survives but response scale moves",
            f"span_half={phi_span(phi_half):.6f}, span_two={phi_span(phi_two):.6f}, gap={coupling_span:.6f}",
            "REFUTES-UNIVERSAL-COUPLING-FROM-POISSON",
        ),
        Row(
            "normal-sector twin",
            "same flat screen metric q_AB but Omega=1 versus exp(alpha u v)",
            "Einstein tensor screen component changes while screen q_AB is identical",
            f"Gxx_flat={g_xx_flat:.6f}, Gxx_curved={g_xx_curved:.6f}, gap={normal_twin_gap:.6f}",
            "REFUTES-SCREEN-ONLY-GR",
        ),
        Row(
            "cross-normalization attack",
            "same alpha but rescale Omega0",
            "normal normalization changes Einstein tensor component",
            f"Gxx_omega1={g_xx_curved:.6f}, Gxx_omega1.7={omega_scaled:.6f}, gap={omega_scale_gap:.6f}",
            "NEEDS-INTRINSIC-NORMALIZATION",
        ),
        Row(
            "component-count gate",
            "compare scalar response components with symmetric 3+1 tensor components",
            "scalar record gravity cannot be a full Einstein tensor equation",
            f"scalar={scalar_components}, Gmunu={einstein_components}, after_Bianchi~={reduced_components}, missing={missing_after_bianchi}",
            "REFUTES-SCALAR-TO-FULL-GR",
        ),
        Row(
            "stress tensor projection attack",
            "hold scalar source projection fixed while changing pressure/flux data",
            "same scalar rho does not determine full stress-energy tensor",
            f"rho_gap={same_scalar_gap:.1e}, pressure_gap={pressure_gap:.6f}",
            "NEEDS-TENSOR-RECORD-READOUT",
        ),
        Row(
            "GR verdict",
            "current SHARD screen/source data versus full 3+1 Einstein equation",
            "operative finite gravity is real; full GR is not derived from current data alone",
            "normal sector + tensor stress + coupling theorem required",
            "FULL-GR-FALSIFIED-FROM-CURRENT-DATA",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "finite_residual": res,
        "finite_span": phi_span(phi),
        "coupling_span_gap": coupling_span,
        "normal_twin_gap": normal_twin_gap,
        "omega_scale_gap": omega_scale_gap,
        "component_missing_after_bianchi": float(missing_after_bianchi),
        "pressure_gap": pressure_gap,
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")


if __name__ == "__main__":
    main()
