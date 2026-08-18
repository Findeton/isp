#!/usr/bin/env python3
"""Score the frozen CEL Paper 7 fixture and render sealed candidate artifacts.

The scorer is verdict-neutral: it measures four separately typed surfaces and
derives the registered primary word from their conjunction.  It writes only
after every scientific and integrity gate passes.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import os
import sys
import tempfile
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

import cel_core as core


Q = Fraction
Matrix = core.Matrix
QMatrix = core.QMatrix

PRIMARY_WORDS = (
    "CEL-CREATION-EVENT-LAYER-CONSTRUCTED-BUT-COUPLINGS-AND-CATALOGUE-UNSELECTED",
    "CEL-MATHEMATICAL-LADDER-CONSTRUCTED-BUT-RELATIONAL-FLAG-WELD-UNBUILT",
    "CEL-RECOVERABILITY-CRITERION-REFUTED",
    "CEL-EXACT-RESOURCE-THEOREM-REFUTED",
    "CEL-INCONSISTENT",
)

QUALIFIER_WORDS = (
    "RECURRENCE-PROPAGATED-BY-NATURALITY-SYMMETRY-AND-GLUING",
    "TOKEN-DISJOINT-UNIVERSALITY-POSTULATE-PRICED",
    "KERNEL-IDENTITY-ONLY-MODULO-OPERATIONAL-NULL",
    "BARE-ALGEBRA-COVARIANCE-NOT-PERMANENCE",
    "CONTINUATION-STABLE-LICENSED-RECOVERABILITY-CONSTRUCTED",
    "REDUNDANCY-SURVIVES-LOCAL-ERASURE-BUT-REMAINS-GRAMMAR-RELATIVE",
    "PORT-FIBER-RETYPED-AS-CREATION-COUPLING-DATA",
    "FLAG-DILATION-WELDED-BUT-ACTUALIZATION-UNBUILT",
    "GAUSSIAN-RATIONAL-REALIZATION-BOUND-PROVED",
    "NUMBER-FIELD-PRICES-MINIMAL-RESOURCES-NOT-REALIZABILITY",
    "COUPLINGS-CATALOGUE-AND-FUNDAMENTAL-DYNAMICS-UNSELECTED",
)

MUTANTS = (
    "anchor-hash",
    "anchor-token",
    "history-typing",
    "kernel-entry",
    "spectator-naturality",
    "operational-null",
    "exchange-licence",
    "shared-restriction",
    "shared-negative-control",
    "universality-dimension",
    "universality-postulate",
    "reset-kraus",
    "covariance-as-permanence",
    "relabeling",
    "writer-involution",
    "copy-support",
    "all-word-grammar",
    "catalogue-enlargement",
    "branch-label",
    "recovery-licence",
    "jcv-coefficient",
    "dilation-isometry",
    "post-catalogue",
    "flag-attachment",
    "support-direction",
    "calibrated-statistic",
    "anonymous-classification",
    "dilation-durability",
    "scalar-obstruction",
    "three-row-witness",
    "ldl-reconstruction",
    "row-bound",
    "psd-refusal",
    "some-vs-specified",
    "field-ontology",
    "actualization",
    "all-n",
    "exact-arithmetic",
    "primary-comparator",
    "transcript-binding",
    "prewrite-seal",
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest(value: Any) -> str:
    return sha256_bytes(canonical_json(value))


def exact_scalar(value: Any) -> core.GQ:
    if isinstance(value, bool):
        raise TypeError("booleans are not exact scalars")
    if isinstance(value, int):
        return core.GQ(value)
    if isinstance(value, str):
        return core.GQ(Q(value))
    if isinstance(value, Mapping) and set(value) == {"re", "im"}:
        return core.GQ(Q(value["re"]), Q(value["im"]))
    raise TypeError(f"untyped exact scalar {value!r}")


def exact_fraction(value: Any) -> Q:
    scalar = exact_scalar(value)
    if scalar.im != 0:
        raise TypeError("expected a real exact scalar")
    return scalar.re


def exact_matrix(value: Sequence[Sequence[Any]]) -> Matrix:
    return core.matrix([[exact_scalar(entry) for entry in row] for row in value])


def exact_qmatrix(value: Sequence[Sequence[Any]]) -> QMatrix:
    return core.qmatrix([[exact_fraction(entry) for entry in row] for row in value])


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


def bits_to_index(bits: Sequence[int]) -> int:
    result = 0
    for bit in bits:
        if bit not in (0, 1):
            raise ValueError("basis bits must be binary")
        result = 2 * result + bit
    return result


def index_to_bits(index: int, count: int) -> tuple[int, ...]:
    return tuple((index >> (count - position - 1)) & 1 for position in range(count))


def cnot_matrix(bit_count: int, control: int, target: int) -> Matrix:
    if control == target or min(control, target) < 0 or max(control, target) >= bit_count:
        raise ValueError("ill-typed CNOT")
    dimension = 1 << bit_count
    rows = [[core.ZERO for _ in range(dimension)] for _ in range(dimension)]
    for source in range(dimension):
        bits = list(index_to_bits(source, bit_count))
        if bits[control] == 1:
            bits[target] ^= 1
        rows[bits_to_index(bits)][source] = core.ONE
    return tuple(tuple(row) for row in rows)


def q_from_matrix(value: Matrix) -> QMatrix:
    rows, columns = core.shape(value)
    result: list[list[Q]] = []
    for row in range(rows):
        line: list[Q] = []
        for column in range(columns):
            if value[row][column].im != 0:
                raise TypeError("classical transition has a non-real entry")
            line.append(value[row][column].re)
        result.append(line)
    return core.qmatrix(result)


def compose_named_history(events: Mapping[str, Matrix], order: Sequence[str]) -> Matrix:
    if not order:
        raise ValueError("empty history order")
    dimension = core.shape(next(iter(events.values())))[0]
    result = core.identity(dimension)
    for name in order:
        result = core.matmul(events[name], result)
    return result


def basis_density(bits: Sequence[int]) -> Matrix:
    dimension = 1 << len(bits)
    index = bits_to_index(bits)
    return core.matrix_unit(dimension, index, index)


def probability(state: Matrix, projector: Matrix) -> Q:
    value = core.trace(core.matmul(projector, state))
    if value.im != 0:
        raise ArithmeticError("probability acquired an imaginary part")
    return value.re


def permutation_from_list(images: Sequence[int]) -> Matrix:
    size = len(images)
    if sorted(images) != list(range(size)):
        raise ValueError("invalid permutation list")
    return tuple(
        tuple(core.ONE if row == images[column] else core.ZERO for column in range(size))
        for row in range(size)
    )


def flag_readout(bit_count: int, bit: int) -> QMatrix:
    dimension = 1 << bit_count
    rows = [[Q(0) for _ in range(dimension)] for _ in range(2)]
    for source in range(dimension):
        rows[index_to_bits(source, bit_count)[bit]][source] = Q(1)
    return core.qmatrix(rows)


def record_encoding(bit_count: int, source_bit: int, writers: Sequence[Mapping[str, int]]) -> QMatrix:
    dimension = 1 << bit_count
    columns: list[list[Q]] = [[Q(0), Q(0)] for _ in range(dimension)]
    operators = [cnot_matrix(bit_count, item["control"], item["target"]) for item in writers]
    total = core.identity(dimension)
    for operator in operators:
        total = core.matmul(operator, total)
    for record in (0, 1):
        bits = [0 for _ in range(bit_count)]
        bits[source_bit] = record
        initial = bits_to_index(bits)
        target = next(row for row in range(dimension) if total[row][initial] == core.ONE)
        columns[target][record] = Q(1)
    return core.qmatrix(columns)


def exact_identity_recovery(
    encoded: QMatrix,
    readouts: Sequence[QMatrix],
    licensed_sector_relabelings: Sequence[QMatrix],
) -> bool:
    recovered = [core.qmul(readout, encoded) for readout in readouts]
    return any(value in licensed_sector_relabelings for value in recovered)


def support(value: Matrix) -> set[tuple[int, int]]:
    rows, columns = core.shape(value)
    return {
        (row, column)
        for row in range(rows)
        for column in range(columns)
        if value[row][column] != core.ZERO
    }


def gate(name: str, passed: bool, evidence: str, group: str) -> dict[str, Any]:
    return {"gate": name, "group": group, "passed": bool(passed), "evidence": evidence}


def apply_mutant(data: dict[str, Any], mutant: str | None) -> set[str]:
    faults: set[str] = set()
    if mutant is None:
        return faults
    if mutant == "anchor-hash":
        data["anchors"][0]["sha256"] = "0" * 64
    elif mutant == "anchor-token":
        data["anchors"][0]["tokens"][0] = "MUTATED-ABSENT-TOKEN"
    elif mutant == "history-typing":
        data["recurrence"]["overlap"]["events"]["AB"]["target"] = 0
    elif mutant == "kernel-entry":
        data["recurrence"]["overlap"]["kernels"]["biased"][0][0] = "15/25"
    elif mutant == "spectator-naturality":
        data["recurrence"]["overlap"]["spectator_naturality_is_licensed"] = False
    elif mutant == "operational-null":
        data["recurrence"]["nonfaithful"]["kernels"]["right"][0][1] = "1/3"
        data["recurrence"]["nonfaithful"]["kernels"]["right"][1][0] = "1/3"
    elif mutant == "exchange-licence":
        data["recurrence"]["overlap"]["exchange_automorphism_is_licensed"] = False
    elif mutant == "shared-restriction":
        data["recurrence"]["gluing"]["right_local"][0] = "2/5"
    elif mutant == "shared-negative-control":
        data["recurrence"]["gluing"]["right_mismatch"][0] = "3/5"
    elif mutant == "universality-dimension":
        data["recurrence"]["universality_constraints"]["universal"] = [["0", "0"]]
    elif mutant == "universality-postulate":
        data["recurrence"]["type_universality_is_postulate"] = False
    elif mutant == "reset-kraus":
        data["records"]["reset"]["kraus"][1] = [["0", "0"], ["0", "1"]]
    elif mutant == "covariance-as-permanence":
        faults.add("covariance-as-permanence")
    elif mutant == "relabeling":
        data["records"]["relabel"]["unitary"] = [["1", "0"], ["0", "1"]]
        data["records"]["relabel"]["classical"] = [["1", "0"], ["0", "1"]]
    elif mutant == "writer-involution":
        faults.add("writer-involution")
    elif mutant == "copy-support":
        data["records"]["two_copy"]["writers"][1] = copy.deepcopy(
            data["records"]["two_copy"]["writers"][0]
        )
    elif mutant == "all-word-grammar":
        data["records"]["two_copy"]["positive_generators"] = [0, 1]
    elif mutant == "catalogue-enlargement":
        data["records"]["two_copy"]["enlarged_generators"] = [0]
    elif mutant == "branch-label":
        data["records"]["branch_instrument"]["weights"] = ["1", "0"]
    elif mutant == "recovery-licence":
        data["records"]["licence_control"]["licensed_sector_relabelings"].append(
            [["0", "1"], ["1", "0"]]
        )
    elif mutant in ("jcv-coefficient", "dilation-isometry"):
        data["dilation"]["coefficient_families"]["second"][0][0] = "15/25"
    elif mutant == "post-catalogue":
        data["dilation"]["post_catalogue_flag_major"].pop()
    elif mutant == "flag-attachment":
        data["dilation"]["rewrite"]["attachment"] = ["flag", "flag"]
    elif mutant == "support-direction":
        data["dilation"]["allowed_support"].pop()
    elif mutant == "calibrated-statistic":
        faults.add("calibrated-statistic")
    elif mutant == "anonymous-classification":
        data["dilation"]["anonymous_control"]["has_named_attachment"] = True
    elif mutant == "dilation-durability":
        data["dilation"]["continuations"]["erasing"] = [["1", "0"], ["0", "1"]]
    elif mutant == "scalar-obstruction":
        data["resources"]["scalar"] = "5/4"
    elif mutant == "three-row-witness":
        data["resources"]["rank_two_three_row_factor"][1][0] = "2/5"
    elif mutant == "ldl-reconstruction":
        faults.add("ldl-reconstruction")
    elif mutant == "row-bound":
        faults.add("row-bound")
    elif mutant == "psd-refusal":
        data["resources"]["non_psd"] = [["1", "0"], ["0", "1"]]
    elif mutant == "some-vs-specified":
        faults.add("some-vs-specified")
    elif mutant == "field-ontology":
        data["resources"]["field_role"] = "ontological number field"
    elif mutant == "actualization":
        data["scope_walls"].remove("actualization")
    elif mutant == "all-n":
        data["scope_walls"].remove("arbitrary-n composition")
    elif mutant == "exact-arithmetic":
        data["resources"]["scalar"] = float("1.4")
    elif mutant in ("primary-comparator", "transcript-binding", "prewrite-seal"):
        faults.add(mutant)
    else:
        raise ValueError(f"unknown mutant {mutant}")
    return faults


def verify_anchors(root: Path, anchors: Sequence[Mapping[str, Any]]) -> tuple[bool, list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    passed = True
    for anchor in anchors:
        path = root / anchor["path"]
        payload = path.read_bytes()
        text = payload.decode("utf-8")
        actual = sha256_bytes(payload)
        tokens = {token: token in text for token in anchor["tokens"]}
        row_pass = actual == anchor["sha256"] and all(tokens.values())
        passed = passed and row_pass
        rows.append(
            {
                "path": anchor["path"],
                "declared_sha256": anchor["sha256"],
                "actual_sha256": actual,
                "tokens": tokens,
                "passed": row_pass,
            }
        )
    return passed, rows


def score(data: dict[str, Any], fixture_bytes: bytes, root: Path, faults: set[str]) -> dict[str, Any]:
    gates: list[dict[str, Any]] = []
    anchor_ok, anchor_rows = verify_anchors(root, data["anchors"])
    forbidden_keys = {"expected", "verdict", "pass_count", "solution_dimension", "selected_witness"}
    fixture_keys = key_census(data)
    scorer_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    scorer_float_literals = [
        node.value
        for node in ast.walk(scorer_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    ]
    core_hash = sha256_bytes((root / "v16/code/cel_core.py").read_bytes())
    gates.extend(
        [
            gate("CEL-ANCHORS", anchor_ok, f"anchors={len(anchor_rows)}", "integrity"),
            gate(
                "CEL-FIXTURE-DATA-ONLY",
                not contains_float(data) and not (fixture_keys & forbidden_keys),
                f"floats={contains_float(data)} forbidden={sorted(fixture_keys & forbidden_keys)}",
                "integrity",
            ),
            gate(
                "CEL-CORE-FROZEN",
                core_hash == "f08b880095e71ac79082d2672ec849dc9ffd1ab66c702a85f2b24165a02aedac",
                f"sha256={core_hash}",
                "integrity",
            ),
            gate(
                "CEL-EXACT-SOURCE",
                not scorer_float_literals and "exact calculation convention" in data["resources"]["field_role"],
                f"scorer-float-literals={len(scorer_float_literals)}",
                "integrity",
            ),
        ]
    )

    # Recurrence ladder.
    recurrence = data["recurrence"]
    overlap = recurrence["overlap"]
    bit_count = len(overlap["actors"])
    events = {
        name: cnot_matrix(bit_count, specification["control"], specification["target"])
        for name, specification in overlap["events"].items()
    }
    histories = tuple(compose_named_history(events, order) for order in overlap["history_orders"])
    history_typed = all(core.shape(history) == (1 << bit_count, 1 << bit_count) for history in histories)
    kernels = {name: exact_matrix(value) for name, value in overlap["kernels"].items()}
    input_state = basis_density(overlap["input_bits"])
    screen = basis_density(overlap["screen_bits"])
    outputs = {name: core.apply_channel_kernel(histories, kernel, input_state) for name, kernel in kernels.items()}
    screen_probabilities = {name: probability(output, screen) for name, output in outputs.items()}
    completeness = {
        name: core.completeness_from_kernel(histories, kernel) for name, kernel in kernels.items()
    }
    gates.append(
        gate(
            "CEL-HISTORY-EVENT-TYPING",
            history_typed and histories[0] != histories[1],
            f"dimension={1 << bit_count} histories-distinct={histories[0] != histories[1]}",
            "recurrence",
        )
    )
    gates.append(
        gate(
            "CEL-R1-LOCAL-SURFACE-NONSELECTION",
            all(value == core.identity(1 << bit_count) for value in completeness.values())
            and screen_probabilities["biased"] != screen_probabilities["balanced"],
            f"screens={core.qtext(screen_probabilities['biased'])},{core.qtext(screen_probabilities['balanced'])}",
            "recurrence",
        )
    )
    spectator_identity = core.identity(len(overlap["idle_actor_state"]))
    dressed_histories = tuple(core.kron(history, spectator_identity) for history in histories)
    idle_state = core.matrix(
        [
            [overlap["idle_actor_state"][row] * overlap["idle_actor_state"][column] for column in range(2)]
            for row in range(2)
        ]
    )
    dressed_input = core.kron(input_state, idle_state)
    dressed_screen = core.kron(screen, spectator_identity)
    dressed_probabilities = {
        name: probability(core.apply_channel_kernel(dressed_histories, kernel, dressed_input), dressed_screen)
        for name, kernel in kernels.items()
    }
    dressed_completeness = {
        name: core.completeness_from_kernel(dressed_histories, kernel) for name, kernel in kernels.items()
    }
    gates.append(
        gate(
            "CEL-R2-COMPLETENESS-DOES-NOT-FORCE-SPECTATOR-RECURRENCE",
            dressed_completeness["balanced"] == core.identity(16)
            and dressed_probabilities["balanced"] == screen_probabilities["balanced"],
            f"balanced-dressed={core.qtext(dressed_probabilities['balanced'])}",
            "recurrence",
        )
    )
    gates.append(
        gate(
            "CEL-R3-LICENSED-SPECTATOR-NATURALITY",
            overlap["spectator_naturality_is_licensed"]
            and dressed_probabilities["biased"] == screen_probabilities["biased"],
            f"licensed={overlap['spectator_naturality_is_licensed']} restriction={core.qtext(dressed_probabilities['biased'])}",
            "recurrence",
        )
    )
    nonfaithful = recurrence["nonfaithful"]
    nonfaithful_histories = (core.identity(nonfaithful["history_dimension"]),) * 2
    null_kernels = {name: exact_matrix(value) for name, value in nonfaithful["kernels"].items()}
    null_signatures = {
        name: core.channel_signature(nonfaithful_histories, kernel) for name, kernel in null_kernels.items()
    }
    null_complete = {
        name: core.completeness_from_kernel(nonfaithful_histories, kernel)
        for name, kernel in null_kernels.items()
    }
    gates.append(
        gate(
            "CEL-R4-OPERATIONAL-NULL-QUOTIENT",
            null_kernels["left"] != null_kernels["right"]
            and null_signatures["left"] == null_signatures["right"]
            and all(value == core.identity(nonfaithful["history_dimension"]) for value in null_complete.values()),
            f"raw-equal={null_kernels['left'] == null_kernels['right']} channel-equal={null_signatures['left'] == null_signatures['right']}",
            "recurrence",
        )
    )
    history_swap = core.matrix([[0, 1], [1, 0]])
    exchange_fixed = {
        name: core.matmul(core.matmul(core.adjoint(history_swap), kernel), history_swap) == kernel
        for name, kernel in kernels.items()
    }
    gates.append(
        gate(
            "CEL-R5-EXCHANGE-SYMMETRY-WITHIN-ORBIT",
            overlap["exchange_automorphism_is_licensed"]
            and not exchange_fixed["biased"]
            and exchange_fixed["balanced"],
            f"licensed={overlap['exchange_automorphism_is_licensed']} biased={exchange_fixed['biased']} balanced={exchange_fixed['balanced']}",
            "recurrence",
        )
    )
    gluing = recurrence["gluing"]
    joint = tuple(exact_fraction(value) for value in gluing["joint_values"])
    restrict_left = tuple(joint[index] for index in gluing["left_restriction"])
    restrict_right = tuple(joint[index] for index in gluing["right_restriction"])
    local_left = tuple(exact_fraction(value) for value in gluing["left_local"])
    local_right = tuple(exact_fraction(value) for value in gluing["right_local"])
    mismatch_right = tuple(exact_fraction(value) for value in gluing["right_mismatch"])
    gates.append(
        gate(
            "CEL-R6-SHARED-TOKEN-GLUING",
            restrict_left == local_left and restrict_right == local_right,
            f"left={','.join(core.qtext(v) for v in restrict_left)} right={','.join(core.qtext(v) for v in restrict_right)}",
            "recurrence",
        )
    )
    gates.append(
        gate(
            "CEL-R7-GLUING-MISMATCH-REFUSED",
            restrict_right != mismatch_right,
            f"joint-shared={core.qtext(restrict_right[0])} mismatch={core.qtext(mismatch_right[0])}",
            "recurrence",
        )
    )
    constraints = recurrence["universality_constraints"]
    target = tuple(exact_fraction(value) for value in constraints["target"])
    independent_dimension = core.affine_solution_dimension(exact_qmatrix(constraints["independent"]), target)
    universal_dimension = core.affine_solution_dimension(exact_qmatrix(constraints["universal"]), target)
    gates.append(
        gate(
            "CEL-R8-UNIVERSALITY-PRICE",
            independent_dimension == 2 and universal_dimension == 1,
            f"dimensions={independent_dimension}->{universal_dimension}",
            "recurrence",
        )
    )
    token_sets = [set(tokens) for tokens in recurrence["token_disjoint_contexts"]]
    token_disjoint = token_sets[0].isdisjoint(token_sets[1])
    gates.append(
        gate(
            "CEL-R9-TYPE-UNIVERSALITY-IS-A-POSTULATE",
            token_disjoint and recurrence["type_universality_is_postulate"],
            f"token-disjoint={token_disjoint} postulate={recurrence['type_universality_is_postulate']}",
            "recurrence",
        )
    )

    # Record recoverability.
    records = data["records"]
    reset_kraus = tuple(exact_matrix(value) for value in records["reset"]["kraus"])
    reset_classical = exact_qmatrix(records["reset"]["classical"])
    reset_covariant = core.diagonal_algebra_covariant(reset_kraus)
    reset_recoverable = core.zero_error_recoverable(reset_classical)
    reset_quantum_columns: list[tuple[Q, ...]] = []
    reset_quantum_diagonal = True
    for source in range(2):
        output = core.apply_kraus(reset_kraus, core.matrix_unit(2, source, source))
        reset_quantum_diagonal = reset_quantum_diagonal and output[0][1] == core.ZERO and output[1][0] == core.ZERO
        reset_quantum_columns.append((output[0][0].re, output[1][1].re))
    reset_matches_classical = reset_quantum_diagonal and all(
        reset_quantum_columns[column] == tuple(reset_classical[row][column] for row in range(2))
        for column in range(2)
    )
    gates.append(
        gate(
            "CEL-P1-RESET-KILLS-BARE-COVARIANCE-CRITERION",
            core.is_complete_kraus(reset_kraus)
            and reset_covariant
            and not reset_recoverable
            and reset_matches_classical
            and "covariance-as-permanence" not in faults,
            f"complete={core.is_complete_kraus(reset_kraus)} covariant={reset_covariant} recoverable={reset_recoverable} representations-agree={reset_matches_classical}",
            "records",
        )
    )
    relabel_unitary = exact_matrix(records["relabel"]["unitary"])
    relabel_classical = exact_qmatrix(records["relabel"]["classical"])
    projector_zero = core.matrix_unit(2, 0, 0)
    fixed_projector_commutes = core.matmul(relabel_unitary, projector_zero) == core.matmul(projector_zero, relabel_unitary)
    gates.append(
        gate(
            "CEL-P2-RELABELING-RECOVERS-WITHOUT-FIXED-PROJECTORS",
            core.zero_error_recoverable(relabel_classical)
            and core.is_complete_kraus((relabel_unitary,))
            and not fixed_projector_commutes,
            f"recoverable={core.zero_error_recoverable(relabel_classical)} fixed-projector-commutes={fixed_projector_commutes}",
            "records",
        )
    )
    append = records["append_only"]
    append_certificate = core.all_word_recoverability(
        exact_qmatrix(append["encoding"]),
        tuple(exact_qmatrix(value) for value in append["generators"]),
        tuple(exact_qmatrix(value) for value in append["readouts"]),
    )
    gates.append(
        gate(
            "CEL-P3-APPEND-ONLY-ALL-WORD-CERTIFICATE",
            append_certificate["mathematical_all"] and append_certificate["licensed_all"],
            f"words={append_certificate['word_count']}",
            "records",
        )
    )
    single = records["single_copy"]
    single_bits = len(single["bits"])
    single_encoding = record_encoding(single_bits, single["record_input_bit"], single["writers"])
    single_writer = cnot_matrix(single_bits, single["writers"][0]["control"], single["writers"][0]["target"])
    single_writer_q = q_from_matrix(single_writer)
    single_readout = flag_readout(single_bits, single["flag_readout_bits"][0])
    single_after_refire = core.qmul(single_writer_q, single_encoding)
    single_flag_channel = core.qmul(single_readout, single_after_refire)
    writer_involutive = core.qmul(single_writer_q, single_writer_q) == core.qidentity(1 << single_bits)
    if "writer-involution" in faults:
        writer_involutive = False
    gates.append(
        gate(
            "CEL-P4-INVOLUTIVE-WRITER-IS-ITS-OWN-FLAG-ERASER",
            writer_involutive and not core.zero_error_recoverable(single_flag_channel),
            f"involutive={writer_involutive} flag-recoverable={core.zero_error_recoverable(single_flag_channel)}",
            "records",
        )
    )
    two = records["two_copy"]
    two_bits = len(two["bits"])
    two_encoding = record_encoding(two_bits, two["record_input_bit"], two["writers"])
    two_writers = tuple(
        q_from_matrix(cnot_matrix(two_bits, item["control"], item["target"]))
        for item in two["writers"]
    )
    two_readouts = tuple(flag_readout(two_bits, bit) for bit in two["licensed_readout_bits"])
    after_first_refire = core.qmul(two_writers[0], two_encoding)
    survives_first = core.zero_error_recoverable(core.qmul(two_readouts[1], after_first_refire))
    gates.append(
        gate(
            "CEL-P5-REDUNDANT-COPY-SURVIVES-LOCAL-ERASURE",
            survives_first,
            f"second-copy-recoverable={survives_first}",
            "records",
        )
    )
    positive_generators = tuple(two_writers[index] for index in two["positive_generators"])
    positive_certificate = core.all_word_recoverability(two_encoding, positive_generators, two_readouts)
    gates.append(
        gate(
            "CEL-P6-REDUNDANT-GRAMMAR-ALL-WORD-RECOVERY",
            positive_certificate["mathematical_all"] and positive_certificate["licensed_all"],
            f"words={positive_certificate['word_count']} licensed={positive_certificate['licensed_all']}",
            "records",
        )
    )
    enlarged_generators = tuple(two_writers[index] for index in two["enlarged_generators"])
    enlarged_certificate = core.all_word_recoverability(two_encoding, enlarged_generators, two_readouts)
    gates.append(
        gate(
            "CEL-P7-CATALOGUE-ENLARGEMENT-DEMOTES-PERMANENCE",
            enlarged_certificate["mathematical_all"] and not enlarged_certificate["licensed_all"],
            f"words={enlarged_certificate['word_count']} global={enlarged_certificate['mathematical_all']} flag-licensed={enlarged_certificate['licensed_all']}",
            "records",
        )
    )
    branch = records["branch_instrument"]
    branch_weights = tuple(exact_fraction(value) for value in branch["weights"])
    branch_channels = tuple(exact_qmatrix(value) for value in branch["channels"])
    branch_readouts = tuple(exact_qmatrix(value) for value in branch["branch_readouts"])
    branch_recovery = tuple(
        core.qmul(readout, channel) == core.qidentity(2)
        for readout, channel in zip(branch_readouts, branch_channels)
    )
    coarse_branch = core.coarse_grain_channels(branch_weights, branch_channels)
    gates.append(
        gate(
            "CEL-P8-RETAINED-BRANCH-RECOVERY",
            all(branch_recovery),
            f"branchwise={','.join(str(value).lower() for value in branch_recovery)}",
            "records",
        )
    )
    gates.append(
        gate(
            "CEL-P9-DISCARDED-BRANCH-LOSES-RECOVERY",
            not core.zero_error_recoverable(coarse_branch),
            f"coarse={core.qmatrix_text(coarse_branch)} recoverable={core.zero_error_recoverable(coarse_branch)}",
            "records",
        )
    )
    licence = records["licence_control"]
    licence_channel = exact_qmatrix(licence["channel"])
    licence_readouts = tuple(exact_qmatrix(value) for value in licence["licensed_readouts"])
    licence_relabelings = tuple(exact_qmatrix(value) for value in licence["licensed_sector_relabelings"])
    mathematically_recoverable = core.zero_error_recoverable(licence_channel)
    physically_licensed = exact_identity_recovery(licence_channel, licence_readouts, licence_relabelings)
    gates.append(
        gate(
            "CEL-P10-MATHEMATICAL-VERSUS-LICENSED-RECOVERY",
            mathematically_recoverable and not physically_licensed,
            f"mathematical={mathematically_recoverable} licensed={physically_licensed}",
            "records",
        )
    )
    gates.append(
        gate(
            "CEL-P11-RECOVERY-GRAINS-SEPARATED",
            reset_covariant
            and not reset_recoverable
            and all(branch_recovery)
            and not core.zero_error_recoverable(coarse_branch)
            and not physically_licensed,
            "covariance, mathematical recovery, branch recovery, coarse recovery, and licence are independently resolved",
            "records",
        )
    )

    # Instrument dilation and relational weld.
    dilation = data["dilation"]
    dilation_histories = tuple(exact_matrix(value) for value in dilation["histories"])
    coefficients = {
        name: exact_matrix(value) for name, value in dilation["coefficient_families"].items()
    }
    dilation_kernels = {name: core.gram(value) for name, value in coefficients.items()}
    class_ops = {
        name: core.class_operators(dilation_histories, value) for name, value in coefficients.items()
    }
    stacks = {name: core.stinespring_stack(operators) for name, operators in class_ops.items()}
    registered_kernel = core.matrix([[Q(16, 25), 0], [0, Q(9, 25)]])
    dilation_complete = {
        name: core.completeness_from_coefficients(dilation_histories, value) == core.identity(2)
        for name, value in coefficients.items()
    }
    gates.append(
        gate(
            "CEL-D1-JCV-SHARED-KERNEL-AND-ISOMETRIES",
            dilation_kernels["first"] == dilation_kernels["second"] == registered_kernel
            and all(dilation_complete.values())
            and all(core.is_stinespring_isometry(operators) for operators in class_ops.values()),
            f"kernel={core.matrix_text(dilation_kernels['first'])} complete={dilation_complete}",
            "dilation",
        )
    )
    flag_vectors = {
        name: {
            "m0": (stack[0][0], stack[2][0]),
            "m1": (stack[1][1], stack[3][1]),
        }
        for name, stack in stacks.items()
    }
    registered_vectors = {
        "first": {"m0": (core.ZERO, core.ONE), "m1": (core.GQ(Q(24, 25)), core.GQ(Q(7, 25)))},
        "second": {"m0": (core.GQ(Q(7, 25)), core.GQ(Q(24, 25))), "m1": (core.ONE, core.ZERO)},
    }
    gates.append(
        gate(
            "CEL-D2-FLAG-COUPLING-VECTORS",
            flag_vectors == registered_vectors,
            "first=(0,1)/(24/25,7/25); second=(7/25,24/25)/(1,0)",
            "dilation",
        )
    )
    pre_dimension = len(dilation["pre_catalogue"])
    post_dimension = len(dilation["post_catalogue_flag_major"])
    rewrite = dilation["rewrite"]
    attachment_typed = (
        rewrite["created_cell"] in rewrite["post_cells"]
        and rewrite["created_cell"] not in rewrite["pre_cells"]
        and len(rewrite["attachment"]) == 2
        and rewrite["attachment"][0] in rewrite["pre_cells"]
        and rewrite["attachment"][1] == rewrite["created_cell"]
    )
    gates.append(
        gate(
            "CEL-D3-DERIVED-CATALOGUE-AND-ATTACHMENT",
            pre_dimension == 2 and post_dimension == 4 and attachment_typed,
            f"dimensions={pre_dimension}->{post_dimension} attachment={rewrite['attachment']}",
            "dilation",
        )
    )
    allowed_support = {tuple(value) for value in dilation["allowed_support"]}
    support_union = support(stacks["first"]) | support(stacks["second"])
    input_relabel = permutation_from_list(dilation["input_relabel"])
    output_relabel = permutation_from_list(dilation["output_relabel"])
    covariance = core.matmul(core.matmul(output_relabel, stacks["first"]), input_relabel) == stacks["second"]
    gates.append(
        gate(
            "CEL-D4-SUPPORT-REWRITE-AND-RELABEL-COVARIANCE",
            support_union == allowed_support and covariance,
            f"support={sorted(support_union)} covariance={covariance}",
            "dilation",
        )
    )
    dilation_input = exact_matrix(dilation["input_state"])
    port_probabilities = {
        name: tuple(core.trace(core.matmul(core.matmul(operator, dilation_input), core.adjoint(operator))).re for operator in operators)
        for name, operators in class_ops.items()
    }
    channel_signatures = {
        name: core.channel_signature(dilation_histories, kernel) for name, kernel in dilation_kernels.items()
    }
    calibrated_moves = port_probabilities["first"] != port_probabilities["second"]
    if "calibrated-statistic" in faults:
        calibrated_moves = False
    gates.append(
        gate(
            "CEL-D5-CALIBRATED-FLAG-MOVES-AT-FIXED-CHANNEL",
            calibrated_moves
            and port_probabilities["first"][0] == 0
            and port_probabilities["second"][0] == Q(49, 625)
            and channel_signatures["first"] == channel_signatures["second"],
            f"first-port={core.qtext(port_probabilities['first'][0])}->{core.qtext(port_probabilities['second'][0])} channel-equal={channel_signatures['first'] == channel_signatures['second']}",
            "dilation",
        )
    )
    relational_weld = pre_dimension == 2 and post_dimension == 4 and attachment_typed and support_union == allowed_support and covariance
    anonymous = dilation["anonymous_control"]
    anonymous_weld = anonymous["has_named_attachment"] and anonymous["has_relational_rewrite"]
    anonymous_is_untyped = not anonymous["has_named_attachment"] and not anonymous["has_relational_rewrite"]
    gates.append(
        gate(
            "CEL-D6-ANONYMOUS-ANCILLA-IS-NOT-A-RELATIONAL-FLAG",
            relational_weld and anonymous_is_untyped and not anonymous_weld,
            f"typed={relational_weld} anonymous-untyped={anonymous_is_untyped} anonymous-weld={anonymous_weld}",
            "dilation",
        )
    )
    continuation_append = exact_qmatrix(dilation["continuations"]["append_only"])
    continuation_erase = exact_qmatrix(dilation["continuations"]["erasing"])
    flag_identity = core.qidentity(2)
    append_durable = core.zero_error_recoverable(core.qmul(continuation_append, flag_identity))
    erase_durable = core.zero_error_recoverable(core.qmul(continuation_erase, flag_identity))
    gates.append(
        gate(
            "CEL-D7-SAME-DILATION-DIFFERENT-DURABILITY-GRAMMARS",
            append_durable and not erase_durable,
            f"append={append_durable} erasing={erase_durable}",
            "dilation",
        )
    )
    gates.append(
        gate(
            "CEL-D8-DILATION-DOES-NOT-DERIVE-ACTUALIZATION",
            "actualization" in data["scope_walls"],
            "Stinespring creation isometry and conditional port records are constructed; one-outcome actualization is outside the model",
            "dilation",
        )
    )

    # Exact resource theorem.
    resources = data["resources"]
    scalar_value = exact_fraction(resources["scalar"])
    scalar_pair = core.gaussian_norm_pair(scalar_value)
    scalar_one_row = core.is_gaussian_norm_rational(scalar_value)
    scalar_two_rows = sum((value.norm2() for value in scalar_pair), Q(0)) == scalar_value
    gates.append(
        gate(
            "CEL-E1-SCALAR-RESOURCE-WITNESS",
            scalar_value == Q(7, 5) and not scalar_one_row and scalar_two_rows,
            f"value={core.qtext(scalar_value)} one-row={scalar_one_row} two-row={scalar_two_rows}",
            "resources",
        )
    )
    rank_two = exact_matrix(resources["rank_two"])
    explicit_three = exact_matrix(resources["rank_two_three_row_factor"])
    determinant_value = core.determinant(rank_two)
    determinant_obstructs_square = determinant_value.im == 0 and not core.is_gaussian_norm_rational(determinant_value.re)
    gates.append(
        gate(
            "CEL-E2-RANK-TWO-MINIMUM-THREE-ROW-WITNESS",
            core.matrix_rank(rank_two) == 2
            and determinant_obstructs_square
            and len(explicit_three) == 3
            and core.gram(explicit_three) == rank_two,
            f"rank={core.matrix_rank(rank_two)} determinant={core.gtext(determinant_value)} rows={len(explicit_three)}",
            "resources",
        )
    )
    registered_psd = tuple(exact_matrix(value) for value in resources["registered_psd"])
    factors = tuple(core.gaussian_rational_gram_factor(value) for value in registered_psd)
    reconstructions = tuple(
        core.gram(factor, columns_if_empty=core.shape(value)[0]) == value
        for factor, value in zip(factors, registered_psd)
    )
    row_bounds = tuple(len(factor) <= 2 * core.matrix_rank(value) for factor, value in zip(factors, registered_psd))
    if "ldl-reconstruction" in faults:
        reconstructions = (False,) + reconstructions[1:]
    if "row-bound" in faults:
        row_bounds = (False,) + row_bounds[1:]
    gates.append(
        gate(
            "CEL-E3-GAUSSIAN-RATIONAL-2R-CONSTRUCTION",
            all(core.is_psd(value) for value in registered_psd)
            and all(reconstructions)
            and all(row_bounds),
            f"ranks={[core.matrix_rank(value) for value in registered_psd]} rows={[len(value) for value in factors]}",
            "resources",
        )
    )
    non_psd = exact_matrix(resources["non_psd"])
    try:
        core.gaussian_rational_gram_factor(non_psd)
        non_psd_refused = False
    except ValueError:
        non_psd_refused = True
    gates.append(
        gate(
            "CEL-E4-NONPSD-REFUSAL",
            not core.is_psd(non_psd) and non_psd_refused,
            f"psd={core.is_psd(non_psd)} refused={non_psd_refused}",
            "resources",
        )
    )
    some_factor = core.gaussian_rational_gram_factor(registered_kernel)
    specified_first = core.gram(coefficients["first"]) == registered_kernel
    some_differs_from_specified = some_factor != coefficients["first"]
    if "some-vs-specified" in faults:
        some_differs_from_specified = False
    gates.append(
        gate(
            "CEL-E5-SOME-SPECIFIED-AND-GRAMMAR-REALIZATION-SEPARATED",
            core.gram(some_factor) == registered_kernel
            and specified_first
            and some_differs_from_specified
            and relational_weld
            and not anonymous_weld,
            f"some-factor-rows={len(some_factor)} specified={specified_first} relational={relational_weld}",
            "resources",
        )
    )
    field_is_ontology = resources["field_role"] == "ontological number field"
    gates.append(
        gate(
            "CEL-E6-NUMBER-FIELD-IS-RESOURCE-BOOKKEEPING",
            not field_is_ontology,
            f"field-role={resources['field_role']}",
            "resources",
        )
    )
    zero_pivot_index = next(index for index, value in enumerate(registered_psd) if value[0][0] == core.ZERO)
    gates.append(
        gate(
            "CEL-E7-ZERO-PIVOT-CONTROL",
            reconstructions[zero_pivot_index]
            and len(factors[zero_pivot_index]) <= 2 * core.matrix_rank(registered_psd[zero_pivot_index]),
            f"index={zero_pivot_index} rank={core.matrix_rank(registered_psd[zero_pivot_index])} rows={len(factors[zero_pivot_index])}",
            "resources",
        )
    )

    required_walls = {
        "actualization",
        "selected coupling values",
        "catalogue selection",
        "unconditional catalogue closure",
        "arbitrary-n composition",
        "conditional steering",
        "metric backreaction",
        "continuum limit",
        "Lorentz symmetry",
        "QFT reconstruction",
        "GR reconstruction",
        "particle species",
        "Hamiltonian reconstruction",
        "affine constant",
        "empirical deviation",
    }
    gates.append(
        gate(
            "CEL-SCOPE-WALLS",
            set(data["scope_walls"]) == required_walls,
            f"walls={len(data['scope_walls'])}",
            "scope",
        )
    )

    recurrence_ok = all(row["passed"] for row in gates if row["group"] == "recurrence")
    records_ok = all(row["passed"] for row in gates if row["group"] == "records")
    dilation_math_ok = all(
        row["passed"] for row in gates if row["gate"] in {"CEL-D1-JCV-SHARED-KERNEL-AND-ISOMETRIES", "CEL-D2-FLAG-COUPLING-VECTORS"}
    )
    dilation_weld_ok = all(row["passed"] for row in gates if row["group"] == "dilation")
    resources_ok = all(row["passed"] for row in gates if row["group"] == "resources")
    integrity_ok = all(row["passed"] for row in gates if row["group"] == "integrity")
    scope_ok = all(row["passed"] for row in gates if row["group"] == "scope")
    if not records_ok:
        primary = PRIMARY_WORDS[2]
    elif not resources_ok:
        primary = PRIMARY_WORDS[3]
    elif recurrence_ok and dilation_math_ok and dilation_weld_ok and integrity_ok and scope_ok:
        primary = PRIMARY_WORDS[0]
    elif recurrence_ok and dilation_math_ok and integrity_ok and scope_ok:
        primary = PRIMARY_WORDS[1]
    else:
        primary = PRIMARY_WORDS[4]
    comparator_consistent = primary in PRIMARY_WORDS
    if "primary-comparator" in faults:
        comparator_consistent = False
    gates.append(
        gate(
            "CEL-PRIMARY-COMPARATOR",
            comparator_consistent and primary == PRIMARY_WORDS[0],
            f"primary={primary}",
            "outcome",
        )
    )
    gates.append(
        gate(
            "CEL-PREWRITE-SEAL",
            "prewrite-seal" not in faults,
            f"fixture-sha256={sha256_bytes(fixture_bytes)}",
            "integrity",
        )
    )
    gates.append(
        gate(
            "CEL-TRANSCRIPT-BINDING-PRECHECK",
            "transcript-binding" not in faults,
            "transcript and paper hashes are added only after deterministic rendering",
            "integrity",
        )
    )

    qualifiers = list(QUALIFIER_WORDS) if primary == PRIMARY_WORDS[0] else []
    measurements = {
        "anchors": anchor_rows,
        "recurrence": {
            "history_outputs": [
                next(index for index in range(1 << bit_count) if history[index][bits_to_index(overlap["input_bits"])] == core.ONE)
                for history in histories
            ],
            "screen_probabilities": {name: core.qtext(value) for name, value in screen_probabilities.items()},
            "dressed_screen_probabilities": {name: core.qtext(value) for name, value in dressed_probabilities.items()},
            "exchange_fixed": exchange_fixed,
            "operational_null_raw_equal": null_kernels["left"] == null_kernels["right"],
            "operational_null_channel_equal": null_signatures["left"] == null_signatures["right"],
            "gluing_restrictions": {
                "left": [core.qtext(value) for value in restrict_left],
                "right": [core.qtext(value) for value in restrict_right],
                "mismatch": [core.qtext(value) for value in mismatch_right],
            },
            "universality_dimensions": [independent_dimension, universal_dimension],
        },
        "records": {
            "reset": {"complete": core.is_complete_kraus(reset_kraus), "covariant": reset_covariant, "recoverable": reset_recoverable},
            "relabel": {"recoverable": core.zero_error_recoverable(relabel_classical), "fixed_projector_commutes": fixed_projector_commutes},
            "append_word_count": append_certificate["word_count"],
            "single_refire_flag_channel": core.qmatrix_text(single_flag_channel),
            "two_copy_positive": positive_certificate,
            "two_copy_enlarged": enlarged_certificate,
            "branchwise_recovery": branch_recovery,
            "discarded_branch_channel": core.qmatrix_text(coarse_branch),
            "mathematical_but_unlicensed": mathematically_recoverable and not physically_licensed,
        },
        "dilation": {
            "kernel": core.matrix_text(registered_kernel),
            "flag_vectors": {
                family: {matter: [core.gtext(value) for value in vector] for matter, vector in vectors.items()}
                for family, vectors in flag_vectors.items()
            },
            "port_probabilities": {
                family: [core.qtext(value) for value in values] for family, values in port_probabilities.items()
            },
            "channel_equal": channel_signatures["first"] == channel_signatures["second"],
            "support_union": [list(value) for value in sorted(support_union)],
            "covariant": covariance,
            "relational_weld": relational_weld,
            "anonymous_weld": anonymous_weld,
            "append_durable": append_durable,
            "erase_durable": erase_durable,
        },
        "resources": {
            "scalar": core.qtext(scalar_value),
            "scalar_one_row": scalar_one_row,
            "scalar_pair": [core.gtext(value) for value in scalar_pair],
            "rank_two_determinant": core.gtext(determinant_value),
            "rank_two_square_obstructed": determinant_obstructs_square,
            "rank_two_explicit_rows": len(explicit_three),
            "registered_ranks": [core.matrix_rank(value) for value in registered_psd],
            "constructed_rows": [len(value) for value in factors],
            "reconstructions": reconstructions,
            "row_bounds": row_bounds,
            "non_psd_refused": non_psd_refused,
            "field_role": resources["field_role"],
        },
    }
    claims = [
        f"The machine-derived primary is `{primary}`.",
        "Transport locality and all-input completeness do not force one probability kernel across token-disjoint same-type contexts.",
        f"The registered recurrence ladder propagates equality by spectator naturality, licensed symmetry, and shared-token gluing; type universality prices the law space from dimension {independent_dimension} to {universal_dimension}.",
        "Raw kernel identity is too strong on nonfaithful history families: the registered distinct kernels induce the same complete operational channel.",
        "Diagonal-algebra covariance is not permanence: the reset channel is covariant and trace preserving while merging the two record sectors.",
        f"The redundant record survives every word of the restricted {positive_certificate['word_count']}-element grammar and fails licensed flag recovery in the enlarged {enlarged_certificate['word_count']}-element grammar.",
        "Retaining the identity/flip branch permits exact recovery; discarding the branch destroys it.",
        "The two JCV factorizations are exact created-flag isometries only after the catalogue, attachment, support, and relabeling-covariance weld is supplied.",
        f"At the shared unconditioned kernel, the calibrated first-port probability moves from {core.qtext(port_probabilities['first'][0])} to {core.qtext(port_probabilities['second'][0])}; no coupling is selected.",
        "Every registered PSD Hermitian matrix over Q(i) is exactly reconstructed by the LDL-dagger/four-square constructor using no more than twice its rank in flag rows.",
        f"The scalar {core.qtext(scalar_value)} needs two Gaussian-rational rows, and the rank-two diagonal witness needs three rather than two because its determinant is not a Gaussian norm.",
        "The number field prices exact minimal resources; it is not declared ontic and does not veto enlarged realizations.",
        "Actualization, the catalogue and coupling law, arbitrary-n composition, conditional steering, backreaction, continuum/Lorentz structure, QFT, GR, particles, Hamiltonians, constants, and deviations remain unconstructed.",
    ]
    return {
        "schema": "cel-result-v1",
        "fixture_sha256": sha256_bytes(fixture_bytes),
        "constructor_sha256": core_hash,
        "measurements": measurements,
        "gates": gates,
        "outcome": {"primary": primary, "qualifiers": qualifiers},
        "claims": claims,
        "scope_walls": list(data["scope_walls"]),
    }


def render_transcript(result: Mapping[str, Any]) -> str:
    lines = ["CEL PAPER 7 PHYSICAL SCORING", f"schema: {result['schema']}"]
    for row in result["gates"]:
        state = "PASS" if row["passed"] else "FAIL"
        lines.append(f"{state} {row['gate']} [{row['group']}] :: {row['evidence']}")
    lines.extend(
        [
            f"gate-count: {len(result['gates'])}",
            f"all-pass: {str(all(row['passed'] for row in result['gates'])).lower()}",
            f"primary: {result['outcome']['primary']}",
            "qualifiers: " + " | ".join(result["outcome"]["qualifiers"]),
        ]
    )
    return "\n".join(lines) + "\n"


def render_paper(result: Mapping[str, Any]) -> str:
    recurrence = result["measurements"]["recurrence"]
    records = result["measurements"]["records"]
    dilation = result["measurements"]["dilation"]
    resources = result["measurements"]["resources"]
    primary = result["outcome"]["primary"]
    qualifier_text = "`, `".join(result["outcome"]["qualifiers"])
    claim_lines = "\n".join(f"{index}. {claim}" for index, claim in enumerate(result["claims"], 1))
    wall_lines = "\n".join(f"- {wall}" for wall in result["scope_walls"])
    return f"""# Creation-event universality, recoverable records, and exact flag resources

