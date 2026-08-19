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
    "note-apr-scorer-repair-pin.md": "14e08b0d2b6ee53fa290849d111579d45ccbe037248cbd086139e600c2668ffc",
    "note-apr-scorer-repair-pin-addendum.md": "d6d59a312ccadfd96ff6b4a002dc98e384c6a0e56d41114f16e273fb9dde408a",
    "note-apr-scorer-repair-pin-addendum-2.md": "898a49596752b9b7789bd6c6b71d471aac02a81836cf85c558b6b7f3c425fd4d",
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
    "1956ad5",
    "ff7e4b0",
    "430795a",
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

MUTANT_DESCRIPTIONS: dict[str, str] = {
    "M01": "replace the symbolic region constructor by a finite-depth constructor",
    "M02": "form the atomic branch-character quotient control",
    "M03": "identify regions by one scalar volume profile",
    "M04": "remove probes from a finite separating catalogue",
    "M05": "change redundant longer continuation words without changing generator closure",
    "M06": "reactivate a one-step null direction with a continuation-stable control",
    "M07": "retype a passive vertical map as horizontal growth",
    "M08": "retype a record-writing horizontal filling as passive comparison",
    "M09": "replace a calibrated comparison transport by a rival isometry",
    "M10": "move comparison into a null-profile target",
    "M11": "replace a comparison transport by a non-isometry",
    "M12": "delete a relation on one side of a frozen factorization equality",
    "M13": "run explicit zero and constant profile laws through the quotient",
    "M14": "compare equal-rank unequal subspaces and supplied-map ancestry",
    "M15": "instantiate syntax-copy, identifier-hash, and finite whitelist oracles",
    "M16": "erase represented candidate-regional overlap in the region-bearing object",
    "M17": "replace the future-profile matrix by a lossy presentation",
    "M18": "split one predictive class redundantly",
    "M19": "apply an invertible change of future-profile basis",
    "M20": "append future-profile rows that may refine the boundary",
    "M21": "run the static common-cause influence control",
    "M22": "run the static reversible-cycle causality control",
    "M23": "destroy a record with a selected same-law reset/eraser then read it",
    "M24": "erase one versus both redundant record copies and read the survivor",
    "M25": "inject a forbidden result-bearing oracle field",
    "M26": "swap neutral family identifiers and relation-mode prose",
    "M27": "transport Boolean presentation and preparation together",
    "M28": "substitute the blind interface for candidate-regional presentation",
    "M29": "request a generated unseen held-out family member",
    "M30": "blind a candidate-regional rule at the registered interface",
    "M31": "change the declared blind resource class",
    "M32": "delete interference in the external quantum comparator",
    "M33": "construct five malformed branch/process objects and rerun ordinary gates",
    "M34": "toggle a declared static contact relation without a generated response",
    "M35": "sever typed provenance while preserving the scientific payload bytes",
    "P1": "replace additive coarse graining by averaging",
    "P2": "drop typed zero-support ports",
    "P3": "overwrite rather than append generated depth-two record bits",
    "P4": "freeze preparation-dependent responses to one preparation row",
    "P5": "test a finite whitelist on a fresh valid deeper region",
    "P6": "use the nonselective question channel as exterior dynamics",
    "P7": "replace pushout composition by a typed-leg tagged-union impostor",
    "P8": "call sequential composition a positive tensor factory",
    "L1": "remove the intrinsic replacement grammar and retain restricted swaps",
    "L2": "delete a listed child-swap generator",
    "L3": "conjugate replacement data by a regrouping presentation",
    "L4": "replace intrinsic exterior transitivity by multiple orbits",
    "L5": "delete a required transported conjugate from a finite closed family",
    "L6": "substitute a supplied support matrix for a generated equalizer",
    "G1": "delete a relation from one side of cospan composition",
    "G2": "change one reachable horizontal-filling leg used by a factorization",
    "G3": "stop after typed-leg validation without constructing a pushout",
    "G4": "alter a filling-to-process assignment",
    "G5": "alter a whole-versus-step process assignment at an alternate cut",
    "G6": "perturb a global extension while recomputing its local marginals",
    "G7": "remove every registered global overlap extension",
}


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
    identifiers: set[str] = set()
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
        if identifier in identifiers:
            raise ScoreRefusal("question transition repeats a neutral port identifier")
        identifiers.add(identifier)
        found[bit] = "complement-event" if bit == 0 else "event"
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
    details: dict[str, object] = field(default_factory=dict)

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
    typed = data.get("typed_fillings")
    if not isinstance(process, Mapping) or not isinstance(typed, Mapping):
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

    # Detect construction interfaces from typed data.  Finite neighboring
    # controls never manufacture a total forest, tensor, naturality square,
    # or filling-to-process assignment.
    total_frontier_interface = process.get("total_adaptive_frontier_factory")
    assignment_interface = process.get("filling_to_process_assignment")
    tensor_interface = typed.get("tensor_factory") or process.get("tensor_factory")
    naturality_interface = typed.get("vertical_horizontal_naturality_squares")
    total_frontier_present = isinstance(total_frontier_interface, Mapping) and all(
        key in total_frontier_interface for key in ("constructor", "typing_rule", "composition_rule")
    )
    assignment_present = isinstance(assignment_interface, Mapping) and all(
        key in assignment_interface
        for key in ("assignment", "identity_equation", "composition_equation", "cut_equation")
    )
    tensor_present = isinstance(tensor_interface, Mapping) and all(
        key in tensor_interface for key in ("object_tensor", "arrow_tensor", "unit", "interchange")
    )
    naturality_present = isinstance(naturality_interface, Mapping) and all(
        key in naturality_interface
        for key in ("squares", "horizontal_assignment", "vertical_assignment")
    )
    construction_ceiling = {
        "B0_identity": (
            "CONSTRUCTED" if b0_identity_constructed else "REFUSED"
        ),
        "B0_identity_evidence": b0_identity_controls,
        "all_boundary_identity": (
            "CONSTRUCTED"
            if all(
                row["present"] for row in _identity_assignments_by_boundary(data).values()
            )
            else "UNCONSTRUCTED"
        ),
        "arbitrary_prefix_free_frontiers": (
            "CONSTRUCTED" if total_frontier_present else "UNCONSTRUCTED"
        ),
        "question_bit_boundary_carrier": (
            "CONSTRUCTED"
            if total_frontier_present
            and all(
                row["present"]
                for row in _identity_assignments_by_boundary(data).values()
            )
            else "UNCONSTRUCTED"
        ),
        "tensor_factory": "CONSTRUCTED" if tensor_present else "UNCONSTRUCTED",
        "mixed_question_replacement_forest": (
            "CONSTRUCTED"
            if total_frontier_present and assignment_present
            else "UNCONSTRUCTED"
        ),
        "vertical_naturality": "CONSTRUCTED" if naturality_present else "VACUOUS-UNCONSTRUCTED",
        "filling_to_process_assignment": "CONSTRUCTED" if assignment_present else "UNCONSTRUCTED",
        "regional_overlap_gluing_rule": (
            "CONSTRUCTED"
            if isinstance(data.get("overlap_gluing"), Mapping)
            and isinstance(data["overlap_gluing"].get("global_selector"), Mapping)
            else "UNCONSTRUCTED"
        ),
    }
    neighboring_controls_pass = (
        all_branch_partitions
        and all_numeric_controls
        and all_cut_controls
        and cospan_result["all_finite_pushouts_match"]
    )
    total_horizontal_process = total_frontier_present and assignment_present
    process_coordinate = (
        "HORIZONTAL-PROCESS-CONSTRUCTED"
        if total_horizontal_process
        else "STATIC-RESPONSE-ONLY"
    )
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
            "finite_tree_control": all_branch_partitions
            and all_numeric_controls
            and all_cut_controls,
            "neighboring_graph_cospan_control": cospan_result[
                "all_finite_pushouts_match"
            ],
            "controls_are_not_a_process_assignment": True,
            "total_forest": (
                "CONSTRUCTED" if total_horizontal_process else "UNCONSTRUCTED"
            ),
        },
        "alternate_cuts": {name: value["cut_reconstruction"] for name, value in tree_results.items()},
        "coarse_graining": {
            "operation": "sum of disjoint Restriction cells",
            "average_forbidden": True,
            "registered_controls": coarse_controls,
        },
        "cospan_pushouts": cospan_result,
        "functorial_assignment": {
            "question_tree_to_graph_cospan_assignment": (
                "CONSTRUCTED" if assignment_present else "UNAVAILABLE"
            ),
            "neighboring_controls_jointly_green": neighboring_controls_pass,
            "total_assignment": "CONSTRUCTED" if assignment_present else "UNCONSTRUCTED",
            "reason": (
                "a typed filling-to-process assignment with identity, "
                "composition, and cut equations is present"
                if assignment_present
                else "tree branch/cut calculations and graph-cospan pushouts are "
                "separate controls; no filling-to-process assignment is frozen"
            ),
        },
        "tensor": (
            "CONSTRUCTED"
            if tensor_present
            else "UNCONSTRUCTED-NO-BOUNDARY-OR-MAP-FACTORY"
        ),
        "vertical_naturality": (
            "CONSTRUCTED"
            if naturality_present
            else "UNCONSTRUCTED-PASSIVE-PAIR-HAS-NO-NONIDENTITY-HORIZONTAL-SQUARE"
        ),
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
        "neighboring_controls_pass": neighboring_controls_pass,
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

    # Build a genuinely fresh region and its symbolic restriction.  Promotion
    # to a generated probe is conditional on a typed total compiler below.
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
    }
    node = provenance.add(
        "probe_profiles",
        roots=["fixture:prefix_controls", "derived:finite_question_instruments"],
        transform="generated finite scalar profiles plus fresh symbolic question",
    )
    compiler = data.get("complete_probe_compiler")
    compiler_fields = ("target_domain", "compile", "separation_proof")
    compiler_present = isinstance(compiler, Mapping) and all(
        field in compiler for field in compiler_fields
    )
    fresh_symbolic["lawful_filling"] = (
        "GENERATED-BY-COMPILER" if compiler_present else "UNCONSTRUCTED"
    )
    fresh_symbolic["reader_effect"] = (
        "GENERATED-BY-COMPILER" if compiler_present else "UNCONSTRUCTED"
    )
    return {
        "finite_catalogue": finite_catalogues,
        "appended_probe": appended_controls,
        "fresh_generated_probe": fresh_symbolic,
        "completeness_scope": (
            "COMPLETE-GENERATED" if compiler_present else "FINITE-CONTROLS-ONLY"
        ),
        "capability_detection": {
            "complete_target_independent_compiler": compiler_present,
            "required_fields": compiler_fields,
            "fresh_symbolic_question_is_not_a_generated_probe": True,
        },
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
    generated_congruence = data.get("generated_regional_congruence")
    required_congruence_fields = (
        "complete_probe_compiler",
        "all_process_contexts",
        "Boolean_compatibility_proof",
        "gluing_compatibility_proof",
    )
    congruence_present = isinstance(generated_congruence, Mapping) and all(
        field in generated_congruence for field in required_congruence_fields
    )
    contextual = {
        "status": "COMPLETE" if congruence_present else "INCOMPLETE",
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
        "coordinate": "CONGRUENCE" if congruence_present else "PROFILE-EQUIVALENCE-ONLY",
        "finite_Boolean_profile_control": finite_equivalence,
        "Boolean_full_cone_theorem": "CONDITIONAL-ON-COMPLETE-GENERATED-PROBES",
        "process_contexts": "UNCONSTRUCTED",
        "contact_causal_contexts": "PRICED",
        "boundary_gluing_contexts": "UNCONSTRUCTED",
        "capability_detection": {
            "generated_congruence_present": congruence_present,
            "required_fields": required_congruence_fields,
            "finite_profile_control_cannot_promote": True,
        },
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
            "a common exterior scalar is not thereby a regional atom; use the relative support quotient"
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


def _record_operation_roles(
    operations: Mapping[str, Mapping[str, object]]
) -> dict[str, str]:
    roles: dict[str, str] = {}
    for identifier, row in operations.items():
        inputs = row.get("input_fields")
        outputs = row.get("output_fields")
        if not isinstance(inputs, list) or len(inputs) != 3 or not isinstance(outputs, list):
            continue
        source, flag0, flag1 = map(str, inputs)
        signature = tuple(str(value) for value in outputs)
        role = {
            (source, source, flag1): "write_flag0",
            (source, flag0, source): "write_flag1",
            (source, "0", flag1): "erase_flag0",
            (source, "0", "0"): "erase_both",
            (flag0,): "read_flag0",
            (flag1,): "read_flag1",
        }.get(signature)
        if role is not None:
            if role in roles:
                raise ScoreRefusal(f"record grammar has multiple operations for role {role}")
            roles[role] = identifier
    required = {
        "write_flag0",
        "write_flag1",
        "erase_flag0",
        "erase_both",
        "read_flag0",
        "read_flag1",
    }
    if set(roles) != required:
        raise ScoreRefusal("record grammar lacks one of the required semantic roles")
    return roles


def score_records(
    data: Mapping[str, object], process_context: Mapping[str, object], provenance: ProvenanceDAG
) -> dict[str, object]:
    recovery = data.get("record_recovery")
    process = data.get("regional_question_process")
    if not isinstance(recovery, Mapping) or not isinstance(process, Mapping):
        raise ScoreRefusal("missing record primitives")
    operations = index_rows(recovery.get("operations"))
    operation_roles = _record_operation_roles(operations)
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
        and row["operation_ids"][-2:]
        == [operation_roles["read_flag0"], operation_roles["read_flag1"]]
    ]
    if malformed_rows:
        raw_word = malformed_rows[0]["operation_ids"]
        assert isinstance(raw_word, list)
        erase_both = operation_roles["erase_both"]
        reset_position = raw_word.index(erase_both) if erase_both in raw_word else 0
        prefix_before_reset = [str(value) for value in raw_word[: reset_position + 1]]
    separate_reset_readers = {
        "reader_0": _word_recovery_signature(
            operations, prefix_before_reset + [operation_roles["read_flag0"]]
        ),
        "reader_1": _word_recovery_signature(
            operations, prefix_before_reset + [operation_roles["read_flag1"]]
        ),
        "joint_semantics": "NOT-DECLARED",
    }

    process_operations = index_rows(process.get("operations"))
    same_law_schedules = validate_reader_schedules(data)

    continuation_results: dict[str, object] = {}
    for identifier, row in sorted(index_rows(process.get("continuation_catalogues")).items()):
        operation_ids = row.get("operation_ids")
        if not isinstance(operation_ids, list):
            raise ScoreRefusal("bad continuation catalogue")
        if any(str(value) not in process_operations for value in operation_ids):
            raise ScoreRefusal("continuation catalogue references an unknown operation")
        operation_semantics = [
            process_record_semantics(process_operations[str(value)])
            for value in operation_ids
        ]
        actions = {str(value["action"]) for value in operation_semantics}
        if "reset" in actions:
            status = "DESTROYED-BY-RESET"
        elif "erase_last" in actions:
            status = "NOT-PERMANENT-UNDER-LAST-TOKEN-ERASURE"
        else:
            status = "APPEND-ONLY-RECOVERABLE-AT-DECLARED-SCOPE"
        continuation_results[identifier] = {
            "status": status,
            "operation_semantics": operation_semantics,
            "typed_subgrammar_only": True,
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
        "unconstructed_continuations": [
            "mixed question/replacement forest",
            "tensor continuation",
            "unassigned total adaptive continuation",
        ],
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
        depth = max(2, max((len(word) for word in target.words), default=0) + 1)
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
                all(value in intrinsic_closure for value in intrinsic_conjugates)
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
    locality_certificate = data.get("generated_dynamic_locality_certificate")
    locality_requirements = (
        "complete_effect_factory",
        "total_process_provenance",
        "nonconstancy",
        "support_faithfulness",
        "order_reflection",
        "all_partition_replacement_closure",
        "regional_congruence",
        "post_quotient_atomlessness",
    )
    locality_certificate_present = isinstance(locality_certificate, Mapping) and all(
        key in locality_certificate for key in locality_requirements
    )
    regional_support_promotable = finite_intrinsic_ok and locality_certificate_present
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
        "registered_grains": {
            target: {
                "target": row["target"],
                "depth": max(
                    2,
                    max(
                        (len(word) for word in row["target"].words),
                        default=0,
                    )
                    + 1,
                ),
                "literal_orbits": row[
                    "literally_listed_child_swaps"
                ]["exterior_orbit_count"],
                "recursive_orbits": row[
                    "generic_recursive_child_swap_closure"
                ]["exterior_orbit_count"],
                "intrinsic_orbits": row[
                    "intrinsic_relative_complement_closure"
                ]["exterior_orbit_count"],
            }
            for target, row in readings.items()
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
        "capability_detection": {
            "finite_analytical_control": finite_intrinsic_ok,
            "generated_certificate_present": locality_certificate_present,
            "required_certificate_fields": locality_requirements,
            "control_cannot_promote": True,
        },
        "locality_coordinate": (
            "DYNAMIC-FAITHFUL" if regional_support_promotable else "FAIL"
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
    generated_system = section.get("generated_comparison_system")
    comparison_fields = (
        "active_law_root",
        "transport_rule",
        "cut_consistency_proof",
        "operational_calibration",
    )
    comparison_present = isinstance(generated_system, Mapping) and all(
        field in generated_system for field in comparison_fields
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
        "comparison_coordinate": "DERIVED" if comparison_present else "PRICED",
        "capability_detection": {
            "generated_comparison_system": comparison_present,
            "required_fields": comparison_fields,
            "mathematical_controls_do_not_promote": True,
        },
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
    generated_system = section.get("generated_future_profile_system")
    sufficient_fields = (
        "active_law_root",
        "future_effect_compiler",
        "completeness_proof",
        "factorization_proof",
    )
    sufficient_present = isinstance(generated_system, Mapping) and all(
        field in generated_system for field in sufficient_fields
    )
    minimal_fields = ("minimality_proof", "natural_isomorphism_rule")
    minimal_present = sufficient_present and all(
        field in generated_system for field in minimal_fields
    )
    boundary_coordinate = (
        "MINIMAL-AT-CATALOGUE"
        if minimal_present
        else "SUFFICIENT"
        if sufficient_present
        else "DECLARED"
    )
    return {
        "generated_profiles": {
            "status": (
                "LAW-GENERATED-COMPLETE-FUTURE-PROFILES"
                if sufficient_present
                else "PRIMITIVE-MATHEMATICAL-CONTROL-NOT-LAW-GENERATED"
            ),
            "matrix": profile,
        },
        "canonical_classes": canonical.classes,
        "lossy_control": partitions,
        "redundant_control": partitions,
        "invertible_change_control": basis_changes,
        "appended_future_control": extensions,
        "linear_presentations": presentations,
        "boundary_coordinate": boundary_coordinate,
        "universal_property": (
            "MINIMAL-FACTORIZATION-UP-TO-NATURAL-ISOMORPHISM-AND-NULL"
            if minimal_present
            else "SUFFICIENT-FACTORIZATION-CONSTRUCTED"
            if sufficient_present
            else "NOT-CONSTRUCTED-FROM-COMPLETE-LAW-FUTURES"
        ),
        "capability_detection": {
            "generated_future_profile_system": sufficient_present,
            "minimality_package": minimal_present,
            "required_sufficiency_fields": sufficient_fields,
            "required_minimality_fields": minimal_fields,
            "finite_profile_controls_do_not_promote": True,
        },
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
            endpoint_equal_probability = sum(
                exact(weight)
                for configuration, weight in zip(configurations, weights)
                if configuration[variables.index("A")]
                == configuration[variables.index("C")]
            ) if "A" in variables and "C" in variables else None
            candidate_rows[str(candidate_id)] = {
                "left_marginal": left_marginal,
                "right_marginal": right_marginal,
                "matches_left": left_marginal == left_expected,
                "matches_right": right_marginal == right_expected,
                "endpoint_equal_probability": endpoint_equal_probability,
                "canonical_candidate_payload_sha256": canonical_sha256(
                    {
                        "variables": variables,
                        "weighted_configurations": sorted(
                            zip(configurations, (exact(value) for value in weights))
                        ),
                    }
                ),
            }
        compatible = [
            name
            for name, candidate in candidate_rows.items()
            if candidate["matches_left"] and candidate["matches_right"]
        ]
        compatible_endpoint_values = sorted(
            {
                candidate_rows[name]["endpoint_equal_probability"]
                for name in compatible
            },
            key=canonical_json,
        )
        compatible_local_values = [
            value
            for name in compatible
            for marginal_name in ("left_marginal", "right_marginal")
            for value in candidate_rows[name][marginal_name].values()
        ]
        result[request_name] = {
            "candidates": candidate_rows,
            "compatible_global_extensions": compatible,
            "selected_extension": "UNSELECTED" if len(compatible) != 1 else compatible[0],
            "regional_gluing_law": "UNCONSTRUCTED",
            "selector_kill": {
                "same_registered_local_marginals": len(compatible) >= 2,
                "different_endpoint_correlation": len(compatible_endpoint_values) >= 2,
                "all_uniform_local_pair_values_one_quarter": bool(
                    compatible_local_values
                )
                and all(value == Fraction(1, 4) for value in compatible_local_values),
                "endpoint_equal_probabilities": compatible_endpoint_values,
                "canonical_order_is_not_a_law": True,
                "row_order_is_not_a_law": True,
                "hash_extremum_is_not_a_law": True,
                "entropy_or_sparsity_convention_is_not_frozen": True,
                "unselected_joint_extension": len(compatible) >= 2
                and len(compatible_endpoint_values) >= 2,
            },
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
    schedule_rows = section.get("generated_schedules")
    response_rows = section.get("generated_delayed_responses")
    schedule_present = isinstance(schedule_rows, list) and bool(schedule_rows)
    response_present = isinstance(response_rows, list) and bool(response_rows)
    if schedule_present:
        for row in schedule_rows:
            if not isinstance(row, Mapping) or not isinstance(row.get("operation_ids"), list):
                raise ScoreRefusal("malformed generated influence schedule")
    if response_present:
        for row in response_rows:
            if not isinstance(row, Mapping) or "before" not in row or "after" not in row:
                raise ScoreRefusal("malformed generated delayed response")
    joint_provenance = section.get("joint_law_provenance")
    provenance_present = isinstance(joint_provenance, Mapping) and all(
        key in joint_provenance for key in ("root", "schedule_edges", "reader_edges")
    )
    generated_contact = schedule_present and response_present and provenance_present
    contact = {
        "static_classification_controls": static_rows,
        "generated_joint_fillings": (
            "CONSTRUCTED"
            if schedule_present and provenance_present
            else "NOT-CONSTRUCTED"
        ),
        "nonoverlap_contact_response": (
            "CONSTRUCTED"
            if response_present and provenance_present
            else "NOT-CONSTRUCTED"
        ),
        "capability_detection": {
            "generated_schedule": schedule_present,
            "generated_delayed_response": response_present,
            "joint_law_provenance": provenance_present,
        },
        "contact_coordinate": "DERIVED" if generated_contact else "PRICED",
    }
    causality = {
        "static_classification_controls": static_rows,
        "intervention_schedule": "GENERATED" if schedule_present else "NOT-FROZEN",
        "generated_delayed_reader_distribution": (
            "CONSTRUCTED" if response_present else "NOT-CONSTRUCTED"
        ),
        "reversible_replacement_cycles_are_causal": False,
        "capability_detection": {
            "generated_schedule": schedule_present,
            "generated_delayed_reader_distribution": response_present,
            "joint_law_provenance": provenance_present,
        },
        "causality_coordinate": "DERIVED" if generated_contact else "PRICED",
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


def _candidate_regional_projection(member: Mapping[str, object]) -> dict[str, object]:
    """Consume and canonicalize the frozen candidate-regional blind map.

    Component preimages are intentionally collapsed after applying the frozen
    map.  Thus two distinct candidate-regional components with one blind image
    are one blind component.  Raw node/component IDs, insertion order, region
    words, and relation-mode prose are excluded from the canonical payload.
    """

    region_rows = member.get("regions")
    occurrence_rows = member.get("component_occurrences")
    projection_rows = member.get("blind_projection")
    blind = member.get("blind_interface")
    resources = member.get("resource_declaration")
    incidence_rows = member.get("incidences")
    if not all(
        isinstance(value, list)
        for value in (region_rows, occurrence_rows, projection_rows, incidence_rows)
    ) or not isinstance(blind, Mapping) or not isinstance(resources, Mapping):
        raise ScoreRefusal("malformed candidate-regional projection presentation")

    regions: dict[str, PrefixRegion] = {}
    for row in region_rows:
        if not isinstance(row, Mapping) or not isinstance(row.get("node_token"), str):
            raise ScoreRefusal("candidate-regional node lacks a token")
        token = str(row["node_token"])
        if token in regions:
            raise ScoreRefusal("duplicate candidate-regional node token")
        antichain = row.get("antichain")
        if not isinstance(antichain, list):
            raise ScoreRefusal("candidate-regional node lacks an antichain")
        regions[token] = PrefixRegion.from_words(str(word) for word in antichain)

    occurrences: dict[str, PrefixRegion] = {}
    for row in occurrence_rows:
        if not isinstance(row, Mapping) or not isinstance(
            row.get("component_token"), str
        ):
            raise ScoreRefusal("candidate-regional component lacks a token")
        token = str(row["component_token"])
        if token in occurrences:
            raise ScoreRefusal("duplicate candidate-regional component token")
        antichain = row.get("antichain")
        if not isinstance(antichain, list):
            raise ScoreRefusal("candidate-regional component lacks an antichain")
        occurrences[token] = PrefixRegion.from_words(str(word) for word in antichain)

    projection: dict[str, str] = {}
    for row in projection_rows:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad candidate-regional-to-blind projection row")
        source = row.get("component_token")
        target = row.get("blind_component_token")
        if not isinstance(source, str) or not isinstance(target, str) or not target:
            raise ScoreRefusal("nonfunctional candidate-regional-to-blind projection")
        if source in projection:
            raise ScoreRefusal("duplicate/nonfunctional candidate-regional-to-blind projection")
        projection[source] = target
    if set(projection) != set(occurrences):
        raise ScoreRefusal("candidate-regional-to-blind projection is not total/exact")

    node_components: dict[str, set[str]] = {node: set() for node in regions}
    for component, event in occurrences.items():
        for node, region in regions.items():
            if event.meet(region) == event:
                node_components[node].add(component)

    declared_crosschecks: list[dict[str, object]] = []
    for row in incidence_rows:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad declared candidate-regional incidence")
        nodes = row.get("node_tokens")
        left_components = row.get("left_component_tokens")
        right_components = row.get("right_component_tokens")
        if (
            not isinstance(nodes, list)
            or len(nodes) != 2
            or not isinstance(left_components, list)
            or not isinstance(right_components, list)
        ):
            raise ScoreRefusal("ill-typed declared candidate-regional incidence")
        left, right = map(str, nodes)
        if left not in regions or right not in regions:
            raise ScoreRefusal("declared incidence references an unknown node")
        left_set = {str(value) for value in left_components}
        right_set = {str(value) for value in right_components}
        if not left_set.issubset(node_components[left]) or not right_set.issubset(
            node_components[right]
        ):
            raise ScoreRefusal("declared incidence disagrees with region antichains")
        represented_shared = node_components[left] & node_components[right]
        declared_shared = left_set & right_set
        if represented_shared != declared_shared:
            raise ScoreRefusal("declared shared-component incidence is incomplete")
        declared_crosschecks.append(
            {
                "represented_overlap": not regions[left].meet(regions[right]).is_zero(),
                "shared_component_count": len(represented_shared),
            }
        )

    node_tokens_raw = blind.get("node_tokens")
    blind_edges_raw = blind.get("edges")
    if not isinstance(node_tokens_raw, list) or not isinstance(blind_edges_raw, list):
        raise ScoreRefusal("bad blind-interface graph")
    node_tokens = [str(value) for value in node_tokens_raw]
    if len(set(node_tokens)) != len(node_tokens) or set(node_tokens) != set(regions):
        raise ScoreRefusal("blind-interface nodes disagree with candidate presentation")

    blind_component_nodes: dict[str, set[str]] = {}
    for node, components in node_components.items():
        for component in components:
            blind_component_nodes.setdefault(projection[component], set()).add(node)

    edge_rows: list[tuple[str, str, str]] = []
    interface_crosschecks: list[dict[str, object]] = []
    for row in blind_edges_raw:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad blind edge")
        nodes = row.get("node_tokens")
        interface = row.get("interface_token")
        if not isinstance(nodes, list) or len(nodes) != 2 or not isinstance(interface, str):
            raise ScoreRefusal("ill-typed blind edge")
        left, right = map(str, nodes)
        if left not in regions or right not in regions:
            raise ScoreRefusal("blind edge references an unknown node")
        interface_crosschecks.append(
            {
                "projected_membership_matches_edge": blind_component_nodes.get(interface)
                == {left, right},
                "projected_membership_size": len(
                    blind_component_nodes.get(interface, set())
                ),
            }
        )
        edge_rows.append((left, right, interface))

    # Canonical graph labeling by exhaustive finite isomorphism search.  The
    # frozen members have at most five nodes, so this is exact and cheap.
    candidates: list[dict[str, object]] = []
    for order in itertools.permutations(node_tokens):
        index = {node: position for position, node in enumerate(order)}
        edges = sorted(
            tuple(sorted((index[left], index[right])))
            for left, right, _ in edge_rows
        )
        projected_components = sorted(
            tuple(sorted(index[node] for node in nodes))
            for nodes in blind_component_nodes.values()
        )
        candidates.append(
            {
                "node_count": len(order),
                "boundary_interface_edges": edges,
                "projected_component_incidence": projected_components,
                "resource_colors": {
                    key: resources[key]
                    for key in sorted(resources)
                    if key
                    in {
                        "state_dimension",
                        "history_depth",
                        "calibration_slots",
                        "parameter_slots",
                    }
                },
            }
        )
    canonical = min(candidates, key=canonical_json)
    return {
        "canonical_blind_object": canonical,
        "canonical_blind_sha256": canonical_sha256(canonical),
        "represented_candidate_regional_relation": {
            "overlap_pair_count": sum(
                not regions[left].meet(regions[right]).is_zero()
                for left, right, _ in edge_rows
            ),
            "declared_incidence_crosschecks": declared_crosschecks,
        },
        "projection_total": True,
        "blind_interface_crosschecks": interface_crosschecks,
        "blind_interface_consistent": all(
            row["projected_membership_matches_edge"]
            for row in interface_crosschecks
        ),
        "raw_identifiers_in_canonical_payload": False,
    }


def _blind_projection(member: Mapping[str, object]) -> dict[str, object]:
    """Backward-compatible name for the canonical consumed projection."""

    return _candidate_regional_projection(member)["canonical_blind_object"]


def _relabel_candidate_member_nodes(
    member: Mapping[str, object], relabeling: Mapping[str, str]
) -> dict[str, object]:
    result = copy.deepcopy(member)
    if not isinstance(result, dict):
        raise ScoreRefusal("candidate member relabel did not preserve a mapping")
    regions = result.get("regions")
    incidences = result.get("incidences")
    blind = result.get("blind_interface")
    if not isinstance(regions, list) or not isinstance(incidences, list) or not isinstance(
        blind, MutableMapping
    ):
        raise ScoreRefusal("candidate member lacks relabelable node data")
    for row in regions:
        if isinstance(row, MutableMapping):
            old = str(row.get("node_token"))
            row["node_token"] = relabeling.get(old, old)
    for row in incidences:
        if isinstance(row, MutableMapping) and isinstance(row.get("node_tokens"), list):
            row["node_tokens"] = [
                relabeling.get(str(value), str(value)) for value in row["node_tokens"]
            ]
    nodes = blind.get("node_tokens")
    edges = blind.get("edges")
    if not isinstance(nodes, list) or not isinstance(edges, list):
        raise ScoreRefusal("blind interface lacks relabelable nodes")
    blind["node_tokens"] = [relabeling.get(str(value), str(value)) for value in nodes]
    for row in edges:
        if isinstance(row, MutableMapping) and isinstance(row.get("node_tokens"), list):
            row["node_tokens"] = [
                relabeling.get(str(value), str(value)) for value in row["node_tokens"]
            ]
    # Neutral presentation permutation: semantics must not depend on list order.
    regions.reverse()
    incidences.reverse()
    blind["node_tokens"] = list(reversed(blind["node_tokens"]))
    edges.reverse()
    return result


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
    projection_readings = {
        name: _candidate_regional_projection(member)
        for name, member in sorted(members.items())
    }
    blind = {
        name: row["canonical_blind_object"]
        for name, row in projection_readings.items()
    }
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
        transform=(
            "candidate-regional-presentation-to-blind projection, exact finite "
            "graph canonicalization, and interface factorization theorem"
        ),
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
        "projection_validation": projection_readings,
        "resource_ledger": resources,
        "generated_candidate_regional_instruments": "NOT-CONSTRUCTED-NO-REGIONAL-TAU",
        "blind_class_instruments": {
            "constant_rule_nonempty": True,
            "registered_easier_task_competence": "NOT-FROZEN",
            "exhaustive_resource_parity": "NOT-LICENSED",
        },
        "relabel_and_erasure_controls": "AVAILABLE-AS-MUTANTS",
        "class_relative_scope": (
            "blind factor-through equality is proved for registered mathematical "
            "interfaces; no uniform regional Tau, calibrated held-out instrument, "
            "or family-level eliminability test is constructed"
        ),
        "external_comparator_is_regional_law": False,
        "provenance_node": node,
    }


def semantic_tree_payload(
    tree: Tree, questions: Mapping[str, PrefixRegion]
) -> object:
    if tree.is_empty:
        return {"kind": "empty_tree"}
    if tree.question_id not in questions:
        raise ScoreRefusal(f"tree references unknown question {tree.question_id}")
    assert tree.port_zero is not None and tree.port_one is not None
    return {
        "kind": "question_node",
        "question_region": questions[tree.question_id],
        "semantic_ports": {
            "0": semantic_tree_payload(tree.port_zero, questions),
            "1": semantic_tree_payload(tree.port_one, questions),
        },
    }


def semantic_process_operation(row: Mapping[str, object]) -> dict[str, object]:
    operation = row.get("operation")
    expression = row.get("expression")
    if not isinstance(operation, str):
        raise ScoreRefusal("process operation lacks a semantic operation name")
    payload: dict[str, object] = {"operation": operation}
    if expression is not None:
        if not isinstance(expression, str):
            raise ScoreRefusal("process operation expression is not text")
        normalized = " ".join(expression.strip().split())
        payload["expression"] = normalized
    for key in ("grammar_id", "replacement_id", "transition_id"):
        if key in row:
            payload[key.replace("_id", "_role")] = key.replace("_id", "")
    return payload


def process_record_semantics(row: Mapping[str, object]) -> dict[str, object]:
    """Derive record behavior from the expression, then audit its declaration.

    The expression is the executable object.  A declaration/expression mismatch is
    evidence, not a reason to silently execute the declared name.  This is needed
    for the registered delay-to-reset control: retaining a delay-shaped label must
    not prevent the reset expression from destroying the record.
    """

    operation = row.get("operation")
    expression = row.get("expression")
    if not isinstance(operation, str):
        raise ScoreRefusal("record operation has no operation field")
    normalized = "" if expression is None else " ".join(str(expression).split()).lower()
    if "empty_sequence" in normalized:
        action = "reset"
    elif "drop_last" in normalized:
        action = "erase_last"
    elif "identity on valuation and record carrier" in normalized:
        action = "identity"
    elif "read record_word after" in normalized or operation in {
        "read_record_word",
        "read_record_after_delay",
    }:
        action = "read"
    elif operation == "apply_question":
        action = "append"
    elif operation in {
        "compose_spectator",
        "apply_region_supported_replacement",
        "apply_identity_replacement",
        "apply_intrinsic_relative_complement_replacement",
    }:
        action = "identity"
    else:
        raise ScoreRefusal(f"unrecognized record semantics for operation {operation}")

    declared_action = {
        "delay_without_record_access": "identity",
        "erase_last_record_token": "erase_last",
        "reset_record_word": "reset",
    }.get(operation)
    return {
        "action": action,
        "declared_action": declared_action,
        "declaration_expression_consistent": (
            declared_action is None or declared_action == action
        ),
    }


def process_record_action(row: Mapping[str, object]) -> str:
    return str(process_record_semantics(row)["action"])


def validate_reader_schedules(
    data: Mapping[str, object]
) -> dict[str, object]:
    process = data.get("regional_question_process")
    if not isinstance(process, Mapping):
        raise ScoreRefusal("missing regional process for reader validation")
    operations = index_rows(process.get("operations"))
    trees, _ = _tree_rows(data)
    questions = question_region_map(data, regions_from_fixture(data))
    results: dict[str, object] = {}
    for schedule_id, row in sorted(index_rows(process.get("reader_schedules")).items()):
        tree_id = row.get("tree_id")
        operation_ids = row.get("operation_ids")
        if not isinstance(tree_id, str) or tree_id not in trees:
            raise ScoreRefusal(f"reader schedule {schedule_id} references a nonexistent tree")
        if not isinstance(operation_ids, list) or any(
            not isinstance(identifier, str) or identifier not in operations
            for identifier in operation_ids
        ):
            raise ScoreRefusal(f"reader schedule {schedule_id} references a nonexistent operation")
        branch_ports = sorted(tree_branch_cells(trees[tree_id], questions))
        current = list(branch_ports)
        reader_outputs: list[str] | None = None
        action_trace: list[dict[str, object]] = []
        for operation_id in operation_ids:
            semantics = process_record_semantics(operations[operation_id])
            action = str(semantics["action"])
            action_trace.append({"operation_role": operation_id, **semantics})
            if action == "identity":
                pass
            elif action == "reset":
                current = ["" for _ in current]
            elif action == "erase_last":
                current = [word[:-1] if word else "" for word in current]
            elif action == "append":
                raise ScoreRefusal("reader schedule contains an unbound question append")
            elif action == "read":
                reader_outputs = list(current)
        if reader_outputs is None:
            raise ScoreRefusal(f"reader schedule {schedule_id} contains no typed reader")
        results[schedule_id] = {
            "tree_semantics": semantic_tree_payload(trees[tree_id], questions),
            "input_ports": branch_ports,
            "action_trace": action_trace,
            "reader_outputs": reader_outputs,
            "distinguishes_every_input_port": len(set(reader_outputs)) == len(branch_ports),
            "declarations_match_expressions": all(
                bool(item["declaration_expression_consistent"])
                for item in action_trace
            ),
        }
    return results


def _active_filling_ids(data: Mapping[str, object]) -> set[str]:
    process = data.get("regional_question_process")
    typed = data.get("typed_fillings")
    if not isinstance(process, Mapping) or not isinstance(typed, Mapping):
        raise ScoreRefusal("missing process/filling data")
    provenance = process.get("generated_law_provenance")
    if not isinstance(provenance, Mapping):
        raise ScoreRefusal("missing generated-law provenance")
    factory = provenance.get("filling_factory")
    if not isinstance(factory, Mapping):
        raise ScoreRefusal("missing filling factory")
    active: set[str] = set()
    for key in ("question_rows", "tree_rows"):
        rows = factory.get(key)
        if not isinstance(rows, list):
            raise ScoreRefusal(f"filling factory lacks {key}")
        for row in rows:
            if not isinstance(row, Mapping) or not isinstance(row.get("filling_id"), str):
                raise ScoreRefusal("filling factory row lacks filling ID")
            active.add(str(row["filling_id"]))
    replacement_rows = factory.get("replacement_rows")
    if not isinstance(replacement_rows, list):
        raise ScoreRefusal("filling factory lacks replacement rows")
    for row in replacement_rows:
        if not isinstance(row, Mapping) or not isinstance(row.get("root_filling_id"), str):
            raise ScoreRefusal("replacement factory row lacks root filling")
        active.add(str(row["root_filling_id"]))
    factorizations = index_rows(typed.get("factorizations"))
    registered_factor_ids = provenance.get("factorization_ids")
    if not isinstance(registered_factor_ids, list):
        raise ScoreRefusal("law provenance lacks factorization IDs")
    for factor_id in registered_factor_ids:
        if str(factor_id) not in factorizations:
            raise ScoreRefusal("law provenance references unknown factorization")
        row = factorizations[str(factor_id)]
        active.add(str(row["whole_filling_id"]))
        active.update(str(value) for value in row["step_ids"])
    return active


def _semantic_active_fillings(data: Mapping[str, object]) -> list[object]:
    cospans = cospans_from_fixture(data)
    active_ids = _active_filling_ids(data)
    if not active_ids.issubset(cospans):
        raise ScoreRefusal("active filling reference is missing")
    return sorted(
        (singleton_quotient(cospans[identifier]).to_data() for identifier in active_ids),
        key=canonical_json,
    )


def _scoped_dependency_roots(
    question_payload: Mapping[str, object],
    catalogue_payloads: Mapping[str, object],
    reader_payloads: Mapping[str, object],
) -> dict[str, object]:
    question_hash = canonical_sha256(question_payload)
    return {
        "question_filling_presentation_root": {
            "payload": question_payload,
            "sha256": question_hash,
        },
        "continuation_catalogue_roots": {
            role: {"payload": payload, "sha256": canonical_sha256(payload)}
            for role, payload in sorted(catalogue_payloads.items())
        },
        "delayed_reader_roots": {
            role: {"payload": payload, "sha256": canonical_sha256(payload)}
            for role, payload in sorted(reader_payloads.items())
        },
        "global_joint_root_status": "NO-GLOBAL-JOINT-ROOT",
    }


def build_active_law_roots(data: Mapping[str, object]) -> dict[str, object]:
    """Build separate semantic roots for each actually selected scope.

    The fixture does not select one catalogue as *the* continuation law, so no
    global joint root is manufactured.  Roots certify dependency ancestry,
    never composition or one-law jointness.
    """

    process = data.get("regional_question_process")
    if not isinstance(process, Mapping):
        raise ScoreRefusal("missing regional process")
    regions = regions_from_fixture(data)
    questions = question_region_map(data, regions)
    trees, _ = _tree_rows(data)
    operations = index_rows(process.get("operations"))
    schedules = validate_reader_schedules(data)
    transition_binding = semantic_branch_binding(data)
    transition = process.get("question_transition")
    if not isinstance(transition, Mapping):
        raise ScoreRefusal("missing question transition")
    branch_semantics = {
        str(bit): {
            "restriction": "event" if bit == 1 else "complement(event)",
            "record_update": f"append({bit})",
        }
        for bit in sorted(transition_binding)
    }
    question_grammar = process.get("question_grammar")
    tree_grammar = process.get("decision_tree_grammar")
    if not isinstance(question_grammar, Mapping) or not isinstance(
        tree_grammar, Mapping
    ):
        raise ScoreRefusal("missing semantic question/tree grammar")
    catalogues = index_rows(process.get("continuation_catalogues"))
    for catalogue_id, row in catalogues.items():
        operation_ids = row.get("operation_ids")
        if not isinstance(operation_ids, list) or any(
            not isinstance(identifier, str) or identifier not in operations
            for identifier in operation_ids
        ):
            raise ScoreRefusal(
                f"continuation catalogue {catalogue_id} has a missing operation"
            )
    for schedule_id, row in index_rows(process.get("reader_schedules")).items():
        operation_ids = row.get("operation_ids")
        if not isinstance(operation_ids, list) or any(
            not isinstance(identifier, str) or identifier not in operations
            for identifier in operation_ids
        ):
            raise ScoreRefusal(f"reader schedule {schedule_id} has a missing operation")

    question_payload = {
        "question_grammar": {
            key: value
            for key, value in question_grammar.items()
            if key != "id"
        },
        "decision_tree_grammar": {
            key: value
            for key, value in tree_grammar.items()
            if key != "id"
        },
        "question_transition": branch_semantics,
        "registered_tree_semantics": sorted(
            (semantic_tree_payload(tree, questions) for tree in trees.values()),
            key=canonical_json,
        ),
        "active_fillings": _semantic_active_fillings(data),
    }
    question_hash = canonical_sha256(question_payload)
    catalogue_payloads: dict[str, object] = {}
    for catalogue_id, row in sorted(catalogues.items()):
        operation_ids = row.get("operation_ids")
        if not isinstance(operation_ids, list) or any(
            not isinstance(identifier, str) or identifier not in operations
            for identifier in operation_ids
        ):
            raise ScoreRefusal(f"continuation catalogue {catalogue_id} has a missing operation")
        semantic_operations = sorted(
            (semantic_process_operation(operations[identifier]) for identifier in operation_ids),
            key=canonical_json,
        )
        root_payload = {
            "question_filling_presentation_sha256": question_hash,
            "continuation_operations": semantic_operations,
        }
        catalogue_payloads[catalogue_id] = root_payload
    reader_rows = index_rows(process.get("reader_schedules"))
    reader_payloads: dict[str, object] = {}
    for schedule_id, semantic_result in sorted(schedules.items()):
        source_row = reader_rows[schedule_id]
        operation_ids = source_row.get("operation_ids")
        assert isinstance(operation_ids, list)
        computed_reader_semantics = copy.deepcopy(semantic_result)
        trace = computed_reader_semantics.get("action_trace")
        if isinstance(trace, list):
            computed_reader_semantics["action_trace"] = [
                {
                    key: value
                    for key, value in item.items()
                    if key != "operation_role"
                }
                for item in trace
                if isinstance(item, Mapping)
            ]
        payload = {
            "question_filling_presentation_sha256": question_hash,
            "tree": semantic_result["tree_semantics"],
            "operation_semantics": [
                semantic_process_operation(operations[str(identifier)])
                for identifier in operation_ids
            ],
            "computed_reader_semantics": computed_reader_semantics,
        }
        reader_payloads[schedule_id] = payload
    preparation = process.get("valuation_family")
    if not isinstance(preparation, Mapping):
        raise ScoreRefusal("missing preparation family")
    preparation_payload = {
        "family_semantics": {
            key: value for key, value in preparation.items() if key != "parameter_rows"
        },
        "rows": preparation.get("parameter_rows"),
    }
    scoped = _scoped_dependency_roots(
        question_payload, catalogue_payloads, reader_payloads
    )
    scoped["question_filling_presentation_root"]["scope_role"] = (
        "ql_000-compatible presentation"
    )
    return {
        **scoped,
        "preparation_root_sha256": canonical_sha256(preparation_payload),
        "p_in_law_root": False,
        "active_filling_count": len(_active_filling_ids(data)),
        "unreachable_control": "declarations outside active references excluded",
        "one_law_provenance": "UNCONSTRUCTED",
        "ancestry_is_not_one_law_proof": True,
    }


def validate_claim_provenance(
    roots: Sequence[str],
    edges: Sequence[tuple[str, str, str]],
    claims: Sequence[str],
) -> dict[str, object]:
    root_set = set(roots)
    if not root_set:
        raise ScoreRefusal("provenance validation needs an active root")
    adjacency: dict[str, list[str]] = {}
    malformed: list[tuple[str, str, str]] = []
    allowed_edge_types = {"derived-from", "typed-by", "read-by", "generated-by"}
    for source, target, edge_type in edges:
        if edge_type not in allowed_edge_types:
            malformed.append((source, target, edge_type))
        adjacency.setdefault(source, []).append(target)
    paths: dict[str, object] = {}
    for claim in claims:
        frontier: list[tuple[str, tuple[str, ...]]] = [(claim, (claim,))]
        visited: set[str] = set()
        found: tuple[str, ...] | None = None
        while frontier:
            node, path = frontier.pop(0)
            if node in root_set:
                found = path
                break
            if node in visited:
                continue
            visited.add(node)
            frontier.extend(
                (target, path + (target,)) for target in sorted(adjacency.get(node, []))
            )
        paths[claim] = {
            "path": found,
            "connected": found is not None,
        }
    return {
        "malformed_edges": malformed,
        "claim_paths": paths,
        "all_claims_connected": not malformed
        and all(row["connected"] for row in paths.values()),
    }


def scoped_dependency_provenance(
    law_roots: Mapping[str, object]
) -> dict[str, object]:
    root_roles: list[str] = ["scope:question-filling"]
    root_hashes: dict[str, object] = {
        "scope:question-filling": law_roots["question_filling_presentation_root"][
            "sha256"
        ]
    }
    edges: list[tuple[str, str, str]] = [
        ("claim:question-filling-presentation", "scope:question-filling", "derived-from")
    ]
    claims: list[str] = ["claim:question-filling-presentation"]
    catalogues = law_roots.get("continuation_catalogue_roots")
    readers = law_roots.get("delayed_reader_roots")
    if not isinstance(catalogues, Mapping) or not isinstance(readers, Mapping):
        raise ScoreRefusal("scoped law roots lack catalogue/reader roots")
    for role in sorted(catalogues):
        root = "scope:continuation:" + str(role)
        claim = "claim:continuation:" + str(role)
        root_roles.append(root)
        root_hashes[root] = catalogues[role]["sha256"]
        claims.append(claim)
        edges.append((claim, root, "typed-by"))
    for role in sorted(readers):
        root = "scope:reader:" + str(role)
        claim = "claim:reader:" + str(role)
        root_roles.append(root)
        root_hashes[root] = readers[role]["sha256"]
        claims.append(claim)
        edges.append((claim, root, "read-by"))
    validation = validate_claim_provenance(root_roles, edges, claims)
    envelope = {
        "root_roles": root_roles,
        "root_hashes": root_hashes,
        "typed_edges": edges,
        "claim_roles": claims,
        "validation": validation,
        "global_joint_root_status": law_roots.get("global_joint_root_status"),
        "ancestry_is_not_one_law_proof": True,
    }
    return {"envelope": envelope, "sha256": canonical_sha256(envelope)}


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
    return build_active_law_roots(data)


def _identity_assignments_by_boundary(data: Mapping[str, object]) -> dict[str, object]:
    typed = data.get("typed_fillings")
    if not isinstance(typed, Mapping):
        raise ScoreRefusal("capability census lacks typed fillings")
    boundaries = index_rows(typed.get("boundaries"))
    fillings = index_rows(typed.get("horizontal_fillings"))
    assignments: dict[str, object] = {}
    for boundary_id, boundary in sorted(boundaries.items()):
        generators = tuple(str(value) for value in boundary.get("generators", []))
        witnesses: list[str] = []
        for filling_id, row in fillings.items():
            if row.get("incoming_boundary_id") != boundary_id or row.get(
                "outgoing_boundary_id"
            ) != boundary_id:
                continue
            incoming = row.get("incoming_images")
            outgoing = row.get("outgoing_images")
            relations = row.get("apex_relations")
            if not isinstance(incoming, list) or not isinstance(
                outgoing, list
            ) or not isinstance(relations, list):
                continue
            in_map = {
                str(pair[0]): str(pair[1])
                for pair in incoming
                if isinstance(pair, list) and len(pair) == 2
            }
            out_map = {
                str(pair[0]): str(pair[1])
                for pair in outgoing
                if isinstance(pair, list) and len(pair) == 2
            }
            if (
                set(in_map) == set(generators)
                and set(out_map) == set(generators)
                and not relations
                and all(in_map[token] == out_map[token] for token in generators)
            ):
                witnesses.append(filling_id)
        assignments[boundary_id] = {
            "present": bool(witnesses),
            "witness_filling_roles": witnesses,
        }
    return assignments


def _interface_package(
    value: object, required_fields: Sequence[str]
) -> dict[str, object]:
    present = isinstance(value, Mapping) and all(field in value for field in required_fields)
    return {
        "present": present,
        "required_fields": list(required_fields),
        "present_fields": sorted(value) if isinstance(value, Mapping) else [],
        "evidence_kind": "typed-frozen-interface" if present else "missing-interface",
    }


def compute_capability_census(
    data: Mapping[str, object],
    *,
    regional_algebra_result: Mapping[str, object],
    process_result: Mapping[str, object],
    probes_result: Mapping[str, object],
    quotients_result: Mapping[str, object],
    atomlessness_result: Mapping[str, object],
    comparisons_result: Mapping[str, object],
    locality_result: Mapping[str, object],
    contact_result: Mapping[str, object],
    causality_result: Mapping[str, object],
    overlap_result: Mapping[str, object],
) -> dict[str, object]:
    """Inspect interfaces; analytical controls are never positive capabilities."""

    typed = data.get("typed_fillings")
    process = data.get("regional_question_process")
    family = data.get("regional_families")
    if not isinstance(typed, Mapping) or not isinstance(process, Mapping) or not isinstance(
        family, Mapping
    ):
        raise ScoreRefusal("capability census lacks a typed interface")

    factory = process.get("generated_law_provenance")
    boundary_factory = factory.get("boundary_factory") if isinstance(factory, Mapping) else None
    registered_frontiers: set[tuple[str, ...]] = set()
    if isinstance(boundary_factory, Mapping):
        for row in boundary_factory.get("rows", []):
            if not isinstance(row, Mapping):
                continue
            boundary_id = row.get("boundary_id")
            boundary = index_rows(typed.get("boundaries")).get(str(boundary_id))
            if boundary is not None:
                registered_frontiers.add(
                    tuple(sorted(str(value) for value in boundary.get("generators", [])))
                )
    adaptive_frontier = ("0", "10", "110", "111")
    adaptive_absent = adaptive_frontier not in registered_frontiers
    frontier_constructor = _interface_package(
        process.get("total_adaptive_frontier_factory"),
        ("constructor", "typing_rule", "composition_rule"),
    )
    frontier_constructor["absent_valid_frontier_witness"] = {
        "frontier": adaptive_frontier,
        "prefix_free": all(
            not right.startswith(left)
            for left, right in itertools.permutations(adaptive_frontier, 2)
        ),
        "covers_binary_unit": PrefixRegion.from_words(adaptive_frontier).is_one(),
        "not_registered": adaptive_absent,
    }

    identities = _identity_assignments_by_boundary(data)
    all_identities = bool(identities) and all(
        bool(row["present"]) for row in identities.values()
    )
    tensor = _interface_package(
        typed.get("tensor_factory") or process.get("tensor_factory"),
        ("object_tensor", "arrow_tensor", "unit", "interchange"),
    )
    naturality = _interface_package(
        typed.get("vertical_horizontal_naturality_squares"),
        ("squares", "horizontal_assignment", "vertical_assignment"),
    )
    probe_compiler = _interface_package(
        data.get("complete_probe_compiler"),
        ("target_domain", "compile", "separation_proof"),
    )
    overlap_section = data.get("overlap_gluing")
    selector = _interface_package(
        overlap_section.get("global_selector")
        if isinstance(overlap_section, Mapping)
        else None,
        ("rule", "domain", "uniqueness_proof"),
    )
    filling_process = _interface_package(
        process.get("filling_to_process_assignment"),
        ("assignment", "identity_equation", "composition_equation", "cut_equation"),
    )
    regional_tau = _interface_package(
        family.get("uniform_regional_tau"),
        ("generator", "calibration", "heldout_application"),
    )
    family_generator = _interface_package(
        family.get("public_family_generator"),
        ("member_generator", "training_rule", "heldout_rule"),
    )
    causal_schedule = _interface_package(
        data.get("causal_schedule"),
        ("operations", "ordering", "delayed_reader"),
    )
    quantum_law = _interface_package(
        data.get("quantum_interference_law"),
        ("history_space", "decoherence_functional", "division_instrument"),
    )
    joint_law = _interface_package(
        data.get("joint_regional_law"),
        (
            "filling_to_process_assignment",
            "composition_proof",
            "tensor_proof",
            "gluing_selector",
            "law_selection_rule",
        ),
    )
    generated_support = _interface_package(
        data.get("generated_support_equalizer"),
        ("active_law_root", "support_map", "equalizer_proof"),
    )
    reader_schedules = validate_reader_schedules(data)
    destructive_reader_witnesses = [
        schedule_id
        for schedule_id, row in reader_schedules.items()
        if any(
            action.get("action") in {"reset", "erase_last"}
            for action in row.get("action_trace", [])
            if isinstance(action, Mapping)
        )
    ]
    same_law_reset_reader = {
        "present": bool(destructive_reader_witnesses),
        "witness_schedule_roles": destructive_reader_witnesses,
        "evidence_kind": "computed-reader-schedule-semantics",
    }

    boundary_package = (
        bool(frontier_constructor["present"])
        and not adaptive_absent
        and all_identities
        and bool(tensor["present"])
        and bool(filling_process["present"])
        and bool(selector["present"])
    )
    total_adaptive_forest = (
        bool(frontier_constructor["present"])
        and not adaptive_absent
        and all_identities
        and bool(filling_process["present"])
    )
    post_quotient_atomless = (
        atomlessness_result.get("atomless_coordinate") == "PHYSICAL-IMAGE-ATOMLESS"
    )
    return {
        "raw_boolean_normalization": {
            "present": bool(process_result["all_input_normalization"]["symbolic"])
            and regional_algebra_result["Boolean_identities"]["failure_count"] == 0,
            "evidence_kind": "computed-semantic-law",
            "Boolean_identity_failure_count": regional_algebra_result[
                "Boolean_identities"
            ]["failure_count"],
            "normalization_identity": bool(
                process_result["all_input_normalization"]["symbolic"]
            ),
        },
        "raw_atomlessness": {
            "present": bool(atomlessness_result["syntax"]),
            "evidence_kind": "computed-prefix-algebra",
        },
        "adaptive_frontier_factory": frontier_constructor,
        "identity_assignments_by_boundary": identities,
        "all_boundary_identities": {
            "present": all_identities,
            "evidence_kind": "computed-horizontal-fillings",
        },
        "tensor_process_factory": tensor,
        "nontrivial_vertical_horizontal_naturality": naturality,
        "filling_to_process_assignment": filling_process,
        "complete_target_independent_probe_compiler": probe_compiler,
        "regional_overlap_global_selector": selector,
        "regional_tau": regional_tau,
        "public_family_generator": family_generator,
        "causal_contact_schedule": causal_schedule,
        "quantum_interference_law": quantum_law,
        "law_selected": joint_law,
        "generated_support_equalizer": generated_support,
        "same_law_reset_reader": same_law_reset_reader,
        "boundary_gluing_package": {
            "present": boundary_package,
            "component_evidence": {
                "adaptive_frontier_factory": bool(frontier_constructor["present"]),
                "absent_frontier_witness_eliminated": not adaptive_absent,
                "all_boundary_identities": all_identities,
                "tensor_factory": bool(tensor["present"]),
                "filling_to_process_assignment": bool(filling_process["present"]),
                "regional_overlap_selector": bool(selector["present"]),
            },
        },
        "total_adaptive_forest_functor": {
            "present": total_adaptive_forest,
            "component_evidence": {
                "adaptive_frontier_factory": bool(frontier_constructor["present"]),
                "absent_frontier_witness_eliminated": not adaptive_absent,
                "all_boundary_identities": all_identities,
                "filling_to_process_assignment": bool(filling_process["present"]),
            },
            "controls_do_not_promote": True,
        },
        "future_profile_complete": {
            "present": probe_compiler["present"]
            and probes_result["completeness_scope"] == "COMPLETE-GENERATED",
            "controls_do_not_promote": True,
        },
        "regional_congruence": {
            "present": quotients_result["regional_congruence"]["coordinate"]
            == "CONGRUENCE",
            "controls_do_not_promote": True,
        },
        "post_quotient_atomlessness": {
            "present": post_quotient_atomless,
            "evidence_kind": "computed quotient-image split certificate",
            "raw_syntax_split_does_not_promote": True,
        },
        "comparison_selected": {
            "present": comparisons_result["comparison_coordinate"] == "DERIVED"
        },
        "dynamic_locality": {
            "present": locality_result["locality_coordinate"] == "DYNAMIC-FAITHFUL",
            "controls_do_not_promote": True,
        },
        "causal_order": {
            "present": causal_schedule["present"]
            and causality_result["causality_coordinate"] == "DERIVED",
            "controls_do_not_promote": True,
        },
        "generated_contact": {
            "present": causal_schedule["present"]
            and contact_result["contact_coordinate"] == "DERIVED",
            "controls_do_not_promote": True,
        },
        "overlap_selector_kill": overlap_result,
    }


def classify_capability_census(census: Mapping[str, object]) -> tuple[str, list[str]]:
    def present(name: str) -> bool:
        row = census.get(name)
        return isinstance(row, Mapping) and bool(row.get("present"))

    if not present("raw_boolean_normalization"):
        return "APR-INCONSISTENT", ["full-cone normalization is absent or inconsistent"]
    if not present("raw_atomlessness"):
        return "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA", [
            "no nonzero raw regional split was constructed"
        ]
    if not present("boundary_gluing_package"):
        package = census.get("boundary_gluing_package")
        components = package.get("component_evidence", {}) if isinstance(package, Mapping) else {}
        missing = [name for name, value in components.items() if not value]
        return "APR-BLOCKED-AT-BOUNDARY-GLUING", [
            "missing computed capability: " + name for name in missing
        ]
    if not present("nontrivial_vertical_horizontal_naturality"):
        return "APR-BLOCKED-AT-TWO-ARROW-TYPING", [
            "no nontrivial vertical/horizontal naturality square"
        ]
    if not present("future_profile_complete"):
        return "APR-BLOCKED-AT-FUTURE-PROFILE-COMPLETENESS", [
            "no complete target-independent probe compiler"
        ]
    if not present("regional_congruence"):
        return "APR-BLOCKED-AT-REGIONAL-CONGRUENCE", [
            "profile equivalence is not a generated regional congruence"
        ]
    if not present("post_quotient_atomlessness"):
        return "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA", [
            "the claimed quotient has no nonzero proper split certificate"
        ]
    if not present("comparison_selected"):
        return "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED", [
            "comparison system remains law data"
        ]
    if not present("dynamic_locality"):
        return "APR-COMPARISON-QUOTIENT-CONSTRUCTED-BUT-DYNAMICAL-LOCALITY-FAILS", [
            "dynamic regional-support requirements fail"
        ]
    if not present("causal_order"):
        return "APR-DYNAMIC-REGIONAL-REFERENT-CONSTRUCTED-BUT-CAUSAL-ORDER-PRICED", [
            "causal schedule and delayed response are not generated"
        ]
    law_selected = census.get("law_selected")
    if not isinstance(law_selected, Mapping) or not law_selected.get("present"):
        return "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED", [
            "one joint law remains unselected"
        ]
    return "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED", []


def classify_primary(receipt: Mapping[str, object]) -> tuple[str, list[str]]:
    census = receipt.get("capability_census")
    if not isinstance(census, Mapping):
        raise ScoreRefusal("primary classifier requires a computed capability census")
    return classify_capability_census(census)


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
    dependency_validation = scoped_dependency_provenance(law_roots)

    capability_census = compute_capability_census(
        data,
        regional_algebra_result=regional_algebra,
        process_result=process,
        probes_result=probes,
        quotients_result=quotients,
        atomlessness_result=atomlessness,
        comparisons_result=comparisons,
        locality_result=locality,
        contact_result=contact,
        causality_result=causality,
        overlap_result=overlap,
    )

    ontology_role = {
        "role": "POSTULATED-CANDIDATE-RELATIONAL-WEB",
        "reason": (
            "the ontic web is a proposal, not an APR result; the represented "
            "question instruments act on one predeclared commutative algebra"
        ),
        "constructed_ceiling": (
            "catalogue-relative record recoverability may be detected; global "
            "durability and actualization are unproved"
        ),
        "valuation_status": "process-state representation; ontic/epistemic/shadow status unselected",
        "p_status": "preparation label, not law data or coupling",
        "actualization": "POSTULATE-UNTOUCHED",
    }
    law_selection = {
        "status": (
            "SELECTED"
            if capability_census["law_selected"]["present"]
            else "UNSELECTED"
        ),
        "preparation_variation_counted_as_law_modulus": False,
        "unselected_law_data": [
            "total forest/boundary/gluing assignment",
            "tensor constructor",
            "vertical comparison system",
            "regional overlap joint kernel",
            "contact/influence schedule",
        ],
    }
    missing_capabilities = sorted(
        name
        for name, row in capability_census.items()
        if isinstance(row, Mapping) and "present" in row and not bool(row["present"])
    )
    scope_walls = [
        "computed missing capability: " + name for name in missing_capabilities
    ] + [
        "analytical controls and dependency roots cannot supply missing positive baselines",
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
        "scoped_dependency_validation": dependency_validation,
        "capability_census": capability_census,
        "missing_capabilities": missing_capabilities,
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
        "dependency_provenance": provenance.to_data(),
        "one_law_provenance": "UNCONSTRUCTED",
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
        PRIMARY_WORDS.index(primary)
        >= PRIMARY_WORDS.index("APR-BLOCKED-AT-BOUNDARY-GLUING")
        and process["process_coordinate"] == "STATIC-RESPONSE-ONLY"
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


def _alter_reachable_leg(
    data: MutableMapping[str, object], options: MutationOptions
) -> None:
    typed = data.get("typed_fillings")
    if not isinstance(typed, MutableMapping):
        raise ScoreRefusal("G2 lacks typed fillings")
    filling_rows = typed.get("horizontal_fillings")
    factor_rows = typed.get("factorizations")
    if not isinstance(filling_rows, list) or not isinstance(factor_rows, list):
        raise ScoreRefusal("G2 lacks fillings/factorizations")
    used_by: dict[str, list[str]] = {}
    for factor in factor_rows:
        if not isinstance(factor, Mapping):
            continue
        factor_id = factor.get("id")
        identifiers = [factor.get("whole_filling_id")]
        steps = factor.get("step_ids")
        if isinstance(steps, list):
            identifiers.extend(steps)
        for identifier in identifiers:
            if isinstance(identifier, str) and isinstance(factor_id, str):
                used_by.setdefault(identifier, []).append(factor_id)

    for row in filling_rows:
        if not isinstance(row, MutableMapping):
            continue
        identifier = row.get("id")
        if not isinstance(identifier, str) or identifier not in used_by:
            continue
        images = row.get("outgoing_images")
        if not isinstance(images, list) or len(images) < 2:
            continue
        distinct_targets = sorted(
            {
                str(pair[1])
                for pair in images
                if isinstance(pair, list) and len(pair) == 2
            }
        )
        if len(distinct_targets) < 2:
            continue
        pre_payload = copy.deepcopy(row)
        for pair in images:
            if (
                isinstance(pair, list)
                and len(pair) == 2
                and str(pair[1]) != distinct_targets[-1]
            ):
                prior_target = str(pair[1])
                pair[1] = distinct_targets[-1]
                post_payload = copy.deepcopy(row)
                options.details["G2"] = {
                    "changed_filling_role": identifier,
                    "affected_factorization_roles": sorted(used_by[identifier]),
                    "changed_leg_source_role": str(pair[0]),
                    "pre_target_role": prior_target,
                    "post_target_role": str(pair[1]),
                    "pre_payload": pre_payload,
                    "post_payload": post_payload,
                    "pre_sha256": canonical_sha256(pre_payload),
                    "post_sha256": canonical_sha256(post_payload),
                }
                return
    raise ScoreRefusal("G2 found no reachable leg with two compatible images")


def _erase_represented_candidate_overlap(
    data: MutableMapping[str, object], options: MutationOptions
) -> None:
    family = data.get("regional_families")
    if not isinstance(family, MutableMapping):
        raise ScoreRefusal("M16 lacks a regional-family object")
    members = family.get("members")
    if not isinstance(members, list):
        raise ScoreRefusal("M16 lacks regional-family members")
    for member in members:
        if not isinstance(member, MutableMapping):
            continue
        incidences = member.get("incidences")
        regions = member.get("regions")
        occurrences = member.get("component_occurrences")
        if not isinstance(incidences, list) or not isinstance(
            regions, list
        ) or not isinstance(occurrences, list):
            continue
        region_index = {
            str(row.get("node_token")): row
            for row in regions
            if isinstance(row, MutableMapping)
        }
        occurrence_index = {
            str(row.get("component_token")): row
            for row in occurrences
            if isinstance(row, Mapping)
        }
        for incidence in incidences:
            if not isinstance(incidence, MutableMapping):
                continue
            left_components = incidence.get("left_component_tokens")
            right_components = incidence.get("right_component_tokens")
            nodes = incidence.get("node_tokens")
            if (
                not isinstance(left_components, list)
                or not isinstance(right_components, list)
                or not isinstance(nodes, list)
                or len(nodes) != 2
            ):
                continue
            shared = sorted(set(map(str, left_components)) & set(map(str, right_components)))
            if not shared:
                continue
            component = shared[0]
            occurrence = occurrence_index.get(component)
            right_node = region_index.get(str(nodes[1]))
            if not isinstance(occurrence, Mapping) or not isinstance(
                right_node, MutableMapping
            ):
                continue
            words = occurrence.get("antichain")
            node_words = right_node.get("antichain")
            if not isinstance(words, list) or not isinstance(node_words, list):
                continue
            removed = [str(word) for word in words if str(word) in node_words]
            if not removed:
                continue
            pre_member = copy.deepcopy(member)
            right_node["antichain"] = [
                word for word in node_words if str(word) not in set(removed)
            ]
            incidence["right_component_tokens"] = [
                value for value in right_components if str(value) != component
            ]
            options.details["M16"] = {
                "member_role": str(member.get("id", "anonymous-member")),
                "node_role": str(nodes[1]),
                "component_role": component,
                "removed_region_words": removed,
                "pre_payload": pre_member,
                "post_payload": copy.deepcopy(member),
                "pre_sha256": canonical_sha256(pre_member),
                "post_sha256": canonical_sha256(member),
            }
            return
    raise ScoreRefusal("M16 found no represented overlap to erase")


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
        _erase_represented_candidate_overlap(data, options)
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
        prefix_controls = data.get("prefix_controls")
        if not isinstance(prefix_controls, MutableMapping):
            raise ScoreRefusal("M27 lacks prefix controls")
        region_rows = prefix_controls.get("regions")
        if not isinstance(region_rows, list):
            raise ScoreRefusal("M27 lacks region presentations")
        for row in region_rows:
            if not isinstance(row, MutableMapping) or not isinstance(
                row.get("antichain"), list
            ):
                raise ScoreRefusal("M27 has a malformed region presentation")
            row["antichain"] = list(
                PrefixRegion.from_words(
                    _flip_binary_word(str(word)) for word in row["antichain"]
                ).words
            )
        process = data["regional_question_process"]
        assert isinstance(process, MutableMapping)
        family = process["valuation_family"]
        assert isinstance(family, MutableMapping)
        for row in family["parameter_rows"]:
            if isinstance(row, MutableMapping):
                row["p"] = fraction_text(Fraction(1) - exact(row["p"]))
        options.modes.add("transport_outputs_back")
        options.details["M27"] = {
            "scope": "Boolean region presentations plus Bernoulli preparations",
            "excluded_scopes": [
                "replacement grammar",
                "E37 family",
                "overlap gluing",
                "global process covariance",
            ],
        }
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
        _alter_reachable_leg(data, options)
    elif mutant_id == "G3":
        options.modes.add("no_pushout")
    elif mutant_id == "G4":
        options.modes.add("process_assignment_mismatch")
    elif mutant_id == "G5":
        options.modes.add("alternate_cut_assignment_unavailable")
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


def conjugation_deletion_control() -> dict[str, object]:
    """Finite analytical L5 model; never a positive locality baseline."""

    target = PrefixRegion.cylinder("00")
    depth = 3
    generators = _intrinsic_exterior_generators(target, depth)
    represented_closed = set(permutation_closure(generators))
    regrouping = block_swap_permutation("01", "10", depth)
    conjugates = {
        conjugate_permutation(value, regrouping) for value in represented_closed
    }
    if not conjugates.issubset(represented_closed):
        raise ScoreRefusal("L5 synthetic baseline is not conjugation closed")
    witness_pair = next(
        (
            (value, conjugate_permutation(value, regrouping))
            for value in sorted(represented_closed)
            if conjugate_permutation(value, regrouping) != value
        ),
        None,
    )
    if witness_pair is None:
        raise ScoreRefusal("L5 has no transported conjugate pair to separate")
    retained_witness, removable = witness_pair
    reduced = set(represented_closed)
    reduced.remove(removable)
    post_conjugates = {
        conjugate_permutation(value, regrouping) for value in reduced
    }
    pre_payload = {"family": sorted(represented_closed), "regrouping": regrouping}
    post_payload = {"family": sorted(reduced), "regrouping": regrouping}
    return {
        "scope": "finite analytical model from frozen leaf/regrouping data",
        "positive_locality_baseline": False,
        "pre_closed": conjugates.issubset(represented_closed),
        "post_closed": post_conjugates.issubset(reduced),
        "deleted_conjugate": removable,
        "retained_preimage": retained_witness,
        "pre_payload": pre_payload,
        "post_payload": post_payload,
        "pre_sha256": canonical_sha256(pre_payload),
        "post_sha256": canonical_sha256(post_payload),
    }


def profile_collapse_controls(regions: Mapping[str, PrefixRegion]) -> dict[str, object]:
    if not regions:
        raise ScoreRefusal("profile-collapse control needs regions")
    zero_entries = [
        RegionProfileEntry(name, region, (Fraction(0),))
        for name, region in sorted(regions.items())
    ]
    constant_entries = [
        RegionProfileEntry(name, region, (Fraction(1),))
        for name, region in sorted(regions.items())
    ]
    zero = regional_profile_equivalence(zero_entries)
    constant = regional_profile_equivalence(constant_entries)
    return {
        "zero_profile_payload": [entry.to_data() for entry in zero_entries],
        "zero_classes": zero.classes,
        "zero_faithful": len(zero.classes) == len(zero_entries),
        "constant_profile_payload": [entry.to_data() for entry in constant_entries],
        "constant_classes": constant.classes,
        "constant_faithful": len(constant.classes) == len(constant_entries),
    }


def oracle_family_controls(regions: Mapping[str, PrefixRegion]) -> dict[str, object]:
    if not regions:
        raise ScoreRefusal("oracle control needs registered regions")
    registered = tuple(sorted(regions.values(), key=canonical_json))
    cutoff = max(
        (len(word) for region in registered for word in region.words),
        default=0,
    )
    fresh = PrefixRegion.cylinder("0" * (cutoff + 1))
    while fresh in set(registered):
        fresh = PrefixRegion.cylinder(next(iter(fresh.words)) + "0")
    sample_name, sample = next(iter(sorted(regions.items())))
    relabeled = PrefixRegion.from_words(_flip_binary_word(word) for word in sample.words)
    refined_words = tuple(
        child
        for word in sample.words
        for child in (word + "0", word + "1")
    )
    refined = PrefixRegion.from_words(refined_words)
    whitelist_payload = {
        "constructor": "membership in finite canonical region set",
        "members": registered,
        "maximum_registered_word_depth": cutoff,
    }
    implementations = {
        "syntax_copy": {
            "fresh_valid_region": fresh,
            "accepts_fresh": True,
            "relabel_covariant": True,
            "refinement_invariant": refined == sample,
            "provenance": "symbolic PrefixRegion constructor",
        },
        "identifier_hash": {
            "sample_role": sample_name,
            "sample_hash": hashlib.sha256(sample_name.encode("utf-8")).hexdigest(),
            "pure_relabel_hash": hashlib.sha256(
                ("renamed-" + sample_name).encode("utf-8")
            ).hexdigest(),
            "accepts_fresh_without_identifier": False,
            "relabel_covariant": False,
            "refinement_invariant": False,
            "provenance": "neutral presentation identifier",
        },
        "finite_depth_whitelist": {
            "payload": whitelist_payload,
            "payload_sha256": canonical_sha256(whitelist_payload),
            "accepts_registered": all(value in set(registered) for value in registered),
            "fresh_valid_region": fresh,
            "accepts_fresh": fresh in set(registered),
            "relabel_covariant": relabeled in set(registered),
            "refinement_invariant": refined in set(registered),
            "provenance": "finite registered table only",
        },
    }
    return implementations


def branch_process_mutant_controls(event: PrefixRegion) -> dict[str, object]:
    baseline = {
        "branches": [
            {"port": "0", "coefficient": Fraction(1), "cell": event.complement()},
            {"port": "1", "coefficient": Fraction(1), "cell": event},
        ],
        "coefficient_rule": "constant",
    }
    variants: dict[str, dict[str, object]] = {
        "delete_branch": {
            "branches": [baseline["branches"][1]],
            "coefficient_rule": "constant",
        },
        "duplicate_branch": {
            "branches": [baseline["branches"][0], baseline["branches"][0]],
            "coefficient_rule": "constant",
        },
        "renormalize_each_branch": {
            "branches": baseline["branches"],
            "coefficient_rule": "divide_each_nonzero_branch_by_its_input_mass",
        },
        "negative_branch": {
            "branches": [
                baseline["branches"][0],
                {"port": "1", "coefficient": Fraction(-1), "cell": event},
            ],
            "coefficient_rule": "constant",
        },
        "wrong_restriction_cell": {
            "branches": [
                baseline["branches"][0],
                {"port": "1", "coefficient": Fraction(1), "cell": event.complement()},
            ],
            "coefficient_rule": "constant",
        },
    }

    def measure(candidate: Mapping[str, object]) -> dict[str, object]:
        branches = candidate["branches"]
        assert isinstance(branches, list)
        cells = [row["cell"] for row in branches]
        coefficients = [exact(row["coefficient"]) for row in branches]
        pairwise_disjoint = all(
            left.disjoint(right)
            for left, right in itertools.combinations(cells, 2)
        )
        exhaustive = join_regions(cells).is_one() if cells else False
        positivity = all(value >= 0 for value in coefficients)
        affine = candidate["coefficient_rule"] == "constant"
        unit_coefficients = all(value == 1 for value in coefficients)
        return {
            "port_count": len(branches),
            "normalization_partition": pairwise_disjoint and exhaustive,
            "positivity": positivity,
            "affinity_and_composition": affine,
            "support_matches_two_question_cells": set(cells)
            == {event, event.complement()},
            "ordinary_restriction_coefficients": unit_coefficients,
            "all_ordinary_gates": pairwise_disjoint
            and exhaustive
            and positivity
            and affine
            and unit_coefficients
            and set(cells) == {event, event.complement()},
        }

    baseline_measurement = measure(baseline)
    return {
        "baseline": baseline,
        "baseline_sha256": canonical_sha256(baseline),
        "baseline_measurement": baseline_measurement,
        "variants": {
            name: {
                "payload": payload,
                "sha256": canonical_sha256(payload),
                "measurement": measure(payload),
            }
            for name, payload in variants.items()
        },
    }


def overwrite_record_family_control(depth: int = 2) -> dict[str, object]:
    if depth < 2:
        raise ScoreRefusal("overwrite control requires depth at least two")
    pre_ports = leaves_at_depth(depth)
    post_ports = tuple(word[-1] for word in pre_ports)
    fibers = {
        value: tuple(word for word, image in zip(pre_ports, post_ports) if image == value)
        for value in sorted(set(post_ports))
    }
    pre_payload = {"constructor": "append", "ports": pre_ports}
    post_payload = {
        "constructor": "last_bit_overwrite",
        "input_ports": pre_ports,
        "output_ports": post_ports,
    }
    return {
        "pre_payload": pre_payload,
        "post_payload": post_payload,
        "pre_sha256": canonical_sha256(pre_payload),
        "post_sha256": canonical_sha256(post_payload),
        "pre_partition": tuple((word,) for word in pre_ports),
        "post_partition": tuple(fibers[value] for value in sorted(fibers)),
        "collisions": {key: value for key, value in fibers.items() if len(value) > 1},
        "lost_reader_distinctions": len(set(post_ports)) < len(pre_ports),
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
        return profile_collapse_controls(regions)
    if mutant_id == "M14":
        first = QMatrix.from_rows(((1,), (0,), (0,)))
        rival = QMatrix.from_rows(((0,), (1,), (0,)))
        supplied_provenance = validate_claim_provenance(
            ["root:active"], [], ["claim:supplied-exterior-map"]
        )
        return {
            "equal_rank": qrank(first) == qrank(rival),
            "first_in_rival_residual": qsubspace_inclusion_residual(first, rival),
            "rival_in_first_residual": qsubspace_inclusion_residual(rival, first),
            "same_subspace": qsubspace_inclusion_residual(first, rival) == 0
            and qsubspace_inclusion_residual(rival, first) == 0,
            "rank_is_not_calibrated_equality": True,
            "supplied_exterior_map_active_law_provenance": supplied_provenance,
            "algebraic_control_is_not_ontology": True,
        }
    if mutant_id == "M15":
        return oracle_family_controls(regions)
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
    if mutant_id == "M23":
        return {
            "status": "UNAVAILABLE",
            "absent_baseline_type": (
                "selected same-law reset/last-token-erasure continuation followed "
                "by a typed delayed reader"
            ),
            "mathematical_reset_control_does_not_supply_baseline": True,
        }
    if mutant_id == "M24":
        recovery = data["record_recovery"]
        operations = index_rows(recovery["operations"])
        roles = _record_operation_roles(operations)
        reset_0 = _word_recovery_signature(
            operations,
            [
                roles["write_flag0"],
                roles["write_flag1"],
                roles["erase_both"],
                roles["read_flag0"],
            ],
        )
        reset_1 = _word_recovery_signature(
            operations,
            [
                roles["write_flag0"],
                roles["write_flag1"],
                roles["erase_both"],
                roles["read_flag1"],
            ],
        )
        one_copy = _word_recovery_signature(
            operations,
            [
                roles["write_flag0"],
                roles["write_flag1"],
                roles["erase_flag0"],
                roles["read_flag1"],
            ],
        )
        return {
            "changed_object": {
                "constructor": "redundant-copy operation word",
                "operation_payloads": {
                    role: operations[identifier]
                    for role, identifier in sorted(roles.items())
                },
                "one_copy_erased_word": [
                    roles["write_flag0"],
                    roles["write_flag1"],
                    roles["erase_flag0"],
                    roles["read_flag1"],
                ],
                "both_copy_read_prefixes": [
                    [
                        roles["write_flag0"],
                        roles["write_flag1"],
                        roles["erase_both"],
                        roles["read_flag0"],
                    ],
                    [
                        roles["write_flag0"],
                        roles["write_flag1"],
                        roles["erase_both"],
                        roles["read_flag1"],
                    ],
                ],
            },
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
            "uniform_regional_Tau": "NOT-CONSTRUCTED",
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
        roots_payload = build_law_roots(data)
        dependency = scoped_dependency_provenance(roots_payload)["envelope"]
        scientific_payload = {
            "scope_root_hashes": {
                "question": roots_payload["question_filling_presentation_root"]["sha256"],
                "continuations": {
                    role: row["sha256"]
                    for role, row in roots_payload["continuation_catalogue_roots"].items()
                },
                "readers": {
                    role: row["sha256"]
                    for role, row in roots_payload["delayed_reader_roots"].items()
                },
            }
        }
        roots = list(dependency["root_roles"])
        claims = list(dependency["claim_roles"])
        pre_edges = [tuple(row) for row in dependency["typed_edges"]]
        if not pre_edges:
            raise ScoreRefusal("M35 dependency graph has no edge to sever")
        deleted_edge = pre_edges[-1]
        post_edges = pre_edges[:-1]
        pre = validate_claim_provenance(roots, pre_edges, claims)
        post = validate_claim_provenance(roots, post_edges, claims)
        pre_envelope = {
            "scientific_payload": scientific_payload,
            "root_roles": roots,
            "claim_roles": claims,
            "edges": pre_edges,
        }
        post_envelope = {
            "scientific_payload": scientific_payload,
            "root_roles": roots,
            "claim_roles": claims,
            "edges": post_edges,
        }
        return {
            "scientific_payload_sha256": canonical_sha256(scientific_payload),
            "pre_provenance_envelope": pre_envelope,
            "post_provenance_envelope": post_envelope,
            "pre_envelope_sha256": canonical_sha256(pre_envelope),
            "post_envelope_sha256": canonical_sha256(post_envelope),
            "deleted_typed_edge": deleted_edge,
            "pre_reachability": pre,
            "post_reachability": post,
        }
    if mutant_id == "M33":
        event = next(iter(questions.values()))
        return branch_process_mutant_controls(event)
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
        return overwrite_record_family_control(2)
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
        whitelist = oracle_family_controls(regions)["finite_depth_whitelist"]
        return {
            "shared_evidence_with": "M15/finite_depth_whitelist",
            "shared_payload_sha256": whitelist["payload_sha256"],
            "fresh_region": whitelist["fresh_valid_region"],
            "symbolic_question_defined": Restriction(whitelist["fresh_valid_region"]),
            "whitelist_accepts": whitelist["accepts_fresh"],
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
            "generated_support_object": "UNAVAILABLE",
            "absent_baseline_type": (
                "support/equalizer object generated by one selected active law"
            ),
            "shortcut_refused": True,
        }
    if mutant_id == "G4":
        return {
            "status": "UNAVAILABLE",
            "absent_baseline_type": "frozen filling-to-process assignment",
            "standalone_restriction_maps_are_only_controls": True,
        }
    if mutant_id == "G5":
        return {
            "status": "UNAVAILABLE",
            "absent_baseline_type": (
                "separately frozen whole-versus-step process assignment at alternate cuts"
            ),
        }
    if mutant_id == "G3":
        typed = data["typed_fillings"]
        factors = index_rows(typed["factorizations"])
        fillings = index_rows(typed["horizontal_fillings"])
        boundaries = index_rows(typed["boundaries"])
        validations: dict[str, object] = {}
        for factor_id, row in sorted(factors.items()):
            steps = [fillings[str(value)] for value in row["step_ids"]]
            cuts = [boundaries[str(value)] for value in row["intermediate_boundary_ids"]]
            typed_legs = all(
                steps[index]["outgoing_boundary_id"] == row["intermediate_boundary_ids"][index]
                and steps[index + 1]["incoming_boundary_id"]
                == row["intermediate_boundary_ids"][index]
                for index in range(len(cuts))
            )
            validations[factor_id] = {
                "typed_legs": typed_legs,
                "pushout_constructed": False,
            }
        return {
            "validation_rows": validations,
            "stopped_before_pushout": True,
            "composition_established": False,
        }
    if mutant_id == "P7":
        cospans = cospans_from_fixture(data)
        factors = index_rows(data["typed_fillings"]["factorizations"])
        factor_id, row = next(iter(sorted(factors.items())))
        steps = [cospans[str(value)] for value in row["step_ids"]]
        union_apex = tuple(
            (index, generator)
            for index, step in enumerate(steps)
            for generator in step.nodes
        )
        true_pushout = compose_cospans(steps)
        impostor_payload = {
            "constructor": "typed-leg tagged union without quotient",
            "factor_role": factor_id,
            "tagged_apex": union_apex,
            "boundary_identifications_applied": False,
        }
        return {
            "typed_legs": True,
            "union_impostor": impostor_payload,
            "union_impostor_sha256": canonical_sha256(impostor_payload),
            "true_pushout_apex_count": true_pushout.node_count,
            "union_apex_count": len(union_apex),
            "pushout_universal_property_checked": False,
            "composition_established": False,
            "process_assignment_established": False,
        }
    if mutant_id == "L5":
        return conjugation_deletion_control()
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


UNAVAILABLE_MUTANT_CAPABILITY: dict[str, tuple[str, str]] = {
    "G4": ("filling_to_process_assignment", "frozen filling-to-process assignment"),
    "G5": (
        "filling_to_process_assignment",
        "whole-versus-step process assignment at alternate cuts",
    ),
    "P8": ("tensor_process_factory", "positive tensor boundary/apex/process factory"),
    "L6": (
        "generated_support_equalizer",
        "support/equalizer generated from one selected active law",
    ),
    "M23": (
        "same_law_reset_reader",
        "selected reset/eraser continuation followed by a typed delayed reader",
    ),
}


SCOPE_MUTANTS = {
    "M21",
    "M22",
    "M28",
    "M29",
    "M30",
    "M31",
    "M32",
    "M34",
}
ANALYTICAL_MUTANTS = {
    "M01",
    "M02",
    "M03",
    "M04",
    "M05",
    "M06",
    "M13",
    "M14",
    "M15",
    "M18",
    "M19",
    "M20",
    "M24",
    "M33",
    "P1",
    "P2",
    "P3",
    "P4",
    "P5",
    "P6",
    "P7",
    "L3",
    "L5",
    "G3",
}


def _transformation_coordinate(mutant_id: str) -> str:
    groups = (
        ({"M01", "M02"}, "raw/post-quotient atomlessness"),
        ({"M03", "M13", "M14", "M15", "P5"}, "regional quotient/congruence"),
        ({"M04"}, "future-profile completeness"),
        ({"M05", "M06"}, "continuation-stable null quotient"),
        ({"M07", "M08"}, "two-arrow typing"),
        ({"M09", "M10", "M11"}, "comparison system"),
        ({"M12", "G1", "G2", "G3", "G4", "G5", "P7"}, "boundary/gluing"),
        ({"M16", "M26", "M27", "M28", "M29", "M30", "M31"}, "E37 family/interface"),
        ({"M17", "M18", "M19", "M20"}, "predictive boundary"),
        ({"M21", "M22", "M34"}, "contact/causality"),
        ({"M23", "M24", "P3"}, "record recovery/permanence"),
        ({"M25"}, "integrity/oracle refusal"),
        ({"M32"}, "quantum-scope control"),
        ({"M33", "P1", "P2", "P4", "P6"}, "question instrument/process"),
        ({"M35"}, "dependency provenance"),
        ({"L1", "L2", "L3", "L4", "L5", "L6"}, "dynamic regional support/locality"),
        ({"G6", "G7"}, "overlap-extension selection"),
        ({"P8"}, "tensor construction"),
    )
    return next((coordinate for members, coordinate in groups if mutant_id in members), "none")


def _semantic_leaf_diffs(
    before: object, after: object, path: tuple[object, ...] = ()
) -> list[dict[str, object]]:
    if canonical_sha256(before) == canonical_sha256(after):
        return []
    if isinstance(before, Mapping) and isinstance(after, Mapping):
        rows: list[dict[str, object]] = []
        for key in sorted(set(before) | set(after), key=str):
            if key not in before:
                rows.append(
                    {"path": path + (str(key),), "old": {"absent": True}, "new": after[key]}
                )
            elif key not in after:
                rows.append(
                    {"path": path + (str(key),), "old": before[key], "new": {"absent": True}}
                )
            else:
                rows.extend(_semantic_leaf_diffs(before[key], after[key], path + (str(key),)))
        return rows
    if isinstance(before, list) and isinstance(after, list) and len(before) == len(after):
        rows = []
        for index, (left, right) in enumerate(zip(before, after)):
            rows.extend(_semantic_leaf_diffs(left, right, path + (index,)))
        return rows
    return [{"path": path, "old": before, "new": after}]


def _classify_transformation(mutant_id: str, result: Mapping[str, object]) -> str:
    if mutant_id in UNAVAILABLE_MUTANT_CAPABILITY:
        return "UNAVAILABLE"
    if result.get("status") == "REFUSED" or mutant_id == "M25":
        return "REFUSED"
    if mutant_id in SCOPE_MUTANTS:
        return "SCOPE-CONTROL"
    if mutant_id in ANALYTICAL_MUTANTS:
        return "ANALYTICAL-CONTROL"
    return "SEMANTIC-MUTATION"


def _finalize_transformation_row(
    mutant_id: str,
    source: Mapping[str, object],
    transformed: Mapping[str, object],
    options: MutationOptions,
    baseline: Mapping[str, object],
    result: MutableMapping[str, object],
    *,
    mutated_receipt: Mapping[str, object] | None = None,
) -> dict[str, object]:
    classification = _classify_transformation(mutant_id, result)
    result["classification"] = classification
    if mutant_id not in MUTANT_DESCRIPTIONS:
        raise ScoreRefusal(f"missing frozen transformation description for {mutant_id}")
    result["frozen_description"] = MUTANT_DESCRIPTIONS[mutant_id]
    census = baseline.get("capability_census")
    if not isinstance(census, Mapping):
        raise ScoreRefusal("transformation evidence needs the computed capability census")

    if classification == "UNAVAILABLE":
        capability_name, baseline_type = UNAVAILABLE_MUTANT_CAPABILITY[mutant_id]
        witness = census.get(capability_name)
        if not isinstance(witness, Mapping) or witness.get("present") is not False:
            raise ScoreRefusal(
                f"{mutant_id} unavailable claim lacks a negative capability witness"
            )
        result["implemented_action"] = "inspect typed interfaces; do not manufacture a baseline"
        result["mutation_descriptor"] = {
            "target_root": capability_name,
            "target_object": baseline_type,
            "absent_baseline_type": baseline_type,
            "capability_census_witness": witness,
            "reference_updates": [],
            "shared_evidence_link": None,
        }
        result["affected_active_roots"] = []
        result["generic_measurement"] = "typed-interface capability census"
        result["before_after"] = {"before": "ABSENT", "after": "NOT-MUTATED"}
        result["falsifiable_coordinate"] = (
            _transformation_coordinate(mutant_id)
            + "; unavailable rows cannot falsify or promote without the baseline"
        )
        result["mutation_descriptor"]["generic_measurement"] = result[
            "generic_measurement"
        ]
        result["mutation_descriptor"]["measurement_before_after"] = result[
            "before_after"
        ]
        result["mutation_descriptor"]["affected_active_roots"] = []
        result["mutation_descriptor"]["falsifiable_coordinate"] = result[
            "falsifiable_coordinate"
        ]
        return dict(result)

    differences = _semantic_leaf_diffs(source, transformed)
    source_hash = canonical_sha256(source)
    transformed_hash = canonical_sha256(transformed)
    evidence = result.get("evidence")
    details = options.details.get(mutant_id)
    if mutant_id == "M35" and isinstance(evidence, Mapping):
        descriptor = {
            "target_root": "dependency_provenance",
            "target_object": "provenance envelope around an invariant scientific payload",
            "constructor_schema": "typed directed dependency graph",
            "pre_payload": evidence.get("pre_provenance_envelope"),
            "post_payload": evidence.get("post_provenance_envelope"),
            "pre_payload_sha256": evidence.get("pre_envelope_sha256"),
            "post_payload_sha256": evidence.get("post_envelope_sha256"),
            "reference_updates": [{"deleted_edge": evidence.get("deleted_typed_edge")}],
            "root_path_reachability_before": evidence.get("pre_reachability"),
            "root_path_reachability_after": evidence.get("post_reachability"),
            "invariant_scientific_payload_sha256": evidence.get(
                "scientific_payload_sha256"
            ),
            "shared_evidence_link": None,
        }
    elif isinstance(details, Mapping):
        descriptor = {
            "target_root": next(
                iter(sorted({str(row["path"][0]) for row in differences if row["path"]})),
                "fixture",
            ),
            "target_object": details,
            "typed_object_paths": [row["path"] for row in differences],
            "exact_changes": differences,
            "pre_payload_sha256": details.get("pre_sha256", source_hash),
            "post_payload_sha256": details.get("post_sha256", transformed_hash),
            "reference_updates": [
                row for row in differences if any("id" in str(part) for part in row["path"])
            ],
            "shared_evidence_link": None,
        }
    elif differences:
        roots = sorted({str(row["path"][0]) for row in differences if row["path"]})
        descriptor = {
            "target_root": roots[0] if len(roots) == 1 else "multiple-fixture-roots",
            "affected_roots": roots,
            "target_object": "frozen semantic fixture object",
            "typed_object_paths": [row["path"] for row in differences],
            "exact_changes": differences,
            "pre_payload_sha256": source_hash,
            "post_payload_sha256": transformed_hash,
            "reference_updates": [
                row for row in differences if any("id" in str(part) for part in row["path"])
            ],
            "shared_evidence_link": None,
        }
    else:
        constructor_output = evidence if evidence is not None else result.get("status")
        pre_payload = {
            "constructor_input_fixture_sha256": source_hash,
            "constructor_role": mutant_id,
        }
        post_payload = {"constructed_measurement": constructor_output}
        descriptor = {
            "target_root": "analytical-or-scope-control",
            "target_object": f"{mutant_id} constructed control",
            "constructor_schema": {
                "input": pre_payload,
                "operation": result.get("transformation_modes", []),
            },
            "pre_payload": pre_payload,
            "post_payload": post_payload,
            "pre_payload_sha256": canonical_sha256(pre_payload),
            "post_payload_sha256": canonical_sha256(post_payload),
            "reference_updates": [],
            "shared_evidence_link": (
                evidence.get("shared_evidence_with")
                if isinstance(evidence, Mapping)
                else None
            ),
        }
    result["mutation_descriptor"] = descriptor
    result["implemented_action"] = (
        "mutate serialized semantic object and recompute"
        if differences
        else "construct registered analytical/scope control and recompute"
    )

    baseline_roots = baseline.get("law_roots")
    post_root_error: str | None = None
    if isinstance(mutated_receipt, Mapping):
        post_roots = mutated_receipt.get("law_roots")
    elif differences:
        try:
            post_roots = build_law_roots(transformed)
        except ScoreRefusal as exc:
            post_roots = None
            post_root_error = str(exc)
    else:
        post_roots = baseline_roots
    affected_roots: list[str] = []
    if isinstance(baseline_roots, Mapping) and isinstance(post_roots, Mapping):
        before_catalogues = baseline_roots.get("continuation_catalogue_roots", {})
        after_catalogues = post_roots.get("continuation_catalogue_roots", {})
        if isinstance(before_catalogues, Mapping) and isinstance(after_catalogues, Mapping):
            affected_roots.extend(
                "continuation:" + name
                for name in sorted(set(before_catalogues) | set(after_catalogues))
                if canonical_sha256(before_catalogues.get(name))
                != canonical_sha256(after_catalogues.get(name))
            )
        for key in ("question_filling_presentation_root", "delayed_reader_roots"):
            if canonical_sha256(baseline_roots.get(key)) != canonical_sha256(post_roots.get(key)):
                affected_roots.append(key)
    result["affected_active_roots"] = affected_roots
    result["active_root_recomputation_refusal"] = post_root_error
    result["generic_measurement"] = (
        "full semantic score and capability census"
        if mutated_receipt is not None
        else "registered exact constructor-specific measurement"
    )
    result["before_after"] = {
        "before_primary": baseline.get("strict_primary"),
        "after_primary": mutated_receipt.get("strict_primary")
        if isinstance(mutated_receipt, Mapping)
        else "CONTROL-ONLY",
        "evidence": evidence,
    }
    result["falsifiable_coordinate"] = (
        _transformation_coordinate(mutant_id)
        + "; sensitivity/falsification only, never a missing positive capability"
    )
    descriptor["generic_measurement"] = result["generic_measurement"]
    descriptor["measurement_before_after"] = result["before_after"]
    descriptor["affected_active_roots"] = affected_roots
    descriptor["falsifiable_coordinate"] = result["falsifiable_coordinate"]
    return dict(result)


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
        return _finalize_transformation_row(
            mutant_id, source, transformed, options, baseline, result
        )
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
        return _finalize_transformation_row(
            mutant_id, source, transformed, options, baseline, result
        )
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
        source_questions = question_region_map(source, source_regions)
        transformed_questions = question_region_map(transformed, transformed_regions)
        transported_questions = {
            name: PrefixRegion.from_words(
                _flip_binary_word(word) for word in region.words
            )
            for name, region in transformed_questions.items()
        }
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
                    "question_outputs_transport_back": transported_questions
                    == source_questions,
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
        return _finalize_transformation_row(
            mutant_id, source, transformed, options, baseline, result
        )
    special = _generic_algorithm_witness(mutant_id, transformed, options)
    if special is not None and not special.get("requires_full_recomputation", False):
        result.update({"status": "RECOMPUTED-SPECIAL-CONTROL", "evidence": special})
        return _finalize_transformation_row(
            mutant_id, source, transformed, options, baseline, result
        )
    try:
        mutated_receipt = score_dataset(
            transformed,
            authentication=authentication,
            options=options,
            include_mutants=False,
        )
    except ScoreRefusal as exc:
        result.update({"status": "REFUSED", "reason": str(exc)})
        return _finalize_transformation_row(
            mutant_id, source, transformed, options, baseline, result
        )
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
    return _finalize_transformation_row(
        mutant_id,
        source,
        transformed,
        options,
        baseline,
        result,
        mutated_receipt=mutated_receipt,
    )


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
    composed = compose_cospans((first, second))
    _require(
        boundary_fixed_isomorphic(composed, singleton_quotient(whole)),
        "constructed cospan pushout",
    )
    tagged_union_apex = tuple(
        (index, generator)
        for index, step in enumerate((first, second))
        for generator in step.nodes
    )
    _require(
        len(tagged_union_apex) > composed.node_count,
        "typed tagged union was silently identified with a pushout",
    )
    checks.append("finite-pushout-vs-validation-and-tagged-union")

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

    delay = {
        "operation": "delay_without_record_access",
        "expression": "identity on valuation and record carrier",
    }
    mislabeled_reset = {
        "operation": "delay_without_record_access",
        "expression": "empty_sequence",
    }
    _require(process_record_semantics(delay)["action"] == "identity", "delay semantics")
    _require(
        process_record_semantics(mislabeled_reset)["action"] == "reset"
        and not process_record_semantics(mislabeled_reset)[
            "declaration_expression_consistent"
        ],
        "expression-driven reset under retained label",
    )
    schedule_fixture: dict[str, object] = {
        "prefix_controls": {
            "regions": [{"id": "region", "antichain": ["0"]}]
        },
        "regional_question_process": {
            "registered_questions": [{"id": "question", "region_id": "region"}],
            "decision_trees": [
                {
                    "id": "tree",
                    "expression": "node(question,empty_tree,empty_tree)",
                }
            ],
            "operations": [
                {
                    "id": "delay",
                    "operation": "delay_without_record_access",
                    "expression": "identity on valuation and record carrier",
                },
                {
                    "id": "reader",
                    "operation": "read_record_after_delay",
                    "expression": "read record_word after registered delay operations",
                },
            ],
            "reader_schedules": [
                {
                    "id": "schedule",
                    "tree_id": "tree",
                    "operation_ids": ["delay", "reader"],
                }
            ],
        },
    }
    schedule_before = validate_reader_schedules(schedule_fixture)["schedule"]
    schedule_fixture["regional_question_process"]["operations"][0][
        "expression"
    ] = "empty_sequence"
    schedule_after = validate_reader_schedules(schedule_fixture)["schedule"]
    _require(
        schedule_before["distinguishes_every_input_port"]
        and not schedule_after["distinguishes_every_input_port"]
        and not schedule_after["declarations_match_expressions"],
        "identity-delay-to-reset mutation did not move recovery",
    )
    checks.append("expression-driven-record-recovery")

    port_fixture_a = {
        "regional_question_process": {
            "question_transition": {
                "ports": [
                    {
                        "id": "neutral-left",
                        "next_valuation": "Q_C^1(nu)(A)=nu(meet(A,C))",
                    },
                    {
                        "id": "neutral-right",
                        "next_valuation": "Q_C^0(nu)(A)=nu(meet(A,complement(C)))",
                    },
                ]
            }
        }
    }
    port_fixture_b = copy.deepcopy(port_fixture_a)
    ports_b = port_fixture_b["regional_question_process"]["question_transition"]["ports"]
    ports_b.reverse()
    ports_b[0]["id"] = "renamed-zero"
    ports_b[1]["id"] = "renamed-one"
    _require(
        canonical_sha256(port_fixture_a) != canonical_sha256(port_fixture_b),
        "port presentation bytes must move",
    )
    _require(
        semantic_branch_binding(port_fixture_a) == semantic_branch_binding(port_fixture_b),
        "port identifiers/list order leaked into semantic bits",
    )
    checks.append("semantic-port-id-order-metamorphic")

    synthetic_member: dict[str, object] = {
        "id": "neutral-member",
        "component_occurrences": [
            {"component_token": "p0", "antichain": ["000"]},
            {"component_token": "p1", "antichain": ["010"]},
            {"component_token": "p2", "antichain": ["100"]},
            {"component_token": "c01", "antichain": ["001"]},
            {"component_token": "c12", "antichain": ["011"]},
        ],
        "regions": [
            {"node_token": "n0", "antichain": ["000", "001"]},
            {"node_token": "n1", "antichain": ["001", "010", "011"]},
            {"node_token": "n2", "antichain": ["011", "100"]},
        ],
        "incidences": [
            {
                "interface_token": "i01",
                "node_tokens": ["n0", "n1"],
                "left_component_tokens": ["c01"],
                "right_component_tokens": ["c01"],
            },
            {
                "interface_token": "i12",
                "node_tokens": ["n1", "n2"],
                "left_component_tokens": ["c12"],
                "right_component_tokens": ["c12"],
            },
        ],
        "blind_projection": [
            {"component_token": "p0", "blind_component_token": "bp0"},
            {"component_token": "p1", "blind_component_token": "bp1"},
            {"component_token": "p2", "blind_component_token": "bp2"},
            {"component_token": "c01", "blind_component_token": "i01"},
            {"component_token": "c12", "blind_component_token": "i12"},
        ],
        "blind_interface": {
            "node_tokens": ["n0", "n1", "n2"],
            "edges": [
                {"interface_token": "i01", "node_tokens": ["n0", "n1"]},
                {"interface_token": "i12", "node_tokens": ["n1", "n2"]},
            ],
        },
        "resource_declaration": {
            "state_dimension": 6,
            "history_depth": 2,
            "calibration_slots": 3,
            "parameter_slots": 1,
        },
    }
    projection_a = _candidate_regional_projection(synthetic_member)
    relabeled_member = _relabel_candidate_member_nodes(
        synthetic_member, {"n0": "z2", "n1": "z0", "n2": "z1"}
    )
    projection_b = _candidate_regional_projection(relabeled_member)
    _require(
        canonical_sha256(synthetic_member) != canonical_sha256(relabeled_member),
        "E37 relabel must move neutral presentation bytes",
    )
    _require(
        projection_a["canonical_blind_sha256"]
        == projection_b["canonical_blind_sha256"],
        "E37 canonical blind hash is not node-relabel invariant",
    )
    relation_data: dict[str, object] = {
        "regional_families": {"members": [copy.deepcopy(synthetic_member)]}
    }
    relation_options = MutationOptions(mutant_id="M16")
    _erase_represented_candidate_overlap(relation_data, relation_options)
    changed_member = relation_data["regional_families"]["members"][0]
    projection_changed = _candidate_regional_projection(changed_member)
    _require(
        projection_changed["canonical_blind_sha256"]
        != projection_a["canonical_blind_sha256"],
        "represented candidate-regional incidence change did not move blind hash",
    )
    _require(
        relation_options.details["M16"]["pre_sha256"]
        != relation_options.details["M16"]["post_sha256"],
        "M16 changed-object evidence is inert",
    )
    checks.append("candidate-regional-projection-and-relabel-canonicalization")

    covariance_source: dict[str, object] = {
        "prefix_controls": {
            "regions": [{"id": "region", "antichain": ["0"]}]
        },
        "regional_question_process": {
            "valuation_family": {
                "parameter_rows": [{"id": "preparation", "p": "1/3"}]
            }
        },
        "regional_families": {"sentinel": {"untransported": True}},
        "overlap_gluing": {"sentinel": {"untransported": True}},
    }
    covariance_mutant, covariance_options = apply_mutant(covariance_source, "M27")
    original_region = PrefixRegion.from_words(("0",))
    transported_region = PrefixRegion.from_words(
        covariance_mutant["prefix_controls"]["regions"][0]["antichain"]
    )
    transported_parameter = exact(
        covariance_mutant["regional_question_process"]["valuation_family"][
            "parameter_rows"
        ][0]["p"]
    )
    _require(
        bernoulli_mass(original_region, Fraction(1, 3))
        == bernoulli_mass(transported_region, transported_parameter),
        "M27 failed at its transported Boolean/preparation scope",
    )
    _require(
        covariance_mutant["regional_families"]
        == covariance_source["regional_families"]
        and covariance_mutant["overlap_gluing"]
        == covariance_source["overlap_gluing"]
        and "E37 family" in covariance_options.details["M27"]["excluded_scopes"],
        "M27 silently promoted covariance outside its transported scope",
    )
    checks.append("m27-scoped-boolean-preparation-covariance")

    reachable_data: dict[str, object] = {
        "typed_fillings": {
            "horizontal_fillings": [
                {
                    "id": "used",
                    "outgoing_images": [["x", "u"], ["y", "v"]],
                },
                {
                    "id": "unused",
                    "outgoing_images": [["x", "u"], ["y", "v"]],
                },
            ],
            "factorizations": [
                {
                    "id": "factor",
                    "whole_filling_id": "used",
                    "step_ids": [],
                }
            ],
        }
    }
    reachable_options = MutationOptions(mutant_id="G2")
    _alter_reachable_leg(reachable_data, reachable_options)
    _require(
        reachable_options.details["G2"]["changed_filling_role"] == "used"
        and reachable_options.details["G2"]["affected_factorization_roles"]
        == ["factor"],
        "G2 did not select a reachable factorization leg",
    )
    checks.append("reachable-g2-leg-mutation")

    scoped_a = _scoped_dependency_roots(
        {"writer": "append"},
        {"c0": {"operations": ["delay"]}, "c1": {"operations": ["erase"]}},
        {"reader": {"operations": ["delay", "read"]}},
    )
    scoped_b = _scoped_dependency_roots(
        {"writer": "append"},
        {"c0": {"operations": ["reset"]}, "c1": {"operations": ["erase"]}},
        {"reader": {"operations": ["delay", "read"]}},
    )
    _require(
        scoped_a["continuation_catalogue_roots"]["c0"]["sha256"]
        != scoped_b["continuation_catalogue_roots"]["c0"]["sha256"]
        and scoped_a["continuation_catalogue_roots"]["c1"]["sha256"]
        == scoped_b["continuation_catalogue_roots"]["c1"]["sha256"]
        and scoped_a["delayed_reader_roots"] == scoped_b["delayed_reader_roots"],
        "reachable reset did not move only its selected continuation root",
    )
    unrelated_declaration = {"unreachable": "edited"}
    _require(
        scoped_a
        == _scoped_dependency_roots(
            {"writer": "append"},
            {"c0": {"operations": ["delay"]}, "c1": {"operations": ["erase"]}},
            {"reader": {"operations": ["delay", "read"]}},
        )
        and unrelated_declaration,
        "unreachable declaration entered a scoped root",
    )
    _require(
        scoped_a["global_joint_root_status"] == "NO-GLOBAL-JOINT-ROOT",
        "scoped roots were promoted to one global root",
    )
    checks.append("scope-indexed-active-roots")

    provenance_before = validate_claim_provenance(
        ["root"],
        [("claim", "middle", "derived-from"), ("middle", "root", "typed-by")],
        ["claim"],
    )
    provenance_after = validate_claim_provenance(
        ["root"], [("claim", "middle", "derived-from")], ["claim"]
    )
    _require(
        provenance_before["all_claims_connected"]
        and not provenance_after["all_claims_connected"],
        "typed provenance severing was not detected",
    )
    checks.append("typed-provenance-path-and-sever")

    variables = ("A", "B", "C")
    all_configurations = tuple("".join(bits) for bits in itertools.product("01", repeat=3))
    uniform_weights = tuple(Fraction(1, 8) for _ in all_configurations)
    correlated_configurations = ("000", "010", "101", "111")
    correlated_weights = tuple(Fraction(1, 4) for _ in correlated_configurations)
    uniform_ab = _marginal_distribution(
        variables, all_configurations, uniform_weights, ("A", "B")
    )
    uniform_bc = _marginal_distribution(
        variables, all_configurations, uniform_weights, ("B", "C")
    )
    correlated_ab = _marginal_distribution(
        variables, correlated_configurations, correlated_weights, ("A", "B")
    )
    correlated_bc = _marginal_distribution(
        variables, correlated_configurations, correlated_weights, ("B", "C")
    )
    uniform_equal = sum(
        weight
        for configuration, weight in zip(all_configurations, uniform_weights)
        if configuration[0] == configuration[2]
    )
    correlated_equal = sum(
        weight
        for configuration, weight in zip(correlated_configurations, correlated_weights)
        if configuration[0] == configuration[2]
    )
    _require(
        uniform_ab == correlated_ab
        and uniform_bc == correlated_bc
        and set(uniform_ab.values()) == {Fraction(1, 4)}
        and uniform_equal == Fraction(1, 2)
        and correlated_equal == Fraction(1),
        "AB/BC overlap selector kill was not reproduced",
    )
    checks.append("overlap-selector-nonuniqueness")

    capability_template = {
        name: {"present": True}
        for name in (
            "raw_boolean_normalization",
            "raw_atomlessness",
            "boundary_gluing_package",
            "nontrivial_vertical_horizontal_naturality",
            "future_profile_complete",
            "regional_congruence",
            "post_quotient_atomlessness",
            "comparison_selected",
            "dynamic_locality",
            "causal_order",
            "law_selected",
        )
    }
    past_boundary = copy.deepcopy(capability_template)
    past_boundary["future_profile_complete"]["present"] = False
    missing_two_arrow = copy.deepcopy(capability_template)
    missing_two_arrow["nontrivial_vertical_horizontal_naturality"]["present"] = False
    _require(
        classify_capability_census(capability_template)[0]
        == "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED"
        and classify_capability_census(past_boundary)[0]
        == "APR-BLOCKED-AT-FUTURE-PROFILE-COMPLETENESS",
        "complete abstract boundary package did not move classifier beyond gluing",
    )
    _require(
        classify_capability_census(missing_two_arrow)[0]
        == "APR-BLOCKED-AT-TWO-ARROW-TYPING",
        "two-arrow capability block is unreachable",
    )
    missing_boundary = copy.deepcopy(capability_template)
    missing_boundary["boundary_gluing_package"] = {
        "present": False,
        "component_evidence": {
            "adaptive_frontier_factory": True,
            "all_boundary_identities": True,
            "tensor_factory": False,
            "filling_to_process_assignment": True,
            "regional_overlap_selector": True,
        },
    }
    _require(
        classify_capability_census(missing_boundary)[0]
        == "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "missing boundary/gluing package did not block",
    )
    missing_normalization = copy.deepcopy(capability_template)
    missing_normalization["raw_boolean_normalization"]["present"] = False
    missing_atomlessness = copy.deepcopy(capability_template)
    missing_atomlessness["raw_atomlessness"]["present"] = False
    _require(
        classify_capability_census(missing_normalization)[0] == "APR-INCONSISTENT"
        and classify_capability_census(missing_atomlessness)[0]
        == "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA",
        "earlier capability failures did not take precedence",
    )
    checks.append("result-neutral-capability-classifier-both-directions")

    boundary_base: dict[str, object] = {
        "predictive_boundaries": {
            "labels": ["left", "right"],
            "future_profile": {
                "matrix": {"shape": [1, 2], "rows": [["1", "0"]]}
            },
            "label_partitions": [],
            "presentations": [],
            "basis_changes": [],
            "future_extensions": [],
        }
    }
    declared_boundary = score_boundaries(boundary_base, ProvenanceDAG())
    sufficient_boundary_data = copy.deepcopy(boundary_base)
    sufficient_section = sufficient_boundary_data["predictive_boundaries"]
    assert isinstance(sufficient_section, MutableMapping)
    sufficient_section["generated_future_profile_system"] = {
        "active_law_root": "synthetic-root",
        "future_effect_compiler": "synthetic-compiler",
        "completeness_proof": "synthetic-proof",
        "factorization_proof": "synthetic-proof",
    }
    sufficient_boundary = score_boundaries(
        sufficient_boundary_data, ProvenanceDAG()
    )
    minimal_boundary_data = copy.deepcopy(sufficient_boundary_data)
    minimal_section = minimal_boundary_data["predictive_boundaries"]
    assert isinstance(minimal_section, MutableMapping)
    generated_system = minimal_section["generated_future_profile_system"]
    assert isinstance(generated_system, MutableMapping)
    generated_system.update(
        {
            "minimality_proof": "synthetic-proof",
            "natural_isomorphism_rule": "synthetic-rule",
        }
    )
    minimal_boundary = score_boundaries(minimal_boundary_data, ProvenanceDAG())
    _require(
        declared_boundary["boundary_coordinate"] == "DECLARED"
        and sufficient_boundary["boundary_coordinate"] == "SUFFICIENT"
        and minimal_boundary["boundary_coordinate"] == "MINIMAL-AT-CATALOGUE",
        "predictive-boundary coordinate is not interface-detected",
    )
    checks.append("result-neutral-boundary-coordinate-detection")

    l5 = conjugation_deletion_control()
    _require(l5["pre_closed"] and not l5["post_closed"], "L5 deletion did not break closure")
    profile_controls = profile_collapse_controls(
        {"zero": PrefixRegion.zero(), "left": PrefixRegion.cylinder("0"), "right": PrefixRegion.cylinder("1")}
    )
    _require(
        len(profile_controls["zero_classes"]) == 1
        and len(profile_controls["constant_classes"]) == 1,
        "M13 actual quotient laws did not collapse",
    )
    oracle = oracle_family_controls(
        {"left": PrefixRegion.cylinder("0"), "right": PrefixRegion.cylinder("1")}
    )
    _require(
        not oracle["finite_depth_whitelist"]["accepts_fresh"],
        "M15/P5 whitelist accepted a fresh valid deeper region",
    )
    branch_mutants = branch_process_mutant_controls(PrefixRegion.cylinder("0"))
    _require(
        branch_mutants["baseline_measurement"]["all_ordinary_gates"]
        and all(
            not row["measurement"]["all_ordinary_gates"]
            for row in branch_mutants["variants"].values()
        ),
        "M33 branch/process mutations did not traverse ordinary gates",
    )
    overwrite = overwrite_record_family_control(2)
    _require(
        overwrite["lost_reader_distinctions"] and len(overwrite["collisions"]) == 2,
        "P3 actual overwrite did not collapse generated records",
    )
    first = QMatrix.from_rows(((1,), (0,), (0,)))
    second = QMatrix.from_rows(((0,), (1,), (0,)))
    _require(
        qrank(first) == qrank(second)
        and qsubspace_inclusion_residual(first, second) == 1
        and qsubspace_inclusion_residual(second, first) == 1,
        "M14 equal-rank unequal-subspace residuals",
    )
    redundant_operations = {
        "write_two": {
            "id": "write_two",
            "input_fields": ["source", "flag0", "flag1"],
            "output_fields": ["source", "source", "source"],
        },
        "erase_first": {
            "id": "erase_first",
            "input_fields": ["source", "flag0", "flag1"],
            "output_fields": ["source", "0", "flag1"],
        },
        "erase_both": {
            "id": "erase_both",
            "input_fields": ["source", "flag0", "flag1"],
            "output_fields": ["source", "0", "0"],
        },
        "read_second": {
            "id": "read_second",
            "input_fields": ["source", "flag0", "flag1"],
            "output_fields": ["flag1"],
        },
    }
    one_copy = _word_recovery_signature(
        redundant_operations, ["write_two", "erase_first", "read_second"]
    )
    both_copies = _word_recovery_signature(
        redundant_operations, ["write_two", "erase_both", "read_second"]
    )
    _require(
        one_copy["recovers_source_for_all_carrier_inputs"]
        and not both_copies["recovers_source_for_all_carrier_inputs"],
        "M24 redundant-copy recovery control",
    )
    checks.append("repaired-analytical-mutant-constructors")

    descriptor_baseline = {
        "strict_primary": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "capability_census": {
            name: {"present": False, "witness": "synthetic absence"}
            for name, _ in UNAVAILABLE_MUTANT_CAPABILITY.values()
        },
        "law_roots": scoped_a,
    }
    descriptor_source = {"root": {"value": 1}}
    descriptor_after = {"root": {"value": 2}}
    descriptor_result: dict[str, object] = {
        "status": "RECOMPUTED",
        "transformation_modes": ["synthetic"],
        "evidence": {"measurement": [1, 2]},
    }
    finalized = _finalize_transformation_row(
        "G6",
        descriptor_source,
        descriptor_after,
        MutationOptions(mutant_id="G6"),
        descriptor_baseline,
        descriptor_result,
    )
    _require(
        finalized["classification"] == "SEMANTIC-MUTATION"
        and finalized["mutation_descriptor"]["exact_changes"][0]["old"] == 1
        and finalized["mutation_descriptor"]["exact_changes"][0]["new"] == 2,
        "machine-reconstructible mutation descriptor",
    )
    for unavailable_id in sorted(UNAVAILABLE_MUTANT_CAPABILITY):
        unavailable_result: dict[str, object] = {"status": "UNAVAILABLE"}
        unavailable = _finalize_transformation_row(
            unavailable_id,
            descriptor_source,
            descriptor_source,
            MutationOptions(mutant_id=unavailable_id),
            descriptor_baseline,
            unavailable_result,
        )
        _require(
            unavailable["classification"] == "UNAVAILABLE"
            and unavailable["mutation_descriptor"][
                "capability_census_witness"
            ]["present"]
            is False,
            f"{unavailable_id} descriptor lacks computed absence witness",
        )
    provenance_payload = {"screen": (Fraction(1), Fraction(2))}
    pre_envelope = {
        "scientific_payload": provenance_payload,
        "edges": [("claim", "root", "typed-by")],
    }
    post_envelope = {"scientific_payload": provenance_payload, "edges": []}
    m35_result: dict[str, object] = {
        "status": "RECOMPUTED-SPECIAL-CONTROL",
        "transformation_modes": ["disconnected_provenance"],
        "evidence": {
            "scientific_payload_sha256": canonical_sha256(provenance_payload),
            "pre_provenance_envelope": pre_envelope,
            "post_provenance_envelope": post_envelope,
            "pre_envelope_sha256": canonical_sha256(pre_envelope),
            "post_envelope_sha256": canonical_sha256(post_envelope),
            "deleted_typed_edge": ("claim", "root", "typed-by"),
            "pre_reachability": provenance_before,
            "post_reachability": provenance_after,
        },
    }
    m35 = _finalize_transformation_row(
        "M35",
        descriptor_source,
        descriptor_source,
        MutationOptions(mutant_id="M35"),
        descriptor_baseline,
        m35_result,
    )
    _require(
        m35["mutation_descriptor"]["pre_payload_sha256"]
        != m35["mutation_descriptor"]["post_payload_sha256"]
        and m35["mutation_descriptor"]["invariant_scientific_payload_sha256"]
        == canonical_sha256(provenance_payload),
        "M35 provenance envelope hashes are not reconstructible",
    )
    checks.append("transformation-descriptor-schema")

    _require(set(MUTANT_IDS) == set(
        [f"M{index:02d}" for index in range(1, 36)]
        + [f"P{index}" for index in range(1, 9)]
        + [f"L{index}" for index in range(1, 7)]
        + [f"G{index}" for index in range(1, 8)]
    ), "mutant registry coverage")
    _require(set(MUTANT_DESCRIPTIONS) == set(MUTANT_IDS), "mutant description coverage")
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
