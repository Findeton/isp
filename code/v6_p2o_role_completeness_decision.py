"""
v6 Paper 2 Part II §5.27: role-completeness decision.

This script states the finite decision in one place:

- Reduced event data cannot determine d_source or beta.
- Full role-complete likelihood data determine J, hence d_source and beta.

Thus the current reduced/bare assumptions prove the opposite of the desired
branch-A closure: role-completeness is not derivable from them. A positive
branch-A theorem must add or derive the full role-complete law.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2n_full_law_p_source_audit import (
    audit_family,
    decomposition_gauge_rows,
    hidden_source_extension_rows,
    identical_full_law_rows,
    source_amplitude_rows,
)


@dataclass
class DecisionRow:
    theorem: str
    assumptions: str
    determines_beta: bool
    beta_span: float
    conclusion: str


def decision_rows() -> list[DecisionRow]:
    same_support = audit_family("same support only", source_amplitude_rows())
    full_law = audit_family("identical full law", identical_full_law_rows())
    gauge = audit_family("decomposition gauge", decomposition_gauge_rows())
    hidden = audit_family("hidden source ext", hidden_source_extension_rows())
    return [
        DecisionRow(
            theorem="negative",
            assumptions="reduced support law",
            determines_beta=False,
            beta_span=same_support.beta_span,
            conclusion="role-completeness independent",
        ),
        DecisionRow(
            theorem="positive",
            assumptions="full role law",
            determines_beta=True,
            beta_span=full_law.beta_span,
            conclusion="J fixes d_source",
        ),
        DecisionRow(
            theorem="gauge",
            assumptions="same J, relabeled p_source",
            determines_beta=True,
            beta_span=gauge.beta_span,
            conclusion="label change is not physics",
        ),
        DecisionRow(
            theorem="negative",
            assumptions="hidden source extension",
            determines_beta=False,
            beta_span=hidden.beta_span,
            conclusion="source added too late",
        ),
    ]


def print_decision(rows: list[DecisionRow]) -> None:
    print("role-completeness decision")
    print("--------------------------")
    print("theorem   assumptions              beta?  beta_span  conclusion")
    for row in rows:
        print(
            f"{row.theorem:8s}  "
            f"{row.assumptions:23s}  "
            f"{('yes' if row.determines_beta else 'no'):5s}  "
            f"{row.beta_span:9.4f}  "
            f"{row.conclusion}"
        )
    print()


def main() -> None:
    rows = decision_rows()
    print("=" * 98)
    print("v6 Paper 2 Part II §5.27: role-completeness decision")
    print("=" * 98)
    print_decision(rows)
    print("VERDICT")
    print("-------")
    print("Opposite proved for the current reduced assumptions: they do not")
    print("derive role-completeness or beta. Positive closure holds only after")
    print("the event law is strengthened or proved to be full role-complete.")


if __name__ == "__main__":
    main()
