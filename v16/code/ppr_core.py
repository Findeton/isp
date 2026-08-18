#!/usr/bin/env python3
"""Generic exact core for PPR.

This module contains no PPR physical fixture and no primary verdict.  It
provides exact Gaussian-rational linear algebra, typed continuation-stable
null spaces, quotient descent, contextual pullbacks, finite record-partition
censuses, channel/instrument comparison, and graph/path utilities.  Its CLI
runs public calibrations only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class GQ:
    """A Gaussian rational number."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __init__(self, re: object = 0, im: object = 0) -> None:
        object.__setattr__(self, "re", _fraction(re))
        object.__setattr__(self, "im", _fraction(im))

    def __add__(self, other: object) -> "GQ":
        rhs = gq(other)
        return GQ(self.re + rhs.re, self.im + rhs.im)

    def __radd__(self, other: object) -> "GQ":
        return self + other

    def __sub__(self, other: object) -> "GQ":
        rhs = gq(other)
        return GQ(self.re - rhs.re, self.im - rhs.im)

    def __rsub__(self, other: object) -> "GQ":
        return gq(other) - self

    def __neg__(self) -> "GQ":
        return GQ(-self.re, -self.im)

    def __mul__(self, other: object) -> "GQ":
        rhs = gq(other)
        return GQ(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    def __rmul__(self, other: object) -> "GQ":
        return self * other

    def __truediv__(self, other: object) -> "GQ":
        rhs = gq(other)
        den = rhs.re * rhs.re + rhs.im * rhs.im
        if den == 0:
            raise ZeroDivisionError("Gaussian-rational division by zero")
        return GQ(
            (self.re * rhs.re + self.im * rhs.im) / den,
            (self.im * rhs.re - self.re * rhs.im) / den,
        )

    def conjugate(self) -> "GQ":
        return GQ(self.re, -self.im)

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0

    def abs2(self) -> Fraction:
        return self.re * self.re + self.im * self.im

    def text(self) -> str:
        if self.im == 0:
            return _fraction_text(self.re)
        if self.re == 0:
            if self.im == 1:
                return "i"
            if self.im == -1:
                return "-i"
            return f"{_fraction_text(self.im)}i"
        sign = "+" if self.im > 0 else "-"
        imag = abs(self.im)
        imag_text = "" if imag == 1 else _fraction_text(imag)
        return f"{_fraction_text(self.re)}{sign}{imag_text}i"


def _fraction(value: object) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, GQ):
        if value.im != 0:
            raise TypeError("cannot coerce a non-real Gaussian rational")
        return value.re
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, int):
        return Fraction(value)
    raise TypeError(f"unsupported exact scalar {type(value).__name__}")


def gq(value: object = 0, im: object = 0) -> GQ:
    if isinstance(value, GQ) and im == 0:
        return value
    return GQ(value, im)


ZERO = GQ(0)
ONE = GQ(1)
I = GQ(0, 1)

Matrix = list[list[GQ]]
Partition = tuple[tuple[int, ...], ...]


def _fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def matrix(rows: Iterable[Iterable[object]]) -> Matrix:
    out = [[gq(item) for item in row] for row in rows]
    if out:
        width = len(out[0])
        if any(len(row) != width for row in out):
            raise ValueError("ragged matrix")
    return out


def matrix_text(value: Matrix) -> list[list[str]]:
    return [[item.text() for item in row] for row in value]


def shape(value: Matrix, *, ncols_if_empty: int | None = None) -> tuple[int, int]:
    if not value:
        if ncols_if_empty is None:
            raise ValueError("empty matrix needs an explicit column count")
        return 0, ncols_if_empty
    return len(value), len(value[0])


def zeros(nrows: int, ncols: int) -> Matrix:
    return [[ZERO for _ in range(ncols)] for _ in range(nrows)]


def identity(dim: int) -> Matrix:
    return [[ONE if row == col else ZERO for col in range(dim)] for row in range(dim)]


def basis_vector(dim: int, index: int) -> Matrix:
    return [[ONE if row == index else ZERO] for row in range(dim)]


