#!/usr/bin/env python3
"""Untrusted public proposer and one total fail-closed architecture boundary.

The proposer may suggest factor or overlap claims.  Acceptance is determined
only by ``rq0_l0_archreset_verifier_exact``, which does not import this module.
This is a public pre-freeze engineering surface and emits no RQ0 scientific
outcome.
"""

from __future__ import annotations

import copy
import dataclasses
import itertools
import json
import signal
import threading
import time
from typing import Callable, Dict, FrozenSet, Mapping, Optional, Sequence, Tuple

try:
    from .rq0_l0_archreset_kernel_exact import MonomialLaw
    from . import rq0_l0_archreset_verifier_exact as trusted
except ImportError:
    from rq0_l0_archreset_kernel_exact import MonomialLaw
    import rq0_l0_archreset_verifier_exact as trusted


REQUEST_SCHEMA = "rq0-l0-archreset-request-v1"
RESPONSE_SCHEMA = "rq0-l0-archreset-response-v1"

PUBLIC_PASS = "ARCHRESET-PUBLIC-PASS"
PUBLIC_NEGATIVE = "ARCHRESET-PUBLIC-SCIENTIFIC-NEGATIVE"
INVALID = "ARCHRESET-INVALID"

ACTIONS = frozenset(
    (
        "ESTIMATE-DIRECT-FACTORS",
        "ESTIMATE-OVERLAP",
        "VERIFY-FACTOR-CLAIM",
        "VERIFY-OVERLAP-CLAIM",
        "VERIFY-TRIPLE",
    )
)


class ProposalError(ValueError):
    pass


def _exact_request(value: object) -> Tuple[str, int, object, object]:
    if type(value) is not dict:
        raise ProposalError("request must be an exact mapping")
    keys = frozenset(("schema", "action", "cap_milliseconds", "dataset", "claim"))
    if frozenset(value) != keys or any(type(key) is not str for key in value):
        raise ProposalError("request has missing, unknown or mistyped keys")
    if type(value["schema"]) is not str or value["schema"] != REQUEST_SCHEMA:
        raise ProposalError("request schema is mistyped")
    if type(value["action"]) is not str or value["action"] not in ACTIONS:
        raise ProposalError("request action is mistyped")
    if type(value["cap_milliseconds"]) is not int or value["cap_milliseconds"] <= 0:
        raise ProposalError("cap_milliseconds must be an exact positive integer")
    action = value["action"]
    if action in ("ESTIMATE-DIRECT-FACTORS", "ESTIMATE-OVERLAP") and value["claim"] is not None:
        raise ProposalError("estimation request may not carry a supplied claim")
    if action in ("VERIFY-FACTOR-CLAIM", "VERIFY-OVERLAP-CLAIM") and (
        type(value["dataset"]) is not dict or type(value["claim"]) is not dict
    ):
        raise ProposalError("claim verification requires raw dataset and claim mappings")
    if action == "VERIFY-TRIPLE" and (
        value["dataset"] is not None or type(value["claim"]) is not dict
    ):
        raise ProposalError("triple verification requires null dataset and a raw triple claim")
    if action in ("ESTIMATE-DIRECT-FACTORS", "ESTIMATE-OVERLAP") and type(value["dataset"]) is not dict:
        raise ProposalError("estimation requires a raw dataset mapping")
    return action, value["cap_milliseconds"], value["dataset"], value["claim"]


