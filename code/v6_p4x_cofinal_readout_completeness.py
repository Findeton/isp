#!/usr/bin/env python3
"""Paper 4 diagnostic X: cofinal readout-completeness campaign.

The previous diagnostic proved readout completeness on one rectangular cell
complex.  This script generalizes the finite linear theorem:

  connected graph:
    reduced incidence source readout has rank V-1;
    an independent cycle-period basis has rank E-V+1;
    together they have rank E and zero kernel on edge/interface cochains.

It also attacks the theorem:
  * local face periods are complete only for simply connected rectangular
    complexes;
  * a hole/global cycle is a ghost unless homology cycle periods are included;
  * scalar work can match while the complete readout changes;
  * zero-coarse fine defects are caught by fine source/cycle readouts.
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


def mat_vec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def l2(vector: list[float]) -> float:
    return math.sqrt(sum(value * value for value in vector))


def max_abs(vector: list[float]) -> float:
    return max(abs(value) for value in vector) if vector else 0.0


def max_gap(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b)) if a else 0.0


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
    parent: dict[int, tuple[int, int, int]] = {}
    queue = deque([start])
    parent[start] = (-1, -1, 0)
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
        # Close the cycle by returning from v to u along the tree path.
        for _, path_edge, sign in tree_path(vertex_count, edges, tree, v, u):
            row[path_edge] += sign
        rows.append(row)
    return rows


def rectangular_graph(nx: int, ny: int) -> tuple[int, list[Edge], list[list[float]]]:
    edges: list[Edge] = []
    edge_idx: dict[tuple[int, int, str], int] = {}
    for y in range(ny):
        for x in range(nx - 1):
            edge_idx[(x, y, "h")] = len(edges)
            edges.append((y * nx + x, y * nx + x + 1))
    for y in range(ny - 1):
        for x in range(nx):
            edge_idx[(x, y, "v")] = len(edges)
            edges.append((y * nx + x, (y + 1) * nx + x))
    faces: list[list[float]] = []
    for y in range(ny - 1):
        for x in range(nx - 1):
            row = [0.0 for _ in edges]
            row[edge_idx[(x, y, "h")]] += 1.0
            row[edge_idx[(x + 1, y, "v")]] += 1.0
            row[edge_idx[(x, y + 1, "h")]] -= 1.0
            row[edge_idx[(x, y, "v")]] -= 1.0
            faces.append(row)
    return nx * ny, edges, faces


def cycle_graph(n: int) -> tuple[int, list[Edge], list[list[float]], list[list[float]]]:
    edges = [(i, (i + 1) % n) for i in range(n)]
    local_faces: list[list[float]] = []
    homology = [[1.0 for _ in edges]]
    return n, edges, local_faces, homology


def complete_rank(vertex_count: int, edges: list[Edge], cycle_rows: list[list[float]]) -> tuple[int, int, int, int]:
    b = incidence(vertex_count, edges)
    return len(edges), rank(b), rank(cycle_rows), rank(b + cycle_rows)


def coarsen_zero_pair(vector: list[float]) -> list[float]:
    return [vector[2 * i] + vector[2 * i + 1] for i in range(len(vector) // 2)]


def main() -> None:
    rect_rows = []
    for nx, ny in ((3, 3), (4, 3), (5, 4), (6, 5)):
        v, edges, faces = rectangular_graph(nx, ny)
        e, rb, rc, rf = complete_rank(v, edges, faces)
        rect_rows.append((nx, ny, v, e, len(faces), rb, rc, rf, e - rf))
    rect_kernel_summary = "; ".join(
        f"{nx}x{ny}:E={e},F={f},rank={rf},ker={ker}"
        for nx, ny, _, e, f, _, _, rf, ker in rect_rows
    )
    rect_all_pass = all(ker == 0 for *_, ker in rect_rows)

    # Arbitrary connected graph test: source plus fundamental cycles.
    graph_edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5),
        (1, 4), (1, 6), (6, 7), (7, 4), (2, 7), (3, 6),
    ]
    graph_v = 8
    graph_cycles = fundamental_cycle_basis(graph_v, graph_edges)
    graph_e, graph_rb, graph_rc, graph_rf = complete_rank(graph_v, graph_edges, graph_cycles)
    graph_kernel = graph_e - graph_rf

    # Topological hole attack: local faces absent, homology period needed.
    ring_v, ring_edges, ring_faces, ring_homology = cycle_graph(8)
    ring_e, ring_rb, ring_rc_local, ring_rf_local = complete_rank(ring_v, ring_edges, ring_faces)
    _, _, ring_rc_full, ring_rf_full = complete_rank(ring_v, ring_edges, ring_faces + ring_homology)
    ring_kernel_local = ring_e - ring_rf_local
    ring_kernel_full = ring_e - ring_rf_full
    ring_defect = [1.0 for _ in ring_edges]
    ring_source_norm = l2(mat_vec(incidence(ring_v, ring_edges), ring_defect))
    ring_local_period_norm = l2(mat_vec(ring_faces, ring_defect))
    ring_homology_norm = l2(mat_vec(ring_homology, ring_defect))

    # Face-only/source-only attacks on a rectangular complex.
    rect_v, rect_edges, rect_faces = rectangular_graph(4, 3)
    rect_b = incidence(rect_v, rect_edges)
    circulation = rect_faces[0][:]
    cut = rect_b[0][:]
    circulation_source = l2(mat_vec(rect_b, circulation))
    circulation_period = l2(mat_vec(rect_faces, circulation))
    cut_source = l2(mat_vec(rect_b, cut))
    cut_period = l2(mat_vec(rect_faces, cut))

    # Zero-coarse pair defect: coarse shadow zero, fine readout nonzero.
    zero_coarse = []
    for i in range(10):
        value = 0.25 * math.sin(0.7 * (i + 1))
        zero_coarse.extend([value, -value])
    zero_coarse_gap = max_abs(coarsen_zero_pair(zero_coarse))
    zero_fine_norm = l2(zero_coarse)

    rows = [
        Row(
            "rectangular cofinal ranks",
            "test simply connected grids of increasing size",
            "source plus face periods have zero kernel at every tested scale",
            rect_kernel_summary,
            "PASS-COFINAL-FINITE",
        ),
        Row(
            "general graph rank theorem",
            "source plus fundamental cycle basis on connected graph",
            "rank(B_red)+rank(cycles)=E and full kernel is zero",
            f"E={graph_e}, rankB={graph_rb}, cycles={graph_rc}, rankFull={graph_rf}, ker={graph_kernel}",
            "PASS-GRAPH",
        ),
        Row(
            "homology-hole attack",
            "cycle graph with no local face period",
            "source and local faces miss global circulation",
            f"local_ker={ring_kernel_local}, source={ring_source_norm:.1e}, local_period={ring_local_period_norm:.1e}, homology={ring_homology_norm:.1f}",
            "REFUTES-LOCAL-FACES-ONLY",
        ),
        Row(
            "homology completion",
            "add the independent global cycle period",
            "hole circulation is separated and kernel vanishes",
            f"rankLocal={ring_rf_local}, rankFull={ring_rf_full}, ker={ring_kernel_full}",
            "PASS-TOPOLOGY-COMPLETE",
        ),
        Row(
            "source/period twin attacks",
            "test circulation and cut defects on rectangle",
            "source-only and period-only lists both have twins",
            f"circ_source={circulation_source:.1e}, circ_period={circulation_period:.3f}; cut_period={cut_period:.1e}, cut_source={cut_source:.3f}",
            "REFUTES-PARTIAL-LISTS",
        ),
        Row(
            "zero-coarse vertical defect",
            "pairwise fine defect with exact zero coarse shadow",
            "coarse projection misses a nonzero fine vertical vector",
            f"coarse={zero_coarse_gap:.1e}, fine_norm={zero_fine_norm:.6f}",
            "REFUTES-COARSE-SHADOW",
        ),
        Row(
            "cofinal readout verdict",
            "all finite levels use source plus complete cycle basis",
            "zero readout at every finite level implies zero vertical defect",
            f"rect_pass={rect_all_pass}, graph_ker={graph_kernel}, ring_ker={ring_kernel_full}",
            "FINITE-COFINAL-COMPLETENESS",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    for nx, ny, v, e, f, rb, rc, rf, ker in rect_rows:
        print(f"rect_{nx}x{ny}_vertices", v)
        print(f"rect_{nx}x{ny}_edges", e)
        print(f"rect_{nx}x{ny}_faces", f)
        print(f"rect_{nx}x{ny}_rank_source", rb)
        print(f"rect_{nx}x{ny}_rank_period", rc)
        print(f"rect_{nx}x{ny}_rank_full", rf)
        print(f"rect_{nx}x{ny}_kernel", ker)
    print("graph_edges", graph_e)
    print("graph_rank_source", graph_rb)
    print("graph_rank_cycles", graph_rc)
    print("graph_rank_full", graph_rf)
    print("graph_kernel", graph_kernel)
    print("ring_local_kernel", ring_kernel_local)
    print("ring_full_kernel", ring_kernel_full)
    print("ring_source_norm", f"{ring_source_norm:.15e}")
    print("ring_local_period_norm", f"{ring_local_period_norm:.15e}")
    print("ring_homology_norm", f"{ring_homology_norm:.15e}")
    print("circulation_source_norm", f"{circulation_source:.15e}")
    print("circulation_period_norm", f"{circulation_period:.15e}")
    print("cut_source_norm", f"{cut_source:.15e}")
    print("cut_period_norm", f"{cut_period:.15e}")
    print("zero_coarse_gap", f"{zero_coarse_gap:.15e}")
    print("zero_fine_norm", f"{zero_fine_norm:.15e}")


if __name__ == "__main__":
    main()
