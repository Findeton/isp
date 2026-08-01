#!/usr/bin/env python3
"""Opened public models for the RQ0-L0 architecture-reset cycle.

Nothing in this file is held out.  The direct-product objects are regression
controls.  The Q8 object is an indecomposable overlap-first architecture
calibration, not a scientific localization result.
"""

from __future__ import annotations

import copy
import itertools
from dataclasses import dataclass
from typing import Dict, FrozenSet, Mapping, Sequence, Tuple

try:
    from .rq0_l0_archreset_kernel_exact import (
        INV_SQRT2,
        Matrix,
        MonomialLaw,
        Vector,
        basis_vector,
        conjugate_dense,
        identity,
        matrix,
        matrix_to_raw,
        permutation_law,
        q24_to_raw,
        rank_one_projector,
        tensor_monomial,
        vector,
        vector_to_raw,
    )
    from .rq0_l0_archreset_verifier_exact import (
        ATLAS_CLAIM_SCHEMA,
        DATASET_SCHEMA,
        FACTOR_CLAIM_SCHEMA,
        REGADDR_SCHEMA,
        TRIPLE_SCHEMA,
    )
except ImportError:
    from rq0_l0_archreset_kernel_exact import (
        INV_SQRT2,
        Matrix,
        MonomialLaw,
        Vector,
        basis_vector,
        conjugate_dense,
        identity,
        matrix,
        matrix_to_raw,
        permutation_law,
        q24_to_raw,
        rank_one_projector,
        tensor_monomial,
        vector,
        vector_to_raw,
    )
    from rq0_l0_archreset_verifier_exact import (
        ATLAS_CLAIM_SCHEMA,
        DATASET_SCHEMA,
        FACTOR_CLAIM_SCHEMA,
        REGADDR_SCHEMA,
        TRIPLE_SCHEMA,
    )


@dataclass(frozen=True)
class WitnessData:
    preparations: Tuple[Vector, ...]
    alternative_projectors: Tuple[Matrix, ...]
    cut_record_projectors: Tuple[Matrix, ...]
    availability_probes: Tuple[Matrix, ...]
    write: Matrix
    preserving: Tuple[Matrix, ...]
    erasing: Tuple[Matrix, ...]
    no_write: Matrix


def two_level_witness() -> WitnessData:
    p0 = matrix(((1, 0), (0, 0)))
    p1 = matrix(((0, 0), (0, 1)))
    h = matrix(((INV_SQRT2, INV_SQRT2), (INV_SQRT2, -INV_SQRT2)))
    plus = vector((INV_SQRT2, INV_SQRT2))
    minus = vector((INV_SQRT2, -INV_SQRT2))
    return WitnessData(
        preparations=(basis_vector(2, 0),),
        alternative_projectors=(rank_one_projector(plus), rank_one_projector(minus)),
        cut_record_projectors=(p0, p1),
        availability_probes=(p0, p1),
        write=h,
        preserving=(identity(2),),
        erasing=(h,),
        no_write=identity(2),
    )


def conjugated_witness(value: WitnessData, action: MonomialLaw) -> WitnessData:
    action_matrix = action.to_matrix()
    try:
        from .rq0_l0_archreset_kernel_exact import mv
    except ImportError:
        from rq0_l0_archreset_kernel_exact import mv
    return WitnessData(
        preparations=tuple(mv(action_matrix, entry) for entry in value.preparations),
        alternative_projectors=tuple(conjugate_dense(action, entry) for entry in value.alternative_projectors),
        cut_record_projectors=tuple(conjugate_dense(action, entry) for entry in value.cut_record_projectors),
        availability_probes=tuple(conjugate_dense(action, entry) for entry in value.availability_probes),
        write=conjugate_dense(action, value.write),
        preserving=tuple(conjugate_dense(action, entry) for entry in value.preserving),
        erasing=tuple(conjugate_dense(action, entry) for entry in value.erasing),
        no_write=conjugate_dense(action, value.no_write),
    )


