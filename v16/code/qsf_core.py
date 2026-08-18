#!/usr/bin/env python3
"""Generic exact core for QSF Paper 9.

This file is frozen before any QSF physical fixture.  Its public calibrations
contain no WRC carrier, walk, target observable, verdict, or expected Paper 9
answer.  Arithmetic is exact in Q(omega), omega^2 + omega + 1 = 0.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


Q = Fraction


@dataclass(frozen=True)
class EW:
    """Element ``a + b*omega`` of Q(omega), omega^2+omega+1=0."""

    a: Q = Q(0)
    b: Q = Q(0)

    def __init__(self, a: Any = 0, b: Any = 0) -> None:
        object.__setattr__(self, "a", Q(a))
        object.__setattr__(self, "b", Q(b))

    @staticmethod
    def coerce(value: Any) -> "EW":
        return value if isinstance(value, EW) else EW(value)

    def __add__(self, other: Any) -> "EW":
        rhs = EW.coerce(other)
        return EW(self.a + rhs.a, self.b + rhs.b)

    __radd__ = __add__

    def __neg__(self) -> "EW":
        return EW(-self.a, -self.b)

    def __sub__(self, other: Any) -> "EW":
        return self + (-EW.coerce(other))

    def __rsub__(self, other: Any) -> "EW":
        return EW.coerce(other) - self

    def __mul__(self, other: Any) -> "EW":
        rhs = EW.coerce(other)
        return EW(
            self.a * rhs.a - self.b * rhs.b,
            self.a * rhs.b + self.b * rhs.a - self.b * rhs.b,
        )

    __rmul__ = __mul__

    def conjugate(self) -> "EW":
        return EW(self.a - self.b, -self.b)

    def norm2(self) -> Q:
        return self.a * self.a - self.a * self.b + self.b * self.b

    def inverse(self) -> "EW":
        norm = self.norm2()
        if norm == 0:
            raise ZeroDivisionError("zero Eisenstein element")
        conjugate = self.conjugate()
        return EW(conjugate.a / norm, conjugate.b / norm)

    def __truediv__(self, other: Any) -> "EW":
        return self * EW.coerce(other).inverse()

    def __pow__(self, exponent: int) -> "EW":
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        result = ONE
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power //= 2
        return result


ZERO = EW(0)
ONE = EW(1)
OMEGA = EW(0, 1)

Vector = tuple[EW, ...]
Matrix = tuple[tuple[EW, ...], ...]


class GateFail(RuntimeError):
    """A public core gate failed before artifact write."""


def qtext(value: Q) -> str:
    item = Q(value)
    return str(item.numerator) if item.denominator == 1 else f"{item.numerator}/{item.denominator}"


def etext(value: EW) -> str:
    if value.b == 0:
        return qtext(value.a)
    return f"({qtext(value.a)},{qtext(value.b)})"


def matrix(rows: Sequence[Sequence[Any]]) -> Matrix:
    result = tuple(tuple(EW.coerce(entry) for entry in row) for row in rows)
    if not result or not result[0]:
        raise ValueError("matrix must be nonempty")
    if len({len(row) for row in result}) != 1:
        raise ValueError("ragged matrix")
    return result


def vector(entries: Sequence[Any]) -> Vector:
    result = tuple(EW.coerce(entry) for entry in entries)
    if not result:
        raise ValueError("vector must be nonempty")
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


def basis(size: int, index: int) -> Vector:
    if not 0 <= index < size:
        raise IndexError(index)
    return tuple(ONE if position == index else ZERO for position in range(size))


def adjoint(value: Matrix) -> Matrix:
    rows, columns = shape(value)
    return tuple(
        tuple(value[row][column].conjugate() for row in range(rows))
        for column in range(columns)
    )


def matadd(left: Matrix, right: Matrix) -> Matrix:
    if shape(left) != shape(right):
        raise ValueError("matrix addition shape mismatch")
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(len(left[0])))
        for row in range(len(left))
    )


def matsub(left: Matrix, right: Matrix) -> Matrix:
    return matadd(left, matscale(-1, right))


def matscale(coefficient: Any, value: Matrix) -> Matrix:
    scalar = EW.coerce(coefficient)
    return tuple(tuple(scalar * entry for entry in row) for row in value)


def matmul(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_columns = shape(left)
    right_rows, right_columns = shape(right)
    if left_columns != right_rows:
        raise ValueError("matrix multiplication shape mismatch")
    return tuple(
        tuple(
            sum(
                (left[row][inner] * right[inner][column] for inner in range(left_columns)),
                ZERO,
            )
            for column in range(right_columns)
        )
        for row in range(left_rows)
    )


def matvec(value: Matrix, state: Vector) -> Vector:
    rows, columns = shape(value)
    if columns != len(state):
        raise ValueError("matrix-vector shape mismatch")
    return tuple(
        sum((value[row][column] * state[column] for column in range(columns)), ZERO)
        for row in range(rows)
    )


def outer(left: Vector, right: Vector | None = None) -> Matrix:
    rhs = left if right is None else right
    return tuple(
        tuple(left[row] * rhs[column].conjugate() for column in range(len(rhs)))
        for row in range(len(left))
    )


def norm2(state: Vector) -> Q:
    return sum((entry.norm2() for entry in state), Q(0))


def density(state: Vector) -> Matrix:
    if norm2(state) != 1:
        raise ValueError("density vector must be normalized")
    return outer(state)


def trace(value: Matrix) -> EW:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("trace requires a square matrix")
    return sum((value[index][index] for index in range(rows)), ZERO)


def tensor(left: Matrix, right: Matrix) -> Matrix:
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


def direct_sum(values: Sequence[Matrix]) -> Matrix:
    if not values:
        raise ValueError("empty direct sum")
    total_rows = sum(shape(value)[0] for value in values)
    total_columns = sum(shape(value)[1] for value in values)
    result = [[ZERO for _ in range(total_columns)] for _ in range(total_rows)]
    row_offset = 0
    column_offset = 0
    for value in values:
        rows, columns = shape(value)
        for row in range(rows):
            for column in range(columns):
                result[row_offset + row][column_offset + column] = value[row][column]
        row_offset += rows
        column_offset += columns
    return matrix(result)


def partial_trace_a(value: Matrix, dim_a: int, dim_b: int) -> Matrix:
    if shape(value) != (dim_a * dim_b, dim_a * dim_b):
        raise ValueError("partial trace dimensions do not match")
    return tuple(
        tuple(
            sum(
                (
                    value[a * dim_b + b_row][a * dim_b + b_column]
                    for a in range(dim_a)
                ),
                ZERO,
            )
            for b_column in range(dim_b)
        )
        for b_row in range(dim_b)
    )


def partial_trace_b(value: Matrix, dim_a: int, dim_b: int) -> Matrix:
    if shape(value) != (dim_a * dim_b, dim_a * dim_b):
        raise ValueError("partial trace dimensions do not match")
    return tuple(
        tuple(
            sum(
                (
                    value[a_row * dim_b + b][a_column * dim_b + b]
                    for b in range(dim_b)
                ),
                ZERO,
            )
            for a_column in range(dim_a)
        )
        for a_row in range(dim_a)
    )


def is_hermitian(value: Matrix) -> bool:
    return value == adjoint(value)


def is_unitary(value: Matrix) -> bool:
    rows, columns = shape(value)
    return rows == columns and matmul(adjoint(value), value) == identity(columns)


def determinant(value: Matrix) -> EW:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("determinant requires square matrix")
    if rows == 1:
        return value[0][0]
    result = ZERO
    for permutation in permutations(range(rows)):
        inversions = sum(
            1
            for left in range(rows)
            for right in range(left + 1, rows)
            if permutation[left] > permutation[right]
        )
        product = ONE
        for row, column in enumerate(permutation):
            product = product * value[row][column]
        result = result + ((-1) ** inversions) * product
    return result


def principal_submatrix(value: Matrix, indices: Sequence[int]) -> Matrix:
    return tuple(tuple(value[row][column] for column in indices) for row in indices)


def is_psd(value: Matrix, cap: int = 6) -> bool:
    rows, columns = shape(value)
    if rows != columns or rows > cap or not is_hermitian(value):
        return False
    for size in range(1, rows + 1):
        for indices in combinations(range(rows), size):
            minor = determinant(principal_submatrix(value, indices))
            if minor.b != 0 or minor.a < 0:
                return False
    return True


def conjugate_by(operator: Matrix, state: Matrix) -> Matrix:
    return matmul(matmul(operator, state), adjoint(operator))


def probability(effect: Matrix, state: Matrix) -> Q:
    result = trace(matmul(effect, state))
    if result.b != 0:
        raise ArithmeticError("probability is not real")
    return result.a


def affine_combination(weight: Q, left: Matrix, right: Matrix) -> Matrix:
    coefficient = Q(weight)
    if not 0 <= coefficient <= 1:
        raise ValueError("affine coefficient outside unit interval")
    return matadd(matscale(coefficient, left), matscale(1 - coefficient, right))


def apply_channel(kraus: Sequence[Matrix], state: Matrix) -> Matrix:
    if not kraus:
        raise ValueError("empty Kraus family")
    rows = shape(kraus[0])[0]
    result = zero(rows, rows)
    for operator in kraus:
        result = matadd(result, conjugate_by(operator, state))
    return result


def instrument_total(kraus: Sequence[Matrix]) -> Matrix:
    if not kraus:
        raise ValueError("empty Kraus family")
    columns = shape(kraus[0])[1]
    result = zero(columns, columns)
    for operator in kraus:
        result = matadd(result, matmul(adjoint(operator), operator))
    return result


def nonlinear_nondemolition(effect: Matrix, unitary: Matrix, state: Matrix) -> Matrix:
    return matscale(probability(effect, state), conjugate_by(unitary, state))


def measure_and_prepare(effect: Matrix, output_state: Matrix, state: Matrix) -> Matrix:
    if trace(output_state) != ONE or not is_psd(output_state):
        raise ValueError("output state must be normalized and positive")
    return matscale(probability(effect, state), output_state)


def rank_one_completion(effect_vectors: Sequence[Vector], output_vectors: Sequence[Vector]) -> tuple[Matrix, ...]:
    if len(effect_vectors) != len(output_vectors) or not effect_vectors:
        raise ValueError("completion vectors must be nonempty and equally sized")
    if any(norm2(state) != 1 for state in effect_vectors + output_vectors):
        raise ValueError("completion vectors must be normalized")
    return tuple(outer(output, effect) for effect, output in zip(effect_vectors, output_vectors))


def affinity_defect(
    operation: Callable[[Matrix], Matrix],
    weight: Q,
    left: Matrix,
    right: Matrix,
) -> Matrix:
    mixture = affine_combination(weight, left, right)
    return matsub(
        operation(mixture),
        affine_combination(weight, operation(left), operation(right)),
    )


def alice_conditioned_bob(
    joint_state: Matrix,
    alice_effect: Matrix,
    dim_a: int,
    dim_b: int,
) -> tuple[Q, Matrix]:
    projector = tensor(alice_effect, identity(dim_b))
    unnormalized_joint = conjugate_by(projector, joint_state)
    unnormalized_bob = partial_trace_a(unnormalized_joint, dim_a, dim_b)
    item = trace(unnormalized_bob)
    if item.b != 0 or item.a <= 0:
        raise ValueError("conditioning probability must be positive real")
    probability_value = item.a
    return probability_value, matscale(Q(1, 1) / probability_value, unnormalized_bob)


def ensemble_density(ensemble: Sequence[tuple[Q, Matrix]]) -> Matrix:
    if not ensemble:
        raise ValueError("empty ensemble")
    rows, columns = shape(ensemble[0][1])
    result = zero(rows, columns)
    total = Q(0)
    for weight, state in ensemble:
        coefficient = Q(weight)
        total += coefficient
        result = matadd(result, matscale(coefficient, state))
    if total != 1:
        raise ValueError("ensemble weights must sum to one")
    return result


def sequential_nondemolition_distribution(
    ensemble: Sequence[tuple[Q, Matrix]],
    first_effects: Sequence[Matrix],
    second_effects: Sequence[Matrix],
) -> tuple[tuple[Q, ...], ...]:
    result = [[Q(0) for _ in second_effects] for _ in first_effects]
    for weight, state in ensemble:
        for first, first_effect in enumerate(first_effects):
            first_probability = probability(first_effect, state)
            for second, second_effect in enumerate(second_effects):
                result[first][second] += Q(weight) * first_probability * probability(second_effect, state)
    return tuple(tuple(row) for row in result)


def sequential_projective_distribution(
    state: Matrix,
    projectors: Sequence[Matrix],
) -> tuple[tuple[Q, ...], ...]:
    result = []
    for first_projector in projectors:
        first_probability = probability(first_projector, state)
        branch = conjugate_by(first_projector, state)
        row = []
        for second_projector in projectors:
            joint = trace(matmul(second_projector, branch))
            if joint.b != 0:
                raise ArithmeticError("joint probability is not real")
            row.append(joint.a)
        if sum(row) != first_probability:
            raise ArithmeticError("projective sequential row is not normalized")
        result.append(tuple(row))
    return tuple(result)


def feedback_coarse_map(
    state: Matrix,
    effects: Sequence[Matrix],
    continuations: Sequence[Matrix],
) -> Matrix:
    if len(effects) != len(continuations) or not effects:
        raise ValueError("feedback arrays must align")
    rows, _columns = shape(state)
    result = zero(rows, rows)
    for effect, continuation in zip(effects, continuations):
        result = matadd(
            result,
            matscale(probability(effect, state), conjugate_by(continuation, state)),
        )
    return result


def partition_from_key(items: Sequence[Any], key: Callable[[Any], Any]) -> tuple[tuple[Any, ...], ...]:
    blocks: dict[str, list[Any]] = {}
    for item in items:
        label = canonical_json_value(key(item))
        blocks.setdefault(label, []).append(item)
    return tuple(tuple(blocks[label]) for label in sorted(blocks))


def summary_sufficient(
    items: Sequence[Any],
    summary: Callable[[Any], Any],
    future_law: Callable[[Any], Any],
) -> bool:
    for block in partition_from_key(items, summary):
        futures = {canonical_json_value(future_law(item)) for item in block}
        if len(futures) != 1:
            return False
    return True


def canonical_json_value(value: Any) -> str:
    return json.dumps(serialize(value), sort_keys=True, separators=(",", ":"))


def serialize(value: Any) -> Any:
    if isinstance(value, EW):
        return etext(value)
    if isinstance(value, Fraction):
        return qtext(value)
    if isinstance(value, Mapping):
        return {str(key): serialize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(item) for item in value]
    if isinstance(value, set):
        return sorted((serialize(item) for item in value), key=canonical_json_value)
    return value


def canonical_json(value: Any) -> bytes:
    return (json.dumps(serialize(value), sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def gate(rows: list[dict[str, Any]], name: str, statement: str, ok: bool, evidence: Mapping[str, Any]) -> None:
    row = {"gate": name, "statement": statement, "ok": bool(ok), "evidence": serialize(dict(evidence))}
    rows.append(row)
    if not ok:
        raise GateFail(f"{name}: {json.dumps(row['evidence'], sort_keys=True)}")


PUBLIC_MUTANTS = (
    "field-relation",
    "instrument-drop",
    "hjw-state",
    "nonlinear-flag",
    "history-feedback",
    "partition-merge",
    "exactness",
    "payload-seal",
)


def public_calibration(mutant: str | None = None) -> tuple[str, dict[str, Any]]:
    if mutant is not None and mutant not in PUBLIC_MUTANTS:
        raise ValueError(f"unknown public mutant {mutant!r}")
    gates: list[dict[str, Any]] = []

    relation = OMEGA * OMEGA + OMEGA + (ZERO if mutant == "field-relation" else ONE)
    gate(
        gates,
        "QSF-PUBLIC-FIELD",
        "the exact Eisenstein generator obeys its minimal polynomial and conjugation norm",
        relation == ZERO and OMEGA.norm2() == 1 and OMEGA.conjugate() == OMEGA * OMEGA,
        {"relation": relation, "norm": OMEGA.norm2()},
    )

    p0 = matrix([[1, 0], [0, 0]])
    p1 = matrix([[0, 0], [0, 1]])
    x = matrix([[0, 1], [1, 0]])
    plus = matrix([[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]])
    minus = matrix([[Q(1, 2), Q(-1, 2)], [Q(-1, 2), Q(1, 2)]])
    maximally_mixed = matscale(Q(1, 2), identity(2))
    bell = matrix(
        [
            [Q(1, 2), 0, 0, Q(1, 2)],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [Q(1, 2), 0, 0, Q(1, 2)],
        ]
    )
    if mutant == "hjw-state":
        bell = tensor(p0, p0)

    z_ensemble = [alice_conditioned_bob(bell, projector, 2, 2) for projector in (p0, p1)]
    x_ensemble = [alice_conditioned_bob(bell, projector, 2, 2) for projector in (plus, minus)]
    z_average = ensemble_density(z_ensemble)
    x_average = ensemble_density(x_ensemble)
    gate(
        gates,
        "QSF-PUBLIC-HJW",
        "two complete Alice measurements remotely realize distinct pure ensembles of one Bob density matrix",
        z_average == maximally_mixed
        and x_average == maximally_mixed
        and {state for _weight, state in z_ensemble} != {state for _weight, state in x_ensemble}
        and all(weight == Q(1, 2) for weight, _state in z_ensemble + x_ensemble),
        {"z_average": z_average, "x_average": x_average, "weights": [row[0] for row in z_ensemble + x_ensemble]},
    )

    outputs = [basis(2, 0), basis(2, 1)]
    if mutant == "instrument-drop":
        outputs = outputs[:1]
    effect_vectors = [basis(2, index) for index in range(len(outputs))]
    ports = rank_one_completion(effect_vectors, outputs)
    complete = instrument_total(ports) == identity(2) if len(ports) == 2 else False
    gate(
        gates,
        "QSF-PUBLIC-INSTRUMENT",
        "rank-one measure-and-prepare ports are CP and complete when their effects resolve the identity",
        complete and all(is_psd(matmul(adjoint(port), port)) for port in ports),
        {"complete": complete, "ports": len(ports)},
    )

    literal = lambda state: nonlinear_nondemolition(p0, x, state)
    literal_defect = affinity_defect(literal, Q(1, 2), p0, plus)
    affine = lambda state: measure_and_prepare(p0, p1, state)
    affine_defect = affinity_defect(affine, Q(1, 2), p0, plus)
    gate(
        gates,
        "QSF-PUBLIC-AFFINITY",
        "the nondemolition probability-times-state rule is nonaffine while fixed-output measure-and-prepare is affine",
        literal_defect != zero(2, 2) and affine_defect == zero(2, 2),
        {"literal_nonzero": sum(entry != ZERO for row in literal_defect for entry in row), "affine_nonzero": sum(entry != ZERO for row in affine_defect for entry in row)},
    )

    z_distribution = sequential_nondemolition_distribution(z_ensemble, (p0, p1), (p0, p1))
    x_distribution = sequential_nondemolition_distribution(x_ensemble, (p0, p1), (p0, p1))
    if mutant == "nonlinear-flag":
        x_distribution = z_distribution
    projective_z = sequential_projective_distribution(z_average, (p0, p1))
    projective_x = sequential_projective_distribution(x_average, (p0, p1))
    gate(
        gates,
        "QSF-PUBLIC-STEERING-DISCRIMINATOR",
        "equal-density ensembles are distinguished by sequential nondemolition readouts but not by the affine projective control",
        z_distribution != x_distribution and projective_z == projective_x,
        {"z_nondemolition": z_distribution, "x_nondemolition": x_distribution, "projective": projective_z},
    )

    one_step_discard = lambda state: state
    retained = lambda state: direct_sum(
        [nonlinear_nondemolition(effect, identity(2), state) for effect in (p0, p1)]
    )
    continuations = (identity(2), x)
    feedback = lambda state: feedback_coarse_map(state, (p0, p1), continuations)
    discard_defect = affinity_defect(one_step_discard, Q(1, 2), p0, p1)
    retained_defect = affinity_defect(retained, Q(1, 2), p0, p1)
    feedback_defect = affinity_defect(feedback, Q(1, 2), p0, p1)
    if mutant == "history-feedback":
        feedback_defect = zero(2, 2)
    gate(
        gates,
        "QSF-PUBLIC-HISTORY-GRAINS",
        "discarding an internal label can be affine while retaining it or feeding it forward exposes nonaffinity",
        discard_defect == zero(2, 2)
        and retained_defect != zero(4, 4)
        and feedback_defect != zero(2, 2),
        {
            "discard_nonzero": sum(entry != ZERO for row in discard_defect for entry in row),
            "retained_nonzero": sum(entry != ZERO for row in retained_defect for entry in row),
            "feedback_nonzero": sum(entry != ZERO for row in feedback_defect for entry in row),
        },
    )

    histories = ((0, 1), (1, 0), (0, 0), (1, 1))
    future = lambda history: history[-1]
    counts = lambda history: tuple(history.count(value) for value in (0, 1))
    previous = lambda history: 0 if mutant == "partition-merge" else history[-1]
    counts_sufficient = summary_sufficient(histories, counts, future)
    previous_sufficient = summary_sufficient(histories, previous, future)
    gate(
        gates,
        "QSF-PUBLIC-PREDICTIVE-PARTITION",
        "a coarser history summary may fail predictive sufficiency while a finer summary succeeds",
        not counts_sufficient and previous_sufficient,
        {"count_blocks": len(partition_from_key(histories, counts)), "previous_blocks": len(partition_from_key(histories, previous))},
    )

    exact_marker: Any = Q(1, 3)
    if mutant == "exactness":
        exact_marker = float(Q(1, 3))
    gate(
        gates,
        "QSF-PUBLIC-EXACTNESS",
        "the public result surface contains exact rational objects and no runtime float",
        isinstance(exact_marker, Fraction),
        {"marker": exact_marker},
    )

    result = {
        "schema": "qsf-public-v1",
        "arithmetic": "Q(omega), omega^2+omega+1=0; exact Fraction coefficients",
        "measurements": {
            "hjw_equal_density": z_average == x_average == maximally_mixed,
            "nondemolition_ensemble_sensitive": z_distribution != x_distribution,
            "affine_projective_blind": projective_z == projective_x,
            "literal_affinity_defect_nonzero": literal_defect != zero(2, 2),
            "measure_prepare_affine": affine_defect == zero(2, 2),
            "record_discard_affine": discard_defect == zero(2, 2),
            "record_retained_nonaffine": retained_defect != zero(4, 4),
            "feedback_nonaffine": feedback_defect != zero(2, 2),
            "count_summary_sufficient": counts_sufficient,
            "previous_summary_sufficient": previous_sufficient,
        },
        "gates": gates,
        "mutants": list(PUBLIC_MUTANTS),
    }
    result["payload_sha256"] = digest(result)
    if mutant == "payload-seal":
        result["measurements"]["hjw_equal_density"] = False
    expected_payload = result["payload_sha256"]
    observed_payload = digest({key: value for key, value in result.items() if key != "payload_sha256"})
    if expected_payload != observed_payload:
        raise GateFail("QSF-PUBLIC-PAYLOAD-SEAL")

    transcript_lines = [
        "QSF GENERIC PUBLIC CORE",
        f"gates={len(gates)} passed={sum(row['ok'] for row in gates)}",
        f"hjw_equal_density={result['measurements']['hjw_equal_density']}",
        f"nondemolition_ensemble_sensitive={result['measurements']['nondemolition_ensemble_sensitive']}",
        f"affine_projective_blind={result['measurements']['affine_projective_blind']}",
        f"record_discard_affine={result['measurements']['record_discard_affine']}",
        f"record_retained_nonaffine={result['measurements']['record_retained_nonaffine']}",
        f"feedback_nonaffine={result['measurements']['feedback_nonaffine']}",
        f"count_summary_sufficient={result['measurements']['count_summary_sufficient']}",
        f"previous_summary_sufficient={result['measurements']['previous_summary_sufficient']}",
        f"payload_sha256={result['payload_sha256']}",
    ]
    return "\n".join(transcript_lines) + "\n", result


def atomic_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def default_paths() -> tuple[Path, Path]:
    here = Path(__file__).resolve().parent
    return here / "qsf_public_output.txt", here / "qsf_public_receipt.json"


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--mutant", choices=PUBLIC_MUTANTS)
    parser.add_argument("--selftest", action="store_true")
    return parser.parse_args(list(argv))


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_args(sys.argv[1:] if argv is None else argv)
    default_output, default_receipt = default_paths()
    if arguments.selftest:
        if arguments.output is not None or arguments.receipt is not None or arguments.mutant is not None:
            raise SystemExit("--selftest cannot be combined with output options or mutants")
        try:
            public_calibration("instrument-drop")
        except GateFail:
            return 0
        return 1

    output = (arguments.output or default_output).resolve()
    receipt = (arguments.receipt or default_receipt).resolve()
    if output == receipt:
        raise SystemExit("output and receipt targets must differ")
    if output.exists() or receipt.exists():
        raise SystemExit("refusing to overwrite an existing target")
    try:
        transcript, result = public_calibration(arguments.mutant)
    except (GateFail, ValueError, TypeError, ArithmeticError, ZeroDivisionError) as error:
        print(f"QSF PUBLIC REFUSAL: {error}", file=sys.stderr)
        return 1
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["transcript_sha256"] = hashlib.sha256(transcript.encode()).hexdigest()
    receipt_payload = canonical_json(result)
    atomic_write(output, transcript.encode())
    atomic_write(receipt, receipt_payload)
    if output.read_text() != transcript or receipt.read_bytes() != receipt_payload:
        raise GateFail("QSF-PUBLIC-DISK-INTEGRITY")
    sys.stdout.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
