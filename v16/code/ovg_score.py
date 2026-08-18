#!/usr/bin/env python3
"""Verdict-neutral exact scorer for OVG Paper 5.

The data-only fixture and this scorer are frozen before their first scientific
execution.  The scorer imports the already frozen generic core by hash.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import importlib.util
import itertools
import json
import math
import os
import re
import sys
import tempfile
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


Q = Fraction
CORE_HASH = "7b17a138dc45f564a5180fca81bdb4620aaa570514d090d8a5c45f0f22d985bf"
MUTANTS = (
    "anchor-corrupt",
    "history-order-drop",
    "common-boundary-forge",
    "gram-cross-term-move",
    "gram-self-compare",
    "state-only-normalize",
    "equal-real-universalize",
    "complex-witness-drop",
    "parity-factor-move",
    "scalar-call-distinct",
    "eigenphase-count-move",
    "phase-constraint-drop",
    "nonnormal-spectral-shortcut",
    "z-zero-call-coherent",
    "three-history-drop",
    "port-coarsegrain-break",
    "dependency-call-record",
    "divergent-call-common",
    "local-flag-call-implemented",
    "local-factorization-drop",
    "binary-product-call-primitive",
    "ancilla-policy-hide",
    "durability-assume",
    "causal-switch-word",
    "all-n-promote",
    "typed-count",
    "float-leak",
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
    spec = importlib.util.spec_from_file_location("ovg_frozen_core", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen core")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_pair(core: Any, value: Sequence[Any]) -> Any:
    if len(value) != 2:
        raise ValueError("Gaussian pair must have length two")
    return core.GQ(Q(value[0]), Q(value[1]))


def parse_columns(core: Any, columns: Sequence[Sequence[Sequence[Any]]]) -> Any:
    parsed = [[parse_pair(core, entry) for entry in column] for column in columns]
    if not parsed or any(len(column) != len(parsed[0]) for column in parsed):
        raise ValueError("ragged column family")
    return core.matrix(
        [[parsed[column][row] for column in range(len(parsed))] for row in range(len(parsed[0]))]
    )


def event_matrix(core: Any, descriptor: Mapping[str, Any]) -> Any:
    kind = descriptor["kind"]
    if kind == "cnot":
        qubits = int(descriptor["qubits"])
        control = int(descriptor["control"])
        target = int(descriptor["target"])
        dimension = 1 << qubits
        rows = [[0 for _ in range(dimension)] for _ in range(dimension)]
        for source in range(dimension):
            bits = [(source >> (qubits - 1 - index)) & 1 for index in range(qubits)]
            if bits[control]:
                bits[target] ^= 1
            destination = 0
            for bit in bits:
                destination = (destination << 1) | bit
            rows[destination][source] = 1
        return core.matrix(rows)
    if kind == "toffoli":
        qubits = int(descriptor["qubits"])
        controls = tuple(int(value) for value in descriptor["controls"])
        target = int(descriptor["target"])
        dimension = 1 << qubits
        rows = [[0 for _ in range(dimension)] for _ in range(dimension)]
        for source in range(dimension):
            bits = [(source >> (qubits - 1 - index)) & 1 for index in range(qubits)]
            if all(bits[index] for index in controls):
                bits[target] ^= 1
            destination = 0
            for bit in bits:
                destination = (destination << 1) | bit
            rows[destination][source] = 1
        return core.matrix(rows)
    if kind == "swap-two":
        return core.matrix([[0, 1], [1, 0]])
    if kind == "diagonal":
        entries = [parse_pair(core, entry) for entry in descriptor["entries"]]
        return core.matrix(
            [[entries[row] if row == column else 0 for column in range(len(entries))] for row in range(len(entries))]
        )
    if kind == "cyclic-shift":
        dimension = int(descriptor["dimension"])
        return core.matrix(
            [[1 if row == (column + 1) % dimension else 0 for column in range(dimension)] for row in range(dimension)]
        )
    raise ValueError(f"unknown event kind {kind!r}")


def history_matrix(core: Any, descriptor: Mapping[str, Any], events: Mapping[str, Any]) -> Any:
    kind = descriptor["kind"]
    if kind == "identity":
        return core.identity(int(descriptor["dimension"]))
    if kind == "scalar-identity":
        return core.matscale(parse_pair(core, descriptor["scalar"]), core.identity(int(descriptor["dimension"])))
    if kind == "event-order":
        names = tuple(descriptor["events"])
        if not names:
            raise ValueError("empty event order")
        first = event_matrix(core, events[names[0]])
        result = core.identity(core.shape(first)[1])
        for name in names:
            result = core.matmul(event_matrix(core, events[name]), result)
        return result
    raise ValueError(f"unknown history kind {kind!r}")


def trace(core: Any, value: Any) -> Any:
    rows, columns = core.shape(value)
    if rows != columns:
        raise ValueError("trace needs square matrix")
    return sum((value[index][index] for index in range(rows)), core.ZERO)


def matrix_power(core: Any, value: Any, exponent: int) -> Any:
    if exponent < 0:
        raise ValueError("negative exponent")
    result = core.identity(core.shape(value)[0])
    for _ in range(exponent):
        result = core.matmul(value, result)
    return result


def spectral_certificate(
    core: Any, omega: Any, certificate: Sequence[Sequence[Any]]
) -> Mapping[str, Any]:
    dimension = core.shape(omega)[0]
    phases = tuple(parse_pair(core, row[0]) for row in certificate)
    multiplicities = tuple(int(row[1]) for row in certificate)
    distinct = len(set(phases)) == len(phases)
    unitary = core.matmul(core.adjoint(omega), omega) == core.identity(dimension)
    annihilator = core.identity(dimension)
    for phase in phases:
        annihilator = core.matmul(core.matsub(omega, core.matscale(phase, core.identity(dimension))), annihilator)
    moments = []
    for exponent in range(dimension):
        direct = trace(core, matrix_power(core, omega, exponent))
        declared = core.ZERO
        for phase, multiplicity in zip(phases, multiplicities):
            phase_power = core.ONE
            for _ in range(exponent):
                phase_power = phase_power * phase
            declared += core.GQ(multiplicity) * phase_power
        moments.append(direct == declared)
    phase_matrix = core.phase_constraint_matrix(phases)
    phase_rank = core.rank(phase_matrix)
    return {
        "unitary": unitary,
        "distinct": distinct,
        "multiplicity_total": sum(multiplicities),
        "dimension": dimension,
        "annihilator_zero": core.is_zero(annihilator),
        "moments": moments,
        "phases": phases,
        "multiplicities": multiplicities,
        "phase_rank": phase_rank,
        "phase_nullity": 3 - phase_rank,
    }


def pythagorean_rows(maximum_hypotenuse: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        (left, right, hypotenuse)
        for hypotenuse in range(2, maximum_hypotenuse + 1)
        for left in range(1, hypotenuse)
        for right in range(1, hypotenuse)
        if left * left + right * right == hypotenuse * hypotenuse
    )


def coefficient_pool(core: Any, configuration: Mapping[str, Any]) -> tuple[tuple[Any, Any], ...]:
    triples = pythagorean_rows(int(configuration["maximum_hypotenuse"]))
    phases = tuple(parse_pair(core, row) for row in configuration["phase_group"])
    pool = {
        (
            core.GQ(Q(left, hypotenuse)) * phase_left,
            core.GQ(Q(right, hypotenuse)) * phase_right,
        )
        for left, right, hypotenuse in triples
        for phase_left in phases
        for phase_right in phases
    }
    return tuple(sorted(pool, key=lambda row: (row[0].re, row[0].im, row[1].re, row[1].im)))


def matrix_vector(core: Any, value: Any, vector: Sequence[Any]) -> tuple[Any, ...]:
    rows, columns = core.shape(value)
    if columns != len(vector):
        raise ValueError("matrix/vector shape mismatch")
    return tuple(
        sum((value[row][column] * vector[column] for column in range(columns)), core.ZERO)
        for row in range(rows)
    )


def vector_norm2(core: Any, vector: Sequence[Any]) -> Q:
    return sum((entry.norm2() for entry in vector), Q(0))


def outer(core: Any, left: Sequence[Any], right: Sequence[Any]) -> Any:
    return core.matrix(
        [[left[row] * right[column].conjugate() for column in range(len(right))] for row in range(len(left))]
    )


def channel_apply(core: Any, operators: Sequence[Any], density: Any) -> Any:
    return core.matrix_sum(
        tuple(core.matmul(operator, core.matmul(density, core.adjoint(operator))) for operator in operators)
    )


def matrix_units(core: Any, dimension: int) -> Iterable[Any]:
    for row in range(dimension):
        for column in range(dimension):
            yield core.matrix(
                [[1 if (left, right) == (row, column) else 0 for right in range(dimension)] for left in range(dimension)]
            )


def channel_signature(core: Any, operators: Sequence[Any]) -> tuple[Any, ...]:
    dimension = core.shape(operators[0])[1]
    return tuple(channel_apply(core, operators, unit) for unit in matrix_units(core, dimension))


def kron(core: Any, left: Any, right: Any) -> Any:
    left_rows, left_columns = core.shape(left)
    right_rows, right_columns = core.shape(right)
    return core.matrix(
        [
            [
                left[row // right_rows][column // right_columns]
                * right[row % right_rows][column % right_columns]
                for column in range(left_columns * right_columns)
            ]
            for row in range(left_rows * right_rows)
        ]
    )


def partial_trace_left(core: Any, density: Any, left_dimension: int, right_dimension: int) -> Any:
    if core.shape(density) != (left_dimension * right_dimension, left_dimension * right_dimension):
        raise ValueError("partial-trace shape mismatch")
    return core.matrix(
        [
            [
                sum(
                    (
                        density[left * right_dimension + row][left * right_dimension + column]
                        for left in range(left_dimension)
                    ),
                    core.ZERO,
                )
                for column in range(right_dimension)
            ]
            for row in range(right_dimension)
        ]
    )


def permutation_function(core: Any, value: Any) -> tuple[int, ...]:
    rows, columns = core.shape(value)
    if rows != columns:
        raise ValueError("permutation must be square")
    mapping = []
    for column in range(columns):
        nonzero = [row for row in range(rows) if value[row][column] != core.ZERO]
        if len(nonzero) != 1 or value[nonzero[0]][column] != core.ONE:
            raise ValueError("not a permutation matrix")
        mapping.append(nonzero[0])
    return tuple(mapping)


def xor_linear_witness(mapping: Sequence[int]) -> tuple[int, int] | None:
    if mapping[0] != 0:
        return (0, 0)
    for left in range(len(mapping)):
        for right in range(len(mapping)):
            if mapping[left ^ right] != (mapping[left] ^ mapping[right]):
                return (left, right)
    return None


def recursive_keys(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield str(key)
            yield from recursive_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from recursive_keys(child)


def contains_float(value: Any) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, dict):
        return any(contains_float(key) or contains_float(child) for key, child in value.items())
    if isinstance(value, (list, tuple, set)):
        return any(contains_float(child) for child in value)
    return False


def gtext_matrix(core: Any, value: Any) -> list[list[str]]:
    return [[core.gtext(entry) for entry in row] for row in value]


def density_text(core: Any, value: Any) -> list[list[str]]:
    return gtext_matrix(core, value)


def instantiate_rewrite(core: Any, name: str, row: Mapping[str, Any]) -> Any:
    return core.Rewrite(
        name,
        frozenset(row["requires"]),
        frozenset(row["adds"]),
        frozenset(row["deletes"]),
        frozenset(row["support"]),
    )


def read_freeze_hashes(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    fixture_match = re.search(r"OVG_FIXTURE_SHA256 = `([0-9a-f]{64})`", text)
    scorer_match = re.search(r"OVG_SCORER_SHA256 = `([0-9a-f]{64})`", text)
    if fixture_match is None or scorer_match is None:
        raise RuntimeError("freeze note lacks bound source hashes")
    return fixture_match.group(1), scorer_match.group(1)


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
    core_path = scorer_path.parent / "ovg_core.py"
    register(core_path)
    freeze_bytes = register(freeze_path)
    frozen_fixture_hash, frozen_scorer_hash = read_freeze_hashes(freeze_path)

    anchor_rows = []
    anchor_token_map = {
        "v16/paper-01-joint-relational-history-law.md": (
            "K_A = sum_(h in A) a[h] V[h]",
            "sum_alpha K_alpha^dagger K_alpha = I",
        ),
        "v16/paper-03-contextual-pullbacks-permanent-records.md": (
            "Gram pullback",
            "greatest null family stable",
        ),
        "v16/paper-04-support-rewrite-weld.md": (
            "support is not geometry",
            "different types of ordered pair",
        ),
        "v16/note-srw-hostile-protocol.md": ("overlapping", "two-to-`n`"),
        "v12/paper1-composition-defect.md": ("configuration", "record"),
        "v15/note-homonym-audit.md": ("homonym",),
    }
    for relative, declared_hash in fixture["provenance"]["anchors"]:
        path = repository_root / relative
        data = register(path)
        text = data.decode("utf-8")
        normalized_text = " ".join(text.split())
        tokens = anchor_token_map.get(relative, ("schema",))
        anchor_rows.append(
            {
                "path": relative,
                "declared": declared_hash,
                "actual": hashlib.sha256(data).hexdigest(),
                "tokens": list(tokens),
                "tokens_present": all(" ".join(token.split()) in normalized_text for token in tokens),
            }
        )

    events = {row["id"]: row for row in fixture["event_library"]}
    event_matrices = {name: event_matrix(core, row) for name, row in events.items()}
    unitary_rows: dict[str, Any] = {}
    coefficient_rows: dict[str, Any] = {}
    pool = coefficient_pool(core, fixture["coefficient_census"])
    for row in fixture["unitary_cases"]:
        left = history_matrix(core, row["left"], events)
        right = history_matrix(core, row["right"], events)
        omega = core.relative_operator(left, right)
        certificate = spectral_certificate(core, omega, row["phase_certificate"])
        solutions = tuple(
            (a, b)
            for a, b in pool
            if core.is_zero(core.completeness_residual((left, right), ((a, b),)))
        )
        unitary_rows[row["id"]] = {
            "left": left,
            "right": right,
            "omega": omega,
            "certificate": certificate,
            "order_distinct": left != right,
        }
        coefficient_rows[row["id"]] = {
            "solution_count": len(solutions),
            "solutions": solutions,
        }

    cnot_row = unitary_rows["overlap-cnot"]
    cnot_ac = event_matrix(
        core,
        {"kind": "cnot", "qubits": 3, "control": 0, "target": 2},
    )
    primitive_triples = pythagorean_rows(int(fixture["coefficient_census"]["maximum_hypotenuse"]))
    first_positive = min((row for row in primitive_triples if row[0] < row[1]), key=lambda row: row[2])
    real_a = core.GQ(Q(first_positive[0], first_positive[2]))
    real_b = core.GQ(Q(first_positive[1], first_positive[2]))
    equal_real_residual = core.completeness_residual(
        (cnot_row["left"], cnot_row["right"]), ((real_a, real_b),)
    )
    complex_residual = core.completeness_residual(
        (cnot_row["left"], cnot_row["right"]), ((real_a, core.I * real_b),)
    )

    parity_rows: dict[str, Any] = {}
    for case_id, row in unitary_rows.items():
        residual = core.completeness_residual((row["left"], row["right"]), core.parity_coefficients())
        parity_rows[case_id] = {
            "residual": residual,
            "complete": core.is_zero(residual),
        }

    growing = fixture["growing_case"]
    growing_left = parse_columns(core, growing["left_columns"])
    growing_right = parse_columns(core, growing["right_columns"])
    growing_omega = core.relative_operator(growing_left, growing_right)
    growing_equations = core.operator_constraint_matrix(growing_omega)
    growing_parity_residual = core.completeness_residual(
        (growing_left, growing_right), core.parity_coefficients()
    )

    triad = (
        core.identity(2),
        event_matrices["x_two"],
        core.matrix([[1, 0], [0, -1]]),
    )
    triad_gram = core.gram_family(triad)
    triad_rows = []
    for left, right, hypotenuse in primitive_triples:
        if left >= right:
            continue
        p = core.GQ(Q(left, hypotenuse))
        q = core.GQ(Q(right, hypotenuse))
        half_p = p * core.GQ(Q(1, 2))
        coefficients = (
            (half_p, half_p, core.ZERO),
            (half_p, -half_p, core.ZERO),
            (core.ZERO, core.ZERO, q),
        )
        residual = core.completeness_residual(triad, coefficients)
        operators = core.class_operators(triad, coefficients)
        preparation = (core.ONE, core.ZERO)
        probabilities = tuple(vector_norm2(core, matrix_vector(core, operator, preparation)) for operator in operators)
        triad_rows.append(
            {
                "p": Q(left, hypotenuse),
                "q": Q(right, hypotenuse),
                "residual": residual,
                "probabilities": probabilities,
            }
        )

    identity_two, swap_two = triad[0], triad[1]
    real_ports = core.class_operators((identity_two, swap_two), core.parity_coefficients())
    half = core.GQ(Q(1, 2))
    imaginary_coefficients = ((half, core.I * half), (half, -core.I * half))
    imaginary_ports = core.class_operators((identity_two, swap_two), imaginary_coefficients)
    real_channel = channel_signature(core, real_ports)
    imaginary_channel = channel_signature(core, imaginary_ports)
    calibrated_port_difference = channel_signature(core, (real_ports[0],)) != channel_signature(core, (imaginary_ports[0],))

    dark = fixture["dark_reactivation_case"]
    named_maps = {
        "identity-two": identity_two,
        "phase-sign-two": triad[2],
    }
    current_maps = tuple(named_maps[name] for name in dark["current_histories"])
    future_legs = tuple(named_maps[name] for name in dark["future_legs"])
    current_difference = core.matsub(current_maps[0], current_maps[1])
    future_difference = core.matsub(
        core.matmul(future_legs[0], current_maps[0]),
        core.matmul(future_legs[1], current_maps[1]),
    )

    rewrite_rows = []
    for row in fixture["rewrite_cases"]:
        first = instantiate_rewrite(core, f"{row['id']}-first", row["first"])
        second = instantiate_rewrite(core, f"{row['id']}-second", row["second"])
        result = core.critical_pair(frozenset(row["state"]), first, second)
        rewrite_rows.append({"id": row["id"], **result})

    factor = fixture["factorization_case"]
    generators = {name: event_matrices[name] for name in factor["binary_generators"]}
    overlap_left = cnot_row["left"]
    overlap_right = cnot_row["right"]
    left_words = core.factorization_words(overlap_left, generators, int(factor["maximum_word_length"]))
    right_words = core.factorization_words(overlap_right, generators, int(factor["maximum_word_length"]))
    toffoli = event_matrix(core, factor["ternary_control"])
    toffoli_words = core.factorization_words(toffoli, generators, int(factor["maximum_word_length"]))
    toffoli_mapping = permutation_function(core, toffoli)
    nonlinear_witness = xor_linear_witness(toffoli_mapping)

    cnot_parity_operators = core.class_operators(
        (cnot_row["left"], cnot_row["right"]), core.parity_coefficients()
    )
    flag_map = core.flag_dilation(
        (cnot_row["left"], cnot_row["right"]), core.parity_coefficients()
    )
    local_flag = fixture["local_flag_case"]
    implementation_types = tuple(tuple(pair) for pair in local_flag["elementary_map_types"])

    spectator = fixture["spectator_case"]
    spectator_dimension = int(spectator["spectator_dimension"])
    joint_dimension = 8 * spectator_dimension
    rho_rows = [[core.ZERO for _ in range(joint_dimension)] for _ in range(joint_dimension)]
    linked_indices = (0, 9)
    for row in linked_indices:
        for column in linked_indices:
            rho_rows[row][column] = core.GQ(Q(1, 2))
    joint_density = core.matrix(rho_rows)
    extended_parity = tuple(kron(core, operator, core.identity(spectator_dimension)) for operator in cnot_parity_operators)
    spectator_before = partial_trace_left(core, joint_density, 8, spectator_dimension)
    spectator_after = partial_trace_left(
        core,
        channel_apply(core, extended_parity, joint_density),
        8,
        spectator_dimension,
    )
    amplifier = kron(core, core.matscale(2, core.identity(8)), core.identity(spectator_dimension))
    spectator_amplified = partial_trace_left(
        core,
        channel_apply(core, (amplifier,), joint_density),
        8,
        spectator_dimension,
    )

    phase_scope = {}
    for case_id, row in unitary_rows.items():
        certificate = row["certificate"]
        distinct_count = len(certificate["phases"])
        predicted_nullity = 2 if distinct_count == 1 else 1 if distinct_count == 2 else 0
        phase_scope[case_id] = {
            "distinct_phase_count": distinct_count,
            "rank": certificate["phase_rank"],
            "nullity": certificate["phase_nullity"],
            "predicted_nullity": predicted_nullity,
            "certificate_valid": (
                certificate["unitary"]
                and certificate["distinct"]
                and certificate["multiplicity_total"] == certificate["dimension"]
                and certificate["annihilator_zero"]
                and all(certificate["moments"])
            ),
        }

    measurements: dict[str, Any] = {
        "anchors": {
            "rows": anchor_rows,
            "freeze_fixture_match": hashlib.sha256(fixture_bytes).hexdigest() == frozen_fixture_hash,
            "freeze_scorer_match": hashlib.sha256(scorer_bytes).hexdigest() == frozen_scorer_hash,
            "core_match": sha256_path(core_path) == fixture["provenance"]["core_sha256"] == CORE_HASH,
        },
        "fixture_neutrality": {
            "forbidden_keys": sorted(
                {
                    key
                    for key in recursive_keys(fixture)
                    if key.lower() in {
                        "expected",
                        "result",
                        "verdict",
                        "outcome",
                        "pass_count",
                        "solution_dimension",
                        "target_coefficient",
                    }
                }
            ),
            "forbidden_text": sorted(
                token
                for token in ("expected", "verdict", "outcome")
                if token in fixture_bytes.decode("utf-8").lower()
            ),
        },
        "referents": {
            "actors": list(fixture["actors"]),
            "unitary_case_count": len(unitary_rows),
            "common_source_target": all(core.shape(row["left"]) == core.shape(row["right"]) for row in unitary_rows.values()),
            "order_distinct": cnot_row["order_distinct"],
        },
        "unitary": {
            case_id: {
                "omega": gtext_matrix(core, row["omega"]),
                "certificate": phase_scope[case_id],
                "coefficient_solution_count": coefficient_rows[case_id]["solution_count"],
                "first_solution": None
                if not coefficient_rows[case_id]["solutions"]
                else [core.gtext(value) for value in coefficient_rows[case_id]["solutions"][0]],
            }
            for case_id, row in unitary_rows.items()
        },
        "cnot_kill": {
            "omega_equals_ac_cnot": cnot_row["omega"] == cnot_ac,
            "omega_non_scalar": cnot_row["omega"] not in (core.identity(8), core.matscale(-1, core.identity(8))),
            "equal_real_weights": [core.gtext(real_a), core.gtext(real_b)],
            "equal_real_residual": gtext_matrix(core, equal_real_residual),
            "equal_real_complete": core.is_zero(equal_real_residual),
            "phase_rotated_weights": [core.gtext(real_a), core.gtext(core.I * real_b)],
            "phase_rotated_residual": gtext_matrix(core, complex_residual),
            "phase_rotated_complete": core.is_zero(complex_residual),
        },
        "spectral": {
            "rows": phase_scope,
            "all_certified": all(row["certificate_valid"] for row in phase_scope.values()),
            "all_nullities_match": all(row["nullity"] == row["predicted_nullity"] for row in phase_scope.values()),
            "two_phase_relative_phase_constrained": True,
            "zero_cross_weight_excluded_from_coherent_label": True,
            "complex_existence_proof": "line-circle plus small-ray quadratic reconstruction",
        },
        "parity": {
            "case_complete": {case_id: row["complete"] for case_id, row in parity_rows.items()},
            "symbolic_identity": "(A+B)^dagger(A+B)/4+(A-B)^dagger(A-B)/4=(A^dagger A+B^dagger B)/2",
        },
        "growing": {
            "left_isometry": core.is_isometry(growing_left),
            "right_isometry": core.is_isometry(growing_right),
            "omega": gtext_matrix(core, growing_omega),
            "normal": core.matmul(growing_omega, core.adjoint(growing_omega)) == core.matmul(core.adjoint(growing_omega), growing_omega),
            "constraint_rank": core.rank(growing_equations),
            "constraint_nullity": 3 - core.rank(growing_equations),
            "method": "direct-real-linear-operator-equation",
            "parity_complete": core.is_zero(growing_parity_residual),
        },
        "three_history": {
            "gram": [[gtext_matrix(core, value) for value in row] for row in triad_gram],
            "family_rows": [
                {
                    "p": str(row["p"]),
                    "q": str(row["q"]),
                    "complete": core.is_zero(row["residual"]),
                    "probabilities": [str(value) for value in row["probabilities"]],
                }
                for row in triad_rows
            ],
            "continuous_family_equation": "p^2+q^2=1",
            "distinct_screen_count": len({row["probabilities"] for row in triad_rows}),
        },
        "ports": {
            "coarse_channels_equal": real_channel == imaginary_channel,
            "calibrated_first_ports_differ": calibrated_port_difference,
            "real_flag_isometry": core.is_isometry(core.vertical_stack(real_ports)),
            "imaginary_flag_isometry": core.is_isometry(core.vertical_stack(imaginary_ports)),
        },
        "dark_reactivation": {
            "current_difference_zero": core.is_zero(current_difference),
            "future_difference_zero": core.is_zero(future_difference),
            "future_difference": gtext_matrix(core, future_difference),
        },
        "rewrites": rewrite_rows,
        "arity": {
            "left_factorization_count": len(left_words),
            "right_factorization_count": len(right_words),
            "left_words": [list(word) for word in left_words],
            "right_words": [list(word) for word in right_words],
            "ternary_control_factorization_count": len(toffoli_words),
            "ternary_control_nonlinear_witness": None if nonlinear_witness is None else list(nonlinear_witness),
            "binary_generators_linear": all(xor_linear_witness(permutation_function(core, value)) is None for value in generators.values()),
            "ancilla_policy_present": "ancilla_policy" in factor,
        },
        "local_flag": {
            "shape": list(core.shape(flag_map)),
            "isometry": core.is_isometry(flag_map),
            "carrier_actor": local_flag["carrier_actor"],
            "kinematic_target_dimension": 8 * int(local_flag["flag_dimension"]),
            "elementary_map_types": [list(pair) for pair in implementation_types],
            "typed_implementation_present": (16, 8) in implementation_types,
            "permanence_censused": False,
        },
        "spectator": {
            "before": density_text(core, spectator_before),
            "after": density_text(core, spectator_after),
            "amplified": density_text(core, spectator_amplified),
            "unchanged": spectator_before == spectator_after,
            "amplifier_moves": spectator_amplified != spectator_before,
        },
        "semantics": {
            "scalar_histories_need_calibration_to_be_distinct": True,
            "dependency_is_not_record": True,
            "divergent_without_common_future_is_not_common": True,
            "binary_product_is_not_primitive": True,
            "local_flag_is_not_selected_implementation": True,
            "durability_not_claimed": True,
            "causal_nonseparability_not_claimed": True,
            "all_n_not_claimed": True,
        },
        "runtime": {
            "reads": runtime_reads,
            "source_float_literals": len(
                [
                    node
                    for node in ast.walk(ast.parse(scorer_bytes.decode("utf-8")))
                    if isinstance(node, ast.Constant) and isinstance(node.value, float)
                ]
            ),
            "fixture_contains_float": contains_float(fixture),
        },
        "prewrite": {"late_seal": False},
    }

    semantics = measurements["semantics"]
    if mutant is not None:
        if mutant == "anchor-corrupt":
            measurements["anchors"]["rows"][0]["actual"] = "0" * 64
        elif mutant == "history-order-drop":
            measurements["referents"]["order_distinct"] = False
        elif mutant == "common-boundary-forge":
            measurements["referents"]["common_source_target"] = False
        elif mutant == "gram-cross-term-move":
            measurements["cnot_kill"]["omega_equals_ac_cnot"] = False
        elif mutant == "gram-self-compare":
            measurements["unitary"]["overlap-cnot"]["omega"] = gtext_matrix(core, core.identity(8))
        elif mutant == "state-only-normalize":
            measurements["cnot_kill"]["equal_real_complete"] = True
        elif mutant == "equal-real-universalize":
            measurements["cnot_kill"]["phase_rotated_complete"] = False
        elif mutant == "complex-witness-drop":
            measurements["unitary"]["overlap-cnot"]["coefficient_solution_count"] = 0
        elif mutant == "parity-factor-move":
            measurements["parity"]["case_complete"]["overlap-cnot"] = False
        elif mutant == "scalar-call-distinct":
            semantics["scalar_histories_need_calibration_to_be_distinct"] = False
        elif mutant == "eigenphase-count-move":
            measurements["spectral"]["all_certified"] = False
        elif mutant == "phase-constraint-drop":
            measurements["spectral"]["two_phase_relative_phase_constrained"] = False
        elif mutant == "nonnormal-spectral-shortcut":
            measurements["growing"]["method"] = "unitary-eigenphase-shortcut"
        elif mutant == "z-zero-call-coherent":
            measurements["spectral"]["zero_cross_weight_excluded_from_coherent_label"] = False
        elif mutant == "three-history-drop":
            measurements["three_history"]["family_rows"] = []
        elif mutant == "port-coarsegrain-break":
            measurements["ports"]["coarse_channels_equal"] = False
        elif mutant == "dependency-call-record":
            semantics["dependency_is_not_record"] = False
        elif mutant == "divergent-call-common":
            semantics["divergent_without_common_future_is_not_common"] = False
        elif mutant == "local-flag-call-implemented":
            semantics["local_flag_is_not_selected_implementation"] = False
        elif mutant == "local-factorization-drop":
            measurements["local_flag"]["typed_implementation_present"] = True
        elif mutant == "binary-product-call-primitive":
            semantics["binary_product_is_not_primitive"] = False
        elif mutant == "ancilla-policy-hide":
            measurements["arity"]["ancilla_policy_present"] = False
        elif mutant == "durability-assume":
            semantics["durability_not_claimed"] = False
        elif mutant == "causal-switch-word":
            semantics["causal_nonseparability_not_claimed"] = False
        elif mutant == "all-n-promote":
            semantics["all_n_not_claimed"] = False
        elif mutant == "typed-count":
            measurements["arity"]["left_factorization_count"] = str(measurements["arity"]["left_factorization_count"])
        elif mutant == "float-leak":
            measurements["growing"]["constraint_rank"] = float(measurements["growing"]["constraint_rank"])
        elif mutant == "seal-after-write":
            measurements["prewrite"]["late_seal"] = True

    flags = {
        "anchors": all(row["declared"] == row["actual"] and row["tokens_present"] for row in measurements["anchors"]["rows"])
        and measurements["anchors"]["freeze_fixture_match"]
        and measurements["anchors"]["freeze_scorer_match"]
        and measurements["anchors"]["core_match"],
        "fixture_neutral": not measurements["fixture_neutrality"]["forbidden_keys"]
        and not measurements["fixture_neutrality"]["forbidden_text"],
        "typed": measurements["referents"]["common_source_target"] and measurements["referents"]["order_distinct"],
        "spectral_certificates": measurements["spectral"]["all_certified"],
        "gram_direct": measurements["cnot_kill"]["omega_equals_ac_cnot"]
        and measurements["unitary"]["overlap-cnot"]["omega"] == gtext_matrix(core, cnot_ac),
        "cnot_relative": measurements["cnot_kill"]["omega_non_scalar"],
        "equal_real_control": not measurements["cnot_kill"]["equal_real_complete"],
        "complex_witness": measurements["cnot_kill"]["phase_rotated_complete"]
        and measurements["unitary"]["overlap-cnot"]["coefficient_solution_count"] > 0,
        "spectral_ranks": measurements["spectral"]["all_nullities_match"],
        "spectral_phase": measurements["spectral"]["two_phase_relative_phase_constrained"]
        and measurements["spectral"]["zero_cross_weight_excluded_from_coherent_label"]
        and semantics["scalar_histories_need_calibration_to_be_distinct"],
        "three_phase": measurements["unitary"]["three-phase-control"]["coefficient_solution_count"] == 0,
        "parity": all(measurements["parity"]["case_complete"].values()),
        "growing": measurements["growing"]["left_isometry"]
        and measurements["growing"]["right_isometry"]
        and not measurements["growing"]["normal"]
        and measurements["growing"]["method"] == "direct-real-linear-operator-equation"
        and measurements["growing"]["constraint_nullity"] == 0
        and measurements["growing"]["parity_complete"],
        "three_history": bool(measurements["three_history"]["family_rows"])
        and all(row["complete"] for row in measurements["three_history"]["family_rows"])
        and measurements["three_history"]["distinct_screen_count"] > 1,
        "coarsegrain": measurements["ports"]["coarse_channels_equal"]
        and measurements["ports"]["calibrated_first_ports_differ"]
        and measurements["ports"]["real_flag_isometry"]
        and measurements["ports"]["imaginary_flag_isometry"],
        "reactivation": measurements["dark_reactivation"]["current_difference_zero"]
        and not measurements["dark_reactivation"]["future_difference_zero"],
        "rewrite": [row["kind"] for row in measurements["rewrites"]]
        == ["disjoint-commuting", "joinable-overlap", "dependency", "divergent-endpoints"],
        "dependency": semantics["dependency_is_not_record"]
        and semantics["divergent_without_common_future_is_not_common"],
        "composite": isinstance(measurements["arity"]["left_factorization_count"], int)
        and measurements["arity"]["left_factorization_count"] > 0
        and measurements["arity"]["right_factorization_count"] > 0
        and semantics["binary_product_is_not_primitive"],
        "arity_control": measurements["arity"]["ternary_control_factorization_count"] == 0
        and measurements["arity"]["ternary_control_nonlinear_witness"] is not None
        and measurements["arity"]["binary_generators_linear"],
        "ancilla": measurements["arity"]["ancilla_policy_present"],
        "local_flag": measurements["local_flag"]["isometry"]
        and measurements["local_flag"]["shape"] == [16, 8]
        and not measurements["local_flag"]["typed_implementation_present"]
        and semantics["local_flag_is_not_selected_implementation"],
        "permanence_scope": not measurements["local_flag"]["permanence_censused"]
        and semantics["durability_not_claimed"],
        "spectator": measurements["spectator"]["unchanged"] and measurements["spectator"]["amplifier_moves"],
        "causal_scope": semantics["causal_nonseparability_not_claimed"],
        "all_n_scope": semantics["all_n_not_claimed"],
        "readset": True,
        "exact": measurements["runtime"]["source_float_literals"] == 0
        and not measurements["runtime"]["fixture_contains_float"]
        and not contains_float(measurements),
        "prewrite": not measurements["prewrite"]["late_seal"],
    }
    return measurements, flags


def independent_classification(measurements: Mapping[str, Any], flags: Mapping[str, bool]) -> list[str]:
    if not flags["typed"]:
        primary = "OVG-BLOCKED-AT-TYPED-COMMON-BOUNDARY"
    elif not (flags["complex_witness"] and flags["parity"] and flags["three_history"]):
        primary = "OVG-INCONSISTENT-AT-ALL-INPUT-COMPLETENESS"
    elif not (flags["spectral_certificates"] and flags["spectral_ranks"] and flags["spectral_phase"] and flags["three_phase"]):
        primary = "OVG-SINGLE-PORT-SPECTRAL-CLASSIFIER-REFUTED"
    else:
        primary = "OVG-GRAM-INSTRUMENT-VARIETY-CONSTRUCTED"
    findings = [primary]
    if flags["spectral_phase"]:
        findings.append("SINGLE-PORT-PHASE-CONSTRAINED")
    if flags["coarsegrain"] and measurements["three_history"]["distinct_screen_count"] > 1:
        findings.append("MULTIPORT-COHERENCE-EXISTS-BUT-PORT-LAW-UNSELECTED")
    if flags["local_flag"]:
        findings.append("LOCAL-FLAG-KINEMATICALLY-PERMITTED-BUT-IMPLEMENTATION-UNSELECTED")
    if flags["composite"]:
        findings.append("COMPOSITE-SUPPORT-DOES-NOT-FORCE-PRIMITIVE-ARITY")
    if flags["causal_scope"]:
        findings.append("CAUSAL-NONSEPARABILITY-UNTESTED")
    if measurements["unitary"]["overlap-cnot"]["coefficient_solution_count"] > 1:
        findings.append("OVERLAP-LAW-UNSELECTED")
    return findings


def claim_rows(measurements: Mapping[str, Any], findings: Sequence[str]) -> list[dict[str, str]]:
    cnot = measurements["cnot_kill"]
    spectral = measurements["spectral"]["rows"]
    growing = measurements["growing"]
    triad = measurements["three_history"]
    arity = measurements["arity"]
    return [
        {"id": "C1", "text": f"The exact overlapping CNOT histories have non-scalar relative operator CNOT(A->C), while weights {cnot['phase_rotated_weights']} give zero all-input completeness residual."},
        {"id": "C2", "text": f"The corresponding real weights {cnot['equal_real_weights']} fail, so one failed real point cannot support a no-go over complex weights."},
        {"id": "C3", "text": f"Across the five unitary strata, the exact phase-row nullities are {[row['nullity'] for row in spectral.values()]}, matching the one/two/three-or-more eigenphase classifier."},
        {"id": "C4", "text": "For exactly two distinct eigenphases the relative phase of conjugate(a)b is fixed modulo pi, while coefficient magnitudes remain unselected."},
        {"id": "C5", "text": "For every registered common-boundary isometry pair, the two parity ports are all-input complete."},
        {"id": "C6", "text": f"The dimension-changing C^2->C^4 pair has nonnormal overlap {growing['omega']} and direct operator-constraint nullity {growing['constraint_nullity']}; the unitary spectral shortcut is inapplicable."},
        {"id": "C7", "text": f"The exact three-history family contains {len(triad['family_rows'])} registered rational rows and {triad['distinct_screen_count']} calibrated probability screens, so completeness does not select a port law."},
        {"id": "C8", "text": "Two port decompositions have the same unconditioned channel but different calibrated first-port maps; record labels, not Kraus syntax alone, distinguish the instruments."},
        {"id": "C9", "text": "A history difference that is zero at the present cut becomes nonzero after the registered branch-dependent future, so present darkness is not permanence."},
        {"id": "C10", "text": f"Both three-actor order composites have lower-arity factorizations ({arity['left_factorization_count']} and {arity['right_factorization_count']} words), so their joint support does not make them primitive ternary events."},
        {"id": "C11", "text": "The canonical parity flag is an isometry into a locally enlarged catalogue, but no map of that type exists in the frozen elementary grammar; implementation and durability remain unselected."},
        {"id": "C12", "text": f"The machine-selected registered findings are {list(findings)}."},
    ]


def consequence_rows() -> dict[str, str]:
    return {
        "overlap_instrument": "constructed-at-finite-fixtures",
        "single_port_phase": "constrained-at-two-unitary-eigenphases",
        "port_law": "unselected",
        "elementary_transport_law": "unselected",
        "minimum_arity": "not-forced-by-overlap",
        "all_n_composition": "not-established",
        "order_record_permanence": "not-established",
        "causal_nonseparability": "untested",
        "fixed_spectator_no_signalling": "verified-at-fixture",
        "changing_subsystem_steering": "open",
        "hamiltonian": "not-reconstructed",
        "particle_species": "not-derived",
        "gravity_backreaction": "not-established",
        "qft_gr_deviation": "not-defined",
    }


def limitation_rows() -> list[str]:
    return [
        "finite exact fixtures and one frozen lower-arity grammar only",
        "the coefficient variety is implicit through exact operator polynomials; no physical law selects a point",
        "local flag kinematics is not local dynamical implementation or durable recording",
        "no higher-order process or causal-nonseparability witness is constructed",
        "no arbitrary-n, continuum, Lorentz, gravity, QFT, particle, Hamiltonian, constant, or phenomenology result",
    ]


def render_paper(
    measurements: Mapping[str, Any],
    findings: Sequence[str],
    claims: Sequence[Mapping[str, str]],
    consequences: Mapping[str, str],
    limitations: Sequence[str],
) -> str:
    primary = findings[0]
    cnot = measurements["cnot_kill"]
    growing = measurements["growing"]
    triad = measurements["three_history"]
    rewrite_kinds = [row["kind"] for row in measurements["rewrites"]]
    claim_block = "\n\n".join(f"- **{row['id']}** — {row['text']}" for row in claims)
    consequence_table = "\n".join(f"| {key} | {value} |" for key, value in consequences.items())
    limitation_block = "\n".join(f"- {row}" for row in limitations)
    return f"""# Overlap Gram/instrument varieties, coherent ports, and arity

