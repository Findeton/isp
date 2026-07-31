#!/usr/bin/env python3
"""Generic exact estimator for v13 RQ0-L0 operational localization.

This module is the estimator-freeze surface required by the strict pin at
commit f218dde7b73631f7fd6359582d7bf494990eb076.  It contains no main L0
fixture, construction partition, expected overlap nerve, spatial label,
causal relation, metric, or field object.  Later fixture and scoring modules
may import this module; this module must never import them.

The scientific path is exact over Q(zeta_8).  Localization uses only frozen
preparations, opaque intervention matrices, composition contexts, rank-one
readout probes, declared presentation actions, and frozen W3 witnesses.
Displayed tensor factors are neither inputs to nor outputs of the estimator.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Iterator, Mapping, Optional, Sequence, Tuple


PIN_COMMIT = "f218dde7b73631f7fd6359582d7bf494990eb076"
PIN_SHA256 = "02ed47ad0a294741e613639b02066797a2057fcfcd816edd81203f353b1f9a59"
ESTIMATOR_API_VERSION = "RQ0-L0-estimator-v1"
MAX_CARRIER_DIMENSION = 32
MAX_INTERVENTION_CLASSES = 8
MAX_SET_PARTITIONS = 4140


# ---------------------------------------------------------------------------
# Exact Q(zeta_8) arithmetic
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Q8:
    """a + b*z + c*z^2 + d*z^3 in Q[z]/(z^4 + 1)."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)
    c: Fraction = Fraction(0)
    d: Fraction = Fraction(0)

    @staticmethod
    def coerce(value: object) -> "Q8":
        if isinstance(value, Q8):
            return value
        if isinstance(value, Fraction):
            return Q8(value)
        if isinstance(value, int):
            return Q8(Fraction(value))
        raise TypeError(f"cannot coerce {type(value).__name__} to Q8")

    @staticmethod
    def from_coefficients(values: Sequence[Fraction]) -> "Q8":
        padded = tuple(values) + (Fraction(0),) * (4 - len(values))
        if len(padded) != 4:
            raise ValueError("Q8 needs at most four reduced coefficients")
        return Q8(*padded)

    def coefficients(self) -> Tuple[Fraction, Fraction, Fraction, Fraction]:
        return (self.a, self.b, self.c, self.d)

    def __add__(self, other: object) -> "Q8":
        rhs = Q8.coerce(other)
        return Q8(*(x + y for x, y in zip(self.coefficients(), rhs.coefficients())))

    def __radd__(self, other: object) -> "Q8":
        return self + other

    def __sub__(self, other: object) -> "Q8":
        rhs = Q8.coerce(other)
        return Q8(*(x - y for x, y in zip(self.coefficients(), rhs.coefficients())))

    def __rsub__(self, other: object) -> "Q8":
        return Q8.coerce(other) - self

    def __neg__(self) -> "Q8":
        return Q8(*(-x for x in self.coefficients()))

    def __mul__(self, other: object) -> "Q8":
        rhs = Q8.coerce(other)
        raw = [Fraction(0)] * 7
        for left_index, left in enumerate(self.coefficients()):
            if left:
                for right_index, right in enumerate(rhs.coefficients()):
                    if right:
                        raw[left_index + right_index] += left * right
        for degree in range(6, 3, -1):
            if raw[degree]:
                raw[degree - 4] -= raw[degree]
        return Q8.from_coefficients(raw[:4])

    def __rmul__(self, other: object) -> "Q8":
        return self * other

    def __pow__(self, exponent: int) -> "Q8":
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = Q8.one()
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power //= 2
        return result

    def conjugate(self) -> "Q8":
        # z -> z^-1 = -z^3, z^2 -> -z^2, z^3 -> -z.
        return Q8(self.a, -self.d, -self.c, -self.b)

    def inverse(self) -> "Q8":
        if self.is_zero():
            raise ZeroDivisionError("inverse of zero")
        columns = []
        for basis_index in range(4):
            basis = Q8.from_coefficients(
                tuple(Fraction(1) if index == basis_index else Fraction(0) for index in range(4))
            )
            columns.append((self * basis).coefficients())
        coefficient_matrix = tuple(
            tuple(columns[column][row] for column in range(4))
            for row in range(4)
        )
        solution = solve_fraction_system(
            coefficient_matrix,
            (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        )
        return Q8.from_coefficients(solution)

    def __truediv__(self, other: object) -> "Q8":
        return self * Q8.coerce(other).inverse()

    def __bool__(self) -> bool:
        return not self.is_zero()

    def is_zero(self) -> bool:
        return all(value == 0 for value in self.coefficients())

    def is_real(self) -> bool:
        return self == self.conjugate()

    def sort_key(self) -> Tuple[Tuple[int, int], ...]:
        return tuple((value.numerator, value.denominator) for value in self.coefficients())

    def render(self) -> str:
        names = ("1", "z", "z^2", "z^3")
        terms = []
        for coefficient, name in zip(self.coefficients(), names):
            if coefficient:
                terms.append(f"({coefficient})*{name}")
        return "0" if not terms else "+".join(terms)

    @staticmethod
    def zero() -> "Q8":
        return Q8()

    @staticmethod
    def one() -> "Q8":
        return Q8(Fraction(1))


def solve_fraction_system(
    matrix: Sequence[Sequence[Fraction]],
    vector: Sequence[Fraction],
) -> Tuple[Fraction, ...]:
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix) or len(vector) != size:
        raise ValueError("fraction system must be nonempty and square")
    augmented = [list(row) + [vector[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if augmented[row][column]), None)
        if pivot is None:
            raise ZeroDivisionError("singular rational system")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [entry / scale for entry in augmented[column]]
        for row in range(size):
            if row == column or not augmented[row][column]:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                left - factor * right
                for left, right in zip(augmented[row], augmented[column])
            ]
    return tuple(augmented[row][-1] for row in range(size))


ZERO = Q8.zero()
ONE = Q8.one()
ZETA = Q8(b=Fraction(1))
I = ZETA ** 2
INV_SQRT2 = (ZETA - (ZETA ** 3)) * Q8(Fraction(1, 2))

Vector = Tuple[Q8, ...]
Matrix = Tuple[Tuple[Q8, ...], ...]


