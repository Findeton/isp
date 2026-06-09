"""
v6 Paper 3 section 38: Einsteinian origin of Q.

Question:
    The previous campaign showed that C and rho are derived once the physical
    process supplies an oriented path/RN law Q.  But is Q itself forced by the
    sealed diamond, or is it another branch-B input?

Finite answer:
    Q is not derivable from static probabilities, boundary marginals, or an
    unordered pair law.  It is forced only if the primitive finite diamond is a
    two-screen record bridge: an intrinsically ordered past/future boundary
    law whose composition is part of the sealed physical process.

    In that object Q is not an extra current.  It is the full law of record
    transport from the lower screen to the upper screen.  C, RN circulation,
    and rho are then readouts.  Without intrinsic screen order and functorial
    composition, Q remains branch B.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt

from v6_p3aa_current_rho_origin_campaign import (
    Matrix,
    affinity,
    col_marginal,
    current,
    cycle_circulation,
    frob_norm,
    matrix_gap,
    row_marginal,
    stationary_base,
)


@dataclass(frozen=True)
class QOriginAudit:
    target: str
    data: str
    construction: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def unordered_pair_law(q: Matrix) -> Matrix:
    n = len(q)
    return [[0.5 * (q[i][j] + q[j][i]) for j in range(n)] for i in range(n)]


def transition(q: Matrix) -> Matrix:
    rows = row_marginal(q)
    return [[q[i][j] / rows[i] for j in range(len(q))] for i in range(len(q))]


def compose_joint(q12: Matrix, q23: Matrix) -> Matrix:
    p1 = row_marginal(q12)
    t12 = transition(q12)
    t23 = transition(q23)
    n = len(q12)
    return [
        [p1[i] * sum(t12[i][j] * t23[j][k] for j in range(n)) for k in range(n)]
        for i in range(n)
    ]


def l1_gap(left: Matrix, right: Matrix) -> float:
    return sum(
        abs(left[i][j] - right[i][j])
        for i in range(len(left))
        for j in range(len(left))
    )


def entropy_production(q: Matrix) -> float:
    # Nonnegative pathwise entropy production for a positive finite bridge.
    n = len(q)
    total = 0.0
    for i in range(n):
        for j in range(n):
            total += q[i][j] * log(q[i][j] / q[j][i])
    return total


def poset_screens(oriented: bool) -> tuple[bool, str, str]:
    # A toy sealed diamond with three lower-screen atoms and three upper-screen
    # atoms.  If the order orientation is retained, minimal and maximal
    # elements are intrinsic.  If only the undirected shadow is retained, past
    # and future screens cannot be distinguished.
    if not oriented:
        return False, "--", "--"
    lower = "0,1,2"
    upper = "3,4,5"
    return True, lower, upper


def bridge_family_span(q_plus: Matrix, q_minus: Matrix) -> tuple[float, float, float]:
    rows_gap = max(abs(a - b) for a, b in zip(row_marginal(q_plus), row_marginal(q_minus)))
    cols_gap = max(abs(a - b) for a, b in zip(col_marginal(q_plus), col_marginal(q_minus)))
    q_gap = l1_gap(q_plus, q_minus)
    return rows_gap, cols_gap, q_gap


def audits() -> list[QOriginAudit]:
    p, _u, work, reversible, q_plus, q_minus = stationary_base()
    sym_plus = unordered_pair_law(q_plus)
    sym_minus = unordered_pair_law(q_minus)
    rows_gap, cols_gap, q_gap = bridge_family_span(q_plus, q_minus)
    unordered_gap = l1_gap(sym_plus, sym_minus)
    c_norm = frob_norm(current(q_plus))
    c_gap = matrix_gap(current(q_plus), current(q_minus))
    circ = cycle_circulation(affinity(q_plus))
    ep = entropy_production(q_plus)
    oriented_ok, lower, upper = poset_screens(oriented=True)
    unoriented_ok, _ulower, _uupper = poset_screens(oriented=False)

    composed_plus = compose_joint(q_plus, q_plus)
    composed_mixed = compose_joint(q_minus, q_plus)
    composition_orientation_gap = l1_gap(composed_plus, composed_mixed)
    associativity_gap = l1_gap(
        compose_joint(compose_joint(q_plus, q_plus), q_plus),
        compose_joint(q_plus, compose_joint(q_plus, q_plus)),
    )

    return [
        QOriginAudit(
            "static sealed law",
            "P,U,W",
            "try Q=Q(P,U,W)",
            f"W={work:.6f}",
            f"opposite Q gap={q_gap:.6f}",
            "same static law",
            "FAIL-NO-Q-FROM-STATIC",
        ),
        QOriginAudit(
            "boundary marginals",
            "P_minus,P_plus",
            "choose bridge Q",
            f"row gap={rows_gap:.1e}, col gap={cols_gap:.1e}",
            f"Q family gap={q_gap:.6f}",
            "same boundary marginals",
            "FAIL-BRIDGE-NONUNIQUE",
        ),
        QOriginAudit(
            "unordered pair law",
            "{i,j} records",
            "sym(Q)",
            f"sym gap={unordered_gap:.1e}",
            f"current gap={c_gap:.6f}",
            "orientation erased",
            "FAIL-UNORDERED-NO-ARROW",
        ),
        QOriginAudit(
            "causal screen order",
            "finite poset diamond",
            "minimal/maximal screens",
            f"lower={lower}; upper={upper}",
            f"unoriented shadow ok={unoriented_ok}",
            f"oriented order ok={oriented_ok}",
            "PASS-CONDITIONAL-SCREENS",
        ),
        QOriginAudit(
            "two-screen bridge",
            "ordered screens + full law",
            "Q=P(screen-,screen+)",
            f"C norm={c_norm:.6f}",
            "full two-screen law must be intrinsic",
            f"entropy prod={ep:.6f}",
            "PASS-CONDITIONAL-Q-IS-LAW",
        ),
        QOriginAudit(
            "RN arrow invariant",
            "ordered Q",
            "log dQ/dQ^rev",
            f"cycle circulation={circ:.6f}",
            "zero if detailed-balanced",
            f"EP={ep:.6f}",
            "PASS-CONDITIONAL-ARROW",
        ),
        QOriginAudit(
            "sealed composition",
            "Q12,Q23",
            "Chapman push-forward",
            f"assoc gap={associativity_gap:.1e}",
            f"orientation mix gap={composition_orientation_gap:.6f}",
            "composition sees arrow",
            "PASS-CONDITIONAL-FUNCTORIALITY",
        ),
        QOriginAudit(
            "reversible default",
            "P plus max entropy",
            "Q0=P tensor P",
            f"C0 norm={frob_norm(current(reversible)):.6f}",
            "selects no source arrow",
            f"physical C norm={c_norm:.6f}",
            "FAIL-DEFAULT-NOT-PHYSICAL",
        ),
        QOriginAudit(
            "sealed record bridge functor",
            "ordered screens, Q, composition",
            "Q primitive as boundary law",
            "C,rho,W are readouts",
            "must be physical process, not fit",
            "Einstein candidate",
            "THM-TARGET-SRBF",
        ),
        QOriginAudit(
            "branch verdict",
            "old static diamond",
            "P,U,R,W",
            "not enough",
            "Q not forced",
            "two-screen functor needed",
            "OLD-A-INCOMPLETE",
        ),
    ]


def print_audits(rows: list[QOriginAudit]) -> None:
    print("Q-origin Einsteinian campaign")
    print("-----------------------------")
    print(
        "target                    data                  construction             "
        "positive                         obstruction                     value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.data:21s} "
            f"{row.construction:24s} "
            f"{row.positive:32s} "
            f"{row.obstruction:31s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 38: Einsteinian origin of Q")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("Q is not forced by a static sealed work diamond, by boundary marginals,")
    print("or by an unordered pair law.  Those data admit opposite oriented bridges")
    print("with the same visible static facts.")
    print()
    print("Q becomes intrinsic only when the sealed diamond is a two-screen record")
    print("bridge: the causal order supplies lower and upper screens, the full")
    print("sealed law supplies the ordered boundary-to-boundary joint law, and")
    print("sealed composition supplies the functorial identity of that law under")
    print("composition and refinement.")
    print()
    print("Thus the invariant is not a chosen Q table.  It is the ordered")
    print("screen-to-screen RN record bridge.  If physical diamonds really carry")
    print("that bridge, C and rho are readouts and branch A-current can continue.")
    print("If the bridge or screen order is supplied externally, this is branch B.")


if __name__ == "__main__":
    main()
