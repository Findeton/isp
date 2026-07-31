#!/usr/bin/env python3
"""Held-out exact fixtures for the RQ0-L0 addressability repair.

This module was created only after the generic estimator was committed and
byte-frozen at v13 #32.  It may contain construction truth for scoring.  The
estimator may not import this module.
"""

from __future__ import annotations

import hashlib
import itertools
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, FrozenSet, Mapping, Optional, Sequence, Tuple

import rq0_l0_addressability_estimator_exact as est


ROOT = Path(__file__).resolve().parents[2]
ESTIMATOR_PATH = ROOT / "v13/code/rq0_l0_addressability_estimator_exact.py"
FROZEN_ESTIMATOR_SHA256 = "79c8d493d29dbc80d8760984da58cd5a8276d757216e13d20abb4404e52ffed3"
ESTIMATOR_COMMIT = "760d921"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_frozen_estimator() -> None:
    observed = sha256(ESTIMATOR_PATH)
    if observed != FROZEN_ESTIMATOR_SHA256:
        raise AssertionError(
            f"frozen addressability estimator changed: {observed} != {FROZEN_ESTIMATOR_SHA256}"
        )


S3 = Tuple[int, int]
V4 = Tuple[int, int]
Triple = Tuple[S3, V4, int]


def s3_elements() -> Tuple[S3, ...]:
    return tuple((rotation, reflection) for rotation in range(3) for reflection in range(2))


def triple_elements() -> Tuple[Triple, ...]:
    v4 = tuple(itertools.product(range(2), repeat=2))
    return tuple(
        (left, right, bit)
        for left in s3_elements()
        for right in v4
        for bit in range(2)
    )


def triple_multiply(left: Triple, right: Triple) -> Triple:
    return (
        est.s3_multiply(left[0], right[0]),
        ((left[1][0] + right[1][0]) % 2, (left[1][1] + right[1][1]) % 2),
        (left[2] + right[2]) % 2,
    )


def natural_s3_representation(element: S3) -> est.Matrix:
    return est.s3_representation(element)


def c2_representation(element: int) -> est.Matrix:
    z = est.matrix(((1, 0), (0, -1)))
    return est.matrix_power(z, element)


def projective_v4_representation(element: V4) -> est.Matrix:
    x = est.matrix(((0, 1), (1, 0)))
    z = est.matrix(((1, 0), (0, -1)))
    return est.mmul(est.matrix_power(x, element[0]), est.matrix_power(z, element[1]))


def triple_representation(element: Triple) -> est.Matrix:
    return est.kron(
        est.kron(
            natural_s3_representation(element[0]),
            projective_v4_representation(element[1]),
        ),
        c2_representation(element[2]),
    )


def tuple_to_index(value: Tuple[int, int, int]) -> int:
    return value[0] * 4 + value[1] * 2 + value[2]