# ---------------------------------------------------------------------------
# Exact vectors and matrices
# ---------------------------------------------------------------------------


def vector(values: Iterable[object]) -> Vector:
    return tuple(Q8.coerce(value) for value in values)


def matrix(rows: Iterable[Iterable[object]]) -> Matrix:
    result = tuple(tuple(Q8.coerce(value) for value in row) for row in rows)
    if not result or not result[0] or any(len(row) != len(result[0]) for row in result):
        raise ValueError("matrix must be nonempty and rectangular")
    return result


def shape(value: Matrix) -> Tuple[int, int]:
    return (len(value), len(value[0]))


def zero_matrix(rows: int, columns: int) -> Matrix:
    return tuple(tuple(ZERO for _ in range(columns)) for _ in range(rows))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(ONE if row == column else ZERO for column in range(size))
        for row in range(size)
    )


def basis_vector(size: int, index: int) -> Vector:
    return tuple(ONE if position == index else ZERO for position in range(size))


def vadd(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))


def vscale(scalar: object, value: Vector) -> Vector:
    coefficient = Q8.coerce(scalar)
    return tuple(coefficient * entry for entry in value)


def inner(left: Vector, right: Vector) -> Q8:
    return sum((a.conjugate() * b for a, b in zip(left, right)), ZERO)


def mv(value: Matrix, state: Vector) -> Vector:
    if len(value[0]) != len(state):
        raise ValueError("matrix and vector dimensions do not compose")
    return tuple(
        sum((entry * state[column] for column, entry in enumerate(row)), ZERO)
        for row in value
    )


def madd(left: Matrix, right: Matrix) -> Matrix:
    if shape(left) != shape(right):
        raise ValueError("matrix dimensions differ")
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def msub(left: Matrix, right: Matrix) -> Matrix:
    if shape(left) != shape(right):
        raise ValueError("matrix dimensions differ")
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def mscale(scalar: object, value: Matrix) -> Matrix:
    coefficient = Q8.coerce(scalar)
    return tuple(tuple(coefficient * entry for entry in row) for row in value)


def mmul(left: Matrix, right: Matrix) -> Matrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not compose")
    output_columns = len(right[0])
    right_nonzero_rows = tuple(
        tuple((column, entry) for column, entry in enumerate(row) if entry)
        for row in right
    )
    rows = []
    for left_row in left:
        output_row = [ZERO] * output_columns
        for middle, left_entry in enumerate(left_row):
            if not left_entry:
                continue
            for column, right_entry in right_nonzero_rows[middle]:
                output_row[column] = output_row[column] + left_entry * right_entry
        rows.append(tuple(output_row))
    return tuple(rows)


def adjoint(value: Matrix) -> Matrix:
    return tuple(
        tuple(value[row][column].conjugate() for row in range(len(value)))
        for column in range(len(value[0]))
    )


def kron(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[left_row][left_column] * right[right_row][right_column]
            for left_column in range(len(left[0]))
            for right_column in range(len(right[0]))
        )
        for left_row in range(len(left))
        for right_row in range(len(right))
    )


def outer(left: Vector, right: Vector) -> Matrix:
    return tuple(
        tuple(a * b.conjugate() for b in right)
        for a in left
    )


def projector(state: Vector) -> Matrix:
    norm = inner(state, state)
    if norm.is_zero():
        raise ValueError("zero vector has no projector")
    return mscale(norm.inverse(), outer(state, state))


def flatten(value: Matrix) -> Tuple[Q8, ...]:
    return tuple(entry for row in value for entry in row)


def unflatten(value: Sequence[Q8], rows: int, columns: int) -> Matrix:
    if len(value) != rows * columns:
        raise ValueError("flat matrix length mismatch")
    return tuple(
        tuple(value[row * columns + column] for column in range(columns))
        for row in range(rows)
    )


def matrix_inverse(value: Matrix) -> Matrix:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("inverse requires a square matrix")
    augmented = [list(value[row]) + list(identity(rows)[row]) for row in range(rows)]
    for column in range(columns):
        pivot = next((row for row in range(column, rows) if augmented[row][column]), None)
        if pivot is None:
            raise ZeroDivisionError("singular matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [entry / scale for entry in augmented[column]]
        for row in range(rows):
            if row == column or not augmented[row][column]:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                left - factor * right
                for left, right in zip(augmented[row], augmented[column])
            ]
    return tuple(tuple(augmented[row][columns:]) for row in range(rows))


def is_zero_matrix(value: Matrix) -> bool:
    return all(entry.is_zero() for row in value for entry in row)


def is_hermitian(value: Matrix) -> bool:
    return value == adjoint(value)


def is_projector(value: Matrix) -> bool:
    return is_hermitian(value) and mmul(value, value) == value


def is_unitary(value: Matrix) -> bool:
    rows, columns = shape(value)
    return rows == columns and mmul(adjoint(value), value) == identity(rows)


def conjugate_by(action: Matrix, value: Matrix) -> Matrix:
    return mmul(mmul(action, value), adjoint(action))


def matrices_commute(left: Matrix, right: Matrix) -> bool:
    return mmul(left, right) == mmul(right, left)


def matrix_phase_key(value: Matrix) -> Tuple[Tuple[Tuple[int, int], ...], ...]:
    return tuple(entry.sort_key() for entry in flatten(value))


def canonical_mu8_phase(value: Matrix) -> Matrix:
    candidates = tuple(mscale(ZETA ** power, value) for power in range(8))
    return min(candidates, key=matrix_phase_key)


# ---------------------------------------------------------------------------
# Exact sparse linear spans and generated star-algebras
# ---------------------------------------------------------------------------


