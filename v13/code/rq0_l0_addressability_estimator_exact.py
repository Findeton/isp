#!/usr/bin/env python3
"""Generic exact estimator for the RQ0-L0 addressability repair.

This file is the estimator-before-truth surface required by the strict repair
pin.  It contains no main fixture, expected atlas, hidden factor labels,
causal object, geometry, field, or gravity object.

The estimator acts on a finite operational composition object.  Primitive
generator handles are presentation data only: factorization is computed from
the complete quotient composition table plus its exact amplitude
representation.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Callable, Dict, FrozenSet, Hashable, Iterable, Iterator, Mapping, Optional, Sequence, Tuple


ESTIMATOR_API_VERSION = "rq0-l0-addressability-v3"
MAX_CARRIER_DIMENSION = 64
MAX_OPERATION_CLASSES = 216
MAX_COMPOSITION_ROWS = 46_656
MAX_CANDIDATE_SUBOBJECTS = 50_000
MAX_AUTOMORPHISM_PERMUTATIONS = 100_000


# ---------------------------------------------------------------------------
# Exact Q(zeta_24) arithmetic
# Phi_24(x) = x^8 - x^4 + 1.
# ---------------------------------------------------------------------------


def _fraction(value: object) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    raise TypeError(f"cannot coerce {type(value).__name__} to Fraction")


def _reduce_polynomial(coefficients: Sequence[Fraction]) -> Tuple[Fraction, ...]:
    work = list(coefficients)
    if len(work) < 8:
        work.extend(Fraction(0) for _ in range(8 - len(work)))
    for degree in range(len(work) - 1, 7, -1):
        coefficient = work[degree]
        if not coefficient:
            continue
        # x^degree = x^(degree-4) - x^(degree-8) modulo Phi_24.
        work[degree - 4] += coefficient
        work[degree - 8] -= coefficient
        work[degree] = Fraction(0)
    return tuple(work[index] for index in range(8))


@dataclass(frozen=True)
class Q24:
    coefficients: Tuple[Fraction, ...]

    def __init__(self, *coefficients: object) -> None:
        if len(coefficients) == 1 and isinstance(coefficients[0], (tuple, list)):
            values = tuple(_fraction(value) for value in coefficients[0])
        else:
            values = tuple(_fraction(value) for value in coefficients)
        object.__setattr__(self, "coefficients", _reduce_polynomial(values))

    @classmethod
    def coerce(cls, value: object) -> "Q24":
        if isinstance(value, Q24):
            return value
        if isinstance(value, (int, Fraction)):
            return cls(value)
        raise TypeError(f"cannot coerce {type(value).__name__} to Q24")

    def __add__(self, other: object) -> "Q24":
        right = self.coerce(other)
        return Q24(tuple(left + value for left, value in zip(self.coefficients, right.coefficients)))

    def __radd__(self, other: object) -> "Q24":
        return self + other

    def __neg__(self) -> "Q24":
        return Q24(tuple(-value for value in self.coefficients))

    def __sub__(self, other: object) -> "Q24":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "Q24":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "Q24":
        right = self.coerce(other)
        work = [Fraction(0) for _ in range(15)]
        for left_degree, left in enumerate(self.coefficients):
            if not left:
                continue
            for right_degree, value in enumerate(right.coefficients):
                if value:
                    work[left_degree + right_degree] += left * value
        return Q24(tuple(work))

    def __rmul__(self, other: object) -> "Q24":
        return self * other

    def __truediv__(self, other: object) -> "Q24":
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other: object) -> "Q24":
        return self.coerce(other) / self

    def __pow__(self, exponent: int) -> "Q24":
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        result = ONE
        base = self
        power = exponent
        while power:
            if power & 1:
                result *= base
            base *= base
            power //= 2
        return result

    def __bool__(self) -> bool:
        return any(self.coefficients)

    def is_zero(self) -> bool:
        return not self

    def conjugate(self) -> "Q24":
        return sum(
            (Q24(coefficient) * (ZETA ** ((24 - degree) % 24))
             for degree, coefficient in enumerate(self.coefficients)),
            ZERO,
        )

    def is_real(self) -> bool:
        return self == self.conjugate()

    def inverse(self) -> "Q24":
        if not self:
            raise ZeroDivisionError("division by zero in Q(zeta_24)")
        return _inverse_coefficients(self.coefficients)

    def sort_key(self) -> Tuple[Tuple[int, int], ...]:
        return tuple((value.numerator, value.denominator) for value in self.coefficients)

    def render(self) -> str:
        names = ("1", "z", "z^2", "z^3", "z^4", "z^5", "z^6", "z^7")
        terms = []
        for coefficient, name in zip(self.coefficients, names):
            if not coefficient:
                continue
            terms.append(f"({coefficient})*{name}")
        return "0" if not terms else " + ".join(terms)


ZERO = Q24(0)
ONE = Q24(1)
ZETA = Q24(0, 1)
I = ZETA ** 6
SQRT2 = ZETA ** 3 - ZETA ** 9
INV_SQRT2 = SQRT2 * Fraction(1, 2)
SQRT3 = ZETA ** 2 + ZETA ** 22
MU24_POWERS = tuple(ZETA ** exponent for exponent in range(24))


def _solve_fraction_system(
    matrix: Sequence[Sequence[Fraction]],
    target: Sequence[Fraction],
) -> Tuple[Fraction, ...]:
    size = len(matrix)
    augmented = [list(row) + [target[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if augmented[row][column]), None)
        if pivot is None:
            raise ZeroDivisionError("singular multiplication map in Q(zeta_24)")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    left - factor * right
                    for left, right in zip(augmented[row], augmented[column])
                ]
    return tuple(augmented[index][-1] for index in range(size))


@lru_cache(maxsize=None)
def _inverse_coefficients(coefficients: Tuple[Fraction, ...]) -> Q24:
    value = Q24(coefficients)
    columns = []
    for degree in range(8):
        product = value * (ZETA ** degree)
        columns.append(product.coefficients)
    matrix = tuple(
        tuple(columns[column][row] for column in range(8))
        for row in range(8)
    )
    solution = _solve_fraction_system(matrix, (Fraction(1),) + (Fraction(0),) * 7)
    result = Q24(solution)
    if value * result != ONE:
        raise AssertionError("Q(zeta_24) inverse failed exact verification")
    return result


# ---------------------------------------------------------------------------
# Exact vectors, matrices, spans, and star algebras
# ---------------------------------------------------------------------------


Vector = Tuple[Q24, ...]
Matrix = Tuple[Tuple[Q24, ...], ...]


def q(value: object) -> Q24:
    return Q24.coerce(value)


def vector(values: Sequence[object]) -> Vector:
    return tuple(q(value) for value in values)


def matrix(rows: Sequence[Sequence[object]]) -> Matrix:
    result = tuple(tuple(q(value) for value in row) for row in rows)
    if result and any(len(row) != len(result[0]) for row in result):
        raise ValueError("ragged matrix")
    return result


def shape(value: Matrix) -> Tuple[int, int]:
    return (len(value), len(value[0]) if value else 0)


def zero_matrix(rows: int, columns: int) -> Matrix:
    return tuple(tuple(ZERO for _ in range(columns)) for _ in range(rows))


def identity(dimension: int) -> Matrix:
    return tuple(
        tuple(ONE if row == column else ZERO for column in range(dimension))
        for row in range(dimension)
    )


def basis_vector(dimension: int, index: int) -> Vector:
    return tuple(ONE if entry == index else ZERO for entry in range(dimension))


def madd(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def msub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def mscale(scalar: object, value: Matrix) -> Matrix:
    factor = q(scalar)
    return tuple(tuple(factor * entry for entry in row) for row in value)


def mmul(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_columns = shape(left)
    right_rows, right_columns = shape(right)
    if left_columns != right_rows:
        raise ValueError("matrix product shape mismatch")
    result = [[ZERO for _ in range(right_columns)] for _ in range(left_rows)]
    for row in range(left_rows):
        for middle, left_entry in enumerate(left[row]):
            if not left_entry:
                continue
            for column, right_entry in enumerate(right[middle]):
                if right_entry:
                    result[row][column] = (
                        result[row][column] + left_entry * right_entry
                    )
    return tuple(tuple(row) for row in result)


def mv(value: Matrix, state: Vector) -> Vector:
    rows, columns = shape(value)
    if columns != len(state):
        raise ValueError("matrix-vector shape mismatch")
    return tuple(
        sum(
            (
                value[row][column] * state[column]
                for column in range(columns)
                if value[row][column] and state[column]
            ),
            ZERO,
        )
        for row in range(rows)
    )


def adjoint(value: Matrix) -> Matrix:
    rows, columns = shape(value)
    return tuple(
        tuple(value[row][column].conjugate() for row in range(rows))
        for column in range(columns)
    )


def inner(left: Vector, right: Vector) -> Q24:
    return sum((a.conjugate() * b for a, b in zip(left, right)), ZERO)


def kron(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_columns = shape(left)
    right_rows, right_columns = shape(right)
    return tuple(
        tuple(
            left[left_row][left_column] * right[right_row][right_column]
            for left_column in range(left_columns)
            for right_column in range(right_columns)
        )
        for left_row in range(left_rows)
        for right_row in range(right_rows)
    )


def vkron(left: Vector, right: Vector) -> Vector:
    return tuple(a * b for a in left for b in right)


def direct_sum(left: Matrix, right: Matrix) -> Matrix:
    left_size = len(left)
    right_size = len(right)
    return tuple(
        tuple(
            left[row][column]
            if row < left_size and column < left_size
            else right[row - left_size][column - left_size]
            if row >= left_size and column >= left_size
            else ZERO
            for column in range(left_size + right_size)
        )
        for row in range(left_size + right_size)
    )


def is_zero_matrix(value: Matrix) -> bool:
    return all(not entry for row in value for entry in row)


def is_unitary(value: Matrix) -> bool:
    rows, columns = shape(value)
    return rows == columns and mmul(adjoint(value), value) == identity(rows)


def is_projector(value: Matrix) -> bool:
    return value == adjoint(value) and mmul(value, value) == value


def matrices_commute(left: Matrix, right: Matrix) -> bool:
    return mmul(left, right) == mmul(right, left)


def conjugate_by(action: Matrix, value: Matrix) -> Matrix:
    return mmul(mmul(action, value), adjoint(action))


def matrix_inverse(value: Matrix) -> Matrix:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("matrix inverse requires a square matrix")
    augmented = [list(value[row]) + list(identity(rows)[row]) for row in range(rows)]
    for column in range(rows):
        pivot = next((row for row in range(column, rows) if augmented[row][column]), None)
        if pivot is None:
            raise ZeroDivisionError("singular exact matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column].inverse()
        augmented[column] = [scale * entry for entry in augmented[column]]
        for row in range(rows):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    left - factor * right
                    for left, right in zip(augmented[row], augmented[column])
                ]
    result = tuple(tuple(row[rows:]) for row in augmented)
    if mmul(value, result) != identity(rows):
        raise AssertionError("exact matrix inverse failed verification")
    return result


def flatten(value: Matrix) -> Vector:
    return tuple(entry for row in value for entry in row)


def unflatten(value: Vector, dimension: int) -> Matrix:
    return tuple(
        tuple(value[row * dimension + column] for column in range(dimension))
        for row in range(dimension)
    )


def canonical_mu24_phase_reference(value: Matrix) -> Matrix:
    """Slow executable specification retained for public equivalence tests."""

    candidates = tuple(mscale(ZETA ** exponent, value) for exponent in range(24))
    return min(candidates, key=lambda candidate: tuple(entry.sort_key() for entry in flatten(candidate)))


def canonical_mu24_phase(value: Matrix) -> Matrix:
    """Exact lexicographic mu_24 quotient without materializing 24 matrices.

    Lexicographic minimization may discard phase candidates as soon as their
    scaled coefficient tuple exceeds the current minimum at the first entry
    where they differ.  This is exactly the reference definition above, not a
    heuristic or a truth-dependent shortcut.
    """

    candidates = tuple(range(24))
    for entry in flatten(value):
        if not entry:
            continue
        keys = tuple(
            (exponent, (MU24_POWERS[exponent] * entry).sort_key())
            for exponent in candidates
        )
        minimum = min(key for _, key in keys)
        candidates = tuple(exponent for exponent, key in keys if key == minimum)
        if len(candidates) == 1:
            break
    exponent = candidates[0]
    return mscale(ZETA ** exponent, value)


@dataclass
class SparseSpan:
    width: int
    rows: Dict[int, Vector]

    def __init__(self, width: int) -> None:
        self.width = width
        self.rows = {}

    def reduce(self, candidate: Vector) -> Vector:
        work = list(candidate)
        for pivot in sorted(self.rows):
            factor = work[pivot]
            if factor:
                row = self.rows[pivot]
                work = [left - factor * right for left, right in zip(work, row)]
        return tuple(work)

    def add(self, candidate: Vector) -> bool:
        work = self.reduce(candidate)
        pivot = next((index for index, value in enumerate(work) if value), None)
        if pivot is None:
            return False
        inverse = work[pivot].inverse()
        normalized = tuple(inverse * value for value in work)
        for old_pivot, row in tuple(self.rows.items()):
            factor = row[pivot]
            if factor:
                self.rows[old_pivot] = tuple(
                    left - factor * right for left, right in zip(row, normalized)
                )
        self.rows[pivot] = normalized
        return True

    @property
    def dimension(self) -> int:
        return len(self.rows)

    def basis(self) -> Tuple[Vector, ...]:
        return tuple(self.rows[pivot] for pivot in sorted(self.rows))

    def contains(self, candidate: Vector) -> bool:
        return not any(self.reduce(candidate))


@dataclass(frozen=True)
class AlgebraBasis:
    dimension: int
    carrier_dimension: int
    vectors: Tuple[Vector, ...]

    def contains_matrix(self, value: Matrix) -> bool:
        span = SparseSpan(self.carrier_dimension * self.carrier_dimension)
        for row in self.vectors:
            span.add(row)
        return span.contains(flatten(value))

    def coordinates(self, value: Matrix) -> Tuple[Q24, ...]:
        target = flatten(value)
        count = len(self.vectors)
        augmented = [list(self.vectors[column]) for column in range(count)]
        # Solve by augmenting the row span with tagged coefficient vectors.
        width = len(target)
        tagged = SparseSpan(width + count)
        for index, row in enumerate(augmented):
            tagged.add(tuple(row) + tuple(ONE if index == j else ZERO for j in range(count)))
        reduced = tagged.reduce(target + (ZERO,) * count)
        if any(reduced[:width]):
            raise ValueError("matrix is not in target algebra")
        return tuple(-value for value in reduced[width:])


def algebra_from_matrices(matrices: Iterable[Matrix], carrier_dimension: int) -> AlgebraBasis:
    span = SparseSpan(carrier_dimension * carrier_dimension)
    for value in matrices:
        span.add(flatten(value))
    return AlgebraBasis(span.dimension, carrier_dimension, span.basis())


def algebra_span_union(left: AlgebraBasis, right: AlgebraBasis) -> AlgebraBasis:
    if left.carrier_dimension != right.carrier_dimension:
        raise ValueError("algebra carrier mismatch")
    span = SparseSpan(left.carrier_dimension * left.carrier_dimension)
    for row in left.vectors + right.vectors:
        span.add(row)
    return AlgebraBasis(span.dimension, left.carrier_dimension, span.basis())


def algebra_intersection_dimension(left: AlgebraBasis, right: AlgebraBasis) -> int:
    union = algebra_span_union(left, right)
    return left.dimension + right.dimension - union.dimension


def algebra_equal(left: AlgebraBasis, right: AlgebraBasis) -> bool:
    if left.carrier_dimension != right.carrier_dimension or left.dimension != right.dimension:
        return False
    return all(right.contains_matrix(unflatten(row, left.carrier_dimension)) for row in left.vectors)


# ---------------------------------------------------------------------------
# Typed operational datasets and quotient composition objects
# ---------------------------------------------------------------------------


IMPLEMENTED = "IMPLEMENTED"
UNAVAILABLE = "UNAVAILABLE"
COLLAPSED = "COLLAPSED"
COMPOSITION_STATUSES = frozenset((IMPLEMENTED, UNAVAILABLE, COLLAPSED))


@dataclass(frozen=True)
class Operation:
    handle: str
    amplitude: Matrix
    boundary_type: str = "end"
    independently_selectable: bool = True


@dataclass(frozen=True)
class CompositionRow:
    left: str
    right: str
    context: str
    status: str
    result: Optional[str]


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
    operations: Tuple[Operation, ...]
    composition_rows: Tuple[CompositionRow, ...]
    generator_handles: Tuple[str, ...]
    preparations: Tuple[Vector, ...] = ()
    probes: Tuple[Vector, ...] = ()
    records: Tuple[RecordWitness, ...] = ()
    gauge_actions: Tuple[Matrix, ...] = ()
    access_declaration: str = "POSTULATE: finite exact amplitude tomography and composition access"
    gauge_declaration: str = "configuration relabelling x finite mu_24 boundary phase"


class InvalidDataset(ValueError):
    pass


class AccessUnderdetermined(ValueError):
    pass


def amplitude_signature(value: Matrix) -> Tuple[Tuple[Tuple[int, int], ...], ...]:
    """Canonical full-process tomography adapter modulo a global mu_24 phase."""

    canonical = canonical_mu24_phase(value)
    return tuple(entry.sort_key() for entry in flatten(canonical))


def _record_actions(records: Sequence[RecordWitness]) -> Tuple[Matrix, ...]:
    return tuple(
        action
        for witness in records
        for action in (
            (witness.write, witness.no_write)
            + witness.preserving
            + witness.erasing
        )
    )


def reachable_support(dataset: OperationalDataset) -> Tuple[Matrix, int]:
    if dataset.preparations:
        preparations = dataset.preparations
    else:
        preparations = tuple(basis_vector(dataset.dimension, index) for index in range(dataset.dimension))
    actions = tuple(operation.amplitude for operation in dataset.operations) + _record_actions(dataset.records)
    span = SparseSpan(dataset.dimension)
    frontier: list[Vector] = []
    for preparation in preparations:
        if span.add(preparation):
            frontier.append(preparation)
    while frontier:
        state = frontier.pop(0)
        for action in actions:
            candidate = mv(action, state)
            if span.add(candidate):
                frontier.append(candidate)
    basis = span.basis()
    if not basis:
        raise InvalidDataset("reachable support is empty")
    basis_matrix = tuple(
        tuple(basis[column][row] for column in range(len(basis)))
        for row in range(dataset.dimension)
    )
    gram = mmul(adjoint(basis_matrix), basis_matrix)
    support = mmul(mmul(basis_matrix, matrix_inverse(gram)), adjoint(basis_matrix))
    if not is_projector(support):
        raise AssertionError("reachable support is not an exact projector")
    complement = msub(identity(dataset.dimension), support)
    for action in actions:
        if not is_zero_matrix(mmul(complement, mmul(action, support))):
            raise InvalidDataset("reachable support is not closed under admitted actions")
    return support, len(basis)


def accessible_amplitude(support: Matrix, value: Matrix) -> Matrix:
    if support == identity(len(support)):
        return value
    return mmul(mmul(support, value), support)


def accessible_signature(support: Matrix, value: Matrix) -> Tuple[Tuple[Tuple[int, int], ...], ...]:
    return amplitude_signature(accessible_amplitude(support, value))


def validate_projector_resolution(
    projectors: Sequence[Matrix],
    dimension: int,
    label: str,
) -> None:
    if not projectors:
        raise InvalidDataset(f"{label} projector family is empty")
    unit = identity(dimension)
    for index, value in enumerate(projectors):
        if shape(value) != (dimension, dimension) or not is_projector(value):
            raise InvalidDataset(f"{label}.{index} is not an exact projector")
    for left, right in itertools.combinations(projectors, 2):
        if not is_zero_matrix(mmul(left, right)):
            raise InvalidDataset(f"{label} projectors are not orthogonal")
    total = zero_matrix(dimension, dimension)
    for value in projectors:
        total = madd(total, value)
    if total != unit:
        raise InvalidDataset(f"{label} projectors do not resolve the unit")


def validate_dataset(dataset: OperationalDataset) -> None:
    if not 1 < dataset.dimension <= MAX_CARRIER_DIMENSION:
        raise InvalidDataset("carrier dimension violates the frozen cap")
    if not dataset.operations:
        raise InvalidDataset("operation family is empty")
    if len(dataset.operations) > MAX_OPERATION_CLASSES:
        raise InvalidDataset("raw operation count exceeds the frozen cap")
    if len(dataset.composition_rows) > MAX_COMPOSITION_ROWS:
        raise InvalidDataset("composition row count exceeds the frozen cap")
    handles = tuple(operation.handle for operation in dataset.operations)
    if len(set(handles)) != len(handles):
        raise InvalidDataset("operation handles are not unique")
    operation_map = {operation.handle: operation for operation in dataset.operations}
    for operation in dataset.operations:
        if shape(operation.amplitude) != (dataset.dimension, dataset.dimension):
            raise InvalidDataset(f"operation {operation.handle} has the wrong carrier")
        if not is_unitary(operation.amplitude):
            raise InvalidDataset(f"operation {operation.handle} is not unitary")
    if len(set(dataset.generator_handles)) != len(dataset.generator_handles):
        raise InvalidDataset("generator handles are duplicated")
    for handle in dataset.generator_handles:
        if handle not in operation_map:
            raise InvalidDataset(f"generator {handle} is not an admitted operation")
        if not operation_map[handle].independently_selectable:
            raise InvalidDataset(f"generator {handle} is not independently selectable")
    expected_pairs = {(left, right) for left in handles for right in handles}
    observed_pairs = {(row.left, row.right) for row in dataset.composition_rows}
    if len(observed_pairs) != len(dataset.composition_rows):
        raise InvalidDataset("composition table contains duplicate ordered rows")
    if observed_pairs != expected_pairs:
        raise InvalidDataset("composition table is not flat and complete over raw handles")
    for row in dataset.composition_rows:
        if row.left not in operation_map or row.right not in operation_map:
            raise InvalidDataset("composition row references an unknown operation")
        if row.status not in COMPOSITION_STATUSES:
            raise InvalidDataset(f"unknown composition status {row.status}")
        if row.status == UNAVAILABLE:
            if row.result is not None:
                raise InvalidDataset("unavailable composition row supplies a result")
            continue
        if row.result not in operation_map:
            raise InvalidDataset("implemented/collapsed composition row lacks a result")
    for index, state in enumerate(dataset.preparations):
        if len(state) != dataset.dimension or not inner(state, state):
            raise InvalidDataset(f"preparation {index} is invalid")
    for index, state in enumerate(dataset.probes):
        if len(state) != dataset.dimension or not inner(state, state):
            raise InvalidDataset(f"probe {index} is invalid")
    for index, action in enumerate(dataset.gauge_actions):
        if shape(action) != (dataset.dimension, dataset.dimension) or not is_unitary(action):
            raise InvalidDataset(f"gauge action {index} is invalid")


@dataclass(frozen=True)
class OperationClass:
    members: Tuple[str, ...]
    boundary_type: str
    signature: Tuple[Tuple[Tuple[int, int], ...], ...]
    representative: Matrix
    independently_selectable: bool


@dataclass(frozen=True)
class QuotientCompositionRow:
    status: str
    result: Optional[int]


@dataclass(frozen=True)
class CompositionObject:
    classes: Tuple[OperationClass, ...]
    table: Tuple[Tuple[QuotientCompositionRow, ...], ...]
    identity: Optional[int]
    generator_classes: Tuple[int, ...]
    congruence_verified: bool
    total_implemented: bool
    unique_product_amplitudes: int
    diagnostics: Tuple[str, ...]

    @property
    def size(self) -> int:
        return len(self.classes)

    def product(self, left: int, right: int) -> int:
        row = self.table[left][right]
        if row.status != IMPLEMENTED or row.result is None:
            raise AccessUnderdetermined("requested composition is not faithfully implemented")
        return row.result


def build_composition_object(
    dataset: OperationalDataset,
    precomputed_support: Optional[Matrix] = None,
) -> CompositionObject:
    validate_dataset(dataset)
    support = precomputed_support
    if support is None:
        support, _ = reachable_support(dataset)
    elif shape(support) != (dataset.dimension, dataset.dimension) or not is_projector(support):
        raise InvalidDataset("precomputed accessible support is mistyped")
    operation_map = {operation.handle: operation for operation in dataset.operations}
    accessible_by_handle = {
        operation.handle: accessible_amplitude(support, operation.amplitude)
        for operation in dataset.operations
    }
    signature_by_handle = {
        handle: amplitude_signature(value)
        for handle, value in accessible_by_handle.items()
    }
    grouped: Dict[Tuple[str, Tuple[Tuple[Tuple[int, int], ...], ...]], list[Operation]] = {}
    for operation in dataset.operations:
        key = (operation.boundary_type, signature_by_handle[operation.handle])
        grouped.setdefault(key, []).append(operation)
    ordered_keys = sorted(grouped, key=lambda item: (item[0], item[1]))
    classes = []
    handle_to_class: Dict[str, int] = {}
    for class_index, key in enumerate(ordered_keys):
        members = tuple(sorted(grouped[key], key=lambda value: value.handle))
        operation_class = OperationClass(
            members=tuple(value.handle for value in members),
            boundary_type=key[0],
            signature=key[1],
            representative=canonical_mu24_phase(accessible_by_handle[members[0].handle]),
            independently_selectable=any(value.independently_selectable for value in members),
        )
        classes.append(operation_class)
        for member in members:
            handle_to_class[member.handle] = class_index
    if len(classes) > MAX_OPERATION_CLASSES:
        raise InvalidDataset("quotient operation count exceeds the frozen cap")
    raw_rows = {(row.left, row.right): row for row in dataset.composition_rows}
    product_signature_cache: Dict[Matrix, Tuple[Tuple[Tuple[int, int], ...], ...]] = {}
    for row in dataset.composition_rows:
        if row.status == UNAVAILABLE:
            continue
        assert row.result is not None
        product = mmul(operation_map[row.left].amplitude, operation_map[row.right].amplitude)
        accessible_product = accessible_amplitude(support, product)
        if accessible_product not in product_signature_cache:
            product_signature_cache[accessible_product] = amplitude_signature(accessible_product)
        if product_signature_cache[accessible_product] != signature_by_handle[row.result]:
            raise InvalidDataset(
                f"accessible composition amplitude law fails for ({row.left},{row.right})"
            )
    quotient_rows = []
    for left_index, left_class in enumerate(classes):
        row_values = []
        for right_index, right_class in enumerate(classes):
            observed = set()
            for left_handle in left_class.members:
                for right_handle in right_class.members:
                    row = raw_rows[(left_handle, right_handle)]
                    result_class = None if row.result is None else handle_to_class[row.result]
                    observed.add((row.context, row.status, result_class))
            contexts = {value[0] for value in observed}
            laws = {(value[1], value[2]) for value in observed}
            if len(contexts) != 1 or len(laws) != 1:
                raise AccessUnderdetermined(
                    "operational aliases are not a congruence for the composition table"
                )
            status, result = next(iter(laws))
            row_values.append(QuotientCompositionRow(status, result))
        quotient_rows.append(tuple(row_values))
    table = tuple(quotient_rows)
    identity_signature = amplitude_signature(support)
    identity_candidates = [
        index
        for index, operation_class in enumerate(classes)
        if operation_class.signature == identity_signature
    ]
    identity_index = identity_candidates[0] if len(identity_candidates) == 1 else None
    diagnostics = []
    if identity_index is None:
        diagnostics.append("no unique accessible identity class")
    else:
        for index in range(len(classes)):
            left = table[identity_index][index]
            right = table[index][identity_index]
            if (
                left.status != IMPLEMENTED
                or right.status != IMPLEMENTED
                or left.result != index
                or right.result != index
            ):
                diagnostics.append("identity composition law fails")
                identity_index = None
                break
    total_implemented = all(
        row.status == IMPLEMENTED and row.result is not None
        for table_row in table
        for row in table_row
    )
    if not total_implemented:
        diagnostics.append("composition object has unavailable or collapsed rows")
    generator_classes = tuple(sorted({handle_to_class[handle] for handle in dataset.generator_handles}))
    return CompositionObject(
        classes=tuple(classes),
        table=table,
        identity=identity_index,
        generator_classes=generator_classes,
        congruence_verified=True,
        total_implemented=total_implemented,
        unique_product_amplitudes=len(product_signature_cache),
        diagnostics=tuple(diagnostics),
    )


def composition_object_is_associative(value: CompositionObject) -> bool:
    if not value.total_implemented:
        return False
    for left in range(value.size):
        for middle in range(value.size):
            left_middle = value.product(left, middle)
            for right in range(value.size):
                if value.product(left_middle, right) != value.product(
                    left, value.product(middle, right)
                ):
                    return False
    return True


def inverse_table(value: CompositionObject) -> Tuple[int, ...]:
    if value.identity is None or not value.total_implemented:
        raise AccessUnderdetermined("composition object lacks a total identity law")
    result = []
    for element in range(value.size):
        candidates = tuple(
            candidate
            for candidate in range(value.size)
            if value.product(element, candidate) == value.identity
            and value.product(candidate, element) == value.identity
        )
        if len(candidates) != 1:
            raise AccessUnderdetermined("composition object is not a finite group at this rung")
        result.append(candidates[0])
    return tuple(result)


# ---------------------------------------------------------------------------
# Generator-independent finite direct-factor search
# ---------------------------------------------------------------------------


Subobject = FrozenSet[int]


def subgroup_generated(
    value: CompositionObject,
    seeds: Iterable[int],
    inverses: Sequence[int],
) -> Subobject:
    if value.identity is None:
        raise AccessUnderdetermined("subgroup closure requires an identity")
    current = {value.identity}
    current.update(seeds)
    current.update(inverses[element] for element in tuple(current))
    changed = True
    while changed:
        changed = False
        entries = tuple(sorted(current))
        for left in entries:
            for right in entries:
                product = value.product(left, right)
                if product not in current:
                    current.add(product)
                    current.add(inverses[product])
                    changed = True
        if len(current) > value.size:
            raise AssertionError("subgroup closure escaped the composition object")
    return frozenset(current)


def normal_closure(
    value: CompositionObject,
    seeds: Iterable[int],
    inverses: Sequence[int],
) -> Subobject:
    conjugates = set()
    for group_element in range(value.size):
        inverse = inverses[group_element]
        for seed in seeds:
            conjugates.add(value.product(value.product(group_element, seed), inverse))
    return subgroup_generated(value, conjugates, inverses)


def normal_subobjects(
    value: CompositionObject,
    inverses: Sequence[int],
) -> Tuple[Subobject, ...]:
    if value.identity is None:
        return ()
    candidates = {frozenset((value.identity,))}
    for element in range(value.size):
        candidates.add(normal_closure(value, (element,), inverses))
    changed = True
    tests = 0
    while changed:
        changed = False
        snapshot = tuple(sorted(candidates, key=lambda item: (len(item), tuple(sorted(item)))))
        for left_index, left in enumerate(snapshot):
            for right in snapshot[left_index:]:
                tests += 1
                if tests > MAX_CANDIDATE_SUBOBJECTS:
                    raise InvalidDataset("normal-subobject search exceeded the frozen cap")
                # The product HK of two normal subgroups is their subgroup
                # join.  Both inputs here are already certified normal
                # subobjects, so exhaustive pair products replace a repeated
                # conjugacy closure without changing the searched lattice.
                joined = frozenset(
                    value.product(left_entry, right_entry)
                    for left_entry in left
                    for right_entry in right
                )
                if joined not in candidates:
                    candidates.add(joined)
                    changed = True
    return tuple(sorted(candidates, key=lambda item: (len(item), tuple(sorted(item)))))


def subobjects_commute(value: CompositionObject, left: Subobject, right: Subobject) -> bool:
    return all(
        value.product(a, b) == value.product(b, a)
        for a in left
        for b in right
    )


def multiply_subobjects(
    value: CompositionObject,
    factors: Sequence[Subobject],
) -> Tuple[bool, Subobject]:
    if value.identity is None:
        return False, frozenset()
    image: Dict[int, Tuple[int, ...]] = {}
    for entries in itertools.product(*(tuple(sorted(factor)) for factor in factors)):
        product = value.identity
        for entry in entries:
            product = value.product(product, entry)
        if product in image and image[product] != entries:
            return False, frozenset(image)
        image[product] = entries
    return True, frozenset(image)


def represented_algebra(
    composition: CompositionObject,
    elements: Iterable[int],
    carrier_dimension: int,
) -> AlgebraBasis:
    return algebra_from_matrices(
        (composition.classes[index].representative for index in sorted(set(elements))),
        carrier_dimension,
    )


@dataclass(frozen=True)
class DirectFactorization:
    factors: Tuple[Subobject, ...]
    group_orders: Tuple[int, ...]
    algebra_dimensions: Tuple[int, ...]


@dataclass(frozen=True)
class AddressabilityCore:
    composition: CompositionObject
    accessible_dimension: int
    support: Matrix
    associative: bool
    inverses: Tuple[int, ...]
    normal_subobjects: Tuple[Subobject, ...]
    factorizations: Tuple[DirectFactorization, ...]
    finest_factorizations: Tuple[DirectFactorization, ...]
    candidate_tests: int
    diagnostics: Tuple[str, ...]

    @property
    def blocked_at_address(self) -> bool:
        return not self.finest_factorizations


def factorization_sort_key(value: DirectFactorization) -> Tuple[object, ...]:
    return (
        len(value.factors),
        tuple(sorted(value.group_orders)),
        tuple(tuple(sorted(factor)) for factor in value.factors),
    )


def analyze_addressability_core(dataset: OperationalDataset) -> AddressabilityCore:
    validate_dataset(dataset)
    support, accessible_dimension = reachable_support(dataset)
    composition = build_composition_object(dataset, support)
    diagnostics = list(composition.diagnostics)
    if composition.identity is None or not composition.total_implemented:
        diagnostics.append("addressability blocked by missing, unavailable, or collapsed composition")
        return AddressabilityCore(
            composition=composition,
            accessible_dimension=accessible_dimension,
            support=support,
            associative=False,
            inverses=(),
            normal_subobjects=(),
            factorizations=(),
            finest_factorizations=(),
            candidate_tests=0,
            diagnostics=tuple(diagnostics),
        )
    associative = composition_object_is_associative(composition)
    if not associative:
        diagnostics.append("composition object is not associative")
        return AddressabilityCore(
            composition=composition,
            accessible_dimension=accessible_dimension,
            support=support,
            associative=False,
            inverses=(),
            normal_subobjects=(),
            factorizations=(),
            finest_factorizations=(),
            candidate_tests=0,
            diagnostics=tuple(diagnostics),
        )
    inverses = inverse_table(composition)
    normals = normal_subobjects(composition, inverses)
    identity_subobject = frozenset((composition.identity,))
    proper = tuple(
        candidate
        for candidate in normals
        if candidate != identity_subobject and len(candidate) != composition.size
    )
    ambient_algebra = represented_algebra(
        composition, range(composition.size), dataset.dimension
    )
    algebra_cache: Dict[Subobject, AlgebraBasis] = {
        candidate: represented_algebra(composition, candidate, dataset.dimension)
        for candidate in proper
    }
    candidate_tests = 0
    direct_pool = set()
    for left_index, left in enumerate(proper):
        for right in proper[left_index + 1 :]:
            if len(left) * len(right) != composition.size:
                continue
            candidate_tests += 1
            if candidate_tests > MAX_CANDIDATE_SUBOBJECTS:
                raise InvalidDataset("direct-complement search exceeded the frozen cap")
            if left & right != identity_subobject:
                continue
            if not subobjects_commute(composition, left, right):
                continue
            faithful, image = multiply_subobjects(composition, (left, right))
            if not faithful or len(image) != composition.size:
                continue
            left_algebra = algebra_cache[left]
            right_algebra = algebra_cache[right]
            if algebra_intersection_dimension(left_algebra, right_algebra) != 1:
                continue
            if left_algebra.dimension * right_algebra.dimension != ambient_algebra.dimension:
                continue
            direct_pool.add(left)
            direct_pool.add(right)
    direct_candidates = tuple(
        sorted(direct_pool, key=lambda item: (len(item), tuple(sorted(item))))
    )
    valid = []
    maximum_factor_count = min(8, len(direct_candidates))
    for factor_count in range(2, maximum_factor_count + 1):
        for factors in itertools.combinations(direct_candidates, factor_count):
            order_product = 1
            for factor in factors:
                order_product *= len(factor)
            if order_product != composition.size:
                continue
            candidate_tests += 1
            if candidate_tests > MAX_CANDIDATE_SUBOBJECTS:
                raise InvalidDataset("direct-factor search exceeded the frozen cap")
            if any(
                left & right != identity_subobject
                for left, right in itertools.combinations(factors, 2)
            ):
                continue
            if any(
                not subobjects_commute(composition, left, right)
                for left, right in itertools.combinations(factors, 2)
            ):
                continue
            faithful, image = multiply_subobjects(composition, factors)
            if not faithful or len(image) != composition.size:
                continue
            factor_algebras = tuple(algebra_cache[factor] for factor in factors)
            if any(
                algebra_intersection_dimension(left, right) != 1
                for left, right in itertools.combinations(factor_algebras, 2)
            ):
                continue
            if any(
                not all(
                    matrices_commute(
                        unflatten(left_row, dataset.dimension),
                        unflatten(right_row, dataset.dimension),
                    )
                    for left_row in left.vectors
                    for right_row in right.vectors
                )
                for left, right in itertools.combinations(factor_algebras, 2)
            ):
                continue
            algebra_dimension_product = 1
            for algebra in factor_algebras:
                algebra_dimension_product *= algebra.dimension
            if algebra_dimension_product != ambient_algebra.dimension:
                continue
            valid.append(
                DirectFactorization(
                    factors=tuple(factors),
                    group_orders=tuple(len(factor) for factor in factors),
                    algebra_dimensions=tuple(algebra.dimension for algebra in factor_algebras),
                )
            )
    valid = sorted(set(valid), key=factorization_sort_key)
    maximum_blocks = max((len(value.factors) for value in valid), default=0)
    finest = tuple(value for value in valid if len(value.factors) == maximum_blocks)
    if finest:
        diagnostics.append(
            "generator-independent direct-product addressability found"
        )
    else:
        diagnostics.append("no faithful jointly implemented direct factorization")
    if len(finest) > 1:
        diagnostics.append("multiple finest factorizations retained")
    return AddressabilityCore(
        composition=composition,
        accessible_dimension=accessible_dimension,
        support=support,
        associative=True,
        inverses=inverses,
        normal_subobjects=normals,
        factorizations=tuple(valid),
        finest_factorizations=finest,
        candidate_tests=candidate_tests,
        diagnostics=tuple(diagnostics),
    )


# ---------------------------------------------------------------------------
# Exact W3 record evaluation
# ---------------------------------------------------------------------------


def h_corr(witness: RecordWitness, write: Matrix) -> bool:
    mapping = []
    for alternative in witness.alternative_projectors:
        observed_sector: Optional[int] = None
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
            if not is_zero_matrix(mmul(final_probe, mmul(continuation, record)))
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
    def passes_w3(self) -> bool:
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
        validate_projector_resolution(family, dimension, f"{witness.handle}.{label}")
    for label, value in (
        (("write", witness.write), ("no_write", witness.no_write))
        + tuple((f"preserving.{index}", entry) for index, entry in enumerate(witness.preserving))
        + tuple((f"erasing.{index}", entry) for index, entry in enumerate(witness.erasing))
    ):
        if shape(value) != (dimension, dimension) or not is_unitary(value):
            raise InvalidDataset(f"{witness.handle}.{label} is not an exact unitary")
        if not is_zero_matrix(
            mmul(msub(identity(dimension), support), mmul(value, support))
        ):
            raise InvalidDataset(f"{witness.handle}.{label} leaves accessible support")
    for index, preparation in enumerate(witness.preparations):
        if len(preparation) != dimension or not inner(preparation, preparation):
            raise InvalidDataset(f"{witness.handle}.preparation.{index} is invalid")
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
    return all(algebra.contains_matrix(value) for value in required)


def two_level_record_witness(handle: str = "public-record") -> RecordWitness:
    p0 = matrix(((1, 0), (0, 0)))
    p1 = matrix(((0, 0), (0, 1)))
    h = matrix(((INV_SQRT2, INV_SQRT2), (INV_SQRT2, -INV_SQRT2)))
    plus = vector((INV_SQRT2, INV_SQRT2))
    minus = vector((INV_SQRT2, -INV_SQRT2))
    p_plus = tuple(tuple(left * right.conjugate() for right in plus) for left in plus)
    p_minus = tuple(tuple(left * right.conjugate() for right in minus) for left in minus)
    return RecordWitness(
        handle=handle,
        preparations=(basis_vector(2, 0),),
        alternative_projectors=(p_plus, p_minus),
        cut_record_projectors=(p0, p1),
        availability_probes=(p0, p1),
        write=h,
        preserving=(identity(2),),
        erasing=(h,),
        no_write=identity(2),
    )


# ---------------------------------------------------------------------------
# Record-bearing local categories and exact maps
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AlgebraInclusion:
    source_atoms: Tuple[int, ...]
    target_atoms: Tuple[int, ...]
    source_dimension: int
    target_dimension: int
    columns: Tuple[Tuple[Q24, ...], ...]


@dataclass(frozen=True)
class LocalObject:
    atoms: Tuple[int, ...]
    operational_elements: Subobject
    algebra: AlgebraBasis
    records: Tuple[str, ...]


@dataclass(frozen=True)
class FactInterface:
    atoms: Tuple[int, ...]
    record_projectors: Tuple[Tuple[str, Tuple[Matrix, ...]], ...]


@dataclass(frozen=True)
class RecordPullback:
    larger_atoms: Tuple[int, ...]
    smaller_atoms: Tuple[int, ...]
    record_maps: Tuple[Tuple[str, str, Tuple[Matrix, ...]], ...]


@dataclass(frozen=True)
class Overlap:
    objects: Tuple[Tuple[int, ...], ...]
    meet_atoms: Tuple[int, ...]


@dataclass(frozen=True)
class LocalizationAtlas:
    factorization_index: int
    objects: Tuple[LocalObject, ...]
    algebra_inclusions: Tuple[AlgebraInclusion, ...]
    fact_interfaces: Tuple[FactInterface, ...]
    record_pullbacks: Tuple[RecordPullback, ...]
    pair_overlaps: Tuple[Overlap, ...]
    triple_overlaps: Tuple[Overlap, ...]
    overlap_closed: bool
    every_object_record_bearing: bool
    algebra_category_closes: bool
    record_functor_closes: bool


@dataclass(frozen=True)
class GroupoidArrow:
    source_factorization: int
    target_factorization: int
    class_map: Tuple[int, ...]
    atom_map: Tuple[int, ...]
    carrier_permutation: Tuple[int, ...]


@dataclass(frozen=True)
class LocalizationResult:
    dataset_handle: str
    core: AddressabilityCore
    record_results: Tuple[RecordResult, ...]
    atlases: Tuple[LocalizationAtlas, ...]
    groupoid_arrows: Tuple[GroupoidArrow, ...]
    diagnostics: Tuple[str, ...]

    @property
    def has_positive_localization(self) -> bool:
        return bool(self.atlases) and all(
            atlas.objects
            and atlas.overlap_closed
            and atlas.every_object_record_bearing
            and atlas.algebra_category_closes
            and atlas.record_functor_closes
            for atlas in self.atlases
        )

    @property
    def is_ambiguous(self) -> bool:
        return len(self.core.finest_factorizations) > 1

    def structural_signature(self) -> Tuple[object, ...]:
        return (
            self.core.accessible_dimension,
            tuple(
                sorted(
                    (
                        tuple(sorted(factorization.group_orders)),
                        tuple(sorted(factorization.algebra_dimensions)),
                    )
                    for factorization in self.core.finest_factorizations
                )
            ),
            tuple(
                sorted(
                    (
                        len(atlas.objects),
                        tuple(sorted((value.algebra.dimension, len(value.records)) for value in atlas.objects)),
                        len(atlas.algebra_inclusions),
                        len(atlas.pair_overlaps),
                        len(atlas.triple_overlaps),
                    )
                    for atlas in self.atlases
                )
            ),
            len(self.groupoid_arrows),
        )


def coordinate_matrix_apply(
    columns: Sequence[Sequence[Q24]],
    coefficients: Sequence[Q24],
) -> Tuple[Q24, ...]:
    if len(columns) != len(coefficients):
        raise ValueError("coordinate map input dimension mismatch")
    if not columns:
        return ()
    target_dimension = len(columns[0])
    return tuple(
        sum((columns[column][row] * coefficients[column] for column in range(len(columns))), ZERO)
        for row in range(target_dimension)
    )


def compose_inclusions(
    first: AlgebraInclusion,
    second: AlgebraInclusion,
) -> AlgebraInclusion:
    if first.target_atoms != second.source_atoms:
        raise ValueError("algebra inclusion composition is mistyped")
    columns = tuple(
        coordinate_matrix_apply(second.columns, column)
        for column in first.columns
    )
    return AlgebraInclusion(
        source_atoms=first.source_atoms,
        target_atoms=second.target_atoms,
        source_dimension=first.source_dimension,
        target_dimension=second.target_dimension,
        columns=columns,
    )


def build_inclusion(source: LocalObject, target: LocalObject) -> AlgebraInclusion:
    if not set(source.atoms) <= set(target.atoms):
        raise ValueError("local-object inclusion is not ordered")
    columns = tuple(
        target.algebra.coordinates(unflatten(row, target.algebra.carrier_dimension))
        for row in source.algebra.vectors
    )
    result = AlgebraInclusion(
        source_atoms=source.atoms,
        target_atoms=target.atoms,
        source_dimension=source.algebra.dimension,
        target_dimension=target.algebra.dimension,
        columns=columns,
    )
    for source_index, source_row in enumerate(source.algebra.vectors):
        coordinates = result.columns[source_index]
        reconstructed = tuple(
            sum(
                (
                    coordinates[target_index] * target.algebra.vectors[target_index][entry]
                    for target_index in range(target.algebra.dimension)
                ),
                ZERO,
            )
            for entry in range(len(source_row))
        )
        if reconstructed != source_row:
            raise AssertionError("algebra inclusion does not reconstruct its source basis")
    return result


def build_fact_interface(
    local_object: LocalObject,
    witness_map: Mapping[str, RecordWitness],
) -> FactInterface:
    return FactInterface(
        atoms=local_object.atoms,
        record_projectors=tuple(
            (handle, witness_map[handle].cut_record_projectors)
            for handle in local_object.records
        ),
    )


def build_record_pullback(
    larger: FactInterface,
    smaller: FactInterface,
) -> RecordPullback:
    if not set(smaller.atoms) <= set(larger.atoms):
        raise ValueError("record pullback is mistyped")
    larger_map = dict(larger.record_projectors)
    maps = []
    for handle, projectors in smaller.record_projectors:
        if handle not in larger_map or larger_map[handle] != projectors:
            raise ValueError("record projector is not an exact pullback")
        maps.append((handle, handle, projectors))
    return RecordPullback(larger.atoms, smaller.atoms, tuple(maps))


def record_pullback_signature(value: RecordPullback) -> Tuple[Tuple[str, str, Tuple[Matrix, ...]], ...]:
    return value.record_maps


def product_image(composition: CompositionObject, factors: Sequence[Subobject]) -> Subobject:
    faithful, image = multiply_subobjects(composition, factors)
    if not faithful:
        raise AssertionError("factor subset lost faithful multiplication")
    return image


def build_atlas(
    dataset: OperationalDataset,
    core: AddressabilityCore,
    factorization_index: int,
    record_results: Sequence[RecordResult],
) -> LocalizationAtlas:
    factorization = core.finest_factorizations[factorization_index]
    result_by_handle = {value.handle: value for value in record_results}
    witness_map = {value.handle: value for value in dataset.records}
    local_objects = []
    atom_count = len(factorization.factors)
    for subset_size in range(1, atom_count):
        for atom_subset in itertools.combinations(range(atom_count), subset_size):
            operational_elements = product_image(
                core.composition,
                tuple(factorization.factors[index] for index in atom_subset),
            )
            algebra = represented_algebra(
                core.composition, operational_elements, dataset.dimension
            )
            records = tuple(
                sorted(
                    witness.handle
                    for witness in dataset.records
                    if result_by_handle[witness.handle].passes_w3
                    and record_lives_in_algebra(witness, algebra)
                )
            )
            if records:
                local_objects.append(
                    LocalObject(atom_subset, operational_elements, algebra, records)
                )
    local_objects = tuple(sorted(local_objects, key=lambda value: (len(value.atoms), value.atoms)))
    object_map = {value.atoms: value for value in local_objects}
    inclusions = tuple(
        build_inclusion(source, target)
        for source in local_objects
        for target in local_objects
        if set(source.atoms) <= set(target.atoms)
    )
    fact_interfaces = tuple(build_fact_interface(value, witness_map) for value in local_objects)
    fact_map = {value.atoms: value for value in fact_interfaces}
    pullbacks = tuple(
        build_record_pullback(fact_map[target.atoms], fact_map[source.atoms])
        for source in local_objects
        for target in local_objects
        if set(source.atoms) <= set(target.atoms)
    )
    pair_overlaps = []
    triple_overlaps = []
    overlap_closed = True
    for left, right in itertools.combinations(local_objects, 2):
        meet = tuple(sorted(set(left.atoms) & set(right.atoms)))
        if not meet:
            continue
        if meet not in object_map:
            overlap_closed = False
            continue
        pair_overlaps.append(Overlap((left.atoms, right.atoms), meet))
    for first, second, third in itertools.combinations(local_objects, 3):
        meet = tuple(sorted(set(first.atoms) & set(second.atoms) & set(third.atoms)))
        if not meet:
            continue
        if meet not in object_map:
            overlap_closed = False
            continue
        triple_overlaps.append(Overlap((first.atoms, second.atoms, third.atoms), meet))
    inclusion_map = {
        (value.source_atoms, value.target_atoms): value for value in inclusions
    }
    algebra_category_closes = True
    for first in inclusions:
        for second in inclusions:
            if first.target_atoms != second.source_atoms:
                continue
            direct = inclusion_map.get((first.source_atoms, second.target_atoms))
            if direct is None or compose_inclusions(first, second).columns != direct.columns:
                algebra_category_closes = False
    pullback_map = {
        (value.larger_atoms, value.smaller_atoms): value for value in pullbacks
    }
    record_functor_closes = True
    for larger_to_middle in pullbacks:
        for middle_to_smaller in pullbacks:
            if larger_to_middle.smaller_atoms != middle_to_smaller.larger_atoms:
                continue
            direct = pullback_map.get(
                (larger_to_middle.larger_atoms, middle_to_smaller.smaller_atoms)
            )
            if direct is None:
                record_functor_closes = False
                continue
            retained = {
                source: (target, projectors)
                for source, target, projectors in larger_to_middle.record_maps
            }
            composite = tuple(
                (source, retained[source][0], projectors)
                for source, _, projectors in middle_to_smaller.record_maps
                if source in retained and retained[source][1] == projectors
            )
            if composite != direct.record_maps:
                record_functor_closes = False
    return LocalizationAtlas(
        factorization_index=factorization_index,
        objects=local_objects,
        algebra_inclusions=inclusions,
        fact_interfaces=fact_interfaces,
        record_pullbacks=pullbacks,
        pair_overlaps=tuple(pair_overlaps),
        triple_overlaps=tuple(triple_overlaps),
        overlap_closed=overlap_closed,
        every_object_record_bearing=bool(local_objects)
        and all(value.records for value in local_objects),
        algebra_category_closes=algebra_category_closes,
        record_functor_closes=record_functor_closes,
    )


def permutation_matrix(permutation: Sequence[int]) -> Matrix:
    dimension = len(permutation)
    if set(permutation) != set(range(dimension)):
        raise ValueError("not a carrier permutation")
    return tuple(
        tuple(ONE if row == permutation[column] else ZERO for column in range(dimension))
        for row in range(dimension)
    )


def derive_groupoid_arrows(
    dataset: OperationalDataset,
    core: AddressabilityCore,
) -> Tuple[GroupoidArrow, ...]:
    factorizations = core.finest_factorizations
    if not factorizations:
        return ()
    if len(factorizations) == 1:
        identity_class_map = tuple(range(core.composition.size))
        return (
            GroupoidArrow(
                0,
                0,
                identity_class_map,
                tuple(range(len(factorizations[0].factors))),
                tuple(range(dataset.dimension)),
            ),
        )
    permutation_count = 1
    for value in range(2, dataset.dimension + 1):
        permutation_count *= value
    if permutation_count > MAX_AUTOMORPHISM_PERMUTATIONS:
        raise InvalidDataset("ambiguity carrier-permutation search exceeds the frozen cap")
    signature_to_class = {
        operation_class.signature: index
        for index, operation_class in enumerate(core.composition.classes)
    }
    arrows = []
    for carrier_permutation in itertools.permutations(range(dataset.dimension)):
        action = permutation_matrix(carrier_permutation)
        class_map = []
        for operation_class in core.composition.classes:
            signature = amplitude_signature(
                conjugate_by(action, operation_class.representative)
            )
            if signature not in signature_to_class:
                class_map = []
                break
            class_map.append(signature_to_class[signature])
        if not class_map or len(set(class_map)) != core.composition.size:
            continue
        if any(
            class_map[core.composition.product(left, right)]
            != core.composition.product(class_map[left], class_map[right])
            for left in range(core.composition.size)
            for right in range(core.composition.size)
        ):
            continue
        for source_index, source in enumerate(factorizations):
            transformed = tuple(
                frozenset(class_map[element] for element in factor)
                for factor in source.factors
            )
            for target_index, target in enumerate(factorizations):
                atom_map = []
                unused = set(range(len(target.factors)))
                for factor in transformed:
                    match = next(
                        (
                            index
                            for index in sorted(unused)
                            if target.factors[index] == factor
                        ),
                        None,
                    )
                    if match is None:
                        atom_map = []
                        break
                    atom_map.append(match)
                    unused.remove(match)
                if atom_map and not unused:
                    arrows.append(
                        GroupoidArrow(
                            source_index,
                            target_index,
                            tuple(class_map),
                            tuple(atom_map),
                            tuple(carrier_permutation),
                        )
                    )
    unique = {
        (
            value.source_factorization,
            value.target_factorization,
            value.class_map,
            value.atom_map,
            value.carrier_permutation,
        ): value
        for value in arrows
    }
    return tuple(unique[key] for key in sorted(unique))


def analyze_localization(dataset: OperationalDataset) -> LocalizationResult:
    core = analyze_addressability_core(dataset)
    record_results = tuple(
        evaluate_record_witness(witness, core.support, dataset.dimension)
        for witness in dataset.records
    )
    atlases = tuple(
        build_atlas(dataset, core, index, record_results)
        for index in range(len(core.finest_factorizations))
    )
    groupoid_arrows = derive_groupoid_arrows(dataset, core)
    diagnostics = list(core.diagnostics)
    if core.finest_factorizations and not atlases:
        diagnostics.append("address factors exist but no record-bearing atlas was built")
    if atlases and not all(atlas.every_object_record_bearing for atlas in atlases):
        diagnostics.append("one or more counted local objects are recordless")
    if atlases and not all(atlas.overlap_closed for atlas in atlases):
        diagnostics.append("record-bearing local objects are not overlap closed")
    return LocalizationResult(
        dataset_handle=dataset.handle,
        core=core,
        record_results=record_results,
        atlases=atlases,
        groupoid_arrows=groupoid_arrows,
        diagnostics=tuple(diagnostics),
    )


def composition_isomorphism_by_action(
    source: OperationalDataset,
    target: OperationalDataset,
    action: Matrix,
) -> Tuple[int, ...]:
    if source.dimension != target.dimension or shape(action) != (
        source.dimension,
        source.dimension,
    ):
        return ()
    if not is_unitary(action):
        return ()
    source_object = build_composition_object(source)
    target_object = build_composition_object(target)
    if source_object.size != target_object.size:
        return ()
    target_signatures = {
        operation_class.signature: index
        for index, operation_class in enumerate(target_object.classes)
    }
    class_map = []
    for operation_class in source_object.classes:
        signature = amplitude_signature(
            conjugate_by(action, operation_class.representative)
        )
        if signature not in target_signatures:
            return ()
        class_map.append(target_signatures[signature])
    if len(set(class_map)) != source_object.size:
        return ()
    for left in range(source_object.size):
        for right in range(source_object.size):
            source_row = source_object.table[left][right]
            target_row = target_object.table[class_map[left]][class_map[right]]
            if source_row.status != target_row.status:
                return ()
            expected_result = (
                None if source_row.result is None else class_map[source_row.result]
            )
            if expected_result != target_row.result:
                return ()
    return tuple(class_map)


def finite_mu8_monomial_actions(dimension: int) -> Iterator[Matrix]:
    permutation_count = 1
    for value in range(2, dimension + 1):
        permutation_count *= value
    phase_count = 8 ** dimension
    if permutation_count * phase_count > MAX_AUTOMORPHISM_PERMUTATIONS:
        raise InvalidDataset("finite monomial bridge search exceeds the frozen cap")
    phase_values = tuple(ZETA ** (3 * exponent) for exponent in range(8))
    for permutation in itertools.permutations(range(dimension)):
        base = permutation_matrix(permutation)
        for phases in itertools.product(phase_values, repeat=dimension):
            diagonal = tuple(
                tuple(phases[row] if row == column else ZERO for column in range(dimension))
                for row in range(dimension)
            )
            yield mmul(diagonal, base)


def search_finite_monomial_bridges(
    source: OperationalDataset,
    target: OperationalDataset,
) -> Tuple[Tuple[Tuple[int, ...], Tuple[int, ...]], ...]:
    if source.dimension != target.dimension:
        return ()
    results = []
    for action in finite_mu8_monomial_actions(source.dimension):
        class_map = composition_isomorphism_by_action(source, target, action)
        if class_map:
            permutation = tuple(
                next(row for row in range(source.dimension) if action[row][column])
                for column in range(source.dimension)
            )
            results.append((class_map, permutation))
    return tuple(sorted(set(results)))


def localization_to_data(result: LocalizationResult) -> Mapping[str, object]:
    return {
        "api": ESTIMATOR_API_VERSION,
        "dataset": result.dataset_handle,
        "composition": {
            "class_count": result.core.composition.size,
            "classes": [list(value.members) for value in result.core.composition.classes],
            "identity": result.core.composition.identity,
            "generator_classes": list(result.core.composition.generator_classes),
            "congruence_verified": result.core.composition.congruence_verified,
            "total_implemented": result.core.composition.total_implemented,
            "unique_product_amplitudes": result.core.composition.unique_product_amplitudes,
        },
        "accessible_dimension": result.core.accessible_dimension,
        "associative": result.core.associative,
        "normal_subobject_count": len(result.core.normal_subobjects),
        "candidate_tests": result.core.candidate_tests,
        "factorizations": [
            {
                "factors": [sorted(factor) for factor in value.factors],
                "group_orders": list(value.group_orders),
                "algebra_dimensions": list(value.algebra_dimensions),
            }
            for value in result.core.factorizations
        ],
        "finest_factorizations": [
            {
                "factors": [sorted(factor) for factor in value.factors],
                "group_orders": list(value.group_orders),
                "algebra_dimensions": list(value.algebra_dimensions),
            }
            for value in result.core.finest_factorizations
        ],
        "records": [
            {
                "handle": value.handle,
                "occurrence": value.occurrence,
                "preserving_available": list(value.preserving_available),
                "erasing_available": list(value.erasing_available),
                "erasing_cross_coherence": list(value.erasing_cross_coherence),
                "no_write_occurrence": value.no_write_occurrence,
                "passes_w3": value.passes_w3,
            }
            for value in result.record_results
        ],
        "atlases": [
            {
                "factorization_index": atlas.factorization_index,
                "objects": [
                    {
                        "atoms": list(value.atoms),
                        "operation_count": len(value.operational_elements),
                        "algebra_dimension": value.algebra.dimension,
                        "records": list(value.records),
                    }
                    for value in atlas.objects
                ],
                "algebra_inclusions": [
                    {
                        "source": list(value.source_atoms),
                        "target": list(value.target_atoms),
                        "source_dimension": value.source_dimension,
                        "target_dimension": value.target_dimension,
                        "columns": [
                            [entry.render() for entry in column]
                            for column in value.columns
                        ],
                    }
                    for value in atlas.algebra_inclusions
                ],
                "fact_interfaces": [
                    {
                        "atoms": list(value.atoms),
                        "records": [handle for handle, _ in value.record_projectors],
                    }
                    for value in atlas.fact_interfaces
                ],
                "record_pullbacks": [
                    {
                        "larger": list(value.larger_atoms),
                        "smaller": list(value.smaller_atoms),
                        "records": [source for source, _, _ in value.record_maps],
                    }
                    for value in atlas.record_pullbacks
                ],
                "pair_overlaps": [
                    {
                        "objects": [list(entry) for entry in value.objects],
                        "meet": list(value.meet_atoms),
                    }
                    for value in atlas.pair_overlaps
                ],
                "triple_overlaps": [
                    {
                        "objects": [list(entry) for entry in value.objects],
                        "meet": list(value.meet_atoms),
                    }
                    for value in atlas.triple_overlaps
                ],
                "overlap_closed": atlas.overlap_closed,
                "every_object_record_bearing": atlas.every_object_record_bearing,
                "algebra_category_closes": atlas.algebra_category_closes,
                "record_functor_closes": atlas.record_functor_closes,
            }
            for atlas in result.atlases
        ],
        "groupoid_arrows": [
            {
                "source": value.source_factorization,
                "target": value.target_factorization,
                "class_map": list(value.class_map),
                "atom_map": list(value.atom_map),
                "carrier_permutation": list(value.carrier_permutation),
            }
            for value in result.groupoid_arrows
        ],
        "diagnostics": list(result.diagnostics),
    }


# ---------------------------------------------------------------------------
# Public calibrations only — no repair-fixture truth
# ---------------------------------------------------------------------------


S3Element = Tuple[int, int]
PublicElement = Tuple[S3Element, int]


def s3_multiply(left: S3Element, right: S3Element) -> S3Element:
    left_rotation, left_reflection = left
    right_rotation, right_reflection = right
    signed_right = right_rotation if left_reflection == 0 else -right_rotation
    return ((left_rotation + signed_right) % 3, (left_reflection + right_reflection) % 2)


def s3_representation(element: S3Element) -> Matrix:
    rotation = matrix(
        (
            (Fraction(-1, 2), -SQRT3 * Fraction(1, 2)),
            (SQRT3 * Fraction(1, 2), Fraction(-1, 2)),
        )
    )
    reflection = matrix(((1, 0), (0, -1)))
    return mmul(
        matrix_power(rotation, element[0]),
        matrix_power(reflection, element[1]),
    )


def matrix_power(value: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        return matrix_power(adjoint(value), -exponent)
    result = identity(len(value))
    base = value
    power = exponent
    while power:
        if power & 1:
            result = mmul(result, base)
        base = mmul(base, base)
        power //= 2
    return result


def public_elements() -> Tuple[PublicElement, ...]:
    return tuple(
        ((rotation, reflection), bit)
        for rotation in range(3)
        for reflection in range(2)
        for bit in range(2)
    )


def public_multiply(left: PublicElement, right: PublicElement) -> PublicElement:
    return (s3_multiply(left[0], right[0]), (left[1] + right[1]) % 2)


def public_representation(element: PublicElement) -> Matrix:
    z = matrix(((1, 0), (0, -1)))
    return kron(s3_representation(element[0]), matrix_power(z, element[1]))


def build_group_dataset(
    handle: str,
    elements: Sequence[Hashable],
    multiply: Callable[[Hashable, Hashable], Hashable],
    representation: Callable[[Hashable], Matrix],
    generator_elements: Sequence[Hashable],
    unavailable_pairs: FrozenSet[Tuple[Hashable, Hashable]] = frozenset(),
    collapsed_pairs: FrozenSet[Tuple[Hashable, Hashable]] = frozenset(),
    aliases: Optional[Mapping[str, Hashable]] = None,
) -> OperationalDataset:
    element_tuple = tuple(elements)
    canonical_handles = {element: f"u{index:03d}" for index, element in enumerate(element_tuple)}
    operations = [
        Operation(canonical_handles[element], representation(element))
        for element in element_tuple
    ]
    alias_elements: Dict[str, Hashable] = {}
    for alias_handle, element in sorted((aliases or {}).items()):
        if element not in canonical_handles:
            raise ValueError("alias references an unknown group element")
        operations.append(Operation(alias_handle, representation(element)))
        alias_elements[alias_handle] = element
    handle_to_element = {}
    for operation in operations:
        if operation.handle in alias_elements:
            handle_to_element[operation.handle] = alias_elements[operation.handle]
        else:
            handle_to_element[operation.handle] = element_tuple[int(operation.handle[1:])]
    rows = []
    for left in operations:
        for right in operations:
            left_element = handle_to_element[left.handle]
            right_element = handle_to_element[right.handle]
            pair = (left_element, right_element)
            if pair in unavailable_pairs:
                rows.append(
                    CompositionRow(left.handle, right.handle, "flat", UNAVAILABLE, None)
                )
                continue
            result_element = multiply(left_element, right_element)
            status = COLLAPSED if pair in collapsed_pairs else IMPLEMENTED
            rows.append(
                CompositionRow(
                    left.handle,
                    right.handle,
                    "flat",
                    status,
                    canonical_handles[result_element],
                )
            )
    generator_handles = tuple(
        next(
            handle
            for handle, element in handle_to_element.items()
            if element == generator_element
        )
        for generator_element in generator_elements
    )
    return OperationalDataset(
        handle=handle,
        dimension=len(representation(element_tuple[0])),
        operations=tuple(operations),
        composition_rows=tuple(rows),
        generator_handles=generator_handles,
        preparations=(),
        probes=(),
        records=(),
        gauge_actions=(identity(len(representation(element_tuple[0]))),),
        access_declaration="PUBLIC CALIBRATION: complete exact amplitude tomography and flat composition table",
    )


def public_calibration_dataset(
    presentation: str = "base",
) -> OperationalDataset:
    elements = public_elements()
    rotation = ((1, 0), 0)
    reflection = ((0, 1), 0)
    bit = ((0, 0), 1)
    mixed = public_multiply(reflection, bit)
    if presentation == "base":
        generators = (rotation, reflection, bit)
        aliases: Mapping[str, object] = {}
    elif presentation == "changed-generator":
        generators = (rotation, reflection, mixed)
        aliases = {}
    elif presentation == "redundant-alias":
        generators = (rotation, reflection, bit)
        aliases = {"redundant-mixed": mixed}
    else:
        raise ValueError(f"unknown public presentation {presentation}")
    return build_group_dataset(
        f"public-s3xc2-{presentation}",
        elements,
        public_multiply,
        public_representation,
        generators,
        aliases=aliases,
    )


def public_blocked_dataset(mode: str) -> OperationalDataset:
    elements = public_elements()
    rotation = ((1, 0), 0)
    reflection = ((0, 1), 0)
    bit = ((0, 0), 1)
    blocked_pair = frozenset(((reflection, bit),))
    if mode == "unavailable":
        unavailable = blocked_pair
        collapsed = frozenset()
    elif mode == "collapsed":
        unavailable = frozenset()
        collapsed = blocked_pair
    else:
        raise ValueError(f"unknown blocked mode {mode}")
    return build_group_dataset(
        f"public-s3xc2-{mode}",
        elements,
        public_multiply,
        public_representation,
        (rotation, reflection, bit),
        unavailable_pairs=unavailable,
        collapsed_pairs=collapsed,
    )


def s3_pair_elements() -> Tuple[Tuple[S3Element, S3Element], ...]:
    s3 = tuple((rotation, reflection) for rotation in range(3) for reflection in range(2))
    return tuple((left, right) for left in s3 for right in s3)


def s3_pair_multiply(
    left: Tuple[S3Element, S3Element],
    right: Tuple[S3Element, S3Element],
) -> Tuple[S3Element, S3Element]:
    return (s3_multiply(left[0], right[0]), s3_multiply(left[1], right[1]))


def s3_pair_representation(element: Tuple[S3Element, S3Element]) -> Matrix:
    return kron(s3_representation(element[0]), s3_representation(element[1]))


def embed_two_factor_matrix(value: Matrix, slot: int) -> Matrix:
    if slot == 0:
        return kron(value, identity(2))
    if slot == 1:
        return kron(identity(2), value)
    raise ValueError("public two-factor slot must be zero or one")


def embed_two_factor_vector(value: Vector, slot: int) -> Vector:
    other = basis_vector(2, 0)
    if slot == 0:
        return vkron(value, other)
    if slot == 1:
        return vkron(other, value)
    raise ValueError("public two-factor slot must be zero or one")


def embedded_public_record(slot: int) -> RecordWitness:
    witness = two_level_record_witness(f"public-record-{slot}")
    return RecordWitness(
        handle=witness.handle,
        preparations=tuple(embed_two_factor_vector(value, slot) for value in witness.preparations),
        alternative_projectors=tuple(
            embed_two_factor_matrix(value, slot) for value in witness.alternative_projectors
        ),
        cut_record_projectors=tuple(
            embed_two_factor_matrix(value, slot) for value in witness.cut_record_projectors
        ),
        availability_probes=tuple(
            embed_two_factor_matrix(value, slot) for value in witness.availability_probes
        ),
        write=embed_two_factor_matrix(witness.write, slot),
        preserving=tuple(embed_two_factor_matrix(value, slot) for value in witness.preserving),
        erasing=tuple(embed_two_factor_matrix(value, slot) for value in witness.erasing),
        no_write=embed_two_factor_matrix(witness.no_write, slot),
    )


def public_record_atlas_dataset() -> OperationalDataset:
    elements = s3_pair_elements()
    base = build_group_dataset(
        "public-s3xs3-record-atlas",
        elements,
        s3_pair_multiply,
        s3_pair_representation,
        (
            ((1, 0), (0, 0)),
            ((0, 1), (0, 0)),
            ((0, 0), (1, 0)),
            ((0, 0), (0, 1)),
        ),
    )
    return OperationalDataset(
        handle=base.handle,
        dimension=base.dimension,
        operations=base.operations,
        composition_rows=base.composition_rows,
        generator_handles=base.generator_handles,
        preparations=(),
        probes=(),
        records=(embedded_public_record(0), embedded_public_record(1)),
        gauge_actions=base.gauge_actions,
        access_declaration=base.access_declaration + "; two W3 record calibrations",
        gauge_declaration=base.gauge_declaration,
    )


def public_inaccessible_extension(dataset: OperationalDataset) -> OperationalDataset:
    hidden = identity(dataset.dimension)
    operations = tuple(
        Operation(
            operation.handle,
            direct_sum(operation.amplitude, hidden),
            operation.boundary_type,
            operation.independently_selectable,
        )
        for operation in dataset.operations
    )
    preparations = tuple(
        vector(tuple(state) + (ZERO,) * dataset.dimension)
        for state in (basis_vector(dataset.dimension, index) for index in range(dataset.dimension))
    )
    return OperationalDataset(
        handle=dataset.handle + "-inaccessible-extension",
        dimension=dataset.dimension * 2,
        operations=operations,
        composition_rows=dataset.composition_rows,
        generator_handles=dataset.generator_handles,
        preparations=preparations,
        probes=preparations,
        records=(),
        gauge_actions=(identity(dataset.dimension * 2),),
        access_declaration=dataset.access_declaration + "; inaccessible direct-sum completion",
        gauge_declaration=dataset.gauge_declaration,
    )


def public_incongruent_alias_dataset() -> OperationalDataset:
    base = public_calibration_dataset("redundant-alias")
    rows = list(base.composition_rows)
    index = next(
        position
        for position, row in enumerate(rows)
        if row.left == "redundant-mixed" and row.right != "redundant-mixed"
    )
    row = rows[index]
    rows[index] = CompositionRow(row.left, row.right, row.context, UNAVAILABLE, None)
    return OperationalDataset(
        handle="public-incongruent-alias",
        dimension=base.dimension,
        operations=base.operations,
        composition_rows=tuple(rows),
        generator_handles=base.generator_handles,
        preparations=base.preparations,
        probes=base.probes,
        records=base.records,
        gauge_actions=base.gauge_actions,
        access_declaration=base.access_declaration + "; deliberate congruence failure",
        gauge_declaration=base.gauge_declaration,
    )


def public_map_chain_check() -> bool:
    p0 = matrix(((1, 0), (0, 0)))
    p1 = matrix(((0, 0), (0, 1)))
    x = matrix(((0, 1), (1, 0)))
    z = matrix(((1, 0), (0, -1)))
    scalar = algebra_from_matrices((identity(2),), 2)
    diagonal = algebra_from_matrices((identity(2), z), 2)
    full = algebra_from_matrices((identity(2), z, x, mmul(x, z)), 2)
    small = LocalObject((0,), frozenset((0,)), scalar, ("r",))
    middle = LocalObject((0, 1), frozenset((0, 1)), diagonal, ("r", "s"))
    large = LocalObject((0, 1, 2), frozenset((0, 1, 2)), full, ("r", "s", "t"))
    small_middle = build_inclusion(small, middle)
    middle_large = build_inclusion(middle, large)
    small_large = build_inclusion(small, large)
    algebra_ok = compose_inclusions(small_middle, middle_large).columns == small_large.columns
    projectors = (p0, p1)
    small_fact = FactInterface(small.atoms, (("r", projectors),))
    middle_fact = FactInterface(middle.atoms, (("r", projectors), ("s", projectors)))
    large_fact = FactInterface(
        large.atoms,
        (("r", projectors), ("s", projectors), ("t", projectors)),
    )
    large_middle = build_record_pullback(large_fact, middle_fact)
    middle_small = build_record_pullback(middle_fact, small_fact)
    large_small = build_record_pullback(large_fact, small_fact)
    composite_records = tuple(
        row for row in large_middle.record_maps if row[0] in {entry[0] for entry in middle_small.record_maps}
    )
    return algebra_ok and composite_records == large_small.record_maps


def core_signature(value: AddressabilityCore) -> Tuple[object, ...]:
    return (
        value.composition.size,
        value.accessible_dimension,
        value.associative,
        tuple(
            sorted(
                (
                    tuple(sorted(factorization.group_orders)),
                    tuple(sorted(factorization.algebra_dimensions)),
                )
                for factorization in value.finest_factorizations
            )
        ),
    )


def normalize(value: object) -> object:
    if isinstance(value, Q24):
        return value.render()
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, frozenset):
        return sorted(normalize(entry) for entry in value)
    if isinstance(value, tuple):
        return [normalize(entry) for entry in value]
    if isinstance(value, list):
        return [normalize(entry) for entry in value]
    if isinstance(value, dict):
        return {str(key): normalize(entry) for key, entry in value.items()}
    return value


def public_self_test() -> Mapping[str, object]:
    field_checks = {
        "zeta24": ZETA ** 24 == ONE,
        "zeta12": ZETA ** 12 == -ONE,
        "sqrt2": SQRT2 * SQRT2 == Q24(2),
        "sqrt3": SQRT3 * SQRT3 == Q24(3),
        "inverse_count": sum(
            1
            for exponent in range(1, 24)
            if (ZETA ** exponent) * (ZETA ** exponent).inverse() == ONE
        ),
    }
    record = evaluate_record_witness(two_level_record_witness(), identity(2), 2)
    phase_samples = (
        zero_matrix(2, 2),
        identity(2),
        matrix(((1, ZETA), (SQRT2, SQRT3))),
        matrix(((ZETA ** 5, -ONE), (INV_SQRT2, ZETA ** 17))),
    ) + tuple(
        s3_representation((rotation, reflection))
        for rotation in range(3)
        for reflection in range(2)
    ) + tuple(
        public_representation(element)
        for element in public_elements()
    )
    phase_quotient_equivalence = all(
        canonical_mu24_phase(value) == canonical_mu24_phase_reference(value)
        and all(
            canonical_mu24_phase(mscale(ZETA ** exponent, value))
            == canonical_mu24_phase_reference(mscale(ZETA ** exponent, value))
            for exponent in range(24)
        )
        for value in phase_samples
    )
    base = analyze_addressability_core(public_calibration_dataset("base"))
    changed = analyze_addressability_core(
        public_calibration_dataset("changed-generator")
    )
    redundant = analyze_addressability_core(
        public_calibration_dataset("redundant-alias")
    )
    unavailable = analyze_addressability_core(public_blocked_dataset("unavailable"))
    collapsed = analyze_addressability_core(public_blocked_dataset("collapsed"))
    public_atlas = analyze_localization(public_record_atlas_dataset())
    public_groupoid = derive_groupoid_arrows(public_calibration_dataset("base"), base)
    inaccessible = analyze_addressability_core(
        public_inaccessible_extension(public_calibration_dataset("base"))
    )
    try:
        build_composition_object(public_incongruent_alias_dataset())
    except AccessUnderdetermined:
        congruence_failure_detected = True
    else:
        congruence_failure_detected = False
    normal_join_equivalence = all(
        frozenset(
            base.composition.product(left_entry, right_entry)
            for left_entry in left
            for right_entry in right
        )
        == normal_closure(base.composition, left | right, base.inverses)
        for left in base.normal_subobjects
        for right in base.normal_subobjects
    )
    expected_signature = (
        12,
        4,
        True,
        (
            ((2, 6), (2, 4)),
            ((2, 6), (2, 4)),
        ),
    )
    checks = {
        "field": field_checks == {
            "zeta24": True,
            "zeta12": True,
            "sqrt2": True,
            "sqrt3": True,
            "inverse_count": 23,
        },
        "phase_quotient_equivalence": phase_quotient_equivalence,
        "normal_join_equivalence": normal_join_equivalence,
        "product_signature_cache": (
            base.composition.unique_product_amplitudes == base.composition.size
            and base.composition.unique_product_amplitudes
            < len(public_calibration_dataset("base").composition_rows)
        ),
        "record": record.passes_w3,
        "public_base": core_signature(base) == expected_signature,
        "changed_generator": core_signature(changed) == core_signature(base),
        "redundant_alias": core_signature(redundant) == core_signature(base),
        "unavailable_blocks": unavailable.blocked_at_address,
        "collapse_blocks": collapsed.blocked_at_address,
        "typed_record_atlas": (
            public_atlas.has_positive_localization
            and len(public_atlas.atlases) == 1
            and len(public_atlas.atlases[0].objects) == 2
            and len(public_atlas.atlases[0].algebra_inclusions) == 2
            and len(public_atlas.atlases[0].record_pullbacks) == 2
        ),
        "derived_ambiguity_arrows": (
            len(base.finest_factorizations) == 2
            and {value.source_factorization for value in public_groupoid} == {0, 1}
            and {value.target_factorization for value in public_groupoid} == {0, 1}
        ),
        "inaccessible_quotient": core_signature(inaccessible) == core_signature(base),
        "congruence_failure": congruence_failure_detected,
        "typed_map_chain": public_map_chain_check(),
    }
    if not all(checks.values()):
        raise AssertionError(
            json.dumps(
                normalize(
                    {
                        "checks": checks,
                        "field": field_checks,
                        "record": {
                            "occurrence": record.occurrence,
                            "preserving_available": record.preserving_available,
                            "erasing_available": record.erasing_available,
                            "erasing_cross_coherence": record.erasing_cross_coherence,
                            "no_write_occurrence": record.no_write_occurrence,
                        },
                        "base": core_signature(base),
                        "changed": core_signature(changed),
                        "redundant": core_signature(redundant),
                        "unavailable": unavailable.diagnostics,
                        "collapsed": collapsed.diagnostics,
                        "atlas": public_atlas.structural_signature(),
                        "groupoid_arrows": tuple(
                            (
                                value.source_factorization,
                                value.target_factorization,
                                value.atom_map,
                                value.carrier_permutation,
                            )
                            for value in public_groupoid
                        ),
                        "inaccessible": core_signature(inaccessible),
                        "congruence_failure": congruence_failure_detected,
                        "typed_map_chain": public_map_chain_check(),
                    }
                ),
                indent=2,
                sort_keys=True,
            )
        )
    return {
        "api": ESTIMATOR_API_VERSION,
        "scope": {
            "scalar_field": "Q(zeta_24), Phi_24=x^8-x^4+1",
            "main_fixture_present": False,
            "causal_or_geometric_object": False,
        },
        "field": field_checks,
        "record": {
            "occurrence": record.occurrence,
            "preserving_available": record.preserving_available,
            "erasing_available": record.erasing_available,
            "erasing_cross_coherence": record.erasing_cross_coherence,
            "no_write_occurrence": record.no_write_occurrence,
        },
        "public_calibration": {
            "composition_classes": base.composition.size,
            "normal_subobjects": len(base.normal_subobjects),
            "valid_factorizations": len(base.factorizations),
            "finest_factorizations": len(base.finest_factorizations),
            "finest_group_orders": tuple(
                tuple(sorted(value.group_orders)) for value in base.finest_factorizations
            ),
            "finest_algebra_dimensions": tuple(
                tuple(sorted(value.algebra_dimensions)) for value in base.finest_factorizations
            ),
            "changed_generator_invariant": core_signature(changed) == core_signature(base),
            "redundant_alias_invariant": core_signature(redundant) == core_signature(base),
            "unavailable_blocks": unavailable.blocked_at_address,
            "collapse_blocks": collapsed.blocked_at_address,
            "typed_record_atlas": checks["typed_record_atlas"],
            "derived_ambiguity_arrows": len(public_groupoid),
            "inaccessible_quotient": checks["inaccessible_quotient"],
            "congruence_failure": checks["congruence_failure"],
            "typed_map_chain": checks["typed_map_chain"],
            "phase_quotient_equivalence": checks["phase_quotient_equivalence"],
            "normal_join_equivalence": checks["normal_join_equivalence"],
            "unique_product_amplitudes": base.composition.unique_product_amplitudes,
            "product_signature_cache": checks["product_signature_cache"],
        },
        "checks": checks,
    }


def main() -> int:
    print(json.dumps(normalize(public_self_test()), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
