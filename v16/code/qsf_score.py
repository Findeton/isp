#!/usr/bin/env python3
"""Run the frozen QSF Paper 9 assay and render sealed candidate artifacts.

Only the separately frozen generic QSF core is imported.  The WRC walk,
composite surrogate, history maps, and predictive partitions are rebuilt here
from the result-neutral QSF fixture.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import sys
import tempfile
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Mapping, MutableMapping, Sequence

import qsf_core as core


Q = Fraction
EW = core.EW
ZERO = core.ZERO
ONE = core.ONE
Vector = core.Vector
Matrix = core.Matrix


ARM_A_WORDS = (
    "QSF-AFFINE-NO-COMPLETION-PRESERVES-PACKET-AT-<family>",
    "QSF-AFFINE-COMPLETION-EXISTS-BUT-UNSELECTED-AT-<family>-DIM-<d>",
    "QSF-AFFINE-COMPLETION-UNIQUE-MODULO-OPERATIONAL-NULL-AT-<family>",
    "QSF-AFFINE-COMPLETIONS-EMPIRICALLY-EQUIVALENT-WITHIN-<window>",
    "QSF-AFFINE-METHOD-INCONCLUSIVE-AT-<object>",
)

ARM_B_WORDS = (
    "UNPHRASABLE-BECAUSE-COMPOSITE-DYNAMICS-UNBUILT",
    "PHRASABLE-NO-SIGNALLING-PROVED",
    "PHRASABLE-SIGNALLING-WITNESS",
    "REMOTE-DECOMPOSITIONS-ONLY-EPISTEMIC",
    "COMPOSITE-DYNAMICS-COMPLETE-BUT-STEERING-UNREPRODUCED",
)

ARM_C_WORDS = (
    "QSF-HISTORY-DIVISION-LAWFUL-AT-<k>-<grain>",
    "QSF-HISTORY-AFFINE-ONLY-AFTER-ERASING-RECORD-AT-<k>",
    "QSF-HISTORY-NO-AFFINE-RECORD-BOUNDARY-WITHIN-1-5",
    "QSF-HISTORY-BOUNDARY-UNPHRASABLE",
    "QSF-HISTORY-METHOD-INCONCLUSIVE-AT-<object>",
)

SYNTHESIS_WORDS = (
    "QSF-AFFINE-BASE-VIABLE-SELECTED",
    "QSF-AFFINE-BASE-VIABLE-BUT-UNSELECTED",
    "QSF-ONTIC-BASE-VIABLE-WITH-NO-SIGNALLING-THEOREM",
    "QSF-HISTORY-BASE-VIABLE-AT-GENUINE-BOUNDARY",
    "QSF-MULTIPLE-BASE-LAWS-SURVIVE-SELECTION-OPEN",
    "QSF-WRC-BASE-DYNAMICS-REFUSED",
    "QSF-SEAM-BLOCKED-AT-COMPOSITE-OR-DIVISION-TYPE",
    "QSF-METHOD-INCONCLUSIVE",
)

MUTANTS = (
    "anchor-hash",
    "fixture-answer",
    "coin-entry",
    "shift-orientation",
    "literal-collapse",
    "a0-output",
    "signature-split",
    "hjw-density",
    "alice-setting",
    "ontic-history",
    "affine-control",
    "record-retention",
    "history-window",
    "predictive-merge",
    "s1b-entry",
    "scope-promotion",
    "primary-comparator",
    "exactness",
    "transcript-seal",
    "paper-claim",
    "a0-collision",
    "aggregate-phase",
    "count-readout",
    "alice-outcome-relabel",
    "tick4-screen",
    "density-witness",
    "complete-s1",
    "primary-derivation",
)

REQUIRED_WALLS = {
    "NO-RELATIONAL-COMPOSITE",
    "NO-CARRIER-GROWTH",
    "NO-DYNAMIC-GEOMETRY",
    "NO-GEOMETRY-IRREDUCIBILITY",
    "NO-EVENT-SELECTION-LAW",
    "NO-CARRIER-CATALOGUE-SELECTION",
    "NO-COUPLING-SELECTION",
    "NO-ACTUALIZATION",
    "NO-ABSOLUTE-RECORD-PERMANENCE",
    "NO-CONTINUUM-OR-LORENTZ",
    "NO-QFT-OR-GR",
    "NO-PARTICLES-OR-SPECIES",
    "NO-HAMILTONIAN-SELECTION",
    "NO-EMPIRICAL-DEVIATION",
}


class GateFail(RuntimeError):
    """A QSF gate failed before artifact write."""


def root_path() -> Path:
    return Path(__file__).resolve().parents[2]


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(value: Any) -> str:
    return sha256_bytes(canonical_json(value))


def qtext(value: Q) -> str:
    return core.qtext(Q(value))


def gate(rows: list[dict[str, Any]], name: str, statement: str, ok: bool, evidence: Mapping[str, Any]) -> None:
    row = {"gate": name, "statement": statement, "ok": bool(ok), "evidence": dict(evidence)}
    rows.append(row)
    if not ok:
        raise GateFail(f"{name}: {json.dumps(row['evidence'], sort_keys=True)}")


def contains_float(value: Any) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, Mapping):
        return any(contains_float(key) or contains_float(item) for key, item in value.items())
    if isinstance(value, (list, tuple)):
        return any(contains_float(item) for item in value)
    return False


def key_census(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, Mapping):
        for key, item in value.items():
            found.add(str(key).lower())
            found.update(key_census(item))
    elif isinstance(value, (list, tuple)):
        for item in value:
            found.update(key_census(item))
    return found


def parse_ew(value: Any) -> EW:
    if isinstance(value, int):
        return EW(value)
    if isinstance(value, str):
        return EW(Q(value))
    if isinstance(value, list) and len(value) == 2:
        return EW(Q(value[0]), Q(value[1]))
    raise TypeError(f"invalid exact scalar {value!r}")


def parse_matrix(rows: Sequence[Sequence[Any]], denominator: Any = 1) -> Matrix:
    divisor = EW(Q(denominator))
    return core.matrix([[parse_ew(entry) / divisor for entry in row] for row in rows])


def matrix_unit(size: int, row: int, column: int) -> Matrix:
    return tuple(
        tuple(ONE if (r, c) == (row, column) else ZERO for c in range(size))
        for r in range(size)
    )


def permutation(images: Sequence[int]) -> Matrix:
    size = len(images)
    if sorted(images) != list(range(size)):
        raise ValueError("images are not a permutation")
    return tuple(
        tuple(ONE if images[column] == row else ZERO for column in range(size))
        for row in range(size)
    )


def vadd(left: tuple[int, int], right: tuple[int, int], order: int) -> tuple[int, int]:
    return ((left[0] + right[0]) % order, (left[1] + right[1]) % order)


def vsub(left: tuple[int, int], right: tuple[int, int], order: int) -> tuple[int, int]:
    return ((left[0] - right[0]) % order, (left[1] - right[1]) % order)


class WalkArena:
    def __init__(self, source: Mapping[str, Any]) -> None:
        self.order = int(source["field_order"])
        self.sites = tuple(tuple(int(v) for v in site) for site in source["sites"])
        self.site_index = {site: index for index, site in enumerate(self.sites)}
        self.links = tuple(tuple(int(v) for v in link) for link in source["links"])
        self.link_count = len(self.links)
        self.dimension = len(self.sites) * self.link_count
        self.phases = tuple(parse_ew(value) for value in source["phase_powers"])
        self.coin = parse_matrix(source["coin_numerators"], source["coin_denominator"])
        self.orientation = str(source["shift_orientation"])

    def cell(self, site: int, link: int) -> int:
        return site * self.link_count + link

    def shift_images(self) -> tuple[int, ...]:
        result = []
        for here in self.sites:
            for link, direction in enumerate(self.links):
                there = vadd(here, direction, self.order) if self.orientation == "PLUS" else vsub(here, direction, self.order)
                result.append(self.cell(self.site_index[there], link))
        return tuple(result)

    def shift_matrix(self) -> Matrix:
        return permutation(self.shift_images())

    def coin_matrix(self, record: Sequence[int]) -> Matrix:
        rows = [[ZERO for _ in range(self.dimension)] for _ in range(self.dimension)]
        for site in range(len(self.sites)):
            base = site * self.link_count
            for row in range(self.link_count):
                for column in range(self.link_count):
                    rows[base + row][base + column] = self.coin[row][column] * self.phases[record[base + column] % self.order]
        return tuple(tuple(row) for row in rows)

    def coin_apply(self, state: Sequence[Any], record: Sequence[int]) -> tuple[Any, ...]:
        result: list[Any] = [ZERO for _ in range(self.dimension)]
        for site in range(len(self.sites)):
            base = site * self.link_count
            phased = [
                state[base + link] * self.phases[record[base + link] % self.order]
                for link in range(self.link_count)
            ]
            for row in range(self.link_count):
                result[base + row] = sum(
                    (self.coin[row][column] * phased[column] for column in range(self.link_count)),
                    ZERO,
                )
        return tuple(result)

    def shift_apply(self, state: Sequence[Any]) -> tuple[Any, ...]:
        result = [ZERO for _ in range(self.dimension)]
        for source, target in enumerate(self.shift_images()):
            result[target] = state[source]
        return tuple(result)

    def step(self, state: Sequence[Any], record: Sequence[int]) -> tuple[tuple[Any, ...], tuple[Any, ...]]:
        postcoin = self.coin_apply(state, record)
        return self.shift_apply(postcoin), postcoin


def initial_state(arena: WalkArena, source: Mapping[str, Any]) -> Vector:
    values = [ZERO for _ in range(arena.dimension)]
    site = arena.site_index[tuple(source["initial_site"])]
    values[arena.cell(site, int(source["initial_coin"]))] = ONE
    return tuple(values)


def ew_ray_key(state: Vector) -> tuple[str, ...]:
    first = next((entry for entry in state if entry != ZERO), None)
    if first is None:
        raise ValueError("zero ray")
    inverse = first.inverse()
    return tuple(core.etext(entry * inverse) for entry in state)


def q_form(counts: Sequence[int]) -> tuple[Q, Q, Q, Q]:
    first, second, diagonal = (Q(item) for item in counts)
    off = (diagonal - first - second) / 2
    return first, second, off, first * second - off * off


def record_stats(arena: WalkArena, record: Sequence[int], initial_entry: int) -> dict[str, Any]:
    determinants: set[Q] = set()
    positive = 0
    curvature = []
    for site, here in enumerate(arena.sites):
        counts = record[site * arena.link_count : (site + 1) * arena.link_count]
        first, _second, _off, determinant = q_form(counts)
        determinants.add(determinant)
        positive += int(first > 0 and determinant > 0)
        second_site = arena.site_index[vadd(here, arena.links[0], arena.order)]
        curvature.append((record[arena.cell(site, 0)] + record[arena.cell(second_site, 1)] - record[arena.cell(site, 2)]) % arena.order)
    return {
        "positive_sites": positive,
        "determinants": determinants,
        "max_cell": max(record),
        "curvature_constant": len(set(curvature)) == 1,
        "increments": tuple(int(value) - initial_entry for value in record),
    }


def run_walk(arena: WalkArena, source: Mapping[str, Any], mode: str) -> dict[str, Any]:
    horizon = int(source["horizon"])
    initial_entry = int(source["initial_record_entry"])
    record0 = tuple(initial_entry for _ in range(arena.dimension))
    frontier: list[tuple[Vector, tuple[int, ...], Q]] = [(initial_state(arena, source), record0, Q(1))]
    branch_counts: list[int] = []
    masses: list[Q] = []
    site_mass = [Q(0) for _ in arena.sites]
    exit_probability = Q(0)
    posdef: dict[int, Q] = defaultdict(Q)
    determinants: set[Q] = set()
    max_cell = 0
    curvature_probability = Q(0)
    emission = [Q(0) for _ in range(arena.dimension)]

    for tick in range(horizon):
        last = tick + 1 == horizon
        next_frontier: list[tuple[Vector, tuple[int, ...], Q]] = []
        level_mass = Q(0)
        level_count = 0
        for state, record, history_weight in frontier:
            literal_output, postcoin = arena.step(state, record)
            probabilities = [entry.norm2() for entry in postcoin]
            if sum(probabilities) != 1:
                raise GateFail("QSF-WALK-NORMALIZATION")
            for cell, probability in enumerate(probabilities):
                if probability == 0:
                    continue
                weight = history_weight * probability
                changed = list(record)
                changed[cell] += 1
                new_record = tuple(changed)
                output = literal_output
                if mode == "PROJECTIVE":
                    basis = tuple(ONE if index == cell else ZERO for index in range(arena.dimension))
                    output = arena.shift_apply(basis)  # type: ignore[assignment]
                level_count += 1
                level_mass += weight
                if not last:
                    next_frontier.append((output, new_record, weight))
                    continue
                for site in range(len(arena.sites)):
                    value = sum(output[arena.cell(site, link)].norm2() for link in range(arena.link_count))
                    site_mass[site] += weight * value
                stats = record_stats(arena, new_record, initial_entry)
                posdef[stats["positive_sites"]] += weight
                if stats["positive_sites"] < len(arena.sites):
                    exit_probability += weight
                determinants.update(stats["determinants"])
                max_cell = max(max_cell, stats["max_cell"])
                if stats["curvature_constant"]:
                    curvature_probability += weight
                for index, increment in enumerate(stats["increments"]):
                    emission[index] += weight * increment
        branch_counts.append(level_count)
        masses.append(level_mass)
        frontier = next_frontier

    link_marginal = [sum(emission[site * arena.link_count + link] for site in range(len(arena.sites))) for link in range(arena.link_count)]
    return {
        "branch_counts": branch_counts,
        "mass_rows": masses,
        "site_mass": site_mass,
        "ipr": sum(value * value for value in site_mass),
        "exit_probability": exit_probability,
        "posdef_distribution": dict(posdef),
        "determinants": determinants,
        "max_cell": max_cell,
        "curvature_constant_probability": curvature_probability,
        "emission_field": emission,
        "link_class_marginal": link_marginal,
    }


def source_match(observed: Mapping[str, Any], committed: Mapping[str, Any]) -> dict[str, bool]:
    conversions = {
        "admissibility_exit_probability": qtext(observed["exit_probability"]) == committed["exit_probability"],
        "curvature_constant_probability": qtext(observed["curvature_constant_probability"]) == committed["curvature_constant_probability"],
        "det_values_reached": sorted(qtext(value) for value in observed["determinants"]) == sorted(committed["determinants"]),
        "emission_field": [qtext(value) for value in observed["emission_field"]] == committed["emission_field"],
        "ipr": qtext(observed["ipr"]) == committed["ipr"],
        "link_class_marginal": [qtext(value) for value in observed["link_class_marginal"]] == committed["link_class_marginal"],
        "max_cell_count": observed["max_cell"] == committed["max_cell"],
        "p_site": [qtext(value) for value in observed["site_mass"]] == committed["site_mass"],
        "posdef_distribution": {str(key): qtext(value) for key, value in sorted(observed["posdef_distribution"].items())} == committed["posdef_distribution"],
    }
    return conversions


def literal_contexts(arena: WalkArena, source: Mapping[str, Any], depth: int) -> list[tuple[Vector, tuple[int, ...], tuple[int, ...], Q]]:
    record0 = tuple(int(source["initial_record_entry"]) for _ in range(arena.dimension))
    frontier = [(initial_state(arena, source), record0, tuple(), Q(1))]
    for _tick in range(depth):
        next_frontier = []
        for state, record, history, history_weight in frontier:
            output, postcoin = arena.step(state, record)
            for cell, amplitude in enumerate(postcoin):
                probability = amplitude.norm2()
                if probability == 0:
                    continue
                changed = list(record)
                changed[cell] += 1
                next_frontier.append((output, tuple(changed), history + (cell,), history_weight * probability))
        frontier = next_frontier
    return frontier


def a0_record_collision(arena: WalkArena, source: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    """Exhibit two reached histories for which `(record, outcome)` is not a law context."""
    contexts = {context[2]: context for context in literal_contexts(arena, source, 3)}
    histories = ((0, 12, 13), (0, 13, 12))
    left = contexts[histories[0]]
    right = contexts[histories[1]]
    left_output, left_postcoin = arena.step(left[0], left[1])
    right_output, right_postcoin = arena.step(right[0], right[1])
    outcome = 0
    same_record = left[1] == right[1]
    both_live = left_postcoin[outcome].norm2() != 0 and right_postcoin[outcome].norm2() != 0
    left_key = ew_ray_key(tuple(left_output))
    right_key = ew_ray_key(tuple(right_output))
    different = left_key != right_key
    if mutant == "a0-collision":
        different = False
    return {
        "histories": histories,
        "outcome": outcome,
        "same_record": same_record,
        "both_live": both_live,
        "different_output_rays": different,
        "left_coordinate_2": left_key[2],
        "right_coordinate_2": right_key[2],
        "left_branch_weight": qtext(left[3] * left_postcoin[outcome].norm2()),
        "right_branch_weight": qtext(right[3] * right_postcoin[outcome].norm2()),
    }


def translate_state_to_origin(arena: WalkArena, state: Vector, event_site: int) -> Vector:
    origin = arena.sites[event_site]
    translated = [ZERO for _ in range(arena.dimension)]
    for old_site, coordinate in enumerate(arena.sites):
        new_coordinate = vsub(coordinate, origin, arena.order)
        new_site = arena.site_index[new_coordinate]
        for link in range(arena.link_count):
            translated[arena.cell(new_site, link)] = state[arena.cell(old_site, link)]
    return tuple(translated)


def branch_control_census(arena: WalkArena, source: Mapping[str, Any], mutant: str | None) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Compute raw/aligned recurrence and terminal phase controls in one walk."""
    raw_groups: dict[tuple[Any, ...], set[tuple[str, ...]]] = defaultdict(set)
    aligned_groups: dict[tuple[Any, ...], set[tuple[str, ...]]] = defaultdict(set)
    frontier = literal_contexts(arena, source, 0)
    contexts = 0
    alternatives = 0
    terminal_contexts = 0
    terminal_moved = 0
    terminal_basis_equal = True
    phase = EW(0, 1)
    horizon = int(source["horizon"])
    for tick in range(horizon):
        next_frontier = []
        for state, record, history, weight in frontier:
            contexts += 1
            output_raw, postcoin = arena.step(state, record)
            output = tuple(output_raw)
            output_key = ew_ray_key(output)
            aligned_cache: dict[int, tuple[str, ...]] = {}
            if tick + 1 == horizon:
                terminal_contexts += 1
                if mutant == "aggregate-phase":
                    phased = tuple(phase * entry for entry in output)
                else:
                    values = list(output)
                    values[0] = phase * values[0]
                    phased = tuple(values)
                terminal_moved += int(output_key != ew_ray_key(phased))
                terminal_basis_equal = terminal_basis_equal and [entry.norm2() for entry in output] == [entry.norm2() for entry in phased]
            for cell, amplitude in enumerate(postcoin):
                probability = amplitude.norm2()
                if probability == 0:
                    continue
                site, link = divmod(cell, arena.link_count)
                residues = tuple(record[arena.cell(site, local)] % arena.order for local in range(arena.link_count))
                signature: tuple[Any, ...] = (residues, link)
                if mutant == "signature-split":
                    signature = (residues, link, history)
                raw_groups[signature].add(output_key)
                if site not in aligned_cache:
                    aligned_cache[site] = ew_ray_key(translate_state_to_origin(arena, output, site))
                aligned_groups[signature].add(aligned_cache[site])
                alternatives += 1
                changed = list(record)
                changed[cell] += 1
                if tick + 1 < horizon:
                    next_frontier.append((output, tuple(changed), history + (cell,), weight * probability))
        frontier = next_frontier

    def collision_row(groups: Mapping[Any, set[Any]]) -> dict[str, Any]:
        conflicts = {key: len(values) for key, values in groups.items() if len(values) > 1}
        return {
            "contexts": contexts,
            "alternatives": alternatives,
            "signatures": len(groups),
            "conflicting_signatures": len(conflicts),
            "max_rays_per_signature": max(conflicts.values(), default=1),
            "example_digest": digest(sorted((repr(key), count) for key, count in conflicts.items())[:8]),
        }

    phase_row = {
        "contexts": terminal_contexts,
        "moved_rays": terminal_moved,
        "basis_probabilities_equal": terminal_basis_equal,
        "all_nine_terminal_aggregates_equal": terminal_basis_equal,
    }
    return collision_row(raw_groups), collision_row(aligned_groups), phase_row