class SparseSpan:
    def __init__(self, length: int):
        self.length = length
        self._rows: dict[int, dict[int, Q8]] = {}

    @property
    def dimension(self) -> int:
        return len(self._rows)

    def _reduce(self, entries: Mapping[int, Q8]) -> dict[int, Q8]:
        work = {index: value for index, value in entries.items() if value}
        for pivot in sorted(self._rows):
            coefficient = work.get(pivot, ZERO)
            if not coefficient:
                continue
            for index, value in self._rows[pivot].items():
                updated = work.get(index, ZERO) - coefficient * value
                if updated:
                    work[index] = updated
                elif index in work:
                    del work[index]
        return work

    def add(self, dense: Sequence[Q8]) -> Optional[Tuple[Q8, ...]]:
        if len(dense) != self.length:
            raise ValueError("span vector length mismatch")
        reduced = self._reduce({index: value for index, value in enumerate(dense) if value})
        if not reduced:
            return None
        pivot = min(reduced)
        scale = reduced[pivot].inverse()
        normalized = {index: scale * value for index, value in reduced.items()}
        self._rows[pivot] = normalized
        return tuple(normalized.get(index, ZERO) for index in range(self.length))

    def contains(self, dense: Sequence[Q8]) -> bool:
        if len(dense) != self.length:
            return False
        return not self._reduce({index: value for index, value in enumerate(dense) if value})

    def basis(self) -> Tuple[Tuple[Q8, ...], ...]:
        return tuple(
            tuple(self._rows[pivot].get(index, ZERO) for index in range(self.length))
            for pivot in sorted(self._rows)
        )


@dataclass(frozen=True)
class AlgebraBasis:
    matrices: Tuple[Matrix, ...]

    @property
    def dimension(self) -> int:
        return len(self.matrices)


def span_from_matrices(values: Sequence[Matrix]) -> SparseSpan:
    if not values:
        raise ValueError("cannot infer matrix size from empty span")
    rows, columns = shape(values[0])
    if any(shape(value) != (rows, columns) for value in values):
        raise ValueError("span matrices have inconsistent shapes")
    result = SparseSpan(rows * columns)
    for value in values:
        result.add(flatten(value))
    return result


def span_contains(algebra: AlgebraBasis, value: Matrix) -> bool:
    return span_from_matrices(algebra.matrices).contains(flatten(value))


def span_subset(left: AlgebraBasis, right: AlgebraBasis) -> bool:
    target = span_from_matrices(right.matrices)
    return all(target.contains(flatten(value)) for value in left.matrices)


def span_equal(left: AlgebraBasis, right: AlgebraBasis) -> bool:
    return (
        left.dimension == right.dimension
        and span_subset(left, right)
        and span_subset(right, left)
    )


def intersection_dimension(left: AlgebraBasis, right: AlgebraBasis) -> int:
    combined = span_from_matrices(left.matrices + right.matrices)
    return left.dimension + right.dimension - combined.dimension


def generated_star_algebra(
    generators: Sequence[Matrix],
    unit: Matrix,
    maximum_dimension: int,
) -> AlgebraBasis:
    rows, columns = shape(unit)
    if rows != columns:
        raise ValueError("algebra unit must be square")
    letters = []
    for generator in generators:
        if shape(generator) != (rows, rows):
            raise ValueError("algebra generator has wrong shape")
        for candidate in (generator, adjoint(generator)):
            if candidate not in letters:
                letters.append(candidate)
    span = SparseSpan(rows * rows)
    first = span.add(flatten(unit))
    if first is None:
        raise AssertionError("nonzero algebra unit reduced to zero")
    frontier = [unflatten(first, rows, rows)]
    while frontier:
        word = frontier.pop(0)
        for letter in letters:
            candidate = mmul(word, letter)
            added = span.add(flatten(candidate))
            if added is not None:
                if span.dimension > maximum_dimension:
                    raise RuntimeError("generated algebra exceeded declared dimension cap")
                frontier.append(unflatten(added, rows, rows))
    return AlgebraBasis(tuple(unflatten(row, rows, rows) for row in span.basis()))


# ---------------------------------------------------------------------------
# Typed black-box operational data
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Operation:
    handle: str
    amplitude: Matrix


@dataclass(frozen=True)
class Context:
    handle: str
    before: Matrix
    after: Matrix


@dataclass(frozen=True)
class Probe:
    handle: str
    state: Vector


@dataclass(frozen=True)
class RecordWitness:
    handle: str
    preparations: Tuple[Vector, ...]
    alternative_projectors: Tuple[Matrix, ...]
    cut_record_projectors: Tuple[Matrix, ...]
    availability_probes: Tuple[Matrix, ...]
    write: Matrix
    preserving: Tuple[Matrix, ...]
    erasing: Tuple[Matrix, ...]
    no_write: Matrix


@dataclass(frozen=True)
class OperationalDataset:
    handle: str
    dimension: int
    preparations: Tuple[Vector, ...]
    interventions: Tuple[Operation, ...]
    contexts: Tuple[Context, ...]
    probes: Tuple[Probe, ...]
    support_actions: Tuple[Matrix, ...]
    presentation_actions: Tuple[Matrix, ...]
    records: Tuple[RecordWitness, ...] = ()
    access_declaration: str = "POSTULATE: frozen finite operational access contract"
    gauge_declaration: str = "configuration relabelling x exact mu_8 boundary phase"


class InvalidDataset(ValueError):
    pass


class AccessUnderdetermined(ValueError):
    pass


def validate_square_matrix(value: Matrix, dimension: int, label: str) -> None:
    if shape(value) != (dimension, dimension):
        raise InvalidDataset(f"{label} has shape {shape(value)}, expected {(dimension, dimension)}")


def validate_dataset(dataset: OperationalDataset) -> None:
    if not 1 < dataset.dimension <= MAX_CARRIER_DIMENSION:
        raise InvalidDataset("carrier dimension violates the frozen cap")
    if not dataset.preparations or not dataset.interventions:
        raise InvalidDataset("preparations and interventions must be nonempty")
    if not dataset.contexts or not dataset.probes:
        raise InvalidDataset("contexts and probes must be frozen and nonempty")
    if len({operation.handle for operation in dataset.interventions}) != len(dataset.interventions):
        raise InvalidDataset("intervention handles must be unique")
    for index, preparation in enumerate(dataset.preparations):
        if len(preparation) != dataset.dimension or inner(preparation, preparation).is_zero():
            raise InvalidDataset(f"invalid preparation {index}")
    for operation in dataset.interventions:
        validate_square_matrix(operation.amplitude, dataset.dimension, operation.handle)
        if not is_unitary(operation.amplitude):
            raise InvalidDataset(f"localization intervention {operation.handle} is not unitary")
    for context in dataset.contexts:
        validate_square_matrix(context.before, dataset.dimension, f"{context.handle}.before")
        validate_square_matrix(context.after, dataset.dimension, f"{context.handle}.after")
        if not is_unitary(context.before) or not is_unitary(context.after):
            raise InvalidDataset(f"context {context.handle} is not unitary at this first rung")
    for probe in dataset.probes:
        if len(probe.state) != dataset.dimension or inner(probe.state, probe.state).is_zero():
            raise InvalidDataset(f"invalid probe {probe.handle}")
    for index, action in enumerate(dataset.support_actions):
        validate_square_matrix(action, dataset.dimension, f"support action {index}")
        if not is_unitary(action):
            raise InvalidDataset(f"support action {index} is not unitary at this first rung")
    for index, action in enumerate(dataset.presentation_actions):
        validate_square_matrix(action, dataset.dimension, f"presentation action {index}")
        if not is_unitary(action):
            raise InvalidDataset(f"presentation action {index} is not unitary")