def witness_to_raw(value: WitnessData) -> Mapping[str, object]:
    return {
        "preparations": [vector_to_raw(entry) for entry in value.preparations],
        "alternative_projectors": [matrix_to_raw(entry) for entry in value.alternative_projectors],
        "cut_record_projectors": [matrix_to_raw(entry) for entry in value.cut_record_projectors],
        "availability_probes": [matrix_to_raw(entry) for entry in value.availability_probes],
        "write": matrix_to_raw(value.write),
        "preserving": [matrix_to_raw(entry) for entry in value.preserving],
        "erasing": [matrix_to_raw(entry) for entry in value.erasing],
        "no_write": matrix_to_raw(value.no_write),
    }


def signature_raw(value: MonomialLaw) -> list[list[int]]:
    permutation, phases = value.signature()
    return [list(permutation), list(phases)]


def _base_dataset(
    handle: str,
    operations: Sequence[Mapping[str, object]],
    rows: Sequence[Mapping[str, object]],
    dimension: int,
    *,
    preparations: Sequence[Mapping[str, object]] = (),
    contexts: Sequence[Mapping[str, object]] = (),
    probes: Sequence[Mapping[str, object]] = (),
    readouts: Sequence[Mapping[str, object]] = (),
    records: Sequence[Mapping[str, object]] = (),
    gauges: Sequence[Mapping[str, object]] = (),
) -> Mapping[str, object]:
    return {
        "schema": DATASET_SCHEMA,
        "handle": handle,
        "phase_modulus": 24,
        "carrier_dimension": dimension,
        "boundary_types": [{"name": "end", "composes_with": ["end"]}],
        "operations": list(operations),
        "composition_rows": list(rows),
        "preparations": list(preparations),
        "contexts": list(contexts),
        "probes": list(probes),
        "readouts": list(readouts),
        "records": list(records),
        "gauge_actions": list(gauges),
        "access_postulate": "PUBLIC POSTULATE: exact finite operational tomography and selectable controls",
    }


def _group_dataset(
    handle: str,
    elements: Sequence[object],
    multiply,
    laws: Mapping[object, MonomialLaw],
    selected: FrozenSet[object],
) -> Mapping[str, object]:
    handles = {value: f"op-{index:03d}" for index, value in enumerate(elements)}
    operations = [
        {
            "handle": handles[value],
            "source_type": "end",
            "target_type": "end",
            "law": laws[value].to_raw(),
            "observed_signature": signature_raw(laws[value]),
            "independently_selectable": value in selected,
        }
        for value in elements
    ]
    rows = []
    for left in elements:
        for right in elements:
            law = laws[left].after(laws[right])
            result = multiply(left, right)
            if law != laws[result]:
                raise AssertionError("public exact representation is not multiplicative")
            rows.append(
                {
                    "left": handles[left],
                    "right": handles[right],
                    "tau": "end|end|end",
                    "status": "IMPLEMENTED",
                    "result_class": handles[result],
                    "law": law.to_raw(),
                    "observed_signature": signature_raw(law),
                }
            )
    return _base_dataset(handle, operations, rows, laws[elements[0]].dimension)


def public_c2_c3_product() -> Mapping[str, object]:
    elements = tuple(itertools.product(range(2), range(3)))

    def multiply(left, right):
        return ((left[0] + right[0]) % 2, (left[1] + right[1]) % 3)

    laws = {
        value: tensor_monomial(
            (
                MonomialLaw((0, 1), (0, 12 * value[0])),
                MonomialLaw((0, 1), (0, 8 * value[1])),
            )
        )
        for value in elements
    }
    return _group_dataset(
        "public-c2-c3-product",
        elements,
        multiply,
        laws,
        frozenset(((0, 0), (1, 0), (0, 1))),
    )


# Quaternion group: sign 0/1 followed by unit 0=1, 1=i, 2=j, 3=k.
Quaternion = Tuple[int, int]


def q8_elements() -> Tuple[Quaternion, ...]:
    return tuple((sign, unit) for sign in range(2) for unit in range(4))


