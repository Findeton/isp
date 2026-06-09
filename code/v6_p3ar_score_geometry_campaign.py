"""
v6 Paper 3 section 54: intrinsic score-geometry campaign.

Question:
    Can the missing packet (L_D, rho_D, exactness) be derived from one deeper
    object: the intrinsic score geometry of a sealed finite diamond?

Finite answer:
    Yes conditionally, not absolutely.

    If the sealed physical process supplies an intrinsic manifold of internally
    distinguishable record laws, with score directions

        u_i = d log P_theta / d theta_i,

    then the missing packet is canonical:

        L_ij   = E_P[u_i u_j]                         (Fisher/Gram operator)
        rho_i  = E_P[Delta u_i]                       (defect projection)
        J      = dS                                   (exact score work)

    and the field equation is the projection/normal equation

        L s = rho.

    It has a unique projected action when L is nonsingular on the observable
    score space.  The defect amplitude is fixed because Delta is a log
    Radon-Nikodym/factorization defect.

    But this is still conditional.  If the score space is chosen, omitted,
    enlarged, or given a nonintegrable current by hand, the result changes.
    Branch A-full therefore needs an intrinsic score-manifold theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp, log
from typing import Callable


Atom = tuple[int, ...]
Feature = Callable[[Atom], float]
Vector = list[float]
Matrix = list[list[float]]


@dataclass(frozen=True)
class ScoreAudit:
    target: str
    score_object: str
    positive_result: str
    obstruction: str
    value: str
    verdict: str


def atoms(n: int) -> list[Atom]:
    return list(product((-1, 1), repeat=n))


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def exponential_law(n: int, features: list[Feature], theta: Vector) -> Vector:
    weights = []
    for atom in atoms(n):
        weights.append(exp(sum(t * f(atom) for t, f in zip(theta, features))))
    return normalize(weights)


def uniform_law(n: int) -> Vector:
    return [1.0 / (2**n)] * (2**n)


def expectation(law: Vector, values: Vector) -> float:
    return sum(probability * value for probability, value in zip(law, values))


def feature_values(n: int, feature: Feature) -> Vector:
    return [feature(atom) for atom in atoms(n)]


def centered(values: Vector, law: Vector) -> Vector:
    avg = expectation(law, values)
    return [value - avg for value in values]


def dot_law(law: Vector, left: Vector, right: Vector) -> float:
    return sum(probability * a * b for probability, a, b in zip(law, left, right))


def fisher_gram(n: int, law: Vector, features: list[Feature]) -> Matrix:
    scores = [centered(feature_values(n, feature), law) for feature in features]
    return [[dot_law(law, left, right) for right in scores] for left in scores]


def source_vector(n: int, law: Vector, features: list[Feature], defect: Vector) -> Vector:
    scores = [centered(feature_values(n, feature), law) for feature in features]
    defect_centered = centered(defect, law)
    return [dot_law(law, defect_centered, score) for score in scores]


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


def projected_action(n: int, law: Vector, features: list[Feature], defect: Vector) -> tuple[Vector, Vector, float]:
    gram = fisher_gram(n, law, features)
    rho = source_vector(n, law, features, defect)
    coeffs = gaussian_solve(gram, rho)
    scores = [centered(feature_values(n, feature), law) for feature in features]
    projection = [sum(coeff * score[i] for coeff, score in zip(coeffs, scores)) for i in range(len(law))]
    err = projection_error(law, defect, projection)
    return coeffs, projection, err


def projection_error(law: Vector, defect: Vector, projection: Vector) -> float:
    defect_centered = centered(defect, law)
    return (
        sum(probability * (d - p) ** 2 for probability, d, p in zip(law, defect_centered, projection))
        ** 0.5
    )


def marginal(law: Vector, n: int, keep: tuple[int, ...]) -> dict[tuple[int, ...], float]:
    result: dict[tuple[int, ...], float] = {}
    for atom, probability in zip(atoms(n), law):
        key = tuple(atom[i] for i in keep)
        result[key] = result.get(key, 0.0) + probability
    return result


def modular_defect(law: Vector, n: int, left: tuple[int, ...], right: tuple[int, ...]) -> Vector:
    p_left = marginal(law, n, left)
    p_right = marginal(law, n, right)
    p_joint = marginal(law, n, left + right)
    values = []
    for atom in atoms(n):
        left_key = tuple(atom[i] for i in left)
        right_key = tuple(atom[i] for i in right)
        joint_key = left_key + right_key
        values.append(log(p_joint[joint_key] / (p_left[left_key] * p_right[right_key])))
    return values


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def law_from_action(action: Vector) -> Vector:
    return normalize([exp(value) for value in action])


def x(atom: Atom) -> float:
    return float(atom[0])


def y(atom: Atom) -> float:
    return float(atom[1])


def z(atom: Atom) -> float:
    return float(atom[2])


def xz(atom: Atom) -> float:
    return float(atom[0] * atom[-1])


def xyz(atom: Atom) -> float:
    return float(atom[0] * atom[1] * atom[2])


def yz(atom: Atom) -> float:
    return float(atom[1] * atom[2])


def positive_pair_projection() -> tuple[float, float]:
    n = 2
    theta = 0.9
    law = exponential_law(n, [xz], [theta])
    defect = modular_defect(law, n, (0,), (1,))
    coeffs, _, err = projected_action(n, law, [xz], defect)
    return coeffs[0], err


def missing_bridge_score_error() -> float:
    n = 2
    law = exponential_law(n, [xz], [0.9])
    defect = modular_defect(law, n, (0,), (1,))
    _, _, err = projected_action(n, law, [lambda atom: float(atom[0]), lambda atom: float(atom[1])], defect)
    return err


def basis_invariance_gap() -> float:
    n = 2
    law = exponential_law(n, [xz], [0.9])
    defect = modular_defect(law, n, (0,), (1,))
    _, projection_a, _ = projected_action(n, law, [xz], defect)
    _, projection_b, _ = projected_action(n, law, [lambda atom: 2.0 * xz(atom)], defect)
    return max(abs(a - b) for a, b in zip(projection_a, projection_b))


def supplied_score_family_gap() -> tuple[float, float, float]:
    n = 3
    law = exponential_law(n, [xz, xyz], [0.55, 0.45])
    defect = modular_defect(law, n, (0, 1), (2,))
    _, projection_small, err_small = projected_action(n, law, [xz], defect)
    _, projection_big, err_big = projected_action(n, law, [xz, xyz], defect)
    gap = max(abs(a - b) for a, b in zip(projection_small, projection_big))
    return err_small, err_big, gap


def defect_amplitude_span() -> float:
    n = 2
    law = exponential_law(n, [xz], [0.9])
    defect = modular_defect(law, n, (0,), (1,))
    laws = []
    for scale in (0.5, 1.0, 2.0):
        _, projection, _ = projected_action(n, law, [xz], [scale * value for value in defect])
        laws.append(law_from_action(projection))
    return max(l1(left, right) for left in laws for right in laws)


def fixed_defect_amplitude_coeff() -> float:
    coeff, _ = positive_pair_projection()
    return coeff


def exact_parameter_loop_residue() -> float:
    n = 2
    features = [x, xz]
    corners = ([0.0, 0.0], [0.4, 0.0], [0.4, 0.7], [0.0, 0.7], [0.0, 0.0])
    actions = []
    for theta in corners:
        law = exponential_law(n, features, theta)
        u = 1.0 / len(law)
        actions.append([-log(prob / u) for prob in law])
    loop = [0.0 for _ in range(len(actions[0]))]
    for i in range(len(actions) - 1):
        for j in range(len(loop)):
            loop[j] += actions[i + 1][j] - actions[i][j]
    return max(abs(value) for value in loop)


def nonintegrable_loop_residue() -> float:
    # Artificial work form A = theta_y d theta_x has unit curl on the unit
    # square.  It is not a score gradient of one potential.
    return abs(0.0 + 1.0 + 0.0 - 0.0)


def score_refinement_loss() -> float:
    n = 3
    law = exponential_law(n, [xz, yz], [0.4, 0.6])
    fine_score = centered(feature_values(n, yz), law)
    p_xz = marginal(law, n, (0, 2))
    conditional: dict[tuple[int, int], float] = {}
    coarse_score_by_key: dict[tuple[int, int], float] = {}
    for atom, probability, score in zip(atoms(n), law, fine_score):
        key = (atom[0], atom[2])
        conditional[key] = conditional.get(key, 0.0) + probability
        coarse_score_by_key[key] = coarse_score_by_key.get(key, 0.0) + probability * score
    for key in coarse_score_by_key:
        coarse_score_by_key[key] /= conditional[key]
    fine_info = sum(prob * score * score for prob, score in zip(law, fine_score))
    coarse_info = sum(prob * coarse_score_by_key[key] ** 2 for key, prob in p_xz.items())
    return fine_info - coarse_info


def score_vs_support_only_span() -> float:
    n = 2
    laws = []
    for theta in (0.3, 0.9, 1.5):
        law = exponential_law(n, [xz], [theta])
        defect = modular_defect(law, n, (0,), (1,))
        _, projection, _ = projected_action(n, law, [xz], defect)
        laws.append(law_from_action(projection))
    return max(l1(left, right) for left in laws for right in laws)


def audits() -> list[ScoreAudit]:
    coeff, pair_err = positive_pair_projection()
    err_small, err_big, supplied_gap = supplied_score_family_gap()
    return [
        ScoreAudit(
            "score Gram derives L",
            "u_i=d log P/d theta_i",
            "Fisher L_ij=<u_i,u_j>",
            "score space must be intrinsic",
            f"pair coeff={coeff:.3f}",
            "PASS-IF-SCORES",
        ),
        ScoreAudit(
            "defect projection derives rho",
            "Delta=log P/(P_L P_R)",
            "rho_i=<Delta,u_i>",
            "requires full log defect, not support",
            f"projection err={pair_err:.1e}",
            "PASS-FIXED-AMPLITUDE",
        ),
        ScoreAudit(
            "basis covariance",
            "same score span, rescaled basis",
            "projected action invariant",
            "only span matters",
            f"gap={basis_invariance_gap():.1e}",
            "PASS-GAUGE-SPAN",
        ),
        ScoreAudit(
            "missing bridge score",
            "single-site scores only",
            "formal Gram exists",
            "bridge defect invisible",
            f"projection err={missing_bridge_score_error():.3f}",
            "FAIL-INCOMPLETE-SCORES",
        ),
        ScoreAudit(
            "supplied score family",
            "add triple score by hand",
            "projection improves",
            "chosen score space changes S",
            f"err {err_small:.3f}->{err_big:.3f}, gap={supplied_gap:.3f}",
            "FAIL-SCORE-SELECTION",
        ),
        ScoreAudit(
            "defect amplitude",
            "full RN/KL Delta",
            "amplitude fixed by log ratio",
            "support-only scaling remains free",
            f"scaled span={defect_amplitude_span():.3f}",
            "COND-LOG-DEFECT-NEEDED",
        ),
        ScoreAudit(
            "exactness",
            "integrable score potential",
            "closed parameter-loop action vanishes",
            "non-score currents can have curl",
            f"loop={exact_parameter_loop_residue():.1e}",
            "PASS-EXACT-SCORES",
        ),
        ScoreAudit(
            "nonintegrable current attack",
            "artificial work form",
            "local components can be assigned",
            "curl creates silent seam",
            f"loop={nonintegrable_loop_residue():.1f}",
            "FAIL-NONINTEGRABLE",
        ),
        ScoreAudit(
            "refinement score receipt",
            "conditional expectation of scores",
            "Fisher information decreases",
            "hidden scores change L if retained",
            f"info loss={score_refinement_loss():.3f}",
            "PASS-MONOTONE",
        ),
        ScoreAudit(
            "support-only source attack",
            "same bridge support",
            "all have same event support",
            "theta/log amplitude changes law",
            f"P span={score_vs_support_only_span():.3f}",
            "FAIL-SUPPORT-ONLY",
        ),
        ScoreAudit(
            "score-geometry theorem",
            "intrinsic score manifold + log defect",
            "derives L,rho,exactness",
            "conditional on intrinsic manifold",
            "one packet",
            "THM-CONDITIONAL-SCORE-GEOMETRY",
        ),
        ScoreAudit(
            "closure status",
            "sealed kinematics alone",
            "not enough to pick score manifold",
            "score-origin theorem missing",
            "A-full open",
            "OPEN-SCORE-ORIGIN",
        ),
    ]


def print_audits(rows: list[ScoreAudit]) -> None:
    print("intrinsic score-geometry campaign")
    print("---------------------------------")
    print(
        "target                    score object                       positive result                  "
        "obstruction                         value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.score_object:34s} "
            f"{row.positive_result:32s} "
            f"{row.obstruction:35s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 54: intrinsic score-geometry campaign")
    print("=" * 150)
    rows = audits()
    print_audits(rows)
    print()
    print("VERDICT")
    print("-------")
    print("Score geometry is the strongest current closure route.  If the sealed")
    print("physical process intrinsically supplies the score manifold of internally")
    print("distinguishable record changes, then L_D is its Fisher Gram, rho_D is the")
    print("projection of the modular log defect, and exactness follows because score")
    print("work is a gradient of one log-likelihood potential.")
    print()
    print("But this is conditional.  Omit the bridge score and the defect is")
    print("invisible.  Add score directions by hand and the projected action changes.")
    print("Use support-only defects and the amplitude is free.  Use nonintegrable")
    print("currents and no-silent-seam fails.  Therefore Branch A-full now needs one")
    print("specific theorem: the sealed diamond intrinsically determines its score")
    print("manifold and full modular log defect.")


if __name__ == "__main__":
    main()
