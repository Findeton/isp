#!/usr/bin/env python3
"""Paper 4 diagnostic Y: closed-holonomy dynamics campaign.

The readout-completeness theorem says which finite readouts separate
interface holonomy.  This diagnostic asks what can now count as dynamics.

Result:
  * consistency/vacuum principles select h=0 when no source/period data are
    supplied;
  * source-only, period-only, and scalar-work laws have twins;
  * the finite closed-holonomy response equation

        [B_red ; C] h = (source, cycle periods)

    is unique because the readout map has full rank;
  * this is a response equation, not yet a law selecting the physical
    source/period data themselves.
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


def vec_add(a: list[float], b: list[float], scale: float = 1.0) -> list[float]:
    return [x + scale * y for x, y in zip(a, b)]


def vec_sub(a: list[float], b: list[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def scale_to_norm(vector: list[float], target_norm: float) -> list[float]:
    norm = l2(vector)
    return [target_norm * value / norm for value in vector]


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


def main() -> None:
    vertex_count, edges = rectangular_graph(4, 3)
    b_red = incidence(vertex_count, edges)
    cycles = fundamental_cycle_basis(vertex_count, edges)
    readout = b_red + cycles
    edge_count = len(edges)
    rank_readout = rank(readout)
    kernel_dim = edge_count - rank_readout

    h_true = [
        0.41 * math.sin(0.37 * (i + 1))
        + 0.23 * math.cos(0.81 * (i + 2))
        + 0.05 * ((i % 3) - 1)
        for i in range(edge_count)
    ]
    source_true = mat_vec(b_red, h_true)
    period_true = mat_vec(cycles, h_true)
    rhs_true = source_true + period_true
    h_recovered = solve_square(readout, rhs_true)
    complete_gap = max_gap(h_true, h_recovered)

    vacuum = solve_square(readout, [0.0 for _ in range(edge_count)])
    vacuum_norm = l2(vacuum)

    cycle_defect = cycles[0]
    h_source_twin = vec_add(h_true, cycle_defect, scale=0.17)
    source_twin_gap = max_gap(mat_vec(b_red, h_true), mat_vec(b_red, h_source_twin))
    period_twin_gap = l2(vec_sub(mat_vec(cycles, h_true), mat_vec(cycles, h_source_twin)))
    h_source_twin_gap = l2(vec_sub(h_true, h_source_twin))

    cut_defect = b_red[0]
    h_period_twin = vec_add(h_true, cut_defect, scale=0.17)
    period_only_gap = max_gap(mat_vec(cycles, h_true), mat_vec(cycles, h_period_twin))
    source_only_gap = l2(vec_sub(mat_vec(b_red, h_true), mat_vec(b_red, h_period_twin)))

    source_only_rhs = source_true + [0.0 for _ in cycles]
    h_zero_period = solve_square(readout, source_only_rhs)
    source_only_recon_gap = max_gap(mat_vec(b_red, h_zero_period), source_true)
    lost_period_norm = l2(period_true)
    h_zero_period_gap = l2(vec_sub(h_true, h_zero_period))

    cycle_same_norm = scale_to_norm(cycle_defect, l2(cut_defect))
    scalar_work_gap = abs(l2(cut_defect) - l2(cycle_same_norm))
    scalar_readout_gap = l2(vec_sub(mat_vec(readout, cut_defect), mat_vec(readout, cycle_same_norm)))

    # Changing complete readout data gives a different unique solution.  This
    # is the boundary between response dynamics and a still-missing source law.
    rhs_changed = rhs_true[:]
    rhs_changed[len(source_true)] += 0.31
    h_changed = solve_square(readout, rhs_changed)
    changed_h_gap = l2(vec_sub(h_true, h_changed))
    changed_readout_gap = l2(vec_sub(rhs_true, rhs_changed))

    rows = [
        Row(
            "vacuum consistency",
            "set all source and cycle-period data to zero",
            "complete response equation selects h=0",
            f"norm={vacuum_norm:.1e}",
            "PASS-VACUUM",
        ),
        Row(
            "source-only no-go",
            "add a closed cycle to h",
            "source is unchanged but periods/future holonomy change",
            f"source_gap={source_twin_gap:.1e}, period_gap={period_twin_gap:.6f}, h_gap={h_source_twin_gap:.6f}",
            "REFUTES-SOURCE-ONLY-DYNAMICS",
        ),
        Row(
            "period-only no-go",
            "add a cut/gradient to h",
            "periods are unchanged but source changes",
            f"period_gap={period_only_gap:.1e}, source_gap={source_only_gap:.6f}",
            "REFUTES-PERIOD-ONLY-DYNAMICS",
        ),
        Row(
            "least-work trap",
            "solve source with all cycle periods silently set to zero",
            "same source is recovered but physical periods are erased",
            f"source_gap={source_only_recon_gap:.1e}, lost_period={lost_period_norm:.6f}, h_gap={h_zero_period_gap:.6f}",
            "REFUTES-UNSUPPLIED-PERIODS",
        ),
        Row(
            "scalar-work no-go",
            "match L2 work of cut and cycle defects",
            "same scalar work gives different complete readout",
            f"work_gap={scalar_work_gap:.1e}, readout_gap={scalar_readout_gap:.6f}",
            "REFUTES-SCALAR-DYNAMICS",
        ),
        Row(
            "complete response equation",
            "solve [B_red; C]h=(rho,kappa)",
            "source plus periods reconstruct h uniquely",
            f"rank={rank_readout}/{edge_count}, kernel={kernel_dim}, gap={complete_gap:.1e}",
            "PASS-UNIQUE-RESPONSE",
        ),
        Row(
            "source-law boundary",
            "change one physical period datum",
            "new data give a new unique solution; the response law does not select the data",
            f"readout_gap={changed_readout_gap:.6f}, h_gap={changed_h_gap:.6f}",
            "OPEN-SOURCE-LAW",
        ),
        Row(
            "closed-holonomy dynamics verdict",
            "selectors versus complete readout response",
            "finite dynamics closes as response to physical source/period data, not as universal h selection",
            "unique response / source law open",
            "FINITE-DYNAMICS-BOUNDARY",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("edge_count", edge_count)
    print("vertex_count", vertex_count)
    print("cycle_count", len(cycles))
    print("rank_readout", rank_readout)
    print("kernel_dim", kernel_dim)
    print("complete_reconstruction_gap", f"{complete_gap:.15e}")
    print("vacuum_norm", f"{vacuum_norm:.15e}")
    print("source_only_source_gap", f"{source_twin_gap:.15e}")
    print("source_only_period_gap", f"{period_twin_gap:.15e}")
    print("source_only_h_gap", f"{h_source_twin_gap:.15e}")
    print("period_only_period_gap", f"{period_only_gap:.15e}")
    print("period_only_source_gap", f"{source_only_gap:.15e}")
    print("least_work_source_gap", f"{source_only_recon_gap:.15e}")
    print("least_work_lost_period_norm", f"{lost_period_norm:.15e}")
    print("least_work_h_gap", f"{h_zero_period_gap:.15e}")
    print("scalar_work_gap", f"{scalar_work_gap:.15e}")
    print("scalar_readout_gap", f"{scalar_readout_gap:.15e}")
    print("changed_readout_gap", f"{changed_readout_gap:.15e}")
    print("changed_h_gap", f"{changed_h_gap:.15e}")


if __name__ == "__main__":
    main()
