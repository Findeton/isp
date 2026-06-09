"""
v6 Paper 3 section 53: origin closure for L_D, rho_D, and exactness.

Question:
    After section 52 finds the relational field equation

        L_D S_D = rho_D,

    can the sealed-diamond kinematics intrinsically derive L_D, rho_D, and
    no-silent-seam exactness?

Finite answer:
    No, not from kinematics/symmetry/composition alone.

    * Invariant Laplacians are weighted sums over edge orbits.  One edge orbit
      leaves a scale; several edge orbits leave weight ratios.
    * Invariant zero-sum sources are weighted sums over vertex orbits.  A
      transitive vertex action gives only rho=0; nontrivial orbit structure
      leaves amplitudes.
    * Exactness removes cycle currents, but on graphs with cycles it is an
      extra condition unless the physical process derives it.

    Thus the Hodge/Poisson equation is the right relational form, but the full
    Branch-A law is equivalent to deriving the triple (L_D, rho_D, exactness)
    from the sealed physical process.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp


Vector = list[float]
Matrix = list[list[float]]
Edge = tuple[int, int, float]


@dataclass(frozen=True)
class OriginAudit:
    target: str
    invariant_data: str
    positive_result: str
    obstruction: str
    value: str
    verdict: str


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def law_from_action(action: Vector) -> Vector:
    return normalize([exp(-value) for value in action])


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def laplacian(n: int, edges: list[Edge]) -> Matrix:
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for u, v, weight in edges:
        matrix[u][u] += weight
        matrix[v][v] += weight
        matrix[u][v] -= weight
        matrix[v][u] -= weight
    return matrix


def mat_vec(matrix: Matrix, vector: Vector) -> Vector:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def gaussian_solve(matrix: Matrix, rhs: Vector) -> Vector:
    n = len(rhs)
    a = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        if abs(a[pivot][col]) < 1.0e-12:
            raise ValueError("singular matrix")
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        for j in range(col, n + 1):
            a[col][j] /= scale
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            for j in range(col, n + 1):
                a[row][j] -= factor * a[col][j]
    return [a[i][n] for i in range(n)]


def solve_mean_zero(l_matrix: Matrix, rho: Vector) -> Vector:
    n = len(rho)
    matrix = [row[:] for row in l_matrix]
    rhs = rho[:]
    matrix[-1] = [1.0] * n
    rhs[-1] = 0.0
    return gaussian_solve(matrix, rhs)


def source_delta(n: int, marked: int, amplitude: float = 1.0) -> Vector:
    source = [-amplitude / n for _ in range(n)]
    source[marked] += amplitude
    return source


def reflection_path_edges(boundary_weight: float, interior_weight: float) -> list[Edge]:
    return [
        (0, 1, boundary_weight),
        (1, 2, interior_weight),
        (2, 3, interior_weight),
        (3, 4, boundary_weight),
    ]


def edge_orbit_weight_span() -> float:
    laws = []
    rho = source_delta(5, 0)
    for boundary_weight, interior_weight in ((1.0, 1.0), (2.0, 1.0), (1.0, 2.0)):
        action = solve_mean_zero(laplacian(5, reflection_path_edges(boundary_weight, interior_weight)), rho)
        laws.append(law_from_action(action))
    return max(l1(a, b) for a in laws for b in laws)


def edge_scale_span() -> float:
    base_edges = reflection_path_edges(1.0, 1.0)
    rho = source_delta(5, 0)
    laws = []
    for scale in (0.5, 1.0, 2.0):
        edges = [(u, v, scale * weight) for u, v, weight in base_edges]
        action = solve_mean_zero(laplacian(5, edges), rho)
        laws.append(law_from_action(action))
    return max(l1(a, b) for a in laws for b in laws)


def vertex_orbit_source_span() -> float:
    # Reflection orbits on a five-point path are {0,4}, {1,3}, {2}.  Zero-sum
    # orbit-constant sources form a two-dimensional family.
    edges = reflection_path_edges(1.0, 1.0)
    sources = [
        [0.5, -0.25, -0.5, -0.25, 0.5],
        [0.2, 0.3, -1.0, 0.3, 0.2],
        [0.8, -0.6, -0.4, -0.6, 0.8],
    ]
    laws = [law_from_action(solve_mean_zero(laplacian(5, edges), source)) for source in sources]
    return max(l1(a, b) for a in laws for b in laws)


def marked_source_amplitude_span() -> float:
    edges = reflection_path_edges(1.0, 1.0)
    laws = []
    for amplitude in (0.5, 1.0, 2.0):
        action = solve_mean_zero(laplacian(5, edges), source_delta(5, 2, amplitude))
        laws.append(law_from_action(action))
    return max(l1(a, b) for a in laws for b in laws)


def transitive_source_dimension() -> int:
    # On a transitive vertex action, an invariant source is constant.  Zero sum
    # forces the constant to vanish.
    return 0


def cycle_rank(n: int, edge_count: int, components: int = 1) -> int:
    return edge_count - n + components


def divergence(n: int, edges: list[Edge], current: Vector) -> Vector:
    result = [0.0 for _ in range(n)]
    for (u, v, weight), value in zip(edges, current):
        result[u] -= weight * value
        result[v] += weight * value
    return result


def cycle_current_invisibility() -> tuple[float, float]:
    n = 5
    edges = [(i, (i + 1) % n, 1.0) for i in range(n)]
    current_a = [0.0] * n
    current_b = [1.0] * n
    div_gap = max(abs(a - b) for a, b in zip(divergence(n, edges, current_a), divergence(n, edges, current_b)))
    loop_gap = sum(current_b) - sum(current_a)
    return div_gap, loop_gap


def complete_graph_scale_span() -> float:
    n = 5
    base_edges = [(i, j, 1.0) for i in range(n) for j in range(i + 1, n)]
    rho = source_delta(n, 0)
    laws = []
    for scale in (0.5, 1.0, 2.0):
        edges = [(u, v, scale * weight) for u, v, weight in base_edges]
        action = solve_mean_zero(laplacian(n, edges), rho)
        laws.append(law_from_action(action))
    return max(l1(a, b) for a in laws for b in laws)


def minimum_complexity_choice_norm() -> float:
    # If no source is derived, minimizing action/work complexity selects the
    # zero action.  This is unique but eventless.
    return 0.0


def possible_binary_laws(n: int) -> int:
    return 2 ** n


def audits() -> list[OriginAudit]:
    div_gap, loop_gap = cycle_current_invisibility()
    return [
        OriginAudit(
            "edge-orbit Laplacian",
            "reflection-invariant path",
            "weights constant on edge orbits",
            "orbit weights remain free",
            f"P span={edge_orbit_weight_span():.3f}",
            "FAIL-L-WEIGHTS",
        ),
        OriginAudit(
            "one edge orbit",
            "edge-transitive graph",
            "only one weight ratio",
            "overall scale remains free",
            f"P span={edge_scale_span():.3f}",
            "FAIL-L-SCALE",
        ),
        OriginAudit(
            "complete graph attempt",
            "maximal invariant adjacency",
            "canonical graph shape",
            "nonlocal and scale still free",
            f"P span={complete_graph_scale_span():.3f}",
            "FAIL-CANONICAL-GRAPH",
        ),
        OriginAudit(
            "vertex-orbit source",
            "reflection-invariant source",
            "source constant on vertex orbits",
            "orbit amplitudes remain free",
            f"P span={vertex_orbit_source_span():.3f}",
            "FAIL-RHO-ORBIT",
        ),
        OriginAudit(
            "transitive source",
            "all vertices indistinguishable",
            "zero-sum invariant source is zero",
            "no nontrivial event",
            f"source dim={transitive_source_dimension()}",
            "FAIL-TRIVIAL-RHO",
        ),
        OriginAudit(
            "marked source",
            "event support supplied",
            "delta_x-uniform source shape",
            "amplitude remains free",
            f"P span={marked_source_amplitude_span():.3f}",
            "FAIL-RHO-AMPLITUDE",
        ),
        OriginAudit(
            "cycle exactness",
            "graph with cycles",
            f"cycle rank={cycle_rank(5, 5)}",
            "cycle current invisible to divergence",
            f"div gap={div_gap:.1e}, loop gap={loop_gap:.1f}",
            "FAIL-EXACTNESS-ORIGIN",
        ),
        OriginAudit(
            "tree exactness",
            "cycle-free graph",
            "no harmonic cycle current",
            "tree choice and weights remain free",
            f"possible states={possible_binary_laws(4)}",
            "COND-NOT-DYNAMICS",
        ),
        OriginAudit(
            "minimum complexity",
            "minimize ||S|| or work without source",
            "unique zero action",
            "selects eventless law",
            f"||S||={minimum_complexity_choice_norm():.1f}",
            "FAIL-TRIVIAL",
        ),
        OriginAudit(
            "full closure packet",
            "intrinsic L_D, rho_D, exactness",
            "then S_D is unique",
            "packet is exactly missing dynamics",
            "conditional theorem",
            "THM-CLOSED-IF-PACKET",
        ),
        OriginAudit(
            "origin no-go",
            "sealed kinematics alone",
            "restricts to invariant cones",
            "does not select point in cones",
            "families survive",
            "THM-ORIGIN-NO-GO",
        ),
    ]


def print_audits(rows: list[OriginAudit]) -> None:
    print("L_D/rho_D/exactness origin closure campaign")
    print("-------------------------------------------")
    print(
        "target                    invariant data                 positive result                  "
        "obstruction                         value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.invariant_data:30s} "
            f"{row.positive_result:32s} "
            f"{row.obstruction:35s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 53: L_D/rho_D/exactness origin closure campaign")
    print("=" * 150)
    rows = audits()
    print_audits(rows)
    print()
    print("VERDICT")
    print("-------")
    print("The relational field equation is closed only if the sealed physical")
    print("process derives the complete packet (L_D, rho_D, exactness).  Finite")
    print("sealed kinematics and symmetry do not derive that packet.  They restrict")
    print("L_D to edge-orbit weights, rho_D to vertex-orbit amplitudes, and cycle")
    print("currents to a harmonic sector, but they do not select the weights,")
    print("amplitudes, or exactness condition.  Without a further physical process")
    print("law, Branch A-full remains open and Branch B is the honest fallback.")


if __name__ == "__main__":
    main()
