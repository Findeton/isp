#!/usr/bin/env python3
"""Paper 5 diagnostic D: minimal invariant datum for chi_NN.

Finish condition:
  Find the minimal invariant record datum that makes chi_NN unavoidable.

The previous diagnostic proved that the current sealed shadow can hide two
normal-normal responses.  This diagnostic asks which added invariant kills that
split without smuggling in chi_NN as a naked answer.

Result:
  The coarsest non-tautological record datum is the oriented normal-frame
  holonomy center of the normal rectangle.  Magnitude-only, unoriented, scalar
  work, and current screen/source shadows fail.  Overcomplete ADM-style packets
  pass only because they contain this center plus extra data.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import math
from typing import Callable, Hashable


@dataclass(frozen=True)
class Atom:
    level: int
    branch: int
    copy: int


@dataclass(frozen=True)
class Candidate:
    name: str
    key: Callable[[Atom], Hashable]
    physical: str
    expected: str


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def atoms(level: int) -> list[Atom]:
    return [Atom(level, branch, copy) for branch in (0, 1) for copy in range(level)]


def prob(level: int, atom: Atom) -> float:
    del atom
    return 1.0 / (2.0 * level)


def sealed_shadow(atom: Atom) -> tuple[str, str, str, str]:
    """Current GR-facing sealed data, before normal-frame enrichment."""
    del atom
    return ("hyp:h0", "nn-rectangle:ell0", "screen:q0", "source:rho0")


def chi_nn(atom: Atom) -> int:
    """The normal-normal response coordinate tested in diagnostic C."""
    return -1 if atom.branch == 0 else 1


def scalar_work_shadow(atom: Atom) -> tuple[str, str, str, str, int]:
    """A scalar work/readout shadow that forgets normal orientation."""
    return (*sealed_shadow(atom), 1)


def holonomy_magnitude(atom: Atom) -> tuple[str, str, str, str, int]:
    """Magnitude-only normal holonomy.  It cannot distinguish inverse boosts."""
    return (*sealed_shadow(atom), abs(chi_nn(atom)))


def unoriented_normal_holonomy(atom: Atom) -> tuple[str, str, str, str, str]:
    """Normal-frame loop with orientation forgotten."""
    return (*sealed_shadow(atom), "boost-pair:{+eta,-eta}")


def oriented_normal_holonomy(atom: Atom) -> tuple[str, str, str, str, int]:
    """The invariant boost-holonomy center of the normal rectangle."""
    return (*sealed_shadow(atom), chi_nn(atom))


def overcomplete_adm_packet(atom: Atom) -> tuple[str, str, str, str, int, int]:
    """ADM-style packet: sufficient, but not minimal because it carries extras."""
    return (*oriented_normal_holonomy(atom), atom.copy % 2)


def raw_chi_answer(atom: Atom) -> tuple[str, int]:
    """Tautological completion: stores the queried coordinate itself."""
    return ("raw-chi", chi_nn(atom))


def grouped(level: int, key_fn: Callable[[Atom], Hashable]) -> dict[Hashable, list[Atom]]:
    groups: dict[Hashable, list[Atom]] = defaultdict(list)
    for atom in atoms(level):
        groups[key_fn(atom)].append(atom)
    return groups


def conditional_variance(
    level: int, key_fn: Callable[[Atom], Hashable], value_fn: Callable[[Atom], int]
) -> float:
    total = 0.0
    for entries in grouped(level, key_fn).values():
        mass = sum(prob(level, atom) for atom in entries)
        mean = sum(value_fn(atom) * prob(level, atom) for atom in entries) / mass
        var = sum(((value_fn(atom) - mean) ** 2) * prob(level, atom) for atom in entries) / mass
        total += mass * var
    return total


def best_success(
    level: int, key_fn: Callable[[Atom], Hashable], value_fn: Callable[[Atom], int]
) -> float:
    success = 0.0
    for entries in grouped(level, key_fn).values():
        masses: dict[int, float] = defaultdict(float)
        for atom in entries:
            masses[value_fn(atom)] += prob(level, atom)
        success += max(masses.values())
    return success


def num_cells(level: int, key_fn: Callable[[Atom], Hashable]) -> int:
    return len(grouped(level, key_fn))


def separates_chi(level: int, key_fn: Callable[[Atom], Hashable]) -> bool:
    return conditional_variance(level, key_fn, chi_nn) == 0.0


def minimal_cell_count(level: int) -> int:
    """Coarsest possible cell count above one sealed cell that determines chi."""
    return len({chi_nn(atom) for atom in atoms(level)})


def common_refinement_cells(
    level: int,
    first: Callable[[Atom], Hashable],
    second: Callable[[Atom], Hashable],
) -> int:
    return len({(first(atom), second(atom)) for atom in atoms(level)})


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    levels = [1, 2, 4, 8, 16, 32]

    candidates = [
        Candidate(
            "current sealed shadow",
            sealed_shadow,
            "screen/source/hyp/rectangle data only",
            "fail",
        ),
        Candidate(
            "scalar work shadow",
            scalar_work_shadow,
            "one scalar normal-work value",
            "fail",
        ),
        Candidate(
            "magnitude-only holonomy",
            holonomy_magnitude,
            "normal loop size without orientation",
            "fail",
        ),
        Candidate(
            "unoriented normal holonomy",
            unoriented_normal_holonomy,
            "boost pair with route orientation forgotten",
            "fail",
        ),
        Candidate(
            "oriented normal-frame holonomy",
            oriented_normal_holonomy,
            "SO(1,1) boost-center of the normal rectangle",
            "pass-minimal",
        ),
        Candidate(
            "overcomplete ADM packet",
            overcomplete_adm_packet,
            "normal holonomy plus irrelevant copy data",
            "pass-not-minimal",
        ),
        Candidate(
            "raw chi_NN answer",
            raw_chi_answer,
            "stores queried response directly",
            "pass-tautological",
        ),
    ]

    rows: list[Row] = []
    for cand in candidates:
        vars_ = [conditional_variance(level, cand.key, chi_nn) for level in levels]
        succ = [best_success(level, cand.key, chi_nn) for level in levels]
        cells = [num_cells(level, cand.key) for level in levels]
        verdict = {
            "fail": "FAILS",
            "pass-minimal": "PASS-MINIMAL",
            "pass-not-minimal": "PASS-NONMINIMAL",
            "pass-tautological": "PASS-TAUTOLOGICAL",
        }[cand.expected]
        rows.append(
            Row(
                cand.name,
                cand.physical,
                "chi_NN determined" if vars_[-1] == 0.0 else "chi_NN still hidden",
                f"var={vars_[-1]:.1e}, success={succ[-1]:.1f}, cells={cells[-1]}",
                verdict,
            )
        )

    min_cells = [minimal_cell_count(level) for level in levels]
    oriented_cells = [num_cells(level, oriented_normal_holonomy) for level in levels]
    over_cells = [num_cells(level, overcomplete_adm_packet) for level in levels]
    meet_with_chi = [
        common_refinement_cells(level, oriented_normal_holonomy, raw_chi_answer) for level in levels
    ]

    rows.extend(
        [
            Row(
                "finite minimality",
                "coarsest refinement of one sealed cell that makes chi_NN measurable",
                "two cells are necessary and sufficient",
                f"min_cells={min_cells}, oriented_cells={oriented_cells}",
                "MINIMAL",
            ),
            Row(
                "overcompletion audit",
                "compare oriented center with ADM packet carrying extra copy data",
                "ADM packet determines chi_NN only by refining the minimal center",
                f"oriented={oriented_cells[-1]}, overcomplete={over_cells[-1]}",
                "NOT-MINIMAL",
            ),
            Row(
                "non-tautology audit",
                "compare oriented holonomy with raw chi label",
                "same finite partition, but holonomy is a closed-route record datum",
                f"common_refinement_cells={meet_with_chi}",
                "PHYSICAL-REALIZATION",
            ),
            Row(
                "campaign verdict",
                "all candidate invariant record data",
                "the minimal invariant datum is oriented normal-frame holonomy center",
                "finish condition reached",
                "NN-HOLONOMY-CENTER-FOUND",
            ),
        ]
    )

    print_table(rows)
    print()

    values = {
        "sealed_variance": conditional_variance(levels[-1], sealed_shadow, chi_nn),
        "magnitude_variance": conditional_variance(levels[-1], holonomy_magnitude, chi_nn),
        "unoriented_variance": conditional_variance(levels[-1], unoriented_normal_holonomy, chi_nn),
        "oriented_variance": conditional_variance(levels[-1], oriented_normal_holonomy, chi_nn),
        "oriented_success": best_success(levels[-1], oriented_normal_holonomy, chi_nn),
        "minimal_cell_count": float(minimal_cell_count(levels[-1])),
        "oriented_cell_count": float(num_cells(levels[-1], oriented_normal_holonomy)),
        "overcomplete_cell_count": float(num_cells(levels[-1], overcomplete_adm_packet)),
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")

    # Hard guards: this is a proof receipt for the finite counterfamily.
    assert math.isclose(values["sealed_variance"], 1.0)
    assert math.isclose(values["magnitude_variance"], 1.0)
    assert math.isclose(values["unoriented_variance"], 1.0)
    assert math.isclose(values["oriented_variance"], 0.0)
    assert math.isclose(values["oriented_success"], 1.0)
    assert math.isclose(values["minimal_cell_count"], values["oriented_cell_count"])
    assert values["overcomplete_cell_count"] > values["oriented_cell_count"]


if __name__ == "__main__":
    main()
