#!/usr/bin/env python3
"""Generic exact core for APR.

This module contains no physical fixture, selected process law, registered
verdict, or candidate-paper prose.  It provides:

* the canonical Boolean algebra of finite binary-prefix cylinders;
* exact finite rational linear algebra, kernels, quotients, and stable nulls;
* typed finite boundary/cospan validation and gluing plans;
* distinct linear and regional future-profile quotients;
* Boolean-congruence and comparison-family invariants; and
* result-neutral exterior-invariant regional-support and faithfulness signatures.

Finite words and matrices are exact representations.  They are not spacetime
atoms, points, global slices, or ticks.  Importing this module has no side
effects.  Its only command-line mode runs deterministic algebraic self-tests
and writes solely to standard output.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Mapping, Sequence


# ---------------------------------------------------------------------------
# Canonical serialization


def fraction_text(value: Fraction) -> str:
    """Return the unique base-10 text for a rational number."""

    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def exact(value: object) -> Fraction:
    """Coerce a supported scalar to ``Fraction`` without using floating point."""

    if isinstance(value, bool):
        raise TypeError("boolean is not an exact scalar")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError(f"unsupported exact scalar {type(value).__name__}")


def canonical_data(value: object) -> object:
    """Convert supported values to a stable JSON-compatible representation."""

    if isinstance(value, Fraction):
        return fraction_text(value)
    if isinstance(value, QMatrix):
        return value.to_data()
    if isinstance(value, PrefixRegion):
        return value.to_data()
    if hasattr(value, "to_data"):
        return canonical_data(value.to_data())  # type: ignore[attr-defined]
    if isinstance(value, Mapping):
        return {
            str(key): canonical_data(value[key])
            for key in sorted(value, key=lambda item: str(item))
        }
    if isinstance(value, (tuple, list)):
        return [canonical_data(item) for item in value]
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    raise TypeError(f"unsupported canonical value {type(value).__name__}")


def canonical_json(value: object) -> str:
    """Serialize with stable key ordering and no insignificant whitespace."""

    return json.dumps(
        canonical_data(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    )


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Finite-prefix Boolean algebra


def _check_binary_word(word: object) -> str:
    if not isinstance(word, str):
        raise TypeError("prefix words must be strings")
    if any(symbol not in "01" for symbol in word):
        raise ValueError(f"non-binary prefix word {word!r}")
    return word


def _canonical_prefix_words(words: Iterable[str]) -> tuple[str, ...]:
    """Reduce a finite cylinder union to its unique prefix-free antichain.

    Covered cylinders are removed and sibling cylinders are merged recursively.
    For example, ``("00", "01", "1")`` reduces to the unit cylinder ``("",)``.
    """

    active = {_check_binary_word(word) for word in words}
    while True:
        if "" in active:
            return ("",)

        ordered = sorted(active, key=lambda item: (len(item), item))
        uncovered: set[str] = set()
        for word in ordered:
            if not any(word.startswith(prefix) for prefix in uncovered):
                uncovered.add(word)
        active = uncovered

        parents = sorted(
            {
                word[:-1]
                for word in active
                if word
                and word.endswith("0")
                and word[:-1] + "1" in active
            },
            key=lambda item: (-len(item), item),
        )
        if not parents:
            return tuple(sorted(active))
        for parent in parents:
            left = parent + "0"
            right = parent + "1"
            if left in active and right in active:
                active.remove(left)
                active.remove(right)
                active.add(parent)


@dataclass(frozen=True, slots=True)
class PrefixRegion:
    """A canonical finite union of binary-prefix cylinders."""

    words: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "words", _canonical_prefix_words(self.words))

    @classmethod
    def from_words(cls, words: Iterable[str]) -> "PrefixRegion":
        return cls(tuple(words))

    @classmethod
    def zero(cls) -> "PrefixRegion":
        return cls(())

    @classmethod
    def one(cls) -> "PrefixRegion":
        return cls(("",))

    @classmethod
    def cylinder(cls, word: str) -> "PrefixRegion":
        return cls((_check_binary_word(word),))

    def is_zero(self) -> bool:
        return not self.words

    def is_one(self) -> bool:
        return self.words == ("",)

    def join(self, other: "PrefixRegion") -> "PrefixRegion":
        return PrefixRegion(self.words + other.words)

    def meet(self, other: "PrefixRegion") -> "PrefixRegion":
        intersections: list[str] = []
        for left in self.words:
            for right in other.words:
                if right.startswith(left):
                    intersections.append(right)
                elif left.startswith(right):
                    intersections.append(left)
        return PrefixRegion(tuple(intersections))

    def complement(self) -> "PrefixRegion":
        if self.is_zero():
            return PrefixRegion.one()
        if self.is_one():
            return PrefixRegion.zero()

        occupied = set(self.words)

        def visit(prefix: str) -> list[str]:
            if prefix in occupied:
                return []
            if not any(word.startswith(prefix) for word in occupied):
                return [prefix]
            return visit(prefix + "0") + visit(prefix + "1")

        return PrefixRegion(tuple(visit("")))

    def difference(self, other: "PrefixRegion") -> "PrefixRegion":
        return self.meet(other.complement())

    def is_part_of(self, other: "PrefixRegion") -> bool:
        return self.meet(other) == self

    def overlaps(self, other: "PrefixRegion") -> bool:
        return not self.meet(other).is_zero()

    def disjoint(self, other: "PrefixRegion") -> bool:
        return self.meet(other).is_zero()

    def atomless_bipartition(self) -> tuple["PrefixRegion", "PrefixRegion"]:
        """Return two disjoint nonzero proper parts whose join is ``self``."""

        if self.is_zero():
            raise ValueError("zero has no nonzero bipartition")
        selected = self.words[0]
        left = PrefixRegion.cylinder(selected + "0")
        right = self.difference(left)
        if left.is_zero() or right.is_zero():
            raise AssertionError("prefix split did not produce nonzero parts")
        if not left.is_part_of(self) or not right.is_part_of(self):
            raise AssertionError("prefix split escaped its source region")
        if not left.disjoint(right) or left.join(right) != self:
            raise AssertionError("prefix split is not a Boolean partition")
        if left == self or right == self:
            raise AssertionError("prefix split did not produce proper parts")
        return left, right

    def to_data(self) -> dict[str, object]:
        return {"prefix_cylinders": list(self.words)}


# ---------------------------------------------------------------------------
# Exact rational matrices and subspaces


@dataclass(frozen=True, slots=True)
class QMatrix:
    """An immutable exact rational matrix retaining empty-matrix dimensions."""

    data: tuple[tuple[Fraction, ...], ...]
    ncols: int

    def __post_init__(self) -> None:
        if self.ncols < 0:
            raise ValueError("matrix column count must be nonnegative")
        converted = tuple(tuple(exact(item) for item in row) for row in self.data)
        if any(len(row) != self.ncols for row in converted):
            raise ValueError("ragged matrix")
        object.__setattr__(self, "data", converted)

    @classmethod
    def from_rows(
        cls,
        rows: Iterable[Iterable[object]],
        *,
        ncols: int | None = None,
    ) -> "QMatrix":
        converted = tuple(tuple(exact(item) for item in row) for row in rows)
        if converted:
            width = len(converted[0])
            if ncols is not None and width != ncols:
                raise ValueError("declared matrix width does not match rows")
            if any(len(row) != width for row in converted):
                raise ValueError("ragged matrix")
            return cls(converted, width)
        if ncols is None:
            raise ValueError("empty matrix needs an explicit column count")
        return cls((), ncols)

    @classmethod
    def zero(cls, nrows: int, ncols: int) -> "QMatrix":
        if nrows < 0 or ncols < 0:
            raise ValueError("matrix dimensions must be nonnegative")
        return cls(tuple(tuple(Fraction(0) for _ in range(ncols)) for _ in range(nrows)), ncols)

    @classmethod
    def identity(cls, size: int) -> "QMatrix":
        if size < 0:
            raise ValueError("identity size must be nonnegative")
        return cls(
            tuple(
                tuple(Fraction(1) if row == col else Fraction(0) for col in range(size))
                for row in range(size)
            ),
            size,
        )

    @property
    def nrows(self) -> int:
        return len(self.data)

    @property
    def shape(self) -> tuple[int, int]:
        return self.nrows, self.ncols

    def to_data(self) -> dict[str, object]:
        return {
            "shape": [self.nrows, self.ncols],
            "rows": [[fraction_text(item) for item in row] for row in self.data],
        }


def qmatrix(
    rows: Iterable[Iterable[object]],
    *,
    ncols: int | None = None,
) -> QMatrix:
    return QMatrix.from_rows(rows, ncols=ncols)


def qtranspose(value: QMatrix) -> QMatrix:
    if value.ncols == 0:
        return QMatrix.from_rows((), ncols=value.nrows)
    return QMatrix.from_rows(
        (
            (value.data[row][col] for row in range(value.nrows))
            for col in range(value.ncols)
        ),
        ncols=value.nrows,
    )


def qadd(left: QMatrix, right: QMatrix) -> QMatrix:
    if left.shape != right.shape:
        raise ValueError("matrix-add shape mismatch")
    return QMatrix.from_rows(
        (
            (left.data[row][col] + right.data[row][col] for col in range(left.ncols))
            for row in range(left.nrows)
        ),
        ncols=left.ncols,
    )


def qscale(coefficient: object, value: QMatrix) -> QMatrix:
    factor = exact(coefficient)
    return QMatrix.from_rows(
        ((factor * item for item in row) for row in value.data),
        ncols=value.ncols,
    )


def qsubtract(left: QMatrix, right: QMatrix) -> QMatrix:
    return qadd(left, qscale(-1, right))


def qmultiply(left: QMatrix, right: QMatrix) -> QMatrix:
    if left.ncols != right.nrows:
        raise ValueError(f"matrix-product shape mismatch {left.shape} x {right.shape}")
    return QMatrix.from_rows(
        (
            (
                sum(
                    (left.data[row][middle] * right.data[middle][col] for middle in range(left.ncols)),
                    Fraction(0),
                )
                for col in range(right.ncols)
            )
            for row in range(left.nrows)
        ),
        ncols=right.ncols,
    )


def qvstack(values: Sequence[QMatrix], *, ncols: int | None = None) -> QMatrix:
    if not values:
        if ncols is None:
            raise ValueError("empty row stack needs an explicit column count")
        return QMatrix.zero(0, ncols)
    width = values[0].ncols
    if ncols is not None and ncols != width:
        raise ValueError("row-stack declared width mismatch")
    if any(value.ncols != width for value in values):
        raise ValueError("row-stack shape mismatch")
    return QMatrix.from_rows(
        (row for value in values for row in value.data),
        ncols=width,
    )


def qhstack(values: Sequence[QMatrix], *, nrows: int | None = None) -> QMatrix:
    if not values:
        if nrows is None:
            raise ValueError("empty column stack needs an explicit row count")
        return QMatrix.zero(nrows, 0)
    height = values[0].nrows
    if nrows is not None and nrows != height:
        raise ValueError("column-stack declared height mismatch")
    if any(value.nrows != height for value in values):
        raise ValueError("column-stack shape mismatch")
    width = sum(value.ncols for value in values)
    return QMatrix.from_rows(
        (
            (item for value in values for item in value.data[row])
            for row in range(height)
        ),
        ncols=width,
    )


def qrref(value: QMatrix) -> tuple[QMatrix, tuple[int, ...]]:
    work = [list(row) for row in value.data]
    pivot_row = 0
    pivots: list[int] = []
    for col in range(value.ncols):
        found = next(
            (row for row in range(pivot_row, value.nrows) if work[row][col] != 0),
            None,
        )
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        pivot = work[pivot_row][col]
        work[pivot_row] = [item / pivot for item in work[pivot_row]]
        for row in range(value.nrows):
            if row == pivot_row:
                continue
            coefficient = work[row][col]
            if coefficient == 0:
                continue
            work[row] = [
                work[row][index] - coefficient * work[pivot_row][index]
                for index in range(value.ncols)
            ]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == value.nrows:
            break
    nonzero = tuple(row for row in work if any(item != 0 for item in row))
    return QMatrix.from_rows(nonzero, ncols=value.ncols), tuple(pivots)


def qrank(value: QMatrix) -> int:
    return len(qrref(value)[1])


def qrowspace(value: QMatrix) -> QMatrix:
    return qrref(value)[0]


def qkernel(value: QMatrix) -> QMatrix:
    reduced, pivots = qrref(value)
    free = tuple(col for col in range(value.ncols) if col not in pivots)
    result = [[Fraction(0) for _ in free] for _ in range(value.ncols)]
    for basis_col, free_col in enumerate(free):
        result[free_col][basis_col] = Fraction(1)
        for row, pivot_col in enumerate(pivots):
            result[pivot_col][basis_col] = -reduced.data[row][free_col]
    return QMatrix.from_rows(result, ncols=len(free))


def qcolumnspace(value: QMatrix) -> QMatrix:
    """Return a deterministic column basis for the image of ``value``."""

    return qtranspose(qrowspace(qtranspose(value)))


def qbasis_columns(ambient_dim: int, indices: Sequence[int]) -> QMatrix:
    if ambient_dim < 0:
        raise ValueError("ambient dimension must be nonnegative")
    chosen = tuple(indices)
    if len(set(chosen)) != len(chosen) or any(index < 0 or index >= ambient_dim for index in chosen):
        raise ValueError("invalid basis-column indices")
    return QMatrix.from_rows(
        (
            (Fraction(1) if row == index else Fraction(0) for index in chosen)
            for row in range(ambient_dim)
        ),
        ncols=len(chosen),
    )


def qconstraints_for_subspace(basis: QMatrix, *, ambient_dim: int) -> QMatrix:
    if basis.nrows != ambient_dim:
        raise ValueError("subspace ambient dimension mismatch")
    annihilator = qkernel(qtranspose(basis))
    return qtranspose(annihilator)


def qsubspace_sum(left: QMatrix, right: QMatrix) -> QMatrix:
    if left.nrows != right.nrows:
        raise ValueError("subspace ambient dimension mismatch")
    return qcolumnspace(qhstack((left, right)))


def qsubspace_intersection(left: QMatrix, right: QMatrix) -> QMatrix:
    if left.nrows != right.nrows:
        raise ValueError("subspace ambient dimension mismatch")
    ambient = left.nrows
    constraints = qvstack(
        (
            qconstraints_for_subspace(left, ambient_dim=ambient),
            qconstraints_for_subspace(right, ambient_dim=ambient),
        ),
        ncols=ambient,
    )
    return qcolumnspace(qkernel(constraints))


def qsubspace_inclusion_residual(subject: QMatrix, container: QMatrix) -> int:
    """Return the number of independent subject directions outside container."""

    if subject.nrows != container.nrows:
        raise ValueError("subspace ambient dimension mismatch")
    return qrank(qhstack((container, subject))) - qrank(container)


def qmatrix_key(value: QMatrix) -> str:
    return canonical_json(value)


# ---------------------------------------------------------------------------
# Future-profile quotients and continuation-stable nulls


@dataclass(frozen=True, slots=True)
class FutureProfileQuotient:
    ambient_dim: int
    profile: QMatrix
    coordinate_map: QMatrix
    null_basis: QMatrix
    section: QMatrix

    @classmethod
    def from_profile(cls, profile: QMatrix) -> "FutureProfileQuotient":
        ambient = profile.ncols
        coordinates, pivots = qrref(profile)
        section = qbasis_columns(ambient, pivots)
        null_basis = qkernel(coordinates)
        if qmultiply(coordinates, section) != QMatrix.identity(len(pivots)):
            raise AssertionError("quotient coordinate section is not normalized")
        if qrank(qmultiply(coordinates, null_basis)) != 0:
            raise AssertionError("quotient coordinates do not kill their null space")
        return cls(
            ambient_dim=ambient,
            profile=profile,
            coordinate_map=coordinates,
            null_basis=null_basis,
            section=section,
        )

    @property
    def quotient_dim(self) -> int:
        return self.coordinate_map.nrows

    @property
    def nullity(self) -> int:
        return self.null_basis.ncols

    def project(self, vectors: QMatrix) -> QMatrix:
        if vectors.nrows != self.ambient_dim:
            raise ValueError("quotient projection ambient dimension mismatch")
        return qmultiply(self.coordinate_map, vectors)

    def descent_residual(self, operator: QMatrix, target: "FutureProfileQuotient") -> QMatrix:
        if operator.shape != (target.ambient_dim, self.ambient_dim):
            raise ValueError("quotient descent operator shape mismatch")
        return qmultiply(target.coordinate_map, qmultiply(operator, self.null_basis))

    def descended_map(self, operator: QMatrix, target: "FutureProfileQuotient") -> QMatrix:
        residual = self.descent_residual(operator, target)
        if qrank(residual) != 0:
            raise ValueError("operator does not descend through the predictive quotient")
        return qmultiply(target.coordinate_map, qmultiply(operator, self.section))

    def to_data(self) -> dict[str, object]:
        return {
            "ambient_dim": self.ambient_dim,
            "profile": self.profile,
            "coordinate_map": self.coordinate_map,
            "null_basis": self.null_basis,
            "section": self.section,
            "quotient_dim": self.quotient_dim,
            "nullity": self.nullity,
        }


@dataclass(frozen=True, slots=True)
class LinearContinuation:
    name: str
    source: str
    target: str
    operator: QMatrix

    def __post_init__(self) -> None:
        if not self.name or not self.source or not self.target:
            raise ValueError("continuation names and endpoints must be nonempty")

    def to_data(self) -> dict[str, object]:
        return {
            "name": self.name,
            "source": self.source,
            "target": self.target,
            "operator": self.operator,
        }


@dataclass(frozen=True, slots=True)
class StableBoundaryNull:
    name: str
    ambient_dim: int
    constraints: QMatrix
    quotient: FutureProfileQuotient

    def to_data(self) -> dict[str, object]:
        return {
            "name": self.name,
            "ambient_dim": self.ambient_dim,
            "constraints": self.constraints,
            "quotient": self.quotient,
        }


@dataclass(frozen=True, slots=True)
class StableNullFamily:
    boundaries: tuple[StableBoundaryNull, ...]
    rank_history: tuple[tuple[tuple[str, int], ...], ...]
    strict_rounds: int

    def boundary(self, name: str) -> StableBoundaryNull:
        matches = tuple(item for item in self.boundaries if item.name == name)
        if len(matches) != 1:
            raise KeyError(name)
        return matches[0]

    def continuation_residual(self, continuation: LinearContinuation) -> QMatrix:
        source = self.boundary(continuation.source).quotient
        target = self.boundary(continuation.target).quotient
        return source.descent_residual(continuation.operator, target)

    def to_data(self) -> dict[str, object]:
        return {
            "boundaries": self.boundaries,
            "rank_history": self.rank_history,
            "strict_rounds": self.strict_rounds,
        }


def compute_stable_null(
    dimensions: Mapping[str, int],
    immediate_profiles: Mapping[str, QMatrix],
    continuations: Sequence[LinearContinuation],
) -> StableNullFamily:
    """Compute the largest continuation-stable present null family.

    The implementation grows the row constraints generated by every future
    continuation.  Their kernels are the descending null spaces.
    """

    names = tuple(sorted(dimensions))
    if not names:
        raise ValueError("stable-null family needs at least one boundary")
    if set(immediate_profiles) != set(names):
        raise ValueError("every boundary needs an immediate profile matrix")
    if any(dimensions[name] < 0 for name in names):
        raise ValueError("boundary dimensions must be nonnegative")

    current: dict[str, QMatrix] = {}
    for name in names:
        profile = immediate_profiles[name]
        if profile.ncols != dimensions[name]:
            raise ValueError(f"immediate profile width mismatch at {name}")
        current[name] = qrowspace(profile)

    outgoing: dict[str, list[LinearContinuation]] = {name: [] for name in names}
    seen_edges: set[str] = set()
    for continuation in continuations:
        if continuation.name in seen_edges:
            raise ValueError(f"duplicate continuation name {continuation.name}")
        seen_edges.add(continuation.name)
        if continuation.source not in dimensions or continuation.target not in dimensions:
            raise ValueError(f"unknown continuation endpoint on {continuation.name}")
        expected = (dimensions[continuation.target], dimensions[continuation.source])
        if continuation.operator.shape != expected:
            raise ValueError(
                f"continuation {continuation.name} has shape {continuation.operator.shape}, expected {expected}"
            )
        outgoing[continuation.source].append(continuation)

    history: list[tuple[tuple[str, int], ...]] = [
        tuple((name, qrank(current[name])) for name in names)
    ]
    strict_rounds = 0
    for _ in range(sum(dimensions.values()) + 1):
        updated: dict[str, QMatrix] = {}
        for name in names:
            rows = [current[name]]
            for continuation in sorted(outgoing[name], key=lambda item: item.name):
                target_constraints = current[continuation.target]
                rows.append(qmultiply(target_constraints, continuation.operator))
            updated[name] = qrowspace(qvstack(rows, ncols=dimensions[name]))
        if all(updated[name] == current[name] for name in names):
            break
        current = updated
        strict_rounds += 1
        history.append(tuple((name, qrank(current[name])) for name in names))
    else:
        raise RuntimeError("stable-null computation exceeded its finite rank bound")

    boundaries = tuple(
        StableBoundaryNull(
            name=name,
            ambient_dim=dimensions[name],
            constraints=current[name],
            quotient=FutureProfileQuotient.from_profile(current[name]),
        )
        for name in names
    )
    result = StableNullFamily(boundaries, tuple(history), strict_rounds)
    for continuation in continuations:
        if qrank(result.continuation_residual(continuation)) != 0:
            raise AssertionError("stable-null fixed point is not a continuation congruence")
    return result


# ---------------------------------------------------------------------------
# Finite predictive boundaries and regional profile equivalence


def _matrix_column(value: QMatrix, column: int) -> tuple[Fraction, ...]:
    if column < 0 or column >= value.ncols:
        raise IndexError(column)
    return tuple(value.data[row][column] for row in range(value.nrows))


def _profile_key(profile: Sequence[Fraction]) -> str:
    return canonical_json(tuple(profile))


@dataclass(frozen=True, slots=True)
class PredictiveBoundary:
    """Canonical finite quotient of labels by equality of full profile columns.

    This configuration-level quotient is deliberately distinct from the linear
    quotient ``V / ker(Phi)`` above.  Duplicate labels have one predictive class
    even when the profile is constant.
    """

    labels: tuple[str, ...]
    profile_matrix: QMatrix
    classes: tuple[tuple[str, ...], ...]
    class_profiles: tuple[tuple[str, tuple[Fraction, ...]], ...]

    @classmethod
    def from_profiles(
        cls,
        labels: Sequence[str],
        profile_matrix: QMatrix,
    ) -> "PredictiveBoundary":
        supplied_labels = tuple(labels)
        if any(not isinstance(label, str) or not label for label in supplied_labels):
            raise ValueError("predictive-boundary labels must be nonempty strings")
        if len(set(supplied_labels)) != len(supplied_labels):
            raise ValueError("predictive-boundary labels must be unique")
        if profile_matrix.ncols != len(supplied_labels):
            raise ValueError("one profile column is required per boundary label")

        ordered_indices = tuple(
            index for index, _ in sorted(enumerate(supplied_labels), key=lambda item: item[1])
        )
        canonical_labels = tuple(supplied_labels[index] for index in ordered_indices)
        canonical_profile = QMatrix.from_rows(
            (
                (profile_matrix.data[row][index] for index in ordered_indices)
                for row in range(profile_matrix.nrows)
            ),
            ncols=len(canonical_labels),
        )
        items = tuple(
            (label, _profile_key(_matrix_column(canonical_profile, index)))
            for index, label in enumerate(canonical_labels)
        )
        classes = _equivalence_classes(items)
        profile_by_label = {
            label: _matrix_column(canonical_profile, index)
            for index, label in enumerate(canonical_labels)
        }
        class_profiles = tuple(
            (members[0], profile_by_label[members[0]])
            for members in classes
        )
        return cls(
            labels=canonical_labels,
            profile_matrix=canonical_profile,
            classes=classes,
            class_profiles=class_profiles,
        )

    def class_of(self, label: str) -> tuple[str, ...]:
        matches = tuple(members for members in self.classes if label in members)
        if len(matches) != 1:
            raise KeyError(label)
        return matches[0]

    def to_data(self) -> dict[str, object]:
        return {
            "labels": self.labels,
            "profile_matrix": self.profile_matrix,
            "classes": self.classes,
            "class_profiles": self.class_profiles,
        }


@dataclass(frozen=True, slots=True)
class BoundaryPartitionSignature:
    proposed_blocks: tuple[tuple[str, ...], ...]
    canonical_classes: tuple[tuple[str, ...], ...]
    mixed_profile_blocks: tuple[tuple[str, ...], ...]
    redundant_block_pairs: tuple[tuple[int, int], ...]

    def to_data(self) -> dict[str, object]:
        return {
            "proposed_blocks": self.proposed_blocks,
            "canonical_classes": self.canonical_classes,
            "mixed_profile_blocks": self.mixed_profile_blocks,
            "redundant_block_pairs": self.redundant_block_pairs,
        }


def boundary_partition_signature(
    boundary: PredictiveBoundary,
    blocks: Sequence[Sequence[str]],
) -> BoundaryPartitionSignature:
    """Compare a proposed label partition with the canonical profile quotient.

    A mixed-profile block loses predictive information.  Two proposed blocks
    contained in one canonical class are a redundant split.  The returned data
    express the finite universal-property checks without selecting a verdict.
    """

    proposed = tuple(
        sorted(
            (tuple(sorted(block)) for block in blocks),
            key=lambda block: block,
        )
    )
    flattened = tuple(label for block in proposed for label in block)
    if any(not block for block in proposed):
        raise ValueError("boundary partition blocks must be nonempty")
    if len(set(flattened)) != len(flattened) or set(flattened) != set(boundary.labels):
        raise ValueError("boundary partition must cover every label exactly once")

    canonical_index = {
        label: index
        for index, members in enumerate(boundary.classes)
        for label in members
    }
    mixed = tuple(
        block
        for block in proposed
        if len({canonical_index[label] for label in block}) > 1
    )
    redundant: list[tuple[int, int]] = []
    for left in range(len(proposed)):
        for right in range(left + 1, len(proposed)):
            left_classes = {canonical_index[label] for label in proposed[left]}
            right_classes = {canonical_index[label] for label in proposed[right]}
            if len(left_classes) == 1 and left_classes == right_classes:
                redundant.append((left, right))
    return BoundaryPartitionSignature(
        proposed_blocks=proposed,
        canonical_classes=boundary.classes,
        mixed_profile_blocks=mixed,
        redundant_block_pairs=tuple(redundant),
    )


@dataclass(frozen=True, slots=True)
class RegionProfileEntry:
    name: str
    region: PrefixRegion
    profile: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("regional profile entry needs a name")
        object.__setattr__(self, "profile", tuple(exact(item) for item in self.profile))

    def to_data(self) -> dict[str, object]:
        return {"name": self.name, "region": self.region, "profile": self.profile}


@dataclass(frozen=True, slots=True)
class RegionalCongruenceViolation:
    left: str
    right: str
    context: str
    operation: str
    left_result: str
    right_result: str

    def to_data(self) -> dict[str, object]:
        return {
            "left": self.left,
            "right": self.right,
            "context": self.context,
            "operation": self.operation,
            "left_result": self.left_result,
            "right_result": self.right_result,
        }


@dataclass(frozen=True, slots=True)
class RegionalProfileEquivalence:
    profile_dim: int
    classes: tuple[tuple[str, ...], ...]
    complement_violations: tuple[RegionalCongruenceViolation, ...]
    meet_violations: tuple[RegionalCongruenceViolation, ...]
    join_violations: tuple[RegionalCongruenceViolation, ...]
    missing_closures: tuple[tuple[str, str, str], ...]

    def to_data(self) -> dict[str, object]:
        return {
            "profile_dim": self.profile_dim,
            "classes": self.classes,
            "complement_violations": self.complement_violations,
            "meet_violations": self.meet_violations,
            "join_violations": self.join_violations,
            "missing_closures": self.missing_closures,
        }


def regional_profile_equivalence(
    entries: Sequence[RegionProfileEntry],
) -> RegionalProfileEquivalence:
    """Group regions by profile and audit Boolean-congruence compatibility.

    Profile equality is *not* assumed to be a congruence.  The returned
    violations and missing closures are the separate gate needed before a
    Boolean quotient can be formed.
    """

    if not entries:
        raise ValueError("regional profile equivalence needs entries")
    if len({entry.name for entry in entries}) != len(entries):
        raise ValueError("regional profile entry names must be unique")
    if len({entry.region for entry in entries}) != len(entries):
        raise ValueError("regional profile entries must use distinct regions")
    profile_dim = len(entries[0].profile)
    if any(len(entry.profile) != profile_dim for entry in entries):
        raise ValueError("regional profiles need one common dimension")

    ordered = tuple(sorted(entries, key=lambda item: item.name))
    by_region = {entry.region: entry for entry in ordered}
    classes = _equivalence_classes(
        tuple((entry.name, _profile_key(entry.profile)) for entry in ordered)
    )
    by_name = {entry.name: entry for entry in ordered}
    equivalent_pairs = tuple(
        (members[left], members[right])
        for members in classes
        for left in range(len(members))
        for right in range(left + 1, len(members))
    )

    complement_violations: list[RegionalCongruenceViolation] = []
    meet_violations: list[RegionalCongruenceViolation] = []
    join_violations: list[RegionalCongruenceViolation] = []
    missing: list[tuple[str, str, str]] = []

    def compare_results(
        left_name: str,
        right_name: str,
        context_name: str,
        operation: str,
        left_region: PrefixRegion,
        right_region: PrefixRegion,
        destination: list[RegionalCongruenceViolation],
    ) -> None:
        left_result = by_region.get(left_region)
        right_result = by_region.get(right_region)
        if left_result is None:
            missing.append((left_name, context_name, f"{operation}:left"))
        if right_result is None:
            missing.append((right_name, context_name, f"{operation}:right"))
        if left_result is None or right_result is None:
            return
        if left_result.profile != right_result.profile:
            destination.append(
                RegionalCongruenceViolation(
                    left=left_name,
                    right=right_name,
                    context=context_name,
                    operation=operation,
                    left_result=left_result.name,
                    right_result=right_result.name,
                )
            )

    for left_name, right_name in equivalent_pairs:
        left = by_name[left_name]
        right = by_name[right_name]
        compare_results(
            left_name,
            right_name,
            "unit",
            "complement",
            left.region.complement(),
            right.region.complement(),
            complement_violations,
        )
        for context in ordered:
            compare_results(
                left_name,
                right_name,
                context.name,
                "meet",
                left.region.meet(context.region),
                right.region.meet(context.region),
                meet_violations,
            )
            compare_results(
                left_name,
                right_name,
                context.name,
                "join",
                left.region.join(context.region),
                right.region.join(context.region),
                join_violations,
            )

    return RegionalProfileEquivalence(
        profile_dim=profile_dim,
        classes=classes,
        complement_violations=tuple(complement_violations),
        meet_violations=tuple(meet_violations),
        join_violations=tuple(join_violations),
        missing_closures=tuple(sorted(set(missing))),
    )


# ---------------------------------------------------------------------------
# Neutral comparison-family invariants


@dataclass(frozen=True, slots=True)
class ComparisonCandidate:
    name: str
    operator: QMatrix

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("comparison candidate needs a name")

    def to_data(self) -> dict[str, object]:
        return {"name": self.name, "operator": self.operator}


@dataclass(frozen=True, slots=True)
class ComparisonSignature:
    name: str
    raw_operator_sha256: str
    descent_residual_rank: int
    future_action: QMatrix
    quotient_action: QMatrix | None

    def to_data(self) -> dict[str, object]:
        return {
            "name": self.name,
            "raw_operator_sha256": self.raw_operator_sha256,
            "descent_residual_rank": self.descent_residual_rank,
            "future_action": self.future_action,
            "quotient_action": self.quotient_action,
        }


@dataclass(frozen=True, slots=True)
class ComparisonFamilyInvariants:
    signatures: tuple[ComparisonSignature, ...]
    raw_classes: tuple[tuple[str, ...], ...]
    quotient_classes: tuple[tuple[str, ...], ...]
    future_action_classes: tuple[tuple[str, ...], ...]
    non_descending: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "signatures": self.signatures,
            "raw_classes": self.raw_classes,
            "quotient_classes": self.quotient_classes,
            "future_action_classes": self.future_action_classes,
            "non_descending": self.non_descending,
        }


def _equivalence_classes(items: Sequence[tuple[str, str]]) -> tuple[tuple[str, ...], ...]:
    grouped: dict[str, list[str]] = {}
    for name, key in items:
        grouped.setdefault(key, []).append(name)
    return tuple(
        sorted(
            (tuple(sorted(names)) for names in grouped.values()),
            key=lambda names: names,
        )
    )


def profile_naturality_residual(
    source_profile: QMatrix,
    target_profile: QMatrix,
    operator: QMatrix,
) -> QMatrix:
    """Return ``target_profile * operator - source_profile`` exactly."""

    if operator.shape != (target_profile.ncols, source_profile.ncols):
        raise ValueError("profile naturality operator shape mismatch")
    transported = qmultiply(target_profile, operator)
    if transported.shape != source_profile.shape:
        raise ValueError("profile naturality row type mismatch")
    return qsubtract(transported, source_profile)


def comparison_family_invariants(
    source: FutureProfileQuotient,
    target: FutureProfileQuotient,
    candidates: Sequence[ComparisonCandidate],
) -> ComparisonFamilyInvariants:
    if len({candidate.name for candidate in candidates}) != len(candidates):
        raise ValueError("comparison candidate names must be unique")

    signatures: list[ComparisonSignature] = []
    raw_items: list[tuple[str, str]] = []
    quotient_items: list[tuple[str, str]] = []
    future_items: list[tuple[str, str]] = []
    non_descending: list[str] = []

    for candidate in sorted(candidates, key=lambda item: item.name):
        if candidate.operator.shape != (target.ambient_dim, source.ambient_dim):
            raise ValueError(f"comparison {candidate.name} has an incompatible shape")
        residual = source.descent_residual(candidate.operator, target)
        residual_rank = qrank(residual)
        future_action = qmultiply(target.coordinate_map, candidate.operator)
        quotient_action: QMatrix | None = None
        if residual_rank == 0:
            quotient_action = source.descended_map(candidate.operator, target)
            quotient_items.append((candidate.name, qmatrix_key(quotient_action)))
        else:
            non_descending.append(candidate.name)
        raw_key = qmatrix_key(candidate.operator)
        future_key = qmatrix_key(future_action)
        raw_items.append((candidate.name, raw_key))
        future_items.append((candidate.name, future_key))
        signatures.append(
            ComparisonSignature(
                name=candidate.name,
                raw_operator_sha256=hashlib.sha256(raw_key.encode("utf-8")).hexdigest(),
                descent_residual_rank=residual_rank,
                future_action=future_action,
                quotient_action=quotient_action,
            )
        )

    return ComparisonFamilyInvariants(
        signatures=tuple(signatures),
        raw_classes=_equivalence_classes(raw_items),
        quotient_classes=_equivalence_classes(quotient_items),
        future_action_classes=_equivalence_classes(future_items),
        non_descending=tuple(sorted(non_descending)),
    )


# ---------------------------------------------------------------------------
# Typed finite boundaries and structured cospans


def _canonical_generators(values: Iterable[str]) -> tuple[str, ...]:
    raw = tuple(values)
    if any(not isinstance(value, str) or not value for value in raw):
        raise ValueError("generators must be nonempty strings")
    if len(set(raw)) != len(raw):
        raise ValueError("generators must be unique")
    return tuple(sorted(raw))


@dataclass(frozen=True, slots=True)
class BoundaryType:
    name: str
    generators: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("boundary type needs a name")
        object.__setattr__(self, "generators", _canonical_generators(self.generators))

    def to_data(self) -> dict[str, object]:
        return {"name": self.name, "generators": self.generators}


@dataclass(frozen=True, slots=True)
class RegionType:
    name: str
    generators: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("region type needs a name")
        object.__setattr__(self, "generators", _canonical_generators(self.generators))

    def to_data(self) -> dict[str, object]:
        return {"name": self.name, "generators": self.generators}


def _canonical_images(
    images: Iterable[tuple[str, str]],
    source_generators: Sequence[str],
    target_generators: Sequence[str],
) -> tuple[tuple[str, str], ...]:
    raw = tuple(images)
    domain = tuple(left for left, _ in raw)
    if len(set(domain)) != len(domain):
        raise ValueError("finite map assigns one generator more than once")
    if set(domain) != set(source_generators):
        raise ValueError("finite map must be total on its source generators")
    if any(right not in target_generators for _, right in raw):
        raise ValueError("finite map targets an unknown generator")
    return tuple(sorted(raw))


@dataclass(frozen=True, slots=True)
class BoundaryLeg:
    source: BoundaryType
    target: RegionType
    images: tuple[tuple[str, str], ...]

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "images",
            _canonical_images(self.images, self.source.generators, self.target.generators),
        )

    def image(self, generator: str) -> str:
        mapping = dict(self.images)
        if generator not in mapping:
            raise KeyError(generator)
        return mapping[generator]

    def fiber_sizes(self) -> tuple[tuple[str, int], ...]:
        return tuple(
            (target, sum(1 for _, image in self.images if image == target))
            for target in self.target.generators
        )

    def to_data(self) -> dict[str, object]:
        return {"source": self.source, "target": self.target, "images": self.images}


@dataclass(frozen=True, slots=True)
class BoundaryComparison:
    source: BoundaryType
    target: BoundaryType
    images: tuple[tuple[str, str], ...]

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "images",
            _canonical_images(self.images, self.source.generators, self.target.generators),
        )

    @classmethod
    def identity(cls, boundary: BoundaryType) -> "BoundaryComparison":
        return cls(boundary, boundary, tuple((item, item) for item in boundary.generators))

    def image(self, generator: str) -> str:
        mapping = dict(self.images)
        if generator not in mapping:
            raise KeyError(generator)
        return mapping[generator]

    def fiber_sizes(self) -> tuple[tuple[str, int], ...]:
        return tuple(
            (target, sum(1 for _, image in self.images if image == target))
            for target in self.target.generators
        )

    def to_data(self) -> dict[str, object]:
        return {"source": self.source, "target": self.target, "images": self.images}


@dataclass(frozen=True, slots=True)
class StructuredCospan:
    name: str
    incoming: BoundaryType
    apex: RegionType
    outgoing: BoundaryType
    in_leg: BoundaryLeg
    out_leg: BoundaryLeg

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("structured cospan needs a name")

    def to_data(self) -> dict[str, object]:
        return {
            "name": self.name,
            "incoming": self.incoming,
            "apex": self.apex,
            "outgoing": self.outgoing,
            "in_leg": self.in_leg,
            "out_leg": self.out_leg,
        }


@dataclass(frozen=True, slots=True)
class CospanValidation:
    name: str
    issues: tuple[str, ...]
    in_fibers: tuple[tuple[str, int], ...]
    out_fibers: tuple[tuple[str, int], ...]

    def to_data(self) -> dict[str, object]:
        return {
            "name": self.name,
            "issues": self.issues,
            "in_fibers": self.in_fibers,
            "out_fibers": self.out_fibers,
        }


def validate_cospan(
    value: StructuredCospan,
    *,
    require_injective_legs: bool = False,
) -> CospanValidation:
    issues: list[str] = []
    if value.in_leg.source != value.incoming:
        issues.append("incoming-leg-source")
    if value.in_leg.target != value.apex:
        issues.append("incoming-leg-target")
    if value.out_leg.source != value.outgoing:
        issues.append("outgoing-leg-source")
    if value.out_leg.target != value.apex:
        issues.append("outgoing-leg-target")
    if require_injective_legs:
        if len({target for _, target in value.in_leg.images}) != len(value.in_leg.images):
            issues.append("incoming-leg-noninjective")
        if len({target for _, target in value.out_leg.images}) != len(value.out_leg.images):
            issues.append("outgoing-leg-noninjective")
    return CospanValidation(
        name=value.name,
        issues=tuple(sorted(issues)),
        in_fibers=value.in_leg.fiber_sizes(),
        out_fibers=value.out_leg.fiber_sizes(),
    )


@dataclass(frozen=True, slots=True)
class GluingValidation:
    """A typing receipt, not a constructed pushout or physical composite.

    ``apex_identifications`` lists the finite equations that a later gluing
    constructor would have to impose after every reported issue is resolved.
    This core deliberately does not form that quotient or assign it dynamics.
    """

    left_name: str
    right_name: str
    issues: tuple[str, ...]
    apex_identifications: tuple[tuple[str, str], ...]

    def to_data(self) -> dict[str, object]:
        return {
            "left_name": self.left_name,
            "right_name": self.right_name,
            "issues": self.issues,
            "apex_identifications": self.apex_identifications,
        }


def validate_gluing(
    left: StructuredCospan,
    right: StructuredCospan,
    *,
    comparison: BoundaryComparison | None = None,
    require_injective_legs: bool = False,
) -> GluingValidation:
    """Validate shared-boundary typing without constructing a pushout."""

    issues = list(validate_cospan(left, require_injective_legs=require_injective_legs).issues)
    issues.extend(validate_cospan(right, require_injective_legs=require_injective_legs).issues)

    bridge = comparison
    if bridge is None:
        if left.outgoing == right.incoming:
            bridge = BoundaryComparison.identity(left.outgoing)
        else:
            issues.append("missing-common-boundary-comparison")
    if bridge is not None:
        if bridge.source != left.outgoing:
            issues.append("comparison-source")
        if bridge.target != right.incoming:
            issues.append("comparison-target")
        target_fibers = dict(bridge.fiber_sizes())
        if any(size != 1 for size in target_fibers.values()):
            issues.append("comparison-not-bijective")

    identifications: list[tuple[str, str]] = []
    if bridge is not None and not issues:
        for generator in left.outgoing.generators:
            identifications.append(
                (
                    left.out_leg.image(generator),
                    right.in_leg.image(bridge.image(generator)),
                )
            )
    return GluingValidation(
        left_name=left.name,
        right_name=right.name,
        issues=tuple(sorted(set(issues))),
        apex_identifications=tuple(sorted(identifications)),
    )


# ---------------------------------------------------------------------------
# Result-neutral exterior-invariant regional-support and faithfulness signatures


@dataclass(frozen=True, slots=True)
class ExteriorProfilePair:
    name: str
    left: QMatrix
    right: QMatrix

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("exterior profile pair needs a name")
        if self.left.shape != self.right.shape:
            raise ValueError("exterior profile pair shape mismatch")

    def difference(self) -> QMatrix:
        return qsubtract(self.left, self.right)

    def to_data(self) -> dict[str, object]:
        return {"name": self.name, "left": self.left, "right": self.right}


@dataclass(frozen=True, slots=True)
class SupportedInternalAction:
    """An internally generated subspace with an independently typed support."""

    name: str
    support: PrefixRegion
    generated_subspace: QMatrix

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("supported internal action needs a name")

    def to_data(self) -> dict[str, object]:
        return {
            "name": self.name,
            "support": self.support,
            "generated_subspace": self.generated_subspace,
        }


@dataclass(frozen=True, slots=True)
class SupportedExteriorReplacement:
    """A calibrated replacement pair with an independently typed support."""

    name: str
    support: PrefixRegion
    left: QMatrix
    right: QMatrix

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("supported exterior replacement needs a name")
        if self.left.shape != self.right.shape:
            raise ValueError("supported exterior replacement shape mismatch")

    def profile_pair(self) -> ExteriorProfilePair:
        return ExteriorProfilePair(self.name, self.left, self.right)

    def to_data(self) -> dict[str, object]:
        return {
            "name": self.name,
            "support": self.support,
            "left": self.left,
            "right": self.right,
        }


def dynamic_invariant_subspace(
    ambient_dim: int,
    exterior_pairs: Sequence[ExteriorProfilePair],
) -> QMatrix:
    if ambient_dim < 0:
        raise ValueError("ambient dimension must be nonnegative")
    rows: list[QMatrix] = []
    for pair in sorted(exterior_pairs, key=lambda item: item.name):
        if pair.left.ncols != ambient_dim:
            raise ValueError(f"exterior profile width mismatch on {pair.name}")
        rows.append(pair.difference())
    constraints = qrowspace(qvstack(rows, ncols=ambient_dim))
    return qcolumnspace(qkernel(constraints))


@dataclass(frozen=True, slots=True)
class LocalitySignature:
    ambient_dim: int
    kinematic_rank: int
    dynamic_rank: int
    intersection_rank: int
    joined_rank: int
    kinematic_outside_dynamic_rank: int
    dynamic_outside_kinematic_rank: int

    def to_data(self) -> dict[str, object]:
        return {
            "ambient_dim": self.ambient_dim,
            "kinematic_rank": self.kinematic_rank,
            "dynamic_rank": self.dynamic_rank,
            "intersection_rank": self.intersection_rank,
            "joined_rank": self.joined_rank,
            "kinematic_outside_dynamic_rank": self.kinematic_outside_dynamic_rank,
            "dynamic_outside_kinematic_rank": self.dynamic_outside_kinematic_rank,
        }


def locality_signature(kinematic: QMatrix, dynamic: QMatrix) -> LocalitySignature:
    if kinematic.nrows != dynamic.nrows:
        raise ValueError("locality subspaces need a common ambient dimension")
    kin = qcolumnspace(kinematic)
    dyn = qcolumnspace(dynamic)
    intersection = qsubspace_intersection(kin, dyn)
    joined = qsubspace_sum(kin, dyn)
    return LocalitySignature(
        ambient_dim=kin.nrows,
        kinematic_rank=qrank(kin),
        dynamic_rank=qrank(dyn),
        intersection_rank=qrank(intersection),
        joined_rank=qrank(joined),
        kinematic_outside_dynamic_rank=qsubspace_inclusion_residual(kin, dyn),
        dynamic_outside_kinematic_rank=qsubspace_inclusion_residual(dyn, kin),
    )


@dataclass(frozen=True, slots=True)
class RegionalSupportLocalitySignature:
    """Exact data from two independent regional-support constructions.

    The kinematic subspace is generated only from actions supported in the
    target region.  The dynamic subspace is an equalizer of replacement pairs
    supported in the Boolean disjoint complement.  No causal exterior, truth
    label, arbitrary subspace isomorphism, or physical-process verdict is
    introduced here.
    """

    region: PrefixRegion
    disjoint_complement: PrefixRegion
    internal_action_names: tuple[str, ...]
    exterior_replacement_names: tuple[str, ...]
    kinematic_subspace: QMatrix
    support_dynamic_subspace: QMatrix
    common_ambient_signature: LocalitySignature

    def to_data(self) -> dict[str, object]:
        return {
            "region": self.region,
            "disjoint_complement": self.disjoint_complement,
            "internal_action_names": self.internal_action_names,
            "exterior_replacement_names": self.exterior_replacement_names,
            "kinematic_subspace": self.kinematic_subspace,
            "support_dynamic_subspace": self.support_dynamic_subspace,
            "common_ambient_signature": self.common_ambient_signature,
        }


def regional_support_locality_signature(
    region: PrefixRegion,
    internal_actions: Sequence[SupportedInternalAction],
    exterior_replacements: Sequence[SupportedExteriorReplacement],
    *,
    ambient_dim: int,
) -> RegionalSupportLocalitySignature:
    """Construct regional ``Kin`` and complement-invariant ``SuppDyn``.

    The two inputs are distinct catalogues and the constructions use different
    algorithms.  Equality, when it occurs, is tested as equality of calibrated
    subspaces in one ambient vector space through inclusion residuals; equal
    dimensions or an arbitrary abstract isomorphism are insufficient.
    """

    if ambient_dim < 0:
        raise ValueError("ambient dimension must be nonnegative")
    if len({item.name for item in internal_actions}) != len(internal_actions):
        raise ValueError("supported internal action names must be unique")
    if len({item.name for item in exterior_replacements}) != len(exterior_replacements):
        raise ValueError("supported exterior replacement names must be unique")
    if any(item.generated_subspace.nrows != ambient_dim for item in internal_actions):
        raise ValueError("internal generated-subspace ambient dimension mismatch")
    if any(item.left.ncols != ambient_dim for item in exterior_replacements):
        raise ValueError("exterior replacement profile width mismatch")

    internal = tuple(
        sorted(
            (item for item in internal_actions if item.support.is_part_of(region)),
            key=lambda item: item.name,
        )
    )
    complement = region.complement()
    exterior = tuple(
        sorted(
            (
                item
                for item in exterior_replacements
                if item.support.is_part_of(complement)
            ),
            key=lambda item: item.name,
        )
    )

    if internal:
        kinematic = qcolumnspace(
            qhstack(tuple(item.generated_subspace for item in internal))
        )
    else:
        kinematic = QMatrix.zero(ambient_dim, 0)
    support_dynamic = dynamic_invariant_subspace(
        ambient_dim,
        tuple(item.profile_pair() for item in exterior),
    )
    return RegionalSupportLocalitySignature(
        region=region,
        disjoint_complement=complement,
        internal_action_names=tuple(item.name for item in internal),
        exterior_replacement_names=tuple(item.name for item in exterior),
        kinematic_subspace=kinematic,
        support_dynamic_subspace=support_dynamic,
        common_ambient_signature=locality_signature(kinematic, support_dynamic),
    )


@dataclass(frozen=True, slots=True)
class SupportEntry:
    name: str
    region: PrefixRegion
    basis: QMatrix

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("support entry needs a name")

    def to_data(self) -> dict[str, object]:
        return {"name": self.name, "region": self.region, "basis": self.basis}


@dataclass(frozen=True, slots=True)
class SupportPairResidual:
    left: str
    right: str
    residual_rank: int

    def to_data(self) -> dict[str, object]:
        return {"left": self.left, "right": self.right, "residual_rank": self.residual_rank}


@dataclass(frozen=True, slots=True)
class SupportLatticeResidual:
    left: str
    right: str
    operation: str
    expected_outside_constructed_rank: int
    constructed_outside_expected_rank: int

    def to_data(self) -> dict[str, object]:
        return {
            "left": self.left,
            "right": self.right,
            "operation": self.operation,
            "expected_outside_constructed_rank": self.expected_outside_constructed_rank,
            "constructed_outside_expected_rank": self.constructed_outside_expected_rank,
        }


@dataclass(frozen=True, slots=True)
class SupportFaithfulnessSignature:
    ambient_dim: int
    ranks: tuple[tuple[str, int], ...]
    collision_classes: tuple[tuple[str, ...], ...]
    order_preservation_residuals: tuple[SupportPairResidual, ...]
    order_reflection_extras: tuple[SupportPairResidual, ...]
    lattice_residuals: tuple[SupportLatticeResidual, ...]
    missing_closures: tuple[tuple[str, str, str], ...]
    nonzero_regions_with_zero_support: tuple[str, ...]
    proper_supported_subregion_counts: tuple[tuple[str, int], ...]

    def to_data(self) -> dict[str, object]:
        return {
            "ambient_dim": self.ambient_dim,
            "ranks": self.ranks,
            "collision_classes": self.collision_classes,
            "order_preservation_residuals": self.order_preservation_residuals,
            "order_reflection_extras": self.order_reflection_extras,
            "lattice_residuals": self.lattice_residuals,
            "missing_closures": self.missing_closures,
            "nonzero_regions_with_zero_support": self.nonzero_regions_with_zero_support,
            "proper_supported_subregion_counts": self.proper_supported_subregion_counts,
        }


def support_faithfulness_signature(
    entries: Sequence[SupportEntry],
    *,
    ambient_dim: int,
) -> SupportFaithfulnessSignature:
    if ambient_dim < 0:
        raise ValueError("ambient dimension must be nonnegative")
    if len({entry.name for entry in entries}) != len(entries):
        raise ValueError("support entry names must be unique")
    if len({entry.region for entry in entries}) != len(entries):
        raise ValueError("support entries must use distinct canonical regions")
    if any(entry.basis.nrows != ambient_dim for entry in entries):
        raise ValueError("support basis ambient dimension mismatch")

    ordered = tuple(sorted(entries, key=lambda item: item.name))
    bases = {entry.name: qcolumnspace(entry.basis) for entry in ordered}
    by_region = {entry.region: entry for entry in ordered}
    ranks = tuple((entry.name, qrank(bases[entry.name])) for entry in ordered)
    collision_classes = _equivalence_classes(
        tuple((entry.name, qmatrix_key(bases[entry.name])) for entry in ordered)
    )

    preservation: list[SupportPairResidual] = []
    reflection: list[SupportPairResidual] = []
    lattice: list[SupportLatticeResidual] = []
    missing: list[tuple[str, str, str]] = []

    for left in ordered:
        for right in ordered:
            residual = qsubspace_inclusion_residual(bases[left.name], bases[right.name])
            if left.region.is_part_of(right.region):
                if residual != 0:
                    preservation.append(SupportPairResidual(left.name, right.name, residual))
            elif residual == 0:
                reflection.append(SupportPairResidual(left.name, right.name, residual))

    for left_index, left in enumerate(ordered):
        for right in ordered[left_index:]:
            for operation, region, constructed in (
                (
                    "meet",
                    left.region.meet(right.region),
                    qsubspace_intersection(bases[left.name], bases[right.name]),
                ),
                (
                    "join",
                    left.region.join(right.region),
                    qsubspace_sum(bases[left.name], bases[right.name]),
                ),
            ):
                expected_entry = by_region.get(region)
                if expected_entry is None:
                    missing.append((left.name, right.name, operation))
                    continue
                expected_basis = bases[expected_entry.name]
                lattice.append(
                    SupportLatticeResidual(
                        left=left.name,
                        right=right.name,
                        operation=operation,
                        expected_outside_constructed_rank=qsubspace_inclusion_residual(
                            expected_basis, constructed
                        ),
                        constructed_outside_expected_rank=qsubspace_inclusion_residual(
                            constructed, expected_basis
                        ),
                    )
                )

    zero_support = tuple(
        entry.name
        for entry in ordered
        if not entry.region.is_zero() and qrank(bases[entry.name]) == 0
    )
    proper_counts: list[tuple[str, int]] = []
    for outer in ordered:
        count = 0
        outer_rank = qrank(bases[outer.name])
        for inner in ordered:
            if inner.region == outer.region or inner.region.is_zero():
                continue
            if inner.region.is_part_of(outer.region):
                residual = qsubspace_inclusion_residual(bases[inner.name], bases[outer.name])
                inner_rank = qrank(bases[inner.name])
                if residual == 0 and 0 < inner_rank < outer_rank:
                    count += 1
        proper_counts.append((outer.name, count))

    return SupportFaithfulnessSignature(
        ambient_dim=ambient_dim,
        ranks=ranks,
        collision_classes=collision_classes,
        order_preservation_residuals=tuple(preservation),
        order_reflection_extras=tuple(reflection),
        lattice_residuals=tuple(lattice),
        missing_closures=tuple(sorted(missing)),
        nonzero_regions_with_zero_support=zero_support,
        proper_supported_subregion_counts=tuple(proper_counts),
    )


# ---------------------------------------------------------------------------
# Deterministic algebra-only self-tests and strict CLI


class SelfTestFailure(AssertionError):
    pass


def _require(condition: bool, name: str) -> None:
    if not condition:
        raise SelfTestFailure(name)


def run_selftests() -> dict[str, object]:
    tests: list[str] = []

    def check(name: str, condition: bool) -> None:
        _require(condition, name)
        tests.append(name)

    # Canonical prefix algebra and atomless splitting.
    unit = PrefixRegion.from_words(("00", "01", "1"))
    check("prefix-canonical-sibling-reduction", unit == PrefixRegion.one())
    region = PrefixRegion.from_words(("00", "10"))
    complement = region.complement()
    check("prefix-complement-meet", region.meet(complement) == PrefixRegion.zero())
    check("prefix-complement-join", region.join(complement) == PrefixRegion.one())
    other = PrefixRegion.from_words(("0", "11"))
    check(
        "prefix-de-morgan",
        region.join(other).complement() == region.complement().meet(other.complement()),
    )
    left_part, right_part = region.atomless_bipartition()
    check("prefix-atomless-split-disjoint", left_part.disjoint(right_part))
    check("prefix-atomless-split-total", left_part.join(right_part) == region)
    check(
        "prefix-atomless-split-proper",
        left_part != region and right_part != region,
    )

    # Exact row reduction, kernels, and quotient coordinates.
    profile = qmatrix(((1, 1, 0), (0, 0, 1)))
    null_basis = qkernel(profile)
    check("linear-rank-nullity", qrank(profile) + null_basis.ncols == profile.ncols)
    check("linear-kernel-annihilation", qrank(qmultiply(profile, null_basis)) == 0)
    quotient = FutureProfileQuotient.from_profile(profile)
    check(
        "quotient-coordinate-section",
        qmultiply(quotient.coordinate_map, quotient.section)
        == QMatrix.identity(quotient.quotient_dim),
    )
    check("quotient-null-annihilation", qrank(quotient.project(quotient.null_basis)) == 0)
    dependent_profile = qmatrix(((1, 2, 3), (2, 4, 6), (0, 0, 0)))
    dependent_quotient = FutureProfileQuotient.from_profile(dependent_profile)
    check(
        "quotient-dependent-rows-rank-normalized",
        dependent_quotient.coordinate_map.nrows == 1
        and dependent_quotient.quotient_dim == 1
        and dependent_quotient.nullity == 2,
    )
    zero_profile = QMatrix.zero(2, 3)
    zero_quotient = FutureProfileQuotient.from_profile(zero_profile)
    check(
        "quotient-zero-profile-rank-normalized",
        zero_quotient.coordinate_map.shape == (0, 3)
        and zero_quotient.section.shape == (3, 0)
        and zero_quotient.quotient_dim == 0
        and zero_quotient.nullity == 3,
    )
    check(
        "quotient-zero-profile-null-annihilation",
        qrank(zero_quotient.project(zero_quotient.null_basis)) == 0,
    )

    # The finite profile quotient is canonical even when every profile agrees;
    # it is not the same construction as a vector-space kernel quotient.
    constant_boundary = PredictiveBoundary.from_profiles(
        ("gamma", "alpha", "beta"),
        qmatrix(((1, 1, 1),)),
    )
    check(
        "predictive-boundary-canonical-label-order",
        constant_boundary.labels == ("alpha", "beta", "gamma"),
    )
    check(
        "predictive-boundary-duplicate-profile-merge",
        constant_boundary.classes == (("alpha", "beta", "gamma"),),
    )
    redundant_partition = boundary_partition_signature(
        constant_boundary,
        (("alpha",), ("beta", "gamma")),
    )
    check(
        "predictive-boundary-redundant-split",
        redundant_partition.mixed_profile_blocks == ()
        and redundant_partition.redundant_block_pairs == ((0, 1),),
    )
    varying_boundary = PredictiveBoundary.from_profiles(
        ("alpha", "beta"),
        qmatrix(((0, 1),)),
    )
    lossy_partition = boundary_partition_signature(
        varying_boundary,
        (("alpha", "beta"),),
    )
    check(
        "predictive-boundary-mixed-profile-block",
        lossy_partition.mixed_profile_blocks == (("alpha", "beta"),),
    )

    # Equal scalar profiles of regions need not form a Boolean congruence.
    # The four-element prefix subalgebra gives the exact context countercheck.
    regional_equivalence = regional_profile_equivalence(
        (
            RegionProfileEntry("empty", PrefixRegion.zero(), (Fraction(0),)),
            RegionProfileEntry("left", PrefixRegion.cylinder("0"), (Fraction(1, 2),)),
            RegionProfileEntry("right", PrefixRegion.cylinder("1"), (Fraction(1, 2),)),
            RegionProfileEntry("unit", PrefixRegion.one(), (Fraction(1),)),
        )
    )
    check(
        "regional-profile-equivalence-class",
        ("left", "right") in regional_equivalence.classes,
    )
    check(
        "regional-profile-not-automatic-meet-congruence",
        any(
            violation.left == "left"
            and violation.right == "right"
            and violation.context == "left"
            for violation in regional_equivalence.meet_violations
        ),
    )
    check(
        "regional-profile-closure-explicit",
        regional_equivalence.missing_closures == (),
    )

    # Stable-null iteration as a purely linear identity.
    dimensions = {"a": 2, "b": 2}
    observations = {
        "a": QMatrix.zero(0, 2),
        "b": qmatrix(((1, 0),)),
    }
    continuation = LinearContinuation("edge", "a", "b", QMatrix.identity(2))
    stable = compute_stable_null(dimensions, observations, (continuation,))
    check("stable-null-future-pullback", stable.boundary("a").quotient.quotient_dim == 1)
    check("stable-null-congruence", qrank(stable.continuation_residual(continuation)) == 0)

    # Typed boundary and cospan identities.
    incoming = BoundaryType("in", ("i",))
    shared = BoundaryType("shared", ("s",))
    outgoing = BoundaryType("out", ("o",))
    left_apex = RegionType("left-apex", ("li", "ls"))
    right_apex = RegionType("right-apex", ("ro", "rs"))
    left_cospan = StructuredCospan(
        "left",
        incoming,
        left_apex,
        shared,
        BoundaryLeg(incoming, left_apex, (("i", "li"),)),
        BoundaryLeg(shared, left_apex, (("s", "ls"),)),
    )
    right_cospan = StructuredCospan(
        "right",
        shared,
        right_apex,
        outgoing,
        BoundaryLeg(shared, right_apex, (("s", "rs"),)),
        BoundaryLeg(outgoing, right_apex, (("o", "ro"),)),
    )
    check("cospan-typed-legs", validate_cospan(left_cospan).issues == ())
    gluing = validate_gluing(left_cospan, right_cospan)
    check("cospan-common-boundary", gluing.issues == ())
    check("cospan-identification", gluing.apex_identifications == (("ls", "rs"),))
    wrong_shared = BoundaryType("wrong-shared", ("t",))
    mistyped_right = StructuredCospan(
        "mistyped-right",
        wrong_shared,
        right_apex,
        outgoing,
        BoundaryLeg(shared, right_apex, (("s", "rs"),)),
        BoundaryLeg(outgoing, right_apex, (("o", "ro"),)),
    )
    invalid_gluing = validate_gluing(left_cospan, mistyped_right)
    check(
        "cospan-validation-does-not-construct-invalid-gluing",
        "missing-common-boundary-comparison" in invalid_gluing.issues
        and "incoming-leg-source" in invalid_gluing.issues
        and invalid_gluing.apex_identifications == (),
    )

    # Raw comparison lifts can differ while their quotient action agrees.
    source_q = FutureProfileQuotient.from_profile(qmatrix(((1,),)))
    target_q = FutureProfileQuotient.from_profile(qmatrix(((1, 0),)))
    comparisons = comparison_family_invariants(
        source_q,
        target_q,
        (
            ComparisonCandidate("first", qmatrix(((1,), (0,)))),
            ComparisonCandidate("second", qmatrix(((1,), (1,)))),
        ),
    )
    check("comparison-raw-distinction", len(comparisons.raw_classes) == 2)
    check("comparison-quotient-identity", len(comparisons.quotient_classes) == 1)
    check("comparison-stable-descent", comparisons.non_descending == ())

    # Exterior equalizers and support residuals expose only exact invariants.
    exterior = (
        ExteriorProfilePair("x", qmatrix(((1, 0),)), qmatrix(((0, 0),))),
    )
    dynamic = dynamic_invariant_subspace(2, exterior)
    kinematic = qmatrix(((0,), (1,)))
    locality = locality_signature(kinematic, dynamic)
    check("dynamic-equalizer-rank", locality.dynamic_rank == 1)
    check(
        "locality-residual-zero",
        locality.kinematic_outside_dynamic_rank == 0
        and locality.dynamic_outside_kinematic_rank == 0,
    )
    regional_locality = regional_support_locality_signature(
        PrefixRegion.cylinder("0"),
        (
            SupportedInternalAction(
                "inside",
                PrefixRegion.cylinder("00"),
                qmatrix(((0,), (1,))),
            ),
            SupportedInternalAction(
                "outside",
                PrefixRegion.cylinder("1"),
                qmatrix(((1,), (0,))),
            ),
        ),
        (
            SupportedExteriorReplacement(
                "complement-replacement",
                PrefixRegion.cylinder("1"),
                qmatrix(((1, 0),)),
                qmatrix(((0, 0),)),
            ),
            SupportedExteriorReplacement(
                "internal-replacement",
                PrefixRegion.cylinder("00"),
                qmatrix(((0, 1),)),
                qmatrix(((0, 0),)),
            ),
        ),
        ambient_dim=2,
    )
    check(
        "regional-locality-independent-support-selection",
        regional_locality.internal_action_names == ("inside",)
        and regional_locality.exterior_replacement_names
        == ("complement-replacement",),
    )
    check(
        "regional-locality-common-ambient-equality",
        regional_locality.common_ambient_signature.kinematic_outside_dynamic_rank == 0
        and regional_locality.common_ambient_signature.dynamic_outside_kinematic_rank == 0,
    )

    zero_region = PrefixRegion.zero()
    left_region = PrefixRegion.cylinder("0")
    right_region = PrefixRegion.cylinder("1")
    whole_region = PrefixRegion.one()
    support = support_faithfulness_signature(
        (
            SupportEntry("zero", zero_region, QMatrix.zero(2, 0)),
            SupportEntry("left", left_region, qmatrix(((1,), (0,)))),
            SupportEntry("right", right_region, qmatrix(((0,), (1,)))),
            SupportEntry("whole", whole_region, QMatrix.identity(2)),
        ),
        ambient_dim=2,
    )
    check("support-order-residuals", support.order_preservation_residuals == ())
    check(
        "support-lattice-residuals",
        all(
            item.expected_outside_constructed_rank == 0
            and item.constructed_outside_expected_rank == 0
            for item in support.lattice_residuals
        ),
    )

    payload: dict[str, object] = {
        "schema": "apr-core-selftest-v1",
        "scope": "generic exact algebraic identities only",
        "test_count": len(tests),
        "tests": tuple(tests),
        "representations": {
            "prefix_words_are_ontic": False,
            "finite_matrices_are_ontic": False,
            "global_tick_used": False,
        },
    }
    payload["payload_sha256"] = canonical_sha256(payload)
    return payload


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="APR generic exact core; import as a library or run algebraic self-tests",
        allow_abbrev=False,
    )
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)
    if not args.selftest:
        parser.error("the only executable mode is --selftest")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    parse_args(sys.argv[1:] if argv is None else argv)
    try:
        payload = run_selftests()
    except (AssertionError, KeyError, TypeError, ValueError, ZeroDivisionError) as exc:
        print(f"APR-CORE-SELFTEST-REFUSED {exc}", file=sys.stderr)
        return 1
    sys.stdout.write(canonical_json(payload) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
