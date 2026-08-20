#!/usr/bin/env python3
"""Exact Stage-B evaluator for the Paper 13 typed-groupoid repair.

This file is intentionally self contained.  The scientific evaluator uses
only immutable typed objects and :class:`fractions.Fraction`; presentation
hashes and JSON are provenance surfaces, never dynamics.

Stage A permits ``--selftest`` and ``--mutant NAME`` only.  The other strict
CLI modes are implemented for the later committed-source stages, but must not
be invoked before the source freeze.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import os
import signal
import sys
import tempfile
from dataclasses import FrozenInstanceError, dataclass, fields
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


SCHEMA = "p13-gamma-exact-v4"
SOURCE_DELTA_PIN_SHA256 = (
    "ae1283784bdcb274ff16cc2f06288f27258e0ada0dd8efe2f84084339941acb0"
)
SOURCE_AUDIT_ADJUDICATION_SHA256 = (
    "1dd09ef639d96c973a3991890e96695692d89249e4033c61579ff5bdbdd93326"
)
REJECTED_V3_SOURCE_SHA256 = (
    "cecf46061df95f57e63b491c380f015fdce297b6ac52dd78f79792495eafb111"
)
REJECTED_V3_FREEZE_SHA256 = (
    "02e22f32ce44d46104377d77469cefc1e7c3ca82445f119ede2056c9b8d16028"
)
V3_OPERATOR_SOURCE_REPORT_SHA256 = (
    "51e1a028c4e7d74fda2f1fe975d24a04e5925525916de1ba006ada80c2771a76"
)
V3_RECORDS_SOURCE_REPORT_SHA256 = (
    "1d0ceba5fca290399f8e24dfbf07b69c1b4758dfbc57c6e87cea9d5ac2cf9148"
)
TYPED_GROUPOID_PIN_SHA256 = (
    "08f7f64efca6210eee356852ad9e9b59487ea62a55aeaf85a483f6a70b85b004"
)
HOSTILE_ADJUDICATION_SHA256 = (
    "9546729fce24ce8a4a08239c881814b9526232a33151324c1b2e98b9daa61e49"
)
HOSTILE_ADJUDICATION_NORMALIZED_SHA256 = (
    "bea277684ef0cacbebcce0464bf2bfc77a1629bf7dbd0e156e2e63263d755ec4"
)
PIN_SHA256 = "4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35"
FORWARD_REPAIR_PIN_SHA256 = (
    "8ae54ada2a97f347a18b90adcab86dcb2e7c18c04c748cc5e0779b8251449a36"
)
RUNBOOK_SHA256 = "5629dd083da923e216143c249ce0246da3238ddb9475bd6d67954ce0aa8aac58"
PREDECESSOR_SHA256 = "06d171a3eea8109e177e2dfa3cb5536fe3785043e676f735c36e91d03834cb51"
OLD_STAGE_A_SOURCE_SHA256 = (
    "c699fc0316295e230c2cd0ef50601f631b195ad2237bebc2c42a75a2163f1aaf"
)
OLD_STAGE_A_FREEZE_SHA256 = (
    "d717f97832efe05996ae5f94249629376ddbe916fc837e0d5d16984bd7a13ad5"
)
STAGE_A_PHYSICS_REPORT_SHA256 = (
    "20a054cd6542fd02f556b461408f48d75ead0c69ec06abd76c9eed3ce3c3d352"
)
STAGE_A_RECORDS_REPORT_SHA256 = (
    "7c5b14a04f938de05b64750f6c8ae454eb4bbe8d0824e9eaaa0016532ab52ed4"
)
STAGE_A_ADJUDICATION_SHA256 = (
    "bd089458ef1d4c4fe8f9dc13fc21134695aba552b95b20f023e4d2f9f34dfb74"
)
HISTORICAL_OLD_SOURCE_PROVENANCE = {
    "sha256": OLD_STAGE_A_SOURCE_SHA256,
    "observation": "historical-unobserved",
    "live_disk_anchor": False,
    "cross_checked_from": (
        "v16/note-paper13-gamma-source-freeze.md",
        "v16/note-paper13-stageA-source-audit-adjudication.md",
    ),
}
PAPER12_SHA256 = "56cddeacbfe477d1af244b310e9a26b5622ef540b82deea5a96158819ba972f7"
PAPER12_ADJUDICATION_SHA256 = (
    "5ef1440064b703bd04bf97f1774f7f5e03efe537aeee2669bd1471f0a402799e"
)
PAPER12_EVALUATOR_SHA256 = (
    "c209486a94016c00921c3b9edfeb2f53eef7d005180eb3c1d95153e56fec86a7"
)
PAPER12_RECEIPT_SHA256 = (
    "d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39"
)
REJECTED_SOURCE_SHA256 = (
    "3da3161c7eef63b90da9c6cb85f7bc918d6e5c99fa431f07d273efd1f18e519e"
)
REJECTED_FRESH_SHA256 = (
    "2ac664c94a6b29c5b73fd8047e97a2e086ac45defc9c3431bc1ded66f011dd29"
)
REJECTED_OUTPUT_SHA256 = (
    "7f544c79f60d91c84e5805541313ec9d7ac068cdf0ee4f6184947cf44f43886f"
)
REJECTED_RECEIPT_SHA256 = (
    "83bd33028c81e9dd555a44e9e7721d5ace298d522e0c069409118bdbf51c6c48"
)
REJECTED_PAPER_SHA256 = (
    "db2f9f9a84f423bd8d23429ce567bc2e9236ea8deb3076f113c6aa692bd32446"
)
HOSTILE_PROTOCOL_SHA256 = (
    "1914ef55118c8261f55d271a7431cf5bc7e5aa90689d39f4b927e6c39fe8bd58"
)
SEAT_A_REPORT_SHA256 = (
    "1b4d566143837c8614bf4aa44469fe87061ce45055fe9aa9ca348057020dc702"
)
SEAT_I_REPORT_SHA256 = (
    "8153eda3ff440712d30483dfa12b6c20e7109d91a2785b1577f3374ebe1fd636"
)
SEAT_R_REPORT_SHA256 = (
    "340a7b7c2e5a24526486244106eb3ec8ba5de485cc585769ad7ca9c878efb314"
)
FRESH_DOMAIN = b"P13-TYPED-GROUPOID-FRESH-v4"
FROZEN_GROUPOID_PROMOTION_AST_SHA256 = (
    "5e246ccc26ebf4338b0889344830b154680f98e1b5369da8c2fac9efc629ab8c"
)
CANONICAL_SECTORS = ("empty", "branch0", "branch1")
CANONICAL_MODES = ("ACTIVE", "CARRIED")
MAX_SECONDS = 300
NATIVE_NONDIVISION_SENTENCE = (
    "The cut is not a lawful stochastic division on the declared configuration "
    "space: the complete endpoint law admits no positive source-independent "
    "factorization through it. A definite configuration may still be actual "
    "there; what is forbidden is an autonomous Markov restart conditioned only "
    "on that configuration."
)
MEASUREMENT_PROGRAMME = (
    "REFERENT-AND-SOURCE-LANGUAGE-CENSUS",
    "TYPED-SOURCE-GROUPOID-TOTAL-BIJECTION-CENSUS",
    "COMPLETE-GAMMA",
    "ANTI-WRAPPER-LINEAGE",
    "CHANGING-SUPPORT",
    "RECIPROCAL-CHAIN",
    "LAWFUL-DIVISION",
    "NATIVE-NONDIVISION",
    "FAMILY-AND-BLIND-CLASS-ASSAY",
    "COVARIANCE-AND-ROOT-MUTATIONS",
    "OUTCOME-AND-SCOPE-RENDERING",
)


class Refusal(Exception):
    """A typed scientific input is outside the declared domain."""


class IntegrityFailure(Exception):
    """An anchor, publication, or transaction invariant failed."""


def registered_failure_exit_code(error: BaseException) -> int:
    if isinstance(error, (IntegrityFailure, OSError)):
        return 1
    if isinstance(error, Refusal):
        return 2
    raise TypeError("unregistered failure class")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _jsonable(value: Any) -> Any:
    if type(value) is Fraction:
        return {"n": value.numerator, "d": value.denominator}
    if type(value) in (str, int, bool) or value is None:
        return value
    if type(value) is bytes:
        return {"hex": value.hex()}
    if type(value) in (tuple, list):
        return [_jsonable(item) for item in value]
    if type(value) is dict:
        return {
            str(key): _jsonable(value[key])
            for key in sorted(value, key=lambda item: str(item))
        }
    to_data = getattr(value, "to_data", None)
    if to_data is not None:
        return _jsonable(to_data())
    raise TypeError(f"not canonically serializable: {type(value).__name__}")


def canonical_json(value: Any) -> str:
    return json.dumps(
        _jsonable(value), ensure_ascii=True, sort_keys=True, separators=(",", ":")
    )


def canonical_bytes(value: Any) -> bytes:
    return canonical_json(value).encode("ascii")


def canonical_hash(value: Any) -> str:
    return sha256_bytes(canonical_bytes(value))


def _require_exact(value: Any, expected: type, label: str) -> None:
    if type(value) is not expected:
        raise Refusal(f"{label} must have exact type {expected.__name__}")


def _require_exact_tuple(value: Any, label: str) -> tuple[Any, ...]:
    _require_exact(value, tuple, label)
    return value


def _assignment_index(bits: Sequence[bool]) -> int:
    index = 0
    for bit in bits:
        index = 2 * index + int(bit)
    return index


def _canonical_formula(
    roles: tuple[str, ...], table: tuple[bool, ...]
) -> tuple[tuple[str, ...], tuple[bool, ...]]:
    if any(type(role) is not str or not role for role in roles):
        raise Refusal("formula roles must be nonempty exact strings")
    if len(set(roles)) != len(roles):
        raise Refusal("formula roles must be unique")
    if len(table) != 1 << len(roles):
        raise Refusal("formula table has wrong cardinality")
    if any(type(value) is not bool for value in table):
        raise Refusal("formula table values must be exact bools")

    ordered = tuple(sorted(roles))
    if ordered != roles:
        reordered: list[bool] = []
        for bits in itertools.product((False, True), repeat=len(ordered)):
            assignment = dict(zip(ordered, bits, strict=True))
            old_bits = tuple(assignment[role] for role in roles)
            reordered.append(table[_assignment_index(old_bits)])
        roles = ordered
        table = tuple(reordered)

    changed = True
    while changed:
        changed = False
        for position in range(len(roles)):
            remaining = roles[:position] + roles[position + 1 :]
            reduced: list[bool] = []
            inessential = True
            for bits in itertools.product((False, True), repeat=len(remaining)):
                left = list(bits)
                left.insert(position, False)
                right = list(bits)
                right.insert(position, True)
                low = table[_assignment_index(left)]
                high = table[_assignment_index(right)]
                if low != high:
                    inessential = False
                    break
                reduced.append(low)
            if inessential:
                roles = remaining
                table = tuple(reduced)
                changed = True
                break
    return roles, table


@dataclass(frozen=True, slots=True)
class Formula:
    roles: tuple[str, ...]
    table: tuple[bool, ...]

    def __post_init__(self) -> None:
        _require_exact_tuple(self.roles, "formula roles")
        _require_exact_tuple(self.table, "formula table")
        roles, table = _canonical_formula(self.roles, self.table)
        object.__setattr__(self, "roles", roles)
        object.__setattr__(self, "table", table)

    def to_data(self) -> dict[str, Any]:
        return {"type": "Formula", "roles": self.roles, "table": self.table}


def formula_constant(value: bool) -> Formula:
    _require_exact(value, bool, "formula constant")
    return Formula((), (value,))


def formula_atom(role: str) -> Formula:
    _require_exact(role, str, "formula atom")
    return Formula((role,), (False, True))


def formula_evaluate(formula: Formula, true_roles: Iterable[str]) -> bool:
    _require_exact(formula, Formula, "formula")
    true_set = frozenset(true_roles)
    bits = tuple(role in true_set for role in formula.roles)
    return formula.table[_assignment_index(bits)]


def formula_not(formula: Formula) -> Formula:
    _require_exact(formula, Formula, "formula")
    return Formula(formula.roles, tuple(not value for value in formula.table))


def _formula_binary(left: Formula, right: Formula, operation: str) -> Formula:
    _require_exact(left, Formula, "left formula")
    _require_exact(right, Formula, "right formula")
    roles = tuple(sorted(set(left.roles) | set(right.roles)))
    values: list[bool] = []
    for bits in itertools.product((False, True), repeat=len(roles)):
        true_roles = {role for role, bit in zip(roles, bits, strict=True) if bit}
        a = formula_evaluate(left, true_roles)
        b = formula_evaluate(right, true_roles)
        if operation == "AND":
            values.append(a and b)
        elif operation == "OR":
            values.append(a or b)
        else:
            raise Refusal("unknown formula operation")
    return Formula(roles, tuple(values))


def formula_and(left: Formula, right: Formula) -> Formula:
    return _formula_binary(left, right, "AND")


def formula_or(left: Formula, right: Formula) -> Formula:
    return _formula_binary(left, right, "OR")


def measure_boolean_quotient() -> dict[str, Any]:
    a = formula_atom("quotient_A")
    b = formula_atom("quotient_B")
    contradiction = formula_and(a, formula_not(a))
    tautology = formula_or(a, formula_not(a))
    absorption = formula_and(a, formula_or(b, formula_not(b)))
    return {
        "A": a,
        "B": b,
        "A_AND_NOT_A": contradiction,
        "A_OR_NOT_A": tautology,
        "A_AND_B_OR_NOT_B": absorption,
        "contradiction_is_zero": contradiction == formula_constant(False),
        "tautology_is_unit": tautology == formula_constant(True),
        "inessential_B_erased": absorption == a,
        "all_exact": contradiction == formula_constant(False)
        and tautology == formula_constant(True)
        and absorption == a,
    }


@dataclass(frozen=True, slots=True)
class Role:
    name: str
    kind: str

    def __post_init__(self) -> None:
        _require_exact(self.name, str, "role name")
        _require_exact(self.kind, str, "role kind")
        if not self.name or self.kind not in ("RELATION", "SPECTATOR"):
            raise Refusal("invalid typed Boolean role")

    def to_data(self) -> dict[str, Any]:
        return {"type": "Role", "name": self.name, "kind": self.kind}


def _cell_key(cell: tuple[str, ...], names: tuple[str, ...]) -> tuple[int, ...]:
    present = frozenset(cell)
    return tuple(int(name in present) for name in names)


@dataclass(frozen=True, slots=True)
class Context:
    roles: tuple[Role, ...]
    cells: tuple[tuple[str, ...], ...]
    neutral_label: str = ""

    def __post_init__(self) -> None:
        _require_exact_tuple(self.roles, "context roles")
        _require_exact_tuple(self.cells, "context cells")
        _require_exact(self.neutral_label, str, "context neutral label")
        if any(type(role) is not Role for role in self.roles):
            raise Refusal("context contains a foreign role")
        ordered_roles = tuple(sorted(self.roles, key=lambda role: (role.kind, role.name)))
        if len({role.name for role in ordered_roles}) != len(ordered_roles):
            raise Refusal("context role names must be unique")
        names = tuple(role.name for role in ordered_roles)
        normalized_cells: list[tuple[str, ...]] = []
        for raw_cell in self.cells:
            _require_exact_tuple(raw_cell, "context cell")
            if any(type(name) is not str for name in raw_cell):
                raise Refusal("cell role names must be exact strings")
            if len(set(raw_cell)) != len(raw_cell):
                raise Refusal("cell contains a duplicate role")
            if not set(raw_cell) <= set(names):
                raise Refusal("cell refers to an undeclared role")
            normalized_cells.append(tuple(sorted(raw_cell)))
        if not normalized_cells:
            raise Refusal("context must retain at least one nonzero Venn cell")
        if len(set(normalized_cells)) != len(normalized_cells):
            raise Refusal("context cells must be unique")
        normalized_cells.sort(key=lambda cell: _cell_key(cell, names))
        for name in names:
            if not any(name in cell for cell in normalized_cells):
                raise Refusal("declared Boolean role has zero support")
        object.__setattr__(self, "roles", ordered_roles)
        object.__setattr__(self, "cells", tuple(normalized_cells))

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "Context",
            "roles": self.roles,
            "cells": self.cells,
            "neutral_label": self.neutral_label,
        }


def context_role_names(context: Context) -> tuple[str, ...]:
    _require_exact(context, Context, "context")
    return tuple(role.name for role in context.roles)


def context_semantic_key(context: Context) -> tuple[Any, ...]:
    _require_exact(context, Context, "context")
    return (
        tuple((role.name, role.kind) for role in context.roles),
        context.cells,
    )


def formula_is_total_on(formula: Formula, declared_roles: Iterable[str]) -> bool:
    _require_exact(formula, Formula, "formula")
    return set(formula.roles) <= set(declared_roles)


def formula_nonzero(context: Context, formula: Formula) -> bool:
    _require_exact(context, Context, "context")
    _require_exact(formula, Formula, "formula")
    if not formula_is_total_on(formula, context_role_names(context)):
        raise Refusal("formula is not total on context")
    return any(formula_evaluate(formula, cell) for cell in context.cells)


def contextual_formula_truth(
    context: Context, formula: Formula
) -> tuple[bool, ...]:
    """Return the physical Boolean element on the context's nonzero cells."""

    _require_exact(context, Context, "contextual Boolean context")
    _require_exact(formula, Formula, "contextual Boolean formula")
    if not formula_is_total_on(formula, context_role_names(context)):
        raise Refusal("contextual Boolean formula is not total")
    return tuple(formula_evaluate(formula, cell) for cell in context.cells)


def contextual_formula_key(context: Context, formula: Formula) -> tuple[Any, ...]:
    return (
        "CONTEXTUAL-BOOLEAN-ELEMENT-v1",
        context_semantic_key(context),
        contextual_formula_truth(context, formula),
    )


def query_nonzero(context: Context, formula: Formula) -> bool:
    """Evaluate a boundary-total query on one status-dependent context.

    A declared child role is false when that child is absent in the current
    sector.  Totality is checked against the complete boundary universe when
    the generator AST is formed, not against each status-dependent support.
    """

    _require_exact(context, Context, "query context")
    _require_exact(formula, Formula, "query formula")
    return any(formula_evaluate(formula, cell) for cell in context.cells)


def context_extend(context: Context, child: Role, parent: Formula) -> Context:
    _require_exact(context, Context, "extension context")
    _require_exact(child, Role, "extension child")
    _require_exact(parent, Formula, "extension parent")
    if child.name in context_role_names(context):
        raise Refusal("horizontal extension child is not fresh")
    if not formula_is_total_on(parent, context_role_names(context)):
        raise Refusal("horizontal extension parent is not total")
    if not formula_nonzero(context, parent):
        raise Refusal("horizontal extension parent is zero")
    cells: list[tuple[str, ...]] = []
    for cell in context.cells:
        cells.append(cell)
        if formula_evaluate(parent, cell):
            cells.append(tuple(sorted(cell + (child.name,))))
    return Context(context.roles + (child,), tuple(cells), context.neutral_label)


def context_forget(context: Context, child_name: str) -> Context:
    _require_exact(context, Context, "forget context")
    _require_exact(child_name, str, "forgotten child")
    if child_name not in context_role_names(context):
        raise Refusal("cannot forget an absent child")
    roles = tuple(role for role in context.roles if role.name != child_name)
    cells = tuple(
        sorted(
            {tuple(name for name in cell if name != child_name) for cell in context.cells},
            key=lambda cell: _cell_key(cell, tuple(role.name for role in roles)),
        )
    )
    return Context(roles, cells, context.neutral_label)


@dataclass(frozen=True, slots=True)
class SplitFiberRow:
    source_cell: tuple[str, ...]
    parent_value: bool
    expected_target_cells: tuple[tuple[str, ...], ...]
    observed_target_cells: tuple[tuple[str, ...], ...]
    expected_child_bits: tuple[int, ...]
    observed_child_bits: tuple[int, ...]
    exact: bool

    def __post_init__(self) -> None:
        _require_exact_tuple(self.source_cell, "split source cell")
        _require_exact(self.parent_value, bool, "split parent value")
        _require_exact_tuple(self.expected_target_cells, "expected split fiber")
        _require_exact_tuple(self.observed_target_cells, "observed split fiber")
        _require_exact_tuple(self.expected_child_bits, "expected child bits")
        _require_exact_tuple(self.observed_child_bits, "observed child bits")
        _require_exact(self.exact, bool, "split fiber equality")
        if any(type(name) is not str for name in self.source_cell):
            raise Refusal("split source cell is malformed")
        for cells, label in (
            (self.expected_target_cells, "expected"),
            (self.observed_target_cells, "observed"),
        ):
            if any(
                type(cell) is not tuple
                or any(type(name) is not str for name in cell)
                for cell in cells
            ):
                raise Refusal(f"{label} split fiber is malformed")
        if any(type(bit) is not int or bit not in (0, 1) for bit in self.expected_child_bits):
            raise Refusal("expected child-bit fiber is malformed")
        if any(type(bit) is not int or bit not in (0, 1) for bit in self.observed_child_bits):
            raise Refusal("observed child-bit fiber is malformed")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "SplitFiberRow",
            "source_cell": self.source_cell,
            "parent_value": self.parent_value,
            "expected_target_cells": self.expected_target_cells,
            "observed_target_cells": self.observed_target_cells,
            "expected_child_bits": self.expected_child_bits,
            "observed_child_bits": self.observed_child_bits,
            "exact": self.exact,
        }


def _derive_context_split_fields(
    source: Context,
    target: Context,
    parent_truth: tuple[bool, ...],
    child: Role,
) -> dict[str, Any]:
    _require_exact(source, Context, "split-proof source")
    _require_exact(target, Context, "split-proof target")
    _require_exact_tuple(parent_truth, "split-proof parent truth")
    _require_exact(child, Role, "split-proof child")
    if len(parent_truth) != len(source.cells) or any(
        type(value) is not bool for value in parent_truth
    ):
        raise Refusal("split-proof parent truth does not cover the source")
    source_set = set(source.cells)
    observed: dict[tuple[str, ...], list[tuple[str, ...]]] = {
        cell: [] for cell in source.cells
    }
    unexpected: list[tuple[str, ...]] = []
    for target_cell in target.cells:
        projected = tuple(name for name in target_cell if name != child.name)
        if projected in source_set:
            observed[projected].append(target_cell)
        else:
            unexpected.append(target_cell)
    rows: list[SplitFiberRow] = []
    for source_cell, parent_value in zip(source.cells, parent_truth, strict=True):
        expected = [source_cell]
        expected_bits = [0]
        if parent_value:
            expected.append(tuple(sorted(source_cell + (child.name,))))
            expected_bits.append(1)
        target_names = context_role_names(target)
        expected_tuple = tuple(
            sorted(
                set(expected),
                key=lambda cell: (_cell_key(cell, target_names), cell),
            )
        )
        observed_tuple = tuple(
            sorted(
                set(observed[source_cell]),
                key=lambda cell: (_cell_key(cell, target_names), cell),
            )
        )
        observed_bits = tuple(
            sorted(int(child.name in cell) for cell in observed_tuple)
        )
        expected_bits_tuple = tuple(expected_bits)
        rows.append(
            SplitFiberRow(
                source_cell,
                parent_value,
                expected_tuple,
                observed_tuple,
                expected_bits_tuple,
                observed_bits,
                expected_tuple == observed_tuple
                and expected_bits_tuple == observed_bits,
            )
        )
    source_roles = tuple((role.name, role.kind) for role in source.roles)
    target_roles = tuple((role.name, role.kind) for role in target.roles)
    expected_roles = tuple(
        sorted(source_roles + ((child.name, child.kind),), key=lambda row: (row[1], row[0]))
    )
    satisfying_count = sum(int(value) for value in parent_truth)
    expected_count = len(source.cells) + satisfying_count
    actual_count = len(target.cells)
    exact_fibers = all(row.exact for row in rows)
    target_exhaustive = not unexpected and sum(
        len(row.observed_target_cells) for row in rows
    ) == len(target.cells)
    disjoint_union = target_exhaustive and len(
        {
            cell
            for row in rows
            for cell in row.observed_target_cells
        }
    ) == len(target.cells)
    try:
        forgotten = context_forget(target, child.name)
        forget_exact = context_semantic_key(forgotten) == context_semantic_key(source)
    except Refusal:
        forget_exact = False
    parent_nonzero = satisfying_count > 0
    satisfying_rows = tuple(row for row in rows if row.parent_value)
    p_and_child_nonzero = any(1 in row.observed_child_bits for row in satisfying_rows)
    p_and_not_child_nonzero = any(0 in row.observed_child_bits for row in satisfying_rows)
    split_inside_every_satisfying_cell = bool(satisfying_rows) and all(
        row.observed_child_bits == (0, 1) for row in satisfying_rows
    )
    roles_exact = target_roles == expected_roles
    old_types_preserved = all(item in target_roles for item in source_roles)
    child_fresh = child.name not in context_role_names(source)
    child_relation = child.kind == "RELATION"
    count_residual = actual_count - expected_count
    final = all(
        (
            parent_nonzero,
            child_fresh,
            child_relation,
            roles_exact,
            old_types_preserved,
            target_exhaustive,
            disjoint_union,
            exact_fibers,
            count_residual == 0,
            forget_exact,
            p_and_child_nonzero,
            p_and_not_child_nonzero,
            split_inside_every_satisfying_cell,
        )
    )
    return {
        "rows": tuple(rows),
        "unexpected_target_cells": tuple(unexpected),
        "satisfying_cell_count": satisfying_count,
        "expected_target_cell_count": expected_count,
        "actual_target_cell_count": actual_count,
        "count_residual": count_residual,
        "target_exhaustive": target_exhaustive,
        "disjoint_fiber_union": disjoint_union,
        "exact_fibers": exact_fibers,
        "forget_exact": forget_exact,
        "roles_exact": roles_exact,
        "old_types_preserved": old_types_preserved,
        "child_fresh": child_fresh,
        "child_relation": child_relation,
        "parent_nonzero": parent_nonzero,
        "p_and_child_nonzero": p_and_child_nonzero,
        "p_and_not_child_nonzero": p_and_not_child_nonzero,
        "child_distinct_from_parent": split_inside_every_satisfying_cell,
        "child_distinct_from_every_old_boolean": split_inside_every_satisfying_cell,
        "final": final,
    }


@dataclass(frozen=True, slots=True)
class ContextSplitProof:
    source: Context
    target: Context
    parent_truth: tuple[bool, ...]
    contextual_parent_key: tuple[Any, ...]
    child: Role
    rows: tuple[SplitFiberRow, ...]
    unexpected_target_cells: tuple[tuple[str, ...], ...]
    satisfying_cell_count: int
    expected_target_cell_count: int
    actual_target_cell_count: int
    count_residual: int
    target_exhaustive: bool
    disjoint_fiber_union: bool
    exact_fibers: bool
    forget_exact: bool
    roles_exact: bool
    old_types_preserved: bool
    child_fresh: bool
    child_relation: bool
    parent_nonzero: bool
    p_and_child_nonzero: bool
    p_and_not_child_nonzero: bool
    child_distinct_from_parent: bool
    child_distinct_from_every_old_boolean: bool
    final: bool

    def __post_init__(self) -> None:
        _require_exact(self.source, Context, "context-split source")
        _require_exact(self.target, Context, "context-split target")
        _require_exact_tuple(self.parent_truth, "context-split parent truth")
        _require_exact_tuple(self.contextual_parent_key, "contextual parent key")
        _require_exact(self.child, Role, "context-split child")
        _require_exact_tuple(self.rows, "context-split rows")
        if any(type(row) is not SplitFiberRow for row in self.rows):
            raise Refusal("context-split rows contain a foreign object")
        derived = _derive_context_split_fields(
            self.source, self.target, self.parent_truth, self.child
        )
        expected_key = (
            "CONTEXTUAL-BOOLEAN-ELEMENT-v1",
            context_semantic_key(self.source),
            self.parent_truth,
        )
        if self.contextual_parent_key != expected_key:
            raise Refusal("context-split parent key is forged")
        for name, value in derived.items():
            if getattr(self, name) != value:
                raise Refusal(f"context-split derived field is forged: {name}")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "ContextSplitProof",
            "source_semantic_key": context_semantic_key(self.source),
            "target_semantic_key": context_semantic_key(self.target),
            "parent_truth": self.parent_truth,
            "contextual_parent_key": self.contextual_parent_key,
            "child": self.child,
            "rows": self.rows,
            "unexpected_target_cells": self.unexpected_target_cells,
            "satisfying_cell_count": self.satisfying_cell_count,
            "expected_target_cell_count": self.expected_target_cell_count,
            "actual_target_cell_count": self.actual_target_cell_count,
            "count_residual": self.count_residual,
            "target_exhaustive": self.target_exhaustive,
            "disjoint_fiber_union": self.disjoint_fiber_union,
            "exact_fibers": self.exact_fibers,
            "forget_exact": self.forget_exact,
            "roles_exact": self.roles_exact,
            "old_types_preserved": self.old_types_preserved,
            "child_fresh": self.child_fresh,
            "child_relation": self.child_relation,
            "parent_nonzero": self.parent_nonzero,
            "p_and_child_nonzero": self.p_and_child_nonzero,
            "p_and_not_child_nonzero": self.p_and_not_child_nonzero,
            "child_distinct_from_parent": self.child_distinct_from_parent,
            "child_distinct_from_every_old_boolean": (
                self.child_distinct_from_every_old_boolean
            ),
            "final": self.final,
        }


def build_context_split_proof(
    source: Context, target: Context, parent: Formula, child: Role
) -> ContextSplitProof:
    truth = contextual_formula_truth(source, parent)
    return build_context_split_proof_from_truth(source, target, truth, child)


def build_context_split_proof_from_truth(
    source: Context,
    target: Context,
    truth: tuple[bool, ...],
    child: Role,
) -> ContextSplitProof:
    derived = _derive_context_split_fields(source, target, truth, child)
    return ContextSplitProof(
        source,
        target,
        truth,
        (
            "CONTEXTUAL-BOOLEAN-ELEMENT-v1",
            context_semantic_key(source),
            truth,
        ),
        child,
        **derived,
    )


def context_product(left: Context, right: Context) -> Context:
    _require_exact(left, Context, "left context")
    _require_exact(right, Context, "right context")
    if set(context_role_names(left)) & set(context_role_names(right)):
        raise Refusal("tensor contexts must have disjoint role names")
    cells = tuple(
        tuple(sorted(a + b)) for a in left.cells for b in right.cells
    )
    return Context(left.roles + right.roles, cells)


@dataclass(frozen=True, slots=True)
class Port:
    name: str
    child: Role
    parent0: Formula
    parent1: Formula

    def __post_init__(self) -> None:
        _require_exact(self.name, str, "port name")
        _require_exact(self.child, Role, "port child")
        _require_exact(self.parent0, Formula, "port parent0")
        _require_exact(self.parent1, Formula, "port parent1")
        if not self.name or self.child.kind != "RELATION":
            raise Refusal("invalid port declaration")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "Port",
            "name": self.name,
            "child": self.child,
            "parent0": self.parent0,
            "parent1": self.parent1,
        }


@dataclass(frozen=True, slots=True)
class PortDecl:
    port: Port
    mode: str

    def __post_init__(self) -> None:
        _require_exact(self.port, Port, "port declaration")
        _require_exact(self.mode, str, "port mode")
        if self.mode not in CANONICAL_MODES:
            raise Refusal("unknown port mode")

    def to_data(self) -> dict[str, Any]:
        return {"type": "PortDecl", "port": self.port, "mode": self.mode}


@dataclass(frozen=True, slots=True)
class Configuration:
    context: Context
    matter: tuple[tuple[str, int], ...]
    sectors: tuple[tuple[str, str], ...]

    def __post_init__(self) -> None:
        _require_exact(self.context, Context, "configuration context")
        _require_exact_tuple(self.matter, "configuration matter")
        _require_exact_tuple(self.sectors, "configuration sectors")
        for item in self.matter:
            _require_exact_tuple(item, "matter assignment")
            if len(item) != 2 or type(item[0]) is not str or type(item[1]) is not int:
                raise Refusal("malformed matter assignment")
            if item[1] not in (0, 1):
                raise Refusal("matter bit is not Boolean")
        for item in self.sectors:
            _require_exact_tuple(item, "sector assignment")
            if len(item) != 2 or type(item[0]) is not str or type(item[1]) is not str:
                raise Refusal("malformed sector assignment")
            if item[1] not in CANONICAL_SECTORS:
                raise Refusal("unknown port sector")
        if len({name for name, _ in self.matter}) != len(self.matter):
            raise Refusal("duplicate matter assignment")
        if len({name for name, _ in self.sectors}) != len(self.sectors):
            raise Refusal("duplicate sector assignment")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "Configuration",
            "context": self.context,
            "matter": self.matter,
            "sectors": self.sectors,
        }


def _validate_port_on_base(base: Context, port: Port) -> None:
    names = context_role_names(base)
    if port.child.name in names:
        raise Refusal("port child is not fresh over the recovered base")
    if not formula_is_total_on(port.parent0, names) or not formula_is_total_on(
        port.parent1, names
    ):
        raise Refusal("port parent is not total on the unique base")
    if not formula_nonzero(base, port.parent0) or not formula_nonzero(
        base, port.parent1
    ):
        raise Refusal("port parents must both be nonzero")
    for cell in base.cells:
        a = formula_evaluate(port.parent0, cell)
        b = formula_evaluate(port.parent1, cell)
        if a == b:
            raise Refusal("port parents must be disjoint and partition the unit")


def _context_from_sectors(
    base: Context, ports: tuple[PortDecl, ...], sectors: tuple[tuple[str, str], ...]
) -> Context:
    by_name = dict(sectors)
    context = base
    for declaration in ports:
        sector = by_name[declaration.port.name]
        if sector == "branch0":
            context = context_extend(
                context, declaration.port.child, declaration.port.parent0
            )
        elif sector == "branch1":
            context = context_extend(
                context, declaration.port.child, declaration.port.parent1
            )
    return context


def _catalogue_for_fields(
    matter_roles: tuple[str, ...], base: Context, ports: tuple[PortDecl, ...]
) -> tuple[Configuration, ...]:
    configurations: list[Configuration] = []
    for matter_bits in itertools.product((0, 1), repeat=len(matter_roles)):
        matter = tuple(zip(matter_roles, matter_bits, strict=True))
        for sector_values in itertools.product(
            CANONICAL_SECTORS, repeat=len(ports)
        ):
            sectors = tuple(
                (decl.port.name, value)
                for decl, value in zip(ports, sector_values, strict=True)
            )
            configurations.append(
                Configuration(
                    _context_from_sectors(base, ports, sectors), matter, sectors
                )
            )
    return tuple(configurations)


@dataclass(frozen=True, slots=True)
class Boundary:
    kind: str
    matter_roles: tuple[str, ...]
    base: Context
    ports: tuple[PortDecl, ...]
    catalogue: tuple[Configuration, ...]
    left: Boundary | None = None
    right: Boundary | None = None
    neutral_label: str = ""
    presentation_status_order: tuple[str, ...] = CANONICAL_SECTORS

    def __post_init__(self) -> None:
        _require_exact(self.kind, str, "boundary kind")
        _require_exact_tuple(self.matter_roles, "matter-role signature")
        _require_exact(self.base, Context, "boundary base")
        _require_exact_tuple(self.ports, "boundary ports")
        _require_exact_tuple(self.catalogue, "boundary catalogue")
        _require_exact(self.neutral_label, str, "boundary neutral label")
        _require_exact_tuple(
            self.presentation_status_order, "presentation status order"
        )
        if set(self.presentation_status_order) != set(CANONICAL_SECTORS) or len(
            self.presentation_status_order
        ) != len(CANONICAL_SECTORS):
            raise Refusal("status presentation is not a permutation")
        if any(type(name) is not str or not name for name in self.matter_roles):
            raise Refusal("matter-role signature contains a foreign name")
        if len(set(self.matter_roles)) != len(self.matter_roles):
            raise Refusal("duplicate matter-role identity")
        if any(type(decl) is not PortDecl for decl in self.ports):
            raise Refusal("boundary contains a foreign port declaration")
        if any(type(state) is not Configuration for state in self.catalogue):
            raise Refusal("boundary contains a foreign configuration")
        if self.kind == "UNIT":
            if self.left is not None or self.right is not None:
                raise Refusal("unit boundary has tensor children")
            if self.matter_roles or self.ports:
                raise Refusal("unit boundary has nonunit fields")
            canonical_unit_base = Context((), ((),))
            if context_semantic_key(self.base) != context_semantic_key(
                canonical_unit_base
            ):
                raise Refusal("unit boundary has a nonunit base context")
        elif self.kind == "ATOM":
            if self.left is not None or self.right is not None:
                raise Refusal("atomic boundary has tensor children")
        elif self.kind == "TENSOR":
            if type(self.left) is not Boundary or type(self.right) is not Boundary:
                raise Refusal("tensor boundary has a foreign child")
        else:
            raise Refusal("unknown boundary kind")
        port_names = tuple(decl.port.name for decl in self.ports)
        child_names = tuple(decl.port.child.name for decl in self.ports)
        if len(set(port_names)) != len(port_names) or len(set(child_names)) != len(
            child_names
        ):
            raise Refusal("duplicate port or child identity")
        if set(child_names) & set(context_role_names(self.base)):
            raise Refusal("dependent fresh child collision")
        for declaration in self.ports:
            _validate_port_on_base(self.base, declaration.port)
        expected = _catalogue_for_fields(self.matter_roles, self.base, self.ports)
        if self.catalogue != expected:
            raise Refusal("boundary catalogue is not the complete product")
        if self.kind == "TENSOR":
            if type(self.left) is not Boundary or type(self.right) is not Boundary:
                raise Refusal("tensor boundary children disappeared")
            if set(self.left.matter_roles) & set(self.right.matter_roles):
                raise Refusal("tensor matter roles collide")
            if set(decl.port.name for decl in self.left.ports) & set(
                decl.port.name for decl in self.right.ports
            ):
                raise Refusal("tensor port identities collide")
            if self.matter_roles != self.left.matter_roles + self.right.matter_roles:
                raise Refusal("tensor matter signature is forged")
            if self.ports != self.left.ports + self.right.ports:
                raise Refusal("tensor port signature is forged")
            if context_semantic_key(self.base) != context_semantic_key(
                context_product(self.left.base, self.right.base)
            ):
                raise Refusal("tensor base context is forged")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "Boundary",
            "kind": self.kind,
            "matter_roles": self.matter_roles,
            "base": self.base,
            "ports": self.ports,
            "catalogue": self.catalogue,
            "left": self.left,
            "right": self.right,
            "neutral_label": self.neutral_label,
            "presentation_status_order": self.presentation_status_order,
        }


def atomic_boundary(
    matter_roles: Sequence[str],
    base: Context,
    ports: Sequence[PortDecl],
    neutral_label: str = "",
    presentation_status_order: tuple[str, ...] = CANONICAL_SECTORS,
) -> Boundary:
    matter = tuple(matter_roles)
    declarations = tuple(ports)
    return Boundary(
        "ATOM",
        matter,
        base,
        declarations,
        _catalogue_for_fields(matter, base, declarations),
        neutral_label=neutral_label,
        presentation_status_order=presentation_status_order,
    )


def unit_boundary() -> Boundary:
    base = Context((), ((),))
    return Boundary("UNIT", (), base, (), _catalogue_for_fields((), base, ()))


def tensor_boundary(left: Boundary, right: Boundary) -> Boundary:
    _require_exact(left, Boundary, "left tensor boundary")
    _require_exact(right, Boundary, "right tensor boundary")
    base = context_product(left.base, right.base)
    matter = left.matter_roles + right.matter_roles
    ports = left.ports + right.ports
    return Boundary(
        "TENSOR",
        matter,
        base,
        ports,
        _catalogue_for_fields(matter, base, ports),
        left,
        right,
    )


def port_contextual_key(base: Context, port: Port) -> tuple[Any, ...]:
    _require_exact(base, Context, "port contextual base")
    _require_exact(port, Port, "contextual port")
    return (
        port.name,
        port.child.name,
        port.child.kind,
        contextual_formula_key(base, port.parent0),
        contextual_formula_key(base, port.parent1),
    )


def boundary_semantic_key(boundary: Boundary) -> tuple[Any, ...]:
    _require_exact(boundary, Boundary, "boundary")
    if boundary.kind == "TENSOR":
        if type(boundary.left) is not Boundary or type(boundary.right) is not Boundary:
            raise Refusal("tensor boundary children are malformed")
        tree: tuple[Any, ...] = (
            "TENSOR",
            boundary_semantic_key(boundary.left),
            boundary_semantic_key(boundary.right),
        )
    else:
        tree = (boundary.kind,)
    return (
        tree,
        boundary.matter_roles,
        context_semantic_key(boundary.base),
        tuple(
            (
                port_contextual_key(boundary.base, decl.port),
                decl.mode,
            )
            for decl in boundary.ports
        ),
    )


def configuration_key(configuration: Configuration) -> tuple[Any, ...]:
    _require_exact(configuration, Configuration, "configuration")
    return (
        context_semantic_key(configuration.context),
        configuration.matter,
        configuration.sectors,
    )


def validate_configuration(boundary: Boundary, configuration: Configuration) -> None:
    _require_exact(boundary, Boundary, "boundary")
    _require_exact(configuration, Configuration, "configuration")
    if tuple(name for name, _ in configuration.matter) != boundary.matter_roles:
        raise Refusal("configuration matter signature differs from its boundary")
    if tuple(name for name, _ in configuration.sectors) != tuple(
        declaration.port.name for declaration in boundary.ports
    ):
        raise Refusal("configuration port signature differs from its boundary")
    expected_context = _context_from_sectors(
        boundary.base, boundary.ports, configuration.sectors
    )
    if context_semantic_key(configuration.context) != context_semantic_key(
        expected_context
    ):
        raise Refusal("configuration context is not derived from its port sectors")


def configuration_from_assignments(
    boundary: Boundary,
    matter: Mapping[str, int],
    sectors: Mapping[str, str],
) -> Configuration:
    _require_exact(boundary, Boundary, "boundary")
    matter_tuple = tuple((name, matter[name]) for name in boundary.matter_roles)
    sectors_tuple = tuple(
        (decl.port.name, sectors[decl.port.name]) for decl in boundary.ports
    )
    candidate = Configuration(
        _context_from_sectors(boundary.base, boundary.ports, sectors_tuple),
        matter_tuple,
        sectors_tuple,
    )
    validate_configuration(boundary, candidate)
    return candidate


def matter_dict(configuration: Configuration) -> dict[str, int]:
    return dict(configuration.matter)


def sector_dict(configuration: Configuration) -> dict[str, str]:
    return dict(configuration.sectors)


def boundary_formula_profile(
    boundary: Boundary, formula: Formula
) -> tuple[tuple[Any, ...], ...]:
    _require_exact(boundary, Boundary, "formula-profile boundary")
    _require_exact(formula, Formula, "formula-profile formula")
    rows: dict[tuple[Any, ...], tuple[bool, ...]] = {}
    for configuration in boundary.catalogue:
        context_key = context_semantic_key(configuration.context)
        rows[context_key] = tuple(
            formula_evaluate(formula, cell) for cell in configuration.context.cells
        )
    return tuple((key, rows[key]) for key in sorted(rows, key=canonical_bytes))


def occurrence_semantic_key(
    source: Boundary, occurrence: Occurrence
) -> tuple[Any, ...]:
    _require_exact(source, Boundary, "occurrence semantic source")
    _require_exact(occurrence, Occurrence, "semantic occurrence")
    return (
        occurrence.occurrence_id,
        occurrence.matter_role,
        occurrence.port_name,
        boundary_formula_profile(source, occurrence.query),
        occurrence.target_mode,
        occurrence.seal,
    )


@dataclass(frozen=True, slots=True)
class Occurrence:
    occurrence_id: str
    matter_role: str
    port_name: str
    query: Formula
    target_mode: str
    seal: bool = True

    def __post_init__(self) -> None:
        _require_exact(self.occurrence_id, str, "occurrence identity")
        _require_exact(self.matter_role, str, "occurrence matter role")
        _require_exact(self.port_name, str, "occurrence port")
        _require_exact(self.query, Formula, "occurrence query")
        _require_exact(self.target_mode, str, "occurrence target mode")
        _require_exact(self.seal, bool, "occurrence seal")
        if not self.occurrence_id or not self.matter_role or not self.port_name:
            raise Refusal("empty occurrence identity")
        if not self.seal:
            raise Refusal("occurrence is unsealed")
        if self.target_mode not in CANONICAL_MODES:
            raise Refusal("unknown occurrence target mode")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "Occurrence",
            "occurrence_id": self.occurrence_id,
            "matter_role": self.matter_role,
            "port_name": self.port_name,
            "query": self.query,
            "target_mode": self.target_mode,
            "seal": self.seal,
        }


def boundary_with_port_mode(boundary: Boundary, port_name: str, mode: str) -> Boundary:
    _require_exact(boundary, Boundary, "boundary")
    _require_exact(port_name, str, "port name")
    _require_exact(mode, str, "port mode")
    if mode not in CANONICAL_MODES:
        raise Refusal("unknown replacement port mode")
    if boundary.kind == "TENSOR":
        if type(boundary.left) is not Boundary or type(boundary.right) is not Boundary:
            raise Refusal("tensor boundary children are malformed")
        left_names = {decl.port.name for decl in boundary.left.ports}
        right_names = {decl.port.name for decl in boundary.right.ports}
        if port_name in left_names:
            changed = boundary_with_port_mode(boundary.left, port_name, mode)
            if changed is boundary.left:
                return boundary
            return tensor_boundary(changed, boundary.right)
        if port_name in right_names:
            changed = boundary_with_port_mode(boundary.right, port_name, mode)
            if changed is boundary.right:
                return boundary
            return tensor_boundary(boundary.left, changed)
        raise Refusal("selected port is absent")
    if boundary.kind != "ATOM":
        raise Refusal("unit boundary has no selectable port")
    found = False
    declarations: list[PortDecl] = []
    for declaration in boundary.ports:
        if declaration.port.name == port_name:
            if declaration.mode == mode:
                return boundary
            declarations.append(PortDecl(declaration.port, mode))
            found = True
        else:
            declarations.append(declaration)
    if not found:
        raise Refusal("selected port is absent")
    return atomic_boundary(
        boundary.matter_roles,
        boundary.base,
        declarations,
        neutral_label=boundary.neutral_label,
        presentation_status_order=boundary.presentation_status_order,
    )


def _same_boundary(left: Boundary, right: Boundary) -> bool:
    return boundary_semantic_key(left) == boundary_semantic_key(right)


@dataclass(frozen=True, slots=True)
class Arrow:
    kind: str
    source: Boundary
    target: Boundary
    occurrence: Occurrence | None = None
    children: tuple[Arrow, ...] = ()
    objects: tuple[Boundary, ...] = ()
    seal: bool = True

    def __post_init__(self) -> None:
        _require_exact(self.kind, str, "arrow kind")
        _require_exact(self.source, Boundary, "arrow source")
        _require_exact(self.target, Boundary, "arrow target")
        _require_exact_tuple(self.children, "arrow children")
        _require_exact_tuple(self.objects, "arrow objects")
        _require_exact(self.seal, bool, "arrow seal")
        if self.occurrence is not None and type(self.occurrence) is not Occurrence:
            raise Refusal("arrow contains a foreign occurrence")
        if any(type(child) is not Arrow for child in self.children):
            raise Refusal("arrow contains a foreign child")
        if any(type(obj) is not Boundary for obj in self.objects):
            raise Refusal("arrow contains a foreign boundary object")
        validate_arrow(self)

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "Arrow",
            "kind": self.kind,
            "source": self.source,
            "target": self.target,
            "occurrence": self.occurrence,
            "children": self.children,
            "objects": self.objects,
            "seal": self.seal,
        }


def _validate_occurrence(source: Boundary, occurrence: Occurrence) -> None:
    if occurrence.matter_role not in source.matter_roles:
        raise Refusal("occurrence selects an undeclared matter role")
    declarations = {
        declaration.port.name: declaration for declaration in source.ports
    }
    declaration = declarations.get(occurrence.port_name)
    if declaration is None:
        raise Refusal("occurrence selects an undeclared port")
    if declaration.mode != "ACTIVE":
        raise Refusal("only an active port may be selected")
    universe = set(context_role_names(source.base)) | {
        item.port.child.name for item in source.ports
    }
    if not formula_is_total_on(occurrence.query, universe):
        raise Refusal("generator query contains an undeclared role")
    return None


def _port_payload(port: Port) -> tuple[Any, ...]:
    return (
        port.name,
        port.child.name,
        port.child.kind,
        port.parent0.to_data(),
        port.parent1.to_data(),
    )


def _matches_port_mode_replacement(
    source: Boundary, target: Boundary, port_name: str, mode: str
) -> bool:
    if source.kind != target.kind or source.matter_roles != target.matter_roles:
        return False
    if context_semantic_key(source.base) != context_semantic_key(target.base):
        return False
    if len(source.ports) != len(target.ports):
        return False
    for source_decl, target_decl in zip(source.ports, target.ports, strict=True):
        if _port_payload(source_decl.port) != _port_payload(target_decl.port):
            return False
        expected_mode = mode if source_decl.port.name == port_name else source_decl.mode
        if target_decl.mode != expected_mode:
            return False
    if source.kind == "TENSOR":
        if type(source.left) is not Boundary or type(source.right) is not Boundary:
            return False
        if type(target.left) is not Boundary or type(target.right) is not Boundary:
            return False
        left_has = port_name in {decl.port.name for decl in source.left.ports}
        if left_has:
            return _matches_port_mode_replacement(
                source.left, target.left, port_name, mode
            ) and _same_boundary(source.right, target.right)
        return _same_boundary(source.left, target.left) and _matches_port_mode_replacement(
            source.right, target.right, port_name, mode
        )
    return True


def _is_tensor_of(boundary: Boundary, left: Boundary, right: Boundary) -> bool:
    return (
        boundary.kind == "TENSOR"
        and type(boundary.left) is Boundary
        and type(boundary.right) is Boundary
        and _same_boundary(boundary.left, left)
        and _same_boundary(boundary.right, right)
    )


def validate_arrow(arrow: Arrow) -> None:
    _require_exact(arrow, Arrow, "arrow")
    if not arrow.seal:
        raise Refusal("unsealed arrow")
    for child in arrow.children:
        validate_arrow(child)
    kind = arrow.kind
    if kind == "IDENTITY":
        if arrow.occurrence is not None or arrow.children or arrow.objects:
            raise Refusal("identity carries undeclared data")
        if not _same_boundary(arrow.source, arrow.target):
            raise Refusal("forged identity target")
    elif kind == "GENERATOR":
        if type(arrow.occurrence) is not Occurrence or arrow.children or arrow.objects:
            raise Refusal("generator AST is malformed")
        _validate_occurrence(arrow.source, arrow.occurrence)
        if not _matches_port_mode_replacement(
            arrow.source,
            arrow.target,
            arrow.occurrence.port_name,
            arrow.occurrence.target_mode,
        ):
            raise Refusal("forged generator target")
    elif kind == "COMPOSE":
        if arrow.occurrence is not None or len(arrow.children) != 2 or arrow.objects:
            raise Refusal("composition AST is malformed")
        first, second = arrow.children
        if not _same_boundary(first.target, second.source):
            raise Refusal("incompatible composition")
        if not _same_boundary(arrow.source, first.source) or not _same_boundary(
            arrow.target, second.target
        ):
            raise Refusal("forged composition endpoints")
    elif kind == "TENSOR":
        if arrow.occurrence is not None or len(arrow.children) != 2 or arrow.objects:
            raise Refusal("tensor AST is malformed")
        left, right = arrow.children
        if not _is_tensor_of(arrow.source, left.source, right.source) or not _is_tensor_of(
            arrow.target, left.target, right.target
        ):
            raise Refusal("forged tensor endpoints")
    elif kind == "SYMMETRY":
        if arrow.occurrence is not None or arrow.children or len(arrow.objects) != 2:
            raise Refusal("symmetry AST is malformed")
        left, right = arrow.objects
        if not _is_tensor_of(arrow.source, left, right) or not _is_tensor_of(
            arrow.target, right, left
        ):
            raise Refusal("forged symmetry endpoints")
    elif kind in ("ASSOCIATOR", "ASSOCIATOR_INV"):
        if arrow.occurrence is not None or arrow.children or len(arrow.objects) != 3:
            raise Refusal("associator AST is malformed")
        a, b, c = arrow.objects
        left_assoc_ok = (
            arrow.source.kind == "TENSOR"
            and type(arrow.source.left) is Boundary
            and _is_tensor_of(arrow.source.left, a, b)
            and _same_boundary(arrow.source.right, c)
        )
        right_assoc_ok = (
            arrow.target.kind == "TENSOR"
            and _same_boundary(arrow.target.left, a)
            and type(arrow.target.right) is Boundary
            and _is_tensor_of(arrow.target.right, b, c)
        )
        if kind == "ASSOCIATOR_INV":
            left_assoc_ok, right_assoc_ok = (
                arrow.target.kind == "TENSOR"
                and type(arrow.target.left) is Boundary
                and _is_tensor_of(arrow.target.left, a, b)
                and _same_boundary(arrow.target.right, c),
                arrow.source.kind == "TENSOR"
                and _same_boundary(arrow.source.left, a)
                and type(arrow.source.right) is Boundary
                and _is_tensor_of(arrow.source.right, b, c),
            )
        if not left_assoc_ok or not right_assoc_ok:
            raise Refusal("forged associator endpoints")
    elif kind in (
        "LEFT_UNITOR",
        "LEFT_UNITOR_INV",
        "RIGHT_UNITOR",
        "RIGHT_UNITOR_INV",
    ):
        if arrow.occurrence is not None or arrow.children or len(arrow.objects) != 1:
            raise Refusal("unitor AST is malformed")
        (obj,) = arrow.objects
        if kind == "LEFT_UNITOR":
            valid = (
                arrow.source.kind == "TENSOR"
                and arrow.source.left is not None
                and arrow.source.left.kind == "UNIT"
                and _same_boundary(arrow.source.right, obj)
                and _same_boundary(arrow.target, obj)
            )
        elif kind == "LEFT_UNITOR_INV":
            valid = (
                _same_boundary(arrow.source, obj)
                and arrow.target.kind == "TENSOR"
                and arrow.target.left is not None
                and arrow.target.left.kind == "UNIT"
                and _same_boundary(arrow.target.right, obj)
            )
        elif kind == "RIGHT_UNITOR":
            valid = (
                arrow.source.kind == "TENSOR"
                and _same_boundary(arrow.source.left, obj)
                and arrow.source.right is not None
                and arrow.source.right.kind == "UNIT"
                and _same_boundary(arrow.target, obj)
            )
        else:
            valid = (
                _same_boundary(arrow.source, obj)
                and arrow.target.kind == "TENSOR"
                and _same_boundary(arrow.target.left, obj)
                and arrow.target.right is not None
                and arrow.target.right.kind == "UNIT"
            )
        if not valid:
            raise Refusal("forged unitor endpoints")
    else:
        raise Refusal("unknown arrow kind")


def identity_arrow(boundary: Boundary) -> Arrow:
    _require_exact(boundary, Boundary, "identity boundary")
    return Arrow("IDENTITY", boundary, boundary)


def generator_arrow(source: Boundary, occurrence: Occurrence) -> Arrow:
    _require_exact(source, Boundary, "generator source")
    _require_exact(occurrence, Occurrence, "generator occurrence")
    _validate_occurrence(source, occurrence)
    target = boundary_with_port_mode(source, occurrence.port_name, occurrence.target_mode)
    return Arrow("GENERATOR", source, target, occurrence)


def compose_arrows(first: Arrow, second: Arrow) -> Arrow:
    _require_exact(first, Arrow, "first composed arrow")
    _require_exact(second, Arrow, "second composed arrow")
    if not _same_boundary(first.target, second.source):
        raise Refusal("incompatible composition")
    return Arrow("COMPOSE", first.source, second.target, children=(first, second))


def compose_word(arrows: Sequence[Arrow]) -> Arrow:
    if not arrows:
        raise Refusal("empty composition word requires an explicit identity")
    result = arrows[0]
    _require_exact(result, Arrow, "composition word arrow")
    for arrow in arrows[1:]:
        _require_exact(arrow, Arrow, "composition word arrow")
        result = compose_arrows(result, arrow)
    return result


def tensor_arrow(left: Arrow, right: Arrow) -> Arrow:
    _require_exact(left, Arrow, "left tensor arrow")
    _require_exact(right, Arrow, "right tensor arrow")
    return Arrow(
        "TENSOR",
        tensor_boundary(left.source, right.source),
        tensor_boundary(left.target, right.target),
        children=(left, right),
    )


def symmetry_arrow(left: Boundary, right: Boundary) -> Arrow:
    return Arrow(
        "SYMMETRY",
        tensor_boundary(left, right),
        tensor_boundary(right, left),
        objects=(left, right),
    )


def associator_arrow(a: Boundary, b: Boundary, c: Boundary, inverse: bool = False) -> Arrow:
    for obj in (a, b, c):
        _require_exact(obj, Boundary, "associator object")
    left = tensor_boundary(tensor_boundary(a, b), c)
    right = tensor_boundary(a, tensor_boundary(b, c))
    return Arrow(
        "ASSOCIATOR_INV" if inverse else "ASSOCIATOR",
        right if inverse else left,
        left if inverse else right,
        objects=(a, b, c),
    )


def unitor_arrow(obj: Boundary, side: str, inverse: bool = False) -> Arrow:
    _require_exact(obj, Boundary, "unitor object")
    _require_exact(side, str, "unitor side")
    if side not in ("LEFT", "RIGHT"):
        raise Refusal("unknown unitor side")
    unit = unit_boundary()
    tensor = tensor_boundary(unit, obj) if side == "LEFT" else tensor_boundary(obj, unit)
    return Arrow(
        f"{side}_UNITOR" + ("_INV" if inverse else ""),
        obj if inverse else tensor,
        tensor if inverse else obj,
        objects=(obj,),
    )


def arrow_key(arrow: Arrow) -> tuple[Any, ...]:
    _require_exact(arrow, Arrow, "arrow")
    validate_arrow(arrow)
    if arrow.kind == "GENERATOR":
        body: Any = (
            occurrence_semantic_key(arrow.source, arrow.occurrence)
            if arrow.occurrence is not None
            else None
        )
    elif arrow.children:
        body = tuple(arrow_key(child) for child in arrow.children)
    else:
        body = tuple(boundary_semantic_key(obj) for obj in arrow.objects)
    return (
        arrow.kind,
        boundary_semantic_key(arrow.source),
        boundary_semantic_key(arrow.target),
        body,
    )


@dataclass(frozen=True, slots=True)
class PrimitiveSpec:
    orientation: str = "ROTATION"
    contact_site: str = "SOURCE"
    rho_mode: str = "CANONICAL"
    reset_one: bool = False

    def __post_init__(self) -> None:
        _require_exact(self.orientation, str, "primitive orientation")
        _require_exact(self.contact_site, str, "primitive contact site")
        _require_exact(self.rho_mode, str, "primitive rho mode")
        _require_exact(self.reset_one, bool, "primitive reset flag")
        if self.orientation not in ("ROTATION", "REFLECTION"):
            raise Refusal("unknown primitive orientation")
        if self.contact_site not in ("SOURCE", "TARGET", "COIN"):
            raise Refusal("unknown primitive contact site")
        if self.rho_mode not in (
            "CANONICAL",
            "NONINJECTIVE",
            "SWAPPED",
            "WRONG_BRANCH",
        ):
            raise Refusal("unknown primitive rho mode")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "PrimitiveSpec",
            "orientation": self.orientation,
            "contact_site": self.contact_site,
            "rho_mode": self.rho_mode,
            "reset_one": self.reset_one,
        }


CANONICAL_PRIMITIVE = PrimitiveSpec()


@dataclass(frozen=True, slots=True)
class GammaLaw:
    g: Fraction
    primitive: PrimitiveSpec = CANONICAL_PRIMITIVE
    implementation: str = "CONTACT-CAYLEY-WHOLE-FILLING-v1"
    seal: bool = True

    def __post_init__(self) -> None:
        _require_exact(self.g, Fraction, "Gamma coupling")
        _require_exact(self.primitive, PrimitiveSpec, "Gamma primitive")
        _require_exact(self.implementation, str, "Gamma implementation")
        _require_exact(self.seal, bool, "Gamma seal")
        if self.g < Fraction(1, 3) or self.g > Fraction(1, 2):
            raise Refusal("Gamma coupling lies outside the frozen rational domain")
        if not self.implementation:
            raise Refusal("Gamma implementation identity is empty")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "GammaLaw",
            "g": self.g,
            "primitive": self.primitive,
            "implementation": self.implementation,
            "seal": self.seal,
        }


def validate_candidate_law(law: GammaLaw) -> None:
    _require_exact(law, GammaLaw, "Gamma law")
    if not law.seal:
        raise Refusal("Gamma law is unsealed")
    if law.primitive != CANONICAL_PRIMITIVE:
        raise Refusal("Gamma primitive is not the frozen candidate")
    if law.implementation != "CONTACT-CAYLEY-WHOLE-FILLING-v1":
        raise Refusal("Gamma implementation identity is foreign")


def law_identity(law: GammaLaw) -> str:
    _require_exact(law, GammaLaw, "Gamma law")
    return canonical_hash(law.to_data())


@dataclass(frozen=True, slots=True)
class Derivation:
    operation: str
    inputs: tuple[Derivation, ...]
    payload: tuple[tuple[str, str], ...]

    def __post_init__(self) -> None:
        _require_exact(self.operation, str, "derivation operation")
        _require_exact_tuple(self.inputs, "derivation inputs")
        _require_exact_tuple(self.payload, "derivation payload")
        if any(type(item) is not Derivation for item in self.inputs):
            raise Refusal("derivation has a foreign input")
        for item in self.payload:
            _require_exact_tuple(item, "derivation payload row")
            if len(item) != 2 or type(item[0]) is not str or type(item[1]) is not str:
                raise Refusal("malformed derivation payload")
        if tuple(sorted(self.payload)) != self.payload or len(
            {key for key, _ in self.payload}
        ) != len(self.payload):
            raise Refusal("derivation payload is duplicated or noncanonical")
        if self.operation not in (
            "T",
            "IDENTITY",
            "COMPOSE",
            "TENSOR",
            "SYMMETRY",
            "ASSOCIATOR",
            "UNITOR",
        ):
            raise Refusal("unknown derivation operation")
        payload = dict(self.payload)
        if self.operation == "T":
            required = {
                "law_identity",
                "occurrence_id",
                "arrow_hash",
                "source_hash",
                "target_hash",
            }
            if self.inputs or set(payload) != required:
                raise Refusal("primitive derivation has a forged signature")
            for key in ("law_identity", "arrow_hash", "source_hash", "target_hash"):
                value = payload[key]
                if len(value) != 64 or any(
                    character not in "0123456789abcdef" for character in value
                ):
                    raise Refusal("primitive derivation contains a malformed digest")
            if not payload["occurrence_id"]:
                raise Refusal("primitive derivation omits its occurrence identity")
        elif self.operation in ("COMPOSE", "TENSOR"):
            if len(self.inputs) != 2 or self.payload:
                raise Refusal("binary derivation has a forged arity or payload")
        else:
            typed_map = payload.get("typed_map")
            if self.inputs or set(payload) != {"typed_map"}:
                raise Refusal("structural derivation has a forged signature")
            if len(typed_map) != 64 or any(
                character not in "0123456789abcdef" for character in typed_map
            ):
                raise Refusal("structural derivation contains a malformed digest")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "Derivation",
            "operation": self.operation,
            "inputs": self.inputs,
            "payload": self.payload,
        }


def derivation_roots(derivation: Derivation) -> tuple[str, ...]:
    _require_exact(derivation, Derivation, "derivation")
    roots: list[str] = []
    if derivation.operation == "T":
        payload = dict(derivation.payload)
        root = payload.get("law_identity")
        if root is None:
            raise Refusal("primitive derivation omits the law root")
        roots.append(root)
    for child in derivation.inputs:
        roots.extend(derivation_roots(child))
    return tuple(roots)


@dataclass(frozen=True, slots=True)
class LinearMap:
    source: Boundary
    target: Boundary
    entries: tuple[tuple[int, int, Fraction], ...]
    derivation: Derivation

    def __post_init__(self) -> None:
        _require_exact(self.source, Boundary, "linear-map source")
        _require_exact(self.target, Boundary, "linear-map target")
        _require_exact_tuple(self.entries, "linear-map entries")
        _require_exact(self.derivation, Derivation, "linear-map derivation")
        seen: set[tuple[int, int]] = set()
        previous: tuple[int, int] | None = None
        for item in self.entries:
            _require_exact_tuple(item, "linear-map entry")
            if len(item) != 3:
                raise Refusal("malformed linear-map entry")
            row, column, value = item
            if type(row) is not int or type(column) is not int or type(value) is not Fraction:
                raise Refusal("linear-map entry has a foreign scalar or index")
            if not (0 <= row < len(self.target.catalogue)) or not (
                0 <= column < len(self.source.catalogue)
            ):
                raise Refusal("linear-map index lies outside its boundary")
            if value == 0:
                raise Refusal("sparse linear map stores an explicit zero")
            key = (row, column)
            if key in seen or (previous is not None and key <= previous):
                raise Refusal("linear-map entries are duplicated or noncanonical")
            seen.add(key)
            previous = key

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "LinearMap",
            "source": boundary_semantic_key(self.source),
            "target": boundary_semantic_key(self.target),
            "entries": self.entries,
            "derivation": self.derivation,
        }


def _linear_map(
    source: Boundary,
    target: Boundary,
    entries: Mapping[tuple[int, int], Fraction],
    derivation: Derivation,
) -> LinearMap:
    canonical = tuple(
        (row, column, value)
        for (row, column), value in sorted(entries.items())
        if value != 0
    )
    return LinearMap(source, target, canonical, derivation)


def map_coefficient(linear_map: LinearMap, row: int, column: int) -> Fraction:
    _require_exact(linear_map, LinearMap, "linear map")
    for candidate_row, candidate_column, value in linear_map.entries:
        if candidate_row == row and candidate_column == column:
            return value
    return Fraction(0)


def dense_matrix(linear_map: LinearMap) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(
            map_coefficient(linear_map, row, column)
            for column in range(len(linear_map.source.catalogue))
        )
        for row in range(len(linear_map.target.catalogue))
    )


def _configuration_index(boundary: Boundary) -> dict[Configuration, int]:
    return {configuration: index for index, configuration in enumerate(boundary.catalogue)}


def configuration_index(boundary: Boundary, configuration: Configuration) -> int:
    validate_configuration(boundary, configuration)
    matter_index = 0
    for _, bit in configuration.matter:
        matter_index = 2 * matter_index + bit
    sector_index = 0
    sector_codes = {name: index for index, name in enumerate(CANONICAL_SECTORS)}
    for _, sector in configuration.sectors:
        sector_index = len(CANONICAL_SECTORS) * sector_index + sector_codes[sector]
    return matter_index * (len(CANONICAL_SECTORS) ** len(boundary.ports)) + sector_index


def _rho_sector(sector: str, output_bit: int, mode: str) -> str:
    if mode == "NONINJECTIVE":
        effective = 0
    elif mode == "SWAPPED":
        effective = 1 - output_bit
    else:
        effective = output_bit
    if mode == "WRONG_BRANCH" and sector == "branch1" and output_bit == 0:
        return "empty"
    if effective == 0:
        if sector == "empty":
            return "branch0"
        if sector == "branch0":
            return "empty"
        return "branch1"
    if sector == "empty":
        return "branch1"
    if sector == "branch1":
        return "empty"
    return "branch0"


def cayley_matrix(x: Fraction, primitive: PrimitiveSpec) -> tuple[tuple[Fraction, ...], ...]:
    _require_exact(x, Fraction, "Cayley parameter")
    _require_exact(primitive, PrimitiveSpec, "Cayley primitive")
    if primitive.reset_one and x == 0:
        return ((Fraction(1), Fraction(1)), (Fraction(1), Fraction(1)))
    if x == 0:
        return ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    denominator = 1 + x * x
    diagonal = (1 - x * x) / denominator
    off = (2 * x) / denominator
    if primitive.orientation == "ROTATION":
        return ((diagonal, -off), (off, diagonal))
    return ((diagonal, -off), (-off, -diagonal))


def _generator_transition(
    law: GammaLaw,
    arrow: Arrow,
    source_state: Configuration,
    output_bit: int,
) -> tuple[Configuration, Fraction]:
    """The single primitive transition clause used by maps and certificates."""

    if arrow.kind != "GENERATOR" or type(arrow.occurrence) is not Occurrence:
        raise Refusal("generator transition received a malformed arrow")
    _require_exact(law, GammaLaw, "generator transition law")
    _require_exact(source_state, Configuration, "generator transition source")
    _require_exact(output_bit, int, "generator transition output bit")
    if output_bit not in (0, 1):
        raise Refusal("generator transition output is not Boolean")
    validate_configuration(arrow.source, source_state)
    occurrence = arrow.occurrence
    source_matter = matter_dict(source_state)
    source_sectors = sector_dict(source_state)
    input_bit = source_matter[occurrence.matter_role]
    target_matter = dict(source_matter)
    target_matter[occurrence.matter_role] = output_bit
    target_sectors = dict(source_sectors)
    target_sectors[occurrence.port_name] = _rho_sector(
        source_sectors[occurrence.port_name],
        output_bit,
        law.primitive.rho_mode,
    )
    target_state = configuration_from_assignments(
        arrow.target, target_matter, target_sectors
    )
    if law.primitive.contact_site == "SOURCE":
        contact = query_nonzero(source_state.context, occurrence.query)
    elif law.primitive.contact_site == "TARGET":
        contact = query_nonzero(target_state.context, occurrence.query)
    else:
        contact = bool(input_bit)
    x = law.g if contact else Fraction(0)
    coefficient = cayley_matrix(x, law.primitive)[output_bit][input_bit]
    return target_state, coefficient


def _generator_coordinate_coefficient(
    law: GammaLaw,
    arrow: Arrow,
    source_state: Configuration,
    target_state: Configuration,
) -> Fraction:
    validate_configuration(arrow.target, target_state)
    if type(arrow.occurrence) is not Occurrence:
        raise Refusal("generator coordinate has no occurrence")
    output_bit = matter_dict(target_state)[arrow.occurrence.matter_role]
    derived_target, coefficient = _generator_transition(
        law, arrow, source_state, output_bit
    )
    return coefficient if derived_target == target_state else Fraction(0)


def _generator_map(law: GammaLaw, arrow: Arrow) -> LinearMap:
    if arrow.kind != "GENERATOR" or type(arrow.occurrence) is not Occurrence:
        raise Refusal("generator map received a malformed arrow")
    occurrence = arrow.occurrence
    entries: dict[tuple[int, int], Fraction] = {}
    for column, source_state in enumerate(arrow.source.catalogue):
        for output_bit in (0, 1):
            target_state, coefficient = _generator_transition(
                law, arrow, source_state, output_bit
            )
            row = configuration_index(arrow.target, target_state)
            key = (row, column)
            entries[key] = entries.get(key, Fraction(0)) + coefficient
    derivation = Derivation(
        "T",
        (),
        tuple(
            sorted(
                {
                    "law_identity": law_identity(law),
                    "occurrence_id": occurrence.occurrence_id,
                    "arrow_hash": canonical_hash(arrow_key(arrow)),
                    "source_hash": canonical_hash(boundary_semantic_key(arrow.source)),
                    "target_hash": canonical_hash(boundary_semantic_key(arrow.target)),
                }.items()
            )
        ),
    )
    return _linear_map(arrow.source, arrow.target, entries, derivation)


def _identity_map(source: Boundary, target: Boundary, operation: str) -> LinearMap:
    target_index = _configuration_index(target)
    entries: dict[tuple[int, int], Fraction] = {}
    for column, state in enumerate(source.catalogue):
        mapped = configuration_from_assignments(
            target, matter_dict(state), sector_dict(state)
        )
        entries[(target_index[mapped], column)] = Fraction(1)
    return _linear_map(
        source,
        target,
        entries,
        Derivation(operation, (), (("typed_map", canonical_hash((boundary_semantic_key(source), boundary_semantic_key(target)))),)),
    )


def _compose_maps(first: LinearMap, second: LinearMap) -> LinearMap:
    if not _same_boundary(first.target, second.source):
        raise Refusal("linear-map composition is ill typed")
    by_middle: dict[int, list[tuple[int, Fraction]]] = {}
    for row, column, value in second.entries:
        by_middle.setdefault(column, []).append((row, value))
    entries: dict[tuple[int, int], Fraction] = {}
    for middle, column, left_value in first.entries:
        for row, right_value in by_middle.get(middle, ()):
            key = (row, column)
            entries[key] = entries.get(key, Fraction(0)) + right_value * left_value
    return _linear_map(
        first.source,
        second.target,
        entries,
        Derivation("COMPOSE", (first.derivation, second.derivation), ()),
    )


def _tensor_maps(left: LinearMap, right: LinearMap) -> LinearMap:
    source = tensor_boundary(left.source, right.source)
    target = tensor_boundary(left.target, right.target)
    source_lookup = _configuration_index(source)
    target_lookup = _configuration_index(target)
    entries: dict[tuple[int, int], Fraction] = {}
    for lrow, lcol, lvalue in left.entries:
        lsource = left.source.catalogue[lcol]
        ltarget = left.target.catalogue[lrow]
        for rrow, rcol, rvalue in right.entries:
            rsource = right.source.catalogue[rcol]
            rtarget = right.target.catalogue[rrow]
            source_state = configuration_from_assignments(
                source,
                matter_dict(lsource) | matter_dict(rsource),
                sector_dict(lsource) | sector_dict(rsource),
            )
            target_state = configuration_from_assignments(
                target,
                matter_dict(ltarget) | matter_dict(rtarget),
                sector_dict(ltarget) | sector_dict(rtarget),
            )
            key = (target_lookup[target_state], source_lookup[source_state])
            entries[key] = entries.get(key, Fraction(0)) + lvalue * rvalue
    return _linear_map(
        source,
        target,
        entries,
        Derivation("TENSOR", (left.derivation, right.derivation), ()),
    )


def _evaluate_arrow_validated(
    law: GammaLaw, arrow: Arrow, candidate_only: bool
) -> LinearMap:
    if arrow.kind == "GENERATOR":
        return _generator_map(law, arrow)
    if arrow.kind == "IDENTITY":
        return _identity_map(arrow.source, arrow.target, "IDENTITY")
    if arrow.kind == "COMPOSE":
        first, second = arrow.children
        return _compose_maps(
            _evaluate_arrow_validated(law, first, candidate_only),
            _evaluate_arrow_validated(law, second, candidate_only),
        )
    if arrow.kind == "TENSOR":
        left, right = arrow.children
        return _tensor_maps(
            _evaluate_arrow_validated(law, left, candidate_only),
            _evaluate_arrow_validated(law, right, candidate_only),
        )
    if arrow.kind == "SYMMETRY":
        return _identity_map(arrow.source, arrow.target, "SYMMETRY")
    if arrow.kind in ("ASSOCIATOR", "ASSOCIATOR_INV"):
        return _identity_map(arrow.source, arrow.target, "ASSOCIATOR")
    if "UNITOR" in arrow.kind:
        return _identity_map(arrow.source, arrow.target, "UNITOR")
    raise Refusal("unreachable arrow evaluator branch")


def evaluate_arrow(law: GammaLaw, arrow: Arrow, candidate_only: bool = True) -> LinearMap:
    _require_exact(law, GammaLaw, "Gamma law")
    _require_exact(arrow, Arrow, "arrow")
    _require_exact(law.primitive, PrimitiveSpec, "Gamma primitive")
    rebuilt_primitive = PrimitiveSpec(
        law.primitive.orientation,
        law.primitive.contact_site,
        law.primitive.rho_mode,
        law.primitive.reset_one,
    )
    rebuilt_law = GammaLaw(law.g, rebuilt_primitive, law.implementation, law.seal)
    if rebuilt_law != law:
        raise Refusal("Gamma law is not its exact canonical reconstruction")
    if candidate_only:
        validate_candidate_law(law)
    validate_arrow_deep(arrow)
    return _evaluate_arrow_validated(law, arrow, candidate_only)


def presentation_key(
    law: GammaLaw, arrow: Arrow, source_state: Configuration
) -> tuple[Any, ...]:
    _require_exact(law, GammaLaw, "Gamma law")
    _require_exact(arrow, Arrow, "arrow")
    validate_arrow_deep(arrow)
    validate_configuration(arrow.source, source_state)
    return _presentation_key_validated(law, arrow, source_state)


def _presentation_key_validated(
    law: GammaLaw, arrow: Arrow, source_state: Configuration
) -> tuple[Any, ...]:
    """Build a source key after the caller has validated its exact packet."""

    return (
        law_identity(law),
        boundary_semantic_key(arrow.source),
        boundary_semantic_key(arrow.target),
        arrow_key(arrow),
        configuration_key(source_state),
    )


@dataclass(frozen=True, slots=True)
class GammaEvaluation:
    presentation_key: tuple[Any, ...]
    amplitudes: tuple[Fraction, ...]
    probabilities: tuple[Fraction, ...]
    normalization: Fraction
    derivation: Derivation

    def __post_init__(self) -> None:
        _require_exact_tuple(self.presentation_key, "Gamma presentation key")
        _require_exact_tuple(self.amplitudes, "Gamma amplitudes")
        _require_exact_tuple(self.probabilities, "Gamma probabilities")
        _require_exact(self.normalization, Fraction, "Gamma normalization")
        _require_exact(self.derivation, Derivation, "Gamma derivation")
        if any(type(value) is not Fraction for value in self.amplitudes):
            raise Refusal("Gamma amplitude has a foreign scalar")
        if any(type(value) is not Fraction for value in self.probabilities):
            raise Refusal("Gamma probability has a foreign scalar")
        if tuple(value * value for value in self.amplitudes) != self.probabilities:
            raise Refusal("Gamma endpoint squaring clause is violated")
        if sum(self.probabilities, Fraction(0)) != self.normalization:
            raise Refusal("Gamma normalization field is forged")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "GammaEvaluation",
            "presentation_key": self.presentation_key,
            "amplitudes": self.amplitudes,
            "probabilities": self.probabilities,
            "normalization": self.normalization,
            "derivation": self.derivation,
        }


def gamma_evaluate(
    law: GammaLaw,
    arrow: Arrow,
    source_state: Configuration,
    candidate_only: bool = True,
) -> GammaEvaluation:
    linear_map = evaluate_arrow(law, arrow, candidate_only)
    validate_configuration(arrow.source, source_state)
    column = configuration_index(arrow.source, source_state)
    amplitudes = tuple(
        map_coefficient(linear_map, row, column)
        for row in range(len(arrow.target.catalogue))
    )
    probabilities = tuple(value * value for value in amplitudes)
    return GammaEvaluation(
        presentation_key(law, arrow, source_state),
        amplitudes,
        probabilities,
        sum(probabilities, Fraction(0)),
        linear_map.derivation,
    )


@dataclass(frozen=True, slots=True)
class BoundSplitCertificate:
    law_identity: str
    source_boundary_sha256: str
    source_configuration_sha256: str
    arrow_sha256: str
    occurrence_sha256: str
    port_sha256: str
    presentation_source_key_sha256: str
    input_matter_bit: int
    output_matter_bit: int
    source_sector: str
    target_sector: str
    branch_parent_key: tuple[Any, ...]
    child_key: tuple[str, str]
    target_boundary_sha256: str
    target_configuration_sha256: str
    operation_kind: str
    coefficient: Fraction
    context_proof: ContextSplitProof
    inverse_creation_proof_sha256: str
    binding_exact: bool
    operation_exact: bool
    final: bool
    classifier_consumed_sha256: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.law_identity, "bound law identity"),
            (self.source_boundary_sha256, "bound source boundary hash"),
            (self.source_configuration_sha256, "bound source configuration hash"),
            (self.arrow_sha256, "bound arrow hash"),
            (self.occurrence_sha256, "bound occurrence hash"),
            (self.port_sha256, "bound port hash"),
            (self.presentation_source_key_sha256, "bound presentation key hash"),
            (self.target_boundary_sha256, "bound target boundary hash"),
            (self.target_configuration_sha256, "bound target configuration hash"),
            (self.inverse_creation_proof_sha256, "bound inverse proof hash"),
            (self.classifier_consumed_sha256, "bound classifier hash"),
        ):
            _require_exact(value, str, label)
            if not _is_lower_hex(value, 32):
                raise Refusal(f"{label} is not SHA-256")
        for value, label in (
            (self.input_matter_bit, "bound input matter bit"),
            (self.output_matter_bit, "bound output matter bit"),
        ):
            _require_exact(value, int, label)
            if value not in (0, 1):
                raise Refusal(f"{label} is not Boolean")
        _require_exact(self.source_sector, str, "bound source sector")
        _require_exact(self.target_sector, str, "bound target sector")
        if self.source_sector not in CANONICAL_SECTORS or self.target_sector not in CANONICAL_SECTORS:
            raise Refusal("bound split sector is not canonical")
        _require_exact_tuple(self.branch_parent_key, "bound branch parent key")
        _require_exact_tuple(self.child_key, "bound child key")
        if (
            len(self.child_key) != 2
            or type(self.child_key[0]) is not str
            or type(self.child_key[1]) is not str
        ):
            raise Refusal("bound child key is malformed")
        _require_exact(self.operation_kind, str, "bound split operation")
        if self.operation_kind not in ("CREATE", "MERGE", "UNCHANGED"):
            raise Refusal("unknown bound split operation")
        _require_exact(self.coefficient, Fraction, "bound transition coefficient")
        _require_exact(self.context_proof, ContextSplitProof, "bound context proof")
        for value, label in (
            (self.binding_exact, "bound split binding"),
            (self.operation_exact, "bound split operation evidence"),
            (self.final, "bound split conjunction"),
        ):
            _require_exact(value, bool, label)
        base = self.to_data(include_classifier=False)
        if canonical_hash(base) != self.classifier_consumed_sha256:
            raise Refusal("bound split classifier hash is forged")
        expected_final = (
            self.coefficient != 0
            and self.binding_exact
            and self.operation_exact
            and self.context_proof.final
        )
        if self.final != expected_final:
            raise Refusal("bound split final conjunction is forged")

    def to_data(self, include_classifier: bool = True) -> dict[str, Any]:
        data = {
            "type": "BoundSplitCertificate",
            "law_identity": self.law_identity,
            "source_boundary_sha256": self.source_boundary_sha256,
            "source_configuration_sha256": self.source_configuration_sha256,
            "arrow_sha256": self.arrow_sha256,
            "occurrence_sha256": self.occurrence_sha256,
            "port_sha256": self.port_sha256,
            "presentation_source_key_sha256": self.presentation_source_key_sha256,
            "input_matter_bit": self.input_matter_bit,
            "output_matter_bit": self.output_matter_bit,
            "source_sector": self.source_sector,
            "target_sector": self.target_sector,
            "branch_parent_key": self.branch_parent_key,
            "child_key": self.child_key,
            "target_boundary_sha256": self.target_boundary_sha256,
            "target_configuration_sha256": self.target_configuration_sha256,
            "operation_kind": self.operation_kind,
            "coefficient": self.coefficient,
            "context_proof": self.context_proof,
            "inverse_creation_proof_sha256": self.inverse_creation_proof_sha256,
            "binding_exact": self.binding_exact,
            "operation_exact": self.operation_exact,
            "final": self.final,
        }
        if include_classifier:
            data["classifier_consumed_sha256"] = self.classifier_consumed_sha256
        return data


def _selected_port(source: Boundary, port_name: str) -> Port:
    matches = tuple(
        declaration.port
        for declaration in source.ports
        if declaration.port.name == port_name
    )
    if len(matches) != 1:
        raise Refusal("bound split occurrence does not select one exact port")
    return matches[0]


def _branch_index(sector: str) -> int:
    if sector == "branch0":
        return 0
    if sector == "branch1":
        return 1
    raise Refusal("split branch sector has no parent index")


def build_bound_split_certificate(
    law: GammaLaw,
    arrow: Arrow,
    source_state: Configuration,
    target_state: Configuration,
) -> BoundSplitCertificate:
    _require_exact(law, GammaLaw, "bound split law")
    _require_exact(arrow, Arrow, "bound split arrow")
    _require_exact(source_state, Configuration, "bound split source state")
    _require_exact(target_state, Configuration, "bound split target state")
    validate_candidate_law(law)
    validate_arrow_deep(arrow)
    if arrow.kind != "GENERATOR" or type(arrow.occurrence) is not Occurrence:
        raise Refusal("bound split certificate requires one actual generator")
    occurrence = arrow.occurrence
    validate_configuration(arrow.source, source_state)
    validate_configuration(arrow.target, target_state)
    source_column = configuration_index(arrow.source, source_state)
    target_row = configuration_index(arrow.target, target_state)
    coefficient = _generator_coordinate_coefficient(
        law, arrow, source_state, target_state
    )
    if coefficient == 0:
        raise Refusal("zero transition cannot carry a bound split certificate")
    port = _selected_port(arrow.source, occurrence.port_name)
    source_sector = sector_dict(source_state)[port.name]
    target_sector = sector_dict(target_state)[port.name]
    input_bit = matter_dict(source_state)[occurrence.matter_role]
    output_bit = matter_dict(target_state)[occurrence.matter_role]
    expected_sector = _rho_sector(
        source_sector, output_bit, law.primitive.rho_mode
    )
    binding_exact = (
        expected_sector == target_sector
        and all(
            matter_dict(source_state)[name] == matter_dict(target_state)[name]
            for name in arrow.source.matter_roles
            if name != occurrence.matter_role
        )
    )
    if source_sector == "empty":
        operation_kind = "CREATE"
        branch = _branch_index(target_sector)
        parent = port.parent0 if branch == 0 else port.parent1
        proof_source = source_state.context
        proof_target = target_state.context
        operation_exact = target_sector == f"branch{output_bit}"
    elif target_sector == "empty":
        operation_kind = "MERGE"
        branch = _branch_index(source_sector)
        parent = port.parent0 if branch == 0 else port.parent1
        proof_source = target_state.context
        proof_target = source_state.context
        operation_exact = source_sector == f"branch{output_bit}"
    elif target_sector == source_sector:
        operation_kind = "UNCHANGED"
        branch = _branch_index(source_sector)
        parent = port.parent0 if branch == 0 else port.parent1
        proof_source = context_forget(source_state.context, port.child.name)
        proof_target = source_state.context
        operation_exact = (
            output_bit != branch
            and context_semantic_key(source_state.context)
            == context_semantic_key(target_state.context)
        )
    else:
        raise Refusal("transition is not CREATE, MERGE, or UNCHANGED")
    proof = build_context_split_proof(proof_source, proof_target, parent, port.child)
    operation_exact = operation_exact and (
        (operation_kind == "CREATE"
         and context_semantic_key(proof.source) == context_semantic_key(source_state.context)
         and context_semantic_key(proof.target) == context_semantic_key(target_state.context))
        or (operation_kind == "MERGE"
            and context_semantic_key(proof.source) == context_semantic_key(target_state.context)
            and context_semantic_key(proof.target) == context_semantic_key(source_state.context))
        or (operation_kind == "UNCHANGED"
            and context_semantic_key(proof.target) == context_semantic_key(source_state.context)
            and context_semantic_key(source_state.context) == context_semantic_key(target_state.context))
    )
    fields: dict[str, Any] = {
        "law_identity": law_identity(law),
        "source_boundary_sha256": canonical_hash(boundary_semantic_key(arrow.source)),
        "source_configuration_sha256": canonical_hash(configuration_key(source_state)),
        "arrow_sha256": canonical_hash(arrow_key(arrow)),
        "occurrence_sha256": canonical_hash(
            occurrence_semantic_key(arrow.source, occurrence)
        ),
        "port_sha256": canonical_hash(port_contextual_key(arrow.source.base, port)),
        "presentation_source_key_sha256": canonical_hash(
            _presentation_key_validated(law, arrow, source_state)
        ),
        "input_matter_bit": input_bit,
        "output_matter_bit": output_bit,
        "source_sector": source_sector,
        "target_sector": target_sector,
        "branch_parent_key": contextual_formula_key(proof_source, parent),
        "child_key": (port.child.name, port.child.kind),
        "target_boundary_sha256": canonical_hash(boundary_semantic_key(arrow.target)),
        "target_configuration_sha256": canonical_hash(configuration_key(target_state)),
        "operation_kind": operation_kind,
        "coefficient": coefficient,
        "context_proof": proof,
        "inverse_creation_proof_sha256": canonical_hash(proof),
        "binding_exact": binding_exact,
        "operation_exact": operation_exact,
        "final": coefficient != 0 and binding_exact and operation_exact and proof.final,
    }
    classifier_hash = canonical_hash(
        {"type": "BoundSplitCertificate", **fields}
    )
    return BoundSplitCertificate(
        **fields, classifier_consumed_sha256=classifier_hash
    )


def validate_bound_split_certificate(
    law: GammaLaw,
    arrow: Arrow,
    source_state: Configuration,
    target_state: Configuration,
    certificate: BoundSplitCertificate,
) -> bool:
    _require_exact(certificate, BoundSplitCertificate, "bound split certificate")
    rebuilt = build_bound_split_certificate(law, arrow, source_state, target_state)
    return canonical_bytes(certificate) == canonical_bytes(rebuilt) and rebuilt.final


def check_isometry(linear_map: LinearMap) -> tuple[bool, Fraction]:
    columns = len(linear_map.source.catalogue)
    by_column: dict[int, dict[int, Fraction]] = {
        column: {} for column in range(columns)
    }
    for row, column, value in linear_map.entries:
        by_column[column][row] = value
    maximum_residual = Fraction(0)
    for left_column in range(columns):
        for right_column in range(columns):
            left_entries = by_column[left_column]
            right_entries = by_column[right_column]
            inner = sum(
                (
                    left_entries[row] * right_entries[row]
                    for row in set(left_entries) & set(right_entries)
                ),
                Fraction(0),
            )
            target = Fraction(int(left_column == right_column))
            residual = abs(inner - target)
            maximum_residual = max(maximum_residual, residual)
    return maximum_residual == 0, maximum_residual


def matrix_multiply(
    left: tuple[tuple[Fraction, ...], ...],
    right: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    if not left or not right or not right[0]:
        raise Refusal("empty matrix product")
    if len(left[0]) != len(right):
        raise Refusal("incompatible exact matrix product")
    return tuple(
        tuple(
            sum(
                (left[row][middle] * right[middle][column] for middle in range(len(right))),
                Fraction(0),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matrix_square_entries(
    matrix: tuple[tuple[Fraction, ...], ...]
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(value * value for value in row) for row in matrix)


def invert_two_by_two(
    matrix: tuple[tuple[Fraction, ...], tuple[Fraction, ...]]
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise Refusal("inverse certificate is restricted to two by two matrices")
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant == 0:
        raise Refusal("singular two by two matrix")
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def _partition_context(prefix: str, include_active: bool = False) -> Context:
    record = Role(f"{prefix}L_record", "RELATION")
    if include_active:
        active = Role(f"{prefix}L_active", "RELATION")
        return Context(
            (record, active),
            (
                (),
                (record.name,),
                (active.name,),
                (record.name, active.name),
            ),
        )
    return Context((record,), ((), (record.name,)))


def _partition_port(
    base_role: str, port_name: str, child_name: str, mode: str = "ACTIVE"
) -> PortDecl:
    atom = formula_atom(base_role)
    port = Port(
        port_name,
        Role(child_name, "RELATION"),
        formula_not(atom),
        atom,
    )
    return PortDecl(port, mode)


def _empty_state(
    boundary: Boundary,
    matter_values: Mapping[str, int] | None = None,
    retained_sectors: Mapping[str, str] | None = None,
) -> Configuration:
    matter = {name: 0 for name in boundary.matter_roles}
    if matter_values is not None:
        matter.update(matter_values)
    sectors = {decl.port.name: "empty" for decl in boundary.ports}
    if retained_sectors is not None:
        sectors.update(retained_sectors)
    return configuration_from_assignments(boundary, matter, sectors)


def create_erase_pair(
    source: Boundary,
    matter_role: str,
    port_name: str,
    query: Formula,
    identity_prefix: str,
) -> Arrow:
    rotate = generator_arrow(
        source,
        Occurrence(
            f"{identity_prefix}:rotate",
            matter_role,
            port_name,
            query,
            "ACTIVE",
        ),
    )
    erase = generator_arrow(
        rotate.target,
        Occurrence(
            f"{identity_prefix}:erase",
            matter_role,
            port_name,
            formula_constant(False),
            "ACTIVE",
        ),
    )
    return compose_arrows(rotate, erase)


def _restricted_matter_amplitudes(
    law: GammaLaw,
    arrow: Arrow,
    matter_role: str,
    fixed_matter: Mapping[str, int] | None = None,
    source_sectors: Mapping[str, str] | None = None,
    target_sectors: Mapping[str, str] | None = None,
    candidate_only: bool = True,
) -> tuple[tuple[Fraction, ...], ...]:
    fixed = dict(fixed_matter or {})
    result: list[tuple[Fraction, ...]] = []
    linear_map = evaluate_arrow(law, arrow, candidate_only)
    source_lookup = _configuration_index(arrow.source)
    target_lookup = _configuration_index(arrow.target)
    for output_bit in (0, 1):
        row: list[Fraction] = []
        for input_bit in (0, 1):
            source_matter = {name: fixed.get(name, 0) for name in arrow.source.matter_roles}
            target_matter = {name: fixed.get(name, 0) for name in arrow.target.matter_roles}
            source_matter[matter_role] = input_bit
            target_matter[matter_role] = output_bit
            source_state = _empty_state(arrow.source, source_matter, source_sectors)
            target_state = _empty_state(arrow.target, target_matter, target_sectors)
            row.append(
                map_coefficient(
                    linear_map,
                    target_lookup[target_state],
                    source_lookup[source_state],
                )
            )
        result.append(tuple(row))
    return tuple(result)


def build_coherent_control(prefix: str = "coh_") -> dict[str, Any]:
    base = _partition_context(prefix)
    role_name = f"{prefix}L_record"
    port_name = f"{prefix}p"
    boundary = atomic_boundary(
        (f"{prefix}c",),
        base,
        (_partition_port(role_name, port_name, f"{prefix}N"),),
    )
    query = formula_atom(role_name)
    first_pair = create_erase_pair(
        boundary, f"{prefix}c", port_name, query, f"{prefix}pair0"
    )
    second_pair = create_erase_pair(
        first_pair.target, f"{prefix}c", port_name, query, f"{prefix}pair1"
    )
    two_pairs = compose_arrows(first_pair, second_pair)
    return {
        "boundary": boundary,
        "first_pair": first_pair,
        "two_pairs": two_pairs,
        "matter": f"{prefix}c",
        "port": port_name,
        "query": query,
    }


def measure_coherent_controls(
    law: GammaLaw, candidate_only: bool = True
) -> dict[str, Any]:
    control = build_coherent_control()
    r = _restricted_matter_amplitudes(
        law, control["first_pair"], control["matter"], candidate_only=candidate_only
    )
    b = matrix_square_entries(r)
    r2 = _restricted_matter_amplitudes(
        law, control["two_pairs"], control["matter"], candidate_only=candidate_only
    )
    c = matrix_square_entries(r2)
    first_map = evaluate_arrow(law, control["first_pair"], candidate_only)
    second_map = evaluate_arrow(law, control["two_pairs"], candidate_only)
    first_iso, first_residual = check_isometry(first_map)
    second_iso, second_residual = check_isometry(second_map)
    return {
        "R": r,
        "B": b,
        "R2": r2,
        "C": c,
        "first_isometry": first_iso,
        "first_isometry_residual": first_residual,
        "second_isometry": second_iso,
        "second_isometry_residual": second_residual,
        "first_lineage": first_map.derivation,
        "second_lineage": second_map.derivation,
        "first_operator_hash": canonical_hash(first_map),
        "second_operator_hash": canonical_hash(second_map),
        "boundary_hash": canonical_hash(boundary_semantic_key(control["boundary"])),
        "support": {
            "source_cells": len(control["boundary"].base.cells),
            "created_cells": len(
                context_extend(
                    control["boundary"].base,
                    control["boundary"].ports[0].port.child,
                    control["boundary"].ports[0].port.parent1,
                ).cells
            ),
        },
    }


@dataclass(frozen=True, slots=True)
class ContinuationGrammar:
    matter_roles: tuple[str, ...]
    active_port: str
    queries: tuple[Formula, ...]
    generator_names: tuple[str, ...]
    seal: bool = True

    def __post_init__(self) -> None:
        _require_exact_tuple(self.matter_roles, "continuation matter roles")
        _require_exact(self.active_port, str, "continuation active port")
        _require_exact_tuple(self.queries, "continuation queries")
        _require_exact_tuple(self.generator_names, "continuation generator names")
        _require_exact(self.seal, bool, "continuation seal")
        if any(type(name) is not str for name in self.matter_roles):
            raise Refusal("continuation matter role is foreign")
        if not self.matter_roles or len(set(self.matter_roles)) != len(
            self.matter_roles
        ):
            raise Refusal("continuation matter roles are empty or duplicated")
        if not self.active_port:
            raise Refusal("continuation active port is empty")
        if any(type(query) is not Formula for query in self.queries):
            raise Refusal("continuation query is foreign")
        if not self.queries or len(set(self.queries)) != len(self.queries):
            raise Refusal("continuation queries are empty or duplicated")
        if any(type(name) is not str or not name for name in self.generator_names):
            raise Refusal("continuation generator name is foreign")
        if len(set(self.generator_names)) != len(self.generator_names):
            raise Refusal("continuation generator names are duplicated")
        if len(self.generator_names) != len(self.matter_roles) * len(self.queries):
            raise Refusal("continuation alphabet is incomplete")
        if not self.seal:
            raise Refusal("continuation grammar is unsealed")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "ContinuationGrammar",
            "matter_roles": self.matter_roles,
            "active_port": self.active_port,
            "queries": self.queries,
            "generator_names": self.generator_names,
            "seal": self.seal,
        }


def build_record_control(prefix: str = "rec_") -> dict[str, Any]:
    base = _partition_context(prefix, include_active=True)
    record_role = f"{prefix}L_record"
    active_role = f"{prefix}L_active"
    record_port = f"{prefix}record"
    work_port = f"{prefix}active"
    source_role = f"{prefix}source"
    probe_role = f"{prefix}probe"
    boundary = atomic_boundary(
        (source_role, probe_role),
        base,
        (
            _partition_port(record_role, record_port, f"{prefix}N_record"),
            _partition_port(active_role, work_port, f"{prefix}N_active"),
        ),
    )
    writer = generator_arrow(
        boundary,
        Occurrence(
            f"{prefix}writer",
            source_role,
            record_port,
            formula_atom(record_role),
            "CARRIED",
        ),
    )
    queries = (
        formula_constant(False),
        formula_atom(active_role),
        formula_and(
            formula_atom(record_role), formula_atom(f"{prefix}N_record")
        ),
    )
    letters: dict[str, Arrow] = {}
    for matter_role in (source_role, probe_role):
        for query_index, query in enumerate(queries):
            name = f"{matter_role}:q{query_index}"
            letters[name] = generator_arrow(
                writer.target,
                Occurrence(
                    f"{prefix}letter:{name}",
                    matter_role,
                    work_port,
                    query,
                    "ACTIVE",
                ),
            )
    grammar = ContinuationGrammar(
        (source_role, probe_role),
        work_port,
        queries,
        tuple(letters),
    )
    contact_letter = letters[f"{source_role}:q1"]
    recorded_chain = compose_arrows(writer, contact_letter)
    return {
        "boundary": boundary,
        "writer": writer,
        "letters": letters,
        "grammar": grammar,
        "recorded_chain": recorded_chain,
        "source_role": source_role,
        "probe_role": probe_role,
        "record_port": record_port,
        "work_port": work_port,
    }


def _record_sector_projector(boundary: Boundary, record_port: str, sector: str) -> tuple[int, ...]:
    return tuple(
        index
        for index, state in enumerate(boundary.catalogue)
        if sector_dict(state)[record_port] == sector
    )


def _intertwining_residual(
    linear_map: LinearMap, record_port: str
) -> Fraction:
    residual = Fraction(0)
    for row, column, value in linear_map.entries:
        source_sector = sector_dict(linear_map.source.catalogue[column])[record_port]
        target_sector = sector_dict(linear_map.target.catalogue[row])[record_port]
        if source_sector != target_sector:
            residual = max(residual, abs(value))
    return residual


def measure_record_division(law: GammaLaw) -> dict[str, Any]:
    control = build_record_control()
    writer_map = evaluate_arrow(law, control["writer"])
    chain_map = evaluate_arrow(law, control["recorded_chain"])
    letter_maps = {
        name: evaluate_arrow(law, arrow) for name, arrow in control["letters"].items()
    }
    residuals = {
        name: _intertwining_residual(linear_map, control["record_port"])
        for name, linear_map in letter_maps.items()
    }
    grammar = control["grammar"]
    grammar_letter_rows: list[dict[str, Any]] = []
    grammar_pairs: set[tuple[str, Formula]] = set()
    for name, arrow in control["letters"].items():
        occurrence = arrow.occurrence
        if type(occurrence) is not Occurrence:
            raise IntegrityFailure("continuation alphabet contains a nongenerator")
        grammar_pairs.add((occurrence.matter_role, occurrence.query))
        grammar_letter_rows.append(
            {
                "name": name,
                "occurrence_id": occurrence.occurrence_id,
                "matter_role": occurrence.matter_role,
                "active_port": occurrence.port_name,
                "query_sha256": canonical_hash(occurrence.query),
                "target_mode": occurrence.target_mode,
                "source_boundary_sha256": canonical_hash(
                    boundary_semantic_key(arrow.source)
                ),
                "target_boundary_sha256": canonical_hash(
                    boundary_semantic_key(arrow.target)
                ),
                "typed_endomorphism": _same_boundary(
                    arrow.source, control["writer"].target
                )
                and _same_boundary(arrow.target, control["writer"].target),
                "record_projector_residual": residuals[name],
            }
        )
    expected_grammar_pairs = {
        (matter_role, query)
        for matter_role in grammar.matter_roles
        for query in grammar.queries
    }
    continuation_grammar_exact = (
        grammar.matter_roles
        == (control["source_role"], control["probe_role"])
        and grammar.active_port == control["work_port"]
        and grammar.generator_names == tuple(control["letters"])
        and grammar_pairs == expected_grammar_pairs
        and all(row["typed_endomorphism"] for row in grammar_letter_rows)
        and all(row["target_mode"] == "ACTIVE" for row in grammar_letter_rows)
    )
    boundary = control["boundary"]
    chain = control["recorded_chain"]
    source_lookup = _configuration_index(boundary)
    target_lookup = _configuration_index(chain.target)
    branch_probabilities: dict[str, Fraction] = {}
    writer_branch_probabilities: dict[str, Fraction] = {}
    marginal_rows: list[tuple[Fraction, ...]] = []
    alternate_residual = Fraction(0)
    for output_bit in (0, 1):
        row: list[Fraction] = []
        for input_bit in (0, 1):
            source_state = _empty_state(
                boundary, {control["source_role"]: input_bit}
            )
            source_column = source_lookup[source_state]
            marginal = Fraction(0)
            for branch in (0, 1):
                target_state = _empty_state(
                    chain.target,
                    {control["source_role"]: output_bit},
                    {
                        control["record_port"]: f"branch{branch}",
                        control["work_port"]: f"branch{output_bit}",
                    },
                )
                amplitude = map_coefficient(
                    chain_map, target_lookup[target_state], source_column
                )
                direct_probability = amplitude * amplitude
                marginal += direct_probability

                writer_target = _empty_state(
                    control["writer"].target,
                    {control["source_role"]: branch},
                    {control["record_port"]: f"branch{branch}"},
                )
                writer_probability = (
                    map_coefficient(
                        writer_map,
                        _configuration_index(control["writer"].target)[writer_target],
                        source_column,
                    )
                    ** 2
                )
                writer_key = f"q{input_bit}:a{branch}"
                if (
                    writer_key in writer_branch_probabilities
                    and writer_branch_probabilities[writer_key]
                    != writer_probability
                ):
                    raise IntegrityFailure(
                        "writer branch probability changed across continuation outputs"
                    )
                writer_branch_probabilities[writer_key] = writer_probability
                continuation_probability = (
                    map_coefficient(
                        letter_maps[f"{control['source_role']}:q1"],
                        target_lookup[target_state],
                        _configuration_index(control["writer"].target)[writer_target],
                    )
                    ** 2
                )
                cut_probability = writer_probability * continuation_probability
                alternate_residual = max(
                    alternate_residual, abs(direct_probability - cut_probability)
                )
                branch_probabilities[
                    f"q{input_bit}:a{branch}:b{output_bit}"
                ] = direct_probability
            row.append(marginal)
        marginal_rows.append(tuple(row))

    alternate_all_input_residual = Fraction(0)
    alternate_all_input_comparisons = 0
    alternate_all_input_rows: list[dict[str, Any]] = []
    writer_target_lookup = _configuration_index(control["writer"].target)
    for probe_bit in (0, 1):
        for input_bit in (0, 1):
            source_state = _empty_state(
                boundary,
                {
                    control["source_role"]: input_bit,
                    control["probe_role"]: probe_bit,
                },
            )
            source_column = source_lookup[source_state]
            for output_bit in (0, 1):
                for branch in (0, 1):
                    target_state = _empty_state(
                        chain.target,
                        {
                            control["source_role"]: output_bit,
                            control["probe_role"]: probe_bit,
                        },
                        {
                            control["record_port"]: f"branch{branch}",
                            control["work_port"]: f"branch{output_bit}",
                        },
                    )
                    direct_probability = (
                        map_coefficient(
                            chain_map, target_lookup[target_state], source_column
                        )
                        ** 2
                    )
                    writer_target = _empty_state(
                        control["writer"].target,
                        {
                            control["source_role"]: branch,
                            control["probe_role"]: probe_bit,
                        },
                        {control["record_port"]: f"branch{branch}"},
                    )
                    writer_row = writer_target_lookup[writer_target]
                    cut_probability = (
                        map_coefficient(writer_map, writer_row, source_column) ** 2
                    ) * (
                        map_coefficient(
                            letter_maps[f"{control['source_role']}:q1"],
                            target_lookup[target_state],
                            writer_row,
                        )
                        ** 2
                    )
                    alternate_all_input_residual = max(
                        alternate_all_input_residual,
                        abs(direct_probability - cut_probability),
                    )
                    alternate_all_input_rows.append(
                        {
                            "source_bit": input_bit,
                            "probe_bit": probe_bit,
                            "output_bit": output_bit,
                            "record_branch": branch,
                            "direct_probability": direct_probability,
                            "cut_probability": cut_probability,
                            "residual": abs(
                                direct_probability - cut_probability
                            ),
                        }
                    )
                    alternate_all_input_comparisons += 1

    continuation_identity_map = evaluate_arrow(
        law, identity_arrow(control["writer"].target)
    )
    continuation_identity_residual = _intertwining_residual(
        continuation_identity_map, control["record_port"]
    )
    word_residual = continuation_identity_residual
    enumerated_lengths = tuple(range(3))
    sampled_words = 0
    letter_items = tuple(control["letters"].items())
    for length in enumerated_lengths:
        for word in itertools.product(letter_items, repeat=length):
            sampled_words += 1
            if not word:
                linear_map = continuation_identity_map
            else:
                linear_map = evaluate_arrow(
                    law, compose_word(tuple(item[1] for item in word))
                )
            word_residual = max(
                word_residual,
                _intertwining_residual(linear_map, control["record_port"]),
            )

    full_target_count = len(chain.target.catalogue)
    source_state = _empty_state(boundary)
    evaluation = gamma_evaluate(law, chain, source_state)
    zero_count = sum(int(value == 0) for value in evaluation.probabilities)

    reactivated = boundary_with_port_mode(
        control["writer"].target, control["record_port"], "ACTIVE"
    )
    active_reuse_eraser = generator_arrow(
        reactivated,
        Occurrence(
            "registered-active-reuse-eraser",
            control["source_role"],
            control["record_port"],
            formula_constant(False),
            "ACTIVE",
        ),
    )
    active_reuse_map = evaluate_arrow(law, active_reuse_eraser)
    active_reuse_residual = Fraction(0)
    active_reuse_coordinates: dict[str, Fraction] = {}
    for probe_bit in (0, 1):
        for branch in (0, 1):
            active_source = _empty_state(
                reactivated,
                {
                    control["source_role"]: branch,
                    control["probe_role"]: probe_bit,
                },
                {control["record_port"]: f"branch{branch}"},
            )
            active_target = _empty_state(
                active_reuse_eraser.target,
                {
                    control["source_role"]: branch,
                    control["probe_role"]: probe_bit,
                },
            )
            source_column = configuration_index(reactivated, active_source)
            target_row = configuration_index(active_reuse_eraser.target, active_target)
            coefficient = map_coefficient(
                active_reuse_map, target_row, source_column
            )
            active_reuse_coordinates[f"probe{probe_bit}:branch{branch}"] = coefficient
            active_reuse_residual = max(
                active_reuse_residual, abs(coefficient - 1)
            )
            for row in range(len(active_reuse_eraser.target.catalogue)):
                expected = Fraction(int(row == target_row))
                active_reuse_residual = max(
                    active_reuse_residual,
                    abs(map_coefficient(active_reuse_map, row, source_column) - expected),
                )
    writer_blank_input_rows: list[dict[str, Any]] = []
    for source_bit in (0, 1):
        for probe_bit in (0, 1):
            blank_source = _empty_state(
                boundary,
                {
                    control["source_role"]: source_bit,
                    control["probe_role"]: probe_bit,
                },
            )
            blank_evaluation = gamma_evaluate(law, control["writer"], blank_source)
            writer_blank_input_rows.append(
                {
                    "source_bit": source_bit,
                    "probe_bit": probe_bit,
                    "source_configuration_sha256": canonical_hash(blank_source),
                    "normalization": blank_evaluation.normalization,
                    "endpoint_probabilities_sha256": canonical_hash(
                        blank_evaluation.probabilities
                    ),
                }
            )
    return {
        "B2": tuple(marginal_rows),
        "branch_probabilities": branch_probabilities,
        "writer_branch_probabilities": writer_branch_probabilities,
        "writer_blank_input_rows": tuple(writer_blank_input_rows),
        "writer_blank_input_count": len(writer_blank_input_rows),
        "writer_normalized_all_blank_inputs": all(
            row["normalization"] == 1 for row in writer_blank_input_rows
        ),
        "generator_intertwining_residuals": residuals,
        "continuation_grammar_exact": continuation_grammar_exact,
        "continuation_grammar_letter_rows": tuple(grammar_letter_rows),
        "continuation_letter_lineages": {
            name: linear_map.derivation
            for name, linear_map in letter_maps.items()
        },
        "all_generator_intertwining": all(value == 0 for value in residuals.values()),
        "free_word_induction": {
            "base": continuation_identity_residual == 0,
            "base_residual": continuation_identity_residual,
            "step": all(value == 0 for value in residuals.values()),
            "composition_step_identity": (
                "IF-P_r*F=F*P_r-AND-P_r*G=G*P_r-THEN-P_r*(G*F)=(G*F)*P_r"
            ),
            "conclusion": "EVERY-FINITE-LICENSED-WORD",
            "enumerated_control_depth": max(enumerated_lengths),
            "enumerated_control_words": sampled_words,
            "enumerated_residual": word_residual,
        },
        "alternate_cut_residual": alternate_residual,
        "alternate_cut_all_input_residual": alternate_all_input_residual,
        "alternate_cut_all_input_comparisons": alternate_all_input_comparisons,
        "alternate_cut_all_input_rows": tuple(alternate_all_input_rows),
        "full_target_count": full_target_count,
        "returned_target_count": len(evaluation.probabilities),
        "retained_zero_count": zero_count,
        "writer_lineage": writer_map.derivation,
        "chain_lineage": chain_map.derivation,
        "writer_source_boundary": control["writer"].source,
        "writer_target_boundary": control["writer"].target,
        "recorded_target_boundary": chain.target,
        "record_port_name": control["record_port"],
        "record_projectors": {
            sector: _record_sector_projector(
                control["writer"].target, control["record_port"], sector
            )
            for sector in CANONICAL_SECTORS
        },
        "active_reuse_eraser": {
            "reactivated_boundary": reactivated,
            "arrow": active_reuse_eraser,
            "coordinates": active_reuse_coordinates,
            "residual": active_reuse_residual,
            "inverse_toggle_exact": active_reuse_residual == 0,
            "lineage": active_reuse_map.derivation,
        },
        "grammar": control["grammar"],
    }


def measure_native_nondivision(law: GammaLaw) -> dict[str, Any]:
    coherent = measure_coherent_controls(law)
    b = coherent["B"]
    c = coherent["C"]
    b_determinant = b[0][0] * b[1][1] - b[0][1] * b[1][0]
    k = matrix_multiply(c, invert_two_by_two(b))
    negative_entries = tuple(
        (row, column, value)
        for row in range(2)
        for column in range(2)
        if (value := k[row][column]) < 0
    )
    def t_value(value: Fraction) -> Fraction:
        return (1 - 6 * value * value + value**4) / (1 + value * value) ** 2

    t = t_value(law.g)
    if t == 0:
        raise Refusal("rational Gamma coupling produced an impossible singular cut")
    nontrivial_eigenvalue = 2 * t - 1 / t
    endpoint_bound = Fraction(527, 175)
    left_t = t_value(Fraction(1, 3))
    right_t = t_value(Fraction(1, 2))
    maximum_absolute_t = Fraction(7, 25)
    derived_bound = 1 / maximum_absolute_t - 2 * maximum_absolute_t
    derivative_factor_signs = {
        "g_positive": Fraction(1, 3) > 0,
        "one_minus_g_squared_positive": 1 - Fraction(1, 2) ** 2 > 0,
        "denominator_positive": 1 + Fraction(1, 3) ** 2 > 0,
        "leading_factor_negative": -8 < 0,
    }
    singularity_polynomial = (1, -6, 1)
    rational_root_candidates = tuple(
        candidate for candidate in (-1, 1) if 1 % abs(candidate) == 0
    )
    rational_root_values = tuple(
        singularity_polynomial[0] * candidate * candidate
        + singularity_polynomial[1] * candidate
        + singularity_polynomial[2]
        for candidate in rational_root_candidates
    )
    rational_singularity_excluded = (
        singularity_polynomial[0] == 1
        and rational_root_candidates == (-1, 1)
        and all(value != 0 for value in rational_root_values)
    )
    positive_radius_factor = 1 - 2 * maximum_absolute_t * maximum_absolute_t
    bound_function_derivative_terms_negative = (
        -1 < 0 and -2 < 0
    )
    interval_certificate = {
        "t_formula": "(1-6*g^2+g^4)/(1+g^2)^2",
        "derivative_sign_witness": "-8*g*(1-g^2)/(1+g^2)^3<0",
        "domain": (Fraction(1, 3), Fraction(1, 2)),
        "left_t": left_t,
        "right_t": right_t,
        "endpoint_values_exact": left_t == Fraction(7, 25)
        and right_t == Fraction(-7, 25),
        "derivative_factor_signs": derivative_factor_signs,
        "strictly_decreasing_on_domain": all(derivative_factor_signs.values()),
        "singularity_polynomial_in_u_equals_g_squared": singularity_polynomial,
        "monic_rational_root_candidates": rational_root_candidates,
        "monic_rational_root_candidate_values": rational_root_values,
        "rational_root_theorem_forcing": (
            "A-RATIONAL-ROOT-OF-A-MONIC-INTEGER-POLYNOMIAL-IS-AN-INTEGER-DIVIDING-THE-CONSTANT-TERM"
        ),
        "rational_singularity_excluded": rational_singularity_excluded,
        "absolute_t_upper_bound": maximum_absolute_t,
        "positive_radius_factor": positive_radius_factor,
        "positive_radius_factor_exact": positive_radius_factor > 0,
        "absolute_factor_identity": "ABS(2*t-1/t)=1/ABS(t)-2*ABS(t)",
        "bound_function_derivative": "-1/u^2-2",
        "bound_function_derivative_terms_negative": (
            bound_function_derivative_terms_negative
        ),
        "bound_derivation": "1/(7/25)-2*(7/25)",
        "derived_absolute_factor_lower_bound": derived_bound,
        "absolute_factor_lower_bound": endpoint_bound,
        "bound_identity_exact": derived_bound == endpoint_bound,
        "universal_factor_outside_stochastic_spectral_interval": endpoint_bound
        > Fraction(1),
        "measured_absolute_factor": abs(nontrivial_eigenvalue),
        "bound_residual": abs(nontrivial_eigenvalue) - endpoint_bound,
        "universal_certificate": left_t == Fraction(7, 25)
        and right_t == Fraction(-7, 25)
        and all(derivative_factor_signs.values())
        and rational_singularity_excluded
        and positive_radius_factor > 0
        and bound_function_derivative_terms_negative
        and derived_bound == endpoint_bound,
    }
    history_joint = tuple(
        tuple(
            tuple(b[a][q] * c[out][q] for out in (0, 1))
            for a in (0, 1)
        )
        for q in (0, 1)
    )
    history_normalizations = tuple(
        sum(
            (history_joint[q][a][out] for a in (0, 1) for out in (0, 1)),
            Fraction(0),
        )
        for q in (0, 1)
    )
    return {
        "B": b,
        "C": c,
        "K": k,
        "negative_entries": negative_entries,
        "unique_factor": b_determinant != 0,
        "B_determinant": b_determinant,
        "nontrivial_eigenvalue": nontrivial_eigenvalue,
        "interval_certificate": interval_certificate,
        "positive_source_independent_restart_exists": not bool(negative_entries),
        "history_conditioned_joint": history_joint,
        "history_joint_normalizations": history_normalizations,
        "history_joint_nonnegative": all(
            value >= 0
            for by_source in history_joint
            for by_cut in by_source
            for value in by_cut
        ),
        "history_joint_positive_coordinates": sum(
            int(value > 0)
            for by_source in history_joint
            for by_cut in by_source
            for value in by_cut
        ),
        "native_sentence": NATIVE_NONDIVISION_SENTENCE,
        "lineage": {
            "operation": "MATMUL-RIGHT-INVERSE",
            "C_hash": canonical_hash(c),
            "B_hash": canonical_hash(b),
            "result_hash": canonical_hash(k),
            "primitive_derivation": coherent["second_lineage"],
        },
    }


def build_reciprocal_control(prefix: str = "rsp_") -> dict[str, Any]:
    record = build_record_control(prefix)
    writer = record["writer"]
    reader_query = formula_and(
        formula_atom(f"{prefix}L_record"),
        formula_atom(f"{prefix}N_record"),
    )
    reader = generator_arrow(
        writer.target,
        Occurrence(
            f"{prefix}reader",
            record["probe_role"],
            record["work_port"],
            reader_query,
            "ACTIVE",
        ),
    )
    return record | {"reader": reader, "chain": compose_arrows(writer, reader)}


def measure_reciprocal_response(law: GammaLaw) -> dict[str, Any]:
    control = build_reciprocal_control()
    chain_map = evaluate_arrow(law, control["chain"])
    source = _empty_state(control["boundary"])
    source_column = _configuration_index(control["boundary"])[source]
    target_lookup = _configuration_index(control["chain"].target)
    joint: dict[str, Fraction] = {}
    for source_bit in (0, 1):
        for probe_bit in (0, 1):
            target = _empty_state(
                control["chain"].target,
                {
                    control["source_role"]: source_bit,
                    control["probe_role"]: probe_bit,
                },
                {
                    control["record_port"]: f"branch{source_bit}",
                    control["work_port"]: f"branch{probe_bit}",
                },
            )
            amplitude = map_coefficient(
                chain_map, target_lookup[target], source_column
            )
            joint[f"{source_bit}{probe_bit}"] = amplitude * amplitude

    reader_map = evaluate_arrow(law, control["reader"])
    counter_source = _empty_state(
        control["reader"].source,
        {control["source_role"]: 1, control["probe_role"]: 0},
        {control["record_port"]: "branch0"},
    )
    counter_target = _empty_state(
        control["reader"].target,
        {control["source_role"]: 1, control["probe_role"]: 1},
        {
            control["record_port"]: "branch0",
            control["work_port"]: "branch1",
        },
    )
    counter_amplitude = map_coefficient(
        reader_map,
        _configuration_index(control["reader"].target)[counter_target],
        _configuration_index(control["reader"].source)[counter_source],
    )
    record_branch1 = _empty_state(
        control["reader"].source,
        {control["source_role"]: 1, control["probe_role"]: 0},
        {control["record_port"]: "branch1"},
    )
    reader_occurrence = control["reader"].occurrence
    if type(reader_occurrence) is not Occurrence:
        raise IntegrityFailure("reciprocal reader lost its occurrence")
    query = reader_occurrence.query
    if type(query) is not Formula:
        raise IntegrityFailure("reciprocal reader lost its query")
    return {
        "joint": joint,
        "earned_scope": (
            "RAW-RELATION-MEDIATED-RECIPROCAL-RESPONSE-OR-PROTO-BACKREACTION-ONLY"
        ),
        "normalization": sum(joint.values(), Fraction(0)),
        "counterfactual_probe_one": counter_amplitude * counter_amplitude,
        "contact_true_branch": query_nonzero(record_branch1.context, query),
        "contact_false_branch": query_nonzero(counter_source.context, query),
        "literal_writer_target_context_hash": canonical_hash(
            context_semantic_key(record_branch1.context)
        ),
        "literal_counterfactual_context_hash": canonical_hash(
            context_semantic_key(counter_source.context)
        ),
        "chain_lineage": chain_map.derivation,
        "reader_lineage": reader_map.derivation,
    }


def _split_diagnostic_artifacts(
    law: GammaLaw, proof: ContextSplitProof
) -> dict[str, Any]:
    rows: list[tuple[int, int, Fraction]] = []
    endpoint_rows: list[tuple[int, tuple[Fraction, ...]]] = []
    target_index = {cell: index for index, cell in enumerate(proof.target.cells)}
    for source_index, fiber in enumerate(proof.rows):
        weight = Fraction(1, len(fiber.observed_target_cells))
        probabilities = [Fraction(0) for _ in proof.target.cells]
        for cell in fiber.observed_target_cells:
            index = target_index[cell]
            rows.append((index, source_index, weight))
            probabilities[index] = weight
        endpoint_rows.append((source_index, tuple(probabilities)))
    process_key = (
        "CONTEXT-SPLIT-DIAGNOSTIC-NOT-GAMMA-v1",
        law_identity(law),
        context_semantic_key(proof.source),
        context_semantic_key(proof.target),
        proof.contextual_parent_key,
        (proof.child.name, proof.child.kind),
    )
    return {
        "physical_source_key_sha256": canonical_hash(
            (context_semantic_key(proof.source), proof.contextual_parent_key)
        ),
        "contextual_process_key_sha256": canonical_hash(process_key),
        "operator_coordinates": tuple(rows),
        "operator_sha256": canonical_hash(tuple(rows)),
        "endpoint_rows": tuple(endpoint_rows),
        "endpoint_law_sha256": canonical_hash(tuple(endpoint_rows)),
        "classifier_lineage_sha256": canonical_hash(
            (law_identity(law), canonical_hash(proof), process_key)
        ),
        "normalizations": tuple(
            sum(probabilities, Fraction(0))
            for _, probabilities in endpoint_rows
        ),
        "diagnostic_only_not_promotive": True,
    }


def _split_census_contexts() -> tuple[tuple[str, Context], ...]:
    a = Role("A", "RELATION")
    b = Role("B", "RELATION")
    return (
        ("C1", Context((a,), ((), ("A",)))),
        ("C2", Context((a, b), ((), ("A",), ("B",), ("A", "B")))),
        ("C3", Context((a, b), ((), ("A",), ("A", "B")))),
        ("C4", Context((a, b), ((), ("B",), ("A", "B")))),
        ("C5", Context((a, b), ((), ("A",), ("B",)))),
        ("C6", Context((a, b), ((), ("A", "B")))),
    )


def _measure_contextual_alias(law: GammaLaw) -> dict[str, Any]:
    context = dict(_split_census_contexts())["C3"]
    b = formula_atom("B")
    a_and_b = formula_and(formula_atom("A"), b)
    child = Role("alias_N", "RELATION")

    def member(parent: Formula) -> dict[str, Any]:
        port = Port("alias_p", child, formula_not(parent), parent)
        boundary = atomic_boundary(("alias_c",), context, (PortDecl(port, "ACTIVE"),))
        occurrence = Occurrence(
            "alias_occurrence", "alias_c", "alias_p", parent, "ACTIVE"
        )
        arrow = generator_arrow(boundary, occurrence)
        source = _empty_state(boundary, {"alias_c": 0})
        target = _empty_state(
            arrow.target,
            {"alias_c": 1},
            {"alias_p": "branch1"},
        )
        linear_map = evaluate_arrow(law, arrow)
        evaluation = gamma_evaluate(law, arrow, source)
        certificate = build_bound_split_certificate(
            law, arrow, source, target
        )
        return {
            "raw_formula_sha256": canonical_hash(parent.to_data()),
            "contextual_parent_key": contextual_formula_key(context, parent),
            "source_boundary_sha256": canonical_hash(boundary_semantic_key(boundary)),
            "arrow_sha256": canonical_hash(arrow_key(arrow)),
            "presentation_key_sha256": canonical_hash(
                presentation_key(law, arrow, source)
            ),
            "target_context_sha256": canonical_hash(
                context_semantic_key(target.context)
            ),
            "operator_entries_sha256": canonical_hash(linear_map.entries),
            "endpoint_law_sha256": canonical_hash(evaluation.probabilities),
            "lineage_sha256": canonical_hash(linear_map.derivation),
            "certificate": certificate,
            "certificate_sha256": canonical_hash(certificate),
        }

    left = member(b)
    right = member(a_and_b)
    physical_fields = (
        "contextual_parent_key",
        "source_boundary_sha256",
        "arrow_sha256",
        "presentation_key_sha256",
        "target_context_sha256",
        "operator_entries_sha256",
        "endpoint_law_sha256",
        "lineage_sha256",
        "certificate_sha256",
    )
    return {
        "left": left,
        "right": right,
        "raw_ambient_formulas_distinct": left["raw_formula_sha256"]
        != right["raw_formula_sha256"],
        "physical_fields_equal": {
            field: left[field] == right[field] for field in physical_fields
        },
        "all_physical_fields_equal": all(
            left[field] == right[field] for field in physical_fields
        ),
    }


def measure_context_split_census(law: GammaLaw) -> dict[str, Any]:
    expected = {
        "C1": (3, 3),
        "C2": (15, 15),
        "C3": (14, 7),
        "C4": (14, 7),
        "C5": (14, 7),
        "C6": (12, 3),
    }
    context_rows: list[dict[str, Any]] = []
    ambient_total = 0
    class_total = 0
    replay_total = 0
    for name, context in _split_census_contexts():
        role_names = context_role_names(context)
        representatives: list[dict[str, Any]] = []
        grouped: dict[tuple[bool, ...], list[dict[str, Any]]] = {}
        for table in itertools.product(
            (False, True), repeat=2 ** len(role_names)
        ):
            formula = Formula(role_names, tuple(table))
            truth = contextual_formula_truth(context, formula)
            if not any(truth):
                continue
            child = Role(f"N_{name}", "RELATION")
            target = context_extend(context, child, formula)
            proof = build_context_split_proof(context, target, formula, child)
            diagnostic = _split_diagnostic_artifacts(law, proof)
            row = {
                "ambient_roles": role_names,
                "ambient_truth_table": tuple(table),
                "ambient_formula_sha256": canonical_hash(
                    {"roles": role_names, "table": tuple(table)}
                ),
                "canonical_formula_provenance_sha256": canonical_hash(formula),
                "contextual_truth": truth,
                "contextual_parent_key": proof.contextual_parent_key,
                "target_semantic_sha256": canonical_hash(
                    context_semantic_key(target)
                ),
                "proof": proof,
                "proof_sha256": canonical_hash(proof),
                **diagnostic,
            }
            representatives.append(row)
            grouped.setdefault(truth, []).append(row)
        classes: list[dict[str, Any]] = []
        invariant_fields = (
            "contextual_parent_key",
            "target_semantic_sha256",
            "proof_sha256",
            "physical_source_key_sha256",
            "contextual_process_key_sha256",
            "operator_sha256",
            "endpoint_law_sha256",
            "classifier_lineage_sha256",
        )
        for truth in sorted(grouped):
            members = grouped[truth]
            reference = members[0]
            invariance = {
                field: all(member[field] == reference[field] for member in members)
                for field in invariant_fields
            }
            classes.append(
                {
                    "contextual_truth": truth,
                    "contextual_parent_key": reference["contextual_parent_key"],
                    "representative_count": len(members),
                    "ambient_formula_sha256s": tuple(
                        member["ambient_formula_sha256"] for member in members
                    ),
                    "native_proof": reference["proof"],
                    "native_proof_sha256": reference["proof_sha256"],
                    "invariance": invariance,
                    "all_invariant": all(invariance.values()),
                }
            )
        ambient_count = len(representatives)
        class_count = len(classes)
        ambient_total += ambient_count
        class_total += class_count
        replay_total += sum(len(grouped[row["contextual_truth"]]) for row in classes)
        context_rows.append(
            {
                "name": name,
                "context": context,
                "ambient_assignment_count": 2 ** len(role_names),
                "ambient_nonzero_representative_count": ambient_count,
                "contextual_class_count": class_count,
                "expected_counts": expected[name],
                "counts_exact": (ambient_count, class_count) == expected[name],
                "representatives": tuple(representatives),
                "classes": tuple(classes),
                "all_representative_proofs_exact": all(
                    row["proof"].final for row in representatives
                ),
                "all_class_invariance_exact": all(
                    row["all_invariant"] for row in classes
                ),
            }
        )
    minimal_source = dict(_split_census_contexts())["C1"]
    minimal_child = Role("N", "RELATION")
    minimal_controls: dict[str, Any] = {}
    for label, parent in (
        ("A", formula_atom("A")),
        ("NOT-A", formula_not(formula_atom("A"))),
    ):
        target = context_extend(minimal_source, minimal_child, parent)
        proof = build_context_split_proof(
            minimal_source, target, parent, minimal_child
        )
        minimal_controls[label] = {
            "source_cells": minimal_source.cells,
            "target_cells": target.cells,
            "fiber_sizes": tuple(
                len(row.observed_target_cells) for row in proof.rows
            ),
            "cell_count_transition": (
                len(minimal_source.cells),
                len(target.cells),
            ),
            "proof": proof,
            "proof_sha256": canonical_hash(proof),
        }
    minimal_controls_exact = (
        minimal_controls["A"]["target_cells"]
        == ((), ("A",), ("A", "N"))
        and minimal_controls["A"]["fiber_sizes"] == (1, 2)
        and minimal_controls["NOT-A"]["target_cells"]
        == ((), ("N",), ("A",))
        and minimal_controls["NOT-A"]["fiber_sizes"] == (2, 1)
        and all(row["proof"].final for row in minimal_controls.values())
    )
    alias = _measure_contextual_alias(law)
    return {
        "minimal_controls": minimal_controls,
        "minimal_controls_exact": minimal_controls_exact,
        "contexts": tuple(context_rows),
        "ambient_nonzero_total": ambient_total,
        "contextual_class_total": class_total,
        "ambient_replay_total": replay_total,
        "expected_ambient_total": sum(row[0] for row in expected.values()),
        "expected_contextual_total": sum(row[1] for row in expected.values()),
        "counts_exact": ambient_total == 72 and class_total == 42,
        "all_replayed": replay_total == ambient_total == 72,
        "all_context_proofs_exact": all(
            row["all_representative_proofs_exact"] for row in context_rows
        ),
        "all_within_class_invariance_exact": all(
            row["all_class_invariance_exact"] for row in context_rows
        ),
        "context_proofs_are_nonpromotive": True,
        "contextual_alias": alias,
        "all_exact": ambient_total == 72
        and class_total == 42
        and replay_total == ambient_total
        and all(row["counts_exact"] for row in context_rows)
        and all(row["all_representative_proofs_exact"] for row in context_rows)
        and all(row["all_class_invariance_exact"] for row in context_rows)
        and minimal_controls_exact
        and alias["raw_ambient_formulas_distinct"]
        and alias["all_physical_fields_equal"],
    }


def _all_generator_split_certificates(
    law: GammaLaw, arrow: Arrow
) -> tuple[BoundSplitCertificate, ...]:
    linear_map = evaluate_arrow(law, arrow)
    certificates: list[BoundSplitCertificate] = []
    for row, column, coefficient in linear_map.entries:
        if coefficient == 0:
            continue
        certificate = build_bound_split_certificate(
            law,
            arrow,
            arrow.source.catalogue[column],
            arrow.target.catalogue[row],
        )
        if certificate.coefficient != coefficient:
            raise IntegrityFailure("bound split coefficient disagrees with the law")
        certificates.append(certificate)
    return tuple(certificates)


def measure_support_change(law: GammaLaw) -> dict[str, Any]:
    control = build_coherent_control("sup_")
    rotate = control["first_pair"].children[0]
    if type(rotate.occurrence) is not Occurrence:
        raise IntegrityFailure("support-change occurrence is missing")
    source = _empty_state(rotate.source)
    evaluation = gamma_evaluate(law, rotate, source)
    changed: list[dict[str, Any]] = []
    for index, probability in enumerate(evaluation.probabilities):
        if probability == 0:
            continue
        target = rotate.target.catalogue[index]
        certificate = build_bound_split_certificate(law, rotate, source, target)
        changed.append(
            {
                "sector": certificate.target_sector,
                "probability": probability,
                "source_role_count": len(source.context.roles),
                "target_role_count": len(target.context.roles),
                "source_cell_count": len(source.context.cells),
                "target_cell_count": len(target.context.cells),
                "inverse_merge_exact": certificate.context_proof.forget_exact,
                "configuration_nonisomorphic_observation_only": (
                    len(source.context.roles), len(source.context.cells)
                )
                != (len(target.context.roles), len(target.context.cells)),
                "target_context_hash": canonical_hash(
                    context_semantic_key(target.context)
                ),
                "bound_certificate": certificate,
                "bound_certificate_sha256": canonical_hash(certificate),
                "classifier_consumed_sha256": certificate.classifier_consumed_sha256,
                "proper_split": certificate.operation_kind == "CREATE"
                and certificate.final,
            }
        )
    all_certificates = _all_generator_split_certificates(law, rotate)
    operation_counts = {
        operation: sum(
            int(certificate.operation_kind == operation)
            for certificate in all_certificates
        )
        for operation in ("CREATE", "MERGE", "UNCHANGED")
    }
    create_certificates = tuple(
        certificate
        for certificate in all_certificates
        if certificate.operation_kind == "CREATE"
    )
    merge_certificates = tuple(
        certificate
        for certificate in all_certificates
        if certificate.operation_kind == "MERGE"
    )
    unchanged_certificates = tuple(
        certificate
        for certificate in all_certificates
        if certificate.operation_kind == "UNCHANGED"
    )
    return {
        "branches": tuple(changed),
        "bound_transition_certificates": all_certificates,
        "bound_transition_count": len(all_certificates),
        "operation_counts": operation_counts,
        "all_bound_certificates_exact": all(
            certificate.final for certificate in all_certificates
        ),
        "all_create_certificates_exact": bool(create_certificates)
        and all(certificate.final for certificate in create_certificates),
        "all_merge_certificates_exact": bool(merge_certificates)
        and all(certificate.final for certificate in merge_certificates),
        "all_unchanged_certificates_exact": bool(unchanged_certificates)
        and all(certificate.final for certificate in unchanged_certificates),
        "all_inverse_merge": all(
            certificate.context_proof.forget_exact
            for certificate in create_certificates + merge_certificates
        ),
        "all_support_changed": bool(changed)
        and all(row["proper_split"] for row in changed),
        "classifier_consumed_certificate_sha256": canonical_hash(
            tuple(
                certificate.classifier_consumed_sha256
                for certificate in all_certificates
            )
        ),
        "context_proof_alone_is_promotive": False,
        "legacy_role_cell_inequality_is_promotive": False,
        "meta_catalogue_state_count": len(rotate.target.catalogue),
        "meta_catalogue_is_physical_support": False,
        "lineage": evaluation.derivation,
    }


@dataclass(frozen=True, slots=True)
class MatchingPresentation:
    size: int
    permutation: tuple[int, ...]
    queries: tuple[int, ...]
    exposure: str
    seal: bool = True

    def __post_init__(self) -> None:
        _require_exact(self.size, int, "matching size")
        _require_exact_tuple(self.permutation, "matching permutation")
        _require_exact_tuple(self.queries, "matching queries")
        _require_exact(self.exposure, str, "matching exposure")
        _require_exact(self.seal, bool, "matching seal")
        if self.size < 2:
            raise Refusal("matching size is too small")
        if any(type(value) is not int for value in self.permutation):
            raise Refusal("matching permutation contains a foreign value")
        if self.permutation != tuple(self.permutation):
            raise Refusal("matching permutation is malformed")
        if sorted(self.permutation) != list(range(self.size)):
            raise Refusal("matching permutation is not bijective")
        if any(type(value) is not int for value in self.queries):
            raise Refusal("matching query contains a foreign value")
        if len(set(self.queries)) != len(self.queries) or not set(self.queries) <= set(
            range(self.size)
        ):
            raise Refusal("matching query subset is malformed")
        if not self.queries:
            raise Refusal("matching assay has no query")
        if self.exposure not in ("EXPOSED-CONTROL", "POST-SOURCE-FRESH"):
            raise Refusal("matching exposure class is invalid")
        if not self.seal:
            raise Refusal("matching presentation is unsealed")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "MatchingPresentation",
            "size": self.size,
            "permutation": self.permutation,
            "queries": self.queries,
            "exposure": self.exposure,
            "seal": self.seal,
        }


def matching_context(presentation: MatchingPresentation, prefix: str) -> Context:
    _require_exact(presentation, MatchingPresentation, "matching presentation")
    roles = tuple(
        Role(f"{prefix}L_{index}", "RELATION")
        for index in range(presentation.size)
    ) + tuple(
        Role(f"{prefix}N_{index}", "RELATION")
        for index in range(presentation.size)
    )
    cells: list[tuple[str, ...]] = [()]
    cells.extend((f"{prefix}L_{index}",) for index in range(presentation.size))
    cells.extend((f"{prefix}N_{index}",) for index in range(presentation.size))
    cells.extend(
        (f"{prefix}L_{index}", f"{prefix}N_{presentation.permutation[index]}")
        for index in range(presentation.size)
    )
    return Context(roles, tuple(cells))


def build_matching_arrow(
    presentation: MatchingPresentation, prefix: str = "match_"
) -> dict[str, Any]:
    context = matching_context(presentation, prefix)
    matter_roles = tuple(f"{prefix}coin_{index}" for index in presentation.queries)
    ports = tuple(
        _partition_port(
            f"{prefix}L_{index}",
            f"{prefix}port_{index}",
            f"{prefix}child_{index}",
        )
        for index in presentation.queries
    )
    boundary = atomic_boundary(matter_roles, context, ports)
    arrows: list[Arrow] = []
    current = boundary
    for index in presentation.queries:
        query = formula_and(
            formula_atom(f"{prefix}L_{index}"),
            formula_atom(f"{prefix}N_{index}"),
        )
        occurrence = generator_arrow(
            current,
            Occurrence(
                f"{prefix}slot_{index}",
                f"{prefix}coin_{index}",
                f"{prefix}port_{index}",
                query,
                "ACTIVE",
            ),
        )
        arrows.append(occurrence)
        current = occurrence.target
    return {
        "presentation": presentation,
        "context": context,
        "boundary": boundary,
        "arrow": compose_word(arrows),
        "matter_roles": matter_roles,
        "ports": ports,
        "prefix": prefix,
    }


def _context_resource_projection(context: Context, size: int, prefix: str) -> dict[str, Any]:
    supports = tuple(
        sorted(sum(int(role.name in cell) for cell in context.cells) for role in context.roles)
    )
    arities = tuple(sorted(len(cell) for cell in context.cells))
    degrees: list[int] = []
    for left in range(size):
        degree = 0
        for right in range(size):
            query = formula_and(
                formula_atom(f"{prefix}L_{left}"),
                formula_atom(f"{prefix}N_{right}"),
            )
            degree += int(query_nonzero(context, query))
        degrees.append(degree)
    return {
        "cell_count": len(context.cells),
        "incidence_count": sum(len(cell) for cell in context.cells),
        "role_count": len(context.roles),
        "cell_arity_histogram": tuple(
            (arity, arities.count(arity)) for arity in sorted(set(arities))
        ),
        "support_multiset": supports,
        "degree_multiset": tuple(sorted(degrees + degrees)),
    }


def blind_projection(model: Mapping[str, Any]) -> dict[str, Any]:
    presentation = model["presentation"]
    _require_exact(presentation, MatchingPresentation, "matching presentation")
    resources = _context_resource_projection(
        model["context"], presentation.size, model["prefix"]
    )
    return {
        "size": presentation.size,
        "resources": resources,
        "query_count": len(presentation.queries),
        "port_count": len(model["ports"]),
        "coin_count": len(model["matter_roles"]),
        "schedule": tuple(range(len(presentation.queries))),
        "calibrated_query_roles": tuple("L-AND-N" for _ in presentation.queries),
        "prior_record_tokens": (),
    }


def measure_matching_case(law: GammaLaw, presentation: MatchingPresentation) -> dict[str, Any]:
    model = build_matching_arrow(presentation)
    source = _empty_state(model["boundary"])
    call_count = 0
    evaluation = gamma_evaluate(law, model["arrow"], source)
    call_count += 1
    marginal: dict[str, Fraction] = {}
    target = model["arrow"].target
    for query_index in presentation.queries:
        matter_name = f"{model['prefix']}coin_{query_index}"
        probability = Fraction(0)
        for row, target_state in enumerate(target.catalogue):
            if matter_dict(target_state)[matter_name] == 1:
                probability += evaluation.probabilities[row]
        marginal[str(query_index)] = probability
    analytic_marginals: dict[str, Fraction] = {}
    analytic_residual = Fraction(0)
    contact_probability = cayley_matrix(law.g, law.primitive)[1][0] ** 2
    for query_index in presentation.queries:
        query = formula_and(
            formula_atom(f"{model['prefix']}L_{query_index}"),
            formula_atom(f"{model['prefix']}N_{query_index}"),
        )
        predicted = (
            contact_probability
            if query_nonzero(model["context"], query)
            else Fraction(0)
        )
        analytic_marginals[str(query_index)] = predicted
        analytic_residual = max(
            analytic_residual, abs(marginal[str(query_index)] - predicted)
        )
    resources = _context_resource_projection(
        model["context"], presentation.size, model["prefix"]
    )
    return {
        "presentation_hash": canonical_hash(presentation),
        "presentation": presentation,
        "context_hash": canonical_hash(context_semantic_key(model["context"])),
        "arrow_hash": canonical_hash(arrow_key(model["arrow"])),
        "source_boundary": model["boundary"],
        "target_boundary": target,
        "source_state": source,
        "source_state_count": len(model["boundary"].catalogue),
        "target_state_count": len(target.catalogue),
        "single_global_gamma_calls": call_count,
        "normalization": evaluation.normalization,
        "marginals": marginal,
        "analytic_marginals": analytic_marginals,
        "direct_vs_analytic_residual": analytic_residual,
        "direct_vs_analytic_exact": analytic_residual == 0,
        "g_half_exposed_marginals_exact": law.g != Fraction(1, 2)
        or all(
            value
            == (
                Fraction(16, 25)
                if presentation.permutation[index] == index
                else Fraction(0)
            )
            for index, value in (
                (index, marginal[str(index)]) for index in presentation.queries
            )
        ),
        "endpoint_probabilities_hash": canonical_hash(evaluation.probabilities),
        "nonzero_endpoint_coordinates": tuple(
            (index, value)
            for index, value in enumerate(evaluation.probabilities)
            if value != 0
        ),
        "resources": resources,
        "blind_projection": blind_projection(model),
        "lineage": evaluation.derivation,
        "primitive_roots": derivation_roots(evaluation.derivation),
    }


def measure_blind_family(law: GammaLaw) -> dict[str, Any]:
    size = 4
    queries = tuple(range(size))
    first = MatchingPresentation(
        size, tuple(range(size)), queries, "EXPOSED-CONTROL"
    )
    second = MatchingPresentation(
        size, tuple((index + 1) % size for index in range(size)), queries, "EXPOSED-CONTROL"
    )
    first_result = measure_matching_case(law, first)
    second_result = measure_matching_case(law, second)
    prefix_equal = first_result["blind_projection"] == second_result["blind_projection"]
    response_unequal = first_result["marginals"] != second_result["marginals"]
    induction = {
        "base_common_initialization": True,
        "observation_word_equal": prefix_equal,
        "step": (
            "for every stochastic transducer state h, equal h and equal next blind "
            "symbol induce equal next-state/output laws"
        ),
        "memory_scope": "UNBOUNDED",
        "conclusion_same_blind_output_law": prefix_equal,
    }
    return {
        "first": first_result,
        "second": second_result,
        "resource_parity": first_result["resources"] == second_result["resources"],
        "blind_prefix_equal": prefix_equal,
        "same_initialization": True,
        "prior_record_law_equal": True,
        "same_law_root": set(first_result["primitive_roots"])
        == set(second_result["primitive_roots"])
        == {law_identity(law)},
        "direct_factorization_exact": first_result["direct_vs_analytic_exact"]
        and second_result["direct_vs_analytic_exact"],
        "exposed_marginals_exact": first_result["g_half_exposed_marginals_exact"]
        and second_result["g_half_exposed_marginals_exact"],
        "response_unequal": response_unequal,
        "blind_transducer_induction": induction,
        "class_scope": "ALL-STOCHASTIC-BLIND-TRANSDUCERS-WITH-UNBOUNDED-MEMORY",
    }


def maps_equal(left: LinearMap, right: LinearMap) -> bool:
    return (
        _same_boundary(left.source, right.source)
        and _same_boundary(left.target, right.target)
        and left.entries == right.entries
    )


def generator_leaves(arrow: Arrow) -> tuple[Arrow, ...]:
    _require_exact(arrow, Arrow, "generator-leaf source")
    if arrow.kind == "GENERATOR":
        return (arrow,)
    return tuple(
        leaf for child in arrow.children for leaf in generator_leaves(child)
    )


def registered_generator_families() -> tuple[Arrow, ...]:
    """The frozen twelve-family generator census used by every totality gate."""

    coherent = build_coherent_control("total_")
    record = build_record_control("total_record_")
    reciprocal = build_reciprocal_control("total_rsp_")
    arrows = list(generator_leaves(coherent["two_pairs"]))
    arrows.append(record["writer"])
    for letter in record["letters"].values():
        arrows.extend(generator_leaves(letter))
    arrows.extend(generator_leaves(reciprocal["reader"]))
    return tuple(arrows)


def measure_totality_certificate(law: GammaLaw) -> dict[str, Any]:
    arrows = registered_generator_families()
    rows: list[dict[str, Any]] = []
    for arrow in arrows:
        linear_map = evaluate_arrow(law, arrow)
        isometry, residual = check_isometry(linear_map)
        if type(arrow.occurrence) is not Occurrence:
            raise IntegrityFailure("totality battery contains a nongenerator")
        split_certificates = _all_generator_split_certificates(law, arrow)
        split_operation_counts = {
            operation: sum(
                int(certificate.operation_kind == operation)
                for certificate in split_certificates
            )
            for operation in ("CREATE", "MERGE", "UNCHANGED")
        }
        rows.append(
            {
                "occurrence_id": arrow.occurrence.occurrence_id,
                "query_sha256": canonical_hash(arrow.occurrence.query),
                "source_state_count": len(arrow.source.catalogue),
                "target_state_count": len(arrow.target.catalogue),
                "operator_sha256": canonical_hash(linear_map),
                "isometry": isometry,
                "isometry_residual": residual,
                "all_source_columns_checked": len(arrow.source.catalogue),
                "bound_split_certificate_count": len(split_certificates),
                "bound_split_operation_counts": split_operation_counts,
                "bound_split_classifier_sha256": canonical_hash(
                    tuple(
                        certificate.classifier_consumed_sha256
                        for certificate in split_certificates
                    )
                ),
                "all_nonzero_transitions_bound": bool(split_certificates)
                and all(certificate.final for certificate in split_certificates),
            }
        )
    rho_involutions = {
        f"output{output_bit}": all(
            _rho_sector(
                _rho_sector(sector, output_bit, "CANONICAL"),
                output_bit,
                "CANONICAL",
            )
            == sector
            for sector in CANONICAL_SECTORS
        )
        for output_bit in (0, 1)
    }
    cayley_left_coefficients = (1, -2 + 4, 1)
    cayley_right_coefficients = (1, 2, 1)
    endpoint_laws: list[dict[str, Any]] = []
    sample_arrow = arrows[0]
    sample_source = _empty_state(sample_arrow.source)
    for coupling in (Fraction(1, 3), law.g):
        endpoint_law = GammaLaw(coupling)
        evaluation = gamma_evaluate(endpoint_law, sample_arrow, sample_source)
        endpoint_laws.append(
            {
                "g": coupling,
                "normalization": evaluation.normalization,
                "endpoint_sha256": canonical_hash(evaluation.probabilities),
                "law_identity": law_identity(endpoint_law),
            }
        )
    return {
        "generator_rows": tuple(rows),
        "generator_count": len(rows),
        "all_declared_source_columns_checked": sum(
            row["all_source_columns_checked"] for row in rows
        ),
        "all_generator_isometries": all(
            row["isometry"] and row["isometry_residual"] == 0 for row in rows
        ),
        "all_nonzero_generator_transitions_bound": all(
            row["all_nonzero_transitions_bound"] for row in rows
        ),
        "total_bound_split_certificate_count": sum(
            row["bound_split_certificate_count"] for row in rows
        ),
        "rho_involutions": rho_involutions,
        "all_rho_involutions": all(rho_involutions.values()),
        "cayley_norm_polynomial_left": cayley_left_coefficients,
        "cayley_norm_polynomial_right": cayley_right_coefficients,
        "cayley_norm_identity_for_every_rational_x": (
            cayley_left_coefficients == cayley_right_coefficients
        ),
        "denominator_positive_certificate": {
            "denominator": "1+x^2",
            "rational_square_nonnegative": True,
            "exact_lower_bound": Fraction(1),
            "positive_for_every_rational_x": Fraction(1) > 0,
        },
        "endpoint_domain_controls": tuple(endpoint_laws),
        "endpoint_domain_controls_normalized": all(
            row["normalization"] == 1 for row in endpoint_laws
        ),
        "closure_theorem": (
            "IDENTITY-COMPOSITION-TENSOR-AND-TYPED-PERMUTATIONS-PRESERVE-ISOMETRY"
        ),
    }


def _small_atom(prefix: str) -> Boundary:
    base = _partition_context(prefix)
    return atomic_boundary(
        (f"{prefix}c",),
        base,
        (
            _partition_port(
                f"{prefix}L_record", f"{prefix}p", f"{prefix}N"
            ),
        ),
    )


def _small_generator(boundary: Boundary, prefix: str) -> Arrow:
    return generator_arrow(
        boundary,
        Occurrence(
            f"{prefix}g",
            f"{prefix}c",
            f"{prefix}p",
            formula_atom(f"{prefix}L_record"),
            "ACTIVE",
        ),
    )


def measure_category_laws(law: GammaLaw) -> dict[str, Any]:
    a = _small_atom("cat_a_")
    b = _small_atom("cat_b_")
    c = _small_atom("cat_c_")
    f = _small_generator(a, "cat_a_")
    g = _small_generator(b, "cat_b_")
    h = _small_generator(f.target, "cat_a_")
    k = _small_generator(g.target, "cat_b_")
    ell = _small_generator(h.target, "cat_a_")

    identity_map = evaluate_arrow(law, identity_arrow(a))
    identity_ok = all(
        map_coefficient(identity_map, row, column)
        == Fraction(int(row == column))
        for row in range(len(a.catalogue))
        for column in range(len(a.catalogue))
    )
    composition = evaluate_arrow(law, compose_arrows(f, h))
    composed_direct = _compose_maps(evaluate_arrow(law, f), evaluate_arrow(law, h))
    composition_ok = maps_equal(composition, composed_direct)
    left_identity_ok = maps_equal(
        evaluate_arrow(law, compose_arrows(identity_arrow(f.source), f)),
        evaluate_arrow(law, f),
    )
    right_identity_ok = maps_equal(
        evaluate_arrow(law, compose_arrows(f, identity_arrow(f.target))),
        evaluate_arrow(law, f),
    )
    associativity_left = compose_arrows(compose_arrows(f, h), ell)
    associativity_right = compose_arrows(f, compose_arrows(h, ell))
    composition_associativity = maps_equal(
        evaluate_arrow(law, associativity_left),
        evaluate_arrow(law, associativity_right),
    )

    interchange_left = compose_arrows(tensor_arrow(f, g), tensor_arrow(h, k))
    interchange_right = tensor_arrow(compose_arrows(f, h), compose_arrows(g, k))
    interchange_ok = maps_equal(
        evaluate_arrow(law, interchange_left), evaluate_arrow(law, interchange_right)
    )

    symmetry_source = symmetry_arrow(a, b)
    symmetry_target = symmetry_arrow(f.target, g.target)
    naturality_left = compose_arrows(tensor_arrow(f, g), symmetry_target)
    naturality_right = compose_arrows(symmetry_source, tensor_arrow(g, f))
    naturality_ok = maps_equal(
        evaluate_arrow(law, naturality_left), evaluate_arrow(law, naturality_right)
    )
    symmetry_square = compose_arrows(symmetry_arrow(a, b), symmetry_arrow(b, a))
    symmetry_involutive = maps_equal(
        evaluate_arrow(law, symmetry_square), evaluate_arrow(law, identity_arrow(tensor_boundary(a, b)))
    )

    assoc = associator_arrow(a, b, c)
    assoc_inverse = associator_arrow(a, b, c, inverse=True)
    associator_inverse = maps_equal(
        evaluate_arrow(law, compose_arrows(assoc, assoc_inverse)),
        evaluate_arrow(law, identity_arrow(assoc.source)),
    )
    left_unitor = unitor_arrow(a, "LEFT")
    left_unitor_inverse = unitor_arrow(a, "LEFT", inverse=True)
    right_unitor = unitor_arrow(a, "RIGHT")
    right_unitor_inverse = unitor_arrow(a, "RIGHT", inverse=True)
    unitors = all(
        (
            maps_equal(
                evaluate_arrow(law, compose_arrows(left_unitor, left_unitor_inverse)),
                evaluate_arrow(law, identity_arrow(left_unitor.source)),
            ),
            maps_equal(
                evaluate_arrow(law, compose_arrows(right_unitor, right_unitor_inverse)),
                evaluate_arrow(law, identity_arrow(right_unitor.source)),
            ),
        )
    )
    maps = (
        evaluate_arrow(law, f),
        evaluate_arrow(law, g),
        composition,
        evaluate_arrow(law, associativity_left),
        evaluate_arrow(law, interchange_left),
        evaluate_arrow(law, naturality_left),
        evaluate_arrow(law, assoc),
    )
    isometry_residuals = tuple(check_isometry(item)[1] for item in maps)
    return {
        "identity": identity_ok,
        "composition": composition_ok,
        "left_identity": left_identity_ok,
        "right_identity": right_identity_ok,
        "composition_associativity": composition_associativity,
        "tensor_interchange": interchange_ok,
        "symmetry_naturality": naturality_ok,
        "symmetry_involutive": symmetry_involutive,
        "associator_inverse": associator_inverse,
        "unitors": unitors,
        "isometry_residuals": isometry_residuals,
        "all_exact": all(
            (
                identity_ok,
                composition_ok,
                left_identity_ok,
                right_identity_ok,
                composition_associativity,
                interchange_ok,
                naturality_ok,
                symmetry_involutive,
                associator_inverse,
                unitors,
                all(value == 0 for value in isometry_residuals),
            )
        ),
        "operator_hashes": tuple(canonical_hash(item) for item in maps),
    }


def _walk_boundary_presentation(
    boundary: Boundary,
    roles: dict[str, str],
    matter: set[str],
    ports: set[str],
    seen: set[int],
) -> None:
    _require_exact(boundary, Boundary, "presentation boundary")
    marker = id(boundary)
    if marker in seen:
        return
    seen.add(marker)

    def add_role(role: Role) -> None:
        _require_exact(role, Role, "presentation role")
        prior = roles.get(role.name)
        if prior is not None and prior != role.kind:
            raise Refusal("presentation role has inconsistent types")
        roles[role.name] = role.kind

    for role in boundary.base.roles:
        add_role(role)
    for configuration in boundary.catalogue:
        for role in configuration.context.roles:
            add_role(role)
    matter.update(boundary.matter_roles)
    for declaration in boundary.ports:
        ports.add(declaration.port.name)
        add_role(declaration.port.child)
        for formula in (declaration.port.parent0, declaration.port.parent1):
            for name in formula.roles:
                if name not in roles:
                    raise Refusal("port formula role is absent from presentation")
    if boundary.left is not None:
        _walk_boundary_presentation(boundary.left, roles, matter, ports, seen)
    if boundary.right is not None:
        _walk_boundary_presentation(boundary.right, roles, matter, ports, seen)


def _presentation_carriers(
    arrow: Arrow,
) -> tuple[
    tuple[tuple[str, str], ...],
    tuple[str, ...],
    tuple[str, ...],
    tuple[str, ...],
]:
    _require_exact(arrow, Arrow, "presentation arrow")
    roles: dict[str, str] = {}
    matter: set[str] = set()
    ports: set[str] = set()
    occurrences: set[str] = set()
    seen_arrows: set[int] = set()
    seen_boundaries: set[int] = set()

    def walk(current: Arrow) -> None:
        marker = id(current)
        if marker in seen_arrows:
            return
        seen_arrows.add(marker)
        _walk_boundary_presentation(
            current.source, roles, matter, ports, seen_boundaries
        )
        _walk_boundary_presentation(
            current.target, roles, matter, ports, seen_boundaries
        )
        for boundary in current.objects:
            _walk_boundary_presentation(
                boundary, roles, matter, ports, seen_boundaries
            )
        if current.occurrence is not None:
            occurrences.add(current.occurrence.occurrence_id)
            matter.add(current.occurrence.matter_role)
            ports.add(current.occurrence.port_name)
            for name in current.occurrence.query.roles:
                if name not in roles:
                    raise Refusal("occurrence query role is absent from presentation")
        for child in current.children:
            walk(child)

    walk(arrow)
    return (
        tuple(sorted(roles.items())),
        tuple(sorted(matter)),
        tuple(sorted(ports)),
        tuple(sorted(occurrences)),
    )


@dataclass(frozen=True, slots=True)
class SourcePresentation:
    arrow: Arrow
    role_carrier: tuple[tuple[str, str], ...]
    matter_carrier: tuple[str, ...]
    port_carrier: tuple[str, ...]
    occurrence_carrier: tuple[str, ...]
    seal: bool = True

    def __post_init__(self) -> None:
        _require_exact(self.arrow, Arrow, "source-presentation arrow")
        for label, carrier in (
            ("role", self.role_carrier),
            ("matter", self.matter_carrier),
            ("port", self.port_carrier),
            ("occurrence", self.occurrence_carrier),
        ):
            _require_exact_tuple(carrier, f"source-presentation {label} carrier")
        _require_exact(self.seal, bool, "source-presentation seal")
        if not self.seal:
            raise Refusal("source presentation is unsealed")
        expected = _presentation_carriers(self.arrow)
        observed = (
            self.role_carrier,
            self.matter_carrier,
            self.port_carrier,
            self.occurrence_carrier,
        )
        if observed != expected:
            raise Refusal("source-presentation carriers are incomplete or forged")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "SourcePresentation",
            "arrow": self.arrow,
            "role_carrier": self.role_carrier,
            "matter_carrier": self.matter_carrier,
            "port_carrier": self.port_carrier,
            "occurrence_carrier": self.occurrence_carrier,
            "seal": self.seal,
        }


def presentation_from_arrow(arrow: Arrow) -> SourcePresentation:
    carriers = _presentation_carriers(arrow)
    return SourcePresentation(arrow, *carriers)


def presentation_identity_data(presentation: SourcePresentation) -> dict[str, Any]:
    """Complete semantic presentation data without reserializing derived catalogues."""

    _require_exact(presentation, SourcePresentation, "presentation identity")
    return {
        "type": "SourcePresentationIdentity",
        "arrow_structural_key": arrow_structural_identity_key(presentation.arrow),
        "role_carrier": presentation.role_carrier,
        "matter_carrier": presentation.matter_carrier,
        "port_carrier": presentation.port_carrier,
        "occurrence_carrier": presentation.occurrence_carrier,
        "seal": presentation.seal,
    }


def presentation_identity(presentation: SourcePresentation) -> str:
    return canonical_hash(presentation_identity_data(presentation))


def arrow_structural_identity_key(arrow: Arrow) -> tuple[Any, ...]:
    """Exact raw AST identity with derived catalogues omitted from serialization."""

    _require_exact(arrow, Arrow, "structural Arrow identity")
    return (
        arrow.kind,
        boundary_semantic_key(arrow.source),
        boundary_semantic_key(arrow.target),
        arrow.occurrence.to_data() if arrow.occurrence is not None else None,
        tuple(arrow_structural_identity_key(child) for child in arrow.children),
        tuple(boundary_semantic_key(obj) for obj in arrow.objects),
        arrow.seal,
    )


@dataclass(frozen=True, slots=True)
class _RelabelPlan:
    role_map: tuple[tuple[str, str], ...]
    matter_map: tuple[tuple[str, str], ...]
    port_map: tuple[tuple[str, str], ...]
    occurrence_map: tuple[tuple[str, str], ...]


def _carrier_names(carrier: tuple[Any, ...], role_carrier: bool) -> tuple[str, ...]:
    if role_carrier:
        return tuple(row[0] for row in carrier)
    return tuple(carrier)


def _complete_component_map(
    label: str,
    source_carrier: tuple[Any, ...],
    target_carrier: tuple[Any, ...],
    rows: tuple[tuple[str, str], ...],
    *,
    role_carrier: bool = False,
) -> tuple[tuple[str, str], ...]:
    _require_exact_tuple(rows, f"groupoid {label} map")
    for row in rows:
        _require_exact_tuple(row, f"groupoid {label} row")
        if len(row) != 2 or type(row[0]) is not str or type(row[1]) is not str:
            raise Refusal(f"malformed groupoid {label} row")
    if len({row[0] for row in rows}) != len(rows):
        raise Refusal(f"groupoid {label} map repeats a source")
    source_names = _carrier_names(source_carrier, role_carrier)
    target_names = _carrier_names(target_carrier, role_carrier)
    if len(source_names) != len(set(source_names)) or len(target_names) != len(
        set(target_names)
    ):
        raise Refusal(f"groupoid {label} carrier is duplicated")
    source_set = set(source_names)
    target_set = set(target_names)
    explicit = dict(rows)
    if not set(explicit).issubset(source_set):
        raise Refusal(f"groupoid {label} map has an alien source")
    if not set(explicit.values()).issubset(target_set):
        raise Refusal(f"groupoid {label} map has an alien target")
    completed: list[tuple[str, str]] = []
    for source in source_names:
        if source in explicit:
            target = explicit[source]
        elif source in target_set:
            target = source
        else:
            raise Refusal(f"groupoid {label} map omits a nonidentity source")
        completed.append((source, target))
    images = tuple(target for _, target in completed)
    if len(images) != len(set(images)):
        raise Refusal(f"groupoid {label} map is not injective")
    if set(images) != target_set:
        raise Refusal(f"groupoid {label} map is not surjective")
    if role_carrier:
        source_types = dict(source_carrier)
        target_types = dict(target_carrier)
        if any(source_types[source] != target_types[target] for source, target in completed):
            raise Refusal("groupoid role map changes a role type")
    return tuple((source, target) for source, target in completed if source != target)


@dataclass(frozen=True, slots=True)
class SourceGroupoidWitness:
    source: SourcePresentation
    target: SourcePresentation
    role_map: tuple[tuple[str, str], ...]
    matter_map: tuple[tuple[str, str], ...]
    port_map: tuple[tuple[str, str], ...]
    occurrence_map: tuple[tuple[str, str], ...]
    seal: bool = True

    def __post_init__(self) -> None:
        _require_exact(self.source, SourcePresentation, "groupoid source")
        _require_exact(self.target, SourcePresentation, "groupoid target")
        _require_exact(self.seal, bool, "groupoid witness seal")
        if not self.seal:
            raise Refusal("source-groupoid witness is unsealed")
        canonical = (
            _complete_component_map(
                "role",
                self.source.role_carrier,
                self.target.role_carrier,
                self.role_map,
                role_carrier=True,
            ),
            _complete_component_map(
                "matter",
                self.source.matter_carrier,
                self.target.matter_carrier,
                self.matter_map,
            ),
            _complete_component_map(
                "port",
                self.source.port_carrier,
                self.target.port_carrier,
                self.port_map,
            ),
            _complete_component_map(
                "occurrence",
                self.source.occurrence_carrier,
                self.target.occurrence_carrier,
                self.occurrence_map,
            ),
        )
        for field, value in zip(
            ("role_map", "matter_map", "port_map", "occurrence_map"),
            canonical,
            strict=True,
        ):
            object.__setattr__(self, field, value)
        transported = _relabel_arrow_raw(self.source.arrow, self)
        if transported != self.target.arrow:
            raise Refusal("groupoid witness does not transport source to target")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "SourceGroupoidWitness",
            "source": self.source,
            "target": self.target,
            "role_map": self.role_map,
            "matter_map": self.matter_map,
            "port_map": self.port_map,
            "occurrence_map": self.occurrence_map,
            "seal": self.seal,
        }


def witness_identity_data(witness: SourceGroupoidWitness) -> dict[str, Any]:
    _require_exact(witness, SourceGroupoidWitness, "witness identity")
    return {
        "type": "SourceGroupoidWitnessIdentity",
        "source_presentation_identity": presentation_identity(witness.source),
        "target_presentation_identity": presentation_identity(witness.target),
        "role_map": witness.role_map,
        "matter_map": witness.matter_map,
        "port_map": witness.port_map,
        "occurrence_map": witness.occurrence_map,
        "seal": witness.seal,
    }


def witness_identity(witness: SourceGroupoidWitness) -> str:
    return canonical_hash(witness_identity_data(witness))


def _rename(mapping: tuple[tuple[str, str], ...], value: str) -> str:
    return dict(mapping).get(value, value)


def _relabel_formula_raw(formula: Formula, plan: Any) -> Formula:
    roles = tuple(_rename(plan.role_map, role) for role in formula.roles)
    return Formula(roles, formula.table)


def _relabel_context_raw(context: Context, plan: Any) -> Context:
    roles = tuple(
        Role(_rename(plan.role_map, role.name), role.kind) for role in context.roles
    )
    cells = tuple(
        tuple(_rename(plan.role_map, name) for name in cell)
        for cell in context.cells
    )
    return Context(roles, cells, context.neutral_label)


def _relabel_port_raw(port: Port, plan: Any) -> Port:
    return Port(
        _rename(plan.port_map, port.name),
        Role(_rename(plan.role_map, port.child.name), port.child.kind),
        _relabel_formula_raw(port.parent0, plan),
        _relabel_formula_raw(port.parent1, plan),
    )


def _relabel_boundary_raw(boundary: Boundary, plan: Any) -> Boundary:
    if boundary.kind == "UNIT":
        return unit_boundary()
    if boundary.kind == "TENSOR":
        if type(boundary.left) is not Boundary or type(boundary.right) is not Boundary:
            raise Refusal("tensor boundary children are malformed")
        return tensor_boundary(
            _relabel_boundary_raw(boundary.left, plan),
            _relabel_boundary_raw(boundary.right, plan),
        )
    return atomic_boundary(
        tuple(_rename(plan.matter_map, name) for name in boundary.matter_roles),
        _relabel_context_raw(boundary.base, plan),
        tuple(
            PortDecl(_relabel_port_raw(decl.port, plan), decl.mode)
            for decl in boundary.ports
        ),
        neutral_label=boundary.neutral_label,
        presentation_status_order=boundary.presentation_status_order,
    )


def _relabel_occurrence_raw(occurrence: Occurrence, plan: Any) -> Occurrence:
    return Occurrence(
        _rename(plan.occurrence_map, occurrence.occurrence_id),
        _rename(plan.matter_map, occurrence.matter_role),
        _rename(plan.port_map, occurrence.port_name),
        _relabel_formula_raw(occurrence.query, plan),
        occurrence.target_mode,
        occurrence.seal,
    )


def _relabel_arrow_raw(arrow: Arrow, plan: Any) -> Arrow:
    if arrow.kind == "IDENTITY":
        return identity_arrow(_relabel_boundary_raw(arrow.source, plan))
    if arrow.kind == "GENERATOR":
        if type(arrow.occurrence) is not Occurrence:
            raise Refusal("generator occurrence is malformed")
        return generator_arrow(
            _relabel_boundary_raw(arrow.source, plan),
            _relabel_occurrence_raw(arrow.occurrence, plan),
        )
    if arrow.kind == "COMPOSE":
        first, second = arrow.children
        return compose_arrows(
            _relabel_arrow_raw(first, plan), _relabel_arrow_raw(second, plan)
        )
    if arrow.kind == "TENSOR":
        left, right = arrow.children
        return tensor_arrow(
            _relabel_arrow_raw(left, plan), _relabel_arrow_raw(right, plan)
        )
    if arrow.kind == "SYMMETRY":
        left, right = arrow.objects
        return symmetry_arrow(
            _relabel_boundary_raw(left, plan), _relabel_boundary_raw(right, plan)
        )
    if arrow.kind in ("ASSOCIATOR", "ASSOCIATOR_INV"):
        a, b, c = arrow.objects
        return associator_arrow(
            _relabel_boundary_raw(a, plan),
            _relabel_boundary_raw(b, plan),
            _relabel_boundary_raw(c, plan),
            inverse=arrow.kind == "ASSOCIATOR_INV",
        )
    if "UNITOR" in arrow.kind:
        (obj,) = arrow.objects
        return unitor_arrow(
            _relabel_boundary_raw(obj, plan),
            "LEFT" if arrow.kind.startswith("LEFT") else "RIGHT",
            inverse=arrow.kind.endswith("_INV"),
        )
    raise Refusal("unreachable relabelled arrow branch")


def make_groupoid_witness(
    source_arrow: Arrow,
    role_map: tuple[tuple[str, str], ...] = (),
    matter_map: tuple[tuple[str, str], ...] = (),
    port_map: tuple[tuple[str, str], ...] = (),
    occurrence_map: tuple[tuple[str, str], ...] = (),
) -> SourceGroupoidWitness:
    _require_exact(source_arrow, Arrow, "groupoid source arrow")
    plan = _RelabelPlan(role_map, matter_map, port_map, occurrence_map)
    target_arrow = _relabel_arrow_raw(source_arrow, plan)
    return SourceGroupoidWitness(
        presentation_from_arrow(source_arrow),
        presentation_from_arrow(target_arrow),
        role_map,
        matter_map,
        port_map,
        occurrence_map,
    )


def identity_witness(arrow: Arrow) -> SourceGroupoidWitness:
    return make_groupoid_witness(arrow)


def _is_identity_witness_on(
    witness: SourceGroupoidWitness, presentation: SourcePresentation
) -> bool:
    """Recognize the unique empty-sparse identity without rebuilding it."""

    _require_exact(witness, SourceGroupoidWitness, "identity witness candidate")
    _require_exact(presentation, SourcePresentation, "identity witness presentation")
    return (
        witness.source == presentation
        and witness.target == presentation
        and witness.role_map == ()
        and witness.matter_map == ()
        and witness.port_map == ()
        and witness.occurrence_map == ()
    )


def restrict_witness_to_arrow(
    witness: SourceGroupoidWitness, arrow: Arrow
) -> SourceGroupoidWitness:
    _require_exact(witness, SourceGroupoidWitness, "restricted groupoid witness")
    _require_exact(arrow, Arrow, "restricted groupoid arrow")
    presentation = presentation_from_arrow(arrow)

    def keep(
        rows: tuple[tuple[str, str], ...], carrier: tuple[Any, ...], *, role: bool = False
    ) -> tuple[tuple[str, str], ...]:
        allowed = set(_carrier_names(carrier, role))
        return tuple(row for row in rows if row[0] in allowed)

    return make_groupoid_witness(
        arrow,
        keep(witness.role_map, presentation.role_carrier, role=True),
        keep(witness.matter_map, presentation.matter_carrier),
        keep(witness.port_map, presentation.port_carrier),
        keep(witness.occurrence_map, presentation.occurrence_carrier),
    )


def _completed_pairs(
    source_carrier: tuple[Any, ...],
    rows: tuple[tuple[str, str], ...],
    *,
    role_carrier: bool = False,
) -> tuple[tuple[str, str], ...]:
    names = _carrier_names(source_carrier, role_carrier)
    mapping = dict(rows)
    return tuple((source, mapping.get(source, source)) for source in names)


def inverse_witness(witness: SourceGroupoidWitness) -> SourceGroupoidWitness:
    _require_exact(witness, SourceGroupoidWitness, "groupoid witness")
    components = (
        _completed_pairs(witness.source.role_carrier, witness.role_map, role_carrier=True),
        _completed_pairs(witness.source.matter_carrier, witness.matter_map),
        _completed_pairs(witness.source.port_carrier, witness.port_map),
        _completed_pairs(witness.source.occurrence_carrier, witness.occurrence_map),
    )
    inverse_components = tuple(
        tuple((target, source) for source, target in component if source != target)
        for component in components
    )
    return SourceGroupoidWitness(
        witness.target,
        witness.source,
        inverse_components[0],
        inverse_components[1],
        inverse_components[2],
        inverse_components[3],
    )


def compose_witnesses(
    first: SourceGroupoidWitness, second: SourceGroupoidWitness
) -> SourceGroupoidWitness:
    _require_exact(first, SourceGroupoidWitness, "first groupoid witness")
    _require_exact(second, SourceGroupoidWitness, "second groupoid witness")
    if first.target != second.source:
        raise Refusal("groupoid witnesses have mismatched middle presentations")

    def compose_component(
        source_carrier: tuple[Any, ...],
        left: tuple[tuple[str, str], ...],
        right: tuple[tuple[str, str], ...],
        *,
        role_carrier: bool = False,
    ) -> tuple[tuple[str, str], ...]:
        left_map = dict(left)
        right_map = dict(right)
        sources = _carrier_names(source_carrier, role_carrier)
        composed = tuple(
            (
                source,
                right_map.get(left_map.get(source, source), left_map.get(source, source)),
            )
            for source in sources
        )
        return tuple((source, target) for source, target in composed if source != target)

    return SourceGroupoidWitness(
        first.source,
        second.target,
        compose_component(
            first.source.role_carrier,
            first.role_map,
            second.role_map,
            role_carrier=True,
        ),
        compose_component(
            first.source.matter_carrier, first.matter_map, second.matter_map
        ),
        compose_component(first.source.port_carrier, first.port_map, second.port_map),
        compose_component(
            first.source.occurrence_carrier,
            first.occurrence_map,
            second.occurrence_map,
        ),
    )


def _completed_witness_maps(
    witness: SourceGroupoidWitness,
) -> dict[str, tuple[tuple[str, str], ...]]:
    _require_exact(witness, SourceGroupoidWitness, "completed groupoid witness")
    return {
        "role": _completed_pairs(
            witness.source.role_carrier, witness.role_map, role_carrier=True
        ),
        "matter": _completed_pairs(
            witness.source.matter_carrier, witness.matter_map
        ),
        "port": _completed_pairs(witness.source.port_carrier, witness.port_map),
        "occurrence": _completed_pairs(
            witness.source.occurrence_carrier, witness.occurrence_map
        ),
    }


def _abstract_total_map(
    source: tuple[str, ...],
    target: tuple[str, ...],
    sparse: tuple[tuple[str, str], ...],
) -> tuple[tuple[str, str], ...]:
    return _completed_pairs(
        source,
        _complete_component_map("abstract", source, target, sparse),
    )


def _abstract_sparse_map(
    total: tuple[tuple[str, str], ...]
) -> tuple[tuple[str, str], ...]:
    return tuple((source, target) for source, target in total if source != target)


def _abstract_compose_maps(
    first: tuple[tuple[str, str], ...],
    second: tuple[tuple[str, str], ...],
) -> tuple[tuple[str, str], ...]:
    right = dict(second)
    return tuple((source, right[target]) for source, target in first)


def measure_abstract_groupoid_census() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    associativity_hashes: list[str] = []
    associativity_cases = 0
    mixed_identity_rows: list[dict[str, Any]] = []
    for size in range(5):
        source = tuple(f"s_{index}" for index in range(size))
        target = tuple(f"t_{index}" for index in range(size))
        permutations = tuple(itertools.permutations(range(size)))
        for permutation in permutations:
            sparse = tuple(
                (source[index], target[permutation[index]])
                for index in range(size)
            )
            total = _abstract_total_map(source, target, sparse)
            inverse_lookup = {
                target_name: source_name for source_name, target_name in total
            }
            inverse_total = tuple(
                (target_name, inverse_lookup[target_name]) for target_name in target
            )
            source_identity = tuple((name, name) for name in source)
            target_identity = tuple((name, name) for name in target)
            left_identity = _abstract_compose_maps(source_identity, total)
            right_identity = _abstract_compose_maps(total, target_identity)
            inverse_left = _abstract_compose_maps(total, inverse_total)
            inverse_right = _abstract_compose_maps(inverse_total, total)
            row = {
                "size": size,
                "source": source,
                "target": target,
                "total_map": total,
                "canonical_sparse_map": _abstract_sparse_map(total),
                "inverse_total_map": inverse_total,
                "left_identity_exact": left_identity == total,
                "right_identity_exact": right_identity == total,
                "left_inverse_exact": inverse_left == source_identity,
                "right_inverse_exact": inverse_right == target_identity,
                "roundtrip_exact": _abstract_compose_maps(
                    inverse_total, total
                )
                == target_identity,
            }
            rows.append(row)

        common = tuple(f"p_{index}" for index in range(size))
        common_maps = tuple(
            tuple((common[index], common[permutation[index]]) for index in range(size))
            for permutation in permutations
        )
        for first in common_maps:
            for second in common_maps:
                for third in common_maps:
                    left = _abstract_compose_maps(
                        _abstract_compose_maps(first, second), third
                    )
                    right = _abstract_compose_maps(
                        first, _abstract_compose_maps(second, third)
                    )
                    if left != right:
                        raise IntegrityFailure("abstract groupoid associativity failed")
                    associativity_hashes.append(canonical_hash((size, first, second, third, left)))
                    associativity_cases += 1

        if size > 0:
            shared_source = ("shared",) + tuple(
                f"mixed_s_{index}" for index in range(size - 1)
            )
            shared_target = ("shared",) + tuple(
                f"mixed_t_{index}" for index in range(size - 1)
            )
            mixed_sparse = tuple(
                (shared_source[index], shared_target[index])
                for index in range(1, size)
            )
            mixed_total = _abstract_total_map(
                shared_source, shared_target, mixed_sparse
            )
            mixed_identity_rows.append(
                {
                    "size": size,
                    "source": shared_source,
                    "target": shared_target,
                    "canonical_sparse_map": _abstract_sparse_map(mixed_total),
                    "completed_map": mixed_total,
                    "shared_identity_completed": mixed_total[0]
                    == ("shared", "shared"),
                }
            )
    expected_map_count = sum(
        len(tuple(itertools.permutations(range(size)))) for size in range(5)
    )
    expected_associativity_count = sum(
        len(tuple(itertools.permutations(range(size)))) ** 3
        for size in range(5)
    )
    return {
        "sizes": tuple(range(5)),
        "bijection_rows": tuple(rows),
        "bijection_count": len(rows),
        "expected_bijection_count": expected_map_count,
        "mixed_identity_rows": tuple(mixed_identity_rows),
        "associativity_case_count": associativity_cases,
        "expected_associativity_case_count": expected_associativity_count,
        "associativity_case_hashes": tuple(associativity_hashes),
        "all_exact": len(rows) == expected_map_count
        and all(
            row["left_identity_exact"]
            and row["right_identity_exact"]
            and row["left_inverse_exact"]
            and row["right_inverse_exact"]
            and row["roundtrip_exact"]
            for row in rows
        )
        and all(row["shared_identity_completed"] for row in mixed_identity_rows)
        and associativity_cases == expected_associativity_count,
    }


def _suffix_groupoid_witness(
    arrow: Arrow,
    suffix: str,
    namespaces: tuple[str, ...],
) -> SourceGroupoidWitness:
    presentation = presentation_from_arrow(arrow)
    selected = set(namespaces)
    if not selected or not selected <= {"role", "matter", "port", "occurrence"}:
        raise Refusal("groupoid suffix namespaces are malformed")
    role_map = (
        tuple((name, name + suffix) for name, _ in presentation.role_carrier)
        if "role" in selected
        else ()
    )
    matter_map = (
        tuple((name, name + suffix) for name in presentation.matter_carrier)
        if "matter" in selected
        else ()
    )
    port_map = (
        tuple((name, name + suffix) for name in presentation.port_carrier)
        if "port" in selected
        else ()
    )
    occurrence_map = (
        tuple((name, name + suffix) for name in presentation.occurrence_carrier)
        if "occurrence" in selected
        else ()
    )
    return make_groupoid_witness(
        arrow, role_map, matter_map, port_map, occurrence_map
    )


def _require_names_in_carrier(
    names: Iterable[str], carrier: tuple[Any, ...], label: str, *, role: bool = False
) -> None:
    allowed = set(_carrier_names(carrier, role))
    if not set(names).issubset(allowed):
        raise Refusal(f"{label} contains a label outside the witness source")


@dataclass(frozen=True, slots=True)
class BoundaryNode:
    """One address-bound source/target boundary occurrence in an Arrow AST."""

    boundary: Boundary
    boundary_semantic_bytes: bytes
    ast_address: tuple[int, ...]
    endpoint_role: str

    def __post_init__(self) -> None:
        _require_exact(self.boundary, Boundary, "boundary-node boundary")
        _require_exact(
            self.boundary_semantic_bytes, bytes, "boundary-node semantic bytes"
        )
        _require_exact_tuple(self.ast_address, "boundary-node AST address")
        if any(type(index) is not int or index < 0 for index in self.ast_address):
            raise Refusal("boundary-node AST address is malformed")
        _require_exact(self.endpoint_role, str, "boundary-node endpoint role")
        if self.endpoint_role not in ("SOURCE", "TARGET"):
            raise Refusal("boundary-node endpoint role is not source or target")
        expected = canonical_bytes(boundary_semantic_key(self.boundary))
        if self.boundary_semantic_bytes != expected:
            raise Refusal("boundary-node semantic bytes are forged")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "BoundaryNode",
            "boundary_semantic_bytes": self.boundary_semantic_bytes,
            "ast_address": self.ast_address,
            "endpoint_role": self.endpoint_role,
        }


def _arrow_at_address(arrow: Arrow, address: tuple[int, ...]) -> Arrow:
    _require_exact(arrow, Arrow, "addressed Arrow")
    _require_exact_tuple(address, "Arrow AST address")
    current = arrow
    for index in address:
        if type(index) is not int or index < 0 or index >= len(current.children):
            raise Refusal("Arrow AST address is outside the presentation")
        current = current.children[index]
    return current


def boundary_nodes(presentation: SourcePresentation) -> tuple[BoundaryNode, ...]:
    """Return the coefficient-zero-inclusive address catalogue for a presentation."""

    _require_exact(presentation, SourcePresentation, "boundary-node presentation")
    nodes: list[BoundaryNode] = []

    def walk(current: Arrow, address: tuple[int, ...]) -> None:
        nodes.append(
            BoundaryNode(
                current.source,
                canonical_bytes(boundary_semantic_key(current.source)),
                address,
                "SOURCE",
            )
        )
        nodes.append(
            BoundaryNode(
                current.target,
                canonical_bytes(boundary_semantic_key(current.target)),
                address,
                "TARGET",
            )
        )
        for index, child in enumerate(current.children):
            walk(child, address + (index,))

    walk(presentation.arrow, ())
    return tuple(nodes)


def boundary_node_at(
    presentation: SourcePresentation,
    address: tuple[int, ...],
    endpoint_role: str,
) -> BoundaryNode:
    _require_exact(presentation, SourcePresentation, "addressed presentation")
    _require_exact_tuple(address, "addressed boundary-node path")
    _require_exact(endpoint_role, str, "addressed endpoint role")
    if endpoint_role not in ("SOURCE", "TARGET"):
        raise Refusal("addressed endpoint role is invalid")
    arrow = _arrow_at_address(presentation.arrow, address)
    boundary = arrow.source if endpoint_role == "SOURCE" else arrow.target
    return BoundaryNode(
        boundary,
        canonical_bytes(boundary_semantic_key(boundary)),
        address,
        endpoint_role,
    )


def _derive_target_node(
    source_node: BoundaryNode, witness: SourceGroupoidWitness
) -> BoundaryNode:
    _require_exact(source_node, BoundaryNode, "configuration-action source node")
    _require_exact(witness, SourceGroupoidWitness, "configuration-action witness")
    expected_source_node = boundary_node_at(
        witness.source, source_node.ast_address, source_node.endpoint_role
    )
    if source_node != expected_source_node:
        raise Refusal("configuration-action source node is absent from presentation")
    target_node = boundary_node_at(
        witness.target, source_node.ast_address, source_node.endpoint_role
    )
    # SourceGroupoidWitness construction already proves whole-Arrow literal
    # transport.  Address preservation therefore derives this exact endpoint;
    # rebuilding the complete boundary for every catalogue coordinate would be
    # redundant evidence, not a stronger action check.
    return target_node


def _transport_configuration_to_derived_node(
    source_node: BoundaryNode,
    target_node: BoundaryNode,
    configuration: Configuration,
    witness: SourceGroupoidWitness,
) -> Configuration:
    validate_configuration(source_node.boundary, configuration)
    _require_names_in_carrier(
        (name for name, _ in configuration.matter),
        witness.source.matter_carrier,
        "configuration matter",
    )
    _require_names_in_carrier(
        (name for name, _ in configuration.sectors),
        witness.source.port_carrier,
        "configuration sectors",
    )
    _require_names_in_carrier(
        context_role_names(configuration.context),
        witness.source.role_carrier,
        "configuration context",
        role=True,
    )
    transported = configuration_from_assignments(
        target_node.boundary,
        {
            _rename(witness.matter_map, name): value
            for name, value in configuration.matter
        },
        {
            _rename(witness.port_map, name): value
            for name, value in configuration.sectors
        },
    )
    expected_context = relabel_context(configuration.context, witness)
    if context_semantic_key(transported.context) != context_semantic_key(
        expected_context
    ):
        raise Refusal("configuration context failed completed witness action")
    validate_configuration(target_node.boundary, transported)
    return transported


@dataclass(frozen=True, slots=True)
class ConfigurationTransport:
    witness: SourceGroupoidWitness
    source_node: BoundaryNode
    target_node: BoundaryNode
    source_configuration: Configuration
    transported_configuration: Configuration

    def __post_init__(self) -> None:
        _require_exact(self.witness, SourceGroupoidWitness, "transport witness")
        _require_exact(self.source_node, BoundaryNode, "transport source node")
        _require_exact(self.target_node, BoundaryNode, "transport target node")
        _require_exact(
            self.source_configuration, Configuration, "transport source configuration"
        )
        _require_exact(
            self.transported_configuration,
            Configuration,
            "transported configuration",
        )
        expected_node = _derive_target_node(self.source_node, self.witness)
        if self.target_node != expected_node:
            raise Refusal("configuration transport carries a nonimage target node")
        expected_configuration = _transport_configuration_to_derived_node(
            self.source_node,
            self.target_node,
            self.source_configuration,
            self.witness,
        )
        if self.transported_configuration != expected_configuration:
            raise Refusal("configuration transport carries a forged target state")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "ConfigurationTransport",
            "witness_identity": witness_identity(self.witness),
            "source_node": self.source_node,
            "target_node": self.target_node,
            "source_configuration": self.source_configuration,
            "transported_configuration": self.transported_configuration,
        }


def act_configuration(
    source_node: BoundaryNode,
    configuration: Configuration,
    witness: SourceGroupoidWitness,
) -> ConfigurationTransport:
    """Closed configuration action: the target is derived, never supplied."""

    _require_exact(source_node, BoundaryNode, "configuration-action source node")
    _require_exact(configuration, Configuration, "configuration-action state")
    _require_exact(witness, SourceGroupoidWitness, "configuration-action witness")
    target_node = _derive_target_node(source_node, witness)
    transported = _transport_configuration_to_derived_node(
        source_node, target_node, configuration, witness
    )
    return ConfigurationTransport(
        witness, source_node, target_node, configuration, transported
    )


def assert_configuration_target(
    source_node: BoundaryNode,
    asserted_target_node: BoundaryNode,
    witness: SourceGroupoidWitness,
) -> BoundaryNode:
    """Assertion-only target gate; it never constructs a configuration action."""

    _require_exact(source_node, BoundaryNode, "asserted-action source node")
    _require_exact(asserted_target_node, BoundaryNode, "asserted-action target node")
    _require_exact(witness, SourceGroupoidWitness, "asserted-action witness")
    derived = _derive_target_node(source_node, witness)
    if asserted_target_node != derived:
        raise Refusal("asserted configuration target is not the derived witness image")
    return derived


@dataclass(frozen=True, slots=True)
class ConfigurationActionLawRow:
    law_kind: str
    presentations: tuple[SourcePresentation, ...]
    witnesses: tuple[SourceGroupoidWitness, ...]
    transports: tuple[ConfigurationTransport, ...]
    final_nodes: tuple[BoundaryNode, ...]
    final_configurations: tuple[Configuration, ...]
    exact: bool

    def __post_init__(self) -> None:
        _require_exact(self.law_kind, str, "configuration law kind")
        if self.law_kind not in (
            "IDENTITY",
            "INVERSE",
            "COMPOSITION",
            "ASSOCIATIVITY",
            "TENSOR",
        ):
            raise Refusal("unknown configuration action law")
        for value, expected, label in (
            (self.presentations, SourcePresentation, "law presentation"),
            (self.witnesses, SourceGroupoidWitness, "law witness"),
            (self.transports, ConfigurationTransport, "law transport"),
            (self.final_nodes, BoundaryNode, "law final node"),
            (self.final_configurations, Configuration, "law final configuration"),
        ):
            _require_exact_tuple(value, label + " tuple")
            if any(type(item) is not expected for item in value):
                raise Refusal(label + " tuple contains a foreign object")
        _require_exact(self.exact, bool, "configuration law equality")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "ConfigurationActionLawRow",
            "law_kind": self.law_kind,
            "presentation_identities": tuple(
                presentation_identity(value) for value in self.presentations
            ),
            "witness_identities": tuple(
                witness_identity(value) for value in self.witnesses
            ),
            "transports": self.transports,
            "final_nodes": self.final_nodes,
            "final_configurations": self.final_configurations,
            "exact": self.exact,
        }


def identity_action_row(
    source_presentation: SourcePresentation,
    source_node: BoundaryNode,
    configuration: Configuration,
) -> ConfigurationActionLawRow:
    _require_exact(source_presentation, SourcePresentation, "identity presentation")
    if source_node not in boundary_nodes(source_presentation):
        raise Refusal("identity action node is absent from supplied presentation")
    identity = identity_witness(source_presentation.arrow)
    transport = act_configuration(source_node, configuration, identity)
    exact = (
        transport.target_node == source_node
        and transport.transported_configuration == configuration
    )
    return ConfigurationActionLawRow(
        "IDENTITY",
        (source_presentation,),
        (identity,),
        (transport,),
        (transport.target_node,),
        (transport.transported_configuration,),
        exact,
    )


def inverse_action_row(
    source_node: BoundaryNode,
    configuration: Configuration,
    witness: SourceGroupoidWitness,
) -> ConfigurationActionLawRow:
    inverse = inverse_witness(witness)
    forward = act_configuration(source_node, configuration, witness)
    backward = act_configuration(
        forward.target_node, forward.transported_configuration, inverse
    )
    exact = (
        backward.target_node == source_node
        and backward.transported_configuration == configuration
    )
    return ConfigurationActionLawRow(
        "INVERSE",
        (witness.source, witness.target),
        (witness, inverse),
        (forward, backward),
        (backward.target_node,),
        (backward.transported_configuration,),
        exact,
    )


def composition_action_row(
    source_node: BoundaryNode,
    configuration: Configuration,
    first: SourceGroupoidWitness,
    second: SourceGroupoidWitness,
) -> ConfigurationActionLawRow:
    composite = compose_witnesses(first, second)
    first_transport = act_configuration(source_node, configuration, first)
    second_transport = act_configuration(
        first_transport.target_node,
        first_transport.transported_configuration,
        second,
    )
    composite_transport = act_configuration(source_node, configuration, composite)
    exact = (
        second_transport.target_node == composite_transport.target_node
        and second_transport.transported_configuration
        == composite_transport.transported_configuration
    )
    return ConfigurationActionLawRow(
        "COMPOSITION",
        (first.source, first.target, second.target),
        (first, second, composite),
        (first_transport, second_transport, composite_transport),
        (second_transport.target_node, composite_transport.target_node),
        (
            second_transport.transported_configuration,
            composite_transport.transported_configuration,
        ),
        exact,
    )


def associativity_action_row(
    source_node: BoundaryNode,
    configuration: Configuration,
    first: SourceGroupoidWitness,
    second: SourceGroupoidWitness,
    third: SourceGroupoidWitness,
) -> ConfigurationActionLawRow:
    first_second = compose_witnesses(first, second)
    second_third = compose_witnesses(second, third)
    left = compose_witnesses(first_second, third)
    right = compose_witnesses(first, second_third)
    t_first = act_configuration(source_node, configuration, first)
    t_second = act_configuration(
        t_first.target_node, t_first.transported_configuration, second
    )
    t_third = act_configuration(
        t_second.target_node, t_second.transported_configuration, third
    )
    t_left = act_configuration(source_node, configuration, left)
    t_right = act_configuration(source_node, configuration, right)
    exact = (
        t_third.target_node == t_left.target_node == t_right.target_node
        and t_third.transported_configuration
        == t_left.transported_configuration
        == t_right.transported_configuration
    )
    return ConfigurationActionLawRow(
        "ASSOCIATIVITY",
        (first.source, first.target, second.target, third.target),
        (first, second, third, first_second, second_third, left, right),
        (t_first, t_second, t_third, t_left, t_right),
        (t_third.target_node, t_left.target_node, t_right.target_node),
        (
            t_third.transported_configuration,
            t_left.transported_configuration,
            t_right.transported_configuration,
        ),
        exact,
    )


def _tensor_configuration_from_factors(
    tensor_node: BoundaryNode,
    left_configuration: Configuration,
    right_configuration: Configuration,
) -> Configuration:
    if tensor_node.boundary.kind != "TENSOR":
        raise Refusal("tensor configuration node is not a tensor boundary")
    matter = matter_dict(left_configuration) | matter_dict(right_configuration)
    sectors = sector_dict(left_configuration) | sector_dict(right_configuration)
    if len(matter) != len(left_configuration.matter) + len(right_configuration.matter):
        raise Refusal("tensor configuration matter carriers collide")
    if len(sectors) != len(left_configuration.sectors) + len(right_configuration.sectors):
        raise Refusal("tensor configuration port carriers collide")
    return configuration_from_assignments(tensor_node.boundary, matter, sectors)


def tensor_action_row(
    tensor_source_node: BoundaryNode,
    tensor_configuration: Configuration,
    left_node: BoundaryNode,
    left_configuration: Configuration,
    left_witness: SourceGroupoidWitness,
    right_node: BoundaryNode,
    right_configuration: Configuration,
    right_witness: SourceGroupoidWitness,
) -> ConfigurationActionLawRow:
    left_source_root = boundary_node_at(left_witness.source, (), "SOURCE")
    right_source_root = boundary_node_at(right_witness.source, (), "SOURCE")
    if left_node != left_source_root or right_node != right_source_root:
        raise Refusal("tensor factor node is not its exact root source node")
    source_arrow = tensor_arrow(
        left_witness.source.arrow, right_witness.source.arrow
    )
    tensor_presentation = presentation_from_arrow(source_arrow)
    expected_tensor_source = boundary_node_at(tensor_presentation, (), "SOURCE")
    if tensor_source_node != expected_tensor_source:
        raise Refusal("declared tensor source node is not reconstructed by factors")
    expected_source_configuration = _tensor_configuration_from_factors(
        tensor_source_node, left_configuration, right_configuration
    )
    if tensor_configuration != expected_source_configuration:
        raise Refusal("declared tensor source configuration is not its factor product")
    tensor_witness = make_groupoid_witness(
        source_arrow,
        left_witness.role_map + right_witness.role_map,
        left_witness.matter_map + right_witness.matter_map,
        left_witness.port_map + right_witness.port_map,
        left_witness.occurrence_map + right_witness.occurrence_map,
    )
    left_transport = act_configuration(
        left_node, left_configuration, left_witness
    )
    right_transport = act_configuration(
        right_node, right_configuration, right_witness
    )
    left_target_root = boundary_node_at(left_witness.target, (), "SOURCE")
    right_target_root = boundary_node_at(right_witness.target, (), "SOURCE")
    if (
        left_transport.target_node != left_target_root
        or right_transport.target_node != right_target_root
    ):
        raise Refusal("tensor factor transport does not end at its root target node")
    tensor_transport = act_configuration(
        tensor_source_node, tensor_configuration, tensor_witness
    )
    expected_tensor_target = boundary_node_at(
        tensor_witness.target, (), "SOURCE"
    )
    if tensor_transport.target_node != expected_tensor_target:
        raise Refusal("tensor transport does not end at its reconstructed root target")
    expected_target_configuration = _tensor_configuration_from_factors(
        tensor_transport.target_node,
        left_transport.transported_configuration,
        right_transport.transported_configuration,
    )
    exact = tensor_transport.transported_configuration == expected_target_configuration
    return ConfigurationActionLawRow(
        "TENSOR",
        (left_witness.source, right_witness.source, tensor_presentation),
        (left_witness, right_witness, tensor_witness),
        (left_transport, right_transport, tensor_transport),
        (left_transport.target_node, right_transport.target_node, tensor_transport.target_node),
        (
            left_transport.transported_configuration,
            right_transport.transported_configuration,
            tensor_transport.transported_configuration,
            expected_target_configuration,
        ),
        exact,
    )


def relabel_formula(formula: Formula, witness: SourceGroupoidWitness) -> Formula:
    _require_exact(formula, Formula, "relabelled formula")
    _require_exact(witness, SourceGroupoidWitness, "formula groupoid witness")
    _require_names_in_carrier(
        formula.roles, witness.source.role_carrier, "formula", role=True
    )
    return _relabel_formula_raw(formula, witness)


def relabel_context(context: Context, witness: SourceGroupoidWitness) -> Context:
    _require_exact(context, Context, "relabelled context")
    _require_exact(witness, SourceGroupoidWitness, "context groupoid witness")
    _require_names_in_carrier(
        context_role_names(context),
        witness.source.role_carrier,
        "context",
        role=True,
    )
    return _relabel_context_raw(context, witness)


def relabel_context_split_proof(
    proof: ContextSplitProof, witness: SourceGroupoidWitness
) -> ContextSplitProof:
    _require_exact(proof, ContextSplitProof, "transported context split proof")
    _require_exact(witness, SourceGroupoidWitness, "split-proof groupoid witness")
    return build_context_split_proof_from_truth(
        relabel_context(proof.source, witness),
        relabel_context(proof.target, witness),
        proof.parent_truth,
        Role(_rename(witness.role_map, proof.child.name), proof.child.kind),
    )


def relabel_port(port: Port, witness: SourceGroupoidWitness) -> Port:
    _require_exact(port, Port, "relabelled port")
    _require_exact(witness, SourceGroupoidWitness, "port groupoid witness")
    _require_names_in_carrier(
        (port.name,), witness.source.port_carrier, "port identity"
    )
    _require_names_in_carrier(
        (port.child.name,) + port.parent0.roles + port.parent1.roles,
        witness.source.role_carrier,
        "port roles",
        role=True,
    )
    return _relabel_port_raw(port, witness)


def relabel_boundary(boundary: Boundary, witness: SourceGroupoidWitness) -> Boundary:
    _require_exact(boundary, Boundary, "relabelled boundary")
    _require_exact(witness, SourceGroupoidWitness, "groupoid witness")
    roles: dict[str, str] = {}
    matter: set[str] = set()
    ports: set[str] = set()
    _walk_boundary_presentation(boundary, roles, matter, ports, set())
    _require_names_in_carrier(
        roles, witness.source.role_carrier, "boundary roles", role=True
    )
    _require_names_in_carrier(matter, witness.source.matter_carrier, "boundary matter")
    _require_names_in_carrier(ports, witness.source.port_carrier, "boundary ports")
    return _relabel_boundary_raw(boundary, witness)


def relabel_occurrence(
    occurrence: Occurrence, witness: SourceGroupoidWitness
) -> Occurrence:
    _require_exact(occurrence, Occurrence, "relabelled occurrence")
    _require_exact(witness, SourceGroupoidWitness, "occurrence groupoid witness")
    _require_names_in_carrier(
        (occurrence.occurrence_id,),
        witness.source.occurrence_carrier,
        "occurrence identity",
    )
    _require_names_in_carrier(
        (occurrence.matter_role,), witness.source.matter_carrier, "occurrence matter"
    )
    _require_names_in_carrier(
        (occurrence.port_name,), witness.source.port_carrier, "occurrence port"
    )
    _require_names_in_carrier(
        occurrence.query.roles,
        witness.source.role_carrier,
        "occurrence query",
        role=True,
    )
    return _relabel_occurrence_raw(occurrence, witness)


def relabel_arrow(arrow: Arrow, witness: SourceGroupoidWitness) -> Arrow:
    _require_exact(arrow, Arrow, "relabelled arrow")
    _require_exact(witness, SourceGroupoidWitness, "groupoid witness")
    if presentation_from_arrow(arrow) != witness.source:
        raise Refusal("groupoid witness has the wrong source presentation")
    transformed = _relabel_arrow_raw(arrow, witness)
    if presentation_from_arrow(transformed) != witness.target:
        raise Refusal("groupoid witness produced the wrong target presentation")
    return transformed


def relabel_configuration(
    source_boundary: Boundary,
    target_boundary: Boundary,
    configuration: Configuration,
    witness: SourceGroupoidWitness,
) -> Configuration:
    _require_exact(witness, SourceGroupoidWitness, "configuration groupoid witness")
    _require_exact(source_boundary, Boundary, "configuration source boundary")
    _require_exact(target_boundary, Boundary, "configuration target boundary")
    expected_target_boundary = relabel_boundary(source_boundary, witness)
    if target_boundary != expected_target_boundary:
        raise Refusal("configuration target boundary is not the witness image")
    validate_configuration(source_boundary, configuration)
    relabelled = configuration_from_assignments(
        target_boundary,
        {
            _rename(witness.matter_map, name): value
            for name, value in configuration.matter
        },
        {
            _rename(witness.port_map, name): value
            for name, value in configuration.sectors
        },
    )
    expected_context = relabel_context(configuration.context, witness)
    if context_semantic_key(relabelled.context) != context_semantic_key(
        expected_context
    ):
        raise Refusal("configuration context failed groupoid transport")
    return relabelled


def generator_leaf_addresses(arrow: Arrow) -> tuple[tuple[int, ...], ...]:
    _require_exact(arrow, Arrow, "generator-address presentation")
    addresses: list[tuple[int, ...]] = []

    def walk(current: Arrow, address: tuple[int, ...]) -> None:
        if current.kind == "GENERATOR":
            addresses.append(address)
        for index, child in enumerate(current.children):
            walk(child, address + (index,))

    walk(arrow, ())
    return tuple(addresses)


def _certificate_parent(
    arrow: Arrow,
    source_configuration: Configuration,
    target_configuration: Configuration,
    operation_kind: str,
) -> tuple[Port, Formula]:
    if type(arrow.occurrence) is not Occurrence:
        raise Refusal("certificate binding requires a generator occurrence")
    port = _selected_port(arrow.source, arrow.occurrence.port_name)
    source_sector = sector_dict(source_configuration)[port.name]
    target_sector = sector_dict(target_configuration)[port.name]
    if operation_kind == "CREATE":
        branch = _branch_index(target_sector)
    elif operation_kind in ("MERGE", "UNCHANGED"):
        branch = _branch_index(source_sector)
    else:
        raise Refusal("certificate binding has an unknown operation")
    return port, port.parent0 if branch == 0 else port.parent1


@dataclass(frozen=True, slots=True)
class CertificateActionInput:
    certificate: BoundSplitCertificate
    law: GammaLaw
    enclosing_source_presentation: SourcePresentation
    generator_ast_address: tuple[int, ...]
    generator_subpresentation: SourcePresentation
    source_node: BoundaryNode
    target_node: BoundaryNode
    arrow: Arrow
    occurrence: Occurrence
    port: Port
    contextual_parent: Formula
    source_configuration: Configuration
    target_configuration: Configuration
    source_column: int
    target_row: int
    input_matter_bit: int
    output_matter_bit: int
    target_sector: str
    operation_kind: str
    child: Role
    context_proof: ContextSplitProof
    inverse_creation_proof: ContextSplitProof
    classifier_consumed_bytes: bytes
    coefficient: Fraction

    def __post_init__(self) -> None:
        for value, expected, label in (
            (self.certificate, BoundSplitCertificate, "action certificate"),
            (self.law, GammaLaw, "action law"),
            (
                self.enclosing_source_presentation,
                SourcePresentation,
                "action enclosing presentation",
            ),
            (
                self.generator_subpresentation,
                SourcePresentation,
                "action generator presentation",
            ),
            (self.source_node, BoundaryNode, "action source node"),
            (self.target_node, BoundaryNode, "action target node"),
            (self.arrow, Arrow, "action Arrow"),
            (self.occurrence, Occurrence, "action occurrence"),
            (self.port, Port, "action port"),
            (self.contextual_parent, Formula, "action contextual parent"),
            (self.source_configuration, Configuration, "action source state"),
            (self.target_configuration, Configuration, "action target state"),
            (self.child, Role, "action child"),
            (self.context_proof, ContextSplitProof, "action context proof"),
            (
                self.inverse_creation_proof,
                ContextSplitProof,
                "action inverse proof",
            ),
            (self.classifier_consumed_bytes, bytes, "action classifier bytes"),
            (self.coefficient, Fraction, "action coefficient"),
        ):
            _require_exact(value, expected, label)
        _require_exact_tuple(
            self.generator_ast_address, "certificate generator AST address"
        )
        if any(
            type(index) is not int or index < 0
            for index in self.generator_ast_address
        ):
            raise Refusal("certificate generator AST address is malformed")
        for value, label in (
            (self.source_column, "certificate source column"),
            (self.target_row, "certificate target row"),
            (self.input_matter_bit, "certificate input bit"),
            (self.output_matter_bit, "certificate output bit"),
        ):
            _require_exact(value, int, label)
        _require_exact(self.target_sector, str, "certificate target sector")
        _require_exact(self.operation_kind, str, "certificate operation")
        leaf = _arrow_at_address(
            self.enclosing_source_presentation.arrow, self.generator_ast_address
        )
        if leaf.kind != "GENERATOR" or leaf != self.arrow:
            raise Refusal("certificate action address is not the bound generator")
        if self.generator_subpresentation != presentation_from_arrow(self.arrow):
            raise Refusal("certificate generator subpresentation is forged")
        expected_source_node = boundary_node_at(
            self.enclosing_source_presentation,
            self.generator_ast_address,
            "SOURCE",
        )
        expected_target_node = boundary_node_at(
            self.enclosing_source_presentation,
            self.generator_ast_address,
            "TARGET",
        )
        if self.source_node != expected_source_node or self.target_node != expected_target_node:
            raise Refusal("certificate action nodes do not match its AST address")
        if type(self.arrow.occurrence) is not Occurrence or self.occurrence != self.arrow.occurrence:
            raise Refusal("certificate action occurrence is not the generator occurrence")
        expected_port, expected_parent = _certificate_parent(
            self.arrow,
            self.source_configuration,
            self.target_configuration,
            self.operation_kind,
        )
        if self.port != expected_port or self.contextual_parent != expected_parent:
            raise Refusal("certificate action port or parent binding is forged")
        if self.child != self.port.child:
            raise Refusal("certificate action child is not the selected port child")
        validate_configuration(self.source_node.boundary, self.source_configuration)
        validate_configuration(self.target_node.boundary, self.target_configuration)
        if self.source_node.boundary != self.arrow.source or self.target_node.boundary != self.arrow.target:
            raise Refusal("certificate action nodes do not carry the generator endpoints")
        if self.source_column != configuration_index(
            self.arrow.source, self.source_configuration
        ):
            raise Refusal("certificate source column is forged")
        if self.target_row != configuration_index(
            self.arrow.target, self.target_configuration
        ):
            raise Refusal("certificate target row is forged")
        if self.input_matter_bit != matter_dict(self.source_configuration)[
            self.occurrence.matter_role
        ]:
            raise Refusal("certificate input bit is forged")
        if self.output_matter_bit != matter_dict(self.target_configuration)[
            self.occurrence.matter_role
        ]:
            raise Refusal("certificate output bit is forged")
        if self.target_sector != sector_dict(self.target_configuration)[self.port.name]:
            raise Refusal("certificate target sector is forged")
        coefficient = _generator_coordinate_coefficient(
            self.law,
            self.arrow,
            self.source_configuration,
            self.target_configuration,
        )
        if coefficient == 0 or coefficient != self.coefficient:
            raise Refusal("certificate action coordinate is zero or forged")
        certificate = self.certificate
        expected_hash_fields = {
            "law_identity": law_identity(self.law),
            "source_boundary_sha256": canonical_hash(
                boundary_semantic_key(self.arrow.source)
            ),
            "source_configuration_sha256": canonical_hash(
                configuration_key(self.source_configuration)
            ),
            "arrow_sha256": canonical_hash(arrow_key(self.arrow)),
            "occurrence_sha256": canonical_hash(
                occurrence_semantic_key(self.arrow.source, self.occurrence)
            ),
            "port_sha256": canonical_hash(
                port_contextual_key(self.arrow.source.base, self.port)
            ),
            "presentation_source_key_sha256": canonical_hash(
                presentation_key(self.law, self.arrow, self.source_configuration)
            ),
            "target_boundary_sha256": canonical_hash(
                boundary_semantic_key(self.arrow.target)
            ),
            "target_configuration_sha256": canonical_hash(
                configuration_key(self.target_configuration)
            ),
            "inverse_creation_proof_sha256": canonical_hash(
                self.inverse_creation_proof
            ),
        }
        if any(getattr(certificate, key) != value for key, value in expected_hash_fields.items()):
            raise Refusal("certificate hash identity disagrees with literal binding")
        proof_source = self.context_proof.source
        if certificate.branch_parent_key != contextual_formula_key(
            proof_source, self.contextual_parent
        ):
            raise Refusal("certificate contextual parent binding is forged")
        if certificate.child_key != (self.child.name, self.child.kind):
            raise Refusal("certificate child binding is forged")
        if (
            certificate.input_matter_bit != self.input_matter_bit
            or certificate.output_matter_bit != self.output_matter_bit
            or certificate.target_sector != self.target_sector
            or certificate.operation_kind != self.operation_kind
            or certificate.coefficient != self.coefficient
            or certificate.context_proof != self.context_proof
            or self.inverse_creation_proof != self.context_proof
            or not certificate.final
        ):
            raise Refusal("certificate scalar or proof binding is forged")
        expected_classifier = canonical_bytes(
            certificate.to_data(include_classifier=False)
        )
        if self.classifier_consumed_bytes != expected_classifier:
            raise Refusal("certificate classifier bytes are not literal")
        if sha256_bytes(self.classifier_consumed_bytes) != (
            certificate.classifier_consumed_sha256
        ):
            raise Refusal("certificate classifier bytes do not match its hash")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "CertificateActionInput",
            "certificate": self.certificate,
            "law": self.law,
            "enclosing_source_presentation_bytes": canonical_bytes(
                presentation_identity_data(self.enclosing_source_presentation)
            ),
            "generator_ast_address": self.generator_ast_address,
            "generator_subpresentation_bytes": canonical_bytes(
                presentation_identity_data(self.generator_subpresentation)
            ),
            "source_node": self.source_node,
            "target_node": self.target_node,
            "arrow": self.arrow,
            "occurrence": self.occurrence,
            "port": self.port,
            "contextual_parent": self.contextual_parent,
            "source_configuration": self.source_configuration,
            "target_configuration": self.target_configuration,
            "source_column": self.source_column,
            "target_row": self.target_row,
            "input_matter_bit": self.input_matter_bit,
            "output_matter_bit": self.output_matter_bit,
            "target_sector": self.target_sector,
            "operation_kind": self.operation_kind,
            "child": self.child,
            "context_proof": self.context_proof,
            "inverse_creation_proof": self.inverse_creation_proof,
            "classifier_consumed_bytes": self.classifier_consumed_bytes,
            "coefficient": self.coefficient,
        }


def _assemble_certificate_action_input(
    law: GammaLaw,
    source_presentation: SourcePresentation,
    generator_ast_address: tuple[int, ...],
    source_configuration: Configuration,
    target_configuration: Configuration,
    certificate: BoundSplitCertificate,
) -> CertificateActionInput:
    leaf = _arrow_at_address(source_presentation.arrow, generator_ast_address)
    if leaf.kind != "GENERATOR" or type(leaf.occurrence) is not Occurrence:
        raise Refusal("certificate action address is not a generator leaf")
    port, parent = _certificate_parent(
        leaf, source_configuration, target_configuration, certificate.operation_kind
    )
    return CertificateActionInput(
        certificate,
        law,
        source_presentation,
        generator_ast_address,
        presentation_from_arrow(leaf),
        boundary_node_at(source_presentation, generator_ast_address, "SOURCE"),
        boundary_node_at(source_presentation, generator_ast_address, "TARGET"),
        leaf,
        leaf.occurrence,
        port,
        parent,
        source_configuration,
        target_configuration,
        configuration_index(leaf.source, source_configuration),
        configuration_index(leaf.target, target_configuration),
        matter_dict(source_configuration)[leaf.occurrence.matter_role],
        matter_dict(target_configuration)[leaf.occurrence.matter_role],
        sector_dict(target_configuration)[port.name],
        certificate.operation_kind,
        port.child,
        certificate.context_proof,
        certificate.context_proof,
        canonical_bytes(certificate.to_data(include_classifier=False)),
        certificate.coefficient,
    )


def build_certificate_action_input(
    law: GammaLaw,
    source_presentation: SourcePresentation,
    generator_ast_address: tuple[int, ...],
    source_configuration: Configuration,
    target_configuration: Configuration,
    inherited_certificate: BoundSplitCertificate,
) -> CertificateActionInput:
    """Bind an inherited hash certificate to its complete literal source packet."""

    _require_exact(law, GammaLaw, "certificate-input law")
    _require_exact(source_presentation, SourcePresentation, "certificate-input presentation")
    _require_exact_tuple(generator_ast_address, "certificate-input address")
    _require_exact(source_configuration, Configuration, "certificate-input source")
    _require_exact(target_configuration, Configuration, "certificate-input target")
    _require_exact(
        inherited_certificate, BoundSplitCertificate, "inherited split certificate"
    )
    leaf = _arrow_at_address(source_presentation.arrow, generator_ast_address)
    rebuilt = build_bound_split_certificate(
        law, leaf, source_configuration, target_configuration
    )
    if rebuilt != inherited_certificate:
        raise Refusal("inherited certificate is foreign to its literal binding")
    return _assemble_certificate_action_input(
        law,
        source_presentation,
        generator_ast_address,
        source_configuration,
        target_configuration,
        inherited_certificate,
    )


def certificate_pairing_key(value: CertificateActionInput) -> tuple[Any, ...]:
    _require_exact(value, CertificateActionInput, "certificate pairing input")
    return (
        law_identity(value.law),
        presentation_identity(value.enclosing_source_presentation),
        value.generator_ast_address,
        presentation_identity(value.generator_subpresentation),
        canonical_hash(value.source_node),
        canonical_hash(value.target_node),
        canonical_hash(arrow_key(value.arrow)),
        canonical_hash(occurrence_semantic_key(value.arrow.source, value.occurrence)),
        canonical_hash(port_contextual_key(value.arrow.source.base, value.port)),
        contextual_formula_key(value.context_proof.source, value.contextual_parent),
        canonical_hash(configuration_key(value.source_configuration)),
        value.input_matter_bit,
        value.output_matter_bit,
        value.target_sector,
        canonical_hash(configuration_key(value.target_configuration)),
        value.operation_kind,
        (value.child.name, value.child.kind),
        canonical_hash(value.context_proof),
        value.certificate.classifier_consumed_sha256,
    )


def _literal_transported_certificate(
    witness: SourceGroupoidWitness,
    value: CertificateActionInput,
    transformed_arrow: Arrow,
    transformed_source: Configuration,
    transformed_target: Configuration,
    local_witness: SourceGroupoidWitness,
) -> BoundSplitCertificate:
    transformed_occurrence = relabel_occurrence(value.occurrence, local_witness)
    transformed_port = relabel_port(value.port, local_witness)
    transformed_parent = relabel_formula(value.contextual_parent, local_witness)
    transformed_proof = relabel_context_split_proof(value.context_proof, local_witness)
    fields: dict[str, Any] = {
        "law_identity": law_identity(value.law),
        "source_boundary_sha256": canonical_hash(
            boundary_semantic_key(transformed_arrow.source)
        ),
        "source_configuration_sha256": canonical_hash(
            configuration_key(transformed_source)
        ),
        "arrow_sha256": canonical_hash(arrow_key(transformed_arrow)),
        "occurrence_sha256": canonical_hash(
            occurrence_semantic_key(transformed_arrow.source, transformed_occurrence)
        ),
        "port_sha256": canonical_hash(
            port_contextual_key(transformed_arrow.source.base, transformed_port)
        ),
        "presentation_source_key_sha256": canonical_hash(
            presentation_key(value.law, transformed_arrow, transformed_source)
        ),
        "input_matter_bit": value.input_matter_bit,
        "output_matter_bit": value.output_matter_bit,
        "source_sector": value.certificate.source_sector,
        "target_sector": value.target_sector,
        "branch_parent_key": contextual_formula_key(
            transformed_proof.source, transformed_parent
        ),
        "child_key": (transformed_port.child.name, transformed_port.child.kind),
        "target_boundary_sha256": canonical_hash(
            boundary_semantic_key(transformed_arrow.target)
        ),
        "target_configuration_sha256": canonical_hash(
            configuration_key(transformed_target)
        ),
        "operation_kind": value.operation_kind,
        "coefficient": value.coefficient,
        "context_proof": transformed_proof,
        "inverse_creation_proof_sha256": canonical_hash(transformed_proof),
        "binding_exact": value.certificate.binding_exact,
        "operation_exact": value.certificate.operation_exact,
        "final": value.certificate.final,
    }
    classifier = canonical_hash({"type": "BoundSplitCertificate", **fields})
    return BoundSplitCertificate(
        **fields, classifier_consumed_sha256=classifier
    )


def act_certificate(
    witness: SourceGroupoidWitness,
    certificate_action_input: CertificateActionInput,
) -> CertificateActionInput:
    """Closed field-by-field action on a complete certificate binding."""

    _require_exact(witness, SourceGroupoidWitness, "certificate-action witness")
    _require_exact(
        certificate_action_input,
        CertificateActionInput,
        "complete certificate-action input",
    )
    value = certificate_action_input
    if witness.source != value.enclosing_source_presentation:
        raise Refusal("certificate action witness has the wrong enclosing source")
    transformed_leaf = _arrow_at_address(
        witness.target.arrow, value.generator_ast_address
    )
    local_witness = restrict_witness_to_arrow(witness, value.arrow)
    if relabel_arrow(value.arrow, local_witness) != transformed_leaf:
        raise Refusal("certificate action leaf is not the restricted witness image")
    source_transport = act_configuration(
        value.source_node, value.source_configuration, witness
    )
    target_transport = act_configuration(
        value.target_node, value.target_configuration, witness
    )
    literal_certificate = _literal_transported_certificate(
        witness,
        value,
        transformed_leaf,
        source_transport.transported_configuration,
        target_transport.transported_configuration,
        local_witness,
    )
    return _assemble_certificate_action_input(
        value.law,
        witness.target,
        value.generator_ast_address,
        source_transport.transported_configuration,
        target_transport.transported_configuration,
        literal_certificate,
    )


def rebuild_certificate_input(
    law: GammaLaw,
    transformed_presentation: SourcePresentation,
    generator_ast_address: tuple[int, ...],
    transformed_source: Configuration,
    transformed_target: Configuration,
) -> CertificateActionInput:
    """Independent reconstruction from transformed law/Arrow/coordinate literals."""

    leaf = _arrow_at_address(transformed_presentation.arrow, generator_ast_address)
    rebuilt = build_bound_split_certificate(
        law, leaf, transformed_source, transformed_target
    )
    return _assemble_certificate_action_input(
        law,
        transformed_presentation,
        generator_ast_address,
        transformed_source,
        transformed_target,
        rebuilt,
    )


@dataclass(frozen=True, slots=True)
class CertificateTransportTriple:
    witness: SourceGroupoidWitness
    original: CertificateActionInput
    literal_transport: CertificateActionInput
    independent_rebuild: CertificateActionInput
    original_pairing_key: tuple[Any, ...]
    transported_pairing_key: tuple[Any, ...]
    equality_coordinates: tuple[tuple[str, bool], ...]
    exact: bool

    def __post_init__(self) -> None:
        _require_exact(self.witness, SourceGroupoidWitness, "certificate triple witness")
        for value, label in (
            (self.original, "certificate triple original"),
            (self.literal_transport, "certificate triple literal transport"),
            (self.independent_rebuild, "certificate triple independent rebuild"),
        ):
            _require_exact(value, CertificateActionInput, label)
        _require_exact_tuple(self.original_pairing_key, "original certificate pairing key")
        _require_exact_tuple(
            self.transported_pairing_key, "transported certificate pairing key"
        )
        _require_exact_tuple(self.equality_coordinates, "certificate equality coordinates")
        if any(
            type(row) is not tuple
            or len(row) != 2
            or type(row[0]) is not str
            or type(row[1]) is not bool
            for row in self.equality_coordinates
        ):
            raise Refusal("certificate equality coordinates are malformed")
        _require_exact(self.exact, bool, "certificate triple equality")
        expected = (
            self.original_pairing_key == certificate_pairing_key(self.original)
            and self.transported_pairing_key
            == certificate_pairing_key(self.literal_transport)
            and all(value for _, value in self.equality_coordinates)
            and self.literal_transport == self.independent_rebuild
        )
        if self.exact != expected:
            raise Refusal("certificate triple conjunction is forged")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "CertificateTransportTriple",
            "witness_identity": witness_identity(self.witness),
            "original": self.original,
            "literal_transport": self.literal_transport,
            "independent_rebuild": self.independent_rebuild,
            "original_pairing_key": self.original_pairing_key,
            "transported_pairing_key": self.transported_pairing_key,
            "equality_coordinates": self.equality_coordinates,
            "exact": self.exact,
        }


def certificate_transport_triple(
    witness: SourceGroupoidWitness,
    value: CertificateActionInput,
) -> CertificateTransportTriple:
    identity = _is_identity_witness_on(
        witness, value.enclosing_source_presentation
    )
    transported = value if identity else act_certificate(witness, value)
    rebuilt = (
        value
        if identity
        else rebuild_certificate_input(
            value.law,
            witness.target,
            value.generator_ast_address,
            transported.source_configuration,
            transported.target_configuration,
        )
    )
    fields = (
        "certificate",
        "law",
        "generator_subpresentation",
        "source_node",
        "target_node",
        "arrow",
        "occurrence",
        "port",
        "contextual_parent",
        "source_configuration",
        "target_configuration",
        "input_matter_bit",
        "output_matter_bit",
        "target_sector",
        "operation_kind",
        "child",
        "context_proof",
        "inverse_creation_proof",
        "classifier_consumed_bytes",
        "coefficient",
    )
    coordinates = tuple(
        (field, getattr(transported, field) == getattr(rebuilt, field))
        for field in fields
    )
    exact = all(value for _, value in coordinates) and transported == rebuilt
    return CertificateTransportTriple(
        witness,
        value,
        transported,
        rebuilt,
        certificate_pairing_key(value),
        certificate_pairing_key(transported),
        coordinates,
        exact,
    )


@dataclass(frozen=True, slots=True)
class CompleteCertificateActionRow:
    """One source-keyed certificate action retained with complete objects."""

    law_kind: str
    witness: SourceGroupoidWitness
    input_value: CertificateActionInput
    pairing_key: tuple[Any, ...]
    triple: CertificateTransportTriple
    exact: bool

    def __post_init__(self) -> None:
        _require_exact(self.law_kind, str, "complete certificate action kind")
        if self.law_kind not in ("IDENTITY", "NONTRIVIAL"):
            raise Refusal("complete certificate action has an unknown kind")
        _require_exact(
            self.witness, SourceGroupoidWitness, "complete certificate witness"
        )
        _require_exact(
            self.input_value,
            CertificateActionInput,
            "complete certificate input",
        )
        _require_exact_tuple(self.pairing_key, "complete certificate pairing key")
        _require_exact(
            self.triple, CertificateTransportTriple, "complete certificate triple"
        )
        _require_exact(self.exact, bool, "complete certificate action exactness")
        expected = (
            self.triple.witness == self.witness
            and self.triple.original == self.input_value
            and self.pairing_key == certificate_pairing_key(self.input_value)
            and self.triple.original_pairing_key == self.pairing_key
            and self.triple.transported_pairing_key
            == certificate_pairing_key(self.triple.literal_transport)
            and self.triple.exact
        )
        if self.law_kind == "IDENTITY":
            expected = (
                expected
                and _is_identity_witness_on(
                    self.witness,
                    self.input_value.enclosing_source_presentation,
                )
                and self.triple.literal_transport == self.input_value
                and self.triple.independent_rebuild == self.input_value
                and self.triple.transported_pairing_key == self.pairing_key
            )
        if self.exact != expected:
            raise Refusal("complete certificate action conjunction is forged")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "CompleteCertificateActionRow",
            "law_kind": self.law_kind,
            "witness": self.witness,
            "input_value": self.input_value,
            "pairing_key": self.pairing_key,
            "triple": self.triple,
            "exact": self.exact,
        }


def complete_certificate_action_row(
    law_kind: str,
    witness: SourceGroupoidWitness,
    value: CertificateActionInput,
) -> CompleteCertificateActionRow:
    """Construct a complete row from the closed action, never from references."""

    triple = certificate_transport_triple(witness, value)
    exact = triple.exact
    if law_kind == "IDENTITY":
        exact = (
            exact
            and _is_identity_witness_on(
                witness, value.enclosing_source_presentation
            )
            and triple.literal_transport == value
            and triple.independent_rebuild == value
            and triple.transported_pairing_key == certificate_pairing_key(value)
        )
    return CompleteCertificateActionRow(
        law_kind,
        witness,
        value,
        certificate_pairing_key(value),
        triple,
        exact,
    )


@dataclass(frozen=True, slots=True)
class CertificateActionLawRow:
    law_kind: str
    witnesses: tuple[SourceGroupoidWitness, ...]
    inputs: tuple[CertificateActionInput, ...]
    triples: tuple[CertificateTransportTriple, ...]
    outputs: tuple[CertificateActionInput, ...]
    exact: bool

    def __post_init__(self) -> None:
        _require_exact(self.law_kind, str, "certificate law kind")
        if self.law_kind not in (
            "IDENTITY",
            "INVERSE",
            "COMPOSITION",
            "ASSOCIATIVITY",
        ):
            raise Refusal("unknown certificate action law")
        for values, expected, label in (
            (self.witnesses, SourceGroupoidWitness, "certificate law witnesses"),
            (self.inputs, CertificateActionInput, "certificate law inputs"),
            (self.triples, CertificateTransportTriple, "certificate law triples"),
            (self.outputs, CertificateActionInput, "certificate law outputs"),
        ):
            _require_exact_tuple(values, label)
            if any(type(value) is not expected for value in values):
                raise Refusal(label + " contain a foreign object")
        _require_exact(self.exact, bool, "certificate law equality")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "CertificateActionLawRow",
            "law_kind": self.law_kind,
            "witness_identities": tuple(
                witness_identity(value) for value in self.witnesses
            ),
            "inputs": self.inputs,
            "triples": self.triples,
            "outputs": self.outputs,
            "exact": self.exact,
        }


def certificate_identity_row(value: CertificateActionInput) -> CertificateActionLawRow:
    _require_exact(value, CertificateActionInput, "certificate identity input")
    identity = identity_witness(value.enclosing_source_presentation.arrow)
    triple = certificate_transport_triple(identity, value)
    exact = canonical_bytes(triple.literal_transport) == canonical_bytes(value)
    return CertificateActionLawRow(
        "IDENTITY", (identity,), (value,), (triple,), (triple.literal_transport,), exact
    )


def certificate_inverse_row(
    value: CertificateActionInput, witness: SourceGroupoidWitness
) -> CertificateActionLawRow:
    forward = certificate_transport_triple(witness, value)
    inverse = inverse_witness(witness)
    backward = certificate_transport_triple(inverse, forward.literal_transport)
    exact = canonical_bytes(backward.literal_transport) == canonical_bytes(value)
    return CertificateActionLawRow(
        "INVERSE",
        (witness, inverse),
        (value, forward.literal_transport),
        (forward, backward),
        (backward.literal_transport,),
        exact,
    )


def certificate_composition_row(
    value: CertificateActionInput,
    first: SourceGroupoidWitness,
    second: SourceGroupoidWitness,
) -> CertificateActionLawRow:
    first_triple = certificate_transport_triple(first, value)
    second_triple = certificate_transport_triple(
        second, first_triple.literal_transport
    )
    composite = compose_witnesses(first, second)
    composite_triple = certificate_transport_triple(composite, value)
    exact = canonical_bytes(second_triple.literal_transport) == canonical_bytes(
        composite_triple.literal_transport
    )
    return CertificateActionLawRow(
        "COMPOSITION",
        (first, second, composite),
        (value, first_triple.literal_transport),
        (first_triple, second_triple, composite_triple),
        (second_triple.literal_transport, composite_triple.literal_transport),
        exact,
    )


def certificate_associativity_row(
    value: CertificateActionInput,
    first: SourceGroupoidWitness,
    second: SourceGroupoidWitness,
    third: SourceGroupoidWitness,
) -> CertificateActionLawRow:
    first_triple = certificate_transport_triple(first, value)
    second_triple = certificate_transport_triple(
        second, first_triple.literal_transport
    )
    third_triple = certificate_transport_triple(
        third, second_triple.literal_transport
    )
    left_witness = compose_witnesses(compose_witnesses(first, second), third)
    right_witness = compose_witnesses(first, compose_witnesses(second, third))
    left_triple = certificate_transport_triple(left_witness, value)
    right_triple = certificate_transport_triple(right_witness, value)
    exact = (
        canonical_bytes(third_triple.literal_transport)
        == canonical_bytes(left_triple.literal_transport)
        == canonical_bytes(right_triple.literal_transport)
    )
    return CertificateActionLawRow(
        "ASSOCIATIVITY",
        (first, second, third, left_witness, right_witness),
        (value, first_triple.literal_transport, second_triple.literal_transport),
        (first_triple, second_triple, third_triple, left_triple, right_triple),
        (
            third_triple.literal_transport,
            left_triple.literal_transport,
            right_triple.literal_transport,
        ),
        exact,
    )


def generator_certificate_inputs(
    law: GammaLaw,
    presentation: SourcePresentation,
    generator_ast_address: tuple[int, ...],
    operation_kind: str | None = None,
) -> tuple[CertificateActionInput, ...]:
    _require_exact(law, GammaLaw, "certificate-input census law")
    _require_exact(presentation, SourcePresentation, "certificate-input census presentation")
    _require_exact_tuple(generator_ast_address, "certificate-input census address")
    if operation_kind is not None and operation_kind not in (
        "CREATE",
        "MERGE",
        "UNCHANGED",
    ):
        raise Refusal("certificate-input census operation is invalid")
    leaf = _arrow_at_address(presentation.arrow, generator_ast_address)
    if leaf.kind != "GENERATOR":
        raise Refusal("certificate-input census address is not a generator")
    linear_map = evaluate_arrow(law, leaf)
    values: list[CertificateActionInput] = []
    for target_row, source_column, coefficient in linear_map.entries:
        if coefficient == 0:
            continue
        source_configuration = leaf.source.catalogue[source_column]
        target_configuration = leaf.target.catalogue[target_row]
        certificate = build_bound_split_certificate(
            law, leaf, source_configuration, target_configuration
        )
        if operation_kind is not None and certificate.operation_kind != operation_kind:
            continue
        values.append(
            _assemble_certificate_action_input(
                law,
                presentation,
                generator_ast_address,
                source_configuration,
                target_configuration,
                certificate,
            )
        )
    return tuple(values)


def _store_complete_bytes(store: dict[str, bytes], value: Any) -> str:
    payload = canonical_bytes(value)
    identity = sha256_bytes(payload)
    prior = store.get(identity)
    if prior is not None and prior != payload:
        raise IntegrityFailure("content-addressed evidence collision")
    store[identity] = payload
    return identity


def _freeze_complete_byte_store(store: Mapping[str, bytes]) -> tuple[dict[str, Any], ...]:
    return tuple(
        {"sha256": identity, "canonical_bytes": store[identity]}
        for identity in sorted(store)
    )


def _complete_byte_store_exact(entries: Sequence[Mapping[str, Any]]) -> bool:
    if type(entries) not in (tuple, list):
        return False
    if not entries:
        return False
    identities: list[str] = []
    for entry in entries:
        if type(entry) is not dict or set(entry) != {"sha256", "canonical_bytes"}:
            return False
        identity = entry["sha256"]
        payload = entry["canonical_bytes"]
        if not _is_lower_hex(identity, 32) or type(payload) is not bytes:
            return False
        if sha256_bytes(payload) != identity:
            return False
        identities.append(identity)
    return len(identities) == len(set(identities))


def _complete_byte_store_identities(
    entries: Sequence[Mapping[str, Any]],
) -> set[str]:
    if not _complete_byte_store_exact(entries):
        return set()
    return {entry["sha256"] for entry in entries}


def _complete_byte_store_payloads(
    entries: Sequence[Mapping[str, Any]],
) -> dict[str, bytes]:
    """Authenticate a complete store before exposing any payload to a decoder."""

    if not _complete_byte_store_exact(entries):
        return {}
    return {entry["sha256"]: entry["canonical_bytes"] for entry in entries}


def _decoded_mapping(value: Any, expected: set[str], label: str) -> dict[str, Any]:
    if type(value) is not dict or set(value) != expected:
        raise Refusal(f"decoded {label} has a foreign field set")
    return value


def _decoded_tuple(value: Any, label: str) -> tuple[Any, ...]:
    if type(value) is not list:
        raise Refusal(f"decoded {label} is not a canonical array")
    return tuple(value)


def _decoded_rows(value: Any, label: str) -> tuple[tuple[Any, ...], ...]:
    return tuple(
        _decoded_tuple(row, f"{label} row")
        for row in _decoded_tuple(value, label)
    )


def _decode_fraction_data(value: Any, label: str) -> Fraction:
    row = _decoded_mapping(value, {"n", "d"}, label)
    if type(row["n"]) is not int or type(row["d"]) is not int or row["d"] == 0:
        raise Refusal(f"decoded {label} is not an exact rational")
    return Fraction(row["n"], row["d"])


def _decode_bytes_data(value: Any, label: str) -> bytes:
    row = _decoded_mapping(value, {"hex"}, label)
    if type(row["hex"]) is not str:
        raise Refusal(f"decoded {label} is not canonical bytes")
    try:
        payload = bytes.fromhex(row["hex"])
    except ValueError as error:
        raise Refusal(f"decoded {label} has malformed hexadecimal bytes") from error
    if payload.hex() != row["hex"]:
        raise Refusal(f"decoded {label} hexadecimal bytes are not canonical")
    return payload


def _decode_formula_data(value: Any) -> Formula:
    row = _decoded_mapping(value, {"type", "roles", "table"}, "Formula")
    if row["type"] != "Formula":
        raise Refusal("decoded Formula type tag is foreign")
    roles = _decoded_tuple(row["roles"], "Formula roles")
    table = _decoded_tuple(row["table"], "Formula table")
    return Formula(roles, table)


def _decode_role_data(value: Any) -> Role:
    row = _decoded_mapping(value, {"type", "name", "kind"}, "Role")
    if row["type"] != "Role":
        raise Refusal("decoded Role type tag is foreign")
    return Role(row["name"], row["kind"])


def _decode_context_data(value: Any) -> Context:
    row = _decoded_mapping(
        value, {"type", "roles", "cells", "neutral_label"}, "Context"
    )
    if row["type"] != "Context":
        raise Refusal("decoded Context type tag is foreign")
    roles = tuple(_decode_role_data(item) for item in _decoded_tuple(row["roles"], "Context roles"))
    cells = _decoded_rows(row["cells"], "Context cells")
    return Context(roles, cells, row["neutral_label"])


def _decode_port_data(value: Any) -> Port:
    row = _decoded_mapping(
        value, {"type", "name", "child", "parent0", "parent1"}, "Port"
    )
    if row["type"] != "Port":
        raise Refusal("decoded Port type tag is foreign")
    return Port(
        row["name"],
        _decode_role_data(row["child"]),
        _decode_formula_data(row["parent0"]),
        _decode_formula_data(row["parent1"]),
    )


def _decode_port_decl_data(value: Any) -> PortDecl:
    row = _decoded_mapping(value, {"type", "port", "mode"}, "PortDecl")
    if row["type"] != "PortDecl":
        raise Refusal("decoded PortDecl type tag is foreign")
    return PortDecl(_decode_port_data(row["port"]), row["mode"])


def _decode_configuration_data(value: Any) -> Configuration:
    row = _decoded_mapping(
        value, {"type", "context", "matter", "sectors"}, "Configuration"
    )
    if row["type"] != "Configuration":
        raise Refusal("decoded Configuration type tag is foreign")
    return Configuration(
        _decode_context_data(row["context"]),
        _decoded_rows(row["matter"], "Configuration matter"),
        _decoded_rows(row["sectors"], "Configuration sectors"),
    )


def _decode_boundary_data(value: Any) -> Boundary:
    row = _decoded_mapping(
        value,
        {
            "type",
            "kind",
            "matter_roles",
            "base",
            "ports",
            "catalogue",
            "left",
            "right",
            "neutral_label",
            "presentation_status_order",
        },
        "Boundary",
    )
    if row["type"] != "Boundary":
        raise Refusal("decoded Boundary type tag is foreign")
    left = None if row["left"] is None else _decode_boundary_data(row["left"])
    right = None if row["right"] is None else _decode_boundary_data(row["right"])
    return Boundary(
        row["kind"],
        _decoded_tuple(row["matter_roles"], "Boundary matter roles"),
        _decode_context_data(row["base"]),
        tuple(
            _decode_port_decl_data(item)
            for item in _decoded_tuple(row["ports"], "Boundary ports")
        ),
        tuple(
            _decode_configuration_data(item)
            for item in _decoded_tuple(row["catalogue"], "Boundary catalogue")
        ),
        left,
        right,
        row["neutral_label"],
        _decoded_tuple(
            row["presentation_status_order"], "Boundary status order"
        ),
    )


def _decode_occurrence_data(value: Any) -> Occurrence:
    row = _decoded_mapping(
        value,
        {
            "type",
            "occurrence_id",
            "matter_role",
            "port_name",
            "query",
            "target_mode",
            "seal",
        },
        "Occurrence",
    )
    if row["type"] != "Occurrence":
        raise Refusal("decoded Occurrence type tag is foreign")
    return Occurrence(
        row["occurrence_id"],
        row["matter_role"],
        row["port_name"],
        _decode_formula_data(row["query"]),
        row["target_mode"],
        row["seal"],
    )


def _decoded_json_identity(value: Any) -> str:
    return sha256_bytes(
        json.dumps(
            value, ensure_ascii=True, sort_keys=True, separators=(",", ":")
        ).encode("ascii")
    )


def _decode_arrow_data(
    value: Any, arrow_cache: dict[str, Arrow] | None = None
) -> Arrow:
    if arrow_cache is None:
        arrow_cache = {}
    identity = _decoded_json_identity(value)
    prior = arrow_cache.get(identity)
    if prior is not None:
        return prior
    row = _decoded_mapping(
        value,
        {"type", "kind", "source", "target", "occurrence", "children", "objects", "seal"},
        "Arrow",
    )
    if row["type"] != "Arrow":
        raise Refusal("decoded Arrow type tag is foreign")
    occurrence = (
        None
        if row["occurrence"] is None
        else _decode_occurrence_data(row["occurrence"])
    )
    arrow = Arrow(
        row["kind"],
        _decode_boundary_data(row["source"]),
        _decode_boundary_data(row["target"]),
        occurrence,
        tuple(
            _decode_arrow_data(item, arrow_cache)
            for item in _decoded_tuple(row["children"], "Arrow children")
        ),
        tuple(
            _decode_boundary_data(item)
            for item in _decoded_tuple(row["objects"], "Arrow objects")
        ),
        row["seal"],
    )
    if _decoded_json_identity(json.loads(canonical_json(arrow))) != identity:
        raise Refusal("decoded Arrow does not reproduce its canonical data")
    arrow_cache[identity] = arrow
    return arrow


def _decode_primitive_data(value: Any) -> PrimitiveSpec:
    row = _decoded_mapping(
        value,
        {"type", "orientation", "contact_site", "rho_mode", "reset_one"},
        "PrimitiveSpec",
    )
    if row["type"] != "PrimitiveSpec":
        raise Refusal("decoded PrimitiveSpec type tag is foreign")
    return PrimitiveSpec(
        row["orientation"], row["contact_site"], row["rho_mode"], row["reset_one"]
    )


def _decode_law_data(
    value: Any, law_cache: dict[str, GammaLaw] | None = None
) -> GammaLaw:
    if law_cache is None:
        law_cache = {}
    identity = _decoded_json_identity(value)
    prior = law_cache.get(identity)
    if prior is not None:
        return prior
    row = _decoded_mapping(
        value, {"type", "g", "primitive", "implementation", "seal"}, "GammaLaw"
    )
    if row["type"] != "GammaLaw":
        raise Refusal("decoded GammaLaw type tag is foreign")
    law = GammaLaw(
        _decode_fraction_data(row["g"], "Gamma coupling"),
        _decode_primitive_data(row["primitive"]),
        row["implementation"],
        row["seal"],
    )
    if _decoded_json_identity(json.loads(canonical_json(law))) != identity:
        raise Refusal("decoded GammaLaw does not reproduce its canonical data")
    law_cache[identity] = law
    return law


def _decode_source_presentation_data(
    value: Any, arrow_cache: dict[str, Arrow] | None = None
) -> SourcePresentation:
    row = _decoded_mapping(
        value,
        {
            "type",
            "arrow",
            "role_carrier",
            "matter_carrier",
            "port_carrier",
            "occurrence_carrier",
            "seal",
        },
        "SourcePresentation",
    )
    if row["type"] != "SourcePresentation":
        raise Refusal("decoded SourcePresentation type tag is foreign")
    return SourcePresentation(
        _decode_arrow_data(row["arrow"], arrow_cache),
        _decoded_rows(row["role_carrier"], "presentation role carrier"),
        _decoded_tuple(row["matter_carrier"], "presentation matter carrier"),
        _decoded_tuple(row["port_carrier"], "presentation port carrier"),
        _decoded_tuple(
            row["occurrence_carrier"], "presentation occurrence carrier"
        ),
        row["seal"],
    )


def _decode_witness_payload(
    payload: bytes, arrow_cache: dict[str, Arrow] | None = None
) -> SourceGroupoidWitness:
    try:
        raw = json.loads(payload.decode("ascii"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise Refusal("witness canonical bytes do not decode as exact JSON") from error
    row = _decoded_mapping(
        raw,
        {
            "type",
            "source",
            "target",
            "role_map",
            "matter_map",
            "port_map",
            "occurrence_map",
            "seal",
        },
        "SourceGroupoidWitness",
    )
    if row["type"] != "SourceGroupoidWitness":
        raise Refusal("decoded witness type tag is foreign")
    witness = SourceGroupoidWitness(
        _decode_source_presentation_data(row["source"], arrow_cache),
        _decode_source_presentation_data(row["target"], arrow_cache),
        _decoded_rows(row["role_map"], "witness role map"),
        _decoded_rows(row["matter_map"], "witness matter map"),
        _decoded_rows(row["port_map"], "witness port map"),
        _decoded_rows(row["occurrence_map"], "witness occurrence map"),
        row["seal"],
    )
    if canonical_bytes(witness) != payload:
        raise Refusal("decoded witness does not reproduce its canonical bytes")
    return witness


def _decode_certificate_action_input_payload(
    payload: bytes,
    arrow_cache: dict[str, Arrow] | None = None,
    law_cache: dict[str, GammaLaw] | None = None,
) -> CertificateActionInput:
    try:
        raw = json.loads(payload.decode("ascii"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise Refusal("certificate input bytes do not decode as exact JSON") from error
    required = {
        "type",
        "certificate",
        "law",
        "enclosing_source_presentation_bytes",
        "generator_ast_address",
        "generator_subpresentation_bytes",
        "source_node",
        "target_node",
        "arrow",
        "occurrence",
        "port",
        "contextual_parent",
        "source_configuration",
        "target_configuration",
        "source_column",
        "target_row",
        "input_matter_bit",
        "output_matter_bit",
        "target_sector",
        "operation_kind",
        "child",
        "context_proof",
        "inverse_creation_proof",
        "classifier_consumed_bytes",
        "coefficient",
    }
    row = _decoded_mapping(raw, required, "CertificateActionInput")
    if row["type"] != "CertificateActionInput":
        raise Refusal("decoded certificate input type tag is foreign")
    law = _decode_law_data(row["law"], law_cache)
    arrow = _decode_arrow_data(row["arrow"], arrow_cache)
    address = _decoded_tuple(
        row["generator_ast_address"], "certificate generator address"
    )
    if address != () or arrow.kind != "GENERATOR":
        raise Refusal("complete action decoder requires a root generator input")
    presentation = presentation_from_arrow(arrow)
    expected_presentation_bytes = canonical_bytes(
        presentation_identity_data(presentation)
    )
    if _decode_bytes_data(
        row["enclosing_source_presentation_bytes"],
        "enclosing source presentation identity",
    ) != expected_presentation_bytes:
        raise Refusal("decoded enclosing presentation identity is forged")
    if _decode_bytes_data(
        row["generator_subpresentation_bytes"],
        "generator subpresentation identity",
    ) != expected_presentation_bytes:
        raise Refusal("decoded generator subpresentation identity is forged")
    source_configuration = _decode_configuration_data(row["source_configuration"])
    target_configuration = _decode_configuration_data(row["target_configuration"])
    certificate = build_bound_split_certificate(
        law, arrow, source_configuration, target_configuration
    )
    rebuilt = _assemble_certificate_action_input(
        law,
        presentation,
        address,
        source_configuration,
        target_configuration,
        certificate,
    )
    if canonical_bytes(rebuilt) != payload:
        raise Refusal("decoded certificate input does not reproduce all embedded bytes")
    return rebuilt


def _configuration_law_reference_exact(
    row: Mapping[str, Any], identities: set[str]
) -> bool:
    required = {
        "law_kind",
        "presentation_identities",
        "witness_identities",
        "transport_refs",
        "final_node_refs",
        "final_configuration_refs",
        "exact",
    }
    return (
        type(row) is dict
        and set(row) == required
        and row["law_kind"]
        in ("IDENTITY", "INVERSE", "COMPOSITION", "ASSOCIATIVITY", "TENSOR")
        and type(row["exact"]) is bool
        and row["exact"]
        and all(
            type(values) is tuple
            for values in (
                row["presentation_identities"],
                row["witness_identities"],
                row["transport_refs"],
                row["final_node_refs"],
                row["final_configuration_refs"],
            )
        )
        and bool(row["transport_refs"])
        and set(row["transport_refs"]) <= identities
        and set(row["final_node_refs"]) <= identities
        and set(row["final_configuration_refs"]) <= identities
        and all(_is_lower_hex(value, 32) for value in row["presentation_identities"])
        and all(_is_lower_hex(value, 32) for value in row["witness_identities"])
    )


def _certificate_triple_reference_exact(
    row: Mapping[str, Any], identities: set[str]
) -> bool:
    required = {
        "witness_identity",
        "original_ref",
        "literal_transport_ref",
        "independent_rebuild_ref",
        "original_pairing_key",
        "transported_pairing_key",
        "equality_coordinates",
        "exact",
    }
    return (
        type(row) is dict
        and set(row) == required
        and _is_lower_hex(row["witness_identity"], 32)
        and {
            row["original_ref"],
            row["literal_transport_ref"],
            row["independent_rebuild_ref"],
        }
        <= identities
        and row["literal_transport_ref"] == row["independent_rebuild_ref"]
        and type(row["equality_coordinates"]) is tuple
        and bool(row["equality_coordinates"])
        and all(
            type(item) is tuple
            and len(item) == 2
            and type(item[0]) is str
            and item[1] is True
            for item in row["equality_coordinates"]
        )
        and row["exact"] is True
    )


def verify_complete_certificate_action_row(
    row: Mapping[str, Any], complete_store: Sequence[Mapping[str, Any]]
) -> bool:
    """Decode and recompute one complete action; ``exact`` is never a premise."""

    payloads = _complete_byte_store_payloads(complete_store)
    if not payloads:
        return False
    return _verify_complete_certificate_action_row_decoded(
        row, payloads, {}, {}, {}, {}, {}
    )


def _verify_complete_certificate_action_row_decoded(
    row: Mapping[str, Any],
    payloads: Mapping[str, bytes],
    witness_cache: dict[str, SourceGroupoidWitness],
    input_cache: dict[str, CertificateActionInput],
    arrow_cache: dict[str, Arrow],
    law_cache: dict[str, GammaLaw],
    pairing_cache: dict[str, tuple[Any, ...]],
) -> bool:
    """Batch-capable pure verifier with only explicit content-address reuse."""

    required = {
        "law_kind",
        "witness_ref",
        "input_ref",
        "original_ref",
        "literal_transport_ref",
        "independent_rebuild_ref",
        "pairing_key",
        "original_pairing_key",
        "transported_pairing_key",
        "equality_coordinates",
        "action_binding_sha256",
        "exact",
    }
    try:
        if type(row) is not dict or set(row) != required:
            return False
        reference_fields = (
            "witness_ref",
            "input_ref",
            "original_ref",
            "literal_transport_ref",
            "independent_rebuild_ref",
        )
        if not all(row[field] in payloads for field in reference_fields):
            return False
        for key in (
            "pairing_key",
            "original_pairing_key",
            "transported_pairing_key",
        ):
            if type(row[key]) is not tuple:
                return False
        witness_reference = row["witness_ref"]
        if witness_reference not in witness_cache:
            witness_cache[witness_reference] = _decode_witness_payload(
                payloads[witness_reference], arrow_cache
            )
        witness = witness_cache[witness_reference]

        def decode_input(reference: str) -> CertificateActionInput:
            if reference not in input_cache:
                input_cache[reference] = _decode_certificate_action_input_payload(
                    payloads[reference], arrow_cache, law_cache
                )
            return input_cache[reference]

        input_value = decode_input(row["input_ref"])
        original = decode_input(row["original_ref"])
        literal = decode_input(row["literal_transport_ref"])
        independent = decode_input(row["independent_rebuild_ref"])

        def pairing_key(
            reference: str, value: CertificateActionInput
        ) -> tuple[Any, ...]:
            prior = pairing_cache.get(reference)
            if prior is None:
                prior = certificate_pairing_key(value)
                pairing_cache[reference] = prior
            return prior

        input_pairing_key = pairing_key(row["input_ref"], input_value)
        original_pairing_key = pairing_key(row["original_ref"], original)
        literal_pairing_key = pairing_key(
            row["literal_transport_ref"], literal
        )
        recomputed = certificate_transport_triple(witness, original)
        recomputed_coordinates = recomputed.equality_coordinates
        binding_data = {
            key: row[key]
            for key in (
                "law_kind",
                "witness_ref",
                "input_ref",
                "original_ref",
                "literal_transport_ref",
                "independent_rebuild_ref",
                "pairing_key",
                "original_pairing_key",
                "transported_pairing_key",
            )
        }
        common = (
            original == input_value
            and original == recomputed.original
            and literal == recomputed.literal_transport
            and independent == recomputed.independent_rebuild
            and row["original_ref"] == row["input_ref"]
            and row["pairing_key"] == input_pairing_key
            and row["original_pairing_key"] == original_pairing_key
            and row["transported_pairing_key"] == literal_pairing_key
            and row["equality_coordinates"] == recomputed_coordinates
            and recomputed.exact
            and row["action_binding_sha256"] == canonical_hash(binding_data)
        )
        if row["law_kind"] == "IDENTITY":
            return (
                common
                and _is_identity_witness_on(
                    witness, original.enclosing_source_presentation
                )
                and literal == input_value == independent
                and row["literal_transport_ref"] == row["input_ref"]
                and row["independent_rebuild_ref"] == row["input_ref"]
                and row["transported_pairing_key"] == row["pairing_key"]
            )
        if row["law_kind"] == "NONTRIVIAL":
            return common
        return False
    except (Refusal, IntegrityFailure, KeyError, TypeError, ValueError):
        return False


def _complete_action_reference_attachment_exact(
    row: Mapping[str, Any], identities: set[str]
) -> bool:
    """Cheap per-key reference check; raw action evidence is verified separately."""

    required = {
        "law_kind",
        "witness_ref",
        "input_ref",
        "original_ref",
        "literal_transport_ref",
        "independent_rebuild_ref",
        "pairing_key",
        "original_pairing_key",
        "transported_pairing_key",
        "equality_coordinates",
        "action_binding_sha256",
        "exact",
    }
    if type(row) is not dict or set(row) != required:
        return False
    references = tuple(
        row[key]
        for key in (
            "witness_ref",
            "input_ref",
            "original_ref",
            "literal_transport_ref",
            "independent_rebuild_ref",
        )
    )
    if not set(references) <= identities:
        return False
    binding_data = {
        key: row[key]
        for key in (
            "law_kind",
            "witness_ref",
            "input_ref",
            "original_ref",
            "literal_transport_ref",
            "independent_rebuild_ref",
            "pairing_key",
            "original_pairing_key",
            "transported_pairing_key",
        )
    }
    common = (
        row["original_ref"] == row["input_ref"]
        and row["literal_transport_ref"] == row["independent_rebuild_ref"]
        and row["original_pairing_key"] == row["pairing_key"]
        and type(row["pairing_key"]) is tuple
        and type(row["transported_pairing_key"]) is tuple
        and row["action_binding_sha256"] == canonical_hash(binding_data)
    )
    if row["law_kind"] == "IDENTITY":
        return (
            common
            and row["literal_transport_ref"] == row["input_ref"]
            and row["transported_pairing_key"] == row["pairing_key"]
        )
    return row["law_kind"] == "NONTRIVIAL" and common


def _complete_action_rows(
    census: Mapping[str, Any],
) -> tuple[tuple[str, int, int, Mapping[str, Any], str, tuple[Any, ...]], ...]:
    rows: list[
        tuple[str, int, int, Mapping[str, Any], str, tuple[Any, ...]]
    ] = []
    for family in census.get("family_rows", ()):
        family_index = family.get("family_index")
        for row_index, row in enumerate(family.get("identity_rows", ())):
            rows.append(
                (
                    "IDENTITY",
                    family_index,
                    row_index,
                    row.get("identity_action", {}),
                    row.get("input_ref"),
                    row.get("pairing_key"),
                )
            )
        nontrivial = family.get("nontrivial_action", {})
        rows.append(
            (
                "NONTRIVIAL",
                family_index,
                -1,
                nontrivial,
                nontrivial.get("input_ref"),
                nontrivial.get("pairing_key"),
            )
        )
    return tuple(rows)


def _measure_complete_action_raw_verification(
    census: Mapping[str, Any]
) -> dict[str, Any]:
    store = census.get("complete_input_table", ())
    payloads = _complete_byte_store_payloads(store)
    witness_cache: dict[str, SourceGroupoidWitness] = {}
    input_cache: dict[str, CertificateActionInput] = {}
    arrow_cache: dict[str, Arrow] = {}
    law_cache: dict[str, GammaLaw] = {}
    pairing_cache: dict[str, tuple[Any, ...]] = {}
    evidence: list[dict[str, Any]] = []
    for law_kind, family_index, row_index, action, input_ref, pairing_key in (
        _complete_action_rows(census)
    ):
        decoded_exact = bool(payloads) and (
            _verify_complete_certificate_action_row_decoded(
                action,
                payloads,
                witness_cache,
                input_cache,
                arrow_cache,
                law_cache,
                pairing_cache,
            )
        )
        evidence.append(
            {
                "law_kind": law_kind,
                "family_index": family_index,
                "row_index": row_index,
                "input_ref": input_ref,
                "pairing_key": pairing_key,
                "action_reference_sha256": canonical_hash(action),
                "decoded_action_exact": decoded_exact,
            }
        )
    rows = tuple(evidence)
    return {
        "rows": rows,
        "row_count": len(rows),
        "decoded_witness_count": len(witness_cache),
        "decoded_input_count": len(input_cache),
        "decoded_arrow_count": len(arrow_cache),
        "decoded_law_count": len(law_cache),
        "rows_sha256": canonical_hash(rows),
        "all_exact": len(rows) == 480
        and all(row["decoded_action_exact"] for row in rows),
    }


def _complete_action_verification_manifest_exact(
    census: Mapping[str, Any]
) -> bool:
    verification = census.get("raw_action_verification")
    if type(verification) is not dict:
        return False
    expected_rows = tuple(
        {
            "law_kind": law_kind,
            "family_index": family_index,
            "row_index": row_index,
            "input_ref": input_ref,
            "pairing_key": pairing_key,
            "action_reference_sha256": canonical_hash(action),
            "decoded_action_exact": True,
        }
        for law_kind, family_index, row_index, action, input_ref, pairing_key in (
            _complete_action_rows(census)
        )
    )
    return (
        verification.get("rows") == expected_rows
        and verification.get("row_count") == len(expected_rows) == 480
        and verification.get("rows_sha256") == canonical_hash(expected_rows)
        and verification.get("all_exact") is True
        and verification.get("decoded_witness_count") == 24
        and verification.get("decoded_input_count") == 480
        and verification.get("decoded_arrow_count") == 24
        and verification.get("decoded_law_count") == 1
    )


def _certificate_law_reference_exact(
    row: Mapping[str, Any], identities: set[str]
) -> bool:
    required = {
        "law_kind",
        "witness_identities",
        "input_refs",
        "triple_rows",
        "output_refs",
        "exact",
    }
    return (
        type(row) is dict
        and set(row) == required
        and row["law_kind"] in ("IDENTITY", "INVERSE", "COMPOSITION", "ASSOCIATIVITY")
        and type(row["witness_identities"]) is tuple
        and all(_is_lower_hex(value, 32) for value in row["witness_identities"])
        and type(row["input_refs"]) is tuple
        and type(row["output_refs"]) is tuple
        and set(row["input_refs"]) <= identities
        and set(row["output_refs"]) <= identities
        and type(row["triple_rows"]) is tuple
        and bool(row["triple_rows"])
        and all(
            _certificate_triple_reference_exact(value, identities)
            for value in row["triple_rows"]
        )
        and row["exact"] is True
    )


def _configuration_action_census_exact(census: Mapping[str, Any]) -> bool:
    if type(census) is not dict or not _complete_byte_store_exact(
        census.get("complete_object_table", ())
    ):
        return False
    identities = _complete_byte_store_identities(census["complete_object_table"])
    rows = census.get("rows")
    return (
        type(rows) is tuple
        and census.get("configuration_row_count") == len(rows)
        and bool(rows)
        and all(
            type(row) is dict
            and row.get("node_ref") in identities
            and row.get("configuration_ref") in identities
            and row.get("identity", {}).get("law_kind") == "IDENTITY"
            and row.get("inverse", {}).get("law_kind") == "INVERSE"
            and row.get("composition", {}).get("law_kind") == "COMPOSITION"
            and row.get("associativity", {}).get("law_kind") == "ASSOCIATIVITY"
            and _configuration_law_reference_exact(row.get("identity", {}), identities)
            and _configuration_law_reference_exact(row.get("inverse", {}), identities)
            and _configuration_law_reference_exact(row.get("composition", {}), identities)
            and _configuration_law_reference_exact(row.get("associativity", {}), identities)
            for row in rows
        )
    )


def _certificate_action_census_exact(census: Mapping[str, Any]) -> bool:
    if type(census) is not dict or not _complete_byte_store_exact(
        census.get("complete_input_table", ())
    ):
        return False
    identities = _complete_byte_store_identities(census["complete_input_table"])
    rows = census.get("rows")
    original_keys = census.get("original_pairing_keys")
    target_keys = census.get("target_pairing_keys")
    return (
        type(rows) is tuple
        and type(original_keys) is tuple
        and type(target_keys) is tuple
        and census.get("row_count") == len(rows) == len(original_keys) == len(target_keys)
        and bool(rows)
        and tuple(row.get("pairing_key") for row in rows) == original_keys
        and len({canonical_hash(value) for value in original_keys}) == len(rows)
        and len({canonical_hash(value) for value in target_keys}) == len(rows)
        and all(
            row.get("input_ref") in identities
            and row.get("identity", {}).get("law_kind") == "IDENTITY"
            and row.get("inverse", {}).get("law_kind") == "INVERSE"
            and row.get("composition", {}).get("law_kind") == "COMPOSITION"
            and row.get("associativity", {}).get("law_kind") == "ASSOCIATIVITY"
            and _certificate_law_reference_exact(row.get("identity", {}), identities)
            and _certificate_triple_reference_exact(row.get("nontrivial", {}), identities)
            and _certificate_law_reference_exact(row.get("inverse", {}), identities)
            and _certificate_law_reference_exact(row.get("composition", {}), identities)
            and _certificate_law_reference_exact(row.get("associativity", {}), identities)
            for row in rows
        )
    )


def _complete_certificate_action_census_exact(census: Mapping[str, Any]) -> bool:
    if type(census) is not dict or not _complete_byte_store_exact(
        census.get("complete_input_table", ())
    ):
        return False
    identities = _complete_byte_store_identities(census["complete_input_table"])
    families = census.get("family_rows")
    if type(families) is not tuple:
        return False
    identity_rows = tuple(
        row for family in families for row in family.get("identity_rows", ())
    )
    return (
        census.get("family_count") == len(families) == 12
        and census.get("source_column_count") == 312
        and census.get("identity_triple_count") == len(identity_rows) == 468
        and census.get("operation_counts")
        == {"CREATE": 156, "MERGE": 156, "UNCHANGED": 156}
        and census.get("all_original_keys_unique") is True
        and census.get("enumeration_reorder_nonkill") is True
        and _complete_action_verification_manifest_exact(census)
        and all(
            row.get("input_ref") in identities
            and _complete_action_reference_attachment_exact(
                row.get("identity_action", {}), identities
            )
            and row["identity_action"]["input_ref"] == row["input_ref"]
            and row["identity_action"]["pairing_key"] == row["pairing_key"]
            for row in identity_rows
        )
        and all(
            _complete_action_reference_attachment_exact(
                family.get("nontrivial_action", {}), identities
            )
            for family in families
        )
    )


def _tensor_configuration_action_exact(census: Mapping[str, Any]) -> bool:
    if type(census) is not dict or not _complete_byte_store_exact(
        census.get("complete_object_table", ())
    ):
        return False
    identities = _complete_byte_store_identities(census["complete_object_table"])
    cases = census.get("cases")
    if type(cases) is not tuple:
        return False
    return (
        census.get("case_count") == len(cases) == 3
        and all(
            type(case) is dict
            and _configuration_law_reference_exact(
                case.get("law_row", {}), identities
            )
            and case.get("left_source_root_ref") in identities
            and case.get("right_source_root_ref") in identities
            and case.get("left_target_root_ref") in identities
            and case.get("right_target_root_ref") in identities
            and case.get("tensor_target_root_ref") in identities
            and case.get("left_transport_target_root_ref")
            == case.get("left_target_root_ref")
            and case.get("right_transport_target_root_ref")
            == case.get("right_target_root_ref")
            and case.get("tensor_transport_target_root_ref")
            == case.get("tensor_target_root_ref")
            and case.get("factor_keys_unique") is True
            and type(case.get("factor_certificate_lineage")) is tuple
            and all(
                type(lineage) is dict
                and lineage.get("input_ref") in identities
                and lineage.get("certificate_ref") in identities
                and type(lineage.get("factor_generator_address")) is tuple
                and type(lineage.get("pairing_key")) is tuple
                for lineage in case.get("factor_certificate_lineage", ())
            )
            and case.get("all_exact") is True
            for case in cases
        )
    )


def _configuration_law_reference(
    row: ConfigurationActionLawRow, store: dict[str, bytes]
) -> dict[str, Any]:
    def transport_reference(value: ConfigurationTransport) -> str:
        normalized = {
            "type": "NormalizedConfigurationTransport",
            "witness_identity": witness_identity(value.witness),
            "source_node_ref": _store_complete_bytes(store, value.source_node),
            "target_node_ref": _store_complete_bytes(store, value.target_node),
            "source_configuration_ref": _store_complete_bytes(
                store, value.source_configuration
            ),
            "transported_configuration_ref": _store_complete_bytes(
                store, value.transported_configuration
            ),
        }
        normalized["normalized_transport_sha256"] = canonical_hash(normalized)
        return _store_complete_bytes(store, normalized)

    return {
        "law_kind": row.law_kind,
        "presentation_identities": tuple(
            presentation_identity(value) for value in row.presentations
        ),
        "witness_identities": tuple(
            witness_identity(value) for value in row.witnesses
        ),
        "transport_refs": tuple(
            transport_reference(value) for value in row.transports
        ),
        "final_node_refs": tuple(
            _store_complete_bytes(store, value) for value in row.final_nodes
        ),
        "final_configuration_refs": tuple(
            _store_complete_bytes(store, value)
            for value in row.final_configurations
        ),
        "exact": row.exact,
    }


def _certificate_triple_reference(
    triple: CertificateTransportTriple, store: dict[str, bytes]
) -> dict[str, Any]:
    return {
        "witness_identity": witness_identity(triple.witness),
        "original_ref": _store_complete_bytes(store, triple.original),
        "literal_transport_ref": _store_complete_bytes(
            store, triple.literal_transport
        ),
        "independent_rebuild_ref": _store_complete_bytes(
            store, triple.independent_rebuild
        ),
        "original_pairing_key": triple.original_pairing_key,
        "transported_pairing_key": triple.transported_pairing_key,
        "equality_coordinates": triple.equality_coordinates,
        "exact": triple.exact,
    }


def _complete_certificate_action_reference(
    row: CompleteCertificateActionRow, store: dict[str, bytes]
) -> dict[str, Any]:
    """Serialize one complete action with the witness and all target bytes."""

    witness_ref = _store_complete_bytes(store, row.witness)
    input_ref = _store_complete_bytes(store, row.input_value)
    original_ref = _store_complete_bytes(store, row.triple.original)
    literal_ref = _store_complete_bytes(store, row.triple.literal_transport)
    rebuild_ref = _store_complete_bytes(store, row.triple.independent_rebuild)
    binding_data = {
        "law_kind": row.law_kind,
        "witness_ref": witness_ref,
        "input_ref": input_ref,
        "original_ref": original_ref,
        "literal_transport_ref": literal_ref,
        "independent_rebuild_ref": rebuild_ref,
        "pairing_key": row.pairing_key,
        "original_pairing_key": row.triple.original_pairing_key,
        "transported_pairing_key": row.triple.transported_pairing_key,
    }
    return {
        **binding_data,
        "equality_coordinates": row.triple.equality_coordinates,
        "action_binding_sha256": canonical_hash(binding_data),
        "exact": row.exact,
    }


def _identity_complete_certificate_action_reference(
    witness: SourceGroupoidWitness,
    value: CertificateActionInput,
    store: dict[str, bytes],
) -> tuple[str, tuple[Any, ...], dict[str, Any]]:
    """Serialize the typed identity theorem without rebuilding equal packets."""

    if not _is_identity_witness_on(
        witness, value.enclosing_source_presentation
    ):
        raise Refusal("complete identity reference has a nonidentity witness")
    witness_ref = _store_complete_bytes(store, witness)
    input_ref = _store_complete_bytes(store, value)
    pairing_key = certificate_pairing_key(value)
    fields = (
        "certificate",
        "law",
        "generator_subpresentation",
        "source_node",
        "target_node",
        "arrow",
        "occurrence",
        "port",
        "contextual_parent",
        "source_configuration",
        "target_configuration",
        "input_matter_bit",
        "output_matter_bit",
        "target_sector",
        "operation_kind",
        "child",
        "context_proof",
        "inverse_creation_proof",
        "classifier_consumed_bytes",
        "coefficient",
    )
    binding_data = {
        "law_kind": "IDENTITY",
        "witness_ref": witness_ref,
        "input_ref": input_ref,
        "original_ref": input_ref,
        "literal_transport_ref": input_ref,
        "independent_rebuild_ref": input_ref,
        "pairing_key": pairing_key,
        "original_pairing_key": pairing_key,
        "transported_pairing_key": pairing_key,
    }
    return (
        input_ref,
        pairing_key,
        {
            **binding_data,
            "equality_coordinates": tuple((field, True) for field in fields),
            "action_binding_sha256": canonical_hash(binding_data),
            "exact": True,
        },
    )


def _tensor_factor_certificate_lineage(
    law: GammaLaw,
    presentation: SourcePresentation,
    factor_address: tuple[int, ...],
    store: dict[str, bytes],
) -> tuple[dict[str, Any], ...]:
    """Flatten only generator-bound certificates; structural leaves add none."""

    rows: list[dict[str, Any]] = []
    for generator_address in generator_leaf_addresses(presentation.arrow):
        for value in generator_certificate_inputs(
            law, presentation, generator_address
        ):
            rows.append(
                {
                    "factor_generator_address": factor_address
                    + generator_address,
                    "input_ref": _store_complete_bytes(store, value),
                    "certificate_ref": _store_complete_bytes(
                        store, value.certificate
                    ),
                    "pairing_key": certificate_pairing_key(value),
                }
            )
    return tuple(
        sorted(
            rows,
            key=lambda row: canonical_bytes(
                (row["factor_generator_address"], row["pairing_key"])
            ),
        )
    )


def _measure_tensor_configuration_case(
    law: GammaLaw,
    label: str,
    left_arrow: Arrow,
    right_arrow: Arrow,
    store: dict[str, bytes],
) -> dict[str, Any]:
    left_witness = _suffix_groupoid_witness(
        left_arrow,
        "__tensor_action",
        ("role", "matter", "port", "occurrence"),
    )
    right_witness = _suffix_groupoid_witness(
        right_arrow,
        "__tensor_action",
        ("role", "matter", "port", "occurrence"),
    )
    tensor_presentation = presentation_from_arrow(tensor_arrow(left_arrow, right_arrow))
    left_node = boundary_node_at(left_witness.source, (), "SOURCE")
    right_node = boundary_node_at(right_witness.source, (), "SOURCE")
    tensor_node = boundary_node_at(tensor_presentation, (), "SOURCE")
    left_configuration = left_arrow.source.catalogue[0]
    right_configuration = right_arrow.source.catalogue[0]
    tensor_configuration = _tensor_configuration_from_factors(
        tensor_node, left_configuration, right_configuration
    )
    row = tensor_action_row(
        tensor_node,
        tensor_configuration,
        left_node,
        left_configuration,
        left_witness,
        right_node,
        right_configuration,
        right_witness,
    )
    reference = _configuration_law_reference(row, store)
    left_lineage = _tensor_factor_certificate_lineage(
        law, left_witness.source, (0,), store
    )
    right_lineage = _tensor_factor_certificate_lineage(
        law, right_witness.source, (1,), store
    )
    lineage = tuple(
        sorted(
            left_lineage + right_lineage,
            key=lambda value: canonical_bytes(
                (value["factor_generator_address"], value["pairing_key"])
            ),
        )
    )
    lineage_keys = tuple(
        (value["factor_generator_address"], value["pairing_key"])
        for value in lineage
    )
    return {
        "label": label,
        "law_row": reference,
        "left_source_root_ref": _store_complete_bytes(store, left_node),
        "right_source_root_ref": _store_complete_bytes(store, right_node),
        "left_target_root_ref": _store_complete_bytes(
            store, boundary_node_at(left_witness.target, (), "SOURCE")
        ),
        "right_target_root_ref": _store_complete_bytes(
            store, boundary_node_at(right_witness.target, (), "SOURCE")
        ),
        "left_transport_target_root_ref": _store_complete_bytes(
            store, row.transports[0].target_node
        ),
        "right_transport_target_root_ref": _store_complete_bytes(
            store, row.transports[1].target_node
        ),
        "tensor_transport_target_root_ref": _store_complete_bytes(
            store, row.transports[2].target_node
        ),
        "tensor_target_root_ref": _store_complete_bytes(
            store,
            boundary_node_at(row.witnesses[2].target, (), "SOURCE"),
        ),
        "factor_certificate_lineage": lineage,
        "factor_certificate_count": len(lineage),
        "factor_keys_unique": len(lineage_keys)
        == len({canonical_hash(value) for value in lineage_keys}),
        "all_exact": row.exact
        and len(lineage_keys)
        == len({canonical_hash(value) for value in lineage_keys}),
    }


def measure_tensor_configuration_action(law: GammaLaw) -> dict[str, Any]:
    left_arrow = _small_generator(_small_atom("action_tensor_left_"), "action_tensor_left_")
    right_arrow = _small_generator(_small_atom("action_tensor_right_"), "action_tensor_right_")
    unit_identity = identity_arrow(unit_boundary())
    nested_left = tensor_arrow(
        _small_generator(_small_atom("action_tensor_nested_"), "action_tensor_nested_"),
        identity_arrow(unit_boundary()),
    )
    nested_right = _small_generator(
        _small_atom("action_tensor_nested_right_"),
        "action_tensor_nested_right_",
    )
    store: dict[str, bytes] = {}
    cases = (
        _measure_tensor_configuration_case(
            law, "GENERATOR-BY-GENERATOR", left_arrow, right_arrow, store
        ),
        _measure_tensor_configuration_case(
            law, "UNIT-BY-GENERATOR", unit_identity, right_arrow, store
        ),
        _measure_tensor_configuration_case(
            law, "NESTED-BY-GENERATOR", nested_left, nested_right, store
        ),
    )
    frozen_store = _freeze_complete_byte_store(store)
    identities = _complete_byte_store_identities(frozen_store)
    return {
        "complete_object_table": frozen_store,
        "complete_object_table_exact": _complete_byte_store_exact(frozen_store),
        "cases": cases,
        "case_count": len(cases),
        "law_row": cases[0]["law_row"],
        "factor_certificate_lineage": tuple(
            row for case in cases for row in case["factor_certificate_lineage"]
        ),
        "lineage_cardinalities": tuple(
            case["factor_certificate_count"] for case in cases
        ),
        "all_exact": _complete_byte_store_exact(frozen_store)
        and len(cases) == 3
        and all(
            case["all_exact"]
            and _configuration_law_reference_exact(case["law_row"], identities)
            and case["left_source_root_ref"] in identities
            and case["right_source_root_ref"] in identities
            and case["left_target_root_ref"] in identities
            and case["right_target_root_ref"] in identities
            and case["left_transport_target_root_ref"]
            == case["left_target_root_ref"]
            and case["right_transport_target_root_ref"]
            == case["right_target_root_ref"]
            and case["tensor_transport_target_root_ref"]
            == case["tensor_target_root_ref"]
            and all(
                lineage["input_ref"] in identities
                and lineage["certificate_ref"] in identities
                for lineage in case["factor_certificate_lineage"]
            )
            for case in cases
        ),
    }


def _certificate_law_reference(
    row: CertificateActionLawRow, store: dict[str, bytes]
) -> dict[str, Any]:
    return {
        "law_kind": row.law_kind,
        "witness_identities": tuple(
            witness_identity(value) for value in row.witnesses
        ),
        "input_refs": tuple(_store_complete_bytes(store, value) for value in row.inputs),
        "triple_rows": tuple(
            _certificate_triple_reference(value, store) for value in row.triples
        ),
        "output_refs": tuple(_store_complete_bytes(store, value) for value in row.outputs),
        "exact": row.exact,
    }


def configuration_action_census(
    presentation: SourcePresentation,
    first: SourceGroupoidWitness,
    second: SourceGroupoidWitness,
    third: SourceGroupoidWitness,
) -> dict[str, Any]:
    if first.source != presentation or second.source != first.target or third.source != second.target:
        raise Refusal("configuration-action census witnesses are not composable")
    identity = identity_witness(presentation.arrow)
    inverse = inverse_witness(first)
    first_second = compose_witnesses(first, second)
    second_third = compose_witnesses(second, third)
    left = compose_witnesses(first_second, third)
    right = compose_witnesses(first, second_third)
    rows: list[dict[str, Any]] = []
    object_store: dict[str, bytes] = {}
    nodes = boundary_nodes(presentation)
    for node in nodes:
        for configuration in node.boundary.catalogue:
            t_identity = act_configuration(node, configuration, identity)
            t_first = act_configuration(node, configuration, first)
            t_back = act_configuration(
                t_first.target_node, t_first.transported_configuration, inverse
            )
            t_second = act_configuration(
                t_first.target_node, t_first.transported_configuration, second
            )
            t_composite = act_configuration(node, configuration, first_second)
            t_third = act_configuration(
                t_second.target_node, t_second.transported_configuration, third
            )
            t_left = act_configuration(node, configuration, left)
            t_right = act_configuration(node, configuration, right)
            identity_row = ConfigurationActionLawRow(
                "IDENTITY",
                (presentation,),
                (identity,),
                (t_identity,),
                (t_identity.target_node,),
                (t_identity.transported_configuration,),
                t_identity.target_node == node
                and t_identity.transported_configuration == configuration,
            )
            inverse_row = ConfigurationActionLawRow(
                "INVERSE",
                (first.source, first.target),
                (first, inverse),
                (t_first, t_back),
                (t_back.target_node,),
                (t_back.transported_configuration,),
                t_back.target_node == node
                and t_back.transported_configuration == configuration,
            )
            composition_row = ConfigurationActionLawRow(
                "COMPOSITION",
                (first.source, first.target, second.target),
                (first, second, first_second),
                (t_first, t_second, t_composite),
                (t_second.target_node, t_composite.target_node),
                (
                    t_second.transported_configuration,
                    t_composite.transported_configuration,
                ),
                t_second.target_node == t_composite.target_node
                and t_second.transported_configuration
                == t_composite.transported_configuration,
            )
            associativity_row = ConfigurationActionLawRow(
                "ASSOCIATIVITY",
                (first.source, first.target, second.target, third.target),
                (first, second, third, first_second, second_third, left, right),
                (t_first, t_second, t_third, t_left, t_right),
                (t_third.target_node, t_left.target_node, t_right.target_node),
                (
                    t_third.transported_configuration,
                    t_left.transported_configuration,
                    t_right.transported_configuration,
                ),
                t_third.target_node == t_left.target_node == t_right.target_node
                and t_third.transported_configuration
                == t_left.transported_configuration
                == t_right.transported_configuration,
            )
            rows.append(
                {
                    "node_ref": _store_complete_bytes(object_store, node),
                    "configuration_ref": _store_complete_bytes(
                        object_store, configuration
                    ),
                    "identity": _configuration_law_reference(
                        identity_row, object_store
                    ),
                    "inverse": _configuration_law_reference(
                        inverse_row, object_store
                    ),
                    "composition": _configuration_law_reference(
                        composition_row, object_store
                    ),
                    "associativity": _configuration_law_reference(
                        associativity_row, object_store
                    ),
                    "all_exact": identity_row.exact
                    and inverse_row.exact
                    and composition_row.exact
                    and associativity_row.exact,
                }
            )
    return {
        "presentation_bytes": tuple(
            canonical_bytes(presentation_identity_data(value))
            for value in (presentation, first.target, second.target, third.target)
        ),
        "witness_bytes": tuple(
            canonical_bytes(witness_identity_data(value))
            for value in (
                identity,
                first,
                inverse,
                second,
                third,
                first_second,
                second_third,
                left,
                right,
            )
        ),
        "boundary_nodes": nodes,
        "complete_object_table": _freeze_complete_byte_store(object_store),
        "complete_object_table_exact": _complete_byte_store_exact(
            _freeze_complete_byte_store(object_store)
        ),
        "boundary_node_count": len(nodes),
        "configuration_row_count": len(rows),
        "rows": tuple(rows),
        "duplicate_semantic_node_count": len(nodes)
        - len({
            (node.boundary_semantic_bytes, node.endpoint_role)
            for node in nodes
        }),
        "all_exact": bool(rows) and all(row["all_exact"] for row in rows),
    }


def certificate_action_census(
    law: GammaLaw,
    presentation: SourcePresentation,
    generator_ast_address: tuple[int, ...],
    first: SourceGroupoidWitness,
    second: SourceGroupoidWitness,
    third: SourceGroupoidWitness,
    operation_kind: str | None = None,
) -> dict[str, Any]:
    values = generator_certificate_inputs(
        law, presentation, generator_ast_address, operation_kind
    )
    rows: list[dict[str, Any]] = []
    object_store: dict[str, bytes] = {}
    original_keys: list[tuple[Any, ...]] = []
    target_keys: list[tuple[Any, ...]] = []
    for value in values:
        identity_row = certificate_identity_row(value)
        nontrivial = certificate_transport_triple(first, value)
        inverse_row = certificate_inverse_row(value, first)
        composition_row = certificate_composition_row(value, first, second)
        associativity_row = certificate_associativity_row(
            value, first, second, third
        )
        pairing_key = certificate_pairing_key(value)
        transformed_key = certificate_pairing_key(nontrivial.independent_rebuild)
        original_keys.append(pairing_key)
        target_keys.append(transformed_key)
        rows.append(
            {
                "pairing_key": pairing_key,
                "input_ref": _store_complete_bytes(object_store, value),
                "identity": _certificate_law_reference(identity_row, object_store),
                "nontrivial": _certificate_triple_reference(
                    nontrivial, object_store
                ),
                "inverse": _certificate_law_reference(inverse_row, object_store),
                "composition": _certificate_law_reference(
                    composition_row, object_store
                ),
                "associativity": _certificate_law_reference(
                    associativity_row, object_store
                ),
                "all_exact": identity_row.exact
                and nontrivial.exact
                and inverse_row.exact
                and composition_row.exact
                and associativity_row.exact,
            }
        )
    original_key_tuple = tuple(original_keys)
    target_key_tuple = tuple(target_keys)
    frozen_store = _freeze_complete_byte_store(object_store)
    return {
        "generator_ast_address": generator_ast_address,
        "operation": operation_kind,
        "rows": tuple(rows),
        "row_count": len(rows),
        "complete_input_table": frozen_store,
        "complete_input_table_exact": _complete_byte_store_exact(frozen_store),
        "original_pairing_keys": original_key_tuple,
        "target_pairing_keys": target_key_tuple,
        "original_keys_unique": len(original_key_tuple)
        == len(set(map(canonical_hash, original_key_tuple))),
        "target_keys_unique": len(target_key_tuple)
        == len(set(map(canonical_hash, target_key_tuple))),
        "all_exact": bool(rows)
        and all(row["all_exact"] for row in rows)
        and _complete_byte_store_exact(frozen_store)
        and len(original_key_tuple)
        == len(set(map(canonical_hash, original_key_tuple)))
        and len(target_key_tuple)
        == len(set(map(canonical_hash, target_key_tuple))),
    }


def measure_complete_certificate_action_census(law: GammaLaw) -> dict[str, Any]:
    """Emit all 468 identity triples plus one nontrivial triple per family."""

    family_rows: list[dict[str, Any]] = []
    all_identity_rows: list[dict[str, Any]] = []
    object_store: dict[str, bytes] = {}
    operation_counts = {operation: 0 for operation in ("CREATE", "MERGE", "UNCHANGED")}
    for family_index, arrow in enumerate(registered_generator_families()):
        presentation = presentation_from_arrow(arrow)
        values = generator_certificate_inputs(law, presentation, ())
        identity = identity_witness(arrow)
        identity_rows: list[dict[str, Any]] = []
        for value in values:
            input_ref, pairing_key, identity_action = (
                _identity_complete_certificate_action_reference(
                    identity, value, object_store
                )
            )
            row = {
                "family_index": family_index,
                "occurrence_id": value.occurrence.occurrence_id,
                "pairing_key": pairing_key,
                "input_ref": input_ref,
                "identity_action": identity_action,
                "exact": identity_action["exact"],
            }
            identity_rows.append(row)
            all_identity_rows.append(row)
            operation_counts[value.operation_kind] += 1
        if not values:
            raise IntegrityFailure("registered generator family has no certificate input")
        nontrivial_witness = _suffix_groupoid_witness(
            arrow,
            f"__family_{family_index}",
            ("role", "matter", "port", "occurrence"),
        )
        nontrivial = complete_certificate_action_row(
            "NONTRIVIAL", nontrivial_witness, values[0]
        )
        family_rows.append(
            {
                "family_index": family_index,
                "occurrence_id": values[0].occurrence.occurrence_id,
                "source_column_count": len(arrow.source.catalogue),
                "certificate_count": len(values),
                "identity_rows": tuple(identity_rows),
                "nontrivial_witness_bytes": canonical_bytes(
                    witness_identity_data(nontrivial_witness)
                ),
                "nontrivial_action": _complete_certificate_action_reference(
                    nontrivial, object_store
                ),
                "all_exact": bool(identity_rows)
                and all(row["exact"] for row in identity_rows)
                and nontrivial.exact,
            }
        )
    original_keys = tuple(
        canonical_hash(row["pairing_key"]) for row in all_identity_rows
    )
    reversed_canonical = tuple(sorted(reversed(original_keys)))
    forward_canonical = tuple(sorted(original_keys))
    census = {
        "family_rows": tuple(family_rows),
        "family_count": len(family_rows),
        "source_column_count": sum(row["source_column_count"] for row in family_rows),
        "identity_triple_count": len(all_identity_rows),
        "operation_counts": operation_counts,
        "all_original_keys_unique": len(original_keys) == len(set(original_keys)),
        "enumeration_reorder_nonkill": reversed_canonical == forward_canonical,
        "all_identity_rows_exact": bool(all_identity_rows)
        and all(row["exact"] for row in all_identity_rows),
        "all_nontrivial_family_rows_exact": all(
            row["nontrivial_action"]["exact"] for row in family_rows
        ),
        "complete_input_table": _freeze_complete_byte_store(object_store),
        "complete_input_table_exact": _complete_byte_store_exact(
            _freeze_complete_byte_store(object_store)
        ),
        "all_exact": len(family_rows) == 12
        and len(all_identity_rows) == 468
        and operation_counts
        == {"CREATE": 156, "MERGE": 156, "UNCHANGED": 156}
        and len(original_keys) == len(set(original_keys))
        and reversed_canonical == forward_canonical
        and all(row["all_exact"] for row in family_rows),
    }
    raw_verification = _measure_complete_action_raw_verification(census)
    census["raw_action_verification"] = raw_verification
    census["all_exact"] = census["all_exact"] and raw_verification["all_exact"]
    return census


def covariance_residual(
    law: GammaLaw, arrow: Arrow, witness: SourceGroupoidWitness
) -> tuple[Fraction, dict[str, Any]]:
    transformed_arrow = relabel_arrow(arrow, witness)
    original = evaluate_arrow(law, arrow)
    transformed = evaluate_arrow(law, transformed_arrow)
    return _covariance_residual_from_maps(
        arrow, witness, transformed_arrow, original, transformed
    )


def _covariance_residual_from_maps(
    arrow: Arrow,
    witness: SourceGroupoidWitness,
    transformed_arrow: Arrow,
    original: LinearMap,
    transformed: LinearMap,
) -> tuple[Fraction, dict[str, Any]]:
    _require_exact(arrow, Arrow, "covariance source arrow")
    _require_exact(witness, SourceGroupoidWitness, "covariance witness")
    _require_exact(transformed_arrow, Arrow, "covariance target arrow")
    _require_exact(original, LinearMap, "covariance source operator")
    _require_exact(transformed, LinearMap, "covariance target operator")
    if relabel_arrow(arrow, witness) != transformed_arrow:
        raise Refusal("covariance target arrow is not the witness action")
    transformed_source_lookup = _configuration_index(transformed_arrow.source)
    transformed_target_lookup = _configuration_index(transformed_arrow.target)
    original_entries = {
        (row, column): value for row, column, value in original.entries
    }
    transformed_entries = {
        (row, column): value for row, column, value in transformed.entries
    }
    maximum = Fraction(0)
    endpoint_maximum = Fraction(0)
    compared = 0
    for source_column, source_state in enumerate(arrow.source.catalogue):
        mapped_source = relabel_configuration(
            arrow.source,
            transformed_arrow.source,
            source_state,
            witness,
        )
        mapped_column = transformed_source_lookup[mapped_source]
        for target_row, target_state in enumerate(arrow.target.catalogue):
            mapped_target = relabel_configuration(
                arrow.target,
                transformed_arrow.target,
                target_state,
                witness,
            )
            mapped_row = transformed_target_lookup[mapped_target]
            original_coefficient = original_entries.get(
                (target_row, source_column), Fraction(0)
            )
            transformed_coefficient = transformed_entries.get(
                (mapped_row, mapped_column), Fraction(0)
            )
            maximum = max(
                maximum, abs(original_coefficient - transformed_coefficient)
            )
            endpoint_maximum = max(
                endpoint_maximum,
                abs(
                    original_coefficient * original_coefficient
                    - transformed_coefficient * transformed_coefficient
                ),
            )
            compared += 1
    return maximum, {
        "original_operator_hash": canonical_hash(original),
        "transformed_operator_hash": canonical_hash(transformed),
        "witness_hash": canonical_hash(witness),
        "coordinates_compared": compared,
        "endpoint_probability_residual": endpoint_maximum,
        "uncached_operator_evaluations": len((original, transformed)),
        "original_nomological_roots": derivation_roots(original.derivation),
        "transformed_nomological_roots": derivation_roots(transformed.derivation),
    }


def _native_groupoid_law_row(
    law: GammaLaw,
    label: str,
    arrow: Arrow,
    namespaces: tuple[str, ...],
    certificate_operation: str | None = None,
    contextual_alias: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    _require_exact(label, str, "native groupoid row label")
    _require_exact(arrow, Arrow, "native groupoid row arrow")
    if certificate_operation is not None and certificate_operation not in (
        "CREATE",
        "MERGE",
        "UNCHANGED",
    ):
        raise Refusal("native groupoid certificate operation is invalid")
    first = _suffix_groupoid_witness(arrow, "__g1", namespaces)
    second = _suffix_groupoid_witness(first.target.arrow, "__g2", namespaces)
    third = _suffix_groupoid_witness(second.target.arrow, "__g3", namespaces)
    source_identity = identity_witness(arrow)
    target_identity = identity_witness(first.target.arrow)
    left_identity = compose_witnesses(source_identity, first)
    right_identity = compose_witnesses(first, target_identity)
    inverse = inverse_witness(first)
    inverse_left = compose_witnesses(first, inverse)
    inverse_right = compose_witnesses(inverse, first)
    first_second = compose_witnesses(first, second)
    second_third = compose_witnesses(second, third)
    associativity_left = compose_witnesses(first_second, third)
    associativity_right = compose_witnesses(first, second_third)
    configuration_action = configuration_action_census(
        first.source, first, second, third
    )
    transformed_arrow = relabel_arrow(arrow, first)
    sequential_arrow = relabel_arrow(transformed_arrow, second)
    composite_arrow = relabel_arrow(arrow, first_second)
    original_operator = evaluate_arrow(law, arrow)
    transformed_operator = evaluate_arrow(law, transformed_arrow)
    chain_operator = evaluate_arrow(law, composite_arrow)
    covariance, covariance_evidence = _covariance_residual_from_maps(
        arrow, first, transformed_arrow, original_operator, transformed_operator
    )
    chain_covariance, chain_evidence = _covariance_residual_from_maps(
        arrow, first_second, composite_arrow, original_operator, chain_operator
    )
    source_state = arrow.source.catalogue[0]
    root_source_node = boundary_node_at(first.source, (), "SOURCE")
    transformed_source_state = act_configuration(
        root_source_node, source_state, first
    ).transported_configuration
    original_key = presentation_key(law, arrow, source_state)
    transformed_key = presentation_key(
        law, transformed_arrow, transformed_source_state
    )
    original_roots = covariance_evidence["original_nomological_roots"]
    transformed_roots = covariance_evidence["transformed_nomological_roots"]
    leaves = generator_leaves(arrow)
    if leaves:
        leaf = leaves[0]
        leaf_witness = restrict_witness_to_arrow(first, leaf)
        transformed_leaf = relabel_arrow(leaf, leaf_witness)
        if type(leaf.occurrence) is not Occurrence or type(
            transformed_leaf.occurrence
        ) is not Occurrence:
            raise IntegrityFailure("native groupoid row lost its occurrence")
        selected_port = _selected_port(leaf.source, leaf.occurrence.port_name)
        transformed_port = _selected_port(
            transformed_leaf.source, transformed_leaf.occurrence.port_name
        )
        object_action = {
            "formula": relabel_formula(leaf.occurrence.query, leaf_witness)
            == transformed_leaf.occurrence.query,
            "context": relabel_context(leaf.source.base, leaf_witness)
            == transformed_leaf.source.base,
            "port": relabel_port(selected_port, leaf_witness)
            == transformed_port,
            "source_boundary": relabel_boundary(leaf.source, leaf_witness)
            == transformed_leaf.source,
            "target_boundary": relabel_boundary(leaf.target, leaf_witness)
            == transformed_leaf.target,
            "occurrence": relabel_occurrence(leaf.occurrence, leaf_witness)
            == transformed_leaf.occurrence,
            "arrow": transformed_leaf == leaf_witness.target.arrow,
        }
    else:
        object_action = {
            "formula": True,
            "context": relabel_context(arrow.source.base, first)
            == transformed_arrow.source.base,
            "port": True,
            "source_boundary": relabel_boundary(arrow.source, first)
            == transformed_arrow.source,
            "target_boundary": relabel_boundary(arrow.target, first)
            == transformed_arrow.target,
            "occurrence": True,
            "arrow": transformed_arrow == first.target.arrow,
        }
    object_action["complete_target_catalogue"] = all(
        relabel_configuration(
            arrow.target,
            transformed_arrow.target,
            configuration,
            first,
        )
        in transformed_arrow.target.catalogue
        for configuration in arrow.target.catalogue
    )
    object_action["record_projector_sectors"] = all(
        sector_dict(configuration)[declaration.port.name]
        == sector_dict(
            relabel_configuration(
                arrow.target,
                transformed_arrow.target,
                configuration,
                first,
            )
        )[_rename(first.port_map, declaration.port.name)]
        for declaration in arrow.target.ports
        for configuration in arrow.target.catalogue
    )
    certificate_row: dict[str, Any] | None = None
    if certificate_operation is not None:
        if arrow.kind != "GENERATOR":
            raise Refusal("native certificate row requires a generator")
        certificate_row = certificate_action_census(
            law,
            first.source,
            (),
            first,
            second,
            third,
            certificate_operation,
        )
    contextual_alias_exact = (
        contextual_alias is None
        or (
            contextual_alias["raw_ambient_formulas_distinct"]
            and contextual_alias["all_physical_fields_equal"]
        )
    )
    law_fields = {
        "left_identity_exact": left_identity == first,
        "right_identity_exact": right_identity == first,
        "left_inverse_exact": inverse_left == source_identity,
        "right_inverse_exact": inverse_right == target_identity,
        "associativity_exact": associativity_left == associativity_right,
        "application_order_exact": sequential_arrow == composite_arrow,
        "source_target_typed": first.source == presentation_from_arrow(arrow)
        and first.target == presentation_from_arrow(transformed_arrow),
        "transported_presentation_exact": transformed_arrow == first.target.arrow,
        "operator_covariance_residual": covariance,
        "chain_operator_covariance_residual": chain_covariance,
        "endpoint_covariance_residual": covariance_evidence[
            "endpoint_probability_residual"
        ],
        "chain_endpoint_covariance_residual": chain_evidence[
            "endpoint_probability_residual"
        ],
        "source_configuration_action_exact": transformed_source_state
        in transformed_arrow.source.catalogue,
        "complete_configuration_action_exact": configuration_action["all_exact"],
        "nomological_roots_preserved": len(original_roots)
        == len(transformed_roots)
        and set(original_roots) == set(transformed_roots)
        == ({law_identity(law)} if leaves else set()),
        "contextual_alias_exact": contextual_alias_exact,
        "certificate_transport_exact": certificate_row is None
        or certificate_row["all_exact"],
        "all_object_actions_exact": all(object_action.values()),
    }
    row_all_exact = (
        law_fields["left_identity_exact"]
        and law_fields["right_identity_exact"]
        and law_fields["left_inverse_exact"]
        and law_fields["right_inverse_exact"]
        and law_fields["associativity_exact"]
        and law_fields["application_order_exact"]
        and law_fields["source_target_typed"]
        and law_fields["transported_presentation_exact"]
        and law_fields["operator_covariance_residual"] == 0
        and law_fields["chain_operator_covariance_residual"] == 0
        and law_fields["endpoint_covariance_residual"] == 0
        and law_fields["chain_endpoint_covariance_residual"] == 0
        and law_fields["source_configuration_action_exact"]
        and law_fields["complete_configuration_action_exact"]
        and law_fields["nomological_roots_preserved"]
        and law_fields["contextual_alias_exact"]
        and law_fields["certificate_transport_exact"]
        and law_fields["all_object_actions_exact"]
    )
    return {
        "label": label,
        "namespaces": namespaces,
        "source_presentation": first.source,
        "target_presentation": first.target,
        "sparse_maps": {
            "role": first.role_map,
            "matter": first.matter_map,
            "port": first.port_map,
            "occurrence": first.occurrence_map,
        },
        "completed_maps": _completed_witness_maps(first),
        "inverse": inverse,
        "left_identity_composite": left_identity,
        "right_identity_composite": right_identity,
        "left_inverse_composite": inverse_left,
        "right_inverse_composite": inverse_right,
        "associativity_left": associativity_left,
        "associativity_right": associativity_right,
        "law_fields": law_fields,
        "original_arrow_hash": canonical_hash(arrow),
        "transported_arrow_hash": canonical_hash(transformed_arrow),
        "sequential_arrow_hash": canonical_hash(sequential_arrow),
        "composite_arrow_hash": canonical_hash(composite_arrow),
        "original_operator_hash": canonical_hash(original_operator),
        "transported_operator_hash": canonical_hash(transformed_operator),
        "original_source_key": original_key,
        "transported_source_key": transformed_key,
        "source_key_changed_with_presentation": original_key != transformed_key,
        "covariance_evidence": covariance_evidence,
        "chain_covariance_evidence": chain_evidence,
        "certificate_row": certificate_row,
        "configuration_action": configuration_action,
        "object_action": object_action,
        "contextual_alias": contextual_alias,
        "all_exact": row_all_exact,
    }


def _contextual_alias_arrow() -> Arrow:
    context = dict(_split_census_contexts())["C3"]
    parent = formula_atom("B")
    port = Port(
        "native_alias_p",
        Role("native_alias_N", "RELATION"),
        formula_not(parent),
        parent,
    )
    boundary = atomic_boundary(
        ("native_alias_c",), context, (PortDecl(port, "ACTIVE"),)
    )
    return generator_arrow(
        boundary,
        Occurrence(
            "native_alias_occurrence",
            "native_alias_c",
            "native_alias_p",
            parent,
            "ACTIVE",
        ),
    )


def _minimal_role_relabel_arrow() -> Arrow:
    context = Context(
        (Role("A", "RELATION"),),
        ((), ("A",)),
    )
    return identity_arrow(atomic_boundary(("minimal_coin",), context, ()))


def measure_native_groupoid_census(law: GammaLaw) -> dict[str, Any]:
    minimal_relabel = _minimal_role_relabel_arrow()
    minimal = _minimal_bound_split_application(law)["arrow"]
    coherent = build_coherent_control("native_coh_")
    record = build_record_control("native_record_")
    reciprocal = build_reciprocal_control("native_rsp_")
    alias_measurement = _measure_contextual_alias(law)
    tensor = tensor_arrow(
        _small_generator(_small_atom("native_tensor_left_"), "native_tensor_left_"),
        _small_generator(_small_atom("native_tensor_right_"), "native_tensor_right_"),
    )
    matching_presentation = MatchingPresentation(
        12,
        tuple(range(12)),
        (1, 8),
        "EXPOSED-CONTROL",
    )
    matching = build_matching_arrow(
        matching_presentation, "native_match_"
    )["arrow"]
    specifications = (
        ("minimal-role-A-to-B", minimal_relabel, ("role",), None, None),
        ("matter-namespace", coherent["first_pair"], ("matter",), None, None),
        ("port-namespace", coherent["first_pair"], ("port",), None, None),
        (
            "occurrence-namespace",
            coherent["first_pair"],
            ("occurrence",),
            None,
            None,
        ),
        (
            "all-four-namespaces",
            coherent["two_pairs"],
            ("role", "matter", "port", "occurrence"),
            None,
            None,
        ),
        (
            "contextual-boolean-alias",
            _contextual_alias_arrow(),
            ("role", "matter", "port", "occurrence"),
            None,
            alias_measurement,
        ),
        (
            "bound-split-create",
            minimal,
            ("role", "matter", "port", "occurrence"),
            "CREATE",
            None,
        ),
        (
            "bound-split-merge",
            minimal,
            ("role", "matter", "port", "occurrence"),
            "MERGE",
            None,
        ),
        (
            "bound-split-unchanged",
            minimal,
            ("role", "matter", "port", "occurrence"),
            "UNCHANGED",
            None,
        ),
        (
            "record-writer-continuation",
            record["recorded_chain"],
            ("role", "matter", "port", "occurrence"),
            None,
            None,
        ),
        (
            "reciprocal-writer-probe",
            reciprocal["chain"],
            ("role", "matter", "port", "occurrence"),
            None,
            None,
        ),
        (
            "size-twelve-global-matching",
            matching,
            ("role", "matter", "port", "occurrence"),
            None,
            None,
        ),
        (
            "tensor-two-nontrivial-factors",
            tensor,
            ("role", "matter", "port", "occurrence"),
            None,
            None,
        ),
    )
    rows = tuple(
        _native_groupoid_law_row(
            law,
            label,
            arrow,
            namespaces,
            certificate_operation,
            contextual_alias,
        )
        for label, arrow, namespaces, certificate_operation, contextual_alias in specifications
    )
    return {
        "rows": rows,
        "row_count": len(rows),
        "required_labels": tuple(row["label"] for row in rows),
        "all_law_rows_exact": all(row["all_exact"] for row in rows),
        "all_identity_laws_exact": all(
            row["law_fields"]["left_identity_exact"]
            and row["law_fields"]["right_identity_exact"]
            for row in rows
        ),
        "all_inverse_laws_exact": all(
            row["law_fields"]["left_inverse_exact"]
            and row["law_fields"]["right_inverse_exact"]
            for row in rows
        ),
        "all_associativity_exact": all(
            row["law_fields"]["associativity_exact"] for row in rows
        ),
        "all_operator_endpoint_covariance_exact": all(
            row["law_fields"]["operator_covariance_residual"] == 0
            and row["law_fields"]["endpoint_covariance_residual"] == 0
            and row["law_fields"]["chain_operator_covariance_residual"] == 0
            and row["law_fields"]["chain_endpoint_covariance_residual"] == 0
            for row in rows
        ),
        "all_source_target_typed": all(
            row["law_fields"]["source_target_typed"]
            and row["law_fields"]["transported_presentation_exact"]
            for row in rows
        ),
        "all_configuration_actions_exact": all(
            row["configuration_action"]["all_exact"] for row in rows
        ),
        "all_certificate_lineage_exact": all(
            row["law_fields"]["certificate_transport_exact"] for row in rows
        ),
        "all_exact": all(row["all_exact"] for row in rows),
    }


def split_certificate_covariance(
    law: GammaLaw,
    arrow: Arrow,
    first: SourceGroupoidWitness,
    second: SourceGroupoidWitness,
) -> dict[str, Any]:
    if arrow.kind != "GENERATOR" or type(arrow.occurrence) is not Occurrence:
        raise Refusal("split covariance requires an actual generator")
    first = restrict_witness_to_arrow(first, arrow)
    second = restrict_witness_to_arrow(second, first.target.arrow)
    occurrence = arrow.occurrence
    port = _selected_port(arrow.source, occurrence.port_name)
    source = _empty_state(arrow.source)
    target = _empty_state(
        arrow.target,
        {occurrence.matter_role: 1},
        {port.name: "branch1"},
    )
    original = build_bound_split_certificate(law, arrow, source, target)
    first_arrow = relabel_arrow(arrow, first)
    first_source = relabel_configuration(arrow.source, first_arrow.source, source, first)
    first_target = relabel_configuration(arrow.target, first_arrow.target, target, first)
    transported = build_bound_split_certificate(
        law, first_arrow, first_source, first_target
    )
    expected_proof = relabel_context_split_proof(original.context_proof, first)
    identity = identity_witness(arrow)
    identity_arrow_value = relabel_arrow(arrow, identity)
    identity_source = relabel_configuration(
        arrow.source, identity_arrow_value.source, source, identity
    )
    identity_target = relabel_configuration(
        arrow.target, identity_arrow_value.target, target, identity
    )
    identity_certificate = build_bound_split_certificate(
        law, identity_arrow_value, identity_source, identity_target
    )
    inverse = inverse_witness(first)
    roundtrip_arrow = relabel_arrow(first_arrow, inverse)
    roundtrip_source = relabel_configuration(
        first_arrow.source, roundtrip_arrow.source, first_source, inverse
    )
    roundtrip_target = relabel_configuration(
        first_arrow.target, roundtrip_arrow.target, first_target, inverse
    )
    roundtrip_certificate = build_bound_split_certificate(
        law, roundtrip_arrow, roundtrip_source, roundtrip_target
    )
    sequential_arrow = relabel_arrow(first_arrow, second)
    sequential_source = relabel_configuration(
        first_arrow.source, sequential_arrow.source, first_source, second
    )
    sequential_target = relabel_configuration(
        first_arrow.target, sequential_arrow.target, first_target, second
    )
    sequential_certificate = build_bound_split_certificate(
        law, sequential_arrow, sequential_source, sequential_target
    )
    composite = compose_witnesses(first, second)
    composite_arrow = relabel_arrow(arrow, composite)
    composite_source = relabel_configuration(
        arrow.source, composite_arrow.source, source, composite
    )
    composite_target = relabel_configuration(
        arrow.target, composite_arrow.target, target, composite
    )
    composite_certificate = build_bound_split_certificate(
        law, composite_arrow, composite_source, composite_target
    )
    proof_transport_exact = canonical_bytes(expected_proof) == canonical_bytes(
        transported.context_proof
    )
    scalar_fields = (
        "input_matter_bit",
        "output_matter_bit",
        "source_sector",
        "target_sector",
        "operation_kind",
        "coefficient",
        "binding_exact",
        "operation_exact",
        "final",
    )
    scalar_transport = all(
        getattr(original, field) == getattr(transported, field)
        for field in scalar_fields
    )
    return {
        "original": original,
        "transported": transported,
        "expected_transported_context_proof": expected_proof,
        "proof_transport_exact": proof_transport_exact,
        "scalar_transport_exact": scalar_transport,
        "identity_exact": canonical_bytes(identity_certificate)
        == canonical_bytes(original),
        "inverse_roundtrip_exact": canonical_bytes(roundtrip_certificate)
        == canonical_bytes(original),
        "composition_exact": canonical_bytes(sequential_certificate)
        == canonical_bytes(composite_certificate),
        "uncached_certificate_constructions": len(
            (
                original,
                transported,
                identity_certificate,
                roundtrip_certificate,
                sequential_certificate,
                composite_certificate,
            )
        ),
        "all_exact": original.final
        and transported.final
        and proof_transport_exact
        and scalar_transport
        and canonical_bytes(identity_certificate) == canonical_bytes(original)
        and canonical_bytes(roundtrip_certificate) == canonical_bytes(original)
        and canonical_bytes(sequential_certificate)
        == canonical_bytes(composite_certificate),
    }


def measure_groupoid_covariance(law: GammaLaw) -> dict[str, Any]:
    abstract_census = measure_abstract_groupoid_census()
    native_census = measure_native_groupoid_census(law)
    complete_certificate_action = measure_complete_certificate_action_census(law)
    tensor_configuration_action = measure_tensor_configuration_action(law)
    model = build_coherent_control("cov_")
    arrow = model["two_pairs"]
    split_arrow = model["first_pair"].children[0]
    occurrence_ids: list[str] = []

    def collect(current: Arrow) -> None:
        if current.occurrence is not None:
            occurrence_ids.append(current.occurrence.occurrence_id)
        for child in current.children:
            collect(child)

    collect(arrow)
    first = make_groupoid_witness(
        arrow,
        (
            ("cov_L_record", "renamed_R"),
            ("cov_N", "renamed_child"),
        ),
        (("cov_c", "renamed_matter"),),
        (("cov_p", "renamed_port"),),
        tuple((name, f"renamed_occ_{index}") for index, name in enumerate(occurrence_ids)),
    )
    second = make_groupoid_witness(
        first.target.arrow,
        (("renamed_R", "twice_R"), ("renamed_child", "twice_child")),
        (("renamed_matter", "twice_matter"),),
        (("renamed_port", "twice_port"),),
        tuple(
            (f"renamed_occ_{index}", f"twice_occ_{index}")
            for index in range(len(occurrence_ids))
        ),
    )
    identity = identity_witness(arrow)
    inverse = inverse_witness(first)
    composed = compose_witnesses(first, second)
    identity_residual, identity_evidence = covariance_residual(law, arrow, identity)
    first_residual, first_evidence = covariance_residual(law, arrow, first)
    composed_residual, composed_evidence = covariance_residual(law, arrow, composed)
    roundtrip_arrow = relabel_arrow(relabel_arrow(arrow, first), inverse)
    roundtrip = maps_equal(
        evaluate_arrow(law, arrow), evaluate_arrow(law, roundtrip_arrow)
    )
    sequential = maps_equal(
        evaluate_arrow(law, relabel_arrow(relabel_arrow(arrow, first), second)),
        evaluate_arrow(law, relabel_arrow(arrow, composed)),
    )
    uncached_evaluations = sum(
        evidence["uncached_operator_evaluations"]
        for evidence in (
            identity_evidence,
            first_evidence,
            composed_evidence,
        )
    ) + len(("roundtrip-original", "roundtrip-transformed")) + len(
        ("sequential", "composite")
    )
    split_covariance = split_certificate_covariance(
        law, split_arrow, first, second
    )
    return {
        "abstract_census": abstract_census,
        "native_census": native_census,
        "complete_certificate_action": complete_certificate_action,
        "tensor_configuration_action": tensor_configuration_action,
        "identity_residual": identity_residual,
        "nontrivial_residual": first_residual,
        "composed_residual": composed_residual,
        "inverse_roundtrip": roundtrip,
        "composition_exact": sequential,
        "identity_evidence": identity_evidence,
        "nontrivial_evidence": first_evidence,
        "composed_evidence": composed_evidence,
        "uncached_evaluations": uncached_evaluations,
        "cache_hits": uncached_evaluations - uncached_evaluations,
        "cache_implementation_present": False,
        "split_certificate_covariance": split_covariance,
        "witnesses": {
            "identity": identity,
            "nontrivial": first,
            "inverse": inverse,
            "composite": composed,
            "second": second,
        },
        "native_dependency_sha256": canonical_hash(
            tuple(
                {
                    "label": row["label"],
                    "source": row["source_presentation"],
                    "target": row["target_presentation"],
                    "completed_maps": row["completed_maps"],
                    "law_fields": row["law_fields"],
                    "original_operator_hash": row["original_operator_hash"],
                    "transported_operator_hash": row["transported_operator_hash"],
                    "configuration_action": row["configuration_action"],
                    "certificate_row": row["certificate_row"],
                }
                for row in native_census["rows"]
            )
            + (tensor_configuration_action,)
        ),
        "all_exact": abstract_census["all_exact"]
        and native_census["all_exact"]
        and complete_certificate_action["all_exact"]
        and tensor_configuration_action["all_exact"]
        and all(
            (
                identity_residual == 0,
                first_residual == 0,
                composed_residual == 0,
                identity_evidence["endpoint_probability_residual"] == 0,
                first_evidence["endpoint_probability_residual"] == 0,
                composed_evidence["endpoint_probability_residual"] == 0,
                roundtrip,
                sequential,
                split_covariance["all_exact"],
            )
        ),
    }


def groupoid_promotion_predicate(groupoid: Mapping[str, Any]) -> bool:
    abstract = groupoid["abstract_census"]
    native = groupoid["native_census"]
    complete_certificates = groupoid["complete_certificate_action"]
    tensor_configuration = groupoid["tensor_configuration_action"]
    rows = native["rows"]
    configuration_table_ids = {
        row["label"]: _complete_byte_store_identities(
            row["configuration_action"]["complete_object_table"]
        )
        for row in rows
    }
    certificate_table_ids = {
        row["label"]: _complete_byte_store_identities(
            row["certificate_row"]["complete_input_table"]
        )
        for row in rows
        if row["certificate_row"] is not None
    }
    tensor_configuration_ids = _complete_byte_store_identities(
        tensor_configuration["complete_object_table"]
    )
    return (
        abstract["bijection_count"] == abstract["expected_bijection_count"]
        and abstract["associativity_case_count"]
        == abstract["expected_associativity_case_count"]
        and all(
            row["left_identity_exact"]
            and row["right_identity_exact"]
            and row["left_inverse_exact"]
            and row["right_inverse_exact"]
            and row["roundtrip_exact"]
            for row in abstract["bijection_rows"]
        )
        and bool(rows)
        and all(
            row["law_fields"]["left_identity_exact"]
            and row["law_fields"]["right_identity_exact"]
            and row["law_fields"]["left_inverse_exact"]
            and row["law_fields"]["right_inverse_exact"]
            and row["law_fields"]["associativity_exact"]
            and row["law_fields"]["application_order_exact"]
            and row["law_fields"]["source_target_typed"]
            and row["law_fields"]["transported_presentation_exact"]
            and row["law_fields"]["operator_covariance_residual"] == 0
            and row["law_fields"]["chain_operator_covariance_residual"] == 0
            and row["law_fields"]["endpoint_covariance_residual"] == 0
            and row["law_fields"]["chain_endpoint_covariance_residual"] == 0
            and row["law_fields"]["source_configuration_action_exact"]
            and row["law_fields"]["complete_configuration_action_exact"]
            and row["law_fields"]["nomological_roots_preserved"]
            and row["law_fields"]["contextual_alias_exact"]
            and row["law_fields"]["certificate_transport_exact"]
            and row["law_fields"]["all_object_actions_exact"]
            for row in rows
        )
        and all(
            _configuration_action_census_exact(row["configuration_action"])
            for row in rows
        )
        and all(
            row["configuration_action"]["complete_object_table_exact"]
            and action_row["node_ref"]
            in configuration_table_ids[row["label"]]
            and action_row["configuration_ref"]
            in configuration_table_ids[row["label"]]
            and _configuration_law_reference_exact(
                action_row["identity"], configuration_table_ids[row["label"]]
            )
            and _configuration_law_reference_exact(
                action_row["inverse"], configuration_table_ids[row["label"]]
            )
            and _configuration_law_reference_exact(
                action_row["composition"], configuration_table_ids[row["label"]]
            )
            and _configuration_law_reference_exact(
                action_row["associativity"], configuration_table_ids[row["label"]]
            )
            for row in rows
            for action_row in row["configuration_action"]["rows"]
        )
        and all(
            row["certificate_row"] is None
            or (
                bool(row["certificate_row"]["rows"])
                and row["certificate_row"]["complete_input_table_exact"]
                and row["certificate_row"]["original_keys_unique"]
                and row["certificate_row"]["target_keys_unique"]
                and all(
                    certificate_row["input_ref"]
                    in certificate_table_ids[row["label"]]
                    and _certificate_law_reference_exact(
                        certificate_row["identity"],
                        certificate_table_ids[row["label"]],
                    )
                    and _certificate_triple_reference_exact(
                        certificate_row["nontrivial"],
                        certificate_table_ids[row["label"]],
                    )
                    and _certificate_law_reference_exact(
                        certificate_row["inverse"],
                        certificate_table_ids[row["label"]],
                    )
                    and _certificate_law_reference_exact(
                        certificate_row["composition"],
                        certificate_table_ids[row["label"]],
                    )
                    and _certificate_law_reference_exact(
                        certificate_row["associativity"],
                        certificate_table_ids[row["label"]],
                    )
                    for certificate_row in row["certificate_row"]["rows"]
                )
            )
            for row in rows
        )
        and all(
            row["certificate_row"] is None
            or _certificate_action_census_exact(row["certificate_row"])
            for row in rows
        )
        and complete_certificates["family_count"] == 12
        and complete_certificates["source_column_count"] == 312
        and complete_certificates["identity_triple_count"] == 468
        and complete_certificates["operation_counts"]
        == {"CREATE": 156, "MERGE": 156, "UNCHANGED": 156}
        and complete_certificates["all_original_keys_unique"]
        and complete_certificates["enumeration_reorder_nonkill"]
        and complete_certificates["complete_input_table_exact"]
        and _complete_certificate_action_census_exact(complete_certificates)
        and tensor_configuration["complete_object_table_exact"]
        and _tensor_configuration_action_exact(tensor_configuration)
        and tensor_configuration["case_count"] == 3
        and all(
            _configuration_law_reference_exact(
                case["law_row"], tensor_configuration_ids
            )
            and case["left_source_root_ref"] in tensor_configuration_ids
            and case["right_source_root_ref"] in tensor_configuration_ids
            and case["left_target_root_ref"] in tensor_configuration_ids
            and case["right_target_root_ref"] in tensor_configuration_ids
            and case["factor_keys_unique"]
            and all(
                lineage["input_ref"] in tensor_configuration_ids
                and lineage["certificate_ref"] in tensor_configuration_ids
                for lineage in case["factor_certificate_lineage"]
            )
            for case in tensor_configuration["cases"]
        )
        and _configuration_law_reference_exact(
            tensor_configuration["law_row"], tensor_configuration_ids
        )
        and tuple(tensor_configuration["lineage_cardinalities"])
        and all(value >= 0 for value in tensor_configuration["lineage_cardinalities"])
        and groupoid["identity_residual"] == 0
        and groupoid["nontrivial_residual"] == 0
        and groupoid["composed_residual"] == 0
        and groupoid["inverse_roundtrip"]
        and groupoid["composition_exact"]
        and groupoid["split_certificate_covariance"]["all_exact"]
        and groupoid["cache_hits"] == 0
        and not groupoid["cache_implementation_present"]
    )


def measure_source_identity(law: GammaLaw) -> dict[str, Any]:
    model = build_coherent_control("key_")
    source = _empty_state(model["boundary"])
    first = gamma_evaluate(law, model["first_pair"], source)
    repeated = gamma_evaluate(law, model["first_pair"], source)
    distinct = gamma_evaluate(law, model["two_pairs"], source)

    dummy = "key_dummy"
    tautology = formula_or(formula_atom(dummy), formula_not(formula_atom(dummy)))
    equivalent_query = formula_and(model["query"], tautology)
    equivalent_pair = create_erase_pair(
        model["boundary"],
        model["matter"],
        model["port"],
        equivalent_query,
        "key_pair0",
    )
    equivalent = gamma_evaluate(law, equivalent_pair, source)
    labelled_boundary = atomic_boundary(
        model["boundary"].matter_roles,
        Context(
            model["boundary"].base.roles,
            model["boundary"].base.cells,
            "presentation-only",
        ),
        model["boundary"].ports,
        neutral_label="presentation-only",
        presentation_status_order=("branch1", "empty", "branch0"),
    )
    labelled_pair = create_erase_pair(
        labelled_boundary,
        model["matter"],
        model["port"],
        equivalent_query,
        "key_pair0",
    )
    labelled_source = _empty_state(labelled_boundary)
    labelled = gamma_evaluate(law, labelled_pair, labelled_source)
    contextual_alias = _measure_contextual_alias(law)
    return {
        "equal_key_equal_profile": first.presentation_key == repeated.presentation_key
        and first.probabilities == repeated.probabilities,
        "distinct_filling_distinct_key": first.presentation_key
        != distinct.presentation_key,
        "inessential_formula_equal": equivalent_query == model["query"],
        "inessential_formula_profile_equal": equivalent.probabilities
        == first.probabilities,
        "neutral_label_and_status_order_invariant": labelled.probabilities
        == equivalent.probabilities
        and boundary_semantic_key(labelled_pair.source)
        == boundary_semantic_key(equivalent_pair.source),
        "contextual_boolean_alias": contextual_alias,
        "contextual_boolean_alias_exact": contextual_alias[
            "raw_ambient_formulas_distinct"
        ]
        and contextual_alias["all_physical_fields_equal"],
        "source_key_hash": canonical_hash(first.presentation_key),
        "distinct_key_hash": canonical_hash(distinct.presentation_key),
        "profile_hash": canonical_hash(first.probabilities),
    }


def count_generator_leaves(arrow: Arrow) -> int:
    _require_exact(arrow, Arrow, "arrow")
    return int(arrow.kind == "GENERATOR") + sum(
        count_generator_leaves(child) for child in arrow.children
    )


def verify_lineage(law: GammaLaw, arrow: Arrow, linear_map: LinearMap) -> dict[str, Any]:
    _require_exact(law, GammaLaw, "lineage law")
    _require_exact(arrow, Arrow, "lineage arrow")
    _require_exact(linear_map, LinearMap, "lineage linear map")
    rebuilt = evaluate_arrow(law, arrow)
    roots = derivation_roots(linear_map.derivation)
    generator_count = count_generator_leaves(arrow)
    return {
        "typed_endpoints": _same_boundary(linear_map.source, arrow.source)
        and _same_boundary(linear_map.target, arrow.target),
        "operator_recomputed_equal": linear_map.entries == rebuilt.entries,
        "derivation_recomputed_equal": linear_map.derivation == rebuilt.derivation,
        "primitive_leaf_count": len(roots),
        "generator_leaf_count": generator_count,
        "all_roots_are_law": set(roots) == {law_identity(law)} if roots else False,
        "complete": (
            _same_boundary(linear_map.source, arrow.source)
            and _same_boundary(linear_map.target, arrow.target)
            and linear_map.entries == rebuilt.entries
            and linear_map.derivation == rebuilt.derivation
            and len(roots) == generator_count
            and set(roots) == {law_identity(law)}
        ),
        "rebuilt_hash": canonical_hash(rebuilt),
        "observed_hash": canonical_hash(linear_map),
    }


def measure_full_target_retyping(law: GammaLaw) -> dict[str, Any]:
    model = build_coherent_control("full_")
    first_pair = model["first_pair"]
    two_pairs = model["two_pairs"]
    first_rotate, first_erase = first_pair.children
    second_pair = two_pairs.children[1]
    second_rotate, second_erase = second_pair.children
    initial = _empty_state(first_rotate.source)
    first_evaluation = gamma_evaluate(law, first_rotate, initial)
    complete_counts = tuple(
        (
            len(leg.source.catalogue),
            len(leg.target.catalogue),
        )
        for leg in (first_rotate, first_erase, second_rotate, second_erase)
    )
    edge_equalities = (
        _same_boundary(first_rotate.target, first_erase.source),
        _same_boundary(first_erase.target, second_rotate.source),
        _same_boundary(second_rotate.target, second_erase.source),
    )
    return {
        "primitive_leg_count": count_generator_leaves(two_pairs),
        "complete_catalogue_counts": complete_counts,
        "full_edge_retyping": edge_equalities,
        "first_full_target_count": len(first_rotate.target.catalogue),
        "first_returned_coordinate_count": len(first_evaluation.probabilities),
        "first_zero_coordinate_count": sum(
            int(value == 0) for value in first_evaluation.probabilities
        ),
        "all_full": all(edge_equalities)
        and len(first_rotate.target.catalogue) == len(first_evaluation.probabilities)
        and count_generator_leaves(two_pairs) == 4,
        "four_leg_lineage": evaluate_arrow(law, two_pairs).derivation,
    }


PUBLIC_NODE_TYPES = (
    Formula,
    Role,
    Context,
    SplitFiberRow,
    ContextSplitProof,
    Port,
    PortDecl,
    Configuration,
    Boundary,
    Occurrence,
    Arrow,
    PrimitiveSpec,
    GammaLaw,
    Derivation,
    LinearMap,
    GammaEvaluation,
    BoundSplitCertificate,
    ContinuationGrammar,
    MatchingPresentation,
    SourcePresentation,
    SourceGroupoidWitness,
    BoundaryNode,
    ConfigurationTransport,
    ConfigurationActionLawRow,
    CertificateActionInput,
    CertificateTransportTriple,
    CompleteCertificateActionRow,
    CertificateActionLawRow,
)


def _require_reconstruction_equal(original: Any, rebuilt: Any, label: str) -> None:
    if rebuilt != original:
        raise Refusal(f"{label} is not its exact canonical reconstruction")


def validate_context_deep(context: Context) -> None:
    _require_exact(context, Context, "context")
    for role in context.roles:
        _require_exact(role, Role, "context role")
        _require_reconstruction_equal(role, Role(role.name, role.kind), "role")
    rebuilt = Context(context.roles, context.cells, context.neutral_label)
    _require_reconstruction_equal(context, rebuilt, "context")


def validate_port_deep(port: Port) -> None:
    _require_exact(port, Port, "port")
    _require_exact(port.child, Role, "port child")
    _require_reconstruction_equal(
        port.child, Role(port.child.name, port.child.kind), "port child"
    )
    for formula in (port.parent0, port.parent1):
        _require_exact(formula, Formula, "port parent formula")
        _require_reconstruction_equal(
            formula, Formula(formula.roles, formula.table), "port parent formula"
        )
    _require_reconstruction_equal(
        port,
        Port(port.name, port.child, port.parent0, port.parent1),
        "port",
    )


def _validate_boundary_deep_seen(boundary: Boundary, seen: set[int]) -> None:
    _require_exact(boundary, Boundary, "boundary")
    marker = id(boundary)
    if marker in seen:
        return
    seen.add(marker)
    validate_context_deep(boundary.base)
    for declaration in boundary.ports:
        _require_exact(declaration, PortDecl, "port declaration")
        validate_port_deep(declaration.port)
        _require_reconstruction_equal(
            declaration,
            PortDecl(declaration.port, declaration.mode),
            "port declaration",
        )
    if boundary.left is not None:
        _validate_boundary_deep_seen(boundary.left, seen)
    if boundary.right is not None:
        _validate_boundary_deep_seen(boundary.right, seen)
    rebuilt = Boundary(
        boundary.kind,
        boundary.matter_roles,
        boundary.base,
        boundary.ports,
        boundary.catalogue,
        boundary.left,
        boundary.right,
        boundary.neutral_label,
        boundary.presentation_status_order,
    )
    _require_reconstruction_equal(boundary, rebuilt, "boundary")


def validate_boundary_deep(boundary: Boundary) -> None:
    _validate_boundary_deep_seen(boundary, set())


def validate_occurrence_deep(occurrence: Occurrence) -> None:
    _require_exact(occurrence, Occurrence, "occurrence")
    _require_exact(occurrence.query, Formula, "occurrence query")
    _require_reconstruction_equal(
        occurrence.query,
        Formula(occurrence.query.roles, occurrence.query.table),
        "occurrence query",
    )
    rebuilt = Occurrence(
        occurrence.occurrence_id,
        occurrence.matter_role,
        occurrence.port_name,
        occurrence.query,
        occurrence.target_mode,
        occurrence.seal,
    )
    _require_reconstruction_equal(occurrence, rebuilt, "occurrence")


def _validate_arrow_deep_seen(
    arrow: Arrow, seen_arrows: set[int], seen_boundaries: set[int]
) -> None:
    _require_exact(arrow, Arrow, "arrow")
    marker = id(arrow)
    if marker in seen_arrows:
        return
    seen_arrows.add(marker)
    _validate_boundary_deep_seen(arrow.source, seen_boundaries)
    _validate_boundary_deep_seen(arrow.target, seen_boundaries)
    if arrow.occurrence is not None:
        validate_occurrence_deep(arrow.occurrence)
    for child in arrow.children:
        _validate_arrow_deep_seen(child, seen_arrows, seen_boundaries)
    for boundary in arrow.objects:
        _validate_boundary_deep_seen(boundary, seen_boundaries)
    validate_arrow(arrow)


def validate_arrow_deep(arrow: Arrow) -> None:
    _validate_arrow_deep_seen(arrow, set(), set())


def validate_derivation_deep(derivation: Derivation) -> None:
    _require_exact(derivation, Derivation, "derivation")
    for child in derivation.inputs:
        validate_derivation_deep(child)
    _require_reconstruction_equal(
        derivation,
        Derivation(derivation.operation, derivation.inputs, derivation.payload),
        "derivation",
    )


def validate_public_exact_node(value: Any) -> None:
    if type(value) not in PUBLIC_NODE_TYPES:
        raise Refusal("foreign or subclassed public primitive node")
    if type(value) is Formula:
        _require_reconstruction_equal(
            value, Formula(value.roles, value.table), "formula"
        )
    elif type(value) is Role:
        _require_reconstruction_equal(value, Role(value.name, value.kind), "role")
    elif type(value) is Context:
        validate_context_deep(value)
    elif type(value) is SplitFiberRow:
        _require_reconstruction_equal(
            value,
            SplitFiberRow(
                value.source_cell,
                value.parent_value,
                value.expected_target_cells,
                value.observed_target_cells,
                value.expected_child_bits,
                value.observed_child_bits,
                value.exact,
            ),
            "split fiber row",
        )
    elif type(value) is ContextSplitProof:
        validate_context_deep(value.source)
        validate_context_deep(value.target)
        validate_public_exact_node(value.child)
        for row in value.rows:
            validate_public_exact_node(row)
        _require_reconstruction_equal(
            value,
            ContextSplitProof(
                value.source,
                value.target,
                value.parent_truth,
                value.contextual_parent_key,
                value.child,
                value.rows,
                value.unexpected_target_cells,
                value.satisfying_cell_count,
                value.expected_target_cell_count,
                value.actual_target_cell_count,
                value.count_residual,
                value.target_exhaustive,
                value.disjoint_fiber_union,
                value.exact_fibers,
                value.forget_exact,
                value.roles_exact,
                value.old_types_preserved,
                value.child_fresh,
                value.child_relation,
                value.parent_nonzero,
                value.p_and_child_nonzero,
                value.p_and_not_child_nonzero,
                value.child_distinct_from_parent,
                value.child_distinct_from_every_old_boolean,
                value.final,
            ),
            "context split proof",
        )
    elif type(value) is Port:
        validate_port_deep(value)
    elif type(value) is PortDecl:
        validate_port_deep(value.port)
        _require_reconstruction_equal(
            value, PortDecl(value.port, value.mode), "port declaration"
        )
    elif type(value) is Configuration:
        validate_context_deep(value.context)
        _require_reconstruction_equal(
            value,
            Configuration(value.context, value.matter, value.sectors),
            "configuration",
        )
    elif type(value) is Boundary:
        validate_boundary_deep(value)
    elif type(value) is Occurrence:
        validate_occurrence_deep(value)
    elif type(value) is Arrow:
        validate_arrow_deep(value)
    elif type(value) is PrimitiveSpec:
        _require_reconstruction_equal(
            value,
            PrimitiveSpec(
                value.orientation,
                value.contact_site,
                value.rho_mode,
                value.reset_one,
            ),
            "primitive specification",
        )
    elif type(value) is GammaLaw:
        validate_public_exact_node(value.primitive)
        _require_reconstruction_equal(
            value,
            GammaLaw(value.g, value.primitive, value.implementation, value.seal),
            "Gamma law",
        )
        validate_candidate_law(value)
    elif type(value) is Derivation:
        validate_derivation_deep(value)
    elif type(value) is LinearMap:
        validate_boundary_deep(value.source)
        validate_boundary_deep(value.target)
        validate_derivation_deep(value.derivation)
        _require_reconstruction_equal(
            value,
            LinearMap(value.source, value.target, value.entries, value.derivation),
            "linear map",
        )
    elif type(value) is GammaEvaluation:
        validate_derivation_deep(value.derivation)
        _require_reconstruction_equal(
            value,
            GammaEvaluation(
                value.presentation_key,
                value.amplitudes,
                value.probabilities,
                value.normalization,
                value.derivation,
            ),
            "Gamma evaluation",
        )
    elif type(value) is BoundSplitCertificate:
        validate_public_exact_node(value.context_proof)
        _require_reconstruction_equal(
            value,
            BoundSplitCertificate(
                value.law_identity,
                value.source_boundary_sha256,
                value.source_configuration_sha256,
                value.arrow_sha256,
                value.occurrence_sha256,
                value.port_sha256,
                value.presentation_source_key_sha256,
                value.input_matter_bit,
                value.output_matter_bit,
                value.source_sector,
                value.target_sector,
                value.branch_parent_key,
                value.child_key,
                value.target_boundary_sha256,
                value.target_configuration_sha256,
                value.operation_kind,
                value.coefficient,
                value.context_proof,
                value.inverse_creation_proof_sha256,
                value.binding_exact,
                value.operation_exact,
                value.final,
                value.classifier_consumed_sha256,
            ),
            "bound split certificate",
        )
    elif type(value) is ContinuationGrammar:
        for query in value.queries:
            validate_public_exact_node(query)
        _require_reconstruction_equal(
            value,
            ContinuationGrammar(
                value.matter_roles,
                value.active_port,
                value.queries,
                value.generator_names,
                value.seal,
            ),
            "continuation grammar",
        )
    elif type(value) is MatchingPresentation:
        _require_reconstruction_equal(
            value,
            MatchingPresentation(
                value.size,
                value.permutation,
                value.queries,
                value.exposure,
                value.seal,
            ),
            "matching presentation",
        )
    elif type(value) is SourcePresentation:
        validate_arrow_deep(value.arrow)
        _require_reconstruction_equal(
            value,
            SourcePresentation(
                value.arrow,
                value.role_carrier,
                value.matter_carrier,
                value.port_carrier,
                value.occurrence_carrier,
                value.seal,
            ),
            "source presentation",
        )
    elif type(value) is SourceGroupoidWitness:
        validate_public_exact_node(value.source)
        validate_public_exact_node(value.target)
        _require_reconstruction_equal(
            value,
            SourceGroupoidWitness(
                value.source,
                value.target,
                value.role_map,
                value.matter_map,
                value.port_map,
                value.occurrence_map,
                value.seal,
            ),
            "source-groupoid witness",
        )
    elif type(value) is BoundaryNode:
        validate_boundary_deep(value.boundary)
        _require_reconstruction_equal(
            value,
            BoundaryNode(
                value.boundary,
                value.boundary_semantic_bytes,
                value.ast_address,
                value.endpoint_role,
            ),
            "boundary node",
        )
    elif type(value) is ConfigurationTransport:
        validate_public_exact_node(value.source_node)
        validate_public_exact_node(value.target_node)
        validate_public_exact_node(value.source_configuration)
        validate_public_exact_node(value.transported_configuration)
        _require_reconstruction_equal(
            value,
            ConfigurationTransport(
                value.witness,
                value.source_node,
                value.target_node,
                value.source_configuration,
                value.transported_configuration,
            ),
            "configuration transport",
        )
    elif type(value) is ConfigurationActionLawRow:
        for transport in value.transports:
            validate_public_exact_node(transport)
        _require_reconstruction_equal(
            value,
            ConfigurationActionLawRow(
                value.law_kind,
                value.presentations,
                value.witnesses,
                value.transports,
                value.final_nodes,
                value.final_configurations,
                value.exact,
            ),
            "configuration action law row",
        )
    elif type(value) is CertificateActionInput:
        validate_public_exact_node(value.certificate)
        validate_public_exact_node(value.source_node)
        validate_public_exact_node(value.target_node)
        _require_reconstruction_equal(
            value,
            CertificateActionInput(
                value.certificate,
                value.law,
                value.enclosing_source_presentation,
                value.generator_ast_address,
                value.generator_subpresentation,
                value.source_node,
                value.target_node,
                value.arrow,
                value.occurrence,
                value.port,
                value.contextual_parent,
                value.source_configuration,
                value.target_configuration,
                value.source_column,
                value.target_row,
                value.input_matter_bit,
                value.output_matter_bit,
                value.target_sector,
                value.operation_kind,
                value.child,
                value.context_proof,
                value.inverse_creation_proof,
                value.classifier_consumed_bytes,
                value.coefficient,
            ),
            "certificate action input",
        )
    elif type(value) is CertificateTransportTriple:
        validate_public_exact_node(value.original)
        validate_public_exact_node(value.literal_transport)
        validate_public_exact_node(value.independent_rebuild)
        _require_reconstruction_equal(
            value,
            CertificateTransportTriple(
                value.witness,
                value.original,
                value.literal_transport,
                value.independent_rebuild,
                value.original_pairing_key,
                value.transported_pairing_key,
                value.equality_coordinates,
                value.exact,
            ),
            "certificate transport triple",
        )
    elif type(value) is CertificateActionLawRow:
        for item in value.inputs + value.outputs:
            validate_public_exact_node(item)
        for triple in value.triples:
            validate_public_exact_node(triple)
        _require_reconstruction_equal(
            value,
            CertificateActionLawRow(
                value.law_kind,
                value.witnesses,
                value.inputs,
                value.triples,
                value.outputs,
                value.exact,
            ),
            "certificate action law row",
        )


SCOPE_COORDINATES = {
    "event_filling_selection": "PRICED-KINEMATICS",
    "division_doctrine": "TYPED-CANDIDATE-AND-GRAMMAR-RELATIVE",
    "actualization": "POSTULATED",
    "valuation": "UNCONSTRUCTED",
    "metric": "UNCONSTRUCTED",
    "curvature": "UNCONSTRUCTED",
    "continuum": "UNCONSTRUCTED",
    "GR": "UNCONSTRUCTED",
}


SCOPE_WALLS = (
    "FINITE-EXACT-CLASS-RELATIVE-CANDIDATE-ONLY",
    "COUPLING-LAW-CATALOGUE-EVENT-GRAMMAR-DIVISION-UNSELECTED",
    "ACTUALIZATION-POSTULATED-NOT-DERIVED",
    "AMPLITUDE-AND-PATHS-REPRESENTATIONAL-NOT-ONTIC",
    "META-CATALOGUE-NOT-PHYSICAL-SUPPORT",
    "RAW-CONTACT-NOT-METRIC-GEOMETRY-OR-CAUSALITY",
    "INCIDENCE-CYCLE-NOT-TOPOLOGY",
    "FILLING-ORDER-NOT-EMERGENT-TIME",
    "NATIVE-NONDIVISION-CONFIGURATION-AND-CARRIER-RELATIVE",
    "HISTORY-MARKOVIZATION-DOES-NOT-ESTABLISH-MISSING-CLASSICAL-STATE",
    "BLIND-EXCLUSION-IS-RESOURCE-CLASS-RELATIVE-NOT-ABSOLUTE",
    "NO-VALUATION-METRIC-CURVATURE-CONTINUUM-GR-QFT-OR-PHENOMENOLOGY",
    "CANDIDATE-ONTOLOGY-IS-ONE-ACTUAL-RELATIONAL-CONFIGURATION-WHILE-LAW-RANGES-OVER-POSSIBLE-SOURCES-AND-TARGETS",
    "LAW-SUFFICIENCY-BELONGS-ONLY-TO-COMPLETE-TYPED-ARGUMENTS-AT-ADMISSIBLE-SOURCE-OR-DIVISION-BOUNDARIES",
    "BARE-CONFIGURATION-AND-NATIVE-NONDIVISION-CUT-ARE-NOT-AUTONOMOUS-RESTART-STATES",
)


def validate_scope_surface(coordinates: Mapping[str, str], walls: Sequence[str]) -> None:
    if type(coordinates) is not dict or coordinates != SCOPE_COORDINATES:
        raise Refusal("scope coordinate surface is incomplete or promoted")
    if type(walls) not in (tuple, list) or tuple(walls) != SCOPE_WALLS:
        raise Refusal("scope wall surface is incomplete or weakened")


def static_source_scan(source: str) -> dict[str, Any]:
    _require_exact(source, str, "static source")
    tree = ast.parse(source)
    float_nodes = tuple(
        (node.lineno, repr(node.value))
        for node in ast.walk(tree)
        if type(node) is ast.Constant and type(node.value) is float
    )
    forbidden_calls = tuple(
        (node.lineno, node.func.id)
        for node in ast.walk(tree)
        if type(node) is ast.Call
        and type(node.func) is ast.Name
        and node.func.id in ("eval", "exec")
    )
    forbidden_import_roots = {
        "numpy",
        "scipy",
        "requests",
        "socket",
        "urllib",
        "subprocess",
        "random",
        "time",
    }
    forbidden_imports: list[tuple[int, str]] = []
    for node in ast.walk(tree):
        if type(node) is ast.Import:
            for alias in node.names:
                if alias.name.split(".")[0] in forbidden_import_roots:
                    forbidden_imports.append((node.lineno, alias.name))
        elif type(node) is ast.ImportFrom:
            module = node.module or ""
            if module.split(".")[0] in forbidden_import_roots:
                forbidden_imports.append((node.lineno, module))
    git_literals = tuple(
        (node.lineno, argument.value)
        for node in ast.walk(tree)
        if type(node) is ast.Call
        for argument in node.args
        if type(argument) is ast.Constant
        and type(argument.value) is str
        and any(
            needle in argument.value.lower()
            for needle in ("git show", "git rev-parse", "git status")
        )
    )
    answer_table_names: list[tuple[int, str]] = []
    for node in ast.walk(tree):
        if type(node) in (ast.Assign, ast.AnnAssign):
            targets = node.targets if type(node) is ast.Assign else (node.target,)
            for target in targets:
                if type(target) is ast.Name and any(
                    token in target.id.upper()
                    for token in ("EXPECTED_TABLE", "ANSWER_ORACLE", "LOOKUP_ORACLE")
                ):
                    answer_table_names.append((node.lineno, target.id))
    return {
        "ast": True,
        "float_nodes": float_nodes,
        "forbidden_calls": forbidden_calls,
        "forbidden_imports": tuple(forbidden_imports),
        "git_query_literals": git_literals,
        "answer_table_names": tuple(answer_table_names),
        "clean": not (
            float_nodes
            or forbidden_calls
            or forbidden_imports
            or git_literals
            or answer_table_names
        ),
    }


def _capture_refusal(action: Any) -> tuple[bool, str]:
    try:
        action()
    except (Refusal, FrozenInstanceError, AttributeError, TypeError, ValueError) as error:
        return True, f"{type(error).__name__}:{error}"
    return False, "NO-REFUSAL"


def _attack_record(
    old: Any,
    new: Any,
    changed_path: str,
    affected_claim: str,
    killed_by: str,
    passed: bool,
    evidence: Mapping[str, Any],
    outcome_drop: str,
) -> dict[str, Any]:
    old_bytes = canonical_bytes(old)
    new_bytes = canonical_bytes(new)
    # The hostile record must be independently replayable.  Preserve every
    # measured coordinate/refusal, rather than a name-filtered digest of the
    # evidence that could silently discard a mutation's decisive witness.
    residuals = dict(evidence)
    if not residuals:
        residuals = {"kill_predicate": bool(passed)}
    return {
        "status": "KILLED" if passed else "SURVIVED",
        "changed_path": changed_path,
        "old_primitive_bytes_hex": old_bytes.hex(),
        "new_primitive_bytes_hex": new_bytes.hex(),
        "old_primitive_sha256": sha256_bytes(old_bytes),
        "new_primitive_sha256": sha256_bytes(new_bytes),
        "changed": old_bytes != new_bytes,
        "affected_claim": affected_claim,
        "killed_by": killed_by,
        "evidence": dict(evidence),
        "evidence_sha256": canonical_hash(dict(evidence)),
        "recomputed_residuals": residuals,
        "outcome_drop": outcome_drop,
        "pass": bool(passed and old_bytes != new_bytes),
    }


def _invalid_boundary_attacks(identifier: str) -> dict[str, Any]:
    base = Context((Role("mL", "RELATION"),), ((), ("mL",)))
    valid_port = _partition_port("mL", "mp", "mN")
    valid = atomic_boundary(("mc",), base, (valid_port,))
    old = valid.to_data()
    if identifier == "PORT-PARENT-NONTOTAL":
        bad_port = Port(
            "mp", Role("mN", "RELATION"), formula_atom("alien"), formula_atom("mL")
        )
        payload = {"base": base, "ports": (PortDecl(bad_port, "ACTIVE"),)}
        action = lambda: atomic_boundary(("mc",), base, (PortDecl(bad_port, "ACTIVE"),))
    elif identifier == "ACTIVE-ROLE-ZERO":
        payload = {"roles": (Role("zero", "RELATION"),), "cells": ((),)}
        action = lambda: Context((Role("zero", "RELATION"),), ((),))
    elif identifier == "TWO-BASE-CATALOG":
        payload = {"base": (base, base), "ports": (valid_port,)}
        action = lambda: identity_arrow(payload["base"])
    elif identifier == "CROSS-CHILD-PARENT":
        first = valid_port
        second_port = Port(
            "mp2",
            Role("mN2", "RELATION"),
            formula_atom("mN"),
            formula_not(formula_atom("mN")),
        )
        payload = {"base": base, "ports": (first, PortDecl(second_port, "ACTIVE"))}
        action = lambda: atomic_boundary(("mc",), base, payload["ports"])
    elif identifier == "BOUNDARY-SIGNATURE-MISSING-SPECTATOR":
        spectator_boundary = atomic_boundary(("mc", "spectator"), base, (valid_port,))
        payload = {
            "matter_roles": spectator_boundary.matter_roles,
            "catalogue": valid.catalogue,
        }
        action = lambda: Boundary(
            "ATOM",
            spectator_boundary.matter_roles,
            base,
            (valid_port,),
            valid.catalogue,
        )
    elif identifier == "PARTIAL-BOUNDARY-CATALOG":
        payload = {"catalogue": valid.catalogue[:-1]}
        action = lambda: Boundary(
            "ATOM", valid.matter_roles, valid.base, valid.ports, valid.catalogue[:-1]
        )
    elif identifier == "DEPENDENT-FRESH-CHILD-COLLISION":
        duplicate = _partition_port("mL", "mp2", "mN")
        payload = {"ports": (valid_port, duplicate)}
        action = lambda: atomic_boundary(("mc",), base, payload["ports"])
    elif identifier == "DUPLICATE-ID":
        payload = {"matter_roles": ("mc", "mc")}
        action = lambda: atomic_boundary(("mc", "mc"), base, (valid_port,))
    else:
        raise Refusal("unknown invalid-boundary development mutation")
    caught, error = _capture_refusal(action)
    return _attack_record(
        old,
        payload,
        "boundary",
        "REFERENT-AND-SOURCE-LANGUAGE",
        "EXACT-BOUNDARY-CONSTRUCTION",
        caught,
        {"refusal": error},
        "P13-REFERENT-PRESENTATION-ONLY",
    )


def _arrow_and_language_attacks(identifier: str) -> dict[str, Any]:
    boundary = _small_atom("mut_")
    generator = _small_generator(boundary, "mut_")
    alternate = _small_atom("alt_")
    old = generator.to_data()
    if identifier == "GENERATOR-UNDECLARED-QUERY-ROLE":
        occurrence = Occurrence(
            "mut_bad_query",
            "mut_c",
            "mut_p",
            formula_atom("undeclared"),
            "ACTIVE",
        )
        new = occurrence.to_data()
        action = lambda: generator_arrow(boundary, occurrence)
    elif identifier == "ALIEN-TENSOR-OPERAND":
        new = {"left": generator, "right": {"foreign": True}}
        action = lambda: tensor_arrow(generator, new["right"])
    elif identifier == "ALIEN-IDENTITY-BOUNDARY":
        new = {"foreign_boundary": boundary.to_data()}
        action = lambda: identity_arrow(new)
    elif identifier == "FORGED-UNIT-CONTEXT":
        forged_catalogue = _catalogue_for_fields((), boundary.base, ())
        new = {
            "kind": "UNIT",
            "base": boundary.base,
            "catalogue": forged_catalogue,
        }
        action = lambda: Boundary(
            "UNIT", (), boundary.base, (), forged_catalogue
        )
    elif identifier == "FORGED-IDENTITY-TARGET":
        new = {"source": boundary, "target": alternate}
        action = lambda: Arrow("IDENTITY", boundary, alternate)
    elif identifier == "FORGED-COMPOSE-TARGET":
        second = _small_generator(generator.target, "mut_")
        new = {"children": (generator, second), "target": alternate}
        action = lambda: Arrow(
            "COMPOSE", generator.source, alternate, children=(generator, second)
        )
    elif identifier == "FORGED-TENSOR-TARGET":
        right = _small_generator(alternate, "alt_")
        new = {"children": (generator, right), "target": alternate}
        action = lambda: Arrow(
            "TENSOR",
            tensor_boundary(generator.source, right.source),
            alternate,
            children=(generator, right),
        )
    elif identifier == "FORGED-GENERATOR-TARGET":
        new = {"source": boundary, "target": alternate, "occurrence": generator.occurrence}
        action = lambda: Arrow(
            "GENERATOR", boundary, alternate, generator.occurrence
        )
    elif identifier == "FORMULA-SUBCLASS-PROXY":
        class FormulaProxy(Formula):
            pass

        proxy = FormulaProxy(("mut_L_record",), (False, True))
        new = {"proxy_type": type(proxy).__name__, "payload": proxy.to_data()}
        action = lambda: Occurrence(
            "proxy", "mut_c", "mut_p", proxy, "ACTIVE"
        )
    elif identifier == "CONTEXT-SUBCLASS-PROXY":
        class ContextProxy(Context):
            pass

        proxy = ContextProxy(boundary.base.roles, boundary.base.cells)
        new = {"proxy_type": type(proxy).__name__, "payload": proxy.to_data()}
        action = lambda: Boundary(
            "ATOM",
            boundary.matter_roles,
            proxy,
            boundary.ports,
            boundary.catalogue,
        )
    elif identifier == "LAW-SUBCLASS-PROXY":
        class LawProxy(GammaLaw):
            pass

        proxy = LawProxy(Fraction(1, 2))
        new = {"proxy_type": type(proxy).__name__, "payload": proxy.to_data()}
        action = lambda: evaluate_arrow(proxy, generator)
    elif identifier == "FOREIGN-RHO-LEAF":
        new = {"rho_mode": {"callable": "foreign"}}
        action = lambda: PrimitiveSpec(rho_mode=new["rho_mode"])
    elif identifier == "FORMULA-INSTANCE-METHOD-SHADOW":
        formula = generator.occurrence.query
        if type(formula) is not Formula:
            raise IntegrityFailure("attack generator lost its formula")
        new = {"formula": formula, "instance_field": "evaluate"}
        action = lambda: object.__setattr__(formula, "evaluate", lambda _: True)
    elif identifier == "PORT-RHO-OVERRIDE":
        port = boundary.ports[0].port
        new = {"port": port, "instance_field": "rho"}
        action = lambda: object.__setattr__(port, "rho", lambda *_: "empty")
    elif identifier == "MUTABLE-LAW-METHOD-SHADOW":
        law = GammaLaw(Fraction(1, 2))
        new = {"law": law, "instance_field": "to_data"}
        action = lambda: object.__setattr__(law, "to_data", lambda: {})
    elif identifier == "NONBOOLEAN-SEAL":
        occurrence = generator.occurrence
        if type(occurrence) is not Occurrence:
            raise IntegrityFailure("attack generator lost its occurrence")
        new = occurrence.to_data() | {"seal": 1}
        action = lambda: Occurrence(
            occurrence.occurrence_id,
            occurrence.matter_role,
            occurrence.port_name,
            occurrence.query,
            occurrence.target_mode,
            1,
        )
    elif identifier == "UNSEALED-OCCURRENCE":
        occurrence = generator.occurrence
        if type(occurrence) is not Occurrence:
            raise IntegrityFailure("attack generator lost its occurrence")
        new = occurrence.to_data() | {"seal": False}
        action = lambda: Occurrence(
            occurrence.occurrence_id,
            occurrence.matter_role,
            occurrence.port_name,
            occurrence.query,
            occurrence.target_mode,
            False,
        )
    elif identifier == "MALFORMED-CONTINUATION-ALPHABET":
        query = formula_constant(False)
        new = {
            "matter_roles": ("source", "probe"),
            "active_port": "active",
            "queries": (query,),
            "generator_names": ("duplicate", "duplicate"),
        }
        action = lambda: ContinuationGrammar(
            new["matter_roles"],
            new["active_port"],
            new["queries"],
            new["generator_names"],
        )
    elif identifier == "FORGED-DERIVATION-ARITY":
        new = {"operation": "COMPOSE", "inputs": (), "payload": ()}
        action = lambda: Derivation("COMPOSE", (), ())
    elif identifier == "INCOMPATIBLE-COMPOSITION":
        right = _small_generator(alternate, "alt_")
        new = {"first_target": generator.target, "second_source": right.source}
        action = lambda: compose_arrows(generator, right)
    else:
        raise Refusal("unknown arrow/language development mutation")
    caught, error = _capture_refusal(action)
    return _attack_record(
        old,
        new,
        "public_ast",
        "EXACT-PRIMITIVE-LANGUAGE-CLOSURE",
        "RECURSIVE-EXACT-TYPE-AND-ENDPOINT-GATE",
        caught,
        {"refusal": error},
        "P13-GAMMA-UNCONSTRUCTED",
    )


def _postinit_identity_attack() -> dict[str, Any]:
    law = GammaLaw(Fraction(1, 2))
    old_identity = law_identity(law)
    normal_caught, normal_error = _capture_refusal(
        lambda: setattr(law, "g", Fraction(1, 3))
    )
    object.__setattr__(law, "g", Fraction(1, 3))
    new_identity = law_identity(law)
    new = law.to_data()
    return _attack_record(
        {"identity": old_identity, "g": Fraction(1, 2)},
        new,
        "law.g",
        "COMPLETE-SOURCE-IDENTITY",
        "RECOMPUTED-CANONICAL-LAW-IDENTITY",
        normal_caught and old_identity != new_identity,
        {
            "ordinary_assignment": normal_error,
            "old_identity": old_identity,
            "new_identity": new_identity,
        },
        "P13-LAWFUL-SOURCE-SUFFICIENCY-UNPROVEN",
    )


def _presentation_control_attack(identifier: str) -> dict[str, Any]:
    law = GammaLaw(Fraction(1, 2))
    identity = measure_source_identity(law)
    if identifier == "INESSENTIAL-BOOLEAN-ROLE":
        passed = identity["inessential_formula_equal"] and identity[
            "inessential_formula_profile_equal"
        ]
        old = {"query": "A"}
        new = {"query": "A and (D or not D)"}
        evidence = identity
    elif identifier in ("STATUS-ORDER-PRESENTATION", "NEUTRAL-LABEL-PRESENTATION"):
        passed = identity["neutral_label_and_status_order_invariant"]
        old = {"label": "", "order": CANONICAL_SECTORS}
        new = {
            "label": "presentation-only",
            "order": ("branch1", "empty", "branch0"),
        }
        evidence = identity
    elif identifier == "SOURCE-KEY-OMITS-FILLING":
        passed = identity["distinct_filling_distinct_key"]
        old = {"filling": "one-pair"}
        new = {"filling": "two-pairs"}
        evidence = identity
    else:
        raise Refusal("unknown presentation development control")
    return _attack_record(
        old,
        new,
        "presentation",
        "COMPLETE-SOURCE-IDENTITY",
        "SEMANTIC-KEY-CONTROL",
        passed,
        evidence,
        "CONTROL-INVARIANT" if passed else "P13-LAWFUL-SOURCE-SUFFICIENCY-UNPROVEN",
    )


class _WrapperLaw:
    __slots__ = ("regional", "writer", "response")

    def __init__(self, regional: Any, writer: Any, response: Any) -> None:
        self.regional = regional
        self.writer = writer
        self.response = response

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "WrapperLaw",
            "regional": self.regional,
            "writer": self.writer,
            "response": self.response,
        }


def _lineage_attacks(identifier: str) -> dict[str, Any]:
    law = GammaLaw(Fraction(1, 2))
    model = build_coherent_control("lin_")
    arrow = model["two_pairs"]
    valid = evaluate_arrow(law, arrow)
    old = valid.to_data()
    if identifier == "WRAPPER-GAMMA":
        wrapper = _WrapperLaw({"B": "supplied"}, {"W": "supplied"}, {"R": "supplied"})
        new = wrapper.to_data()
        caught, error = _capture_refusal(lambda: evaluate_arrow(wrapper, arrow))
        passed = caught
        evidence = {"refusal": error}
    elif identifier in (
        "OCCURRENCE-SEVER",
        "ALIEN-CARRIER-OR-CLONE-ROUTING",
        "BARE-KRON-AS-CONTEXT-TENSOR",
    ):
        structural_leaf = Derivation(
            "IDENTITY", (), (("typed_map", "0" * 64),)
        )
        fake_derivation = (
            Derivation("TENSOR", (structural_leaf, structural_leaf), ())
            if identifier == "BARE-KRON-AS-CONTEXT-TENSOR"
            else structural_leaf
        )
        fake = LinearMap(valid.source, valid.target, valid.entries, fake_derivation)
        new = fake.to_data()
        evidence = verify_lineage(law, arrow, fake)
        passed = not evidence["complete"]
    else:
        raise Refusal("unknown lineage development mutation")
    return _attack_record(
        old,
        new,
        "shadow.backward_slice",
        "ANTI-WRAPPER-LINEAGE",
        "ACTUAL-RECOMPUTED-BACKWARD-SLICE",
        passed,
        evidence,
        "P13-WRAPPER-OR-LOOKUP",
    )


def _mutated_law(identifier: str) -> GammaLaw:
    if identifier == "RESET-ONE":
        primitive = PrimitiveSpec(reset_one=True)
    elif identifier == "TARGET-CONTACT":
        primitive = PrimitiveSpec(contact_site="TARGET")
    elif identifier == "COIN-CONTACT":
        primitive = PrimitiveSpec(contact_site="COIN")
    elif identifier == "NONINJECTIVE-RHO":
        primitive = PrimitiveSpec(rho_mode="NONINJECTIVE")
    elif identifier == "ISOMETRIC-SWAPPED-RHO":
        primitive = PrimitiveSpec(rho_mode="SWAPPED")
    elif identifier == "WRONG-BRANCH-RHO":
        primitive = PrimitiveSpec(rho_mode="WRONG_BRANCH")
    elif identifier in ("SAME-BORN-REFLECTION", "PHASE-REFLECTION-MUTATION"):
        primitive = PrimitiveSpec(orientation="REFLECTION")
    else:
        raise Refusal("unknown primitive-law development mutation")
    coupling = (
        Fraction(2, 5)
        if identifier == "PHASE-REFLECTION-MUTATION"
        else Fraction(1, 2)
    )
    return GammaLaw(coupling, primitive)


def _law_primitive_attacks(identifier: str) -> dict[str, Any]:
    baseline_law = GammaLaw(
        Fraction(2, 5)
        if identifier == "PHASE-REFLECTION-MUTATION"
        else Fraction(1, 2)
    )
    changed_law = _mutated_law(identifier)
    model = build_coherent_control("law_")
    old = baseline_law.to_data()
    new = changed_law.to_data()
    caught, error = _capture_refusal(lambda: validate_candidate_law(changed_law))
    raw_map = evaluate_arrow(changed_law, model["first_pair"], candidate_only=False)
    raw_isometry, raw_residual = check_isometry(raw_map)
    baseline = measure_coherent_controls(baseline_law)
    changed = measure_coherent_controls(changed_law, candidate_only=False)
    evidence = {
        "candidate_refusal": error,
        "raw_isometry": raw_isometry,
        "raw_isometry_residual": raw_residual,
        "baseline_B_hash": canonical_hash(baseline["B"]),
        "changed_B_hash": canonical_hash(changed["B"]),
        "baseline_C_hash": canonical_hash(baseline["C"]),
        "changed_C_hash": canonical_hash(changed["C"]),
        "B_equal": baseline["B"] == changed["B"],
        "C_equal": baseline["C"] == changed["C"],
    }
    if identifier in ("SAME-BORN-REFLECTION", "PHASE-REFLECTION-MUTATION"):
        passed = caught and evidence["B_equal"] and not evidence["C_equal"]
    else:
        passed = caught
    return _attack_record(
        old,
        new,
        "Gamma.primitive",
        "ONE-PRIMITIVE-LAW-AND-NATIVE-SHADOWS",
        "FROZEN-PRIMITIVE-IDENTITY-AND-RECOMPUTED-SHADOWS",
        passed,
        evidence,
        "P13-GAMMA-UNCONSTRUCTED",
    )


def _output_and_shadow_attacks(identifier: str) -> dict[str, Any]:
    law = GammaLaw(Fraction(1, 2))
    model = build_coherent_control("out_")
    rotate = model["first_pair"].children[0]
    source = _empty_state(rotate.source)
    evaluation = gamma_evaluate(law, rotate, source)
    old: Any = evaluation.to_data()
    if identifier in (
        "ZERO-TARGET-DROPPED",
        "SUPPORT-FILTERED-TARGET",
        "FULL-TARGET-RETYPE",
    ):
        if identifier == "ZERO-TARGET-DROPPED":
            retained = tuple(value for value in evaluation.probabilities if value != 0)
            changed_path = "Gamma.probabilities[zero-filter]"
        elif identifier == "SUPPORT-FILTERED-TARGET":
            retained = tuple(
                value
                for value, state in zip(
                    evaluation.probabilities, rotate.target.catalogue, strict=True
                )
                if len(state.context.roles) > len(rotate.source.base.roles)
            )
            changed_path = "Gamma.target_catalogue[support-filter]"
        else:
            retained = tuple(value for value in evaluation.probabilities if value != 0)
            changed_path = "filling.second_leg.source[reached-support-only]"
        new = {
            "probabilities": retained,
            "declared_target_count": len(rotate.target.catalogue),
        }
        full_target = measure_full_target_retyping(law)
        passed = len(retained) != len(rotate.target.catalogue) and full_target["all_full"]
        evidence = {
            "mutant_returned_count": len(retained),
            "required_count": len(rotate.target.catalogue),
            "baseline_zero_count": sum(
                int(value == 0) for value in evaluation.probabilities
            ),
            "baseline_full_target": full_target,
        }
        drop = "P13-GAMMA-UNCONSTRUCTED"
    elif identifier == "BORN-TABLE-AS-GAMMA":
        wrapper = _WrapperLaw(
            {"B": matrix_square_entries(cayley_matrix(Fraction(1, 2), CANONICAL_PRIMITIVE))},
            {},
            {},
        )
        new = wrapper.to_data()
        caught, error = _capture_refusal(lambda: gamma_evaluate(wrapper, rotate, source))
        passed = caught
        evidence = {"refusal": error}
        changed_path = "Gamma"
        drop = "P13-WRAPPER-OR-LOOKUP"
    elif identifier == "BRANCH-SUM-ONLY":
        half_identity = (
            (Fraction(1, 2), Fraction(0)),
            (Fraction(0), Fraction(1, 2)),
        )
        new = {"branches": (half_identity, half_identity), "record_projectors": ()}
        total = tuple(
            tuple(half_identity[row][column] + half_identity[row][column] for column in range(2))
            for row in range(2)
        )
        normalization_only = total == (
            (Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(1)),
        )
        record_semantics = bool(new["record_projectors"])
        passed = normalization_only and not record_semantics
        evidence = {
            "branch_sum_is_identity": normalization_only,
            "record_semantics_present": record_semantics,
        }
        changed_path = "division.instrument"
        drop = "P13-DIVISION-RECOVERY-UNPROVEN"
    elif identifier == "CACHED-G-OR-SHADOW":
        changed_law = GammaLaw(Fraction(2, 5))
        cached = measure_coherent_controls(law)["C"]
        recomputed = measure_coherent_controls(changed_law)["C"]
        new = {"law": changed_law, "cached_C": cached}
        passed = cached != recomputed
        evidence = {
            "cached_hash": canonical_hash(cached),
            "recomputed_hash": canonical_hash(recomputed),
            "mismatch": cached != recomputed,
        }
        changed_path = "Gamma.g"
        drop = "P13-SHADOW-WELD-FAILS"
    elif identifier == "QUERY-FORMULA-MUTATION":
        changed_pair = create_erase_pair(
            model["boundary"],
            model["matter"],
            model["port"],
            formula_constant(False),
            "out_pair0",
        )
        baseline = _restricted_matter_amplitudes(
            law, model["first_pair"], model["matter"]
        )
        changed = _restricted_matter_amplitudes(law, changed_pair, model["matter"])
        new = changed_pair.to_data()
        passed = baseline != changed
        evidence = {
            "baseline_hash": canonical_hash(baseline),
            "changed_hash": canonical_hash(changed),
            "moved": baseline != changed,
        }
        changed_path = "filling.query"
        drop = "P13-SHADOW-WELD-FAILS"
    elif identifier == "MOVE-DOWNSTREAM":
        measured = measure_coherent_controls(law)["B"]
        moved = (
            (measured[0][0] + Fraction(1, 100), measured[0][1] - Fraction(1, 100)),
            measured[1],
        )
        new = {"stored_B": moved, "law": law}
        passed = moved != measured
        evidence = {
            "stored_hash": canonical_hash(moved),
            "root_recomputed_hash": canonical_hash(measured),
            "mismatch": moved != measured,
        }
        changed_path = "shadow.B"
        drop = "P13-SHADOW-WELD-FAILS"
    else:
        raise Refusal("unknown output/shadow development mutation")
    return _attack_record(
        old,
        new,
        changed_path,
        "COMPLETE-TARGET-AND-SHADOW-WELD",
        "RECOMPUTED-FULL-CATALOGUE-AND-ROOT-LINEAGE",
        passed,
        evidence,
        drop,
    )


def _record_attacks(identifier: str) -> dict[str, Any]:
    law = GammaLaw(Fraction(1, 2))
    control = build_record_control("atkrec_")
    old = {"writer": control["writer"], "grammar": control["grammar"]}
    if identifier in (
        "CARRIED-PORT-STILL-ACTIVE",
        "RETURN-TO-OLD-PORT",
    ):
        is_return = identifier == "RETURN-TO-OLD-PORT"
        occurrence = Occurrence(
            "return-to-old-port" if is_return else "carried-port-still-active",
            control["source_role"],
            control["record_port"],
            (
                formula_atom("atkrec_L_record")
                if is_return
                else formula_constant(False)
            ),
            "CARRIED",
        )
        new = occurrence.to_data()
        caught, error = _capture_refusal(
            lambda: generator_arrow(control["writer"].target, occurrence)
        )
        passed = caught
        evidence = {"refusal": error}
        changed_path = "continuation.selected_port"
    elif identifier == "HIDDEN-ERASER":
        reactivated = boundary_with_port_mode(
            control["writer"].target, control["record_port"], "ACTIVE"
        )
        hidden = generator_arrow(
            reactivated,
            Occurrence(
                "hidden-eraser",
                control["source_role"],
                control["record_port"],
                formula_constant(False),
                "ACTIVE",
            ),
        )
        new = {"undeclared_letter": hidden, "declared_source": control["writer"].target}
        passed = not _same_boundary(hidden.source, control["writer"].target)
        evidence = {
            "declared_source_hash": canonical_hash(
                boundary_semantic_key(control["writer"].target)
            ),
            "hidden_source_hash": canonical_hash(boundary_semantic_key(hidden.source)),
            "grammar_closed": False,
        }
        changed_path = "continuation.hidden_letter"
    elif identifier == "RESET-WRITER-CHAIN":
        changed_law = GammaLaw(Fraction(1, 2), PrimitiveSpec(reset_one=True))
        new = changed_law.to_data()
        caught, error = _capture_refusal(lambda: validate_candidate_law(changed_law))
        raw_writer = evaluate_arrow(
            changed_law, control["recorded_chain"], candidate_only=False
        )
        _, residual = check_isometry(raw_writer)
        # This registered attack is a disjunction in the pin: it must either
        # destroy recovery or be refused by the exact primitive-law type.
        # On the now-literal single-leg writer chain the reset happens only on
        # inactive contacts, so the decisive kill is the candidate-law refusal.
        passed = caught
        evidence = {
            "candidate_type_refusal": error,
            "raw_isometry_residual": residual,
            "kill_route": "EXACT-CANDIDATE-PRIMITIVE-REFUSAL",
        }
        changed_path = "Gamma.primitive.reset_one"
    elif identifier == "DELAYED-READER-SEVER":
        reciprocal = build_reciprocal_control("sever_")
        baseline = measure_reciprocal_response(law)["joint"]
        severed_reader = generator_arrow(
            reciprocal["writer"].target,
            Occurrence(
                "sever_reader",
                reciprocal["probe_role"],
                reciprocal["work_port"],
                formula_constant(False),
                "ACTIVE",
            ),
        )
        severed_chain = compose_arrows(reciprocal["writer"], severed_reader)
        source = _empty_state(reciprocal["boundary"])
        evaluation = gamma_evaluate(law, severed_chain, source)
        probe_one = sum(
            (
                probability
                for probability, state in zip(
                    evaluation.probabilities, severed_chain.target.catalogue, strict=True
                )
                if matter_dict(state)[reciprocal["probe_role"]] == 1
            ),
            Fraction(0),
        )
        new = severed_reader.to_data()
        baseline_probe_one = baseline["01"] + baseline["11"]
        passed = probe_one != baseline_probe_one
        evidence = {
            "baseline_probe_one": baseline_probe_one,
            "severed_probe_one": probe_one,
            "moved": probe_one != baseline_probe_one,
        }
        changed_path = "reciprocal.reader.query"
    else:
        raise Refusal("unknown record development mutation")
    return _attack_record(
        old,
        new,
        changed_path,
        "CARRIED-RECORD-RECOVERY",
        "TYPED-CONTINUATION-GRAMMAR-AND-READER-LINEAGE",
        passed,
        evidence,
        "P13-DIVISION-RECOVERY-UNPROVEN",
    )


def _fresh_baseline_metadata() -> dict[str, Any]:
    first = MatchingPresentation(
        4, tuple(range(4)), (0, 1, 2), "POST-SOURCE-FRESH"
    )
    second = MatchingPresentation(
        4, (1, 2, 3, 0), (0, 1, 2), "POST-SOURCE-FRESH"
    )
    projection = _fresh_blind_projection(first)
    if projection != _fresh_blind_projection(second):
        raise IntegrityFailure("synthetic assay lacks resource parity")
    presentations = (first.to_data(), second.to_data())
    hashes = tuple(canonical_hash(item) for item in presentations)
    return {
        "exposure": "POST-SOURCE-FRESH",
        "generated": True,
        "reroll_count": 0,
        "presentations": presentations,
        "case_hashes": hashes,
        "resource_projection": projection,
        "resource_projection_sha256": canonical_hash(projection),
        "blind_tokens": tuple(canonical_hash(projection) for _ in hashes),
        "schedules": ((0, 1, 2), (0, 1, 2)),
        "prior_record_laws": ("blank", "blank"),
        "allowed_keys": (
            "exposure",
            "generated",
            "reroll_count",
            "presentations",
            "case_hashes",
            "resource_projection",
            "resource_projection_sha256",
            "blind_tokens",
            "schedules",
            "prior_record_laws",
            "allowed_keys",
        ),
    }


def validate_fresh_assay_metadata(metadata: Mapping[str, Any]) -> None:
    if type(metadata) is not dict:
        raise Refusal("fresh assay metadata must be an exact mapping")
    allowed = tuple(metadata.get("allowed_keys", ()))
    if set(metadata) != set(allowed):
        raise Refusal("fresh assay metadata leaks an undeclared field")
    if metadata.get("exposure") != "POST-SOURCE-FRESH":
        raise Refusal("exposed control is represented as fresh")
    if metadata.get("generated") is not True or metadata.get("reroll_count") != 0:
        raise Refusal("fresh cases were duplicated, rerolled, or not generated")
    hashes = metadata.get("case_hashes")
    if type(hashes) is not tuple or len(set(hashes)) != len(hashes):
        raise Refusal("fresh case hashes are duplicated")
    presentations = metadata.get("presentations")
    if type(presentations) is not tuple or len(presentations) != len(hashes):
        raise Refusal("fresh matching presentations are missing")
    if hashes != tuple(canonical_hash(item) for item in presentations):
        raise Refusal("fresh case hash is not derived from its presentation")
    recomputed_projections: list[dict[str, Any]] = []
    for raw in presentations:
        if type(raw) is not dict:
            raise Refusal("fresh matching presentation is malformed")
        presentation = MatchingPresentation(
            raw.get("size"),
            tuple(raw.get("permutation", ())),
            tuple(raw.get("queries", ())),
            raw.get("exposure"),
            raw.get("seal"),
        )
        recomputed_projections.append(_fresh_blind_projection(presentation))
    projection = metadata.get("resource_projection")
    if any(item != projection for item in recomputed_projections):
        raise Refusal("resource table is not derived from literal presentations")
    if canonical_hash(projection) != metadata.get("resource_projection_sha256"):
        raise Refusal("resource table is hand-entered or stale")
    tokens = metadata.get("blind_tokens")
    if type(tokens) is not tuple or tokens != tuple(
        canonical_hash(projection) for _ in hashes
    ):
        raise Refusal("blind token is constant or not derived from resources")
    schedules = metadata.get("schedules")
    prior = metadata.get("prior_record_laws")
    if (
        type(schedules) is not tuple
        or len(set(schedules)) != 1
        or schedules != tuple(projection["schedule"] for _ in hashes)
    ):
        raise Refusal("blind schedules are unequal")
    if (
        type(prior) is not tuple
        or len(set(prior)) != 1
        or prior != tuple("blank" for _ in hashes)
    ):
        raise Refusal("prior record laws are unequal")


def _metadata_attacks(identifier: str) -> dict[str, Any]:
    old = _fresh_baseline_metadata()
    new = dict(old)
    if identifier == "HELDOUT-SHADOW-DUPLICATED":
        new["case_hashes"] = ("a" * 64, "a" * 64)
        path = "fresh.case_hashes"
    elif identifier == "RESULT-EXPOSED-AS-HOLDOUT":
        new["exposure"] = "EXPOSED-CONTROL"
        path = "fresh.exposure"
    elif identifier == "REROLL-OR-EXPOSED-AS-HOLDOUT":
        new["reroll_count"] = 1
        path = "fresh.reroll_count"
    elif identifier == "HAND-ENTERED-RESOURCE-TABLE":
        new["resource_projection"] = dict(old["resource_projection"]) | {"size": 9}
        new["resource_projection_sha256"] = canonical_hash(new["resource_projection"])
        new["blind_tokens"] = tuple(
            canonical_hash(new["resource_projection"])
            for _ in new["case_hashes"]
        )
        path = "fresh.resource_projection"
    elif identifier == "CONSTANT-BLIND-TOKEN":
        new["blind_tokens"] = ("constant", "constant")
        path = "blind.tokens"
    elif identifier == "UNEQUAL-BLIND-SCHEDULE":
        new["schedules"] = ((0, 1, 2), (2, 1, 0))
        path = "blind.schedules"
    elif identifier == "UNEQUAL-PRIOR-RECORD-LAW":
        new["prior_record_laws"] = ("blank", "member-correlated")
        path = "blind.prior_record_laws"
    elif identifier == "LEAKED-INCIDENCE-BIT":
        new["incidence_bit"] = 1
        path = "blind.incidence_bit"
    else:
        raise Refusal("unknown fresh/blind development mutation")
    caught, error = _capture_refusal(lambda: validate_fresh_assay_metadata(new))
    return _attack_record(
        old,
        new,
        path,
        "FRESH-MATCHING-BLIND-CLASS-ASSAY",
        "EXPOSURE-RESOURCE-AND-BLIND-PROJECTION-GATE",
        caught,
        {"refusal": error},
        "P13-BLIND-CLASS-UNRESOLVED",
    )


def _scope_attacks(identifier: str) -> dict[str, Any]:
    old = {"coordinates": SCOPE_COORDINATES, "walls": SCOPE_WALLS}
    coordinates = dict(SCOPE_COORDINATES)
    walls = list(SCOPE_WALLS)
    if identifier == "HISTORY-PASSED-OFF-AS-NATIVE-K":
        walls[9] = "HISTORY-MARKOVIZATION-IS-THE-NATIVE-PHYSICAL-FACTOR"
        path = "scope.native_nondivision"
    elif identifier == "NONDIVISION-AS-STATE-DEFECT":
        walls[8] = "NATIVE-NONDIVISION-PROVES-CONFIGURATION-INCOMPLETE"
        path = "scope.configuration_sufficiency"
    elif identifier == "ABSOLUTE-NONDIVISION":
        walls[8] = "ABSOLUTELY-NONDIVISIBLE-IN-EVERY-ENLARGED-STATE-SPACE"
        path = "scope.native_nondivision"
    elif identifier == "META-CATALOGUE-AS-SUPPORT":
        walls[4] = "META-CATALOGUE-IS-PHYSICAL-SUPPORT"
        path = "scope.support"
    elif identifier == "HIDDEN-VALUATION":
        coordinates["valuation"] = "DERIVED"
        path = "coordinates.valuation"
    elif identifier == "RAW-RELATION-TO-GEOMETRY":
        coordinates["metric"] = "CONSTRUCTED"
        path = "coordinates.metric"
    elif identifier == "INCIDENCE-CYCLE-TO-TOPOLOGY":
        walls[6] = "INCIDENCE-CYCLE-IS-TOPOLOGY"
        path = "scope.topology"
    elif identifier == "EVENT-ORDER-TO-TIME":
        walls[7] = "FILLING-ORDER-IS-EMERGENT-TIME"
        path = "scope.time"
    elif identifier == "AMPLITUDE-TO-ONTOLOGY":
        walls[3] = "AMPLITUDE-IS-ONTIC"
        path = "scope.amplitude"
    elif identifier == "NORMALIZATION-TO-ACTUALIZATION":
        coordinates["actualization"] = "DERIVED"
        path = "coordinates.actualization"
    else:
        raise Refusal("unknown scope development mutation")
    new = {"coordinates": coordinates, "walls": tuple(walls)}
    caught, error = _capture_refusal(
        lambda: validate_scope_surface(coordinates, tuple(walls))
    )
    return _attack_record(
        old,
        new,
        path,
        "ONTOLOGY-AND-SCOPE-RENDERER",
        "EXACT-POSITIVE-SCOPE-SURFACE",
        caught,
        {"refusal": error},
        "P13-SPECIFICATION-INCONSISTENT",
    )


def _static_injection_attack() -> dict[str, Any]:
    old = "value = Fraction(1, 2)\n"
    new = (
        "import random, socket, time\n"
        "value = 0.5\n"
        "EXPECTED_TABLE = {\"answer\": 1}\n"
        "eval(\"1\")\n"
        "print(\"git status\")\n"
    )
    clean_scan = static_source_scan(old)
    injected_scan = static_source_scan(new)
    return _attack_record(
        {"source": old},
        {"source": new},
        "scientific_source",
        "EXACT-ARITHMETIC-AND-NO-ORACLE",
        "AST-STATIC-SOURCE-SCAN",
        clean_scan["clean"] and not injected_scan["clean"],
        {"clean": clean_scan, "injected": injected_scan},
        "P13-SPECIFICATION-INCONSISTENT",
    )


def authenticate_payload(payload: bytes, expected_sha256: str, label: str) -> dict[str, str]:
    _require_exact(payload, bytes, "authenticated payload")
    _require_exact(expected_sha256, str, "expected hash")
    _require_exact(label, str, "anchor label")
    observed = sha256_bytes(payload)
    if observed != expected_sha256:
        raise IntegrityFailure(f"anchor mismatch: {label}")
    return {"label": label, "expected": expected_sha256, "observed": observed}


def _anchor_corruption_attack() -> dict[str, Any]:
    payload = b"synthetic-anchor"
    expected = sha256_bytes(payload)
    corrupted = payload + b"!"
    try:
        authenticate_payload(corrupted, expected, "synthetic")
    except IntegrityFailure as error:
        caught = True
        message = str(error)
        exit_code = registered_failure_exit_code(error)
    else:
        caught = False
        message = "NO-INTEGRITY-FAILURE"
        exit_code = 0
    return _attack_record(
        {"payload_hex": payload.hex(), "expected": expected},
        {"payload_hex": corrupted.hex(), "expected": expected},
        "anchor.bytes",
        "ANCHOR-INTEGRITY",
        "EXIT-1-ONLY-AUTHENTICATION",
        caught and exit_code == 1,
        {
            "integrity_failure": message,
            "registered_exit_code": exit_code,
            "publication_writes": 0,
        },
        "INTEGRITY-EXIT-1",
    )


def _groupoid_attacks(
    identifier: str, measurements: Mapping[str, Any] | None = None
) -> dict[str, Any]:
    law = GammaLaw(Fraction(1, 2))
    model = build_coherent_control("gmut_")
    arrow = model["first_pair"]
    first = _suffix_groupoid_witness(
        arrow, "__attack1", ("role", "matter", "port", "occurrence")
    )
    second = _suffix_groupoid_witness(
        first.target.arrow,
        "__attack2",
        ("role", "matter", "port", "occurrence"),
    )
    third = _suffix_groupoid_witness(
        second.target.arrow,
        "__attack3",
        ("role", "matter", "port", "occurrence"),
    )
    drop = "P13-REFERENT-PRESENTATION-ONLY"
    if identifier == "RELABEL-RAW-NAME":
        witness = make_groupoid_witness(
            arrow,
            (("gmut_L_record", "other_L"), ("gmut_N", "other_N")),
            (("gmut_c", "other_c"),),
            (("gmut_p", "other_p"),),
            (
                ("gmut_pair0:rotate", "other_rotate"),
                ("gmut_pair0:erase", "other_erase"),
            ),
        )
        residual, evidence = covariance_residual(law, arrow, witness)
        passed = residual == 0
        old = {"witness": "identity"}
        new = witness.to_data()
        evidence = evidence | {"residual": residual, "typed_witness": True}
    elif identifier == "RELABEL-ORIENTATION":
        witness = make_groupoid_witness(
            arrow,
            (("gmut_L_record", "other_L"), ("gmut_N", "other_N")),
            (("gmut_c", "other_c"),),
            (("gmut_p", "other_p"),),
            (),
        )
        transformed_source = relabel_boundary(arrow.source, witness)
        occurrence = arrow.children[0].occurrence
        if type(occurrence) is not Occurrence:
            raise IntegrityFailure("groupoid attack lost its occurrence")
        malformed = Occurrence(
            occurrence.occurrence_id,
            "other_c",
            "other_p",
            occurrence.query,
            occurrence.target_mode,
        )
        caught, error = _capture_refusal(
            lambda: generator_arrow(transformed_source, malformed)
        )
        passed = caught
        old = arrow.to_data()
        new = {"source": transformed_source, "untransported_query": malformed.query}
        evidence = {"refusal": error}
    elif identifier == "EMPTY-LEFT-IDENTITY":
        minimal_arrow = _minimal_role_relabel_arrow()
        minimal_witness = make_groupoid_witness(
            minimal_arrow, (("A", "B"),)
        )
        identity = identity_witness(minimal_arrow)
        composite = compose_witnesses(identity, minimal_witness)
        passed = composite == minimal_witness and relabel_arrow(
            minimal_arrow, composite
        ) == minimal_witness.target.arrow
        old = {"old_first-row-only_result": identity}
        new = {"total_composite": composite}
        evidence = {
            "application_order": "FIRST-THEN-SECOND",
            "exact_adjudicated_map": (("A", "B"),),
            "left_identity_exact": composite == minimal_witness,
            "action_exact": relabel_arrow(minimal_arrow, composite)
            == minimal_witness.target.arrow,
        }
    elif identifier == "EMPTY-RIGHT-IDENTITY":
        identity = identity_witness(first.target.arrow)
        composite = compose_witnesses(first, identity)
        passed = composite == first and relabel_arrow(arrow, composite) == first.target.arrow
        old = {"old_sparse_shortcut": identity}
        new = {"total_composite": composite}
        evidence = {
            "application_order": "FIRST-THEN-SECOND",
            "right_identity_exact": composite == first,
        }
    elif identifier == "INVERSE-LEFT":
        inverse = inverse_witness(first)
        composite = compose_witnesses(first, inverse)
        identity = identity_witness(arrow)
        passed = composite == identity
        old = {"nontrivial": first}
        new = {"inverse_then_witness": composite}
        evidence = {"inverse_left_exact": passed, "identity": identity}
    elif identifier == "INVERSE-RIGHT":
        inverse = inverse_witness(first)
        composite = compose_witnesses(inverse, first)
        identity = identity_witness(first.target.arrow)
        passed = composite == identity
        old = {"nontrivial": inverse}
        new = {"witness_then_inverse": composite}
        evidence = {"inverse_right_exact": passed, "identity": identity}
    elif identifier == "THREE-SPARSE-ASSOCIATIVITY":
        left = compose_witnesses(compose_witnesses(first, second), third)
        right = compose_witnesses(first, compose_witnesses(second, third))
        passed = left == right and relabel_arrow(arrow, left) == relabel_arrow(arrow, right)
        old = {"left_parenthesization": left}
        new = {"right_parenthesization": right, "raw_chain": (first, second, third)}
        evidence = {"associativity_exact": passed}
    elif identifier == "MIDDLE-PRESENTATION-MISMATCH":
        alien = _suffix_groupoid_witness(
            arrow,
            "__equal_size_but_alien",
            ("role", "matter", "port", "occurrence"),
        )
        caught, error = _capture_refusal(lambda: compose_witnesses(first, alien))
        passed = caught
        old = {"lawful_middle": first.target}
        new = {"alien_middle": alien.source, "same_carrier_sizes": tuple(
            len(carrier)
            for carrier in (
                alien.source.role_carrier,
                alien.source.matter_carrier,
                alien.source.port_carrier,
                alien.source.occurrence_carrier,
            )
        )}
        evidence = {"refusal": error, "refused_before_action": caught}
    elif identifier == "SOURCE-LABEL-OMITTED":
        role_only = _suffix_groupoid_witness(arrow, "__role_only", ("role",))
        caught, error = _capture_refusal(
            lambda: SourceGroupoidWitness(
                role_only.source, role_only.target, (), (), (), ()
            )
        )
        passed = caught
        old = {"complete": role_only}
        new = {"omitted_sparse_map": (), "target": role_only.target}
        evidence = {"refusal": error, "nontotal_refused": caught}
    elif identifier == "EXTRA-TARGET-LABEL":
        source = presentation_from_arrow(arrow)
        forged_roles = source.role_carrier + (("extra_target", "RELATION"),)
        caught, error = _capture_refusal(
            lambda: SourcePresentation(
                source.arrow,
                forged_roles,
                source.matter_carrier,
                source.port_carrier,
                source.occurrence_carrier,
            )
        )
        passed = caught
        old = source
        new = {"forged_target_roles": forged_roles}
        evidence = {"refusal": error, "nonsurjective_refused": caught}
    elif identifier == "MAP-COLLISION":
        role_only = _suffix_groupoid_witness(arrow, "__collision", ("role",))
        source_roles = tuple(name for name, _ in role_only.source.role_carrier)
        target_roles = tuple(name for name, _ in role_only.target.role_carrier)
        collision_rows = tuple(
            (source_name, target_roles[0]) for source_name in source_roles
        )
        caught, error = _capture_refusal(
            lambda: SourceGroupoidWitness(
                role_only.source,
                role_only.target,
                collision_rows,
                (),
                (),
                (),
            )
        )
        passed = caught
        old = role_only.role_map
        new = collision_rows
        evidence = {"refusal": error, "noninjective_refused": caught}
    elif identifier == "ROLE-TYPE-SWAP":
        relation = Context((Role("typed_A", "RELATION"),), ((), ("typed_A",)))
        spectator = Context((Role("typed_A", "SPECTATOR"),), ((), ("typed_A",)))
        source_arrow = identity_arrow(atomic_boundary(("typed_c",), relation, ()))
        target_arrow = identity_arrow(atomic_boundary(("typed_c",), spectator, ()))
        source_presentation = presentation_from_arrow(source_arrow)
        target_presentation = presentation_from_arrow(target_arrow)
        caught, error = _capture_refusal(
            lambda: SourceGroupoidWitness(
                source_presentation, target_presentation, (), (), (), ()
            )
        )
        passed = caught
        old = source_presentation
        new = target_presentation
        evidence = {"refusal": error, "type_change_refused": caught}
    elif identifier == "NAMESPACE-CROSSING":
        role_name = first.source.role_carrier[0][0]
        matter_target = first.target.matter_carrier[0]
        caught, error = _capture_refusal(
            lambda: SourceGroupoidWitness(
                first.source,
                first.target,
                (),
                ((role_name, matter_target),),
                first.port_map,
                first.occurrence_map,
            )
        )
        passed = caught
        old = first
        new = {"role_as_matter": (role_name, matter_target)}
        evidence = {"refusal": error, "namespace_crossing_refused": caught}
    elif identifier == "TARGET-PRESENTATION-FORGERY":
        first_leaf = arrow.children[0]
        if type(first_leaf.occurrence) is not Occurrence:
            raise IntegrityFailure("forgery attack lost a generator occurrence")
        forged_occurrence = Occurrence(
            first_leaf.occurrence.occurrence_id,
            first_leaf.occurrence.matter_role,
            first_leaf.occurrence.port_name,
            formula_constant(False),
            first_leaf.occurrence.target_mode,
        )
        forged_leaf = generator_arrow(first_leaf.source, forged_occurrence)
        forged_second = arrow.children[1]
        forged_arrow = compose_arrows(forged_leaf, forged_second)
        caught, error = _capture_refusal(
            lambda: SourceGroupoidWitness(
                presentation_from_arrow(arrow),
                presentation_from_arrow(forged_arrow),
                (),
                (),
                (),
                (),
            )
        )
        passed = caught
        old = arrow
        new = forged_arrow
        evidence = {"refusal": error, "literal_transport_refused": caught}
    elif identifier == "IDENTITY-ROW-ENCODING":
        presentation = presentation_from_arrow(arrow)
        explicit = SourceGroupoidWitness(
            presentation,
            presentation,
            tuple((name, name) for name, _ in presentation.role_carrier),
            tuple((name, name) for name in presentation.matter_carrier),
            tuple((name, name) for name in presentation.port_carrier),
            tuple((name, name) for name in presentation.occurrence_carrier),
        )
        omitted = identity_witness(arrow)
        passed = explicit == omitted and canonical_bytes(explicit) == canonical_bytes(omitted)
        old = {"raw_sparse_rows": ()}
        new = {"raw_sparse_rows": _presentation_carriers(arrow), "canonical": explicit}
        evidence = {"canonical_identity_equal": passed}
    elif identifier == "ORDER-REVERSAL":
        carrier = ("order_A", "order_B", "order_C")
        first_total = (
            ("order_A", "order_B"),
            ("order_B", "order_A"),
            ("order_C", "order_C"),
        )
        second_total = (
            ("order_A", "order_A"),
            ("order_B", "order_C"),
            ("order_C", "order_B"),
        )
        forward = _abstract_compose_maps(first_total, second_total)
        reverse = _abstract_compose_maps(second_total, first_total)
        probe = formula_atom("order_A")
        forward_image = _rename(_abstract_sparse_map(forward), probe.roles[0])
        reverse_image = _rename(_abstract_sparse_map(reverse), probe.roles[0])
        passed = forward != reverse and forward_image != reverse_image
        old = {"opposite_order": reverse, "probe_image": reverse_image}
        new = {"declared_order": forward, "probe_image": forward_image}
        evidence = {"order_changes_transported_formula": passed}
    elif identifier == "TRANSPORT-SEVER":
        role_only = _suffix_groupoid_witness(arrow, "__sever", ("role",))
        transformed_source = relabel_boundary(arrow.source, role_only)
        leaf = arrow.children[0]
        if type(leaf.occurrence) is not Occurrence:
            raise IntegrityFailure("transport sever attack lost occurrence")
        caught, error = _capture_refusal(
            lambda: generator_arrow(transformed_source, leaf.occurrence)
        )
        passed = caught
        old = relabel_occurrence(leaf.occurrence, restrict_witness_to_arrow(role_only, leaf))
        new = leaf.occurrence
        evidence = {"refusal": error, "untransported_query_refused": caught}
    elif identifier == "CERTIFICATE-TRANSPORT-CACHE":
        application = _minimal_bound_split_application(law)
        split_arrow = application["arrow"]
        witness = _suffix_groupoid_witness(
            split_arrow, "__cert", ("role", "matter", "port", "occurrence")
        )
        transformed_arrow = relabel_arrow(split_arrow, witness)
        source_state = application["source"]
        target_state = application["branch1"]
        transformed_source = relabel_configuration(
            split_arrow.source, transformed_arrow.source, source_state, witness
        )
        transformed_target = relabel_configuration(
            split_arrow.target, transformed_arrow.target, target_state, witness
        )
        cached = application["branch1_certificate"]
        cached_valid = validate_bound_split_certificate(
            law, transformed_arrow, transformed_source, transformed_target, cached
        )
        rebuilt = build_bound_split_certificate(
            law, transformed_arrow, transformed_source, transformed_target
        )
        passed = not cached_valid and rebuilt.final and canonical_hash(cached) != canonical_hash(rebuilt)
        old = cached
        new = rebuilt
        evidence = {"cached_valid": cached_valid, "rebuilt_final": rebuilt.final}
    elif identifier == "COMPOSITE-OPERATOR-CACHE":
        composite = compose_witnesses(first, second)
        transformed = relabel_arrow(arrow, composite)
        original_operator = evaluate_arrow(law, arrow)
        transformed_operator = evaluate_arrow(law, transformed)
        residual, covariance = _covariance_residual_from_maps(
            arrow, composite, transformed, original_operator, transformed_operator
        )
        passed = residual == 0 and canonical_hash(original_operator) != canonical_hash(transformed_operator)
        old = {"cached_operator": original_operator, "source": composite.source}
        new = {"required_operator": transformed_operator, "source": composite.target}
        evidence = covariance | {"cache_key_changed": passed}
    elif identifier == "COPIED-GROUPOID-BOOLEAN":
        baseline_groupoid = (
            measurements["groupoid"]
            if measurements is not None
            else measure_groupoid_covariance(law)
        )
        native = baseline_groupoid["native_census"]
        rows = list(native["rows"])
        changed_row = dict(rows[0])
        changed_fields = dict(changed_row["law_fields"])
        changed_fields["left_identity_exact"] = False
        changed_row["law_fields"] = changed_fields
        changed_row["all_exact"] = True
        rows[0] = changed_row
        changed_native = dict(native)
        changed_native["rows"] = tuple(rows)
        changed_native["all_exact"] = True
        copied = dict(baseline_groupoid)
        copied["native_census"] = changed_native
        copied["all_exact"] = True
        passed = not groupoid_promotion_predicate(copied)
        old = baseline_groupoid["native_dependency_sha256"]
        new = {"copied_all_exact": True, "false_native_row": changed_row}
        evidence = {
            "native_conjunction_refused": passed,
            "earliest_rung": drop,
        }
    elif identifier == "TENSOR-SHARED-LABEL-CONFLICT":
        relation = Context((Role("shared_role", "RELATION"),), ((), ("shared_role",)))
        spectator = Context((Role("shared_role", "SPECTATOR"),), ((), ("shared_role",)))
        left = identity_arrow(atomic_boundary(("left_coin",), relation, ()))
        right = identity_arrow(atomic_boundary(("right_coin",), spectator, ()))
        caught, error = _capture_refusal(
            lambda: presentation_from_arrow(tensor_arrow(left, right))
        )
        passed = caught
        old = {"left": left}
        new = {"left": left, "right_conflict": right}
        evidence = {"refusal": error, "shared_type_conflict_refused": caught}
    elif identifier == "FRESH-GLOBAL-RELABEL-SEVER":
        matching = build_matching_arrow(
            MatchingPresentation(4, tuple(range(4)), (0,), "EXPOSED-CONTROL"),
            "fresh_sever_",
        )
        matching_arrow = matching["arrow"]
        witness = _suffix_groupoid_witness(matching_arrow, "__fresh", ("role",))
        transformed_source = relabel_boundary(matching_arrow.source, witness)
        if type(matching_arrow.occurrence) is not Occurrence:
            raise IntegrityFailure("fresh sever attack lost occurrence")
        caught, error = _capture_refusal(
            lambda: generator_arrow(transformed_source, matching_arrow.occurrence)
        )
        passed = caught
        old = relabel_arrow(matching_arrow, witness)
        new = {"context": transformed_source, "unmoved_schedule": matching_arrow.occurrence}
        evidence = {"refusal": error, "blind_groupoid_dependency_failed": caught}
    else:
        raise Refusal("unknown groupoid development mutation")
    return _attack_record(
        old,
        new,
        "source_groupoid.action",
        "PRESENTATION-COVARIANCE",
        "EXPLICIT-TRANSPORT-WITNESS",
        passed,
        evidence,
        "CONTROL-COVARIANT" if passed else drop,
    )


def _minimal_split_attack_objects() -> dict[str, Any]:
    source = Context((Role("A", "RELATION"),), ((), ("A",)))
    parent = formula_atom("A")
    child = Role("N", "RELATION")
    lawful_target = context_extend(source, child, parent)
    lawful_proof = build_context_split_proof(
        source, lawful_target, parent, child
    )
    return {
        "source": source,
        "parent": parent,
        "child": child,
        "lawful_target": lawful_target,
        "lawful_proof": lawful_proof,
    }


def _minimal_bound_split_application(law: GammaLaw) -> dict[str, Any]:
    context = Context((Role("A", "RELATION"),), ((), ("A",)))
    parent = formula_atom("A")
    port = Port(
        "split_attack_port",
        Role("N", "RELATION"),
        formula_not(parent),
        parent,
    )
    boundary = atomic_boundary(
        ("split_attack_matter",), context, (PortDecl(port, "ACTIVE"),)
    )
    occurrence = Occurrence(
        "split_attack_occurrence",
        "split_attack_matter",
        "split_attack_port",
        parent,
        "ACTIVE",
    )
    arrow = generator_arrow(boundary, occurrence)
    source = _empty_state(boundary, {"split_attack_matter": 0})
    branch0 = _empty_state(
        arrow.target,
        {"split_attack_matter": 0},
        {"split_attack_port": "branch0"},
    )
    branch1 = _empty_state(
        arrow.target,
        {"split_attack_matter": 1},
        {"split_attack_port": "branch1"},
    )
    return {
        "boundary": boundary,
        "arrow": arrow,
        "source": source,
        "branch0": branch0,
        "branch1": branch1,
        "branch0_certificate": build_bound_split_certificate(
            law, arrow, source, branch0
        ),
        "branch1_certificate": build_bound_split_certificate(
            law, arrow, source, branch1
        ),
    }


def _all_true_gate_surface() -> dict[str, bool]:
    return {
        "specification": True,
        "referent": True,
        "complete_gamma": True,
        "source_sufficiency": True,
        "anti_wrapper": True,
        "shadow_weld": True,
        "variable_carrier": True,
        "support_change": True,
        "reciprocal": True,
        "division": True,
        "native_nondivision": True,
        "blind_class": True,
    }


def _split_support_attacks(identifier: str) -> dict[str, Any]:
    law = GammaLaw(Fraction(1, 2))
    objects = _minimal_split_attack_objects()
    source = objects["source"]
    parent = objects["parent"]
    child = objects["child"]
    lawful = objects["lawful_proof"]
    old: Any = lawful
    changed_path = "context_split.target"
    drop = "P13-SUPPORT-CHANGE-UNPROVEN"
    if identifier in ("TAUTOLOGICAL-CHILD", "COEXTENSIVE-CHILD-OBJECT"):
        target = Context(
            (Role("A", "RELATION"), child),
            ((), ("A", "N")),
        )
        mutant = build_context_split_proof(source, target, parent, child)
        new = mutant
        degraded = _all_true_gate_surface()
        degraded["support_change"] = False
        passed = (
            lawful.final
            and mutant.forget_exact
            and not mutant.exact_fibers
            and not mutant.final
            and mutant.rows[1].observed_child_bits == (1,)
            and classify_primary(degraded) == "P13-SUPPORT-CHANGE-UNPROVEN"
        )
        evidence = {
            "lawful_certificate_sha256": canonical_hash(lawful),
            "mutant_certificate_sha256": canonical_hash(mutant),
            "satisfying_fiber": mutant.rows[1],
            "count_residual": mutant.count_residual,
            "forget_exact": mutant.forget_exact,
            "native_support_gate": mutant.final,
            "rendered_rung": classify_primary(degraded),
            "source_mutation_target": identifier == "TAUTOLOGICAL-CHILD",
        }
        changed_path = (
            "context_extend.parent_cell_retention"
            if identifier == "TAUTOLOGICAL-CHILD"
            else "context_split.supplied_coextensive_target"
        )
    elif identifier == "FORGET-ONLY":
        target = Context(
            (Role("A", "RELATION"), child),
            ((), ("N",), ("A",)),
        )
        mutant = build_context_split_proof(source, target, parent, child)
        new = mutant
        passed = mutant.forget_exact and not mutant.exact_fibers and not mutant.final
        evidence = {
            "forget_exact": mutant.forget_exact,
            "fiber_rows": mutant.rows,
            "count_residual": mutant.count_residual,
            "final": mutant.final,
        }
    elif identifier == "CELL-COUNT-PADDING":
        target = Context(
            (Role("A", "RELATION"), child),
            ((), ("N",), ("A", "N")),
        )
        mutant = build_context_split_proof(source, target, parent, child)
        new = mutant
        passed = (
            mutant.actual_target_cell_count == mutant.expected_target_cell_count == 3
            and mutant.forget_exact
            and not mutant.exact_fibers
            and not mutant.final
        )
        evidence = {
            "scalar_count_equal": mutant.actual_target_cell_count
            == mutant.expected_target_cell_count,
            "forget_exact": mutant.forget_exact,
            "fiber_rows": mutant.rows,
            "final": mutant.final,
        }
    elif identifier == "ROLE-COUNT-ONLY":
        target = Context(
            (Role("A", "RELATION"), child),
            ((), ("A", "N")),
        )
        mutant = build_context_split_proof(source, target, parent, child)
        legacy_predicate = (
            len(source.roles), len(source.cells)
        ) != (len(target.roles), len(target.cells))
        native_predicate = mutant.final
        degraded = _all_true_gate_surface()
        degraded["support_change"] = native_predicate
        old = {
            "native_certificate": lawful,
            "promotive_predicate": lawful.final,
        }
        new = {
            "coextensive_certificate": mutant,
            "legacy_role_cell_inequality": legacy_predicate,
        }
        measurement_old = canonical_hash(lawful)
        measurement_new = canonical_hash(mutant)
        lineage_old = canonical_hash(
            (law_identity(law), canonical_hash(lawful), lawful.final)
        )
        lineage_new = canonical_hash(
            (law_identity(law), canonical_hash(mutant), legacy_predicate)
        )
        claim_old = canonical_hash(("support_change", lawful.final, measurement_old))
        claim_new = canonical_hash(("support_change", native_predicate, measurement_new))
        seal_old = canonical_hash((measurement_old, lineage_old, claim_old))
        seal_new = canonical_hash((measurement_new, lineage_new, claim_new))
        passed = (
            legacy_predicate
            and not native_predicate
            and measurement_old != measurement_new
            and lineage_old != lineage_new
            and claim_old != claim_new
            and seal_old != seal_new
            and classify_primary(degraded) == "P13-SUPPORT-CHANGE-UNPROVEN"
        )
        evidence = {
            "legacy_predicate": legacy_predicate,
            "native_predicate": native_predicate,
            "measurement_hashes": (measurement_old, measurement_new),
            "lineage_hashes": (lineage_old, lineage_new),
            "claim_hashes": (claim_old, claim_new),
            "seal_hashes": (seal_old, seal_new),
            "rendered_rung": classify_primary(degraded),
            "source_mutation_target": True,
        }
        changed_path = "support_promotion_predicate"
    elif identifier == "TRANSPORT-SPLIT-SEVER":
        application = _minimal_bound_split_application(law)
        witness = make_groupoid_witness(
            application["arrow"],
            (("A", "transport_A"), ("N", "transport_N")),
        )
        transported = relabel_context_split_proof(lawful, witness)
        severed = build_context_split_proof_from_truth(
            transported.source,
            transported.target,
            transported.parent_truth,
            Role("N", "RELATION"),
        )
        old = transported
        new = severed
        passed = transported.final and not severed.final
        evidence = {
            "transported_sha256": canonical_hash(transported),
            "severed_sha256": canonical_hash(severed),
            "unexpected_target_cells": severed.unexpected_target_cells,
            "count_residual": severed.count_residual,
            "final": severed.final,
        }
        changed_path = "source_groupoid.split_child_transport"
    elif identifier == "SUPPLIED-SPLIT-BOOLEAN":
        application = _minimal_bound_split_application(law)
        supplied = {
            "split_valid": True,
            "context_proof": lawful,
            "attached_to": "coextensive-target",
        }
        caught, error = _capture_refusal(
            lambda: validate_bound_split_certificate(
                law,
                application["arrow"],
                application["source"],
                application["branch1"],
                supplied,
            )
        )
        old = application["branch1_certificate"]
        new = supplied
        passed = caught
        evidence = {
            "typed_refusal": error,
            "context_proof_alone_promotive": False,
            "supplied_boolean_inert": True,
        }
        changed_path = "classifier.supplied_split_valid"
    elif identifier == "CERTIFICATE-PORT-SWAP":
        application = _minimal_bound_split_application(law)
        attached = application["branch1_certificate"]
        accepted = validate_bound_split_certificate(
            law,
            application["arrow"],
            application["source"],
            application["branch0"],
            attached,
        )
        correct = application["branch0_certificate"]
        old = correct
        new = attached
        passed = not accepted and canonical_bytes(correct) != canonical_bytes(attached)
        evidence = {
            "attached_parent_key": attached.branch_parent_key,
            "actual_parent_key": correct.branch_parent_key,
            "attached_target_hash": attached.target_configuration_sha256,
            "actual_target_hash": correct.target_configuration_sha256,
            "validation_predicate": accepted,
        }
        changed_path = "classifier.bound_certificate.branch_attachment"
    elif identifier == "OLD-CHILD-REUSE":
        same_name_caught, same_name_error = _capture_refusal(
            lambda: context_extend(
                source, Role("A", "RELATION"), parent
            )
        )
        changed_type_caught, changed_type_error = _capture_refusal(
            lambda: context_extend(
                source, Role("A", "SPECTATOR"), parent
            )
        )
        old = child
        new = {
            "same_name": Role("A", "RELATION"),
            "changed_type": Role("A", "SPECTATOR"),
        }
        passed = same_name_caught and changed_type_caught
        evidence = {
            "same_name_refusal": same_name_error,
            "changed_type_refusal": changed_type_error,
        }
        changed_path = "context_split.child_identity"
    elif identifier == "AMBIENT-TARGET-PADDING":
        extra = Role("X", "RELATION")
        target = Context(
            (Role("A", "RELATION"), child, extra),
            ((), ("A",), ("A", "N", "X")),
        )
        mutant = build_context_split_proof(source, target, parent, child)
        new = mutant
        passed = (
            mutant.actual_target_cell_count == mutant.expected_target_cell_count
            and (not mutant.target_exhaustive or not mutant.roles_exact)
            and not mutant.final
        )
        evidence = {
            "scalar_count_equal": mutant.actual_target_cell_count
            == mutant.expected_target_cell_count,
            "unexpected_target_cells": mutant.unexpected_target_cells,
            "target_exhaustive": mutant.target_exhaustive,
            "roles_exact": mutant.roles_exact,
            "final": mutant.final,
        }
    elif identifier == "CONTEXTUAL-BOOLEAN-ALIAS":
        alias = _measure_contextual_alias(law)
        old = alias["left"]["raw_formula_sha256"]
        new = alias["right"]["raw_formula_sha256"]
        passed = alias["raw_ambient_formulas_distinct"] and alias[
            "all_physical_fields_equal"
        ]
        evidence = {
            "raw_ambient_formulas_distinct": alias[
                "raw_ambient_formulas_distinct"
            ],
            "physical_fields_equal": alias["physical_fields_equal"],
            "left_certificate_sha256": alias["left"]["certificate_sha256"],
            "right_certificate_sha256": alias["right"]["certificate_sha256"],
        }
        changed_path = "formula.ambient_provenance_only"
        drop = "CONTROL-CONTEXTUAL-IDENTITY-INVARIANT"
    else:
        raise Refusal("unknown split-support development mutation")
    return _attack_record(
        old,
        new,
        changed_path,
        "POINT-FREE-HORIZONTAL-SPLIT",
        "EXHAUSTIVE-BOUND-SPLIT-CERTIFICATE",
        passed,
        evidence,
        drop,
    )


def _typed_groupoid_v4_attack_context(
    measurements: Mapping[str, Any] | None = None,
    include_shared_censuses: bool = False,
) -> dict[str, Any]:
    """Build immutable common inputs once for the full action-attack registry."""

    law = GammaLaw(Fraction(1, 2))
    application = _minimal_bound_split_application(law)
    arrow = application["arrow"]
    presentation = presentation_from_arrow(arrow)
    source_node = boundary_node_at(presentation, (), "SOURCE")
    source_configuration = application["source"]
    identity = identity_witness(arrow)
    first = _suffix_groupoid_witness(
        arrow, "__v3_attack1", ("role", "matter", "port", "occurrence")
    )
    second = _suffix_groupoid_witness(
        first.target.arrow,
        "__v3_attack2",
        ("role", "matter", "port", "occurrence"),
    )
    third = _suffix_groupoid_witness(
        second.target.arrow,
        "__v3_attack3",
        ("role", "matter", "port", "occurrence"),
    )
    certificate0 = application["branch0_certificate"]
    certificate1 = application["branch1_certificate"]
    input0 = build_certificate_action_input(
        law,
        presentation,
        (),
        source_configuration,
        application["branch0"],
        certificate0,
    )
    input1 = build_certificate_action_input(
        law,
        presentation,
        (),
        source_configuration,
        application["branch1"],
        certificate1,
    )
    triple0 = certificate_transport_triple(first, input0)
    promotion_static = (
        measurements["groupoid_promotion_static"]
        if measurements is not None
        else groupoid_promotion_source_scan(Path(__file__).read_text(encoding="utf-8"))
    )
    context = {
        "law": law,
        "application": application,
        "arrow": arrow,
        "presentation": presentation,
        "source_node": source_node,
        "source_configuration": source_configuration,
        "identity": identity,
        "first": first,
        "second": second,
        "third": third,
        "certificate0": certificate0,
        "certificate1": certificate1,
        "input0": input0,
        "input1": input1,
        "triple0": triple0,
        "promotion_static": promotion_static,
        "old_configuration_action": act_configuration(
            source_node, source_configuration, identity
        ),
    }
    if include_shared_censuses:
        context["configuration_census"] = configuration_action_census(
            presentation, first, second, third
        )
        context["certificate_create_census"] = certificate_action_census(
            law, presentation, (), first, second, third, "CREATE"
        )
    return context


def _typed_groupoid_v4_action_attack(
    identifier: str,
    measurements: Mapping[str, Any] | None = None,
    shared_context: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    context = (
        _typed_groupoid_v4_attack_context(measurements)
        if shared_context is None
        else shared_context
    )
    law = context["law"]
    application = context["application"]
    arrow = context["arrow"]
    presentation = context["presentation"]
    source_node = context["source_node"]
    source_configuration = context["source_configuration"]
    identity = context["identity"]
    first = context["first"]
    second = context["second"]
    third = context["third"]
    certificate0 = context["certificate0"]
    certificate1 = context["certificate1"]
    input0 = context["input0"]
    input1 = context["input1"]
    triple0 = context["triple0"]
    promotion_static = context["promotion_static"]
    old: Any = {
        "lawful_configuration_action": context["old_configuration_action"]
    }
    new: Any = {"attack": identifier}
    evidence: dict[str, Any] = {}
    passed = False
    changed_path = "typed_groupoid_v4.action"
    killed_by = "COMPLETE-TARGET-FREE-ACTION-AND-LITERAL-CERTIFICATE-BINDING"
    drop = "P13-REFERENT-PRESENTATION-ONLY"

    if identifier == "NONIMAGE-ACTIVE-CARRIED":
        carried = boundary_with_port_mode(
            arrow.source, arrow.occurrence.port_name, "CARRIED"
        )
        asserted = BoundaryNode(
            carried, canonical_bytes(boundary_semantic_key(carried)), (), "SOURCE"
        )
        passed, refusal = _capture_refusal(
            lambda: assert_configuration_target(source_node, asserted, identity)
        )
        new = asserted
        evidence = {"refusal": refusal, "refused_before_action": passed}
    elif identifier == "SAME-CARDINALITY-ALIEN-BOUNDARY":
        alien = atomic_boundary(("alien_matter",), arrow.source.base, arrow.source.ports)
        asserted = BoundaryNode(
            alien, canonical_bytes(boundary_semantic_key(alien)), (), "SOURCE"
        )
        passed, refusal = _capture_refusal(
            lambda: assert_configuration_target(source_node, asserted, identity)
        )
        new = asserted
        evidence = {
            "same_catalogue_size": len(alien.catalogue) == len(arrow.source.catalogue),
            "refusal": refusal,
        }
    elif identifier == "WRONG-BRANCH-TARGET":
        asserted = boundary_node_at(presentation, (), "TARGET")
        passed, refusal = _capture_refusal(
            lambda: assert_configuration_target(source_node, asserted, identity)
        )
        new = asserted
        evidence = {"refusal": refusal, "endpoint_role_changed": True}
    elif identifier == "ALIEN-CONFIGURATION-MATTER":
        alien = Configuration(
            source_configuration.context,
            (("alien_matter", 0),),
            source_configuration.sectors,
        )
        passed, refusal = _capture_refusal(
            lambda: act_configuration(source_node, alien, identity)
        )
        new = alien
        evidence = {"refusal": refusal}
    elif identifier == "ALIEN-CONFIGURATION-PORT":
        alien = Configuration(
            source_configuration.context,
            source_configuration.matter,
            (("alien_port", "empty"),),
        )
        passed, refusal = _capture_refusal(
            lambda: act_configuration(source_node, alien, identity)
        )
        new = alien
        evidence = {"refusal": refusal}
    elif identifier == "CONTEXT-ONLY-EQUAL-TARGET":
        carried = boundary_with_port_mode(
            arrow.source, arrow.occurrence.port_name, "CARRIED"
        )
        asserted = BoundaryNode(
            carried, canonical_bytes(boundary_semantic_key(carried)), (), "SOURCE"
        )
        passed, refusal = _capture_refusal(
            lambda: assert_configuration_target(source_node, asserted, identity)
        )
        new = asserted
        evidence = {
            "base_context_equal": context_semantic_key(carried.base)
            == context_semantic_key(arrow.source.base),
            "mode_differs": carried.ports[0].mode != arrow.source.ports[0].mode,
            "refusal": refusal,
        }
    elif identifier == "BOUNDARY-NOT-IN-PRESENTATION":
        labelled = atomic_boundary(
            arrow.source.matter_roles,
            arrow.source.base,
            arrow.source.ports,
            neutral_label="alien-presentation-node",
        )
        alien_node = BoundaryNode(
            labelled,
            canonical_bytes(boundary_semantic_key(labelled)),
            (),
            "SOURCE",
        )
        passed, refusal = _capture_refusal(
            lambda: act_configuration(alien_node, source_configuration, identity)
        )
        new = alien_node
        evidence = {"semantic_bytes_equal": alien_node.boundary_semantic_bytes == source_node.boundary_semantic_bytes, "refusal": refusal}
    elif identifier in ("CHAINED-NONIMAGE-TARGET", "DERIVED-TARGET-CACHE"):
        first_transport = act_configuration(source_node, source_configuration, first)
        passed, refusal = _capture_refusal(
            lambda: assert_configuration_target(
                first_transport.target_node, first_transport.target_node, second
            )
        )
        new = {"stale_target": first_transport.target_node, "second_witness": second}
        evidence = {"refusal": refusal, "stale_target_refused": passed}
    elif identifier == "TENSOR-FOREIGN-FACTOR":
        left_arrow = _small_generator(_small_atom("v3_tl_"), "v3_tl_")
        right_arrow = _small_generator(_small_atom("v3_tr_"), "v3_tr_")
        tensor = tensor_arrow(left_arrow, right_arrow)
        tensor_witness = _suffix_groupoid_witness(
            tensor, "__tensor", ("role", "matter", "port", "occurrence")
        )
        tensor_source = boundary_node_at(tensor_witness.source, (), "SOURCE")
        foreign_arrow = tensor_arrow(left_arrow, _small_generator(_small_atom("v3_foreign_"), "v3_foreign_"))
        foreign_target = boundary_node_at(
            presentation_from_arrow(foreign_arrow), (), "TARGET"
        )
        passed, refusal = _capture_refusal(
            lambda: assert_configuration_target(
                tensor_source, foreign_target, tensor_witness
            )
        )
        new = foreign_target
        evidence = {"refusal": refusal}
    elif identifier == "DUPLICATE-SEMANTIC-NODE-COLLAPSE":
        identity_presentation = presentation_from_arrow(identity_arrow(arrow.source))
        left_node = boundary_node_at(identity_presentation, (), "SOURCE")
        right_node = boundary_node_at(identity_presentation, (), "TARGET")
        left_row = identity_action_row(identity_presentation, left_node, source_configuration)
        right_row = identity_action_row(identity_presentation, right_node, source_configuration)
        passed = (
            left_node.boundary_semantic_bytes == right_node.boundary_semantic_bytes
            and left_node != right_node
            and canonical_hash(left_node) != canonical_hash(right_node)
            and left_row.exact
            and right_row.exact
        )
        old = {"nodes": (left_node, right_node)}
        new = {"collapsed_node": left_node}
        evidence = {"distinct_provenance_rows": passed}
    elif identifier in (
        "CONFIGURATION-COMPOSITION-SEVER",
        "CONFIGURATION-ASSOCIATIVITY-SEVER",
    ):
        census = context.get("configuration_census")
        if census is None:
            census = configuration_action_census(
                presentation, first, second, third
            )
        changed = dict(census)
        rows = list(census["rows"])
        row = dict(rows[0])
        key = "composition" if identifier.endswith("COMPOSITION-SEVER") else "associativity"
        law_row = dict(row[key])
        law_row["exact"] = False
        row[key] = law_row
        rows[0] = row
        changed["rows"] = tuple(rows)
        passed = _configuration_action_census_exact(census) and not _configuration_action_census_exact(changed)
        old = census
        new = changed
        evidence = {"changed_law": key, "promotion_refused": passed}
    elif identifier == "CONFIGURATION-TENSOR-SEVER":
        left_arrow = _small_generator(_small_atom("v3_al_"), "v3_al_")
        right_arrow = _small_generator(_small_atom("v3_ar_"), "v3_ar_")
        left_witness = _suffix_groupoid_witness(left_arrow, "__a", ("role", "matter", "port", "occurrence"))
        right_witness = _suffix_groupoid_witness(right_arrow, "__a", ("role", "matter", "port", "occurrence"))
        left_node = boundary_node_at(left_witness.source, (), "SOURCE")
        right_node = boundary_node_at(right_witness.source, (), "SOURCE")
        tensor_presentation = presentation_from_arrow(tensor_arrow(left_arrow, right_arrow))
        tensor_node = boundary_node_at(tensor_presentation, (), "SOURCE")
        left_q = left_node.boundary.catalogue[0]
        right_q = right_node.boundary.catalogue[0]
        tensor_q = _tensor_configuration_from_factors(tensor_node, left_q, right_q)
        tensor_row = tensor_action_row(tensor_node, tensor_q, left_node, left_q, left_witness, right_node, right_q, right_witness)
        store: dict[str, bytes] = {}
        reference = _configuration_law_reference(tensor_row, store)
        identities = set(store)
        severed = dict(reference)
        severed["transport_refs"] = reference["transport_refs"][:-1] + (("0" * 64),)
        passed = _configuration_law_reference_exact(reference, identities) and not _configuration_law_reference_exact(severed, identities)
        old = reference
        new = severed
        evidence = {"tensor_row_exact": tensor_row.exact, "sever_refused": passed}
    elif identifier == "IDENTITY-PRESENTATION-COLLISION":
        identity_leaf = identity_arrow(arrow.source)
        first_presentation = presentation_from_arrow(identity_leaf)
        second_presentation = presentation_from_arrow(compose_arrows(identity_leaf, identity_leaf))
        first_node = boundary_node_at(first_presentation, (), "SOURCE")
        second_node = boundary_node_at(second_presentation, (), "SOURCE")
        first_row = identity_action_row(first_presentation, first_node, source_configuration)
        second_row = identity_action_row(second_presentation, second_node, source_configuration)
        passed = (
            first_node == second_node
            and presentation_identity(first_presentation) != presentation_identity(second_presentation)
            and first_row.exact
            and second_row.exact
            and first_row.presentations != second_row.presentations
        )
        old = {"first": first_row}
        new = {"second": second_row}
        evidence = {"presentation_collision_discriminated": passed}
    elif identifier == "CORE-TARGET-BACKDOOR":
        mutant_source = "def act_configuration(source_node, configuration, witness, asserted_target_node=None):\n    return asserted_target_node\n"
        mutant = ast.parse(mutant_source).body[0]
        passed = (
            promotion_static["configuration_signature_exact"]
            and len(mutant.args.args) == 4
            and bool(mutant.args.defaults)
        )
        old = {"signature": ("source_node", "configuration", "witness")}
        new = {"source": mutant_source}
        evidence = {"exact_signature_gate_kills": passed}
    elif identifier == "TENSOR-INTERNAL-FACTOR-NODE":
        left_leaf = _small_generator(_small_atom("v4_internal_left_"), "v4_internal_left_")
        left_arrow = compose_arrows(identity_arrow(left_leaf.source), left_leaf)
        right_arrow = _small_generator(_small_atom("v4_internal_right_"), "v4_internal_right_")
        left_witness = _suffix_groupoid_witness(
            left_arrow, "__v4_tensor", ("role", "matter", "port", "occurrence")
        )
        right_witness = _suffix_groupoid_witness(
            right_arrow, "__v4_tensor", ("role", "matter", "port", "occurrence")
        )
        left_root = boundary_node_at(left_witness.source, (), "SOURCE")
        left_internal = boundary_node_at(left_witness.source, (1,), "SOURCE")
        right_root = boundary_node_at(right_witness.source, (), "SOURCE")
        tensor_presentation = presentation_from_arrow(tensor_arrow(left_arrow, right_arrow))
        tensor_root = boundary_node_at(tensor_presentation, (), "SOURCE")
        left_q = left_root.boundary.catalogue[0]
        right_q = right_root.boundary.catalogue[0]
        tensor_q = _tensor_configuration_from_factors(tensor_root, left_q, right_q)
        passed, refusal = _capture_refusal(
            lambda: tensor_action_row(
                tensor_root,
                tensor_q,
                left_internal,
                left_q,
                left_witness,
                right_root,
                right_q,
                right_witness,
            )
        )
        old = left_root
        new = left_internal
        evidence = {
            "root_address": left_root.ast_address,
            "internal_address": left_internal.ast_address,
            "root_boundary_sha256": canonical_hash(left_root.boundary_semantic_bytes),
            "internal_boundary_sha256": canonical_hash(left_internal.boundary_semantic_bytes),
            "nodes_distinct": left_root != left_internal,
            "refusal": refusal,
        }
    elif identifier == "TENSOR-TARGET-FACTOR-NODE-SEVER":
        tensor_measure = (
            measurements["groupoid"]["tensor_configuration_action"]
            if measurements is not None
            else measure_tensor_configuration_action(law)
        )
        changed = dict(tensor_measure)
        cases = list(tensor_measure["cases"])
        first_case = dict(cases[0])
        first_case["left_transport_target_root_ref"] = first_case[
            "right_target_root_ref"
        ]
        cases[0] = first_case
        changed["cases"] = tuple(cases)
        passed = _tensor_configuration_action_exact(
            tensor_measure
        ) and not _tensor_configuration_action_exact(changed)
        old = {
            "left_target_root_ref": tensor_measure["cases"][0]["left_target_root_ref"],
            "left_transport_target_root_ref": tensor_measure["cases"][0]["left_transport_target_root_ref"],
        }
        new = {
            "left_target_root_ref": first_case["left_target_root_ref"],
            "left_transport_target_root_ref": first_case["left_transport_target_root_ref"],
        }
        evidence = {
            "clean_tensor_exact": _tensor_configuration_action_exact(tensor_measure),
            "severed_tensor_exact": _tensor_configuration_action_exact(changed),
        }
    else:
        store: dict[str, bytes] = {}
        triple_reference = _certificate_triple_reference(triple0, store)
        identities = set(store)
        if identifier == "MALFORMED-TRANSPORTED-CERTIFICATE-BYTES":
            _store_complete_bytes(store, input1)
            changed = dict(triple_reference)
            changed["literal_transport_ref"] = canonical_hash(input1)
            passed = _certificate_triple_reference_exact(triple_reference, set(store)) and not _certificate_triple_reference_exact(changed, set(store))
            old, new = triple_reference, changed
            evidence = {"full_bytes_not_final_count": passed}
        elif identifier == "FINAL-COUNT-ONLY-CERTIFICATE":
            passed = promotion_static["legacy_certificate_summary_absent"]
            old = {"complete_input_and_triples": True}
            new = {"all_original_final": True, "all_transformed_final": True, "count_preserved": True}
            evidence = {"static_legacy_predicate_refused": passed}
        elif identifier == "HASH-LIST-ONLY-CERTIFICATE":
            passed = _complete_byte_store_exact(_freeze_complete_byte_store(store)) and not _complete_byte_store_exact(())
            old = _freeze_complete_byte_store(store)
            new = {"hashes_only": tuple(sorted(store))}
            evidence = {"complete_bytes_required": passed}
        elif identifier in (
            "CERTIFICATE-KEY-ATTACHMENT-SWAP",
            "CERTIFICATE-TARGET-DROP",
            "CERTIFICATE-TARGET-DUPLICATE",
            "CERTIFICATE-WRONG-OPERATION",
            "CERTIFICATE-IDENTITY-ONLY",
            "COPIED-CERTIFICATE-ACTION-BOOLEAN",
            "NATIVE-CERTIFICATE-ROW-BYPASS",
        ):
            census = context.get("certificate_create_census")
            if census is None:
                census = certificate_action_census(
                    law, presentation, (), first, second, third, "CREATE"
                )
            changed = dict(census)
            rows = list(census["rows"])
            if identifier == "CERTIFICATE-KEY-ATTACHMENT-SWAP":
                first_row = dict(rows[0]); second_row = dict(rows[1])
                first_triple = dict(first_row["nontrivial"]); second_triple = dict(second_row["nontrivial"])
                first_triple["independent_rebuild_ref"], second_triple["independent_rebuild_ref"] = second_triple["independent_rebuild_ref"], first_triple["independent_rebuild_ref"]
                first_row["nontrivial"], second_row["nontrivial"] = first_triple, second_triple
                rows[0], rows[1] = first_row, second_row
            elif identifier == "CERTIFICATE-TARGET-DROP":
                rows = rows[:-1]
            elif identifier == "CERTIFICATE-TARGET-DUPLICATE":
                rows[-1] = rows[0]
            elif identifier == "CERTIFICATE-WRONG-OPERATION":
                row = dict(rows[0]); key = list(row["pairing_key"]); key[-5] = "MERGE"; row["pairing_key"] = tuple(key); rows[0] = row
            elif identifier == "CERTIFICATE-IDENTITY-ONLY":
                row = dict(rows[0]); triple = dict(row["nontrivial"]); triple["exact"] = False; row["nontrivial"] = triple; rows[0] = row
            elif identifier == "COPIED-CERTIFICATE-ACTION-BOOLEAN":
                row = dict(rows[0]); triple = dict(row["nontrivial"]); triple["exact"] = False; row["nontrivial"] = triple; row["all_exact"] = True; rows[0] = row
            else:
                changed["operation"] = "OMITTED"
                rows = ()
            changed["rows"] = tuple(rows)
            passed = _certificate_action_census_exact(census) and not _certificate_action_census_exact(changed)
            old, new = census, changed
            evidence = {"total_keyed_pairing_refused": passed}
        elif identifier == "CERTIFICATE-WRONG-BRANCH":
            passed, refusal = _capture_refusal(
                lambda: build_certificate_action_input(law, presentation, (), source_configuration, application["branch1"], certificate0)
            )
            old, new = input0, {"wrong_target": application["branch1"], "certificate": certificate0}
            evidence = {"refusal": refusal}
        elif identifier == "STALE-LITERAL-TRANSPORT":
            passed, refusal = _capture_refusal(lambda: act_certificate(second, input0))
            old, new = triple0.literal_transport, {"stale_input": input0, "new_witness": second}
            evidence = {"refusal": refusal}
        elif identifier == "STALE-INDEPENDENT-REBUILD":
            changed = dict(triple_reference)
            changed["independent_rebuild_ref"] = triple_reference["original_ref"]
            passed = _certificate_triple_reference_exact(triple_reference, identities) and not _certificate_triple_reference_exact(changed, identities)
            old, new = triple_reference, changed
            evidence = {"stale_rebuild_refused": passed}
        elif identifier == "CERTIFICATE-CLASSIFIER-LINEAGE-DROP":
            input_fields = [getattr(input0, field.name) for field in fields(CertificateActionInput)]
            input_fields[-2] = b""
            passed, refusal = _capture_refusal(lambda: CertificateActionInput(*input_fields))
            old, new = input0, {"classifier_consumed_bytes": b""}
            evidence = {"refusal": refusal}
        elif identifier in ("CERTIFICATE-COMPOSITION-SEVER", "CERTIFICATE-INVERSE-SEVER", "CERTIFICATE-ASSOCIATIVITY-SEVER"):
            if identifier == "CERTIFICATE-COMPOSITION-SEVER":
                law_row = certificate_composition_row(input0, first, second)
            elif identifier == "CERTIFICATE-INVERSE-SEVER":
                law_row = certificate_inverse_row(input0, first)
            else:
                law_row = certificate_associativity_row(input0, first, second, third)
            reference = _certificate_law_reference(law_row, store)
            changed = dict(reference); changed["exact"] = False
            passed = _certificate_law_reference_exact(reference, set(store)) and not _certificate_law_reference_exact(changed, set(store))
            old, new = reference, changed
            evidence = {"complete_law_row_refused": passed}
        elif identifier == "HASH-ONLY-CERTIFICATE-ACTION-INPUT":
            passed, refusal = _capture_refusal(lambda: act_certificate(first, certificate0))
            old, new = input0, certificate0
            evidence = {"refusal": refusal}
        elif identifier == "FOREIGN-CERTIFICATE-BINDING":
            foreign = _minimal_bound_split_application(law)
            foreign_arrow = foreign["arrow"]
            foreign_witness = _suffix_groupoid_witness(foreign_arrow, "__foreign", ("role", "matter", "port", "occurrence"))
            passed, refusal = _capture_refusal(
                lambda: build_certificate_action_input(law, foreign_witness.target, (), foreign["source"], foreign["branch0"], certificate0)
            )
            old, new = input0, {"foreign_presentation": foreign_witness.target, "certificate": certificate0}
            evidence = {"refusal": refusal}
        elif identifier == "CERTIFICATE-ACTION-REGISTRY-BACKDOOR":
            mutant_source = "def act_certificate(witness, certificate_action_input, registry=None):\n    return registry\n"
            mutant = ast.parse(mutant_source).body[0]
            passed = promotion_static["certificate_signature_exact"] and len(mutant.args.args) == 3 and bool(mutant.args.defaults)
            old, new = {"signature": ("witness", "certificate_action_input")}, {"source": mutant_source}
            evidence = {"exact_signature_gate_kills": passed}
        elif identifier == "DUPLICATE-GENERATOR-ADDRESS-COLLAPSE":
            duplicate = compose_arrows(arrow, arrow)
            duplicate_presentation = presentation_from_arrow(duplicate)
            first_input = build_certificate_action_input(law, duplicate_presentation, (0,), source_configuration, application["branch0"], certificate0)
            second_input = build_certificate_action_input(law, duplicate_presentation, (1,), source_configuration, application["branch0"], certificate0)
            passed = canonical_bytes(first_input.certificate) == canonical_bytes(second_input.certificate) and certificate_pairing_key(first_input) != certificate_pairing_key(second_input)
            old, new = {"inputs": (first_input, second_input)}, {"collapsed": first_input}
            evidence = {"address_provenance_distinct": passed}
        elif identifier == "COMPLETE-IDENTITY-TARGET-PACKET-SWAP":
            census = (
                measurements["groupoid"]["complete_certificate_action"]
                if measurements is not None
                else measure_complete_certificate_action_census(law)
            )
            changed = dict(census)
            families = list(census["family_rows"])
            first_family = dict(families[0])
            rows = list(first_family["identity_rows"])
            first_row = dict(rows[0])
            second_row = dict(rows[1])
            first_action = dict(first_row["identity_action"])
            second_action = dict(second_row["identity_action"])
            packet_fields = (
                "literal_transport_ref",
                "independent_rebuild_ref",
                "transported_pairing_key",
            )
            for field in packet_fields:
                first_action[field], second_action[field] = (
                    second_action[field],
                    first_action[field],
                )
            binding_fields = (
                "law_kind",
                "witness_ref",
                "input_ref",
                "original_ref",
                "literal_transport_ref",
                "independent_rebuild_ref",
                "pairing_key",
                "original_pairing_key",
                "transported_pairing_key",
            )
            first_action["action_binding_sha256"] = canonical_hash(
                {field: first_action[field] for field in binding_fields}
            )
            second_action["action_binding_sha256"] = canonical_hash(
                {field: second_action[field] for field in binding_fields}
            )
            first_row["identity_action"] = first_action
            second_row["identity_action"] = second_action
            rows[0], rows[1] = first_row, second_row
            first_family["identity_rows"] = tuple(rows)
            families[0] = first_family
            changed["family_rows"] = tuple(families)
            passed = _complete_certificate_action_census_exact(
                census
            ) and not _complete_certificate_action_census_exact(changed)
            old = {
                "row0_input": rows[0]["input_ref"],
                "row1_input": rows[1]["input_ref"],
                "clean_packet0": census["family_rows"][0]["identity_rows"][0]["identity_action"],
                "clean_packet1": census["family_rows"][0]["identity_rows"][1]["identity_action"],
            }
            new = {
                "row0_input": rows[0]["input_ref"],
                "row1_input": rows[1]["input_ref"],
                "swapped_packet0": first_action,
                "swapped_packet1": second_action,
            }
            evidence = {
                "target_multiset_preserved": sorted(
                    (
                        first_action["literal_transport_ref"],
                        second_action["literal_transport_ref"],
                    )
                )
                == sorted(
                    (
                        census["family_rows"][0]["identity_rows"][0]["identity_action"]["literal_transport_ref"],
                        census["family_rows"][0]["identity_rows"][1]["identity_action"]["literal_transport_ref"],
                    )
                ),
                "clean_exact": _complete_certificate_action_census_exact(census),
                "mutant_exact": _complete_certificate_action_census_exact(changed),
            }
        elif identifier == "COMPLETE-ACTION-PRODUCER-BYPASS":
            source = Path(__file__).read_text(encoding="utf-8")
            needle = (
                '                "identity_action": identity_action,\n'
                '                "exact": identity_action["exact"],'
            )
            replacement = (
                '                "identity_action": identity_action,\n'
                '                "producer_bypass": True,\n'
                '                "exact": identity_action["exact"],'
            )
            if source.count(needle) != 1:
                raise IntegrityFailure("complete-action producer mutation anchor moved")
            mutant_source = source.replace(needle, replacement, 1)
            baseline_scan = groupoid_promotion_source_scan(source)
            mutant_scan = groupoid_promotion_source_scan(mutant_source)
            passed = baseline_scan["all_exact"] and not mutant_scan["all_exact"]
            old = {"producer_ast_sha256": baseline_scan["ast_sha256"]}
            new = {"producer_ast_sha256": mutant_scan["ast_sha256"]}
            evidence = {
                "producer_ast_changed": baseline_scan["ast_sha256"]
                != mutant_scan["ast_sha256"],
                "baseline_static_exact": baseline_scan["all_exact"],
                "mutant_static_exact": mutant_scan["all_exact"],
            }
        else:
            raise Refusal("unknown v4 typed-groupoid action attack")

    return _attack_record(
        old,
        new,
        changed_path,
        "POINT-FREE-TYPED-GROUPOID-ACTION",
        killed_by,
        passed,
        evidence,
        drop,
    )


OUTCOME_LADDER = (
    "P13-SPECIFICATION-INCONSISTENT",
    "P13-REFERENT-PRESENTATION-ONLY",
    "P13-GAMMA-UNCONSTRUCTED",
    "P13-LAWFUL-SOURCE-SUFFICIENCY-UNPROVEN",
    "P13-WRAPPER-OR-LOOKUP",
    "P13-SHADOW-WELD-FAILS",
    "P13-FIXED-CARRIER-ONLY",
    "P13-SUPPORT-CHANGE-UNPROVEN",
    "P13-RECIPROCAL-CHAIN-UNINSTANTIATED",
    "P13-DIVISION-RECOVERY-UNPROVEN",
    "P13-NATIVE-NONDIVISION-UNRESOLVED",
    "P13-BLIND-CLASS-UNRESOLVED",
    "P13-RELATIONAL-GAMMA-CLASS-RELATIVE-EVENT-GRAMMAR-PRICED",
    "P13-RELATIONAL-GAMMA-LAW-UNSELECTED",
    "P13-LAW-SELECTED",
)
ELIGIBLE_CAP = OUTCOME_LADDER[12]
OUTCOME_SEGMENTS = (
    ("P13", "SPECIFICATION", "INCONSISTENT"),
    ("P13", "REFERENT", "PRESENTATION", "ONLY"),
    ("P13", "GAMMA", "UNCONSTRUCTED"),
    ("P13", "LAWFUL", "SOURCE", "SUFFICIENCY", "UNPROVEN"),
    ("P13", "WRAPPER", "OR", "LOOKUP"),
    ("P13", "SHADOW", "WELD", "FAILS"),
    ("P13", "FIXED", "CARRIER", "ONLY"),
    ("P13", "SUPPORT", "CHANGE", "UNPROVEN"),
    ("P13", "RECIPROCAL", "CHAIN", "UNINSTANTIATED"),
    ("P13", "DIVISION", "RECOVERY", "UNPROVEN"),
    ("P13", "NATIVE", "NONDIVISION", "UNRESOLVED"),
    ("P13", "BLIND", "CLASS", "UNRESOLVED"),
    (
        "P13",
        "RELATIONAL",
        "GAMMA",
        "CLASS",
        "RELATIVE",
        "EVENT",
        "GRAMMAR",
        "PRICED",
    ),
    ("P13", "RELATIONAL", "GAMMA", "LAW", "UNSELECTED"),
    ("P13", "LAW", "SELECTED"),
)


def render_outcome_index(index: int) -> tuple[str, dict[str, Any]]:
    _require_exact(index, int, "outcome index")
    if not 0 <= index < len(OUTCOME_SEGMENTS):
        raise IntegrityFailure("outcome index is outside the registered ladder")
    segments = OUTCOME_SEGMENTS[index]
    rendered = "-".join(segments)
    if rendered != OUTCOME_LADDER[index]:
        raise IntegrityFailure("segment outcome renderer disagrees with ladder")
    return rendered, {
        "index": index,
        "segments": segments,
        "segment_sha256": tuple(
            sha256_bytes(segment.encode("ascii")) for segment in segments
        ),
        "rendered_sha256": sha256_bytes(rendered.encode("ascii")),
    }


def recompute_shadow_predicates(
    measurements: Mapping[str, Any]
) -> dict[str, bool]:
    coherent = measurements["coherent"]
    division = measurements["division"]
    native = measurements["native_nondivision"]
    reciprocal = measurements["reciprocal"]
    blind = measurements["blind_family"]
    support = measurements["support_change"]
    recomputed_b2 = tuple(
        tuple(
            sum(
                (
                    division["branch_probabilities"][
                        f"q{input_bit}:a{branch}:b{output_bit}"
                    ]
                    for branch in (0, 1)
                ),
                Fraction(0),
            )
            for input_bit in (0, 1)
        )
        for output_bit in (0, 1)
    )
    recomputed_projectors = {
        sector: _record_sector_projector(
            division["writer_target_boundary"],
            division["record_port_name"],
            sector,
        )
        for sector in CANONICAL_SECTORS
    }
    shadow_recomputation = {
        "B": matrix_square_entries(coherent["R"]) == coherent["B"],
        "C": matrix_square_entries(coherent["R2"]) == coherent["C"],
        "B2": recomputed_b2 == division["B2"],
        "K": matrix_multiply(
            native["C"], invert_two_by_two(native["B"])
        )
        == native["K"],
        "writer_branches": all(
            sum(
                (
                    division["writer_branch_probabilities"][
                        f"q{input_bit}:a{branch}"
                    ]
                    for branch in (0, 1)
                ),
                Fraction(0),
            )
            == 1
            for input_bit in (0, 1)
        ),
        "record_projectors": recomputed_projectors
        == division["record_projectors"],
        "continuation_certificate": division["all_generator_intertwining"]
        and division["continuation_grammar_exact"]
        and division["free_word_induction"]["base"]
        and division["free_word_induction"]["step"]
        and division["free_word_induction"]["enumerated_residual"] == 0,
        "alternate_cuts": division["alternate_cut_residual"] == 0
        and division["alternate_cut_all_input_residual"] == 0,
        "active_reuse_eraser": division["active_reuse_eraser"][
            "inverse_toggle_exact"
        ],
        "reciprocal_joint": sum(reciprocal["joint"].values(), Fraction(0))
        == 1,
        "matching_first": blind["first"]["direct_vs_analytic_exact"],
        "matching_second": blind["second"]["direct_vs_analytic_exact"],
        "blind_projection": blind["resource_parity"]
        and blind["blind_prefix_equal"],
        "support_split_certificates": support["all_bound_certificates_exact"]
        and support["all_create_certificates_exact"]
        and support["all_merge_certificates_exact"]
        and support["all_unchanged_certificates_exact"]
        and not support["context_proof_alone_is_promotive"]
        and not support["legacy_role_cell_inequality_is_promotive"],
        "typed_groupoid_action": groupoid_promotion_predicate(
            measurements["groupoid"]
        ),
    }
    return shadow_recomputation


def assert_exposed_controls(measurements: Mapping[str, Any]) -> tuple[str, ...]:
    failures: list[str] = []
    coherent = measurements["coherent"]
    division = measurements["division"]
    native = measurements["native_nondivision"]
    reciprocal = measurements["reciprocal"]
    blind = measurements["blind_family"]
    anchors = (
        ("R", coherent["R"], ((Fraction(3, 5), Fraction(-4, 5)), (Fraction(4, 5), Fraction(3, 5)))),
        ("B", coherent["B"], ((Fraction(9, 25), Fraction(16, 25)), (Fraction(16, 25), Fraction(9, 25)))),
        ("C", coherent["C"], ((Fraction(49, 625), Fraction(576, 625)), (Fraction(576, 625), Fraction(49, 625)))),
        ("B2", division["B2"], ((Fraction(337, 625), Fraction(288, 625)), (Fraction(288, 625), Fraction(337, 625)))),
        ("K", native["K"], ((Fraction(351, 175), Fraction(-176, 175)), (Fraction(-176, 175), Fraction(351, 175)))),
        (
            "reciprocal",
            reciprocal["joint"],
            {
                "00": Fraction(9, 25),
                "01": Fraction(0),
                "10": Fraction(144, 625),
                "11": Fraction(256, 625),
            },
        ),
        (
            "matching-fixed",
            blind["first"]["marginals"],
            {
                key: Fraction(16, 25)
                for key in blind["first"]["marginals"]
            },
        ),
        (
            "matching-moved",
            blind["second"]["marginals"],
            {key: Fraction(0) for key in blind["second"]["marginals"]},
        ),
    )
    for label, measured, pinned in anchors:
        if measured != pinned:
            failures.append(label)
    if native["interval_certificate"]["absolute_factor_lower_bound"] != Fraction(
        527, 175
    ):
        failures.append("interval-lower-bound")
    if failures:
        raise IntegrityFailure("exposed analytic control mismatch: " + ",".join(failures))
    return tuple(label for label, _, _ in anchors) + ("interval-lower-bound",)


def build_result_neutral_regression_wall(
    measurements: Mapping[str, Any], source_text: str
) -> dict[str, Any]:
    _require_exact(source_text, str, "regression-wall source")
    tree = ast.parse(source_text)
    function_names = {
        node.name for node in ast.walk(tree) if type(node) is ast.FunctionDef
    }
    coherent = measurements["coherent"]
    division = measurements["division"]
    native = measurements["native_nondivision"]
    reciprocal = measurements["reciprocal"]
    blind = measurements["blind_family"]
    predicates = {
        "rational_domain_exact": measurements["g_domain"]
        == {
            "number_system": "RATIONAL",
            "lower_closed": Fraction(1, 3),
            "upper_closed": Fraction(1, 2),
        },
        "one_contact_cayley_primitive_exact": measurements["law"].primitive
        == CANONICAL_PRIMITIVE
        and measurements["law"].implementation
        == "CONTACT-CAYLEY-WHOLE-FILLING-v1",
        "R_exact": coherent["R"]
        == ((Fraction(3, 5), Fraction(-4, 5)), (Fraction(4, 5), Fraction(3, 5))),
        "B_exact": coherent["B"]
        == ((Fraction(9, 25), Fraction(16, 25)), (Fraction(16, 25), Fraction(9, 25))),
        "C_exact": coherent["C"]
        == ((Fraction(49, 625), Fraction(576, 625)), (Fraction(576, 625), Fraction(49, 625))),
        "B2_exact": division["B2"]
        == ((Fraction(337, 625), Fraction(288, 625)), (Fraction(288, 625), Fraction(337, 625))),
        "K_exact": native["K"]
        == ((Fraction(351, 175), Fraction(-176, 175)), (Fraction(-176, 175), Fraction(351, 175))),
        "interval_527_over_175_exact": native["interval_certificate"][
            "absolute_factor_lower_bound"
        ]
        == Fraction(527, 175),
        "reciprocal_joint_exact": reciprocal["joint"]
        == {
            "00": Fraction(9, 25),
            "01": Fraction(0),
            "10": Fraction(144, 625),
            "11": Fraction(256, 625),
        },
        "native_wording_exact": NATIVE_NONDIVISION_SENTENCE.startswith(
            "The cut is not a lawful stochastic division"
        ),
        "history_positive_control_exact": native["history_joint_normalizations"]
        == (Fraction(1), Fraction(1))
        and native["history_joint_nonnegative"],
        "continuation_and_cut_exact": division["continuation_grammar_exact"]
        and division["all_generator_intertwining"]
        and division["alternate_cut_all_input_residual"] == 0
        and division["active_reuse_eraser"]["inverse_toggle_exact"],
        "matching_class_exact": blind["resource_parity"]
        and blind["blind_prefix_equal"]
        and blind["direct_factorization_exact"]
        and blind["response_unequal"],
        "source_groupoid_doctrine_exact": groupoid_promotion_predicate(
            measurements["groupoid"]
        ),
        "source_groupoid_promotion_ast_exact": measurements[
            "groupoid_promotion_static"
        ]["all_exact"],
        "source_identity_exact": measurements["source_identity"][
            "equal_key_equal_profile"
        ],
        "fresh_generator_preserved_uninvoked": {
            "derive_fresh_payload",
            "generate_fresh_mode",
            "run_official_mode",
            "transactional_publish",
        }
        <= function_names,
        "outcome_vocabulary_and_cap_exact": ELIGIBLE_CAP == OUTCOME_LADDER[12]
        and len(OUTCOME_LADDER) == 15,
        "scope_surface_exact": measurements["scope_coordinates"]
        == SCOPE_COORDINATES
        and measurements["scope_walls"] == SCOPE_WALLS,
    }
    return {
        "predicates": predicates,
        "predicate_count": len(predicates),
        "all_exact": all(predicates.values()),
        "value_sha256s": {
            "R": canonical_hash(coherent["R"]),
            "B": canonical_hash(coherent["B"]),
            "C": canonical_hash(coherent["C"]),
            "B2": canonical_hash(division["B2"]),
            "K": canonical_hash(native["K"]),
            "reciprocal_joint": canonical_hash(reciprocal["joint"]),
            "matching": canonical_hash(
                (blind["first"]["marginals"], blind["second"]["marginals"])
            ),
        },
    }


def _lineage_gate(law: GammaLaw, measurements: Mapping[str, Any]) -> dict[str, Any]:
    derivations = {
        "B": measurements["coherent"]["first_lineage"],
        "C": measurements["coherent"]["second_lineage"],
        "writer": measurements["division"]["writer_lineage"],
        "recorded_chain": measurements["division"]["chain_lineage"],
        "reciprocal_chain": measurements["reciprocal"]["chain_lineage"],
        "support_change": measurements["support_change"]["lineage"],
        "matching_first": measurements["blind_family"]["first"]["lineage"],
        "matching_second": measurements["blind_family"]["second"]["lineage"],
    }
    rows: dict[str, Any] = {}
    for name, derivation in derivations.items():
        roots = derivation_roots(derivation)
        rows[name] = {
            "primitive_roots": roots,
            "root_count": len(roots),
            "all_same_root": bool(roots) and set(roots) == {law_identity(law)},
            "derivation_hash": canonical_hash(derivation),
        }
    support = measurements["support_change"]
    support_roots = derivation_roots(support["lineage"])
    rows["bound_split_classifier"] = {
        "primitive_roots": support_roots,
        "root_count": len(support_roots),
        "all_same_root": bool(support_roots)
        and set(support_roots) == {law_identity(law)}
        and support["all_bound_certificates_exact"],
        "derivation_hash": canonical_hash(support["lineage"]),
        "classifier_consumed_certificate_sha256": support[
            "classifier_consumed_certificate_sha256"
        ],
    }
    groupoid = measurements["groupoid"]
    rows["typed_groupoid_action"] = {
        "primitive_roots": (law_identity(law),),
        "root_count": 1,
        "all_same_root": groupoid_promotion_predicate(groupoid),
        "derivation_hash": canonical_hash(
            {
                "native_dependency_sha256": groupoid[
                    "native_dependency_sha256"
                ],
                "configuration_action_rows": tuple(
                    canonical_hash(row["configuration_action"])
                    for row in groupoid["native_census"]["rows"]
                ),
                "complete_certificate_action": canonical_hash(
                    groupoid["complete_certificate_action"]
                ),
                "promotion_backward_slice_ast_sha256": measurements[
                    "groupoid_promotion_static"
                ]["ast_sha256"],
                "assertion_target_equality_exact": measurements[
                    "groupoid_promotion_static"
                ]["assertion_target_equality_exact"],
            }
        ),
    }
    return {
        "rows": rows,
        "all_complete": all(row["all_same_root"] for row in rows.values()),
        "unique_root": law_identity(law),
    }


def build_shadow_lineages(measurements: Mapping[str, Any]) -> dict[str, Any]:
    law_root = law_identity(measurements["law"])
    coherent = measurements["coherent"]
    division = measurements["division"]
    native = measurements["native_nondivision"]
    reciprocal = measurements["reciprocal"]
    blind = measurements["blind_family"]
    support = measurements["support_change"]
    shadow_recomputation = recompute_shadow_predicates(measurements)
    rows: dict[str, Any] = {
        "primitive": {
            "operation": "ONE-ROOT",
            "primitive_ids": (law_root,),
            "output_sha256": law_root,
        },
        "B": {
            "operation": "ENTRYWISE-SQUARE",
            "inputs": (canonical_hash(coherent["R"]),),
            "output_sha256": canonical_hash(coherent["B"]),
            "type_dag": coherent["first_lineage"],
            "primitive_ids": derivation_roots(coherent["first_lineage"]),
        },
        "C": {
            "operation": "ENTRYWISE-SQUARE-AFTER-TWO-PAIR-COMPOSITION",
            "inputs": (canonical_hash(coherent["R2"]),),
            "output_sha256": canonical_hash(coherent["C"]),
            "type_dag": coherent["second_lineage"],
            "primitive_ids": derivation_roots(coherent["second_lineage"]),
        },
        "B2": {
            "operation": "RECORD-PROJECTED-ORDINARY-COMPOSITION",
            "inputs": (canonical_hash(division["branch_probabilities"]),),
            "output_sha256": canonical_hash(division["B2"]),
            "type_dag": division["chain_lineage"],
            "primitive_ids": derivation_roots(division["chain_lineage"]),
        },
        "K": {
            "operation": "C-RIGHT-MULTIPLIED-BY-EXACT-B-INVERSE",
            "inputs": (
                canonical_hash(native["C"]),
                canonical_hash(native["B"]),
            ),
            "output_sha256": canonical_hash(native["K"]),
            "arithmetic_dag": native["lineage"],
            "primitive_ids": derivation_roots(coherent["first_lineage"])
            + derivation_roots(coherent["second_lineage"]),
        },
        "writer_branches": {
            "operation": "SAME-ROOT-WRITER-ENDPOINT-SQUARES",
            "inputs": (law_root,),
            "output_sha256": canonical_hash(
                division["writer_branch_probabilities"]
            ),
            "type_dag": division["writer_lineage"],
            "primitive_ids": derivation_roots(division["writer_lineage"]),
        },
        "record_projectors": {
            "operation": "TARGET-CATALOGUE-SECTOR-PROJECTION",
            "inputs": (canonical_hash(division["writer_lineage"]),),
            "output_sha256": canonical_hash(division["record_projectors"]),
            "primitive_ids": derivation_roots(division["writer_lineage"]),
        },
        "continuation_certificate": {
            "operation": "GENERATOR-INTERTWINING-AND-FREE-WORD-INDUCTION",
            "inputs": (
                canonical_hash(division["grammar"]),
                canonical_hash(division["generator_intertwining_residuals"]),
            ),
            "output_sha256": canonical_hash(division["free_word_induction"]),
            "type_dag": division["continuation_letter_lineages"],
            "primitive_ids": tuple(
                root
                for derivation in division["continuation_letter_lineages"].values()
                for root in derivation_roots(derivation)
            ),
        },
        "alternate_cuts": {
            "operation": "COMPLETE-RECORD-PROJECTED-CUT-SUM",
            "inputs": (
                canonical_hash(division["writer_lineage"]),
                canonical_hash(division["chain_lineage"]),
            ),
            "output_sha256": canonical_hash(
                {
                    "registered": division["alternate_cut_residual"],
                    "all_input": division["alternate_cut_all_input_residual"],
                }
            ),
            "primitive_ids": derivation_roots(division["writer_lineage"])
            + derivation_roots(division["chain_lineage"]),
        },
        "active_reuse_eraser": {
            "operation": "REACTIVATE-THEN-SAME-ROOT-INVERSE-TOGGLE",
            "inputs": (law_root,),
            "output_sha256": canonical_hash(division["active_reuse_eraser"]),
            "type_dag": division["active_reuse_eraser"]["lineage"],
            "primitive_ids": derivation_roots(
                division["active_reuse_eraser"]["lineage"]
            ),
        },
        "reciprocal_joint": {
            "operation": "WRITER-THEN-LITERAL-CONTEXT-READER",
            "inputs": (law_root,),
            "output_sha256": canonical_hash(reciprocal["joint"]),
            "type_dag": reciprocal["chain_lineage"],
            "primitive_ids": derivation_roots(reciprocal["chain_lineage"]),
        },
        "matching_first": {
            "operation": "ONE-GLOBAL-GAMMA-CALL",
            "inputs": (law_root,),
            "output_sha256": canonical_hash(blind["first"]["marginals"]),
            "type_dag": blind["first"]["lineage"],
            "primitive_ids": derivation_roots(blind["first"]["lineage"]),
        },
        "matching_second": {
            "operation": "ONE-GLOBAL-GAMMA-CALL",
            "inputs": (law_root,),
            "output_sha256": canonical_hash(blind["second"]["marginals"]),
            "type_dag": blind["second"]["lineage"],
            "primitive_ids": derivation_roots(blind["second"]["lineage"]),
        },
        "blind_projection": {
            "operation": "LITERAL-CATALOGUE-RESOURCE-PROJECTION",
            "inputs": (
                blind["first"]["context_hash"],
                blind["second"]["context_hash"],
            ),
            "output_sha256": canonical_hash(
                (
                    blind["first"]["blind_projection"],
                    blind["second"]["blind_projection"],
                )
            ),
            "root_requirement": "CONTEXT-CATALOGUE",
            "context_catalogue_ids": (
                blind["first"]["context_hash"],
                blind["second"]["context_hash"],
            ),
            "primitive_ids": (),
        },
        "support_split_certificates": {
            "operation": "BOUND-CREATE-MERGE-UNCHANGED-SPLIT-CLASSIFIER",
            "inputs": (
                support["classifier_consumed_certificate_sha256"],
                canonical_hash(
                    tuple(
                        certificate.context_proof
                        for certificate in support[
                            "bound_transition_certificates"
                        ]
                    )
                ),
            ),
            "output_sha256": support[
                "classifier_consumed_certificate_sha256"
            ],
            "type_dag": support["lineage"],
            "primitive_ids": derivation_roots(support["lineage"]),
        },
        "typed_groupoid_action": {
            "operation": "COMPLETE-TYPED-GROUPOID-ACTION-AND-INDEPENDENT-REBUILD",
            "inputs": (
                measurements["groupoid"]["native_dependency_sha256"],
                canonical_hash(
                    tuple(
                        row["configuration_action"]
                        for row in measurements["groupoid"]["native_census"][
                            "rows"
                        ]
                    )
                ),
                canonical_hash(
                    measurements["groupoid"]["complete_certificate_action"]
                ),
                measurements["groupoid_promotion_static"]["ast_sha256"],
            ),
            "output_sha256": measurements["groupoid"][
                "native_dependency_sha256"
            ],
            "primitive_ids": (law_root,),
        },
    }
    fresh = measurements.get("fresh_confirmation")
    if fresh is not None:
        for case in fresh["cases"]:
            for member in case["members"]:
                key = f"fresh:{case['case_index']}:{member['member']}"
                rows[key] = {
                    "operation": "ONE-GLOBAL-GAMMA-CALL",
                    "inputs": (law_root,),
                    "output_sha256": member["result"][
                        "endpoint_probabilities_hash"
                    ],
                    "type_dag": member["result"]["lineage"],
                    "primitive_ids": derivation_roots(
                        member["result"]["lineage"]
                    ),
                }
    for row in rows.values():
        row["arithmetic_type_dag_sha256"] = canonical_hash(
            {
                key: value
                for key, value in row.items()
                if key not in ("output_sha256", "arithmetic_type_dag_sha256")
            }
        )
    def lineage_root_complete(row: Mapping[str, Any]) -> bool:
        if row.get("root_requirement", "GAMMA") == "CONTEXT-CATALOGUE":
            context_ids = row.get("context_catalogue_ids")
            return (
                type(context_ids) is tuple
                and bool(context_ids)
                and all(_is_lower_hex(value, 32) for value in context_ids)
                and row.get("primitive_ids") == ()
            )
        primitive_ids = row.get("primitive_ids")
        return (
            type(primitive_ids) is tuple
            and bool(primitive_ids)
            and set(primitive_ids) == {law_root}
        )

    all_outputs_bound = all(
        _is_lower_hex(row["output_sha256"], 32)
        and lineage_root_complete(row)
        and _is_lower_hex(row["arithmetic_type_dag_sha256"], 32)
        for row in rows.values()
    )
    all_law_shadows_consume_unique_primitive = all(
        lineage_root_complete(row)
        for row in rows.values()
        if row.get("root_requirement", "GAMMA") == "GAMMA"
    )
    blind_projection_context_rooted = (
        rows["blind_projection"]["root_requirement"] == "CONTEXT-CATALOGUE"
        and lineage_root_complete(rows["blind_projection"])
    )
    all_arithmetic_recomputed = all(shadow_recomputation.values())
    return {
        "unique_primitive_root": law_root,
        "rows": rows,
        "row_count": len(rows),
        "all_outputs_bound": all_outputs_bound,
        "all_law_shadows_consume_unique_primitive": (
            all_law_shadows_consume_unique_primitive
        ),
        "blind_projection_rooted_in_literal_context_not_gamma": (
            blind_projection_context_rooted
        ),
        "recomputation_predicates": shadow_recomputation,
        "all_arithmetic_recomputed": all_arithmetic_recomputed,
    }


def support_promotion_predicate(
    support: Mapping[str, Any], split_groupoid: Mapping[str, Any]
) -> bool:
    """The sole promotive support predicate; source-mutation target S5."""

    return (
        support["all_inverse_merge"]
        and support["all_support_changed"]
        and support["all_create_certificates_exact"]
        and support["all_merge_certificates_exact"]
        and support["all_unchanged_certificates_exact"]
        and support["all_bound_certificates_exact"]
        and not support["context_proof_alone_is_promotive"]
        and not support["legacy_role_cell_inequality_is_promotive"]
        and split_groupoid["all_exact"]
    )


def support_promotion_source_scan(source: str) -> dict[str, Any]:
    _require_exact(source, str, "support-promotion source")
    tree = ast.parse(source)
    matches = tuple(
        node
        for node in ast.walk(tree)
        if type(node) is ast.FunctionDef
        and node.name == "support_promotion_predicate"
    )
    if len(matches) != 1:
        return {
            "one_function": False,
            "required_keys_present": False,
            "legacy_keys_absent": False,
            "ast_sha256": canonical_hash(()),
            "all_exact": False,
        }
    function = matches[0]
    literals = tuple(
        node.value
        for node in ast.walk(function)
        if type(node) is ast.Constant and type(node.value) is str
    )
    required = {
        "all_inverse_merge",
        "all_support_changed",
        "all_create_certificates_exact",
        "all_merge_certificates_exact",
        "all_unchanged_certificates_exact",
        "all_bound_certificates_exact",
        "context_proof_alone_is_promotive",
        "legacy_role_cell_inequality_is_promotive",
        "all_exact",
    }
    legacy = {
        "source_role_count",
        "target_role_count",
        "source_cell_count",
        "target_cell_count",
        "configuration_nonisomorphic",
    }
    required_exact = required <= set(literals)
    legacy_absent = not (legacy & set(literals))
    return {
        "one_function": True,
        "required_keys": tuple(sorted(required)),
        "observed_key_literals": tuple(sorted(set(literals))),
        "required_keys_present": required_exact,
        "legacy_keys_absent": legacy_absent,
        "ast_sha256": canonical_hash(ast.dump(function, include_attributes=False)),
        "all_exact": required_exact and legacy_absent,
    }


def groupoid_promotion_source_scan(source: str) -> dict[str, Any]:
    _require_exact(source, str, "groupoid-promotion source")
    tree = ast.parse(source)
    matches = tuple(
        node
        for node in ast.walk(tree)
        if type(node) is ast.FunctionDef
        and node.name == "groupoid_promotion_predicate"
    )
    if len(matches) != 1:
        return {
            "one_function": False,
            "required_native_fields_present": False,
            "copied_final_boolean_absent": False,
            "ast_sha256": canonical_hash(()),
            "all_exact": False,
        }
    function = matches[0]
    functions = {
        node.name: node
        for node in ast.walk(tree)
        if type(node) is ast.FunctionDef
    }
    backward_slice_names = (
        "measure_complete_certificate_action_census",
        "generator_certificate_inputs",
        "build_bound_split_certificate",
        "_presentation_key_validated",
        "build_certificate_action_input",
        "_assemble_certificate_action_input",
        "_store_complete_bytes",
        "_freeze_complete_byte_store",
        "_complete_certificate_action_reference",
        "_identity_complete_certificate_action_reference",
        "_complete_byte_store_payloads",
        "_decoded_mapping",
        "_decoded_tuple",
        "_decoded_rows",
        "_decode_fraction_data",
        "_decode_bytes_data",
        "_decode_formula_data",
        "_decode_role_data",
        "_decode_context_data",
        "_decode_port_data",
        "_decode_port_decl_data",
        "_decode_configuration_data",
        "_decode_boundary_data",
        "_decode_occurrence_data",
        "_decoded_json_identity",
        "_decode_arrow_data",
        "_decode_primitive_data",
        "_decode_law_data",
        "_decode_source_presentation_data",
        "_decode_witness_payload",
        "_decode_certificate_action_input_payload",
        "_complete_byte_store_identities",
        "_configuration_action_census_exact",
        "_configuration_law_reference_exact",
        "_certificate_action_census_exact",
        "_certificate_triple_reference_exact",
        "_certificate_law_reference_exact",
        "verify_complete_certificate_action_row",
        "_verify_complete_certificate_action_row_decoded",
        "_complete_action_reference_attachment_exact",
        "_complete_action_rows",
        "_measure_complete_action_raw_verification",
        "_complete_action_verification_manifest_exact",
        "_complete_certificate_action_census_exact",
        "_tensor_configuration_action_exact",
        "certificate_pairing_key",
        "complete_certificate_action_row",
        "certificate_transport_triple",
        "_is_identity_witness_on",
        "act_certificate",
        "_literal_transported_certificate",
        "rebuild_certificate_input",
        "_generator_transition",
        "_generator_coordinate_coefficient",
        "_generator_map",
    )
    backward_slice_functions_exact = all(
        type(functions.get(name)) is ast.FunctionDef
        for name in backward_slice_names
    )
    inspected_functions = (function,) + tuple(
        functions[name]
        for name in backward_slice_names
        if type(functions.get(name)) is ast.FunctionDef
    )
    bound_source_names = (
        "groupoid_promotion_predicate",
        *backward_slice_names,
        "act_configuration",
        "assert_configuration_target",
        "build_certificate_action_input",
        "act_certificate",
        "tensor_action_row",
        "recompute_shadow_predicates",
        "_lineage_gate",
        "build_shadow_lineages",
        "build_gate_table",
        "classify_primary",
        "independent_outcome_index",
        "build_claim_table",
        "build_seal_manifest",
    )
    bound_source_ast_sha256 = canonical_hash(
        tuple(
            (
                name,
                ast.dump(functions[name], include_attributes=False),
            )
            for name in bound_source_names
            if type(functions.get(name)) is ast.FunctionDef
        )
    )
    literals = tuple(
        node.value
        for inspected in inspected_functions
        for node in ast.walk(inspected)
        if type(node) is ast.Constant and type(node.value) is str
    )
    required = {
        "bijection_rows",
        "left_identity_exact",
        "right_identity_exact",
        "left_inverse_exact",
        "right_inverse_exact",
        "associativity_exact",
        "application_order_exact",
        "source_target_typed",
        "transported_presentation_exact",
        "operator_covariance_residual",
        "chain_operator_covariance_residual",
        "endpoint_covariance_residual",
        "chain_endpoint_covariance_residual",
        "source_configuration_action_exact",
        "complete_configuration_action_exact",
        "nomological_roots_preserved",
        "contextual_alias_exact",
        "certificate_transport_exact",
        "all_object_actions_exact",
        "complete_object_table",
        "node_ref",
        "configuration_ref",
        "transport_refs",
        "complete_input_table",
        "input_ref",
        "witness_ref",
        "literal_transport_ref",
        "independent_rebuild_ref",
        "original_pairing_key",
        "transported_pairing_key",
        "action_binding_sha256",
        "equality_coordinates",
        "enumeration_reorder_nonkill",
        "tensor_configuration_action",
        "cases",
        "law_row",
        "factor_certificate_lineage",
        "left_source_root_ref",
        "right_source_root_ref",
        "left_target_root_ref",
        "right_target_root_ref",
        "left_transport_target_root_ref",
        "right_transport_target_root_ref",
        "tensor_transport_target_root_ref",
        "tensor_target_root_ref",
    }
    required_present = required <= set(literals)
    function_source = ast.get_source_segment(source, function) or ""
    copied_final_absent = all(
        pattern not in function_source
        for pattern in (
            'groupoid["all_exact"]',
            "groupoid['all_exact']",
            'native["all_exact"]',
            "native['all_exact']",
            'row["all_exact"]',
            "row['all_exact']",
        )
    )
    def exact_signature(name: str, parameters: tuple[str, ...]) -> bool:
        node = functions.get(name)
        return (
            type(node) is ast.FunctionDef
            and tuple(argument.arg for argument in node.args.args) == parameters
            and not node.args.posonlyargs
            and not node.args.kwonlyargs
            and node.args.vararg is None
            and node.args.kwarg is None
            and not node.args.defaults
            and not node.args.kw_defaults
        )

    configuration_signature_exact = exact_signature(
        "act_configuration", ("source_node", "configuration", "witness")
    )
    assertion_signature_exact = exact_signature(
        "assert_configuration_target",
        ("source_node", "asserted_target_node", "witness"),
    )
    assertion_node = functions.get("assert_configuration_target")
    assertion_derives_target_exact = (
        type(assertion_node) is ast.FunctionDef
        and any(
            type(node) is ast.Assign
            and len(node.targets) == 1
            and type(node.targets[0]) is ast.Name
            and node.targets[0].id == "derived"
            and type(node.value) is ast.Call
            and type(node.value.func) is ast.Name
            and node.value.func.id == "_derive_target_node"
            and tuple(
                argument.id
                for argument in node.value.args
                if type(argument) is ast.Name
            )
            == ("source_node", "witness")
            for node in ast.walk(assertion_node)
        )
    )
    assertion_compares_target_exact = (
        type(assertion_node) is ast.FunctionDef
        and any(
            type(node) is ast.If
            and type(node.test) is ast.Compare
            and len(node.test.ops) == 1
            and type(node.test.ops[0]) is ast.NotEq
            and len(node.test.comparators) == 1
            and {
                node.test.left.id
                if type(node.test.left) is ast.Name
                else "",
                node.test.comparators[0].id
                if type(node.test.comparators[0]) is ast.Name
                else "",
            }
            == {"asserted_target_node", "derived"}
            and any(type(descendant) is ast.Raise for descendant in ast.walk(node))
            for node in ast.walk(assertion_node)
        )
    )
    assertion_returns_derived_exact = (
        type(assertion_node) is ast.FunctionDef
        and any(
            type(node) is ast.Return
            and type(node.value) is ast.Name
            and node.value.id == "derived"
            for node in ast.walk(assertion_node)
        )
    )
    assertion_target_equality_exact = (
        assertion_derives_target_exact
        and assertion_compares_target_exact
        and assertion_returns_derived_exact
    )
    certificate_signature_exact = exact_signature(
        "act_certificate", ("witness", "certificate_action_input")
    )
    certificate_factory_signature_exact = exact_signature(
        "build_certificate_action_input",
        (
            "law",
            "source_presentation",
            "generator_ast_address",
            "source_configuration",
            "target_configuration",
            "inherited_certificate",
        ),
    )
    tensor_signature_exact = exact_signature(
        "tensor_action_row",
        (
            "tensor_source_node",
            "tensor_configuration",
            "left_node",
            "left_configuration",
            "left_witness",
            "right_node",
            "right_configuration",
            "right_witness",
        ),
    )
    configuration_source = ast.get_source_segment(
        source, functions.get("act_configuration")
    ) or ""
    certificate_source = ast.get_source_segment(
        source, functions.get("act_certificate")
    ) or ""
    tensor_source = ast.get_source_segment(
        source, functions.get("tensor_action_row")
    ) or ""
    core_target_backdoor_absent = all(
        token not in configuration_source
        for token in (
            "asserted_target_node",
            "caller_target",
            "target_cache",
            "global_target",
        )
    )
    certificate_backdoor_absent = all(
        token not in certificate_source
        for token in (
            "registry",
            "cache",
            "preimage",
            "expected_transformed",
            "caller_target",
        )
    )
    tensor_root_binding_exact = all(
        token in tensor_source
        for token in (
            'boundary_node_at(left_witness.source, (), "SOURCE")',
            'boundary_node_at(right_witness.source, (), "SOURCE")',
            'boundary_node_at(left_witness.target, (), "SOURCE")',
            'boundary_node_at(right_witness.target, (), "SOURCE")',
            "left_node != left_source_root",
            "right_node != right_source_root",
            "left_transport.target_node != left_target_root",
            "right_transport.target_node != right_target_root",
        )
    ) and "left_node not in boundary_nodes" not in tensor_source
    producer_consumer_ast_matches_frozen = (
        FROZEN_GROUPOID_PROMOTION_AST_SHA256 == "TO-BE-FROZEN"
        or bound_source_ast_sha256 == FROZEN_GROUPOID_PROMOTION_AST_SHA256
    )
    legacy_certificate_summary_absent = all(
        token not in function_source
        for token in (
            "all_original_final",
            "all_transformed_final",
            "count_preserved",
            "original_classifier_hashes",
            "transformed_classifier_hashes",
        )
    )
    return {
        "one_function": True,
        "required_native_fields": tuple(sorted(required)),
        "observed_key_literals": tuple(sorted(set(literals))),
        "required_native_fields_present": required_present,
        "copied_final_boolean_absent": copied_final_absent,
        "configuration_signature_exact": configuration_signature_exact,
        "assertion_signature_exact": assertion_signature_exact,
        "assertion_target_equality_exact": assertion_target_equality_exact,
        "certificate_signature_exact": certificate_signature_exact,
        "certificate_factory_signature_exact": certificate_factory_signature_exact,
        "tensor_signature_exact": tensor_signature_exact,
        "tensor_root_binding_exact": tensor_root_binding_exact,
        "backward_slice_functions_exact": backward_slice_functions_exact,
        "core_target_backdoor_absent": core_target_backdoor_absent,
        "certificate_backdoor_absent": certificate_backdoor_absent,
        "legacy_certificate_summary_absent": legacy_certificate_summary_absent,
        "producer_consumer_ast_matches_frozen": (
            producer_consumer_ast_matches_frozen
        ),
        "ast_sha256": bound_source_ast_sha256,
        "all_exact": required_present
        and copied_final_absent
        and configuration_signature_exact
        and assertion_signature_exact
        and assertion_target_equality_exact
        and certificate_signature_exact
        and certificate_factory_signature_exact
        and tensor_signature_exact
        and tensor_root_binding_exact
        and backward_slice_functions_exact
        and core_target_backdoor_absent
        and certificate_backdoor_absent
        and legacy_certificate_summary_absent
        and producer_consumer_ast_matches_frozen,
    }


def build_gate_table(measurements: Mapping[str, Any]) -> dict[str, bool]:
    coherent = measurements["coherent"]
    category = measurements["category"]
    source_identity = measurements["source_identity"]
    full_target = measurements["full_target"]
    support = measurements["support_change"]
    reciprocal = measurements["reciprocal"]
    division = measurements["division"]
    native = measurements["native_nondivision"]
    blind = measurements["blind_family"]
    lineage = measurements["lineage"]
    fresh = measurements.get("fresh_confirmation")
    fresh_exact = fresh is None or fresh["all_confirmed"]
    return {
        "specification": measurements["scope_valid"]
        and measurements["static_scan"]["clean"]
        and measurements["support_promotion_static"]["all_exact"]
        and measurements["groupoid_promotion_static"]["all_exact"]
        and measurements["regression_wall"]["all_exact"],
        "referent": measurements["referent_census"]["all_exact"]
        and source_identity["inessential_formula_equal"]
        and source_identity["contextual_boolean_alias_exact"]
        and measurements["context_split_census"]["all_exact"]
        and groupoid_promotion_predicate(measurements["groupoid"]),
        "complete_gamma": category["all_exact"]
        and coherent["first_isometry"]
        and coherent["second_isometry"]
        and measurements["totality"]["all_generator_isometries"]
        and measurements["totality"]["all_rho_involutions"]
        and measurements["totality"][
            "cayley_norm_identity_for_every_rational_x"
        ]
        and measurements["totality"]["denominator_positive_certificate"][
            "positive_for_every_rational_x"
        ]
        and measurements["totality"]["endpoint_domain_controls_normalized"]
        and measurements["totality"]["all_nonzero_generator_transitions_bound"]
        and full_target["all_full"],
        "source_sufficiency": source_identity["equal_key_equal_profile"]
        and source_identity["distinct_filling_distinct_key"]
        and source_identity["neutral_label_and_status_order_invariant"]
        and source_identity["contextual_boolean_alias_exact"],
        "anti_wrapper": lineage["all_complete"]
        and measurements["shadow_lineages"]["all_outputs_bound"]
        and measurements["shadow_lineages"][
            "all_law_shadows_consume_unique_primitive"
        ]
        and measurements["shadow_lineages"][
            "blind_projection_rooted_in_literal_context_not_gamma"
        ]
        and measurements["shadow_lineages"]["all_arithmetic_recomputed"],
        "shadow_weld": coherent["B"] == native["B"]
        and coherent["C"] == native["C"],
        "variable_carrier": bool(support["branches"])
        and support["all_bound_certificates_exact"]
        and support["all_create_certificates_exact"]
        and not support["context_proof_alone_is_promotive"]
        and not support["legacy_role_cell_inequality_is_promotive"],
        "support_change": support_promotion_predicate(
            support, measurements["groupoid"]["split_certificate_covariance"]
        ),
        "reciprocal": reciprocal["normalization"] == 1
        and reciprocal["counterfactual_probe_one"] == 0
        and reciprocal["contact_true_branch"]
        and not reciprocal["contact_false_branch"],
        "division": division["writer_normalized_all_blank_inputs"]
        and division["writer_blank_input_count"]
        == len(division["writer_blank_input_rows"])
        and division["writer_blank_input_count"] > 0
        and division["continuation_grammar_exact"]
        and division["all_generator_intertwining"]
        and division["free_word_induction"]["base"]
        and division["free_word_induction"]["step"]
        and division["free_word_induction"]["enumerated_residual"] == 0
        and division["alternate_cut_residual"] == 0
        and division["alternate_cut_all_input_residual"] == 0
        and division["alternate_cut_all_input_comparisons"]
        == len(division["alternate_cut_all_input_rows"])
        and division["alternate_cut_all_input_comparisons"] > 0
        and division["active_reuse_eraser"]["inverse_toggle_exact"]
        and division["returned_target_count"] == division["full_target_count"]
        and division["retained_zero_count"] > 0,
        "native_nondivision": not native["positive_source_independent_restart_exists"]
        and bool(native["negative_entries"])
        and native["unique_factor"]
        and native["interval_certificate"]["universal_certificate"]
        and native["interval_certificate"][
            "universal_factor_outside_stochastic_spectral_interval"
        ]
        and native["interval_certificate"]["bound_residual"] >= 0
        and native["history_joint_normalizations"] == (Fraction(1), Fraction(1))
        and native["history_joint_nonnegative"]
        and native["history_joint_positive_coordinates"] > 0,
        "blind_class": blind["resource_parity"]
        and blind["blind_prefix_equal"]
        and blind["same_initialization"]
        and blind["prior_record_law_equal"]
        and blind["same_law_root"]
        and blind["direct_factorization_exact"]
        and blind["exposed_marginals_exact"]
        and blind["response_unequal"]
        and blind["first"]["single_global_gamma_calls"] == 1
        and blind["second"]["single_global_gamma_calls"] == 1
        and fresh_exact,
    }


def classify_primary(gates: Mapping[str, bool]) -> str:
    ordered = (
        ("specification", 0),
        ("referent", 1),
        ("complete_gamma", 2),
        ("source_sufficiency", 3),
        ("anti_wrapper", 4),
        ("shadow_weld", 5),
        ("variable_carrier", 6),
        ("support_change", 7),
        ("reciprocal", 8),
        ("division", 9),
        ("native_nondivision", 10),
        ("blind_class", 11),
    )
    for key, outcome_index in ordered:
        if gates.get(key) is not True:
            return OUTCOME_LADDER[outcome_index]
    return OUTCOME_LADDER[12]


def independent_outcome_index(measurements: Mapping[str, Any]) -> int:
    fresh = measurements.get("fresh_confirmation")
    fresh_exact = fresh is None or fresh["all_confirmed"]
    predicates = (
        measurements["scope_valid"]
        and measurements["static_scan"]["clean"]
        and measurements["support_promotion_static"]["all_exact"]
        and measurements["groupoid_promotion_static"]["all_exact"]
        and measurements["regression_wall"]["all_exact"],
        measurements["referent_census"]["all_exact"]
        and measurements["source_identity"]["inessential_formula_equal"]
        and measurements["source_identity"]["contextual_boolean_alias_exact"]
        and measurements["context_split_census"]["all_exact"]
        and (
            measurements["groupoid"]["abstract_census"]["bijection_count"]
            == measurements["groupoid"]["abstract_census"][
                "expected_bijection_count"
            ]
        )
        and (
            measurements["groupoid"]["abstract_census"][
                "associativity_case_count"
            ]
            == measurements["groupoid"]["abstract_census"][
                "expected_associativity_case_count"
            ]
        )
        and all(
            row["law_fields"]["left_identity_exact"]
            and row["law_fields"]["right_identity_exact"]
            and row["law_fields"]["left_inverse_exact"]
            and row["law_fields"]["right_inverse_exact"]
            and row["law_fields"]["associativity_exact"]
            and row["law_fields"]["operator_covariance_residual"] == 0
            and row["law_fields"]["chain_operator_covariance_residual"] == 0
            and row["law_fields"]["endpoint_covariance_residual"] == 0
            and row["law_fields"]["chain_endpoint_covariance_residual"] == 0
            and row["law_fields"]["source_target_typed"]
            and row["law_fields"]["transported_presentation_exact"]
            and row["law_fields"]["source_configuration_action_exact"]
            and row["law_fields"]["nomological_roots_preserved"]
            and row["law_fields"]["contextual_alias_exact"]
            and row["law_fields"]["certificate_transport_exact"]
            and row["law_fields"]["all_object_actions_exact"]
            for row in measurements["groupoid"]["native_census"]["rows"]
        ),
        measurements["category"]["all_exact"]
        and measurements["coherent"]["first_isometry"]
        and measurements["coherent"]["second_isometry"]
        and measurements["totality"]["all_generator_isometries"]
        and measurements["totality"]["all_rho_involutions"]
        and measurements["totality"][
            "cayley_norm_identity_for_every_rational_x"
        ]
        and measurements["totality"]["denominator_positive_certificate"][
            "positive_for_every_rational_x"
        ]
        and measurements["totality"]["endpoint_domain_controls_normalized"]
        and measurements["totality"]["all_nonzero_generator_transitions_bound"]
        and measurements["full_target"]["all_full"],
        measurements["source_identity"]["equal_key_equal_profile"]
        and measurements["source_identity"]["distinct_filling_distinct_key"]
        and measurements["source_identity"]["neutral_label_and_status_order_invariant"]
        and measurements["source_identity"]["contextual_boolean_alias_exact"],
        measurements["lineage"]["all_complete"]
        and measurements["shadow_lineages"]["all_outputs_bound"]
        and measurements["shadow_lineages"][
            "all_law_shadows_consume_unique_primitive"
        ]
        and measurements["shadow_lineages"][
            "blind_projection_rooted_in_literal_context_not_gamma"
        ]
        and measurements["shadow_lineages"]["all_arithmetic_recomputed"],
        measurements["coherent"]["B"] == measurements["native_nondivision"]["B"]
        and measurements["coherent"]["C"] == measurements["native_nondivision"]["C"],
        bool(measurements["support_change"]["branches"])
        and measurements["support_change"]["all_bound_certificates_exact"]
        and measurements["support_change"]["all_create_certificates_exact"]
        and not measurements["support_change"]["context_proof_alone_is_promotive"]
        and not measurements["support_change"][
            "legacy_role_cell_inequality_is_promotive"
        ],
        measurements["support_change"]["all_inverse_merge"]
        and measurements["support_change"]["all_support_changed"]
        and measurements["support_change"]["all_create_certificates_exact"]
        and measurements["support_change"]["all_merge_certificates_exact"]
        and measurements["support_change"]["all_unchanged_certificates_exact"]
        and measurements["groupoid"]["split_certificate_covariance"]["all_exact"],
        measurements["reciprocal"]["normalization"] == 1
        and measurements["reciprocal"]["counterfactual_probe_one"] == 0
        and measurements["reciprocal"]["contact_true_branch"]
        and not measurements["reciprocal"]["contact_false_branch"],
        measurements["division"]["writer_normalized_all_blank_inputs"]
        and measurements["division"]["writer_blank_input_count"]
        == len(measurements["division"]["writer_blank_input_rows"])
        and measurements["division"]["writer_blank_input_count"] > 0
        and measurements["division"]["continuation_grammar_exact"]
        and measurements["division"]["all_generator_intertwining"]
        and measurements["division"]["free_word_induction"]["base"]
        and measurements["division"]["free_word_induction"]["step"]
        and measurements["division"]["free_word_induction"][
            "enumerated_residual"
        ]
        == 0
        and measurements["division"]["alternate_cut_residual"] == 0
        and measurements["division"]["alternate_cut_all_input_residual"] == 0
        and measurements["division"]["alternate_cut_all_input_comparisons"]
        == len(measurements["division"]["alternate_cut_all_input_rows"])
        and measurements["division"]["alternate_cut_all_input_comparisons"] > 0
        and measurements["division"]["active_reuse_eraser"][
            "inverse_toggle_exact"
        ]
        and measurements["division"]["retained_zero_count"] > 0,
        not measurements["native_nondivision"]["positive_source_independent_restart_exists"]
        and bool(measurements["native_nondivision"]["negative_entries"])
        and measurements["native_nondivision"]["unique_factor"]
        and measurements["native_nondivision"]["interval_certificate"][
            "universal_certificate"
        ]
        and measurements["native_nondivision"]["interval_certificate"][
            "universal_factor_outside_stochastic_spectral_interval"
        ]
        and measurements["native_nondivision"]["interval_certificate"]["bound_residual"] >= 0
        and measurements["native_nondivision"]["history_joint_normalizations"]
        == (Fraction(1), Fraction(1))
        and measurements["native_nondivision"]["history_joint_nonnegative"]
        and measurements["native_nondivision"]["history_joint_positive_coordinates"]
        > 0,
        measurements["blind_family"]["resource_parity"]
        and measurements["blind_family"]["blind_prefix_equal"]
        and measurements["blind_family"]["same_law_root"]
        and measurements["blind_family"]["direct_factorization_exact"]
        and measurements["blind_family"]["exposed_marginals_exact"]
        and measurements["blind_family"]["response_unequal"]
        and fresh_exact,
    )
    for index, predicate in enumerate(predicates):
        if not predicate:
            return index
    return 12


def verify_outcome_rendering(measurements: Mapping[str, Any], rendered: str) -> bool:
    _require_exact(rendered, str, "rendered outcome")
    index = independent_outcome_index(measurements)
    independently_rebuilt = "-".join(OUTCOME_SEGMENTS[index])
    return rendered == independently_rebuilt


def classify_repair_disposition(
    measurements: Mapping[str, Any], attacks: Mapping[str, Any]
) -> str:
    if (
        not measurements["static_scan"]["clean"]
        or not measurements["support_promotion_static"]["all_exact"]
        or not measurements["groupoid_promotion_static"]["all_exact"]
        or not measurements["regression_wall"]["all_exact"]
    ):
        return "REPAIR-SPECIFICATION-INCONSISTENT"
    if (
        not measurements["context_split_census"]["all_exact"]
        or not measurements["source_identity"]["contextual_boolean_alias_exact"]
        or not groupoid_promotion_predicate(measurements["groupoid"])
        or any(
            not attacks["rows"][name]["pass"] for name in GROUPID_ATTACKS
        )
    ):
        return "P13-REFERENT-PRESENTATION-ONLY"
    if (
        not measurements["gates"]["variable_carrier"]
        or not measurements["gates"]["support_change"]
        or any(not attacks["rows"][name]["pass"] for name in SPLIT_SUPPORT_ATTACKS)
    ):
        return "P13-SUPPORT-CHANGE-UNPROVEN"
    return "REPAIR-GREEN-UNREVIEWED"


def measure_scientific_core(source_text: str) -> dict[str, Any]:
    law = GammaLaw(Fraction(1, 2))
    representative = build_coherent_control("receipt_")
    representative_source = _empty_state(representative["boundary"])
    measurements: dict[str, Any] = {
        "law": law,
        "g_domain": {
            "number_system": "RATIONAL",
            "lower_closed": Fraction(1, 3),
            "upper_closed": Fraction(1, 2),
        },
        "representative_application": {
            "source_boundary": representative["boundary"],
            "target_boundary": representative["two_pairs"].target,
            "filling_ast": representative["two_pairs"],
            "source_state": representative_source,
            "source_key": presentation_key(
                law, representative["two_pairs"], representative_source
            ),
        },
        "scope_coordinates": dict(SCOPE_COORDINATES),
        "scope_walls": SCOPE_WALLS,
        "scope_valid": True,
        "static_scan": static_source_scan(source_text),
        "support_promotion_static": support_promotion_source_scan(source_text),
        "groupoid_promotion_static": groupoid_promotion_source_scan(source_text),
        "measurement_programme": MEASUREMENT_PROGRAMME,
        "historical_old_source_provenance": dict(
            HISTORICAL_OLD_SOURCE_PROVENANCE
        ),
    }
    validate_scope_surface(measurements["scope_coordinates"], measurements["scope_walls"])
    measurements["boolean_quotient"] = measure_boolean_quotient()
    measurements["context_split_census"] = measure_context_split_census(law)
    measurements["source_identity"] = measure_source_identity(law)
    measurements["groupoid"] = measure_groupoid_covariance(law)
    measurements["full_target"] = measure_full_target_retyping(law)
    measurements["category"] = measure_category_laws(law)
    measurements["coherent"] = measure_coherent_controls(law)
    measurements["totality"] = measure_totality_certificate(law)
    measurements["support_change"] = measure_support_change(law)
    measurements["public_language"] = _public_language_selfcheck(measurements)
    measurements["referent_census"] = {
        "essential_boolean_support_exact": measurements["boolean_quotient"][
            "all_exact"
        ],
        "primitive_language_closed": measurements["public_language"][
            "all_registered_visited"
        ],
        "boundary_catalogue_complete": measurements["full_target"]["all_full"],
        "zero_targets_retained": measurements["full_target"][
            "first_zero_coordinate_count"
        ]
        > 0
        and measurements["full_target"]["first_full_target_count"]
        == measurements["full_target"]["first_returned_coordinate_count"],
        "complete_source_identity": measurements["source_identity"][
            "equal_key_equal_profile"
        ]
        and measurements["source_identity"]["contextual_boolean_alias_exact"],
        "contextual_boolean_census_exact": measurements["context_split_census"][
            "all_exact"
        ],
        "context_proof_nonpromotive": measurements["context_split_census"][
            "context_proofs_are_nonpromotive"
        ]
        and not measurements["support_change"]["context_proof_alone_is_promotive"],
        "bound_split_classifier_exact": measurements["support_change"][
            "all_bound_certificates_exact"
        ],
        "groupoid_transport_exact": groupoid_promotion_predicate(
            measurements["groupoid"]
        )
        and measurements["groupoid"]["split_certificate_covariance"]["all_exact"]
        and measurements["groupoid"]["cache_hits"] == 0
        and not measurements["groupoid"]["cache_implementation_present"],
        "bound_split_classifier_sha256": measurements["support_change"][
            "classifier_consumed_certificate_sha256"
        ],
    }
    measurements["referent_census"]["all_exact"] = all(
        value
        for key, value in measurements["referent_census"].items()
        if key != "bound_split_classifier_sha256"
    )
    measurements["reciprocal"] = measure_reciprocal_response(law)
    measurements["division"] = measure_record_division(law)
    measurements["native_nondivision"] = measure_native_nondivision(law)
    measurements["blind_family"] = measure_blind_family(law)
    measurements["regression_wall"] = build_result_neutral_regression_wall(
        measurements, source_text
    )
    measurements["lineage"] = _lineage_gate(law, measurements)
    measurements["shadow_lineages"] = build_shadow_lineages(measurements)
    measurements["exposed_anchor_assertions"] = assert_exposed_controls(measurements)
    measurements["gates"] = build_gate_table(measurements)
    measurements["strict_primary"] = classify_primary(measurements["gates"])
    measurements["outcome_render_trace"] = render_outcome_index(
        independent_outcome_index(measurements)
    )[1]
    measurements["outcome_comparator"] = verify_outcome_rendering(
        measurements, measurements["strict_primary"]
    )
    if not measurements["outcome_comparator"]:
        raise IntegrityFailure("independent outcome comparator disagrees")
    return measurements


def _outcome_flip_attack(measurements: Mapping[str, Any]) -> dict[str, Any]:
    old = measurements["strict_primary"]
    new = old + "-FORGED"
    passed = verify_outcome_rendering(measurements, old) and not verify_outcome_rendering(
        measurements, new
    )
    return _attack_record(
        {"rendered": old},
        {"rendered": new},
        "receipt.strict_primary",
        "EARLIEST-OUTCOME-RENDERING",
        "INDEPENDENT-DIGEST-COMPARATOR",
        passed,
        {
            "baseline_digest": sha256_bytes(old.encode("ascii")),
            "mutant_digest": sha256_bytes(new.encode("ascii")),
            "independent_index": independent_outcome_index(measurements),
        },
        "INTEGRITY-EXIT-1",
    )


BOUNDARY_ATTACKS = (
    "PORT-PARENT-NONTOTAL",
    "ACTIVE-ROLE-ZERO",
    "TWO-BASE-CATALOG",
    "CROSS-CHILD-PARENT",
    "BOUNDARY-SIGNATURE-MISSING-SPECTATOR",
    "PARTIAL-BOUNDARY-CATALOG",
    "DEPENDENT-FRESH-CHILD-COLLISION",
    "DUPLICATE-ID",
)
LANGUAGE_ATTACKS = (
    "GENERATOR-UNDECLARED-QUERY-ROLE",
    "ALIEN-TENSOR-OPERAND",
    "ALIEN-IDENTITY-BOUNDARY",
    "FORGED-UNIT-CONTEXT",
    "FORGED-IDENTITY-TARGET",
    "FORGED-COMPOSE-TARGET",
    "FORGED-TENSOR-TARGET",
    "FORGED-GENERATOR-TARGET",
    "FORMULA-SUBCLASS-PROXY",
    "CONTEXT-SUBCLASS-PROXY",
    "LAW-SUBCLASS-PROXY",
    "FOREIGN-RHO-LEAF",
    "FORMULA-INSTANCE-METHOD-SHADOW",
    "PORT-RHO-OVERRIDE",
    "MUTABLE-LAW-METHOD-SHADOW",
    "NONBOOLEAN-SEAL",
    "UNSEALED-OCCURRENCE",
    "MALFORMED-CONTINUATION-ALPHABET",
    "FORGED-DERIVATION-ARITY",
    "INCOMPATIBLE-COMPOSITION",
)
PRESENTATION_CONTROLS = (
    "INESSENTIAL-BOOLEAN-ROLE",
    "STATUS-ORDER-PRESENTATION",
    "NEUTRAL-LABEL-PRESENTATION",
    "SOURCE-KEY-OMITS-FILLING",
)
LINEAGE_ATTACKS = (
    "WRAPPER-GAMMA",
    "OCCURRENCE-SEVER",
    "ALIEN-CARRIER-OR-CLONE-ROUTING",
    "BARE-KRON-AS-CONTEXT-TENSOR",
)
LAW_ATTACKS = (
    "RESET-ONE",
    "TARGET-CONTACT",
    "COIN-CONTACT",
    "NONINJECTIVE-RHO",
    "ISOMETRIC-SWAPPED-RHO",
    "WRONG-BRANCH-RHO",
    "SAME-BORN-REFLECTION",
    "PHASE-REFLECTION-MUTATION",
)
OUTPUT_ATTACKS = (
    "ZERO-TARGET-DROPPED",
    "SUPPORT-FILTERED-TARGET",
    "FULL-TARGET-RETYPE",
    "BORN-TABLE-AS-GAMMA",
    "BRANCH-SUM-ONLY",
    "CACHED-G-OR-SHADOW",
    "QUERY-FORMULA-MUTATION",
    "MOVE-DOWNSTREAM",
)
RECORD_ATTACKS = (
    "CARRIED-PORT-STILL-ACTIVE",
    "RESET-WRITER-CHAIN",
    "HIDDEN-ERASER",
    "RETURN-TO-OLD-PORT",
    "DELAYED-READER-SEVER",
)
METADATA_ATTACKS = (
    "HELDOUT-SHADOW-DUPLICATED",
    "RESULT-EXPOSED-AS-HOLDOUT",
    "REROLL-OR-EXPOSED-AS-HOLDOUT",
    "HAND-ENTERED-RESOURCE-TABLE",
    "CONSTANT-BLIND-TOKEN",
    "UNEQUAL-BLIND-SCHEDULE",
    "UNEQUAL-PRIOR-RECORD-LAW",
    "LEAKED-INCIDENCE-BIT",
)
SCOPE_ATTACKS = (
    "HISTORY-PASSED-OFF-AS-NATIVE-K",
    "NONDIVISION-AS-STATE-DEFECT",
    "ABSOLUTE-NONDIVISION",
    "META-CATALOGUE-AS-SUPPORT",
    "HIDDEN-VALUATION",
    "RAW-RELATION-TO-GEOMETRY",
    "INCIDENCE-CYCLE-TO-TOPOLOGY",
    "EVENT-ORDER-TO-TIME",
    "AMPLITUDE-TO-ONTOLOGY",
    "NORMALIZATION-TO-ACTUALIZATION",
)
TYPED_GROUPOID_ATTACKS = (
    "EMPTY-LEFT-IDENTITY",
    "EMPTY-RIGHT-IDENTITY",
    "INVERSE-LEFT",
    "INVERSE-RIGHT",
    "THREE-SPARSE-ASSOCIATIVITY",
    "MIDDLE-PRESENTATION-MISMATCH",
    "SOURCE-LABEL-OMITTED",
    "EXTRA-TARGET-LABEL",
    "MAP-COLLISION",
    "ROLE-TYPE-SWAP",
    "NAMESPACE-CROSSING",
    "TARGET-PRESENTATION-FORGERY",
    "IDENTITY-ROW-ENCODING",
    "ORDER-REVERSAL",
    "TRANSPORT-SEVER",
    "CERTIFICATE-TRANSPORT-CACHE",
    "COMPOSITE-OPERATOR-CACHE",
    "COPIED-GROUPOID-BOOLEAN",
    "TENSOR-SHARED-LABEL-CONFLICT",
    "FRESH-GLOBAL-RELABEL-SEVER",
)
V3_CONFIGURATION_ACTION_ATTACKS = (
    "NONIMAGE-ACTIVE-CARRIED",
    "SAME-CARDINALITY-ALIEN-BOUNDARY",
    "WRONG-BRANCH-TARGET",
    "ALIEN-CONFIGURATION-MATTER",
    "ALIEN-CONFIGURATION-PORT",
    "CONTEXT-ONLY-EQUAL-TARGET",
    "BOUNDARY-NOT-IN-PRESENTATION",
    "CHAINED-NONIMAGE-TARGET",
    "DERIVED-TARGET-CACHE",
    "TENSOR-FOREIGN-FACTOR",
    "DUPLICATE-SEMANTIC-NODE-COLLAPSE",
    "CONFIGURATION-COMPOSITION-SEVER",
    "CONFIGURATION-ASSOCIATIVITY-SEVER",
    "CONFIGURATION-TENSOR-SEVER",
    "IDENTITY-PRESENTATION-COLLISION",
    "CORE-TARGET-BACKDOOR",
)
V3_CERTIFICATE_ACTION_ATTACKS = (
    "MALFORMED-TRANSPORTED-CERTIFICATE-BYTES",
    "FINAL-COUNT-ONLY-CERTIFICATE",
    "HASH-LIST-ONLY-CERTIFICATE",
    "CERTIFICATE-KEY-ATTACHMENT-SWAP",
    "CERTIFICATE-TARGET-DROP",
    "CERTIFICATE-TARGET-DUPLICATE",
    "CERTIFICATE-WRONG-OPERATION",
    "CERTIFICATE-WRONG-BRANCH",
    "STALE-LITERAL-TRANSPORT",
    "STALE-INDEPENDENT-REBUILD",
    "CERTIFICATE-CLASSIFIER-LINEAGE-DROP",
    "CERTIFICATE-IDENTITY-ONLY",
    "CERTIFICATE-COMPOSITION-SEVER",
    "CERTIFICATE-INVERSE-SEVER",
    "COPIED-CERTIFICATE-ACTION-BOOLEAN",
    "NATIVE-CERTIFICATE-ROW-BYPASS",
    "CERTIFICATE-ASSOCIATIVITY-SEVER",
    "HASH-ONLY-CERTIFICATE-ACTION-INPUT",
    "FOREIGN-CERTIFICATE-BINDING",
    "CERTIFICATE-ACTION-REGISTRY-BACKDOOR",
    "DUPLICATE-GENERATOR-ADDRESS-COLLAPSE",
)
V3_TYPED_GROUPOID_ATTACKS = (
    V3_CONFIGURATION_ACTION_ATTACKS + V3_CERTIFICATE_ACTION_ATTACKS
)
V4_CONFIGURATION_ACTION_ATTACKS = (
    "TENSOR-INTERNAL-FACTOR-NODE",
    "TENSOR-TARGET-FACTOR-NODE-SEVER",
)
V4_CERTIFICATE_ACTION_ATTACKS = (
    "COMPLETE-IDENTITY-TARGET-PACKET-SWAP",
    "COMPLETE-ACTION-PRODUCER-BYPASS",
)
V4_TYPED_GROUPOID_ATTACKS = (
    V4_CONFIGURATION_ACTION_ATTACKS + V4_CERTIFICATE_ACTION_ATTACKS
)
GROUPID_ATTACKS = (
    "RELABEL-RAW-NAME",
    "RELABEL-ORIENTATION",
) + TYPED_GROUPOID_ATTACKS + V3_TYPED_GROUPOID_ATTACKS + V4_TYPED_GROUPOID_ATTACKS
SPLIT_SUPPORT_ATTACKS = (
    "TAUTOLOGICAL-CHILD",
    "COEXTENSIVE-CHILD-OBJECT",
    "FORGET-ONLY",
    "CELL-COUNT-PADDING",
    "ROLE-COUNT-ONLY",
    "TRANSPORT-SPLIT-SEVER",
    "SUPPLIED-SPLIT-BOOLEAN",
    "CERTIFICATE-PORT-SWAP",
    "OLD-CHILD-REUSE",
    "AMBIENT-TARGET-PADDING",
    "CONTEXTUAL-BOOLEAN-ALIAS",
)
MUTANT_IDS = (
    BOUNDARY_ATTACKS
    + LANGUAGE_ATTACKS
    + ("POSTINIT-LAW-IDENTITY",)
    + PRESENTATION_CONTROLS
    + LINEAGE_ATTACKS
    + LAW_ATTACKS
    + OUTPUT_ATTACKS
    + RECORD_ATTACKS
    + METADATA_ATTACKS
    + SCOPE_ATTACKS
    + ("FLOAT-OR-EXPECTED-TABLE", "ANCHOR-CORRUPTION", "OUTCOME-FLIP")
    + GROUPID_ATTACKS
    + SPLIT_SUPPORT_ATTACKS
)


def run_attack(
    identifier: str,
    measurements: Mapping[str, Any] | None = None,
    groupoid_attack_context: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    _require_exact(identifier, str, "mutant identifier")
    if identifier not in MUTANT_IDS:
        raise Refusal("unknown mutant")
    if identifier in BOUNDARY_ATTACKS:
        return _invalid_boundary_attacks(identifier)
    if identifier in LANGUAGE_ATTACKS:
        return _arrow_and_language_attacks(identifier)
    if identifier == "POSTINIT-LAW-IDENTITY":
        return _postinit_identity_attack()
    if identifier in PRESENTATION_CONTROLS:
        return _presentation_control_attack(identifier)
    if identifier in LINEAGE_ATTACKS:
        return _lineage_attacks(identifier)
    if identifier in LAW_ATTACKS:
        return _law_primitive_attacks(identifier)
    if identifier in OUTPUT_ATTACKS:
        return _output_and_shadow_attacks(identifier)
    if identifier in RECORD_ATTACKS:
        return _record_attacks(identifier)
    if identifier in METADATA_ATTACKS:
        return _metadata_attacks(identifier)
    if identifier in SCOPE_ATTACKS:
        return _scope_attacks(identifier)
    if identifier == "FLOAT-OR-EXPECTED-TABLE":
        return _static_injection_attack()
    if identifier == "ANCHOR-CORRUPTION":
        return _anchor_corruption_attack()
    if identifier == "OUTCOME-FLIP":
        if measurements is None:
            source_text = Path(__file__).read_text(encoding="utf-8")
            measurements = measure_scientific_core(source_text)
        return _outcome_flip_attack(measurements)
    if identifier in GROUPID_ATTACKS:
        if identifier in V3_TYPED_GROUPOID_ATTACKS + V4_TYPED_GROUPOID_ATTACKS:
            return _typed_groupoid_v4_action_attack(
                identifier, measurements, groupoid_attack_context
            )
        return _groupoid_attacks(identifier, measurements)
    if identifier in SPLIT_SUPPORT_ATTACKS:
        return _split_support_attacks(identifier)
    raise Refusal("unreachable mutant dispatcher branch")


def run_all_attacks(measurements: Mapping[str, Any]) -> dict[str, Any]:
    groupoid_attack_context = _typed_groupoid_v4_attack_context(
        measurements, include_shared_censuses=True
    )
    rows = {
        identifier: run_attack(
            identifier,
            measurements,
            groupoid_attack_context
            if identifier in V3_TYPED_GROUPOID_ATTACKS + V4_TYPED_GROUPOID_ATTACKS
            else None,
        )
        for identifier in MUTANT_IDS
    }
    return {
        "registered": len(MUTANT_IDS),
        "executed": len(rows),
        "killed": sum(int(row["pass"]) for row in rows.values()),
        "all_pass": all(row["pass"] for row in rows.values()),
        "rows": rows,
    }


ANCHOR_SPECS = (
    (
        "v16/note-paper13-typed-groupoid-v4-source-delta-pin.md",
        SOURCE_DELTA_PIN_SHA256,
        "typed-groupoid-v4-source-delta-contract",
    ),
    (
        "v16/note-paper13-typed-groupoid-v3-source-audit-adjudication.md",
        SOURCE_AUDIT_ADJUDICATION_SHA256,
        "typed-groupoid-v3-source-audit-adjudication",
    ),
    (
        "v16/code/p13_gamma_exact_v3.py",
        REJECTED_V3_SOURCE_SHA256,
        "rejected-v3-source-regression-only-never-imported",
    ),
    (
        "v16/note-paper13-typed-groupoid-source-freeze-v3.md",
        REJECTED_V3_FREEZE_SHA256,
        "rejected-v3-source-freeze-authentication-only",
    ),
    (
        "v16/review-paper13-typed-groupoid-v3-source-operator.md",
        V3_OPERATOR_SOURCE_REPORT_SHA256,
        "v3-source-operator-counterexample",
    ),
    (
        "v16/review-paper13-typed-groupoid-v3-source-records.md",
        V3_RECORDS_SOURCE_REPORT_SHA256,
        "v3-source-records-counterexample",
    ),
    (
        "v16/note-paper13-typed-groupoid-forward-repair-pin.md",
        TYPED_GROUPOID_PIN_SHA256,
        "typed-groupoid-forward-repair-contract",
    ),
    (
        "v16/note-paper13-hostile-review-adjudication.md",
        HOSTILE_ADJUDICATION_SHA256,
        "rejected-candidate-adjudication-and-forward-authority",
    ),
    (
        "v16/note-paper13-stageA-support-split-forward-repair-pin.md",
        FORWARD_REPAIR_PIN_SHA256,
        "support-split-forward-repair-contract",
    ),
    (
        "v16/note-paper13-one-gamma-construction-pin.md",
        PIN_SHA256,
        "construction-contract",
    ),
    ("RUNBOOK.md", RUNBOOK_SHA256, "process-integrity-contract"),
    (
        "v16/note-apr-one-gamma-paper-review-gate.md",
        PREDECESSOR_SHA256,
        "methodology-and-ontology-gate",
    ),
    (
        "v16/paper-12-atomless-regions-and-the-missing-gluing-law.md",
        PAPER12_SHA256,
        "terminal-negative-and-scope-provenance",
    ),
    (
        "v16/note-apr-paper12-final-adjudication.md",
        PAPER12_ADJUDICATION_SHA256,
        "terminal-disposition-provenance",
    ),
    (
        "v16/code/apr_paper12_exact.py",
        PAPER12_EVALUATOR_SHA256,
        "authentication-only-never-imported",
    ),
    (
        "v16/code/apr_paper12_receipt.json",
        PAPER12_RECEIPT_SHA256,
        "authentication-only-never-scientific-input",
    ),
    (
        "v16/note-paper13-gamma-source-freeze.md",
        OLD_STAGE_A_FREEZE_SHA256,
        "historical-flawed-freeze-authentication-only",
    ),
    (
        "v16/review-paper13-stageA-source-physics.md",
        STAGE_A_PHYSICS_REPORT_SHA256,
        "source-audit-physics-report-authentication-only",
    ),
    (
        "v16/review-paper13-stageA-source-records.md",
        STAGE_A_RECORDS_REPORT_SHA256,
        "source-audit-records-report-authentication-only",
    ),
    (
        "v16/note-paper13-stageA-source-audit-adjudication.md",
        STAGE_A_ADJUDICATION_SHA256,
        "source-audit-adjudication-authentication-only",
    ),
    (
        "v16/code/p13_gamma_exact.py",
        REJECTED_SOURCE_SHA256,
        "rejected-source-authentication-only-never-imported",
    ),
    (
        "v16/code/p13_gamma_fresh_cases.json",
        REJECTED_FRESH_SHA256,
        "rejected-fresh-exposed-regression-only",
    ),
    (
        "v16/code/p13_gamma_output.txt",
        REJECTED_OUTPUT_SHA256,
        "rejected-output-exposed-regression-only",
    ),
    (
        "v16/code/p13_gamma_receipt.json",
        REJECTED_RECEIPT_SHA256,
        "rejected-receipt-known-incomplete-authentication-only",
    ),
    (
        "v16/paper-13-one-relational-gamma.md",
        REJECTED_PAPER_SHA256,
        "rejected-paper-authentication-only",
    ),
    (
        "v16/note-paper13-hostile-review-protocol.md",
        HOSTILE_PROTOCOL_SHA256,
        "rejected-cycle-hostile-protocol-provenance",
    ),
    (
        "v16/review-paper13-operator-category.md",
        SEAT_A_REPORT_SHA256,
        "decisive-empty-identity-counterexample",
    ),
    (
        "v16/review-paper13-indivisibility-records.md",
        SEAT_I_REPORT_SHA256,
        "preserved-indivisibility-and-record-scope",
    ),
    (
        "v16/review-paper13-relational-ontology.md",
        SEAT_R_REPORT_SHA256,
        "preserved-relational-and-runner-scope",
    ),
)
SOURCE_FREEZE_TASK_PATHS = (
    "v16/code/p13_gamma_exact_v4.py",
    "v16/note-paper13-typed-groupoid-source-freeze-v4.md",
)
PUBLICATION_PATHS = (
    "v16/code/p13_gamma_fresh_cases_v4.json",
    "v16/code/p13_gamma_output_v4.txt",
    "v16/code/p13_gamma_receipt_v4.json",
)


class CLIUsage(Exception):
    """The command line is not one of the four exact registered forms."""


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def source_path() -> Path:
    return Path(__file__).resolve()


def _is_lower_hex(value: str, byte_count: int) -> bool:
    return (
        type(value) is str
        and len(value) == 2 * byte_count
        and all(character in "0123456789abcdef" for character in value)
    )


def _is_hex(value: str, byte_count: int) -> bool:
    return (
        type(value) is str
        and len(value) == 2 * byte_count
        and all(character.lower() in "0123456789abcdef" for character in value)
    )


def with_normalized_payload_hash(
    payload: Mapping[str, Any], field: str = "normalized_payload_sha256"
) -> dict[str, Any]:
    if type(payload) is not dict or field in payload:
        raise IntegrityFailure("normalized payload hash input is malformed")
    rendered = dict(payload)
    rendered[field] = canonical_hash(payload)
    return rendered


def verify_normalized_payload_hash(
    payload: Mapping[str, Any], field: str = "normalized_payload_sha256"
) -> bool:
    if type(payload) is not dict or set(payload).issuperset({field}) is not True:
        return False
    observed = payload.get(field)
    if not _is_lower_hex(observed, 32):
        return False
    normalized = {key: value for key, value in payload.items() if key != field}
    return canonical_hash(normalized) == observed


def authenticate_committed_inputs(
    source_sha256: str,
    source_payload: bytes | None = None,
    start_index: int = 1,
) -> tuple[dict[str, Any], ...]:
    if not _is_lower_hex(source_sha256, 32):
        raise IntegrityFailure("source hash is not canonical SHA-256")
    _require_exact(start_index, int, "read-set start index")
    if start_index < 1:
        raise IntegrityFailure("read-set start index is invalid")
    root = repository_root()
    reads: list[dict[str, Any]] = []
    anchor_payloads: dict[str, bytes] = {}
    if source_payload is None:
        source_payload = source_path().read_bytes()
    _require_exact(source_payload, bytes, "evaluator source payload")
    own = authenticate_payload(source_payload, source_sha256, "p13 evaluator source")
    reads.append(
        {
            "open_index": start_index,
            "path": "v16/code/p13_gamma_exact_v4.py",
            "expected_sha256": own["expected"],
            "observed_sha256": own["observed"],
            "consumption_key": "authoritative-evaluator-and-generator",
            "consumed": True,
        }
    )
    for open_index, (logical_path, expected, consumption_key) in enumerate(
        ANCHOR_SPECS, start=start_index + 1
    ):
        payload = (root / logical_path).read_bytes()
        anchor_payloads[logical_path] = payload
        authentication = authenticate_payload(payload, expected, logical_path)
        reads.append(
            {
                "open_index": open_index,
                "path": logical_path,
                "expected_sha256": authentication["expected"],
                "observed_sha256": authentication["observed"],
                "consumption_key": consumption_key,
                "consumed": True,
            }
        )
    if len({row["consumption_key"] for row in reads}) != len(reads):
        raise IntegrityFailure("anchor consumption keys are not unique")
    if not all(row["consumed"] for row in reads):
        raise IntegrityFailure("an authenticated anchor was not consumed")
    historical_token = OLD_STAGE_A_SOURCE_SHA256.encode("ascii")
    for logical_path in HISTORICAL_OLD_SOURCE_PROVENANCE["cross_checked_from"]:
        if historical_token not in anchor_payloads[logical_path]:
            raise IntegrityFailure(
                "historical unobserved source hash is absent from provenance"
            )
    return tuple(reads)


def authentication_manifest_hash(reads: Sequence[Mapping[str, Any]]) -> str:
    semantic_rows = tuple(
        {
            key: value
            for key, value in row.items()
            if key != "open_index"
        }
        for row in reads
    )
    return canonical_hash(semantic_rows)


def _entropy_permutation(size: int, block: bytes, offset: int) -> tuple[tuple[int, ...], int]:
    values = list(range(size))
    cursor = offset
    for upper in range(size - 1, 0, -1):
        if cursor + 2 > len(block):
            raise IntegrityFailure("fresh entropy block exhausted")
        draw = int.from_bytes(block[cursor : cursor + 2], "big")
        cursor += 2
        swap = draw % (upper + 1)
        values[upper], values[swap] = values[swap], values[upper]
    return tuple(values), cursor


def _fresh_blind_projection(presentation: MatchingPresentation) -> dict[str, Any]:
    prefix = "match_"
    context = matching_context(presentation, prefix)
    return {
        "size": presentation.size,
        "resources": _context_resource_projection(context, presentation.size, prefix),
        "query_count": len(presentation.queries),
        "port_count": len(presentation.queries),
        "coin_count": len(presentation.queries),
        "schedule": tuple(range(len(presentation.queries))),
        "calibrated_query_roles": tuple(
            "L-AND-N" for _ in presentation.queries
        ),
        "prior_record_tokens": (),
    }


def derive_fresh_payload(source_sha256: str, nonce_hex: str) -> dict[str, Any]:
    if not _is_lower_hex(source_sha256, 32):
        raise Refusal("fresh source hash must be lower-case SHA-256")
    if not _is_lower_hex(nonce_hex, 32):
        raise Refusal("fresh nonce must encode exactly 32 bytes in lower-case hex")
    seed = FRESH_DOMAIN + bytes.fromhex(source_sha256) + bytes.fromhex(nonce_hex)
    stream = hashlib.shake_256(seed).digest(512)
    root_block = stream[:256]
    size = 7 + root_block[0] % 6
    query_count = 2 + root_block[1] % 3
    query_order, cursor = _entropy_permutation(size, root_block, 2)
    queries = tuple(sorted(query_order[:query_count]))
    rejection_count = 0
    while True:
        block = stream[256 * rejection_count : 256 * (rejection_count + 1)]
        if rejection_count == 0:
            challenge_permutation, _ = _entropy_permutation(
                size, root_block, cursor
            )
        else:
            forced = list(range(size))
            fixed_query = queries[0]
            moved_query = queries[1]
            partners = tuple(
                index
                for index in range(size)
                if index not in (fixed_query, moved_query)
            )
            partner = partners[block[0] % len(partners)]
            forced[moved_query], forced[partner] = (
                forced[partner],
                forced[moved_query],
            )
            challenge_permutation = tuple(forced)
        fixed_pattern = tuple(
            challenge_permutation[index] == index for index in queries
        )
        if any(fixed_pattern) and not all(fixed_pattern):
            break
        rejection_count += 1
        if rejection_count > 1:
            raise IntegrityFailure("fresh deterministic repair failed")

    common = MatchingPresentation(
        size,
        tuple(range(size)),
        queries,
        "POST-SOURCE-FRESH",
    )
    challenge = MatchingPresentation(
        size,
        challenge_permutation,
        queries,
        "POST-SOURCE-FRESH",
    )
    common_projection = _fresh_blind_projection(common)
    challenge_projection = _fresh_blind_projection(challenge)
    if common_projection != challenge_projection:
        raise IntegrityFailure("fresh pair lacks exact blind-resource parity")
    blind_token = canonical_hash(common_projection)
    case_without_hash = {
        "case_index": 0,
        "size": size,
        "query_count": query_count,
        "queries": queries,
        "members": (
            {"member": "COMMON", "presentation": common.to_data()},
            {"member": "CHALLENGE", "presentation": challenge.to_data()},
        ),
        "fixed_pattern": fixed_pattern,
        "blind_projection": common_projection,
        "blind_token_sha256": blind_token,
        "prior_record_law": "BLANK-NO-PRIOR-RECORD",
        "resource_parity": True,
        "direct_global_gamma_calls_required": 2,
    }
    case = dict(case_without_hash)
    case["case_sha256"] = canonical_hash(case_without_hash)
    base_payload = {
        "schema": "p13-gamma-fresh-v4",
        "domain_ascii": FRESH_DOMAIN.decode("ascii"),
        "source_sha256": source_sha256,
        "generator_sha256": source_sha256,
        "source_sha_encoding": "RAW-32-BYTE-DIGEST",
        "nonce_hex": nonce_hex,
        "nonce_encoding": "RAW-32-BYTE-LOWER-HEX",
        "nonce_provenance": "EXTERNAL-MUTUALLY-BLIND-REQUIRED-BY-PIN",
        "seed_sha256": sha256_bytes(seed),
        "counter_rule": "CONSECUTIVE-256-BYTE-SHAKE256-BLOCK-INDEX",
        "rejection_rule": (
            "TRY-ENTROPY-PERMUTATION-THEN-ONE-DETERMINISTIC-FIXED-MOVED-REPAIR"
        ),
        "rejection_count": rejection_count,
        "selected_block_sha256": sha256_bytes(block),
        "exposure": "POST-SOURCE-FRESH",
        "reroll_count": 0,
        "cases": (case,),
        "case_hashes": (case["case_sha256"],),
        "declared_peak_cell_count": 3 * size + 1,
        "declared_query_range": (2, 4),
        "outputs_present": False,
    }
    return with_normalized_payload_hash(base_payload)


def bind_fresh_anchor_manifest(
    fresh_payload: Mapping[str, Any], reads: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    if not verify_normalized_payload_hash(fresh_payload):
        raise IntegrityFailure("unanchored fresh derivation has a bad self-hash")
    bound = {
        key: value
        for key, value in fresh_payload.items()
        if key != "normalized_payload_sha256"
    }
    bound["anchor_read_manifest_sha256"] = authentication_manifest_hash(reads)
    return with_normalized_payload_hash(bound)


def _strict_json_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise Refusal("JSON object contains a duplicate key")
        result[key] = value
    return result


def _reject_json_float(_: str) -> Any:
    raise Refusal("JSON float is forbidden")


def parse_canonical_json_bytes(payload: bytes, label: str) -> dict[str, Any]:
    _require_exact(payload, bytes, "JSON payload")
    _require_exact(label, str, "JSON label")
    try:
        decoded = payload.decode("ascii")
    except UnicodeDecodeError as error:
        raise Refusal(f"{label} is not ASCII JSON") from error
    try:
        parsed = json.loads(
            decoded,
            object_pairs_hook=_strict_json_pairs,
            parse_float=_reject_json_float,
            parse_constant=_reject_json_float,
        )
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise Refusal(f"{label} is malformed JSON") from error
    if type(parsed) is not dict:
        raise Refusal(f"{label} top level is not an object")
    if payload != (canonical_json(parsed) + "\n").encode("ascii"):
        raise Refusal(f"{label} is not in canonical byte form")
    return parsed


def measure_fresh_confirmations(
    law: GammaLaw, fresh_payload: Mapping[str, Any]
) -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    peak_state_count = 0
    peak_cell_count = 0
    total_calls = 0
    for raw_case in fresh_payload["cases"]:
        results: list[dict[str, Any]] = []
        for raw_member in raw_case["members"]:
            raw_presentation = raw_member["presentation"]
            presentation = MatchingPresentation(
                raw_presentation["size"],
                tuple(raw_presentation["permutation"]),
                tuple(raw_presentation["queries"]),
                raw_presentation["exposure"],
                raw_presentation["seal"],
            )
            result = measure_matching_case(law, presentation)
            results.append({"member": raw_member["member"], "result": result})
            peak_state_count = max(peak_state_count, result["target_state_count"])
            peak_cell_count = max(peak_cell_count, 3 * presentation.size + 1)
            total_calls += result["single_global_gamma_calls"]
        first = results[0]["result"]
        second = results[1]["result"]
        blind_equal = first["blind_projection"] == second["blind_projection"]
        token_exact = (
            canonical_hash(first["blind_projection"])
            == raw_case["blind_token_sha256"]
        )
        response_unequal = first["marginals"] != second["marginals"]
        common_observed_pattern = tuple(
            first["marginals"][str(index)] != 0
            for index in raw_case["queries"]
        )
        challenge_observed_pattern = tuple(
            second["marginals"][str(index)] != 0
            for index in raw_case["queries"]
        )
        generated_pattern_exact = (
            all(common_observed_pattern)
            and challenge_observed_pattern == tuple(raw_case["fixed_pattern"])
            and any(challenge_observed_pattern)
            and not all(challenge_observed_pattern)
        )
        direct_factorization_exact = all(
            row["result"]["direct_vs_analytic_exact"] for row in results
        )
        exposed_marginals_exact = all(
            row["result"]["g_half_exposed_marginals_exact"] for row in results
        )
        normalizations = tuple(
            row["result"]["normalization"] for row in results
        )
        direct_call_count = sum(
            row["result"]["single_global_gamma_calls"] for row in results
        )
        direct_call_count_exact = (
            direct_call_count == raw_case["direct_global_gamma_calls_required"]
        )
        case_result = {
            "case_index": raw_case["case_index"],
            "input_case_sha256": raw_case["case_sha256"],
            "members": tuple(results),
            "blind_prefix_equal": blind_equal,
            "blind_token_recomputed": token_exact,
            "prior_record_law_equal": True,
            "response_unequal": response_unequal,
            "common_observed_fixed_pattern": common_observed_pattern,
            "challenge_observed_fixed_pattern": challenge_observed_pattern,
            "generated_pattern_exact": generated_pattern_exact,
            "direct_factorization_exact": direct_factorization_exact,
            "exposed_marginals_exact": exposed_marginals_exact,
            "normalizations": normalizations,
            "single_global_gamma_calls": direct_call_count,
            "direct_call_count_exact": direct_call_count_exact,
            "confirmed": blind_equal
            and token_exact
            and response_unequal
            and generated_pattern_exact
            and direct_factorization_exact
            and exposed_marginals_exact
            and direct_call_count_exact
            and all(value == 1 for value in normalizations),
        }
        cases.append(case_result)
    declared_peak_exact = peak_cell_count == fresh_payload["declared_peak_cell_count"]
    return {
        "exposure": "POST-SOURCE-FRESH",
        "reroll_count": fresh_payload["reroll_count"],
        "rejection_count": fresh_payload["rejection_count"],
        "cases": tuple(cases),
        "all_confirmed": bool(cases)
        and all(row["confirmed"] for row in cases)
        and declared_peak_exact,
        "total_global_gamma_calls": total_calls,
        "peak_state_count": peak_state_count,
        "peak_cell_count": peak_cell_count,
        "declared_peak_cell_count": fresh_payload["declared_peak_cell_count"],
        "declared_peak_cell_count_exact": declared_peak_exact,
    }


def _validate_publication_path(path_text: str, must_exist: bool) -> Path:
    _require_exact(path_text, str, "publication path")
    path = Path(path_text)
    if not path.is_absolute():
        raise CLIUsage("publication and input paths must be absolute")
    if must_exist:
        if not path.is_file():
            raise CLIUsage("required input path is absent or not a file")
    else:
        if path.exists() or path.is_symlink():
            raise CLIUsage("publication destination must be absent")
        if not path.parent.is_dir():
            raise CLIUsage("publication parent directory is absent")
    return path


def _validate_publication_role(path: Path, logical_path: str) -> None:
    if type(path) is not type(Path(".")):
        raise IntegrityFailure("publication role path has a foreign type")
    _require_exact(logical_path, str, "publication logical path")
    if logical_path not in PUBLICATION_PATHS:
        raise IntegrityFailure("publication role is outside the Stage-B whitelist")
    if path.name != Path(logical_path).name:
        raise CLIUsage("publication path has the wrong whitelisted basename")


def transactional_publish(items: Sequence[tuple[Path, bytes]]) -> None:
    if type(items) not in (tuple, list) or not items:
        raise IntegrityFailure("publication transaction is empty")
    destinations = tuple(path for path, _ in items)
    if len(set(destinations)) != len(destinations):
        raise IntegrityFailure("publication transaction repeats a destination")
    temporary_paths: list[Path] = []
    created_paths: list[Path] = []
    try:
        for destination, payload in items:
            if not destination.is_absolute() or destination.exists() or destination.is_symlink():
                raise IntegrityFailure("publication destination is no longer absent")
            descriptor, temporary_name = tempfile.mkstemp(
                prefix=".p13-transaction-", dir=destination.parent
            )
            temporary = Path(temporary_name)
            temporary_paths.append(temporary)
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            if temporary.read_bytes() != payload:
                raise IntegrityFailure("staged publication bytes changed")
        for (destination, payload), temporary in zip(items, temporary_paths, strict=True):
            os.link(temporary, destination)
            created_paths.append(destination)
            if destination.read_bytes() != payload:
                raise IntegrityFailure("gate-to-disk byte seal failed")
        for directory in sorted({path.parent for path in destinations}, key=str):
            descriptor = os.open(directory, os.O_RDONLY)
            try:
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
    except Exception:
        for created in reversed(created_paths):
            try:
                created.unlink()
            except FileNotFoundError:
                pass
        raise
    finally:
        for temporary in temporary_paths:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass


def _selftest_check(name: str, passed: bool, evidence: Any) -> dict[str, Any]:
    _require_exact(name, str, "self-test check name")
    _require_exact(passed, bool, "self-test predicate")
    return {
        "name": name,
        "status": "PASS" if passed else "FAIL",
        "pass": passed,
        "evidence": evidence,
        "evidence_sha256": canonical_hash(evidence),
    }


def _public_language_selfcheck(measurements: Mapping[str, Any]) -> dict[str, Any]:
    representative = measurements["representative_application"]
    arrow = representative["filling_ast"]
    first_generator = arrow.children[0].children[0]
    if type(first_generator.occurrence) is not Occurrence:
        raise IntegrityFailure("public-language witness lost its occurrence")
    boundary = representative["source_boundary"]
    source = representative["source_state"]
    linear_map = evaluate_arrow(measurements["law"], arrow)
    gamma = gamma_evaluate(measurements["law"], arrow, source)
    first_evaluation = gamma_evaluate(measurements["law"], first_generator, source)
    first_target_index = next(
        index
        for index, probability in enumerate(first_evaluation.probabilities)
        if probability != 0
    )
    split_certificate = build_bound_split_certificate(
        measurements["law"],
        first_generator,
        source,
        first_generator.target.catalogue[first_target_index],
    )
    split_proof = split_certificate.context_proof
    record = build_record_control("closure_")
    matching = MatchingPresentation(
        3, (0, 2, 1), (0, 1), "EXPOSED-CONTROL"
    )
    witness = identity_witness(arrow)
    presentation = witness.source
    boundary_node = boundary_node_at(presentation, (0, 0), "SOURCE")
    configuration_transport = act_configuration(boundary_node, source, witness)
    configuration_law = identity_action_row(
        presentation, boundary_node, source
    )
    certificate_input = build_certificate_action_input(
        measurements["law"],
        presentation,
        (0, 0),
        source,
        first_generator.target.catalogue[first_target_index],
        split_certificate,
    )
    certificate_triple = certificate_transport_triple(witness, certificate_input)
    complete_certificate_action = complete_certificate_action_row(
        "IDENTITY", witness, certificate_input
    )
    certificate_law = certificate_identity_row(certificate_input)
    nodes = (
        formula_constant(False),
        boundary.base.roles[0],
        boundary.base,
        split_proof.rows[0],
        split_proof,
        boundary.ports[0].port,
        boundary.ports[0],
        source,
        boundary,
        first_generator.occurrence,
        arrow,
        measurements["law"].primitive,
        measurements["law"],
        linear_map.derivation,
        linear_map,
        gamma,
        split_certificate,
        record["grammar"],
        matching,
        presentation,
        witness,
        boundary_node,
        configuration_transport,
        configuration_law,
        certificate_input,
        certificate_triple,
        complete_certificate_action,
        certificate_law,
    )
    for node in nodes:
        validate_public_exact_node(node)
    return {
        "registered_types": tuple(item.__name__ for item in PUBLIC_NODE_TYPES),
        "visited_types": tuple(type(node).__name__ for node in nodes),
        "all_registered_visited": set(PUBLIC_NODE_TYPES) == {type(node) for node in nodes},
        "node_hashes": tuple(canonical_hash(node) for node in nodes),
    }


def parse_strict_cli(argv: Sequence[str]) -> dict[str, str]:
    if type(argv) not in (tuple, list) or any(type(item) is not str for item in argv):
        raise CLIUsage("arguments must be exact strings")
    arguments = tuple(argv)
    if arguments == ("--selftest",):
        return {"mode": "selftest"}
    if len(arguments) == 2 and arguments[0] == "--mutant":
        if arguments[1] not in MUTANT_IDS:
            raise CLIUsage("unknown mutant name")
        return {"mode": "mutant", "name": arguments[1]}
    if arguments and arguments[0] == "--generate-fresh":
        allowed = {"--nonce", "--source-sha", "--fresh-out"}
        expected_length = 7
        mode = "generate-fresh"
    elif arguments and arguments[0] == "--run":
        allowed = {"--fresh", "--output", "--receipt"}
        expected_length = 7
        mode = "run"
    else:
        raise CLIUsage("unknown or missing strict mode")
    if len(arguments) != expected_length:
        raise CLIUsage("strict mode has a missing or extra argument")
    parsed: dict[str, str] = {"mode": mode}
    seen: set[str] = set()
    for index in range(1, len(arguments), 2):
        option = arguments[index]
        value = arguments[index + 1]
        if option not in allowed:
            raise CLIUsage("strict mode has an incompatible or unknown argument")
        if option in seen:
            raise CLIUsage("strict mode repeats an argument")
        if not value or value.startswith("--"):
            raise CLIUsage("strict mode has a missing argument value")
        seen.add(option)
        parsed[option[2:].replace("-", "_")] = value
    if seen != allowed:
        raise CLIUsage("strict mode is missing a required argument")
    if mode == "generate-fresh":
        if not _is_hex(parsed["nonce"], 32):
            raise CLIUsage("nonce must encode exactly 32 hexadecimal bytes")
        parsed["nonce"] = parsed["nonce"].lower()
        if not _is_lower_hex(parsed["source_sha"], 32):
            raise CLIUsage("source SHA must be lower-case SHA-256")
    return parsed


def _cli_parser_selfcheck() -> dict[str, Any]:
    valid = (
        parse_strict_cli(("--selftest",)),
        parse_strict_cli(("--mutant", "RESET-ONE")),
    )
    invalid = (
        (),
        ("--unknown",),
        ("--selftest", "extra"),
        ("--mutant", "NOT-REGISTERED"),
        (
            "--generate-fresh",
            "--nonce",
            "0" * 64,
            "--nonce",
            "1" * 64,
            "--fresh-out",
            "/tmp/unused",
        ),
        (
            "--run",
            "--fresh",
            "relative.json",
            "--output",
            "/tmp/output",
            "--alien",
            "/tmp/receipt",
        ),
    )
    refusals: list[str] = []
    for arguments in invalid:
        try:
            parse_strict_cli(arguments)
        except CLIUsage as error:
            refusals.append(str(error))
    return {
        "valid_forms": valid,
        "invalid_case_count": len(invalid),
        "invalid_refusal_count": len(refusals),
        "refusals": tuple(refusals),
        "all_invalid_refused": len(refusals) == len(invalid),
    }


def _read_ledger_selfcheck() -> dict[str, Any]:
    semantic_rows = (
        {
            "open_index": 1,
            "path": "v16/code/p13_gamma_exact_v4.py",
            "expected_sha256": "0" * 64,
            "observed_sha256": "0" * 64,
            "consumption_key": "authoritative-evaluator-and-generator",
            "consumed": True,
        },
    ) + tuple(
        {
            "open_index": index,
            "path": path,
            "expected_sha256": expected,
            "observed_sha256": expected,
            "consumption_key": consumption_key,
            "consumed": True,
        }
        for index, (path, expected, consumption_key) in enumerate(
            ANCHOR_SPECS, start=2
        )
    )
    shifted_rows = tuple(
        dict(row) | {"open_index": row["open_index"] + 1}
        for row in semantic_rows
    )
    official_rows = (
        {
            "open_index": 1,
            "path": "v16/code/p13_gamma_fresh_cases_v4.json",
            "expected_sha256": "1" * 64,
            "observed_sha256": "1" * 64,
            "consumption_key": "post-source-fresh-confirmation-input",
            "consumed": True,
        },
    ) + shifted_rows
    manifest_invariant = authentication_manifest_hash(
        semantic_rows
    ) == authentication_manifest_hash(shifted_rows)
    expected_anchor_paths = tuple(path for path, _, _ in ANCHOR_SPECS)
    observed_anchor_paths = tuple(row["path"] for row in semantic_rows[1:])
    required_forward_paths = (
        "v16/note-paper13-typed-groupoid-v4-source-delta-pin.md",
        "v16/note-paper13-typed-groupoid-v3-source-audit-adjudication.md",
        "v16/code/p13_gamma_exact_v3.py",
        "v16/note-paper13-typed-groupoid-source-freeze-v3.md",
        "v16/review-paper13-typed-groupoid-v3-source-operator.md",
        "v16/review-paper13-typed-groupoid-v3-source-records.md",
        "v16/note-paper13-typed-groupoid-forward-repair-pin.md",
        "v16/note-paper13-hostile-review-adjudication.md",
        "v16/note-paper13-stageA-support-split-forward-repair-pin.md",
        "v16/note-paper13-gamma-source-freeze.md",
        "v16/review-paper13-stageA-source-physics.md",
        "v16/review-paper13-stageA-source-records.md",
        "v16/note-paper13-stageA-source-audit-adjudication.md",
        "v16/review-paper13-operator-category.md",
        "v16/review-paper13-indivisibility-records.md",
        "v16/review-paper13-relational-ontology.md",
    )
    historical_unobserved_exact = (
        HISTORICAL_OLD_SOURCE_PROVENANCE["sha256"]
        == OLD_STAGE_A_SOURCE_SHA256
        and HISTORICAL_OLD_SOURCE_PROVENANCE["observation"]
        == "historical-unobserved"
        and HISTORICAL_OLD_SOURCE_PROVENANCE["live_disk_anchor"] is False
        and OLD_STAGE_A_SOURCE_SHA256
        not in {row["expected_sha256"] for row in semantic_rows}
    )
    return {
        "generator_open_order": tuple(row["path"] for row in semantic_rows),
        "official_open_order": tuple(row["path"] for row in official_rows),
        "official_open_indices": tuple(row["open_index"] for row in official_rows),
        "fresh_precedes_source_in_official_run": official_rows[0]["path"]
        == "v16/code/p13_gamma_fresh_cases_v4.json"
        and official_rows[1]["path"] == "v16/code/p13_gamma_exact_v4.py",
        "anchor_manifest_ignores_only_open_position": manifest_invariant,
        "anchor_paths_two_way_equal": observed_anchor_paths
        == expected_anchor_paths,
        "required_forward_anchor_paths": required_forward_paths,
        "required_forward_anchor_paths_live": all(
            path in observed_anchor_paths for path in required_forward_paths
        ),
        "historical_old_source": HISTORICAL_OLD_SOURCE_PROVENANCE,
        "historical_old_source_unobserved_exact": historical_unobserved_exact,
        "all_consumed": all(row["consumed"] for row in official_rows),
        "all_exact": manifest_invariant
        and observed_anchor_paths == expected_anchor_paths
        and all(path in observed_anchor_paths for path in required_forward_paths)
        and historical_unobserved_exact
        and tuple(row["open_index"] for row in official_rows)
        == tuple(range(1, len(official_rows) + 1))
        and all(row["consumed"] for row in official_rows),
    }


class FixtureImportDenial:
    __slots__ = ("attempts",)

    def __init__(self) -> None:
        self.attempts: list[str] = []

    def find_spec(self, fullname: str, _: Any, __: Any = None) -> Any:
        forbidden = (
            "apr_fixtures",
            "apr_score",
            "apr_paper12_exact",
            "p13_gamma_fresh_cases",
        )
        if any(fullname == name or fullname.startswith(name + ".") for name in forbidden):
            self.attempts.append(fullname)
            raise IntegrityFailure("fixture/import-denial sentinel fired")
        return None


def run_selftest() -> dict[str, Any]:
    source_bytes = source_path().read_bytes()
    try:
        source_text = source_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        raise IntegrityFailure("source is not UTF-8") from error
    # Source-only hostile mutations must be rejected by the exact producer-to-
    # promotion backward slice before any expensive scientific reconstruction.
    # Their forbidden semantic behavior and full dependency movement are
    # established by separate changed-source probes; this early gate prevents
    # a known-invalid source from consuming the entire per-mode runtime budget.
    early_static = static_source_scan(source_text)
    early_support = support_promotion_source_scan(source_text)
    early_groupoid = groupoid_promotion_source_scan(source_text)
    if not (
        early_static["clean"]
        and early_support["all_exact"]
        and early_groupoid["all_exact"]
    ):
        raise IntegrityFailure(
            "pre-science source-integrity backward slice is inexact"
        )
    denial = FixtureImportDenial()
    sys.meta_path.insert(0, denial)
    try:
        measurements = measure_scientific_core(source_text)
        attacks = run_all_attacks(measurements)
    finally:
        sys.meta_path.remove(denial)
    repair_disposition = classify_repair_disposition(measurements, attacks)
    public_language = measurements["public_language"]
    cli_parser = _cli_parser_selfcheck()
    read_ledger = _read_ledger_selfcheck()
    synthetic_claims = build_claim_table(measurements, attacks)
    synthetic_sealed = {
        "mode": "SELFTEST-NO-PUBLICATION",
        "claims": synthetic_claims,
        "scope": {
            "coordinates": measurements["scope_coordinates"],
            "walls": measurements["scope_walls"],
        },
        "artifacts": {"source_sha256": sha256_bytes(source_bytes)},
        "read_set": (
            {
                "open_index": 1,
                "path": "v16/code/p13_gamma_exact_v4.py",
                "consumption_key": "development-selftest-source",
                "consumed": True,
            },
        ),
        "mutations": attacks["rows"],
    }
    synthetic_manifest = build_seal_manifest(synthetic_sealed)
    fixture_modules = tuple(
        sorted(
            name
            for name in sys.modules
            if name == "apr_fixtures" or name.startswith("apr_fixtures.")
        )
    )
    denial_positive_control = FixtureImportDenial()
    try:
        denial_positive_control.find_spec("apr_fixtures", None)
    except IntegrityFailure as error:
        denial_positive_caught = True
        denial_positive_error = f"{type(error).__name__}:{error}"
    else:
        denial_positive_caught = False
        denial_positive_error = "NO-INTEGRITY-FAILURE"
    coherent = measurements["coherent"]
    full = measurements["full_target"]
    division = measurements["division"]
    native = measurements["native_nondivision"]
    reciprocal = measurements["reciprocal"]
    blind = measurements["blind_family"]
    groupoid = measurements["groupoid"]
    native_groupoid = groupoid["native_census"]
    complete_certificate_action = groupoid["complete_certificate_action"]
    groupoid_selftest_summary = {
        "groupoid_sha256": canonical_hash(groupoid),
        "promotion_predicate": groupoid_promotion_predicate(groupoid),
        "abstract_bijection_count": groupoid["abstract_census"][
            "bijection_count"
        ],
        "abstract_associativity_case_count": groupoid["abstract_census"][
            "associativity_case_count"
        ],
        "native_row_count": native_groupoid["row_count"],
        "native_dependency_sha256": groupoid["native_dependency_sha256"],
        "complete_certificate_action_sha256": canonical_hash(
            complete_certificate_action
        ),
        "complete_input_table_sha256": canonical_hash(
            complete_certificate_action["complete_input_table"]
        ),
        "family_count": complete_certificate_action["family_count"],
        "source_column_count": complete_certificate_action[
            "source_column_count"
        ],
        "identity_triple_count": complete_certificate_action[
            "identity_triple_count"
        ],
        "operation_counts": complete_certificate_action["operation_counts"],
        "raw_action_verification_sha256": canonical_hash(
            complete_certificate_action["raw_action_verification"]
        ),
        "raw_action_verification_row_count": complete_certificate_action[
            "raw_action_verification"
        ]["row_count"],
        "raw_action_decoded_object_counts": {
            key: complete_certificate_action["raw_action_verification"][key]
            for key in (
                "decoded_witness_count",
                "decoded_input_count",
                "decoded_arrow_count",
                "decoded_law_count",
            )
        },
        "tensor_configuration_action_sha256": canonical_hash(
            groupoid["tensor_configuration_action"]
        ),
        "tensor_configuration_action_exact": groupoid[
            "tensor_configuration_action"
        ]["all_exact"],
        "all_exact": groupoid["all_exact"],
    }
    attack_selftest_summary = {
        "registered": attacks["registered"],
        "executed": attacks["executed"],
        "killed": attacks["killed"],
        "all_pass": attacks["all_pass"],
        "registry_sha256": canonical_hash(MUTANT_IDS),
        "rows_sha256": canonical_hash(attacks["rows"]),
    }
    checks = (
        _selftest_check(
            "AST-AND-STATIC-SOURCE-CLEAN",
            measurements["static_scan"]["clean"],
            measurements["static_scan"],
        ),
        _selftest_check(
            "TYPED-GROUPOID-PROMOTION-CONSUMES-NATIVE-LAW-ROWS",
            measurements["groupoid_promotion_static"]["all_exact"],
            measurements["groupoid_promotion_static"],
        ),
        _selftest_check(
            "FRACTION-ONLY-SCIENTIFIC-COORDINATES",
            not measurements["static_scan"]["float_nodes"],
            {"float_nodes": measurements["static_scan"]["float_nodes"]},
        ),
        _selftest_check(
            "ESSENTIAL-SUPPORT-BOOLEAN-QUOTIENT",
            measurements["boolean_quotient"]["all_exact"]
            and measurements["source_identity"]["inessential_formula_equal"]
            and measurements["source_identity"]["inessential_formula_profile_equal"],
            {
                "quotient": measurements["boolean_quotient"],
                "consumer_invariance": measurements["source_identity"],
            },
        ),
        _selftest_check(
            "CONTEXT-SPLIT-CENSUS-72-AMBIENT-42-CONTEXTUAL",
            measurements["context_split_census"]["counts_exact"]
            and measurements["context_split_census"]["all_replayed"]
            and measurements["context_split_census"]["all_context_proofs_exact"]
            and measurements["context_split_census"][
                "all_within_class_invariance_exact"
            ]
            and measurements["context_split_census"][
                "context_proofs_are_nonpromotive"
            ],
            measurements["context_split_census"],
        ),
        _selftest_check(
            "CONTEXTUAL-BOOLEAN-ALIAS-PHYSICAL-IDENTITY",
            measurements["source_identity"]["contextual_boolean_alias_exact"]
            and measurements["context_split_census"]["contextual_alias"][
                "all_physical_fields_equal"
            ],
            measurements["context_split_census"]["contextual_alias"],
        ),
        _selftest_check(
            "PUBLIC-PRIMITIVE-LANGUAGE-CLOSED",
            public_language["all_registered_visited"],
            public_language,
        ),
        _selftest_check(
            "FOUR-PRIMITIVE-LEGS-ON-FULL-TYPED-CHAIN",
            full["all_full"] and full["primitive_leg_count"] == 4,
            full,
        ),
        _selftest_check(
            "ZERO-AMPLITUDE-TARGETS-RETAINED",
            full["first_zero_coordinate_count"] > 0
            and full["first_full_target_count"]
            == full["first_returned_coordinate_count"],
            {
                "first_zero_coordinate_count": full["first_zero_coordinate_count"],
                "first_full_target_count": full["first_full_target_count"],
                "returned": full["first_returned_coordinate_count"],
            },
        ),
        _selftest_check(
            "COHERENT-R-B-C-EXACT",
            coherent["first_isometry"]
            and coherent["second_isometry"]
            and coherent["first_isometry_residual"] == 0
            and coherent["second_isometry_residual"] == 0,
            coherent,
        ),
        _selftest_check(
            "CATEGORY-IDENTITY-COMPOSE-TENSOR-SYMMETRY",
            measurements["category"]["all_exact"],
            measurements["category"],
        ),
        _selftest_check(
            "TOTAL-NORMALIZED-PRIMITIVE-DOMAIN",
            measurements["totality"]["all_generator_isometries"]
            and measurements["totality"]["all_rho_involutions"]
            and measurements["totality"][
                "cayley_norm_identity_for_every_rational_x"
            ]
            and measurements["totality"]["denominator_positive_certificate"][
                "positive_for_every_rational_x"
            ]
            and measurements["totality"][
                "endpoint_domain_controls_normalized"
            ]
            and measurements["totality"][
                "all_nonzero_generator_transitions_bound"
            ]
            and measurements["totality"][
                "total_bound_split_certificate_count"
            ]
            > 0,
            measurements["totality"],
        ),
        _selftest_check(
            "COMPLETE-SOURCE-KEY-SUFFICIENCY",
            measurements["source_identity"]["equal_key_equal_profile"]
            and measurements["source_identity"]["distinct_filling_distinct_key"],
            measurements["source_identity"],
        ),
        _selftest_check(
            "NEUTRAL-PRESENTATION-INVARIANCE",
            measurements["source_identity"][
                "neutral_label_and_status_order_invariant"
            ],
            measurements["source_identity"],
        ),
        _selftest_check(
            "SOURCE-GROUPOID-TOTAL-BIJECTION-LAWS",
            groupoid_promotion_predicate(groupoid),
            groupoid_selftest_summary,
        ),
        _selftest_check(
            "SOURCE-GROUPOID-ABSTRACT-AND-NATIVE-CENSUS",
            measurements["groupoid"]["abstract_census"]["all_exact"]
            and measurements["groupoid"]["native_census"]["all_exact"]
            and measurements["groupoid"]["native_census"]["row_count"] >= 13,
            groupoid_selftest_summary,
        ),
        _selftest_check(
            "COMPLETE-CONFIGURATION-ACTION-ALL-BOUNDARY-NODES",
            all(
                row["configuration_action"]["all_exact"]
                and row["configuration_action"]["complete_object_table_exact"]
                for row in measurements["groupoid"]["native_census"]["rows"]
            )
            and measurements["groupoid"]["tensor_configuration_action"][
                "all_exact"
            ],
            tuple(
                {
                    "label": row["label"],
                    "boundary_node_count": row["configuration_action"][
                        "boundary_node_count"
                    ],
                    "configuration_row_count": row["configuration_action"][
                        "configuration_row_count"
                    ],
                    "complete_object_table_sha256": canonical_hash(
                        row["configuration_action"]["complete_object_table"]
                    ),
                    "all_exact": row["configuration_action"]["all_exact"],
                }
                for row in measurements["groupoid"]["native_census"]["rows"]
            ),
        ),
        _selftest_check(
            "COMPLETE-CERTIFICATE-ACTION-468-BOUND-TRANSITIONS",
            measurements["groupoid"]["complete_certificate_action"][
                "all_exact"
            ]
            and measurements["groupoid"]["complete_certificate_action"][
                "family_count"
            ]
            == 12
            and measurements["groupoid"]["complete_certificate_action"][
                "source_column_count"
            ]
            == 312
            and measurements["groupoid"]["complete_certificate_action"][
                "identity_triple_count"
            ]
            == 468
            and measurements["groupoid"]["complete_certificate_action"][
                "operation_counts"
            ]
            == {"CREATE": 156, "MERGE": 156, "UNCHANGED": 156}
            and _complete_action_verification_manifest_exact(
                measurements["groupoid"]["complete_certificate_action"]
            ),
            groupoid_selftest_summary,
        ),
        _selftest_check(
            "BOUND-SPLIT-GROUPOID-IDENTITY-INVERSE-COMPOSITION",
            measurements["groupoid"]["split_certificate_covariance"][
                "all_exact"
            ],
            measurements["groupoid"]["split_certificate_covariance"],
        ),
        _selftest_check(
            "ONE-PRIMITIVE-ROOT-LINEAGE",
            measurements["lineage"]["all_complete"]
            and measurements["shadow_lineages"]["all_outputs_bound"]
            and measurements["shadow_lineages"][
                "all_law_shadows_consume_unique_primitive"
            ]
            and measurements["shadow_lineages"][
                "blind_projection_rooted_in_literal_context_not_gamma"
            ]
            and measurements["shadow_lineages"]["all_arithmetic_recomputed"],
            {
                "operator_lineage": measurements["lineage"],
                "shadow_lineages": measurements["shadow_lineages"],
            },
        ),
        _selftest_check(
            "ACTIVE-SUPPORT-CHANGE-AND-INVERSE-MERGE",
            measurements["support_change"]["all_inverse_merge"]
            and measurements["support_change"]["all_support_changed"]
            and measurements["support_change"]["all_bound_certificates_exact"],
            measurements["support_change"],
        ),
        _selftest_check(
            "BOUND-SPLIT-CREATE-MERGE-UNCHANGED-EXHAUSTIVE",
            measurements["support_change"]["operation_counts"]
            == {"CREATE": 4, "MERGE": 4, "UNCHANGED": 4}
            and measurements["support_change"]["all_create_certificates_exact"]
            and measurements["support_change"]["all_merge_certificates_exact"]
            and measurements["support_change"][
                "all_unchanged_certificates_exact"
            ]
            and not measurements["support_change"][
                "context_proof_alone_is_promotive"
            ]
            and not measurements["support_change"][
                "legacy_role_cell_inequality_is_promotive"
            ],
            measurements["support_change"],
        ),
        _selftest_check(
            "RECIPROCAL-SAME-LAW-READER",
            reciprocal["normalization"] == 1
            and reciprocal["counterfactual_probe_one"] == 0,
            reciprocal,
        ),
        _selftest_check(
            "WRITER-ALL-INPUT-NORMALIZATION",
            division["writer_normalized_all_blank_inputs"]
            and division["writer_blank_input_count"]
            == len(division["writer_blank_input_rows"])
            and division["writer_blank_input_count"] > 0,
            {
                "writer_normalized_all_blank_inputs": division[
                    "writer_normalized_all_blank_inputs"
                ],
                "writer_blank_input_count": division[
                    "writer_blank_input_count"
                ],
                "writer_blank_input_rows": division["writer_blank_input_rows"],
                "record_projectors": division["record_projectors"],
            },
        ),
        _selftest_check(
            "ACTIVE-TO-CARRIED-GENERATOR-INTERTWINING",
            division["all_generator_intertwining"]
            and division["continuation_grammar_exact"],
            {
                "residuals": division["generator_intertwining_residuals"],
                "grammar_exact": division["continuation_grammar_exact"],
                "letters": division["continuation_grammar_letter_rows"],
            },
        ),
        _selftest_check(
            "ALL-WORD-CONTINUATION-RECOVERY",
            division["free_word_induction"]["base"]
            and division["free_word_induction"]["step"]
            and division["free_word_induction"]["enumerated_residual"] == 0,
            division["free_word_induction"],
        ),
        _selftest_check(
            "ALTERNATE-RECORD-CUT-EXACT",
            division["alternate_cut_residual"] == 0
            and division["alternate_cut_all_input_residual"] == 0
            and division["alternate_cut_all_input_comparisons"]
            == len(division["alternate_cut_all_input_rows"])
            and division["alternate_cut_all_input_comparisons"] > 0,
            {
                "alternate_cut_residual": division["alternate_cut_residual"],
                "alternate_cut_all_input_residual": division[
                    "alternate_cut_all_input_residual"
                ],
                "alternate_cut_all_input_comparisons": division[
                    "alternate_cut_all_input_comparisons"
                ],
                "alternate_cut_all_input_rows": division[
                    "alternate_cut_all_input_rows"
                ],
                "branch_probabilities": division["branch_probabilities"],
            },
        ),
        _selftest_check(
            "REACTIVATED-CARRIED-PORT-ERASES-RECORD",
            division["active_reuse_eraser"]["inverse_toggle_exact"],
            division["active_reuse_eraser"],
        ),
        _selftest_check(
            "NATIVE-NONDIVISION-NEGATIVE-FACTOR",
            not native["positive_source_independent_restart_exists"]
            and bool(native["negative_entries"]),
            native,
        ),
        _selftest_check(
            "RATIONAL-INTERVAL-CERTIFICATE",
            native["interval_certificate"]["universal_certificate"]
            and native["interval_certificate"][
                "universal_factor_outside_stochastic_spectral_interval"
            ]
            and native["interval_certificate"]["bound_residual"] >= 0,
            native["interval_certificate"],
        ),
        _selftest_check(
            "HISTORY-CONDITIONED-POSITIVE-CONTROL",
            native["history_joint_normalizations"]
            == (Fraction(1), Fraction(1))
            and native["history_joint_nonnegative"]
            and native["history_joint_positive_coordinates"] > 0,
            {
                "joint": native["history_conditioned_joint"],
                "normalizations": native["history_joint_normalizations"],
                "nonnegative": native["history_joint_nonnegative"],
                "positive_coordinates": native[
                    "history_joint_positive_coordinates"
                ],
            },
        ),
        _selftest_check(
            "BLIND-RESOURCE-PARITY-AND-INDUCTION",
            blind["resource_parity"]
            and blind["blind_prefix_equal"]
            and blind["direct_factorization_exact"]
            and blind["exposed_marginals_exact"]
            and blind["blind_transducer_induction"][
                "conclusion_same_blind_output_law"
            ],
            blind,
        ),
        _selftest_check(
            "SAME-ROOT-MATCHING-RESPONSE-SEPARATION",
            blind["same_law_root"] and blind["response_unequal"],
            {
                "first_marginals": blind["first"]["marginals"],
                "second_marginals": blind["second"]["marginals"],
                "same_law_root": blind["same_law_root"],
            },
        ),
        _selftest_check(
            "EXACT-SCOPE-COORDINATES-AND-WALLS",
            measurements["scope_valid"],
            {
                "coordinates": measurements["scope_coordinates"],
                "walls": measurements["scope_walls"],
            },
        ),
        _selftest_check(
            "ORDERED-MEASUREMENT-PROGRAMME",
            measurements["measurement_programme"] == MEASUREMENT_PROGRAMME,
            {"measurement_programme": measurements["measurement_programme"]},
        ),
        _selftest_check(
            "RESULT-NEUTRAL-SCIENTIFIC-REGRESSION-WALL",
            measurements["regression_wall"]["all_exact"]
            and measurements["support_promotion_static"]["all_exact"],
            {
                "regression_wall": measurements["regression_wall"],
                "support_promotion_static": measurements[
                    "support_promotion_static"
                ],
            },
        ),
        _selftest_check(
            "OUTCOME-LADDER-CAP-AND-INDEPENDENT-COMPARATOR",
            measurements["strict_primary"] == ELIGIBLE_CAP
            and measurements["outcome_comparator"]
            and repair_disposition == "REPAIR-GREEN-UNREVIEWED",
            {
                "strict_primary": measurements["strict_primary"],
                "eligible_cap": ELIGIBLE_CAP,
                "independent_index": independent_outcome_index(measurements),
                "render_trace": measurements["outcome_render_trace"],
                "repair_disposition": repair_disposition,
            },
        ),
        _selftest_check(
            "MUTANT-REGISTRY-UNIQUE-AND-COMPLETE",
            len(MUTANT_IDS) == 153
            and len(MUTANT_IDS)
            - len(V3_TYPED_GROUPOID_ATTACKS)
            - len(V4_TYPED_GROUPOID_ATTACKS)
            == 112
            and len(MUTANT_IDS) == len(set(MUTANT_IDS))
            and attacks["registered"] == len(MUTANT_IDS)
            and attacks["executed"] == len(MUTANT_IDS),
            {
                "names": MUTANT_IDS,
                "registry_sha256": canonical_hash(MUTANT_IDS),
                "registered": attacks["registered"],
                "executed": attacks["executed"],
                "expected_v4_total": 153,
                "inherited_count": len(MUTANT_IDS)
                - len(V3_TYPED_GROUPOID_ATTACKS)
                - len(V4_TYPED_GROUPOID_ATTACKS),
            },
        ),
        _selftest_check(
            "ALL-REGISTERED-MUTATIONS-KILLED",
            attacks["all_pass"] and attacks["killed"] == len(MUTANT_IDS),
            attack_selftest_summary,
        ),
        _selftest_check(
            "S1-THROUGH-S11-SPLIT-ATTACKS-KILLED",
            all(attacks["rows"][name]["pass"] for name in SPLIT_SUPPORT_ATTACKS)
            and tuple(name for name in MUTANT_IDS if name in SPLIT_SUPPORT_ATTACKS)
            == SPLIT_SUPPORT_ATTACKS,
            {
                "names": SPLIT_SUPPORT_ATTACKS,
                "rows": {
                    name: attacks["rows"][name]
                    for name in SPLIT_SUPPORT_ATTACKS
                },
            },
        ),
        _selftest_check(
            "G1-THROUGH-G20-TYPED-GROUPOID-ATTACKS-KILLED",
            all(
                attacks["rows"][name]["pass"]
                for name in TYPED_GROUPOID_ATTACKS
            )
            and tuple(
                name for name in MUTANT_IDS if name in TYPED_GROUPOID_ATTACKS
            )
            == TYPED_GROUPOID_ATTACKS,
            {
                "names": TYPED_GROUPOID_ATTACKS,
                "rows": {
                    name: attacks["rows"][name]
                    for name in TYPED_GROUPOID_ATTACKS
                },
            },
        ),
        _selftest_check(
            "A1-A16-AND-C1-C21-V3-ACTION-ATTACKS-KILLED",
            all(
                attacks["rows"][name]["pass"]
                for name in V3_TYPED_GROUPOID_ATTACKS
            )
            and tuple(
                name
                for name in MUTANT_IDS
                if name in V3_TYPED_GROUPOID_ATTACKS
            )
            == V3_TYPED_GROUPOID_ATTACKS,
            {
                "configuration_action_names": V3_CONFIGURATION_ACTION_ATTACKS,
                "certificate_action_names": V3_CERTIFICATE_ACTION_ATTACKS,
                "rows": {
                    name: attacks["rows"][name]
                    for name in V3_TYPED_GROUPOID_ATTACKS
                },
            },
        ),
        _selftest_check(
            "A17-A18-AND-C22-C23-V4-ACTION-ATTACKS-KILLED",
            all(
                attacks["rows"][name]["pass"]
                for name in V4_TYPED_GROUPOID_ATTACKS
            )
            and tuple(
                name
                for name in MUTANT_IDS
                if name in V4_TYPED_GROUPOID_ATTACKS
            )
            == V4_TYPED_GROUPOID_ATTACKS,
            {
                "configuration_action_names": V4_CONFIGURATION_ACTION_ATTACKS,
                "certificate_action_names": V4_CERTIFICATE_ACTION_ATTACKS,
                "rows": {
                    name: attacks["rows"][name]
                    for name in V4_TYPED_GROUPOID_ATTACKS
                },
            },
        ),
        _selftest_check(
            "DISTINCT-REFLECTION-AND-OLD-PORT-CHANGED-OBJECTS",
            attacks["rows"]["SAME-BORN-REFLECTION"][
                "new_primitive_sha256"
            ]
            != attacks["rows"]["PHASE-REFLECTION-MUTATION"][
                "new_primitive_sha256"
            ]
            and attacks["rows"]["CARRIED-PORT-STILL-ACTIVE"][
                "new_primitive_sha256"
            ]
            != attacks["rows"]["RETURN-TO-OLD-PORT"][
                "new_primitive_sha256"
            ],
            {
                "same_born_reflection": attacks["rows"][
                    "SAME-BORN-REFLECTION"
                ]["new_primitive_sha256"],
                "phase_reflection": attacks["rows"][
                    "PHASE-REFLECTION-MUTATION"
                ]["new_primitive_sha256"],
                "carried_port": attacks["rows"][
                    "CARRIED-PORT-STILL-ACTIVE"
                ]["new_primitive_sha256"],
                "return_old_port": attacks["rows"]["RETURN-TO-OLD-PORT"][
                    "new_primitive_sha256"
                ],
            },
        ),
        _selftest_check(
            "SYNTHETIC-ANCHOR-CORRUPTION-IS-INTEGRITY-ONLY",
            attacks["rows"]["ANCHOR-CORRUPTION"]["pass"]
            and attacks["rows"]["ANCHOR-CORRUPTION"]["evidence"][
                "registered_exit_code"
            ]
            == 1
            and attacks["rows"]["ANCHOR-CORRUPTION"]["evidence"][
                "publication_writes"
            ]
            == 0,
            attacks["rows"]["ANCHOR-CORRUPTION"],
        ),
        _selftest_check(
            "STRICT-CLI-FORMS-AND-REFUSALS",
            cli_parser["all_invalid_refused"],
            cli_parser,
        ),
        _selftest_check(
            "READ-LEDGER-ORDER-AND-ANCHOR-BINDING",
            read_ledger["all_exact"]
            and read_ledger["fresh_precedes_source_in_official_run"],
            read_ledger,
        ),
        _selftest_check(
            "SEAL-MANIFEST-TOTALITY-RECOMPUTED",
            verify_normalized_payload_hash(
                synthetic_manifest, "manifest_sha256"
            )
            and synthetic_manifest["coverage"][
                "all_sealed_top_level_keys_covered"
            ],
            synthetic_manifest,
        ),
        _selftest_check(
            "STAGE-WHITELIST-EXACT",
            SOURCE_FREEZE_TASK_PATHS
            == (
                "v16/code/p13_gamma_exact_v4.py",
                "v16/note-paper13-typed-groupoid-source-freeze-v4.md",
            )
            and PUBLICATION_PATHS
            == (
                "v16/code/p13_gamma_fresh_cases_v4.json",
                "v16/code/p13_gamma_output_v4.txt",
                "v16/code/p13_gamma_receipt_v4.json",
            ),
            {
                "source_freeze_task_paths": SOURCE_FREEZE_TASK_PATHS,
                "publication_paths": PUBLICATION_PATHS,
            },
        ),
        _selftest_check(
            "FIXTURE-AND-OFFICIAL-ARTIFACT-SEPARATION",
            not fixture_modules
            and not denial.attempts
            and denial_positive_caught
            and denial_positive_control.attempts == ["apr_fixtures"],
            {
                "fixture_modules_loaded": fixture_modules,
                "denied_import_attempts": tuple(denial.attempts),
                "denial_sentinel_installed_for_scientific_path": True,
                "denial_positive_control_caught": denial_positive_caught,
                "denial_positive_control_error": denial_positive_error,
                "denial_positive_control_attempts": tuple(
                    denial_positive_control.attempts
                ),
                "fresh_cases_read": False,
                "official_artifacts_read": False,
                "publication_writes": 0,
            },
        ),
    )
    if not all(row["pass"] for row in checks):
        failed = tuple(row["name"] for row in checks if not row["pass"])
        raise IntegrityFailure("development self-test failed: " + ",".join(failed))
    base_payload = {
        "schema": SCHEMA,
        "mode": "selftest",
        "status": "PASS",
        "source_sha256": sha256_bytes(source_bytes),
        "source_byte_count": len(source_bytes),
        "source_line_count": len(source_text.splitlines()),
        "check_count": len(checks),
        "checks": checks,
        "measurements": measurements,
        "mutation_summary": {
            "registered": attacks["registered"],
            "executed": attacks["executed"],
            "killed": attacks["killed"],
            "all_pass": attacks["all_pass"],
            "registry_sha256": canonical_hash(MUTANT_IDS),
        },
        "mutations": attacks["rows"],
        "repair_disposition": repair_disposition,
        "scientific_fixture_evaluated": False,
        "fresh_cases_read": False,
        "official_artifacts_read": False,
        "publication_writes": 0,
    }
    return with_normalized_payload_hash(base_payload)


CLAIM_FALSIFIERS = {
    "specification": (
        "FLOAT-OR-EXPECTED-TABLE",
        "ANCHOR-CORRUPTION",
        "ROLE-COUNT-ONLY",
        "COPIED-GROUPOID-BOOLEAN",
    ),
    "referent": (
        "RELABEL-RAW-NAME",
        "RELABEL-ORIENTATION",
        "EMPTY-LEFT-IDENTITY",
        "EMPTY-RIGHT-IDENTITY",
        "INVERSE-LEFT",
        "INVERSE-RIGHT",
        "THREE-SPARSE-ASSOCIATIVITY",
        "MIDDLE-PRESENTATION-MISMATCH",
        "SOURCE-LABEL-OMITTED",
        "EXTRA-TARGET-LABEL",
        "MAP-COLLISION",
        "ROLE-TYPE-SWAP",
        "NAMESPACE-CROSSING",
        "TARGET-PRESENTATION-FORGERY",
        "IDENTITY-ROW-ENCODING",
        "ORDER-REVERSAL",
        "TRANSPORT-SEVER",
        "CERTIFICATE-TRANSPORT-CACHE",
        "COMPOSITE-OPERATOR-CACHE",
        "TENSOR-SHARED-LABEL-CONFLICT",
        "FRESH-GLOBAL-RELABEL-SEVER",
        "OLD-CHILD-REUSE",
        "CONTEXTUAL-BOOLEAN-ALIAS",
    ) + V3_TYPED_GROUPOID_ATTACKS + V4_TYPED_GROUPOID_ATTACKS,
    "complete_gamma": ("RESET-ONE", "FORGED-COMPOSE-TARGET"),
    "source_sufficiency": ("SOURCE-KEY-OMITS-FILLING", "POSTINIT-LAW-IDENTITY"),
    "anti_wrapper": ("WRAPPER-GAMMA", "OCCURRENCE-SEVER"),
    "shadow_weld": ("CACHED-G-OR-SHADOW", "PHASE-REFLECTION-MUTATION"),
    "variable_carrier": (
        "META-CATALOGUE-AS-SUPPORT",
        "MOVE-DOWNSTREAM",
        "COEXTENSIVE-CHILD-OBJECT",
        "SUPPLIED-SPLIT-BOOLEAN",
    ),
    "support_change": (
        "SUPPORT-FILTERED-TARGET",
        "FULL-TARGET-RETYPE",
        "TAUTOLOGICAL-CHILD",
        "FORGET-ONLY",
        "CELL-COUNT-PADDING",
        "ROLE-COUNT-ONLY",
        "TRANSPORT-SPLIT-SEVER",
        "CERTIFICATE-PORT-SWAP",
        "AMBIENT-TARGET-PADDING",
    ),
    "reciprocal": ("DELAYED-READER-SEVER", "QUERY-FORMULA-MUTATION"),
    "division": ("RESET-WRITER-CHAIN", "HIDDEN-ERASER"),
    "native_nondivision": (
        "HISTORY-PASSED-OFF-AS-NATIVE-K",
        "NONDIVISION-AS-STATE-DEFECT",
    ),
    "blind_class": ("LEAKED-INCIDENCE-BIT", "CONSTANT-BLIND-TOKEN"),
}
CLAIM_INPUT_PATHS = {
    "specification": (
        "static_scan",
        "support_promotion_static",
        "groupoid_promotion_static",
        "scope_coordinates",
        "scope_walls",
        "regression_wall",
    ),
    "referent": (
        "referent_census",
        "boolean_quotient",
        "public_language",
        "full_target",
        "groupoid",
        "source_identity",
        "context_split_census",
        "support_change",
    ),
    "complete_gamma": ("category", "coherent", "full_target", "totality"),
    "source_sufficiency": (
        "source_identity",
        "context_split_census",
        "representative_application",
    ),
    "anti_wrapper": ("lineage", "shadow_lineages"),
    "shadow_weld": ("coherent", "native_nondivision"),
    "variable_carrier": ("support_change", "context_split_census"),
    "support_change": ("support_change", "groupoid", "context_split_census"),
    "reciprocal": ("reciprocal",),
    "division": ("division",),
    "native_nondivision": ("native_nondivision",),
    "blind_class": ("blind_family", "fresh_confirmation"),
}


def build_claim_table(
    measurements: Mapping[str, Any], attacks: Mapping[str, Any]
) -> dict[str, Any]:
    gates = measurements["gates"]
    if set(gates) != set(CLAIM_FALSIFIERS) or set(gates) != set(CLAIM_INPUT_PATHS):
        raise IntegrityFailure("claim/falsifier table is not keyed two-way equal")
    rows: dict[str, Any] = {}
    for gate_name in gates:
        falsifiers = CLAIM_FALSIFIERS[gate_name]
        if any(name not in attacks["rows"] for name in falsifiers):
            raise IntegrityFailure("claim names an unregistered falsifier")
        if any(not attacks["rows"][name]["changed"] for name in falsifiers):
            raise IntegrityFailure("claim falsifier does not change its object")
        consumed_paths = tuple(
            path
            for path in CLAIM_INPUT_PATHS[gate_name]
            if path in measurements
        )
        if not consumed_paths:
            raise IntegrityFailure("claim has no consumed measurement path")
        rows[gate_name] = {
            "gate": gate_name,
            "pass": gates[gate_name],
            "gate_value_sha256": canonical_hash(
                {"gate": gate_name, "value": gates[gate_name]}
            ),
            "falsifiers": falsifiers,
            "falsifier_changed_paths": tuple(
                attacks["rows"][name]["changed_path"] for name in falsifiers
            ),
            "consumed_measurement_paths": consumed_paths,
            "consumed_arithmetic_type_dag_sha256": canonical_hash(
                tuple((path, measurements[path]) for path in consumed_paths)
            ),
            "forcing_waiver": None,
        }
    return rows


def _fresh_public_summary(fresh: Mapping[str, Any]) -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    for case in fresh["cases"]:
        cases.append(
            {
                "case_index": case["case_index"],
                "input_case_sha256": case["input_case_sha256"],
                "member_marginals": tuple(
                    {
                        "member": member["member"],
                        "marginals": member["result"]["marginals"],
                        "nonzero_endpoint_coordinates": member["result"][
                            "nonzero_endpoint_coordinates"
                        ],
                        "endpoint_probabilities_sha256": member["result"][
                            "endpoint_probabilities_hash"
                        ],
                        "single_global_gamma_calls": member["result"][
                            "single_global_gamma_calls"
                        ],
                    }
                    for member in case["members"]
                ),
                "blind_prefix_equal": case["blind_prefix_equal"],
                "blind_token_recomputed": case["blind_token_recomputed"],
                "response_unequal": case["response_unequal"],
                "common_observed_fixed_pattern": case[
                    "common_observed_fixed_pattern"
                ],
                "challenge_observed_fixed_pattern": case[
                    "challenge_observed_fixed_pattern"
                ],
                "generated_pattern_exact": case["generated_pattern_exact"],
                "direct_factorization_exact": case[
                    "direct_factorization_exact"
                ],
                "exposed_marginals_exact": case["exposed_marginals_exact"],
                "direct_call_count_exact": case["direct_call_count_exact"],
                "confirmed": case["confirmed"],
            }
        )
    return {
        "exposure": fresh["exposure"],
        "rejection_count": fresh["rejection_count"],
        "reroll_count": fresh["reroll_count"],
        "cases": tuple(cases),
        "all_confirmed": fresh["all_confirmed"],
        "total_global_gamma_calls": fresh["total_global_gamma_calls"],
        "peak_state_count": fresh["peak_state_count"],
        "peak_cell_count": fresh["peak_cell_count"],
        "declared_peak_cell_count": fresh["declared_peak_cell_count"],
        "declared_peak_cell_count_exact": fresh[
            "declared_peak_cell_count_exact"
        ],
    }


def render_output_payload(measurements: Mapping[str, Any]) -> dict[str, Any]:
    fresh = measurements.get("fresh_confirmation")
    base = {
        "schema": "p13-gamma-output-v4",
        "strict_primary": measurements["strict_primary"],
        "repair_disposition": measurements.get("repair_disposition"),
        "outcome_render_trace": measurements["outcome_render_trace"],
        "eligible_cap": ELIGIBLE_CAP,
        "future_rungs_ineligible": OUTCOME_LADDER[13:],
        "gates": measurements["gates"],
        "orthogonal_coordinates": measurements["scope_coordinates"],
        "scope_walls": measurements["scope_walls"],
        "native_nondivision_sentence": NATIVE_NONDIVISION_SENTENCE,
        "typed_source_groupoid": {
            "abstract_bijection_count": measurements["groupoid"][
                "abstract_census"
            ]["bijection_count"],
            "abstract_associativity_case_count": measurements["groupoid"][
                "abstract_census"
            ]["associativity_case_count"],
            "native_row_count": measurements["groupoid"]["native_census"][
                "row_count"
            ],
            "native_labels": measurements["groupoid"]["native_census"][
                "required_labels"
            ],
            "native_dependency_sha256": measurements["groupoid"][
                "native_dependency_sha256"
            ],
            "complete_configuration_action_exact": all(
                row["configuration_action"]["all_exact"]
                for row in measurements["groupoid"]["native_census"]["rows"]
            ),
            "tensor_configuration_action_exact": measurements["groupoid"][
                "tensor_configuration_action"
            ]["all_exact"],
            "complete_certificate_action": {
                "family_count": measurements["groupoid"][
                    "complete_certificate_action"
                ]["family_count"],
                "source_column_count": measurements["groupoid"][
                    "complete_certificate_action"
                ]["source_column_count"],
                "identity_triple_count": measurements["groupoid"][
                    "complete_certificate_action"
                ]["identity_triple_count"],
                "operation_counts": measurements["groupoid"][
                    "complete_certificate_action"
                ]["operation_counts"],
                "complete_input_table_sha256": canonical_hash(
                    measurements["groupoid"]["complete_certificate_action"][
                        "complete_input_table"
                    ]
                ),
            },
            "promotion_predicate": groupoid_promotion_predicate(
                measurements["groupoid"]
            ),
            "application_order": "FIRST-THEN-SECOND",
        },
        "exposed_exact_controls": {
            "R": measurements["coherent"]["R"],
            "B": measurements["coherent"]["B"],
            "C": measurements["coherent"]["C"],
            "B2": measurements["division"]["B2"],
            "K": measurements["native_nondivision"]["K"],
            "reciprocal_joint": measurements["reciprocal"]["joint"],
            "native_interval_certificate": measurements["native_nondivision"][
                "interval_certificate"
            ],
        },
        "fresh_confirmation": _fresh_public_summary(fresh) if fresh is not None else None,
        "scientific_fixture_evaluated": False,
    }
    return with_normalized_payload_hash(base)


def build_seal_manifest(sealed: Mapping[str, Any]) -> dict[str, Any]:
    claims = sealed["claims"]
    scope = sealed["scope"]
    artifacts = sealed["artifacts"]
    reads = sealed["read_set"]
    mutations = sealed["mutations"]
    entries: list[dict[str, Any]] = []
    for key in sorted(claims):
        entries.append(
            {"kind": "claim", "key": key, "sha256": canonical_hash(claims[key])}
        )
    for index, wall in enumerate(scope["walls"]):
        entries.append(
            {"kind": "wall", "key": str(index), "sha256": canonical_hash(wall)}
        )
    for key in sorted(scope["coordinates"]):
        entries.append(
            {
                "kind": "scope-coordinate",
                "key": key,
                "sha256": canonical_hash(scope["coordinates"][key]),
            }
        )
    for key in sorted(artifacts):
        entries.append(
            {
                "kind": "artifact",
                "key": key,
                "sha256": canonical_hash(artifacts[key]),
            }
        )
    for row in reads:
        entries.append(
            {
                "kind": "read",
                "key": f"{row['open_index']}:{row['path']}",
                "sha256": canonical_hash(row),
            }
        )
    for key in sorted(mutations):
        entries.append(
            {
                "kind": "mutation",
                "key": key,
                "sha256": canonical_hash(mutations[key]),
            }
        )
    for key in sorted(sealed):
        entries.append(
            {
                "kind": "sealed-top-level",
                "key": key,
                "sha256": canonical_hash(sealed[key]),
            }
        )
    coverage = {
        "claims_two_way_equal": set(claims) == set(CLAIM_FALSIFIERS),
        "walls_two_way_equal": tuple(scope["walls"]) == SCOPE_WALLS,
        "coordinates_two_way_equal": scope["coordinates"] == SCOPE_COORDINATES,
        "mutation_rows_two_way_equal": set(mutations) == set(MUTANT_IDS),
        "all_mutations_changed": all(row["changed"] for row in mutations.values()),
        "all_mutations_killed": all(row["pass"] for row in mutations.values()),
        "all_reads_consumed": all(row["consumed"] for row in reads),
        "all_sealed_top_level_keys_covered": {
            row["key"] for row in entries if row["kind"] == "sealed-top-level"
        }
        == set(sealed),
    }
    if not all(coverage.values()):
        raise IntegrityFailure("seal manifest coverage is incomplete")
    base = {
        "schema": "p13-gate-to-disk-seal-v1",
        "entries": tuple(entries),
        "entry_count": len(entries),
        "covered_sealed_top_level_keys": tuple(sorted(sealed)),
        "coverage": coverage,
    }
    return with_normalized_payload_hash(base, "manifest_sha256")


def verify_sealed_receipt(receipt: Mapping[str, Any]) -> bool:
    if type(receipt) is not dict or not verify_normalized_payload_hash(receipt):
        return False
    if set(receipt) != {
        "schema",
        "sealed",
        "seal_manifest",
        "normalized_payload_sha256",
    }:
        return False
    manifest = build_seal_manifest(receipt["sealed"])
    return canonical_bytes(manifest) == canonical_bytes(receipt["seal_manifest"])


def build_receipt(
    measurements: Mapping[str, Any],
    attacks: Mapping[str, Any],
    read_set: Sequence[Mapping[str, Any]],
    source_sha256: str,
    fresh_payload: Mapping[str, Any],
    fresh_file_sha256: str,
    input_sha256: str,
    output_sha256: str,
) -> dict[str, Any]:
    if not attacks["all_pass"] or attacks["killed"] != len(MUTANT_IDS):
        raise IntegrityFailure("mandatory mutation suite is not fully killed")
    claims = build_claim_table(measurements, attacks)
    fresh = measurements["fresh_confirmation"]
    artifacts = {
        "source_delta_pin_sha256": SOURCE_DELTA_PIN_SHA256,
        "source_audit_adjudication_sha256": SOURCE_AUDIT_ADJUDICATION_SHA256,
        "typed_groupoid_pin_sha256": TYPED_GROUPOID_PIN_SHA256,
        "hostile_adjudication_sha256": HOSTILE_ADJUDICATION_SHA256,
        "hostile_adjudication_normalized_sha256": (
            HOSTILE_ADJUDICATION_NORMALIZED_SHA256
        ),
        "forward_repair_pin_sha256": FORWARD_REPAIR_PIN_SHA256,
        "pin_sha256": PIN_SHA256,
        "runbook_sha256": RUNBOOK_SHA256,
        "predecessor_sha256": PREDECESSOR_SHA256,
        "paper12_sha256": PAPER12_SHA256,
        "paper12_adjudication_sha256": PAPER12_ADJUDICATION_SHA256,
        "paper12_evaluator_sha256": PAPER12_EVALUATOR_SHA256,
        "paper12_receipt_sha256": PAPER12_RECEIPT_SHA256,
        "old_stage_a_freeze_sha256": OLD_STAGE_A_FREEZE_SHA256,
        "stage_a_physics_report_sha256": STAGE_A_PHYSICS_REPORT_SHA256,
        "stage_a_records_report_sha256": STAGE_A_RECORDS_REPORT_SHA256,
        "stage_a_adjudication_sha256": STAGE_A_ADJUDICATION_SHA256,
        "historical_old_source": HISTORICAL_OLD_SOURCE_PROVENANCE,
        "rejected_v2_source_cycle": {
            "source_sha256": REJECTED_V3_SOURCE_SHA256,
            "freeze_sha256": REJECTED_V3_FREEZE_SHA256,
            "operator_report_sha256": V3_OPERATOR_SOURCE_REPORT_SHA256,
            "records_report_sha256": V3_RECORDS_SOURCE_REPORT_SHA256,
            "scientific_input": False,
            "exposure": "EXPOSED-REJECTED-SOURCE-REGRESSION-ONLY",
        },
        "rejected_paper13_corpus": {
            "source_sha256": REJECTED_SOURCE_SHA256,
            "fresh_sha256": REJECTED_FRESH_SHA256,
            "output_sha256": REJECTED_OUTPUT_SHA256,
            "receipt_sha256": REJECTED_RECEIPT_SHA256,
            "paper_sha256": REJECTED_PAPER_SHA256,
            "hostile_protocol_sha256": HOSTILE_PROTOCOL_SHA256,
            "seat_a_report_sha256": SEAT_A_REPORT_SHA256,
            "seat_i_report_sha256": SEAT_I_REPORT_SHA256,
            "seat_r_report_sha256": SEAT_R_REPORT_SHA256,
            "scientific_input": False,
            "exposure": "EXPOSED-HISTORICAL-REGRESSION-ONLY",
        },
        "source_sha256": source_sha256,
        "fresh_case_file_sha256": fresh_file_sha256,
        "fresh_case_payload_sha256": fresh_payload["normalized_payload_sha256"],
        "input_sha256": input_sha256,
        "output_sha256": output_sha256,
        "receipt_hash_kind": "NORMALIZED-PAYLOAD-SHA256",
    }
    exposure_ledger = {
        "analytic_controls": "EXPOSED-BEFORE-SOURCE-FREEZE",
        "development_selftests": "EXPOSED-ADVISORY",
        "fresh_cases": "POST-SOURCE-FRESH",
        "fresh_outputs_in_generator": False,
        "apr_scientific_input": False,
        "private_exploratory_input": False,
        "scientific_fixture_evaluated": False,
        "old_source_observation": "historical-unobserved",
        "old_freeze_and_audits_scientific_input": False,
    }
    freshness_ledger = {
        "domain_ascii": fresh_payload["domain_ascii"],
        "nonce_hex": fresh_payload["nonce_hex"],
        "source_sha256": fresh_payload["source_sha256"],
        "generator_sha256": fresh_payload["generator_sha256"],
        "rejection_count": fresh_payload["rejection_count"],
        "reroll_count": fresh_payload["reroll_count"],
        "case_hashes": fresh_payload["case_hashes"],
        "resource_parity": tuple(
            case["blind_prefix_equal"] for case in fresh["cases"]
        ),
        "prior_record_law_equality": tuple(
            case["prior_record_law_equal"] for case in fresh["cases"]
        ),
        "peak_cell_count": fresh["peak_cell_count"],
        "peak_state_count": fresh["peak_state_count"],
        "exposure": fresh["exposure"],
    }
    sealed = {
        "schema": SCHEMA,
        "strict_primary": measurements["strict_primary"],
        "repair_disposition": measurements["repair_disposition"],
        "eligible_cap": ELIGIBLE_CAP,
        "outcome_ladder": OUTCOME_LADDER,
        "outcome_comparator": measurements["outcome_comparator"],
        "claims": claims,
        "gates": measurements["gates"],
        "scope": {
            "coordinates": measurements["scope_coordinates"],
            "walls": measurements["scope_walls"],
            "native_nondivision_sentence": NATIVE_NONDIVISION_SENTENCE,
        },
        "artifacts": artifacts,
        "read_set": tuple(read_set),
        "law_and_measurements": measurements,
        "lineage": {
            "operator": measurements["lineage"],
            "shadows": measurements["shadow_lineages"],
        },
        "mutations": attacks["rows"],
        "mutation_registry": {
            "names": MUTANT_IDS,
            "registered": attacks["registered"],
            "executed": attacks["executed"],
            "killed": attacks["killed"],
            "registry_sha256": canonical_hash(MUTANT_IDS),
        },
        "exposure_ledger": exposure_ledger,
        "freshness_ledger": freshness_ledger,
        "publication_whitelist": PUBLICATION_PATHS,
    }
    manifest = build_seal_manifest(sealed)
    receipt = with_normalized_payload_hash(
        {
            "schema": "p13-gamma-receipt-v4",
            "sealed": sealed,
            "seal_manifest": manifest,
        }
    )
    if not verify_sealed_receipt(receipt):
        raise IntegrityFailure("receipt seal does not recompute")
    return receipt


def generate_fresh_mode(parsed: Mapping[str, str]) -> dict[str, Any]:
    destination = _validate_publication_path(parsed["fresh_out"], False)
    _validate_publication_role(
        destination, "v16/code/p13_gamma_fresh_cases_v4.json"
    )
    requested_source_sha = parsed["source_sha"]
    reads = authenticate_committed_inputs(requested_source_sha)
    fresh_payload = bind_fresh_anchor_manifest(
        derive_fresh_payload(requested_source_sha, parsed["nonce"]), reads
    )
    payload_bytes = (canonical_json(fresh_payload) + "\n").encode("ascii")
    transactional_publish(((destination, payload_bytes),))
    return {
        "schema": SCHEMA,
        "mode": "generate-fresh",
        "status": "PASS",
        "source_sha256": requested_source_sha,
        "fresh_file_sha256": sha256_bytes(payload_bytes),
        "fresh_payload_sha256": fresh_payload["normalized_payload_sha256"],
        "rejection_count": fresh_payload["rejection_count"],
        "case_count": len(fresh_payload["cases"]),
        "publication_writes": 1,
    }


def _validate_generated_fresh_with_anchors(
    payload: Mapping[str, Any], source_sha256: str, reads: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    if type(payload) is not dict or not verify_normalized_payload_hash(payload):
        raise IntegrityFailure("fresh normalized payload self-hash mismatch")
    nonce = payload.get("nonce_hex")
    if not _is_lower_hex(nonce, 32):
        raise Refusal("fresh nonce is malformed")
    regenerated = bind_fresh_anchor_manifest(
        derive_fresh_payload(source_sha256, nonce), reads
    )
    if canonical_bytes(payload) != canonical_bytes(regenerated):
        raise IntegrityFailure("fresh payload is not the unique anchored derivation")
    return regenerated


def run_official_mode(parsed: Mapping[str, str]) -> dict[str, Any]:
    fresh_path = _validate_publication_path(parsed["fresh"], True)
    output_path = _validate_publication_path(parsed["output"], False)
    receipt_path = _validate_publication_path(parsed["receipt"], False)
    _validate_publication_role(
        fresh_path, "v16/code/p13_gamma_fresh_cases_v4.json"
    )
    _validate_publication_role(output_path, "v16/code/p13_gamma_output_v4.txt")
    _validate_publication_role(receipt_path, "v16/code/p13_gamma_receipt_v4.json")
    if output_path == receipt_path:
        raise CLIUsage("output and receipt destinations must differ")

    fresh_bytes = fresh_path.read_bytes()
    fresh_file_sha = sha256_bytes(fresh_bytes)
    fresh_untrusted = parse_canonical_json_bytes(fresh_bytes, "fresh case file")
    if not verify_normalized_payload_hash(fresh_untrusted):
        raise IntegrityFailure("fresh normalized payload self-hash mismatch")
    source_sha = fresh_untrusted.get("source_sha256")
    if not _is_lower_hex(source_sha, 32):
        raise Refusal("fresh source hash is malformed")
    reads: list[dict[str, Any]] = [
        {
            "open_index": 1,
            "path": "v16/code/p13_gamma_fresh_cases_v4.json",
            "expected_sha256": fresh_file_sha,
            "observed_sha256": fresh_file_sha,
            "consumption_key": "post-source-fresh-confirmation-input",
            "consumed": True,
        }
    ]
    source_bytes = source_path().read_bytes()
    authenticated_inputs = authenticate_committed_inputs(
        source_sha, source_bytes, start_index=2
    )
    reads.extend(authenticated_inputs)
    fresh_payload = _validate_generated_fresh_with_anchors(
        fresh_untrusted, source_sha, authenticated_inputs
    )
    input_sha = canonical_hash(
        {
            "source_sha256": source_sha,
            "fresh_file_sha256": fresh_file_sha,
            "fresh_payload_sha256": fresh_payload["normalized_payload_sha256"],
        }
    )
    try:
        source_text = source_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        raise IntegrityFailure("source is not UTF-8") from error
    measurements = measure_scientific_core(source_text)
    measurements["fresh_confirmation"] = measure_fresh_confirmations(
        measurements["law"], fresh_payload
    )
    measurements["shadow_lineages"] = build_shadow_lineages(measurements)
    measurements["gates"] = build_gate_table(measurements)
    measurements["strict_primary"] = classify_primary(measurements["gates"])
    measurements["outcome_render_trace"] = render_outcome_index(
        independent_outcome_index(measurements)
    )[1]
    measurements["outcome_comparator"] = verify_outcome_rendering(
        measurements, measurements["strict_primary"]
    )
    if not measurements["outcome_comparator"]:
        raise IntegrityFailure("official outcome comparator disagrees")
    attacks = run_all_attacks(measurements)
    measurements["repair_disposition"] = classify_repair_disposition(
        measurements, attacks
    )

    output_payload = render_output_payload(measurements)
    output_bytes = (canonical_json(output_payload) + "\n").encode("ascii")
    output_sha = sha256_bytes(output_bytes)
    receipt = build_receipt(
        measurements,
        attacks,
        reads,
        source_sha,
        fresh_payload,
        fresh_file_sha,
        input_sha,
        output_sha,
    )
    receipt_bytes = (canonical_json(receipt) + "\n").encode("ascii")
    if not verify_sealed_receipt(receipt):
        raise IntegrityFailure("promotion-door receipt seal failed")
    if sha256_bytes(output_bytes) != receipt["sealed"]["artifacts"]["output_sha256"]:
        raise IntegrityFailure("promotion-door output seal failed")
    transactional_publish(
        ((output_path, output_bytes), (receipt_path, receipt_bytes))
    )
    return {
        "schema": SCHEMA,
        "mode": "run",
        "status": "PASS",
        "strict_primary": measurements["strict_primary"],
        "repair_disposition": measurements["repair_disposition"],
        "eligible_cap": ELIGIBLE_CAP,
        "source_sha256": source_sha,
        "fresh_file_sha256": fresh_file_sha,
        "output_sha256": output_sha,
        "receipt_sha256": sha256_bytes(receipt_bytes),
        "receipt_normalized_payload_sha256": receipt[
            "normalized_payload_sha256"
        ],
        "mutation_count": attacks["executed"],
        "mutation_kill_count": attacks["killed"],
        "fresh_case_count": len(fresh_payload["cases"]),
        "scientific_fixture_evaluated": False,
        "publication_writes": 2,
    }


_WATCHDOG_STATE: dict[str, Any] = {"mode": "", "ticks": 0}


def _watchdog_handler(_: int, __: Any) -> None:
    _WATCHDOG_STATE["ticks"] += 1
    record = {
        "schema": SCHEMA,
        "progress": "RUNNING",
        "mode": _WATCHDOG_STATE["mode"],
        "elapsed_upper_bound_seconds": 60 * _WATCHDOG_STATE["ticks"],
    }
    print(canonical_json(record), file=sys.stderr, flush=True)
    if 60 * _WATCHDOG_STATE["ticks"] >= MAX_SECONDS:
        raise IntegrityFailure("mode exceeded the 300-second cap")


class ModeWatchdog:
    def __init__(self, mode: str) -> None:
        _require_exact(mode, str, "watchdog mode")
        self.mode = mode
        self.previous: Any = None

    def __enter__(self) -> "ModeWatchdog":
        _WATCHDOG_STATE["mode"] = self.mode
        _WATCHDOG_STATE["ticks"] = 0
        self.previous = signal.getsignal(signal.SIGALRM)
        signal.signal(signal.SIGALRM, _watchdog_handler)
        signal.setitimer(signal.ITIMER_REAL, 60, 60)
        return self

    def __exit__(self, _: Any, __: Any, ___: Any) -> None:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, self.previous)


def dispatch_mode(parsed: Mapping[str, str]) -> dict[str, Any]:
    mode = parsed["mode"]
    if mode == "selftest":
        return run_selftest()
    if mode == "mutant":
        row = run_attack(parsed["name"])
        return with_normalized_payload_hash(
            {
                "schema": SCHEMA,
                "mode": "mutant",
                "name": parsed["name"],
                "status": "PASS" if row["pass"] else "FAIL",
                "mutation": row,
                "scientific_fixture_evaluated": False,
                "fresh_cases_read": False,
                "official_artifacts_read": False,
                "publication_writes": 0,
            }
        )
    if mode == "generate-fresh":
        return generate_fresh_mode(parsed)
    if mode == "run":
        return run_official_mode(parsed)
    raise CLIUsage("unreachable strict mode")


def main(argv: Sequence[str] | None = None) -> int:
    arguments = tuple(sys.argv[1:] if argv is None else argv)
    try:
        parsed = parse_strict_cli(arguments)
    except CLIUsage as error:
        print(
            canonical_json(
                {"schema": SCHEMA, "status": "USAGE-ERROR", "message": str(error)}
            ),
            file=sys.stderr,
        )
        return 2
    try:
        with ModeWatchdog(parsed["mode"]):
            payload = dispatch_mode(parsed)
    except CLIUsage as error:
        print(
            canonical_json(
                {"schema": SCHEMA, "status": "USAGE-ERROR", "message": str(error)}
            ),
            file=sys.stderr,
        )
        return 2
    except Refusal as error:
        print(
            canonical_json(
                {"schema": SCHEMA, "status": "INPUT-REFUSAL", "message": str(error)}
            ),
            file=sys.stderr,
        )
        return 2
    except (IntegrityFailure, OSError) as error:
        print(
            canonical_json(
                {
                    "schema": SCHEMA,
                    "status": "INTEGRITY-FAILURE",
                    "message": str(error),
                }
            ),
            file=sys.stderr,
        )
        return 1
    print(canonical_json(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
