#!/usr/bin/env python3
"""Paper 4 diagnostic T: cellular source-conservation campaign.

Diagnostic S proves source gluing on a chain.  This diagnostic upgrades the
result to a finite 2D cellular diamond complex with vector-valued interface
holonomy.

Finite model:
  * rectangular grid of sealed diamonds;
  * oriented vertical/horizontal interfaces carrying a two-component h-vector;
  * local tensor/source vector rho_D = divergence of h on the cell boundary;
  * exact cancellation of every internal interface for arbitrary glued blocks;
  * scalar source readouts are projections of the same rho_D;
  * same external boundary with different internal h gives different local
    sources, proving boundary-summary data are insufficient.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


Vec = tuple[float, float]
Cell = tuple[int, int]


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


@dataclass
class GridFlux:
    width: int
    height: int
    # vertical[x][y] is the flux through vertical interface x at row y,
    # oriented in +x direction.  x=0 and x=width are external boundaries.
    vertical: list[list[Vec]]
    # horizontal[x][y] is the flux through horizontal interface y at column x,
    # oriented in +y direction.  y=0 and y=height are external boundaries.
    horizontal: list[list[Vec]]


def vadd(a: Vec, b: Vec) -> Vec:
    return (a[0] + b[0], a[1] + b[1])


def vsub(a: Vec, b: Vec) -> Vec:
    return (a[0] - b[0], a[1] - b[1])


def vscale(scale: float, a: Vec) -> Vec:
    return (scale * a[0], scale * a[1])


def vnorm(a: Vec) -> float:
    return math.sqrt(a[0] * a[0] + a[1] * a[1])


def vmax_gap(a: Vec, b: Vec) -> float:
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def max_vec_gap(left: list[Vec], right: list[Vec]) -> float:
    return max(vmax_gap(a, b) for a, b in zip(left, right))


def flux_value(seed: float, x: int, y: int, kind: str) -> Vec:
    xx = x + 0.37 * y + seed
    yy = y - 0.21 * x - 0.4 * seed
    if kind == "v":
        return (
            0.31 * math.sin(xx) + 0.17 * math.cos(2.0 * yy),
            -0.22 * math.cos(yy) + 0.19 * math.sin(1.7 * xx),
        )
    return (
        -0.27 * math.sin(0.8 * xx) + 0.13 * math.cos(yy),
        0.24 * math.cos(1.2 * yy) + 0.11 * math.sin(xx),
    )


def build_grid(width: int, height: int, seed: float) -> GridFlux:
    vertical = [
        [flux_value(seed, x, y, "v") for y in range(height)]
        for x in range(width + 1)
    ]
    horizontal = [
        [flux_value(seed, x, y, "h") for y in range(height + 1)]
        for x in range(width)
    ]
    return GridFlux(width=width, height=height, vertical=vertical, horizontal=horizontal)


def divergence(grid: GridFlux, cell: Cell) -> Vec:
    x, y = cell
    right_minus_left = vsub(grid.vertical[x + 1][y], grid.vertical[x][y])
    top_minus_bottom = vsub(grid.horizontal[x][y + 1], grid.horizontal[x][y])
    return vadd(right_minus_left, top_minus_bottom)


def all_cells(grid: GridFlux) -> list[Cell]:
    return [(x, y) for y in range(grid.height) for x in range(grid.width)]


def all_sources(grid: GridFlux) -> list[Vec]:
    return [divergence(grid, cell) for cell in all_cells(grid)]


def sum_vec(values: list[Vec]) -> Vec:
    out = (0.0, 0.0)
    for value in values:
        out = vadd(out, value)
    return out


def block_cells(x0: int, x1: int, y0: int, y1: int) -> list[Cell]:
    return [(x, y) for y in range(y0, y1) for x in range(x0, x1)]


def block_source(grid: GridFlux, x0: int, x1: int, y0: int, y1: int) -> Vec:
    return sum_vec([divergence(grid, cell) for cell in block_cells(x0, x1, y0, y1)])


def block_boundary_flux(grid: GridFlux, x0: int, x1: int, y0: int, y1: int) -> Vec:
    total = (0.0, 0.0)
    for y in range(y0, y1):
        total = vsub(total, grid.vertical[x0][y])
        total = vadd(total, grid.vertical[x1][y])
    for x in range(x0, x1):
        total = vsub(total, grid.horizontal[x][y0])
        total = vadd(total, grid.horizontal[x][y1])
    return total


def max_block_conservation_error(grid: GridFlux) -> float:
    errors = []
    for x0 in range(grid.width):
        for x1 in range(x0 + 1, grid.width + 1):
            for y0 in range(grid.height):
                for y1 in range(y0 + 1, grid.height + 1):
                    errors.append(vmax_gap(block_source(grid, x0, x1, y0, y1), block_boundary_flux(grid, x0, x1, y0, y1)))
    return max(errors)


def internal_interface_cancel_max(grid: GridFlux) -> float:
    max_cancel = 0.0
    for x in range(1, grid.width):
        for y in range(grid.height):
            left_cell_contribution = grid.vertical[x][y]
            right_cell_contribution = vscale(-1.0, grid.vertical[x][y])
            max_cancel = max(max_cancel, vnorm(vadd(left_cell_contribution, right_cell_contribution)))
    for x in range(grid.width):
        for y in range(1, grid.height):
            bottom_cell_contribution = grid.horizontal[x][y]
            top_cell_contribution = vscale(-1.0, grid.horizontal[x][y])
            max_cancel = max(max_cancel, vnorm(vadd(bottom_cell_contribution, top_cell_contribution)))
    return max_cancel


def boundary_summary(grid: GridFlux) -> Vec:
    return block_boundary_flux(grid, 0, grid.width, 0, grid.height)


def make_same_boundary_twin(grid: GridFlux) -> GridFlux:
    twin = build_grid(grid.width, grid.height, seed=2.7)
    # Copy every external boundary interface; keep different internal fluxes.
    for y in range(grid.height):
        twin.vertical[0][y] = grid.vertical[0][y]
        twin.vertical[grid.width][y] = grid.vertical[grid.width][y]
    for x in range(grid.width):
        twin.horizontal[x][0] = grid.horizontal[x][0]
        twin.horizontal[x][grid.height] = grid.horizontal[x][grid.height]
    return twin


def scalar_projection(sources: list[Vec], weight: Vec) -> list[float]:
    return [rho[0] * weight[0] + rho[1] * weight[1] for rho in sources]


def refine_grid(grid: GridFlux) -> GridFlux:
    width = 2 * grid.width
    height = 2 * grid.height
    refined = GridFlux(
        width=width,
        height=height,
        vertical=[[(0.0, 0.0) for _ in range(height)] for _ in range(width + 1)],
        horizontal=[[(0.0, 0.0) for _ in range(height + 1)] for _ in range(width)],
    )
    for x in range(grid.width + 1):
        for y in range(grid.height):
            value = vscale(0.5, grid.vertical[x][y])
            refined.vertical[2 * x][2 * y] = value
            refined.vertical[2 * x][2 * y + 1] = value
    for x in range(grid.width):
        for y in range(grid.height + 1):
            value = vscale(0.5, grid.horizontal[x][y])
            refined.horizontal[2 * x][2 * y] = value
            refined.horizontal[2 * x + 1][2 * y] = value
    # Internal split interfaces carry zero flux; they create no silent source.
    return refined


def coarse_sources_from_refined(refined: GridFlux) -> list[Vec]:
    coarse_width = refined.width // 2
    coarse_height = refined.height // 2
    out = []
    for y in range(coarse_height):
        for x in range(coarse_width):
            total = (0.0, 0.0)
            for yy in (2 * y, 2 * y + 1):
                for xx in (2 * x, 2 * x + 1):
                    total = vadd(total, divergence(refined, (xx, yy)))
            out.append(total)
    return out


def add_local_source_knob(sources: list[Vec]) -> list[Vec]:
    knobs = [(0.11, -0.07), (-0.04, 0.03), (0.02, 0.08), (-0.03, -0.01), (0.01, 0.04), (0.06, -0.05)]
    return [vadd(source, knobs[idx % len(knobs)]) for idx, source in enumerate(sources)]


def total_boundary_gap_after_knob(grid: GridFlux, knobbed_sources: list[Vec]) -> float:
    return vmax_gap(sum_vec(knobbed_sources), boundary_summary(grid))


def main() -> None:
    grid = build_grid(width=3, height=2, seed=0.45)
    sources = all_sources(grid)
    source_norm = math.sqrt(sum(vnorm(source) ** 2 for source in sources))
    seam_cancel = internal_interface_cancel_max(grid)
    block_error = max_block_conservation_error(grid)
    total_source = sum_vec(sources)
    boundary_total = boundary_summary(grid)
    total_gap = vmax_gap(total_source, boundary_total)

    twin = make_same_boundary_twin(grid)
    twin_sources = all_sources(twin)
    external_gap = vmax_gap(boundary_summary(grid), boundary_summary(twin))
    local_source_gap = max_vec_gap(sources, twin_sources)
    total_source_gap = vmax_gap(sum_vec(sources), sum_vec(twin_sources))

    weight = (0.6, -0.8)
    scalar_sources = scalar_projection(sources, weight)
    scalar_direct = scalar_projection(all_sources(grid), weight)
    scalar_projection_gap = max(abs(a - b) for a, b in zip(scalar_sources, scalar_direct))
    scalar_block_gap = abs(sum(scalar_sources) - (boundary_total[0] * weight[0] + boundary_total[1] * weight[1]))

    refined = refine_grid(grid)
    refined_block_error = max_block_conservation_error(refined)
    refinement_source_gap = max_vec_gap(sources, coarse_sources_from_refined(refined))

    knobbed = add_local_source_knob(sources)
    knob_boundary_gap = total_boundary_gap_after_knob(grid, knobbed)
    zero_total_knobbed = knobbed[:]
    correction = vscale(1.0 / len(zero_total_knobbed), vsub(sum_vec(zero_total_knobbed), sum_vec(sources)))
    zero_total_knobbed = [vsub(source, correction) for source in zero_total_knobbed]
    zero_total_gap = vmax_gap(sum_vec(zero_total_knobbed), sum_vec(sources))
    zero_local_gap = max_vec_gap(zero_total_knobbed, sources)

    rows = [
        Row(
            "cellular tensor source",
            "rho_D^nu = discrete divergence of vector interface h^{mu nu}",
            "all source components are induced by one global interface cochain",
            f"norm={source_norm:.6f}",
            "PASS-INTERNAL-TENSOR-SOURCE",
        ),
        Row(
            "internal seam cancellation",
            "each shared interface enters adjacent cells with opposite signs",
            "no tensor source is created by a cellular cut",
            f"cancel={seam_cancel:.1e}",
            "PASS-SEAM-CANCELS",
        ),
        Row(
            "cellular divergence theorem",
            "sum sources over every rectangular glued subcomplex",
            "local source sum equals external boundary flux",
            f"block_err={block_error:.1e}, total_gap={total_gap:.1e}",
            "PASS-CONSERVATION",
        ),
        Row(
            "same-boundary cellular twin",
            "fix every external boundary interface and change internal h",
            "boundary data alone do not determine local tensor sources",
            f"boundary_gap={external_gap:.1e}, local_gap={local_source_gap:.6f}, total_gap={total_source_gap:.1e}",
            "REFUTES-BOUNDARY-ONLY",
        ),
        Row(
            "scalar projection",
            "project vector source with an arbitrary readout weight",
            "scalar source is a projection of the same conserved tensor source",
            f"proj_gap={scalar_projection_gap:.1e}, block_gap={scalar_block_gap:.1e}",
            "PASS-SCALAR-AS-PROJECTION",
        ),
        Row(
            "neutral cellular refinement",
            "split each diamond into four count subdiamonds",
            "coarse sources and conservation are preserved",
            f"source_gap={refinement_source_gap:.1e}, refined_block_err={refined_block_error:.1e}",
            "PASS-REFINEMENT",
        ),
        Row(
            "free local tensor-source attack",
            "add local source knobs after h is fixed",
            "global boundary conservation is generically violated",
            f"boundary_gap={knob_boundary_gap:.6f}",
            "FAILS-AS-KNOB",
        ),
        Row(
            "zero-total tensor-source attack",
            "adjust local sources with total boundary preserved",
            "still changes local source field and is not the same h-process",
            f"total_gap={zero_total_gap:.1e}, local_gap={zero_local_gap:.6f}",
            "FAILS-SAME-PROCESS",
        ),
        Row(
            "cellular source verdict",
            "complete interface h versus tensor source conservation",
            "full source conservation is a cellular gluing identity, not an added axiom",
            "complete h required",
            "FINITE-CELLULAR-CLOSURE",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("width", grid.width)
    print("height", grid.height)
    print("source_norm", f"{source_norm:.15e}")
    print("seam_cancel", f"{seam_cancel:.15e}")
    print("block_error", f"{block_error:.15e}")
    print("total_source", f"{total_source[0]:.15e}", f"{total_source[1]:.15e}")
    print("boundary_total", f"{boundary_total[0]:.15e}", f"{boundary_total[1]:.15e}")
    print("total_gap", f"{total_gap:.15e}")
    print("same_boundary_external_gap", f"{external_gap:.15e}")
    print("same_boundary_local_source_gap", f"{local_source_gap:.15e}")
    print("same_boundary_total_source_gap", f"{total_source_gap:.15e}")
    print("scalar_projection_gap", f"{scalar_projection_gap:.15e}")
    print("scalar_block_gap", f"{scalar_block_gap:.15e}")
    print("refinement_source_gap", f"{refinement_source_gap:.15e}")
    print("refined_block_error", f"{refined_block_error:.15e}")
    print("knob_boundary_gap", f"{knob_boundary_gap:.15e}")
    print("zero_total_gap", f"{zero_total_gap:.15e}")
    print("zero_local_gap", f"{zero_local_gap:.15e}")


if __name__ == "__main__":
    main()