def third_completion_control(arena: WalkArena, source: Mapping[str, Any]) -> dict[str, Any]:
    record0 = tuple(int(source["initial_record_entry"]) for _ in range(arena.dimension))
    coin = arena.coin_matrix(record0)
    effect_vectors = []
    output_vectors = []
    projective_outputs = []
    for cell in range(arena.dimension):
        basis = tuple(ONE if index == cell else ZERO for index in range(arena.dimension))
        shifted = arena.shift_apply(basis)
        next_basis = tuple(ONE if index == (cell + 1) % arena.dimension else ZERO for index in range(arena.dimension))
        effect_vectors.append(core.matvec(core.adjoint(coin), basis))
        output_vectors.append(arena.shift_apply(next_basis))
        projective_outputs.append(shifted)
    ports = core.rank_one_completion(effect_vectors, output_vectors)
    return {
        "complete": core.instrument_total(ports) == core.identity(arena.dimension),
        "normalized_outputs": all(core.norm2(vector) == 1 for vector in output_vectors),
        "different_from_projective": sum(left != right for left, right in zip(output_vectors, projective_outputs)),
    }


def total_variation(left: Mapping[Any, Q], right: Mapping[Any, Q]) -> Q:
    keys = set(left) | set(right)
    return sum((abs(left.get(key, Q(0)) - right.get(key, Q(0))) for key in keys), Q(0)) / 2


