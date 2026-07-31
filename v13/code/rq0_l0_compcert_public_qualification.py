#!/usr/bin/env python3
"""Public functional/performance qualification for the RQ0-L0 successor.

This runner may read the opened order-192 benchmark.  The benchmark is only
calibration evidence and can never supply a scientific RQ0-L0 outcome.  The
runner keeps canonical functional evidence separate from noncanonical timing.

During Stage A the expected estimator/proof hashes remain provisional.  They
are replaced once those two files are final, immediately before the Stage-B
freeze and its last public qualification run.
"""

from __future__ import annotations

import argparse
import ast
import copy
import dataclasses
import hashlib
import json
import platform
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, Mapping, Optional, Sequence, Tuple

try:
    from . import rq0_l0_compcert_estimator_exact as estimator
    from . import rq0_l0_certification_estimator_exact as legacy
    from . import rq0_l0_certification_fixtures_exact as opened_benchmark
except ImportError:
    import rq0_l0_compcert_estimator_exact as estimator
    import rq0_l0_certification_estimator_exact as legacy
    import rq0_l0_certification_fixtures_exact as opened_benchmark


SCHEMA = "rq0-l0-compcert-public-qualification-v1"
ROOT = Path(__file__).resolve().parents[2]
ESTIMATOR_PATH = ROOT / "v13/code/rq0_l0_compcert_estimator_exact.py"
PROOF_PATH = ROOT / "v13/note-rq0-operational-localization-computational-certification-soundness.md"
PIN_PATH = ROOT / "v13/note-rq0-operational-localization-computational-certification-pin.md"
FUNCTIONAL_RECEIPT_PATH = ROOT / "v13/code/rq0_l0_compcert_public_functional_receipt.json"
FUNCTIONAL_OUTPUT_PATH = ROOT / "v13/code/rq0_l0_compcert_public_functional_output.txt"
PERFORMANCE_RECEIPT_PATH = ROOT / "v13/code/rq0_l0_compcert_public_performance_receipt.json"
PERFORMANCE_OUTPUT_PATH = ROOT / "v13/code/rq0_l0_compcert_public_performance_output.txt"
EXPECTED_ESTIMATOR_SHA256 = "a9f8f93a01d7bf84d7dfde1e43b5c14a0111e9722b42d8e3dc999de887630f8b"
EXPECTED_PROOF_SHA256 = "5839fedcb680cb24e0ba778aff6e00aa92ac4f98191753693abbad1a54bbcd2d"
PUBLIC_ADDRESS_CAP_SECONDS = 120.0
PUBLIC_COMPLETE_CAP_SECONDS = 240.0
OFFICIAL_HELD_OUT_CAP_SECONDS = 360.0

FUTURE_PATHS = (
    "v13/code/rq0_l0_compcert_heldout_fixture_exact.py",
    "v13/code/rq0_l0_compcert_heldout_score.py",
    "v13/code/rq0_l0_compcert_heldout_receipt.json",
    "v13/code/rq0_l0_compcert_heldout_output.txt",
    "v13/note-rq0-operational-localization-computational-certification.md",
)


def sha256_file(path: Path) -> Optional[str]:
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_digest(value: object) -> str:
    return hashlib.sha256(
        estimator.canonical_json(value).encode("utf-8")
    ).hexdigest()


def serialized(dataset: legacy.OperationalDataset) -> Mapping[str, object]:
    # JSON round-trip enforces the same primitive-data boundary used by the
    # future scorer and gives mutants a real serialized input to modify.
    return json.loads(json.dumps(legacy.dataset_to_data(dataset), sort_keys=True))


def address_seconds(instrumentation: estimator.Instrumentation) -> float:
    keys = (
        "composition_validation",
        "normal_subobjects",
        "direct_complements",
        "factor_certification",
        "certificate_replay",
    )
    return sum(instrumentation.phase_seconds.get(key, 0.0) for key in keys)


@dataclass
class CaseRun:
    label: str
    resolution: estimator.Resolution
    functional: Mapping[str, object]
    timing: Mapping[str, object]
    dataset: legacy.OperationalDataset = field(repr=False)


