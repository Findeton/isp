"""
v6 Paper 2 Part II §5.41: role-sector origin attack.

The §5.40 canonical lock says that a one-dimensional isolated role-sector
operator L_x would fix the four IDA-germ directions.  This script attacks the
origin of L_x.

Result:
    An isolated sector operator is not enough if its eigenvectors are chosen
    externally.  The same Physical ICS base data can be paired with different
    isolated L_x choices, moving beta.  Branch A needs L_x to be derived from
    the Physical-ICS deletion dynamics itself.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2aa_ida_germ_uniqueness_attack import (
    beta_span_from_grams,
    beta_span_from_rows,
    nonconvergent_family,
    role_rotation_family,
    source_row_family,
)
from v6_p2ab_canonical_ida_germ_lock import canonical_family, weak_source_family


@dataclass
class OriginAudit:
    candidate: str
    l_exists: str
    l_intrinsic: str
    sectors_isolated: str
    labels_from_law: str
    source_internal: str
    convergence: str
    beta_span: float
    verdict: str


def audits() -> list[OriginAudit]:
    no_l_span = beta_span_from_rows(source_row_family())
    external_l_span = beta_span_from_grams(role_rotation_family())
    drift_span = beta_span_from_rows(nonconvergent_family())
    canonical_span = beta_span_from_rows(canonical_family())
    weak_span = beta_span_from_rows(weak_source_family())
    return [
        OriginAudit(
            "no role-sector operator",
            "no",
            "no",
            "no",
            "no",
            "no",
            "no",
            no_l_span,
            "FAIL",
        ),
        OriginAudit(
            "external isolated L",
            "yes",
            "no",
            "yes",
            "no",
            "yes",
            "no",
            external_l_span,
            "FAIL",
        ),
        OriginAudit(
            "automorphism-degenerate L",
            "yes",
            "partial",
            "no",
            "no",
            "yes",
            "no",
            external_l_span,
            "FAIL",
        ),
        OriginAudit(
            "hessian eigenbasis only",
            "yes",
            "partial",
            "yes",
            "no",
            "no",
            "no",
            float("inf"),
            "FAIL",
        ),
        OriginAudit(
            "source-external sector",
            "yes",
            "no",
            "yes",
            "yes",
            "no",
            "no",
            no_l_span,
            "FAIL",
        ),
        OriginAudit(
            "intrinsic L with drift",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "no",
            drift_span,
            "FAIL",
        ),
        OriginAudit(
            "intrinsic weak-source L",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            "yes",
            weak_span,
            "FAIL",
        ),
        OriginAudit(
            "intrinsic canonical L",
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


def print_audits(rows: list[OriginAudit]) -> None:
    print("role-sector origin attack")
    print("-------------------------")
    print(
        "candidate                  L     intrinsic  isolated  labels  source  "
        "conv  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:25s}  "
            f"{row.l_exists:5s}  "
            f"{row.l_intrinsic:9s}  "
            f"{row.sectors_isolated:8s}  "
            f"{row.labels_from_law:6s}  "
            f"{row.source_internal:6s}  "
            f"{row.convergence:4s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = audits()
    print("=" * 104)
    print("v6 Paper 2 Part II §5.41: role-sector origin attack")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("The final finite residue is the origin of L_x.  An isolated sector")
    print("operator that is external, automorphism-degenerate, unlabeled,")
    print("source-external, drifting, or weak-source fails.  The surviving theorem")
    print("target is an intrinsic Physical-ICS deletion-dynamics operator L_x whose")
    print("four isolated sectors are record, source, causal, and antichain.")


if __name__ == "__main__":
    main()