def q8_multiply(left: Quaternion, right: Quaternion) -> Quaternion:
    left_sign, left_unit = left
    right_sign, right_unit = right
    sign = (left_sign + right_sign) % 2
    if left_unit == 0:
        return sign, right_unit
    if right_unit == 0:
        return sign, left_unit
    if left_unit == right_unit:
        return (sign + 1) % 2, 0
    positive = {(1, 2): 3, (2, 3): 1, (3, 1): 2}
    if (left_unit, right_unit) in positive:
        return sign, positive[(left_unit, right_unit)]
    return (sign + 1) % 2, positive[(right_unit, left_unit)]


def q8_inverse(value: Quaternion) -> Quaternion:
    return value if value[1] == 0 else ((value[0] + 1) % 2, value[1])


def q8_conjugate(action: Quaternion, value: Quaternion) -> Quaternion:
    return q8_multiply(q8_multiply(action, value), q8_inverse(action))


def q8_laws() -> Mapping[Quaternion, MonomialLaw]:
    unit = MonomialLaw.unit(2)
    minus = MonomialLaw((0, 1), (12, 12))
    i_law = MonomialLaw((0, 1), (6, 18))
    j_law = MonomialLaw((1, 0), (12, 0))
    positive = {
        0: unit,
        1: i_law,
        2: j_law,
        3: i_law.after(j_law),
    }
    result = {}
    for sign, unit_index in q8_elements():
        result[(sign, unit_index)] = (
            positive[unit_index] if sign == 0 else minus.after(positive[unit_index])
        )
    for left, right in itertools.product(q8_elements(), repeat=2):
        if result[left].after(result[right]) != result[q8_multiply(left, right)]:
            raise AssertionError("Q8 monomial representation failed")
    return result


Q8_NAMES = {
    (0, 0): "q1",
    (1, 0): "qm1",
    (0, 1): "qi",
    (1, 1): "qmi",
    (0, 2): "qj",
    (1, 2): "qmj",
    (0, 3): "qk",
    (1, 3): "qmk",
}


Q8_SCOPES = {
    "core": frozenset(((0, 0), (1, 0))),
    "i": frozenset(((0, 0), (1, 0), (0, 1), (1, 1))),
    "j": frozenset(((0, 0), (1, 0), (0, 2), (1, 2))),
    "k": frozenset(((0, 0), (1, 0), (0, 3), (1, 3))),
}


def public_q8_ambient(*, disagree_records: bool = False) -> Mapping[str, object]:
    elements = q8_elements()
    laws = q8_laws()
    handles = {value: Q8_NAMES[value] for value in elements}
    operations = [
        {
            "handle": handles[value],
            "source_type": "end",
            "target_type": "end",
            "law": laws[value].to_raw(),
            "observed_signature": signature_raw(laws[value]),
            # The opened Q8 overlap fixture keeps the selectable declaration
            # invariant under its full public inner-automorphism controls.
            "independently_selectable": True,
        }
        for value in elements
    ]
    rows = []
    for left, right in itertools.product(elements, repeat=2):
        result = q8_multiply(left, right)
        law = laws[left].after(laws[right])
        rows.append(
            {
                "left": handles[left],
                "right": handles[right],
                "tau": "end|end|end",
                "status": "IMPLEMENTED",
                "result_class": handles[result],
                "law": law.to_raw(),
                "observed_signature": signature_raw(law),
            }
        )

    preparation = {"handle": "prep", "boundary_type": "end", "payload": [1, 0]}
    probe = {"handle": "probe", "boundary_type": "end", "payload": [0, 1]}
    readout = {
        "handle": "readout",
        "boundary_type": "end",
        "projector_resolution": [[0], [1]],
    }
    gauge = {
        "handle": "gauge",
        "boundary_type": "end",
        "law": MonomialLaw.unit(2).to_raw(),
    }
    witness_zero = two_level_witness()
    witness_one = conjugated_witness(witness_zero, laws[(0, 1)])
    records = []
    contexts = []
    for scope_name, scope in Q8_SCOPES.items():
        if disagree_records and scope_name == "k":
            continue
        access = sorted(handles[value] for value in scope)
        for variant, witness in enumerate((witness_zero, witness_one)):
            record_handle = f"record-{scope_name}-{variant}"
            context_handle = f"context-{scope_name}-{variant}"
            records.append(
                {
                    "handle": record_handle,
                    "boundary_type": "end",
                    "access_operations": access,
                    "witness": witness_to_raw(witness),
                    "ambient_projector_resolution": [[0], [1]],
                }
            )
            contexts.append(
                {
                    "handle": context_handle,
                    "boundary_type": "end",
                    "operation_handles": access,
                    "preparation_handles": ["prep"],
                    "probe_handles": ["probe"],
                    "readout_handles": ["readout"],
                    "record_handles": [record_handle],
                    "gauge_handles": ["gauge"],
                }
            )
    # In the disagreement control the operational k context remains while its
    # independent record candidate is absent.
    if disagree_records:
        access = sorted(handles[value] for value in Q8_SCOPES["k"])
        contexts.append(
            {
                "handle": "context-k-unmatched",
                "boundary_type": "end",
                "operation_handles": access,
                "preparation_handles": ["prep"],
                "probe_handles": ["probe"],
                "readout_handles": ["readout"],
                "record_handles": [],
                "gauge_handles": ["gauge"],
            }
        )
    return _base_dataset(
        "public-q8-ambient",
        operations,
        rows,
        2,
        preparations=(preparation,),
        contexts=contexts,
        probes=(probe,),
        readouts=(readout,),
        records=records,
        gauges=(gauge,),
    )


