#!/usr/bin/env python3
"""Generic pre-fixture estimator for RQ0-L0 computational certification.

This module is generic.  It imports the immutable exact finite composition,
Q(zeta_24), W3, and serialization layer as antecedent lemmas.  It does not
import any public performance fixture or future held-out fixture.

The new work is:

* a sparse exact represented-algebra span with canonical subobject caching;
* cheap-predicate-first factor certification and deterministic counters;
* complete regional row/context arrows and projector/Boolean fact maps;
* full-instrument twisted-triple controls;
* one total outcome resolver.

This source confers no scientific status by itself.  The public qualification,
freeze chronology, one held-out score, and hostile review remain mandatory.
"""

from __future__ import annotations

import dataclasses
import hashlib
import itertools
import json
import time
from dataclasses import dataclass, field
from typing import Callable, Dict, FrozenSet, Iterable, Mapping, Optional, Sequence, Tuple

try:  # package import
    from . import rq0_l0_certification_estimator_exact as legacy
except ImportError:  # direct execution/import from v13/code
    import rq0_l0_certification_estimator_exact as legacy


ESTIMATOR_API_VERSION = "rq0-l0-computational-certification-frozen-api-v1"
PIN_PATH = "v13/note-rq0-operational-localization-computational-certification-pin.md"

SCIENTIFIC_OUTCOMES = frozenset(
    (
        "RQ0-LOCALIZATION-GROUPOID",
        "RQ0-LOCAL-ATLAS",
        "RQ0-L0-BLOCKED-AT-ADDRESS",
        "RQ0-L0-BLOCKED-AT-REGIONAL-MAPS",
    )
)
PROCEDURAL_OUTCOME = "RQ0-L0-INVALID"


class RuntimeCapExceeded(RuntimeError):
    """Registered wall/search cap was exhausted; never a scientific no-go."""


class RegionalMapFailure(RuntimeError):
    """Address factors returned, but mandatory regional/fact maps failed."""


def _stable(value: object) -> str:
    return legacy.stable_hash(legacy.normalize(value))


# ---------------------------------------------------------------------------
# Deterministic instrumentation and sparse exact represented algebras
# ---------------------------------------------------------------------------


@dataclass
class Instrumentation:
    counters: Dict[str, int] = field(default_factory=dict)
    phase_seconds: Dict[str, float] = field(default_factory=dict)
    progress: list[Mapping[str, object]] = field(default_factory=list)

    def increment(self, key: str, amount: int = 1) -> None:
        self.counters[key] = self.counters.get(key, 0) + amount

    def timed(self, key: str):
        instrumentation = self

        class _Timer:
            def __enter__(self):
                self.started = time.monotonic()
                return self

            def __exit__(self, exc_type, exc, traceback):
                instrumentation.phase_seconds[key] = (
                    instrumentation.phase_seconds.get(key, 0.0)
                    + time.monotonic()
                    - self.started
                )
                return False

        return _Timer()

    def mark(self, phase: str, **values: object) -> None:
        self.progress.append({"phase": phase, **values})

    def canonical(self) -> Mapping[str, object]:
        return {
            "counters": dict(sorted(self.counters.items())),
            "progress": [dict(sorted(value.items())) for value in self.progress],
        }

    def timing(self) -> Mapping[str, float]:
        return {key: self.phase_seconds[key] for key in sorted(self.phase_seconds)}


SparseVector = Dict[int, legacy.Q24]


@dataclass(frozen=True)
class SparseAlgebra:
    subobject: FrozenSet[int]
    # Deterministic normalized row-echelon vectors.
    basis: Tuple[Tuple[Tuple[int, legacy.Q24], ...], ...]

    @property
    def dimension(self) -> int:
        return len(self.basis)


def _law_sparse_vector(law: legacy.MonomialLaw) -> SparseVector:
    dimension = law.dimension
    return {
        target * dimension + source: legacy.ZETA ** law.phases[source]
        for source, target in enumerate(law.permutation)
    }


def _basis_to_vectors(
    basis: Sequence[Tuple[Tuple[int, legacy.Q24], ...]],
) -> Tuple[SparseVector, ...]:
    return tuple(dict(value) for value in basis)


def _sparse_span_basis(vectors: Iterable[Mapping[int, legacy.Q24]]) -> Tuple[Tuple[Tuple[int, legacy.Q24], ...], ...]:
    pivots: Dict[int, SparseVector] = {}
    for original in vectors:
        value = {index: coefficient for index, coefficient in original.items() if coefficient}
        while value:
            pivot = min(value)
            if pivot not in pivots:
                normalizer = value[pivot]
                value = {
                    index: coefficient / normalizer
                    for index, coefficient in value.items()
                    if coefficient
                }
                pivots[pivot] = value
                break
            factor = value[pivot]
            row = pivots[pivot]
            for index, coefficient in row.items():
                updated = value.get(index, legacy.Q24(0)) - factor * coefficient
                if updated:
                    value[index] = updated
                elif index in value:
                    del value[index]
    return tuple(
        tuple(sorted(pivots[pivot].items()))
        for pivot in sorted(pivots)
    )


def sparse_intersection_dimension(left: SparseAlgebra, right: SparseAlgebra) -> int:
    union = _sparse_span_basis(
        itertools.chain(_basis_to_vectors(left.basis), _basis_to_vectors(right.basis))
    )
    return left.dimension + right.dimension - len(union)


class ExactAlgebraCache:
    """One exact cache per dataset; keys are quotient subobjects, never handles."""

    def __init__(
        self,
        composition: legacy.CompositionObject,
        instrumentation: Instrumentation,
    ) -> None:
        self.composition = composition
        self.instrumentation = instrumentation
        self._law_vectors: Dict[legacy.MonomialLaw, Mapping[int, legacy.Q24]] = {}
        self._dense_matrices: Dict[legacy.MonomialLaw, legacy.Matrix] = {}
        self._algebras: Dict[FrozenSet[int], SparseAlgebra] = {}
        self._ambient = frozenset(range(composition.size))

    @staticmethod
    def key(elements: Iterable[int]) -> FrozenSet[int]:
        return frozenset(int(value) for value in elements)

    def law_vector(self, law: legacy.MonomialLaw) -> Mapping[int, legacy.Q24]:
        if law in self._law_vectors:
            self.instrumentation.increment("sparse_law_vector_cache_hits")
            return self._law_vectors[law]
        self.instrumentation.increment("sparse_law_vector_cache_misses")
        value = _law_sparse_vector(law)
        self._law_vectors[law] = value
        return value

    def dense_matrix(self, law: legacy.MonomialLaw) -> legacy.Matrix:
        if law in self._dense_matrices:
            self.instrumentation.increment("dense_matrix_cache_hits")
            return self._dense_matrices[law]
        self.instrumentation.increment("dense_matrix_cache_misses")
        value = law.to_matrix()
        self._dense_matrices[law] = value
        return value

    def algebra(self, elements: Iterable[int]) -> SparseAlgebra:
        key = self.key(elements)
        if key in self._algebras:
            self.instrumentation.increment("represented_algebra_cache_hits")
            return self._algebras[key]
        self.instrumentation.increment("represented_algebra_cache_misses")
        if key == self._ambient:
            self.instrumentation.increment("ambient_represented_algebra_builds")
        else:
            self.instrumentation.increment("factor_represented_algebra_builds")
            fingerprint = _stable(tuple(sorted(key)))
            self.instrumentation.increment(f"factor_algebra_build::{fingerprint}")
        basis = _sparse_span_basis(
            self.law_vector(self.composition.classes[index].law)
            for index in sorted(key)
        )
        result = SparseAlgebra(key, basis)
        self._algebras[key] = result
        return result

    def ambient(self) -> SparseAlgebra:
        return self.algebra(self._ambient)

    def exact_matrices_commute(self, left: int, right: int) -> bool:
        # Exact MonomialLaw composition is the same predicate as dense mmul
        # equality but avoids conversion and dense multiplication.
        left_law = self.composition.classes[left].law
        right_law = self.composition.classes[right].law
        self.instrumentation.increment("exact_monomial_commutation_tests")
        return left_law.after(right_law) == right_law.after(left_law)