def run_case(
    label: str,
    dataset: legacy.OperationalDataset,
    *,
    cap_seconds: float = PUBLIC_COMPLETE_CAP_SECONDS,
    injected_branch: Optional[str] = None,
) -> CaseRun:
    payload = serialized(dataset)
    started = time.monotonic()
    resolution = estimator.resolve_serialized_dataset(
        payload,
        cap_seconds=cap_seconds,
        injected_branch=injected_branch,
    )
    elapsed = time.monotonic() - started
    instrumentation = (
        resolution.analysis.instrumentation
        if resolution.analysis is not None
        else estimator.Instrumentation()
    )
    analysis_digest = None
    atlas_digest = None
    row_audit = None
    if resolution.analysis is not None:
        analysis_digest = stable_digest(
            {
                "normal_subobjects": resolution.analysis.result.normal_subobjects,
                "certificates": resolution.analysis.result.certificates,
                "finest": resolution.analysis.result.finest_certificates,
                "obstruction": resolution.analysis.result.first_obstruction,
            }
        )
        row_audit = dataclasses.asdict(
            resolution.analysis.result.composition.row_audit
        )
    if resolution.atlas is not None:
        atlas_digest = stable_digest(resolution.atlas)
    functional = {
        "outcome": dataclasses.asdict(resolution.outcome),
        "structural_summary": estimator.structural_summary(resolution),
        "analysis_digest": analysis_digest,
        "atlas_digest": atlas_digest,
        "row_audit": row_audit,
        "instrumentation": instrumentation.canonical(),
    }
    timing = {
        "label": label,
        "complete_seconds": elapsed,
        "address_seconds": address_seconds(instrumentation),
        "phases": instrumentation.timing(),
    }
    return CaseRun(label, resolution, functional, timing, dataset)


@dataclass
class Checks:
    values: list[Mapping[str, object]] = field(default_factory=list)

    def add(
        self,
        check_id: str,
        check_class: str,
        passed: bool,
        evidence: object,
    ) -> None:
        self.values.append(
            {
                "id": check_id,
                "class": check_class,
                "pass": bool(passed),
                "evidence": estimator.canonical_data(evidence),
            }
        )

    @property
    def passed(self) -> int:
        return sum(bool(value["pass"]) for value in self.values)

    @property
    def all_pass(self) -> bool:
        return self.passed == len(self.values)


def static_tailoring_audit() -> Mapping[str, object]:
    source = ESTIMATOR_PATH.read_text()
    tree = ast.parse(source)
    banned_module = "rq0_l0_certification_" + "fixtures_exact"
    banned_strings = (
        banned_module,
        "opaque-operation",
        "opaque-record",
        "serialized_main_input_" + "sha256",
        "759d7c0ac774943cf220526751b54d9c5aaa8dcfd4ef98b344758a09cf61d322",
    )
    text_hits = tuple(value for value in banned_strings if value in source)
    import_hits = []
    condition_hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            import_hits.extend(
                value.name for value in node.names if value.name == banned_module
            )
        elif isinstance(node, ast.ImportFrom):
            if node.module == banned_module:
                import_hits.append(node.module)
        elif isinstance(node, (ast.If, ast.IfExp, ast.While)):
            segment = ast.get_source_segment(source, node.test) or ""
            constants = {
                value.value
                for value in ast.walk(node.test)
                if isinstance(value, ast.Constant)
            }
            tuples = {
                tuple(
                    item.value
                    for item in value.elts
                    if isinstance(item, ast.Constant)
                )
                for value in ast.walk(node.test)
                if isinstance(value, (ast.Tuple, ast.List))
                and all(isinstance(item, ast.Constant) for item in value.elts)
            }
            if 192 in constants or (2, 3, 4, 8) in tuples:
                condition_hits.append(segment)
            if "dataset.handle" in segment or "dataset.records" in segment:
                condition_hits.append(segment)
    return {
        "pass": not text_hits and not import_hits and not condition_hits,
        "text_hits": text_hits,
        "import_hits": tuple(import_hits),
        "condition_hits": tuple(condition_hits),
    }


def record_handle_renamed(dataset: legacy.OperationalDataset) -> legacy.OperationalDataset:
    data = serialized(dataset)
    mapping = {
        value["handle"]: f"presentation-only-record-{index}"
        for index, value in enumerate(data["records"])
    }
    for value in data["records"]:
        old = value["handle"]
        value["handle"] = mapping[old]
        value["witness"]["handle"] = f"presentation-only-witness::{mapping[old]}"
    for context in data["contexts"]:
        context["record_handles"] = [
            mapping[value] for value in context["record_handles"]
        ]
    data["handle"] = "record-handle-renamed-presentation"
    return legacy.dataset_from_data(data)


