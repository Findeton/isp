#!/usr/bin/env python3
"""Score the frozen WRC Paper 8 fixture and render sealed artifacts.

The scorer imports only the already frozen generic core.  It reconstructs the
committed walk from data, derives every packet coordinate, and chooses a
pre-registered outcome without reading any review report or target answer.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import os
import re
import sys
import tempfile
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, MutableMapping, Sequence

import wrc_core as core


Q = Fraction
EW = core.EW
Matrix = core.Matrix
Vector = core.Vector

PRIMARY_WORDS = (
    "WRC-WALK-PACKET-RECONSTRUCTED",
    "WRC-WALK-REPRESENTABLE-MODULO-CELL-HIT-INSTRUMENT",
    "WRC-WALK-REPRESENTABLE-MODULO-RECORD-BEABLE-MAP",
    "WRC-WALK-REPRESENTABLE-MODULO-CELL-HIT-INSTRUMENT-AND-RECORD-BEABLE-MAP",
    "WRC-WALK-REFUSES-CREATION-EVENT-REPRESENTATION",
    "WRC-BLOCKED-AT-PACKET-REFERENT",
    "WRC-INCONSISTENT",
)

QUALIFIER_WORDS = (
    "FIXED-CARRIER-TRANSPORT-RECONSTRUCTED",
    "DECLARED-CLOCK-AND-CUTS-RECONSTRUCTED",
    "REGISTERED-OBSERVABLES-RECONSTRUCTED",
    "TRANSLATION-COVARIANT-WITH-TRANSFORMED-STATE-AND-RECORD",
    "ARENA-EXTENSION-UNBUILT",
    "CELL-HIT-BEABLE-DICTIONARY-RECONSTRUCTED",
    "NONCOLLAPSE-CELL-HIT-MAP-NONAFFINE",
    "AFFINE-CP-REPAIR-MOVES-CONDITIONED-FUTURE",
    "ONTIC-PSI-EXTENSION-EXACT-BUT-OUTSIDE-AFFINE-CLASS",
    "RECURRING-VERTEX-COUPLINGS-EXTRACTED-NOT-SELECTED",
    "STATE-DEPENDENT-BORN-WEIGHTS-NOT-CONSTANTS",
    "WALK-IS-IMPORTED-CANDIDATE-DYNAMICS-NOT-DERIVED-LAW",
    "Q8-RETIRED-AT-COMMITTED-FINITE-ARENA",
)

MUTANTS = (
    "anchor-hash",
    "anchor-token",
    "receipt-binding",
    "carrier-catalogue",
    "cell-dictionary",
    "coin-entry",
    "phase-power",
    "shift-orientation",
    "initial-state",
    "cut-order",
    "born-normalization",
    "branch-state",
    "record-increment",
    "beable-histogram",
    "mixture-affinity",
    "cp-completeness",
    "cp-state",
    "continuation",
    "translation-action",
    "record-translation",
    "absolute-anchor",
    "gauge-phase",
    "recurrence-signature",
    "hidden-coin",
    "coupling-typing",
    "arena-scope",
    "cell-hit-type",
    "clock-boundary",
    "primary-comparator",
    "q8-retirement",
    "exact-arithmetic",
    "transcript-binding",
    "paper-claim",
    "prewrite-seal",
)

REQUIRED_WALLS = {
    "NO-FUNDAMENTAL-LAW-SELECTION",
    "NO-CARRIER-GROWTH",
    "NO-ALL-ARENA-EXTENSION",
    "NO-GENUINE-DIVISION-BOUNDARY",
    "NO-GRAVITY-OR-RELATIONAL-GRAPH-BACKREACTION",
    "NO-CONTINUUM-OR-LORENTZ",
    "NO-QFT-OR-GR",
    "NO-PARTICLES-SPECIES-OR-STATISTICS",
    "NO-HAMILTONIAN-RECONSTRUCTION",
    "NO-CONSTANT-SELECTION",
    "NO-STEERING-BELL-OR-EPR-EQUIVALENCE",
    "NO-ACTUALIZATION",
    "NO-EMPIRICAL-DEVIATION",
}


class GateFail(RuntimeError):
    """A WRC gate failed before any artifact write."""


def root_path() -> Path:
    return Path(__file__).resolve().parents[2]


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest(value: Any) -> str:
    return sha256_bytes(canonical_json(value))


def qtext(value: Q) -> str:
    return core.qtext(Q(value))


def contains_float(value: Any) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, Mapping):
        return any(contains_float(key) or contains_float(item) for key, item in value.items())
    if isinstance(value, (list, tuple)):
        return any(contains_float(item) for item in value)
    return False


def key_census(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, Mapping):
        for key, item in value.items():
            result.add(str(key).lower())
            result.update(key_census(item))
    elif isinstance(value, (list, tuple)):
        for item in value:
            result.update(key_census(item))
    return result


def gate(rows: list[dict[str, Any]], name: str, statement: str, ok: bool, evidence: Mapping[str, Any]) -> None:
    row = {"gate": name, "statement": statement, "ok": bool(ok), "evidence": dict(evidence)}
    rows.append(row)
    if not ok:
        raise GateFail(f"{name}: {json.dumps(dict(evidence), sort_keys=True)}")


def jpath(value: Any, pointer: Sequence[Any]) -> Any:
    current = value
    for token in pointer:
        current = current[token]
    return current


def parse_ew(value: Any) -> EW:
    if isinstance(value, int):
        return EW(value)
    if isinstance(value, str):
        return EW(Q(value))
    if isinstance(value, list) and len(value) == 2:
        return EW(Q(value[0]), Q(value[1]))
    raise TypeError(f"invalid exact Eisenstein scalar {value!r}")


def parse_fraction(value: Any) -> Q:
    item = parse_ew(value)
    if item.b != 0:
        raise TypeError("expected real fraction")
    return item.a


def parse_matrix(value: Sequence[Sequence[Any]], denominator: Any = 1) -> Matrix:
    divisor = Q(denominator)
    return core.matrix([[parse_ew(entry) / divisor for entry in row] for row in value])


def apply_mutant(fixture: MutableMapping[str, Any], mutant: str | None) -> None:
    if mutant is None:
        return
    if mutant not in MUTANTS:
        raise ValueError(f"unknown mutant {mutant!r}")
    source = fixture["source_packet"]
    controls = fixture["controls"]
    if mutant == "anchor-hash":
        fixture["anchors"][0]["sha256"] = "0" * 64
    elif mutant == "anchor-token":
        fixture["anchors"][0]["tokens"][0] += " MUTATED"
    elif mutant == "receipt-binding":
        fixture["committed_receipt_bindings"][1]["committed_value"] -= 1
    elif mutant == "carrier-catalogue":
        source["sites"].pop()
    elif mutant == "cell-dictionary":
        source["links"][2] = list(source["links"][1])
    elif mutant == "coin-entry":
        source["coin_numerators"][0][0] += 1
    elif mutant == "phase-power":
        source["phase_powers"][1] = [1, 0]
    elif mutant == "shift-orientation":
        source["shift_orientation"] = "MINUS"
    elif mutant == "initial-state":
        source["initial_coin"] = 2
    elif mutant == "cut-order":
        source["cuts"] = [source["cuts"][0], source["cuts"][2], source["cuts"][1]]
    elif mutant == "born-normalization":
        controls["born_scale"] = "2"
    elif mutant == "branch-state":
        controls["literal_branch_mode"] = "COLLAPSE"
    elif mutant == "record-increment":
        controls["record_increment"] = 2
    elif mutant == "beable-histogram":
        source["beable_readout"] = "ORDERED-HISTORY"
    elif mutant == "mixture-affinity":
        controls["affinity_postcoin_cells"] = [0, 0]
    elif mutant == "cp-completeness":
        controls["drop_cp_port"] = True
    elif mutant == "cp-state":
        controls["cp_branch_mode"] = "NONCOLLAPSE"
    elif mutant == "continuation":
        controls["continuation_postcoin_vector"] = ["1", "0"]
    elif mutant == "translation-action":
        controls["translation_vectors"] = [[0, 0], [0, 0]]
    elif mutant == "record-translation":
        controls["translate_record"] = False
    elif mutant == "absolute-anchor":
        controls["absolute_anchor_site"] = [1, 0]
    elif mutant == "gauge-phase":
        controls["gauge_phase_power"] = 0
    elif mutant == "recurrence-signature":
        controls["signature_uses_site_name"] = True
    elif mutant == "hidden-coin":
        controls["hidden_coin_numerators"] = [
            [[-1, 0], [2, 0], [2, 0]],
            [[2, 0], [-1, 0], [2, 0]],
            [[2, 0], [2, 0], [-1, 0]],
        ]
    elif mutant == "coupling-typing":
        controls["born_weights_are_constants"] = True
    elif mutant == "arena-scope":
        fixture["scope_walls"].remove("NO-ALL-ARENA-EXTENSION")
    elif mutant == "cell-hit-type":
        controls["cell_hit_type"] = "THREE-ACTOR-DIVISION-EVENT"
    elif mutant == "clock-boundary":
        source["cuts"] = ["INPUT", "GENUINE-DIVISION-BOUNDARY", "POST-SHIFT-OUTPUT"]
    elif mutant == "primary-comparator":
        controls["primary_word_offset"] = 1
    elif mutant == "q8-retirement":
        controls["retire_q8"] = False
    elif mutant == "exact-arithmetic":
        source["field_order"] = float("3")
    elif mutant == "transcript-binding":
        controls["transcript_suffix"] = "MUTATED\n"
    elif mutant == "paper-claim":
        controls["paper_claim_corruption"] = True
    elif mutant == "prewrite-seal":
        controls["prewrite_corruption"] = True


def vadd(left: tuple[int, int], right: tuple[int, int], order: int) -> tuple[int, int]:
    return ((left[0] + right[0]) % order, (left[1] + right[1]) % order)


def vsub(left: tuple[int, int], right: tuple[int, int], order: int) -> tuple[int, int]:
    return ((left[0] - right[0]) % order, (left[1] - right[1]) % order)


class WalkArena:
    def __init__(self, source: Mapping[str, Any]) -> None:
        self.order = int(source["field_order"])
        self.sites = tuple(tuple(int(item) for item in site) for site in source["sites"])
        self.site_index = {site: index for index, site in enumerate(self.sites)}
        self.links = tuple(tuple(int(item) for item in link) for link in source["links"])
        self.link_count = len(self.links)
        self.dimension = len(self.sites) * self.link_count
        self.phases = tuple(parse_ew(value) for value in source["phase_powers"])
        self.coin = parse_matrix(source["coin_numerators"], source["coin_denominator"])
        self.orientation = source["shift_orientation"]

    def cell(self, site: int, link: int) -> int:
        return site * self.link_count + link

    def cell_pair(self, cell: int) -> frozenset[tuple[int, int]]:
        site, link = divmod(cell, self.link_count)
        here = self.sites[site]
        return frozenset((here, vadd(here, self.links[link], self.order)))

    def shift_images(self) -> tuple[int, ...]:
        result = []
        for site, here in enumerate(self.sites):
            for link, direction in enumerate(self.links):
                there = (
                    vadd(here, direction, self.order)
                    if self.orientation == "PLUS"
                    else vsub(here, direction, self.order)
                )
                result.append(self.cell(self.site_index[there], link))
        return tuple(result)

    def shift_matrix(self) -> Matrix:
        return core.permutation(self.shift_images())

    def coin_apply(self, state: Vector, record: Sequence[int], coin: Matrix | None = None) -> Vector:
        local = self.coin if coin is None else coin
        if len(state) != self.dimension or len(record) != self.dimension:
            raise ValueError("walk state/record dimension mismatch")
        result = [core.ZERO for _ in range(self.dimension)]
        for site in range(len(self.sites)):
            base = site * self.link_count
            phased = [
                state[base + link] * self.phases[record[base + link] % self.order]
                for link in range(self.link_count)
            ]
            for row in range(self.link_count):
                result[base + row] = sum(
                    (local[row][column] * phased[column] for column in range(self.link_count)),
                    core.ZERO,
                )
        return tuple(result)

    def shift_apply(self, state: Vector) -> Vector:
        result = [core.ZERO for _ in range(self.dimension)]
        for source, target in enumerate(self.shift_images()):
            result[target] = state[source]
        return tuple(result)

    def step(self, state: Vector, record: Sequence[int], coin: Matrix | None = None) -> tuple[Vector, Vector]:
        postcoin = self.coin_apply(state, record, coin)
        return self.shift_apply(postcoin), postcoin

    def coin_matrix(self, record: Sequence[int], coin: Matrix | None = None) -> Matrix:
        local = self.coin if coin is None else coin
        rows = [[core.ZERO for _ in range(self.dimension)] for _ in range(self.dimension)]
        for site in range(len(self.sites)):
            base = site * self.link_count
            for row in range(self.link_count):
                for column in range(self.link_count):
                    rows[base + row][base + column] = (
                        local[row][column] * self.phases[record[base + column] % self.order]
                    )
        return tuple(tuple(row) for row in rows)

    def translation_images(self, translation: tuple[int, int]) -> tuple[int, ...]:
        result = []
        for site, here in enumerate(self.sites):
            moved = vadd(here, translation, self.order)
            for link in range(self.link_count):
                result.append(self.cell(self.site_index[moved], link))
        return tuple(result)

    def translate_record(self, record: Sequence[int], translation: tuple[int, int]) -> tuple[int, ...]:
        result = [0 for _ in range(self.dimension)]
        for source, target in enumerate(self.translation_images(translation)):
            result[target] = int(record[source])
        return tuple(result)


def initial_state(arena: WalkArena, source: Mapping[str, Any]) -> Vector:
    values = [core.ZERO for _ in range(arena.dimension)]
    site = arena.site_index[tuple(source["initial_site"])]
    values[arena.cell(site, int(source["initial_coin"]))] = core.ONE
    return tuple(values)


def q_form(counts: Sequence[int]) -> tuple[Q, Q, Q, Q]:
    first, second, diagonal = (Q(item) for item in counts)
    off = (diagonal - first - second) / 2
    return first, second, off, first * second - off * off


def admissible(counts: Sequence[int]) -> bool:
    first, _second, _off, determinant = q_form(counts)
    return first > 0 and determinant > 0


def curvature(arena: WalkArena, record: Sequence[int]) -> tuple[int, ...]:
    values = []
    for site, here in enumerate(arena.sites):
        second_site = arena.site_index[vadd(here, arena.links[0], arena.order)]
        values.append(
            (
                record[arena.cell(site, 0)]
                + record[arena.cell(second_site, 1)]
                - record[arena.cell(site, 2)]
            )
            % arena.order
        )
    return tuple(values)


def record_stats(arena: WalkArena, record: Sequence[int], initial_entry: int) -> dict[str, Any]:
    determinants: set[Q] = set()
    positive = 0
    for site in range(len(arena.sites)):
        counts = record[site * arena.link_count : (site + 1) * arena.link_count]
        determinant = q_form(counts)[3]
        determinants.add(determinant)
        positive += int(admissible(counts))
    return {
        "positive_sites": positive,
        "determinants": determinants,
        "max_cell": max(record),
        "curvature_constant": len(set(curvature(arena, record))) == 1,
        "increments": tuple(int(value) - initial_entry for value in record),
    }


def run_walk(
    arena: WalkArena,
    source: Mapping[str, Any],
    coin: Matrix | None = None,
    born_scale: Q = Q(1),
    record_increment: int = 1,
) -> dict[str, Any]:
    horizon = int(source["horizon"])
    initial_entry = int(source["initial_record_entry"])
    record0 = tuple(initial_entry for _ in range(arena.dimension))
    state0 = initial_state(arena, source)
    frontier: list[tuple[Vector, tuple[int, ...], Q]] = [(state0, record0, Q(1))]
    branch_counts: list[int] = []
    mass_rows: list[Q] = []
    recurrence_tokens: dict[tuple[Any, ...], set[tuple[int, int, int]]] = defaultdict(set)
    final_site_mass = [Q(0) for _ in arena.sites]
    final_exit = Q(0)
    final_posdef: dict[int, Q] = defaultdict(Q)
    final_determinants: set[Q] = set()
    final_max = 0
    final_curvature = Q(0)
    final_record_increments = [Q(0) for _ in range(arena.dimension)]
    final_history_count = 0
    final_stats_cache: dict[tuple[int, ...], dict[str, Any]] = {}

    for step_index in range(horizon):
        last = step_index + 1 == horizon
        next_frontier: list[tuple[Vector, tuple[int, ...], Q]] = []
        level_mass = Q(0)
        level_count = 0
        for history_index, (state, record, history_weight) in enumerate(frontier):
            output, postcoin = arena.step(state, record, coin)
            if core.norm2(state) != 1 or core.norm2(postcoin) != 1 or core.norm2(output) != 1:
                raise GateFail("WALK-NORM")
            probabilities = [entry.norm2() * born_scale for entry in postcoin]
            if sum(probabilities) != 1:
                raise GateFail("WALK-BORN-NORMALIZATION")

            if step_index < int(source["recurrence_horizon"]):
                for site in range(len(arena.sites)):
                    residues = tuple(record[arena.cell(site, link)] % arena.order for link in range(arena.link_count))
                    recurrence_tokens[residues].add((step_index, history_index, site))

            if last:
                for site in range(len(arena.sites)):
                    site_mass = sum(output[arena.cell(site, link)].norm2() for link in range(arena.link_count))
                    final_site_mass[site] += history_weight * site_mass

            for cell, probability in enumerate(probabilities):
                if probability == 0:
                    continue
                weight = history_weight * probability
                changed = list(record)
                changed[cell] += record_increment
                new_record = tuple(changed)
                level_count += 1
                level_mass += weight
                if not last:
                    next_frontier.append((output, new_record, weight))
                    continue
                final_history_count += 1
                stats = final_stats_cache.get(new_record)
                if stats is None:
                    stats = record_stats(arena, new_record, initial_entry)
                    final_stats_cache[new_record] = stats
                final_posdef[stats["positive_sites"]] += weight
                if stats["positive_sites"] < len(arena.sites):
                    final_exit += weight
                final_determinants.update(stats["determinants"])
                final_max = max(final_max, stats["max_cell"])
                if stats["curvature_constant"]:
                    final_curvature += weight
                for index, increment in enumerate(stats["increments"]):
                    final_record_increments[index] += weight * increment
        branch_counts.append(level_count)
        mass_rows.append(level_mass)
        frontier = next_frontier

    ipr = sum(value * value for value in final_site_mass)
    return {
        "branch_counts": branch_counts,
        "mass_rows": mass_rows,
        "site_mass": final_site_mass,
        "ipr": ipr,
        "exit_probability": final_exit,
        "posdef_distribution": dict(final_posdef),
        "determinants": final_determinants,
        "max_cell": final_max,
        "curvature_constant_probability": final_curvature,
        "record_increment_field": final_record_increments,
        "final_history_count": final_history_count,
        "recurrence_tokens": recurrence_tokens,
    }


def short_beable_census(arena: WalkArena, source: Mapping[str, Any], record_increment: int) -> dict[str, Any]:
    record0 = tuple(int(source["initial_record_entry"]) for _ in range(arena.dimension))
    frontier: list[tuple[Vector, tuple[int, ...], tuple[int, ...]]] = [
        (initial_state(arena, source), record0, tuple())
    ]
    violations = 0
    for _step in range(2):
        next_frontier = []
        for state, record, history in frontier:
            output, postcoin = arena.step(state, record)
            for cell, amplitude in enumerate(postcoin):
                if amplitude.norm2() == 0:
                    continue
                new_history = history + (cell,)
                changed = list(record)
                changed[cell] += record_increment
                new_record = tuple(changed)
                expected = tuple(
                    record0[index] + record_increment * core.histogram(new_history, arena.dimension)[index]
                    for index in range(arena.dimension)
                )
                violations += int(new_record != expected)
                next_frontier.append((output, new_record, new_history))
        frontier = next_frontier
    return {"histories": len(frontier), "violations": violations}


def translated_vector(arena: WalkArena, state: Vector, translation: tuple[int, int]) -> Vector:
    return core.matvec(core.permutation(arena.translation_images(translation)), state)


def translation_census(arena: WalkArena, source: Mapping[str, Any], controls: Mapping[str, Any]) -> dict[str, Any]:
    record_values = [int(source["initial_record_entry"]) for _ in range(arena.dimension)]
    initial_site = arena.site_index[tuple(source["initial_site"])]
    initial_cell = arena.cell(initial_site, int(source["initial_coin"]))
    record_values[initial_cell] += 1
    record = tuple(record_values)
    state = initial_state(arena, source)
    base_output, base_postcoin = arena.step(state, record)
    rows = []
    for item in controls["translation_vectors"]:
        translation = tuple(int(value) for value in item)
        moved_state = translated_vector(arena, state, translation)
        moved_record = (
            arena.translate_record(record, translation)
            if controls.get("translate_record", True)
            else record
        )
        moved_output, moved_postcoin = arena.step(moved_state, moved_record)
        expected_output = translated_vector(arena, base_output, translation)
        permutation = arena.translation_images(translation)
        expected_probabilities = [Q(0) for _ in range(arena.dimension)]
        for source_cell, target_cell in enumerate(permutation):
            expected_probabilities[target_cell] = base_postcoin[source_cell].norm2()
        rows.append(
            {
                "translation": translation,
                "nontrivial": translation != (0, 0),
                "record_moved": moved_record != record,
                "state_equal": moved_output == expected_output,
                "probability_equal": [entry.norm2() for entry in moved_postcoin] == expected_probabilities,
            }
        )
    absolute_site = tuple(int(value) for value in controls["absolute_anchor_site"])
    absolute_index = arena.cell(arena.site_index[absolute_site], int(source["initial_coin"]))
    anchor_retained = any(translated_vector(arena, state, row["translation"])[absolute_index] == core.ONE for row in rows)
    return {
        "rows": rows,
        "absolute_anchor_retained": anchor_retained,
        "record_nonuniform": len(set(record)) > 1,
    }


def instrument_census(arena: WalkArena, source: Mapping[str, Any], controls: Mapping[str, Any]) -> dict[str, Any]:
    record = tuple(int(source["initial_record_entry"]) for _ in range(arena.dimension))
    coin = arena.coin_matrix(record)
    shift = arena.shift_matrix()
    unitary = core.matmul(shift, coin)
    first, second = (int(value) for value in controls["affinity_postcoin_cells"])
    basis_first = tuple(core.ONE if index == first else core.ZERO for index in range(arena.dimension))
    basis_second = tuple(core.ONE if index == second else core.ZERO for index in range(arena.dimension))
    input_first = core.matvec(core.adjoint(coin), basis_first)
    input_second = core.matvec(core.adjoint(coin), basis_second)
    rho_first = core.density(input_first)
    rho_second = core.density(input_second)
    mixture = core.affine_combination(Q(1, 2), rho_first, rho_second)
    effect_first = core.conjugate_by(core.adjoint(coin), core.matrix_unit(arena.dimension, first, first))

    literal_direct = core.nonlinear_nondemolition_outcome(effect_first, unitary, mixture)
    literal_affine = core.affine_combination(
        Q(1, 2),
        core.nonlinear_nondemolition_outcome(effect_first, unitary, rho_first),
        core.nonlinear_nondemolition_outcome(effect_first, unitary, rho_second),
    )
    affinity_delta = core.matsub(literal_direct, literal_affine)

    effect_diagonal = effect_first[0][0]
    effect_scalar = all(
        effect_first[row][column] == (effect_diagonal if row == column else core.ZERO)
        for row in range(arena.dimension)
        for column in range(arena.dimension)
    )
    all_input_nonaffine = core.is_unitary(unitary) and not effect_scalar

    full_effect_total = core.zero(arena.dimension, arena.dimension)
    for cell in range(arena.dimension):
        projector = core.matrix_unit(arena.dimension, cell, cell)
        effect = core.conjugate_by(core.adjoint(coin), projector)
        full_effect_total = core.matadd(full_effect_total, effect)
    source_probability_complete = full_effect_total == core.identity(arena.dimension)

    ports = []
    for cell in range(arena.dimension):
        if controls.get("drop_cp_port") and cell == arena.dimension - 1:
            continue
        projector = core.matrix_unit(arena.dimension, cell, cell)
        ports.append(core.matmul(core.matmul(shift, projector), coin))
    cp_total = core.instrument_total(ports)
    cp_complete = cp_total == core.identity(arena.dimension)

    continuation_first, continuation_second = (
        int(value) for value in controls["continuation_postcoin_cells"]
    )
    coefficients = [parse_fraction(value) for value in controls["continuation_postcoin_vector"]]
    postcoin_state = tuple(
        EW(coefficients[0])
        if index == continuation_first
        else EW(coefficients[1])
        if index == continuation_second
        else core.ZERO
        for index in range(arena.dimension)
    )
    if core.norm2(postcoin_state) != 1:
        raise GateFail("CONTINUATION-PREPARATION-NORM")
    input_state = core.matvec(core.adjoint(coin), postcoin_state)
    source_output, source_postcoin = arena.step(input_state, record)
    outcome = int(controls["continuation_outcome_cell"])
    source_probability = source_postcoin[outcome].norm2()
    repair_vector = tuple(core.ONE if index == outcome else core.ZERO for index in range(arena.dimension))
    standard_repair_output = arena.shift_apply(repair_vector)
    repair_output = standard_repair_output
    literal_mode = controls.get("literal_branch_mode", source["conditioned_state_rule"])
    if literal_mode == "COLLAPSE":
        literal_output = repair_output
    else:
        literal_output = source_output
    if controls.get("cp_branch_mode") == "NONCOLLAPSE":
        repair_output = source_output

    continuation_witness_quality = (
        continuation_first != continuation_second
        and all(value != 0 for value in coefficients)
        and core.norm2(postcoin_state) == 1
        and Q(0) < source_probability < Q(1)
    )

    changed = list(record)
    changed[outcome] += int(controls.get("record_increment", 1))
    next_record = tuple(changed)
    next_source = arena.coin_apply(source_output, next_record)
    next_repair = arena.coin_apply(repair_output, next_record)
    source_screen = [entry.norm2() for entry in next_source]
    repair_screen = [entry.norm2() for entry in next_repair]
    moved_cells = [index for index in range(arena.dimension) if source_screen[index] != repair_screen[index]]

    ontic_match = literal_output == source_output and source_probability == postcoin_state[outcome].norm2()
    cp_probability = core.trace(core.kraus_operation(ports[outcome], core.density(input_state))) if outcome < len(ports) else core.ZERO
    cp_probability_real = cp_probability.a if cp_probability.b == 0 else Q(-1)
    return {
        "coin_matrix": coin,
        "shift_matrix": shift,
        "unitary": unitary,
        "effect": effect_first,
        "effect_nontrivial": effect_first != core.zero(arena.dimension, arena.dimension) and effect_first != core.identity(arena.dimension),
        "effect_scalar": effect_scalar,
        "all_input_nonaffine": all_input_nonaffine,
        "source_probability_complete": source_probability_complete,
        "affinity_delta": affinity_delta,
        "affine": affinity_delta == core.zero(arena.dimension, arena.dimension),
        "cp_total": cp_total,
        "cp_complete": cp_complete,
        "source_probability": source_probability,
        "cp_probability": cp_probability_real,
        "literal_output": literal_output,
        "source_output": source_output,
        "repair_output": repair_output,
        "standard_repair_output": standard_repair_output,
        "cp_implementation": repair_output == standard_repair_output,
        "continuation_witness_quality": continuation_witness_quality,
        "ontic_match": ontic_match,
        "next_source_screen": source_screen,
        "next_repair_screen": repair_screen,
        "moved_cells": moved_cells,
        "beable_label_equal": outcome == int(controls["continuation_outcome_cell"]),
        "beable_record": next_record,
    }


def support_census(arena: WalkArena, record: Sequence[int]) -> dict[str, Any]:
    coin = arena.coin_matrix(record)
    unitary = core.matmul(arena.shift_matrix(), coin)
    support = []
    allowed = []
    shift = arena.shift_images()
    for row in range(arena.dimension):
        for column in range(arena.dimension):
            if unitary[row][column] == core.ZERO:
                continue
            support.append((row, column))
            source_site, source_link = divmod(column, arena.link_count)
            for output_link in range(arena.link_count):
                if row == shift[arena.cell(source_site, output_link)]:
                    allowed.append((row, column))
                    break
    return {
        "support_size": len(support),
        "allowed_size": len(allowed),
        "support_equal": set(support) == set(allowed),
        "dimension": arena.dimension,
    }


def hidden_coin_census(arena: WalkArena, source: Mapping[str, Any], controls: Mapping[str, Any], grover_ipr: Q) -> dict[str, Any]:
    hidden = parse_matrix(controls["hidden_coin_numerators"], controls["hidden_coin_denominator"])
    hidden_source = dict(source)
    hidden_source["horizon"] = int(source["recurrence_horizon"])
    hidden_result = run_walk(arena, hidden_source, coin=hidden)
    grover_source = dict(source)
    grover_source["horizon"] = int(source["recurrence_horizon"])
    grover_result = run_walk(arena, grover_source)
    return {
        "hidden_unitary": core.is_unitary(hidden),
        "hidden_distinct": hidden != arena.coin,
        "hidden_ipr": hidden_result["ipr"],
        "grover_short_ipr": grover_result["ipr"],
        "moves": hidden_result["ipr"] != grover_result["ipr"],
        "full_grover_ipr": grover_ipr,
    }


def derive_primary_code(coordinates: Mapping[str, bool]) -> int:
    if not coordinates["referent"]:
        return 5
    base = coordinates["transport"] and coordinates["cuts"] and coordinates["observables"]
    if not base:
        return 4
    if coordinates["instrument"] and coordinates["beable"]:
        return 0
    if not coordinates["instrument"] and coordinates["beable"]:
        return 1
    if coordinates["instrument"] and not coordinates["beable"]:
        return 2
    if not coordinates["instrument"] and not coordinates["beable"]:
        return 3
    return 6


def render_transcript(results: Mapping[str, Any], gates: Sequence[Mapping[str, Any]]) -> str:
    source = results["source_regression"]
    instrument = results["instrument"]
    recurrence = results["recurrence"]
    lines = [
        "WRC PAPER 8 — FULL PACKET RECONSTRUCTION",
        f"primary={results['verdict']['primary']}",
        f"coordinates={json.dumps(results['verdict']['coordinates'], sort_keys=True, separators=(',', ':'))}",
        f"gates={len(gates) + 3} passed={sum(1 for row in gates if row['ok']) + 3}",
        f"branch_ladder={','.join(str(item) for item in source['branch_counts'])}",
        f"exit_probability={source['exit_probability']}",
        f"ipr={source['ipr']}",
        f"affinity_delta_nonzero={instrument['affinity_delta_nonzero']}",
        f"cp_complete={instrument['cp_complete']}",
        f"continuation_moved_cells={instrument['continuation_moved_cells']}",
        f"recurring_signatures={recurrence['repeated_signature_count']}",
        f"hidden_coin_ipr={recurrence['hidden_coin_ipr']}",
        f"qualifiers={'|'.join(results['verdict']['qualifiers'])}",
        "scope=committed finite fixed-carrier arena; empirical packet equivalence only",
    ]
    return "\n".join(lines) + "\n"


def render_paper(results: Mapping[str, Any], claims: Sequence[str]) -> str:
    source = results["source_regression"]
    instrument = results["instrument"]
    recurrence = results["recurrence"]
    packet = results["packet"]
    targets = results["targets"]
    verdict = results["verdict"]
    scope = results["scope"]
    claims_block = "\n".join(f"- {claim}" for claim in claims)
    qualifier_block = "\n".join(f"- `{item}`" for item in verdict["qualifiers"])
    wall_block = "\n".join(f"- `{item}`" for item in scope["walls"])
    transport_summary = (
        "admits an exact creation-layer representation at the transport grain"
        if verdict["coordinates"]["transport"]
        else "does not admit the registered creation-layer transport representation"
    )
    instrument_summary = (
        "is affine on the all-input density-operator domain"
        if verdict["coordinates"]["instrument"]
        else "is nonaffine on the all-input density-operator domain"
    )
    repair_summary = (
        "changes the registered conditioned continuation"
        if instrument["continuation_moved_cells"] > 0
        else "does not change the registered conditioned continuation"
    )
    covariance_summary = "passes" if packet["translation_covariant"] else "fails"
    beable_summary = (
        "reconstructs"
        if verdict["coordinates"]["beable"]
        else "does not reconstruct"
    )
    fiber_summary = (
        "changes"
        if recurrence["hidden_coin_moves"]
        else "does not change"
    )
    return f"""# Walk reconstruction at full packet grain

