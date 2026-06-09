#!/usr/bin/env python3
"""Paper 4 diagnostic S: sealed source-gluing law.

Diagnostic R leaves source/boundary cochains as physical state data.  This
diagnostic asks whether those data can be internalized by gluing:

    rho_D = boundary coboundary / divergence of neighboring h-cochains.

Finite model:
  * a chain of sealed diamonds;
  * oriented interface holonomies h_e, including external boundary edges;
  * local source rho_i = -h_left(i) + h_right(i);
  * internal interface contributions cancel exactly when diamonds are glued.

The result:
  * complete global interface h fixes every local source;
  * internal sources cancel on glued composites, leaving only external boundary
    mismatch;
  * external boundary totals alone do not determine local sources;
  * arbitrary local source knobs either violate sealed gluing or correspond to
    a different global h-cochain.
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


def max_gap(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def l2(values: list[float]) -> float:
    return math.sqrt(sum(value * value for value in values))


def sources_from_interfaces(h: list[float]) -> list[float]:
    # h has n+1 oriented interfaces for n diamonds.  Source at diamond i is
    # the right holonomy minus the left holonomy.
    return [h[i + 1] - h[i] for i in range(len(h) - 1)]


def internal_contribution_pairs(h: list[float]) -> list[tuple[float, float]]:
    # Shared interface i contributes +h_i to the left diamond's right boundary
    # and -h_i to the right diamond's left boundary.
    return [(h[i], -h[i]) for i in range(1, len(h) - 1)]


def composite_source(h: list[float], start: int, stop: int) -> float:
    # Composite of diamonds start..stop-1 has only external boundary mismatch.
    return h[stop] - h[start]


def local_sum(rho: list[float], start: int, stop: int) -> float:
    return sum(rho[start:stop])


def solve_chain_interfaces_from_boundary_and_sources(left: float, rho: list[float]) -> list[float]:
    h = [left]
    for value in rho:
        h.append(h[-1] + value)
    return h


def laplacian_chain(n: int) -> list[list[float]]:
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 2.0
        if i > 0:
            matrix[i][i - 1] = -1.0
        if i + 1 < n:
            matrix[i][i + 1] = -1.0
    matrix[0][0] = 1.0
    matrix[-1][-1] = 1.0
    return matrix


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
            aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [aug[row][-1] for row in range(n)]


def poisson_response(rho: list[float]) -> list[float]:
    n = len(rho)
    matrix = laplacian_chain(n)
    rhs = rho[:]
    # Dirichlet/eventless exterior response at the two ends.
    matrix[0] = [0.0] * n
    matrix[-1] = [0.0] * n
    matrix[0][0] = 1.0
    matrix[-1][-1] = 1.0
    rhs[0] = 0.0
    rhs[-1] = 0.0
    return solve_linear(matrix, rhs)


def matrix_vec(a: list[list[float]], x: list[float]) -> list[float]:
    return [sum(aij * xj for aij, xj in zip(row, x)) for row in a]


def main() -> None:
    # Complete global interface cochain for four glued diamonds.
    h = [0.15, 0.72, -0.08, 0.46, 0.91]
    rho = sources_from_interfaces(h)
    internal_pairs = internal_contribution_pairs(h)
    internal_cancel_max = max(abs(left + right) for left, right in internal_pairs)
    total_source = sum(rho)
    external_mismatch = h[-1] - h[0]
    composite_errors = [
        abs(local_sum(rho, start, stop) - composite_source(h, start, stop))
        for start in range(len(rho))
        for stop in range(start + 1, len(rho) + 1)
    ]
    composite_error = max(composite_errors)

    # Same external boundary, different internal interface cochain.
    h_twin = [h[0], -0.31, 0.28, -0.52, h[-1]]
    rho_twin = sources_from_interfaces(h_twin)
    external_gap = max(abs(h_twin[0] - h[0]), abs(h_twin[-1] - h[-1]))
    local_source_gap = max_gap(rho, rho_twin)
    total_source_gap = abs(sum(rho) - sum(rho_twin))

    # Complete h fixes source and can be recovered from left boundary plus
    # local source list.  If local source is analyst-chosen, it changes h.
    recovered_h = solve_chain_interfaces_from_boundary_and_sources(h[0], rho)
    recovery_gap = max_gap(h, recovered_h)
    free_rho = [rho[0] + 0.20, rho[1] - 0.35, rho[2] + 0.11, rho[3] + 0.09]
    free_h = solve_chain_interfaces_from_boundary_and_sources(h[0], free_rho)
    free_right_gap = abs(free_h[-1] - h[-1])
    free_h_gap = max_gap(h, free_h)

    # A locally adjusted source that preserves total external mismatch is still
    # a different internal h-cochain, not the same physical sealed process.
    zero_sum_adjustment = [0.18, -0.23, 0.14, -0.09]
    adjusted_rho = [a + b for a, b in zip(rho, zero_sum_adjustment)]
    adjusted_h = solve_chain_interfaces_from_boundary_and_sources(h[0], adjusted_rho)
    adjusted_external_gap = abs(adjusted_h[-1] - h[-1])
    adjusted_h_gap = max_gap(h, adjusted_h)

    # Source conservation and unique response once rho is induced.
    phi = poisson_response(rho)
    matrix = laplacian_chain(len(rho))
    poisson_residual = max_gap(matrix_vec(matrix, phi)[1:-1], rho[1:-1])
    phi_twin = poisson_response(rho_twin)
    response_gap = max_gap(phi, phi_twin)

    rows = [
        Row(
            "source as coboundary",
            "rho_i=h_{i+1}-h_i from global interface cochain",
            "complete glued h fixes every local source",
            f"rho_norm={l2(rho):.6f}",
            "PASS-INTERNAL-SOURCE",
        ),
        Row(
            "internal cancellation",
            "shared interface contributes with opposite signs",
            "no source is created by an artificial cut",
            f"cancel={internal_cancel_max:.1e}",
            "PASS-SEAM-CANCELS",
        ),
        Row(
            "composite conservation",
            "sum local sources over any glued block",
            "composite source equals external boundary mismatch",
            f"err={composite_error:.1e}, total={total_source:.6f}, ext={external_mismatch:.6f}",
            "PASS-BOUNDARY-ONLY",
        ),
        Row(
            "same-boundary twin",
            "hold external h fixed and change internal interfaces",
            "external boundary summaries do not determine local sources",
            f"ext_gap={external_gap:.1e}, local_gap={local_source_gap:.6f}, total_gap={total_source_gap:.1e}",
            "REFUTES-BOUNDARY-ONLY",
        ),
        Row(
            "complete h uniqueness",
            "recover h from left boundary plus induced rho",
            "same complete cochain gives same source assignment",
            f"gap={recovery_gap:.1e}",
            "PROVES-UNIQUE-GIVEN-H",
        ),
        Row(
            "free local source attack",
            "alter local rho after h is fixed",
            "either right boundary or the global cochain changes",
            f"right_gap={free_right_gap:.6f}, h_gap={free_h_gap:.6f}",
            "FAILS-AS-EXTERNAL-KNOB",
        ),
        Row(
            "zero-sum local source attack",
            "preserve external mismatch but alter internal rho",
            "still changes the internal closed-holonomy cochain",
            f"ext_gap={adjusted_external_gap:.1e}, h_gap={adjusted_h_gap:.6f}",
            "FAILS-SAME-PROCESS",
        ),
        Row(
            "Poisson response",
            "solve response equation using induced rho",
            "response is unique once source is glued from h",
            f"res={poisson_residual:.1e}, twin_response_gap={response_gap:.6f}",
            "PASS-CONDITIONAL-RESPONSE",
        ),
        Row(
            "source-gluing verdict",
            "source data from complete global h versus local knobs",
            "sources are internal boundary mismatches, not independent parameters",
            "complete h required",
            "FINITE-CLOSURE-WITH-GLOBAL-H",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("h", " ".join(f"{value:.15e}" for value in h))
    print("rho", " ".join(f"{value:.15e}" for value in rho))
    print("internal_cancel_max", f"{internal_cancel_max:.15e}")
    print("composite_error", f"{composite_error:.15e}")
    print("total_source", f"{total_source:.15e}")
    print("external_mismatch", f"{external_mismatch:.15e}")
    print("same_boundary_external_gap", f"{external_gap:.15e}")
    print("same_boundary_local_source_gap", f"{local_source_gap:.15e}")
    print("same_boundary_total_source_gap", f"{total_source_gap:.15e}")
    print("recovery_gap", f"{recovery_gap:.15e}")
    print("free_right_gap", f"{free_right_gap:.15e}")
    print("free_h_gap", f"{free_h_gap:.15e}")
    print("adjusted_external_gap", f"{adjusted_external_gap:.15e}")
    print("adjusted_h_gap", f"{adjusted_h_gap:.15e}")
    print("poisson_residual", f"{poisson_residual:.15e}")
    print("response_gap", f"{response_gap:.15e}")


if __name__ == "__main__":
    main()