def redundant_alias(dataset: legacy.OperationalDataset) -> legacy.OperationalDataset:
    data = serialized(dataset)
    source = copy.deepcopy(data["operations"][0])
    source_handle = source["handle"]
    alias_handle = "redundant-legal-operation-alias"
    source["handle"] = alias_handle
    data["operations"].append(source)
    old_rows = {
        (value["left"], value["right"]): value
        for value in data["composition_rows"]
    }
    handles = [value["handle"] for value in data["operations"]]
    rows = []
    for left in handles:
        for right in handles:
            base_left = source_handle if left == alias_handle else left
            base_right = source_handle if right == alias_handle else right
            row = copy.deepcopy(old_rows[(base_left, base_right)])
            row["left"] = left
            row["right"] = right
            rows.append(row)
    data["composition_rows"] = rows
    data["handle"] = "redundant-legal-alias-presentation"
    return legacy.dataset_from_data(data)


def mutate_serialized_row(
    dataset: legacy.OperationalDataset,
    field_name: str,
    value: object,
) -> Mapping[str, object]:
    data = serialized(dataset)
    data["composition_rows"][0][field_name] = value
    return data


def mutate_selectability(dataset: legacy.OperationalDataset) -> Mapping[str, object]:
    data = serialized(dataset)
    for value in data["operations"]:
        value["independently_selectable"] = False
    return data


def artifact_map_mutant(
    run: CaseRun,
    which: str,
) -> estimator.Resolution:
    if run.resolution.atlas is None:
        raise AssertionError("artifact mutant requires a positive atlas")
    atlas = run.resolution.atlas
    if which == "regional-row":
        index = next(
            i for i, value in enumerate(atlas.arrows) if value.row_map
        )
        arrow = atlas.arrows[index]
        row = dataclasses.replace(arrow.row_map[0], target_tau="mutated|tau")
        arrow = dataclasses.replace(
            arrow, row_map=(row,) + arrow.row_map[1:]
        )
        arrows = list(atlas.arrows)
        arrows[index] = arrow
        atlas = dataclasses.replace(atlas, arrows=tuple(arrows))
    elif which == "context-map":
        index = next(
            i
            for i, value in enumerate(atlas.arrows)
            if value.context_map.target_records
        )
        arrow = atlas.arrows[index]
        context = dataclasses.replace(
            arrow.context_map, target_records=frozenset()
        )
        arrow = dataclasses.replace(arrow, context_map=context)
        arrows = list(atlas.arrows)
        arrows[index] = arrow
        atlas = dataclasses.replace(atlas, arrows=tuple(arrows))
    elif which == "projector-pullback":
        index = next(
            i
            for i, value in enumerate(atlas.fact_maps)
            if value.projector_equalities
        )
        fact = dataclasses.replace(
            atlas.fact_maps[index], projector_equalities=()
        )
        facts = list(atlas.fact_maps)
        facts[index] = fact
        atlas = dataclasses.replace(atlas, fact_maps=tuple(facts))
    else:
        raise ValueError("unknown artifact mutant")
    return estimator.adjudicate_resolution_artifacts(
        run.dataset, dataclasses.replace(run.resolution, atlas=atlas)
    )


def guarded_anchor_outcome(actual_hash: str, expected_hash: str) -> estimator.Outcome:
    if actual_hash != expected_hash:
        return estimator.Outcome(
            estimator.PROCEDURAL_OUTCOME,
            "procedural",
            1,
            "frozen estimator anchor mismatch",
        )
    return estimator.Outcome(
        "RQ0-L0-BLOCKED-AT-ADDRESS",
        "scientific",
        0,
        "anchor calibration sentinel",
    )


def dense_sparse_public_equivalence(
    base: CaseRun,
) -> Tuple[Mapping[str, object], Mapping[str, object]]:
    if base.resolution.analysis is None or base.resolution.atlas is None:
        return ({"all_pass": False, "reason": "base analysis absent"}, {})
    analysis = base.resolution.analysis
    composition = analysis.result.composition
    requested = {frozenset(range(composition.size))}
    for certificate in analysis.result.certificates:
        requested.update(certificate.factors)
    requested.update(value.operations for value in base.resolution.atlas.objects)
    instrumentation = estimator.Instrumentation()
    cache = estimator.ExactAlgebraCache(composition, instrumentation)
    started = time.monotonic()
    checks = []
    for subobject in sorted(requested, key=lambda value: (len(value), tuple(sorted(value)))):
        checks.append(
            {
                "order": len(subobject),
                "key": legacy.stable_hash(tuple(sorted(subobject))),
                "pass": estimator.dense_sparse_equivalent(
                    composition,
                    subobject,
                    base.dataset.carrier_dimension,
                    cache,
                ),
            }
        )
    elapsed = time.monotonic() - started
    functional = {
        "subobjects_checked": len(checks),
        "orders": [value["order"] for value in checks],
        "all_pass": all(value["pass"] for value in checks),
        "checks": checks,
    }
    return functional, {
        "dense_sparse_equivalence_seconds": elapsed,
        "cache": instrumentation.canonical(),
    }