Status: **GREEN-UNREVIEWED CANDIDATE**.

Primary result:

```text
{verdict['primary']}
```

## Abstract

The committed finite walk {transport_summary}. Full packet equivalence is
stricter. Its delivered Born-selected CELL-HIT operation
{instrument_summary}. The independently constructed affine CP comparison
preserves the registered CELL-HIT probability and {repair_summary}. The
primary word above is derived from the full coordinate table; no outcome is a
derivation or selection of the walk as fundamental dynamics.

The three target packets remain separate:

| target | exact finite result |
|---|---|
| `TRANSPORT` | match = `{targets['TRANSPORT']['match']}` |
| `AFFINE-CP` | source match = `{targets['AFFINE-CP']['match']}`; comparison instrument complete = `{targets['AFFINE-CP']['comparison_complete']}` |
| `ONTIC-PURE-STATE` | exact recoding = `{targets['ONTIC-PURE-STATE']['exact_recoding']}`; inside affine class = `{targets['ONTIC-PURE-STATE']['inside_affine_class']}` |

## 1. The packet being compared

The source carrier has {packet['sites']} sites, {packet['links']} local link
labels, and {packet['dimension']} one-excitation cells. The three declared cuts
are `{packet['cuts'][0]}`, `{packet['cuts'][1]}`, and `{packet['cuts'][2]}`.
The clock is the declared integer walk step, not proper time or an established
physical division boundary.