def _restrict_dataset(
    ambient: Mapping[str, object],
    scope: FrozenSet[str],
    handle: str,
) -> Mapping[str, object]:
    result = copy.deepcopy(ambient)
    result["handle"] = handle
    result["operations"] = [
        value for value in result["operations"] if value["handle"] in scope
    ]
    result["composition_rows"] = [
        value
        for value in result["composition_rows"]
        if value["left"] in scope and value["right"] in scope
    ]
    result["records"] = [
        value
        for value in result["records"]
        if set(value["access_operations"]) <= scope
    ]
    record_handles = {value["handle"] for value in result["records"]}
    result["contexts"] = [
        value
        for value in result["contexts"]
        if set(value["operation_handles"]) <= scope
        and set(value["record_handles"]) <= record_handles
    ]
    return result


def _pairs(source: Sequence[Mapping[str, object]], target: Sequence[Mapping[str, object]]) -> list[Mapping[str, str]]:
    target_handles = {value["handle"] for value in target}
    return [
        {"source": value["handle"], "target": value["handle"]}
        for value in source
        if value["handle"] in target_handles
    ]


def _full_row_map_entry(
    source_row: Mapping[str, object],
    target_row: Mapping[str, object],
) -> Mapping[str, object]:
    """Carry every typed row field rather than only its endpoints."""

    return {
        "source_left": source_row["left"],
        "source_right": source_row["right"],
        "target_left": target_row["left"],
        "target_right": target_row["right"],
        "source_tau": source_row["tau"],
        "target_tau": target_row["tau"],
        "source_status": source_row["status"],
        "target_status": target_row["status"],
        "source_result_class": source_row["result_class"],
        "target_result_class": target_row["result_class"],
        "source_law": source_row["law"],
        "target_law": target_row["law"],
        "source_observed_signature": source_row["observed_signature"],
        "target_observed_signature": target_row["observed_signature"],
    }


def identity_regaddr(
    source: Mapping[str, object],
    target: Mapping[str, object],
    handle: str,
    *,
    kind: str,
) -> Mapping[str, object]:
    source_operations = {value["handle"] for value in source["operations"]}
    target_operations = {value["handle"] for value in target["operations"]}
    if not source_operations <= target_operations:
        raise ValueError("identity embedding source is not a target subinstrument")
    return {
        "schema": REGADDR_SCHEMA,
        "handle": handle,
        "kind": kind,
        "source": source["handle"],
        "target": target["handle"],
        "carrier_action": MonomialLaw.unit(source["carrier_dimension"]).to_raw(),
        "operation_map": [
            {"source": value, "target": value} for value in sorted(source_operations)
        ],
        "row_map": [
            _full_row_map_entry(value, value)
            for value in source["composition_rows"]
        ],
        "preparation_map": _pairs(source["preparations"], target["preparations"]),
        "context_map": _pairs(source["contexts"], target["contexts"]),
        "probe_map": _pairs(source["probes"], target["probes"]),
        "readout_map": _pairs(source["readouts"], target["readouts"]),
        "record_map": _pairs(source["records"], target["records"]),
        "gauge_map": _pairs(source["gauge_actions"], target["gauge_actions"]),
    }


