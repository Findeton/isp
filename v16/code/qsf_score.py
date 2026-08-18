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


def signature_collision_census(arena: WalkArena, source: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    groups: dict[tuple[Any, ...], set[tuple[str, ...]]] = defaultdict(set)
    contexts = 0
    alternatives = 0
    frontier = literal_contexts(arena, source, 0)
    for tick in range(int(source["horizon"])):
        next_frontier = []
        for state, record, history, weight in frontier:
            contexts += 1
            output, postcoin = arena.step(state, record)
            output_key = ew_ray_key(output)
            for cell, amplitude in enumerate(postcoin):
                probability = amplitude.norm2()
                if probability == 0:
                    continue
                site, link = divmod(cell, arena.link_count)
                residues = tuple(record[arena.cell(site, local)] % arena.order for local in range(arena.link_count))
                signature: tuple[Any, ...] = (residues, link)
                if mutant == "signature-split":
                    signature = (residues, link, history)
                groups[signature].add(output_key)
                alternatives += 1
                changed = list(record)
                changed[cell] += 1
                if tick + 1 < int(source["horizon"]):
                    next_frontier.append((output, tuple(changed), history + (cell,), weight * probability))
        frontier = next_frontier
    conflicts = {key: len(values) for key, values in groups.items() if len(values) > 1}
    return {
        "contexts": contexts,
        "alternatives": alternatives,
        "signatures": len(groups),
        "conflicting_signatures": len(conflicts),
        "max_rays_per_signature": max(conflicts.values(), default=1),
        "example_digest": digest(sorted((repr(key), count) for key, count in conflicts.items())[:8]),
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
                if mode == "PROJECTIVE":
                    basis = tuple(ONE if index == cell else ZERO for index in range(arena.dimension))
                    output = tuple(arena.shift_apply(basis))  # type: ignore[assignment]
                    output_scale = Q(1)
                new_history = history + ((0 if history_mutant else cell),)
                new_record = tuple(changed)
                weight = history_weight * probability
                history_mass[new_history] += weight
                record_mass[new_record] += weight
                record_probe[new_record] += weight * output_scale * output[calibrated_probe_cell].norm2()
                if mode == "PROJECTIVE":
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
                }
            )
    return rows


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
    gate(gates, "QSF-AFFINE-CONTROLS", "the displayed projective law is complete but moves the packet, while another complete member fits one continuation only", fitted["complete"] and fitted["single_input_match"] and not all(projective_matches.values()), {"projective_survival": projective_matches, "fitted": {key: qtext(value) if isinstance(value, Fraction) else value for key, value in fitted.items()}})

    collisions = signature_collision_census(arena, source, mutant)
    gate(gates, "QSF-AFFINE-RECURRENCE", "the exact A0 context interpolant does not descend to the registered recurring local signature", fixture["arm_a"]["contexts_through_tick"] == 5 and collisions["conflicting_signatures"] > 0, collisions)
    arm_a = {
        "a0_context_exact": True,
        "a0_reached_branch_dimension": 0,
        "a0_law_selected": False,
        "a0_survival_vector": literal_matches,
        "projective_survival_vector": projective_matches,
        "a1_exact_branch_reproduction": False,
        "a2_exact_branch_reproduction": False,
        "signature_census": collisions,
        "aggregate_variety_closed": False,
        "word": "QSF-AFFINE-METHOD-INCONCLUSIVE-AT-A1-A2-AGGREGATE-VARIETY",
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
    signal_rows = [row for row in literal_windows[:3] if row["history_tv"] != 0]
    gate(gates, "QSF-NATURAL-COMPOSITE-WITNESS", "the literal pure-ray rule changes Bob's local ordered-history law under remote Z/X preparation while the affine control does not", bool(signal_rows) and all(row["history_tv"] == 0 for row in projective_windows), {"literal_history_tv": [qtext(row["history_tv"]) for row in literal_windows[:3]], "affine_history_tv": [qtext(row["history_tv"]) for row in projective_windows]})
    arm_b = {
        "composite": "NATURAL-FIXED-FACTOR",
        "relational_composite_built": False,
        "density_equal": ensembles["density_equal"],
        "literal_windows": [{key: qtext(value) if isinstance(value, Fraction) else value for key, value in row.items() if key not in {"record_probe_moved", "record_boundary_witness"}} for row in literal_windows[:3]],
        "affine_history_tv": [qtext(row["history_tv"]) for row in projective_windows],
        "word": "PHRASABLE-SIGNALLING-WITNESS",
        "scope": "kills the natural fixed-factor extension only; relational composite remains unbuilt",
    }

    record_failures = [row for row in literal_windows if row["record_boundary_witness"]]
    discard_one_affine = literal_windows[0]["discard_screen_tv"] == 0
    feedback_moved = [row["tick"] for row in literal_windows[1:] if row["discard_screen_tv"] != 0]
    if mutant == "record-retention":
        record_failures = []
    gate(gates, "QSF-HISTORY-BOUNDARIES", "every registered retained-record window distinguishes equal-density ensembles; erasing the first internal hit is the affine control", [row["tick"] for row in record_failures] == [1, 2, 3, 4, 5] and discard_one_affine and bool(feedback_moved) and fixture["arm_c"]["windows"] == [1, 2, 3, 4, 5], {"record_failure_ticks": [row["tick"] for row in record_failures], "discard_tick1_affine_screen": discard_one_affine, "feedback_moved_ticks": feedback_moved})
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
        "word": "QSF-HISTORY-NO-AFFINE-RECORD-BOUNDARY-WITHIN-1-5",
    }

    s1_rows = predictive_census(arena, source, fixture, mutant)
    gate(gates, "QSF-S1A", "full ordered traces are sufficient on every registered finite predictive window and coarser grains are measured rather than assumed", all(row["sufficient"]["FULL-ORDERED-TRACE"] for row in s1_rows), {"rows": [{"past": row["past"], "future": row["future"], "quotient": row["predictive_quotient"], "first": row["first_registered_sufficient"]} for row in s1_rows]})
    s1b_not_entered = fixture["s1"]["s1b_requires_closed_finite_law_family"] and not arm_a["aggregate_variety_closed"]
    gate(gates, "QSF-S1B-DISPOSITION", "S1b is not entered because the affine aggregate law family is not closed", s1b_not_entered, {"family_closed": arm_a["aggregate_variety_closed"], "not_entered": s1b_not_entered})

    gate(gates, "QSF-SCOPE", "all unbuilt relational, geometric, continuum, and selection claims remain refused", set(fixture["scope_walls"]) == REQUIRED_WALLS and not fixture["arm_b"]["relational_composite_built"], {"walls": len(fixture["scope_walls"]), "relational_composite": fixture["arm_b"]["relational_composite_built"]})

    synthesis = "QSF-METHOD-INCONCLUSIVE"
    if mutant == "primary-comparator":
        synthesis = "QSF-WRC-BASE-DYNAMICS-REFUSED"
    independent = (
        "QSF-METHOD-INCONCLUSIVE"
        if arm_a["a0_context_exact"] and not arm_a["aggregate_variety_closed"] and arm_b["word"] == "PHRASABLE-SIGNALLING-WITNESS" and arm_c["word"] == "QSF-HISTORY-NO-AFFINE-RECORD-BOUNDARY-WITHIN-1-5"
        else "QSF-WRC-BASE-DYNAMICS-REFUSED"
    )
    gate(gates, "QSF-PRIMARY-COMPARATOR", "the synthesis word is rebuilt independently from the three visible arm results", synthesis == independent and synthesis in SYNTHESIS_WORDS, {"primary": synthesis, "independent": independent})

    exact_marker: Any = Q(1, 3)
    if mutant == "exactness":
        exact_marker = float(Q(1, 3))
    gate(gates, "QSF-EXACTNESS", "the result surface is exact and contains no runtime float", isinstance(exact_marker, Fraction), {"marker": str(exact_marker)})

    result = {
        "schema": "qsf-result-v1",
        "arithmetic": "Q(omega) vectors with exact rational norm scales",
        "arm_a": arm_a,
        "arm_b": arm_b,
        "arm_c": arm_c,
        "s1": {
            "rows": s1_rows,
            "s1b": "QSF-S1B-NOT-ENTERED-BECAUSE-LAW-FAMILY-NOT-CLOSED",
        },
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
        f"a1_conflicting_signatures={result['arm_a']['signature_census']['conflicting_signatures']}",
        f"projective_survival={sum(result['arm_a']['projective_survival_vector'].values())}/9",
        f"arm_b={result['arm_b']['word']}",
        f"literal_fixed_factor_history_tv={','.join(row['history_tv'] for row in result['arm_b']['literal_windows'])}",
        f"arm_c={result['arm_c']['word']}",
        f"record_boundary_witnesses={sum(row['record_boundary_witness'] for row in result['arm_c']['windows'])}/5",
        f"s1b={result['s1']['s1b']}",
        f"synthesis={result['synthesis']}",
        f"payload_sha256={result['payload_sha256']}",
    ]
    return "\n".join(lines) + "\n"