def effective_presentation_group(dataset: OperationalDataset) -> Tuple[Matrix, ...]:
    unit = identity(dataset.dimension)
    actions = []
    for candidate in (unit,) + dataset.presentation_actions:
        if candidate not in actions:
            actions.append(candidate)
    for action in tuple(actions):
        if adjoint(action) not in actions:
            raise InvalidDataset("presentation actions are not inverse closed")
    for left in tuple(actions):
        for right in tuple(actions):
            if mmul(left, right) not in actions:
                raise InvalidDataset("presentation actions are not composition closed")
    return tuple(actions)


# ---------------------------------------------------------------------------
# Accessible support and operational quotient
# ---------------------------------------------------------------------------


def reachable_support(dataset: OperationalDataset) -> Tuple[Matrix, int]:
    dimension = dataset.dimension
    actions = tuple(dataset.support_actions) + tuple(
        operation.amplitude for operation in dataset.interventions
    ) + tuple(
        action
        for context in dataset.contexts
        for action in (context.before, context.after)
    )
    span = SparseSpan(dimension)
    frontier: list[Vector] = []
    for preparation in dataset.preparations:
        added = span.add(preparation)
        if added is not None:
            frontier.append(added)
    while frontier:
        state = frontier.pop(0)
        for action in actions:
            added = span.add(mv(action, state))
            if added is not None:
                frontier.append(added)
    basis = span.basis()
    columns = tuple(zip(*basis))
    basis_matrix = tuple(tuple(entry for entry in row) for row in columns)
    gram = mmul(adjoint(basis_matrix), basis_matrix)
    support = mmul(mmul(basis_matrix, matrix_inverse(gram)), adjoint(basis_matrix))
    if not is_projector(support):
        raise AssertionError("reachable-support projector failed exact projector test")
    for action in actions:
        escaped = mmul(msub(identity(dimension), support), mmul(action, support))
        if not is_zero_matrix(escaped):
            raise AssertionError("reachable-support closure failed")
    return support, span.dimension


def born_probability(probe: Vector, state: Vector) -> Q8:
    amplitude = inner(probe, state)
    probability = amplitude.conjugate() * amplitude
    if not probability.is_real():
        raise AssertionError("Born probability is not exactly real")
    return probability


def operational_signature(dataset: OperationalDataset, operation: Matrix) -> Tuple[Q8, ...]:
    result = []
    for preparation in dataset.preparations:
        for context in dataset.contexts:
            state = mv(context.after, mv(operation, mv(context.before, preparation)))
            for probe in dataset.probes:
                result.append(born_probability(probe.state, state))
    return tuple(result)


@dataclass(frozen=True)
class InterventionClass:
    members: Tuple[str, ...]
    signature: Tuple[Q8, ...]
    representative: Matrix


def intervention_quotient(
    dataset: OperationalDataset,
    support: Matrix,
) -> Tuple[InterventionClass, ...]:
    grouped: dict[Tuple[Q8, ...], list[Operation]] = {}
    for operation in dataset.interventions:
        grouped.setdefault(operational_signature(dataset, operation.amplitude), []).append(operation)
    result = []
    ordered_signatures = sorted(
        grouped,
        key=lambda signature: tuple(value.sort_key() for value in signature),
    )
    for signature in ordered_signatures:
        operations = grouped[signature]
        compressed = tuple(
            canonical_mu8_phase(mmul(mmul(support, operation.amplitude), support))
            for operation in operations
        )
        if any(value != compressed[0] for value in compressed[1:]):
            raise AccessUnderdetermined(
                "operationally equal interventions retain distinct accessible actions"
            )
        result.append(
            InterventionClass(
                members=tuple(sorted(operation.handle for operation in operations)),
                signature=signature,
                representative=compressed[0],
            )
        )
    if len(result) > MAX_INTERVENTION_CLASSES:
        raise InvalidDataset("operational quotient exceeds intervention-class cap")
    return tuple(result)


# ---------------------------------------------------------------------------
# W3 witness evaluation, basis invariant under simultaneous conjugation
# ---------------------------------------------------------------------------


def validate_projector_family(projectors: Sequence[Matrix], unit: Matrix, label: str) -> None:
    if not projectors:
        raise InvalidDataset(f"{label} projector family is empty")
    if any(not is_projector(value) for value in projectors):
        raise InvalidDataset(f"{label} contains a non-projector")
    for left, right in itertools.combinations(projectors, 2):
        if not is_zero_matrix(mmul(left, right)):
            raise InvalidDataset(f"{label} projectors are not orthogonal")
    total = zero_matrix(*shape(unit))
    for value in projectors:
        total = madd(total, value)
    if total != unit:
        raise InvalidDataset(f"{label} projectors do not resolve the accessible unit")


def matrix_has_action(value: Matrix) -> bool:
    return not is_zero_matrix(value)


def h_corr(witness: RecordWitness, write: Matrix) -> bool:
    mapping = []
    for alternative in witness.alternative_projectors:
        observed_sector: Optional[int] = None
        live = False
        for preparation in witness.preparations:
            component = mv(write, mv(alternative, preparation))
            if inner(component, component).is_zero():
                continue
            live = True
            sectors = tuple(
                index
                for index, record in enumerate(witness.cut_record_projectors)
                if not inner(mv(record, component), mv(record, component)).is_zero()
            )
            if len(sectors) != 1:
                return False
            if observed_sector is None:
                observed_sector = sectors[0]
            elif observed_sector != sectors[0]:
                return False
        if not live or observed_sector is None:
            return False
        mapping.append(observed_sector)
    return len(mapping) == len(set(mapping))