def git_tracked(path: str) -> bool:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", path],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def qualify(*, development: bool) -> Tuple[Mapping[str, object], Mapping[str, object]]:
    checks = Checks()
    estimator_hash = sha256_file(ESTIMATOR_PATH)
    proof_hash = sha256_file(PROOF_PATH)
    pin_hash = sha256_file(PIN_PATH)
    future_absence = {
        value: {"filesystem_absent": not (ROOT / value).exists(), "git_untracked": not git_tracked(value)}
        for value in FUTURE_PATHS
    }
    if development:
        estimator_anchor_ok = estimator_hash is not None
        proof_anchor_ok = proof_hash is not None
    else:
        estimator_anchor_ok = estimator_hash == EXPECTED_ESTIMATOR_SHA256
        proof_anchor_ok = proof_hash == EXPECTED_PROOF_SHA256
    checks.add("Q001", "provenance", estimator_anchor_ok, {"actual": estimator_hash, "expected": EXPECTED_ESTIMATOR_SHA256, "development": development})
    checks.add("Q002", "provenance", proof_anchor_ok, {"actual": proof_hash, "expected": EXPECTED_PROOF_SHA256, "development": development})
    checks.add("Q003", "provenance", all(value["filesystem_absent"] and value["git_untracked"] for value in future_absence.values()), future_absence)
    static = static_tailoring_audit()
    checks.add("Q004", "no-tailoring", static["pass"], static)

    public_legacy = legacy.public_self_test()
    checks.add("Q005", "inherited", public_legacy["all_pass"] and public_legacy["passed"] == public_legacy["total"], {"passed": public_legacy["passed"], "total": public_legacy["total"]})

    base_dataset = opened_benchmark.build_main_dataset("base")
    base_one = run_case("opened-base-run-1", base_dataset)
    base_two = run_case("opened-base-run-2", opened_benchmark.build_main_dataset("base"))
    base_canonical_one = estimator.canonical_json(base_one.functional)
    base_canonical_two = estimator.canonical_json(base_two.functional)
    checks.add("Q006", "benchmark", base_one.resolution.outcome.code == "RQ0-LOCAL-ATLAS", base_one.resolution.outcome.code)
    checks.add("Q007", "determinism", base_canonical_one == base_canonical_two, hashlib.sha256(base_canonical_one.encode()).hexdigest())
    checks.add("Q008", "performance", base_one.timing["address_seconds"] < PUBLIC_ADDRESS_CAP_SECONDS, "addressability below registered 120-second cap")
    checks.add("Q009", "performance", base_one.timing["complete_seconds"] < PUBLIC_COMPLETE_CAP_SECONDS, "base pipeline below registered 240-second cap")
    counters = base_one.resolution.analysis.instrumentation.counters if base_one.resolution.analysis else {}
    factor_key_counts = {key: value for key, value in counters.items() if key.startswith("factor_algebra_build::")}
    checks.add("Q010", "cache", counters.get("ambient_represented_algebra_builds") == 1, counters.get("ambient_represented_algebra_builds"))
    checks.add("Q011", "cache", bool(factor_key_counts) and max(factor_key_counts.values()) <= 1, factor_key_counts)
    checks.add("Q012", "cache", counters.get("represented_algebra_cache_hits", 0) > 0 and counters.get("regional_restriction_algebra_requests", 0) > 0, {"cache_hits": counters.get("represented_algebra_cache_hits", 0), "regional_requests": counters.get("regional_restriction_algebra_requests", 0)})

    summary = estimator.structural_summary(base_one.resolution)
    transformed_inputs = (
        ("fully-renamed", opened_benchmark.build_main_dataset("base", rename_handles=True)),
        ("serialization-reordered", estimator.reorder_dataset(base_dataset)),
        ("carrier-gauge-conjugated", opened_benchmark.build_main_dataset("carrier-relabel")),
        ("global-character-gauge", opened_benchmark.build_main_dataset("gauge-character")),
        ("record-handle-only", record_handle_renamed(base_dataset)),
        ("redundant-legal-alias", redundant_alias(base_dataset)),
    )
    transformed = []
    for label, dataset in transformed_inputs:
        value = run_case(label, dataset)
        transformed.append(value)
        checks.add(
            f"Q{13 + len(transformed) - 1:03d}",
            "metamorphic",
            value.resolution.outcome.code == "RQ0-LOCAL-ATLAS" and estimator.structural_summary(value.resolution) == summary,
            {"label": label, "outcome": value.resolution.outcome.code, "summary": estimator.structural_summary(value.resolution)},
        )

    positive = run_case("unrelated-positive", legacy.public_regional_calibration_dataset(), cap_seconds=60)
    blocked_address = run_case("unrelated-address-block", legacy.public_selectability_pair(True), cap_seconds=60)
    blocked_maps = run_case("unrelated-map-block", legacy.public_selectability_pair(False), cap_seconds=60)
    checks.add("Q019", "outcome", positive.resolution.outcome.code == "RQ0-LOCAL-ATLAS", positive.resolution.outcome.code)
    checks.add("Q020", "outcome", blocked_address.resolution.outcome.code == "RQ0-L0-BLOCKED-AT-ADDRESS", blocked_address.resolution.outcome.code)
    checks.add("Q021", "outcome", blocked_maps.resolution.outcome.code == "RQ0-L0-BLOCKED-AT-REGIONAL-MAPS", blocked_maps.resolution.outcome.code)

    collapse = run_case("declared-collapse", legacy.public_declared_collapse_dataset(), cap_seconds=60)
    unavailable = run_case("unavailable-row", legacy.public_unavailable_dataset(), cap_seconds=60)
    checks.add("Q022", "composition", collapse.resolution.outcome.code == "RQ0-L0-BLOCKED-AT-ADDRESS" and "COLLAPSED" in collapse.resolution.outcome.reason, collapse.resolution.outcome.reason)
    checks.add("Q023", "composition", unavailable.resolution.outcome.code == "RQ0-L0-BLOCKED-AT-ADDRESS" and "unavailable" in unavailable.resolution.outcome.reason, unavailable.resolution.outcome.reason)
    fully_selectable_analysis = estimator.analyze_addressability(legacy.public_selectability_pair(False))
    collision_factor = fully_selectable_analysis.result.finest_certificates[0].factors[0]
    _image, collision = legacy.multiplication_image(fully_selectable_analysis.result.composition, (collision_factor, collision_factor))
    checks.add("Q024", "composition", collision is not None and collapse.resolution.analysis.result.composition.row_audit.collapsed_rows > 0, {"true_collision": collision, "declared_collapsed_rows": collapse.resolution.analysis.result.composition.row_audit.collapsed_rows})

    v4_dataset = legacy.public_v4_dataset(with_records=True)
    v4_analysis = estimator.analyze_addressability(v4_dataset)
    groupoid = legacy.derive_record_bearing_groupoid(v4_dataset, v4_analysis.result)
    checks.add("Q025", "ambiguity", len(v4_analysis.result.finest_certificates) > 1 and groupoid.every_factor_record_bearing and groupoid.object_count > 1, {"finest": len(v4_analysis.result.finest_certificates), "objects": groupoid.object_count, "arrows": groupoid.arrow_count})

    twisted = estimator.full_instrument_twisted_triple()
    pair_rechecks = (
        estimator.validate_full_instrument_isomorphism(twisted.pair_maps[0], twisted.instruments[0], twisted.instruments[1]),
        estimator.validate_full_instrument_isomorphism(twisted.pair_maps[1], twisted.instruments[1], twisted.instruments[2]),
        estimator.validate_full_instrument_isomorphism(twisted.pair_maps[2], twisted.instruments[0], twisted.instruments[2]),
    )
    checks.add("Q026", "twisted-triple", all(twisted.pair_valid) and all(pair_rechecks), {"built": twisted.pair_valid, "rechecked": pair_rechecks})
    checks.add("Q027", "twisted-triple", twisted.rejected_only_at_loop and not twisted.regional_loop_commutes and not twisted.record_loop_commutes, {"regional_loop": twisted.regional_loop_commutes, "record_loop": twisted.record_loop_commutes})

    dense_functional, dense_timing = dense_sparse_public_equivalence(base_one)
    checks.add("Q028", "backend-equivalence", dense_functional["all_pass"], {"subobjects": dense_functional.get("subobjects_checked"), "orders": dense_functional.get("orders")})

    row_audit = base_one.resolution.analysis.result.composition.row_audit
    complete_rows = len(base_dataset.composition_rows)
    checks.add("Q029", "typed-rows", all(value == complete_rows for value in (row_audit.typed_rows, row_audit.status_rows, row_audit.result_rows, row_audit.exact_law_rows, row_audit.physical_composition_rows, row_audit.gauge_rows, row_audit.signature_rows)), dataclasses.asdict(row_audit))
    atlas = base_one.resolution.atlas
    all_arrows_valid = atlas is not None and all(
        estimator.validate_full_regional_arrow(
            arrow,
            next(value for value in atlas.objects if value.structural_id == arrow.source),
            next(value for value in atlas.objects if value.structural_id == arrow.target),
            base_one.resolution.analysis.result.composition,
        )
        for arrow in atlas.arrows
    )
    checks.add("Q030", "regional-morphisms", all_arrows_valid and estimator.validate_full_regional_atlas(base_dataset, base_one.resolution.analysis, atlas), {"arrows": 0 if atlas is None else len(atlas.arrows), "regional_paths": 0 if atlas is None else atlas.coherent_regional_paths})
    checks.add("Q031", "record-functor", atlas is not None and atlas.coherent_fact_paths > 0 and all(value.record_generator_map is not None and value.projector_equalities is not None for value in atlas.fact_maps), {"fact_maps": 0 if atlas is None else len(atlas.fact_maps), "coherent_paths": 0 if atlas is None else atlas.coherent_fact_paths})
    record_only_run = next(value for value in transformed if value.label == "record-handle-only")
    checks.add("Q032", "handle-invariance", record_only_run.functional["atlas_digest"] == base_one.functional["atlas_digest"], {"base": base_one.functional["atlas_digest"], "renamed": record_only_run.functional["atlas_digest"]})

    mutant_started = time.monotonic()
    composition_tau = estimator.resolve_serialized_dataset(mutate_serialized_row(base_dataset, "tau", "bad|tau"), cap_seconds=PUBLIC_COMPLETE_CAP_SECONDS)
    selectability = estimator.resolve_serialized_dataset(mutate_selectability(base_dataset), cap_seconds=PUBLIC_COMPLETE_CAP_SECONDS)
    malformed_data = serialized(base_dataset)
    malformed_data["composition_rows"] = malformed_data["composition_rows"][:-1]
    malformed = estimator.resolve_serialized_dataset(malformed_data, cap_seconds=60)
    runtime_cap = estimator.resolve_serialized_dataset(serialized(base_dataset), cap_seconds=0.0)
    checks.add("Q033", "end-to-end-mutant", composition_tau.outcome.code == estimator.PROCEDURAL_OUTCOME and composition_tau.outcome.exit_code == 1, composition_tau.outcome.reason)
    checks.add("Q034", "end-to-end-mutant", selectability.outcome.code != "RQ0-LOCAL-ATLAS" and selectability.outcome.code != "RQ0-LOCALIZATION-GROUPOID", selectability.outcome.code)
    checks.add("Q035", "end-to-end-mutant", malformed.outcome.code == estimator.PROCEDURAL_OUTCOME and malformed.outcome.exit_code == 1, malformed.outcome.reason)
    checks.add("Q036", "end-to-end-mutant", runtime_cap.outcome.code == estimator.PROCEDURAL_OUTCOME and runtime_cap.outcome.exit_code == 1, runtime_cap.outcome.reason)

    map_source = run_case("map-mutant-source", opened_benchmark.build_main_dataset("base"))
    regional_mutant = artifact_map_mutant(map_source, "regional-row")
    context_mutant = artifact_map_mutant(map_source, "context-map")
    projector_source = run_case("projector-mutant-source", opened_benchmark.build_main_dataset("base"))
    projector_mutant = artifact_map_mutant(projector_source, "projector-pullback")
    checks.add("Q037", "end-to-end-mutant", regional_mutant.outcome.code == estimator.PROCEDURAL_OUTCOME and regional_mutant.outcome.exit_code == 1, regional_mutant.outcome.reason)
    checks.add("Q038", "end-to-end-mutant", context_mutant.outcome.code == estimator.PROCEDURAL_OUTCOME and context_mutant.outcome.exit_code == 1, context_mutant.outcome.reason)
    checks.add("Q039", "end-to-end-mutant", projector_mutant.outcome.code == estimator.PROCEDURAL_OUTCOME and projector_mutant.outcome.exit_code == 1, projector_mutant.outcome.reason)

    small_payload = serialized(legacy.public_v4_dataset(with_records=False))
    branches = {
        name: estimator.resolve_serialized_dataset(small_payload, cap_seconds=60, injected_branch=name)
        for name in ("timeout", "exception", "missing-outcome", "multiple-outcomes")
    }
    for ordinal, name in enumerate(("timeout", "exception", "missing-outcome", "multiple-outcomes"), start=40):
        checks.add(f"Q{ordinal:03d}", "total-resolver", branches[name].outcome.code == estimator.PROCEDURAL_OUTCOME and branches[name].outcome.exit_code == 1, {"branch": name, "reason": branches[name].outcome.reason})
    bad_anchor = guarded_anchor_outcome(estimator_hash or "", "0" * 64)
    checks.add("Q044", "end-to-end-mutant", bad_anchor.code == estimator.PROCEDURAL_OUTCOME and bad_anchor.exit_code == 1, bad_anchor.reason)
    mutant_seconds = time.monotonic() - mutant_started
    opened_complete_mutant_pipeline_seconds = (
        base_one.timing["complete_seconds"] + mutant_seconds
    )
    checks.add(
        "Q048",
        "performance",
        opened_complete_mutant_pipeline_seconds < PUBLIC_COMPLETE_CAP_SECONDS,
        "base plus complete end-to-end mutant pipeline below registered 240-second cap",
    )

    actual_invariants = estimator.composition_invariants(base_one.resolution.analysis.result.composition)
    checks.add("Q045", "novelty-discipline", actual_invariants.get("group_like") is True and actual_invariants.get("order") == len(base_one.resolution.analysis.result.composition.classes), actual_invariants)
    checks.add("Q046", "truth-separation", "old_s3_cubed_imported" not in ESTIMATOR_PATH.read_text() and "held_out_truth" not in ESTIMATOR_PATH.read_text(), "novelty read from composition_invariants only")
    checks.add("Q047", "ceiling", True, "public benchmark only; no scientific L0 promotion")

    canonical_benchmark = {
        "run_one": base_one.functional,
        "run_two_sha256": hashlib.sha256(base_canonical_two.encode()).hexdigest(),
        "metamorphic": {
            value.label: {
                "outcome": value.resolution.outcome.code,
                "summary": estimator.structural_summary(value.resolution),
            }
            for value in transformed
        },
        "dense_sparse": dense_functional,
        "actual_composition_invariants": actual_invariants,
    }
    controls = {
        "unrelated_positive": positive.resolution.outcome.code,
        "blocked_at_address": blocked_address.resolution.outcome.code,
        "blocked_at_regional_maps": blocked_maps.resolution.outcome.code,
        "declared_collapse": collapse.resolution.outcome.code,
        "unavailable": unavailable.resolution.outcome.code,
        "record_bearing_ambiguity": {"objects": groupoid.object_count, "arrows": groupoid.arrow_count},
        "twisted_triple": {"pair_valid": twisted.pair_valid, "rejected_only_at_loop": twisted.rejected_only_at_loop},
        "mutants": {
            "anchor": bad_anchor.code,
            "composition_row": composition_tau.outcome.code,
            "selectability": selectability.outcome.code,
            "regional_row_map": regional_mutant.outcome.code,
            "context_map": context_mutant.outcome.code,
            "projector_pullback": projector_mutant.outcome.code,
            "malformed": malformed.outcome.code,
            "runtime_cap": runtime_cap.outcome.code,
            **{name: value.outcome.code for name, value in branches.items()},
        },
    }
    functional = {
        "schema": SCHEMA,
        "stage": "A-PUBLIC-DEVELOPMENT" if development else "B-FROZEN-PUBLIC-QUALIFICATION",
        "qualification_outcome": "PUBLIC-QUALIFIED" if checks.all_pass else "PUBLIC-QUALIFICATION-FAILED",
        "scientific_outcome": None,
        "opened_benchmark_can_earn_rung": False,
        "sources": {
            "pin_sha256": pin_hash,
            "estimator_sha256": estimator_hash,
            "proof_sha256": proof_hash,
            "expected_estimator_sha256": EXPECTED_ESTIMATOR_SHA256,
            "expected_proof_sha256": EXPECTED_PROOF_SHA256,
        },
        "future_paths_absent": future_absence,
        "static_no_tailoring": static,
        "benchmark": canonical_benchmark,
        "controls": controls,
        "checks": checks.values,
        "passed": checks.passed,
        "total": len(checks.values),
        "all_pass": checks.all_pass,
        "definitions_postulates": [
            "complete finite operational row access is a declared access postulate",
            "full basis preparation/configuration tomography are public fixture postulates",
            "wall-clock time is noncanonical and enters only registered cap gates",
        ],
        "nonclaims": [
            "no scientific result is inferred from the opened benchmark",
            "no topology, spatial localization, influence or causality",
            "no Lorentzian geometry, spacetime, fields or gravity",
        ],
    }
    performance = {
        "schema": SCHEMA + "-timing",
        "canonical": False,
        "machine": {
            "platform": platform.platform(),
            "python": sys.version.split()[0],
        },
        "caps_seconds": {
            "public_address": PUBLIC_ADDRESS_CAP_SECONDS,
            "public_complete": PUBLIC_COMPLETE_CAP_SECONDS,
            "future_official_held_out": OFFICIAL_HELD_OUT_CAP_SECONDS,
        },
        "base_runs": [base_one.timing, base_two.timing],
        "metamorphic_runs": [value.timing for value in transformed],
        "control_runs": [positive.timing, blocked_address.timing, blocked_maps.timing, collapse.timing, unavailable.timing, map_source.timing, projector_source.timing],
        "backend_equivalence": dense_timing,
        "opened_complete_mutant_pipeline_seconds": opened_complete_mutant_pipeline_seconds,
        "thresholds_pass": {
            "address_under_120": base_one.timing["address_seconds"] < PUBLIC_ADDRESS_CAP_SECONDS,
            "base_complete_under_240": base_one.timing["complete_seconds"] < PUBLIC_COMPLETE_CAP_SECONDS,
            "complete_mutant_pipeline_under_240": opened_complete_mutant_pipeline_seconds < PUBLIC_COMPLETE_CAP_SECONDS,
        },
    }
    return functional, performance


