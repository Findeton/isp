#!/usr/bin/env python3
"""Public-only adversarial audit for the RQ0-L0 architecture reset.

This is not a held-out scorer, official receipt, or scientific delivery.  All
inputs are opened calibration objects.  The audit exercises the one total
entry point and treats both verified positives and verified finite negatives
neutrally.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import math
import pathlib
import time
from collections import Counter, defaultdict
from typing import Callable, Dict, Iterable, Mapping, MutableMapping, Sequence, Tuple

try:
    from . import rq0_l0_archreset_exact as proposer
    from . import rq0_l0_archreset_verifier_exact as trusted
    from .rq0_l0_archreset_kernel_exact import (
        monomial_span_dimension,
        represented_algebra,
    )
    from .rq0_l0_archreset_public_models import (
        opened_order_144,
        opened_order_192,
        public_c2_c3_product,
        public_full_triple,
        public_q8_ambient,
    )
except ImportError:
    import rq0_l0_archreset_exact as proposer
    import rq0_l0_archreset_verifier_exact as trusted
    from rq0_l0_archreset_kernel_exact import (
        monomial_span_dimension,
        represented_algebra,
    )
    from rq0_l0_archreset_public_models import (
        opened_order_144,
        opened_order_192,
        public_c2_c3_product,
        public_full_triple,
        public_q8_ambient,
    )


HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SCHEMA = "rq0-l0-archreset-public-audit-v1"


def canonical_clone(value: object) -> object:
    return json.loads(json.dumps(value, sort_keys=True, separators=(",", ":")))


def invoke(request_raw: object, **kwargs: object) -> Tuple[int, Mapping[str, object]]:
    exit_code, text = proposer.total_entry(request_raw, **kwargs)
    if type(exit_code) is not int or type(text) is not str:
        raise AssertionError("total entry did not return an exact exit/text pair")
    response = json.loads(text)
    if type(response) is not dict or response.get("exit_code") != exit_code:
        raise AssertionError("serialized response and process exit disagree")
    return exit_code, response


def run_case(
    name: str,
    request_raw: object,
    expected_status: str,
    predicate: Callable[[Mapping[str, object]], bool] = lambda _value: True,
    **kwargs: object,
) -> Mapping[str, object]:
    exit_code, response = invoke(request_raw, **kwargs)
    passed = (
        response.get("engineering_status") == expected_status
        and exit_code == (1 if expected_status == proposer.INVALID else 0)
        and predicate(response)
    )
    return {
        "name": name,
        "expected_status": expected_status,
        "observed_status": response.get("engineering_status"),
        "exit_code": exit_code,
        "phase": response.get("phase"),
        "detail": response.get("detail"),
        "pass": passed,
    }


def factor_claim(dataset: object) -> Mapping[str, object]:
    return proposer.propose_direct_factors(canonical_clone(dataset), time.monotonic() + 60.0)


def overlap_claim(dataset: object) -> Mapping[str, object]:
    return proposer.propose_overlap(canonical_clone(dataset))


def add_boundary(dataset: MutableMapping[str, object], name: str = "other") -> None:
    dataset["boundary_types"].append({"name": name, "composes_with": [name]})


def rename_operations(dataset_raw: object) -> Mapping[str, object]:
    dataset = canonical_clone(dataset_raw)
    mapping = {
        value["handle"]: f"renamed-operation-{index:03d}"
        for index, value in enumerate(dataset["operations"])
    }
    for value in dataset["operations"]:
        value["handle"] = mapping[value["handle"]]
    for row in dataset["composition_rows"]:
        row["left"] = mapping[row["left"]]
        row["right"] = mapping[row["right"]]
        if row["result_class"] is not None:
            row["result_class"] = mapping[row["result_class"]]
    for context in dataset["contexts"]:
        context["operation_handles"] = [mapping[value] for value in context["operation_handles"]]
    for record in dataset["records"]:
        record["access_operations"] = [mapping[value] for value in record["access_operations"]]
    dataset["handle"] = "fully-operation-renamed-q8"
    return dataset


def rename_record_handles(dataset_raw: object) -> Mapping[str, object]:
    dataset = canonical_clone(dataset_raw)
    mapping = {
        value["handle"]: f"renamed-record-{index:03d}"
        for index, value in enumerate(dataset["records"])
    }
    for value in dataset["records"]:
        value["handle"] = mapping[value["handle"]]
    for context in dataset["contexts"]:
        context["record_handles"] = [mapping[value] for value in context["record_handles"]]
    dataset["handle"] = "record-handle-renamed-q8"
    return dataset


def reorder_dataset(dataset_raw: object) -> Mapping[str, object]:
    dataset = canonical_clone(dataset_raw)
    for key in (
        "boundary_types",
        "operations",
        "composition_rows",
        "preparations",
        "contexts",
        "probes",
        "readouts",
        "records",
        "gauge_actions",
    ):
        dataset[key] = list(reversed(dataset[key]))
    dataset["handle"] = "serialization-reordered-q8"
    return dataset


def wrong_type(value: object) -> object:
    if type(value) is bool:
        return "false"
    if type(value) is int:
        return True
    if type(value) is str:
        return 7
    if type(value) is list:
        return {}
    if type(value) is dict:
        return []
    if value is None:
        return False
    return {"mistyped": True}


Path = Tuple[object, ...]


def normalize(path: Path) -> str:
    result = []
    for component in path:
        if type(component) is int:
            result.append("[]")
        elif not result:
            result.append(str(component))
        else:
            result.append("." + str(component))
    return "".join(result)


def locate(root: object, path: Path) -> object:
    current = root
    for component in path:
        current = current[component]
    return current


def mapping_field_paths(value: object, path: Path = ()) -> Iterable[Tuple[Path, str]]:
    if type(value) is dict:
        for key, child in value.items():
            yield path, key
            yield from mapping_field_paths(child, path + (key,))
    elif type(value) is list:
        for index, child in enumerate(value):
            yield from mapping_field_paths(child, path + (index,))


def primitive_leaf_paths(value: object, path: Path = ()) -> Iterable[Path]:
    if type(value) is dict:
        for key, child in value.items():
            yield from primitive_leaf_paths(child, path + (key,))
    elif type(value) is list:
        for index, child in enumerate(value):
            yield from primitive_leaf_paths(child, path + (index,))
    else:
        yield path


def systematic_mutations(
    roots: Sequence[Tuple[str, object, Callable[[object], object]]],
) -> Mapping[str, object]:
    """Mutate one representative of every normalized raw schema field."""

    cases = []
    seen_mapping_fields = set()
    seen_mapping_objects = set()
    seen_leaves = set()

    def execute(label: str, mutated: object, request_builder: Callable[[object], object]) -> None:
        exit_code, response = invoke(request_builder(mutated))
        detail = response.get("detail")
        timed_out = type(detail) is dict and detail.get("error_type") == "TimeoutError"
        cases.append(
            {
                "label": label,
                "status": response.get("engineering_status"),
                "exit_code": exit_code,
                "phase": response.get("phase"),
                "pass": exit_code == 1
                and response.get("engineering_status") == proposer.INVALID
                and not timed_out,
            }
        )
        if len(cases) % 50 == 0:
            print(f"public schema mutations completed: {len(cases)}", flush=True)

    def redundant_embedded_schema(root_name: str, relative_path: Path) -> bool:
        """Avoid replaying an already-covered schema merely because embedded.

        The standalone dataset root covers the full Dataset schema.  The
        overlap claim covers one complete RegAddr schema.  Triple instruments
        and maps are independent values at runtime, but their raw field schema
        is identical and is therefore not multiplied again here.
        """

        return (
            root_name == "overlap_claim"
            and len(relative_path) >= 2
            and relative_path[0] == "objects"
        ) or (
            root_name == "triple"
            and len(relative_path) >= 2
            and relative_path[0] in ("instruments", "pair_maps")
        )

    for root_name, root_value, request_builder in roots:
        root = canonical_clone(root_value)
        for object_path, key in mapping_field_paths(root, (root_name,)):
            if redundant_embedded_schema(root_name, object_path[1:]):
                continue
            normalized = normalize(object_path + (key,))
            if normalized in seen_mapping_fields:
                continue
            seen_mapping_fields.add(normalized)
            relative_object_path = object_path[1:]

            missing = canonical_clone(root)
            parent = locate(missing, relative_object_path)
            del parent[key]
            execute(f"{normalized}:missing", missing, request_builder)

            mistyped = canonical_clone(root)
            parent = locate(mistyped, relative_object_path)
            parent[key] = wrong_type(parent[key])
            execute(f"{normalized}:wrong-type", mistyped, request_builder)

            normalized_object = normalize(object_path)
            if normalized_object not in seen_mapping_objects:
                seen_mapping_objects.add(normalized_object)
                extra = canonical_clone(root)
                parent = locate(extra, relative_object_path)
                parent["__unknown_schema_field__"] = True
                execute(f"{normalized_object}:unknown-key", extra, request_builder)

        for leaf_path in primitive_leaf_paths(root, (root_name,)):
            if redundant_embedded_schema(root_name, leaf_path[1:]):
                continue
            if type(leaf_path[-1]) is not int:
                continue
            normalized = normalize(leaf_path)
            if normalized in seen_leaves:
                continue
            seen_leaves.add(normalized)
            relative = leaf_path[1:]
            mutated = canonical_clone(root)
            parent = locate(mutated, relative[:-1])
            parent[relative[-1]] = wrong_type(parent[relative[-1]])
            execute(f"{normalized}:element-wrong-type", mutated, request_builder)

    by_root = Counter(value["label"].split(".", 1)[0].split(":", 1)[0] for value in cases)
    by_phase = Counter(str(value["phase"]) for value in cases)
    failures = [value for value in cases if not value["pass"]]
    return {
        "normalized_mapping_fields": len(seen_mapping_fields),
        "normalized_mapping_objects": len(seen_mapping_objects),
        "normalized_primitive_array_leaves": len(seen_leaves),
        "mutations": len(cases),
        "by_root": dict(sorted(by_root.items())),
        "failure_phase_counts": dict(sorted(by_phase.items())),
        "survivors": failures,
        "all_fail_closed": not failures,
    }


def source_static_audit() -> Mapping[str, object]:
    proposer_path = HERE / "rq0_l0_archreset_exact.py"
    verifier_path = HERE / "rq0_l0_archreset_verifier_exact.py"
    kernel_path = HERE / "rq0_l0_archreset_kernel_exact.py"
    sources = {path.name: path.read_text() for path in (proposer_path, verifier_path, kernel_path)}
    forbidden_tailoring = (
        "order-192",
        "order-144",
        "public-q8",
        "public-c2-c3",
        "MainTruth",
        "fixture_novelty",
        "expected_factors",
        "serialized_fingerprint",
    )
    verifier_tree = ast.parse(sources[verifier_path.name])
    imports = []
    for node in ast.walk(verifier_tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    verifier_forbidden_import = any(
        value.endswith("rq0_l0_archreset_exact")
        or value.endswith("rq0_l0_archreset_public_models")
        for value in imports
    )
    forbidden_paths = tuple(
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*")
        if path.is_file()
        and any(token in path.name.lower() for token in ("heldout", "hidden", "official", "score"))
        and "archreset" in path.name.lower()
    )
    tailored = {
        name: [token for token in forbidden_tailoring if token in source]
        for name, source in sources.items()
    }
    hashes = {
        name: hashlib.sha256(source.encode("utf-8")).hexdigest()
        for name, source in sources.items()
    }
    return {
        "verifier_imports_proposer_or_models": verifier_forbidden_import,
        "tailoring_tokens": tailored,
        "forbidden_archreset_paths": list(forbidden_paths),
        "source_sha256": hashes,
        "pass": not verifier_forbidden_import
        and not any(tailored.values())
        and not forbidden_paths,
    }


def neutral_accounting_control() -> Mapping[str, object]:
    reached = True
    states = []
    for predicate in (True, False, True):
        if not reached:
            states.append("NOT-REACHED")
            continue
        state = "PASS" if predicate else "FAIL"
        states.append(state)
        reached = predicate
    reached_states = [value for value in states if value != "NOT-REACHED"]
    return {
        "states": states,
        "pass_numerator": reached_states.count("PASS"),
        "reached_denominator": len(reached_states),
        "not_reached_counted_as_pass": False,
        "meta_pass": states == ["PASS", "FAIL", "NOT-REACHED"]
        and reached_states.count("PASS") == 1
        and len(reached_states) == 2,
    }


def run_large_regressions() -> Sequence[Mapping[str, object]]:
    results = []
    for name, dataset_builder in (
        ("opened-order-144", opened_order_144),
        ("opened-order-192", opened_order_192),
    ):
        started = time.monotonic()
        exit_code, response = invoke(
            proposer.request(
                "ESTIMATE-DIRECT-FACTORS",
                canonical_clone(dataset_builder()),
                cap_milliseconds=360_000,
            )
        )
        elapsed = time.monotonic() - started
        results.append(
            {
                "name": name,
                "classification": "opened-regression-only",
                "engineering_status": response.get("engineering_status"),
                "exit_code": exit_code,
                "phase": response.get("phase"),
                "detail": response.get("detail"),
                "timing_seconds_noncanonical": round(elapsed, 3),
                "earns_scientific_rung": False,
            }
        )
    return results


def build_audit(include_large: bool) -> Mapping[str, object]:
    product = canonical_clone(public_c2_c3_product())
    q8 = canonical_clone(public_q8_ambient())
    q8_disagree = canonical_clone(public_q8_ambient(disagree_records=True))
    positive_factor_claim = factor_claim(product)
    positive_overlap_claim = overlap_claim(q8)

    cases = [
        run_case(
            "direct-product-positive",
            proposer.request("ESTIMATE-DIRECT-FACTORS", product, cap_milliseconds=360_000),
            proposer.PUBLIC_PASS,
            lambda value: value["detail"].get("factor_orders") == [[2, 3]],
        ),
        run_case(
            "indecomposable-q8-direct-negative",
            proposer.request("ESTIMATE-DIRECT-FACTORS", q8, cap_milliseconds=360_000),
            proposer.PUBLIC_NEGATIVE,
            lambda value: value["detail"].get("certificates") == 0,
        ),
        run_case(
            "q8-overlap-first-positive",
            proposer.request("ESTIMATE-OVERLAP", q8, cap_milliseconds=360_000),
            proposer.PUBLIC_PASS,
            lambda value: value["detail"].get("operational_scopes") == 4
            and value["detail"].get("record_scopes") == 4
            and value["detail"].get("pair_intersections") == 3
            and value["detail"].get("triple_intersections") == 1,
        ),
        run_case(
            "q8-independent-reconstructions-disagree",
            proposer.request("ESTIMATE-OVERLAP", q8_disagree, cap_milliseconds=360_000),
            proposer.PUBLIC_NEGATIVE,
            lambda value: value["detail"].get("category") == "scientific-negative",
        ),
        run_case(
            "full-coherent-triple",
            proposer.request("VERIFY-TRIPLE", None, public_full_triple("COHERENT"), 360_000),
            proposer.PUBLIC_PASS,
            lambda value: value["detail"].get("pair_maps_valid") == 3
            and value["detail"].get("loop_commutes") is True
            and value["detail"].get("differing_fields") == [],
        ),
        run_case(
            "full-twisted-triple",
            proposer.request("VERIFY-TRIPLE", None, public_full_triple("TWISTED"), 360_000),
            proposer.PUBLIC_PASS,
            lambda value: value["detail"].get("pair_maps_valid") == 3
            and value["detail"].get("loop_commutes") is False
            and "row_map" in value["detail"].get("differing_fields", []),
        ),
    ]

    baseline_overlap_detail = cases[2]["detail"]
    for name, transformed in (
        ("operation-handle-renaming", rename_operations(q8)),
        ("record-handle-renaming", rename_record_handles(q8)),
        ("serialization-reordering", reorder_dataset(q8)),
    ):
        cases.append(
            run_case(
                name,
                proposer.request("ESTIMATE-OVERLAP", transformed, cap_milliseconds=360_000),
                proposer.PUBLIC_PASS,
                lambda value, expected=baseline_overlap_detail: value["detail"] == expected,
            )
        )

    adversarial = []
    forged = canonical_clone(positive_factor_claim)
    forged["certificates"][0]["asserted_predicates"]["P1"] = False
    adversarial.append(
        run_case(
            "forged-factor-certificate",
            proposer.request("VERIFY-FACTOR-CLAIM", product, forged, 360_000),
            proposer.INVALID,
        )
    )

    malformed_selectability = canonical_clone(product)
    malformed_selectability["operations"][0]["independently_selectable"] = "false"
    adversarial.append(
        run_case(
            "string-false-selectability",
            proposer.request("ESTIMATE-DIRECT-FACTORS", malformed_selectability, cap_milliseconds=360_000),
            proposer.INVALID,
        )
    )

    wrong_gauge = canonical_clone(q8)
    wrong_gauge["gauge_actions"][0]["law"] = {"permutation": [0], "phases": [0]}
    adversarial.append(
        run_case(
            "wrong-gauge-dimension",
            proposer.request("ESTIMATE-OVERLAP", wrong_gauge, cap_milliseconds=360_000),
            proposer.INVALID,
        )
    )

    projector_mutations = {
        "projector-out-of-range": [[0], [2]],
        "projector-overlap": [[0], [0, 1]],
        "projector-incomplete": [[0]],
        "projector-duplicate": [[0], [0]],
    }
    for name, resolution in projector_mutations.items():
        value = canonical_clone(q8)
        value["records"][0]["ambient_projector_resolution"] = resolution
        adversarial.append(
            run_case(
                name,
                proposer.request("ESTIMATE-OVERLAP", value, cap_milliseconds=360_000),
                proposer.INVALID,
            )
        )

    bad_context = canonical_clone(q8)
    add_boundary(bad_context)
    bad_context["contexts"][0]["boundary_type"] = "other"
    adversarial.append(
        run_case(
            "incompatible-context-boundary",
            proposer.request("ESTIMATE-OVERLAP", bad_context, cap_milliseconds=360_000),
            proposer.INVALID,
        )
    )

    bad_record = canonical_clone(q8)
    add_boundary(bad_record)
    bad_record["records"][0]["boundary_type"] = "other"
    adversarial.append(
        run_case(
            "incompatible-record-boundary",
            proposer.request("ESTIMATE-OVERLAP", bad_record, cap_milliseconds=360_000),
            proposer.INVALID,
        )
    )

    duplicate_row = canonical_clone(q8)
    duplicate_row["composition_rows"][-1] = canonical_clone(duplicate_row["composition_rows"][0])
    adversarial.append(
        run_case(
            "duplicate-dataset-row",
            proposer.request("ESTIMATE-OVERLAP", duplicate_row, cap_milliseconds=360_000),
            proposer.INVALID,
        )
    )

    duplicate_map_row = canonical_clone(positive_overlap_claim)
    duplicate_map_row["arrows"][0]["row_map"][-1] = canonical_clone(
        duplicate_map_row["arrows"][0]["row_map"][0]
    )
    adversarial.append(
        run_case(
            "duplicate-regaddr-row-map",
            proposer.request("VERIFY-OVERLAP-CLAIM", q8, duplicate_map_row, 360_000),
            proposer.INVALID,
        )
    )

    forged_row_metadata = canonical_clone(positive_overlap_claim)
    forged_row_metadata["arrows"][0]["row_map"][0]["source_tau"] = "forged|tau|value"
    adversarial.append(
        run_case(
            "forged-regaddr-row-metadata",
            proposer.request("VERIFY-OVERLAP-CLAIM", q8, forged_row_metadata, 360_000),
            proposer.INVALID,
        )
    )

    none_cap = proposer.request("ESTIMATE-DIRECT-FACTORS", product, cap_milliseconds=1)
    none_cap["cap_milliseconds"] = None
    nan_cap = proposer.request("ESTIMATE-DIRECT-FACTORS", product, cap_milliseconds=1)
    nan_cap["cap_milliseconds"] = float("nan")
    adversarial.extend(
        (
            run_case("none-cap", none_cap, proposer.INVALID),
            run_case("nan-cap", nan_cap, proposer.INVALID),
            run_case(
                "nonfinite-clock",
                proposer.request("ESTIMATE-DIRECT-FACTORS", product, cap_milliseconds=360_000),
                proposer.INVALID,
                clock=lambda: float("nan"),
            ),
            run_case(
                "serializer-exception",
                proposer.request("ESTIMATE-DIRECT-FACTORS", product, cap_milliseconds=360_000),
                proposer.INVALID,
                serializer=lambda *_args, **_kwargs: (_ for _ in ()).throw(RuntimeError("public serializer mutant")),
            ),
        )
    )

    singleton = canonical_clone(positive_factor_claim)
    singleton["certificates"][0]["factors"] = singleton["certificates"][0]["factors"][:1]
    adversarial.append(
        run_case(
            "singleton-factor-outside-completeness-scope",
            proposer.request("VERIFY-FACTOR-CLAIM", product, singleton, 360_000),
            proposer.INVALID,
        )
    )
    nine = canonical_clone(positive_factor_claim)
    nine["certificates"][0]["factors"] = [
        canonical_clone(nine["certificates"][0]["factors"][0]) for _ in range(9)
    ]
    adversarial.append(
        run_case(
            "nine-factor-outside-completeness-scope",
            proposer.request("VERIFY-FACTOR-CLAIM", product, nine, 360_000),
            proposer.INVALID,
        )
    )

    roots = (
        (
            "request",
            proposer.request("ESTIMATE-DIRECT-FACTORS", product, cap_milliseconds=360_000),
            lambda value: value,
        ),
        (
            "dataset",
            q8,
            lambda value: proposer.request("ESTIMATE-OVERLAP", value, cap_milliseconds=360_000),
        ),
        (
            "factor_claim",
            positive_factor_claim,
            lambda value: proposer.request("VERIFY-FACTOR-CLAIM", product, value, 360_000),
        ),
        (
            "overlap_claim",
            positive_overlap_claim,
            lambda value: proposer.request("VERIFY-OVERLAP-CLAIM", q8, value, 360_000),
        ),
        (
            "triple",
            public_full_triple("COHERENT"),
            lambda value: proposer.request("VERIFY-TRIPLE", None, value, 360_000),
        ),
    )
    systematic = systematic_mutations(roots)

    dense_sparse = []
    for dataset_raw in (product, q8):
        dataset = trusted.parse_dataset(dataset_raw)
        laws = tuple(value.law for value in dataset.operations)
        dense = represented_algebra(laws, dataset.carrier_dimension).dimension
        sparse = monomial_span_dimension(laws)
        dense_sparse.append(
            {"dataset": dataset.handle, "dense_dimension": dense, "sparse_dimension": sparse, "pass": dense == sparse}
        )

    large = []
    if include_large:
        large = list(run_large_regressions())
    else:
        large = [
            {
                "name": name,
                "classification": "opened-regression-only",
                "engineering_status": "NOT-REACHED",
                "earns_scientific_rung": False,
            }
            for name in ("opened-order-144", "opened-order-192")
        ]

    static = source_static_audit()
    neutral = neutral_accounting_control()
    all_pass = (
        all(value["pass"] for value in cases)
        and all(value["pass"] for value in adversarial)
        and systematic["all_fail_closed"]
        and all(value["pass"] for value in dense_sparse)
        and static["pass"]
        and neutral["meta_pass"]
    )
    return {
        "schema": SCHEMA,
        "classification": "PUBLIC-ARCHITECTURE-AUDIT-NOT-A-SCIENTIFIC-RECEIPT",
        "antecedent_head": "e247d34",
        "pin_commit": "c0fab11",
        "scientific_outcome": None,
        "estimator_frozen": False,
        "held_out_content_created": False,
        "all_public_gates_pass": all_pass,
        "cases": cases,
        "adversarial_cases": adversarial,
        "systematic_schema_mutations": systematic,
        "dense_sparse_equivalence": dense_sparse,
        "neutral_accounting": neutral,
        "static_audit": static,
        "opened_large_regressions": large,
        "claim_ceiling": "public architecture candidate awaiting external hostile review",
    }


def render_text(audit: Mapping[str, object]) -> str:
    lines = [
        "RQ0-L0 PUBLIC ARCHITECTURE AUDIT",
        "================================",
        f"public gates: {'PASS' if audit['all_public_gates_pass'] else 'FAIL'}",
        "scientific outcome: null",
        "estimator frozen: no",
        "held-out content: none",
        "",
        "Public cases:",
    ]
    lines.extend(
        f"- {value['name']}: {'PASS' if value['pass'] else 'FAIL'} "
        f"({value['observed_status']})"
        for value in audit["cases"]
    )
    lines.extend(("", "Adversarial cases:"))
    lines.extend(
        f"- {value['name']}: {'PASS' if value['pass'] else 'FAIL'} "
        f"({value['observed_status']}, phase={value['phase']})"
        for value in audit["adversarial_cases"]
    )
    systematic = audit["systematic_schema_mutations"]
    lines.extend(
        (
            "",
            "Systematic schema mutation:",
            f"- mutations: {systematic['mutations']}",
            f"- all fail closed: {systematic['all_fail_closed']}",
            f"- phases: {json.dumps(systematic['failure_phase_counts'], sort_keys=True)}",
            "",
            "Opened large regressions (never scientific):",
        )
    )
    lines.extend(
        f"- {value['name']}: {value['engineering_status']}"
        + (
            f" ({value.get('timing_seconds_noncanonical')} s)"
            if "timing_seconds_noncanonical" in value
            else ""
        )
        for value in audit["opened_large_regressions"]
    )
    lines.extend(
        (
            "",
            "Ceiling:",
            "- public architecture candidate only",
            "- no RQ0-L0 scientific claim",
            "- no T1, C1, topology, influence, causality, geometry, spacetime, fields, or gravity",
            "",
        )
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--include-large", action="store_true")
    parser.add_argument("--write", action="store_true")
    parser.add_argument(
        "--update-large",
        action="store_true",
        help="rerun only opened large regressions and update an existing public audit",
    )
    arguments = parser.parse_args()
    if arguments.update_large:
        audit_path = HERE / "rq0_l0_archreset_public_audit.json"
        if not audit_path.exists():
            raise SystemExit("--update-large requires an existing public audit JSON")
        audit = json.loads(audit_path.read_text())
        audit["opened_large_regressions"] = list(run_large_regressions())
        audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
        (HERE / "rq0_l0_archreset_public_output.txt").write_text(render_text(audit))
        print(json.dumps({"large": audit["opened_large_regressions"]}, indent=2, sort_keys=True))
        return 0
    audit = build_audit(arguments.include_large)
    if arguments.write:
        (HERE / "rq0_l0_archreset_public_audit.json").write_text(
            json.dumps(audit, indent=2, sort_keys=True) + "\n"
        )
        (HERE / "rq0_l0_archreset_public_output.txt").write_text(render_text(audit))
    print(json.dumps({
        "all_public_gates_pass": audit["all_public_gates_pass"],
        "adversarial_cases": len(audit["adversarial_cases"]),
        "systematic_mutations": audit["systematic_schema_mutations"]["mutations"],
        "systematic_survivors": len(audit["systematic_schema_mutations"]["survivors"]),
        "large": audit["opened_large_regressions"],
    }, indent=2, sort_keys=True))
    return 0 if audit["all_public_gates_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
