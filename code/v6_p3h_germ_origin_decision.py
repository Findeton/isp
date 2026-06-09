"""
v6 Paper 3 section 18: sealed-germ origin decision ledger.

Question:
    After the Feynman/origin campaign, do we have a derivation of G_x from
    established ISP principles, or only a conditional finite generation class?

Finite answer:
    We have a conditional finite generation class, not a derivation from
    established ISP alone.  The exact missing theorem is that ISP supplies the
    strict event-intervention/deletion structure, canonical shell ranks,
    role-blind maps, fixed units/action, and cofinal uniqueness.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DecisionRow:
    candidate: str
    input: str
    gx: str
    mdp: str
    beta: str
    status: str


def rows() -> list[DecisionRow]:
    return [
        DecisionRow(
            "bare ICS",
            "order+count",
            "no",
            "no",
            "no",
            "REFUTED",
        ),
        DecisionRow(
            "retained whole law only",
            "P_x",
            "no",
            "no",
            "no",
            "REFUTED",
        ),
        DecisionRow(
            "free deletion/shells",
            "P_x plus choices",
            "nonunique",
            "yes",
            "nonunique",
            "REFUTED",
        ),
        DecisionRow(
            "hand profile",
            "M_x(k) supplied",
            "no",
            "yes",
            "yes",
            "BRANCH-B",
        ),
        DecisionRow(
            "whole-history channel",
            "P_x,P_delete,F",
            "partial",
            "yes",
            "yes",
            "CONDITIONAL",
        ),
        DecisionRow(
            "canonical event intervention",
            "strict do-delete law",
            "yes",
            "yes",
            "yes",
            "PASS-CONDITIONAL",
        ),
        DecisionRow(
            "established ISP alone",
            "current principles",
            "open",
            "open",
            "open",
            "OPEN-THEOREM",
        ),
    ]


def print_rows(items: list[DecisionRow]) -> None:
    print("sealed-germ origin decision ledger")
    print("----------------------------------")
    print("candidate                     input                  G_x        MDP   beta  status")
    for row in items:
        print(
            f"{row.candidate:29s} "
            f"{row.input:22s} "
            f"{row.gx:10s} "
            f"{row.mdp:5s} "
            f"{row.beta:5s} "
            f"{row.status}"
        )
    print()


def main() -> None:
    items = rows()
    print("=" * 118)
    print("v6 Paper 3 section 18: sealed-germ origin decision ledger")
    print("=" * 118)
    print_rows(items)
    print("VERDICT")
    print("-------")
    print("The campaign does not prove G_x from established ISP alone.  It proves")
    print("a conditional finite generation theorem target: ISP must supply a strict")
    print("canonical event-intervention/deletion law.  Without that, G_x is an")
    print("enriched branch-B primitive or selected modular kernel.")


if __name__ == "__main__":
    main()
