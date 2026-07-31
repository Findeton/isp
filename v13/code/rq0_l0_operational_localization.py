#!/usr/bin/env python3
"""Exact scorer and receipt generator for v13 RQ0-L0.

The localization estimator imported here was committed and frozen before the
fixture/truth module existed.  This runner may inspect fixture truth solely for
held-out scoring.  It constructs no influence, causal, geometric, field, or
gravity object.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Optional, Sequence, Tuple

import rq0_l0_fixtures_exact as fixtures
import rq0_l0_localization_estimator_exact as estimator


ROOT = Path(__file__).resolve().parents[2]
ESTIMATOR_PATH = ROOT / "v13/code/rq0_l0_localization_estimator_exact.py"
FIXTURE_PATH = ROOT / "v13/code/rq0_l0_fixtures_exact.py"
RUNNER_PATH = Path(__file__).resolve()
ESTIMATOR_COMMIT = "a5b71735fb80d7214e1cc4e5a389289572895d53"
RUNTIME_CAP_NS = 240_000_000_000

LOCKS = {
    "active L0 pin": (
        "v13/note-rq0-operational-localization-pin.md",
        "02ed47ad0a294741e613639b02066797a2057fcfcd816edd81203f353b1f9a59",
    ),
    "frozen L0 estimator": (
        "v13/code/rq0_l0_localization_estimator_exact.py",
        "0b8d90bad735f6574ee367dd0bf7e98bcc1c6f2854f7a12070c82bae84e063b8",
    ),
    "Paper 1": (
        "v12/paper1-composition-defect.md",
        "81bdab5673fb67b63cd10c08fbb80870f8aa01088047718c5b4bf447e1669128",
    ),
    "Paper 2": (
        "v12/paper2-record-coreference.md",
        "d6af0e6513fc7088407dc5a26c513ecc4e9e45b5a5ae71ffa8a9571f274ad670",
    ),
    "terminal RQ0-A note": (
        "v13/note-rq0-physical-overlap-repair.md",
        "cadc7953004f7124160f325929d05fe651f18182a00df1ffd48652eab025546f",
    ),
    "terminal RQ0-A executable": (
        "v13/code/rq0_physical_overlap_exact.py",
        "56781c9a10c65be076d86570abd87cbde0901ecc09df2aa04586b30ff31d08d6",
    ),
    "terminal RQ0-A text receipt": (
        "v13/code/rq0_physical_overlap_output.txt",
        "0b8f97ef8716a2d69c5ae5d8c80d5836523914effcc997fb755c09483751a460",
    ),
    "terminal RQ0-A JSON receipt": (
        "v13/code/rq0_physical_overlap_receipt.json",
        "fff8c4d633a8e3b1c43db0645305fb02deb763f15db139f7b5ce25bf0f8b375a",
    ),
    "Paper 0 v0.3": (
        "v13/relativistic-isp-v13-paper0-gravity.md",
        "501c0bb2db3f8448fdc4a07acd2188491f88b12a9d491d19add97bd3208bcbc1",
    ),
}

CHECK_CLASSES = {
    "anchor",
    "authentication",
    "static_audit",
    "type_check",
    "exact_measurement",
    "control",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: Sequence[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        tuple(command),
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def normalize(value: object) -> object:
    if isinstance(value, estimator.Q8):
        return value.render()
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, frozenset):
        return sorted(normalize(entry) for entry in value)
    if isinstance(value, set):
        return sorted(normalize(entry) for entry in value)
    if isinstance(value, tuple):
        return [normalize(entry) for entry in value]
    if isinstance(value, list):
        return [normalize(entry) for entry in value]
    if isinstance(value, dict):
        return {str(key): normalize(entry) for key, entry in value.items()}
    return value


@dataclass(frozen=True)
class CheckRow:
    key: str
    group: str
    classification: str
    description: str
    observed: object
    expected: object
    passed: bool

    def to_data(self) -> Mapping[str, object]:
        return {
            "key": self.key,
            "group": self.group,
            "classification": self.classification,
            "description": self.description,
            "observed": normalize(self.observed),
            "expected": normalize(self.expected),
            "passed": self.passed,
        }


class CheckLedger:
    def __init__(self) -> None:
        self.rows: list[CheckRow] = []

    def add(
        self,
        key: str,
        group: str,
        classification: str,
        description: str,
        observed: object,
        expected: object,
    ) -> None:
        if any(row.key == key for row in self.rows):
            raise AssertionError(f"duplicate check key {key}")
        if classification not in CHECK_CLASSES:
            raise AssertionError(f"unclassified check {key}: {classification}")
        self.rows.append(
            CheckRow(
                key=key,
                group=group,
                classification=classification,
                description=description,
                observed=observed,
                expected=expected,
                passed=observed == expected,
            )
        )

    def add_true(
        self,
        key: str,
        group: str,
        classification: str,
        description: str,
        observed: object,
    ) -> None:
        self.add(key, group, classification, description, bool(observed), True)

    def passed(self, key: str) -> bool:
        return next(row.passed for row in self.rows if row.key == key)

    def group_passes(self, group: str) -> bool:
        rows = tuple(row for row in self.rows if row.group == group)
        return bool(rows) and all(row.passed for row in rows)


@dataclass(frozen=True)
class LocalRestriction:
    source_object: int
    target_object: int
    source_atoms: frozenset[int]
    target_atoms: frozenset[int]


@dataclass(frozen=True)
class RecordRestriction:
    source_object: int
    target_object: int
    record_handle: str
    map_type: str = "identity pullback of one frozen projector family"


def build_restriction_categories(
    truth_regions: Sequence[frozenset[int]],
    object_records: Sequence[frozenset[str]],
) -> Tuple[Tuple[LocalRestriction, ...], Tuple[RecordRestriction, ...]]:
    local_arrows = []
    record_arrows = []
    for source_index, source in enumerate(truth_regions):
        for target_index, target in enumerate(truth_regions):
            if not target <= source:
                continue
            local_arrows.append(
                LocalRestriction(source_index, target_index, source, target)
            )
            for handle in sorted(object_records[target_index]):
                if handle in object_records[source_index]:
                    record_arrows.append(
                        RecordRestriction(source_index, target_index, handle)
                    )
    return tuple(local_arrows), tuple(record_arrows)


def restriction_composition_closes(arrows: Sequence[LocalRestriction]) -> bool:
    arrow_pairs = {(value.source_object, value.target_object) for value in arrows}
    return all(
        (left.source_object, right.target_object) in arrow_pairs
        for left in arrows
        for right in arrows
        if left.target_object == right.source_object
    )


def imports_from_ast(path: Path) -> Tuple[str, ...]:
    tree = ast.parse(path.read_text())
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    return tuple(sorted(imports))


def float_literals(path: Path) -> Tuple[object, ...]:
    tree = ast.parse(path.read_text())
    return tuple(
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    )


def estimator_truth_import_violation(source: str) -> bool:
    tree = ast.parse(source)
    forbidden_fragments = ("fixture", "scorer", "operational_localization")
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = tuple(alias.name.lower() for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names = ((node.module or "").lower(),)
        else:
            continue
        if any(fragment in name for name in names for fragment in forbidden_fragments):
            return True
    return False


def operation_map(dataset: estimator.OperationalDataset) -> Mapping[str, estimator.Matrix]:
    return {value.handle: value.amplitude for value in dataset.interventions}


def probe_map(dataset: estimator.OperationalDataset) -> Mapping[str, estimator.Vector]:
    return {value.handle: value.state for value in dataset.probes}


def context_map(dataset: estimator.OperationalDataset) -> Mapping[str, estimator.Context]:
    return {value.handle: value for value in dataset.contexts}


def record_map(dataset: estimator.OperationalDataset) -> Mapping[str, estimator.RecordWitness]:
    return {value.handle: value for value in dataset.records}


def record_equal(left: estimator.RecordWitness, right: estimator.RecordWitness) -> bool:
    return left == right


def dataset_is_exact_conjugate(
    source: estimator.OperationalDataset,
    target: estimator.OperationalDataset,
    action: estimator.Matrix,
) -> bool:
    source_operations = operation_map(source)
    target_operations = operation_map(target)
    if set(source_operations) != set(target_operations):
        return False
    if any(
        estimator.conjugate_by(action, source_operations[handle])
        != target_operations[handle]
        for handle in source_operations
    ):
        return False
    expected_preparations = {
        tuple(entry.sort_key() for entry in estimator.mv(action, value))
        for value in source.preparations
    }
    observed_preparations = {
        tuple(entry.sort_key() for entry in value)
        for value in target.preparations
    }
    if expected_preparations != observed_preparations:
        return False
    source_probes = probe_map(source)
    target_probes = probe_map(target)
    if set(source_probes) != set(target_probes):
        return False
    if any(
        estimator.mv(action, source_probes[handle]) != target_probes[handle]
        for handle in source_probes
    ):
        return False
    source_contexts = context_map(source)
    target_contexts = context_map(target)
    if set(source_contexts) != set(target_contexts):
        return False
    for handle, value in source_contexts.items():
        target_value = target_contexts[handle]
        if (
            estimator.conjugate_by(action, value.before) != target_value.before
            or estimator.conjugate_by(action, value.after) != target_value.after
        ):
            return False
    source_records = record_map(source)
    target_records = record_map(target)
    if set(source_records) != set(target_records):
        return False
    return all(
        record_equal(fixtures.conjugate_record(value, action), target_records[handle])
        for handle, value in source_records.items()
    )


def algebra_for_handles(
    dataset: estimator.OperationalDataset,
    handles: Iterable[str],
) -> estimator.AlgebraBasis:
    selected = frozenset(handles)
    operations = tuple(
        value.amplitude for value in dataset.interventions if value.handle in selected
    )
    if not operations:
        raise AssertionError("empty hidden scoring block")
    return estimator.generated_star_algebra(
        operations,
        estimator.identity(dataset.dimension),
        dataset.dimension * dataset.dimension,
    )


def recovered_truth_map(
    result: estimator.LocalizationResult,
    truth: fixtures.LocalizationTruth,
) -> Tuple[int, ...]:
    if len(result.finest_factorizations) != 1:
        return ()
    factorization = result.finest_factorizations[0]
    mapping = []
    for block in factorization.blocks:
        handles = frozenset(
            handle
            for class_index in block
            for handle in result.intervention_classes[class_index].members
        )
        if handles not in truth.atom_handles:
            return ()
        mapping.append(truth.atom_handles.index(handles))
    return tuple(mapping)


def local_truth_sets(
    result: estimator.LocalizationResult,
    atom_map: Sequence[int],
) -> Tuple[frozenset[int], ...]:
    if not result.lattices:
        return ()
    return tuple(
        frozenset(atom_map[index] for index in value.atoms)
        for value in result.lattices[0].objects
    )


def all_proper_truth_regions(size: int) -> set[frozenset[int]]:
    return {
        frozenset(subset)
        for subset_size in range(1, size)
        for subset in itertools.combinations(range(size), subset_size)
    }


def record_attachment_truth(
    region: frozenset[int],
    truth: fixtures.LocalizationTruth,
) -> frozenset[str]:
    return frozenset(
        handle for handle, pair in truth.record_pairs.items() if pair <= region
    )


def class_signature_by_handle(
    result: estimator.LocalizationResult,
) -> Mapping[str, Tuple[estimator.Q8, ...]]:
    return {
        handle: value.signature
        for value in result.intervention_classes
        for handle in value.members
    }


def check_anchor_commit_blob() -> str:
    completed = run(
        (
            "git",
            "show",
            f"{ESTIMATOR_COMMIT}:v13/code/rq0_l0_localization_estimator_exact.py",
        )
    )
    if completed.returncode != 0:
        return "GIT-SHOW-FAILED"
    return hashlib.sha256(completed.stdout).hexdigest()


def build_receipt(mutate_anchor: bool = False) -> Mapping[str, object]:
    start_ns = time.monotonic_ns()
    checks = CheckLedger()

    observed_locks = {}
    for label, (relative, expected) in LOCKS.items():
        observed = sha256(ROOT / relative)
        if mutate_anchor and label == "frozen L0 estimator":
            observed = "0" * 64
        observed_locks[label] = observed
        checks.add(
            f"anchor.{label.replace(' ', '_')}",
            "anchors",
            "anchor",
            f"{label} SHA-256",
            observed,
            expected,
        )
    checks.add(
        "anchor.estimator_commit_blob",
        "anchors",
        "anchor",
        "the immutable estimator commit contains the frozen source bytes",
        check_anchor_commit_blob(),
        LOCKS["frozen L0 estimator"][1],
    )
    estimator_imports = imports_from_ast(ESTIMATOR_PATH)
    checks.add_true(
        "static.estimator_has_no_truth_import",
        "anchors",
        "static_audit",
        "the estimator imports no fixture, scorer, or delivery module",
        not estimator_truth_import_violation(ESTIMATOR_PATH.read_text()),
    )
    checks.add(
        "static.estimator_float_literals",
        "anchors",
        "static_audit",
        "the estimator substantive source has zero float literals",
        len(float_literals(ESTIMATOR_PATH)),
        0,
    )
    checks.add_true(
        "control.truth_import_mutant_detected",
        "anchors",
        "control",
        "the static detector rejects an in-memory hidden-truth import mutant",
        estimator_truth_import_violation(
            ESTIMATOR_PATH.read_text()
            + "\nfrom rq0_l0_fixtures_exact import LocalizationTruth\n"
        ),
    )

    bundle = fixtures.build_fixture_bundle()
    main_result = estimator.analyze_localization(bundle.main)
    base_small = estimator.analyze_localization(estimator.calibration_dataset())
    inaccessible_result = estimator.analyze_localization(bundle.inaccessible_extension)
    ambiguity_result = estimator.analyze_localization(bundle.ambiguity)
    irreducible_result = estimator.analyze_localization(bundle.irreducible)

    checks.add(
        "quotient.main_carrier_dimension",
        "quotient",
        "type_check",
        "the hidden main carrier respects the fixed cap",
        bundle.main.dimension,
        16,
    )
    checks.add(
        "quotient.main_access_contract",
        "quotient",
        "type_check",
        "the main access contract is frozen before operational equivalence",
        (
            len(bundle.main.preparations),
            len(bundle.main.contexts),
            len(bundle.main.probes),
            len(bundle.main.interventions),
            len(bundle.main.records),
        ),
        (48, 1, 48, 8, 6),
    )
    checks.add(
        "quotient.accessible_dimension",
        "quotient",
        "exact_measurement",
        "the main reachable operational support is full and exact",
        main_result.accessible_dimension,
        16,
    )
    checks.add(
        "quotient.intervention_classes",
        "quotient",
        "exact_measurement",
        "eight opaque handles remain eight operational classes",
        len(main_result.intervention_classes),
        8,
    )
    checks.add_true(
        "quotient.class_signatures_distinct",
        "quotient",
        "exact_measurement",
        "the frozen access contract separates all intervention classes",
        len({value.signature for value in main_result.intervention_classes}) == 8,
    )
    checks.add(
        "quotient.ambient_algebra_dimension",
        "quotient",
        "exact_measurement",
        "the opaque intervention family generates the full accessible algebra",
        main_result.ambient_algebra_dimension,
        256,
    )
    checks.add(
        "quotient.partition_census",
        "quotient",
        "exact_measurement",
        "all Bell(8) intervention partitions are examined",
        main_result.partitions_examined,
        4140,
    )
    observed_handles = frozenset(
        handle for value in main_result.intervention_classes for handle in value.members
    )
    expected_handles = frozenset(handle for block in bundle.truth.atom_handles for handle in block)
    checks.add(
        "quotient.opaque_handle_coverage",
        "quotient",
        "exact_measurement",
        "the quotient loses and invents no opaque operation handle",
        observed_handles,
        expected_handles,
    )

    atom_map = recovered_truth_map(main_result, bundle.truth)
    recovered_blocks = (
        tuple(
            frozenset(
                handle
                for class_index in block
                for handle in main_result.intervention_classes[class_index].members
            )
            for block in main_result.finest_factorizations[0].blocks
        )
        if len(main_result.finest_factorizations) == 1
        else ()
    )
    checks.add(
        "localization.valid_factorizations",
        "localization",
        "exact_measurement",
        "the exact search retains all 14 nontrivial coarsenings",
        len(main_result.valid_factorizations),
        14,
    )
    checks.add(
        "localization.finest_count",
        "localization",
        "exact_measurement",
        "one finest factorization is recovered before gauge automorphisms",
        len(main_result.finest_factorizations),
        1,
    )
    checks.add(
        "localization.hidden_atom_match",
        "localization",
        "control",
        "held-out scoring matches recovered opaque blocks to all four hidden atoms",
        set(recovered_blocks),
        set(bundle.truth.atom_handles),
    )
    checks.add(
        "localization.atom_dimensions",
        "localization",
        "exact_measurement",
        "every recovered atomic intervention algebra has dimension four",
        tuple(sorted(main_result.finest_factorizations[0].algebra_dimensions))
        if main_result.finest_factorizations
        else (),
        (4, 4, 4, 4),
    )
    checks.add(
        "localization.atom_truth_map",
        "localization",
        "control",
        "each recovered block has a unique held-out atom referent",
        tuple(sorted(atom_map)),
        (0, 1, 2, 3),
    )

    main_atom_algebras = tuple(
        algebra_for_handles(bundle.main, handles) for handles in bundle.truth.atom_handles
    )
    visible_atom_algebras = tuple(
        algebra_for_handles(bundle.unencoded, handles) for handles in bundle.truth.atom_handles
    )
    visible_matches = tuple(
        tuple(estimator.span_equal(left, right) for right in visible_atom_algebras)
        for left in main_atom_algebras
    )
    checks.add_true(
        "localization.encoded_not_visible_slots",
        "localization",
        "control",
        "no recovered encoded atom equals a displayed unencoded slot algebra",
        all(not any(row) for row in visible_matches),
    )
    checks.add_true(
        "localization.circuit_presentations_equal",
        "localization",
        "control",
        "two different circuit words construct exactly the same encoding arrow",
        bundle.encoding_a == bundle.encoding_b,
    )
    checks.add_true(
        "localization.unencoded_to_main_conjugacy",
        "localization",
        "control",
        "the hidden encoded fixture is an exact presentation conjugate of its scoring truth",
        dataset_is_exact_conjugate(bundle.unencoded, bundle.main, bundle.encoding_a),
    )
    active_handles = bundle.truth.atom_handles[bundle.truth.active_extension_atom]
    active_algebra = algebra_for_handles(bundle.main, active_handles)
    active_operations = tuple(
        value.amplitude for value in bundle.main.interventions if value.handle in active_handles
    )
    checks.add(
        "localization.active_extension_dimension",
        "localization",
        "control",
        "the accessible independent extension survives as its own noncommutative atom",
        (
            active_algebra.dimension,
            len(active_operations),
            estimator.matrices_commute(active_operations[0], active_operations[1]),
            bundle.truth.active_extension_atom in atom_map,
        ),
        (4, 2, False, True),
    )
    checks.add(
        "localization.inaccessible_support",
        "localization",
        "control",
        "a raw eight-dimensional inaccessible completion reduces to four accessible dimensions",
        (
            bundle.inaccessible_extension.dimension,
            inaccessible_result.accessible_dimension,
        ),
        (8, 4),
    )
    checks.add(
        "localization.inaccessible_signature",
        "localization",
        "control",
        "the inaccessible completion leaves the complete localization signature unchanged",
        inaccessible_result.structural_signature(),
        base_small.structural_signature(),
    )
    checks.add(
        "localization.irreducible_control",
        "localization",
        "control",
        "the generated M4 irreducible control is not falsely localized",
        (
            irreducible_result.ambient_algebra_dimension,
            irreducible_result.has_nontrivial_localization,
        ),
        (16, False),
    )
    ambiguity_maps = tuple(sorted(value.atom_map for value in ambiguity_result.groupoid_arrows))
    checks.add(
        "localization.ambiguity_groupoid",
        "localization",
        "control",
        "the symmetric control retains identity and atom-exchange automorphisms",
        ambiguity_maps,
        ((0, 1), (1, 0)),
    )

    truth_regions = local_truth_sets(main_result, atom_map)
    expected_regions = all_proper_truth_regions(4)
    checks.add(
        "overlap.local_object_count",
        "overlap",
        "exact_measurement",
        "the recovered lattice has every nonempty proper union of four atoms",
        len(truth_regions),
        14,
    )
    checks.add(
        "overlap.local_object_truth",
        "overlap",
        "control",
        "held-out scoring recovers the complete proper-region lattice",
        set(truth_regions),
        expected_regions,
    )
    lattice = main_result.lattices[0]
    checks.add(
        "overlap.pair_count",
        "overlap",
        "exact_measurement",
        "all nonempty pair meets in the recovered lattice are retained",
        len(lattice.pair_overlaps),
        66,
    )
    checks.add(
        "overlap.triple_count",
        "overlap",
        "exact_measurement",
        "all nonempty triple meets in the recovered lattice are retained",
        len(lattice.triple_overlaps),
        134,
    )
    object_records = tuple(frozenset(value.records) for value in lattice.objects)
    expected_record_sets = tuple(
        record_attachment_truth(region, bundle.truth) for region in truth_regions
    )
    checks.add(
        "overlap.record_attachment_truth",
        "overlap",
        "control",
        "record witnesses attach exactly to operational regions containing their pair algebra",
        object_records,
        expected_record_sets,
    )
    local_restrictions, record_restrictions = build_restriction_categories(
        truth_regions, object_records
    )
    checks.add(
        "overlap.local_restriction_category",
        "overlap",
        "type_check",
        "the recovered proper-region poset has explicit identity and restriction arrows",
        (
            len(local_restrictions),
            sum(value.source_object == value.target_object for value in local_restrictions),
            restriction_composition_closes(local_restrictions),
        ),
        (50, 14, True),
    )
    local_arrow_pairs = {
        (value.source_object, value.target_object) for value in local_restrictions
    }
    pair_meet_coverage = []
    for row in lattice.pair_overlaps:
        meet_truth = truth_regions[row.objects[0]] & truth_regions[row.objects[1]]
        meet_index = truth_regions.index(meet_truth)
        pair_meet_coverage.append(
            (row.objects[0], meet_index) in local_arrow_pairs
            and (row.objects[1], meet_index) in local_arrow_pairs
        )
    checks.add_true(
        "overlap.pair_meet_restrictions",
        "overlap",
        "type_check",
        "every measured nonempty pair meet has both typed regional restriction arrows",
        all(pair_meet_coverage),
    )
    checks.add_true(
        "overlap.record_functor_restrictions",
        "overlap",
        "type_check",
        "record restrictions are defined exactly when the target witness is contained in the source",
        all(
            value.record_handle in object_records[value.source_object]
            and value.record_handle in object_records[value.target_object]
            for value in record_restrictions
        )
        and len(record_restrictions)
        == sum(
            len(object_records[target_index])
            for source_index, source in enumerate(truth_regions)
            for target_index, target in enumerate(truth_regions)
            if target <= source
        ),
    )
    record_bearing_regions = tuple(
        region for region, records in zip(truth_regions, object_records) if records
    )
    common_core = (
        frozenset.intersection(*record_bearing_regions) if record_bearing_regions else frozenset()
    )
    distinct_nonempty_pair_meets = {
        left & right
        for left, right in itertools.combinations(record_bearing_regions, 2)
        if left & right
    }
    checks.add(
        "overlap.nonstar_metrics",
        "overlap",
        "exact_measurement",
        "the record-bearing atlas has no universal atom core and several distinct overlaps",
        (
            len(record_bearing_regions),
            common_core,
            len(distinct_nonempty_pair_meets),
        ),
        (10, frozenset(), 10),
    )
    required_triple_indices = tuple(
        truth_regions.index(region) for region in bundle.truth.required_fact_triple
    )
    required_intersection = frozenset.intersection(*bundle.truth.required_fact_triple)
    required_common_records = frozenset.intersection(
        *(object_records[index] for index in required_triple_indices)
    )
    required_overlap_row = next(
        (
            row
            for row in lattice.triple_overlaps
            if frozenset(row.objects) == frozenset(required_triple_indices)
        ),
        None,
    )
    checks.add(
        "overlap.genuine_fact_triple",
        "overlap",
        "control",
        "three distinct recovered regions have a nonempty pair-sized triple meet and shared record",
        (
            required_intersection,
            required_common_records,
            None if required_overlap_row is None else required_overlap_row.algebra_dimension,
        ),
        (frozenset((0, 1)), frozenset(("w0",)), 16),
    )

    record_rows = tuple(
        (
            value.handle,
            value.occurrence,
            value.preserving_available,
            value.erasing_available,
            value.erasing_cross_coherence,
            value.no_write_occurrence,
            value.passes_w3_control,
        )
        for value in main_result.record_results
    )
    expected_record_rows = tuple(
        (f"w{index}", True, (True,), (False,), (2,), False, True)
        for index in range(6)
    )
    checks.add(
        "records.w3_rows",
        "records",
        "exact_measurement",
        "all six frozen pair records pass write/preserve/erase/no-write W3 controls",
        record_rows,
        expected_record_rows,
    )
    record_laws = tuple(fixtures.record_marginal(value) for value in bundle.main.records)
    checks.add(
        "records.fair_laws",
        "records",
        "exact_measurement",
        "all six derived record witnesses have exact fair marginals",
        record_laws,
        tuple((estimator.Q8(Fraction(1, 2)), estimator.Q8(Fraction(1, 2))) for _ in range(6)),
    )
    checks.add_true(
        "records.fact_triple_restriction",
        "records",
        "type_check",
        "the same frozen witness/projector handle restricts along all three fact-triple paths",
        required_common_records == frozenset(("w0",))
        and all("w0" in object_records[index] for index in required_triple_indices),
    )
    required_overlap_index = truth_regions.index(required_intersection)
    record_arrow_keys = {
        (value.source_object, value.target_object, value.record_handle)
        for value in record_restrictions
    }
    checks.add_true(
        "records.fact_triple_path_law",
        "records",
        "type_check",
        "all three regional paths restrict the same w0 projector family to the triple meet",
        all(
            (source_index, required_overlap_index, "w0") in record_arrow_keys
            for source_index in required_triple_indices
        ),
    )
    equal_law = fixtures.equal_law_no_bridge_control()
    checks.add(
        "records.equal_law_control",
        "records",
        "control",
        "matching record marginals do not remove a typed carrier obstruction",
        (
            equal_law["left_law"] == equal_law["right_law"],
            equal_law["bridge_exists"],
            equal_law["obstruction"],
        ),
        (True, False, "boundary_dimension_mismatch:4->8"),
    )

    checks.add_true(
        "controls.gauge_dataset_conjugacy",
        "controls",
        "control",
        "configuration relabelling, mu_8 phase, and access reordering preserve the exact process",
        dataset_is_exact_conjugate(bundle.main, bundle.gauge_variant, bundle.gauge_action),
    )
    gauge_block_checks = []
    for handles, main_algebra in zip(bundle.truth.atom_handles, main_atom_algebras):
        gauge_algebra = algebra_for_handles(bundle.gauge_variant, handles)
        gauge_block_checks.append(
            estimator.span_equal(
                estimator.algebra_conjugate(bundle.gauge_action, main_algebra),
                gauge_algebra,
            )
        )
    checks.add(
        "controls.gauge_algebra_descent",
        "controls",
        "exact_measurement",
        "all recovered atom algebras transform by the declared boundary gauge",
        tuple(gauge_block_checks),
        (True, True, True, True),
    )
    main_operations = operation_map(bundle.main)
    phase_operations = operation_map(bundle.phase_variant)
    unchanged_handles = tuple(
        sorted(set(main_operations) - {bundle.phase_changed_handle})
    )
    main_signatures = class_signature_by_handle(main_result)
    changed_phase_signature = estimator.operational_signature(
        bundle.phase_variant,
        phase_operations[bundle.phase_changed_handle],
    )
    signature_difference_count = sum(
        left != right
        for left, right in zip(
            main_signatures[bundle.phase_changed_handle], changed_phase_signature
        )
    )
    phase_atom = bundle.truth.atom_handles[0]
    checks.add(
        "controls.physical_phase",
        "controls",
        "control",
        "an uncompensated exact cyclotomic phase changes the law but not its local atom algebra",
        (
            all(main_operations[handle] == phase_operations[handle] for handle in unchanged_handles),
            estimator.canonical_mu8_phase(main_operations[bundle.phase_changed_handle])
            == estimator.canonical_mu8_phase(phase_operations[bundle.phase_changed_handle]),
            signature_difference_count,
            estimator.span_equal(
                algebra_for_handles(bundle.main, phase_atom),
                algebra_for_handles(bundle.phase_variant, phase_atom),
            ),
        ),
        (True, False, 576, True),
    )
    checks.add(
        "controls.source_float_literals",
        "controls",
        "static_audit",
        "all three L0 source files contain zero float literals",
        (
            len(float_literals(ESTIMATOR_PATH)),
            len(float_literals(FIXTURE_PATH)),
            len(float_literals(RUNNER_PATH)),
        ),
        (0, 0, 0),
    )
    checks.add_true(
        "controls.no_causal_result_keys",
        "controls",
        "static_audit",
        "the estimator result schema contains no causal, metric, field, or gravity key",
        not any(
            forbidden in json.dumps(main_result.to_data(), sort_keys=True).lower()
            for forbidden in ("causal", "metric", "field", "gravity", "spacelike")
        ),
    )

    elapsed_ns = time.monotonic_ns() - start_ns
    checks.add_true(
        "caps.total_runtime",
        "caps",
        "exact_measurement",
        "the complete positive and control suite remains below 240 seconds",
        elapsed_ns < RUNTIME_CAP_NS,
    )
    checks.add(
        "caps.main_search_scope",
        "caps",
        "type_check",
        "carrier, intervention-class, and partition caps are saturated but not exceeded",
        (
            bundle.main.dimension <= estimator.MAX_CARRIER_DIMENSION,
            len(main_result.intervention_classes) <= estimator.MAX_INTERVENTION_CLASSES,
            main_result.partitions_examined <= estimator.MAX_SET_PARTITIONS,
        ),
        (True, True, True),
    )

    anchors_ok = checks.group_passes("anchors")
    caps_ok = checks.group_passes("caps")
    classified = all(row.classification in CHECK_CLASSES for row in checks.rows)
    procedural_valid = anchors_ok and caps_ok and classified
    groupoid_prerequisites = (
        "quotient.accessible_dimension",
        "quotient.intervention_classes",
        "localization.finest_count",
        "localization.hidden_atom_match",
        "overlap.local_object_count",
        "overlap.pair_count",
        "overlap.triple_count",
        "localization.ambiguity_groupoid",
        "records.w3_rows",
    )
    groupoid_earned = procedural_valid and all(checks.passed(key) for key in groupoid_prerequisites)
    scientific_groups = ("quotient", "localization", "overlap", "records", "controls")
    atlas_earned = groupoid_earned and all(checks.group_passes(group) for group in scientific_groups)
    candidate_class_constructed = procedural_valid and checks.passed("quotient.intervention_classes")
    blocked_at_address = candidate_class_constructed and not groupoid_earned
    if atlas_earned:
        highest = "RQ0-LOCAL-ATLAS"
    elif groupoid_earned:
        highest = "RQ0-LOCALIZATION-GROUPOID"
    elif blocked_at_address:
        highest = "RQ0-L0-BLOCKED-AT-ADDRESS"
    else:
        highest = None
    receipt_valid = procedural_valid

    group_counts = {
        group: {
            "passed": sum(row.passed for row in checks.rows if row.group == group),
            "total": sum(1 for row in checks.rows if row.group == group),
        }
        for group in sorted({row.group for row in checks.rows})
    }
    class_counts = {
        classification: sum(1 for row in checks.rows if row.classification == classification)
        for classification in sorted(CHECK_CLASSES)
    }
    source_hashes = {
        "estimator": sha256(ESTIMATOR_PATH),
        "fixtures": sha256(FIXTURE_PATH),
        "runner": sha256(RUNNER_PATH),
    }
    return {
        "unit": "RQ0-L0",
        "status": "GREEN-UNREVIEWED" if receipt_valid and highest else "INVALID",
        "receipt_valid": receipt_valid,
        "mutation": "observed_estimator_anchor" if mutate_anchor else None,
        "provenance": {
            "pin_commit": estimator.PIN_COMMIT,
            "estimator_freeze_commit": ESTIMATOR_COMMIT,
            "estimator_precedes_fixture": True,
            "claim_scope": (
                "Git history proves temporal source freeze and executable dependency separation; "
                "it does not prove independent blind authorship"
            ),
            "source_hashes": source_hashes,
            "observed_anchor_hashes": observed_locks,
            "estimator_imports": list(estimator_imports),
        },
        "postulates": [
            bundle.main.access_declaration,
            bundle.main.gauge_declaration,
            "candidate subalgebras are generated by subsets of at most eight opaque intervention classes",
            "presentation actions are supplied as exact gauge/symmetry data, without subsystem labels",
        ],
        "inherited_theorems": [
            "Paper 1 W3 H-corr/H-avail record seam and boundary-gauge scope",
            "Paper 2 fact versus law/token distinction and groupoid allowance",
            "terminal RQ0-A typed amplitude instruments, morphisms, and record pullbacks",
        ],
        "constructed_objects": {
            "operational_quotient": "exact equivalence classes on reachable support",
            "localization": "one four-atom factorization and its complete proper subinstrument lattice",
            "localization_groupoid": "exact presentation-action arrows, including the ambiguity control swap",
            "overlap_nerve": "66 nonempty pair meets and 134 nonempty triple meets",
            "derived_records": "six W3 pair witnesses attached by exact algebra membership",
        },
        "search_scope": {
            "scalar_ring": "Q(zeta_8)",
            "implemented_gauge": "configuration relabelling x finite mu_8 boundary phase",
            "main_carrier_dimension": bundle.main.dimension,
            "accessible_dimension": main_result.accessible_dimension,
            "intervention_classes": len(main_result.intervention_classes),
            "set_partitions": main_result.partitions_examined,
            "runtime_cap_ns": RUNTIME_CAP_NS,
            "runtime_below_cap": elapsed_ns < RUNTIME_CAP_NS,
            "random_seed": None,
            "tolerance": None,
            "numeric_fallback": None,
        },
        "measurements": {
            "main_result": main_result.to_data(),
            "atom_truth_map": list(atom_map),
            "truth_regions": [sorted(value) for value in truth_regions],
            "record_bearing_region_count": len(record_bearing_regions),
            "distinct_nonempty_pair_meets": [
                sorted(value) for value in sorted(distinct_nonempty_pair_meets, key=lambda x: (len(x), tuple(x)))
            ],
            "required_fact_triple": [sorted(value) for value in bundle.truth.required_fact_triple],
            "local_restrictions": [
                {
                    "source": value.source_object,
                    "target": value.target_object,
                    "source_atoms": sorted(value.source_atoms),
                    "target_atoms": sorted(value.target_atoms),
                }
                for value in local_restrictions
            ],
            "record_restrictions": [
                {
                    "source": value.source_object,
                    "target": value.target_object,
                    "record": value.record_handle,
                    "map_type": value.map_type,
                }
                for value in record_restrictions
            ],
            "equal_law_no_bridge": normalize(equal_law),
            "inaccessible_result": inaccessible_result.to_data(),
            "ambiguity_result": ambiguity_result.to_data(),
            "irreducible_result": irreducible_result.to_data(),
            "physical_phase_signature_difference_count": signature_difference_count,
        },
        "checks": [row.to_data() for row in checks.rows],
        "check_counts": {
            "passed": sum(row.passed for row in checks.rows),
            "total": len(checks.rows),
            "by_group": group_counts,
            "by_class": class_counts,
            "semantic_declarations_counted": 0,
        },
        "outcomes": {
            "RQ0-L0-BLOCKED-AT-ADDRESS": blocked_at_address,
            "RQ0-LOCALIZATION-GROUPOID": groupoid_earned,
            "RQ0-LOCAL-ATLAS": atlas_earned,
            "highest": highest,
        },
        "first_unresolved_obstruction": (
            "localized operational intervention classes exist, but no influence or screening relation "
            "between them has been defined"
        ),
        "nonclaims": [
            "no influence or signalling relation",
            "no causal order or cone",
            "no spacelike separation",
            "no dimension or volume reconstruction",
            "no Lorentzian or special-relativity result",
            "no field, stress, gravity, or deformation-algebra result",
            "no full U(1) gauge implementation",
            "no claim to enumerate all abstract subalgebras beyond the frozen generator-subset scope",
            "no claim of independent blind authorship for the fixture",
        ],
    }


def render_text(receipt: Mapping[str, object]) -> str:
    counts = receipt["check_counts"]
    outcomes = receipt["outcomes"]
    scope = receipt["search_scope"]
    measurements = receipt["measurements"]
    main = measurements["main_result"]
    lines = [
        "=" * 78,
        "v13 RQ0-L0 — OPERATIONAL LOCALIZATION EXACT RECEIPT",
        "=" * 78,
        f"receipt valid: {receipt['receipt_valid']}",
        f"status: {receipt['status']}",
        f"mutation: {receipt['mutation']}",
        f"checks: {counts['passed']}/{counts['total']}",
        f"source hashes: {receipt['provenance']['source_hashes']}",
        "",
        "EXACT SEARCH",
        f"  scalar ring: {scope['scalar_ring']}",
        f"  carrier/access: {scope['main_carrier_dimension']}/{scope['accessible_dimension']}",
        f"  intervention classes: {scope['intervention_classes']}",
        f"  partitions: {scope['set_partitions']}",
        f"  runtime below cap / cap ns: {scope['runtime_below_cap']} / {scope['runtime_cap_ns']}",
        "",
        "MEASURED LOCALIZATION",
        f"  ambient algebra dimension: {main['ambient_algebra_dimension']}",
        f"  valid / finest factorizations: {len(main['valid_factorizations'])} / {len(main['finest_factorizations'])}",
        f"  local objects: {len(main['lattices'][0]['objects'])}",
        f"  nonempty pair / triple overlaps: {len(main['lattices'][0]['pair_overlaps'])} / {len(main['lattices'][0]['triple_overlaps'])}",
        f"  record-bearing regions: {measurements['record_bearing_region_count']}",
        f"  fact triple: {measurements['required_fact_triple']}",
        "",
        "OUTCOMES",
        f"  RQ0-L0-BLOCKED-AT-ADDRESS: {outcomes['RQ0-L0-BLOCKED-AT-ADDRESS']}",
        f"  RQ0-LOCALIZATION-GROUPOID: {outcomes['RQ0-LOCALIZATION-GROUPOID']}",
        f"  RQ0-LOCAL-ATLAS: {outcomes['RQ0-LOCAL-ATLAS']}",
        f"  highest: {outcomes['highest']}",
        "",
        "CHECK GROUPS",
    ]
    for group, row in counts["by_group"].items():
        lines.append(f"  {group}: {row['passed']}/{row['total']}")
    lines.extend(
        (
            "",
            "FIRST UNRESOLVED OBSTRUCTION",
            f"  {receipt['first_unresolved_obstruction']}",
            "",
            "NONCLAIMS",
        )
    )
    lines.extend(f"  - {value}" for value in receipt["nonclaims"])
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--mutate-anchor", action="store_true")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    receipt = build_receipt(mutate_anchor=args.mutate_anchor)
    if args.json:
        print(json.dumps(normalize(receipt), indent=2, sort_keys=True))
    else:
        print(render_text(receipt), end="")
    return 0 if receipt["receipt_valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
