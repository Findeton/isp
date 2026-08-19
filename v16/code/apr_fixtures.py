#!/usr/bin/env python3
"""Primitive, result-neutral fixture declarations for APR.

The objects below are frozen inputs.  This module does not evaluate a future
profile, multiply a transport chain, score a comparison, run a regional
process, or attach a physical interpretation to a fixture.  Finite words,
matrices, transition expressions, and cospan presentations are verification
data only.

Importing the module has no side effects.  The sole command-line mode checks
schema/reference/canonical-form integrity and prints a canonical content hash
to standard output.  It has no output-path argument and writes no file.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from typing import Iterable, Mapping, Sequence

from apr_core import (
    BoundaryLeg,
    BoundaryType,
    PrefixRegion,
    RegionType,
    StructuredCospan,
    canonical_json,
    canonical_sha256,
    exact,
    validate_cospan,
)


SCHEMA = "apr-primitive-fixtures-v1"


def _matrix(rows: Sequence[Sequence[object]], columns: int | None = None) -> dict[str, object]:
    """Freeze a rectangular exact matrix without performing linear algebra."""

    materialized = tuple(tuple(str(item) for item in row) for row in rows)
    width = len(materialized[0]) if materialized else columns
    if width is None:
        raise ValueError("an empty primitive matrix needs a column count")
    if any(len(row) != width for row in materialized):
        raise ValueError("ragged primitive matrix")
    for row in materialized:
        for item in row:
            exact(item)
    return {
        "shape": [len(materialized), width],
        "rows": [list(row) for row in materialized],
    }


def _region(identifier: str, words: Sequence[str]) -> dict[str, object]:
    return {"id": identifier, "antichain": list(words)}


PREFIX_CONTROLS: dict[str, object] = {
    "alphabet": ["0", "1"],
    "region_grammar": {
        "id": "pg_000",
        "productions": [
            "word := epsilon | word 0 | word 1",
            "cylinder := cyl(word)",
            "region := zero | cylinder | join(region, region)",
        ],
        "normal_form": "finite prefix-free antichain with recursive sibling reduction",
    },
    "regions": [
        _region("rg_000", ()),
        _region("rg_001", ("",)),
        _region("rg_002", ("0",)),
        _region("rg_003", ("1",)),
        _region("rg_004", ("00",)),
        _region("rg_005", ("01",)),
        _region("rg_006", ("10",)),
        _region("rg_007", ("11",)),
        _region("rg_008", ("00", "10")),
        _region("rg_009", ("01", "11")),
    ],
    "branch_characters": [
        {
            "id": "uc_000",
            "alphabet": ["0", "1"],
            "branch_rule": {"operation": "repeat_symbol", "symbol": "0"},
            "character_rule": "one iff some listed cylinder contains the generated branch",
        }
    ],
    "probe_catalogues": [
        {
            "id": "pc_000",
            "region_ids": ["rg_000", "rg_001", "rg_002", "rg_003"],
        },
        {
            "id": "pc_001",
            "generator_id": "pg_000",
        },
        {
            "id": "pc_002",
            "base_catalogue_id": "pc_000",
            "appended_region_ids": ["rg_004"],
        },
    ],
    "profile_expression": {
        "arguments": ["candidate_region", "probe_region"],
        "expression": "mu(meet(candidate_region, probe_region))",
    },
    "character_quotient_expression": {
        "equivalence": "same branch_character value",
        "operations": ["meet", "join", "complement"],
    },
}


LINEAR_CONTINUATION_PRIMITIVES: dict[str, object] = {
    "spaces": [{"id": "vs_000", "dimension": 3}],
    "profiles": [
        {
            "id": "lp_000",
            "space_id": "vs_000",
            "matrix": _matrix(((1, 0, 0),)),
        }
    ],
    "continuations": [
        {
            "id": "lt_000",
            "source_space_id": "vs_000",
            "target_space_id": "vs_000",
            "matrix": _matrix(((0, 1, 0), (0, 0, 1), (1, 0, 0))),
        }
    ],
    "registered_words": [
        {"id": "lw_000", "continuation_ids": []},
        {"id": "lw_001", "continuation_ids": ["lt_000"]},
        {"id": "lw_002", "continuation_ids": ["lt_000", "lt_000"]},
        {
            "id": "lw_003",
            "continuation_ids": ["lt_000", "lt_000", "lt_000"],
        },
    ],
}


COMPARISON_PRIMITIVES: dict[str, object] = {
    "spaces": [
        {"id": "cs_000", "dimension": 2},
        {"id": "cs_001", "dimension": 2},
        {"id": "cs_002", "dimension": 3},
    ],
    "vectors": [
        {"id": "cv_000", "space_id": "cs_000", "entries": ["1", "0"]},
        {"id": "cv_001", "space_id": "cs_000", "entries": ["0", "1"]},
        {"id": "cv_002", "space_id": "cs_001", "entries": ["1", "0"]},
        {"id": "cv_003", "space_id": "cs_001", "entries": ["0", "1"]},
    ],
    "maps": [
        {
            "id": "cm_000",
            "source_space_id": "cs_000",
            "target_space_id": "cs_002",
            "matrix": _matrix(((1, 0), (0, 1), (0, 0))),
        },
        {
            "id": "cm_001",
            "source_space_id": "cs_001",
            "target_space_id": "cs_002",
            "matrix": _matrix(((1, 0), (0, 1), (0, 0))),
        },
        {
            "id": "cm_002",
            "source_space_id": "cs_001",
            "target_space_id": "cs_002",
            "matrix": _matrix(((1, 0), (0, 0), (0, 1))),
        },
        {
            "id": "cm_003",
            "source_space_id": "cs_001",
            "target_space_id": "cs_002",
            "matrix": _matrix(((0, 0), (0, 1), (0, 0))),
        },
        {
            "id": "cm_004",
            "source_space_id": "cs_001",
            "target_space_id": "cs_002",
            "matrix": _matrix(((1, 0), (0, -1), (0, 0))),
        },
    ],
    "target_profile_catalogues": [
        {
            "id": "cp_000",
            "space_id": "cs_002",
            "matrix": _matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1))),
        },
        {
            "id": "cp_001",
            "space_id": "cs_002",
            "matrix": _matrix(((1, 0, 0), (0, 1, 1))),
        },
        {
            "id": "cp_002",
            "space_id": "cs_002",
            "matrix": _matrix(((1, 0, 0),)),
        },
    ],
    "configurations": [
        {
            "id": "cc_000",
            "left_map_id": "cm_000",
            "right_map_id": "cm_001",
            "target_profile_id": "cp_000",
        },
        {
            "id": "cc_001",
            "left_map_id": "cm_000",
            "right_map_id": "cm_002",
            "target_profile_id": "cp_000",
        },
        {
            "id": "cc_002",
            "left_map_id": "cm_000",
            "right_map_id": "cm_002",
            "target_profile_id": "cp_001",
        },
        {
            "id": "cc_003",
            "left_map_id": "cm_000",
            "right_map_id": "cm_003",
            "target_profile_id": "cp_000",
        },
        {
            "id": "cc_004",
            "left_map_id": "cm_000",
            "right_map_id": "cm_004",
            "target_profile_id": "cp_002",
        },
    ],
    "coherent_reference": {
        "id": "cr_000",
        "source_vector_ids": ["cv_001", "cv_003"],
        "map_slots": ["left_map_id", "right_map_id"],
        "combination_coefficients": ["1", "1"],
        "quadratic_scale": "1/4",
        "target_pairing": "standard_exact_pairing",
    },
}


PREDICTIVE_BOUNDARY_PRIMITIVES: dict[str, object] = {
    "labels": ["bl_000", "bl_001", "bl_002"],
    "future_profile": {
        "id": "bp_000",
        "matrix": _matrix(((1, 1, 0), (0, 0, 1))),
    },
    "presentations": [
        {"id": "bm_000", "matrix": _matrix(((1, 1, 0), (0, 0, 1)))},
        {"id": "bm_001", "matrix": _matrix(((1, 1, 1),))},
        {
            "id": "bm_002",
            "matrix": _matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1))),
        },
        {"id": "bm_003", "matrix": _matrix(((1, 1, 1), (1, 1, -1)))},
    ],
    "label_partitions": [
        {"id": "bk_000", "blocks": [["bl_000", "bl_001"], ["bl_002"]]},
        {"id": "bk_001", "blocks": [["bl_000", "bl_001", "bl_002"]]},
        {
            "id": "bk_002",
            "blocks": [["bl_000"], ["bl_001"], ["bl_002"]],
        },
    ],
    "basis_changes": [
        {"id": "bc_000", "matrix": _matrix(((1, 1), (1, -1)))},
    ],
    "future_extensions": [
        {
            "id": "be_000",
            "base_profile_id": "bp_000",
            "appended_rows": _matrix(((1, 0, 0),)),
        }
    ],
}


TYPED_FILLING_PRIMITIVES: dict[str, object] = {
    "boundaries": [
        {"id": "bd_000", "generators": ["a"]},
        {"id": "bd_001", "generators": ["b"]},
        {"id": "bd_002", "generators": ["c"]},
        {"id": "bd_003", "generators": ["d"]},
        {"id": "bd_004", "generators": ["x0", "x1"]},
        {"id": "bd_005", "generators": ["s"]},
        {"id": "bd_006", "generators": ["b0", "b1"]},
        {"id": "bd_007", "generators": ["b", "r"]},
        {"id": "bd_008", "generators": ["epsilon"]},
        {"id": "bd_009", "generators": ["0", "1"]},
        {"id": "bd_010", "generators": ["00", "01", "10", "11"]},
        {
            "id": "bd_011",
            "generators": ["000", "001", "010", "011", "100", "101", "110", "111"],
        },
        {"id": "bd_012", "generators": ["beta0", "beta1"]},
    ],
    "apices": [
        {"id": "ap_000", "generators": ["a"]},
        {"id": "ap_001", "generators": ["a_in", "b_out", "u"]},
        {"id": "ap_002", "generators": ["b_in", "c_out", "v"]},
        {"id": "ap_003", "generators": ["a_in", "d_out", "w"]},
        {"id": "ap_004", "generators": ["d_in", "c_out", "y"]},
        {"id": "ap_005", "generators": ["a_in", "c_out", "q"]},
        {"id": "ap_006", "generators": ["s"]},
        {"id": "ap_007", "generators": ["x_in", "c_out"]},
        {"id": "ap_008", "generators": ["b_in", "b_out", "record"]},
        {"id": "ap_009", "generators": ["event_epsilon", "event_0", "event_1"]},
        {
            "id": "ap_010",
            "generators": [
                "event_0",
                "event_1",
                "event_00",
                "event_01",
                "event_10",
                "event_11",
            ],
        },
        {
            "id": "ap_011",
            "generators": [
                "event_00",
                "event_01",
                "event_10",
                "event_11",
                "event_000",
                "event_001",
                "event_010",
                "event_011",
                "event_100",
                "event_101",
                "event_110",
                "event_111",
            ],
        },
        {
            "id": "ap_012",
            "generators": [
                "event_epsilon",
                "event_0",
                "event_1",
                "event_00",
                "event_01",
                "event_10",
                "event_11",
            ],
        },
        {
            "id": "ap_013",
            "generators": [
                "event_0",
                "event_1",
                "event_00",
                "event_01",
                "event_10",
                "event_11",
                "event_000",
                "event_001",
                "event_010",
                "event_011",
                "event_100",
                "event_101",
                "event_110",
                "event_111",
            ],
        },
        {
            "id": "ap_014",
            "generators": [
                "event_epsilon",
                "event_0",
                "event_1",
                "event_00",
                "event_01",
                "event_10",
                "event_11",
                "event_000",
                "event_001",
                "event_010",
                "event_011",
                "event_100",
                "event_101",
                "event_110",
                "event_111",
            ],
        },
        {"id": "ap_015", "generators": ["epsilon"]},
        {"id": "ap_016", "generators": ["swap_event"]},
    ],
    "horizontal_fillings": [
        {
            "id": "hf_000",
            "incoming_boundary_id": "bd_000",
            "outgoing_boundary_id": "bd_000",
            "apex_id": "ap_000",
            "incoming_images": [["a", "a"]],
            "outgoing_images": [["a", "a"]],
        },
        {
            "id": "hf_001",
            "incoming_boundary_id": "bd_000",
            "outgoing_boundary_id": "bd_001",
            "apex_id": "ap_001",
            "incoming_images": [["a", "a_in"]],
            "outgoing_images": [["b", "b_out"]],
        },
        {
            "id": "hf_002",
            "incoming_boundary_id": "bd_001",
            "outgoing_boundary_id": "bd_002",
            "apex_id": "ap_002",
            "incoming_images": [["b", "b_in"]],
            "outgoing_images": [["c", "c_out"]],
        },
        {
            "id": "hf_003",
            "incoming_boundary_id": "bd_000",
            "outgoing_boundary_id": "bd_003",
            "apex_id": "ap_003",
            "incoming_images": [["a", "a_in"]],
            "outgoing_images": [["d", "d_out"]],
        },
        {
            "id": "hf_004",
            "incoming_boundary_id": "bd_003",
            "outgoing_boundary_id": "bd_002",
            "apex_id": "ap_004",
            "incoming_images": [["d", "d_in"]],
            "outgoing_images": [["c", "c_out"]],
        },
        {
            "id": "hf_005",
            "incoming_boundary_id": "bd_000",
            "outgoing_boundary_id": "bd_002",
            "apex_id": "ap_005",
            "incoming_images": [["a", "a_in"]],
            "outgoing_images": [["c", "c_out"]],
        },
        {
            "id": "hf_006",
            "incoming_boundary_id": "bd_005",
            "outgoing_boundary_id": "bd_005",
            "apex_id": "ap_006",
            "incoming_images": [["s", "s"]],
            "outgoing_images": [["s", "s"]],
        },
        {
            "id": "hf_007",
            "incoming_boundary_id": "bd_004",
            "outgoing_boundary_id": "bd_002",
            "apex_id": "ap_007",
            "incoming_images": [["x0", "x_in"], ["x1", "x_in"]],
            "outgoing_images": [["c", "c_out"]],
        },
        {
            "id": "hf_008",
            "incoming_boundary_id": "bd_001",
            "outgoing_boundary_id": "bd_007",
            "apex_id": "ap_008",
            "incoming_images": [["b", "b_in"]],
            "outgoing_images": [["b", "b_out"], ["r", "record"]],
        },
        {
            "id": "hf_009",
            "incoming_boundary_id": "bd_008",
            "outgoing_boundary_id": "bd_009",
            "apex_id": "ap_009",
            "incoming_images": [["epsilon", "event_epsilon"]],
            "outgoing_images": [["0", "event_0"], ["1", "event_1"]],
            "apex_relations": [
                ["event_epsilon", "event_0"],
                ["event_epsilon", "event_1"],
            ],
        },
        {
            "id": "hf_010",
            "incoming_boundary_id": "bd_009",
            "outgoing_boundary_id": "bd_010",
            "apex_id": "ap_010",
            "incoming_images": [["0", "event_0"], ["1", "event_1"]],
            "outgoing_images": [
                ["00", "event_00"],
                ["01", "event_01"],
                ["10", "event_10"],
                ["11", "event_11"],
            ],
            "apex_relations": [
                ["event_0", "event_00"],
                ["event_0", "event_01"],
                ["event_1", "event_10"],
                ["event_1", "event_11"],
            ],
        },
        {
            "id": "hf_011",
            "incoming_boundary_id": "bd_010",
            "outgoing_boundary_id": "bd_011",
            "apex_id": "ap_011",
            "incoming_images": [
                ["00", "event_00"],
                ["01", "event_01"],
                ["10", "event_10"],
                ["11", "event_11"],
            ],
            "outgoing_images": [
                ["000", "event_000"],
                ["001", "event_001"],
                ["010", "event_010"],
                ["011", "event_011"],
                ["100", "event_100"],
                ["101", "event_101"],
                ["110", "event_110"],
                ["111", "event_111"],
            ],
            "apex_relations": [
                ["event_00", "event_000"],
                ["event_00", "event_001"],
                ["event_01", "event_010"],
                ["event_01", "event_011"],
                ["event_10", "event_100"],
                ["event_10", "event_101"],
                ["event_11", "event_110"],
                ["event_11", "event_111"],
            ],
        },
        {
            "id": "hf_012",
            "incoming_boundary_id": "bd_008",
            "outgoing_boundary_id": "bd_010",
            "apex_id": "ap_012",
            "incoming_images": [["epsilon", "event_epsilon"]],
            "outgoing_images": [
                ["00", "event_00"],
                ["01", "event_01"],
                ["10", "event_10"],
                ["11", "event_11"],
            ],
            "apex_relations": [
                ["event_epsilon", "event_0"],
                ["event_epsilon", "event_1"],
                ["event_0", "event_00"],
                ["event_0", "event_01"],
                ["event_1", "event_10"],
                ["event_1", "event_11"],
            ],
        },
        {
            "id": "hf_013",
            "incoming_boundary_id": "bd_009",
            "outgoing_boundary_id": "bd_011",
            "apex_id": "ap_013",
            "incoming_images": [["0", "event_0"], ["1", "event_1"]],
            "outgoing_images": [
                ["000", "event_000"],
                ["001", "event_001"],
                ["010", "event_010"],
                ["011", "event_011"],
                ["100", "event_100"],
                ["101", "event_101"],
                ["110", "event_110"],
                ["111", "event_111"],
            ],
            "apex_relations": [
                ["event_0", "event_00"],
                ["event_0", "event_01"],
                ["event_1", "event_10"],
                ["event_1", "event_11"],
                ["event_00", "event_000"],
                ["event_00", "event_001"],
                ["event_01", "event_010"],
                ["event_01", "event_011"],
                ["event_10", "event_100"],
                ["event_10", "event_101"],
                ["event_11", "event_110"],
                ["event_11", "event_111"],
            ],
        },
        {
            "id": "hf_014",
            "incoming_boundary_id": "bd_008",
            "outgoing_boundary_id": "bd_011",
            "apex_id": "ap_014",
            "incoming_images": [["epsilon", "event_epsilon"]],
            "outgoing_images": [
                ["000", "event_000"],
                ["001", "event_001"],
                ["010", "event_010"],
                ["011", "event_011"],
                ["100", "event_100"],
                ["101", "event_101"],
                ["110", "event_110"],
                ["111", "event_111"],
            ],
            "apex_relations": [
                ["event_epsilon", "event_0"],
                ["event_epsilon", "event_1"],
                ["event_0", "event_00"],
                ["event_0", "event_01"],
                ["event_1", "event_10"],
                ["event_1", "event_11"],
                ["event_00", "event_000"],
                ["event_00", "event_001"],
                ["event_01", "event_010"],
                ["event_01", "event_011"],
                ["event_10", "event_100"],
                ["event_10", "event_101"],
                ["event_11", "event_110"],
                ["event_11", "event_111"],
            ],
        },
        {
            "id": "hf_015",
            "incoming_boundary_id": "bd_008",
            "outgoing_boundary_id": "bd_008",
            "apex_id": "ap_015",
            "incoming_images": [["epsilon", "epsilon"]],
            "outgoing_images": [["epsilon", "epsilon"]],
            "apex_relations": [],
        },
        {
            "id": "hf_016",
            "incoming_boundary_id": "bd_008",
            "outgoing_boundary_id": "bd_008",
            "apex_id": "ap_016",
            "incoming_images": [["epsilon", "swap_event"]],
            "outgoing_images": [["epsilon", "swap_event"]],
            "apex_relations": [],
        },
    ],
    "factorizations": [
        {
            "id": "fx_002",
            "whole_filling_id": "hf_014",
            "step_ids": ["hf_009", "hf_013"],
            "intermediate_boundary_ids": ["bd_009"],
        },
        {
            "id": "fx_003",
            "whole_filling_id": "hf_014",
            "step_ids": ["hf_012", "hf_011"],
            "intermediate_boundary_ids": ["bd_010"],
        },
        {
            "id": "fx_004",
            "whole_filling_id": "hf_014",
            "step_ids": ["hf_009", "hf_010", "hf_011"],
            "intermediate_boundary_ids": ["bd_009", "bd_010"],
        },
    ],
    "monoidal_presentations": [
        {
            "id": "mp_000",
            "active_filling_id": "hf_001",
            "spectator_filling_id": "hf_006",
        }
    ],
    "sequence_presentations": [
        {"id": "sq_000", "step_ids": ["hf_001", "hf_002"]},
        {"id": "sq_001", "step_ids": ["hf_001", "hf_007"]},
    ],
    "vertical_maps": [
        {
            "id": "vm_000",
            "source_boundary_id": "bd_006",
            "target_boundary_id": "bd_001",
            "images": [["b0", "b"], ["b1", "b"]],
            "map_sort": "many_to_one_boundary_map",
        },
        {
            "id": "vm_001",
            "source_boundary_id": "bd_007",
            "target_boundary_id": "bd_001",
            "images": [["b", "b"], ["r", "b"]],
            "map_sort": "record_retyping_candidate",
        },
        {
            "id": "vm_002",
            "source_boundary_id": "bd_006",
            "target_boundary_id": "bd_012",
            "images": [["b0", "beta0"], ["b1", "beta1"]],
            "map_sort": "passive_presentation_isomorphism",
            "inverse_map_id": "vm_003",
        },
        {
            "id": "vm_003",
            "source_boundary_id": "bd_012",
            "target_boundary_id": "bd_006",
            "images": [["beta0", "b0"], ["beta1", "b1"]],
            "map_sort": "passive_presentation_isomorphism",
            "inverse_map_id": "vm_002",
        },
    ],
    "arrow_retypings": [
        {
            "id": "ar_000",
            "primitive_id": "hf_008",
            "proposed_arrow_sort": "horizontal_filling",
        },
        {
            "id": "ar_001",
            "primitive_id": "hf_008",
            "proposed_arrow_sort": "vertical_comparison",
        },
    ],
}


REGIONAL_QUESTION_PROCESS: dict[str, object] = {
    "schema_id": "qp_000",
    "law_semantics": "classical finitely additive regional probability process",
    "representation": {
        "regional_state": {
            "fields": [
                {
                    "name": "preparation_support",
                    "type": "PrefixRegion",
                    "constraint": "nonzero for a prepared root",
                },
                {
                    "name": "valuation",
                    "type": "positive finitely additive rational functional on the prefix algebra",
                    "normalization": "arbitrary nonnegative total mass",
                    "support_constraint": "nu(A)=nu(meet(A,preparation_support))",
                },
                {
                    "name": "record_word",
                    "type": "finite_sequence(question_token, port_token)",
                    "update_operation": "append",
                },
            ]
        },
        "filling_composition": {
            "objects": "typed regional boundaries",
            "arrows": "finite record-labelled decision-tree fillings",
            "identity": "empty_tree",
            "operation": "grafting at every compatible live record port",
            "linear_word_role": "a uniform-depth tree presentation of one bounded composition",
        },
        "port_carrier": {
            "type": "positive finitely additive valuation cone with record label",
            "zero_element": "zero valuation retained as a typed port",
        },
    },
    "question_grammar": {
        "id": "qg_000",
        "region_grammar_id": "pg_000",
        "production": "question := ask(region)",
        "question_identity": "canonical region antichain",
    },
    "decision_tree_grammar": {
        "id": "qg_001",
        "productions": [
            "tree := empty_tree",
            "tree := node(question, port_0:tree, port_1:tree)",
        ],
        "composition_domain": "finite record-labelled decision trees",
        "identity": "empty_tree",
    },
    "valuation_family": {
        "id": "qv_000",
        "parameter_domain": "rational p with 0 < p < 1",
        "cylinder_expression": "p^count_0(word) * (1-p)^count_1(word)",
        "region_expression": "sum over cylinders in the canonical antichain",
        "law_role": "preparation rows inside the full valuation cone",
        "parameter_rows": [
            {"id": "vp_000", "p": "1/2"},
            {"id": "vp_001", "p": "1/3"},
        ],
    },
    "question_transition": {
        "id": "qt_000",
        "inputs": ["valuation nu", "question C", "record_word R"],
        "map_type": "affine positive map on the full finitely additive valuation cone",
        "ports": [
            {
                "id": "pt_000",
                "next_valuation": "Q_C^1(nu)(A)=nu(meet(A,C))",
                "next_record_word": "append(R,(C,pt_000))",
                "zero_element_policy": "retain the typed port",
            },
            {
                "id": "pt_001",
                "next_valuation": "Q_C^0(nu)(A)=nu(meet(A,complement(C)))",
                "next_record_word": "append(R,(C,pt_001))",
                "zero_element_policy": "retain the typed port",
            },
        ],
    },
    "replacement_grammar": {
        "id": "qg_002",
        "production": "replacement := swap_children(cylinder)",
        "regional_action": "sigma_A exchanges the two child cylinders of A and fixes complement(A)",
        "state_map": "T_A(nu)(B)=nu(inverse_sigma_A(B))",
        "record_update": "identity(record_word)",
        "support_scope": "the declared cylinder A",
    },
    "intrinsic_replacement_grammar": {
        "id": "qg_004",
        "production": "intrinsic_replacement := relative_complement_map(target_region,finite_partition,generator)",
        "support_scope": "complement(target_region)",
        "generator_family": "all finite-partition automorphisms and rational mixing maps supported in the relative complement",
        "transitivity_rule": "the generated semigroup is transitive on the declared finite complement-partition blocks",
        "state_map": "T_g(nu)(B)=nu(inverse_g(B)) for automorphisms, extended affinely to rational mixtures",
        "vertical_closure": "G(complement(jA))=j G(complement(A)) inverse_j",
        "record_update": "identity(record_word)",
    },
    "replacement_primitives": [
        {"id": "rs_000", "operation": "swap_children", "support_region_id": "rg_002"},
        {"id": "rs_001", "operation": "swap_children", "support_region_id": "rg_003"},
        {"id": "rs_002", "operation": "swap_children", "support_region_id": "rg_004"},
        {"id": "rs_003", "operation": "identity_replacement", "support_region_id": "rg_001"},
        {"id": "rs_006", "operation": "swap_children", "support_region_id": "rg_005"},
        {
            "id": "rs_004",
            "operation": "relative_complement_generator_family",
            "target_region_id": "rg_002",
            "partition_region_ids": ["rg_003"],
            "grammar_id": "qg_004",
        },
        {
            "id": "rs_005",
            "operation": "relative_complement_generator_family",
            "target_region_id": "rg_004",
            "partition_region_ids": ["rg_005", "rg_003"],
            "grammar_id": "qg_004",
        },
    ],
    "finite_replacement_boundary": {
        "id": "qb_000",
        "leaf_tokens": ["00", "01", "10", "11"],
        "maps": [
            {
                "id": "qm_000",
                "replacement_id": "rs_000",
                "matrix": _matrix(
                    ((0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
                ),
            },
            {
                "id": "qm_001",
                "replacement_id": "rs_001",
                "matrix": _matrix(
                    ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0))
                ),
            },
            {
                "id": "qm_002",
                "replacement_id": "rs_003",
                "matrix": _matrix(
                    ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
                ),
            },
        ],
        "effect_catalogues": [
            {
                "id": "qe_000",
                "target_region_id": "rg_002",
                "replacement_ids": ["rs_001"],
                "calibrated_effect_rows": _matrix(
                    (
                        (1, 0, 0, 0),
                        (0, 1, 0, 0),
                        (0, 0, 1, 0),
                        (0, 0, 0, 1),
                        (1, 1, 1, 1),
                    )
                ),
            }
        ],
        "refined_boundaries": [
            {
                "id": "qb_001",
                "leaf_tokens": ["000", "001", "010", "011", "100", "101", "110", "111"],
                "calibrated_effect_rows": _matrix(
                    (
                        (1, 0, 0, 0, 0, 0, 0, 0),
                        (0, 1, 0, 0, 0, 0, 0, 0),
                        (0, 0, 1, 0, 0, 0, 0, 0),
                        (0, 0, 0, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 0),
                        (0, 0, 0, 0, 0, 0, 0, 1),
                        (1, 1, 1, 1, 1, 1, 1, 1),
                    )
                ),
            }
        ],
    },
    "operations": [
        {
            "id": "qo_000",
            "operation": "apply_question",
            "transition_id": "qt_000",
        },
        {
            "id": "qo_001",
            "operation": "read_record_word",
            "expression": "identity(record_word)",
        },
        {
            "id": "qo_002",
            "operation": "compose_spectator",
            "expression": "tensor_with_independent_identity_filling",
        },
        {
            "id": "qo_003",
            "operation": "erase_last_record_token",
            "expression": "drop_last(record_word)",
        },
        {
            "id": "qo_004",
            "operation": "reset_record_word",
            "expression": "empty_sequence",
        },
        {
            "id": "qo_005",
            "operation": "delay_without_record_access",
            "expression": "identity on valuation and record carrier",
        },
        {
            "id": "qo_006",
            "operation": "read_record_after_delay",
            "expression": "read record_word after registered delay operations",
        },
        {
            "id": "qo_007",
            "operation": "apply_region_supported_replacement",
            "grammar_id": "qg_002",
        },
        {
            "id": "qo_008",
            "operation": "apply_identity_replacement",
            "replacement_id": "rs_003",
        },
        {
            "id": "qo_009",
            "operation": "apply_intrinsic_relative_complement_replacement",
            "grammar_id": "qg_004",
        },
    ],
    "continuation_catalogues": [
        {
            "id": "qc_000",
            "operation_ids": [
                "qo_000",
                "qo_001",
                "qo_002",
                "qo_005",
                "qo_006",
                "qo_009",
            ],
        },
        {
            "id": "qc_001",
            "operation_ids": [
                "qo_000",
                "qo_001",
                "qo_002",
                "qo_003",
                "qo_005",
                "qo_006",
                "qo_009",
            ],
        },
        {
            "id": "qc_002",
            "operation_ids": [
                "qo_000",
                "qo_001",
                "qo_002",
                "qo_004",
                "qo_005",
                "qo_006",
                "qo_009",
            ],
        },
        {
            "id": "qc_003",
            "operation_ids": ["qo_000", "qo_001", "qo_002", "qo_005", "qo_006", "qo_008"],
        },
        {
            "id": "qc_004",
            "operation_ids": ["qo_000", "qo_001", "qo_002", "qo_005", "qo_006", "qo_007"],
        },
    ],
    "registered_questions": [
        {"id": "qq_000", "region_id": "rg_002"},
        {"id": "qq_001", "region_id": "rg_003"},
        {"id": "qq_002", "region_id": "rg_004"},
        {"id": "qq_003", "region_id": "rg_005"},
        {"id": "qq_004", "region_id": "rg_001"},
    ],
    "decision_trees": [
        {"id": "qw_000", "expression": "empty_tree"},
        {"id": "qw_001", "expression": "node(qq_000,empty_tree,empty_tree)"},
        {
            "id": "qw_002",
            "expression": "node(qq_000,node(qq_002,empty_tree,empty_tree),node(qq_002,empty_tree,empty_tree))",
        },
        {
            "id": "qw_003",
            "expression": "node(qq_000,node(qq_002,node(qq_003,empty_tree,empty_tree),node(qq_003,empty_tree,empty_tree)),node(qq_002,node(qq_003,empty_tree,empty_tree),node(qq_003,empty_tree,empty_tree)))",
        },
        {"id": "qw_004", "expression": "node(qq_004,empty_tree,empty_tree)"},
    ],
    "mixed_tree_grammar": {
        "id": "qg_003",
        "productions": [
            "mixed_tree := empty_tree",
            "mixed_tree := replace(replacement,mixed_tree)",
            "mixed_tree := node(question,port_0:mixed_tree,port_1:mixed_tree)",
        ],
    },
    "mixed_tree_rows": [
        {"id": "mx_000", "expression": "replace(rs_000,node(qq_000,empty_tree,empty_tree))"},
        {"id": "mx_001", "expression": "replace(rs_000,node(qq_001,empty_tree,empty_tree))"},
        {"id": "mx_002", "expression": "replace(rs_000,replace(rs_001,empty_tree))"},
        {"id": "mx_003", "expression": "replace(rs_001,replace(rs_000,empty_tree))"},
        {"id": "mx_004", "expression": "replace(rs_000,replace(rs_002,empty_tree))"},
        {"id": "mx_005", "expression": "replace(rs_002,replace(rs_000,empty_tree))"},
        {"id": "mx_006", "expression": "replace(rs_003,node(qq_000,empty_tree,empty_tree))"},
        {"id": "mx_007", "expression": "intrinsic_replace(rs_004,node(qq_000,empty_tree,empty_tree))"},
        {"id": "mx_008", "expression": "intrinsic_replace(rs_005,node(qq_002,empty_tree,empty_tree))"},
    ],
    "changed_object_rows": [
        {
            "id": "co_000",
            "preparation_id": "vp_001",
            "replacement_id": "rs_000",
            "question_region_id": "rg_008",
        },
        {
            "id": "co_001",
            "preparation_id": "vp_001",
            "replacement_id": "rs_000",
            "question_region_id": "rg_003",
        },
        {
            "id": "co_002",
            "presentation_map": "exchange prefix symbols 0 and 1",
            "source_replacement_id": "rs_000",
            "target_replacement_id": "rs_001",
        },
        {
            "id": "co_003",
            "target_region_id": "rg_002",
            "restricted_replacement_ids": ["rs_001"],
            "intrinsic_replacement_id": "rs_004",
            "exterior_partition_region_ids": ["rg_003"],
        },
        {
            "id": "co_004",
            "target_region_id": "rg_004",
            "restricted_replacement_ids": ["rs_006", "rs_001"],
            "intrinsic_replacement_id": "rs_005",
            "exterior_partition_region_ids": ["rg_005", "rg_003"],
        },
        {
            "id": "co_005",
            "presentation_map": "exchange region terms rg_005 and rg_006 inside the depth-two partition",
            "source_region_id": "rg_005",
            "target_region_id": "rg_006",
            "source_replacement_id": "rs_000",
            "conjugated_grammar_id": "qg_004",
        },
    ],
    "spectator_schema": {
        "id": "qs_000",
        "active_carrier": "regional valuation cone",
        "spectator_carrier": "independent finitely additive valuation cone",
        "composition": "tensor product of independent carriers",
        "separation_from_regional_operation": "not Boolean meet or disjointness",
    },
    "reader_schedules": [
        {
            "id": "qr_000",
            "tree_id": "qw_001",
            "operation_ids": ["qo_005", "qo_005", "qo_006"],
        }
    ],
    "generated_law_provenance": {
        "id": "ql_000",
        "question_transition_id": "qt_000",
        "question_grammar_id": "qg_000",
        "decision_tree_grammar_id": "qg_001",
        "replacement_grammar_id": "qg_002",
        "boundary_factory": {
            "id": "qf_000",
            "rows": [
                {"tree_depth": 0, "boundary_id": "bd_008"},
                {"tree_depth": 1, "boundary_id": "bd_009"},
                {"tree_depth": 2, "boundary_id": "bd_010"},
                {"tree_depth": 3, "boundary_id": "bd_011"},
            ],
            "record_port_rule": "append 0 or 1 to each incoming record token",
            "depth_role": "finite record-tree presentation depth, not a universal time coordinate",
        },
        "filling_factory": {
            "id": "qf_001",
            "question_rows": [
                {"input_depth": 0, "output_depth": 1, "filling_id": "hf_009"},
                {"input_depth": 1, "output_depth": 2, "filling_id": "hf_010"},
                {"input_depth": 2, "output_depth": 3, "filling_id": "hf_011"},
            ],
            "tree_rows": [
                {"tree_id": "qw_000", "filling_id": "hf_015"},
                {"tree_id": "qw_001", "filling_id": "hf_009"},
                {"tree_id": "qw_002", "filling_id": "hf_012"},
                {"tree_id": "qw_003", "filling_id": "hf_014"},
                {"tree_id": "qw_004", "filling_id": "hf_009"},
            ],
            "replacement_rows": [
                {
                    "root_filling_id": "hf_016",
                    "transfer_grammar_id": "qg_002",
                    "port_rule": "one non-recording event per live record token with identical input and output token",
                },
                {
                    "root_filling_id": "hf_016",
                    "transfer_grammar_id": "qg_004",
                    "port_rule": "one non-recording event per live record token with identical input and output token",
                },
            ],
        },
        "composition_rule": "assignment(graft(U,V)) := compose(assignment(U),assignment(V)) on every compatible live record port",
        "factorization_ids": ["fx_002", "fx_003", "fx_004"],
        "construction_scope": "primitive boundary, generator, and transfer-law provenance; categorical extension is a later gate",
    },
}


REGIONAL_SUPPORT_PRIMITIVES: dict[str, object] = {
    "ambient_dimension": 3,
    "target_region_ids": ["rg_002", "rg_003", "rg_004", "rg_005"],
    "internal_actions": [
        {
            "id": "ia_000",
            "support_region_id": "rg_004",
            "generated_subspace": _matrix(((1,), (0,), (0,))),
        },
        {
            "id": "ia_001",
            "support_region_id": "rg_005",
            "generated_subspace": _matrix(((0,), (1,), (0,))),
        },
        {
            "id": "ia_002",
            "support_region_id": "rg_003",
            "generated_subspace": _matrix(((0,), (0,), (1,))),
        },
        {
            "id": "ia_003",
            "support_region_id": "rg_002",
            "generated_subspace": _matrix(((1,), (1,), (0,))),
        },
    ],
    "exterior_replacements": [
        {
            "id": "er_000",
            "support_region_id": "rg_003",
            "left_profile": _matrix(((0, 1, 0),)),
            "right_profile": _matrix(((0, 0, 0),)),
        },
        {
            "id": "er_001",
            "support_region_id": "rg_002",
            "left_profile": _matrix(((0, 0, 1),)),
            "right_profile": _matrix(((0, 0, 0),)),
        },
        {
            "id": "er_002",
            "support_region_id": "rg_004",
            "left_profile": _matrix(((1, 0, 0),)),
            "right_profile": _matrix(((0, 0, 0),)),
        },
        {
            "id": "er_003",
            "support_region_id": "rg_005",
            "left_profile": _matrix(((0, 1, 1),)),
            "right_profile": _matrix(((0, 0, 0),)),
        },
    ],
    "calibrated_ambient_labels": ["am_000", "am_001", "am_002"],
}


def _topology_edges(topology: str, node_count: int) -> tuple[tuple[int, int], ...]:
    if node_count < 3:
        raise ValueError("regional family members need at least three nodes")
    if topology == "series":
        return tuple((index, index + 1) for index in range(node_count - 1))
    if topology == "fork":
        return tuple((0, index) for index in range(1, node_count))
    if topology == "loop":
        return tuple((index, (index + 1) % node_count) for index in range(node_count))
    raise ValueError(f"unknown topology {topology}")


def _slot_word(slot: int) -> str:
    """Use equal-depth, even slots so no listed pair is sibling-reducible."""

    if slot < 0 or 2 * slot >= 2**12:
        raise ValueError("regional family slot outside frozen word width")
    return format(2 * slot, "012b")


def _regional_family_member(
    identifier: str,
    topology: str,
    node_count: int,
    relation_mode: str,
    slot_offset: int,
) -> dict[str, object]:
    edges = _topology_edges(topology, node_count)
    occurrences: list[dict[str, object]] = []
    region_words: dict[int, list[str]] = {index: [] for index in range(node_count)}
    projections: list[dict[str, str]] = []
    incidences: list[dict[str, object]] = []
    next_slot = slot_offset

    def allocate(token: str, blind_token: str) -> str:
        nonlocal next_slot
        word = _slot_word(next_slot)
        next_slot += 1
        occurrences.append({"component_token": token, "antichain": [word]})
        projections.append(
            {"component_token": token, "blind_component_token": blind_token}
        )
        return word

    for node in range(node_count):
        token = f"private_{node}"
        word = allocate(token, token)
        region_words[node].append(word)

    for edge_index, (left, right) in enumerate(edges):
        blind_token = f"interface_{edge_index}"
        token_a = f"edge_{edge_index}_a"
        token_b = f"edge_{edge_index}_b"
        token_c = f"edge_{edge_index}_c"
        token_d = f"edge_{edge_index}_d"
        word_a = allocate(token_a, f"endpoint_{edge_index}_0")
        word_b = allocate(token_b, f"endpoint_{edge_index}_1")
        word_c = allocate(token_c, blind_token)
        word_d = allocate(token_d, blind_token)
        left_components = [token_a, token_c]
        left_words = [word_a, word_c]
        if relation_mode == "identified_component":
            right_components = [token_b, token_c]
            right_words = [word_b, word_c]
        elif relation_mode == "paired_components":
            right_components = [token_b, token_d]
            right_words = [word_b, word_d]
        else:
            raise ValueError(f"unknown regional relation mode {relation_mode}")
        region_words[left].extend(left_words)
        region_words[right].extend(right_words)
        incidences.append(
            {
                "interface_token": blind_token,
                "node_tokens": [f"node_{left}", f"node_{right}"],
                "left_component_tokens": left_components,
                "right_component_tokens": right_components,
            }
        )

    regions = [
        {
            "node_token": f"node_{node}",
            "antichain": sorted(region_words[node]),
        }
        for node in range(node_count)
    ]
    blind_edges = [
        {
            "interface_token": f"interface_{edge_index}",
            "node_tokens": [f"node_{left}", f"node_{right}"],
        }
        for edge_index, (left, right) in enumerate(edges)
    ]
    return {
        "id": identifier,
        "topology": topology,
        "relation_mode": relation_mode,
        "component_occurrences": occurrences,
        "regions": regions,
        "incidences": incidences,
        "blind_projection": projections,
        "blind_interface": {
            "topology": topology,
            "node_tokens": [f"node_{node}" for node in range(node_count)],
            "edges": blind_edges,
        },
        "resource_declaration": {
            "state_dimension": 8 * node_count,
            "history_depth": 2 * node_count,
            "calibration_slots": 3 * node_count,
            "parameter_slots": 5 * node_count,
        },
    }


_FAMILY_SPECS = (
    ("series", 3, "training"),
    ("fork", 4, "training"),
    ("loop", 3, "training"),
    ("series", 5, "held_out"),
    ("fork", 5, "held_out"),
    ("loop", 5, "held_out"),
)

_regional_members: list[dict[str, object]] = []
_training_ids: list[str] = []
_held_out_ids: list[str] = []
_matched_pairs: list[dict[str, object]] = []
for spec_index, (topology, node_count, registration) in enumerate(_FAMILY_SPECS):
    member_ids: list[str] = []
    for mode_index, mode in enumerate(("identified_component", "paired_components")):
        identifier = f"rf_{2 * spec_index + mode_index:03d}"
        member_ids.append(identifier)
        _regional_members.append(
            _regional_family_member(
                identifier,
                topology,
                node_count,
                mode,
                slot_offset=64 * spec_index,
            )
        )
        if registration == "training":
            _training_ids.append(identifier)
        else:
            _held_out_ids.append(identifier)
    _matched_pairs.append(
        {
            "id": f"rp_{spec_index:03d}",
            "member_ids": member_ids,
        }
    )


REGIONAL_FAMILY_PRIMITIVES: dict[str, object] = {
    "members": _regional_members,
    "matched_pairs": _matched_pairs,
    "registration": {
        "training_ids": _training_ids,
        "held_out_ids": _held_out_ids,
    },
    "blind_rule_classes": [
        {
            "id": "br_000",
            "available_fields": ["blind_interface", "resource_declaration"],
            "memory_interface": "current filling only",
        },
        {
            "id": "br_001",
            "available_fields": ["blind_interface", "resource_declaration"],
            "memory_interface": "registered finite blind-interface words",
        },
        {
            "id": "br_002",
            "available_fields": ["blind_interface", "resource_declaration"],
            "memory_interface": "registered blind histories and calibration requests",
        },
    ],
    "uniform_rule_interface": {
        "inputs": ["blind or regional member presentation", "registered filling word"],
        "parameter_source": "one shared parameter row per rule",
        "held_out_generation": "same callable rule used on every registered member",
    },
}


OVERLAP_GLUING_PRIMITIVES: dict[str, object] = {
    "variables": ["A", "B", "C"],
    "local_boundaries": [
        {
            "id": "ob_000",
            "variable_tokens": ["A", "B"],
            "configurations": ["00", "01", "10", "11"],
            "weights": ["1/4", "1/4", "1/4", "1/4"],
        },
        {
            "id": "ob_001",
            "variable_tokens": ["B", "C"],
            "configurations": ["00", "01", "10", "11"],
            "weights": ["1/4", "1/4", "1/4", "1/4"],
        },
        {
            "id": "ob_002",
            "variable_tokens": ["B"],
            "configurations": ["0", "1"],
            "weights": ["1/2", "1/2"],
        },
    ],
    "restriction_maps": [
        {"id": "om_000", "source_variables": ["A", "B", "C"], "target_boundary_id": "ob_000"},
        {"id": "om_001", "source_variables": ["A", "B", "C"], "target_boundary_id": "ob_001"},
        {"id": "om_002", "source_boundary_id": "ob_000", "target_boundary_id": "ob_002"},
        {"id": "om_003", "source_boundary_id": "ob_001", "target_boundary_id": "ob_002"},
    ],
    "global_candidates": [
        {
            "id": "og_000",
            "variable_tokens": ["A", "B", "C"],
            "configurations": ["000", "001", "010", "011", "100", "101", "110", "111"],
            "weights": ["1/8", "1/8", "1/8", "1/8", "1/8", "1/8", "1/8", "1/8"],
        },
        {
            "id": "og_001",
            "variable_tokens": ["A", "B", "C"],
            "configurations": ["000", "010", "101", "111"],
            "weights": ["1/4", "1/4", "1/4", "1/4"],
        },
    ],
    "gluing_requests": [
        {
            "id": "oj_000",
            "left_boundary_id": "ob_000",
            "right_boundary_id": "ob_001",
            "common_boundary_id": "ob_002",
            "candidate_ids": ["og_000", "og_001"],
        }
    ],
}


INFLUENCE_AND_CONTACT_PRIMITIVES: dict[str, object] = {
    "arenas": [
        {
            "id": "ci_000",
            "node_tokens": ["h", "a", "b"],
            "operation_arrows": [["h", "a"], ["h", "b"]],
            "arrow_operation_id": "io_000",
            "contact_pairs": [],
            "intervention_tokens": ["set_a_0", "set_a_1"],
            "reader_tokens": ["read_b"],
        },
        {
            "id": "ci_001",
            "node_tokens": ["a", "b"],
            "operation_arrows": [["a", "b"]],
            "arrow_operation_id": "io_000",
            "contact_pairs": [],
            "intervention_tokens": ["set_a_0", "set_a_1"],
            "reader_tokens": ["read_b"],
        },
        {
            "id": "ci_002",
            "node_tokens": ["a", "b"],
            "operation_arrows": [["a", "b"], ["b", "a"]],
            "arrow_operation_id": "io_000",
            "contact_pairs": [],
            "intervention_tokens": ["set_a_0", "set_b_0"],
            "reader_tokens": ["read_a", "read_b"],
        },
        {
            "id": "ci_003",
            "node_tokens": ["a", "b"],
            "operation_arrows": [],
            "contact_pairs": [["a", "b"]],
            "region_assignments": [["a", "rg_002"], ["b", "rg_003"]],
            "joint_filling_tokens": ["joint_ab"],
            "intervention_tokens": ["set_a_0", "set_a_1"],
            "reader_tokens": ["read_b"],
        },
    ],
    "operation_schemas": [
        {"id": "io_000", "expression": "copy source bit to target bit"},
        {"id": "io_001", "expression": "set selected source bit to supplied bit"},
        {"id": "io_002", "expression": "read selected target bit into a record token"},
    ],
    "common_boundary_schema": {
        "id": "ib_000",
        "fields": ["prepared source bits", "intervention token", "reader token"],
    },
}


RECORD_RECOVERY_PRIMITIVES: dict[str, object] = {
    "carrier_schema": {
        "id": "rb_000",
        "fields": ["source_bit", "flag_0", "flag_1"],
        "alphabet": ["0", "1"],
    },
    "operations": [
        {
            "id": "ro_000",
            "input_fields": ["source_bit", "flag_0", "flag_1"],
            "output_fields": ["source_bit", "source_bit", "flag_1"],
        },
        {
            "id": "ro_001",
            "input_fields": ["source_bit", "flag_0", "flag_1"],
            "output_fields": ["source_bit", "flag_0", "source_bit"],
        },
        {
            "id": "ro_002",
            "input_fields": ["source_bit", "flag_0", "flag_1"],
            "output_fields": ["source_bit", "0", "flag_1"],
        },
        {
            "id": "ro_003",
            "input_fields": ["source_bit", "flag_0", "flag_1"],
            "output_fields": ["source_bit", "0", "0"],
        },
        {
            "id": "ro_004",
            "input_fields": ["source_bit", "flag_0", "flag_1"],
            "output_fields": ["flag_0"],
        },
        {
            "id": "ro_005",
            "input_fields": ["source_bit", "flag_0", "flag_1"],
            "output_fields": ["flag_1"],
        },
    ],
    "operation_words": [
        {"id": "rw_000", "operation_ids": ["ro_000", "ro_002", "ro_004"]},
        {"id": "rw_001", "operation_ids": ["ro_000", "ro_001", "ro_002", "ro_005"]},
        {"id": "rw_002", "operation_ids": ["ro_000", "ro_001", "ro_003", "ro_004", "ro_005"]},
    ],
    "reader_delays": [
        {"id": "rd_000", "writer_operation_id": "ro_000", "delay_count": 2, "reader_operation_id": "ro_004"},
        {"id": "rd_001", "writer_operation_id": "ro_001", "delay_count": 3, "reader_operation_id": "ro_005"},
    ],
}


COHERENT_COMPARATOR_PRIMITIVES: dict[str, object] = {
    "namespace": "separate comparator outside the regional-question process",
    "carriers": [{"id": "ec_000", "dimension": 2}],
    "maps": [
        {
            "id": "ec_001",
            "source_carrier_id": "ec_000",
            "target_carrier_id": "ec_000",
            "matrix": _matrix((("3/5", "-4/5"), ("4/5", "3/5"))),
        },
        {
            "id": "ec_002",
            "source_carrier_id": "ec_000",
            "target_carrier_id": "ec_000",
            "matrix": _matrix((("3/5", "4/5"), ("-4/5", "3/5"))),
        },
    ],
    "family_link": {
        "regional_family_id": "rf_006",
        "input_interface": "blind_interface only",
        "composition_role": "external E37 comparator",
    },
}


FIXTURE_DATA: dict[str, object] = {
    "schema": SCHEMA,
    "prefix_controls": PREFIX_CONTROLS,
    "linear_continuations": LINEAR_CONTINUATION_PRIMITIVES,
    "comparisons": COMPARISON_PRIMITIVES,
    "predictive_boundaries": PREDICTIVE_BOUNDARY_PRIMITIVES,
    "typed_fillings": TYPED_FILLING_PRIMITIVES,
    "regional_question_process": REGIONAL_QUESTION_PROCESS,
    "regional_support": REGIONAL_SUPPORT_PRIMITIVES,
    "regional_families": REGIONAL_FAMILY_PRIMITIVES,
    "overlap_gluing": OVERLAP_GLUING_PRIMITIVES,
    "influence_contact": INFLUENCE_AND_CONTACT_PRIMITIVES,
    "record_recovery": RECORD_RECOVERY_PRIMITIVES,
    "coherent_comparator": COHERENT_COMPARATOR_PRIMITIVES,
}


_NEUTRAL_ID = re.compile(r"^[a-z]{2}_[0-9]{3}$")
_FORBIDDEN_KEY_PARTS = ("expected", "verdict", "outcome", "screen")


def _walk(value: object, path: tuple[str, ...] = ()) -> Iterable[tuple[tuple[str, ...], object]]:
    yield path, value
    if isinstance(value, Mapping):
        for key in sorted(value, key=str):
            yield from _walk(value[key], path + (str(key),))
    elif isinstance(value, (tuple, list)):
        for index, item in enumerate(value):
            yield from _walk(item, path + (str(index),))


def _declared_ids(value: object) -> dict[str, tuple[str, ...]]:
    declared: dict[str, tuple[str, ...]] = {}
    for path, item in _walk(value):
        if not path or path[-1] not in {"id", "schema_id"}:
            continue
        if not isinstance(item, str) or not _NEUTRAL_ID.fullmatch(item):
            raise ValueError(f"non-neutral fixture identifier at {'/'.join(path)}")
        if item in declared:
            raise ValueError(
                f"duplicate fixture identifier {item} at {'/'.join(declared[item])} and {'/'.join(path)}"
            )
        declared[item] = path
    return declared


def _validate_references(value: object, declared: Mapping[str, tuple[str, ...]]) -> None:
    for path, item in _walk(value):
        if not path:
            continue
        key = path[-1]
        if key in {"id", "schema_id"}:
            continue
        references: tuple[str, ...] = ()
        if key.endswith("_id") and isinstance(item, str):
            references = (item,)
        elif key.endswith("_ids") and isinstance(item, list):
            if any(not isinstance(entry, str) for entry in item):
                raise ValueError(f"non-string fixture reference at {'/'.join(path)}")
            references = tuple(item)
        for reference in references:
            if reference not in declared:
                raise ValueError(f"unknown fixture reference {reference} at {'/'.join(path)}")


def _validate_matrix_records(value: object) -> None:
    for path, item in _walk(value):
        if not isinstance(item, Mapping) or "shape" not in item or "rows" not in item:
            continue
        shape = item["shape"]
        rows = item["rows"]
        if (
            not isinstance(shape, list)
            or len(shape) != 2
            or any(isinstance(entry, bool) or not isinstance(entry, int) or entry < 0 for entry in shape)
        ):
            raise ValueError(f"bad primitive matrix shape at {'/'.join(path)}")
        if not isinstance(rows, list) or len(rows) != shape[0]:
            raise ValueError(f"bad primitive matrix height at {'/'.join(path)}")
        for row in rows:
            if not isinstance(row, list) or len(row) != shape[1]:
                raise ValueError(f"bad primitive matrix width at {'/'.join(path)}")
            for scalar in row:
                exact(scalar)


def _validate_antichains(value: object) -> None:
    for path, item in _walk(value):
        if not path or path[-1] != "antichain":
            continue
        if not isinstance(item, list) or any(not isinstance(word, str) for word in item):
            raise ValueError(f"bad primitive antichain at {'/'.join(path)}")
        canonical = PrefixRegion.from_words(item).words
        if canonical != tuple(item):
            raise ValueError(f"noncanonical or reducible antichain at {'/'.join(path)}")


def _validate_family_pairing(data: Mapping[str, object]) -> None:
    family = data["regional_families"]
    if not isinstance(family, Mapping):
        raise ValueError("regional family section must be a mapping")
    members_raw = family["members"]
    pairs_raw = family["matched_pairs"]
    registration = family["registration"]
    if not isinstance(members_raw, list) or not isinstance(pairs_raw, list):
        raise ValueError("regional family members and pairs must be lists")
    if not isinstance(registration, Mapping):
        raise ValueError("regional family registration must be a mapping")
    members = {member["id"]: member for member in members_raw if isinstance(member, Mapping)}
    if len(members) != len(members_raw):
        raise ValueError("regional family member schema mismatch")
    for pair in pairs_raw:
        if not isinstance(pair, Mapping):
            raise ValueError("regional family pair schema mismatch")
        member_ids = pair["member_ids"]
        if not isinstance(member_ids, list) or len(member_ids) != 2:
            raise ValueError("regional family pair needs two members")
        left = members[member_ids[0]]
        right = members[member_ids[1]]
        for field in (
            "blind_interface",
            "resource_declaration",
            "component_occurrences",
            "blind_projection",
        ):
            if left[field] != right[field]:
                raise ValueError(f"matched regional family field differs: {field}")
        left_regions = left["regions"]
        right_regions = right["regions"]
        if not isinstance(left_regions, list) or not isinstance(right_regions, list):
            raise ValueError("matched regional regions must be lists")
        left_profiles = {
            row["node_token"]: sorted(len(word) for word in row["antichain"])
            for row in left_regions
        }
        right_profiles = {
            row["node_token"]: sorted(len(word) for word in row["antichain"])
            for row in right_regions
        }
        if left_profiles != right_profiles:
            raise ValueError("matched regional incidence resources differ")
        left_incidences = left["incidences"]
        right_incidences = right["incidences"]
        if not isinstance(left_incidences, list) or not isinstance(right_incidences, list):
            raise ValueError("matched regional incidences must be lists")
        left_arity = [
            (len(row["left_component_tokens"]), len(row["right_component_tokens"]))
            for row in left_incidences
        ]
        right_arity = [
            (len(row["left_component_tokens"]), len(row["right_component_tokens"]))
            for row in right_incidences
        ]
        if left_arity != right_arity:
            raise ValueError("matched regional incidence arities differ")
    training = registration["training_ids"]
    held_out = registration["held_out_ids"]
    if not isinstance(training, list) or not isinstance(held_out, list):
        raise ValueError("regional family registration rows must be lists")
    if set(training).intersection(held_out):
        raise ValueError("regional family registrations overlap")
    if set(training).union(held_out) != set(members):
        raise ValueError("regional family registrations do not cover the members")


def _validate_typed_fillings(data: Mapping[str, object]) -> None:
    section = data["typed_fillings"]
    if not isinstance(section, Mapping):
        raise ValueError("typed filling section must be a mapping")
    boundary_rows = section["boundaries"]
    apex_rows = section["apices"]
    filling_rows = section["horizontal_fillings"]
    if not isinstance(boundary_rows, list) or not isinstance(apex_rows, list):
        raise ValueError("typed boundaries and apices must be lists")
    if not isinstance(filling_rows, list):
        raise ValueError("horizontal fillings must be a list")

    boundaries = {
        row["id"]: BoundaryType(row["id"], tuple(row["generators"]))
        for row in boundary_rows
    }
    apices = {
        row["id"]: RegionType(row["id"], tuple(row["generators"]))
        for row in apex_rows
    }
    fillings: dict[str, StructuredCospan] = {}
    filling_rows_by_id: dict[str, Mapping[str, object]] = {}
    for row in filling_rows:
        incoming = boundaries[row["incoming_boundary_id"]]
        outgoing = boundaries[row["outgoing_boundary_id"]]
        apex = apices[row["apex_id"]]
        value = StructuredCospan(
            row["id"],
            incoming,
            apex,
            outgoing,
            BoundaryLeg(incoming, apex, tuple(tuple(pair) for pair in row["incoming_images"])),
            BoundaryLeg(outgoing, apex, tuple(tuple(pair) for pair in row["outgoing_images"])),
        )
        if validate_cospan(value).issues:
            raise ValueError(f"typed filling {row['id']} has incompatible legs")
        for relation in row.get("apex_relations", []):
            if (
                not isinstance(relation, list)
                or len(relation) != 2
                or relation[0] not in apex.generators
                or relation[1] not in apex.generators
            ):
                raise ValueError(f"typed filling {row['id']} has an ill-typed apex relation")
        fillings[row["id"]] = value
        filling_rows_by_id[row["id"]] = row

    factorizations = section["factorizations"]
    if not isinstance(factorizations, list):
        raise ValueError("factorizations must be a list")
    for row in factorizations:
        whole = fillings[row["whole_filling_id"]]
        steps = [fillings[identifier] for identifier in row["step_ids"]]
        cuts = row["intermediate_boundary_ids"]
        if not steps or len(cuts) != len(steps) - 1:
            raise ValueError(f"factorization {row['id']} has a bad cut count")
        if steps[0].incoming != whole.incoming or steps[-1].outgoing != whole.outgoing:
            raise ValueError(f"factorization {row['id']} has incompatible endpoints")
        for index, cut_id in enumerate(cuts):
            cut = boundaries[cut_id]
            if steps[index].outgoing != cut or steps[index + 1].incoming != cut:
                raise ValueError(f"factorization {row['id']} has an incompatible cut")
        whole_row = filling_rows_by_id[row["whole_filling_id"]]
        whole_nodes = set(apices[whole_row["apex_id"]].generators)
        whole_relations = {tuple(pair) for pair in whole_row.get("apex_relations", [])}
        step_nodes: set[str] = set()
        step_relations: set[tuple[str, str]] = set()
        for identifier in row["step_ids"]:
            step_row = filling_rows_by_id[identifier]
            step_nodes.update(apices[step_row["apex_id"]].generators)
            step_relations.update(tuple(pair) for pair in step_row.get("apex_relations", []))
        if step_nodes != whole_nodes or step_relations != whole_relations:
            raise ValueError(f"factorization {row['id']} does not reproduce its canonical tree")

    process_section = data["regional_question_process"]
    if not isinstance(process_section, Mapping):
        raise ValueError("regional question process must be a mapping")
    provenance = process_section["generated_law_provenance"]
    if not isinstance(provenance, Mapping):
        raise ValueError("generated law provenance must be a mapping")
    factory = provenance["filling_factory"]
    if not isinstance(factory, Mapping):
        raise ValueError("generated filling factory must be a mapping")
    question_filling_ids = {
        row["filling_id"] for row in factory["question_rows"]
    }.union(
        row["filling_id"]
        for row in factory["tree_rows"]
        if row["tree_id"] != "qw_000"
    )
    for identifier in question_filling_ids:
        images = filling_rows_by_id[identifier]["outgoing_images"]
        if len({pair[1] for pair in images}) != len(images):
            raise ValueError(f"question filling {identifier} collapses distinct record ports")

    vertical_rows = section["vertical_maps"]
    if not isinstance(vertical_rows, list):
        raise ValueError("vertical maps must be a list")
    for row in vertical_rows:
        source = boundaries[row["source_boundary_id"]]
        target = boundaries[row["target_boundary_id"]]
        images = row["images"]
        if {pair[0] for pair in images} != set(source.generators):
            raise ValueError(f"vertical map {row['id']} is not total")
        if any(pair[1] not in target.generators for pair in images):
            raise ValueError(f"vertical map {row['id']} has an unknown target")
        if row["map_sort"] == "passive_presentation_isomorphism":
            if len({pair[1] for pair in images}) != len(target.generators):
                raise ValueError(f"vertical map {row['id']} is not bijective")


def validate_schema(data: Mapping[str, object]) -> dict[str, int]:
    if data.get("schema") != SCHEMA:
        raise ValueError("fixture schema mismatch")
    for path, item in _walk(data):
        if isinstance(item, bool):
            raise ValueError(f"fixture booleans are forbidden at {'/'.join(path)}")
        if path:
            lowered = path[-1].lower()
            if any(part in lowered for part in _FORBIDDEN_KEY_PARTS):
                raise ValueError(f"computed-result key is forbidden at {'/'.join(path)}")

    declared = _declared_ids(data)
    _validate_references(data, declared)
    _validate_matrix_records(data)
    _validate_antichains(data)
    _validate_family_pairing(data)
    _validate_typed_fillings(data)

    encoded = canonical_json(data)
    decoded = json.loads(encoded)
    if canonical_json(decoded) != encoded:
        raise ValueError("canonical serialization is not idempotent")
    return {
        "declared_id_count": len(declared),
        "section_count": len(data) - 1,
    }


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate and hash the APR primitive fixture declarations",
        allow_abbrev=False,
    )
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args(argv)
    if not args.validate:
        parser.error("the only executable mode is --validate")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    parse_args(sys.argv[1:] if argv is None else argv)
    try:
        counts = validate_schema(FIXTURE_DATA)
    except (KeyError, TypeError, ValueError) as exc:
        print(f"APR-FIXTURE-SCHEMA-REFUSED {exc}", file=sys.stderr)
        return 1
    payload = {
        "schema": "apr-fixture-hash-v1",
        "fixture_schema": SCHEMA,
        "declared_id_count": counts["declared_id_count"],
        "section_count": counts["section_count"],
        "fixture_sha256": canonical_sha256(FIXTURE_DATA),
    }
    sys.stdout.write(canonical_json(payload) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
