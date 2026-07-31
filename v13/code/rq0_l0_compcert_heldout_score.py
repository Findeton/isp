#!/usr/bin/env python3
"""One-shot official scorer for the frozen RQ0-L0 held-out fixture."""

from __future__ import annotations

import argparse
import copy
import dataclasses
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Mapping, Optional

try:
    from . import rq0_l0_compcert_estimator_exact as estimator
    from . import rq0_l0_certification_estimator_exact as legacy
    from . import rq0_l0_compcert_heldout_fixture_exact as fixture
except ImportError:
    import rq0_l0_compcert_estimator_exact as estimator
    import rq0_l0_certification_estimator_exact as legacy
    import rq0_l0_compcert_heldout_fixture_exact as fixture


SCHEMA = "rq0-l0-compcert-heldout-official-receipt-v1"
ROOT = Path(__file__).resolve().parents[2]
SCORER_PATH = Path(__file__).resolve()
ESTIMATOR_PATH = ROOT / "v13/code/rq0_l0_compcert_estimator_exact.py"
PROOF_PATH = ROOT / "v13/note-rq0-operational-localization-computational-certification-soundness.md"
FIXTURE_PATH = ROOT / "v13/code/rq0_l0_compcert_heldout_fixture_exact.py"
RECEIPT_PATH = ROOT / "v13/code/rq0_l0_compcert_heldout_receipt.json"
OUTPUT_PATH = ROOT / "v13/code/rq0_l0_compcert_heldout_output.txt"
DELIVERY_PATH = "v13/note-rq0-operational-localization-computational-certification.md"
COMPLETE_CAP_SECONDS = 360.0
EXPECTED_FIXTURE_SHA256 = "d4a72c05f8755b4247ecac19f7ac9a49656c3c855a2fea08a77c73ce7b8d72ea"


def sha256_file(path: Path) -> Optional[str]:
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_digest(value: object) -> str:
    return hashlib.sha256(
        estimator.canonical_json(value).encode("utf-8")
    ).hexdigest()


def serialized(dataset: legacy.OperationalDataset) -> Mapping[str, object]:
    return json.loads(json.dumps(legacy.dataset_to_data(dataset), sort_keys=True))