def dense_sparse_equivalent(
    composition: legacy.CompositionObject,
    subobject: Iterable[int],
    carrier_dimension: int,
    cache: ExactAlgebraCache,
) -> bool:
    key = frozenset(subobject)
    sparse = cache.algebra(key)
    dense = legacy.algebra_from_matrices(
        (
            cache.dense_matrix(composition.classes[index].law)
            for index in sorted(key)
        ),
        carrier_dimension,
    )
    dense_vectors = tuple(
        {
            index: coefficient
            for index, coefficient in enumerate(vector)
            if coefficient
        }
        for vector in dense.vectors
    )
    union = _sparse_span_basis(
        itertools.chain(_basis_to_vectors(sparse.basis), dense_vectors)
    )
    return (
        sparse.dimension == dense.dimension
        and len(union) == sparse.dimension
    )


# ---------------------------------------------------------------------------
# Cheap-first, cached factor certification
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AnalysisRun:
    result: legacy.AddressabilityResult
    instrumentation: Instrumentation
    algebra_cache: ExactAlgebraCache


def _empty_certificate(
    factors: Tuple[FrozenSet[int], ...],
    **overrides: object,
) -> legacy.FactorCertificate:
    values: Dict[str, object] = {
        "factors": factors,
        "factor_orders": tuple(len(value) for value in factors),
        "algebra_dimensions": (),
        "independently_generated": False,
        "mixed_implemented_both_orders": False,
        "operationally_commuting": False,
        "faithful_multiplication": False,
        "multiplication_collision": None,
        "closed_with_inverses": False,
        "typed_scalar_intersection": False,
        "represented_algebra_product": False,
        "restriction_stable": False,
    }
    values.update(overrides)
    return legacy.FactorCertificate(**values)


def certify_factor_tuple(
    dataset: legacy.OperationalDataset,
    composition: legacy.CompositionObject,
    factors: Sequence[FrozenSet[int]],
    inverses: Sequence[int],
    cache: ExactAlgebraCache,
) -> legacy.FactorCertificate:
    factors = tuple(frozenset(value) for value in factors)
    cache.instrumentation.increment("factor_certificates_started")

    independent = all(
        legacy.subgroup_generated(
            composition,
            (
                entry
                for entry in factor
                if composition.classes[entry].independently_selectable
            ),
            inverses,
        )
        == factor
        for factor in factors
    )
    if not independent:
        cache.instrumentation.increment("cheap_reject_independent_generation")
        return _empty_certificate(factors)

    mixed = all(
        composition.row(a, b).status == legacy.IMPLEMENTED
        and composition.row(b, a).status == legacy.IMPLEMENTED
        for left, right in itertools.combinations(factors, 2)
        for a in left
        for b in right
    )
    if not mixed:
        cache.instrumentation.increment("cheap_reject_mixed_implementation")
        return _empty_certificate(factors, independently_generated=True)

    operationally_commuting = all(
        legacy.subobjects_commute(composition, left, right)
        for left, right in itertools.combinations(factors, 2)
    )
    if not operationally_commuting:
        cache.instrumentation.increment("cheap_reject_operational_commutation")
        return _empty_certificate(
            factors,
            independently_generated=True,
            mixed_implemented_both_orders=True,
        )

    image, collision = legacy.multiplication_image(composition, factors)
    faithful = collision is None and len(image) == composition.size
    if not faithful:
        cache.instrumentation.increment("cheap_reject_multiplication_faithfulness")
        return _empty_certificate(
            factors,
            independently_generated=True,
            mixed_implemented_both_orders=True,
            operationally_commuting=True,
            multiplication_collision=collision,
        )

    closed = all(
        legacy._closed_and_inverse(composition, factor, inverses)
        for factor in factors
    )
    if not closed:
        cache.instrumentation.increment("cheap_reject_closure")
        return _empty_certificate(
            factors,
            independently_generated=True,
            mixed_implemented_both_orders=True,
            operationally_commuting=True,
            faithful_multiplication=True,
        )

    identity = composition.identity
    scalar_intersection = identity is not None and all(
        left & right == frozenset((identity,))
        for left, right in itertools.combinations(factors, 2)
    )
    if not scalar_intersection:
        cache.instrumentation.increment("cheap_reject_typed_intersection")
        return _empty_certificate(
            factors,
            independently_generated=True,
            mixed_implemented_both_orders=True,
            operationally_commuting=True,
            faithful_multiplication=True,
            closed_with_inverses=True,
        )

    restriction_stable = legacy._restriction_stable(composition, factors, inverses)
    if not restriction_stable:
        cache.instrumentation.increment("cheap_reject_restriction_stability")
        return _empty_certificate(
            factors,
            independently_generated=True,
            mixed_implemented_both_orders=True,
            operationally_commuting=True,
            faithful_multiplication=True,
            closed_with_inverses=True,
            typed_scalar_intersection=True,
        )

    # Only candidates surviving every group/row predicate reach exact
    # represented-algebra construction.
    factor_algebras = tuple(cache.algebra(factor) for factor in factors)
    ambient = cache.ambient()
    algebra_dimensions = tuple(value.dimension for value in factor_algebras)
    intersections = all(
        sparse_intersection_dimension(left, right) == 1
        for left, right in itertools.combinations(factor_algebras, 2)
    )
    exact_commutation = all(
        cache.exact_matrices_commute(a, b)
        for left, right in itertools.combinations(factors, 2)
        for a in left
        for b in right
    )
    dimension_product = 1
    for dimension in algebra_dimensions:
        dimension_product *= dimension
    represented_product = (
        intersections
        and exact_commutation
        and dimension_product == ambient.dimension
    )
    if not represented_product:
        cache.instrumentation.increment("represented_algebra_rejections")
    else:
        cache.instrumentation.increment("factor_certificates_passed")
    return legacy.FactorCertificate(
        factors=factors,
        factor_orders=tuple(len(value) for value in factors),
        algebra_dimensions=algebra_dimensions,
        independently_generated=True,
        mixed_implemented_both_orders=True,
        operationally_commuting=True,
        faithful_multiplication=True,
        multiplication_collision=None,
        closed_with_inverses=True,
        typed_scalar_intersection=True,
        represented_algebra_product=represented_product,
        restriction_stable=True,
    )


