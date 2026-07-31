#!/usr/bin/env python3
"""Single post-freeze held-out fixture for RQ0-L0 computational certification.

This file first exists after estimator freeze commit ``d881a3e`` and its
Git-object attestation ``59011af``.  It defines one exact heterogeneous
composition object and one irregular record-bearing access family.  The
frozen estimator receives only the serialized ``OperationalDataset``; only
the scorer may read ``held_out_truth``.

The fixture is immutable once created.  It is not a topology, causal, field,
or gravitational model.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import FrozenSet, Mapping, Sequence, Tuple

try:
    from .rq0_l0_certification_estimator_exact import (
        AccessContext,
        CompositionRow,
        FieldDatum,
        GaugeDatum,
        IMPLEMENTED,
        MonomialLaw,
        OperationClass,
        OperationalDataset,
        ReadoutDatum,
        RecordCandidate,
        fourier_record_witness,
        permutation_law,
    )
except ImportError:
    from rq0_l0_certification_estimator_exact import (
        AccessContext,
        CompositionRow,
        FieldDatum,
        GaugeDatum,
        IMPLEMENTED,
        MonomialLaw,
        OperationClass,
        OperationalDataset,
        ReadoutDatum,
        RecordCandidate,
        fourier_record_witness,
        permutation_law,
    )


FIXTURE_SCHEMA = "rq0-l0-compcert-heldout-c2-c3-c4-s3-v1"
ESTIMATOR_FREEZE_COMMIT = "d881a3e"
ESTIMATOR_FROZEN_SHA256 = "a9f8f93a01d7bf84d7dfde1e43b5c14a0111e9722b42d8e3dc999de887630f8b"
PROOF_FROZEN_SHA256 = "5839fedcb680cb24e0ba778aff6e00aa92ac4f98191753693abbad1a54bbcd2d"


Permutation3 = Tuple[int, int, int]
HeldOutElement = Tuple[int, int, int, Permutation3]
IDENTITY_PERMUTATION: Permutation3 = (0, 1, 2)


def abstract_elements() -> Tuple[HeldOutElement, ...]:
    return tuple(
        (c2, c3, c4, permutation)
        for c2 in range(2)
        for c3 in range(3)
        for c4 in range(4)
        for permutation in itertools.permutations(range(3))
    )


def _permutation_product(
    left: Permutation3,
    right: Permutation3,
) -> Permutation3:
    return tuple(left[right[index]] for index in range(3))


def abstract_multiply(
    left: HeldOutElement,
    right: HeldOutElement,
) -> HeldOutElement:
    return (
        (left[0] + right[0]) % 2,
        (left[1] + right[1]) % 3,
        (left[2] + right[2]) % 4,
        _permutation_product(left[3], right[3]),
    )


def _encode_index(
    coordinates: Sequence[int],
    dimensions: Sequence[int],
) -> int:
    value = 0
    for coordinate, dimension in zip(coordinates, dimensions):
        value = value * dimension + coordinate
    return value


def _decode_index(
    index: int,
    dimensions: Sequence[int],
) -> Tuple[int, ...]:
    coordinates = []
    value = index
    for dimension in reversed(dimensions):
        coordinates.append(value % dimension)
        value //= dimension
    return tuple(reversed(coordinates))


def _tensor_monomial(laws: Sequence[MonomialLaw]) -> MonomialLaw:
    dimensions = tuple(value.dimension for value in laws)
    total = 1
    for dimension in dimensions:
        total *= dimension
    permutation = []
    phases = []
    for index in range(total):
        coordinates = _decode_index(index, dimensions)
        targets = tuple(
            law.permutation[coordinate]
            for law, coordinate in zip(laws, coordinates)
        )
        permutation.append(_encode_index(targets, dimensions))
        phases.append(
            sum(
                law.phases[coordinate]
                for law, coordinate in zip(laws, coordinates)
            )
            % 24
        )
    return MonomialLaw(tuple(permutation), tuple(phases))


def _exact_character(order: int, exponent: int) -> MonomialLaw:
    if order not in (2, 3, 4):
        raise ValueError("held-out exact character supports orders 2, 3, 4")
    return MonomialLaw(
        (0, 1),
        (0, ((24 // order) * exponent) % 24),
    )


def _raw_representation(value: HeldOutElement) -> MonomialLaw:
    return _tensor_monomial(
        (
            _exact_character(2, value[0]),
            _exact_character(3, value[1]),
            _exact_character(4, value[2]),
            permutation_law(value[3]),
        )
    )


def _phase_frame(dimension: int) -> MonomialLaw:
    phases = tuple(
        (5 * index * index + 7 * index + 3 * (index % 5)) % 24
        for index in range(dimension)
    )
    return MonomialLaw(tuple(range(dimension)), phases)


def _representation(value: HeldOutElement) -> MonomialLaw:
    raw = _raw_representation(value)
    frame = _phase_frame(raw.dimension)
    return frame.after(raw).after(frame.inverse())


def _identity_element() -> HeldOutElement:
    return (0, 0, 0, IDENTITY_PERMUTATION)


def _selectable_generators() -> FrozenSet[HeldOutElement]:
    return frozenset(
        (
            _identity_element(),
            (1, 0, 0, IDENTITY_PERMUTATION),
            (0, 1, 0, IDENTITY_PERMUTATION),
            (0, 0, 1, IDENTITY_PERMUTATION),
            (0, 0, 0, (1, 0, 2)),
            (0, 0, 0, (1, 2, 0)),
        )
    )


def _factor_elements(
    atom: int,
    elements: Sequence[HeldOutElement],
) -> Tuple[HeldOutElement, ...]:
    if atom == 0:
        return tuple(
            value
            for value in elements
            if value[1] == 0
            and value[2] == 0
            and value[3] == IDENTITY_PERMUTATION
        )
    if atom == 1:
        return tuple(
            value
            for value in elements
            if value[0] == 0
            and value[2] == 0
            and value[3] == IDENTITY_PERMUTATION
        )
    if atom == 2:
        return tuple(
            value
            for value in elements
            if value[0] == 0
            and value[1] == 0
            and value[3] == IDENTITY_PERMUTATION
        )
    if atom == 3:
        return tuple(
            value
            for value in elements
            if value[0] == value[1] == value[2] == 0
        )
    raise ValueError("held-out fixture has four construction atoms")


def _scope_elements(
    atom_set: Sequence[int],
    elements: Sequence[HeldOutElement],
) -> Tuple[HeldOutElement, ...]:
    atoms = set(atom_set)
    return tuple(
        value
        for value in elements
        if (
            (0 in atoms or value[0] == 0)
            and (1 in atoms or value[1] == 0)
            and (2 in atoms or value[2] == 0)
            and (3 in atoms or value[3] == IDENTITY_PERMUTATION)
        )
    )


def _ambient_binary_resolution(atom: int) -> Tuple[FrozenSet[int], ...]:
    dimensions = (2, 2, 2, 3)
    zero = frozenset(
        index
        for index in range(24)
        if _decode_index(index, dimensions)[atom] == 0
    )
    nonzero = frozenset(range(24)) - zero
    return zero, nonzero


CONTEXT_ATOM_SETS: Tuple[Tuple[int, ...], ...] = (
    (0, 1, 2),
    (0, 2, 3),
    (0, 1, 3),
    (1, 2),
)


def build_dataset() -> OperationalDataset:
    elements = abstract_elements()
    element_index = {value: index for index, value in enumerate(elements)}
    laws = tuple(_representation(value) for value in elements)
    handles = tuple(f"theta-operation-{index:03d}" for index in range(len(elements)))
    selectable = _selectable_generators()

    operations = tuple(
        OperationClass(
            handle=handles[index],
            source_type="q",
            target_type="q",
            law=laws[index],
            observed_signature=laws[index].signature(),
            independently_selectable=value in selectable,
        )
        for index, value in enumerate(elements)
    )

    rows = []
    for left_index, left in enumerate(elements):
        for right_index, right in enumerate(elements):
            result_index = element_index[abstract_multiply(left, right)]
            supplied_law = laws[result_index]
            rows.append(
                CompositionRow(
                    left=handles[left_index],
                    right=handles[right_index],
                    tau="q|q|q",
                    status=IMPLEMENTED,
                    result_class=handles[result_index],
                    law=supplied_law,
                    observed_signature=supplied_law.signature(),
                )
            )

    preparations = tuple(
        FieldDatum(f"theta-preparation-{atom}", "q", (atom, 307 + atom))
        for atom in range(4)
    )
    probes = tuple(
        FieldDatum(f"theta-probe-{atom}", "q", (atom, 401 + atom))
        for atom in range(4)
    )
    readouts = tuple(
        ReadoutDatum(
            f"theta-readout-{atom}",
            "q",
            _ambient_binary_resolution(atom),
        )
        for atom in range(4)
    )

    records = []
    for atom in range(4):
        support = _factor_elements(atom, elements)
        records.append(
            RecordCandidate(
                handle=f"theta-record-{atom}",
                boundary_type="q",
                access_operations=tuple(
                    handles[element_index[value]]
                    for value in support
                    if value in selectable
                ),
                witness=fourier_record_witness(
                    2, f"theta-w3-witness-{atom}"
                ),
                ambient_projector_resolution=_ambient_binary_resolution(atom),
            )
        )

    gauge_generators = (
        (1, 0, 0, IDENTITY_PERMUTATION),
        (0, 1, 0, IDENTITY_PERMUTATION),
        (0, 0, 1, IDENTITY_PERMUTATION),
        (0, 0, 0, (1, 0, 2)),
    )
    gauges = tuple(
        GaugeDatum(
            f"theta-gauge-{atom}",
            laws[element_index[value]],
        )
        for atom, value in enumerate(gauge_generators)
    )

    contexts = []
    for ordinal, atom_set in enumerate(CONTEXT_ATOM_SETS):
        scope = _scope_elements(atom_set, elements)
        contexts.append(
            AccessContext(
                handle=f"theta-context-{ordinal}",
                boundary_type="q",
                operation_handles=tuple(
                    handles[element_index[value]] for value in scope
                ),
                preparation_handles=tuple(
                    f"theta-preparation-{atom}" for atom in atom_set
                ),
                probe_handles=tuple(
                    f"theta-probe-{atom}" for atom in atom_set
                ),
                readout_handles=tuple(
                    f"theta-readout-{atom}" for atom in atom_set
                ),
                record_handles=tuple(
                    f"theta-record-{atom}" for atom in atom_set
                ),
                gauge_handles=tuple(
                    f"theta-gauge-{atom}" for atom in atom_set
                ),
            )
        )

    return OperationalDataset(
        handle="theta-heldout-amplitude-instrument",
        carrier_dimension=24,
        operations=operations,
        composition_rows=tuple(rows),
        preparations=preparations,
        contexts=tuple(contexts),
        probes=probes,
        readouts=readouts,
        records=tuple(records),
        gauge_actions=gauges,
        access_postulate=(
            "POSTULATE: complete exact finite row access, six independently "
            "selectable operations, and four selective operational contexts"
        ),
    )


@dataclass(frozen=True)
class HeldOutTruth:
    schema: str
    abstract_order: int
    carrier_dimension: int
    factor_orders: Tuple[int, ...]
    independently_selectable: int
    composite_only: int
    complete_rows: int
    context_atom_sets: Tuple[Tuple[int, ...], ...]
    regional_atom_sets: Tuple[Tuple[int, ...], ...]
    regional_objects: int
    regional_arrows: int
    fact_maps: int
    nonempty_pair_instances: int
    nonvacuous_triples: int
    universal_atoms: Tuple[int, ...]
    complete_proper_boolean: bool


def held_out_truth() -> HeldOutTruth:
    return HeldOutTruth(
        schema=FIXTURE_SCHEMA,
        abstract_order=144,
        carrier_dimension=24,
        factor_orders=(2, 3, 4, 6),
        independently_selectable=6,
        composite_only=138,
        complete_rows=20_736,
        context_atom_sets=CONTEXT_ATOM_SETS,
        regional_atom_sets=(
            (0,),
            (1,),
            (2,),
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 2),
            (0, 1, 2),
            (0, 1, 3),
            (0, 2, 3),
        ),
        regional_objects=10,
        regional_arrows=31,
        fact_maps=31,
        nonempty_pair_instances=6,
        nonvacuous_triples=3,
        universal_atoms=(),
        complete_proper_boolean=False,
    )


def construction_metadata() -> Mapping[str, object]:
    return {
        "schema": FIXTURE_SCHEMA,
        "estimator_freeze_commit": ESTIMATOR_FREEZE_COMMIT,
        "abstract_description": "C2 x C3 x C4 x S3",
        "truth_visible_to_estimator": False,
        "post_freeze_fixture": True,
        "exact_field": "Q(zeta_24)",
        "random_seed": None,
    }
