"""
v6 Paper 3 section 52: relational record field equation campaign.

Question:
    Can the whole-diamond action S_D satisfy an intrinsic relational field
    equation F_D(S_D)=0?

Finite answer:
    Yes conditionally, and no as full closure from structure alone.

    The finite relational equation is the sealed-diamond Hodge/Poisson
    equation

        L_D S_D = rho_D,

    where L_D is the graph Laplacian of allowed sealed-diamond changes and
    rho_D is the zero-sum modular defect source.  This equation is relational:
    it uses only the change graph, its weights/inner product, and the defect
    source.  On a connected finite change graph it has a unique solution up to
    additive constants whenever sum rho_D=0.  It is the Euler equation for
    minimal record-work energy.

    But this still does not close Branch A-full unless L_D and rho_D are
    derived by the sealed physical process.  The campaign exhibits surviving
    families: same support with different source amplitude, same boundary with
    different hidden weights, and divergence-free cycle currents with the same
    local source.  The relational equation is therefore the right form of the
    missing law, not yet a derivation of the law.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp


Matrix = list[list[float]]
Vector = list[float]
Edge = tuple[int, int, float]


@dataclass(frozen=True)
class Graph:
    n: int
    edges: list[Edge]


@dataclass(frozen=True)
class FieldAudit:
    target: str
    relational_object: str
    positive_result: str
    obstruction: str
    diagnostic_value: str
    verdict: str


def path_graph(n: int, weights: list[float] | None = None) -> Graph:
    if weights is None:
        weights = [1.0] * (n - 1)
    return Graph(n, [(i, i + 1, weights[i]) for i in range(n - 1)])


def cycle_graph(n: int, weight: float = 1.0) -> Graph:
    return Graph(n, [(i, (i + 1) % n, weight) for i in range(n)])


def laplacian(graph: Graph) -> Matrix:
    matrix = [[0.0 for _ in range(graph.n)] for _ in range(graph.n)]
    for u, v, weight in graph.edges:
        matrix[u][u] += weight
        matrix[v][v] += weight
        matrix[u][v] -= weight
        matrix[v][u] -= weight
    return matrix


def mat_vec(matrix: Matrix, vector: Vector) -> Vector:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def dot(left: Vector, right: Vector) -> float:
    return sum(a * b for a, b in zip(left, right))


def norm_inf(vector: Vector) -> float:
    return max(abs(value) for value in vector)


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def law_from_action(action: Vector) -> Vector:
    return normalize([exp(-value) for value in action])


def gaussian_solve(matrix: Matrix, rhs: Vector) -> Vector:
    n = len(rhs)
    a = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        if abs(a[pivot][col]) < 1.0e-12:
            raise ValueError("singular matrix in gaussian_solve")
        a[col], a[pivot] = a[pivot], a[col]
        pivot_value = a[col][col]
        for j in range(col, n + 1):
            a[col][j] /= pivot_value
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            if abs(factor) < 1.0e-18:
                continue
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


def residual(l_matrix: Matrix, action: Vector, rho: Vector) -> float:
    return norm_inf([a - b for a, b in zip(mat_vec(l_matrix, action), rho)])


def energy(l_matrix: Matrix, action: Vector, rho: Vector) -> float:
    return 0.5 * dot(action, mat_vec(l_matrix, action)) - dot(rho, action)


def gradient(graph: Graph, action: Vector) -> Vector:
    return [action[v] - action[u] for u, v, _ in graph.edges]


def divergence(graph: Graph, edge_current: Vector) -> Vector:
    result = [0.0 for _ in range(graph.n)]
    for (u, v, weight), current in zip(graph.edges, edge_current):
        result[u] -= weight * current
        result[v] += weight * current
    return result


def cycle_work(edge_current: Vector) -> float:
    return sum(edge_current)


def jacobi_eigenvalues(matrix: Matrix) -> Vector:
    n = len(matrix)
    a = [row[:] for row in matrix]
    for _ in range(200):
        p, q = 0, 1
        max_off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > max_off:
                    max_off = abs(a[i][j])
                    p, q = i, j
        if max_off < 1.0e-12:
            break
        if abs(a[p][p] - a[q][q]) < 1.0e-18:
            c = s = 2.0 ** -0.5
        else:
            tau = (2.0 * a[p][q]) / (a[q][q] - a[p][p])
            t = tau / (1.0 + (1.0 + tau * tau) ** 0.5)
            c = 1.0 / (1.0 + t * t) ** 0.5
            s = t * c
        app = c * c * a[p][p] - 2.0 * s * c * a[p][q] + s * s * a[q][q]
        aqq = s * s * a[p][p] + 2.0 * s * c * a[p][q] + c * c * a[q][q]
        a[p][p] = app
        a[q][q] = aqq
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            if k in (p, q):
                continue
            akp = c * a[k][p] - s * a[k][q]
            akq = s * a[k][p] + c * a[k][q]
            a[k][p] = a[p][k] = akp
            a[k][q] = a[q][k] = akq
    return sorted(a[i][i] for i in range(n))


def algebraic_connectivity(graph: Graph) -> float:
    values = jacobi_eigenvalues(laplacian(graph))
    return values[1]


def submatrix(matrix: Matrix, rows: list[int], cols: list[int]) -> Matrix:
    return [[matrix[i][j] for j in cols] for i in rows]


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matrix_inverse(matrix: Matrix) -> Matrix:
    n = len(matrix)
    columns = []
    for j in range(n):
        rhs = [1.0 if i == j else 0.0 for i in range(n)]
        columns.append(gaussian_solve(matrix, rhs))
    return transpose(columns)


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] - right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def kron_reduce(l_matrix: Matrix, terminals: list[int]) -> Matrix:
    internal = [i for i in range(len(l_matrix)) if i not in terminals]
    l_tt = submatrix(l_matrix, terminals, terminals)
    l_ti = submatrix(l_matrix, terminals, internal)
    l_it = submatrix(l_matrix, internal, terminals)
    l_ii = submatrix(l_matrix, internal, internal)
    return mat_sub(l_tt, matmul(matmul(l_ti, matrix_inverse(l_ii)), l_it))


def kron_refinement_error() -> float:
    graph = path_graph(4)
    l_matrix = laplacian(graph)
    rho = [1.0, 0.0, 0.0, -1.0]
    fine_action = solve_mean_zero(l_matrix, rho)
    l_eff = kron_reduce(l_matrix, [0, 3])
    coarse_action = solve_mean_zero(l_eff, [1.0, -1.0])
    fine_boundary_gap = fine_action[0] - fine_action[3]
    coarse_boundary_gap = coarse_action[0] - coarse_action[1]
    return abs(fine_boundary_gap - coarse_boundary_gap)


def hidden_weight_refinement_span() -> float:
    gaps = []
    for weights in ([1.0, 1.0, 1.0], [1.0, 2.0, 1.0], [2.0, 0.5, 2.0]):
        graph = path_graph(4, weights)
        action = solve_mean_zero(laplacian(graph), [1.0, 0.0, 0.0, -1.0])
        gaps.append(action[0] - action[3])
    return max(gaps) - min(gaps)


def source_amplitude_span() -> float:
    graph = path_graph(5)
    l_matrix = laplacian(graph)
    laws = []
    for amplitude in (0.5, 1.0, 2.0):
        action = solve_mean_zero(l_matrix, source_delta(graph.n, 2, amplitude))
        laws.append(law_from_action(action))
    return max(l1(left, right) for left in laws for right in laws)


def graph_family_span() -> float:
    graphs = [path_graph(5), cycle_graph(5)]
    laws = []
    for graph in graphs:
        action = solve_mean_zero(laplacian(graph), source_delta(graph.n, 0))
        laws.append(law_from_action(action))
    return l1(laws[0], laws[1])


def eventless_action_norm() -> float:
    graph = path_graph(5)
    action = solve_mean_zero(laplacian(graph), [0.0] * graph.n)
    return max(abs(value) for value in action)


def isolated_solution_residual() -> tuple[float, float, float]:
    graph = path_graph(5)
    l_matrix = laplacian(graph)
    rho = source_delta(graph.n, 2)
    action = solve_mean_zero(l_matrix, rho)
    perturb = [-0.4, 0.1, 0.6, -0.2, -0.1]
    m = sum(perturb) / len(perturb)
    perturb = [value - m for value in perturb]
    margin = energy(l_matrix, [a + p for a, p in zip(action, perturb)], rho) - energy(l_matrix, action, rho)
    return residual(l_matrix, action, rho), algebraic_connectivity(graph), margin


def cycle_ambiguity() -> tuple[float, float]:
    graph = cycle_graph(6)
    l_matrix = laplacian(graph)
    rho = source_delta(graph.n, 0)
    action = solve_mean_zero(l_matrix, rho)
    exact_current = gradient(graph, action)
    cycle_current = [current + 1.0 for current in exact_current]
    div_gap = norm_inf([a - b for a, b in zip(divergence(graph, exact_current), divergence(graph, cycle_current))])
    return div_gap, cycle_work(cycle_current) - cycle_work(exact_current)


def no_seam_residue() -> float:
    graph = cycle_graph(6)
    action = solve_mean_zero(laplacian(graph), source_delta(graph.n, 0))
    return abs(cycle_work(gradient(graph, action)))


def audits() -> list[FieldAudit]:
    poisson_residual, gap, margin = isolated_solution_residual()
    div_gap, loop_shift = cycle_ambiguity()
    return [
        FieldAudit(
            "relational equation",
            "change Laplacian L_D and source rho_D",
            f"residual={poisson_residual:.1e}",
            "L_D and rho_D must be intrinsic",
            "L_D S=rho",
            "THM-POISSON-IF-DATA",
        ),
        FieldAudit(
            "eventless collar",
            "rho_D=0",
            "only constant mean-zero action",
            "trivial but necessary",
            f"||S||={eventless_action_norm():.1e}",
            "PASS-FLAT",
        ),
        FieldAudit(
            "unique representative",
            "connected change graph",
            f"lambda_1={gap:.3f}",
            "fails on disconnected graphs",
            f"energy margin={margin:.3f}",
            "PASS-UNIQUE-MOD-CONST",
        ),
        FieldAudit(
            "no-silent seam",
            "exact record-work dS",
            "closed loop work vanishes",
            "kills cycle current, not source",
            f"loop residue={no_seam_residue():.1e}",
            "PASS-EXACT-WORK",
        ),
        FieldAudit(
            "cycle-current attack",
            "same divergence/source",
            f"div gap={div_gap:.1e}",
            "hidden loop current changes work",
            f"loop shift={loop_shift:.3f}",
            "FAIL-SOURCE-NOT-FULL-CURRENT",
        ),
        FieldAudit(
            "source amplitude attack",
            "same marked event support",
            "all solve L S=rho_alpha",
            "amplitude alpha is free",
            f"P span={source_amplitude_span():.3f}",
            "FAIL-RHO-AMPLITUDE",
        ),
        FieldAudit(
            "change graph attack",
            "same vertices and source",
            "path and cycle both covariant",
            "L_D changes the action",
            f"P span={graph_family_span():.3f}",
            "FAIL-L-DERIVATION",
        ),
        FieldAudit(
            "refinement receipt",
            "Schur/Kron coarse change law",
            f"boundary error={kron_refinement_error():.1e}",
            "works only if reduction map fixed",
            "fine/coarse agree",
            "PASS-IF-SCHUR",
        ),
        FieldAudit(
            "hidden refinement attack",
            "same boundary source",
            "all have valid reductions",
            "interior weights alter response",
            f"gap span={hidden_weight_refinement_span():.3f}",
            "FAIL-HIDDEN-WEIGHTS",
        ),
        FieldAudit(
            "factorization source",
            "modular defect log ratio",
            "rho fixed if full defect law supplied",
            "support-only defect leaves amplitude free",
            "conditional",
            "COND-RHO-FROM-DEFECT",
        ),
        FieldAudit(
            "field equation status",
            "F_D(S)=L_D S-rho_D",
            "relational and unique if data intrinsic",
            "not selected by kinematics alone",
            "right form, open origin",
            "OPEN-L-RHO-ORIGIN",
        ),
    ]


def print_audits(rows: list[FieldAudit]) -> None:
    print("relational record field equation campaign")
    print("-----------------------------------------")
    print(
        "target                    relational object                      positive result                  "
        "obstruction                         diagnostic value              verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.relational_object:38s} "
            f"{row.positive_result:32s} "
            f"{row.obstruction:35s} "
            f"{row.diagnostic_value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 52: relational record field equation campaign")
    print("=" * 150)
    rows = audits()
    print_audits(rows)
    print()
    print("VERDICT")
    print("-------")
    print("The relational equation exists in finite form:")
    print()
    print("    F_D(S_D)=L_D S_D-rho_D=0.")
    print()
    print("On a connected sealed-diamond change graph, this equation has a unique")
    print("mean-zero solution for every zero-sum defect source.  It is the Euler")
    print("equation for minimal record-work energy, and it gives eventless collars")
    print("as flat constant actions.")
    print()
    print("But the full Branch-A derivation is not closed.  The campaign finds")
    print("three independent openings: L_D must be the intrinsic allowed-change")
    print("operator, rho_D must be the intrinsic defect source with fixed amplitude,")
    print("and no-silent-seam exactness must kill divergence-free cycle currents.")
    print("If these are derived, the equation is a real Branch-A field law.  If any")
    print("are supplied, it is Branch B.")


if __name__ == "__main__":
    main()
