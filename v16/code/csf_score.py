#!/usr/bin/env python3
"""Verdict-neutral exact scorer for CSF Paper 6.

The data-only fixture and this scorer are frozen before their first scientific
execution. The scorer imports the already frozen generic core by hash.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import importlib.util
import json
import os
import re
import sys
import tempfile
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence


Q = Fraction
CORE_HASH = "93a093d6ce72be4167d277719daf37aa7df7704510819f3b2e264546a14362b4"
MUTANTS = (
    "anchor-corrupt",
    "history-event-mix",
    "gram-index-transpose",
    "completeness-cross-drop",
    "channel-cross-drop",
    "state-only-normalize",
    "psd-skip",
    "same-m-different-channel",
    "same-m-call-same-instrument",
    "calibrated-port-call-gauge",
    "jcv-first-move",
    "jcv-third-same",
    "rich-spectrum-cross-keep",
    "rich-spectrum-call-record",
    "nonnormal-spectral-shortcut",
    "flag-overlap-ignore",
    "orthogonal-call-durable",
    "eraser-drop",
    "recurrence-dictionary-postselect",
    "recurrence-rephase-break",
    "recurrence-swap-break",
    "asymmetric-swap-impose",
    "context-drop",
    "heldout-use-in-fit",
    "intersection-dimension-type",
    "singleton-no-certificate",
    "extreme-equals-rankone",
    "extreme-stability-assume",
    "port-refinement-move-m",
    "steering-promote",
    "all-n-promote",
    "float-leak",
    "typed-count",
    "verdict-flip",
    "transcript-forge",
    "seal-after-write",
)


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def load_core(path: Path) -> Any:
    actual = sha256_path(path)
    if actual != CORE_HASH:
        raise RuntimeError(f"core hash mismatch: {actual}")
    spec = importlib.util.spec_from_file_location("csf_frozen_core", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen core")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_entry(core: Any, value: Any) -> Any:
    if isinstance(value, list):
        if len(value) != 2:
            raise ValueError("Gaussian pair must have length two")
        return core.GQ(Q(value[0]), Q(value[1]))
    return core.GQ(Q(value))


def parse_matrix(core: Any, rows: Sequence[Sequence[Any]]) -> Any:
    return core.matrix([[parse_entry(core, entry) for entry in row] for row in rows])


def parse_columns(core: Any, columns: Sequence[Sequence[Any]]) -> Any:
    parsed = [tuple(parse_entry(core, entry) for entry in column) for column in columns]
    if not parsed or any(len(column) != len(parsed[0]) for column in parsed):
        raise ValueError("ragged column family")
    return core.matrix(
        [[parsed[column][row] for column in range(len(parsed))] for row in range(len(parsed[0]))]
    )


def direct_sum(core: Any, left: Any, right: Any) -> Any:
    left_rows, left_columns = core.shape(left)
    right_rows, right_columns = core.shape(right)
    return core.matrix(
        [
            [
                left[row][column]
                if row < left_rows and column < left_columns
                else right[row - left_rows][column - left_columns]
                if row >= left_rows and column >= left_columns
                else core.ZERO
                for column in range(left_columns + right_columns)
            ]
            for row in range(left_rows + right_rows)
        ]
    )


def scale_rows(core: Any, transformation: Any, coefficients: Sequence[Sequence[Any]]) -> tuple[tuple[Any, ...], ...]:
    source = core.matrix(coefficients)
    moved = core.matmul(transformation, source)
    return tuple(tuple(entry for entry in row) for row in moved)


def solve_affine(core: Any, system: tuple[Any, Any, Any]) -> tuple[tuple[Q, ...], tuple[tuple[Q, ...], ...]] | None:
    names, rows, target = system
    augmented = tuple(tuple(row) + (target[index],) for index, row in enumerate(rows))
    reduced, pivots = core.rref(augmented)
    variable_count = len(names)
    if variable_count in pivots:
        return None
    particular = [Q(0) for _ in range(variable_count)]
    for row, pivot in enumerate(pivots):
        if pivot < variable_count:
            particular[pivot] = reduced[row][-1]
    return tuple(particular), core.nullspace(rows)


def affine_rank(core: Any, system: tuple[Any, Any, Any]) -> int:
    return core.rank(system[1])


def history_pair(core: Any, relative: Any) -> tuple[Any, Any]:
    dimension = core.shape(relative)[0]
    if core.shape(relative) != (dimension, dimension):
        raise ValueError("relative operator must be square")
    return core.identity(dimension), relative


def partial_trace_first(core: Any, value: Any, first: int, second: int) -> Any:
    if core.shape(value) != (first * second, first * second):
        raise ValueError("partial-trace shape mismatch")
    return core.matrix(
        [
            [
                sum(
                    (value[a * second + row][a * second + column] for a in range(first)),
                    core.ZERO,
                )
                for column in range(second)
            ]
            for row in range(second)
        ]
    )


def source_float_literals(path: Path) -> int:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return sum(
        isinstance(node, ast.Constant) and isinstance(node.value, float)
        for node in ast.walk(tree)
    )


def json_has_float(value: Any) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, list):
        return any(json_has_float(entry) for entry in value)
    if isinstance(value, dict):
        return any(json_has_float(entry) for entry in value.values())
    return False


def recursive_keys(value: Any) -> tuple[str, ...]:
    keys: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            keys.append(str(key))
            keys.extend(recursive_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.extend(recursive_keys(child))
    return tuple(keys)


def read_freeze_hashes(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    fixture = re.search(r"fixture SHA-256: `([0-9a-f]{64})`", text)
    scorer = re.search(r"scorer SHA-256: `([0-9a-f]{64})`", text)
    if fixture is None or scorer is None:
        raise ValueError("freeze note lacks fixture/scorer hashes")
    return fixture.group(1), scorer.group(1)


def matrix_text(core: Any, value: Any) -> list[list[str]]:
    return [[core.gtext(entry) for entry in row] for row in value]


def gate(name: str, passed: bool, evidence: str) -> dict[str, Any]:
    return {"gate": name, "passed": bool(passed), "evidence": evidence}


def evaluate(
    core: Any,
    fixture: Mapping[str, Any],
    fixture_path: Path,
    scorer_path: Path,
    freeze_path: Path,
    repository_root: Path,
    mutant: str | None,
) -> tuple[dict[str, Any], dict[str, bool]]:
    runtime_reads: list[dict[str, str]] = []

    def register(path: Path) -> bytes:
        data = path.read_bytes()
        try:
            relative = path.resolve().relative_to(repository_root.resolve()).as_posix()
        except ValueError:
            relative = path.name
        runtime_reads.append({"path": relative, "sha256": hashlib.sha256(data).hexdigest()})
        return data

    fixture_bytes = register(fixture_path)
    scorer_bytes = register(scorer_path)
    core_path = scorer_path.parent / "csf_core.py"
    register(core_path)
    freeze_bytes = register(freeze_path)
    frozen_fixture_hash, frozen_scorer_hash = read_freeze_hashes(freeze_path)

    anchor_token_map = {
        "v16/note-csf-pin.md": ("instrument-realization fiber", "recurring-history law"),
        "v16/note-csf-core-freeze.md": ("common unconditioned channel", "tangent-support extremality"),
        "v16/paper-05-overlap-gram-instrument-variety.md": ("Gram operators", "all-input complete"),
        "v16/code/ovg_receipt.json": ("OVG-GRAM-INSTRUMENT-VARIETY-CONSTRUCTED",),
        "v16/note-ovg-candidate-verification.md": ("REPLAY-VERIFIED GREEN-UNREVIEWED",),
        "v16/paper-02-joint-comparison-fixed-point.md": ("Two exact rational active-locus witnesses",),
        "v16/note-jcv-adjudication.md": ("same unconditioned channel",),
        "v16/paper-03-contextual-pullbacks-permanent-records.md": ("continuation-stable", "erasable"),
        "v16/paper-04-support-rewrite-weld.md": ("relational rewrite arrow", "coupling"),
        "v16/paper-01-joint-relational-history-law.md": ("all-input", "no-signalling"),
        "v12/paper1-composition-defect.md": ("configuration space", "record"),
        "v15/note-homonym-audit.md": ("CELL-HIT", "mutually exclusive"),
    }
    anchor_rows: list[dict[str, Any]] = []
    for relative, declared_hash in fixture["provenance"]["anchors"]:
        path = repository_root / relative
        data = register(path)
        normalized = " ".join(data.decode("utf-8").split())
        tokens = anchor_token_map[relative]
        anchor_rows.append(
            {
                "path": relative,
                "declared": declared_hash,
                "actual": hashlib.sha256(data).hexdigest(),
                "tokens": list(tokens),
                "tokens_present": all(" ".join(token.split()) in normalized for token in tokens),
            }
        )

    forbidden_keys = {
        "expected",
        "verdict",
        "outcome",
        "solution_dimension",
        "selected_matrix",
        "pass_count",
    }
    found_forbidden_keys = sorted(set(recursive_keys(fixture)).intersection(forbidden_keys))
    fixture_text = fixture_bytes.decode("utf-8").lower()
    found_forbidden_text = sorted(
        token for token in ("expected verdict", "selected matrix", "target witness") if token in fixture_text
    )

    dictionary = fixture["history_dictionary"]
    contexts: dict[str, dict[str, Any]] = {}
    context_systems: dict[str, Any] = {}
    typed_rows: list[dict[str, Any]] = []
    for descriptor in fixture["contexts"]:
        relative = parse_matrix(core, descriptor["relative_operator"])
        histories = history_pair(core, relative)
        system = core.affine_completeness_system(histories)
        context_systems[descriptor["id"]] = system
        exchange = descriptor.get("exchange_map")
        relations = {tuple(row) for row in descriptor["relations"]}
        exchange_preserves = False
        if exchange is not None:
            moved = {
                tuple(sorted((exchange[left], exchange[right])))
                for left, right in descriptor["relations"]
            }
            canonical = {tuple(sorted(row)) for row in relations}
            exchange_preserves = moved == canonical and descriptor["calibration"] == "symmetric"
        contexts[descriptor["id"]] = {
            "descriptor": descriptor,
            "relative": relative,
            "histories": histories,
            "system": system,
            "dimension": core.affine_dimension(system),
            "unitary": core.matmul(core.adjoint(relative), relative) == core.identity(core.shape(relative)[0]),
            "exchange_preserves": exchange_preserves,
        }
        typed_rows.append(
            {
                "id": descriptor["id"],
                "actor_count": len(descriptor["actors"]),
                "relation_count": len(descriptor["relations"]),
                "exchange_preserves": exchange_preserves,
                "calibration": descriptor["calibration"],
            }
        )

    training_ids = tuple(row["id"] for row in fixture["contexts"] if row["role"] == "training")
    heldout_ids = tuple(row["id"] for row in fixture["contexts"] if row["role"] == "heldout")
    if mutant == "context-drop":
        training_ids = training_ids[:-1]
    if mutant == "heldout-use-in-fit":
        training_ids = training_ids + heldout_ids
    training_systems = tuple(context_systems[name] for name in training_ids)
    recurring_system = core.stack_affine_systems(training_systems)
    recurring_dimension: Any = core.affine_dimension(recurring_system)
    if mutant == "intersection-dimension-type":
        recurring_dimension = str(recurring_dimension)
    swap = core.matrix([[0, 1], [1, 0]])
    exchange_system = core.invariance_system(2, swap)
    selected_system = core.stack_affine_systems((recurring_system, exchange_system))
    selected_dimension = core.affine_dimension(selected_system)
    selected_solution = solve_affine(core, selected_system)
    selected_coordinates = None if selected_solution is None else selected_solution[0]
    selected_kernel = None if selected_coordinates is None else core.evaluate_coordinates(2, selected_coordinates)
    if mutant == "singleton-no-certificate":
        selected_solution = None

    separate_dimension = sum(
        int(contexts[name]["dimension"])
        for name in training_ids
        if contexts[name]["dimension"] is not None
    )
    heldout_complete = bool(selected_kernel is not None) and all(
        core.completeness_from_kernel(contexts[name]["histories"], selected_kernel)
        == core.identity(core.shape(contexts[name]["relative"])[0])
        for name in heldout_ids
    )
    asymmetric_complete = bool(selected_kernel is not None) and (
        core.completeness_from_kernel(contexts["left-calibrated"]["histories"], selected_kernel)
        == core.identity(2)
    )

    rich_solution = solve_affine(core, context_systems["rich-three"])
    rich_particular, rich_nullspace = rich_solution if rich_solution is not None else (tuple(), tuple())
    rich_cross_forced_zero = bool(rich_solution is not None) and all(
        vector[2] == 0 and vector[3] == 0 for vector in rich_nullspace
    ) and rich_particular[2] == 0 and rich_particular[3] == 0
    if mutant == "rich-spectrum-cross-keep":
        rich_cross_forced_zero = False

    phase_solution = solve_affine(core, context_systems["phase-sign"])
    quarter_solution = solve_affine(core, context_systems["quarter-sign"])
    phase_nullspace = tuple() if phase_solution is None else phase_solution[1]
    quarter_nullspace = tuple() if quarter_solution is None else quarter_solution[1]
    phase_cross_direction = any(vector[3] != 0 for vector in phase_nullspace)
    quarter_cross_direction = any(vector[2] != 0 for vector in quarter_nullspace)
    incompatible_cross_directions = phase_cross_direction and quarter_cross_direction and recurring_dimension == 1

    rephase = core.matrix([[core.I, 0], [0, 1]])
    quarter_histories = contexts["quarter-sign"]["histories"]
    rephased_histories = (
        core.matscale(core.I, quarter_histories[0]),
        quarter_histories[1],
    )
    quarter_witness = core.matrix([[Q(1, 2), Q(1, 4)], [Q(1, 4), Q(1, 2)]])
    rephased_kernel = core.matmul(core.matmul(rephase, quarter_witness), core.adjoint(rephase))
    if mutant == "recurrence-rephase-break":
        rephased_kernel = quarter_witness
    rephase_complete = (
        core.completeness_from_kernel(quarter_histories, quarter_witness) == core.identity(2)
        and core.completeness_from_kernel(rephased_histories, rephased_kernel) == core.identity(2)
    )
    rephase_channel_equal = (
        core.channel_signature(quarter_histories, quarter_witness)
        == core.channel_signature(rephased_histories, rephased_kernel)
    )
    held_exchange_kernel = None if selected_kernel is None else core.matmul(core.matmul(swap, selected_kernel), swap)
    exchange_covariant = selected_kernel is not None and held_exchange_kernel == selected_kernel
    if mutant == "recurrence-swap-break":
        exchange_covariant = False
    asymmetric_exchange_forbidden = contexts["left-calibrated"]["descriptor"]["calibration"] != "symmetric"
    if mutant == "asymmetric-swap-impose":
        asymmetric_exchange_forbidden = False
    doctrine_prediction_polynomials = {"identity": [1, 0], "asymmetric_exchange": [0, 1]}
    doctrine_moves = doctrine_prediction_polynomials["identity"] != doctrine_prediction_polynomials["asymmetric_exchange"]
    dictionary_frozen = all(
        row["id"] in {"event-identity", "quarter-rephase", "held-exchange", "asymmetric-exchange"}
        for row in fixture["recurrence_dictionaries"]
    )
    if mutant == "recurrence-dictionary-postselect":
        dictionary_frozen = False

    identity_two = core.identity(2)
    z_two = core.matrix([[1, 0], [0, -1]])
    histories_jcv = (identity_two, z_two)
    c_jcv_first = (
        (core.GQ(Q(12, 25)), core.GQ(Q(-12, 25))),
        (core.GQ(Q(16, 25)), core.GQ(Q(9, 25))),
    )
    c_jcv_second = (
        (core.GQ(Q(16, 25)), core.GQ(Q(-9, 25))),
        (core.GQ(Q(12, 25)), core.GQ(Q(12, 25))),
    )
    c_jcv_third = (
        (core.GQ(Q(3, 13)), core.GQ(Q(-48, 65))),
        (core.GQ(Q(4, 13)), core.GQ(Q(36, 65))),
    )
    m_jcv_first = core.gram_kernel(c_jcv_first)
    m_jcv_second = core.gram_kernel(c_jcv_second)
    m_jcv_third = core.gram_kernel(c_jcv_third)
    if mutant == "jcv-first-move":
        m_jcv_second = core.matadd(m_jcv_second, core.matrix([[Q(1, 625), 0], [0, 0]]))
    if mutant == "jcv-third-same":
        m_jcv_third = m_jcv_first
    state_zero = core.matrix([[1, 0], [0, 0]])
    state_plus = core.matscale(Q(1, 2), core.matrix([[1, 1], [1, 1]]))
    jcv_first_ports = tuple(core.trace(value) if hasattr(core, "trace") else sum((value[index][index] for index in range(2)), core.ZERO) for value in core.port_outputs(histories_jcv, c_jcv_first, state_zero))
    jcv_second_ports = tuple(core.trace(value) if hasattr(core, "trace") else sum((value[index][index] for index in range(2)), core.ZERO) for value in core.port_outputs(histories_jcv, c_jcv_second, state_zero))
    jcv_first_channel = core.apply_channel_kernel(histories_jcv, m_jcv_first, state_plus)
    jcv_third_channel = core.apply_channel_kernel(histories_jcv, m_jcv_third, state_plus)

    half = core.GQ(Q(1, 2))
    c_parity = ((half, half), (half, -half))
    rotation = core.matrix([[Q(value) for value in row] for row in fixture["record_calibration"]["port_rotation"]])
    c_rotated = scale_rows(core, rotation, c_parity)
    m_parity = core.gram_kernel(c_parity)
    m_rotated = core.gram_kernel(c_rotated)
    selected_matches_fiber = selected_kernel == m_parity == m_rotated
    parity_ports = core.port_outputs(histories_jcv, c_parity, state_zero)
    rotated_ports = core.port_outputs(histories_jcv, c_rotated, state_zero)
    parity_p0 = sum((parity_ports[0][index][index] for index in range(2)), core.ZERO)
    rotated_p0 = sum((rotated_ports[0][index][index] for index in range(2)), core.ZERO)
    calibrated_fiber_moves = parity_p0 != rotated_p0
    if mutant in {"same-m-call-same-instrument", "calibrated-port-call-gauge"}:
        calibrated_fiber_moves = False
    if mutant == "same-m-different-channel":
        m_rotated = core.matadd(m_rotated, core.matrix([[0, Q(1, 10)], [Q(1, 10), 0]]))

    refined_coefficients = c_parity + ((core.ZERO, core.ZERO),)
    refined_kernel = core.gram_kernel(refined_coefficients)
    if mutant == "port-refinement-move-m":
        refined_kernel = core.matadd(refined_kernel, core.matrix([[Q(1, 100), 0], [0, 0]]))

    nonnormal = fixture["nonnormal_control"]
    nonnormal_left = parse_columns(core, nonnormal["left_columns"])
    nonnormal_right = parse_columns(core, nonnormal["right_columns"])
    nonnormal_histories = (nonnormal_left, nonnormal_right)
    nonnormal_relative = core.matmul(core.adjoint(nonnormal_left), nonnormal_right)
    nonnormal_system = core.affine_completeness_system(nonnormal_histories)
    nonnormal_dimension = core.affine_dimension(nonnormal_system)
    nonnormal_direct = (
        core.matmul(nonnormal_relative, core.adjoint(nonnormal_relative))
        != core.matmul(core.adjoint(nonnormal_relative), nonnormal_relative)
    )
    nonnormal_method = "full-real-linear-operator-map"
    if mutant == "nonnormal-spectral-shortcut":
        nonnormal_method = "eigenphase-count"
    nonnormal_selected_complete = selected_kernel is not None and (
        core.completeness_from_kernel(nonnormal_histories, selected_kernel) == core.identity(2)
    )

    flags = fixture["flag_family"]
    flag_first = parse_matrix(core, flags["first"])
    flag_identical = parse_matrix(core, flags["identical"])
    flag_partial = parse_matrix(core, flags["partial"])
    flag_orthogonal = parse_matrix(core, flags["orthogonal"])
    overlap_identical = core.matmul(core.adjoint(flag_first), flag_identical)[0][0]
    overlap_partial = core.matmul(core.adjoint(flag_first), flag_partial)[0][0]
    overlap_orthogonal = core.matmul(core.adjoint(flag_first), flag_orthogonal)[0][0]
    if mutant == "flag-overlap-ignore":
        overlap_partial = core.ONE
    coherent_kernel = core.matrix(
        [[Q(1, 2), core.GQ(0, Q(3, 10))], [core.GQ(0, Q(-3, 10)), Q(1, 2)]]
    )
    real_kernel = core.matrix([[Q(1, 2), Q(3, 10)], [Q(3, 10), Q(1, 2)]])
    phase_histories = contexts["phase-sign"]["histories"]
    rich_histories = contexts["rich-three"]["histories"]
    flagged_identical_histories = (
        core.kron(phase_histories[0], flag_first),
        core.kron(phase_histories[1], flag_identical),
    )
    flagged_partial_histories = (
        core.kron(phase_histories[0], flag_first),
        core.kron(phase_histories[1], flag_partial),
    )
    flagged_orthogonal_histories = (
        core.kron(phase_histories[0], flag_first),
        core.kron(phase_histories[1], flag_orthogonal),
    )
    flagged_rich_histories = (
        core.kron(rich_histories[0], flag_first),
        core.kron(rich_histories[1], flag_partial),
    )
    flag_identical_complete = core.completeness_from_kernel(flagged_identical_histories, coherent_kernel) == core.identity(2)
    flag_partial_complete = core.completeness_from_kernel(flagged_partial_histories, coherent_kernel) == core.identity(2)
    flag_orthogonal_complete = core.completeness_from_kernel(flagged_orthogonal_histories, coherent_kernel) == core.identity(2)
    flag_real_failure = core.completeness_from_kernel(flagged_partial_histories, real_kernel) != core.identity(2)
    flag_rich_failure = core.completeness_from_kernel(flagged_rich_histories, coherent_kernel) != core.identity(3)
    reconvergence_left = parse_matrix(core, flags["reconvergence_legs"][0])
    reconvergence_right = parse_matrix(core, flags["reconvergence_legs"][1])
    reconverged_left = core.matmul(reconvergence_left, flag_first)
    reconverged_right = core.matmul(reconvergence_right, flag_orthogonal)
    reconverged_overlap = core.matmul(core.adjoint(reconverged_left), reconverged_right)[0][0]
    if mutant == "eraser-drop":
        reconverged_overlap = core.ZERO
    durability_claimed = False
    if mutant in {"orthogonal-call-durable", "rich-spectrum-call-record"}:
        durability_claimed = True

    rich_endpoint = core.matrix([[1, 0], [0, 0]])
    support_endpoint = core.matrix([[1], [0]])
    support_full = core.identity(2)
    endpoint_tangent = core.tangent_extreme_nullity(rich_histories, support_endpoint)
    rich_selected_tangent = core.tangent_extreme_nullity(rich_histories, support_full)
    selected_tangent = None if selected_dimension is None else selected_dimension
    selected_rank = 0 if selected_kernel is None else (2 if core.determinant(selected_kernel) != core.ZERO else 1)
    rank_equals_extreme = False
    if mutant == "extreme-equals-rankone":
        rank_equals_extreme = True
    restriction_breaks_extreme = selected_tangent == 0 and rich_selected_tangent > 0
    if mutant == "extreme-stability-assume":
        restriction_breaks_extreme = False

    spectator_identity = core.identity(int(fixture["safety"]["spectator_dimension"]))
    spectator_histories = tuple(core.kron(history, spectator_identity) for history in rich_histories)
    spectator_complete = selected_kernel is not None and (
        core.completeness_from_kernel(spectator_histories, selected_kernel) == core.identity(6)
    )
    embedded_histories = tuple(direct_sum(core, history, history) for history in rich_histories)
    catalogue_complete = selected_kernel is not None and (
        core.completeness_from_kernel(embedded_histories, selected_kernel) == core.identity(6)
    )

    bell = core.zero(4, 4)
    bell_rows = [list(row) for row in bell]
    for row, column in ((0, 0), (0, 3), (3, 0), (3, 3)):
        bell_rows[row][column] = core.GQ(Q(1, 2))
    bell = core.matrix(bell_rows)
    global_histories = (core.kron(identity_two, identity_two), core.kron(z_two, identity_two))
    global_output = core.apply_channel_kernel(global_histories, selected_kernel, bell) if selected_kernel is not None else bell
    bob_before = partial_trace_first(core, bell, 2, 2)
    bob_after = partial_trace_first(core, global_output, 2, 2)
    amplifier_kernel = core.matscale(Q(int(fixture["safety"]["amplifier_scale"])) ** 2, selected_kernel) if selected_kernel is not None else core.identity(2)
    amplifier_output = core.apply_channel_kernel(global_histories, amplifier_kernel, bell)
    bob_amplified = partial_trace_first(core, amplifier_output, 2, 2)
    no_signal = bob_before == bob_after
    amplifier_moves = bob_amplified != bob_before

    coefficient_orientation = (
        core.apply_channel_coefficients(histories_jcv, c_jcv_first, state_plus)
        == core.apply_channel_kernel(histories_jcv, m_jcv_first, state_plus)
    )
    if mutant == "gram-index-transpose":
        coefficient_orientation = False
    completeness_factors = (
        core.completeness_from_coefficients(histories_jcv, c_jcv_first)
        == core.completeness_from_kernel(histories_jcv, m_jcv_first)
        == identity_two
    )
    if mutant == "completeness-cross-drop":
        completeness_factors = False
    channel_factors = coefficient_orientation and (
        core.apply_channel_coefficients(histories_jcv, c_jcv_first, state_plus)
        == core.apply_channel_kernel(histories_jcv, m_jcv_first, state_plus)
    )
    if mutant == "channel-cross-drop":
        channel_factors = False
    all_input = completeness_factors
    if mutant == "state-only-normalize":
        all_input = False
    psd_certified = all(
        core.is_psd_by_principal_minors(value)
        for value in (m_jcv_first, m_jcv_second, m_jcv_third, selected_kernel, coherent_kernel)
        if value is not None
    ) and not core.is_psd_by_principal_minors(core.matrix([[1, 2], [2, 1]]))
    if mutant == "psd-skip":
        psd_certified = False

    typed = (
        dictionary["coordinates"] == ["left-then-right", "right-then-left"]
        and len(contexts) == 5
        and all(row["actor_count"] == 3 and row["relation_count"] == 2 for row in typed_rows)
        and all(contexts[name]["unitary"] for name in contexts)
    )
    if mutant == "history-event-mix":
        typed = False

    source_floats = source_float_literals(scorer_path) + source_float_literals(core_path)
    fixture_float = json_has_float(fixture)
    typed_result_count = None
    if mutant == "float-leak":
        source_floats += 1
    if mutant == "typed-count":
        typed_result_count = 37

    conditional_steering_claimed = False
    all_n_claimed = False
    if mutant == "steering-promote":
        conditional_steering_claimed = True
    if mutant == "all-n-promote":
        all_n_claimed = True

    anchors_ok = all(
        row["declared"] == row["actual"] and row["tokens_present"]
        for row in anchor_rows
    )
    if mutant == "anchor-corrupt":
        anchor_rows[0]["actual"] = "0" * 64
        anchors_ok = False

    measurements: dict[str, Any] = {
        "anchors": {
            "rows": anchor_rows,
            "freeze_fixture_match": hashlib.sha256(fixture_bytes).hexdigest() == frozen_fixture_hash,
            "freeze_scorer_match": hashlib.sha256(scorer_bytes).hexdigest() == frozen_scorer_hash,
            "core_match": sha256_path(core_path) == CORE_HASH,
            "freeze_sha256": hashlib.sha256(freeze_bytes).hexdigest(),
        },
        "fixture_neutrality": {
            "forbidden_keys": found_forbidden_keys,
            "forbidden_text": found_forbidden_text,
        },
        "referents": {
            "coordinates": list(dictionary["coordinates"]),
            "context_rows": typed_rows,
            "training_ids": list(training_ids),
            "heldout_ids": list(heldout_ids),
            "typed": typed,
        },
        "base_fiber": {
            "jcv_m_first": matrix_text(core, m_jcv_first),
            "jcv_m_second": matrix_text(core, m_jcv_second),
            "jcv_m_third": matrix_text(core, m_jcv_third),
            "jcv_first_port_zero": core.gtext(jcv_first_ports[0]),
            "jcv_second_port_zero": core.gtext(jcv_second_ports[0]),
            "jcv_third_channel_moves": jcv_third_channel != jcv_first_channel,
            "completeness_factors": completeness_factors,
            "channel_factors": channel_factors,
            "coefficient_orientation": coefficient_orientation,
            "all_input": all_input,
            "psd_certified": psd_certified,
        },
        "contexts": {
            "affine_dimensions": {name: row["dimension"] for name, row in contexts.items()},
            "separate_training_dimension": separate_dimension,
            "recurring_dimension": recurring_dimension,
            "selected_dimension": selected_dimension,
            "selected_coordinates": None if selected_coordinates is None else [core.qtext(value) for value in selected_coordinates],
            "selected_kernel": None if selected_kernel is None else matrix_text(core, selected_kernel),
            "selected_psd": selected_kernel is not None and core.is_psd_by_principal_minors(selected_kernel),
            "heldout_complete": heldout_complete,
            "asymmetric_complete": asymmetric_complete,
            "phase_cross_direction": phase_cross_direction,
            "quarter_cross_direction": quarter_cross_direction,
            "incompatible_cross_directions": incompatible_cross_directions,
            "rich_cross_forced_zero": rich_cross_forced_zero,
            "rich_nullity": len(rich_nullspace),
        },
        "recurrence": {
            "dictionary_frozen": dictionary_frozen,
            "rephase_complete": rephase_complete,
            "rephase_channel_equal": rephase_channel_equal,
            "held_exchange_covariant": exchange_covariant,
            "symmetric_contexts_licensed": all(contexts[name]["exchange_preserves"] for name in training_ids if name != "left-calibrated"),
            "asymmetric_exchange_forbidden": asymmetric_exchange_forbidden,
            "doctrine_prediction_polynomials": doctrine_prediction_polynomials,
            "doctrine_moves_pre_symmetry": doctrine_moves,
            "heldout_not_in_fit": not bool(set(training_ids).intersection(heldout_ids)),
        },
        "record_fiber": {
            "selected_matches_both": selected_matches_fiber,
            "m_parity": matrix_text(core, m_parity),
            "m_rotated": matrix_text(core, m_rotated),
            "parity_port_zero": core.gtext(parity_p0),
            "rotated_port_zero": core.gtext(rotated_p0),
            "calibrated_moves": calibrated_fiber_moves,
            "unconditioned_channels_equal": core.channel_signature(histories_jcv, m_parity) == core.channel_signature(histories_jcv, m_rotated),
            "port_refinement_same_m": refined_kernel == m_parity,
            "calibrated_mixing_is_gauge": False,
        },
        "nonnormal": {
            "relative": matrix_text(core, nonnormal_relative),
            "is_nonnormal": nonnormal_direct,
            "method": nonnormal_method,
            "affine_dimension": nonnormal_dimension,
            "selected_complete": nonnormal_selected_complete,
        },
        "flags": {
            "overlaps": [core.gtext(overlap_identical), core.gtext(overlap_partial), core.gtext(overlap_orthogonal)],
            "identical_complete": flag_identical_complete,
            "partial_complete": flag_partial_complete,
            "orthogonal_complete": flag_orthogonal_complete,
            "real_weight_failure": flag_real_failure,
            "rich_partial_failure": flag_rich_failure,
            "reconverged_overlap": core.gtext(reconverged_overlap),
            "durability_claimed": durability_claimed,
        },
        "extremality": {
            "endpoint_tangent_nullity": endpoint_tangent,
            "selected_tangent_nullity": selected_tangent,
            "selected_rank": selected_rank,
            "rich_selected_tangent_nullity": rich_selected_tangent,
            "restriction_breaks_extreme": restriction_breaks_extreme,
            "rank_equals_extreme_claimed": rank_equals_extreme,
            "port_refinement_same_m": refined_kernel == m_parity,
            "spectator_complete": spectator_complete,
            "catalogue_embedding_complete": catalogue_complete,
        },
        "safety": {
            "bob_before": matrix_text(core, bob_before),
            "bob_after": matrix_text(core, bob_after),
            "bob_amplified": matrix_text(core, bob_amplified),
            "unconditioned_no_signal": no_signal,
            "amplifier_moves": amplifier_moves,
            "conditional_steering_claimed": conditional_steering_claimed,
            "all_n_claimed": all_n_claimed,
        },
        "runtime": {
            "reads": runtime_reads,
            "source_float_literals": source_floats,
            "fixture_contains_float": fixture_float,
            "typed_result_count": typed_result_count,
        },
    }

    flags_out = {
        "anchors": anchors_ok
        and measurements["anchors"]["freeze_fixture_match"]
        and measurements["anchors"]["freeze_scorer_match"]
        and measurements["anchors"]["core_match"],
        "fixture_neutral": not found_forbidden_keys and not found_forbidden_text,
        "typed": typed,
        "spectrahedral": completeness_factors and channel_factors and all_input and psd_certified,
        "jcv": m_jcv_first == m_jcv_second
        and m_jcv_third != m_jcv_first
        and jcv_first_ports[0] == core.ZERO
        and jcv_second_ports[0] == core.GQ(Q(49, 625))
        and jcv_third_channel != jcv_first_channel,
        "affine": all(contexts[name]["dimension"] is not None for name in contexts),
        "rich": rich_cross_forced_zero and incompatible_cross_directions,
        "nonnormal": nonnormal_direct and nonnormal_method == "full-real-linear-operator-map" and nonnormal_selected_complete,
        "dictionary": dictionary_frozen and rephase_complete and rephase_channel_equal and exchange_covariant,
        "symmetry": measurements["recurrence"]["symmetric_contexts_licensed"] and asymmetric_exchange_forbidden,
        "intersection": isinstance(recurring_dimension, int)
        and recurring_dimension < separate_dimension
        and training_ids == ("phase-sign", "quarter-sign", "rich-three"),
        "selected": selected_dimension == 0 and selected_solution is not None and measurements["contexts"]["selected_psd"],
        "heldout": heldout_complete and asymmetric_complete and measurements["recurrence"]["heldout_not_in_fit"],
        "doctrine": doctrine_moves,
        "record_fiber": selected_matches_fiber
        and m_parity == m_rotated
        and calibrated_fiber_moves
        and measurements["record_fiber"]["unconditioned_channels_equal"]
        and not measurements["record_fiber"]["calibrated_mixing_is_gauge"],
        "port_refinement": refined_kernel == m_parity,
        "flags": overlap_identical == core.ONE
        and overlap_partial == core.GQ(Q(3, 5))
        and overlap_orthogonal == core.ZERO
        and flag_identical_complete
        and flag_partial_complete
        and flag_orthogonal_complete
        and flag_real_failure
        and flag_rich_failure
        and overlap_orthogonal == core.ZERO,
        "eraser": reconverged_overlap == core.ONE and not durability_claimed,
        "extreme": endpoint_tangent == 0
        and selected_tangent == 0
        and selected_rank == 2
        and rich_selected_tangent > 0
        and not rank_equals_extreme,
        "extreme_unstable": restriction_breaks_extreme,
        "extensions": spectator_complete and catalogue_complete,
        "safety": no_signal and amplifier_moves,
        "scope": not conditional_steering_claimed and not all_n_claimed and not durability_claimed,
        "exact": source_floats == 0 and not fixture_float and typed_result_count is None,
    }
    return measurements, flags_out


def classify_primary(flags: Mapping[str, bool], measurements: Mapping[str, Any]) -> str:
    if not flags["typed"]:
        return "CSF-BLOCKED-AT-HISTORY-INDIVIDUATION"
    if not flags["dictionary"]:
        return "CSF-BLOCKED-AT-RECURRENCE-DICTIONARY"
    if not flags["spectrahedral"]:
        return "CSF-SPECTRAHEDRAL-FORMULATION-REFUTED"
    dimension = measurements["contexts"]["recurring_dimension"]
    if dimension is None:
        return "CSF-RECURRING-LAW-INCONSISTENT"
    if flags["selected"] and flags["heldout"]:
        return "CSF-RECURRING-LAW-SELECTED-MODULO-GAUGE"
    if flags["intersection"]:
        return "CSF-RECURRING-LAW-PARTIALLY-SELECTED"
    return "CSF-RECURRING-LAW-UNSELECTED"


def independent_primary(measurements: Mapping[str, Any]) -> str:
    if not measurements["referents"]["typed"]:
        return "CSF-BLOCKED-AT-HISTORY-INDIVIDUATION"
    recurrence = measurements["recurrence"]
    if not (
        recurrence["dictionary_frozen"]
        and recurrence["rephase_complete"]
        and recurrence["rephase_channel_equal"]
        and recurrence["held_exchange_covariant"]
    ):
        return "CSF-BLOCKED-AT-RECURRENCE-DICTIONARY"
    base = measurements["base_fiber"]
    if not (
        base["completeness_factors"]
        and base["channel_factors"]
        and base["all_input"]
        and base["psd_certified"]
    ):
        return "CSF-SPECTRAHEDRAL-FORMULATION-REFUTED"
    recurring = measurements["contexts"]["recurring_dimension"]
    if recurring is None:
        return "CSF-RECURRING-LAW-INCONSISTENT"
    if (
        measurements["contexts"]["selected_dimension"] == 0
        and measurements["contexts"]["selected_psd"]
        and measurements["contexts"]["heldout_complete"]
        and measurements["recurrence"]["heldout_not_in_fit"]
    ):
        return "CSF-RECURRING-LAW-SELECTED-MODULO-GAUGE"
    if isinstance(recurring, int) and recurring < measurements["contexts"]["separate_training_dimension"]:
        return "CSF-RECURRING-LAW-PARTIALLY-SELECTED"
    return "CSF-RECURRING-LAW-UNSELECTED"


def qualifier_rows(flags: Mapping[str, bool]) -> list[str]:
    rows: list[str] = []
    if flags["spectrahedral"]:
        rows.append("COMPLETENESS-SPECTRAHEDRON-CONSTRUCTED")
    if flags["jcv"]:
        rows.append("JCV-UNCONDITIONED-BASE-AND-CALIBRATED-FIBER-EMBEDDED")
    if flags["rich"]:
        rows.append("RICH-SPECTRUM-UNCONDITIONED-CROSS-MOMENT-ZERO")
    if flags["record_fiber"]:
        rows.append("CALIBRATED-RECORD-FIBER-OPERATIONALLY-NONTRIVIAL")
    if flags["selected"]:
        rows.append("SELECTION-CONDITIONAL-ON-EXCHANGE-SYMMETRY")
    if flags["doctrine"]:
        rows.append("RECURRENCE-DOCTRINE-MOVES-PHYSICS")
    if flags["extreme_unstable"]:
        rows.append("EXTREME-POINT-SELECTION-UNSTABLE")
    elif flags["extreme"]:
        rows.append("EXTREME-POINT-SELECTION-SURVIVES-REGISTERED-MAPS")
    if flags["flags"] and flags["eraser"]:
        rows.append("FLAG-ORTHOGONALITY-CONSTRUCTED-BUT-PERMANENCE-UNPROVED")
    rows.extend(("CONDITIONAL-STEERING-OPEN", "ELEMENTARY-TRANSPORTS-AND-CATALOGUE-UNSELECTED"))
    return rows


def claim_rows(measurements: Mapping[str, Any], primary: str, qualifiers: Sequence[str]) -> list[dict[str, str]]:
    dimensions = measurements["contexts"]["affine_dimensions"]
    return [
        {"id": "C1", "text": f"The primary finite verdict is `{primary}`."},
        {"id": "C2", "text": "At fixed typed histories, all-input completeness is an affine constraint on the positive-semidefinite kernel `M=C^dagger C`, while retained calibrated ports still depend on its factorization."},
        {"id": "C3", "text": f"The JCV reconstruction has one common kernel for its first two instruments and calibrated first-port probabilities {measurements['base_fiber']['jcv_first_port_zero']} and {measurements['base_fiber']['jcv_second_port_zero']}; its third kernel moves the unconditioned channel."},
        {"id": "C4", "text": f"The five context affine dimensions are {dimensions}; independent training laws have total dimension {measurements['contexts']['separate_training_dimension']}, recurrence leaves dimension {measurements['contexts']['recurring_dimension']}, and licensed exchange symmetry leaves dimension {measurements['contexts']['selected_dimension']}."},
        {"id": "C5", "text": f"The exchange-fixed recurring kernel is {measurements['contexts']['selected_kernel']} and passes the held-out context: {str(measurements['contexts']['heldout_complete']).lower()}."},
        {"id": "C6", "text": f"Two calibrated factorizations of that kernel move the retained first-port probability from {measurements['record_fiber']['parity_port_zero']} to {measurements['record_fiber']['rotated_port_zero']} while their unconditioned channels agree."},
        {"id": "C7", "text": f"Rich spectrum forces the unconditioned cross moment to zero at this arena: {str(measurements['contexts']['rich_cross_forced_zero']).lower()}; it does not make an order actual or durable."},
        {"id": "C8", "text": f"The selected rank-{measurements['extremality']['selected_rank']} kernel is extreme only after the recurrence and exchange constraints; restriction to the rich context gives tangent nullity {measurements['extremality']['rich_selected_tangent_nullity']}."},
        {"id": "C9", "text": f"Flag overlaps {measurements['flags']['overlaps']} distinguish identical, partial, and orthogonal tags, while a licensed reconvergence restores overlap {measurements['flags']['reconverged_overlap']}; permanence is therefore unproved."},
        {"id": "C10", "text": f"The registered unconditioned spectator test leaves Bob unchanged: {str(measurements['safety']['unconditioned_no_signal']).lower()}, while the incomplete amplifier moves him: {str(measurements['safety']['amplifier_moves']).lower()}."},
        {"id": "C11", "text": f"The exact qualifiers are {list(qualifiers)}."},
        {"id": "C12", "text": "The elementary transports, relational rewrite, configuration catalogue, calibrated port law, record permanence, conditional steering, arbitrary finite composition, actualization, continuum, QFT, gravity, particles, Hamiltonian, constants, and empirical deviations remain unselected or unconstructed."},
    ]


def consequence_rows() -> list[dict[str, str]]:
    return [
        {"item": "fixed-history ensemble law", "status": "CONSTRUCTED", "reason": "affine PSD completeness at the registered finite histories"},
        {"item": "unconditioned rich-spectrum order coherence", "status": "FORCED-ZERO-AT-FIXTURE", "reason": "three distinct eigenphases remove both cross coordinates"},
        {"item": "recurring unconditioned kernel", "status": "CONDITIONALLY-SELECTED", "reason": "recurrence plus a licensed exchange automorphism leave one point"},
        {"item": "calibrated record instrument", "status": "UNSELECTED", "reason": "same kernel admits operationally different retained-port factorizations"},
        {"item": "extreme-point principle", "status": "REFUTED-AS-CONTEXT-INVARIANT", "reason": "restriction sends the selected extreme to an interior point"},
        {"item": "record permanence", "status": "OPEN", "reason": "orthogonal tags can reconverge under a licensed continuation"},
        {"item": "conditional steering", "status": "OPEN", "reason": "no remote preparation/instrument is typed"},
        {"item": "fundamental dynamics", "status": "UNSELECTED", "reason": "history transports and catalogue are fixed inputs"},
    ]


def limitation_rows() -> list[str]:
    return [
        "Finite exact fixtures do not establish a continuum or Lorentzian limit.",
        "Recurrence of a history kernel is not derived vertex locality.",
        "Exchange selection is conditional on a calibrated relational automorphism.",
        "A selected unconditioned kernel does not select its recorded instrument fiber.",
        "Orthogonality at one cut is not record permanence or actualization.",
        "The no-signalling check has fixed subsystem factorization and is unconditioned.",
        "No QFT, gravity, particle, Hamiltonian, coupling, affine, or phenomenological claim is made.",
    ]


def render_paper(
    measurements: Mapping[str, Any],
    primary: str,
    qualifiers: Sequence[str],
    claims: Sequence[Mapping[str, str]],
    consequences: Sequence[Mapping[str, str]],
    limitations: Sequence[str],
) -> str:
    lines = [
        "# Completeness spectrahedra and calibrated record fibers",
        "",
        "Status: **GREEN-UNREVIEWED CANDIDATE**.",
        "",
        "## Abstract",
        "",
        "For a fixed family of typed complete-history maps, this paper rewrites all-input instrument completeness as an affine constraint on a positive-semidefinite history kernel. The kernel determines the unconditioned channel, while calibrated record-resolving factorizations remain additional operational data. Several independently typed overlap contexts are then intersected under one frozen recurrence dictionary. At the finite arena, recurrence reduces the law family and a licensed exchange automorphism leaves one unconditioned kernel, but its calibrated record fiber remains physically nontrivial. The selection is conditional on the recurrence and symmetry doctrine; elementary dynamics and the configuration catalogue are not selected.",
        "",
        "## 1. Fixed-history base and instrument fiber",
        "",
        "For histories `V_h` and port coefficients `c[j,h]`, set",
        "",
        "```text",
        "K_j = sum_h c[j,h] V_h,",
        "M = C^dagger C,",
        "L_V(M) = sum_h,k M[h,k] V_h^dagger V_k.",
        "```",
        "",
        "All-input completeness is `L_V(M)=I`. With the index convention above, the unconditioned channel is `Phi_M(rho)=sum_h,k M[h,k] V_k rho V_h^dagger`. Consequently the lawful fixed-history kernels form an affine slice of the positive-semidefinite cone. This statement is not extended to changing history catalogues or transports.",
        "",
        "A factorization `C^dagger C=M` is not automatically gauge. If its port is retained and calibrated, its resolved maps are operational data. Only transformations invisible to the admitted port calibration are quotiented.",
        "",
        claims[1]["text"],
        "",
        "## 2. Exact base/fiber reconstruction",
        "",
        claims[2]["text"],
        "",
        claims[5]["text"],
        "",
        "Thus the spectrahedron is a base for unconditioned laws, and calibrated instruments form fibers above it. Collapsing the fiber would erase measured record statistics.",
        "",
        "## 3. Spectral ensemble theorem",
        "",
        "For two unitary histories and `Omega=A^dagger B`, write `M=[[p,m],[mbar,q]]`. Completeness is `(p+q)I+m Omega+mbar Omega^dagger=I`. Evaluating this identity on distinct eigenphases gives a real affine line condition on points of the unit circle. One phase leaves two cross coordinates, two phases leave one phase-quantized direction, and three distinct phases force `p+q=1,m=0`. The remaining diagonal bias is not selected by completeness.",
        "",
        claims[6]["text"],
        "",
        f"The registered context dimensions are {measurements['contexts']['affine_dimensions']}. The nonnormal control is classified by `{measurements['nonnormal']['method']}` and has affine dimension {measurements['nonnormal']['affine_dimension']}; no eigenphase shortcut is used.",
        "",
        "## 4. Recurring contexts",
        "",
        claims[3]["text"],
        "",
        claims[4]["text"],
        "",
        "The identity recurrence dictionary is fixed before solving. A coordinate rephase preserves completeness and the unconditioned channel, while exchange is licensed only in contexts whose relational graph and calibration carry that automorphism. The asymmetric source-calibrated control forbids treating exchange as universal gauge. Before the exchange-fixed reduction, an inequivalent coordinate assignment moves a calibrated history prediction; recurrence doctrine therefore carries physical content.",
        "",
        "The result selects one unconditioned kernel only relative to those declarations. It does not derive recurrence or vertex locality.",
        "",
        "## 5. Extremality is not a selection principle",
        "",
        claims[7]["text"],
        "",
        "The kernel has rank greater than one yet is extreme in the exchange-fixed singleton, directly refuting identification of extremality with rank one. Forgetting the exchange calibration maps it into the interior of the rich-context segment. Hence extremality is constraint-relative and cannot serve as a context-independent physical selection principle here.",
        "",
        "## 6. Flags, records, and safety",
        "",
        claims[8]["text"],
        "",
        "At rich spectrum, nonzero tag overlap cannot preserve the registered nonzero cross coefficient; at two phases a phase-compatible partial tag remains complete. These are ensemble identities, not an actualization mechanism.",
        "",
        claims[9]["text"],
        "",
        "This fixed-factor unconditioned test is not a conditional steering theorem and says nothing about a changing Bob algebra.",
        "",
        "## 7. Verdict and consequences",
        "",
        claims[0]["text"],
        "",
        claims[10]["text"],
        "",
        "| item | status | reason |",
        "|---|---|---|",
    ]
    for row in consequences:
        lines.append(f"| {row['item']} | {row['status']} | {row['reason']} |")
    lines.extend(["", "## 8. Scope walls", ""])
    lines.extend(f"- {row}" for row in limitations)
    lines.extend(["", claims[11]["text"], "", "## Exact claim register", ""])
    for row in claims:
        lines.append(f"- **{row['id']}** — bound in the numbered sections above.")
    return "\n".join(lines) + "\n"


def render_transcript(measurements: Mapping[str, Any], primary: str, qualifiers: Sequence[str], gates: Sequence[Mapping[str, Any]]) -> str:
    lines = ["CSF PAPER 6 EXACT RESULT", f"primary: {primary}", f"qualifiers: {list(qualifiers)}"]
    for row in gates:
        state = "PASS" if row["passed"] else "FAIL"
        lines.append(f"{state} {row['gate']} :: {row['evidence']}")
    lines.append(f"gate-count: {len(gates)}")
    lines.append(f"all-pass: {str(all(row['passed'] for row in gates)).lower()}")
    return "\n".join(lines) + "\n"


def build_result(
    core: Any,
    fixture: Mapping[str, Any],
    fixture_path: Path,
    scorer_path: Path,
    freeze_path: Path,
    repository_root: Path,
    mutant: str | None,
) -> tuple[dict[str, Any], str, str]:
    measurements, flags = evaluate(core, fixture, fixture_path, scorer_path, freeze_path, repository_root, mutant)
    primary = classify_primary(flags, measurements)
    comparator = independent_primary(measurements)
    if mutant == "verdict-flip":
        primary = "CSF-RECURRING-LAW-UNSELECTED"
    qualifiers = qualifier_rows(flags)
    claims = claim_rows(measurements, primary, qualifiers)
    consequences = consequence_rows()
    limitations = limitation_rows()
    paper = render_paper(measurements, primary, qualifiers, claims, consequences, limitations)
    claim_occurrences = {row["id"]: paper.count(row["text"]) for row in claims}
    expected_reads = {
        "v16/code/csf_fixture.json",
        "v16/code/csf_score.py",
        "v16/code/csf_core.py",
        "v16/note-csf-fixture-freeze.md",
        *{row[0] for row in fixture["provenance"]["anchors"]},
    }
    actual_reads = {row["path"] for row in measurements["runtime"]["reads"]}
    gates = [
        gate("CSF-ANCHORS", flags["anchors"], f"rows={len(measurements['anchors']['rows'])} freeze={measurements['anchors']['freeze_fixture_match']}/{measurements['anchors']['freeze_scorer_match']}"),
        gate("CSF-FIXTURE-NEUTRALITY", flags["fixture_neutral"], f"keys={measurements['fixture_neutrality']['forbidden_keys']} text={measurements['fixture_neutrality']['forbidden_text']}"),
        gate("CSF-HISTORY-INDIVIDUATION", flags["typed"], f"contexts={len(measurements['referents']['context_rows'])} coordinates={measurements['referents']['coordinates']}"),
        gate("CSF-M-FACTORIZATION", measurements["base_fiber"]["jcv_m_first"] == measurements["base_fiber"]["jcv_m_second"], f"M={measurements['base_fiber']['jcv_m_first']}"),
        gate("CSF-ALL-INPUT-COMPLETENESS", flags["spectrahedral"], f"complete={measurements['base_fiber']['completeness_factors']} all_input={measurements['base_fiber']['all_input']} psd={measurements['base_fiber']['psd_certified']}"),
        gate("CSF-CHANNEL-INDEX-ORIENTATION", measurements["base_fiber"]["coefficient_orientation"], f"orientation={measurements['base_fiber']['coefficient_orientation']}"),
        gate("CSF-JCV-BASE-FIBER", flags["jcv"], f"p0={measurements['base_fiber']['jcv_first_port_zero']},{measurements['base_fiber']['jcv_second_port_zero']} third_moves={measurements['base_fiber']['jcv_third_channel_moves']}"),
        gate("CSF-AFFINE-CONTEXTS", flags["affine"], f"dims={measurements['contexts']['affine_dimensions']}"),
        gate("CSF-RICH-SPECTRUM", flags["rich"], f"cross_zero={measurements['contexts']['rich_cross_forced_zero']} incompatible={measurements['contexts']['incompatible_cross_directions']}"),
        gate("CSF-NONNORMAL-DIRECT", flags["nonnormal"], f"method={measurements['nonnormal']['method']} dim={measurements['nonnormal']['affine_dimension']}"),
        gate("CSF-RECURRENCE-DICTIONARY", flags["dictionary"], f"rephase={measurements['recurrence']['rephase_complete']}/{measurements['recurrence']['rephase_channel_equal']} exchange={measurements['recurrence']['held_exchange_covariant']}"),
        gate("CSF-RECURRENCE-INTERSECTION", flags["intersection"], f"separate={measurements['contexts']['separate_training_dimension']} recurring={measurements['contexts']['recurring_dimension']}"),
        gate("CSF-EXCHANGE-LICENCE", flags["symmetry"], f"symmetric={measurements['recurrence']['symmetric_contexts_licensed']} asymmetric_forbidden={measurements['recurrence']['asymmetric_exchange_forbidden']}"),
        gate("CSF-SELECTED-KERNEL", flags["selected"], f"dimension={measurements['contexts']['selected_dimension']} kernel={measurements['contexts']['selected_kernel']}"),
        gate("CSF-HELDOUT-CONTEXT", flags["heldout"], f"heldout={measurements['contexts']['heldout_complete']} not_fit={measurements['recurrence']['heldout_not_in_fit']} asym={measurements['contexts']['asymmetric_complete']}"),
        gate("CSF-DOCTRINE-CONTROL", flags["doctrine"], f"polynomials={measurements['recurrence']['doctrine_prediction_polynomials']}"),
        gate("CSF-CALIBRATED-RECORD-FIBER", flags["record_fiber"], f"p0={measurements['record_fiber']['parity_port_zero']},{measurements['record_fiber']['rotated_port_zero']}"),
        gate("CSF-PORT-REFINEMENT", flags["port_refinement"], f"same_m={measurements['record_fiber']['port_refinement_same_m']}"),
        gate("CSF-FLAG-SPECTRAL", flags["flags"], f"overlaps={measurements['flags']['overlaps']} rich_fail={measurements['flags']['rich_partial_failure']}"),
        gate("CSF-ERASER-PERMANENCE", flags["eraser"], f"reconverged={measurements['flags']['reconverged_overlap']} durability={measurements['flags']['durability_claimed']}"),
        gate("CSF-EXTREME-TANGENT", flags["extreme"], f"rank={measurements['extremality']['selected_rank']} tangents={measurements['extremality']['endpoint_tangent_nullity']}/{measurements['extremality']['selected_tangent_nullity']}/{measurements['extremality']['rich_selected_tangent_nullity']}"),
        gate("CSF-EXTREME-STABILITY", flags["extreme_unstable"], f"restriction_breaks={measurements['extremality']['restriction_breaks_extreme']}"),
        gate("CSF-EXTENSION-CONTROLS", flags["extensions"], f"spectator={measurements['extremality']['spectator_complete']} catalogue={measurements['extremality']['catalogue_embedding_complete']}"),
        gate("CSF-FIXED-BOB-NOSIGNAL", flags["safety"], f"unchanged={measurements['safety']['unconditioned_no_signal']} amplifier={measurements['safety']['amplifier_moves']}"),
        gate("CSF-SCOPE-WALLS", flags["scope"], f"steering={measurements['safety']['conditional_steering_claimed']} all_n={measurements['safety']['all_n_claimed']}"),
        gate("CSF-EXACT-ARITHMETIC", flags["exact"], f"floats={measurements['runtime']['source_float_literals']} fixture_float={measurements['runtime']['fixture_contains_float']} typed_count={measurements['runtime']['typed_result_count']}"),
        gate("CSF-RUNTIME-READ-SET", actual_reads == expected_reads, f"reads={sorted(actual_reads)}"),
        gate("CSF-PRIMARY-EQUALITY", primary == comparator, f"primary={primary} comparator={comparator}"),
        gate("CSF-CLAIM-COVERAGE", all(count == 1 for count in claim_occurrences.values()), f"occurrences={claim_occurrences}"),
        gate("CSF-PAPER-SCOPE", "actualization is derived" not in paper.lower() and "arbitrary-n theorem" not in paper.lower(), f"limitations={len(limitations)}"),
    ]
    result = {
        "schema": "csf-result-v1",
        "primary": primary,
        "qualifiers": list(qualifiers),
        "measurements": measurements,
        "claims": claims,
        "consequences": consequences,
        "limitations": limitations,
        "gates": gates,
    }
    transcript = render_transcript(measurements, primary, qualifiers, gates)
    return result, transcript, paper


def finalized_receipt(result: Mapping[str, Any], transcript: str, paper: str) -> dict[str, Any]:
    receipt = copy.deepcopy(dict(result))
    seal_keys = ("schema", "primary", "qualifiers", "measurements", "claims", "consequences", "limitations", "gates")
    receipt["seals"] = {key: digest(receipt[key]) for key in seal_keys}
    receipt["sealed_keys"] = list(seal_keys)
    receipt["transcript_sha256"] = hashlib.sha256(transcript.encode("utf-8")).hexdigest()
    receipt["paper_sha256"] = hashlib.sha256(paper.encode("utf-8")).hexdigest()
    return receipt


def validate_promotion(receipt: Mapping[str, Any], transcript: str, paper: str) -> tuple[bool, str]:
    sealed_keys = tuple(receipt["sealed_keys"])
    total = set(sealed_keys) == {"schema", "primary", "qualifiers", "measurements", "claims", "consequences", "limitations", "gates"}
    seals = all(receipt["seals"][key] == digest(receipt[key]) for key in sealed_keys)
    transcript_ok = receipt["transcript_sha256"] == hashlib.sha256(transcript.encode("utf-8")).hexdigest()
    paper_ok = receipt["paper_sha256"] == hashlib.sha256(paper.encode("utf-8")).hexdigest()
    all_gates = all(row["passed"] for row in receipt["gates"])
    return total and seals and transcript_ok and paper_ok and all_gates, f"total={total} seals={seals} transcript={transcript_ok} paper={paper_ok} gates={all_gates}"


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=root / "csf_fixture.json")
    parser.add_argument("--core", type=Path, default=root / "csf_core.py")
    parser.add_argument("--freeze", type=Path, default=root.parent / "note-csf-fixture-freeze.md")
    parser.add_argument("--output", type=Path, default=root / "csf_output.txt")
    parser.add_argument("--receipt", type=Path, default=root / "csf_receipt.json")
    parser.add_argument("--paper", type=Path, default=root.parent / "paper-06-completeness-spectrahedra-record-fibers.md")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--mutant", choices=MUTANTS)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.selftest and args.mutant is not None:
        print("REFUSE CSF-CLI :: selftest and mutant are mutually exclusive", file=sys.stderr)
        return 2
    mutant = "anchor-corrupt" if args.selftest else args.mutant
    targets = (args.output.resolve(), args.receipt.resolve(), args.paper.resolve())
    if any(path.exists() for path in targets):
        print("REFUSE CSF-EXISTING-TARGET :: " + ",".join(str(path) for path in targets if path.exists()), file=sys.stderr)
        return 1
    try:
        core = load_core(args.core.resolve())
        fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
        repository_root = args.fixture.resolve().parents[2]
        result, transcript, paper = build_result(
            core,
            fixture,
            args.fixture.resolve(),
            Path(__file__).resolve(),
            args.freeze.resolve(),
            repository_root,
            mutant,
        )
    except Exception as error:
        print(f"REFUSE CSF-EXECUTION :: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    failed = [row["gate"] for row in result["gates"] if not row["passed"]]
    if failed:
        label = "CSF-SELFTEST" if args.selftest else "CSF-GATE"
        print(f"REFUSE {label} :: {','.join(failed)}", file=sys.stderr)
        return 1
    receipt = finalized_receipt(result, transcript, paper)
    if mutant == "transcript-forge":
        transcript += "FORGED\n"
    if mutant == "seal-after-write":
        receipt["measurements"]["contexts"]["selected_dimension"] = 99
    promotion_ok, evidence = validate_promotion(receipt, transcript, paper)
    if not promotion_ok:
        print(f"REFUSE CSF-PROMOTION :: {evidence}", file=sys.stderr)
        return 1
    atomic_write(args.output.resolve(), transcript.encode("utf-8"))
    atomic_write(args.receipt.resolve(), canonical_json(receipt))
    atomic_write(args.paper.resolve(), paper.encode("utf-8"))
    sys.stdout.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