def copy_matrix(value: Matrix) -> Matrix:
    return [row[:] for row in value]


def transpose(value: Matrix) -> Matrix:
    if not value:
        return []
    return [[value[row][col] for row in range(len(value))] for col in range(len(value[0]))]


def dagger(value: Matrix) -> Matrix:
    if not value:
        return []
    return [
        [value[row][col].conjugate() for row in range(len(value))]
        for col in range(len(value[0]))
    ]


def add(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or (left and len(left[0]) != len(right[0])):
        raise ValueError("addition shape mismatch")
    return [
        [left[row][col] + right[row][col] for col in range(len(left[row]))]
        for row in range(len(left))
    ]


def subtract(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or (left and len(left[0]) != len(right[0])):
        raise ValueError("subtraction shape mismatch")
    return [
        [left[row][col] - right[row][col] for col in range(len(left[row]))]
        for row in range(len(left))
    ]


def scale(scalar: object, value: Matrix) -> Matrix:
    coefficient = gq(scalar)
    return [[coefficient * item for item in row] for row in value]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        raise ValueError("multiply requires nonempty typed matrices")
    if len(left[0]) != len(right):
        raise ValueError(f"multiplication shape mismatch {len(left[0])} != {len(right)}")
    out = zeros(len(left), len(right[0]))
    for row in range(len(left)):
        for inner in range(len(right)):
            coefficient = left[row][inner]
            if coefficient.is_zero():
                continue
            for col in range(len(right[0])):
                out[row][col] = out[row][col] + coefficient * right[inner][col]
    return out


def tensor(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        raise ValueError("tensor requires nonempty matrices")
    out = zeros(len(left) * len(right), len(left[0]) * len(right[0]))
    for a_row in range(len(left)):
        for a_col in range(len(left[0])):
            for b_row in range(len(right)):
                for b_col in range(len(right[0])):
                    out[a_row * len(right) + b_row][a_col * len(right[0]) + b_col] = (
                        left[a_row][a_col] * right[b_row][b_col]
                    )
    return out


def direct_sum(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        raise ValueError("direct sum requires nonempty matrices")
    out = zeros(len(left) + len(right), len(left[0]) + len(right[0]))
    for row in range(len(left)):
        for col in range(len(left[0])):
            out[row][col] = left[row][col]
    for row in range(len(right)):
        for col in range(len(right[0])):
            out[len(left) + row][len(left[0]) + col] = right[row][col]
    return out


def matrices_equal(left: Matrix, right: Matrix) -> bool:
    return left == right


def is_zero_matrix(value: Matrix) -> bool:
    return all(item.is_zero() for row in value for item in row)


def stack_rows(values: Sequence[Matrix], ncols: int) -> Matrix:
    out: Matrix = []
    for value in values:
        if value and len(value[0]) != ncols:
            raise ValueError("row-stack shape mismatch")
        out.extend(copy_matrix(value))
    return out


def stack_columns(values: Sequence[Matrix], nrows: int) -> Matrix:
    if not values:
        return zeros(nrows, 0)
    out = [[] for _ in range(nrows)]
    for value in values:
        if len(value) != nrows:
            raise ValueError("column-stack shape mismatch")
        for row in range(nrows):
            out[row].extend(value[row])
    return out


def rref(value: Matrix, *, ncols: int | None = None) -> tuple[Matrix, tuple[int, ...]]:
    if value:
        width = len(value[0])
        if any(len(row) != width for row in value):
            raise ValueError("ragged matrix")
    elif ncols is not None:
        width = ncols
    else:
        raise ValueError("empty RREF input needs ncols")
    work = copy_matrix(value)
    pivot_row = 0
    pivots: list[int] = []
    for col in range(width):
        found = next((row for row in range(pivot_row, len(work)) if not work[row][col].is_zero()), None)
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        pivot = work[pivot_row][col]
        work[pivot_row] = [item / pivot for item in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            coefficient = work[row][col]
            if coefficient.is_zero():
                continue
            work[row] = [
                work[row][index] - coefficient * work[pivot_row][index]
                for index in range(width)
            ]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == len(work):
            break
    nonzero = [row for row in work if any(not item.is_zero() for item in row)]
    return nonzero, tuple(pivots)


def rank(value: Matrix, *, ncols: int | None = None) -> int:
    return len(rref(value, ncols=ncols)[1])


def kernel(value: Matrix, *, ncols: int | None = None) -> Matrix:
    reduced, pivots = rref(value, ncols=ncols)
    if value:
        width = len(value[0])
    elif ncols is not None:
        width = ncols
    else:
        raise ValueError("empty kernel input needs ncols")
    free = [col for col in range(width) if col not in pivots]
    out = zeros(width, len(free))
    for basis_col, free_col in enumerate(free):
        out[free_col][basis_col] = ONE
        for row, pivot_col in enumerate(pivots):
            out[pivot_col][basis_col] = -reduced[row][free_col]
    return out


def canonical_rowspace(value: Matrix, *, ncols: int) -> Matrix:
    return rref(value, ncols=ncols)[0]


def subspace_equal(left: Matrix, right: Matrix, *, ambient_dim: int) -> bool:
    left_rank = rank(left, ncols=0) if ambient_dim == 0 else rank(left, ncols=len(left[0]) if left else 0)
    right_rank = rank(right, ncols=0) if ambient_dim == 0 else rank(right, ncols=len(right[0]) if right else 0)
    if left_rank != right_rank:
        return False
    if ambient_dim == 0:
        return True
    joined = stack_columns([left, right], ambient_dim)
    return rank(joined, ncols=len(joined[0]) if joined else 0) == left_rank


def constraints_for_subspace(columns: Matrix, *, ambient_dim: int) -> Matrix:
    if len(columns) != ambient_dim:
        raise ValueError("subspace ambient dimension mismatch")
    if not columns or len(columns[0]) == 0:
        return identity(ambient_dim)
    orthogonal_columns = kernel(dagger(columns), ncols=ambient_dim)
    return dagger(orthogonal_columns)


def inverse(value: Matrix) -> Matrix:
    if not value or len(value) != len(value[0]):
        raise ValueError("inverse requires a nonempty square matrix")
    dim = len(value)
    augmented = [value[row][:] + identity(dim)[row] for row in range(dim)]
    reduced, pivots = rref(augmented)
    if tuple(range(dim)) != pivots[:dim]:
        raise ValueError("singular matrix")
    if any(reduced[row][col] != (ONE if row == col else ZERO) for row in range(dim) for col in range(dim)):
        raise ValueError("left block did not reduce to identity")
    return [row[dim:] for row in reduced]


def quotient_complement(constraints: Matrix, *, ambient_dim: int) -> Matrix:
    reduced, pivots = rref(constraints, ncols=ambient_dim)
    if not pivots:
        return zeros(ambient_dim, 0)
    return stack_columns([basis_vector(ambient_dim, pivot) for pivot in pivots], ambient_dim)


@dataclass(frozen=True)
class Continuation:
    name: str
    source: str
    target: str
    operator: Matrix


@dataclass(frozen=True)
class StableNullResult:
    dimensions: Mapping[str, int]
    constraints: Mapping[str, Matrix]
    bases: Mapping[str, Matrix]
    rank_history: tuple[tuple[tuple[str, int], ...], ...]
    strict_rounds: int


def stable_null_family(
    dimensions: Mapping[str, int],
    observations: Mapping[str, Matrix],
    continuations: Sequence[Continuation],
) -> StableNullResult:
    names = tuple(sorted(dimensions))
    if set(observations) != set(names):
        raise ValueError("every boundary needs one immediate observation map")
    current: dict[str, Matrix] = {}
    for name in names:
        dim = dimensions[name]
        observation = observations[name]
        if observation and len(observation[0]) != dim:
            raise ValueError(f"observation shape mismatch at {name}")
        current[name] = canonical_rowspace(observation, ncols=dim)
    outgoing: dict[str, list[Continuation]] = {name: [] for name in names}
    for edge in continuations:
        if edge.source not in dimensions or edge.target not in dimensions:
            raise ValueError(f"unknown boundary on continuation {edge.name}")
        expected = (dimensions[edge.target], dimensions[edge.source])
        actual = shape(edge.operator)
        if actual != expected:
            raise ValueError(f"continuation {edge.name} has shape {actual}, expected {expected}")
        outgoing[edge.source].append(edge)
    history: list[tuple[tuple[str, int], ...]] = [
        tuple((name, len(current[name])) for name in names)
    ]
    strict_rounds = 0
    max_rounds = sum(dimensions.values()) + 1
    for _ in range(max_rounds):
        next_constraints: dict[str, Matrix] = {}
        for name in names:
            pulled = [current[name]]
            for edge in sorted(outgoing[name], key=lambda item: item.name):
                target_constraints = current[edge.target]
                if target_constraints:
                    pulled.append(multiply(target_constraints, edge.operator))
            next_constraints[name] = canonical_rowspace(
                stack_rows(pulled, dimensions[name]),
                ncols=dimensions[name],
            )
        if all(next_constraints[name] == current[name] for name in names):
            break
        strict_rounds += 1
        current = next_constraints
        history.append(tuple((name, len(current[name])) for name in names))
    else:
        raise RuntimeError("stable-null descent exceeded its finite dimension bound")
    bases = {
        name: kernel(current[name], ncols=dimensions[name])
        for name in names
    }
    result = StableNullResult(
        dimensions=dict(dimensions),
        constraints=current,
        bases=bases,
        rank_history=tuple(history),
        strict_rounds=strict_rounds,
    )
    if not continuation_congruence(result, continuations):
        raise AssertionError("computed stable-null family is not a continuation congruence")
    return result


def continuation_congruence(result: StableNullResult, continuations: Sequence[Continuation]) -> bool:
    for edge in continuations:
        source_null = result.bases[edge.source]
        target_constraints = result.constraints[edge.target]
        if source_null and source_null[0] and target_constraints:
            tested = multiply(target_constraints, multiply(edge.operator, source_null))
            if not is_zero_matrix(tested):
                return False
    return True


def descended_quotient_map(
    edge: Continuation,
    result: StableNullResult,
) -> Matrix:
    source_dim = result.dimensions[edge.source]
    target_dim = result.dimensions[edge.target]
    source_complement = quotient_complement(result.constraints[edge.source], ambient_dim=source_dim)
    target_complement = quotient_complement(result.constraints[edge.target], ambient_dim=target_dim)
    source_rank = len(source_complement[0]) if source_complement else 0
    target_rank = len(target_complement[0]) if target_complement else 0
    if source_rank == 0:
        return zeros(target_rank, 0)
    target_constraints = result.constraints[edge.target]
    coordinate_matrix = multiply(target_constraints, target_complement)
    if target_rank == 0:
        tested = multiply(target_constraints, multiply(edge.operator, source_complement))
        if not is_zero_matrix(tested):
            raise ValueError("nonzero quotient image into a zero quotient")
        return zeros(0, source_rank)
    if len(coordinate_matrix) != target_rank:
        coordinate_matrix = canonical_rowspace(target_constraints, ncols=target_dim)
        coordinate_matrix = multiply(coordinate_matrix, target_complement)
    return multiply(
        inverse(coordinate_matrix),
        multiply(target_constraints, multiply(edge.operator, source_complement)),
    )


def pullback(left_continuation: Matrix, right_continuation: Matrix) -> Matrix:
    if len(left_continuation) != len(right_continuation):
        raise ValueError("pullback continuations need a common codomain")
    return multiply(dagger(left_continuation), right_continuation)


def pullback_basis_identity(left_continuation: Matrix, right_continuation: Matrix) -> bool:
    candidate = pullback(left_continuation, right_continuation)
    left_dim = len(left_continuation[0])
    right_dim = len(right_continuation[0])
    for left_index in range(left_dim):
        left_basis = basis_vector(left_dim, left_index)
        for right_index in range(right_dim):
            right_basis = basis_vector(right_dim, right_index)
            direct = multiply(
                dagger(multiply(left_continuation, left_basis)),
                multiply(right_continuation, right_basis),
            )
            through = multiply(dagger(left_basis), multiply(candidate, right_basis))
            if direct != through:
                return False
    return True


def superoperator(kraus: Sequence[Matrix]) -> Matrix:
    if not kraus:
        raise ValueError("a channel needs at least one Kraus operator")
    out_dim = len(kraus[0])
    in_dim = len(kraus[0][0])
    out = zeros(out_dim * out_dim, in_dim * in_dim)
    for operator in kraus:
        if shape(operator) != (out_dim, in_dim):
            raise ValueError("Kraus shape mismatch")
        for row in range(out_dim):
            for col in range(out_dim):
                for left in range(in_dim):
                    for right in range(in_dim):
                        out[row * out_dim + col][left * in_dim + right] = (
                            out[row * out_dim + col][left * in_dim + right]
                            + operator[row][left] * operator[col][right].conjugate()
                        )
    return out


def completeness_operator(kraus: Sequence[Matrix]) -> Matrix:
    if not kraus:
        raise ValueError("completeness needs Kraus operators")
    in_dim = len(kraus[0][0])
    out = zeros(in_dim, in_dim)
    for operator in kraus:
        out = add(out, multiply(dagger(operator), operator))
    return out


def is_complete(kraus: Sequence[Matrix]) -> bool:
    return completeness_operator(kraus) == identity(len(kraus[0][0]))


def instrument_equal(left: Sequence[Sequence[Matrix]], right: Sequence[Sequence[Matrix]]) -> bool:
    if len(left) != len(right):
        return False
    return all(superoperator(left[index]) == superoperator(right[index]) for index in range(len(left)))


def set_partitions(size: int) -> tuple[Partition, ...]:
    if size < 1:
        raise ValueError("partition size must be positive")
    raw: list[list[list[int]]] = []

    def visit(index: int, blocks: list[list[int]]) -> None:
        if index == size:
            raw.append([block[:] for block in blocks])
            return
        for block in blocks:
            block.append(index)
            visit(index + 1, blocks)
            block.pop()
        blocks.append([index])
        visit(index + 1, blocks)
        blocks.pop()

    visit(0, [])
    canonical = {
        tuple(sorted((tuple(sorted(block)) for block in partition), key=lambda block: block[0]))
        for partition in raw
    }
    return tuple(sorted(canonical, key=lambda item: (len(item), item)))


def _block_map(partition: Partition) -> dict[int, int]:
    return {item: block_index for block_index, block in enumerate(partition) for item in block}


def partition_is_stable(
    partition: Partition,
    decoherence: Matrix,
    continuations: Sequence[Matrix],
) -> bool:
    size = sum(len(block) for block in partition)
    if shape(decoherence) != (size, size):
        raise ValueError("decoherence matrix shape mismatch")
    membership = _block_map(partition)
    for left in range(size):
        for right in range(size):
            if membership[left] != membership[right] and not decoherence[left][right].is_zero():
                return False
    for continuation in continuations:
        if shape(continuation) != (size, size):
            raise ValueError("record continuation shape mismatch")
        images: list[int] = []
        for block in partition:
            support = {
                row
                for column in block
                for row in range(size)
                if not continuation[row][column].is_zero()
            }
            if not support:
                return False
            target_blocks = {membership[item] for item in support}
            if len(target_blocks) != 1:
                return False
            images.append(next(iter(target_blocks)))
        if len(set(images)) != len(images):
            return False
    return True


@dataclass(frozen=True)
class PartitionCensus:
    stable: tuple[Partition, ...]
    finest: tuple[Partition, ...]
    all_count: int


def partition_census(
    decoherence: Matrix,
    continuations: Sequence[Matrix],
) -> PartitionCensus:
    size = len(decoherence)
    candidates = set_partitions(size)
    stable = tuple(
        partition
        for partition in candidates
        if partition_is_stable(partition, decoherence, continuations)
    )
    maximum = max(len(partition) for partition in stable)
    finest = tuple(partition for partition in stable if len(partition) == maximum)
    return PartitionCensus(stable=stable, finest=finest, all_count=len(candidates))


def class_operator(terms: Sequence[tuple[object, Matrix]]) -> Matrix:
    if not terms:
        raise ValueError("class operator needs terms")
    out = zeros(len(terms[0][1]), len(terms[0][1][0]))
    for coefficient, operator in terms:
        out = add(out, scale(coefficient, operator))
    return out


def canonical_edges(edges: Iterable[tuple[str, str]]) -> tuple[tuple[str, str], ...]:
    return tuple(sorted(tuple(sorted(edge)) for edge in edges))


def rename_edges(
    edges: Iterable[tuple[str, str]],
    rename: Mapping[str, str],
) -> tuple[tuple[str, str], ...]:
    return canonical_edges((rename[left], rename[right]) for left, right in edges)


def path_transport(
    path: Sequence[str],
    edge_operators: Mapping[tuple[str, str], Matrix],
) -> Matrix:
    if len(path) < 2:
        raise ValueError("a path needs at least one edge")
    first = edge_operators[(path[0], path[1])]
    dim = len(first)
    if shape(first) != (dim, dim):
        raise ValueError("path edge operators must be square")
    out = identity(dim)
    for source, target in zip(path, path[1:]):
        operator = edge_operators[(source, target)]
        if shape(operator) != (dim, dim):
            raise ValueError("path edge dimension mismatch")
        out = multiply(operator, out)
    return out


def vector_probability(vector: Matrix) -> Fraction:
    if not vector or len(vector[0]) != 1:
        raise ValueError("probability requires a column vector")
    return sum((item[0].abs2() for item in vector), Fraction(0))


class GateFailure(RuntimeError):
    pass


class GateBook:
    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []

    def check(self, name: str, condition: bool, detail: object, falsifier: str) -> None:
        row = {
            "name": name,
            "pass": bool(condition),
            "detail": detail,
            "falsifier": falsifier,
        }
        self.rows.append(row)
        if not condition:
            raise GateFailure(name)


PUBLIC_ANCHOR = b"PPR-PUBLIC-CALIBRATION-v1"
PUBLIC_ANCHOR_SHA256 = "805d7ba388a154f591a1cfc51968ddd8133bda2f4219649a7c3fb9963fd9df03"
PUBLIC_MUTANTS = (
    "anchor-corrupt",
    "stable-drop-edge",
    "pullback-transpose",
    "partition-preplant",
    "channel-shadow",
    "split-weight",
)


def public_calibrations(mutant: str | None = None) -> tuple[dict[str, object], GateBook]:
    gates = GateBook()
    anchor = PUBLIC_ANCHOR + (b"!" if mutant == "anchor-corrupt" else b"")
    gates.check(
        "PUB-ANCHOR",
        hashlib.sha256(anchor).hexdigest() == PUBLIC_ANCHOR_SHA256,
        {"expected": PUBLIC_ANCHOR_SHA256, "observed": hashlib.sha256(anchor).hexdigest()},
        "anchor-corrupt",
    )

    dimensions = {"cut": 3, "future": 2}
    observations = {
        "cut": matrix([[1, 0, 0]]),
        "future": matrix([[1, 0]]),
    }
    activation = matrix([[0, 1, 0], [0, 0, 0]])
    continuations = [] if mutant == "stable-drop-edge" else [
        Continuation("activate-second", "cut", "future", activation)
    ]
    stable = stable_null_family(dimensions, observations, continuations)
    cut_null = stable.bases["cut"]
    gates.check(
        "PUB-STABLE-NULL",
        stable.strict_rounds == 1
        and shape(cut_null) == (3, 1)
        and cut_null == matrix([[0], [0], [1]]),
        {
            "rank_history": [dict(row) for row in stable.rank_history],
            "cut_basis": matrix_text(cut_null),
            "strict_rounds": stable.strict_rounds,
        },
        "stable-drop-edge",
    )
    gates.check(
        "PUB-CONGRUENCE",
        continuation_congruence(stable, continuations),
        {"continuations": len(continuations)},
        "stable-drop-edge",
    )
    quotient_map = descended_quotient_map(continuations[0], stable) if continuations else []
    gates.check(
        "PUB-QUOTIENT-DESCENT",
        quotient_map == matrix([[0, 1]]),
        {"descended_map": matrix_text(quotient_map) if quotient_map else []},
        "stable-drop-edge",
    )

    left = matrix([[1, 0], [0, 1], [0, 0]])
    right = matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
    candidate = transpose(pullback(left, right)) if mutant == "pullback-transpose" else pullback(left, right)
    expected_pullback = matrix([[0, 1, 0], [-1, 0, 0]])
    gates.check(
        "PUB-PULLBACK",
        candidate == expected_pullback and pullback_basis_identity(left, right),
        {"pullback": matrix_text(candidate)},
        "pullback-transpose",
    )

    diagonal = identity(2)
    eraser = matrix([[Fraction(3, 5), Fraction(4, 5)], [Fraction(-4, 5), Fraction(3, 5)]])
    durable = partition_census(diagonal, [identity(2)])
    erasable = partition_census(diagonal, [eraser])
    coherent = partition_census(matrix([[1, 1], [1, 1]]), [identity(2)])
    if mutant == "partition-preplant":
        erasable = PartitionCensus(
            stable=erasable.stable + (((0,), (1,)),),
            finest=(((0,), (1,)),),
            all_count=erasable.all_count,
        )
    gates.check(
        "PUB-PARTITIONS",
        durable.all_count == 2
        and durable.finest == (((0,), (1,)),)
        and erasable.finest == (((0, 1),),)
        and coherent.finest == (((0, 1),),),
        {
            "all": durable.all_count,
            "durable_finest": durable.finest,
            "erasable_finest": erasable.finest,
            "coherent_finest": coherent.finest,
        },
        "partition-preplant",
    )

    ident = identity(2)
    zed = matrix([[1, 0], [0, -1]])
    first = [scale(Fraction(3, 5), ident), scale(Fraction(4, 5), zed)]
    second = [
        add(scale(Fraction(3, 5), first[0]), scale(Fraction(4, 5), first[1])),
        add(scale(Fraction(-4, 5), first[0]), scale(Fraction(3, 5), first[1])),
    ]
    same_channel = superoperator(first) == superoperator(second)
    different_instrument = not instrument_equal([[first[0]], [first[1]]], [[second[0]], [second[1]]])
    if mutant == "channel-shadow":
        different_instrument = not same_channel
    gates.check(
        "PUB-CHANNEL-INSTRUMENT-SPLIT",
        is_complete(first) and is_complete(second) and same_channel and different_instrument,
        {
            "same_unconditioned_channel": same_channel,
            "different_record_instrument": different_instrument,
        },
        "channel-shadow",
    )

    rotation = matrix([[Fraction(3, 5), Fraction(4, 5)], [Fraction(-4, 5), Fraction(3, 5)]])
    unsplit = class_operator([(Fraction(3, 5), ident), (Fraction(4, 5), rotation)])
    split_second_weight = Fraction(1, 5) if mutant == "split-weight" else Fraction(2, 5)
    split = class_operator(
        [
            (Fraction(1, 5), ident),
            (split_second_weight, ident),
            (Fraction(4, 5), rotation),
        ]
    )
    gates.check(
        "PUB-HISTORY-SPLIT-MERGE",
        unsplit == split,
        {"class_operator": matrix_text(split)},
        "split-weight",
    )

    graph = canonical_edges((("a", "b"), ("b", "p")))
    renamed = rename_edges(graph, {"a": "x", "b": "y", "p": "z"})
    gates.check(
        "PUB-GRAPH-RELABEL",
        graph == (("a", "b"), ("b", "p"))
        and renamed == (("x", "y"), ("y", "z")),
        {"graph": graph, "renamed": renamed},
        "machine-forced",
    )

    values: dict[str, object] = {
        "stable_null": {
            "rank_history": [dict(row) for row in stable.rank_history],
            "strict_rounds": stable.strict_rounds,
            "cut_basis": matrix_text(cut_null),
            "descended_map": matrix_text(quotient_map),
        },
        "pullback": matrix_text(candidate),
        "partitions": {
            "bell_number_2": durable.all_count,
            "durable_finest": durable.finest,
            "erasable_finest": erasable.finest,
            "coherent_finest": coherent.finest,
        },
        "representations": {
            "same_unconditioned_channel": same_channel,
            "different_record_instrument": different_instrument,
        },
        "graph": {"original": graph, "renamed": renamed},
    }
    return values, gates


def _canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def _seal_payload(payload: Mapping[str, object]) -> dict[str, str]:
    return {
        key: hashlib.sha256(_canonical_json(payload[key]).encode("utf-8")).hexdigest()
        for key in sorted(payload)
    }


def render_public(values: Mapping[str, object], gates: GateBook, source_hash: str) -> tuple[str, dict[str, object]]:
    lines = [
        "PPR GENERIC CORE — PUBLIC CALIBRATIONS",
        f"SOURCE_SHA256 {source_hash}",
        f"GATES {len(gates.rows)}/{len(gates.rows)}",
        f"STABLE_NULL {values['stable_null']}",
        f"PULLBACK {values['pullback']}",
        f"PARTITIONS {values['partitions']}",
        f"REPRESENTATIONS {values['representations']}",
        f"GRAPH {values['graph']}",
        "PUBLIC-CALIBRATIONS-ONLY — NO PPR PHYSICAL FIXTURE OR VERDICT",
    ]
    transcript = "\n".join(lines) + "\n"
    payload: dict[str, object] = {
        "schema": "ppr-public-v1",
        "scope": "PUBLIC-CALIBRATIONS-ONLY",
        "source_sha256": source_hash,
        "values": values,
        "gates": gates.rows,
        "gate_count": len(gates.rows),
        "machine_outcome": "PUBLIC-CALIBRATIONS-ONLY",
        "transcript_sha256": hashlib.sha256(transcript.encode("utf-8")).hexdigest(),
    }
    payload["seals"] = _seal_payload(payload)
    payload["seal_manifest_total"] = sorted(payload["seals"]) == sorted(
        key for key in payload if key != "seals"
    )
    if not payload["seal_manifest_total"]:
        raise GateFailure("PUB-SEAL-MANIFEST")
    return transcript, payload


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PPR generic exact public calibrations")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--mutant", choices=PUBLIC_MUTANTS)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.selftest:
        try:
            public_calibrations("anchor-corrupt")
        except GateFailure as exc:
            if str(exc) != "PUB-ANCHOR":
                print(f"SELFTEST-FAIL unexpected gate {exc}", file=sys.stderr)
                return 1
            print("SELFTEST-PASS anchor corruption exited before artifact construction")
            return 0
        print("SELFTEST-FAIL anchor corruption survived", file=sys.stderr)
        return 1
    try:
        values, gates = public_calibrations(args.mutant)
        source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        transcript, receipt = render_public(values, gates, source_hash)
    except (GateFailure, AssertionError, ValueError, ZeroDivisionError) as exc:
        print(f"PPR-PUBLIC-REFUSED {exc}", file=sys.stderr)
        return 1
    if args.mutant is not None:
        print(f"PPR-PUBLIC-MUTANT-SURVIVED {args.mutant}", file=sys.stderr)
        return 1
    if (args.output is None) != (args.receipt is None):
        print("PPR-PUBLIC-REFUSED output and receipt must be supplied together", file=sys.stderr)
        return 2
    if args.output is not None and args.receipt is not None:
        if args.output.exists() or args.receipt.exists():
            print("PPR-PUBLIC-REFUSED output paths already exist", file=sys.stderr)
            return 2
        args.output.write_text(transcript, encoding="utf-8")
        args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        sys.stdout.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