Status: **GREEN-UNREVIEWED CANDIDATE**. This paper is generated from the
sealed CEL result object. It is not terminal, and Papers 3–6 remain pending
their separately frozen hostile panels.

## Abstract

This finite exact investigation asks whether probability-law recurrence,
durable records, and calibrated measurement ports are three aspects of one
creation-event layer. The answer is constructive but conditional. Spectator
naturality, licensed symmetries, and shared-token gluing propagate a law once
their hypotheses apply; they do not derive a common kernel across unrelated
copies of an event type. Record permanence is not invariance of a label or
algebra: it is recoverability, by licensed operations, after every word in a
declared continuation grammar. Calibrated instrument ports admit exact
Stinespring dilations and, in the registered fixture, those dilations satisfy
an explicit relational created-flag weld. Finally, every registered positive
Hermitian kernel over `Q(i)` receives a constructive rectangular Gram factor,
and exact-field obstructions alter minimum flag resources rather than absolute
realizability.

The machine-selected primary is `{primary}`. Its qualifiers are
`{qualifier_text}`.

## 1. Ontological and mathematical separation

The construction keeps seven coordinates distinct: a configuration catalogue,
a relational rewrite, complete-history transports, an unconditioned positive
kernel, a calibrated port factorization, a continuation grammar, and licensed
readouts. A shared name does not identify these objects. The unconditioned
kernel controls ensemble evolution; its factorization controls which retained
port record is seen. A flag becomes a relational cell only when a catalogue,
attachment, support rule, and relabeling covariance are supplied. It becomes a
durable record only under a further continuation test. Nothing in those steps
explains why one outcome happens.