def _legacy_dataset(dataset: trusted.Dataset):
    """Convert trusted parsed data for the opened legacy proposer only."""

    try:
        from . import rq0_l0_certification_estimator_exact as legacy
    except ImportError:
        import rq0_l0_certification_estimator_exact as legacy

    def law(value: MonomialLaw):
        return legacy.MonomialLaw(value.permutation, value.phases)

    operations = tuple(
        legacy.OperationClass(
            value.handle,
            value.source_type,
            value.target_type,
            law(value.law),
            value.observed_signature,
            value.independently_selectable,
        )
        for value in dataset.operations
    )
    rows = tuple(
        legacy.CompositionRow(
            value.left,
            value.right,
            value.tau,
            value.status,
            value.result_class,
            None if value.law is None else law(value.law),
            value.observed_signature,
        )
        for value in dataset.rows
    )
    return legacy.OperationalDataset(
        handle=dataset.handle,
        carrier_dimension=dataset.carrier_dimension,
        operations=operations,
        composition_rows=rows,
        preparations=(),
        contexts=(),
        probes=(),
        readouts=(),
        records=(),
        gauge_actions=(),
        access_postulate=dataset.access_postulate,
    )


def propose_direct_factors(dataset_raw: object, deadline: float) -> Mapping[str, object]:
    """Untrusted generic proposer using the opened direct-factor engine."""

    try:
        from . import rq0_l0_compcert_estimator_exact as legacy_proposer
    except ImportError:
        import rq0_l0_compcert_estimator_exact as legacy_proposer
    dataset = trusted.parse_dataset(dataset_raw)
    analysis = legacy_proposer.analyze_addressability(
        _legacy_dataset(dataset), deadline=deadline
    )
    if not analysis.result.finest_certificates:
        return {
            "schema": trusted.FACTOR_CLAIM_SCHEMA,
            "kind": "DIRECT-FACTOR-NONE",
            "certificates": [],
            "obstruction": analysis.result.first_obstruction or "public proposer found no eligible proper factor tuple",
        }
    certificates = []
    for value in analysis.result.finest_certificates:
        factors = [
            sorted(analysis.result.composition.classes[index].aliases[0] for index in factor)
            for factor in value.factors
        ]
        predicates = {
            "P1": value.independently_generated,
            "P2": value.mixed_implemented_both_orders,
            "P3": value.operationally_commuting,
            "P4": value.faithful_multiplication,
            "P5": value.closed_with_inverses,
            "P6": value.typed_scalar_intersection,
            "P7": value.represented_algebra_product,
            "P8": value.restriction_stable,
        }
        certificates.append(
            {
                "factors": factors,
                "asserted_predicates": predicates,
                "asserted_passes": all(predicates.values()),
            }
        )
    return {
        "schema": trusted.FACTOR_CLAIM_SCHEMA,
        "kind": "DIRECT-FACTOR-CERTIFICATES",
        "certificates": certificates,
        "obstruction": None,
    }


def _restrict_raw_dataset(
    ambient: Mapping[str, object],
    scope: FrozenSet[str],
    handle: str,
) -> Mapping[str, object]:
    value = copy.deepcopy(ambient)
    value["handle"] = handle
    value["operations"] = [item for item in value["operations"] if item["handle"] in scope]
    value["composition_rows"] = [
        item
        for item in value["composition_rows"]
        if item["left"] in scope and item["right"] in scope
    ]
    value["records"] = [
        item for item in value["records"] if set(item["access_operations"]) <= scope
    ]
    record_handles = {item["handle"] for item in value["records"]}
    value["contexts"] = [
        item
        for item in value["contexts"]
        if set(item["operation_handles"]) <= scope
        and set(item["record_handles"]) <= record_handles
    ]
    return value


def _identity_pairs(source: Sequence[Mapping[str, object]], target: Sequence[Mapping[str, object]]) -> list[Mapping[str, str]]:
    targets = {value["handle"] for value in target}
    return [
        {"source": value["handle"], "target": value["handle"]}
        for value in source
        if value["handle"] in targets
    ]


def _full_identity_row_map(value: Mapping[str, object]) -> Mapping[str, object]:
    """Serialize all row fields into a proposed regional map for replay."""

    return {
        "source_left": value["left"],
        "source_right": value["right"],
        "target_left": value["left"],
        "target_right": value["right"],
        "source_tau": value["tau"],
        "target_tau": value["tau"],
        "source_status": value["status"],
        "target_status": value["status"],
        "source_result_class": value["result_class"],
        "target_result_class": value["result_class"],
        "source_law": value["law"],
        "target_law": value["law"],
        "source_observed_signature": value["observed_signature"],
        "target_observed_signature": value["observed_signature"],
    }