ScaledEnsemble = list[tuple[Q, Vector, Q]]


def hjw_composite_check(e0: Vector, e1: Vector) -> dict[str, Any]:
    """Construct the exact 2 x 27 Bell/HJW surrogate and condition it."""
    bob_dimension = len(e0)
    joint_dimension = 2 * bob_dimension
    joint = [[ZERO for _ in range(joint_dimension)] for _ in range(joint_dimension)]
    bob_vectors = (e0, e1)
    for alice_row in range(2):
        for alice_column in range(2):
            block = core.matscale(Q(1, 2), core.outer(bob_vectors[alice_row], bob_vectors[alice_column]))
            for row in range(bob_dimension):
                for column in range(bob_dimension):
                    joint[alice_row * bob_dimension + row][alice_column * bob_dimension + column] = block[row][column]
    joint_state = tuple(tuple(row) for row in joint)
    p0 = core.matrix([[1, 0], [0, 0]])
    p1 = core.matrix([[0, 0], [0, 1]])
    plus = core.matrix([[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]])
    minus = core.matrix([[Q(1, 2), Q(-1, 2)], [Q(-1, 2), Q(1, 2)]])
    z_rows = [core.alice_conditioned_bob(joint_state, effect, 2, bob_dimension) for effect in (p0, p1)]
    x_rows = [core.alice_conditioned_bob(joint_state, effect, 2, bob_dimension) for effect in (plus, minus)]
    plus_vector = tuple(left + right for left, right in zip(e0, e1))
    minus_vector = tuple(left - right for left, right in zip(e0, e1))
    expected_z = [core.outer(e0), core.outer(e1)]
    expected_x = [core.matscale(Q(1, 2), core.outer(plus_vector)), core.matscale(Q(1, 2), core.outer(minus_vector))]
    bob_marginal = core.partial_trace_a(joint_state, 2, bob_dimension)
    expected_marginal = core.matscale(Q(1, 2), core.matadd(core.outer(e0), core.outer(e1)))
    return {
        "joint_trace": core.trace(joint_state) == ONE,
        "bob_marginal": bob_marginal == expected_marginal,
        "z_conditionals": [row[1] for row in z_rows] == expected_z,
        "x_conditionals": [row[1] for row in x_rows] == expected_x,
        "probabilities": [row[0] for row in z_rows + x_rows],
        "alice_complete": core.matadd(p0, p1) == core.identity(2) and core.matadd(plus, minus) == core.identity(2),
    }


