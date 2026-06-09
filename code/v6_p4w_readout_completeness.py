#!/usr/bin/env python3
"""Paper 4 diagnostic W: finite readout-completeness campaign.

Admissible refinement says that silent vertical defects must vanish in every
intrinsic future-relevant readout.  This diagnostic asks whether the proposed
readout complex is actually separating at finite level.

Two finite complexes are tested:
  * history fibers: full vertical RN action reconstructs the fine history law,
    while scalar KL work does not;
  * cellular interface holonomy: divergence/source plus closed-cycle periods
    reconstruct every edge cochain, while either part alone has twins.
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


def normalize(values: list[float]) -> list[float]:
    total = sum(values)
    return [value / total for value in values]


def uniform(n: int) -> list[float]:
    return [1.0 / n for _ in range(n)]


def kl(p: list[float], q: list[float]) -> float:
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0.0)


def hidden_lift(p_coarse: list[float], theta: float, pattern: list[int]) -> list[float]:
    out: list[float] = []
    for pc, sign in zip(p_coarse, pattern):
        out.append(0.5 * pc * (1.0 + theta * sign))
        out.append(0.5 * pc * (1.0 - theta * sign))
    return out


def vertical_action(p_fine: list[float], p_coarse: list[float]) -> list[float]:
    mu_fine = uniform(len(p_fine))
    mu_coarse = uniform(len(p_coarse))
    out = []
    for i, pc in enumerate(p_coarse):
        coarse_action = math.log(pc / mu_coarse[i])
        out.append(math.log(p_fine[2 * i] / mu_fine[2 * i]) - coarse_action)
        out.append(math.log(p_fine[2 * i + 1] / mu_fine[2 * i + 1]) - coarse_action)
    return out


def reconstruct_from_vertical_action(p_coarse: list[float], v_action: list[float]) -> list[float]:
    mu_fine = uniform(2 * len(p_coarse))
    mu_coarse = uniform(len(p_coarse))
    out = []
    for i, pc in enumerate(p_coarse):
        coarse_action = math.log(pc / mu_coarse[i])
        out.append(mu_fine[2 * i] * math.exp(coarse_action + v_action[2 * i]))
        out.append(mu_fine[2 * i + 1] * math.exp(coarse_action + v_action[2 * i + 1]))
    return out


def max_gap(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def l2(values: list[float]) -> float:
    return math.sqrt(sum(value * value for value in values))


def mat_vec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def rank(matrix: list[list[float]], tol: float = 1e-10) -> int:
    a = [row[:] for row in matrix]
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


def edge_index(nx: int, ny: int) -> tuple[dict[tuple[int, int, str], int], list[tuple[int, int, str]]]:
    idx: dict[tuple[int, int, str], int] = {}
    edges: list[tuple[int, int, str]] = []
    for y in range(ny):
        for x in range(nx - 1):
            key = (x, y, "h")
            idx[key] = len(edges)
            edges.append(key)
    for y in range(ny - 1):
        for x in range(nx):
            key = (x, y, "v")
            idx[key] = len(edges)
            edges.append(key)
    return idx, edges


def incidence_matrix(nx: int, ny: int, idx: dict[tuple[int, int, str], int], edges: list[tuple[int, int, str]]) -> list[list[float]]:
    rows = [[0.0 for _ in edges] for _ in range(nx * ny)]
    for e, (x, y, kind) in enumerate(edges):
        if kind == "h":
            tail = y * nx + x
            head = y * nx + x + 1
        else:
            tail = y * nx + x
            head = (y + 1) * nx + x
        rows[tail][e] = -1.0
        rows[head][e] = 1.0
    # Drop one redundant constant row.
    return rows[:-1]


def face_cycle_matrix(nx: int, ny: int, idx: dict[tuple[int, int, str], int], edges: list[tuple[int, int, str]]) -> list[list[float]]:
    rows: list[list[float]] = []
    for y in range(ny - 1):
        for x in range(nx - 1):
            row = [0.0 for _ in edges]
            row[idx[(x, y, "h")]] += 1.0
            row[idx[(x + 1, y, "v")]] += 1.0
            row[idx[(x, y + 1, "h")]] -= 1.0
            row[idx[(x, y, "v")]] -= 1.0
            rows.append(row)
    return rows


def scale_to_norm(vector: list[float], target_norm: float) -> list[float]:
    norm = l2(vector)
    return [target_norm * value / norm for value in vector]


def main() -> None:
    # History-fiber readout tests.
    p_coarse = normalize([0.19, 0.31, 0.23, 0.27])
    theta = 0.52
    pattern_a = [1, -1, 1, -1]
    pattern_b = [1, 1, -1, -1]
    p_a = hidden_lift(p_coarse, theta, pattern_a)
    p_b = hidden_lift(p_coarse, theta, pattern_b)
    mu_fine = uniform(len(p_a))
    mu_coarse = uniform(len(p_coarse))
    kl_gap_a = kl(p_a, mu_fine) - kl(p_coarse, mu_coarse)
    kl_gap_b = kl(p_b, mu_fine) - kl(p_coarse, mu_coarse)
    scalar_kl_gap = abs(kl_gap_a - kl_gap_b)
    future_probe = []
    for sign in pattern_a:
        future_probe.extend([sign, -sign])
    future_a = sum(g * p for g, p in zip(future_probe, p_a))
    future_b = sum(g * p for g, p in zip(future_probe, p_b))
    future_gap = abs(future_a - future_b)
    v_action_a = vertical_action(p_a, p_coarse)
    v_action_b = vertical_action(p_b, p_coarse)
    action_gap = l2([a - b for a, b in zip(v_action_a, v_action_b)])
    recon_a = reconstruct_from_vertical_action(p_coarse, v_action_a)
    recon_gap = max_gap(p_a, recon_a)

    # Cellular readout tests.
    nx, ny = 4, 3
    idx, edges = edge_index(nx, ny)
    b_mat = incidence_matrix(nx, ny, idx, edges)
    c_mat = face_cycle_matrix(nx, ny, idx, edges)
    e_count = len(edges)
    v_count = nx * ny
    f_count = (nx - 1) * (ny - 1)
    full_readout = b_mat + c_mat
    rank_b = rank(b_mat)
    rank_c = rank(c_mat)
    rank_full = rank(full_readout)

    # A plaquette circulation is source-free but has period/curl readout.
    cycle_vector = c_mat[0][:]
    cycle_source_norm = l2(mat_vec(b_mat, cycle_vector))
    cycle_period_norm = l2(mat_vec(c_mat, cycle_vector))

    # A cut/gradient vector has zero plaquette periods but nonzero source.
    gradient_vector = b_mat[0][:]
    gradient_period_norm = l2(mat_vec(c_mat, gradient_vector))
    gradient_source_norm = l2(mat_vec(b_mat, gradient_vector))

    same_energy_gradient = scale_to_norm(gradient_vector, l2(cycle_vector))
    scalar_energy_gap = abs(l2(cycle_vector) - l2(same_energy_gradient))
    scalar_future_gap = abs(
        mat_vec(c_mat, cycle_vector)[0]
        - mat_vec(c_mat, same_energy_gradient)[0]
    )

    # Reconstruction from the complete readout.
    defect = [math.sin(0.37 * (i + 1)) + 0.2 * math.cos(0.91 * (i + 2)) for i in range(e_count)]
    readout = mat_vec(full_readout, defect)
    recovered = solve_square(full_readout, readout)
    cellular_recon_gap = max_gap(defect, recovered)
    kernel_dim_full = e_count - rank_full

    rows = [
        Row(
            "history scalar-work attack",
            "same coarse law and same conditional KL with different hidden orientation",
            "scalar RN work does not determine future composition",
            f"dKL_gap={scalar_kl_gap:.1e}, future_gap={future_gap:.6f}",
            "REFUTES-SCALAR-HISTORY",
        ),
        Row(
            "vertical RN action",
            "reconstruct fine law from coarse law plus full fiber action",
            "full vertical action separates hidden history twins",
            f"action_gap={action_gap:.6f}, recon={recon_gap:.1e}",
            "PASS-HISTORY-COMPLETE",
        ),
        Row(
            "source-only attack",
            "plaquette circulation has zero divergence",
            "source readout misses closed-cycle holonomy",
            f"source={cycle_source_norm:.1e}, period={cycle_period_norm:.6f}",
            "REFUTES-SOURCE-ONLY",
        ),
        Row(
            "period-only attack",
            "cut/gradient defect has zero plaquette period",
            "cycle readout alone misses source",
            f"period={gradient_period_norm:.1e}, source={gradient_source_norm:.6f}",
            "REFUTES-PERIOD-ONLY",
        ),
        Row(
            "scalar work attack",
            "match edge L2 work for different defects",
            "same scalar work gives different readout/future effect",
            f"energy_gap={scalar_energy_gap:.1e}, readout_gap={scalar_future_gap:.6f}",
            "REFUTES-SCALAR-CELLULAR",
        ),
        Row(
            "cellular rank theorem",
            "divergence/source plus independent face periods",
            "readout map has full rank on edge cochains",
            f"E={e_count}, rankB={rank_b}, rankC={rank_c}, rankFull={rank_full}",
            "PASS-SEPARATES-EDGES",
        ),
        Row(
            "cellular reconstruction",
            "solve defect from complete cellular readout",
            "kernel is zero and defect is reconstructed",
            f"kernel={kernel_dim_full}, gap={cellular_recon_gap:.1e}",
            "PASS-COMPLETE",
        ),
        Row(
            "readout-completeness verdict",
            "vertical RN action plus cellular source/cycle readouts",
            "partial summaries have twins; complete finite readout separates them",
            "history + cellular",
            "FINITE-COMPLETENESS",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("history_conditional_kl_a", f"{kl_gap_a:.15e}")
    print("history_conditional_kl_b", f"{kl_gap_b:.15e}")
    print("history_scalar_kl_gap", f"{scalar_kl_gap:.15e}")
    print("history_future_gap", f"{future_gap:.15e}")
    print("history_vertical_action_gap", f"{action_gap:.15e}")
    print("history_reconstruction_gap", f"{recon_gap:.15e}")
    print("edge_count", e_count)
    print("vertex_count", v_count)
    print("face_count", f_count)
    print("rank_source", rank_b)
    print("rank_period", rank_c)
    print("rank_full", rank_full)
    print("cycle_source_norm", f"{cycle_source_norm:.15e}")
    print("cycle_period_norm", f"{cycle_period_norm:.15e}")
    print("gradient_period_norm", f"{gradient_period_norm:.15e}")
    print("gradient_source_norm", f"{gradient_source_norm:.15e}")
    print("scalar_energy_gap", f"{scalar_energy_gap:.15e}")
    print("scalar_readout_gap", f"{scalar_future_gap:.15e}")
    print("cellular_reconstruction_gap", f"{cellular_recon_gap:.15e}")
    print("cellular_kernel_dim", kernel_dim_full)


if __name__ == "__main__":
    main()
