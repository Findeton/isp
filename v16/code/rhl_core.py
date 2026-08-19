#!/usr/bin/env python3
"""Result-neutral exact algebra for RHL.

This module knows nothing about the RHL verdict, physical fixture, ontology
outcome, graph size, lattice, or tick.  It supplies exact finite-dimensional
receipts for general algebraic statements that are proved at arbitrary-region
scope in the paper: Gram strong positivity, coarse graining, refinement
pullback, composition, tensor product, interference defects, and all-input
instrument completeness.

Finite matrices here are theorem checks and counterexample generators.  They
are not a proposed microscopic state space.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


Q = Fraction


@dataclass(frozen=True, slots=True)
class QI:
    """A Gaussian rational, stored without floating point."""

    re: Q = Q(0)
    im: Q = Q(0)

    def __add__(self, other: object) -> "QI":
        value = qi(other)
        return QI(self.re + value.re, self.im + value.im)

    def __radd__(self, other: object) -> "QI":
        return self + other

    def __sub__(self, other: object) -> "QI":
        value = qi(other)
        return QI(self.re - value.re, self.im - value.im)

    def __rsub__(self, other: object) -> "QI":
        return qi(other) - self

    def __neg__(self) -> "QI":
        return QI(-self.re, -self.im)

    def __mul__(self, other: object) -> "QI":
        value = qi(other)
        return QI(
            self.re * value.re - self.im * value.im,
            self.re * value.im + self.im * value.re,
        )

    def __rmul__(self, other: object) -> "QI":
        return self * other

    def __truediv__(self, other: object) -> "QI":
        value = qi(other)
        denominator = value.re * value.re + value.im * value.im
        if denominator == 0:
            raise ZeroDivisionError("Gaussian-rational division by zero")
        return QI(
            (self.re * value.re + self.im * value.im) / denominator,
            (self.im * value.re - self.re * value.im) / denominator,
        )

    def conjugate(self) -> "QI":
        return QI(self.re, -self.im)

    def norm2(self) -> Q:
        return self.re * self.re + self.im * self.im


ZERO = QI()
ONE = QI(Q(1))
I = QI(Q(0), Q(1))


def qi(value: object) -> QI:
    if isinstance(value, QI):
        return value
    if isinstance(value, Fraction):
        return QI(value)
    if isinstance(value, int):
        return QI(Q(value))
    raise TypeError(f"cannot coerce {type(value).__name__} to QI")


Vector = tuple[QI, ...]
Matrix = tuple[tuple[QI, ...], ...]


def vector(values: Iterable[object]) -> Vector:
    return tuple(qi(value) for value in values)


def matrix(rows: Iterable[Iterable[object]]) -> Matrix:
    result = tuple(tuple(qi(value) for value in row) for row in rows)
    if not result:
        return tuple()
    width = len(result[0])
    if width == 0 or any(len(row) != width for row in result):
        raise ValueError("matrix must be nonempty and rectangular")
    return result


def shape(value: Matrix) -> tuple[int, int]:
    return (len(value), len(value[0]) if value else 0)


def zeros(rows: int, columns: int) -> Matrix:
    return tuple(tuple(ZERO for _ in range(columns)) for _ in range(rows))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(ONE if row == column else ZERO for column in range(size))
        for row in range(size)
    )


def adjoint(value: Matrix) -> Matrix:
    rows, columns = shape(value)
    return tuple(
        tuple(value[row][column].conjugate() for row in range(rows))
        for column in range(columns)
    )


def madd(left: Matrix, right: Matrix) -> Matrix:
    if shape(left) != shape(right):
        raise ValueError("matrix-add shape mismatch")
    return tuple(
        tuple(a + b for a, b in zip(row_left, row_right, strict=True))
        for row_left, row_right in zip(left, right, strict=True)
    )


def mscale(scalar: object, value: Matrix) -> Matrix:
    factor = qi(scalar)
    return tuple(tuple(factor * entry for entry in row) for row in value)


def mmul(left: Matrix, right: Matrix) -> Matrix:
    rows, inner = shape(left)
    inner_right, columns = shape(right)
    if inner != inner_right:
        raise ValueError("matrix-multiply shape mismatch")
    return tuple(
        tuple(
            sum((left[row][index] * right[index][column] for index in range(inner)), ZERO)
            for column in range(columns)
        )
        for row in range(rows)
    )


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


def mv(value: Matrix, item: Vector) -> Vector:
    rows, columns = shape(value)
    if columns != len(item):
        raise ValueError("matrix-vector shape mismatch")
    return tuple(
        sum((value[row][column] * item[column] for column in range(columns)), ZERO)
        for row in range(rows)
    )


def inner(left: Vector, right: Vector) -> QI:
    if len(left) != len(right):
        raise ValueError("inner-product shape mismatch")
    return sum((a.conjugate() * b for a, b in zip(left, right, strict=True)), ZERO)


def gram(vectors: Sequence[Vector]) -> Matrix:
    return tuple(tuple(inner(left, right) for right in vectors) for left in vectors)


def determinant(value: Matrix) -> QI:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("determinant requires a square matrix")
    if rows == 0:
        return ONE
    work = [list(row) for row in value]
    result = ONE
    for column in range(columns):
        pivot = next((row for row in range(column, rows) if work[row][column] != ZERO), None)
        if pivot is None:
            return ZERO
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result = result * pivot_value
        for row in range(column + 1, rows):
            factor = work[row][column] / pivot_value
            for target in range(column + 1, columns):
                work[row][target] = work[row][target] - factor * work[column][target]
    return result


def principal_submatrix(value: Matrix, indices: Sequence[int]) -> Matrix:
    return tuple(tuple(value[row][column] for column in indices) for row in indices)


def hermitian(value: Matrix) -> bool:
    return value == adjoint(value)


def gram_strong_positivity_certificate(vectors: Sequence[Vector]) -> dict[str, object]:
    """Certify Gram positivity without claiming a complete PSD decision method.

    A Gram matrix is positive by construction at every finite list.  Principal
    determinants are printed as independent exact receipts for the supplied
    public calibration.
    """

    value = gram(vectors)
    minors: list[str] = []
    size = len(vectors)
    for mask in range(1, 1 << size):
        indices = tuple(index for index in range(size) if mask & (1 << index))
        minor = determinant(principal_submatrix(value, indices))
        if minor.im != 0 or minor.re < 0:
            raise AssertionError("Gram principal minor failed exact nonnegativity")
        minors.append(qtext(minor))
    return {"gram": mtext(value), "principal_minors": minors}


def coarse_grain(value: Matrix, blocks: Sequence[Sequence[int]]) -> Matrix:
    """Push a decoherence matrix to a disjoint event partition."""

    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("decoherence matrix must be square")
    flat = tuple(index for block in blocks for index in block)
    if sorted(flat) != list(range(rows)) or len(set(flat)) != rows:
        raise ValueError("blocks must partition every fine alternative exactly once")
    return tuple(
        tuple(
            sum((value[row][column] for row in block_left for column in block_right), ZERO)
            for block_right in blocks
        )
        for block_left in blocks
    )


def refinement_pullback(fine: Matrix, embedding: Matrix) -> Matrix:
    """Pull a fine functional back along a coarse-to-fine linear embedding."""

    fine_rows, fine_columns = shape(fine)
    embed_rows, _ = shape(embedding)
    if fine_rows != fine_columns or fine_rows != embed_rows:
        raise ValueError("refinement pullback shape mismatch")
    return mmul(adjoint(embedding), mmul(fine, embedding))


def interference_defect(value: Matrix, indices: Sequence[int]) -> QI:
    """Return total coarse weight minus the classical diagonal sum."""

    coherent = sum((value[row][column] for row in indices for column in indices), ZERO)
    classical = sum((value[index][index] for index in indices), ZERO)
    return coherent - classical


def class_operator(operators: Sequence[Matrix], weights: Sequence[QI]) -> Matrix:
    if len(operators) != len(weights) or not operators:
        raise ValueError("class-operator data mismatch")
    result = zeros(*shape(operators[0]))
    for operator, weight in zip(operators, weights, strict=True):
        if shape(operator) != shape(result):
            raise ValueError("class-operator shape mismatch")
        result = madd(result, mscale(weight, operator))
    return result


def instrument_effect(operators: Sequence[Matrix]) -> Matrix:
    if not operators:
        raise ValueError("instrument needs at least one outcome operator")
    columns = shape(operators[0])[1]
    result = zeros(columns, columns)
    for operator in operators:
        if shape(operator)[1] != columns:
            raise ValueError("instrument input dimensions differ")
        result = madd(result, mmul(adjoint(operator), operator))
    return result


def instrument_complete(operators: Sequence[Matrix]) -> bool:
    return instrument_effect(operators) == identity(shape(operators[0])[1])


def qtext(value: QI) -> str:
    def fraction_text(item: Q) -> str:
        return str(item.numerator) if item.denominator == 1 else f"{item.numerator}/{item.denominator}"

    if value.im == 0:
        return fraction_text(value.re)
    if value.re == 0:
        if value.im == 1:
            return "i"
        if value.im == -1:
            return "-i"
        return f"{fraction_text(value.im)}i"
    sign = "+" if value.im > 0 else "-"
    magnitude = abs(value.im)
    imaginary = "i" if magnitude == 1 else f"{fraction_text(magnitude)}i"
    return f"{fraction_text(value.re)}{sign}{imaginary}"


def mtext(value: Matrix) -> list[list[str]]:
    return [[qtext(entry) for entry in row] for row in value]


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def public_calibrations() -> tuple[list[dict[str, object]], dict[str, object]]:
    """Run generic public checks with no RHL physical fixture or verdict."""

    gates: list[dict[str, object]] = []

    def gate(name: str, passed: bool, evidence: str) -> None:
        if not passed:
            raise AssertionError(f"{name}: {evidence}")
        gates.append({"gate": name, "passed": True, "evidence": evidence})

    # Gaussian-rational arithmetic.
    gate("CORE-EXACT-FIELD", I * I == -ONE and I.conjugate() == -I, "i^2=-1 and conj(i)=-i")

    # A public Gram family: positivity comes from construction, not a finite
    # numerical claim about nature.
    vectors = (
        vector((Q(1), Q(0))),
        vector((Q(3, 5), Q(4, 5))),
        vector((QI(Q(0), Q(1)), Q(0))),
    )
    positivity = gram_strong_positivity_certificate(vectors)
    gate(
        "CORE-GRAM-STRONG-POSITIVITY",
        hermitian(gram(vectors)),
        f"principal_minors={positivity['principal_minors']}",
    )

    # Refinement pullback on a generic exact isometric embedding.
    embedding = matrix(((Q(3, 5), Q(0)), (Q(4, 5), Q(0)), (Q(0), Q(1))))
    gate(
        "CORE-REFINEMENT-ISOMETRY",
        mmul(adjoint(embedding), embedding) == identity(2),
        f"JdagJ={mtext(mmul(adjoint(embedding), embedding))}",
    )
    fine = identity(3)
    pulled = refinement_pullback(fine, embedding)
    gate("CORE-REFINEMENT-PULLBACK", pulled == identity(2), f"pullback={mtext(pulled)}")

    # Coarse-graining is biadditive and exposes the cross term.
    coherent = matrix(((Q(1, 4), Q(1, 4)), (Q(1, 4), Q(1, 4))))
    coarse = coarse_grain(coherent, ((0, 1),))
    defect = interference_defect(coherent, (0, 1))
    gate("CORE-COARSE-BIADDITIVITY", coarse == matrix(((Q(1),),)), f"coarse={mtext(coarse)}")
    gate("CORE-INTERFERENCE-DEFECT", defect == QI(Q(1, 2)), f"defect={qtext(defect)}")

    # Associativity is the finite receipt for the general categorical axiom.
    rotation = matrix(((Q(3, 5), Q(4, 5)), (-Q(4, 5), Q(3, 5))))
    phase = matrix(((ONE, ZERO), (ZERO, I)))
    left_cut = mmul(phase, mmul(rotation, rotation))
    right_cut = mmul(mmul(phase, rotation), rotation)
    gate("CORE-CUT-ASSOCIATIVITY", left_cut == right_cut, f"composite={mtext(left_cut)}")

    # Disjoint composition is monoidal at the representation level.
    gate(
        "CORE-DISJOINT-MONOIDAL",
        kron(mmul(rotation, rotation), phase) == mmul(kron(rotation, identity(2)), kron(rotation, phase)),
        "(R^2) tensor P = (R tensor I)(R tensor P)",
    )

    # All-input completeness and a state-only normalization countercontrol.
    k0 = matrix(((ONE, ZERO), (ZERO, ZERO)))
    k1 = matrix(((ZERO, ZERO), (ZERO, ONE)))
    gate("CORE-INSTRUMENT-COMPLETE", instrument_complete((k0, k1)), f"effect={mtext(instrument_effect((k0, k1)))}")
    amplifier = matrix(((ONE, ZERO), (ZERO, qi(2))))
    prepared = vector((ONE, ZERO))
    prepared_norm = inner(mv(amplifier, prepared), mv(amplifier, prepared))
    gate(
        "CORE-STATE-NORMALIZATION-NOT-COMPLETE",
        prepared_norm == ONE and not instrument_complete((amplifier,)),
        f"prepared_norm={qtext(prepared_norm)} effect={mtext(instrument_effect((amplifier,)))}",
    )

    measurements = {
        "positivity": positivity,
        "refinement": {"embedding": mtext(embedding), "pullback": mtext(pulled)},
        "interference": {"functional": mtext(coherent), "coarse": mtext(coarse), "defect": qtext(defect)},
        "composition": {"cut_composite": mtext(left_cut)},
        "instrument": {
            "complete_effect": mtext(instrument_effect((k0, k1))),
            "state_only_effect": mtext(instrument_effect((amplifier,))),
        },
    }
    return gates, measurements


def render_transcript(gates: Sequence[dict[str, object]], measurements: dict[str, object]) -> str:
    lines = [
        "RHL GENERIC CORE — RESULT NEUTRAL",
        "scope: exact Q(i) theorem receipts; no points, ticks, graph fixture, or physical verdict",
    ]
    for item in gates:
        lines.append(f"PASS {item['gate']} :: {item['evidence']}")
    lines.append(f"SUMMARY {len(gates)}/{len(gates)} public gates")
    lines.append(f"MEASUREMENTS-SHA256 {digest(measurements)}")
    return "\n".join(lines) + "\n"


def write_new(path: Path, text: str) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path}")
    path.write_text(text, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--selftest", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    gates, measurements = public_calibrations()
    transcript = render_transcript(gates, measurements)
    receipt = {
        "schema": "rhl-generic-core-v1",
        "scope": {
            "arithmetic": "exact Q(i)",
            "role": "generic theorem receipts only; no RHL regulator, physical fixture, or outcome",
            "ontological_disclaimer": "finite matrices authenticate algebra and are not spacetime atoms",
        },
        "gates": gates,
        "measurements": measurements,
        "transcript_sha256": hashlib.sha256(transcript.encode("utf-8")).hexdigest(),
    }
    receipt["seals"] = {
        "scope": digest(receipt["scope"]),
        "gates": digest(receipt["gates"]),
        "measurements": digest(receipt["measurements"]),
    }

    if args.selftest:
        broken = matrix(((Q(1, 4), Q(0)), (Q(0), Q(1, 4))))
        if interference_defect(broken, (0, 1)) == QI(Q(1, 2)):
            raise AssertionError("selftest failed to break interference anchor")
        print("SELFTEST PASS: broken cross term refused the public interference anchor")
        return 0

    write_new(args.output, transcript)
    write_new(args.receipt, canonical_json(receipt) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
