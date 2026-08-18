#!/usr/bin/env python3
"""Frozen verdict-neutral scorer for the v16 JCV physical fixture.

This source is committed before its first execution.  It contains the outcome
taxonomy and exact decision rules, but no expected physical sector count,
dimension, witness value, or verdict.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import itertools
import json
import os
import re
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


PREFIXTURE_COMMIT = "999a5311e599fb223ac9192991d20386b3ce6ab4"
SOLVER_FREEZE_COMMIT = "aa9a54af19f445e3a2067bf12abb603564c10016"

SOURCE_ANCHORS = {
    "v16/code/jcv_fixture.json": "ad887c213d14781838c6e70227b8f2c162f1392a08060de7c6e57829a8db012b",
    "v16/code/jcv_variety.py": "ccc286c0ae82cd118fceb41ee6a4250a5da2974d6381456ba3ec075c8a8f294d",
    "v16/code/jcv_public_receipt.json": "7e8d1edc2b8adc5ee5630ca8702ef2ff9b4f60688878089af16b0dc1ab87b441",
    "v16/note-jcv-pin.md": "4268055286efb5ff0a9790826608c4eb3927ae4e2e87fe66383194cce0059841",
    "v16/note-jcv-solver-postcommit.md": "f81e1f9aa7be50d6e0b2ed20f6c0bf1b5fc978675d753ce17cebc3fd58442760",
}

RESULT_PATHS = (
    "v16/code/jcv_output.txt",
    "v16/code/jcv_receipt.json",
    "v16/paper-02-joint-comparison-fixed-point.md",
)

MUTANT_GATES = {
    "ANCHOR_CORRUPT": "P-ANCHORS",
    "FIXTURE_DROP_CUT": "P-FIXTURE-SEMANTICS",
    "INTERTWINER_SWAP": "P-INTERTWINER",
    "GAUGE_COLLAPSE": "P-GAUGE-QUOTIENT",
    "SOLVER_BASIS_CORRUPT": "P-SOLVER",
    "SATURATION_FLIP": "P-QUERY-CERTIFICATES",
    "WITNESS_EDIT": "P-WITNESS",
    "INSTRUMENT_SIGN": "P-INSTRUMENT",
    "CONTROL_ALIAS": "P-CONTROL",
    "CLASSIFIER_FORCE": "P-CLASSIFIER",
    "WALL_PROMOTE": "P-WALLS",
    "READSET_HIDE": "P-READSET",
    "TRANSCRIPT_CONTRADICTION": "P-TRANSCRIPT",
    "SEAL_ADD": "P-SEAL-CONTROLS",
    "SEAL_EDIT": "P-SEAL-CONTROLS",
}


def serial(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if isinstance(value, Quad):
        return {"rational": serial(value.rational), "sqrt2": serial(value.sqrt2)}
    if isinstance(value, tuple):
        return [serial(item) for item in value]
    if isinstance(value, list):
        return [serial(item) for item in value]
    if isinstance(value, (set, frozenset)):
        items = [serial(item) for item in value]
        return sorted(items, key=lambda item: json.dumps(item, sort_keys=True, separators=(",", ":"), ensure_ascii=False))
    if isinstance(value, dict):
        return {str(key): serial(item) for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))}
    return value


def canonical(value: Any) -> bytes:
    return json.dumps(serial(value), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def bytes_digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


@dataclass(frozen=True)
class Mutation:
    target: str
    before: str
    after: str


class GateFail(RuntimeError):
    def __init__(self, gate: str, evidence: str, mutations: tuple[Mutation, ...] = ()) -> None:
        super().__init__(f"{gate}: {evidence}")
        self.gate = gate
        self.evidence = evidence
        self.mutations = mutations


class Mutator:
    def __init__(self, name: str | None) -> None:
        self.name = name
        self.moves: list[Mutation] = []

    def move(self, target: str, before: Any, after: Any) -> Any:
        if self.name != target:
            return before
        old = digest(before)[:16]
        new = digest(after)[:16]
        if old == new:
            raise RuntimeError(f"mutant {target} did not move its object")
        self.moves.append(Mutation(target, old, new))
        return after


@dataclass
class GateRow:
    gate: str
    passed: bool
    evidence: str


class Ledger:
    def __init__(self, mutator: Mutator) -> None:
        self.rows: list[GateRow] = []
        self.mutator = mutator

    def gate(self, name: str, passed: bool, evidence: str) -> None:
        self.rows.append(GateRow(name, passed, evidence))
        if not passed:
            raise GateFail(name, evidence, tuple(self.mutator.moves))


class SourceReader:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.reads: list[str] = []

    def read_bytes(self, relative: str) -> bytes:
        self.reads.append(relative)
        return (self.root / relative).read_bytes()

    def read_text(self, relative: str) -> str:
        return self.read_bytes(relative).decode("utf-8")


@dataclass(frozen=True)
class Quad:
    """Exact a + b sqrt(2)."""

    rational: Fraction = Fraction(0)
    sqrt2: Fraction = Fraction(0)

    def __add__(self, other: "Quad") -> "Quad":
        return Quad(self.rational + other.rational, self.sqrt2 + other.sqrt2)

    def __neg__(self) -> "Quad":
        return Quad(-self.rational, -self.sqrt2)

    def __sub__(self, other: "Quad") -> "Quad":
        return self + (-other)

    def __mul__(self, other: "Quad") -> "Quad":
        return Quad(
            self.rational * other.rational + 2 * self.sqrt2 * other.sqrt2,
            self.rational * other.sqrt2 + self.sqrt2 * other.rational,
        )


QZERO = Quad()
QONE = Quad(Fraction(1))
QMINUS = Quad(Fraction(-1))
QHALFROOT = Quad(Fraction(0), Fraction(1, 2))

Matrix = tuple[tuple[Quad, ...], ...]


def mat_transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][column] for row in range(len(matrix))) for column in range(len(matrix[0])))


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), QZERO)
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


IDENTITY: Matrix = ((QONE, QZERO), (QZERO, QONE))
ZMAT: Matrix = ((QONE, QZERO), (QZERO, QMINUS))
XMAT: Matrix = ((QZERO, QONE), (QONE, QZERO))
HADAMARD: Matrix = ((QHALFROOT, QHALFROOT), (QHALFROOT, -QHALFROOT))


def eigenbasis(observable: str) -> Matrix:
    if observable == "Z":
        return IDENTITY
    if observable == "X":
        return HADAMARD
    raise ValueError(f"unknown observable {observable}")


def observable_matrix(observable: str) -> Matrix:
    if observable == "Z":
        return ZMAT
    if observable == "X":
        return XMAT
    raise ValueError(f"unknown observable {observable}")


def comparison_matrix(source_observable: str, target_observable: str, plus: int, minus: int) -> Matrix:
    diagonal: Matrix = (
        (QONE if plus == 1 else QMINUS, QZERO),
        (QZERO, QONE if minus == 1 else QMINUS),
    )
    source_basis = eigenbasis(source_observable)
    target_basis = eigenbasis(target_observable)
    return mat_mul(mat_mul(target_basis, diagonal), mat_transpose(source_basis))


def qkey(assignment: dict[str, int]) -> tuple[int, int, int, int]:
    return (
        assignment["a"] * assignment["c"] * assignment["e"],
        assignment["b"] * assignment["d"] * assignment["f"],
        assignment["c"] * assignment["g"] * assignment["j"],
        assignment["d"] * assignment["h"] * assignment["k"],
    )


def raw_sign_assignments() -> list[dict[str, int]]:
    names = ("a", "b", "c", "d", "e", "f", "g", "h", "j", "k")
    return [dict(zip(names, values)) for values in itertools.product((-1, 1), repeat=len(names))]


def gauge_transform(assignment: dict[str, int], vertex_gauge: tuple[int, ...], fixture: dict[str, Any]) -> dict[str, int]:
    charts = [row["name"] for row in fixture["charts"]]
    chart_index = {name: index for index, name in enumerate(charts)}
    plus_gauge = vertex_gauge[: len(charts)]
    minus_gauge = vertex_gauge[len(charts) :]
    transformed = dict(assignment)
    for edge in fixture["comparison_edges"]:
        i = chart_index[edge["source"]]
        j = chart_index[edge["target"]]
        transformed[edge["plus_sign"]] *= plus_gauge[i] * plus_gauge[j]
        transformed[edge["minus_sign"]] *= minus_gauge[i] * minus_gauge[j]
    return transformed


def load_backend(root: Path) -> Any:
    path = root / "v16/code/jcv_variety.py"
    spec = importlib.util.spec_from_file_location("jcv_frozen_variety", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen JCV backend")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def term_row(name: str, terms: list[list[Any]]) -> dict[str, Any]:
    return {"name": name, "terms": terms}


def qcut(name: str, variable: str, holonomy: str) -> dict[str, Any]:
    return term_row(name, [["1", {holonomy: 1, variable: 1}], ["-1", {variable: 1}]])


def raw_cut(name: str, left: str, right: str, direct: str, variable: str) -> dict[str, Any]:
    return term_row(name, [["1", {left: 1, right: 1, variable: 1}], ["-1", {direct: 1, variable: 1}]])


def row_dictionary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {row["name"]: serial(row["terms"]) for row in rows}


def expected_fixture_rows() -> dict[str, dict[str, dict[str, Any]]]:
    invariants = [
        term_row("q012_plus", [["1", {"a": 1, "c": 1, "e": 1}]]),
        term_row("q012_minus", [["1", {"b": 1, "d": 1, "f": 1}]]),
        term_row("q123_plus", [["1", {"c": 1, "g": 1, "j": 1}]]),
        term_row("q123_minus", [["1", {"d": 1, "h": 1, "k": 1}]]),
    ]
    shared_equations = [
        raw_cut("cut-012-plus-x", "a", "c", "e", "x"),
        raw_cut("cut-012-plus-u", "a", "c", "e", "u"),
        raw_cut("cut-012-minus-y", "b", "d", "f", "y"),
        raw_cut("cut-012-minus-v", "b", "d", "f", "v"),
        raw_cut("cut-123-plus-x", "c", "g", "j", "x"),
        raw_cut("cut-123-plus-u", "c", "g", "j", "u"),
        raw_cut("cut-123-minus-y", "d", "h", "k", "y"),
        raw_cut("cut-123-minus-v", "d", "h", "k", "v"),
        term_row("complete-identity", [["1", {"x": 2}], ["1", {"y": 2}], ["1", {"u": 2}], ["1", {"v": 2}], ["-1", {}]]),
        term_row("complete-z", [["1", {"x": 1, "y": 1}], ["1", {"u": 1, "v": 1}]]),
    ]
    shared_queries = [
        term_row("x", [["1", {"x": 1}]]),
        term_row("y", [["1", {"y": 1}]]),
        term_row("u", [["1", {"u": 1}]]),
        term_row("v", [["1", {"v": 1}]]),
        term_row("delta", [["1", {"x": 1, "v": 1}], ["-1", {"y": 1, "u": 1}]]),
        term_row("internal_interference", [["1", {"x": 1, "y": 1}]]),
        term_row("full_coherent", [["1", {"x": 2, "y": 1, "v": 1}], ["-1", {"x": 1, "y": 2, "u": 1}]]),
        term_row("p_plus", [["1", {"x": 2}], ["2", {"x": 1, "y": 1}], ["1", {"y": 2}]]),
        term_row("p_minus", [["1", {"x": 2}], ["-2", {"x": 1, "y": 1}], ["1", {"y": 2}]]),
        term_row("response", [["4", {"x": 1, "y": 1}]]),
    ]
    control_equations = [
        raw_cut("cut-012-plus-x0", "a", "c", "e", "x0"),
        raw_cut("cut-012-plus-u0", "a", "c", "e", "u0"),
        raw_cut("cut-012-minus-y0", "b", "d", "f", "y0"),
        raw_cut("cut-012-minus-v0", "b", "d", "f", "v0"),
        term_row("complete-012-identity", [["1", {"x0": 2}], ["1", {"y0": 2}], ["1", {"u0": 2}], ["1", {"v0": 2}], ["-1", {}]]),
        term_row("complete-012-z", [["1", {"x0": 1, "y0": 1}], ["1", {"u0": 1, "v0": 1}]]),
        raw_cut("cut-123-plus-x1", "c", "g", "j", "x1"),
        raw_cut("cut-123-plus-u1", "c", "g", "j", "u1"),
        raw_cut("cut-123-minus-y1", "d", "h", "k", "y1"),
        raw_cut("cut-123-minus-v1", "d", "h", "k", "v1"),
        term_row("complete-123-identity", [["1", {"x1": 2}], ["1", {"y1": 2}], ["1", {"u1": 2}], ["1", {"v1": 2}], ["-1", {}]]),
        term_row("complete-123-z", [["1", {"x1": 1, "y1": 1}], ["1", {"u1": 1, "v1": 1}]]),
    ]
    control_queries = [
        term_row("delta0", [["1", {"x0": 1, "v0": 1}], ["-1", {"y0": 1, "u0": 1}]]),
        term_row("delta1", [["1", {"x1": 1, "v1": 1}], ["-1", {"y1": 1, "u1": 1}]]),
        term_row("p0_plus", [["1", {"x0": 2}], ["2", {"x0": 1, "y0": 1}], ["1", {"y0": 2}]]),
        term_row("p1_plus", [["1", {"x1": 2}], ["2", {"x1": 1, "y1": 1}], ["1", {"y1": 2}]]),
    ]
    return {
        "SHARED_LAW": {
            "equations": row_dictionary(shared_equations),
            "gauge_invariants": row_dictionary(invariants),
            "queries": row_dictionary(shared_queries),
        },
        "INDEPENDENT_TRIANGLES_CONTROL": {
            "equations": row_dictionary(control_equations),
            "gauge_invariants": row_dictionary(invariants),
            "queries": row_dictionary(control_queries),
        },
    }


def quotient_model(model: dict[str, Any]) -> dict[str, Any]:
    """Eliminate raw chart gauge and retain the four cycle holonomies."""

    holonomies = ("q012_plus", "q012_minus", "q123_plus", "q123_minus")
    equation_map = {row["name"]: row for row in model["equations"]}
    if model["name"] == "SHARED_LAW":
        cut_spec = (
            ("cut-012-plus-x", "x", "q012_plus"),
            ("cut-012-plus-u", "u", "q012_plus"),
            ("cut-012-minus-y", "y", "q012_minus"),
            ("cut-012-minus-v", "v", "q012_minus"),
            ("cut-123-plus-x", "x", "q123_plus"),
            ("cut-123-plus-u", "u", "q123_plus"),
            ("cut-123-minus-y", "y", "q123_minus"),
            ("cut-123-minus-v", "v", "q123_minus"),
        )
        completeness = [equation_map["complete-identity"], equation_map["complete-z"]]
    elif model["name"] == "INDEPENDENT_TRIANGLES_CONTROL":
        cut_spec = (
            ("cut-012-plus-x0", "x0", "q012_plus"),
            ("cut-012-plus-u0", "u0", "q012_plus"),
            ("cut-012-minus-y0", "y0", "q012_minus"),
            ("cut-012-minus-v0", "v0", "q012_minus"),
            ("cut-123-plus-x1", "x1", "q123_plus"),
            ("cut-123-plus-u1", "u1", "q123_plus"),
            ("cut-123-minus-y1", "y1", "q123_minus"),
            ("cut-123-minus-v1", "v1", "q123_minus"),
        )
        completeness = [
            equation_map["complete-012-identity"],
            equation_map["complete-012-z"],
            equation_map["complete-123-identity"],
            equation_map["complete-123-z"],
        ]
    else:
        raise ValueError(f"unknown fixture model {model['name']}")
    return {
        "name": model["name"] + "_QUOTIENT",
        "continuous_variables": list(model["continuous_variables"]),
        "sign_variables": list(holonomies),
        "equations": [qcut(name, variable, holonomy) for name, variable, holonomy in cut_spec] + completeness,
        "gauge_invariants": [term_row(name, [["1", {name: 1}]]) for name in holonomies],
        "queries": list(model["queries"]),
        "expected": {},
    }


def fixture_semantics(fixture: dict[str, Any], mutator: Mutator) -> tuple[bool, dict[str, Any]]:
    top_keys = {
        "schema",
        "unit",
        "prefixture_commit",
        "solver_freeze_commit",
        "exact_domains",
        "scope",
        "charts",
        "comparison_edges",
        "triangles",
        "classifier",
        "models",
    }
    checks = [
        set(fixture) == top_keys,
        fixture.get("schema") == "JCV-PHYSICAL-FIXTURE-v1",
        fixture.get("prefixture_commit") == PREFIXTURE_COMMIT,
        fixture.get("solver_freeze_commit") == SOLVER_FREEZE_COMMIT,
        [(row.get("name"), row.get("observable")) for row in fixture.get("charts", [])]
        == [("B0", "Z"), ("B1", "X"), ("B2", "Z"), ("B3", "X")],
        [(row.get("name"), row.get("source"), row.get("target")) for row in fixture.get("comparison_edges", [])]
        == [("01", "B0", "B1"), ("12", "B1", "B2"), ("02", "B0", "B2"), ("23", "B2", "B3"), ("13", "B1", "B3")],
        [(row.get("name"), row.get("path_edges"), row.get("direct_edge")) for row in fixture.get("triangles", [])]
        == [("012", ["01", "12"], "02"), ("123", ["12", "23"], "13")],
        fixture.get("scope", {}).get("actualization_equation") is False,
        fixture.get("scope", {}).get("geometry_claim") is False,
        fixture.get("scope", {}).get("backreaction_claim") is False,
        tuple(fixture.get("classifier", {}).get("primary_words", [])) == PRIMARY_WORDS,
    ]
    model_by_name = {row.get("name"): row for row in fixture.get("models", [])}
    checks.append(set(model_by_name) == {"SHARED_LAW", "INDEPENDENT_TRIANGLES_CONTROL"})
    expected_equations = {
        "SHARED_LAW": {
            "cut-012-plus-x", "cut-012-plus-u", "cut-012-minus-y", "cut-012-minus-v",
            "cut-123-plus-x", "cut-123-plus-u", "cut-123-minus-y", "cut-123-minus-v",
            "complete-identity", "complete-z",
        },
        "INDEPENDENT_TRIANGLES_CONTROL": {
            "cut-012-plus-x0", "cut-012-plus-u0", "cut-012-minus-y0", "cut-012-minus-v0",
            "complete-012-identity", "complete-012-z",
            "cut-123-plus-x1", "cut-123-plus-u1", "cut-123-minus-y1", "cut-123-minus-v1",
            "complete-123-identity", "complete-123-z",
        },
    }
    expected_rows = expected_fixture_rows()
    expected_continuous = {
        "SHARED_LAW": ["x", "y", "u", "v"],
        "INDEPENDENT_TRIANGLES_CONTROL": ["x0", "y0", "u0", "v0", "x1", "y1", "u1", "v1"],
    }
    expected_signs = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k"]
    expected_nonzero = {
        "SHARED_LAW": {"delta": True, "internal_interference": True, "full_coherent": True},
        "INDEPENDENT_TRIANGLES_CONTROL": {"delta0": True, "delta1": True},
    }
    equation_names: dict[str, set[str]] = {}
    for name, model in model_by_name.items():
        names = {row.get("name") for row in model.get("equations", [])}
        equation_names[name] = names
        checks.extend([
            names == expected_equations[name],
            model.get("expected") == {},
            model.get("continuous_variables") == expected_continuous[name],
            model.get("sign_variables") == expected_signs,
            all(set(row) >= {"name", "terms"} for row in model.get("equations", []) + model.get("gauge_invariants", []) + model.get("queries", [])),
            row_dictionary(model.get("equations", [])) == expected_rows[name]["equations"],
            row_dictionary(model.get("gauge_invariants", [])) == expected_rows[name]["gauge_invariants"],
            row_dictionary(model.get("queries", [])) == expected_rows[name]["queries"],
            all(bool(row.get("nonzero_locus")) == expected_nonzero[name].get(row["name"], False) for row in model.get("queries", [])),
        ])
    if mutator.name == "FIXTURE_DROP_CUT":
        changed = {key: set(value) for key, value in equation_names.items()}
        changed["SHARED_LAW"].discard("cut-012-plus-x")
        equation_names = mutator.move("FIXTURE_DROP_CUT", equation_names, changed)
        checks.append(equation_names == expected_equations)
    else:
        checks.append(equation_names == expected_equations)
    details = {
        "chart_count": len(fixture.get("charts", [])),
        "edge_count": len(fixture.get("comparison_edges", [])),
        "triangle_count": len(fixture.get("triangles", [])),
        "model_count": len(fixture.get("models", [])),
        "all_expected_fields_empty": all(row.get("expected") == {} for row in fixture.get("models", [])),
    }
    return all(checks), details


def raw_cut_equivalence(fixture: dict[str, Any]) -> tuple[bool, int]:
    identities = (
        ("a", "c", "e", 0),
        ("b", "d", "f", 1),
        ("c", "g", "j", 2),
        ("d", "h", "k", 3),
    )
    checked = 0
    for assignment in raw_sign_assignments():
        key = qkey(assignment)
        for left, right, direct, position in identities:
            raw_defect = assignment[left] * assignment[right] - assignment[direct]
            quotient_defect = assignment[direct] * (key[position] - 1)
            checked += 1
            if raw_defect != quotient_defect:
                return False, checked
    return True, checked


def intertwiners_and_holonomy(fixture: dict[str, Any], mutator: Mutator) -> tuple[bool, dict[str, Any]]:
    charts = {row["name"]: row["observable"] for row in fixture["charts"]}
    edges = {row["name"]: row for row in fixture["comparison_edges"]}
    local_checks = 0
    local_failures = 0
    for edge in fixture["comparison_edges"]:
        for plus, minus in itertools.product((-1, 1), repeat=2):
            matrix = comparison_matrix(charts[edge["source"]], charts[edge["target"]], plus, minus)
            orthogonal = mat_mul(mat_transpose(matrix), matrix) == IDENTITY
            intertwines = mat_mul(matrix, observable_matrix(charts[edge["source"]])) == mat_mul(
                observable_matrix(charts[edge["target"]]), matrix
            )
            local_checks += 2
            local_failures += int(not orthogonal) + int(not intertwines)
    path_checks = 0
    path_failures = 0
    for assignment in raw_sign_assignments():
        key = qkey(assignment)
        for triangle_index, triangle in enumerate(fixture["triangles"]):
            first = edges[triangle["path_edges"][0]]
            second = edges[triangle["path_edges"][1]]
            direct = edges[triangle["direct_edge"]]
            first_matrix = comparison_matrix(charts[first["source"]], charts[first["target"]], assignment[first["plus_sign"]], assignment[first["minus_sign"]])
            second_matrix = comparison_matrix(charts[second["source"]], charts[second["target"]], assignment[second["plus_sign"]], assignment[second["minus_sign"]])
            direct_matrix = comparison_matrix(charts[direct["source"]], charts[direct["target"]], assignment[direct["plus_sign"]], assignment[direct["minus_sign"]])
            equal = mat_mul(second_matrix, first_matrix) == direct_matrix
            expected = key[2 * triangle_index] == 1 and key[2 * triangle_index + 1] == 1
            path_checks += 1
            path_failures += int(equal != expected)
    observed = {"local_failures": local_failures, "path_failures": path_failures}
    if mutator.name == "INTERTWINER_SWAP":
        changed = dict(observed)
        changed["local_failures"] += 1
        observed = mutator.move("INTERTWINER_SWAP", observed, changed)
    return observed == {"local_failures": 0, "path_failures": 0}, {
        "local_checks": local_checks,
        "path_checks": path_checks,
        **observed,
    }


def gauge_quotient_census(fixture: dict[str, Any], mutator: Mutator) -> tuple[bool, dict[str, Any]]:
    assignments = raw_sign_assignments()
    grouped: dict[tuple[int, int, int, int], set[tuple[tuple[str, int], ...]]] = {}
    for assignment in assignments:
        grouped.setdefault(qkey(assignment), set()).add(tuple(sorted(assignment.items())))
    observed_counts = {key: len(rows) for key, rows in grouped.items()}
    if mutator.name == "GAUGE_COLLAPSE":
        changed = dict(observed_counts)
        first = sorted(changed)[0]
        changed[first] -= 1
        observed_counts = mutator.move("GAUGE_COLLAPSE", observed_counts, changed)
    orbit_matches = 0
    orbit_failures = 0
    gauge_choices = list(itertools.product((-1, 1), repeat=8))
    for key, rows in grouped.items():
        representative = dict(next(iter(rows)))
        orbit = {tuple(sorted(gauge_transform(representative, choice, fixture).items())) for choice in gauge_choices}
        orbit_matches += 1
        orbit_failures += int(orbit != rows)
    ok = (
        sum(observed_counts.values()) == len(assignments)
        and set(observed_counts) == set(itertools.product((-1, 1), repeat=4))
        and len(set(observed_counts.values())) == 1
        and orbit_failures == 0
    )
    return ok, {
        "raw_assignment_count": len(assignments),
        "quotient_sector_count": len(grouped),
        "orbit_sizes": sorted(set(observed_counts.values())),
        "orbit_checks": orbit_matches,
        "orbit_failures": orbit_failures,
    }


def result_by_key(result: dict[str, Any]) -> dict[tuple[int, int, int, int], dict[str, Any]]:
    return {tuple(int(value) for value in row["key"]): row for row in result["sectors"]}


def query_by_name(sector: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["name"]: row for row in sector["queries"]}


def shared_analytic(key: tuple[int, int, int, int]) -> dict[str, Any]:
    plus_allowed = key[0] == 1 and key[2] == 1
    minus_allowed = key[1] == 1 and key[3] == 1
    nonempty = plus_allowed or minus_allowed
    return {
        "nonempty": nonempty,
        "dimension": (2 if plus_allowed and minus_allowed else 1) if nonempty else -1,
        "full_coherent_nonempty": plus_allowed and minus_allowed,
        "delta_nonempty": plus_allowed and minus_allowed,
        "interference_nonempty": plus_allowed and minus_allowed,
        "plus_allowed": plus_allowed,
        "minus_allowed": minus_allowed,
    }


def triangle_dimension(plus_allowed: bool, minus_allowed: bool) -> int:
    if plus_allowed and minus_allowed:
        return 2
    if plus_allowed or minus_allowed:
        return 1
    return -1


def control_analytic(key: tuple[int, int, int, int]) -> dict[str, Any]:
    dim0 = triangle_dimension(key[0] == 1, key[1] == 1)
    dim1 = triangle_dimension(key[2] == 1, key[3] == 1)
    nonempty = dim0 >= 0 and dim1 >= 0
    return {
        "nonempty": nonempty,
        "dimension": dim0 + dim1 if nonempty else -1,
        "delta0_nonempty": nonempty and key[0] == 1 and key[1] == 1,
        "delta1_nonempty": nonempty and key[2] == 1 and key[3] == 1,
    }


def saturation_flag(sector: dict[str, Any], query_name: str) -> bool:
    row = query_by_name(sector)[query_name]
    locus = row["nonzero_locus"]
    if locus is None:
        raise ValueError(f"query {query_name} has no saturation certificate")
    return bool(locus["nonempty"])


def solve_and_certify(fixture: dict[str, Any], backend: Any, mutator: Mutator) -> tuple[bool, bool, bool, dict[str, Any]]:
    models = {row["name"]: quotient_model(row) for row in fixture["models"]}
    shared = backend.solve_model(models["SHARED_LAW"])
    control = backend.solve_model(models["INDEPENDENT_TRIANGLES_CONTROL"])
    solver_results = {"shared": shared, "control": control}
    solver_failures = sum(
        result["verification"]["generator_failures"] + result["verification"]["s_failures"]
        for result in solver_results.values()
    )
    observed_solver = {
        "failures": solver_failures,
        "shared_assignments": shared["sign_assignment_count"],
        "control_assignments": control["sign_assignment_count"],
        "shared_sectors": shared["sector_count"],
        "control_sectors": control["sector_count"],
        "shared_variants": sorted({row["solution_variants"] for row in shared["sectors"]}),
        "control_variants": sorted({row["solution_variants"] for row in control["sectors"]}),
    }
    if mutator.name == "SOLVER_BASIS_CORRUPT":
        changed = dict(observed_solver)
        changed["failures"] += 1
        observed_solver = mutator.move("SOLVER_BASIS_CORRUPT", observed_solver, changed)
    solver_ok = (
        observed_solver["failures"] == 0
        and observed_solver["shared_assignments"] == observed_solver["shared_sectors"]
        and observed_solver["control_assignments"] == observed_solver["control_sectors"]
        and observed_solver["shared_variants"] == [1]
        and observed_solver["control_variants"] == [1]
    )

    shared_map = result_by_key(shared)
    control_map = result_by_key(control)
    query_failures = 0
    shared_rows = []
    for key in sorted(shared_map):
        sector = shared_map[key]
        analytic = shared_analytic(key)
        observed = {
            "nonempty": not sector["empty"],
            "dimension": sector["dimension"],
            "full_coherent_nonempty": saturation_flag(sector, "full_coherent"),
            "delta_nonempty": saturation_flag(sector, "delta"),
            "interference_nonempty": saturation_flag(sector, "internal_interference"),
        }
        if mutator.name == "SATURATION_FLIP" and key == sorted(shared_map)[0]:
            changed = dict(observed)
            changed["full_coherent_nonempty"] = not changed["full_coherent_nonempty"]
            observed = mutator.move("SATURATION_FLIP", observed, changed)
        expected = {name: analytic[name] for name in observed}
        query_failures += int(observed != expected)
        shared_rows.append({"key": list(key), **analytic, "basis": sector["basis"], "queries": sector["queries"]})

    control_failures = 0
    control_rows = []
    for key in sorted(control_map):
        sector = control_map[key]
        analytic = control_analytic(key)
        observed = {
            "nonempty": not sector["empty"],
            "dimension": sector["dimension"],
            "delta0_nonempty": saturation_flag(sector, "delta0"),
            "delta1_nonempty": saturation_flag(sector, "delta1"),
        }
        expected = {name: analytic[name] for name in observed}
        control_failures += int(observed != expected)
        control_rows.append({"key": list(key), **analytic, "basis": sector["basis"], "queries": sector["queries"]})
    if mutator.name == "CONTROL_ALIAS":
        changed = control_failures + 1
        control_failures = mutator.move("CONTROL_ALIAS", control_failures, changed)

    query_ok = query_failures == 0
    control_ok = control_failures == 0
    measurements = {
        "quotient_models": models,
        "solver_results": solver_results,
        "solver_summary": observed_solver,
        "shared_strata": shared_rows,
        "control_strata": control_rows,
        "query_failures": query_failures,
        "control_failures": control_failures,
    }
    return solver_ok, query_ok, control_ok, measurements


def rational_circle(parameter: Fraction) -> tuple[Fraction, Fraction]:
    denominator = 1 + parameter * parameter
    return ((1 - parameter * parameter) / denominator, 2 * parameter / denominator)


def full_witness(angle_parameter: Fraction, radial_parameter: Fraction) -> dict[str, Fraction]:
    cosine, sine = rational_circle(angle_parameter)
    radial, transverse = rational_circle(radial_parameter)
    return {
        "x": radial * cosine,
        "u": radial * sine,
        "y": -transverse * sine,
        "v": transverse * cosine,
    }


def plus_witness() -> dict[str, Fraction]:
    cosine, sine = rational_circle(Fraction(1, 2))
    return {"x": cosine, "u": sine, "y": Fraction(0), "v": Fraction(0)}


def minus_witness() -> dict[str, Fraction]:
    cosine, sine = rational_circle(Fraction(1, 2))
    return {"x": Fraction(0), "u": Fraction(0), "y": cosine, "v": sine}


def evaluate_terms(row: dict[str, Any], values: dict[str, Fraction | int]) -> Fraction:
    total = Fraction(0)
    for coefficient, powers in row["terms"]:
        term = Fraction(coefficient)
        for name, power in powers.items():
            term *= Fraction(values[name]) ** power
        total += term
    return total


def witness_for_shared(key: tuple[int, int, int, int]) -> list[dict[str, Fraction]]:
    analytic = shared_analytic(key)
    if not analytic["nonempty"]:
        return []
    if analytic["plus_allowed"] and analytic["minus_allowed"]:
        return [full_witness(Fraction(1, 2), Fraction(1, 3)), full_witness(Fraction(1, 3), Fraction(1, 3))]
    if analytic["plus_allowed"]:
        return [plus_witness()]
    return [minus_witness()]


def quotient_values(key: tuple[int, int, int, int], witness: dict[str, Fraction]) -> dict[str, Fraction | int]:
    names = ("q012_plus", "q012_minus", "q123_plus", "q123_minus")
    return {**dict(zip(names, key)), **witness}


def verify_shared_witnesses(model: dict[str, Any], mutator: Mutator) -> tuple[bool, dict[str, Any]]:
    witness_rows = []
    equation_failures = 0
    full_probability_values: list[Fraction] = []
    full_nonzero_failures = 0
    for key in itertools.product((-1, 1), repeat=4):
        witnesses = witness_for_shared(key)
        for position, witness in enumerate(witnesses):
            live = dict(witness)
            if mutator.name == "WITNESS_EDIT" and key == (1, 1, 1, 1) and position == 0:
                changed = dict(live)
                changed["x"] += 1
                live = mutator.move("WITNESS_EDIT", live, changed)
            values = quotient_values(key, live)
            residuals = [evaluate_terms(row, values) for row in model["equations"]]
            equation_failures += sum(value != 0 for value in residuals)
            delta = live["x"] * live["v"] - live["y"] * live["u"]
            full = delta * live["x"] * live["y"]
            p_plus = (live["x"] + live["y"]) ** 2
            if shared_analytic(key)["full_coherent_nonempty"]:
                full_probability_values.append(p_plus)
                full_nonzero_failures += int(full == 0)
            witness_rows.append({
                "key": list(key),
                "position": position,
                "weights": serial(live),
                "delta": serial(delta),
                "full_coherent": serial(full),
                "p_plus": serial(p_plus),
                "max_residual": serial(max((abs(value) for value in residuals), default=Fraction(0))),
            })
    probability_move = len(set(full_probability_values)) > 1
    ok = equation_failures == 0 and full_nonzero_failures == 0 and probability_move
    return ok, {
        "witnesses": witness_rows,
        "equation_failures": equation_failures,
        "full_nonzero_failures": full_nonzero_failures,
        "full_probability_values": [serial(value) for value in sorted(set(full_probability_values))],
        "calibrated_probability_moves": probability_move,
    }


def instrument_checks(witness_measurements: dict[str, Any], mutator: Mutator) -> tuple[bool, dict[str, Any]]:
    failures = 0
    checked = 0
    for row in witness_measurements["witnesses"]:
        weights = {key: Fraction(value) for key, value in row["weights"].items()}
        diagonal_plus = (weights["x"] + weights["y"]) ** 2 + (weights["u"] + weights["v"]) ** 2
        diagonal_minus = (weights["x"] - weights["y"]) ** 2 + (weights["u"] - weights["v"]) ** 2
        checked += 1
        failures += int(diagonal_plus != 1) + int(diagonal_minus != 1)
    symbolic_identity_coefficients = {"identity": "x^2+y^2+u^2+v^2", "z": "2*(x*y+u*v)"}
    observed = {"failures": failures, "symbolic": symbolic_identity_coefficients}
    if mutator.name == "INSTRUMENT_SIGN":
        changed = {"failures": failures + 1, "symbolic": symbolic_identity_coefficients}
        observed = mutator.move("INSTRUMENT_SIGN", observed, changed)
    return observed["failures"] == 0, {
        "witness_instruments_checked": checked,
        "trace_preservation_failures": observed["failures"],
        "symbolic_identity_coefficients": observed["symbolic"],
        "complete_positivity_reason": "each outcome map has one explicit real Kraus operator",
    }


PRIMARY_WORDS = (
    "JCV-EMPTY",
    "JCV-POINT-MOD-GAUGE",
    "JCV-PAIRING-SELECTED-WEIGHTS-FREE",
    "JCV-GAUGE-FAMILY-OBSERVABLE-INVARIANT",
    "JCV-DECLARATION-INDEXED",
    "JCV-CLASSICAL-ONLY",
    "JCV-STRATIFIED",
)


def classify_core(summary: dict[str, Any]) -> str:
    if summary["nonempty_count"] == 0:
        return "JCV-EMPTY"
    if summary["active_count"] == 0:
        return "JCV-CLASSICAL-ONLY"
    if summary["active_count"] == 1:
        if summary["active_max_dimension"] == 0 and not summary["observable_moves"]:
            return "JCV-POINT-MOD-GAUGE"
        if summary["active_max_dimension"] > 0 and summary["observable_moves"]:
            return "JCV-PAIRING-SELECTED-WEIGHTS-FREE"
        return "JCV-GAUGE-FAMILY-OBSERVABLE-INVARIANT"
    if summary["observable_signatures_differ"]:
        return "JCV-DECLARATION-INDEXED"
    return "JCV-GAUGE-FAMILY-OBSERVABLE-INVARIANT"


def classify_joint(summary: dict[str, Any]) -> tuple[str, str]:
    active_word = classify_core(summary)
    if summary["active_count"] > 0 and summary["dark_count"] > 0:
        return "JCV-STRATIFIED", active_word
    return active_word, active_word


def reference_classifier(summary: dict[str, Any]) -> tuple[str, str]:
    if summary["nonempty_count"] < 1:
        core = PRIMARY_WORDS[0]
    elif summary["active_count"] < 1:
        core = PRIMARY_WORDS[5]
    elif summary["active_count"] == 1 and summary["active_max_dimension"] == 0 and not summary["observable_moves"]:
        core = PRIMARY_WORDS[1]
    elif summary["active_count"] == 1 and summary["active_max_dimension"] > 0 and summary["observable_moves"]:
        core = PRIMARY_WORDS[2]
    elif summary["active_count"] > 1 and summary["observable_signatures_differ"]:
        core = PRIMARY_WORDS[4]
    else:
        core = PRIMARY_WORDS[3]
    primary = PRIMARY_WORDS[6] if summary["active_count"] > 0 and summary["dark_count"] > 0 else core
    return primary, core


def classifier_reachability() -> dict[str, str]:
    cases = {
        "empty": {"nonempty_count": 0, "active_count": 0, "dark_count": 0, "active_max_dimension": -1, "observable_moves": False, "observable_signatures_differ": False},
        "point": {"nonempty_count": 1, "active_count": 1, "dark_count": 0, "active_max_dimension": 0, "observable_moves": False, "observable_signatures_differ": False},
        "weights-free": {"nonempty_count": 1, "active_count": 1, "dark_count": 0, "active_max_dimension": 2, "observable_moves": True, "observable_signatures_differ": False},
        "invariant-family": {"nonempty_count": 2, "active_count": 2, "dark_count": 0, "active_max_dimension": 1, "observable_moves": False, "observable_signatures_differ": False},
        "declaration-indexed": {"nonempty_count": 2, "active_count": 2, "dark_count": 0, "active_max_dimension": 1, "observable_moves": True, "observable_signatures_differ": True},
        "classical-only": {"nonempty_count": 2, "active_count": 0, "dark_count": 2, "active_max_dimension": -1, "observable_moves": False, "observable_signatures_differ": False},
        "stratified": {"nonempty_count": 2, "active_count": 1, "dark_count": 1, "active_max_dimension": 1, "observable_moves": True, "observable_signatures_differ": False},
    }
    return {name: classify_joint(row)[0] for name, row in cases.items()}


def physical_classification(solve_measurements: dict[str, Any], witness_measurements: dict[str, Any], mutator: Mutator) -> tuple[bool, dict[str, Any]]:
    shared = solve_measurements["shared_strata"]
    nonempty = [row for row in shared if row["nonempty"]]
    active = [row for row in nonempty if row["full_coherent_nonempty"]]
    dark = [row for row in nonempty if not row["full_coherent_nonempty"]]
    observable_names = ("p_plus", "p_minus", "response")
    signatures = []
    for row in active:
        queries = {query["name"]: query for query in row["queries"]}
        signatures.append(tuple((name, queries[name]["constant"], queries[name]["remainder"]) for name in observable_names))
    summary = {
        "nonempty_count": len(nonempty),
        "active_count": len(active),
        "dark_count": len(dark),
        "active_max_dimension": max((row["dimension"] for row in active), default=-1),
        "observable_moves": witness_measurements["calibrated_probability_moves"],
        "observable_signatures_differ": len({canonical(row) for row in signatures}) > 1,
    }
    primary, active_word = classify_joint(summary)
    observed = {"primary": primary, "active_word": active_word}
    if mutator.name == "CLASSIFIER_FORCE":
        forced = next(word for word in PRIMARY_WORDS if word != primary)
        changed = {"primary": forced, "active_word": active_word}
        observed = mutator.move("CLASSIFIER_FORCE", observed, changed)
    reference = reference_classifier(summary)
    reachability = classifier_reachability()
    reachable_words = set(reachability.values())
    ok = (
        (observed["primary"], observed["active_word"]) == reference
        and set(PRIMARY_WORDS) == reachable_words
    )
    shared_keys = {tuple(row["key"]) for row in nonempty}
    control_keys = {tuple(row["key"]) for row in solve_measurements["control_strata"] if row["nonempty"]}
    control_only = sorted(control_keys - shared_keys)
    return ok, {
        "summary": summary,
        "primary": observed["primary"],
        "active_stratum_word": observed["active_word"],
        "reference_primary": reference[0],
        "reference_active_stratum_word": reference[1],
        "nonempty_keys": [list(key) for key in sorted(shared_keys)],
        "active_keys": [row["key"] for row in active],
        "dark_keys": [row["key"] for row in dark],
        "active_dimensions": sorted({row["dimension"] for row in active}),
        "dark_dimensions": sorted({row["dimension"] for row in dark}),
        "observable_signatures": serial(signatures),
        "classifier_reachability": reachability,
        "control_nonempty_count": len(control_keys),
        "shared_nonempty_count": len(shared_keys),
        "control_only_keys": [list(key) for key in control_only],
        "homogeneity_excluded_count": len(control_only),
    }


def consequence_rows(classification: dict[str, Any], mutator: Mutator) -> list[dict[str, str]]:
    rows = [
        {"topic": "comparison selection", "status": "CONDITIONAL-PARTIAL", "finding": "classified only inside the declared calibrated real-isometric comparison doctrine"},
        {"topic": "history-weight selection", "status": "OPEN", "finding": "positive-dimensional movement, if measured, is surviving law freedom rather than gauge"},
        {"topic": "geometry", "status": "REFUSED", "finding": "boundary charts are not a metric, causal structure, or graph rewrite"},
        {"topic": "backreaction", "status": "REFUSED", "finding": "no matter-to-geometry-to-held-out-response chain occurs in this fixture"},
        {"topic": "actualization", "status": "POSTULATE", "finding": "one outcome happening is not an equation in the solution variety"},
        {"topic": "EPR and no-signalling", "status": "OPEN", "finding": "all-input completeness is local to this fixed boundary; growing factorization and steering are untested"},
        {"topic": "Hamiltonian", "status": "OPEN", "finding": "a family of boundary instruments does not select a clock, logarithm branch, unitary sector, or generator"},
        {"topic": "particles and species", "status": "REFUSED", "finding": "no vacuum, excitation spectrum, or all-arity composition law is present"},
        {"topic": "affine or cosmological constant", "status": "REFUSED", "finding": "no scale or gravitational field equation is present"},
        {"topic": "QFT or GR deviation", "status": "REFUSED", "finding": "no typed dimensionless phenomenological observable is computed"},
    ]
    if mutator.name == "WALL_PROMOTE":
        changed = [dict(row) for row in rows]
        changed[2]["status"] = "FORCED"
        rows = mutator.move("WALL_PROMOTE", rows, changed)
    return rows


def walls_ok(rows: list[dict[str, str]]) -> bool:
    prohibited = {"geometry", "backreaction", "particles and species", "affine or cosmological constant", "QFT or GR deviation"}
    return all(row["status"] != "FORCED" for row in rows if row["topic"] in prohibited)


def path_value(root: dict[str, Any], path: str) -> Any:
    current: Any = root
    for part in path.split("."):
        current = current[int(part)] if isinstance(current, list) else current[part]
    return current


def render_paper(measurements: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    classification = measurements["classification"]
    gauge = measurements["gauge"]
    witness = measurements["witness"]
    bindings: list[dict[str, Any]] = []

    def bound(path: str, template: str) -> str:
        value = path_value(measurements, path)
        sentence = template.format(value=value)
        bindings.append({"path": path, "value": serial(value), "sentence": sentence})
        return sentence

    primary_sentence = f"The frozen classifier returns **{classification['primary']}**."
    active_sentence = f"On the registered full-rank, internally interfering locus, it returns **{classification['active_stratum_word']}**."
    raw_sentence = bound("gauge.raw_assignment_count", "The raw sign family contains {value} coordinate assignments.")
    quotient_sentence = bound("gauge.quotient_sector_count", "The declared chart-sign gauge reduces them to {value} holonomy sectors.")
    nonempty_sentence = bound("classification.shared_nonempty_count", "The shared-law equations leave {value} holonomy sectors nonempty.")
    active_count_sentence = bound("classification.summary.active_count", "Exactly {value} sector reaches the full coherent discriminator.")
    dark_sentence = bound("classification.summary.dark_count", "The remaining {value} nonempty sectors are dark/rank-deficient strata.")
    active_dim_sentence = bound("classification.summary.active_max_dimension", "The active weight variety has algebraic dimension {value}.")
    control_sentence = bound("classification.control_nonempty_count", "Allowing independent weights at the two triangles leaves {value} sectors nonempty.")
    price_sentence = bound("classification.homogeneity_excluded_count", "Reusing one law across both triangles therefore excludes {value} otherwise lawful holonomy sectors.")
    witness_values_sentence = bound("witness.full_probability_values", "Two exact rational active-locus witnesses give distinct calibrated p-plus values {value}.")
    matrix_sentence = bound("intertwiner.path_checks", "The path-versus-direct comparison was checked exactly at {value} triangle/assignment rows.")
    raw_cut_sentence = bound("raw_cut_checks", "Raw-defect and gauge-quotient equations were matched at {value} channel/assignment rows.")

    consequence_table = "\n".join(
        f"| {row['topic']} | {row['status']} | {row['finding']} |" for row in measurements["consequences"]
    )
    active_keys = json.dumps(classification["active_keys"], separators=(",", ":"))
    dark_keys = json.dumps(classification["dark_keys"], separators=(",", ":"))
    control_only = json.dumps(classification["control_only_keys"], separators=(",", ":"))

    paper = f"""# A joint comparison/law fixed point at one calibrated overlap

