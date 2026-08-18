#!/usr/bin/env python3
"""Generic exact algebraic-variety instrument for the v16 JCV unit.

This freeze knows public calibration models only.  It deliberately contains no
physical JCV fixture, expected physical dimension, witness, or verdict.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import os
import re
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


PIN_COMMIT = "a51f9493e5be78f090aa7d387afa9a1eecfc6a4c"
BASE_COMMIT = "7adc7cbf4897b303077bbfba4e11a7268274a10f"

SOURCE_ANCHORS = {
    "v16/note-jcv-pin.md": "4268055286efb5ff0a9790826608c4eb3927ae4e2e87fe66383194cce0059841",
    "v16/code/jcv_public_calibrations.json": "d16d7487c9110aa510c4b61108779d0529aa2a339088ea748eecc5379f7f00f1",
    "v16/paper-01-joint-relational-history-law.md": "98489edb6a83919199c11b14b92c423965d1a08ad7652a1c1915d5402f9e6003",
    "v16/note-jrh-delta-adjudication.md": "cc4f4d11abd77287f645dfd34af438630629c1bfcb2a52212bfd90fd48c0660c",
    "v16/note-jrh-terminal-verification.md": "223e12ccca014947b6fe8a0dcbd584c72ff0ff83a81f630a14a89ff512047824",
    "v15/paper-43-contract.md": "0c8d1a687b148a6cc5a0c1bfc199d2caa30db85f1e9ce4bbcf50fbe91ffe057f",
    "v13/paper-coc-cocycle.md": "44c50aa1faf956b2e814c82a35d0aac4427eaa8b83061c6a6772d7391681cb82",
    "v12/paper1-composition-defect.md": "81bdab5673fb67b63cd10c08fbb80870f8aa01088047718c5b4bf447e1669128",
    "v14/code/era_template.py": "d04a3eb58fbcfe3d093b98126ca23c1610a9cc7cec96c9b9097eed515516f2b9",
}

RESERVED_PHYSICAL_PATHS = (
    "v16/code/jcv_fixture.json",
    "v16/code/jcv_score.py",
    "v16/code/jcv_output.txt",
    "v16/code/jcv_receipt.json",
    "v16/paper-02-joint-comparison-fixed-point.md",
)

MUTANT_GATES = {
    "ANCHOR_CORRUPT": "G-ANCHORS",
    "RESERVED_SMUGGLE": "G-CHRONOLOGY",
    "DROP_EQUATION": "G-CAL-EMPTY",
    "S_POLY_SKIP": "G-GROEBNER",
    "DIMENSION_SHIFT": "G-CAL-POSDIM",
    "SIGN_SECTOR_COLLAPSE": "G-CAL-GAUGE",
    "SATURATION_FAKE": "G-CAL-POSDIM",
    "READSET_HIDE": "G-READSET",
    "TRANSCRIPT_CONTRADICTION": "G-TRANSCRIPT",
    "SEAL_ADD": "G-SEAL-CONTROLS",
    "SEAL_EDIT": "G-SEAL-CONTROLS",
}


def q(value: str | int) -> Fraction:
    return Fraction(str(value))


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def serial(value: Any) -> Any:
    if isinstance(value, Fraction):
        return qstr(value)
    if isinstance(value, Poly):
        return {
            "variables": list(value.variables),
            "terms": [[list(exp), qstr(coeff)] for exp, coeff in value.terms],
        }
    if isinstance(value, tuple):
        return [serial(x) for x in value]
    if isinstance(value, list):
        return [serial(x) for x in value]
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in sorted(value.items(), key=lambda item: str(item[0]))}
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


class SourceReader:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.reads: list[str] = []

    def read_bytes(self, relative: str) -> bytes:
        self.reads.append(relative)
        return (self.root / relative).read_bytes()

    def read_text(self, relative: str) -> str:
        return self.read_bytes(relative).decode("utf-8")


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


Exponent = tuple[int, ...]


@dataclass(frozen=True)
class Poly:
    variables: tuple[str, ...]
    terms: tuple[tuple[Exponent, Fraction], ...]

    @staticmethod
    def make(variables: Iterable[str], raw: dict[Exponent, Fraction]) -> "Poly":
        vars_tuple = tuple(variables)
        clean = {exp: coeff for exp, coeff in raw.items() if coeff != 0}
        for exp in clean:
            if len(exp) != len(vars_tuple) or any(power < 0 for power in exp):
                raise ValueError("invalid exponent")
        return Poly(vars_tuple, tuple(sorted(clean.items(), reverse=True)))

    @staticmethod
    def zero(variables: Iterable[str]) -> "Poly":
        return Poly.make(tuple(variables), {})

    @staticmethod
    def one(variables: Iterable[str]) -> "Poly":
        vars_tuple = tuple(variables)
        return Poly.make(vars_tuple, {(0,) * len(vars_tuple): Fraction(1)})

    def as_dict(self) -> dict[Exponent, Fraction]:
        return dict(self.terms)

    def is_zero(self) -> bool:
        return not self.terms

    def leading(self) -> tuple[Exponent, Fraction]:
        if self.is_zero():
            raise ValueError("zero polynomial has no leading term")
        return self.terms[0]

    def __add__(self, other: "Poly") -> "Poly":
        self._same(other)
        result = self.as_dict()
        for exp, coeff in other.terms:
            result[exp] = result.get(exp, Fraction(0)) + coeff
        return Poly.make(self.variables, result)

    def __neg__(self) -> "Poly":
        return Poly.make(self.variables, {exp: -coeff for exp, coeff in self.terms})

    def __sub__(self, other: "Poly") -> "Poly":
        return self + (-other)

    def __mul__(self, other: "Poly") -> "Poly":
        self._same(other)
        result: dict[Exponent, Fraction] = {}
        for exp_a, coeff_a in self.terms:
            for exp_b, coeff_b in other.terms:
                exp = tuple(a + b for a, b in zip(exp_a, exp_b))
                result[exp] = result.get(exp, Fraction(0)) + coeff_a * coeff_b
        return Poly.make(self.variables, result)

    def scale(self, scalar: Fraction) -> "Poly":
        return Poly.make(self.variables, {exp: scalar * coeff for exp, coeff in self.terms})

    def monomial_mul(self, exp_delta: Exponent, scalar: Fraction) -> "Poly":
        return Poly.make(
            self.variables,
            {tuple(a + b for a, b in zip(exp, exp_delta)): scalar * coeff for exp, coeff in self.terms},
        )

    def monic(self) -> "Poly":
        if self.is_zero():
            return self
        return self.scale(Fraction(1) / self.leading()[1])

    def _same(self, other: "Poly") -> None:
        if self.variables != other.variables:
            raise ValueError("polynomial rings differ")


def divides(left: Exponent, right: Exponent) -> bool:
    return all(a <= b for a, b in zip(left, right))


def exp_sub(left: Exponent, right: Exponent) -> Exponent:
    if not divides(right, left):
        raise ValueError("negative monomial quotient")
    return tuple(a - b for a, b in zip(left, right))


def exp_lcm(left: Exponent, right: Exponent) -> Exponent:
    return tuple(max(a, b) for a, b in zip(left, right))


def reduce_poly(poly: Poly, basis: Iterable[Poly]) -> Poly:
    reducers = [item for item in basis if not item.is_zero()]
    current = poly
    remainder = Poly.zero(poly.variables)
    while not current.is_zero():
        exp_f, coeff_f = current.leading()
        used = False
        for reducer in reducers:
            exp_g, coeff_g = reducer.leading()
            if divides(exp_g, exp_f):
                delta = exp_sub(exp_f, exp_g)
                current = current - reducer.monomial_mul(delta, coeff_f / coeff_g)
                used = True
                break
        if not used:
            lead = Poly.make(poly.variables, {exp_f: coeff_f})
            remainder = remainder + lead
            current = current - lead
    return remainder


def s_polynomial(left: Poly, right: Poly) -> Poly:
    exp_l, coeff_l = left.leading()
    exp_r, coeff_r = right.leading()
    common = exp_lcm(exp_l, exp_r)
    return left.monomial_mul(exp_sub(common, exp_l), Fraction(1) / coeff_l) - right.monomial_mul(
        exp_sub(common, exp_r), Fraction(1) / coeff_r
    )


def unique_polys(polys: Iterable[Poly]) -> list[Poly]:
    seen: set[tuple[tuple[Exponent, Fraction], ...]] = set()
    result = []
    for poly in polys:
        item = poly.monic()
        if item.is_zero() or item.terms in seen:
            continue
        seen.add(item.terms)
        result.append(item)
    return result


def groebner(generators: Iterable[Poly]) -> list[Poly]:
    basis = unique_polys(generators)
    pairs = [(i, j) for i in range(len(basis)) for j in range(i)]
    while pairs:
        i, j = pairs.pop(0)
        remainder = reduce_poly(s_polynomial(basis[i], basis[j]), basis)
        if not remainder.is_zero():
            remainder = remainder.monic()
            new_index = len(basis)
            pairs.extend((new_index, old) for old in range(new_index))
            basis.append(remainder)

    changed = True
    while changed:
        changed = False
        reduced: list[Poly] = []
        for index, item in enumerate(basis):
            others = basis[:index] + basis[index + 1 :]
            remainder = reduce_poly(item, others).monic()
            if not remainder.is_zero():
                reduced.append(remainder)
            if remainder.terms != item.terms:
                changed = True
        basis = unique_polys(reduced)

    minimal: list[Poly] = []
    for index, item in enumerate(basis):
        lead = item.leading()[0]
        if any(divides(other.leading()[0], lead) for j, other in enumerate(basis) if j != index):
            continue
        minimal.append(item)
    return sorted(unique_polys(minimal), key=lambda item: item.leading()[0], reverse=True)


def verify_groebner(generators: list[Poly], basis: list[Poly]) -> tuple[bool, dict[str, int]]:
    generator_failures = sum(not reduce_poly(item, basis).is_zero() for item in generators)
    s_failures = 0
    s_pairs = 0
    for i in range(len(basis)):
        for j in range(i):
            s_pairs += 1
            if not reduce_poly(s_polynomial(basis[i], basis[j]), basis).is_zero():
                s_failures += 1
    return (generator_failures == 0 and s_failures == 0, {
        "generators": len(generators),
        "generator_failures": generator_failures,
        "s_pairs": s_pairs,
        "s_failures": s_failures,
    })


def is_unit_ideal(basis: list[Poly]) -> bool:
    return any(len(item.terms) == 1 and item.terms[0][0] == (0,) * len(item.variables) for item in basis)


def ideal_dimension(basis: list[Poly], variable_count: int) -> int:
    if is_unit_ideal(basis):
        return -1
    if not basis:
        return variable_count
    supports = [{index for index, power in enumerate(item.leading()[0]) if power} for item in basis]
    if any(not support for support in supports):
        return -1
    for cover_size in range(variable_count + 1):
        for cover_tuple in itertools.combinations(range(variable_count), cover_size):
            cover = set(cover_tuple)
            if all(cover & support for support in supports):
                return variable_count - cover_size
    raise RuntimeError("monomial ideal dimension not found")


def polynomial_text(poly: Poly) -> str:
    if poly.is_zero():
        return "0"
    pieces: list[str] = []
    for position, (exp, coeff) in enumerate(poly.terms):
        factors = []
        for name, power in zip(poly.variables, exp):
            if power == 1:
                factors.append(name)
            elif power:
                factors.append(f"{name}^{power}")
        monomial = "*".join(factors)
        absolute = abs(coeff)
        if monomial and absolute == 1:
            body = monomial
        elif monomial:
            body = f"{qstr(absolute)}*{monomial}"
        else:
            body = qstr(absolute)
        sign = "-" if coeff < 0 else "+"
        if position == 0:
            pieces.append(body if coeff > 0 else f"-{body}")
        else:
            pieces.append(f" {sign} {body}")
    return "".join(pieces)


def poly_from_terms(terms: list[list[Any]], variables: tuple[str, ...]) -> Poly:
    index = {name: position for position, name in enumerate(variables)}
    raw: dict[Exponent, Fraction] = {}
    for coefficient, powers in terms:
        exp = [0] * len(variables)
        for name, power in powers.items():
            if name not in index or not isinstance(power, int) or power < 0:
                raise ValueError(f"invalid polynomial variable/power {name}:{power}")
            exp[index[name]] = power
        exp_tuple = tuple(exp)
        raw[exp_tuple] = raw.get(exp_tuple, Fraction(0)) + q(coefficient)
    return Poly.make(variables, raw)


def substitute_signs(poly: Poly, signs: dict[str, int], continuous: tuple[str, ...]) -> Poly:
    continuous_index = {name: position for position, name in enumerate(continuous)}
    raw: dict[Exponent, Fraction] = {}
    for exp, coeff in poly.terms:
        out_exp = [0] * len(continuous)
        out_coeff = coeff
        for name, power in zip(poly.variables, exp):
            if name in signs:
                out_coeff *= signs[name] ** power
            elif name in continuous_index:
                out_exp[continuous_index[name]] = power
            elif power:
                raise ValueError(f"unassigned variable {name}")
        out_tuple = tuple(out_exp)
        raw[out_tuple] = raw.get(out_tuple, Fraction(0)) + out_coeff
    return Poly.make(continuous, raw)


def lift_poly(poly: Poly, variables: tuple[str, ...]) -> Poly:
    if variables[: len(poly.variables)] != poly.variables:
        raise ValueError("lift requires prefix variables")
    extra = (0,) * (len(variables) - len(poly.variables))
    return Poly.make(variables, {exp + extra: coeff for exp, coeff in poly.terms})


def saturation_nonempty(generators: list[Poly], query: Poly) -> tuple[bool, int, list[str]]:
    aux_name = "__inverse"
    while aux_name in query.variables:
        aux_name += "_x"
    variables = query.variables + (aux_name,)
    lifted = [lift_poly(item, variables) for item in generators]
    query_lifted = lift_poly(query, variables)
    aux = Poly.make(variables, {(0,) * len(query.variables) + (1,): Fraction(1)})
    equations = lifted + [aux * query_lifted - Poly.one(variables)]
    basis = groebner(equations)
    return (not is_unit_ideal(basis), ideal_dimension(basis, len(variables)), [polynomial_text(item) for item in basis])


def validate_model_schema(model: dict[str, Any]) -> None:
    required = {"name", "continuous_variables", "sign_variables", "equations", "gauge_invariants", "queries", "expected"}
    if set(model) != required:
        raise ValueError(f"model keys differ for {model.get('name')}")
    variables = model["sign_variables"] + model["continuous_variables"]
    if len(set(variables)) != len(variables) or not variables:
        raise ValueError("variables must be unique and nonempty")
    for row in model["equations"] + model["gauge_invariants"] + model["queries"]:
        if "name" not in row or "terms" not in row:
            raise ValueError("polynomial row missing name/terms")


def solve_model(model: dict[str, Any], mutator: Mutator | None = None) -> dict[str, Any]:
    validate_model_schema(model)
    sign_variables = tuple(model["sign_variables"])
    continuous = tuple(model["continuous_variables"])
    all_variables = sign_variables + continuous
    equations = [poly_from_terms(row["terms"], all_variables) for row in model["equations"]]
    invariants = [(row["name"], poly_from_terms(row["terms"], all_variables)) for row in model["gauge_invariants"]]
    queries = [(row, poly_from_terms(row["terms"], all_variables)) for row in model["queries"]]

    assignments = [dict(zip(sign_variables, values)) for values in itertools.product((-1, 1), repeat=len(sign_variables))]
    if not assignments:
        assignments = [{}]
    sectors: dict[tuple[str, ...], list[dict[str, Any]]] = {}
    verification_totals = {"generators": 0, "generator_failures": 0, "s_pairs": 0, "s_failures": 0}

    for assignment in assignments:
        generators = [substitute_signs(item, assignment, continuous) for item in equations]
        if mutator and mutator.name == "DROP_EQUATION" and model["name"] == "EMPTY":
            generators = mutator.move("DROP_EQUATION", generators, generators[:1])
        basis = groebner(generators)
        if mutator and mutator.name == "S_POLY_SKIP" and model["name"] == "REDUCIBLE":
            basis = mutator.move("S_POLY_SKIP", basis, [])
        verified, verification = verify_groebner(generators, basis)
        for key in verification_totals:
            verification_totals[key] += verification[key]
        if not verified:
            raise GateFail("G-GROEBNER", f"{model['name']} basis verification failed", tuple(mutator.moves if mutator else ()))
        dimension = ideal_dimension(basis, len(continuous))
        if mutator and mutator.name == "DIMENSION_SHIFT" and model["name"] == "POSITIVE_DIMENSIONAL":
            dimension = mutator.move("DIMENSION_SHIFT", dimension, dimension + 1)

        invariant_values = []
        for _, invariant in invariants:
            reduced = substitute_signs(invariant, assignment, continuous)
            if any(any(exp) for exp, _ in reduced.terms):
                raise ValueError("gauge invariant depends on continuous variable")
            value = reduced.as_dict().get((0,) * len(continuous), Fraction(0))
            invariant_values.append(qstr(value))
        sector_key = tuple(invariant_values)
        if mutator and mutator.name == "SIGN_SECTOR_COLLAPSE" and model["name"] == "GAUGE_SECTOR" and sector_key == ("-1",):
            sector_key = tuple(mutator.move("SIGN_SECTOR_COLLAPSE", sector_key, ("1",)))

        query_rows = []
        for row, query in queries:
            reduced_query = substitute_signs(query, assignment, continuous)
            remainder = reduce_poly(reduced_query, basis)
            constant = None
            if all(not any(exp) for exp, _ in remainder.terms):
                constant = qstr(remainder.as_dict().get((0,) * len(continuous), Fraction(0)))
            saturation = None
            if row.get("nonzero_locus"):
                nonempty, sat_dimension, sat_basis = saturation_nonempty(generators, reduced_query)
                if mutator and mutator.name == "SATURATION_FAKE" and model["name"] == "POSITIVE_DIMENSIONAL" and row["name"] == "xy":
                    nonempty = mutator.move("SATURATION_FAKE", nonempty, not nonempty)
                saturation = {"nonempty": nonempty, "dimension": sat_dimension, "basis": sat_basis}
            query_rows.append({
                "name": row["name"],
                "remainder": polynomial_text(remainder),
                "constant": constant,
                "nonzero_locus": saturation,
            })

        row = {
            "assignment": {key: assignment[key] for key in sorted(assignment)},
            "empty": is_unit_ideal(basis),
            "dimension": dimension,
            "basis": [polynomial_text(item) for item in basis],
            "queries": query_rows,
        }
        sectors.setdefault(sector_key, []).append(row)

    sector_rows = []
    for key in sorted(sectors):
        rows = sectors[key]
        variants = sorted({canonical({"empty": row["empty"], "dimension": row["dimension"], "basis": row["basis"], "queries": row["queries"]}).decode("utf-8") for row in rows})
        representative = rows[0]
        sector_rows.append({
            "key": list(key),
            "assignment_count": len(rows),
            "solution_variants": len(variants),
            "empty": representative["empty"],
            "dimension": representative["dimension"],
            "basis": representative["basis"],
            "queries": representative["queries"],
        })

    return {
        "name": model["name"],
        "sign_assignment_count": len(assignments),
        "sector_count": len(sector_rows),
        "nonempty_sectors": sum(not row["empty"] for row in sector_rows),
        "sectors": sector_rows,
        "verification": verification_totals,
    }


def check_expected(model: dict[str, Any], result: dict[str, Any]) -> tuple[bool, str]:
    expected = model["expected"]
    nonempty = [row for row in result["sectors"] if not row["empty"]]
    observed_dimensions = sorted(row["dimension"] for row in nonempty)
    checks = [result["nonempty_sectors"] == expected["nonempty_sectors"], observed_dimensions == expected["dimensions"]]
    details = [f"nonempty={result['nonempty_sectors']}", f"dimensions={observed_dimensions}"]
    if "sector_keys" in expected:
        keys = sorted(row["key"] for row in nonempty)
        checks.append(keys == expected["sector_keys"])
        details.append(f"keys={keys}")
    query_rows = {query["name"]: query for sector in nonempty for query in sector["queries"]}
    for name, value in expected.get("query_constants", {}).items():
        checks.append(query_rows[name]["constant"] == value)
        details.append(f"{name}={query_rows[name]['constant']}")
    for name in expected.get("query_nonconstant", []):
        checks.append(query_rows[name]["constant"] is None)
        details.append(f"{name}=nonconstant:{query_rows[name]['remainder']}")
    for name in expected.get("nonzero_nonempty", []):
        checks.append(query_rows[name]["nonzero_locus"]["nonempty"] is True)
        details.append(f"{name}!=0:nonempty")
    for name in expected.get("nonzero_empty", []):
        checks.append(query_rows[name]["nonzero_locus"]["nonempty"] is False)
        details.append(f"{name}!=0:empty")
    return (all(checks), "; ".join(details))


def parser_contract(argv: list[str]) -> tuple[str, str | None]:
    if not argv:
        return ("plain", None)
    if argv == ["--selftest"]:
        return ("selftest", None)
    if len(argv) == 2 and argv[0] == "--mutant" and argv[1] in MUTANT_GATES:
        return ("mutant", argv[1])
    raise ValueError("usage: jcv_variety.py [--selftest | --mutant NAME]")


def artifact_paths(root: Path) -> tuple[Path, ...]:
    return (
        root / "v16/code/jcv_public_output.txt",
        root / "v16/code/jcv_public_receipt.json",
        root / "v16/note-jcv-solver-freeze.md",
    )


def snapshot(paths: Iterable[Path]) -> dict[str, str | None]:
    return {str(item): bytes_digest(item.read_bytes()) if item.exists() else None for item in paths}


def run_core(root: Path, mutant_name: str | None = None) -> tuple[Ledger, dict[str, Any], SourceReader, Mutator]:
    if mutant_name is not None and mutant_name not in MUTANT_GATES:
        raise ValueError(f"unknown mutant {mutant_name}")
    mutator = Mutator(mutant_name)
    ledger = Ledger(mutator)
    reader = SourceReader(root)

    observed = {relative: bytes_digest(reader.read_bytes(relative)) for relative in sorted(SOURCE_ANCHORS)}
    expected = dict(SOURCE_ANCHORS)
    if mutant_name == "ANCHOR_CORRUPT":
        first = sorted(observed)[0]
        changed = dict(observed)
        changed[first] = "0" * 64
        observed = mutator.move("ANCHOR_CORRUPT", observed, changed)
    ledger.gate("G-ANCHORS", observed == expected, f"matched {sum(observed.get(key) == value for key, value in expected.items())} of {len(expected)} frozen source hashes")

    reserved_present = [relative for relative in RESERVED_PHYSICAL_PATHS if (root / relative).exists()]
    if mutant_name == "RESERVED_SMUGGLE":
        reserved_present = mutator.move("RESERVED_SMUGGLE", reserved_present, [RESERVED_PHYSICAL_PATHS[0]])
    ledger.gate("G-CHRONOLOGY", not reserved_present, f"reserved physical paths present={reserved_present}")

    calibration_relative = "v16/code/jcv_public_calibrations.json"
    calibration = json.loads(reader.read_text(calibration_relative))
    schema_ok = calibration.get("schema") == "JCV-PUBLIC-CALIBRATIONS-v1" and isinstance(calibration.get("models"), list)
    if schema_ok:
        try:
            for model in calibration["models"]:
                validate_model_schema(model)
        except (KeyError, TypeError, ValueError):
            schema_ok = False
    ledger.gate("G-SCHEMA", schema_ok, f"public models={len(calibration.get('models', []))}")

    results = [solve_model(model, mutator) for model in calibration["models"]]
    by_name = {row["name"]: row for row in results}
    model_by_name = {row["name"]: row for row in calibration["models"]}

    verification = {
        key: sum(result["verification"][key] for result in results)
        for key in ("generators", "generator_failures", "s_pairs", "s_failures")
    }
    ledger.gate("G-GROEBNER", verification["generator_failures"] == 0 and verification["s_failures"] == 0, f"generator reductions={verification['generators']}; S-pairs={verification['s_pairs']}; failures={verification['generator_failures'] + verification['s_failures']}")

    calibration_gates = {
        "EMPTY": "G-CAL-EMPTY",
        "POINT": "G-CAL-POINT",
        "POSITIVE_DIMENSIONAL": "G-CAL-POSDIM",
        "REDUCIBLE": "G-CAL-REDUCIBLE",
        "GAUGE_SECTOR": "G-CAL-GAUGE",
    }
    for name, gate in calibration_gates.items():
        passed, evidence = check_expected(model_by_name[name], by_name[name])
        ledger.gate(gate, passed, evidence)

    pos_pass, pos_evidence = check_expected(model_by_name["POSITIVE_DIMENSIONAL"], by_name["POSITIVE_DIMENSIONAL"])
    red_pass, red_evidence = check_expected(model_by_name["REDUCIBLE"], by_name["REDUCIBLE"])
    ledger.gate("G-CAL-QUERY", pos_pass and red_pass, f"positive={pos_evidence}; reducible={red_evidence}")

    source_relative = "v16/code/jcv_variety.py"
    source_text = reader.read_text(source_relative)
    parsed = ast.parse(source_text)
    float_literals = [(node.lineno, node.value) for node in ast.walk(parsed) if isinstance(node, ast.Constant) and isinstance(node.value, float)]
    ledger.gate("G-EXACT", not float_literals, f"AST float literals={len(float_literals)}")

    declared_reads = set(SOURCE_ANCHORS) | {calibration_relative, source_relative}
    observed_reads = set(reader.reads)
    if mutant_name == "READSET_HIDE":
        observed_reads = set(mutator.move("READSET_HIDE", sorted(observed_reads), sorted(observed_reads)[:-1]))
    ledger.gate("G-READSET", observed_reads == declared_reads, f"declared={len(declared_reads)} observed={len(observed_reads)}")

    measurements = {
        "schema": calibration["schema"],
        "model_count": len(results),
        "models": results,
        "groebner_verification": verification,
        "reserved_paths_absent": not reserved_present,
        "anchor_count": len(SOURCE_ANCHORS),
        "pin_commit": PIN_COMMIT,
        "base_commit": BASE_COMMIT,
    }
    return ledger, measurements, reader, mutator


def render_note(measurements: dict[str, Any], gate_count: int, mutant_count: int) -> str:
    rows = []
    for model in measurements["models"]:
        dims = [sector["dimension"] for sector in model["sectors"] if not sector["empty"]]
        rows.append(f"| {model['name']} | {model['nonempty_sectors']} | {dims} |")
    table = "\n".join(rows)
    return f"""# JCV generic solver freeze