def h_avail(witness: RecordWitness, continuation: Matrix) -> bool:
    for final_probe in witness.availability_probes:
        incoming = tuple(
            index
            for index, record in enumerate(witness.cut_record_projectors)
            if matrix_has_action(mmul(final_probe, mmul(continuation, record)))
        )
        if len(incoming) > 1:
            return False
    return True


def cross_sector_coherence_count(witness: RecordWitness, continuation: Matrix) -> int:
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


@dataclass(frozen=True)
class RecordResult:
    handle: str
    occurrence: bool
    preserving_available: Tuple[bool, ...]
    erasing_available: Tuple[bool, ...]
    erasing_cross_coherence: Tuple[int, ...]
    no_write_occurrence: bool

    @property
    def passes_w3_control(self) -> bool:
        return (
            self.occurrence
            and bool(self.preserving_available)
            and all(self.preserving_available)
            and bool(self.erasing_available)
            and all(not value for value in self.erasing_available)
            and all(value > 0 for value in self.erasing_cross_coherence)
            and not self.no_write_occurrence
        )


def evaluate_record_witness(
    witness: RecordWitness,
    support: Matrix,
    dimension: int,
) -> RecordResult:
    for label, family in (
        ("alternative", witness.alternative_projectors),
        ("record", witness.cut_record_projectors),
        ("availability", witness.availability_probes),
    ):
        for value in family:
            validate_square_matrix(value, dimension, f"{witness.handle}.{label}")
        validate_projector_family(family, support, f"{witness.handle}.{label}")
    for label, value in (
        ("write", witness.write),
        ("no_write", witness.no_write),
    ):
        validate_square_matrix(value, dimension, f"{witness.handle}.{label}")
        if not is_unitary(value):
            raise InvalidDataset(f"{witness.handle}.{label} is not unitary")
    for index, value in enumerate(witness.preserving):
        validate_square_matrix(value, dimension, f"{witness.handle}.preserving.{index}")
        if not is_unitary(value):
            raise InvalidDataset(f"{witness.handle}.preserving.{index} is not unitary")
    for index, value in enumerate(witness.erasing):
        validate_square_matrix(value, dimension, f"{witness.handle}.erasing.{index}")
        if not is_unitary(value):
            raise InvalidDataset(f"{witness.handle}.erasing.{index} is not unitary")
    complement = msub(identity(dimension), support)
    for index, preparation in enumerate(witness.preparations):
        if len(preparation) != dimension or inner(preparation, preparation).is_zero():
            raise InvalidDataset(f"{witness.handle}.preparation.{index} is invalid")
        if any(mv(complement, preparation)):
            raise InvalidDataset(f"{witness.handle}.preparation.{index} leaves accessible support")
    for label, value in (
        (("write", witness.write), ("no_write", witness.no_write))
        + tuple((f"preserving.{index}", entry) for index, entry in enumerate(witness.preserving))
        + tuple((f"erasing.{index}", entry) for index, entry in enumerate(witness.erasing))
    ):
        if not is_zero_matrix(mmul(complement, mmul(value, support))):
            raise InvalidDataset(f"{witness.handle}.{label} leaves accessible support")
    return RecordResult(
        handle=witness.handle,
        occurrence=h_corr(witness, witness.write),
        preserving_available=tuple(h_avail(witness, value) for value in witness.preserving),
        erasing_available=tuple(h_avail(witness, value) for value in witness.erasing),
        erasing_cross_coherence=tuple(
            cross_sector_coherence_count(witness, value) for value in witness.erasing
        ),
        no_write_occurrence=h_corr(witness, witness.no_write),
    )


def record_lives_in_algebra(witness: RecordWitness, algebra: AlgebraBasis) -> bool:
    required = (
        witness.alternative_projectors
        + witness.cut_record_projectors
        + witness.availability_probes
        + (witness.write, witness.no_write)
        + witness.preserving
        + witness.erasing
    )
    return all(span_contains(algebra, value) for value in required)


# ---------------------------------------------------------------------------
# Exhaustive factorization, groupoid, local lattice, and overlap nerve
# ---------------------------------------------------------------------------


def set_partitions(size: int) -> Iterator[Tuple[Tuple[int, ...], ...]]:
    if size < 1:
        return

    def build(next_value: int, blocks: list[list[int]]) -> Iterator[Tuple[Tuple[int, ...], ...]]:
        if next_value == size:
            yield tuple(tuple(block) for block in blocks)
            return
        for index in range(len(blocks)):
            blocks[index].append(next_value)
            yield from build(next_value + 1, blocks)
            blocks[index].pop()
        blocks.append([next_value])
        yield from build(next_value + 1, blocks)
        blocks.pop()

    yield from build(1, [[0]])


@dataclass(frozen=True)
class Factorization:
    blocks: Tuple[Tuple[int, ...], ...]
    algebra_dimensions: Tuple[int, ...]


@dataclass(frozen=True)
class LocalObject:
    atoms: Tuple[int, ...]
    algebra_dimension: int
    records: Tuple[str, ...]


@dataclass(frozen=True)
class OverlapRow:
    objects: Tuple[int, ...]
    atoms: Tuple[int, ...]
    algebra_dimension: int


@dataclass(frozen=True)
class LocalLattice:
    factorization_index: int
    objects: Tuple[LocalObject, ...]
    pair_overlaps: Tuple[OverlapRow, ...]
    triple_overlaps: Tuple[OverlapRow, ...]


@dataclass(frozen=True)
class GroupoidArrow:
    action_index: int
    source_factorization: int
    target_factorization: int
    atom_map: Tuple[int, ...]


