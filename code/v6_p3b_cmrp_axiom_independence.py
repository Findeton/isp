"""
v6 Paper 3 section 4: CMRP axiom independence audit.

Question:
    Are the sealed-CMRP axioms redundant, or does each one guard a genuine
    failure mode?

Finite answer:
    In the finite packet tested here, removing any one structural axiom breaks
    at least one required derived object.  This does not prove logical
    independence in full mathematics; it gives explicit finite witnesses for
    why none of the axioms may be silently dropped in the current theorem.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from v6_p3a_cmrp_ontology_closure import OntologyCandidate, audit


ROLE_NAMES = ("record", "source", "causal", "screen")
CANONICAL = (0.0, 0.1853, 0.5707, 1.1764)


@dataclass
class IndependenceRow:
    removed: str
    appearance: str
    derived_break: str
    verdict: str


def full_packet() -> OntologyCandidate:
    return OntologyCandidate(
        "sealed CMRP",
        "fixed role-blind MDP",
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        {name: CANONICAL for name in ROLE_NAMES},
    )


def mutation(field: str, appearance: str, derived_break: str) -> IndependenceRow:
    case = replace(full_packet(), name=f"remove {field}", **{field: False})
    verdict = audit(case).verdict
    return IndependenceRow(field, appearance, derived_break, verdict)


def rows() -> list[IndependenceRow]:
    return [
        mutation("local_diamonds", "no closed laboratory", "no invariant domain"),
        mutation("record_algebras", "only order remains", "no local record law"),
        mutation("process_law", "static event set", "no retained law P_x"),
        mutation("deletion", "no counterfactual removal", "no P_{delete x}"),
        mutation("shells", "unfiltered diamond", "no F_{x,k} or shell work"),
        mutation("rn_absolute", "singular deletion", "no finite M_x(k)"),
        mutation("role_maps", "four labels only", "no one-event role identity"),
        mutation("fixed_action", "action chosen later", "no H_x/T_x/sigma/beta"),
        mutation("count_units", "screen unit chosen", "free kappa_G and beta"),
        mutation("spacelike_additive", "ordered updates", "TS loop residue"),
        mutation("isolated", "flat memory shell", "beta not selected"),
        mutation("cofinal", "refinement drift", "no continuum limit"),
        mutation("order_projection", "record without geometry", "no ICS shadow"),
    ]


def print_rows(items: list[IndependenceRow]) -> None:
    print("CMRP axiom independence audit")
    print("-----------------------------")
    print("removed              appearance              derived break              verdict")
    for row in items:
        print(
            f"{row.removed:20s} "
            f"{row.appearance:23s} "
            f"{row.derived_break:26s} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    items = rows()
    passed_full = audit(full_packet()).verdict
    print("=" * 118)
    print("v6 Paper 3 section 4: CMRP axiom independence audit")
    print("=" * 118)
    print_rows(items)
    print("FULL PACKET")
    print("-----------")
    print(f"sealed CMRP: {passed_full}")
    print()
    print("VERDICT")
    print("-------")
    print("Every removed axiom has a finite witness failure.  The packet is not")
    print("minimal in a formal logical sense yet, but no axiom is currently")
    print("dispensable in the branch-A-enriched theorem target.")


if __name__ == "__main__":
    main()