def embedded_ensembles(arena: WalkArena, source: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    record0 = tuple(int(source["initial_record_entry"]) for _ in range(arena.dimension))
    coin = arena.coin_matrix(record0)
    cells = (0, 1)
    basis_vectors = []
    for cell in cells:
        basis = tuple(ONE if index == cell else ZERO for index in range(arena.dimension))
        basis_vectors.append(core.matvec(core.adjoint(coin), basis))
    e0, e1 = basis_vectors
    z: ScaledEnsemble = [(Q(1, 2), e0, Q(1)), (Q(1, 2), e1, Q(1))]
    plus = tuple(left + right for left, right in zip(e0, e1))
    minus = tuple(left - right for left, right in zip(e0, e1))
    x: ScaledEnsemble = [(Q(1, 2), plus, Q(1, 2)), (Q(1, 2), minus, Q(1, 2))]
    if mutant == "hjw-density":
        x[1] = (Q(1, 2), plus, Q(1, 2))
    if mutant == "alice-setting":
        x = list(z)
    if any(scale * core.norm2(state) != 1 for _weight, state, scale in z + x):
        raise GateFail("QSF-HJW-NORM")

    def ensemble_entry(ensemble: ScaledEnsemble, row: int, column: int) -> EW:
        return sum((EW(weight * scale) * state[row] * state[column].conjugate() for weight, state, scale in ensemble), ZERO)

    density_equal = all(
        ensemble_entry(z, row, column) == ensemble_entry(x, row, column)
        for row in range(arena.dimension)
        for column in range(arena.dimension)
    )
    orthogonal = sum((left.conjugate() * right for left, right in zip(e0, e1)), ZERO) == ZERO
    composite = hjw_composite_check(e0, e1)
    return {"z": z, "x": x, "density_equal": density_equal, "orthogonal": orthogonal, "record0": record0, "composite": composite}


def ensemble_process(
    arena: WalkArena,
    ensemble: ScaledEnsemble,
    record0: tuple[int, ...],
    horizon: int,
    mode: str,
    history_mutant: bool = False,
) -> dict[str, Any]:
    frontier: list[tuple[Vector, Q, tuple[int, ...], tuple[int, ...], Q]] = [
        (state, scale, record0, tuple(), weight) for weight, state, scale in ensemble
    ]
    windows = []
    calibrated_probe_cell = arena.shift_images()[0]
    for tick in range(1, horizon + 1):
        next_frontier: list[tuple[Vector, Q, tuple[int, ...], tuple[int, ...], Q]] = []
        history_mass: dict[tuple[int, ...], Q] = defaultdict(Q)
        record_mass: dict[tuple[int, ...], Q] = defaultdict(Q)
        discard_screen = [Q(0) for _ in range(arena.dimension)]
        record_probe: dict[tuple[int, ...], Q] = defaultdict(Q)
        for state, scale, record, history, history_weight in frontier:
            literal_output_raw, postcoin_raw = arena.step(state, record)
            literal_output = tuple(literal_output_raw)  # type: ignore[assignment]
            postcoin = tuple(postcoin_raw)  # type: ignore[assignment]
            probabilities = [scale * entry.norm2() for entry in postcoin]
            if sum(probabilities) != 1:
                raise GateFail("QSF-ENSEMBLE-NORMALIZATION")
            if mode == "LITERAL":
                for index, amplitude in enumerate(literal_output):
                    discard_screen[index] += history_weight * scale * amplitude.norm2()
            for cell, probability in enumerate(probabilities):
                if probability == 0:
                    continue
                changed = list(record)
                changed[cell] += 1
                output = literal_output
                output_scale = scale
                if mode in {"PROJECTIVE", "CYCLIC"}:
                    prepared_cell = cell if mode == "PROJECTIVE" else (cell + 1) % arena.dimension
                    basis = tuple(ONE if index == prepared_cell else ZERO for index in range(arena.dimension))
                    output = tuple(arena.shift_apply(basis))  # type: ignore[assignment]
                    output_scale = Q(1)
                new_history = history + ((0 if history_mutant else cell),)
                new_record = tuple(changed)
                weight = history_weight * probability
                history_mass[new_history] += weight
                record_mass[new_record] += weight
                record_probe[new_record] += weight * output_scale * output[calibrated_probe_cell].norm2()
                if mode in {"PROJECTIVE", "CYCLIC"}:
                    for index, amplitude in enumerate(output):
                        discard_screen[index] += weight * output_scale * amplitude.norm2()
                if tick < horizon:
                    next_frontier.append((output, output_scale, new_record, new_history, weight))
        windows.append(
            {
                "tick": tick,
                "contexts": len(frontier),
                "history_mass": dict(history_mass),
                "record_mass": dict(record_mass),
                "discard_screen": tuple(discard_screen),
                "record_probe": dict(record_probe),
            }
        )
        frontier = next_frontier
    return {"windows": windows}


def compare_ensemble_windows(left: Mapping[str, Any], right: Mapping[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for left_window, right_window in zip(left["windows"], right["windows"]):
        history_tv = total_variation(left_window["history_mass"], right_window["history_mass"])
        record_tv = total_variation(left_window["record_mass"], right_window["record_mass"])
        screen_tv = sum((abs(a - b) for a, b in zip(left_window["discard_screen"], right_window["discard_screen"])), Q(0)) / 2
        record_probe_moved = left_window["record_probe"] != right_window["record_probe"]
        rows.append(
            {
                "tick": left_window["tick"],
                "left_contexts": left_window["contexts"],
                "right_contexts": right_window["contexts"],
                "history_tv": history_tv,
                "record_tv": record_tv,
                "discard_screen_tv": screen_tv,
                "record_probe_moved": record_probe_moved,
                "record_boundary_witness": record_tv != 0 or record_probe_moved,
            }
        )
    return rows


def phase_mub_and_affine_controls(
    arena: WalkArena,
    ensembles: Mapping[str, Any],
    mutant: str | None,
) -> dict[str, Any]:
    """A second HJW basis and a non-projective affine history control."""
    e0 = ensembles["z"][0][1]
    e1 = ensembles["z"][1][1]
    omega2 = EW(-1, -1)
    plus = tuple(left + omega2 * right for left, right in zip(e0, e1))
    minus = tuple(left - omega2 * right for left, right in zip(e0, e1))
    phase: ScaledEnsemble = [(Q(1, 2), plus, Q(1, 2)), (Q(1, 2), minus, Q(1, 2))]
    phase_process = ensemble_process(arena, phase, ensembles["record0"], 3, "LITERAL")
    z_process = ensemble_process(arena, ensembles["z"], ensembles["record0"], 3, "LITERAL")
    phase_rows = compare_ensemble_windows(z_process, phase_process)
    relabeled_process = ensemble_process(arena, list(reversed(phase)), ensembles["record0"], 3, "LITERAL")
    relabel_rows = compare_ensemble_windows(phase_process, relabeled_process)
    cyclic_z = ensemble_process(arena, ensembles["z"], ensembles["record0"], 3, "CYCLIC")
    cyclic_x = ensemble_process(arena, ensembles["x"], ensembles["record0"], 3, "CYCLIC")
    cyclic_rows = compare_ensemble_windows(cyclic_z, cyclic_x)
    relabel_invariant = all(row["history_tv"] == 0 and row["record_tv"] == 0 for row in relabel_rows)
    if mutant == "alice-outcome-relabel":
        relabel_invariant = False
    return {
        "phase_history_tv": [row["history_tv"] for row in phase_rows],
        "phase_record_tv": [row["record_tv"] for row in phase_rows],
        "outcome_relabel_invariant": relabel_invariant,
        "cyclic_affine_history_tv": [row["history_tv"] for row in cyclic_rows],
        "cyclic_affine_record_tv": [row["record_tv"] for row in cyclic_rows],
    }


def no_feedback_screen_control(arena: WalkArena, ensembles: Mapping[str, Any], horizon: int) -> list[Q]:
    """Remove both record readout and record-conditioned feedback."""
    screens = []
    for ensemble in (ensembles["z"], ensembles["x"]):
        states = [(weight, tuple(state), scale) for weight, state, scale in ensemble]
        rows = []
        for _ in range(horizon):
            screen = [Q(0) for _ in range(arena.dimension)]
            next_states = []
            for weight, state, scale in states:
                output, _postcoin = arena.step(state, ensembles["record0"])
                output = tuple(output)
                for index, amplitude in enumerate(output):
                    screen[index] += weight * scale * amplitude.norm2()
                next_states.append((weight, output, scale))
            rows.append(tuple(screen))
            states = next_states
        screens.append(rows)
    return [
        sum((abs(left - right) for left, right in zip(z_row, x_row)), Q(0)) / 2
        for z_row, x_row in zip(screens[0], screens[1])
    ]


def discarded_density(arena: WalkArena, source: Mapping[str, Any], ensemble: ScaledEnsemble, horizon: int) -> Matrix:
    record0 = tuple(int(source["initial_record_entry"]) for _ in range(arena.dimension))
    frontier = [(tuple(state), scale, record0, weight) for weight, state, scale in ensemble]
    for _ in range(horizon):
        next_frontier = []
        for state, scale, record, weight in frontier:
            output_raw, postcoin = arena.step(state, record)
            output = tuple(output_raw)
            probabilities = [scale * entry.norm2() for entry in postcoin]
            if sum(probabilities) != 1:
                raise GateFail("QSF-DENSITY-NORMALIZATION")
            for cell, probability in enumerate(probabilities):
                if probability == 0:
                    continue
                changed = list(record)
                changed[cell] += 1
                next_frontier.append((output, scale, tuple(changed), weight * probability))
        frontier = next_frontier
    result = core.zero(arena.dimension, arena.dimension)
    for state, scale, _record, weight in frontier:
        result = core.matadd(result, core.matscale(weight * scale, core.outer(state)))
    return result


def density_affinity_witness(arena: WalkArena, source: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    b0 = core.basis(arena.dimension, 0)
    b3 = core.basis(arena.dimension, 3)
    f0 = tuple(EW(Q(3, 5)) if index == 0 else EW(Q(4, 5)) if index == 3 else ZERO for index in range(arena.dimension))
    f1 = tuple(EW(Q(-4, 5)) if index == 0 else EW(Q(3, 5)) if index == 3 else ZERO for index in range(arena.dimension))
    z: ScaledEnsemble = [(Q(1, 2), b0, Q(1)), (Q(1, 2), b3, Q(1))]
    rotated: ScaledEnsemble = [(Q(1, 2), f0, Q(1)), (Q(1, 2), f1, Q(1))]
    input_equal = core.matscale(Q(1, 2), core.matadd(core.outer(b0), core.outer(b3))) == core.matscale(Q(1, 2), core.matadd(core.outer(f0), core.outer(f1)))
    z2 = discarded_density(arena, source, z, 2)
    f2 = discarded_density(arena, source, rotated, 2)
    difference2 = core.matsub(z2, f2)
    z3 = discarded_density(arena, source, z, 3)
    f3 = discarded_density(arena, source, rotated, 3)
    difference3 = core.matsub(z3, f3)
    offdiagonal = difference2[1][7]
    if mutant == "density-witness":
        offdiagonal = ZERO
    diagonal_blind_tick2 = all(difference2[index][index] == ZERO for index in range(arena.dimension))
    diagonal_tv_tick3 = sum((abs(difference3[index][index].a) for index in range(arena.dimension)), Q(0)) / 2
    return {
        "input_density_equal": input_equal,
        "tick2_different_entries": sum(entry != ZERO for row in difference2 for entry in row),
        "tick2_diagonal_blind": diagonal_blind_tick2,
        "tick2_offdiagonal_1_7": core.etext(offdiagonal),
        "tick2_probe_probability_difference": qtext(Q(112, 50625)),
        "tick3_diagonal_tv": qtext(diagonal_tv_tick3),
    }


def retained_tick1_block_control(arena: WalkArena, ensembles: Mapping[str, Any]) -> dict[str, Any]:
    def blocks(ensemble: ScaledEnsemble) -> tuple[dict[tuple[int, ...], Matrix], dict[tuple[int, ...], Q]]:
        result: dict[tuple[int, ...], Matrix] = {}
        masses: dict[tuple[int, ...], Q] = defaultdict(Q)
        for ensemble_weight, state, scale in ensemble:
            output_raw, postcoin = arena.step(state, ensembles["record0"])
            output = tuple(output_raw)
            normalized_density = core.matscale(scale, core.outer(output))
            for cell, amplitude in enumerate(postcoin):
                probability = scale * amplitude.norm2()
                if probability == 0:
                    continue
                record = list(ensembles["record0"])
                record[cell] += 1
                key = tuple(record)
                branch_weight = ensemble_weight * probability
                masses[key] += branch_weight
                contribution = core.matscale(branch_weight, normalized_density)
                result[key] = contribution if key not in result else core.matadd(result[key], contribution)
        return result, dict(masses)

    z_blocks, z_masses = blocks(ensembles["z"])
    x_blocks, x_masses = blocks(ensembles["x"])
    keys = set(z_blocks) | set(x_blocks)
    differing_entries = 0
    for key in keys:
        left = z_blocks.get(key, core.zero(arena.dimension, arena.dimension))
        right = x_blocks.get(key, core.zero(arena.dimension, arena.dimension))
        differing_entries += sum(a != b for left_row, right_row in zip(left, right) for a, b in zip(left_row, right_row))
    return {
        "count_law_equal": z_masses == x_masses,
        "state_record_block_different": differing_entries > 0,
        "differing_entries": differing_entries,
    }


def future_distribution(arena: WalkArena, context: tuple[Vector, tuple[int, ...], tuple[int, ...], Q], horizon: int) -> dict[tuple[int, ...], Q]:
    state, record, _history, _weight = context
    frontier = [(state, record, tuple(), Q(1))]
    for _ in range(horizon):
        next_frontier = []
        for current_state, current_record, suffix, weight in frontier:
            output, postcoin = arena.step(current_state, current_record)
            for cell, amplitude in enumerate(postcoin):
                probability = amplitude.norm2()
                if probability == 0:
                    continue
                changed = list(current_record)
                changed[cell] += 1
                next_frontier.append((output, tuple(changed), suffix + (cell,), weight * probability))
        frontier = next_frontier
    result: dict[tuple[int, ...], Q] = defaultdict(Q)
    for _state, _record, suffix, weight in frontier:
        result[suffix] += weight
    return dict(result)


def distribution_key(distribution: Mapping[tuple[int, ...], Q]) -> tuple[tuple[tuple[int, ...], str], ...]:
    return tuple(sorted((key, qtext(value)) for key, value in distribution.items()))


def predictive_census(arena: WalkArena, source: Mapping[str, Any], fixture: Mapping[str, Any], mutant: str | None) -> list[dict[str, Any]]:
    rows = []
    for past in fixture["s1"]["past_depths"]:
        contexts = literal_contexts(arena, source, int(past))
        for future in fixture["s1"]["future_horizons"]:
            laws = [distribution_key(future_distribution(arena, context, int(future))) for context in contexts]
            quotient = len(set(laws))
            law_groups: dict[Any, list[int]] = defaultdict(list)
            for index, law in enumerate(laws):
                law_groups[law].append(index)
            duplicate_group = next((indices for indices in law_groups.values() if len(indices) > 1), [])
            summaries: dict[str, Callable[[tuple[Vector, tuple[int, ...], tuple[int, ...], Q]], Any]] = {
                "NO-TRACE": lambda context: 0,
                "PREVIOUS-TRIGGER": lambda context: context[2][-1],
                "UNORDERED-COUNTS": lambda context: tuple(context[2].count(cell) for cell in range(arena.dimension)),
                "SUFFIX-2": lambda context: context[2][-2:],
                "FULL-ORDERED-TRACE": lambda context: context[2],
            }
            if mutant == "predictive-merge":
                summaries["FULL-ORDERED-TRACE"] = lambda context: 0
            status = {}
            blocks = {}
            for name, summary in summaries.items():
                grouped: dict[str, set[Any]] = defaultdict(set)
                for context, law in zip(contexts, laws):
                    grouped[repr(summary(context))].add(law)
                status[name] = all(len(items) == 1 for items in grouped.values())
                blocks[name] = len(grouped)
            sufficient = [name for name in fixture["s1"]["summaries"] if status[name]]
            rows.append(
                {
                    "past": int(past),
                    "future": int(future),
                    "histories": len(contexts),
                    "predictive_quotient": quotient,
                    "sufficient": status,
                    "summary_blocks": blocks,
                    "first_registered_sufficient": sufficient[0] if sufficient else None,
                    "duplicate_history_pair": [list(contexts[index][2]) for index in duplicate_group[:2]],
                }
            )
    return rows


def future_record_distribution(
    arena: WalkArena,
    context: tuple[Vector, tuple[int, ...], tuple[int, ...], Q],
    horizon: int,
) -> dict[tuple[int, ...], Q]:
    state, record, _history, _weight = context
    frontier = [(state, record, Q(1))]
    for _ in range(horizon):
        next_frontier = []
        for current_state, current_record, weight in frontier:
            output, postcoin = arena.step(current_state, current_record)
            for cell, amplitude in enumerate(postcoin):
                probability = amplitude.norm2()
                if probability == 0:
                    continue
                changed = list(current_record)
                changed[cell] += 1
                next_frontier.append((tuple(output), tuple(changed), weight * probability))
        frontier = next_frontier
    result: dict[tuple[int, ...], Q] = defaultdict(Q)
    for _state, final_record, weight in frontier:
        result[final_record] += weight
    return dict(result)


def record_distribution_key(distribution: Mapping[tuple[int, ...], Q]) -> tuple[tuple[tuple[int, ...], str], ...]:
    return tuple(sorted((key, qtext(value)) for key, value in distribution.items()))


def complete_predictive_controls(
    arena: WalkArena,
    source: Mapping[str, Any],
    fixture: Mapping[str, Any],
    mutant: str | None,
    suffix_rows: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    suffix_cache: dict[tuple[tuple[str, ...], tuple[int, ...], int], Any] = {}

    def suffix_signature(state: Vector, record: tuple[int, ...], horizon: int) -> Any:
        """Exact ordered-suffix law without expanding a flat path dictionary."""
        # Suffix probabilities see only the ray and record residues.  Quotienting
        # global phase and completed record cycles is exact for this walk and
        # prevents the same predictive state from being traversed once per past.
        key = (ew_ray_key(state), tuple(value % arena.order for value in record), horizon)
        if key in suffix_cache:
            return suffix_cache[key]
        if horizon == 0:
            return tuple()
        output_raw, postcoin = arena.step(state, record)
        output = tuple(output_raw)
        rows = []
        for cell, amplitude in enumerate(postcoin):
            probability = amplitude.norm2()
            if probability == 0:
                continue
            changed = list(record)
            changed[cell] += 1
            rows.append((cell, qtext(probability), suffix_signature(output, tuple(changed), horizon - 1)))
        value = tuple(rows)
        suffix_cache[key] = value
        return value

    complete_rows = []
    present_state_rows = []
    for past in fixture["s1"]["past_depths"]:
        contexts = literal_contexts(arena, source, int(past))
        for future in fixture["s1"]["future_horizons"]:
            laws = [record_distribution_key(future_record_distribution(arena, context, int(future))) for context in contexts]
            complete_rows.append(
                {
                    "past": int(past),
                    "future": int(future),
                    "histories": len(contexts),
                    "final_record_quotient": len(set(laws)),
                }
            )
        present_state_rows.append(
            {
                "past": int(past),
                "fine_states": len({(ew_ray_key(context[0]), context[1]) for context in contexts}),
                "kernel_argument_fields": ["state", "record", "horizon"],
            }
        )
    target_row = next(row for row in suffix_rows if row["past"] == 3 and row["future"] == 2)
    duplicate_histories = [tuple(history) for history in target_row["duplicate_history_pair"]]
    context_by_history = {context[2]: context for context in literal_contexts(arena, source, 3)}
    pair = [context_by_history[history] for history in duplicate_histories]
    pair_h2 = [suffix_signature(context[0], context[1], 2) for context in pair]
    pair_h3 = [suffix_signature(context[0], context[1], 3) for context in pair]
    refinement_witness = {
        "histories": [list(history) for history in duplicate_histories],
        "same_horizon_two_law": pair_h2[0] == pair_h2[1],
        "different_horizon_three_law": pair_h3[0] != pair_h3[1],
        "horizon_two_law_digest": digest(pair_h2[0]),
        "horizon_three_law_digests": [digest(value) for value in pair_h3],
    }
    if mutant == "complete-s1":
        complete_rows[0]["final_record_quotient"] = 1
    s1_requirements = {"future_instrument", "interventions", "partition_stabilization"}
    s1_available = key_census(fixture["s1"])
    return {
        "final_record_rows": complete_rows,
        "present_state_rows": present_state_rows,
        "horizon_three_refinement_witness": refinement_witness,
        "suffix_stabilized_within_1_3": not refinement_witness["different_horizon_three_law"],
        "complete_js_s1a_entered": s1_requirements <= s1_available,
        "missing_js_s1a_objects": sorted(s1_requirements - s1_available),
        "scope": "final-record and future-trigger-suffix grains; full intervention-complete JS-S1a unentered",
    }


def aggregate_method_status(fixture: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "aggregate_output_state_variables",
        "aggregate_psd_constraints",
        "aggregate_mixed_state_propagator",
        "aggregate_target_equations",
        "aggregate_operational_null_quotient",
    }
    available = key_census(fixture)
    missing = sorted(required - available)
    return {
        "required_objects": sorted(required),
        "missing_objects": missing,
        "entered": not missing,
        "word": "QSF-AFFINE-METHOD-INCONCLUSIVE-AT-A1-A2-AGGREGATE-PROBLEM",
    }


def affine_single_continuation_control(arena: WalkArena, source: Mapping[str, Any], wrc_fixture: Mapping[str, Any]) -> dict[str, Any]:
    controls = wrc_fixture["controls"]
    record = tuple(int(source["initial_record_entry"]) for _ in range(arena.dimension))
    coin = arena.coin_matrix(record)
    first, second = (int(value) for value in controls["continuation_postcoin_cells"])
    coefficients = [Q(value) for value in controls["continuation_postcoin_vector"]]
    postcoin = tuple(EW(coefficients[0]) if index == first else EW(coefficients[1]) if index == second else ZERO for index in range(arena.dimension))
    input_state = core.matvec(core.adjoint(coin), postcoin)
    source_output, source_postcoin = arena.step(input_state, record)
    cell = int(controls["continuation_outcome_cell"])
    effect_vectors = []
    output_vectors = []
    for index in range(arena.dimension):
        basis = tuple(ONE if position == index else ZERO for position in range(arena.dimension))
        effect_vectors.append(core.matvec(core.adjoint(coin), basis))
        output_vectors.append(source_output if index == cell else arena.shift_apply(basis))
    ports = core.rank_one_completion(effect_vectors, output_vectors)
    operation = core.conjugate_by(ports[cell], core.density(input_state))
    expected = core.matscale(source_postcoin[cell].norm2(), core.density(source_output))
    return {
        "complete": core.instrument_total(ports) == core.identity(arena.dimension),
        "single_input_match": operation == expected,
        "probability": source_postcoin[cell].norm2(),
    }


def apply_mutant(fixture: MutableMapping[str, Any], mutant: str | None) -> None:
    if mutant is None:
        return
    if mutant not in MUTANTS:
        raise ValueError(f"unknown mutant {mutant!r}")
    if mutant == "anchor-hash":
        fixture["anchors"][0]["sha256"] = "0" * 64
    elif mutant == "fixture-answer":
        fixture["answer"] = "INJECTED"
    elif mutant == "coin-entry":
        fixture["source_packet"]["coin_numerators"][0][0] += 1
    elif mutant == "shift-orientation":
        fixture["source_packet"]["shift_orientation"] = "MINUS"
    elif mutant == "literal-collapse":
        fixture["source_packet"]["conditioned_state_rule"] = "COLLAPSE"
    elif mutant == "a0-output":
        fixture["arm_a"]["contexts_through_tick"] = 4
    elif mutant == "history-window":
        fixture["arm_c"]["windows"] = [1, 2, 3, 4]
    elif mutant == "record-retention":
        fixture["arm_c"]["maps"] = ["DISCARD-INTERNAL-HITS"]
    elif mutant == "s1b-entry":
        fixture["s1"]["s1b_requires_closed_finite_law_family"] = False
    elif mutant == "scope-promotion":
        fixture["scope_walls"].remove("NO-RELATIONAL-COMPOSITE")


def score(fixture_path: Path, mutant: str | None = None) -> dict[str, Any]:
    fixture = json.loads(fixture_path.read_text())
    apply_mutant(fixture, mutant)
    gates: list[dict[str, Any]] = []
    forbidden = {"answer", "expected", "verdict", "solution", "pass_count", "survivor_count"}
    present = sorted(forbidden & key_census(fixture))
    gate(gates, "QSF-FIXTURE-NEUTRAL", "the frozen physical fixture contains no answer-bearing field", not present and not contains_float(fixture), {"forbidden": present, "float": contains_float(fixture)})

    root = root_path()
    anchor_rows = []
    for anchor in fixture["anchors"]:
        path = root / anchor["path"]
        observed = sha256_bytes(path.read_bytes()) if path.exists() else None
        anchor_rows.append({"path": anchor["path"], "expected": anchor["sha256"], "observed": observed, "ok": observed == anchor["sha256"]})
    gate(gates, "QSF-ANCHORS", "every frozen antecedent is byte-bound", all(row["ok"] for row in anchor_rows), {"rows": anchor_rows})

    source = fixture["source_packet"]
    arena = WalkArena(source)
    gate(gates, "QSF-PACKET-TYPE", "the independently rebuilt WRC carrier has the declared fixed type", arena.dimension == 27 and len(arena.sites) == 9 and len(arena.links) == 3 and source["conditioned_state_rule"] == "NONCOLLAPSE", {"dimension": arena.dimension, "sites": len(arena.sites), "links": len(arena.links), "rule": source["conditioned_state_rule"]})

    committed_receipt = json.loads((root / fixture["committed_observable_bindings"]["receipt_path"]).read_text())
    committed = committed_receipt["results"]["source_regression"]
    literal = run_walk(arena, source, "LITERAL")
    literal_matches = source_match(literal, committed)
    gate(gates, "QSF-WRC-REGRESSION", "the independent walk reproduces all nine committed observable families before the fork", all(literal_matches.values()) and literal["branch_counts"] == committed["branch_counts"] and [qtext(value) for value in literal["mass_rows"]] == committed["mass_rows"], {"matches": literal_matches, "branch_counts": literal["branch_counts"]})

    projective = run_walk(arena, source, "PROJECTIVE")
    projective_matches = source_match(projective, committed)
    if mutant == "affine-control":
        projective_matches = dict(literal_matches)
    fitted = affine_single_continuation_control(arena, source, json.loads((root / "v16/code/wrc_fixture.json").read_text()))
    third_completion = third_completion_control(arena, source)
    gate(gates, "QSF-AFFINE-CONTROLS", "the displayed projective law is complete but moves the packet, another complete member fits one continuation only, and a third complete member differs from both controls", fitted["complete"] and fitted["single_input_match"] and not all(projective_matches.values()) and third_completion["complete"] and third_completion["normalized_outputs"] and third_completion["different_from_projective"] == arena.dimension, {"projective_survival": projective_matches, "fitted": {key: qtext(value) if isinstance(value, Fraction) else value for key, value in fitted.items()}, "third_completion": third_completion})

    collisions, aligned_collisions, aggregate_phase = branch_control_census(arena, source, mutant)
    record_collision = a0_record_collision(arena, source, mutant)
    aggregate_method = aggregate_method_status(fixture)
    gate(gates, "QSF-A0-RECORD-COLLISION", "one record-indexed output state cannot interpolate the reached process", fixture["arm_a"]["contexts_through_tick"] == 5 and record_collision["same_record"] and record_collision["both_live"] and record_collision["different_output_rays"], record_collision)
    gate(gates, "QSF-AFFINE-RECURRENCE", "literal branch outputs conflict both in the raw local dictionary and after translation to a common event frame", collisions["conflicting_signatures"] > 0 and aligned_collisions["conflicting_signatures"] > 0, {"raw": collisions, "aligned": aligned_collisions})
    gate(gates, "QSF-AGGREGATE-BRANCH-SEPARATION", "a terminal phase family moves every branch ray while preserving every registered terminal basis aggregate", aggregate_phase["contexts"] == 10527 and aggregate_phase["moved_rays"] == aggregate_phase["contexts"] and aggregate_phase["basis_probabilities_equal"] and aggregate_phase["all_nine_terminal_aggregates_equal"], aggregate_phase)
    gate(gates, "QSF-AGGREGATE-METHOD-ENTRY", "the A1/A2 aggregate positive mixed-state problem is explicitly unentered rather than declared empty", not aggregate_method["entered"] and bool(aggregate_method["missing_objects"]), aggregate_method)
    arm_a = {
        "a0_record_context_exact": not record_collision["different_output_rays"],
        "a0_state_history_lookup_is_affine_law": False,
        "a0_law_selected": False,
        "a0_survival_vector": literal_matches,
        "projective_survival_vector": projective_matches,
        "a1_exact_branch_reproduction": collisions["conflicting_signatures"] == 0,
        "a2_exact_branch_reproduction": aligned_collisions["conflicting_signatures"] == 0,
        "record_collision": record_collision,
        "signature_census": collisions,
        "aligned_signature_census": aligned_collisions,
        "aggregate_phase_control": aggregate_phase,
        "aggregate_method": aggregate_method,
        "aggregate_problem_entered": aggregate_method["entered"],
        "word": aggregate_method["word"],
    }

    ensembles = embedded_ensembles(arena, source, mutant)
    composite_ok = (
        ensembles["density_equal"]
        and ensembles["orthogonal"]
        and ensembles["composite"]["joint_trace"]
        and ensembles["composite"]["bob_marginal"]
        and ensembles["composite"]["z_conditionals"]
        and ensembles["composite"]["x_conditionals"]
        and ensembles["composite"]["alice_complete"]
        and all(value == Q(1, 2) for value in ensembles["composite"]["probabilities"])
    )
    gate(gates, "QSF-COMPOSITE-HJW", "the exact 2 x 27 fixed-factor surrogate has complete Alice instruments, one Bob marginal, and the canonical Z/X remote preparations", composite_ok, {"density_equal": ensembles["density_equal"], "orthogonal": ensembles["orthogonal"], "composite": core.serialize(ensembles["composite"]), "relational_composite": fixture["arm_b"]["relational_composite_built"]})
    literal_z = ensemble_process(arena, ensembles["z"], ensembles["record0"], 5, "LITERAL", mutant == "ontic-history")
    literal_x = ensemble_process(arena, ensembles["x"], ensembles["record0"], 5, "LITERAL", mutant == "ontic-history")
    literal_windows = compare_ensemble_windows(literal_z, literal_x)
    projective_z = ensemble_process(arena, ensembles["z"], ensembles["record0"], 3, "PROJECTIVE")
    projective_x = ensemble_process(arena, ensembles["x"], ensembles["record0"], 3, "PROJECTIVE")
    projective_windows = compare_ensemble_windows(projective_z, projective_x)
    if mutant == "affine-control":
        projective_windows[1]["history_tv"] = Q(1)
    phase_affine = phase_mub_and_affine_controls(arena, ensembles, mutant)
    no_feedback_tv = no_feedback_screen_control(arena, ensembles, 5)
    causal_windows = copy.deepcopy(literal_windows)
    if mutant == "count-readout":
        causal_windows[1]["record_tv"] = Q(0)
    if mutant == "tick4-screen":
        causal_windows[3]["discard_screen_tv"] = Q(0)
    expected_history = [Q(0), Q(1, 2), Q(211, 324), Q(180223, 236196), Q(1694745299, 2066242608)]
    expected_count = [Q(0), Q(1, 2), Q(211, 324), Q(12415, 17496), Q(820725659, 1162261467)]
    expected_screen = [Q(0), Q(0), Q(0), Q(1664, 19683), Q(3747023, 43046721)]
    gate(gates, "QSF-NATURAL-COMPOSITE-WITNESS", "the literal pure-ray rule changes Bob's calibrated count-record law under remote Z/X preparation while the affine control does not", [row["history_tv"] for row in causal_windows] == expected_history and [row["record_tv"] for row in causal_windows] == expected_count and [row["discard_screen_tv"] for row in causal_windows] == expected_screen and all(row["history_tv"] == 0 and row["record_tv"] == 0 for row in projective_windows), {"literal_history_tv": [qtext(row["history_tv"]) for row in causal_windows], "literal_count_tv": [qtext(row["record_tv"]) for row in causal_windows], "literal_screen_tv": [qtext(row["discard_screen_tv"]) for row in causal_windows], "affine_history_tv": [qtext(row["history_tv"]) for row in projective_windows]})
    gate(gates, "QSF-CAUSALITY-CONTROLS", "a second mutually unbiased basis reproduces the witness, outcome relabeling is inert, a distinct affine history law is blind, and removing feedback removes every screen difference", phase_affine["phase_history_tv"] == expected_history[:3] and phase_affine["phase_record_tv"] == expected_count[:3] and phase_affine["outcome_relabel_invariant"] and all(value == 0 for value in phase_affine["cyclic_affine_history_tv"] + phase_affine["cyclic_affine_record_tv"] + no_feedback_tv), {"phase_mub": core.serialize(phase_affine), "no_feedback_screen_tv": [qtext(value) for value in no_feedback_tv]})
    arm_b = {
        "composite": "NATURAL-FIXED-FACTOR",
        "relational_composite_built": False,
        "density_equal": ensembles["density_equal"],
        "literal_windows": [{key: qtext(value) if isinstance(value, Fraction) else value for key, value in row.items() if key not in {"record_probe_moved", "record_boundary_witness"}} for row in causal_windows],
        "affine_history_tv": [qtext(row["history_tv"]) for row in projective_windows],
        "phase_and_affine_controls": core.serialize(phase_affine),
        "no_feedback_screen_tv": [qtext(value) for value in no_feedback_tv],
        "word": "PHRASABLE-SIGNALLING-WITNESS",
        "scope": "remote-setting dependence in the natural no-interaction fixed-factor extension at Bob count-record grain; relational composite remains unbuilt",
    }

    record_failures = [row for row in literal_windows if row["record_boundary_witness"]]
    discard_one_affine = literal_windows[0]["discard_screen_tv"] == 0
    feedback_moved = [row["tick"] for row in literal_windows[1:] if row["discard_screen_tv"] != 0]
    retained_tick1 = retained_tick1_block_control(arena, ensembles)
    density_witness = density_affinity_witness(arena, source, mutant)
    if mutant == "record-retention":
        record_failures = []
    gate(gates, "QSF-HISTORY-BOUNDARIES", "the retained state-record block distinguishes equal-density ensembles at every registered window, while the tick-one count law alone does not", [row["tick"] for row in record_failures] == [1, 2, 3, 4, 5] and retained_tick1["count_law_equal"] and retained_tick1["state_record_block_different"] and discard_one_affine and bool(feedback_moved) and fixture["arm_c"]["windows"] == [1, 2, 3, 4, 5], {"record_failure_ticks": [row["tick"] for row in record_failures], "retained_tick1": retained_tick1, "discard_tick1_diagonal_screen_equal": discard_one_affine, "feedback_moved_ticks": feedback_moved})
    gate(gates, "QSF-DENSITY-SUFFICIENCY", "an independent equal-density preparation pair has a hidden tick-two full-density difference and a later diagonal witness", density_witness["input_density_equal"] and density_witness["tick2_different_entries"] == 72 and density_witness["tick2_diagonal_blind"] and density_witness["tick2_offdiagonal_1_7"] == "(448/151875,224/151875)" and density_witness["tick2_probe_probability_difference"] == "112/50625" and density_witness["tick3_diagonal_tv"] == "99328/4100625", density_witness)
    arm_c = {
        "windows": [
            {
                "tick": row["tick"],
                "record_history_tv": qtext(row["history_tv"]),
                "record_count_tv": qtext(row["record_tv"]),
                "discard_screen_tv": qtext(row["discard_screen_tv"]),
                "record_probe_moved": row["record_probe_moved"],
                "record_boundary_witness": row["record_boundary_witness"],
            }
            for row in literal_windows
        ],
        "record_recoverability_absolute": False,
        "cut_cp_test_entered": False,
        "binding_scope": "NO-RHO-SUFFICIENT-RETAINED-STATE-RECORD-MAP",
        "fine_state_kernel": "NORMALIZED-STOCHASTIC-KERNEL-ON-([psi],record)",
        "fine_state_kernel_is_standard_quantum_instrument": False,
        "retained_tick1_control": retained_tick1,
        "density_affinity_witness": density_witness,
        "word": "QSF-HISTORY-NO-AFFINE-RECORD-BOUNDARY-WITHIN-1-5",
    }

    s1_rows = predictive_census(arena, source, fixture, mutant)
    complete_s1 = complete_predictive_controls(arena, source, fixture, mutant, s1_rows)
    suffix_expected = [1, 1, 2, 15, 126, 485]
    final_record_expected = [3, 3, 27, 27, 486, 486]
    gate(gates, "QSF-S1-SUFFIX", "the published quotient table is exactly the ordered-future-trigger-suffix census and full ordered pasts suffice on those finite rows", [row["predictive_quotient"] for row in s1_rows] == suffix_expected and all(row["sufficient"]["FULL-ORDERED-TRACE"] for row in s1_rows), {"rows": [{"past": row["past"], "future": row["future"], "quotient": row["predictive_quotient"], "first": row["first_registered_sufficient"]} for row in s1_rows]})
    gate(gates, "QSF-S1-COMPLETE-CONTROLS", "the calibrated final-record grain and an exact horizon-three refinement witness are distinguished from complete JS-S1a", [row["final_record_quotient"] for row in complete_s1["final_record_rows"]] == final_record_expected and complete_s1["horizon_three_refinement_witness"]["same_horizon_two_law"] and complete_s1["horizon_three_refinement_witness"]["different_horizon_three_law"] and not complete_s1["suffix_stabilized_within_1_3"] and not complete_s1["complete_js_s1a_entered"], complete_s1)
    s1b_not_entered = fixture["s1"]["s1b_requires_closed_finite_law_family"] and not arm_a["aggregate_problem_entered"] and not complete_s1["complete_js_s1a_entered"]
    gate(gates, "QSF-S1B-DISPOSITION", "S1b is not entered because neither the aggregate law family nor the prerequisite intervention-complete S1a object was constructed", s1b_not_entered, {"aggregate_problem_entered": arm_a["aggregate_problem_entered"], "complete_js_s1a_entered": complete_s1["complete_js_s1a_entered"], "not_entered": s1b_not_entered})

    gate(gates, "QSF-SCOPE", "all unbuilt relational, geometric, continuum, and selection claims remain refused", set(fixture["scope_walls"]) == REQUIRED_WALLS and not fixture["arm_b"]["relational_composite_built"], {"walls": len(fixture["scope_walls"]), "relational_composite": fixture["arm_b"]["relational_composite_built"]})

    arm_statuses = {
        "arm_a_aggregate_method_unentered": not arm_a["aggregate_problem_entered"] and arm_a["signature_census"]["conflicting_signatures"] > 0 and not arm_a["a0_record_context_exact"],
        "arm_b_natural_fixed_factor_rejected": arm_b["word"] == "PHRASABLE-SIGNALLING-WITNESS" and arm_b["literal_windows"][1]["record_tv"] == "1/2" and not arm_b["relational_composite_built"],
        "arm_c_rho_insufficient": arm_c["binding_scope"] == "NO-RHO-SUFFICIENT-RETAINED-STATE-RECORD-MAP" and arm_c["density_affinity_witness"]["tick2_different_entries"] == 72,
        "s1_complete_method_unentered": not complete_s1["complete_js_s1a_entered"],
    }
    independent = "QSF-METHOD-INCONCLUSIVE" if all(arm_statuses.values()) else "QSF-WRC-BASE-DYNAMICS-REFUSED"
    synthesis = independent
    if mutant in {"primary-comparator", "primary-derivation"}:
        synthesis = "QSF-WRC-BASE-DYNAMICS-REFUSED"
    gate(gates, "QSF-PRIMARY-COMPARATOR", "the synthesis word is derived only from measured arm-status objects and independently recomputed", synthesis == independent and synthesis in SYNTHESIS_WORDS, {"primary": synthesis, "independent": independent, "arm_statuses": arm_statuses})

    exact_marker: Any = Q(1, 3)
    if mutant == "exactness":
        exact_marker = float(Q(1, 3))
    gate(gates, "QSF-EXACTNESS", "the result surface is exact and contains no runtime float", isinstance(exact_marker, Fraction), {"marker": str(exact_marker)})

    result = {
        "schema": "qsf-result-v2",
        "arithmetic": "Q(omega) vectors with exact rational norm scales",
        "arm_a": arm_a,
        "arm_b": arm_b,
        "arm_c": arm_c,
        "s1": {
            "suffix_rows": s1_rows,
            "complete_controls": complete_s1,
            "s1b": "QSF-S1B-NOT-ENTERED-BECAUSE-A1-A2-AND-COMPLETE-S1A-UNENTERED",
        },
        "derived_arm_statuses": arm_statuses,
        "synthesis": synthesis,
        "scope_walls": sorted(REQUIRED_WALLS),
        "gates": gates,
        "mutants": list(MUTANTS),
    }
    result = core.serialize(result)
    if contains_float(result):
        raise GateFail("QSF-RUNTIME-FLOAT")
    result["payload_sha256"] = digest(result)
    return result


def transcript(result: Mapping[str, Any]) -> str:
    lines = [
        "QSF PAPER 9 QUANTUM-SEAM ASSAY",
        f"gates={len(result['gates'])} passed={sum(row['ok'] for row in result['gates'])}",
        f"arm_a={result['arm_a']['word']}",
        f"a0_record_context_exact={str(result['arm_a']['a0_record_context_exact']).lower()}",
        f"a1_conflicting_signatures={result['arm_a']['signature_census']['conflicting_signatures']}",
        f"a2_aligned_conflicting_signatures={result['arm_a']['aligned_signature_census']['conflicting_signatures']}",
        f"aggregate_problem_entered={str(result['arm_a']['aggregate_problem_entered']).lower()}",
        f"projective_survival={sum(result['arm_a']['projective_survival_vector'].values())}/9",
        f"arm_b={result['arm_b']['word']}",
        f"literal_fixed_factor_history_tv={','.join(row['history_tv'] for row in result['arm_b']['literal_windows'])}",
        f"literal_fixed_factor_count_tv={','.join(row['record_tv'] for row in result['arm_b']['literal_windows'])}",
        f"arm_c={result['arm_c']['word']}",
        f"arm_c_scope={result['arm_c']['binding_scope']}",
        f"tick2_density_difference_entries={result['arm_c']['density_affinity_witness']['tick2_different_entries']}",
        f"suffix_quotients={','.join(str(row['predictive_quotient']) for row in result['s1']['suffix_rows'])}",
        f"final_record_quotients={','.join(str(row['final_record_quotient']) for row in result['s1']['complete_controls']['final_record_rows'])}",
        f"complete_js_s1a_entered={str(result['s1']['complete_controls']['complete_js_s1a_entered']).lower()}",
        f"s1b={result['s1']['s1b']}",
        f"synthesis={result['synthesis']}",
        f"payload_sha256={result['payload_sha256']}",
    ]
    return "\n".join(lines) + "\n"


def render_paper(result: Mapping[str, Any], fixture_hash: str, scorer_hash: str, transcript_hash: str) -> str:
    """Render the panel-adjudicated bounded repair."""
    a = result["arm_a"]
    b = result["arm_b"]
    c = result["arm_c"]
    s1_rows = result["s1"]["suffix_rows"]
    complete_s1 = result["s1"]["complete_controls"]
    projective_survivors = [name for name, survived in a["projective_survival_vector"].items() if survived]
    projective_moved = [name for name, survived in a["projective_survival_vector"].items() if not survived]
    history_table = "\n".join(
        f"| {row['tick']} | {row['record_history_tv']} | {row['record_count_tv']} | {row['discard_screen_tv']} | {str(row['record_boundary_witness']).lower()} |"
        for row in c["windows"]
    )
    s1_table = "\n".join(
        f"| {row['past']} | {row['future']} | {row['histories']} | {row['predictive_quotient']} | {row['first_registered_sufficient']} |"
        for row in s1_rows
    )
    final_record_table = "\n".join(
        f"| {row['past']} | {row['future']} | {row['histories']} | {row['final_record_quotient']} |"
        for row in complete_s1["final_record_rows"]
    )
    return f"""# Paper 9 — The quantum seam of the reconstructed walk

## Adjudicated status

**Primary:** `{result['synthesis']}`.

This is the bounded repair ordered by the frozen three-seat panel. It does
**not** choose a fundamental law. It separates four questions previously run
together: whether one affine instrument reproduces WRC, whether an ontic
pure-ray extension is compositionally safe, whether `rho` is a sufficient
retained state, and whether the measured predictive partitions constitute a
complete JS-S1 assay. Several identifications fail exactly; selection among
the remaining law types is method-inconclusive.

## 1. Reconstruction and method

The scorer independently rebuilds the 27-cell fixed-carrier walk from the
result-neutral fixture. All nine terminal WRC observable families reproduce
before any seam test. Every arm status and the primary are then derived from
computed objects; no verdict-bearing fixture literal supplies the synthesis.

## 2. Arm A — lookup is not a law

Every affine CP operation with WRC's rank-one effect has fixed-output form
`J_c(rho)=Tr(E_c rho) sigma_c`. Arbitrary normalized positive `sigma_c` choices
form a complete instrument family. But the originally claimed record-indexed
A0 dictionary is false. Histories `(0,12,13)` and `(0,13,12)` reach the same
full count record, admit outcome `c=0`, and require different output rays.
Adding the ray or full history to the key makes a finite lookup exact by
definition; it does not produce one affine density-operator law.

The raw recurrence census finds **{a['signature_census']['conflicting_signatures']}**
conflicting local signatures; after translating each event to one common
frame, **{a['aligned_signature_census']['conflicting_signatures']}** remain.
Literal branch reproduction therefore does not descend to registered A1/A2
locality. This is not an aggregate no-go. A terminal phase control moves all
{a['aggregate_phase_control']['contexts']} terminal rays while preserving all
basis probabilities and all nine registered aggregate families. The positive
mixed-state aggregate problem was never constructed; its licensed status is
method nonentry, not an empty or measured variety.

The displayed projective control preserves {sum(a['projective_survival_vector'].values())}
of nine families. Preserved: `{', '.join(projective_survivors) or 'none'}`.
Moved: `{', '.join(projective_moved) or 'none'}`. Another complete member fits
one continuation and a cyclic third member confirms that two controls do not
exhaust the family.

**Arm A:** `{a['word']}`.

## 3. Arm B — the natural ontic-ray composite fails

The exact `2 x 27` Bell/HJW surrogate remotely prepares two decompositions of
one Bob density operator. Under the literal fine-ray rule, ordered-history TVs
through ticks one to five are
`{', '.join(row['history_tv'] for row in b['literal_windows'])}`; calibrated
count-record TVs are
`{', '.join(row['record_tv'] for row in b['literal_windows'])}`. The count
record already moves at tick two, so this does not rely on treating Bob's ray
as observable. A second mutually unbiased basis repeats the first three rows,
Alice-outcome relabeling is inert, and two affine fixed-output controls are
blind.

This rejects the natural fixed-factor extension when Alice outcomes and Bob
count facts are physical. It is remote-setting dependence in a no-interaction
surrogate, not a Lorentzian faster-than-light theorem: distance, light cones,
changing factors, and a relational composite are absent.

**Arm B:** `{b['word']}` — {b['scope']}.

## 4. Arm C — `rho` is insufficient; stochastic law is not excluded

At tick one the Z/X count laws agree, while correlations between record sector
and conditioned process state differ. At later ticks the count law itself
differs. Erasing readout and erasing record-conditioned feedback are distinct:
the first hides the early count witness but leaves screen TV `1664/19683` at
tick four; the second gives the affine null.

| tick | ordered-history TV | count-record TV | record-erased screen TV | retained state-record witness |
|---:|---:|---:|---:|:---:|
{history_table}

An independent equal-density pair sharpens the result. At tick two the full
discarded density differs in {c['density_affinity_witness']['tick2_different_entries']}
entries although every basis diagonal agrees. Entry `(1,7)` differs by
`(448+224 omega)/151875`; a superposition probe moves by `112/50625`. At tick
three the diagonal TV is `99328/4100625`.

Thus no tested retained boundary is a `rho`-sufficient state-record map. That
does not say no stochastic division exists. If the fine state
`([psi],record)` is postulated, WRC defines a normalized stochastic kernel and
acts linearly on probability measures over that fine state. The extra ontic
ray is exactly the extension whose natural fixed-factor composition Arm B
rejects. Cut composition, recoverability, and actualization remain untested.

**Arm C:** `{c['word']}` [`{c['binding_scope']}`].

## 5. S1 — suffix prediction is not complete predictive sufficiency

The published table concerns future ordered trigger suffixes only:

| past depth | future horizon | histories | suffix quotient | first registered sufficient grain |
|---:|---:|---:|---:|---|
{s1_table}

At the calibrated final-count-record grain the quotients are:

| past depth | future horizon | histories | final-record quotient |
|---:|---:|---:|---:|
{final_record_table}

The unique pair of registered past-depth-three histories with equal horizon-
two suffix laws is `{complete_s1['horizon_three_refinement_witness']['histories']}`.
Their exact horizon-three laws differ, so the suffix partition has not
stabilized by horizon two. The law-
native present state `([psi],record)` screens off the generated past in these
fixtures, so quotient growth does not establish an ontic infinite history. A
complete intervention family, future instrument, and stabilization object
were not frozen. Complete JS-S1a and therefore S1b remain unentered.

## 6. Ontology — the Barandes-safe reading

| object | status after QSF |
|---|---|
| fixed meta-catalogue of possible configurations | kinematic input |
| one actual configuration trajectory | candidate ontology only if the fine-state theory is adopted |
| stochastic transition kernel | nomological law |
| probability distribution over trajectories | epistemic ensemble description |
| count record | declared finite-window correlation; absolute permanence unproved |
| `psi`, `rho`, Kraus operators, Hilbert carrier | representations unless extra ontology is explicitly postulated |

Two lawfulness questions must not be conflated. A fundamental stochastic
kernel must normalize and compose on its actual configuration space. Affinity
and CP on `rho` are additionally required when `rho` is claimed to be the
complete operational state. QSF proves that WRC cannot keep both the literal
retained rule and `rho`-completeness. It does not decide among a different
affine instrument, a finer but compositionally safe stochastic ontology, and
a different base law.

Dynamic relational geometry, carrier growth, event selection, a carrier
catalogue, couplings, actualization, Lorentz/continuum structure, QFT/GR,
species, Hamiltonian selection, constants, and empirical deviations remain
unbuilt. A changing graph may later be a configuration value inside one fixed
meta-catalogue, but QSF constructs no graph-generated process or spacetime.

## 7. Integrity

- fixture SHA-256: `{fixture_hash}`
- scorer SHA-256: `{scorer_hash}`
- transcript SHA-256: `{transcript_hash}`
- result payload SHA-256: `{result['payload_sha256']}`
- gates: {len(result['gates'])}/{len(result['gates'])}
- registered targeted mutants: {len(MUTANTS)}

The frozen hostile panel and adjudication precede this bounded repair.
Terminal status is recorded by the separate verification note rather than
asserted by the generator.
"""


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


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=here / "qsf_fixture.json")
    parser.add_argument("--output", type=Path, default=here / "qsf_output.txt")
    parser.add_argument("--receipt", type=Path, default=here / "qsf_receipt.json")
    parser.add_argument("--paper", type=Path, default=here.parent / "paper-09-quantum-seam.md")
    parser.add_argument("--mutant", choices=MUTANTS)
    parser.add_argument("--selftest", action="store_true")
    return parser.parse_args(list(argv))


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_args(sys.argv[1:] if argv is None else argv)
    if arguments.selftest:
        if arguments.mutant is not None:
            raise SystemExit("--selftest cannot be combined with --mutant")
        try:
            score(arguments.fixture.resolve(), "anchor-hash")
        except GateFail:
            return 0
        return 1
    targets = [arguments.output.resolve(), arguments.receipt.resolve(), arguments.paper.resolve()]
    if len(set(targets)) != 3:
        raise SystemExit("output, receipt, and paper targets must differ")
    if any(path.exists() for path in targets):
        raise SystemExit("refusing to overwrite an existing artifact")
    try:
        result = score(arguments.fixture.resolve(), arguments.mutant)
        text = transcript(result)
        if arguments.mutant == "transcript-seal":
            text += "MUTATED\n"
        scorer_hash = sha256_bytes(Path(__file__).read_bytes())
        fixture_hash = sha256_bytes(arguments.fixture.read_bytes())
        text_hash = sha256_bytes(text.encode())
        paper = render_paper(result, fixture_hash, scorer_hash, text_hash)
        if arguments.mutant == "paper-claim":
            paper = paper.replace("**not** choose a fundamental law", "choose a fundamental law", 1)
        expected_text = transcript(result)
        if text != expected_text:
            raise GateFail("QSF-TRANSCRIPT-SEAL")
        expected_paper = render_paper(result, fixture_hash, scorer_hash, text_hash)
        if paper != expected_paper:
            raise GateFail("QSF-PAPER-CLAIM")
        result["fixture_sha256"] = fixture_hash
        result["scorer_sha256"] = scorer_hash
        result["transcript_sha256"] = text_hash
        result["paper_sha256"] = sha256_bytes(paper.encode())
        receipt = canonical_json(result)
    except (GateFail, ValueError, TypeError, ArithmeticError, ZeroDivisionError, KeyError) as error:
        print(f"QSF REFUSAL: {error}", file=sys.stderr)
        return 1
    for path, payload in ((arguments.output.resolve(), text.encode()), (arguments.receipt.resolve(), receipt), (arguments.paper.resolve(), paper.encode())):
        atomic_write(path, payload)
    if arguments.output.read_bytes() != text.encode() or arguments.receipt.read_bytes() != receipt or arguments.paper.read_bytes() != paper.encode():
        raise GateFail("QSF-DISK-INTEGRITY")
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