At record `n`, the post-coin state is `C_n rho C_n^dagger`; the fixed-carrier
output is `U_n rho U_n^dagger` with `U_n=S C_n`. CELL-HIT `c` has probability
`Tr(E_c rho)`. Its record consequence is `n -> n+e_c`.

## 2. Exact finite regression

The independently reconstructed Born branch ladder is
`{', '.join(str(item) for item in source['branch_counts'])}` and every level
has total mass one. At the declared horizon the inverse participation is
`{source['ipr']}`, the record maximum is `{source['max_cell']}`, and the
admissibility-exit probability is `{source['exit_probability']}`. These values
match the committed packet at the registered paths.

The transport support has {packet['support_size']} nonzero entries and equals
the coin-then-shift kinematic support. This is a fixed {packet['dimension']}
dimensional carrier. No graph growth or changing spatial factorization was
constructed.

## 3. Clock, cuts, covariance, and beables

Reading CELL-HIT weights at the post-coin cut rather than after the shift
moves {packet['cut_moved_cells']} labelled probabilities. Translating the
state and a nonuniform count record together {covariance_summary}
{packet['translation_rows']} exact covariance rows; keeping an absolute
preparation anchor is the negative control.

The count-field beable dictionary {beable_summary} on the short exhaustive
history census: {packet['beable_histories']} labelled histories have
{packet['beable_violations']} history-to-histogram violations. This assay does
not identify CELL-HIT with a three-actor grammar event.