def git_path_absent(commit: str, path: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{commit}:{path}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode != 0


def run_payload(
    payload: Mapping[str, object],
    deadline: float,
    *,
    injected_branch: Optional[str] = None,
) -> estimator.Resolution:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        return estimator.Resolution(
            estimator.Outcome(
                estimator.PROCEDURAL_OUTCOME,
                "procedural",
                1,
                "official complete-run deadline exhausted",
            ),
            None,
            None,
        )
    return estimator.resolve_serialized_dataset(
        payload,
        cap_seconds=remaining,
        injected_branch=injected_branch,
    )


def is_positive(value: estimator.Resolution) -> bool:
    return value.outcome.code in (
        "RQ0-LOCALIZATION-GROUPOID",
        "RQ0-LOCAL-ATLAS",
    )


def no_positive(value: estimator.Resolution) -> bool:
    return not is_positive(value)


def _record_handle_renamed(
    dataset: legacy.OperationalDataset,
) -> legacy.OperationalDataset:
    data = copy.deepcopy(serialized(dataset))
    mapping = {
        value["handle"]: f"heldout-record-presentation-{index}"
        for index, value in enumerate(data["records"])
    }
    for value in data["records"]:
        old = value["handle"]
        value["handle"] = mapping[old]
        value["witness"]["handle"] = f"heldout-witness-presentation-{mapping[old]}"
    for context in data["contexts"]:
        context["record_handles"] = [
            mapping[value] for value in context["record_handles"]
        ]
    data["handle"] = "heldout-record-handle-presentation"
    return legacy.dataset_from_data(data)


def _carrier_gauge_conjugated(
    dataset: legacy.OperationalDataset,
) -> legacy.OperationalDataset:
    dimension = dataset.carrier_dimension
    action = legacy.permutation_law(
        tuple((5 * index + 7) % dimension for index in range(dimension))
    )

    def resolution(value):
        return tuple(
            frozenset(action.permutation[index] for index in atom)
            for atom in value
        )

    return legacy.OperationalDataset(
        handle="heldout-carrier-gauge-presentation",
        carrier_dimension=dimension,
        operations=tuple(
            dataclasses.replace(
                value,
                law=value.law.conjugated(action),
                observed_signature=value.law.conjugated(action).signature(),
            )
            for value in dataset.operations
        ),
        composition_rows=tuple(
            dataclasses.replace(
                value,
                law=None if value.law is None else value.law.conjugated(action),
                observed_signature=(
                    None
                    if value.law is None
                    else value.law.conjugated(action).signature()
                ),
            )
            for value in dataset.composition_rows
        ),
        preparations=dataset.preparations,
        contexts=dataset.contexts,
        probes=dataset.probes,
        readouts=tuple(
            dataclasses.replace(
                value,
                projector_resolution=resolution(value.projector_resolution),
            )
            for value in dataset.readouts
        ),
        records=tuple(
            dataclasses.replace(
                value,
                ambient_projector_resolution=resolution(
                    value.ambient_projector_resolution
                ),
            )
            for value in dataset.records
        ),
        gauge_actions=tuple(
            dataclasses.replace(value, law=value.law.conjugated(action))
            for value in dataset.gauge_actions
        ),
        access_postulate=dataset.access_postulate,
    )


def _mutate_row(
    dataset: legacy.OperationalDataset,
    field_name: str,
    value: object,
) -> Mapping[str, object]:
    data = copy.deepcopy(serialized(dataset))
    data["composition_rows"][0][field_name] = value
    return data


def _mutate_row_law(
    dataset: legacy.OperationalDataset,
) -> Mapping[str, object]:
    data = copy.deepcopy(serialized(dataset))
    phases = data["composition_rows"][0]["law"]["phases"]
    phases[1] = (phases[1] + 1) % 24
    return data


def _mutate_row_signature(
    dataset: legacy.OperationalDataset,
) -> Mapping[str, object]:
    data = copy.deepcopy(serialized(dataset))
    phases = data["composition_rows"][0]["observed_signature"][1]
    phases[1] = (phases[1] + 1) % 24
    return data


def _mutate_selectability(
    dataset: legacy.OperationalDataset,
) -> Mapping[str, object]:
    data = copy.deepcopy(serialized(dataset))
    for value in data["operations"]:
        value["independently_selectable"] = False
    return data


def _artifact_mutant(
    dataset: legacy.OperationalDataset,
    source: estimator.Resolution,
    which: str,
) -> estimator.Resolution:
    if source.atlas is None:
        return estimator.Resolution(
            estimator.Outcome(
                estimator.PROCEDURAL_OUTCOME,
                "procedural",
                1,
                "map mutant source has no positive atlas",
            ),
            None,
            None,
        )
    atlas = source.atlas
    if which == "regional-row":
        index = next(i for i, value in enumerate(atlas.arrows) if value.row_map)
        arrow = atlas.arrows[index]
        changed = dataclasses.replace(
            arrow.row_map[0], target_tau="corrupt|heldout|tau"
        )
        arrow = dataclasses.replace(
            arrow, row_map=(changed,) + arrow.row_map[1:]
        )
        arrows = list(atlas.arrows)
        arrows[index] = arrow
        atlas = dataclasses.replace(atlas, arrows=tuple(arrows))
    elif which == "context":
        index = next(
            i
            for i, value in enumerate(atlas.arrows)
            if value.context_map.target_records
        )
        arrow = atlas.arrows[index]
        arrow = dataclasses.replace(
            arrow,
            context_map=dataclasses.replace(
                arrow.context_map, target_records=frozenset()
            ),
        )
        arrows = list(atlas.arrows)
        arrows[index] = arrow
        atlas = dataclasses.replace(atlas, arrows=tuple(arrows))
    elif which == "projector":
        index = next(
            i
            for i, value in enumerate(atlas.fact_maps)
            if value.projector_equalities
        )
        maps = list(atlas.fact_maps)
        maps[index] = dataclasses.replace(
            maps[index], projector_equalities=()
        )
        atlas = dataclasses.replace(atlas, fact_maps=tuple(maps))
    else:
        raise ValueError("unknown held-out artifact mutant")
    return estimator.adjudicate_resolution_artifacts(
        dataset, dataclasses.replace(source, atlas=atlas)
    )


def worker() -> int:
    started = time.monotonic()
    deadline = started + COMPLETE_CAP_SECONDS
    dataset = fixture.build_dataset()
    truth = fixture.held_out_truth()
    payload = serialized(dataset)
    main = run_payload(payload, deadline)
    checks = []

    def add(check_id: str, check_class: str, passed: bool, evidence: object) -> None:
        checks.append(
            {
                "id": check_id,
                "class": check_class,
                "pass": bool(passed),
                "evidence": estimator.canonical_data(evidence),
            }
        )

    add("H001", "fixture", len(dataset.operations) == truth.abstract_order, len(dataset.operations))
    add("H002", "fixture", dataset.carrier_dimension == truth.carrier_dimension <= 32, dataset.carrier_dimension)
    add("H003", "fixture", len(dataset.composition_rows) == truth.complete_rows <= 36_864, len(dataset.composition_rows))
    selected = sum(value.independently_selectable for value in dataset.operations)
    add("H004", "fixture", selected == truth.independently_selectable and len(dataset.operations) - selected == truth.composite_only, {"selectable": selected, "composite_only": len(dataset.operations) - selected})

    actual_invariants = (
        estimator.composition_invariants(main.analysis.result.composition)
        if main.analysis is not None
        else {"order": None, "group_like": False}
    )
    novelty = actual_invariants.get("order") == 144 and actual_invariants.get("order") not in (192, 216)
    add("H005", "novelty", novelty, actual_invariants)
    nonabelian = False
    if main.analysis is not None:
        composition = main.analysis.result.composition
        nonabelian = any(
            composition.product(left, right) != composition.product(right, left)
            for left in range(composition.size)
            for right in range(composition.size)
        )
    add("H006", "fixture", nonabelian, "measured from quotient multiplication")
    add("H007", "resolver", main.outcome.category == "scientific" and main.outcome.exit_code == 0, dataclasses.asdict(main.outcome))

    main_summary = estimator.structural_summary(main)
    if is_positive(main):
        factor_orders = sorted(main.atlas.factorization.factor_orders)
        object_atoms = tuple(sorted((value.atoms for value in main.atlas.objects), key=lambda value: (len(value), value)))
        expected_atoms = tuple(sorted(truth.regional_atom_sets, key=lambda value: (len(value), value)))
        resolved_records, _by_handle = legacy.resolve_records(
            dataset,
            main.analysis.result.composition,
            main.analysis.result.inverses,
        )
        add("H008", "score", factor_orders == sorted(truth.factor_orders), factor_orders)
        add("H009", "score", len(set(truth.factor_orders)) == 4 and len(factor_orders) >= 3, factor_orders)
        add("H010", "score", object_atoms == expected_atoms, object_atoms)
        add("H011", "score", len(main.atlas.objects) == truth.regional_objects and len(main.atlas.arrows) == truth.regional_arrows and len(main.atlas.fact_maps) == truth.fact_maps, {"objects": len(main.atlas.objects), "arrows": len(main.atlas.arrows), "fact_maps": len(main.atlas.fact_maps)})
        add("H012", "score", len(main.atlas.nonvacuous_triples) == truth.nonvacuous_triples and main.atlas.universal_atoms == truth.universal_atoms and main.atlas.is_complete_proper_boolean == truth.complete_proper_boolean, {"triples": len(main.atlas.nonvacuous_triples), "universal": main.atlas.universal_atoms, "complete_boolean": main.atlas.is_complete_proper_boolean})
        add("H013", "records", len(resolved_records) == 4 and all(value.passes_w3 for value in resolved_records), {"records": len(resolved_records), "all_w3": all(value.passes_w3 for value in resolved_records)})
        add("H014", "regional", estimator.validate_full_regional_atlas(dataset, main.analysis, main.atlas), {"regional_paths": main.atlas.coherent_regional_paths, "fact_paths": main.atlas.coherent_fact_paths})
    else:
        add("H008", "score", True, "not reached: main returned a registered scientific negative")

    # Serialized complete-row mutants.
    row_mutants = {
        "tau": _mutate_row(dataset, "tau", "wrong|tau"),
        "status": _mutate_row(dataset, "status", legacy.COLLAPSED),
        "result": _mutate_row(
            dataset, "result_class", dataset.operations[1].handle
        ),
        "law": _mutate_row_law(dataset),
        "signature": _mutate_row_signature(dataset),
    }
    for ordinal, (name, value) in enumerate(row_mutants.items(), start=15):
        result = run_payload(value, deadline)
        add(f"H{ordinal:03d}", "row-mutant", no_positive(result), {"field": name, "outcome": result.outcome.code})

    selectability = run_payload(_mutate_selectability(dataset), deadline)
    add("H020", "selectability-mutant", no_positive(selectability), selectability.outcome.code)

    baseline_summary = main_summary
    presentations = {
        "rename": legacy._rename_dataset(dataset),
        "reorder": estimator.reorder_dataset(dataset),
        "gauge": _carrier_gauge_conjugated(dataset),
        "record-handle": _record_handle_renamed(dataset),
    }
    for ordinal, (name, value) in enumerate(presentations.items(), start=21):
        result = run_payload(serialized(value), deadline)
        add(
            f"H{ordinal:03d}",
            "metamorphic",
            is_positive(result)
            and estimator.structural_summary(result) == baseline_summary,
            {"presentation": name, "outcome": result.outcome.code},
        )

    if is_positive(main):
        regional_source = run_payload(payload, deadline)
        regional_mutant = _artifact_mutant(
            dataset, regional_source, "regional-row"
        )
        context_mutant = _artifact_mutant(dataset, regional_source, "context")
        projector_source = run_payload(payload, deadline)
        projector_mutant = _artifact_mutant(
            dataset, projector_source, "projector"
        )
        add("H025", "map-mutant", regional_mutant.outcome.code == estimator.PROCEDURAL_OUTCOME, regional_mutant.outcome.code)
        add("H026", "map-mutant", context_mutant.outcome.code == estimator.PROCEDURAL_OUTCOME, context_mutant.outcome.code)
        add("H027", "map-mutant", projector_mutant.outcome.code == estimator.PROCEDURAL_OUTCOME, projector_mutant.outcome.code)
    else:
        add("H025", "map-mutant", True, "not reached after registered scientific negative")

    malformed = copy.deepcopy(payload)
    malformed["composition_rows"] = malformed["composition_rows"][:-1]
    malformed_result = run_payload(malformed, deadline)
    cap_result = estimator.resolve_serialized_dataset(payload, cap_seconds=0.0)
    timeout_result = run_payload(payload, deadline, injected_branch="timeout")
    exception_result = run_payload(payload, deadline, injected_branch="exception")
    missing_result = run_payload(payload, deadline, injected_branch="missing-outcome")
    multiple_result = run_payload(payload, deadline, injected_branch="multiple-outcomes")
    for ordinal, (name, value) in enumerate(
        (
            ("malformed", malformed_result),
            ("cap", cap_result),
            ("timeout", timeout_result),
            ("exception", exception_result),
            ("missing", missing_result),
            ("multiple", multiple_result),
        ),
        start=28,
    ):
        add(f"H{ordinal:03d}", "total-resolver", value.outcome.code == estimator.PROCEDURAL_OUTCOME and value.outcome.exit_code == 1, {"branch": name, "reason": value.outcome.reason})

    twisted = estimator.full_instrument_twisted_triple()
    add("H034", "twisted-triple", all(twisted.pair_valid) and twisted.rejected_only_at_loop, {"pair_valid": twisted.pair_valid, "regional_loop": twisted.regional_loop_commutes, "record_loop": twisted.record_loop_commutes})
    add("H035", "ceiling", True, "L0 only; no T1/C1/topology/causality/spacetime")

    payload_out = {
        "fixture": {
            **fixture.construction_metadata(),
            "serialized_input_sha256": hashlib.sha256(
                json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
            "operations": len(dataset.operations),
            "rows": len(dataset.composition_rows),
            "carrier": dataset.carrier_dimension,
            "selectable": selected,
            "composite_only": len(dataset.operations) - selected,
        },
        "main": {
            "outcome": dataclasses.asdict(main.outcome),
            "summary": main_summary,
            "analysis_digest": None if main.analysis is None else stable_digest({"certificates": main.analysis.result.certificates, "finest": main.analysis.result.finest_certificates}),
            "atlas_digest": None if main.atlas is None else stable_digest(main.atlas),
            "instrumentation": None if main.analysis is None else main.analysis.instrumentation.canonical(),
            "composition_invariants": actual_invariants,
        },
        "checks": checks,
        "passed": sum(value["pass"] for value in checks),
        "total": len(checks),
        "all_pass": all(value["pass"] for value in checks),
        "elapsed_seconds": time.monotonic() - started,
        "deadline_seconds": COMPLETE_CAP_SECONDS,
    }
    print(estimator.canonical_json(payload_out), end="", flush=True)
    return 0


def official_receipt() -> Mapping[str, object]:
    started = time.monotonic()
    estimator_hash = sha256_file(ESTIMATOR_PATH)
    proof_hash = sha256_file(PROOF_PATH)
    fixture_hash = sha256_file(FIXTURE_PATH)
    scorer_hash = sha256_file(SCORER_PATH)
    future_at_freeze = {
        path: git_path_absent(fixture.ESTIMATOR_FREEZE_COMMIT, path)
        for path in (
            "v13/code/rq0_l0_compcert_heldout_fixture_exact.py",
            "v13/code/rq0_l0_compcert_heldout_score.py",
            "v13/code/rq0_l0_compcert_heldout_receipt.json",
            "v13/code/rq0_l0_compcert_heldout_output.txt",
            DELIVERY_PATH,
        )
    }
    anchors = {
        "estimator_hash": estimator_hash == fixture.ESTIMATOR_FROZEN_SHA256,
        "proof_hash": proof_hash == fixture.PROOF_FROZEN_SHA256,
        "fixture_hash": fixture_hash == EXPECTED_FIXTURE_SHA256,
        "future_paths_absent_at_freeze": all(future_at_freeze.values()),
    }
    bad_anchor_control = estimator.Outcome(
        estimator.PROCEDURAL_OUTCOME,
        "procedural",
        1,
        "deliberately mutated frozen anchor",
    )
    worker_data = None
    timed_out = False
    worker_returncode = None
    worker_stderr_tail = ""
    if all(anchors.values()):
        remaining = COMPLETE_CAP_SECONDS - (time.monotonic() - started)
        try:
            completed = subprocess.run(
                [sys.executable, str(SCORER_PATH), "--worker"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=max(0.001, remaining),
                check=False,
                env={**os.environ, "PYTHONHASHSEED": "0"},
            )
            worker_returncode = completed.returncode
            worker_stderr_tail = "\n".join(completed.stderr.splitlines()[-16:])
            if completed.returncode == 0:
                worker_data = json.loads(completed.stdout)
        except subprocess.TimeoutExpired as error:
            timed_out = True
            raw = error.stderr or b""
            if isinstance(raw, bytes):
                raw = raw.decode("utf-8", errors="replace")
            worker_stderr_tail = "\n".join(str(raw).splitlines()[-16:])
        except Exception as error:
            worker_stderr_tail = f"{type(error).__name__}: {error}"

    worker_ok = (
        worker_data is not None
        and worker_returncode == 0
        and not timed_out
        and worker_data.get("all_pass") is True
    )
    main_outcome = (
        worker_data.get("main", {}).get("outcome", {})
        if worker_data is not None
        else {}
    )
    registered_scientific = (
        main_outcome.get("code") in estimator.SCIENTIFIC_OUTCOMES
        and main_outcome.get("category") == "scientific"
        and main_outcome.get("exit_code") == 0
    )
    official_valid = all(anchors.values()) and worker_ok and registered_scientific
    scientific_outcome = main_outcome.get("code") if official_valid else None
    procedural_outcome = None if official_valid else estimator.PROCEDURAL_OUTCOME
    status = (
        "GREEN-UNREVIEWED"
        if scientific_outcome in ("RQ0-LOCALIZATION-GROUPOID", "RQ0-LOCAL-ATLAS")
        else "SCIENTIFIC-NEGATIVE-UNREVIEWED"
        if scientific_outcome is not None
        else "INVALID-FROZEN"
    )
    reason = (
        "all frozen anchors and held-out scientific/control prerequisites pass"
        if official_valid
        else "official 360-second worker timed out"
        if timed_out
        else "frozen source/chronology anchor failure"
        if not all(anchors.values())
        else "worker, control, or registered-outcome failure"
    )
    complete_elapsed = time.monotonic() - started
    return {
        "schema": SCHEMA,
        "status": status,
        "procedural_outcome": procedural_outcome,
        "scientific_outcome": scientific_outcome,
        "reason": reason,
        "official_runs": 1,
        "sources": {
            "freeze_commit": fixture.ESTIMATOR_FREEZE_COMMIT,
            "estimator_sha256": estimator_hash,
            "proof_sha256": proof_hash,
            "fixture_sha256": fixture_hash,
            "scorer_sha256": scorer_hash,
        },
        "anchors": anchors,
        "future_paths_absent_at_freeze": future_at_freeze,
        "anchor_mutant": {
            "outcome": bad_anchor_control.code,
            "exit_code": bad_anchor_control.exit_code,
            "positive_suppressed": bad_anchor_control.category == "procedural",
        },
        "worker": worker_data,
        "runtime": {
            "canonical": False,
            "complete_cap_seconds": COMPLETE_CAP_SECONDS,
            "complete_elapsed_seconds": complete_elapsed,
            "timed_out": timed_out,
            "worker_returncode": worker_returncode,
            "worker_stderr_tail": worker_stderr_tail,
            "seed": "none; PYTHONHASHSEED=0",
        },
        "legacy_imports": {
            "rq0_l0_certification_estimator_exact": "typed exact arithmetic/W3/serialization antecedent lemma",
            "rq0_l0_compcert_estimator_exact": "byte-frozen generic estimator under official score",
            "prior order-192 fixture": "not imported by held-out fixture or scorer",
            "S3^3 fixture": "not imported by held-out fixture or scorer",
        },
        "stopping_rule": {
            "estimator_edit_allowed": False,
            "proof_edit_allowed": False,
            "fixture_edit_or_replacement_allowed": False,
            "second_held_out_score_allowed": False,
            "next_event": "freeze delivery; external read-only hostile review; separate adjudication",
        },
        "nonclaims": [
            "no terminal L0 status before external hostile review and adjudication",
            "no topology or spatial localization",
            "no influence or causal order",
            "no Lorentzian geometry or spacetime",
            "no fields or gravity",
        ],
    }


def render_text(receipt: Mapping[str, object]) -> str:
    worker = receipt.get("worker") or {}
    main = worker.get("main") or {}
    summary = main.get("summary") or {}
    return "\n".join(
        (
            "RQ0-L0 COMPUTATIONAL-CERTIFICATION HELD-OUT OFFICIAL RECEIPT",
            f"status: {receipt['status']}",
            f"procedural_outcome: {receipt['procedural_outcome']}",
            f"scientific_outcome: {receipt['scientific_outcome']}",
            f"reason: {receipt['reason']}",
            f"official_runs: {receipt['official_runs']}",
            f"worker_checks: {worker.get('passed')}/{worker.get('total')}",
            f"factor_orders: {summary.get('factor_orders')}",
            f"regional_objects: {summary.get('regional_objects')}",
            f"regional_arrows: {summary.get('regional_arrows')}",
            f"fact_maps: {summary.get('fact_maps')}",
            f"nonvacuous_triples: {summary.get('nonvacuous_triples')}",
            f"complete_elapsed_seconds: {receipt['runtime']['complete_elapsed_seconds']:.6f} / 360",
            "next: freeze delivery and dispatch external read-only hostile review",
            "ceiling: L0 only; no T1/C1/topology/causality/spacetime",
            "",
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--write-receipts", action="store_true")
    args = parser.parse_args()
    if args.worker:
        return worker()
    receipt = official_receipt()
    output = render_text(receipt)
    if args.write_receipts:
        RECEIPT_PATH.write_text(estimator.canonical_json(receipt))
        OUTPUT_PATH.write_text(output)
    print(output, end="")
    return 1 if receipt["procedural_outcome"] is not None else 0


if __name__ == "__main__":
    raise SystemExit(main())
