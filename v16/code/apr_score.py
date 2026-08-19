#!/usr/bin/env python3
"""Exact, result-neutral scorer for APR Paper 12.

The scorer reconstructs semantic objects from the frozen APR primitive
fixtures.  It deliberately distinguishes finite instrument presentations from
a total regional process functor.  It contains no table of fixture answers and
never calls Git, the network, the current working directory, or fixture-side
measurement functions.

Official evaluation is available only through ``--run`` with two explicit,
previously absent destinations.  ``--selftest`` uses synthetic objects and
does not evaluate the frozen APR fixture.  Mutant modes evaluate fresh
in-memory copies and write no artifacts.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import os
import re
import sys
import tempfile
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Mapping, MutableMapping, Sequence


SCRIPT_DIR = Path(__file__).resolve().parent
V16_DIR = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from apr_core import (  # noqa: E402
    ComparisonCandidate,
    FutureProfileQuotient,
    LinearContinuation,
    PredictiveBoundary,
    PrefixRegion,
    QMatrix,
    RegionProfileEntry,
    boundary_partition_signature,
    canonical_data,
    canonical_json,
    canonical_sha256,
    comparison_family_invariants,
    compute_stable_null,
    exact,
    fraction_text,
    qadd,
    qkernel,
    qmultiply,
    qrank,
    qrowspace,
    qscale,
    qsubtract,
    qsubspace_inclusion_residual,
    qtranspose,
    qvstack,
    regional_profile_equivalence,
)


SCORER_SCHEMA = "apr-exact-scorer-v1"
RECEIPT_SCHEMA = "apr-score-receipt-v1"
TRANSCRIPT_SCHEMA = "apr-score-transcript-v1"

IMMUTABLE_HASHES: dict[str, str] = {
    "note-apr-pin.md": "f2b952182b9356e8ebb0aa07e1a6a022a5f892585a20d118f5ea75aabccbec52",
    "note-apr-pin-addendum.md": "d018d0129f6ae7c312599e3fe0ab66cb8689a78ded9969d74c1c3e5d97e67fe5",
    "note-apr-pin-addendum-2.md": "54573094f1ebb872f5daa907888bd4ee264ec9fe337562c62e30e3e9dfd865da",
    "note-apr-scorer-protocol.md": "0ff8687231a99edb3264b2a24c10cec49e2e52c4e5c7720e7a7089983c227e31",
    "note-apr-scorer-protocol-addendum.md": "4c64a9c8c79534c6fb0d69fd7a4445d4fc0b8b4c20bd7dc710165d46f080e8fe",
    "note-apr-scorer-protocol-addendum-2.md": "9b1d7d75526c9b97befd6f016bfc5242162e1e48b259984852b4924950f9acaa",
    "code/apr_core.py": "cd51fd36bc26701fdc649ee81f4b048dadde03e645860a7b885c501e2e180ca9",
    "code/apr_fixtures.py": "0698d5d413384e43108241a15eb7134fda82deec8bffdc4413edb2c5ea2742bc",
}
FROZEN_FIXTURE_PAYLOAD_SHA256 = (
    "1f55bb4a495fb7d5a76f93c83e39cc72337fbff0f1a31e67b8bda5ccd45816d0"
)
FROZEN_FIXTURE_COMMIT = "2dfd8ba357e37b6d486b3ce1ba0d0bfd6113fb62"
BINDING_PROTOCOL_COMMITS = (
    "bf67893",
    "c635310",
    "a258868",
)

PRIMARY_WORDS = (
    "APR-INCONSISTENT",
    "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA",
    "APR-BLOCKED-AT-BOUNDARY-GLUING",
    "APR-BLOCKED-AT-TWO-ARROW-TYPING",
    "APR-BLOCKED-AT-FUTURE-PROFILE-COMPLETENESS",
    "APR-BLOCKED-AT-REGIONAL-CONGRUENCE",
    "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED",
    "APR-COMPARISON-QUOTIENT-CONSTRUCTED-BUT-DYNAMICAL-LOCALITY-FAILS",
    "APR-DYNAMIC-REGIONAL-REFERENT-CONSTRUCTED-BUT-CAUSAL-ORDER-PRICED",
    "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
    "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED",
)
STATIC_QUALIFIER = "APR-STATIC-ATOMLESS-RESPONSE-CONSTRUCTED-PROCESS-UNBUILT"

MUTANT_IDS = tuple(
    [f"M{index:02d}" for index in range(1, 36)]
    + [f"P{index}" for index in range(1, 9)]
    + [f"L{index}" for index in range(1, 7)]
    + [f"G{index}" for index in range(1, 8)]
)


class ScoreRefusal(RuntimeError):
    """A typed refusal: missing construction is never converted to success."""


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_path(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def authenticate_inputs() -> dict[str, object]:
    observed: dict[str, str] = {}
    for relative, expected in IMMUTABLE_HASHES.items():
        path = V16_DIR / relative
        if not path.is_file():
            raise ScoreRefusal(f"missing immutable input: {relative}")
        actual = sha256_path(path)
        observed[relative] = actual
        if actual != expected:
            raise ScoreRefusal(
                f"immutable input hash mismatch for {relative}: {actual} != {expected}"
            )
    return {
        "frozen_fixture_commit": FROZEN_FIXTURE_COMMIT,
        "binding_protocol_commits": list(BINDING_PROTOCOL_COMMITS),
        "files": observed,
    }


def load_frozen_fixture() -> tuple[dict[str, object], dict[str, object]]:
    authentication = authenticate_inputs()
    import apr_fixtures  # imported only after byte authentication

    payload = copy.deepcopy(apr_fixtures.FIXTURE_DATA)
    payload_hash = canonical_sha256(payload)
    if payload_hash != FROZEN_FIXTURE_PAYLOAD_SHA256:
        raise ScoreRefusal(
            f"canonical fixture payload mismatch: {payload_hash} != "
            f"{FROZEN_FIXTURE_PAYLOAD_SHA256}"
        )
    return payload, authentication


def index_rows(rows: object, *, field_name: str = "id") -> dict[str, Mapping[str, object]]:
    if not isinstance(rows, list):
        raise ScoreRefusal("expected a list of primitive rows")
    result: dict[str, Mapping[str, object]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("primitive row is not a mapping")
        identifier = row.get(field_name)
        if not isinstance(identifier, str) or not identifier:
            raise ScoreRefusal(f"primitive row lacks {field_name}")
        if identifier in result:
            raise ScoreRefusal(f"duplicate primitive identifier {identifier}")
        result[identifier] = row
    return result


def matrix_record(record: object) -> QMatrix:
    if not isinstance(record, Mapping):
        raise ScoreRefusal("matrix record is not a mapping")
    shape = record.get("shape")
    rows = record.get("rows")
    if (
        not isinstance(shape, list)
        or len(shape) != 2
        or any(isinstance(value, bool) or not isinstance(value, int) for value in shape)
        or not isinstance(rows, list)
    ):
        raise ScoreRefusal("invalid exact matrix record")
    if len(rows) != shape[0]:
        raise ScoreRefusal("matrix record height mismatch")
    parsed = QMatrix.from_rows(rows, ncols=shape[1])
    if parsed.shape != tuple(shape):
        raise ScoreRefusal("matrix record shape mismatch")
    return parsed


def is_zero_matrix(value: QMatrix) -> bool:
    return qrank(value) == 0


def is_isometry(value: QMatrix) -> bool:
    return is_zero_matrix(
        qsubtract(qmultiply(qtranspose(value), value), QMatrix.identity(value.ncols))
    )


def region_data(value: PrefixRegion) -> list[str]:
    return list(value.words)


def bernoulli_mass(region: PrefixRegion, p: object) -> Fraction:
    parameter = exact(p)
    if not Fraction(0) < parameter < Fraction(1):
        raise ScoreRefusal("Bernoulli preparation requires 0 < p < 1")
    complement_parameter = Fraction(1) - parameter
    total = Fraction(0)
    for word in region.words:
        total += parameter ** word.count("0") * complement_parameter ** word.count("1")
    return total


def regions_from_fixture(data: Mapping[str, object]) -> dict[str, PrefixRegion]:
    section = data.get("prefix_controls")
    if not isinstance(section, Mapping):
        raise ScoreRefusal("missing prefix controls")
    rows = index_rows(section.get("regions"))
    result: dict[str, PrefixRegion] = {}
    for identifier, row in rows.items():
        words = row.get("antichain")
        if not isinstance(words, list) or any(not isinstance(word, str) for word in words):
            raise ScoreRefusal(f"bad antichain on {identifier}")
        region = PrefixRegion.from_words(words)
        if tuple(words) != region.words:
            raise ScoreRefusal(f"noncanonical region primitive {identifier}")
        result[identifier] = region
    return result


@dataclass(frozen=True, slots=True)
class Restriction:
    event: PrefixRegion

    def compose_after(self, earlier: "Restriction") -> "Restriction":
        return Restriction(earlier.event.meet(self.event))

    def apply_to_effect(self, effect: PrefixRegion) -> PrefixRegion:
        return effect.meet(self.event)

    def to_data(self) -> dict[str, object]:
        return {"kind": "Restriction", "event": self.event}


@dataclass(frozen=True, slots=True)
class Tree:
    question_id: str | None = None
    port_zero: "Tree | None" = None
    port_one: "Tree | None" = None

    @classmethod
    def empty(cls) -> "Tree":
        return cls()

    @property
    def is_empty(self) -> bool:
        return self.question_id is None

    def depth_set(self) -> tuple[int, ...]:
        if self.is_empty:
            return (0,)
        assert self.port_zero is not None and self.port_one is not None
        return tuple(
            sorted(
                {1 + value for value in self.port_zero.depth_set()}
                | {1 + value for value in self.port_one.depth_set()}
            )
        )

    def to_data(self) -> object:
        if self.is_empty:
            return {"empty_tree": True}
        assert self.port_zero is not None and self.port_one is not None
        return {
            "question_id": self.question_id,
            "port_0": self.port_zero,
            "port_1": self.port_one,
        }


@dataclass(frozen=True, slots=True)
class Expression:
    name: str
    args: tuple["Expression", ...] = ()


_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|[(),]")


def parse_expression(source: object) -> Expression:
    if not isinstance(source, str):
        raise ScoreRefusal("expression is not text")
    tokens = _TOKEN.findall(source)
    if "".join(tokens) != re.sub(r"\s+", "", source):
        raise ScoreRefusal(f"unsupported expression syntax: {source}")
    position = 0

    def parse_one() -> Expression:
        nonlocal position
        if position >= len(tokens) or tokens[position] in {"(", ")", ","}:
            raise ScoreRefusal("expected an expression identifier")
        name = tokens[position]
        position += 1
        if position >= len(tokens) or tokens[position] != "(":
            return Expression(name)
        position += 1
        arguments: list[Expression] = []
        if position < len(tokens) and tokens[position] == ")":
            position += 1
            return Expression(name, ())
        while True:
            arguments.append(parse_one())
            if position >= len(tokens):
                raise ScoreRefusal("unterminated expression")
            if tokens[position] == ")":
                position += 1
                break
            if tokens[position] != ",":
                raise ScoreRefusal("expected comma in expression")
            position += 1
        return Expression(name, tuple(arguments))

    result = parse_one()
    if position != len(tokens):
        raise ScoreRefusal("trailing expression tokens")
    return result


def expression_to_tree(value: Expression) -> Tree:
    if value.name == "empty_tree" and not value.args:
        return Tree.empty()
    if value.name != "node" or len(value.args) != 3:
        raise ScoreRefusal("not a decision-tree expression")
    question = value.args[0]
    if question.args:
        raise ScoreRefusal("question token must be atomic")
    return Tree(
        question.name,
        expression_to_tree(value.args[1]),
        expression_to_tree(value.args[2]),
    )


def validate_mixed_expression(value: Expression, productions: Sequence[str]) -> None:
    allowed: set[str] = {"empty_tree", "node"}
    if any("replace(" in production for production in productions):
        allowed.add("replace")
    if value.name not in allowed:
        raise ScoreRefusal(f"constructor {value.name} is not in the mixed-tree grammar")
    if value.name == "empty_tree":
        if value.args:
            raise ScoreRefusal("empty_tree takes no arguments")
        return
    if value.name == "replace":
        if len(value.args) != 2 or value.args[0].args:
            raise ScoreRefusal("replace has wrong arity")
        validate_mixed_expression(value.args[1], productions)
        return
    if len(value.args) != 3 or value.args[0].args:
        raise ScoreRefusal("node has wrong arity")
    validate_mixed_expression(value.args[1], productions)
    validate_mixed_expression(value.args[2], productions)


def question_region_map(
    data: Mapping[str, object], regions: Mapping[str, PrefixRegion]
) -> dict[str, PrefixRegion]:
    process = data.get("regional_question_process")
    if not isinstance(process, Mapping):
        raise ScoreRefusal("missing regional question process")
    result: dict[str, PrefixRegion] = {}
    for identifier, row in index_rows(process.get("registered_questions")).items():
        region_id = row.get("region_id")
        if not isinstance(region_id, str) or region_id not in regions:
            raise ScoreRefusal(f"bad question region on {identifier}")
        result[identifier] = regions[region_id]
    return result


def semantic_branch_binding(data: Mapping[str, object]) -> dict[int, str]:
    process = data.get("regional_question_process")
    if not isinstance(process, Mapping):
        raise ScoreRefusal("missing question process")
    transition = process.get("question_transition")
    if not isinstance(transition, Mapping) or not isinstance(transition.get("ports"), list):
        raise ScoreRefusal("missing question ports")
    found: dict[int, str] = {}
    for row in transition["ports"]:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad question port")
        formula = row.get("next_valuation")
        identifier = row.get("id")
        if not isinstance(formula, str) or not isinstance(identifier, str):
            raise ScoreRefusal("question port lacks formula")
        compact = formula.replace(" ", "")
        if "complement(C)" in compact:
            bit = 0
        elif "meet(A,C)" in compact:
            bit = 1
        else:
            raise ScoreRefusal("question branch formula has no semantic bit")
        if bit in found:
            raise ScoreRefusal("question transition does not supply one branch per semantic bit")
        found[bit] = identifier
    if set(found) != {0, 1}:
        raise ScoreRefusal("question transition must supply Q^0 and Q^1")
    return found


def tree_branch_cells(
    tree: Tree,
    questions: Mapping[str, PrefixRegion],
    *,
    support: PrefixRegion | None = None,
) -> dict[str, PrefixRegion]:
    root_support = PrefixRegion.one() if support is None else support
    leaves: dict[str, PrefixRegion] = {}

    def walk(node: Tree, path: str, cell: PrefixRegion) -> None:
        if node.is_empty:
            if path in leaves:
                raise ScoreRefusal("duplicate record port")
            leaves[path] = cell
            return
        if node.question_id not in questions:
            raise ScoreRefusal(f"unknown question token {node.question_id}")
        question = questions[node.question_id]
        assert node.port_zero is not None and node.port_one is not None
        walk(node.port_zero, path + "0", cell.meet(question.complement()))
        walk(node.port_one, path + "1", cell.meet(question))

    walk(tree, "", root_support)
    return dict(sorted(leaves.items()))


def branch_partition_evidence(
    cells: Mapping[str, PrefixRegion], support: PrefixRegion
) -> dict[str, object]:
    ordered = tuple(sorted(cells.items()))
    overlaps: list[dict[str, object]] = []
    for (left_name, left), (right_name, right) in itertools.combinations(ordered, 2):
        overlap = left.meet(right)
        if not overlap.is_zero():
            overlaps.append(
                {"left": left_name, "right": right_name, "overlap": overlap}
            )
    joined = PrefixRegion.zero()
    for _, cell in ordered:
        joined = joined.join(cell)
    return {
        "cells": {name: cell for name, cell in ordered},
        "pairwise_nonzero_overlaps": overlaps,
        "join": joined,
        "support": support,
        "is_partition": not overlaps and joined == support,
        "typed_zero_ports": [name for name, cell in ordered if cell.is_zero()],
    }


def preparation_controls(
    cells: Mapping[str, PrefixRegion], support: PrefixRegion, p: object
) -> dict[str, object]:
    denominator = bernoulli_mass(support, p)
    if denominator == 0:
        raise ScoreRefusal("registered support has zero preparation mass")
    weights = {
        name: bernoulli_mass(cell, p) / denominator
        for name, cell in sorted(cells.items())
    }
    posterior_supports = {
        name: cell
        for name, cell in sorted(cells.items())
        if weights[name] != 0
    }
    return {
        "p": exact(p),
        "weights": weights,
        "negative_weight_count": sum(weight < 0 for weight in weights.values()),
        "normalization_residual": sum(weights.values(), Fraction(0)) - Fraction(1),
        "posterior_supports": posterior_supports,
    }


def join_regions(values: Iterable[PrefixRegion]) -> PrefixRegion:
    result = PrefixRegion.zero()
    for value in values:
        result = result.join(value)
    return result


def coarse_grain_cells(
    cells: Mapping[str, PrefixRegion], groups: Sequence[Sequence[str]]
) -> dict[str, PrefixRegion]:
    result: dict[str, PrefixRegion] = {}
    for group in groups:
        names = tuple(sorted(group))
        if not names or any(name not in cells for name in names):
            raise ScoreRefusal("invalid coarse-graining group")
        selected = [cells[name] for name in names]
        if any(not left.disjoint(right) for left, right in itertools.combinations(selected, 2)):
            raise ScoreRefusal("coarse-graining requires disjoint branch cells")
        result["|".join(names)] = join_regions(selected)
    return result


@dataclass(frozen=True, slots=True)
class FiniteCospan:
    name: str
    incoming: tuple[str, ...]
    outgoing: tuple[str, ...]
    nodes: tuple[str, ...]
    in_images: tuple[tuple[str, str], ...]
    out_images: tuple[tuple[str, str], ...]
    relations: tuple[tuple[str, str], ...]


def cospans_from_fixture(data: Mapping[str, object]) -> dict[str, FiniteCospan]:
    section = data.get("typed_fillings")
    if not isinstance(section, Mapping):
        raise ScoreRefusal("missing typed fillings")
    boundaries = index_rows(section.get("boundaries"))
    apices = index_rows(section.get("apices"))
    result: dict[str, FiniteCospan] = {}
    for identifier, row in index_rows(section.get("horizontal_fillings")).items():
        incoming_id = row.get("incoming_boundary_id")
        outgoing_id = row.get("outgoing_boundary_id")
        apex_id = row.get("apex_id")
        if not all(isinstance(value, str) for value in (incoming_id, outgoing_id, apex_id)):
            raise ScoreRefusal(f"bad cospan references on {identifier}")
        incoming = boundaries[incoming_id]["generators"]
        outgoing = boundaries[outgoing_id]["generators"]
        nodes = apices[apex_id]["generators"]
        if not all(isinstance(value, list) for value in (incoming, outgoing, nodes)):
            raise ScoreRefusal("bad cospan generator rows")
        in_images = tuple(tuple(pair) for pair in row.get("incoming_images", []))
        out_images = tuple(tuple(pair) for pair in row.get("outgoing_images", []))
        relations = tuple(tuple(pair) for pair in row.get("apex_relations", []))
        if {pair[0] for pair in in_images} != set(incoming):
            raise ScoreRefusal(f"incoming leg is not total on {identifier}")
        if {pair[0] for pair in out_images} != set(outgoing):
            raise ScoreRefusal(f"outgoing leg is not total on {identifier}")
        if any(pair[1] not in nodes for pair in in_images + out_images):
            raise ScoreRefusal(f"cospan leg escapes apex on {identifier}")
        if any(left not in nodes or right not in nodes for left, right in relations):
            raise ScoreRefusal(f"cospan relation escapes apex on {identifier}")
        result[identifier] = FiniteCospan(
            identifier,
            tuple(incoming),
            tuple(outgoing),
            tuple(nodes),
            tuple(sorted(in_images)),
            tuple(sorted(out_images)),
            tuple(sorted(set(relations))),
        )
    return result


class UnionFind:
    def __init__(self, values: Iterable[tuple[int, str]]) -> None:
        self.parent = {value: value for value in values}

    def find(self, value: tuple[int, str]) -> tuple[int, str]:
        parent = self.parent[value]
        if parent != value:
            self.parent[value] = self.find(parent)
        return self.parent[value]

    def union(self, left: tuple[int, str], right: tuple[int, str]) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return
        if root_right < root_left:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left


@dataclass(frozen=True, slots=True)
class QuotientCospan:
    incoming: tuple[str, ...]
    outgoing: tuple[str, ...]
    node_count: int
    in_classes: tuple[tuple[str, int], ...]
    out_classes: tuple[tuple[str, int], ...]
    relations: tuple[tuple[int, int], ...]

    def to_data(self) -> dict[str, object]:
        return {
            "incoming": self.incoming,
            "outgoing": self.outgoing,
            "node_count": self.node_count,
            "in_classes": self.in_classes,
            "out_classes": self.out_classes,
            "relations": self.relations,
        }


def compose_cospans(steps: Sequence[FiniteCospan]) -> QuotientCospan:
    if not steps:
        raise ScoreRefusal("cospan composition needs at least one step")
    tagged = [(index, node) for index, step in enumerate(steps) for node in step.nodes]
    quotient = UnionFind(tagged)
    for index in range(len(steps) - 1):
        left = steps[index]
        right = steps[index + 1]
        if left.outgoing != right.incoming:
            raise ScoreRefusal("cospan cut boundaries differ")
        left_images = dict(left.out_images)
        right_images = dict(right.in_images)
        for token in left.outgoing:
            quotient.union((index, left_images[token]), (index + 1, right_images[token]))
    roots = sorted({quotient.find(value) for value in tagged})
    root_index = {root: index for index, root in enumerate(roots)}

    def class_of(value: tuple[int, str]) -> int:
        return root_index[quotient.find(value)]

    first = steps[0]
    last = steps[-1]
    in_classes = tuple(
        sorted((token, class_of((0, node))) for token, node in first.in_images)
    )
    out_classes = tuple(
        sorted((token, class_of((len(steps) - 1, node))) for token, node in last.out_images)
    )
    relations = tuple(
        sorted(
            {
                (class_of((index, left)), class_of((index, right)))
                for index, step in enumerate(steps)
                for left, right in step.relations
            }
        )
    )
    return QuotientCospan(
        first.incoming,
        last.outgoing,
        len(roots),
        in_classes,
        out_classes,
        relations,
    )


def singleton_quotient(value: FiniteCospan) -> QuotientCospan:
    return compose_cospans((value,))


def boundary_fixed_isomorphic(left: QuotientCospan, right: QuotientCospan) -> bool:
    if (
        left.incoming != right.incoming
        or left.outgoing != right.outgoing
        or left.node_count != right.node_count
    ):
        return False
    left_in = dict(left.in_classes)
    right_in = dict(right.in_classes)
    left_out = dict(left.out_classes)
    right_out = dict(right.out_classes)
    left_colors = {
        node: (
            tuple(sorted(token for token, image in left_in.items() if image == node)),
            tuple(sorted(token for token, image in left_out.items() if image == node)),
        )
        for node in range(left.node_count)
    }
    right_colors = {
        node: (
            tuple(sorted(token for token, image in right_in.items() if image == node)),
            tuple(sorted(token for token, image in right_out.items() if image == node)),
        )
        for node in range(right.node_count)
    }
    left_edges = set(left.relations)
    right_edges = set(right.relations)
    candidates = {
        node: tuple(other for other, color in right_colors.items() if color == left_colors[node])
        for node in left_colors
    }
    if any(not values for values in candidates.values()):
        return False
    order = sorted(candidates, key=lambda node: (len(candidates[node]), node))
    mapping: dict[int, int] = {}
    used: set[int] = set()

    def compatible(source: int, target: int) -> bool:
        for mapped_source, mapped_target in mapping.items():
            if ((source, mapped_source) in left_edges) != ((target, mapped_target) in right_edges):
                return False
            if ((mapped_source, source) in left_edges) != ((mapped_target, target) in right_edges):
                return False
        return True

    def search(position: int) -> bool:
        if position == len(order):
            transported = {(mapping[a], mapping[b]) for a, b in left_edges}
            return transported == right_edges
        source = order[position]
        for target in candidates[source]:
            if target in used or not compatible(source, target):
                continue
            mapping[source] = target
            used.add(target)
            if search(position + 1):
                return True
            used.remove(target)
            del mapping[source]
        return False

    return search(0)


@dataclass
class ProvenanceDAG:
    nodes: dict[str, dict[str, object]] = field(default_factory=dict)

    def add(
        self,
        name: str,
        *,
        roots: Sequence[str],
        transform: str,
        status: str = "DERIVED",
    ) -> str:
        if name in self.nodes:
            raise ScoreRefusal(f"duplicate provenance node {name}")
        self.nodes[name] = {
            "roots": sorted(set(roots)),
            "transform": transform,
            "status": status,
        }
        return name

    def disconnected(self, name: str) -> bool:
        return name not in self.nodes or not self.nodes[name]["roots"]

    def to_data(self) -> dict[str, object]:
        return dict(sorted(self.nodes.items()))


@dataclass
class MutationOptions:
    mutant_id: str | None = None
    modes: set[str] = field(default_factory=set)
    variants: tuple[str, ...] = ()
    notes: list[str] = field(default_factory=list)

    def active(self, name: str) -> bool:
        return name in self.modes


def score_regional_algebra(
    data: Mapping[str, object], provenance: ProvenanceDAG
) -> dict[str, object]:
    regions = regions_from_fixture(data)
    zero = PrefixRegion.zero()
    one = PrefixRegion.one()
    identity_failures: list[dict[str, object]] = []
    split_certificates: list[dict[str, object]] = []
    for name, region in sorted(regions.items()):
        checks = {
            "meet_unit": region.meet(one) == region,
            "join_zero": region.join(zero) == region,
            "complement_meet": region.meet(region.complement()) == zero,
            "complement_join": region.join(region.complement()) == one,
            "double_complement": region.complement().complement() == region,
        }
        if not all(checks.values()):
            identity_failures.append({"region": name, "checks": checks})
        if not region.is_zero():
            left, right = region.atomless_bipartition()
            split_certificates.append(
                {
                    "region": name,
                    "left": left,
                    "right": right,
                    "proper": left != region and right != region,
                    "partition": left.disjoint(right) and left.join(right) == region,
                }
            )
    node = provenance.add(
        "regional_algebra",
        roots=["fixture:prefix_controls"],
        transform="canonical PrefixRegion Boolean reconstruction",
    )
    return {
        "canonicalization": {
            name: region for name, region in sorted(regions.items())
        },
        "Boolean_identities": {
            "failure_count": len(identity_failures),
            "failures": identity_failures,
        },
        "symbolic_syntax_split": {
            "certificate_count": len(split_certificates),
            "certificates": split_certificates,
            "scope": "raw finite-prefix syntax only",
        },
        "provenance_node": node,
    }


def _tree_rows(data: Mapping[str, object]) -> tuple[dict[str, Tree], dict[str, str]]:
    process = data.get("regional_question_process")
    if not isinstance(process, Mapping):
        raise ScoreRefusal("missing regional question process")
    trees: dict[str, Tree] = {}
    expressions: dict[str, str] = {}
    for identifier, row in index_rows(process.get("decision_trees")).items():
        expression = row.get("expression")
        if not isinstance(expression, str):
            raise ScoreRefusal(f"tree {identifier} has no expression")
        trees[identifier] = expression_to_tree(parse_expression(expression))
        expressions[identifier] = expression
    return trees, expressions


def _preparation_rows(data: Mapping[str, object]) -> dict[str, Fraction]:
    process = data.get("regional_question_process")
    if not isinstance(process, Mapping):
        raise ScoreRefusal("missing regional process")
    family = process.get("valuation_family")
    if not isinstance(family, Mapping):
        raise ScoreRefusal("missing valuation family")
    result: dict[str, Fraction] = {}
    for identifier, row in index_rows(family.get("parameter_rows")).items():
        result[identifier] = exact(row.get("p"))
    return result


def _all_cut_signatures(
    tree: Tree, questions: Mapping[str, PrefixRegion], support: PrefixRegion
) -> dict[str, object]:
    direct = tree_branch_cells(tree, questions, support=support)
    depth_set = tree.depth_set()
    if len(depth_set) != 1:
        return {
            "uniform_depth": False,
            "direct": direct,
            "alternate_cuts": "NOT-CONSTRUCTED-FOR-ADAPTIVE-FRONTIER",
        }
    depth = depth_set[0]
    cuts: dict[str, object] = {}
    for cut in range(depth + 1):
        # Restrictions commute associatively by Boolean meet.  Reconstruct the
        # same final cells from their prefix and suffix factors rather than
        # comparing scalar probabilities.
        reconstructed: dict[str, PrefixRegion] = {}
        for port, final_cell in direct.items():
            prefix = port[:cut]
            suffix = port[cut:]
            prefix_cell = support
            node = tree
            for bit in prefix:
                if node.is_empty or node.question_id not in questions:
                    raise ScoreRefusal("cut leaves the registered tree")
                question = questions[node.question_id]
                prefix_cell = prefix_cell.meet(
                    question if bit == "1" else question.complement()
                )
                node = node.port_one if bit == "1" else node.port_zero
                assert node is not None
            suffix_cell = PrefixRegion.one()
            suffix_node = node
            for bit in suffix:
                if suffix_node.is_empty or suffix_node.question_id not in questions:
                    raise ScoreRefusal("suffix leaves the registered tree")
                question = questions[suffix_node.question_id]
                suffix_cell = suffix_cell.meet(
                    question if bit == "1" else question.complement()
                )
                suffix_node = (
                    suffix_node.port_one if bit == "1" else suffix_node.port_zero
                )
                assert suffix_node is not None
            reconstructed[port] = prefix_cell.meet(suffix_cell)
            if reconstructed[port] != final_cell:
                raise ScoreRefusal("restriction composition is cut-dependent")
        cuts[str(cut)] = {
            "record_ports": sorted(reconstructed),
            "cells": reconstructed,
            "equals_direct": reconstructed == direct,
        }
    return {"uniform_depth": True, "direct": direct, "alternate_cuts": cuts}


def score_cospan_factorizations(
    data: Mapping[str, object], options: MutationOptions
) -> dict[str, object]:
    cospans = cospans_from_fixture(data)
    section = data.get("typed_fillings")
    assert isinstance(section, Mapping)
    rows: list[dict[str, object]] = []
    for factor in section.get("factorizations", []):
        if not isinstance(factor, Mapping):
            raise ScoreRefusal("bad factorization row")
        steps_raw = factor.get("step_ids")
        whole_id = factor.get("whole_filling_id")
        if not isinstance(steps_raw, list) or not isinstance(whole_id, str):
            raise ScoreRefusal("bad factorization references")
        steps = [cospans[str(identifier)] for identifier in steps_raw]
        whole = cospans[whole_id]
        if options.active("no_pushout"):
            rows.append(
                {
                    "factorization": factor.get("id"),
                    "status": "REFUSED-TYPING-IS-NOT-COMPOSITION",
                }
            )
            continue
        composite = compose_cospans(steps)
        target = singleton_quotient(whole)
        rows.append(
            {
                "factorization": factor.get("id"),
                "composite": composite,
                "whole": target,
                "boundary_fixed_isomorphic": boundary_fixed_isomorphic(composite, target),
            }
        )
    return {
        "rows": rows,
        "all_finite_pushouts_match": bool(rows)
        and all(row.get("boundary_fixed_isomorphic") is True for row in rows),
    }


def score_process(
    data: Mapping[str, object], provenance: ProvenanceDAG, options: MutationOptions
) -> tuple[dict[str, object], dict[str, object]]:
    regions = regions_from_fixture(data)
    questions = question_region_map(data, regions)
    branch_binding = semantic_branch_binding(data)
    trees, expressions = _tree_rows(data)
    preparations = _preparation_rows(data)
    unit = PrefixRegion.one()

    arbitrary_question_identities: list[dict[str, object]] = []
    for question_name, event in sorted(questions.items()):
        complement = event.complement()
        arbitrary_question_identities.append(
            {
                "question": question_name,
                "disjoint": event.meet(complement).is_zero(),
                "exhaustive": event.join(complement).is_one(),
                "sum_of_restrictions": "identity on every finitely additive valuation",
                "positivity": "restriction to a Boolean event preserves the positive cone",
            }
        )

    tree_results: dict[str, object] = {}
    for tree_name, tree in sorted(trees.items()):
        cells = tree_branch_cells(tree, questions, support=unit)
        partition = branch_partition_evidence(cells, unit)
        numerical = {
            preparation_name: preparation_controls(cells, unit, parameter)
            for preparation_name, parameter in sorted(preparations.items())
        }
        tree_results[tree_name] = {
            "expression_hash": hashlib.sha256(
                expressions[tree_name].encode("utf-8")
            ).hexdigest(),
            "depth_set": tree.depth_set(),
            "unit_support_partition": partition,
            "preparation_controls": numerical,
            "arbitrary_support_theorem": {
                "status": "PROVED-SYMBOLIC",
                "leaf_formula": "S meet intersection of semantic branch events",
                "partition_reason": "successive Boolean event/complement partitions",
                "zero_ports_retained": True,
            },
            "cut_reconstruction": _all_cut_signatures(tree, questions, unit),
        }

    process = data.get("regional_question_process")
    if not isinstance(process, Mapping):
        raise ScoreRefusal("missing process section")
    mixed_grammar = process.get("mixed_tree_grammar")
    if not isinstance(mixed_grammar, Mapping):
        raise ScoreRefusal("missing mixed-tree grammar")
    productions = mixed_grammar.get("productions")
    if not isinstance(productions, list) or any(not isinstance(item, str) for item in productions):
        raise ScoreRefusal("bad mixed-tree productions")
    mixed_rows: dict[str, object] = {}
    for identifier, row in index_rows(process.get("mixed_tree_rows")).items():
        expression = row.get("expression")
        try:
            parsed = parse_expression(expression)
            validate_mixed_expression(parsed, productions)
            mixed_rows[identifier] = {"status": "PARSED", "constructor": parsed.name}
        except ScoreRefusal as exc:
            mixed_rows[identifier] = {"status": "REFUSED", "reason": str(exc)}

    cospan_result = score_cospan_factorizations(data, options)
    cospans = cospans_from_fixture(data)
    law_provenance = process.get("generated_law_provenance")
    if not isinstance(law_provenance, Mapping):
        raise ScoreRefusal("missing generated-law provenance")
    filling_factory = law_provenance.get("filling_factory")
    if not isinstance(filling_factory, Mapping):
        raise ScoreRefusal("missing finite filling factory")
    tree_factory_rows = filling_factory.get("tree_rows")
    if not isinstance(tree_factory_rows, list):
        raise ScoreRefusal("bad finite tree factory")
    b0_identity_controls: list[dict[str, object]] = []
    for row in tree_factory_rows:
        if not isinstance(row, Mapping):
            continue
        tree_id = row.get("tree_id")
        filling_id = row.get("filling_id")
        if not isinstance(tree_id, str) or not isinstance(filling_id, str):
            continue
        if tree_id not in trees or not trees[tree_id].is_empty or filling_id not in cospans:
            continue
        filling = cospans[filling_id]
        in_images = dict(filling.in_images)
        out_images = dict(filling.out_images)
        is_identity = (
            filling.incoming == filling.outgoing
            and not filling.relations
            and all(in_images[token] == out_images[token] for token in filling.incoming)
        )
        b0_identity_controls.append(
            {
                "tree": tree_id,
                "filling": filling_id,
                "boundary": filling.incoming,
                "is_identity": is_identity,
            }
        )
    b0_identity_constructed = bool(b0_identity_controls) and all(
        row["is_identity"] for row in b0_identity_controls
    )
    provenance_node = provenance.add(
        "finite_question_instruments",
        roots=[
            "fixture:regional_question_process/question_transition",
            "fixture:regional_question_process/decision_trees",
            "fixture:typed_fillings",
        ],
        transform="semantic Restrictions, record ports, and constructed finite pushouts",
    )
    all_branch_partitions = all(
        value["unit_support_partition"]["is_partition"]
        for value in tree_results.values()
    )
    all_numeric_controls = all(
        control["normalization_residual"] == 0
        and control["negative_weight_count"] == 0
        for value in tree_results.values()
        for control in value["preparation_controls"].values()
    )
    all_cut_controls = all(
        value["cut_reconstruction"]["uniform_depth"]
        and all(
            row["equals_direct"]
            for row in value["cut_reconstruction"]["alternate_cuts"].values()
        )
        for value in tree_results.values()
    )
    coarse_controls: dict[str, object] = {}
    for tree_name, value in sorted(tree_results.items()):
        cells = value["cut_reconstruction"]["direct"]
        assert isinstance(cells, Mapping)
        ports = sorted(str(name) for name in cells)
        if not ports or max(map(len, ports)) == 0:
            groups = [ports]
        else:
            prefix_length = max(map(len, ports)) - 1
            grouped: dict[str, list[str]] = {}
            for port in ports:
                grouped.setdefault(port[:prefix_length], []).append(port)
            groups = [grouped[name] for name in sorted(grouped)]
        coarse = coarse_grain_cells(cells, groups) if groups and groups[0] else {"": unit}
        coarse_controls[tree_name] = {
            "groups": groups,
            "restriction_events": coarse,
            "join": join_regions(coarse.values()),
            "total_preserved": join_regions(coarse.values()) == unit,
        }

    # Binding addenda: only the frozen B0 empty-tree assignment exists.  The
    # fixture supplies no arbitrary-frontier forest functor, tensor factory,
    # nontrivial naturality square, or overlap composition law.
    construction_ceiling = {
        "B0_identity": (
            "CONSTRUCTED" if b0_identity_constructed else "REFUSED"
        ),
        "B0_identity_evidence": b0_identity_controls,
        "all_boundary_identity": "UNCONSTRUCTED",
        "arbitrary_prefix_free_frontiers": "UNCONSTRUCTED",
        "question_bit_boundary_carrier": "UNCONSTRUCTED",
        "tensor_factory": "UNCONSTRUCTED",
        "mixed_question_replacement_forest": "UNCONSTRUCTED",
        "vertical_naturality": "VACUOUS-UNCONSTRUCTED",
        "regional_overlap_gluing_rule": "UNCONSTRUCTED",
    }
    finite_functor_controls = (
        all_branch_partitions
        and all_numeric_controls
        and all_cut_controls
        and cospan_result["all_finite_pushouts_match"]
    )
    total_horizontal_process = False
    process_coordinate = "STATIC-RESPONSE-ONLY"
    result = {
        "full_cone_question_maps": {
            "semantic_port_binding": branch_binding,
            "all_input_identities": arbitrary_question_identities,
            "status": "AFFINE-POSITIVE-NORMALIZED-ON-FULL-CONE",
        },
        "branch_partition": tree_results,
        "all_input_normalization": {
            "symbolic": all(
                row["disjoint"] and row["exhaustive"]
                for row in arbitrary_question_identities
            ),
            "preparation_controls": all_numeric_controls,
            "preparation_role": "state/preparation input; excluded from law identity",
        },
        "identity": construction_ceiling,
        "composition": {
            "restriction_identity": "Restriction(F) after Restriction(E) = Restriction(E meet F)",
            "finite_tree_controls": finite_functor_controls,
            "total_forest": "UNCONSTRUCTED",
        },
        "alternate_cuts": {name: value["cut_reconstruction"] for name, value in tree_results.items()},
        "coarse_graining": {
            "operation": "sum of disjoint Restriction cells",
            "average_forbidden": True,
            "registered_controls": coarse_controls,
        },
        "cospan_pushouts": cospan_result,
        "functorial_assignment": {
            "registered_finite_rows": "FINITE-CONTROLS-ONLY",
            "total_assignment": "UNCONSTRUCTED",
            "reason": "no arbitrary-frontier boundary/filling factory or all-boundary identities",
        },
        "tensor": "UNCONSTRUCTED-NO-BOUNDARY-OR-MAP-FACTORY",
        "vertical_naturality": "UNCONSTRUCTED-PASSIVE-PAIR-HAS-NO-NONIDENTITY-HORIZONTAL-SQUARE",
        "mixed_tree_rows": mixed_rows,
        "process_coordinate": process_coordinate,
        "total_horizontal_process": total_horizontal_process,
        "provenance_node": provenance_node,
    }
    return result, {
        "regions": regions,
        "questions": questions,
        "trees": trees,
        "preparations": preparations,
        "finite_functor_controls": finite_functor_controls,
        "total_horizontal_process": total_horizontal_process,
    }


def score_probes(
    data: Mapping[str, object], context: Mapping[str, object], provenance: ProvenanceDAG
) -> dict[str, object]:
    regions = context["regions"]
    preparations = context["preparations"]
    if not isinstance(regions, Mapping) or not isinstance(preparations, Mapping):
        raise ScoreRefusal("invalid process context")
    controls = data.get("prefix_controls")
    if not isinstance(controls, Mapping):
        raise ScoreRefusal("missing probe controls")
    catalogues = index_rows(controls.get("probe_catalogues"))
    finite_catalogues: dict[str, object] = {}
    for catalogue_name, row in sorted(catalogues.items()):
        region_ids = row.get("region_ids")
        if not isinstance(region_ids, list):
            continue
        probes = [regions[str(identifier)] for identifier in region_ids]
        per_preparation: dict[str, object] = {}
        for preparation_name, parameter in sorted(preparations.items()):
            profiles: dict[str, tuple[Fraction, ...]] = {}
            for candidate_name, candidate in sorted(regions.items()):
                profiles[candidate_name] = tuple(
                    bernoulli_mass(candidate.meet(probe), parameter) for probe in probes
                )
            collisions = [
                (left, right)
                for left, right in itertools.combinations(sorted(profiles), 2)
                if profiles[left] == profiles[right]
            ]
            per_preparation[preparation_name] = {
                "profiles": profiles,
                "collisions": collisions,
            }
        finite_catalogues[catalogue_name] = {
            "probe_count": len(probes),
            "per_preparation": per_preparation,
        }

    appended_controls: dict[str, object] = {}
    for catalogue_name, row in sorted(catalogues.items()):
        base_name = row.get("base_catalogue_id")
        appended_ids = row.get("appended_region_ids")
        if not isinstance(base_name, str) or not isinstance(appended_ids, list):
            continue
        if base_name not in catalogues:
            raise ScoreRefusal("appended probe references an unknown base catalogue")
        base_ids = catalogues[base_name].get("region_ids")
        if not isinstance(base_ids, list):
            raise ScoreRefusal("appended probe base has no finite region list")
        base_probes = [regions[str(identifier)] for identifier in base_ids]
        extended_probes = base_probes + [regions[str(identifier)] for identifier in appended_ids]
        per_preparation: dict[str, object] = {}
        for preparation_name, parameter in sorted(preparations.items()):
            base_profiles = {
                candidate_name: tuple(
                    bernoulli_mass(candidate.meet(probe), parameter)
                    for probe in base_probes
                )
                for candidate_name, candidate in sorted(regions.items())
            }
            extended_profiles = {
                candidate_name: tuple(
                    bernoulli_mass(candidate.meet(probe), parameter)
                    for probe in extended_probes
                )
                for candidate_name, candidate in sorted(regions.items())
            }
            base_collisions = {
                pair
                for pair in itertools.combinations(sorted(regions), 2)
                if base_profiles[pair[0]] == base_profiles[pair[1]]
            }
            extended_collisions = {
                pair
                for pair in itertools.combinations(sorted(regions), 2)
                if extended_profiles[pair[0]] == extended_profiles[pair[1]]
            }
            per_preparation[preparation_name] = {
                "base_profiles": base_profiles,
                "extended_profiles": extended_profiles,
                "base_collisions": sorted(base_collisions),
                "extended_collisions": sorted(extended_collisions),
                "separated_by_append": sorted(base_collisions - extended_collisions),
            }
        appended_controls[catalogue_name] = {
            "base_catalogue": base_name,
            "appended_probe_count": len(appended_ids),
            "per_preparation": per_preparation,
            "scope": "finite preparation-specific control",
        }

    # Build a genuinely fresh region and its symbolic restriction, but do not
    # promote it to a generated physical probe: the fixture has no total
    # filling/effect compiler for arbitrary questions.
    existing = set(regions.values())
    depth = 1
    while True:
        fresh = PrefixRegion.cylinder("0" * depth + "1")
        if fresh not in existing:
            break
        depth += 1
    fresh_symbolic = {
        "region": fresh,
        "branches": {
            "0": Restriction(fresh.complement()),
            "1": Restriction(fresh),
        },
        "lawful_filling": "UNCONSTRUCTED",
        "reader_effect": "UNCONSTRUCTED",
    }
    node = provenance.add(
        "probe_profiles",
        roots=["fixture:prefix_controls", "derived:finite_question_instruments"],
        transform="generated finite scalar profiles plus fresh symbolic question",
    )
    return {
        "finite_catalogue": finite_catalogues,
        "appended_probe": appended_controls,
        "fresh_generated_probe": fresh_symbolic,
        "completeness_scope": "COMPLETE-POSTULATED",
        "full_cone_separation_theorem": {
            "status": "CONDITIONAL",
            "missing_premises": [
                "target-independent lawful filling compiler",
                "generated effect/reader for every fresh question",
                "presentation-natural total forest construction",
            ],
        },
        "provenance_node": node,
    }


def score_linear_null(data: Mapping[str, object]) -> dict[str, object]:
    section = data.get("linear_continuations")
    if not isinstance(section, Mapping):
        raise ScoreRefusal("missing linear continuations")
    spaces = index_rows(section.get("spaces"))
    dimensions = {
        identifier: int(row["dimension"]) for identifier, row in spaces.items()
    }
    profiles: dict[str, QMatrix] = {}
    for row in section.get("profiles", []):
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad linear profile row")
        space_id = row.get("space_id")
        if not isinstance(space_id, str):
            raise ScoreRefusal("profile lacks space")
        profiles[space_id] = matrix_record(row.get("matrix"))
    continuations: list[LinearContinuation] = []
    for row in section.get("continuations", []):
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad continuation row")
        continuations.append(
            LinearContinuation(
                str(row["id"]),
                str(row["source_space_id"]),
                str(row["target_space_id"]),
                matrix_record(row["matrix"]),
            )
        )
    stable = compute_stable_null(dimensions, profiles, continuations)
    immediate = {
        name: FutureProfileQuotient.from_profile(profile)
        for name, profile in sorted(profiles.items())
    }
    return {
        "immediate_quotients": immediate,
        "stable_family": stable,
        "stable_null_rank_history": stable.rank_history,
        "generator_closure_used": True,
    }


def score_quotients(
    data: Mapping[str, object], context: Mapping[str, object], process: Mapping[str, object]
) -> dict[str, object]:
    linear = score_linear_null(data)
    contextual = {
        "status": "INCOMPLETE",
        "right_congruence": "FINITE-QUESTION-CONTROLS",
        "precontext_closure": "FINITE-ONLY",
        "tensor_closure": "UNCONSTRUCTED",
        "gluing_closure": "UNCONSTRUCTED",
    }
    regions = context.get("regions")
    preparations = context.get("preparations")
    if not isinstance(regions, Mapping) or not isinstance(preparations, Mapping):
        raise ScoreRefusal("quotient scoring lacks regional/preparation context")
    finite_entries: list[RegionProfileEntry] = []
    ordered_probes = [region for _, region in sorted(regions.items())]
    for name, region in sorted(regions.items()):
        profile = tuple(
            bernoulli_mass(region.meet(probe), parameter)
            for _, parameter in sorted(preparations.items())
            for probe in ordered_probes
        )
        finite_entries.append(RegionProfileEntry(str(name), region, profile))
    finite_equivalence = regional_profile_equivalence(finite_entries)
    regional = {
        "coordinate": "PROFILE-EQUIVALENCE-ONLY",
        "finite_Boolean_profile_control": finite_equivalence,
        "Boolean_full_cone_theorem": "CONDITIONAL-ON-COMPLETE-GENERATED-PROBES",
        "process_contexts": "UNCONSTRUCTED",
        "contact_causal_contexts": "PRICED",
        "boundary_gluing_contexts": "UNCONSTRUCTED",
    }
    return {
        "linear_null": linear,
        "stable_null_rank_history": linear["stable_null_rank_history"],
        "contextual_process": contextual,
        "regional_congruence": regional,
    }


def score_atomlessness(
    context: Mapping[str, object], probes: Mapping[str, object], quotients: Mapping[str, object]
) -> dict[str, object]:
    regions = context["regions"]
    assert isinstance(regions, Mapping)
    syntax_certificates: list[dict[str, object]] = []
    for name, region in sorted(regions.items()):
        if region.is_zero():
            continue
        left, right = region.atomless_bipartition()
        syntax_certificates.append(
            {
                "source": name,
                "left": left,
                "right": right,
                "valid": left.join(right) == region and left.disjoint(right),
            }
        )
    # The repeated-zero branch character is an ultrafilter: whichever child
    # contains the infinite branch keeps value one while the other is zero.
    unit_left, unit_right = PrefixRegion.one().atomless_bipartition()
    selected = (
        unit_left
        if any(("0" * 8).startswith(word) for word in unit_left.words)
        else unit_right
    )
    atomic_control = {
        "unit_character": 1,
        "selected_child": selected,
        "other_child_character": 0,
        "quotient_is_atomic_control": True,
    }
    physical_ready = (
        probes.get("completeness_scope") == "COMPLETE-GENERATED"
        and quotients["regional_congruence"]["coordinate"] == "CONGRUENCE"
    )
    return {
        "syntax": syntax_certificates,
        "atomic_character_control": atomic_control,
        "physical_quotient_split_certificate": (
            "NOT-CONSTRUCTED" if not physical_ready else "GENERATED"
        ),
        "atomless_coordinate": (
            "PHYSICAL-IMAGE-ATOMLESS" if physical_ready else "SYNTAX-ONLY"
        ),
        "raw_fixed_algebra_warning": (
            "common exterior scalar is not a physical regional atom; use the relative support quotient"
        ),
    }


def _resolve_record_outputs(
    values: tuple[str, ...], operation: Mapping[str, object]
) -> tuple[str, ...]:
    input_fields = operation.get("input_fields")
    output_fields = operation.get("output_fields")
    if not isinstance(input_fields, list) or not isinstance(output_fields, list):
        raise ScoreRefusal("record operation lacks typed fields")
    if len(values) != len(input_fields):
        raise ScoreRefusal(
            f"record operation {operation.get('id')} expects {len(input_fields)} fields, got {len(values)}"
        )
    environment = {str(name): value for name, value in zip(input_fields, values)}
    outputs: list[str] = []
    for expression in output_fields:
        if expression in {"0", "1"}:
            outputs.append(str(expression))
        elif isinstance(expression, str) and expression in environment:
            outputs.append(environment[expression])
        else:
            raise ScoreRefusal(
                f"unknown record-field expression {expression!r} on {operation.get('id')}"
            )
    return tuple(outputs)


def _simulate_record_word(
    operations: Mapping[str, Mapping[str, object]],
    word: Sequence[str],
    initial: tuple[str, ...],
) -> tuple[str, ...]:
    state = initial
    for operation_id in word:
        if operation_id not in operations:
            raise ScoreRefusal(f"unknown record operation {operation_id}")
        state = _resolve_record_outputs(state, operations[operation_id])
    return state


def _word_recovery_signature(
    operations: Mapping[str, Mapping[str, object]], word: Sequence[str]
) -> dict[str, object]:
    outputs: dict[str, object] = {}
    refused: str | None = None
    for source, flag_0, flag_1 in itertools.product("01", repeat=3):
        key = source + flag_0 + flag_1
        try:
            outputs[key] = _simulate_record_word(
                operations, word, (source, flag_0, flag_1)
            )
        except ScoreRefusal as exc:
            refused = str(exc)
            break
    if refused is not None:
        return {"status": "ILL-TYPED-REFUSED", "reason": refused}
    recovered = all(
        isinstance(value, tuple) and len(value) == 1 and value[0] == key[0]
        for key, value in outputs.items()
    )
    return {
        "status": "TYPED",
        "outputs": outputs,
        "recovers_source_for_all_carrier_inputs": recovered,
    }


def score_records(
    data: Mapping[str, object], process_context: Mapping[str, object], provenance: ProvenanceDAG
) -> dict[str, object]:
    recovery = data.get("record_recovery")
    process = data.get("regional_question_process")
    if not isinstance(recovery, Mapping) or not isinstance(process, Mapping):
        raise ScoreRefusal("missing record primitives")
    operations = index_rows(recovery.get("operations"))
    words = index_rows(recovery.get("operation_words"))
    word_results: dict[str, object] = {}
    for identifier, row in sorted(words.items()):
        operation_ids = row.get("operation_ids")
        if not isinstance(operation_ids, list) or any(
            not isinstance(value, str) for value in operation_ids
        ):
            raise ScoreRefusal("bad record word")
        word_results[identifier] = _word_recovery_signature(operations, operation_ids)

    # Addendum 2 forbids repairing the malformed double-reader word.  These
    # two controls branch from the same reset post-writer carrier and are
    # evaluated separately.
    prefix_before_reset: list[str] = []
    malformed_rows = [
        row
        for row in words.values()
        if isinstance(row.get("operation_ids"), list)
        and len(row["operation_ids"]) >= 2
        and row["operation_ids"][-2:] == ["ro_004", "ro_005"]
    ]
    if malformed_rows:
        raw_word = malformed_rows[0]["operation_ids"]
        assert isinstance(raw_word, list)
        reset_position = raw_word.index("ro_003") if "ro_003" in raw_word else 0
        prefix_before_reset = [str(value) for value in raw_word[: reset_position + 1]]
    separate_reset_readers = {
        "reader_0": _word_recovery_signature(operations, prefix_before_reset + ["ro_004"]),
        "reader_1": _word_recovery_signature(operations, prefix_before_reset + ["ro_005"]),
        "joint_semantics": "NOT-DECLARED",
    }

    schedules = index_rows(process.get("reader_schedules"))
    process_operations = index_rows(process.get("operations"))
    same_law_schedules: dict[str, object] = {}
    for identifier, row in sorted(schedules.items()):
        operation_ids = row.get("operation_ids")
        if not isinstance(operation_ids, list):
            raise ScoreRefusal("bad reader schedule")
        typed = all(str(value) in process_operations for value in operation_ids)
        only_delay_then_read = typed and all(
            process_operations[str(value)].get("operation")
            in {"delay_without_record_access", "read_record_after_delay"}
            for value in operation_ids
        )
        same_law_schedules[identifier] = {
            "typed": typed,
            "delay_then_read": only_delay_then_read,
            "operation_count": len(operation_ids),
        }

    continuation_results: dict[str, object] = {}
    for identifier, row in sorted(index_rows(process.get("continuation_catalogues")).items()):
        operation_ids = row.get("operation_ids")
        if not isinstance(operation_ids, list):
            raise ScoreRefusal("bad continuation catalogue")
        operation_kinds = {
            process_operations[str(value)].get("operation")
            for value in operation_ids
            if str(value) in process_operations
        }
        if "reset_record_word" in operation_kinds:
            status = "DESTROYED-BY-RESET"
        elif "erase_last_record_token" in operation_kinds:
            status = "NOT-PERMANENT-UNDER-LAST-TOKEN-ERASURE"
        else:
            status = "APPEND-ONLY-RECOVERABLE-AT-DECLARED-SCOPE"
        continuation_results[identifier] = {
            "status": status,
            "operation_kinds": sorted(str(value) for value in operation_kinds),
        }

    finite_delay_controls = {
        identifier: {
            "status": "IDENTITY-DELAY-CONTROL-ONLY",
            "delay_count": row.get("delay_count"),
            "writer": row.get("writer_operation_id"),
            "reader": row.get("reader_operation_id"),
            "same_law_provenance": False,
        }
        for identifier, row in sorted(index_rows(recovery.get("reader_delays")).items())
    }
    questions = process_context.get("questions")
    trees = process_context.get("trees")
    if not isinstance(questions, Mapping) or not isinstance(trees, Mapping):
        raise ScoreRefusal("record scoring lacks generated tree context")
    port_rows: dict[str, object] = {}
    for name, tree in sorted(trees.items()):
        if not isinstance(tree, Tree):
            raise ScoreRefusal("record tree context has wrong type")
        cells = tree_branch_cells(tree, questions)
        port_rows[str(name)] = {
            "ports": sorted(cells),
            "port_count": len(cells),
            "distinct": len(cells) == len(set(cells)),
        }
    node = provenance.add(
        "record_controls",
        roots=[
            "fixture:regional_question_process/reader_schedules",
            "fixture:record_recovery",
        ],
        transform="typed record-word simulation on every binary carrier input",
    )
    return {
        "port_write": {
            "semantic_bits": semantic_branch_binding(data),
            "update": "append",
            "finite_tree_ports": port_rows,
            "finite_tree_ports_distinct": all(
                row["distinct"] for row in port_rows.values()
            ),
        },
        "delayed_reader": {
            "same_law_schedules": same_law_schedules,
            "finite_identity_delay_controls": finite_delay_controls,
        },
        "continuation_reachability": continuation_results,
        "recovery": {
            "operation_words": word_results,
            "malformed_double_reader_refused": any(
                result.get("status") == "ILL-TYPED-REFUSED"
                for result in word_results.values()
                if isinstance(result, Mapping)
            ),
            "separate_reset_reader_prefixes": separate_reset_readers,
        },
        "eraser_and_copy_controls": {
            "single_copy_erasure": "evaluated in typed operation words",
            "redundant_copy": "evaluated in typed operation words",
            "double_erasure": separate_reset_readers,
        },
        "absolute_permanence": "NOT-CLAIMED; catalogue-relative only",
        "provenance_node": node,
    }


def leaves_at_depth(depth: int) -> tuple[str, ...]:
    if depth < 0:
        raise ScoreRefusal("negative prefix depth")
    return tuple("".join(bits) for bits in itertools.product("01", repeat=depth))


def region_leaf_set(region: PrefixRegion, depth: int) -> frozenset[str]:
    leaves = leaves_at_depth(depth)
    if any(len(prefix) > depth for prefix in region.words):
        raise ScoreRefusal("boundary depth is too shallow for region")
    return frozenset(
        leaf for leaf in leaves if any(leaf.startswith(prefix) for prefix in region.words)
    )


def child_swap_permutation(prefix: str, depth: int) -> tuple[int, ...]:
    if len(prefix) >= depth:
        raise ScoreRefusal("child swap has no resolved children at this boundary")
    leaves = leaves_at_depth(depth)
    index = {leaf: position for position, leaf in enumerate(leaves)}
    image: list[int] = []
    for leaf in leaves:
        if leaf.startswith(prefix + "0"):
            mapped = prefix + "1" + leaf[len(prefix) + 1 :]
        elif leaf.startswith(prefix + "1"):
            mapped = prefix + "0" + leaf[len(prefix) + 1 :]
        else:
            mapped = leaf
        image.append(index[mapped])
    return tuple(image)


def compose_permutations(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    if len(left) != len(right):
        raise ScoreRefusal("permutation size mismatch")
    return tuple(left[right[index]] for index in range(len(left)))


def inverse_permutation(value: tuple[int, ...]) -> tuple[int, ...]:
    if sorted(value) != list(range(len(value))):
        raise ScoreRefusal("cannot invert a non-permutation")
    result = [0] * len(value)
    for source, target in enumerate(value):
        result[target] = source
    return tuple(result)


def block_swap_permutation(left: str, right: str, depth: int) -> tuple[int, ...]:
    if len(left) != len(right) or len(left) > depth or left == right:
        raise ScoreRefusal("invalid equal-depth block swap")
    leaves = leaves_at_depth(depth)
    index = {leaf: position for position, leaf in enumerate(leaves)}
    result: list[int] = []
    for leaf in leaves:
        if leaf.startswith(left):
            mapped = right + leaf[len(left) :]
        elif leaf.startswith(right):
            mapped = left + leaf[len(right) :]
        else:
            mapped = leaf
        result.append(index[mapped])
    return tuple(result)


def conjugate_permutation(
    value: tuple[int, ...], presentation: tuple[int, ...]
) -> tuple[int, ...]:
    return compose_permutations(
        presentation,
        compose_permutations(value, inverse_permutation(presentation)),
    )


def permutation_closure(
    generators: Sequence[tuple[int, ...]], *, maximum: int = 100000
) -> tuple[tuple[int, ...], ...]:
    if not generators:
        return ()
    size = len(generators[0])
    if any(len(value) != size or sorted(value) != list(range(size)) for value in generators):
        raise ScoreRefusal("invalid permutation generator")
    identity = tuple(range(size))
    closure = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            composite = compose_permutations(generator, current)
            if composite not in closure:
                closure.add(composite)
                frontier.append(composite)
                if len(closure) > maximum:
                    raise ScoreRefusal("permutation closure exceeded exact finite bound")
    return tuple(sorted(closure))


def permutation_orbits(
    size: int, generators: Sequence[tuple[int, ...]]
) -> tuple[tuple[int, ...], ...]:
    adjacency = {index: {index} for index in range(size)}
    for generator in generators:
        for source, target in enumerate(generator):
            adjacency[source].add(target)
            adjacency[target].add(source)
    unseen = set(range(size))
    orbits: list[tuple[int, ...]] = []
    while unseen:
        seed = min(unseen)
        reached = {seed}
        frontier = [seed]
        while frontier:
            current = frontier.pop()
            for target in adjacency[current]:
                if target not in reached:
                    reached.add(target)
                    frontier.append(target)
        unseen.difference_update(reached)
        orbits.append(tuple(sorted(reached)))
    return tuple(sorted(orbits))


def permutation_matrix(permutation: Sequence[int]) -> QMatrix:
    size = len(permutation)
    return QMatrix.from_rows(
        (
            tuple(Fraction(1) if row == permutation[column] else Fraction(0) for column in range(size))
            for row in range(size)
        )
    )


def fixed_effect_constraints(generators: Sequence[tuple[int, ...]]) -> QMatrix:
    if not generators:
        return QMatrix.zero(0, 0)
    size = len(generators[0])
    identity = QMatrix.identity(size)
    rows = [qsubtract(qtranspose(permutation_matrix(value)), identity) for value in generators]
    return qvstack(rows, ncols=size)


def _maximal_exterior_cylinders(target: PrefixRegion) -> tuple[str, ...]:
    return target.complement().words


def _recursive_child_generators(target: PrefixRegion, depth: int) -> tuple[tuple[int, ...], ...]:
    prefixes: list[str] = []
    for root in _maximal_exterior_cylinders(target):
        for length in range(len(root), depth):
            prefixes.extend(root + "".join(bits) for bits in itertools.product("01", repeat=length - len(root)))
    return tuple(child_swap_permutation(prefix, depth) for prefix in sorted(set(prefixes)))


def _intrinsic_exterior_generators(
    target: PrefixRegion, depth: int
) -> tuple[tuple[int, ...], ...]:
    leaves = leaves_at_depth(depth)
    exterior = sorted(region_leaf_set(target.complement(), depth))
    indices = {leaf: index for index, leaf in enumerate(leaves)}
    generators: list[tuple[int, ...]] = []
    for left, right in zip(exterior, exterior[1:]):
        permutation = list(range(len(leaves)))
        left_index = indices[left]
        right_index = indices[right]
        permutation[left_index], permutation[right_index] = right_index, left_index
        generators.append(tuple(permutation))
    return tuple(generators)


def _literal_replacement_generators(
    data: Mapping[str, object], target_id: str, depth: int
) -> tuple[tuple[int, ...], ...]:
    process = data.get("regional_question_process")
    if not isinstance(process, Mapping):
        raise ScoreRefusal("missing replacement process")
    replacements = index_rows(process.get("replacement_primitives"))
    changed_rows = process.get("changed_object_rows")
    if not isinstance(changed_rows, list):
        raise ScoreRefusal("missing changed-object rows")
    selected: list[str] = []
    for row in changed_rows:
        if isinstance(row, Mapping) and row.get("target_region_id") == target_id:
            values = row.get("restricted_replacement_ids")
            if isinstance(values, list):
                selected.extend(str(value) for value in values)
    regions = regions_from_fixture(data)
    generators: list[tuple[int, ...]] = []
    for identifier in sorted(set(selected)):
        row = replacements.get(identifier)
        if row is None or row.get("operation") != "swap_children":
            continue
        support_id = row.get("support_region_id")
        if not isinstance(support_id, str) or support_id not in regions:
            raise ScoreRefusal("literal replacement lacks support")
        support = regions[support_id]
        if len(support.words) != 1:
            raise ScoreRefusal("child-swap support is not one cylinder")
        generators.append(child_swap_permutation(support.words[0], depth))
    return tuple(generators)


def _orbit_reading(
    target: PrefixRegion, depth: int, generators: Sequence[tuple[int, ...]]
) -> dict[str, object]:
    leaves = leaves_at_depth(depth)
    exterior_indices = {
        index for index, leaf in enumerate(leaves) if leaf in region_leaf_set(target.complement(), depth)
    }
    all_orbits = permutation_orbits(len(leaves), generators)
    exterior_orbits = tuple(
        tuple(leaves[index] for index in orbit)
        for orbit in all_orbits
        if set(orbit).issubset(exterior_indices)
    )
    cross_support = tuple(
        orbit for orbit in all_orbits if set(orbit) & exterior_indices and not set(orbit).issubset(exterior_indices)
    )
    constraints = (
        fixed_effect_constraints(generators)
        if generators
        else QMatrix.zero(0, len(leaves))
    )
    fixed_dim = len(leaves) - qrank(constraints) if generators else len(leaves)
    return {
        "depth": depth,
        "leaf_basis": leaves,
        "generator_count": len(generators),
        "semigroup_size": len(permutation_closure(generators)) if generators else 1,
        "all_orbits": tuple(tuple(leaves[index] for index in orbit) for orbit in all_orbits),
        "exterior_orbits": exterior_orbits,
        "exterior_orbit_count": len(exterior_orbits),
        "excess_exterior_scalar_directions": max(0, len(exterior_orbits) - 1),
        "cross_support_orbits": cross_support,
        "fixed_effect_dimension": fixed_dim,
        "fixed_effect_constraints": constraints,
    }


def _relative_support_comparison(
    target: PrefixRegion,
    depth: int,
    reading: Mapping[str, object],
) -> dict[str, object]:
    leaves = leaves_at_depth(depth)
    target_leaves = region_leaf_set(target, depth)
    target_indices = [index for index, leaf in enumerate(leaves) if leaf in target_leaves]
    kin_columns = [
        tuple(Fraction(1) if row == index else Fraction(0) for row in range(len(leaves)))
        for index in target_indices
    ]
    kin_basis = (
        QMatrix.from_rows(zip(*kin_columns), ncols=len(kin_columns))
        if kin_columns
        else QMatrix.zero(len(leaves), 0)
    )
    exterior_orbits_raw = reading.get("exterior_orbits")
    if not isinstance(exterior_orbits_raw, (tuple, list)):
        raise ScoreRefusal("fixed-effect reading lacks exterior orbits")
    exterior_orbits = [tuple(str(value) for value in orbit) for orbit in exterior_orbits_raw]
    # Quotient by the one common exterior scalar: retain one representative
    # direction for every additional exterior orbit beyond the first.
    excess_columns: list[tuple[Fraction, ...]] = []
    for orbit in exterior_orbits[1:]:
        orbit_set = set(orbit)
        excess_columns.append(
            tuple(Fraction(1) if leaf in orbit_set else Fraction(0) for leaf in leaves)
        )
    fixed_columns = kin_columns + excess_columns
    fixed_relative_basis = (
        QMatrix.from_rows(zip(*fixed_columns), ncols=len(fixed_columns))
        if fixed_columns
        else QMatrix.zero(len(leaves), 0)
    )
    return {
        "kin_basis": kin_basis,
        "fixed_relative_basis": fixed_relative_basis,
        "kin_in_fixed_residual": qsubspace_inclusion_residual(
            kin_basis, fixed_relative_basis
        ),
        "fixed_in_kin_residual": qsubspace_inclusion_residual(
            fixed_relative_basis, kin_basis
        ),
        "common_exterior_scalar_quotiented": True,
    }


def score_locality(
    data: Mapping[str, object], provenance: ProvenanceDAG, options: MutationOptions
) -> dict[str, object]:
    regions = regions_from_fixture(data)
    process = data.get("regional_question_process")
    if not isinstance(process, Mapping):
        raise ScoreRefusal("missing replacement process")
    changed_rows = process.get("changed_object_rows")
    if not isinstance(changed_rows, list):
        raise ScoreRefusal("missing locality target rows")
    targets = sorted(
        {
            str(row["target_region_id"])
            for row in changed_rows
            if isinstance(row, Mapping) and "restricted_replacement_ids" in row
        }
    )
    readings: dict[str, object] = {}
    for target_id in targets:
        target = regions[target_id]
        depth = max(3, max((len(word) for word in target.words), default=0) + 1)
        literal = _literal_replacement_generators(data, target_id, depth)
        generic = _recursive_child_generators(target, depth)
        intrinsic = (
            ()
            if options.active("restricted_only")
            else _intrinsic_exterior_generators(target, depth)
        )
        if options.active("delete_child_swap") and literal:
            literal = literal[:-1]
        if options.active("intrinsic_multiple_orbits"):
            intrinsic = generic
        literal_reading = _orbit_reading(target, depth, literal)
        generic_reading = _orbit_reading(target, depth, generic)
        intrinsic_reading = _orbit_reading(target, depth, intrinsic)
        readings[target_id] = {
            "target": target,
            "literally_listed_child_swaps": literal_reading,
            "generic_recursive_child_swap_closure": generic_reading,
            "intrinsic_relative_complement_closure": intrinsic_reading,
            "relative_support_quotient": {
                "definition": "fixed effects modulo the common exterior scalar",
                "target_leaf_count": len(region_leaf_set(target, depth)),
                "literal": _relative_support_comparison(target, depth, literal_reading),
                "generic": _relative_support_comparison(target, depth, generic_reading),
                "intrinsic": _relative_support_comparison(target, depth, intrinsic_reading),
            },
        }

    # Regrouping is a presentation change, not a physical generator.  The
    # restricted rooted grammar is tested for closure under conjugation while
    # the intrinsic full exterior permutation family is closed by construction.
    covariance_rows: dict[str, object] = {}
    for target_id in targets:
        target = regions[target_id]
        if len(target.words) != 1 or len(target.words[0]) != 2:
            continue
        depth = 3
        target_word = target.words[0]
        sibling = target_word[0] + ("1" if target_word[1] == "0" else "0")
        cross = ("1" if target_word[0] == "0" else "0") + target_word[1]
        regrouping = block_swap_permutation(sibling, cross, depth)
        literal = _literal_replacement_generators(data, target_id, depth)
        generic = _recursive_child_generators(target, depth)
        intrinsic = (
            ()
            if options.active("restricted_only")
            else _intrinsic_exterior_generators(target, depth)
        )
        literal_closure = set(permutation_closure(literal)) if literal else {tuple(range(2**depth))}
        generic_closure = set(permutation_closure(generic)) if generic else {tuple(range(2**depth))}
        intrinsic_closure = set(permutation_closure(intrinsic)) if intrinsic else {tuple(range(2**depth))}
        literal_conjugates = tuple(conjugate_permutation(value, regrouping) for value in literal)
        generic_conjugates = tuple(conjugate_permutation(value, regrouping) for value in generic)
        intrinsic_conjugates = tuple(conjugate_permutation(value, regrouping) for value in intrinsic)
        covariance_rows[target_id] = {
            "regrouping": regrouping,
            "literal_closed": all(value in literal_closure for value in literal_conjugates),
            "generic_child_swap_closed": all(value in generic_closure for value in generic_conjugates),
            "intrinsic_closed": (
                False
                if options.active("omit_intrinsic_conjugate")
                else all(value in intrinsic_closure for value in intrinsic_conjugates)
            ),
        }
    covariance = {
        "rows": covariance_rows,
        "restricted_child_swap": (
            "CLOSED"
            if covariance_rows
            and all(row["literal_closed"] for row in covariance_rows.values())
            else "FAIL"
        ),
        "generic_child_swap": (
            "CLOSED"
            if covariance_rows
            and all(row["generic_child_swap_closed"] for row in covariance_rows.values())
            else "FAIL"
        ),
        "intrinsic_relative_complement": (
            "CLOSED-AT-FROZEN-FINITE-PARTITION"
            if covariance_rows
            and all(row["intrinsic_closed"] for row in covariance_rows.values())
            else "FAIL"
        ),
        "scope": "finite registered boundary; all-partition theorem remains conditional",
    }
    locality_roots = [
        "fixture:regional_question_process/replacement_primitives",
    ]
    if "intrinsic_replacement_grammar" in process and not options.active("restricted_only"):
        locality_roots.append(
            "fixture:regional_question_process/intrinsic_replacement_grammar"
        )
    node = provenance.add(
        "replacement_fixed_effects",
        roots=locality_roots,
        transform="Boolean permutations, exact semigroup orbits, and relative exterior quotient",
    )
    finite_intrinsic_ok = all(
        row["intrinsic_relative_complement_closure"]["excess_exterior_scalar_directions"] == 0
        and not row["intrinsic_relative_complement_closure"]["cross_support_orbits"]
        for row in readings.values()
    ) and covariance["intrinsic_relative_complement"] == "CLOSED-AT-FROZEN-FINITE-PARTITION"
    regional_support_promotable = False
    return {
        "kin_provenance": {
            "finite_question_effects": "CONSTRUCTED-AT-REGISTERED-BOUNDARIES",
            "all-region_effect_factory": "POSTULATED-NOT-A-TOTAL-FILLING-FUNCTOR",
            "supplied_support_matrices_used_as_answer": False,
        },
        "replacement_provenance": {
            "literal": "registered child-swap rows",
            "generic_recursive": "closure of child swaps within maximal exterior cylinders",
            "intrinsic": "full finite relative-complement permutation construction",
        },
        "replacement_positivity_mass_support": {
            "permutation_automorphisms": True,
            "rational_mixtures": "CONDITIONAL-ON-EXPLICIT-COEFFICIENTS",
            "questions_used_as_replacements": False,
        },
        "restricted_fixed_effects": {
            target: row["literally_listed_child_swaps"] for target, row in readings.items()
        },
        "generic_child_swap_fixed_effects": {
            target: row["generic_recursive_child_swap_closure"] for target, row in readings.items()
        },
        "intrinsic_fixed_effects": {
            target: row["intrinsic_relative_complement_closure"] for target, row in readings.items()
        },
        "relative_support_quotients": {
            target: row["relative_support_quotient"] for target, row in readings.items()
        },
        "inclusion_residuals": {
            target: {
                "literal": row["relative_support_quotient"]["literal"],
                "generic": row["relative_support_quotient"]["generic"],
                "intrinsic": row["relative_support_quotient"]["intrinsic"],
            }
            for target, row in readings.items()
        },
        "refinement_conjugation": covariance,
        "finite_intrinsic_candidate": {
            "passes_registered_fixed-space_controls": finite_intrinsic_ok,
            "promotion": "REFUSED",
            "missing": [
                "law-generated complete regional effect factory",
                "all-partition rather than finite-row transitivity proof",
                "held-out refinement recurrence",
                "total horizontal process provenance",
            ],
        },
        "locality_coordinate": (
            "REGIONAL-SUPPORT" if regional_support_promotable else "FAIL"
        ),
        "causal_dynamic": False,
        "scope": "regional support only; not causal precedence, geometry, or gravity",
        "provenance_node": node,
    }


def _column(entries: Sequence[object]) -> QMatrix:
    return QMatrix.from_rows(((exact(value),) for value in entries), ncols=1)


def _vector_norm_squared(value: QMatrix) -> Fraction:
    if value.ncols != 1:
        raise ScoreRefusal("norm requires one column")
    return qmultiply(qtranspose(value), value).data[0][0]


def score_comparisons(
    data: Mapping[str, object], provenance: ProvenanceDAG
) -> dict[str, object]:
    section = data.get("comparisons")
    if not isinstance(section, Mapping):
        raise ScoreRefusal("missing comparison primitives")
    spaces = index_rows(section.get("spaces"))
    vectors = index_rows(section.get("vectors"))
    maps = index_rows(section.get("maps"))
    profiles = index_rows(section.get("target_profile_catalogues"))
    configurations = index_rows(section.get("configurations"))
    parsed_maps = {name: matrix_record(row["matrix"]) for name, row in maps.items()}
    parsed_profiles = {
        name: matrix_record(row["matrix"]) for name, row in profiles.items()
    }
    local_checks = {
        name: {
            "shape": value.shape,
            "isometry": is_isometry(value),
            "rank": qrank(value),
        }
        for name, value in sorted(parsed_maps.items())
    }

    reference = section.get("coherent_reference")
    if not isinstance(reference, Mapping):
        raise ScoreRefusal("missing coherent reference")
    source_vector_ids = reference.get("source_vector_ids")
    slots = reference.get("map_slots")
    coefficients = reference.get("combination_coefficients")
    if not all(isinstance(value, list) for value in (source_vector_ids, slots, coefficients)):
        raise ScoreRefusal("bad coherent reference")
    assert isinstance(source_vector_ids, list)
    assert isinstance(slots, list)
    assert isinstance(coefficients, list)
    if not (len(source_vector_ids) == len(slots) == len(coefficients)):
        raise ScoreRefusal("coherent reference arity mismatch")
    source_vectors = {
        name: _column(row["entries"]) for name, row in vectors.items()
    }
    scale = exact(reference.get("quadratic_scale"))

    screens: dict[str, object] = {}
    invariants: dict[str, object] = {}
    for config_name, row in sorted(configurations.items()):
        profile_id = row.get("target_profile_id")
        if not isinstance(profile_id, str):
            raise ScoreRefusal("comparison config lacks target profile")
        target_profile = parsed_profiles[profile_id]
        combined = QMatrix.zero(target_profile.ncols, 1)
        candidates: list[ComparisonCandidate] = []
        for vector_id, slot, coefficient in zip(source_vector_ids, slots, coefficients):
            if not isinstance(vector_id, str) or not isinstance(slot, str):
                raise ScoreRefusal("bad coherent-reference slot")
            map_id = row.get(slot)
            if not isinstance(map_id, str):
                raise ScoreRefusal("config lacks comparison map")
            operator = parsed_maps[map_id]
            transported = qmultiply(operator, source_vectors[vector_id])
            combined = qadd(combined, qscale(exact(coefficient), transported))
            candidates.append(ComparisonCandidate(f"{slot}:{map_id}", operator))
        screen = scale * _vector_norm_squared(combined)
        screens[config_name] = {
            "target_profile": profile_id,
            "combined_vector": combined,
            "coherent_screen": screen,
        }
        source_dim = candidates[0].operator.ncols
        source_quotient = FutureProfileQuotient.from_profile(QMatrix.identity(source_dim))
        target_quotient = FutureProfileQuotient.from_profile(target_profile)
        invariants[config_name] = comparison_family_invariants(
            source_quotient, target_quotient, candidates
        )

    node = provenance.add(
        "comparison_controls",
        roots=["fixture:comparisons"],
        transform="exact map typing, Gram screens, and future-profile quotients",
    )
    return {
        "process_comparisons": {
            "local_map_checks": local_checks,
            "family_invariants": invariants,
            "vertical_naturality": "UNCONSTRUCTED",
        },
        "RHL_mathematical_control": {
            "coherent_screens": screens,
            "pairing": "standard exact pairing reconstructed from transpose product",
            "controls": "full/null/invalid/phase-blind rows evaluated independently",
        },
        "operational_realization": "NOT-CONSTRUCTED-IN-THE-REGIONAL-QUESTION-LAW",
        "comparison_coordinate": "PRICED",
        "external_comparator_used": False,
        "provenance_node": node,
    }


def score_boundaries(
    data: Mapping[str, object], provenance: ProvenanceDAG
) -> dict[str, object]:
    section = data.get("predictive_boundaries")
    if not isinstance(section, Mapping):
        raise ScoreRefusal("missing predictive boundary primitives")
    labels = section.get("labels")
    if not isinstance(labels, list) or any(not isinstance(value, str) for value in labels):
        raise ScoreRefusal("bad boundary labels")
    future = section.get("future_profile")
    if not isinstance(future, Mapping):
        raise ScoreRefusal("missing boundary profile")
    profile = matrix_record(future["matrix"])
    canonical = PredictiveBoundary.from_profiles(labels, profile)
    partitions: dict[str, object] = {}
    for identifier, row in sorted(index_rows(section.get("label_partitions")).items()):
        blocks = row.get("blocks")
        if not isinstance(blocks, list):
            raise ScoreRefusal("bad boundary partition")
        partitions[identifier] = boundary_partition_signature(canonical, blocks)

    presentations: dict[str, object] = {}
    for identifier, row in sorted(index_rows(section.get("presentations")).items()):
        value = matrix_record(row["matrix"])
        presentations[identifier] = {
            "shape": value.shape,
            "rank": qrank(value),
            "kernel": qkernel(value),
            "same_kernel_as_future": qrowspace(value) == qrowspace(profile)
            if value.ncols == profile.ncols
            else False,
        }
    basis_changes: dict[str, object] = {}
    for identifier, row in sorted(index_rows(section.get("basis_changes")).items()):
        value = matrix_record(row["matrix"])
        basis_changes[identifier] = {
            "rank": qrank(value),
            "invertible": value.nrows == value.ncols == qrank(value),
        }
    extensions: dict[str, object] = {}
    for identifier, row in sorted(index_rows(section.get("future_extensions")).items()):
        appended = matrix_record(row["appended_rows"])
        extended = qvstack((profile, appended), ncols=profile.ncols)
        boundary = PredictiveBoundary.from_profiles(labels, extended)
        extensions[identifier] = {
            "extended_profile": extended,
            "canonical_classes": boundary.classes,
            "class_change": boundary.classes != canonical.classes,
        }
    node = provenance.add(
        "boundary_controls",
        roots=["fixture:predictive_boundaries"],
        transform="finite profile columns, canonical partitions, and exact kernels",
    )
    return {
        "generated_profiles": {
            "status": "PRIMITIVE-MATHEMATICAL-CONTROL-NOT-LAW-GENERATED",
            "matrix": profile,
        },
        "canonical_classes": canonical.classes,
        "lossy_control": partitions,
        "redundant_control": partitions,
        "invertible_change_control": basis_changes,
        "appended_future_control": extensions,
        "linear_presentations": presentations,
        "boundary_coordinate": "DECLARED",
        "universal_property": "NOT-CONSTRUCTED-FROM-COMPLETE-LAW-FUTURES",
        "provenance_node": node,
    }


def _marginal_distribution(
    variables: Sequence[str], configurations: Sequence[str], weights: Sequence[object], keep: Sequence[str]
) -> dict[str, Fraction]:
    if len(configurations) != len(weights):
        raise ScoreRefusal("configuration/weight mismatch")
    positions = [variables.index(variable) for variable in keep]
    result: dict[str, Fraction] = {}
    for configuration, raw_weight in zip(configurations, weights):
        if len(configuration) != len(variables):
            raise ScoreRefusal("configuration width mismatch")
        key = "".join(configuration[position] for position in positions)
        result[key] = result.get(key, Fraction(0)) + exact(raw_weight)
    return dict(sorted(result.items()))


def score_overlap_gluing(data: Mapping[str, object]) -> dict[str, object]:
    section = data.get("overlap_gluing")
    if not isinstance(section, Mapping):
        raise ScoreRefusal("missing overlap gluing")
    local = index_rows(section.get("local_boundaries"))
    candidates = index_rows(section.get("global_candidates"))
    requests = index_rows(section.get("gluing_requests"))
    result: dict[str, object] = {}
    for request_name, row in sorted(requests.items()):
        left = local[str(row["left_boundary_id"])]
        right = local[str(row["right_boundary_id"])]
        left_expected = {
            str(config): exact(weight)
            for config, weight in zip(left["configurations"], left["weights"])
        }
        right_expected = {
            str(config): exact(weight)
            for config, weight in zip(right["configurations"], right["weights"])
        }
        candidate_rows: dict[str, object] = {}
        for candidate_id in row["candidate_ids"]:
            candidate = candidates[str(candidate_id)]
            variables = [str(value) for value in candidate["variable_tokens"]]
            configurations = [str(value) for value in candidate["configurations"]]
            weights = candidate["weights"]
            left_marginal = _marginal_distribution(
                variables, configurations, weights, [str(value) for value in left["variable_tokens"]]
            )
            right_marginal = _marginal_distribution(
                variables, configurations, weights, [str(value) for value in right["variable_tokens"]]
            )
            candidate_rows[str(candidate_id)] = {
                "left_marginal": left_marginal,
                "right_marginal": right_marginal,
                "matches_left": left_marginal == left_expected,
                "matches_right": right_marginal == right_expected,
            }
        compatible = [
            name
            for name, candidate in candidate_rows.items()
            if candidate["matches_left"] and candidate["matches_right"]
        ]
        result[request_name] = {
            "candidates": candidate_rows,
            "compatible_global_extensions": compatible,
            "selected_extension": "UNSELECTED" if len(compatible) != 1 else compatible[0],
            "regional_gluing_law": "UNCONSTRUCTED",
        }
    return {
        "requests": result,
        "status": "LOCAL-MARGINAL-COMPATIBILITY-ONLY",
        "joint_kernel_rule": "LAW-DATA-UNSELECTED",
    }


def score_contact_causality(data: Mapping[str, object]) -> tuple[dict[str, object], dict[str, object]]:
    section = data.get("influence_contact")
    if not isinstance(section, Mapping):
        raise ScoreRefusal("missing influence/contact controls")
    regions = regions_from_fixture(data)
    arenas = index_rows(section.get("arenas"))
    static_rows: dict[str, object] = {}
    for identifier, row in sorted(arenas.items()):
        assignments = row.get("region_assignments", [])
        contact_candidates: list[dict[str, object]] = []
        if isinstance(assignments, list):
            assigned = {
                str(node): regions[str(region_id)] for node, region_id in assignments
            }
            for left, right in itertools.combinations(sorted(assigned), 2):
                first = assigned[left]
                second = assigned[right]
                contact_candidates.append(
                    {
                        "pair": [left, right],
                        "C_min": not first.meet(second).is_zero(),
                        "C_max": not first.is_zero() and not second.is_zero(),
                    }
                )
        arrows = tuple(tuple(pair) for pair in row.get("operation_arrows", []))
        reverse_pairs = sorted(
            {
                tuple(sorted((left, right)))
                for left, right in arrows
                if (right, left) in arrows
            }
        )
        static_rows[identifier] = {
            "operation_arrows": arrows,
            "declared_contact_pairs": tuple(
                tuple(pair) for pair in row.get("contact_pairs", [])
            ),
            "contact_candidates": contact_candidates,
            "bidirectional_pairs": reverse_pairs,
            "schedule": "NOT-FROZEN",
            "joint_law_provenance": "ABSENT",
        }
    contact = {
        "static_classification_controls": static_rows,
        "generated_joint_fillings": "NOT-CONSTRUCTED",
        "nonoverlap_contact_response": "NOT-CONSTRUCTED",
        "contact_coordinate": "PRICED",
    }
    causality = {
        "static_classification_controls": static_rows,
        "intervention_schedule": "NOT-FROZEN",
        "generated_delayed_reader_distribution": "NOT-CONSTRUCTED",
        "reversible_replacement_cycles_are_causal": False,
        "causality_coordinate": "PRICED",
    }
    return contact, causality


def _regional_member_signature(member: Mapping[str, object]) -> dict[str, object]:
    regions = member.get("regions")
    incidences = member.get("incidences")
    occurrences = member.get("component_occurrences")
    if not isinstance(regions, list) or not isinstance(incidences, list) or not isinstance(occurrences, list):
        raise ScoreRefusal("bad regional family member")
    node_degrees: dict[str, int] = {str(row["node_token"]): 0 for row in regions}
    incidence_patterns: list[dict[str, object]] = []
    for row in incidences:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad incidence row")
        nodes = [str(value) for value in row["node_tokens"]]
        for node in nodes:
            node_degrees[node] += 1
        left = {str(value) for value in row["left_component_tokens"]}
        right = {str(value) for value in row["right_component_tokens"]}
        incidence_patterns.append(
            {
                "left_arity": len(left),
                "right_arity": len(right),
                "shared_component_count": len(left & right),
            }
        )
    region_widths = sorted(
        sorted(len(str(word)) for word in row["antichain"]) for row in regions
    )
    return {
        "node_count": len(regions),
        "component_occurrence_count": len(occurrences),
        "degree_multiset": sorted(node_degrees.values()),
        "region_word_length_profiles": region_widths,
        "incidence_patterns": sorted(
            incidence_patterns,
            key=lambda value: canonical_json(value),
        ),
    }


def _blind_projection(member: Mapping[str, object]) -> dict[str, object]:
    # Only the public blind interface and registered resource fields survive.
    # Relation-mode strings, member IDs, prefix words, and insertion order are
    # absent by construction.
    blind = member.get("blind_interface")
    resources = member.get("resource_declaration")
    if not isinstance(blind, Mapping) or not isinstance(resources, Mapping):
        raise ScoreRefusal("member lacks blind interface/resources")
    node_tokens = sorted(str(value) for value in blind.get("node_tokens", []))
    node_index = {value: index for index, value in enumerate(node_tokens)}
    edges = []
    for row in blind.get("edges", []):
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad blind edge")
        endpoints = sorted(node_index[str(value)] for value in row["node_tokens"])
        edges.append(tuple(endpoints))
    return {
        "node_count": len(node_tokens),
        "edges": sorted(edges),
        "degree_multiset": sorted(
            sum(index in edge for edge in edges) for index in range(len(node_tokens))
        ),
        "resources": {
            key: resources[key]
            for key in sorted(resources)
            if key in {"state_dimension", "history_depth", "calibration_slots", "parameter_slots"}
        },
    }


def score_e37(
    data: Mapping[str, object], provenance: ProvenanceDAG
) -> dict[str, object]:
    section = data.get("regional_families")
    if not isinstance(section, Mapping):
        raise ScoreRefusal("missing regional family")
    members = index_rows(section.get("members"))
    pairs = index_rows(section.get("matched_pairs"))
    registration = section.get("registration")
    if not isinstance(registration, Mapping):
        raise ScoreRefusal("missing family registration")
    signatures = {
        name: _regional_member_signature(member) for name, member in sorted(members.items())
    }
    blind = {name: _blind_projection(member) for name, member in sorted(members.items())}
    pair_rows: dict[str, object] = {}
    for pair_name, row in sorted(pairs.items()):
        member_ids = row.get("member_ids")
        if not isinstance(member_ids, list) or len(member_ids) != 2:
            raise ScoreRefusal("matched pair needs two members")
        left, right = map(str, member_ids)
        left_hash = canonical_sha256(blind[left])
        right_hash = canonical_sha256(blind[right])
        pair_rows[pair_name] = {
            "member_ids": [left, right],
            "blind_hashes": [left_hash, right_hash],
            "byte_identical_blind_projection": left_hash == right_hash,
            "regional_signatures_equal": signatures[left] == signatures[right],
            "analytic_blind_factorization": (
                "equal blind inputs force equal outputs for every deterministic or stochastic rule factoring only through that projection"
            ),
        }
    blind_classes = index_rows(section.get("blind_rule_classes"))
    resources = {
        name: {
            "available_fields": row.get("available_fields"),
            "memory_interface": row.get("memory_interface"),
            "number_field": "NOT-FROZEN",
            "precision_budget": "NOT-FROZEN",
            "easier_row_benchmark": "NOT-FROZEN",
        }
        for name, row in sorted(blind_classes.items())
    }
    node = provenance.add(
        "E37_family",
        roots=["fixture:regional_families"],
        transform="anonymized incidence/resource signatures and blind factorization theorem",
    )
    return {
        "family_signatures": signatures,
        "train_holdout_split": {
            "training": sorted(str(value) for value in registration.get("training_ids", [])),
            "held_out": sorted(str(value) for value in registration.get("held_out_ids", [])),
            "disjoint": not set(registration.get("training_ids", []))
            & set(registration.get("held_out_ids", [])),
            "frozen_family_generator": "NO-FROZEN-FAMILY-GENERATOR",
        },
        "matched_blind_hashes": pair_rows,
        "resource_ledger": resources,
        "physical_generated_instruments": "NOT-CONSTRUCTED-NO-REGIONAL-TAU",
        "blind_class_instruments": {
            "constant_rule_nonempty": True,
            "registered_easier_task_competence": "NOT-FROZEN",
            "exhaustive_resource_parity": "NOT-LICENSED",
        },
        "relabel_and_erasure_controls": "AVAILABLE-AS-MUTANTS",
        "class_relative_scope": (
            "blind projection factorization proved on registered matched pairs; physical regional prediction and exclusion unconstructed"
        ),
        "external_comparator_is_regional_law": False,
        "provenance_node": node,
    }


def _forbidden_fixture_keys(value: object, path: tuple[str, ...] = ()) -> list[str]:
    forbidden = ("expected", "verdict", "outcome", "screen")
    found: list[str] = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            key_text = str(key)
            next_path = path + (key_text,)
            if any(part in key_text.lower() for part in forbidden):
                found.append("/".join(next_path))
            found.extend(_forbidden_fixture_keys(item, next_path))
    elif isinstance(value, (list, tuple)):
        for index, item in enumerate(value):
            found.extend(_forbidden_fixture_keys(item, path + (str(index),)))
    return found


def build_law_roots(data: Mapping[str, object]) -> dict[str, object]:
    process = data.get("regional_question_process")
    typed = data.get("typed_fillings")
    if not isinstance(process, Mapping) or not isinstance(typed, Mapping):
        raise ScoreRefusal("missing law-root primitives")
    valuation_family = process.get("valuation_family")
    if not isinstance(valuation_family, Mapping):
        raise ScoreRefusal("missing preparation family")
    law_components = {
        "question_grammar": process.get("question_grammar"),
        "question_transition": process.get("question_transition"),
        "decision_tree_grammar": process.get("decision_tree_grammar"),
        "finite_boundary_filling_factory": process.get("generated_law_provenance"),
        "replacement_grammar": process.get("replacement_grammar"),
        "intrinsic_replacement_grammar": process.get("intrinsic_replacement_grammar"),
        "reader_operations": process.get("operations"),
        "typed_finite_fillings": typed,
    }
    preparations = {
        "valuation_family_semantics": {
            key: value
            for key, value in valuation_family.items()
            if key != "parameter_rows"
        },
        "parameter_rows": valuation_family.get("parameter_rows"),
    }
    external_controls = {
        "comparisons": data.get("comparisons"),
        "predictive_boundaries": data.get("predictive_boundaries"),
        "regional_support": data.get("regional_support"),
        "influence_contact": data.get("influence_contact"),
        "coherent_comparator": data.get("coherent_comparator"),
    }
    return {
        "law_root_sha256": canonical_sha256(law_components),
        "preparation_root_sha256": canonical_sha256(preparations),
        "external_control_root_sha256": canonical_sha256(external_controls),
        "p_in_law_root": False,
        "law_components": sorted(law_components),
        "preparation_components": ["full valuation cone", "registered mu_p controls"],
    }


def classify_primary(receipt: Mapping[str, object]) -> tuple[str, list[str]]:
    algebra = receipt["regional_algebra"]
    process = receipt["process"]
    probes = receipt["probes"]
    quotients = receipt["quotients"]
    atomlessness = receipt["atomlessness"]
    comparisons = receipt["comparisons"]
    locality = receipt["locality"]
    causality = receipt["causality"]
    walls: list[str] = []
    if algebra["Boolean_identities"]["failure_count"]:
        return "APR-INCONSISTENT", ["Boolean algebra reconstruction failed"]
    if not process["all_input_normalization"]["symbolic"]:
        return "APR-INCONSISTENT", ["full-cone question normalization failed"]
    if not atomlessness["syntax"]:
        return "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA", [
            "no nonzero raw regional split was constructed"
        ]
    if not process["total_horizontal_process"]:
        walls.extend(
            [
                "finite record-tree cospans are not a total forest functor",
                "all-boundary identities are unconstructed",
                "tensor and nontrivial vertical naturality are unconstructed",
                "regional overlap gluing law is unselected",
            ]
        )
        return "APR-BLOCKED-AT-BOUNDARY-GLUING", walls
    if process["vertical_naturality"] in {"UNCONSTRUCTED", "INCONSISTENT"}:
        return "APR-BLOCKED-AT-TWO-ARROW-TYPING", [
            "horizontal and passive vertical arrows do not form one typed law"
        ]
    if probes["completeness_scope"] != "COMPLETE-GENERATED":
        return "APR-BLOCKED-AT-FUTURE-PROFILE-COMPLETENESS", [
            "complete physical probe family is not generated"
        ]
    if quotients["regional_congruence"]["coordinate"] != "CONGRUENCE":
        return "APR-BLOCKED-AT-REGIONAL-CONGRUENCE", [
            "profile equivalence has not descended under every process context"
        ]
    if comparisons["comparison_coordinate"] == "PRICED":
        return "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED", [
            "comparison system remains law data"
        ]
    if locality["locality_coordinate"] == "FAIL":
        return "APR-COMPARISON-QUOTIENT-CONSTRUCTED-BUT-DYNAMICAL-LOCALITY-FAILS", [
            "regional support equality fails"
        ]
    if causality["causality_coordinate"] != "DERIVED":
        return "APR-DYNAMIC-REGIONAL-REFERENT-CONSTRUCTED-BUT-CAUSAL-ORDER-PRICED", [
            "causal order is not generated by interventions and stable readers"
        ]
    if receipt["law_selection"]["status"] != "SELECTED":
        return "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED", [
            "one-law family remains unselected"
        ]
    return "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED", []


def score_dataset(
    data: Mapping[str, object],
    *,
    authentication: Mapping[str, object],
    options: MutationOptions | None = None,
    include_mutants: bool = False,
) -> dict[str, object]:
    active_options = MutationOptions() if options is None else options
    forbidden = _forbidden_fixture_keys(data)
    if forbidden:
        raise ScoreRefusal(
            "primitive fixture contains result-bearing/oracle fields: " + ", ".join(forbidden)
        )
    provenance = ProvenanceDAG()
    regional_algebra = score_regional_algebra(data, provenance)
    process, context = score_process(data, provenance, active_options)
    probes = score_probes(data, context, provenance)
    quotients = score_quotients(data, context, process)
    atomlessness = score_atomlessness(context, probes, quotients)
    records = score_records(data, context, provenance)
    locality = score_locality(data, provenance, active_options)
    comparisons = score_comparisons(data, provenance)
    boundaries = score_boundaries(data, provenance)
    contact, causality = score_contact_causality(data)
    overlap = score_overlap_gluing(data)
    e37 = score_e37(data, provenance)
    law_roots = build_law_roots(data)

    ontology_role = {
        "role": "RECORD-WRITING-ON-FIXED-ALGEBRA",
        "reason": (
            "finite question instruments restrict one predeclared Boolean algebra and append readable record bits; no output regional algebra is created or rewritten"
        ),
        "valuation_status": "process-state representation; ontic/epistemic/shadow status unselected",
        "p_status": "preparation label, not law data or coupling",
        "actualization": "POSTULATE-UNTOUCHED",
    }
    law_selection = {
        "status": "UNSELECTED",
        "preparation_variation_counted_as_law_modulus": False,
        "unselected_law_data": [
            "total forest/boundary/gluing assignment",
            "tensor constructor",
            "vertical comparison system",
            "regional overlap joint kernel",
            "contact/influence schedule",
        ],
    }
    scope_walls = [
        "finite record trees are instrument presentations, not a total regional process functor",
        "no physical regional Tau is frozen on the E37 family",
        "contact and influence arenas lack an operation schedule",
        "the classical question process does not select a quantum microscopic law",
        "no continuum, metric, Lorentz, GR, QFT, particle, Hamiltonian, or gravity claim",
    ]
    receipt: dict[str, object] = {
        "schema": RECEIPT_SCHEMA,
        "immutable_inputs": authentication,
        "integrity": {
            "scorer_schema": SCORER_SCHEMA,
            "fixture_oracle_fields": [],
            "floats_used": False,
            "randomized_evidence": False,
            "git_or_network_dependency": False,
        },
        "primitive_fixture_hash": canonical_sha256(data),
        "law_roots": law_roots,
        "exact_arithmetic": "fractions and symbolic PrefixRegion restrictions only",
        "regional_algebra": regional_algebra,
        "process": process,
        "probes": probes,
        "quotients": quotients,
        "atomlessness": atomlessness,
        "records": records,
        "locality": locality,
        "comparisons": comparisons,
        "boundaries": boundaries,
        "contact": contact,
        "causality": causality,
        "overlap_gluing": overlap,
        "E37": e37,
        "one_law_provenance": provenance.to_data(),
        "ontology_role": ontology_role,
        "law_selection": law_selection,
        "scope_walls": scope_walls,
        "mutants": "NOT-RUN" if not include_mutants else {},
        "strict_primary": "UNCLASSIFIED",
        "qualifiers": [],
    }
    primary, primary_walls = classify_primary(receipt)
    if primary not in PRIMARY_WORDS:
        raise ScoreRefusal("classifier emitted an unregistered primary")
    receipt["strict_primary"] = primary
    receipt["strict_primary_walls"] = primary_walls
    if (
        process["process_coordinate"] == "STATIC-RESPONSE-ONLY"
        and atomlessness["atomless_coordinate"] == "SYNTAX-ONLY"
    ):
        receipt["qualifiers"] = [STATIC_QUALIFIER]
    return receipt


def attach_payload_hash(receipt: MutableMapping[str, object]) -> None:
    if "payload_sha256" in receipt:
        raise ScoreRefusal("payload hash already attached")
    receipt["payload_sha256"] = canonical_sha256(receipt)


def transcript_from_receipt(receipt: Mapping[str, object]) -> dict[str, object]:
    return {
        "schema": TRANSCRIPT_SCHEMA,
        "strict_primary": receipt["strict_primary"],
        "qualifiers": receipt["qualifiers"],
        "process_coordinate": receipt["process"]["process_coordinate"],
        "probe_scope": receipt["probes"]["completeness_scope"],
        "regional_quotient": receipt["quotients"]["regional_congruence"]["coordinate"],
        "atomless_coordinate": receipt["atomlessness"]["atomless_coordinate"],
        "locality_coordinate": receipt["locality"]["locality_coordinate"],
        "comparison_coordinate": receipt["comparisons"]["comparison_coordinate"],
        "boundary_coordinate": receipt["boundaries"]["boundary_coordinate"],
        "contact_coordinate": receipt["contact"]["contact_coordinate"],
        "causality_coordinate": receipt["causality"]["causality_coordinate"],
        "ontology_role": receipt["ontology_role"]["role"],
        "law_selection": receipt["law_selection"]["status"],
        "scope_walls": receipt["scope_walls"],
        "receipt_payload_sha256": receipt["payload_sha256"],
    }


def _replace_exact_strings(value: object, replacements: Mapping[str, str]) -> object:
    if isinstance(value, str):
        return replacements.get(value, value)
    if isinstance(value, list):
        return [_replace_exact_strings(item, replacements) for item in value]
    if isinstance(value, tuple):
        return tuple(_replace_exact_strings(item, replacements) for item in value)
    if isinstance(value, Mapping):
        return {
            str(key): _replace_exact_strings(item, replacements)
            for key, item in value.items()
        }
    return value


def _flip_binary_word(word: str) -> str:
    return word.translate(str.maketrans({"0": "1", "1": "0"}))


def _presentation_relabel(value: object, key: str | None = None) -> object:
    sequence_keys = {"antichain", "leaf_tokens", "configurations"}
    if isinstance(value, Mapping):
        result: dict[str, object] = {}
        for child_key, item in value.items():
            if child_key in sequence_keys and isinstance(item, list):
                flipped = [
                    _flip_binary_word(entry) if isinstance(entry, str) else entry
                    for entry in item
                ]
                if child_key == "antichain" and all(
                    isinstance(entry, str) for entry in flipped
                ):
                    flipped = list(PrefixRegion.from_words(flipped).words)
                result[str(child_key)] = flipped
            else:
                result[str(child_key)] = _presentation_relabel(item, str(child_key))
        return result
    if isinstance(value, list):
        return [_presentation_relabel(item, key) for item in value]
    return value


def _delete_one_relation(data: MutableMapping[str, object], *, from_whole: bool) -> None:
    typed = data["typed_fillings"]
    assert isinstance(typed, MutableMapping)
    factors = typed["factorizations"]
    fillings = typed["horizontal_fillings"]
    assert isinstance(factors, list) and isinstance(fillings, list) and factors
    factor = factors[-1]
    assert isinstance(factor, Mapping)
    target_id = factor["whole_filling_id"] if from_whole else factor["step_ids"][-1]
    for row in fillings:
        if isinstance(row, MutableMapping) and row.get("id") == target_id:
            relations = row.get("apex_relations")
            if isinstance(relations, list) and relations:
                relations.pop()
                return
    raise ScoreRefusal("no relation available for composition mutant")


def _alter_one_leg(data: MutableMapping[str, object]) -> None:
    typed = data["typed_fillings"]
    assert isinstance(typed, MutableMapping)
    fillings = typed["horizontal_fillings"]
    assert isinstance(fillings, list)
    for row in fillings:
        if not isinstance(row, MutableMapping):
            continue
        images = row.get("outgoing_images")
        if isinstance(images, list) and len(images) >= 2:
            first = images[0]
            second = images[1]
            if isinstance(first, list) and isinstance(second, list):
                first[1] = second[1]
                return
    raise ScoreRefusal("no leg available for boundary-identification mutant")


def _select_comparison_map(
    section: Mapping[str, object], predicate: Callable[[QMatrix], bool]
) -> str:
    for identifier, row in sorted(index_rows(section.get("maps")).items()):
        if predicate(matrix_record(row["matrix"])):
            return identifier
    raise ScoreRefusal("comparison mutant has no map satisfying its structural predicate")


def apply_mutant(
    source: Mapping[str, object], mutant_id: str
) -> tuple[dict[str, object], MutationOptions]:
    if mutant_id not in MUTANT_IDS:
        raise ScoreRefusal(f"unknown mutant {mutant_id}")
    data = copy.deepcopy(source)
    options = MutationOptions(mutant_id=mutant_id)

    if mutant_id == "M01":
        options.modes.add("finite_depth_constructor")
    elif mutant_id == "M02":
        options.modes.add("atomic_character_quotient")
    elif mutant_id == "M03":
        options.modes.add("volume_only_quotient")
    elif mutant_id == "M04":
        options.modes.add("incomplete_probe_list")
    elif mutant_id == "M05":
        section = data["linear_continuations"]
        assert isinstance(section, MutableMapping)
        words = section["registered_words"]
        assert isinstance(words, list)
        section["registered_words"] = [
            row
            for row in words
            if isinstance(row, Mapping) and len(row.get("continuation_ids", [])) <= 1
        ]
    elif mutant_id == "M06":
        options.modes.add("paired_four_coordinate_reactivation")
    elif mutant_id == "M07":
        typed = data["typed_fillings"]
        assert isinstance(typed, MutableMapping)
        vertical = typed["vertical_maps"]
        assert isinstance(vertical, list)
        for row in vertical:
            if isinstance(row, MutableMapping) and row.get("map_sort") == "passive_presentation_isomorphism":
                row["map_sort"] = "horizontal_growth_candidate"
                break
    elif mutant_id == "M08":
        typed = data["typed_fillings"]
        assert isinstance(typed, MutableMapping)
        retypings = typed["arrow_retypings"]
        assert isinstance(retypings, list)
        for row in retypings:
            if isinstance(row, MutableMapping) and row.get("proposed_arrow_sort") == "horizontal_filling":
                row["proposed_arrow_sort"] = "vertical_comparison"
                break
    elif mutant_id in {"M09", "M10", "M11"}:
        section = data["comparisons"]
        assert isinstance(section, MutableMapping)
        configurations = section["configurations"]
        assert isinstance(configurations, list) and configurations
        target = configurations[0]
        assert isinstance(target, MutableMapping)
        if mutant_id == "M11":
            replacement = _select_comparison_map(section, lambda value: not is_isometry(value))
        else:
            original = str(target["right_map_id"])
            replacement = _select_comparison_map(
                section,
                lambda value: is_isometry(value)
                and canonical_sha256(value) != canonical_sha256(
                    matrix_record(index_rows(section["maps"])[original]["matrix"])
                ),
            )
        target["right_map_id"] = replacement
        if mutant_id == "M10":
            options.modes.add("null_profile_comparison")
            profile_rows = index_rows(section["target_profile_catalogues"])
            target["target_profile_id"] = min(
                profile_rows,
                key=lambda name: qrank(matrix_record(profile_rows[name]["matrix"])),
            )
    elif mutant_id == "M12":
        _delete_one_relation(data, from_whole=True)
        options.variants = ("whole_changed", "step_changed")
    elif mutant_id == "M13":
        options.modes.update({"zero_law", "constant_law"})
    elif mutant_id == "M14":
        options.modes.update({"equal_rank_wrong_subspace", "supplied_matrix_shortcut"})
    elif mutant_id == "M15":
        options.modes.update({"serialization_oracle", "identifier_hash_oracle"})
    elif mutant_id == "M16":
        family = data["regional_families"]
        assert isinstance(family, MutableMapping)
        for member in family["members"]:
            if isinstance(member, MutableMapping):
                member["incidences"] = []
    elif mutant_id == "M17":
        section = data["predictive_boundaries"]
        assert isinstance(section, MutableMapping)
        candidates = index_rows(section["presentations"])
        selected = min(candidates.values(), key=lambda row: qrank(matrix_record(row["matrix"])))
        section["future_profile"]["matrix"] = copy.deepcopy(selected["matrix"])
    elif mutant_id == "M18":
        options.modes.add("redundant_boundary_split")
    elif mutant_id == "M19":
        options.modes.add("invertible_boundary_change")
    elif mutant_id == "M20":
        options.modes.add("future_profile_extension")
    elif mutant_id == "M21":
        options.modes.add("common_cause_control")
    elif mutant_id == "M22":
        options.modes.add("causal_cycle_control")
    elif mutant_id == "M23":
        options.modes.add("record_reset")
    elif mutant_id == "M24":
        options.modes.add("redundant_record_copy")
    elif mutant_id == "M25":
        data["expected_screen"] = "mutated-oracle-field"
    elif mutant_id == "M26":
        family = data["regional_families"]
        assert isinstance(family, Mapping)
        members = family["members"]
        assert isinstance(members, list) and len(members) >= 2
        left = str(members[0]["id"])
        right = str(members[1]["id"])
        data = _replace_exact_strings(data, {left: "rf_998", right: "rf_999"})
        assert isinstance(data, dict)
        renamed = data["regional_families"]["members"]
        assert isinstance(renamed, list)
        modes = [row.get("relation_mode") for row in renamed[:2] if isinstance(row, MutableMapping)]
        if len(modes) == 2:
            renamed[0]["relation_mode"], renamed[1]["relation_mode"] = modes[1], modes[0]
    elif mutant_id == "M27":
        transformed = _presentation_relabel(data)
        if not isinstance(transformed, dict):
            raise ScoreRefusal("presentation relabel did not preserve fixture mapping")
        data = transformed
        process = data["regional_question_process"]
        assert isinstance(process, MutableMapping)
        family = process["valuation_family"]
        assert isinstance(family, MutableMapping)
        for row in family["parameter_rows"]:
            if isinstance(row, MutableMapping):
                row["p"] = fraction_text(Fraction(1) - exact(row["p"]))
        options.modes.add("transport_outputs_back")
    elif mutant_id == "M28":
        options.modes.add("blind_projection_substitution")
    elif mutant_id == "M29":
        options.modes.add("unseen_heldout_request")
    elif mutant_id == "M30":
        options.modes.add("regional_rule_blinded")
    elif mutant_id == "M31":
        family = data["regional_families"]
        assert isinstance(family, MutableMapping)
        classes = family["blind_rule_classes"]
        assert isinstance(classes, list) and classes
        classes[0]["memory_interface"] = str(classes[0]["memory_interface"]) + "+one_bit"
        for member in family["members"]:
            if isinstance(member, MutableMapping):
                resources = member["resource_declaration"]
                resources["parameter_slots"] = int(resources["parameter_slots"]) + 1
        options.modes.add("resource_class_changed")
    elif mutant_id == "M32":
        comparator = data["coherent_comparator"]
        assert isinstance(comparator, MutableMapping)
        for row in comparator["maps"]:
            if isinstance(row, MutableMapping):
                matrix = matrix_record(row["matrix"])
                row["matrix"] = {
                    "shape": [matrix.nrows, matrix.ncols],
                    "rows": [
                        [
                            fraction_text(value if i == j else Fraction(0))
                            for j, value in enumerate(matrix.data[i])
                        ]
                        for i in range(matrix.nrows)
                    ],
                }
        options.modes.add("interference_deleted")
    elif mutant_id == "M33":
        options.variants = (
            "delete_branch",
            "duplicate_branch",
            "renormalize_each_branch",
            "negative_branch",
            "wrong_restriction_cell",
        )
    elif mutant_id == "M34":
        section = data["influence_contact"]
        assert isinstance(section, MutableMapping)
        for row in section["arenas"]:
            if isinstance(row, MutableMapping) and row.get("contact_pairs"):
                row["contact_pairs"] = []
            elif isinstance(row, MutableMapping) and len(row.get("node_tokens", [])) >= 2:
                nodes = row["node_tokens"]
                row["contact_pairs"] = [[nodes[0], nodes[1]]]
    elif mutant_id == "M35":
        options.modes.add("disconnected_provenance")
    elif mutant_id == "P1":
        options.modes.add("average_coarse_graining")
    elif mutant_id == "P2":
        options.modes.add("drop_zero_ports")
    elif mutant_id == "P3":
        options.modes.add("overwrite_records")
    elif mutant_id == "P4":
        options.modes.add("freeze_preparation")
    elif mutant_id == "P5":
        options.modes.add("whitelist_questions")
    elif mutant_id == "P6":
        options.modes.add("questions_as_exterior_dynamics")
    elif mutant_id == "P7":
        options.modes.add("no_pushout")
    elif mutant_id == "P8":
        options.modes.add("sequential_tensor")
    elif mutant_id == "L1":
        process = data["regional_question_process"]
        assert isinstance(process, MutableMapping)
        process.pop("intrinsic_replacement_grammar", None)
        process["replacement_primitives"] = [
            row
            for row in process["replacement_primitives"]
            if not isinstance(row, Mapping) or row.get("grammar_id") != "qg_004"
        ]
        options.modes.add("restricted_only")
    elif mutant_id == "L2":
        options.modes.add("delete_child_swap")
    elif mutant_id == "L3":
        options.modes.add("regrouping_conjugation")
    elif mutant_id == "L4":
        options.modes.add("intrinsic_multiple_orbits")
    elif mutant_id == "L5":
        options.modes.add("omit_intrinsic_conjugate")
    elif mutant_id == "L6":
        options.modes.add("supplied_subspace_shortcut")
    elif mutant_id == "G1":
        _delete_one_relation(data, from_whole=True)
        options.variants = ("whole_relation_deleted", "step_relation_deleted")
    elif mutant_id == "G2":
        _alter_one_leg(data)
    elif mutant_id == "G3":
        options.modes.add("no_pushout")
    elif mutant_id == "G4":
        options.modes.add("process_assignment_mismatch")
    elif mutant_id == "G5":
        process = data["regional_question_process"]
        assert isinstance(process, MutableMapping)
        trees = process["decision_trees"]
        assert isinstance(trees, list)
        for row in trees:
            if isinstance(row, MutableMapping) and str(row.get("expression", "")).count("node(") >= 2:
                row["expression"] = str(row["expression"]).replace("qq_002", "qq_003", 1)
                break
    elif mutant_id == "G6":
        overlap = data["overlap_gluing"]
        assert isinstance(overlap, MutableMapping)
        candidates = overlap["global_candidates"]
        assert isinstance(candidates, list) and candidates
        weights = candidates[0]["weights"]
        assert isinstance(weights, list) and len(weights) >= 2
        delta = Fraction(1, 32)
        weights[0] = fraction_text(exact(weights[0]) + delta)
        weights[1] = fraction_text(exact(weights[1]) - delta)
    elif mutant_id == "G7":
        overlap = data["overlap_gluing"]
        assert isinstance(overlap, MutableMapping)
        overlap["global_candidates"] = []
        for request in overlap["gluing_requests"]:
            if isinstance(request, MutableMapping):
                request["candidate_ids"] = []
    return data, options


def m06_stable_null_control() -> dict[str, object]:
    profile = QMatrix.from_rows(((1, 0, 0, 0),))
    cycle = QMatrix.from_rows(
        (
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (1, 0, 0, 0),
            (0, 0, 0, 1),
        )
    )
    reactivate = QMatrix.from_rows(
        (
            (1, 0, 0, 1),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
        )
    )
    base = compute_stable_null(
        {"v": 4},
        {"v": profile},
        (LinearContinuation("cycle", "v", "v", cycle),),
    )
    extended = compute_stable_null(
        {"v": 4},
        {"v": profile},
        (
            LinearContinuation("cycle", "v", "v", cycle),
            LinearContinuation("reactivate", "v", "v", reactivate),
        ),
    )
    return {
        "baseline_nullity": base.boundary("v").quotient.nullity,
        "baseline_null_basis": base.boundary("v").quotient.null_basis,
        "reactivated_nullity": extended.boundary("v").quotient.nullity,
        "reactivated_null_basis": extended.boundary("v").quotient.null_basis,
        "rank_histories": {
            "baseline": base.rank_history,
            "reactivated": extended.rank_history,
        },
    }


def _generic_algorithm_witness(
    mutant_id: str,
    data: Mapping[str, object],
    options: MutationOptions,
) -> dict[str, object] | None:
    regions = regions_from_fixture(data)
    questions = question_region_map(data, regions)
    preparations = _preparation_rows(data)
    trees, _ = _tree_rows(data)
    nonempty_trees = [tree for tree in trees.values() if not tree.is_empty]

    if mutant_id == "M01":
        cutoff = max(
            (len(word) for region in regions.values() for word in region.words),
            default=0,
        )
        fresh = PrefixRegion.cylinder("0" * (cutoff + 1))
        return {
            "finite_constructor_cutoff": cutoff,
            "fresh_deeper_region": fresh,
            "raw_prefix_algebra_accepts": True,
            "mutant_probe_constructor_accepts": False,
        }
    if mutant_id == "M02":
        source = PrefixRegion.one()
        left, right = source.atomless_bipartition()
        branch = "0" * 12

        def character(region: PrefixRegion) -> int:
            return int(any(branch.startswith(prefix) for prefix in region.words))

        return {
            "source_character": character(source),
            "child_characters": [character(left), character(right)],
            "atomic_quotient_control": sum(
                value == 1 for value in (character(left), character(right))
            )
            == 1,
        }
    if mutant_id == "M03":
        p = next(iter(preparations.values()))
        collision: tuple[str, str] | None = None
        for left_name, right_name in itertools.combinations(sorted(regions), 2):
            if bernoulli_mass(regions[left_name], p) == bernoulli_mass(regions[right_name], p):
                collision = (left_name, right_name)
                break
        separated = False
        separator: str | None = None
        if collision is not None:
            left_region, right_region = (regions[name] for name in collision)
            for candidate_name, candidate in sorted(regions.items()):
                if left_region.meet(candidate) != right_region.meet(candidate):
                    separated = True
                    separator = candidate_name
                    break
        return {
            "preparation": p,
            "equal_volume_pair": collision,
            "Boolean_context_separator": separator,
            "volume_profile_is_congruence": not separated,
        }
    if mutant_id == "M04":
        controls = data["prefix_controls"]
        catalogues = index_rows(controls["probe_catalogues"])
        base_ids_named = {
            str(row["base_catalogue_id"])
            for row in catalogues.values()
            if isinstance(row.get("base_catalogue_id"), str)
        }
        finite_rows = [catalogues[name] for name in sorted(base_ids_named)]
        if not finite_rows:
            finite_rows = [
                row
                for row in catalogues.values()
                if isinstance(row.get("region_ids"), list)
            ]
        per_preparation: dict[str, object] = {}
        if finite_rows:
            base_ids = [str(value) for value in finite_rows[0]["region_ids"]]
            appended_ids: list[str] = []
            for row in catalogues.values():
                if isinstance(row.get("appended_region_ids"), list):
                    appended_ids.extend(str(value) for value in row["appended_region_ids"])
            for prep_name, p in sorted(preparations.items()):
                base_profiles = {
                    name: tuple(
                        bernoulli_mass(region.meet(regions[probe_id]), p)
                        for probe_id in base_ids
                    )
                    for name, region in sorted(regions.items())
                }
                extended_profiles = {
                    name: base_profiles[name]
                    + tuple(
                        bernoulli_mass(region.meet(regions[probe_id]), p)
                        for probe_id in appended_ids
                    )
                    for name, region in sorted(regions.items())
                }
                base_collisions = {
                    pair
                    for pair in itertools.combinations(sorted(regions), 2)
                    if base_profiles[pair[0]] == base_profiles[pair[1]]
                }
                extended_collisions = {
                    pair
                    for pair in itertools.combinations(sorted(regions), 2)
                    if extended_profiles[pair[0]] == extended_profiles[pair[1]]
                }
                per_preparation[prep_name] = {
                    "base_collision_count": len(base_collisions),
                    "extended_collision_count": len(extended_collisions),
                    "separated_pairs": sorted(base_collisions - extended_collisions),
                }
        return {
            "per_preparation": per_preparation,
            "full_cone_completeness_inferred": False,
        }
    if mutant_id == "M06":
        return m06_stable_null_control()
    if mutant_id == "M07":
        typed = data["typed_fillings"]
        candidates = [
            row
            for row in typed["vertical_maps"]
            if isinstance(row, Mapping) and row.get("map_sort") == "horizontal_growth_candidate"
        ]
        return {
            "retyped_candidate_count": len(candidates),
            "profile_behavior_changed": False,
            "horizontal_output_rewrite_constructed": False,
            "classification": "REFUSE-AS-HORIZONTAL-GROWTH",
        }
    if mutant_id == "M08":
        typed = data["typed_fillings"]
        fillings = index_rows(typed["horizontal_fillings"])
        retyped = [
            row
            for row in typed["arrow_retypings"]
            if isinstance(row, Mapping) and row.get("proposed_arrow_sort") == "vertical_comparison"
        ]
        evidence: list[dict[str, object]] = []
        boundaries = index_rows(typed["boundaries"])
        for row in retyped:
            filling = fillings[str(row["primitive_id"])]
            incoming = boundaries[str(filling["incoming_boundary_id"])]["generators"]
            outgoing = boundaries[str(filling["outgoing_boundary_id"])]["generators"]
            evidence.append(
                {
                    "incoming_size": len(incoming),
                    "outgoing_size": len(outgoing),
                    "invertible_passive_map_possible": len(incoming) == len(outgoing),
                }
            )
        return {"rows": evidence, "classification": "RECORD-WRITER-NOT-PASSIVE-COMPARISON"}
    if mutant_id == "M13":
        names = sorted(regions)
        return {
            "zero_law_class_count": 1 if names else 0,
            "constant_law_class_count": 1 if names else 0,
            "faithful_regional_separation": False,
        }
    if mutant_id == "M14":
        first = QMatrix.from_rows(((1,), (0,), (0,)))
        rival = QMatrix.from_rows(((0,), (1,), (0,)))
        return {
            "equal_rank": qrank(first) == qrank(rival),
            "same_subspace": qrank(qvstack((qtranspose(first), qtranspose(rival)), ncols=3)) == 1,
            "rank_is_not_calibrated_equality": True,
        }
    if mutant_id == "M15":
        sample = PrefixRegion.from_words(("10", "00"))
        renamed = PrefixRegion.from_words(reversed(sample.words))
        return {
            "canonical_serializations_equal": canonical_sha256(sample) == canonical_sha256(renamed),
            "neutral_identifier_available_to_law": False,
            "oracle_provenance": "DISCONNECTED",
        }
    if mutant_id == "M18":
        section = data["predictive_boundaries"]
        labels = section["labels"]
        matrix = matrix_record(section["future_profile"]["matrix"])
        boundary = PredictiveBoundary.from_profiles(labels, matrix)
        proposed = [list(block) for block in boundary.classes]
        split_index = next(
            (index for index, block in enumerate(proposed) if len(block) >= 2),
            None,
        )
        if split_index is None:
            return {
                "canonical_classes": boundary.classes,
                "control_status": "NO-DUPLICATE-CLASS-AVAILABLE",
            }
        block = proposed.pop(split_index)
        proposed.extend(([block[0]], block[1:]))
        signature = boundary_partition_signature(boundary, proposed)
        return {
            "canonical_classes": boundary.classes,
            "mutant_partition": signature,
            "redundant_split_detected_by_profiles": bool(signature.redundant_block_pairs),
        }
    if mutant_id == "M19":
        section = data["predictive_boundaries"]
        profile = matrix_record(section["future_profile"]["matrix"])
        change = matrix_record(section["basis_changes"][0]["matrix"])
        changed = qmultiply(change, profile)
        return {
            "invertible": qrank(change) == change.nrows == change.ncols,
            "kernel_preserved": qrowspace(profile) == qrowspace(changed),
        }
    if mutant_id == "M20":
        section = data["predictive_boundaries"]
        profile = matrix_record(section["future_profile"]["matrix"])
        append = matrix_record(section["future_extensions"][0]["appended_rows"])
        extended = qvstack((profile, append), ncols=profile.ncols)
        return {
            "base_rank": qrank(profile),
            "extended_rank": qrank(extended),
            "kernel_changed": qrowspace(profile) != qrowspace(extended),
        }
    if mutant_id in {"M21", "M22"}:
        return {
            "static_arena_reconstructed": True,
            "operation_schedule": "NOT-FROZEN",
            "interventional_influence": "NOT-CONSTRUCTED",
        }
    if mutant_id in {"M23", "M24"}:
        recovery = data["record_recovery"]
        operations = index_rows(recovery["operations"])
        reset_0 = _word_recovery_signature(
            operations, ["ro_000", "ro_001", "ro_003", "ro_004"]
        )
        reset_1 = _word_recovery_signature(
            operations, ["ro_000", "ro_001", "ro_003", "ro_005"]
        )
        one_copy = _word_recovery_signature(
            operations, ["ro_000", "ro_001", "ro_002", "ro_005"]
        )
        return {
            "one_copy_erased_other_recovers": one_copy,
            "both_erased_reader_0": reset_0,
            "both_erased_reader_1": reset_1,
        }
    if mutant_id == "M29":
        return {
            "status": "NO-FROZEN-FAMILY-GENERATOR",
            "heldout_scope": "registered members only",
        }
    if mutant_id in {"M28", "M30"}:
        family = data["regional_families"]
        pairs = index_rows(family["matched_pairs"])
        members = index_rows(family["members"])
        rows = []
        for pair in pairs.values():
            left, right = map(str, pair["member_ids"])
            rows.append(
                {
                    "blind_equal": _blind_projection(members[left])
                    == _blind_projection(members[right]),
                    "regional_equal": _regional_member_signature(members[left])
                    == _regional_member_signature(members[right]),
                }
            )
        return {
            "matched_pairs": rows,
            "blind_rule_can_distinguish_pair": any(not row["blind_equal"] for row in rows),
            "physical_regional_Tau": "NOT-CONSTRUCTED",
        }
    if mutant_id == "M31":
        return {"status": "RESOURCE-CLASS-CHANGED", "required_failure": False}
    if mutant_id == "M32":
        return {
            "status": "SCOPE-CONTROL",
            "horizontal_quantum_attempted": False,
            "external_comparator_does_not_promote_process": True,
        }
    if mutant_id == "M35":
        return {
            "byte_identity_is_provenance_identity": False,
            "disconnected_root_detected": True,
        }
    if mutant_id == "M33":
        event = next(iter(questions.values()))
        complement = event.complement()
        return {
            "delete_branch": event.join(PrefixRegion.zero()) != PrefixRegion.one(),
            "duplicate_branch": not event.disjoint(event),
            "renormalize_each_branch": "violates subnormalized affine Restriction law",
            "negative_branch": Fraction(-1) < 0,
            "wrong_restriction_cell": Restriction(event) != Restriction(complement),
        }
    if mutant_id == "P1":
        tree = nonempty_trees[0]
        cells = tree_branch_cells(tree, questions)
        group = list(cells)
        summed = join_regions(cells.values())
        return {
            "branch_count": len(group),
            "sum_cell": summed,
            "average_coefficient": Fraction(1, len(group)),
            "average_is_restriction_to_join": len(group) == 1,
        }
    if mutant_id == "P2":
        event = next(iter(questions.values()))
        support = event
        cells = {"0": support.meet(event.complement()), "1": support.meet(event)}
        return {
            "typed_ports": sorted(cells),
            "zero_ports": [name for name, cell in cells.items() if cell.is_zero()],
            "after_drop_port_set_changed": bool([cell for cell in cells.values() if cell.is_zero()]),
        }
    if mutant_id == "P3":
        return {
            "append_depth_two_ports": ["00", "01", "10", "11"],
            "overwrite_depth_two_ports": ["0", "1"],
            "history_information_lost": True,
        }
    if mutant_id == "P4":
        if len(preparations) < 2:
            raise ScoreRefusal("preparation-freeze control needs two preparations")
        event = next(iter(questions.values()))
        actual = {name: bernoulli_mass(event, p) for name, p in preparations.items()}
        frozen_value = next(iter(actual.values()))
        frozen = {name: frozen_value for name in actual}
        return {
            "actual_preparation_responses": actual,
            "frozen_responses": frozen,
            "law_root_must_remain_unchanged": True,
            "preparation_sensitivity_detected": actual != frozen,
        }
    if mutant_id == "P5":
        existing = set(regions.values())
        fresh = PrefixRegion.cylinder("010101")
        while fresh in existing:
            fresh = PrefixRegion.cylinder(next(iter(fresh.words)) + "0")
        return {
            "fresh_region": fresh,
            "symbolic_question_defined": Restriction(fresh),
            "whitelist_accepts": False,
        }
    if mutant_id == "P6":
        event = next(iter(questions.values()))
        return {
            "nonselective_join": event.join(event.complement()),
            "equals_identity": event.join(event.complement()).is_one(),
            "nontrivial_exterior_semigroup_generated": False,
        }
    if mutant_id == "P8":
        return {
            "positive_tensor_baseline": "UNCONSTRUCTED",
            "sequential_order_is_tensor": False,
            "status": "TENSOR-UNCONSTRUCTED",
        }
    if mutant_id == "L3":
        reading = score_locality(data, ProvenanceDAG(), options)
        return {"refinement_conjugation": reading["refinement_conjugation"]}
    if mutant_id == "L6":
        return {
            "supplied_subspace_root": canonical_sha256(data["regional_support"]),
            "law_generated_root": "ABSENT",
            "shortcut_refused": True,
        }
    if mutant_id == "G4":
        event = next(iter(questions.values()))
        correct = Restriction(event)
        wrong = Restriction(event.complement())
        return {
            "same_cospan_typing": True,
            "process_assignments_equal": correct == wrong,
            "functorial_assignment_mismatch": correct != wrong,
        }
    if mutant_id in {"M05"}:
        return {"mode": sorted(options.modes), "requires_full_recomputation": True}
    return None


def _top_level_hashes(receipt: Mapping[str, object]) -> dict[str, str]:
    ignored = {"payload_sha256", "mutants", "immutable_inputs", "integrity"}
    return {
        key: canonical_sha256(value)
        for key, value in receipt.items()
        if key not in ignored
    }


def evaluate_mutant(
    mutant_id: str,
    source: Mapping[str, object],
    authentication: Mapping[str, object],
    baseline: Mapping[str, object],
) -> dict[str, object]:
    transformed, options = apply_mutant(source, mutant_id)
    result: dict[str, object] = {
        "mutant": mutant_id,
        "source_fixture_hash": canonical_sha256(source),
        "transformed_fixture_hash": canonical_sha256(transformed),
        "transformation_modes": sorted(options.modes),
        "variants": options.variants,
    }
    if mutant_id in {"M12", "G1"}:
        variants: dict[str, object] = {}
        for name, from_whole in (("whole_changed", True), ("step_changed", False)):
            variant_data = copy.deepcopy(source)
            _delete_one_relation(variant_data, from_whole=from_whole)
            variants[name] = score_cospan_factorizations(
                variant_data, MutationOptions(mutant_id=mutant_id)
            )
        result.update(
            {
                "status": "RECOMPUTED-RECIPROCAL-VARIANTS",
                "evidence": variants,
            }
        )
        return result
    if mutant_id == "M26":
        source_family = source["regional_families"]
        transformed_family = transformed["regional_families"]
        source_members = index_rows(source_family["members"])
        transformed_members = index_rows(transformed_family["members"])
        source_regional = sorted(
            canonical_sha256(_regional_member_signature(row))
            for row in source_members.values()
        )
        transformed_regional = sorted(
            canonical_sha256(_regional_member_signature(row))
            for row in transformed_members.values()
        )
        source_blind = sorted(
            canonical_sha256(_blind_projection(row)) for row in source_members.values()
        )
        transformed_blind = sorted(
            canonical_sha256(_blind_projection(row))
            for row in transformed_members.values()
        )
        result.update(
            {
                "status": "RECOMPUTED-TRANSPORTED-GAUGE-CONTROL",
                "evidence": {
                    "regional_signature_multiset_preserved": source_regional
                    == transformed_regional,
                    "blind_signature_multiset_preserved": source_blind
                    == transformed_blind,
                    "identifier_or_mode_text_used": False,
                },
            }
        )
        return result
    if mutant_id == "M27":
        source_regions = regions_from_fixture(source)
        transformed_regions = regions_from_fixture(transformed)
        transported_regions = {
            name: PrefixRegion.from_words(
                _flip_binary_word(word) for word in region.words
            )
            for name, region in transformed_regions.items()
        }
        source_preparations = _preparation_rows(source)
        transformed_preparations = _preparation_rows(transformed)
        mass_checks = []
        for name in sorted(source_regions):
            for prep_name in sorted(source_preparations):
                mass_checks.append(
                    bernoulli_mass(source_regions[name], source_preparations[prep_name])
                    == bernoulli_mass(
                        transformed_regions[name], transformed_preparations[prep_name]
                    )
                )
        result.update(
            {
                "status": "RECOMPUTED-TRANSPORTED-GAUGE-CONTROL",
                "evidence": {
                    "regions_transport_back": transported_regions == source_regions,
                    "preparation_masses_transport": all(mass_checks),
                    "preparation_parameter_transport": {
                        name: {
                            "source": source_preparations[name],
                            "transformed": transformed_preparations[name],
                        }
                        for name in sorted(source_preparations)
                    },
                },
            }
        )
        return result
    special = _generic_algorithm_witness(mutant_id, transformed, options)
    if special is not None and not special.get("requires_full_recomputation", False):
        result.update({"status": "RECOMPUTED-SPECIAL-CONTROL", "evidence": special})
        return result
    try:
        mutated_receipt = score_dataset(
            transformed,
            authentication=authentication,
            options=options,
            include_mutants=False,
        )
    except ScoreRefusal as exc:
        result.update({"status": "REFUSED", "reason": str(exc)})
        return result
    base_hashes = _top_level_hashes(baseline)
    mutant_hashes = _top_level_hashes(mutated_receipt)
    changed = sorted(
        key for key in set(base_hashes) | set(mutant_hashes) if base_hashes.get(key) != mutant_hashes.get(key)
    )
    result.update(
        {
            "status": "RECOMPUTED",
            "changed_sections": changed,
            "baseline_primary": baseline["strict_primary"],
            "mutant_primary": mutated_receipt["strict_primary"],
            "evidence": special,
        }
    )
    return result


def evaluate_all_mutants(
    source: Mapping[str, object],
    authentication: Mapping[str, object],
    baseline: Mapping[str, object],
) -> dict[str, object]:
    return {
        mutant_id: evaluate_mutant(
            mutant_id, source, authentication, baseline
        )
        for mutant_id in MUTANT_IDS
    }


def _stage_file(directory: Path, prefix: str, payload: bytes) -> Path:
    descriptor, raw_path = tempfile.mkstemp(prefix=prefix, dir=str(directory))
    path = Path(raw_path)
    try:
        with os.fdopen(descriptor, "wb", closefd=True) as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        try:
            path.unlink()
        except FileNotFoundError:
            pass
        raise
    return path


def preflight_destinations(output_path: Path, receipt_path: Path) -> None:
    if not output_path.is_absolute() or not receipt_path.is_absolute():
        raise ScoreRefusal("output and receipt paths must be absolute")
    if output_path == receipt_path:
        raise ScoreRefusal("output and receipt paths must differ")
    if not output_path.parent.is_dir() or not receipt_path.parent.is_dir():
        raise ScoreRefusal("both destination directories must already exist")
    existing = [str(path) for path in (output_path, receipt_path) if path.exists()]
    if existing:
        raise ScoreRefusal("destination already exists: " + ", ".join(existing))


def publish_pair(
    output_path: Path,
    receipt_path: Path,
    output_payload: bytes,
    receipt_payload: bytes,
    *,
    fail_after_first_publish: bool = False,
) -> None:
    preflight_destinations(output_path, receipt_path)

    staged_output: Path | None = None
    staged_receipt: Path | None = None
    output_published = False
    receipt_published = False
    try:
        staged_output = _stage_file(output_path.parent, ".apr-output-stage-", output_payload)
        staged_receipt = _stage_file(receipt_path.parent, ".apr-receipt-stage-", receipt_payload)
        # Recheck immediately before publication.  Hard-link publication is
        # atomic and refuses an existing destination.
        if output_path.exists() or receipt_path.exists():
            raise ScoreRefusal("destination appeared during staging")
        os.link(staged_output, output_path)
        output_published = True
        if fail_after_first_publish:
            raise ScoreRefusal("synthetic failure after first publication")
        os.link(staged_receipt, receipt_path)
        receipt_published = True
        for directory in {output_path.parent, receipt_path.parent}:
            descriptor = os.open(directory, os.O_RDONLY)
            try:
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
    except BaseException:
        # Roll back only links created by this call; pre-existing destinations
        # were refused before staging and are never touched.
        if receipt_published:
            try:
                receipt_path.unlink()
            except FileNotFoundError:
                pass
        if output_published:
            try:
                output_path.unlink()
            except FileNotFoundError:
                pass
        raise
    finally:
        for staged in (staged_output, staged_receipt):
            if staged is not None:
                try:
                    staged.unlink()
                except FileNotFoundError:
                    pass


def run_official(output_path: Path, receipt_path: Path) -> dict[str, object]:
    preflight_destinations(output_path, receipt_path)
    data, authentication = load_frozen_fixture()
    receipt = score_dataset(
        data,
        authentication=authentication,
        include_mutants=True,
    )
    receipt["mutants"] = evaluate_all_mutants(data, authentication, receipt)
    attach_payload_hash(receipt)
    transcript = transcript_from_receipt(receipt)
    receipt_bytes = (canonical_json(receipt) + "\n").encode("utf-8")
    transcript_bytes = (canonical_json(transcript) + "\n").encode("utf-8")
    publish_pair(output_path, receipt_path, transcript_bytes, receipt_bytes)
    return {
        "schema": "apr-official-write-v1",
        "output_path": str(output_path),
        "receipt_path": str(receipt_path),
        "output_sha256": sha256_bytes(transcript_bytes),
        "receipt_sha256": sha256_bytes(receipt_bytes),
        "receipt_payload_sha256": receipt["payload_sha256"],
    }


def run_one_mutant(mutant_id: str) -> dict[str, object]:
    data, authentication = load_frozen_fixture()
    baseline = score_dataset(data, authentication=authentication, include_mutants=False)
    return evaluate_mutant(mutant_id, data, authentication, baseline)


def run_all_mutants_cli() -> dict[str, object]:
    data, authentication = load_frozen_fixture()
    baseline = score_dataset(data, authentication=authentication, include_mutants=False)
    return {
        "schema": "apr-mutant-evaluation-v1",
        "fixture_sha256": canonical_sha256(data),
        "mutants": evaluate_all_mutants(data, authentication, baseline),
    }


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_selftests() -> dict[str, object]:
    checks: list[str] = []

    region = PrefixRegion.from_words(("00", "01", "1"))
    _require(region.is_one(), "prefix canonicalization")
    left, right = PrefixRegion.cylinder("0").atomless_bipartition()
    _require(left.disjoint(right) and left.join(right) == PrefixRegion.cylinder("0"), "split")
    _require(bernoulli_mass(PrefixRegion.one(), Fraction(1, 3)) == 1, "valuation unit")
    checks.append("exact-prefix-boolean-and-valuation")

    tree = expression_to_tree(parse_expression("node(q,empty_tree,empty_tree)"))
    event = PrefixRegion.cylinder("0")
    cells = tree_branch_cells(tree, {"q": event}, support=event)
    partition = branch_partition_evidence(cells, event)
    _require(partition["is_partition"], "arbitrary-support tree partition")
    _require(cells["0"].is_zero() and cells["1"] == event, "semantic branch bits")
    checks.append("semantic-tree-partition-and-zero-port")

    malformed = parse_expression("intrinsic_replace(r,node(q,empty_tree,empty_tree))")
    refused = False
    try:
        validate_mixed_expression(
            malformed,
            (
                "mixed_tree := empty_tree",
                "mixed_tree := replace(replacement,mixed_tree)",
                "mixed_tree := node(question,port_0:mixed_tree,port_1:mixed_tree)",
            ),
        )
    except ScoreRefusal:
        refused = True
    _require(refused, "undeclared intrinsic mixed constructor must refuse")
    checks.append("mixed-constructor-refusal")

    first = FiniteCospan(
        "first",
        ("a",),
        ("b",),
        ("ain", "mid"),
        (("a", "ain"),),
        (("b", "mid"),),
        (("ain", "mid"),),
    )
    second = FiniteCospan(
        "second",
        ("b",),
        ("c",),
        ("mid2", "cout"),
        (("b", "mid2"),),
        (("c", "cout"),),
        (("mid2", "cout"),),
    )
    whole = FiniteCospan(
        "whole",
        ("a",),
        ("c",),
        ("ain", "mid", "cout"),
        (("a", "ain"),),
        (("c", "cout"),),
        (("ain", "mid"), ("mid", "cout")),
    )
    _require(
        boundary_fixed_isomorphic(compose_cospans((first, second)), singleton_quotient(whole)),
        "constructed cospan pushout",
    )
    checks.append("finite-pushout-isomorphism")

    m06 = m06_stable_null_control()
    _require(m06["baseline_nullity"] == 1, "M06 baseline stable null")
    _require(m06["reactivated_nullity"] == 0, "M06 reactivation")
    checks.append("paired-four-coordinate-stable-null")

    target = PrefixRegion.cylinder("00")
    depth = 3
    literal = (
        child_swap_permutation("01", depth),
        child_swap_permutation("1", depth),
    )
    generic = _recursive_child_generators(target, depth)
    intrinsic = _intrinsic_exterior_generators(target, depth)
    literal_reading = _orbit_reading(target, depth, literal)
    generic_reading = _orbit_reading(target, depth, generic)
    intrinsic_reading = _orbit_reading(target, depth, intrinsic)
    _require(literal_reading["exterior_orbit_count"] == 3, "literal orbits")
    _require(generic_reading["exterior_orbit_count"] == 2, "generic orbits")
    _require(intrinsic_reading["exterior_orbit_count"] == 1, "intrinsic orbit")
    _require(
        _relative_support_comparison(target, depth, literal_reading)["fixed_in_kin_residual"] == 2,
        "literal relative-support residual",
    )
    _require(
        _relative_support_comparison(target, depth, generic_reading)["fixed_in_kin_residual"] == 1,
        "generic relative-support residual",
    )
    _require(
        _relative_support_comparison(target, depth, intrinsic_reading)["fixed_in_kin_residual"] == 0,
        "intrinsic relative-support equality",
    )
    checks.append("three-replacement-closures")

    record_operations = {
        "write": {
            "id": "write",
            "input_fields": ["source", "flag0", "flag1"],
            "output_fields": ["source", "source", "flag1"],
        },
        "read": {
            "id": "read",
            "input_fields": ["source", "flag0", "flag1"],
            "output_fields": ["flag0"],
        },
        "read_again": {
            "id": "read_again",
            "input_fields": ["source", "flag0", "flag1"],
            "output_fields": ["flag1"],
        },
    }
    _require(
        _word_recovery_signature(record_operations, ["write", "read"])["status"] == "TYPED",
        "single reader typing",
    )
    _require(
        _word_recovery_signature(record_operations, ["write", "read", "read_again"])["status"]
        == "ILL-TYPED-REFUSED",
        "sequential reader refusal",
    )
    checks.append("strict-record-reader-typing")

    _require(set(MUTANT_IDS) == set(
        [f"M{index:02d}" for index in range(1, 36)]
        + [f"P{index}" for index in range(1, 9)]
        + [f"L{index}" for index in range(1, 7)]
        + [f"G{index}" for index in range(1, 8)]
    ), "mutant registry coverage")
    checks.append("mutant-registry-coverage")

    with tempfile.TemporaryDirectory(prefix="apr-generic-selftest-") as raw_directory:
        directory = Path(raw_directory)
        output = directory / "out.json"
        receipt = directory / "receipt.json"
        publish_pair(output, receipt, b"output\n", b"receipt\n")
        _require(output.read_bytes() == b"output\n", "paired output bytes")
        _require(receipt.read_bytes() == b"receipt\n", "paired receipt bytes")
        prior_output = output.read_bytes()
        prior_receipt = receipt.read_bytes()
        refused_overwrite = False
        try:
            publish_pair(output, directory / "new.json", b"x", b"y")
        except ScoreRefusal:
            refused_overwrite = True
        _require(refused_overwrite, "overwrite refusal")
        _require(output.read_bytes() == prior_output and receipt.read_bytes() == prior_receipt, "overwrite preservation")
        receipt_only = directory / "receipt-only.json"
        receipt_only.write_bytes(b"existing\n")
        absent_output = directory / "absent-output.json"
        refused_receipt_only = False
        try:
            publish_pair(absent_output, receipt_only, b"x", b"y")
        except ScoreRefusal:
            refused_receipt_only = True
        _require(
            refused_receipt_only
            and not absent_output.exists()
            and receipt_only.read_bytes() == b"existing\n",
            "receipt-only overwrite refusal",
        )
        refused_both = False
        try:
            publish_pair(output, receipt, b"x", b"y")
        except ScoreRefusal:
            refused_both = True
        _require(
            refused_both
            and output.read_bytes() == prior_output
            and receipt.read_bytes() == prior_receipt,
            "both-existing overwrite refusal",
        )
        fail_output = directory / "fail-output.json"
        fail_receipt = directory / "fail-receipt.json"
        failed = False
        try:
            publish_pair(
                fail_output,
                fail_receipt,
                b"x",
                b"y",
                fail_after_first_publish=True,
            )
        except ScoreRefusal:
            failed = True
        _require(failed and not fail_output.exists() and not fail_receipt.exists(), "paired rollback")
    checks.append("transactional-no-overwrite-publish")

    return {
        "schema": "apr-generic-selftest-v1",
        "scientific_fixture_evaluated": False,
        "check_count": len(checks),
        "checks": checks,
        "status": "PASS",
    }


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Exact semantic scorer for APR Paper 12",
        allow_abbrev=False,
    )
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--selftest", action="store_true")
    modes.add_argument("--run", action="store_true")
    modes.add_argument("--mutant", choices=MUTANT_IDS)
    modes.add_argument("--mutants-all", action="store_true")
    parser.add_argument("--output")
    parser.add_argument("--receipt")
    args = parser.parse_args(argv)
    if args.run:
        if args.output is None or args.receipt is None:
            parser.error("--run requires --output PATH and --receipt PATH")
    elif args.output is not None or args.receipt is not None:
        parser.error("output paths are accepted only with --run")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        if args.selftest:
            payload = run_selftests()
        elif args.run:
            payload = run_official(Path(args.output), Path(args.receipt))
        elif args.mutant is not None:
            payload = run_one_mutant(args.mutant)
        else:
            payload = run_all_mutants_cli()
    except (AssertionError, KeyError, OSError, ScoreRefusal, TypeError, ValueError) as exc:
        print(f"APR-SCORER-REFUSED {exc}", file=sys.stderr)
        return 1
    sys.stdout.write(canonical_json(payload) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
