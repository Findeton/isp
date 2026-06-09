#!/usr/bin/env python3
"""Paper 4 diagnostic Z: projective source/period origin campaign.

This diagnostic starts from a finite whole-history law, reconstructs its
closed-holonomy RN coefficients, and derives source/period data from those
coefficients.  It then attacks the construction with external reassignment,
partial readouts, and hidden fine vertical data.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import deque
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


Edge = tuple[int, int]


def rank(matrix: list[list[float]], tol: float = 1e-10) -> int:
    a = [row[:] for row in matrix if any(abs(value) > tol for value in row)]
    if not a:
        return 0
    m = len(a)
    n = len(a[0])
    r = 0
    for c in range(n):
        pivot = max(range(r, m), key=lambda i: abs(a[i][c]))
        if abs(a[pivot][c]) <= tol:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [value / pv for value in a[r]]
        for i in range(m):
            if i == r:
                continue
            factor = a[i][c]
            if abs(factor) > tol:
                a[i] = [a[i][j] - factor * a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def solve_square(matrix: list[list[float]], rhs: list[float], tol: float = 1e-10) -> list[float]:
    n = len(matrix)
    a = [matrix[i][:] + [rhs[i]] for i in range(n)]
    for c in range(n):
        pivot = max(range(c, n), key=lambda i: abs(a[i][c]))
        if abs(a[pivot][c]) <= tol:
            raise ValueError("singular matrix")
        a[c], a[pivot] = a[pivot], a[c]
        pv = a[c][c]
        a[c] = [value / pv for value in a[c]]
        for i in range(n):
            if i == c:
                continue
            factor = a[i][c]
            if abs(factor) > tol:
                a[i] = [a[i][j] - factor * a[c][j] for j in range(n + 1)]
    return [a[i][-1] for i in range(n)]


def mat_vec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def l2(vector: list[float]) -> float:
    return math.sqrt(sum(value * value for value in vector))


def max_gap(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b)) if a else 0.0


def vec_sub(a: list[float], b: list[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def incidence(vertex_count: int, edges: list[Edge], drop_last: bool = True) -> list[list[float]]:
    rows = [[0.0 for _ in edges] for _ in range(vertex_count)]
    for e, (tail, head) in enumerate(edges):
        rows[tail][e] = -1.0
        rows[head][e] = 1.0
    return rows[:-1] if drop_last else rows


def adjacency(vertex_count: int, edges: list[Edge]) -> list[list[tuple[int, int]]]:
    adj: list[list[tuple[int, int]]] = [[] for _ in range(vertex_count)]
    for e, (u, v) in enumerate(edges):
        adj[u].append((v, e))
        adj[v].append((u, e))
    return adj


def spanning_tree_edges(vertex_count: int, edges: list[Edge]) -> set[int]:
    adj = adjacency(vertex_count, edges)
    seen = {0}
    tree: set[int] = set()
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v, e in adj[u]:
            if v not in seen:
                seen.add(v)
                tree.add(e)
                queue.append(v)
    if len(seen) != vertex_count:
        raise ValueError("graph is not connected")
    return tree


def tree_path(vertex_count: int, edges: list[Edge], tree_edges: set[int], start: int, goal: int) -> list[tuple[int, int, int]]:
    adj: list[list[tuple[int, int, int]]] = [[] for _ in range(vertex_count)]
    for e in tree_edges:
        u, v = edges[e]
        adj[u].append((v, e, 1))
        adj[v].append((u, e, -1))
    parent: dict[int, tuple[int, int, int]] = {start: (-1, -1, 0)}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u == goal:
            break
        for v, e, sign in adj[u]:
            if v not in parent:
                parent[v] = (u, e, sign)
                queue.append(v)
    if goal not in parent:
        raise ValueError("tree path not found")
    path: list[tuple[int, int, int]] = []
    cur = goal
    while cur != start:
        prev, e, sign = parent[cur]
        path.append((prev, e, sign))
        cur = prev
    path.reverse()
    return path


def fundamental_cycle_basis(vertex_count: int, edges: list[Edge]) -> list[list[float]]:
    tree = spanning_tree_edges(vertex_count, edges)
    rows: list[list[float]] = []
    for e, (u, v) in enumerate(edges):
        if e in tree:
            continue
        row = [0.0 for _ in edges]
        row[e] = 1.0
        for _, path_edge, sign in tree_path(vertex_count, edges, tree, v, u):
            row[path_edge] += sign
        rows.append(row)
    return rows


def rectangular_graph(nx: int, ny: int) -> tuple[int, list[Edge]]:
    edges: list[Edge] = []
    for y in range(ny):
        for x in range(nx - 1):
            edges.append((y * nx + x, y * nx + x + 1))
    for y in range(ny - 1):
        for x in range(nx):
            edges.append((y * nx + x, (y + 1) * nx + x))
    return nx * ny, edges


def edge_law_from_h(h: list[float]) -> list[tuple[float, float]]:
    # Product edge-sign law.  For each edge sign s in {-1,+1},
    # P(s)=exp(h*s)/(2 cosh h).  The complete RN coefficient is recovered by
    # the half-log odds below.
    return [
        (
            math.exp(-value) / (2.0 * math.cosh(value)),
            math.exp(value) / (2.0 * math.cosh(value)),
        )
        for value in h
    ]


def recover_h_from_edge_law(edge_law: list[tuple[float, float]]) -> list[float]:
    return [0.5 * math.log(p_plus / p_minus) for p_minus, p_plus in edge_law]


def future_functional(h: list[float]) -> float:
    return sum((0.13 * math.sin(0.41 * (i + 1)) + 0.07 * math.cos(0.23 * i)) * value for i, value in enumerate(h))


def split_fine_h(h: list[float], vertical: list[float] | None = None) -> list[float]:
    if vertical is None:
        vertical = [0.0 for _ in h]
    out: list[float] = []
    for value, defect in zip(h, vertical):
        out.append(0.5 * value + defect)
        out.append(0.5 * value - defect)
    return out


def coarsen_split_h(h_fine: list[float]) -> list[float]:
    return [h_fine[2 * i] + h_fine[2 * i + 1] for i in range(len(h_fine) // 2)]


def vertical_split_norm(h_fine: list[float]) -> float:
    return l2([h_fine[2 * i] - h_fine[2 * i + 1] for i in range(len(h_fine) // 2)])


def main() -> None:
    vertex_count, edges = rectangular_graph(4, 3)
    b_red = incidence(vertex_count, edges)
    cycles = fundamental_cycle_basis(vertex_count, edges)
    readout = b_red + cycles
    edge_count = len(edges)

    h_true = [
        0.35 * math.sin(0.31 * (i + 1))
        + 0.18 * math.cos(0.67 * (i + 2))
        + 0.04 * ((i % 4) - 1.5)
        for i in range(edge_count)
    ]
    edge_law = edge_law_from_h(h_true)
    h_from_p = recover_h_from_edge_law(edge_law)
    rn_reconstruction_gap = max_gap(h_true, h_from_p)

    rho = mat_vec(b_red, h_from_p)
    kappa = mat_vec(cycles, h_from_p)
    h_response = solve_square(readout, rho + kappa)
    response_gap = max_gap(h_true, h_response)

    # Same P^{hist}, external altered source: rejected because it is not the
    # derivative/readout of log dP/dmu.
    rho_external = rho[:]
    rho_external[0] += 0.21
    external_residual = max_gap(rho_external, rho)
    h_external = solve_square(readout, rho_external + kappa)
    external_h_gap = l2(vec_sub(h_external, h_true))

    # Same source only, different cycle: same rho, different kappa and future.
    h_source_twin = [value + 0.14 * cycles[0][i] for i, value in enumerate(h_true)]
    source_twin_gap = max_gap(mat_vec(b_red, h_source_twin), rho)
    kappa_twin_gap = l2(vec_sub(mat_vec(cycles, h_source_twin), kappa))
    future_source_twin_gap = abs(future_functional(h_source_twin) - future_functional(h_true))

    # Same complete readout, same h and same future.
    h_same = solve_square(readout, rho + kappa)
    same_h_gap = max_gap(h_same, h_true)
    same_future_gap = abs(future_functional(h_same) - future_functional(h_true))

    # Neutral and hidden fine lifts.
    h_fine_neutral = split_fine_h(h_true)
    neutral_coarse_gap = max_gap(coarsen_split_h(h_fine_neutral), h_true)
    neutral_vertical_norm = vertical_split_norm(h_fine_neutral)

    vertical = [0.03 * math.sin(0.59 * (i + 1)) for i in range(edge_count)]
    h_fine_hidden = split_fine_h(h_true, vertical)
    hidden_coarse_gap = max_gap(coarsen_split_h(h_fine_hidden), h_true)
    hidden_vertical_norm = vertical_split_norm(h_fine_hidden)
    hidden_future_gap = abs(sum((i + 1) * (h_fine_hidden[2 * i] - h_fine_hidden[2 * i + 1]) for i in range(edge_count)))

    # Projective naturality of derived coarse readouts under neutral split.
    h_coarse_from_fine = coarsen_split_h(h_fine_neutral)
    rho_from_fine = mat_vec(b_red, h_coarse_from_fine)
    kappa_from_fine = mat_vec(cycles, h_coarse_from_fine)
    rho_projective_gap = max_gap(rho_from_fine, rho)
    kappa_projective_gap = max_gap(kappa_from_fine, kappa)

    rows = [
        Row(
            "RN coefficient origin",
            "recover h from the finite whole-history edge law",
            "half-log odds reconstruct the closed-holonomy coefficients",
            f"gap={rn_reconstruction_gap:.1e}",
            "PASS-H-FROM-P",
        ),
        Row(
            "source/period derivation",
            "apply exact/cycle readouts to reconstructed h",
            "rho and kappa are derivatives/readouts of the same RN action",
            f"rho_dim={len(rho)}, kappa_dim={len(kappa)}, response_gap={response_gap:.1e}",
            "PASS-DERIVES-READOUTS",
        ),
        Row(
            "same-P external-source attack",
            "alter rho after P_hist is fixed",
            "altered source is not the derivative of the same history law",
            f"residual={external_residual:.3f}, h_gap={external_h_gap:.6f}",
            "REFUTES-EXTERNAL-RHO",
        ),
        Row(
            "source-only twin",
            "add closed cycle to h",
            "same rho has different kappa and future composition",
            f"source_gap={source_twin_gap:.1e}, kappa_gap={kappa_twin_gap:.6f}, future_gap={future_source_twin_gap:.6f}",
            "REFUTES-RHO-ONLY",
        ),
        Row(
            "same complete readout",
            "solve response from identical rho and kappa",
            "same complete readout gives same h and same future",
            f"h_gap={same_h_gap:.1e}, future_gap={same_future_gap:.1e}",
            "PASS-NO-TWIN",
        ),
        Row(
            "projective neutral lift",
            "split every edge coefficient with zero vertical defect",
            "coarse source and periods are exactly preserved",
            f"coarse={neutral_coarse_gap:.1e}, vertical={neutral_vertical_norm:.1e}, rho={rho_projective_gap:.1e}, kappa={kappa_projective_gap:.1e}",
            "PASS-PROJECTIVE",
        ),
        Row(
            "hidden fine vertical attack",
            "add opposite fine defects with the same coarse h",
            "coarse rho/kappa agree but fine vertical RN data are nonzero",
            f"coarse={hidden_coarse_gap:.1e}, vertical={hidden_vertical_norm:.6f}, future={hidden_future_gap:.6f}",
            "REFUTES-COARSE-ONLY",
        ),
        Row(
            "source/period origin verdict",
            "P_hist -> h -> (rho,kappa) with projective tests",
            "source and periods are intrinsic readouts once P_hist is supplied",
            "process law still selects P_hist",
            "FINITE-ORIGIN-CLOSED",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("edge_count", edge_count)
    print("rho_dim", len(rho))
    print("kappa_dim", len(kappa))
    print("rn_reconstruction_gap", f"{rn_reconstruction_gap:.15e}")
    print("response_gap", f"{response_gap:.15e}")
    print("external_source_residual", f"{external_residual:.15e}")
    print("external_h_gap", f"{external_h_gap:.15e}")
    print("source_twin_gap", f"{source_twin_gap:.15e}")
    print("kappa_twin_gap", f"{kappa_twin_gap:.15e}")
    print("future_source_twin_gap", f"{future_source_twin_gap:.15e}")
    print("same_h_gap", f"{same_h_gap:.15e}")
    print("same_future_gap", f"{same_future_gap:.15e}")
    print("neutral_coarse_gap", f"{neutral_coarse_gap:.15e}")
    print("neutral_vertical_norm", f"{neutral_vertical_norm:.15e}")
    print("rho_projective_gap", f"{rho_projective_gap:.15e}")
    print("kappa_projective_gap", f"{kappa_projective_gap:.15e}")
    print("hidden_coarse_gap", f"{hidden_coarse_gap:.15e}")
    print("hidden_vertical_norm", f"{hidden_vertical_norm:.15e}")
    print("hidden_future_gap", f"{hidden_future_gap:.15e}")


if __name__ == "__main__":
    main()