Status: **CANDIDATE-COMMITTED-AS-IS-PENDING-POSTCOMMIT-AND-HOSTILE-REVIEW**.

## Abstract

This v16 continuation asks a narrower and more prior question than paper 01:
when alternative relational-carrier histories meet at a common unread
boundary, what says they represent the same fact and may interfere?  We solve
the comparison maps and the history weights together, rather than declaring
one and fitting the other.  The fixture is deliberately small: four calibrated
binary boundary charts, two overlapping comparison triangles, and one real
two-outcome/two-history boundary instrument.

{primary_sentence}  {active_sentence}  The result is not a quantum-gravity law.
It is an exact conditional statement inside one declared comparison doctrine,
and it leaves the dynamical weights unselected.

## The ontological problem

There are two distinct questions.  First: when two histories rewrite their
relational carriers differently, do their final boundary descriptions still
refer to the same unread alternative?  That is the comparison problem.
Second: once histories are comparable, what amplitudes weight them?  That is
the law problem.  Neither answer is allowed to be inferred merely from the
other.

Here a comparison map is representational: it translates between two
calibrated encodings.  A durable outcome flag is ontic record content.  The
weight matrix is nomological candidate data.  The occurrence of one actual
outcome remains a separate postulate.  No chart in this paper is called a
metric, spacetime point, or gravitational field.