## 4. The instrument comparison

For the literal non-collapse outcome operation

```text
N_c(rho) = Tr(E_c rho) U_n rho U_n^dagger,
```

the exact mixture test has {instrument['affinity_nonzero_entries']} nonzero
defect entries. The independent scalar-effect criterion reports all-input
nonaffinity as `{instrument['all_input_nonaffine']}`; the witness and theorem
agree.

The all-input step is not inferred from one mixture. For an invertible unitary
`U`, affinity of `rho -> Tr(E rho) U rho U^dagger` on the trace-one state space
requires `Tr(E rho)` to be constant, hence `E` to be scalar. Conversely a
scalar `E` makes the map linear there. The reconstructed CELL-HIT effect is
non-scalar, so the obstruction holds over the full registered state space.

The comparison instrument

```text
J_c(rho) = S P_c C_n rho C_n^dagger P_c S^dagger
```

is all-input complete and gives the same registered outcome probability
`{instrument['source_probability']}`. At the next record-dependent coin,
{instrument['continuation_moved_cells']} of the {packet['dimension']} CELL-HIT
probabilities differ; the first registered comparison is
`{instrument['continuation_first_source']}` versus
`{instrument['continuation_first_repair']}`.

Treating the pure state itself as an ontic variable reproduces the nonlinear
rule exactly at the registered witness. That is an extension of the ontology
and law class, not an affine-instrument reconstruction.