## 2. The recurrence ladder

Two order histories are built from overlapping CNOT events on actors A, B, C.
From the input `100`, the histories end at basis indices
`{recurrence['history_outputs']}`. Both the biased kernel
`diag(16/25,9/25)` and the balanced kernel `diag(1/2,1/2)` are all-input
complete. Nevertheless the registered `111` screen is
`{recurrence['screen_probabilities']['biased']}` for the first and
`{recurrence['screen_probabilities']['balanced']}` for the second. The same
separation survives idle dressing. Therefore transport locality and
completeness do not choose the probability law.

The positive recurrence statements are narrower:

1. the standing spectator-naturality axiom transports an operational law to
   its idle extension;
2. a licensed exchange automorphism rejects the biased kernel and admits the
   balanced one inside that symmetry orbit;
3. restrictions of one explicit joint token law agree on the shared token;
   the registered mismatched local value fails; and
4. declaring one parameter for two token-disjoint instances reduces the
   affine law space from `{recurrence['universality_dimensions'][0]}` to
   `{recurrence['universality_dimensions'][1]}`.

The fourth item is a predictive price, not a derivation. It is the ordinary
nomological move “the same event type carries the same coupling in both
laboratories.” Moreover, raw kernel equality is not always physical: with two
identical histories, two different raw kernels have byte-identical complete
channel signatures. Recurrence is therefore equality modulo the operational
null ideal unless faithfulness is separately proved.