@dataclass(frozen=True)
class LocalizationResult:
    dataset_handle: str
    accessible_dimension: int
    intervention_classes: Tuple[InterventionClass, ...]
    ambient_algebra_dimension: int
    partitions_examined: int
    valid_factorizations: Tuple[Factorization, ...]
    finest_factorizations: Tuple[Factorization, ...]
    lattices: Tuple[LocalLattice, ...]
    groupoid_arrows: Tuple[GroupoidArrow, ...]
    record_results: Tuple[RecordResult, ...]
    diagnostics: Tuple[str, ...]

    @property
    def has_nontrivial_localization(self) -> bool:
        return bool(self.finest_factorizations)

    @property
    def is_factorization_ambiguous(self) -> bool:
        return len(self.finest_factorizations) > 1

    def structural_signature(self) -> Tuple[object, ...]:
        lattice_signatures = []
        for factorization, lattice in zip(self.finest_factorizations, self.lattices):
            lattice_signatures.append(
                (
                    tuple(sorted(factorization.algebra_dimensions)),
                    tuple(sorted((row.algebra_dimension, len(row.records)) for row in lattice.objects)),
                    tuple(sorted(row.algebra_dimension for row in lattice.pair_overlaps)),
                    tuple(sorted(row.algebra_dimension for row in lattice.triple_overlaps)),
                )
            )
        return (
            self.accessible_dimension,
            self.ambient_algebra_dimension,
            len(self.intervention_classes),
            tuple(sorted(lattice_signatures)),
            len(self.groupoid_arrows),
        )

    def to_data(self) -> Mapping[str, object]:
        return {
            "api": ESTIMATOR_API_VERSION,
            "dataset": self.dataset_handle,
            "accessible_dimension": self.accessible_dimension,
            "intervention_class_count": len(self.intervention_classes),
            "intervention_classes": [list(value.members) for value in self.intervention_classes],
            "ambient_algebra_dimension": self.ambient_algebra_dimension,
            "partitions_examined": self.partitions_examined,
            "valid_factorizations": [
                {
                    "blocks": [list(block) for block in value.blocks],
                    "algebra_dimensions": list(value.algebra_dimensions),
                }
                for value in self.valid_factorizations
            ],
            "finest_factorizations": [
                {
                    "blocks": [list(block) for block in value.blocks],
                    "algebra_dimensions": list(value.algebra_dimensions),
                }
                for value in self.finest_factorizations
            ],
            "lattices": [
                {
                    "factorization_index": lattice.factorization_index,
                    "objects": [
                        {
                            "atoms": list(value.atoms),
                            "algebra_dimension": value.algebra_dimension,
                            "records": list(value.records),
                        }
                        for value in lattice.objects
                    ],
                    "pair_overlaps": [
                        {
                            "objects": list(value.objects),
                            "atoms": list(value.atoms),
                            "algebra_dimension": value.algebra_dimension,
                        }
                        for value in lattice.pair_overlaps
                    ],
                    "triple_overlaps": [
                        {
                            "objects": list(value.objects),
                            "atoms": list(value.atoms),
                            "algebra_dimension": value.algebra_dimension,
                        }
                        for value in lattice.triple_overlaps
                    ],
                }
                for lattice in self.lattices
            ],
            "groupoid_arrows": [
                {
                    "action_index": value.action_index,
                    "source": value.source_factorization,
                    "target": value.target_factorization,
                    "atom_map": list(value.atom_map),
                }
                for value in self.groupoid_arrows
            ],
            "records": [
                {
                    "handle": value.handle,
                    "occurrence": value.occurrence,
                    "preserving_available": list(value.preserving_available),
                    "erasing_available": list(value.erasing_available),
                    "erasing_cross_coherence": list(value.erasing_cross_coherence),
                    "no_write_occurrence": value.no_write_occurrence,
                    "passes_w3_control": value.passes_w3_control,
                }
                for value in self.record_results
            ],
            "diagnostics": list(self.diagnostics),
        }


def algebra_conjugate(action: Matrix, algebra: AlgebraBasis) -> AlgebraBasis:
    return AlgebraBasis(tuple(conjugate_by(action, value) for value in algebra.matrices))