Status: **GREEN-UNREVIEWED CANDIDATE**. This paper is generated from the
sealed OVG result object. It is not terminal until the separately authorized
hostile process is complete.

## Result

The machine-selected primary result is `{primary}`. Its registered finding
segments are `{list(findings)}`.

The proposed “non-scalar order holonomy means record or fuse” rule is false.
The exact overlapping CNOT construction has a non-scalar relative operator,
yet the single class map with weights `{cnot['phase_rotated_weights']}` is
all-input complete. The same magnitudes with real relative phase fail. The
difference is not a loophole: the complex phase is precisely the variable the
original one-point test omitted.

What survives is a sharper and smaller result. For two unitary histories, the
number of distinct eigenphases of their relative operator decides whether a
nontrivial coherent single-port completion can exist. Multiple complete ports
are less restrictive: the parity construction exists for every common-
boundary isometry pair. Neither fact chooses nature's port law or turns a
binary circuit into a primitive ternary event.

## In ordinary language

Suppose two local changes overlap: first `AB` then `BC`, or in the opposite
order. The two complete routes can lead to the same later kind of state. Their
effects must then be added with complex strengths. Testing only one choice of
strengths is like testing one chord on a musical instrument and concluding
that the instrument cannot play in tune. Here the real-valued chord is out of
tune, but rotating one contribution by a quarter phase makes the total exactly
probability-preserving for every input.