def public_q8_overlap_claim() -> Tuple[Mapping[str, object], Mapping[str, object]]:
    ambient = public_q8_ambient()
    scopes = {
        name: frozenset(Q8_NAMES[value] for value in scope)
        for name, scope in Q8_SCOPES.items()
    }
    objects = {
        "ambient": ambient,
        "core": _restrict_dataset(ambient, scopes["core"], "public-q8-core"),
        "i": _restrict_dataset(ambient, scopes["i"], "public-q8-i"),
        "j": _restrict_dataset(ambient, scopes["j"], "public-q8-j"),
        "k": _restrict_dataset(ambient, scopes["k"], "public-q8-k"),
    }
    arrows: Dict[str, Mapping[str, object]] = {}
    for name, dataset in objects.items():
        arrow_handle = f"id-{name}"
        arrows[arrow_handle] = identity_regaddr(
            dataset, dataset, arrow_handle, kind="ISOMORPHISM"
        )
    for target in ("i", "j", "k"):
        arrow_handle = f"core-to-{target}"
        arrows[arrow_handle] = identity_regaddr(
            objects["core"], objects[target], arrow_handle, kind="EMBEDDING"
        )
    arrows["core-to-ambient"] = identity_regaddr(
        objects["core"], ambient, "core-to-ambient", kind="EMBEDDING"
    )
    for source in ("i", "j", "k"):
        arrow_handle = f"{source}-to-ambient"
        arrows[arrow_handle] = identity_regaddr(
            objects[source], ambient, arrow_handle, kind="EMBEDDING"
        )

    pairs = []
    for left, right in itertools.combinations(("i", "j", "k"), 2):
        pairs.append(
            {
                "left": objects[left]["handle"],
                "right": objects[right]["handle"],
                "intersection": objects["core"]["handle"],
                "ambient": ambient["handle"],
                "to_left": f"core-to-{left}",
                "to_right": f"core-to-{right}",
                "left_to_ambient": f"{left}-to-ambient",
                "right_to_ambient": f"{right}-to-ambient",
                "intersection_to_ambient": "core-to-ambient",
            }
        )
    triple = {
        "regions": [objects[name]["handle"] for name in ("i", "j", "k")],
        "intersection": objects["core"]["handle"],
        "ambient": ambient["handle"],
        "to_regions": [f"core-to-{name}" for name in ("i", "j", "k")],
        "region_to_ambient": [f"{name}-to-ambient" for name in ("i", "j", "k")],
        "intersection_to_ambient": "core-to-ambient",
    }
    claim = {
        "schema": ATLAS_CLAIM_SCHEMA,
        "kind": "OVERLAP-FIRST-ATLAS",
        "op_scopes": [sorted(value) for value in scopes.values()],
        "rec_scopes": [sorted(value) for value in scopes.values()],
        "objects": list(objects.values()),
        "arrows": list(arrows.values()),
        "pair_intersections": pairs,
        "triple_intersections": [triple],
    }
    return ambient, claim


