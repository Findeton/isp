"""
v6 Paper 2 Part II §5.31: local-operator origin gate.

After §5.30, a candidate can pass only if it produces the full four-role Gram
before thresholding.  This script tests the next Branch-A demand:

    Do record, source, causal, and antichain roles come from the same local
    scalar field/record operator family?

A full Gram assembled from an independent source operator is not enough for
pure Branch A.  It is a coupled source model unless the source role is a
pre-threshold readout of the same local operator that defines the record event.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2r_full_role_gram_derivation import (
    ROLE_ORDER,
    base_role_rows,
    beta_from_gram,
    convergent_role_rows,
    gram,
    matrix_span,
    role_rows,
    weak_source_rows,
)


@dataclass
class OperatorLaw:
    rows: dict[str, list[float]]
    operator_ids: dict[str, str]
    source_stage: str
    support_id: str = "seven-click-support"
    internal_coupling: float = 0.015


@dataclass
class OperatorAudit:
    candidate: str
    full_roles: bool
    one_operator: bool
    source_pre: bool
    acv: bool
    gram_span: float
    kappa_min: float
    beta_span: float
    verdict: str


def full_roles(law: OperatorLaw) -> bool:
    return all(role in law.rows for role in ROLE_ORDER)


def one_operator(law: OperatorLaw) -> bool:
    if not full_roles(law):
        return False
    ids = [law.operator_ids.get(role) for role in ROLE_ORDER]
    return None not in ids and len(set(ids)) == 1


def audit(candidate: str, laws: list[OperatorLaw]) -> OperatorAudit:
    has_full_roles = all(full_roles(law) for law in laws)
    source_pre = all(law.source_stage == "pre" for law in laws)
    same_operator = all(one_operator(law) for law in laws)

    grams = []
    kappas = []
    betas = []
    acv_flags = []
    if has_full_roles:
        for law in laws:
            j = gram(role_rows(law, ROLE_ORDER))
            kappa, beta, ok = beta_from_gram(j, law.internal_coupling)
            grams.append(j)
            kappas.append(kappa)
            betas.append(beta)
            acv_flags.append(ok)

    gram_span = matrix_span(grams) if grams else float("inf")
    kappa_min = min(kappas) if kappas else 0.0
    beta_span = max(betas) - min(betas) if betas else float("inf")
    acv = all(acv_flags) if acv_flags else False

    passes = (
        has_full_roles
        and source_pre
        and same_operator
        and acv
        and kappa_min > 0.0
        and gram_span <= 0.07
        and beta_span <= 0.02
    )
    return OperatorAudit(
        candidate=candidate,
        full_roles=has_full_roles,
        one_operator=same_operator,
        source_pre=source_pre,
        acv=acv,
        gram_span=gram_span,
        kappa_min=kappa_min,
        beta_span=beta_span,
        verdict="PASS" if passes else "FAIL",
    )


def ids(all_id: str = "O") -> dict[str, str]:
    return {role: all_id for role in ROLE_ORDER}


def mixed_ids() -> dict[str, str]:
    return {
        "record": "O",
        "source": "Q_source",
        "causal": "O",
        "antichain": "O",
    }


def omit(rows: dict[str, list[float]], roles: list[str]) -> dict[str, list[float]]:
    return {role: rows[role] for role in roles}


def candidate_laws() -> list[tuple[str, list[OperatorLaw]]]:
    exact_single = [
        OperatorLaw(base_role_rows(0.95), ids(), "pre")
        for _ in range(4)
    ]
    convergent_single = [
        OperatorLaw(convergent_role_rows(step), ids(), "pre")
        for step in [1.00, 0.50, 0.25, 0.00]
    ]
    independent_source = [
        OperatorLaw(base_role_rows(0.95), mixed_ids(), "pre")
        for _ in range(4)
    ]
    post_source = [
        OperatorLaw(base_role_rows(strength), ids(), "post")
        for strength in [0.55, 0.75, 0.95, 1.15]
    ]
    record_only = [
        OperatorLaw(omit(base_role_rows(0.95), ["record"]), {"record": "O"}, "absent")
        for _ in range(4)
    ]
    nonconvergent_single = [
        OperatorLaw(base_role_rows(strength), ids(), "pre")
        for strength in [0.55, 1.15, 0.65, 1.05]
    ]
    weak_single = [
        OperatorLaw(weak_source_rows(strength), ids(), "pre")
        for strength in [0.04, 0.05, 0.06, 0.05]
    ]
    return [
        ("exact single local O", exact_single),
        ("convergent single O", convergent_single),
        ("independent source Q", independent_source),
        ("post-selected source", post_source),
        ("record-only O", record_only),
        ("nonconvergent single O", nonconvergent_single),
        ("weak source single O", weak_single),
    ]


def print_audits(rows: list[OperatorAudit]) -> None:
    print("local-operator origin gate")
    print("--------------------------")
    print(
        "candidate                roles  oneO  src_pre  ACV   "
        "J_span  kappa_min  beta_span  verdict"
    )
    for row in rows:
        j_span = "inf" if row.gram_span == float("inf") else f"{row.gram_span:7.4f}"
        b_span = "inf" if row.beta_span == float("inf") else f"{row.beta_span:9.4f}"
        print(
            f"{row.candidate:24s}  "
            f"{('yes' if row.full_roles else 'no'):5s}  "
            f"{('yes' if row.one_operator else 'no'):4s}  "
            f"{('yes' if row.source_pre else 'no'):7s}  "
            f"{('PASS' if row.acv else 'FAIL'):4s}  "
            f"{j_span:>7s}  "
            f"{row.kappa_min:9.4f}  "
            f"{b_span:>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(name, laws) for name, laws in candidate_laws()]
    print("=" * 104)
    print("v6 Paper 2 Part II §5.31: local-operator origin gate")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("A full pre-threshold Gram is not enough if its source row comes")
    print("from an independent source operator.  Branch A requires all four")
    print("roles to be readouts of the same local scalar operator family,")
    print("with positive source response and cofinal Gram convergence.")


if __name__ == "__main__":
    main()
