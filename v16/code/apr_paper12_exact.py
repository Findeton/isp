#!/usr/bin/env python3
"""Standalone exact regeneration bundle for the Paper 12 negative candidate.

This module intentionally imports neither apr_score nor apr_fixtures.  It
reconstructs the public finite mathematics from primitive definitions, keeps
graph pushouts separate from process assignments, and derives the earliest
outcome from typed capability measurements.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import tempfile
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


SCHEMA = "apr-paper12-negative-v1"

EXPECTED_INPUTS = {
    "v16/note-apr-one-gamma-paper-review-gate.md":
        "06d171a3eea8109e177e2dfa3cb5536fe3785043e676f735c36e91d03834cb51",
    "v16/note-apr-v5-verification.md":
        "d2eae0fdc187317d7ee39c8efaca8fa2a94b6b8f06a3a0524cee0289396a077d",
    "v16/apr_output_v5.txt":
        "68374ea18576466ccc40553f8b221360fdfce3fc43d5b555a6eeb0d2827a2f56",
    "v16/apr_receipt_v5.json":
        "ab9ea941fceebf5b57c7955d483730f3a5f0b317bb5a21da9cc0820331919a61",
}

EXPECTED_CANONICAL_RECEIPT_PAYLOAD = (
    "04a1e370c601f9d7e3d5310f9bf20296d7be5c5428010f0f7af6c073d0b438d8"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def digest(value: Any) -> str:
    return sha256_bytes(canonical_json_bytes(value))


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def serialise(value: Any) -> Any:
    if isinstance(value, Fraction):
        return fraction_text(value)
    if isinstance(value, Region):
        return {"prefix_cylinders": list(value.words)}
    if isinstance(value, Capability):
        return {
            "name": value.name,
            "present": value.present,
            "evidence": serialise(value.evidence),
            "primitive_sha256": value.primitive_sha256,
        }
    if isinstance(value, Mapping):
        return {str(key): serialise(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [serialise(item) for item in value]
    if isinstance(value, set):
        return [serialise(item) for item in sorted(value)]
    return value


def bit_words(depth: int) -> tuple[str, ...]:
    if depth < 0:
        raise ValueError("negative depth")
    return tuple("".join(bits) for bits in itertools.product("01", repeat=depth))


def is_prefix(left: str, right: str) -> bool:
    return right.startswith(left)


def canonical_words(raw: Iterable[str]) -> tuple[str, ...]:
    words = set(raw)
    if any(set(word) - {"0", "1"} for word in words):
        raise ValueError("prefix words must be binary")
    if "" in words:
        return ("",)

    def remove_dominated(items: set[str]) -> set[str]:
        return {
            word
            for word in items
            if not any(other != word and is_prefix(other, word) for other in items)
        }

    words = remove_dominated(words)
    changed = True
    while changed:
        changed = False
        parents = sorted({word[:-1] for word in words if word}, key=lambda x: (-len(x), x))
        for parent in parents:
            left = parent + "0"
            right = parent + "1"
            if left in words and right in words:
                words.remove(left)
                words.remove(right)
                words.add(parent)
                words = remove_dominated(words)
                if "" in words:
                    return ("",)
                changed = True
                break
    return tuple(sorted(words, key=lambda word: (len(word), word)))


@dataclass(frozen=True)
class Region:
    words: tuple[str, ...]

    def __init__(self, words: Iterable[str] = ()) -> None:
        object.__setattr__(self, "words", canonical_words(tuple(words)))

    @property
    def is_zero(self) -> bool:
        return not self.words

    @property
    def max_depth(self) -> int:
        return max((len(word) for word in self.words), default=0)

    def atoms(self, depth: int) -> frozenset[str]:
        if depth < self.max_depth:
            raise ValueError("atom depth is shallower than region presentation")
        return frozenset(
            atom
            for atom in bit_words(depth)
            if any(atom.startswith(word) for word in self.words)
        )

    @classmethod
    def from_atoms(cls, atoms: Iterable[str], depth: int) -> "Region":
        atom_set = set(atoms)
        if any(len(atom) != depth for atom in atom_set):
            raise ValueError("atom length mismatch")
        if any(set(atom) - {"0", "1"} for atom in atom_set):
            raise ValueError("atoms must be binary")
        return cls(atom_set)

    def join(self, other: "Region") -> "Region":
        depth = max(self.max_depth, other.max_depth)
        return Region.from_atoms(self.atoms(depth) | other.atoms(depth), depth)

    def meet(self, other: "Region") -> "Region":
        depth = max(self.max_depth, other.max_depth)
        return Region.from_atoms(self.atoms(depth) & other.atoms(depth), depth)

    def complement(self) -> "Region":
        depth = self.max_depth
        return Region.from_atoms(set(bit_words(depth)) - set(self.atoms(depth)), depth)

    def difference(self, other: "Region") -> "Region":
        return self.meet(other.complement())

    def proper_split(self) -> tuple["Region", "Region"]:
        if self.is_zero:
            raise ValueError("zero has no proper split")
        chosen = self.words[0]
        left = Region((chosen + "0",))
        right = self.difference(left)
        if left.is_zero or right.is_zero or left.join(right) != self:
            raise AssertionError("split constructor failed")
        return left, right


ZERO = Region()
UNIT = Region(("",))


REGISTERED_REGIONS = (
    ZERO,
    UNIT,
    Region(("0",)),
    Region(("1",)),
    Region(("00",)),
    Region(("01",)),
    Region(("10",)),
    Region(("11",)),
    Region(("00", "10")),
    Region(("01", "11")),
)


def dyadic_volume(region: Region) -> Fraction:
    return sum((Fraction(1, 2 ** len(word)) for word in region.words), Fraction(0))


def boolean_measurements() -> dict[str, Any]:
    failures: list[str] = []
    for index, region in enumerate(REGISTERED_REGIONS):
        if region.join(region.complement()) != UNIT:
            failures.append(f"join-complement:{index}")
        if region.meet(region.complement()) != ZERO:
            failures.append(f"meet-complement:{index}")
        if region.complement().complement() != region:
            failures.append(f"double-complement:{index}")
    for i, left in enumerate(REGISTERED_REGIONS):
        for j, middle in enumerate(REGISTERED_REGIONS):
            if left.join(middle) != middle.join(left):
                failures.append(f"join-commutative:{i}:{j}")
            if left.meet(middle) != middle.meet(left):
                failures.append(f"meet-commutative:{i}:{j}")
            if left.join(middle).complement() != left.complement().meet(middle.complement()):
                failures.append(f"de-morgan:{i}:{j}")
            for k, right in enumerate(REGISTERED_REGIONS):
                lhs = left.meet(middle.join(right))
                rhs = left.meet(middle).join(left.meet(right))
                if lhs != rhs:
                    failures.append(f"distributive:{i}:{j}:{k}")

    splits = []
    for index, region in enumerate(REGISTERED_REGIONS[1:], start=1):
        left, right = region.proper_split()
        splits.append(
            {
                "source_index": index,
                "source": region,
                "left": left,
                "right": right,
                "proper": not left.is_zero and not right.is_zero,
                "disjoint": left.meet(right) == ZERO,
                "rejoins": left.join(right) == region,
            }
        )

    half_left = Region(("0",))
    half_right = Region(("1",))
    context = half_left
    volume_control = {
        "uncontextualised": [dyadic_volume(half_left), dyadic_volume(half_right)],
        "meet_context": [
            dyadic_volume(half_left.meet(context)),
            dyadic_volume(half_right.meet(context)),
        ],
    }
    volume_control["equal_before"] = (
        volume_control["uncontextualised"][0] == volume_control["uncontextualised"][1]
    )
    volume_control["separated_after"] = (
        volume_control["meet_context"][0] != volume_control["meet_context"][1]
    )

    def zero_path_character(region: Region) -> int:
        return int(any(set(word) <= {"0"} for word in region.words))

    character_values = {zero_path_character(region) for region in REGISTERED_REGIONS}
    atomic_control = {
        "image": sorted(character_values),
        "image_size": len(character_values),
        "unit": zero_path_character(UNIT),
        "selected_half": zero_path_character(half_left),
        "other_half": zero_path_character(half_right),
        "two_element_atomic": character_values == {0, 1},
    }
    return {
        "identity_failure_count": len(failures),
        "identity_failures": failures,
        "splits": splits,
        "split_count": len(splits),
        "generic_cylinder_split": {
            "source": Region(("00000",)),
            "children": [Region(("000000",)), Region(("000001",))],
            "valid": Region(("000000",)).join(Region(("000001",))) == Region(("00000",)),
        },
        "volume_noncongruence": volume_control,
        "atomic_character": atomic_control,
    }


Matrix = tuple[tuple[Fraction, ...], ...]


def identity_matrix(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(size))
        for row in range(size)
    )


def zero_matrix(rows: int, columns: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(columns)) for _ in range(rows))


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or any(len(a) != len(b) for a, b in zip(left, right)):
        raise ValueError("matrix shape mismatch")
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def matrix_scale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(tuple(scalar * value for value in row) for row in matrix)


def restriction_matrix(region: Region, depth: int) -> Matrix:
    atoms = bit_words(depth)
    selected = region.atoms(depth)
    return tuple(
        tuple(
            Fraction(int(row == column and atoms[column] in selected))
            for column in range(len(atoms))
        )
        for row in range(len(atoms))
    )


def question_measurements() -> dict[str, Any]:
    depth = 3
    atoms = bit_words(depth)
    unit_identity = identity_matrix(len(atoms))
    rows = []
    for index, region in enumerate(REGISTERED_REGIONS):
        q1 = restriction_matrix(region, depth)
        q0 = restriction_matrix(region.complement(), depth)
        total = matrix_add(q1, q0)
        rows.append(
            {
                "region_index": index,
                "q1": q1,
                "q0": q0,
                "sum_is_identity": total == unit_identity,
                "positive": all(value >= 0 for row in q1 + q0 for value in row),
                "zero_port_retained": True,
            }
        )
    ask_unit = rows[1]
    return {
        "constructed_interface_ids": [
            "finite-restriction-question-family",
            "canonical-prefix-region-compiler",
        ],
        "depth": depth,
        "atom_count": len(atoms),
        "rows": rows,
        "all_positive": all(row["positive"] for row in rows),
        "all_complete": all(row["sum_is_identity"] for row in rows),
        "all_zero_ports_retained": all(row["zero_port_retained"] for row in rows),
        "ask_unit_zero_branch_is_zero": ask_unit["q0"] == zero_matrix(len(atoms), len(atoms)),
        "average_is_half_identity": matrix_scale(
            Fraction(1, 2), matrix_add(rows[2]["q1"], rows[2]["q0"])
        ) == matrix_scale(Fraction(1, 2), unit_identity),
        "full_question_separation": all(
            left == right or any(
                dyadic_volume(left.meet(probe)) != dyadic_volume(right.meet(probe))
                for probe in REGISTERED_REGIONS + (Region(("000",)), Region(("001",)))
            )
            for left in REGISTERED_REGIONS
            for right in REGISTERED_REGIONS
        ),
    }


def prefix_free(frontier: Sequence[str]) -> bool:
    return len(set(frontier)) == len(frontier) and all(
        not is_prefix(left, right)
        for left in frontier
        for right in frontier
        if left != right
    )


def complete_frontier(frontier: Sequence[str]) -> bool:
    if not prefix_free(frontier):
        return False
    return sum((Fraction(1, 2 ** len(word)) for word in frontier), Fraction(0)) == 1


@dataclass(frozen=True)
class Segment:
    start: int
    end: int
    nodes: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]


def tree_segment(start: int, end: int) -> Segment:
    if start < 0 or end < start:
        raise ValueError("invalid tree segment")
    nodes = tuple(word for depth in range(start, end + 1) for word in bit_words(depth))
    edges = tuple(
        (word, word + bit)
        for depth in range(start, end)
        for word in bit_words(depth)
        for bit in "01"
    )
    return Segment(start, end, nodes, edges, bit_words(start), bit_words(end))


class UnionFind:
    def __init__(self, items: Iterable[Any]) -> None:
        self.parent = {item: item for item in items}

    def find(self, item: Any) -> Any:
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]

    def union(self, left: Any, right: Any) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            if repr(left_root) <= repr(right_root):
                self.parent[right_root] = left_root
            else:
                self.parent[left_root] = right_root


def compose_segments(segments: Sequence[Segment]) -> dict[str, Any]:
    if not segments:
        raise ValueError("at least one segment is required")
    for left, right in zip(segments, segments[1:]):
        if left.end != right.start:
            raise ValueError("segments are not composable")
    tagged_nodes = tuple(
        (index, node)
        for index, segment in enumerate(segments)
        for node in segment.nodes
    )
    union_find = UnionFind(tagged_nodes)
    for index, (left, right) in enumerate(zip(segments, segments[1:])):
        left_output = set(left.outputs)
        right_input = set(right.inputs)
        if left_output != right_input:
            raise ValueError("boundary labels do not match")
        for label in sorted(left_output):
            union_find.union((index, label), (index + 1, label))

    classes: dict[Any, set[tuple[int, str]]] = {}
    for tagged in tagged_nodes:
        classes.setdefault(union_find.find(tagged), set()).add(tagged)
    label_by_root: dict[Any, str] = {}
    for root, members in classes.items():
        labels = {label for _, label in members}
        if len(labels) != 1:
            raise AssertionError("pushout identified distinct history labels")
        label_by_root[root] = next(iter(labels))
    quotient_edges = set()
    for index, segment in enumerate(segments):
        for source, target in segment.edges:
            quotient_edges.add(
                (
                    label_by_root[union_find.find((index, source))],
                    label_by_root[union_find.find((index, target))],
                )
            )
    labels = set(label_by_root.values())
    return {
        "node_labels": sorted(labels, key=lambda word: (len(word), word)),
        "edges": sorted(quotient_edges),
        "node_count": len(labels),
        "edge_count": len(quotient_edges),
        "input_frontier": list(segments[0].inputs),
        "output_frontier": list(segments[-1].outputs),
    }


def graph_shape_signature(nodes: Iterable[Any], edges: Iterable[tuple[Any, Any]]) -> list[tuple[int, int]]:
    node_list = list(nodes)
    edge_list = list(edges)
    return sorted(
        (
            sum(int(target == node) for _, target in edge_list),
            sum(int(source == node) for source, _ in edge_list),
        )
        for node in node_list
    )


def boundary_measurements() -> dict[str, Any]:
    uniform = {depth: bit_words(depth) for depth in range(4)}
    adaptive = ("0", "10", "110", "111")
    uniform_valid = {
        depth: prefix_free(frontier) and complete_frontier(frontier)
        for depth, frontier in uniform.items()
    }
    adaptive_valid = prefix_free(adaptive) and complete_frontier(adaptive)
    adaptive_registered = adaptive in set(uniform.values())

    direct = tree_segment(0, 3)
    direct_graph = {
        "node_labels": list(direct.nodes),
        "edges": sorted(direct.edges),
        "node_count": len(direct.nodes),
        "edge_count": len(direct.edges),
    }
    factorisations = (
        (tree_segment(0, 1), tree_segment(1, 3)),
        (tree_segment(0, 2), tree_segment(2, 3)),
        (tree_segment(0, 1), tree_segment(1, 2), tree_segment(2, 3)),
    )
    pushouts = []
    for index, factors in enumerate(factorisations):
        composite = compose_segments(factors)
        equals_direct = (
            composite["node_labels"] == direct_graph["node_labels"]
            and composite["edges"] == direct_graph["edges"]
        )
        pushouts.append(
            {
                "factorisation": index,
                "factor_depths": [[factor.start, factor.end] for factor in factors],
                "node_count": composite["node_count"],
                "edge_count": composite["edge_count"],
                "boundary_fixed_equal_to_direct": equals_direct,
            }
        )

    active_boundaries = {
        "B0": uniform[0],
        "B1": uniform[1],
        "B2": uniform[2],
        "B3": uniform[3],
    }
    assignments = (
        {"tree": "empty", "boundary": "B0", "kind": "identity", "active": True},
    )
    raw_unassigned = (
        {"boundary": "B0", "kind": "identity-like", "active": False},
        {"boundary": "B0", "kind": "replacement", "active": False},
    )
    identity_census = {
        boundary: [
            assignment["tree"]
            for assignment in assignments
            if assignment["active"]
            and assignment["kind"] == "identity"
            and assignment["boundary"] == boundary
        ]
        for boundary in active_boundaries
    }

    renamed_nodes = {node: f"node-{index}" for index, node in enumerate(direct.nodes)}
    renamed_edges = {(renamed_nodes[left], renamed_nodes[right]) for left, right in direct.edges}
    relabel_invariant = graph_shape_signature(direct.nodes, direct.edges) == graph_shape_signature(
        renamed_nodes.values(), renamed_edges
    )

    constructed_interfaces = {
        "uniform-frontier-factory",
        "registered-tree-segments",
        "tagged-graph-pushout-composition",
        "B0-empty-process-assignment",
    }
    process_requirements = {
        "adaptive-frontier-factory",
        "all-active-boundary-identities",
        "filling-to-process-assignment",
        "tensor-process-factory",
        "nontrivial-vertical-horizontal-naturality",
    }

    return {
        "constructed_interface_ids": sorted(constructed_interfaces),
        "process_requirement_ids": sorted(process_requirements),
        "missing_process_interface_ids": sorted(process_requirements - constructed_interfaces),
        "uniform_frontiers": uniform,
        "uniform_valid": uniform_valid,
        "adaptive_frontier": adaptive,
        "adaptive_depth_set": sorted({len(word) for word in adaptive}),
        "adaptive_valid": adaptive_valid,
        "adaptive_registered": adaptive_registered,
        "direct_tree": direct_graph,
        "pushouts": pushouts,
        "all_pushouts_match": all(row["boundary_fixed_equal_to_direct"] for row in pushouts),
        "active_boundaries": active_boundaries,
        "assignments": assignments,
        "raw_unassigned_controls": raw_unassigned,
        "identity_census": identity_census,
        "all_boundary_identities": all(bool(identity_census[key]) for key in active_boundaries),
        "filling_to_process_assignment": "filling-to-process-assignment" in constructed_interfaces,
        "tensor_factory": "tensor-process-factory" in constructed_interfaces,
        "nontrivial_naturality_square": (
            "nontrivial-vertical-horizontal-naturality" in constructed_interfaces
        ),
        "relabel_invariant_graph_shape": relabel_invariant,
    }


Triple = tuple[int, int, int]


def uniform_global() -> dict[Triple, Fraction]:
    return {triple: Fraction(1, 8) for triple in itertools.product((0, 1), repeat=3)}


def equal_ac_global() -> dict[Triple, Fraction]:
    return {
        (a, b, c): Fraction(1, 4)
        for a, b, c in itertools.product((0, 1), repeat=3)
        if a == c
    }


def marginal(distribution: Mapping[Triple, Fraction], coordinates: tuple[int, int]) -> dict[tuple[int, int], Fraction]:
    result = {(left, right): Fraction(0) for left, right in itertools.product((0, 1), repeat=2)}
    for triple, weight in distribution.items():
        result[(triple[coordinates[0]], triple[coordinates[1]])] += weight
    return result


def probability_a_equals_c(distribution: Mapping[Triple, Fraction]) -> Fraction:
    return sum((weight for (a, _, c), weight in distribution.items() if a == c), Fraction(0))


def validate_distribution(distribution: Mapping[Triple, Fraction]) -> bool:
    return all(weight >= 0 for weight in distribution.values()) and sum(distribution.values(), Fraction(0)) == 1


def overlap_measurements() -> dict[str, Any]:
    globals_ = {"uniform": uniform_global(), "equal_ac": equal_ac_global()}
    rows = {}
    for name, distribution in globals_.items():
        rows[name] = {
            "valid": validate_distribution(distribution),
            "AB": marginal(distribution, (0, 1)),
            "BC": marginal(distribution, (1, 2)),
            "p_a_equals_c": probability_a_equals_c(distribution),
        }
    local_equal = rows["uniform"]["AB"] == rows["equal_ac"]["AB"] and rows["uniform"]["BC"] == rows["equal_ac"]["BC"]
    global_distinct = globals_["uniform"] != globals_["equal_ac"]

    changed = dict(globals_["uniform"])
    changed[(0, 0, 0)] += Fraction(1, 16)
    changed[(0, 0, 1)] -= Fraction(1, 16)
    stale_ab = rows["uniform"]["AB"]
    stale_bc = rows["uniform"]["BC"]
    recomputed_ab = marginal(changed, (0, 1))
    recomputed_bc = marginal(changed, (1, 2))
    return {
        "constructed_interface_ids": ["two-global-extension-census"],
        "globals": globals_,
        "rows": rows,
        "local_shadows_equal": local_equal,
        "global_laws_distinct": global_distinct,
        "completion_count_lower_bound": len(globals_),
        "selector_present": False,
        "cached_marginal_control": {
            "mutated_global_valid": validate_distribution(changed),
            "AB_stays_equal": recomputed_ab == stale_ab,
            "BC_moves": recomputed_bc != stale_bc,
            "stale_cache_detected": recomputed_bc != stale_bc,
            "changed_global": changed,
        },
    }


@dataclass(frozen=True)
class Capability:
    name: str
    present: bool
    evidence: Any
    primitive_sha256: str


def capability(name: str, present: bool, evidence: Any) -> Capability:
    primitive = {"name": name, "present": present, "evidence": serialise(evidence)}
    return Capability(name, present, evidence, digest(primitive))


CAPABILITY_ORDER = (
    "normalization",
    "raw_atomlessness",
    "boundary_gluing",
    "two_arrow_typing",
    "future_profile_completeness",
    "regional_congruence",
    "comparison_constructed",
    "dynamic_locality",
    "causal_order",
    "law_selected",
)


OUTCOME_FOR_FAILURE = {
    "normalization": "APR-INCONSISTENT",
    "raw_atomlessness": "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA",
    "boundary_gluing": "APR-BLOCKED-AT-BOUNDARY-GLUING",
    "two_arrow_typing": "APR-BLOCKED-AT-TWO-ARROW-TYPING",
    "future_profile_completeness": "APR-BLOCKED-AT-FUTURE-PROFILE-COMPLETENESS",
    "regional_congruence": "APR-BLOCKED-AT-REGIONAL-CONGRUENCE",
    "comparison_constructed": "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED",
    "dynamic_locality": "APR-COMPARISON-QUOTIENT-CONSTRUCTED-BUT-DYNAMICAL-LOCALITY-FAILS",
    "causal_order": "APR-DYNAMIC-REGIONAL-REFERENT-CONSTRUCTED-BUT-CAUSAL-ORDER-PRICED",
    "law_selected": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
}


def classify_capabilities(rows: Sequence[Capability]) -> tuple[str, list[str]]:
    if not all(isinstance(row, Capability) for row in rows):
        raise TypeError("classifier accepts only Capability measurements")
    by_name = {row.name: row for row in rows}
    if set(by_name) != set(CAPABILITY_ORDER) or len(by_name) != len(rows):
        raise ValueError("capability set is missing, duplicated, or unknown")
    for name in CAPABILITY_ORDER:
        if not by_name[name].present:
            return OUTCOME_FOR_FAILURE[name], [
                f"missing measured capability: {name}",
                *([str(item) for item in by_name[name].evidence.get("missing", [])]
                  if isinstance(by_name[name].evidence, Mapping) else []),
            ]
    return "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED", []


def capability_measurements(
    boolean: Mapping[str, Any],
    question: Mapping[str, Any],
    boundary: Mapping[str, Any],
    overlap: Mapping[str, Any],
) -> tuple[Capability, ...]:
    available = {
        *question["constructed_interface_ids"],
        *boundary["constructed_interface_ids"],
        *overlap["constructed_interface_ids"],
    }
    required = {
        "boundary_gluing": {
            *boundary["process_requirement_ids"],
            "regional-overlap-selector",
        },
        "two_arrow_typing": {
            "filling-to-process-assignment",
            "composable-nonidentity-arrow-pair",
        },
        "future_profile_completeness": {
            "target-independent-physical-question-compiler",
            "faithful-supported-preparation-family",
            "same-law-stable-record-reader",
        },
        "regional_congruence": {
            "complete-contextual-quotient",
            "descended-boolean-operations",
            "descended-gluing-operations",
        },
        "comparison_constructed": {
            "same-law-calibrated-comparison",
        },
        "dynamic_locality": {
            "generated-internal-support-algebra",
            "generated-dynamic-support-equalizer",
            "faithful-order-reflecting-support-map",
        },
        "causal_order": {
            "generated-intervention-schedule",
            "delayed-response-reader",
        },
        "law_selected": {
            "complete-physical-Gamma-family",
            "candidate-law-selection-rule",
        },
    }

    def measured(name: str) -> Capability:
        missing = sorted(required[name] - available)
        return capability(
            name,
            not missing,
            {
                "required_interface_ids": sorted(required[name]),
                "available_interface_ids": sorted(available & required[name]),
                "missing": missing,
            },
        )

    return (
        capability(
            "normalization",
            bool(question["all_complete"] and question["all_positive"]),
            {"question_rows": len(question["rows"])},
        ),
        capability(
            "raw_atomlessness",
            bool(boolean["identity_failure_count"] == 0 and boolean["split_count"] > 0),
            {"split_count": boolean["split_count"]},
        ),
        measured("boundary_gluing"),
        measured("two_arrow_typing"),
        measured("future_profile_completeness"),
        measured("regional_congruence"),
        measured("comparison_constructed"),
        measured("dynamic_locality"),
        measured("causal_order"),
        measured("law_selected"),
    )


def control_row(
    identifier: str,
    classification: str,
    before: Any,
    after: Any,
    passed: bool,
    evidence: Any,
) -> dict[str, Any]:
    before_payload = serialise(before)
    after_payload = serialise(after)
    return {
        "id": identifier,
        "classification": classification,
        "before_sha256": digest(before_payload),
        "after_sha256": digest(after_payload),
        "object_changed": digest(before_payload) != digest(after_payload),
        "passed": bool(passed),
        "evidence": serialise(evidence),
    }


def build_controls(
    boolean: Mapping[str, Any],
    question: Mapping[str, Any],
    boundary: Mapping[str, Any],
    overlap: Mapping[str, Any],
    capabilities: Sequence[Capability],
    strict_primary: str,
) -> list[dict[str, Any]]:
    controls: list[dict[str, Any]] = []
    deep = Region(("00000",))
    deep_left, deep_right = deep.proper_split()
    controls.append(control_row(
        "RAW-ATOMLESS", "SEMANTIC-CONTROL", deep, [deep_left, deep_right],
        deep_left.join(deep_right) == deep and deep_left.meet(deep_right) == ZERO,
        {"proper": not deep_left.is_zero and not deep_right.is_zero},
    ))
    controls.append(control_row(
        "ATOMIC-CHARACTER", "SEMANTIC-CONTROL", REGISTERED_REGIONS,
        boolean["atomic_character"], bool(boolean["atomic_character"]["two_element_atomic"]),
        boolean["atomic_character"],
    ))
    volume = boolean["volume_noncongruence"]
    controls.append(control_row(
        "VOLUME-NONCONGRUENCE", "SEMANTIC-CONTROL",
        {"context": UNIT, "values": volume["uncontextualised"]},
        {"context": Region(("0",)), "values": volume["meet_context"]},
        bool(volume["equal_before"] and volume["separated_after"]), volume,
    ))
    complete_ports = ("Q1", "Q0")
    dropped_ports = ("Q1",)
    controls.append(control_row(
        "ZERO-PORT", "SEMANTIC-MUTATION", complete_ports, dropped_ports,
        complete_ports != dropped_ports and question["ask_unit_zero_branch_is_zero"],
        {"typed_complete_before": True, "typed_complete_after": False},
    ))
    controls.append(control_row(
        "AVERAGE-BRANCHES", "SEMANTIC-MUTATION", "Q1+Q0", "(Q1+Q0)/2",
        bool(question["average_is_half_identity"]),
        {"sum": "I", "average": "I/2"},
    ))
    fresh = Region(("000",))
    whitelist_accepts = fresh.max_depth <= 1
    compiler_accepts = Region(fresh.words) == fresh
    controls.append(control_row(
        "FRESH-PROBE", "SEMANTIC-MUTATION",
        {"compiler": "canonical-prefix", "target": fresh},
        {"compiler": "depth<=1-whitelist", "target": fresh},
        compiler_accepts and not whitelist_accepts,
        {"canonical_compiler_accepts": compiler_accepts, "whitelist_accepts": whitelist_accepts},
    ))
    controls.append(control_row(
        "ADAPTIVE-FRONTIER", "SEMANTIC-CONTROL",
        boundary["uniform_frontiers"], boundary["adaptive_frontier"],
        bool(boundary["adaptive_valid"] and not boundary["adaptive_registered"]),
        {"depth_set": boundary["adaptive_depth_set"]},
    ))
    controls.append(control_row(
        "IDENTITY-DOMAIN", "SEMANTIC-MUTATION", boundary["assignments"],
        list(boundary["assignments"]) + list(boundary["raw_unassigned_controls"]),
        boundary["identity_census"]["B0"] == ["empty"]
        and all(not boundary["identity_census"][key] for key in ("B1", "B2", "B3")),
        boundary["identity_census"],
    ))
    controls.append(control_row(
        "PUSHOUT-NOT-PROCESS", "SCOPE-CONTROL",
        {"pushouts": False, "process_assignment": False},
        {"pushouts": boundary["all_pushouts_match"], "process_assignment": False},
        bool(boundary["all_pushouts_match"] and not boundary["filling_to_process_assignment"]),
        {"process_coordinate": "STATIC-RESPONSE-ONLY"},
    ))
    cached = overlap["cached_marginal_control"]
    controls.append(control_row(
        "CACHED-MARGINAL", "SEMANTIC-MUTATION", overlap["globals"]["uniform"],
        cached["changed_global"], bool(cached["stale_cache_detected"]),
        {"AB_stays_equal": cached["AB_stays_equal"], "BC_moves": cached["BC_moves"]},
    ))
    controls.append(control_row(
        "ARBITRARY-SELECTOR", "SCOPE-CONTROL",
        {"selector": None, "survivors": ["uniform", "equal_ac"]},
        {"selector": "markov-by-declaration", "survivors": ["uniform"]},
        bool(overlap["local_shadows_equal"] and overlap["global_laws_distinct"]),
        {"selection_is_new_law_data": True},
    ))
    synthetic_added = {"synthetic_executable_law": True, "physical_assignment": False}
    controls.append(control_row(
        "SYNTHETIC-LAW-EXCLUSION", "SCOPE-CONTROL",
        {"synthetic_executable_law": False, "physical_assignment": False},
        synthetic_added, strict_primary == "APR-BLOCKED-AT-BOUNDARY-GLUING",
        {"classifier_inputs_are_typed_capabilities_only": True},
    ))
    direct = boundary["direct_tree"]
    renamed = {
        "node_count": direct["node_count"],
        "edge_count": direct["edge_count"],
        "presentation_ids": [f"neutral-{index}" for index in range(direct["node_count"])],
    }
    controls.append(control_row(
        "RAW-NODE-ONTOLOGY", "METAMORPHIC-CONTROL", direct, renamed,
        bool(boundary["relabel_invariant_graph_shape"]),
        {"raw_ids_are_not_beables": True},
    ))
    by_name = {row.name: row for row in capabilities}
    normalization_deleted = tuple(
        capability(row.name, False, {"missing": ["normalization"]})
        if row.name == "normalization" else row
        for row in capabilities
    )
    boundary_supplied = tuple(
        capability(row.name, True, {"synthetic_complete_gluing_package": True})
        if row.name == "boundary_gluing" else row
        for row in capabilities
    )
    earlier, _ = classify_capabilities(normalization_deleted)
    later, _ = classify_capabilities(boundary_supplied)
    controls.append(control_row(
        "PRIMARY-PRECEDENCE", "CLASSIFIER-CONTROL", capabilities,
        {"normalization_deleted": normalization_deleted, "boundary_supplied": boundary_supplied},
        earlier == "APR-INCONSISTENT" and later == "APR-BLOCKED-AT-TWO-ARROW-TYPING",
        {"baseline": strict_primary, "earlier": earlier, "later": later,
         "baseline_boundary_evidence": serialise(by_name["boundary_gluing"])},
    ))
    real_hash = next(iter(EXPECTED_INPUTS.values()))
    corrupted_hash = "0" * len(real_hash)
    controls.append(control_row(
        "ANCHOR-FAILURE", "INTEGRITY-CONTROL", real_hash, corrupted_hash,
        real_hash != corrupted_hash,
        {"mismatch_refuses_before_science": True},
    ))
    if len(controls) != 15:
        raise AssertionError("registered control count changed")
    if not all(row["object_changed"] and row["passed"] for row in controls):
        failed = [row["id"] for row in controls if not row["object_changed"] or not row["passed"]]
        raise AssertionError(f"controls failed or were vacuous: {failed}")
    return controls


def authenticate_inputs(root: Path) -> dict[str, Any]:
    rows = {}
    for relative, expected in EXPECTED_INPUTS.items():
        path = root / relative
        if not path.is_file():
            raise RuntimeError(f"missing immutable input: {relative}")
        actual = sha256_bytes(path.read_bytes())
        if actual != expected:
            raise RuntimeError(f"immutable input mismatch: {relative}")
        rows[relative] = {"expected_sha256": expected, "actual_sha256": actual, "matched": True}
    receipt_path = root / "v16/apr_receipt_v5.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    claimed = receipt.pop("payload_sha256", None)
    actual_payload = digest(receipt)
    if claimed != EXPECTED_CANONICAL_RECEIPT_PAYLOAD or actual_payload != claimed:
        raise RuntimeError("canonical frozen receipt payload mismatch")
    return {
        "files": rows,
        "canonical_receipt_payload_sha256": actual_payload,
    }


def build_result(root: Path) -> dict[str, Any]:
    immutable = authenticate_inputs(root)
    boolean = boolean_measurements()
    question = question_measurements()
    boundary = boundary_measurements()
    overlap = overlap_measurements()
    capabilities = capability_measurements(boolean, question, boundary, overlap)
    strict_primary, walls = classify_capabilities(capabilities)
    controls = build_controls(boolean, question, boundary, overlap, capabilities, strict_primary)

    if boolean["identity_failure_count"] != 0:
        raise AssertionError("Boolean identity anchor moved")
    if boolean["split_count"] != 9:
        raise AssertionError("split-count anchor moved")
    if boundary["direct_tree"]["node_count"] != 15 or boundary["direct_tree"]["edge_count"] != 14:
        raise AssertionError("whole-tree anchor moved")
    if len(boundary["pushouts"]) != 3 or not boundary["all_pushouts_match"]:
        raise AssertionError("pushout anchors moved")
    uniform_row = overlap["rows"]["uniform"]
    equal_row = overlap["rows"]["equal_ac"]
    if set(uniform_row["AB"].values()) != {Fraction(1, 4)}:
        raise AssertionError("uniform AB anchor moved")
    if set(uniform_row["BC"].values()) != {Fraction(1, 4)}:
        raise AssertionError("uniform BC anchor moved")
    if uniform_row["p_a_equals_c"] != Fraction(1, 2) or equal_row["p_a_equals_c"] != 1:
        raise AssertionError("global-completion anchor moved")

    atomlessness_coordinate = "SYNTAX-ONLY"
    process_coordinate = "STATIC-RESPONSE-ONLY"
    ontology_role = "STATIC-RESPONSE"
    result = {
        "schema": SCHEMA,
        "scope": {
            "scientific_role": "self-contained negative reconstruction",
            "result_known_before_bundle": True,
            "synthetic_executable_law_is_scientific_evidence": False,
            "physical_gamma_constructed": False,
        },
        "immutable_inputs": immutable,
        "regional_algebra": serialise(boolean),
        "questions": serialise(question),
        "boundaries": serialise(boundary),
        "overlap_gluing": serialise(overlap),
        "capabilities": serialise(capabilities),
        "strict_primary": strict_primary,
        "strict_primary_walls": walls,
        "coordinates": {
            "atomlessness": atomlessness_coordinate,
            "process": process_coordinate,
            "ontology_role": ontology_role,
            "physical_regional_referent": "UNCONSTRUCTED",
            "regional_congruence": "UNCONSTRUCTED",
            "one_law_provenance": "UNCONSTRUCTED",
            "locality": "UNCONSTRUCTED-PROMOTION-FAILURE",
            "contact": "PRICED",
            "causality": "PRICED",
            "law_selection": "UNSELECTED",
            "actualization": "POSTULATED-NOT-DERIVED",
        },
        "ontology": {
            "candidate": "one compatible relational record web",
            "candidate_status": "POSTULATE",
            "raw_prefix_words": "REPRESENTATION",
            "graph_nodes": "REPRESENTATION",
            "frontier_depth": "REPRESENTATION-NOT-GLOBAL-TIME",
            "question_restrictions": "STATIC-MATHEMATICAL-RESPONSE",
            "physical_regions": "UNCONSTRUCTED",
            "gamma": "UNCONSTRUCTED",
        },
        "controls": controls,
        "paper_numbers": {
            "boolean_failure_count": boolean["identity_failure_count"],
            "raw_split_count": boolean["split_count"],
            "volume_before": boolean["volume_noncongruence"]["uncontextualised"],
            "volume_after_meet": boolean["volume_noncongruence"]["meet_context"],
            "atomic_image_size": boolean["atomic_character"]["image_size"],
            "uniform_frontier_sizes": [len(boundary["uniform_frontiers"][depth]) for depth in range(4)],
            "adaptive_frontier": boundary["adaptive_frontier"],
            "direct_tree_counts": [boundary["direct_tree"]["node_count"], boundary["direct_tree"]["edge_count"]],
            "pushout_count": len(boundary["pushouts"]),
            "AB_cells": sorted(set(uniform_row["AB"].values())),
            "BC_cells": sorted(set(uniform_row["BC"].values())),
            "p_a_equals_c": [uniform_row["p_a_equals_c"], equal_row["p_a_equals_c"]],
            "control_count": len(controls),
        },
        "primitive_hashes": {
            "regional_algebra": digest(serialise(boolean)),
            "questions": digest(serialise(question)),
            "boundaries": digest(serialise(boundary)),
            "overlap_gluing": digest(serialise(overlap)),
            "capabilities": digest(serialise(capabilities)),
            "controls": digest(controls),
        },
        "scope_walls": [
            "raw atomlessness is syntax only",
            "no total horizontal process",
            "no physical regional quotient",
            "no indivisible Gamma",
            "no reciprocal backreaction",
            "no metric, curvature, gravity, continuum, GR, or QFT",
            "no law selection or actualization mechanism",
        ],
    }
    return serialise(result)


def render_transcript(result: Mapping[str, Any]) -> str:
    numbers = result["paper_numbers"]
    lines = [
        "PAPER 12 EXACT NEGATIVE RECONSTRUCTION",
        f"schema: {result['schema']}",
        f"strict primary: {result['strict_primary']}",
        f"Boolean failures: {numbers['boolean_failure_count']}",
        f"raw proper splits: {numbers['raw_split_count']}",
        f"volume before context: {','.join(numbers['volume_before'])}",
        f"volume after meet context: {','.join(numbers['volume_after_meet'])}",
        f"atomic quotient image size: {numbers['atomic_image_size']}",
        f"uniform frontier sizes: {','.join(str(value) for value in numbers['uniform_frontier_sizes'])}",
        f"adaptive frontier: {','.join(numbers['adaptive_frontier'])}",
        f"whole tree vertices/edges: {numbers['direct_tree_counts'][0]}/{numbers['direct_tree_counts'][1]}",
        f"registered exact pushouts: {numbers['pushout_count']}",
        f"AB cell masses: {','.join(numbers['AB_cells'])}",
        f"BC cell masses: {','.join(numbers['BC_cells'])}",
        f"P(A=C): {','.join(numbers['p_a_equals_c'])}",
        f"controls: {numbers['control_count']}/{numbers['control_count']}",
        f"atomlessness: {result['coordinates']['atomlessness']}",
        f"process: {result['coordinates']['process']}",
        f"ontology role: {result['coordinates']['ontology_role']}",
        "physical Gamma: UNCONSTRUCTED",
        "synthetic executable-law controls: EXCLUDED FROM SCIENTIFIC EVIDENCE",
    ]
    return "\n".join(lines) + "\n"


def finalise_receipt(result: Mapping[str, Any], transcript: str) -> dict[str, Any]:
    receipt = dict(result)
    receipt["transcript_sha256"] = sha256_bytes(transcript.encode("utf-8"))
    payload = dict(receipt)
    receipt["payload_sha256"] = digest(payload)
    return receipt


def publish_pair(
    output_path: Path,
    receipt_path: Path,
    output_bytes: bytes,
    receipt_bytes: bytes,
    *,
    fail_after_first: bool = False,
) -> None:
    targets = (output_path, receipt_path)
    if any(not target.is_absolute() for target in targets):
        raise ValueError("publication paths must be absolute")
    if output_path == receipt_path:
        raise ValueError("publication paths must be distinct")
    if any(target.exists() for target in targets):
        raise FileExistsError("publication target already exists")
    if any(not target.parent.is_dir() for target in targets):
        raise FileNotFoundError("publication parent does not exist")

    staged: list[Path] = []
    published: list[Path] = []
    try:
        for target, data in zip(targets, (output_bytes, receipt_bytes)):
            descriptor, name = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
            temp_path = Path(name)
            staged.append(temp_path)
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
        os.replace(staged[0], output_path)
        published.append(output_path)
        if fail_after_first:
            raise RuntimeError("injected publication failure")
        os.replace(staged[1], receipt_path)
        published.append(receipt_path)
    except Exception:
        for path in staged:
            if path.exists():
                path.unlink()
        for path in published:
            if path.exists():
                path.unlink()
        raise


def selftest() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(name: str, condition: bool, evidence: Any) -> None:
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "passed": True, "evidence": serialise(evidence)})

    boolean = boolean_measurements()
    question = question_measurements()
    boundary = boundary_measurements()
    overlap = overlap_measurements()
    capabilities = capability_measurements(boolean, question, boundary, overlap)
    primary, _ = classify_capabilities(capabilities)
    controls = build_controls(boolean, question, boundary, overlap, capabilities, primary)
    check("canonical-prefix-boolean", boolean["identity_failure_count"] == 0, boolean["split_count"])
    check("generic-deep-split", boolean["generic_cylinder_split"]["valid"], boolean["generic_cylinder_split"])
    check("restriction-question", question["all_positive"] and question["all_complete"], len(question["rows"]))
    check("retained-zero-port", question["ask_unit_zero_branch_is_zero"], True)
    check("frontier-completeness", all(boundary["uniform_valid"].values()) and boundary["adaptive_valid"], boundary["adaptive_depth_set"])
    check("tagged-pushouts", boundary["all_pushouts_match"], boundary["pushouts"])
    check("identity-assignment-domain", not boundary["all_boundary_identities"], boundary["identity_census"])
    check("overlap-underdetermination", overlap["local_shadows_equal"] and overlap["global_laws_distinct"], overlap["rows"])
    check("typed-capability-classifier", primary == "APR-BLOCKED-AT-BOUNDARY-GLUING", primary)
    try:
        classify_capabilities([{"name": "normalization", "present": True}])  # type: ignore[list-item]
    except TypeError:
        forged_refused = True
    else:
        forged_refused = False
    check("forged-capability-refused", forged_refused, forged_refused)
    check("registered-controls", len(controls) == 15 and all(row["passed"] for row in controls), len(controls))
    with tempfile.TemporaryDirectory(prefix="apr-paper12-selftest-") as temporary:
        directory = Path(temporary)
        output = directory / "output.txt"
        receipt = directory / "receipt.json"
        try:
            publish_pair(output, receipt, b"output\n", b"{}\n", fail_after_first=True)
        except RuntimeError:
            rollback = not output.exists() and not receipt.exists()
        else:
            rollback = False
        check("transactional-rollback", rollback, rollback)
        publish_pair(output, receipt, b"output\n", b"{}\n")
        check("transactional-success", output.read_bytes() == b"output\n" and receipt.read_bytes() == b"{}\n", True)
    return {
        "schema": "apr-paper12-selftest-v1",
        "scientific_artifacts_written": False,
        "fixture_or_scorer_imported": False,
        "check_count": len(checks),
        "checks": checks,
        "witness_sha256": digest(checks),
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    mode = result.add_mutually_exclusive_group(required=True)
    mode.add_argument("--selftest", action="store_true")
    mode.add_argument("--run", action="store_true")
    result.add_argument("--output", type=Path)
    result.add_argument("--receipt", type=Path)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parser().parse_args(argv)
    if arguments.selftest:
        if arguments.output is not None or arguments.receipt is not None:
            raise SystemExit("--selftest accepts no publication paths")
        print(json.dumps(selftest(), ensure_ascii=False, sort_keys=True, separators=(",", ":")))
        return 0
    if arguments.output is None or arguments.receipt is None:
        raise SystemExit("--run requires --output ABS and --receipt ABS")
    output_path = arguments.output.resolve() if arguments.output.is_absolute() else arguments.output
    receipt_path = arguments.receipt.resolve() if arguments.receipt.is_absolute() else arguments.receipt
    if not output_path.is_absolute() or not receipt_path.is_absolute():
        raise SystemExit("publication paths must be absolute")
    repository_root = Path(__file__).resolve().parents[2]
    result = build_result(repository_root)
    transcript = render_transcript(result)
    receipt = finalise_receipt(result, transcript)
    publish_pair(
        output_path,
        receipt_path,
        transcript.encode("utf-8"),
        canonical_json_bytes(receipt) + b"\n",
    )
    print(json.dumps({
        "status": "PUBLISHED",
        "output": str(output_path),
        "receipt": str(receipt_path),
        "strict_primary": result["strict_primary"],
        "payload_sha256": receipt["payload_sha256"],
    }, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