def analyze_addressability(
    dataset: legacy.OperationalDataset,
    *,
    deadline: Optional[float] = None,
    progress: Optional[Callable[[Mapping[str, object]], None]] = None,
) -> AnalysisRun:
    instrumentation = Instrumentation()

    def check_deadline() -> None:
        if deadline is not None and time.monotonic() > deadline:
            raise RuntimeCapExceeded("addressability exceeded the registered deadline")

    def mark(phase: str, **values: object) -> None:
        instrumentation.mark(phase, **values)
        if progress is not None:
            progress(instrumentation.progress[-1])

    with instrumentation.timed("composition_validation"):
        composition = legacy.build_composition_object(dataset)
    cache = ExactAlgebraCache(composition, instrumentation)
    mark("composition-validated", classes=composition.size, rows=len(composition.rows))
    check_deadline()

    if not composition.total_implemented:
        obstruction = (
            "declared COLLAPSED status"
            if composition.row_audit.collapsed_rows
            else "unavailable composition row"
        )
        return AnalysisRun(
            legacy.AddressabilityResult(
                composition, (), (), (), (), 0, 0, obstruction
            ),
            instrumentation,
            cache,
        )
    if composition.identity is None:
        return AnalysisRun(
            legacy.AddressabilityResult(
                composition, (), (), (), (), 0, 0, "no unique identity"
            ),
            instrumentation,
            cache,
        )
    if not composition.associative:
        return AnalysisRun(
            legacy.AddressabilityResult(
                composition,
                (),
                (),
                (),
                (),
                0,
                0,
                "nonassociative quotient composition",
            ),
            instrumentation,
            cache,
        )

    try:
        inverses = legacy.inverse_table(composition)
    except legacy.AccessUnderdetermined as error:
        return AnalysisRun(
            legacy.AddressabilityResult(
                composition, (), (), (), (), 0, 0, str(error)
            ),
            instrumentation,
            cache,
        )

    with instrumentation.timed("normal_subobjects"):
        normals, join_tests = legacy.enumerate_normal_subobjects(
            composition, inverses
        )
    mark("normal-subobjects", count=len(normals), join_tests=join_tests)
    check_deadline()

    identity_subobject = frozenset((composition.identity,))
    proper = tuple(
        value
        for value in normals
        if value != identity_subobject and len(value) != composition.size
    )
    direct_pool = set()
    factor_tests = 0
    with instrumentation.timed("direct_complements"):
        for index, left in enumerate(proper):
            for right in proper[index + 1 :]:
                if len(left) * len(right) != composition.size:
                    continue
                factor_tests += 1
                instrumentation.increment("direct_complement_candidates")
                if join_tests + factor_tests > legacy.MAX_CANDIDATE_TESTS:
                    raise RuntimeCapExceeded(
                        "direct-complement search exceeded the registered cap"
                    )
                if left & right != identity_subobject:
                    continue
                if not legacy.subobjects_commute(composition, left, right):
                    continue
                image, collision = legacy.multiplication_image(
                    composition, (left, right)
                )
                if collision is None and len(image) == composition.size:
                    direct_pool.add(left)
                    direct_pool.add(right)
            check_deadline()
    pool = tuple(
        sorted(direct_pool, key=lambda item: (len(item), tuple(sorted(item))))
    )
    mark("direct-pool", count=len(pool), tests=factor_tests)

    certificates = []

    # Exhaustive divisibility-pruned tuple enumeration.  A member of a sound
    # tuple is independently generated and closed, and every pair has scalar
    # intersection and commutes.  Applying those necessary predicates while
    # extending a tuple cannot remove a positive certificate.  The order
    # product must divide the ambient order at every prefix.
    independently_generated: Dict[FrozenSet[int], bool] = {}
    closed_factor: Dict[FrozenSet[int], bool] = {}
    for factor in pool:
        independently_generated[factor] = (
            legacy.subgroup_generated(
                composition,
                (
                    entry
                    for entry in factor
                    if composition.classes[entry].independently_selectable
                ),
                inverses,
            )
            == factor
        )
        closed_factor[factor] = legacy._closed_and_inverse(
            composition, factor, inverses
        )
    eligible_pool = tuple(
        factor
        for factor in pool
        if independently_generated[factor] and closed_factor[factor]
    )
    instrumentation.counters["eligible_direct_pool"] = len(eligible_pool)
    pair_cache: Dict[Tuple[int, int], bool] = {}
    search_nodes = 0

    def pair_is_eligible(left_index: int, right_index: int) -> bool:
        key = (min(left_index, right_index), max(left_index, right_index))
        if key not in pair_cache:
            left = eligible_pool[key[0]]
            right = eligible_pool[key[1]]
            pair_cache[key] = (
                left & right == identity_subobject
                and legacy.subobjects_commute(composition, left, right)
            )
            instrumentation.increment("factor_pair_cheap_tests")
        return pair_cache[key]

    def candidate_tuples(
        start: int,
        chosen_indices: Tuple[int, ...],
        order_product: int,
    ):
        nonlocal search_nodes
        if len(chosen_indices) >= 2 and order_product == composition.size:
            yield tuple(eligible_pool[index] for index in chosen_indices)
            return
        if len(chosen_indices) >= 8 or order_product >= composition.size:
            return
        for index in range(start, len(eligible_pool)):
            search_nodes += 1
            instrumentation.increment("factor_tuple_search_nodes")
            if join_tests + factor_tests + search_nodes > legacy.MAX_CANDIDATE_TESTS:
                raise RuntimeCapExceeded(
                    "factor-tuple search exceeded the registered cap"
                )
            factor = eligible_pool[index]
            new_product = order_product * len(factor)
            if new_product > composition.size or composition.size % new_product:
                continue
            if any(not pair_is_eligible(previous, index) for previous in chosen_indices):
                continue
            check_deadline()
            yield from candidate_tuples(
                index + 1,
                chosen_indices + (index,),
                new_product,
            )

    with instrumentation.timed("factor_certification"):
        for factors in candidate_tuples(0, (), 1):
            factor_tests += 1
            instrumentation.increment("factor_tuple_candidates")
            certificate = certify_factor_tuple(
                dataset, composition, factors, inverses, cache
            )
            if certificate.passes:
                certificates.append(certificate)
            check_deadline()
    certificates = sorted(set(certificates), key=legacy.certificate_sort_key)
    maximum = max((len(value.factors) for value in certificates), default=0)
    finest = tuple(
        value for value in certificates if len(value.factors) == maximum
    )
    obstruction = None
    if not finest:
        selectable = frozenset(
            value.index
            for value in composition.classes
            if value.independently_selectable
        )
        obstruction = (
            "no complete factor tuple is independently generated"
            if selectable != frozenset(range(composition.size))
            else "no sound normal direct-factor tuple"
        )

    with instrumentation.timed("certificate_replay"):
        for certificate in finest:
            replay = certify_factor_tuple(
                dataset,
                composition,
                certificate.factors,
                inverses,
                cache,
            )
            if replay != certificate or not replay.passes:
                raise AssertionError(
                    "returned factor certificate failed cached exact replay"
                )
    mark(
        "addressability-complete",
        certificates=len(certificates),
        finest=len(finest),
        factor_tuple_tests=factor_tests,
    )
    return AnalysisRun(
        legacy.AddressabilityResult(
            composition=composition,
            inverses=inverses,
            normal_subobjects=normals,
            certificates=tuple(certificates),
            finest_certificates=finest,
            normal_join_tests=join_tests,
            factor_tuple_tests=factor_tests,
            first_obstruction=obstruction,
        ),
        instrumentation,
        cache,
    )


# ---------------------------------------------------------------------------
# Complete regional arrows and exact fact descent
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FullRowMap:
    source_left: int
    source_right: int
    target_left: int
    target_right: int
    source_tau: str
    target_tau: str
    source_status: str
    target_status: str
    source_result: int
    target_result: int
    source_law: legacy.MonomialLaw
    target_law: legacy.MonomialLaw
    source_signature: Tuple[Tuple[int, ...], Tuple[int, ...]]
    target_signature: Tuple[Tuple[int, ...], Tuple[int, ...]]


@dataclass(frozen=True)
class ExactFieldMap:
    source_key: str
    target_key: str
    source_payload: object
    target_payload: object


@dataclass(frozen=True)
class ExactRecordPayload:
    structural_id: str
    support: FrozenSet[int]
    projector_resolution: Tuple[FrozenSet[int], ...]
    candidate_structure: Tuple[object, ...]
    passes_w3: bool


@dataclass(frozen=True)
class ExactRecordMap:
    source: ExactRecordPayload
    target: ExactRecordPayload


@dataclass(frozen=True)
class ExecutableContextMap:
    source_operations: FrozenSet[int]
    target_operations: FrozenSet[int]
    operation_map: Tuple[Tuple[int, int], ...]
    source_preparations: FrozenSet[str]
    target_preparations: FrozenSet[str]
    source_probes: FrozenSet[str]
    target_probes: FrozenSet[str]
    source_readouts: FrozenSet[str]
    target_readouts: FrozenSet[str]
    source_records: FrozenSet[str]
    target_records: FrozenSet[str]
    source_gauges: FrozenSet[str]
    target_gauges: FrozenSet[str]


@dataclass(frozen=True)
class FullRegionalArrow:
    source: str
    target: str
    operation_map: Tuple[Tuple[int, int], ...]
    row_map: Tuple[FullRowMap, ...]
    selectability_map: Tuple[Tuple[int, int, bool, bool], ...]
    preparation_maps: Tuple[ExactFieldMap, ...]
    context_map: ExecutableContextMap
    probe_maps: Tuple[ExactFieldMap, ...]
    readout_maps: Tuple[ExactFieldMap, ...]
    record_maps: Tuple[ExactRecordMap, ...]
    gauge_maps: Tuple[ExactFieldMap, ...]


@dataclass(frozen=True)
class FullRegionalAtlas:
    factorization: legacy.FactorCertificate
    contexts: Tuple[legacy.ContextView, ...]
    objects: Tuple[legacy.RegionalObject, ...]
    arrows: Tuple[FullRegionalArrow, ...]
    facts: Tuple[legacy.FactInterface, ...]
    fact_maps: Tuple[legacy.FactMap, ...]
    coherent_regional_paths: int
    coherent_fact_paths: int
    nonvacuous_triples: Tuple[Tuple[str, str, str, str], ...]
    universal_atoms: Tuple[int, ...]
    is_complete_proper_boolean: bool