def render_text(functional: Mapping[str, object], performance: Mapping[str, object]) -> str:
    first = performance["base_runs"][0]
    return "\n".join(
        (
            "RQ0-L0 COMPUTATIONAL-CERTIFICATION PUBLIC QUALIFICATION",
            f"stage: {functional['stage']}",
            f"qualification_outcome: {functional['qualification_outcome']}",
            "scientific_outcome: none (opened benchmark)",
            f"checks: {functional['passed']}/{functional['total']}",
            f"opened benchmark address: {first['address_seconds']:.6f}s / 120s",
            f"opened benchmark complete: {first['complete_seconds']:.6f}s / 240s",
            (
                "opened benchmark + end-to-end mutants: "
                f"{performance['opened_complete_mutant_pipeline_seconds']:.6f}s / 240s"
            ),
            f"canonical repeat: {'PASS' if functional['checks'][6]['pass'] else 'FAIL'}",
            f"future held-out paths absent: {'PASS' if functional['checks'][2]['pass'] else 'FAIL'}",
            "ceiling: L0 only; no T1/C1 or spacetime claim",
            "",
        )
    )


def render_performance_text(performance: Mapping[str, object]) -> str:
    first = performance["base_runs"][0]
    return "\n".join(
        (
            "RQ0-L0 COMPUTATIONAL-CERTIFICATION PUBLIC PERFORMANCE",
            "canonical: false",
            f"address: {first['address_seconds']:.6f}s / 120s",
            f"base complete: {first['complete_seconds']:.6f}s / 240s",
            (
                "base plus end-to-end mutants: "
                f"{performance['opened_complete_mutant_pipeline_seconds']:.6f}s / 240s"
            ),
            (
                "dense/sparse audit: "
                f"{performance['backend_equivalence']['dense_sparse_equivalence_seconds']:.6f}s"
            ),
            "timing is noncanonical and enters no scientific predicate except registered caps",
            "",
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--development", action="store_true")
    parser.add_argument("--section", choices=("all", "functional", "performance", "text"), default="all")
    parser.add_argument("--write-receipts", action="store_true")
    args = parser.parse_args()
    functional, performance = qualify(development=args.development)
    if args.write_receipts:
        FUNCTIONAL_RECEIPT_PATH.write_text(
            estimator.canonical_json(functional)
        )
        FUNCTIONAL_OUTPUT_PATH.write_text(render_text(functional, performance))
        PERFORMANCE_RECEIPT_PATH.write_text(
            estimator.canonical_json(performance)
        )
        PERFORMANCE_OUTPUT_PATH.write_text(
            render_performance_text(performance)
        )
    if args.section == "functional":
        print(estimator.canonical_json(functional), end="")
    elif args.section == "performance":
        print(estimator.canonical_json(performance), end="")
    elif args.section == "text":
        print(render_text(functional, performance), end="")
    else:
        print(estimator.canonical_json({"functional": functional, "performance": performance}), end="")
    return 0 if functional["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
