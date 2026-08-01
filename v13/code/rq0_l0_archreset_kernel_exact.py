#!/usr/bin/env python3
"""Small shared exact-arithmetic kernel for the public L0 architecture reset.

This module contains no estimator, certificate predicate, regional object,
fixture truth, outcome resolver, or scientific label.  The public proposer
and the independent trusted verifier may share only these exact arithmetic
primitives.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Dict, Iterable, Mapping, Sequence, Tuple

try:
    from .rq0_l0_addressability_estimator_exact import (
        AlgebraBasis,
        INV_SQRT2,
        Matrix,
        ONE,
        Q24,
        Vector,
        ZERO,
        ZETA,
        adjoint,
        algebra_from_matrices,
        algebra_intersection_dimension,
        basis_vector,
        flatten,
        identity,
        inner,
        is_projector,
        is_unitary,
        is_zero_matrix,
        madd,
        matrices_commute,
        matrix,
        mmul,
        mscale,
        msub,
        mv,
        shape,
        vector,
        zero_matrix,
    )
except ImportError:
    from rq0_l0_addressability_estimator_exact import (
        AlgebraBasis,
        INV_SQRT2,
        Matrix,
        ONE,
        Q24,
        Vector,
        ZERO,
        ZETA,
        adjoint,
        algebra_from_matrices,
        algebra_intersection_dimension,
        basis_vector,
        flatten,
        identity,
        inner,
        is_projector,
        is_unitary,
        is_zero_matrix,
        madd,
        matrices_commute,
        matrix,
        mmul,
        mscale,
        msub,
        mv,
        shape,
        vector,
        zero_matrix,
    )


PHASE_MODULUS = 24


@dataclass(frozen=True)
class MonomialLaw:
    """Exact |j> -> zeta_24^phase[j] |permutation[j]> law."""

    permutation: Tuple[int, ...]
    phases: Tuple[int, ...]

    def __post_init__(self) -> None:
        dimension = len(self.permutation)
        if dimension < 1 or len(self.phases) != dimension:
            raise ValueError("monomial law has inconsistent dimension")
        if tuple(sorted(self.permutation)) != tuple(range(dimension)):
            raise ValueError("monomial permutation is not bijective")
        if any(type(value) is not int or not 0 <= value < PHASE_MODULUS for value in self.phases):
            raise ValueError("monomial phase is not a canonical integer exponent")

    @property
    def dimension(self) -> int:
        return len(self.permutation)

    @classmethod
    def unit(cls, dimension: int) -> "MonomialLaw":
        if type(dimension) is not int or dimension < 1:
            raise ValueError("unit law dimension must be a positive exact integer")
        return cls(tuple(range(dimension)), (0,) * dimension)

    def after(self, right: "MonomialLaw") -> "MonomialLaw":
        if self.dimension != right.dimension:
            raise ValueError("cannot compose laws on different carriers")
        return MonomialLaw(
            tuple(self.permutation[right.permutation[index]] for index in range(self.dimension)),
            tuple(
                (right.phases[index] + self.phases[right.permutation[index]])
                % PHASE_MODULUS
                for index in range(self.dimension)
            ),
        )

    def inverse(self) -> "MonomialLaw":
        permutation = [0] * self.dimension
        phases = [0] * self.dimension
        for source, target in enumerate(self.permutation):
            permutation[target] = source
            phases[target] = (-self.phases[source]) % PHASE_MODULUS
        return MonomialLaw(tuple(permutation), tuple(phases))

    def conjugated(self, action: "MonomialLaw") -> "MonomialLaw":
        return action.after(self).after(action.inverse())

    def signature(self) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
        anchor = self.phases[0]
        return self.permutation, tuple(
            (value - anchor) % PHASE_MODULUS for value in self.phases
        )

    def global_phase_equivalent(self, other: "MonomialLaw") -> bool:
        return (
            self.dimension == other.dimension
            and self.permutation == other.permutation
            and len(
                {
                    (left - right) % PHASE_MODULUS
                    for left, right in zip(self.phases, other.phases)
                }
            )
            == 1
        )

    def to_matrix(self) -> Matrix:
        rows = [[ZERO for _ in range(self.dimension)] for _ in range(self.dimension)]
        for source, target in enumerate(self.permutation):
            rows[target][source] = ZETA ** self.phases[source]
        return tuple(tuple(row) for row in rows)

    def to_raw(self) -> Mapping[str, object]:
        return {
            "permutation": list(self.permutation),
            "phases": list(self.phases),
        }


def permutation_law(permutation: Sequence[int]) -> MonomialLaw:
    return MonomialLaw(tuple(permutation), (0,) * len(permutation))


def q24_to_raw(value: Q24) -> list[list[int]]:
    return [[entry.numerator, entry.denominator] for entry in value.coefficients]


def matrix_to_raw(value: Matrix) -> list[list[list[list[int]]]]:
    return [[q24_to_raw(entry) for entry in row] for row in value]


def vector_to_raw(value: Vector) -> list[list[list[int]]]:
    return [q24_to_raw(entry) for entry in value]


def rank_one_projector(state: Vector) -> Matrix:
    return tuple(
        tuple(left * right.conjugate() for right in state)
        for left in state
    )


def tensor_monomial(laws: Sequence[MonomialLaw]) -> MonomialLaw:
    dimensions = tuple(value.dimension for value in laws)
    total = 1
    for dimension in dimensions:
        total *= dimension

    def decode(index: int) -> Tuple[int, ...]:
        result = []
        current = index
        for dimension in reversed(dimensions):
            result.append(current % dimension)
            current //= dimension
        return tuple(reversed(result))

    def encode(values: Sequence[int]) -> int:
        result = 0
        for value, dimension in zip(values, dimensions):
            result = result * dimension + value
        return result

    permutation = []
    phases = []
    for index in range(total):
        coordinates = decode(index)
        permutation.append(
            encode(
                tuple(
                    law.permutation[coordinate]
                    for law, coordinate in zip(laws, coordinates)
                )
            )
        )
        phases.append(
            sum(
                law.phases[coordinate]
                for law, coordinate in zip(laws, coordinates)
            )
            % PHASE_MODULUS
        )
    return MonomialLaw(tuple(permutation), tuple(phases))


def conjugate_dense(action: MonomialLaw, value: Matrix) -> Matrix:
    unitary = action.to_matrix()
    return mmul(mmul(unitary, value), adjoint(unitary))


def map_projector_atoms(
    action: MonomialLaw,
    atoms: Sequence[frozenset[int]],
) -> Tuple[frozenset[int], ...]:
    return tuple(
        frozenset(action.permutation[index] for index in atom)
        for atom in atoms
    )


def represented_algebra(laws: Iterable[MonomialLaw], dimension: int) -> AlgebraBasis:
    return algebra_from_matrices((law.to_matrix() for law in laws), dimension)


SparseLawVector = Tuple[Tuple[int, Q24], ...]


def _canonical_laws(laws: Iterable[MonomialLaw]) -> Tuple[MonomialLaw, ...]:
    values = tuple(laws)
    if values and len({value.dimension for value in values}) != 1:
        raise ValueError("represented laws have inconsistent carriers")
    return tuple(sorted(set(values), key=lambda value: (value.permutation, value.phases)))


def monomial_sparse_vector(law: MonomialLaw) -> SparseLawVector:
    """Return the exact nonzero entries of the dense flattened law."""

    return tuple(
        sorted(
            (
                law.permutation[source] * law.dimension + source,
                ZETA ** law.phases[source],
            )
            for source in range(law.dimension)
        )
    )


@lru_cache(maxsize=None)
def _monomial_span_basis_cached(
    laws: Tuple[MonomialLaw, ...],
) -> Tuple[SparseLawVector, ...]:
    """Exact sparse Gaussian basis for the span of monomial matrices."""

    pivots: Dict[int, Dict[int, Q24]] = {}
    for law in laws:
        row = dict(monomial_sparse_vector(law))
        while row:
            pivot = min(row)
            if pivot not in pivots:
                inverse = ONE / row[pivot]
                normalized = {
                    index: value * inverse
                    for index, value in row.items()
                    if value * inverse
                }
                pivots[pivot] = normalized
                break
            scale = row[pivot]
            basis = pivots[pivot]
            for index, value in basis.items():
                updated = row.get(index, ZERO) - scale * value
                if updated:
                    row[index] = updated
                else:
                    row.pop(index, None)
    return tuple(
        tuple(sorted(pivots[pivot].items()))
        for pivot in sorted(pivots)
    )


def monomial_span_basis(laws: Iterable[MonomialLaw]) -> Tuple[SparseLawVector, ...]:
    return _monomial_span_basis_cached(_canonical_laws(laws))


def monomial_span_dimension(laws: Iterable[MonomialLaw]) -> int:
    return len(monomial_span_basis(laws))


def monomial_span_intersection_dimension(
    left: Iterable[MonomialLaw],
    right: Iterable[MonomialLaw],
) -> int:
    left_values = _canonical_laws(left)
    right_values = _canonical_laws(right)
    return (
        len(_monomial_span_basis_cached(left_values))
        + len(_monomial_span_basis_cached(right_values))
        - len(_monomial_span_basis_cached(_canonical_laws(left_values + right_values)))
    )


__all__ = [
    "AlgebraBasis",
    "Fraction",
    "INV_SQRT2",
    "Matrix",
    "MonomialLaw",
    "ONE",
    "PHASE_MODULUS",
    "Q24",
    "Vector",
    "ZERO",
    "ZETA",
    "adjoint",
    "algebra_from_matrices",
    "algebra_intersection_dimension",
    "basis_vector",
    "conjugate_dense",
    "flatten",
    "identity",
    "inner",
    "is_projector",
    "is_unitary",
    "is_zero_matrix",
    "madd",
    "map_projector_atoms",
    "matrices_commute",
    "matrix",
    "matrix_to_raw",
    "mmul",
    "mscale",
    "msub",
    "mv",
    "permutation_law",
    "q24_to_raw",
    "rank_one_projector",
    "represented_algebra",
    "monomial_sparse_vector",
    "monomial_span_basis",
    "monomial_span_dimension",
    "monomial_span_intersection_dimension",
    "shape",
    "tensor_monomial",
    "vector",
    "vector_to_raw",
    "zero_matrix",
]
