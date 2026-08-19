#!/usr/bin/env python3
"""Exact Stage-A evaluator for the Paper 13 ONE-GAMMA construction.

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
from dataclasses import FrozenInstanceError, dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


SCHEMA = "p13-gamma-exact-v1"
PIN_SHA256 = "4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35"
RUNBOOK_SHA256 = "5629dd083da923e216143c249ce0246da3238ddb9475bd6d67954ce0aa8aac58"
PREDECESSOR_SHA256 = "06d171a3eea8109e177e2dfa3cb5536fe3785043e676f735c36e91d03834cb51"
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
FRESH_DOMAIN = b"P13-FRESH-v1"
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
                decl.port.name,
                decl.port.child.name,
                decl.port.parent0.to_data(),
                decl.port.parent1.to_data(),
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
        body: Any = arrow.occurrence.to_data() if arrow.occurrence is not None else None
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


def _generator_map(law: GammaLaw, arrow: Arrow) -> LinearMap:
    if arrow.kind != "GENERATOR" or type(arrow.occurrence) is not Occurrence:
        raise Refusal("generator map received a malformed arrow")
    occurrence = arrow.occurrence
    entries: dict[tuple[int, int], Fraction] = {}
    for column, source_state in enumerate(arrow.source.catalogue):
        source_matter = matter_dict(source_state)
        source_sectors = sector_dict(source_state)
        input_bit = source_matter[occurrence.matter_role]
        for output_bit in (0, 1):
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
        "derivative_sign_formula": "-8*g*(1-g^2)/(1+g^2)^3<0",
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
        sector = sector_dict(target)[control["port"]]
        forgotten = context_forget(
            target.context, rotate.source.ports[0].port.child.name
        )
        changed.append(
            {
                "sector": sector,
                "probability": probability,
                "source_role_count": len(source.context.roles),
                "target_role_count": len(target.context.roles),
                "source_cell_count": len(source.context.cells),
                "target_cell_count": len(target.context.cells),
                "inverse_merge_exact": context_semantic_key(forgotten)
                == context_semantic_key(source.context),
                "configuration_nonisomorphic": (
                    len(source.context.roles), len(source.context.cells)
                )
                != (len(target.context.roles), len(target.context.cells)),
                "target_context_hash": canonical_hash(context_semantic_key(target.context)),
            }
        )
    return {
        "branches": tuple(changed),
        "all_inverse_merge": all(row["inverse_merge_exact"] for row in changed),
        "all_support_changed": all(
            row["configuration_nonisomorphic"] for row in changed
        ),
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


def measure_totality_certificate(law: GammaLaw) -> dict[str, Any]:
    coherent = build_coherent_control("total_")
    record = build_record_control("total_record_")
    reciprocal = build_reciprocal_control("total_rsp_")
    arrows = list(generator_leaves(coherent["two_pairs"]))
    arrows.append(record["writer"])
    for letter in record["letters"].values():
        arrows.extend(generator_leaves(letter))
    arrows.extend(generator_leaves(reciprocal["reader"]))
    rows: list[dict[str, Any]] = []
    for arrow in arrows:
        linear_map = evaluate_arrow(law, arrow)
        isometry, residual = check_isometry(linear_map)
        if type(arrow.occurrence) is not Occurrence:
            raise IntegrityFailure("totality battery contains a nongenerator")
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


@dataclass(frozen=True, slots=True)
class SourceGroupoidWitness:
    role_map: tuple[tuple[str, str], ...]
    matter_map: tuple[tuple[str, str], ...]
    port_map: tuple[tuple[str, str], ...]
    occurrence_map: tuple[tuple[str, str], ...]
    seal: bool = True

    def __post_init__(self) -> None:
        for label, rows in (
            ("role", self.role_map),
            ("matter", self.matter_map),
            ("port", self.port_map),
            ("occurrence", self.occurrence_map),
        ):
            _require_exact_tuple(rows, f"groupoid {label} map")
            for row in rows:
                _require_exact_tuple(row, f"groupoid {label} row")
                if len(row) != 2 or type(row[0]) is not str or type(row[1]) is not str:
                    raise Refusal(f"malformed groupoid {label} row")
            if len({row[0] for row in rows}) != len(rows) or len(
                {row[1] for row in rows}
            ) != len(rows):
                raise Refusal(f"groupoid {label} map is not injective")
        _require_exact(self.seal, bool, "groupoid witness seal")
        if not self.seal:
            raise Refusal("source-groupoid witness is unsealed")

    def to_data(self) -> dict[str, Any]:
        return {
            "type": "SourceGroupoidWitness",
            "role_map": self.role_map,
            "matter_map": self.matter_map,
            "port_map": self.port_map,
            "occurrence_map": self.occurrence_map,
            "seal": self.seal,
        }


def _rename(mapping: tuple[tuple[str, str], ...], value: str) -> str:
    return dict(mapping).get(value, value)


def inverse_witness(witness: SourceGroupoidWitness) -> SourceGroupoidWitness:
    _require_exact(witness, SourceGroupoidWitness, "groupoid witness")
    return SourceGroupoidWitness(
        tuple((right, left) for left, right in witness.role_map),
        tuple((right, left) for left, right in witness.matter_map),
        tuple((right, left) for left, right in witness.port_map),
        tuple((right, left) for left, right in witness.occurrence_map),
    )


def compose_witnesses(
    first: SourceGroupoidWitness, second: SourceGroupoidWitness
) -> SourceGroupoidWitness:
    _require_exact(first, SourceGroupoidWitness, "first groupoid witness")
    _require_exact(second, SourceGroupoidWitness, "second groupoid witness")

    def compose_rows(
        left: tuple[tuple[str, str], ...], right: tuple[tuple[str, str], ...]
    ) -> tuple[tuple[str, str], ...]:
        right_map = dict(right)
        return tuple((source, right_map.get(middle, middle)) for source, middle in left)

    return SourceGroupoidWitness(
        compose_rows(first.role_map, second.role_map),
        compose_rows(first.matter_map, second.matter_map),
        compose_rows(first.port_map, second.port_map),
        compose_rows(first.occurrence_map, second.occurrence_map),
    )


def relabel_formula(formula: Formula, witness: SourceGroupoidWitness) -> Formula:
    roles = tuple(_rename(witness.role_map, role) for role in formula.roles)
    return Formula(roles, formula.table)


def relabel_context(context: Context, witness: SourceGroupoidWitness) -> Context:
    roles = tuple(
        Role(_rename(witness.role_map, role.name), role.kind) for role in context.roles
    )
    cells = tuple(
        tuple(_rename(witness.role_map, name) for name in cell)
        for cell in context.cells
    )
    return Context(roles, cells, context.neutral_label)


def relabel_port(port: Port, witness: SourceGroupoidWitness) -> Port:
    return Port(
        _rename(witness.port_map, port.name),
        Role(_rename(witness.role_map, port.child.name), port.child.kind),
        relabel_formula(port.parent0, witness),
        relabel_formula(port.parent1, witness),
    )


def relabel_boundary(boundary: Boundary, witness: SourceGroupoidWitness) -> Boundary:
    _require_exact(boundary, Boundary, "relabelled boundary")
    _require_exact(witness, SourceGroupoidWitness, "groupoid witness")
    if boundary.kind == "UNIT":
        return unit_boundary()
    if boundary.kind == "TENSOR":
        if type(boundary.left) is not Boundary or type(boundary.right) is not Boundary:
            raise Refusal("tensor boundary children are malformed")
        return tensor_boundary(
            relabel_boundary(boundary.left, witness),
            relabel_boundary(boundary.right, witness),
        )
    return atomic_boundary(
        tuple(_rename(witness.matter_map, name) for name in boundary.matter_roles),
        relabel_context(boundary.base, witness),
        tuple(
            PortDecl(relabel_port(decl.port, witness), decl.mode)
            for decl in boundary.ports
        ),
        neutral_label=boundary.neutral_label,
        presentation_status_order=boundary.presentation_status_order,
    )


def relabel_occurrence(
    occurrence: Occurrence, witness: SourceGroupoidWitness
) -> Occurrence:
    return Occurrence(
        _rename(witness.occurrence_map, occurrence.occurrence_id),
        _rename(witness.matter_map, occurrence.matter_role),
        _rename(witness.port_map, occurrence.port_name),
        relabel_formula(occurrence.query, witness),
        occurrence.target_mode,
        occurrence.seal,
    )


def relabel_arrow(arrow: Arrow, witness: SourceGroupoidWitness) -> Arrow:
    _require_exact(arrow, Arrow, "relabelled arrow")
    _require_exact(witness, SourceGroupoidWitness, "groupoid witness")
    if arrow.kind == "IDENTITY":
        return identity_arrow(relabel_boundary(arrow.source, witness))
    if arrow.kind == "GENERATOR":
        if type(arrow.occurrence) is not Occurrence:
            raise Refusal("generator occurrence is malformed")
        return generator_arrow(
            relabel_boundary(arrow.source, witness),
            relabel_occurrence(arrow.occurrence, witness),
        )
    if arrow.kind == "COMPOSE":
        first, second = arrow.children
        return compose_arrows(
            relabel_arrow(first, witness), relabel_arrow(second, witness)
        )
    if arrow.kind == "TENSOR":
        left, right = arrow.children
        return tensor_arrow(
            relabel_arrow(left, witness), relabel_arrow(right, witness)
        )
    if arrow.kind == "SYMMETRY":
        left, right = arrow.objects
        return symmetry_arrow(
            relabel_boundary(left, witness), relabel_boundary(right, witness)
        )
    if arrow.kind in ("ASSOCIATOR", "ASSOCIATOR_INV"):
        a, b, c = arrow.objects
        return associator_arrow(
            relabel_boundary(a, witness),
            relabel_boundary(b, witness),
            relabel_boundary(c, witness),
            inverse=arrow.kind == "ASSOCIATOR_INV",
        )
    if "UNITOR" in arrow.kind:
        (obj,) = arrow.objects
        return unitor_arrow(
            relabel_boundary(obj, witness),
            "LEFT" if arrow.kind.startswith("LEFT") else "RIGHT",
            inverse=arrow.kind.endswith("_INV"),
        )
    raise Refusal("unreachable relabelled arrow branch")


def relabel_configuration(
    source_boundary: Boundary,
    target_boundary: Boundary,
    configuration: Configuration,
    witness: SourceGroupoidWitness,
) -> Configuration:
    validate_configuration(source_boundary, configuration)
    return configuration_from_assignments(
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


def covariance_residual(
    law: GammaLaw, arrow: Arrow, witness: SourceGroupoidWitness
) -> tuple[Fraction, dict[str, Any]]:
    transformed_arrow = relabel_arrow(arrow, witness)
    original = evaluate_arrow(law, arrow)
    transformed = evaluate_arrow(law, transformed_arrow)
    transformed_source_lookup = _configuration_index(transformed_arrow.source)
    transformed_target_lookup = _configuration_index(transformed_arrow.target)
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
            original_coefficient = map_coefficient(
                original, target_row, source_column
            )
            transformed_coefficient = map_coefficient(
                transformed, mapped_row, mapped_column
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
    }


def measure_groupoid_covariance(law: GammaLaw) -> dict[str, Any]:
    model = build_coherent_control("cov_")
    arrow = model["two_pairs"]
    occurrence_ids: list[str] = []

    def collect(current: Arrow) -> None:
        if current.occurrence is not None:
            occurrence_ids.append(current.occurrence.occurrence_id)
        for child in current.children:
            collect(child)

    collect(arrow)
    first = SourceGroupoidWitness(
        (
            ("cov_L_record", "renamed_R"),
            ("cov_N", "renamed_child"),
        ),
        (("cov_c", "renamed_matter"),),
        (("cov_p", "renamed_port"),),
        tuple((name, f"renamed_occ_{index}") for index, name in enumerate(occurrence_ids)),
    )
    second = SourceGroupoidWitness(
        (("renamed_R", "twice_R"), ("renamed_child", "twice_child")),
        (("renamed_matter", "twice_matter"),),
        (("renamed_port", "twice_port"),),
        tuple(
            (f"renamed_occ_{index}", f"twice_occ_{index}")
            for index in range(len(occurrence_ids))
        ),
    )
    identity = SourceGroupoidWitness((), (), (), ())
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
    return {
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
        "witnesses": {
            "identity": identity,
            "nontrivial": first,
            "inverse": inverse,
            "composite": composed,
            "second": second,
        },
        "all_exact": all(
            (
                identity_residual == 0,
                first_residual == 0,
                composed_residual == 0,
                identity_evidence["endpoint_probability_residual"] == 0,
                first_evidence["endpoint_probability_residual"] == 0,
                composed_evidence["endpoint_probability_residual"] == 0,
                roundtrip,
                sequential,
            )
        ),
    }


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
    ContinuationGrammar,
    MatchingPresentation,
    SourceGroupoidWitness,
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
    elif type(value) is SourceGroupoidWitness:
        _require_reconstruction_equal(
            value,
            SourceGroupoidWitness(
                value.role_map,
                value.matter_map,
                value.port_map,
                value.occurrence_map,
                value.seal,
            ),
            "source-groupoid witness",
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
    return GammaLaw(Fraction(1, 2), primitive)


def _law_primitive_attacks(identifier: str) -> dict[str, Any]:
    baseline_law = GammaLaw(Fraction(1, 2))
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
        occurrence = Occurrence(
            "illegal-old-port",
            control["source_role"],
            control["record_port"],
            formula_constant(False),
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


def _groupoid_attacks(identifier: str) -> dict[str, Any]:
    law = GammaLaw(Fraction(1, 2))
    baseline = measure_groupoid_covariance(law)
    model = build_coherent_control("gmut_")
    arrow = model["first_pair"]
    if identifier == "RELABEL-RAW-NAME":
        witness = SourceGroupoidWitness(
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
        evidence = evidence | {"residual": residual, "baseline": baseline["all_exact"]}
    elif identifier == "RELABEL-ORIENTATION":
        witness = SourceGroupoidWitness(
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
        "CONTROL-COVARIANT" if passed else "P13-REFERENT-PRESENTATION-ONLY",
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
        and measurements["static_scan"]["clean"],
        "referent": measurements["referent_census"]["all_exact"]
        and source_identity["inessential_formula_equal"],
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
        and full_target["all_full"],
        "source_sufficiency": source_identity["equal_key_equal_profile"]
        and source_identity["distinct_filling_distinct_key"]
        and source_identity["neutral_label_and_status_order_invariant"],
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
        "variable_carrier": bool(support["branches"]),
        "support_change": support["all_inverse_merge"]
        and support["all_support_changed"],
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
        measurements["scope_valid"] and measurements["static_scan"]["clean"],
        measurements["referent_census"]["all_exact"]
        and measurements["source_identity"]["inessential_formula_equal"],
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
        and measurements["full_target"]["all_full"],
        measurements["source_identity"]["equal_key_equal_profile"]
        and measurements["source_identity"]["distinct_filling_distinct_key"]
        and measurements["source_identity"]["neutral_label_and_status_order_invariant"],
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
        bool(measurements["support_change"]["branches"]),
        measurements["support_change"]["all_inverse_merge"]
        and measurements["support_change"]["all_support_changed"],
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
        "measurement_programme": MEASUREMENT_PROGRAMME,
    }
    validate_scope_surface(measurements["scope_coordinates"], measurements["scope_walls"])
    measurements["boolean_quotient"] = measure_boolean_quotient()
    measurements["source_identity"] = measure_source_identity(law)
    measurements["groupoid"] = measure_groupoid_covariance(law)
    measurements["full_target"] = measure_full_target_retyping(law)
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
        ],
        "groupoid_transport_exact": measurements["groupoid"]["all_exact"]
        and measurements["groupoid"]["cache_hits"] == 0
        and not measurements["groupoid"]["cache_implementation_present"],
    }
    measurements["referent_census"]["all_exact"] = all(
        measurements["referent_census"].values()
    )
    measurements["category"] = measure_category_laws(law)
    measurements["coherent"] = measure_coherent_controls(law)
    measurements["totality"] = measure_totality_certificate(law)
    measurements["support_change"] = measure_support_change(law)
    measurements["reciprocal"] = measure_reciprocal_response(law)
    measurements["division"] = measure_record_division(law)
    measurements["native_nondivision"] = measure_native_nondivision(law)
    measurements["blind_family"] = measure_blind_family(law)
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
GROUPID_ATTACKS = ("RELABEL-RAW-NAME", "RELABEL-ORIENTATION")
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
)


def run_attack(
    identifier: str, measurements: Mapping[str, Any] | None = None
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
        return _groupoid_attacks(identifier)
    raise Refusal("unreachable mutant dispatcher branch")


def run_all_attacks(measurements: Mapping[str, Any]) -> dict[str, Any]:
    rows = {identifier: run_attack(identifier, measurements) for identifier in MUTANT_IDS}
    return {
        "registered": len(MUTANT_IDS),
        "executed": len(rows),
        "killed": sum(int(row["pass"]) for row in rows.values()),
        "all_pass": all(row["pass"] for row in rows.values()),
        "rows": rows,
    }


ANCHOR_SPECS = (
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
)
STAGE_A_TASK_PATHS = (
    "v16/code/p13_gamma_exact.py",
    "v16/note-paper13-gamma-source-freeze.md",
)
STAGE_B_PUBLICATION_PATHS = (
    "v16/code/p13_gamma_fresh_cases.json",
    "v16/code/p13_gamma_output.txt",
    "v16/code/p13_gamma_receipt.json",
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
    if source_payload is None:
        source_payload = source_path().read_bytes()
    _require_exact(source_payload, bytes, "evaluator source payload")
    own = authenticate_payload(source_payload, source_sha256, "p13 evaluator source")
    reads.append(
        {
            "open_index": start_index,
            "path": "v16/code/p13_gamma_exact.py",
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
        "schema": "p13-gamma-fresh-v1",
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
    if logical_path not in STAGE_B_PUBLICATION_PATHS:
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
    record = build_record_control("closure_")
    matching = MatchingPresentation(
        3, (0, 2, 1), (0, 1), "EXPOSED-CONTROL"
    )
    witness = SourceGroupoidWitness((), (), (), ())
    nodes = (
        formula_constant(False),
        boundary.base.roles[0],
        boundary.base,
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
        record["grammar"],
        matching,
        witness,
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
            "path": "v16/code/p13_gamma_exact.py",
            "expected_sha256": "0" * 64,
            "observed_sha256": "0" * 64,
            "consumption_key": "authoritative-evaluator-and-generator",
            "consumed": True,
        },
        {
            "open_index": 2,
            "path": "RUNBOOK.md",
            "expected_sha256": RUNBOOK_SHA256,
            "observed_sha256": RUNBOOK_SHA256,
            "consumption_key": "process-integrity-contract",
            "consumed": True,
        },
    )
    shifted_rows = tuple(
        dict(row) | {"open_index": row["open_index"] + 1}
        for row in semantic_rows
    )
    official_rows = (
        {
            "open_index": 1,
            "path": "v16/code/p13_gamma_fresh_cases.json",
            "expected_sha256": "1" * 64,
            "observed_sha256": "1" * 64,
            "consumption_key": "post-source-fresh-confirmation-input",
            "consumed": True,
        },
    ) + shifted_rows
    manifest_invariant = authentication_manifest_hash(
        semantic_rows
    ) == authentication_manifest_hash(shifted_rows)
    return {
        "generator_open_order": tuple(row["path"] for row in semantic_rows),
        "official_open_order": tuple(row["path"] for row in official_rows),
        "official_open_indices": tuple(row["open_index"] for row in official_rows),
        "fresh_precedes_source_in_official_run": official_rows[0]["path"]
        == "v16/code/p13_gamma_fresh_cases.json"
        and official_rows[1]["path"] == "v16/code/p13_gamma_exact.py",
        "anchor_manifest_ignores_only_open_position": manifest_invariant,
        "all_consumed": all(row["consumed"] for row in official_rows),
        "all_exact": manifest_invariant
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
    denial = FixtureImportDenial()
    sys.meta_path.insert(0, denial)
    try:
        measurements = measure_scientific_core(source_text)
        attacks = run_all_attacks(measurements)
    finally:
        sys.meta_path.remove(denial)
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
                "path": "v16/code/p13_gamma_exact.py",
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
    checks = (
        _selftest_check(
            "AST-AND-STATIC-SOURCE-CLEAN",
            measurements["static_scan"]["clean"],
            measurements["static_scan"],
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
            ],
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
            "SOURCE-GROUPOID-COVARIANCE",
            measurements["groupoid"]["all_exact"],
            measurements["groupoid"],
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
            and measurements["support_change"]["all_support_changed"],
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
            "OUTCOME-LADDER-CAP-AND-INDEPENDENT-COMPARATOR",
            measurements["strict_primary"] == ELIGIBLE_CAP
            and measurements["outcome_comparator"],
            {
                "strict_primary": measurements["strict_primary"],
                "eligible_cap": ELIGIBLE_CAP,
                "independent_index": independent_outcome_index(measurements),
                "render_trace": measurements["outcome_render_trace"],
            },
        ),
        _selftest_check(
            "MUTANT-REGISTRY-UNIQUE-AND-COMPLETE",
            len(MUTANT_IDS) == len(set(MUTANT_IDS))
            and attacks["registered"] == len(MUTANT_IDS)
            and attacks["executed"] == len(MUTANT_IDS),
            {
                "names": MUTANT_IDS,
                "registry_sha256": canonical_hash(MUTANT_IDS),
                "registered": attacks["registered"],
                "executed": attacks["executed"],
            },
        ),
        _selftest_check(
            "ALL-REGISTERED-MUTATIONS-KILLED",
            attacks["all_pass"] and attacks["killed"] == len(MUTANT_IDS),
            attacks,
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
            STAGE_A_TASK_PATHS
            == (
                "v16/code/p13_gamma_exact.py",
                "v16/note-paper13-gamma-source-freeze.md",
            )
            and STAGE_B_PUBLICATION_PATHS
            == (
                "v16/code/p13_gamma_fresh_cases.json",
                "v16/code/p13_gamma_output.txt",
                "v16/code/p13_gamma_receipt.json",
            ),
            {
                "stage_a_task_paths": STAGE_A_TASK_PATHS,
                "stage_b_publication_paths": STAGE_B_PUBLICATION_PATHS,
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
        "scientific_fixture_evaluated": False,
        "fresh_cases_read": False,
        "official_artifacts_read": False,
        "publication_writes": 0,
    }
    return with_normalized_payload_hash(base_payload)


CLAIM_FALSIFIERS = {
    "specification": ("FLOAT-OR-EXPECTED-TABLE", "ANCHOR-CORRUPTION"),
    "referent": ("RELABEL-RAW-NAME", "RELABEL-ORIENTATION"),
    "complete_gamma": ("RESET-ONE", "FORGED-COMPOSE-TARGET"),
    "source_sufficiency": ("SOURCE-KEY-OMITS-FILLING", "POSTINIT-LAW-IDENTITY"),
    "anti_wrapper": ("WRAPPER-GAMMA", "OCCURRENCE-SEVER"),
    "shadow_weld": ("CACHED-G-OR-SHADOW", "PHASE-REFLECTION-MUTATION"),
    "variable_carrier": ("META-CATALOGUE-AS-SUPPORT", "MOVE-DOWNSTREAM"),
    "support_change": ("SUPPORT-FILTERED-TARGET", "FULL-TARGET-RETYPE"),
    "reciprocal": ("DELAYED-READER-SEVER", "QUERY-FORMULA-MUTATION"),
    "division": ("RESET-WRITER-CHAIN", "HIDDEN-ERASER"),
    "native_nondivision": (
        "HISTORY-PASSED-OFF-AS-NATIVE-K",
        "NONDIVISION-AS-STATE-DEFECT",
    ),
    "blind_class": ("LEAKED-INCIDENCE-BIT", "CONSTANT-BLIND-TOKEN"),
}
CLAIM_INPUT_PATHS = {
    "specification": ("static_scan", "scope_coordinates", "scope_walls"),
    "referent": (
        "referent_census",
        "boolean_quotient",
        "public_language",
        "full_target",
        "groupoid",
        "source_identity",
    ),
    "complete_gamma": ("category", "coherent", "full_target", "totality"),
    "source_sufficiency": ("source_identity", "representative_application"),
    "anti_wrapper": ("lineage", "shadow_lineages"),
    "shadow_weld": ("coherent", "native_nondivision"),
    "variable_carrier": ("support_change",),
    "support_change": ("support_change",),
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
        "schema": "p13-gamma-output-v1",
        "strict_primary": measurements["strict_primary"],
        "outcome_render_trace": measurements["outcome_render_trace"],
        "eligible_cap": ELIGIBLE_CAP,
        "future_rungs_ineligible": OUTCOME_LADDER[13:],
        "gates": measurements["gates"],
        "orthogonal_coordinates": measurements["scope_coordinates"],
        "scope_walls": measurements["scope_walls"],
        "native_nondivision_sentence": NATIVE_NONDIVISION_SENTENCE,
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
        "pin_sha256": PIN_SHA256,
        "runbook_sha256": RUNBOOK_SHA256,
        "predecessor_sha256": PREDECESSOR_SHA256,
        "paper12_sha256": PAPER12_SHA256,
        "paper12_adjudication_sha256": PAPER12_ADJUDICATION_SHA256,
        "paper12_evaluator_sha256": PAPER12_EVALUATOR_SHA256,
        "paper12_receipt_sha256": PAPER12_RECEIPT_SHA256,
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
        "publication_whitelist": STAGE_B_PUBLICATION_PATHS,
    }
    manifest = build_seal_manifest(sealed)
    receipt = with_normalized_payload_hash(
        {
            "schema": "p13-gamma-receipt-v1",
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
        destination, "v16/code/p13_gamma_fresh_cases.json"
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
        fresh_path, "v16/code/p13_gamma_fresh_cases.json"
    )
    _validate_publication_role(output_path, "v16/code/p13_gamma_output.txt")
    _validate_publication_role(receipt_path, "v16/code/p13_gamma_receipt.json")
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
            "path": "v16/code/p13_gamma_fresh_cases.json",
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