## 3. Permanence means licensed recoverability

The reset channel is the decisive negative control. It is trace preserving and
its Heisenberg action preserves the diagonal flag algebra, yet both input
sectors become the same output sector. Algebra covariance is therefore not
record permanence. Conversely a flag flip does not commute with each fixed
sector projector, but it merely relabels the two sectors and is perfectly
recoverable. The invariant object is distinguishable information, not a
particular name.

An append-only grammar has an exact all-word certificate. Re-firing a single
involutive CNOT writer erases the flag it wrote. With two flag copies, re-firing
the first writer leaves the second copy readable. That is not yet absolute
permanence: the restricted continuation semigroup has
`{records['two_copy_positive']['word_count']}` elements and preserves a
licensed copy for every word, whereas the enlarged
`{records['two_copy_enlarged']['word_count']}`-element grammar can re-fire the
second writer too and remove the last licensed flag copy. Global source
information may still exist; the claim concerns the declared flag-record
algebra.

The identity/flip instrument isolates another distinction. Each retained
branch has an exact inverse readout. When the branch label is discarded, the
coarse channel is `{records['discarded_branch_channel']}` and is not
zero-error recoverable. Finally, a mathematically invertible flip is refused
when the grammar licenses neither its inverse readout nor a sector relabeling.
Mathematical, branch-assisted, and physically licensed recovery are not one
predicate.