def _payload_lookups(dataset: legacy.OperationalDataset) -> Mapping[str, Mapping[str, object]]:
    prep_keys, probe_keys, readout_keys, gauge_keys = legacy._key_maps(dataset)
    return {
        "preparation": {
            prep_keys[value.handle]: value for value in dataset.preparations
        },
        "probe": {probe_keys[value.handle]: value for value in dataset.probes},
        "readout": {
            readout_keys[value.handle]: value for value in dataset.readouts
        },
        "gauge": {gauge_keys[value.handle]: value for value in dataset.gauge_actions},
    }


def _exact_field_maps(
    target_values: FrozenSet[str],
    source_values: FrozenSet[str],
    lookup: Mapping[str, object],
    label: str,
) -> Tuple[ExactFieldMap, ...]:
    if not target_values <= source_values:
        raise RegionalMapFailure(f"regional {label} pullback is missing")
    return tuple(
        ExactFieldMap(key, key, lookup[key], lookup[key])
        for key in sorted(target_values)
    )


def _record_payloads(
    dataset: legacy.OperationalDataset,
    resolved_by_handle: Mapping[str, legacy.ResolvedRecord],
) -> Mapping[str, ExactRecordPayload]:
    result = {}
    for candidate in dataset.records:
        resolved = resolved_by_handle[candidate.handle]
        result[resolved.structural_id] = ExactRecordPayload(
            structural_id=resolved.structural_id,
            support=resolved.support,
            projector_resolution=resolved.projector_resolution,
            candidate_structure=candidate.structural_key(),
            passes_w3=resolved.passes_w3,
        )
    return result


def build_full_regional_arrow(
    source: legacy.RegionalObject,
    target: legacy.RegionalObject,
    composition: legacy.CompositionObject,
    factors: Sequence[FrozenSet[int]],
    element_to_coordinate: Mapping[int, Tuple[int, ...]],
    coordinate_to_element: Mapping[Tuple[int, ...], int],
    payloads: Mapping[str, Mapping[str, object]],
    records: Mapping[str, ExactRecordPayload],
) -> FullRegionalArrow:
    if not set(target.atoms) <= set(source.atoms):
        raise RegionalMapFailure("regional arrow is not a restriction")
    operation_map = tuple(
        (
            operation,
            legacy._project_operation(
                operation,
                source.atoms,
                target.atoms,
                composition,
                factors,
                element_to_coordinate,
                coordinate_to_element,
            ),
        )
        for operation in sorted(source.operations)
    )
    operation_dict = dict(operation_map)
    if any(value not in target.operations for value in operation_dict.values()):
        raise RegionalMapFailure("operation projection leaves target")

    rows = []
    for left, right in source.row_pairs:
        target_left = operation_dict[left]
        target_right = operation_dict[right]
        source_row = composition.row(left, right)
        target_row = composition.row(target_left, target_right)
        if (
            source_row.status != legacy.IMPLEMENTED
            or target_row.status != legacy.IMPLEMENTED
            or source_row.result is None
            or target_row.result is None
            or source_row.law is None
            or target_row.law is None
            or source_row.observed_signature is None
            or target_row.observed_signature is None
        ):
            raise RegionalMapFailure("regional row is incomplete")
        if operation_dict[source_row.result] != target_row.result:
            raise RegionalMapFailure("regional row result square fails")
        if source_row.observed_signature != source_row.law.signature():
            raise RegionalMapFailure("source row signature/law mismatch")
        if target_row.observed_signature != target_row.law.signature():
            raise RegionalMapFailure("target row signature/law mismatch")
        rows.append(
            FullRowMap(
                source_left=left,
                source_right=right,
                target_left=target_left,
                target_right=target_right,
                source_tau=source_row.tau,
                target_tau=target_row.tau,
                source_status=source_row.status,
                target_status=target_row.status,
                source_result=source_row.result,
                target_result=target_row.result,
                source_law=source_row.law,
                target_law=target_row.law,
                source_signature=source_row.observed_signature,
                target_signature=target_row.observed_signature,
            )
        )

    selectability = tuple(
        (
            source_operation,
            target_operation,
            composition.classes[source_operation].independently_selectable,
            composition.classes[target_operation].independently_selectable,
        )
        for source_operation, target_operation in operation_map
    )
    if any(left and not right for _, _, left, right in selectability):
        raise RegionalMapFailure("restriction destroys independent selectability")

    if not target.records <= source.records:
        raise RegionalMapFailure("record restriction is missing")
    record_maps = tuple(
        ExactRecordMap(records[key], records[key]) for key in sorted(target.records)
    )
    if any(not value.source.passes_w3 or not value.target.passes_w3 for value in record_maps):
        raise RegionalMapFailure("record map contains a non-W3 interface")

    context_map = ExecutableContextMap(
        source_operations=source.operations,
        target_operations=target.operations,
        operation_map=operation_map,
        source_preparations=source.preparations,
        target_preparations=target.preparations,
        source_probes=source.probes,
        target_probes=target.probes,
        source_readouts=source.readouts,
        target_readouts=target.readouts,
        source_records=source.records,
        target_records=target.records,
        source_gauges=source.gauges,
        target_gauges=target.gauges,
    )
    return FullRegionalArrow(
        source=source.structural_id,
        target=target.structural_id,
        operation_map=operation_map,
        row_map=tuple(rows),
        selectability_map=selectability,
        preparation_maps=_exact_field_maps(
            target.preparations,
            source.preparations,
            payloads["preparation"],
            "preparation",
        ),
        context_map=context_map,
        probe_maps=_exact_field_maps(
            target.probes, source.probes, payloads["probe"], "probe"
        ),
        readout_maps=_exact_field_maps(
            target.readouts,
            source.readouts,
            payloads["readout"],
            "readout",
        ),
        record_maps=record_maps,
        gauge_maps=_exact_field_maps(
            target.gauges, source.gauges, payloads["gauge"], "gauge"
        ),
    )


def validate_full_regional_arrow(
    arrow: FullRegionalArrow,
    source: legacy.RegionalObject,
    target: legacy.RegionalObject,
    composition: legacy.CompositionObject,
) -> bool:
    operation_map = dict(arrow.operation_map)
    if set(operation_map) != set(source.operations):
        return False
    if set(operation_map.values()) - set(target.operations):
        return False
    rows = {(value.source_left, value.source_right): value for value in arrow.row_map}
    if set(rows) != set(source.row_pairs):
        return False
    for key, value in rows.items():
        source_row = composition.row(*key)
        target_row = composition.row(value.target_left, value.target_right)
        if (
            value.source_tau != source_row.tau
            or value.target_tau != target_row.tau
            or value.source_status != source_row.status
            or value.target_status != target_row.status
            or value.source_result != source_row.result
            or value.target_result != target_row.result
            or value.source_law != source_row.law
            or value.target_law != target_row.law
            or value.source_signature != source_row.observed_signature
            or value.target_signature != target_row.observed_signature
            or operation_map[value.source_result] != value.target_result
        ):
            return False
    context = arrow.context_map
    return (
        context.source_operations == source.operations
        and context.target_operations == target.operations
        and context.operation_map == arrow.operation_map
        and context.source_preparations == source.preparations
        and context.target_preparations == target.preparations
        and context.source_probes == source.probes
        and context.target_probes == target.probes
        and context.source_readouts == source.readouts
        and context.target_readouts == target.readouts
        and context.source_records == source.records
        and context.target_records == target.records
        and context.source_gauges == source.gauges
        and context.target_gauges == target.gauges
    )


def _compose_pairs(
    first: Sequence[Tuple[int, int]],
    second: Sequence[Tuple[int, int]],
) -> Tuple[Tuple[int, int], ...]:
    first_map = dict(first)
    second_map = dict(second)
    return tuple(sorted((source, second_map[middle]) for source, middle in first_map.items()))


