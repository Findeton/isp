"""
v6 Paper 3 section 21: do-delete decision ledger.

Question:
    Did the campaign derive canonical do-delete from ISP?

Finite answer:
    It derives a conditional target, not a completed theorem.  Observational
    whole-history laws do not determine do-delete.  The ISP-native route is a
    division-event factorization-repair principle with a fixed null state and
    unique boundary-preserving minimum-disturbance repair.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Decision:
    candidate: str
    do_delete: str
    gx: str
    status: str


def rows() -> list[Decision]:
    return [
        Decision("observed whole-history law", "no", "no", "REFUTED"),
        Decision("conditioning on absence", "apparent", "no", "REFUTED"),
        Decision("erasure of label", "apparent", "no", "REFUTED"),
        Decision("unconstrained KL projection", "nonunique", "no", "REFUTED"),
        Decision("SCM/Pearl intervention supplied", "yes", "yes", "BRANCH-B/INPUT"),
        Decision("division-event factor repair", "yes", "yes", "PASS-CONDITIONAL"),
        Decision("established ISP alone", "open", "open", "OPEN-THEOREM"),
    ]


def print_rows(items: list[Decision]) -> None:
    print("do-delete decision ledger")
    print("-------------------------")
    print("candidate                         do-delete   G_x   status")
    for row in items:
        print(f"{row.candidate:33s} {row.do_delete:10s} {row.gx:5s} {row.status}")
    print()


def main() -> None:
    items = rows()
    print("=" * 118)
    print("v6 Paper 3 section 21: do-delete decision ledger")
    print("=" * 118)
    print_rows(items)
    print("VERDICT")
    print("-------")
    print("The do-delete structure is not an observational consequence of a whole")
    print("history law.  It is conditionally ISP-native only if division events")
    print("come with a canonical factorization-repair operation.  Proving that is")
    print("the remaining theorem.")


if __name__ == "__main__":
    main()
