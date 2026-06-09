"""
v6 Paper 3 section 46: sealed Leibniz record-functor campaign.

Question:
    Can the finite record-algebra functor itself be derived from the physical
    meaning of a sealed record, or is it only a new axiom?

Finite answer:
    It is not derived from an actual record transcript, repeatability alone,
    endpoint diamonds, or role marginals.  It is derived from a sharper
    physical principle:

        Sealed Leibniz record principle.
        The physical alternatives in a sealed diamond are equivalence classes
        of possible local histories under all invariant, repeatable,
        nondisturbing sealed record tests.  Two alternatives that no possible
        sealed record distinction can separate are the same physical atom.

    With nested-test compatibility and one-count-unit-per-Leibniz-atom, this
    principle constructs the record-algebra functor:

      * atoms = equivalence classes of possible histories;
      * algebra = powerset of atoms;
      * restrictions = induced maps from restricted histories;
      * roles = readout functions on the same atoms;
      * U = count/projective fiber-count reference on those atoms.

    If the possible-history law, allowed record tests, nested compatibility,
    or count-unit quotient are supplied externally, branch A remains
    conditional.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import log
from typing import Callable, Hashable


History = Hashable
Readout = Callable[[History], Hashable]


@dataclass(frozen=True)
class LeibnizAudit:
    target: str
    data: str
    invariant: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def l1(left: list[float], right: list[float]) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def equivalence_classes(histories: list[History], readouts: list[Readout]) -> list[tuple[History, ...]]:
    buckets: dict[tuple[Hashable, ...], list[History]] = {}
    for history in histories:
        signature = tuple(readout(history) for readout in readouts)
        buckets.setdefault(signature, []).append(history)
    return [tuple(values) for _, values in sorted(buckets.items(), key=lambda item: repr(item[0]))]


def boolean_size(atom_count: int) -> int:
    return 2 ** atom_count


def actualist_reference_span() -> float:
    # The actual transcript "0 occurred" is compatible with a binary possible
    # space or a ternary possible space.  The zero-action reference for the
    # same actual atom changes if the possible space is not part of the law.
    return abs(log(2.0) - log(3.0))


def apply_map(mapping: tuple[int, ...], value: int) -> int:
    return mapping[value]


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    # left after right.
    return tuple(left[right[i]] for i in range(len(right)))


def idempotence_error(mapping: tuple[int, ...]) -> int:
    return sum(1 for i, value in enumerate(compose(mapping, mapping)) if value != mapping[i])


def commutator_gap(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(1 for a, b in zip(compose(left, right), compose(right, left)) if a != b)


def hidden_response_split(histories: list[int], readouts: list[Readout], response: Readout) -> int:
    split = 0
    for block in equivalence_classes(histories, readouts):
        values = {response(history) for history in block}
        if len(values) > 1:
            split += len(values) - 1
    return split


def nested_restriction_ambiguity(
    histories_e: list[tuple[int, int]],
    readouts_e: list[Callable[[tuple[int, int]], Hashable]],
    readouts_d: list[Callable[[int], Hashable]],
    restrict: Callable[[tuple[int, int]], int],
) -> int:
    ambiguity = 0
    for block in equivalence_classes(histories_e, readouts_e):
        images = {
            tuple(readout(restrict(history)) for readout in readouts_d)
            for history in block
        }
        if len(images) > 1:
            ambiguity += len(images) - 1
    return ambiguity


def functor_path_gap() -> int:
    # F has four atoms.  F->E groups adjacent pairs, E->D is identity on two
    # atoms, so F->E->D is (0,0,1,1).  A conflicting direct F->D map would
    # make restriction depend on the chosen intermediate diamond.
    f_to_e = (0, 0, 1, 1)
    e_to_d = (0, 1)
    via_e = tuple(e_to_d[value] for value in f_to_e)
    direct_bad = (0, 1, 0, 1)
    return sum(1 for a, b in zip(via_e, direct_bad) if a != b)


def role_separate_ambiguity() -> float:
    # Same record/source marginal counts but different joint identity.
    aligned = [[0.5, 0.0], [0.0, 0.5]]
    crossed = [[0.25, 0.25], [0.25, 0.25]]
    return sum(abs(aligned[i][j] - crossed[i][j]) for i in range(2) for j in range(2))


def role_common_atom_mismatch() -> int:
    histories = [(0, 0), (0, 1), (1, 0), (1, 1)]
    record = lambda h: h[0]
    source = lambda h: h[0]
    return sum(1 for history in histories if record(history) != source(history))


def hidden_multiplicity_reference_span() -> float:
    # Two Leibniz atoms A,B with hidden representative counts 1 and 3.  Counting
    # representatives gives (1/4,3/4); counting physical atoms gives (1/2,1/2).
    return l1([0.25, 0.75], [0.5, 0.5])


def quotient_count_permutation_gap(atom_count: int = 4) -> float:
    uniform = [1.0 / atom_count] * atom_count
    swapped = [uniform[1], uniform[0], uniform[3], uniform[2]]
    return l1(uniform, swapped)


def audits() -> list[LeibnizAudit]:
    histories = list(range(6))
    parity = lambda h: h % 2
    coarse = lambda h: h // 3
    histories_nested = list(product((0, 1), (0, 1)))
    read_a = lambda h: h[0]
    read_b = lambda h: h[1]

    # Individually repeatable idempotents that do not commute.  Repeatability
    # alone therefore does not imply a joint objective record algebra.
    repeatable_left = (0, 0, 2)
    repeatable_right = (0, 1, 1)

    leibniz_classes = equivalence_classes(histories, [parity, coarse])

    return [
        LeibnizAudit(
            "actual transcript",
            "same event occurred",
            "actual outcome only",
            "actual data identical",
            "possible spaces differ",
            f"RN zero span={actualist_reference_span():.3f}",
            "FAIL-ACTUAL-NOT-MODAL",
        ),
        LeibnizAudit(
            "repeatability alone",
            "idempotent tests",
            "T^2=T",
            f"idempotence={idempotence_error(repeatable_left) + idempotence_error(repeatable_right)}",
            f"order gap={commutator_gap(repeatable_left, repeatable_right)}",
            "no joint record",
            "FAIL-REPEATABLE-NOT-BOOLEAN",
        ),
        LeibnizAudit(
            "nondisturbing tests",
            "two bit readouts",
            "joint signatures",
            f"atoms={len(equivalence_classes(histories_nested, [read_a, read_b]))}",
            "requires commutation",
            f"Boolean size={boolean_size(4)}",
            "PASS-JOINT-BOOLEAN",
        ),
        LeibnizAudit(
            "Leibniz quotient",
            "possible histories",
            "all sealed readouts",
            f"classes={len(leibniz_classes)}",
            "requires possible-test law",
            f"Boolean size={boolean_size(len(leibniz_classes))}",
            "PASS-QUOTIENT-ALGEBRA",
        ),
        LeibnizAudit(
            "incomplete readouts",
            "parity only",
            "hidden response",
            f"classes={len(equivalence_classes(histories, [parity]))}",
            f"split={hidden_response_split(histories, [parity], coarse)}",
            "not complete",
            "FAIL-HIDDEN-RESPONSE",
        ),
        LeibnizAudit(
            "completed readouts",
            "parity+response",
            "response-stable classes",
            f"classes={len(leibniz_classes)}",
            f"split={hidden_response_split(histories, [parity, coarse], coarse)}",
            "complete under tests",
            "PASS-COMPLETE-RECORD",
        ),
        LeibnizAudit(
            "nested compatibility",
            "E=(a,b), D=a",
            "restriction of tests",
            f"ambiguity={nested_restriction_ambiguity(histories_nested, [read_a, read_b], [lambda a: a], lambda h: h[0])}",
            "requires D-tests included",
            "well-defined map",
            "PASS-RESTRICTION-WELL-DEFINED",
        ),
        LeibnizAudit(
            "bad nesting",
            "E knows b, D asks a",
            "restriction attempt",
            f"ambiguity={nested_restriction_ambiguity(histories_nested, [read_b], [lambda a: a], lambda h: h[0])}",
            "same E atom has two D images",
            "no functor",
            "FAIL-NESTING-INCOMPATIBLE",
        ),
        LeibnizAudit(
            "path independence",
            "F<=E<=D",
            "restriction composition",
            "via map fixed",
            f"path gap={functor_path_gap()}",
            "direct map cannot differ",
            "FAIL-UNLESS-FUNCTORIAL",
        ),
        LeibnizAudit(
            "role ledgers",
            "same marginals",
            "separate role atoms",
            "marginals match",
            f"joint span={role_separate_ambiguity():.3f}",
            "identity not fixed",
            "FAIL-SEPARATE-ROLES",
        ),
        LeibnizAudit(
            "role readouts",
            "same quotient atom",
            "functions on atoms",
            f"mismatch={role_common_atom_mismatch()}",
            "requires common quotient",
            "one event",
            "PASS-COMMON-ROLE-READOUTS",
        ),
        LeibnizAudit(
            "hidden multiplicity",
            "two Leibniz atoms",
            "count representatives",
            "same quotient",
            f"U span={hidden_multiplicity_reference_span():.3f}",
            "multiplicity is unobservable",
            "FAIL-HIDDEN-MULTIPLICITY",
        ),
        LeibnizAudit(
            "count-unit quotient",
            "Leibniz atoms",
            "one atom one unit",
            f"perm gap={quotient_count_permutation_gap():.1e}",
            "requires no hidden multiplicity",
            "U fixed on quotient",
            "PASS-COUNT-UNIT",
        ),
        LeibnizAudit(
            "Leibniz functor theorem",
            "possible sealed records",
            "quotient+nested tests+count unit",
            "record functor constructed",
            "physical possible-change law open",
            "branch-A base principle",
            "THM-CONDITIONAL-LEIBNIZ-FUNCTOR",
        ),
    ]


def print_audits(rows: list[LeibnizAudit]) -> None:
    print("sealed Leibniz record-functor campaign")
    print("--------------------------------------")
    print(
        "target                    data                    invariant               "
        "positive                         obstruction                     value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.data:23s} "
            f"{row.invariant:23s} "
            f"{row.positive:32s} "
            f"{row.obstruction:31s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 46: sealed Leibniz record-functor campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("The record-algebra functor is not derived from actual outcomes or from")
    print("repeatability alone.  It is derived from a modal physical principle:")
    print("physical atoms are equivalence classes under all possible invariant,")
    print("repeatable, nondisturbing sealed record tests.  Nested compatibility makes")
    print("restrictions functorial, and one-count-unit-per-Leibniz-atom fixes U.")
    print()
    print("Thus the closest Einsteinian primitive is the sealed Leibniz record")
    print("principle plus the physical law of possible sealed record distinctions.")
    print("If that possible-change law is not intrinsic, branch A-current is still")
    print("conditional; if it is the physical base, the record-algebra functor is")
    print("constructed rather than chosen.")


if __name__ == "__main__":
    main()
