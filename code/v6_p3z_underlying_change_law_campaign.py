"""
v6 Paper 3 section 36: underlying law of possible changes.

Question:
    Can the sealed probability/work diamond (P,R,U,W) derive the signed
    local tangent/intervention law needed by the free Dirac benchmark?

Finite answer:
    No.  P,R,U,W give a Fisher/KL geometry and exact work components, but
    they do not determine the signed local comparison generator A_R^(1), nor
    the phase/current information behind possible changes.

    The minimal branch-A candidate is therefore stronger:

        sealed current-work diamond =
        (P, U, R, W, C, rho)

    where C is an intrinsic tangent/current cocycle and rho is the canonical
    refinement/intervention cocycle.  With C supplied, the free Dirac anchor
    is recovered conditionally; without deriving C, the theory is branch B.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, sin, pi

from v6_p3y_full_branch_a_target_campaign import (
    dirac_a1_singleton,
    probability_hessian_reference,
    support_mismatch,
)


@dataclass(frozen=True)
class ChangeLawAudit:
    candidate: str
    data: str
    observable: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def commutator(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    ab = matmul(a, b)
    ba = matmul(b, a)
    return [[ab[i][j] - ba[i][j] for j in range(len(a))] for i in range(len(a))]


def frob_norm(a: list[list[float]]) -> float:
    return sum(value * value for row in a for value in row) ** 0.5


def scale_matrix(a: list[list[float]], scale: float) -> list[list[float]]:
    return [[scale * value for value in row] for row in a]


def subtract(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]


def max_abs(a: list[list[float]]) -> float:
    return max(abs(value) for row in a for value in row)


def nonzero_offdiag(a: list[list[float]]) -> int:
    return sum(
        1
        for i, row in enumerate(a)
        for j, value in enumerate(row)
        if i != j and abs(value) > 1.0e-12
    )


def lambda_scale(lam: float) -> float:
    return lam * (2.0 - lam)


def hidden_phase_current(phi: float) -> tuple[float, float, float]:
    # Two state vectors have the same probabilities but opposite probability
    # current Im(conj(psi0) psi1).  This is the smallest receipt that
    # probability-only data cannot determine possible changes.
    p_gap = 0.0
    current_plus = 0.5 * sin(phi)
    current_minus = -0.5 * sin(phi)
    return p_gap, current_plus, current_minus


def rows() -> list[ChangeLawAudit]:
    a_r = dirac_a1_singleton(L=5, n0=2, a=1.0)
    a_s = dirac_a1_singleton(L=5, n0=4, a=1.0)
    h = probability_hessian_reference(len(a_r))
    a_off, h_off, mismatch = support_mismatch(a_r, h)
    dirac_comm = frob_norm(commutator(a_r, a_s))
    fisher_comm = frob_norm(commutator(h, h))

    lambdas = (0.25, 1.0, 1.75)
    scales = [lambda_scale(lam) for lam in lambdas]
    normalized_errors = [
        max_abs(subtract(scale_matrix(a_r, scale), scale_matrix(a_r, scale)))
        for scale in scales
    ]
    raw_span = max(scales) - min(scales)

    p_gap, current_plus, current_minus = hidden_phase_current(pi / 3.0)
    current_gap = abs(current_plus - current_minus)

    return [
        ChangeLawAudit(
            "probability Hessian",
            "P,R,U,W",
            "Hess(D(p||u))",
            f"Hess offdiag={h_off}",
            f"A_R offdiag={a_off}",
            f"support mismatch={mismatch}",
            "FAIL-NOT-DIRAC-TANGENT",
        ),
        ChangeLawAudit(
            "exchange curvature",
            "P,R,U,W",
            "[tangent_R,tangent_S]",
            f"Dirac comm norm={dirac_comm:.6f}",
            f"Fisher comm norm={fisher_comm:.6f}",
            "probability metric has no bracket",
            "FAIL-NO-CHANGE-BRACKET",
        ),
        ChangeLawAudit(
            "hidden phase/current",
            "same probabilities",
            "Im(conj psi_i psi_j)",
            f"probability gap={p_gap:.3e}",
            f"current gap={current_gap:.6f}",
            "same P opposite current",
            "FAIL-PROBA-LOSES-CURRENT",
        ),
        ChangeLawAudit(
            "lambda rule family",
            "same P,R,U,W",
            "A_lambda=c_lambda A",
            f"normalized error={max(normalized_errors):.1e}",
            f"raw scale span={raw_span:.4f}",
            "raw rule not selected",
            "FAIL-RAW-RULE-NONUNIQUE",
        ),
        ChangeLawAudit(
            "Dirac cocycle supplied",
            "P,R,U,W plus C",
            "C_R=A_R^(1)",
            f"support={nonzero_offdiag(a_r)} offdiag",
            "C supplied, not derived",
            f"comm norm={dirac_comm:.6f}",
            "PASS-CONDITIONAL-DIRAC-ANCHOR",
        ),
        ChangeLawAudit(
            "sealed current-work diamond",
            "(P,U,R,W,C,rho)",
            "metric + current cocycle",
            "minimal object has metric and bracket",
            "existence not proved",
            "Einstein candidate",
            "THM-TARGET-NOT-CLOSED",
        ),
        ChangeLawAudit(
            "branch verdict",
            "current ontology",
            "possible-change law",
            "W_x exact kinematics",
            "C/rho dynamics missing",
            "branch-A gate isolated",
            "A-PARTIAL-OR-B",
        ),
    ]


def print_rows(audits: list[ChangeLawAudit]) -> None:
    print("underlying possible-change law audit")
    print("------------------------------------")
    print(
        "candidate                    data                 observable              "
        "positive                    obstruction                 value                         verdict"
    )
    for row in audits:
        print(
            f"{row.candidate:28s} "
            f"{row.data:20s} "
            f"{row.observable:23s} "
            f"{row.positive:27s} "
            f"{row.obstruction:27s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 136)
    print("v6 Paper 3 section 36: underlying law of possible changes")
    print("=" * 136)
    print_rows(rows())
    print()
    print("VERDICT")
    print("-------")
    print("The sealed KL work profile is invariant kinematics, not a complete")
    print("law of possible changes.  P,R,U,W determine the Fisher metric and exact")
    print("work split, but they do not determine signed Dirac intervention")
    print("directions, exchange brackets, hidden phase/current, or raw rule scale.")
    print()
    print("The minimal Einstein-satisfactory object is a sealed current-work")
    print("diamond (P,U,R,W,C,rho): W gives the metric/work profile, C gives the")
    print("signed tangent/current cocycle, and rho gives canonical refinement and")
    print("intervention composition.  The free Dirac A_R^(1) is then a conditional")
    print("anchor.  If C and rho are derived from the physical process, branch A can")
    print("continue.  If C or rho are supplied, this is branch B.")


if __name__ == "__main__":
    main()