def full_regional_arrow_composes(
    first: FullRegionalArrow,
    second: FullRegionalArrow,
    direct: FullRegionalArrow,
) -> bool:
    if first.target != second.source or first.source != direct.source or second.target != direct.target:
        return False
    if _compose_pairs(first.operation_map, second.operation_map) != direct.operation_map:
        return False
    first_rows = {(value.source_left, value.source_right): value for value in first.row_map}
    second_rows = {(value.source_left, value.source_right): value for value in second.row_map}
    direct_rows = {(value.source_left, value.source_right): value for value in direct.row_map}
    for key, direct_row in direct_rows.items():
        if key not in first_rows:
            return False
        middle = first_rows[key]
        middle_key = (middle.target_left, middle.target_right)
        if middle_key not in second_rows:
            return False
        last = second_rows[middle_key]
        if (
            middle.target_tau != last.source_tau
            or middle.target_status != last.source_status
            or middle.target_result != last.source_result
            or middle.target_law != last.source_law
            or middle.target_signature != last.source_signature
        ):
            return False
        if (
            direct_row.target_left != last.target_left
            or direct_row.target_right != last.target_right
            or direct_row.target_tau != last.target_tau
            or direct_row.target_status != last.target_status
            or direct_row.target_result != last.target_result
            or direct_row.target_law != last.target_law
            or direct_row.target_signature != last.target_signature
        ):
            return False
    if first.context_map.target_operations != second.context_map.source_operations:
        return False
    if first.context_map.source_operations != direct.context_map.source_operations:
        return False
    if second.context_map.target_operations != direct.context_map.target_operations:
        return False
    for name in (
        "preparation_maps",
        "probe_maps",
        "readout_maps",
        "gauge_maps",
    ):
        first_values = {value.target_key: value for value in getattr(first, name)}
        second_values = {value.source_key: value for value in getattr(second, name)}
        direct_values = {(value.source_key, value.target_key) for value in getattr(direct, name)}
        composed = {
            (first_values[key].source_key, second_values[key].target_key)
            for key in first_values.keys() & second_values.keys()
        }
        if composed != direct_values:
            return False
    first_records = {value.target.structural_id: value for value in first.record_maps}
    second_records = {value.source.structural_id: value for value in second.record_maps}
    direct_records = {
        (value.source.structural_id, value.target.structural_id)
        for value in direct.record_maps
    }
    composed_records = {
        (first_records[key].source.structural_id, second_records[key].target.structural_id)
        for key in first_records.keys() & second_records.keys()
    }
    return composed_records == direct_records


def build_full_regional_atlas(
    dataset: legacy.OperationalDataset,
    analysis: AnalysisRun,
    factorization: legacy.FactorCertificate,
) -> FullRegionalAtlas:
    address = analysis.result
    if factorization not in address.finest_certificates:
        raise RegionalMapFailure("atlas requested for a non-finest factorization")
    resolved_records, records_by_handle = legacy.resolve_records(
        dataset, address.composition, address.inverses
    )
    record_by_id = {value.structural_id: value for value in resolved_records}
    exact_record_payloads = _record_payloads(dataset, records_by_handle)
    contexts = legacy._resolve_contexts(
        dataset, address, factorization, records_by_handle
    )
    if not contexts:
        raise RegionalMapFailure("no operational contexts for regional atlas")
    raw_objects = legacy._meet_contexts(contexts)
    try:
        objects = legacy._complete_regional_objects(
            raw_objects, address.composition, record_by_id
        )
    except legacy.InvalidInput as error:
        raise RegionalMapFailure(str(error)) from error
    if not objects:
        raise RegionalMapFailure("no record-bearing regional objects")

    # Regional restriction replay uses the same canonical exact cache as
    # factor discovery and certificate replay.  No handle enters the key.
    with analysis.instrumentation.timed("regional_restriction_algebras"):
        for value in objects:
            analysis.instrumentation.increment(
                "regional_restriction_algebra_requests"
            )
            if analysis.algebra_cache.algebra(value.operations).dimension < 1:
                raise RegionalMapFailure("regional represented algebra is empty")

    object_by_id = {value.structural_id: value for value in objects}
    element_to_coordinate, coordinate_to_element = legacy.factor_coordinates(
        address.composition, factorization.factors
    )
    payloads = _payload_lookups(dataset)
    arrows = []
    for source in objects:
        for target in objects:
            if set(target.atoms) <= set(source.atoms):
                arrow = build_full_regional_arrow(
                    source,
                    target,
                    address.composition,
                    factorization.factors,
                    element_to_coordinate,
                    coordinate_to_element,
                    payloads,
                    exact_record_payloads,
                )
                if not validate_full_regional_arrow(
                    arrow, source, target, address.composition
                ):
                    raise RegionalMapFailure("full RegAddr arrow validation fails")
                arrows.append(arrow)
    arrows = tuple(sorted(arrows, key=lambda value: (value.source, value.target)))
    arrow_by_pair = {(value.source, value.target): value for value in arrows}
    coherent_regional_paths = 0
    for source in objects:
        for middle in objects:
            for target in objects:
                if set(target.atoms) <= set(middle.atoms) <= set(source.atoms):
                    if not full_regional_arrow_composes(
                        arrow_by_pair[(source.structural_id, middle.structural_id)],
                        arrow_by_pair[(middle.structural_id, target.structural_id)],
                        arrow_by_pair[(source.structural_id, target.structural_id)],
                    ):
                        raise RegionalMapFailure(
                            "full RegAddr direct/composite diagram fails"
                        )
                    coherent_regional_paths += 1

    facts = tuple(
        legacy.build_fact_interface(
            value, record_by_id, dataset.carrier_dimension
        )
        for value in objects
    )
    facts_by_region = {value.region: value for value in facts}
    fact_maps = tuple(
        legacy.build_fact_map(
            value, facts_by_region[value.source], facts_by_region[value.target]
        )
        for value in arrows
    )
    fact_by_pair = {
        (value.regional_source, value.regional_target): value
        for value in fact_maps
    }
    coherent_fact_paths = 0
    for source in objects:
        for middle in objects:
            for target in objects:
                if set(target.atoms) <= set(middle.atoms) <= set(source.atoms):
                    if not legacy.fact_map_composes(
                        fact_by_pair[(source.structural_id, middle.structural_id)],
                        fact_by_pair[(middle.structural_id, target.structural_id)],
                        fact_by_pair[(source.structural_id, target.structural_id)],
                    ):
                        raise RegionalMapFailure(
                            "projector/Boolean Rec naturality fails"
                        )
                    coherent_fact_paths += 1

    nonvacuous_triples = []
    for left, middle, right in itertools.combinations(contexts, 3):
        atoms = tuple(
            sorted(set(left.atoms) & set(middle.atoms) & set(right.atoms))
        )
        if not atoms:
            continue
        matches = tuple(value for value in objects if value.atoms == atoms)
        if len(matches) == 1 and matches[0].records:
            nonvacuous_triples.append(
                (
                    left.structural_id,
                    middle.structural_id,
                    right.structural_id,
                    matches[0].structural_id,
                )
            )
    universal = (
        tuple(sorted(set.intersection(*(set(value.atoms) for value in contexts))))
        if contexts
        else ()
    )
    all_proper = {
        tuple(atoms)
        for count in range(1, len(factorization.factors))
        for atoms in itertools.combinations(range(len(factorization.factors)), count)
    }
    return FullRegionalAtlas(
        factorization=factorization,
        contexts=contexts,
        objects=objects,
        arrows=arrows,
        facts=facts,
        fact_maps=fact_maps,
        coherent_regional_paths=coherent_regional_paths,
        coherent_fact_paths=coherent_fact_paths,
        nonvacuous_triples=tuple(nonvacuous_triples),
        universal_atoms=universal,
        is_complete_proper_boolean={value.atoms for value in objects} == all_proper,
    )


def validate_full_regional_atlas(
    dataset: legacy.OperationalDataset,
    analysis: AnalysisRun,
    atlas: FullRegionalAtlas,
) -> bool:
    """Replay every regional and factual map from the typed input.

    Equality with the replayed value is intentionally stronger than a digest
    check: it compares every operation, row, law, selectability declaration,
    context payload, projector pullback, Boolean map, identity and composite
    diagram represented by ``FullRegionalAtlas``.
    """

    if atlas.factorization not in analysis.result.finest_certificates:
        return False
    replay = build_full_regional_atlas(
        dataset, analysis, atlas.factorization
    )
    return replay == atlas


# ---------------------------------------------------------------------------
# Full-instrument twisted triple
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FullInstrumentIsomorphism:
    source: str
    target: str
    carrier_action: legacy.MonomialLaw
    operation_map: Tuple[Tuple[str, str], ...]
    row_map: Tuple[Tuple[legacy.CompositionRow, legacy.CompositionRow], ...]
    preparation_map: Tuple[Tuple[legacy.FieldDatum, legacy.FieldDatum], ...]
    context_map: Tuple[Tuple[legacy.AccessContext, legacy.AccessContext], ...]
    probe_map: Tuple[Tuple[legacy.FieldDatum, legacy.FieldDatum], ...]
    readout_map: Tuple[Tuple[legacy.ReadoutDatum, legacy.ReadoutDatum], ...]
    record_map: Tuple[Tuple[legacy.RecordCandidate, legacy.RecordCandidate], ...]
    gauge_map: Tuple[Tuple[legacy.GaugeDatum, legacy.GaugeDatum], ...]