## 4. Ports as created flag cells—conditionally

For histories `I` and `Z`, the two calibrated JCV coefficient families have
the same kernel `{dilation['kernel']}` and each stacks into an exact
Stinespring isometry. Their flag coupling vectors are:

- first family: `m0 -> {dilation['flag_vectors']['first']['m0']}` and
  `m1 -> {dilation['flag_vectors']['first']['m1']}`;
- second family: `m0 -> {dilation['flag_vectors']['second']['m0']}` and
  `m1 -> {dilation['flag_vectors']['second']['m1']}`.

The fixture supplies two pre-configurations, four post-configurations, a new
flag cell attached to the matter cell, and the exact allowed support
`{dilation['support_union']}`. Swapping the matter and flag names carries the
first transport into the second exactly. Thus the ports can be retyped as two
coupling settings of one created-flag grammar at this arena. An anonymous
four-dimensional ancilla with no catalogue, attachment, or rewrite fails the
same classifier.

The unconditioned channel is identical, while the calibrated first-port
probability moves from `{dilation['port_probabilities']['first'][0]}` to
`{dilation['port_probabilities']['second'][0]}`. This is physical calibrated
fiber freedom; the architecture does not select either coupling. Nor does the
isometry alone make the flag a permanent record: an append-only continuation
preserves conditional port labels and a reset continuation erases them.
Actualization is still postulated rather than derived.