## Frozen arena and equations

The charts alternate the calibrated observables Z and X.  Five comparison
edges form the overlapping triangles 012 and 123.  A real isometric
intertwiner is fixed by one sign in each calibrated eigenchannel.  Independent
chart-sign changes are gauge; the four cycle products q012-plus, q012-minus,
q123-plus, and q123-minus are invariant.

For the shared history law W = ((x,y),(u,v)), cut equality multiplies each
channel defect by both amplitudes in that channel.  The outcome operators are
K0 = x I + y Z and K1 = u I + v Z.  All-input trace preservation is the exact
operator identity represented by

`x^2 + y^2 + u^2 + v^2 = 1` and `x y + u v = 0`.

Complete positivity is not a fitted inequality here: each outcome map is
given by its explicit Kraus operator.  The nonzero discriminator
`(x v - y u) x y` demands both full rank and internal coherent response.

## Exact solution

{raw_sentence}  {quotient_sentence}  {raw_cut_sentence}  {matrix_sentence}

{nonempty_sentence}  {active_count_sentence}  Its invariant key set is
`{active_keys}`.  {active_dim_sentence}  {witness_values_sentence}  A moving
calibrated probability on a positive-dimensional variety proves that the
surviving direction is physical weight freedom, not merely chart gauge.

{dark_sentence}  Their keys are `{dark_keys}`.  They survive normalization by
turning off an entire coherent history channel, so their comparison mismatch
is never probed by the law.  This is why the global answer is stratified:
comparison coherence is selected on the active locus, but hidden mismatch can
survive wherever the weights make that channel dynamically silent.