def index_to_tuple(index: int) -> Tuple[int, int, int]:
    return (index // 4, (index // 2) % 2, index % 2)


def main_encoding() -> est.Matrix:
    permutation = []
    phases = []
    for index in range(8):
        left, middle, right = index_to_tuple(index)
        encoded = (left ^ middle, middle ^ right, left ^ middle ^ right)
        permutation.append(tuple_to_index(encoded))
        exponent = (left + 2 * middle + 5 * right + 3 * left * right) % 24
        phases.append(est.ZETA ** exponent)
    relabelling = est.permutation_matrix(tuple(permutation))
    diagonal = tuple(
        tuple(phases[row] if row == column else est.ZERO for column in range(8))
        for row in range(8)
    )
    action = est.mmul(diagonal, relabelling)
    if not est.is_unitary(action):
        raise AssertionError("main encoding is not exactly unitary")
    return action


def gauge_action() -> est.Matrix:
    permutation = tuple((3 * index + 2) % 8 for index in range(8))
    if len(set(permutation)) != 8:
        raise AssertionError("gauge relabelling is not a permutation")
    phases = tuple(est.ZETA ** (3 * ((index * index + 2 * index) % 8)) for index in range(8))
    diagonal = tuple(
        tuple(phases[row] if row == column else est.ZERO for column in range(8))
        for row in range(8)
    )
    return est.mmul(diagonal, est.permutation_matrix(permutation))


def local_physical_phase_action() -> est.Matrix:
    imaginary = est.ZETA ** 6
    return (
        (est.INV_SQRT2, est.INV_SQRT2 * imaginary),
        (est.INV_SQRT2, -est.INV_SQRT2 * imaginary),
    )


def physical_phase_action() -> est.Matrix:
    action = est.kron(
        est.kron(local_physical_phase_action(), est.identity(2)),
        est.identity(2),
    )
    if not est.is_unitary(action):
        raise AssertionError("physical phase action is not exactly unitary")
    return action


def outer(left: est.Vector, right: est.Vector) -> est.Matrix:
    return tuple(
        tuple(a * b.conjugate() for b in right)
        for a in left
    )


def local_three_level_record(handle: str) -> est.RecordWitness:
    inv_sqrt3 = est.SQRT3 * Fraction(1, 3)
    inv_sqrt6 = est.INV_SQRT2 * inv_sqrt3
    trivial = est.vector((inv_sqrt3, inv_sqrt3, inv_sqrt3))
    first = est.vector((est.INV_SQRT2, -est.INV_SQRT2, 0))
    second = est.vector((inv_sqrt6, inv_sqrt6, -2 * inv_sqrt6))
    record_zero = tuple(
        est.INV_SQRT2 * (left + right)
        for left, right in zip(first, second)
    )
    record_one = tuple(
        est.INV_SQRT2 * (left - right)
        for left, right in zip(first, second)
    )
    alternative_zero = outer(first, first)
    alternative_one = est.madd(outer(second, second), outer(trivial, trivial))
    cut_zero = outer(record_zero, record_zero)
    cut_one = est.madd(outer(record_one, record_one), outer(trivial, trivial))
    write = est.madd(
        est.madd(outer(record_zero, first), outer(record_one, second)),
        outer(trivial, trivial),
    )
    preparation = tuple(
        est.INV_SQRT2 * (left + right)
        for left, right in zip(first, second)
    )
    witness = est.RecordWitness(
        handle=handle,
        preparations=(preparation,),
        alternative_projectors=(alternative_zero, alternative_one),
        cut_record_projectors=(cut_zero, cut_one),
        availability_probes=(cut_zero, cut_one),
        write=write,
        preserving=(est.identity(3),),
        erasing=(est.adjoint(write),),
        no_write=est.identity(3),
    )
    result = est.evaluate_record_witness(witness, est.identity(3), 3)
    if not result.passes_w3:
        raise AssertionError(f"local three-level record failed W3: {result}")
    return witness


def embed_local_matrix(value: est.Matrix, slot: int) -> est.Matrix:
    factors = [est.identity(2), est.identity(2), est.identity(2)]
    factors[slot] = value
    return est.kron(est.kron(factors[0], factors[1]), factors[2])


def embed_local_vector(value: est.Vector, slot: int) -> est.Vector:
    factors = [est.basis_vector(2, 0), est.basis_vector(2, 0), est.basis_vector(2, 0)]
    factors[slot] = value
    return est.vkron(est.vkron(factors[0], factors[1]), factors[2])


def embedded_record(slot: int) -> est.RecordWitness:
    local = est.two_level_record_witness(f"w{slot}")
    return est.RecordWitness(
        handle=local.handle,
        preparations=tuple(embed_local_vector(value, slot) for value in local.preparations),
        alternative_projectors=tuple(embed_local_matrix(value, slot) for value in local.alternative_projectors),
        cut_record_projectors=tuple(embed_local_matrix(value, slot) for value in local.cut_record_projectors),
        availability_probes=tuple(embed_local_matrix(value, slot) for value in local.availability_probes),
        write=embed_local_matrix(local.write, slot),
        preserving=tuple(embed_local_matrix(value, slot) for value in local.preserving),
        erasing=tuple(embed_local_matrix(value, slot) for value in local.erasing),
        no_write=embed_local_matrix(local.no_write, slot),
    )


def conjugate_record(witness: est.RecordWitness, action: est.Matrix) -> est.RecordWitness:
    return est.RecordWitness(
        handle=witness.handle,
        preparations=tuple(est.mv(action, value) for value in witness.preparations),
        alternative_projectors=tuple(est.conjugate_by(action, value) for value in witness.alternative_projectors),
        cut_record_projectors=tuple(est.conjugate_by(action, value) for value in witness.cut_record_projectors),
        availability_probes=tuple(est.conjugate_by(action, value) for value in witness.availability_probes),
        write=est.conjugate_by(action, witness.write),
        preserving=tuple(est.conjugate_by(action, value) for value in witness.preserving),
        erasing=tuple(est.conjugate_by(action, value) for value in witness.erasing),
        no_write=est.conjugate_by(action, witness.no_write),
    )


def monomial_action_data(action: est.Matrix) -> Tuple[Tuple[int, ...], Tuple[est.Q24, ...]]:
    """Return the exact basis image and phase for a monomial unitary.

    The held-out main encoding and the declared gauge control are monomial.
    Exploiting that fact here changes only fixture-construction cost; the
    frozen estimator still receives and checks the complete dense matrices.
    """

    dimension = len(action)
    if any(len(row) != dimension for row in action):
        raise ValueError("monomial action must be square")
    image = []
    phases = []
    used_rows = set()
    for column in range(dimension):
        entries = tuple(
            (row, action[row][column])
            for row in range(dimension)
            if action[row][column]
        )
        if len(entries) != 1:
            raise ValueError("action is not monomial")
        row, phase = entries[0]
        if row in used_rows or phase * phase.conjugate() != est.ONE:
            raise ValueError("action is not a monomial unitary")
        used_rows.add(row)
        image.append(row)
        phases.append(phase)
    if len(used_rows) != dimension:
        raise ValueError("action is not a monomial permutation")
    return tuple(image), tuple(phases)


def conjugate_matrix_monomial(value: est.Matrix, action: est.Matrix) -> est.Matrix:
    image, phases = monomial_action_data(action)
    dimension = len(image)
    result = [[est.ZERO for _ in range(dimension)] for _ in range(dimension)]
    for row in range(dimension):
        for column in range(dimension):
            entry = value[row][column]
            if entry:
                result[image[row]][image[column]] = (
                    phases[row] * entry * phases[column].conjugate()
                )
    return tuple(tuple(row) for row in result)


def apply_vector_monomial(value: est.Vector, action: est.Matrix) -> est.Vector:
    image, phases = monomial_action_data(action)
    result = [est.ZERO for _ in image]
    for index, entry in enumerate(value):
        if entry:
            result[image[index]] = phases[index] * entry
    return tuple(result)


def conjugate_record_monomial(
    witness: est.RecordWitness,
    action: est.Matrix,
) -> est.RecordWitness:
    return est.RecordWitness(
        handle=witness.handle,
        preparations=tuple(apply_vector_monomial(value, action) for value in witness.preparations),
        alternative_projectors=tuple(
            conjugate_matrix_monomial(value, action)
            for value in witness.alternative_projectors
        ),
        cut_record_projectors=tuple(
            conjugate_matrix_monomial(value, action)
            for value in witness.cut_record_projectors
        ),
        availability_probes=tuple(
            conjugate_matrix_monomial(value, action)
            for value in witness.availability_probes
        ),
        write=conjugate_matrix_monomial(witness.write, action),
        preserving=tuple(
            conjugate_matrix_monomial(value, action) for value in witness.preserving
        ),
        erasing=tuple(
            conjugate_matrix_monomial(value, action) for value in witness.erasing
        ),
        no_write=conjugate_matrix_monomial(witness.no_write, action),
    )


def conjugate_dataset_monomial(
    dataset: est.OperationalDataset,
    action: est.Matrix,
    handle: str,
) -> est.OperationalDataset:
    # Validate once; the exact sparse formula below is then equivalent to
    # action * value * action^dagger for every operational field.
    monomial_action_data(action)
    return est.OperationalDataset(
        handle=handle,
        dimension=dataset.dimension,
        operations=tuple(
            est.Operation(
                operation.handle,
                conjugate_matrix_monomial(operation.amplitude, action),
                operation.boundary_type,
                operation.independently_selectable,
            )
            for operation in dataset.operations
        ),
        composition_rows=dataset.composition_rows,
        generator_handles=dataset.generator_handles,
        preparations=tuple(
            apply_vector_monomial(value, action) for value in dataset.preparations
        ),
        probes=tuple(apply_vector_monomial(value, action) for value in dataset.probes),
        records=tuple(
            conjugate_record_monomial(value, action) for value in dataset.records
        ),
        gauge_actions=tuple(
            conjugate_matrix_monomial(value, action) for value in dataset.gauge_actions
        ),
        access_declaration=dataset.access_declaration,
        gauge_declaration=dataset.gauge_declaration,
    )


def with_records(dataset: est.OperationalDataset, records: Sequence[est.RecordWitness]) -> est.OperationalDataset:
    return est.OperationalDataset(
        handle=dataset.handle,
        dimension=dataset.dimension,
        operations=dataset.operations,
        composition_rows=dataset.composition_rows,
        generator_handles=dataset.generator_handles,
        preparations=dataset.preparations,
        probes=dataset.probes,
        records=tuple(records),
        gauge_actions=dataset.gauge_actions,
        access_declaration=dataset.access_declaration,
        gauge_declaration=dataset.gauge_declaration,
    )


def conjugate_dataset(
    dataset: est.OperationalDataset,
    action: est.Matrix,
    handle: str,
) -> est.OperationalDataset:
    return est.OperationalDataset(
        handle=handle,
        dimension=dataset.dimension,
        operations=tuple(
            est.Operation(
                operation.handle,
                est.conjugate_by(action, operation.amplitude),
                operation.boundary_type,
                operation.independently_selectable,
            )
            for operation in dataset.operations
        ),
        composition_rows=dataset.composition_rows,
        generator_handles=dataset.generator_handles,
        preparations=tuple(est.mv(action, value) for value in dataset.preparations),
        probes=tuple(est.mv(action, value) for value in dataset.probes),
        records=tuple(conjugate_record(value, action) for value in dataset.records),
        gauge_actions=tuple(est.conjugate_by(action, value) for value in dataset.gauge_actions),
        access_declaration=dataset.access_declaration,
        gauge_declaration=dataset.gauge_declaration,
    )


def opaque_handle(index: int) -> str:
    return f"k{(83 * index + 41) % 48:03d}"


def rename_dataset(
    dataset: est.OperationalDataset,
    handle: str,
    mapping: Mapping[str, str],
    generator_handles: Optional[Sequence[str]] = None,
    reverse_order: bool = False,
) -> est.OperationalDataset:
    operations = tuple(
        est.Operation(
            mapping[operation.handle],
            operation.amplitude,
            operation.boundary_type,
            operation.independently_selectable,
        )
        for operation in dataset.operations
    )
    rows = tuple(
        est.CompositionRow(
            mapping[row.left],
            mapping[row.right],
            row.context,
            row.status,
            None if row.result is None else mapping[row.result],
        )
        for row in dataset.composition_rows
    )
    if reverse_order:
        operations = tuple(reversed(operations))
        rows = tuple(reversed(rows))
    return est.OperationalDataset(
        handle=handle,
        dimension=dataset.dimension,
        operations=operations,
        composition_rows=rows,
        generator_handles=tuple(
            mapping[value] for value in (generator_handles or dataset.generator_handles)
        ),
        preparations=tuple(reversed(dataset.preparations)) if reverse_order else dataset.preparations,
        probes=tuple(reversed(dataset.probes)) if reverse_order else dataset.probes,
        records=tuple(reversed(dataset.records)) if reverse_order else dataset.records,
        gauge_actions=tuple(reversed(dataset.gauge_actions)) if reverse_order else dataset.gauge_actions,
        access_declaration=dataset.access_declaration + "; opaque handle presentation",
        gauge_declaration=dataset.gauge_declaration,
    )


def replace_row_status(
    dataset: est.OperationalDataset,
    pairs: FrozenSet[Tuple[str, str]],
    status: str,
    handle: str,
) -> est.OperationalDataset:
    rows = []
    for row in dataset.composition_rows:
        if (row.left, row.right) not in pairs:
            rows.append(row)
        elif status == est.UNAVAILABLE:
            rows.append(est.CompositionRow(row.left, row.right, row.context, status, None))
        else:
            rows.append(est.CompositionRow(row.left, row.right, row.context, status, row.result))
    return est.OperationalDataset(
        handle=handle,
        dimension=dataset.dimension,
        operations=dataset.operations,
        composition_rows=tuple(rows),
        generator_handles=dataset.generator_handles,
        preparations=dataset.preparations,
        probes=dataset.probes,
        records=dataset.records,
        gauge_actions=dataset.gauge_actions,
        access_declaration=dataset.access_declaration + f"; {status.lower()} mixed-pair control",
        gauge_declaration=dataset.gauge_declaration,
    )


@dataclass(frozen=True)
class MainTruth:
    element_by_handle: Mapping[str, Triple]
    factor_elements: Tuple[FrozenSet[Triple], ...]
    generator_elements: Tuple[Triple, ...]
    changed_generator_elements: Tuple[Triple, ...]
    required_record_triple: Tuple[FrozenSet[int], ...]


@dataclass(frozen=True)
class FixtureBundle:
    main: est.OperationalDataset
    renamed_generator_variant: est.OperationalDataset
    gauge_variant: est.OperationalDataset
    phase_variant: est.OperationalDataset
    address_blocked: est.OperationalDataset
    collapsed: est.OperationalDataset
    ambiguity: est.OperationalDataset
    irreducible: est.OperationalDataset
    bridge_positive_source: est.OperationalDataset
    bridge_positive_target: est.OperationalDataset
    bridge_negative: est.OperationalDataset
    encoding: est.Matrix
    gauge: est.Matrix
    phase_action: est.Matrix
    truth: MainTruth


def build_main_unencoded() -> Tuple[est.OperationalDataset, Dict[str, Triple], Tuple[Triple, ...]]:
    elements = triple_elements()
    identity_local = (0, 0)
    generators: Tuple[Triple, ...] = (
        ((1, 0), identity_local, 0),
        ((0, 1), identity_local, 0),
        (identity_local, (1, 0), 0),
        (identity_local, (0, 1), 0),
        (identity_local, identity_local, 1),
    )
    base = est.build_group_dataset(
        "held-out-s3-v4-c2-unencoded",
        elements,
        triple_multiply,
        triple_representation,
        generators,
    )
    base = with_records(base, tuple(embedded_record(slot) for slot in range(2)))
    old_to_new = {operation.handle: opaque_handle(index) for index, operation in enumerate(base.operations)}
    opaque = rename_dataset(base, "held-out-s3-v4-c2-opaque", old_to_new)
    element_by_handle = {
        old_to_new[f"u{index:03d}"]: element for index, element in enumerate(elements)
    }
    return opaque, element_by_handle, generators


def build_phase_unencoded() -> est.OperationalDataset:
    """Build the physical complex-phase control before the global encoding.

    The qutrit Fourier transform is not in the declared monomial boundary
    gauge.  Conjugating the natural S3 representation by it changes exact
    operational signatures while preserving the abstract composition object.
    Constructing the transformed 3x3 factors directly avoids an irrelevant
    dense 27x27 fixture-generation bottleneck.
    """

    elements = triple_elements()
    identity_local = (0, 0)
    generators: Tuple[Triple, ...] = (
        ((1, 0), identity_local, 0),
        ((0, 1), identity_local, 0),
        (identity_local, (1, 0), 0),
        (identity_local, (0, 1), 0),
        (identity_local, identity_local, 1),
    )
    fourier = local_physical_phase_action()

    def representation(element: Triple) -> est.Matrix:
        phased_first = est.conjugate_by(
            fourier,
            natural_s3_representation(element[0]),
        )
        return est.kron(
            est.kron(phased_first, projective_v4_representation(element[1])),
            c2_representation(element[2]),
        )

    base = est.build_group_dataset(
        "held-out-s3-v4-c2-phase-unencoded",
        elements,
        triple_multiply,
        representation,
        generators,
    )
    local_phase_record = conjugate_record(est.two_level_record_witness("w0"), fourier)
    records = []
    for slot in range(2):
        local = (
            local_phase_record
            if slot == 0
            else est.two_level_record_witness(f"w{slot}")
        )
        records.append(
            est.RecordWitness(
                handle=f"w{slot}",
                preparations=tuple(embed_local_vector(value, slot) for value in local.preparations),
                alternative_projectors=tuple(
                    embed_local_matrix(value, slot) for value in local.alternative_projectors
                ),
                cut_record_projectors=tuple(
                    embed_local_matrix(value, slot) for value in local.cut_record_projectors
                ),
                availability_probes=tuple(
                    embed_local_matrix(value, slot) for value in local.availability_probes
                ),
                write=embed_local_matrix(local.write, slot),
                preserving=tuple(embed_local_matrix(value, slot) for value in local.preserving),
                erasing=tuple(embed_local_matrix(value, slot) for value in local.erasing),
                no_write=embed_local_matrix(local.no_write, slot),
            )
        )
    base = with_records(base, tuple(records))
    mapping = {operation.handle: opaque_handle(index) for index, operation in enumerate(base.operations)}
    return rename_dataset(base, "held-out-s3-v4-c2-phase-opaque", mapping)


def build_ambiguity_dataset() -> est.OperationalDataset:
    elements = tuple(itertools.product(range(2), repeat=2))

    def multiply(left, right):
        return ((left[0] + right[0]) % 2, (left[1] + right[1]) % 2)

    def representation(element):
        permutation = tuple(
            elements.index(multiply(element, value)) for value in elements
        )
        return est.permutation_matrix(permutation)

    return est.build_group_dataset(
        "ambiguity-v4-regular",
        elements,
        multiply,
        representation,
        ((1, 0), (0, 1)),
    )


def build_irreducible_dataset() -> est.OperationalDataset:
    elements = s3_elements()
    return est.build_group_dataset(
        "irreducible-s3-natural",
        elements,
        est.s3_multiply,
        natural_s3_representation,
        ((1, 0), (0, 1)),
    )


def four_dimensional_record(handle: str) -> est.RecordWitness:
    local = est.two_level_record_witness(handle)
    other = est.identity(2)
    return est.RecordWitness(
        handle=handle,
        preparations=tuple(est.vkron(value, est.basis_vector(2, 0)) for value in local.preparations),
        alternative_projectors=tuple(est.kron(value, other) for value in local.alternative_projectors),
        cut_record_projectors=tuple(est.kron(value, other) for value in local.cut_record_projectors),
        availability_probes=tuple(est.kron(value, other) for value in local.availability_probes),
        write=est.kron(local.write, other),
        preserving=tuple(est.kron(value, other) for value in local.preserving),
        erasing=tuple(est.kron(value, other) for value in local.erasing),
        no_write=est.kron(local.no_write, other),
    )


def build_bridge_dataset(kind: str, handle: str) -> est.OperationalDataset:
    if kind == "v4":
        elements = tuple(itertools.product(range(2), repeat=2))

        def multiply(left, right):
            return ((left[0] + right[0]) % 2, (left[1] + right[1]) % 2)

    elif kind == "c4":
        elements = tuple(range(4))

        def multiply(left, right):
            return (left + right) % 4

    else:
        raise ValueError(f"unknown bridge group {kind}")

    def representation(element):
        permutation = tuple(
            elements.index(multiply(element, value)) for value in elements
        )
        return est.permutation_matrix(permutation)

    generators = ((1, 0), (0, 1)) if kind == "v4" else (1,)
    base = est.build_group_dataset(handle, elements, multiply, representation, generators)
    return with_records(base, (four_dimensional_record("bridge-record"),))


def build_fixture_bundle() -> FixtureBundle:
    assert_frozen_estimator()
    unencoded, element_by_handle, generators = build_main_unencoded()
    encoding = main_encoding()
    main = conjugate_dataset_monomial(
        unencoded, encoding, "held-out-addressability-main"
    )
    changed_generators = (
        generators[0],
        generators[1],
        generators[2],
        triple_multiply(generators[1], generators[3]),
        generators[4],
    )
    handle_by_element = {element: handle for handle, element in element_by_handle.items()}
    second_mapping = {
        operation.handle: f"r{(47 * index + 19) % 48:03d}"
        for index, operation in enumerate(main.operations)
    }
    renamed = rename_dataset(
        main,
        "renamed-generator-presentation",
        second_mapping,
        generator_handles=tuple(handle_by_element[value] for value in changed_generators),
        reverse_order=True,
    )
    gauge = gauge_action()
    gauge_variant = conjugate_dataset_monomial(
        main, gauge, "gauge-conjugate-main"
    )
    phase_unencoded = physical_phase_action()
    phase = conjugate_matrix_monomial(phase_unencoded, encoding)
    phase_variant = conjugate_dataset_monomial(
        build_phase_unencoded(), encoding, "physical-phase-main"
    )
    left_handle = handle_by_element[generators[1]]
    right_handle = handle_by_element[generators[3]]
    mixed_pairs = frozenset(((left_handle, right_handle), (right_handle, left_handle)))
    address_blocked = replace_row_status(
        main, mixed_pairs, est.UNAVAILABLE, "same-matrices-mixed-composites-unavailable"
    )
    collapsed = replace_row_status(
        main, mixed_pairs, est.COLLAPSED, "same-matrices-mixed-composites-collapsed"
    )
    ambiguity = build_ambiguity_dataset()
    irreducible = build_irreducible_dataset()
    bridge_source = build_bridge_dataset("v4", "bridge-v4-source")
    bridge_action = est.permutation_matrix((0, 2, 1, 3))
    bridge_target = conjugate_dataset(
        bridge_source, bridge_action, "bridge-v4-positive-target"
    )
    bridge_negative = build_bridge_dataset("c4", "bridge-c4-negative")
    identities = ((0, 0), (0, 0), 0)
    factor_elements = tuple(
        frozenset(
            element
            for element in triple_elements()
            if all(
                element[index] == identities[index]
                for index in range(3)
                if index != factor
            )
        )
        for factor in range(3)
    )
    truth = MainTruth(
        element_by_handle=element_by_handle,
        factor_elements=factor_elements,
        generator_elements=generators,
        changed_generator_elements=changed_generators,
        required_record_triple=(
            frozenset((0,)),
            frozenset((0, 1)),
            frozenset((0, 2)),
        ),
    )
    return FixtureBundle(
        main=main,
        renamed_generator_variant=renamed,
        gauge_variant=gauge_variant,
        phase_variant=phase_variant,
        address_blocked=address_blocked,
        collapsed=collapsed,
        ambiguity=ambiguity,
        irreducible=irreducible,
        bridge_positive_source=bridge_source,
        bridge_positive_target=bridge_target,
        bridge_negative=bridge_negative,
        encoding=encoding,
        gauge=gauge,
        phase_action=phase,
        truth=truth,
    )


if __name__ == "__main__":
    bundle = build_fixture_bundle()
    print(
        {
            "estimator_hash": sha256(ESTIMATOR_PATH),
            "main_dimension": bundle.main.dimension,
            "main_operations": len(bundle.main.operations),
            "main_composition_rows": len(bundle.main.composition_rows),
            "main_records": len(bundle.main.records),
            "ambiguity_dimension": bundle.ambiguity.dimension,
            "bridge_dimension": bundle.bridge_positive_source.dimension,
        }
    )
