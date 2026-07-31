#!/usr/bin/env python3
"""Generic exact estimator for the final RQ0-L0 certification cycle.

This is the estimator-before-truth surface required by the strict pin at
v13 ledger #41.  It contains no main fixture, hidden factorization, atlas
truth, topology, influence relation, spacetime object, field, or gravity
object.

Scientific equality never uses dataset, operation, context, or record
handles.  Complete composition rows carry independently supplied exact
monomial amplitude laws.  The finite factor search reads independent-
selectability declarations and returns replayable predicate certificates.

The only legacy import is the exact Q(zeta_24) linear-algebra/W3 layer.  It is
used as a verified arithmetic lemma, not as a factor estimator or fixture.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, FrozenSet, Iterable, Iterator, Mapping, Optional, Sequence, Tuple

try:  # package import
    from .rq0_l0_addressability_estimator_exact import (
        AlgebraBasis,
        INV_SQRT2,
        Matrix,
        Q24,
        RecordWitness,
        SQRT3,
        Vector,
        ZETA,
        adjoint,
        algebra_from_matrices,
        algebra_intersection_dimension,
        basis_vector,
        evaluate_record_witness,
        flatten,
        identity,
        is_projector,
        is_unitary,
        madd,
        matrix,
        matrices_commute,
        mmul,
        mscale,
        mv,
        shape,
        vector,
        zero_matrix,
    )
except ImportError:  # direct script execution
    from rq0_l0_addressability_estimator_exact import (
        AlgebraBasis,
        INV_SQRT2,
        Matrix,
        Q24,
        RecordWitness,
        SQRT3,
        Vector,
        ZETA,
        adjoint,
        algebra_from_matrices,
        algebra_intersection_dimension,
        basis_vector,
        evaluate_record_witness,
        flatten,
        identity,
        is_projector,
        is_unitary,
        madd,
        matrix,
        matrices_commute,
        mmul,
        mscale,
        mv,
        shape,
        vector,
        zero_matrix,
    )


ESTIMATOR_API_VERSION = "rq0-l0-final-certification-v1"
EXACT_SCALAR_FIELD = "Q(zeta_24), Phi_24(x)=x^8-x^4+1"
GAUGE_SCOPE = "global mu_24 row phase; finite carrier relabelling in controls"

MAX_CARRIER_DIMENSION = 64
MAX_OPERATION_CLASSES = 256
MAX_COMPOSITION_ROWS = 65_536
MAX_CANDIDATE_TESTS = 100_000
MAX_ISOMORPHISM_TESTS = 250_000

IMPLEMENTED = "IMPLEMENTED"
UNAVAILABLE = "UNAVAILABLE"
COLLAPSED = "COLLAPSED"
STATUSES = frozenset((IMPLEMENTED, UNAVAILABLE, COLLAPSED))


class InvalidInput(ValueError):
    """Procedural/type/exactness failure.  It cannot print a scientific rung."""


class AccessUnderdetermined(ValueError):
    """Operational aliases or access rows do not define one quotient object."""


def stable_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Exact monomial amplitude laws
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class MonomialLaw:
    """Exact unitary: |j> -> zeta_24^phase[j] |permutation[j]>."""

    permutation: Tuple[int, ...]
    phases: Tuple[int, ...]

    def __post_init__(self) -> None:
        dimension = len(self.permutation)
        if not dimension or len(self.phases) != dimension:
            raise InvalidInput("monomial law has inconsistent dimension")
        if tuple(sorted(self.permutation)) != tuple(range(dimension)):
            raise InvalidInput("monomial law permutation is not bijective")
        object.__setattr__(self, "phases", tuple(value % 24 for value in self.phases))

    @property
    def dimension(self) -> int:
        return len(self.permutation)

    @classmethod
    def unit(cls, dimension: int) -> "MonomialLaw":
        return cls(tuple(range(dimension)), (0,) * dimension)

    def after(self, right: "MonomialLaw") -> "MonomialLaw":
        """Return self o right.  No row ever calls this for UNAVAILABLE."""

        if self.dimension != right.dimension:
            raise InvalidInput("cannot compose amplitude laws on different carriers")
        permutation = tuple(self.permutation[right.permutation[index]] for index in range(self.dimension))
        phases = tuple(
            (right.phases[index] + self.phases[right.permutation[index]]) % 24
            for index in range(self.dimension)
        )
        return MonomialLaw(permutation, phases)

    def inverse(self) -> "MonomialLaw":
        inverse_permutation = [0] * self.dimension
        inverse_phases = [0] * self.dimension
        for source, target in enumerate(self.permutation):
            inverse_permutation[target] = source
            inverse_phases[target] = (-self.phases[source]) % 24
        return MonomialLaw(tuple(inverse_permutation), tuple(inverse_phases))

    def global_phase_equivalent(self, other: "MonomialLaw") -> bool:
        if self.permutation != other.permutation or self.dimension != other.dimension:
            return False
        offsets = {
            (left - right) % 24
            for left, right in zip(self.phases, other.phases)
        }
        return len(offsets) == 1

    def signature(self) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
        """Operational signature modulo the declared global mu_24 gauge."""

        anchor = self.phases[0]
        return self.permutation, tuple((value - anchor) % 24 for value in self.phases)

    def conjugated(self, action: "MonomialLaw") -> "MonomialLaw":
        return action.after(self).after(action.inverse())

    def to_matrix(self) -> Matrix:
        rows = [[Q24(0) for _ in range(self.dimension)] for _ in range(self.dimension)]
        for source, target in enumerate(self.permutation):
            rows[target][source] = ZETA ** self.phases[source]
        return tuple(tuple(row) for row in rows)

    def to_data(self) -> Mapping[str, object]:
        return {"permutation": list(self.permutation), "phases": list(self.phases)}

    @classmethod
    def from_data(cls, value: Mapping[str, object]) -> "MonomialLaw":
        return cls(
            tuple(int(entry) for entry in value["permutation"]),
            tuple(int(entry) for entry in value["phases"]),
        )


def permutation_law(permutation: Sequence[int]) -> MonomialLaw:
    return MonomialLaw(tuple(permutation), (0,) * len(permutation))


def q24_key(value: Q24) -> Tuple[Tuple[int, int], ...]:
    return value.sort_key()


def vector_key(value: Vector) -> Tuple[Tuple[Tuple[int, int], ...], ...]:
    return tuple(q24_key(entry) for entry in value)


def matrix_key(value: Matrix) -> Tuple[Tuple[Tuple[Tuple[int, int], ...], ...], ...]:
    return tuple(tuple(q24_key(entry) for entry in row) for row in value)


def q24_to_data(value: Q24) -> list[list[int]]:
    return [[entry.numerator, entry.denominator] for entry in value.coefficients]


def q24_from_data(value: Sequence[Sequence[int]]) -> Q24:
    from fractions import Fraction

    return Q24(tuple(Fraction(int(num), int(den)) for num, den in value))


def vector_to_data(value: Vector) -> list[object]:
    return [q24_to_data(entry) for entry in value]


def vector_from_data(value: Sequence[object]) -> Vector:
    return tuple(q24_from_data(entry) for entry in value)


def matrix_to_data(value: Matrix) -> list[object]:
    return [[q24_to_data(entry) for entry in row] for row in value]


def matrix_from_data(value: Sequence[Sequence[object]]) -> Matrix:
    return tuple(tuple(q24_from_data(entry) for entry in row) for row in value)


# ---------------------------------------------------------------------------
# Complete serialized instrument input
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class OperationClass:
    handle: str
    source_type: str
    target_type: str
    law: MonomialLaw
    observed_signature: Tuple[Tuple[int, ...], Tuple[int, ...]]
    independently_selectable: bool


@dataclass(frozen=True)
class CompositionRow:
    left: str
    right: str
    tau: str
    status: str
    result_class: Optional[str]
    law: Optional[MonomialLaw]
    observed_signature: Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]]


@dataclass(frozen=True)
class FieldDatum:
    handle: str
    boundary_type: str
    payload: Tuple[int, ...]

    def scientific_key(self) -> Tuple[str, Tuple[int, ...]]:
        return self.boundary_type, self.payload


@dataclass(frozen=True)
class ReadoutDatum:
    handle: str
    boundary_type: str
    projector_resolution: Tuple[FrozenSet[int], ...]

    def scientific_key(self) -> Tuple[str, Tuple[Tuple[int, ...], ...]]:
        return self.boundary_type, tuple(tuple(sorted(atom)) for atom in self.projector_resolution)


@dataclass(frozen=True)
class GaugeDatum:
    handle: str
    law: MonomialLaw

    def scientific_key(self) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
        return self.law.signature()


@dataclass(frozen=True)
class RecordCandidate:
    handle: str
    boundary_type: str
    access_operations: Tuple[str, ...]
    witness: RecordWitness
    ambient_projector_resolution: Tuple[FrozenSet[int], ...]

    def structural_key(self) -> Tuple[object, ...]:
        witness = self.witness
        return (
            self.boundary_type,
            tuple(vector_key(value) for value in witness.preparations),
            tuple(matrix_key(value) for value in witness.alternative_projectors),
            tuple(matrix_key(value) for value in witness.cut_record_projectors),
            tuple(matrix_key(value) for value in witness.availability_probes),
            matrix_key(witness.write),
            tuple(matrix_key(value) for value in witness.preserving),
            tuple(matrix_key(value) for value in witness.erasing),
            matrix_key(witness.no_write),
            tuple(tuple(sorted(atom)) for atom in self.ambient_projector_resolution),
        )


@dataclass(frozen=True)
class AccessContext:
    handle: str
    boundary_type: str
    operation_handles: Tuple[str, ...]
    preparation_handles: Tuple[str, ...]
    probe_handles: Tuple[str, ...]
    readout_handles: Tuple[str, ...]
    record_handles: Tuple[str, ...]
    gauge_handles: Tuple[str, ...]


@dataclass(frozen=True)
class OperationalDataset:
    handle: str
    carrier_dimension: int
    operations: Tuple[OperationClass, ...]
    composition_rows: Tuple[CompositionRow, ...]
    preparations: Tuple[FieldDatum, ...] = ()
    contexts: Tuple[AccessContext, ...] = ()
    probes: Tuple[FieldDatum, ...] = ()
    readouts: Tuple[ReadoutDatum, ...] = ()
    records: Tuple[RecordCandidate, ...] = ()
    gauge_actions: Tuple[GaugeDatum, ...] = ()
    access_postulate: str = "POSTULATE: finite exact operational selection/composition access"


def _signature_to_data(value: Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]]) -> object:
    if value is None:
        return None
    return [list(value[0]), list(value[1])]


def _signature_from_data(value: object) -> Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]]:
    if value is None:
        return None
    return tuple(int(entry) for entry in value[0]), tuple(int(entry) for entry in value[1])


def witness_to_data(value: RecordWitness) -> Mapping[str, object]:
    return {
        "handle": value.handle,
        "preparations": [vector_to_data(entry) for entry in value.preparations],
        "alternative_projectors": [matrix_to_data(entry) for entry in value.alternative_projectors],
        "cut_record_projectors": [matrix_to_data(entry) for entry in value.cut_record_projectors],
        "availability_probes": [matrix_to_data(entry) for entry in value.availability_probes],
        "write": matrix_to_data(value.write),
        "preserving": [matrix_to_data(entry) for entry in value.preserving],
        "erasing": [matrix_to_data(entry) for entry in value.erasing],
        "no_write": matrix_to_data(value.no_write),
    }


def witness_from_data(value: Mapping[str, object]) -> RecordWitness:
    return RecordWitness(
        handle=str(value["handle"]),
        preparations=tuple(vector_from_data(entry) for entry in value["preparations"]),
        alternative_projectors=tuple(matrix_from_data(entry) for entry in value["alternative_projectors"]),
        cut_record_projectors=tuple(matrix_from_data(entry) for entry in value["cut_record_projectors"]),
        availability_probes=tuple(matrix_from_data(entry) for entry in value["availability_probes"]),
        write=matrix_from_data(value["write"]),
        preserving=tuple(matrix_from_data(entry) for entry in value["preserving"]),
        erasing=tuple(matrix_from_data(entry) for entry in value["erasing"]),
        no_write=matrix_from_data(value["no_write"]),
    )


def dataset_to_data(dataset: OperationalDataset) -> Mapping[str, object]:
    return {
        "schema": ESTIMATOR_API_VERSION,
        "handle": dataset.handle,
        "carrier_dimension": dataset.carrier_dimension,
        "operations": [
            {
                "handle": value.handle,
                "source_type": value.source_type,
                "target_type": value.target_type,
                "law": value.law.to_data(),
                "observed_signature": _signature_to_data(value.observed_signature),
                "independently_selectable": value.independently_selectable,
            }
            for value in dataset.operations
        ],
        "composition_rows": [
            {
                "left": value.left,
                "right": value.right,
                "tau": value.tau,
                "status": value.status,
                "result_class": value.result_class,
                "law": None if value.law is None else value.law.to_data(),
                "observed_signature": _signature_to_data(value.observed_signature),
            }
            for value in dataset.composition_rows
        ],
        "preparations": [
            {"handle": value.handle, "boundary_type": value.boundary_type, "payload": list(value.payload)}
            for value in dataset.preparations
        ],
        "contexts": [
            {
                "handle": value.handle,
                "boundary_type": value.boundary_type,
                "operation_handles": list(value.operation_handles),
                "preparation_handles": list(value.preparation_handles),
                "probe_handles": list(value.probe_handles),
                "readout_handles": list(value.readout_handles),
                "record_handles": list(value.record_handles),
                "gauge_handles": list(value.gauge_handles),
            }
            for value in dataset.contexts
        ],
        "probes": [
            {"handle": value.handle, "boundary_type": value.boundary_type, "payload": list(value.payload)}
            for value in dataset.probes
        ],
        "readouts": [
            {
                "handle": value.handle,
                "boundary_type": value.boundary_type,
                "projector_resolution": [sorted(atom) for atom in value.projector_resolution],
            }
            for value in dataset.readouts
        ],
        "records": [
            {
                "handle": value.handle,
                "boundary_type": value.boundary_type,
                "access_operations": list(value.access_operations),
                "witness": witness_to_data(value.witness),
                "ambient_projector_resolution": [sorted(atom) for atom in value.ambient_projector_resolution],
            }
            for value in dataset.records
        ],
        "gauge_actions": [
            {"handle": value.handle, "law": value.law.to_data()}
            for value in dataset.gauge_actions
        ],
        "access_postulate": dataset.access_postulate,
    }


def dataset_from_data(value: Mapping[str, object]) -> OperationalDataset:
    if value.get("schema") != ESTIMATOR_API_VERSION:
        raise InvalidInput("serialized dataset has the wrong schema")
    try:
        return OperationalDataset(
            handle=str(value["handle"]),
            carrier_dimension=int(value["carrier_dimension"]),
            operations=tuple(
                OperationClass(
                    handle=str(entry["handle"]),
                    source_type=str(entry["source_type"]),
                    target_type=str(entry["target_type"]),
                    law=MonomialLaw.from_data(entry["law"]),
                    observed_signature=_signature_from_data(entry["observed_signature"]),
                    independently_selectable=bool(entry["independently_selectable"]),
                )
                for entry in value["operations"]
            ),
            composition_rows=tuple(
                CompositionRow(
                    left=str(entry["left"]),
                    right=str(entry["right"]),
                    tau=str(entry["tau"]),
                    status=str(entry["status"]),
                    result_class=None if entry["result_class"] is None else str(entry["result_class"]),
                    law=None if entry["law"] is None else MonomialLaw.from_data(entry["law"]),
                    observed_signature=_signature_from_data(entry["observed_signature"]),
                )
                for entry in value["composition_rows"]
            ),
            preparations=tuple(
                FieldDatum(str(entry["handle"]), str(entry["boundary_type"]), tuple(int(item) for item in entry["payload"]))
                for entry in value["preparations"]
            ),
            contexts=tuple(
                AccessContext(
                    handle=str(entry["handle"]),
                    boundary_type=str(entry["boundary_type"]),
                    operation_handles=tuple(str(item) for item in entry["operation_handles"]),
                    preparation_handles=tuple(str(item) for item in entry["preparation_handles"]),
                    probe_handles=tuple(str(item) for item in entry["probe_handles"]),
                    readout_handles=tuple(str(item) for item in entry["readout_handles"]),
                    record_handles=tuple(str(item) for item in entry["record_handles"]),
                    gauge_handles=tuple(str(item) for item in entry["gauge_handles"]),
                )
                for entry in value["contexts"]
            ),
            probes=tuple(
                FieldDatum(str(entry["handle"]), str(entry["boundary_type"]), tuple(int(item) for item in entry["payload"]))
                for entry in value["probes"]
            ),
            readouts=tuple(
                ReadoutDatum(
                    str(entry["handle"]),
                    str(entry["boundary_type"]),
                    tuple(frozenset(int(item) for item in atom) for atom in entry["projector_resolution"]),
                )
                for entry in value["readouts"]
            ),
            records=tuple(
                RecordCandidate(
                    handle=str(entry["handle"]),
                    boundary_type=str(entry["boundary_type"]),
                    access_operations=tuple(str(item) for item in entry["access_operations"]),
                    witness=witness_from_data(entry["witness"]),
                    ambient_projector_resolution=tuple(
                        frozenset(int(item) for item in atom)
                        for atom in entry["ambient_projector_resolution"]
                    ),
                )
                for entry in value["records"]
            ),
            gauge_actions=tuple(
                GaugeDatum(str(entry["handle"]), MonomialLaw.from_data(entry["law"]))
                for entry in value["gauge_actions"]
            ),
            access_postulate=str(value["access_postulate"]),
        )
    except (KeyError, TypeError, ValueError) as error:
        raise InvalidInput(f"malformed serialized dataset: {error}") from error


# ---------------------------------------------------------------------------
# Validation and quotient composition object
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RowAudit:
    typed_rows: int
    status_rows: int
    result_rows: int
    exact_law_rows: int
    physical_composition_rows: int
    gauge_rows: int
    signature_rows: int
    unavailable_rows: int
    collapsed_rows: int


@dataclass(frozen=True)
class QuotientClass:
    index: int
    aliases: Tuple[str, ...]
    source_type: str
    target_type: str
    law: MonomialLaw
    observed_signature: Tuple[Tuple[int, ...], Tuple[int, ...]]
    independently_selectable: bool


@dataclass(frozen=True)
class QuotientRow:
    left: int
    right: int
    tau: str
    status: str
    result: Optional[int]
    law: Optional[MonomialLaw]
    observed_signature: Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]]


@dataclass(frozen=True)
class CompositionObject:
    classes: Tuple[QuotientClass, ...]
    rows: Tuple[QuotientRow, ...]
    handle_to_class: Tuple[Tuple[str, int], ...]
    identity: Optional[int]
    total_implemented: bool
    associative: bool
    row_audit: RowAudit

    @property
    def size(self) -> int:
        return len(self.classes)

    def row(self, left: int, right: int) -> QuotientRow:
        return self.rows[left * self.size + right]

    def product(self, left: int, right: int) -> int:
        row = self.row(left, right)
        if row.status != IMPLEMENTED or row.result is None:
            raise AccessUnderdetermined("requested product is not implemented")
        return row.result

    def class_for_handle(self, handle: str) -> int:
        mapping = dict(self.handle_to_class)
        if handle not in mapping:
            raise InvalidInput(f"unknown operation handle {handle}")
        return mapping[handle]


def expected_tau(left: OperationClass, right: OperationClass) -> str:
    return f"{right.source_type}|{right.target_type}|{left.target_type}"


def _validate_field_handles(dataset: OperationalDataset) -> None:
    families = {
        "preparation": dataset.preparations,
        "context": dataset.contexts,
        "probe": dataset.probes,
        "readout": dataset.readouts,
        "record": dataset.records,
        "gauge": dataset.gauge_actions,
    }
    for label, values in families.items():
        handles = tuple(value.handle for value in values)
        if len(handles) != len(set(handles)):
            raise InvalidInput(f"duplicate {label} handle")


def validate_dataset_shape(dataset: OperationalDataset) -> None:
    if not 1 < dataset.carrier_dimension <= MAX_CARRIER_DIMENSION:
        raise InvalidInput("carrier dimension violates the frozen cap")
    if not dataset.operations or len(dataset.operations) > MAX_OPERATION_CLASSES:
        raise InvalidInput("operation count violates the frozen cap")
    if len(dataset.composition_rows) > MAX_COMPOSITION_ROWS:
        raise InvalidInput("composition-row count violates the frozen cap")
    handles = tuple(value.handle for value in dataset.operations)
    if len(handles) != len(set(handles)):
        raise InvalidInput("operation handles are not unique")
    for operation in dataset.operations:
        if operation.law.dimension != dataset.carrier_dimension:
            raise InvalidInput("operation law has the wrong carrier")
        if operation.observed_signature != operation.law.signature():
            raise InvalidInput("operation signature does not match its exact law")
        if not operation.source_type or not operation.target_type:
            raise InvalidInput("operation boundary type is empty")
    _validate_field_handles(dataset)
    operation_set = set(handles)
    expected_pairs = {(left, right) for left in handles for right in handles}
    observed_pairs = {(row.left, row.right) for row in dataset.composition_rows}
    if len(observed_pairs) != len(dataset.composition_rows):
        raise InvalidInput("composition table contains duplicate ordered rows")
    if observed_pairs != expected_pairs:
        raise InvalidInput("composition table is not complete over operation handles")
    for context in dataset.contexts:
        if not set(context.operation_handles) <= operation_set:
            raise InvalidInput("access context references an unknown operation")
    for record in dataset.records:
        if not set(record.access_operations) <= operation_set:
            raise InvalidInput("record support references an unknown operation")
        universe = frozenset(range(dataset.carrier_dimension))
        if not record.ambient_projector_resolution:
            raise InvalidInput("record has an empty ambient projector resolution")
        if any(not atom for atom in record.ambient_projector_resolution):
            raise InvalidInput("record ambient projector contains an empty atom")
        if any(left & right for left, right in itertools.combinations(record.ambient_projector_resolution, 2)):
            raise InvalidInput("record ambient projectors are not disjoint")
        if frozenset().union(*record.ambient_projector_resolution) != universe:
            raise InvalidInput("record ambient projectors do not resolve the carrier")


def _operation_alias_key(operation: OperationClass) -> Tuple[object, ...]:
    return (
        operation.source_type,
        operation.target_type,
        operation.observed_signature,
        operation.independently_selectable,
    )


def build_composition_object(dataset: OperationalDataset) -> CompositionObject:
    validate_dataset_shape(dataset)
    operation_map = {value.handle: value for value in dataset.operations}
    row_map = {(value.left, value.right): value for value in dataset.composition_rows}

    typed = status = result = exact_law = physical = gauge = signature = 0
    unavailable = collapsed = 0
    for row in dataset.composition_rows:
        left = operation_map[row.left]
        right = operation_map[row.right]
        if right.target_type != left.source_type or row.tau != expected_tau(left, right):
            raise InvalidInput("composition row fails boundary/context typing")
        typed += 1
        if row.status not in STATUSES:
            raise InvalidInput("composition row has an unknown status")
        if row.status == UNAVAILABLE:
            unavailable += 1
            if row.result_class is not None or row.law is not None or row.observed_signature is not None:
                raise InvalidInput("UNAVAILABLE row supplies a result or synthetic law")
            status += 1
            continue
        if row.result_class not in operation_map or row.law is None or row.observed_signature is None:
            raise InvalidInput("implemented/collapsed row lacks result or supplied law")
        status += 1
        if row.status == COLLAPSED:
            collapsed += 1
        result += 1
        if row.law.dimension != dataset.carrier_dimension:
            raise InvalidInput("row law has the wrong carrier")
        exact_law += 1
        composed = left.law.after(right.law)
        if not row.law.global_phase_equivalent(composed):
            raise InvalidInput("independently supplied row law disagrees with physical composition")
        physical += 1
        result_operation = operation_map[row.result_class]
        if not row.law.global_phase_equivalent(result_operation.law):
            raise InvalidInput("row law is not gauge-equivalent to the declared result class")
        gauge += 1
        if row.observed_signature != row.law.signature() or row.observed_signature != result_operation.observed_signature:
            raise InvalidInput("row operational signature mismatch")
        signature += 1

    groups: Dict[Tuple[object, ...], list[OperationClass]] = {}
    for operation in dataset.operations:
        groups.setdefault(_operation_alias_key(operation), []).append(operation)
    ordered_groups = sorted(
        groups.values(),
        key=lambda values: (
            values[0].source_type,
            values[0].target_type,
            values[0].observed_signature,
            tuple(sorted(value.handle for value in values)),
        ),
    )
    classes = []
    handle_to_class: Dict[str, int] = {}
    for index, aliases in enumerate(ordered_groups):
        aliases = sorted(aliases, key=lambda value: value.handle)
        representative = aliases[0]
        if any(not representative.law.global_phase_equivalent(value.law) for value in aliases[1:]):
            raise AccessUnderdetermined("signature aliases are not gauge-equivalent")
        value = QuotientClass(
            index=index,
            aliases=tuple(entry.handle for entry in aliases),
            source_type=representative.source_type,
            target_type=representative.target_type,
            law=representative.law,
            observed_signature=representative.observed_signature,
            independently_selectable=representative.independently_selectable,
        )
        classes.append(value)
        for alias in aliases:
            handle_to_class[alias.handle] = index

    quotient_rows = []
    for left_class in classes:
        for right_class in classes:
            candidates = []
            for left_alias in left_class.aliases:
                for right_alias in right_class.aliases:
                    raw = row_map[(left_alias, right_alias)]
                    candidates.append(
                        (
                            raw.tau,
                            raw.status,
                            None if raw.result_class is None else handle_to_class[raw.result_class],
                            None if raw.law is None else raw.law.signature(),
                            raw.observed_signature,
                            raw.law,
                        )
                    )
            comparable = {(tau, state, target, law_signature, observed) for tau, state, target, law_signature, observed, _ in candidates}
            if len(comparable) != 1:
                raise AccessUnderdetermined("operation aliases are not a composition congruence")
            tau, state, target, _, observed, supplied_law = candidates[0]
            quotient_rows.append(
                QuotientRow(
                    left=left_class.index,
                    right=right_class.index,
                    tau=tau,
                    status=state,
                    result=target,
                    law=supplied_law,
                    observed_signature=observed,
                )
            )

    size = len(classes)
    total_implemented = all(value.status == IMPLEMENTED for value in quotient_rows)
    identity_candidates = []
    if total_implemented:
        for candidate in range(size):
            if all(
                quotient_rows[candidate * size + other].result == other
                and quotient_rows[other * size + candidate].result == other
                for other in range(size)
            ):
                identity_candidates.append(candidate)
    identity_index = identity_candidates[0] if len(identity_candidates) == 1 else None
    associative = False
    if total_implemented and identity_index is not None:
        associative = all(
            quotient_rows[quotient_rows[left * size + middle].result * size + right].result
            == quotient_rows[left * size + quotient_rows[middle * size + right].result].result
            for left in range(size)
            for middle in range(size)
            for right in range(size)
        )
    return CompositionObject(
        classes=tuple(classes),
        rows=tuple(quotient_rows),
        handle_to_class=tuple(sorted(handle_to_class.items())),
        identity=identity_index,
        total_implemented=total_implemented,
        associative=associative,
        row_audit=RowAudit(
            typed_rows=typed,
            status_rows=status,
            result_rows=result,
            exact_law_rows=exact_law,
            physical_composition_rows=physical,
            gauge_rows=gauge,
            signature_rows=signature,
            unavailable_rows=unavailable,
            collapsed_rows=collapsed,
        ),
    )


# ---------------------------------------------------------------------------
# Complete finite normal-direct-factor search and replayable certificates
# ---------------------------------------------------------------------------


Subobject = FrozenSet[int]


def inverse_table(composition: CompositionObject) -> Tuple[int, ...]:
    if composition.identity is None or not composition.total_implemented or not composition.associative:
        raise AccessUnderdetermined("positive scope requires a total associative identity law")
    values = []
    for element in range(composition.size):
        candidates = tuple(
            other
            for other in range(composition.size)
            if composition.product(element, other) == composition.identity
            and composition.product(other, element) == composition.identity
        )
        if len(candidates) != 1:
            raise AccessUnderdetermined("positive scope requires unique inverses")
        values.append(candidates[0])
    return tuple(values)


def subgroup_generated(
    composition: CompositionObject,
    seeds: Iterable[int],
    inverses: Sequence[int],
) -> Subobject:
    if composition.identity is None:
        raise AccessUnderdetermined("subgroup generation requires an identity")
    current = {composition.identity}
    current.update(int(value) for value in seeds)
    changed = True
    while changed:
        changed = False
        for value in tuple(current):
            if inverses[value] not in current:
                current.add(inverses[value])
                changed = True
        for left in tuple(current):
            for right in tuple(current):
                product = composition.product(left, right)
                if product not in current:
                    current.add(product)
                    changed = True
    return frozenset(current)


def normal_closure(
    composition: CompositionObject,
    seeds: Iterable[int],
    inverses: Sequence[int],
) -> Subobject:
    conjugates = set()
    for group_element in range(composition.size):
        inverse = inverses[group_element]
        for seed in seeds:
            conjugates.add(composition.product(composition.product(group_element, seed), inverse))
    return subgroup_generated(composition, conjugates, inverses)


def enumerate_normal_subobjects(
    composition: CompositionObject,
    inverses: Sequence[int],
) -> Tuple[Tuple[Subobject, ...], int]:
    if composition.identity is None:
        return (), 0
    candidates = {frozenset((composition.identity,))}
    for element in range(composition.size):
        candidates.add(normal_closure(composition, (element,), inverses))
    tests = 0
    changed = True
    while changed:
        changed = False
        snapshot = tuple(sorted(candidates, key=lambda item: (len(item), tuple(sorted(item)))))
        for index, left in enumerate(snapshot):
            for right in snapshot[index:]:
                tests += 1
                if tests > MAX_CANDIDATE_TESTS:
                    raise InvalidInput("normal-subobject join search exceeded the frozen cap")
                joined = frozenset(
                    composition.product(a, b)
                    for a in left
                    for b in right
                )
                if joined not in candidates:
                    candidates.add(joined)
                    changed = True
    return tuple(sorted(candidates, key=lambda item: (len(item), tuple(sorted(item))))), tests


def subobjects_commute(composition: CompositionObject, left: Subobject, right: Subobject) -> bool:
    for a in left:
        for b in right:
            row_ab = composition.row(a, b)
            row_ba = composition.row(b, a)
            if row_ab.status != IMPLEMENTED or row_ba.status != IMPLEMENTED:
                return False
            if row_ab.result != row_ba.result or row_ab.law is None or row_ba.law is None:
                return False
            if not row_ab.law.global_phase_equivalent(row_ba.law):
                return False
            if row_ab.observed_signature != row_ba.observed_signature:
                return False
    return True


def multiply_tuple(
    composition: CompositionObject,
    entries: Sequence[int],
) -> int:
    if composition.identity is None:
        raise AccessUnderdetermined("multiplication requires an identity")
    value = composition.identity
    for entry in entries:
        value = composition.product(value, entry)
    return value


def multiplication_image(
    composition: CompositionObject,
    factors: Sequence[Subobject],
) -> Tuple[Subobject, Optional[Tuple[Tuple[int, ...], Tuple[int, ...], int]]]:
    image: Dict[int, Tuple[int, ...]] = {}
    for entries in itertools.product(*(tuple(sorted(value)) for value in factors)):
        result = multiply_tuple(composition, entries)
        if result in image and image[result] != entries:
            return frozenset(image), (image[result], entries, result)
        image[result] = entries
    return frozenset(image), None


def represented_algebra(
    composition: CompositionObject,
    elements: Iterable[int],
    carrier_dimension: int,
) -> AlgebraBasis:
    return algebra_from_matrices(
        (composition.classes[index].law.to_matrix() for index in sorted(set(elements))),
        carrier_dimension,
    )


def product_subobject(composition: CompositionObject, factors: Sequence[Subobject]) -> Subobject:
    image, collision = multiplication_image(composition, factors)
    if collision is not None:
        raise AccessUnderdetermined("claimed product subobject is not faithful")
    return image


def _closed_and_inverse(
    composition: CompositionObject,
    candidate: Subobject,
    inverses: Sequence[int],
) -> bool:
    return (
        composition.identity in candidate
        and all(inverses[value] in candidate for value in candidate)
        and all(composition.product(left, right) in candidate for left in candidate for right in candidate)
    )


def _restriction_stable(
    composition: CompositionObject,
    factors: Sequence[Subobject],
    inverses: Sequence[int],
) -> bool:
    for count in range(1, len(factors) + 1):
        for chosen in itertools.combinations(factors, count):
            region = product_subobject(composition, chosen)
            if not _closed_and_inverse(composition, region, inverses):
                return False
            for left in region:
                for right in region:
                    row = composition.row(left, right)
                    if row.status != IMPLEMENTED or row.result not in region or row.law is None:
                        return False
                    if row.observed_signature != row.law.signature():
                        return False
    return True


@dataclass(frozen=True)
class FactorCertificate:
    factors: Tuple[Subobject, ...]
    factor_orders: Tuple[int, ...]
    algebra_dimensions: Tuple[int, ...]
    independently_generated: bool
    mixed_implemented_both_orders: bool
    operationally_commuting: bool
    faithful_multiplication: bool
    multiplication_collision: Optional[Tuple[Tuple[int, ...], Tuple[int, ...], int]]
    closed_with_inverses: bool
    typed_scalar_intersection: bool
    represented_algebra_product: bool
    restriction_stable: bool

    @property
    def passes(self) -> bool:
        return (
            self.independently_generated
            and self.mixed_implemented_both_orders
            and self.operationally_commuting
            and self.faithful_multiplication
            and self.closed_with_inverses
            and self.typed_scalar_intersection
            and self.represented_algebra_product
            and self.restriction_stable
        )


def certify_factor_tuple(
    dataset: OperationalDataset,
    composition: CompositionObject,
    factors: Sequence[Subobject],
    inverses: Optional[Sequence[int]] = None,
) -> FactorCertificate:
    if inverses is None:
        inverses = inverse_table(composition)
    factors = tuple(frozenset(value) for value in factors)
    independently_generated = all(
        subgroup_generated(
            composition,
            (entry for entry in factor if composition.classes[entry].independently_selectable),
            inverses,
        )
        == factor
        for factor in factors
    )
    mixed_implemented = all(
        composition.row(a, b).status == IMPLEMENTED
        and composition.row(b, a).status == IMPLEMENTED
        for left, right in itertools.combinations(factors, 2)
        for a in left
        for b in right
    )
    operationally_commuting = all(
        subobjects_commute(composition, left, right)
        for left, right in itertools.combinations(factors, 2)
    )
    image, collision = multiplication_image(composition, factors)
    faithful = collision is None and len(image) == composition.size
    closed = all(_closed_and_inverse(composition, factor, inverses) for factor in factors)
    scalar_intersection = composition.identity is not None and all(
        left & right == frozenset((composition.identity,))
        for left, right in itertools.combinations(factors, 2)
    )

    algebra_cache = tuple(
        represented_algebra(composition, factor, dataset.carrier_dimension)
        for factor in factors
    )
    ambient_algebra = represented_algebra(composition, range(composition.size), dataset.carrier_dimension)
    algebra_dimensions = tuple(value.dimension for value in algebra_cache)
    algebra_intersections = all(
        algebra_intersection_dimension(left, right) == 1
        for left, right in itertools.combinations(algebra_cache, 2)
    )
    algebra_commutation = all(
        matrices_commute(composition.classes[a].law.to_matrix(), composition.classes[b].law.to_matrix())
        for left, right in itertools.combinations(factors, 2)
        for a in left
        for b in right
    )
    dimension_product = 1
    for value in algebra_dimensions:
        dimension_product *= value
    represented_product = algebra_intersections and algebra_commutation and dimension_product == ambient_algebra.dimension
    restriction_stable = False
    if collision is None:
        restriction_stable = _restriction_stable(composition, factors, inverses)
    return FactorCertificate(
        factors=factors,
        factor_orders=tuple(len(value) for value in factors),
        algebra_dimensions=algebra_dimensions,
        independently_generated=independently_generated,
        mixed_implemented_both_orders=mixed_implemented,
        operationally_commuting=operationally_commuting,
        faithful_multiplication=faithful,
        multiplication_collision=collision,
        closed_with_inverses=closed,
        typed_scalar_intersection=scalar_intersection,
        represented_algebra_product=represented_product,
        restriction_stable=restriction_stable,
    )


@dataclass(frozen=True)
class AddressabilityResult:
    composition: CompositionObject
    inverses: Tuple[int, ...]
    normal_subobjects: Tuple[Subobject, ...]
    certificates: Tuple[FactorCertificate, ...]
    finest_certificates: Tuple[FactorCertificate, ...]
    normal_join_tests: int
    factor_tuple_tests: int
    first_obstruction: Optional[str]

    @property
    def blocked_at_address(self) -> bool:
        return not self.finest_certificates


def certificate_sort_key(value: FactorCertificate) -> Tuple[object, ...]:
    return (
        len(value.factors),
        tuple(sorted(value.factor_orders)),
        tuple(tuple(sorted(factor)) for factor in value.factors),
    )


def analyze_addressability(dataset: OperationalDataset) -> AddressabilityResult:
    composition = build_composition_object(dataset)
    if not composition.total_implemented:
        obstruction = "declared COLLAPSED status" if composition.row_audit.collapsed_rows else "unavailable composition row"
        return AddressabilityResult(composition, (), (), (), (), 0, 0, obstruction)
    if composition.identity is None:
        return AddressabilityResult(composition, (), (), (), (), 0, 0, "no unique identity")
    if not composition.associative:
        return AddressabilityResult(composition, (), (), (), (), 0, 0, "nonassociative quotient composition")
    try:
        inverses = inverse_table(composition)
    except AccessUnderdetermined as error:
        return AddressabilityResult(composition, (), (), (), (), 0, 0, str(error))
    normals, join_tests = enumerate_normal_subobjects(composition, inverses)
    identity_subobject = frozenset((composition.identity,))
    proper = tuple(value for value in normals if value != identity_subobject and len(value) != composition.size)

    direct_pool = set()
    factor_tests = 0
    for index, left in enumerate(proper):
        for right in proper[index + 1:]:
            if len(left) * len(right) != composition.size:
                continue
            factor_tests += 1
            if join_tests + factor_tests > MAX_CANDIDATE_TESTS:
                raise InvalidInput("direct-complement search exceeded the frozen cap")
            if left & right != identity_subobject:
                continue
            if not subobjects_commute(composition, left, right):
                continue
            image, collision = multiplication_image(composition, (left, right))
            if collision is None and len(image) == composition.size:
                direct_pool.add(left)
                direct_pool.add(right)

    pool = tuple(sorted(direct_pool, key=lambda item: (len(item), tuple(sorted(item)))))
    certificates = []
    for count in range(2, min(8, len(pool)) + 1):
        for factors in itertools.combinations(pool, count):
            order_product = 1
            for factor in factors:
                order_product *= len(factor)
            if order_product != composition.size:
                continue
            factor_tests += 1
            if join_tests + factor_tests > MAX_CANDIDATE_TESTS:
                raise InvalidInput("factor-tuple search exceeded the frozen cap")
            certificate = certify_factor_tuple(dataset, composition, factors, inverses)
            if certificate.passes:
                certificates.append(certificate)
    certificates = sorted(set(certificates), key=certificate_sort_key)
    maximum = max((len(value.factors) for value in certificates), default=0)
    finest = tuple(value for value in certificates if len(value.factors) == maximum)

    obstruction = None
    if not finest:
        selectable = frozenset(
            value.index for value in composition.classes if value.independently_selectable
        )
        if selectable != frozenset(range(composition.size)):
            obstruction = "no complete factor tuple is independently generated"
        else:
            obstruction = "no sound normal direct-factor tuple"
    for certificate in finest:
        replay = certify_factor_tuple(dataset, composition, certificate.factors, inverses)
        if replay != certificate or not replay.passes:
            raise AssertionError("returned factor certificate failed exact replay")
    return AddressabilityResult(
        composition=composition,
        inverses=inverses,
        normal_subobjects=normals,
        certificates=tuple(certificates),
        finest_certificates=finest,
        normal_join_tests=join_tests,
        factor_tuple_tests=factor_tests,
        first_obstruction=obstruction,
    )


# ---------------------------------------------------------------------------
# Exact W3 records, regional restrictions, and factual interfaces
# ---------------------------------------------------------------------------


def _rank_one_projector(state: Vector) -> Matrix:
    return tuple(
        tuple(left * right.conjugate() for right in state)
        for left in state
    )


def fourier_record_witness(levels: int, handle: str) -> RecordWitness:
    """Fresh exact n-level write/preserve/erase seam for n in {2,3,4}."""

    if levels == 2:
        normalizer = INV_SQRT2
    elif levels == 3:
        normalizer = SQRT3 * Fraction(1, 3)
    elif levels == 4:
        normalizer = Q24(Fraction(1, 2))
    else:
        raise InvalidInput("public exact Fourier record supports 2, 3, or 4 levels")
    phase_step = 24 // levels
    fourier = tuple(
        tuple(normalizer * (ZETA ** ((phase_step * row * column) % 24)) for column in range(levels))
        for row in range(levels)
    )
    alternatives = tuple(
        _rank_one_projector(tuple(fourier[row][column] for row in range(levels)))
        for column in range(levels)
    )
    computational = tuple(
        tuple(
            tuple(Q24(1 if row == column == atom else 0) for column in range(levels))
            for row in range(levels)
        )
        for atom in range(levels)
    )
    write = adjoint(fourier)
    return RecordWitness(
        handle=handle,
        preparations=(basis_vector(levels, 0),),
        alternative_projectors=alternatives,
        cut_record_projectors=computational,
        availability_probes=computational,
        write=write,
        preserving=(identity(levels),),
        erasing=(fourier,),
        no_write=identity(levels),
    )


@dataclass(frozen=True)
class ResolvedRecord:
    structural_id: str
    support: Subobject
    projector_resolution: Tuple[FrozenSet[int], ...]
    levels: int
    passes_w3: bool
    occurrence: bool
    preserving_available: Tuple[bool, ...]
    erasing_available: Tuple[bool, ...]
    erasing_cross_coherence: Tuple[int, ...]
    no_write_occurrence: bool


def resolve_records(
    dataset: OperationalDataset,
    composition: CompositionObject,
    inverses: Sequence[int],
) -> Tuple[Tuple[ResolvedRecord, ...], Mapping[str, ResolvedRecord]]:
    resolved = []
    by_handle: Dict[str, ResolvedRecord] = {}
    for candidate in dataset.records:
        local_dimension = len(candidate.witness.write)
        result = evaluate_record_witness(candidate.witness, identity(local_dimension), local_dimension)
        support = subgroup_generated(
            composition,
            (composition.class_for_handle(handle) for handle in candidate.access_operations),
            inverses,
        )
        structural_id = stable_hash(
            {
                "record_structure": candidate.structural_key(),
                "support": sorted(support),
            }
        )
        value = ResolvedRecord(
            structural_id=structural_id,
            support=support,
            projector_resolution=candidate.ambient_projector_resolution,
            levels=len(candidate.ambient_projector_resolution),
            passes_w3=result.passes_w3,
            occurrence=result.occurrence,
            preserving_available=result.preserving_available,
            erasing_available=result.erasing_available,
            erasing_cross_coherence=result.erasing_cross_coherence,
            no_write_occurrence=result.no_write_occurrence,
        )
        resolved.append(value)
        by_handle[candidate.handle] = value
    return tuple(sorted(set(resolved), key=lambda item: item.structural_id)), by_handle


@dataclass(frozen=True)
class ContextView:
    structural_id: str
    atoms: Tuple[int, ...]
    operations: Subobject
    preparations: FrozenSet[str]
    probes: FrozenSet[str]
    readouts: FrozenSet[str]
    records: FrozenSet[str]
    gauges: FrozenSet[str]


@dataclass(frozen=True)
class RegionalObject:
    structural_id: str
    atoms: Tuple[int, ...]
    operations: Subobject
    row_pairs: Tuple[Tuple[int, int], ...]
    selectability: Tuple[Tuple[int, bool], ...]
    preparations: FrozenSet[str]
    context_key: str
    probes: FrozenSet[str]
    readouts: FrozenSet[str]
    records: FrozenSet[str]
    gauges: FrozenSet[str]


@dataclass(frozen=True)
class RegionalArrow:
    source: str
    target: str
    operation_map: Tuple[Tuple[int, int], ...]
    row_map: Tuple[
        Tuple[int, int, int, int, str, str, Optional[MonomialLaw], Optional[MonomialLaw]],
        ...,
    ]
    selectability_map: Tuple[Tuple[int, int, bool, bool], ...]
    preparation_lift: Tuple[Tuple[str, str], ...]
    context_map: Tuple[str, str]
    probe_lift: Tuple[Tuple[str, str], ...]
    readout_lift: Tuple[Tuple[str, str], ...]
    record_lift: Tuple[Tuple[str, str], ...]
    gauge_lift: Tuple[Tuple[str, str], ...]


@dataclass(frozen=True)
class FactInterface:
    region: str
    record_ids: Tuple[str, ...]
    atoms: Tuple[FrozenSet[int], ...]
    generator_projectors: Tuple[Tuple[str, Tuple[FrozenSet[int], ...]], ...]


@dataclass(frozen=True)
class FactMap:
    regional_source: str
    regional_target: str
    fact_source: str
    fact_target: str
    record_generator_map: Tuple[
        Tuple[
            str,
            str,
            Tuple[FrozenSet[int], ...],
            Tuple[FrozenSet[int], ...],
        ],
        ...,
    ]
    atom_images: Tuple[Tuple[int, Tuple[int, ...]], ...]
    projector_equalities: Tuple[Tuple[int, FrozenSet[int], FrozenSet[int]], ...]


@dataclass(frozen=True)
class RegionalAtlas:
    factorization: FactorCertificate
    contexts: Tuple[ContextView, ...]
    objects: Tuple[RegionalObject, ...]
    arrows: Tuple[RegionalArrow, ...]
    facts: Tuple[FactInterface, ...]
    fact_maps: Tuple[FactMap, ...]
    coherent_paths: int
    nonvacuous_triples: Tuple[Tuple[str, str, str, str], ...]
    universal_atoms: Tuple[int, ...]
    is_complete_proper_boolean: bool


def _key_maps(dataset: OperationalDataset) -> Tuple[Mapping[str, str], Mapping[str, str], Mapping[str, str], Mapping[str, str]]:
    preparations = {value.handle: stable_hash(value.scientific_key()) for value in dataset.preparations}
    probes = {value.handle: stable_hash(value.scientific_key()) for value in dataset.probes}
    readouts = {value.handle: stable_hash(value.scientific_key()) for value in dataset.readouts}
    gauges = {value.handle: stable_hash(value.scientific_key()) for value in dataset.gauge_actions}
    return preparations, probes, readouts, gauges


def factor_coordinates(
    composition: CompositionObject,
    factors: Sequence[Subobject],
) -> Tuple[Mapping[int, Tuple[int, ...]], Mapping[Tuple[int, ...], int]]:
    coordinate_to_element: Dict[Tuple[int, ...], int] = {}
    element_to_coordinate: Dict[int, Tuple[int, ...]] = {}
    for entries in itertools.product(*(tuple(sorted(value)) for value in factors)):
        result = multiply_tuple(composition, entries)
        if result in element_to_coordinate:
            raise AccessUnderdetermined("factor coordinates are not faithful")
        element_to_coordinate[result] = entries
        coordinate_to_element[entries] = result
    if len(element_to_coordinate) != composition.size:
        raise AccessUnderdetermined("factor coordinates do not cover the composition object")
    return element_to_coordinate, coordinate_to_element


def product_for_atom_indices(
    composition: CompositionObject,
    factorization: FactorCertificate,
    atoms: Iterable[int],
) -> Subobject:
    atoms = tuple(sorted(set(atoms)))
    if not atoms:
        if composition.identity is None:
            raise AccessUnderdetermined("empty product requires identity")
        return frozenset((composition.identity,))
    return product_subobject(composition, tuple(factorization.factors[index] for index in atoms))


def _resolve_contexts(
    dataset: OperationalDataset,
    address: AddressabilityResult,
    factorization: FactorCertificate,
    records_by_handle: Mapping[str, ResolvedRecord],
) -> Tuple[ContextView, ...]:
    composition = address.composition
    prep_keys, probe_keys, readout_keys, gauge_keys = _key_maps(dataset)
    possible: Dict[Subobject, Tuple[int, ...]] = {}
    for count in range(1, len(factorization.factors)):
        for atoms in itertools.combinations(range(len(factorization.factors)), count):
            subobject = product_for_atom_indices(composition, factorization, atoms)
            if subobject in possible and possible[subobject] != atoms:
                raise AccessUnderdetermined("factor products do not give unique context scopes")
            possible[subobject] = atoms
    views = []
    for context in dataset.contexts:
        if context.boundary_type == "":
            raise InvalidInput("context boundary type is empty")
        generated = subgroup_generated(
            composition,
            (composition.class_for_handle(handle) for handle in context.operation_handles),
            address.inverses,
        )
        if generated not in possible:
            raise InvalidInput("access context is not a proper returned-factor product")
        try:
            preparations = frozenset(prep_keys[handle] for handle in context.preparation_handles)
            probes = frozenset(probe_keys[handle] for handle in context.probe_handles)
            readouts = frozenset(readout_keys[handle] for handle in context.readout_handles)
            record_ids = frozenset(records_by_handle[handle].structural_id for handle in context.record_handles)
            gauges = frozenset(gauge_keys[handle] for handle in context.gauge_handles)
        except KeyError as error:
            raise InvalidInput(f"context field reference is unknown: {error}") from error
        if any(not records_by_handle[handle].support <= generated for handle in context.record_handles):
            raise InvalidInput("context exposes a record outside its operation scope")
        payload = {
            "atoms": list(possible[generated]),
            "operations": sorted(generated),
            "preparations": sorted(preparations),
            "probes": sorted(probes),
            "readouts": sorted(readouts),
            "records": sorted(record_ids),
            "gauges": sorted(gauges),
        }
        views.append(
            ContextView(
                structural_id=stable_hash(payload),
                atoms=possible[generated],
                operations=generated,
                preparations=preparations,
                probes=probes,
                readouts=readouts,
                records=record_ids,
                gauges=gauges,
            )
        )
    if len({value.structural_id for value in views}) != len(views):
        raise InvalidInput("duplicate operational access contexts")
    return tuple(sorted(views, key=lambda item: (len(item.atoms), item.atoms, item.structural_id)))


def _meet_contexts(contexts: Sequence[ContextView]) -> Tuple[RegionalObject, ...]:
    by_atoms: Dict[Tuple[int, ...], Tuple[FrozenSet[str], FrozenSet[str], FrozenSet[str], FrozenSet[str], FrozenSet[str]]] = {}
    operations_by_atoms: Dict[Tuple[int, ...], Subobject] = {}
    for count in range(1, len(contexts) + 1):
        for chosen in itertools.combinations(contexts, count):
            atoms = tuple(sorted(set.intersection(*(set(value.atoms) for value in chosen))))
            if not atoms:
                continue
            fields = (
                frozenset.intersection(*(value.preparations for value in chosen)),
                frozenset.intersection(*(value.probes for value in chosen)),
                frozenset.intersection(*(value.readouts for value in chosen)),
                frozenset.intersection(*(value.records for value in chosen)),
                frozenset.intersection(*(value.gauges for value in chosen)),
            )
            operations = frozenset.intersection(*(value.operations for value in chosen))
            if atoms in by_atoms and by_atoms[atoms] != fields:
                raise AccessUnderdetermined("context meets give path-dependent field restrictions")
            if atoms in operations_by_atoms and operations_by_atoms[atoms] != operations:
                raise AccessUnderdetermined("context meets give path-dependent operation restrictions")
            by_atoms[atoms] = fields
            operations_by_atoms[atoms] = operations
    objects = []
    for atoms in sorted(by_atoms, key=lambda value: (len(value), value)):
        preparations, probes, readouts, records, gauges = by_atoms[atoms]
        operations = operations_by_atoms[atoms]
        context_key = stable_hash(
            {
                "operations": sorted(operations),
                "preparations": sorted(preparations),
                "probes": sorted(probes),
                "readouts": sorted(readouts),
                "records": sorted(records),
                "gauges": sorted(gauges),
            }
        )
        structural_id = stable_hash({"context": context_key, "atoms": list(atoms)})
        objects.append(
            RegionalObject(
                structural_id=structural_id,
                atoms=atoms,
                operations=operations,
                row_pairs=tuple((left, right) for left in sorted(operations) for right in sorted(operations)),
                selectability=(),
                preparations=preparations,
                context_key=context_key,
                probes=probes,
                readouts=readouts,
                records=records,
                gauges=gauges,
            )
        )
    return tuple(objects)


def _complete_regional_objects(
    objects: Sequence[RegionalObject],
    composition: CompositionObject,
    resolved_records: Mapping[str, ResolvedRecord],
) -> Tuple[RegionalObject, ...]:
    result = []
    for value in objects:
        expected_rows = tuple((left, right) for left in sorted(value.operations) for right in sorted(value.operations))
        if value.row_pairs != expected_rows:
            raise InvalidInput("regional row table is incomplete")
        for left, right in expected_rows:
            row = composition.row(left, right)
            if row.status != IMPLEMENTED or row.result not in value.operations or row.law is None:
                raise InvalidInput("regional subinstrument is not restriction-stable")
        if not value.records:
            raise InvalidInput("positive regional object has no record interface")
        if any(not resolved_records[key].passes_w3 for key in value.records):
            raise InvalidInput("regional object contains a non-W3 record")
        result.append(
            RegionalObject(
                structural_id=value.structural_id,
                atoms=value.atoms,
                operations=value.operations,
                row_pairs=value.row_pairs,
                selectability=tuple((index, composition.classes[index].independently_selectable) for index in sorted(value.operations)),
                preparations=value.preparations,
                context_key=value.context_key,
                probes=value.probes,
                readouts=value.readouts,
                records=value.records,
                gauges=value.gauges,
            )
        )
    return tuple(result)


def _project_operation(
    operation: int,
    source_atoms: Sequence[int],
    target_atoms: Sequence[int],
    composition: CompositionObject,
    factors: Sequence[Subobject],
    element_to_coordinate: Mapping[int, Tuple[int, ...]],
    coordinate_to_element: Mapping[Tuple[int, ...], int],
) -> int:
    if composition.identity is None:
        raise AccessUnderdetermined("regional projection requires identity")
    coordinates = list(element_to_coordinate[operation])
    for atom in source_atoms:
        if atom not in target_atoms:
            coordinates[atom] = composition.identity
    return coordinate_to_element[tuple(coordinates)]


def build_regional_arrow(
    source: RegionalObject,
    target: RegionalObject,
    composition: CompositionObject,
    factors: Sequence[Subobject],
    element_to_coordinate: Mapping[int, Tuple[int, ...]],
    coordinate_to_element: Mapping[Tuple[int, ...], int],
) -> RegionalArrow:
    if not set(target.atoms) <= set(source.atoms):
        raise InvalidInput("regional arrow is not a restriction")
    operation_map = tuple(
        (
            operation,
            _project_operation(
                operation,
                source.atoms,
                target.atoms,
                composition,
                factors,
                element_to_coordinate,
                coordinate_to_element,
            ),
        )
        for operation in sorted(source.operations)
    )
    operation_dict = dict(operation_map)
    if any(value not in target.operations for value in operation_dict.values()):
        raise InvalidInput("regional operation projection leaves target")
    row_map = []
    for left, right in source.row_pairs:
        target_left = operation_dict[left]
        target_right = operation_dict[right]
        source_row = composition.row(left, right)
        target_row = composition.row(target_left, target_right)
        if source_row.status != IMPLEMENTED or target_row.status != IMPLEMENTED:
            raise InvalidInput("regional row projection is not implemented")
        if operation_dict[source_row.result] != target_row.result:
            raise InvalidInput("regional row result square does not commute")
        row_map.append(
            (
                left,
                right,
                target_left,
                target_right,
                source_row.status,
                target_row.status,
                source_row.law,
                target_row.law,
            )
        )
    selectability_map = tuple(
        (
            operation,
            operation_dict[operation],
            composition.classes[operation].independently_selectable,
            composition.classes[operation_dict[operation]].independently_selectable,
        )
        for operation in sorted(source.operations)
    )
    if any(source_flag and not target_flag for _, _, source_flag, target_flag in selectability_map):
        raise InvalidInput("regional restriction destroys independent selectability")

    def lift(target_values: FrozenSet[str], source_values: FrozenSet[str], label: str) -> Tuple[Tuple[str, str], ...]:
        if not target_values <= source_values:
            raise InvalidInput(f"regional {label} pullback is missing")
        return tuple((value, value) for value in sorted(target_values))

    return RegionalArrow(
        source=source.structural_id,
        target=target.structural_id,
        operation_map=operation_map,
        row_map=tuple(row_map),
        selectability_map=selectability_map,
        preparation_lift=lift(target.preparations, source.preparations, "preparation"),
        context_map=(source.context_key, target.context_key),
        probe_lift=lift(target.probes, source.probes, "probe"),
        readout_lift=lift(target.readouts, source.readouts, "readout"),
        record_lift=lift(target.records, source.records, "record"),
        gauge_lift=lift(target.gauges, source.gauges, "gauge"),
    )


def _compose_simple_map(first: Sequence[Tuple[int, int]], second: Sequence[Tuple[int, int]]) -> Tuple[Tuple[int, int], ...]:
    first_map = dict(first)
    second_map = dict(second)
    return tuple(sorted((source, second_map[middle]) for source, middle in first_map.items()))


def regional_arrow_composes(
    source_to_middle: RegionalArrow,
    middle_to_target: RegionalArrow,
    direct: RegionalArrow,
) -> bool:
    if source_to_middle.target != middle_to_target.source:
        return False
    if source_to_middle.source != direct.source or middle_to_target.target != direct.target:
        return False
    if _compose_simple_map(source_to_middle.operation_map, middle_to_target.operation_map) != direct.operation_map:
        return False
    first_rows = {
        (left, right): (target_left, target_right, source_status, target_status, source_law, target_law)
        for left, right, target_left, target_right, source_status, target_status, source_law, target_law
        in source_to_middle.row_map
    }
    second_rows = {
        (left, right): (target_left, target_right, source_status, target_status, source_law, target_law)
        for left, right, target_left, target_right, source_status, target_status, source_law, target_law
        in middle_to_target.row_map
    }
    direct_rows = {
        (left, right): (target_left, target_right, source_status, target_status, source_law, target_law)
        for left, right, target_left, target_right, source_status, target_status, source_law, target_law
        in direct.row_map
    }
    composed_rows = {}
    for key, (middle_left, middle_right, source_status, middle_status, source_law, middle_law) in first_rows.items():
        if (middle_left, middle_right) not in second_rows:
            return False
        target_left, target_right, second_source_status, target_status, second_source_law, target_law = second_rows[(middle_left, middle_right)]
        if middle_status != second_source_status or middle_law != second_source_law:
            return False
        composed_rows[key] = (
            target_left,
            target_right,
            source_status,
            target_status,
            source_law,
            target_law,
        )
    if composed_rows != direct_rows:
        return False
    first_selectability = {
        source: (middle, source_flag, middle_flag)
        for source, middle, source_flag, middle_flag in source_to_middle.selectability_map
    }
    second_selectability = {
        middle: (target, middle_flag, target_flag)
        for middle, target, middle_flag, target_flag in middle_to_target.selectability_map
    }
    direct_selectability = {
        source: (target, source_flag, target_flag)
        for source, target, source_flag, target_flag in direct.selectability_map
    }
    composed_selectability = {}
    for source, (middle, source_flag, middle_flag) in first_selectability.items():
        if middle not in second_selectability:
            return False
        target, second_middle_flag, target_flag = second_selectability[middle]
        if middle_flag != second_middle_flag:
            return False
        composed_selectability[source] = (target, source_flag, target_flag)
    if composed_selectability != direct_selectability:
        return False
    for field in ("preparation_lift", "probe_lift", "readout_lift", "record_lift", "gauge_lift"):
        first = dict(getattr(source_to_middle, field))
        second = dict(getattr(middle_to_target, field))
        direct_field = dict(getattr(direct, field))
        composed = {key: first[value] for key, value in second.items()}
        if composed != direct_field:
            return False
    return (
        source_to_middle.context_map[0] == direct.context_map[0]
        and source_to_middle.context_map[1] == middle_to_target.context_map[0]
        and middle_to_target.context_map[1] == direct.context_map[1]
    )


def build_fact_interface(
    region: RegionalObject,
    record_map: Mapping[str, ResolvedRecord],
    carrier_dimension: int,
) -> FactInterface:
    records = tuple(sorted(region.records))
    universe = frozenset(range(carrier_dimension))
    atoms = (universe,)
    generators = []
    for record_id in records:
        resolution = record_map[record_id].projector_resolution
        generators.append((record_id, resolution))
        refined = []
        for current in atoms:
            for projector in resolution:
                intersection = current & projector
                if intersection:
                    refined.append(intersection)
        atoms = tuple(sorted(set(refined), key=lambda item: (min(item), len(item), tuple(sorted(item)))))
    if frozenset().union(*atoms) != universe or any(left & right for left, right in itertools.combinations(atoms, 2)):
        raise InvalidInput("fact-interface atoms do not partition the carrier")
    return FactInterface(
        region=region.structural_id,
        record_ids=records,
        atoms=atoms,
        generator_projectors=tuple(generators),
    )


def build_fact_map(
    regional_arrow: RegionalArrow,
    fact_source: FactInterface,
    fact_target: FactInterface,
) -> FactMap:
    if regional_arrow.source != fact_source.region or regional_arrow.target != fact_target.region:
        raise InvalidInput("fact map has the wrong regional source/target")
    if not set(fact_target.record_ids) <= set(fact_source.record_ids):
        raise InvalidInput("fact restriction loses a target record")
    source_generators = dict(fact_source.generator_projectors)
    target_generators = dict(fact_target.generator_projectors)
    generator_map = []
    for record_id, target_resolution in sorted(target_generators.items()):
        if record_id not in source_generators:
            raise InvalidInput("fact generator has no source lift")
        source_resolution = source_generators[record_id]
        if source_resolution != target_resolution:
            raise InvalidInput("fact generator projector pullback is not exact")
        generator_map.append((record_id, record_id, target_resolution, source_resolution))
    images = []
    equalities = []
    for target_index, target_atom in enumerate(fact_target.atoms):
        source_indices = tuple(
            index for index, source_atom in enumerate(fact_source.atoms)
            if source_atom <= target_atom
        )
        if not source_indices:
            raise InvalidInput("fact atom has empty projector lift")
        lifted = frozenset().union(*(fact_source.atoms[index] for index in source_indices))
        if lifted != target_atom:
            raise InvalidInput("fact projector lift is not exact")
        images.append((target_index, source_indices))
        equalities.append((target_index, target_atom, lifted))
    used = tuple(index for _, values in images for index in values)
    if sorted(used) != list(range(len(fact_source.atoms))):
        raise InvalidInput("fact atom map is not a Boolean partition homomorphism")
    return FactMap(
        regional_source=regional_arrow.source,
        regional_target=regional_arrow.target,
        fact_source=fact_source.region,
        fact_target=fact_target.region,
        record_generator_map=tuple(generator_map),
        atom_images=tuple(images),
        projector_equalities=tuple(equalities),
    )


def fact_map_composes(source_to_middle: FactMap, middle_to_target: FactMap, direct: FactMap) -> bool:
    if source_to_middle.fact_target != middle_to_target.fact_source:
        return False
    first_generators = {target: source for target, source, _, _ in source_to_middle.record_generator_map}
    second_generators = {target: source for target, source, _, _ in middle_to_target.record_generator_map}
    direct_generators = {target: source for target, source, _, _ in direct.record_generator_map}
    if {target: first_generators[middle] for target, middle in second_generators.items()} != direct_generators:
        return False
    first = dict(source_to_middle.atom_images)
    second = dict(middle_to_target.atom_images)
    composed = tuple(
        (
            target_atom,
            tuple(sorted(index for middle_atom in middle_atoms for index in first[middle_atom])),
        )
        for target_atom, middle_atoms in second.items()
    )
    return composed == direct.atom_images


def build_regional_atlas(
    dataset: OperationalDataset,
    address: AddressabilityResult,
    factorization: FactorCertificate,
) -> RegionalAtlas:
    if factorization not in address.finest_certificates:
        raise InvalidInput("atlas requested for a non-finest factorization")
    resolved_records, records_by_handle = resolve_records(dataset, address.composition, address.inverses)
    record_by_id = {value.structural_id: value for value in resolved_records}
    contexts = _resolve_contexts(dataset, address, factorization, records_by_handle)
    raw_objects = _meet_contexts(contexts)
    objects = _complete_regional_objects(raw_objects, address.composition, record_by_id)
    object_by_id = {value.structural_id: value for value in objects}
    element_to_coordinate, coordinate_to_element = factor_coordinates(address.composition, factorization.factors)
    arrows = []
    for source in objects:
        for target in objects:
            if set(target.atoms) <= set(source.atoms):
                arrows.append(
                    build_regional_arrow(
                        source,
                        target,
                        address.composition,
                        factorization.factors,
                        element_to_coordinate,
                        coordinate_to_element,
                    )
                )
    arrows = tuple(sorted(arrows, key=lambda item: (item.source, item.target)))
    arrow_by_pair = {(value.source, value.target): value for value in arrows}
    coherent_paths = 0
    for source in objects:
        for middle in objects:
            for target in objects:
                if set(target.atoms) <= set(middle.atoms) <= set(source.atoms):
                    if not regional_arrow_composes(
                        arrow_by_pair[(source.structural_id, middle.structural_id)],
                        arrow_by_pair[(middle.structural_id, target.structural_id)],
                        arrow_by_pair[(source.structural_id, target.structural_id)],
                    ):
                        raise InvalidInput("RegAddr direct/composite diagram fails")
                    coherent_paths += 1

    facts = tuple(build_fact_interface(value, record_by_id, dataset.carrier_dimension) for value in objects)
    fact_by_region = {value.region: value for value in facts}
    fact_maps = tuple(
        build_fact_map(value, fact_by_region[value.source], fact_by_region[value.target])
        for value in arrows
    )
    fact_map_by_pair = {(value.regional_source, value.regional_target): value for value in fact_maps}
    for source in objects:
        for middle in objects:
            for target in objects:
                if set(target.atoms) <= set(middle.atoms) <= set(source.atoms):
                    if not fact_map_composes(
                        fact_map_by_pair[(source.structural_id, middle.structural_id)],
                        fact_map_by_pair[(middle.structural_id, target.structural_id)],
                        fact_map_by_pair[(source.structural_id, target.structural_id)],
                    ):
                        raise InvalidInput("Rec direct/composite naturality fails")

    nonvacuous_triples = []
    maximal = tuple(contexts)
    for left, middle, right in itertools.combinations(maximal, 3):
        atoms = tuple(sorted(set(left.atoms) & set(middle.atoms) & set(right.atoms)))
        if not atoms:
            continue
        matches = tuple(value for value in objects if value.atoms == atoms)
        if len(matches) == 1 and matches[0].records:
            nonvacuous_triples.append((left.structural_id, middle.structural_id, right.structural_id, matches[0].structural_id))
    universal = tuple(sorted(set.intersection(*(set(value.atoms) for value in maximal)))) if maximal else ()
    all_proper = {
        tuple(atoms)
        for count in range(1, len(factorization.factors))
        for atoms in itertools.combinations(range(len(factorization.factors)), count)
    }
    observed = {value.atoms for value in objects}
    return RegionalAtlas(
        factorization=factorization,
        contexts=contexts,
        objects=objects,
        arrows=arrows,
        facts=facts,
        fact_maps=fact_maps,
        coherent_paths=coherent_paths,
        nonvacuous_triples=tuple(nonvacuous_triples),
        universal_atoms=universal,
        is_complete_proper_boolean=observed == all_proper,
    )


@dataclass(frozen=True)
class TwistedTripleResult:
    regional_pair_maps_valid: Tuple[bool, bool, bool]
    record_pair_maps_valid: Tuple[bool, bool, bool]
    regional_loop_commutes: bool
    loop_commutes: bool
    rejected_at_triple_gate: bool


@dataclass(frozen=True)
class TypedPresentationIsomorphism:
    source: str
    target: str
    operation_map: Tuple[Tuple[str, str], ...]
    row_map: Tuple[Tuple[Tuple[str, str], Tuple[str, str]], ...]
    selectability_map: Tuple[Tuple[str, str, bool, bool], ...]
    preparation_map: Tuple[Tuple[str, str], ...]
    context_map: Tuple[Tuple[str, str], ...]
    probe_map: Tuple[Tuple[str, str], ...]
    readout_map: Tuple[Tuple[str, str], ...]
    record_map: Tuple[Tuple[str, str], ...]
    gauge_map: Tuple[Tuple[str, str], ...]
    carrier_action: MonomialLaw
    fact_atom_permutation: Tuple[int, int]


def _typed_pair_isomorphism_valid(value: TypedPresentationIsomorphism) -> Tuple[bool, bool]:
    expected_singletons = (
        value.operation_map,
        value.row_map,
        value.selectability_map,
        value.preparation_map,
        value.context_map,
        value.probe_map,
        value.readout_map,
        value.record_map,
        value.gauge_map,
    )
    regional = all(len(field) == 1 for field in expected_singletons)
    regional = regional and value.selectability_map[0][2:] == (True, True)
    regional = regional and value.carrier_action.dimension == 2
    record = tuple(sorted(value.fact_atom_permutation)) == (0, 1)
    p0 = frozenset((0,))
    p1 = frozenset((1,))
    projectors = (p0, p1)
    carried = tuple(
        frozenset(value.carrier_action.permutation[index] for index in atom)
        for atom in projectors
    )
    record = record and all(
        carried[source] == projectors[target]
        for source, target in enumerate(value.fact_atom_permutation)
    )
    return regional, record


def pairwise_valid_twisted_triple() -> TwistedTripleResult:
    """All pair maps are typed isomorphisms; only their triple loop fails."""

    unit = MonomialLaw.unit(2)
    swap = permutation_law((1, 0))

    def pair(source: int, target: int, action: MonomialLaw, atom_map: Tuple[int, int]) -> TypedPresentationIsomorphism:
        return TypedPresentationIsomorphism(
            source=f"presentation-{source}",
            target=f"presentation-{target}",
            operation_map=((f"op-{source}", f"op-{target}"),),
            row_map=(((f"op-{source}", f"op-{source}"), (f"op-{target}", f"op-{target}")),),
            selectability_map=((f"op-{source}", f"op-{target}", True, True),),
            preparation_map=((f"prep-{source}", f"prep-{target}"),),
            context_map=((f"ctx-{source}", f"ctx-{target}"),),
            probe_map=((f"probe-{source}", f"probe-{target}"),),
            readout_map=((f"read-{source}", f"read-{target}"),),
            record_map=((f"record-{source}", f"record-{target}"),),
            gauge_map=((f"gauge-{source}", f"gauge-{target}"),),
            carrier_action=action,
            fact_atom_permutation=atom_map,
        )

    phi_12 = pair(1, 2, unit, (0, 1))
    phi_23 = pair(2, 3, unit, (0, 1))
    phi_13 = pair(1, 3, swap, (1, 0))
    validity = tuple(_typed_pair_isomorphism_valid(value) for value in (phi_12, phi_23, phi_13))
    regional_pairs = tuple(value[0] for value in validity)
    record_pairs = tuple(value[1] for value in validity)
    composed_atoms = tuple(
        phi_23.fact_atom_permutation[phi_12.fact_atom_permutation[index]]
        for index in range(2)
    )
    fact_loop = composed_atoms == phi_13.fact_atom_permutation
    composed_action = phi_23.carrier_action.after(phi_12.carrier_action)
    regional_loop = composed_action == phi_13.carrier_action
    return TwistedTripleResult(
        regional_pair_maps_valid=regional_pairs,
        record_pair_maps_valid=record_pairs,
        regional_loop_commutes=regional_loop,
        loop_commutes=fact_loop,
        rejected_at_triple_gate=(
            all(regional_pairs)
            and all(record_pairs)
            and not regional_loop
            and not fact_loop
        ),
    )


# ---------------------------------------------------------------------------
# Public calibrations only (no future main-fixture truth)
# ---------------------------------------------------------------------------


def _left_regular_dataset(
    handle: str,
    elements: Sequence[object],
    multiply,
    selectable,
    records: Sequence[RecordCandidate] = (),
    contexts: Sequence[AccessContext] = (),
    preparations: Sequence[FieldDatum] = (),
    probes: Sequence[FieldDatum] = (),
    readouts: Sequence[ReadoutDatum] = (),
    gauges: Sequence[GaugeDatum] = (),
) -> OperationalDataset:
    elements = tuple(elements)
    index = {value: position for position, value in enumerate(elements)}
    if len(index) != len(elements):
        raise InvalidInput("public group calibration contains duplicate elements")
    laws = []
    for left in elements:
        permutation = tuple(index[multiply(left, right)] for right in elements)
        laws.append(permutation_law(permutation))
    operations = tuple(
        OperationClass(
            handle=f"u{position:03d}",
            source_type="q",
            target_type="q",
            law=laws[position],
            observed_signature=laws[position].signature(),
            independently_selectable=bool(selectable(value)),
        )
        for position, value in enumerate(elements)
    )
    rows = []
    for left_index, left in enumerate(elements):
        for right_index, right in enumerate(elements):
            result_index = index[multiply(left, right)]
            supplied_law = laws[result_index]
            rows.append(
                CompositionRow(
                    left=operations[left_index].handle,
                    right=operations[right_index].handle,
                    tau="q|q|q",
                    status=IMPLEMENTED,
                    result_class=operations[result_index].handle,
                    law=supplied_law,
                    observed_signature=supplied_law.signature(),
                )
            )
    return OperationalDataset(
        handle=handle,
        carrier_dimension=len(elements),
        operations=operations,
        composition_rows=tuple(rows),
        preparations=tuple(preparations),
        contexts=tuple(contexts),
        probes=tuple(probes),
        readouts=tuple(readouts),
        records=tuple(records),
        gauge_actions=tuple(gauges),
    )


def _permute3(left: Tuple[int, int, int], right: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return tuple(left[right[index]] for index in range(3))


def _public_three_letter_group() -> Tuple[Tuple[int, int, int], ...]:
    return tuple(itertools.permutations(range(3)))


def public_selectability_pair(composite_only_coset: bool) -> OperationalDataset:
    permutations = _public_three_letter_group()
    elements = tuple((value, bit) for value in permutations for bit in range(2))

    def multiply(left, right):
        return _permute3(left[0], right[0]), left[1] ^ right[1]

    return _left_regular_dataset(
        "public-selectability-negative" if composite_only_coset else "public-selectability-positive",
        elements,
        multiply,
        (lambda value: value[1] == 0) if composite_only_coset else (lambda _value: True),
    )


def public_v4_dataset(with_records: bool = True) -> OperationalDataset:
    elements = tuple((left, right) for left in range(2) for right in range(2))

    def multiply(left, right):
        return left[0] ^ right[0], left[1] ^ right[1]

    records = []
    if with_records:
        element_index = {value: index for index, value in enumerate(elements)}
        identity_element = (0, 0)
        for ordinal, generator in enumerate(value for value in elements if value != identity_element):
            subgroup = frozenset((element_index[identity_element], element_index[generator]))
            complement = frozenset(set(range(4)) - set(subgroup))
            records.append(
                RecordCandidate(
                    handle=f"public-fact-{ordinal}",
                    boundary_type="q",
                    access_operations=(f"u{element_index[identity_element]:03d}", f"u{element_index[generator]:03d}"),
                    witness=fourier_record_witness(2, f"presentation-record-{ordinal}"),
                    ambient_projector_resolution=(subgroup, complement),
                )
            )
    return _left_regular_dataset(
        "public-record-bearing-v4",
        elements,
        multiply,
        lambda _value: True,
        records=records,
    )


def _replace_row(dataset: OperationalDataset, row_index: int, row: CompositionRow) -> OperationalDataset:
    rows = list(dataset.composition_rows)
    rows[row_index] = row
    return OperationalDataset(
        handle=dataset.handle,
        carrier_dimension=dataset.carrier_dimension,
        operations=dataset.operations,
        composition_rows=tuple(rows),
        preparations=dataset.preparations,
        contexts=dataset.contexts,
        probes=dataset.probes,
        readouts=dataset.readouts,
        records=dataset.records,
        gauge_actions=dataset.gauge_actions,
        access_postulate=dataset.access_postulate,
    )


def public_declared_collapse_dataset() -> OperationalDataset:
    base = public_v4_dataset(with_records=False)
    row_index = next(
        index
        for index, row in enumerate(base.composition_rows)
        if row.left != "u000" and row.right != "u000"
    )
    old = base.composition_rows[row_index]
    return _replace_row(
        base,
        row_index,
        CompositionRow(old.left, old.right, old.tau, COLLAPSED, old.result_class, old.law, old.observed_signature),
    )


def public_unavailable_dataset() -> OperationalDataset:
    base = public_v4_dataset(with_records=False)
    row_index = next(
        index
        for index, row in enumerate(base.composition_rows)
        if row.left != "u000" and row.right != "u000"
    )
    old = base.composition_rows[row_index]
    return _replace_row(
        base,
        row_index,
        CompositionRow(old.left, old.right, old.tau, UNAVAILABLE, None, None, None),
    )


def public_regional_calibration_dataset() -> OperationalDataset:
    """Public C2 x C3 x C5 map/record calibration; never a main score."""

    elements = tuple(
        (left, middle, right)
        for left in range(2)
        for middle in range(3)
        for right in range(5)
    )

    def multiply(left, right):
        return (
            (left[0] + right[0]) % 2,
            (left[1] + right[1]) % 3,
            (left[2] + right[2]) % 5,
        )

    element_index = {value: index for index, value in enumerate(elements)}
    atom_subgroups = (
        tuple(value for value in elements if value[1] == 0 and value[2] == 0),
        tuple(value for value in elements if value[0] == 0 and value[2] == 0),
        tuple(value for value in elements if value[0] == 0 and value[1] == 0),
    )
    records = []
    preparations = []
    probes = []
    readouts = []
    gauges = []
    for atom in range(3):
        zero_sector = frozenset(
            index for index, value in enumerate(elements) if value[atom] == 0
        )
        nonzero_sector = frozenset(range(len(elements))) - zero_sector
        records.append(
            RecordCandidate(
                handle=f"public-regional-record-{atom}",
                boundary_type="q",
                access_operations=tuple(f"u{element_index[value]:03d}" for value in atom_subgroups[atom]),
                witness=fourier_record_witness(2, f"public-regional-witness-{atom}"),
                ambient_projector_resolution=(zero_sector, nonzero_sector),
            )
        )
        preparations.append(FieldDatum(f"public-preparation-{atom}", "q", (atom, 11)))
        probes.append(FieldDatum(f"public-probe-{atom}", "q", (atom, 17)))
        readouts.append(ReadoutDatum(f"public-readout-{atom}", "q", (zero_sector, nonzero_sector)))
        phases = tuple((atom * index) % 24 for index in range(len(elements)))
        gauges.append(GaugeDatum(f"public-gauge-{atom}", MonomialLaw(tuple(range(len(elements))), phases)))

    context_atom_sets = ((0, 1), (0, 2), (0,))
    contexts = []
    for ordinal, atom_set in enumerate(context_atom_sets):
        operations = tuple(
            value
            for value in elements
            if all(value[index] == 0 for index in range(3) if index not in atom_set)
        )
        contexts.append(
            AccessContext(
                handle=f"public-context-{ordinal}",
                boundary_type="q",
                operation_handles=tuple(f"u{element_index[value]:03d}" for value in operations),
                preparation_handles=tuple(f"public-preparation-{atom}" for atom in atom_set),
                probe_handles=tuple(f"public-probe-{atom}" for atom in atom_set),
                readout_handles=tuple(f"public-readout-{atom}" for atom in atom_set),
                record_handles=tuple(f"public-regional-record-{atom}" for atom in atom_set),
                gauge_handles=tuple(f"public-gauge-{atom}" for atom in atom_set),
            )
        )
    return _left_regular_dataset(
        "public-regional-calibration",
        elements,
        multiply,
        lambda _value: True,
        records=records,
        contexts=contexts,
        preparations=preparations,
        probes=probes,
        readouts=readouts,
        gauges=gauges,
    )


def _rename_dataset(dataset: OperationalDataset) -> OperationalDataset:
    operation_names = {value.handle: f"renamed-operation-{index:03d}" for index, value in enumerate(reversed(dataset.operations))}
    preparation_names = {value.handle: f"renamed-preparation-{index}" for index, value in enumerate(dataset.preparations)}
    probe_names = {value.handle: f"renamed-probe-{index}" for index, value in enumerate(dataset.probes)}
    readout_names = {value.handle: f"renamed-readout-{index}" for index, value in enumerate(dataset.readouts)}
    record_names = {value.handle: f"renamed-record-{index}" for index, value in enumerate(dataset.records)}
    gauge_names = {value.handle: f"renamed-gauge-{index}" for index, value in enumerate(dataset.gauge_actions)}
    context_names = {value.handle: f"renamed-context-{index}" for index, value in enumerate(dataset.contexts)}
    return OperationalDataset(
        handle="renamed-dataset",
        carrier_dimension=dataset.carrier_dimension,
        operations=tuple(
            OperationClass(
                operation_names[value.handle],
                value.source_type,
                value.target_type,
                value.law,
                value.observed_signature,
                value.independently_selectable,
            )
            for value in reversed(dataset.operations)
        ),
        composition_rows=tuple(
            CompositionRow(
                operation_names[value.left],
                operation_names[value.right],
                value.tau,
                value.status,
                None if value.result_class is None else operation_names[value.result_class],
                value.law,
                value.observed_signature,
            )
            for value in reversed(dataset.composition_rows)
        ),
        preparations=tuple(FieldDatum(preparation_names[value.handle], value.boundary_type, value.payload) for value in dataset.preparations),
        contexts=tuple(
            AccessContext(
                context_names[value.handle],
                value.boundary_type,
                tuple(operation_names[item] for item in value.operation_handles),
                tuple(preparation_names[item] for item in value.preparation_handles),
                tuple(probe_names[item] for item in value.probe_handles),
                tuple(readout_names[item] for item in value.readout_handles),
                tuple(record_names[item] for item in value.record_handles),
                tuple(gauge_names[item] for item in value.gauge_handles),
            )
            for value in dataset.contexts
        ),
        probes=tuple(FieldDatum(probe_names[value.handle], value.boundary_type, value.payload) for value in dataset.probes),
        readouts=tuple(ReadoutDatum(readout_names[value.handle], value.boundary_type, value.projector_resolution) for value in dataset.readouts),
        records=tuple(
            RecordCandidate(
                record_names[value.handle],
                value.boundary_type,
                tuple(operation_names[item] for item in value.access_operations),
                RecordWitness(
                    handle=f"renamed-witness-{index}",
                    preparations=value.witness.preparations,
                    alternative_projectors=value.witness.alternative_projectors,
                    cut_record_projectors=value.witness.cut_record_projectors,
                    availability_probes=value.witness.availability_probes,
                    write=value.witness.write,
                    preserving=value.witness.preserving,
                    erasing=value.witness.erasing,
                    no_write=value.witness.no_write,
                ),
                value.ambient_projector_resolution,
            )
            for index, value in enumerate(dataset.records)
        ),
        gauge_actions=tuple(GaugeDatum(gauge_names[value.handle], value.law) for value in dataset.gauge_actions),
        access_postulate=dataset.access_postulate,
    )


@dataclass(frozen=True)
class GroupoidArrow:
    source_factorization: int
    target_factorization: int
    class_automorphism: Tuple[int, ...]
    carrier_action: MonomialLaw
    mapped_record_supports: Tuple[Tuple[Tuple[int, ...], Tuple[int, ...]], ...]


@dataclass(frozen=True)
class RecordBearingGroupoid:
    object_count: int
    arrow_count: int
    all_source_target_pairs: Tuple[Tuple[int, int], ...]
    every_factor_record_bearing: bool
    arrows: Tuple[GroupoidArrow, ...]


def _factorization_key(factors: Sequence[Subobject]) -> Tuple[Tuple[int, ...], ...]:
    return tuple(sorted((tuple(sorted(value)) for value in factors), key=lambda value: (len(value), value)))


def _composition_automorphisms(composition: CompositionObject) -> Tuple[Tuple[int, ...], ...]:
    if composition.identity is None or composition.size > 9:
        raise InvalidInput("public exhaustive automorphism control exceeds its declared size")
    others = tuple(value for value in range(composition.size) if value != composition.identity)
    results = []
    tests = 0
    for tail in itertools.permutations(others):
        tests += 1
        if tests > MAX_ISOMORPHISM_TESTS:
            raise InvalidInput("automorphism search exceeded the frozen cap")
        mapping = [0] * composition.size
        mapping[composition.identity] = composition.identity
        for source, target in zip(others, tail):
            mapping[source] = target
        mapping_tuple = tuple(mapping)
        if any(
            mapping_tuple[composition.product(left, right)]
            != composition.product(mapping_tuple[left], mapping_tuple[right])
            for left in range(composition.size)
            for right in range(composition.size)
        ):
            continue
        if any(
            composition.classes[source].independently_selectable
            != composition.classes[mapping_tuple[source]].independently_selectable
            for source in range(composition.size)
        ):
            continue
        carrier = permutation_law(mapping_tuple)
        if any(
            not composition.classes[source].law.conjugated(carrier).global_phase_equivalent(
                composition.classes[mapping_tuple[source]].law
            )
            for source in range(composition.size)
        ):
            continue
        results.append(mapping_tuple)
    return tuple(results)


def derive_record_bearing_groupoid(
    dataset: OperationalDataset,
    address: AddressabilityResult,
) -> RecordBearingGroupoid:
    factorizations = tuple(_factorization_key(value.factors) for value in address.finest_certificates)
    resolved, _ = resolve_records(dataset, address.composition, address.inverses)
    record_by_support = {tuple(sorted(value.support)): value for value in resolved if value.passes_w3}
    every_record_bearing = all(
        tuple(sorted(factor)) in record_by_support
        for factorization in address.finest_certificates
        for factor in factorization.factors
    )
    raw_records = []
    for candidate in dataset.records:
        support = subgroup_generated(
            address.composition,
            (address.composition.class_for_handle(handle) for handle in candidate.access_operations),
            address.inverses,
        )
        raw_records.append((support, candidate.ambient_projector_resolution))
    arrows = []
    factorization_index = {value: index for index, value in enumerate(factorizations)}
    for automorphism in _composition_automorphisms(address.composition):
        carrier = permutation_law(automorphism)
        for source_index, source in enumerate(address.finest_certificates):
            mapped_factors = tuple(frozenset(automorphism[value] for value in factor) for factor in source.factors)
            target_key = _factorization_key(mapped_factors)
            if target_key not in factorization_index:
                continue
            mapped_records = []
            record_ok = True
            for factor in source.factors:
                candidates = tuple(value for value in raw_records if value[0] == factor)
                if not candidates:
                    record_ok = False
                    break
                support, resolution = candidates[0]
                mapped_support = frozenset(automorphism[value] for value in support)
                mapped_resolution = tuple(frozenset(automorphism[value] for value in atom) for atom in resolution)
                targets = tuple(value for value in raw_records if value[0] == mapped_support and set(value[1]) == set(mapped_resolution))
                if not targets:
                    record_ok = False
                    break
                mapped_records.append((tuple(sorted(support)), tuple(sorted(mapped_support))))
            if record_ok:
                arrows.append(
                    GroupoidArrow(
                        source_factorization=source_index,
                        target_factorization=factorization_index[target_key],
                        class_automorphism=automorphism,
                        carrier_action=carrier,
                        mapped_record_supports=tuple(mapped_records),
                    )
                )
    pairs = tuple(sorted(set((value.source_factorization, value.target_factorization) for value in arrows)))
    return RecordBearingGroupoid(
        object_count=len(factorizations),
        arrow_count=len(arrows),
        all_source_target_pairs=pairs,
        every_factor_record_bearing=every_record_bearing,
        arrows=tuple(arrows),
    )


def _scientific_factor_summary(value: AddressabilityResult) -> Tuple[Tuple[int, ...], ...]:
    return tuple(sorted(tuple(sorted(certificate.factor_orders)) for certificate in value.finest_certificates))


def _expect_invalid(dataset: OperationalDataset, fragment: str) -> bool:
    try:
        build_composition_object(dataset)
    except (InvalidInput, AccessUnderdetermined) as error:
        return fragment in str(error)
    return False


def public_self_test() -> Mapping[str, object]:
    positive_dataset = public_selectability_pair(False)
    positive = analyze_addressability(positive_dataset)
    hostile_dataset = public_selectability_pair(True)
    hostile = analyze_addressability(hostile_dataset)
    collapse = analyze_addressability(public_declared_collapse_dataset())
    unavailable = analyze_addressability(public_unavailable_dataset())
    ambiguity_dataset = public_v4_dataset(with_records=True)
    ambiguity = analyze_addressability(ambiguity_dataset)
    groupoid = derive_record_bearing_groupoid(ambiguity_dataset, ambiguity)
    regional_dataset = public_regional_calibration_dataset()
    regional_address = analyze_addressability(regional_dataset)
    if len(regional_address.finest_certificates) != 1:
        raise AssertionError("public coprime regional calibration is not uniquely localized")
    regional_atlas = build_regional_atlas(
        regional_dataset,
        regional_address,
        regional_address.finest_certificates[0],
    )
    renamed_regional_dataset = _rename_dataset(regional_dataset)
    renamed_regional_address = analyze_addressability(renamed_regional_dataset)
    renamed_regional_atlas = build_regional_atlas(
        renamed_regional_dataset,
        renamed_regional_address,
        renamed_regional_address.finest_certificates[0],
    )

    nontrivial_factor = next(
        factor
        for factor in ambiguity.finest_certificates[0].factors
        if len(factor) == 2
    )
    collision = certify_factor_tuple(
        ambiguity_dataset,
        ambiguity.composition,
        (nontrivial_factor, nontrivial_factor),
        ambiguity.inverses,
    )
    replay = tuple(
        certify_factor_tuple(positive_dataset, positive.composition, value.factors, positive.inverses) == value
        for value in positive.finest_certificates
    )
    renamed = analyze_addressability(_rename_dataset(positive_dataset))
    roundtrip = dataset_from_data(dataset_to_data(ambiguity_dataset))

    row_base = positive_dataset
    target_index = next(
        index for index, row in enumerate(row_base.composition_rows)
        if row.left != "u000" and row.right != "u000"
    )
    target = row_base.composition_rows[target_index]
    wrong_law = MonomialLaw.unit(row_base.carrier_dimension)
    if target.law.global_phase_equivalent(wrong_law):
        wrong_law = MonomialLaw(tuple(reversed(range(row_base.carrier_dimension))), (0,) * row_base.carrier_dimension)
    wrong_m = _replace_row(
        row_base,
        target_index,
        CompositionRow(target.left, target.right, target.tau, target.status, target.result_class, wrong_law, wrong_law.signature()),
    )
    wrong_signature = _replace_row(
        row_base,
        target_index,
        CompositionRow(target.left, target.right, target.tau, target.status, target.result_class, target.law, ((999,), (999,))),
    )
    wrong_type = _replace_row(
        row_base,
        target_index,
        CompositionRow(target.left, target.right, "wrong|type|row", target.status, target.result_class, target.law, target.observed_signature),
    )
    bad_unavailable = _replace_row(
        row_base,
        target_index,
        CompositionRow(target.left, target.right, target.tau, UNAVAILABLE, target.result_class, target.law, target.observed_signature),
    )

    twisted = pairwise_valid_twisted_triple()
    checks = (
        (
            "P01",
            "scientific",
            bool(_scientific_factor_summary(positive))
            and all(value == (2, 6) for value in _scientific_factor_summary(positive)),
        ),
        ("P02", "scientific", all(replay)),
        ("P03", "scientific", hostile.blocked_at_address),
        ("P04", "scientific", hostile.first_obstruction == "no complete factor tuple is independently generated"),
        ("P05", "scientific", collapse.first_obstruction == "declared COLLAPSED status"),
        ("P06", "scientific", unavailable.first_obstruction == "unavailable composition row"),
        ("P07", "scientific", collision.multiplication_collision is not None and not collision.faithful_multiplication),
        ("P08", "scientific", groupoid.object_count == 3),
        ("P09", "scientific", groupoid.every_factor_record_bearing),
        ("P10", "scientific", groupoid.all_source_target_pairs == tuple(itertools.product(range(3), repeat=2))),
        ("P11", "scientific", twisted.regional_pair_maps_valid == (True, True, True)),
        ("P12", "scientific", twisted.record_pair_maps_valid == (True, True, True)),
        ("P13", "scientific", _scientific_factor_summary(positive) == _scientific_factor_summary(renamed)),
        ("P14", "procedural", roundtrip == ambiguity_dataset),
        ("P15", "scientific", _expect_invalid(wrong_m, "supplied row law disagrees")),
        ("P16", "scientific", _expect_invalid(wrong_signature, "row operational signature mismatch")),
        ("P17", "scientific", _expect_invalid(wrong_type, "boundary/context typing")),
        ("P18", "scientific", _expect_invalid(bad_unavailable, "UNAVAILABLE row supplies")),
        ("P19", "scientific", positive.composition.row_audit.typed_rows == 144),
        ("P20", "scientific", positive.composition.row_audit.exact_law_rows == 144),
        ("P21", "scientific", tuple(sorted(value.factor_orders for value in regional_address.finest_certificates)) == ((2, 3, 5),)),
        ("P22", "scientific", len(regional_atlas.objects) == 3),
        ("P23", "scientific", len(regional_atlas.nonvacuous_triples) == 1),
        ("P24", "scientific", all(value.records for value in regional_atlas.objects)),
        ("P25", "scientific", regional_atlas.coherent_paths > 0),
        ("P26", "scientific", not regional_atlas.is_complete_proper_boolean),
        ("P27", "scientific", len(regional_atlas.arrows) == len(regional_atlas.fact_maps)),
        (
            "P28",
            "scientific",
            (
                sorted(value.atoms for value in regional_atlas.objects),
                len(regional_atlas.arrows),
                len(regional_atlas.nonvacuous_triples),
            )
            == (
                sorted(value.atoms for value in renamed_regional_atlas.objects),
                len(renamed_regional_atlas.arrows),
                len(renamed_regional_atlas.nonvacuous_triples),
            ),
        ),
        (
            "P29",
            "scientific",
            twisted.rejected_at_triple_gate
            and not twisted.regional_loop_commutes
            and not twisted.loop_commutes,
        ),
    )
    passed = sum(1 for _, _, value in checks if value)
    return {
        "schema": "rq0-l0-certification-estimator-public-v1",
        "estimator_api": ESTIMATOR_API_VERSION,
        "scope": {
            "scalar_field": EXACT_SCALAR_FIELD,
            "gauge": GAUGE_SCOPE,
            "main_fixture_truth_present": False,
            "topology_or_causality_present": False,
        },
        "calibrations": {
            "fully_selectable_factor_orders": [list(value) for value in _scientific_factor_summary(positive)],
            "composite_only_coset_blocked": hostile.blocked_at_address,
            "declared_collapse_obstruction": collapse.first_obstruction,
            "unavailable_obstruction": unavailable.first_obstruction,
            "true_collision": None if collision.multiplication_collision is None else [list(collision.multiplication_collision[0]), list(collision.multiplication_collision[1]), collision.multiplication_collision[2]],
            "record_bearing_groupoid_objects": groupoid.object_count,
            "record_bearing_groupoid_arrows": groupoid.arrow_count,
            "record_bearing_groupoid_pairs": [list(value) for value in groupoid.all_source_target_pairs],
            "twisted_regional_pair_maps_valid": list(twisted.regional_pair_maps_valid),
            "twisted_record_pair_maps_valid": list(twisted.record_pair_maps_valid),
            "twisted_regional_loop_commutes": twisted.regional_loop_commutes,
            "twisted_loop_commutes": twisted.loop_commutes,
            "regional_calibration_factor_orders": list(regional_address.finest_certificates[0].factor_orders),
            "regional_calibration_objects": len(regional_atlas.objects),
            "regional_calibration_arrows": len(regional_atlas.arrows),
            "regional_calibration_fact_maps": len(regional_atlas.fact_maps),
            "regional_calibration_triples": len(regional_atlas.nonvacuous_triples),
        },
        "checks": [
            {"id": check_id, "class": check_class, "pass": value}
            for check_id, check_class, value in checks
        ],
        "passed": passed,
        "total": len(checks),
        "all_pass": passed == len(checks),
        "nonclaims": [
            "no main fixture or hidden main truth",
            "no spatial or causal localization",
            "no topology, spacetime, fields, or gravity",
        ],
    }


def normalize(value: object) -> object:
    if isinstance(value, Q24):
        return q24_to_data(value)
    if isinstance(value, MonomialLaw):
        return value.to_data()
    if isinstance(value, frozenset):
        return [normalize(entry) for entry in sorted(value)]
    if isinstance(value, tuple):
        return [normalize(entry) for entry in value]
    if isinstance(value, list):
        return [normalize(entry) for entry in value]
    if isinstance(value, dict):
        return {str(key): normalize(entry) for key, entry in sorted(value.items(), key=lambda item: str(item[0]))}
    return value


def main() -> int:
    result = public_self_test()
    print(json.dumps(normalize(result), indent=2, sort_keys=True))
    return 0 if result["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