## 5. Couplings and recurrence

The extracted local coin entries are {', '.join(recurrence['coin_entries'])};
the phase rule has {recurrence['phase_count']} exact values. The recurrence
census finds {recurrence['repeated_signature_count']} local record signatures
appearing at more than one distinct token. Equal signatures carry equal local
operators by the reconstructed rule.

This does not select the coupling. A second distinct admitted unitary coin
preserves the architecture and {fiber_summary} the short-horizon inverse
participation from
`{recurrence['grover_short_ipr']}` to `{recurrence['hidden_coin_ipr']}`.
Accordingly the walk contributes measured coupling values to later work; it
does not derive a universal constant. State-dependent Born probabilities are
not vertex constants.

## 6. Measured claims

{claims_block}

## 7. Qualifiers

{qualifier_block}

## 8. Scope

{wall_block}

Question Q8 is retired at this committed finite-arena scope. The result does
not establish carrier growth, gravity, continuum or Lorentz structure, QFT or
GR, particles or species, Hamiltonian reconstruction, constants, steering,
actualization, or empirical deviations.

In particular, a successful finite reconstruction does not show that geometry
is irreducible. Any such claim requires a separately frozen uniform law over a
family of relational carriers, held-out members, and a declared class of
geometry-blind adversaries. WRC constructs none of those and does not relabel
record dependence on its fixed carrier as dynamical geometry.
"""


def paper_number_tokens(text: str) -> set[str]:
    return set(re.findall(r"(?<![A-Za-z_])\d+(?:/\d+)?(?![A-Za-z_])", text))


def atomic_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def score(fixture_path: Path, mutant: str | None = None) -> tuple[bytes, bytes, bytes]:
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    apply_mutant(fixture, mutant)
    gates: list[dict[str, Any]] = []
    root = root_path()

    forbidden_keys = {"expected", "target", "primary", "verdict", "outcome", "pass_count", "solution"}
    fixture_keys = key_census(fixture)
    gate(
        gates,
        "WRC-FIXTURE-NEUTRAL",
        "the physical fixture is exact data and contains no answer-bearing key",
        not contains_float(fixture) and not (fixture_keys & forbidden_keys),
        {"float": contains_float(fixture), "forbidden": sorted(fixture_keys & forbidden_keys)},
    )

    anchor_rows = []
    for anchor in fixture["anchors"]:
        path = root / anchor["path"]
        payload = path.read_bytes()
        text = payload.decode("utf-8")
        missing = [token for token in anchor.get("tokens", []) if token not in text]
        anchor_rows.append(
            {
                "path": anchor["path"],
                "sha256": sha256_bytes(payload),
                "hash_ok": sha256_bytes(payload) == anchor["sha256"],
                "missing_tokens": missing,
            }
        )
    gate(
        gates,
        "WRC-ANCHORS",
        "every runtime antecedent is byte- and token-bound",
        all(row["hash_ok"] and not row["missing_tokens"] for row in anchor_rows),
        {"rows": anchor_rows},
    )

    committed_receipt = json.loads((root / "v14/code/coupling_receipt.json").read_text(encoding="utf-8"))
    binding_rows = []
    for binding in fixture["committed_receipt_bindings"]:
        observed = jpath(committed_receipt, binding["pointer"])
        binding_rows.append(
            {"pointer": binding["pointer"], "observed": observed, "bound": binding["committed_value"], "ok": observed == binding["committed_value"]}
        )
    gate(
        gates,
        "WRC-PATH-VALUES",
        "all inherited walk values are bound at their committed receipt paths",
        all(row["ok"] for row in binding_rows),
        {"rows": binding_rows},
    )

    source = fixture["source_packet"]
    controls = fixture["controls"]
    arena = WalkArena(source)
    pairs = [arena.cell_pair(cell) for cell in range(arena.dimension)]
    referent_ok = (
        arena.order == 3
        and len(arena.sites) == 9
        and arena.link_count == 3
        and arena.dimension == 27
        and len(set(pairs)) == arena.dimension
        and all(len(pair) == 2 for pair in pairs)
    )
    gate(
        gates,
        "WRC-PACKET-REFERENT",
        "the walk carrier is the 27 distinct co-division-pair catalogue, not nine actors",
        referent_ok,
        {"sites": len(arena.sites), "links": arena.link_count, "dimension": arena.dimension, "distinct_pairs": len(set(pairs))},
    )
    source_declarations_ok = (
        source["coin_order"] == "GD"
        and source["shift_orientation"] == "PLUS"
        and source["initial_site"] == [0, 0]
        and source["initial_coin"] == 0
        and source["conditioned_state_rule"] == "NONCOLLAPSE"
    )
    gate(
        gates,
        "WRC-SOURCE-DECLARATIONS",
        "the reconstructed packet uses the committed GD, PLUS, origin, and first-link representative",
        source_declarations_ok,
        {
            "coin_order": source["coin_order"],
            "shift_orientation": source["shift_orientation"],
            "initial_site": source["initial_site"],
            "initial_coin": source["initial_coin"],
            "conditioned_state_rule": source["conditioned_state_rule"],
        },
    )
    gate(
        gates,
        "WRC-TERM-BINDING",
        "CELL-HIT remains a one-cell alternative and is not a three-actor division event",
        controls.get("cell_hit_type", "CELL-HIT") == "CELL-HIT" and source["cell_hit_reading"] == "BORN",
        {"type": controls.get("cell_hit_type", "CELL-HIT"), "reading": source["cell_hit_reading"]},
    )

    record0 = tuple(int(source["initial_record_entry"]) for _ in range(arena.dimension))
    coin_matrix = arena.coin_matrix(record0)
    shift_matrix = arena.shift_matrix()
    unitary = core.matmul(shift_matrix, coin_matrix)
    local_unitary = core.is_unitary(arena.coin)
    phase_unitary = all(value.norm2() == 1 for value in arena.phases)
    transport_ok = local_unitary and phase_unitary and core.is_unitary(coin_matrix) and core.is_unitary(shift_matrix) and core.is_unitary(unitary)
    gate(
        gates,
        "WRC-TRANSPORT-UNITARY",
        "coin, record phase, shift, and composed fixed-carrier transport are exact unitaries",
        transport_ok,
        {"local_coin": local_unitary, "phases": phase_unitary, "coin": core.is_unitary(coin_matrix), "shift": core.is_unitary(shift_matrix), "unitary": core.is_unitary(unitary)},
    )

    support = support_census(arena, record0)
    gate(
        gates,
        "WRC-SUPPORT-TYPED",
        "the one-excitation transport support equals the declared coin-then-shift grammar",
        support["support_equal"] and support["dimension"] == arena.dimension,
        support,
    )

    cuts = list(source["cuts"])
    expected_cuts = ["INPUT", "POST-COIN-CELL-HIT", "POST-SHIFT-OUTPUT"]
    clock_ok = cuts == expected_cuts and "GENUINE-DIVISION-BOUNDARY" not in cuts
    gate(
        gates,
        "WRC-CLOCK-CUTS",
        "the declared algorithmic clock and three ordered cuts are reconstructed without promoting a genuine boundary",
        clock_ok,
        {"cuts": cuts},
    )
    state0 = initial_state(arena, source)
    output0, postcoin0 = arena.step(state0, record0)
    postshift_probabilities = [entry.norm2() for entry in output0]
    postcoin_probabilities = [entry.norm2() for entry in postcoin0]
    cut_moved_cells = sum(1 for left, right in zip(postcoin_probabilities, postshift_probabilities) if left != right)
    gate(
        gates,
        "WRC-CUT-DISCRIMINATOR",
        "post-coin CELL-HIT and post-shift labelled probability fields are operationally distinct",
        cut_moved_cells > 0,
        {"moved_cells": cut_moved_cells},
    )

    born_scale = parse_fraction(controls.get("born_scale", "1"))
    record_increment = int(controls.get("record_increment", 1))
    walk = run_walk(arena, source, born_scale=born_scale, record_increment=record_increment)
    branch_anchor = [
        int(row["branches"])
        for row in jpath(committed_receipt, ["ensemble", "arms", "A-COUPLED", "levels"])
    ]
    observable_anchors = {
        row["observable"]: row["coupled"]
        for row in jpath(committed_receipt, ["nontriviality", "observables"])
        if row.get("reading") == "A"
    }
    link_class_marginal = [
        sum(walk["record_increment_field"][site * arena.link_count + link] for site in range(len(arena.sites)))
        for link in range(arena.link_count)
    ]
    observable_matches = {
        "p_site": [qtext(value) for value in walk["site_mass"]] == observable_anchors["p_site"],
        "ipr": qtext(walk["ipr"]) == observable_anchors["ipr"],
        "emission_field": [qtext(value) for value in walk["record_increment_field"]]
        == observable_anchors["emission_field"],
        "link_class_marginal": [qtext(value) for value in link_class_marginal]
        == observable_anchors["link_class_marginal"],
        "admissibility_exit_probability": qtext(walk["exit_probability"])
        == observable_anchors["admissibility_exit_probability"],
        "posdef_distribution": {
            str(key): qtext(value) for key, value in sorted(walk["posdef_distribution"].items())
        }
        == observable_anchors["posdef_distribution"],
        "det_values_reached": {Q(value) for value in observable_anchors["det_values_reached"]}
        == set(walk["determinants"]),
        "max_cell_count": walk["max_cell"] == int(observable_anchors["max_cell_count"]),
        "curvature_constant_probability": qtext(walk["curvature_constant_probability"])
        == observable_anchors["curvature_constant_probability"],
    }
    regression_ok = (
        walk["branch_counts"] == branch_anchor
        and all(item == 1 for item in walk["mass_rows"])
        and len(observable_matches) == 9
        and all(observable_matches.values())
    )
    gate(
        gates,
        "WRC-SOURCE-REGRESSION",
        "the independent finite walk reproduces the committed ladder and held observables exactly",
        regression_ok,
        {
            "branch_counts": walk["branch_counts"],
            "mass": [qtext(item) for item in walk["mass_rows"]],
            "exit": qtext(walk["exit_probability"]),
            "ipr": qtext(walk["ipr"]),
            "max_cell": walk["max_cell"],
            "observable_matches": observable_matches,
        },
    )

    beable = short_beable_census(arena, source, record_increment)
    beable_ok = beable["violations"] == 0 and source["beable_readout"] == "COUNT-FIELD" and record_increment == 1
    gate(
        gates,
        "WRC-BEABLE-MAP",
        "the complete short-history beable assay is typed at the declared count-field readout",
        beable["histories"] > 0 and source["beable_readout"] == "COUNT-FIELD",
        beable,
    )

    translations = translation_census(arena, source, controls)
    translation_assay_ok = (
        translations["record_nonuniform"]
        and all(
            row["nontrivial"]
            and row["record_moved"]
            for row in translations["rows"]
        )
        and not translations["absolute_anchor_retained"]
    )
    translation_ok = translation_assay_ok and all(
        row["state_equal"] and row["probability_equal"]
        for row in translations["rows"]
    )
    gate(
        gates,
        "WRC-TRANSLATION-COVARIANCE",
        "the covariance assay uses nontrivial translations, a moved nonuniform record, and a failing absolute anchor",
        translation_assay_ok,
        {"rows": translations["rows"], "absolute_anchor_retained": translations["absolute_anchor_retained"]},
    )

    gauge_power = int(controls["gauge_phase_power"])
    gauged_state = tuple(arena.phases[gauge_power % arena.order] * entry for entry in state0)
    gauge_output, gauge_postcoin = arena.step(gauged_state, record0)
    gauge_ok = (
        gauge_power % arena.order != 0
        and core.density(gauged_state) == core.density(state0)
        and [entry.norm2() for entry in gauge_output] == [entry.norm2() for entry in output0]
        and [entry.norm2() for entry in gauge_postcoin] == postcoin_probabilities
    )
    gate(
        gates,
        "WRC-GAUGE-SELFTEST",
        "a fresh nontrivial global phase action leaves every registered probability invariant",
        gauge_ok,
        {"power": gauge_power, "state_density_equal": core.density(gauged_state) == core.density(state0)},
    )

    instrument = instrument_census(arena, source, controls)
    affinity_nonzero = instrument["affinity_delta"] != core.zero(arena.dimension, arena.dimension)
    gate(
        gates,
        "WRC-NONAFFINITY",
        "the registered exact mixture witness agrees with the independent all-input scalar-effect criterion",
        instrument["effect_nontrivial"]
        and affinity_nonzero == instrument["all_input_nonaffine"],
        {
            "effect_nontrivial": instrument["effect_nontrivial"],
            "effect_scalar": instrument["effect_scalar"],
            "all_input_nonaffine": instrument["all_input_nonaffine"],
            "witness_nonzero": affinity_nonzero,
            "nonzero_entries": sum(entry != core.ZERO for row in instrument["affinity_delta"] for entry in row),
        },
    )
    gate(
        gates,
        "WRC-CP-COMPLETENESS",
        "the projective comparison ports form an all-input complete affine CP instrument",
        instrument["cp_complete"],
        {"complete": instrument["cp_complete"]},
    )
    probability_equal = instrument["source_probability"] == instrument["cp_probability"]
    continuation_moves = len(instrument["moved_cells"]) > 0
    gate(
        gates,
        "WRC-CP-REPAIR-DISCRIMINATOR",
        "the CP comparison is implemented by its Kraus port and the held-out coherent continuation is nondegenerate",
        probability_equal
        and instrument["cp_implementation"]
        and instrument["continuation_witness_quality"],
        {
            "source_probability": qtext(instrument["source_probability"]),
            "cp_probability": qtext(instrument["cp_probability"]),
            "cp_implementation": instrument["cp_implementation"],
            "witness_quality": instrument["continuation_witness_quality"],
            "moved_cells": instrument["moved_cells"],
        },
    )
    gate(
        gates,
        "WRC-ONTIC-PSI-CONTROL",
        "the literal pure-state successor reproduces the source branch but remains outside the affine class",
        instrument["ontic_match"] and affinity_nonzero,
        {"ontic_match": instrument["ontic_match"], "affine": instrument["affine"]},
    )
    gate(
        gates,
        "WRC-BEABLE-VS-STATE",
        "the same CELL-HIT label and record are compared without presupposing equality of process states",
        instrument["beable_label_equal"],
        {"label_equal": instrument["beable_label_equal"], "state_equal": instrument["source_output"] == instrument["repair_output"]},
    )

    signature_uses_site = bool(controls.get("signature_uses_site_name", False))
    signature_counts: dict[Any, set[Any]] = defaultdict(set)
    for signature, tokens in walk["recurrence_tokens"].items():
        if signature_uses_site:
            for token in tokens:
                signature_counts[(signature, token[2])].add(token)
        else:
            signature_counts[signature].update(tokens)
    repeated_signatures = [key for key, tokens in signature_counts.items() if len({token[2] for token in tokens}) > 1 and len(tokens) > 1]
    gate(
        gates,
        "WRC-RECURRENCE-CENSUS",
        "equal local record signatures recur across distinct site tokens under one reconstructed rule",
        len(repeated_signatures) > 0,
        {"signatures": len(signature_counts), "repeated_across_sites": len(repeated_signatures)},
    )

    hidden = hidden_coin_census(arena, source, controls, walk["ipr"])
    gate(
        gates,
        "WRC-COUPLING-FIBER",
        "the fiber control is a distinct admitted unitary; observable movement is measured rather than required",
        hidden["hidden_unitary"] and hidden["hidden_distinct"],
        {
            "unitary": hidden["hidden_unitary"],
            "distinct": hidden["hidden_distinct"],
            "grover_ipr": qtext(hidden["grover_short_ipr"]),
            "hidden_ipr": qtext(hidden["hidden_ipr"]),
            "moves": hidden["moves"],
        },
    )
    born_rows = [entry.norm2() for entry in postcoin0]
    born_rows.extend(
        parse_fraction(entry) * parse_fraction(entry)
        for entry in controls["continuation_postcoin_vector"]
    )
    nonzero_born = sorted(set(item for item in born_rows if item != 0))
    coupling_entries = sorted(set(core.etext(entry) for row in arena.coin for entry in row))
    coupling_typing_ok = not controls.get("born_weights_are_constants", False) and len(nonzero_born) > 1 and len(coupling_entries) == 2
    gate(
        gates,
        "WRC-COUPLING-TYPING",
        "state-dependent Born weights are distinguished from the two local coin couplings",
        coupling_typing_ok,
        {"coin_entries": coupling_entries, "nonzero_born_values": [qtext(item) for item in nonzero_born]},
    )

    walls = set(fixture["scope_walls"])
    gate(
        gates,
        "WRC-SCOPE-WALLS",
        "all thirteen finite-scope refusals remain explicit",
        walls == REQUIRED_WALLS,
        {"missing": sorted(REQUIRED_WALLS - walls), "extra": sorted(walls - REQUIRED_WALLS)},
    )

    source_regression = {
        "branch_counts": walk["branch_counts"],
        "mass_rows": [qtext(item) for item in walk["mass_rows"]],
        "site_mass": [qtext(item) for item in walk["site_mass"]],
        "emission_field": [qtext(item) for item in walk["record_increment_field"]],
        "link_class_marginal": [qtext(item) for item in link_class_marginal],
        "ipr": qtext(walk["ipr"]),
        "exit_probability": qtext(walk["exit_probability"]),
        "max_cell": walk["max_cell"],
        "determinants": sorted(qtext(item) for item in walk["determinants"]),
        "posdef_distribution": {
            str(key): qtext(value) for key, value in sorted(walk["posdef_distribution"].items())
        },
        "curvature_constant_probability": qtext(walk["curvature_constant_probability"]),
        "observable_matches": observable_matches,
        "observable_match_count": sum(observable_matches.values()),
    }
    first_moved = instrument["moved_cells"][0] if instrument["moved_cells"] else None
    first_source = (
        qtext(instrument["next_source_screen"][first_moved])
        if first_moved is not None
        else "none"
    )
    first_repair = (
        qtext(instrument["next_repair_screen"][first_moved])
        if first_moved is not None
        else "none"
    )
    instrument_result = {
        "effect_nontrivial": instrument["effect_nontrivial"],
        "effect_scalar": instrument["effect_scalar"],
        "all_input_nonaffine": instrument["all_input_nonaffine"],
        "source_probability_complete": instrument["source_probability_complete"],
        "affinity_delta_nonzero": affinity_nonzero,
        "affinity_nonzero_entries": sum(entry != core.ZERO for row in instrument["affinity_delta"] for entry in row),
        "affinity_delta_digest": digest(core.matrix_text(instrument["affinity_delta"])),
        "cp_complete": instrument["cp_complete"],
        "cp_implementation": instrument["cp_implementation"],
        "continuation_witness_quality": instrument["continuation_witness_quality"],
        "source_probability": qtext(instrument["source_probability"]),
        "cp_probability": qtext(instrument["cp_probability"]),
        "conditioned_state_equal": instrument["source_output"] == instrument["repair_output"],
        "continuation_moved_cells": len(instrument["moved_cells"]),
        "continuation_first_cell": first_moved,
        "continuation_first_source": first_source,
        "continuation_first_repair": first_repair,
        "ontic_pure_state_match": instrument["ontic_match"],
        "beable_label_equal": instrument["beable_label_equal"],
    }
    packet_result = {
        "sites": len(arena.sites),
        "links": arena.link_count,
        "dimension": arena.dimension,
        "cuts": cuts,
        "support_size": support["support_size"],
        "cut_moved_cells": cut_moved_cells,
        "translation_rows": len(translations["rows"]),
        "translation_covariant": translation_ok,
        "beable_histories": beable["histories"],
        "beable_violations": beable["violations"],
        "fixed_carrier": True,
        "arena_extension_built": False,
    }
    recurrence_result = {
        "coin_entries": coupling_entries,
        "phase_count": len(arena.phases),
        "signature_count": len(signature_counts),
        "repeated_signature_count": len(repeated_signatures),
        "grover_short_ipr": qtext(hidden["grover_short_ipr"]),
        "hidden_coin_ipr": qtext(hidden["hidden_ipr"]),
        "hidden_coin_moves": hidden["moves"],
        "hidden_coin_distinct": hidden["hidden_distinct"],
        "couplings_selected": False,
        "born_weights_are_constants": False,
    }

    coordinates = {
        "referent": referent_ok,
        "transport": transport_ok and support["support_equal"],
        "cuts": clock_ok and cut_moved_cells > 0,
        "observables": regression_ok and translation_ok,
        "instrument": instrument["source_probability_complete"]
        and not instrument["all_input_nonaffine"],
        "beable": beable_ok and instrument["beable_label_equal"],
    }
    targets = {
        "TRANSPORT": {
            "fixed_carrier_unitary": coordinates["transport"],
            "clock_and_cuts": coordinates["cuts"],
            "registered_observables": coordinates["observables"],
            "match": coordinates["transport"] and coordinates["cuts"] and coordinates["observables"],
        },
        "AFFINE-CP": {
            "source_probability_complete": instrument["source_probability_complete"],
            "source_all_input_affine": not instrument["all_input_nonaffine"],
            "comparison_complete": instrument["cp_complete"],
            "comparison_probability_equal": probability_equal,
            "conditioned_continuation_equal": not continuation_moves,
            "match": coordinates["instrument"],
        },
        "ONTIC-PURE-STATE": {
            "source_branch_exact": instrument["ontic_match"],
            "inside_affine_class": not instrument["all_input_nonaffine"],
            "exact_recoding": instrument["ontic_match"],
        },
    }
    target_table_ok = (
        set(targets) == {"TRANSPORT", "AFFINE-CP", "ONTIC-PURE-STATE"}
        and targets["TRANSPORT"]["match"]
        == (coordinates["transport"] and coordinates["cuts"] and coordinates["observables"])
        and targets["AFFINE-CP"]["match"] == coordinates["instrument"]
        and targets["ONTIC-PURE-STATE"]["exact_recoding"] == instrument["ontic_match"]
    )
    gate(
        gates,
        "WRC-TARGET-TABLE",
        "TRANSPORT, AFFINE-CP, and ONTIC-PURE-STATE are scored as separate target packets",
        target_table_ok,
        {"targets": targets},
    )
    primary_code = derive_primary_code(coordinates)
    word_index = (primary_code + int(controls.get("primary_word_offset", 0))) % len(PRIMARY_WORDS)
    primary = PRIMARY_WORDS[word_index]
    gate(
        gates,
        "WRC-PRIMARY-COMPARATOR",
        "the printed primary index equals an independently recomputed coordinate code",
        PRIMARY_WORDS.index(primary) == derive_primary_code(dict(coordinates)),
        {"printed_index": PRIMARY_WORDS.index(primary), "coordinate_code": derive_primary_code(dict(coordinates)), "coordinates": coordinates},
    )

    qualifiers = []
    qualifier_conditions = {
        "FIXED-CARRIER-TRANSPORT-RECONSTRUCTED": coordinates["transport"],
        "DECLARED-CLOCK-AND-CUTS-RECONSTRUCTED": coordinates["cuts"],
        "REGISTERED-OBSERVABLES-RECONSTRUCTED": coordinates["observables"],
        "TRANSLATION-COVARIANT-WITH-TRANSFORMED-STATE-AND-RECORD": translation_ok,
        "ARENA-EXTENSION-UNBUILT": not packet_result["arena_extension_built"],
        "CELL-HIT-BEABLE-DICTIONARY-RECONSTRUCTED": coordinates["beable"],
        "NONCOLLAPSE-CELL-HIT-MAP-NONAFFINE": instrument["all_input_nonaffine"],
        "AFFINE-CP-REPAIR-MOVES-CONDITIONED-FUTURE": instrument["cp_complete"] and continuation_moves,
        "ONTIC-PSI-EXTENSION-EXACT-BUT-OUTSIDE-AFFINE-CLASS": instrument["ontic_match"]
        and instrument["all_input_nonaffine"],
        "RECURRING-VERTEX-COUPLINGS-EXTRACTED-NOT-SELECTED": len(repeated_signatures) > 0 and hidden["moves"],
        "STATE-DEPENDENT-BORN-WEIGHTS-NOT-CONSTANTS": coupling_typing_ok,
        "WALK-IS-IMPORTED-CANDIDATE-DYNAMICS-NOT-DERIVED-LAW": not recurrence_result["couplings_selected"],
        "Q8-RETIRED-AT-COMMITTED-FINITE-ARENA": bool(controls.get("retire_q8", True)),
    }
    qualifiers = [word for word in QUALIFIER_WORDS if qualifier_conditions[word]]
    gate(
        gates,
        "WRC-QUALIFIERS",
        "every emitted qualifier is derived from its measured predicate and Q8 is retired at finite scope",
        set(qualifiers) == {word for word, ok in qualifier_conditions.items() if ok} and qualifier_conditions["Q8-RETIRED-AT-COMMITTED-FINITE-ARENA"],
        {"qualifiers": qualifiers},
    )

    results: dict[str, Any] = {
        "anchors": {"files": anchor_rows, "path_values": binding_rows},
        "packet": packet_result,
        "source_regression": source_regression,
        "instrument": instrument_result,
        "targets": targets,
        "recurrence": recurrence_result,
        "scope": {"walls": sorted(walls), "q8_retired": qualifier_conditions["Q8-RETIRED-AT-COMMITTED-FINITE-ARENA"]},
        "verdict": {"primary": primary, "coordinates": coordinates, "qualifiers": qualifiers},
    }

    claims = [
        f"The independent Born ladder is {', '.join(str(item) for item in walk['branch_counts'])}.",
        f"The committed exit probability reproduces as {qtext(walk['exit_probability'])}.",
        f"The committed inverse participation reproduces as {qtext(walk['ipr'])}.",
        f"All {source_regression['observable_match_count']} committed observable families reproduce exactly.",
        f"The fixed carrier has {arena.dimension} co-division-pair cells and support size {support['support_size']}.",
        f"The post-coin versus post-shift cut moves {cut_moved_cells} labelled probabilities.",
        f"The exact CELL-HIT affinity witness has {instrument_result['affinity_nonzero_entries']} nonzero defect entries.",
        f"The affine CP comparison differs on {instrument_result['continuation_moved_cells']} next-step probabilities.",
        f"The record map has {beable['violations']} violations over {beable['histories']} short histories.",
        f"The recurrence census has {len(repeated_signatures)} signatures repeated across site tokens.",
        f"The admitted coin fiber maps the short inverse participation from {qtext(hidden['grover_short_ipr'])} to {qtext(hidden['hidden_ipr'])}.",
        f"The full-packet comparator returns {primary} for the committed finite arena.",
        "Question Q8 is retired only at the committed finite fixed-carrier arena.",
    ]
    paper = render_paper(results, claims)
    if controls.get("paper_claim_corruption"):
        paper = paper.replace(claims[0], "CORRUPTED PAPER CLAIM", 1)
    claim_counts = {claim: paper.count(claim) for claim in claims}
    gate(
        gates,
        "WRC-PAPER-CLAIMS",
        "every measured paper claim renders exactly once from the sealed result object",
        all(count == 1 for count in claim_counts.values()),
        {"counts": claim_counts},
    )
    receipt_numeric_surface = canonical_json(results).decode("utf-8") + canonical_json(claims).decode("utf-8")
    missing_numbers = sorted(token for token in paper_number_tokens(paper) if token not in receipt_numeric_surface)
    gate(
        gates,
        "WRC-PAPER-NUMBERS",
        "every numeric paper token is carried by the measured result or claim surface",
        not missing_numbers,
        {"missing": missing_numbers},
    )

    transcript = render_transcript(results, gates) + str(controls.get("transcript_suffix", ""))
    clean_transcript = render_transcript(results, gates)
    gate(
        gates,
        "WRC-TRANSCRIPT-BINDING",
        "the delivered transcript is the deterministic rendering of the measured object",
        transcript == clean_transcript,
        {"observed": sha256_bytes(transcript.encode()), "rebuilt": sha256_bytes(clean_transcript.encode())},
    )

    source_trees = [ast.parse((root / "v16/code/wrc_core.py").read_text()), ast.parse(Path(__file__).read_text())]
    float_nodes = sum(
        1
        for tree in source_trees
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    )
    gate(
        gates,
        "WRC-EXACT-ARITHMETIC",
        "fixture and substantive Python paths contain no runtime float",
        not contains_float(fixture) and float_nodes == 0,
        {"fixture_float": contains_float(fixture), "source_float_literals": float_nodes},
    )
    gate(
        gates,
        "WRC-PREWRITE-READY",
        "all scientific, scope, rendering, and exactness gates pass before sealing",
        all(row["ok"] for row in gates),
        {"gates": len(gates)},
    )

    output_bytes = transcript.encode("utf-8")
    paper_bytes = paper.encode("utf-8")
    seal_manifest = {
        "anchors": digest(results["anchors"]),
        "packet": digest(results["packet"]),
        "source_regression": digest(results["source_regression"]),
        "instrument": digest(results["instrument"]),
        "targets": digest(results["targets"]),
        "recurrence": digest(results["recurrence"]),
        "scope": digest(results["scope"]),
        "verdict": digest(results["verdict"]),
        "gates": digest(gates),
        "claims": digest(claims),
        "transcript": sha256_bytes(output_bytes),
        "paper": sha256_bytes(paper_bytes),
    }
    receipt_results = copy.deepcopy(results)
    if controls.get("prewrite_corruption"):
        receipt_results["packet"]["dimension"] += 1
    seal_ok = (
        digest(receipt_results["anchors"]) == seal_manifest["anchors"]
        and digest(receipt_results["packet"]) == seal_manifest["packet"]
        and digest(receipt_results["source_regression"]) == seal_manifest["source_regression"]
        and digest(receipt_results["instrument"]) == seal_manifest["instrument"]
        and digest(receipt_results["targets"]) == seal_manifest["targets"]
        and digest(receipt_results["recurrence"]) == seal_manifest["recurrence"]
        and digest(receipt_results["scope"]) == seal_manifest["scope"]
        and digest(receipt_results["verdict"]) == seal_manifest["verdict"]
        and digest(gates) == seal_manifest["gates"]
        and digest(claims) == seal_manifest["claims"]
        and sha256_bytes(output_bytes) == seal_manifest["transcript"]
        and sha256_bytes(paper_bytes) == seal_manifest["paper"]
    )
    if not seal_ok:
        raise GateFail("WRC-PREWRITE-SEAL")

    receipt = {
        "schema": "wrc-result-v1",
        "fixture_sha256": sha256_bytes(fixture_path.read_bytes()),
        "core_sha256": sha256_bytes((root / "v16/code/wrc_core.py").read_bytes()),
        "scorer_sha256": sha256_bytes(Path(__file__).read_bytes()),
        "arithmetic": fixture["arithmetic"],
        "results": receipt_results,
        "claims": claims,
        "gates": gates,
        "seal_manifest": seal_manifest,
        "mutants": list(MUTANTS),
        "runtime_reads": [anchor["path"] for anchor in fixture["anchors"]] + [str(fixture_path.relative_to(root))],
    }
    receipt["payload_sha256"] = digest(receipt)
    return output_bytes, canonical_json(receipt), paper_bytes


def default_paths() -> tuple[Path, Path, Path, Path]:
    here = Path(__file__).resolve().parent
    return (
        here / "wrc_fixture.json",
        here / "wrc_output.txt",
        here / "wrc_receipt.json",
        here.parent / "paper-08-walk-reconstruction.md",
    )


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--paper", type=Path)
    parser.add_argument("--mutant", choices=MUTANTS)
    parser.add_argument("--selftest", action="store_true")
    return parser.parse_args(list(argv))


def run_selftest(fixture: Path) -> int:
    try:
        score(fixture, "anchor-hash")
    except GateFail:
        return 0
    return 1


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_args(sys.argv[1:] if argv is None else argv)
    default_fixture, default_output, default_receipt, default_paper = default_paths()
    fixture = (arguments.fixture or default_fixture).resolve()
    if arguments.selftest:
        if any(value is not None for value in (arguments.output, arguments.receipt, arguments.paper, arguments.mutant)):
            raise SystemExit("--selftest cannot be combined with output options or mutants")
        return run_selftest(fixture)

    output = (arguments.output or default_output).resolve()
    receipt = (arguments.receipt or default_receipt).resolve()
    paper = (arguments.paper or default_paper).resolve()
    if len({output, receipt, paper}) != 3:
        raise SystemExit("output, receipt, and paper targets must differ")
    if output.exists() or receipt.exists() or paper.exists():
        raise SystemExit("refusing to overwrite an existing target")

    try:
        output_bytes, receipt_bytes, paper_bytes = score(fixture, arguments.mutant)
    except (GateFail, ValueError, TypeError, KeyError, ArithmeticError) as error:
        print(f"WRC REFUSAL: {error}", file=sys.stderr)
        return 1

    atomic_write(output, output_bytes)
    atomic_write(receipt, receipt_bytes)
    atomic_write(paper, paper_bytes)
    if output.read_bytes() != output_bytes or receipt.read_bytes() != receipt_bytes or paper.read_bytes() != paper_bytes:
        raise GateFail("WRC-DISK-INTEGRITY")
    sys.stdout.buffer.write(output_bytes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
