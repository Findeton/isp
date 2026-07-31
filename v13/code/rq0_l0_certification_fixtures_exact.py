#!/usr/bin/env python3
"""Post-freeze fixture for the final RQ0-L0 certification cycle.

This module was created only after estimator commit 3b9d88a.  It defines one
new heterogeneous abstract composition family.  It does not import or reuse
the old S3^3 constructors, truth object, factor multiset, or proper-Boolean
atlas.

Only the scorer may read ``held_out_truth``.  The frozen estimator receives
only ``dataset_to_data(build_main_dataset(...))``.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Dict, FrozenSet, Mapping, Sequence, Tuple

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
        RecordWitness,
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
        RecordWitness,
        fourier_record_witness,
        permutation_law,
    )


FIXTURE_SCHEMA = "rq0-l0-final-fresh-heterogeneous-v1"
ESTIMATOR_FREEZE_COMMIT = "3b9d88a"
ESTIMATOR_FROZEN_SHA256 = "c1d3c3b36df71ed80b9ca9152be3d5a97f4d4c1c88ab9f3b0defd360ed14a5c3"


# The new abstract law is C2 x C3 x C4 x D4, but no factor label or truth is
# serialized into the estimator input.  Elements are opaque operation handles
# there.  D4 is represented as (rotation, reflection) with
# (r,s)(r',s') = (r + (-1)^s r', s+s').
FreshElement = Tuple[int, int, int, int, int]


def fresh_elements() -> Tuple[FreshElement, ...]:
    return tuple(
        (c2, c3, c4, rotation, reflection)
        for c2 in range(2)
        for c3 in range(3)
        for c4 in range(4)
        for rotation in range(4)
        for reflection in range(2)
    )


def fresh_multiply(left: FreshElement, right: FreshElement) -> FreshElement:
    sign = -1 if left[4] else 1
    return (
        (left[0] + right[0]) % 2,
        (left[1] + right[1]) % 3,
        (left[2] + right[2]) % 4,
        (left[3] + sign * right[3]) % 4,
        (left[4] + right[4]) % 2,
    )


def _encode_index(coordinates: Sequence[int], dimensions: Sequence[int]) -> int:
    value = 0
    for coordinate, dimension in zip(coordinates, dimensions):
        value = value * dimension + coordinate
    return value


def _decode_index(index: int, dimensions: Sequence[int]) -> Tuple[int, ...]:
    coordinates = []
    value = index
    for dimension in reversed(dimensions):
        coordinates.append(value % dimension)
        value //= dimension
    return tuple(reversed(coordinates))


def tensor_monomial(laws: Sequence[MonomialLaw]) -> MonomialLaw:
    dimensions = tuple(value.dimension for value in laws)
    total = 1
    for dimension in dimensions:
        total *= dimension
    permutation = []
    phases = []
    for index in range(total):
        coordinates = _decode_index(index, dimensions)
        targets = tuple(law.permutation[coordinate] for law, coordinate in zip(laws, coordinates))
        permutation.append(_encode_index(targets, dimensions))
        phases.append(sum(law.phases[coordinate] for law, coordinate in zip(laws, coordinates)) % 24)
    return MonomialLaw(tuple(permutation), tuple(phases))


def _cyclic_two_level(order: int, exponent: int) -> MonomialLaw:
    if order not in (2, 3, 4):
        raise ValueError("fresh two-level character supports orders 2, 3, 4")
    step = 24 // order
    return MonomialLaw((0, 1), (0, (step * exponent) % 24))


def _square_dihedral(rotation: int, reflection: int) -> MonomialLaw:
    sign = -1 if reflection else 1
    return permutation_law(tuple((rotation + sign * vertex) % 4 for vertex in range(4)))


def _phase_frame(dimension: int, variant: str) -> MonomialLaw:
    if variant == "base":
        phases = tuple((7 * index * index + 5 * index + 3 * (index % 4)) % 24 for index in range(dimension))
    elif variant == "physical-contrast":
        phases = tuple((11 * index * index + index + 9 * (index % 3)) % 24 for index in range(dimension))
    elif variant in ("gauge-character", "carrier-relabel"):
        phases = tuple((7 * index * index + 5 * index + 3 * (index % 4)) % 24 for index in range(dimension))
    else:
        raise ValueError(f"unknown fixture variant {variant}")
    return MonomialLaw(tuple(range(dimension)), phases)


def _carrier_relabelling(dimension: int) -> MonomialLaw:
    # Affine permutation i -> 5i+7 mod 32; 5 is invertible modulo 32.
    return permutation_law(tuple((5 * index + 7) % dimension for index in range(dimension)))


def _raw_representation(value: FreshElement) -> MonomialLaw:
    return tensor_monomial(
        (
            _cyclic_two_level(2, value[0]),
            _cyclic_two_level(3, value[1]),
            _cyclic_two_level(4, value[2]),
            _square_dihedral(value[3], value[4]),
        )
    )


def _representation(value: FreshElement, variant: str) -> MonomialLaw:
    raw = _raw_representation(value)
    frame = _phase_frame(raw.dimension, variant)
    law = frame.after(raw).after(frame.inverse())
    if variant == "gauge-character":
        # A genuine one-dimensional C3 character: global row phase only.
        phase = (8 * value[1]) % 24
        law = MonomialLaw(law.permutation, tuple((entry + phase) % 24 for entry in law.phases))
    if variant == "carrier-relabel":
        law = law.conjugated(_carrier_relabelling(raw.dimension))
    return law


def _selected(value: FreshElement) -> bool:
    generators = {
        (0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1),
    }
    return value in generators


def _factor_subgroup(atom: int, elements: Sequence[FreshElement]) -> Tuple[FreshElement, ...]:
    if atom == 0:
        return tuple(value for value in elements if value[1:] == (0, 0, 0, 0))
    if atom == 1:
        return tuple(value for value in elements if value[0] == 0 and value[2:] == (0, 0, 0))
    if atom == 2:
        return tuple(value for value in elements if value[:2] == (0, 0) and value[3:] == (0, 0))
    if atom == 3:
        return tuple(value for value in elements if value[:3] == (0, 0, 0))
    raise ValueError("fresh fixture has four hidden construction atoms")


def _scope_elements(atom_set: Sequence[int], elements: Sequence[FreshElement]) -> Tuple[FreshElement, ...]:
    atoms = set(atom_set)
    return tuple(
        value
        for value in elements
        if (
            (0 in atoms or value[0] == 0)
            and (1 in atoms or value[1] == 0)
            and (2 in atoms or value[2] == 0)
            and (3 in atoms or value[3:] == (0, 0))
        )
    )


def _ambient_resolution(atom: int, variant: str) -> Tuple[FrozenSet[int], ...]:
    dimensions = (2, 2, 2, 4)
    sectors = []
    for outcome in range(dimensions[atom]):
        sectors.append(
            frozenset(
                index
                for index in range(32)
                if _decode_index(index, dimensions)[atom] == outcome
            )
        )
    if variant == "carrier-relabel":
        relabel = _carrier_relabelling(32)
        sectors = [
            frozenset(relabel.permutation[index] for index in sector)
            for sector in sectors
        ]
    return tuple(sectors)


def _rename_record_witness(value: RecordWitness, handle: str) -> RecordWitness:
    return RecordWitness(
        handle=handle,
        preparations=value.preparations,
        alternative_projectors=value.alternative_projectors,
        cut_record_projectors=value.cut_record_projectors,
        availability_probes=value.availability_probes,
        write=value.write,
        preserving=value.preserving,
        erasing=value.erasing,
        no_write=value.no_write,
    )


def build_main_dataset(variant: str = "base", rename_handles: bool = False) -> OperationalDataset:
    if variant not in ("base", "physical-contrast", "gauge-character", "carrier-relabel"):
        raise ValueError("unknown main-fixture variant")
    elements = fresh_elements()
    element_index = {value: index for index, value in enumerate(elements)}
    laws = tuple(_representation(value, variant) for value in elements)

    prefix = "opaque-renamed" if rename_handles else "opaque"
    operation_handles = tuple(f"{prefix}-operation-{index:03d}" for index in range(len(elements)))
    operations = tuple(
        OperationClass(
            handle=operation_handles[index],
            source_type="q",
            target_type="q",
            law=laws[index],
            observed_signature=laws[index].signature(),
            independently_selectable=_selected(value),
        )
        for index, value in enumerate(elements)
    )

    rows = []
    for left_index, left in enumerate(elements):
        for right_index, right in enumerate(elements):
            result_index = element_index[fresh_multiply(left, right)]
            # M is supplied from the independently constructed result-law
            # table.  The estimator separately compares it with composition.
            supplied_law = laws[result_index]
            rows.append(
                CompositionRow(
                    left=operation_handles[left_index],
                    right=operation_handles[right_index],
                    tau="q|q|q",
                    status=IMPLEMENTED,
                    result_class=operation_handles[result_index],
                    law=supplied_law,
                    observed_signature=supplied_law.signature(),
                )
            )

    preparations = tuple(
        FieldDatum(f"{prefix}-preparation-{atom}", "q", (atom, 101 + atom))
        for atom in range(4)
    )
    probes = tuple(
        FieldDatum(f"{prefix}-probe-{atom}", "q", (atom, 211 + atom))
        for atom in range(4)
    )
    readouts = tuple(
        ReadoutDatum(
            f"{prefix}-readout-{atom}",
            "q",
            _ambient_resolution(atom, variant),
        )
        for atom in range(4)
    )

    records = []
    for atom in range(4):
        subgroup = _factor_subgroup(atom, elements)
        local_levels = 4 if atom == 3 else 2
        witness = fourier_record_witness(local_levels, f"{prefix}-witness-{atom}")
        records.append(
            RecordCandidate(
                handle=f"{prefix}-record-{atom}",
                boundary_type="q",
                access_operations=tuple(operation_handles[element_index[value]] for value in subgroup if _selected(value)),
                witness=witness,
                ambient_projector_resolution=_ambient_resolution(atom, variant),
            )
        )

    # These are presentation/gauge actions carried by every corresponding
    # regional instrument.  They are exact operational data, not factor names.
    gauge_actions = []
    gauge_elements = (
        (1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
    )
    for atom, value in enumerate(gauge_elements):
        gauge_actions.append(GaugeDatum(f"{prefix}-gauge-{atom}", laws[element_index[value]]))

    # Selective non-Boolean context family.  It is not the old complete
    # proper-Boolean family and has several differently shaped overlaps.
    context_atom_sets = ((0, 1), (1, 2), (2, 3), (0, 3), (0, 1, 2))
    contexts = []
    for ordinal, atom_set in enumerate(context_atom_sets):
        scope = _scope_elements(atom_set, elements)
        contexts.append(
            AccessContext(
                handle=f"{prefix}-context-{ordinal}",
                boundary_type="q",
                operation_handles=tuple(operation_handles[element_index[value]] for value in scope),
                preparation_handles=tuple(f"{prefix}-preparation-{atom}" for atom in atom_set),
                probe_handles=tuple(f"{prefix}-probe-{atom}" for atom in atom_set),
                readout_handles=tuple(f"{prefix}-readout-{atom}" for atom in atom_set),
                record_handles=tuple(f"{prefix}-record-{atom}" for atom in atom_set),
                gauge_handles=tuple(f"{prefix}-gauge-{atom}" for atom in atom_set),
            )
        )

    return OperationalDataset(
        handle=f"{prefix}-fresh-heterogeneous-{variant}",
        carrier_dimension=32,
        operations=operations,
        composition_rows=tuple(rows),
        preparations=preparations,
        contexts=tuple(contexts),
        probes=probes,
        readouts=readouts,
        records=tuple(records),
        gauge_actions=tuple(gauge_actions),
        access_postulate=(
            "POSTULATE: complete exact finite row tomography, five selective "
            "operational access contexts, and six independently selectable generators"
        ),
    )


@dataclass(frozen=True)
class HeldOutCertificationTruth:
    schema: str
    abstract_order: int
    carrier_dimension: int
    factor_orders: Tuple[int, ...]
    independently_selectable_count: int
    context_atom_sets: Tuple[Tuple[int, ...], ...]
    regional_atom_sets: Tuple[Tuple[int, ...], ...]
    regional_object_count: int
    regional_arrow_count: int
    fact_map_count: int
    nonempty_pair_instances: int
    nonvacuous_triple_count: int
    universal_atoms: Tuple[int, ...]
    complete_proper_boolean: bool


def held_out_truth() -> HeldOutCertificationTruth:
    """Scorer-only truth; never passed to or imported by the estimator."""

    return HeldOutCertificationTruth(
        schema=FIXTURE_SCHEMA,
        abstract_order=192,
        carrier_dimension=32,
        factor_orders=(2, 3, 4, 8),
        independently_selectable_count=6,
        context_atom_sets=((0, 1), (1, 2), (2, 3), (0, 3), (0, 1, 2)),
        regional_atom_sets=(
            (0,),
            (1,),
            (2,),
            (3,),
            (0, 1),
            (1, 2),
            (2, 3),
            (0, 3),
            (0, 1, 2),
        ),
        regional_object_count=9,
        regional_arrow_count=22,
        fact_map_count=22,
        nonempty_pair_instances=8,
        nonvacuous_triple_count=3,
        universal_atoms=(),
        complete_proper_boolean=False,
    )


def fixture_provenance() -> Mapping[str, object]:
    return {
        "schema": FIXTURE_SCHEMA,
        "estimator_freeze_commit": ESTIMATOR_FREEZE_COMMIT,
        "estimator_frozen_sha256": ESTIMATOR_FROZEN_SHA256,
        "old_s3_cubed_imported": False,
        "abstract_family": "fresh heterogeneous C2 x C3 x C4 x D4",
        "truth_visible_to_estimator": False,
        "post_freeze_fixture": True,
    }