def _identity_regaddr(
    source: Mapping[str, object],
    target: Mapping[str, object],
    handle: str,
) -> Mapping[str, object]:
    same = source["handle"] == target["handle"]
    source_operations = {value["handle"] for value in source["operations"]}
    target_operations = {value["handle"] for value in target["operations"]}
    if not source_operations <= target_operations:
        raise ProposalError("proposed regional embedding is not a subinstrument")
    return {
        "schema": trusted.REGADDR_SCHEMA,
        "handle": handle,
        "kind": "ISOMORPHISM" if same else "EMBEDDING",
        "source": source["handle"],
        "target": target["handle"],
        "carrier_action": MonomialLaw.unit(source["carrier_dimension"]).to_raw(),
        "operation_map": [
            {"source": value, "target": value} for value in sorted(source_operations)
        ],
        "row_map": [
            _full_identity_row_map(value) for value in source["composition_rows"]
        ],
        "preparation_map": _identity_pairs(source["preparations"], target["preparations"]),
        "context_map": _identity_pairs(source["contexts"], target["contexts"]),
        "probe_map": _identity_pairs(source["probes"], target["probes"]),
        "readout_map": _identity_pairs(source["readouts"], target["readouts"]),
        "record_map": _identity_pairs(source["records"], target["records"]),
        "gauge_map": _identity_pairs(source["gauge_actions"], target["gauge_actions"]),
    }


def propose_overlap(dataset_raw: object) -> Mapping[str, object]:
    """Untrusted overlap-first proposer using no direct-factor output."""

    ambient = trusted.parse_dataset(dataset_raw)
    op_scopes = trusted.operational_scopes(ambient)
    rec_scopes = trusted.record_scopes(ambient)
    if op_scopes != rec_scopes:
        return {
            "schema": trusted.ATLAS_CLAIM_SCHEMA,
            "kind": "OVERLAP-FIRST-NONE",
            "op_scopes": [sorted(value) for value in op_scopes],
            "rec_scopes": [sorted(value) for value in rec_scopes],
            "objects": [],
            "arrows": [],
            "pair_intersections": [],
            "triple_intersections": [],
        }

    ambient_scope = frozenset(value.handle for value in ambient.operations)
    ordered_scopes = tuple(sorted(op_scopes, key=lambda value: (len(value), tuple(sorted(value)))))
    raw_objects = [copy.deepcopy(dataset_raw)]
    scope_to_object: Dict[FrozenSet[str], Mapping[str, object]] = {ambient_scope: raw_objects[0]}
    for index, scope in enumerate(ordered_scopes):
        handle = f"{ambient.handle}-region-{index:03d}"
        region = _restrict_raw_dataset(dataset_raw, scope, handle)
        scope_to_object[scope] = region
        raw_objects.append(region)

    arrows = []
    arrow_by_endpoints: Dict[Tuple[str, str], str] = {}
    all_scopes = ordered_scopes + (ambient_scope,)
    for source_scope in all_scopes:
        for target_scope in all_scopes:
            if not source_scope <= target_scope:
                continue
            source = scope_to_object[source_scope]
            target = scope_to_object[target_scope]
            handle = f"map-{len(arrows):03d}"
            arrows.append(_identity_regaddr(source, target, handle))
            arrow_by_endpoints[(source["handle"], target["handle"])] = handle

    maximal = tuple(
        scope
        for scope in ordered_scopes
        if not any(scope < other for other in ordered_scopes)
    )
    pairs = []
    for left_scope, right_scope in itertools.combinations(maximal, 2):
        intersection = left_scope & right_scope
        if intersection not in scope_to_object:
            continue
        left = scope_to_object[left_scope]
        right = scope_to_object[right_scope]
        common = scope_to_object[intersection]
        ambient_raw = scope_to_object[ambient_scope]
        pairs.append(
            {
                "left": left["handle"],
                "right": right["handle"],
                "intersection": common["handle"],
                "ambient": ambient_raw["handle"],
                "to_left": arrow_by_endpoints[(common["handle"], left["handle"])],
                "to_right": arrow_by_endpoints[(common["handle"], right["handle"])],
                "left_to_ambient": arrow_by_endpoints[(left["handle"], ambient_raw["handle"])],
                "right_to_ambient": arrow_by_endpoints[(right["handle"], ambient_raw["handle"])],
                "intersection_to_ambient": arrow_by_endpoints[(common["handle"], ambient_raw["handle"])],
            }
        )
    triples = []
    for regions in itertools.combinations(maximal, 3):
        intersection = frozenset.intersection(*regions)
        if intersection not in scope_to_object:
            continue
        common = scope_to_object[intersection]
        region_objects = tuple(scope_to_object[value] for value in regions)
        ambient_raw = scope_to_object[ambient_scope]
        triples.append(
            {
                "regions": [value["handle"] for value in region_objects],
                "intersection": common["handle"],
                "ambient": ambient_raw["handle"],
                "to_regions": [
                    arrow_by_endpoints[(common["handle"], value["handle"])]
                    for value in region_objects
                ],
                "region_to_ambient": [
                    arrow_by_endpoints[(value["handle"], ambient_raw["handle"])]
                    for value in region_objects
                ],
                "intersection_to_ambient": arrow_by_endpoints[(common["handle"], ambient_raw["handle"])],
            }
        )
    return {
        "schema": trusted.ATLAS_CLAIM_SCHEMA,
        "kind": "OVERLAP-FIRST-ATLAS",
        "op_scopes": [sorted(value) for value in op_scopes],
        "rec_scopes": [sorted(value) for value in rec_scopes],
        "objects": raw_objects,
        "arrows": arrows,
        "pair_intersections": pairs,
        "triple_intersections": triples,
    }