## 5. Exact resource theorem

Let `A` be positive-semidefinite Hermitian over `Q(i)`. Exact Hermitian
`LDL^dagger` writes `A = L D L^dagger` with nonnegative rational pivots. For
each positive pivot `d=p/q`, Lagrange's four-square theorem gives
`pq=a^2+b^2+c^2+e^2`, hence

```text
d = |(a+ib)/q|^2 + |(c+ie)/q|^2.
```

Multiplying the corresponding row of `L^dagger` by those two Gaussian
rationals yields at most two Gram rows per nonzero pivot. Zero PSD pivots have
zero residual columns and contribute no row. Therefore every rank-`r` kernel
in the registered exact class has a `Q(i)` factor with at most `2r` rows.

The four registered real, non-real, singular, and three-dimensional controls
have ranks `{resources['registered_ranks']}` and constructive row counts
`{resources['constructed_rows']}`; every reconstruction and bound is exact.
The non-PSD control is refused.

The resource witnesses show why rectangularity matters. The scalar
`{resources['scalar']}` is not one Gaussian-rational norm but is the sum of
two, here `{resources['scalar_pair']}`. The rank-two diagonal kernel has
determinant `{resources['rank_two_determinant']}`, also not a Gaussian norm,
so a square two-row factor is impossible; the registered three-row factor is
exact. The field restricts minimum exact port dimension. It does not prevent
an enlarged realization, and the theory has not declared `Q(i)` ontological.