@dataclass(frozen=True)
class FullTwistedTriple:
    instruments: Tuple[legacy.OperationalDataset, ...]
    pair_maps: Tuple[FullInstrumentIsomorphism, ...]
    pair_valid: Tuple[bool, bool, bool]
    regional_loop_commutes: bool
    record_loop_commutes: bool
    rejected_only_at_loop: bool


def _mini_full_instrument(prefix: str) -> legacy.OperationalDataset:
    unit = legacy.MonomialLaw.unit(2)
    swap = legacy.permutation_law((1, 0))
    operations = (
        legacy.OperationClass(
            f"{prefix}-unit", "q", "q", unit, unit.signature(), True
        ),
        legacy.OperationClass(
            f"{prefix}-swap", "q", "q", swap, swap.signature(), True
        ),
    )
    multiplication = ((0, 1), (1, 0))
    rows = []
    for left in range(2):
        for right in range(2):
            result = multiplication[left][right]
            law = operations[result].law
            rows.append(
                legacy.CompositionRow(
                    operations[left].handle,
                    operations[right].handle,
                    "q|q|q",
                    legacy.IMPLEMENTED,
                    operations[result].handle,
                    law,
                    law.signature(),
                )
            )
    preparation = legacy.FieldDatum(f"{prefix}-prep", "q", (5, 8))
    probe = legacy.FieldDatum(f"{prefix}-probe", "q", (13, 21))
    resolution = (frozenset((0,)), frozenset((1,)))
    readout = legacy.ReadoutDatum(f"{prefix}-readout", "q", resolution)
    witness = legacy.fourier_record_witness(2, f"{prefix}-witness")
    record = legacy.RecordCandidate(
        f"{prefix}-record",
        "q",
        tuple(value.handle for value in operations),
        witness,
        resolution,
    )
    gauge = legacy.GaugeDatum(f"{prefix}-gauge", unit)
    context = legacy.AccessContext(
        f"{prefix}-context",
        "q",
        tuple(value.handle for value in operations),
        (preparation.handle,),
        (probe.handle,),
        (readout.handle,),
        (record.handle,),
        (gauge.handle,),
    )
    return legacy.OperationalDataset(
        handle=f"{prefix}-instrument",
        carrier_dimension=2,
        operations=operations,
        composition_rows=tuple(rows),
        preparations=(preparation,),
        contexts=(context,),
        probes=(probe,),
        readouts=(readout,),
        records=(record,),
        gauge_actions=(gauge,),
        access_postulate="public full-instrument twisted-triple calibration",
    )


def _map_by_scientific_key(
    source: Sequence[object],
    target: Sequence[object],
    source_key,
    target_key=None,
) -> Tuple[Tuple[object, object], ...]:
    if target_key is None:
        target_key = source_key
    target_by_key = {target_key(value): value for value in target}
    if len(target_by_key) != len(target):
        raise RegionalMapFailure("full instrument target field is ambiguous")
    result = []
    for value in source:
        scientific = source_key(value)
        if scientific not in target_by_key:
            raise RegionalMapFailure("full instrument field has no target")
        result.append((value, target_by_key[scientific]))
    return tuple(result)


def _record_nonprojector_key(value: legacy.RecordCandidate) -> Tuple[object, ...]:
    projector_key = tuple(
        tuple(sorted(atom)) for atom in value.ambient_projector_resolution
    )
    return tuple(item for item in value.structural_key() if item != projector_key)


def build_full_instrument_isomorphism(
    source: legacy.OperationalDataset,
    target: legacy.OperationalDataset,
    carrier_action: legacy.MonomialLaw,
) -> FullInstrumentIsomorphism:
    target_operations = {
        (value.source_type, value.target_type, value.observed_signature): value
        for value in target.operations
    }
    operation_pairs = []
    for value in source.operations:
        transformed = value.law.conjugated(carrier_action)
        key = (value.source_type, value.target_type, transformed.signature())
        if key not in target_operations:
            raise RegionalMapFailure("operation has no isomorphic target")
        operation_pairs.append((value.handle, target_operations[key].handle))
    operation_map = dict(operation_pairs)
    target_rows = {(value.left, value.right): value for value in target.composition_rows}
    row_pairs = []
    for row in source.composition_rows:
        key = (operation_map[row.left], operation_map[row.right])
        if key not in target_rows:
            raise RegionalMapFailure("composition row has no isomorphic target")
        row_pairs.append((row, target_rows[key]))

    preparations = _map_by_scientific_key(
        source.preparations, target.preparations, lambda value: value.scientific_key()
    )
    probes = _map_by_scientific_key(
        source.probes, target.probes, lambda value: value.scientific_key()
    )

    def transported_resolution(value: legacy.ReadoutDatum):
        return (
            value.boundary_type,
            frozenset(
                frozenset(carrier_action.permutation[index] for index in atom)
                for atom in value.projector_resolution
            ),
        )

    readouts = _map_by_scientific_key(
        source.readouts,
        target.readouts,
        transported_resolution,
        lambda value: (
            value.boundary_type,
            frozenset(value.projector_resolution),
        ),
    )

    def record_key(value: legacy.RecordCandidate):
        return (
            value.boundary_type,
            frozenset(operation_map[handle] for handle in value.access_operations),
            _record_nonprojector_key(value),
            frozenset(
                frozenset(carrier_action.permutation[index] for index in atom)
                for atom in value.ambient_projector_resolution
            ),
        )

    target_record_lookup = {}
    for value in target.records:
        target_record_lookup[
            (
                value.boundary_type,
                frozenset(value.access_operations),
                _record_nonprojector_key(value),
                frozenset(value.ambient_projector_resolution),
            )
        ] = value
    records = []
    for value in source.records:
        key = record_key(value)
        if key not in target_record_lookup:
            raise RegionalMapFailure("record candidate has no isomorphic target")
        records.append((value, target_record_lookup[key]))

    gauges = _map_by_scientific_key(
        source.gauge_actions,
        target.gauge_actions,
        lambda value: value.law.conjugated(carrier_action).signature(),
        lambda value: value.law.signature(),
    )
    prep_map = {left.handle: right.handle for left, right in preparations}
    probe_map = {left.handle: right.handle for left, right in probes}
    readout_map = {left.handle: right.handle for left, right in readouts}
    record_map = {left.handle: right.handle for left, right in records}
    gauge_map = {left.handle: right.handle for left, right in gauges}
    target_contexts = {
        (
            value.boundary_type,
            frozenset(value.operation_handles),
            frozenset(value.preparation_handles),
            frozenset(value.probe_handles),
            frozenset(value.readout_handles),
            frozenset(value.record_handles),
            frozenset(value.gauge_handles),
        ): value
        for value in target.contexts
    }
    contexts = []
    for value in source.contexts:
        key = (
            value.boundary_type,
            frozenset(operation_map[entry] for entry in value.operation_handles),
            frozenset(prep_map[entry] for entry in value.preparation_handles),
            frozenset(probe_map[entry] for entry in value.probe_handles),
            frozenset(readout_map[entry] for entry in value.readout_handles),
            frozenset(record_map[entry] for entry in value.record_handles),
            frozenset(gauge_map[entry] for entry in value.gauge_handles),
        )
        if key not in target_contexts:
            raise RegionalMapFailure("context has no isomorphic target")
        contexts.append((value, target_contexts[key]))
    return FullInstrumentIsomorphism(
        source=source.handle,
        target=target.handle,
        carrier_action=carrier_action,
        operation_map=tuple(operation_pairs),
        row_map=tuple(row_pairs),
        preparation_map=tuple(preparations),
        context_map=tuple(contexts),
        probe_map=tuple(probes),
        readout_map=tuple(readouts),
        record_map=tuple(records),
        gauge_map=tuple(gauges),
    )


