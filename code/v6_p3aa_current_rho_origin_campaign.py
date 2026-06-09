"""
v6 Paper 3 section 37: can C and rho be derived?

Question:
    Branch A can continue only if the signed current/tangent cocycle C and
    the refinement/intervention cocycle rho are derived from the physical
    process.  If either is supplied after the sealed probability/work diamond
    is known, the theory is branch B.

Finite answer:
    C and rho are not derived from the static sealed work data (P,U,R,W).
    There are finite laws with identical static probabilities and work but
    opposite oriented currents.  There are also refinement towers in which two
    lawful projections preserve the same static work while only one preserves
    the oriented current.

    The invariant that can close the gate is therefore not another scalar.  It
    is an oriented, projective record-change law: a sealed current-work functor
    whose primitive datum is the local path/RN law Q on possible record changes.
    From Q, C is the antisymmetric RN current; from functorial push-forward of
    Q, rho is the canonical refinement map, unique up to internal automorphism.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import log, sqrt


EPS = 1.0e-12


Vector = list[float]
Matrix = list[list[float]]


@dataclass(frozen=True)
class OriginAudit:
    target: str
    data: str
    construction: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def normalize(values: Vector) -> Vector:
    total = sum(values)
    return [value / total for value in values]


def kl_vec(p: Vector, q: Vector) -> float:
    return sum(pi * log(pi / qi) for pi, qi in zip(p, q) if pi > 0.0)


def outer(p: Vector, q: Vector) -> Matrix:
    return [[pi * qj for qj in q] for pi in p]


def add_cycle_current(base: Matrix, epsilon: float, sign: float = 1.0) -> Matrix:
    """Add a divergence-free oriented 3-cycle to a path law."""
    out = [row[:] for row in base]
    cycle = ((0, 1), (1, 2), (2, 0))
    for i, j in cycle:
        out[i][j] += sign * epsilon
        out[j][i] -= sign * epsilon
    if min(value for row in out for value in row) <= 0.0:
        raise ValueError("epsilon makes the path law nonpositive")
    return out


def row_marginal(q: Matrix) -> Vector:
    return [sum(row) for row in q]


def col_marginal(q: Matrix) -> Vector:
    return [sum(q[i][j] for i in range(len(q))) for j in range(len(q))]


def marginal_gap(q: Matrix, p: Vector) -> float:
    rows = row_marginal(q)
    cols = col_marginal(q)
    return max(
        max(abs(a - b) for a, b in zip(rows, p)),
        max(abs(a - b) for a, b in zip(cols, p)),
    )


def current(q: Matrix) -> Matrix:
    n = len(q)
    return [[q[i][j] - q[j][i] for j in range(n)] for i in range(n)]


def affinity(q: Matrix) -> Matrix:
    n = len(q)
    return [[0.0 if i == j else log(q[i][j] / q[j][i]) for j in range(n)] for i in range(n)]


def frob_norm(matrix: Matrix) -> float:
    return sqrt(sum(value * value for row in matrix for value in row))


def matrix_gap(left: Matrix, right: Matrix) -> float:
    return max(
        abs(left[i][j] - right[i][j])
        for i in range(len(left))
        for j in range(len(left))
    )


def path_gap(left: Matrix, right: Matrix) -> float:
    return sum(
        abs(left[i][j] - right[i][j])
        for i in range(len(left))
        for j in range(len(left))
    )


def flatten(matrix: Matrix) -> Vector:
    return [value for row in matrix for value in row]


def entropy(matrix: Matrix) -> float:
    return -sum(value * log(value) for value in flatten(matrix) if value > 0.0)


def cycle_circulation(a: Matrix) -> float:
    # Oriented RN circulation around 0 -> 1 -> 2 -> 0.
    return a[0][1] + a[1][2] + a[2][0]


def stationary_base() -> tuple[Vector, Vector, float, Matrix, Matrix, Matrix]:
    p = normalize([0.40, 0.35, 0.25])
    u = [1.0 / 3.0] * 3
    work = kl_vec(p, u)
    reversible = outer(p, p)
    q_plus = add_cycle_current(reversible, epsilon=0.030, sign=1.0)
    q_minus = add_cycle_current(reversible, epsilon=0.030, sign=-1.0)
    return p, u, work, reversible, q_plus, q_minus


def product_path_refinement(q_first: Matrix, q_second: Matrix) -> dict[tuple[int, int, int, int], float]:
    """Refined path law on states (first-copy, second-copy)."""
    out: dict[tuple[int, int, int, int], float] = {}
    n = len(q_first)
    for i, j, k, l in product(range(n), repeat=4):
        out[(i, j, k, l)] = q_first[i][k] * q_second[j][l]
    return out


def project_refined_path(
    refined: dict[tuple[int, int, int, int], float], projection: str, n: int = 3
) -> Matrix:
    out = [[0.0 for _ in range(n)] for _ in range(n)]
    if projection not in {"first", "second"}:
        raise ValueError(projection)
    for (i, j, k, l), prob in refined.items():
        if projection == "first":
            out[i][k] += prob
        else:
            out[j][l] += prob
    return out


def static_projection_work(q: Matrix, u: Vector) -> float:
    return kl_vec(row_marginal(q), u)


def audits() -> list[OriginAudit]:
    p, u, work, reversible, q_plus, q_minus = stationary_base()
    c_plus = current(q_plus)
    c_minus = current(q_minus)
    a_plus = affinity(q_plus)
    a_minus = affinity(q_minus)
    c_norm = frob_norm(c_plus)
    c_sign_gap = matrix_gap(c_plus, c_minus)
    affinity_circ_gap = abs(cycle_circulation(a_plus) - cycle_circulation(a_minus))
    static_gap = max(abs(a - b) for a, b in zip(row_marginal(q_plus), row_marginal(q_minus)))
    path_entropy_gap = entropy(reversible) - entropy(q_plus)

    refined_hidden = product_path_refinement(q_plus, reversible)
    first_q = project_refined_path(refined_hidden, "first")
    second_q = project_refined_path(refined_hidden, "second")
    first_work = static_projection_work(first_q, u)
    second_work = static_projection_work(second_q, u)
    work_drift = abs(first_work - second_work)
    current_preservation_gap_first = matrix_gap(current(first_q), current(q_plus))
    current_preservation_gap_second = matrix_gap(current(second_q), current(q_plus))
    path_preservation_gap_first = path_gap(first_q, q_plus)
    path_preservation_gap_second = path_gap(second_q, q_plus)

    refined_tie = product_path_refinement(q_plus, q_plus)
    tie_first = project_refined_path(refined_tie, "first")
    tie_second = project_refined_path(refined_tie, "second")
    tie_path_gap = path_gap(tie_first, tie_second)
    tie_current_gap = matrix_gap(current(tie_first), current(tie_second))

    return [
        OriginAudit(
            "C from static work",
            "P,U,W",
            "try C=C(P,U,W)",
            f"W={work:.6f}",
            f"same P,W opposite C gap={c_sign_gap:.6f}",
            f"marginal gap={static_gap:.1e}",
            "FAIL-STATIC-NO-C",
        ),
        OriginAudit(
            "max-entropy selector",
            "P only",
            "Q*=P tensor P",
            f"H(Q*)-H(Q+)={path_entropy_gap:.6f}",
            f"selected C norm={frob_norm(current(reversible)):.6f}",
            f"physical C norm={c_norm:.6f}",
            "FAIL-REVERSIBLE-ZERO-C",
        ),
        OriginAudit(
            "oriented path law",
            "P,Q",
            "C=Q-Q^T",
            f"marginal gap={marginal_gap(q_plus, p):.1e}",
            "Q must be physical, not fitted later",
            f"C norm={c_norm:.6f}",
            "PASS-CONDITIONAL-C-FROM-Q",
        ),
        OriginAudit(
            "RN current cocycle",
            "P,Q",
            "A=log(dQ/dQ^rev)",
            f"cycle circulation={cycle_circulation(a_plus):.6f}",
            f"opposite circulation gap={affinity_circ_gap:.6f}",
            "same static P,W",
            "PASS-CONDITIONAL-RN-CURRENT",
        ),
        OriginAudit(
            "rho from static tower",
            "refined P,W",
            "choose first or second projection",
            f"work drift={work_drift:.1e}",
            f"current error second={current_preservation_gap_second:.6f}",
            "both preserve static P,W",
            "FAIL-STATIC-RHO-NONUNIQUE",
        ),
        OriginAudit(
            "rho from path functor",
            "refined Q -> Q",
            "push forward Q exactly",
            f"path error first={path_preservation_gap_first:.1e}",
            f"path error second={path_preservation_gap_second:.6f}",
            f"current error first={current_preservation_gap_first:.1e}",
            "PASS-CONDITIONAL-RHO-FROM-Q",
        ),
        OriginAudit(
            "duplicate symmetry attack",
            "refined Q,Q",
            "two exact projections",
            f"path tie gap={tie_path_gap:.1e}",
            f"current tie gap={tie_current_gap:.1e}",
            "requires quotient by automorphism",
            "FAIL-UNIQUE-RHO-UP-TO-GAUGE",
        ),
        OriginAudit(
            "sealed current-work functor",
            "D -> (P,Q,U,R,W)",
            "C and rho by RN functoriality",
            "C=antisymmetric RN current",
            "rho=unique Q-pushforward morphism",
            "exists only if physical process supplies Q",
            "THM-TARGET-SCWF",
        ),
        OriginAudit(
            "branch verdict",
            "old sealed diamond",
            "(P,U,R,W) only",
            "W exact kinematics",
            "C/rho not derivable",
            "need projective oriented-change law",
            "OLD-A-INCOMPLETE-NEW-A-TARGET",
        ),
    ]


def print_audits(rows: list[OriginAudit]) -> None:
    print("C/rho origin campaign")
    print("---------------------")
    print(
        "target                    data             construction              "
        "positive                         obstruction                     value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.data:16s} "
            f"{row.construction:25s} "
            f"{row.positive:32s} "
            f"{row.obstruction:31s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 37: C/rho origin and invariant campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("C and rho are not derivable from the static sealed probability/work")
    print("diamond (P,U,R,W).  Same static work data admit opposite oriented")
    print("currents, and static refinement data admit alternate lifts that preserve")
    print("P and W while changing the current.")
    print()
    print("The invariant that closes the gate, if it is physical, is a sealed")
    print("current-work functor: a projective law assigning each sealed diamond an")
    print("oriented path/RN law Q, with P as its marginal, W as its KL work profile,")
    print("C as the antisymmetric RN current, and rho as the unique push-forward")
    print("morphism preserving Q, W, and composition, up to internal automorphism.")
    print()
    print("Thus old branch A-enriched is incomplete.  A new branch A-current can")
    print("continue only if the physical process intrinsically supplies this")
    print("projective oriented-change law.  If Q, C, or rho are chosen after the")
    print("sealed diamond is known, this is branch B.")


if __name__ == "__main__":
    main()
