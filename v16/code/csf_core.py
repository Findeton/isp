#!/usr/bin/env python3
"""Generic exact machinery for CSF Paper 6.

This module contains no CSF recurring-context physical fixture, target
verdict, selected kernel, or Paper 6 result. Its CLI runs only constructor-
stated public calibrations.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import sys
import tempfile
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence


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
        if isinstance(value, (int, Fraction)):
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
        value = self.norm2()
        if value == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        return GQ(self.re / value, -self.im / value)

    def __truediv__(self, other: Any) -> "GQ":
        return self * GQ.coerce(other).inverse()


ZERO = GQ(0)
ONE = GQ(1)
I = GQ(0, 1)
Matrix = tuple[tuple[GQ, ...], ...]
QMatrix = tuple[tuple[Q, ...], ...]


def qtext(value: Q) -> str:
    value = Q(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


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


def matrix(rows: Sequence[Sequence[Any]]) -> Matrix:
    result = tuple(tuple(scalar(entry) for entry in row) for row in rows)
    if not result or not result[0]:
        raise ValueError("matrix must be nonempty")
    width = len(result[0])
    if any(len(row) != width for row in result):
        raise ValueError("ragged matrix")
    return result


def shape(value: Matrix) -> tuple[int, int]:
    return len(value), len(value[0])


def zero(rows: int, columns: int) -> Matrix:
    return tuple(tuple(ZERO for _ in range(columns)) for _ in range(rows))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(ONE if row == column else ZERO for column in range(size))
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


def matrix_unit(size: int, row: int, column: int) -> Matrix:
    return tuple(
        tuple(ONE if (i, j) == (row, column) else ZERO for j in range(size))
        for i in range(size)
    )


def matrix_equal(left: Matrix, right: Matrix) -> bool:
    return left == right


def is_zero(value: Matrix) -> bool:
    return all(entry == ZERO for row in value for entry in row)


def is_hermitian(value: Matrix) -> bool:
    return shape(value)[0] == shape(value)[1] and value == adjoint(value)


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


def is_psd_by_principal_minors(value: Matrix) -> bool:
    """Exact finite PSD certificate by all principal minors.

    This is intended only for the small registered matrices, not advertised as
    a general-purpose semidefinite solver.
    """

    rows, columns = shape(value)
    if rows != columns or not is_hermitian(value):
        return False
    for size in range(1, rows + 1):
        for indices in itertools.combinations(range(rows), size):
            minor = determinant(principal_submatrix(value, indices))
            if minor.im != 0 or minor.re < 0:
                return False
    return True


def qmatrix(rows: Sequence[Sequence[Any]]) -> QMatrix:
    result = tuple(tuple(Q(entry) for entry in row) for row in rows)
    if not result:
        return tuple()
    width = len(result[0])
    if any(len(row) != width for row in result):
        raise ValueError("ragged rational matrix")
    return result


def rref(value: QMatrix) -> tuple[QMatrix, tuple[int, ...]]:
    if not value:
        return tuple(), tuple()
    work = [list(row) for row in value]
    rows = len(work)
    columns = len(work[0])
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
            factor = work[row][column]
            if factor != 0:
                work[row] = [
                    work[row][index] - factor * work[pivot_row][index]
                    for index in range(columns)
                ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return tuple(tuple(entry for entry in row) for row in work), tuple(pivots)


def rank(value: QMatrix) -> int:
    return len(rref(value)[1])


def nullspace(value: QMatrix) -> tuple[tuple[Q, ...], ...]:
    if not value:
        return tuple()
    reduced, pivots = rref(value)
    columns = len(value[0])
    free = [column for column in range(columns) if column not in pivots]
    basis: list[tuple[Q, ...]] = []
    for free_column in free:
        vector = [Q(0) for _ in range(columns)]
        vector[free_column] = Q(1)
        for row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[row][free_column]
        basis.append(tuple(vector))
    return tuple(basis)


def hermitian_basis(size: int) -> tuple[tuple[str, Matrix], ...]:
    result: list[tuple[str, Matrix]] = []
    for index in range(size):
        result.append((f"d{index}", matrix_unit(size, index, index)))
    for left in range(size):
        for right in range(left + 1, size):
            real = matadd(matrix_unit(size, left, right), matrix_unit(size, right, left))
            imaginary = matadd(
                matscale(I, matrix_unit(size, left, right)),
                matscale(-I, matrix_unit(size, right, left)),
            )
            result.append((f"r{left}{right}", real))
            result.append((f"i{left}{right}", imaginary))
    return tuple(result)


def flatten_complex(value: Matrix) -> tuple[Q, ...]:
    return tuple(component for row in value for entry in row for component in (entry.re, entry.im))


def gram_kernel(coefficients: Sequence[Sequence[GQ]]) -> Matrix:
    if not coefficients or not coefficients[0]:
        raise ValueError("coefficient matrix must be nonempty")
    width = len(coefficients[0])
    if any(len(row) != width for row in coefficients):
        raise ValueError("ragged coefficient matrix")
    return tuple(
        tuple(
            sum(
                (coefficients[port][left].conjugate() * coefficients[port][right]
                 for port in range(len(coefficients))),
                ZERO,
            )
            for right in range(width)
        )
        for left in range(width)
    )


def history_gram(histories: Sequence[Matrix]) -> tuple[tuple[Matrix, ...], ...]:
    if not histories:
        raise ValueError("empty history family")
    target, source = shape(histories[0])
    if any(shape(history) != (target, source) for history in histories):
        raise ValueError("histories lack common typed boundary")
    return tuple(
        tuple(matmul(adjoint(left), right) for right in histories)
        for left in histories
    )


def class_operators(histories: Sequence[Matrix], coefficients: Sequence[Sequence[GQ]]) -> tuple[Matrix, ...]:
    if any(len(row) != len(histories) for row in coefficients):
        raise ValueError("coefficient/history mismatch")
    history_gram(histories)
    return tuple(
        matrix_sum(tuple(matscale(coefficient, history) for coefficient, history in zip(row, histories)))
        for row in coefficients
    )


def completeness_from_coefficients(histories: Sequence[Matrix], coefficients: Sequence[Sequence[GQ]]) -> Matrix:
    operators = class_operators(histories, coefficients)
    return matrix_sum(tuple(matmul(adjoint(operator), operator) for operator in operators))


def completeness_from_kernel(histories: Sequence[Matrix], kernel: Matrix) -> Matrix:
    if shape(kernel) != (len(histories), len(histories)):
        raise ValueError("kernel/history mismatch")
    grams = history_gram(histories)
    terms = tuple(
        matscale(kernel[left][right], grams[left][right])
        for left in range(len(histories))
        for right in range(len(histories))
    )
    return matrix_sum(terms)


def apply_channel_coefficients(
    histories: Sequence[Matrix], coefficients: Sequence[Sequence[GQ]], state: Matrix
) -> Matrix:
    operators = class_operators(histories, coefficients)
    return matrix_sum(tuple(matmul(matmul(operator, state), adjoint(operator)) for operator in operators))


def apply_channel_kernel(histories: Sequence[Matrix], kernel: Matrix, state: Matrix) -> Matrix:
    terms = tuple(
        matscale(
            kernel[left][right],
            matmul(matmul(histories[right], state), adjoint(histories[left])),
        )
        for left in range(len(histories))
        for right in range(len(histories))
    )
    return matrix_sum(terms)


def port_outputs(
    histories: Sequence[Matrix], coefficients: Sequence[Sequence[GQ]], state: Matrix
) -> tuple[Matrix, ...]:
    return tuple(
        matmul(matmul(operator, state), adjoint(operator))
        for operator in class_operators(histories, coefficients)
    )


def trace(value: Matrix) -> GQ:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("trace requires square matrix")
    return sum((value[index][index] for index in range(rows)), ZERO)


def affine_completeness_system(histories: Sequence[Matrix]) -> tuple[tuple[str, ...], QMatrix, tuple[Q, ...]]:
    basis = hermitian_basis(len(histories))
    columns = [flatten_complex(completeness_from_kernel(histories, element)) for _, element in basis]
    target = flatten_complex(identity(shape(histories[0])[1]))
    rows = tuple(tuple(columns[column][row] for column in range(len(columns))) for row in range(len(target)))
    return tuple(name for name, _ in basis), rows, target


def stack_affine_systems(
    systems: Sequence[tuple[tuple[str, ...], QMatrix, tuple[Q, ...]]]
) -> tuple[tuple[str, ...], QMatrix, tuple[Q, ...]]:
    if not systems:
        raise ValueError("empty affine system family")
    names = systems[0][0]
    if any(system[0] != names for system in systems):
        raise ValueError("coordinate dictionaries differ")
    rows = tuple(row for _, matrix_rows, _ in systems for row in matrix_rows)
    target = tuple(entry for _, _, rhs in systems for entry in rhs)
    return names, rows, target


def affine_dimension(system: tuple[tuple[str, ...], QMatrix, tuple[Q, ...]]) -> int | None:
    names, rows, target = system
    augmented = tuple(tuple(row) + (target[index],) for index, row in enumerate(rows))
    if rank(augmented) != rank(rows):
        return None
    return len(names) - rank(rows)


def invariance_system(size: int, transformation: Matrix) -> tuple[tuple[str, ...], QMatrix, tuple[Q, ...]]:
    if shape(transformation) != (size, size):
        raise ValueError("history transformation shape mismatch")
    basis = hermitian_basis(size)
    columns = [
        flatten_complex(matsub(matmul(matmul(adjoint(transformation), element), transformation), element))
        for _, element in basis
    ]
    target = tuple(Q(0) for _ in columns[0])
    rows = tuple(tuple(columns[column][row] for column in range(len(columns))) for row in range(len(target)))
    return tuple(name for name, _ in basis), rows, target


def evaluate_coordinates(size: int, coordinates: Sequence[Q]) -> Matrix:
    basis = hermitian_basis(size)
    if len(coordinates) != len(basis):
        raise ValueError("Hermitian coordinate length mismatch")
    return matrix_sum(tuple(matscale(coefficient, element) for coefficient, (_, element) in zip(coordinates, basis)))


def tangent_extreme_nullity(
    histories: Sequence[Matrix],
    support_embedding: Matrix,
    symmetries: Sequence[Matrix] = (),
) -> int:
    history_count = len(histories)
    if shape(support_embedding)[0] != history_count:
        raise ValueError("support embedding/history mismatch")
    support_size = shape(support_embedding)[1]
    support_basis = hermitian_basis(support_size)
    perturbations = tuple(
        matmul(matmul(support_embedding, element), adjoint(support_embedding))
        for _, element in support_basis
    )
    def constrained_column(perturbation: Matrix) -> tuple[Q, ...]:
        parts = list(flatten_complex(completeness_from_kernel(histories, perturbation)))
        for transformation in symmetries:
            moved = matmul(matmul(adjoint(transformation), perturbation), transformation)
            parts.extend(flatten_complex(matsub(moved, perturbation)))
        return tuple(parts)

    columns = [constrained_column(perturbation) for perturbation in perturbations]
    rows = tuple(tuple(columns[column][row] for column in range(len(columns))) for row in range(len(columns[0])))
    return len(perturbations) - rank(rows)


def channel_signature(histories: Sequence[Matrix], kernel: Matrix) -> tuple[str, ...]:
    source = shape(histories[0])[1]
    return tuple(
        ",".join(gtext(entry) for row in apply_channel_kernel(histories, kernel, matrix_unit(source, left, right)) for entry in row)
        for left in range(source)
        for right in range(source)
    )


def matrix_text(value: Matrix) -> list[list[str]]:
    return [[gtext(entry) for entry in row] for row in value]


def gate(name: str, passed: bool, evidence: str) -> dict[str, Any]:
    return {"gate": name, "passed": bool(passed), "evidence": evidence}


def public_calibration(mutant: str | None = None) -> dict[str, Any]:
    """Run public examples whose answers are stated in their constructors."""

    identity_two = identity(2)
    z_two = matrix([[1, 0], [0, -1]])
    histories_jcv = (identity_two, z_two)
    c_first = (
        (GQ(Q(12, 25)), GQ(Q(-12, 25))),
        (GQ(Q(16, 25)), GQ(Q(9, 25))),
    )
    c_second = (
        (GQ(Q(16, 25)), GQ(Q(-9, 25))),
        (GQ(Q(12, 25)), GQ(Q(12, 25))),
    )
    c_third = (
        (GQ(Q(3, 13)), GQ(Q(-48, 65))),
        (GQ(Q(4, 13)), GQ(Q(36, 65))),
    )
    m_first = gram_kernel(c_first)
    m_second = gram_kernel(c_second)
    m_third = gram_kernel(c_third)
    if mutant == "public-kernel":
        m_second = matadd(m_second, matrix([[0, Q(1, 25)], [Q(1, 25), 0]]))

    state_plus = matscale(Q(1, 2), matrix([[1, 1], [1, 1]]))
    state_zero = matrix([[1, 0], [0, 0]])
    first_channel = apply_channel_coefficients(histories_jcv, c_first, state_plus)
    first_kernel_channel = apply_channel_kernel(histories_jcv, m_first, state_plus)
    second_channel = apply_channel_coefficients(histories_jcv, c_second, state_plus)
    third_channel = apply_channel_coefficients(histories_jcv, c_third, state_plus)
    first_ports = tuple(trace(value) for value in port_outputs(histories_jcv, c_first, state_zero))
    second_ports = tuple(trace(value) for value in port_outputs(histories_jcv, c_second, state_zero))

    scalar_context = (identity(3), identity(3))
    two_context = (identity_two, z_two)
    rich_relative = matrix([[1, 0, 0], [0, I, 0], [0, 0, -1]])
    rich_context = (identity(3), rich_relative)
    scalar_dimension = affine_dimension(affine_completeness_system(scalar_context))
    two_dimension = affine_dimension(affine_completeness_system(two_context))
    rich_dimension = affine_dimension(affine_completeness_system(rich_context))
    intersection = stack_affine_systems(
        (affine_completeness_system(scalar_context), affine_completeness_system(two_context), affine_completeness_system(rich_context))
    )
    intersection_dimension = affine_dimension(intersection)
    swap = matrix([[0, 1], [1, 0]])
    symmetric_intersection = stack_affine_systems((intersection, invariance_system(2, swap)))
    symmetric_dimension = affine_dimension(symmetric_intersection)
    if mutant == "public-intersection":
        symmetric_dimension = intersection_dimension

    rich_left = matrix([[1, 0], [0, 0]])
    rich_middle = matscale(Q(1, 2), identity_two)
    support_left = matrix([[1], [0]])
    support_full = identity_two
    left_extreme_nullity = tangent_extreme_nullity(rich_context, support_left)
    middle_extreme_nullity = tangent_extreme_nullity(rich_context, support_full)
    middle_symmetric_nullity = tangent_extreme_nullity(rich_context, support_full, (swap,))

    f = matrix([[1], [0]])
    g = matrix([[Q(3, 5)], [Q(4, 5)]])
    flagged_two = (kron(identity_two, f), kron(z_two, g))
    flagged_rich = (kron(identity(3), f), kron(rich_relative, g))
    flagged_kernel = matrix([[Q(1, 2), GQ(0, Q(3, 10))], [GQ(0, Q(-3, 10)), Q(1, 2)]])
    flagged_two_residual = matsub(completeness_from_kernel(flagged_two, flagged_kernel), identity(2))
    flagged_rich_residual = matsub(completeness_from_kernel(flagged_rich, flagged_kernel), identity(3))
    if mutant == "public-flag":
        flagged_rich_residual = zero(3, 3)

    non_psd = matrix([[1, 2], [2, 1]])
    factorized_psd = m_first

    measurements = {
        "jcv": {
            "m_first": matrix_text(m_first),
            "m_second": matrix_text(m_second),
            "m_third": matrix_text(m_third),
            "first_ports": [gtext(value) for value in first_ports],
            "second_ports": [gtext(value) for value in second_ports],
            "first_channel": matrix_text(first_channel),
            "third_channel": matrix_text(third_channel),
        },
        "affine_dimensions": {
            "scalar": scalar_dimension,
            "two_phase": two_dimension,
            "rich_phase": rich_dimension,
            "three_context_intersection": intersection_dimension,
            "exchange_fixed_intersection": symmetric_dimension,
        },
        "extremality": {
            "rich_left_tangent_nullity": left_extreme_nullity,
            "rich_middle_tangent_nullity": middle_extreme_nullity,
            "rich_middle_exchange_tangent_nullity": middle_symmetric_nullity,
            "note": "extremality is relative to the registered affine constraints",
        },
        "flags": {
            "overlap": gtext(matmul(adjoint(f), g)[0][0]),
            "two_phase_residual": matrix_text(flagged_two_residual),
            "rich_phase_residual": matrix_text(flagged_rich_residual),
        },
        "psd": {
            "factorized": is_psd_by_principal_minors(factorized_psd),
            "negative_control": is_psd_by_principal_minors(non_psd),
        },
    }

    expected_first_m = matrix([[Q(16, 25), 0], [0, Q(9, 25)]])
    expected_third_m = matrix([[Q(25, 169), 0], [0, Q(144, 169)]])
    gates = [
        gate("PUB-M-FACTORIZATION", m_first == expected_first_m and m_second == expected_first_m, f"M1={matrix_text(m_first)} M2={matrix_text(m_second)}"),
        gate("PUB-COMPLETENESS-FACTORS-THROUGH-M", completeness_from_coefficients(histories_jcv, c_first) == completeness_from_kernel(histories_jcv, m_first) == identity_two, f"complete={matrix_text(completeness_from_kernel(histories_jcv, m_first))}"),
        gate("PUB-CHANNEL-FACTORS-THROUGH-M", first_channel == first_kernel_channel == second_channel, f"Phi={matrix_text(first_channel)}"),
        gate("PUB-CALIBRATED-FIBER-MOVES", first_ports != second_ports and first_ports[0] == ZERO and second_ports[0] == GQ(Q(49, 625)), f"p0={gtext(first_ports[0])},{gtext(second_ports[0])}"),
        gate("PUB-THIRD-M-MOVES-CHANNEL", m_third == expected_third_m and third_channel != first_channel, f"M3={matrix_text(m_third)}"),
        gate("PUB-AFFINE-DIMENSIONS", (scalar_dimension, two_dimension, rich_dimension) == (3, 2, 1), f"dims={scalar_dimension},{two_dimension},{rich_dimension}"),
        gate("PUB-RECURRING-INTERSECTION", intersection_dimension == 1 and symmetric_dimension == 0, f"intersection={intersection_dimension} exchange={symmetric_dimension}"),
        gate("PUB-EXTREME-TANGENT", left_extreme_nullity == 0 and middle_extreme_nullity == 1 and middle_symmetric_nullity == 0 and is_psd_by_principal_minors(rich_left) and is_psd_by_principal_minors(rich_middle), f"nullities={left_extreme_nullity},{middle_extreme_nullity},{middle_symmetric_nullity}"),
        gate("PUB-FLAG-SPECTRAL-SEPARATION", is_zero(flagged_two_residual) and not is_zero(flagged_rich_residual), f"two={matrix_text(flagged_two_residual)} rich={matrix_text(flagged_rich_residual)}"),
        gate("PUB-PSD-CONTROLS", is_psd_by_principal_minors(factorized_psd) and not is_psd_by_principal_minors(non_psd), f"factorized={is_psd_by_principal_minors(factorized_psd)} nonpsd={is_psd_by_principal_minors(non_psd)}"),
        gate("PUB-CHANNEL-SIGNATURE", channel_signature(histories_jcv, m_first) == channel_signature(histories_jcv, m_second), f"signature-size={len(channel_signature(histories_jcv, m_first))}"),
    ]
    return {
        "schema": "csf-public-v1",
        "scope": {
            "arithmetic": "Q and Q(i)",
            "role": "generic public calibrations only; no CSF recurring-context physical fixture or outcome",
            "psd": "all principal minors, registered matrices of order at most two",
        },
        "measurements": measurements,
        "gates": gates,
    }


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def render_public(result: Mapping[str, Any]) -> str:
    lines = ["CSF GENERIC PUBLIC CALIBRATION", f"schema: {result['schema']}"]
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
    parser.add_argument("--output", type=Path, default=root / "csf_public_output.txt")
    parser.add_argument("--receipt", type=Path, default=root / "csf_public_receipt.json")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument(
        "--mutant",
        choices=("public-kernel", "public-intersection", "public-flag"),
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.selftest and args.mutant is not None:
        print("REFUSE CSF-PUBLIC-CLI :: selftest and mutant are mutually exclusive", file=sys.stderr)
        return 2
    mutant = "public-kernel" if args.selftest else args.mutant
    result = public_calibration(mutant)
    failed = [row["gate"] for row in result["gates"] if not row["passed"]]
    if failed:
        label = "CSF-PUBLIC-SELFTEST" if args.selftest else "CSF-PUBLIC-GATE"
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