def validate_full_instrument_isomorphism(
    value: FullInstrumentIsomorphism,
    source: legacy.OperationalDataset,
    target: legacy.OperationalDataset,
) -> bool:
    operation_map = dict(value.operation_map)
    if set(operation_map) != {item.handle for item in source.operations}:
        return False
    if set(operation_map.values()) != {item.handle for item in target.operations}:
        return False
    source_operations = {item.handle: item for item in source.operations}
    target_operations = {item.handle: item for item in target.operations}
    for left, right in operation_map.items():
        source_value = source_operations[left]
        target_value = target_operations[right]
        if (
            source_value.law.conjugated(value.carrier_action).signature()
            != target_value.observed_signature
            or source_value.independently_selectable
            != target_value.independently_selectable
            or source_value.source_type != target_value.source_type
            or source_value.target_type != target_value.target_type
        ):
            return False
    if len(value.row_map) != len(source.composition_rows):
        return False
    for source_row, target_row in value.row_map:
        if (
            source_row not in source.composition_rows
            or target_row not in target.composition_rows
            or
            target_row.left != operation_map[source_row.left]
            or target_row.right != operation_map[source_row.right]
            or target_row.tau != source_row.tau
            or target_row.status != source_row.status
            or target_row.result_class != operation_map[source_row.result_class]
            or source_row.law is None
            or target_row.law is None
            or source_row.law.conjugated(value.carrier_action).signature()
            != target_row.observed_signature
            or source_row.law.conjugated(value.carrier_action)
            != target_row.law
            or target_row.law.signature() != target_row.observed_signature
        ):
            return False

    def complete_bijection(mapping, source_values, target_values) -> bool:
        return (
            len(mapping) == len(source_values) == len(target_values)
            and {left for left, _right in mapping} == set(source_values)
            and {right for _left, right in mapping} == set(target_values)
        )

    if not complete_bijection(
        value.preparation_map, source.preparations, target.preparations
    ) or any(left.scientific_key() != right.scientific_key() for left, right in value.preparation_map):
        return False
    if not complete_bijection(value.probe_map, source.probes, target.probes) or any(
        left.scientific_key() != right.scientific_key()
        for left, right in value.probe_map
    ):
        return False
    if not complete_bijection(value.readout_map, source.readouts, target.readouts):
        return False
    for left, right in value.readout_map:
        transported = frozenset(
            frozenset(value.carrier_action.permutation[index] for index in atom)
            for atom in left.projector_resolution
        )
        if left.boundary_type != right.boundary_type or transported != frozenset(
            right.projector_resolution
        ):
            return False
    if not complete_bijection(value.record_map, source.records, target.records):
        return False
    record_handle_map = {}
    for left, right in value.record_map:
        transported = frozenset(
            frozenset(value.carrier_action.permutation[index] for index in atom)
            for atom in left.ambient_projector_resolution
        )
        if (
            left.boundary_type != right.boundary_type
            or frozenset(operation_map[handle] for handle in left.access_operations)
            != frozenset(right.access_operations)
            or _record_nonprojector_key(left) != _record_nonprojector_key(right)
            or transported != frozenset(right.ambient_projector_resolution)
            or not legacy.evaluate_record_witness(
                left.witness,
                legacy.identity(len(left.witness.write)),
                len(left.witness.write),
            ).passes_w3
            or not legacy.evaluate_record_witness(
                right.witness,
                legacy.identity(len(right.witness.write)),
                len(right.witness.write),
            ).passes_w3
        ):
            return False
        record_handle_map[left.handle] = right.handle
    if not complete_bijection(
        value.gauge_map, source.gauge_actions, target.gauge_actions
    ) or any(
        left.law.conjugated(value.carrier_action) != right.law
        for left, right in value.gauge_map
    ):
        return False
    if not complete_bijection(value.context_map, source.contexts, target.contexts):
        return False
    preparation_handles = {
        left.handle: right.handle for left, right in value.preparation_map
    }
    probe_handles = {left.handle: right.handle for left, right in value.probe_map}
    readout_handles = {
        left.handle: right.handle for left, right in value.readout_map
    }
    gauge_handles = {left.handle: right.handle for left, right in value.gauge_map}
    for left, right in value.context_map:
        if (
            left.boundary_type != right.boundary_type
            or frozenset(operation_map[handle] for handle in left.operation_handles)
            != frozenset(right.operation_handles)
            or frozenset(preparation_handles[handle] for handle in left.preparation_handles)
            != frozenset(right.preparation_handles)
            or frozenset(probe_handles[handle] for handle in left.probe_handles)
            != frozenset(right.probe_handles)
            or frozenset(readout_handles[handle] for handle in left.readout_handles)
            != frozenset(right.readout_handles)
            or frozenset(record_handle_map[handle] for handle in left.record_handles)
            != frozenset(right.record_handles)
            or frozenset(gauge_handles[handle] for handle in left.gauge_handles)
            != frozenset(right.gauge_handles)
        ):
            return False
    return True


def full_instrument_twisted_triple() -> FullTwistedTriple:
    first = _mini_full_instrument("alpha")
    second = _mini_full_instrument("beta")
    third = _mini_full_instrument("gamma")
    unit = legacy.MonomialLaw.unit(2)
    swap = legacy.permutation_law((1, 0))
    phi_12 = build_full_instrument_isomorphism(first, second, unit)
    phi_23 = build_full_instrument_isomorphism(second, third, unit)
    phi_13 = build_full_instrument_isomorphism(first, third, swap)
    pair_valid = (
        validate_full_instrument_isomorphism(phi_12, first, second),
        validate_full_instrument_isomorphism(phi_23, second, third),
        validate_full_instrument_isomorphism(phi_13, first, third),
    )
    composed_action = phi_23.carrier_action.after(phi_12.carrier_action)
    regional_loop = composed_action == phi_13.carrier_action
    identity_atoms = (frozenset((0,)), frozenset((1,)))
    composed_records = tuple(
        frozenset(composed_action.permutation[index] for index in atom)
        for atom in identity_atoms
    )
    direct_records = tuple(
        frozenset(phi_13.carrier_action.permutation[index] for index in atom)
        for atom in identity_atoms
    )
    record_loop = composed_records == direct_records
    return FullTwistedTriple(
        instruments=(first, second, third),
        pair_maps=(phi_12, phi_23, phi_13),
        pair_valid=pair_valid,
        regional_loop_commutes=regional_loop,
        record_loop_commutes=record_loop,
        rejected_only_at_loop=(
            all(pair_valid) and not regional_loop and not record_loop
        ),
    )


# ---------------------------------------------------------------------------
# Generic transformations, novelty invariants, and total resolver
# ---------------------------------------------------------------------------


def reorder_dataset(dataset: legacy.OperationalDataset) -> legacy.OperationalDataset:
    return legacy.OperationalDataset(
        handle=f"reordered::{dataset.handle}",
        carrier_dimension=dataset.carrier_dimension,
        operations=tuple(reversed(dataset.operations)),
        composition_rows=tuple(reversed(dataset.composition_rows)),
        preparations=tuple(reversed(dataset.preparations)),
        contexts=tuple(reversed(dataset.contexts)),
        probes=tuple(reversed(dataset.probes)),
        readouts=tuple(reversed(dataset.readouts)),
        records=tuple(reversed(dataset.records)),
        gauge_actions=tuple(reversed(dataset.gauge_actions)),
        access_postulate=dataset.access_postulate,
    )


def composition_invariants(composition: legacy.CompositionObject) -> Mapping[str, object]:
    if composition.identity is None or not composition.total_implemented:
        return {"order": composition.size, "group_like": False}
    inverses = legacy.inverse_table(composition)
    orders = []
    for element in range(composition.size):
        value = composition.identity
        order = 0
        while True:
            order += 1
            value = composition.product(value, element)
            if value == composition.identity:
                break
            if order > composition.size:
                raise legacy.AccessUnderdetermined("element order exceeds group size")
        orders.append(order)
    center = tuple(
        element
        for element in range(composition.size)
        if all(
            composition.product(element, other)
            == composition.product(other, element)
            for other in range(composition.size)
        )
    )
    commutators = []
    for left in range(composition.size):
        for right in range(composition.size):
            commutators.append(
                composition.product(
                    composition.product(
                        composition.product(left, right), inverses[left]
                    ),
                    inverses[right],
                )
            )
    derived = legacy.subgroup_generated(composition, commutators, inverses)
    histogram: Dict[int, int] = {}
    for order in orders:
        histogram[order] = histogram.get(order, 0) + 1
    return {
        "order": composition.size,
        "group_like": True,
        "element_order_histogram": dict(sorted(histogram.items())),
        "center_order": len(center),
        "derived_order": len(derived),
    }