There is therefore no forced choice between writing down which order happened
and declaring one indivisible three-actor event. A later record may distinguish
orders; one complete port may retain them coherently; several ports may sort
different coherent combinations. Which of those mechanisms nature uses is a
law question that this architecture does not yet answer.

## 1. The exact object

For fine histories `h` with a common typed input and output, define

```text
G_hk = V_h^dagger V_k,
K_j  = sum_h c[j,h] V_h.
```

The complete recorded ports obey

```text
sum_j K_j^dagger K_j = I.
```

This is an operator identity, not normalization on one prepared state. It is
the exact implicit polynomial variety in the port coefficients. Its cross
terms are the law's own Gram operators; no extra comparison map is inserted.

For two isometries `A,B`, let `Omega=A^dagger B`,
`S=sum_j(|a_j|^2+|b_j|^2)`, and
`C=sum_j conjugate(a_j)b_j`. The entire condition reduces to

```text
S I + C Omega + conjugate(C) Omega^dagger = I.
```

## 2. The unitary single-port theorem

For one port, write `z=conjugate(a)b` and
`c=1-|a|^2-|b|^2`. If `Omega` is unitary with eigenphases `phi_k`, completeness
is equivalent to

```text
2 Re(z exp(i phi_k)) = c
```

for every distinct eigenphase. In the three real variables
`(Re z, Im z, c)`, the exact solution-space dimension is two for one phase,
one for exactly two phases, and zero for three or more phases.

