#!/usr/bin/env python3
"""Exact fixtures and hidden scoring truth for the frozen RQ0-L0 estimator.

This module was created only after estimator commit
a5b7173 was frozen.  It may import the estimator.  The estimator must not
import this module.  Construction labels in ``LocalizationTruth`` are for the
scorer only and are never included in ``OperationalDataset``.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Mapping, Optional, Sequence, Tuple

import rq0_l0_localization_estimator_exact as est


FROZEN_ESTIMATOR_COMMIT = "a5b7173"
FROZEN_ESTIMATOR_SHA256 = "0b8d90bad735f6574ee367dd0bf7e98bcc1c6f2854f7a12070c82bae84e063b8"


@dataclass(frozen=True)
class LocalizationTruth:
    atom_handles: Tuple[frozenset[str], ...]
    record_pairs: Mapping[str, frozenset[int]]
    active_extension_atom: int
    required_fact_triple: Tuple[frozenset[int], frozenset[int], frozenset[int]]


@dataclass(frozen=True)
class FixtureBundle:
    main: est.OperationalDataset
    unencoded: est.OperationalDataset
    gauge_variant: est.OperationalDataset
    phase_variant: est.OperationalDataset
    inaccessible_extension: est.OperationalDataset
    ambiguity: est.OperationalDataset
    irreducible: est.OperationalDataset
    truth: LocalizationTruth
    encoding_a: est.Matrix
    encoding_b: est.Matrix
    gauge_action: est.Matrix
    phase_changed_handle: str


def compose_chronological(*operations: est.Matrix) -> est.Matrix:
    if not operations:
        raise ValueError("at least one operation is required")
    result = operations[0]
    for operation in operations[1:]:
        result = est.mmul(operation, result)
    return result


def on_slot(operation: est.Matrix, slot: int, slots: int) -> est.Matrix:
    if est.shape(operation) != (2, 2):
        raise ValueError("slot operation must be two dimensional")
    result = est.identity(1)
    for index in range(slots):
        result = est.kron(result, operation if index == slot else est.identity(2))
    return result


def basis_projector(slot: int, value: int, slots: int) -> est.Matrix:
    p0 = est.matrix(((1, 0), (0, 0)))
    p1 = est.matrix(((0, 0), (0, 1)))
    return on_slot(p0 if value == 0 else p1, slot, slots)


def controlled_x(slots: int, control: int, target: int) -> est.Matrix:
    dimension = 1 << slots
    rows = [[est.ZERO for _ in range(dimension)] for _ in range(dimension)]
    for source in range(dimension):
        bits = [((source >> (slots - 1 - index)) & 1) for index in range(slots)]
        output_bits = list(bits)
        if bits[control]:
            output_bits[target] ^= 1
        destination = 0
        for bit in output_bits:
            destination = (destination << 1) | bit
        rows[destination][source] = est.ONE
    return tuple(tuple(row) for row in rows)


def swap_slots(slots: int, left: int, right: int) -> est.Matrix:
    dimension = 1 << slots
    rows = [[est.ZERO for _ in range(dimension)] for _ in range(dimension)]
    for source in range(dimension):
        bits = [((source >> (slots - 1 - index)) & 1) for index in range(slots)]
        bits[left], bits[right] = bits[right], bits[left]
        destination = 0
        for bit in bits:
            destination = (destination << 1) | bit
        rows[destination][source] = est.ONE
    return tuple(tuple(row) for row in rows)


def direct_sum(left: est.Matrix, right: est.Matrix) -> est.Matrix:
    left_rows, left_columns = est.shape(left)
    right_rows, right_columns = est.shape(right)
    top = tuple(
        tuple(left[row]) + tuple(est.ZERO for _ in range(right_columns))
        for row in range(left_rows)
    )
    bottom = tuple(
        tuple(est.ZERO for _ in range(left_columns)) + tuple(right[row])
        for row in range(right_rows)
    )
    return top + bottom


def extend_vector(value: est.Vector, extra: int) -> est.Vector:
    return value + tuple(est.ZERO for _ in range(extra))


def conjugate_record(witness: est.RecordWitness, action: est.Matrix) -> est.RecordWitness:
    return est.RecordWitness(
        handle=witness.handle,
        preparations=tuple(est.mv(action, value) for value in witness.preparations),
        alternative_projectors=tuple(
            est.conjugate_by(action, value) for value in witness.alternative_projectors
        ),
        cut_record_projectors=tuple(
            est.conjugate_by(action, value) for value in witness.cut_record_projectors
        ),
        availability_probes=tuple(
            est.conjugate_by(action, value) for value in witness.availability_probes
        ),
        write=est.conjugate_by(action, witness.write),
        preserving=tuple(est.conjugate_by(action, value) for value in witness.preserving),
        erasing=tuple(est.conjugate_by(action, value) for value in witness.erasing),
        no_write=est.conjugate_by(action, witness.no_write),
    )


def conjugate_dataset(
    dataset: est.OperationalDataset,
    action: est.Matrix,
    handle: str,
    reverse_access_order: bool = False,
) -> est.OperationalDataset:
    preparations = tuple(est.mv(action, value) for value in dataset.preparations)
    interventions = tuple(
        est.Operation(value.handle, est.conjugate_by(action, value.amplitude))
        for value in dataset.interventions
    )
    contexts = tuple(
        est.Context(
            value.handle,
            est.conjugate_by(action, value.before),
            est.conjugate_by(action, value.after),
        )
        for value in dataset.contexts
    )
    probes = tuple(est.Probe(value.handle, est.mv(action, value.state)) for value in dataset.probes)
    support_actions = tuple(est.conjugate_by(action, value) for value in dataset.support_actions)
    presentation_actions = tuple(
        est.conjugate_by(action, value) for value in dataset.presentation_actions
    )
    records = tuple(conjugate_record(value, action) for value in dataset.records)
    if reverse_access_order:
        preparations = tuple(reversed(preparations))
        interventions = tuple(reversed(interventions))
        contexts = tuple(reversed(contexts))
        probes = tuple(reversed(probes))
        support_actions = tuple(reversed(support_actions))
        records = tuple(reversed(records))
    return est.OperationalDataset(
        handle=handle,
        dimension=dataset.dimension,
        preparations=preparations,
        interventions=interventions,
        contexts=contexts,
        probes=probes,
        support_actions=support_actions,
        presentation_actions=presentation_actions,
        records=records,
        access_declaration=dataset.access_declaration,
        gauge_declaration=dataset.gauge_declaration,
    )


def access_vectors(slots: int) -> Tuple[est.Vector, ...]:
    dimension = 1 << slots
    computational = tuple(est.basis_vector(dimension, index) for index in range(dimension))
    h = est.matrix(
        (
            (est.INV_SQRT2, est.INV_SQRT2),
            (est.INV_SQRT2, -est.INV_SQRT2),
        )
    )
    s = est.matrix(((1, 0), (0, est.I)))
    h_all = est.identity(1)
    sh_all = est.identity(1)
    for _ in range(slots):
        h_all = est.kron(h_all, h)
        sh_all = est.kron(sh_all, est.mmul(s, h))
    hadamard = tuple(est.mv(h_all, value) for value in computational)
    phase = tuple(est.mv(sh_all, value) for value in computational)
    return computational + hadamard + phase


def local_record_witness(slots: int, branch: int, memory: int, handle: str) -> est.RecordWitness:
    h = est.matrix(
        (
            (est.INV_SQRT2, est.INV_SQRT2),
            (est.INV_SQRT2, -est.INV_SQRT2),
        )
    )
    z = est.matrix(((1, 0), (0, -1)))
    write = controlled_x(slots, branch, memory)
    preserve = on_slot(z, branch, slots)
    erase = compose_chronological(write, on_slot(h, branch, slots))
    initial = est.basis_vector(1 << slots, 0)
    preparation = est.mv(on_slot(h, branch, slots), initial)
    alternatives = tuple(basis_projector(branch, value, slots) for value in (0, 1))
    records = tuple(basis_projector(memory, value, slots) for value in (0, 1))
    probes = []
    for branch_value, memory_value in itertools.product((0, 1), repeat=2):
        probes.append(
            est.mmul(
                basis_projector(branch, branch_value, slots),
                basis_projector(memory, memory_value, slots),
            )
        )
    return est.RecordWitness(
        handle=handle,
        preparations=(preparation,),
        alternative_projectors=alternatives,
        cut_record_projectors=records,
        availability_probes=tuple(probes),
        write=write,
        preserving=(preserve,),
        erasing=(erase,),
        no_write=est.identity(1 << slots),
    )


def primitive_operations(slots: int, phase_variant_handle: Optional[str] = None) -> Tuple[est.Operation, ...]:
    x = est.matrix(((0, 1), (1, 0)))
    z = est.matrix(((1, 0), (0, -1)))
    t = est.matrix(((1, 0), (0, est.ZETA)))
    handles = (
        ("q7", "q2"),
        ("q0", "q5"),
        ("q6", "q1"),
        ("q3", "q4"),
    )
    operations = []
    for slot, (x_handle, z_handle) in enumerate(handles):
        x_action = on_slot(x, slot, slots)
        if phase_variant_handle == x_handle:
            x_action = compose_chronological(x_action, on_slot(t, slot, slots))
        operations.extend(
            (
                est.Operation(x_handle, x_action),
                est.Operation(z_handle, on_slot(z, slot, slots)),
            )
        )
    order = (3, 0, 6, 1, 5, 2, 7, 4)
    return tuple(operations[index] for index in order)


def unencoded_dataset(
    handle: str,
    phase_variant_handle: Optional[str] = None,
) -> est.OperationalDataset:
    slots = 4
    dimension = 1 << slots
    operations = primitive_operations(slots, phase_variant_handle)
    access = access_vectors(slots)
    record_pairs = tuple(itertools.combinations(range(slots), 2))
    records = tuple(
        local_record_witness(slots, left, right, f"w{index}")
        for index, (left, right) in enumerate(record_pairs)
    )
    return est.OperationalDataset(
        handle=handle,
        dimension=dimension,
        preparations=access,
        interventions=operations,
        contexts=(est.Context("c0", est.identity(dimension), est.identity(dimension)),),
        probes=tuple(est.Probe(f"e{index}", value) for index, value in enumerate(access)),
        support_actions=tuple(value.amplitude for value in operations)
        + tuple(
            action
            for witness in records
            for action in (witness.write,) + witness.preserving + witness.erasing
        ),
        presentation_actions=(est.identity(dimension),),
        records=records,
        access_declaration=(
            "POSTULATE: 48 exact preparation probes, 48 exact readout probes, "
            "eight opaque intervention handles, six frozen record candidates"
        ),
        gauge_declaration="configuration relabelling x exact mu_8 boundary phase",
    )


def encoding_surfaces() -> Tuple[est.Matrix, est.Matrix]:
    slots = 4
    h = est.matrix(
        (
            (est.INV_SQRT2, est.INV_SQRT2),
            (est.INV_SQRT2, -est.INV_SQRT2),
        )
    )
    t = est.matrix(((1, 0), (0, est.ZETA)))
    h0 = on_slot(h, 0, slots)
    t3 = on_slot(t, 3, slots)
    c01 = controlled_x(slots, 0, 1)
    c12 = controlled_x(slots, 1, 2)
    c23 = controlled_x(slots, 2, 3)
    encoding_a = compose_chronological(t3, h0, c01, c12, c23)
    # Same exact amplitude law with two cancelling gates inserted in a
    # different circuit presentation.
    encoding_b = compose_chronological(t3, h0, h0, h0, c01, c12, c23)
    if encoding_a != encoding_b:
        raise AssertionError("the two declared circuit presentations are not exactly equal")
    return encoding_a, encoding_b


def gauge_surface() -> est.Matrix:
    slots = 4
    t = est.matrix(((1, 0), (0, est.ZETA)))
    return compose_chronological(
        swap_slots(slots, 0, 3),
        on_slot(t, 1, slots),
    )


def hidden_unitary(size: int, power: int) -> est.Matrix:
    rows = [[est.ZERO for _ in range(size)] for _ in range(size)]
    for source in range(size):
        rows[(source + power) % size][source] = est.ONE
    return tuple(tuple(row) for row in rows)


def inaccessible_extension(dataset: est.OperationalDataset) -> est.OperationalDataset:
    hidden_size = dataset.dimension
    hidden_identity = est.identity(hidden_size)
    operations = tuple(
        est.Operation(
            value.handle,
            direct_sum(value.amplitude, hidden_unitary(hidden_size, index + 1)),
        )
        for index, value in enumerate(dataset.interventions)
    )
    records = []
    for witness in dataset.records:
        records.append(
            est.RecordWitness(
                handle=witness.handle,
                preparations=tuple(extend_vector(value, hidden_size) for value in witness.preparations),
                alternative_projectors=tuple(
                    direct_sum(value, est.zero_matrix(hidden_size, hidden_size))
                    for value in witness.alternative_projectors
                ),
                cut_record_projectors=tuple(
                    direct_sum(value, est.zero_matrix(hidden_size, hidden_size))
                    for value in witness.cut_record_projectors
                ),
                availability_probes=tuple(
                    direct_sum(value, est.zero_matrix(hidden_size, hidden_size))
                    for value in witness.availability_probes
                ),
                write=direct_sum(witness.write, hidden_identity),
                preserving=tuple(
                    direct_sum(value, hidden_identity) for value in witness.preserving
                ),
                erasing=tuple(direct_sum(value, hidden_identity) for value in witness.erasing),
                no_write=direct_sum(witness.no_write, hidden_identity),
            )
        )
    contexts = tuple(
        est.Context(
            value.handle,
            direct_sum(value.before, hidden_identity),
            direct_sum(value.after, hidden_identity),
        )
        for value in dataset.contexts
    )
    return est.OperationalDataset(
        handle="opaque-inaccessible-extension",
        dimension=dataset.dimension + hidden_size,
        preparations=tuple(extend_vector(value, hidden_size) for value in dataset.preparations),
        interventions=operations,
        contexts=contexts,
        probes=tuple(
            est.Probe(value.handle, extend_vector(value.state, hidden_size))
            for value in dataset.probes
        ),
        support_actions=tuple(value.amplitude for value in operations)
        + tuple(
            action
            for witness in records
            for action in (witness.write,) + witness.preserving + witness.erasing
        ),
        presentation_actions=(est.identity(dataset.dimension + hidden_size),),
        records=tuple(records),
        access_declaration=dataset.access_declaration + "; inaccessible direct-sum completion",
        gauge_declaration=dataset.gauge_declaration,
    )


def ambiguity_dataset() -> est.OperationalDataset:
    dataset = est.calibration_dataset()
    swap = swap_slots(2, 0, 1)
    return est.OperationalDataset(
        handle="opaque-symmetric-control",
        dimension=dataset.dimension,
        preparations=dataset.preparations,
        interventions=dataset.interventions,
        contexts=dataset.contexts,
        probes=dataset.probes,
        support_actions=dataset.support_actions,
        presentation_actions=(est.identity(4), swap),
        records=(),
        access_declaration=dataset.access_declaration,
        gauge_declaration="exact order-two presentation symmetry",
    )


def build_fixture_bundle() -> FixtureBundle:
    truth = LocalizationTruth(
        atom_handles=(
            frozenset(("q7", "q2")),
            frozenset(("q0", "q5")),
            frozenset(("q6", "q1")),
            frozenset(("q3", "q4")),
        ),
        record_pairs={
            f"w{index}": frozenset(pair)
            for index, pair in enumerate(itertools.combinations(range(4), 2))
        },
        active_extension_atom=3,
        required_fact_triple=(
            frozenset((0, 1)),
            frozenset((0, 1, 2)),
            frozenset((0, 1, 3)),
        ),
    )
    unencoded = unencoded_dataset("opaque-unencoded-scoring-surface")
    encoding_a, encoding_b = encoding_surfaces()
    main = conjugate_dataset(unencoded, encoding_a, "opaque-main-surface")
    gauge_action = gauge_surface()
    gauge_variant = conjugate_dataset(
        main,
        gauge_action,
        "opaque-gauge-presentation",
        reverse_access_order=True,
    )
    phase_changed_handle = "q7"
    phase_unencoded = unencoded_dataset(
        "opaque-phase-law-surface",
        phase_variant_handle=phase_changed_handle,
    )
    phase_variant = conjugate_dataset(
        phase_unencoded,
        encoding_b,
        "opaque-phase-law-surface-encoded",
    )
    return FixtureBundle(
        main=main,
        unencoded=unencoded,
        gauge_variant=gauge_variant,
        phase_variant=phase_variant,
        inaccessible_extension=inaccessible_extension(est.calibration_dataset()),
        ambiguity=ambiguity_dataset(),
        irreducible=est.irreducible_calibration_dataset(),
        truth=truth,
        encoding_a=encoding_a,
        encoding_b=encoding_b,
        gauge_action=gauge_action,
        phase_changed_handle=phase_changed_handle,
    )


def record_marginal(witness: est.RecordWitness) -> Tuple[est.Q8, ...]:
    state = est.mv(witness.write, witness.preparations[0])
    return tuple(
        est.inner(est.mv(projector, state), est.mv(projector, state))
        for projector in witness.cut_record_projectors
    )


def equal_law_no_bridge_control() -> Mapping[str, object]:
    four = est.public_record_witness()
    eight = local_record_witness(3, 0, 1, "rogue-eight")
    return {
        "left_dimension": 4,
        "right_dimension": 8,
        "left_law": record_marginal(four),
        "right_law": record_marginal(eight),
        "declared_bridge_type": "fixed-carrier operational isomorphism",
        "bridge_exists": False,
        "obstruction": "boundary_dimension_mismatch:4->8",
    }


if __name__ == "__main__":
    bundle = build_fixture_bundle()
    print(
        {
            "estimator_hash": FROZEN_ESTIMATOR_SHA256,
            "main_dimension": bundle.main.dimension,
            "main_interventions": len(bundle.main.interventions),
            "main_records": len(bundle.main.records),
            "hidden_atoms": len(bundle.truth.atom_handles),
            "encoding_surfaces_equal": bundle.encoding_a == bundle.encoding_b,
            "equal_law_control": equal_law_no_bridge_control()["left_law"]
            == equal_law_no_bridge_control()["right_law"],
        }
    )
