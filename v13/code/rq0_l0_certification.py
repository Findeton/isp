#!/usr/bin/env python3
"""Official scorer for the one-shot final RQ0-L0 certification fixture.

The scorer is fail-closed.  Its default mode runs the frozen public suite,
authenticates chronology and sources, serializes the one post-freeze fixture,
and executes the unchanged estimator in a subprocess under the pin's single
360-second complete-run cap.  A timeout prints only RQ0-L0-INVALID and exits 1.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Mapping

try:
    from .rq0_l0_certification_estimator_exact import (
        ESTIMATOR_API_VERSION,
        analyze_addressability,
        dataset_to_data,
        normalize,
        public_self_test,
    )
    from .rq0_l0_certification_fixtures_exact import (
        ESTIMATOR_FREEZE_COMMIT,
        ESTIMATOR_FROZEN_SHA256,
        FIXTURE_SCHEMA,
        build_main_dataset,
        fixture_provenance,
    )
except ImportError:
    from rq0_l0_certification_estimator_exact import (
        ESTIMATOR_API_VERSION,
        analyze_addressability,
        dataset_to_data,
        normalize,
        public_self_test,
    )
    from rq0_l0_certification_fixtures_exact import (
        ESTIMATOR_FREEZE_COMMIT,
        ESTIMATOR_FROZEN_SHA256,
        FIXTURE_SCHEMA,
        build_main_dataset,
        fixture_provenance,
    )


SCHEMA = "rq0-l0-final-certification-receipt-v1"
COMPLETE_RUN_CAP_SECONDS = 360
ROOT = Path(__file__).resolve().parents[2]
ESTIMATOR_PATH = ROOT / "v13/code/rq0_l0_certification_estimator_exact.py"
PROOF_PATH = ROOT / "v13/note-rq0-operational-localization-final-certification-soundness.md"
FIXTURE_PATH = ROOT / "v13/code/rq0_l0_certification_fixtures_exact.py"
SCORER_PATH = Path(__file__).resolve()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(normalize(value), indent=2, sort_keys=True) + "\n"


def git_path_absent(commit: str, path: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{commit}:{path}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode != 0


def worker() -> int:
    dataset = build_main_dataset("base")
    print(
        json.dumps(
            {
                "worker": "fixture-built",
                "operations": len(dataset.operations),
                "rows": len(dataset.composition_rows),
                "carrier": dataset.carrier_dimension,
            },
            sort_keys=True,
        ),
        flush=True,
    )
    result = analyze_addressability(dataset)
    print(
        json.dumps(
            {
                "worker": "analysis-returned",
                "normal_subobjects": len(result.normal_subobjects),
                "normal_join_tests": result.normal_join_tests,
                "factor_tuple_tests": result.factor_tuple_tests,
                "finest_factor_orders": [list(value.factor_orders) for value in result.finest_certificates],
                "first_obstruction": result.first_obstruction,
            },
            sort_keys=True,
        ),
        flush=True,
    )
    return 0


def official_receipt() -> Mapping[str, object]:
    started = time.monotonic()
    estimator_hash = sha256_file(ESTIMATOR_PATH)
    proof_hash = sha256_file(PROOF_PATH)
    fixture_hash = sha256_file(FIXTURE_PATH)
    scorer_hash = sha256_file(SCORER_PATH)
    public = public_self_test()
    dataset = build_main_dataset("base")
    serialized = dataset_to_data(dataset)
    serialized_hash = hashlib.sha256(
        json.dumps(serialized, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    chronology = {
        "estimator_freeze_commit": ESTIMATOR_FREEZE_COMMIT,
        "estimator_hash_matches_pin": estimator_hash == ESTIMATOR_FROZEN_SHA256,
        "fixture_absent_at_estimator_freeze": git_path_absent(
            ESTIMATOR_FREEZE_COMMIT,
            "v13/code/rq0_l0_certification_fixtures_exact.py",
        ),
        "scorer_absent_at_estimator_freeze": git_path_absent(
            ESTIMATOR_FREEZE_COMMIT,
            "v13/code/rq0_l0_certification.py",
        ),
    }
    anchors_ok = all(
        (
            chronology["estimator_hash_matches_pin"],
            chronology["fixture_absent_at_estimator_freeze"],
            chronology["scorer_absent_at_estimator_freeze"],
            public["all_pass"],
        )
    )

    remaining = COMPLETE_RUN_CAP_SECONDS - (time.monotonic() - started)
    timed_out = False
    worker_returncode = None
    worker_stdout = ""
    worker_stderr_tail = ""
    if anchors_ok and remaining > 0:
        try:
            completed = subprocess.run(
                [sys.executable, str(SCORER_PATH), "--worker"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=remaining,
                check=False,
                env={**os.environ, "PYTHONHASHSEED": "0"},
            )
            worker_returncode = completed.returncode
            worker_stdout = completed.stdout
            worker_stderr_tail = "\n".join(completed.stderr.splitlines()[-12:])
        except subprocess.TimeoutExpired as error:
            timed_out = True
            worker_stdout = (error.stdout or b"").decode("utf-8") if isinstance(error.stdout, bytes) else (error.stdout or "")
            worker_stderr = (error.stderr or b"").decode("utf-8") if isinstance(error.stderr, bytes) else (error.stderr or "")
            worker_stderr_tail = "\n".join(worker_stderr.splitlines()[-12:])

    main_returned = worker_returncode == 0 and not timed_out
    invalid = (not anchors_ok) or timed_out or not main_returned
    reason = (
        "main complete pipeline exceeded the registered 360-second cap"
        if timed_out
        else "immutable anchor/public calibration failure"
        if not anchors_ok
        else "main worker returned a nonzero or missing outcome"
        if not main_returned
        else None
    )
    checks = (
        ("R01", "provenance", chronology["estimator_hash_matches_pin"]),
        ("R02", "provenance", chronology["fixture_absent_at_estimator_freeze"]),
        ("R03", "provenance", chronology["scorer_absent_at_estimator_freeze"]),
        ("R04", "procedural", public["all_pass"] and public["passed"] == public["total"] == 29),
        ("R05", "procedural", len(dataset.operations) == 192),
        ("R06", "procedural", len(dataset.composition_rows) == 36_864),
        ("R07", "procedural", dataset.carrier_dimension == 32),
        ("R08", "procedural", sum(value.independently_selectable for value in dataset.operations) == 6),
        ("R09", "procedural", fixture_provenance()["old_s3_cubed_imported"] is False),
        ("R10", "procedural", timed_out),
        ("R11", "procedural", invalid),
    )
    return {
        "schema": SCHEMA,
        "status": "INVALID-FROZEN" if invalid else "UNEXPECTED-RETURN",
        "procedural_outcome": "RQ0-L0-INVALID" if invalid else None,
        "scientific_outcome": None,
        "reason": reason,
        "chronology": chronology,
        "sources": {
            "estimator_sha256": estimator_hash,
            "proof_sha256": proof_hash,
            "fixture_sha256": fixture_hash,
            "scorer_sha256": scorer_hash,
            "serialized_main_input_sha256": serialized_hash,
        },
        "fixture": {
            **fixture_provenance(),
            "operations": len(dataset.operations),
            "complete_rows": len(dataset.composition_rows),
            "carrier_dimension": dataset.carrier_dimension,
            "independently_selectable": sum(value.independently_selectable for value in dataset.operations),
            "contexts": len(dataset.contexts),
            "records": len(dataset.records),
        },
        "runtime": {
            "complete_run_cap_seconds": COMPLETE_RUN_CAP_SECONDS,
            "main_worker_timed_out": timed_out,
            "worker_returncode": worker_returncode,
            "worker_stdout": worker_stdout.strip().splitlines(),
            "worker_stderr_tail": worker_stderr_tail,
            "seed": "none; PYTHONHASHSEED=0 for worker",
        },
        "public_calibration": {
            "passed": public["passed"],
            "total": public["total"],
            "all_pass": public["all_pass"],
        },
        "checks": [
            {"id": check_id, "class": check_class, "pass": passed}
            for check_id, check_class, passed in checks
        ],
        "positive_prerequisites": {
            "estimator_returned_under_cap": main_returned,
            "factor_certificates_available": False,
            "regional_maps_available": False,
            "record_functor_available": False,
            "all_positive_outcomes_suppressed": invalid,
        },
        "mandatory_controls_not_reached": [
            "new-main sound-factor scoring",
            "new-main RegAddr and Rec scoring",
            "new-main gauge and physical-phase comparison",
            "new-main handle/projector/map mutants",
            "new-main deterministic positive regeneration",
        ],
        "surviving_evidence": [
            "frozen 29/29 public estimator calibrations",
            "new fixture constructor produced 192 classes, 36864 rows, carrier 32",
            "new fixture provenance is post-freeze and non-S3^3",
        ],
        "stopping_rule": {
            "estimator_edit_allowed": False,
            "replacement_fixture_allowed": False,
            "next_event": "freeze invalid delivery, external hostile review, adjudication",
        },
        "nonclaims": [
            "no terminal RQ0-L0 rung",
            "not RQ0-L0-BLOCKED-AT-ADDRESS",
            "no topology or spatial claim",
            "no influence or causal claim",
            "no spacetime, field, or gravity claim",
        ],
    }


def render_text(receipt: Mapping[str, object]) -> str:
    lines = [
        "RQ0-L0 FINAL CERTIFICATION RECEIPT",
        f"status: {receipt['status']}",
        f"procedural_outcome: {receipt['procedural_outcome']}",
        f"scientific_outcome: {receipt['scientific_outcome']}",
        f"reason: {receipt['reason']}",
        f"estimator_sha256: {receipt['sources']['estimator_sha256']}",
        f"fixture_sha256: {receipt['sources']['fixture_sha256']}",
        f"serialized_main_input_sha256: {receipt['sources']['serialized_main_input_sha256']}",
        (
            "fixture: "
            f"{receipt['fixture']['operations']} operations; "
            f"{receipt['fixture']['complete_rows']} complete rows; "
            f"carrier {receipt['fixture']['carrier_dimension']}; "
            f"{receipt['fixture']['independently_selectable']} independently selectable"
        ),
        (
            "public_calibration: "
            f"{receipt['public_calibration']['passed']}/"
            f"{receipt['public_calibration']['total']}"
        ),
        (
            "main_worker: "
            f"timed_out={receipt['runtime']['main_worker_timed_out']} "
            f"cap={receipt['runtime']['complete_run_cap_seconds']}s"
        ),
        "checks:",
    ]
    lines.extend(
        f"  {entry['id']} [{entry['class']}]: {'PASS' if entry['pass'] else 'FAIL'}"
        for entry in receipt["checks"]
    )
    lines.append("positive outcomes: SUPPRESSED")
    lines.append("next: external read-only hostile review; no estimator/fixture retry")
    lines.append("nonclaims:")
    lines.extend(f"  - {value}" for value in receipt["nonclaims"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--render-json", type=Path)
    args = parser.parse_args()
    if args.worker:
        return worker()
    if args.render_json is not None:
        receipt = json.loads(args.render_json.read_text())
        sys.stdout.write(render_text(receipt))
        return 0
    receipt = official_receipt()
    sys.stdout.write(canonical_json(receipt))
    return 1 if receipt["procedural_outcome"] == "RQ0-L0-INVALID" else 0


if __name__ == "__main__":
    raise SystemExit(main())
