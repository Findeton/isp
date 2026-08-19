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
import builtins
import copy
import hashlib
import itertools
import os
import re
import sys
import tempfile
from dataclasses import dataclass, field, replace
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
    qcolumnspace,
    qhstack,
    qkernel,
    qmultiply,
    qrank,
    qrowspace,
    qscale,
    qsubtract,
    qsubspace_inclusion_residual,
    qsubspace_intersection,
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
    "note-apr-v3-delta-repair-pin.md": "88c2941f2fb4c90ed8476a5e814ab116b66369f23661dbacf4f89555ea6dd7f0",
    "note-apr-v3-delta-repair-pin-addendum.md": "22eb137fc5496a73ae46fadaaba26f98451dbc5f45c266826c135f7542f63e88",
    "note-apr-v4-semantic-repair-pin.md": "3b0737e3f9a37966659f32a521f56df892cba8d9194530ea4560bc3bbc1d313d",
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
    "bcfdc0a",
    "61953d5",
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
STATIC_QUALIFIER = (
    "APR-STATIC-RAW-PREFIX-SYNTAX-ATOMLESS-RESPONSE-CONSTRUCTED-PROCESS-UNBUILT"
)

BLINDING_STATUS = "RESULT-KNOWN-BEFORE-V4-IMPLEMENTATION"
EXPOSURE_DEBT = "PERMANENT-PREFREEZE-M01-AND-ALL-MUTANTS-EXPOSURE"
REGIONAL_SUPPORT_SCOPE = (
    "finite regional-support controls only; regional-support coordinate unearned"
)
PREFIX_SYNTAX_SCOPE = (
    "raw prefix-syntax atomlessness only; physical regional referent unconstructed"
)

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
    "M16": "substitute c by blind-equivalent d on the first represented interface",
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


_RECORD_APPEND = re.compile(
    r"^append\(R,\(C,([A-Za-z_][A-Za-z0-9_-]*)\)\)$"
)


def _semantic_transition_ports(
    data: Mapping[str, object],
) -> dict[int, dict[str, object]]:
    """Bind a branch bit from its restriction and carry it through its writer.

    Neutral port identifiers are allowed to change, but the identifier consumed
    by ``next_record_word`` must be the identifier of the same semantic branch.
    Thus neither list position nor an identifier suffix can repair a crossed
    writer reference.
    """

    process = data.get("regional_question_process")
    if not isinstance(process, Mapping):
        raise ScoreRefusal("missing question process")
    transition = process.get("question_transition")
    if not isinstance(transition, Mapping) or not isinstance(transition.get("ports"), list):
        raise ScoreRefusal("missing question ports")
    found: dict[int, dict[str, object]] = {}
    identifiers: set[str] = set()
    for row in transition["ports"]:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad question port")
        formula = row.get("next_valuation")
        record_update = row.get("next_record_word")
        identifier = row.get("id")
        if (
            not isinstance(formula, str)
            or not isinstance(record_update, str)
            or not isinstance(identifier, str)
        ):
            raise ScoreRefusal("question port lacks formula or record update")
        compact = formula.replace(" ", "")
        has_complement_branch = "meet(A,complement(C))" in compact
        has_event_branch = "meet(A,C)" in compact
        if has_complement_branch == has_event_branch:
            raise ScoreRefusal("question branch formula has ambiguous semantic bit")
        if has_complement_branch:
            bit = 0
        elif has_event_branch:
            bit = 1
        if bit in found:
            raise ScoreRefusal("question transition does not supply one branch per semantic bit")
        if identifier in identifiers:
            raise ScoreRefusal("question transition repeats a neutral port identifier")
        identifiers.add(identifier)
        record_match = _RECORD_APPEND.fullmatch(record_update.replace(" ", ""))
        if record_match is None:
            raise ScoreRefusal("question record update is not a typed append")
        referenced_identifier = record_match.group(1)
        if referenced_identifier != identifier:
            raise ScoreRefusal(
                "question branch formula contradicts its next_record_word reference"
            )
        supplied_bit = row.get("semantic_bit")
        if supplied_bit is not None and supplied_bit != bit:
            raise ScoreRefusal("question branch supplies a contradictory semantic bit")
        found[bit] = {
            "restriction": "complement-event" if bit == 0 else "event",
            "neutral_port_role": identifier,
            "next_record_reference": referenced_identifier,
            "record_bit": bit,
        }
    if set(found) != {0, 1}:
        raise ScoreRefusal("question transition must supply Q^0 and Q^1")
    return found


def semantic_branch_binding(data: Mapping[str, object]) -> dict[int, str]:
    return {
        bit: str(row["restriction"])
        for bit, row in sorted(_semantic_transition_ports(data).items())
    }


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
            "scope": PREFIX_SYNTAX_SCOPE,
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


def _binary_record_word(token: object) -> str:
    if token in {"", "epsilon"}:
        return ""
    if not isinstance(token, str) or not token or set(token) - {"0", "1"}:
        raise ScoreRefusal("record boundary contains a nonsemantic port token")
    return token


def semantic_port_chain(
    data: Mapping[str, object],
    questions: Mapping[str, PrefixRegion],
    trees: Mapping[str, Tree],
    cospans: Mapping[str, FiniteCospan],
) -> dict[str, object]:
    """Reconstruct every frozen consumer of the question-branch bit.

    The returned invariant signature contains no neutral transition identifiers.
    The audit rows retain those identifiers only to make reference transport
    reconstructible.
    """

    transition_rows = _semantic_transition_ports(data)
    process = data.get("regional_question_process")
    typed = data.get("typed_fillings")
    if not isinstance(process, Mapping) or not isinstance(typed, Mapping):
        raise ScoreRefusal("semantic port chain lacks process or boundary data")
    boundaries = index_rows(typed.get("boundaries"))
    provenance = process.get("generated_law_provenance")
    if not isinstance(provenance, Mapping):
        raise ScoreRefusal("semantic port chain lacks generated provenance")
    boundary_factory = provenance.get("boundary_factory")
    filling_factory = provenance.get("filling_factory")
    if not isinstance(boundary_factory, Mapping) or not isinstance(
        filling_factory, Mapping
    ):
        raise ScoreRefusal("semantic port chain lacks boundary/filling factory")

    boundary_by_depth: dict[int, dict[str, object]] = {}
    boundary_rows = boundary_factory.get("rows")
    if not isinstance(boundary_rows, list):
        raise ScoreRefusal("semantic port boundary factory has no rows")
    for row in boundary_rows:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad semantic port boundary row")
        depth = row.get("tree_depth")
        boundary_id = row.get("boundary_id")
        if not isinstance(depth, int) or depth < 0 or not isinstance(boundary_id, str):
            raise ScoreRefusal("semantic port boundary row is ill typed")
        if depth in boundary_by_depth or boundary_id not in boundaries:
            raise ScoreRefusal("duplicate or missing semantic record boundary")
        generators = boundaries[boundary_id].get("generators")
        if not isinstance(generators, list):
            raise ScoreRefusal("semantic record boundary lacks generators")
        words = tuple(sorted(_binary_record_word(value) for value in generators))
        if len(words) != len(set(words)):
            raise ScoreRefusal("semantic record boundary has duplicate ports")
        expected = leaves_at_depth(depth)
        if words != expected:
            raise ScoreRefusal("record boundary ports contradict semantic bit words")
        boundary_by_depth[depth] = {
            "boundary_role": boundary_id,
            "semantic_ports": words,
        }

    question_rows = filling_factory.get("question_rows")
    tree_rows = filling_factory.get("tree_rows")
    if not isinstance(question_rows, list) or not isinstance(tree_rows, list):
        raise ScoreRefusal("semantic port filling factory lacks rows")
    question_factory_checks: list[dict[str, object]] = []
    for row in question_rows:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad question-filling port row")
        input_depth = row.get("input_depth")
        output_depth = row.get("output_depth")
        filling_id = row.get("filling_id")
        if (
            not isinstance(input_depth, int)
            or not isinstance(output_depth, int)
            or output_depth != input_depth + 1
            or not isinstance(filling_id, str)
            or filling_id not in cospans
            or input_depth not in boundary_by_depth
            or output_depth not in boundary_by_depth
        ):
            raise ScoreRefusal("question filling does not type one semantic bit append")
        filling = cospans[filling_id]
        incoming = tuple(sorted(_binary_record_word(value) for value in filling.incoming))
        outgoing = tuple(sorted(_binary_record_word(value) for value in filling.outgoing))
        if (
            incoming != boundary_by_depth[input_depth]["semantic_ports"]
            or outgoing != boundary_by_depth[output_depth]["semantic_ports"]
            or any(
                word[:-1] not in set(incoming) or word[-1] not in {"0", "1"}
                for word in outgoing
            )
        ):
            raise ScoreRefusal("question cospan ports contradict semantic append")
        question_factory_checks.append(
            {
                "input_depth": input_depth,
                "output_depth": output_depth,
                "incoming_ports": incoming,
                "outgoing_ports": outgoing,
            }
        )

    tree_factory_checks: dict[str, object] = {}
    for row in tree_rows:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("bad tree-filling port row")
        tree_id = row.get("tree_id")
        filling_id = row.get("filling_id")
        if (
            not isinstance(tree_id, str)
            or tree_id not in trees
            or not isinstance(filling_id, str)
            or filling_id not in cospans
        ):
            raise ScoreRefusal("tree-filling port row references a missing object")
        frontier = tuple(sorted(tree_branch_cells(trees[tree_id], questions)))
        filling = cospans[filling_id]
        incoming = tuple(sorted(_binary_record_word(value) for value in filling.incoming))
        outgoing = tuple(sorted(_binary_record_word(value) for value in filling.outgoing))
        if incoming != ("",) or outgoing != frontier:
            raise ScoreRefusal("tree frontier and cospan record ports contradict")
        tree_factory_checks[tree_id] = {
            "frontier": frontier,
            "incoming_ports": incoming,
            "outgoing_ports": outgoing,
            "binding_consistent": True,
        }

    downstream = process.get("port_to_bit_map")
    downstream_rows: list[dict[str, object]] = []
    if downstream is not None:
        if not isinstance(downstream, list):
            raise ScoreRefusal("downstream port-to-bit map is not a row list")
        observed: dict[str, int] = {}
        expected_by_id = {
            str(row["neutral_port_role"]): bit
            for bit, row in transition_rows.items()
        }
        for row in downstream:
            if not isinstance(row, Mapping):
                raise ScoreRefusal("bad downstream port-to-bit row")
            port_id = row.get("port_id")
            bit = row.get("bit")
            if (
                not isinstance(port_id, str)
                or type(bit) is not int
                or bit not in {0, 1}
                or port_id in observed
            ):
                raise ScoreRefusal("downstream port-to-bit map is nonfunctional")
            observed[port_id] = int(bit)
        if observed != expected_by_id:
            raise ScoreRefusal("downstream port-to-bit map contradicts branch formulas")
        downstream_rows = [
            {"semantic_bit": bit, "reference_present": True}
            for bit in sorted(observed.values())
        ]

    reader_rows = validate_reader_schedules(data)
    reader_bindings: dict[str, object] = {}
    for schedule_id, row in sorted(reader_rows.items()):
        if not row["distinguishes_every_input_port"]:
            raise ScoreRefusal("delayed reader does not preserve its semantic port binding")
        reader_bindings[schedule_id] = {
            "input_ports": row["input_ports"],
            "reader_outputs": row["reader_outputs"],
            "distinguishes_every_input_port": True,
        }

    invariant_signature = {
        "question_formula_to_bit": {
            str(bit): row["restriction"] for bit, row in transition_rows.items()
        },
        "record_append_bits": tuple(sorted(transition_rows)),
        "boundaries": {
            str(depth): row["semantic_ports"]
            for depth, row in sorted(boundary_by_depth.items())
        },
        "question_fillings": question_factory_checks,
        "tree_frontiers": tree_factory_checks,
        "reader_bindings": reader_bindings,
        "downstream_port_to_bit": downstream_rows,
    }
    return {
        "transition_audit": transition_rows,
        "transport_invariant_signature": invariant_signature,
        "transport_invariant_sha256": canonical_sha256(invariant_signature),
        "all_consumers_consistent": True,
    }


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


PROCESS_COORDINATES = (
    "SYNTAX-ONLY",
    "STATIC-RESPONSE-ONLY",
    "HORIZONTAL-CLASSICAL",
    "HORIZONTAL-QUANTUM",
    "INCONSISTENT",
)


def _substantive(value: object) -> bool:
    if value is None or value == "":
        return False
    if isinstance(value, (Mapping, list, tuple, set, frozenset)) and not value:
        return False
    return True


def _finite_unique_texts(value: object) -> tuple[str, ...] | None:
    if (
        not isinstance(value, list)
        or not value
        or any(not isinstance(item, str) or not item for item in value)
        or len(set(value)) != len(value)
    ):
        return None
    return tuple(value)


def _semantic_equation_family(
    value: object, active_root: str, role: str
) -> dict[str, object]:
    if not isinstance(value, list) or not value:
        return {"valid": False, "contradictory": False, "reason": f"missing {role}"}
    rows: list[dict[str, object]] = []
    contradictory = False
    for row in value:
        if not isinstance(row, Mapping):
            return {"valid": False, "contradictory": False, "reason": f"bad {role} row"}
        lhs = row.get("lhs")
        rhs = row.get("rhs")
        connected = row.get("active_root") == active_root
        substantive = _substantive(lhs) and _substantive(rhs)
        equal = substantive and canonical_sha256(lhs) == canonical_sha256(rhs)
        contradictory = contradictory or (substantive and connected and not equal)
        rows.append(
            {
                "lhs": lhs,
                "rhs": rhs,
                "connected": connected,
                "substantive": substantive,
                "equal": equal,
            }
        )
    return {
        "valid": all(row["connected"] and row["substantive"] and row["equal"] for row in rows),
        "contradictory": contradictory,
        "rows": rows,
    }


def _determinant(value: QMatrix) -> Fraction:
    if value.nrows != value.ncols:
        raise ScoreRefusal("determinant needs a square matrix")
    rows = [list(row) for row in value.data]
    result = Fraction(1)
    sign = 1
    for column in range(value.ncols):
        pivot = next((index for index in range(column, value.nrows) if rows[index][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            sign *= -1
        pivot_value = rows[column][column]
        result *= pivot_value
        for index in range(column + 1, value.nrows):
            if rows[index][column] == 0:
                continue
            factor = rows[index][column] / pivot_value
            for offset in range(column, value.ncols):
                rows[index][offset] -= factor * rows[column][offset]
    return result * sign


def _strongly_positive(value: QMatrix) -> bool:
    if value.nrows != value.ncols or value != qtranspose(value):
        return False
    indices = range(value.nrows)
    for size in range(1, value.nrows + 1):
        for selected in itertools.combinations(indices, size):
            principal = QMatrix.from_rows(
                tuple(tuple(value.data[row][column] for column in selected) for row in selected)
            )
            if _determinant(principal) < 0:
                return False
    return True


def measure_horizontal_process_package(
    package: object, *, static_response_available: bool
) -> dict[str, object]:
    """Validate the complete classical package and optional quantum extension."""

    fallback = "STATIC-RESPONSE-ONLY" if static_response_available else "SYNTAX-ONLY"
    if isinstance(package, QuantumPrimitiveLaw):
        measured_quantum = measure_quantum_primitive_law(package)
        payload = measured_quantum.to_data()
        if not measured_quantum.valid:
            payload["coordinate"] = (
                "HORIZONTAL-CLASSICAL"
                if measured_quantum.classical.valid
                else fallback
            )
        payload["active_root"] = package.root
        return payload
    if isinstance(package, ClassicalPrimitiveLaw):
        measured = measure_classical_primitive_law(package)
        payload = measured.to_data()
        if not measured.valid:
            payload["coordinate"] = fallback
        payload["active_root"] = package.root
        payload["component_evidence"] = {
            "active_frontier_factory": {
                "valid": measured.valid,
                "total_on_declared_domain": measured.valid,
            },
            "filling_positive_map_assignment": {"valid": measured.valid},
            "identity_assignments": {"valid": measured.valid},
            "typed_tensor_unit_interchange": {"valid": measured.valid},
            "vertical_horizontal_squares": {"valid": measured.valid},
            "record_effect_semantics": {"valid": measured.valid},
        }
        payload["equation_evidence"] = measured.residuals
        payload["quantum_evidence"] = {"present": False}
        return payload
    return {
        "coordinate": fallback,
        "classical_valid": False,
        "quantum_valid": False,
        "missing": ["typed ClassicalPrimitiveLaw"],
        "contradictions": [],
        "rejected_asserted_mapping": isinstance(package, Mapping),
    }


def synthetic_horizontal_process_package(
    *, quantum: bool = False
) -> ClassicalPrimitiveLaw | QuantumPrimitiveLaw:
    """Complete generic positive package used only by ``--selftest``."""

    return build_quantum_existence_law() if quantum else build_classical_existence_law()


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
    port_chain = semantic_port_chain(data, questions, trees, cospans)
    law_provenance = process.get("generated_law_provenance")
    if not isinstance(law_provenance, Mapping):
        raise ScoreRefusal("missing generated-law provenance")
    filling_factory = law_provenance.get("filling_factory")
    if not isinstance(filling_factory, Mapping):
        raise ScoreRefusal("missing finite filling factory")
    tree_factory_rows = filling_factory.get("tree_rows")
    if not isinstance(tree_factory_rows, list):
        raise ScoreRefusal("bad finite tree factory")
    identity_census = _active_identity_census(data)
    identity_by_level = identity_census["by_level"]
    b0_identity_controls = identity_by_level["B0"][
        "empty_process_semantic_witnesses"
    ]
    b0_identity_constructed = bool(identity_by_level["B0"]["present"])
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
    assignment_interface = process.get("filling_to_process_assignment")
    static_response_available = all_branch_partitions and all_numeric_controls
    semantic_package = process.get("horizontal_process_package")
    if semantic_package is None and isinstance(assignment_interface, Mapping) and (
        "components" in assignment_interface or "equations" in assignment_interface
    ):
        semantic_package = assignment_interface
    process_package_measurement = measure_horizontal_process_package(
        semantic_package,
        static_response_available=static_response_available,
    )
    assignment_present = bool(process_package_measurement["classical_valid"])
    component_evidence = process_package_measurement.get("component_evidence", {})
    total_frontier_present = bool(
        isinstance(component_evidence, Mapping)
        and isinstance(component_evidence.get("active_frontier_factory"), Mapping)
        and component_evidence["active_frontier_factory"].get("valid")
        and component_evidence["active_frontier_factory"].get("total_on_declared_domain")
    )
    tensor_present = bool(
        isinstance(component_evidence, Mapping)
        and isinstance(component_evidence.get("typed_tensor_unit_interchange"), Mapping)
        and component_evidence["typed_tensor_unit_interchange"].get("valid")
        and assignment_present
    )
    naturality_present = bool(
        isinstance(component_evidence, Mapping)
        and isinstance(component_evidence.get("vertical_horizontal_squares"), Mapping)
        and component_evidence["vertical_horizontal_squares"].get("valid")
        and assignment_present
    )
    construction_ceiling = {
        "B0_identity": (
            "CONSTRUCTED" if b0_identity_constructed else "REFUSED"
        ),
        "B0_identity_evidence": b0_identity_controls,
        "active_identity_domain": identity_census["active_domain"],
        "identity_assignments_by_active_level": identity_by_level,
        "out_of_domain_boundaries": identity_census["out_of_domain_boundaries"],
        "all_boundary_identity": (
            "CONSTRUCTED"
            if all(
                row["present"] for row in identity_by_level.values()
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
                row["present"] for row in identity_by_level.values()
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
    total_horizontal_process = bool(process_package_measurement["classical_valid"])
    process_coordinate = str(process_package_measurement["coordinate"])
    if process_coordinate not in PROCESS_COORDINATES:
        raise ScoreRefusal("process coordinate escaped the frozen vocabulary")
    result = {
        "full_cone_question_maps": {
            "semantic_branch_restrictions": branch_binding,
            "semantic_port_binding": port_chain,
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
        "semantic_process_package": process_package_measurement,
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
        continuation_results[identifier] = construct_typed_continuation_closure(
            row, process_operations
        )

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
    return tuple(
        row["permutation"]
        for row in _literal_replacement_generator_rows(data, target_id, depth)
    )


def _literal_replacement_generator_rows(
    data: Mapping[str, object], target_id: str, depth: int
) -> tuple[dict[str, object], ...]:
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
    generators: list[dict[str, object]] = []
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
        generators.append(
            {
                "replacement_role": identifier,
                "support_region": support,
                "permutation": child_swap_permutation(support.words[0], depth),
            }
        )
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
        "scope": REGIONAL_SUPPORT_SCOPE,
        "FAIL_interpretation": (
            "promotion failure/unconstructed capability; not observed physical nonlocality"
        ),
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


def _typed_finite_graph(
    row: object, active_root: object, *, assignment_field: str
) -> dict[str, object]:
    if not isinstance(row, Mapping):
        return {"valid": False}
    domain = _finite_unique_texts(row.get("domain"))
    codomain = _finite_unique_texts(row.get("codomain"))
    assignment = row.get(assignment_field)
    graph = assignment.get("graph") if isinstance(assignment, Mapping) else None
    pairs = [
        (pair[0], pair[1])
        for pair in graph
        if isinstance(pair, list)
        and len(pair) == 2
        and isinstance(pair[0], str)
        and isinstance(pair[1], str)
    ] if isinstance(graph, list) else []
    graph_map = dict(pairs)
    valid = bool(
        row.get("active_root") == active_root
        and isinstance(row.get("input_carrier"), str)
        and bool(row.get("input_carrier"))
        and isinstance(row.get("output_carrier"), str)
        and bool(row.get("output_carrier"))
        and domain is not None
        and codomain is not None
        and isinstance(graph, list)
        and len(pairs) == len(graph) == len(graph_map) == len(domain)
        and set(graph_map) == set(domain)
        and set(graph_map.values()).issubset(set(codomain))
    )
    return {
        "valid": valid,
        "input_carrier": row.get("input_carrier"),
        "output_carrier": row.get("output_carrier"),
        "domain": domain,
        "codomain": codomain,
        "graph": tuple(sorted(graph_map.items())),
    }


def measure_generated_influence_package(
    package: object, *, require_nonoverlap_contact: bool
) -> dict[str, object]:
    role = "generated_contact" if require_nonoverlap_contact else "causal_order"
    if isinstance(package, InfluencePrimitiveLaw):
        measured = measure_influence_primitive_law(package)
        payload = measured.to_data()
        if measured.role != role:
            payload["present"] = False
            payload["missing"] = ("requested influence role does not match typed law",)
        return payload
    return {
        "present": False,
        "role": role,
        "missing": ["typed InfluencePrimitiveLaw"],
        "rejected_asserted_mapping": isinstance(package, Mapping),
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
    contact_measurement = measure_generated_influence_package(
        section.get("generated_contact_package"),
        require_nonoverlap_contact=True,
    )
    causal_measurement = measure_generated_influence_package(
        section.get("generated_causal_package"),
        require_nonoverlap_contact=False,
    )
    generated_contact = bool(contact_measurement["present"])
    generated_causal_order = bool(causal_measurement["present"])
    contact = {
        "static_classification_controls": static_rows,
        "generated_joint_fillings": (
            "CONSTRUCTED"
            if generated_contact
            else "NOT-CONSTRUCTED"
        ),
        "nonoverlap_contact_response": (
            "CONSTRUCTED"
            if generated_contact
            else "NOT-CONSTRUCTED"
        ),
        "capability_detection": contact_measurement,
        "contact_coordinate": "DERIVED" if generated_contact else "PRICED",
    }
    causality = {
        "static_classification_controls": static_rows,
        "intervention_schedule": "GENERATED" if generated_causal_order else "NOT-FROZEN",
        "generated_delayed_reader_distribution": (
            "CONSTRUCTED" if generated_causal_order else "NOT-CONSTRUCTED"
        ),
        "reversible_replacement_cycles_are_causal": False,
        "capability_detection": causal_measurement,
        "causality_coordinate": "DERIVED" if generated_causal_order else "PRICED",
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
        interface = row.get("interface_token")
        if (
            not isinstance(nodes, list)
            or len(nodes) != 2
            or not isinstance(left_components, list)
            or not isinstance(right_components, list)
            or not isinstance(interface, str)
            or not interface
        ):
            raise ScoreRefusal("ill-typed declared candidate-regional incidence")
        left, right = map(str, nodes)
        if left not in regions or right not in regions:
            raise ScoreRefusal("declared incidence references an unknown node")
        left_set = {str(value) for value in left_components}
        right_set = {str(value) for value in right_components}
        if len(left_set) != len(left_components) or len(right_set) != len(
            right_components
        ):
            raise ScoreRefusal("declared incidence repeats a component reference")
        if not left_set.issubset(node_components[left]) or not right_set.issubset(
            node_components[right]
        ):
            raise ScoreRefusal("declared incidence disagrees with region antichains")
        represented_shared = node_components[left] & node_components[right]
        declared_shared = left_set & right_set
        if represented_shared != declared_shared:
            raise ScoreRefusal("declared shared-component incidence is incomplete")
        projected_left = {projection[component] for component in left_set}
        projected_right = {projection[component] for component in right_set}
        if projected_left & projected_right != {interface}:
            raise ScoreRefusal(
                "declared incidence contradicts its projected blind interface"
            )
        declared_crosschecks.append(
            {
                "nodes": tuple(sorted((left, right))),
                "interface": interface,
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
    blind_edge_keys: set[tuple[tuple[str, str], str]] = set()
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
        edge_key = (tuple(sorted((left, right))), interface)
        if edge_key in blind_edge_keys:
            raise ScoreRefusal("blind interface repeats an edge")
        blind_edge_keys.add(edge_key)
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

    declared_edge_keys = [
        (row["nodes"], row["interface"]) for row in declared_crosschecks
    ]
    if len(set(declared_edge_keys)) != len(declared_edge_keys) or set(
        declared_edge_keys
    ) != {
        (tuple(sorted((left, right))), interface)
        for left, right, interface in edge_rows
    }:
        raise ScoreRefusal(
            "declared incidences and frozen blind-interface edges disagree"
        )

    if not all(
        row["projected_membership_matches_edge"] for row in interface_crosschecks
    ):
        raise ScoreRefusal(
            "candidate-regional projection contradicts the frozen blind interface"
        )

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


def construct_typed_continuation_closure(
    catalogue: Mapping[str, object],
    operations: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    """Construct a finite, assigned, carrier-typed continuation semigroup.

    A catalogue is not a word.  This constructor first verifies the complete
    operation interface, then closes only assigned state transformations under
    type-correct composition.  Readers/effects are kept outside that semigroup
    and are attached afterwards to quantify recovery on every closed word.
    """

    operation_ids = catalogue.get("operation_ids")
    active_root = catalogue.get("active_root")
    declared_carriers = _finite_unique_texts(catalogue.get("declared_carriers"))
    if not isinstance(operation_ids, list) or any(
        not isinstance(identifier, str) for identifier in operation_ids
    ):
        raise ScoreRefusal("continuation catalogue has malformed operation references")
    if len(set(operation_ids)) != len(operation_ids):
        raise ScoreRefusal("continuation catalogue repeats an operation reference")

    typing_rows: dict[str, object] = {}
    state_maps: list[dict[str, object]] = []
    readers: list[dict[str, object]] = []
    missing: list[dict[str, object]] = []
    for identifier in operation_ids:
        row = operations.get(identifier)
        if not isinstance(row, Mapping):
            raise ScoreRefusal("continuation catalogue references a missing operation")
        required = (
            "carrier",
            "domain",
            "codomain",
            "semantic_role",
            "process_assignment",
            "assignment_root",
        )
        absent = [
            field
            for field in required
            if field not in row
            or row[field] is None
            or row[field] == ""
            or row[field] == []
            or row[field] == {}
        ]
        if not isinstance(active_root, str) or not active_root:
            absent.append("catalogue.active_root")
        if declared_carriers is None:
            absent.append("catalogue.declared_carriers")
        if row.get("assignment_root") != active_root:
            absent.append("connected_assignment_root")
        domain = row.get("domain")
        codomain = row.get("codomain")
        typed_domain = _finite_unique_texts(domain)
        typed_codomain = _finite_unique_texts(codomain)
        assignment = row.get("process_assignment")
        role = row.get("semantic_role")
        graph = assignment.get("graph") if isinstance(assignment, Mapping) else None
        if typed_domain is None:
            absent.append("finite_unique_domain")
        if typed_codomain is None:
            absent.append("finite_unique_codomain")
        if not isinstance(graph, list):
            absent.append("process_assignment.graph")
        if role not in {"state-transformation", "reader-effect"}:
            absent.append("recognized_semantic_role")
        if not isinstance(row.get("carrier"), str) or not row.get("carrier"):
            absent.append("finite_carrier_role")
        if absent:
            missing.append({"operation_role": identifier, "missing": sorted(set(absent))})
            typing_rows[identifier] = {
                "status": "UNTYPED-OR-UNASSIGNED",
                "missing": sorted(set(absent)),
            }
            continue

        assert typed_domain is not None and typed_codomain is not None
        assert isinstance(graph, list) and isinstance(role, str)
        pairs: list[tuple[str, str]] = []
        for pair in graph:
            if (
                not isinstance(pair, list)
                or len(pair) != 2
                or not isinstance(pair[0], str)
                or not isinstance(pair[1], str)
            ):
                raise ScoreRefusal("continuation assignment graph has a malformed pair")
            pairs.append((pair[0], pair[1]))
        graph_map = dict(pairs)
        domain_values = typed_domain
        codomain_values = typed_codomain
        if len(graph_map) != len(pairs) or set(graph_map) != set(domain_values):
            raise ScoreRefusal("continuation assignment is not functional and total")
        if not set(graph_map.values()).issubset(codomain_values):
            raise ScoreRefusal("continuation assignment escapes its codomain")
        semantic_map = {
            "word": (identifier,),
            "domain_carrier": str(row["carrier"]),
            "codomain_carrier": str(row["carrier"]),
            "domain": domain_values,
            "codomain": codomain_values,
            "graph": tuple(sorted(graph_map.items())),
        }
        # Distinct carrier names may be supplied explicitly without inventing
        # an identity or transport between them.
        input_carrier = row.get("input_carrier", row["carrier"])
        output_carrier = row.get("output_carrier", row["carrier"])
        if not isinstance(input_carrier, str) or not isinstance(output_carrier, str):
            raise ScoreRefusal("continuation carrier names are not typed")
        if (
            declared_carriers is None
            or input_carrier not in declared_carriers
            or output_carrier not in declared_carriers
        ):
            missing.append(
                {
                    "operation_role": identifier,
                    "missing": ["carrier-in-declared-continuation-scope"],
                }
            )
            typing_rows[identifier] = {
                "status": "UNTYPED-OR-UNASSIGNED",
                "missing": ["carrier-in-declared-continuation-scope"],
            }
            continue
        semantic_map["domain_carrier"] = input_carrier
        semantic_map["codomain_carrier"] = output_carrier
        typing_rows[identifier] = {
            "status": "TYPED-ASSIGNED",
            "semantic_role": role,
            "input_carrier": input_carrier,
            "output_carrier": output_carrier,
        }
        if role == "state-transformation":
            state_maps.append(semantic_map)
        else:
            readers.append(semantic_map)

    if missing or not state_maps or not readers:
        return {
            "status": "TYPED-CONTINUATION-SUBGRAMMAR-UNCONSTRUCTED",
            "active_root": active_root,
            "declared_carriers": declared_carriers,
            "operation_typing": typing_rows,
            "missing_or_disconnected": missing,
            "state_transformations": [row["word"][0] for row in state_maps],
            "reader_effects": [row["word"][0] for row in readers],
            "closed_typed_word_set": [],
            "recovery_scope": "UNCONSTRUCTED",
        }

    def map_key(row: Mapping[str, object]) -> tuple[object, ...]:
        return (
            row["domain_carrier"],
            row["codomain_carrier"],
            tuple(row["domain"]),
            tuple(row["codomain"]),
            tuple(row["graph"]),
        )

    closure = {map_key(row): dict(row) for row in state_maps}
    changed = True
    while changed:
        changed = False
        rows = list(closure.values())
        for earlier in rows:
            for later in rows:
                if (
                    earlier["codomain_carrier"] != later["domain_carrier"]
                    or tuple(earlier["codomain"]) != tuple(later["domain"])
                ):
                    continue
                earlier_graph = dict(earlier["graph"])
                later_graph = dict(later["graph"])
                composite_graph = tuple(
                    sorted(
                        (source, later_graph[earlier_graph[source]])
                        for source in earlier["domain"]
                    )
                )
                candidate = {
                    "word": tuple(earlier["word"]) + tuple(later["word"]),
                    "domain_carrier": earlier["domain_carrier"],
                    "codomain_carrier": later["codomain_carrier"],
                    "domain": tuple(earlier["domain"]),
                    "codomain": tuple(later["codomain"]),
                    "graph": composite_graph,
                }
                key = map_key(candidate)
                if key not in closure:
                    closure[key] = candidate
                    changed = True
                    if len(closure) > 10000:
                        raise ScoreRefusal("typed continuation closure exceeded finite bound")

    closed_rows = sorted(closure.values(), key=canonical_json)
    attached_readers = [
        reader
        for reader in readers
        if any(
            word["codomain_carrier"] == reader["domain_carrier"]
            and tuple(word["codomain"]) == tuple(reader["domain"])
            for word in closed_rows
        )
    ]
    if len(attached_readers) != len(readers):
        return {
            "status": "TYPED-CONTINUATION-SUBGRAMMAR-UNCONSTRUCTED",
            "active_root": active_root,
            "declared_carriers": declared_carriers,
            "operation_typing": typing_rows,
            "missing_or_disconnected": [
                {
                    "reader_roles": [row["word"][0] for row in readers if row not in attached_readers],
                    "missing": ["attached_typed_state_transformation"],
                }
            ],
            "state_transformations": [row["word"][0] for row in state_maps],
            "reader_effects": [row["word"][0] for row in readers],
            "closed_typed_word_set": closed_rows,
            "recovery_scope": "UNCONSTRUCTED",
        }

    recovery_rows: list[dict[str, object]] = []
    for word in closed_rows:
        word_graph = dict(word["graph"])
        compatible_readers = [
            reader
            for reader in attached_readers
            if word["codomain_carrier"] == reader["domain_carrier"]
            and tuple(word["codomain"]) == tuple(reader["domain"])
        ]
        word_recoverable = False
        reader_results: list[dict[str, object]] = []
        for reader in compatible_readers:
            reader_graph = dict(reader["graph"])
            outputs = tuple(
                reader_graph[word_graph[source]] for source in word["domain"]
            )
            distinguishes = len(set(outputs)) == len(tuple(word["domain"]))
            word_recoverable = word_recoverable or distinguishes
            reader_results.append(
                {
                    "reader_role": reader["word"][0],
                    "outputs": outputs,
                    "distinguishes_domain": distinguishes,
                }
            )
        recovery_rows.append(
            {
                "word": word["word"],
                "readers": reader_results,
                "recoverable": word_recoverable,
            }
        )
    return {
        "status": "TYPED-CONTINUATION-CLOSED",
        "active_root": active_root,
        "declared_carriers": declared_carriers,
        "operation_typing": typing_rows,
        "missing_or_disconnected": [],
        "state_transformations": [row["word"][0] for row in state_maps],
        "reader_effects": [row["word"][0] for row in readers],
        "closed_typed_word_set": closed_rows,
        "closed_under_typed_composition": True,
        "recovery_scope": {
            "word_count": len(closed_rows),
            "rows": recovery_rows,
            "all_words_recoverable": all(row["recoverable"] for row in recovery_rows),
        },
    }


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
    port_chain = semantic_port_chain(data, questions, trees, cospans_from_fixture(data))
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
        "end_to_end_port_binding": port_chain["transport_invariant_signature"],
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


def _active_identity_census(data: Mapping[str, object]) -> dict[str, object]:
    typed = data.get("typed_fillings")
    process = data.get("regional_question_process")
    if not isinstance(typed, Mapping) or not isinstance(process, Mapping):
        raise ScoreRefusal("identity census lacks typed process/fillings")
    boundaries = index_rows(typed.get("boundaries"))
    fillings = index_rows(typed.get("horizontal_fillings"))
    trees, _ = _tree_rows(data)
    provenance = process.get("generated_law_provenance")
    if not isinstance(provenance, Mapping):
        raise ScoreRefusal("identity census lacks generated provenance")
    boundary_factory = provenance.get("boundary_factory")
    filling_factory = provenance.get("filling_factory")
    if not isinstance(boundary_factory, Mapping) or not isinstance(
        filling_factory, Mapping
    ):
        raise ScoreRefusal("identity census lacks active factories")

    active_rows = boundary_factory.get("rows")
    if not isinstance(active_rows, list):
        raise ScoreRefusal("identity census lacks active boundary rows")
    active_by_level: dict[str, str] = {}
    for row in active_rows:
        if not isinstance(row, Mapping):
            raise ScoreRefusal("identity census has a malformed boundary row")
        depth = row.get("tree_depth")
        boundary_id = row.get("boundary_id")
        if not isinstance(depth, int) or not isinstance(boundary_id, str):
            raise ScoreRefusal("identity census boundary row is ill typed")
        level = f"B{depth}"
        if depth in range(4):
            if level in active_by_level or boundary_id not in boundaries:
                raise ScoreRefusal("identity census has duplicate/missing B0-B3 boundary")
            active_by_level[level] = boundary_id
    if set(active_by_level) != {"B0", "B1", "B2", "B3"}:
        raise ScoreRefusal("active identity domain must be exactly B0-B3")

    replacement_rows = filling_factory.get("replacement_rows")
    if not isinstance(replacement_rows, list):
        raise ScoreRefusal("identity census lacks replacement assignments")
    replacement_fillings = {
        str(row["root_filling_id"])
        for row in replacement_rows
        if isinstance(row, Mapping) and isinstance(row.get("root_filling_id"), str)
    }
    assignment_rows_raw = filling_factory.get("tree_rows")
    if not isinstance(assignment_rows_raw, list):
        raise ScoreRefusal("identity census lacks tree assignments")
    explicit_identity_rows = filling_factory.get("identity_rows", [])
    if not isinstance(explicit_identity_rows, list):
        raise ScoreRefusal("identity census identity_rows is not a list")
    assignment_rows: list[dict[str, object]] = []
    assignment_keys: set[tuple[str, str, str]] = set()
    for source, rows in (
        ("tree_rows", assignment_rows_raw),
        ("identity_rows", explicit_identity_rows),
    ):
        for row in rows:
            if not isinstance(row, Mapping):
                raise ScoreRefusal("identity census has a malformed assignment row")
            tree_id = row.get("tree_id")
            filling_id = row.get("filling_id")
            if (
                not isinstance(tree_id, str)
                or tree_id not in trees
                or not isinstance(filling_id, str)
                or filling_id not in fillings
            ):
                raise ScoreRefusal("identity assignment references a missing tree/filling")
            filling = fillings[filling_id]
            boundary_id = filling.get("incoming_boundary_id")
            declared_boundary = row.get("boundary_id", boundary_id)
            if declared_boundary != boundary_id:
                raise ScoreRefusal("identity assignment is attached to the wrong boundary")
            assignment_key = (source, tree_id, str(boundary_id))
            if assignment_key in assignment_keys:
                raise ScoreRefusal(
                    "identity census assignment is nonfunctional at a boundary"
                )
            assignment_keys.add(assignment_key)
            assignment_rows.append(
                {
                    "source": source,
                    "tree_role": tree_id,
                    "filling_role": filling_id,
                    "boundary_role": boundary_id,
                    "empty_process_semantic_witness": trees[tree_id].is_empty,
                }
            )

    def structurally_identity(boundary_id: str, row: Mapping[str, object]) -> bool:
        generators_raw = boundaries[boundary_id].get("generators")
        incoming = row.get("incoming_images")
        outgoing = row.get("outgoing_images")
        relations = row.get("apex_relations", [])
        if not isinstance(generators_raw, list) or not isinstance(
            incoming, list
        ) or not isinstance(outgoing, list) or not isinstance(relations, list):
            return False
        generators = tuple(str(value) for value in generators_raw)
        if (
            row.get("incoming_boundary_id") != boundary_id
            or row.get("outgoing_boundary_id") != boundary_id
            or relations
        ):
            return False
        in_pairs = [pair for pair in incoming if isinstance(pair, list) and len(pair) == 2]
        out_pairs = [pair for pair in outgoing if isinstance(pair, list) and len(pair) == 2]
        in_map = {str(pair[0]): str(pair[1]) for pair in in_pairs}
        out_map = {str(pair[0]): str(pair[1]) for pair in out_pairs}
        return (
            len(in_pairs) == len(in_map) == len(generators)
            and len(out_pairs) == len(out_map) == len(generators)
            and set(in_map) == set(out_map) == set(generators)
            and len(set(in_map.values())) == len(generators)
            and len(set(out_map.values())) == len(generators)
            and all(in_map[token] == out_map[token] for token in generators)
        )

    by_level: dict[str, object] = {}
    for level in ("B0", "B1", "B2", "B3"):
        boundary_id = active_by_level[level]
        attached = [
            dict(row)
            for row in assignment_rows
            if row["boundary_role"] == boundary_id
            and fillings[str(row["filling_role"])].get("outgoing_boundary_id")
            == boundary_id
        ]
        witnesses: list[dict[str, object]] = []
        for row in attached:
            filling_id = str(row["filling_role"])
            structural = structurally_identity(boundary_id, fillings[filling_id])
            replacement = filling_id in replacement_fillings
            valid = bool(row["empty_process_semantic_witness"]) and structural and not replacement
            row.update(
                {
                    "structural_identity": structural,
                    "replacement_or_swap_assignment": replacement,
                    "counts_as_identity": valid,
                }
            )
            if valid:
                witnesses.append(dict(row))

        exclusions: list[dict[str, object]] = []
        for filling_id, filling in sorted(fillings.items()):
            if filling.get("incoming_boundary_id") != boundary_id or filling.get(
                "outgoing_boundary_id"
            ) != boundary_id:
                continue
            structural = structurally_identity(boundary_id, filling)
            attached_rows = [row for row in attached if row["filling_role"] == filling_id]
            if any(row["counts_as_identity"] for row in attached_rows):
                continue
            reasons: list[str] = []
            if not attached_rows:
                reasons.append("raw-but-unassigned")
            if structural:
                reasons.append("identity-shaped-only")
            else:
                reasons.append("nonidentity-endomorphism")
            if filling_id in replacement_fillings:
                reasons.append("replacement-or-swap-assignment")
            if attached_rows and not any(
                row["empty_process_semantic_witness"] for row in attached_rows
            ):
                reasons.append("assigned-to-nonempty-process")
            exclusions.append(
                {
                    "filling_role": filling_id,
                    "reasons": reasons,
                    "assignment_rows": attached_rows,
                }
            )
        by_level[level] = {
            "boundary_role": boundary_id,
            "registered_assignment_rows": attached,
            "empty_process_semantic_witnesses": witnesses,
            "present": bool(witnesses),
            "witness_filling_roles": [row["filling_role"] for row in witnesses],
            "excluded_endomorphisms": exclusions,
        }

    active_boundary_ids = set(active_by_level.values())
    return {
        "active_domain": ("B0", "B1", "B2", "B3"),
        "by_level": by_level,
        "out_of_domain_boundaries": [
            {
                "boundary_role": boundary_id,
                "status": "OUT-OF-ACTIVE-IDENTITY-DOMAIN",
            }
            for boundary_id in sorted(set(boundaries) - active_boundary_ids)
        ],
    }


def _identity_assignments_by_boundary(data: Mapping[str, object]) -> dict[str, object]:
    return _active_identity_census(data)["by_level"]


def _interface_package(
    value: object, required_fields: Sequence[str]
) -> dict[str, object]:
    present = isinstance(value, Mapping) and all(
        field in value and _substantive(value[field]) for field in required_fields
    )
    return {
        "present": present,
        "required_fields": list(required_fields),
        "present_fields": sorted(value) if isinstance(value, Mapping) else [],
        "evidence_kind": "typed-frozen-interface" if present else "missing-interface",
    }


def _typed_destructive_reader_witnesses(
    records_result: Mapping[str, object],
) -> list[dict[str, object]]:
    continuation_rows = records_result.get("continuation_reachability")
    witnesses: list[dict[str, object]] = []
    if not isinstance(continuation_rows, Mapping):
        return witnesses
    for catalogue_role, closure in sorted(continuation_rows.items()):
        if not isinstance(closure, Mapping) or closure.get("status") != (
            "TYPED-CONTINUATION-CLOSED"
        ):
            continue
        recovery_scope = closure.get("recovery_scope")
        recovery_rows = (
            recovery_scope.get("rows") if isinstance(recovery_scope, Mapping) else None
        )
        readers_by_word = {
            tuple(row.get("word", ())): row.get("readers", [])
            for row in recovery_rows
            if isinstance(row, Mapping)
        } if isinstance(recovery_rows, list) else {}
        closed_words = closure.get("closed_typed_word_set")
        if not isinstance(closed_words, list):
            continue
        for word in closed_words:
            if not isinstance(word, Mapping):
                continue
            graph = word.get("graph")
            word_roles = tuple(word.get("word", ()))
            outputs = [
                pair[1]
                for pair in graph
                if isinstance(pair, (list, tuple)) and len(pair) == 2
            ] if isinstance(graph, (list, tuple)) else []
            attached_readers = readers_by_word.get(word_roles, [])
            if (
                outputs
                and len(set(outputs)) < len(outputs)
                and isinstance(attached_readers, list)
                and bool(attached_readers)
            ):
                witnesses.append(
                    {
                        "catalogue_role": catalogue_role,
                        "active_root": closure.get("active_root"),
                        "destructive_word": word_roles,
                        "attached_readers": attached_readers,
                    }
                )
    return witnesses


class ComputedCapabilityCensus(dict[str, object]):
    """Sealed output of the scientific census constructor, never caller evidence."""

    __slots__ = ("measurement_sha256",)

    def __init__(self, payload: Mapping[str, object]) -> None:
        super().__init__(payload)
        self.measurement_sha256 = canonical_sha256(dict(self))

    def intact(self) -> bool:
        return self.measurement_sha256 == canonical_sha256(dict(self))

    def __deepcopy__(self, memo: dict[int, object]) -> "ComputedCapabilityCensus":
        copied = ComputedCapabilityCensus(copy.deepcopy(dict(self), memo))
        memo[id(self)] = copied
        return copied


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
    records_result: Mapping[str, object],
    contact_result: Mapping[str, object],
    causality_result: Mapping[str, object],
    overlap_result: Mapping[str, object],
) -> ComputedCapabilityCensus:
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

    identity_census = _active_identity_census(data)
    identities = identity_census["by_level"]
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
    process_package = process_result.get("semantic_process_package")
    semantic_process_valid = bool(
        isinstance(process_package, Mapping)
        and process_package.get("classical_valid")
        and process_result.get("process_coordinate")
        in {"HORIZONTAL-CLASSICAL", "HORIZONTAL-QUANTUM"}
    )
    filling_process = {
        "present": semantic_process_valid,
        "evidence_kind": "recomputed-horizontal-process-package",
        "measurement": process_package,
    }
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
    contact_measurement = contact_result.get("capability_detection")
    causality_measurement = causality_result.get("capability_detection")
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
    destructive_reader_witnesses = _typed_destructive_reader_witnesses(
        records_result
    )
    same_law_reset_reader = {
        "present": bool(destructive_reader_witnesses),
        "witness_typed_continuations": destructive_reader_witnesses,
        "delayed_schedules_do_not_supply_this_capability": True,
        "evidence_kind": "computed-closed-typed-continuation-semantics",
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
    return ComputedCapabilityCensus({
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
        "active_identity_domain": identity_census["active_domain"],
        "out_of_domain_identity_boundaries": identity_census[
            "out_of_domain_boundaries"
        ],
        "all_boundary_identities": {
            "present": all_identities,
            "evidence_kind": "computed-horizontal-fillings",
        },
        "tensor_process_factory": tensor,
        "nontrivial_vertical_horizontal_naturality": naturality,
        "filling_to_process_assignment": filling_process,
        "horizontal_process": {
            "present": semantic_process_valid,
            "measurement": process_package,
            "process_coordinate": process_result.get("process_coordinate"),
        },
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
            "present": bool(
                isinstance(causality_measurement, Mapping)
                and causality_measurement.get("present")
                and causality_result["causality_coordinate"] == "DERIVED"
            ),
            "measurement": causality_measurement,
            "controls_do_not_promote": True,
        },
        "generated_contact": {
            "present": bool(
                isinstance(contact_measurement, Mapping)
                and contact_measurement.get("present")
                and contact_result["contact_coordinate"] == "DERIVED"
            ),
            "measurement": contact_measurement,
            "controls_do_not_promote": True,
        },
        "overlap_selector_kill": overlap_result,
    })


def classify_capability_census(census: object) -> tuple[str, list[str]]:
    if type(census) is not ComputedCapabilityCensus or not census.intact():
        raise ScoreRefusal(
            "primary classifier requires an intact internally computed capability census"
        )

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
    horizontal = census.get("horizontal_process")
    horizontal_measurement = (
        horizontal.get("measurement") if isinstance(horizontal, Mapping) else None
    )
    horizontal_valid = bool(
        isinstance(horizontal_measurement, Mapping)
        and horizontal_measurement.get("classical_valid")
        and horizontal_measurement.get("coordinate")
        in {"HORIZONTAL-CLASSICAL", "HORIZONTAL-QUANTUM"}
        and isinstance(horizontal, Mapping)
        and horizontal.get("process_coordinate")
        == horizontal_measurement.get("coordinate")
    )
    if not horizontal_valid:
        return "APR-BLOCKED-AT-TWO-ARROW-TYPING", [
            "no validated horizontal process package"
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
    causal = census.get("causal_order")
    causal_measurement = causal.get("measurement") if isinstance(causal, Mapping) else None
    causal_valid = bool(
        isinstance(causal, Mapping)
        and causal.get("present")
        and isinstance(causal_measurement, Mapping)
        and causal_measurement.get("present")
        and causal_measurement.get("role") == "causal_order"
        and not causal_measurement.get("missing")
    )
    if not causal_valid:
        return "APR-DYNAMIC-REGIONAL-REFERENT-CONSTRUCTED-BUT-CAUSAL-ORDER-PRICED", [
            "causal schedule and delayed response are not generated"
        ]
    contact = census.get("generated_contact")
    contact_measurement = contact.get("measurement") if isinstance(contact, Mapping) else None
    contact_valid = bool(
        isinstance(contact, Mapping)
        and contact.get("present")
        and isinstance(contact_measurement, Mapping)
        and contact_measurement.get("present")
        and contact_measurement.get("role") == "generated_contact"
        and not contact_measurement.get("missing")
    )
    if not contact_valid:
        return "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED", [
            "missing generated_contact"
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


ONTOLOGY_ROLES = (
    "STATIC-RESPONSE",
    "FIXED-ALGEBRA-CONDITIONING",
    "RECORD-WRITING-ON-FIXED-ALGEBRA",
    "REGION-REWRITING",
)


def measure_ontology_role(evidence: object) -> dict[str, object]:
    """Measure a construction role without consulting an ontology proposal."""

    if isinstance(evidence, OntologyPrimitiveLaw):
        return measure_ontology_primitive_law(evidence).to_data()
    if not isinstance(evidence, Mapping):
        raise ScoreRefusal("ontology-role measurement lacks a static response baseline")
    if evidence.get("static_response") is not True:
        raise ScoreRefusal("ontology-role measurement lacks a static response baseline")
    return {
        "role": "STATIC-RESPONSE",
        "static_response": True,
        "process_valid": False,
        "conditioning": {"valid": False, "rejected_asserted_mapping": True},
        "record": {"valid": False, "rejected_asserted_mapping": True},
        "region_rewrite": {"valid": False, "rejected_asserted_mapping": True},
        "candidate_consulted": False,
    }


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
        records_result=records,
        contact_result=contact,
        causality_result=causality,
        overlap_result=overlap,
    )

    ontology_evidence: dict[str, object] = {
        "static_response": bool(process["all_input_normalization"]["symbolic"]),
        "process_measurement": process["semantic_process_package"],
    }
    horizontal_package = data.get("regional_question_process", {}).get(
        "horizontal_process_package"
    ) if isinstance(data.get("regional_question_process"), Mapping) else None
    if isinstance(horizontal_package, Mapping) and isinstance(
        horizontal_package.get("ontology_evidence"), Mapping
    ):
        ontology_evidence.update(horizontal_package["ontology_evidence"])
    ontology_role = measure_ontology_role(ontology_evidence)
    ontology_role.update(
        {
            "valuation_status": "process-state representation; ontic/epistemic/shadow status unselected",
            "p_status": "preparation label, not law data or coupling",
            "actualization": "POSTULATE-UNTOUCHED",
        }
    )
    ontology_candidate = {
        "candidate": "POSTULATED-CANDIDATE-RELATIONAL-WEB",
        "measurement_status": "PROPOSAL-NOT-MEASURED-ROLE",
        "classifier_input": False,
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
        REGIONAL_SUPPORT_SCOPE,
        PREFIX_SYNTAX_SCOPE,
        "locality=FAIL is promotion failure/unconstructed capability, not observed physical nonlocality",
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
        "ontology_candidate": ontology_candidate,
        "law_selection": law_selection,
        "scope_walls": scope_walls,
        "mutants": "NOT-RUN" if not include_mutants else {},
        "strict_primary": "UNCLASSIFIED",
        "qualifiers": [],
        "blinding_status": BLINDING_STATUS,
        "exposure_debt": EXPOSURE_DEBT,
        "v4_source_frozen_before_v4_run": True,
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
    validate_v4_exposure_fields(receipt)
    if "payload_sha256" in receipt:
        raise ScoreRefusal("payload hash already attached")
    receipt["payload_sha256"] = canonical_sha256(receipt)


def validate_v4_exposure_fields(value: Mapping[str, object]) -> None:
    expected = {
        "blinding_status": BLINDING_STATUS,
        "exposure_debt": EXPOSURE_DEBT,
        "v4_source_frozen_before_v4_run": True,
    }
    if any(value.get(key) != expected_value for key, expected_value in expected.items()):
        raise ScoreRefusal("v4 artifact exposure metadata is missing or changed")


def transcript_from_receipt(receipt: Mapping[str, object]) -> dict[str, object]:
    validate_v4_exposure_fields(receipt)
    transcript = {
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
        "ontology_candidate": receipt["ontology_candidate"]["candidate"],
        "law_selection": receipt["law_selection"]["status"],
        "scope_walls": receipt["scope_walls"],
        "blinding_status": receipt["blinding_status"],
        "exposure_debt": receipt["exposure_debt"],
        "v4_source_frozen_before_v4_run": receipt[
            "v4_source_frozen_before_v4_run"
        ],
        "receipt_payload_sha256": receipt["payload_sha256"],
    }
    validate_v4_exposure_fields(transcript)
    return transcript


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


def _substitute_represented_candidate_overlap(
    data: MutableMapping[str, object],
    options: MutationOptions,
    *,
    expected_member_role: str | None = None,
    expected_source_component: str | None = None,
    expected_target_component: str | None = None,
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
        if expected_member_role is not None and member.get("id") != expected_member_role:
            continue
        incidences = member.get("incidences")
        regions = member.get("regions")
        occurrences = member.get("component_occurrences")
        projection_rows = member.get("blind_projection")
        if (
            not isinstance(incidences, list)
            or not isinstance(regions, list)
            or not isinstance(occurrences, list)
            or not isinstance(projection_rows, list)
        ):
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
        projection: dict[str, str] = {}
        for row in projection_rows:
            if not isinstance(row, Mapping):
                raise ScoreRefusal("M16 has a malformed frozen blind projection")
            source = row.get("component_token")
            target = row.get("blind_component_token")
            if not isinstance(source, str) or not isinstance(target, str) or source in projection:
                raise ScoreRefusal("M16 has a nonfunctional frozen blind projection")
            projection[source] = target
        pre_projection = _candidate_regional_projection(member)
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
            source_component = shared[0]
            if (
                expected_source_component is not None
                and source_component != expected_source_component
            ):
                continue
            blind_component = projection.get(source_component)
            alternatives = sorted(
                component
                for component, projected in projection.items()
                if projected == blind_component and component != source_component
            )
            if expected_target_component is not None:
                alternatives = [
                    component
                    for component in alternatives
                    if component == expected_target_component
                ]
            if not alternatives:
                continue
            target_component = alternatives[0]
            source_occurrence = occurrence_index.get(source_component)
            target_occurrence = occurrence_index.get(target_component)
            right_node = region_index.get(str(nodes[1]))
            if (
                not isinstance(source_occurrence, Mapping)
                or not isinstance(target_occurrence, Mapping)
                or not isinstance(right_node, MutableMapping)
            ):
                continue
            source_words = source_occurrence.get("antichain")
            target_words = target_occurrence.get("antichain")
            node_words = right_node.get("antichain")
            if (
                not isinstance(source_words, list)
                or not isinstance(target_words, list)
                or len(source_words) != 1
                or len(target_words) != 1
                or not isinstance(node_words, list)
            ):
                continue
            old_word = str(source_words[0])
            new_word = str(target_words[0])
            if old_word not in set(map(str, node_words)) or new_word in set(
                map(str, node_words)
            ):
                continue
            pre_member = copy.deepcopy(member)
            right_node["antichain"] = sorted(
                new_word if str(word) == old_word else str(word) for word in node_words
            )
            incidence["right_component_tokens"] = [
                target_component if str(value) == source_component else str(value)
                for value in right_components
            ]
            post_projection = _candidate_regional_projection(member)
            before_overlap = pre_projection[
                "represented_candidate_regional_relation"
            ]["overlap_pair_count"]
            after_overlap = post_projection[
                "represented_candidate_regional_relation"
            ]["overlap_pair_count"]
            if before_overlap != 2 or after_overlap != 1:
                raise ScoreRefusal("M16 substitution did not move represented overlap 2 -> 1")
            if (
                pre_projection["canonical_blind_sha256"]
                != post_projection["canonical_blind_sha256"]
            ):
                raise ScoreRefusal("M16 substitution changed the frozen blind colored graph")
            if not post_projection["blind_interface_consistent"]:
                raise ScoreRefusal("M16 substitution broke projection/interface consistency")
            if canonical_sha256(pre_member["component_occurrences"]) != canonical_sha256(
                member["component_occurrences"]
            ) or canonical_sha256(pre_member["resource_declaration"]) != canonical_sha256(
                member["resource_declaration"]
            ) or canonical_sha256(pre_member["blind_projection"]) != canonical_sha256(
                member["blind_projection"]
            ):
                raise ScoreRefusal("M16 altered a frozen catalogue, resource, or projection")
            options.details["M16"] = {
                "member_role": str(member.get("id", "anonymous-member")),
                "node_role": str(nodes[1]),
                "source_component_role": source_component,
                "target_component_role": target_component,
                "old_region_word": old_word,
                "new_region_word": new_word,
                "incidence_reference_update": {
                    "old": source_component,
                    "new": target_component,
                },
                "overlap_count_before": before_overlap,
                "overlap_count_after": after_overlap,
                "projection_consistent_before": pre_projection[
                    "blind_interface_consistent"
                ],
                "projection_consistent_after": post_projection[
                    "blind_interface_consistent"
                ],
                "blind_sha256_before": pre_projection["canonical_blind_sha256"],
                "blind_sha256_after": post_projection["canonical_blind_sha256"],
                "pre_payload": pre_member,
                "post_payload": copy.deepcopy(member),
                "pre_sha256": canonical_sha256(pre_member),
                "post_sha256": canonical_sha256(member),
            }
            return
    raise ScoreRefusal("M16 found no exact blind-equivalent c-to-d substitution")


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
        options.modes.update(
            {
                "raw_syntax_copy",
                "identifier_hash_copy",
                "finite_depth_whitelist",
            }
        )
    elif mutant_id == "M16":
        _substitute_represented_candidate_overlap(
            data,
            options,
            expected_member_role="rf_000",
            expected_source_component="edge_0_c",
            expected_target_component="edge_0_d",
        )
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


def _serialized_permutation_family(
    *,
    family_kind: str,
    target: PrefixRegion,
    depth: int,
    generators: Sequence[Mapping[str, object]],
) -> dict[str, object]:
    leaves = leaves_at_depth(depth)
    rows: list[dict[str, object]] = []
    permutations: list[tuple[int, ...]] = []
    for index, row in enumerate(generators):
        permutation = row.get("permutation")
        if not isinstance(permutation, tuple) or sorted(permutation) != list(
            range(len(leaves))
        ):
            raise ScoreRefusal("serialized replacement family has a bad permutation")
        permutations.append(permutation)
        rows.append(
            {
                "generator_index": index,
                "source_role": row.get("replacement_role", f"finite-generator-{index}"),
                "support_region": row.get("support_region"),
                "permutation": permutation,
            }
        )
    return {
        "family_kind": family_kind,
        "carrier": {"depth": depth, "leaf_basis": leaves},
        "target_region": target,
        "generators": rows,
        "generated_family": permutation_closure(permutations) if permutations else (),
    }


def _permutation_family_measurement(
    payload: Mapping[str, object],
) -> dict[str, object]:
    carrier = payload.get("carrier")
    target = payload.get("target_region")
    generator_rows = payload.get("generators")
    if (
        not isinstance(carrier, Mapping)
        or not isinstance(carrier.get("depth"), int)
        or not isinstance(target, PrefixRegion)
        or not isinstance(generator_rows, list)
    ):
        raise ScoreRefusal("cannot measure malformed serialized permutation family")
    permutations = [row["permutation"] for row in generator_rows if isinstance(row, Mapping)]
    reading = _orbit_reading(target, int(carrier["depth"]), permutations)
    return {
        "exterior_orbits": reading["exterior_orbits"],
        "exterior_orbit_count": reading["exterior_orbit_count"],
        "fixed_effect_dimension": reading["fixed_effect_dimension"],
        "fixed_effect_constraints": reading["fixed_effect_constraints"],
        "semigroup_size": reading["semigroup_size"],
    }


def l2_generator_deletion_control(data: Mapping[str, object]) -> dict[str, object]:
    regions = regions_from_fixture(data)
    process = data.get("regional_question_process")
    if not isinstance(process, Mapping) or not isinstance(
        process.get("changed_object_rows"), list
    ):
        raise ScoreRefusal("L2 lacks replacement-control rows")
    candidates: list[tuple[int, str, PrefixRegion, tuple[dict[str, object], ...]]] = []
    for row in process["changed_object_rows"]:
        if not isinstance(row, Mapping) or not isinstance(
            row.get("target_region_id"), str
        ):
            continue
        target_id = str(row["target_region_id"])
        if target_id not in regions:
            continue
        target = regions[target_id]
        depth = max(2, max((len(word) for word in target.words), default=0) + 1)
        generators = _literal_replacement_generator_rows(data, target_id, depth)
        if len(generators) >= 2:
            candidates.append((depth, target_id, target, generators))
    if not candidates:
        raise ScoreRefusal("L2 has no finite child-swap family with two generators")
    depth, target_id, target, generators = max(candidates, key=lambda row: (row[0], row[1]))
    pre_payload = _serialized_permutation_family(
        family_kind="finite child-swap family from replacement-control rows",
        target=target,
        depth=depth,
        generators=generators,
    )
    deleted = generators[-1]
    post_payload = _serialized_permutation_family(
        family_kind="finite child-swap family with one serialized generator deleted",
        target=target,
        depth=depth,
        generators=generators[:-1],
    )
    before = _permutation_family_measurement(pre_payload)
    after = _permutation_family_measurement(post_payload)
    if (
        before["exterior_orbit_count"] == after["exterior_orbit_count"]
        or before["fixed_effect_dimension"] == after["fixed_effect_dimension"]
    ):
        raise ScoreRefusal("L2 generator deletion did not move orbit/fixed space")
    return {
        "scope": "finite analytical replacement control only",
        "positive_locality_baseline": False,
        "target_region_role": target_id,
        "deleted_generator": deleted,
        "pre_payload": pre_payload,
        "post_payload": post_payload,
        "pre_sha256": canonical_sha256(pre_payload),
        "post_sha256": canonical_sha256(post_payload),
        "measurement_before": before,
        "measurement_after": after,
    }


def l4_transitivity_deletion_control(
    target: PrefixRegion = PrefixRegion.cylinder("00"), depth: int = 3
) -> dict[str, object]:
    intrinsic = _intrinsic_exterior_generators(target, depth)
    if len(intrinsic) < 2:
        raise ScoreRefusal("L4 finite exterior family has no removable bridge")
    generator_rows = tuple(
        {
            "replacement_role": f"finite-exterior-adjacent-swap-{index}",
            "support_region": target.complement(),
            "permutation": permutation,
        }
        for index, permutation in enumerate(intrinsic)
    )
    bridge_index = len(generator_rows) // 2
    post_rows = generator_rows[:bridge_index] + generator_rows[bridge_index + 1 :]
    pre_payload = _serialized_permutation_family(
        family_kind="finite transitive exterior permutation/mixing family",
        target=target,
        depth=depth,
        generators=generator_rows,
    )
    post_payload = _serialized_permutation_family(
        family_kind="serialized multiple-orbit exterior subfamily",
        target=target,
        depth=depth,
        generators=post_rows,
    )
    before = _permutation_family_measurement(pre_payload)
    after = _permutation_family_measurement(post_payload)
    if before["exterior_orbit_count"] != 1 or after["exterior_orbit_count"] < 2:
        raise ScoreRefusal("L4 did not move transitivity to multiple exterior orbits")
    if before["fixed_effect_dimension"] == after["fixed_effect_dimension"]:
        raise ScoreRefusal("L4 multiple-orbit subfamily did not move fixed space")
    return {
        "scope": "finite analytical transitivity control only",
        "positive_locality_baseline": False,
        "deleted_generator": generator_rows[bridge_index],
        "pre_payload": pre_payload,
        "post_payload": post_payload,
        "pre_sha256": canonical_sha256(pre_payload),
        "post_sha256": canonical_sha256(post_payload),
        "measurement_before": before,
        "measurement_after": after,
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


def raw_syntax_copy(expression: Mapping[str, object]) -> str:
    """Wrong M15 implementation: copy an unreduced syntax tree verbatim."""

    operation = expression.get("op")
    if operation == "cyl":
        word = expression.get("word")
        if not isinstance(word, str) or set(word) - {"0", "1"}:
            raise ScoreRefusal("raw-syntax oracle received a malformed cylinder")
    elif operation == "join":
        arguments = expression.get("args")
        if not isinstance(arguments, list) or len(arguments) != 2:
            raise ScoreRefusal("raw-syntax oracle received a malformed join")
        for argument in arguments:
            if not isinstance(argument, Mapping):
                raise ScoreRefusal("raw-syntax oracle join argument is not syntax")
            raw_syntax_copy(argument)
    else:
        raise ScoreRefusal("raw-syntax oracle received an unknown constructor")
    return canonical_json(expression)


def identifier_hash_copy(identifier: str, region: PrefixRegion) -> str:
    """Wrong M15 implementation: ignore the region and copy a neutral ID hash."""

    if not isinstance(identifier, str) or not identifier:
        raise ScoreRefusal("identifier-hash oracle needs a presentation identifier")
    # Mention ``region`` in the executable signature while deliberately not
    # consuming it; the family test below detects this disconnected argument.
    if not isinstance(region, PrefixRegion):
        raise ScoreRefusal("identifier-hash oracle needs a canonical region argument")
    return hashlib.sha256(identifier.encode("utf-8")).hexdigest()


def finite_whitelist_copy(
    region: PrefixRegion, registered: Sequence[PrefixRegion]
) -> str | None:
    """Wrong M15/P5 implementation: answer only a frozen finite member set."""

    allowed = set(registered)
    return canonical_json(region) if region in allowed else None


def _flip_syntax_expression(expression: Mapping[str, object]) -> dict[str, object]:
    if expression.get("op") == "cyl":
        return {"op": "cyl", "word": _flip_binary_word(str(expression["word"]))}
    arguments = expression.get("args")
    if expression.get("op") != "join" or not isinstance(arguments, list):
        raise ScoreRefusal("cannot Boolean-relabel malformed raw syntax")
    return {
        "op": "join",
        "args": [
            _flip_syntax_expression(argument)
            for argument in arguments
            if isinstance(argument, Mapping)
        ],
    }


def oracle_family_controls(regions: Mapping[str, PrefixRegion]) -> dict[str, object]:
    if not regions:
        raise ScoreRefusal("oracle control needs registered regions")
    registered = tuple(sorted(set(regions.values()), key=canonical_json))
    fresh = PrefixRegion.cylinder("000")
    if fresh in set(registered):
        raise ScoreRefusal("M15/P5 requires fresh [000] outside the whitelist")

    unreduced = {
        "op": "join",
        "args": [
            {"op": "cyl", "word": "000"},
            {"op": "cyl", "word": "001"},
        ],
    }
    reduced = {"op": "cyl", "word": "00"}
    canonical_region = PrefixRegion.from_words(("000", "001"))
    if canonical_region != PrefixRegion.cylinder("00"):
        raise ScoreRefusal("oracle control failed canonical sibling reduction")
    raw_unreduced = raw_syntax_copy(unreduced)
    raw_reduced = raw_syntax_copy(reduced)
    relabeled_unreduced = _flip_syntax_expression(unreduced)
    relabeled_reduced = _flip_syntax_expression(reduced)

    sample_name, sample = next(
        (
            (name, region)
            for name, region in sorted(regions.items())
            if not region.is_zero()
        ),
        next(iter(sorted(regions.items()))),
    )
    clone_name = "fresh-clone-of-" + sample_name
    sample_hash = identifier_hash_copy(sample_name, sample)
    clone_hash = identifier_hash_copy(clone_name, sample)
    fresh_identifier = "fresh-region-000"
    fresh_identifier_output = identifier_hash_copy(fresh_identifier, fresh)
    relabeled_sample = PrefixRegion.from_words(
        _flip_binary_word(word) for word in sample.words
    )
    refined_sample = PrefixRegion.from_words(
        child
        for word in sample.words
        for child in (word + "0", word + "1")
    )

    whitelist_payload = {
        "implementation": "finite canonical membership table",
        "registered_regions": registered,
    }
    whitelist_hash = canonical_sha256(whitelist_payload)
    whitelist_registered = [
        finite_whitelist_copy(region, registered) for region in registered
    ]
    whitelist_relabel = finite_whitelist_copy(relabeled_sample, registered)
    whitelist_refinement = finite_whitelist_copy(refined_sample, registered)

    return {
        "raw_syntax_copy": {
            "implementation": {
                "key": "unreduced expression tree",
                "constructor": "raw_syntax_copy",
            },
            "fresh_region_test": {
                "region": fresh,
                "accepted": raw_syntax_copy({"op": "cyl", "word": "000"})
                is not None,
            },
            "canonical_reduction_test": {
                "unreduced_expression": unreduced,
                "reduced_expression": reduced,
                "canonical_region": canonical_region,
                "unreduced_output": raw_unreduced,
                "reduced_output": raw_reduced,
                "agrees_on_same_canonical_region": raw_unreduced == raw_reduced,
            },
            "Boolean_relabel_test": {
                "unreduced_output": raw_syntax_copy(relabeled_unreduced),
                "reduced_output": raw_syntax_copy(relabeled_reduced),
                "agrees_after_relabel": raw_syntax_copy(relabeled_unreduced)
                == raw_syntax_copy(relabeled_reduced),
            },
            "refinement_test": {
                "parent": reduced,
                "children_join": unreduced,
                "invariant": raw_reduced == raw_unreduced,
            },
        },
        "identifier_hash_copy": {
            "implementation": {
                "key": "neutral presentation identifier",
                "constructor": "identifier_hash_copy",
            },
            "fresh_region_test": {
                "region": fresh,
                "identifier": fresh_identifier,
                "output": fresh_identifier_output,
                "returns_canonical_region": fresh_identifier_output
                == canonical_json(fresh),
            },
            "fresh_id_clone_test": {
                "canonical_region": sample,
                "source_identifier": sample_name,
                "clone_identifier": clone_name,
                "source_hash": sample_hash,
                "clone_hash": clone_hash,
                "agrees_on_same_canonical_region": sample_hash == clone_hash,
            },
            "Boolean_relabel_test": {
                "relabeled_region": relabeled_sample,
                "output": identifier_hash_copy(sample_name, relabeled_sample),
                "returns_relabeled_region": identifier_hash_copy(
                    sample_name, relabeled_sample
                )
                == canonical_json(relabeled_sample),
            },
            "refinement_test": {
                "refined_region_equals_source": refined_sample == sample,
                "identifier_output_equal": identifier_hash_copy(sample_name, refined_sample)
                == sample_hash,
                "returns_canonical_region": sample_hash == canonical_json(sample),
            },
        },
        "finite_depth_whitelist": {
            "payload": whitelist_payload,
            "payload_sha256": whitelist_hash,
            "fresh_region_test": {
                "region": fresh,
                "accepted": finite_whitelist_copy(fresh, registered) is not None,
            },
            "accepts_registered": all(value is not None for value in whitelist_registered),
            "Boolean_relabel_test": {
                "source": sample,
                "relabeled": relabeled_sample,
                "accepted": whitelist_relabel is not None,
            },
            "refinement_test": {
                "source": sample,
                "refined": refined_sample,
                "same_canonical_region": refined_sample == sample,
                "accepted": whitelist_refinement is not None,
            },
        },
    }


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
        fresh_test = whitelist["fresh_region_test"]
        return {
            "shared_evidence_with": "M15/finite_depth_whitelist",
            "shared_payload_sha256": whitelist["payload_sha256"],
            "fresh_region": fresh_test["region"],
            "symbolic_question_defined": Restriction(fresh_test["region"]),
            "whitelist_accepts": fresh_test["accepted"],
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
    if mutant_id == "L2":
        return l2_generator_deletion_control(data)
    if mutant_id == "L4":
        return l4_transitivity_deletion_control()
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
    "L2",
    "L3",
    "L4",
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
    elif mutant_id in {"L2", "L4"} and isinstance(evidence, Mapping):
        descriptor = {
            "target_root": "finite-replacement-analytical-control",
            "target_object": evidence.get("scope"),
            "constructor_schema": (
                "serialize complete finite permutation family, delete one explicit "
                "generator, close both families, and recompute orbit/fixed spaces"
            ),
            "pre_payload": evidence.get("pre_payload"),
            "post_payload": evidence.get("post_payload"),
            "pre_payload_sha256": evidence.get("pre_sha256"),
            "post_payload_sha256": evidence.get("post_sha256"),
            "exact_changes": [{"deleted_generator": evidence.get("deleted_generator")}],
            "reference_updates": [],
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
        post_payload = {"constructed_control_payload": constructor_output}
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
        "construct serialized finite family, delete one generator, and recompute"
        if mutant_id in {"L2", "L4"}
        else (
            "mutate serialized semantic object and recompute"
            if differences
            else "construct registered analytical/scope control and recompute"
        )
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


# ---------------------------------------------------------------------------
# V4 fixture-free exact semantic laws


V4_INTERNAL_ROOT = "v4:internal-reachability-control"


def _q_kron(left: QMatrix, right: QMatrix) -> QMatrix:
    return QMatrix.from_rows(
        (
            (
                left.data[left_row][left_col]
                * right.data[right_row][right_col]
                for left_col in range(left.ncols)
                for right_col in range(right.ncols)
            )
            for left_row in range(left.nrows)
            for right_row in range(right.nrows)
        ),
        ncols=left.ncols * right.ncols,
    )


def _q_nonzero_count(value: QMatrix) -> int:
    return sum(item != 0 for row in value.data for item in row)


def _q_residual(left: QMatrix, right: QMatrix) -> dict[str, object]:
    if left.shape != right.shape:
        return {
            "shape_match": False,
            "left_shape": left.shape,
            "right_shape": right.shape,
            "nonzero_count": None,
        }
    difference = qsubtract(left, right)
    return {
        "shape_match": True,
        "left_shape": left.shape,
        "right_shape": right.shape,
        "difference": difference,
        "nonzero_count": _q_nonzero_count(difference),
    }


def _q_column_residual(value: QMatrix, target: Fraction = Fraction(1)) -> tuple[Fraction, ...]:
    return tuple(
        sum((value.data[row][column] for row in range(value.nrows)), Fraction(0))
        - target
        for column in range(value.ncols)
    )


def _q_is_permutation(value: QMatrix) -> tuple[bool, QMatrix | None]:
    if value.nrows != value.ncols:
        return False, None
    permitted = {Fraction(0), Fraction(1)}
    entrywise = all(item in permitted for row in value.data for item in row)
    rows = all(sum(row, Fraction(0)) == 1 for row in value.data)
    columns = all(
        sum((value.data[row][column] for row in range(value.nrows)), Fraction(0))
        == 1
        for column in range(value.ncols)
    )
    inverse = qtranspose(value)
    inverse_valid = (
        qmultiply(value, inverse) == QMatrix.identity(value.nrows)
        and qmultiply(inverse, value) == QMatrix.identity(value.nrows)
    )
    return entrywise and rows and columns and inverse_valid, inverse


def _q_permutation_from_images(images: Sequence[int]) -> QMatrix:
    size = len(images)
    if sorted(images) != list(range(size)):
        raise ScoreRefusal("permutation images are not bijective")
    return QMatrix.from_rows(
        (
            (Fraction(1) if row == images[column] else Fraction(0) for column in range(size))
            for row in range(size)
        ),
        ncols=size,
    )


def _tensor_frontier(left: Sequence[str], right: Sequence[str]) -> tuple[str, ...]:
    return tuple(f"({first},{second})" for first in left for second in right)


def _symmetry_permutation(left_size: int, right_size: int) -> QMatrix:
    images = [
        right * left_size + left
        for left in range(left_size)
        for right in range(right_size)
    ]
    return _q_permutation_from_images(images)


def _associator_permutation(first: int, second: int, third: int) -> QMatrix:
    images = [
        left * (second * third) + middle * third + right
        for left in range(first)
        for middle in range(second)
        for right in range(third)
    ]
    return _q_permutation_from_images(images)


@dataclass(frozen=True, slots=True)
class TypedBoundary:
    root: str
    identifier: str
    frontier: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {"root": self.root, "id": self.identifier, "frontier": self.frontier}


@dataclass(frozen=True, slots=True)
class TypedArrow:
    root: str
    identifier: str
    generator_id: str
    source_id: str
    target_id: str
    matrix: QMatrix
    process_word: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "generator_id": self.generator_id,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "matrix": self.matrix,
            "process_word": self.process_word,
        }


@dataclass(frozen=True, slots=True)
class TypedInstrument:
    root: str
    identifier: str
    source_id: str
    target_id: str
    flags: tuple[str, ...]
    branch_matrices: tuple[QMatrix, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "flags": self.flags,
            "branch_matrices": self.branch_matrices,
        }


@dataclass(frozen=True, slots=True)
class TypedFactorization:
    root: str
    identifier: str
    whole_arrow_id: str
    arrow_occurrence_ids: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "whole_arrow_id": self.whole_arrow_id,
            "arrow_occurrence_ids": self.arrow_occurrence_ids,
        }


@dataclass(frozen=True, slots=True)
class TypedVerticalMap:
    root: str
    identifier: str
    source_id: str
    target_id: str
    matrix: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "matrix": self.matrix,
        }


@dataclass(frozen=True, slots=True)
class TensorBoundaryClaim:
    left_boundary_id: str
    right_boundary_id: str
    product_boundary_id: str

    def to_data(self) -> dict[str, object]:
        return {
            "left_boundary_id": self.left_boundary_id,
            "right_boundary_id": self.right_boundary_id,
            "product_boundary_id": self.product_boundary_id,
        }


@dataclass(frozen=True, slots=True)
class TensorArrowClaim:
    left_arrow_id: str
    right_arrow_id: str
    product_arrow_id: str

    def to_data(self) -> dict[str, object]:
        return {
            "left_arrow_id": self.left_arrow_id,
            "right_arrow_id": self.right_arrow_id,
            "product_arrow_id": self.product_arrow_id,
        }


@dataclass(frozen=True, slots=True)
class TensorPrimitive:
    root: str
    identifier: str
    unit_boundary_id: str
    boundary_claims: tuple[TensorBoundaryClaim, ...]
    arrow_claims: tuple[TensorArrowClaim, ...]
    associator_boundary_ids: tuple[str, str, str]
    associator_matrix: QMatrix
    symmetry_boundary_ids: tuple[str, str]
    symmetry_matrix: QMatrix
    associativity_arrow_ids: tuple[str, str, str]
    interchange_arrow_ids: tuple[str, str, str, str]
    interchange_tensor_arrow_ids: tuple[str, str]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "unit_boundary_id": self.unit_boundary_id,
            "boundary_claims": self.boundary_claims,
            "arrow_claims": self.arrow_claims,
            "associator_boundary_ids": self.associator_boundary_ids,
            "associator_matrix": self.associator_matrix,
            "symmetry_boundary_ids": self.symmetry_boundary_ids,
            "symmetry_matrix": self.symmetry_matrix,
            "associativity_arrow_ids": self.associativity_arrow_ids,
            "interchange_arrow_ids": self.interchange_arrow_ids,
            "interchange_tensor_arrow_ids": self.interchange_tensor_arrow_ids,
            "ordering": "left-major-lexicographic",
        }


@dataclass(frozen=True, slots=True)
class NaturalityPrimitive:
    root: str
    identifier: str
    arrow_id: str
    transported_arrow_id: str
    source_vertical_id: str
    target_vertical_id: str
    calibrated_state: QMatrix
    calibrated_effect: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "arrow_id": self.arrow_id,
            "transported_arrow_id": self.transported_arrow_id,
            "source_vertical_id": self.source_vertical_id,
            "target_vertical_id": self.target_vertical_id,
            "calibrated_state": self.calibrated_state,
            "calibrated_effect": self.calibrated_effect,
        }


@dataclass(frozen=True, slots=True)
class ClassicalPrimitiveLaw:
    root: str
    identifier: str
    active_boundary_ids: tuple[str, ...]
    boundaries: tuple[TypedBoundary, ...]
    tensor_boundaries: tuple[TypedBoundary, ...]
    arrows: tuple[TypedArrow, ...]
    instruments: tuple[TypedInstrument, ...]
    identity_arrow_ids: tuple[str, ...]
    factorizations: tuple[TypedFactorization, ...]
    two_step_factorization_id: str
    alternate_cut_ids: tuple[str, ...]
    tensor: TensorPrimitive
    vertical_maps: tuple[TypedVerticalMap, ...]
    naturality: NaturalityPrimitive
    opaque_proofs: tuple[tuple[str, str], ...] = ()
    transition_reference_id: str | None = "shared-transition-X"

    def to_data(self) -> dict[str, object]:
        return {
            "type": "ClassicalPrimitiveLaw",
            "root": self.root,
            "id": self.identifier,
            "active_boundary_ids": self.active_boundary_ids,
            "boundaries": self.boundaries,
            "tensor_boundaries": self.tensor_boundaries,
            "arrows": self.arrows,
            "instruments": self.instruments,
            "identity_arrow_ids": self.identity_arrow_ids,
            "factorizations": self.factorizations,
            "two_step_factorization_id": self.two_step_factorization_id,
            "alternate_cut_ids": self.alternate_cut_ids,
            "tensor": self.tensor,
            "vertical_maps": self.vertical_maps,
            "naturality": self.naturality,
            "opaque_proofs": self.opaque_proofs,
            "transition_reference_id": self.transition_reference_id,
        }


@dataclass(frozen=True, slots=True)
class ClassicalLawMeasurement:
    primitive_payload_sha256: str
    consumed_primitive_ids: tuple[str, ...]
    coordinate: str
    valid: bool
    residuals: Mapping[str, object]
    issues: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "ClassicalLawMeasurement",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "consumed_primitive_ids": self.consumed_primitive_ids,
            "coordinate": self.coordinate,
            "classical_valid": self.valid,
            "quantum_valid": False,
            "residuals": self.residuals,
            "issues": self.issues,
            "missing": self.issues,
            "contradictions": (),
        }


def _unique_index(values: Sequence[object], role: str) -> tuple[dict[str, object], list[str]]:
    result: dict[str, object] = {}
    issues: list[str] = []
    for value in values:
        identifier = getattr(value, "identifier", None)
        if not isinstance(identifier, str) or not identifier:
            issues.append(f"{role}:missing-id")
        elif identifier in result:
            issues.append(f"{role}:duplicate:{identifier}")
        else:
            result[identifier] = value
    return result, issues


def measure_classical_primitive_law(law: object) -> ClassicalLawMeasurement:
    if not isinstance(law, ClassicalPrimitiveLaw):
        raise ScoreRefusal("classical promotion requires ClassicalPrimitiveLaw")
    payload_hash = canonical_sha256(law.to_data())
    issues: list[str] = []
    residuals: dict[str, object] = {}
    if not law.root or not law.identifier:
        issues.append("law-root-or-id")

    boundary_index_raw, boundary_issues = _unique_index(
        law.boundaries + law.tensor_boundaries, "boundary"
    )
    boundary_index = {
        key: value for key, value in boundary_index_raw.items() if isinstance(value, TypedBoundary)
    }
    issues.extend(boundary_issues)
    active_ids = tuple(law.active_boundary_ids)
    if (
        not active_ids
        or len(set(active_ids)) != len(active_ids)
        or set(active_ids) != {row.identifier for row in law.boundaries}
    ):
        issues.append("frontier-constructor-not-total-on-declared-domain")
    for boundary in boundary_index.values():
        if (
            boundary.root != law.root
            or not boundary.frontier
            or len(set(boundary.frontier)) != len(boundary.frontier)
            or any(not isinstance(port, str) or not port for port in boundary.frontier)
        ):
            issues.append(f"boundary-typing:{boundary.identifier}")

    arrow_index_raw, arrow_issues = _unique_index(law.arrows, "arrow")
    arrow_index = {
        key: value for key, value in arrow_index_raw.items() if isinstance(value, TypedArrow)
    }
    issues.extend(arrow_issues)
    arrow_rows: dict[str, object] = {}
    for arrow_id, arrow in sorted(arrow_index.items()):
        source = boundary_index.get(arrow.source_id)
        target = boundary_index.get(arrow.target_id)
        shape_expected = (
            (len(target.frontier), len(source.frontier))
            if isinstance(source, TypedBoundary) and isinstance(target, TypedBoundary)
            else None
        )
        dimensioned = shape_expected is not None and arrow.matrix.shape == shape_expected
        nonnegative = all(item >= 0 for row in arrow.matrix.data for item in row)
        column_residual = _q_column_residual(arrow.matrix)
        mass_preserving = all(item == 0 for item in column_residual)
        connected = arrow.root == law.root
        if not (dimensioned and nonnegative and mass_preserving and connected):
            issues.append(f"arrow-law:{arrow_id}")
        arrow_rows[arrow_id] = {
            "declared_shape": shape_expected,
            "actual_shape": arrow.matrix.shape,
            "dimension_residual": 0 if dimensioned else 1,
            "negative_entry_count": sum(
                item < 0 for row in arrow.matrix.data for item in row
            ),
            "column_sum_residual": column_residual,
            "zero_vector_retained": True,
            "output_frontier_retained": (
                target.frontier if isinstance(target, TypedBoundary) else ()
            ),
            "connected": connected,
        }
    residuals["arrows"] = arrow_rows

    instrument_rows: dict[str, object] = {}
    instrument_index_raw, instrument_issues = _unique_index(law.instruments, "instrument")
    instrument_index = {
        key: value
        for key, value in instrument_index_raw.items()
        if isinstance(value, TypedInstrument)
    }
    issues.extend(instrument_issues)
    for instrument_id, instrument in sorted(instrument_index.items()):
        source = boundary_index.get(instrument.source_id)
        target = boundary_index.get(instrument.target_id)
        expected_shape = (
            (len(target.frontier), len(source.frontier))
            if isinstance(source, TypedBoundary) and isinstance(target, TypedBoundary)
            else None
        )
        branches_typed = bool(
            expected_shape is not None
            and instrument.root == law.root
            and instrument.flags
            and len(instrument.flags) == len(set(instrument.flags))
            and len(instrument.flags) == len(instrument.branch_matrices)
            and all(branch.shape == expected_shape for branch in instrument.branch_matrices)
            and all(
                item >= 0
                for branch in instrument.branch_matrices
                for row in branch.data
                for item in row
            )
        )
        branch_sum = (
            instrument.branch_matrices[0]
            if instrument.branch_matrices
            else QMatrix.zero(0, 0)
        )
        for branch in instrument.branch_matrices[1:]:
            if branch.shape == branch_sum.shape:
                branch_sum = qadd(branch_sum, branch)
        completeness = (
            _q_column_residual(branch_sum)
            if branches_typed
            else (Fraction(1),)
        )
        flagged = (
            qvstack(instrument.branch_matrices, ncols=expected_shape[1])
            if branches_typed and expected_shape is not None
            else QMatrix.zero(0, 0)
        )
        flagged_residual = (
            _q_column_residual(flagged) if branches_typed else (Fraction(1),)
        )
        valid = branches_typed and all(value == 0 for value in completeness) and all(
            value == 0 for value in flagged_residual
        )
        if not valid:
            issues.append(f"instrument-law:{instrument_id}")
        instrument_rows[instrument_id] = {
            "branch_shapes": tuple(branch.shape for branch in instrument.branch_matrices),
            "branch_sum_column_residual": completeness,
            "stacked_flagged_arrow": flagged,
            "stacked_column_residual": flagged_residual,
            "individual_branches_subnormalized": tuple(
                any(value != 0 for value in _q_column_residual(branch))
                for branch in instrument.branch_matrices
            ),
            "valid": valid,
        }
    residuals["instruments"] = instrument_rows

    identity_rows: dict[str, object] = {}
    identity_boundaries: list[str] = []
    for identity_id in law.identity_arrow_ids:
        arrow = arrow_index.get(identity_id)
        valid = False
        boundary_id: str | None = None
        identity_residual: dict[str, object] = {"nonzero_count": None}
        if isinstance(arrow, TypedArrow) and arrow.source_id == arrow.target_id:
            boundary_id = arrow.source_id
            boundary = boundary_index.get(boundary_id)
            if isinstance(boundary, TypedBoundary):
                identity_residual = _q_residual(
                    arrow.matrix, QMatrix.identity(len(boundary.frontier))
                )
                valid = bool(
                    arrow.root == law.root
                    and arrow.process_word == ()
                    and identity_residual["nonzero_count"] == 0
                )
        if boundary_id is not None:
            identity_boundaries.append(boundary_id)
        if not valid:
            issues.append(f"identity-law:{identity_id}")
        identity_rows[str(identity_id)] = {
            "boundary_id": boundary_id,
            "empty_process_attached": bool(
                isinstance(arrow, TypedArrow) and arrow.process_word == ()
            ),
            "matrix_residual": identity_residual,
            "valid": valid,
        }
    identity_exact = (
        len(identity_boundaries) == len(active_ids)
        and len(set(identity_boundaries)) == len(active_ids)
        and set(identity_boundaries) == set(active_ids)
    )
    if not identity_exact:
        issues.append("active-identity-domain")
    residuals["identities"] = {
        "rows": identity_rows,
        "active_domain": active_ids,
        "exactly_one_per_active_object": identity_exact,
    }

    factor_index_raw, factor_issues = _unique_index(law.factorizations, "factorization")
    factor_index = {
        key: value
        for key, value in factor_index_raw.items()
        if isinstance(value, TypedFactorization)
    }
    issues.extend(factor_issues)
    factor_rows: dict[str, object] = {}
    factor_products: dict[str, QMatrix] = {}
    for factor_id, factor in sorted(factor_index.items()):
        whole = arrow_index.get(factor.whole_arrow_id)
        occurrences = [arrow_index.get(identifier) for identifier in factor.arrow_occurrence_ids]
        typed = bool(
            factor.root == law.root
            and isinstance(whole, TypedArrow)
            and occurrences
            and all(isinstance(item, TypedArrow) for item in occurrences)
        )
        composable = typed
        product: QMatrix | None = None
        if typed:
            first = occurrences[0]
            assert isinstance(first, TypedArrow)
            product = first.matrix
            prior_target = first.target_id
            for occurrence in occurrences[1:]:
                assert isinstance(occurrence, TypedArrow)
                if occurrence.source_id != prior_target:
                    composable = False
                    break
                try:
                    product = qmultiply(occurrence.matrix, product)
                except ValueError:
                    composable = False
                    break
                prior_target = occurrence.target_id
            if isinstance(whole, TypedArrow) and (
                first.source_id != whole.source_id or prior_target != whole.target_id
            ):
                composable = False
        residual = (
            _q_residual(product, whole.matrix)
            if composable and product is not None and isinstance(whole, TypedArrow)
            else {"shape_match": False, "nonzero_count": None}
        )
        valid = composable and residual.get("nonzero_count") == 0
        if not valid:
            issues.append(f"factorization-law:{factor_id}")
        if product is not None:
            factor_products[factor_id] = product
        factor_rows[factor_id] = {
            "occurrence_count": len(factor.arrow_occurrence_ids),
            "occurrence_ids": factor.arrow_occurrence_ids,
            "composable": composable,
            "recomputed_product": product,
            "whole_residual": residual,
            "valid": valid,
        }
    two_step = factor_index.get(law.two_step_factorization_id)
    two_step_valid = False
    if isinstance(two_step, TypedFactorization) and len(two_step.arrow_occurrence_ids) == 2:
        two_arrows = [arrow_index.get(identifier) for identifier in two_step.arrow_occurrence_ids]
        two_step_valid = bool(
            len(set(two_step.arrow_occurrence_ids)) == 2
            and factor_rows.get(two_step.identifier, {}).get("valid")
            and all(
                isinstance(arrow, TypedArrow)
                and (
                    arrow.source_id != arrow.target_id
                    or arrow.matrix
                    != QMatrix.identity(arrow.matrix.nrows)
                )
                for arrow in two_arrows
            )
        )
    if not two_step_valid:
        issues.append("missing-two-nonidentity-occurrences")
    cut_wholes = {
        factor_index[identifier].whole_arrow_id
        for identifier in law.alternate_cut_ids
        if identifier in factor_index
    }
    cuts_valid = bool(
        len(law.alternate_cut_ids) >= 2
        and len(set(law.alternate_cut_ids)) == len(law.alternate_cut_ids)
        and all(
            identifier in factor_rows and factor_rows[identifier]["valid"]
            for identifier in law.alternate_cut_ids
        )
        and len(cut_wholes) == 1
    )
    if not cuts_valid:
        issues.append("alternate-cut-equality")
    residuals["factorizations"] = {
        "rows": factor_rows,
        "two_nonidentity_occurrences": two_step_valid,
        "alternate_cuts_same_whole": cuts_valid,
    }

    tensor = law.tensor
    tensor_rows: dict[str, object] = {}
    tensor_valid = tensor.root == law.root
    product_boundaries: dict[tuple[str, str], str] = {}
    for claim in tensor.boundary_claims:
        left = boundary_index.get(claim.left_boundary_id)
        right = boundary_index.get(claim.right_boundary_id)
        product = boundary_index.get(claim.product_boundary_id)
        expected = (
            _tensor_frontier(left.frontier, right.frontier)
            if isinstance(left, TypedBoundary) and isinstance(right, TypedBoundary)
            else None
        )
        valid = bool(
            isinstance(product, TypedBoundary)
            and expected is not None
            and product.frontier == expected
            and product.root == law.root
        )
        key = (claim.left_boundary_id, claim.right_boundary_id)
        if key in product_boundaries:
            valid = False
        product_boundaries[key] = claim.product_boundary_id
        tensor_valid = tensor_valid and valid
        tensor_rows[f"boundary:{claim.product_boundary_id}"] = {
            "expected_frontier": expected,
            "actual_frontier": (
                product.frontier if isinstance(product, TypedBoundary) else None
            ),
            "residual": 0 if valid else 1,
        }
    arrow_claim_by_pair: dict[tuple[str, str], TypedArrow] = {}
    for claim in tensor.arrow_claims:
        left = arrow_index.get(claim.left_arrow_id)
        right = arrow_index.get(claim.right_arrow_id)
        product = arrow_index.get(claim.product_arrow_id)
        expected_matrix: QMatrix | None = None
        valid = False
        if isinstance(left, TypedArrow) and isinstance(right, TypedArrow):
            expected_matrix = _q_kron(left.matrix, right.matrix)
            expected_source = product_boundaries.get((left.source_id, right.source_id))
            expected_target = product_boundaries.get((left.target_id, right.target_id))
            valid = bool(
                isinstance(product, TypedArrow)
                and product.source_id == expected_source
                and product.target_id == expected_target
                and product.matrix == expected_matrix
                and product.root == law.root
            )
        tensor_valid = tensor_valid and valid
        if isinstance(product, TypedArrow):
            arrow_claim_by_pair[(claim.left_arrow_id, claim.right_arrow_id)] = product
        tensor_rows[f"arrow:{claim.product_arrow_id}"] = {
            "expected_matrix": expected_matrix,
            "actual_matrix": product.matrix if isinstance(product, TypedArrow) else None,
            "residual": (
                _q_residual(product.matrix, expected_matrix)
                if isinstance(product, TypedArrow) and expected_matrix is not None
                else {"shape_match": False, "nonzero_count": None}
            ),
            "valid": valid,
        }
    unit_boundary = boundary_index.get(tensor.unit_boundary_id)
    unit_valid = isinstance(unit_boundary, TypedBoundary) and len(unit_boundary.frontier) == 1
    assoc_boundaries = [boundary_index.get(item) for item in tensor.associator_boundary_ids]
    associator_expected = (
        _associator_permutation(*(len(item.frontier) for item in assoc_boundaries))
        if all(isinstance(item, TypedBoundary) for item in assoc_boundaries)
        else None
    )
    associator_residual = (
        _q_residual(tensor.associator_matrix, associator_expected)
        if associator_expected is not None
        else {"shape_match": False, "nonzero_count": None}
    )
    associator_valid = associator_residual.get("nonzero_count") == 0
    symmetry_boundaries = [boundary_index.get(item) for item in tensor.symmetry_boundary_ids]
    symmetry_expected = (
        _symmetry_permutation(
            len(symmetry_boundaries[0].frontier), len(symmetry_boundaries[1].frontier)
        )
        if all(isinstance(item, TypedBoundary) for item in symmetry_boundaries)
        else None
    )
    symmetry_residual = (
        _q_residual(tensor.symmetry_matrix, symmetry_expected)
        if symmetry_expected is not None
        else {"shape_match": False, "nonzero_count": None}
    )
    symmetry_valid = symmetry_residual.get("nonzero_count") == 0
    associativity_arrows = [arrow_index.get(item) for item in tensor.associativity_arrow_ids]
    associativity_residual: dict[str, object] = {"shape_match": False, "nonzero_count": None}
    if all(isinstance(item, TypedArrow) for item in associativity_arrows):
        first_arrow, second_arrow, third_arrow = associativity_arrows
        assert isinstance(first_arrow, TypedArrow)
        assert isinstance(second_arrow, TypedArrow)
        assert isinstance(third_arrow, TypedArrow)
        left_assoc = _q_kron(_q_kron(first_arrow.matrix, second_arrow.matrix), third_arrow.matrix)
        right_assoc = _q_kron(first_arrow.matrix, _q_kron(second_arrow.matrix, third_arrow.matrix))
        if associator_expected is not None and left_assoc.shape == associator_expected.shape:
            transported = qmultiply(
                associator_expected,
                qmultiply(left_assoc, qtranspose(associator_expected)),
            )
            associativity_residual = _q_residual(transported, right_assoc)
    associativity_valid = associativity_residual.get("nonzero_count") == 0
    interchange_arrows = [arrow_index.get(item) for item in tensor.interchange_arrow_ids]
    interchange_residual: dict[str, object] = {"shape_match": False, "nonzero_count": None}
    claimed_interchange_residual: dict[str, object] = {
        "shape_match": False,
        "nonzero_count": None,
    }
    if all(isinstance(item, TypedArrow) for item in interchange_arrows):
        first, second, spectator_first, spectator_second = interchange_arrows
        assert isinstance(first, TypedArrow)
        assert isinstance(second, TypedArrow)
        assert isinstance(spectator_first, TypedArrow)
        assert isinstance(spectator_second, TypedArrow)
        if (
            second.source_id == first.target_id
            and spectator_second.source_id == spectator_first.target_id
        ):
            try:
                left_interchange = qmultiply(
                    _q_kron(second.matrix, spectator_second.matrix),
                    _q_kron(first.matrix, spectator_first.matrix),
                )
                right_interchange = _q_kron(
                    qmultiply(second.matrix, first.matrix),
                    qmultiply(spectator_second.matrix, spectator_first.matrix),
                )
                interchange_residual = _q_residual(
                    left_interchange, right_interchange
                )
                claimed_first = arrow_index.get(
                    tensor.interchange_tensor_arrow_ids[0]
                )
                claimed_second = arrow_index.get(
                    tensor.interchange_tensor_arrow_ids[1]
                )
                if isinstance(claimed_first, TypedArrow) and isinstance(
                    claimed_second, TypedArrow
                ):
                    claimed_interchange_residual = _q_residual(
                        qmultiply(claimed_second.matrix, claimed_first.matrix),
                        right_interchange,
                    )
            except ValueError:
                pass
    interchange_valid = bool(
        interchange_residual.get("nonzero_count") == 0
        and claimed_interchange_residual.get("nonzero_count") == 0
    )
    tensor_valid = bool(
        tensor_valid
        and unit_valid
        and associator_valid
        and symmetry_valid
        and associativity_valid
        and interchange_valid
    )
    if not tensor_valid:
        issues.append("tensor-unit-associator-symmetry-interchange")
    residuals["tensor"] = {
        "ordering": "left-major-lexicographic",
        "claims": tensor_rows,
        "unit_valid": unit_valid,
        "associator_residual": associator_residual,
        "symmetry_residual": symmetry_residual,
        "associativity_transport_residual": associativity_residual,
        "interchange_residual": interchange_residual,
        "claimed_interchange_residual": claimed_interchange_residual,
        "valid": tensor_valid,
    }

    vertical_index_raw, vertical_issues = _unique_index(law.vertical_maps, "vertical-map")
    vertical_index = {
        key: value
        for key, value in vertical_index_raw.items()
        if isinstance(value, TypedVerticalMap)
    }
    issues.extend(vertical_issues)
    vertical_rows: dict[str, object] = {}
    vertical_valid = True
    for vertical_id, vertical in sorted(vertical_index.items()):
        source = boundary_index.get(vertical.source_id)
        target = boundary_index.get(vertical.target_id)
        expected_shape = (
            (len(target.frontier), len(source.frontier))
            if isinstance(source, TypedBoundary) and isinstance(target, TypedBoundary)
            else None
        )
        permutation, inverse = _q_is_permutation(vertical.matrix)
        valid = bool(
            vertical.root == law.root
            and expected_shape == vertical.matrix.shape
            and permutation
        )
        vertical_valid = vertical_valid and valid
        vertical_rows[vertical_id] = {
            "expected_shape": expected_shape,
            "permutation_entrywise": permutation,
            "inverse": inverse,
            "rank": qrank(vertical.matrix),
            "valid": valid,
        }
    naturality = law.naturality
    arrow = arrow_index.get(naturality.arrow_id)
    transported_arrow = arrow_index.get(naturality.transported_arrow_id)
    source_vertical = vertical_index.get(naturality.source_vertical_id)
    target_vertical = vertical_index.get(naturality.target_vertical_id)
    naturality_residual: dict[str, object] = {"shape_match": False, "nonzero_count": None}
    state_movement = False
    effect_movement = False
    if all(
        isinstance(item, expected)
        for item, expected in (
            (arrow, TypedArrow),
            (transported_arrow, TypedArrow),
            (source_vertical, TypedVerticalMap),
            (target_vertical, TypedVerticalMap),
        )
    ):
        assert isinstance(arrow, TypedArrow)
        assert isinstance(transported_arrow, TypedArrow)
        assert isinstance(source_vertical, TypedVerticalMap)
        assert isinstance(target_vertical, TypedVerticalMap)
        if (
            source_vertical.source_id == arrow.source_id
            and source_vertical.target_id == transported_arrow.source_id
            and target_vertical.source_id == arrow.target_id
            and target_vertical.target_id == transported_arrow.target_id
        ):
            try:
                naturality_residual = _q_residual(
                    qmultiply(target_vertical.matrix, arrow.matrix),
                    qmultiply(transported_arrow.matrix, source_vertical.matrix),
                )
                state_movement = (
                    qmultiply(source_vertical.matrix, naturality.calibrated_state)
                    != naturality.calibrated_state
                )
                target_inverse = qtranspose(target_vertical.matrix)
                effect_movement = (
                    qmultiply(naturality.calibrated_effect, target_inverse)
                    != naturality.calibrated_effect
                )
            except ValueError:
                pass
    source_nonidentity = bool(
        isinstance(source_vertical, TypedVerticalMap)
        and source_vertical.matrix
        != QMatrix.identity(source_vertical.matrix.nrows)
    )
    target_nonidentity = bool(
        isinstance(target_vertical, TypedVerticalMap)
        and target_vertical.matrix
        != QMatrix.identity(target_vertical.matrix.nrows)
    )
    naturality_valid = bool(
        naturality.root == law.root
        and vertical_valid
        and source_nonidentity
        and target_nonidentity
        and state_movement
        and effect_movement
        and naturality_residual.get("nonzero_count") == 0
    )
    if not naturality_valid:
        issues.append("nonidentity-permutation-naturality")
    residuals["naturality"] = {
        "vertical_maps": vertical_rows,
        "square_residual": naturality_residual,
        "source_nonidentity": source_nonidentity,
        "target_nonidentity": target_nonidentity,
        "calibrated_state_moved": state_movement,
        "calibrated_effect_moved": effect_movement,
        "valid": naturality_valid,
    }

    consumed_ids = tuple(
        sorted(
            {law.identifier, law.tensor.identifier, law.naturality.identifier}
            | set(boundary_index)
            | set(arrow_index)
            | set(instrument_index)
            | set(factor_index)
            | set(vertical_index)
            | ({law.transition_reference_id} if law.transition_reference_id else set())
        )
    )
    valid = not issues
    return ClassicalLawMeasurement(
        primitive_payload_sha256=payload_hash,
        consumed_primitive_ids=consumed_ids,
        coordinate="HORIZONTAL-CLASSICAL" if valid else "STATIC-RESPONSE-ONLY",
        valid=valid,
        residuals=residuals,
        issues=tuple(sorted(set(issues))),
    )


def build_classical_existence_law(fault: str | None = None) -> ClassicalPrimitiveLaw:
    root = V4_INTERNAL_ROOT
    two = ("0", "1")
    boundary_rows = [
        TypedBoundary(root, "A", two),
        TypedBoundary(root, "B", ("0",) if fault == "dropped-zero-port" else two),
        TypedBoundary(root, "C", two),
        TypedBoundary(root, "U", ("u0", "u1") if fault == "wrong-unit" else ("unit",)),
    ]
    product_specs = (
        ("A", "A", "AA"),
        ("B", "B", "BB"),
        ("C", "C", "CC"),
        ("A", "U", "AU"),
        ("B", "U", "BU"),
    )
    base_index = {row.identifier: row for row in boundary_rows}
    tensor_boundaries: list[TypedBoundary] = []
    for left_id, right_id, product_id in product_specs:
        left = base_index[left_id]
        right = base_index[right_id]
        frontier = _tensor_frontier(left.frontier, right.frontier)
        if fault == "wrong-tensor-frontier" and product_id == "AA":
            frontier = tuple(reversed(frontier))
        tensor_boundaries.append(TypedBoundary(root, product_id, frontier))

    identity = QMatrix.identity(2)
    flip = QMatrix.from_rows(((0, 1), (1, 0)))
    unit_identity = QMatrix.identity(len(base_index["U"].frontier))
    f_matrix = flip
    f_source = "A"
    f_target = "B"
    if fault == "frontier-domain-mismatch":
        f_matrix = QMatrix.from_rows(((1,), (0,)))
    elif fault == "frontier-codomain-mismatch":
        f_matrix = QMatrix.from_rows(((1, 0),), ncols=2)
    elif fault == "negative-entry":
        f_matrix = QMatrix.from_rows(((2, 0), (-1, 1)))
    elif fault == "nonconserving":
        f_matrix = QMatrix.from_rows(((1, 0), (0, 2)))
    g_source = "MISSING" if fault == "missing-intermediate" else "B"
    whole_matrix = flip if fault == "wrong-whole" else identity
    r2_matrix = flip if fault == "altered-cut" else identity
    arrows = [
        TypedArrow(root, "id_A", "identity", "A", "A", identity, ()),
        TypedArrow(root, "id_B", "identity", "B", "B", QMatrix.identity(len(base_index["B"].frontier)), ()),
        TypedArrow(root, "id_C", "identity", "C", "C", identity, ()),
        TypedArrow(root, "id_U", "identity", "U", "U", unit_identity, ()),
        TypedArrow(root, "f_occ", "X", f_source, f_target, f_matrix, ("X:first",)),
        TypedArrow(root, "g_occ", "X", g_source, "C", flip, ("X:second",)),
        TypedArrow(root, "r1_occ", "I-route", "A", "B", identity, ("I:first",)),
        TypedArrow(root, "r2_occ", "I-route", "B", "C", r2_matrix, ("I:second",)),
        TypedArrow(root, "whole_h", "whole", "A", "C", whole_matrix, ("whole",)),
        TypedArrow(root, "x_A", "X", "A", "A", flip, ("X:endomorphism",)),
        TypedArrow(root, "k_occ", "X", "A", "B", flip, ("X:spectator-first",)),
        TypedArrow(root, "h_occ", "X", "B", "C", flip, ("X:spectator-second",)),
        TypedArrow(root, "f_prime", "X-conjugate", "A", "B", flip, ("conjugated",)),
    ]
    product_boundary_index = {row.identifier: row for row in tensor_boundaries}
    tfk_matrix = QMatrix.identity(4) if fault == "wrong-interchange" else _q_kron(flip, flip)
    arrows.extend(
        [
            TypedArrow(root, "tensor_fk", "tensor", "AA", "BB", tfk_matrix, ("tensor",)),
            TypedArrow(root, "tensor_gh", "tensor", "BB", "CC", _q_kron(flip, flip), ("tensor",)),
            TypedArrow(
                root,
                "tensor_f_unit",
                "tensor",
                "AU",
                "BU",
                _q_kron(flip, unit_identity),
                ("tensor-unit",),
            ),
        ]
    )
    if fault == "opaque-replacement":
        arrows = []

    q0 = QMatrix.from_rows(((1, 0), (0, 0)))
    q1 = QMatrix.from_rows(((0, 0), (0, 1)))
    instruments = (
        TypedInstrument(root, "question_instrument", "A", "A", ("0", "1"), (q0, q1)),
    )
    factors = [
        TypedFactorization(
            root,
            "cut_flip_flip",
            "whole_h",
            ("f_occ",) if fault == "one-standalone-occurrence" else ("f_occ", "g_occ"),
        ),
        TypedFactorization(root, "cut_identity_route", "whole_h", ("r1_occ", "r2_occ")),
    ]
    if fault == "opaque-replacement":
        factors = []

    boundary_claims = tuple(
        TensorBoundaryClaim(left, right, product)
        for left, right, product in product_specs
    )
    arrow_claims = (
        TensorArrowClaim("f_occ", "k_occ", "tensor_fk"),
        TensorArrowClaim("g_occ", "h_occ", "tensor_gh"),
        TensorArrowClaim("f_occ", "id_U", "tensor_f_unit"),
    )
    associator = _associator_permutation(2, 2, len(base_index["U"].frontier))
    if fault == "wrong-associator":
        associator = _q_permutation_from_images(tuple(reversed(range(associator.nrows))))
    symmetry = _symmetry_permutation(2, 2)
    if fault == "wrong-symmetry":
        symmetry = QMatrix.identity(4)
    tensor = TensorPrimitive(
        root=root,
        identifier="tensor_primitive",
        unit_boundary_id="U",
        boundary_claims=boundary_claims,
        arrow_claims=arrow_claims,
        associator_boundary_ids=("A", "A", "U"),
        associator_matrix=associator,
        symmetry_boundary_ids=("A", "A"),
        symmetry_matrix=symmetry,
        associativity_arrow_ids=("f_occ", "k_occ", "id_U"),
        interchange_arrow_ids=("f_occ", "g_occ", "k_occ", "h_occ"),
        interchange_tensor_arrow_ids=("tensor_fk", "tensor_gh"),
    )
    vertical_matrix = flip
    target_vertical_matrix = flip
    naturality_root = root
    if fault == "identity-naturality":
        vertical_matrix = identity
        target_vertical_matrix = identity
    elif fault == "changed-target-vertical":
        target_vertical_matrix = identity
    elif fault == "rank-deficient-vertical":
        target_vertical_matrix = QMatrix.zero(2, 2)
    elif fault == "disconnected-naturality":
        naturality_root = "v4:disconnected"
    vertical_maps = (
        TypedVerticalMap(root, "J_A", "A", "A", vertical_matrix),
        TypedVerticalMap(root, "J_B", "B", "B", target_vertical_matrix),
    )
    naturality = NaturalityPrimitive(
        root=naturality_root,
        identifier="naturality_square",
        arrow_id="f_occ",
        transported_arrow_id="f_prime",
        source_vertical_id="J_A",
        target_vertical_id="J_B",
        calibrated_state=QMatrix.from_rows(((1,), (0,))),
        calibrated_effect=QMatrix.from_rows(((1, 0),), ncols=2),
    )
    identities = ["id_A", "id_B", "id_C", "id_U"]
    if fault == "duplicate-identity":
        identities.append("id_A")
    elif fault == "missing-identity":
        identities.remove("id_C")
    opaque = (
        (("copy-oracle", "same opaque equation bytes"),)
        if fault == "opaque-replacement"
        else (("unused", "changed but inert"),)
        if fault == "unused-proof-change"
        else ()
    )
    return ClassicalPrimitiveLaw(
        root=root,
        identifier="classical_existence_law",
        active_boundary_ids=("A", "B", "C", "U"),
        boundaries=tuple(boundary_rows),
        tensor_boundaries=tuple(tensor_boundaries),
        arrows=tuple(arrows),
        instruments=instruments,
        identity_arrow_ids=tuple(identities),
        factorizations=tuple(factors),
        two_step_factorization_id="cut_flip_flip",
        alternate_cut_ids=("cut_flip_flip", "cut_identity_route"),
        tensor=tensor,
        vertical_maps=vertical_maps,
        naturality=naturality,
        opaque_proofs=opaque,
    )


@dataclass(frozen=True, slots=True)
class GaussianRational:
    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "real", exact(self.real))
        object.__setattr__(self, "imag", exact(self.imag))

    @classmethod
    def coerce(cls, value: object) -> "GaussianRational":
        if isinstance(value, cls):
            return value
        return cls(exact(value), Fraction(0))

    def __add__(self, other: object) -> "GaussianRational":
        right = self.coerce(other)
        return GaussianRational(self.real + right.real, self.imag + right.imag)

    def __radd__(self, other: object) -> "GaussianRational":
        return self + other

    def __neg__(self) -> "GaussianRational":
        return GaussianRational(-self.real, -self.imag)

    def __sub__(self, other: object) -> "GaussianRational":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "GaussianRational":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "GaussianRational":
        right = self.coerce(other)
        return GaussianRational(
            self.real * right.real - self.imag * right.imag,
            self.real * right.imag + self.imag * right.real,
        )

    def __rmul__(self, other: object) -> "GaussianRational":
        return self * other

    def __truediv__(self, other: object) -> "GaussianRational":
        right = self.coerce(other)
        denominator = right.real * right.real + right.imag * right.imag
        if denominator == 0:
            raise ZeroDivisionError("Gaussian-rational division by zero")
        numerator = self * right.conjugate()
        return GaussianRational(numerator.real / denominator, numerator.imag / denominator)

    def conjugate(self) -> "GaussianRational":
        return GaussianRational(self.real, -self.imag)

    def is_zero(self) -> bool:
        return self.real == 0 and self.imag == 0

    def to_data(self) -> dict[str, str]:
        return {"real": fraction_text(self.real), "imag": fraction_text(self.imag)}


GI = GaussianRational(0, 1)
GZERO = GaussianRational()
GONE = GaussianRational(1)


@dataclass(frozen=True, slots=True)
class GMatrix:
    data: tuple[tuple[GaussianRational, ...], ...]
    ncols: int

    @classmethod
    def from_rows(
        cls, rows: Iterable[Iterable[object]], *, ncols: int | None = None
    ) -> "GMatrix":
        converted = tuple(
            tuple(GaussianRational.coerce(item) for item in row) for row in rows
        )
        width = ncols if not converted and ncols is not None else (
            len(converted[0]) if converted else 0
        )
        if width < 0 or any(len(row) != width for row in converted):
            raise ValueError("Gaussian matrix has ragged rows")
        return cls(converted, width)

    @classmethod
    def zero(cls, nrows: int, ncols: int) -> "GMatrix":
        return cls.from_rows(
            ((GZERO for _ in range(ncols)) for _ in range(nrows)), ncols=ncols
        )

    @classmethod
    def identity(cls, size: int) -> "GMatrix":
        return cls.from_rows(
            (
                (GONE if row == column else GZERO for column in range(size))
                for row in range(size)
            ),
            ncols=size,
        )

    @property
    def nrows(self) -> int:
        return len(self.data)

    @property
    def shape(self) -> tuple[int, int]:
        return self.nrows, self.ncols

    def to_data(self) -> dict[str, object]:
        return {
            "shape": self.shape,
            "rows": tuple(tuple(item.to_data() for item in row) for row in self.data),
        }


def _g_from_q(value: QMatrix) -> GMatrix:
    return GMatrix.from_rows(value.data, ncols=value.ncols)


def _g_add(left: GMatrix, right: GMatrix) -> GMatrix:
    if left.shape != right.shape:
        raise ValueError("Gaussian matrix-add shape mismatch")
    return GMatrix.from_rows(
        (
            (left.data[row][column] + right.data[row][column] for column in range(left.ncols))
            for row in range(left.nrows)
        ),
        ncols=left.ncols,
    )


def _g_scale(coefficient: object, value: GMatrix) -> GMatrix:
    factor = GaussianRational.coerce(coefficient)
    return GMatrix.from_rows(
        ((factor * item for item in row) for row in value.data), ncols=value.ncols
    )


def _g_subtract(left: GMatrix, right: GMatrix) -> GMatrix:
    return _g_add(left, _g_scale(-1, right))


def _g_multiply(left: GMatrix, right: GMatrix) -> GMatrix:
    if left.ncols != right.nrows:
        raise ValueError("Gaussian matrix-product shape mismatch")
    return GMatrix.from_rows(
        (
            (
                sum(
                    (
                        left.data[row][middle] * right.data[middle][column]
                        for middle in range(left.ncols)
                    ),
                    GZERO,
                )
                for column in range(right.ncols)
            )
            for row in range(left.nrows)
        ),
        ncols=right.ncols,
    )


def _g_transpose(value: GMatrix) -> GMatrix:
    return GMatrix.from_rows(
        (
            (value.data[row][column] for row in range(value.nrows))
            for column in range(value.ncols)
        ),
        ncols=value.nrows,
    )


def _g_adjoint(value: GMatrix) -> GMatrix:
    return GMatrix.from_rows(
        (
            (value.data[row][column].conjugate() for row in range(value.nrows))
            for column in range(value.ncols)
        ),
        ncols=value.nrows,
    )


def _g_kron(left: GMatrix, right: GMatrix) -> GMatrix:
    return GMatrix.from_rows(
        (
            (
                left.data[left_row][left_column]
                * right.data[right_row][right_column]
                for left_column in range(left.ncols)
                for right_column in range(right.ncols)
            )
            for left_row in range(left.nrows)
            for right_row in range(right.nrows)
        ),
        ncols=left.ncols * right.ncols,
    )


def _g_vstack(values: Sequence[GMatrix]) -> GMatrix:
    if not values or any(value.ncols != values[0].ncols for value in values):
        raise ValueError("Gaussian row-stack shape mismatch")
    return GMatrix.from_rows(
        (row for value in values for row in value.data), ncols=values[0].ncols
    )


def _g_trace(value: GMatrix) -> GaussianRational:
    if value.nrows != value.ncols:
        raise ValueError("Gaussian trace needs a square matrix")
    return sum((value.data[index][index] for index in range(value.nrows)), GZERO)


def _g_nonzero_count(value: GMatrix) -> int:
    return sum(not item.is_zero() for row in value.data for item in row)


def _g_residual(left: GMatrix, right: GMatrix) -> dict[str, object]:
    if left.shape != right.shape:
        return {
            "shape_match": False,
            "left_shape": left.shape,
            "right_shape": right.shape,
            "nonzero_count": None,
        }
    difference = _g_subtract(left, right)
    return {
        "shape_match": True,
        "difference": difference,
        "nonzero_count": _g_nonzero_count(difference),
    }


def _g_determinant(value: GMatrix) -> GaussianRational:
    if value.nrows != value.ncols:
        raise ValueError("Gaussian determinant needs a square matrix")
    rows = [list(row) for row in value.data]
    result = GONE
    sign = 1
    for column in range(value.ncols):
        pivot = next(
            (row for row in range(column, value.nrows) if not rows[row][column].is_zero()),
            None,
        )
        if pivot is None:
            return GZERO
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            sign *= -1
        pivot_value = rows[column][column]
        result = result * pivot_value
        for row in range(column + 1, value.nrows):
            if rows[row][column].is_zero():
                continue
            factor = rows[row][column] / pivot_value
            for offset in range(column, value.ncols):
                rows[row][offset] = rows[row][offset] - factor * rows[column][offset]
    return result * sign


def _g_positive_semidefinite(value: GMatrix) -> tuple[bool, tuple[dict[str, object], ...]]:
    if value.nrows != value.ncols or value != _g_adjoint(value):
        return False, ()
    rows: list[dict[str, object]] = []
    valid = True
    for size in range(1, value.nrows + 1):
        for selected in itertools.combinations(range(value.nrows), size):
            principal = GMatrix.from_rows(
                (
                    (value.data[row][column] for column in selected)
                    for row in selected
                ),
                ncols=size,
            )
            determinant = _g_determinant(principal)
            nonnegative_real = determinant.imag == 0 and determinant.real >= 0
            valid = valid and nonnegative_real
            rows.append(
                {
                    "indices": selected,
                    "determinant": determinant,
                    "nonnegative_real": nonnegative_real,
                }
            )
    return valid, tuple(rows)


@dataclass(frozen=True, slots=True)
class AmplitudeArrow:
    root: str
    identifier: str
    source_id: str
    target_id: str
    classical_arrow_id: str
    scale: GaussianRational
    matrix: GMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "classical_arrow_id": self.classical_arrow_id,
            "scale": self.scale,
            "matrix": self.matrix,
        }


@dataclass(frozen=True, slots=True)
class QuantumHistory:
    root: str
    identifier: str
    amplitude_arrow_ids: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "amplitude_arrow_ids": self.amplitude_arrow_ids,
        }


@dataclass(frozen=True, slots=True)
class DivisionPort:
    root: str
    identifier: str
    coefficients: tuple[GaussianRational, ...]

    def to_data(self) -> dict[str, object]:
        return {"root": self.root, "id": self.identifier, "coefficients": self.coefficients}


@dataclass(frozen=True, slots=True)
class QuantumCut:
    root: str
    identifier: str
    history_id: str
    alternate_amplitude_arrow_ids: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "history_id": self.history_id,
            "alternate_amplitude_arrow_ids": self.alternate_amplitude_arrow_ids,
        }


@dataclass(frozen=True, slots=True)
class FlagContinuation:
    root: str
    identifier: str
    matrix: GMatrix

    def to_data(self) -> dict[str, object]:
        return {"root": self.root, "id": self.identifier, "matrix": self.matrix}


@dataclass(frozen=True, slots=True)
class QuantumPrimitiveLaw:
    root: str
    identifier: str
    classical_law: ClassicalPrimitiveLaw
    amplitude_arrows: tuple[AmplitudeArrow, ...]
    histories: tuple[QuantumHistory, ...]
    divisions: tuple[DivisionPort, ...]
    cuts: tuple[QuantumCut, ...]
    input_state: GMatrix
    flag_continuations: tuple[FlagContinuation, ...]
    phase_control: GMatrix
    gram_test_coefficients: tuple[GaussianRational, ...]
    opaque_free_gram: GMatrix | None = None
    opaque_recovery_payload: tuple[tuple[str, str], ...] = ()

    def to_data(self) -> dict[str, object]:
        return {
            "type": "QuantumPrimitiveLaw",
            "root": self.root,
            "id": self.identifier,
            "classical_law": self.classical_law,
            "amplitude_arrows": self.amplitude_arrows,
            "histories": self.histories,
            "divisions": self.divisions,
            "cuts": self.cuts,
            "input_state": self.input_state,
            "flag_continuations": self.flag_continuations,
            "phase_control": self.phase_control,
            "gram_test_coefficients": self.gram_test_coefficients,
            "opaque_free_gram": self.opaque_free_gram,
            "opaque_recovery_payload": self.opaque_recovery_payload,
        }


@dataclass(frozen=True, slots=True)
class QuantumLawMeasurement:
    primitive_payload_sha256: str
    consumed_primitive_ids: tuple[str, ...]
    coordinate: str
    valid: bool
    classical: ClassicalLawMeasurement
    residuals: Mapping[str, object]
    issues: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "QuantumLawMeasurement",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "consumed_primitive_ids": self.consumed_primitive_ids,
            "coordinate": self.coordinate,
            "classical_valid": self.classical.valid,
            "quantum_valid": self.valid,
            "classical_measurement": self.classical,
            "residuals": self.residuals,
            "issues": self.issues,
            "missing": self.issues,
            "contradictions": (),
        }


def _compose_amplitude_path(
    identifiers: Sequence[str], arrows: Mapping[str, AmplitudeArrow]
) -> tuple[GMatrix | None, str | None, str | None, bool]:
    if not identifiers:
        return None, None, None, False
    rows = [arrows.get(identifier) for identifier in identifiers]
    if not all(isinstance(row, AmplitudeArrow) for row in rows):
        return None, None, None, False
    first = rows[0]
    assert isinstance(first, AmplitudeArrow)
    result = first.matrix
    source = first.source_id
    target = first.target_id
    for row in rows[1:]:
        assert isinstance(row, AmplitudeArrow)
        if row.source_id != target:
            return None, source, target, False
        try:
            result = _g_multiply(row.matrix, result)
        except ValueError:
            return None, source, target, False
        target = row.target_id
    return result, source, target, True


def measure_quantum_primitive_law(law: object) -> QuantumLawMeasurement:
    if not isinstance(law, QuantumPrimitiveLaw):
        raise ScoreRefusal("quantum promotion requires QuantumPrimitiveLaw")
    classical = measure_classical_primitive_law(law.classical_law)
    payload_hash = canonical_sha256(law.to_data())
    issues: list[str] = []
    residuals: dict[str, object] = {}
    if law.root != law.classical_law.root or not law.root:
        issues.append("quantum-root-disconnected")
    classical_arrows = {arrow.identifier: arrow for arrow in law.classical_law.arrows}
    amplitude_index_raw, amplitude_issues = _unique_index(law.amplitude_arrows, "amplitude-arrow")
    amplitude_index = {
        key: value
        for key, value in amplitude_index_raw.items()
        if isinstance(value, AmplitudeArrow)
    }
    issues.extend(amplitude_issues)
    amplitude_rows: dict[str, object] = {}
    for arrow_id, arrow in sorted(amplitude_index.items()):
        classical_arrow = classical_arrows.get(arrow.classical_arrow_id)
        expected = (
            _g_scale(arrow.scale, _g_from_q(classical_arrow.matrix))
            if isinstance(classical_arrow, TypedArrow)
            else None
        )
        residual = (
            _g_residual(arrow.matrix, expected)
            if expected is not None
            else {"shape_match": False, "nonzero_count": None}
        )
        valid = bool(
            arrow.root == law.root
            and isinstance(classical_arrow, TypedArrow)
            and arrow.source_id == classical_arrow.source_id
            and arrow.target_id == classical_arrow.target_id
            and residual.get("nonzero_count") == 0
        )
        if not valid:
            issues.append(f"amplitude-derivation:{arrow_id}")
        amplitude_rows[arrow_id] = {
            "classical_arrow_id": arrow.classical_arrow_id,
            "scale": arrow.scale,
            "derivation_residual": residual,
            "valid": valid,
        }
    residuals["amplitude_arrows"] = amplitude_rows

    history_index_raw, history_issues = _unique_index(law.histories, "history")
    history_index = {
        key: value
        for key, value in history_index_raw.items()
        if isinstance(value, QuantumHistory)
    }
    issues.extend(history_issues)
    history_operators: dict[str, GMatrix] = {}
    history_rows: dict[str, object] = {}
    common_endpoints: set[tuple[str | None, str | None]] = set()
    for history_id, history in sorted(history_index.items()):
        operator, source, target, composable = _compose_amplitude_path(
            history.amplitude_arrow_ids, amplitude_index
        )
        valid = bool(history.root == law.root and composable and operator is not None)
        if not valid:
            issues.append(f"history-composition:{history_id}")
        if operator is not None:
            history_operators[history_id] = operator
        common_endpoints.add((source, target))
        history_rows[history_id] = {
            "arrow_ids": history.amplitude_arrow_ids,
            "source_id": source,
            "target_id": target,
            "operator": operator,
            "composable": composable,
            "valid": valid,
        }
    if not history_operators or len(common_endpoints) != 1:
        issues.append("typed-history-family")
    residuals["histories"] = history_rows

    state_positive, state_minors = _g_positive_semidefinite(law.input_state)
    state_trace = _g_trace(law.input_state) if law.input_state.nrows == law.input_state.ncols else GZERO
    state_valid = state_positive and state_trace == GONE
    if not state_valid:
        issues.append("positive-unit-input-state")
    residuals["input_state"] = {
        "principal_minors": state_minors,
        "trace": state_trace,
        "positive_unit_state": state_valid,
    }

    history_ids = tuple(history_index)
    gram: GMatrix | None = None
    gram_psd = False
    gram_minors: tuple[dict[str, object], ...] = ()
    gram_operator_identity: dict[str, object] = {"nonzero_count": None}
    gram_scalar_left = GZERO
    gram_scalar_right = GZERO
    universal_positive_operator: GMatrix | None = None
    universal_positive_minors: tuple[dict[str, object], ...] = ()
    universal_positive = False
    if (
        state_valid
        and history_ids
        and all(identifier in history_operators for identifier in history_ids)
    ):
        gram = GMatrix.from_rows(
            (
                (
                    _g_trace(
                        _g_multiply(
                            _g_multiply(history_operators[left], law.input_state),
                            _g_adjoint(history_operators[right]),
                        )
                    )
                    for right in history_ids
                )
                for left in history_ids
            ),
            ncols=len(history_ids),
        )
        gram_psd, gram_minors = _g_positive_semidefinite(gram)
        z = law.gram_test_coefficients
        if len(z) == len(history_ids):
            z_column = GMatrix.from_rows(((value,) for value in z), ncols=1)
            gram_scalar_left = _g_trace(
                _g_multiply(_g_adjoint(z_column), _g_multiply(gram, z_column))
            )
            abar = GMatrix.zero(
                next(iter(history_operators.values())).nrows,
                next(iter(history_operators.values())).ncols,
            )
            for coefficient, identifier in zip(z, history_ids):
                abar = _g_add(
                    abar,
                    _g_scale(coefficient.conjugate(), history_operators[identifier]),
                )
            gram_scalar_right = _g_trace(
                _g_multiply(
                    _g_multiply(abar, law.input_state), _g_adjoint(abar)
                )
            )
            universal_positive_operator = _g_multiply(_g_adjoint(abar), abar)
            universal_positive, universal_positive_minors = _g_positive_semidefinite(
                universal_positive_operator
            )
            gram_operator_identity = {
                "left_z_adjoint_D_z": gram_scalar_left,
                "right_trace_Abar_rho_Abar_adjoint": gram_scalar_right,
                "nonzero_count": 0 if gram_scalar_left == gram_scalar_right else 1,
                "Abar": abar,
                "Abar_adjoint_Abar": universal_positive_operator,
                "Abar_adjoint_Abar_principal_minors": universal_positive_minors,
                "positive_for_every_positive_input": universal_positive,
                "uses_conjugated_history_coefficients": True,
            }
    gram_valid = bool(
        gram is not None
        and gram_psd
        and gram_operator_identity.get("nonzero_count") == 0
        and universal_positive
    )
    if not gram_valid:
        issues.append("derived-strong-positive-history-gram")
    residuals["gram_operator_proof"] = {
        "derived_gram": gram,
        "principal_minors": gram_minors,
        "operator_identity": gram_operator_identity,
        "universal_positive_operator": universal_positive_operator,
        "universal_positive_principal_minors": universal_positive_minors,
        "strong_positivity_for_every_positive_input": universal_positive,
        "free_gram_ignored": law.opaque_free_gram is not None,
        "valid": gram_valid,
    }

    division_index_raw, division_issues = _unique_index(law.divisions, "division-port")
    division_index = {
        key: value
        for key, value in division_index_raw.items()
        if isinstance(value, DivisionPort)
    }
    issues.extend(division_issues)
    division_operators: dict[str, GMatrix] = {}
    division_rows: dict[str, object] = {}
    for division_id, division in sorted(division_index.items()):
        valid = bool(
            division.root == law.root
            and len(division.coefficients) == len(history_ids)
            and all(identifier in history_operators for identifier in history_ids)
        )
        operator: GMatrix | None = None
        if valid:
            prototype = next(iter(history_operators.values()))
            operator = GMatrix.zero(prototype.nrows, prototype.ncols)
            for coefficient, history_id in zip(division.coefficients, history_ids):
                operator = _g_add(
                    operator, _g_scale(coefficient, history_operators[history_id])
                )
            division_operators[division_id] = operator
        if not valid:
            issues.append(f"division-derivation:{division_id}")
        division_rows[division_id] = {
            "coefficients": division.coefficients,
            "derived_operator": operator,
            "valid": valid,
        }
    completeness: GMatrix | None = None
    completeness_residual: dict[str, object] = {"nonzero_count": None}
    dilation: GMatrix | None = None
    dilation_residual: dict[str, object] = {"nonzero_count": None}
    flag_projector_residuals: list[dict[str, object]] = []
    if division_operators:
        input_size = next(iter(division_operators.values())).ncols
        completeness = GMatrix.zero(input_size, input_size)
        for operator in division_operators.values():
            completeness = _g_add(
                completeness, _g_multiply(_g_adjoint(operator), operator)
            )
        completeness_residual = _g_residual(completeness, GMatrix.identity(input_size))
        dilation = _g_vstack(tuple(division_operators.values()))
        dilation_residual = _g_residual(
            _g_multiply(_g_adjoint(dilation), dilation), GMatrix.identity(input_size)
        )
        output_size = next(iter(division_operators.values())).nrows
        total_flagged_size = output_size * len(division_operators)
        projectors: list[GMatrix] = []
        for flag_index in range(len(division_operators)):
            projector = GMatrix.from_rows(
                (
                    (
                        GONE
                        if row == column
                        and row // output_size == flag_index
                        else GZERO
                        for column in range(total_flagged_size)
                    )
                    for row in range(total_flagged_size)
                ),
                ncols=total_flagged_size,
            )
            projectors.append(projector)
        for left_index, left in enumerate(projectors):
            for right_index, right in enumerate(projectors):
                expected = left if left_index == right_index else GMatrix.zero(
                    total_flagged_size, total_flagged_size
                )
                flag_projector_residuals.append(
                    {
                        "left": left_index,
                        "right": right_index,
                        "residual": _g_residual(_g_multiply(left, right), expected),
                    }
                )
    division_valid = bool(
        division_operators
        and completeness_residual.get("nonzero_count") == 0
        and dilation_residual.get("nonzero_count") == 0
        and all(
            row["residual"].get("nonzero_count") == 0
            for row in flag_projector_residuals
        )
    )
    if not division_valid:
        issues.append("unit-normalized-division-dilation-flags")
    residuals["division"] = {
        "ports": division_rows,
        "sum_L_adjoint_L": completeness,
        "completeness_residual": completeness_residual,
        "dilation_W": dilation,
        "dilation_isometry_residual": dilation_residual,
        "flag_projector_residuals": flag_projector_residuals,
        "valid": division_valid,
    }

    continuation_index_raw, continuation_issues = _unique_index(
        law.flag_continuations, "flag-continuation"
    )
    continuation_index = {
        key: value
        for key, value in continuation_index_raw.items()
        if isinstance(value, FlagContinuation)
    }
    issues.extend(continuation_issues)
    flag_size = len(division_operators)
    closure: dict[str, GMatrix] = {}
    for continuation_id, continuation in sorted(continuation_index.items()):
        continuation_typed = bool(
            continuation.root != law.root
            or continuation.matrix.shape != (flag_size, flag_size)
        )
        if continuation_typed:
            issues.append(f"flag-continuation-typing:{continuation_id}")
        else:
            closure[canonical_sha256(continuation.matrix)] = continuation.matrix
    changed = True
    while changed and len(closure) <= 64:
        changed = False
        for left in tuple(closure.values()):
            for right in tuple(closure.values()):
                product = _g_multiply(left, right)
                key = canonical_sha256(product)
                if key not in closure:
                    closure[key] = product
                    changed = True
    closure_complete = not changed
    nonidentity_continuation = any(
        value != GMatrix.identity(flag_size) for value in closure.values()
    ) if flag_size else False
    recovery_rows: list[dict[str, object]] = []
    recovery_valid = bool(
        closure and closure_complete and nonidentity_continuation
    )
    for word_hash, continuation in sorted(closure.items()):
        recovered: list[int] = []
        for flag in range(flag_size):
            column = tuple(continuation.data[row][flag] for row in range(flag_size))
            support = [index for index, value in enumerate(column) if not value.is_zero()]
            if len(support) == 1:
                recovered.append(support[0])
            else:
                recovered.append(-1)
        word_valid = recovered == list(range(flag_size))
        recovery_valid = recovery_valid and word_valid
        recovery_rows.append(
            {
                "word_sha256": word_hash,
                "matrix": continuation,
                "reader_outputs": tuple(recovered),
                "recovers_flag": word_valid,
            }
        )
    if not recovery_valid:
        issues.append("closed-nonidentity-flag-recovery")
    residuals["flag_recovery"] = {
        "closure_size": len(closure),
        "closure_complete": closure_complete,
        "nonidentity_word_present": nonidentity_continuation,
        "rows": recovery_rows,
        "valid": recovery_valid,
    }

    cut_rows: dict[str, object] = {}
    cuts_valid = bool(law.cuts)
    for cut in law.cuts:
        direct = history_operators.get(cut.history_id)
        alternate, source, target, composable = _compose_amplitude_path(
            cut.alternate_amplitude_arrow_ids, amplitude_index
        )
        residual = (
            _g_residual(direct, alternate)
            if direct is not None and alternate is not None
            else {"shape_match": False, "nonzero_count": None}
        )
        valid = bool(
            cut.root == law.root
            and composable
            and residual.get("nonzero_count") == 0
        )
        cuts_valid = cuts_valid and valid
        cut_rows[cut.identifier] = {
            "history_id": cut.history_id,
            "alternate_arrow_ids": cut.alternate_amplitude_arrow_ids,
            "source_id": source,
            "target_id": target,
            "residual": residual,
            "valid": valid,
        }
    if not cuts_valid:
        issues.append("coherent-cuts-from-same-arrows")
    residuals["coherent_cuts"] = {"rows": cut_rows, "valid": cuts_valid}

    coherent_probability = GZERO
    incoherent_probability = GZERO
    cross_operator: GMatrix | None = None
    interference_valid = False
    if division_operators and len(history_ids) >= 2 and state_valid:
        plus_operator = division_operators.get(
            "flag_plus", next(iter(division_operators.values()))
        )
        coherent_probability = _g_trace(
            _g_multiply(
                _g_multiply(plus_operator, law.input_state),
                _g_adjoint(plus_operator),
            )
        )
        incoherent_probability = sum(
            (
                _g_trace(
                    _g_multiply(
                        _g_multiply(history_operators[identifier], law.input_state),
                        _g_adjoint(history_operators[identifier]),
                    )
                )
                for identifier in history_ids
            ),
            GZERO,
        )
        first = history_operators[history_ids[0]]
        second = history_operators[history_ids[1]]
        cross_operator = _g_add(
            _g_multiply(_g_multiply(first, law.input_state), _g_adjoint(second)),
            _g_multiply(_g_multiply(second, law.input_state), _g_adjoint(first)),
        )
        interference_valid = bool(
            coherent_probability != incoherent_probability
            and _g_nonzero_count(cross_operator) > 0
        )
    if not interference_valid:
        issues.append("operational-interference")
    residuals["interference"] = {
        "coherent_probability": coherent_probability,
        "incoherent_history_sum": incoherent_probability,
        "probability_difference": coherent_probability - incoherent_probability,
        "cross_operator": cross_operator,
        "cross_operator_nonzero_count": (
            _g_nonzero_count(cross_operator) if cross_operator is not None else 0
        ),
        "valid": interference_valid,
    }

    phase_adjoint_residual = _g_residual(
        _g_multiply(_g_adjoint(law.phase_control), law.phase_control),
        GMatrix.identity(law.phase_control.ncols),
    )
    phase_transpose_residual = _g_residual(
        _g_multiply(_g_transpose(law.phase_control), law.phase_control),
        GMatrix.identity(law.phase_control.ncols),
    )
    phase_valid = bool(
        phase_adjoint_residual.get("nonzero_count") == 0
        and isinstance(phase_transpose_residual.get("nonzero_count"), int)
        and phase_transpose_residual["nonzero_count"] > 0
    )
    if not phase_valid:
        issues.append("conjugate-transpose-phase-control")
    residuals["phase_conjugation_control"] = {
        "P": law.phase_control,
        "P_adjoint_P_residual": phase_adjoint_residual,
        "P_transpose_P_residual": phase_transpose_residual,
        "valid": phase_valid,
    }

    consumed_ids = tuple(
        sorted(
            set(classical.consumed_primitive_ids)
            | {law.identifier}
            | set(amplitude_index)
            | set(history_index)
            | set(division_index)
            | {cut.identifier for cut in law.cuts}
            | set(continuation_index)
        )
    )
    valid = classical.valid and not issues
    return QuantumLawMeasurement(
        primitive_payload_sha256=payload_hash,
        consumed_primitive_ids=consumed_ids,
        coordinate=(
            "HORIZONTAL-QUANTUM"
            if valid
            else "HORIZONTAL-CLASSICAL"
            if classical.valid
            else "STATIC-RESPONSE-ONLY"
        ),
        valid=valid,
        classical=classical,
        residuals=residuals,
        issues=tuple(sorted(set(issues))),
    )


def build_quantum_existence_law(fault: str | None = None) -> QuantumPrimitiveLaw:
    classical = build_classical_existence_law()
    root = classical.root
    classical_arrows = {arrow.identifier: arrow for arrow in classical.arrows}
    half = GaussianRational(Fraction(1, 2))
    amp_i = AmplitudeArrow(
        root,
        "amp_I_half",
        "A",
        "A",
        "id_A",
        half,
        _g_scale(half, _g_from_q(classical_arrows["id_A"].matrix)),
    )
    x_scale = GaussianRational(0) if fault == "zero-cross" else half
    amp_x_root = "v4:other-root" if fault == "different-root-history" else root
    amp_x_source = "C" if fault == "different-frontier-history" else "A"
    amp_x = AmplitudeArrow(
        amp_x_root,
        "amp_X_half",
        amp_x_source,
        "A",
        "x_A",
        x_scale,
        _g_scale(x_scale, _g_from_q(classical_arrows["x_A"].matrix)),
    )
    amp_id = AmplitudeArrow(
        root,
        "amp_identity",
        "A",
        "A",
        "id_A",
        GaussianRational(1),
        _g_from_q(classical_arrows["id_A"].matrix),
    )
    histories = (
        QuantumHistory(root, "history_I", ("amp_I_half",)),
        QuantumHistory(root, "history_X", ("amp_X_half",)),
    )
    if fault == "free-gram-no-histories":
        histories = ()
    divisions = (
        DivisionPort(root, "flag_plus", (GONE, GONE)),
        DivisionPort(root, "flag_minus", (GONE, GaussianRational(-1))),
    )
    if fault == "total-2I":
        divisions = divisions + (
            DivisionPort(root, "flag_plus_2", (GONE, GONE)),
            DivisionPort(root, "flag_minus_2", (GONE, GaussianRational(-1))),
        )
    elif fault in {"nonunit-total", "missing-flags"}:
        divisions = divisions[:1] if fault == "nonunit-total" else ()
    cuts = (
        QuantumCut(root, "cut_I", "history_I", ("amp_I_half", "amp_identity")),
        QuantumCut(root, "cut_X", "history_X", ("amp_X_half", "amp_identity")),
    )
    if fault == "different-cut-arrows":
        cuts = (
            QuantumCut(root, "cut_I", "history_I", ("amp_X_half", "amp_identity")),
            cuts[1],
        )
    elif fault == "arbitrary-equal-payload":
        cuts = ()
    rho_plus = GMatrix.from_rows(
        (
            (GaussianRational(Fraction(1, 2)), GaussianRational(Fraction(1, 2))),
            (GaussianRational(Fraction(1, 2)), GaussianRational(Fraction(1, 2))),
        )
    )
    if fault == "nonpositive-state":
        rho_plus = GMatrix.from_rows(((2, 0), (0, -1)))
    elif fault == "no-probability-difference":
        rho_plus = GMatrix.from_rows(((Fraction(1, 2), 0), (0, Fraction(1, 2))))
    continuation_root = "v4:other-root" if fault == "disconnected-recovery" else root
    continuations = (
        FlagContinuation(continuation_root, "flag_I", GMatrix.identity(2)),
        FlagContinuation(
            continuation_root,
            "flag_Z",
            GMatrix.from_rows(((1, 0), (0, -1))),
        ),
    )
    if fault == "no-nonidentity-continuation":
        continuations = continuations[:1]
    elif fault == "nonclosed-continuation-semigroup":
        continuations = (
            continuations[0],
            FlagContinuation(
                root,
                "flag-nonclosed-scaling",
                GMatrix.from_rows(((1, 0), (0, Fraction(1, 2)))),
            ),
        )
    elif fault == "arbitrary-equal-payload":
        continuations = ()
    phase = (
        GMatrix.identity(2)
        if fault == "transpose-phase-control"
        else GMatrix.from_rows(((GONE, GZERO), (GZERO, GI)))
    )
    negative_free_gram = GMatrix.from_rows(((1, 2), (2, 1)))
    return QuantumPrimitiveLaw(
        root=root,
        identifier="quantum_existence_law",
        classical_law=classical,
        amplitude_arrows=(amp_i, amp_x, amp_id),
        histories=histories,
        divisions=divisions,
        cuts=cuts,
        input_state=rho_plus,
        flag_continuations=continuations,
        phase_control=phase,
        gram_test_coefficients=(GONE, GI),
        opaque_free_gram=(
            negative_free_gram
            if fault in {"negative-free-gram", "free-gram-no-histories"}
            else None
        ),
        opaque_recovery_payload=(
            (("lhs", "same"), ("rhs", "same"))
            if fault == "arbitrary-equal-payload"
            else ()
        ),
    )


@dataclass(frozen=True, slots=True)
class CarrierPrimitive:
    root: str
    identifier: str
    states: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {"root": self.root, "id": self.identifier, "states": self.states}


@dataclass(frozen=True, slots=True)
class ProductCarrierPrimitive:
    root: str
    identifier: str
    source_states: tuple[str, ...]
    target_states: tuple[str, ...]
    states: tuple[str, ...]
    source_factor_id: str = "source-factor"
    target_factor_id: str = "target-factor"

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_states": self.source_states,
            "target_states": self.target_states,
            "states": self.states,
            "source_factor_id": self.source_factor_id,
            "target_factor_id": self.target_factor_id,
            "ordering": "left-major-lexicographic",
        }


@dataclass(frozen=True, slots=True)
class ScheduledTransitionPrimitive:
    root: str
    identifier: str
    source_carrier_id: str
    target_carrier_id: str
    matrix: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_carrier_id": self.source_carrier_id,
            "target_carrier_id": self.target_carrier_id,
            "matrix": self.matrix,
        }


@dataclass(frozen=True, slots=True)
class InterventionAlternativePrimitive:
    root: str
    identifier: str
    carrier_id: str
    matrix: QMatrix
    source_factor_matrix: QMatrix | None = None

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
            "matrix": self.matrix,
            "source_factor_matrix": self.source_factor_matrix,
        }


@dataclass(frozen=True, slots=True)
class InterventionPrimitive:
    root: str
    identifier: str
    carrier_id: str
    slot: int
    alternatives: tuple[InterventionAlternativePrimitive, ...]
    registered_alternative_ids: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
            "slot": self.slot,
            "alternatives": self.alternatives,
            "registered_alternative_ids": self.registered_alternative_ids,
        }


@dataclass(frozen=True, slots=True)
class ReaderPrimitive:
    root: str
    identifier: str
    carrier_id: str
    outcomes: tuple[str, ...]
    matrix: QMatrix
    schedule_position: int

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
            "outcomes": self.outcomes,
            "matrix": self.matrix,
            "schedule_position": self.schedule_position,
        }


@dataclass(frozen=True, slots=True)
class InfluencePrimitiveLaw:
    root: str
    identifier: str
    carrier: CarrierPrimitive
    initial_state: QMatrix
    pre_schedule: tuple[ScheduledTransitionPrimitive, ...]
    intervention: InterventionPrimitive
    post_schedule: tuple[ScheduledTransitionPrimitive, ...]
    reader: ReaderPrimitive
    product_carrier: ProductCarrierPrimitive | None = None
    contact_required: bool = False
    opaque_before_after: tuple[tuple[str, tuple[Fraction, ...]], ...] = ()
    opaque_provenance: tuple[tuple[str, str, str], ...] = ()
    transition_reference_id: str | None = "shared-transition-X"

    def to_data(self) -> dict[str, object]:
        return {
            "type": "InfluencePrimitiveLaw",
            "root": self.root,
            "id": self.identifier,
            "carrier": self.carrier,
            "initial_state": self.initial_state,
            "pre_schedule": self.pre_schedule,
            "intervention": self.intervention,
            "post_schedule": self.post_schedule,
            "reader": self.reader,
            "product_carrier": self.product_carrier,
            "contact_required": self.contact_required,
            "opaque_before_after": self.opaque_before_after,
            "opaque_provenance": self.opaque_provenance,
            "transition_reference_id": self.transition_reference_id,
        }


@dataclass(frozen=True, slots=True)
class InfluenceLawMeasurement:
    primitive_payload_sha256: str
    consumed_primitive_ids: tuple[str, ...]
    role: str
    present: bool
    responses: tuple[tuple[str, QMatrix], ...]
    residuals: Mapping[str, object]
    issues: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "InfluenceLawMeasurement",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "consumed_primitive_ids": self.consumed_primitive_ids,
            "role": self.role,
            "present": self.present,
            "responses": self.responses,
            "residuals": self.residuals,
            "missing": self.issues,
            "issues": self.issues,
        }


def _stochastic_matrix_measurement(
    value: QMatrix, *, expected_shape: tuple[int, int]
) -> dict[str, object]:
    shape_valid = value.shape == expected_shape
    negative_count = sum(item < 0 for row in value.data for item in row)
    column_residual = _q_column_residual(value) if value.ncols else ()
    return {
        "expected_shape": expected_shape,
        "actual_shape": value.shape,
        "shape_residual": 0 if shape_valid else 1,
        "negative_entry_count": negative_count,
        "column_sum_residual": column_residual,
        "valid": shape_valid
        and negative_count == 0
        and all(item == 0 for item in column_residual),
    }


def _compose_q_schedule(
    initial: QMatrix,
    carrier_id: str,
    schedule: Sequence[ScheduledTransitionPrimitive],
    *,
    root: str,
    carrier_sizes: Mapping[str, int],
) -> tuple[QMatrix | None, str, tuple[dict[str, object], ...], bool]:
    state = initial
    active_carrier = carrier_id
    rows: list[dict[str, object]] = []
    valid = True
    for transition in schedule:
        source_size = carrier_sizes.get(transition.source_carrier_id)
        target_size = carrier_sizes.get(transition.target_carrier_id)
        stochastic = (
            _stochastic_matrix_measurement(
                transition.matrix,
                expected_shape=(target_size, source_size),
            )
            if source_size is not None and target_size is not None
            else {"valid": False, "shape_residual": 1}
        )
        typed = bool(
            transition.root == root
            and transition.source_carrier_id == active_carrier
            and stochastic["valid"]
        )
        row: dict[str, object] = {
            "transition_id": transition.identifier,
            "input_carrier_id": active_carrier,
            "declared_source_carrier_id": transition.source_carrier_id,
            "declared_target_carrier_id": transition.target_carrier_id,
            "stochastic": stochastic,
            "composable": typed,
        }
        if typed:
            try:
                state = qmultiply(transition.matrix, state)
                active_carrier = transition.target_carrier_id
                row["output_state"] = state
            except ValueError:
                typed = False
                row["composable"] = False
        valid = valid and typed
        rows.append(row)
    return (state if valid else None), active_carrier, tuple(rows), valid


def _source_reader_matrix(source_size: int, target_size: int) -> QMatrix:
    return QMatrix.from_rows(
        (
            (
                Fraction(1) if source == output else Fraction(0)
                for source in range(source_size)
                for _target in range(target_size)
            )
            for output in range(source_size)
        ),
        ncols=source_size * target_size,
    )


def _target_reader_matrix(source_size: int, target_size: int) -> QMatrix:
    return QMatrix.from_rows(
        (
            (
                Fraction(1) if target == output else Fraction(0)
                for _source in range(source_size)
                for target in range(target_size)
            )
            for output in range(target_size)
        ),
        ncols=source_size * target_size,
    )


def measure_influence_primitive_law(law: object) -> InfluenceLawMeasurement:
    if not isinstance(law, InfluencePrimitiveLaw):
        raise ScoreRefusal("influence promotion requires InfluencePrimitiveLaw")
    payload_hash = canonical_sha256(law.to_data())
    role = "generated_contact" if law.contact_required else "causal_order"
    issues: list[str] = []
    residuals: dict[str, object] = {}
    carrier = law.carrier
    carrier_valid = bool(
        carrier.root == law.root
        and carrier.states
        and len(set(carrier.states)) == len(carrier.states)
    )
    if not carrier_valid:
        issues.append("typed-carrier")
    carrier_sizes: dict[str, int] = {carrier.identifier: len(carrier.states)}
    product = law.product_carrier
    product_valid = not law.contact_required
    if product is not None:
        expected_states = tuple(
            f"({source},{target})"
            for source in product.source_states
            for target in product.target_states
        )
        product_valid = bool(
            product.root == law.root
            and product.identifier == carrier.identifier
            and product.source_states
            and product.target_states
            and len(set(product.source_states)) == len(product.source_states)
            and len(set(product.target_states)) == len(product.target_states)
            and bool(product.source_factor_id)
            and bool(product.target_factor_id)
            and product.source_factor_id != product.target_factor_id
            and product.states == expected_states
            and carrier.states == expected_states
        )
        carrier_sizes[product.identifier] = len(product.states)
    if law.contact_required and not product_valid:
        issues.append("typed-disjoint-product-carrier")
    residuals["carrier"] = {
        "carrier_valid": carrier_valid,
        "product_required": law.contact_required,
        "product_valid": product_valid,
        "source_factor_nonempty": bool(product and product.source_states),
        "target_factor_nonempty": bool(product and product.target_states),
        "source_factor_id": product.source_factor_id if product else None,
        "target_factor_id": product.target_factor_id if product else None,
        "factor_roles_distinct": bool(
            product
            and product.source_states
            and product.target_states
            and product.source_factor_id != product.target_factor_id
        ),
        "ordering": "left-major-lexicographic",
    }

    initial_measurement = _stochastic_matrix_measurement(
        law.initial_state, expected_shape=(len(carrier.states), 1)
    )
    if not initial_measurement["valid"]:
        issues.append("normalized-initial-state")
    pre_state, pre_carrier, pre_rows, pre_valid = _compose_q_schedule(
        law.initial_state,
        carrier.identifier,
        law.pre_schedule,
        root=law.root,
        carrier_sizes=carrier_sizes,
    )
    if not pre_valid:
        issues.append("typed-before-schedule")
    residuals["initial_and_before_schedule"] = {
        "initial": initial_measurement,
        "operations": pre_rows,
        "output_carrier_id": pre_carrier,
    }

    intervention = law.intervention
    alternatives = intervention.alternatives
    alternative_ids = tuple(row.identifier for row in alternatives)
    registered_exact = bool(
        len(alternatives) >= 2
        and len(set(alternative_ids)) == len(alternative_ids)
        and intervention.registered_alternative_ids == alternative_ids
    )
    intervention_typed = bool(
        pre_state is not None
        and intervention.root == law.root
        and intervention.carrier_id == pre_carrier
        and intervention.slot == len(law.pre_schedule)
        and registered_exact
    )
    alternative_rows: dict[str, object] = {}
    local_source_matrices: list[QMatrix] = []
    for alternative in alternatives:
        stochastic = _stochastic_matrix_measurement(
            alternative.matrix,
            expected_shape=(len(carrier.states), len(carrier.states)),
        )
        typed = bool(
            alternative.root == law.root
            and alternative.carrier_id == carrier.identifier
            and stochastic["valid"]
        )
        locality_residual: dict[str, object] | None = None
        local = not law.contact_required
        if law.contact_required and product is not None:
            factor = alternative.source_factor_matrix
            factor_measurement = (
                _stochastic_matrix_measurement(
                    factor,
                    expected_shape=(
                        len(product.source_states), len(product.source_states)
                    ),
                )
                if isinstance(factor, QMatrix)
                else {"valid": False}
            )
            expected_local = (
                _q_kron(factor, QMatrix.identity(len(product.target_states)))
                if isinstance(factor, QMatrix) and factor_measurement["valid"]
                else None
            )
            locality_residual = (
                _q_residual(alternative.matrix, expected_local)
                if expected_local is not None
                else {"shape_match": False, "nonzero_count": None}
            )
            local = bool(
                factor_measurement["valid"]
                and locality_residual.get("nonzero_count") == 0
            )
            if isinstance(factor, QMatrix):
                local_source_matrices.append(factor)
        typed = typed and local
        intervention_typed = intervention_typed and typed
        alternative_rows[alternative.identifier] = {
            "stochastic": stochastic,
            "source_local_factorization_residual": locality_residual,
            "source_local": local,
            "valid": typed,
        }
    distinct_alternatives = any(
        left.matrix != right.matrix
        for left, right in itertools.combinations(alternatives, 2)
    )
    if not intervention_typed or not distinct_alternatives:
        issues.append("distinct-used-typed-interventions")
    residuals["intervention"] = {
        "slot": intervention.slot,
        "expected_slot": len(law.pre_schedule),
        "registered_alternative_ids": intervention.registered_alternative_ids,
        "actual_alternative_ids": alternative_ids,
        "registered_exactly": registered_exact,
        "alternatives_distinct": distinct_alternatives,
        "rows": alternative_rows,
        "valid": intervention_typed and distinct_alternatives,
    }

    response_rows: list[tuple[str, QMatrix]] = []
    path_rows: dict[str, object] = {}
    all_paths_valid = intervention_typed and pre_state is not None
    for alternative in alternatives:
        if pre_state is None:
            all_paths_valid = False
            continue
        try:
            intervened = qmultiply(alternative.matrix, pre_state)
        except ValueError:
            all_paths_valid = False
            continue
        post_state, post_carrier, post_rows, post_valid = _compose_q_schedule(
            intervened,
            alternative.carrier_id,
            law.post_schedule,
            root=law.root,
            carrier_sizes=carrier_sizes,
        )
        reader_measurement = _stochastic_matrix_measurement(
            law.reader.matrix,
            expected_shape=(len(law.reader.outcomes), len(carrier.states)),
        )
        reader_after = law.reader.schedule_position == (
            len(law.pre_schedule) + 1 + len(law.post_schedule)
        )
        reader_typed = bool(
            post_state is not None
            and law.reader.root == law.root
            and law.reader.carrier_id == post_carrier
            and law.reader.outcomes
            and len(set(law.reader.outcomes)) == len(law.reader.outcomes)
            and reader_measurement["valid"]
            and reader_after
        )
        response: QMatrix | None = None
        if reader_typed and post_state is not None:
            try:
                response = qmultiply(law.reader.matrix, post_state)
            except ValueError:
                reader_typed = False
        path_valid = post_valid and reader_typed and response is not None
        all_paths_valid = all_paths_valid and path_valid
        if response is not None:
            response_rows.append((alternative.identifier, response))
        path_rows[alternative.identifier] = {
            "intervened_state": intervened,
            "post_schedule": post_rows,
            "post_carrier_id": post_carrier,
            "reader_stochastic": reader_measurement,
            "reader_after_intervention": reader_after,
            "derived_response": response,
            "valid": path_valid,
        }
    changed_response = any(
        left[1] != right[1] for left, right in itertools.combinations(response_rows, 2)
    )
    if not all_paths_valid or not changed_response:
        issues.append("derived-delayed-response")
    residuals["derived_response_paths"] = {
        "rows": path_rows,
        "changed_response": changed_response,
        "opaque_before_after_ignored": bool(law.opaque_before_after),
        "valid": all_paths_valid and changed_response,
    }

    contact_valid = not law.contact_required
    if law.contact_required and product is not None:
        expected_reader = _target_reader_matrix(
            len(product.source_states), len(product.target_states)
        )
        target_reader_residual = _q_residual(law.reader.matrix, expected_reader)
        post_nonidentity = bool(
            law.post_schedule
            and any(
                transition.matrix
                != QMatrix.identity(transition.matrix.nrows)
                for transition in law.post_schedule
                if transition.matrix.nrows == transition.matrix.ncols
            )
        )
        target_changes = False
        if len(response_rows) >= 2:
            target_changes = response_rows[0][1] != response_rows[1][1]
        contact_valid = bool(
            product_valid
            and intervention_typed
            and len(local_source_matrices) == len(alternatives)
            and target_reader_residual.get("nonzero_count") == 0
            and post_nonidentity
            and target_changes
        )
        residuals["generated_contact"] = {
            "source_local_interventions": len(local_source_matrices)
            == len(alternatives),
            "target_reader_factorization_residual": target_reader_residual,
            "nonidentity_propagation": post_nonidentity,
            "derived_target_response_changes": target_changes,
            "valid": contact_valid,
        }
        if not contact_valid:
            issues.append("generated-contact-factor-chain")
    else:
        residuals["generated_contact"] = {
            "required": False,
            "causal_order_not_aliased_to_contact": True,
        }

    consumed_ids = tuple(
        sorted(
            {
                law.identifier,
                carrier.identifier,
                intervention.identifier,
                law.reader.identifier,
                *(row.identifier for row in law.pre_schedule),
                *(row.identifier for row in law.post_schedule),
                *(row.identifier for row in alternatives),
                *((product.identifier,) if product is not None else ()),
                *((law.transition_reference_id,) if law.transition_reference_id else ()),
            }
        )
    )
    present = bool(
        carrier_valid
        and product_valid
        and initial_measurement["valid"]
        and pre_valid
        and intervention_typed
        and distinct_alternatives
        and all_paths_valid
        and changed_response
        and contact_valid
        and not issues
    )
    residuals["computed_chain_provenance"] = {
        "primitive_ids": consumed_ids,
        "opaque_provenance_ignored": bool(law.opaque_provenance),
        "chain_connected_by_typed_composition": present,
    }
    return InfluenceLawMeasurement(
        primitive_payload_sha256=payload_hash,
        consumed_primitive_ids=consumed_ids,
        role=role,
        present=present,
        responses=tuple(response_rows),
        residuals=residuals,
        issues=tuple(sorted(set(issues))),
    )


def _cnot_matrix() -> QMatrix:
    return _q_permutation_from_images((0, 1, 3, 2))


def build_influence_existence_law(
    *, contact: bool, fault: str | None = None
) -> InfluencePrimitiveLaw:
    root = V4_INTERNAL_ROOT
    zero_reset = QMatrix.from_rows(((1, 1), (0, 0)))
    one_reset = QMatrix.from_rows(((0, 0), (1, 1)))
    if not contact:
        carrier = CarrierPrimitive(root, "system", ("0", "1"))
        alternative_matrices = (zero_reset, one_reset)
        if fault == "identical-alternatives":
            alternative_matrices = (zero_reset, zero_reset)
        alternatives = tuple(
            InterventionAlternativePrimitive(
                root,
                f"reset_{index}",
                carrier.identifier,
                matrix,
            )
            for index, matrix in enumerate(alternative_matrices)
        )
        registered = tuple(row.identifier for row in alternatives)
        if fault == "unused-alternative":
            registered = registered[:1]
        intervention = InterventionPrimitive(
            root,
            "reset-slot",
            carrier.identifier,
            0,
            alternatives,
            registered,
        )
        continuation_root = "v4:disconnected" if fault == "disconnected-root" else root
        continuation = ScheduledTransitionPrimitive(
            continuation_root,
            "identity-continuation",
            carrier.identifier,
            carrier.identifier,
            QMatrix.identity(2),
        )
        if fault == "noncomposable-carrier":
            continuation = ScheduledTransitionPrimitive(
                root,
                "identity-continuation",
                "alien-carrier",
                carrier.identifier,
                QMatrix.identity(2),
            )
        reader_position = 0 if fault in {"reader-before", "supplied-tables"} else 2
        reader = ReaderPrimitive(
            root,
            "later-bit-reader",
            carrier.identifier,
            ("0", "1"),
            QMatrix.identity(2),
            reader_position,
        )
        causal_post_schedule = () if fault == "provenance-only" else (continuation,)
        return InfluencePrimitiveLaw(
            root=root,
            identifier="causal-existence-law",
            carrier=carrier,
            initial_state=QMatrix.from_rows(((1,), (0,))),
            pre_schedule=(),
            intervention=intervention,
            post_schedule=causal_post_schedule,
            reader=reader,
            opaque_before_after=(
                ("before", (Fraction(1), Fraction(0))),
                ("after", (Fraction(0), Fraction(1))),
            )
            if fault in {"supplied-tables", "reader-before"}
            else (),
            opaque_provenance=(
                ("root", "claim", "asserts"),
            )
            if fault == "provenance-only"
            else (),
        )

    source_states = ("0", "1")
    target_states = ("0", "1")
    product_states = tuple(
        f"({source},{target})" for source in source_states for target in target_states
    )
    if fault == "overlapping-or-labeled-supports":
        product_states = ("source", "target", "both", "labeled")
    product = ProductCarrierPrimitive(
        root,
        "source_x_target",
        source_states,
        target_states,
        product_states,
        source_factor_id="same-labeled-factor"
        if fault == "overlapping-or-labeled-supports"
        else "source-factor",
        target_factor_id="same-labeled-factor"
        if fault == "overlapping-or-labeled-supports"
        else "target-factor",
    )
    carrier = CarrierPrimitive(root, product.identifier, product_states)
    local_matrices = (
        _q_kron(zero_reset, QMatrix.identity(2)),
        _q_kron(one_reset, QMatrix.identity(2)),
    )
    if fault == "identical-alternatives":
        local_matrices = (local_matrices[0], local_matrices[0])
    if fault == "target-acting-intervention":
        local_matrices = (
            _q_kron(zero_reset, QMatrix.identity(2)),
            _q_kron(one_reset, QMatrix.from_rows(((0, 1), (1, 0)))),
        )
    alternatives = tuple(
        InterventionAlternativePrimitive(
            root,
            f"source_reset_{index}",
            carrier.identifier,
            matrix,
            (zero_reset, one_reset)[index],
        )
        for index, matrix in enumerate(local_matrices)
    )
    registered = tuple(row.identifier for row in alternatives)
    if fault == "unused-alternative":
        registered = registered[:1]
    intervention = InterventionPrimitive(
        root,
        "source-reset-slot",
        carrier.identifier,
        0,
        alternatives,
        registered,
    )
    propagation_matrix = (
        QMatrix.identity(4) if fault == "identity-propagation" else _cnot_matrix()
    )
    propagation_root = "v4:disconnected" if fault == "disconnected-root" else root
    propagation_source = (
        "alien-product" if fault == "noncomposable-carrier" else carrier.identifier
    )
    propagation = ScheduledTransitionPrimitive(
        propagation_root,
        "cnot-source-to-target",
        propagation_source,
        carrier.identifier,
        propagation_matrix,
    )
    reader_matrix = (
        _source_reader_matrix(2, 2)
        if fault == "source-consuming-reader"
        else _target_reader_matrix(2, 2)
    )
    reader = ReaderPrimitive(
        root,
        "target-reader",
        carrier.identifier,
        ("0", "1"),
        reader_matrix,
        0 if fault in {"reader-before", "supplied-tables"} else 2,
    )
    post_schedule = () if fault == "provenance-only" else (propagation,)
    return InfluencePrimitiveLaw(
        root=root,
        identifier="contact-existence-law",
        carrier=carrier,
        initial_state=QMatrix.from_rows(((1,), (0,), (0,), (0,))),
        pre_schedule=(),
        intervention=intervention,
        post_schedule=post_schedule,
        reader=reader,
        product_carrier=product,
        contact_required=True,
        opaque_before_after=(
            ("reset_0", (Fraction(1), Fraction(0))),
            ("reset_1", (Fraction(0), Fraction(1))),
        )
        if fault in {"identity-propagation", "supplied-tables", "reader-before"}
        else (),
        opaque_provenance=(
            ("source", "target", "asserted-contact"),
        )
        if fault == "provenance-only"
        else (),
    )


@dataclass(frozen=True, slots=True)
class RecordWriterPrimitive:
    root: str
    identifier: str
    source_carrier: CarrierPrimitive
    target_carrier: ProductCarrierPrimitive
    matrix: QMatrix
    semantic_label: str = "writer"

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_carrier": self.source_carrier,
            "target_carrier": self.target_carrier,
            "matrix": self.matrix,
            "semantic_label": self.semantic_label,
        }


@dataclass(frozen=True, slots=True)
class RewritePrimitive:
    root: str
    identifier: str
    source_carrier: CarrierPrimitive
    target_carrier: CarrierPrimitive
    source_region_id: str
    target_region_id: str
    created_support_state: str
    matrix: QMatrix
    passive_inclusion: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_carrier": self.source_carrier,
            "target_carrier": self.target_carrier,
            "source_region_id": self.source_region_id,
            "target_region_id": self.target_region_id,
            "created_support_state": self.created_support_state,
            "matrix": self.matrix,
            "passive_inclusion": self.passive_inclusion,
        }


@dataclass(frozen=True, slots=True)
class OntologyPrimitiveLaw:
    root: str
    identifier: str
    classical_law: ClassicalPrimitiveLaw | None
    conditioning_instrument_id: str | None
    writer: RecordWriterPrimitive | None
    delayed_flag_reader: ReaderPrimitive | None
    record_continuations: tuple[ScheduledTransitionPrimitive, ...]
    rewrite: RewritePrimitive | None
    rewrite_input_state: QMatrix | None
    compiler_mode: str
    ontology_candidate: str | None = None
    opaque_role_tables: tuple[tuple[str, str], ...] = ()

    def to_data(self) -> dict[str, object]:
        return {
            "type": "OntologyPrimitiveLaw",
            "root": self.root,
            "id": self.identifier,
            "classical_law": self.classical_law,
            "conditioning_instrument_id": self.conditioning_instrument_id,
            "writer": self.writer,
            "delayed_flag_reader": self.delayed_flag_reader,
            "record_continuations": self.record_continuations,
            "rewrite": self.rewrite,
            "rewrite_input_state": self.rewrite_input_state,
            "compiler_mode": self.compiler_mode,
            "ontology_candidate": self.ontology_candidate,
            "opaque_role_tables": self.opaque_role_tables,
        }


@dataclass(frozen=True, slots=True)
class OntologyLawMeasurement:
    primitive_payload_sha256: str
    consumed_primitive_ids: tuple[str, ...]
    role: str
    residuals: Mapping[str, object]
    issues: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "OntologyLawMeasurement",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "consumed_primitive_ids": self.consumed_primitive_ids,
            "role": self.role,
            "residuals": self.residuals,
            "issues": self.issues,
            "candidate_consulted": False,
        }


def _compile_carrier_state_effect(
    compiler_mode: str, carrier: CarrierPrimitive, state: str
) -> QMatrix | None:
    if compiler_mode != "target-independent-uniform" or state not in carrier.states:
        return None
    index = carrier.states.index(state)
    return QMatrix.from_rows(
        (
            tuple(
                Fraction(1) if column == index else Fraction(0)
                for column in range(len(carrier.states))
            ),
        ),
        ncols=len(carrier.states),
    )


def measure_ontology_primitive_law(law: object) -> OntologyLawMeasurement:
    if not isinstance(law, OntologyPrimitiveLaw):
        raise ScoreRefusal("ontology promotion requires OntologyPrimitiveLaw")
    payload_hash = canonical_sha256(law.to_data())
    residuals: dict[str, object] = {
        "static_response": {
            "present": True,
            "source": "generic-static-baseline-control",
        }
    }
    issues: list[str] = []
    consumed_ids: set[str] = {law.identifier}
    conditioning_valid = False
    classical_measurement: ClassicalLawMeasurement | None = None
    instrument: TypedInstrument | None = None
    if isinstance(law.classical_law, ClassicalPrimitiveLaw):
        classical_measurement = measure_classical_primitive_law(law.classical_law)
        consumed_ids.update(classical_measurement.consumed_primitive_ids)
        instrument = next(
            (
                row
                for row in law.classical_law.instruments
                if row.identifier == law.conditioning_instrument_id
            ),
            None,
        )
        instrument_measurement = (
            classical_measurement.residuals.get("instruments", {}).get(
                instrument.identifier
            )
            if isinstance(instrument, TypedInstrument)
            and isinstance(classical_measurement.residuals.get("instruments"), Mapping)
            else None
        )
        branches_subnormalized = bool(
            isinstance(instrument_measurement, Mapping)
            and instrument_measurement.get("individual_branches_subnormalized")
            and all(instrument_measurement["individual_branches_subnormalized"])
        )
        conditioning_valid = bool(
            classical_measurement.valid
            and isinstance(instrument, TypedInstrument)
            and isinstance(instrument_measurement, Mapping)
            and instrument_measurement.get("valid")
            and branches_subnormalized
        )
        if isinstance(instrument, TypedInstrument):
            consumed_ids.add(instrument.identifier)
        residuals["conditioning"] = {
            "classical_coordinate": classical_measurement.coordinate,
            "instrument_id": law.conditioning_instrument_id,
            "derived_instrument_measurement": instrument_measurement,
            "individual_selected_branch_is_subnormalized": branches_subnormalized,
            "same_fixed_algebra": bool(
                isinstance(instrument, TypedInstrument)
                and instrument.source_id == instrument.target_id
            ),
            "valid": conditioning_valid,
        }
    else:
        residuals["conditioning"] = {
            "instrument_id": law.conditioning_instrument_id,
            "valid": False,
        }

    record_valid = False
    writer = law.writer
    reader = law.delayed_flag_reader
    if conditioning_valid and isinstance(writer, RecordWriterPrimitive):
        consumed_ids.add(writer.identifier)
        source = writer.source_carrier
        target = writer.target_carrier
        expected_target_states = tuple(
            f"({state},{flag})"
            for state in target.source_states
            for flag in target.target_states
        )
        carriers_valid = bool(
            writer.root == law.root
            and source.root == law.root
            and target.root == law.root
            and target.source_states == source.states
            and target.target_states == source.states
            and target.states == expected_target_states
        )
        expected_writer = QMatrix.from_rows(
            (
                (
                    Fraction(1)
                    if row == column * len(source.states) + column
                    else Fraction(0)
                    for column in range(len(source.states))
                )
                for row in range(len(target.states))
            ),
            ncols=len(source.states),
        )
        writer_residual = _q_residual(writer.matrix, expected_writer)
        writer_stochastic = _stochastic_matrix_measurement(
            writer.matrix,
            expected_shape=(len(target.states), len(source.states)),
        )
        expected_reader = _target_reader_matrix(
            len(target.source_states), len(target.target_states)
        )
        reader_residual = (
            _q_residual(reader.matrix, expected_reader)
            if isinstance(reader, ReaderPrimitive)
            else {"shape_match": False, "nonzero_count": None}
        )
        reader_valid = bool(
            isinstance(reader, ReaderPrimitive)
            and reader.root == law.root
            and reader.carrier_id == target.identifier
            and reader.schedule_position == 2
            and reader.outcomes == source.states
            and reader_residual.get("nonzero_count") == 0
        )
        if isinstance(reader, ReaderPrimitive):
            consumed_ids.add(reader.identifier)

        continuation_index_raw, continuation_issues = _unique_index(
            law.record_continuations, "ontology-continuation"
        )
        issues.extend(continuation_issues)
        continuation_index = {
            key: value
            for key, value in continuation_index_raw.items()
            if isinstance(value, ScheduledTransitionPrimitive)
        }
        continuation_closure: dict[str, QMatrix] = {}
        continuation_rows: dict[str, object] = {}
        for continuation_id, continuation in sorted(continuation_index.items()):
            consumed_ids.add(continuation_id)
            stochastic = _stochastic_matrix_measurement(
                continuation.matrix,
                expected_shape=(len(target.states), len(target.states)),
            )
            typed = bool(
                continuation.root == law.root
                and continuation.source_carrier_id == target.identifier
                and continuation.target_carrier_id == target.identifier
                and stochastic["valid"]
            )
            if typed:
                continuation_closure[canonical_sha256(continuation.matrix)] = (
                    continuation.matrix
                )
            continuation_rows[continuation_id] = {
                "stochastic": stochastic,
                "typed": typed,
            }
        changed = True
        while changed and len(continuation_closure) <= 64:
            changed = False
            for left in tuple(continuation_closure.values()):
                for right in tuple(continuation_closure.values()):
                    product_matrix = qmultiply(left, right)
                    key = canonical_sha256(product_matrix)
                    if key not in continuation_closure:
                        continuation_closure[key] = product_matrix
                        changed = True
        closure_complete = not changed
        identity = QMatrix.identity(len(target.states))
        nonidentity = any(row != identity for row in continuation_closure.values())
        recovery_rows: list[dict[str, object]] = []
        all_recover = bool(
            continuation_closure
            and closure_complete
            and nonidentity
            and reader_valid
        )
        if reader_valid:
            for word_hash, continuation in sorted(continuation_closure.items()):
                recovered = qmultiply(
                    reader.matrix,
                    qmultiply(continuation, writer.matrix),
                )
                recovery_residual = _q_residual(
                    recovered, QMatrix.identity(len(source.states))
                )
                word_valid = recovery_residual.get("nonzero_count") == 0
                all_recover = all_recover and word_valid
                recovery_rows.append(
                    {
                        "word_sha256": word_hash,
                        "continuation": continuation,
                        "reader_after_word_after_writer": recovered,
                        "recovery_residual": recovery_residual,
                        "recovers_original_flag": word_valid,
                    }
                )
        record_valid = bool(
            carriers_valid
            and writer_stochastic["valid"]
            and writer_residual.get("nonzero_count") == 0
            and reader_valid
            and all_recover
        )
        residuals["record_writing"] = {
            "writer_label_ignored": writer.semantic_label,
            "carrier_typing": carriers_valid,
            "writer_stochastic": writer_stochastic,
            "writer_W_residual": writer_residual,
            "target_flag_reader_residual": reader_residual,
            "continuation_generators": continuation_rows,
            "closure_size": len(continuation_closure),
            "closure_complete": closure_complete,
            "nonidentity_word_present": nonidentity,
            "recovery_rows": recovery_rows,
            "valid": record_valid,
        }
    else:
        residuals["record_writing"] = {
            "writer_present": isinstance(writer, RecordWriterPrimitive),
            "reader_present": isinstance(reader, ReaderPrimitive),
            "valid": False,
        }

    rewrite_valid = False
    rewrite = law.rewrite
    if record_valid and isinstance(rewrite, RewritePrimitive):
        consumed_ids.add(rewrite.identifier)
        source = rewrite.source_carrier
        target = rewrite.target_carrier
        input_state = law.rewrite_input_state
        rewrite_measurement = _stochastic_matrix_measurement(
            rewrite.matrix,
            expected_shape=(len(target.states), len(source.states)),
        )
        passive_measurement = _stochastic_matrix_measurement(
            rewrite.passive_inclusion,
            expected_shape=(len(target.states), len(source.states)),
        )
        effect = _compile_carrier_state_effect(
            law.compiler_mode, target, rewrite.created_support_state
        )
        output_state: QMatrix | None = None
        passive_state: QMatrix | None = None
        response: QMatrix | None = None
        passive_response: QMatrix | None = None
        if (
            isinstance(input_state, QMatrix)
            and input_state.shape == (len(source.states), 1)
            and rewrite_measurement["valid"]
            and passive_measurement["valid"]
            and effect is not None
        ):
            output_state = qmultiply(rewrite.matrix, input_state)
            passive_state = qmultiply(rewrite.passive_inclusion, input_state)
            response = qmultiply(effect, output_state)
            passive_response = qmultiply(effect, passive_state)
        expected_created = QMatrix.from_rows(
            (
                (
                    Fraction(1)
                    if row == target.states.index(rewrite.created_support_state)
                    else Fraction(0)
                ,)
                for row in range(len(target.states))
            ),
            ncols=1,
        ) if rewrite.created_support_state in target.states else None
        state_transport_residual = (
            _q_residual(output_state, expected_created)
            if output_state is not None and expected_created is not None
            else {"shape_match": False, "nonzero_count": None}
        )
        rewrite_valid = bool(
            rewrite.root == law.root
            and source.root == law.root
            and target.root == law.root
            and source.states == ("0", "1")
            and target.states == ("0", "1", "n")
            and rewrite.source_region_id != rewrite.target_region_id
            and rewrite.created_support_state == "n"
            and rewrite_measurement["valid"]
            and passive_measurement["valid"]
            and state_transport_residual.get("nonzero_count") == 0
            and response == QMatrix.from_rows(((1,),))
            and passive_response == QMatrix.from_rows(((0,),))
        )
        residuals["region_rewriting"] = {
            "source_region_id": rewrite.source_region_id,
            "output_region_id": rewrite.target_region_id,
            "regional_object_changed": rewrite.source_region_id
            != rewrite.target_region_id,
            "rewrite_stochastic": rewrite_measurement,
            "passive_inclusion_stochastic": passive_measurement,
            "transported_state": output_state,
            "created_support_state": rewrite.created_support_state,
            "state_transport_residual": state_transport_residual,
            "compiled_new_support_effect": effect,
            "composed_rewrite_response": response,
            "passive_inclusion_control_response": passive_response,
            "compiler_target_independent": law.compiler_mode
            == "target-independent-uniform",
            "valid": rewrite_valid,
        }
    else:
        residuals["region_rewriting"] = {
            "rewrite_present": isinstance(rewrite, RewritePrimitive),
            "opaque_tables_ignored": bool(law.opaque_role_tables),
            "valid": False,
        }

    role = (
        "REGION-REWRITING"
        if rewrite_valid
        else "RECORD-WRITING-ON-FIXED-ALGEBRA"
        if record_valid
        else "FIXED-ALGEBRA-CONDITIONING"
        if conditioning_valid
        else "STATIC-RESPONSE"
    )
    if role not in ONTOLOGY_ROLES:
        raise ScoreRefusal("ontology role escaped its frozen vocabulary")
    residuals["candidate_invariance"] = {
        "candidate_consulted": False,
        "candidate_value_not_a_measurement": True,
    }
    return OntologyLawMeasurement(
        primitive_payload_sha256=payload_hash,
        consumed_primitive_ids=tuple(sorted(consumed_ids)),
        role=role,
        residuals=residuals,
        issues=tuple(sorted(set(issues))),
    )


def build_ontology_existence_law(
    level: str, *, fault: str | None = None, candidate: str | None = None
) -> OntologyPrimitiveLaw:
    if level not in ONTOLOGY_ROLES:
        raise ValueError("unknown ontology control level")
    root = V4_INTERNAL_ROOT
    classical = (
        build_classical_existence_law()
        if level != "STATIC-RESPONSE"
        else None
    )
    conditioning_id = "question_instrument" if classical is not None else None
    source = CarrierPrimitive(root, "record-source", ("0", "1"))
    product_states = tuple(
        f"({state},{flag})" for state in source.states for flag in source.states
    )
    target = ProductCarrierPrimitive(
        root,
        "record-source_x_flag",
        source.states,
        source.states,
        product_states,
    )
    writer_matrix = QMatrix.from_rows(((1, 0), (0, 0), (0, 0), (0, 1)))
    writer = RecordWriterPrimitive(
        root,
        "deterministic-writer",
        source,
        target,
        writer_matrix,
    )
    reader = ReaderPrimitive(
        root,
        "delayed-flag-reader",
        target.identifier,
        source.states,
        _target_reader_matrix(2, 2),
        2,
    )
    continuations = (
        ScheduledTransitionPrimitive(
            root,
            "record-I",
            target.identifier,
            target.identifier,
            QMatrix.identity(4),
        ),
        ScheduledTransitionPrimitive(
            root,
            "record-X-source",
            target.identifier,
            target.identifier,
            _q_kron(QMatrix.from_rows(((0, 1), (1, 0))), QMatrix.identity(2)),
        ),
    )
    if fault == "nonclosed-continuation-semigroup":
        source_mixing = QMatrix.from_rows(
            ((1, Fraction(1, 2)), (0, Fraction(1, 2)))
        )
        continuations = (
            continuations[0],
            ScheduledTransitionPrimitive(
                root,
                "record-nonclosed-source-mixing",
                target.identifier,
                target.identifier,
                _q_kron(source_mixing, QMatrix.identity(2)),
            ),
        )
    if level in {"STATIC-RESPONSE", "FIXED-ALGEBRA-CONDITIONING"}:
        writer = None
        reader = None
        continuations = ()
    if fault == "missing-writer":
        writer = None
    elif fault == "missing-reader":
        reader = None
    elif fault == "missing-continuation":
        continuations = ()
    elif fault == "identity-writer-label":
        writer = RecordWriterPrimitive(
            root,
            "identity-labeled-writer",
            source,
            ProductCarrierPrimitive(
                root,
                source.identifier,
                source.states,
                ("unit",),
                source.states,
            ),
            QMatrix.identity(2),
            semantic_label="record-write",
        )

    rewrite_source = CarrierPrimitive(root, "G2", ("0", "1"))
    rewrite_target = CarrierPrimitive(root, "G3", ("0", "1", "n"))
    rewrite = RewritePrimitive(
        root,
        "two-to-three-rewrite",
        rewrite_source,
        rewrite_target,
        "region-G2",
        "region-G3-created-n",
        "n",
        QMatrix.from_rows(((1, 0), (0, 0), (0, 1))),
        QMatrix.from_rows(((1, 0), (0, 1), (0, 0))),
    )
    rewrite_input = QMatrix.from_rows(((0,), (1,)))
    if level != "REGION-REWRITING":
        rewrite = None
        rewrite_input = None
    if fault == "missing-rewrite":
        rewrite = None
    elif fault == "changed-table-no-rewrite":
        rewrite = None
    elif fault == "identity-rewrite-label":
        rewrite = RewritePrimitive(
            root,
            "identity-labeled-rewrite",
            rewrite_source,
            rewrite_source,
            "region-G2",
            "renamed-region-G2",
            "1",
            QMatrix.identity(2),
            QMatrix.identity(2),
        )
    return OntologyPrimitiveLaw(
        root=root,
        identifier=f"ontology-{level.lower()}",
        classical_law=classical,
        conditioning_instrument_id=(
            None if fault == "missing-conditioning" else conditioning_id
        ),
        writer=writer,
        delayed_flag_reader=reader,
        record_continuations=continuations,
        rewrite=rewrite,
        rewrite_input_state=rewrite_input,
        compiler_mode=(
            "target-specific-whitelist"
            if fault == "target-specific-compiler"
            else "target-independent-uniform"
        ),
        ontology_candidate=candidate,
        opaque_role_tables=(
            ("before", "0"), ("after", "1")
        )
        if fault in {"changed-table-no-rewrite", "identity-writer-label"}
        else (),
    )


@dataclass(frozen=True, slots=True)
class PrefixCompilerPrimitive:
    root: str
    identifier: str
    mode: str
    seed_regions: tuple[PrefixRegion, ...]
    whitelist_regions: tuple[PrefixRegion, ...] = ()
    split_mode: str = "symbolic-prefix-split"
    transition_reference_id: str | None = "shared-transition-X"

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "mode": self.mode,
            "seed_regions": self.seed_regions,
            "whitelist_regions": self.whitelist_regions,
            "split_mode": self.split_mode,
            "transition_reference_id": self.transition_reference_id,
        }


@dataclass(frozen=True, slots=True)
class CompilerLawMeasurement:
    primitive_payload_sha256: str
    consumed_primitive_ids: tuple[str, ...]
    normalization_valid: bool
    raw_atomless_valid: bool
    future_complete: bool
    congruence_valid: bool
    quotient_atomless_valid: bool
    residuals: Mapping[str, object]

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "CompilerLawMeasurement",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "consumed_primitive_ids": self.consumed_primitive_ids,
            "normalization_valid": self.normalization_valid,
            "raw_atomless_valid": self.raw_atomless_valid,
            "future_complete": self.future_complete,
            "congruence_valid": self.congruence_valid,
            "quotient_atomless_valid": self.quotient_atomless_valid,
            "residuals": self.residuals,
        }


def _binary_atoms(depth: int) -> tuple[str, ...]:
    return tuple("".join(bits) for bits in itertools.product("01", repeat=depth))


def _prefix_effect(
    compiler: PrefixCompilerPrimitive, region: PrefixRegion, atoms: Sequence[str]
) -> QMatrix | None:
    if compiler.mode == "uniform-prefix-compiler":
        accepted = True
    elif compiler.mode == "seed-whitelist-compiler":
        accepted = region in compiler.whitelist_regions
    elif compiler.mode == "scalar-volume-compiler":
        mass = bernoulli_mass(region, Fraction(1, 2))
        return QMatrix.from_rows(((mass for _atom in atoms),), ncols=len(atoms))
    else:
        accepted = False
    if not accepted:
        return None
    return QMatrix.from_rows(
        (
            (
                Fraction(1)
                if PrefixRegion.cylinder(atom).is_part_of(region)
                else Fraction(0)
                for atom in atoms
            ),
        ),
        ncols=len(atoms),
    )


def measure_prefix_compiler(
    compiler: object, *, quotient_mode: str = "literal-prefix-algebra"
) -> CompilerLawMeasurement:
    if not isinstance(compiler, PrefixCompilerPrimitive):
        raise ScoreRefusal("compiler promotion requires PrefixCompilerPrimitive")
    payload_hash = canonical_sha256(compiler.to_data())
    atoms = _binary_atoms(3)
    identity = QMatrix.identity(len(atoms))
    regions = tuple(
        dict.fromkeys(
            compiler.seed_regions
            + (
                PrefixRegion.zero(),
                PrefixRegion.one(),
                PrefixRegion.cylinder("0"),
                PrefixRegion.cylinder("1"),
            )
        )
    )
    normalization_rows: list[dict[str, object]] = []
    normalization_valid = compiler.mode in {
        "uniform-prefix-compiler",
        "seed-whitelist-compiler",
    }
    atomless_rows: list[dict[str, object]] = []
    raw_atomless_valid = bool(
        compiler.mode in {"uniform-prefix-compiler", "seed-whitelist-compiler"}
        and compiler.split_mode == "symbolic-prefix-split"
    )
    for region in regions:
        effect = _prefix_effect(compiler, region, atoms)
        complement_effect = _prefix_effect(compiler, region.complement(), atoms)
        if effect is None or complement_effect is None:
            normalization_valid = False
            normalization_rows.append(
                {
                    "region": region,
                    "compiled": False,
                    "normalization_residual": {"nonzero_count": None},
                }
            )
        else:
            question_yes = QMatrix.from_rows(
                (
                    (
                        effect.data[0][row]
                        if row == column
                        else Fraction(0)
                        for column in range(len(atoms))
                    )
                    for row in range(len(atoms))
                ),
                ncols=len(atoms),
            )
            question_no = QMatrix.from_rows(
                (
                    (
                        complement_effect.data[0][row]
                        if row == column
                        else Fraction(0)
                        for column in range(len(atoms))
                    )
                    for row in range(len(atoms))
                ),
                ncols=len(atoms),
            )
            residual = _q_residual(qadd(question_yes, question_no), identity)
            valid = residual.get("nonzero_count") == 0
            normalization_valid = normalization_valid and valid
            normalization_rows.append(
                {
                    "region": region,
                    "Q_A": question_yes,
                    "Q_notA": question_no,
                    "both_ports_retained": True,
                    "normalization_residual": residual,
                    "valid": valid,
                }
            )
        if not region.is_zero():
            left, right = region.atomless_bipartition()
            split_valid = bool(
                not left.is_zero()
                and not right.is_zero()
                and left != region
                and right != region
                and left.disjoint(right)
                and left.join(right) == region
            )
            raw_atomless_valid = raw_atomless_valid and split_valid
            atomless_rows.append(
                {
                    "region": region,
                    "left": left,
                    "right": right,
                    "proper_nonzero_partition": split_valid,
                }
            )

    fresh = PrefixRegion.cylinder("000")
    fresh_not_seed = fresh not in compiler.seed_regions
    fresh_effect = _prefix_effect(compiler, fresh, atoms)
    separation_profile: tuple[Fraction, ...] | None = None
    if fresh_effect is not None:
        separation_profile = tuple(fresh_effect.data[0])
    future_complete = bool(
        compiler.mode == "uniform-prefix-compiler"
        and fresh_not_seed
        and fresh_effect is not None
        and len(set(separation_profile or ())) == 2
    )

    profile_rows: list[tuple[PrefixRegion, tuple[Fraction, ...]]] = []
    for region in regions:
        effect = _prefix_effect(compiler, region, atoms)
        if effect is not None:
            profile_rows.append((region, tuple(effect.data[0])))
    literal_injective = len({profile for _region, profile in profile_rows}) == len(
        {region for region, _profile in profile_rows}
    )
    symbolic_separation_rows: list[dict[str, object]] = []
    symbolic_separation_valid = compiler.mode == "uniform-prefix-compiler"
    for first_region, second_region in itertools.combinations(regions, 2):
        if first_region == second_region:
            continue
        first_only = first_region.difference(second_region)
        second_only = second_region.difference(first_region)
        symmetric_difference = first_only.join(second_only)
        directional_witness = first_only if not first_only.is_zero() else second_only
        witness_prefix = (
            directional_witness.words[0]
            if directional_witness.words
            else None
        )
        faithful_preparation = (
            PrefixRegion.cylinder(witness_prefix)
            if isinstance(witness_prefix, str)
            else PrefixRegion.zero()
        )
        first_response = faithful_preparation.is_part_of(first_region)
        second_response = faithful_preparation.is_part_of(second_region)
        separates = bool(
            witness_prefix is not None
            and not symmetric_difference.is_zero()
            and first_response != second_response
        )
        symbolic_separation_valid = symbolic_separation_valid and separates
        symbolic_separation_rows.append(
            {
                "first_region": first_region,
                "second_region": second_region,
                "symmetric_difference": symmetric_difference,
                "directional_difference_used": directional_witness,
                "canonical_witness_prefix": witness_prefix,
                "faithful_support_preparation": faithful_preparation,
                "first_response": first_response,
                "second_response": second_response,
                "separates": separates,
            }
        )
    operation_rows: list[dict[str, object]] = []
    operation_valid = True
    operation_regions = (
        PrefixRegion.cylinder("0"),
        PrefixRegion.cylinder("00"),
        PrefixRegion.cylinder("1"),
    )
    for left in operation_regions:
        for right in operation_regions:
            left_effect = _prefix_effect(compiler, left, atoms)
            right_effect = _prefix_effect(compiler, right, atoms)
            meet_effect = _prefix_effect(compiler, left.meet(right), atoms)
            join_effect = _prefix_effect(compiler, left.join(right), atoms)
            complement_effect = _prefix_effect(compiler, left.complement(), atoms)
            if any(
                value is None
                for value in (
                    left_effect,
                    right_effect,
                    meet_effect,
                    join_effect,
                    complement_effect,
                )
            ):
                valid = False
                row = {"left": left, "right": right, "compiled": False}
            else:
                assert left_effect is not None
                assert right_effect is not None
                assert meet_effect is not None
                assert join_effect is not None
                assert complement_effect is not None
                pointwise_meet = QMatrix.from_rows(
                    (
                        (
                            min(left_effect.data[0][index], right_effect.data[0][index])
                            for index in range(len(atoms))
                        ),
                    ),
                    ncols=len(atoms),
                )
                pointwise_join = QMatrix.from_rows(
                    (
                        (
                            max(left_effect.data[0][index], right_effect.data[0][index])
                            for index in range(len(atoms))
                        ),
                    ),
                    ncols=len(atoms),
                )
                pointwise_complement = QMatrix.from_rows(
                    (
                        (
                            1 - left_effect.data[0][index]
                            for index in range(len(atoms))
                        ),
                    ),
                    ncols=len(atoms),
                )
                meet_residual = _q_residual(meet_effect, pointwise_meet)
                join_residual = _q_residual(join_effect, pointwise_join)
                complement_residual = _q_residual(
                    complement_effect, pointwise_complement
                )
                left_question = QMatrix.from_rows(
                    (
                        (
                            left_effect.data[0][row]
                            if row == column
                            else Fraction(0)
                            for column in range(len(atoms))
                        )
                        for row in range(len(atoms))
                    ),
                    ncols=len(atoms),
                )
                right_question = QMatrix.from_rows(
                    (
                        (
                            right_effect.data[0][row]
                            if row == column
                            else Fraction(0)
                            for column in range(len(atoms))
                        )
                        for row in range(len(atoms))
                    ),
                    ncols=len(atoms),
                )
                meet_question = QMatrix.from_rows(
                    (
                        (
                            meet_effect.data[0][row]
                            if row == column
                            else Fraction(0)
                            for column in range(len(atoms))
                        )
                        for row in range(len(atoms))
                    ),
                    ncols=len(atoms),
                )
                process_composition_row_residual = _q_residual(
                    qmultiply(left_question, right_question), meet_question
                )
                valid = all(
                    residual.get("nonzero_count") == 0
                    for residual in (
                        meet_residual,
                        join_residual,
                        complement_residual,
                        process_composition_row_residual,
                    )
                )
                row = {
                    "left": left,
                    "right": right,
                    "meet_residual": meet_residual,
                    "join_residual": join_residual,
                    "complement_residual": complement_residual,
                    "process_composition_residual": process_composition_row_residual,
                    "valid": valid,
                }
            operation_valid = operation_valid and valid
            operation_rows.append(row)
    process_composition_residual = _q_residual(
        qmultiply(identity, identity), identity
    )
    scalar_volume_control = quotient_mode == "scalar-volume-equivalence"
    congruence_valid = bool(
        compiler.mode == "uniform-prefix-compiler"
        and literal_injective
        and symbolic_separation_valid
        and operation_valid
        and process_composition_residual.get("nonzero_count") == 0
        and not scalar_volume_control
    )
    quotient_atomless_valid = bool(
        congruence_valid
        and quotient_mode == "literal-prefix-algebra"
        and raw_atomless_valid
    )
    return CompilerLawMeasurement(
        primitive_payload_sha256=payload_hash,
        consumed_primitive_ids=tuple(
            identifier
            for identifier in (compiler.identifier, compiler.transition_reference_id)
            if identifier is not None
        ),
        normalization_valid=normalization_valid,
        raw_atomless_valid=raw_atomless_valid,
        future_complete=future_complete,
        congruence_valid=congruence_valid,
        quotient_atomless_valid=quotient_atomless_valid,
        residuals={
            "normalization": {
                "generic_constructor": compiler.mode,
                "rows": normalization_rows,
                "valid": normalization_valid,
            },
            "raw_atomlessness": {
                "constructor": "PrefixRegion.atomless_bipartition",
                "rows": atomless_rows,
                "valid": raw_atomless_valid,
            },
            "heldout_future": {
                "region": fresh,
                "not_in_seed_list": fresh_not_seed,
                "compiled_effect": fresh_effect,
                "separation_profile": separation_profile,
                "valid": future_complete,
            },
            "regional_congruence": {
                "profile_rows": profile_rows,
                "contextual_equality_is_literal_equality": literal_injective,
                "symbolic_faithful_separation_rule": (
                    "for A!=B choose the first canonical cylinder in A symmetric-difference B"
                ),
                "symbolic_faithful_separation_rows": symbolic_separation_rows,
                "symbolic_faithful_separation_valid": symbolic_separation_valid,
                "finite_leaf_census_used_as_theorem": False,
                "scalar_volume_control": scalar_volume_control,
                "equal_volume_distinct_regions": {
                    "left": PrefixRegion.cylinder("0"),
                    "right": PrefixRegion.cylinder("1"),
                    "both_mass": Fraction(1, 2),
                    "identified_by_control": scalar_volume_control,
                },
                "operation_descent_rows": operation_rows,
                "process_composition_residual": process_composition_residual,
                "valid": congruence_valid,
            },
            "physical_image_atomlessness": {
                "quotient_mode": quotient_mode,
                "finite_leaf_census_used_as_proof": False,
                "symbolic_split_constructor_reused_after_quotient": True,
                "valid": quotient_atomless_valid,
            },
        },
    )


@dataclass(frozen=True, slots=True)
class OverlapCandidatePrimitive:
    root: str
    identifier: str
    probabilities: tuple[Fraction, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "probabilities": self.probabilities,
        }


@dataclass(frozen=True, slots=True)
class OverlapPrimitiveLaw:
    root: str
    identifier: str
    configurations: tuple[str, ...]
    candidates: tuple[OverlapCandidatePrimitive, ...]
    transition_reference_id: str | None = "shared-transition-X"

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "configurations": self.configurations,
            "candidates": self.candidates,
            "transition_reference_id": self.transition_reference_id,
        }


@dataclass(frozen=True, slots=True)
class OverlapLawMeasurement:
    primitive_payload_sha256: str
    consumed_primitive_ids: tuple[str, ...]
    valid: bool
    selected_candidate_id: str | None
    residuals: Mapping[str, object]

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "OverlapLawMeasurement",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "consumed_primitive_ids": self.consumed_primitive_ids,
            "valid": self.valid,
            "selected_candidate_id": self.selected_candidate_id,
            "residuals": self.residuals,
        }


def measure_overlap_primitive_law(law: object) -> OverlapLawMeasurement:
    if not isinstance(law, OverlapPrimitiveLaw):
        raise ScoreRefusal("overlap promotion requires OverlapPrimitiveLaw")
    expected_configurations = tuple(
        "".join(bits) for bits in itertools.product("01", repeat=3)
    )
    configuration_valid = law.configurations == expected_configurations
    candidate_ids = tuple(candidate.identifier for candidate in law.candidates)
    candidate_family_exact = bool(
        len(law.candidates) == 2
        and len(set(candidate_ids)) == len(candidate_ids)
        and all(candidate_ids)
    )
    candidate_rows: dict[str, object] = {}
    zero_residual_candidates: list[str] = []
    marginal_signatures: list[tuple[tuple[Fraction, ...], tuple[Fraction, ...]]] = []
    for candidate in law.candidates:
        probabilities = candidate.probabilities
        distribution_valid = bool(
            candidate.root == law.root
            and len(probabilities) == len(law.configurations)
            and all(value >= 0 for value in probabilities)
            and sum(probabilities, Fraction(0)) == 1
        )
        probability = {
            configuration: probabilities[index]
            for index, configuration in enumerate(law.configurations)
        } if len(probabilities) == len(law.configurations) else {}
        p_ab = {
            ab: sum(
                (
                    probability.get(ab[0] + ab[1] + c, Fraction(0))
                    for c in "01"
                ),
                Fraction(0),
            )
            for ab in ("00", "01", "10", "11")
        }
        p_bc = {
            bc: sum(
                (
                    probability.get(a + bc[0] + bc[1], Fraction(0))
                    for a in "01"
                ),
                Fraction(0),
            )
            for bc in ("00", "01", "10", "11")
        }
        p_b = {
            b: sum(
                (
                    probability.get(a + b + c, Fraction(0))
                    for a in "01"
                    for c in "01"
                ),
                Fraction(0),
            )
            for b in "01"
        }
        markov_residuals = {
            configuration: probability.get(configuration, Fraction(0))
            * p_b[configuration[1]]
            - p_ab[configuration[:2]] * p_bc[configuration[1:]]
            for configuration in law.configurations
        }
        markov_zero = distribution_valid and all(
            value == 0 for value in markov_residuals.values()
        )
        if markov_zero:
            zero_residual_candidates.append(candidate.identifier)
        marginal_signatures.append(
            (
                tuple(p_ab[key] for key in ("00", "01", "10", "11")),
                tuple(p_bc[key] for key in ("00", "01", "10", "11")),
            )
        )
        endpoint_equal = sum(
            value
            for configuration, value in probability.items()
            if configuration[0] == configuration[2]
        )
        candidate_rows[candidate.identifier] = {
            "distribution_valid": distribution_valid,
            "P_AB": p_ab,
            "P_BC": p_bc,
            "P_B": p_b,
            "markov_cell_residuals": markov_residuals,
            "markov_zero": markov_zero,
            "P_A_equals_C": endpoint_equal,
        }
    identical_marginals = bool(marginal_signatures) and len(set(marginal_signatures)) == 1
    uniform_signature = (
        tuple(Fraction(1, 4) for _ in range(4)),
        tuple(Fraction(1, 4) for _ in range(4)),
    )
    uniform_marginals = bool(marginal_signatures) and all(
        signature == uniform_signature for signature in marginal_signatures
    )
    endpoint_values = {
        row["P_A_equals_C"] for row in candidate_rows.values()
    }
    endpoint_control_exact = endpoint_values == {
        Fraction(1, 2),
        Fraction(1),
    }
    valid = bool(
        configuration_valid
        and candidate_family_exact
        and identical_marginals
        and uniform_marginals
        and endpoint_control_exact
        and len(zero_residual_candidates) == 1
    )
    return OverlapLawMeasurement(
        primitive_payload_sha256=canonical_sha256(law.to_data()),
        consumed_primitive_ids=tuple(
            sorted(
                {
                    law.identifier,
                    *(row.identifier for row in law.candidates),
                    *((law.transition_reference_id,) if law.transition_reference_id else ()),
                }
            )
        ),
        valid=valid,
        selected_candidate_id=(
            zero_residual_candidates[0]
            if len(zero_residual_candidates) == 1
            else None
        ),
        residuals={
            "configuration_order": law.configurations,
            "configuration_order_valid": configuration_valid,
            "candidate_ids": candidate_ids,
            "exactly_two_unique_candidates": candidate_family_exact,
            "candidates": candidate_rows,
            "identical_AB_BC_marginals": identical_marginals,
            "identical_uniform_AB_BC_marginals": (
                identical_marginals and uniform_marginals
            ),
            "each_AB_BC_marginal_cell_is_one_quarter": uniform_marginals,
            "endpoint_correlation_values": tuple(sorted(endpoint_values)),
            "endpoint_control_exact_half_versus_one": endpoint_control_exact,
            "zero_markov_residual_candidates": tuple(zero_residual_candidates),
            "selected_by_order_hash_or_sparsity": False,
            "valid": valid,
        },
    )


def build_overlap_existence_law(fault: str | None = None) -> OverlapPrimitiveLaw:
    root = V4_INTERNAL_ROOT
    configurations = tuple(
        "".join(bits) for bits in itertools.product("01", repeat=3)
    )
    uniform = tuple(Fraction(1, 8) for _ in configurations)
    correlated = tuple(
        Fraction(1, 4) if row[0] == row[2] else Fraction(0)
        for row in configurations
    )
    candidates: tuple[OverlapCandidatePrimitive, ...] = (
        OverlapCandidatePrimitive(root, "uniform-independent", uniform),
        OverlapCandidatePrimitive(root, "A-equals-C", correlated),
    )
    if fault == "missing-markov-selector":
        candidates = candidates[:1]
    elif fault == "both-markov-survive":
        candidates = (
            candidates[0],
            OverlapCandidatePrimitive(root, "uniform-independent-clone", uniform),
        )
    elif fault == "extra-overlap-candidate":
        candidates = candidates + (
            OverlapCandidatePrimitive(root, "A-equals-C-clone", correlated),
        )
    elif fault == "nonuniform-shared-marginals":
        independent_b_zero = tuple(
            Fraction(1, 4) if row[1] == "0" else Fraction(0)
            for row in configurations
        )
        correlated_b_zero = tuple(
            Fraction(1, 2)
            if row[1] == "0" and row[0] == row[2]
            else Fraction(0)
            for row in configurations
        )
        candidates = (
            OverlapCandidatePrimitive(
                root, "B-zero-conditionally-independent", independent_b_zero
            ),
            OverlapCandidatePrimitive(
                root, "B-zero-A-equals-C", correlated_b_zero
            ),
        )
    return OverlapPrimitiveLaw(
        root=root,
        identifier="ABC-overlap-family",
        configurations=configurations,
        candidates=candidates,
    )


@dataclass(frozen=True, slots=True)
class ComparisonCutPrimitive:
    root: str
    identifier: str
    whole_transition_id: str
    factor_matrices: tuple[QMatrix, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "whole_transition_id": self.whole_transition_id,
            "factor_matrices": self.factor_matrices,
        }


@dataclass(frozen=True, slots=True)
class ComparisonPrimitiveLaw:
    root: str
    identifier: str
    transition_id: str
    transition: QMatrix
    transported_transition_id: str
    transported_transition: QMatrix
    comparison_id: str
    comparison: QMatrix
    calibrated_state: QMatrix
    calibrated_effect: QMatrix
    cuts: tuple[ComparisonCutPrimitive, ...]
    transition_reference_id: str | None = "shared-transition-X"

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "transition_id": self.transition_id,
            "transition": self.transition,
            "transported_transition_id": self.transported_transition_id,
            "transported_transition": self.transported_transition,
            "comparison_id": self.comparison_id,
            "comparison": self.comparison,
            "calibrated_state": self.calibrated_state,
            "calibrated_effect": self.calibrated_effect,
            "cuts": self.cuts,
            "transition_reference_id": self.transition_reference_id,
        }


@dataclass(frozen=True, slots=True)
class ComparisonLawMeasurement:
    primitive_payload_sha256: str
    consumed_primitive_ids: tuple[str, ...]
    valid: bool
    residuals: Mapping[str, object]

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "ComparisonLawMeasurement",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "consumed_primitive_ids": self.consumed_primitive_ids,
            "valid": self.valid,
            "residuals": self.residuals,
        }


def measure_comparison_primitive_law(law: object) -> ComparisonLawMeasurement:
    if not isinstance(law, ComparisonPrimitiveLaw):
        raise ScoreRefusal("comparison promotion requires ComparisonPrimitiveLaw")
    permutation_valid, inverse = _q_is_permutation(law.comparison)
    carrier_size = law.comparison.nrows
    transition_measurement = _stochastic_matrix_measurement(
        law.transition, expected_shape=(carrier_size, carrier_size)
    )
    transported_transition_measurement = _stochastic_matrix_measurement(
        law.transported_transition,
        expected_shape=(carrier_size, carrier_size),
    )
    state_measurement = _stochastic_matrix_measurement(
        law.calibrated_state, expected_shape=(carrier_size, 1)
    )
    effect_valid = bool(
        law.calibrated_effect.shape == (1, carrier_size)
        and all(
            Fraction(0) <= entry <= Fraction(1)
            for row in law.calibrated_effect.data
            for entry in row
        )
    )
    typed_transition_control = bool(
        transition_measurement["valid"]
        and transported_transition_measurement["valid"]
        and state_measurement["valid"]
        and effect_valid
    )
    nonidentity = bool(
        permutation_valid
        and law.comparison != QMatrix.identity(law.comparison.nrows)
    )
    transported_expected: QMatrix | None = None
    naturality_residual: dict[str, object] = {"nonzero_count": None}
    conjugation_residual: dict[str, object] = {"nonzero_count": None}
    transported_state: QMatrix | None = None
    transported_effect: QMatrix | None = None
    state_moved = False
    effect_moved = False
    calibration_left: QMatrix | None = None
    calibration_right: QMatrix | None = None
    calibration_residual: dict[str, object] = {"nonzero_count": None}
    if permutation_valid and inverse is not None and typed_transition_control:
        transported_expected = qmultiply(
            law.comparison, qmultiply(law.transition, inverse)
        )
        conjugation_residual = _q_residual(
            law.transported_transition, transported_expected
        )
        naturality_residual = _q_residual(
            qmultiply(law.comparison, law.transition),
            qmultiply(law.transported_transition, law.comparison),
        )
        transported_state = qmultiply(law.comparison, law.calibrated_state)
        transported_effect = qmultiply(law.calibrated_effect, inverse)
        state_moved = transported_state != law.calibrated_state
        effect_moved = transported_effect != law.calibrated_effect
        calibration_left = qmultiply(
            law.calibrated_effect,
            qmultiply(law.transition, law.calibrated_state),
        )
        calibration_right = qmultiply(
            transported_effect,
            qmultiply(law.transported_transition, transported_state),
        )
        calibration_residual = _q_residual(calibration_left, calibration_right)
    cut_rows: dict[str, object] = {}
    cut_ids = tuple(cut.identifier for cut in law.cuts)
    cut_signatures = tuple(
        canonical_sha256(cut.factor_matrices) for cut in law.cuts
    )
    cuts_registered_exactly = bool(
        len(law.cuts) == 2
        and len(set(cut_ids)) == 2
        and all(cut_ids)
        and len(set(cut_signatures)) == 2
    )
    cuts_valid = cuts_registered_exactly
    for cut in law.cuts:
        product: QMatrix | None = None
        factors_typed = bool(
            cut.factor_matrices
            and all(
                _stochastic_matrix_measurement(
                    factor, expected_shape=(carrier_size, carrier_size)
                )["valid"]
                for factor in cut.factor_matrices
            )
        )
        composable = factors_typed
        if cut.factor_matrices:
            product = cut.factor_matrices[0]
            for factor in cut.factor_matrices[1:]:
                try:
                    product = qmultiply(factor, product)
                except ValueError:
                    composable = False
                    product = None
                    break
        residual = (
            _q_residual(product, law.transition)
            if product is not None
            else {"shape_match": False, "nonzero_count": None}
        )
        valid = bool(
            cut.root == law.root
            and cut.whole_transition_id == law.transition_id
            and factors_typed
            and composable
            and residual.get("nonzero_count") == 0
        )
        cuts_valid = cuts_valid and valid
        cut_rows[cut.identifier] = {
            "factor_matrices": cut.factor_matrices,
            "factors_typed_stochastic": factors_typed,
            "recomposed_product": product,
            "residual": residual,
            "valid": valid,
        }
    valid = bool(
        law.root
        and permutation_valid
        and typed_transition_control
        and nonidentity
        and conjugation_residual.get("nonzero_count") == 0
        and naturality_residual.get("nonzero_count") == 0
        and state_moved
        and effect_moved
        and calibration_residual.get("nonzero_count") == 0
        and cuts_valid
    )
    return ComparisonLawMeasurement(
        primitive_payload_sha256=canonical_sha256(law.to_data()),
        consumed_primitive_ids=tuple(
            sorted(
                {
                    law.identifier,
                    law.transition_id,
                    law.transported_transition_id,
                    law.comparison_id,
                    *(cut.identifier for cut in law.cuts),
                    *((law.transition_reference_id,) if law.transition_reference_id else ()),
                }
            )
        ),
        valid=valid,
        residuals={
            "comparison_matrix": law.comparison,
            "permutation_entrywise_with_inverse": permutation_valid,
            "inverse": inverse,
            "genuinely_nonidentity": nonidentity,
            "transition_stochastic": transition_measurement,
            "transported_transition_stochastic": transported_transition_measurement,
            "calibrated_state": state_measurement,
            "calibrated_effect_typed": effect_valid,
            "conjugated_transition": transported_expected,
            "conjugation_residual": conjugation_residual,
            "naturality_residual": naturality_residual,
            "transported_state": transported_state,
            "transported_effect": transported_effect,
            "calibrated_state_moved": state_moved,
            "calibrated_effect_moved": effect_moved,
            "calibration_left": calibration_left,
            "calibration_right": calibration_right,
            "calibration_residual": calibration_residual,
            "cuts": cut_rows,
            "exactly_two_distinct_registered_cuts": cuts_registered_exactly,
            "two_registered_cuts": cuts_valid,
            "valid": valid,
        },
    )


def build_comparison_existence_law(
    fault: str | None = None,
) -> ComparisonPrimitiveLaw:
    root = V4_INTERNAL_ROOT
    transition = QMatrix.from_rows(((1, 1), (0, 0)))
    comparison = QMatrix.from_rows(((0, 1), (1, 0)))
    if fault == "negative-comparison-transition":
        transition = QMatrix.from_rows(((2, 0), (-1, 1)))
    transported = qmultiply(
        comparison, qmultiply(transition, qtranspose(comparison))
    )
    if fault == "altered-comparison-permutation":
        comparison = QMatrix.identity(2)
    elif fault == "rank-deficient-comparison":
        comparison = QMatrix.from_rows(((1, 0), (0, 0)))
    if fault == "changed-transported-transition":
        transported = transition
    cuts = (
        ComparisonCutPrimitive(
            root,
            "comparison-cut-left",
            "comparison-T",
            (transition, QMatrix.identity(2)),
        ),
        ComparisonCutPrimitive(
            root,
            "comparison-cut-right",
            "comparison-T",
            (QMatrix.identity(2), transition),
        ),
    )
    if fault == "altered-comparison-cut":
        cuts = (
            cuts[0],
            ComparisonCutPrimitive(
                root,
                "comparison-cut-right",
                "comparison-T",
                (QMatrix.identity(2), QMatrix.identity(2)),
            ),
        )
    elif fault == "duplicate-comparison-cut":
        cuts = (
            cuts[0],
            ComparisonCutPrimitive(
                root,
                "comparison-cut-duplicate",
                "comparison-T",
                cuts[0].factor_matrices,
            ),
        )
    calibrated_state = QMatrix.from_rows(((1,), (0,)))
    if fault == "nonstate-comparison-calibration":
        calibrated_state = QMatrix.from_rows(((2,), (-1,)))
    return ComparisonPrimitiveLaw(
        root=root,
        identifier="comparison-control",
        transition_id="comparison-T",
        transition=transition,
        transported_transition_id="comparison-T-prime",
        transported_transition=transported,
        comparison_id="comparison-P",
        comparison=comparison,
        calibrated_state=calibrated_state,
        calibrated_effect=QMatrix.from_rows(((1, 0),)),
        cuts=cuts,
    )


@dataclass(frozen=True, slots=True)
class ReplacementPrimitive:
    root: str
    identifier: str
    matrix: QMatrix

    def to_data(self) -> dict[str, object]:
        return {"root": self.root, "id": self.identifier, "matrix": self.matrix}


@dataclass(frozen=True, slots=True)
class LocalityRegionPrimitive:
    root: str
    identifier: str
    effect_generators: tuple[QMatrix, ...]
    exterior_replacement_ids: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "effect_generators": self.effect_generators,
            "exterior_replacement_ids": self.exterior_replacement_ids,
        }


@dataclass(frozen=True, slots=True)
class LocalityPrimitiveLaw:
    root: str
    identifier: str
    carrier_states: tuple[str, ...]
    regions: tuple[LocalityRegionPrimitive, ...]
    replacements: tuple[ReplacementPrimitive, ...]
    opaque_row_spaces: tuple[tuple[str, QMatrix], ...] = ()
    transition_reference_id: str | None = "shared-transition-X"

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_states": self.carrier_states,
            "regions": self.regions,
            "replacements": self.replacements,
            "opaque_row_spaces": self.opaque_row_spaces,
            "transition_reference_id": self.transition_reference_id,
            "ordering": "left-major-lexicographic",
        }


@dataclass(frozen=True, slots=True)
class LocalityLawMeasurement:
    primitive_payload_sha256: str
    consumed_primitive_ids: tuple[str, ...]
    valid: bool
    residuals: Mapping[str, object]

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "LocalityLawMeasurement",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "consumed_primitive_ids": self.consumed_primitive_ids,
            "valid": self.valid,
            "residuals": self.residuals,
        }


def _fixed_space_from_replacements(
    replacements: Sequence[QMatrix], ambient: int
) -> QMatrix:
    if not replacements:
        return QMatrix.identity(ambient)
    spaces = tuple(
        qkernel(qsubtract(replacement, QMatrix.identity(ambient)))
        for replacement in replacements
    )
    result = spaces[0]
    for space in spaces[1:]:
        result = qsubspace_intersection(result, space)
    return qcolumnspace(result)


def measure_locality_primitive_law(law: object) -> LocalityLawMeasurement:
    if not isinstance(law, LocalityPrimitiveLaw):
        raise ScoreRefusal("locality promotion requires LocalityPrimitiveLaw")
    ambient = len(law.carrier_states)
    carrier_valid = bool(
        law.root
        and law.carrier_states == ("(0,0)", "(0,1)", "(1,0)", "(1,1)")
    )
    replacement_index_raw, replacement_issues = _unique_index(
        law.replacements, "locality-replacement"
    )
    replacement_index = {
        key: value
        for key, value in replacement_index_raw.items()
        if isinstance(value, ReplacementPrimitive)
    }
    replacement_rows: dict[str, object] = {}
    replacements_valid = not replacement_issues
    for replacement_id, replacement in sorted(replacement_index.items()):
        permutation_valid, inverse = _q_is_permutation(replacement.matrix)
        typed = bool(
            replacement.root == law.root
            and replacement.matrix.shape == (ambient, ambient)
            and permutation_valid
        )
        replacements_valid = replacements_valid and typed
        replacement_rows[replacement_id] = {
            "permutation_valid": permutation_valid,
            "inverse": inverse,
            "typed": typed,
        }
    region_index_raw, region_issues = _unique_index(law.regions, "locality-region")
    region_index = {
        key: value
        for key, value in region_index_raw.items()
        if isinstance(value, LocalityRegionPrimitive)
    }
    rows: dict[str, object] = {}
    spaces: dict[str, QMatrix] = {}
    dynamic_spaces: dict[str, QMatrix] = {}
    regions_valid = not region_issues and set(region_index) == {"S", "T", "ST"}
    for region_id, region in sorted(region_index.items()):
        generators_typed = bool(
            region.root == law.root
            and region.effect_generators
            and all(
                generator.nrows == ambient and generator.ncols == 1
                for generator in region.effect_generators
            )
        )
        kin = (
            qcolumnspace(qhstack(region.effect_generators, nrows=ambient))
            if generators_typed
            else QMatrix.zero(ambient, 0)
        )
        replacement_values = tuple(
            replacement_index[identifier].matrix
            for identifier in region.exterior_replacement_ids
            if identifier in replacement_index
        )
        references_total = len(replacement_values) == len(
            region.exterior_replacement_ids
        )
        dyn = _fixed_space_from_replacements(replacement_values, ambient)
        kin_outside_dyn = qsubspace_inclusion_residual(kin, dyn)
        dyn_outside_kin = qsubspace_inclusion_residual(dyn, kin)
        equality = kin_outside_dyn == 0 and dyn_outside_kin == 0
        region_valid = generators_typed and references_total and equality
        regions_valid = regions_valid and region_valid
        spaces[region_id] = kin
        dynamic_spaces[region_id] = dyn
        rows[region_id] = {
            "generated_effect_columns": region.effect_generators,
            "Kin": kin,
            "exterior_replacement_ids": region.exterior_replacement_ids,
            "Dyn_equalizer": dyn,
            "Kin_outside_Dyn": kin_outside_dyn,
            "Dyn_outside_Kin": dyn_outside_kin,
            "equal": equality,
            "valid": region_valid,
        }
    inclusion_rows: dict[str, object] = {}
    inclusion_valid = False
    if set(spaces) == {"S", "T", "ST"}:
        s_in_st = qsubspace_inclusion_residual(spaces["S"], spaces["ST"])
        t_in_st = qsubspace_inclusion_residual(spaces["T"], spaces["ST"])
        st_in_s = qsubspace_inclusion_residual(spaces["ST"], spaces["S"])
        st_in_t = qsubspace_inclusion_residual(spaces["ST"], spaces["T"])
        s_in_t = qsubspace_inclusion_residual(spaces["S"], spaces["T"])
        t_in_s = qsubspace_inclusion_residual(spaces["T"], spaces["S"])
        inclusion_valid = bool(
            s_in_st == 0
            and t_in_st == 0
            and st_in_s > 0
            and st_in_t > 0
            and s_in_t > 0
            and t_in_s > 0
        )
        inclusion_rows = {
            "Kin_S_subset_Kin_ST_residual": s_in_st,
            "Kin_T_subset_Kin_ST_residual": t_in_st,
            "Kin_ST_outside_Kin_S": st_in_s,
            "Kin_ST_outside_Kin_T": st_in_t,
            "Kin_S_outside_Kin_T": s_in_t,
            "Kin_T_outside_Kin_S": t_in_s,
            "strict_inclusions_and_noninclusions": inclusion_valid,
        }
    full_rank = qrank(spaces.get("ST", QMatrix.zero(ambient, 0))) == ambient
    nonconstant = bool(
        qrank(spaces.get("S", QMatrix.zero(ambient, 0))) > 1
        and qrank(spaces.get("T", QMatrix.zero(ambient, 0))) > 1
    )
    faithful = full_rank
    valid = bool(
        carrier_valid
        and replacements_valid
        and regions_valid
        and inclusion_valid
        and nonconstant
        and faithful
    )
    return LocalityLawMeasurement(
        primitive_payload_sha256=canonical_sha256(law.to_data()),
        consumed_primitive_ids=tuple(
            sorted(
                {
                    law.identifier,
                    *region_index,
                    *replacement_index,
                    *((law.transition_reference_id,) if law.transition_reference_id else ()),
                }
            )
        ),
        valid=valid,
        residuals={
            "carrier_states": law.carrier_states,
            "carrier_valid": carrier_valid,
            "replacement_rows": replacement_rows,
            "regions": rows,
            "inclusions": inclusion_rows,
            "nonconstant": nonconstant,
            "faithful": faithful,
            "opaque_row_spaces_ignored": bool(law.opaque_row_spaces),
            "valid": valid,
        },
    )


def build_locality_existence_law(fault: str | None = None) -> LocalityPrimitiveLaw:
    root = V4_INTERNAL_ROOT
    states = ("(0,0)", "(0,1)", "(1,0)", "(1,1)")
    s_generators = (
        QMatrix.from_rows(((1,), (1,), (0,), (0,))),
        QMatrix.from_rows(((0,), (0,), (1,), (1,))),
    )
    t_generators = (
        QMatrix.from_rows(((1,), (0,), (1,), (0,))),
        QMatrix.from_rows(((0,), (1,), (0,), (1,))),
    )
    st_generators = tuple(
        QMatrix.from_rows(
            (
                (Fraction(1) if row == column else Fraction(0),)
                for row in range(4)
            ),
            ncols=1,
        )
        for column in range(4)
    )
    flip_target = ReplacementPrimitive(
        root, "replace-outside-S", _q_permutation_from_images((1, 0, 3, 2))
    )
    flip_source = ReplacementPrimitive(
        root, "replace-outside-T", _q_permutation_from_images((2, 3, 0, 1))
    )
    s_replacements = (flip_target.identifier,)
    t_replacements = (flip_source.identifier,)
    if fault == "delete-exterior-replacement":
        s_replacements = ()
    if fault == "merge-exterior-replacements":
        s_generators = t_generators
        s_replacements = t_replacements
    if fault == "supplied-row-spaces":
        s_replacements = ()
    regions = (
        LocalityRegionPrimitive(root, "S", s_generators, s_replacements),
        LocalityRegionPrimitive(root, "T", t_generators, t_replacements),
        LocalityRegionPrimitive(root, "ST", st_generators, ()),
    )
    return LocalityPrimitiveLaw(
        root=root,
        identifier="two-bit-locality-control",
        carrier_states=states,
        regions=regions,
        replacements=(flip_target, flip_source),
        opaque_row_spaces=(
            ("S", qcolumnspace(qhstack(s_generators, nrows=4))),
        )
        if fault == "supplied-row-spaces"
        else (),
    )


@dataclass(frozen=True, slots=True)
class SharedTransitionPrimitive:
    root: str
    identifier: str
    matrix: QMatrix

    def to_data(self) -> dict[str, object]:
        return {"root": self.root, "id": self.identifier, "matrix": self.matrix}


@dataclass(frozen=True, slots=True)
class ComponentTransitionUse:
    root: str
    component_id: str
    transition_id: str
    input_state: QMatrix
    expected_output_state: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "component_id": self.component_id,
            "transition_id": self.transition_id,
            "input_state": self.input_state,
            "expected_output_state": self.expected_output_state,
        }


@dataclass(frozen=True, slots=True)
class LawCandidatePrimitive:
    root: str
    identifier: str
    schema_id: str
    transition_id: str
    measured_component_ids: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "schema_id": self.schema_id,
            "transition_id": self.transition_id,
            "measured_component_ids": self.measured_component_ids,
        }


@dataclass(frozen=True, slots=True)
class LawCalibrationPrimitive:
    root: str
    identifier: str
    input_state: QMatrix
    observed_output_state: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "input_state": self.input_state,
            "observed_output_state": self.observed_output_state,
        }


@dataclass(frozen=True, slots=True)
class CapabilityPrimitiveLaw:
    root: str
    identifier: str
    compiler: PrefixCompilerPrimitive
    quotient_mode: str
    overlap: OverlapPrimitiveLaw
    classical: ClassicalPrimitiveLaw
    comparison: ComparisonPrimitiveLaw
    locality: LocalityPrimitiveLaw
    causal: InfluencePrimitiveLaw
    contact: InfluencePrimitiveLaw
    transitions: tuple[SharedTransitionPrimitive, ...]
    transition_uses: tuple[ComponentTransitionUse, ...]
    candidates: tuple[LawCandidatePrimitive, ...]
    calibration: LawCalibrationPrimitive

    def to_data(self) -> dict[str, object]:
        return {
            "type": "CapabilityPrimitiveLaw",
            "root": self.root,
            "id": self.identifier,
            "compiler": self.compiler,
            "quotient_mode": self.quotient_mode,
            "overlap": self.overlap,
            "classical": self.classical,
            "comparison": self.comparison,
            "locality": self.locality,
            "causal": self.causal,
            "contact": self.contact,
            "transitions": self.transitions,
            "transition_uses": self.transition_uses,
            "candidates": self.candidates,
            "calibration": self.calibration,
        }


@dataclass(frozen=True, slots=True)
class CapabilityEntry:
    name: str
    present: bool
    measurement_payload_sha256: str
    coordinate: str

    def to_data(self) -> dict[str, object]:
        return {
            "name": self.name,
            "present": self.present,
            "measurement_payload_sha256": self.measurement_payload_sha256,
            "coordinate": self.coordinate,
        }


@dataclass(frozen=True, slots=True)
class CapabilityCensus:
    primitive_payload_sha256: str
    entries: tuple[CapabilityEntry, ...]
    dependency_graph: Mapping[str, object]
    law_selection: Mapping[str, object]

    def to_data(self) -> dict[str, object]:
        return {
            "type": "CapabilityCensus",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "entries": self.entries,
            "dependency_graph": self.dependency_graph,
            "law_selection": self.law_selection,
        }


@dataclass(frozen=True, slots=True)
class PrimitiveClassification:
    primitive_payload_sha256: str
    consumed_primitive_ids: tuple[str, ...]
    primary: str
    walls: tuple[str, ...]
    census: CapabilityCensus
    measurements: Mapping[str, object]

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "PrimitiveClassification",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "consumed_primitive_ids": self.consumed_primitive_ids,
            "primary": self.primary,
            "walls": self.walls,
            "census": self.census,
            "measurements": self.measurements,
        }


@dataclass(frozen=True, slots=True)
class ForgedCapabilityCensus:
    """Negative control: nominal census fields never enter the classifier."""

    present: bool
    valid: bool
    primary: str

    def to_data(self) -> dict[str, object]:
        return {
            "type": "ForgedCapabilityCensus",
            "present": self.present,
            "valid": self.valid,
            "primary": self.primary,
        }


def _measurement_hash(value: object) -> str:
    if hasattr(value, "to_data"):
        return canonical_sha256(value.to_data())
    return canonical_sha256(value)


def _connected_components(
    nodes: Sequence[str], edges: Sequence[tuple[str, str]]
) -> tuple[tuple[str, ...], ...]:
    adjacency = {node: set() for node in nodes}
    for left, right in edges:
        if left in adjacency and right in adjacency:
            adjacency[left].add(right)
            adjacency[right].add(left)
    components: list[tuple[str, ...]] = []
    unseen = set(adjacency)
    while unseen:
        start = min(unseen)
        stack = [start]
        reached: set[str] = set()
        while stack:
            node = stack.pop()
            if node in reached:
                continue
            reached.add(node)
            stack.extend(sorted(adjacency[node] - reached, reverse=True))
        unseen -= reached
        components.append(tuple(sorted(reached)))
    return tuple(sorted(components))


def _measure_dependency_graph(
    law: CapabilityPrimitiveLaw,
    component_measurements: Mapping[str, object],
) -> dict[str, object]:
    transition_index_raw, transition_issues = _unique_index(
        law.transitions, "shared-transition"
    )
    transition_index = {
        key: value
        for key, value in transition_index_raw.items()
        if isinstance(value, SharedTransitionPrimitive)
    }
    component_ids = tuple(sorted(component_measurements))
    component_primitives: dict[str, object] = {
        law.compiler.identifier: law.compiler,
        law.overlap.identifier: law.overlap,
        law.classical.identifier: law.classical,
        law.comparison.identifier: law.comparison,
        law.locality.identifier: law.locality,
        law.causal.identifier: law.causal,
        law.contact.identifier: law.contact,
    }
    use_rows: dict[str, object] = {}
    uses_by_component: dict[str, list[ComponentTransitionUse]] = {
        component_id: [] for component_id in component_ids
    }
    edges: list[tuple[str, str]] = []
    nodes: set[str] = set(component_ids)
    valid = not transition_issues
    for use in law.transition_uses:
        transition = transition_index.get(use.transition_id)
        component_known = use.component_id in component_measurements
        transition_known = isinstance(transition, SharedTransitionPrimitive)
        component_primitive = component_primitives.get(use.component_id)
        component_root_matches = bool(
            component_known
            and getattr(component_primitive, "root", None) == law.root
        )
        root_connected = bool(
            use.root == law.root
            and transition_known
            and transition.root == law.root
        )
        actual_reference_id = getattr(
            component_primitive,
            "transition_reference_id",
            None,
        )
        residual: dict[str, object] = {"nonzero_count": None}
        transition_stochastic: dict[str, object] = {"valid": False}
        input_state_valid: dict[str, object] = {"valid": False}
        expected_output_state_valid: dict[str, object] = {"valid": False}
        if transition_known:
            transition_stochastic = _stochastic_matrix_measurement(
                transition.matrix,
                expected_shape=(transition.matrix.nrows, transition.matrix.nrows),
            )
            input_state_valid = _stochastic_matrix_measurement(
                use.input_state,
                expected_shape=(transition.matrix.ncols, 1),
            )
            expected_output_state_valid = _stochastic_matrix_measurement(
                use.expected_output_state,
                expected_shape=(transition.matrix.nrows, 1),
            )
            try:
                residual = _q_residual(
                    qmultiply(transition.matrix, use.input_state),
                    use.expected_output_state,
                )
            except ValueError:
                residual = {"shape_match": False, "nonzero_count": None}
        use_valid = bool(
            component_known
            and component_root_matches
            and transition_known
            and root_connected
            and actual_reference_id == use.transition_id
            and transition_stochastic["valid"]
            and input_state_valid["valid"]
            and expected_output_state_valid["valid"]
            and residual.get("nonzero_count") == 0
        )
        valid = valid and use_valid
        if component_known:
            uses_by_component[use.component_id].append(use)
        if component_known and transition_known:
            nodes.add(use.transition_id)
            edges.append((use.component_id, use.transition_id))
        use_key = f"{use.component_id}->{use.transition_id}"
        use_rows[use_key] = {
            "input_state": use.input_state,
            "expected_output_state": use.expected_output_state,
            "component_root_matches": component_root_matches,
            "component_actual_transition_reference_id": actual_reference_id,
            "transition_stochastic": transition_stochastic,
            "input_state_normalized": input_state_valid,
            "expected_output_state_normalized": expected_output_state_valid,
            "recomputed_residual": residual,
            "valid": use_valid,
        }
    exactly_one_use = all(len(rows) == 1 for rows in uses_by_component.values())
    valid = valid and exactly_one_use
    containment_rows: dict[str, tuple[str, ...]] = {}
    for component_id, measurement in sorted(component_measurements.items()):
        consumed = tuple(getattr(measurement, "consumed_primitive_ids", ()))
        containment_rows[component_id] = consumed
        for primitive_id in consumed:
            nodes.add(primitive_id)
            if primitive_id != component_id:
                edges.append((component_id, primitive_id))
    components = _connected_components(tuple(sorted(nodes)), tuple(edges))
    connected = bool(nodes) and len(components) == 1
    valid = valid and connected
    return {
        "nodes": tuple(sorted(nodes)),
        "edges": tuple(sorted(set(edges))),
        "component_consumed_primitive_ids": containment_rows,
        "transition_use_rows": use_rows,
        "exactly_one_actual_transition_use_per_component": exactly_one_use,
        "connected_components": components,
        "connected": connected,
        "hash_equality_used_as_edge": False,
        "valid": valid,
    }


def _measure_candidate_selection(
    law: CapabilityPrimitiveLaw, component_ids: Sequence[str]
) -> dict[str, object]:
    transition_index_raw, transition_issues = _unique_index(
        law.transitions, "candidate-transition"
    )
    transition_index = {
        key: value
        for key, value in transition_index_raw.items()
        if isinstance(value, SharedTransitionPrimitive)
    }
    expected_components = tuple(sorted(component_ids))
    calibration_size = law.calibration.input_state.nrows
    calibration_input = _stochastic_matrix_measurement(
        law.calibration.input_state, expected_shape=(calibration_size, 1)
    )
    calibration_output = _stochastic_matrix_measurement(
        law.calibration.observed_output_state,
        expected_shape=(calibration_size, 1),
    )
    calibration_valid = bool(
        law.calibration.root == law.root
        and bool(law.calibration.identifier)
        and calibration_input["valid"]
        and calibration_output["valid"]
    )
    transition_rows: dict[str, object] = {}
    transitions_valid = not transition_issues and bool(transition_index)
    for transition_id, transition in sorted(transition_index.items()):
        stochastic = _stochastic_matrix_measurement(
            transition.matrix,
            expected_shape=(calibration_size, calibration_size),
        )
        valid = bool(transition.root == law.root and stochastic["valid"])
        transitions_valid = transitions_valid and valid
        transition_rows[transition_id] = {
            "stochastic": stochastic,
            "root_matches": transition.root == law.root,
            "valid": valid,
        }
    candidate_rows: dict[str, object] = {}
    survivors: list[str] = []
    schemas: set[str] = set()
    identifiers: set[str] = set()
    candidate_transition_ids: list[str] = []
    family_typed = bool(
        len(law.candidates) == 2
        and calibration_valid
        and transitions_valid
    )
    for candidate in law.candidates:
        transition = transition_index.get(candidate.transition_id)
        candidate_transition_ids.append(candidate.transition_id)
        references_complete = tuple(sorted(candidate.measured_component_ids)) == (
            expected_components
        ) and len(set(candidate.measured_component_ids)) == len(
            candidate.measured_component_ids
        )
        identifier_unique = candidate.identifier not in identifiers
        identifiers.add(candidate.identifier)
        schemas.add(candidate.schema_id)
        residual: dict[str, object] = {"nonzero_count": None}
        predicted: QMatrix | None = None
        if isinstance(transition, SharedTransitionPrimitive):
            try:
                predicted = qmultiply(
                    transition.matrix, law.calibration.input_state
                )
                residual = _q_residual(
                    predicted, law.calibration.observed_output_state
                )
            except ValueError:
                pass
        valid = bool(
            candidate.root == law.root
            and isinstance(transition, SharedTransitionPrimitive)
            and transition.root == law.root
            and bool(candidate.schema_id)
            and references_complete
            and identifier_unique
            and transition_rows.get(candidate.transition_id, {}).get("valid")
            and residual.get("nonzero_count") is not None
        )
        zero_residual = valid and residual.get("nonzero_count") == 0
        if zero_residual:
            survivors.append(candidate.identifier)
        family_typed = family_typed and valid
        candidate_rows[candidate.identifier] = {
            "schema_id": candidate.schema_id,
            "transition_id": candidate.transition_id,
            "measured_component_ids": candidate.measured_component_ids,
            "references_every_measured_component": references_complete,
            "predicted_output_state": predicted,
            "observed_output_state": law.calibration.observed_output_state,
            "recomputed_residual": residual,
            "zero_residual": zero_residual,
            "valid": valid,
        }
    same_schema = len(schemas) == 1
    distinct_candidate_transitions = len(set(candidate_transition_ids)) == 2
    unique_survivor = bool(
        family_typed
        and same_schema
        and distinct_candidate_transitions
        and len(survivors) == 1
    )
    return {
        "calibration_id": law.calibration.identifier,
        "calibration_input_state": law.calibration.input_state,
        "calibration_observed_output_state": law.calibration.observed_output_state,
        "calibration_input_normalized": calibration_input,
        "calibration_output_normalized": calibration_output,
        "calibration_valid": calibration_valid,
        "transition_registry_issues": tuple(transition_issues),
        "transition_rows": transition_rows,
        "transitions_valid": transitions_valid,
        "finite_printed_candidate_family": tuple(
            candidate.to_data() for candidate in law.candidates
        ),
        "candidates": candidate_rows,
        "same_frozen_schema": same_schema,
        "candidate_transition_ids_distinct": distinct_candidate_transitions,
        "zero_residual_survivors": tuple(survivors),
        "literal_law_selected_field_consumed": False,
        "unique_zero_residual_survivor": unique_survivor,
        "selected_candidate_id": survivors[0] if unique_survivor else None,
        "valid": unique_survivor,
    }


def _classify_v4_control_law(law: object) -> PrimitiveClassification:
    if not isinstance(law, CapabilityPrimitiveLaw):
        raise ScoreRefusal(
            "capability classifier requires one immutable CapabilityPrimitiveLaw"
        )
    primitive_hash = canonical_sha256(law.to_data())
    compiler = measure_prefix_compiler(law.compiler, quotient_mode=law.quotient_mode)
    overlap = measure_overlap_primitive_law(law.overlap)
    classical = measure_classical_primitive_law(law.classical)
    comparison = measure_comparison_primitive_law(law.comparison)
    locality = measure_locality_primitive_law(law.locality)
    causal = measure_influence_primitive_law(law.causal)
    contact = measure_influence_primitive_law(law.contact)
    roots_valid = bool(
        law.root
        and law.identifier
        and all(
            root == law.root
            for root in (
                law.compiler.root,
                law.overlap.root,
                law.classical.root,
                law.comparison.root,
                law.locality.root,
                law.causal.root,
                law.contact.root,
                law.calibration.root,
            )
        )
    )
    component_measurements: dict[str, object] = {
        law.compiler.identifier: compiler,
        law.overlap.identifier: overlap,
        law.classical.identifier: classical,
        law.comparison.identifier: comparison,
        law.locality.identifier: locality,
        law.causal.identifier: causal,
        law.contact.identifier: contact,
    }
    dependency_graph = _measure_dependency_graph(law, component_measurements)
    law_selection = _measure_candidate_selection(
        law, tuple(component_measurements)
    )
    entries = (
        CapabilityEntry(
            "raw_boolean_normalization",
            compiler.normalization_valid,
            _measurement_hash(compiler),
            "NORMALIZED" if compiler.normalization_valid else "INCONSISTENT",
        ),
        CapabilityEntry(
            "raw_atomlessness",
            compiler.raw_atomless_valid,
            _measurement_hash(compiler),
            "RAW-ATOMLESS" if compiler.raw_atomless_valid else "UNCONSTRUCTED",
        ),
        CapabilityEntry(
            "boundary_gluing_package",
            overlap.valid and roots_valid and dependency_graph["valid"],
            _measurement_hash(overlap),
            "GLUING-DIAGNOSTIC-SELECTED"
            if overlap.valid and roots_valid and dependency_graph["valid"]
            else "UNCONSTRUCTED",
        ),
        CapabilityEntry(
            "horizontal_process",
            classical.valid,
            _measurement_hash(classical),
            classical.coordinate,
        ),
        CapabilityEntry(
            "future_profile_complete",
            compiler.future_complete,
            _measurement_hash(compiler),
            "COMPLETE-GENERATED"
            if compiler.future_complete
            else "FINITE-CATALOGUE",
        ),
        CapabilityEntry(
            "regional_congruence",
            compiler.congruence_valid,
            _measurement_hash(compiler),
            "CONGRUENCE" if compiler.congruence_valid else "UNCONSTRUCTED",
        ),
        CapabilityEntry(
            "post_quotient_atomlessness",
            compiler.quotient_atomless_valid,
            _measurement_hash(compiler),
            "PHYSICAL-IMAGE-ATOMLESS"
            if compiler.quotient_atomless_valid
            else "UNCONSTRUCTED",
        ),
        CapabilityEntry(
            "comparison_selected",
            comparison.valid,
            _measurement_hash(comparison),
            "DERIVED" if comparison.valid else "PRICED",
        ),
        CapabilityEntry(
            "dynamic_locality",
            locality.valid,
            _measurement_hash(locality),
            "DYNAMIC-FAITHFUL" if locality.valid else "FAIL",
        ),
        CapabilityEntry(
            "causal_order",
            causal.present and causal.role == "causal_order",
            _measurement_hash(causal),
            "DERIVED" if causal.present else "PRICED",
        ),
        CapabilityEntry(
            "generated_contact",
            contact.present and contact.role == "generated_contact",
            _measurement_hash(contact),
            "DERIVED" if contact.present else "PRICED",
        ),
        CapabilityEntry(
            "law_selected",
            bool(law_selection["valid"]),
            canonical_sha256(law_selection),
            "SELECTED" if law_selection["valid"] else "UNSELECTED",
        ),
    )
    census = CapabilityCensus(
        primitive_payload_sha256=primitive_hash,
        entries=entries,
        dependency_graph=dependency_graph,
        law_selection=law_selection,
    )
    present = {entry.name: entry.present for entry in entries}
    if not present["raw_boolean_normalization"]:
        primary = "APR-INCONSISTENT"
        walls = ("full-cone normalization is absent or inconsistent",)
    elif not present["raw_atomlessness"]:
        primary = "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA"
        walls = ("no nonzero raw regional split was constructed",)
    elif not present["boundary_gluing_package"]:
        primary = "APR-BLOCKED-AT-BOUNDARY-GLUING"
        walls = (
            "missing computed simultaneous-gluing diagnostic selector or connected primitive graph",
        )
    elif not present["horizontal_process"]:
        primary = "APR-BLOCKED-AT-TWO-ARROW-TYPING"
        walls = ("no validated typed horizontal reachability-control process",)
    elif not present["future_profile_complete"]:
        primary = "APR-BLOCKED-AT-FUTURE-PROFILE-COMPLETENESS"
        walls = ("no complete target-independent probe compiler",)
    elif not present["regional_congruence"]:
        primary = "APR-BLOCKED-AT-REGIONAL-CONGRUENCE"
        walls = ("profile equivalence is not a generated regional congruence",)
    elif not present["post_quotient_atomlessness"]:
        primary = "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA"
        walls = ("the claimed quotient has no nonzero proper split certificate",)
    elif not present["comparison_selected"]:
        primary = "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED"
        walls = ("comparison system remains law data",)
    elif not present["dynamic_locality"]:
        primary = (
            "APR-COMPARISON-QUOTIENT-CONSTRUCTED-BUT-DYNAMICAL-LOCALITY-FAILS"
        )
        walls = ("dynamic regional-support requirements fail",)
    elif not present["causal_order"]:
        primary = (
            "APR-DYNAMIC-REGIONAL-REFERENT-CONSTRUCTED-BUT-CAUSAL-ORDER-PRICED"
        )
        walls = ("causal schedule and delayed response are not generated",)
    elif not present["generated_contact"]:
        primary = (
            "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED"
        )
        walls = ("missing generated_contact",)
    elif not present["law_selected"]:
        primary = (
            "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED"
        )
        walls = ("one joint law remains unselected",)
    else:
        primary = "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED"
        walls = ()
    consumed = tuple(
        sorted(
            {
                law.identifier,
                law.calibration.identifier,
                *(identifier for measurement in component_measurements.values() for identifier in getattr(measurement, "consumed_primitive_ids", ())),
                *(transition.identifier for transition in law.transitions),
                *(candidate.identifier for candidate in law.candidates),
            }
        )
    )
    return PrimitiveClassification(
        primitive_payload_sha256=primitive_hash,
        consumed_primitive_ids=consumed,
        primary=primary,
        walls=walls,
        census=census,
        measurements={
            "compiler": compiler,
            "overlap_simultaneous_gluing_diagnostic": overlap,
            "classical_internal_reachability_control": classical,
            "comparison": comparison,
            "locality": locality,
            "causal_order": causal,
            "generated_contact": contact,
            "dependency_graph": dependency_graph,
            "law_selection_within_finite_test_family": law_selection,
            "candidate_fundamental_law_status": (
                "UNCONSTRUCTED-INDIVISIBLE-STOCHASTIC-RELATIONAL-TRANSITION-LAW"
            ),
        },
    )


def build_capability_primitive_law(
    fault: str | None = None,
) -> CapabilityPrimitiveLaw:
    root = V4_INTERNAL_ROOT
    compiler_mode = "uniform-prefix-compiler"
    split_mode = "symbolic-prefix-split"
    if fault == "missing-normalization":
        compiler_mode = "missing-normalization-constructor"
    elif fault == "seed-whitelist":
        compiler_mode = "seed-whitelist-compiler"
    elif fault == "missing-raw-atomlessness":
        split_mode = "missing-symbolic-split"
    seed_regions = (
        PrefixRegion.cylinder("0"),
        PrefixRegion.cylinder("1"),
        PrefixRegion.cylinder("00"),
    )
    whitelist_regions = tuple(
        dict.fromkeys(
            seed_regions
            + tuple(region.complement() for region in seed_regions)
            + (PrefixRegion.zero(), PrefixRegion.one())
        )
    )
    compiler = PrefixCompilerPrimitive(
        root=root,
        identifier="uniform-prefix-compiler",
        mode=compiler_mode,
        seed_regions=seed_regions,
        whitelist_regions=whitelist_regions,
        split_mode=split_mode,
    )
    quotient_mode = "literal-prefix-algebra"
    if fault == "scalar-volume-noncongruence":
        quotient_mode = "scalar-volume-equivalence"
    elif fault == "ultrafilter-atomic-quotient":
        quotient_mode = "ultrafilter-two-element-atomic-quotient"
    overlap_fault = fault if fault in {
        "missing-markov-selector",
        "both-markov-survive",
        "extra-overlap-candidate",
        "nonuniform-shared-marginals",
    } else None
    classical_fault = (
        "opaque-replacement" if fault == "missing-classical-witness" else None
    )
    comparison_fault = fault if fault in {
        "altered-comparison-permutation",
        "negative-comparison-transition",
        "nonstate-comparison-calibration",
        "duplicate-comparison-cut",
    } else None
    locality_fault = fault if fault in {
        "delete-exterior-replacement", "merge-exterior-replacements"
    } else None
    causal_fault = (
        "identical-alternatives" if fault == "missing-causal-order" else None
    )
    contact_fault = (
        "identity-propagation" if fault == "missing-generated-contact" else None
    )
    overlap = build_overlap_existence_law(overlap_fault)
    classical = build_classical_existence_law(classical_fault)
    comparison = build_comparison_existence_law(comparison_fault)
    locality = build_locality_existence_law(locality_fault)
    causal = build_influence_existence_law(contact=False, fault=causal_fault)
    contact = build_influence_existence_law(contact=True, fault=contact_fault)
    components = (
        compiler.identifier,
        overlap.identifier,
        classical.identifier,
        comparison.identifier,
        locality.identifier,
        causal.identifier,
        contact.identifier,
    )
    transition_i_matrix = QMatrix.identity(2)
    if fault == "negative-candidate-transition":
        transition_i_matrix = QMatrix.from_rows(((1, -1), (0, 2)))
    transition_i = SharedTransitionPrimitive(
        root, "candidate-transition-I", transition_i_matrix
    )
    transition_x = SharedTransitionPrimitive(
        root, "shared-transition-X", QMatrix.from_rows(((0, 1), (1, 0)))
    )
    transitions: tuple[SharedTransitionPrimitive, ...] = (
        transition_i, transition_x
    )
    uses = tuple(
        ComponentTransitionUse(
            root,
            component_id,
            transition_x.identifier,
            QMatrix.from_rows(((1,), (0,))),
            QMatrix.from_rows(((0,), (1,))),
        )
        for component_id in components
    )
    if fault == "disconnected-byte-identical-transition":
        clone = SharedTransitionPrimitive(
            root, "byte-identical-distinct-transition-X", transition_x.matrix
        )
        transitions = transitions + (clone,)
        contact = replace(contact, transition_reference_id=clone.identifier)
        uses = tuple(
            ComponentTransitionUse(
                row.root,
                row.component_id,
                clone.identifier if row.component_id == contact.identifier else row.transition_id,
                row.input_state,
                row.expected_output_state,
            )
            for row in uses
        )
    candidate_schema = (
        "" if fault == "empty-candidate-schema" else "complete-v4-test-law-bundle"
    )
    candidates = (
        LawCandidatePrimitive(
            root,
            "L_I",
            candidate_schema,
            transition_i.identifier,
            tuple(sorted(components)),
        ),
        LawCandidatePrimitive(
            root,
            "L_X",
            candidate_schema,
            transition_x.identifier,
            tuple(sorted(components)),
        ),
    )
    if fault == "zero-zero-residual-candidates":
        candidates = (
            candidates[0],
            LawCandidatePrimitive(
                root,
                "L_I_2",
                "complete-v4-test-law-bundle",
                transition_i.identifier,
                tuple(sorted(components)),
            ),
        )
    elif fault == "two-zero-residual-candidates":
        candidates = (
            candidates[1],
            LawCandidatePrimitive(
                root,
                "L_X_2",
                "complete-v4-test-law-bundle",
                transition_x.identifier,
                tuple(sorted(components)),
            ),
        )
    elif fault == "candidate-missing-component-reference":
        candidates = (
            candidates[0],
            LawCandidatePrimitive(
                root,
                "L_X",
                "complete-v4-test-law-bundle",
                transition_x.identifier,
                tuple(sorted(components[:-1])),
            ),
        )
    calibration_input = QMatrix.from_rows(((1,), (0,)))
    calibration_output = QMatrix.from_rows(((0,), (1,)))
    if fault == "nonstate-law-calibration":
        calibration_input = QMatrix.from_rows(((2,), (-1,)))
        calibration_output = qmultiply(transition_x.matrix, calibration_input)
    calibration = LawCalibrationPrimitive(
        root,
        "delta-zero-to-delta-one-calibration",
        calibration_input,
        calibration_output,
    )
    return CapabilityPrimitiveLaw(
        root=root,
        identifier="complete-v4-internal-capability-law",
        compiler=compiler,
        quotient_mode=quotient_mode,
        overlap=overlap,
        classical=classical,
        comparison=comparison,
        locality=locality,
        causal=causal,
        contact=contact,
        transitions=transitions,
        transition_uses=uses,
        candidates=candidates,
        calibration=calibration,
    )


def _v4_witness_record(primitive: object, measurement: object) -> dict[str, object]:
    primitive_data = primitive.to_data() if hasattr(primitive, "to_data") else primitive
    measurement_data = (
        measurement.to_data() if hasattr(measurement, "to_data") else measurement
    )
    coordinate = None
    for name in ("coordinate", "role", "primary", "present", "valid"):
        if hasattr(measurement, name):
            coordinate = getattr(measurement, name)
            break
    return {
        "primitive": primitive_data,
        "primitive_sha256": canonical_sha256(primitive_data),
        "measurement": measurement_data,
        "measurement_sha256": canonical_sha256(measurement_data),
        "derived_coordinate_or_status": coordinate,
    }


def run_v4_selftests() -> dict[str, object]:
    checks: list[str] = []
    witnesses: dict[str, object] = {}

    region = PrefixRegion.from_words(("00", "01", "1"))
    left, right = PrefixRegion.cylinder("0").atomless_bipartition()
    _require(
        region.is_one()
        and left.disjoint(right)
        and left.join(right) == PrefixRegion.cylinder("0")
        and bernoulli_mass(PrefixRegion.one(), Fraction(1, 3)) == 1,
        "exact prefix Boolean/valuation control",
    )
    checks.append("exact-prefix-boolean-and-valuation")

    tree = expression_to_tree(parse_expression("node(q,empty_tree,empty_tree)"))
    event = PrefixRegion.cylinder("0")
    cells = tree_branch_cells(tree, {"q": event}, support=event)
    partition = branch_partition_evidence(cells, event)
    _require(
        partition["is_partition"]
        and cells["0"].is_zero()
        and cells["1"] == event,
        "semantic branch partition/zero port",
    )
    witnesses["semantic_branch_partition"] = {
        "cells": cells,
        "partition": partition,
    }
    checks.append("semantic-tree-partition-and-zero-port")

    refused_mixed = False
    try:
        validate_mixed_expression(
            parse_expression("intrinsic_replace(r,node(q,empty_tree,empty_tree))"),
            (
                "mixed_tree := empty_tree",
                "mixed_tree := replace(replacement,mixed_tree)",
                "mixed_tree := node(question,port_0:mixed_tree,port_1:mixed_tree)",
            ),
        )
    except ScoreRefusal:
        refused_mixed = True
    _require(refused_mixed, "undeclared mixed constructor accepted")
    checks.append("mixed-constructor-refusal")

    first_cospan = FiniteCospan(
        "first",
        ("a",),
        ("b",),
        ("ain", "mid"),
        (("a", "ain"),),
        (("b", "mid"),),
        (("ain", "mid"),),
    )
    second_cospan = FiniteCospan(
        "second",
        ("b",),
        ("c",),
        ("mid2", "cout"),
        (("b", "mid2"),),
        (("c", "cout"),),
        (("mid2", "cout"),),
    )
    whole_cospan = FiniteCospan(
        "whole",
        ("a",),
        ("c",),
        ("ain", "mid", "cout"),
        (("a", "ain"),),
        (("c", "cout"),),
        (("ain", "mid"), ("mid", "cout")),
    )
    composed_cospan = compose_cospans((first_cospan, second_cospan))
    _require(
        boundary_fixed_isomorphic(composed_cospan, singleton_quotient(whole_cospan)),
        "finite cospan pushout was not constructed",
    )
    witnesses["finite_pushout"] = {
        "composed": composed_cospan,
        "whole": singleton_quotient(whole_cospan),
    }
    checks.append("finite-pushout-vs-validation-and-tagged-union")

    classical_positive = build_classical_existence_law()
    classical_measurement = measure_classical_primitive_law(classical_positive)
    _require(
        classical_measurement.valid
        and classical_measurement.coordinate == "HORIZONTAL-CLASSICAL"
        and measure_horizontal_process_package(
            classical_positive, static_response_available=True
        )["coordinate"]
        == "HORIZONTAL-CLASSICAL",
        "typed classical positive did not reach its coordinate",
    )
    witnesses["classical_positive"] = _v4_witness_record(
        classical_positive, classical_measurement
    )
    checks.append("typed-classical-positive-coordinate")

    classical_fault_groups = {
        "frontier_composition": (
            "frontier-domain-mismatch",
            "frontier-codomain-mismatch",
            "dropped-zero-port",
            "missing-intermediate",
            "one-standalone-occurrence",
            "wrong-whole",
            "altered-cut",
        ),
        "stochastic": ("negative-entry", "nonconserving"),
        "tensor": (
            "wrong-tensor-frontier",
            "wrong-unit",
            "wrong-associator",
            "wrong-symmetry",
            "wrong-interchange",
        ),
        "naturality_identity": (
            "identity-naturality",
            "changed-target-vertical",
            "rank-deficient-vertical",
            "disconnected-naturality",
            "duplicate-identity",
            "missing-identity",
        ),
    }
    classical_drop_rows: dict[str, object] = {}
    for fault_group, fault_names in classical_fault_groups.items():
        for fault_name in fault_names:
            primitive = build_classical_existence_law(fault_name)
            measurement = measure_classical_primitive_law(primitive)
            _require(not measurement.valid, f"classical fault survived: {fault_name}")
            classical_drop_rows[fault_name] = _v4_witness_record(
                primitive, measurement
            )
        checks.append(
            {
                "frontier_composition": "typed-classical-frontier-and-composition-drops",
                "stochastic": "typed-classical-stochastic-and-zero-port-drops",
                "tensor": "typed-classical-tensor-law-drops",
                "naturality_identity": "typed-classical-naturality-and-identity-drops",
            }[fault_group]
        )
    opaque_replacement = build_classical_existence_law("opaque-replacement")
    opaque_measurement = measure_classical_primitive_law(opaque_replacement)
    unused_proof = build_classical_existence_law("unused-proof-change")
    unused_measurement = measure_classical_primitive_law(unused_proof)
    mapping_measurement = measure_horizontal_process_package(
        {"present": True, "valid": True, "lhs": "same", "rhs": "same"},
        static_response_available=True,
    )
    _require(
        not opaque_measurement.valid
        and unused_measurement.valid
        and mapping_measurement["coordinate"] == "STATIC-RESPONSE-ONLY"
        and mapping_measurement["rejected_asserted_mapping"],
        "opaque copy oracle or mapping bypassed classical typing",
    )
    classical_drop_rows["opaque-replacement"] = _v4_witness_record(
        opaque_replacement, opaque_measurement
    )
    classical_drop_rows["unused-proof-change-inert"] = _v4_witness_record(
        unused_proof, unused_measurement
    )
    witnesses["classical_drops"] = classical_drop_rows
    checks.append("typed-classical-opaque-proof-inert-and-copy-refusal")

    quantum_positive = build_quantum_existence_law()
    quantum_measurement = measure_quantum_primitive_law(quantum_positive)
    _require(
        quantum_measurement.valid
        and quantum_measurement.coordinate == "HORIZONTAL-QUANTUM"
        and quantum_measurement.residuals["division"]["completeness_residual"][
            "nonzero_count"
        ]
        == 0
        and quantum_measurement.residuals["division"][
            "dilation_isometry_residual"
        ]["nonzero_count"]
        == 0,
        "typed quantum positive/completeness/dilation failed",
    )
    witnesses["quantum_positive"] = _v4_witness_record(
        quantum_positive, quantum_measurement
    )
    checks.append("typed-quantum-positive-coordinate-and-unit-normalization")

    quantum_history_faults = (
        "free-gram-no-histories",
        "different-root-history",
        "different-frontier-history",
        "nonpositive-state",
    )
    quantum_division_faults = (
        "total-2I",
        "nonunit-total",
        "missing-flags",
        "disconnected-recovery",
        "no-nonidentity-continuation",
        "nonclosed-continuation-semigroup",
        "different-cut-arrows",
        "arbitrary-equal-payload",
    )
    quantum_interference_faults = (
        "zero-cross",
        "no-probability-difference",
        "transpose-phase-control",
    )
    quantum_drop_rows: dict[str, object] = {}
    for fault_name in quantum_history_faults:
        primitive = build_quantum_existence_law(fault_name)
        measurement = measure_quantum_primitive_law(primitive)
        _require(
            not measurement.valid
            and measurement.coordinate == "HORIZONTAL-CLASSICAL",
            f"quantum history fault survived: {fault_name}",
        )
        quantum_drop_rows[fault_name] = _v4_witness_record(primitive, measurement)
    negative_free = build_quantum_existence_law("negative-free-gram")
    negative_free_measurement = measure_quantum_primitive_law(negative_free)
    _require(
        negative_free_measurement.valid
        and negative_free_measurement.residuals["gram_operator_proof"][
            "free_gram_ignored"
        ],
        "free negative Gram was consumed instead of ignored",
    )
    quantum_drop_rows["negative-free-gram-ignored"] = _v4_witness_record(
        negative_free, negative_free_measurement
    )
    checks.append("typed-quantum-history-gram-and-state-drops")

    for fault_name in quantum_division_faults:
        primitive = build_quantum_existence_law(fault_name)
        measurement = measure_quantum_primitive_law(primitive)
        _require(not measurement.valid, f"quantum division fault survived: {fault_name}")
        quantum_drop_rows[fault_name] = _v4_witness_record(primitive, measurement)
    checks.append("typed-quantum-division-flag-and-cut-drops")

    for fault_name in quantum_interference_faults:
        primitive = build_quantum_existence_law(fault_name)
        measurement = measure_quantum_primitive_law(primitive)
        _require(
            not measurement.valid,
            f"quantum interference/phase fault survived: {fault_name}",
        )
        quantum_drop_rows[fault_name] = _v4_witness_record(primitive, measurement)
    _require(
        quantum_measurement.residuals["interference"]["probability_difference"]
        == GONE / GaussianRational(2)
        and quantum_measurement.residuals["gram_operator_proof"][
            "operator_identity"
        ]["nonzero_count"]
        == 0
        and quantum_measurement.residuals["phase_conjugation_control"][
            "P_adjoint_P_residual"
        ]["nonzero_count"]
        == 0
        and quantum_measurement.residuals["phase_conjugation_control"][
            "P_transpose_P_residual"
        ]["nonzero_count"]
        > 0,
        "quantum interference/conjugation controls were not load-bearing",
    )
    witnesses["quantum_drops"] = quantum_drop_rows
    checks.append("typed-quantum-interference-phase-conjugation-controls")

    causal_positive = build_influence_existence_law(contact=False)
    causal_measurement = measure_influence_primitive_law(causal_positive)
    causal_faults = (
        "identical-alternatives",
        "unused-alternative",
        "reader-before",
        "supplied-tables",
        "noncomposable-carrier",
        "disconnected-root",
        "provenance-only",
    )
    causal_drop_rows: dict[str, object] = {}
    for fault_name in causal_faults:
        primitive = build_influence_existence_law(contact=False, fault=fault_name)
        measurement = measure_influence_primitive_law(primitive)
        _require(not measurement.present, f"causal fault survived: {fault_name}")
        causal_drop_rows[fault_name] = _v4_witness_record(primitive, measurement)
    _require(
        causal_measurement.present
        and causal_measurement.role == "causal_order"
        and len({canonical_sha256(row) for _name, row in causal_measurement.responses})
        == 2,
        "generated causal-order positive failed",
    )
    witnesses["causal_positive"] = _v4_witness_record(
        causal_positive, causal_measurement
    )
    witnesses["causal_drops"] = causal_drop_rows
    checks.append("generated-causal-order-positive-and-drops")

    contact_positive = build_influence_existence_law(contact=True)
    contact_measurement = measure_influence_primitive_law(contact_positive)
    _require(
        contact_measurement.present
        and contact_measurement.role == "generated_contact"
        and contact_measurement.responses[0][1]
        == QMatrix.from_rows(((1,), (0,)))
        and contact_measurement.responses[1][1]
        == QMatrix.from_rows(((0,), (1,)))
        and contact_measurement.residuals["generated_contact"][
            "target_reader_factorization_residual"
        ]["nonzero_count"]
        == 0,
        "CNOT target-reader contact chain failed",
    )
    witnesses["contact_positive"] = _v4_witness_record(
        contact_positive, contact_measurement
    )
    checks.append("generated-contact-cnot-target-reader-positive")

    contact_faults = (
        "identical-alternatives",
        "unused-alternative",
        "reader-before",
        "supplied-tables",
        "noncomposable-carrier",
        "disconnected-root",
        "overlapping-or-labeled-supports",
        "target-acting-intervention",
        "source-consuming-reader",
        "identity-propagation",
        "provenance-only",
    )
    contact_drop_rows: dict[str, object] = {}
    for fault_name in contact_faults:
        primitive = build_influence_existence_law(contact=True, fault=fault_name)
        measurement = measure_influence_primitive_law(primitive)
        _require(not measurement.present, f"contact fault survived: {fault_name}")
        contact_drop_rows[fault_name] = _v4_witness_record(primitive, measurement)
    _require(
        not measure_generated_influence_package(
            causal_positive, require_nonoverlap_contact=True
        )["present"]
        and not measure_generated_influence_package(
            contact_positive, require_nonoverlap_contact=False
        )["present"],
        "causal order aliased generated contact",
    )
    witnesses["contact_drops"] = contact_drop_rows
    checks.append("generated-contact-locality-propagation-and-provenance-drops")

    capability_positive = build_capability_primitive_law()
    capability_measurement = _classify_v4_control_law(capability_positive)
    compiler_measurement = capability_measurement.measurements["compiler"]
    _require(
        isinstance(compiler_measurement, CompilerLawMeasurement)
        and compiler_measurement.normalization_valid
        and compiler_measurement.raw_atomless_valid
        and compiler_measurement.future_complete
        and compiler_measurement.residuals["heldout_future"]["not_in_seed_list"],
        "uniform compiler normalization/atomlessness/heldout failed",
    )
    witnesses["capability_positive"] = _v4_witness_record(
        capability_positive, capability_measurement
    )
    checks.append("primitive-compiler-normalization-atomlessness-heldout")

    classifier_drop_expectations = {
        "missing-normalization": "APR-INCONSISTENT",
        "missing-raw-atomlessness": "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA",
        "missing-markov-selector": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "both-markov-survive": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "extra-overlap-candidate": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "nonuniform-shared-marginals": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "missing-classical-witness": "APR-BLOCKED-AT-TWO-ARROW-TYPING",
        "seed-whitelist": "APR-BLOCKED-AT-FUTURE-PROFILE-COMPLETENESS",
        "scalar-volume-noncongruence": "APR-BLOCKED-AT-REGIONAL-CONGRUENCE",
        "ultrafilter-atomic-quotient": "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA",
        "altered-comparison-permutation": "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED",
        "negative-comparison-transition": "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED",
        "nonstate-comparison-calibration": "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED",
        "duplicate-comparison-cut": "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED",
        "delete-exterior-replacement": "APR-COMPARISON-QUOTIENT-CONSTRUCTED-BUT-DYNAMICAL-LOCALITY-FAILS",
        "merge-exterior-replacements": "APR-COMPARISON-QUOTIENT-CONSTRUCTED-BUT-DYNAMICAL-LOCALITY-FAILS",
        "disconnected-byte-identical-transition": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "missing-causal-order": "APR-DYNAMIC-REGIONAL-REFERENT-CONSTRUCTED-BUT-CAUSAL-ORDER-PRICED",
        "missing-generated-contact": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "zero-zero-residual-candidates": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "two-zero-residual-candidates": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "candidate-missing-component-reference": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "negative-candidate-transition": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "nonstate-law-calibration": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "empty-candidate-schema": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
    }
    classifier_drop_rows: dict[str, object] = {}
    classifier_drop_measurements: dict[str, PrimitiveClassification] = {}
    for fault_name, expected_primary in classifier_drop_expectations.items():
        primitive = build_capability_primitive_law(fault_name)
        measurement = _classify_v4_control_law(primitive)
        _require(
            measurement.primary == expected_primary,
            f"classifier drop {fault_name} gave {measurement.primary}",
        )
        classifier_drop_rows[fault_name] = _v4_witness_record(
            primitive, measurement
        )
        classifier_drop_measurements[fault_name] = measurement
    overlap_positive = capability_measurement.measurements[
        "overlap_simultaneous_gluing_diagnostic"
    ]
    _require(
        isinstance(overlap_positive, OverlapLawMeasurement)
        and overlap_positive.valid
        and overlap_positive.selected_candidate_id == "uniform-independent"
        and len(
            overlap_positive.residuals["zero_markov_residual_candidates"]
        )
        == 1,
        "Markov overlap selector did not select uniquely by cell residuals",
    )
    checks.append("primitive-overlap-markov-selector-drops")

    _require(
        classifier_drop_measurements["scalar-volume-noncongruence"].primary
        == "APR-BLOCKED-AT-REGIONAL-CONGRUENCE"
        and classifier_drop_measurements["ultrafilter-atomic-quotient"].primary
        == "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA"
        and classifier_drop_measurements["altered-comparison-permutation"].primary
        == "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED",
        "congruence/quotient/comparison precedence moved",
    )
    checks.append("primitive-congruence-quotient-comparison-drops")

    locality_positive = capability_measurement.measurements["locality"]
    _require(
        isinstance(locality_positive, LocalityLawMeasurement)
        and locality_positive.valid
        and locality_positive.residuals["inclusions"][
            "strict_inclusions_and_noninclusions"
        ],
        "generated Kin/Dyn locality ladder failed",
    )
    checks.append("primitive-locality-generated-space-drops")

    dependency_positive = capability_measurement.measurements["dependency_graph"]
    _require(
        dependency_positive["valid"]
        and dependency_positive["connected"]
        and not classifier_drop_measurements[
            "disconnected-byte-identical-transition"
        ].census.dependency_graph["connected"],
        "connected consumed-ID graph failed to reject cloned transition ID",
    )
    forgery_refusals: list[dict[str, object]] = []
    for forged in (
        {"present": True, "valid": True, "law_selected": True},
        ForgedCapabilityCensus(
            True, True, "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED"
        ),
    ):
        refused = False
        reason = ""
        try:
            _classify_v4_control_law(forged)
        except ScoreRefusal as exc:
            refused = True
            reason = str(exc)
        _require(refused, "forged primitive census reached classifier")
        forgery_refusals.append(
            {
                "forged_payload": (
                    forged.to_data() if hasattr(forged, "to_data") else forged
                ),
                "forged_payload_sha256": canonical_sha256(
                    forged.to_data() if hasattr(forged, "to_data") else forged
                ),
                "refused": refused,
                "reason": reason,
            }
        )
    bare_census_refused = False
    try:
        classify_capability_census({"raw_boolean_normalization": {"present": True}})
    except ScoreRefusal:
        bare_census_refused = True
    _require(bare_census_refused, "plain mapping entered legacy census classifier")
    witnesses["classifier_forgery_refusals"] = forgery_refusals
    checks.append("primitive-dependency-graph-and-forgery-refusals")

    _require(
        capability_measurement.primary
        == "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED"
        and classifier_drop_measurements["missing-generated-contact"].walls
        == ("missing generated_contact",)
        and classifier_drop_measurements[
            "zero-zero-residual-candidates"
        ].census.law_selection["zero_residual_survivors"]
        == (),
        "law selection or generated-contact-only primary failed",
    )
    witnesses["classifier_drops"] = classifier_drop_rows
    checks.append("primitive-law-selection-and-contact-only-primary")

    ontology_rows: dict[str, object] = {}
    observed_roles: list[str] = []
    for level in ONTOLOGY_ROLES:
        primitive = build_ontology_existence_law(level)
        measurement = measure_ontology_primitive_law(primitive)
        observed_roles.append(measurement.role)
        ontology_rows[level] = _v4_witness_record(primitive, measurement)
    _require(
        tuple(observed_roles) == ONTOLOGY_ROLES,
        f"ontology ladder not reachable: {observed_roles}",
    )
    ontology_demotion_expectations = {
        "missing-conditioning": "STATIC-RESPONSE",
        "missing-writer": "FIXED-ALGEBRA-CONDITIONING",
        "missing-reader": "FIXED-ALGEBRA-CONDITIONING",
        "missing-continuation": "FIXED-ALGEBRA-CONDITIONING",
        "nonclosed-continuation-semigroup": "FIXED-ALGEBRA-CONDITIONING",
        "missing-rewrite": "RECORD-WRITING-ON-FIXED-ALGEBRA",
        "target-specific-compiler": "RECORD-WRITING-ON-FIXED-ALGEBRA",
    }
    ontology_drop_rows: dict[str, object] = {}
    for fault_name, expected_role in ontology_demotion_expectations.items():
        primitive = build_ontology_existence_law(
            "REGION-REWRITING", fault=fault_name
        )
        measurement = measure_ontology_primitive_law(primitive)
        _require(
            measurement.role == expected_role,
            f"ontology deletion {fault_name} gave {measurement.role}",
        )
        ontology_drop_rows[fault_name] = _v4_witness_record(
            primitive, measurement
        )
    checks.append("ontology-role-ladder-and-load-bearing-demotions")

    ontology_attack_expectations = {
        "identity-writer-label": "FIXED-ALGEBRA-CONDITIONING",
        "changed-table-no-rewrite": "RECORD-WRITING-ON-FIXED-ALGEBRA",
        "identity-rewrite-label": "RECORD-WRITING-ON-FIXED-ALGEBRA",
    }
    for fault_name, expected_role in ontology_attack_expectations.items():
        primitive = build_ontology_existence_law(
            "REGION-REWRITING", fault=fault_name
        )
        measurement = measure_ontology_primitive_law(primitive)
        _require(
            measurement.role == expected_role,
            f"ontology forged action {fault_name} promoted",
        )
        ontology_drop_rows[fault_name] = _v4_witness_record(
            primitive, measurement
        )
    candidate_a = build_ontology_existence_law(
        "REGION-REWRITING", candidate="POSTULATED-CANDIDATE-RELATIONAL-WEB"
    )
    candidate_b = build_ontology_existence_law(
        "REGION-REWRITING", candidate="RENAMED-UNMEASURED-PROPOSAL"
    )
    candidate_none = build_ontology_existence_law("REGION-REWRITING")
    candidate_measurements = tuple(
        measure_ontology_primitive_law(row)
        for row in (candidate_a, candidate_b, candidate_none)
    )
    _require(
        len({row.primitive_payload_sha256 for row in candidate_measurements}) == 3
        and len({row.role for row in candidate_measurements}) == 1
        and len(
            {
                canonical_sha256(row.residuals)
                for row in candidate_measurements
            }
        )
        == 1,
        "ontology candidate changed measured coordinate/residuals",
    )
    ontology_rows["candidate_invariance"] = tuple(
        _v4_witness_record(primitive, measurement)
        for primitive, measurement in zip(
            (candidate_a, candidate_b, candidate_none), candidate_measurements
        )
    )
    witnesses["ontology_positive_ladder"] = ontology_rows
    witnesses["ontology_drops"] = ontology_drop_rows
    checks.append("ontology-writer-rewrite-attacks-and-candidate-invariance")

    exposure_payload = {
        "blinding_status": BLINDING_STATUS,
        "exposure_debt": EXPOSURE_DEBT,
        "v4_source_frozen_before_v4_run": True,
    }
    validate_v4_exposure_fields(exposure_payload)
    tampered_exposure = dict(exposure_payload)
    tampered_exposure["blinding_status"] = "BLIND"
    exposure_refused = False
    try:
        validate_v4_exposure_fields(tampered_exposure)
    except ScoreRefusal:
        exposure_refused = True
    law_scope = (
        "ISP's candidate ontology is one actual, law-sufficient relational "
        "configuration; its missing fundamental dynamics is an indivisible "
        "stochastic law of transition probabilities between complete "
        "configurations, conditioned at admissible division events/times. "
        "Hilbert/history machinery is representational, and APR's AB/BC table "
        "is only a simultaneous regional-gluing diagnostic—not that law."
    )
    _require(
        exposure_refused
        and BLINDING_STATUS == "RESULT-KNOWN-BEFORE-V4-IMPLEMENTATION"
        and STATIC_QUALIFIER
        == "APR-STATIC-RAW-PREFIX-SYNTAX-ATOMLESS-RESPONSE-CONSTRUCTED-PROCESS-UNBUILT"
        and REGIONAL_SUPPORT_SCOPE
        == "finite regional-support controls only; regional-support coordinate unearned"
        and PREFIX_SYNTAX_SCOPE
        == "raw prefix-syntax atomlessness only; physical regional referent unconstructed",
        "exact qualifier/scope/exposure fields changed",
    )
    witnesses["scope_and_exposure"] = {
        "artifact_fields": exposure_payload,
        "static_qualifier": STATIC_QUALIFIER,
        "regional_support_scope": REGIONAL_SUPPORT_SCOPE,
        "prefix_syntax_scope": PREFIX_SYNTAX_SCOPE,
        "candidate_law_scope": law_scope,
        "internal_classical_role": "SCORER-REACHABILITY-CONTROL-NOT-CANDIDATE-LAW",
        "overlap_role": "SIMULTANEOUS-GLUING-DIAGNOSTIC-NOT-TRANSITION-LAW",
    }
    checks.append("exact-qualifier-scope-exposure-and-law-scope")

    with tempfile.TemporaryDirectory(prefix="apr-v4-generic-publish-") as raw_directory:
        directory = Path(raw_directory)
        output = directory / "out.json"
        receipt = directory / "receipt.json"
        publish_pair(output, receipt, b"output\n", b"receipt\n")
        prior_output = output.read_bytes()
        prior_receipt = receipt.read_bytes()
        overwrite_refused = False
        try:
            publish_pair(output, receipt, b"changed\n", b"changed\n")
        except ScoreRefusal:
            overwrite_refused = True
        _require(
            overwrite_refused
            and output.read_bytes() == prior_output
            and receipt.read_bytes() == prior_receipt,
            "transactional no-overwrite publish changed existing bytes",
        )
    witnesses["publish_control"] = {
        "first_output_sha256": sha256_bytes(b"output\n"),
        "first_receipt_sha256": sha256_bytes(b"receipt\n"),
        "overwrite_refused": True,
    }
    checks.append("machine-reconstructible-witnesses-and-transactional-publish")

    _require(len(checks) == 27 and len(set(checks)) == 27, "v4 check registry")
    witness_hash = canonical_sha256(witnesses)
    return {
        "schema": "apr-generic-selftest-v4",
        "scientific_fixture_evaluated": False,
        "check_count": len(checks),
        "checks": checks,
        "semantic_witnesses": witnesses,
        "semantic_witness_sha256": witness_hash,
        "status": "PASS",
    }


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


# The v4 integration remains only as an inherited synthetic regression oracle.
# It is deliberately private; the sole public classifier is the v5 weld below.


# ---------------------------------------------------------------------------
# V5 one-law executable weld


V5_EXECUTABLE_ROOT = "v5:one-executable-law-control"
V5_EXECUTABLE_SCHEMA = "apr-v5-executable-law-schema-v1"
V5_SCOPE_SENTENCE = (
    "ISP's candidate ontology is one actual, law-sufficient relational "
    "configuration; its missing fundamental dynamics is an indivisible "
    "stochastic law of transition probabilities between complete "
    "configurations, conditioned at admissible division events/times. "
    "Hilbert/history machinery is representational, and APR's AB/BC table is "
    "only a simultaneous regional-gluing diagnostic—not that law."
)


@dataclass(frozen=True, slots=True)
class ExecutableCarrier:
    root: str
    identifier: str
    states: tuple[str, ...]
    factor_ids: tuple[str, ...] = ()

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "states": self.states,
            "factor_ids": self.factor_ids,
            "ordering": "left-major-lexicographic" if self.factor_ids else None,
        }


@dataclass(frozen=True, slots=True)
class ExecutableBoundary:
    root: str
    identifier: str
    carrier_id: str

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
        }


@dataclass(frozen=True, slots=True)
class ExecutableTransition:
    root: str
    identifier: str
    source_carrier_id: str
    target_carrier_id: str
    matrix: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_carrier_id": self.source_carrier_id,
            "target_carrier_id": self.target_carrier_id,
            "matrix": self.matrix,
        }


@dataclass(frozen=True, slots=True)
class ExecutableOccurrence:
    root: str
    identifier: str
    primitive_id: str
    consumer: str
    source_carrier_id: str
    target_carrier_id: str
    typed_path: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "primitive_id": self.primitive_id,
            "consumer": self.consumer,
            "source_carrier_id": self.source_carrier_id,
            "target_carrier_id": self.target_carrier_id,
            "typed_path": self.typed_path,
        }


@dataclass(frozen=True, slots=True)
class ExecutableComposition:
    root: str
    identifier: str
    consumer: str
    operand_ids: tuple[str, ...]
    source_carrier_id: str
    target_carrier_id: str

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "consumer": self.consumer,
            "operand_ids": self.operand_ids,
            "source_carrier_id": self.source_carrier_id,
            "target_carrier_id": self.target_carrier_id,
        }


@dataclass(frozen=True, slots=True)
class ExecutableInstrument:
    root: str
    identifier: str
    source_carrier_id: str
    target_carrier_id: str
    flag_carrier_id: str
    branch_ids: tuple[str, ...]
    branch_matrices: tuple[QMatrix, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_carrier_id": self.source_carrier_id,
            "target_carrier_id": self.target_carrier_id,
            "flag_carrier_id": self.flag_carrier_id,
            "branch_ids": self.branch_ids,
            "branch_matrices": self.branch_matrices,
        }


@dataclass(frozen=True, slots=True)
class ExecutableWriter:
    root: str
    identifier: str
    source_carrier_id: str
    target_carrier_id: str
    matrix: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_carrier_id": self.source_carrier_id,
            "target_carrier_id": self.target_carrier_id,
            "matrix": self.matrix,
        }


@dataclass(frozen=True, slots=True)
class ExecutableRewrite:
    root: str
    identifier: str
    source_carrier_id: str
    target_carrier_id: str
    base_source_carrier_id: str
    base_target_carrier_id: str
    flag_carrier_id: str
    theta: QMatrix
    passive_inclusion: QMatrix
    supplied_tensor_lift: QMatrix | None = None

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "source_carrier_id": self.source_carrier_id,
            "target_carrier_id": self.target_carrier_id,
            "base_source_carrier_id": self.base_source_carrier_id,
            "base_target_carrier_id": self.base_target_carrier_id,
            "flag_carrier_id": self.flag_carrier_id,
            "theta": self.theta,
            "passive_inclusion": self.passive_inclusion,
            "supplied_tensor_lift": self.supplied_tensor_lift,
        }


@dataclass(frozen=True, slots=True)
class ExecutableReader:
    root: str
    identifier: str
    carrier_id: str
    factor_carrier_id: str
    outcomes: tuple[str, ...]
    matrix: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
            "factor_carrier_id": self.factor_carrier_id,
            "outcomes": self.outcomes,
            "matrix": self.matrix,
        }


@dataclass(frozen=True, slots=True)
class ExecutableContinuation:
    root: str
    identifier: str
    carrier_id: str
    matrix: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
            "matrix": self.matrix,
        }


@dataclass(frozen=True, slots=True)
class ExecutableComparison:
    root: str
    identifier: str
    carrier_id: str
    permutation: QMatrix
    calibrated_state: QMatrix
    calibrated_effect: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
            "permutation": self.permutation,
            "calibrated_state": self.calibrated_state,
            "calibrated_effect": self.calibrated_effect,
        }


@dataclass(frozen=True, slots=True)
class ExecutableInterventionSet:
    root: str
    identifier: str
    carrier_id: str
    alternative_ids: tuple[str, ...]
    base_alternative_matrices: tuple[QMatrix, ...]
    propagation_matrix: QMatrix | None
    reader_id: str

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
            "alternative_ids": self.alternative_ids,
            "base_alternative_matrices": self.base_alternative_matrices,
            "propagation_matrix": self.propagation_matrix,
            "reader_id": self.reader_id,
        }


@dataclass(frozen=True, slots=True)
class ExecutableRegionalSupport:
    root: str
    identifier: str
    carrier_id: str
    state_ids: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
            "state_ids": self.state_ids,
        }


@dataclass(frozen=True, slots=True)
class ExecutableGlobalABC:
    root: str
    identifier: str
    carrier_id: str
    probabilities: tuple[Fraction, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
            "probabilities": self.probabilities,
        }


@dataclass(frozen=True, slots=True)
class ExecutableQuantumStructure:
    root: str
    identifier: str
    carrier_id: str
    flag_carrier_id: str
    base_x: GMatrix
    phase_control: GMatrix
    gram_coefficients: tuple[GaussianRational, ...]
    division_coefficients: tuple[tuple[GaussianRational, ...], ...]
    flag_continuations: tuple[FlagContinuation, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "carrier_id": self.carrier_id,
            "flag_carrier_id": self.flag_carrier_id,
            "base_x": self.base_x,
            "phase_control": self.phase_control,
            "gram_coefficients": self.gram_coefficients,
            "division_coefficients": self.division_coefficients,
            "flag_continuations": self.flag_continuations,
        }


@dataclass(frozen=True, slots=True)
class ExecutableAuxiliaryClaim:
    root: str
    identifier: str
    kind: str
    occurrence_id: str

    def to_data(self) -> dict[str, object]:
        return {
            "root": self.root,
            "id": self.identifier,
            "kind": self.kind,
            "occurrence_id": self.occurrence_id,
        }


@dataclass(frozen=True, slots=True)
class ExecutableLaw:
    root: str
    identifier: str
    schema_id: str
    carriers: tuple[ExecutableCarrier, ...]
    boundaries: tuple[ExecutableBoundary, ...]
    transitions: tuple[ExecutableTransition, ...]
    occurrences: tuple[ExecutableOccurrence, ...]
    valid_compositions: tuple[ExecutableComposition, ...]
    instrument: ExecutableInstrument
    writer: ExecutableWriter
    rewrite: ExecutableRewrite
    comparison: ExecutableComparison
    interventions: tuple[ExecutableInterventionSet, ...]
    readers: tuple[ExecutableReader, ...]
    regional_supports: tuple[ExecutableRegionalSupport, ...]
    continuations: tuple[ExecutableContinuation, ...]
    licensed_continuation_ids: tuple[str, ...]
    owned_global_abc: ExecutableGlobalABC
    alternate_global_abc: ExecutableGlobalABC
    compiler: PrefixCompilerPrimitive
    locality: LocalityPrimitiveLaw
    quantum: ExecutableQuantumStructure
    cached_measurement_payloads: tuple[tuple[str, object], ...] = ()
    cached_restriction_rows: tuple[tuple[str, object], ...] = ()
    opaque_common_labels: tuple[str, ...] = ()
    auxiliary_dependency_claims: tuple[ExecutableAuxiliaryClaim, ...] = ()

    def to_data(self) -> dict[str, object]:
        return {
            "type": "ExecutableLaw",
            "root": self.root,
            "id": self.identifier,
            "schema_id": self.schema_id,
            "carriers": self.carriers,
            "boundaries": self.boundaries,
            "transitions": self.transitions,
            "valid_compositions": self.valid_compositions,
            "instruments": (self.instrument,),
            "comparisons": (self.comparison,),
            "interventions": self.interventions,
            "readers": self.readers,
            "regional_supports": self.regional_supports,
            "regional_rewrites": (self.rewrite,),
            "tensor_and_gluing_structure": {
                "writer": self.writer,
                "continuations": self.continuations,
                "licensed_continuation_ids": self.licensed_continuation_ids,
                "owned_global_abc": self.owned_global_abc,
                "alternate_global_abc": self.alternate_global_abc,
                "compiler": self.compiler,
                "locality": self.locality,
                "quantum": self.quantum,
                "ordering": "left-major-lexicographic",
            },
            "typed_occurrences": self.occurrences,
            "cached_measurement_payloads": self.cached_measurement_payloads,
            "cached_restriction_rows": self.cached_restriction_rows,
            "opaque_common_labels": self.opaque_common_labels,
            "auxiliary_dependency_claims": self.auxiliary_dependency_claims,
        }


@dataclass(frozen=True, slots=True)
class ExecutableLawFamily:
    root: str
    identifier: str
    schema_id: str
    candidates: tuple[ExecutableLaw, ...]
    observed_endpoint: QMatrix

    def to_data(self) -> dict[str, object]:
        return {
            "type": "ExecutableLawFamily",
            "root": self.root,
            "id": self.identifier,
            "schema_id": self.schema_id,
            "candidates": self.candidates,
            "observed_endpoint": self.observed_endpoint,
        }


@dataclass(frozen=True, slots=True)
class ExecutableLawMeasurement:
    primitive_payload_sha256: str
    candidate_id: str
    valid: bool
    issues: tuple[str, ...]
    coordinates: Mapping[str, object]
    native_measurements: Mapping[str, object]
    dataflow_dag: Mapping[str, object]
    composed_map: QMatrix | None
    selection_response: QMatrix | None
    selection_residual: Mapping[str, object]
    ontology_role: str

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "ExecutableLawMeasurement",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "candidate_id": self.candidate_id,
            "valid": self.valid,
            "issues": self.issues,
            "coordinates": self.coordinates,
            "native_measurements": self.native_measurements,
            "dataflow_dag": self.dataflow_dag,
            "P_i": self.composed_map,
            "r_i": self.selection_response,
            "selection_residual": self.selection_residual,
            "ontology_role": self.ontology_role,
        }


@dataclass(frozen=True, slots=True)
class ExecutableFamilyClassification:
    primitive_payload_sha256: str
    primary: str
    walls: tuple[str, ...]
    selected_candidate_id: str | None
    candidate_measurements: tuple[ExecutableLawMeasurement, ...]
    family_residuals: Mapping[str, object]
    issues: tuple[str, ...]

    def to_data(self) -> dict[str, object]:
        return {
            "measurement_type": "ExecutableFamilyClassification",
            "primitive_payload_sha256": self.primitive_payload_sha256,
            "primary": self.primary,
            "walls": self.walls,
            "selected_candidate_id": self.selected_candidate_id,
            "candidate_measurements": self.candidate_measurements,
            "family_residuals": self.family_residuals,
            "issues": self.issues,
        }


@dataclass(frozen=True, slots=True)
class ForgedExecutableMeasurement:
    valid: bool
    primary: str
    residual: int

    def to_data(self) -> dict[str, object]:
        return {
            "type": "ForgedExecutableMeasurement",
            "valid": self.valid,
            "primary": self.primary,
            "residual": self.residual,
        }


def _v5_index(
    rows: Sequence[object], role: str, issues: list[str]
) -> dict[str, object]:
    result: dict[str, object] = {}
    for row in rows:
        identifier = getattr(row, "identifier", None)
        if not isinstance(identifier, str) or not identifier:
            issues.append(f"{role}:missing-id")
        elif identifier in result:
            issues.append(f"{role}:duplicate-id:{identifier}")
        else:
            result[identifier] = row
    return result


def _v5_effect(carrier: ExecutableCarrier, state_id: str) -> QMatrix | None:
    if state_id not in carrier.states:
        return None
    selected = carrier.states.index(state_id)
    return QMatrix.from_rows(
        (
            tuple(
                Fraction(1) if column == selected else Fraction(0)
                for column in range(len(carrier.states))
            ),
        ),
        ncols=len(carrier.states),
    )


def _v5_distribution_measurement(
    probabilities: Sequence[Fraction], expected_size: int
) -> dict[str, object]:
    return {
        "expected_size": expected_size,
        "actual_size": len(probabilities),
        "negative_entry_count": sum(value < 0 for value in probabilities),
        "normalization_residual": sum(probabilities, Fraction(0)) - 1,
        "valid": len(probabilities) == expected_size
        and all(value >= 0 for value in probabilities)
        and sum(probabilities, Fraction(0)) == 1,
    }


def _v5_abc_shadows(
    configurations: Sequence[str], probabilities: Sequence[Fraction]
) -> dict[str, object]:
    probability = {
        configuration: probabilities[index]
        for index, configuration in enumerate(configurations)
    } if len(configurations) == len(probabilities) else {}
    ab = {
        pair: sum(
            (probability.get(pair + c, Fraction(0)) for c in "01"),
            Fraction(0),
        )
        for pair in ("00", "01", "10", "11")
    }
    bc = {
        pair: sum(
            (probability.get(a + pair, Fraction(0)) for a in "01"),
            Fraction(0),
        )
        for pair in ("00", "01", "10", "11")
    }
    b = {
        value: sum(
            (
                probability.get(a + value + c, Fraction(0))
                for a in "01"
                for c in "01"
            ),
            Fraction(0),
        )
        for value in "01"
    }
    markov = {
        configuration: probability.get(configuration, Fraction(0))
        * b[configuration[1]]
        - ab[configuration[:2]] * bc[configuration[1:]]
        for configuration in configurations
    }
    return {
        "P_AB": ab,
        "P_BC": bc,
        "P_B": b,
        "markov_cell_residuals": markov,
        "markov_zero": bool(markov) and all(value == 0 for value in markov.values()),
    }


def _v5_close_q_matrices(
    generators: Sequence[QMatrix], *, maximum: int = 64
) -> tuple[dict[str, QMatrix], bool]:
    closure = {canonical_sha256(row): row for row in generators}
    changed = True
    while changed and len(closure) <= maximum:
        changed = False
        for left in tuple(closure.values()):
            for right in tuple(closure.values()):
                try:
                    product = qmultiply(left, right)
                except ValueError:
                    return closure, False
                key = canonical_sha256(product)
                if key not in closure:
                    closure[key] = product
                    changed = True
    return closure, not changed


def _v5_add_primitive_node(
    nodes: MutableMapping[str, dict[str, object]],
    identifier: str,
    primitive: object,
    kind: str,
) -> None:
    nodes[identifier] = {
        "kind": kind,
        "operands": (),
        "primitive": primitive,
        "derived_object": primitive,
        "independently_recomputed_expected_object": primitive,
        "exact_residual": {"nonzero_count": 0},
        "carrier_composition_trace": (),
    }


def _v5_add_derived_node(
    nodes: MutableMapping[str, dict[str, object]],
    identifier: str,
    *,
    kind: str,
    operands: Sequence[str],
    derived: object,
    expected: object,
    residual: object,
    carrier_trace: Sequence[str],
) -> None:
    nodes[identifier] = {
        "kind": kind,
        "operands": tuple(operands),
        "derived_object": derived,
        "independently_recomputed_expected_object": expected,
        "exact_residual": residual,
        "carrier_composition_trace": tuple(carrier_trace),
    }


def _v5_finalize_dataflow_dag(
    nodes: Mapping[str, Mapping[str, object]],
    terminal_coordinates: Mapping[str, str],
    auxiliary_claims: Sequence[Mapping[str, object]],
) -> dict[str, object]:
    issues: list[str] = []
    needed: set[str] = set()
    stack = list(terminal_coordinates)
    while stack:
        node_id = stack.pop()
        if node_id in needed:
            continue
        node = nodes.get(node_id)
        if not isinstance(node, Mapping):
            issues.append(f"backward-slice:missing-node:{node_id}")
            continue
        needed.add(node_id)
        for operand_id in node.get("operands", ()):
            if operand_id not in nodes:
                issues.append(
                    f"backward-slice:unresolved-operand:{node_id}:{operand_id}"
                )
            else:
                stack.append(str(operand_id))

    children: dict[str, set[str]] = {identifier: set() for identifier in needed}
    raw_edges: list[tuple[str, str]] = []
    for target_id in sorted(needed):
        node = nodes[target_id]
        for operand_id in node.get("operands", ()):
            operand_text = str(operand_id)
            if operand_text in needed:
                raw_edges.append((operand_text, target_id))
                children[operand_text].add(target_id)

    coordinate_reachability: dict[str, tuple[str, ...]] = {}
    for source_id, target_id in raw_edges:
        reached_coordinates: set[str] = set()
        pending = [target_id]
        visited: set[str] = set()
        while pending:
            active = pending.pop()
            if active in visited:
                continue
            visited.add(active)
            if active in terminal_coordinates:
                reached_coordinates.add(terminal_coordinates[active])
            pending.extend(children.get(active, ()))
        coordinate_reachability[f"{source_id}->{target_id}"] = tuple(
            sorted(reached_coordinates)
        )
        if not reached_coordinates:
            issues.append(
                f"backward-slice:edge-without-native-coordinate:{source_id}:{target_id}"
            )

    adjacency: dict[str, set[str]] = {identifier: set() for identifier in needed}
    for source_id, target_id in raw_edges:
        adjacency[source_id].add(target_id)
        adjacency[target_id].add(source_id)
    components: list[tuple[str, ...]] = []
    unseen = set(needed)
    while unseen:
        start = min(unseen)
        reached: set[str] = set()
        pending = [start]
        while pending:
            active = pending.pop()
            if active in reached:
                continue
            reached.add(active)
            pending.extend(sorted(adjacency[active] - reached, reverse=True))
        unseen -= reached
        components.append(tuple(sorted(reached)))
    connected = bool(needed) and len(components) == 1
    if not connected:
        issues.append("backward-slice:not-connected")

    unused_nodes = tuple(sorted(set(nodes) - needed))
    deletion_assays = {
        f"{source_id}->{target_id}": {
            "removed_operand_id": source_id,
            "invalidated_derived_node_id": target_id,
            "original_actual_operand_ids": tuple(nodes[target_id].get("operands", ())),
            "remaining_operand_ids": tuple(
                operand_id
                for operand_id in nodes[target_id].get("operands", ())
                if str(operand_id) != source_id
            ),
            "derived_object_after_deletion": None,
            "exact_residual_after_deletion": {
                "shape_match": False,
                "nonzero_count": None,
            },
            "result": "ILL-TYPED-MISSING-ACTUAL-OPERAND",
            "classifier_consumed_native_coordinates": coordinate_reachability[
                f"{source_id}->{target_id}"
            ],
        }
        for source_id, target_id in raw_edges
    }
    return {
        "nodes": {identifier: nodes[identifier] for identifier in sorted(needed)},
        "edges": tuple(raw_edges),
        "terminal_coordinates": dict(sorted(terminal_coordinates.items())),
        "edge_native_coordinate_reachability": coordinate_reachability,
        "edge_deletion_assays": deletion_assays,
        "connected_components": tuple(sorted(components)),
        "connected": connected,
        "unused_nodes_not_admitted": unused_nodes,
        "auxiliary_claims_not_admitted": tuple(auxiliary_claims),
        "carrier_or_boundary_equality_edges": (),
        "root_identifier_or_hash_edges": (),
        "cached_payload_edges": (),
        "issues": tuple(sorted(set(issues))),
        "valid": not issues,
    }


def _v5_occurrence_rows(root: str) -> tuple[ExecutableOccurrence, ...]:
    consumers = (
        ("occ:T:process:a1", "process-cut-a", ("G2", "T", "G2")),
        ("occ:T:process:a2", "process-cut-a", ("G2", "T", "G2")),
        ("occ:T:process:b1", "process-cut-b", ("G2", "T", "G2")),
        ("occ:T:process:b2", "process-cut-b", ("G2", "T", "G2")),
        ("occ:T:tensor", "tensor-interface", ("G2", "T", "G2", "tensor", "F")),
        ("occ:T:comparison", "comparison", ("G2", "T", "G2", "compare")),
        ("occ:T:causal", "causal-order", ("G2", "reset", "T", "reader")),
        (
            "occ:T:contact",
            "generated-contact",
            ("G2", "reset", "T", "tensor-I_F", "CNOT", "reader-F"),
        ),
        ("occ:T:overlap", "overlap-shadows", ("A", "T", "A", "restrict-AB-BC")),
        ("occ:T:quantum", "quantum-history", ("G2", "T", "H0", "endpoint")),
        (
            "occ:T:ontology",
            "ontology-calibration",
            ("G2", "T", "Q_tot", "W", "Theta-tensor-I_F", "R_F"),
        ),
        (
            "occ:T:compiler",
            "compiler-tensor",
            ("G2", "T", "G2", "tensor", "fresh-prefix-effect"),
        ),
        (
            "occ:T:locality",
            "locality-transport",
            ("G2", "T", "G2", "tensor-I_F", "support-effect"),
        ),
    )
    return tuple(
        ExecutableOccurrence(
            root,
            identifier,
            "T",
            consumer,
            "G2",
            "G2",
            path,
        )
        for identifier, consumer, path in consumers
    )


def _v5_composition_rows(root: str) -> tuple[ExecutableComposition, ...]:
    return (
        ExecutableComposition(
            root,
            "composition:process-cut-a",
            "process-cut-a",
            ("occ:T:process:a1", "occ:T:process:a2"),
            "G2",
            "G2",
        ),
        ExecutableComposition(
            root,
            "composition:process-cut-b",
            "process-cut-b",
            ("occ:T:process:b1", "occ:T:process:b2"),
            "G2",
            "G2",
        ),
        ExecutableComposition(
            root,
            "composition:tensor-interface",
            "tensor-interface",
            ("occ:T:tensor",),
            "G2xF",
            "G2xF",
        ),
        ExecutableComposition(
            root,
            "composition:comparison",
            "comparison",
            ("comparison:P", "occ:T:comparison"),
            "G2",
            "G2",
        ),
        ExecutableComposition(
            root,
            "composition:causal-order",
            "causal-order",
            ("intervention:causal", "occ:T:causal", "reader:causal"),
            "G2",
            "outcome:G2",
        ),
        ExecutableComposition(
            root,
            "composition:generated-contact",
            "generated-contact",
            ("intervention:contact", "occ:T:contact", "reader:contact"),
            "G2xF",
            "outcome:F",
        ),
        ExecutableComposition(
            root,
            "composition:overlap-shadows",
            "overlap-shadows",
            ("global:ABC:owned", "occ:T:overlap"),
            "ABC",
            "AB+BC",
        ),
        ExecutableComposition(
            root,
            "composition:quantum-history",
            "quantum-history",
            ("quantum:phase-history", "occ:T:quantum"),
            "G2",
            "quantum-endpoint",
        ),
        ExecutableComposition(
            root,
            "composition:ontology-calibration",
            "ontology-calibration",
            (
                "occ:T:ontology",
                "instrument:Q",
                "writer:W",
                "rewrite:Theta",
                "support:new-n",
                "reader:output-flag",
            ),
            "G2",
            "outcome:F",
        ),
        ExecutableComposition(
            root,
            "composition:compiler-tensor",
            "compiler-tensor",
            ("compiler:uniform-prefix", "occ:T:compiler"),
            "G2xPrefix3",
            "G2xPrefix3",
        ),
        ExecutableComposition(
            root,
            "composition:locality-transport",
            "locality-transport",
            ("locality:two-bit", "occ:T:locality"),
            "G2xF",
            "G2xF",
        ),
    )


def build_executable_law(
    candidate_id: str,
    *,
    transition_kind: str,
    fault: str | None = None,
    cached_measurement: object | None = None,
) -> ExecutableLaw:
    if candidate_id not in {"L_I", "L_X"}:
        raise ValueError("v5 executable candidate id")
    root = V5_EXECUTABLE_ROOT
    g2_states = ("0", "1")
    flag_states = ("0", "1")
    g3_states = ("0", "1", "n")
    g2f_states = _tensor_frontier(g2_states, flag_states)
    g3f_states = _tensor_frontier(g3_states, flag_states)
    abc_states = tuple(
        "".join(bits) for bits in itertools.product("01", repeat=3)
    )
    carriers: list[ExecutableCarrier] = [
        ExecutableCarrier(root, "G2", g2_states),
        ExecutableCarrier(root, "F", flag_states),
        ExecutableCarrier(root, "G2xF", g2f_states, ("G2", "F")),
        ExecutableCarrier(root, "G3", g3_states),
        ExecutableCarrier(root, "G3xF", g3f_states, ("G3", "F")),
        ExecutableCarrier(root, "ABC", abc_states, ("A", "B", "C")),
    ]
    boundaries = tuple(
        ExecutableBoundary(root, f"boundary:{carrier.identifier}", carrier.identifier)
        for carrier in carriers
    )

    identity = QMatrix.identity(2)
    flip = QMatrix.from_rows(((0, 1), (1, 0)))
    if transition_kind == "I":
        transition_matrix = identity
    elif transition_kind == "X":
        transition_matrix = flip
    else:
        raise ValueError("unknown executable transition kind")
    if fault in {"RESET-ONE", "STALE-CACHE"}:
        transition_matrix = QMatrix.from_rows(((0, 0), (1, 1)))
    elif fault == "NONINVOLUTIVE":
        transition_matrix = QMatrix.from_rows(
            ((0, Fraction(1, 2)), (1, Fraction(1, 2)))
        )
    transitions: list[ExecutableTransition] = [
        ExecutableTransition(root, "T", "G2", "G2", transition_matrix)
    ]

    occurrences = list(_v5_occurrence_rows(root))
    if fault == "CLONE-ID":
        transitions.append(
            ExecutableTransition(root, "T-clone", "G2", "G2", transition_matrix)
        )
        occurrences = [
            replace(row, primitive_id="T-clone")
            if row.consumer == "generated-contact"
            else row
            for row in occurrences
        ]
    sever_consumer = {
        "SEVER-OCCURRENCE": "comparison",
        "ZERO-SLICE": "compiler-tensor",
        "CANCELLED-LOOP": "generated-contact",
        "CARRIER-ONLY": "causal-order",
    }.get(fault)
    if sever_consumer is not None:
        occurrences = [row for row in occurrences if row.consumer != sever_consumer]

    compositions = list(_v5_composition_rows(root))
    if fault in {"REMOVE-BRIDGE", "LABEL-ONLY-JOINT"}:
        compositions = [
            row for row in compositions if row.consumer != "ontology-calibration"
        ]
    elif fault == "CALIBRATION-BYPASS":
        compositions = [
            replace(
                row,
                operand_ids=("occ:T:ontology", "reader:output-flag"),
            )
            if row.consumer == "ontology-calibration"
            else row
            for row in compositions
        ]

    q0 = QMatrix.from_rows(((1, 0), (0, 0)))
    q1 = QMatrix.from_rows(((0, 0), (0, 1)))
    if fault == "BRANCH-SUM-ONLY":
        half_identity = qscale(Fraction(1, 2), identity)
        q0 = half_identity
        q1 = half_identity
    instrument = ExecutableInstrument(
        root,
        "instrument:Q",
        "G2",
        "G2",
        "F",
        ("Q_0", "Q_1"),
        (q0, q1),
    )

    writer = ExecutableWriter(
        root,
        "writer:W",
        "G2",
        "G2xF",
        QMatrix.from_rows(((1, 0), (0, 0), (0, 0), (0, 1))),
    )
    theta = QMatrix.from_rows(((1, 0), (0, 0), (0, 1)))
    if fault == "ONE-COLUMN-TENSOR":
        theta = QMatrix.from_rows(((1, 1), (0, 0), (0, 0)))
    iota = QMatrix.from_rows(((1, 0), (0, 1), (0, 0)))
    rewrite_source = "G2xF"
    rewrite_target = "G3xF"
    if fault == "ALIEN-CARRIER":
        carriers.append(
            ExecutableCarrier(root, "ALIEN-G2xF", g2f_states, ("G2", "F"))
        )
        rewrite_source = "ALIEN-G2xF"
    elif fault == "ISOMORPHIC-DISCONNECT":
        carriers.extend(
            (
                ExecutableCarrier(root, "G2xF-writer", g2f_states, ("G2", "F")),
                ExecutableCarrier(root, "G2xF-rewrite", g2f_states, ("G2", "F")),
            )
        )
        writer = replace(writer, target_carrier_id="G2xF-writer")
        rewrite_source = "G2xF-rewrite"
    rewrite = ExecutableRewrite(
        root,
        "rewrite:Theta",
        rewrite_source,
        rewrite_target,
        "G2",
        "G3",
        "F",
        theta,
        iota,
        (
            QMatrix.from_rows(
                (
                    tuple(
                        Fraction(1)
                        if row == column
                        else Fraction(0)
                        for column in range(4)
                    )
                    for row in range(6)
                ),
                ncols=4,
            )
            if fault == "ONE-COLUMN-TENSOR"
            else None
        ),
    )

    output_flag_reader = ExecutableReader(
        root,
        "reader:output-flag",
        "G3xF",
        "F",
        flag_states,
        _target_reader_matrix(3, 2),
    )
    if fault == "SINGLE-INPUT-READER":
        reader_rows = [list(row) for row in output_flag_reader.matrix.data]
        reader_rows[0][5] = Fraction(1)
        reader_rows[1][5] = Fraction(0)
        output_flag_reader = replace(
            output_flag_reader,
            matrix=QMatrix.from_rows(reader_rows, ncols=6),
        )
    readers = (
        ExecutableReader(
            root,
            "reader:causal",
            "G2",
            "G2",
            g2_states,
            QMatrix.identity(2),
        ),
        ExecutableReader(
            root,
            "reader:contact",
            "G2xF",
            "F",
            flag_states,
            _target_reader_matrix(2, 2),
        ),
        output_flag_reader,
    )

    swap_g3 = _q_permutation_from_images((1, 0, 2))
    continuations: list[ExecutableContinuation] = [
        ExecutableContinuation(root, "continuation:I", "G3xF", QMatrix.identity(6)),
        ExecutableContinuation(
            root,
            "continuation:X_G3",
            "G3xF",
            _q_kron(swap_g3, QMatrix.identity(2)),
        ),
    ]
    licensed = tuple(row.identifier for row in continuations)
    if fault == "DUPLICATE-ID":
        continuations.append(
            ExecutableContinuation(
                root,
                "continuation:X_G3",
                "G3xF",
                QMatrix.identity(6),
            )
        )
    elif fault == "HIDDEN-ERASER":
        flag_reset_zero = QMatrix.from_rows(((1, 1), (0, 0)))
        continuations.append(
            ExecutableContinuation(
                root,
                "continuation:hidden-flag-eraser",
                "G3xF",
                _q_kron(QMatrix.identity(3), flag_reset_zero),
            )
        )

    comparison = ExecutableComparison(
        root,
        "comparison:P",
        "G2",
        flip,
        QMatrix.from_rows(((1,), (0,))),
        QMatrix.from_rows(((1, 0),), ncols=2),
    )
    reset_zero = QMatrix.from_rows(((1, 1), (0, 0)))
    reset_one = QMatrix.from_rows(((0, 0), (1, 1)))
    contact_propagation = (
        QMatrix.identity(4) if fault == "CONTACT-IDENTITY" else _cnot_matrix()
    )
    interventions = (
        ExecutableInterventionSet(
            root,
            "intervention:causal",
            "G2",
            ("reset-zero", "reset-one"),
            (reset_zero, reset_one),
            None,
            "reader:causal",
        ),
        ExecutableInterventionSet(
            root,
            "intervention:contact",
            "G2",
            ("source-reset-zero", "source-reset-one"),
            (reset_zero, reset_one),
            contact_propagation,
            "reader:contact",
        ),
    )

    support = ExecutableRegionalSupport(
        root, "support:new-n", "G3xF", ("(n,0)", "(n,1)")
    )
    uniform = tuple(Fraction(1, 8) for _ in abc_states)
    parity = tuple(
        Fraction(1, 4)
        if (int(row[0]) + int(row[1]) + int(row[2])) % 2 == 0
        else Fraction(0)
        for row in abc_states
    )
    owned_probabilities = parity if fault == "RESTRICTION-CACHE" else uniform
    alternate_probabilities = uniform if fault == "RESTRICTION-CACHE" else parity
    owned_global = ExecutableGlobalABC(
        root, "global:ABC:owned", "ABC", owned_probabilities
    )
    alternate_global = ExecutableGlobalABC(
        root, "global:ABC:parity-control", "ABC", alternate_probabilities
    )

    compiler = PrefixCompilerPrimitive(
        root,
        "compiler:uniform-prefix",
        "uniform-prefix-compiler",
        (
            PrefixRegion.cylinder("0"),
            PrefixRegion.cylinder("1"),
            PrefixRegion.cylinder("00"),
        ),
        (),
        "symbolic-prefix-split",
        None,
    )
    locality_template = build_locality_existence_law()
    locality = replace(
        locality_template,
        root=root,
        identifier="locality:two-bit",
        regions=tuple(
            replace(
                row,
                root=root,
                identifier=f"locality-region:{row.identifier}",
            )
            for row in locality_template.regions
        ),
        replacements=tuple(
            replace(row, root=root) for row in locality_template.replacements
        ),
        transition_reference_id=None,
    )
    quantum = ExecutableQuantumStructure(
        root,
        "quantum:phase-history",
        "G2",
        "F",
        GMatrix.from_rows(((0, 1), (1, 0))),
        GMatrix.from_rows(((GONE, GZERO), (GZERO, GI))),
        (GONE, GI),
        (
            (GONE, GaussianRational(0, -1)),
            (GONE, GI),
        ),
        (
            FlagContinuation(root, "quantum-flag-I", GMatrix.identity(2)),
            FlagContinuation(
                root,
                "quantum-flag-Z",
                GMatrix.from_rows(((1, 0), (0, -1))),
            ),
        ),
    )

    cached_payloads: tuple[tuple[str, object], ...] = ()
    if fault == "STALE-CACHE":
        cached_payloads = (
            (
                "old-L_X-measurement",
                cached_measurement
                if cached_measurement is not None
                else {"valid": True, "primary": "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED"},
            ),
        )
    cached_restrictions: tuple[tuple[str, object], ...] = ()
    if fault == "RESTRICTION-CACHE":
        cached_restrictions = (
            ("P_AB", tuple(Fraction(1, 4) for _ in range(4))),
            ("P_BC", tuple(Fraction(1, 4) for _ in range(4))),
        )
    auxiliary_claims: tuple[ExecutableAuxiliaryClaim, ...] = ()
    if fault == "ZERO-SLICE":
        auxiliary_claims = (
            ExecutableAuxiliaryClaim(
                root, "auxiliary:zero-times-T", "ZERO-SLICE", "occ:T:compiler"
            ),
        )
    elif fault == "CANCELLED-LOOP":
        auxiliary_claims = (
            ExecutableAuxiliaryClaim(
                root,
                "auxiliary:T-inverse-T",
                "CANCELLED-LOOP",
                "occ:T:contact",
            ),
        )
    return ExecutableLaw(
        root=root,
        identifier=candidate_id,
        schema_id=V5_EXECUTABLE_SCHEMA,
        carriers=tuple(carriers),
        boundaries=boundaries,
        transitions=tuple(transitions),
        occurrences=tuple(occurrences),
        valid_compositions=tuple(compositions),
        instrument=instrument,
        writer=writer,
        rewrite=rewrite,
        comparison=comparison,
        interventions=interventions,
        readers=readers,
        regional_supports=(support,),
        continuations=tuple(continuations),
        licensed_continuation_ids=licensed,
        owned_global_abc=owned_global,
        alternate_global_abc=alternate_global,
        compiler=compiler,
        locality=locality,
        quantum=quantum,
        cached_measurement_payloads=cached_payloads,
        cached_restriction_rows=cached_restrictions,
        opaque_common_labels=(
            ("one-law", "record-write", "region-rewrite")
            if fault == "LABEL-ONLY-JOINT"
            else ()
        ),
        auxiliary_dependency_claims=auxiliary_claims,
    )


def build_executable_family(
    fault: str | None = None,
    *,
    cached_measurement: object | None = None,
) -> ExecutableLawFamily:
    left_fault = fault if fault == "MOVE-DOWNSTREAM" else None
    right_fault = None if fault == "MOVE-DOWNSTREAM" else fault
    left = build_executable_law(
        "L_I",
        transition_kind="X" if fault == "MOVE-DOWNSTREAM" else "I",
        fault=left_fault,
    )
    right = build_executable_law(
        "L_X",
        transition_kind="X",
        fault=right_fault,
        cached_measurement=cached_measurement,
    )
    return ExecutableLawFamily(
        V5_EXECUTABLE_ROOT,
        "finite-family:L_I,L_X",
        V5_EXECUTABLE_SCHEMA,
        (left, right),
        QMatrix.from_rows(((0,), (1,))),
    )


def _v5_basis_state(size: int, selected: int) -> QMatrix:
    return QMatrix.from_rows(
        (
            (Fraction(1) if row == selected else Fraction(0),)
            for row in range(size)
        ),
        ncols=1,
    )


def _v5_support_effect(
    carrier: ExecutableCarrier, state_ids: Sequence[str]
) -> QMatrix | None:
    if not state_ids or len(set(state_ids)) != len(state_ids):
        return None
    if any(state_id not in carrier.states for state_id in state_ids):
        return None
    selected = {carrier.states.index(state_id) for state_id in state_ids}
    return QMatrix.from_rows(
        (
            tuple(
                Fraction(1) if column in selected else Fraction(0)
                for column in range(len(carrier.states))
            ),
        ),
        ncols=len(carrier.states),
    )


def _v5_safe_q_product(values: Sequence[QMatrix]) -> QMatrix | None:
    if not values:
        return None
    result = values[-1]
    try:
        for value in reversed(values[:-1]):
            result = qmultiply(value, result)
    except ValueError:
        return None
    return result


def _v5_safe_g_product(values: Sequence[GMatrix]) -> GMatrix | None:
    if not values:
        return None
    result = values[-1]
    try:
        for value in reversed(values[:-1]):
            result = _g_multiply(value, result)
    except ValueError:
        return None
    return result


def _v5_phase_quantum_measurement(
    quantum: ExecutableQuantumStructure,
    transition: QMatrix,
    *,
    source_variant: str = "ADJOINT",
) -> dict[str, object]:
    if source_variant not in {
        "ADJOINT",
        "CONJUGATION-SOURCE",
        "HISTORY-TRANSPOSE",
        "Z-TRANSPOSE",
    }:
        raise ValueError("unknown v5 phase source control")
    issues: list[str] = []
    half = GaussianRational(Fraction(1, 2))
    quarter = GaussianRational(Fraction(1, 4))
    identity = GMatrix.identity(2)
    expected_x = GMatrix.from_rows(((0, 1), (1, 0)))
    expected_phase = GMatrix.from_rows(((1, 0), (0, GI)))
    h0 = _g_scale(half, identity)
    h1 = _g_scale(GI * half, quantum.base_x)
    histories = (h0, h1)
    rho_plus = GMatrix.from_rows(
        (
            (half, half),
            (half, half),
        )
    )

    gram = GMatrix.from_rows(
        (
            (
                _g_trace(
                    _g_multiply(
                        _g_multiply(histories[left], rho_plus),
                        (
                            _g_transpose(histories[right])
                            if source_variant == "HISTORY-TRANSPOSE"
                            else _g_adjoint(histories[right])  # V5-HISTORY-TRANSPOSE-SOURCE-TARGET
                        ),
                    )
                )
                for right in range(2)
            )
            for left in range(2)
        ),
        ncols=2,
    )
    expected_gram = GMatrix.from_rows(
        (
            (quarter, GaussianRational(0, Fraction(-1, 4))),
            (GaussianRational(0, Fraction(1, 4)), quarter),
        )
    )
    gram_residual = _g_residual(gram, expected_gram)
    gram_positive, gram_minors = _g_positive_semidefinite(gram)

    coefficients = quantum.gram_coefficients
    z_column = GMatrix.from_rows(((coefficient,) for coefficient in coefficients), ncols=1)
    z_bra = (
        _g_transpose(z_column)
        if source_variant == "Z-TRANSPOSE"
        else _g_adjoint(z_column)  # V5-Z-TRANSPOSE-SOURCE-TARGET
    )
    z_scalar_matrix = (
        _v5_safe_g_product((z_bra, gram, z_column))
        if len(coefficients) == 2
        else None
    )
    z_scalar = (
        _g_trace(z_scalar_matrix)
        if isinstance(z_scalar_matrix, GMatrix) and z_scalar_matrix.shape == (1, 1)
        else GZERO
    )
    abar = GMatrix.zero(2, 2)
    awrong = GMatrix.zero(2, 2)
    if len(coefficients) == 2:
        for coefficient, history in zip(coefficients, histories):
            abar_scale = (
                coefficient
                if source_variant == "CONJUGATION-SOURCE"
                else coefficient.conjugate()  # V5-CONJUGATION-SOURCE-TARGET
            )
            abar = _g_add(abar, _g_scale(abar_scale, history))
            awrong = _g_add(awrong, _g_scale(coefficient, history))
    expected_abar = _g_scale(half, _g_add(identity, expected_x))
    expected_awrong = _g_scale(half, _g_subtract(identity, expected_x))
    abar_scalar_matrix = _v5_safe_g_product((abar, rho_plus, _g_adjoint(abar)))
    awrong_scalar_matrix = _v5_safe_g_product(
        (awrong, rho_plus, _g_adjoint(awrong))
    )
    abar_scalar = (
        _g_trace(abar_scalar_matrix)
        if isinstance(abar_scalar_matrix, GMatrix)
        else GZERO
    )
    awrong_scalar = (
        _g_trace(awrong_scalar_matrix)
        if isinstance(awrong_scalar_matrix, GMatrix)
        else GZERO
    )
    gram_operator_identity_residual = {
        "left_z_adjoint_D_z": z_scalar,
        "right_trace_Abar_rho_Abar_adjoint": abar_scalar,
        "nonzero_count": 0 if z_scalar == abar_scalar else 1,
    }

    division_operators: list[GMatrix] = []
    division_rows: list[dict[str, object]] = []
    for coefficients_row in quantum.division_coefficients:
        operator = GMatrix.zero(2, 2)
        row_valid = len(coefficients_row) == len(histories)
        if row_valid:
            for coefficient, history in zip(coefficients_row, histories):
                operator = _g_add(operator, _g_scale(coefficient, history))
            division_operators.append(operator)
        division_rows.append(
            {
                "coefficients": coefficients_row,
                "derived_operator": operator if row_valid else None,
                "valid": row_valid,
            }
        )
    expected_division_coefficients = (
        (GONE, GaussianRational(0, -1)),
        (GONE, GI),
    )
    expected_plus = expected_abar
    expected_minus = expected_awrong
    completeness = GMatrix.zero(2, 2)
    for operator in division_operators:
        completeness = _g_add(
            completeness,
            _g_multiply(_g_adjoint(operator), operator),
        )
    completeness_residual = _g_residual(completeness, identity)
    dilation = (
        _g_vstack(tuple(division_operators))
        if division_operators
        else GMatrix.zero(0, 2)
    )
    dilation_residual = (
        _g_residual(
            _g_multiply(_g_adjoint(dilation), dilation),
            identity,
        )
        if dilation.nrows
        else {"shape_match": False, "nonzero_count": None}
    )

    flag_projectors = tuple(
        GMatrix.from_rows(
            (
                (
                    GONE
                    if row == column and row // 2 == flag
                    else GZERO
                    for column in range(4)
                )
                for row in range(4)
            ),
            ncols=4,
        )
        for flag in range(2)
    )
    flag_orthogonality_rows: list[dict[str, object]] = []
    for left, left_projector in enumerate(flag_projectors):
        for right, right_projector in enumerate(flag_projectors):
            expected = (
                left_projector if left == right else GMatrix.zero(4, 4)
            )
            flag_orthogonality_rows.append(
                {
                    "left": left,
                    "right": right,
                    "residual": _g_residual(
                        _g_multiply(left_projector, right_projector), expected
                    ),
                }
            )

    continuation_index: dict[str, FlagContinuation] = {}
    continuation_issues: list[str] = []
    for continuation in quantum.flag_continuations:
        if continuation.identifier in continuation_index:
            continuation_issues.append(
                f"quantum-continuation:duplicate-id:{continuation.identifier}"
            )
        else:
            continuation_index[continuation.identifier] = continuation
    closure: dict[str, GMatrix] = {}
    for continuation_id, continuation in sorted(continuation_index.items()):
        typed = bool(
            continuation.root == quantum.root
            and continuation.matrix.shape == (2, 2)
        )
        if not typed:
            continuation_issues.append(
                f"quantum-continuation:typing:{continuation_id}"
            )
        else:
            closure[canonical_sha256(continuation.matrix)] = continuation.matrix
    closure_changed = True
    while closure_changed and len(closure) <= 64:
        closure_changed = False
        for left in tuple(closure.values()):
            for right in tuple(closure.values()):
                product = _g_multiply(left, right)
                product_hash = canonical_sha256(product)
                if product_hash not in closure:
                    closure[product_hash] = product
                    closure_changed = True
    closure_complete = not closure_changed
    recovery_rows: list[dict[str, object]] = []
    recovery_valid = bool(closure and closure_complete)
    for word_hash, continuation in sorted(closure.items()):
        lifted = _g_kron(continuation, identity)
        continued_dilation = _g_multiply(lifted, dilation)
        isometry_residual = _g_residual(
            _g_multiply(_g_adjoint(continued_dilation), continued_dilation),
            identity,
        )
        projector_rows: list[dict[str, object]] = []
        for flag, projector in enumerate(flag_projectors):
            stability_residual = _g_residual(
                _g_multiply(
                    _g_multiply(_g_adjoint(lifted), projector), lifted
                ),
                projector,
            )
            projector_rows.append(
                {
                    "flag": flag,
                    "stability_residual": stability_residual,
                }
            )
        word_valid = bool(
            isometry_residual.get("nonzero_count") == 0
            and all(
                row["stability_residual"].get("nonzero_count") == 0
                for row in projector_rows
            )
        )
        recovery_valid = recovery_valid and word_valid
        recovery_rows.append(
            {
                "word_sha256": word_hash,
                "flag_continuation": continuation,
                "lifted_continuation": lifted,
                "continued_dilation": continued_dilation,
                "dilation_isometry_residual": isometry_residual,
                "orthogonal_flag_recovery": tuple(projector_rows),
                "valid": word_valid,
            }
        )

    plus_operator = (
        division_operators[0]
        if division_operators
        else GMatrix.zero(2, 2)
    )
    coherent_matrix = _v5_safe_g_product(
        (plus_operator, rho_plus, _g_adjoint(plus_operator))
    )
    coherent_probability = (
        _g_trace(coherent_matrix)
        if isinstance(coherent_matrix, GMatrix)
        else GZERO
    )
    incoherent_probability = sum(
        (
            _g_trace(
                _g_multiply(
                    _g_multiply(history, rho_plus), _g_adjoint(history)
                )
            )
            for history in histories
        ),
        GZERO,
    )
    plus_coefficients = (
        quantum.division_coefficients[0]
        if quantum.division_coefficients
        else ()
    )
    port_weighted_cross = GZERO
    if len(plus_coefficients) == len(histories):
        for left in range(len(histories)):
            for right in range(len(histories)):
                if left != right:
                    port_weighted_cross += (
                        plus_coefficients[left]
                        * plus_coefficients[right].conjugate()
                        * gram.data[left][right]
                    )
    unweighted_cross_operator = _g_add(
        _g_multiply(
            _g_multiply(histories[0], rho_plus), _g_adjoint(histories[1])
        ),
        _g_multiply(
            _g_multiply(histories[1], rho_plus), _g_adjoint(histories[0])
        ),
    )

    phase_adjoint_residual = _g_residual(
        _g_multiply(_g_adjoint(quantum.phase_control), quantum.phase_control),
        identity,
    )
    phase_transpose_residual = _g_residual(
        _g_multiply(_g_transpose(quantum.phase_control), quantum.phase_control),
        identity,
    )
    transition_endpoint: GMatrix | None = None
    if transition.shape == (2, 2):
        transition_endpoint = _g_multiply(
            h0,
            _g_multiply(
                _g_from_q(transition),
                GMatrix.from_rows(((1,), (0,)), ncols=1),
            ),
        )

    exact_input_valid = bool(
        quantum.root == V5_EXECUTABLE_ROOT
        and quantum.identifier == "quantum:phase-history"
        and quantum.carrier_id == "G2"
        and quantum.flag_carrier_id == "F"
        and quantum.base_x == expected_x
        and quantum.phase_control == expected_phase
        and quantum.gram_coefficients == (GONE, GI)
        and quantum.division_coefficients == expected_division_coefficients
        and set(continuation_index)
        == {"quantum-flag-I", "quantum-flag-Z"}
    )
    valid = bool(
        source_variant == "ADJOINT"
        and exact_input_valid
        and gram_residual.get("nonzero_count") == 0
        and gram_positive
        and tuple(row["determinant"] for row in gram_minors)
        == (quarter, quarter, GZERO)
        and _g_residual(abar, expected_abar).get("nonzero_count") == 0
        and _g_residual(awrong, expected_awrong).get("nonzero_count") == 0
        and z_scalar == GONE
        and abar_scalar == GONE
        and awrong_scalar == GZERO
        and gram_operator_identity_residual["nonzero_count"] == 0
        and len(division_operators) == 2
        and _g_residual(division_operators[0], expected_plus).get("nonzero_count")
        == 0
        and _g_residual(division_operators[1], expected_minus).get("nonzero_count")
        == 0
        and completeness_residual.get("nonzero_count") == 0
        and dilation_residual.get("nonzero_count") == 0
        and all(
            row["residual"].get("nonzero_count") == 0
            for row in flag_orthogonality_rows
        )
        and not continuation_issues
        and len(closure) == 2
        and recovery_valid
        and coherent_probability == GONE
        and incoherent_probability == half
        and port_weighted_cross == half
        and _g_nonzero_count(unweighted_cross_operator) == 0
        and phase_adjoint_residual.get("nonzero_count") == 0
        and isinstance(phase_transpose_residual.get("nonzero_count"), int)
        and phase_transpose_residual["nonzero_count"] > 0
        and transition_endpoint is not None
    )
    if not valid:
        issues.append("phase-bearing-quantum-control")
    issues.extend(continuation_issues)
    return {
        "source_variant": source_variant,
        "scorer_source_sha256": sha256_path(Path(__file__)),
        "history_operators": {"H_0": h0, "H_1": h1},
        "rho_plus": rho_plus,
        "D": gram,
        "expected_D": expected_gram,
        "D_residual": gram_residual,
        "D_principal_minors": gram_minors,
        "D_positive_semidefinite": gram_positive,
        "z": coefficients,
        "z_column": z_column,
        "z_bra": z_bra,
        "z_adjoint_D_z": z_scalar,
        "A_bar": abar,
        "A_wrong": awrong,
        "A_bar_residual": _g_residual(abar, expected_abar),
        "A_wrong_residual": _g_residual(awrong, expected_awrong),
        "A_bar_scalar": abar_scalar,
        "A_wrong_scalar": awrong_scalar,
        "gram_operator_identity_residual": gram_operator_identity_residual,
        "division_rows": tuple(division_rows),
        "sum_L_adjoint_L": completeness,
        "division_completeness_residual": completeness_residual,
        "flag_dilation": dilation,
        "flag_dilation_isometry_residual": dilation_residual,
        "orthogonal_flag_projectors": flag_projectors,
        "orthogonal_flag_residuals": tuple(flag_orthogonality_rows),
        "continuation_closure_size": len(closure),
        "continuation_closure_complete": closure_complete,
        "continuation_recovery_rows": tuple(recovery_rows),
        "coherent_p_plus": coherent_probability,
        "incoherent_history_sum": incoherent_probability,
        "port_weighted_cross_term": port_weighted_cross,
        "unweighted_cross_operator": unweighted_cross_operator,
        "unweighted_cross_operator_nonzero_count": _g_nonzero_count(
            unweighted_cross_operator
        ),
        "phase_P": quantum.phase_control,
        "P_adjoint_P_residual": phase_adjoint_residual,
        "P_transpose_P_residual": phase_transpose_residual,
        "transition_history_endpoint": transition_endpoint,
        "exact_input_valid": exact_input_valid,
        "issues": tuple(sorted(set(issues))),
        "valid": valid and not issues,
    }


def _v5_schema_projection(law: ExecutableLaw) -> dict[str, object]:
    normalized_transitions = tuple(
        replace(
            transition,
            matrix=QMatrix.zero(
                transition.matrix.nrows, transition.matrix.ncols
            ),
        )
        for transition in law.transitions
    )
    normalized = replace(
        law,
        identifier="<candidate-id>",
        transitions=normalized_transitions,
        cached_measurement_payloads=(),
        cached_restriction_rows=(),
        opaque_common_labels=(),
        auxiliary_dependency_claims=(),
    )
    return {
        "normalization": (
            "candidate identifier, T matrix, and explicitly nonsemantic "
            "cache/label/auxiliary fields removed"
        ),
        "projection": normalized.to_data(),
        "sha256": canonical_sha256(normalized.to_data()),
    }


def _v5_all_identifier_rows(law: ExecutableLaw) -> tuple[object, ...]:
    return (
        *law.carriers,
        *law.boundaries,
        *law.transitions,
        *law.occurrences,
        *law.valid_compositions,
        law.instrument,
        law.writer,
        law.rewrite,
        law.comparison,
        *law.interventions,
        *law.readers,
        *law.regional_supports,
        *law.continuations,
        law.owned_global_abc,
        law.alternate_global_abc,
        law.compiler,
        law.locality,
        *law.locality.regions,
        *law.locality.replacements,
        law.quantum,
        *law.quantum.flag_continuations,
        *law.auxiliary_dependency_claims,
    )


def _v5_prepare_executable_law(law: ExecutableLaw) -> dict[str, object]:
    issues: list[str] = []
    nodes: dict[str, dict[str, object]] = {}
    terminals: dict[str, str] = {}
    if law.root != V5_EXECUTABLE_ROOT:
        issues.append("law:wrong-root")
    if law.schema_id != V5_EXECUTABLE_SCHEMA:
        issues.append("law:wrong-schema")
    if law.identifier not in {"L_I", "L_X"}:
        issues.append("law:wrong-candidate-id")

    global_ids: dict[str, object] = {}
    for row in _v5_all_identifier_rows(law):
        identifier = getattr(row, "identifier", None)
        if not isinstance(identifier, str) or not identifier:
            issues.append("primitive:missing-id")
            continue
        if identifier in global_ids:
            issues.append(f"primitive:duplicate-id:{identifier}")
        else:
            global_ids[identifier] = row
        if getattr(row, "root", None) != law.root:
            issues.append(f"primitive:root-mismatch:{identifier}")

    carrier_index_raw = _v5_index(law.carriers, "carrier", issues)
    carrier_index = {
        key: value
        for key, value in carrier_index_raw.items()
        if isinstance(value, ExecutableCarrier)
    }
    expected_carriers = {
        "G2": (("0", "1"), ()),
        "F": (("0", "1"), ()),
        "G2xF": (
            ("(0,0)", "(0,1)", "(1,0)", "(1,1)"),
            ("G2", "F"),
        ),
        "G3": (("0", "1", "n"), ()),
        "G3xF": (
            (
                "(0,0)",
                "(0,1)",
                "(1,0)",
                "(1,1)",
                "(n,0)",
                "(n,1)",
            ),
            ("G3", "F"),
        ),
        "ABC": (
            ("000", "001", "010", "011", "100", "101", "110", "111"),
            ("A", "B", "C"),
        ),
    }
    if set(carrier_index) != set(expected_carriers):
        issues.append("carrier:registry-not-exact")
    carrier_rows: dict[str, object] = {}
    for carrier_id, carrier in sorted(carrier_index.items()):
        expected = expected_carriers.get(carrier_id)
        valid = bool(
            expected is not None
            and carrier.root == law.root
            and carrier.states == expected[0]
            and carrier.factor_ids == expected[1]
            and len(set(carrier.states)) == len(carrier.states)
        )
        if not valid:
            issues.append(f"carrier:typing:{carrier_id}")
        carrier_rows[carrier_id] = {
            "states": carrier.states,
            "factor_ids": carrier.factor_ids,
            "expected": expected,
            "valid": valid,
        }

    boundary_index_raw = _v5_index(law.boundaries, "boundary", issues)
    boundary_index = {
        key: value
        for key, value in boundary_index_raw.items()
        if isinstance(value, ExecutableBoundary)
    }
    expected_boundary_ids = {
        f"boundary:{carrier_id}" for carrier_id in expected_carriers
    }
    if set(boundary_index) != expected_boundary_ids:
        issues.append("boundary:registry-not-exact")
    boundary_rows: dict[str, object] = {}
    for boundary_id, boundary in sorted(boundary_index.items()):
        expected_carrier_id = boundary_id.removeprefix("boundary:")
        valid = bool(
            boundary.root == law.root
            and boundary.carrier_id == expected_carrier_id
            and expected_carrier_id in carrier_index
        )
        if not valid:
            issues.append(f"boundary:typing:{boundary_id}")
        boundary_rows[boundary_id] = {
            "carrier_id": boundary.carrier_id,
            "expected_carrier_id": expected_carrier_id,
            "valid": valid,
        }

    transition_index_raw = _v5_index(law.transitions, "transition", issues)
    transition_index = {
        key: value
        for key, value in transition_index_raw.items()
        if isinstance(value, ExecutableTransition)
    }
    transition = transition_index.get("T")
    if set(transition_index) != {"T"}:
        issues.append("transition:single-resolved-T-required")
    transition_stochastic: Mapping[str, object] = {
        "valid": False,
        "shape_residual": 1,
    }
    transition_permutation = False
    transition_inverse: QMatrix | None = None
    transition_involution_residual: Mapping[str, object] = {
        "nonzero_count": None
    }
    transition_registered = False
    if isinstance(transition, ExecutableTransition):
        transition_stochastic = _stochastic_matrix_measurement(
            transition.matrix, expected_shape=(2, 2)
        )
        transition_permutation, transition_inverse = _q_is_permutation(
            transition.matrix
        )
        if transition.matrix.shape == (2, 2):
            transition_involution_residual = _q_residual(
                qmultiply(transition.matrix, transition.matrix),
                QMatrix.identity(2),
            )
        transition_registered = transition.matrix in {
            QMatrix.identity(2),
            QMatrix.from_rows(((0, 1), (1, 0))),
        }
        transition_valid = bool(
            transition.root == law.root
            and transition.source_carrier_id == "G2"
            and transition.target_carrier_id == "G2"
            and transition_stochastic["valid"]
            and transition_permutation
            and transition_involution_residual.get("nonzero_count") == 0
            and transition_registered
        )
        if not transition_valid:
            issues.append("transition:reversible-registered-involution")
    else:
        transition_valid = False
        issues.append("transition:missing-T")
    for transition_id, transition_row in sorted(transition_index.items()):
        _v5_add_primitive_node(
            nodes,
            f"primitive:{transition_id}",
            transition_row,
            "typed-transition-primitive",
        )

    occurrence_index_raw = _v5_index(law.occurrences, "occurrence", issues)
    occurrence_index = {
        key: value
        for key, value in occurrence_index_raw.items()
        if isinstance(value, ExecutableOccurrence)
    }
    expected_occurrences = {
        row.identifier: row for row in _v5_occurrence_rows(law.root)
    }
    if set(occurrence_index) != set(expected_occurrences):
        issues.append("occurrence:registry-not-exact")
    occurrence_rows: dict[str, object] = {}
    occurrence_matrices: dict[str, QMatrix] = {}
    for occurrence_id, occurrence in sorted(occurrence_index.items()):
        expected = expected_occurrences.get(occurrence_id)
        resolved = transition_index.get(occurrence.primitive_id)
        valid = bool(
            expected is not None
            and occurrence == expected
            and isinstance(resolved, ExecutableTransition)
            and resolved.identifier == "T"
            and resolved.root == law.root
            and resolved.source_carrier_id == occurrence.source_carrier_id
            and resolved.target_carrier_id == occurrence.target_carrier_id
        )
        if not valid:
            issues.append(f"occurrence:unresolved-or-rewired:{occurrence_id}")
        if isinstance(resolved, ExecutableTransition):
            occurrence_matrices[occurrence_id] = resolved.matrix
            _v5_add_derived_node(
                nodes,
                occurrence_id,
                kind="typed-transition-occurrence",
                operands=(f"primitive:{resolved.identifier}",),
                derived=resolved.matrix,
                expected=(transition.matrix if isinstance(transition, ExecutableTransition) else None),
                residual=(
                    _q_residual(resolved.matrix, transition.matrix)
                    if isinstance(transition, ExecutableTransition)
                    else {"nonzero_count": None}
                ),
                carrier_trace=occurrence.typed_path,
            )
        occurrence_rows[occurrence_id] = {
            "primitive_id": occurrence.primitive_id,
            "consumer": occurrence.consumer,
            "source_carrier_id": occurrence.source_carrier_id,
            "target_carrier_id": occurrence.target_carrier_id,
            "typed_path": occurrence.typed_path,
            "resolved_transition": (
                resolved.to_data()
                if isinstance(resolved, ExecutableTransition)
                else None
            ),
            "valid": valid,
        }

    composition_index_raw = _v5_index(
        law.valid_compositions, "composition", issues
    )
    composition_index = {
        key: value
        for key, value in composition_index_raw.items()
        if isinstance(value, ExecutableComposition)
    }
    expected_compositions = {
        row.identifier: row for row in _v5_composition_rows(law.root)
    }
    if set(composition_index) != set(expected_compositions):
        issues.append("composition:registry-not-exact")
    composition_valid_by_consumer: dict[str, bool] = {}
    composition_rows: dict[str, object] = {}
    for composition_id, composition in sorted(composition_index.items()):
        expected = expected_compositions.get(composition_id)
        valid = composition == expected
        if not valid:
            issues.append(f"composition:not-exact:{composition_id}")
        composition_valid_by_consumer[composition.consumer] = valid
        composition_rows[composition_id] = {
            "actual": composition,
            "expected": expected,
            "valid": valid,
        }
        _v5_add_primitive_node(
            nodes, composition_id, composition, "typed-composition-primitive"
        )

    for identifier, primitive, kind in (
        (law.instrument.identifier, law.instrument, "conditioning-instrument"),
        (law.writer.identifier, law.writer, "record-writer"),
        (law.rewrite.identifier, law.rewrite, "regional-rewrite"),
        (law.comparison.identifier, law.comparison, "comparison-permutation"),
        (law.owned_global_abc.identifier, law.owned_global_abc, "owned-global-ABC"),
        (
            law.alternate_global_abc.identifier,
            law.alternate_global_abc,
            "alternate-global-ABC-control",
        ),
        (law.compiler.identifier, law.compiler, "uniform-region-compiler"),
        (law.locality.identifier, law.locality, "generated-locality-law"),
        (law.quantum.identifier, law.quantum, "phase-history-structure"),
    ):
        _v5_add_primitive_node(nodes, identifier, primitive, kind)
    for primitive, kind in (
        *((row, "intervention-set") for row in law.interventions),
        *((row, "reader") for row in law.readers),
        *((row, "regional-support") for row in law.regional_supports),
        *((row, "licensed-continuation") for row in law.continuations),
        *((row, "locality-region") for row in law.locality.regions),
        *((row, "locality-replacement") for row in law.locality.replacements),
        *((row, "quantum-flag-continuation") for row in law.quantum.flag_continuations),
    ):
        _v5_add_primitive_node(nodes, primitive.identifier, primitive, kind)

    if law.auxiliary_dependency_claims:
        issues.append("auxiliary-dependency-claim:not-admissible")

    return {
        "law": law,
        "issues": issues,
        "nodes": nodes,
        "terminals": terminals,
        "carrier_index": carrier_index,
        "boundary_index": boundary_index,
        "transition_index": transition_index,
        "transition": transition,
        "transition_valid": transition_valid,
        "transition_measurement": {
            "stochastic": transition_stochastic,
            "permutation": transition_permutation,
            "inverse": transition_inverse,
            "involution_residual": transition_involution_residual,
            "registered_I_or_X": transition_registered,
            "valid": transition_valid,
        },
        "occurrence_index": occurrence_index,
        "occurrence_matrices": occurrence_matrices,
        "composition_index": composition_index,
        "composition_valid_by_consumer": composition_valid_by_consumer,
        "structural_measurement": {
            "global_primitive_id_count": len(global_ids),
            "global_primitive_ids": tuple(sorted(global_ids)),
            "carriers": carrier_rows,
            "boundaries": boundary_rows,
            "transition": {
                "primitive": transition,
                "measurement": {
                    "stochastic": transition_stochastic,
                    "permutation": transition_permutation,
                    "inverse": transition_inverse,
                    "involution_residual": transition_involution_residual,
                    "registered_I_or_X": transition_registered,
                    "valid": transition_valid,
                },
            },
            "typed_occurrences": occurrence_rows,
            "valid_compositions": composition_rows,
            "cached_measurement_payloads_ignored": law.cached_measurement_payloads,
            "cached_restriction_rows_ignored": law.cached_restriction_rows,
            "opaque_common_labels_ignored": law.opaque_common_labels,
            "auxiliary_dependency_claims_not_admitted": law.auxiliary_dependency_claims,
        },
    }


def _v5_composition_ready(context: Mapping[str, object], consumer: str) -> bool:
    rows = context.get("composition_valid_by_consumer")
    return bool(isinstance(rows, Mapping) and rows.get(consumer))


def _v5_record_gate(
    context: MutableMapping[str, object], gate: str, valid: bool
) -> None:
    if not valid:
        issues = context["issues"]
        assert isinstance(issues, list)
        issues.append(f"gate:{gate}")


def _v5_measure_process_tensor_instrument(
    context: MutableMapping[str, object]
) -> dict[str, object]:
    nodes = context["nodes"]
    terminals = context["terminals"]
    occurrence_matrices = context["occurrence_matrices"]
    transition = context["transition"]
    law = context["law"]
    assert isinstance(nodes, dict)
    assert isinstance(terminals, dict)
    assert isinstance(occurrence_matrices, dict)
    assert isinstance(law, ExecutableLaw)

    process_ids = (
        "occ:T:process:a1",
        "occ:T:process:a2",
        "occ:T:process:b1",
        "occ:T:process:b2",
    )
    process_matrices = tuple(occurrence_matrices.get(row) for row in process_ids)
    cut_a = (
        qmultiply(process_matrices[1], process_matrices[0])
        if all(isinstance(row, QMatrix) for row in process_matrices[:2])
        else None
    )
    cut_b = (
        qmultiply(process_matrices[3], process_matrices[2])
        if all(isinstance(row, QMatrix) for row in process_matrices[2:])
        else None
    )
    expected_cut = QMatrix.identity(2)
    cut_a_residual = (
        _q_residual(cut_a, expected_cut)
        if isinstance(cut_a, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    cut_b_residual = (
        _q_residual(cut_b, expected_cut)
        if isinstance(cut_b, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    alternate_cut_residual = (
        _q_residual(cut_a, cut_b)
        if isinstance(cut_a, QMatrix) and isinstance(cut_b, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    process_valid = bool(
        context["transition_valid"]
        and _v5_composition_ready(context, "process-cut-a")
        and _v5_composition_ready(context, "process-cut-b")
        and all(isinstance(row, QMatrix) for row in process_matrices)
        and len(set(process_ids)) == 4
        and cut_a_residual.get("nonzero_count") == 0
        and cut_b_residual.get("nonzero_count") == 0
        and alternate_cut_residual.get("nonzero_count") == 0
    )
    _v5_add_derived_node(
        nodes,
        "derived:process-cut-a",
        kind="two-occurrence-process-cut",
        operands=("composition:process-cut-a", *process_ids[:2]),
        derived=cut_a,
        expected=expected_cut,
        residual=cut_a_residual,
        carrier_trace=("G2", "T:a1", "G2", "T:a2", "G2"),
    )
    _v5_add_derived_node(
        nodes,
        "derived:process-cut-b",
        kind="alternate-two-occurrence-process-cut",
        operands=("composition:process-cut-b", *process_ids[2:]),
        derived=cut_b,
        expected=expected_cut,
        residual=cut_b_residual,
        carrier_trace=("G2", "T:b1", "G2", "T:b2", "G2"),
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:horizontal-process",
        kind="classifier-native-coordinate",
        operands=("derived:process-cut-a", "derived:process-cut-b"),
        derived={"cut_a": cut_a, "cut_b": cut_b},
        expected={"cut_a": expected_cut, "cut_b": expected_cut},
        residual={
            "cut_a": cut_a_residual,
            "cut_b": cut_b_residual,
            "alternate_cut": alternate_cut_residual,
            "valid": process_valid,
        },
        carrier_trace=("boundary:G2", "two genuine T occurrences per cut"),
    )
    terminals["coordinate:horizontal-process"] = "horizontal_process"
    _v5_record_gate(context, "horizontal-process", process_valid)

    tensor_occurrence = occurrence_matrices.get("occ:T:tensor")
    tensor_map = (
        _q_kron(tensor_occurrence, QMatrix.identity(2))
        if isinstance(tensor_occurrence, QMatrix)
        else None
    )
    expected_tensor = (
        QMatrix.from_rows(
            (
                (
                    tensor_occurrence.data[left_row][left_column]
                    * (Fraction(1) if right_row == right_column else Fraction(0))
                    for left_column in range(2)
                    for right_column in range(2)
                )
                for left_row in range(2)
                for right_row in range(2)
            ),
            ncols=4,
        )
        if isinstance(tensor_occurrence, QMatrix)
        and tensor_occurrence.shape == (2, 2)
        else None
    )
    tensor_residual = (
        _q_residual(tensor_map, expected_tensor)
        if isinstance(tensor_map, QMatrix)
        and isinstance(expected_tensor, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    symmetry = _symmetry_permutation(2, 2)
    symmetry_naturality_residual = (
        _q_residual(
            qmultiply(symmetry, tensor_map),
            qmultiply(
                _q_kron(QMatrix.identity(2), tensor_occurrence), symmetry
            ),
        )
        if isinstance(tensor_map, QMatrix)
        and isinstance(tensor_occurrence, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    associator = _associator_permutation(2, 2, 2)
    left_associated = (
        _q_kron(tensor_map, QMatrix.identity(2))
        if isinstance(tensor_map, QMatrix)
        else None
    )
    right_associated = (
        _q_kron(tensor_occurrence, QMatrix.identity(4))
        if isinstance(tensor_occurrence, QMatrix)
        else None
    )
    associator_residual = (
        _q_residual(
            qmultiply(associator, left_associated),
            qmultiply(right_associated, associator),
        )
        if isinstance(left_associated, QMatrix)
        and isinstance(right_associated, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    interchange_residual = (
        _q_residual(
            qmultiply(tensor_map, tensor_map),
            _q_kron(
                qmultiply(tensor_occurrence, tensor_occurrence),
                QMatrix.identity(2),
            ),
        )
        if isinstance(tensor_map, QMatrix)
        and isinstance(tensor_occurrence, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    unit_residual = (
        _q_residual(
            _q_kron(tensor_occurrence, QMatrix.identity(1)),
            tensor_occurrence,
        )
        if isinstance(tensor_occurrence, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    tensor_valid = bool(
        _v5_composition_ready(context, "tensor-interface")
        and isinstance(tensor_map, QMatrix)
        and tensor_residual.get("nonzero_count") == 0
        and symmetry_naturality_residual.get("nonzero_count") == 0
        and associator_residual.get("nonzero_count") == 0
        and interchange_residual.get("nonzero_count") == 0
        and unit_residual.get("nonzero_count") == 0
    )
    _v5_add_derived_node(
        nodes,
        "derived:tensor-interface",
        kind="ordered-tensor-transition",
        operands=("composition:tensor-interface", "occ:T:tensor"),
        derived=tensor_map,
        expected=expected_tensor,
        residual={
            "matrix": tensor_residual,
            "unit": unit_residual,
            "associator": associator_residual,
            "symmetry_naturality": symmetry_naturality_residual,
            "interchange": interchange_residual,
        },
        carrier_trace=("G2xF", "(T tensor I_F)", "G2xF"),
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:tensor",
        kind="classifier-native-coordinate",
        operands=("derived:tensor-interface",),
        derived=tensor_map,
        expected=expected_tensor,
        residual={"valid": tensor_valid, "matrix": tensor_residual},
        carrier_trace=("left-major-lexicographic",),
    )
    terminals["coordinate:tensor"] = "tensor_gluing_interfaces"
    _v5_record_gate(context, "tensor", tensor_valid)

    instrument = law.instrument
    branches = instrument.branch_matrices
    branch_shapes = tuple(branch.shape for branch in branches)
    branches_typed = bool(
        instrument.root == law.root
        and instrument.identifier == "instrument:Q"
        and instrument.source_carrier_id == "G2"
        and instrument.target_carrier_id == "G2"
        and instrument.flag_carrier_id == "F"
        and instrument.branch_ids == ("Q_0", "Q_1")
        and len(branches) == 2
        and all(branch.shape == (2, 2) for branch in branches)
        and all(
            item >= 0
            for branch in branches
            for row in branch.data
            for item in row
        )
    )
    branch_sum = QMatrix.zero(2, 2)
    if branches_typed:
        for branch in branches:
            branch_sum = qadd(branch_sum, branch)
    expected_q0 = QMatrix.from_rows(((1, 0), (0, 0)))
    expected_q1 = QMatrix.from_rows(((0, 0), (0, 1)))
    completeness_residual = _q_residual(branch_sum, QMatrix.identity(2))
    branch_semantics = bool(
        branches_typed
        and branches == (expected_q0, expected_q1)
        and branches[0] != branches[1]
        and all(qrank(branch) == 1 for branch in branches)
        and _q_residual(qmultiply(branches[0], branches[0]), branches[0]).get(
            "nonzero_count"
        )
        == 0
        and _q_residual(qmultiply(branches[1], branches[1]), branches[1]).get(
            "nonzero_count"
        )
        == 0
        and _q_nonzero_count(qmultiply(branches[0], branches[1])) == 0
        and _q_nonzero_count(qmultiply(branches[1], branches[0])) == 0
    )
    flagged = (
        qvstack(branches, ncols=2)
        if branches_typed
        else QMatrix.zero(0, 2)
    )
    flagged_residual = _q_column_residual(flagged) if flagged.nrows else (Fraction(1),)
    subnormalization_rows = tuple(
        {
            "branch_id": branch_id,
            "column_sums": tuple(
                sum((branch.data[row][column] for row in range(2)), Fraction(0))
                for column in range(2)
            ),
            "subnormalized": all(
                Fraction(0)
                <= sum(
                    (branch.data[row][column] for row in range(2)),
                    Fraction(0),
                )
                <= Fraction(1)
                for column in range(2)
            ),
        }
        for branch_id, branch in zip(instrument.branch_ids, branches)
    ) if branches_typed else ()
    instrument_valid = bool(
        branches_typed
        and completeness_residual.get("nonzero_count") == 0
        and all(value == 0 for value in flagged_residual)
        and all(row["subnormalized"] for row in subnormalization_rows)
        and branch_semantics
    )
    ontology_occurrence = occurrence_matrices.get("occ:T:ontology")
    conditioned_after_t = (
        qmultiply(branch_sum, ontology_occurrence)
        if isinstance(ontology_occurrence, QMatrix)
        else None
    )
    _v5_add_derived_node(
        nodes,
        "derived:conditioning-after-T",
        kind="conditioned-transition-total",
        operands=("instrument:Q", "occ:T:ontology"),
        derived=conditioned_after_t,
        expected=ontology_occurrence,
        residual=(
            _q_residual(conditioned_after_t, ontology_occurrence)
            if isinstance(conditioned_after_t, QMatrix)
            and isinstance(ontology_occurrence, QMatrix)
            else {"shape_match": False, "nonzero_count": None}
        ),
        carrier_trace=("G2", "T", "G2", "Q_tot", "G2"),
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:instrument",
        kind="classifier-native-coordinate",
        operands=("derived:conditioning-after-T",),
        derived={"Q_tot": branch_sum, "flagged": flagged},
        expected={"Q_tot": QMatrix.identity(2), "branches": (expected_q0, expected_q1)},
        residual={
            "completeness": completeness_residual,
            "branch_semantics": branch_semantics,
            "valid": instrument_valid,
        },
        carrier_trace=("G2", "Q={Q_0,Q_1}", "G2xF"),
    )
    terminals["coordinate:instrument"] = "conditioning_instrument"
    _v5_record_gate(context, "conditioning-instrument", instrument_valid)
    return {
        "process": {
            "occurrence_ids": process_ids,
            "cut_a": cut_a,
            "cut_b": cut_b,
            "cut_a_residual": cut_a_residual,
            "cut_b_residual": cut_b_residual,
            "alternate_cut_residual": alternate_cut_residual,
            "valid": process_valid,
        },
        "tensor": {
            "ordering": "left-major-lexicographic",
            "T_tensor_I_F": tensor_map,
            "independently_enumerated_expected": expected_tensor,
            "matrix_residual": tensor_residual,
            "unit_residual": unit_residual,
            "associator": associator,
            "associator_naturality_residual": associator_residual,
            "symmetry": symmetry,
            "symmetry_naturality_residual": symmetry_naturality_residual,
            "interchange_residual": interchange_residual,
            "valid": tensor_valid,
        },
        "instrument": {
            "branch_ids": instrument.branch_ids,
            "branch_shapes": branch_shapes,
            "branch_matrices": branches,
            "Q_tot": branch_sum,
            "completeness_residual": completeness_residual,
            "flagged_total": flagged,
            "flagged_column_residual": flagged_residual,
            "subnormalization_rows": subnormalization_rows,
            "semantic_projective_branches": branch_semantics,
            "conditioned_after_T": conditioned_after_t,
            "valid": instrument_valid,
        },
    }


def _v5_measure_ontology_chain(
    context: MutableMapping[str, object],
    instrument_measurement: Mapping[str, object],
    observed_endpoint: QMatrix,
) -> dict[str, object]:
    law = context["law"]
    nodes = context["nodes"]
    terminals = context["terminals"]
    carrier_index = context["carrier_index"]
    occurrence_matrices = context["occurrence_matrices"]
    assert isinstance(law, ExecutableLaw)
    assert isinstance(nodes, dict)
    assert isinstance(terminals, dict)
    assert isinstance(carrier_index, dict)
    assert isinstance(occurrence_matrices, dict)

    writer = law.writer
    expected_writer = QMatrix.from_rows(
        ((1, 0), (0, 0), (0, 0), (0, 1))
    )
    writer_stochastic = _stochastic_matrix_measurement(
        writer.matrix, expected_shape=(4, 2)
    )
    writer_residual = _q_residual(writer.matrix, expected_writer)
    direct_writer_reader = _target_reader_matrix(2, 2)
    direct_writer_recovery = (
        qmultiply(direct_writer_reader, writer.matrix)
        if writer.matrix.shape == (4, 2)
        else None
    )
    direct_writer_recovery_residual = (
        _q_residual(direct_writer_recovery, QMatrix.identity(2))
        if isinstance(direct_writer_recovery, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    conditioning_valid = bool(instrument_measurement.get("valid"))
    writer_valid = bool(
        conditioning_valid
        and writer.root == law.root
        and writer.identifier == "writer:W"
        and writer.source_carrier_id == "G2"
        and writer.target_carrier_id == "G2xF"
        and writer_stochastic["valid"]
        and writer_residual.get("nonzero_count") == 0
        and direct_writer_recovery_residual.get("nonzero_count") == 0
    )

    rewrite = law.rewrite
    expected_theta = QMatrix.from_rows(((1, 0), (0, 0), (0, 1)))
    expected_iota = QMatrix.from_rows(((1, 0), (0, 1), (0, 0)))
    theta_residual = _q_residual(rewrite.theta, expected_theta)
    iota_residual = _q_residual(rewrite.passive_inclusion, expected_iota)
    theta_stochastic = _stochastic_matrix_measurement(
        rewrite.theta, expected_shape=(3, 2)
    )
    iota_stochastic = _stochastic_matrix_measurement(
        rewrite.passive_inclusion, expected_shape=(3, 2)
    )
    theta_tensor_identity = (
        _q_kron(rewrite.theta, QMatrix.identity(2))
        if rewrite.theta.shape == (3, 2)
        else None
    )
    iota_tensor_identity = (
        _q_kron(rewrite.passive_inclusion, QMatrix.identity(2))
        if rewrite.passive_inclusion.shape == (3, 2)
        else None
    )
    expected_theta_tensor_identity = _q_kron(
        expected_theta, QMatrix.identity(2)
    )
    expected_iota_tensor_identity = _q_kron(
        expected_iota, QMatrix.identity(2)
    )
    theta_tensor_residual = (
        _q_residual(theta_tensor_identity, expected_theta_tensor_identity)
        if isinstance(theta_tensor_identity, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    iota_tensor_residual = (
        _q_residual(iota_tensor_identity, expected_iota_tensor_identity)
        if isinstance(iota_tensor_identity, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )

    reader_index_raw = _v5_index(law.readers, "ontology-reader", context["issues"])
    reader_index = {
        key: value
        for key, value in reader_index_raw.items()
        if isinstance(value, ExecutableReader)
    }
    output_reader = reader_index.get("reader:output-flag")
    expected_output_reader = _target_reader_matrix(3, 2)
    output_reader_residual = (
        _q_residual(output_reader.matrix, expected_output_reader)
        if isinstance(output_reader, ExecutableReader)
        else {"shape_match": False, "nonzero_count": None}
    )
    output_reader_valid = bool(
        isinstance(output_reader, ExecutableReader)
        and output_reader.root == law.root
        and output_reader.carrier_id == "G3xF"
        and output_reader.factor_carrier_id == "F"
        and output_reader.outcomes == ("0", "1")
        and output_reader_residual.get("nonzero_count") == 0
    )

    support_index_raw = _v5_index(
        law.regional_supports, "regional-support", context["issues"]
    )
    support_index = {
        key: value
        for key, value in support_index_raw.items()
        if isinstance(value, ExecutableRegionalSupport)
    }
    support = support_index.get("support:new-n")
    output_carrier = carrier_index.get("G3xF")
    support_effect = (
        _v5_support_effect(output_carrier, support.state_ids)
        if isinstance(output_carrier, ExecutableCarrier)
        and isinstance(support, ExecutableRegionalSupport)
        else None
    )
    support_valid = bool(
        set(support_index) == {"support:new-n"}
        and isinstance(support, ExecutableRegionalSupport)
        and support.root == law.root
        and support.carrier_id == "G3xF"
        and support.state_ids == ("(n,0)", "(n,1)")
        and isinstance(support_effect, QMatrix)
        and support_effect
        == QMatrix.from_rows(((0, 0, 0, 0, 1, 1),), ncols=6)
    )

    occurrence = occurrence_matrices.get("occ:T:ontology")
    q_total = instrument_measurement.get("Q_tot")
    p_i = (
        _v5_safe_q_product(
            (
                theta_tensor_identity,
                writer.matrix,
                q_total,
                occurrence,
            )
        )
        if isinstance(theta_tensor_identity, QMatrix)
        and isinstance(q_total, QMatrix)
        and isinstance(occurrence, QMatrix)
        else None
    )
    expected_p_i = (
        _v5_safe_q_product(
            (
                expected_theta_tensor_identity,
                expected_writer,
                QMatrix.identity(2),
                occurrence,
            )
        )
        if isinstance(occurrence, QMatrix)
        else None
    )
    passive_p_i = (
        _v5_safe_q_product(
            (
                iota_tensor_identity,
                writer.matrix,
                q_total,
                occurrence,
            )
        )
        if isinstance(iota_tensor_identity, QMatrix)
        and isinstance(q_total, QMatrix)
        and isinstance(occurrence, QMatrix)
        else None
    )
    delta_zero = _v5_basis_state(2, 0)
    selection_response_map = (
        qmultiply(output_reader.matrix, p_i)
        if isinstance(output_reader, ExecutableReader)
        and isinstance(p_i, QMatrix)
        and output_reader.matrix.ncols == p_i.nrows
        else None
    )
    selection_response = (
        qmultiply(selection_response_map, delta_zero)
        if isinstance(selection_response_map, QMatrix)
        else None
    )
    selection_residual = (
        _q_residual(selection_response, observed_endpoint)
        if isinstance(selection_response, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    support_response_map = (
        qmultiply(support_effect, p_i)
        if isinstance(support_effect, QMatrix) and isinstance(p_i, QMatrix)
        else None
    )
    expected_support_response_map = (
        qmultiply(support_effect, expected_p_i)
        if isinstance(support_effect, QMatrix)
        and isinstance(expected_p_i, QMatrix)
        else None
    )
    passive_support_response_map = (
        qmultiply(support_effect, passive_p_i)
        if isinstance(support_effect, QMatrix)
        and isinstance(passive_p_i, QMatrix)
        else None
    )

    joint_writer_rewrite = (
        qmultiply(theta_tensor_identity, writer.matrix)
        if isinstance(theta_tensor_identity, QMatrix)
        and theta_tensor_identity.ncols == writer.matrix.nrows
        else None
    )
    passive_joint = (
        qmultiply(iota_tensor_identity, writer.matrix)
        if isinstance(iota_tensor_identity, QMatrix)
        and iota_tensor_identity.ncols == writer.matrix.nrows
        else None
    )
    created_state = (
        qmultiply(joint_writer_rewrite, _v5_basis_state(2, 1))
        if isinstance(joint_writer_rewrite, QMatrix)
        else None
    )
    passive_state = (
        qmultiply(passive_joint, _v5_basis_state(2, 1))
        if isinstance(passive_joint, QMatrix)
        else None
    )
    created_response = (
        qmultiply(support_effect, created_state)
        if isinstance(support_effect, QMatrix)
        and isinstance(created_state, QMatrix)
        else None
    )
    passive_response = (
        qmultiply(support_effect, passive_state)
        if isinstance(support_effect, QMatrix)
        and isinstance(passive_state, QMatrix)
        else None
    )

    continuation_index_raw = _v5_index(
        law.continuations, "ontology-continuation", context["issues"]
    )
    continuation_index = {
        key: value
        for key, value in continuation_index_raw.items()
        if isinstance(value, ExecutableContinuation)
    }
    expected_continuation_ids = {
        "continuation:I",
        "continuation:X_G3",
    }
    continuation_rows: dict[str, object] = {}
    continuation_generators: list[QMatrix] = []
    continuations_typed = bool(
        set(continuation_index) == expected_continuation_ids
        and set(law.licensed_continuation_ids) == expected_continuation_ids
        and len(law.licensed_continuation_ids)
        == len(set(law.licensed_continuation_ids))
        and set(continuation_index) == set(law.licensed_continuation_ids)
    )
    for continuation_id, continuation in sorted(continuation_index.items()):
        stochastic = _stochastic_matrix_measurement(
            continuation.matrix, expected_shape=(6, 6)
        )
        permutation, inverse = _q_is_permutation(continuation.matrix)
        typed = bool(
            continuation.root == law.root
            and continuation.carrier_id == "G3xF"
            and stochastic["valid"]
            and permutation
        )
        continuations_typed = continuations_typed and typed
        if typed:
            continuation_generators.append(continuation.matrix)
        continuation_rows[continuation_id] = {
            "stochastic": stochastic,
            "permutation": permutation,
            "inverse": inverse,
            "licensed": continuation_id in law.licensed_continuation_ids,
            "typed": typed,
        }
    closure, closure_complete = _v5_close_q_matrices(continuation_generators)
    recovery_rows: list[dict[str, object]] = []
    recovery_valid = bool(
        continuations_typed
        and closure_complete
        and len(closure) == 2
        and isinstance(joint_writer_rewrite, QMatrix)
        and output_reader_valid
    )
    baseline_reader_after_joint = (
        qmultiply(output_reader.matrix, joint_writer_rewrite)
        if isinstance(output_reader, ExecutableReader)
        and isinstance(joint_writer_rewrite, QMatrix)
        else None
    )
    for word_hash, continuation in sorted(closure.items()):
        recovered = (
            _v5_safe_q_product(
                (output_reader.matrix, continuation, joint_writer_rewrite)
            )
            if isinstance(output_reader, ExecutableReader)
            and isinstance(joint_writer_rewrite, QMatrix)
            else None
        )
        recovery_residual = (
            _q_residual(recovered, baseline_reader_after_joint)
            if isinstance(recovered, QMatrix)
            and isinstance(baseline_reader_after_joint, QMatrix)
            else {"shape_match": False, "nonzero_count": None}
        )
        word_valid = recovery_residual.get("nonzero_count") == 0
        recovery_valid = recovery_valid and word_valid
        recovery_rows.append(
            {
                "word_sha256": word_hash,
                "word_matrix": continuation,
                "R_F_U_word_Theta_tensor_I_W": recovered,
                "expected_R_F_Theta_tensor_I_W": baseline_reader_after_joint,
                "recovery_residual": recovery_residual,
                "valid": word_valid,
            }
        )

    literal_chain = bool(
        rewrite.root == law.root
        and rewrite.identifier == "rewrite:Theta"
        and rewrite.source_carrier_id == writer.target_carrier_id
        and writer.target_carrier_id == "G2xF"
        and rewrite.target_carrier_id == "G3xF"
        and rewrite.base_source_carrier_id == "G2"
        and rewrite.base_target_carrier_id == "G3"
        and rewrite.flag_carrier_id == "F"
        and _v5_composition_ready(context, "ontology-calibration")
    )
    rewrite_valid = bool(
        writer_valid
        and literal_chain
        and theta_stochastic["valid"]
        and iota_stochastic["valid"]
        and theta_residual.get("nonzero_count") == 0
        and iota_residual.get("nonzero_count") == 0
        and theta_tensor_residual.get("nonzero_count") == 0
        and iota_tensor_residual.get("nonzero_count") == 0
        and support_valid
        and output_reader_valid
        and isinstance(p_i, QMatrix)
        and isinstance(selection_response, QMatrix)
        and isinstance(selection_response_map, QMatrix)
        and isinstance(support_response_map, QMatrix)
        and isinstance(support_response_map, QMatrix)
        and support_response_map == expected_support_response_map
        and sum(support_response_map.data[0], Fraction(0)) == 1
        and passive_support_response_map
        == QMatrix.from_rows(((0, 0),), ncols=2)
        and created_response == QMatrix.from_rows(((1,),), ncols=1)
        and passive_response == QMatrix.from_rows(((0,),), ncols=1)
        and baseline_reader_after_joint == QMatrix.identity(2)
        and recovery_valid
    )
    ontology_role = (
        "REGION-REWRITING"
        if rewrite_valid
        else "RECORD-WRITING-ON-FIXED-ALGEBRA"
        if writer_valid
        else "FIXED-ALGEBRA-CONDITIONING"
        if conditioning_valid
        else "STATIC-RESPONSE"
    )
    ontology_valid = ontology_role == "REGION-REWRITING"
    _v5_record_gate(context, "ontology-chain", ontology_valid)

    _v5_add_derived_node(
        nodes,
        "derived:ontology:J",
        kind="writer-rewrite-composite",
        operands=("writer:W", "rewrite:Theta"),
        derived=joint_writer_rewrite,
        expected=QMatrix.from_rows(
            ((1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 1))
        ),
        residual=(
            _q_residual(
                joint_writer_rewrite,
                QMatrix.from_rows(
                    ((1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 1))
                ),
            )
            if isinstance(joint_writer_rewrite, QMatrix)
            else {"shape_match": False, "nonzero_count": None}
        ),
        carrier_trace=("G2", "W", writer.target_carrier_id, "Theta tensor I_F", "G3xF"),
    )
    _v5_add_derived_node(
        nodes,
        "derived:ontology:P_i",
        kind="candidate-calibration-map",
        operands=(
            "composition:ontology-calibration",
            "derived:conditioning-after-T",
            "writer:W",
            "rewrite:Theta",
        ),
        derived=p_i,
        expected=expected_p_i,
        residual=(
            _q_residual(
                p_i,
                expected_p_i,
            )
            if isinstance(p_i, QMatrix)
            and isinstance(occurrence, QMatrix)
            else {"shape_match": False, "nonzero_count": None}
        ),
        carrier_trace=(
            "G2",
            "T_i",
            "G2",
            "Q_tot",
            "G2",
            "W",
            "G2xF",
            "Theta tensor I_F",
            "G3xF",
        ),
    )
    _v5_add_derived_node(
        nodes,
        "derived:ontology:r_i",
        kind="typed-effect-contraction",
        operands=("derived:ontology:P_i", "reader:output-flag"),
        derived=selection_response,
        expected=observed_endpoint,
        residual=selection_residual,
        carrier_trace=("G3xF", "R_F", "F", "evaluate at delta_0"),
    )
    _v5_add_derived_node(
        nodes,
        "derived:ontology:new-support",
        kind="compiled-output-carrier-effect",
        operands=("derived:ontology:P_i", "support:new-n"),
        derived=support_response_map,
        expected=expected_support_response_map,
        residual=(
            _q_residual(
                support_response_map,
                expected_support_response_map,
            )
            if isinstance(support_response_map, QMatrix)
            else {"shape_match": False, "nonzero_count": None}
        ),
        carrier_trace=("G3xF", "effect:{(n,0),(n,1)}", "scalar"),
    )
    _v5_add_derived_node(
        nodes,
        "derived:ontology:passive-control",
        kind="passive-inclusion-control",
        operands=("writer:W", "rewrite:Theta", "support:new-n"),
        derived=passive_support_response_map,
        expected=QMatrix.from_rows(((0, 0),), ncols=2),
        residual=(
            _q_residual(
                passive_support_response_map,
                QMatrix.from_rows(((0, 0),), ncols=2),
            )
            if isinstance(passive_support_response_map, QMatrix)
            else {"shape_match": False, "nonzero_count": None}
        ),
        carrier_trace=("G2xF", "iota tensor I_F", "old G2 support"),
    )
    closure_operands = tuple(sorted(continuation_index))
    _v5_add_derived_node(
        nodes,
        "derived:ontology:continuation-closure",
        kind="full-licensed-continuation-recovery",
        operands=("derived:ontology:J", "reader:output-flag", *closure_operands),
        derived=tuple(recovery_rows),
        expected={"all_recover": True, "closure_size": 2},
        residual={
            "all_recover": recovery_valid,
            "closure_size_residual": len(closure) - 2,
        },
        carrier_trace=("G3xF", "U_word", "G3xF", "R_F", "F"),
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:ontology",
        kind="classifier-native-coordinate",
        operands=(
            "derived:ontology:P_i",
            "derived:ontology:r_i",
            "derived:ontology:new-support",
            "derived:ontology:passive-control",
            "derived:ontology:continuation-closure",
        ),
        derived={
            "P_i": p_i,
            "r_i": selection_response,
            "role": ontology_role,
        },
        expected={"role": "REGION-REWRITING"},
        residual={"valid": ontology_valid, "selection": selection_residual},
        carrier_trace=(
            "G2 --T_i--> G2 --Q_tot--> G2 --W--> G2xF "
            "--Theta tensor I_F--> G3xF --readers--> outcomes",
        ),
    )
    terminals["coordinate:ontology"] = "ontology_calibration"
    _v5_add_derived_node(
        nodes,
        "coordinate:law-selection-response",
        kind="classifier-native-selection-coordinate",
        operands=("derived:ontology:r_i",),
        derived={
            "r_i": selection_response,
            "observed_endpoint": observed_endpoint,
        },
        expected={"observed_endpoint": observed_endpoint},
        residual=selection_residual,
        carrier_trace=("G2", "delta_0", "P_i", "G3xF", "R_F", "F"),
    )
    terminals["coordinate:law-selection-response"] = "law_selection_response"
    return {
        "conditioning": {
            "Q_tot": q_total,
            "valid": conditioning_valid,
        },
        "record_writing": {
            "writer": writer,
            "expected_W": expected_writer,
            "writer_stochastic": writer_stochastic,
            "writer_residual": writer_residual,
            "direct_flag_reader": direct_writer_reader,
            "direct_recovery": direct_writer_recovery,
            "direct_recovery_residual": direct_writer_recovery_residual,
            "valid": writer_valid,
        },
        "regional_rewrite": {
            "rewrite": rewrite,
            "literal_writer-target-rewrite-source": literal_chain,
            "Theta": rewrite.theta,
            "Theta_residual": theta_residual,
            "iota": rewrite.passive_inclusion,
            "iota_residual": iota_residual,
            "Theta_tensor_I_F_recomputed": theta_tensor_identity,
            "Theta_tensor_I_F_expected": expected_theta_tensor_identity,
            "Theta_tensor_I_F_residual": theta_tensor_residual,
            "iota_tensor_I_F_recomputed": iota_tensor_identity,
            "iota_tensor_I_F_expected": expected_iota_tensor_identity,
            "iota_tensor_I_F_residual": iota_tensor_residual,
            "supplied_tensor_lift_ignored": rewrite.supplied_tensor_lift,
            "joint_writer_rewrite": joint_writer_rewrite,
            "compiled_new_support_effect": support_effect,
            "created_state": created_state,
            "created_response": created_response,
            "passive_state": passive_state,
            "passive_response": passive_response,
            "valid": rewrite_valid,
        },
        "delayed_reader_and_continuations": {
            "output_reader": output_reader,
            "expected_output_reader": expected_output_reader,
            "reader_residual": output_reader_residual,
            "reader_valid": output_reader_valid,
            "licensed_continuation_ids": law.licensed_continuation_ids,
            "actual_continuation_ids": tuple(sorted(continuation_index)),
            "continuation_rows": continuation_rows,
            "closure_matrices": dict(sorted(closure.items())),
            "closure_complete": closure_complete,
            "recovery_rows": tuple(recovery_rows),
            "valid": recovery_valid,
        },
        "P_i": p_i,
        "P_passive_i": passive_p_i,
        "R_F_P_i": selection_response_map,
        "r_i": selection_response,
        "selection_input": delta_zero,
        "observed_endpoint": observed_endpoint,
        "selection_residual": selection_residual,
        "new_support_response_map": support_response_map,
        "passive_support_response_map": passive_support_response_map,
        "role": ontology_role,
        "valid": ontology_valid,
    }


def _v5_measure_comparison_influence(
    context: MutableMapping[str, object]
) -> dict[str, object]:
    law = context["law"]
    nodes = context["nodes"]
    terminals = context["terminals"]
    occurrence_matrices = context["occurrence_matrices"]
    assert isinstance(law, ExecutableLaw)
    assert isinstance(nodes, dict)
    assert isinstance(terminals, dict)
    assert isinstance(occurrence_matrices, dict)

    comparison = law.comparison
    comparison_occurrence = occurrence_matrices.get("occ:T:comparison")
    permutation_valid, inverse = _q_is_permutation(comparison.permutation)
    expected_flip = QMatrix.from_rows(((0, 1), (1, 0)))
    permutation_residual = _q_residual(comparison.permutation, expected_flip)
    conjugated_transition = (
        _v5_safe_q_product(
            (comparison.permutation, comparison_occurrence, inverse)
        )
        if isinstance(comparison_occurrence, QMatrix)
        and isinstance(inverse, QMatrix)
        else None
    )
    naturality_residual = (
        _q_residual(
            qmultiply(comparison.permutation, comparison_occurrence),
            qmultiply(conjugated_transition, comparison.permutation),
        )
        if isinstance(comparison_occurrence, QMatrix)
        and isinstance(conjugated_transition, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    transported_state = (
        qmultiply(comparison.permutation, comparison.calibrated_state)
        if comparison.calibrated_state.shape == (2, 1)
        else None
    )
    transported_effect = (
        qmultiply(comparison.calibrated_effect, inverse)
        if isinstance(inverse, QMatrix)
        and comparison.calibrated_effect.shape == (1, 2)
        else None
    )
    state_measurement = _stochastic_matrix_measurement(
        comparison.calibrated_state, expected_shape=(2, 1)
    )
    effect_entries_valid = bool(
        comparison.calibrated_effect.shape == (1, 2)
        and all(
            item in {Fraction(0), Fraction(1)}
            for row in comparison.calibrated_effect.data
            for item in row
        )
        and sum(comparison.calibrated_effect.data[0], Fraction(0)) == 1
    )
    comparison_valid = bool(
        comparison.root == law.root
        and comparison.identifier == "comparison:P"
        and comparison.carrier_id == "G2"
        and _v5_composition_ready(context, "comparison")
        and permutation_valid
        and permutation_residual.get("nonzero_count") == 0
        and state_measurement["valid"]
        and effect_entries_valid
        and transported_state != comparison.calibrated_state
        and transported_effect != comparison.calibrated_effect
        and naturality_residual.get("nonzero_count") == 0
    )
    _v5_add_derived_node(
        nodes,
        "derived:comparison-square",
        kind="permutation-naturality-square",
        operands=(
            "composition:comparison",
            "comparison:P",
            "occ:T:comparison",
        ),
        derived={
            "P_T": (
                qmultiply(comparison.permutation, comparison_occurrence)
                if isinstance(comparison_occurrence, QMatrix)
                else None
            ),
            "T_prime_P": (
                qmultiply(conjugated_transition, comparison.permutation)
                if isinstance(conjugated_transition, QMatrix)
                else None
            ),
            "transported_state": transported_state,
            "transported_effect": transported_effect,
        },
        expected={"naturality_square_commutes": True},
        residual={
            "square": naturality_residual,
            "state_moved": transported_state != comparison.calibrated_state,
            "effect_moved": transported_effect != comparison.calibrated_effect,
        },
        carrier_trace=("G2", "T", "G2", "P", "G2"),
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:comparison",
        kind="classifier-native-coordinate",
        operands=("derived:comparison-square",),
        derived={
            "conjugated_transition": conjugated_transition,
            "transported_state": transported_state,
            "transported_effect": transported_effect,
        },
        expected={"nonidentity_naturality": True},
        residual={"square": naturality_residual, "valid": comparison_valid},
        carrier_trace=("comparison transport on G2",),
    )
    terminals["coordinate:comparison"] = "comparison_selected"
    _v5_record_gate(context, "comparison", comparison_valid)

    intervention_index_raw = _v5_index(
        law.interventions, "intervention", context["issues"]
    )
    intervention_index = {
        key: value
        for key, value in intervention_index_raw.items()
        if isinstance(value, ExecutableInterventionSet)
    }
    reader_index_raw = _v5_index(law.readers, "reader", context["issues"])
    reader_index = {
        key: value
        for key, value in reader_index_raw.items()
        if isinstance(value, ExecutableReader)
    }
    expected_reset_zero = QMatrix.from_rows(((1, 1), (0, 0)))
    expected_reset_one = QMatrix.from_rows(((0, 0), (1, 1)))
    delta_zero = _v5_basis_state(2, 0)

    causal = intervention_index.get("intervention:causal")
    causal_reader = reader_index.get("reader:causal")
    causal_occurrence = occurrence_matrices.get("occ:T:causal")
    causal_responses: list[tuple[str, QMatrix]] = []
    causal_path_rows: list[dict[str, object]] = []
    causal_typed = bool(
        isinstance(causal, ExecutableInterventionSet)
        and isinstance(causal_reader, ExecutableReader)
        and isinstance(causal_occurrence, QMatrix)
        and causal.root == law.root
        and causal.carrier_id == "G2"
        and causal.alternative_ids == ("reset-zero", "reset-one")
        and causal.base_alternative_matrices
        == (expected_reset_zero, expected_reset_one)
        and causal.propagation_matrix is None
        and causal.reader_id == "reader:causal"
        and causal_reader.root == law.root
        and causal_reader.carrier_id == "G2"
        and causal_reader.factor_carrier_id == "G2"
        and causal_reader.outcomes == ("0", "1")
        and causal_reader.matrix == QMatrix.identity(2)
        and _v5_composition_ready(context, "causal-order")
    )
    if causal_typed:
        assert isinstance(causal, ExecutableInterventionSet)
        assert isinstance(causal_reader, ExecutableReader)
        assert isinstance(causal_occurrence, QMatrix)
        for alternative_index, (alternative_id, reset) in enumerate(
            zip(causal.alternative_ids, causal.base_alternative_matrices)
        ):
            response = _v5_safe_q_product(
                (causal_reader.matrix, causal_occurrence, reset, delta_zero)
            )
            expected_reset = (expected_reset_zero, expected_reset_one)[
                alternative_index
            ]
            expected_response = _v5_safe_q_product(
                (
                    QMatrix.identity(2),
                    causal_occurrence,
                    expected_reset,
                    delta_zero,
                )
            )
            response_residual = (
                _q_residual(response, expected_response)
                if isinstance(response, QMatrix)
                and isinstance(expected_response, QMatrix)
                else {"shape_match": False, "nonzero_count": None}
            )
            if isinstance(response, QMatrix):
                causal_responses.append((alternative_id, response))
            causal_path_rows.append(
                {
                    "alternative_id": alternative_id,
                    "reset": reset,
                    "input": delta_zero,
                    "T_after_reset": qmultiply(
                        causal_occurrence, qmultiply(reset, delta_zero)
                    ),
                    "delayed_response": response,
                    "independently_recomputed_expected_response": expected_response,
                    "response_residual": response_residual,
                }
            )
            _v5_add_derived_node(
                nodes,
                f"derived:causal:{alternative_id}",
                kind="generated-causal-response",
                operands=(
                    "composition:causal-order",
                    "intervention:causal",
                    "occ:T:causal",
                    "reader:causal",
                ),
                derived=response,
                expected=expected_response,
                residual=response_residual,
                carrier_trace=("G2", alternative_id, "G2", "T", "G2", "reader"),
            )
    causal_changed = bool(
        len(causal_responses) == 2
        and causal_responses[0][1] != causal_responses[1][1]
    )
    causal_valid = bool(
        causal_typed
        and causal_changed
        and all(
            row["response_residual"].get("nonzero_count") == 0
            for row in causal_path_rows
        )
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:causal-order",
        kind="classifier-native-coordinate",
        operands=tuple(
            f"derived:causal:{alternative_id}"
            for alternative_id in (
                causal.alternative_ids
                if isinstance(causal, ExecutableInterventionSet)
                else ("reset-zero", "reset-one")
            )
        ),
        derived=tuple(causal_responses),
        expected={"two_distinct_delayed_responses": True},
        residual={"changed_response": causal_changed, "valid": causal_valid},
        carrier_trace=("intervention before shared T before reader",),
    )
    terminals["coordinate:causal-order"] = "causal_order"
    _v5_record_gate(context, "causal-order", causal_valid)

    contact = intervention_index.get("intervention:contact")
    contact_reader = reader_index.get("reader:contact")
    contact_occurrence = occurrence_matrices.get("occ:T:contact")
    expected_cnot = _cnot_matrix()
    expected_contact_reader = _target_reader_matrix(2, 2)
    contact_responses: list[tuple[str, QMatrix]] = []
    contact_path_rows: list[dict[str, object]] = []
    contact_composable = bool(
        isinstance(contact, ExecutableInterventionSet)
        and isinstance(contact_reader, ExecutableReader)
        and isinstance(contact_occurrence, QMatrix)
        and contact.root == law.root
        and contact.carrier_id == "G2"
        and contact.alternative_ids
        == ("source-reset-zero", "source-reset-one")
        and contact.base_alternative_matrices
        == (expected_reset_zero, expected_reset_one)
        and isinstance(contact.propagation_matrix, QMatrix)
        and contact.propagation_matrix.shape == (4, 4)
        and contact.reader_id == "reader:contact"
        and contact_reader.root == law.root
        and contact_reader.carrier_id == "G2xF"
        and contact_reader.factor_carrier_id == "F"
        and contact_reader.outcomes == ("0", "1")
        and contact_reader.matrix == expected_contact_reader
        and _v5_composition_ready(context, "generated-contact")
    )
    contact_typed = bool(
        contact_composable
        and isinstance(contact, ExecutableInterventionSet)
        and contact.propagation_matrix == expected_cnot
    )
    if contact_composable:
        assert isinstance(contact, ExecutableInterventionSet)
        assert isinstance(contact_reader, ExecutableReader)
        assert isinstance(contact_occurrence, QMatrix)
        assert isinstance(contact.propagation_matrix, QMatrix)
        flag_zero = _v5_basis_state(2, 0)
        for alternative_index, (alternative_id, reset) in enumerate(
            zip(contact.alternative_ids, contact.base_alternative_matrices)
        ):
            reset_state = qmultiply(reset, delta_zero)
            transitioned_source = qmultiply(contact_occurrence, reset_state)
            product_state = _q_kron(transitioned_source, flag_zero)
            propagated = qmultiply(contact.propagation_matrix, product_state)
            response = qmultiply(contact_reader.matrix, propagated)
            expected_reset = (expected_reset_zero, expected_reset_one)[
                alternative_index
            ]
            expected_source = qmultiply(
                contact_occurrence, qmultiply(expected_reset, delta_zero)
            )
            expected_product = _q_kron(expected_source, flag_zero)
            expected_propagated = qmultiply(expected_cnot, expected_product)
            expected_response = qmultiply(
                expected_contact_reader, expected_propagated
            )
            response_residual = _q_residual(response, expected_response)
            contact_responses.append((alternative_id, response))
            contact_path_rows.append(
                {
                    "alternative_id": alternative_id,
                    "source_reset_state": reset_state,
                    "source_after_T": transitioned_source,
                    "source_tensor_fixed_target": product_state,
                    "after_CNOT": propagated,
                    "target_reader_response": response,
                    "independently_recomputed_expected_response": expected_response,
                    "response_residual": response_residual,
                }
            )
            _v5_add_derived_node(
                nodes,
                f"derived:contact:{alternative_id}",
                kind="intervention-through-CNOT-target-reader",
                operands=(
                    "composition:generated-contact",
                    "intervention:contact",
                    "occ:T:contact",
                    "reader:contact",
                ),
                derived=response,
                expected=expected_response,
                residual=response_residual,
                carrier_trace=(
                    "G2",
                    alternative_id,
                    "G2",
                    "T",
                    "G2",
                    "tensor fixed F=0",
                    "G2xF",
                    "CNOT",
                    "G2xF",
                    "R_F",
                ),
            )
    contact_changed = bool(
        len(contact_responses) == 2
        and contact_responses[0][1] != contact_responses[1][1]
    )
    contact_valid = bool(
        contact_typed
        and contact_changed
        and all(
            row["response_residual"].get("nonzero_count") == 0
            for row in contact_path_rows
        )
        and isinstance(contact, ExecutableInterventionSet)
        and contact.propagation_matrix != QMatrix.identity(4)
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:generated-contact",
        kind="classifier-native-coordinate",
        operands=tuple(
            f"derived:contact:{alternative_id}"
            for alternative_id in (
                contact.alternative_ids
                if isinstance(contact, ExecutableInterventionSet)
                else ("source-reset-zero", "source-reset-one")
            )
        ),
        derived=tuple(contact_responses),
        expected={"two_distinct_target_responses": True},
        residual={"changed_response": contact_changed, "valid": contact_valid},
        carrier_trace=("source intervention through CNOT to disjoint target reader",),
    )
    terminals["coordinate:generated-contact"] = "generated_contact"
    _v5_record_gate(context, "generated-contact", contact_valid)
    return {
        "comparison": {
            "primitive": comparison,
            "permutation_residual": permutation_residual,
            "inverse": inverse,
            "conjugated_transition": conjugated_transition,
            "naturality_residual": naturality_residual,
            "calibrated_state": comparison.calibrated_state,
            "transported_state": transported_state,
            "calibrated_effect": comparison.calibrated_effect,
            "transported_effect": transported_effect,
            "valid": comparison_valid,
        },
        "causal_order": {
            "intervention": causal,
            "reader": causal_reader,
            "path_rows": tuple(causal_path_rows),
            "responses": tuple(causal_responses),
            "changed_response": causal_changed,
            "valid": causal_valid,
        },
        "generated_contact": {
            "intervention": contact,
            "reader": contact_reader,
            "path_rows": tuple(contact_path_rows),
            "responses": tuple(contact_responses),
            "changed_target_response": contact_changed,
            "source_local_interventions": True if contact_composable else False,
            "target_reader_factorization_residual": (
                _q_residual(contact_reader.matrix, expected_contact_reader)
                if isinstance(contact_reader, ExecutableReader)
                else {"shape_match": False, "nonzero_count": None}
            ),
            "valid": contact_valid,
        },
    }


def _v5_measure_overlap_compiler_locality_quantum(
    context: MutableMapping[str, object]
) -> dict[str, object]:
    law = context["law"]
    nodes = context["nodes"]
    terminals = context["terminals"]
    carrier_index = context["carrier_index"]
    occurrence_matrices = context["occurrence_matrices"]
    assert isinstance(law, ExecutableLaw)
    assert isinstance(nodes, dict)
    assert isinstance(terminals, dict)
    assert isinstance(carrier_index, dict)
    assert isinstance(occurrence_matrices, dict)

    abc_carrier = carrier_index.get("ABC")
    overlap_occurrence = occurrence_matrices.get("occ:T:overlap")
    abc_transition = (
        _q_kron(
            _q_kron(overlap_occurrence, QMatrix.identity(2)),
            QMatrix.identity(2),
        )
        if isinstance(overlap_occurrence, QMatrix)
        else None
    )
    expected_abc_transition = (
        QMatrix.from_rows(
            (
                (
                    overlap_occurrence.data[output // 4][source // 4]
                    if output % 4 == source % 4
                    else Fraction(0)
                    for source in range(8)
                )
                for output in range(8)
            ),
            ncols=8,
        )
        if isinstance(overlap_occurrence, QMatrix)
        and overlap_occurrence.shape == (2, 2)
        else None
    )
    abc_transition_residual = (
        _q_residual(abc_transition, expected_abc_transition)
        if isinstance(abc_transition, QMatrix)
        and isinstance(expected_abc_transition, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    abc_transition_stochastic = (
        _stochastic_matrix_measurement(abc_transition, expected_shape=(8, 8))
        if isinstance(abc_transition, QMatrix)
        else {"valid": False, "shape_residual": 1}
    )
    abc_transition_permutation = (
        _q_is_permutation(abc_transition)[0]
        if isinstance(abc_transition, QMatrix)
        else False
    )

    owned_distribution_measurement = _v5_distribution_measurement(
        law.owned_global_abc.probabilities, 8
    )
    alternate_distribution_measurement = _v5_distribution_measurement(
        law.alternate_global_abc.probabilities, 8
    )
    owned_input = QMatrix.from_rows(
        ((value,) for value in law.owned_global_abc.probabilities), ncols=1
    )
    alternate_input = QMatrix.from_rows(
        ((value,) for value in law.alternate_global_abc.probabilities), ncols=1
    )
    owned_after = (
        qmultiply(abc_transition, owned_input)
        if isinstance(abc_transition, QMatrix)
        and owned_input.shape == (8, 1)
        else None
    )
    alternate_after = (
        qmultiply(abc_transition, alternate_input)
        if isinstance(abc_transition, QMatrix)
        and alternate_input.shape == (8, 1)
        else None
    )
    expected_owned_after = (
        qmultiply(expected_abc_transition, owned_input)
        if isinstance(expected_abc_transition, QMatrix)
        and owned_input.shape == (8, 1)
        else None
    )
    expected_alternate_after = (
        qmultiply(expected_abc_transition, alternate_input)
        if isinstance(expected_abc_transition, QMatrix)
        and alternate_input.shape == (8, 1)
        else None
    )
    configurations = (
        abc_carrier.states
        if isinstance(abc_carrier, ExecutableCarrier)
        else ()
    )
    owned_shadows = (
        _v5_abc_shadows(
            configurations, tuple(row[0] for row in owned_after.data)
        )
        if isinstance(owned_after, QMatrix)
        else {
            "P_AB": {},
            "P_BC": {},
            "P_B": {},
            "markov_cell_residuals": {},
            "markov_zero": False,
        }
    )
    alternate_shadows = (
        _v5_abc_shadows(
            configurations, tuple(row[0] for row in alternate_after.data)
        )
        if isinstance(alternate_after, QMatrix)
        else {
            "P_AB": {},
            "P_BC": {},
            "P_B": {},
            "markov_cell_residuals": {},
            "markov_zero": False,
        }
    )
    expected_owned_shadows = (
        _v5_abc_shadows(
            configurations,
            tuple(row[0] for row in expected_owned_after.data),
        )
        if isinstance(expected_owned_after, QMatrix)
        else {}
    )
    expected_alternate_shadows = (
        _v5_abc_shadows(
            configurations,
            tuple(row[0] for row in expected_alternate_after.data),
        )
        if isinstance(expected_alternate_after, QMatrix)
        else {}
    )
    zero_survivors = tuple(
        candidate_id
        for candidate_id, shadows in (
            (law.owned_global_abc.identifier, owned_shadows),
            (law.alternate_global_abc.identifier, alternate_shadows),
        )
        if shadows["markov_zero"]
    )
    same_pair_shadows = bool(
        owned_shadows["P_AB"] == alternate_shadows["P_AB"]
        and owned_shadows["P_BC"] == alternate_shadows["P_BC"]
    )
    parity_even = tuple(
        Fraction(1, 4)
        if (int(row[0]) + int(row[1]) + int(row[2])) % 2 == 0
        else Fraction(0)
        for row in configurations
    )
    parity_control_present = bool(
        law.owned_global_abc.probabilities == parity_even
        or law.alternate_global_abc.probabilities == parity_even
    )
    overlap_valid = bool(
        isinstance(abc_carrier, ExecutableCarrier)
        and law.owned_global_abc.root == law.root
        and law.owned_global_abc.identifier == "global:ABC:owned"
        and law.owned_global_abc.carrier_id == "ABC"
        and law.alternate_global_abc.root == law.root
        and law.alternate_global_abc.identifier
        == "global:ABC:parity-control"
        and law.alternate_global_abc.carrier_id == "ABC"
        and _v5_composition_ready(context, "overlap-shadows")
        and abc_transition_stochastic["valid"]
        and abc_transition_permutation
        and abc_transition_residual.get("nonzero_count") == 0
        and owned_distribution_measurement["valid"]
        and alternate_distribution_measurement["valid"]
        and owned_shadows == expected_owned_shadows
        and alternate_shadows == expected_alternate_shadows
        and len(zero_survivors) == 1
        and zero_survivors == (law.owned_global_abc.identifier,)
        and same_pair_shadows
        and parity_control_present
    )
    _v5_add_derived_node(
        nodes,
        "derived:overlap:T_A",
        kind="full-ABC-transition-map",
        operands=("composition:overlap-shadows", "occ:T:overlap"),
        derived=abc_transition,
        expected=expected_abc_transition,
        residual=abc_transition_residual,
        carrier_trace=("ABC", "T_A tensor I_B tensor I_C", "ABC"),
    )
    _v5_add_derived_node(
        nodes,
        "derived:overlap:owned-state",
        kind="bundle-owned-global-state-after-transition",
        operands=("derived:overlap:T_A", "global:ABC:owned"),
        derived=owned_after,
        expected=expected_owned_after,
        residual=(
            _q_residual(owned_after, expected_owned_after)
            if isinstance(owned_after, QMatrix)
            and isinstance(expected_owned_after, QMatrix)
            else {"shape_match": False, "nonzero_count": None}
        ),
        carrier_trace=("ABC", "owned global operand", "ABC"),
    )
    _v5_add_derived_node(
        nodes,
        "derived:overlap:alternate-state",
        kind="printed-alternate-global-control-after-transition",
        operands=("derived:overlap:T_A", "global:ABC:parity-control"),
        derived=alternate_after,
        expected=expected_alternate_after,
        residual=(
            _q_residual(alternate_after, expected_alternate_after)
            if isinstance(alternate_after, QMatrix)
            and isinstance(expected_alternate_after, QMatrix)
            else {"shape_match": False, "nonzero_count": None}
        ),
        carrier_trace=("ABC", "alternate global control", "ABC"),
    )
    _v5_add_derived_node(
        nodes,
        "derived:overlap:owned-shadows",
        kind="computed-AB-BC-restrictions",
        operands=("derived:overlap:owned-state",),
        derived=owned_shadows,
        expected=expected_owned_shadows,
        residual={
            "exact_object_match": owned_shadows == expected_owned_shadows,
            "markov_cell_residuals": owned_shadows["markov_cell_residuals"],
        },
        carrier_trace=("ABC", "restrict AB", "restrict BC"),
    )
    _v5_add_derived_node(
        nodes,
        "derived:overlap:alternate-shadows",
        kind="computed-alternate-AB-BC-restrictions",
        operands=("derived:overlap:alternate-state",),
        derived=alternate_shadows,
        expected=expected_alternate_shadows,
        residual={
            "exact_object_match": alternate_shadows
            == expected_alternate_shadows,
            "markov_cell_residuals": alternate_shadows["markov_cell_residuals"]
        },
        carrier_trace=("ABC", "restrict AB", "restrict BC"),
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:overlap",
        kind="classifier-native-coordinate",
        operands=(
            "derived:overlap:owned-shadows",
            "derived:overlap:alternate-shadows",
        ),
        derived={
            "zero_residual_survivors": zero_survivors,
            "selected": zero_survivors[0] if len(zero_survivors) == 1 else None,
        },
        expected={"selected": law.owned_global_abc.identifier},
        residual={"valid": overlap_valid},
        carrier_trace=("one owned ABC object -> computed AB/BC shadows",),
    )
    terminals["coordinate:overlap"] = "boundary_gluing_package"
    _v5_record_gate(context, "overlap", overlap_valid)

    compiler_measurement = measure_prefix_compiler(
        law.compiler, quotient_mode="literal-prefix-algebra"
    )
    compiler_occurrence = occurrence_matrices.get("occ:T:compiler")
    atoms = _binary_atoms(3)
    fresh_region = PrefixRegion.cylinder("000")
    fresh_effect = _prefix_effect(law.compiler, fresh_region, atoms)
    compiler_tensor_transition = (
        _q_kron(compiler_occurrence, QMatrix.identity(len(atoms)))
        if isinstance(compiler_occurrence, QMatrix)
        else None
    )
    expected_compiler_tensor_transition = (
        QMatrix.from_rows(
            (
                (
                    compiler_occurrence.data[left_output][left_input]
                    * (
                        Fraction(1)
                        if prefix_output == prefix_input
                        else Fraction(0)
                    )
                    for left_input in range(2)
                    for prefix_input in range(len(atoms))
                )
                for left_output in range(2)
                for prefix_output in range(len(atoms))
            ),
            ncols=2 * len(atoms),
        )
        if isinstance(compiler_occurrence, QMatrix)
        and compiler_occurrence.shape == (2, 2)
        else None
    )
    source_zero_effect = QMatrix.from_rows(((1, 0),), ncols=2)
    joint_fresh_effect = (
        _q_kron(source_zero_effect, fresh_effect)
        if isinstance(fresh_effect, QMatrix)
        else None
    )
    transported_fresh_effect = (
        qmultiply(joint_fresh_effect, compiler_tensor_transition)
        if isinstance(joint_fresh_effect, QMatrix)
        and isinstance(compiler_tensor_transition, QMatrix)
        else None
    )
    expected_transported_fresh_effect = (
        qmultiply(joint_fresh_effect, expected_compiler_tensor_transition)
        if isinstance(joint_fresh_effect, QMatrix)
        and isinstance(expected_compiler_tensor_transition, QMatrix)
        else None
    )
    compiler_transport_residual = (
        _q_residual(
            transported_fresh_effect, expected_transported_fresh_effect
        )
        if isinstance(transported_fresh_effect, QMatrix)
        and isinstance(expected_transported_fresh_effect, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    compiler_valid = bool(
        law.compiler.root == law.root
        and law.compiler.identifier == "compiler:uniform-prefix"
        and law.compiler.transition_reference_id is None
        and compiler_measurement.normalization_valid
        and compiler_measurement.raw_atomless_valid
        and compiler_measurement.future_complete
        and compiler_measurement.congruence_valid
        and compiler_measurement.quotient_atomless_valid
        and isinstance(transported_fresh_effect, QMatrix)
        and _q_nonzero_count(transported_fresh_effect) > 0
        and compiler_transport_residual.get("nonzero_count") == 0
        and _v5_composition_ready(context, "compiler-tensor")
    )
    _v5_add_derived_node(
        nodes,
        "derived:compiler-tensor-effect",
        kind="fresh-prefix-effect-after-shared-transition",
        operands=(
            "composition:compiler-tensor",
            "compiler:uniform-prefix",
            "occ:T:compiler",
        ),
        derived=transported_fresh_effect,
        expected=expected_transported_fresh_effect,
        residual=compiler_transport_residual,
        carrier_trace=("G2xPrefix3", "T tensor I_Prefix3", "effect"),
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:compiler",
        kind="classifier-native-coordinate",
        operands=("derived:compiler-tensor-effect",),
        derived={
            "measurement": compiler_measurement,
            "transported_fresh_effect": transported_fresh_effect,
        },
        expected={
            "normalization": True,
            "raw_atomless": True,
            "future_complete": True,
            "congruence": True,
            "quotient_atomless": True,
        },
        residual={"valid": compiler_valid},
        carrier_trace=("uniform target-independent prefix compiler",),
    )
    compiler_coordinate_values = {
        "raw_boolean_normalization": compiler_measurement.normalization_valid,
        "raw_atomlessness": compiler_measurement.raw_atomless_valid,
        "future_profile_complete": compiler_measurement.future_complete,
        "regional_congruence": compiler_measurement.congruence_valid,
        "post_quotient_atomlessness": compiler_measurement.quotient_atomless_valid,
    }
    for coordinate_name, coordinate_value in compiler_coordinate_values.items():
        node_id = f"coordinate:compiler:{coordinate_name}"
        _v5_add_derived_node(
            nodes,
            node_id,
            kind="classifier-native-coordinate",
            operands=("coordinate:compiler",),
            derived={"present": coordinate_value},
            expected={"present": True},
            residual={"boolean_residual": 0 if coordinate_value else 1},
            carrier_trace=("uniform target-independent prefix compiler",),
        )
        terminals[node_id] = coordinate_name
    _v5_record_gate(context, "prefix-compiler", compiler_valid)

    locality_measurement_view = replace(
        law.locality,
        regions=tuple(
            replace(
                row,
                identifier=row.identifier.removeprefix("locality-region:"),
            )
            for row in law.locality.regions
        ),
    )
    locality_measurement = measure_locality_primitive_law(
        locality_measurement_view
    )
    locality_occurrence = occurrence_matrices.get("occ:T:locality")
    locality_transition = (
        _q_kron(locality_occurrence, QMatrix.identity(2))
        if isinstance(locality_occurrence, QMatrix)
        else None
    )
    expected_locality_transition = (
        QMatrix.from_rows(
            (
                (
                    locality_occurrence.data[left_output][left_input]
                    * (
                        Fraction(1)
                        if flag_output == flag_input
                        else Fraction(0)
                    )
                    for left_input in range(2)
                    for flag_input in range(2)
                )
                for left_output in range(2)
                for flag_output in range(2)
            ),
            ncols=4,
        )
        if isinstance(locality_occurrence, QMatrix)
        and locality_occurrence.shape == (2, 2)
        else None
    )
    locality_regions = {row.identifier: row for row in law.locality.regions}
    s_region = locality_regions.get("locality-region:S")
    s_effect = (
        qtranspose(s_region.effect_generators[0])
        if isinstance(s_region, LocalityRegionPrimitive)
        and s_region.effect_generators
        else None
    )
    transported_locality_effect = (
        qmultiply(s_effect, locality_transition)
        if isinstance(s_effect, QMatrix)
        and isinstance(locality_transition, QMatrix)
        else None
    )
    expected_transported_locality_effect = (
        qmultiply(s_effect, expected_locality_transition)
        if isinstance(s_effect, QMatrix)
        and isinstance(expected_locality_transition, QMatrix)
        else None
    )
    locality_transport_residual = (
        _q_residual(
            transported_locality_effect,
            expected_transported_locality_effect,
        )
        if isinstance(transported_locality_effect, QMatrix)
        and isinstance(expected_transported_locality_effect, QMatrix)
        else {"shape_match": False, "nonzero_count": None}
    )
    locality_valid = bool(
        law.locality.root == law.root
        and law.locality.identifier == "locality:two-bit"
        and law.locality.transition_reference_id is None
        and locality_measurement.valid
        and isinstance(transported_locality_effect, QMatrix)
        and _q_nonzero_count(transported_locality_effect) > 0
        and locality_transport_residual.get("nonzero_count") == 0
        and _v5_composition_ready(context, "locality-transport")
    )
    locality_operands = (
        "composition:locality-transport",
        law.locality.identifier,
        *(row.identifier for row in law.locality.regions),
        *(row.identifier for row in law.locality.replacements),
        "occ:T:locality",
    )
    _v5_add_derived_node(
        nodes,
        "derived:locality-transport",
        kind="generated-support-effect-after-shared-transition",
        operands=locality_operands,
        derived=transported_locality_effect,
        expected=expected_transported_locality_effect,
        residual=locality_transport_residual,
        carrier_trace=("G2xF", "generated Kin(S)=Dyn(S)", "T tensor I_F"),
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:locality",
        kind="classifier-native-coordinate",
        operands=("derived:locality-transport",),
        derived={
            "measurement": locality_measurement,
            "transported_effect": transported_locality_effect,
        },
        expected={"generated_locality_valid": True},
        residual={"valid": locality_valid},
        carrier_trace=("generated finite regional-support control",),
    )
    terminals["coordinate:locality"] = "dynamic_locality"
    _v5_record_gate(context, "locality", locality_valid)

    quantum_occurrence = occurrence_matrices.get("occ:T:quantum")
    quantum_measurement = (
        _v5_phase_quantum_measurement(law.quantum, quantum_occurrence)
        if isinstance(quantum_occurrence, QMatrix)
        else {
            "valid": False,
            "issues": ("missing-quantum-transition-occurrence",),
            "scorer_source_sha256": sha256_path(Path(__file__)),
        }
    )
    quantum_valid = bool(
        quantum_measurement["valid"]
        and _v5_composition_ready(context, "quantum-history")
    )
    quantum_operands = (
        "composition:quantum-history",
        law.quantum.identifier,
        *(row.identifier for row in law.quantum.flag_continuations),
        "occ:T:quantum",
    )
    _v5_add_derived_node(
        nodes,
        "derived:quantum-history",
        kind="phase-bearing-history-control-with-transition-endpoint",
        operands=quantum_operands,
        derived=quantum_measurement,
        expected={
            "D": GMatrix.from_rows(
                (
                    (
                        GaussianRational(Fraction(1, 4)),
                        GaussianRational(0, Fraction(-1, 4)),
                    ),
                    (
                        GaussianRational(0, Fraction(1, 4)),
                        GaussianRational(Fraction(1, 4)),
                    ),
                )
            ),
            "coherent_p_plus": GONE,
            "incoherent_history_sum": GaussianRational(Fraction(1, 2)),
            "port_weighted_cross_term": GaussianRational(Fraction(1, 2)),
        },
        residual={
            "D": quantum_measurement.get("D_residual"),
            "operator_identity": quantum_measurement.get(
                "gram_operator_identity_residual"
            ),
            "valid": quantum_valid,
        },
        carrier_trace=("G2", "T", "phase histories H0,H1", "division flags"),
    )
    _v5_add_derived_node(
        nodes,
        "coordinate:quantum",
        kind="classifier-native-coordinate",
        operands=("derived:quantum-history",),
        derived=quantum_measurement,
        expected={"phase-bearing-exact-control": True},
        residual={"valid": quantum_valid},
        carrier_trace=("Hilbert/history representational control",),
    )
    terminals["coordinate:quantum"] = "horizontal_quantum"
    _v5_record_gate(context, "quantum", quantum_valid)
    return {
        "overlap": {
            "role": "SIMULTANEOUS-REGIONAL-GLUING-DIAGNOSTIC-NOT-TRANSITION-LAW",
            "T_A_tensor_I_B_tensor_I_C": abc_transition,
            "owned_global_input": law.owned_global_abc,
            "owned_global_after_T": owned_after,
            "owned_computed_shadows": owned_shadows,
            "alternate_global_input": law.alternate_global_abc,
            "alternate_global_after_T": alternate_after,
            "alternate_computed_shadows": alternate_shadows,
            "zero_markov_residual_survivors": zero_survivors,
            "selected_candidate_id": (
                zero_survivors[0] if len(zero_survivors) == 1 else None
            ),
            "cached_restrictions_ignored": law.cached_restriction_rows,
            "parity_global_same_shadow_control": {
                "present": parity_control_present,
                "same_AB_BC_shadows": same_pair_shadows,
                "global_objects_distinct": owned_after != alternate_after,
                "proves_shadows_do_not_select_global": True,
                "scientific_primary_affected": False,
            },
            "valid": overlap_valid,
        },
        "compiler": {
            "measurement": compiler_measurement,
            "fresh_region": fresh_region,
            "fresh_effect": fresh_effect,
            "T_tensor_I_prefix": compiler_tensor_transition,
            "source_zero_tensor_fresh_effect": joint_fresh_effect,
            "transported_fresh_effect": transported_fresh_effect,
            "valid": compiler_valid,
        },
        "locality": {
            "measurement": locality_measurement,
            "source_region_effect": s_effect,
            "T_tensor_I_F": locality_transition,
            "transported_effect": transported_locality_effect,
            "valid": locality_valid,
        },
        "quantum": quantum_measurement,
    }


def evaluate_executable_law(
    law: object, observed_endpoint: QMatrix
) -> ExecutableLawMeasurement:
    if not isinstance(law, ExecutableLaw):
        raise ScoreRefusal(
            "v5 evaluation requires one immutable ExecutableLaw bundle"
        )
    observed_measurement = _stochastic_matrix_measurement(
        observed_endpoint, expected_shape=(2, 1)
    )
    context = _v5_prepare_executable_law(law)
    if not observed_measurement["valid"]:
        context["issues"].append("calibration:invalid-observed-endpoint")
    process_tensor_instrument = _v5_measure_process_tensor_instrument(context)
    ontology = _v5_measure_ontology_chain(
        context,
        process_tensor_instrument["instrument"],
        observed_endpoint,
    )
    comparison_influence = _v5_measure_comparison_influence(context)
    remaining = _v5_measure_overlap_compiler_locality_quantum(context)

    nodes = context["nodes"]
    terminals = context["terminals"]
    assert isinstance(nodes, Mapping)
    assert isinstance(terminals, Mapping)
    dag = _v5_finalize_dataflow_dag(
        nodes,
        terminals,
        tuple(
            row.to_data() for row in law.auxiliary_dependency_claims
        ),
    )
    issues = context["issues"]
    assert isinstance(issues, list)
    issues.extend(str(row) for row in dag["issues"])

    coordinates = {
        "raw_boolean_normalization": bool(
            remaining["compiler"]["measurement"].normalization_valid
        ),
        "raw_atomlessness": bool(
            remaining["compiler"]["measurement"].raw_atomless_valid
        ),
        "boundary_gluing_package": bool(
            remaining["overlap"]["valid"] and dag["valid"]
        ),
        "horizontal_process": bool(
            process_tensor_instrument["process"]["valid"]
        ),
        "tensor_gluing_interfaces": bool(
            process_tensor_instrument["tensor"]["valid"]
        ),
        "conditioning_instrument": bool(
            process_tensor_instrument["instrument"]["valid"]
        ),
        "horizontal_quantum": bool(remaining["quantum"]["valid"]),
        "future_profile_complete": bool(
            remaining["compiler"]["measurement"].future_complete
        ),
        "regional_congruence": bool(
            remaining["compiler"]["measurement"].congruence_valid
        ),
        "post_quotient_atomlessness": bool(
            remaining["compiler"]["measurement"].quotient_atomless_valid
        ),
        "comparison_selected": bool(
            comparison_influence["comparison"]["valid"]
        ),
        "dynamic_locality": bool(remaining["locality"]["valid"]),
        "causal_order": bool(comparison_influence["causal_order"]["valid"]),
        "generated_contact": bool(
            comparison_influence["generated_contact"]["valid"]
        ),
        "ontology_region_rewriting": bool(ontology["valid"]),
        "backward_slice_connected": bool(dag["valid"]),
    }
    issue_rows = tuple(sorted(set(issues)))
    required_coordinate_names = tuple(coordinates)
    valid = bool(
        observed_measurement["valid"]
        and all(coordinates[name] for name in required_coordinate_names)
        and not issue_rows
    )
    measured_role = str(ontology["role"])
    ontology_role = (
        measured_role
        if not issue_rows or measured_role != "REGION-REWRITING"
        else "RECORD-WRITING-ON-FIXED-ALGEBRA"
    )
    native_measurements = {
        "structural_typing": context["structural_measurement"],
        "transition": context["transition_measurement"],
        **process_tensor_instrument,
        "ontology_chain": ontology,
        **comparison_influence,
        **remaining,
        "observed_endpoint": {
            "state": observed_endpoint,
            "measurement": observed_measurement,
        },
        "scope": {
            "canonical_sentence": V5_SCOPE_SENTENCE,
            "AB_BC_role": (
                "SIMULTANEOUS-REGIONAL-GLUING-DIAGNOSTIC-NOT-TRANSITION-LAW"
            ),
            "candidate_fundamental_law_status": (
                "UNCONSTRUCTED-INDIVISIBLE-STOCHASTIC-RELATIONAL-TRANSITION-LAW"
            ),
        },
    }
    return ExecutableLawMeasurement(
        primitive_payload_sha256=canonical_sha256(law.to_data()),
        candidate_id=law.identifier,
        valid=valid,
        issues=issue_rows,
        coordinates=coordinates,
        native_measurements=native_measurements,
        dataflow_dag=dag,
        composed_map=(ontology["P_i"] if isinstance(ontology["P_i"], QMatrix) else None),
        selection_response=(
            ontology["r_i"] if isinstance(ontology["r_i"], QMatrix) else None
        ),
        selection_residual=ontology["selection_residual"],
        ontology_role=ontology_role,
    )


def _v5_family_primary(
    coordinates: Mapping[str, bool], law_selected: bool
) -> tuple[str, tuple[str, ...]]:
    if not coordinates["raw_boolean_normalization"]:
        return "APR-INCONSISTENT", (
            "full-cone normalization is absent or inconsistent",
        )
    if not coordinates["raw_atomlessness"]:
        return "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA", (
            "no nonzero raw regional split was constructed",
        )
    if not coordinates["boundary_gluing_package"]:
        return "APR-BLOCKED-AT-BOUNDARY-GLUING", (
            "missing computed simultaneous-gluing diagnostic selector or connected primitive graph",
        )
    if not coordinates["horizontal_process"]:
        return "APR-BLOCKED-AT-TWO-ARROW-TYPING", (
            "no validated typed horizontal reachability-control process",
        )
    if not coordinates["future_profile_complete"]:
        return "APR-BLOCKED-AT-FUTURE-PROFILE-COMPLETENESS", (
            "no complete target-independent probe compiler",
        )
    if not coordinates["regional_congruence"]:
        return "APR-BLOCKED-AT-REGIONAL-CONGRUENCE", (
            "profile equivalence is not a generated regional congruence",
        )
    if not coordinates["post_quotient_atomlessness"]:
        return "APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA", (
            "the claimed quotient has no nonzero proper split certificate",
        )
    if not coordinates["comparison_selected"]:
        return "APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED", (
            "comparison system remains law data",
        )
    if not coordinates["dynamic_locality"]:
        return (
            "APR-COMPARISON-QUOTIENT-CONSTRUCTED-BUT-DYNAMICAL-LOCALITY-FAILS",
            ("dynamic regional-support requirements fail",),
        )
    if not coordinates["causal_order"]:
        return (
            "APR-DYNAMIC-REGIONAL-REFERENT-CONSTRUCTED-BUT-CAUSAL-ORDER-PRICED",
            ("causal schedule and delayed response are not generated",),
        )
    if not coordinates["generated_contact"]:
        return (
            "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
            ("missing generated_contact",),
        )
    if not law_selected:
        return (
            "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
            ("one joint law remains unselected",),
        )
    return "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED", ()


def classify_executable_family(law_family: object) -> ExecutableFamilyClassification:
    if not isinstance(law_family, ExecutableLawFamily):
        raise ScoreRefusal(
            "v5 classifier requires one immutable ExecutableLawFamily"
        )
    family_hash = canonical_sha256(law_family.to_data())
    issues: list[str] = []
    observed_measurement = _stochastic_matrix_measurement(
        law_family.observed_endpoint, expected_shape=(2, 1)
    )
    observed_valid = bool(
        observed_measurement["valid"]
        and law_family.observed_endpoint == _v5_basis_state(2, 1)
    )
    if not observed_valid:
        issues.append("family:fixed-delta-one-observation")
    family_header_valid = bool(
        law_family.root == V5_EXECUTABLE_ROOT
        and law_family.identifier == "finite-family:L_I,L_X"
        and law_family.schema_id == V5_EXECUTABLE_SCHEMA
    )
    if not family_header_valid:
        issues.append("family:header")
    candidate_ids = tuple(candidate.identifier for candidate in law_family.candidates)
    candidate_registry_valid = bool(
        len(law_family.candidates) == 2
        and candidate_ids == ("L_I", "L_X")
        and len(set(candidate_ids)) == 2
    )
    if not candidate_registry_valid:
        issues.append("family:exact-candidate-registry")
    measurements = tuple(
        evaluate_executable_law(candidate, law_family.observed_endpoint)
        for candidate in law_family.candidates
    )
    measurement_by_id = {row.candidate_id: row for row in measurements}

    projections = tuple(
        _v5_schema_projection(candidate) for candidate in law_family.candidates
    )
    same_schema_projection = bool(
        len(projections) == 2
        and len({row["sha256"] for row in projections}) == 1
    )
    if not same_schema_projection:
        issues.append("family:candidates-not-one-schema")
    transition_rows: dict[str, object] = {}
    exact_transition_assignment = candidate_registry_valid
    expected_matrices = {
        "L_I": QMatrix.identity(2),
        "L_X": QMatrix.from_rows(((0, 1), (1, 0))),
    }
    for candidate in law_family.candidates:
        transition = (
            candidate.transitions[0]
            if len(candidate.transitions) == 1
            and isinstance(candidate.transitions[0], ExecutableTransition)
            else None
        )
        expected = expected_matrices.get(candidate.identifier)
        valid = bool(
            isinstance(transition, ExecutableTransition)
            and transition.identifier == "T"
            and transition.matrix == expected
        )
        exact_transition_assignment = exact_transition_assignment and valid
        transition_rows[candidate.identifier] = {
            "transition": transition,
            "expected_matrix": expected,
            "residual": (
                _q_residual(transition.matrix, expected)
                if isinstance(transition, ExecutableTransition)
                and isinstance(expected, QMatrix)
                else {"shape_match": False, "nonzero_count": None}
            ),
            "valid": valid,
        }
    if not exact_transition_assignment:
        issues.append("family:exact-I-X-transition-assignment")

    left_measurement = measurement_by_id.get("L_I")
    right_measurement = measurement_by_id.get("L_X")
    p_moved = bool(
        isinstance(left_measurement, ExecutableLawMeasurement)
        and isinstance(right_measurement, ExecutableLawMeasurement)
        and isinstance(left_measurement.composed_map, QMatrix)
        and isinstance(right_measurement.composed_map, QMatrix)
        and left_measurement.composed_map != right_measurement.composed_map
    )
    r_moved = bool(
        isinstance(left_measurement, ExecutableLawMeasurement)
        and isinstance(right_measurement, ExecutableLawMeasurement)
        and isinstance(left_measurement.selection_response, QMatrix)
        and isinstance(right_measurement.selection_response, QMatrix)
        and left_measurement.selection_response
        != right_measurement.selection_response
    )
    residuals_moved = bool(
        isinstance(left_measurement, ExecutableLawMeasurement)
        and isinstance(right_measurement, ExecutableLawMeasurement)
        and canonical_sha256(left_measurement.selection_residual)
        != canonical_sha256(right_measurement.selection_residual)
    )
    movement_valid = p_moved and r_moved and residuals_moved
    if not movement_valid:
        issues.append("family:P-r-selection-residual-must-move")

    zero_survivors = tuple(
        measurement.candidate_id
        for measurement in measurements
        if measurement.valid
        and measurement.selection_residual.get("nonzero_count") == 0
    )
    candidates_complete = bool(
        len(measurements) == 2 and all(row.valid for row in measurements)
    )
    unique_selection = bool(
        candidates_complete
        and zero_survivors == ("L_X",)
    )
    if not candidates_complete:
        issues.extend(
            f"family:candidate-invalid:{row.candidate_id}"
            for row in measurements
            if not row.valid
        )
    if not unique_selection:
        issues.append("family:unique-zero-residual-L_X")

    aggregate_coordinates = {
        name: all(bool(row.coordinates.get(name)) for row in measurements)
        for name in (
            "raw_boolean_normalization",
            "raw_atomlessness",
            "boundary_gluing_package",
            "horizontal_process",
            "future_profile_complete",
            "regional_congruence",
            "post_quotient_atomlessness",
            "comparison_selected",
            "dynamic_locality",
            "causal_order",
            "generated_contact",
        )
    }
    law_selected = bool(
        family_header_valid
        and observed_valid
        and candidate_registry_valid
        and same_schema_projection
        and exact_transition_assignment
        and movement_valid
        and unique_selection
        and not issues
    )
    primary, walls = _v5_family_primary(aggregate_coordinates, law_selected)
    family_residuals = {
        "family_header_valid": family_header_valid,
        "observed_endpoint": law_family.observed_endpoint,
        "observed_endpoint_measurement": observed_measurement,
        "observed_endpoint_is_fixed_delta_one": observed_valid,
        "candidate_ids": candidate_ids,
        "candidate_registry_valid": candidate_registry_valid,
        "schema_projections": projections,
        "same_schema_projection": same_schema_projection,
        "transition_rows": transition_rows,
        "exact_transition_assignment": exact_transition_assignment,
        "movement_assay": {
            "P_I": (
                left_measurement.composed_map
                if isinstance(left_measurement, ExecutableLawMeasurement)
                else None
            ),
            "P_X": (
                right_measurement.composed_map
                if isinstance(right_measurement, ExecutableLawMeasurement)
                else None
            ),
            "P_moved": p_moved,
            "r_I": (
                left_measurement.selection_response
                if isinstance(left_measurement, ExecutableLawMeasurement)
                else None
            ),
            "r_X": (
                right_measurement.selection_response
                if isinstance(right_measurement, ExecutableLawMeasurement)
                else None
            ),
            "r_moved": r_moved,
            "selection_residual_I": (
                left_measurement.selection_residual
                if isinstance(left_measurement, ExecutableLawMeasurement)
                else None
            ),
            "selection_residual_X": (
                right_measurement.selection_residual
                if isinstance(right_measurement, ExecutableLawMeasurement)
                else None
            ),
            "selection_residual_moved": residuals_moved,
            "valid": movement_valid,
        },
        "aggregate_coordinates": aggregate_coordinates,
        "candidate_measurements_complete": candidates_complete,
        "zero_residual_survivors": zero_survivors,
        "unique_zero_residual_L_X": unique_selection,
        "cached_payloads_consulted": False,
        "plain_roots_or_hashes_used_as_edges": False,
        "law_selected": law_selected,
        "canonical_scope_sentence": V5_SCOPE_SENTENCE,
        "scientific_fixture_evaluated": False,
    }
    return ExecutableFamilyClassification(
        primitive_payload_sha256=family_hash,
        primary=primary,
        walls=walls,
        selected_candidate_id="L_X" if law_selected else None,
        candidate_measurements=measurements,
        family_residuals=family_residuals,
        issues=tuple(sorted(set(issues))),
    )


def classify_primitive_law(law: object) -> ExecutableFamilyClassification:
    """V5 public classifier: detached v4 modules and nominal results refuse."""

    if not isinstance(law, ExecutableLawFamily):
        raise ScoreRefusal(
            "v5 classifier requires fresh evaluation of one ExecutableLawFamily"
        )
    return classify_executable_family(law)


def _v5_source_mutation_record(
    *,
    marker: str,
    old_text: str,
    new_text: str,
    semantic_measurement: Mapping[str, object],
) -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    marked_lines = tuple(
        line
        for line in source.splitlines(True)
        if marker in line and old_text in line
    )
    _require(len(marked_lines) == 1, f"source marker cardinality: {marker}")
    original_line = marked_lines[0]
    _require(
        original_line.count(old_text) == 1,
        f"source target cardinality on marked line: {marker}",
    )
    changed_line = original_line.replace(old_text, new_text, 1)
    _require(
        source.count(original_line) == 1,
        f"marked source line is not unique: {marker}",
    )
    changed_source = source.replace(original_line, changed_line, 1)
    return {
        "marker": marker,
        "old_text": old_text,
        "new_text": new_text,
        "original_source_line": original_line.rstrip("\n"),
        "changed_source_line": changed_line.rstrip("\n"),
        "original_source_sha256": sha256_bytes(source.encode("utf-8")),
        "changed_source_sha256": sha256_bytes(changed_source.encode("utf-8")),
        "semantic_measurement": semantic_measurement,
        "semantic_measurement_sha256": canonical_sha256(semantic_measurement),
    }


def _v5_attack_witness(
    family: ExecutableLawFamily,
    classification: ExecutableFamilyClassification,
) -> dict[str, object]:
    return {
        "attack_primitive_family": family,
        "attack_primitive_sha256": canonical_sha256(family.to_data()),
        "fresh_classification": classification,
        "fresh_classification_sha256": canonical_sha256(
            classification.to_data()
        ),
        "drop": {
            "primary": classification.primary,
            "walls": classification.walls,
            "selected_candidate_id": classification.selected_candidate_id,
            "issues": classification.issues,
        },
    }


def _run_v5_fixture_denied_selftests() -> dict[str, object]:
    checks: list[str] = []
    witnesses: dict[str, object] = {}
    inherited = run_v4_selftests()
    _require(
        inherited["status"] == "PASS"
        and inherited["check_count"] == 27
        and len(set(inherited["checks"])) == 27,
        "inherited v4 exact gates",
    )
    checks.extend(inherited["checks"])
    witnesses["inherited_v4"] = {
        "schema": inherited["schema"],
        "check_count": inherited["check_count"],
        "checks": inherited["checks"],
        "semantic_witness_sha256": inherited["semantic_witness_sha256"],
        "status": inherited["status"],
    }

    family = build_executable_family()
    classification = classify_primitive_law(family)
    _require(
        classification.primary
        == "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED"
        and classification.selected_candidate_id == "L_X"
        and not classification.issues
        and all(row.valid for row in classification.candidate_measurements),
        f"v5 executable positive failed: {classification.primary} "
        f"{classification.issues} "
        f"{[(row.candidate_id, row.issues, row.coordinates) for row in classification.candidate_measurements]}",
    )
    measurements = {
        row.candidate_id: row for row in classification.candidate_measurements
    }
    left = measurements["L_I"]
    right = measurements["L_X"]
    witnesses["positive_executable_family"] = {
        "primitive": family,
        "primitive_sha256": canonical_sha256(family.to_data()),
        "classification": classification,
        "classification_sha256": canonical_sha256(classification.to_data()),
    }
    checks.append("v5-one-executable-law-positive")

    expected_occurrence_ids = {
        row.identifier for row in _v5_occurrence_rows(V5_EXECUTABLE_ROOT)
    }
    for candidate, measurement in zip(family.candidates, classification.candidate_measurements):
        dag = measurement.dataflow_dag
        _require(
            len(candidate.transitions) == 1
            and candidate.transitions[0].identifier == "T"
            and {row.identifier for row in candidate.occurrences}
            == expected_occurrence_ids
            and all(row.primitive_id == "T" for row in candidate.occurrences)
            and len({row.identifier for row in candidate.occurrences})
            == len(candidate.occurrences)
            and dag["valid"]
            and dag["connected"]
            and dag["unused_nodes_not_admitted"] == ()
            and not dag["carrier_or_boundary_equality_edges"]
            and not dag["root_identifier_or_hash_edges"]
            and not dag["cached_payload_edges"]
            and all(dag["edge_native_coordinate_reachability"].values())
            and all(
                row["derived_object_after_deletion"] is None
                and row["result"] == "ILL-TYPED-MISSING-ACTUAL-OPERAND"
                for row in dag["edge_deletion_assays"].values()
            ),
            f"actual backward slice failed for {candidate.identifier}",
        )
    witnesses["shared_T_and_backward_slices"] = {
        candidate.identifier: {
            "transition": candidate.transitions[0],
            "typed_occurrences": candidate.occurrences,
            "dataflow_dag": measurement.dataflow_dag,
            "dataflow_dag_sha256": canonical_sha256(measurement.dataflow_dag),
        }
        for candidate, measurement in zip(
            family.candidates, classification.candidate_measurements
        )
    }
    checks.append("v5-one-shared-T-and-actual-backward-slices")

    movement = classification.family_residuals["movement_assay"]
    _require(
        movement["valid"]
        and movement["P_moved"]
        and movement["r_moved"]
        and movement["selection_residual_moved"]
        and left.composed_map is not None
        and right.composed_map is not None
        and left.composed_map.shape == (6, 2)
        and right.composed_map.shape == (6, 2)
        and left.selection_response == _v5_basis_state(2, 0)
        and right.selection_response == _v5_basis_state(2, 1)
        and left.selection_residual["nonzero_count"] == 2
        and right.selection_residual["nonzero_count"] == 0,
        "P_i/r_i/selection movement",
    )
    witnesses["P_r_selection_movement"] = movement
    checks.append("v5-P-r-and-selection-residual-move")

    left_native = left.native_measurements
    right_native = right.native_measurements
    recomputation_rows = {
        "shared_transition": (
            left_native["transition"]["valid"],
            right_native["transition"]["valid"],
            family.candidates[0].transitions[0].matrix,
            family.candidates[1].transitions[0].matrix,
        ),
        "process_cut_invariance_derived_from_changed_occurrences": {
            "left_cut": left_native["process"]["cut_a"],
            "right_cut": right_native["process"]["cut_a"],
            "invariant": left_native["process"]["cut_a"]
            == right_native["process"]["cut_a"],
            "left_occurrence_matrix": family.candidates[0].transitions[0].matrix,
            "right_occurrence_matrix": family.candidates[1].transitions[0].matrix,
        },
        "conditioned_after_T_moved": left_native["instrument"][
            "conditioned_after_T"
        ]
        != right_native["instrument"]["conditioned_after_T"],
        "tensor_map_moved": left_native["tensor"]["T_tensor_I_F"]
        != right_native["tensor"]["T_tensor_I_F"],
        "comparison_map_moved": left_native["comparison"][
            "conjugated_transition"
        ]
        != right_native["comparison"]["conjugated_transition"],
        "causal_responses_moved": left_native["causal_order"]["responses"]
        != right_native["causal_order"]["responses"],
        "contact_responses_moved": left_native["generated_contact"]["responses"]
        != right_native["generated_contact"]["responses"],
        "ABC_transition_map_moved": left_native["overlap"][
            "T_A_tensor_I_B_tensor_I_C"
        ]
        != right_native["overlap"]["T_A_tensor_I_B_tensor_I_C"],
        "quantum_endpoint_moved": left_native["quantum"][
            "transition_history_endpoint"
        ]
        != right_native["quantum"]["transition_history_endpoint"],
        "compiler_effect_moved": left_native["compiler"][
            "transported_fresh_effect"
        ]
        != right_native["compiler"]["transported_fresh_effect"],
        "locality_effect_moved": left_native["locality"]["transported_effect"]
        != right_native["locality"]["transported_effect"],
        "ontology_P_moved": left.composed_map != right.composed_map,
        "ontology_r_moved": left.selection_response != right.selection_response,
    }
    _require(
        recomputation_rows["process_cut_invariance_derived_from_changed_occurrences"][
            "invariant"
        ]
        and all(
            value
            for key, value in recomputation_rows.items()
            if key
            not in {
                "shared_transition",
                "process_cut_invariance_derived_from_changed_occurrences",
            }
        ),
        "complete candidate bundle was not recomputed from changed T",
    )
    witnesses["complete_candidate_recomputation"] = recomputation_rows
    checks.append("v5-complete-candidate-bundle-recomputed-from-shared-T")

    for measurement in classification.candidate_measurements:
        native = measurement.native_measurements
        _require(
            native["process"]["valid"]
            and native["process"]["cut_a_residual"]["nonzero_count"] == 0
            and native["process"]["cut_b_residual"]["nonzero_count"] == 0
            and native["tensor"]["valid"]
            and native["tensor"]["associator_naturality_residual"]["nonzero_count"]
            == 0
            and native["tensor"]["symmetry_naturality_residual"]["nonzero_count"]
            == 0
            and native["tensor"]["interchange_residual"]["nonzero_count"] == 0
            and native["instrument"]["valid"]
            and native["instrument"]["semantic_projective_branches"],
            f"process/tensor/instrument gate {measurement.candidate_id}",
        )
    witnesses["process_tensor_instrument"] = {
        row.candidate_id: {
            "process": row.native_measurements["process"],
            "tensor": row.native_measurements["tensor"],
            "instrument": row.native_measurements["instrument"],
        }
        for row in classification.candidate_measurements
    }
    checks.append("v5-process-cuts-tensor-laws-and-branch-semantics")

    for measurement in classification.candidate_measurements:
        ontology = measurement.native_measurements["ontology_chain"]
        rewrite = ontology["regional_rewrite"]
        continuation = ontology["delayed_reader_and_continuations"]
        _require(
            ontology["valid"]
            and ontology["role"] == "REGION-REWRITING"
            and rewrite["literal_writer-target-rewrite-source"]
            and rewrite["Theta_tensor_I_F_residual"]["nonzero_count"] == 0
            and rewrite["iota_tensor_I_F_residual"]["nonzero_count"] == 0
            and rewrite["created_response"] == QMatrix.from_rows(((1,),))
            and rewrite["passive_response"] == QMatrix.from_rows(((0,),))
            and continuation["closure_complete"]
            and len(continuation["closure_matrices"]) == 2
            and continuation["valid"]
            and all(row["valid"] for row in continuation["recovery_rows"]),
            f"literal ontology chain {measurement.candidate_id}",
        )
    witnesses["literal_ontology_chain"] = {
        row.candidate_id: row.native_measurements["ontology_chain"]
        for row in classification.candidate_measurements
    }
    checks.append("v5-literal-ontology-chain-support-reader-and-closure")

    quantum = right.native_measurements["quantum"]
    half = GaussianRational(Fraction(1, 2))
    _require(
        quantum["valid"]
        and quantum["D_residual"]["nonzero_count"] == 0
        and tuple(row["determinant"] for row in quantum["D_principal_minors"])
        == (
            GaussianRational(Fraction(1, 4)),
            GaussianRational(Fraction(1, 4)),
            GZERO,
        )
        and quantum["z_adjoint_D_z"] == GONE
        and quantum["A_bar_scalar"] == GONE
        and quantum["A_wrong_scalar"] == GZERO
        and quantum["division_completeness_residual"]["nonzero_count"] == 0
        and quantum["flag_dilation_isometry_residual"]["nonzero_count"] == 0
        and quantum["coherent_p_plus"] == GONE
        and quantum["incoherent_history_sum"] == half
        and quantum["port_weighted_cross_term"] == half
        and quantum["unweighted_cross_operator_nonzero_count"] == 0
        and quantum["P_adjoint_P_residual"]["nonzero_count"] == 0
        and quantum["P_transpose_P_residual"]["nonzero_count"] > 0,
        "phase-bearing exact quantum control",
    )
    witnesses["phase_bearing_quantum"] = quantum
    checks.append("v5-phase-bearing-quantum-history-division-and-interference")

    overlap = right.native_measurements["overlap"]
    _require(
        overlap["valid"]
        and overlap["selected_candidate_id"] == "global:ABC:owned"
        and overlap["zero_markov_residual_survivors"]
        == ("global:ABC:owned",)
        and overlap["parity_global_same_shadow_control"]["present"]
        and overlap["parity_global_same_shadow_control"]["same_AB_BC_shadows"]
        and overlap["parity_global_same_shadow_control"]["global_objects_distinct"]
        and not overlap["parity_global_same_shadow_control"][
            "scientific_primary_affected"
        ],
        "owned ABC restrictions/parity non-kill",
    )
    witnesses["owned_ABC_and_parity_control"] = overlap
    checks.append("v5-owned-ABC-shadows-and-parity-global-nonkill")

    for measurement in classification.candidate_measurements:
        native = measurement.native_measurements
        _require(
            native["comparison"]["valid"]
            and native["causal_order"]["valid"]
            and native["generated_contact"]["valid"]
            and native["compiler"]["valid"]
            and native["locality"]["valid"]
            and native["generated_contact"]["target_reader_factorization_residual"][
                "nonzero_count"
            ]
            == 0,
            f"comparison/influence/compiler/locality {measurement.candidate_id}",
        )
    witnesses["remaining_native_coordinates"] = {
        row.candidate_id: {
            name: row.native_measurements[name]
            for name in (
                "comparison",
                "causal_order",
                "generated_contact",
                "compiler",
                "locality",
            )
        }
        for row in classification.candidate_measurements
    }
    checks.append("v5-comparison-influence-compiler-and-locality-native-gates")

    expected_attack_primaries = {
        "RESET-ONE": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "NONINVOLUTIVE": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "STALE-CACHE": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "CLONE-ID": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "SEVER-OCCURRENCE": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "ZERO-SLICE": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "CANCELLED-LOOP": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "CARRIER-ONLY": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "RESTRICTION-CACHE": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "REMOVE-BRIDGE": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "LABEL-ONLY-JOINT": "APR-BLOCKED-AT-BOUNDARY-GLUING",
        "ALIEN-CARRIER": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "ISOMORPHIC-DISCONNECT": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "DUPLICATE-ID": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "BRANCH-SUM-ONLY": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "ONE-COLUMN-TENSOR": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "SINGLE-INPUT-READER": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "HIDDEN-ERASER": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "CALIBRATION-BYPASS": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
        "CONTACT-IDENTITY": "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED",
    }
    attack_rows: dict[str, object] = {}
    attack_classifications: dict[str, ExecutableFamilyClassification] = {}
    attack_families: dict[str, ExecutableLawFamily] = {}
    for fault, expected_primary in expected_attack_primaries.items():
        stale_payload = (
            {
                "forged_old_primary": (
                    "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED"
                ),
                "forged_old_selected": "L_X",
                "forged_old_measurement_sha256": canonical_sha256(
                    classification.to_data()
                ),
            }
            if fault == "STALE-CACHE"
            else None
        )
        attack_family = build_executable_family(
            fault, cached_measurement=stale_payload
        )
        attack_classification = classify_primitive_law(attack_family)
        _require(
            attack_classification.primary == expected_primary
            and attack_classification.primary
            != "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED"
            and attack_classification.selected_candidate_id is None
            and attack_classification.issues,
            f"attack survived or wrong precedence: {fault} "
            f"{attack_classification.primary} {attack_classification.issues}",
        )
        attack_families[fault] = attack_family
        attack_classifications[fault] = attack_classification
        attack_rows[fault] = _v5_attack_witness(
            attack_family, attack_classification
        )
    witnesses["registered_attack_objects_and_drops"] = attack_rows

    for fault in ("RESET-ONE", "NONINVOLUTIVE", "STALE-CACHE"):
        attacked = attack_classifications[fault].candidate_measurements[1]
        _require(
            not attacked.native_measurements["transition"]["valid"]
            and not attacked.coordinates["horizontal_process"]
            and attacked.selection_response == _v5_basis_state(2, 1),
            f"transition attack did not recompute/fail typing: {fault}",
        )
    stale_measurement = attack_classifications["STALE-CACHE"].candidate_measurements[1]
    _require(
        stale_measurement.native_measurements["structural_typing"][
            "cached_measurement_payloads_ignored"
        ]
        and not stale_measurement.dataflow_dag["cached_payload_edges"],
        "stale cache entered dependency graph",
    )
    checks.append("v5-reset-noninvolutive-and-stale-cache-drops")

    clone_measurement = attack_classifications["CLONE-ID"].candidate_measurements[1]
    _require(
        not clone_measurement.dataflow_dag["connected"]
        and any("single-resolved-T" in row for row in clone_measurement.issues)
        and len(attack_families["CLONE-ID"].candidates[1].transitions) == 2,
        "clone ID attack welded by hash/root",
    )
    for fault in (
        "SEVER-OCCURRENCE",
        "ZERO-SLICE",
        "CANCELLED-LOOP",
        "CARRIER-ONLY",
    ):
        attacked = attack_classifications[fault].candidate_measurements[1]
        _require(
            not attacked.dataflow_dag["valid"]
            and not attacked.coordinates["backward_slice_connected"],
            f"severed native occurrence survived: {fault}",
        )
    for fault in ("ZERO-SLICE", "CANCELLED-LOOP"):
        attacked = attack_classifications[fault].candidate_measurements[1]
        _require(
            attacked.dataflow_dag["auxiliary_claims_not_admitted"]
            and all(
                "auxiliary:" not in node_id
                for node_id in attacked.dataflow_dag["nodes"]
            ),
            f"auxiliary fake dependency admitted: {fault}",
        )
    checks.append("v5-clone-sever-zero-cancel-and-carrier-only-drops")

    restriction = attack_classifications[
        "RESTRICTION-CACHE"
    ].candidate_measurements[1].native_measurements["overlap"]
    _require(
        not restriction["valid"]
        and restriction["selected_candidate_id"]
        == "global:ABC:parity-control"
        and restriction["cached_restrictions_ignored"]
        and restriction["parity_global_same_shadow_control"]["same_AB_BC_shadows"],
        "restriction cache selected detached shadows",
    )
    checks.append("v5-owned-global-restriction-cache-drop")

    ontology_expectations = {
        "ALIEN-CARRIER": "RECORD-WRITING-ON-FIXED-ALGEBRA",
        "ISOMORPHIC-DISCONNECT": "FIXED-ALGEBRA-CONDITIONING",
        "REMOVE-BRIDGE": "RECORD-WRITING-ON-FIXED-ALGEBRA",
        "LABEL-ONLY-JOINT": "RECORD-WRITING-ON-FIXED-ALGEBRA",
    }
    for fault, expected_role in ontology_expectations.items():
        attacked = attack_classifications[fault].candidate_measurements[1]
        _require(
            attacked.ontology_role == expected_role
            and not attacked.coordinates["ontology_region_rewriting"],
            f"ontology weld attack promoted: {fault} {attacked.ontology_role}",
        )
    duplicate = attack_classifications["DUPLICATE-ID"].candidate_measurements[1]
    _require(
        duplicate.issues
        and not duplicate.valid
        and duplicate.ontology_role != "REGION-REWRITING",
        "duplicate-ID issue was not fatal before promotion",
    )
    checks.append("v5-ontology-carrier-bridge-label-and-duplicate-drops")

    branch = attack_classifications["BRANCH-SUM-ONLY"].candidate_measurements[1]
    one_column = attack_classifications[
        "ONE-COLUMN-TENSOR"
    ].candidate_measurements[1]
    single_reader = attack_classifications[
        "SINGLE-INPUT-READER"
    ].candidate_measurements[1]
    hidden_eraser = attack_classifications[
        "HIDDEN-ERASER"
    ].candidate_measurements[1]
    calibration_bypass = attack_classifications[
        "CALIBRATION-BYPASS"
    ].candidate_measurements[1]
    _require(
        not branch.native_measurements["instrument"][
            "semantic_projective_branches"
        ]
        and not one_column.native_measurements["ontology_chain"][
            "regional_rewrite"
        ]["valid"]
        and one_column.native_measurements["ontology_chain"][
            "regional_rewrite"
        ]["supplied_tensor_lift_ignored"]
        is not None
        and single_reader.native_measurements["ontology_chain"][
            "delayed_reader_and_continuations"
        ]["reader_residual"]["nonzero_count"]
        > 0
        and set(
            hidden_eraser.native_measurements["ontology_chain"]
            ["delayed_reader_and_continuations"]["actual_continuation_ids"]
        )
        != set(
            hidden_eraser.native_measurements["ontology_chain"]
            ["delayed_reader_and_continuations"]["licensed_continuation_ids"]
        )
        and not calibration_bypass.native_measurements["ontology_chain"]["valid"],
        "Seat-2 ontology/instrument hardening attack survived",
    )
    checks.append("v5-branch-column-reader-eraser-and-calibration-drops")

    contact_only = attack_classifications["CONTACT-IDENTITY"]
    contact_attacked = contact_only.candidate_measurements[1]
    _require(
        contact_only.walls == ("missing generated_contact",)
        and contact_attacked.dataflow_dag["connected"]
        and contact_attacked.coordinates["causal_order"]
        and not contact_attacked.coordinates["generated_contact"],
        "generated-contact-only classifier gate",
    )
    checks.append("v5-generated-contact-only-classifier-gate")

    moved_family = build_executable_family("MOVE-DOWNSTREAM")
    moved_classification = classify_primitive_law(moved_family)
    moved_left = moved_classification.candidate_measurements[0]
    _require(
        moved_left.valid
        and moved_left.composed_map != left.composed_map
        and moved_left.selection_response != left.selection_response
        and canonical_sha256(moved_left.selection_residual)
        != canonical_sha256(left.selection_residual)
        and moved_classification.primary
        == "APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED"
        and moved_classification.selected_candidate_id is None
        and moved_classification.family_residuals["zero_residual_survivors"]
        == ("L_I", "L_X")
        and not moved_classification.family_residuals["movement_assay"]["valid"],
        "MOVE-DOWNSTREAM movement/duplicate-family refusal",
    )
    witnesses["MOVE-DOWNSTREAM"] = {
        **_v5_attack_witness(moved_family, moved_classification),
        "isolated_L_I_before": left,
        "isolated_L_I_after": moved_left,
        "movement": {
            "P_moved": moved_left.composed_map != left.composed_map,
            "r_moved": moved_left.selection_response != left.selection_response,
            "selection_residual_moved": canonical_sha256(
                moved_left.selection_residual
            )
            != canonical_sha256(left.selection_residual),
        },
    }
    checks.append("v5-move-downstream-recomputes-then-duplicate-family-refuses")

    transition_x = family.candidates[1].transitions[0].matrix
    conjugation_measurement = _v5_phase_quantum_measurement(
        family.candidates[1].quantum,
        transition_x,
        source_variant="CONJUGATION-SOURCE",
    )
    history_transpose_measurement = _v5_phase_quantum_measurement(
        family.candidates[1].quantum,
        transition_x,
        source_variant="HISTORY-TRANSPOSE",
    )
    z_transpose_measurement = _v5_phase_quantum_measurement(
        family.candidates[1].quantum,
        transition_x,
        source_variant="Z-TRANSPOSE",
    )
    conjugation_attack = _v5_source_mutation_record(
        marker="V5-CONJUGATION-SOURCE-TARGET",
        old_text="coefficient.conjugate()",
        new_text="coefficient",
        semantic_measurement=conjugation_measurement,
    )
    history_attack = _v5_source_mutation_record(
        marker="V5-HISTORY-TRANSPOSE-SOURCE-TARGET",
        old_text="_g_adjoint(histories[right])",
        new_text="_g_transpose(histories[right])",
        semantic_measurement=history_transpose_measurement,
    )
    z_attack = _v5_source_mutation_record(
        marker="V5-Z-TRANSPOSE-SOURCE-TARGET",
        old_text="_g_adjoint(z_column)",
        new_text="_g_transpose(z_column)",
        semantic_measurement=z_transpose_measurement,
    )
    _require(
        not conjugation_measurement["valid"]
        and conjugation_measurement["gram_operator_identity_residual"][
            "nonzero_count"
        ]
        == 1
        and conjugation_measurement["A_bar_scalar"] == GZERO
        and conjugation_attack["original_source_sha256"]
        != conjugation_attack["changed_source_sha256"],
        "CONJUGATION-SOURCE did not flip operator identity",
    )
    _require(
        not history_transpose_measurement["valid"]
        and history_transpose_measurement["D_residual"]["nonzero_count"] > 0
        and history_attack["original_source_sha256"]
        != history_attack["changed_source_sha256"]
        and not z_transpose_measurement["valid"]
        and z_transpose_measurement["gram_operator_identity_residual"][
            "nonzero_count"
        ]
        == 1
        and z_attack["original_source_sha256"]
        != z_attack["changed_source_sha256"],
        "history/z transpose source attacks survived",
    )
    witnesses["quantum_source_attacks"] = {
        "CONJUGATION-SOURCE": conjugation_attack,
        "HISTORY-TRANSPOSE": history_attack,
        "Z-TRANSPOSE": z_attack,
    }
    checks.append("v5-conjugation-source-attack-changes-operator-identity")
    checks.append("v5-history-and-z-transpose-source-attacks-drop")

    forgery_rows: list[dict[str, object]] = []
    forged_objects: tuple[object, ...] = (
        {"primary": "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED"},
        ForgedExecutableMeasurement(
            True,
            "APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED",
            0,
        ),
        classification,
        right,
        family.candidates[1],
        build_capability_primitive_law(),
    )
    for forged in forged_objects:
        refused = False
        reason = ""
        try:
            classify_primitive_law(forged)
        except ScoreRefusal as exc:
            refused = True
            reason = str(exc)
        _require(refused, f"forged/detached classifier input survived: {type(forged)}")
        payload = forged.to_data() if hasattr(forged, "to_data") else forged
        forgery_rows.append(
            {
                "payload": payload,
                "payload_sha256": canonical_sha256(payload),
                "refused": refused,
                "reason": reason,
            }
        )
    witnesses["classifier_forgery_refusals"] = tuple(forgery_rows)
    checks.append("v5-public-classifier-refuses-detached-and-forged-results")

    source_text = Path(__file__).read_text(encoding="utf-8")
    forbidden_division_species = "division " + "configuration"
    _require(
        V5_SCOPE_SENTENCE
        == (
            "ISP's candidate ontology is one actual, law-sufficient relational "
            "configuration; its missing fundamental dynamics is an indivisible "
            "stochastic law of transition probabilities between complete "
            "configurations, conditioned at admissible division events/times. "
            "Hilbert/history machinery is representational, and APR's AB/BC table "
            "is only a simultaneous regional-gluing diagnostic—not that law."
        )
        and forbidden_division_species not in source_text.lower()
        and STATIC_QUALIFIER
        == "APR-STATIC-RAW-PREFIX-SYNTAX-ATOMLESS-RESPONSE-CONSTRUCTED-PROCESS-UNBUILT"
        and BLINDING_STATUS == "RESULT-KNOWN-BEFORE-V4-IMPLEMENTATION"
        and "note-apr-v5-executable-law-weld-pin.md" not in IMMUTABLE_HASHES,
        "v5 exact scope/qualifier/exposure or scientific receipt immutability",
    )
    witnesses["scope_exposure_and_scientific_boundary"] = {
        "canonical_scope_sentence": V5_SCOPE_SENTENCE,
        "static_qualifier": STATIC_QUALIFIER,
        "blinding_status": BLINDING_STATUS,
        "exposure_debt": EXPOSURE_DEBT,
        "AB_BC_role": (
            "SIMULTANEOUS-REGIONAL-GLUING-DIAGNOSTIC-NOT-TRANSITION-LAW"
        ),
        "candidate_fundamental_law_status": (
            "UNCONSTRUCTED-INDIVISIBLE-STOCHASTIC-RELATIONAL-TRANSITION-LAW"
        ),
        "v5_pin_appended_to_scientific_receipt_hashes": False,
    }
    checks.append("v5-exact-scope-qualifier-exposure-and-receipt-boundary")

    _require(
        len(checks) == 47 and len(set(checks)) == 47,
        f"v5 exact check registry: {len(checks)}",
    )
    return {
        "schema": "apr-generic-selftest-v5",
        "scientific_fixture_evaluated": False,
        "fixture_import_denial_active": True,
        "scorer_source_sha256": sha256_path(Path(__file__)),
        "check_count": len(checks),
        "checks": checks,
        "semantic_witnesses": witnesses,
        "semantic_witness_sha256": canonical_sha256(witnesses),
        "registered_attack_count": len(expected_attack_primaries) + 4,
        "registered_attacks": tuple(expected_attack_primaries) + (
            "MOVE-DOWNSTREAM",
            "CONJUGATION-SOURCE",
            "HISTORY-TRANSPOSE",
            "Z-TRANSPOSE",
        ),
        "status": "PASS",
    }


def run_v5_selftests() -> dict[str, object]:
    fixture_import_attempts: list[str] = []
    original_import = builtins.__import__

    def deny_fixture_import(
        name: str,
        globals: Mapping[str, object] | None = None,
        locals: Mapping[str, object] | None = None,
        fromlist: Sequence[str] = (),
        level: int = 0,
    ) -> object:
        if name == "apr_fixtures" or name.endswith(".apr_fixtures"):
            fixture_import_attempts.append(name)
            raise AssertionError("fixture import denied during v5 selftest")
        return original_import(name, globals, locals, fromlist, level)

    builtins.__import__ = deny_fixture_import
    try:
        payload = _run_v5_fixture_denied_selftests()
    finally:
        builtins.__import__ = original_import
    _require(
        not fixture_import_attempts,
        f"scientific fixture import attempted: {fixture_import_attempts}",
    )
    payload["fixture_import_attempts"] = tuple(fixture_import_attempts)
    payload["fixture_import_denial_active"] = True
    return payload


def run_selftests() -> dict[str, object]:
    return run_v5_selftests()


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
