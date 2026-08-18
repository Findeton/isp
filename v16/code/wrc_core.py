#!/usr/bin/env python3
"""Generic exact machinery for WRC Paper 8.

This module contains no WRC arena, 27-cell catalogue, Grover coin, committed
walk observable, outcome word, or Paper 8 prose.  It supplies exact
``Q(omega)`` arithmetic, finite matrix/instrument operations, affine-map
diagnostics, covariance helpers, canonical artifacts, and public calibration
fixtures only.
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
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


Q = Fraction


class GateFail(RuntimeError):
    """A measured gate failed."""


@dataclass(frozen=True, order=True)
class EW:
    """Exact ``a + b*omega`` with ``omega**2 + omega + 1 = 0``."""

    a: Q = Q(0)
    b: Q = Q(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", Q(self.a))
        object.__setattr__(self, "b", Q(self.b))

    @staticmethod
    def coerce(value: Any) -> "EW":
        if isinstance(value, EW):
            return value
        if isinstance(value, (int, Fraction, str)):
            return EW(Q(value), Q(0))
        raise TypeError(f"cannot coerce {type(value)!r} to EW")

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
        denominator = self.norm2()
        if denominator == 0:
            raise ZeroDivisionError("zero Eisenstein rational")
        return EW(self.a - self.b, -self.b) / denominator

    def __truediv__(self, other: Any) -> "EW":
        if isinstance(other, (int, Fraction, str)):
            denominator = Q(other)
            if denominator == 0:
                raise ZeroDivisionError("zero rational divisor")
            return EW(self.a / denominator, self.b / denominator)
        return self * EW.coerce(other).inverse()


ZERO = EW(0)
ONE = EW(1)
OMEGA = EW(0, 1)
Matrix = tuple[tuple[EW, ...], ...]
Vector = tuple[EW, ...]


def qtext(value: Q) -> str:
    item = Q(value)
    if item.denominator == 1:
        return str(item.numerator)
    return f"{item.numerator}/{item.denominator}"


def etext(value: EW) -> str:
    if value.b == 0:
        return qtext(value.a)
    if value.a == 0:
        if value.b == 1:
            return "w"
        if value.b == -1:
            return "-w"
        return f"{qtext(value.b)}w"
    sign = "+" if value.b > 0 else "-"
    magnitude = abs(value.b)
    tail = "w" if magnitude == 1 else f"{qtext(magnitude)}w"
    return f"{qtext(value.a)}{sign}{tail}"


def scalar(value: Any) -> EW:
    return EW.coerce(value)


def vector(values: Iterable[Any]) -> Vector:
    result = tuple(scalar(value) for value in values)
    if not result:
        raise ValueError("vector must be nonempty")
    return result


def matrix(rows: Iterable[Iterable[Any]]) -> Matrix:
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
    if rows <= 0 or columns <= 0:
        raise ValueError("positive matrix dimensions required")
    return tuple(tuple(ZERO for _ in range(columns)) for _ in range(rows))


def identity(size: int) -> Matrix:
    if size <= 0:
        raise ValueError("positive identity dimension required")
    return tuple(
        tuple(ONE if row == column else ZERO for column in range(size))
        for row in range(size)
    )


def matrix_unit(size: int, row: int, column: int) -> Matrix:
    if not 0 <= row < size or not 0 <= column < size:
        raise ValueError("matrix-unit index out of range")
    return tuple(
        tuple(ONE if (left, right) == (row, column) else ZERO for right in range(size))
        for left in range(size)
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


def matvec(value: Matrix, state: Vector) -> Vector:
    rows, columns = shape(value)
    if len(state) != columns:
        raise ValueError("matrix-vector shape mismatch")
    return tuple(
        sum((value[row][column] * state[column] for column in range(columns)), ZERO)
        for row in range(rows)
    )


def trace(value: Matrix) -> EW:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("trace requires square matrix")
    return sum((value[index][index] for index in range(rows)), ZERO)


def outer(left: Vector, right: Vector | None = None) -> Matrix:
    rhs = left if right is None else right
    return tuple(
        tuple(left[row] * rhs[column].conjugate() for column in range(len(rhs)))
        for row in range(len(left))
    )


def norm2(state: Vector) -> Q:
    result = sum((entry.norm2() for entry in state), Q(0))
    return result


def density(state: Vector) -> Matrix:
    if norm2(state) != 1:
        raise ValueError("density vector must be exactly normalized")
    return outer(state)


def is_hermitian(value: Matrix) -> bool:
    return value == adjoint(value)


def is_unitary(value: Matrix) -> bool:
    rows, columns = shape(value)
    return rows == columns and matmul(adjoint(value), value) == identity(columns)


def conjugate_by(unitary: Matrix, value: Matrix) -> Matrix:
    return matmul(matmul(unitary, value), adjoint(unitary))


def probability(effect: Matrix, state: Matrix) -> Q:
    item = trace(matmul(effect, state))
    if item.b != 0:
        raise ArithmeticError("probability is not real")
    return item.a


def kraus_operation(kraus: Matrix, state: Matrix) -> Matrix:
    return matmul(matmul(kraus, state), adjoint(kraus))


def instrument_total(kraus: Sequence[Matrix]) -> Matrix:
    if not kraus:
        raise ValueError("empty instrument")
    dimension = shape(kraus[0])[1]
    result = zero(dimension, dimension)
    for operator in kraus:
        result = matadd(result, matmul(adjoint(operator), operator))
    return result


def instrument_complete(kraus: Sequence[Matrix]) -> bool:
    if not kraus:
        return False
    dimension = shape(kraus[0])[1]
    return instrument_total(kraus) == identity(dimension)


def nonlinear_nondemolition_outcome(effect: Matrix, unitary: Matrix, state: Matrix) -> Matrix:
    """The literal ``Tr(E rho) U rho U*`` outcome rule."""
    return matscale(probability(effect, state), conjugate_by(unitary, state))


def affine_combination(weight: Q, left: Matrix, right: Matrix) -> Matrix:
    coefficient = Q(weight)
    if coefficient < 0 or coefficient > 1:
        raise ValueError("affine weight outside [0,1]")
    return matadd(matscale(coefficient, left), matscale(1 - coefficient, right))


def permutation(images: Sequence[int]) -> Matrix:
    size = len(images)
    if sorted(images) != list(range(size)):
        raise ValueError("invalid permutation")
    return tuple(
        tuple(ONE if row == images[column] else ZERO for column in range(size))
        for row in range(size)
    )


def histogram(labels: Sequence[int], size: int) -> tuple[int, ...]:
    if size <= 0:
        raise ValueError("positive histogram size required")
    counts = [0 for _ in range(size)]
    for label in labels:
        if not 0 <= label < size:
            raise ValueError("histogram label out of range")
        counts[label] += 1
    return tuple(counts)


def matrix_text(value: Matrix) -> list[list[str]]:
    return [[etext(entry) for entry in row] for row in value]


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


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


def require(gates: list[dict[str, Any]], name: str, ok: bool, evidence: Mapping[str, Any]) -> None:
    row = {"gate": name, "ok": bool(ok), "evidence": dict(evidence)}
    gates.append(row)
    if not ok:
        raise GateFail(f"{name}: {json.dumps(dict(evidence), sort_keys=True)}")


PUBLIC_MUTANTS = (
    "field-relation",
    "instrument-drop",
    "affinity-effect",
    "covariance-action",
    "histogram-label",
    "payload-seal",
)


def public_calibration(mutant: str | None = None) -> tuple[str, dict[str, Any]]:
    if mutant is not None and mutant not in PUBLIC_MUTANTS:
        raise ValueError(f"unknown public mutant {mutant!r}")

    gates: list[dict[str, Any]] = []

    relation = OMEGA * OMEGA + OMEGA + (ZERO if mutant == "field-relation" else ONE)
    require(gates, "PUBLIC-FIELD", relation == ZERO, {"relation": etext(relation)})

    x = matrix([[0, 1], [1, 0]])
    phase = matrix([[1, 0], [0, OMEGA]])
    unitary = matmul(x, phase)
    require(
        gates,
        "PUBLIC-UNITARY",
        is_unitary(x) and is_unitary(phase) and is_unitary(unitary),
        {"x": is_unitary(x), "phase": is_unitary(phase), "product": is_unitary(unitary)},
    )

    p0 = matrix_unit(2, 0, 0)
    p1 = matrix_unit(2, 1, 1)
    kraus = [p0] if mutant == "instrument-drop" else [p0, p1]
    require(
        gates,
        "PUBLIC-INSTRUMENT",
        instrument_complete(kraus),
        {"total": matrix_text(instrument_total(kraus))},
    )

    psi = vector([Q(3, 5), Q(4, 5)])
    rho = density(psi)
    probabilities = [probability(p0, rho), probability(p1, rho)]
    require(
        gates,
        "PUBLIC-BORN",
        probabilities == [Q(9, 25), Q(16, 25)] and sum(probabilities) == 1,
        {"probabilities": [qtext(item) for item in probabilities]},
    )

    rho0 = p0
    rho1 = p1
    mixture = affine_combination(Q(1, 2), rho0, rho1)
    effect = identity(2) if mutant == "affinity-effect" else p0
    direct = nonlinear_nondemolition_outcome(effect, identity(2), mixture)
    affine = affine_combination(
        Q(1, 2),
        nonlinear_nondemolition_outcome(effect, identity(2), rho0),
        nonlinear_nondemolition_outcome(effect, identity(2), rho1),
    )
    delta = matsub(direct, affine)
    require(
        gates,
        "PUBLIC-NONAFFINITY",
        delta != zero(2, 2),
        {"direct": matrix_text(direct), "affine": matrix_text(affine), "delta": matrix_text(delta)},
    )

    repair = kraus_operation(p0, mixture)
    require(
        gates,
        "PUBLIC-CP-COMPARISON",
        repair != direct and trace(repair) == trace(direct),
        {"repair": matrix_text(repair), "literal": matrix_text(direct), "trace": etext(trace(repair))},
    )

    swap = identity(2) if mutant == "covariance-action" else x
    transformed_effect = conjugate_by(swap, p0)
    transformed_state = conjugate_by(swap, rho0)
    require(
        gates,
        "PUBLIC-COVARIANCE",
        transformed_effect == p1 and transformed_state == rho1,
        {"effect": matrix_text(transformed_effect), "state": matrix_text(transformed_state)},
    )

    labels = [2, 0, 2, 3 if mutant == "histogram-label" else 1]
    try:
        counts = histogram(labels, 3)
        histogram_ok = counts == (1, 1, 2)
        histogram_evidence: Mapping[str, Any] = {"counts": list(counts)}
    except ValueError as error:
        histogram_ok = False
        histogram_evidence = {"error": str(error)}
    require(gates, "PUBLIC-HISTOGRAM", histogram_ok, histogram_evidence)

    results = {
        "field_relation": etext(relation),
        "unitary_product": matrix_text(unitary),
        "born_probabilities": [qtext(item) for item in probabilities],
        "nonaffinity_delta": matrix_text(delta),
        "cp_comparison": {"literal": matrix_text(direct), "repair": matrix_text(repair)},
        "histogram": list(counts),
    }
    claims = [
        "Exact Q(w) matrix and instrument operations are available.",
        "A non-scalar Born effect with outcome-independent state retention is non-affine on the public mixture.",
        "A projective CP operation can preserve the outcome probability while changing the conditioned state.",
        "Covariance transforms effects and preparations together.",
    ]
    transcript_lines = [
        "WRC GENERIC CORE — PUBLIC CALIBRATION",
        f"gates={len(gates)} passed={sum(1 for row in gates if row['ok'])}",
        f"born={','.join(qtext(item) for item in probabilities)}",
        f"nonaffinity_delta={json.dumps(matrix_text(delta), separators=(',', ':'))}",
        f"histogram={','.join(str(item) for item in counts)}",
        "scope=generic exact machinery; no WRC physical fixture or verdict",
    ]
    transcript = "\n".join(transcript_lines) + "\n"

    sealed = {
        "gates": sha256_bytes(canonical_json(gates)),
        "results": sha256_bytes(canonical_json(results)),
        "claims": sha256_bytes(canonical_json(claims)),
        "transcript": sha256_bytes(transcript.encode("utf-8")),
    }
    receipt_base = {
        "schema": "wrc-public-v1",
        "arithmetic": "Q(w), w^2+w+1=0; Fraction only",
        "gates": gates,
        "results": results,
        "claims": claims,
        "seal_manifest": sealed,
        "mutants": list(PUBLIC_MUTANTS),
        "scope": "public generic calibration only",
    }
    receipt_base["payload_sha256"] = sha256_bytes(canonical_json(receipt_base))

    if mutant == "payload-seal":
        receipt_base["results"]["histogram"] = [9]

    seal_ok = (
        sha256_bytes(canonical_json(receipt_base["gates"])) == sealed["gates"]
        and sha256_bytes(canonical_json(receipt_base["results"])) == sealed["results"]
        and sha256_bytes(canonical_json(receipt_base["claims"])) == sealed["claims"]
        and sha256_bytes(transcript.encode("utf-8")) == sealed["transcript"]
    )
    if not seal_ok:
        raise GateFail("PUBLIC-PAYLOAD-SEAL")
    return transcript, receipt_base


def default_paths() -> tuple[Path, Path]:
    here = Path(__file__).resolve().parent
    return here / "wrc_public_output.txt", here / "wrc_public_receipt.json"


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--mutant", choices=PUBLIC_MUTANTS)
    parser.add_argument("--selftest", action="store_true")
    return parser.parse_args(list(argv))


def run_selftest() -> int:
    try:
        public_calibration("field-relation")
    except GateFail:
        return 0
    return 1


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_args(sys.argv[1:] if argv is None else argv)
    if arguments.selftest:
        if arguments.output is not None or arguments.receipt is not None or arguments.mutant is not None:
            raise SystemExit("--selftest cannot be combined with output options or mutants")
        return run_selftest()

    default_output, default_receipt = default_paths()
    output = arguments.output or default_output
    receipt = arguments.receipt or default_receipt
    if output.resolve() == receipt.resolve():
        raise SystemExit("output and receipt targets must differ")
    if output.exists() or receipt.exists():
        raise SystemExit("refusing to overwrite an existing target")

    try:
        transcript, payload = public_calibration(arguments.mutant)
    except (GateFail, ValueError, ArithmeticError) as error:
        print(f"WRC PUBLIC REFUSAL: {error}", file=sys.stderr)
        return 1

    output_bytes = transcript.encode("utf-8")
    receipt_bytes = canonical_json(payload)
    atomic_write(output, output_bytes)
    atomic_write(receipt, receipt_bytes)
    if output.read_bytes() != output_bytes or receipt.read_bytes() != receipt_bytes:
        raise GateFail("PUBLIC-DISK-INTEGRITY")
    sys.stdout.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