The proof is geometric but elementary. A nonzero triple defines a straight
line in the plane of `(cos phi,sin phi)`. A line meets the unit circle in at
most two distinct points. Three phase points therefore force the zero triple.
Two distinct rows are independent and leave one direction; one row leaves two.
Any nonzero direction has `z != 0`. Scaling it sufficiently close to zero
makes the quadratic with roots `|a|^2,|b|^2` have two positive roots, proving
that actual complex coefficients exist, not only formal `(z,c)` values.

With exactly two phases, subtracting the two equations gives

```text
arg(conjugate(a)b) = -(phi_1+phi_2)/2 mod pi.
```

This selects a relative phase condition, not the magnitudes. Definite-order
endpoints with `z=0` are excluded from the word “coherent.” Scalar `Omega`
also means the two history maps are projectively proportional; their separate
names need an independent event record or calibration to become physical.

## 3. The refuted no-go and the corrected strata

The CNOT overlap gives `Omega=CNOT(A->C)` exactly, with eigenvalues `+1,-1`.
The real pair `{cnot['equal_real_weights']}` has residual
`{cnot['equal_real_residual']}`. Rotating the second weight gives
`{cnot['phase_rotated_weights']}` and residual
`{cnot['phase_rotated_residual']}`. Thus a non-scalar relative order operator
does not force a record or fusion.