def _q8_automorphism_regaddr(
    source: Mapping[str, object],
    target: Mapping[str, object],
    handle: str,
    *,
    twisted: bool,
) -> Mapping[str, object]:
    if not twisted:
        return identity_regaddr(source, target, handle, kind="ISOMORPHISM")
    action_element = (0, 1)
    action = q8_laws()[action_element]
    operation_map = {
        Q8_NAMES[value]: Q8_NAMES[q8_conjugate(action_element, value)]
        for value in q8_elements()
    }
    # Conjugation by i preserves each named subgroup and flips the two witness
    # variants.  Handles encode only public presentation data.
    record_map = {}
    for value in source["records"]:
        prefix, scope, variant = value["handle"].split("-")
        record_map[value["handle"]] = f"{prefix}-{scope}-{1 - int(variant)}"
    context_map = {}
    for value in source["contexts"]:
        prefix, scope, variant = value["handle"].split("-")
        context_map[value["handle"]] = f"{prefix}-{scope}-{1 - int(variant)}"
    return {
        "schema": REGADDR_SCHEMA,
        "handle": handle,
        "kind": "ISOMORPHISM",
        "source": source["handle"],
        "target": target["handle"],
        "carrier_action": action.to_raw(),
        "operation_map": [
            {"source": key, "target": value} for key, value in sorted(operation_map.items())
        ],
        "row_map": [
            _full_row_map_entry(
                value,
                next(
                    target_row
                    for target_row in target["composition_rows"]
                    if target_row["left"] == operation_map[value["left"]]
                    and target_row["right"] == operation_map[value["right"]]
                ),
            )
            for value in source["composition_rows"]
        ],
        "preparation_map": _pairs(source["preparations"], target["preparations"]),
        "context_map": [
            {"source": key, "target": value} for key, value in sorted(context_map.items())
        ],
        "probe_map": _pairs(source["probes"], target["probes"]),
        "readout_map": _pairs(source["readouts"], target["readouts"]),
        "record_map": [
            {"source": key, "target": value} for key, value in sorted(record_map.items())
        ],
        "gauge_map": _pairs(source["gauge_actions"], target["gauge_actions"]),
    }


def public_full_triple(mode: str) -> Mapping[str, object]:
    if mode not in ("COHERENT", "TWISTED"):
        raise ValueError("unknown public triple mode")
    instruments = []
    for name in ("alpha", "beta", "gamma"):
        dataset = copy.deepcopy(public_q8_ambient())
        dataset["handle"] = f"triple-{name}"
        instruments.append(dataset)
    first = _q8_automorphism_regaddr(
        instruments[0], instruments[1], "phi-12", twisted=False
    )
    second = _q8_automorphism_regaddr(
        instruments[1], instruments[2], "phi-23", twisted=False
    )
    direct = _q8_automorphism_regaddr(
        instruments[0],
        instruments[2],
        "phi-13",
        twisted=mode == "TWISTED",
    )
    return {
        "schema": TRIPLE_SCHEMA,
        "mode": mode,
        "instruments": instruments,
        "pair_maps": [first, second, direct],
    }


def adapt_opened_legacy_dataset(dataset) -> Mapping[str, object]:
    """Public adapter: discard old fields and retain raw amplitude rows only."""

    try:
        from . import rq0_l0_certification_estimator_exact as legacy
    except ImportError:
        import rq0_l0_certification_estimator_exact as legacy
    data = legacy.dataset_to_data(dataset)
    boundary_names = sorted(
        {
            value["source_type"]
            for value in data["operations"]
        }
        | {value["target_type"] for value in data["operations"]}
    )
    raw = {
        "schema": DATASET_SCHEMA,
        "handle": f"opened-{data['handle']}",
        "phase_modulus": 24,
        "carrier_dimension": data["carrier_dimension"],
        "boundary_types": [
            {"name": name, "composes_with": boundary_names} for name in boundary_names
        ],
        "operations": data["operations"],
        "composition_rows": data["composition_rows"],
        "preparations": [],
        "contexts": [],
        "probes": [],
        "readouts": [],
        "records": [],
        "gauge_actions": [],
        "access_postulate": "OPENED REGRESSION ADAPTER: amplitude rows only",
    }
    return raw


def opened_order_192() -> Mapping[str, object]:
    try:
        from . import rq0_l0_certification_fixtures_exact as fixture
    except ImportError:
        import rq0_l0_certification_fixtures_exact as fixture
    return adapt_opened_legacy_dataset(fixture.build_main_dataset())


def opened_order_144() -> Mapping[str, object]:
    try:
        from . import rq0_l0_compcert_heldout_fixture_exact as fixture
    except ImportError:
        import rq0_l0_compcert_heldout_fixture_exact as fixture
    return adapt_opened_legacy_dataset(fixture.build_dataset())