def analyze_localization(dataset: OperationalDataset) -> LocalizationResult:
    validate_dataset(dataset)
    support, accessible_dimension = reachable_support(dataset)
    classes = intervention_quotient(dataset, support)
    representatives = tuple(value.representative for value in classes)
    maximum_algebra_dimension = accessible_dimension * accessible_dimension
    ambient = generated_star_algebra(representatives, support, maximum_algebra_dimension)
    record_results = tuple(
        evaluate_record_witness(witness, support, dataset.dimension)
        for witness in dataset.records
    )

    algebra_cache: dict[Tuple[int, ...], AlgebraBasis] = {}

    def algebra_for(indices: Iterable[int]) -> AlgebraBasis:
        key = tuple(sorted(set(indices)))
        if key not in algebra_cache:
            algebra_cache[key] = generated_star_algebra(
                tuple(representatives[index] for index in key),
                support,
                maximum_algebra_dimension,
            )
        return algebra_cache[key]

    valid = []
    partitions_examined = 0
    for partition in set_partitions(len(classes)):
        partitions_examined += 1
        if partitions_examined > MAX_SET_PARTITIONS:
            raise InvalidDataset("set-partition search exceeded frozen cap")
        if len(partition) < 2:
            continue
        algebras = tuple(algebra_for(block) for block in partition)
        if any(value.dimension <= 1 for value in algebras):
            continue
        product_dimension = 1
        for value in algebras:
            product_dimension *= value.dimension
        if product_dimension != ambient.dimension:
            continue
        pairwise_ok = True
        for left_index, right_index in itertools.combinations(range(len(partition)), 2):
            if any(
                not matrices_commute(representatives[left], representatives[right])
                for left in partition[left_index]
                for right in partition[right_index]
            ):
                pairwise_ok = False
                break
            if intersection_dimension(algebras[left_index], algebras[right_index]) != 1:
                pairwise_ok = False
                break
        if not pairwise_ok:
            continue
        valid.append(
            Factorization(
                blocks=partition,
                algebra_dimensions=tuple(value.dimension for value in algebras),
            )
        )

    maximum_blocks = max((len(value.blocks) for value in valid), default=0)
    finest = tuple(value for value in valid if len(value.blocks) == maximum_blocks)

    lattices = []
    finest_atom_algebras: list[Tuple[AlgebraBasis, ...]] = []
    for factorization_index, factorization in enumerate(finest):
        atom_algebras = tuple(algebra_for(block) for block in factorization.blocks)
        finest_atom_algebras.append(atom_algebras)
        local_objects = []
        object_algebras = []
        atom_count = len(factorization.blocks)
        for subset_size in range(1, atom_count):
            for atom_subset in itertools.combinations(range(atom_count), subset_size):
                class_indices = tuple(
                    index
                    for atom_index in atom_subset
                    for index in factorization.blocks[atom_index]
                )
                algebra = algebra_for(class_indices)
                attached_records = tuple(
                    witness.handle
                    for witness, result in zip(dataset.records, record_results)
                    if result.passes_w3_control and record_lives_in_algebra(witness, algebra)
                )
                local_objects.append(
                    LocalObject(atom_subset, algebra.dimension, attached_records)
                )
                object_algebras.append(algebra)
        pair_overlaps = []
        for left, right in itertools.combinations(range(len(local_objects)), 2):
            atoms = tuple(sorted(set(local_objects[left].atoms) & set(local_objects[right].atoms)))
            if not atoms:
                continue
            class_indices = tuple(
                index
                for atom_index in atoms
                for index in factorization.blocks[atom_index]
            )
            overlap_algebra = algebra_for(class_indices)
            measured_dimension = intersection_dimension(
                object_algebras[left], object_algebras[right]
            )
            if measured_dimension != overlap_algebra.dimension:
                raise AssertionError("derived atom meet disagrees with algebra intersection")
            pair_overlaps.append(OverlapRow((left, right), atoms, overlap_algebra.dimension))
        triple_overlaps = []
        for first, second, third in itertools.combinations(range(len(local_objects)), 3):
            atoms = tuple(
                sorted(
                    set(local_objects[first].atoms)
                    & set(local_objects[second].atoms)
                    & set(local_objects[third].atoms)
                )
            )
            if not atoms:
                continue
            class_indices = tuple(
                index
                for atom_index in atoms
                for index in factorization.blocks[atom_index]
            )
            overlap_algebra = algebra_for(class_indices)
            pair_atoms = tuple(
                sorted(set(local_objects[first].atoms) & set(local_objects[second].atoms))
            )
            pair_classes = tuple(
                index
                for atom_index in pair_atoms
                for index in factorization.blocks[atom_index]
            )
            pair_algebra = algebra_for(pair_classes)
            measured_dimension = intersection_dimension(
                pair_algebra, object_algebras[third]
            )
            if measured_dimension != overlap_algebra.dimension:
                raise AssertionError("derived atom triple meet disagrees with algebra intersection")
            triple_overlaps.append(
                OverlapRow((first, second, third), atoms, overlap_algebra.dimension)
            )
        lattices.append(
            LocalLattice(
                factorization_index=factorization_index,
                objects=tuple(local_objects),
                pair_overlaps=tuple(pair_overlaps),
                triple_overlaps=tuple(triple_overlaps),
            )
        )

    actions = effective_presentation_group(dataset)
    groupoid_arrows = []
    for action_index, action in enumerate(actions):
        support_image = conjugate_by(action, support)
        if support_image != support:
            continue
        for source_index, source_atoms in enumerate(finest_atom_algebras):
            transformed = tuple(algebra_conjugate(action, algebra) for algebra in source_atoms)
            for target_index, target_atoms in enumerate(finest_atom_algebras):
                mapping = []
                unused = set(range(len(target_atoms)))
                for algebra in transformed:
                    match = next(
                        (
                            index
                            for index in sorted(unused)
                            if span_equal(algebra, target_atoms[index])
                        ),
                        None,
                    )
                    if match is None:
                        mapping = []
                        break
                    mapping.append(match)
                    unused.remove(match)
                if mapping and not unused:
                    groupoid_arrows.append(
                        GroupoidArrow(action_index, source_index, target_index, tuple(mapping))
                    )

    diagnostics = []
    if not finest:
        diagnostics.append("no nontrivial independently addressable factorization")
    elif len(finest) > 1:
        diagnostics.append("multiple finest factorizations retained")
    else:
        diagnostics.append("one finest factorization up to returned presentation actions")
    if record_results and not all(value.passes_w3_control for value in record_results):
        diagnostics.append("one or more frozen W3 witnesses failed")

    return LocalizationResult(
        dataset_handle=dataset.handle,
        accessible_dimension=accessible_dimension,
        intervention_classes=classes,
        ambient_algebra_dimension=ambient.dimension,
        partitions_examined=partitions_examined,
        valid_factorizations=tuple(valid),
        finest_factorizations=finest,
        lattices=tuple(lattices),
        groupoid_arrows=tuple(groupoid_arrows),
        record_results=record_results,
        diagnostics=tuple(diagnostics),
    )


# ---------------------------------------------------------------------------
# Public calibration only — no main fixture or expected L0 overlap truth
# ---------------------------------------------------------------------------


def normalized_superposition(left: Vector, right: Vector, phase: Q8 = ONE) -> Vector:
    return vscale(INV_SQRT2, vadd(left, vscale(phase, right)))


def tomography_vectors(dimension: int) -> Tuple[Vector, ...]:
    basis = tuple(basis_vector(dimension, index) for index in range(dimension))
    additions = []
    for left, right in itertools.combinations(range(dimension), 2):
        additions.append(normalized_superposition(basis[left], basis[right], ONE))
        additions.append(normalized_superposition(basis[left], basis[right], I))
    return basis + tuple(additions)


def calibration_dataset(encoding: Optional[Matrix] = None) -> OperationalDataset:
    x = matrix(((0, 1), (1, 0)))
    z = matrix(((1, 0), (0, -1)))
    unit2 = identity(2)
    operations = (
        kron(x, unit2),
        kron(z, unit2),
        kron(unit2, x),
        kron(unit2, z),
    )
    preparations = tomography_vectors(4)
    probes = tomography_vectors(4)
    if encoding is not None:
        if not is_unitary(encoding):
            raise ValueError("calibration encoding must be unitary")
        operations = tuple(conjugate_by(encoding, value) for value in operations)
        preparations = tuple(mv(encoding, value) for value in preparations)
        probes = tuple(mv(encoding, value) for value in probes)
    return OperationalDataset(
        handle="public-encoded-calibration" if encoding is not None else "public-calibration",
        dimension=4,
        preparations=preparations,
        interventions=tuple(Operation(f"o{index}", value) for index, value in enumerate(operations)),
        contexts=(Context("c0", identity(4), identity(4)),),
        probes=tuple(Probe(f"p{index}", value) for index, value in enumerate(probes)),
        support_actions=operations,
        presentation_actions=(identity(4),),
    )