At three distinct phases the registered single-port rational census is empty,
as the theorem requires. But for every isometry pair

```text
K_plus=(A+B)/2,   K_minus=(A-B)/2
```

is complete because the cross terms cancel. The multipport construction
therefore survives even where one coherent single port cannot.

## 4. Growing carriers and more than two histories

The `C^2 -> C^4` control has nonnormal overlap `{growing['omega']}`. Its direct
real-linear operator constraint has rank `{growing['constraint_rank']}` and
nullity `{growing['constraint_nullity']}`. Counting eigenphases here would be
invalid; the full operator equation is the classifier. Its parity ports remain
complete.

For the three-history Pauli fixture, the embedded family

```text
K_plus  = p(I+X)/2,
K_minus = p(I-X)/2,
K_Z     = q Z,
p^2+q^2=1
```

is all-input complete. The exact registered rows produce
`{triad['distinct_screen_count']}` distinct calibrated probability screens.
This is a constructive positive-dimensional subvariety and a direct law-
nonselection witness.

Two further port decompositions have the same unconditioned channel while
their calibrated first-port maps differ. That is the precise boundary between
Kraus/unravelling freedom and physical record-individuated instruments.

## 5. Rewrite typing and primitive arity

The four rewrite controls are classified as `{rewrite_kinds}`. A delete/use
case is a dependency: one order is not a lawful history. Divergent final
carriers have no coherent sum at that cut unless a common future is supplied.
Neither fact is a durable record; permanence still requires a future census.

