#!/usr/bin/env python3
"""Generic exact machinery for OVG Paper 5.

This module contains no OVG physical fixture, target verdict, or Paper 5
result.  Its command-line entry point runs public calibration examples only.
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
from typing import Any, Iterable, Mapping, Sequence


Q = Fraction


@dataclass(frozen=True, order=True)
class GQ:
    """Gaussian rational ``re + im*i`` with runtime coercion to ``Fraction``."""

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
        n2 = self.norm2()
        if n2 == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        return GQ(self.re / n2, -self.im / n2)

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
    imag = "i" if magnitude == 1 else f"{qtext(magnitude)}i"
    return f"{qtext(value.re)}{sign}{imag}"


def scalar(value: Any) -> GQ:
    return GQ.coerce(value)


def matrix(rows: Sequence[Sequence[Any]]) -> Matrix:
    out = tuple(tuple(scalar(value) for value in row) for row in rows)
    if not out or not out[0]:
        raise ValueError("matrix must be nonempty")
    width = len(out[0])
    if any(len(row) != width for row in out):
        raise ValueError("ragged matrix")
    return out


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


def matsub(left: Matrix, right: Matrix) -> Matrix:
    return matadd(left, matscale(-1, right))


def matscale(coefficient: Any, value: Matrix) -> Matrix:
    factor = scalar(coefficient)
    return tuple(tuple(factor * entry for entry in row) for row in value)


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
        raise ValueError("cannot sum an empty matrix family")
    total = zero(*shape(values[0]))
    for value in values:
        total = matadd(total, value)
    return total


def direct_sum(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_columns = shape(left)
    right_rows, right_columns = shape(right)
    return tuple(
        tuple(
            left[row][column]
            if row < left_rows and column < left_columns
            else right[row - left_rows][column - left_columns]
            if row >= left_rows and column >= left_columns
            else ZERO
            for column in range(left_columns + right_columns)
        )
        for row in range(left_rows + right_rows)
    )


def vertical_stack(values: Sequence[Matrix]) -> Matrix:
    if not values:
        raise ValueError("cannot stack an empty matrix family")
    columns = shape(values[0])[1]
    if any(shape(value)[1] != columns for value in values):
        raise ValueError("stack column mismatch")
    return tuple(row for value in values for row in value)


def is_zero(value: Matrix) -> bool:
    return all(entry == ZERO for row in value for entry in row)


def is_isometry(value: Matrix) -> bool:
    return matmul(adjoint(value), value) == identity(shape(value)[1])


def gram_family(histories: Sequence[Matrix]) -> tuple[tuple[Matrix, ...], ...]:
    if not histories:
        raise ValueError("empty history family")
    source = shape(histories[0])[1]
    target = shape(histories[0])[0]
    if any(shape(history) != (target, source) for history in histories):
        raise ValueError("histories do not share a typed source and target")
    return tuple(
        tuple(matmul(adjoint(left), right) for right in histories)
        for left in histories
    )


def class_operators(
    histories: Sequence[Matrix], coefficients: Sequence[Sequence[GQ]]
) -> tuple[Matrix, ...]:
    if not histories or not coefficients:
        raise ValueError("histories and ports must be nonempty")
    if any(len(port) != len(histories) for port in coefficients):
        raise ValueError("coefficient/history width mismatch")
    gram_family(histories)
    return tuple(
        matrix_sum(tuple(matscale(coefficient, history) for coefficient, history in zip(port, histories)))
        for port in coefficients
    )


def completeness_operator(
    histories: Sequence[Matrix], coefficients: Sequence[Sequence[GQ]]
) -> Matrix:
    operators = class_operators(histories, coefficients)
    source = shape(histories[0])[1]
    return matrix_sum(tuple(matmul(adjoint(operator), operator) for operator in operators))


def completeness_residual(
    histories: Sequence[Matrix], coefficients: Sequence[Sequence[GQ]]
) -> Matrix:
    return matsub(completeness_operator(histories, coefficients), identity(shape(histories[0])[1]))


def parity_coefficients() -> tuple[tuple[GQ, GQ], tuple[GQ, GQ]]:
    half = GQ(Q(1, 2))
    return ((half, half), (half, -half))


def flag_dilation(
    histories: Sequence[Matrix], coefficients: Sequence[Sequence[GQ]]
) -> Matrix:
    """Canonical output-record dilation, with the flag encoded by row blocks."""

    return vertical_stack(class_operators(histories, coefficients))


def relative_operator(left: Matrix, right: Matrix) -> Matrix:
    if shape(left) != shape(right):
        raise ValueError("relative operator needs a shared source and target")
    return matmul(adjoint(left), right)


def qmatrix(rows: Sequence[Sequence[Any]]) -> QMatrix:
    out = tuple(tuple(Q(value) for value in row) for row in rows)
    if not out:
        return tuple()
    width = len(out[0])
    if any(len(row) != width for row in out):
        raise ValueError("ragged rational matrix")
    return out


def rref(value: QMatrix) -> tuple[QMatrix, tuple[int, ...]]:
    if not value:
        return tuple(), tuple()
    work = [list(row) for row in value]
    rows = len(work)
    columns = len(work[0])
    pivot_columns: list[int] = []
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
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return tuple(tuple(entry for entry in row) for row in work), tuple(pivot_columns)


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


def operator_constraint_matrix(omega: Matrix) -> QMatrix:
    """Real-linear equations for ``z*Omega+zbar*Omega^dagger-cI=0``.

    Columns are ``(Re(z), Im(z), c)``.  Zero real/imaginary rows are retained;
    rank and nullspace routines remove their effect.
    """

    rows, columns = shape(omega)
    if rows != columns:
        raise ValueError("relative operator must be square")
    basis_x = matadd(omega, adjoint(omega))
    basis_y = matadd(matscale(I, omega), matscale(-I, adjoint(omega)))
    basis_c = matscale(-1, identity(rows))
    equations: list[tuple[Q, Q, Q]] = []
    for row in range(rows):
        for column in range(columns):
            equations.append(
                (basis_x[row][column].re, basis_y[row][column].re, basis_c[row][column].re)
            )
            equations.append(
                (basis_x[row][column].im, basis_y[row][column].im, basis_c[row][column].im)
            )
    return tuple(equations)


def phase_constraint_matrix(phases: Sequence[GQ]) -> QMatrix:
    """Exact eigenphase rows for unit-modulus Gaussian-rational phases."""

    if not phases:
        raise ValueError("at least one phase is required")
    if any(phase.norm2() != 1 for phase in phases):
        raise ValueError("phase is not unit modulus")
    unique = tuple(dict.fromkeys(phases))
    return tuple((2 * phase.re, -2 * phase.im, Q(-1)) for phase in unique)


@dataclass(frozen=True)
class Rewrite:
    name: str
    requires: frozenset[str]
    adds: frozenset[str]
    deletes: frozenset[str]
    support: frozenset[str]

    def apply(self, state: frozenset[str]) -> frozenset[str] | None:
        if not self.requires.issubset(state):
            return None
        if self.adds.intersection(state - self.deletes):
            return None
        return frozenset((state - self.deletes).union(self.adds))


def compose_rewrites(
    state: frozenset[str], order: Sequence[Rewrite]
) -> frozenset[str] | None:
    current = state
    for rewrite in order:
        following = rewrite.apply(current)
        if following is None:
            return None
        current = following
    return current


def critical_pair(
    state: frozenset[str], first: Rewrite, second: Rewrite
) -> Mapping[str, Any]:
    forward = compose_rewrites(state, (first, second))
    reverse = compose_rewrites(state, (second, first))
    overlap = bool(first.support.intersection(second.support))
    if forward is None or reverse is None:
        kind = "dependency" if (forward is None) != (reverse is None) else "both-blocked"
    elif forward == reverse:
        kind = "joinable-overlap" if overlap else "disjoint-commuting"
    else:
        kind = "divergent-endpoints"
    return {
        "kind": kind,
        "forward": None if forward is None else tuple(sorted(forward)),
        "reverse": None if reverse is None else tuple(sorted(reverse)),
    }


def product_word(generators: Mapping[str, Matrix], word: Sequence[str]) -> Matrix:
    if not word:
        first = next(iter(generators.values()))
        return identity(shape(first)[1])
    result = identity(shape(generators[word[0]])[1])
    for name in word:
        result = matmul(generators[name], result)
    return result


def factorization_words(
    target: Matrix, generators: Mapping[str, Matrix], maximum_length: int
) -> tuple[tuple[str, ...], ...]:
    if maximum_length < 1:
        raise ValueError("maximum length must be positive")
    names = tuple(sorted(generators))
    return tuple(
        word
        for length in range(1, maximum_length + 1)
        for word in itertools.product(names, repeat=length)
        if product_word(generators, word) == target
    )


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def matrix_text(value: Matrix) -> list[list[str]]:
    return [[gtext(entry) for entry in row] for row in value]


def qmatrix_text(value: QMatrix) -> list[list[str]]:
    return [[qtext(entry) for entry in row] for row in value]


def gate(name: str, passed: bool, evidence: str) -> dict[str, Any]:
    return {"gate": name, "passed": bool(passed), "evidence": evidence}


def public_calibration(mutant: str | None = None) -> dict[str, Any]:
    """Run public examples with constructor-stated answers."""

    identity_two = identity(2)
    swap = matrix([[0, 1], [1, 0]])
    grams = gram_family((identity_two, swap))
    if mutant == "public-gram":
        grams = ((grams[0][0], zero(2, 2)), grams[1])

    parity = parity_coefficients()
    parity_residual = completeness_residual((identity_two, swap), parity)
    parity_flag = flag_dilation((identity_two, swap), parity)
    if mutant == "public-parity":
        parity_residual = matadd(parity_residual, identity_two)

    phase_sets = {
        "one": (ONE,),
        "two": (ONE, -ONE),
        "three": (ONE, I, -ONE),
    }
    phase_ranks = {name: rank(phase_constraint_matrix(phases)) for name, phases in phase_sets.items()}
    phase_nullities = {name: 3 - value for name, value in phase_ranks.items()}
    if mutant == "public-rank":
        phase_ranks["three"] -= 1

    five = Q(5, 13)
    twelve = Q(12, 13)
    embed_a = matrix([[1, 0], [0, 1], [0, 0], [0, 0]])
    embed_b = matrix([[0, five], [0, 0], [1, 0], [0, twelve]])
    nonnormal = relative_operator(embed_a, embed_b)
    nonnormal_equations = operator_constraint_matrix(nonnormal)

    base = frozenset({"p", "q"})
    disjoint_left = Rewrite("left", frozenset({"p"}), frozenset({"u"}), frozenset(), frozenset({"p"}))
    disjoint_right = Rewrite("right", frozenset({"q"}), frozenset({"v"}), frozenset(), frozenset({"q"}))
    overlap_left = Rewrite("overlap-left", frozenset({"p"}), frozenset({"u"}), frozenset(), frozenset({"p"}))
    overlap_right = Rewrite("overlap-right", frozenset({"p"}), frozenset({"v"}), frozenset(), frozenset({"p"}))
    delete_p = Rewrite("delete-p", frozenset({"p"}), frozenset(), frozenset({"p"}), frozenset({"p"}))
    use_p = Rewrite("use-p", frozenset({"p"}), frozenset({"w"}), frozenset(), frozenset({"p"}))
    rewrite_kinds = (
        critical_pair(base, disjoint_left, disjoint_right)["kind"],
        critical_pair(base, overlap_left, overlap_right)["kind"],
        critical_pair(base, delete_p, use_p)["kind"],
    )

    phase_gate = matrix([[1, 0], [0, I]])
    target = matmul(phase_gate, swap)
    factorizations = factorization_words(target, {"P": phase_gate, "X": swap}, 2)

    measurements = {
        "gaussian": {"i_squared": gtext(I * I), "inverse_i": gtext(I.inverse())},
        "gram": {
            "g00": matrix_text(grams[0][0]),
            "g01": matrix_text(grams[0][1]),
            "g10": matrix_text(grams[1][0]),
            "g11": matrix_text(grams[1][1]),
        },
        "parity": {
            "residual": matrix_text(parity_residual),
            "flag_shape": list(shape(parity_flag)),
            "flag_isometry": is_isometry(parity_flag),
        },
        "phase_classifier": {
            "ranks": phase_ranks,
            "nullities": phase_nullities,
            "three_nullspace": [list(map(qtext, vector)) for vector in nullspace(phase_constraint_matrix(phase_sets["three"]))],
        },
        "nonnormal": {
            "overlap": matrix_text(nonnormal),
            "is_normal": matmul(nonnormal, adjoint(nonnormal)) == matmul(adjoint(nonnormal), nonnormal),
            "constraint_rank": rank(nonnormal_equations),
            "constraint_nullity": 3 - rank(nonnormal_equations),
        },
        "rewrite": {"critical_pair_kinds": list(rewrite_kinds)},
        "factorization": {
            "maximum_length": 2,
            "words": [list(word) for word in factorizations],
        },
    }

    gates = [
        gate("PUB-GAUSSIAN-EXACT", I * I == GQ(-1) and I.inverse() == -I, f"i^2={gtext(I*I)} inverse={gtext(I.inverse())}"),
        gate("PUB-GRAM-TYPED", grams[0][0] == identity_two and grams[1][1] == identity_two and grams[0][1] == swap and grams[1][0] == swap, f"cross={matrix_text(grams[0][1])}"),
        gate("PUB-PARITY-COMPLETE", is_zero(parity_residual), f"residual={matrix_text(parity_residual)}"),
        gate("PUB-FLAG-ISOMETRY", is_isometry(parity_flag) and shape(parity_flag) == (4, 2), f"shape={shape(parity_flag)}"),
        gate("PUB-PHASE-RANKS", phase_ranks == {"one": 1, "two": 2, "three": 3}, f"ranks={phase_ranks}"),
        gate("PUB-PHASE-NULLITIES", phase_nullities == {"one": 2, "two": 1, "three": 0}, f"nullities={phase_nullities}"),
        gate("PUB-NONNORMAL-DIRECT", is_isometry(embed_a) and is_isometry(embed_b) and nonnormal == matrix([[0, five], [0, 0]]) and rank(nonnormal_equations) == 3, f"overlap={matrix_text(nonnormal)} rank={rank(nonnormal_equations)}"),
        gate("PUB-REWRITE-CRITICAL-PAIRS", rewrite_kinds == ("disjoint-commuting", "joinable-overlap", "dependency"), f"kinds={rewrite_kinds}"),
        gate("PUB-BINARY-FACTORIZATION", ("X", "P") in factorizations and product_word({"P": phase_gate, "X": swap}, ("X", "P")) == target, f"words={factorizations}"),
    ]
    return {
        "schema": "ovg-public-v1",
        "scope": {
            "arithmetic": "Q and Q(i)",
            "role": "generic public calibrations only; no OVG physical fixture or outcome",
        },
        "measurements": measurements,
        "gates": gates,
    }


def render_public(result: Mapping[str, Any]) -> str:
    lines = ["OVG GENERIC PUBLIC CALIBRATION", f"schema: {result['schema']}"]
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
    receipt["seals"] = {
        key: digest(receipt[key]) for key in ("schema", "scope", "measurements", "gates")
    }
    return receipt


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=root / "ovg_public_output.txt")
    parser.add_argument("--receipt", type=Path, default=root / "ovg_public_receipt.json")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument(
        "--mutant",
        choices=("public-gram", "public-parity", "public-rank"),
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.selftest and args.mutant is not None:
        print("REFUSE OVG-PUBLIC-CLI :: selftest and mutant are mutually exclusive", file=sys.stderr)
        return 2
    mutant = "public-gram" if args.selftest else args.mutant
    result = public_calibration(mutant)
    failed = [row["gate"] for row in result["gates"] if not row["passed"]]
    if failed:
        label = "OVG-PUBLIC-SELFTEST" if args.selftest else "OVG-PUBLIC-GATE"
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
