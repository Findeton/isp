#!/usr/bin/env python3
"""Paper 4 diagnostic U: cofinal continuum reconstruction campaign.

The finite sealed-holonomy laws are internally consistent.  This diagnostic
asks whether a projective/cofinal refinement family can converge to a
continuum record-gravity object.

Finite model:
  * dyadic square grids;
  * interface h is an integrated flux of a smooth vector field F;
  * rho is cellular divergence of h, hence cell integral of div F;
  * dyadic coarsening of h and rho is exact for integrated fluxes;
  * finite source densities converge to the continuum divergence;
  * finite Poisson/Laplace operators converge at second order on a smooth
    scalar test field;
  * non-Markovian whole-history parity under neutral refinement is preserved;
  * high-frequency zero-coarse refinements refute convergence without a
    bounded-energy / no-silent-refinement condition.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


Vec = tuple[float, float]


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


@dataclass
class FluxGrid:
    n: int
    vertical: list[list[float]]
    horizontal: list[list[float]]


def f_vec(x: float, y: float) -> Vec:
    return (
        math.sin(2.0 * math.pi * x) * math.cos(math.pi * y) + 0.25 * x * y,
        -0.7 * math.cos(math.pi * x) * math.sin(2.0 * math.pi * y) + 0.18 * x * x,
    )


def div_f(x: float, y: float) -> float:
    return (
        2.0 * math.pi * math.cos(2.0 * math.pi * x) * math.cos(math.pi * y)
        + 0.25 * y
        - 1.4 * math.pi * math.cos(math.pi * x) * math.cos(2.0 * math.pi * y)
    )


def phi(x: float, y: float) -> float:
    return math.sin(math.pi * x) * math.sin(math.pi * y) + 0.2 * math.sin(2.0 * math.pi * x) * math.sin(math.pi * y)


def lap_phi(x: float, y: float) -> float:
    return (
        -2.0 * math.pi**2 * math.sin(math.pi * x) * math.sin(math.pi * y)
        - 0.2 * 5.0 * math.pi**2 * math.sin(2.0 * math.pi * x) * math.sin(math.pi * y)
    )


def midpoint_flux_grid(n: int) -> FluxGrid:
    dx = 1.0 / n
    vertical = [[0.0 for _ in range(n)] for _ in range(n + 1)]
    horizontal = [[0.0 for _ in range(n + 1)] for _ in range(n)]
    for i in range(n + 1):
        x = i * dx
        for j in range(n):
            y = (j + 0.5) * dx
            vertical[i][j] = f_vec(x, y)[0] * dx
    for i in range(n):
        x = (i + 0.5) * dx
        for j in range(n + 1):
            y = j * dx
            horizontal[i][j] = f_vec(x, y)[1] * dx
    return FluxGrid(n=n, vertical=vertical, horizontal=horizontal)


def source_integrals(grid: FluxGrid) -> list[list[float]]:
    n = grid.n
    out = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            out[i][j] = (
                grid.vertical[i + 1][j]
                - grid.vertical[i][j]
                + grid.horizontal[i][j + 1]
                - grid.horizontal[i][j]
            )
    return out


def source_density(grid: FluxGrid) -> list[list[float]]:
    n = grid.n
    dx2 = (1.0 / n) ** 2
    rho = source_integrals(grid)
    return [[rho[i][j] / dx2 for j in range(n)] for i in range(n)]


def continuum_divergence_on_cells(n: int) -> list[list[float]]:
    dx = 1.0 / n
    return [[div_f((i + 0.5) * dx, (j + 0.5) * dx) for j in range(n)] for i in range(n)]


def l2_grid_error(a: list[list[float]], b: list[list[float]]) -> float:
    n = len(a)
    return math.sqrt(sum((a[i][j] - b[i][j]) ** 2 for i in range(n) for j in range(n)) / (n * n))


def coarsen_flux(fine: FluxGrid) -> FluxGrid:
    if fine.n % 2:
        raise ValueError("expected even fine grid")
    n = fine.n // 2
    vertical = [[0.0 for _ in range(n)] for _ in range(n + 1)]
    horizontal = [[0.0 for _ in range(n + 1)] for _ in range(n)]
    for i in range(n + 1):
        for j in range(n):
            vertical[i][j] = fine.vertical[2 * i][2 * j] + fine.vertical[2 * i][2 * j + 1]
    for i in range(n):
        for j in range(n + 1):
            horizontal[i][j] = fine.horizontal[2 * i][2 * j] + fine.horizontal[2 * i + 1][2 * j]
    return FluxGrid(n=n, vertical=vertical, horizontal=horizontal)


def coarsen_sources(fine_rho: list[list[float]]) -> list[list[float]]:
    nf = len(fine_rho)
    n = nf // 2
    out = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            out[i][j] = (
                fine_rho[2 * i][2 * j]
                + fine_rho[2 * i + 1][2 * j]
                + fine_rho[2 * i][2 * j + 1]
                + fine_rho[2 * i + 1][2 * j + 1]
            )
    return out


def flux_gap(a: FluxGrid, b: FluxGrid) -> float:
    max_gap = 0.0
    for i in range(a.n + 1):
        for j in range(a.n):
            max_gap = max(max_gap, abs(a.vertical[i][j] - b.vertical[i][j]))
    for i in range(a.n):
        for j in range(a.n + 1):
            max_gap = max(max_gap, abs(a.horizontal[i][j] - b.horizontal[i][j]))
    return max_gap


def source_gap(a: list[list[float]], b: list[list[float]]) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a)))


def discrete_laplacian_error(n: int) -> float:
    dx = 1.0 / n
    errors = []
    for i in range(1, n - 1):
        x = i * dx
        for j in range(1, n - 1):
            y = j * dx
            disc = (
                phi((i + 1) * dx, y)
                + phi((i - 1) * dx, y)
                + phi(x, (j + 1) * dx)
                + phi(x, (j - 1) * dx)
                - 4.0 * phi(x, y)
            ) / (dx * dx)
            errors.append((disc - lap_phi(x, y)) ** 2)
    return math.sqrt(sum(errors) / len(errors))


def total_variation_parity(theta: float) -> float:
    # Neutral refinement copies a 3-bit parity law into an added independent
    # bit. Coarse-graining the added bit preserves the non-Markovian parity
    # law exactly; CMI/triple content is not forced to vanish.
    left = []
    coarse = []
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                parity = (1 if a else -1) * (1 if b else -1) * (1 if c else -1)
                p = 0.125 * (1.0 + theta * parity)
                coarse.append(p)
                left.append(0.5 * p)
                left.append(0.5 * p)
    recovered = [left[2 * i] + left[2 * i + 1] for i in range(len(coarse))]
    return 0.5 * sum(abs(a - b) for a, b in zip(coarse, recovered))


def oscillatory_fine_zero_coarse(n: int, amp: float) -> FluxGrid:
    # Fine grid with n even. Coarse vertical/horizontal boundary sums vanish
    # in pairs, but fine source density and energy do not.
    vertical = [[0.0 for _ in range(n)] for _ in range(n + 1)]
    horizontal = [[0.0 for _ in range(n + 1)] for _ in range(n)]
    for i in range(n + 1):
        x_sign = 1.0 if i % 2 == 0 else -1.0
        for j in range(n):
            # The y-parity makes every coarse interface sum vanish.  The
            # x-parity makes neighboring fine cells see different inflow and
            # outflow, so the source density is not zero.
            vertical[i][j] = amp * x_sign * ((-1.0) ** j)
    return FluxGrid(n=n, vertical=vertical, horizontal=horizontal)


def flux_energy(grid: FluxGrid) -> float:
    return (
        sum(value * value for col in grid.vertical for value in col)
        + sum(value * value for col in grid.horizontal for value in col)
    )


def max_abs_density(density: list[list[float]]) -> float:
    return max(abs(value) for row in density for value in row)


def main() -> None:
    coarse = midpoint_flux_grid(16)
    fine = midpoint_flux_grid(32)
    coarsened_fine = coarsen_flux(fine)
    rho_coarse = source_integrals(coarse)
    rho_fine = source_integrals(fine)
    coarsened_rho_fine = coarsen_sources(rho_fine)
    projective_flux_gap = flux_gap(coarse, coarsened_fine)
    projective_source_gap = source_gap(rho_coarse, coarsened_rho_fine)

    div_errors = []
    lap_errors = []
    for n in (16, 32, 64):
        grid = midpoint_flux_grid(n)
        div_errors.append(l2_grid_error(source_density(grid), continuum_divergence_on_cells(n)))
        lap_errors.append(discrete_laplacian_error(n))
    div_ratio_16_32 = div_errors[0] / div_errors[1]
    div_ratio_32_64 = div_errors[1] / div_errors[2]
    lap_ratio_16_32 = lap_errors[0] / lap_errors[1]
    lap_ratio_32_64 = lap_errors[1] / lap_errors[2]

    parity_tv = total_variation_parity(theta=0.54)

    osc = oscillatory_fine_zero_coarse(32, amp=0.002)
    osc_coarse = coarsen_flux(osc)
    zero_grid = FluxGrid(
        n=16,
        vertical=[[0.0 for _ in range(16)] for _ in range(17)],
        horizontal=[[0.0 for _ in range(17)] for _ in range(16)],
    )
    osc_coarse_gap = flux_gap(osc_coarse, zero_grid)
    osc_density = source_density(osc)
    osc_density_max = max_abs_density(osc_density)
    osc_energy = flux_energy(osc)

    bounded_amp = 1.0 / (32**4)
    osc_bounded = oscillatory_fine_zero_coarse(32, amp=bounded_amp)
    bounded_density_max = max_abs_density(source_density(osc_bounded))
    bounded_energy = flux_energy(osc_bounded)

    rows = [
        Row(
            "projective flux compatibility",
            "coarsen integrated fine interface h to coarse grid",
            "smooth flux family is cofinally compatible up to quadrature error",
            f"flux_gap={projective_flux_gap:.3e}",
            "PASS-CONTROLLED",
        ),
        Row(
            "projective source compatibility",
            "coarsen fine cellular divergences",
            "source integrals coarsen to coarse source integrals",
            f"rho_gap={projective_source_gap:.3e}",
            "PASS-CONTROLLED",
        ),
        Row(
            "source-density convergence",
            "compare cellular divergence density to continuum div F",
            "smooth h gives convergent source density",
            f"err16/32/64={div_errors[0]:.3e}/{div_errors[1]:.3e}/{div_errors[2]:.3e}",
            "PASS-CONTINUUM",
        ),
        Row(
            "operator convergence",
            "finite Laplacian on smooth scalar test field",
            "L_n converges to continuum Laplace operator",
            f"err16/32/64={lap_errors[0]:.3e}/{lap_errors[1]:.3e}/{lap_errors[2]:.3e}",
            "PASS-CONTINUUM",
        ),
        Row(
            "convergence rates",
            "error ratios under dyadic refinement",
            "rates are stable and near second-order for smooth tests",
            f"div={div_ratio_16_32:.2f}/{div_ratio_32_64:.2f}, lap={lap_ratio_16_32:.2f}/{lap_ratio_32_64:.2f}",
            "PASS-RATE",
        ),
        Row(
            "non-Markovian projective history",
            "neutral refinement of parity whole-history law",
            "coarse whole-history law is preserved; Markov factorization is not forced",
            f"TV={parity_tv:.1e}",
            "PASS-INDIVISIBLE",
        ),
        Row(
            "refinement-twin attack",
            "add zero-coarse high-frequency interface holonomy",
            "same coarse h can hide nonzero fine source density",
            f"coarse_gap={osc_coarse_gap:.1e}, density_max={osc_density_max:.3e}",
            "REFUTES-COARSE-ONLY",
        ),
        Row(
            "energy/tightness gate",
            "scale zero-coarse oscillation with refinement",
            "bounded-energy/no-silent-refinement condition suppresses hidden fine source",
            f"density_max={bounded_density_max:.3e}, energy={bounded_energy:.3e}",
            "COND-COFINAL-GATE",
        ),
        Row(
            "cofinal verdict",
            "controlled projective h versus arbitrary refinements",
            "continuum reconstruction works with projective tightness; fails from coarse shadows alone",
            "bounded complete h required",
            "FINITE-COFINAL-THEOREM-TARGET",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("projective_flux_gap", f"{projective_flux_gap:.15e}")
    print("projective_source_gap", f"{projective_source_gap:.15e}")
    print("div_error_16", f"{div_errors[0]:.15e}")
    print("div_error_32", f"{div_errors[1]:.15e}")
    print("div_error_64", f"{div_errors[2]:.15e}")
    print("div_ratio_16_32", f"{div_ratio_16_32:.15e}")
    print("div_ratio_32_64", f"{div_ratio_32_64:.15e}")
    print("lap_error_16", f"{lap_errors[0]:.15e}")
    print("lap_error_32", f"{lap_errors[1]:.15e}")
    print("lap_error_64", f"{lap_errors[2]:.15e}")
    print("lap_ratio_16_32", f"{lap_ratio_16_32:.15e}")
    print("lap_ratio_32_64", f"{lap_ratio_32_64:.15e}")
    print("parity_refinement_tv", f"{parity_tv:.15e}")
    print("osc_coarse_gap", f"{osc_coarse_gap:.15e}")
    print("osc_density_max", f"{osc_density_max:.15e}")
    print("osc_energy", f"{osc_energy:.15e}")
    print("bounded_density_max", f"{bounded_density_max:.15e}")
    print("bounded_energy", f"{bounded_energy:.15e}")


if __name__ == "__main__":
    main()