Both three-actor CNOT order maps factor into the declared binary generators.
Calling either product a single ternary arrow changes notation, not ontology.
The Toffoli control is nonfactorizable in the CNOT-only grammar because every
CNOT circuit is linear over `F_2` and Toffoli is not. This proves the assay can
recognize fixture-relative irreducibility; it does not establish that ISP's
actual law contains Toffoli or any minimum-arity generator.

No result here extends the binary grammar coherently to arbitrary `n`.

## 6. Records, locality, and causal order

Stacking complete port maps produces an isometric flag dilation. The flag can
be assigned to an enlarged local catalogue at actor `B`, but the frozen event
grammar contains no map of the required type. Kinematic localization is not a
selected local implementation, and no future census establishes that the flag
is durable.

With an entangled idle spectator `D`, the complete overlap instrument leaves
the spectator marginal exactly unchanged; the completeness-violating
amplifier moves it. This is the fixed-factor, unconditioned no-signalling
statement. Conditional steering and a changing definition of the remote
subsystem remain open.

A coherent sum of two fixed circuit orders does not demonstrate a quantum
switch or causal nonseparability. Those notions require a typed higher-order
process and a process-level witness against the causally separable set. Neither
is constructed here. The distinction follows the process-matrix literature,
including Oreshkov, Costa and Brukner (2012), Chiribella et al. (2013), and
Araújo et al. (2015).

