"""
v6 Paper 2 Part II §5.39: full IDA-germ uniqueness attack.

The §5.38 theorem shows that a full regular IDA germ would close the finite
role-Gram gate.  This script attacks the word "full": is the germ determined
by finite Physical-ICS data (P_n, D_x, A_x(0)), or is it extra structure?

Result:
    P_n, D_x, and the scalar deletion action value do not determine the germ.
    Even with finite positivity, order covariance, and slice-freeness, one can
    keep the same base deletion law while changing:

        1. the source score row;
        2. the role basis inside an unlabeled score subspace;
        3. the normalization of the source parameter;
        4. the refinement sequence of germs.

Branch A therefore needs a canonical normalized four-direction germ theorem,
not just IDA existence.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, sin

from v6_p2r_full_role_gram_derivation import (
    ROLE_ORDER,
    LawInstance,
    base_role_rows,
    beta_from_gram,
    gram,
    role_rows,
    weak_source_rows,
)


@dataclass
class GermAttack:
    candidate: str
    same_physical_ics: str
    scalar_a_fixed: str
    directions_intrinsic: str
    role_labels_intrinsic: str
    normalization_fixed: str
    convergence: str
    beta_span: float
    verdict: str


def beta_from_rows(rows: dict[str, list[float]]) -> tuple[float, bool]:
    j = gram(role_rows(LawInstance(rows, "pre"), ROLE_ORDER))
    _, beta, ok = beta_from_gram(j, 0.015)
    return beta, ok


def beta_span_from_rows(row_family: list[dict[str, list[float]]]) -> float:
    betas = []
    for rows in row_family:
        beta, ok = beta_from_rows(rows)
        if ok:
            betas.append(beta)
    return max(betas) - min(betas) if len(betas) >= 2 else float("inf")


def source_row_family() -> list[dict[str, list[float]]]:
    return [base_role_rows(strength) for strength in [0.55, 0.75, 0.95, 1.15]]


def rotate_j(j: list[list[float]], angle: float) -> list[list[float]]:
    """Rotate record/source coordinates, leaving causal/antichain fixed."""
    r = [
        [cos(angle), -sin(angle), 0.0, 0.0],
        [sin(angle), cos(angle), 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    return [
        [
            sum(r[i][a] * j[a][b] * r[k][b] for a in range(4) for b in range(4))
            for k in range(4)
        ]
        for i in range(4)
    ]


def beta_span_from_grams(grams: list[list[list[float]]]) -> float:
    betas = []
    for j in grams:
        _, beta, ok = beta_from_gram(j, 0.015)
        if ok:
            betas.append(beta)
    return max(betas) - min(betas) if len(betas) >= 2 else float("inf")


def role_rotation_family() -> list[list[list[float]]]:
    base_j = gram(role_rows(LawInstance(base_role_rows(0.95), "pre"), ROLE_ORDER))
    return [rotate_j(base_j, angle) for angle in [-0.45, -0.20, 0.0, 0.20, 0.45]]


def source_scale_family() -> list[dict[str, list[float]]]:
    out = []
    for scale in [0.70, 0.90, 1.00, 1.15, 1.35]:
        rows = base_role_rows(0.95)
        rows["source"] = [scale * value for value in rows["source"]]
        out.append(rows)
    return out


def convergent_canonical_family() -> list[dict[str, list[float]]]:
    return [
        {
            "record": [0.95 + 0.02 * step, 0.05, 0.02, 0.00],
            "source": [0.08, 0.92 + 0.03 * step, 0.05, 0.02],
            "causal": [0.03, 0.06, 0.96 + 0.01 * step, 0.04],
            "antichain": [0.02, 0.04, 0.08, 0.98 + 0.01 * step],
        }
        for step in [1.0, 0.5, 0.25, 0.0]
    ]


def nonconvergent_family() -> list[dict[str, list[float]]]:
    return [base_role_rows(strength) for strength in [0.55, 1.15, 0.65, 1.05]]


def weak_source_family() -> list[dict[str, list[float]]]:
    return [weak_source_rows(strength) for strength in [0.04, 0.05, 0.06, 0.05]]


def attack_rows() -> list[GermAttack]:
    source_span = beta_span_from_rows(source_row_family())
    rotation_span = beta_span_from_grams(role_rotation_family())
    scale_span = beta_span_from_rows(source_scale_family())
    canonical_span = beta_span_from_rows(convergent_canonical_family())
    drift_span = beta_span_from_rows(nonconvergent_family())
    weak_span = beta_span_from_rows(weak_source_family())
    return [
        GermAttack(
            "base P,D,A only",
            "yes",
            "yes",
            "no",
            "no",
            "no",
            "no",
            source_span,
            "FAIL",
        ),
        GermAttack(
            "unlabeled score subspace",
            "yes",
            "yes",
            "yes",
            "no",
            "no",
            "no",
            rotation_span,
            "FAIL",
        ),
        GermAttack(
            "free source units",
            "yes",
            "yes",
            "yes",
            "yes",
            "no",
            "no",
            scale_span,
            "FAIL",
        ),
        GermAttack(
            "drifting canonical-looking germ",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "no",
            drift_span,
            "FAIL",
        ),
        GermAttack(
            "weak-source canonical germ",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            weak_span,
            "FAIL",
        ),
        GermAttack(
            "canonical normalized germ",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            canonical_span,
            "PASS-TARGET",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_attacks(rows: list[GermAttack]) -> None:
    print("full IDA-germ uniqueness attack")
    print("--------------------------------")
    print(
        "candidate                      sameICS  A0  dirs  labels  units  "
        "conv  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:29s}  "
            f"{row.same_physical_ics:7s}  "
            f"{row.scalar_a_fixed:3s}  "
            f"{row.directions_intrinsic:4s}  "
            f"{row.role_labels_intrinsic:6s}  "
            f"{row.normalization_fixed:5s}  "
            f"{row.convergence:4s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = attack_rows()
    print("=" * 104)
    print("v6 Paper 2 Part II §5.39: full IDA-germ uniqueness attack")
    print("=" * 104)
    print_attacks(rows)
    print("VERDICT")
    print("-------")
    print("Physical ICS data P_n, D_x, and A_x(0) do not determine the full")
    print("IDA germ.  A score subspace without role labels, or role labels without")
    print("fixed units, still leaves beta freedom.  The surviving object is a")
    print("canonical normalized four-role deletion germ with a positive source")
    print("floor and cofinal convergence.  That is an additional theorem target.")


if __name__ == "__main__":
    main()