## 6. What is achieved and what is not

The finite result compresses three debts into one conditional creation-event
layer. Probability recurrence is a ladder of explicit propagation principles
plus a residual universality postulate. Record durability is a computable,
grammar-relative recoverability property. Instrument fibers can be concrete
created-cell couplings when the relational weld is actually present. Exact
number theory controls realization cost. These are architecture and
classification results, not a fundamental dynamical law.

Frozen claim table:

{claim_lines}

The following remain outside the result:

{wall_lines}

In particular, the paper neither derives the catalogue and couplings nor
turns the Hamiltonian into ontology. It supplies a sharper place for those
unknowns to live: the local creation-event law and its universally recurring
parameters.

## 7. Scope and review status

All computations are finite-dimensional and exact over `Q(i)`. The CNOT,
flag, and resource fixtures are falsifiable controls, not empirical models of
known matter or gravity. The result has passed its frozen constructor gates
but has not undergone the separately required hostile panel. A hostile review
must attack, at minimum, recurrence modulo nulls, branch-dependent recovery,
catalogue-relative permanence, the relational flag weld, the generality of
the `2r` construction, and every attempted QFT/GR promotion.
"""


def finalized_receipt(result: Mapping[str, Any], transcript: str, paper: str) -> dict[str, Any]:
    receipt = dict(result)
    receipt["transcript_sha256"] = sha256_bytes(transcript.encode("utf-8"))
    receipt["paper_sha256"] = sha256_bytes(paper.encode("utf-8"))
    receipt["seals"] = {
        key: digest(receipt[key])
        for key in (
            "schema",
            "fixture_sha256",
            "constructor_sha256",
            "measurements",
            "gates",
            "outcome",
            "claims",
            "scope_walls",
        )
    }
    return receipt


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
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=code_root / "cel_fixture.json")
    parser.add_argument("--output", type=Path, default=code_root / "cel_output.txt")
    parser.add_argument("--receipt", type=Path, default=code_root / "cel_receipt.json")
    parser.add_argument(
        "--paper",
        type=Path,
        default=repo_root / "v16/paper-07-creation-event-universality-recoverable-records.md",
    )
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--mutant", choices=MUTANTS)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.selftest and args.mutant is not None:
        print("REFUSE CEL-CLI :: selftest and mutant are mutually exclusive", file=sys.stderr)
        return 2
    targets = (args.output.resolve(), args.receipt.resolve(), args.paper.resolve())
    if any(path.exists() for path in targets):
        print("REFUSE CEL-TARGET :: output, receipt, or paper already exists", file=sys.stderr)
        return 1
    try:
        fixture_bytes = args.fixture.resolve().read_bytes()
        data = json.loads(fixture_bytes)
        mutant = "anchor-hash" if args.selftest else args.mutant
        faults = apply_mutant(data, mutant)
        root = Path(__file__).resolve().parents[2]
        result = score(data, fixture_bytes, root, faults)
        failed = [row["gate"] for row in result["gates"] if not row["passed"]]
        if failed:
            label = "CEL-SELFTEST" if args.selftest else "CEL-GATE"
            print(f"REFUSE {label} :: {','.join(failed)}", file=sys.stderr)
            return 1
        transcript = render_transcript(result)
        paper = render_paper(result)
        receipt = finalized_receipt(result, transcript, paper)
        if receipt["transcript_sha256"] != sha256_bytes(transcript.encode("utf-8")):
            print("REFUSE CEL-TRANSCRIPT-SEAL", file=sys.stderr)
            return 1
        if receipt["paper_sha256"] != sha256_bytes(paper.encode("utf-8")):
            print("REFUSE CEL-PAPER-SEAL", file=sys.stderr)
            return 1
        atomic_write(args.output.resolve(), transcript.encode("utf-8"))
        atomic_write(args.receipt.resolve(), canonical_json(receipt))
        atomic_write(args.paper.resolve(), paper.encode("utf-8"))
        sys.stdout.write(transcript)
        return 0
    except Exception as error:
        print(f"REFUSE CEL-EXCEPTION :: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