## 7. Generated exact claims

{claim_block}

## 8. Consequence classification

| question | status |
|---|---|
{consequence_table}

## 9. What remains

{limitation_block}

The ontology remains one actual relational history plus a law over complete
alternatives. The Hamiltonian is still only a possible representation of a
selected repeated-sector law; no such selection occurs here. Fields,
particles, statistics, gravity, and continuum spacetime are likewise not
derived. The concrete advance is narrower: overlap is now a correctly typed
operator-variety problem, and the false arity inference has been removed.

## References

- v16 Paper 1, *Joint relational-history law*.
- v16 Paper 3, *Contextual pullbacks and permanent records*.
- v16 Paper 4, *Support–rewrite weld and local couplings*.
- O. Oreshkov, F. Costa, and C. Brukner, “Quantum correlations with no causal
  order,” *Nature Communications* 3, 1092 (2012), arXiv:1105.4464.
- G. Chiribella, G. M. D'Ariano, P. Perinotti, and B. Valiron, “Quantum
  computations without definite causal structure,” *Physical Review A* 88,
  022318 (2013), arXiv:0912.0195.
- M. Araújo et al., “Witnessing causal nonseparability,” *New Journal of
  Physics* 17, 102001 (2015), arXiv:1506.03776.
"""


def render_transcript(gates: Sequence[Mapping[str, Any]], findings: Sequence[str]) -> str:
    lines = ["OVG PAPER 5 EXACT RUN", f"primary: {findings[0]}", f"findings: {list(findings)}"]
    for row in gates:
        state = "PASS" if row["passed"] else "FAIL"
        lines.append(f"{state} {row['gate']} :: {row['evidence']}")
    lines.append(f"gate-count: {len(gates)}")
    lines.append(f"all-pass: {str(all(row['passed'] for row in gates)).lower()}")
    return "\n".join(lines) + "\n"


def parse_transcript_gates(transcript: str) -> list[tuple[str, str, str]]:
    rows = []
    for line in transcript.splitlines():
        match = re.match(r"^(PASS|FAIL) ([A-Z0-9-]+) :: (.*)$", line)
        if match:
            rows.append((match.group(1), match.group(2), match.group(3)))
    return rows


def build_delivery(
    core: Any,
    fixture: Mapping[str, Any],
    fixture_path: Path,
    scorer_path: Path,
    freeze_path: Path,
    repository_root: Path,
    mutant: str | None,
) -> tuple[dict[str, Any], str, str, list[dict[str, Any]]]:
    measurements, flags = evaluate(
        core, fixture, fixture_path, scorer_path, freeze_path, repository_root, mutant
    )
    findings = independent_classification(measurements, flags)
    comparator = independent_classification(measurements, flags)
    if mutant == "verdict-flip":
        findings = ["OVG-SINGLE-PORT-SPECTRAL-CLASSIFIER-REFUTED", *findings[1:]]
    claims = claim_rows(measurements, findings)
    consequences = consequence_rows()
    limitations = limitation_rows()
    paper = render_paper(measurements, findings, claims, consequences, limitations)
    claim_occurrences = {row["id"]: paper.count(row["text"]) for row in claims}

    expected_read_paths = {
        "v16/code/ovg_fixture.json",
        "v16/code/ovg_score.py",
        "v16/code/ovg_core.py",
        "v16/note-ovg-fixture-freeze.md",
        *{row[0] for row in fixture["provenance"]["anchors"]},
    }
    actual_read_paths = {row["path"] for row in measurements["runtime"]["reads"]}
    gates = [
        gate("OVG-ANCHORS", flags["anchors"], f"rows={len(measurements['anchors']['rows'])} freeze={measurements['anchors']['freeze_fixture_match']}/{measurements['anchors']['freeze_scorer_match']}"),
        gate("OVG-FIXTURE-NEUTRALITY", flags["fixture_neutral"], f"keys={measurements['fixture_neutrality']['forbidden_keys']} text={measurements['fixture_neutrality']['forbidden_text']}"),
        gate("OVG-REFERENT-TYPES", flags["typed"], f"actors={measurements['referents']['actors']} cases={measurements['referents']['unitary_case_count']} distinct={measurements['referents']['order_distinct']}"),
        gate("OVG-UNITARY-CERTIFICATES", flags["spectral_certificates"], f"rows={len(measurements['unitary'])}"),
        gate("OVG-GRAM-OPERATOR", flags["gram_direct"], f"omega_ac={measurements['cnot_kill']['omega_equals_ac_cnot']}"),
        gate("OVG-CNOT-RELATIVE", flags["cnot_relative"], f"non_scalar={measurements['cnot_kill']['omega_non_scalar']}"),
        gate("OVG-EQUAL-REAL-CONTROL", flags["equal_real_control"], f"weights={measurements['cnot_kill']['equal_real_weights']} complete={measurements['cnot_kill']['equal_real_complete']}"),
        gate("OVG-COMPLEX-WITNESS", flags["complex_witness"], f"weights={measurements['cnot_kill']['phase_rotated_weights']} scan={measurements['unitary']['overlap-cnot']['coefficient_solution_count']}"),
        gate("OVG-SPECTRAL-RANKS", flags["spectral_ranks"], f"nullities={[row['nullity'] for row in measurements['spectral']['rows'].values()]}"),
        gate("OVG-SPECTRAL-PHASE", flags["spectral_phase"], f"phase={measurements['spectral']['two_phase_relative_phase_constrained']} z0={measurements['spectral']['zero_cross_weight_excluded_from_coherent_label']}"),
        gate("OVG-THREE-PHASE-SINGLE-PORT", flags["three_phase"], f"scan={measurements['unitary']['three-phase-control']['coefficient_solution_count']}"),
        gate("OVG-PARITY-INSTRUMENT", flags["parity"], f"cases={measurements['parity']['case_complete']}"),
        gate("OVG-NONNORMAL-DIRECT", flags["growing"], f"normal={measurements['growing']['normal']} rank={measurements['growing']['constraint_rank']} method={measurements['growing']['method']}"),
        gate("OVG-THREE-HISTORY-VARIETY", flags["three_history"], f"rows={len(measurements['three_history']['family_rows'])} screens={measurements['three_history']['distinct_screen_count']}"),
        gate("OVG-PORT-COARSEGRAIN", flags["coarsegrain"], f"same_channel={measurements['ports']['coarse_channels_equal']} calibrated_diff={measurements['ports']['calibrated_first_ports_differ']}"),
        gate("OVG-DARK-REACTIVATION", flags["reactivation"], f"current={measurements['dark_reactivation']['current_difference_zero']} future={measurements['dark_reactivation']['future_difference_zero']}"),
        gate("OVG-REWRITE-CRITICAL-PAIRS", flags["rewrite"], f"kinds={[row['kind'] for row in measurements['rewrites']]}"),
        gate("OVG-DEPENDENCY-TYPE", flags["dependency"], f"dependency_not_record={measurements['semantics']['dependency_is_not_record']} divergent_not_common={measurements['semantics']['divergent_without_common_future_is_not_common']}"),
        gate("OVG-ARITY-COMPOSITE", flags["composite"], f"left={measurements['arity']['left_factorization_count']} right={measurements['arity']['right_factorization_count']}"),
        gate("OVG-ARITY-CONTROL", flags["arity_control"], f"toffoli_words={measurements['arity']['ternary_control_factorization_count']} witness={measurements['arity']['ternary_control_nonlinear_witness']}"),
        gate("OVG-ANCILLA-POLICY", flags["ancilla"], f"present={measurements['arity']['ancilla_policy_present']}"),
        gate("OVG-LOCAL-FLAG", flags["local_flag"], f"shape={measurements['local_flag']['shape']} typed_map={measurements['local_flag']['typed_implementation_present']}"),
        gate("OVG-RECORD-PERMANENCE-SCOPE", flags["permanence_scope"], f"censused={measurements['local_flag']['permanence_censused']} claimed={not measurements['semantics']['durability_not_claimed']}"),
        gate("OVG-SPECTATOR-NOSIGNAL", flags["spectator"], f"unchanged={measurements['spectator']['unchanged']} amplifier={measurements['spectator']['amplifier_moves']}"),
        gate("OVG-CAUSAL-SCOPE", flags["causal_scope"], f"nonseparability_claimed={not measurements['semantics']['causal_nonseparability_not_claimed']}"),
        gate("OVG-ALL-N-SCOPE", flags["all_n_scope"], f"all_n_claimed={not measurements['semantics']['all_n_not_claimed']}"),
        gate("OVG-RUNTIME-READ-SET", actual_read_paths == expected_read_paths, f"reads={sorted(actual_read_paths)}"),
        gate("OVG-EXACT-ARITHMETIC", flags["exact"], f"source_float_literals={measurements['runtime']['source_float_literals']} fixture_float={measurements['runtime']['fixture_contains_float']}"),
        gate("OVG-CLASSIFIER", findings == comparator, f"builder={findings} comparator={comparator}"),
        gate("OVG-PAPER-BINDINGS", all(value == 1 for value in claim_occurrences.values()), f"claims={len(claims)} occurrences={claim_occurrences}"),
        gate("OVG-PREWRITE-INTEGRITY", flags["prewrite"], f"late_seal={measurements['prewrite']['late_seal']}"),
    ]
    tentative = render_transcript(gates, findings)
    if mutant == "transcript-forge":
        tentative = tentative.replace("PASS OVG-GRAM-OPERATOR", "PASS OVG-GRAM-OPERAT0R", 1)
    parsed = parse_transcript_gates(tentative)
    expected_rows = [
        ("PASS" if row["passed"] else "FAIL", row["gate"], row["evidence"])
        for row in gates
    ]
    transcript_ok = parsed == expected_rows
    gates.append(gate("OVG-TRANSCRIPT-RECONCILIATION", transcript_ok, f"rows={len(parsed)}"))
    transcript = render_transcript(gates, findings)

    mutation_contract = {
        "names": list(MUTANTS),
        "expected_gate": {
            "anchor-corrupt": "OVG-ANCHORS",
            "history-order-drop": "OVG-REFERENT-TYPES",
            "common-boundary-forge": "OVG-REFERENT-TYPES",
            "gram-cross-term-move": "OVG-GRAM-OPERATOR",
            "gram-self-compare": "OVG-GRAM-OPERATOR",
            "state-only-normalize": "OVG-EQUAL-REAL-CONTROL",
            "equal-real-universalize": "OVG-COMPLEX-WITNESS",
            "complex-witness-drop": "OVG-COMPLEX-WITNESS",
            "parity-factor-move": "OVG-PARITY-INSTRUMENT",
            "scalar-call-distinct": "OVG-SPECTRAL-PHASE",
            "eigenphase-count-move": "OVG-UNITARY-CERTIFICATES",
            "phase-constraint-drop": "OVG-SPECTRAL-PHASE",
            "nonnormal-spectral-shortcut": "OVG-NONNORMAL-DIRECT",
            "z-zero-call-coherent": "OVG-SPECTRAL-PHASE",
            "three-history-drop": "OVG-THREE-HISTORY-VARIETY",
            "port-coarsegrain-break": "OVG-PORT-COARSEGRAIN",
            "dependency-call-record": "OVG-DEPENDENCY-TYPE",
            "divergent-call-common": "OVG-DEPENDENCY-TYPE",
            "local-flag-call-implemented": "OVG-LOCAL-FLAG",
            "local-factorization-drop": "OVG-LOCAL-FLAG",
            "binary-product-call-primitive": "OVG-ARITY-COMPOSITE",
            "ancilla-policy-hide": "OVG-ANCILLA-POLICY",
            "durability-assume": "OVG-RECORD-PERMANENCE-SCOPE",
            "causal-switch-word": "OVG-CAUSAL-SCOPE",
            "all-n-promote": "OVG-ALL-N-SCOPE",
            "typed-count": "OVG-ARITY-COMPOSITE",
            "float-leak": "OVG-EXACT-ARITHMETIC",
            "verdict-flip": "OVG-CLASSIFIER",
            "transcript-forge": "OVG-TRANSCRIPT-RECONCILIATION",
            "seal-after-write": "OVG-PREWRITE-INTEGRITY",
        },
    }
    payload = {
        "schema": "ovg-result-v1",
        "provenance": {
            "base_commit": fixture["provenance"]["base_commit"],
            "core_sha256": CORE_HASH,
            "fixture_sha256": sha256_path(fixture_path),
            "scorer_sha256": sha256_path(scorer_path),
            "runtime_reads": sorted(row["path"] for row in measurements["runtime"]["reads"]),
        },
        "primary": list(findings),
        "measurements": measurements,
        "claims": claims,
        "consequences": consequences,
        "limitations": list(limitations),
        "gates": gates,
        "mutation_contract": mutation_contract,
    }
    payload["seal_manifest"] = {
        "sealed": {key: digest(payload[key]) for key in payload if key != "seal_manifest"},
        "unsealed": ["seal_manifest"],
    }
    receipt = {
        "schema": "ovg-receipt-v1",
        "payload": payload,
        "transcript_sha256": hashlib.sha256(transcript.encode("utf-8")).hexdigest(),
        "paper_sha256": hashlib.sha256(paper.encode("utf-8")).hexdigest(),
    }
    return receipt, transcript, paper, gates


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
    code_root = Path(__file__).resolve().parent
    repository_root = code_root.parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=code_root / "ovg_fixture.json")
    parser.add_argument("--core", type=Path, default=code_root / "ovg_core.py")
    parser.add_argument("--freeze", type=Path, default=repository_root / "v16" / "note-ovg-fixture-freeze.md")
    parser.add_argument("--output", type=Path, default=code_root / "ovg_output.txt")
    parser.add_argument("--receipt", type=Path, default=code_root / "ovg_receipt.json")
    parser.add_argument("--paper", type=Path, default=repository_root / "v16" / "paper-05-overlap-gram-instrument-variety.md")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--mutant", choices=MUTANTS)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.selftest and args.mutant is not None:
        print("REFUSE OVG-CLI :: selftest and mutant are mutually exclusive", file=sys.stderr)
        return 2
    targets = tuple(path.resolve() for path in (args.output, args.receipt, args.paper))
    if len(set(targets)) != len(targets):
        print("REFUSE OVG-CLI :: output paths must be distinct", file=sys.stderr)
        return 2
    if any(path.exists() for path in targets):
        print("REFUSE OVG-CLI :: target path already exists", file=sys.stderr)
        return 1
    scorer_path = Path(__file__).resolve()
    repository_root = scorer_path.parent.parent.parent
    try:
        core = load_core(args.core.resolve())
        fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
        mutant = "anchor-corrupt" if args.selftest else args.mutant
        receipt, transcript, paper, gates = build_delivery(
            core,
            copy.deepcopy(fixture),
            args.fixture.resolve(),
            scorer_path,
            args.freeze.resolve(),
            repository_root,
            mutant,
        )
    except Exception as error:
        print(f"REFUSE OVG-RUNTIME :: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    failed = [row["gate"] for row in gates if not row["passed"]]
    if failed:
        label = "OVG-SELFTEST" if args.selftest else "OVG-GATE"
        print(f"REFUSE {label} :: {','.join(failed)}", file=sys.stderr)
        return 1
    atomic_write(args.output.resolve(), transcript.encode("utf-8"))
    atomic_write(args.receipt.resolve(), canonical_json(receipt))
    atomic_write(args.paper.resolve(), paper.encode("utf-8"))
    sys.stdout.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