Status: **INSTRUMENT-FROZEN-BEFORE-PHYSICAL-FIXTURE**.

Pin commit: `{PIN_COMMIT}`.  The physical JCV fixture, scorer, output, receipt,
and paper paths were absent throughout this freeze.  This artifact reports
public calibration behavior only and carries no JCV physical verdict.

## Public exact calibration table

| model | nonempty gauge sectors | Krull dimensions |
|---|---:|---|
{table}

The backend uses rational multivariate polynomials, exact Buchberger reduction,
an independently checked S-pair remainder criterion, leading-monomial-ideal
dimension, exact sign-sector substitution, and saturation by an inverse
variable for nonzero-locus questions.

The frozen public battery has {gate_count} gates and {mutant_count} named
falsifiers.  It reads {measurements['anchor_count']} committed source anchors.
Every number in this note is rendered from the measurement object sealed in
`v16/code/jcv_public_receipt.json`.

## Non-claims

No physical comparison map, weight law, gauge quotient, solution dimension,
interference witness, backreaction, geometry, particle, constant, or QFT/GR
claim is made.  The next authorized event is the separate freeze of one
physical fixture and its verdict-neutral scorer, followed by one official run.
"""


def render_output(rows: list[GateRow], measurements: dict[str, Any], mutant_rows: list[dict[str, Any]]) -> str:
    lines = ["JCV GENERIC VARIETY SOLVER — PUBLIC CALIBRATIONS ONLY"]
    for row in rows:
        lines.append(f"GATE {row.gate} {'PASS' if row.passed else 'FAIL'} :: {row.evidence}")
    lines.append(f"MODELS {measurements['model_count']}")
    for model in measurements["models"]:
        dimensions = [sector["dimension"] for sector in model["sectors"] if not sector["empty"]]
        lines.append(f"MODEL {model['name']} NONEMPTY {model['nonempty_sectors']} DIMENSIONS {json.dumps(dimensions, separators=(',', ':'))}")
    lines.append(f"MUTANTS {sum(row['passed'] for row in mutant_rows)} OF {len(mutant_rows)} DIE AT NAMED GATES")
    lines.append("END JCV PUBLIC SOLVER FREEZE")
    return "\n".join(lines) + "\n"


def parse_gate_lines(output: str) -> list[tuple[str, bool, str]]:
    result = []
    pattern = re.compile(r"^GATE ([A-Z0-9-]+) (PASS|FAIL) :: (.*)$")
    for line in output.splitlines():
        match = pattern.fullmatch(line)
        if match:
            result.append((match.group(1), match.group(2) == "PASS", match.group(3)))
    return result


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
            rows.append({"mutant": name, "expected_gate": expected_gate, "observed_gate": "SURVIVED", "moved": False, "move_proofs": [], "passed": False})
    return rows


def verify_seal(payload: dict[str, Any], manifest: dict[str, str]) -> tuple[bool, str]:
    if set(payload) != set(manifest):
        return (False, f"key mismatch payload={len(payload)} manifest={len(manifest)}")
    moved = [key for key in payload if digest(payload[key]) != manifest[key]]
    return (not moved, "all keys match" if not moved else f"moved={moved}")


def build(root: Path, mutant_name: str | None = None, include_survey: bool = True) -> tuple[str, str, dict[str, Any]]:
    ledger, measurements, reader, mutator = run_core(root, mutant_name)
    mutant_rows: list[dict[str, Any]] = []
    if include_survey:
        mutant_rows = mutation_survey(root)
        ledger.gate("G-MUTANTS", len(mutant_rows) == len(MUTANT_GATES) and all(row["passed"] for row in mutant_rows), f"killed={sum(row['passed'] for row in mutant_rows)} declared={len(MUTANT_GATES)}")

    dummy = {"alpha": {"value": 1}, "beta": [2, 3]}
    dummy_manifest = {key: digest(value) for key, value in dummy.items()}
    clean_ok = verify_seal(dummy, dummy_manifest)[0]
    add_control = dict(dummy)
    add_control["intruder"] = 4
    edit_control = dict(dummy)
    edit_control["alpha"] = {"value": 9}
    controls_reject = not verify_seal(add_control, dummy_manifest)[0] and not verify_seal(edit_control, dummy_manifest)[0]
    if mutant_name == "SEAL_ADD":
        changed = dict(dummy)
        changed["intruder"] = 4
        dummy = mutator.move("SEAL_ADD", dummy, changed)
    if mutant_name == "SEAL_EDIT":
        changed = dict(dummy)
        changed["alpha"] = {"value": 9}
        dummy = mutator.move("SEAL_EDIT", dummy, changed)
    controls_ok = clean_ok and controls_reject and verify_seal(dummy, dummy_manifest)[0]
    ledger.gate("G-SEAL-CONTROLS", controls_ok, "clean seal accepted and add/edit controls are rejected")

    future_gate_count = len(ledger.rows) + 1
    note = render_note(measurements, future_gate_count, len(MUTANT_GATES))
    transcript_row = GateRow("G-TRANSCRIPT", True, "rendered gate multiset equals the in-memory ledger in both directions")
    projected_rows = ledger.rows + [transcript_row]
    output = render_output(projected_rows, measurements, mutant_rows)
    if mutant_name == "TRANSCRIPT_CONTRADICTION":
        changed = output.replace("PUBLIC CALIBRATIONS ONLY", "PUBLIC PHYSICAL RESULT", 1)
        output = mutator.move("TRANSCRIPT_CONTRADICTION", output, changed)
    got = parse_gate_lines(output)
    wanted = [(row.gate, row.passed, row.evidence) for row in projected_rows]
    transcript_ok = got == wanted and "PUBLIC PHYSICAL RESULT" not in output
    ledger.gate("G-TRANSCRIPT", transcript_ok, transcript_row.evidence)
    if len(ledger.rows) != future_gate_count:
        raise RuntimeError("gate count drift")

    output = render_output(ledger.rows, measurements, mutant_rows)
    note = render_note(measurements, len(ledger.rows), len(MUTANT_GATES))
    payload: dict[str, Any] = {
        "schema": "JCV-PUBLIC-RECEIPT-v1",
        "unit": "v16-jcv-solver-freeze",
        "status": "INSTRUMENT-FROZEN-BEFORE-PHYSICAL-FIXTURE",
        "pin_commit": PIN_COMMIT,
        "base_commit": BASE_COMMIT,
        "measurements": measurements,
        "gates": [serial(row.__dict__) for row in ledger.rows],
        "mutant_survey": mutant_rows,
        "source_anchors": SOURCE_ANCHORS,
        "read_set": sorted(set(reader.reads)),
        "scope": {"public_calibrations_only": True, "physical_fixture_present": False, "exact_field": "Q", "complex_physical_claim": False},
        "note_sha256": bytes_digest(note.encode("utf-8")),
        "output_sha256": bytes_digest(output.encode("utf-8")),
    }
    manifest = {key: digest(value) for key, value in payload.items()}
    receipt = dict(payload)
    receipt["seal_manifest"] = {
        "algorithm": "sha256-canonical-json",
        "total_keys_excluding_manifest": len(payload),
        "sealed_keys": manifest,
    }
    return note, output, serial(receipt)


def atomic_promote(root: Path, note: str, output: str, receipt: dict[str, Any]) -> None:
    targets = {
        root / "v16/note-jcv-solver-freeze.md": note.encode("utf-8"),
        root / "v16/code/jcv_public_output.txt": output.encode("utf-8"),
        root / "v16/code/jcv_public_receipt.json": (json.dumps(receipt, sort_keys=True, indent=1, ensure_ascii=False) + "\n").encode("utf-8"),
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
        staged_receipt = json.loads(staged[root / "v16/code/jcv_public_receipt.json"].read_text(encoding="utf-8"))
        manifest = staged_receipt.pop("seal_manifest")
        ok, evidence = verify_seal(staged_receipt, manifest["sealed_keys"])
        if not ok:
            raise GateFail("G-SEAL-CONTROLS", f"staged receipt {evidence}")
        if bytes_digest(staged[root / "v16/note-jcv-solver-freeze.md"].read_bytes()) != staged_receipt["note_sha256"]:
            raise GateFail("G-SEAL-CONTROLS", "staged note hash mismatch")
        if bytes_digest(staged[root / "v16/code/jcv_public_output.txt"].read_bytes()) != staged_receipt["output_sha256"]:
            raise GateFail("G-SEAL-CONTROLS", "staged output hash mismatch")
        for target in targets:
            os.replace(staged[target], target)
        promoted = True
        on_disk = json.loads((root / "v16/code/jcv_public_receipt.json").read_text(encoding="utf-8"))
        disk_manifest = on_disk.pop("seal_manifest")
        ok, evidence = verify_seal(on_disk, disk_manifest["sealed_keys"])
        if not ok:
            raise GateFail("G-SEAL-CONTROLS", f"promoted receipt {evidence}")
        if bytes_digest((root / "v16/note-jcv-solver-freeze.md").read_bytes()) != on_disk["note_sha256"]:
            raise GateFail("G-SEAL-CONTROLS", "promoted note hash mismatch")
        if bytes_digest((root / "v16/code/jcv_public_output.txt").read_bytes()) != on_disk["output_sha256"]:
            raise GateFail("G-SEAL-CONTROLS", "promoted output hash mismatch")
    finally:
        if not promoted:
            for temporary in staged.values():
                if temporary.exists():
                    temporary.unlink()


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
    if mode == "plain":
        note, output, receipt = build(root)
        atomic_promote(root, note, output, receipt)
        return 0

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
            print(f"MUTANT-FAIL {mutant} expected={expected} observed={exc.gate} moved={moved} writes={before != after}", file=sys.stderr)
            return 1
        print(f"MUTANT-DIED {mutant} AT {exc.gate} MOVE {exc.mutations[0].before}->{exc.mutations[0].after}")
        return 0 if mode == "selftest" else 3
    print(f"MUTANT-SURVIVED {mutant}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