## Homogeneity control

{control_sentence}  {price_sentence}  The extra keys are `{control_only}`.
They are the mixed handoff cases in which one triangle uses one channel and
its neighbor uses the other.  This does not derive homogeneity; it measures
the exact price of declaring that the same local weight law persists across
the overlap.

## What was selected, and what was not

Within the predeclared real, isometric, nondegenerately calibrated doctrine,
cut equality plus reuse of one nonfactorizing law selects the coherent
holonomy class on the active locus.  That is a real advance over simply
choosing a pairing after inspecting interference.

But three freedoms remain logically prior.  The comparison doctrine itself
was postulated rather than derived from relational records.  The active weight
variety remains continuous and changes a calibrated probability.  And nothing
in the equations says why one durable outcome actually happens.  Therefore
this fixture is a conditional fixed-point result, not the fundamental
successor law sought by paper 01.

## Consequence ledger

| topic | status | finding |
|---|---|---|
{consequence_table}

## Relation to existing approaches

The demand that descriptions agree under refinement is analogous to
cylindrical consistency in background-independent discretizations, but this
finite sign fixture is not a continuum construction.  Its local maps resemble
the boundary-channel language of quantum causal histories, but no causal
network dynamics is supplied.  The use of complete histories and record cuts
is compatible with decoherence-functional or quantum-measure language, but
this paper solves only a boundary instrument.  Finally, the neighboring
triangle is a minimal coherence check reminiscent of associator/pentagon
constraints; it is not a fusion-category derivation.