def _summary(value: object) -> Mapping[str, object]:
    if isinstance(value, trusted.FactorVerification):
        return {
            "verification": "factor",
            "category": value.category,
            "certificates": len(value.certificates),
            "factor_orders": [list(item.factor_orders) for item in value.certificates],
            "exhaustive_candidates": value.exhaustive_candidates,
        }
    if isinstance(value, trusted.AtlasVerification):
        return {
            "verification": "overlap",
            **dataclasses.asdict(value),
        }
    if isinstance(value, trusted.TripleVerification):
        return {
            "verification": "triple",
            **dataclasses.asdict(value),
        }
    raise ProposalError("unknown trusted verification object")


def _response(status: str, exit_code: int, phase: str, detail: object) -> Mapping[str, object]:
    return {
        "schema": RESPONSE_SCHEMA,
        "engineering_status": status,
        "exit_code": exit_code,
        "phase": phase,
        "detail": detail,
    }


def total_entry(
    request_raw: object,
    *,
    serializer: Callable[..., str] = json.dumps,
    clock: Callable[[], float] = time.monotonic,
) -> Tuple[int, str]:
    """Return exactly one serialized response; no exception escapes."""

    phase = "request"
    alarm_state = None
    try:
        action, cap_milliseconds, dataset_raw, supplied_claim = _exact_request(request_raw)
        phase = "cap"
        started = clock()
        if type(started) is not float or not math_is_finite(started):
            raise ProposalError("clock returned a nonfinite or mistyped value")
        deadline = started + cap_milliseconds / 1000.0

        # Deep exact schema validation can itself be computationally large.
        # On the main Unix thread, enforce the registered wall cap around the
        # entire remaining boundary rather than checking only between phases.
        if threading.current_thread() is not threading.main_thread():
            raise ProposalError("total entry requires the main thread for hard-cap enforcement")
        previous_handler = signal.getsignal(signal.SIGALRM)
        previous_timer = signal.getitimer(signal.ITIMER_REAL)
        if previous_timer != (0.0, 0.0):
            raise ProposalError("pre-existing real-time alarm is unsupported")

        def cap_alarm(_signum: int, _frame: object) -> None:
            raise TimeoutError("public architecture cap exhausted")

        signal.signal(signal.SIGALRM, cap_alarm)
        signal.setitimer(signal.ITIMER_REAL, cap_milliseconds / 1000.0)
        alarm_state = (previous_handler, previous_timer)

        def check_deadline() -> None:
            current = clock()
            if type(current) is not float or not math_is_finite(current):
                raise ProposalError("clock returned a nonfinite or mistyped value")
            if current > deadline:
                raise TimeoutError("public architecture cap exhausted")

        phase = "parse"
        if action == "VERIFY-TRIPLE":
            parsed_dataset = None
        else:
            parsed_dataset = trusted.parse_dataset(dataset_raw)
        check_deadline()

        phase = "estimate"
        if action == "ESTIMATE-DIRECT-FACTORS":
            claim = propose_direct_factors(dataset_raw, deadline)
        elif action == "ESTIMATE-OVERLAP":
            claim = propose_overlap(dataset_raw)
        else:
            claim = supplied_claim
        # Raw JSON round-trip severs proposer object identity before trust.
        claim = json.loads(json.dumps(claim, sort_keys=True, separators=(",", ":")))
        check_deadline()

        phase = "verify"
        if action in ("ESTIMATE-DIRECT-FACTORS", "VERIFY-FACTOR-CLAIM"):
            verification = trusted.verify_factor_claim(dataset_raw, claim, check_deadline)
            category = verification.category
        elif action in ("ESTIMATE-OVERLAP", "VERIFY-OVERLAP-CLAIM"):
            verification = trusted.verify_overlap_claim(dataset_raw, claim)
            category = verification.category
        else:
            verification = trusted.verify_full_triple(claim)
            category = "positive"
        check_deadline()

        phase = "resolve"
        status = PUBLIC_NEGATIVE if category == "scientific-negative" else PUBLIC_PASS
        response = _response(status, 0, "complete", _summary(verification))

        phase = "serialize"
        text = serializer(response, sort_keys=True, separators=(",", ":"))
        if type(text) is not str:
            raise ProposalError("response serializer did not return text")
        return 0, text + ("" if text.endswith("\n") else "\n")
    except BaseException as error:
        # The fallback uses the standard encoder even when the injected public
        # serializer is the failing component.  This branch itself contains
        # only primitive JSON values.
        response = _response(
            INVALID,
            1,
            phase,
            {"error_type": type(error).__name__, "message": str(error)},
        )
        try:
            return 1, json.dumps(response, sort_keys=True, separators=(",", ":")) + "\n"
        except BaseException:
            return 1, '{"detail":{"error_type":"FatalSerialization","message":"fallback failed"},"engineering_status":"ARCHRESET-INVALID","exit_code":1,"phase":"serialize","schema":"rq0-l0-archreset-response-v1"}\n'
    finally:
        if alarm_state is not None:
            try:
                signal.setitimer(signal.ITIMER_REAL, 0.0)
                signal.signal(signal.SIGALRM, alarm_state[0])
            except BaseException:
                # The structured response has already been determined.  Alarm
                # cleanup may not create a second or unstructured outcome.
                pass


def math_is_finite(value: float) -> bool:
    # Kept below the total entry so every caller reaches it only inside the
    # outer fail-closed boundary.
    return value == value and value not in (float("inf"), float("-inf"))


def request(action: str, dataset: object, claim: object = None, cap_milliseconds: int = 120_000) -> Mapping[str, object]:
    return {
        "schema": REQUEST_SCHEMA,
        "action": action,
        "cap_milliseconds": cap_milliseconds,
        "dataset": dataset,
        "claim": claim,
    }
