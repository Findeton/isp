#!/usr/bin/env python3
"""Generic exact machinery for CEL Paper 7.

This module contains no CEL physical fixture, recurrence doctrine, selected
coupling, primary verdict, or Paper 7 prose.  It supplies exact arithmetic,
kernel/channel operations, finite classical recoverability tests, instrument
dilations, and constructive Gaussian-rational Gram factorizations.  Its CLI
runs constructor-stated public calibrations only.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
import sys
import tempfile
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


Q = Fraction


@dataclass(frozen=True, order=True)
class GQ:
    """Gaussian rational ``re + im*i``."""

    re: Q = Q(0)
    im: Q = Q(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "re", Q(self.re))
        object.__setattr__(self, "im", Q(self.im))

    @staticmethod
    def coerce(value: Any) -> "GQ":
        if isinstance(value, GQ):
            return value
        if isinstance(value, (int, Fraction, str)):
            return GQ(Q(value), Q(0))
        raise TypeError(f"cannot coerce {type(value)!r} to GQ")

    def __add__(self, other: Any) -> "GQ":
        rhs = GQ.coerce(other)
        return GQ(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "GQ":
        return GQ(-self.re, -self.im)

    def __sub__(self, other: Any) -> "GQ":
        return self + (-GQ.coerce(other))

    def __rsub__(self, other: Any) -> "GQ":
        return GQ.coerce(other) - self

    def __mul__(self, other: Any) -> "GQ":
        rhs = GQ.coerce(other)
        return GQ(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def conjugate(self) -> "GQ":
        return GQ(self.re, -self.im)

    def norm2(self) -> Q:
        return self.re * self.re + self.im * self.im

    def inverse(self) -> "GQ":
        denominator = self.norm2()
        if denominator == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        return GQ(self.re / denominator, -self.im / denominator)

    def __truediv__(self, other: Any) -> "GQ":
        return self * GQ.coerce(other).inverse()


ZERO = GQ(0)
ONE = GQ(1)
I = GQ(0, 1)
Matrix = tuple[tuple[GQ, ...], ...]
QMatrix = tuple[tuple[Q, ...], ...]


def qtext(value: Q) -> str:
    value = Q(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def gtext(value: GQ) -> str:
    if value.im == 0:
        return qtext(value.re)
    if value.re == 0:
        if value.im == 1:
            return "i"
        if value.im == -1:
            return "-i"
        return f"{qtext(value.im)}i"
    sign = "+" if value.im > 0 else "-"
    magnitude = abs(value.im)
    imaginary = "i" if magnitude == 1 else f"{qtext(magnitude)}i"
    return f"{qtext(value.re)}{sign}{imaginary}"


def scalar(value: Any) -> GQ:
    return GQ.coerce(value)


def matrix(rows: Iterable[Iterable[Any]]) -> Matrix:
    result = tuple(tuple(scalar(entry) for entry in row) for row in rows)
    if not result or not result[0]:
        raise ValueError("matrix must be nonempty")
    width = len(result[0])
    if any(len(row) != width for row in result):
        raise ValueError("ragged matrix")
    return result


def qmatrix(rows: Iterable[Iterable[Any]]) -> QMatrix:
    result = tuple(tuple(Q(entry) for entry in row) for row in rows)
    if not result or not result[0]:
        raise ValueError("rational matrix must be nonempty")
    width = len(result[0])
    if any(len(row) != width for row in result):
        raise ValueError("ragged rational matrix")
    return result


def shape(value: Matrix | QMatrix) -> tuple[int, int]:
    return len(value), len(value[0])


def zero(rows: int, columns: int) -> Matrix:
    return tuple(tuple(ZERO for _ in range(columns)) for _ in range(rows))


def qzero(rows: int, columns: int) -> QMatrix:
    return tuple(tuple(Q(0) for _ in range(columns)) for _ in range(rows))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(ONE if row == column else ZERO for column in range(size))
        for row in range(size)
    )


def matrix_unit(size: int, row: int, column: int) -> Matrix:
    return tuple(
        tuple(ONE if (left, right) == (row, column) else ZERO for right in range(size))
        for left in range(size)
    )


def qidentity(size: int) -> QMatrix:
    return tuple(
        tuple(Q(1) if row == column else Q(0) for column in range(size))
        for row in range(size)
    )


def transpose(value: Matrix) -> Matrix:
    rows, columns = shape(value)
    return tuple(tuple(value[row][column] for row in range(rows)) for column in range(columns))


def adjoint(value: Matrix) -> Matrix:
    return tuple(tuple(entry.conjugate() for entry in row) for row in transpose(value))


def matadd(left: Matrix, right: Matrix) -> Matrix:
    if shape(left) != shape(right):
        raise ValueError("matrix-add shape mismatch")
    rows, columns = shape(left)
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(columns))
        for row in range(rows)
    )


def matscale(coefficient: Any, value: Matrix) -> Matrix:
    factor = scalar(coefficient)
    return tuple(tuple(factor * entry for entry in row) for row in value)


def matsub(left: Matrix, right: Matrix) -> Matrix:
    return matadd(left, matscale(-1, right))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_columns = shape(left)
    right_rows, right_columns = shape(right)
    if left_columns != right_rows:
        raise ValueError(f"matrix-product shape mismatch {shape(left)} x {shape(right)}")
    return tuple(
        tuple(
            sum(
                (left[row][middle] * right[middle][column] for middle in range(left_columns)),
                ZERO,
            )
            for column in range(right_columns)
        )
        for row in range(left_rows)
    )


def matrix_sum(values: Sequence[Matrix]) -> Matrix:
    if not values:
        raise ValueError("cannot sum empty matrix family")
    result = zero(*shape(values[0]))
    for value in values:
        result = matadd(result, value)
    return result


def kron(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_columns = shape(left)
    right_rows, right_columns = shape(right)
    return tuple(
        tuple(
            left[row // right_rows][column // right_columns]
            * right[row % right_rows][column % right_columns]
            for column in range(left_columns * right_columns)
        )
        for row in range(left_rows * right_rows)
    )


def trace(value: Matrix) -> GQ:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("trace requires square matrix")
    return sum((value[index][index] for index in range(rows)), ZERO)


def determinant(value: Matrix) -> GQ:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("determinant requires square matrix")
    work = [list(row) for row in value]
    result = ONE
    for column in range(columns):
        pivot_row = next((row for row in range(column, rows) if work[row][column] != ZERO), None)
        if pivot_row is None:
            return ZERO
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            result = -result
        pivot = work[column][column]
        result = result * pivot
        for row in range(column + 1, rows):
            factor = work[row][column] / pivot
            for index in range(column, columns):
                work[row][index] = work[row][index] - factor * work[column][index]
    return result


def principal_submatrix(value: Matrix, indices: Sequence[int]) -> Matrix:
    return tuple(tuple(value[row][column] for column in indices) for row in indices)


def matrix_rank(value: Matrix) -> int:
    rows, columns = shape(value)
    work = [list(row) for row in value]
    rank_value = 0
    for column in range(columns):
        pivot_row = next((row for row in range(rank_value, rows) if work[row][column] != ZERO), None)
        if pivot_row is None:
            continue
        work[rank_value], work[pivot_row] = work[pivot_row], work[rank_value]
        pivot = work[rank_value][column]
        work[rank_value] = [entry / pivot for entry in work[rank_value]]
        for row in range(rows):
            if row == rank_value:
                continue
            factor = work[row][column]
            if factor != ZERO:
                work[row] = [
                    work[row][index] - factor * work[rank_value][index]
                    for index in range(columns)
                ]
        rank_value += 1
        if rank_value == rows:
            break
    return rank_value


def is_hermitian(value: Matrix) -> bool:
    rows, columns = shape(value)
    return rows == columns and value == adjoint(value)


def is_psd(value: Matrix) -> bool:
    """Exact PSD test by the principal-minor criterion."""

    rows, columns = shape(value)
    if rows != columns or not is_hermitian(value):
        return False
    for size in range(1, rows + 1):
        for indices in itertools.combinations(range(rows), size):
            minor = determinant(principal_submatrix(value, indices))
            if minor.im != 0 or minor.re < 0:
                return False
    return True


def matrix_text(value: Matrix) -> list[list[str]]:
    return [[gtext(entry) for entry in row] for row in value]


def qmatrix_text(value: QMatrix) -> list[list[str]]:
    return [[qtext(entry) for entry in row] for row in value]


def gram(coefficients: Matrix, *, columns_if_empty: int | None = None) -> Matrix:
    if not coefficients:
        if columns_if_empty is None:
            raise ValueError("empty Gram factor needs its column count")
        return zero(columns_if_empty, columns_if_empty)
    return matmul(adjoint(coefficients), coefficients)


def history_gram(histories: Sequence[Matrix]) -> tuple[tuple[Matrix, ...], ...]:
    if not histories:
        raise ValueError("empty history family")
    target, source = shape(histories[0])
    if any(shape(history) != (target, source) for history in histories):
        raise ValueError("histories lack a shared typed boundary")
    return tuple(
        tuple(matmul(adjoint(left), right) for right in histories)
        for left in histories
    )


def class_operators(histories: Sequence[Matrix], coefficients: Matrix) -> tuple[Matrix, ...]:
    _, width = shape(coefficients)
    if width != len(histories):
        raise ValueError("coefficient/history mismatch")
    history_gram(histories)
    return tuple(
        matrix_sum(tuple(matscale(coefficient, history) for coefficient, history in zip(row, histories)))
        for row in coefficients
    )


def completeness_from_kernel(histories: Sequence[Matrix], kernel: Matrix) -> Matrix:
    if shape(kernel) != (len(histories), len(histories)):
        raise ValueError("kernel/history mismatch")
    grams = history_gram(histories)
    return matrix_sum(
        tuple(
            matscale(kernel[left][right], grams[left][right])
            for left in range(len(histories))
            for right in range(len(histories))
        )
    )


def completeness_from_coefficients(histories: Sequence[Matrix], coefficients: Matrix) -> Matrix:
    operators = class_operators(histories, coefficients)
    return matrix_sum(tuple(matmul(adjoint(operator), operator) for operator in operators))


def apply_channel_kernel(histories: Sequence[Matrix], kernel: Matrix, state: Matrix) -> Matrix:
    return matrix_sum(
        tuple(
            matscale(
                kernel[left][right],
                matmul(matmul(histories[right], state), adjoint(histories[left])),
            )
            for left in range(len(histories))
            for right in range(len(histories))
        )
    )


def apply_kraus(kraus: Sequence[Matrix], state: Matrix) -> Matrix:
    if not kraus:
        raise ValueError("empty Kraus family")
    return matrix_sum(tuple(matmul(matmul(operator, state), adjoint(operator)) for operator in kraus))


def apply_heisenberg(kraus: Sequence[Matrix], observable: Matrix) -> Matrix:
    if not kraus:
        raise ValueError("empty Kraus family")
    return matrix_sum(tuple(matmul(matmul(adjoint(operator), observable), operator) for operator in kraus))


def is_complete_kraus(kraus: Sequence[Matrix]) -> bool:
    if not kraus:
        return False
    source = shape(kraus[0])[1]
    return matrix_sum(tuple(matmul(adjoint(operator), operator) for operator in kraus)) == identity(source)


def stinespring_stack(kraus: Sequence[Matrix]) -> Matrix:
    """Return the flag-major stack ``sum_j |j> tensor K_j``."""

    if not kraus:
        raise ValueError("empty Kraus family")
    target, source = shape(kraus[0])
    if any(shape(operator) != (target, source) for operator in kraus):
        raise ValueError("Kraus operators lack a common boundary")
    return tuple(row for operator in kraus for row in operator)


def is_stinespring_isometry(kraus: Sequence[Matrix]) -> bool:
    stacked = stinespring_stack(kraus)
    return matmul(adjoint(stacked), stacked) == identity(shape(stacked)[1])


def factor_integer(value: int) -> dict[int, int]:
    if value <= 0:
        raise ValueError("factorization requires a positive integer")
    remaining = value
    result: dict[int, int] = {}
    prime = 2
    while prime * prime <= remaining:
        while remaining % prime == 0:
            result[prime] = result.get(prime, 0) + 1
            remaining //= prime
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        result[remaining] = result.get(remaining, 0) + 1
    return result


def is_sum_two_integer_squares(value: int) -> bool:
    if value < 0:
        return False
    if value == 0:
        return True
    return all(exponent % 2 == 0 for prime, exponent in factor_integer(value).items() if prime % 4 == 3)


def is_gaussian_norm_rational(value: Q) -> bool:
    value = Q(value)
    if value < 0:
        return False
    if value == 0:
        return True
    numerator = factor_integer(value.numerator)
    denominator = factor_integer(value.denominator)
    primes = set(numerator) | set(denominator)
    return all(
        (numerator.get(prime, 0) - denominator.get(prime, 0)) % 2 == 0
        for prime in primes
        if prime % 4 == 3
    )


def two_squares_integer(value: int) -> tuple[int, int] | None:
    if value < 0:
        return None
    limit = math.isqrt(value)
    for left in range(limit + 1):
        right_squared = value - left * left
        right = math.isqrt(right_squared)
        if right * right == right_squared:
            return left, right
    return None


def four_squares_integer(value: int) -> tuple[int, int, int, int]:
    """Deterministic exact four-square construction by bounded search."""

    if value < 0:
        raise ValueError("four-square input must be nonnegative")
    limit = math.isqrt(value)
    for first in range(limit, -1, -1):
        after_first = value - first * first
        for second in range(math.isqrt(after_first), -1, -1):
            pair = two_squares_integer(after_first - second * second)
            if pair is not None:
                return first, second, pair[0], pair[1]
    raise ArithmeticError("Lagrange four-square search failed")


def gaussian_norm_pair(value: Q) -> tuple[GQ, GQ]:
    """Write a nonnegative rational as the sum of two Gaussian norms."""

    value = Q(value)
    if value < 0:
        raise ValueError("norm decomposition requires a nonnegative rational")
    if value == 0:
        return ZERO, ZERO
    target = value.numerator * value.denominator
    first, second, third, fourth = four_squares_integer(target)
    denominator = value.denominator
    return (
        GQ(Q(first, denominator), Q(second, denominator)),
        GQ(Q(third, denominator), Q(fourth, denominator)),
    )


@dataclass(frozen=True)
class LDL:
    lower: Matrix
    diagonal: tuple[Q, ...]


def hermitian_ldl(value: Matrix) -> LDL:
    """Exact unpivoted Hermitian LDL-dagger for a PSD matrix.

    For a PSD Schur complement, a zero diagonal pivot forces the rest of that
    pivot column to vanish.  The explicit check below handles rank-deficient
    inputs without dividing by zero.
    """

    if not is_psd(value):
        raise ValueError("matrix is not positive semidefinite Hermitian")
    size, _ = shape(value)
    lower = [[ONE if row == column else ZERO for column in range(size)] for row in range(size)]
    diagonal: list[Q] = []
    for column in range(size):
        correction = sum(
            (
                lower[column][prior]
                * GQ(diagonal[prior])
                * lower[column][prior].conjugate()
                for prior in range(column)
            ),
            ZERO,
        )
        pivot = value[column][column] - correction
        if pivot.im != 0 or pivot.re < 0:
            raise ArithmeticError("PSD LDL produced a non-real or negative pivot")
        diagonal.append(pivot.re)
        for row in range(column + 1, size):
            numerator = value[row][column] - sum(
                (
                    lower[row][prior]
                    * GQ(diagonal[prior])
                    * lower[column][prior].conjugate()
                    for prior in range(column)
                ),
                ZERO,
            )
            if pivot.re == 0:
                if numerator != ZERO:
                    raise ArithmeticError("zero PSD pivot has a nonzero residual column")
                lower[row][column] = ZERO
            else:
                lower[row][column] = numerator / pivot
    result = LDL(tuple(tuple(row) for row in lower), tuple(diagonal))
    diagonal_matrix = tuple(
        tuple(GQ(result.diagonal[row]) if row == column else ZERO for column in range(size))
        for row in range(size)
    )
    if matmul(matmul(result.lower, diagonal_matrix), adjoint(result.lower)) != value:
        raise ArithmeticError("LDL reconstruction failed")
    return result


def gaussian_rational_gram_factor(value: Matrix) -> Matrix:
    """Construct ``C`` over Q(i) with ``C^dagger C=value`` and rows <= 2 rank."""

    decomposition = hermitian_ldl(value)
    size, _ = shape(value)
    rows: list[tuple[GQ, ...]] = []
    for index, pivot in enumerate(decomposition.diagonal):
        if pivot == 0:
            continue
        first, second = gaussian_norm_pair(pivot)
        base = tuple(decomposition.lower[column][index].conjugate() for column in range(size))
        for coefficient in (first, second):
            if coefficient != ZERO:
                rows.append(tuple(coefficient * entry for entry in base))
    factor = tuple(rows)
    if gram(factor, columns_if_empty=size) != value:
        raise ArithmeticError("Gaussian-rational Gram reconstruction failed")
    rank_value = matrix_rank(value)
    if len(factor) > 2 * rank_value:
        raise ArithmeticError("Gaussian-rational Gram row bound failed")
    return factor


def qtranspose(value: QMatrix) -> QMatrix:
    rows, columns = shape(value)
    return tuple(tuple(value[row][column] for row in range(rows)) for column in range(columns))


def qmul(left: QMatrix, right: QMatrix) -> QMatrix:
    left_rows, left_columns = shape(left)
    right_rows, right_columns = shape(right)
    if left_columns != right_rows:
        raise ValueError("rational matrix-product shape mismatch")
    return tuple(
        tuple(
            sum((left[row][middle] * right[middle][column] for middle in range(left_columns)), Q(0))
            for column in range(right_columns)
        )
        for row in range(left_rows)
    )


def qscale(coefficient: Q, value: QMatrix) -> QMatrix:
    return tuple(tuple(Q(coefficient) * entry for entry in row) for row in value)


def qadd(left: QMatrix, right: QMatrix) -> QMatrix:
    if shape(left) != shape(right):
        raise ValueError("rational matrix-add shape mismatch")
    rows, columns = shape(left)
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(columns))
        for row in range(rows)
    )


def is_stochastic(value: QMatrix) -> bool:
    """Column-stochastic convention: columns are input sectors."""

    rows, columns = shape(value)
    return rows > 0 and columns > 0 and all(
        all(value[row][column] >= 0 for row in range(rows))
        and sum((value[row][column] for row in range(rows)), Q(0)) == 1
        for column in range(columns)
    )


def output_supports(value: QMatrix) -> tuple[frozenset[int], ...]:
    rows, columns = shape(value)
    return tuple(
        frozenset(row for row in range(rows) if value[row][column] != 0)
        for column in range(columns)
    )


def zero_error_recoverable(value: QMatrix) -> bool:
    if not is_stochastic(value):
        return False
    supports = output_supports(value)
    return all(
        supports[left].isdisjoint(supports[right])
        for left in range(len(supports))
        for right in range(left + 1, len(supports))
    )


def permutation_matrix_q(value: QMatrix) -> bool:
    rows, columns = shape(value)
    if rows != columns:
        return False
    return all(
        sorted(value[row][column] for row in range(rows)) == [Q(0)] * (rows - 1) + [Q(1)]
        for column in range(columns)
    ) and all(
        sorted(value[row][column] for column in range(columns)) == [Q(0)] * (columns - 1) + [Q(1)]
        for row in range(rows)
    )


def diagonal_algebra_covariant(kraus: Sequence[Matrix]) -> bool:
    if not is_complete_kraus(kraus):
        return False
    target = shape(kraus[0])[0]
    source = shape(kraus[0])[1]
    if target != source:
        return False
    for index in range(target):
        projector = tuple(
            tuple(ONE if (row, column) == (index, index) else ZERO for column in range(target))
            for row in range(target)
        )
        moved = apply_heisenberg(kraus, projector)
        if any(moved[row][column] != ZERO for row in range(source) for column in range(source) if row != column):
            return False
    return True


def coarse_grain_channels(weights: Sequence[Q], channels: Sequence[QMatrix]) -> QMatrix:
    if not channels or len(weights) != len(channels):
        raise ValueError("coarse-graining family mismatch")
    if sum((Q(weight) for weight in weights), Q(0)) != 1:
        raise ValueError("coarse-graining weights must sum to one")
    return qadd_many(tuple(qscale(Q(weight), channel) for weight, channel in zip(weights, channels)))


def qadd_many(values: Sequence[QMatrix]) -> QMatrix:
    if not values:
        raise ValueError("cannot sum empty rational matrix family")
    result = qzero(*shape(values[0]))
    for value in values:
        result = qadd(result, value)
    return result


def qrref(value: QMatrix) -> tuple[QMatrix, tuple[int, ...]]:
    work = [list(row) for row in value]
    rows, columns = shape(value)
    pivots: list[int] = []
    pivot_row = 0
    for column in range(columns):
        found = next((row for row in range(pivot_row, rows) if work[row][column] != 0), None)
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        pivot = work[pivot_row][column]
        work[pivot_row] = [entry / pivot for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            coefficient = work[row][column]
            if coefficient != 0:
                work[row] = [
                    work[row][index] - coefficient * work[pivot_row][index]
                    for index in range(columns)
                ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return tuple(tuple(row) for row in work), tuple(pivots)


def qrank(value: QMatrix) -> int:
    return len(qrref(value)[1])


def affine_solution_dimension(coefficients: QMatrix, target: Sequence[Q]) -> int | None:
    rows, columns = shape(coefficients)
    if len(target) != rows:
        raise ValueError("affine target length mismatch")
    augmented = tuple(tuple(coefficients[row]) + (Q(target[row]),) for row in range(rows))
    if qrank(augmented) != qrank(coefficients):
        return None
    return columns - qrank(coefficients)


def licensed_recovery_exists(encoded_channel: QMatrix, readouts: Sequence[QMatrix]) -> bool:
    """A licensed readout recovers exactly up to a sector permutation."""

    return any(permutation_matrix_q(qmul(readout, encoded_channel)) for readout in readouts)


def semigroup_closure(generators: Sequence[QMatrix], *, cap: int = 4096) -> tuple[QMatrix, ...]:
    if not generators:
        raise ValueError("empty continuation grammar")
    dimension = shape(generators[0])[0]
    if any(shape(generator) != (dimension, dimension) for generator in generators):
        raise ValueError("continuation generators must be square on one catalogue")
    known: set[QMatrix] = {qidentity(dimension)}
    frontier = [qidentity(dimension)]
    while frontier:
        current = frontier.pop(0)
        for generator in generators:
            candidate = qmul(generator, current)
            if candidate not in known:
                known.add(candidate)
                frontier.append(candidate)
                if len(known) > cap:
                    raise ValueError("continuation semigroup exceeded the exact closure cap")
    return tuple(sorted(known, key=qmatrix_text))


def all_word_recoverability(
    encoding: QMatrix,
    generators: Sequence[QMatrix],
    readouts: Sequence[QMatrix],
) -> dict[str, Any]:
    closure = semigroup_closure(generators)
    mathematical = tuple(zero_error_recoverable(qmul(word, encoding)) for word in closure)
    licensed = tuple(licensed_recovery_exists(qmul(word, encoding), readouts) for word in closure)
    return {
        "word_count": len(closure),
        "mathematical_all": all(mathematical),
        "licensed_all": all(licensed),
        "mathematical_vector": mathematical,
        "licensed_vector": licensed,
    }


def channel_signature(histories: Sequence[Matrix], kernel: Matrix) -> tuple[str, ...]:
    source = shape(histories[0])[1]
    signatures: list[str] = []
    for left in range(source):
        for right in range(source):
            output = apply_channel_kernel(histories, kernel, matrix_unit(source, left, right))
            signatures.append(",".join(gtext(entry) for row in output for entry in row))
    return tuple(signatures)


def gate(name: str, passed: bool, evidence: str) -> dict[str, Any]:
    return {"gate": name, "passed": bool(passed), "evidence": evidence}


def public_calibration(mutant: str | None = None) -> dict[str, Any]:
    """Run public examples whose answers are stated in their constructors."""

    # Public Gram examples are not CEL's registered physical resource witnesses.
    public_psd = matrix([[2, I], [-I, 1]])
    public_singular = matrix([[1, 1], [1, 1]])
    public_non_psd = matrix([[1, 2], [2, 1]])
    factor_psd = gaussian_rational_gram_factor(public_psd)
    factor_singular = gaussian_rational_gram_factor(public_singular)
    try:
        gaussian_rational_gram_factor(public_non_psd)
        non_psd_refused = False
    except ValueError:
        non_psd_refused = True
    if mutant == "public-factor":
        factor_psd = tuple(tuple(entry + (ONE if (row, column) == (0, 0) else ZERO) for column, entry in enumerate(line)) for row, line in enumerate(factor_psd))

    # Public channel controls: swap preserves a two-sector record; reset merges it
    # while its adjoint still preserves the diagonal algebra.
    swap = matrix([[0, 1], [1, 0]])
    reset_kraus = (matrix([[1, 0], [0, 0]]), matrix([[0, 1], [0, 0]]))
    swap_kraus = (swap,)
    reset_classical = qmatrix([[1, 1], [0, 0]])
    swap_classical = qmatrix([[0, 1], [1, 0]])
    if mutant == "public-recovery":
        reset_classical = qidentity(2)

    # Branch information can be sufficient before coarse-graining and lost
    # afterwards.  Identity/flip with equal weights is the public calibration.
    identity_classical = qidentity(2)
    branch_channels = (identity_classical, swap_classical)
    coarse = coarse_grain_channels((Q(1, 2), Q(1, 2)), branch_channels)

    # A finite all-word grammar and its exact licensed recovery certificate.
    closure = semigroup_closure((swap_classical,))
    all_word = all_word_recoverability(qidentity(2), (swap_classical,), (qidentity(2), swap_classical))
    if mutant == "public-grammar":
        all_word = dict(all_word)
        all_word["licensed_all"] = False

    # Public dilation uses a projective measurement, separate from CEL/JCV.
    projector_zero = matrix([[1, 0], [0, 0]])
    projector_one = matrix([[0, 0], [0, 1]])
    public_kraus = (projector_zero, projector_one)
    stack = stinespring_stack(public_kraus)

    public_norm = Q(5, 3)
    norm_pair = gaussian_norm_pair(public_norm)
    measurements = {
        "gram": {
            "complex_input": matrix_text(public_psd),
            "complex_factor": matrix_text(factor_psd),
            "complex_rank": matrix_rank(public_psd),
            "singular_factor": matrix_text(factor_singular),
            "singular_rank": matrix_rank(public_singular),
            "non_psd": is_psd(public_non_psd),
            "non_psd_refused": non_psd_refused,
            "public_norm": qtext(public_norm),
            "public_norm_pair": [gtext(value) for value in norm_pair],
        },
        "recoverability": {
            "reset_algebra_covariant": diagonal_algebra_covariant(reset_kraus),
            "reset_zero_error": zero_error_recoverable(reset_classical),
            "swap_zero_error": zero_error_recoverable(swap_classical),
            "branchwise": [zero_error_recoverable(channel) for channel in branch_channels],
            "coarse_channel": qmatrix_text(coarse),
            "coarse_zero_error": zero_error_recoverable(coarse),
            "closure_size": len(closure),
            "all_word": all_word,
        },
        "dilation": {
            "complete": is_complete_kraus(public_kraus),
            "stack": matrix_text(stack),
            "isometry": is_stinespring_isometry(public_kraus),
        },
    }

    gates = [
        gate(
            "PUB-COMPLEX-LDL-GRAM",
            gram(factor_psd) == public_psd and len(factor_psd) <= 2 * matrix_rank(public_psd),
            f"rank={matrix_rank(public_psd)} rows={len(factor_psd)}",
        ),
        gate(
            "PUB-SINGULAR-LDL-GRAM",
            gram(factor_singular) == public_singular and len(factor_singular) <= 2 * matrix_rank(public_singular),
            f"rank={matrix_rank(public_singular)} rows={len(factor_singular)}",
        ),
        gate(
            "PUB-NONPSD-REFUSAL",
            not is_psd(public_non_psd) and non_psd_refused,
            f"psd={is_psd(public_non_psd)} refused={non_psd_refused}",
        ),
        gate(
            "PUB-FOUR-SQUARE-NORM",
            sum((value.norm2() for value in norm_pair), Q(0)) == public_norm,
            f"{qtext(public_norm)}={' + '.join(gtext(value) for value in norm_pair)} norms",
        ),
        gate(
            "PUB-RESET-SEPARATES-COVARIANCE-RECOVERY",
            is_complete_kraus(reset_kraus)
            and diagonal_algebra_covariant(reset_kraus)
            and not zero_error_recoverable(reset_classical),
            f"covariant={diagonal_algebra_covariant(reset_kraus)} recoverable={zero_error_recoverable(reset_classical)}",
        ),
        gate(
            "PUB-RELABEL-RECOVERABLE",
            is_complete_kraus(swap_kraus)
            and zero_error_recoverable(swap_classical),
            f"recoverable={zero_error_recoverable(swap_classical)}",
        ),
        gate(
            "PUB-BRANCH-COARSE-GRAIN",
            all(zero_error_recoverable(channel) for channel in branch_channels)
            and not zero_error_recoverable(coarse),
            f"branch={','.join(str(zero_error_recoverable(channel)).lower() for channel in branch_channels)} coarse={zero_error_recoverable(coarse)}",
        ),
        gate(
            "PUB-SEMIGROUP-CERTIFICATE",
            len(closure) == 2 and all_word["mathematical_all"] and all_word["licensed_all"],
            f"words={len(closure)} mathematical={all_word['mathematical_all']} licensed={all_word['licensed_all']}",
        ),
        gate(
            "PUB-STINESPRING-ISOMETRY",
            is_complete_kraus(public_kraus) and is_stinespring_isometry(public_kraus),
            f"shape={shape(stack)}",
        ),
    ]
    return {
        "schema": "cel-public-v1",
        "scope": {
            "arithmetic": "Q and Q(i); no float arithmetic",
            "role": "generic public calibrations only; no CEL physical fixture, recurrence doctrine, selected coupling, or Paper 7 outcome",
            "psd": "exact principal-minor certification followed by constructive Hermitian LDL-dagger and four-square pivots",
            "recovery": "finite classical zero-error and licensed-readout semantics; actualization is not represented",
        },
        "measurements": measurements,
        "gates": gates,
    }


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def render_public(result: Mapping[str, Any]) -> str:
    lines = ["CEL GENERIC PUBLIC CALIBRATION", f"schema: {result['schema']}"]
    for row in result["gates"]:
        state = "PASS" if row["passed"] else "FAIL"
        lines.append(f"{state} {row['gate']} :: {row['evidence']}")
    lines.append(f"gate-count: {len(result['gates'])}")
    lines.append(f"all-pass: {str(all(row['passed'] for row in result['gates'])).lower()}")
    return "\n".join(lines) + "\n"


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


def finalized_receipt(result: Mapping[str, Any], transcript: str) -> dict[str, Any]:
    receipt = dict(result)
    receipt["transcript_sha256"] = hashlib.sha256(transcript.encode("utf-8")).hexdigest()
    receipt["seals"] = {key: digest(receipt[key]) for key in ("schema", "scope", "measurements", "gates")}
    return receipt


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=root / "cel_public_output.txt")
    parser.add_argument("--receipt", type=Path, default=root / "cel_public_receipt.json")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument(
        "--mutant",
        choices=("public-factor", "public-recovery", "public-grammar"),
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.selftest and args.mutant is not None:
        print("REFUSE CEL-PUBLIC-CLI :: selftest and mutant are mutually exclusive", file=sys.stderr)
        return 2
    if args.output.resolve().exists() or args.receipt.resolve().exists():
        print("REFUSE CEL-PUBLIC-TARGET :: output or receipt already exists", file=sys.stderr)
        return 1
    mutant = "public-factor" if args.selftest else args.mutant
    result = public_calibration(mutant)
    failed = [row["gate"] for row in result["gates"] if not row["passed"]]
    if failed:
        label = "CEL-PUBLIC-SELFTEST" if args.selftest else "CEL-PUBLIC-GATE"
        print(f"REFUSE {label} :: {','.join(failed)}", file=sys.stderr)
        return 1
    transcript = render_public(result)
    receipt = finalized_receipt(result, transcript)
    atomic_write(args.output.resolve(), transcript.encode("utf-8"))
    atomic_write(args.receipt.resolve(), canonical_json(receipt))
    sys.stdout.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