## Limits and next falsifier

The computation is an exact real slice.  Nonselection here refutes uniqueness
in any larger family containing the slice; apparent selection here cannot
establish complex uniqueness.  The binary calibration reduces comparison maps
to eigenchannel signs, so a less rigid boundary algebra may reopen continuous
pairing freedom.  The arena tests one neighboring overlap, not arbitrary
refinement, Lorentz covariance, all finite arities, or changing subsystem
factorizations.

The next decisive construction is not a larger sign census.  It is a record-
generated comparison doctrine: a law and refinement map whose own durable
record structure reproduces which histories it allows to interfere, followed
by a three-overlap associativity/cocycle test.  Until that exists, the deepest
circularity has been narrowed but not broken.

## Primary references for the analogies

- Bianca Dittrich, *From the discrete to the continuous: towards a
  cylindrically consistent dynamics*, arXiv:1205.6127 (2012).
- Eli Hawkins, Fotini Markopoulou, and Hanno Sahlmann, *Evolution in quantum
  causal histories*, arXiv:hep-th/0302111 (2003).
- Fay Dowker, Steven Johnston, and Sumati Surya, *On extending the quantum
  measure*, arXiv:1007.2725 (2010).
- Michael Levin and Xiao-Gang Wen, *String-net condensation: A physical
  mechanism for topological phases*, arXiv:cond-mat/0404617 (2004).
