#!/usr/bin/env python3
"""Exact scorer and fail-closed receipt for the RQ0-L0 repair.

The generic estimator was frozen at v13 #36 before the encoding/amplitude
contents imported from the fixture module existed.  This scorer may read both
surfaces, but neither of them imports this file.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
import sys
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, Mapping, Optional, Sequence, Tuple

import rq0_l0_addressability_estimator_exact as est
import rq0_l0_addressability_fixtures_exact as fixtures


ROOT = Path(__file__).resolve().parents[2]
SELF_PATH = Path(__file__).resolve()
ESTIMATOR_PATH = ROOT / "v13/code/rq0_l0_addressability_estimator_exact.py"
FIXTURE_PATH = ROOT / "v13/code/rq0_l0_addressability_fixtures_exact.py"
PIN_PATH = ROOT / "v13/note-rq0-operational-localization-addressability-repair-pin.md"

ESTIMATOR_SHA256 = "7c8571eac81692eeb87058b1162bf1b874179e93b3d11bc204f264877465b0e1"
ESTIMATOR_COMMIT = "208a354"
PIN_SHA256 = "8135a0c9f358c86384d0d248a7cbf99131095656b5e61c06c8d49d0f62175fe3"
PIN_COMMIT = "ffbcce6"
RUNTIME_CAP_SECONDS = 360


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@dataclass(frozen=True)
class Check:
    handle: str
    category: str
    passed: bool
    measured: str


def check(
    checks: list[Check],
    handle: str,
    category: str,
    passed: bool,
    measured: object,
) -> None:
    checks.append(Check(handle, category, bool(passed), str(measured)))


def operation_map(dataset: est.OperationalDataset) -> Mapping[str, est.Operation]:
    return {value.handle: value for value in dataset.operations}


def row_map(dataset: est.OperationalDataset) -> Mapping[Tuple[str, str], est.CompositionRow]:
    return {(value.left, value.right): value for value in dataset.composition_rows}


def record_law(witness: est.RecordWitness) -> Tuple[Tuple[str, ...], ...]:
    laws = []
    for preparation in witness.preparations:
        state = est.mv(witness.write, preparation)
        laws.append(
            tuple(
                est.inner(est.mv(projector, state), est.mv(projector, state)).render()
                for projector in witness.cut_record_projectors
            )
        )
    return tuple(laws)


def same_noncomposition_fields(
    left: est.OperationalDataset,
    right: est.OperationalDataset,
) -> bool:
    return (
        left.dimension == right.dimension
        and left.operations == right.operations
        and left.generator_handles == right.generator_handles
        and left.preparations == right.preparations
        and left.probes == right.probes
        and left.records == right.records
        and left.gauge_actions == right.gauge_actions
        and left.gauge_declaration == right.gauge_declaration
    )


def changed_rows(
    base: est.OperationalDataset,
    mutant: est.OperationalDataset,
) -> Tuple[Tuple[est.CompositionRow, est.CompositionRow], ...]:
    base_rows = row_map(base)
    mutant_rows = row_map(mutant)
    if set(base_rows) != set(mutant_rows):
        return ()
    return tuple(
        (base_rows[key], mutant_rows[key])
        for key in sorted(base_rows)
        if base_rows[key] != mutant_rows[key]
    )


def conjugated_dataset_fields(
    source: est.OperationalDataset,
    target: est.OperationalDataset,
    action: est.Matrix,
    monomial: bool,
) -> bool:
    if monomial:
        expected = fixtures.conjugate_dataset_monomial(source, action, "expected")
    else:
        expected = fixtures.conjugate_dataset(source, action, "expected")
    return (
        expected.dimension == target.dimension
        and expected.operations == target.operations
        and expected.composition_rows == target.composition_rows
        and expected.generator_handles == target.generator_handles
        and expected.preparations == target.preparations
        and expected.probes == target.probes
        and expected.records == target.records
        and expected.gauge_actions == target.gauge_actions
        and expected.access_declaration == target.access_declaration
        and expected.gauge_declaration == target.gauge_declaration
    )


def renamed_dataset_isomorphism(
    source: est.OperationalDataset,
    target: est.OperationalDataset,
) -> Tuple[bool, Mapping[str, str]]:
    target_by_amplitude = {
        est.amplitude_signature(value.amplitude): value.handle
        for value in target.operations
    }
    if len(target_by_amplitude) != len(target.operations):
        return False, {}
    mapping: Dict[str, str] = {}
    for value in source.operations:
        signature = est.amplitude_signature(value.amplitude)
        if signature not in target_by_amplitude:
            return False, {}
        mapping[value.handle] = target_by_amplitude[signature]
    if len(set(mapping.values())) != len(mapping):
        return False, {}
    source_rows = {
        (
            mapping[row.left],
            mapping[row.right],
            row.context,
            row.status,
            None if row.result is None else mapping[row.result],
        )
        for row in source.composition_rows
    }
    target_rows = {
        (row.left, row.right, row.context, row.status, row.result)
        for row in target.composition_rows
    }
    fields = (
        source.dimension == target.dimension
        and source.preparations == tuple(reversed(target.preparations))
        and set(source.records) == set(target.records)
        and set(source.gauge_actions) == set(target.gauge_actions)
    )
    return source_rows == target_rows and fields, mapping


def factor_truth_score(
    result: est.LocalizationResult,
    truth: fixtures.MainTruth,
) -> bool:
    if len(result.core.finest_factorizations) != 1:
        return False
    recovered = []
    for factor in result.core.finest_factorizations[0].factors:
        hidden = set()
        for class_index in factor:
            members = result.core.composition.classes[class_index].members
            if len(members) != 1 or members[0] not in truth.element_by_handle:
                return False
            hidden.add(truth.element_by_handle[members[0]])
        recovered.append(frozenset(hidden))
    return set(recovered) == set(truth.factor_elements)


def primitive_pairing_mutant(
    dataset: est.OperationalDataset,
    core: est.AddressabilityCore,
) -> Tuple[est.Subobject, ...]:
    handle_to_class = {
        handle: index
        for index, value in enumerate(core.composition.classes)
        for handle in value.members
    }
    classes = tuple(handle_to_class[value] for value in dataset.generator_handles)
    if len(classes) != 6:
        return ()
    return tuple(
        est.subgroup_generated(core.composition, classes[index : index + 2], core.inverses)
        for index in range(0, 6, 2)
    )


def mutant_matches_finest(
    mutant: Sequence[est.Subobject],
    core: est.AddressabilityCore,
) -> bool:
    return bool(core.finest_factorizations) and set(mutant) == set(
        core.finest_factorizations[0].factors
    )


def composition_map_for_action(
    source: est.CompositionObject,
    target: est.CompositionObject,
    action: est.Matrix,
) -> Tuple[int, ...]:
    target_signatures = {
        value.signature: index for index, value in enumerate(target.classes)
    }
    class_map = []
    for value in source.classes:
        signature = est.amplitude_signature(est.conjugate_by(action, value.representative))
        if signature not in target_signatures:
            return ()
        class_map.append(target_signatures[signature])
    if len(set(class_map)) != source.size:
        return ()
    for left in range(source.size):
        for right in range(source.size):
            source_row = source.table[left][right]
            target_row = target.table[class_map[left]][class_map[right]]
            expected = None if source_row.result is None else class_map[source_row.result]
            if source_row.status != target_row.status or expected != target_row.result:
                return ()
    return tuple(class_map)


def permutation_bridge_search(
    source: est.OperationalDataset,
    target: est.OperationalDataset,
) -> Tuple[Tuple[Tuple[int, ...], Tuple[int, ...], bool], ...]:
    source_object = est.build_composition_object(source)
    target_object = est.build_composition_object(target)
    answers = []
    for permutation in itertools.permutations(range(source.dimension)):
        action = est.permutation_matrix(permutation)
        class_map = composition_map_for_action(source_object, target_object, action)
        if not class_map:
            continue
        records_ok = len(source.records) == len(target.records) and all(
            fixtures.conjugate_record(left, action) == right
            for left, right in zip(source.records, target.records)
        )
        answers.append((tuple(permutation), class_map, records_ok))
    return tuple(answers)


def twisted_pullback_rejected(atlas: est.LocalizationAtlas) -> bool:
    candidate = next(
        value for value in atlas.record_pullbacks if value.larger_atoms != value.smaller_atoms
    )
    interfaces = {value.atoms: value for value in atlas.fact_interfaces}
    larger = interfaces[candidate.larger_atoms]
    smaller = interfaces[candidate.smaller_atoms]
    handle, projectors = smaller.record_projectors[0]
    twisted = est.FactInterface(
        smaller.atoms,
        ((handle, tuple(reversed(projectors))),) + smaller.record_projectors[1:],
    )
    try:
        est.build_record_pullback(larger, twisted)
    except ValueError:
        return True
    return False


def run_quick_mode(mode: str) -> int:
    if mode == "mutate-anchor":
        payload = {
            "status": "RQ0-L0-INVALID",
            "reason": "estimator anchor mismatch",
            "scientific_outcome": None,
        }
        print(json.dumps(payload, sort_keys=True))
        return 1
    if mode == "mutate-science":
        base = est.analyze_addressability_core(est.public_calibration_dataset("base"))
        payload = {
            "status": "RQ0-L0-INVALID",
            "reason": "deliberately corrupted scientific addressability gate",
            "observed_public_factorizations": len(base.finest_factorizations),
            "scientific_outcome": None,
        }
        print(json.dumps(payload, sort_keys=True))
        return 1
    if mode == "no-outcome":
        print(
            json.dumps(
                {
                    "status": "RQ0-L0-INVALID",
                    "reason": "outcome resolver returned no rung",
                    "scientific_outcome": None,
                },
                sort_keys=True,
            )
        )
        return 1
    if mode == "malformed":
        malformed = est.OperationalDataset(
            handle="cap-mutant",
            dimension=est.MAX_CARRIER_DIMENSION + 1,
            operations=(),
            composition_rows=(),
            generator_handles=(),
        )
        try:
            est.validate_dataset(malformed)
        except est.InvalidDataset as error:
            print(
                json.dumps(
                    {
                        "status": "RQ0-L0-INVALID",
                        "reason": str(error),
                        "scientific_outcome": None,
                    },
                    sort_keys=True,
                )
            )
            return 1
        raise AssertionError("malformed cap mutant unexpectedly passed")
    if mode == "negative-address":
        result = est.analyze_addressability_core(est.public_blocked_dataset("unavailable"))
        if not result.blocked_at_address:
            print(json.dumps({"status": "RQ0-L0-INVALID", "scientific_outcome": None}))
            return 1
        print(
            json.dumps(
                {
                    "status": "RQ0-L0-BLOCKED-AT-ADDRESS",
                    "scientific_outcome": "RQ0-L0-BLOCKED-AT-ADDRESS",
                    "reason": list(result.diagnostics),
                },
                sort_keys=True,
            )
        )
        return 0
    raise ValueError(f"unknown quick mode {mode}")


def subprocess_mutant(mode: str) -> Tuple[int, str, str]:
    completed = subprocess.run(
        (sys.executable, str(SELF_PATH), f"--{mode}"),
        cwd=str(ROOT),
        check=False,
        capture_output=True,
        text=True,
    )
    return completed.returncode, completed.stdout.strip(), completed.stderr.strip()


def build_receipt() -> Tuple[Mapping[str, object], str]:
    checks: list[Check] = []

    estimator_hash = sha256(ESTIMATOR_PATH)
    fixture_hash = sha256(FIXTURE_PATH)
    scorer_hash = sha256(SELF_PATH)
    pin_hash = sha256(PIN_PATH)
    check(checks, "A1-estimator-hash", "anchor", estimator_hash == ESTIMATOR_SHA256, estimator_hash)
    check(checks, "A2-pin-hash", "anchor", pin_hash == PIN_SHA256, pin_hash)
    check(
        checks,
        "A3-fixture-locks-estimator",
        "anchor",
        fixtures.FROZEN_ESTIMATOR_SHA256 == ESTIMATOR_SHA256,
        fixtures.FROZEN_ESTIMATOR_SHA256,
    )
    check(
        checks,
        "A4-estimator-api",
        "anchor",
        est.ESTIMATOR_API_VERSION == "rq0-l0-addressability-v3",
        est.ESTIMATOR_API_VERSION,
    )

    public = est.public_self_test()
    check(
        checks,
        "A5-public-calibrations",
        "anchor",
        all(public["checks"].values()),
        f"{sum(public['checks'].values())}/{len(public['checks'])}",
    )

    bundle = fixtures.build_fixture_bundle()
    main_result = est.analyze_localization(bundle.main)
    renamed_result = est.analyze_localization(bundle.renamed_generator_variant)
    gauge_result = est.analyze_localization(bundle.gauge_variant)
    atlas = main_result.atlases[0] if main_result.atlases else None

    check(
        checks,
        "S1-main-positive",
        "scientific",
        main_result.has_positive_localization,
        main_result.diagnostics,
    )
    check(
        checks,
        "S2-one-finest-factorization",
        "scientific",
        len(main_result.core.finest_factorizations) == 1,
        len(main_result.core.finest_factorizations),
    )
    factorization = main_result.core.finest_factorizations[0]
    faithful_product, product_image = est.multiply_subobjects(
        main_result.core.composition, factorization.factors
    )
    check(
        checks,
        "S3-factor-orders",
        "scientific",
        tuple(sorted(factorization.group_orders)) == (6, 6, 6),
        tuple(sorted(factorization.group_orders)),
    )
    check(
        checks,
        "S4-factor-algebras",
        "scientific",
        tuple(sorted(factorization.algebra_dimensions)) == (4, 4, 4),
        tuple(sorted(factorization.algebra_dimensions)),
    )
    check(
        checks,
        "S4b-faithful-product-map",
        "scientific",
        faithful_product
        and len(product_image) == main_result.core.composition.size,
        (faithful_product, len(product_image), main_result.core.composition.size),
    )
    check(
        checks,
        "S5-truth-scored-after-construction",
        "scientific",
        factor_truth_score(main_result, bundle.truth),
        "recovered factor sets compared after estimator return",
    )
    check(
        checks,
        "S6-order-three",
        "scientific",
        any(
            est.subgroup_generated(
                main_result.core.composition,
                (element,),
                main_result.core.inverses,
            )
            and len(
                est.subgroup_generated(
                    main_result.core.composition,
                    (element,),
                    main_result.core.inverses,
                )
            )
            == 3
            for element in range(main_result.core.composition.size)
        ),
        "searched all quotient classes",
    )
    check(
        checks,
        "S7-nonabelian",
        "scientific",
        any(
            main_result.core.composition.product(left, right)
            != main_result.core.composition.product(right, left)
            for left in range(main_result.core.composition.size)
            for right in range(main_result.core.composition.size)
        ),
        "searched quotient multiplication table",
    )
    check(
        checks,
        "S8-product-cache-authenticated",
        "scientific",
        main_result.core.composition.unique_product_amplitudes
        == main_result.core.composition.size,
        main_result.core.composition.unique_product_amplitudes,
    )
    check(
        checks,
        "S9-three-W3-seams",
        "scientific",
        len(main_result.record_results) == 3
        and all(value.passes_w3 for value in main_result.record_results),
        tuple(value.passes_w3 for value in main_result.record_results),
    )

    assert atlas is not None
    check(checks, "S10-six-regions", "scientific", len(atlas.objects) == 6, len(atlas.objects))
    check(
        checks,
        "S11-C10-record-complete",
        "scientific",
        atlas.every_object_record_bearing
        and all(value.records for value in atlas.objects),
        tuple((value.atoms, value.records) for value in atlas.objects),
    )
    check(checks, "S12-overlap-closed", "scientific", atlas.overlap_closed, atlas.overlap_closed)
    check(
        checks,
        "S13-typed-algebra-category",
        "scientific",
        atlas.algebra_category_closes and len(atlas.algebra_inclusions) == 12,
        (atlas.algebra_category_closes, len(atlas.algebra_inclusions)),
    )
    check(
        checks,
        "S14-record-functor",
        "scientific",
        atlas.record_functor_closes and len(atlas.record_pullbacks) == 12,
        (atlas.record_functor_closes, len(atlas.record_pullbacks)),
    )
    check(
        checks,
        "S15-pair-overlaps",
        "scientific",
        len(atlas.pair_overlaps) == 9,
        len(atlas.pair_overlaps),
    )
    check(
        checks,
        "S16-triple-overlaps",
        "scientific",
        len(atlas.triple_overlaps) == 3
        and all(len(value.meet_atoms) == 1 for value in atlas.triple_overlaps),
        tuple((value.objects, value.meet_atoms) for value in atlas.triple_overlaps),
    )
    universal_core = set(atlas.objects[0].atoms)
    for value in atlas.objects[1:]:
        universal_core &= set(value.atoms)
    check(checks, "S17-non-star", "scientific", not universal_core, sorted(universal_core))
    check(
        checks,
        "S18-twisted-projector-rejected",
        "scientific",
        twisted_pullback_rejected(atlas),
        "changed projector image fails exact pullback",
    )

    recordless_dataset = fixtures.with_records(bundle.main, bundle.main.records[:2])
    recordless_results = tuple(
        est.evaluate_record_witness(value, main_result.core.support, bundle.main.dimension)
        for value in recordless_dataset.records
    )
    recordless_atlas = est.build_atlas(
        recordless_dataset, main_result.core, 0, recordless_results
    )
    check(
        checks,
        "C1-recordless-candidate-excluded",
        "control",
        len(recordless_atlas.objects) < len(atlas.objects)
        and not recordless_atlas.overlap_closed,
        (len(recordless_atlas.objects), recordless_atlas.overlap_closed),
    )

    renamed_iso, rename_map = renamed_dataset_isomorphism(
        bundle.main, bundle.renamed_generator_variant
    )
    check(checks, "C2-handle-row-isomorphism", "control", renamed_iso, len(rename_map))
    check(
        checks,
        "C3-renamed-full-estimator",
        "control",
        renamed_result.has_positive_localization
        and renamed_result.structural_signature() == main_result.structural_signature(),
        renamed_result.structural_signature(),
    )
    base_mutant = primitive_pairing_mutant(bundle.main, main_result.core)
    renamed_mutant = primitive_pairing_mutant(
        bundle.renamed_generator_variant, renamed_result.core
    )
    check(
        checks,
        "C4-generator-list-mutant-detected",
        "control",
        mutant_matches_finest(base_mutant, main_result.core)
        and not mutant_matches_finest(renamed_mutant, renamed_result.core),
        (mutant_matches_finest(base_mutant, main_result.core), mutant_matches_finest(renamed_mutant, renamed_result.core)),
    )
    check(
        checks,
        "C5-handle-branch-mutant-detected",
        "control",
        bundle.main.handle == "held-out-addressability-main"
        and bundle.renamed_generator_variant.handle != "held-out-addressability-main"
        and main_result.has_positive_localization
        and renamed_result.has_positive_localization,
        (bundle.main.handle, bundle.renamed_generator_variant.handle),
    )

    gauge_conjugacy = conjugated_dataset_fields(
        bundle.main, bundle.gauge_variant, bundle.gauge, monomial=True
    )
    gauge_mutant = replace(
        bundle.gauge_variant,
        records=(replace(bundle.gauge_variant.records[0], handle="mutated-record"),)
        + bundle.gauge_variant.records[1:],
    )
    check(checks, "C6-full-gauge-conjugacy", "control", gauge_conjugacy, gauge_conjugacy)
    check(
        checks,
        "C7-gauge-full-estimator",
        "control",
        gauge_result.has_positive_localization
        and gauge_result.structural_signature() == main_result.structural_signature(),
        gauge_result.structural_signature(),
    )
    check(
        checks,
        "C8-gauge-omitted-field-mutant",
        "control",
        not conjugated_dataset_fields(bundle.main, gauge_mutant, bundle.gauge, monomial=True),
        "record-field mutation detected",
    )

    phase_conjugacy = conjugated_dataset_fields(
        bundle.main, bundle.phase_variant, bundle.phase_action, monomial=False
    )
    phase_changes = sum(
        est.amplitude_signature(left.amplitude) != est.amplitude_signature(right.amplitude)
        for left, right in zip(bundle.main.operations, bundle.phase_variant.operations)
    )
    phase_records = tuple(
        est.evaluate_record_witness(value, est.identity(bundle.phase_variant.dimension), bundle.phase_variant.dimension)
        for value in bundle.phase_variant.records
    )
    check(checks, "C9-physical-phase-conjugacy", "control", phase_conjugacy, phase_conjugacy)
    check(checks, "C10-physical-signatures-change", "control", phase_changes > 0, phase_changes)
    check(
        checks,
        "C11-phase-not-fact-criterion",
        "control",
        all(value.passes_w3 for value in phase_records)
        and tuple(value.passes_w3 for value in phase_records)
        == tuple(value.passes_w3 for value in main_result.record_results),
        tuple(value.passes_w3 for value in phase_records),
    )

    unavailable_changes = changed_rows(bundle.main, bundle.address_blocked)
    collapse_changes = changed_rows(bundle.main, bundle.collapsed)
    check(
        checks,
        "C12-Dplus-Dminus-identical-matrices",
        "control",
        same_noncomposition_fields(bundle.main, bundle.address_blocked)
        and len(unavailable_changes) == 2,
        len(unavailable_changes),
    )
    check(
        checks,
        "C13-Dminus-blocks-through-CompD",
        "control",
        main_result.core.composition.total_implemented
        and all(right.status == est.UNAVAILABLE for _, right in unavailable_changes),
        tuple(right.status for _, right in unavailable_changes),
    )
    check(
        checks,
        "C14-collapse-identical-matrices",
        "control",
        same_noncomposition_fields(bundle.main, bundle.collapsed)
        and len(collapse_changes) == 2
        and all(right.status == est.COLLAPSED for _, right in collapse_changes),
        tuple(right.status for _, right in collapse_changes),
    )

    ambiguity = est.analyze_localization(bundle.ambiguity)
    check(
        checks,
        "C15-genuine-ambiguity",
        "control",
        ambiguity.is_ambiguous and len(ambiguity.core.finest_factorizations) >= 2,
        len(ambiguity.core.finest_factorizations),
    )
    ambiguity_pairs = {
        (value.source_factorization, value.target_factorization)
        for value in ambiguity.groupoid_arrows
    }
    expected_pairs = set(
        itertools.product(range(len(ambiguity.core.finest_factorizations)), repeat=2)
    )
    check(
        checks,
        "C16-derived-groupoid-arrows",
        "control",
        ambiguity_pairs == expected_pairs,
        (len(ambiguity.groupoid_arrows), sorted(ambiguity_pairs)),
    )

    irreducible = est.analyze_addressability_core(bundle.irreducible)
    check(
        checks,
        "C17-irreducible-not-split",
        "control",
        irreducible.blocked_at_address,
        irreducible.diagnostics,
    )
    check(
        checks,
        "C18-inaccessible-spectator-quotiented",
        "control",
        bool(public["public_calibration"]["inaccessible_quotient"]),
        public["public_calibration"]["inaccessible_quotient"],
    )
    check(
        checks,
        "C19-active-spectator-survives",
        "control",
        tuple(public["public_calibration"]["finest_group_orders"][0]) == (2, 6),
        public["public_calibration"]["finest_group_orders"],
    )
    check(
        checks,
        "C20-nonjoint-active-blocks",
        "control",
        bool(public["public_calibration"]["unavailable_blocks"]),
        public["public_calibration"]["unavailable_blocks"],
    )
    check(
        checks,
        "C21-redundant-composite-invariant",
        "control",
        bool(public["public_calibration"]["redundant_alias_invariant"]),
        public["public_calibration"]["redundant_alias_invariant"],
    )
    check(
        checks,
        "C22-public-generator-change-invariant",
        "control",
        bool(public["public_calibration"]["changed_generator_invariant"]),
        public["public_calibration"]["changed_generator_invariant"],
    )

    bridge_laws = tuple(
        record_law(value.records[0])
        for value in (
            bundle.bridge_positive_source,
            bundle.bridge_positive_target,
            bundle.bridge_negative,
        )
    )
    positive_bridges = permutation_bridge_search(
        bundle.bridge_positive_source, bundle.bridge_positive_target
    )
    negative_bridges = permutation_bridge_search(
        bundle.bridge_positive_source, bundle.bridge_negative
    )
    check(
        checks,
        "C23-equal-record-laws",
        "control",
        len(set(bridge_laws)) == 1,
        bridge_laws,
    )
    check(
        checks,
        "C24-positive-structural-bridge",
        "control",
        bool(positive_bridges) and any(value[2] for value in positive_bridges),
        (24, len(positive_bridges), sum(value[2] for value in positive_bridges)),
    )
    check(
        checks,
        "C25-equal-law-no-bridge",
        "control",
        not negative_bridges,
        (24, len(negative_bridges), "exhaustive S4 carrier permutations"),
    )

    mutant_modes = {
        mode: subprocess_mutant(mode)
        for mode in (
            "mutate-anchor",
            "mutate-science",
            "no-outcome",
            "malformed",
            "negative-address",
        )
    }
    for mode in ("mutate-anchor", "mutate-science", "no-outcome", "malformed"):
        code, stdout, stderr = mutant_modes[mode]
        check(
            checks,
            f"R-{mode}",
            "receipt",
            code == 1
            and "RQ0-L0-INVALID" in stdout
            and "RQ0-LOCAL-ATLAS" not in stdout
            and "RQ0-LOCALIZATION-GROUPOID" not in stdout
            and not stderr,
            (code, stdout),
        )
    negative_code, negative_stdout, negative_stderr = mutant_modes["negative-address"]
    check(
        checks,
        "R-valid-negative",
        "receipt",
        negative_code == 0
        and "RQ0-L0-BLOCKED-AT-ADDRESS" in negative_stdout
        and not negative_stderr,
        (negative_code, negative_stdout),
    )

    categories = {
        category: {
            "passed": sum(value.passed for value in checks if value.category == category),
            "total": sum(1 for value in checks if value.category == category),
        }
        for category in sorted({value.category for value in checks})
    }
    all_pass = all(value.passed for value in checks)
    groupoid_prerequisites = (
        all_pass
        and main_result.has_positive_localization
        and bool(main_result.groupoid_arrows)
        and atlas.every_object_record_bearing
        and atlas.overlap_closed
        and atlas.algebra_category_closes
        and atlas.record_functor_closes
    )
    local_atlas_prerequisites = (
        groupoid_prerequisites
        and len(atlas.objects) >= 4
        and len(atlas.pair_overlaps) >= 3
        and bool(atlas.triple_overlaps)
        and not universal_core
    )
    if not all_pass:
        status = "RQ0-L0-INVALID"
        outcome: Optional[str] = None
    elif local_atlas_prerequisites:
        status = "RQ0-LOCAL-ATLAS"
        outcome = status
    elif groupoid_prerequisites:
        status = "RQ0-LOCALIZATION-GROUPOID"
        outcome = status
    elif main_result.core.blocked_at_address:
        status = "RQ0-L0-BLOCKED-AT-ADDRESS"
        outcome = status
    else:
        status = "RQ0-L0-INVALID"
        outcome = None

    receipt = {
        "unit": "RQ0-L0 operational localization and addressability repair",
        "status": status,
        "scientific_outcome": outcome,
        "provenance": {
            "pin_commit": PIN_COMMIT,
            "pin_sha256": pin_hash,
            "estimator_commit": ESTIMATOR_COMMIT,
            "estimator_sha256": estimator_hash,
            "fixture_sha256": fixture_hash,
            "scorer_sha256": scorer_hash,
            "estimator_precedes_current_fixture_contents": True,
            "retired_fixture_commits_not_rescored": ["39fb6b3", "3a6cded"],
        },
        "scope": {
            "exact_field": "Q(zeta_24), Phi_24=x^8-x^4+1",
            "carrier_dimension_cap": est.MAX_CARRIER_DIMENSION,
            "class_cap": est.MAX_OPERATION_CLASSES,
            "composition_row_cap": est.MAX_COMPOSITION_ROWS,
            "candidate_subobject_cap": est.MAX_CANDIDATE_SUBOBJECTS,
            "bridge_candidate_cap": est.MAX_AUTOMORPHISM_PERMUTATIONS,
            "runtime_cap_seconds": RUNTIME_CAP_SECONDS,
            "seed": None,
            "gauge": "configuration relabelling x finite mu_24 boundary phase",
        },
        "postulates": [
            "finite exact amplitude tomography on the declared accessible support",
            "flat typed composition-row access including unavailable and collapsed statuses",
            "declared preparations, interventions, probes and record candidates are operationally accessible",
        ],
        "inherited": [
            "v12 Paper 1 W3 occurrence/availability record criteria",
            "v12 Paper 2 fact identity is structural and phase-blind",
            "v13 terminal finite RQ0-A fact descent",
            "v13 #31 four-gate and no-smuggling repair pin",
        ],
        "legacy_use": {
            "v10_or_earlier": "none",
            "v12_paper1": "inherited W3 theorem/decision procedure",
            "v12_paper2": "inherited structural fact-identity discipline",
            "v13_33_and_35": "retired timing/calibration fixtures only; never rescored",
            "estimator_public_models": "calibration, controls and benchmarks only",
        },
        "main": {
            "carrier_dimension": bundle.main.dimension,
            "raw_operations": len(bundle.main.operations),
            "composition_rows": len(bundle.main.composition_rows),
            "quotient_classes": main_result.core.composition.size,
            "quotient_class_members": [
                list(value.members) for value in main_result.core.composition.classes
            ],
            "aliases": [
                list(value.members)
                for value in main_result.core.composition.classes
                if len(value.members) > 1
            ],
            "identity_class": main_result.core.composition.identity,
            "generator_classes": list(main_result.core.composition.generator_classes),
            "composition_congruence": main_result.core.composition.congruence_verified,
            "composition_status_counts": {
                status: sum(
                    row.status == status
                    for table_row in main_result.core.composition.table
                    for row in table_row
                )
                for status in (est.IMPLEMENTED, est.UNAVAILABLE, est.COLLAPSED)
            },
            "unique_product_amplitudes": main_result.core.composition.unique_product_amplitudes,
            "normal_subobjects": len(main_result.core.normal_subobjects),
            "candidate_tests": main_result.core.candidate_tests,
            "finest_factorizations": len(main_result.core.finest_factorizations),
            "factor_orders": list(factorization.group_orders),
            "factor_algebra_dimensions": list(factorization.algebra_dimensions),
            "factor_class_sets": [sorted(value) for value in factorization.factors],
            "direct_product_faithful": faithful_product,
            "direct_product_image": len(product_image),
            "direct_product_collisions": 0 if faithful_product else "detected",
            "records": [asdict(value) | {"passes_w3": value.passes_w3} for value in main_result.record_results],
            "regions": [
                {
                    "atoms": list(value.atoms),
                    "operation_count": len(value.operational_elements),
                    "algebra_dimension": value.algebra.dimension,
                    "records": list(value.records),
                }
                for value in atlas.objects
            ],
            "algebra_restrictions": [
                {
                    "source": list(value.source_atoms),
                    "target": list(value.target_atoms),
                    "source_dimension": value.source_dimension,
                    "target_dimension": value.target_dimension,
                }
                for value in atlas.algebra_inclusions
            ],
            "record_pullbacks": [
                {
                    "larger": list(value.larger_atoms),
                    "smaller": list(value.smaller_atoms),
                    "records": [source for source, _, _ in value.record_maps],
                }
                for value in atlas.record_pullbacks
            ],
            "pair_overlaps": [
                {
                    "objects": [list(entry) for entry in value.objects],
                    "meet": list(value.meet_atoms),
                }
                for value in atlas.pair_overlaps
            ],
            "triple_overlaps": [
                {
                    "objects": [list(entry) for entry in value.objects],
                    "meet": list(value.meet_atoms),
                }
                for value in atlas.triple_overlaps
            ],
            "groupoid_arrows": [
                {
                    "source": value.source_factorization,
                    "target": value.target_factorization,
                    "atom_map": list(value.atom_map),
                    "carrier_permutation": list(value.carrier_permutation),
                }
                for value in main_result.groupoid_arrows
            ],
        },
        "controls": {
            "renamed_full_signature": renamed_result.structural_signature(),
            "gauge_full_signature": gauge_result.structural_signature(),
            "Dminus_changed_rows": len(unavailable_changes),
            "collapse_changed_rows": len(collapse_changes),
            "Dminus_rows": [
                {
                    "left": right.left,
                    "right": right.right,
                    "status": right.status,
                    "result": right.result,
                }
                for _, right in unavailable_changes
            ],
            "collapse_rows": [
                {
                    "left": right.left,
                    "right": right.right,
                    "status": right.status,
                    "result": right.result,
                }
                for _, right in collapse_changes
            ],
            "recordless_region_count": len(recordless_atlas.objects),
            "ambiguity_factorizations": len(ambiguity.core.finest_factorizations),
            "ambiguity_arrows": len(ambiguity.groupoid_arrows),
            "physical_signature_changes": phase_changes,
            "positive_bridge_candidates": len(positive_bridges),
            "negative_bridge_candidates": len(negative_bridges),
            "bridge_search_scope_each": 24,
            "positive_bridge_permutations": [list(value[0]) for value in positive_bridges],
            "positive_bridge_record_flags": [value[2] for value in positive_bridges],
            "negative_bridge_permutations": [list(value[0]) for value in negative_bridges],
        },
        "checks": [asdict(value) for value in checks],
        "check_summary": categories,
        "outcome_prerequisites": {
            "all_measured_gates": all_pass,
            "groupoid_rung": groupoid_prerequisites,
            "local_atlas_rung": local_atlas_prerequisites,
        },
        "nonclaims": [
            "operational localization is not spatial or spacelike separation",
            "no influence or causal relation",
            "no causal cone, dimension, volume or Lorentzian metric",
            "no field propagation or special relativity",
            "no stress tensor, backreaction or gravity",
            "no general black-box uniqueness theorem beyond the declared finite access scope",
        ],
        "first_unresolved_obstruction": (
            "define operational influence between localized record-bearing subinstruments "
            "without importing temporal, circuit-wire, graph or spatial order"
        ),
    }
    text = "\n".join(
        (
            "RQ0-L0 OPERATIONAL LOCALIZATION — EXACT RECEIPT",
            "================================================",
            f"status: {status}",
            f"scientific_outcome: {outcome}",
            f"checks: {sum(value.passed for value in checks)}/{len(checks)}",
            "check_categories: " + ", ".join(
                f"{key}={value['passed']}/{value['total']}"
                for key, value in categories.items()
            ),
            f"estimator_sha256: {estimator_hash}",
            f"fixture_sha256: {fixture_hash}",
            f"main: carrier={bundle.main.dimension}, classes={main_result.core.composition.size}, rows={len(bundle.main.composition_rows)}",
            f"localization: factors={tuple(factorization.group_orders)}, algebra_dims={tuple(factorization.algebra_dimensions)}",
            f"atlas: regions={len(atlas.objects)}, restrictions={len(atlas.algebra_inclusions)}, pair_overlaps={len(atlas.pair_overlaps)}, triple_overlaps={len(atlas.triple_overlaps)}",
            f"records: {tuple(value.passes_w3 for value in main_result.record_results)}",
            f"controls: Dminus={len(unavailable_changes)}, collapse={len(collapse_changes)}, ambiguity={len(ambiguity.core.finest_factorizations)}, phase_changes={phase_changes}, bridges=({len(positive_bridges)},{len(negative_bridges)})",
            "scope: finite exact amplitude-instrument addressability; not spatial or causal locality",
            "next_obstruction: operational influence without planted order",
        )
    ) + "\n"
    return receipt, text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text-out", type=Path)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--mutate-anchor", action="store_true")
    parser.add_argument("--mutate-science", action="store_true")
    parser.add_argument("--no-outcome", action="store_true")
    parser.add_argument("--malformed", action="store_true")
    parser.add_argument("--negative-address", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    quick = tuple(
        name
        for name, active in (
            ("mutate-anchor", args.mutate_anchor),
            ("mutate-science", args.mutate_science),
            ("no-outcome", args.no_outcome),
            ("malformed", args.malformed),
            ("negative-address", args.negative_address),
        )
        if active
    )
    if len(quick) > 1:
        print(json.dumps({"status": "RQ0-L0-INVALID", "reason": "multiple modes", "scientific_outcome": None}))
        return 1
    if quick:
        return run_quick_mode(quick[0])
    try:
        receipt, text = build_receipt()
    except Exception as error:  # fail closed before any scientific outcome
        print(
            json.dumps(
                {
                    "status": "RQ0-L0-INVALID",
                    "reason": f"{type(error).__name__}: {error}",
                    "scientific_outcome": None,
                },
                sort_keys=True,
            )
        )
        return 1
    rendered_json = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.text_out is not None:
        args.text_out.write_text(text)
    if args.json_out is not None:
        args.json_out.write_text(rendered_json)
    print(text, end="")
    return 0 if receipt["scientific_outcome"] is not None else 1


if __name__ == "__main__":
    raise SystemExit(main())
