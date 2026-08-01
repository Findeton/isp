#!/usr/bin/env python3
"""Independent trusted verifier for the public RQ0-L0 architecture reset.

The verifier consumes raw mappings and reconstructs every judgment.  It does
not import the proposer and does not trust attached pass flags, result-list
membership, atlases, obstruction strings, novelty declarations, or expected
fixture truth.
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Dict, FrozenSet, Iterable, Mapping, Optional, Sequence, Tuple

try:
    from .rq0_l0_archreset_kernel_exact import (
        Matrix,
        MonomialLaw,
        ONE,
        PHASE_MODULUS,
        Q24,
        Vector,
        ZERO,
        adjoint,
        conjugate_dense,
        identity,
        inner,
        is_projector,
        is_unitary,
        is_zero_matrix,
        map_projector_atoms,
        monomial_span_dimension,
        monomial_span_intersection_dimension,
        mmul,
        msub,
        mv,
        shape,
        zero_matrix,
    )
except ImportError:
    from rq0_l0_archreset_kernel_exact import (
        Matrix,
        MonomialLaw,
        ONE,
        PHASE_MODULUS,
        Q24,
        Vector,
        ZERO,
        adjoint,
        conjugate_dense,
        identity,
        inner,
        is_projector,
        is_unitary,
        is_zero_matrix,
        map_projector_atoms,
        monomial_span_dimension,
        monomial_span_intersection_dimension,
        mmul,
        msub,
        mv,
        shape,
        zero_matrix,
    )


DATASET_SCHEMA = "rq0-l0-archreset-dataset-v1"
FACTOR_CLAIM_SCHEMA = "rq0-l0-archreset-factor-claim-v1"
ATLAS_CLAIM_SCHEMA = "rq0-l0-archreset-overlap-claim-v1"
REGADDR_SCHEMA = "rq0-l0-archreset-regaddr-v1"
TRIPLE_SCHEMA = "rq0-l0-archreset-triple-v1"

IMPLEMENTED = "IMPLEMENTED"
UNAVAILABLE = "UNAVAILABLE"
COLLAPSED = "COLLAPSED"
STATUSES = frozenset((IMPLEMENTED, UNAVAILABLE, COLLAPSED))

MAX_CARRIER = 64
MAX_OPERATIONS = 256
MAX_ROWS = 65_536
MAX_FACTOR_COUNT = 8


class VerificationError(ValueError):
    """Strict schema or independently recomputed verification failure."""


def _fail(path: str, message: str) -> None:
    raise VerificationError(f"{path}: {message}")


def _mapping(value: object, keys: FrozenSet[str], path: str) -> Mapping[str, object]:
    if type(value) is not dict:
        _fail(path, "expected an exact mapping")
    actual = frozenset(value.keys())
    if actual != keys:
        missing = sorted(keys - actual)
        extra = sorted(actual - keys)
        _fail(path, f"mapping keys differ; missing={missing}, extra={extra}")
    if any(type(key) is not str for key in value):
        _fail(path, "mapping keys must be strings")
    return value


def _array(value: object, path: str) -> list[object]:
    if type(value) is not list:
        _fail(path, "expected an exact array")
    return value


def _string(value: object, path: str) -> str:
    if type(value) is not str or not value:
        _fail(path, "expected a nonempty exact string")
    return value


def _integer(
    value: object,
    path: str,
    *,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
) -> int:
    if type(value) is not int:
        _fail(path, "expected an exact integer")
    if minimum is not None and value < minimum:
        _fail(path, f"integer is below {minimum}")
    if maximum is not None and value > maximum:
        _fail(path, f"integer exceeds {maximum}")
    return value


def _boolean(value: object, path: str) -> bool:
    if type(value) is not bool:
        _fail(path, "expected an exact boolean")
    return value


def _nullable_string(value: object, path: str) -> Optional[str]:
    if value is None:
        return None
    return _string(value, path)


def _unique_strings(value: object, path: str, *, allow_empty: bool = True) -> Tuple[str, ...]:
    entries = tuple(
        _string(item, f"{path}[{index}]")
        for index, item in enumerate(_array(value, path))
    )
    if not allow_empty and not entries:
        _fail(path, "array may not be empty")
    if len(entries) != len(set(entries)):
        _fail(path, "array contains duplicate strings")
    return entries


def _parse_law(value: object, path: str) -> MonomialLaw:
    raw = _mapping(value, frozenset(("permutation", "phases")), path)
    permutation = tuple(
        _integer(item, f"{path}.permutation[{index}]", minimum=0)
        for index, item in enumerate(_array(raw["permutation"], f"{path}.permutation"))
    )
    phases = tuple(
        _integer(
            item,
            f"{path}.phases[{index}]",
            minimum=0,
            maximum=PHASE_MODULUS - 1,
        )
        for index, item in enumerate(_array(raw["phases"], f"{path}.phases"))
    )
    try:
        return MonomialLaw(permutation, phases)
    except ValueError as error:
        _fail(path, str(error))


def _parse_signature(
    value: object,
    path: str,
    *,
    nullable: bool,
) -> Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]]:
    if value is None:
        if nullable:
            return None
        _fail(path, "signature may not be null")
    outer = _array(value, path)
    if len(outer) != 2:
        _fail(path, "signature must contain permutation and phase arrays")
    permutation = tuple(
        _integer(item, f"{path}[0][{index}]", minimum=0)
        for index, item in enumerate(_array(outer[0], f"{path}[0]"))
    )
    phases = tuple(
        _integer(
            item,
            f"{path}[1][{index}]",
            minimum=0,
            maximum=PHASE_MODULUS - 1,
        )
        for index, item in enumerate(_array(outer[1], f"{path}[1]"))
    )
    return permutation, phases


def _parse_q24(value: object, path: str) -> Q24:
    coefficients = _array(value, path)
    if len(coefficients) != 8:
        _fail(path, "Q(zeta_24) scalar must contain eight coefficients")
    parsed = []
    for index, coefficient in enumerate(coefficients):
        pair = _array(coefficient, f"{path}[{index}]")
        if len(pair) != 2:
            _fail(f"{path}[{index}]", "rational must be [numerator, denominator]")
        numerator = _integer(pair[0], f"{path}[{index}][0]")
        denominator = _integer(pair[1], f"{path}[{index}][1]", minimum=1)
        fraction = Fraction(numerator, denominator)
        if fraction.numerator != numerator or fraction.denominator != denominator:
            _fail(f"{path}[{index}]", "rational encoding is not canonical")
        parsed.append(fraction)
    return Q24(tuple(parsed))


def _parse_vector(value: object, path: str, dimension: int) -> Vector:
    raw = _array(value, path)
    if len(raw) != dimension:
        _fail(path, "vector has the wrong carrier dimension")
    return tuple(_parse_q24(item, f"{path}[{index}]") for index, item in enumerate(raw))


def _parse_matrix(value: object, path: str, dimension: int) -> Matrix:
    rows = _array(value, path)
    if len(rows) != dimension:
        _fail(path, "matrix has the wrong row count")
    result = []
    for row_index, row in enumerate(rows):
        entries = _array(row, f"{path}[{row_index}]")
        if len(entries) != dimension:
            _fail(f"{path}[{row_index}]", "matrix has the wrong column count")
        result.append(
            tuple(
                _parse_q24(item, f"{path}[{row_index}][{column}]")
                for column, item in enumerate(entries)
            )
        )
    return tuple(result)


def _parse_atoms(
    value: object,
    path: str,
    dimension: int,
) -> Tuple[FrozenSet[int], ...]:
    raw_atoms = _array(value, path)
    if not raw_atoms:
        _fail(path, "projector resolution is empty")
    atoms = []
    for atom_index, raw_atom in enumerate(raw_atoms):
        entries = tuple(
            _integer(
                item,
                f"{path}[{atom_index}][{index}]",
                minimum=0,
                maximum=dimension - 1,
            )
            for index, item in enumerate(
                _array(raw_atom, f"{path}[{atom_index}]")
            )
        )
        if not entries or len(entries) != len(set(entries)):
            _fail(f"{path}[{atom_index}]", "projector atom is empty or duplicated")
        atoms.append(frozenset(entries))
    if len(atoms) != len(set(atoms)):
        _fail(path, "projector resolution contains duplicate atoms")
    if any(left & right for left, right in itertools.combinations(atoms, 2)):
        _fail(path, "projector atoms overlap")
    if frozenset().union(*atoms) != frozenset(range(dimension)):
        _fail(path, "projector atoms do not resolve the carrier")
    return tuple(atoms)


@dataclass(frozen=True)
class Boundary:
    name: str
    composes_with: Tuple[str, ...]


@dataclass(frozen=True)
class Operation:
    handle: str
    source_type: str
    target_type: str
    law: MonomialLaw
    observed_signature: Tuple[Tuple[int, ...], Tuple[int, ...]]
    independently_selectable: bool


@dataclass(frozen=True)
class Row:
    left: str
    right: str
    tau: str
    status: str
    result_class: Optional[str]
    law: Optional[MonomialLaw]
    observed_signature: Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]]


@dataclass(frozen=True)
class Field:
    handle: str
    boundary_type: str
    payload: Tuple[int, ...]


@dataclass(frozen=True)
class Readout:
    handle: str
    boundary_type: str
    projector_resolution: Tuple[FrozenSet[int], ...]


@dataclass(frozen=True)
class Gauge:
    handle: str
    boundary_type: str
    law: MonomialLaw


@dataclass(frozen=True)
class Witness:
    preparations: Tuple[Vector, ...]
    alternative_projectors: Tuple[Matrix, ...]
    cut_record_projectors: Tuple[Matrix, ...]
    availability_probes: Tuple[Matrix, ...]
    write: Matrix
    preserving: Tuple[Matrix, ...]
    erasing: Tuple[Matrix, ...]
    no_write: Matrix


@dataclass(frozen=True)
class Record:
    handle: str
    boundary_type: str
    access_operations: Tuple[str, ...]
    witness: Witness
    ambient_projector_resolution: Tuple[FrozenSet[int], ...]


@dataclass(frozen=True)
class Context:
    handle: str
    boundary_type: str
    operation_handles: Tuple[str, ...]
    preparation_handles: Tuple[str, ...]
    probe_handles: Tuple[str, ...]
    readout_handles: Tuple[str, ...]
    record_handles: Tuple[str, ...]
    gauge_handles: Tuple[str, ...]


@dataclass(frozen=True)
class Dataset:
    handle: str
    carrier_dimension: int
    boundaries: Tuple[Boundary, ...]
    operations: Tuple[Operation, ...]
    rows: Tuple[Row, ...]
    preparations: Tuple[Field, ...]
    contexts: Tuple[Context, ...]
    probes: Tuple[Field, ...]
    readouts: Tuple[Readout, ...]
    records: Tuple[Record, ...]
    gauges: Tuple[Gauge, ...]
    access_postulate: str

    @property
    def operation_map(self) -> Mapping[str, Operation]:
        return {value.handle: value for value in self.operations}

    @property
    def row_map(self) -> Mapping[Tuple[str, str], Row]:
        return {(value.left, value.right): value for value in self.rows}


def _parse_witness(value: object, path: str, dimension: int) -> Witness:
    raw = _mapping(
        value,
        frozenset(
            (
                "preparations",
                "alternative_projectors",
                "cut_record_projectors",
                "availability_probes",
                "write",
                "preserving",
                "erasing",
                "no_write",
            )
        ),
        path,
    )

    def vectors(name: str) -> Tuple[Vector, ...]:
        return tuple(
            _parse_vector(item, f"{path}.{name}[{index}]", dimension)
            for index, item in enumerate(_array(raw[name], f"{path}.{name}"))
        )

    def matrices(name: str) -> Tuple[Matrix, ...]:
        return tuple(
            _parse_matrix(item, f"{path}.{name}[{index}]", dimension)
            for index, item in enumerate(_array(raw[name], f"{path}.{name}"))
        )

    return Witness(
        preparations=vectors("preparations"),
        alternative_projectors=matrices("alternative_projectors"),
        cut_record_projectors=matrices("cut_record_projectors"),
        availability_probes=matrices("availability_probes"),
        write=_parse_matrix(raw["write"], f"{path}.write", dimension),
        preserving=matrices("preserving"),
        erasing=matrices("erasing"),
        no_write=_parse_matrix(raw["no_write"], f"{path}.no_write", dimension),
    )


def parse_dataset(value: object, path: str = "dataset") -> Dataset:
    raw = _mapping(
        value,
        frozenset(
            (
                "schema",
                "handle",
                "phase_modulus",
                "carrier_dimension",
                "boundary_types",
                "operations",
                "composition_rows",
                "preparations",
                "contexts",
                "probes",
                "readouts",
                "records",
                "gauge_actions",
                "access_postulate",
            )
        ),
        path,
    )
    if _string(raw["schema"], f"{path}.schema") != DATASET_SCHEMA:
        _fail(f"{path}.schema", "wrong schema version")
    if _integer(raw["phase_modulus"], f"{path}.phase_modulus") != PHASE_MODULUS:
        _fail(f"{path}.phase_modulus", "only exact mu_24 laws are admitted")
    dimension = _integer(
        raw["carrier_dimension"],
        f"{path}.carrier_dimension",
        minimum=2,
        maximum=MAX_CARRIER,
    )

    boundaries = []
    for index, item in enumerate(_array(raw["boundary_types"], f"{path}.boundary_types")):
        entry = _mapping(
            item,
            frozenset(("name", "composes_with")),
            f"{path}.boundary_types[{index}]",
        )
        boundaries.append(
            Boundary(
                _string(entry["name"], f"{path}.boundary_types[{index}].name"),
                _unique_strings(
                    entry["composes_with"],
                    f"{path}.boundary_types[{index}].composes_with",
                ),
            )
        )
    if not boundaries or len({value.name for value in boundaries}) != len(boundaries):
        _fail(f"{path}.boundary_types", "boundary declarations are empty or duplicated")
    boundary_names = frozenset(value.name for value in boundaries)
    if any(not set(value.composes_with) <= boundary_names for value in boundaries):
        _fail(f"{path}.boundary_types", "boundary compatibility references an unknown type")

    operations = []
    for index, item in enumerate(_array(raw["operations"], f"{path}.operations")):
        entry = _mapping(
            item,
            frozenset(
                (
                    "handle",
                    "source_type",
                    "target_type",
                    "law",
                    "observed_signature",
                    "independently_selectable",
                )
            ),
            f"{path}.operations[{index}]",
        )
        law = _parse_law(entry["law"], f"{path}.operations[{index}].law")
        signature = _parse_signature(
            entry["observed_signature"],
            f"{path}.operations[{index}].observed_signature",
            nullable=False,
        )
        operations.append(
            Operation(
                _string(entry["handle"], f"{path}.operations[{index}].handle"),
                _string(entry["source_type"], f"{path}.operations[{index}].source_type"),
                _string(entry["target_type"], f"{path}.operations[{index}].target_type"),
                law,
                signature,
                _boolean(
                    entry["independently_selectable"],
                    f"{path}.operations[{index}].independently_selectable",
                ),
            )
        )
    if not operations or len(operations) > MAX_OPERATIONS:
        _fail(f"{path}.operations", "operation count violates the public cap")
    operation_handles = tuple(value.handle for value in operations)
    if len(operation_handles) != len(set(operation_handles)):
        _fail(f"{path}.operations", "operation handles are duplicated")
    for operation in operations:
        if operation.source_type not in boundary_names or operation.target_type not in boundary_names:
            _fail(f"{path}.operations", "operation references an unknown boundary")
        if operation.law.dimension != dimension:
            _fail(f"{path}.operations.{operation.handle}.law", "law has the wrong carrier")
        if operation.observed_signature != operation.law.signature():
            _fail(f"{path}.operations.{operation.handle}.observed_signature", "signature differs from exact law")

    rows = []
    for index, item in enumerate(
        _array(raw["composition_rows"], f"{path}.composition_rows")
    ):
        entry = _mapping(
            item,
            frozenset(
                (
                    "left",
                    "right",
                    "tau",
                    "status",
                    "result_class",
                    "law",
                    "observed_signature",
                )
            ),
            f"{path}.composition_rows[{index}]",
        )
        status = _string(entry["status"], f"{path}.composition_rows[{index}].status")
        if status not in STATUSES:
            _fail(f"{path}.composition_rows[{index}].status", "unknown row status")
        law = None if entry["law"] is None else _parse_law(
            entry["law"], f"{path}.composition_rows[{index}].law"
        )
        rows.append(
            Row(
                _string(entry["left"], f"{path}.composition_rows[{index}].left"),
                _string(entry["right"], f"{path}.composition_rows[{index}].right"),
                _string(entry["tau"], f"{path}.composition_rows[{index}].tau"),
                status,
                _nullable_string(
                    entry["result_class"],
                    f"{path}.composition_rows[{index}].result_class",
                ),
                law,
                _parse_signature(
                    entry["observed_signature"],
                    f"{path}.composition_rows[{index}].observed_signature",
                    nullable=True,
                ),
            )
        )
    if len(rows) > MAX_ROWS:
        _fail(f"{path}.composition_rows", "row count violates the public cap")

    def parse_fields(name: str) -> Tuple[Field, ...]:
        result = []
        for index, item in enumerate(_array(raw[name], f"{path}.{name}")):
            entry = _mapping(
                item,
                frozenset(("handle", "boundary_type", "payload")),
                f"{path}.{name}[{index}]",
            )
            payload = tuple(
                _integer(value, f"{path}.{name}[{index}].payload[{ordinal}]")
                for ordinal, value in enumerate(
                    _array(entry["payload"], f"{path}.{name}[{index}].payload")
                )
            )
            if len(payload) != dimension:
                _fail(f"{path}.{name}[{index}].payload", "payload has the wrong carrier dimension")
            result.append(
                Field(
                    _string(entry["handle"], f"{path}.{name}[{index}].handle"),
                    _string(
                        entry["boundary_type"],
                        f"{path}.{name}[{index}].boundary_type",
                    ),
                    payload,
                )
            )
        return tuple(result)

    preparations = parse_fields("preparations")
    probes = parse_fields("probes")

    readouts = []
    for index, item in enumerate(_array(raw["readouts"], f"{path}.readouts")):
        entry = _mapping(
            item,
            frozenset(("handle", "boundary_type", "projector_resolution")),
            f"{path}.readouts[{index}]",
        )
        readouts.append(
            Readout(
                _string(entry["handle"], f"{path}.readouts[{index}].handle"),
                _string(
                    entry["boundary_type"],
                    f"{path}.readouts[{index}].boundary_type",
                ),
                _parse_atoms(
                    entry["projector_resolution"],
                    f"{path}.readouts[{index}].projector_resolution",
                    dimension,
                ),
            )
        )

    records = []
    for index, item in enumerate(_array(raw["records"], f"{path}.records")):
        entry = _mapping(
            item,
            frozenset(
                (
                    "handle",
                    "boundary_type",
                    "access_operations",
                    "witness",
                    "ambient_projector_resolution",
                )
            ),
            f"{path}.records[{index}]",
        )
        records.append(
            Record(
                _string(entry["handle"], f"{path}.records[{index}].handle"),
                _string(
                    entry["boundary_type"],
                    f"{path}.records[{index}].boundary_type",
                ),
                _unique_strings(
                    entry["access_operations"],
                    f"{path}.records[{index}].access_operations",
                    allow_empty=False,
                ),
                _parse_witness(
                    entry["witness"], f"{path}.records[{index}].witness", dimension
                ),
                _parse_atoms(
                    entry["ambient_projector_resolution"],
                    f"{path}.records[{index}].ambient_projector_resolution",
                    dimension,
                ),
            )
        )

    gauges = []
    for index, item in enumerate(_array(raw["gauge_actions"], f"{path}.gauge_actions")):
        entry = _mapping(
            item,
            frozenset(("handle", "boundary_type", "law")),
            f"{path}.gauge_actions[{index}]",
        )
        gauges.append(
            Gauge(
                _string(entry["handle"], f"{path}.gauge_actions[{index}].handle"),
                _string(
                    entry["boundary_type"],
                    f"{path}.gauge_actions[{index}].boundary_type",
                ),
                _parse_law(entry["law"], f"{path}.gauge_actions[{index}].law"),
            )
        )

    contexts = []
    context_keys = frozenset(
        (
            "handle",
            "boundary_type",
            "operation_handles",
            "preparation_handles",
            "probe_handles",
            "readout_handles",
            "record_handles",
            "gauge_handles",
        )
    )
    for index, item in enumerate(_array(raw["contexts"], f"{path}.contexts")):
        entry = _mapping(item, context_keys, f"{path}.contexts[{index}]")
        contexts.append(
            Context(
                _string(entry["handle"], f"{path}.contexts[{index}].handle"),
                _string(
                    entry["boundary_type"],
                    f"{path}.contexts[{index}].boundary_type",
                ),
                _unique_strings(
                    entry["operation_handles"],
                    f"{path}.contexts[{index}].operation_handles",
                    allow_empty=False,
                ),
                _unique_strings(
                    entry["preparation_handles"],
                    f"{path}.contexts[{index}].preparation_handles",
                ),
                _unique_strings(
                    entry["probe_handles"],
                    f"{path}.contexts[{index}].probe_handles",
                ),
                _unique_strings(
                    entry["readout_handles"],
                    f"{path}.contexts[{index}].readout_handles",
                ),
                _unique_strings(
                    entry["record_handles"],
                    f"{path}.contexts[{index}].record_handles",
                ),
                _unique_strings(
                    entry["gauge_handles"],
                    f"{path}.contexts[{index}].gauge_handles",
                ),
            )
        )

    dataset = Dataset(
        handle=_string(raw["handle"], f"{path}.handle"),
        carrier_dimension=dimension,
        boundaries=tuple(boundaries),
        operations=tuple(operations),
        rows=tuple(rows),
        preparations=preparations,
        contexts=tuple(contexts),
        probes=probes,
        readouts=tuple(readouts),
        records=tuple(records),
        gauges=tuple(gauges),
        access_postulate=_string(raw["access_postulate"], f"{path}.access_postulate"),
    )
    validate_dataset(dataset, path)
    return dataset


def _handle_map(values: Sequence[object], path: str) -> Mapping[str, object]:
    result = {value.handle: value for value in values}
    if len(result) != len(values):
        _fail(path, "field handles are duplicated")
    return result


def validate_dataset(dataset: Dataset, path: str = "dataset") -> None:
    operation_map = dataset.operation_map
    operation_handles = frozenset(operation_map)
    boundary_map = {value.name: value for value in dataset.boundaries}
    expected_pairs = frozenset(itertools.product(operation_handles, repeat=2))
    observed_pairs = tuple((value.left, value.right) for value in dataset.rows)
    if len(observed_pairs) != len(set(observed_pairs)):
        _fail(f"{path}.composition_rows", "ordered row pairs are duplicated")
    if frozenset(observed_pairs) != expected_pairs:
        missing = len(expected_pairs - frozenset(observed_pairs))
        extra = len(frozenset(observed_pairs) - expected_pairs)
        _fail(f"{path}.composition_rows", f"table is incomplete; missing={missing}, extra={extra}")
    row_map = dataset.row_map
    for pair, row in row_map.items():
        left = operation_map[row.left]
        right = operation_map[row.right]
        expected_tau = f"{right.source_type}|{right.target_type}|{left.target_type}"
        if row.tau != expected_tau:
            _fail(f"{path}.composition_rows.{pair}.tau", "tau is mistyped")
        compatible = left.source_type in boundary_map[right.target_type].composes_with
        if row.status == UNAVAILABLE:
            if row.result_class is not None or row.law is not None or row.observed_signature is not None:
                _fail(f"{path}.composition_rows.{pair}", "unavailable row carries synthetic data")
            continue
        if not compatible:
            _fail(f"{path}.composition_rows.{pair}", "implemented row has incompatible boundaries")
        if row.result_class not in operation_map or row.law is None or row.observed_signature is None:
            _fail(f"{path}.composition_rows.{pair}", "implemented/collapsed row is incomplete")
        if row.law.dimension != dataset.carrier_dimension:
            _fail(f"{path}.composition_rows.{pair}.law", "row law has the wrong carrier")
        physical = left.law.after(right.law)
        if row.law != physical:
            _fail(f"{path}.composition_rows.{pair}.law", "row law differs from exact physical composition")
        if row.observed_signature != row.law.signature():
            _fail(f"{path}.composition_rows.{pair}.observed_signature", "row signature differs from its law")
        result = operation_map[row.result_class]
        if not row.law.global_phase_equivalent(result.law):
            _fail(f"{path}.composition_rows.{pair}.result_class", "result class is not gauge-equivalent to row law")

    families = {
        "preparations": dataset.preparations,
        "contexts": dataset.contexts,
        "probes": dataset.probes,
        "readouts": dataset.readouts,
        "records": dataset.records,
        "gauge_actions": dataset.gauges,
    }
    maps = {name: _handle_map(values, f"{path}.{name}") for name, values in families.items()}
    boundary_names = frozenset(boundary_map)
    for name, values in families.items():
        for value in values:
            if value.boundary_type not in boundary_names:
                _fail(f"{path}.{name}.{value.handle}.boundary_type", "unknown boundary")
    for gauge in dataset.gauges:
        if gauge.law.dimension != dataset.carrier_dimension:
            _fail(f"{path}.gauge_actions.{gauge.handle}.law", "gauge has the wrong carrier")
    for record in dataset.records:
        if not set(record.access_operations) <= operation_handles:
            _fail(f"{path}.records.{record.handle}.access_operations", "record references unknown operation")
        if any(
            operation_map[handle].source_type != record.boundary_type
            or operation_map[handle].target_type != record.boundary_type
            for handle in record.access_operations
        ):
            _fail(f"{path}.records.{record.handle}.boundary_type", "record boundary is incompatible with access operations")
        evaluate_w3(record.witness, f"{path}.records.{record.handle}.witness")
    field_map_names = {
        "preparation_handles": "preparations",
        "probe_handles": "probes",
        "readout_handles": "readouts",
        "record_handles": "records",
        "gauge_handles": "gauge_actions",
    }
    for context in dataset.contexts:
        if not set(context.operation_handles) <= operation_handles:
            _fail(f"{path}.contexts.{context.handle}.operation_handles", "unknown operation")
        if any(
            operation_map[handle].source_type != context.boundary_type
            or operation_map[handle].target_type != context.boundary_type
            for handle in context.operation_handles
        ):
            _fail(f"{path}.contexts.{context.handle}.boundary_type", "context boundary is incompatible with operations")
        for attribute, family_name in field_map_names.items():
            handles = getattr(context, attribute)
            family = maps[family_name]
            if not set(handles) <= set(family):
                _fail(f"{path}.contexts.{context.handle}.{attribute}", "context references unknown field")
            if any(family[handle].boundary_type != context.boundary_type for handle in handles):
                _fail(f"{path}.contexts.{context.handle}.boundary_type", f"context boundary conflicts with {family_name}")


def _validate_dense_resolution(values: Sequence[Matrix], dimension: int, path: str) -> None:
    if not values:
        _fail(path, "dense projector resolution is empty")
    if any(shape(value) != (dimension, dimension) or not is_projector(value) for value in values):
        _fail(path, "dense projector family contains a nonprojector")
    if any(not is_zero_matrix(mmul(left, right)) for left, right in itertools.combinations(values, 2)):
        _fail(path, "dense projectors are not orthogonal")
    total = zero_matrix(dimension, dimension)
    for value in values:
        total = tuple(
            tuple(total[row][column] + value[row][column] for column in range(dimension))
            for row in range(dimension)
        )
    if total != identity(dimension):
        _fail(path, "dense projectors do not resolve the unit")


@dataclass(frozen=True)
class W3Result:
    occurrence: bool
    preserving_available: Tuple[bool, ...]
    erasing_available: Tuple[bool, ...]
    erasing_cross_coherence: Tuple[int, ...]
    no_write_occurrence: bool

    @property
    def passes(self) -> bool:
        return (
            self.occurrence
            and bool(self.preserving_available)
            and all(self.preserving_available)
            and bool(self.erasing_available)
            and all(not value for value in self.erasing_available)
            and all(value > 0 for value in self.erasing_cross_coherence)
            and not self.no_write_occurrence
        )


def _h_corr(witness: Witness, write: Matrix) -> bool:
    mapping = []
    for alternative in witness.alternative_projectors:
        observed = None
        live = False
        for preparation in witness.preparations:
            component = mv(write, mv(alternative, preparation))
            if not inner(component, component):
                continue
            live = True
            sectors = tuple(
                index
                for index, record in enumerate(witness.cut_record_projectors)
                if inner(mv(record, component), mv(record, component))
            )
            if len(sectors) != 1:
                return False
            if observed is None:
                observed = sectors[0]
            elif observed != sectors[0]:
                return False
        if not live or observed is None:
            return False
        mapping.append(observed)
    return len(mapping) == len(set(mapping))


def _h_avail(witness: Witness, continuation: Matrix) -> bool:
    for final_probe in witness.availability_probes:
        incoming = tuple(
            index
            for index, record in enumerate(witness.cut_record_projectors)
            if not is_zero_matrix(mmul(final_probe, mmul(continuation, record)))
        )
        if len(incoming) > 1:
            return False
    return True


def _cross_coherence(witness: Witness, continuation: Matrix) -> int:
    count = 0
    for preparation in witness.preparations:
        cut_state = mv(witness.write, preparation)
        for final_probe in witness.availability_probes:
            branches = tuple(
                mv(final_probe, mv(continuation, mv(record, cut_state)))
                for record in witness.cut_record_projectors
            )
            for left, right in itertools.combinations(branches, 2):
                if inner(left, right):
                    count += 1
    return count


def evaluate_w3(witness: Witness, path: str = "witness") -> W3Result:
    dimension = len(witness.write)
    if dimension < 2:
        _fail(path, "record witness carrier is too small")
    for label, family in (
        ("alternative_projectors", witness.alternative_projectors),
        ("cut_record_projectors", witness.cut_record_projectors),
        ("availability_probes", witness.availability_probes),
    ):
        _validate_dense_resolution(family, dimension, f"{path}.{label}")
    if not witness.preparations:
        _fail(f"{path}.preparations", "record witness has no preparation")
    for index, value in enumerate(witness.preparations):
        if len(value) != dimension or not inner(value, value):
            _fail(f"{path}.preparations[{index}]", "invalid preparation")
    for label, value in (
        (("write", witness.write), ("no_write", witness.no_write))
        + tuple((f"preserving[{index}]", item) for index, item in enumerate(witness.preserving))
        + tuple((f"erasing[{index}]", item) for index, item in enumerate(witness.erasing))
    ):
        if shape(value) != (dimension, dimension) or not is_unitary(value):
            _fail(f"{path}.{label}", "record dynamics is not an exact unitary")
    result = W3Result(
        occurrence=_h_corr(witness, witness.write),
        preserving_available=tuple(_h_avail(witness, value) for value in witness.preserving),
        erasing_available=tuple(_h_avail(witness, value) for value in witness.erasing),
        erasing_cross_coherence=tuple(_cross_coherence(witness, value) for value in witness.erasing),
        no_write_occurrence=_h_corr(witness, witness.no_write),
    )
    return result


# ---------------------------------------------------------------------------
# Independently reconstructed group and direct-factor predicates
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class GroupView:
    dataset: Dataset
    handles: Tuple[str, ...]
    index: Mapping[str, int]
    table: Tuple[Tuple[int, ...], ...]
    identity: int
    inverses: Tuple[int, ...]

    @property
    def order(self) -> int:
        return len(self.handles)

    def product(self, left: int, right: int) -> int:
        return self.table[left][right]


def build_group(
    dataset: Dataset,
    check_deadline: Callable[[], None] = lambda: None,
) -> GroupView:
    if any(row.status != IMPLEMENTED for row in dataset.rows):
        raise VerificationError("group reconstruction requires every row IMPLEMENTED")
    handles = tuple(sorted(value.handle for value in dataset.operations))
    index = {handle: ordinal for ordinal, handle in enumerate(handles)}
    table = []
    for left in handles:
        table.append(
            tuple(index[dataset.row_map[(left, right)].result_class] for right in handles)
        )
    table_tuple = tuple(table)
    identities = tuple(
        candidate
        for candidate in range(len(handles))
        if all(
            table_tuple[candidate][value] == value
            and table_tuple[value][candidate] == value
            for value in range(len(handles))
        )
    )
    if len(identities) != 1:
        raise VerificationError("composition object lacks a unique identity")
    identity_index = identities[0]
    for left in range(len(handles)):
        check_deadline()
        for right in range(len(handles)):
            for third in range(len(handles)):
                if table_tuple[table_tuple[left][right]][third] != table_tuple[left][table_tuple[right][third]]:
                    raise VerificationError("composition object is not associative")
    inverses = []
    for value in range(len(handles)):
        candidates = tuple(
            other
            for other in range(len(handles))
            if table_tuple[value][other] == identity_index
            and table_tuple[other][value] == identity_index
        )
        if len(candidates) != 1:
            raise VerificationError("composition object lacks unique inverses")
        inverses.append(candidates[0])
    return GroupView(dataset, handles, index, table_tuple, identity_index, tuple(inverses))


Subobject = FrozenSet[int]


def subgroup_generated(group: GroupView, seeds: Iterable[int]) -> Subobject:
    current = {group.identity}
    current.update(seeds)
    changed = True
    while changed:
        changed = False
        for value in tuple(current):
            if group.inverses[value] not in current:
                current.add(group.inverses[value])
                changed = True
        for left in tuple(current):
            for right in tuple(current):
                result = group.product(left, right)
                if result not in current:
                    current.add(result)
                    changed = True
    return frozenset(current)


def normal_closure(group: GroupView, seeds: Iterable[int]) -> Subobject:
    conjugates = set()
    for ambient in range(group.order):
        for seed in seeds:
            conjugates.add(
                group.product(
                    group.product(ambient, seed), group.inverses[ambient]
                )
            )
    return subgroup_generated(group, conjugates)


def enumerate_normal_subobjects(group: GroupView) -> Tuple[Subobject, ...]:
    candidates = {frozenset((group.identity,))}
    for element in range(group.order):
        candidates.add(normal_closure(group, (element,)))
    changed = True
    tests = 0
    while changed:
        changed = False
        snapshot = tuple(sorted(candidates, key=lambda item: (len(item), tuple(sorted(item)))))
        for position, left in enumerate(snapshot):
            for right in snapshot[position:]:
                tests += 1
                if tests > 100_000:
                    raise VerificationError("normal-subobject enumeration exceeded public cap")
                joined = frozenset(group.product(a, b) for a in left for b in right)
                if joined not in candidates:
                    candidates.add(joined)
                    changed = True
    return tuple(sorted(candidates, key=lambda item: (len(item), tuple(sorted(item)))))


def _closed(group: GroupView, factor: Subobject) -> bool:
    return (
        group.identity in factor
        and all(group.inverses[value] in factor for value in factor)
        and all(group.product(left, right) in factor for left in factor for right in factor)
    )


def _normal(group: GroupView, factor: Subobject) -> bool:
    return all(
        group.product(group.product(ambient, value), group.inverses[ambient]) in factor
        for ambient in range(group.order)
        for value in factor
    )


def _multiplication_image(
    group: GroupView,
    factors: Sequence[Subobject],
) -> Tuple[FrozenSet[int], bool]:
    seen: Dict[int, Tuple[int, ...]] = {}
    for entries in itertools.product(*(tuple(sorted(value)) for value in factors)):
        result = group.identity
        for entry in entries:
            result = group.product(result, entry)
        if result in seen and seen[result] != entries:
            return frozenset(seen), False
        seen[result] = entries
    return frozenset(seen), True


@dataclass(frozen=True)
class PredicateResult:
    values: Mapping[str, bool]
    factor_orders: Tuple[int, ...]
    algebra_dimensions: Tuple[int, ...]

    @property
    def passes(self) -> bool:
        return all(self.values.values())


PREDICATE_KEYS = tuple(f"P{index}" for index in range(1, 9))


def verify_factor_tuple(group: GroupView, factors: Sequence[Subobject]) -> PredicateResult:
    factors = tuple(frozenset(value) for value in factors)
    if not 2 <= len(factors) <= MAX_FACTOR_COUNT:
        raise VerificationError("factor tuple must contain two through eight factors")
    if any(
        factor == frozenset((group.identity,))
        or len(factor) == group.order
        or not _normal(group, factor)
        for factor in factors
    ):
        raise VerificationError("claimed factor is not proper, nontrivial and normal")
    selectable = frozenset(
        group.index[value.handle]
        for value in group.dataset.operations
        if value.independently_selectable
    )
    p1 = all(subgroup_generated(group, factor & selectable) == factor for factor in factors)
    p2 = all(
        group.dataset.row_map[(group.handles[left], group.handles[right])].status == IMPLEMENTED
        and group.dataset.row_map[(group.handles[right], group.handles[left])].status == IMPLEMENTED
        for first, second in itertools.combinations(factors, 2)
        for left in first
        for right in second
    )
    p3 = all(
        group.product(left, right) == group.product(right, left)
        and group.dataset.row_map[
            (group.handles[left], group.handles[right])
        ].law.global_phase_equivalent(
            group.dataset.row_map[
                (group.handles[right], group.handles[left])
            ].law
        )
        and group.dataset.row_map[
            (group.handles[left], group.handles[right])
        ].observed_signature
        == group.dataset.row_map[
            (group.handles[right], group.handles[left])
        ].observed_signature
        for first, second in itertools.combinations(factors, 2)
        for left in first
        for right in second
    )
    image, faithful = _multiplication_image(group, factors)
    p4 = faithful and len(image) == group.order
    p5 = all(_closed(group, factor) for factor in factors)
    group_scalar = all(
        left & right == frozenset((group.identity,))
        for left, right in itertools.combinations(factors, 2)
    )
    laws = {value.handle: value.law for value in group.dataset.operations}
    factor_laws = tuple(
        tuple(laws[group.handles[index]] for index in factor)
        for factor in factors
    )
    algebra_dimensions = tuple(
        monomial_span_dimension(values) for values in factor_laws
    )
    algebra_scalar = all(
        monomial_span_intersection_dimension(left, right) == 1
        for left, right in itertools.combinations(factor_laws, 2)
    )
    p6 = group_scalar and algebra_scalar
    ambient_dimension = monomial_span_dimension(laws.values())
    commute_matrices = all(
        laws[group.handles[left]].after(laws[group.handles[right]])
        == laws[group.handles[right]].after(laws[group.handles[left]])
        for first, second in itertools.combinations(factors, 2)
        for left in first
        for right in second
    )
    dimension_product = math.prod(algebra_dimensions)
    p7 = commute_matrices and dimension_product == ambient_dimension
    p8 = True
    if faithful:
        for count in range(1, len(factors) + 1):
            for chosen in itertools.combinations(factors, count):
                region, region_faithful = _multiplication_image(group, chosen)
                if not region_faithful or not _closed(group, region):
                    p8 = False
                    break
                if any(
                    group.dataset.row_map[(group.handles[left], group.handles[right])].status != IMPLEMENTED
                    or group.product(left, right) not in region
                    for left in region
                    for right in region
                ):
                    p8 = False
                    break
            if not p8:
                break
    else:
        p8 = False
    return PredicateResult(
        dict(zip(PREDICATE_KEYS, (p1, p2, p3, p4, p5, p6, p7, p8))),
        tuple(len(value) for value in factors),
        algebra_dimensions,
    )


def _parse_assertions(value: object, path: str) -> Mapping[str, bool]:
    raw = _mapping(value, frozenset(PREDICATE_KEYS), path)
    return {key: _boolean(raw[key], f"{path}.{key}") for key in PREDICATE_KEYS}


def parse_factor_claim(value: object, path: str = "claim") -> Mapping[str, object]:
    raw = _mapping(
        value,
        frozenset(("schema", "kind", "certificates", "obstruction")),
        path,
    )
    if _string(raw["schema"], f"{path}.schema") != FACTOR_CLAIM_SCHEMA:
        _fail(f"{path}.schema", "wrong factor-claim schema")
    kind = _string(raw["kind"], f"{path}.kind")
    if kind not in ("DIRECT-FACTOR-CERTIFICATES", "DIRECT-FACTOR-NONE"):
        _fail(f"{path}.kind", "unknown factor claim kind")
    certificates = []
    for index, item in enumerate(_array(raw["certificates"], f"{path}.certificates")):
        entry = _mapping(
            item,
            frozenset(("factors", "asserted_predicates", "asserted_passes")),
            f"{path}.certificates[{index}]",
        )
        factors = tuple(
            _unique_strings(
                factor,
                f"{path}.certificates[{index}].factors[{factor_index}]",
                allow_empty=False,
            )
            for factor_index, factor in enumerate(
                _array(entry["factors"], f"{path}.certificates[{index}].factors")
            )
        )
        certificates.append(
            {
                "factors": factors,
                "asserted_predicates": _parse_assertions(
                    entry["asserted_predicates"],
                    f"{path}.certificates[{index}].asserted_predicates",
                ),
                "asserted_passes": _boolean(
                    entry["asserted_passes"],
                    f"{path}.certificates[{index}].asserted_passes",
                ),
            }
        )
    obstruction = _nullable_string(raw["obstruction"], f"{path}.obstruction")
    if kind == "DIRECT-FACTOR-CERTIFICATES" and (not certificates or obstruction is not None):
        _fail(path, "positive factor claim has inconsistent payload")
    if kind == "DIRECT-FACTOR-NONE" and (certificates or obstruction is None):
        _fail(path, "negative factor claim has inconsistent payload")
    return {"kind": kind, "certificates": tuple(certificates), "obstruction": obstruction}


@dataclass(frozen=True)
class FactorVerification:
    category: str
    certificates: Tuple[PredicateResult, ...]
    exhaustive_candidates: int


def verify_factor_claim(
    dataset_raw: object,
    claim_raw: object,
    check_deadline: Callable[[], None] = lambda: None,
) -> FactorVerification:
    dataset = parse_dataset(dataset_raw)
    check_deadline()
    group = build_group(dataset, check_deadline)
    claim = parse_factor_claim(claim_raw)
    results = []
    if claim["kind"] == "DIRECT-FACTOR-CERTIFICATES":
        for certificate in claim["certificates"]:
            check_deadline()
            factors = []
            for factor in certificate["factors"]:
                if not set(factor) <= set(group.index):
                    raise VerificationError("certificate references unknown operation handles")
                factors.append(frozenset(group.index[handle] for handle in factor))
            recomputed = verify_factor_tuple(group, factors)
            if certificate["asserted_predicates"] != recomputed.values:
                raise VerificationError("asserted P1--P8 table differs from trusted recomputation")
            if certificate["asserted_passes"] is not recomputed.passes:
                raise VerificationError("asserted certificate pass flag differs from trusted recomputation")
            if not recomputed.passes:
                raise VerificationError("positive factor certificate fails a trusted predicate")
            results.append(recomputed)
        return FactorVerification("positive", tuple(results), 0)

    normals = tuple(
        value
        for value in enumerate_normal_subobjects(group)
        if value != frozenset((group.identity,)) and len(value) != group.order
    )
    candidates = 0
    for count in range(2, min(MAX_FACTOR_COUNT, len(normals)) + 1):
        for factors in itertools.combinations(normals, count):
            check_deadline()
            if math.prod(len(value) for value in factors) != group.order:
                continue
            candidates += 1
            result = verify_factor_tuple(group, factors)
            if result.passes:
                raise VerificationError("claimed addressability negative has a passing factor tuple")
    return FactorVerification("scientific-negative", (), candidates)


# ---------------------------------------------------------------------------
# Full-field RegAddr maps
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PairMap:
    source: str
    target: str


@dataclass(frozen=True)
class RowPairMap:
    source_left: str
    source_right: str
    target_left: str
    target_right: str
    source_tau: str
    target_tau: str
    source_status: str
    target_status: str
    source_result_class: Optional[str]
    target_result_class: Optional[str]
    source_law: Optional[MonomialLaw]
    target_law: Optional[MonomialLaw]
    source_observed_signature: Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]]
    target_observed_signature: Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]]


@dataclass(frozen=True)
class RegAddr:
    handle: str
    kind: str
    source: str
    target: str
    carrier_action: MonomialLaw
    operation_map: Tuple[PairMap, ...]
    row_map: Tuple[RowPairMap, ...]
    preparation_map: Tuple[PairMap, ...]
    context_map: Tuple[PairMap, ...]
    probe_map: Tuple[PairMap, ...]
    readout_map: Tuple[PairMap, ...]
    record_map: Tuple[PairMap, ...]
    gauge_map: Tuple[PairMap, ...]


def _parse_pair_maps(value: object, path: str) -> Tuple[PairMap, ...]:
    result = []
    for index, item in enumerate(_array(value, path)):
        raw = _mapping(
            item,
            frozenset(("source", "target")),
            f"{path}[{index}]",
        )
        result.append(
            PairMap(
                _string(raw["source"], f"{path}[{index}].source"),
                _string(raw["target"], f"{path}[{index}].target"),
            )
        )
    return tuple(result)


def parse_regaddr(value: object, path: str = "arrow") -> RegAddr:
    raw = _mapping(
        value,
        frozenset(
            (
                "schema",
                "handle",
                "kind",
                "source",
                "target",
                "carrier_action",
                "operation_map",
                "row_map",
                "preparation_map",
                "context_map",
                "probe_map",
                "readout_map",
                "record_map",
                "gauge_map",
            )
        ),
        path,
    )
    if _string(raw["schema"], f"{path}.schema") != REGADDR_SCHEMA:
        _fail(f"{path}.schema", "wrong RegAddr schema")
    kind = _string(raw["kind"], f"{path}.kind")
    if kind not in ("EMBEDDING", "ISOMORPHISM"):
        _fail(f"{path}.kind", "unknown regional-map kind")
    rows = []
    for index, item in enumerate(_array(raw["row_map"], f"{path}.row_map")):
        entry = _mapping(
            item,
            frozenset(
                (
                    "source_left",
                    "source_right",
                    "target_left",
                    "target_right",
                    "source_tau",
                    "target_tau",
                    "source_status",
                    "target_status",
                    "source_result_class",
                    "target_result_class",
                    "source_law",
                    "target_law",
                    "source_observed_signature",
                    "target_observed_signature",
                )
            ),
            f"{path}.row_map[{index}]",
        )
        rows.append(
            RowPairMap(
                _string(entry["source_left"], f"{path}.row_map[{index}].source_left"),
                _string(entry["source_right"], f"{path}.row_map[{index}].source_right"),
                _string(entry["target_left"], f"{path}.row_map[{index}].target_left"),
                _string(entry["target_right"], f"{path}.row_map[{index}].target_right"),
                _string(entry["source_tau"], f"{path}.row_map[{index}].source_tau"),
                _string(entry["target_tau"], f"{path}.row_map[{index}].target_tau"),
                _string(entry["source_status"], f"{path}.row_map[{index}].source_status"),
                _string(entry["target_status"], f"{path}.row_map[{index}].target_status"),
                _nullable_string(
                    entry["source_result_class"],
                    f"{path}.row_map[{index}].source_result_class",
                ),
                _nullable_string(
                    entry["target_result_class"],
                    f"{path}.row_map[{index}].target_result_class",
                ),
                None
                if entry["source_law"] is None
                else _parse_law(entry["source_law"], f"{path}.row_map[{index}].source_law"),
                None
                if entry["target_law"] is None
                else _parse_law(entry["target_law"], f"{path}.row_map[{index}].target_law"),
                _parse_signature(
                    entry["source_observed_signature"],
                    f"{path}.row_map[{index}].source_observed_signature",
                    nullable=True,
                ),
                _parse_signature(
                    entry["target_observed_signature"],
                    f"{path}.row_map[{index}].target_observed_signature",
                    nullable=True,
                ),
            )
        )
    return RegAddr(
        handle=_string(raw["handle"], f"{path}.handle"),
        kind=kind,
        source=_string(raw["source"], f"{path}.source"),
        target=_string(raw["target"], f"{path}.target"),
        carrier_action=_parse_law(raw["carrier_action"], f"{path}.carrier_action"),
        operation_map=_parse_pair_maps(raw["operation_map"], f"{path}.operation_map"),
        row_map=tuple(rows),
        preparation_map=_parse_pair_maps(raw["preparation_map"], f"{path}.preparation_map"),
        context_map=_parse_pair_maps(raw["context_map"], f"{path}.context_map"),
        probe_map=_parse_pair_maps(raw["probe_map"], f"{path}.probe_map"),
        readout_map=_parse_pair_maps(raw["readout_map"], f"{path}.readout_map"),
        record_map=_parse_pair_maps(raw["record_map"], f"{path}.record_map"),
        gauge_map=_parse_pair_maps(raw["gauge_map"], f"{path}.gauge_map"),
    )


def _pair_dictionary(
    values: Sequence[PairMap],
    source_handles: FrozenSet[str],
    target_handles: FrozenSet[str],
    kind: str,
    path: str,
) -> Mapping[str, str]:
    sources = tuple(value.source for value in values)
    targets = tuple(value.target for value in values)
    if len(sources) != len(set(sources)) or len(targets) != len(set(targets)):
        _fail(path, "map is not injective")
    if frozenset(sources) != source_handles:
        _fail(path, "map does not cover every source field exactly once")
    if not frozenset(targets) <= target_handles:
        _fail(path, "map references an unknown target field")
    if kind == "ISOMORPHISM" and frozenset(targets) != target_handles:
        _fail(path, "isomorphism is not target-surjective")
    return {value.source: value.target for value in values}


def _payload_transport(action: MonomialLaw, payload: Tuple[int, ...]) -> Tuple[int, ...]:
    if len(payload) != action.dimension:
        raise VerificationError("payload/action carrier mismatch")
    result = [0] * len(payload)
    for source, target in enumerate(action.permutation):
        result[target] = payload[source]
    return tuple(result)


def _transform_witness(action: MonomialLaw, witness: Witness) -> Witness:
    action_matrix = action.to_matrix()
    return Witness(
        preparations=tuple(mv(action_matrix, value) for value in witness.preparations),
        alternative_projectors=tuple(conjugate_dense(action, value) for value in witness.alternative_projectors),
        cut_record_projectors=tuple(conjugate_dense(action, value) for value in witness.cut_record_projectors),
        availability_probes=tuple(conjugate_dense(action, value) for value in witness.availability_probes),
        write=conjugate_dense(action, witness.write),
        preserving=tuple(conjugate_dense(action, value) for value in witness.preserving),
        erasing=tuple(conjugate_dense(action, value) for value in witness.erasing),
        no_write=conjugate_dense(action, witness.no_write),
    )


def _vector_projector(value: Vector) -> Matrix:
    return tuple(
        tuple(left * right.conjugate() for right in value)
        for left in value
    )


def _witness_equivalent(left: Witness, right: Witness) -> bool:
    """Compare preparation rays and every other record field exactly."""

    return (
        len(left.preparations) == len(right.preparations)
        and all(
            _vector_projector(a) == _vector_projector(b)
            for a, b in zip(left.preparations, right.preparations)
        )
        and left.alternative_projectors == right.alternative_projectors
        and left.cut_record_projectors == right.cut_record_projectors
        and left.availability_probes == right.availability_probes
        and left.write == right.write
        and left.preserving == right.preserving
        and left.erasing == right.erasing
        and left.no_write == right.no_write
    )


@dataclass(frozen=True)
class RegAddrVerification:
    operation_entries: int
    row_entries: int
    field_entries: Mapping[str, int]


def verify_regaddr(source: Dataset, target: Dataset, arrow: RegAddr) -> RegAddrVerification:
    if arrow.source != source.handle or arrow.target != target.handle:
        raise VerificationError("RegAddr endpoint handles are mistyped")
    if source.carrier_dimension != target.carrier_dimension:
        raise VerificationError("RegAddr endpoints have different carriers")
    if arrow.carrier_action.dimension != source.carrier_dimension:
        raise VerificationError("RegAddr carrier action has the wrong dimension")
    source_operations = _handle_map(source.operations, "source.operations")
    target_operations = _handle_map(target.operations, "target.operations")
    operation_map = _pair_dictionary(
        arrow.operation_map,
        frozenset(source_operations),
        frozenset(target_operations),
        arrow.kind,
        "arrow.operation_map",
    )
    for source_handle, target_handle in operation_map.items():
        left = source_operations[source_handle]
        right = target_operations[target_handle]
        if (
            left.source_type != right.source_type
            or left.target_type != right.target_type
            or left.independently_selectable != right.independently_selectable
            or left.law.conjugated(arrow.carrier_action) != right.law
            or right.observed_signature != right.law.signature()
        ):
            raise VerificationError("RegAddr operation map fails fieldwise intertwining")

    source_rows = source.row_map
    target_rows = target.row_map
    source_pairs = tuple((value.source_left, value.source_right) for value in arrow.row_map)
    target_pairs = tuple((value.target_left, value.target_right) for value in arrow.row_map)
    if len(source_pairs) != len(set(source_pairs)) or len(target_pairs) != len(set(target_pairs)):
        raise VerificationError("RegAddr row map duplicates a row")
    if frozenset(source_pairs) != frozenset(source_rows):
        raise VerificationError("RegAddr row map omits or invents a source row")
    if not frozenset(target_pairs) <= frozenset(target_rows):
        raise VerificationError("RegAddr row map references an unknown target row")
    if arrow.kind == "ISOMORPHISM" and frozenset(target_pairs) != frozenset(target_rows):
        raise VerificationError("RegAddr isomorphism is not row-surjective")
    for row_pair in arrow.row_map:
        if (
            row_pair.target_left != operation_map[row_pair.source_left]
            or row_pair.target_right != operation_map[row_pair.source_right]
        ):
            raise VerificationError("RegAddr row endpoints disagree with operation map")
        left = source_rows[(row_pair.source_left, row_pair.source_right)]
        right = target_rows[(row_pair.target_left, row_pair.target_right)]
        if (
            row_pair.source_tau != left.tau
            or row_pair.target_tau != right.tau
            or row_pair.source_status != left.status
            or row_pair.target_status != right.status
            or row_pair.source_result_class != left.result_class
            or row_pair.target_result_class != right.result_class
            or row_pair.source_law != left.law
            or row_pair.target_law != right.law
            or row_pair.source_observed_signature != left.observed_signature
            or row_pair.target_observed_signature != right.observed_signature
        ):
            raise VerificationError("RegAddr row map's carried metadata differs from raw rows")
        expected_result = (
            None if left.result_class is None else operation_map[left.result_class]
        )
        transformed_law = (
            None if left.law is None else left.law.conjugated(arrow.carrier_action)
        )
        transformed_signature = (
            None if transformed_law is None else transformed_law.signature()
        )
        if (
            left.tau != right.tau
            or left.status != right.status
            or expected_result != right.result_class
            or transformed_law != right.law
            or transformed_signature != right.observed_signature
        ):
            raise VerificationError("RegAddr row map fails tau/status/result/law/signature")

    family_specs = (
        ("preparation_map", source.preparations, target.preparations),
        ("probe_map", source.probes, target.probes),
        ("readout_map", source.readouts, target.readouts),
        ("record_map", source.records, target.records),
        ("gauge_map", source.gauges, target.gauges),
        ("context_map", source.contexts, target.contexts),
    )
    dictionaries: Dict[str, Mapping[str, str]] = {}
    source_family_maps: Dict[str, Mapping[str, object]] = {}
    target_family_maps: Dict[str, Mapping[str, object]] = {}
    for name, source_values, target_values in family_specs:
        source_map = _handle_map(source_values, f"source.{name}")
        target_map = _handle_map(target_values, f"target.{name}")
        dictionaries[name] = _pair_dictionary(
            getattr(arrow, name),
            frozenset(source_map),
            frozenset(target_map),
            arrow.kind,
            f"arrow.{name}",
        )
        source_family_maps[name] = source_map
        target_family_maps[name] = target_map

    for name in ("preparation_map", "probe_map"):
        for source_handle, target_handle in dictionaries[name].items():
            left = source_family_maps[name][source_handle]
            right = target_family_maps[name][target_handle]
            if (
                left.boundary_type != right.boundary_type
                or _payload_transport(arrow.carrier_action, left.payload) != right.payload
            ):
                raise VerificationError(f"RegAddr {name} fails payload transport")

    for source_handle, target_handle in dictionaries["readout_map"].items():
        left = source_family_maps["readout_map"][source_handle]
        right = target_family_maps["readout_map"][target_handle]
        if (
            left.boundary_type != right.boundary_type
            or frozenset(map_projector_atoms(arrow.carrier_action, left.projector_resolution))
            != frozenset(right.projector_resolution)
        ):
            raise VerificationError("RegAddr readout map fails projector transport")

    for source_handle, target_handle in dictionaries["gauge_map"].items():
        left = source_family_maps["gauge_map"][source_handle]
        right = target_family_maps["gauge_map"][target_handle]
        if (
            left.boundary_type != right.boundary_type
            or left.law.conjugated(arrow.carrier_action) != right.law
        ):
            raise VerificationError("RegAddr gauge map fails law transport")

    for source_handle, target_handle in dictionaries["record_map"].items():
        left = source_family_maps["record_map"][source_handle]
        right = target_family_maps["record_map"][target_handle]
        mapped_access = frozenset(operation_map[handle] for handle in left.access_operations)
        target_access = frozenset(right.access_operations)
        access_ok = (
            mapped_access == target_access
            if arrow.kind == "ISOMORPHISM"
            else mapped_access <= target_access
        )
        if (
            left.boundary_type != right.boundary_type
            or not access_ok
            or not _witness_equivalent(
                _transform_witness(arrow.carrier_action, left.witness),
                right.witness,
            )
            or frozenset(map_projector_atoms(arrow.carrier_action, left.ambient_projector_resolution))
            != frozenset(right.ambient_projector_resolution)
            or not evaluate_w3(left.witness).passes
            or not evaluate_w3(right.witness).passes
        ):
            raise VerificationError("RegAddr record map fails dynamics/projector/W3 transport")

    preparation_map = dictionaries["preparation_map"]
    probe_map = dictionaries["probe_map"]
    readout_map = dictionaries["readout_map"]
    record_map = dictionaries["record_map"]
    gauge_map = dictionaries["gauge_map"]
    for source_handle, target_handle in dictionaries["context_map"].items():
        left = source_family_maps["context_map"][source_handle]
        right = target_family_maps["context_map"][target_handle]

        def compare(mapped: FrozenSet[str], target_values: FrozenSet[str]) -> bool:
            return mapped == target_values if arrow.kind == "ISOMORPHISM" else mapped <= target_values

        if (
            left.boundary_type != right.boundary_type
            or not compare(
                frozenset(operation_map[handle] for handle in left.operation_handles),
                frozenset(right.operation_handles),
            )
            or not compare(
                frozenset(preparation_map[handle] for handle in left.preparation_handles),
                frozenset(right.preparation_handles),
            )
            or not compare(
                frozenset(probe_map[handle] for handle in left.probe_handles),
                frozenset(right.probe_handles),
            )
            or not compare(
                frozenset(readout_map[handle] for handle in left.readout_handles),
                frozenset(right.readout_handles),
            )
            or not compare(
                frozenset(record_map[handle] for handle in left.record_handles),
                frozenset(right.record_handles),
            )
            or not compare(
                frozenset(gauge_map[handle] for handle in left.gauge_handles),
                frozenset(right.gauge_handles),
            )
        ):
            raise VerificationError("RegAddr context map is not field-complete")

    return RegAddrVerification(
        operation_entries=len(arrow.operation_map),
        row_entries=len(arrow.row_map),
        field_entries={name: len(getattr(arrow, name)) for name, _left, _right in family_specs},
    )


def _compose_pair_maps(first: Sequence[PairMap], second: Sequence[PairMap]) -> Tuple[PairMap, ...]:
    right = {value.source: value.target for value in second}
    if not set(value.target for value in first) <= set(right):
        raise VerificationError("regional maps are not composable")
    return tuple(
        PairMap(value.source, right[value.target])
        for value in first
    )


def compose_regaddr(first: RegAddr, second: RegAddr, handle: str = "composite") -> RegAddr:
    if first.target != second.source:
        raise VerificationError("RegAddr endpoint mismatch in composition")
    second_rows = {
        (value.source_left, value.source_right): value for value in second.row_map
    }
    rows = []
    for value in first.row_map:
        key = (value.target_left, value.target_right)
        if key not in second_rows:
            raise VerificationError("RegAddr row maps are not composable")
        target = second_rows[key]
        rows.append(
            RowPairMap(
                value.source_left,
                value.source_right,
                target.target_left,
                target.target_right,
                value.source_tau,
                target.target_tau,
                value.source_status,
                target.target_status,
                value.source_result_class,
                target.target_result_class,
                value.source_law,
                target.target_law,
                value.source_observed_signature,
                target.target_observed_signature,
            )
        )
    kind = (
        "ISOMORPHISM"
        if first.kind == second.kind == "ISOMORPHISM"
        else "EMBEDDING"
    )
    return RegAddr(
        handle=handle,
        kind=kind,
        source=first.source,
        target=second.target,
        carrier_action=second.carrier_action.after(first.carrier_action),
        operation_map=_compose_pair_maps(first.operation_map, second.operation_map),
        row_map=tuple(rows),
        preparation_map=_compose_pair_maps(first.preparation_map, second.preparation_map),
        context_map=_compose_pair_maps(first.context_map, second.context_map),
        probe_map=_compose_pair_maps(first.probe_map, second.probe_map),
        readout_map=_compose_pair_maps(first.readout_map, second.readout_map),
        record_map=_compose_pair_maps(first.record_map, second.record_map),
        gauge_map=_compose_pair_maps(first.gauge_map, second.gauge_map),
    )


def _arrow_content(value: RegAddr) -> Tuple[object, ...]:
    def pairs(items: Sequence[PairMap]) -> Tuple[Tuple[str, str], ...]:
        return tuple(sorted((item.source, item.target) for item in items))

    return (
        value.kind,
        value.source,
        value.target,
        value.carrier_action,
        pairs(value.operation_map),
        tuple(
            sorted(
                (
                    item.source_left,
                    item.source_right,
                    item.target_left,
                    item.target_right,
                    item.source_tau,
                    item.target_tau,
                    item.source_status,
                    item.target_status,
                    item.source_result_class,
                    item.target_result_class,
                    item.source_law,
                    item.target_law,
                    item.source_observed_signature,
                    item.target_observed_signature,
                )
                for item in value.row_map
            )
        ),
        pairs(value.preparation_map),
        pairs(value.context_map),
        pairs(value.probe_map),
        pairs(value.readout_map),
        pairs(value.record_map),
        pairs(value.gauge_map),
    )


def regaddr_equal(left: RegAddr, right: RegAddr) -> bool:
    return _arrow_content(left) == _arrow_content(right)


# ---------------------------------------------------------------------------
# Overlap-first category and full triple verification
# ---------------------------------------------------------------------------


def _scope_from_handles(group: GroupView, handles: Iterable[str]) -> Subobject:
    handles = tuple(handles)
    if not set(handles) <= set(group.index):
        raise VerificationError("scope references an unknown operation")
    return subgroup_generated(group, (group.index[handle] for handle in handles))


def operational_scopes(dataset: Dataset) -> Tuple[FrozenSet[str], ...]:
    group = build_group(dataset)
    result = set()
    for context in dataset.contexts:
        seed = frozenset(group.index[handle] for handle in context.operation_handles)
        closure = subgroup_generated(group, seed)
        if closure != seed:
            raise VerificationError("operational context is not composition-closed")
        if 1 < len(closure) < group.order:
            result.add(frozenset(group.handles[index] for index in closure))
    return tuple(sorted(result, key=lambda value: (len(value), tuple(sorted(value)))))


def record_scopes(dataset: Dataset) -> Tuple[FrozenSet[str], ...]:
    group = build_group(dataset)
    result = set()
    for record in dataset.records:
        decision = evaluate_w3(record.witness)
        if not decision.passes:
            continue
        seed = frozenset(group.index[handle] for handle in record.access_operations)
        closure = subgroup_generated(group, seed)
        if closure != seed:
            raise VerificationError("record access support is not composition-closed")
        if 1 < len(closure) < group.order:
            result.add(frozenset(group.handles[index] for index in closure))
    return tuple(sorted(result, key=lambda value: (len(value), tuple(sorted(value)))))


def _parse_scope_array(value: object, path: str) -> Tuple[FrozenSet[str], ...]:
    scopes = tuple(
        frozenset(
            _unique_strings(item, f"{path}[{index}]", allow_empty=False)
        )
        for index, item in enumerate(_array(value, path))
    )
    if len(scopes) != len(set(scopes)):
        _fail(path, "scope list contains duplicates")
    return tuple(sorted(scopes, key=lambda item: (len(item), tuple(sorted(item)))))


@dataclass(frozen=True)
class PairIntersectionClaim:
    left: str
    right: str
    intersection: str
    ambient: str
    to_left: str
    to_right: str
    left_to_ambient: str
    right_to_ambient: str
    intersection_to_ambient: str


@dataclass(frozen=True)
class TripleIntersectionClaim:
    regions: Tuple[str, str, str]
    intersection: str
    ambient: str
    to_regions: Tuple[str, str, str]
    region_to_ambient: Tuple[str, str, str]
    intersection_to_ambient: str


def _parse_pair_intersection(value: object, path: str) -> PairIntersectionClaim:
    raw = _mapping(
        value,
        frozenset(
            (
                "left",
                "right",
                "intersection",
                "ambient",
                "to_left",
                "to_right",
                "left_to_ambient",
                "right_to_ambient",
                "intersection_to_ambient",
            )
        ),
        path,
    )
    return PairIntersectionClaim(
        *(
            _string(raw[name], f"{path}.{name}")
            for name in (
                "left",
                "right",
                "intersection",
                "ambient",
                "to_left",
                "to_right",
                "left_to_ambient",
                "right_to_ambient",
                "intersection_to_ambient",
            )
        )
    )


def _triple_strings(value: object, path: str) -> Tuple[str, str, str]:
    result = _unique_strings(value, path, allow_empty=False)
    if len(result) != 3:
        _fail(path, "triple field must contain exactly three distinct handles")
    return result


def _parse_triple_intersection(value: object, path: str) -> TripleIntersectionClaim:
    raw = _mapping(
        value,
        frozenset(
            (
                "regions",
                "intersection",
                "ambient",
                "to_regions",
                "region_to_ambient",
                "intersection_to_ambient",
            )
        ),
        path,
    )
    return TripleIntersectionClaim(
        regions=_triple_strings(raw["regions"], f"{path}.regions"),
        intersection=_string(raw["intersection"], f"{path}.intersection"),
        ambient=_string(raw["ambient"], f"{path}.ambient"),
        to_regions=_triple_strings(raw["to_regions"], f"{path}.to_regions"),
        region_to_ambient=_triple_strings(
            raw["region_to_ambient"], f"{path}.region_to_ambient"
        ),
        intersection_to_ambient=_string(
            raw["intersection_to_ambient"],
            f"{path}.intersection_to_ambient",
        ),
    )


@dataclass(frozen=True)
class AtlasVerification:
    category: str
    operational_scopes: int
    record_scopes: int
    objects: int
    arrows: int
    pair_intersections: int
    triple_intersections: int
    coherent_paths: int


def verify_overlap_claim(dataset_raw: object, claim_raw: object) -> AtlasVerification:
    ambient = parse_dataset(dataset_raw, "dataset")
    raw = _mapping(
        claim_raw,
        frozenset(
            (
                "schema",
                "kind",
                "op_scopes",
                "rec_scopes",
                "objects",
                "arrows",
                "pair_intersections",
                "triple_intersections",
            )
        ),
        "claim",
    )
    if _string(raw["schema"], "claim.schema") != ATLAS_CLAIM_SCHEMA:
        _fail("claim.schema", "wrong overlap-claim schema")
    kind = _string(raw["kind"], "claim.kind")
    if kind not in ("OVERLAP-FIRST-ATLAS", "OVERLAP-FIRST-NONE"):
        _fail("claim.kind", "wrong overlap claim kind")
    claimed_op = _parse_scope_array(raw["op_scopes"], "claim.op_scopes")
    claimed_rec = _parse_scope_array(raw["rec_scopes"], "claim.rec_scopes")
    actual_op = operational_scopes(ambient)
    actual_rec = record_scopes(ambient)
    if claimed_op != actual_op or claimed_rec != actual_rec:
        raise VerificationError("claimed operational/record scopes differ from reconstruction")
    if kind == "OVERLAP-FIRST-NONE":
        if actual_op == actual_rec:
            raise VerificationError("claimed overlap negative has agreeing reconstructions")
        if any(
            _array(raw[name], f"claim.{name}")
            for name in (
                "objects",
                "arrows",
                "pair_intersections",
                "triple_intersections",
            )
        ):
            raise VerificationError("overlap negative carries positive regional artifacts")
        return AtlasVerification(
            category="scientific-negative",
            operational_scopes=len(actual_op),
            record_scopes=len(actual_rec),
            objects=0,
            arrows=0,
            pair_intersections=0,
            triple_intersections=0,
            coherent_paths=0,
        )
    if actual_op != actual_rec:
        raise VerificationError("operational and record regional categories do not agree")

    objects = tuple(
        parse_dataset(item, f"claim.objects[{index}]")
        for index, item in enumerate(_array(raw["objects"], "claim.objects"))
    )
    object_map = {value.handle: value for value in objects}
    if len(object_map) != len(objects):
        raise VerificationError("overlap claim contains duplicate object handles")
    if ambient.handle not in object_map:
        raise VerificationError("overlap claim omits the ambient instrument object")
    expected_scopes = set(actual_op) | {frozenset(value.handle for value in ambient.operations)}
    observed_scopes = {
        frozenset(value.handle for value in dataset.operations) for dataset in objects
    }
    if expected_scopes != observed_scopes or len(observed_scopes) != len(objects):
        raise VerificationError("overlap objects do not realize exactly the reconstructed scopes")
    for dataset in objects:
        scope = frozenset(value.handle for value in dataset.operations)
        if scope != frozenset(value.handle for value in ambient.operations):
            if not dataset.records or not all(evaluate_w3(value.witness).passes for value in dataset.records):
                raise VerificationError("proper overlap object is not record-bearing")

    arrows = tuple(
        parse_regaddr(item, f"claim.arrows[{index}]")
        for index, item in enumerate(_array(raw["arrows"], "claim.arrows"))
    )
    arrow_map = {value.handle: value for value in arrows}
    if len(arrow_map) != len(arrows):
        raise VerificationError("overlap claim contains duplicate arrow handles")
    for arrow in arrows:
        if arrow.source not in object_map or arrow.target not in object_map:
            raise VerificationError("overlap arrow references an unknown object")
        verify_regaddr(object_map[arrow.source], object_map[arrow.target], arrow)

    coherent_paths = 0
    for first in arrows:
        for second in arrows:
            if first.target != second.source:
                continue
            direct = tuple(
                value
                for value in arrows
                if value.source == first.source and value.target == second.target
            )
            if len(direct) != 1:
                raise VerificationError("regional category lacks a unique direct composite arrow")
            if not regaddr_equal(compose_regaddr(first, second), direct[0]):
                raise VerificationError("regional direct-versus-composite diagram fails")
            coherent_paths += 1

    pair_claims = tuple(
        _parse_pair_intersection(item, f"claim.pair_intersections[{index}]")
        for index, item in enumerate(
            _array(raw["pair_intersections"], "claim.pair_intersections")
        )
    )
    for pair in pair_claims:
        if any(
            handle not in object_map
            for handle in (pair.left, pair.right, pair.intersection, pair.ambient)
        ) or any(
            handle not in arrow_map
            for handle in (
                pair.to_left,
                pair.to_right,
                pair.left_to_ambient,
                pair.right_to_ambient,
                pair.intersection_to_ambient,
            )
        ):
            raise VerificationError("pair intersection references an unknown object or arrow")
        left_scope = frozenset(value.handle for value in object_map[pair.left].operations)
        right_scope = frozenset(value.handle for value in object_map[pair.right].operations)
        intersection_scope = frozenset(
            value.handle for value in object_map[pair.intersection].operations
        )
        if intersection_scope != left_scope & right_scope:
            raise VerificationError("pair intersection instrument has the wrong operational pullback")
        to_left = arrow_map[pair.to_left]
        to_right = arrow_map[pair.to_right]
        left_ambient = arrow_map[pair.left_to_ambient]
        right_ambient = arrow_map[pair.right_to_ambient]
        direct = arrow_map[pair.intersection_to_ambient]
        if (
            to_left.source != pair.intersection
            or to_left.target != pair.left
            or to_right.source != pair.intersection
            or to_right.target != pair.right
            or not regaddr_equal(compose_regaddr(to_left, left_ambient), direct)
            or not regaddr_equal(compose_regaddr(to_right, right_ambient), direct)
        ):
            raise VerificationError("pair intersection square does not commute")
        # Finite universal-property check over every claimed object and arrow.
        for candidate in objects:
            to_l = [a for a in arrows if a.source == candidate.handle and a.target == pair.left]
            to_r = [a for a in arrows if a.source == candidate.handle and a.target == pair.right]
            compatible_cones = [
                (a, b)
                for a in to_l
                for b in to_r
                if regaddr_equal(compose_regaddr(a, left_ambient), compose_regaddr(b, right_ambient))
            ]
            for a, b in compatible_cones:
                mediators = [
                    m
                    for m in arrows
                    if m.source == candidate.handle
                    and m.target == pair.intersection
                    and regaddr_equal(compose_regaddr(m, to_left), a)
                    and regaddr_equal(compose_regaddr(m, to_right), b)
                ]
                if len(mediators) != 1:
                    raise VerificationError("pair intersection fails the finite pullback universal property")

    triple_claims = tuple(
        _parse_triple_intersection(item, f"claim.triple_intersections[{index}]")
        for index, item in enumerate(
            _array(raw["triple_intersections"], "claim.triple_intersections")
        )
    )
    for triple in triple_claims:
        if triple.intersection not in object_map or triple.ambient not in object_map:
            raise VerificationError("triple intersection references an unknown object")
        if any(value not in object_map for value in triple.regions) or any(
            value not in arrow_map
            for value in triple.to_regions
            + triple.region_to_ambient
            + (triple.intersection_to_ambient,)
        ):
            raise VerificationError("triple intersection references unknown regions/arrows")
        scopes = [
            frozenset(value.handle for value in object_map[handle].operations)
            for handle in triple.regions
        ]
        intersection_scope = frozenset(
            value.handle for value in object_map[triple.intersection].operations
        )
        if intersection_scope != frozenset.intersection(*scopes):
            raise VerificationError("triple intersection instrument has the wrong operational pullback")
        direct = arrow_map[triple.intersection_to_ambient]
        for to_region_handle, to_ambient_handle, region in zip(
            triple.to_regions, triple.region_to_ambient, triple.regions
        ):
            to_region = arrow_map[to_region_handle]
            to_ambient = arrow_map[to_ambient_handle]
            if (
                to_region.source != triple.intersection
                or to_region.target != region
                or not regaddr_equal(compose_regaddr(to_region, to_ambient), direct)
            ):
                raise VerificationError("triple intersection cone does not commute")

    return AtlasVerification(
        category="positive",
        operational_scopes=len(actual_op),
        record_scopes=len(actual_rec),
        objects=len(objects),
        arrows=len(arrows),
        pair_intersections=len(pair_claims),
        triple_intersections=len(triple_claims),
        coherent_paths=coherent_paths,
    )


@dataclass(frozen=True)
class TripleVerification:
    pair_maps_valid: int
    loop_commutes: bool
    differing_fields: Tuple[str, ...]


def verify_full_triple(value: object, path: str = "triple") -> TripleVerification:
    raw = _mapping(
        value,
        frozenset(("schema", "mode", "instruments", "pair_maps")),
        path,
    )
    if _string(raw["schema"], f"{path}.schema") != TRIPLE_SCHEMA:
        _fail(f"{path}.schema", "wrong triple schema")
    mode = _string(raw["mode"], f"{path}.mode")
    if mode not in ("COHERENT", "TWISTED"):
        _fail(f"{path}.mode", "unknown triple mode")
    instruments = tuple(
        parse_dataset(item, f"{path}.instruments[{index}]")
        for index, item in enumerate(_array(raw["instruments"], f"{path}.instruments"))
    )
    if len(instruments) != 3 or len({value.handle for value in instruments}) != 3:
        _fail(f"{path}.instruments", "triple requires three independently handled instruments")
    instrument_map = {value.handle: value for value in instruments}
    maps = tuple(
        parse_regaddr(item, f"{path}.pair_maps[{index}]")
        for index, item in enumerate(_array(raw["pair_maps"], f"{path}.pair_maps"))
    )
    if len(maps) != 3:
        _fail(f"{path}.pair_maps", "triple requires exactly three pair maps")
    for arrow in maps:
        if arrow.kind != "ISOMORPHISM":
            raise VerificationError("triple pair map is not a full isomorphism")
        if arrow.source not in instrument_map or arrow.target not in instrument_map:
            raise VerificationError("triple pair map has unknown endpoint")
        verify_regaddr(instrument_map[arrow.source], instrument_map[arrow.target], arrow)
    first = next((value for value in maps if value.source == instruments[0].handle and value.target == instruments[1].handle), None)
    second = next((value for value in maps if value.source == instruments[1].handle and value.target == instruments[2].handle), None)
    direct = next((value for value in maps if value.source == instruments[0].handle and value.target == instruments[2].handle), None)
    if first is None or second is None or direct is None:
        raise VerificationError("triple pair maps do not have the required orientation")
    composite = compose_regaddr(first, second)
    fields = (
        "carrier_action",
        "operation_map",
        "row_map",
        "preparation_map",
        "context_map",
        "probe_map",
        "readout_map",
        "record_map",
        "gauge_map",
    )
    differing = []
    for field in fields:
        if field == "carrier_action":
            equal = composite.carrier_action == direct.carrier_action
        elif field == "row_map":
            # RowPairMap equality includes endpoints, tau, statuses, result
            # classes, independently carried laws, and signatures.
            equal = {
                (value.source_left, value.source_right): value
                for value in composite.row_map
            } == {
                (value.source_left, value.source_right): value
                for value in direct.row_map
            }
        else:
            equal = tuple(sorted((v.source, v.target) for v in getattr(composite, field))) == tuple(sorted((v.source, v.target) for v in getattr(direct, field)))
        if not equal:
            differing.append(field)
    commutes = not differing
    if mode == "COHERENT" and not commutes:
        raise VerificationError("coherent triple fails the full-field loop equation")
    if mode == "TWISTED" and commutes:
        raise VerificationError("twisted triple does not fail the full-field loop equation")
    return TripleVerification(3, commutes, tuple(differing))