@dataclass(frozen=True)
class Outcome:
    code: str
    category: str
    exit_code: int
    reason: str

    def __post_init__(self) -> None:
        if self.category == "scientific":
            valid = self.code in SCIENTIFIC_OUTCOMES and self.exit_code == 0
        elif self.category == "procedural":
            valid = self.code == PROCEDURAL_OUTCOME and self.exit_code == 1
        else:
            valid = False
        if not valid:
            raise ValueError("outcome is not one registered total-resolver value")


@dataclass(frozen=True)
class Resolution:
    outcome: Outcome
    analysis: Optional[AnalysisRun]
    atlas: Optional[FullRegionalAtlas]


def adjudicate_resolution_artifacts(
    dataset: legacy.OperationalDataset,
    resolution: Resolution,
) -> Resolution:
    """Total, fail-closed validation of a returned or adversarially mutated result."""

    try:
        outcome = resolution.outcome
        if outcome.category == "procedural":
            if resolution.analysis is not None or resolution.atlas is not None:
                raise AssertionError("procedural result carries scientific artifacts")
            return resolution
        if resolution.analysis is None:
            raise AssertionError("scientific result lacks address analysis")
        finest = resolution.analysis.result.finest_certificates
        if outcome.code == "RQ0-L0-BLOCKED-AT-ADDRESS":
            if finest or resolution.atlas is not None:
                raise AssertionError("address block carries a positive certificate")
            return resolution
        if outcome.code == "RQ0-L0-BLOCKED-AT-REGIONAL-MAPS":
            if not finest or resolution.atlas is not None:
                raise AssertionError("regional-map block has inconsistent artifacts")
            return resolution
        if resolution.atlas is None:
            raise AssertionError("positive outcome lacks a regional atlas")
        expected_code = (
            "RQ0-LOCALIZATION-GROUPOID"
            if len(finest) > 1
            else "RQ0-LOCAL-ATLAS"
        )
        if outcome.code != expected_code:
            raise AssertionError("positive outcome disagrees with ambiguity scope")
        if not validate_full_regional_atlas(
            dataset, resolution.analysis, resolution.atlas
        ):
            raise AssertionError("regional/fact artifact replay fails")
        return resolution
    except Exception as error:
        return Resolution(
            Outcome(
                PROCEDURAL_OUTCOME,
                "procedural",
                1,
                f"artifact validation failed closed: {type(error).__name__}: {error}",
            ),
            None,
            None,
        )


def resolve_dataset(
    dataset: legacy.OperationalDataset,
    *,
    cap_seconds: float,
    injected_branch: Optional[str] = None,
    progress: Optional[Callable[[Mapping[str, object]], None]] = None,
) -> Resolution:
    started = time.monotonic()
    deadline = started + cap_seconds
    try:
        if injected_branch == "timeout":
            raise RuntimeCapExceeded("injected registered timeout")
        if injected_branch == "exception":
            raise RuntimeError("injected resolver exception")
        analysis = analyze_addressability(
            dataset, deadline=deadline, progress=progress
        )
        if injected_branch == "missing-outcome":
            raise RuntimeError("normal return produced no registered outcome")
        if injected_branch == "multiple-outcomes":
            raise RuntimeError("normal return produced multiple registered outcomes")
        if analysis.result.blocked_at_address:
            return adjudicate_resolution_artifacts(dataset, Resolution(
                Outcome(
                    "RQ0-L0-BLOCKED-AT-ADDRESS",
                    "scientific",
                    0,
                    analysis.result.first_obstruction
                    or "complete factor search returned no eligible certificate",
                ),
                analysis,
                None,
            ))
        factorization = analysis.result.finest_certificates[0]
        try:
            atlas = build_full_regional_atlas(dataset, analysis, factorization)
        except (RegionalMapFailure, legacy.InvalidInput, legacy.AccessUnderdetermined) as error:
            return adjudicate_resolution_artifacts(dataset, Resolution(
                Outcome(
                    "RQ0-L0-BLOCKED-AT-REGIONAL-MAPS",
                    "scientific",
                    0,
                    str(error),
                ),
                analysis,
                None,
            ))
        code = (
            "RQ0-LOCALIZATION-GROUPOID"
            if len(analysis.result.finest_certificates) > 1
            else "RQ0-LOCAL-ATLAS"
        )
        return adjudicate_resolution_artifacts(dataset, Resolution(
            Outcome(code, "scientific", 0, "all registered prerequisites pass"),
            analysis,
            atlas,
        ))
    except RuntimeCapExceeded as error:
        return Resolution(
            Outcome(PROCEDURAL_OUTCOME, "procedural", 1, str(error)),
            None,
            None,
        )
    except (legacy.InvalidInput, legacy.AccessUnderdetermined) as error:
        return Resolution(
            Outcome(
                PROCEDURAL_OUTCOME,
                "procedural",
                1,
                f"malformed/access-underdetermined input: {error}",
            ),
            None,
            None,
        )
    except Exception as error:  # total resolver boundary
        return Resolution(
            Outcome(
                PROCEDURAL_OUTCOME,
                "procedural",
                1,
                f"caught {type(error).__name__}: {error}",
            ),
            None,
            None,
        )


def resolve_serialized_dataset(
    value: Mapping[str, object],
    *,
    cap_seconds: float,
    injected_branch: Optional[str] = None,
    progress: Optional[Callable[[Mapping[str, object]], None]] = None,
) -> Resolution:
    """Total entry point from untrusted serialized operational input."""

    try:
        dataset = legacy.dataset_from_data(value)
    except Exception as error:
        return Resolution(
            Outcome(
                PROCEDURAL_OUTCOME,
                "procedural",
                1,
                f"serialized input failed closed: {type(error).__name__}: {error}",
            ),
            None,
            None,
        )
    return resolve_dataset(
        dataset,
        cap_seconds=cap_seconds,
        injected_branch=injected_branch,
        progress=progress,
    )


def structural_summary(resolution: Resolution) -> Mapping[str, object]:
    if resolution.analysis is None:
        return {"outcome": resolution.outcome.code}
    address = resolution.analysis.result
    summary: Dict[str, object] = {
        "outcome": resolution.outcome.code,
        "factor_orders": [
            sorted(value.factor_orders) for value in address.finest_certificates
        ],
        "normal_subobjects": len(address.normal_subobjects),
    }
    if resolution.atlas is not None:
        orders = resolution.atlas.factorization.factor_orders
        summary.update(
            {
                "regional_scopes": sorted(
                    sorted(orders[index] for index in value.atoms)
                    for value in resolution.atlas.objects
                ),
                "regional_objects": len(resolution.atlas.objects),
                "regional_arrows": len(resolution.atlas.arrows),
                "fact_maps": len(resolution.atlas.fact_maps),
                "nonvacuous_triples": len(
                    resolution.atlas.nonvacuous_triples
                ),
                "universal_factor_orders": sorted(
                    orders[index] for index in resolution.atlas.universal_atoms
                ),
                "complete_proper_boolean": resolution.atlas.is_complete_proper_boolean,
            }
        )
    return summary


def canonical_data(value: object) -> object:
    if dataclasses.is_dataclass(value):
        return canonical_data(dataclasses.asdict(value))
    if isinstance(value, legacy.Q24):
        return legacy.q24_to_data(value)
    if isinstance(value, legacy.MonomialLaw):
        return value.to_data()
    if isinstance(value, frozenset):
        return [canonical_data(entry) for entry in sorted(value)]
    if isinstance(value, tuple):
        return [canonical_data(entry) for entry in value]
    if isinstance(value, list):
        return [canonical_data(entry) for entry in value]
    if isinstance(value, dict):
        return {
            str(key): canonical_data(entry)
            for key, entry in sorted(value.items(), key=lambda item: str(item[0]))
        }
    return value


def canonical_json(value: object) -> str:
    return json.dumps(canonical_data(value), indent=2, sort_keys=True) + "\n"


if __name__ == "__main__":
    # Stage-A smoke surface only.  Full qualification lives in its own runner.
    twisted = full_instrument_twisted_triple()
    payload = {
        "schema": ESTIMATOR_API_VERSION,
        "full_twisted_pair_valid": list(twisted.pair_valid),
        "full_twisted_rejected_only_at_loop": twisted.rejected_only_at_loop,
        "scientific_outcome": None,
        "stage": "PRE-FIXTURE-FROZEN-API",
    }
    print(canonical_json(payload), end="")