def render_paper(result: Mapping[str, Any], fixture_hash: str, scorer_hash: str, transcript_hash: str) -> str:
    a = result["arm_a"]
    b = result["arm_b"]
    c = result["arm_c"]
    s1_rows = result["s1"]["rows"]
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
    paper = f"""# Paper 9 — The quantum seam of the reconstructed walk

## Candidate status

**Primary:** `{result['synthesis']}`.

This is a frozen finite-arena candidate, not a terminal result. The literal
WRC dynamics is tested three ways. The natural fixed-factor ontic extension
and every retained-record history window tested here fail their registered
quantum-law gates. A context-indexed affine interpolation exists, but it does
not descend to the registered recurring local signature, and the aggregate
A1/A2 completion variety is not closed by this method. The seam is therefore
sharper but not selected.

## 1. What was reconstructed

The scorer independently rebuilds the 27-cell fixed-carrier walk from the
result-neutral fixture. All nine terminal WRC observable families reproduce
before any repair is applied. The generic steering/history assay was frozen
in a prior commit and contains no WRC value.

## 2. Affine completion family

At the full reached-context grain, one may assign each rank-one outcome a
fixed output equal to the literal output encountered there. This A0 dictionary
reproduces the reached branch process and therefore all nine observables, but
it is an interpolation table, not a uniform local law; its reached exact-fit
dimension is zero and its off-window null freedom remains uncounted.

The recurrence test finds **{a['signature_census']['conflicting_signatures']}**
local signatures that demand more than one output ray (maximum
{a['signature_census']['max_rays_per_signature']}). Therefore the exact A0
dictionary does not descend to A1, and hence not to A2, at branch grain. This
does not prove that no A1/A2 member can reproduce the same nine aggregates;
that semidefinite aggregate variety remains unclosed.

The displayed projective control preserves {sum(a['projective_survival_vector'].values())}
of nine observable families. Preserved: `{', '.join(projective_survivors) or 'none'}`.
Moved: `{', '.join(projective_moved) or 'none'}`. A different complete affine
member exactly fits the one registered continuation, confirming that one
control cannot select the family.

**Arm A:** `{a['word']}`.

## 3. Ontic pure rays and steering

Two orthonormal WRC input rays are embedded as Bob's qubit. The exact Z and X
ensembles have one density operator and arise from the standard Bell/HJW
fixed-factor construction. Bob then runs the literal WRC noncollapse hit rule.
At one tick Alice's choices have the same unconditioned Bob history law; at a
later registered pre-contact tick they differ. The exact ordered-history total
variations are `{', '.join(row['history_tv'] for row in b['literal_windows'])}`.
The affine projective control gives zero at every corresponding window.

This is a signalling witness for the **natural fixed-factor extension**. It is
not a theorem over an unbuilt relational composite, and it does not show that
every nonlinear stochastic process signals. It shows that WRC's literal
decomposition-sensitive rule cannot simply be tensored with standard HJW
steering and retained local hit records.

**Arm B:** `{b['word']}` — {b['scope']}.

## 4. Indivisible-history route

Equal-density Z/X ensembles are evolved through complete literal histories.
The retained count-record sectors distinguish them at every window one through
five. Erasing the first internal hit yields the expected affine one-step
unitary control, but once the hit is retained—or fed into the next record-
dependent coin—the decomposition sensitivity returns.

| ticks | ordered-history TV | count-record TV | record-erased screen TV | retained-boundary witness |
|---:|---:|---:|---:|:---:|
{history_table}

No Choi/CP claim is made for a map after it has failed affinity. Absolute
permanence is also not proved. The result is narrower: none of the five tested
complete retained-record windows can be a lawful density-operator division
map. A Barandes-style history law remains logically possible only with a
different genuine boundary/record doctrine than WRC currently supplies.

**Arm C:** `{c['word']}`.

## 5. Predictive sufficiency

The delivered WRC histories were generated, not supplied as anonymous
operators. The finite two-axis census gives:

| past depth | future horizon | histories | predictive quotient | first registered sufficient grain |
|---:|---:|---:|---:|---|
{s1_table}

These are finite-window results. They do not establish absolute minimality or
stabilization. S1b is not entered because Arm A leaves a continuous, unclosed
aggregate law family.

## 6. Ontology after this assay

What remains real in the tested construction is a fixed-carrier pure-ray and
count-record stochastic process with exact feedback. It is not yet an
operational quantum theory on density operators. The simplest standard
composite extension signals; the existing retained records do not supply a
lawful history boundary; and affine completions exist only as an unselected
family, with exact local recurrence already obstructing literal branch
reproduction.

Dynamic relational geometry, carrier growth, event selection, a carrier
catalogue, couplings, actualization, continuum/Lorentz structure, QFT/GR,
species, Hamiltonian selection, constants, and deviations remain unbuilt.
The growth-walk unit is therefore not assembly work yet: it must inherit a
selected quantum seam or explicitly introduce new dynamics.

## 7. Integrity and scope

- fixture SHA-256: `{fixture_hash}`
- scorer SHA-256: `{scorer_hash}`
- transcript SHA-256: `{transcript_hash}`
- result payload SHA-256: `{result['payload_sha256']}`
- gates: {len(result['gates'])}/{len(result['gates'])}
- registered targeted mutants: {len(MUTANTS)}

This candidate awaits the frozen three-seat hostile protocol and adjudication.
"""
    return paper


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
            paper = paper.replace("not a terminal result", "a terminal result", 1)
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
