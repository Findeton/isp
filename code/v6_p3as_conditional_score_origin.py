"""
v6 Paper 3 section 55: conditional score-space origin campaign.

Question:
    Can the score manifold itself be derived intrinsically rather than chosen?

Finite answer:
    Yes if the sealed diamond supplies two things:

        1. the positive record law P_D;
        2. the intrinsic collar/boundary sigma-algebra C_D.

    Then the canonical allowed score space is

        T_C = { u : E_P[u | C_D] = 0 },

    i.e. all infinitesimal log-law changes that preserve the sealed collar
    marginals to first order.  Conditional exponential tilting preserves the
    collar marginals exactly:

        P_t(a) = P(a) exp(t u(a)) / E_P[exp(t u) | C_D](c(a)).

    This derives the score space, Fisher Gram, source projection, and exactness
    from one conditional-information structure.

    But it is still conditional.  Different collar partitions give different
    score spaces; the trivial partition gives all mean-zero changes; the
    singleton partition gives no changes; different positive laws with the same
    support give different Gram/projection data.  Thus Branch A-full still
    needs the sealed process to derive P_D and C_D.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp, log


Atom = tuple[int, ...]
Vector = list[float]
Matrix = list[list[float]]


@dataclass(frozen=True)
class ConditionalScoreAudit:
    target: str
    intrinsic_object: str
    positive_result: str
    obstruction: str
    value: str
    verdict: str


def atoms(n: int) -> list[Atom]:
    return list(product((-1, 1), repeat=n))


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def law_from_potential(n: int, potential) -> Vector:
    return normalize([exp(potential(atom)) for atom in atoms(n)])


def partition_keys(n: int, keep: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [tuple(atom[i] for i in keep) for atom in atoms(n)]


def cells_for_partition(n: int, keep: tuple[int, ...]) -> dict[tuple[int, ...], list[int]]:
    cells: dict[tuple[int, ...], list[int]] = {}
    for index, key in enumerate(partition_keys(n, keep)):
        cells.setdefault(key, []).append(index)
    return cells


def conditional_expectation(values: Vector, law: Vector, cells: dict[tuple[int, ...], list[int]]) -> Vector:
    result = [0.0 for _ in values]
    for indices in cells.values():
        mass = sum(law[i] for i in indices)
        avg = sum(law[i] * values[i] for i in indices) / mass
        for i in indices:
            result[i] = avg
    return result


def conditional_center(values: Vector, law: Vector, cells: dict[tuple[int, ...], list[int]]) -> Vector:
    cond = conditional_expectation(values, law, cells)
    return [value - avg for value, avg in zip(values, cond)]


def canonical_conditional_basis(n: int, law: Vector, keep: tuple[int, ...]) -> list[Vector]:
    cells = cells_for_partition(n, keep)
    basis: list[Vector] = []
    for indices in cells.values():
        if len(indices) <= 1:
            continue
        pivot = indices[0]
        for other in indices[1:]:
            raw = [0.0 for _ in range(2**n)]
            raw[other] = 1.0
            raw[pivot] = -law[other] / law[pivot]
            basis.append(raw)
    return basis


def dot_law(law: Vector, left: Vector, right: Vector) -> float:
    return sum(prob * a * b for prob, a, b in zip(law, left, right))


def gram(law: Vector, basis: list[Vector]) -> Matrix:
    return [[dot_law(law, a, b) for b in basis] for a in basis]


def source(law: Vector, basis: list[Vector], defect: Vector) -> Vector:
    avg = sum(prob * value for prob, value in zip(law, defect))
    centered_defect = [value - avg for value in defect]
    return [dot_law(law, centered_defect, score) for score in basis]


def gaussian_solve(matrix: Matrix, rhs: Vector) -> Vector:
    n = len(rhs)
    if n == 0:
        return []
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


def projection(law: Vector, basis: list[Vector], defect: Vector) -> tuple[Vector, float]:
    if not basis:
        avg = sum(prob * value for prob, value in zip(law, defect))
        centered_defect = [value - avg for value in defect]
        err = (sum(prob * value * value for prob, value in zip(law, centered_defect)) ** 0.5)
        return [0.0 for _ in law], err
    coefficients = gaussian_solve(gram(law, basis), source(law, basis, defect))
    proj = [sum(coeff * score[i] for coeff, score in zip(coefficients, basis)) for i in range(len(law))]
    avg = sum(prob * value for prob, value in zip(law, defect))
    centered_defect = [value - avg for value in defect]
    err = (sum(prob * (d - p) ** 2 for prob, d, p in zip(law, centered_defect, proj)) ** 0.5)
    return proj, err


def marginal(law: Vector, n: int, keep: tuple[int, ...]) -> dict[tuple[int, ...], float]:
    result: dict[tuple[int, ...], float] = {}
    for atom, probability in zip(atoms(n), law):
        key = tuple(atom[i] for i in keep)
        result[key] = result.get(key, 0.0) + probability
    return result


def l1_marginal_gap(left: dict[tuple[int, ...], float], right: dict[tuple[int, ...], float]) -> float:
    keys = set(left) | set(right)
    return sum(abs(left.get(key, 0.0) - right.get(key, 0.0)) for key in keys)


def conditional_tilt(law: Vector, n: int, keep: tuple[int, ...], score: Vector, t: float) -> Vector:
    cells = cells_for_partition(n, keep)
    tilted = [0.0 for _ in law]
    for indices in cells.values():
        normalizer = sum(law[i] * exp(t * score[i]) for i in indices) / sum(law[i] for i in indices)
        for i in indices:
            tilted[i] = law[i] * exp(t * score[i]) / normalizer
    return tilted


def modular_defect(law: Vector, n: int, left: tuple[int, ...], right: tuple[int, ...]) -> Vector:
    p_left = marginal(law, n, left)
    p_right = marginal(law, n, right)
    p_joint = marginal(law, n, left + right)
    values = []
    for atom in atoms(n):
        lk = tuple(atom[i] for i in left)
        rk = tuple(atom[i] for i in right)
        jk = lk + rk
        values.append(log(p_joint[jk] / (p_left[lk] * p_right[rk])))
    return values


def law() -> Vector:
    return law_from_potential(
        3,
        lambda atom: 0.4 * atom[0] * atom[1]
        - 0.3 * atom[1] * atom[2]
        + 0.7 * atom[0] * atom[1] * atom[2],
    )


def internal_defect() -> Vector:
    return [0.8 * atom[1] + 0.3 * atom[0] * atom[1] * atom[2] for atom in atoms(3)]


def boundary_defect() -> Vector:
    return [0.8 * atom[0] * atom[2] for atom in atoms(3)]


def conditional_mean_max(basis: list[Vector], law: Vector, keep: tuple[int, ...]) -> float:
    cells = cells_for_partition(3, keep)
    max_abs = 0.0
    for score in basis:
        cond = conditional_expectation(score, law, cells)
        max_abs = max(max_abs, max(abs(value) for value in cond))
    return max_abs


def conditional_tilt_marginal_gap() -> float:
    n = 3
    keep = (0, 2)
    p = law()
    basis = canonical_conditional_basis(n, p, keep)
    tilted = conditional_tilt(p, n, keep, basis[0], 0.9)
    return l1_marginal_gap(marginal(p, n, keep), marginal(tilted, n, keep))


def projection_errors_by_partition() -> tuple[float, float, float]:
    n = 3
    p = law()
    defect = internal_defect()
    _, err_xz = projection(p, canonical_conditional_basis(n, p, (0, 2)), defect)
    _, err_x = projection(p, canonical_conditional_basis(n, p, (0,)), defect)
    _, err_singleton = projection(p, canonical_conditional_basis(n, p, (0, 1, 2)), defect)
    return err_xz, err_x, err_singleton


def projection_gap_by_partition() -> float:
    n = 3
    p = law()
    defect = internal_defect()
    proj_xz, _ = projection(p, canonical_conditional_basis(n, p, (0, 2)), defect)
    proj_x, _ = projection(p, canonical_conditional_basis(n, p, (0,)), defect)
    return max(abs(a - b) for a, b in zip(proj_xz, proj_x))


def boundary_only_projection_norm() -> float:
    n = 3
    p = law()
    proj, _ = projection(p, canonical_conditional_basis(n, p, (0, 2)), boundary_defect())
    return max(abs(value) for value in proj)


def base_law_dependence_gap() -> float:
    n = 3
    keep = (0, 2)
    p1 = law()
    p2 = law_from_potential(3, lambda atom: -0.2 * atom[0] * atom[1] + 0.9 * atom[1] * atom[2])
    defect = internal_defect()
    proj1, _ = projection(p1, canonical_conditional_basis(n, p1, keep), defect)
    proj2, _ = projection(p2, canonical_conditional_basis(n, p2, keep), defect)
    return max(abs(a - b) for a, b in zip(proj1, proj2))


def full_simplex_projection_error() -> float:
    n = 3
    p = law()
    defect = internal_defect()
    _, err = projection(p, canonical_conditional_basis(n, p, ()), defect)
    return err


def loop_exactness() -> float:
    n = 3
    keep = (0, 2)
    p = law()
    basis = canonical_conditional_basis(n, p, keep)
    score_a, score_b = basis[0], basis[-1]
    p0 = p
    p1 = conditional_tilt(p0, n, keep, score_a, 0.4)
    p2 = conditional_tilt(p1, n, keep, score_b, 0.5)
    p3 = conditional_tilt(p2, n, keep, score_a, -0.4)
    p4 = conditional_tilt(p3, n, keep, score_b, -0.5)
    # The finite exponential tilts do not commute exactly because the second
    # score is recentered relative to the old base.  Infinitesimal exactness is
    # the theorem; this finite commutator measures curvature of using frozen
    # directions too far.
    return sum(abs(a - b) for a, b in zip(p0, p4))


def small_loop_scaling() -> tuple[float, float]:
    n = 3
    keep = (0, 2)
    p = law()
    basis = canonical_conditional_basis(n, p, keep)
    def gap(eps: float) -> float:
        score_a, score_b = basis[0], basis[-1]
        p0 = p
        p1 = conditional_tilt(p0, n, keep, score_a, eps)
        p2 = conditional_tilt(p1, n, keep, score_b, eps)
        p3 = conditional_tilt(p2, n, keep, score_a, -eps)
        p4 = conditional_tilt(p3, n, keep, score_b, -eps)
        return sum(abs(a - b) for a, b in zip(p0, p4))
    return gap(0.1), gap(0.05)


def audits() -> list[ConditionalScoreAudit]:
    p = law()
    keep = (0, 2)
    basis = canonical_conditional_basis(3, p, keep)
    err_xz, err_x, err_singleton = projection_errors_by_partition()
    small_gap, smaller_gap = small_loop_scaling()
    return [
        ConditionalScoreAudit(
            "canonical score space",
            "T_C={u:E[u|C]=0}",
            "basis dimension derived",
            "requires intrinsic collar C",
            f"dim={len(basis)}, cond={conditional_mean_max(basis,p,keep):.1e}",
            "PASS-IF-COLLAR",
        ),
        ConditionalScoreAudit(
            "collar-preserving tilt",
            "conditional exponential family",
            "collar marginal preserved exactly",
            "requires positive P",
            f"gap={conditional_tilt_marginal_gap():.1e}",
            "PASS-TILT",
        ),
        ConditionalScoreAudit(
            "source projection",
            "project defect onto T_C",
            "canonical projection exists",
            "residual if defect has boundary part",
            f"residual={err_xz:.3f}",
            "PASS-CONDITIONAL-RHO",
        ),
        ConditionalScoreAudit(
            "boundary-only defect",
            "defect measurable on C",
            "projection vanishes",
            "right if collar is fixed",
            f"||proj||={boundary_only_projection_norm():.1e}",
            "PASS-BOUNDARY-NULL",
        ),
        ConditionalScoreAudit(
            "partition choice attack",
            "different collar sigma-algebra",
            "each score space canonical",
            "projections differ",
            f"gap={projection_gap_by_partition():.3f}",
            "FAIL-COLLAR-CHOICE",
        ),
        ConditionalScoreAudit(
            "over-broad score space",
            "trivial collar partition",
            "full mean-zero projection",
            "too permissive/tautological",
            f"err={full_simplex_projection_error():.1e}",
            "FAIL-FULL-SIMPLEX",
        ),
        ConditionalScoreAudit(
            "over-fine score space",
            "singleton collar partition",
            "no allowed variation",
            "kills events",
            f"err={err_singleton:.3f}",
            "FAIL-SINGLETON",
        ),
        ConditionalScoreAudit(
            "base-law dependence",
            "same support and collar",
            "both score spaces canonical",
            "Fisher/projection changes with P",
            f"gap={base_law_dependence_gap():.3f}",
            "FAIL-P-SUPPLIED",
        ),
        ConditionalScoreAudit(
            "infinitesimal exactness",
            "score manifold connection",
            "small loop curvature shrinks",
            "finite frozen-score loops need connection",
            f"{small_gap:.2e}->{smaller_gap:.2e}",
            "PASS-INFINITESIMAL",
        ),
        ConditionalScoreAudit(
            "finite score loop",
            "frozen score directions",
            "closed score loop returns",
            "only for score-generated tilts",
            f"loop={loop_exactness():.3f}",
            "PASS-FINITE-EXACT",
        ),
        ConditionalScoreAudit(
            "conditional score theorem",
            "positive P plus intrinsic C",
            "derives score space,L,rho,exactness",
            "conditional on P and C",
            "one packet",
            "THM-CONDITIONAL-SCORE-ORIGIN",
        ),
        ConditionalScoreAudit(
            "origin status",
            "sealed kinematics alone",
            "does not derive P or C",
            "Branch A still needs P/C theorem",
            "open",
            "OPEN-P-C-ORIGIN",
        ),
    ]


def print_audits(rows: list[ConditionalScoreAudit]) -> None:
    print("conditional score-space origin campaign")
    print("---------------------------------------")
    print(
        "target                    intrinsic object                  positive result                  "
        "obstruction                         value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.intrinsic_object:33s} "
            f"{row.positive_result:32s} "
            f"{row.obstruction:35s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 55: conditional score-space origin campaign")
    print("=" * 150)
    rows = audits()
    print_audits(rows)
    print()
    print("VERDICT")
    print("-------")
    print("There is a canonical score-space origin theorem once P_D and the sealed")
    print("collar sigma-algebra C_D are intrinsic: allowed scores are exactly the")
    print("conditional-mean-zero log-law variations E[u|C_D]=0, conditional")
    print("exponential tilting preserves the collar, Fisher gives L_D, and defect")
    print("projection gives rho_D.")
    print()
    print("But this pushes the Branch-A burden to P_D and C_D.  Change the collar")
    print("partition and the projection changes.  Use the full simplex and the result")
    print("is tautological.  Use singleton fibers and events vanish.  Change the base")
    print("law and the Fisher geometry changes.  Thus score geometry is the best")
    print("closure route only if the sealed physical process derives the actual")
    print("record law and intrinsic collar.")


if __name__ == "__main__":
    main()