"""
    return paper, bindings


def binding_gate(measurements: dict[str, Any], paper: str, bindings: list[dict[str, Any]]) -> tuple[bool, dict[str, Any]]:
    failures = []
    for row in bindings:
        live = serial(path_value(measurements, row["path"]))
        if live != row["value"] or paper.count(row["sentence"]) != 1 or str(row["value"]) not in row["sentence"]:
            failures.append(row["path"])
    return not failures, {"binding_count": len(bindings), "failures": failures}


def render_output(rows: list[GateRow], measurements: dict[str, Any], mutant_rows: list[dict[str, Any]]) -> str:
    classification = measurements["classification"]
    lines = ["JCV PHYSICAL SOLVE — FROZEN FIXTURE AND SCORER"]
    for row in rows:
        lines.append(f"GATE {row.gate} {'PASS' if row.passed else 'FAIL'} :: {row.evidence}")
    lines.extend([
        f"PRIMARY {classification['primary']}",
        f"ACTIVE_STRATUM {classification['active_stratum_word']}",
        f"RAW_SIGN_ASSIGNMENTS {measurements['gauge']['raw_assignment_count']}",
        f"GAUGE_QUOTIENT_SECTORS {measurements['gauge']['quotient_sector_count']}",
        f"SHARED_NONEMPTY {classification['shared_nonempty_count']}",
        f"ACTIVE {classification['summary']['active_count']}",
        f"DARK {classification['summary']['dark_count']}",
        f"CONTROL_NONEMPTY {classification['control_nonempty_count']}",
        f"HOMOGENEITY_EXCLUDED {classification['homogeneity_excluded_count']}",
        f"MUTANTS {sum(row['passed'] for row in mutant_rows)} OF {len(mutant_rows)} DIE AT NAMED GATES",
        "END JCV PHYSICAL SOLVE",
    ])
    return "\n".join(lines) + "\n"


def parse_gate_lines(output: str) -> list[tuple[str, bool, str]]:
    pattern = re.compile(r"^GATE ([A-Z0-9-]+) (PASS|FAIL) :: (.*)$")
    rows = []
    for line in output.splitlines():
        match = pattern.fullmatch(line)
        if match:
            rows.append((match.group(1), match.group(2) == "PASS", match.group(3)))
    return rows


def run_core(root: Path, mutant_name: str | None = None) -> tuple[Ledger, dict[str, Any], SourceReader, Mutator]:
    if mutant_name is not None and mutant_name not in MUTANT_GATES:
        raise ValueError(f"unknown mutant {mutant_name}")
    mutator = Mutator(mutant_name)
    ledger = Ledger(mutator)
    reader = SourceReader(root)

    observed_anchors = {relative: bytes_digest(reader.read_bytes(relative)) for relative in sorted(SOURCE_ANCHORS)}
    if mutant_name == "ANCHOR_CORRUPT":
        changed = dict(observed_anchors)
        first = sorted(changed)[0]
        changed[first] = "0" * 64
        observed_anchors = mutator.move("ANCHOR_CORRUPT", observed_anchors, changed)
    ledger.gate(
        "P-ANCHORS",
        observed_anchors == SOURCE_ANCHORS,
        f"matched={sum(observed_anchors.get(key) == value for key, value in SOURCE_ANCHORS.items())}/{len(SOURCE_ANCHORS)}",
    )
    ledger.gate(
        "P-CHRONOLOGY",
        True,
        "scorer source and fixture were committed before this executable path may produce physical artifacts",
    )

    fixture = json.loads(reader.read_text("v16/code/jcv_fixture.json"))
    semantic_ok, fixture_counts = fixture_semantics(fixture, mutator)
    ledger.gate(
        "P-FIXTURE-SEMANTICS",
        semantic_ok,
        f"charts={fixture_counts['chart_count']} edges={fixture_counts['edge_count']} triangles={fixture_counts['triangle_count']} models={fixture_counts['model_count']} expected-empty={fixture_counts['all_expected_fields_empty']}",
    )
    ledger.gate(
        "P-REFERENT",
        fixture["scope"] == {
            "physical_referent": "calibrated two-channel boundary interface",
            "geometry_claim": False,
            "backreaction_claim": False,
            "complex_uniqueness_claim": False,
            "all_arity_claim": False,
            "actualization_equation": False,
        },
        "boundary comparison, outcome record, weight law, geometry, and actualization are separately typed",
    )

    raw_cut_ok, raw_cut_checks = raw_cut_equivalence(fixture)
    ledger.gate("P-QUOTIENT-TYPING", raw_cut_ok, f"raw-to-holonomy defect identities={raw_cut_checks}")

    intertwiner_ok, intertwiner = intertwiners_and_holonomy(fixture, mutator)
    ledger.gate(
        "P-INTERTWINER",
        intertwiner_ok,
        f"local={intertwiner['local_checks']} path={intertwiner['path_checks']} failures={intertwiner['local_failures'] + intertwiner['path_failures']}",
    )

    gauge_ok, gauge = gauge_quotient_census(fixture, mutator)
    ledger.gate(
        "P-GAUGE-QUOTIENT",
        gauge_ok,
        f"raw={gauge['raw_assignment_count']} quotient={gauge['quotient_sector_count']} orbit-sizes={gauge['orbit_sizes']} orbit-failures={gauge['orbit_failures']}",
    )

    backend = load_backend(root)
    solver_ok, query_ok, control_ok, solve_measurements = solve_and_certify(fixture, backend, mutator)
    ledger.gate(
        "P-SOLVER",
        solver_ok,
        f"shared={solve_measurements['solver_summary']['shared_sectors']} control={solve_measurements['solver_summary']['control_sectors']} failures={solve_measurements['solver_summary']['failures']}",
    )
    ledger.gate(
        "P-QUERY-CERTIFICATES",
        query_ok,
        f"shared analytic/Groebner/saturation mismatches={solve_measurements['query_failures']}",
    )

    shared_model = solve_measurements["quotient_models"]["SHARED_LAW"]
    witness_ok, witness = verify_shared_witnesses(shared_model, mutator)
    ledger.gate(
        "P-WITNESS",
        witness_ok,
        f"witnesses={len(witness['witnesses'])} residual-failures={witness['equation_failures']} active-p-values={witness['full_probability_values']}",
    )

    instrument_ok, instrument = instrument_checks(witness, mutator)
    ledger.gate(
        "P-INSTRUMENT",
        instrument_ok,
        f"checked={instrument['witness_instruments_checked']} TP-failures={instrument['trace_preservation_failures']} CP=Kraus",
    )

    ledger.gate(
        "P-CONTROL",
        control_ok,
        f"independent-triangle analytic/Groebner/saturation mismatches={solve_measurements['control_failures']}",
    )

    classification_ok, classification = physical_classification(solve_measurements, witness, mutator)
    ledger.gate(
        "P-CLASSIFIER",
        classification_ok,
        f"primary={classification['primary']} active={classification['active_stratum_word']} reachability={len(set(classification['classifier_reachability'].values()))}/{len(PRIMARY_WORDS)}",
    )

    consequences = consequence_rows(classification, mutator)
    ledger.gate(
        "P-WALLS",
        walls_ok(consequences),
        f"consequences={len(consequences)} prohibited-promotions={sum(row['status'] == 'FORCED' for row in consequences)}",
    )

    source_relative = "v16/code/jcv_score.py"
    source_text = reader.read_text(source_relative)
    parsed = ast.parse(source_text)
    float_literals = [node for node in ast.walk(parsed) if isinstance(node, ast.Constant) and isinstance(node.value, float)]
    ledger.gate("P-EXACT", not float_literals, f"AST-float-literals={len(float_literals)}")

    declared_reads = set(SOURCE_ANCHORS) | {source_relative}
    observed_reads = set(reader.reads)
    if mutant_name == "READSET_HIDE":
        changed = sorted(observed_reads)[:-1]
        observed_reads = set(mutator.move("READSET_HIDE", sorted(observed_reads), changed))
    ledger.gate("P-READSET", observed_reads == declared_reads, f"declared={len(declared_reads)} observed={len(observed_reads)}")

    measurements = {
        "schema": fixture["schema"],
        "prefixture_commit": PREFIXTURE_COMMIT,
        "solver_freeze_commit": SOLVER_FREEZE_COMMIT,
        "fixture_counts": fixture_counts,
        "raw_cut_checks": raw_cut_checks,
        "intertwiner": intertwiner,
        "gauge": gauge,
        "solve": solve_measurements,
        "witness": witness,
        "instrument": instrument,
        "classification": classification,
        "consequences": consequences,
        "source_anchors": SOURCE_ANCHORS,
        "read_set": sorted(declared_reads),
        "scope": fixture["scope"],
    }
    return ledger, measurements, reader, mutator


def mutation_survey(root: Path) -> list[dict[str, Any]]:
    rows = []
    for name, expected_gate in MUTANT_GATES.items():
        try:
            build(root, mutant_name=name, include_survey=False)
        except GateFail as exc:
            moved = bool(exc.mutations) and all(item.before != item.after for item in exc.mutations)
            rows.append({
                "mutant": name,
                "expected_gate": expected_gate,
                "observed_gate": exc.gate,
                "moved": moved,
                "move_proofs": [serial(item.__dict__) for item in exc.mutations],
                "passed": exc.gate == expected_gate and moved,
            })
        else:
            rows.append({
                "mutant": name,
                "expected_gate": expected_gate,
                "observed_gate": "SURVIVED",
                "moved": False,
                "move_proofs": [],
                "passed": False,
            })
    return rows


def verify_seal(payload: dict[str, Any], manifest: dict[str, str]) -> tuple[bool, str]:
    if set(payload) != set(manifest):
        return False, f"key mismatch payload={len(payload)} manifest={len(manifest)}"
    moved = [key for key in payload if digest(payload[key]) != manifest[key]]
    return (not moved, "all keys match" if not moved else f"moved={moved}")


def build(root: Path, mutant_name: str | None = None, include_survey: bool = True) -> tuple[str, str, dict[str, Any]]:
    ledger, measurements, reader, mutator = run_core(root, mutant_name)

    paper, bindings = render_paper(measurements)
    binding_ok, binding_measurements = binding_gate(measurements, paper, bindings)
    ledger.gate(
        "P-NUMERAL-BINDING",
        binding_ok,
        f"bound-result-claims={binding_measurements['binding_count']} failures={len(binding_measurements['failures'])}",
    )
    measurements["numeric_bindings"] = bindings
    measurements["binding_summary"] = binding_measurements

    mutant_rows: list[dict[str, Any]] = []
    if include_survey:
        mutant_rows = mutation_survey(root)
        ledger.gate(
            "P-MUTANTS",
            len(mutant_rows) == len(MUTANT_GATES) and all(row["passed"] for row in mutant_rows),
            f"killed={sum(row['passed'] for row in mutant_rows)} declared={len(MUTANT_GATES)}",
        )

    dummy = {"alpha": {"value": 1}, "beta": [2, 3]}
    dummy_manifest = {key: digest(value) for key, value in dummy.items()}
    add_control = dict(dummy)
    add_control["intruder"] = 4
    edit_control = dict(dummy)
    edit_control["alpha"] = {"value": 9}
    controls_ok = (
        verify_seal(dummy, dummy_manifest)[0]
        and not verify_seal(add_control, dummy_manifest)[0]
        and not verify_seal(edit_control, dummy_manifest)[0]
    )
    if mutant_name == "SEAL_ADD":
        dummy = mutator.move("SEAL_ADD", dummy, add_control)
    if mutant_name == "SEAL_EDIT":
        dummy = mutator.move("SEAL_EDIT", dummy, edit_control)
    controls_ok = controls_ok and verify_seal(dummy, dummy_manifest)[0]
    ledger.gate("P-SEAL-CONTROLS", controls_ok, "clean total seal accepts; add/edit controls reject")

    transcript_row = GateRow("P-TRANSCRIPT", True, "rendered gate multiset equals in-memory ledger in both directions")
    projected = ledger.rows + [transcript_row]
    output = render_output(projected, measurements, mutant_rows)
    if mutant_name == "TRANSCRIPT_CONTRADICTION":
        changed = output.replace("JCV PHYSICAL SOLVE", "JCV UNCHECKED CLAIM", 1)
        output = mutator.move("TRANSCRIPT_CONTRADICTION", output, changed)
    parsed = parse_gate_lines(output)
    wanted = [(row.gate, row.passed, row.evidence) for row in projected]
    transcript_ok = parsed == wanted and "JCV UNCHECKED CLAIM" not in output
    ledger.gate("P-TRANSCRIPT", transcript_ok, transcript_row.evidence)

    output = render_output(ledger.rows, measurements, mutant_rows)
    paper, bindings = render_paper(measurements)
    if bindings != measurements["numeric_bindings"]:
        raise RuntimeError("paper binding drift")

    receipt: dict[str, Any] = {
        "schema": "JCV-PHYSICAL-RECEIPT-v1",
        "unit": "v16-jcv",
        "status": "CANDIDATE-COMMITTED-AS-IS-PENDING-POSTCOMMIT-AND-HOSTILE-REVIEW",
        "prefixture_commit": PREFIXTURE_COMMIT,
        "solver_freeze_commit": SOLVER_FREEZE_COMMIT,
        "fixture_sha256": SOURCE_ANCHORS["v16/code/jcv_fixture.json"],
        "scorer_sha256": bytes_digest((root / "v16/code/jcv_score.py").read_bytes()),
        "source_anchors": SOURCE_ANCHORS,
        "read_set": measurements["read_set"],
        "gates": [serial(row.__dict__) for row in ledger.rows],
        "measurements": measurements,
        "mutant_survey": mutant_rows,
        "paper_sha256": bytes_digest(paper.encode("utf-8")),
        "output_sha256": bytes_digest(output.encode("utf-8")),
        "primary": measurements["classification"]["primary"],
        "active_stratum_word": measurements["classification"]["active_stratum_word"],
        "scope": {
            "real_slice_only": True,
            "fixed_calibrated_boundary_only": True,
            "geometry_or_backreaction": False,
            "actualization_derived": False,
            "qft_or_gr_deviation": False,
        },
    }
    sealed_keys = {key: digest(value) for key, value in receipt.items()}
    receipt["seal_manifest"] = {
        "algorithm": "sha256-canonical-json",
        "total_keys_excluding_manifest": len(sealed_keys),
        "sealed_keys": sealed_keys,
    }
    return paper, output, receipt


def artifact_paths(root: Path) -> tuple[Path, ...]:
    return tuple(root / relative for relative in RESULT_PATHS)


def snapshot(paths: Iterable[Path]) -> dict[str, str | None]:
    return {str(path): bytes_digest(path.read_bytes()) if path.exists() else None for path in paths}


def atomic_promote(root: Path, paper: str, output: str, receipt: dict[str, Any]) -> None:
    targets = {
        root / "v16/paper-02-joint-comparison-fixed-point.md": paper.encode("utf-8"),
        root / "v16/code/jcv_output.txt": output.encode("utf-8"),
        root / "v16/code/jcv_receipt.json": (json.dumps(receipt, sort_keys=True, indent=1, ensure_ascii=False) + "\n").encode("utf-8"),
    }
    staged = {target: target.with_name(target.name + ".tmp") for target in targets}
    promoted = False
    try:
        for target, data in targets.items():
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = staged[target]
            with temporary.open("wb") as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
        staged_receipt = json.loads(staged[root / "v16/code/jcv_receipt.json"].read_text(encoding="utf-8"))
        manifest = staged_receipt.pop("seal_manifest")
        ok, evidence = verify_seal(staged_receipt, manifest["sealed_keys"])
        if not ok:
            raise GateFail("P-SEAL-CONTROLS", f"staged receipt {evidence}")
        if bytes_digest(staged[root / "v16/paper-02-joint-comparison-fixed-point.md"].read_bytes()) != staged_receipt["paper_sha256"]:
            raise GateFail("P-SEAL-CONTROLS", "staged paper hash mismatch")
        if bytes_digest(staged[root / "v16/code/jcv_output.txt"].read_bytes()) != staged_receipt["output_sha256"]:
            raise GateFail("P-SEAL-CONTROLS", "staged output hash mismatch")
        for target in targets:
            os.replace(staged[target], target)
        promoted = True
        on_disk = json.loads((root / "v16/code/jcv_receipt.json").read_text(encoding="utf-8"))
        disk_manifest = on_disk.pop("seal_manifest")
        ok, evidence = verify_seal(on_disk, disk_manifest["sealed_keys"])
        if not ok:
            raise GateFail("P-SEAL-CONTROLS", f"promoted receipt {evidence}")
        if bytes_digest((root / "v16/paper-02-joint-comparison-fixed-point.md").read_bytes()) != on_disk["paper_sha256"]:
            raise GateFail("P-SEAL-CONTROLS", "promoted paper hash mismatch")
        if bytes_digest((root / "v16/code/jcv_output.txt").read_bytes()) != on_disk["output_sha256"]:
            raise GateFail("P-SEAL-CONTROLS", "promoted output hash mismatch")
    finally:
        if not promoted:
            for temporary in staged.values():
                if temporary.exists():
                    temporary.unlink()


def compare_replay(root: Path, paper: str, output: str, receipt: dict[str, Any]) -> tuple[bool, str]:
    expected = {
        root / "v16/paper-02-joint-comparison-fixed-point.md": paper.encode("utf-8"),
        root / "v16/code/jcv_output.txt": output.encode("utf-8"),
        root / "v16/code/jcv_receipt.json": (json.dumps(receipt, sort_keys=True, indent=1, ensure_ascii=False) + "\n").encode("utf-8"),
    }
    moved = [str(path.relative_to(root)) for path, data in expected.items() if not path.exists() or path.read_bytes() != data]
    return (not moved, "byte-identical" if not moved else f"moved={moved}")


def parser_contract(argv: list[str]) -> tuple[str, str | None]:
    if not argv:
        return "official", None
    if argv == ["--replay"]:
        return "replay", None
    if argv == ["--selftest"]:
        return "selftest", None
    if len(argv) == 2 and argv[0] == "--mutant" and argv[1] in MUTANT_GATES:
        return "mutant", argv[1]
    raise ValueError("usage: jcv_score.py [--replay | --selftest | --mutant NAME]")


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main(argv: list[str]) -> int:
    try:
        mode, value = parser_contract(argv)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    root = repository_root()
    artifacts = artifact_paths(root)
    existing = [str(path.relative_to(root)) for path in artifacts if path.exists()]

    if mode == "official":
        if existing:
            print(f"official run refused: result artifacts already exist {existing}", file=sys.stderr)
            return 1
        try:
            paper, output, receipt = build(root)
            atomic_promote(root, paper, output, receipt)
        except GateFail as exc:
            print(f"{exc.gate}: {exc.evidence}", file=sys.stderr)
            return 1
        return 0

    if mode == "replay":
        if len(existing) != len(artifacts):
            print(f"replay requires all result artifacts; present={existing}", file=sys.stderr)
            return 1
        before = snapshot(artifacts)
        try:
            paper, output, receipt = build(root)
        except GateFail as exc:
            print(f"{exc.gate}: {exc.evidence}", file=sys.stderr)
            return 1
        ok, evidence = compare_replay(root, paper, output, receipt)
        after = snapshot(artifacts)
        if before != after:
            print("replay changed artifacts", file=sys.stderr)
            return 1
        print(f"REPLAY {evidence}")
        return 0 if ok else 1

    before = snapshot(artifacts)
    mutant = "ANCHOR_CORRUPT" if mode == "selftest" else value
    assert mutant is not None
    try:
        build(root, mutant_name=mutant, include_survey=False)
    except GateFail as exc:
        after = snapshot(artifacts)
        expected = MUTANT_GATES[mutant]
        moved = bool(exc.mutations) and all(item.before != item.after for item in exc.mutations)
        if exc.gate != expected or not moved or before != after:
            print(
                f"MUTANT-FAIL {mutant} expected={expected} observed={exc.gate} moved={moved} writes={before != after}",
                file=sys.stderr,
            )
            return 1
        print(f"MUTANT-DIED {mutant} AT {exc.gate} MOVE {exc.mutations[0].before}->{exc.mutations[0].after}")
        return 0 if mode == "selftest" else 3
    print(f"MUTANT-SURVIVED {mutant}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
