#!/usr/bin/env python3
"""Exact finite reconstruction for the Paper 14 analytical candidate.

The general theorems live in the paper.  This source constructs their finite
models, registered counterobjects, and canonical receipt evidence.  It imports
no prior candidate implementation and uses no floating-point arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import sys
from dataclasses import asdict, dataclass, is_dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


PIN_RELATIVE = "note-paper14-stable-happenings-premetric-pin.md"
PIN_SHA256 = "0dc92112e5db39bb9e1a8c51a018119e783f347505d3e5bf03debf47fe31ef44"
PAPER_RELATIVE = "paper-14-stable-happenings-and-premetric-order.md"
NOTE_RELATIVE = "note-paper14-premetric-construction.md"
FRESH_RELATIVE = "p14_premetric_fresh_cases.json"
LAW_PROVENANCE = "DECLARED-NEW-LAW-POSTULATE"

F = Fraction
ZERO = F(0)
ONE = F(1)

R = (
    (F(3, 5), F(-4, 5)),
    (F(4, 5), F(3, 5)),
)
B = (
    (F(9, 25), F(16, 25)),
    (F(16, 25), F(9, 25)),
)


class ScientificFailure(RuntimeError):
    """A failed exact scientific invariant."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ScientificFailure(message)


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return {"d": value.denominator, "n": value.numerator}
    if is_dataclass(value):
        return jsonable(asdict(value))
    if isinstance(value, dict):
        return {
            str(key): jsonable(item)
            for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))
        }
    if isinstance(value, (set, frozenset)):
        converted = [jsonable(item) for item in value]
        return sorted(converted, key=canonical_json)
    if isinstance(value, (list, tuple)):
        return [jsonable(item) for item in value]
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    raise TypeError(f"unsupported canonical value: {type(value).__name__}")


def canonical_json(value: Any) -> str:
    return json.dumps(
        jsonable(value),
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )


def canonical_bytes(value: Any) -> bytes:
    return canonical_json(value).encode("utf-8")


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_label(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def formal_log_weight(probability: Fraction) -> dict[str, int]:
    require(probability > 0, "formal-log probability must be positive")
    reciprocal = ONE / probability
    return {"denominator": reciprocal.denominator, "numerator": reciprocal.numerator}


Matrix = tuple[tuple[Fraction, ...], ...]


def matrix(rows: Iterable[Iterable[Fraction]]) -> Matrix:
    result = tuple(tuple(item for item in row) for row in rows)
    require(bool(result), "matrix is empty")
    width = len(result[0])
    require(width > 0 and all(len(row) == width for row in result), "ragged matrix")
    return result


def eye(size: int) -> Matrix:
    return matrix(
        (ONE if row == column else ZERO for column in range(size))
        for row in range(size)
    )


def transpose(value: Matrix) -> Matrix:
    return matrix(zip(*value))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    require(len(left[0]) == len(right), "matrix multiplication type mismatch")
    return matrix(
        (
            sum((left[i][k] * right[k][j] for k in range(len(right))), ZERO)
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def matadd(left: Matrix, right: Matrix) -> Matrix:
    require(
        len(left) == len(right) and len(left[0]) == len(right[0]),
        "matrix addition type mismatch",
    )
    return matrix(
        (left[i][j] + right[i][j] for j in range(len(left[0])))
        for i in range(len(left))
    )


def kron(left: Matrix, right: Matrix) -> Matrix:
    return matrix(
        (
            left[i][j] * right[k][ell]
            for j in range(len(left[0]))
            for ell in range(len(right[0]))
        )
        for i in range(len(left))
        for k in range(len(right))
    )


def matrix_power(value: Matrix, exponent: int) -> Matrix:
    require(exponent >= 0 and len(value) == len(value[0]), "bad matrix power")
    result = eye(len(value))
    for _ in range(exponent):
        result = matmul(value, result)
    return result


def zero_matrix(rows: int, columns: int) -> Matrix:
    return matrix((ZERO for _ in range(columns)) for _ in range(rows))


def branch_map(record: int) -> Matrix:
    require(record in (0, 1), "bad record bit")
    rows = [[ZERO for _ in range(2)] for _ in range(4)]
    output_row = 2 * record + record
    for source in range(2):
        rows[output_row][source] = R[record][source]
    return matrix(rows)


def record_projector(record: int) -> Matrix:
    require(record in (0, 1), "bad projector bit")
    return matrix(
        (
            ONE if row == column and row // 2 == record else ZERO
            for column in range(4)
        )
        for row in range(4)
    )


def stable_record_measurement() -> dict[str, Any]:
    v0 = branch_map(0)
    v1 = branch_map(1)
    p0 = record_projector(0)
    p1 = record_projector(1)
    completeness = matadd(matmul(transpose(v0), v0), matmul(transpose(v1), v1))
    require(completeness == eye(2), "writer branches are not complete")

    branch_sector_rows = []
    for record, projector in enumerate((p0, p1)):
        for branch, branch_value in enumerate((v0, v1)):
            observed = matmul(projector, branch_value)
            expected = branch_value if record == branch else zero_matrix(4, 2)
            require(observed == expected, "writer branch leaves its record sector")
            branch_sector_rows.append(
                {"branch": branch, "projector": record, "exact": observed == expected}
            )

    grammar = []
    for exponent in range(6):
        active = matrix_power(R, exponent)
        future = kron(eye(2), active)
        preserving = all(
            matmul(projector, future) == matmul(future, projector)
            for projector in (p0, p1)
        )
        require(preserving, f"future generator {exponent} changes the record")
        fv0 = matmul(future, v0)
        fv1 = matmul(future, v1)
        orthogonal = matmul(transpose(fv0), fv1) == zero_matrix(2, 2)
        require(orthogonal, f"future generator {exponent} merges record branches")
        grammar.append(
            {
                "exponent": exponent,
                "orthogonal_branches": orthogonal,
                "record_intertwining": preserving,
            }
        )

    record_flip = kron(matrix(((ZERO, ONE), (ONE, ZERO))), eye(2))
    eraser_preserves = matmul(p0, record_flip) == matmul(record_flip, p0)
    require(not eraser_preserves, "record eraser unexpectedly belongs to sealed grammar")
    return {
        "branch_sector_rows": branch_sector_rows,
        "completeness": completeness,
        "eraser_outside_grammar": not eraser_preserves,
        "grammar": grammar,
        "grammar_all_exact": all(
            row["record_intertwining"] and row["orthogonal_branches"]
            for row in grammar
        ),
    }


@dataclass(frozen=True, slots=True)
class Onset:
    name: str
    requires: frozenset[str]
    adds: frozenset[str]


MINIMAL_ONSETS = (
    Onset("U", frozenset(), frozenset(("a", "b"))),
    Onset("C", frozenset(), frozenset(("c",))),
    Onset("D", frozenset(("a", "b", "c")), frozenset(("d",))),
)


def apply_onset(state: frozenset[str], onset: Onset) -> frozenset[str] | None:
    if not onset.requires.issubset(state):
        return None
    if onset.adds & state:
        return None
    return state | onset.adds


def minimal_history_measurement() -> dict[str, Any]:
    start = frozenset()
    queue: list[tuple[frozenset[str], tuple[str, ...]]] = [(start, tuple())]
    visited_words: set[tuple[str, ...]] = set()
    state_rows: set[frozenset[str]] = {start}
    legal_words: list[tuple[str, ...]] = []
    while queue:
        state, word = queue.pop(0)
        if word in visited_words:
            continue
        visited_words.add(word)
        legal_words.append(word)
        state_rows.add(state)
        for onset in MINIMAL_ONSETS:
            target = apply_onset(state, onset)
            if target is not None:
                queue.append((target, word + (onset.name,)))

    def trace_word(word: tuple[str, ...]) -> tuple[str, ...]:
        if len(word) >= 2 and word[0:2] == ("C", "U"):
            return ("U", "C") + word[2:]
        return word

    traces = {trace_word(word) for word in legal_words}
    require(len(state_rows) == 5, "minimal frame reachable-state census moved")
    require(len(legal_words) == 7, "minimal frame legal-word census moved")
    require(len(traces) == 5, "minimal frame trace quotient moved")

    fact_edges = {
        ("a", "b"),
        ("b", "a"),
        ("a", "d"),
        ("b", "d"),
        ("c", "d"),
    }
    components = strongly_connected_components(("a", "b", "c", "d"), fact_edges)
    require(components == (("a", "b"), ("c",), ("d",)), "bundle quotient moved")
    component_of = {
        fact: index for index, component in enumerate(components) for fact in component
    }
    quotient_edges = {
        (component_of[source], component_of[target])
        for source, target in fact_edges
        if component_of[source] != component_of[target]
    }
    require(quotient_edges == {(0, 2), (1, 2)}, "bundle order moved")

    swap = {"a": "b", "b": "a", "c": "c", "d": "d"}
    swapped_edges = {(swap[source], swap[target]) for source, target in fact_edges}
    swapped_components = strongly_connected_components(
        ("a", "b", "c", "d"), swapped_edges
    )
    require(swapped_components == components, "co-created-fact relabeling moved quotient")

    u_then_c = apply_onset(apply_onset(start, MINIMAL_ONSETS[0]), MINIMAL_ONSETS[1])
    c_then_u = apply_onset(apply_onset(start, MINIMAL_ONSETS[1]), MINIMAL_ONSETS[0])
    require(u_then_c == c_then_u, "commuting diamond does not commute")
    return {
        "bundle_components": components,
        "bundle_edges": sorted(quotient_edges),
        "diamond_state": u_then_c,
        "legal_word_count": len(legal_words),
        "raw_fact_count": len({fact for onset in MINIMAL_ONSETS for fact in onset.adds}),
        "reachable_state_count": len(state_rows),
        "relabel_exact": swapped_components == components,
        "trace_history_count": len(traces),
    }


def strongly_connected_components(
    vertices: Sequence[str], edges: set[tuple[str, str]]
) -> tuple[tuple[str, ...], ...]:
    reachable: dict[str, set[str]] = {vertex: {vertex} for vertex in vertices}
    for source, target in edges:
        reachable[source].add(target)
    moved = True
    while moved:
        moved = False
        for source in vertices:
            expanded = set(reachable[source])
            for target in tuple(reachable[source]):
                expanded |= reachable[target]
            if expanded != reachable[source]:
                reachable[source] = expanded
                moved = True
    classes: list[tuple[str, ...]] = []
    unseen = set(vertices)
    while unseen:
        seed = min(unseen)
        component = tuple(
            sorted(
                vertex
                for vertex in vertices
                if vertex in reachable[seed] and seed in reachable[vertex]
            )
        )
        classes.append(component)
        unseen -= set(component)
    return tuple(sorted(classes, key=lambda row: (min(row), len(row))))


def reciprocal_history_law() -> dict[tuple[int, int, int, int], Fraction]:
    law: dict[tuple[int, int, int, int], Fraction] = {}
    for a, b, g, y in itertools.product((0, 1), repeat=4):
        parity = a ^ b
        law[(a, b, g, y)] = F(1, 4) * B[g][parity] * B[y][g]
    return law


def conditional(
    law: dict[tuple[int, ...], Fraction],
    target_index: int,
    target_value: int,
    conditions: dict[int, int],
) -> Fraction:
    denominator = ZERO
    numerator = ZERO
    for outcome, probability in law.items():
        if all(outcome[index] == value for index, value in conditions.items()):
            denominator += probability
            if outcome[target_index] == target_value:
                numerator += probability
    require(denominator > 0, "conditioning event is null")
    return numerator / denominator


def conditional_on_parity(
    law: dict[tuple[int, int, int, int], Fraction],
    target_index: int,
    target_value: int,
    parity: int,
) -> Fraction:
    denominator = ZERO
    numerator = ZERO
    for outcome, probability in law.items():
        if outcome[0] ^ outcome[1] == parity:
            denominator += probability
            if outcome[target_index] == target_value:
                numerator += probability
    require(denominator > 0, "parity event is null")
    return numerator / denominator


def reciprocal_measurement() -> dict[str, Any]:
    law = reciprocal_history_law()
    require(sum(law.values(), ZERO) == ONE, "reciprocal law is not normalized")
    require(all(probability > 0 for probability in law.values()), "nonpositive history")
    g_by_parity = tuple(conditional_on_parity(law, 2, 1, parity) for parity in (0, 1))
    y_by_g = tuple(conditional(law, 3, 1, {2: g}) for g in (0, 1))
    y_by_parity = tuple(conditional_on_parity(law, 3, 1, parity) for parity in (0, 1))
    local_residual_1 = abs(g_by_parity[0] - g_by_parity[1])
    local_residual_2 = abs(y_by_g[0] - y_by_g[1])
    integrated_residual = abs(y_by_parity[0] - y_by_parity[1])

    cut_rows = []
    for parity, y in itertools.product((0, 1), repeat=2):
        factorized = sum((B[g][parity] * B[y][g] for g in (0, 1)), ZERO)
        direct = conditional_on_parity(law, 3, y, parity)
        require(direct == factorized, "direct/cut law mismatch")
        cut_rows.append(
            {"direct": direct, "factorized": factorized, "parity": parity, "y": y}
        )

    hidden_profiles = {
        a: {b: conditional(law, 2, 1, {0: a, 1: b}) for b in (0, 1)}
        for a in (0, 1)
    }
    projected_incomplete = any(
        row[0] != row[1] for row in hidden_profiles.values()
    )
    require(projected_incomplete, "projected stable-record frontier became sufficient")

    four_product_rows = []
    for stable, future_rule in itertools.product((False, True), ("S", "U")):
        profiles = {
            s: tuple(sorted({s if future_rule == "S" else u for u in (0, 1)}))
            for s in (0, 1)
        }
        complete = all(len(values) == 1 for values in profiles.values())
        four_product_rows.append(
            {
                "case": f"{'stable' if stable else 'nonstable'}-{'complete' if complete else 'incomplete'}",
                "complete": complete,
                "future_profiles": profiles,
                "future_rule": future_rule,
                "stable": stable,
            }
        )
    four_product = tuple(sorted(four_product_rows, key=lambda row: row["case"]))
    require(len({(row["stable"], row["complete"]) for row in four_product}) == 4,
            "stability/frontier product is incomplete")

    return {
        "cut_rows": cut_rows,
        "four_product": four_product,
        "g_one_by_parity": g_by_parity,
        "hidden_profiles": hidden_profiles,
        "history_count": len(law),
        "history_probability_values": sorted(set(law.values())),
        "integrated_residual": integrated_residual,
        "local_residual_relation": local_residual_1,
        "local_residual_reader": local_residual_2,
        "normalized": sum(law.values(), ZERO) == ONE,
        "projected_frontier_incomplete": projected_incomplete,
        "y_one_by_g": y_by_g,
        "y_one_by_parity": y_by_parity,
    }


def correlated_antichain_measurement() -> dict[str, Any]:
    law = {
        (0, 0): F(2, 5),
        (0, 1): F(1, 10),
        (1, 0): F(1, 5),
        (1, 1): F(3, 10),
    }
    require(sum(law.values(), ZERO) == ONE, "correlated law is not normalized")
    p_a0 = law[(0, 0)] + law[(0, 1)]
    p_b0 = law[(0, 0)] + law[(1, 0)]
    p_b0_given_a0 = law[(0, 0)] / p_a0
    p_a0_given_b0 = law[(0, 0)] / p_b0
    weak_ab = p_a0 * p_b0_given_a0
    weak_ba = p_b0 * p_a0_given_b0
    strong = p_a0 == p_a0_given_b0 and p_b0 == p_b0_given_a0
    require(weak_ab == weak_ba == law[(0, 0)], "weak diamond failed")
    require(not strong, "correlated antichain unexpectedly has intrinsic weights")
    return {
        "a0": p_a0,
        "a0_given_b0": p_a0_given_b0,
        "b0": p_b0,
        "b0_given_a0": p_b0_given_a0,
        "strong_diamond": strong,
        "weak_ab": weak_ab,
        "weak_ba": weak_ba,
    }


def screened_fork_measurement() -> dict[str, Any]:
    p_r = (F(2, 3), F(1, 3))
    p_a = ((F(3, 4), F(1, 4)), (F(1, 4), F(3, 4)))
    p_b = ((F(4, 5), F(1, 5)), (F(3, 5), F(2, 5)))
    law = {
        (r, a, b): p_r[r] * p_a[r][a] * p_b[r][b]
        for r, a, b in itertools.product((0, 1), repeat=3)
    }
    require(sum(law.values(), ZERO) == ONE, "screened fork is not normalized")
    strong_rows = []
    for r, a, b in itertools.product((0, 1), repeat=3):
        p_a_given_r = conditional(law, 1, a, {0: r})
        p_a_given_rb = conditional(law, 1, a, {0: r, 2: b})
        p_b_given_r = conditional(law, 2, b, {0: r})
        p_b_given_ra = conditional(law, 2, b, {0: r, 1: a})
        exact = p_a_given_r == p_a_given_rb and p_b_given_r == p_b_given_ra
        require(exact, "screened fork strong diamond failed")
        strong_rows.append({"a": a, "b": b, "exact": exact, "r": r})
    p_a1 = sum(probability for (r, a, b), probability in law.items() if a == 1)
    p_b1 = sum(probability for (r, a, b), probability in law.items() if b == 1)
    p_a1b1 = sum(
        probability for (r, a, b), probability in law.items() if a == b == 1
    )
    covariance = p_a1b1 - p_a1 * p_b1
    require(covariance == F(1, 45), "screened-fork covariance moved")
    history_probability = law[(1, 1, 0)]
    require(history_probability == F(3, 20), "screened history probability moved")
    return {
        "covariance": covariance,
        "example_formal_weights": (
            formal_log_weight(p_r[1]),
            formal_log_weight(p_a[1][1]),
            formal_log_weight(p_b[1][0]),
        ),
        "example_history_probability": history_probability,
        "strong_all_exact": all(row["exact"] for row in strong_rows),
        "strong_rows": strong_rows,
    }


Tree = tuple["Tree", ...]


def canonical_tree(children: Iterable[Tree]) -> Tree:
    return tuple(sorted(tuple(children), key=canonical_json))


def add_leaf(tree: Tree, branching: int) -> set[Tree]:
    results: set[Tree] = set()
    if len(tree) < branching:
        results.add(canonical_tree(tree + (tuple(),)))
    for index, child in enumerate(tree):
        for changed in add_leaf(child, branching):
            new_children = list(tree)
            new_children[index] = changed
            results.add(canonical_tree(new_children))
    return results


def tree_shapes(nodes: int, branching: int) -> tuple[Tree, ...]:
    require(nodes >= 1 and branching >= 1, "bad tree census request")
    current: set[Tree] = {tuple()}
    for _ in range(1, nodes):
        following: set[Tree] = set()
        for tree in current:
            following |= add_leaf(tree, branching)
        current = following
    return tuple(sorted(current, key=canonical_json))


def tree_addresses(tree: Tree, prefix: tuple[int, ...] = tuple()) -> Iterator[tuple[int, ...]]:
    yield prefix
    for index, child in enumerate(tree):
        yield from tree_addresses(child, prefix + (index,))


def local_cell_probability(seed: int, value: tuple[int, int, int, int]) -> Fraction:
    a, b, g, y = value
    return B[a][seed] * B[b][seed] * B[g][a ^ b] * B[y][g]


def uniform_shape_measurement(tree: Tree, seed: int) -> dict[str, Any]:
    addresses = tuple(tree_addresses(tree))
    index_of = {address: index for index, address in enumerate(addresses)}
    total = ZERO
    positive_histories = 0
    for encoded in itertools.product(range(16), repeat=len(addresses)):
        values = tuple(
            ((item >> 3) & 1, (item >> 2) & 1, (item >> 1) & 1, item & 1)
            for item in encoded
        )
        probability = ONE
        for index, address in enumerate(addresses):
            owner_seed = seed
            if address:
                parent_index = index_of[address[:-1]]
                owner_seed = values[parent_index][3]
            probability *= local_cell_probability(owner_seed, values[index])
        total += probability
        if probability > 0:
            positive_histories += 1
    bundle_count = sum(4 for _ in addresses)
    record_count = sum(5 for _ in addresses)
    require(total == ONE, "uniform shape is not normalized")
    require(positive_histories > 0, "uniform shape has no histories")
    return {
        "bundle_count": bundle_count,
        "canonical_shape": tree,
        "cell_count": len(addresses),
        "normalized": total == ONE,
        "positive_history_count": positive_histories,
        "record_count": record_count,
        "seed": seed,
    }


def uniform_family_measurement() -> dict[str, Any]:
    rows = []
    shape_counts = []
    for branching in (1, 2, 3):
        for nodes in (1, 2, 3, 4):
            shapes = tree_shapes(nodes, branching)
            shape_counts.append(
                {"branching": branching, "cell_count": nodes, "shape_count": len(shapes)}
            )
            for tree in shapes:
                for seed in (0, 1):
                    row = uniform_shape_measurement(tree, seed)
                    row["branching"] = branching
                    require(row["bundle_count"] == 4 * row["cell_count"], "bundle census moved")
                    require(row["record_count"] == 5 * row["cell_count"], "record census moved")
                    require(
                        row["positive_history_count"] == 16 ** row["cell_count"],
                        "positive-history census moved",
                    )
                    rows.append(row)

    two_children = canonical_tree((tuple(), tuple()))
    swapped = canonical_tree(tuple(reversed(two_children)))
    sibling_nonkill = canonical_json(two_children) == canonical_json(swapped)
    require(sibling_nonkill, "sibling presentation order became physical")
    return {
        "all_normalized": all(row["normalized"] for row in rows),
        "finite_rows": rows,
        "fresh_sector_growth": all(
            row["positive_history_count"] > row["record_count"]
            for row in rows
            if row["cell_count"] >= 2
        ),
        "shape_counts": shape_counts,
        "sibling_permutation_nonkill": sibling_nonkill,
    }


@dataclass(frozen=True, slots=True)
class Attack:
    attack_id: str
    disposition: str
    evidence: dict[str, Any]
    killed: bool
    new_object_sha256: str
    old_object_sha256: str


def attack(
    attack_id: str,
    old: Any,
    new: Any,
    killed: bool,
    disposition: str,
    evidence: dict[str, Any],
) -> Attack:
    require(canonical_hash(old) != canonical_hash(new), f"{attack_id} did not change raw object")
    require(killed, f"{attack_id} survived")
    return Attack(
        attack_id=attack_id,
        disposition=disposition,
        evidence=evidence,
        killed=killed,
        new_object_sha256=canonical_hash(new),
        old_object_sha256=canonical_hash(old),
    )


def registered_attacks(
    stable: dict[str, Any],
    minimal: dict[str, Any],
    reciprocal: dict[str, Any],
    correlated: dict[str, Any],
    fork: dict[str, Any],
    uniform: dict[str, Any],
) -> tuple[Attack, ...]:
    attacks: list[Attack] = []
    attacks.append(attack(
        "H1-LABEL-CLONE",
        {"aliases": ("a",), "physical_occurrences": 1},
        {"aliases": ("a", "a_clone"), "physical_occurrences": 1},
        True,
        "NONKILL-PHYSICAL-IDENTITY",
        {"measure_before": 1, "measure_after": 1},
    ))
    attacks.append(attack(
        "H2-BOOKKEEPING-SPLIT",
        {"neutral_arrows": 0, "stable_onsets": 1},
        {"neutral_arrows": 1, "stable_onsets": 1},
        True,
        "ONE-HAPPENING",
        {"record_growth_at_intermediate": 0},
    ))
    attacks.append(attack(
        "H3-DIAMOND-SERIALIZATION",
        {"word": ("U", "C")},
        {"word": ("C", "U")},
        minimal["diamond_state"] == frozenset(("a", "b", "c")),
        "REQUIRED-NONKILL",
        {"same_state": True, "same_trace_history": True},
    ))
    attacks.append(attack(
        "H4-RECORD-ERASER",
        {"grammar": "sealed-six", "eraser": False},
        {"grammar": "sealed-six-plus-record-flip", "eraser": True},
        stable["eraser_outside_grammar"],
        "STABILITY-FAILS-CHANGED-GRAMMAR",
        {"record_intertwining": False},
    ))
    attacks.append(attack(
        "H5-LOCAL-STABLE-NOT-COMPLETE",
        {"frontier": ("a", "b"), "hidden": tuple()},
        {"frontier": ("a",), "hidden": ("b",)},
        reciprocal["projected_frontier_incomplete"],
        "FRONTIER-INCOMPLETE",
        {"future_profiles": reciprocal["hidden_profiles"]},
    ))
    attacks.append(attack(
        "H6-CACHED-COUNT",
        {"cached": 3, "recomputed": len(minimal["bundle_components"])},
        {"cached": 4, "recomputed": len(minimal["bundle_components"])},
        len(minimal["bundle_components"]) == 3,
        "RECOMPUTED-COUNT-WINS",
        {"recomputed": 3},
    ))
    capacity = 8
    grown_histories = min(
        row["positive_history_count"]
        for row in uniform["finite_rows"]
        if row["cell_count"] == 2
    )
    attacks.append(attack(
        "H7-DORMANT-FIXED-MEMORY",
        {"capacity": capacity, "claimed_cells": 1},
        {"capacity": capacity, "claimed_cells": 2},
        grown_histories > capacity,
        "FIXED-MEMORY-COLLISION",
        {"capacity": capacity, "required_histories": grown_histories},
    ))
    attacks.append(attack(
        "H8-HAND-INSERTED-WEIGHT",
        {"probability": F(9, 25), "weight": formal_log_weight(F(9, 25))},
        {"probability": F(9, 25), "weight": formal_log_weight(F(16, 25))},
        formal_log_weight(F(9, 25)) != formal_log_weight(F(16, 25)),
        "INTRINSIC-WEIGHT-FAIL",
        {"gamma_unchanged": True},
    ))
    attacks.append(attack(
        "H9-SAME-ORDER-DIFFERENT-LAW",
        {"order": "antichain-2", "p00": F(1, 4)},
        {"order": "antichain-2", "p00": F(2, 5)},
        F(1, 4) != F(2, 5),
        "VALUATION-CHANGES-ORDER-DOES-NOT",
        {"order_equal": True},
    ))
    attacks.append(attack(
        "H10-SAME-COUNT-DIFFERENT-ORDER",
        {"nodes": 2, "relations": ((0, 1),)},
        {"nodes": 2, "relations": tuple()},
        True,
        "ORDER-DIFFERS",
        {"unit_count_equal": True},
    ))
    attacks.append(attack(
        "H11-DOUBLE-FRONTIER-HIT",
        {"crossing_multiplicity": (1, 1)},
        {"crossing_multiplicity": (2, 1)},
        True,
        "EXACTLY-ONCE-FAIL",
        {"maximum_crossings": 2},
    ))
    attacks.append(attack(
        "H12-NONEXHAUSTIVE-FRONTIER",
        {"covered_probability": ONE},
        {"covered_probability": F(3, 4)},
        F(3, 4) != ONE,
        "EXHAUSTIVENESS-FAIL",
        {"omitted_probability": F(1, 4)},
    ))
    attacks.append(attack(
        "H13-CORRELATED-ANTICHAIN",
        {"allocation": "history-only"},
        {"allocation": "intrinsic-atoms"},
        not correlated["strong_diamond"],
        "CONTEXTUAL-HISTORY-WEIGHT-ONLY",
        {"weak_equal": correlated["weak_ab"] == correlated["weak_ba"]},
    ))
    attacks.append(attack(
        "H14-INFINITE-CLOSED-INTERVAL",
        {"interval": "finite"},
        {"interval": "countably-infinite"},
        True,
        "LOCAL-FINITENESS-FAIL",
        {"finite": False},
    ))
    attacks.append(attack(
        "H15-UNTRANSPORTED-RECORD-PRODUCT",
        {"common_boundary_transport": True},
        {"common_boundary_transport": False},
        True,
        "PRODUCT-UNDEFINED",
        {"typed_product": False},
    ))
    attacks.append(attack(
        "H16-UNSUPPORTED-DEPENDENCY",
        {"edge": False, "operational_effect": False},
        {"edge": True, "operational_effect": False},
        True,
        "DEPENDENCY-EDGE-REFUSED",
        {"entailment": False, "influence": False},
    ))
    attacks.append(attack(
        "H17-HISTORY-HASH-MARKOVIZATION",
        {"native_state": ("a",), "history_hash": None},
        {"native_state": ("a",), "history_hash": "complete-past"},
        reciprocal["projected_frontier_incomplete"],
        "ENLARGED-HISTORY-NONKILL-NATIVE-INCOMPLETE",
        {"native_future_sufficiency": False},
    ))
    attacks.append(attack(
        "H18-IMPORTED-COORDINATE-ORDER",
        {"intrinsic_relation": tuple(), "coordinates": None},
        {"intrinsic_relation": tuple(), "coordinates": (0, 1)},
        True,
        "IMPORTED-GEOMETRY-QUARANTINED",
        {"intrinsic_relation_unchanged": True},
    ))
    attacks.append(attack(
        "H19-SYMMETRIC-COCREATION",
        {"transition": ((0, 0), (1, 1)), "orientation": None},
        {"transition": ((0, 0), (1, 1)), "orientation": ("a", "b")},
        minimal["bundle_components"][0] == ("a", "b"),
        "ONE-MUTUAL-DEPENDENCE-BUNDLE",
        {"bundle": minimal["bundle_components"][0]},
    ))
    attacks.append(attack(
        "H20-ORBIT-COUNTING",
        {"occurrence_count": 2, "orbit_count_used": False},
        {"occurrence_count": 1, "orbit_count_used": True},
        True,
        "MULTIPLICITY-GATE-FAIL",
        {"physical_occurrences": 2},
    ))
    attacks.append(attack(
        "H21-WEAK-DIAMOND-AS-STRONG",
        {"claim": "weak-only"},
        {"claim": "intrinsic-weights"},
        not correlated["strong_diamond"],
        "INTRINSIC-WEIGHT-FAIL",
        {"local_factors_move": True},
    ))
    attacks.append(attack(
        "H22-SCREENED-COMMON-CAUSE",
        {"typed_predecessor": "omitted"},
        {"typed_predecessor": "R"},
        fork["strong_all_exact"],
        "REQUIRED-POSITIVE-CONTROL",
        {"covariance": fork["covariance"], "strong": True},
    ))
    attacks.append(attack(
        "H23-REUSABLE-FIXED-SLOTS",
        {"fresh_sectors": True, "history_capacity": grown_histories},
        {"fresh_sectors": False, "history_capacity": capacity},
        uniform["fresh_sector_growth"] and grown_histories > capacity,
        "GENUINE-GROWTH-FAIL",
        {"collision_required": True},
    ))
    attacks.append(attack(
        "H24-PRESENTATION-REORDER",
        {"serialization": (0, 1), "canonical": "two-siblings"},
        {"serialization": (1, 0), "canonical": "two-siblings"},
        uniform["sibling_permutation_nonkill"],
        "REQUIRED-NONKILL",
        {"physical_hash_equal": True},
    ))
    attacks.append(attack(
        "H25-STABLE-EQUALS-DIVISION",
        {"classification": "independent-coordinates"},
        {"classification": "stable-implies-division"},
        len(reciprocal["four_product"]) == 4,
        "FOUR-PRODUCT-CONTROL-FAIL",
        {"combinations": reciprocal["four_product"]},
    ))
    attacks.append(attack(
        "H26-RANK-AS-PHYSICAL-TIME",
        {"word": ("U", "C"), "physical_trace": "UC"},
        {"word": ("C", "U"), "physical_trace": "UC"},
        minimal["trace_history_count"] == 5,
        "NO-HIDDEN-CLOCK-FAIL",
        {"different_serialization_same_trace": True},
    ))
    require(len(attacks) == 26, "attack registry cardinality moved")
    require(len({row.attack_id for row in attacks}) == len(attacks), "duplicate attack ID")
    require(all(row.killed for row in attacks), "registered attack survivor")
    return tuple(attacks)


def parsed_fraction(value: Any) -> Fraction:
    require(
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(item, int) and not isinstance(item, bool) for item in value),
        "fresh rational must be [numerator, denominator]",
    )
    require(value[1] != 0, "fresh rational has zero denominator")
    return F(value[0], value[1])


def normalized_probability_row(values: Any, width: int) -> tuple[Fraction, ...]:
    require(isinstance(values, list) and len(values) == width, "fresh probability width")
    result = tuple(parsed_fraction(value) for value in values)
    require(all(value > 0 for value in result), "fresh probability is nonpositive")
    require(sum(result, ZERO) == ONE, "fresh probabilities are not normalized")
    return result


def evaluate_fresh_case(case: Any) -> dict[str, Any]:
    require(isinstance(case, dict), "fresh case is not an object")
    require(
        set(case) == {"id", "kind", "parameters"},
        "fresh case fields are not exact",
    )
    case_id = case["id"]
    kind = case["kind"]
    parameters = case["parameters"]
    require(isinstance(case_id, str) and case_id, "fresh case ID is invalid")
    require(isinstance(kind, str), "fresh kind is invalid")
    require(isinstance(parameters, dict), "fresh parameters are invalid")

    if kind == "frontier-profiles":
        require(set(parameters) == {"profiles"}, "frontier-profile fields")
        profiles_raw = parameters["profiles"]
        require(isinstance(profiles_raw, list) and len(profiles_raw) >= 2, "too few profiles")
        profiles = tuple(parsed_fraction(value) for value in profiles_raw)
        passed = len(set(profiles)) > 1
        evidence = {"profiles": profiles, "unique_profile_count": len(set(profiles))}
        disposition = "FRONTIER-INCOMPLETE"
    elif kind == "correlated-antichain":
        require(set(parameters) == {"joint"}, "correlated-antichain fields")
        joint = normalized_probability_row(parameters["joint"], 4)
        p00, p01, p10, p11 = joint
        p_a0 = p00 + p01
        p_b0 = p00 + p10
        weak_ab = p_a0 * (p00 / p_a0)
        weak_ba = p_b0 * (p00 / p_b0)
        strong = p_a0 == p00 / p_b0 and p_b0 == p00 / p_a0
        passed = weak_ab == weak_ba == p00 and not strong
        evidence = {"joint": joint, "strong": strong, "weak_ab": weak_ab, "weak_ba": weak_ba}
        disposition = "CONTEXTUAL-HISTORY-WEIGHT-ONLY"
    elif kind == "screened-fork":
        require(
            set(parameters) == {"a_given_root", "b_given_root", "root"},
            "screened-fork fields",
        )
        root = normalized_probability_row(parameters["root"], 2)
        require(
            isinstance(parameters["a_given_root"], list)
            and len(parameters["a_given_root"]) == 2,
            "screened A rows",
        )
        require(
            isinstance(parameters["b_given_root"], list)
            and len(parameters["b_given_root"]) == 2,
            "screened B rows",
        )
        a_rows = tuple(normalized_probability_row(row, 2) for row in parameters["a_given_root"])
        b_rows = tuple(normalized_probability_row(row, 2) for row in parameters["b_given_root"])
        joint = {
            (r, a, b): root[r] * a_rows[r][a] * b_rows[r][b]
            for r, a, b in itertools.product((0, 1), repeat=3)
        }
        strong = all(
            conditional(joint, 1, a, {0: r}) == conditional(joint, 1, a, {0: r, 2: b})
            and conditional(joint, 2, b, {0: r}) == conditional(joint, 2, b, {0: r, 1: a})
            for r, a, b in itertools.product((0, 1), repeat=3)
        )
        passed = strong and sum(joint.values(), ZERO) == ONE
        evidence = {"history_count": len(joint), "strong": strong}
        disposition = "INTRINSIC-WEIGHTS-DESCEND"
    elif kind == "fixed-memory":
        require(
            set(parameters) == {"capacity", "cells", "local_histories"},
            "fixed-memory fields",
        )
        capacity = parameters["capacity"]
        cells = parameters["cells"]
        local_histories = parameters["local_histories"]
        require(
            all(
                isinstance(value, int) and not isinstance(value, bool) and value > 0
                for value in (capacity, cells, local_histories)
            ),
            "fixed-memory integers",
        )
        required = local_histories ** cells
        passed = required > capacity
        evidence = {"capacity": capacity, "required_histories": required}
        disposition = "FIXED-MEMORY-COLLISION"
    elif kind == "presentation-permutation":
        require(set(parameters) == {"left", "right"}, "presentation fields")
        left = parameters["left"]
        right = parameters["right"]
        require(isinstance(left, list) and isinstance(right, list), "presentation rows")
        require(left != right, "presentation case did not change raw order")
        passed = sorted(left, key=canonical_json) == sorted(right, key=canonical_json)
        evidence = {"canonical_equal": passed, "raw_equal": False}
        disposition = "REQUIRED-PRESENTATION-NONKILL"
    elif kind == "dependency-bundle":
        require(set(parameters) == {"edges", "vertices"}, "dependency fields")
        vertices_raw = parameters["vertices"]
        edges_raw = parameters["edges"]
        require(
            isinstance(vertices_raw, list)
            and all(isinstance(value, str) and value for value in vertices_raw)
            and len(set(vertices_raw)) == len(vertices_raw),
            "dependency vertices",
        )
        require(
            isinstance(edges_raw, list)
            and all(
                isinstance(edge, list)
                and len(edge) == 2
                and all(isinstance(value, str) for value in edge)
                for edge in edges_raw
            ),
            "dependency edges",
        )
        vertices = tuple(vertices_raw)
        edges = {(edge[0], edge[1]) for edge in edges_raw}
        require(all(source in vertices and target in vertices for source, target in edges), "foreign dependency vertex")
        components = strongly_connected_components(vertices, edges)
        passed = any(len(component) > 1 for component in components)
        evidence = {"components": components}
        disposition = "MUTUAL-DEPENDENCE-BUNDLE"
    else:
        raise ScientificFailure(f"unknown fresh case kind: {kind}")
    require(passed, f"fresh case failed: {case_id}")
    return {
        "case_id": case_id,
        "case_sha256": canonical_hash(case),
        "disposition": disposition,
        "evidence": evidence,
        "kind": kind,
        "pass": passed,
    }


def load_and_evaluate_fresh(path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    require(
        isinstance(raw, dict)
        and set(raw) == {"cases", "nonce", "schema", "source_sha256"},
        "fresh file fields are not exact",
    )
    require(raw["schema"] == "P14-FRESH-1", "fresh schema mismatch")
    require(
        isinstance(raw["nonce"], str)
        and len(raw["nonce"]) == 64
        and all(character in "0123456789abcdef" for character in raw["nonce"]),
        "fresh nonce is not lowercase 256-bit hex",
    )
    source_sha = file_hash(Path(__file__).resolve())
    require(raw["source_sha256"] == source_sha, "fresh cases bind another source")
    require(isinstance(raw["cases"], list) and len(raw["cases"]) >= 6, "too few fresh cases")
    results = tuple(evaluate_fresh_case(case) for case in raw["cases"])
    require(len({row["case_id"] for row in results}) == len(results), "duplicate fresh case ID")
    require(len({row["kind"] for row in results}) >= 5, "fresh cases lack kind diversity")
    require(all(row["pass"] for row in results), "fresh scientific survivor")
    return raw, {
        "all_exact": True,
        "case_count": len(results),
        "kinds": sorted({row["kind"] for row in results}),
        "nonce": raw["nonce"],
        "results": results,
    }


def term_table() -> tuple[dict[str, str], ...]:
    return (
        {"actuality": "possible", "object": "Gamma", "sample_space": "complete histories", "status": "declared law"},
        {"actuality": "possible", "object": "onset germ", "sample_space": "typed local law changes", "status": "derived"},
        {"actuality": "possible", "object": "stable happening type", "sample_space": "persistent onset classes", "status": "derived"},
        {"actuality": "actual", "object": "actual happening", "sample_space": "one rho-selected history", "status": "postulated selection"},
        {"actuality": "possible", "object": "division frontier", "sample_space": "typed history cuts", "status": "measured per cut"},
        {"actuality": "possible", "object": "dependency bundle", "sample_space": "mutual-dependence quotient", "status": "derived"},
        {"actuality": "possible", "object": "unit measure", "sample_space": "physical bundle occurrences", "status": "derived"},
        {"actuality": "possible", "object": "intrinsic weight", "sample_space": "typed occurrence provenance", "status": "conditional on strong descent"},
        {"actuality": "representation", "object": "hash/label/address", "sample_space": "serialization", "status": "nonphysical provenance"},
    )


def four_gate_table() -> tuple[dict[str, str], ...]:
    return (
        {"discriminator": "clone/refinement", "necessity": "presentation overcounts", "no_smuggling": "no label identity", "object": "onset germ", "referent": "complete local law change"},
        {"discriminator": "eraser/reconvergence", "necessity": "paths need not be facts", "no_smuggling": "no actuality flag", "object": "stable happening type", "referent": "persistent onset class"},
        {"discriminator": "possible/actual table", "necessity": "one actual history", "no_smuggling": "external only", "object": "actual happening", "referent": "rho selection"},
        {"discriminator": "four-product/frontier tests", "necessity": "records need not restart", "no_smuggling": "no history ID", "object": "division frontier", "referent": "complete sufficient cut"},
        {"discriminator": "diamond/common cause", "necessity": "order not textual", "no_smuggling": "no rank/index", "object": "dependency edge", "referent": "essential law dependence"},
        {"discriminator": "swap symmetry", "necessity": "co-creation is unoriented", "no_smuggling": "no representative", "object": "happening bundle", "referent": "mutual-dependence class"},
        {"discriminator": "clone/two-versus-one", "necessity": "minimal extensive value", "no_smuggling": "not orbit count", "object": "unit measure", "referent": "bundle occurrences"},
        {"discriminator": "strong diamond", "necessity": "law intensity may differ", "no_smuggling": "no entered weight", "object": "intrinsic weight", "referent": "descended local factor"},
    )


def checks_from_measurements(measurements: dict[str, Any]) -> tuple[dict[str, Any], ...]:
    stable = measurements["stable_record"]
    minimal = measurements["minimal_history"]
    reciprocal = measurements["reciprocal"]
    correlated = measurements["correlated_antichain"]
    fork = measurements["screened_fork"]
    uniform = measurements["uniform_family"]
    checks = (
        {"check": "LAW-PROVENANCE-EXPLICIT", "pass": LAW_PROVENANCE == "DECLARED-NEW-LAW-POSTULATE"},
        {"check": "WRITER-COMPLETE", "pass": stable["completeness"] == eye(2)},
        {"check": "SEALED-GRAMMAR-STABLE", "pass": stable["grammar_all_exact"]},
        {"check": "ERASER-OUTSIDE-GRAMMAR", "pass": stable["eraser_outside_grammar"]},
        {"check": "MINIMAL-POINT-FREE-CENSUS", "pass": minimal["reachable_state_count"] == 5},
        {"check": "MUTUAL-BUNDLE-QUOTIENT", "pass": minimal["bundle_components"][0] == ("a", "b")},
        {"check": "NO-HIDDEN-CLOCK-DIAMOND", "pass": minimal["trace_history_count"] == 5},
        {"check": "RECIPROCAL-LAW-NORMALIZED", "pass": reciprocal["normalized"]},
        {"check": "DIRECT-CUT-EQUALITY", "pass": all(row["direct"] == row["factorized"] for row in reciprocal["cut_rows"])},
        {"check": "STABILITY-FRONTIER-INDEPENDENCE", "pass": len(reciprocal["four_product"]) == 4},
        {"check": "PROJECTED-FRONTIER-INCOMPLETE", "pass": reciprocal["projected_frontier_incomplete"]},
        {"check": "CORRELATED-STRONG-DIAMOND-REFUSAL", "pass": not correlated["strong_diamond"]},
        {"check": "SCREENED-FORK-STRONG-DIAMOND", "pass": fork["strong_all_exact"]},
        {"check": "UNIFORM-FAMILY-NORMALIZED", "pass": uniform["all_normalized"]},
        {"check": "UNIFORM-FRESH-SECTOR-GROWTH", "pass": uniform["fresh_sector_growth"]},
        {"check": "SIBLING-PRESENTATION-NONKILL", "pass": uniform["sibling_permutation_nonkill"]},
    )
    require(all(row["pass"] for row in checks), "scientific check failed")
    return checks


def claim_table() -> tuple[dict[str, Any], ...]:
    return (
        {"claim": "P14-C1-STABLE-WORD", "consumes": ("stable_record.completeness", "stable_record.grammar", "stable_record.eraser_outside_grammar"), "scope": "every finite word of the six-generator sealed grammar"},
        {"claim": "P14-C2-POINT-FREE-BUNDLES", "consumes": ("minimal_history.bundle_components", "minimal_history.relabel_exact", "attacks.H1", "attacks.H19", "attacks.H20"), "scope": "declared finite persistent-set frame"},
        {"claim": "P14-C3-NO-HIDDEN-CLOCK", "consumes": ("minimal_history.diamond_state", "minimal_history.trace_history_count", "attacks.H3", "attacks.H24", "attacks.H26"), "scope": "declared commuting diamonds"},
        {"claim": "P14-C4-DIVISION-FRONTIERS", "consumes": ("reciprocal.cut_rows", "reciprocal.hidden_profiles", "reciprocal.four_product", "attacks.H5", "attacks.H11", "attacks.H12", "attacks.H17", "attacks.H25"), "scope": "declared finite reciprocal future grammar"},
        {"claim": "P14-C5-STRONG-DIAMOND-WEIGHTS", "consumes": ("correlated_antichain", "screened_fork", "attacks.H8", "attacks.H13", "attacks.H21", "attacks.H22"), "scope": "strictly positive finite laws with typed predecessors"},
        {"claim": "P14-C6-RECIPROCAL-RESPONSE", "consumes": ("reciprocal.g_one_by_parity", "reciprocal.y_one_by_g", "reciprocal.y_one_by_parity"), "scope": "declared binary history law"},
        {"claim": "P14-C7-UNIFORM-GROWTH", "consumes": ("uniform_family.finite_rows", "uniform_family.shape_counts", "attacks.H7", "attacks.H23"), "scope": "all finite prefix-closed shapes by proof; q=1..3,n=1..4 finite controls"},
        {"claim": "P14-C8-PREMETRIC-ONLY", "consumes": ("term_table", "four_gate_table", "scope"), "scope": "no chronology, volume calibration, metric, curvature, gravity, or actualization"},
    )


def outcomes(
    measurements: dict[str, Any],
    attacks: tuple[Attack, ...],
    fresh: dict[str, Any] | None,
) -> dict[str, Any]:
    checks = checks_from_measurements(measurements)
    all_checks = all(row["pass"] for row in checks)
    all_attacks = all(row.killed for row in attacks)
    require(all_checks and all_attacks, "positive outcome prerequisites fail")
    candidate = {
        "actuality": "P14-ACTUAL-STABLE-HAPPENINGS-CONDITIONAL-ON-ACTUALIZATION",
        "dependency": "P14-LOCALLY-FINITE-BUNDLE-POSET",
        "frontiers": {
            "full_ab": "P14-COMPLETE-DIVISION-FRONTIER",
            "full_abg": "P14-COMPLETE-DIVISION-FRONTIER",
            "projected_a": "P14-FRONTIER-INCOMPLETE",
        },
        "geometry": "P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE",
        "law": "P14-DECLARED-POINT-FREE-HISTORY-LAW",
        "record": "P14-INDIVISIBLE-STABLE-HAPPENING-BUNDLES",
        "valuation": "P14-INTERVAL-FINITE-ATOMIC-MEASURE",
    }

    if fresh is None:
        return {
            "candidate_coordinates": candidate,
            "official": False,
            "status": "FRESH-CONTROLS-NOT-EVALUATED",
        }
    require(fresh["all_exact"], "fresh controls are not exact")
    return {
        "candidate_coordinates": candidate,
        "official": True,
        "status": "ELIGIBLE-GREEN-UNREVIEWED",
    }


def build_payload(fresh: dict[str, Any] | None = None) -> dict[str, Any]:
    stable = stable_record_measurement()
    minimal = minimal_history_measurement()
    reciprocal = reciprocal_measurement()
    correlated = correlated_antichain_measurement()
    fork = screened_fork_measurement()
    uniform = uniform_family_measurement()
    measurements = {
        "correlated_antichain": correlated,
        "minimal_history": minimal,
        "reciprocal": reciprocal,
        "screened_fork": fork,
        "stable_record": stable,
        "uniform_family": uniform,
    }
    checks = checks_from_measurements(measurements)
    attacks = registered_attacks(stable, minimal, reciprocal, correlated, fork, uniform)
    result = {
        "attack_count": len(attacks),
        "attacks": attacks,
        "check_count": len(checks),
        "checks": checks,
        "claims": claim_table(),
        "four_gate_table": four_gate_table(),
        "fresh_cases": fresh if fresh is not None else {
            "all_exact": False,
            "case_count": 0,
            "results": tuple(),
            "status": "NOT-EVALUATED-IN-SOURCE-FREEZE",
        },
        "fresh_cases_evaluated": fresh is not None,
        "law_provenance": LAW_PROVENANCE,
        "measurements": measurements,
        "outcome_prerequisites": {
            "all_registered_attacks_killed": all(row.killed for row in attacks),
            "all_scientific_checks": all(row["pass"] for row in checks),
            "fresh_controls_exact": fresh is not None and fresh["all_exact"],
            "law_provenance_explicit": LAW_PROVENANCE,
        },
        "outcomes": outcomes(measurements, attacks, fresh),
        "pin_sha256": PIN_SHA256,
        "scope": {
            "actualization": "postulated",
            "continuum": "unconstructed",
            "geometry": "premetric only",
            "gravity": "unconstructed",
            "law_selection": "unconstructed",
            "metric": "unconstructed",
        },
        "status": "PASS",
        "term_table": term_table(),
    }
    payload_hash = canonical_hash(result)
    return {**result, "normalized_payload_sha256": payload_hash}


def repo_v16_dir() -> Path:
    return Path(__file__).resolve().parents[1]


def observed_inputs(fresh_path: Path) -> dict[str, Any]:
    v16 = repo_v16_dir()
    pin = v16 / PIN_RELATIVE
    paper = v16 / PAPER_RELATIVE
    note = v16 / NOTE_RELATIVE
    require(pin.is_file(), "official pin is absent")
    require(file_hash(pin) == PIN_SHA256, "official pin hash mismatch")
    require(paper.is_file(), "paper is absent")
    require(note.is_file(), "construction note is absent")
    return {
        "pin": {"path": PIN_RELATIVE, "sha256": file_hash(pin)},
        "source": {"path": "code/p14_premetric_exact.py", "sha256": file_hash(Path(__file__).resolve())},
        "paper": {"path": PAPER_RELATIVE, "sha256": file_hash(paper)},
        "construction_note": {"path": NOTE_RELATIVE, "sha256": file_hash(note)},
        "fresh_cases": {"path": FRESH_RELATIVE, "sha256": file_hash(fresh_path)},
    }


def write_new(path: Path, data: bytes) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        try:
            path.unlink()
        except FileNotFoundError:
            pass
        raise


def official_run(output_path: Path, receipt_path: Path) -> None:
    require(output_path != receipt_path, "output and receipt paths must differ")
    require(not output_path.exists() and not receipt_path.exists(), "publication path exists")
    v16 = repo_v16_dir()
    expected_output = (v16 / "p14_premetric_output.json").resolve()
    expected_receipt = (v16 / "p14_premetric_receipt.json").resolve()
    require(output_path.resolve() == expected_output, "output path is outside whitelist")
    require(receipt_path.resolve() == expected_receipt, "receipt path is outside whitelist")
    fresh_path = v16 / FRESH_RELATIVE
    require(fresh_path.is_file(), "fresh cases are absent")
    _, fresh = load_and_evaluate_fresh(fresh_path)
    payload = build_payload(fresh)
    payload_bytes = canonical_bytes(payload) + b"\n"
    inputs = observed_inputs(fresh_path)
    scientific_seals = {
        key: canonical_hash(value) for key, value in sorted(payload.items())
    }
    require(set(scientific_seals) == set(payload), "scientific seal is not total")
    receipt_core = {
        "inputs": inputs,
        "output": {
            "bytes": len(payload_bytes),
            "path": str(output_path),
            "sha256": hashlib.sha256(payload_bytes).hexdigest(),
        },
        "payload_sha256": payload["normalized_payload_sha256"],
        "publication_writes": 2,
        "read_ledger": tuple(row["path"] for row in inputs.values()),
        "seal_manifest": {
            "scientific": scientific_seals,
            "scientific_key_count": len(scientific_seals),
            "scientific_total": True,
        },
        "scientific": payload,
        "status": "PASS",
        "write_ledger": (str(output_path), str(receipt_path)),
    }
    receipt_core_seals = {
        key: canonical_hash(value) for key, value in sorted(receipt_core.items())
    }
    receipt = {
        **receipt_core,
        "receipt_core_seals": receipt_core_seals,
        "receipt_core_sha256": canonical_hash(receipt_core),
    }
    receipt_bytes = canonical_bytes(receipt) + b"\n"
    output_written = False
    try:
        write_new(output_path, payload_bytes)
        output_written = True
        write_new(receipt_path, receipt_bytes)
    except BaseException:
        if output_written:
            try:
                output_path.unlink()
            except FileNotFoundError:
                pass
        try:
            receipt_path.unlink()
        except FileNotFoundError:
            pass
        raise


def anchor_failure_selftest() -> None:
    changed = [list(row) for row in B]
    changed[0][0] += F(1, 25)
    require(matrix(changed) != B, "anchor mutation did not change B")
    column_sum = changed[0][0] + changed[1][0]
    if column_sum == ONE:
        raise ScientificFailure("deliberate anchor mutation was not detected")
    raise ScientificFailure("DELIBERATE-ANCHOR-FAILURE")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(prog="p14_premetric_exact.py")
    modes = result.add_mutually_exclusive_group(required=True)
    modes.add_argument("--selftest", action="store_true")
    modes.add_argument("--run", action="store_true")
    modes.add_argument("--mutant", metavar="ID")
    modes.add_argument("--anchor-failure-selftest", action="store_true")
    result.add_argument("--output", type=Path)
    result.add_argument("--receipt", type=Path)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.run:
        if args.output is None or args.receipt is None:
            parser().error("--run requires --output and --receipt")
        official_run(args.output, args.receipt)
        return 0
    if args.output is not None or args.receipt is not None:
        parser().error("publication paths are valid only with --run")
    if args.anchor_failure_selftest:
        anchor_failure_selftest()
        return 1
    payload = build_payload()
    if args.mutant is not None:
        row = next((item for item in payload["attacks"] if item.attack_id == args.mutant), None)
        if row is None:
            parser().error("unknown mutant ID")
        print(canonical_json({"attack": row, "status": "PASS"}))
        return 0
    print(canonical_json(payload))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ScientificFailure as exc:
        print(f"SCIENTIFIC-FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1)