def irreducible_calibration_dataset() -> OperationalDataset:
    shift = matrix(
        (
            (0, 0, 0, 1),
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
        )
    )
    phase = matrix(
        (
            (1, 0, 0, 0),
            (0, -1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
        )
    )
    probes = tomography_vectors(4)
    return OperationalDataset(
        handle="public-irreducible-calibration",
        dimension=4,
        preparations=probes,
        interventions=(Operation("o0", shift), Operation("o1", phase)),
        contexts=(Context("c0", identity(4), identity(4)),),
        probes=tuple(Probe(f"p{index}", value) for index, value in enumerate(probes)),
        support_actions=(shift, phase),
        presentation_actions=(identity(4),),
    )


def public_record_witness() -> RecordWitness:
    unit2 = identity(2)
    p0 = matrix(((1, 0), (0, 0)))
    p1 = matrix(((0, 0), (0, 1)))
    h = matrix(((INV_SQRT2, INV_SQRT2), (INV_SQRT2, -INV_SQRT2)))
    cnot = matrix(
        (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 1),
            (0, 0, 1, 0),
        )
    )
    input_state = mv(kron(h, unit2), basis_vector(4, 0))
    return RecordWitness(
        handle="public-record-calibration",
        preparations=(input_state,),
        alternative_projectors=(kron(p0, unit2), kron(p1, unit2)),
        cut_record_projectors=(kron(unit2, p0), kron(unit2, p1)),
        availability_probes=tuple(projector(basis_vector(4, index)) for index in range(4)),
        write=cnot,
        preserving=(identity(4),),
        erasing=(mmul(kron(h, unit2), cnot),),
        no_write=identity(4),
    )


def self_test() -> Mapping[str, object]:
    if ZETA ** 4 != -ONE or ZETA ** 8 != ONE:
        raise AssertionError("Q(zeta_8) relation failed")
    if INV_SQRT2 * INV_SQRT2 != Q8(Fraction(1, 2)):
        raise AssertionError("exact inverse-square-root relation failed")
    inverse_cases = 0
    for coefficients in itertools.product(range(-1, 2), repeat=4):
        value = Q8(*(Fraction(entry) for entry in coefficients))
        if value:
            inverse_cases += 1
            if value * value.inverse() != ONE:
                raise AssertionError("Q(zeta_8) inverse test failed")
    bell_counts = tuple(sum(1 for _ in set_partitions(size)) for size in range(1, 9))
    if bell_counts != (1, 2, 5, 15, 52, 203, 877, 4140):
        raise AssertionError("set-partition census failed")
    cnot = matrix(
        (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 1),
            (0, 0, 1, 0),
        )
    )
    complex_encoding = mmul(
        cnot,
        kron(matrix(((1, 0), (0, ZETA))), identity(2)),
    )
    plain = analyze_localization(calibration_dataset())
    encoded = analyze_localization(calibration_dataset(cnot))
    complex_encoded = analyze_localization(calibration_dataset(complex_encoding))
    plain_dataset = calibration_dataset()
    reordered_dataset = OperationalDataset(
        handle="public-reordered-calibration",
        dimension=plain_dataset.dimension,
        preparations=tuple(reversed(plain_dataset.preparations)),
        interventions=tuple(reversed(plain_dataset.interventions)),
        contexts=plain_dataset.contexts,
        probes=tuple(reversed(plain_dataset.probes)),
        support_actions=tuple(reversed(plain_dataset.support_actions)),
        presentation_actions=plain_dataset.presentation_actions,
    )
    reordered = analyze_localization(reordered_dataset)
    if len(plain.finest_factorizations) != 1:
        raise AssertionError("public calibration did not have one finest factorization")
    if tuple(sorted(plain.finest_factorizations[0].algebra_dimensions)) != (4, 4):
        raise AssertionError("public calibration factor dimensions changed")
    if plain.structural_signature() != encoded.structural_signature():
        raise AssertionError("encoded public presentation changed localization signature")
    if plain.structural_signature() != complex_encoded.structural_signature():
        raise AssertionError("complex encoded presentation changed localization signature")
    if plain.structural_signature() != reordered.structural_signature():
        raise AssertionError("opaque generator or access-table order changed localization signature")
    irreducible = analyze_localization(irreducible_calibration_dataset())
    if irreducible.ambient_algebra_dimension != 16:
        raise AssertionError("public irreducible calibration does not generate M4")
    if irreducible.has_nontrivial_localization:
        raise AssertionError("public irreducible calibration was falsely split")
    record_result = evaluate_record_witness(public_record_witness(), identity(4), 4)
    if not record_result.passes_w3_control:
        raise AssertionError("public W3 write/preserve/erase calibration failed")
    return {
        "api": ESTIMATOR_API_VERSION,
        "pin_commit": PIN_COMMIT,
        "pin_sha256": PIN_SHA256,
        "scalar_ring": "Q(zeta_8)",
        "inverse_cases": inverse_cases,
        "bell_counts": list(bell_counts),
        "plain_signature": plain.structural_signature(),
        "encoded_signature": encoded.structural_signature(),
        "complex_encoded_signature": complex_encoded.structural_signature(),
        "reordered_signature": reordered.structural_signature(),
        "irreducible_localization": irreducible.has_nontrivial_localization,
        "record_calibration": {
            "occurrence": record_result.occurrence,
            "preserving_available": list(record_result.preserving_available),
            "erasing_available": list(record_result.erasing_available),
            "erasing_cross_coherence": list(record_result.erasing_cross_coherence),
            "no_write_occurrence": record_result.no_write_occurrence,
        },
        "main_fixture_present": False,
        "causal_object_present": False,
    }


if __name__ == "__main__":
    print(json.dumps(self_test(), indent=2, sort_keys=True))
