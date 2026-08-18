#!/usr/bin/env python3
"""Exact physical scorer and renderer for PPR / v16 Paper 3.

The scorer consumes the separately frozen, data-only fixture.  It does not
contain an expected primary verdict.  All substantive arithmetic is exact over
Q(i), and the paper, transcript, and receipt are promoted only after every
gate and the total seal check pass.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from fractions import Fraction
from pathlib import Path
from typing import Mapping, Sequence

from ppr_core import (
    GQ,
    I,
    ONE,
    ZERO,
    Continuation,
    GateFailure,
    add,
    basis_vector,
    class_operator,
    completeness_operator,
    dagger,
    identity,
    instrument_equal,
    inverse,
    is_complete,
    is_zero_matrix,
    kernel,
    matrices_equal,
    matrix,
    matrix_text,
    multiply,
    partition_census,
    partition_is_stable,
    path_transport,
    pullback,
    scale,
    set_partitions,
    shape,
    stable_null_family,
    superoperator,
    tensor,
    transpose,
    vector_probability,
    zeros,
)


HERE = Path(__file__).resolve().parent
V16 = HERE.parent
ROOT = V16.parent
FIXTURE_PATH = HERE / "ppr_fixture.json"
CORE_PATH = HERE / "ppr_core.py"
PIN_PATH = V16 / "note-ppr-pin.md"
DEFAULT_OUTPUT = HERE / "ppr_output.txt"
DEFAULT_RECEIPT = HERE / "ppr_receipt.json"
DEFAULT_PAPER = V16 / "paper-03-contextual-pullbacks-permanent-records.md"

FIXTURE_SHA256 = "cecc3b0d3c7bf46503481fa7b422e915ba0ff6aac42e3cec5f61c395e565b389"
CORE_SHA256 = "490668340b08022ac5d11c8fdc07c392739153b609a72b9bda5bfcf112f472ea"
PIN_SHA256 = "cce2e194f1f1c557e2cb1745c0f15b9feaa98b48b2300126970098da0fadd48f"
PIN_COMMIT = "828b510a3229ae6330a55520b676a33e031c77a8"
BASE_COMMIT = "7e95322c589a42211e3a10cab7655492014bd0ae"

MUTANTS = (
    "anchor-corrupt",
    "event-mix",
    "split-weight",
    "kraus-promote",
    "pullback-half",
    "dark-reactivate-drop",
    "null-promote",
    "eraser-ignore",
    "record-preplant",
    "comparison-phase",
    "transport-flatten",
    "loop-conflate",
    "graph-copy",
    "graph-erase",
    "probe-feedforward",
    "spectator-couple",
    "completeness-amplify",
    "result-count-type",
    "verdict-flip",
    "seal-after-write",
)


class Gates:
    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []

    def check(self, name: str, condition: bool, detail: object, falsifier: str) -> None:
        row = {
            "name": name,
            "pass": bool(condition),
            "detail": detail,
            "falsifier": falsifier,
        }
        self.rows.append(row)
        if not condition:
            raise GateFailure(name)


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def seal_mapping(value: Mapping[str, object]) -> dict[str, str]:
    return {
        key: hashlib.sha256(canonical_json(value[key]).encode("utf-8")).hexdigest()
        for key in sorted(value)
    }


def parse_matrix(value: Sequence[Sequence[object]]) -> list[list[GQ]]:
    return matrix(value)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def scalar_text(value: GQ) -> str:
    return value.text()


def parse_outcome_labels(pin_text: str) -> tuple[str, ...]:
    section = pin_text.split("## Pre-registered primary outcomes", 1)[1]
    section = section.split("## Kill conditions", 1)[0]
    labels = tuple(
        match.group(1)
        for line in section.splitlines()
        if (match := re.match(r"^\d+\. `([^`]+)`", line))
    )
    if len(labels) != 10 or len(set(labels)) != len(labels):
        raise GateFailure("PPR-OUTCOME-PARSE")
    return labels


def outer(vector: list[list[GQ]]) -> list[list[GQ]]:
    return multiply(vector, dagger(vector))


def trace(value: list[list[GQ]]) -> GQ:
    if not value or len(value) != len(value[0]):
        raise ValueError("trace needs a square matrix")
    return sum((value[index][index] for index in range(len(value))), ZERO)


def density_probability(operator: list[list[GQ]], rho: list[list[GQ]]) -> Fraction:
    value = trace(multiply(multiply(operator, rho), dagger(operator)))
    if value.im != 0:
        raise ValueError("probability was not real")
    return value.re


def row_operator(operator: list[list[GQ]], row: int) -> list[list[GQ]]:
    return [operator[row][:]]


def cross_operator(
    left: list[list[GQ]], right: list[list[GQ]], left_weight: GQ, right_weight: GQ
) -> list[list[GQ]]:
    coefficient = left_weight.conjugate() * right_weight
    first = scale(coefficient, multiply(dagger(left), right))
    return add(first, dagger(first))


def purity(rho: list[list[GQ]]) -> Fraction:
    value = trace(multiply(rho, rho))
    if value.im != 0:
        raise ValueError("purity was not real")
    return value.re


def partial_trace_first(rho: list[list[GQ]], first_dim: int, second_dim: int) -> list[list[GQ]]:
    if shape(rho) != (first_dim * second_dim, first_dim * second_dim):
        raise ValueError("partial trace shape mismatch")
    out = zeros(second_dim, second_dim)
    for left in range(second_dim):
        for right in range(second_dim):
            out[left][right] = sum(
                (
                    rho[first * second_dim + left][first * second_dim + right]
                    for first in range(first_dim)
                ),
                ZERO,
            )
    return out


def local_instrument_bob_marginal(
    kraus: Sequence[list[list[GQ]]], bell_rho: list[list[GQ]]
) -> list[list[GQ]]:
    out = zeros(2, 2)
    for operator in kraus:
        lifted = tensor(operator, identity(2))
        evolved = multiply(multiply(lifted, bell_rho), dagger(lifted))
        out = add(out, partial_trace_first(evolved, len(operator), 2))
    return out


def bell_density() -> list[list[GQ]]:
    half = GQ(Fraction(1, 2))
    out = zeros(4, 4)
    for left in (0, 3):
        for right in (0, 3):
            out[left][right] = half
    return out


def co_live_pairs(first_leg: list[list[GQ]]) -> tuple[tuple[int, int], ...]:
    pairs: set[tuple[int, int]] = set()
    for column in range(len(first_leg[0])):
        support = [row for row in range(len(first_leg)) if not first_leg[row][column].is_zero()]
        for left_index, left in enumerate(support):
            for right in support[left_index + 1 :]:
                pairs.add((left, right))
    return tuple(sorted(pairs))


def co_merge_partition(future: list[list[GQ]]) -> tuple[tuple[int, ...], ...]:
    size = len(future[0])
    parent = list(range(size))

    def find(item: int) -> int:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for row in future:
        support = [index for index, item in enumerate(row) if not item.is_zero()]
        for item in support[1:]:
            union(support[0], item)
    groups: dict[int, list[int]] = {}
    for item in range(size):
        groups.setdefault(find(item), []).append(item)
    return tuple(sorted((tuple(group) for group in groups.values()), key=lambda block: block[0]))


def record_available(first_leg: list[list[GQ]], future: list[list[GQ]]) -> tuple[bool, object]:
    live = co_live_pairs(first_leg)
    partition = co_merge_partition(future)
    membership = {item: block for block, items in enumerate(partition) for item in items}
    separated = all(membership[left] != membership[right] for left, right in live)
    return separated, {"co_live_pairs": live, "co_merge_partition": partition}


def bell_number(size: int) -> int:
    row = [1]
    for level in range(1, size + 1):
        next_row = [row[-1]]
        for index in range(1, level + 1):
            next_row.append(next_row[-1] + row[index - 1])
        row = next_row
    return row[0]


def graph_signature(branch: Mapping[str, object]) -> tuple[object, ...]:
    vertices = tuple(branch["vertices"])
    edges = tuple(tuple(edge) for edge in branch["edges"])
    degrees = {vertex: 0 for vertex in vertices}
    for source, target, _ in edges:
        degrees[source] += 1
        degrees[target] += 1
    path_labels = tuple(edge[2] for edge in edges)
    return (
        branch["carrier_dimension"],
        len(vertices),
        tuple(sorted(degrees.values())),
        path_labels,
    )


def edge_operator_map(
    edges: Sequence[Sequence[str]], matrices: Mapping[str, list[list[GQ]]]
) -> dict[tuple[str, str], list[list[GQ]]]:
    return {(source, target): matrices[name] for source, target, name in edges}


def renamed_branch(branch: Mapping[str, object], rename: Mapping[str, str]) -> dict[str, object]:
    return {
        "name": branch["name"],
        "record_label": branch["record_label"],
        "carrier_dimension": branch["carrier_dimension"],
        "vertices": [rename.get(vertex, vertex) for vertex in branch["vertices"]],
        "edges": [
            [rename.get(source, source), rename.get(target, target), name]
            for source, target, name in branch["edges"]
        ],
        "probe_path": [rename.get(vertex, vertex) for vertex in branch["probe_path"]],
    }


def branch_transport(
    branch: Mapping[str, object], matrices: Mapping[str, list[list[GQ]]]
) -> list[list[GQ]]:
    return path_transport(branch["probe_path"], edge_operator_map(branch["edges"], matrices))


def matrix_key(value: list[list[GQ]]) -> str:
    return canonical_json(matrix_text(value))


def apply_mutation(fixture: dict[str, object], mutant: str | None) -> dict[str, object]:
    changed = copy.deepcopy(fixture)
    if mutant == "event-mix":
        alpha = copy.deepcopy(changed["relational_wedge"]["branches"][0])
        alpha["name"] = "beta"
        changed["relational_wedge"]["branches"][1] = alpha
    elif mutant == "split-weight":
        changed.setdefault("mutation_controls", {})["split_second"] = "1/5"
    elif mutant == "kraus-promote":
        changed.setdefault("mutation_controls", {})["promote_kraus"] = true_value()
    elif mutant == "pullback-half":
        changed.setdefault("mutation_controls", {})["pullback_scale"] = "1/2"
    elif mutant == "dark-reactivate-drop":
        changed["stable_null"]["continuations"] = changed["stable_null"]["continuations"][:1]
    elif mutant == "null-promote":
        changed.setdefault("mutation_controls", {})["report_present_null"] = true_value()
    elif mutant == "eraser-ignore":
        support = changed["record_cases"]["support_record"]
        support["erasing_future"] = copy.deepcopy(support["preserving_future"])
    elif mutant == "record-preplant":
        changed.setdefault("mutation_controls", {})["plant_record"] = true_value()
    elif mutant == "comparison-phase":
        changed["comparison_diagram"]["edges"]["03"] = "NEG_RZ"
    elif mutant == "transport-flatten":
        changed["dynamical_loop"]["nonflat_phase"] = "I2"
    elif mutant == "loop-conflate":
        changed.setdefault("mutation_controls", {})["same_loop_type"] = true_value()
    elif mutant == "graph-copy":
        alpha = changed["relational_wedge"]["branches"][0]
        beta = changed["relational_wedge"]["branches"][1]
        beta["vertices"] = copy.deepcopy(alpha["vertices"])
        beta["edges"] = copy.deepcopy(alpha["edges"])
        beta["probe_path"] = copy.deepcopy(alpha["probe_path"])
        beta["carrier_dimension"] = alpha["carrier_dimension"]
    elif mutant == "graph-erase":
        changed["relational_wedge"]["branches"][1]["record_label"] = "beta-record"
    elif mutant == "probe-feedforward":
        changed.setdefault("mutation_controls", {})["reported_beta"] = "R"
    elif mutant == "spectator-couple":
        changed.setdefault("mutation_controls", {})["beta_spectator"] = "I2"
    elif mutant == "completeness-amplify":
        changed["no_signalling"]["amplifier"] = "2"
        changed.setdefault("mutation_controls", {})["use_amplifier_as_law"] = true_value()
    elif mutant == "result-count-type":
        changed.setdefault("mutation_controls", {})["count_as_text"] = true_value()
    elif mutant == "verdict-flip":
        changed.setdefault("mutation_controls", {})["flip_builder"] = true_value()
    elif mutant == "seal-after-write":
        changed.setdefault("mutation_controls", {})["tamper_after_seal"] = true_value()
    return changed


def true_value() -> bool:
    return bool(ONE == GQ(1))


def resolve_matrices(fixture: Mapping[str, object]) -> dict[str, list[list[GQ]]]:
    values = {name: parse_matrix(rows) for name, rows in fixture["matrices"].items()}
    values["RZ"] = multiply(values["R"], values["Z"])
    values["NEG_RZ"] = scale(-1, values["RZ"])
    return values


def comparison_path(
    path: Sequence[str], edges: Mapping[str, list[list[GQ]]]
) -> list[list[GQ]]:
    out = identity(len(next(iter(edges.values()))))
    for name in path:
        out = multiply(edges[name], out)
    return out


def gauge_comparison_edges(
    edges: Mapping[str, list[list[GQ]]], frames: Mapping[str, list[list[GQ]]]
) -> dict[str, list[list[GQ]]]:
    out: dict[str, list[list[GQ]]] = {}
    for name, operator in edges.items():
        source, target = name[0], name[1]
        out[name] = multiply(frames[target], multiply(operator, inverse(frames[source])))
    return out


def stable_partition_payload(census: object) -> dict[str, object]:
    return {
        "all_count": census.all_count,
        "stable": census.stable,
        "finest": census.finest,
    }


def analyse(fixture: dict[str, object], mutant: str | None) -> tuple[dict[str, object], Gates]:
    gates = Gates()
    source_sha = sha256_path(Path(__file__).resolve())
    fixture_observed = sha256_path(FIXTURE_PATH)
    if mutant == "anchor-corrupt":
        fixture_observed = hashlib.sha256((fixture_observed + "!").encode("ascii")).hexdigest()
    pin_text = PIN_PATH.read_text(encoding="utf-8")
    labels = parse_outcome_labels(pin_text)
    gates.check(
        "PPR-ANCHORS",
        fixture_observed == FIXTURE_SHA256
        and sha256_path(CORE_PATH) == CORE_SHA256
        and sha256_path(PIN_PATH) == PIN_SHA256
        and fixture["anchors"]["core_sha256"] == CORE_SHA256
        and fixture["anchors"]["pin_sha256"] == PIN_SHA256
        and fixture["anchors"]["pin_commit"] == PIN_COMMIT
        and fixture["anchors"]["base_commit"] == BASE_COMMIT,
        {
            "fixture": fixture_observed,
            "core": sha256_path(CORE_PATH),
            "pin": sha256_path(PIN_PATH),
            "pin_commit": fixture["anchors"]["pin_commit"],
            "base_commit": fixture["anchors"]["base_commit"],
        },
        "anchor-corrupt",
    )
    gates.check(
        "PPR-OUTCOME-VOCABULARY",
        len(labels) == 10 and all(label.startswith("PPR-") for label in labels),
        {"count": len(labels), "labels_sha256": hashlib.sha256("\n".join(labels).encode()).hexdigest()},
        "anchor-corrupt",
    )

    matrices = resolve_matrices(fixture)
    controls = fixture.get("mutation_controls", {})
    a = GQ(fixture["scalars"]["a"])
    b = GQ(fixture["scalars"]["b"])
    mu = GQ(fixture["scalars"]["mu"])
    nu = GQ(fixture["scalars"]["nu"])
    rho0 = outer(basis_vector(2, 0))

    wedge = fixture["relational_wedge"]
    branches = wedge["branches"]
    signatures = [graph_signature(branch) for branch in branches]
    distinct_events = signatures[0] != signatures[1]
    renamed = [renamed_branch(branch, wedge["rename"]) for branch in branches]
    relabel_covariant = all(
        graph_signature(branches[index]) == graph_signature(renamed[index])
        for index in range(len(branches))
    )
    unsplit = class_operator([(a, matrices["I2"]), (b, matrices["J"])])
    split_second = GQ(controls.get("split_second", "2/5"))
    split = class_operator(
        [(GQ("1/5"), matrices["I2"]), (split_second, matrices["I2"]), (b, matrices["J"])]
    )
    first_kraus = [scale(a, matrices["I2"]), scale(b, matrices["Z"])]
    rotated_kraus = [
        add(scale(a, first_kraus[0]), scale(b, first_kraus[1])),
        add(scale(-b, first_kraus[0]), scale(a, first_kraus[1])),
    ]
    if controls.get("promote_kraus"):
        rotated_kraus = copy.deepcopy(first_kraus)
    same_channel = superoperator(first_kraus) == superoperator(rotated_kraus)
    same_instrument = instrument_equal(
        [[first_kraus[0]], [first_kraus[1]]],
        [[rotated_kraus[0]], [rotated_kraus[1]]],
    )
    gates.check(
        "PPR-EVENT-ALGEBRA",
        distinct_events and relabel_covariant,
        {"distinct_relational_events": distinct_events, "relabel_covariant": relabel_covariant},
        "event-mix",
    )
    gates.check(
        "PPR-HISTORY-REFINEMENT",
        unsplit == split,
        {"unsplit": matrix_text(unsplit), "split": matrix_text(split)},
        "split-weight",
    )
    gates.check(
        "PPR-CHANNEL-INSTRUMENT-QUOTIENT",
        is_complete(first_kraus)
        and is_complete(rotated_kraus)
        and same_channel
        and not same_instrument
        and distinct_events,
        {
            "same_unconditioned_channel": same_channel,
            "same_record_instrument": same_instrument,
            "relational_events_distinct": distinct_events,
        },
        "kraus-promote",
    )
    event_payload = {
        "relational_signatures": signatures,
        "relabel_covariant": relabel_covariant,
        "history_split_merge_equal": unsplit == split,
        "kraus": {
            "same_unconditioned_channel": same_channel,
            "different_calibrated_instrument": not same_instrument,
            "arbitrary_kraus_rotation_is_event_gauge": False,
        },
    }

    null_fixture = fixture["stable_null"]
    dimensions = {name: int(value) for name, value in null_fixture["dimensions"].items()}
    observations = {
        name: parse_matrix(value) for name, value in null_fixture["observations"].items()
    }
    continuations = [
        Continuation(
            item["name"], item["source"], item["target"], parse_matrix(item["operator"])
        )
        for item in null_fixture["continuations"]
    ]
    stable = stable_null_family(dimensions, observations, continuations)
    present_cut = kernel(observations["cut"], ncols=dimensions["cut"])
    reported_cut = present_cut if controls.get("report_present_null") else stable.bases["cut"]
    delayed = multiply(observations["final"], multiply(continuations[-1].operator, continuations[0].operator)) if len(continuations) == 2 else zeros(1, 4)
    e1 = basis_vector(4, 1)
    e2 = basis_vector(4, 2)
    e3 = basis_vector(4, 3)
    current_invisible = is_zero_matrix(multiply(observations["cut"], e1))
    delayed_visible = not is_zero_matrix(multiply(delayed, e1))
    permanent_controls = all(
        is_zero_matrix(multiply(test, e3))
        for test in (observations["cut"], delayed)
    )
    current_second_stays_dark = is_zero_matrix(multiply(delayed, e2))
    gates.check(
        "PPR-STABLE-NULL-DESCENT",
        stable.strict_rounds == 2
        and shape(present_cut) == (4, 3)
        and shape(stable.bases["cut"]) == (4, 2)
        and reported_cut == stable.bases["cut"],
        {
            "rank_history": [dict(row) for row in stable.rank_history],
            "strict_rounds": stable.strict_rounds,
            "present_cut_basis": matrix_text(present_cut),
            "stable_cut_basis": matrix_text(reported_cut),
        },
        "dark-reactivate-drop / null-promote",
    )
    gates.check(
        "PPR-DELAYED-REACTIVATION",
        current_invisible and delayed_visible and current_second_stays_dark and permanent_controls,
        {
            "e1_presently_invisible": current_invisible,
            "e1_later_visible": delayed_visible,
            "e2_later_invisible": current_second_stays_dark,
            "e3_all_registered_contexts_invisible": permanent_controls,
        },
        "dark-reactivate-drop",
    )
    descended = {
        edge.name: matrix_text(__import__("ppr_core").descended_quotient_map(edge, stable))
        for edge in continuations
    }
    null_payload = {
        "rank_history": [dict(row) for row in stable.rank_history],
        "strict_rounds": stable.strict_rounds,
        "present_cut_dimension": len(present_cut[0]),
        "stable_cut_dimension": len(stable.bases["cut"][0]),
        "stable_cut_basis": matrix_text(stable.bases["cut"]),
        "delayed_reactivation": {"e1": delayed_visible, "e2": False, "e3": False},
        "descended_maps": descended,
    }

    ua = matrices["Ualpha"]
    ub = matrices["Ubeta"]
    vgrow = matrices["Vgrow"]
    right_reached = multiply(ub, vgrow)
    derived = pullback(ua, ub)
    displayed = scale(controls.get("pullback_scale", "1"), derived)
    direct_reached = multiply(dagger(ua), right_reached)
    through_reached = multiply(displayed, vgrow)
    reached_pairs = 0
    pairwise = True
    for left_index in range(2):
        for right_index in range(2):
            reached_pairs += 1
            direct = multiply(
                dagger(multiply(ua, basis_vector(2, left_index))),
                multiply(right_reached, basis_vector(2, right_index)),
            )
            through = multiply(
                dagger(basis_vector(2, left_index)),
                multiply(through_reached, basis_vector(2, right_index)),
            )
            pairwise = pairwise and direct == through
    presently_unfed = matrix([["4/5"], ["0"], ["-3/5"]])
    unfed_now = is_zero_matrix(multiply(dagger(vgrow), presently_unfed))
    visible_later = not is_zero_matrix(multiply(ub, presently_unfed))
    gates.check(
        "PPR-HETEROGENEOUS-PULLBACK",
        shape(ua) == (3, 2)
        and shape(ub) == (3, 3)
        and shape(vgrow) == (3, 2)
        and pairwise
        and direct_reached == through_reached,
        {
            "left_shape": shape(ua),
            "right_shape": shape(ub),
            "growth_shape": shape(vgrow),
            "reached_basis_pairs": reached_pairs,
            "pullback": matrix_text(displayed),
        },
        "pullback-half",
    )
    gates.check(
        "PPR-ONE-STEP-DARK-NOT-GAUGE",
        unfed_now and visible_later,
        {"unfed_by_growth": unfed_now, "visible_to_future": visible_later},
        "dark-reactivate-drop",
    )
    pullback_payload = {
        "heterogeneous_shapes": {"left": shape(ua), "right": shape(ub), "growth": shape(vgrow)},
        "pullback": matrix_text(derived),
        "reached_basis_pairs_checked": reached_pairs,
        "direct_equals_pullback": pairwise,
        "one_step_unfed_future_visible": visible_later,
        "interpretation": "context-indexed Gram pullback on reached quotient subspaces",
    }

    uav = ua
    ubv = right_reached
    coherent_class = class_operator([(a, uav), (b, ubv)])
    coherent_complete = multiply(dagger(coherent_class), coherent_class) == identity(2)
    coherent_p0 = density_probability(row_operator(coherent_class, 0), rho0)
    decoherent_p0 = (
        a.abs2() * density_probability(row_operator(uav, 0), rho0)
        + b.abs2() * density_probability(row_operator(ubv, 0), rho0)
    )
    cross0 = cross_operator(row_operator(uav, 0), row_operator(ubv, 0), a, b)
    cross1 = cross_operator(row_operator(uav, 1), row_operator(ubv, 1), a, b)
    cross_sum = add(cross0, cross1)

    iz = scale(I, matrices["Z"])
    sm = multiply(multiply(matrices["R"], iz), matrices["Mdiag"])
    ta = [matrices["R"][0][:], matrices["R"][1][:], [ZERO, ZERO]]
    tb = [sm[0][:], sm[1][:], [b, ZERO]]
    dangling = class_operator([(a, ta), (b, tb)])
    dangling_complete = multiply(dagger(dangling), dangling) == identity(2)
    dangling_cross = cross_operator(ta, tb, a, b)
    dangling_record_probability = density_probability(row_operator(scale(b, tb), 2), rho0)

    ta4 = [matrices["R"][0][:], matrices["R"][1][:], [ZERO, ZERO], [ZERO, ZERO]]
    rj = multiply(matrices["R"], matrices["J"])
    coherent_rows = scale(mu, rj)
    tag_rows = scale(nu, matrices["I2"])
    tb4 = [coherent_rows[0][:], coherent_rows[1][:], tag_rows[0][:], tag_rows[1][:]]
    partial_class = class_operator([(a, ta4), (b, tb4)])
    partial_complete = multiply(dagger(partial_class), partial_class) == identity(2)
    partial_coherent = density_probability(row_operator(partial_class, 0), rho0)
    partial_decoherent = (
        a.abs2() * density_probability(row_operator(ta4, 0), rho0)
        + b.abs2() * density_probability(row_operator(tb4, 0), rho0)
    )
    partial_difference = abs(partial_coherent - partial_decoherent)
    partial_coefficient = partial_difference / mu.re

    one_class = class_operator([(a, matrices["I2"]), (b, matrices["J"])])
    one_total = density_probability(one_class, rho0)
    one_probe_coherent = density_probability(multiply(matrices["Qplus"], one_class), rho0)
    one_probe_decoherent = (
        a.abs2() * density_probability(matrices["Qplus"], rho0)
        + b.abs2() * density_probability(multiply(matrices["Qplus"], matrices["J"]), rho0)
    )
    gates.check(
        "PPR-INTERFERENCE-REDISTRIBUTION",
        coherent_complete
        and coherent_p0 != decoherent_p0
        and not is_zero_matrix(cross0)
        and not is_zero_matrix(cross1)
        and is_zero_matrix(cross_sum),
        {
            "coherent_p0": fraction_text(coherent_p0),
            "decohered_p0": fraction_text(decoherent_p0),
            "cross0": matrix_text(cross0),
            "cross1": matrix_text(cross1),
            "cross_sum": matrix_text(cross_sum),
        },
        "transport-flatten",
    )
    gates.check(
        "PPR-DANGLING-RECORD",
        dangling_complete
        and is_zero_matrix(dangling_cross)
        and dangling_record_probability == b.abs2() * b.abs2(),
        {
            "complete": dangling_complete,
            "cross_operator": matrix_text(dangling_cross),
            "record_probability": fraction_text(dangling_record_probability),
        },
        "completeness-amplify",
    )
    gates.check(
        "PPR-PARTIAL-OVERLAP",
        partial_complete
        and partial_difference != 0
        and partial_coefficient == Fraction(288, 625),
        {
            "mu": scalar_text(mu),
            "coherent_p0": fraction_text(partial_coherent),
            "decohered_p0": fraction_text(partial_decoherent),
            "absolute_difference": fraction_text(partial_difference),
            "difference_over_mu": fraction_text(partial_coefficient),
        },
        "transport-flatten",
    )
    gates.check(
        "PPR-ONE-OUTCOME-CONTROL",
        one_total == 1 and one_probe_coherent != one_probe_decoherent,
        {
            "total_probability": fraction_text(one_total),
            "later_probe_coherent": fraction_text(one_probe_coherent),
            "later_probe_decoherent": fraction_text(one_probe_decoherent),
        },
        "loop-conflate",
    )

    record_fixture = fixture["record_cases"]
    support = record_fixture["support_record"]
    first_leg = parse_matrix(support["first_leg"])
    preserving = parse_matrix(support["preserving_future"])
    erasing = parse_matrix(support["erasing_future"])
    preserved_record, preserved_detail = record_available(first_leg, preserving)
    erased_record, erased_detail = record_available(first_leg, erasing)

    tagged = matrix([[a], [ZERO], [ZERO], [b]])
    screen = matrix(
        [
            [a, ZERO, b, ZERO],
            [ZERO, a, ZERO, b],
            [-b, ZERO, a, ZERO],
            [ZERO, -b, ZERO, a],
        ]
    )
    untagger = matrix(
        [[ONE, ZERO, ZERO, ZERO], [ZERO, ONE, ZERO, ZERO], [ZERO, ZERO, ZERO, ONE], [ZERO, ZERO, ONE, ZERO]]
    )
    tagged_screen = multiply(screen, tagged)
    erased_screen = multiply(screen, multiply(untagger, tagged))
    tagged_path0 = vector_probability(matrix([[tagged_screen[0][0]], [tagged_screen[1][0]]]))
    erased_path0 = vector_probability(matrix([[erased_screen[0][0]], [erased_screen[1][0]]]))

    census_payload: dict[str, object] = {}
    census_objects: dict[str, object] = {}
    for name in ("block_record", "erasable_tag", "coherent_pair", "multiple_maximal"):
        item = record_fixture[name]
        census = partition_census(
            parse_matrix(item["decoherence"]),
            [parse_matrix(value) for value in item["continuations"]],
        )
        census_objects[name] = census
        census_payload[name] = stable_partition_payload(census)
    if controls.get("plant_record"):
        census_payload["erasable_tag"]["finest"] = (((0,), (1,)),)
    if controls.get("count_as_text"):
        census_payload["block_record"]["all_count"] = str(census_payload["block_record"]["all_count"])
    block = census_objects["block_record"]
    erasable_aux = census_objects["erasable_tag"]
    coherent_aux = census_objects["coherent_pair"]
    multiple = census_objects["multiple_maximal"]
    reported_partitions_valid = True
    for name in ("block_record", "erasable_tag", "coherent_pair", "multiple_maximal"):
        item = record_fixture[name]
        decoherence = parse_matrix(item["decoherence"])
        continuations_for_record = [parse_matrix(value) for value in item["continuations"]]
        reported_partitions_valid = reported_partitions_valid and all(
            partition_is_stable(partition, decoherence, continuations_for_record)
            for partition in census_payload[name]["finest"]
        )
    gates.check(
        "PPR-RECORD-AVAILABILITY",
        preserved_record
        and not erased_record
        and tagged_path0 == Fraction(337, 625)
        and erased_path0 == 1,
        {
            "preserving": preserved_detail,
            "erasing": erased_detail,
            "record_preserved": preserved_record,
            "record_after_eraser": erased_record,
            "tagged_path0": fraction_text(tagged_path0),
            "erased_path0": fraction_text(erased_path0),
        },
        "eraser-ignore",
    )
    gates.check(
        "PPR-PARTITION-CENSUS",
        isinstance(census_payload["block_record"]["all_count"], int)
        and census_payload["block_record"]["all_count"] == bell_number(4)
        and block.finest == (((0, 1), (2, 3)),)
        and erasable_aux.finest == (((0, 1),),)
        and coherent_aux.finest == (((0, 1),),)
        and len(multiple.finest) == 2
        and reported_partitions_valid,
        census_payload,
        "record-preplant / result-count-type",
    )
    records_payload = {
        "support_criterion": {
            "preserving_record_available": preserved_record,
            "eraser_record_available": erased_record,
            "preserving": preserved_detail,
            "erasing": erased_detail,
        },
        "quantum_eraser": {
            "tagged_path0": fraction_text(tagged_path0),
            "erased_path0": fraction_text(erased_path0),
        },
        "census": census_payload,
        "interference": {
            "reconvergent_coherent_p0": fraction_text(coherent_p0),
            "reconvergent_decohered_p0": fraction_text(decoherent_p0),
            "dangling_record_probability": fraction_text(dangling_record_probability),
            "partial_difference": fraction_text(partial_difference),
            "partial_difference_over_mu": fraction_text(partial_coefficient),
            "one_outcome_total": fraction_text(one_total),
            "one_outcome_later_coherent": fraction_text(one_probe_coherent),
            "one_outcome_later_decoherent": fraction_text(one_probe_decoherent),
        },
    }

    diagram = fixture["comparison_diagram"]
    comparison_edges = {name: matrices[alias] for name, alias in diagram["edges"].items()}
    path_values = [comparison_path(path, comparison_edges) for path in diagram["paths"]]
    comparison_flat = all(value == path_values[0] for value in path_values[1:])
    frames = {name: matrices[alias] for name, alias in diagram["gauge_frames"].items()}
    gauged_edges = gauge_comparison_edges(comparison_edges, frames)
    gauged_paths = [comparison_path(path, gauged_edges) for path in diagram["paths"]]
    endpoint_covariant = all(value == gauged_paths[0] for value in gauged_paths[1:])
    expected_gauged = multiply(frames["3"], multiply(path_values[0], inverse(frames["0"])))
    endpoint_covariant = endpoint_covariant and gauged_paths[0] == expected_gauged

    loop = fixture["dynamical_loop"]
    beam = matrices[loop["beam_splitter"]]
    flat_phase = matrices[loop["flat_phase"]]
    nonflat_phase = matrices[loop["nonflat_phase"]]
    flat_transport = multiply(dagger(beam), multiply(flat_phase, beam))
    curved_transport = multiply(dagger(beam), multiply(nonflat_phase, beam))
    loop_input = parse_matrix([[item] for item in loop["input"]])
    flat_output = multiply(flat_transport, loop_input)
    curved_output = multiply(curved_transport, loop_input)
    row = int(loop["screen_row"])
    flat_probability = flat_output[row][0].abs2()
    curved_probability = curved_output[row][0].abs2()
    same_loop_type = bool(controls.get("same_loop_type", False))
    gates.check(
        "PPR-COMPARISON-COCYCLE",
        comparison_flat and endpoint_covariant,
        {
            "path_values": [matrix_text(value) for value in path_values],
            "gauged_path_values": [matrix_text(value) for value in gauged_paths],
        },
        "comparison-phase",
    )
    gates.check(
        "PPR-COMPARISON-DYNAMICS-TYPE",
        not same_loop_type
        and flat_probability != curved_probability
        and multiply(dagger(curved_transport), curved_transport) == identity(2),
        {
            "comparison_kind": "same-fact dictionary",
            "dynamical_kind": "distinct physical routes",
            "flat_probability": fraction_text(flat_probability),
            "nonflat_probability": fraction_text(curved_probability),
        },
        "transport-flatten / loop-conflate",
    )
    loops_payload = {
        "comparison": {
            "routes": len(path_values),
            "flat": comparison_flat,
            "frame_covariant": endpoint_covariant,
            "common_value": matrix_text(path_values[0]),
        },
        "dynamics": {
            "flat_screen_probability": fraction_text(flat_probability),
            "nonflat_screen_probability": fraction_text(curved_probability),
            "nonflat_transport_unitary": True,
            "claim_level": "finite curvature-sensitive transport observable; not gravity",
        },
    }

    graph_transports = [branch_transport(branch, matrices) for branch in branches]
    reported_transports = copy.deepcopy(graph_transports)
    if "reported_beta" in controls:
        reported_transports[1] = matrices[controls["reported_beta"]]
    actual_rewrite = (
        len(branches[0]["vertices"]) != len(branches[1]["vertices"])
        and tuple(branches[0]["edges"]) != tuple(branches[1]["edges"])
        and branches[0]["carrier_dimension"] != branches[1]["carrier_dimension"]
    )
    uniform_probe = reported_transports == graph_transports
    renamed_transports = [branch_transport(branch, matrices) for branch in renamed]
    graph_covariant = renamed_transports == graph_transports
    by_record: dict[str, set[str]] = {}
    for branch, transport in zip(branches, graph_transports):
        by_record.setdefault(branch["record_label"], set()).add(matrix_key(transport))
    record_only_can_reconstruct = all(len(values) == 1 for values in by_record.values())

    spectator_alpha = tensor(graph_transports[0], matrices["Z"])
    beta_spectator = matrices[controls.get("beta_spectator", "Z")]
    spectator_beta = tensor(graph_transports[1], beta_spectator)
    spectator_ok = spectator_alpha == tensor(graph_transports[0], matrices["Z"]) and spectator_beta == tensor(graph_transports[1], matrices["Z"])
    disjoint_linearity = tensor(
        class_operator([(a, graph_transports[0]), (b, graph_transports[1])]), matrices["Z"]
    ) == class_operator(
        [(a, tensor(graph_transports[0], matrices["Z"])), (b, tensor(graph_transports[1], matrices["Z"]))]
    )
    gates.check(
        "PPR-RELATIONAL-REWRITE",
        actual_rewrite and uniform_probe and graph_covariant and not record_only_can_reconstruct,
        {
            "actual_relation_and_carrier_change": actual_rewrite,
            "uniform_graph_probe": uniform_probe,
            "relabel_covariant": graph_covariant,
            "record_only_reconstruction": record_only_can_reconstruct,
            "transports": [matrix_text(value) for value in graph_transports],
        },
        "graph-copy / graph-erase / probe-feedforward",
    )
    gates.check(
        "PPR-LOCAL-COMPOSITION",
        spectator_ok and disjoint_linearity,
        {"idle_spectator": spectator_ok, "disjoint_linearity": disjoint_linearity},
        "spectator-couple",
    )

    law_rows: list[dict[str, object]] = []
    all_laws_complete = True
    all_laws_nonfactorizing = True
    for law in wedge["law_family"]:
        predictions: list[str] = []
        operators: list[list[list[str]]] = []
        for weights in law["matter_weights"]:
            left_weight, right_weight = (GQ(weights[0]), GQ(weights[1]))
            operator = class_operator(
                [(left_weight, graph_transports[0]), (right_weight, graph_transports[1])]
            )
            all_laws_complete = all_laws_complete and multiply(dagger(operator), operator) == identity(2)
            predictions.append(fraction_text(density_probability(row_operator(operator, int(wedge["screen_row"])), rho0)))
            operators.append(matrix_text(operator))
        weight_matrix = parse_matrix(law["matter_weights"])
        determinant = weight_matrix[0][0] * weight_matrix[1][1] - weight_matrix[0][1] * weight_matrix[1][0]
        all_laws_nonfactorizing = all_laws_nonfactorizing and not determinant.is_zero()
        law_rows.append(
            {
                "name": law["name"],
                "determinant": scalar_text(determinant),
                "heldout_screen_probabilities": predictions,
                "operators": operators,
            }
        )
    law_predictions = {tuple(row["heldout_screen_probabilities"]) for row in law_rows}
    laws_move_observable = len(law_predictions) > 1
    gates.check(
        "PPR-RELATIONAL-RESPONSE",
        all_laws_complete and all_laws_nonfactorizing and laws_move_observable,
        {
            "all_input_complete": all_laws_complete,
            "nonfactorizing_weight_response": all_laws_nonfactorizing,
            "rival_laws_move_heldout": laws_move_observable,
            "laws": law_rows,
        },
        "completeness-amplify",
    )

    bell = bell_density()
    p0 = matrices["P0"]
    p1 = matrices["P1"]
    qplus = matrices["Qplus"]
    qminus = matrices["Qminus"]
    z_instrument = [p0, multiply(matrices["Vgrow"], p1)]
    x_instrument = [qplus, multiply(matrices["Vgrow2"], qminus)]
    amplifier = GQ(fixture["no_signalling"]["amplifier"])
    bad_instrument = [p0, scale(amplifier, multiply(matrices["Vgrow"], p1))]
    primary_z = bad_instrument if controls.get("use_amplifier_as_law") else z_instrument
    bob_z = local_instrument_bob_marginal(primary_z, bell)
    bob_x = local_instrument_bob_marginal(x_instrument, bell)
    bob_bad = local_instrument_bob_marginal(bad_instrument, bell)
    fixed_bob = scale(Fraction(1, 2), identity(2))
    gates.check(
        "PPR-ALL-INPUT-COMPLETENESS",
        is_complete(primary_z) and is_complete(x_instrument),
        {
            "z_completeness": matrix_text(completeness_operator(primary_z)),
            "x_completeness": matrix_text(completeness_operator(x_instrument)),
        },
        "completeness-amplify",
    )
    gates.check(
        "PPR-FIXED-BOB-NO-SIGNALLING",
        bob_z == fixed_bob and bob_x == fixed_bob and bob_bad != fixed_bob,
        {
            "z_bob": matrix_text(bob_z),
            "x_bob": matrix_text(bob_x),
            "amplified_bob": matrix_text(bob_bad),
        },
        "completeness-amplify",
    )

    coherent_output = multiply(one_class, basis_vector(2, 0))
    coherent_rho = outer(coherent_output)
    bell_joint_purity = purity(bell)
    bell_bob_purity = purity(partial_trace_first(bell, 2, 2))
    non_entanglement_breaking = bell_joint_purity == 1 and bell_bob_purity == Fraction(1, 2)
    nonclassical_witness = coherent_p0 != decoherent_p0 and non_entanglement_breaking
    gates.check(
        "PPR-NONCLASSICAL-WITNESS",
        nonclassical_witness and purity(coherent_rho) == 1,
        {
            "interference_moves_screen": coherent_p0 != decoherent_p0,
            "unitary_channel_not_entanglement_breaking": non_entanglement_breaking,
            "bell_joint_purity": fraction_text(bell_joint_purity),
            "bell_bob_purity": fraction_text(bell_bob_purity),
        },
        "transport-flatten",
    )

    relational_payload = {
        "actual_rewrite": actual_rewrite,
        "carrier_dimensions": [branch["carrier_dimension"] for branch in branches],
        "graph_transports": [matrix_text(value) for value in graph_transports],
        "record_only_reconstruction": record_only_can_reconstruct,
        "relabel_covariant": graph_covariant,
        "idle_spectator": spectator_ok,
        "disjoint_composition": disjoint_linearity,
        "laws": law_rows,
        "rival_laws_move_heldout": laws_move_observable,
        "claim_level": "finite relational back-response wedge; not metric gravity",
    }
    signalling_payload = {
        "z_complete": is_complete(primary_z),
        "x_complete": is_complete(x_instrument),
        "z_bob": matrix_text(bob_z),
        "x_bob": matrix_text(bob_x),
        "amplifier_complete": is_complete(bad_instrument),
        "amplifier_bob": matrix_text(bob_bad),
        "scope": "unconditioned fixed-Bob algebra under finite Alice-carrier growth",
    }
    nonclassical_payload = {
        "coherent_screen_differs": coherent_p0 != decoherent_p0,
        "unitary_not_entanglement_breaking": non_entanglement_breaking,
        "bell_joint_purity": fraction_text(bell_joint_purity),
        "bell_bob_purity": fraction_text(bell_bob_purity),
    }

    builder_flags = {
        "nonempty": all_laws_complete,
        "event": distinct_events and relabel_covariant,
        "representation": same_channel and not same_instrument,
        "congruence": stable.strict_rounds == 2 and delayed_visible,
        "record": preserved_record and not erased_record,
        "type": comparison_flat and flat_probability != curved_probability,
        "rewrite": actual_rewrite and uniform_probe and not record_only_can_reconstruct,
        "nonclassical": nonclassical_witness,
        "selected": not laws_move_observable,
    }
    builder_index = build_outcome_index(builder_flags)
    if controls.get("flip_builder"):
        builder_index = 10 if builder_index != 10 else 9
    raw_for_comparator = {
        "laws_complete": all_laws_complete,
        "event_signatures": signatures,
        "relabel": relabel_covariant,
        "channel_same": same_channel,
        "instrument_same": same_instrument,
        "stable_rounds": stable.strict_rounds,
        "delayed_visible": delayed_visible,
        "record_preserved": preserved_record,
        "record_erased": erased_record,
        "comparison_paths": [matrix_text(value) for value in path_values],
        "flat_probability": fraction_text(flat_probability),
        "curved_probability": fraction_text(curved_probability),
        "actual_rewrite": actual_rewrite,
        "uniform_probe": uniform_probe,
        "record_only": record_only_can_reconstruct,
        "coherent_probability": fraction_text(coherent_p0),
        "decoherent_probability": fraction_text(decoherent_p0),
        "non_eb": non_entanglement_breaking,
        "law_predictions": sorted(law_predictions),
    }
    comparator_index = compare_outcome_from_serialized(canonical_json(raw_for_comparator))
    gates.check(
        "PPR-INDEPENDENT-PRIMARY",
        builder_index == comparator_index and 1 <= builder_index <= len(labels),
        {"builder_index": builder_index, "comparator_index": comparator_index},
        "verdict-flip",
    )

    provenance = {
        "schema": "ppr-result-v1",
        "source_sha256": source_sha,
        "fixture_sha256": FIXTURE_SHA256,
        "core_sha256": CORE_SHA256,
        "pin_sha256": PIN_SHA256,
        "pin_commit": PIN_COMMIT,
        "base_commit": BASE_COMMIT,
        "arithmetic": "Q(i)",
    }
    primary = {
        "index": builder_index,
        "label": labels[builder_index - 1],
        "comparator_index": comparator_index,
        "all_outcomes_digest": hashlib.sha256("\n".join(labels).encode("utf-8")).hexdigest(),
    }
    limitations = [
        "finite exact fixtures only",
        "actualization remains a postulate",
        "configuration catalogue is declared kinematics; the realized relation carrier changes",
        "law weights are not selected",
        "record permanence is proved only against the registered continuation grammar",
        "fixed-Bob unconditional no-signalling only; conditional steering and changing Bob algebras remain open",
        "no continuum, Lorentz, GR, QFT, particle, constant, or phenomenology result",
    ]
    measurements = {
        "event_representation": event_payload,
        "stable_null": null_payload,
        "pullback": pullback_payload,
        "records": records_payload,
        "comparison_dynamics": loops_payload,
        "relational_wedge": relational_payload,
        "no_signalling": signalling_payload,
        "nonclassical": nonclassical_payload,
    }
    exact_claims = make_exact_claims(measurements, primary)
    payload: dict[str, object] = {
        "provenance": provenance,
        "primary": primary,
        "measurements": measurements,
        "exact_claims": exact_claims,
        "limitations": limitations,
        "mutation_contract": {"registered": list(MUTANTS), "clean_run": mutant is None},
    }
    provisional_paper = render_paper(payload, gate_count=len(gates.rows) + 1)
    claim_occurrences = {item["id"]: provisional_paper.count(item["text"]) for item in exact_claims}
    gates.check(
        "PPR-PAPER-CLAIM-BINDINGS",
        all(count == 1 for count in claim_occurrences.values()),
        claim_occurrences,
        "seal-after-write",
    )
    payload["gates"] = copy.deepcopy(gates.rows)
    payload["gate_summary"] = {"passed": len(gates.rows), "total": len(gates.rows)}
    return payload, gates


def build_outcome_index(flags: Mapping[str, bool]) -> int:
    if not flags["nonempty"]:
        return 1
    if not flags["event"]:
        return 2
    if not flags["representation"]:
        return 3
    if not flags["congruence"]:
        return 4
    if not flags["record"]:
        return 5
    if not flags["type"]:
        return 6
    if not flags["rewrite"]:
        return 7
    if not flags["nonclassical"]:
        return 8
    if not flags["selected"]:
        return 9
    return 10


def compare_outcome_from_serialized(serialized: str) -> int:
    raw = json.loads(serialized)
    if not raw["laws_complete"]:
        return 1
    if raw["event_signatures"][0] == raw["event_signatures"][1] or not raw["relabel"]:
        return 2
    if not raw["channel_same"] or raw["instrument_same"]:
        return 3
    if raw["stable_rounds"] != 2 or not raw["delayed_visible"]:
        return 4
    if not raw["record_preserved"] or raw["record_erased"]:
        return 5
    if len({canonical_json(value) for value in raw["comparison_paths"]}) != 1 or raw["flat_probability"] == raw["curved_probability"]:
        return 6
    if not raw["actual_rewrite"] or not raw["uniform_probe"] or raw["record_only"]:
        return 7
    if raw["coherent_probability"] == raw["decoherent_probability"] or not raw["non_eb"]:
        return 8
    if len({tuple(value) for value in raw["law_predictions"]}) > 1:
        return 9
    return 10


def make_exact_claims(measurements: Mapping[str, object], primary: Mapping[str, object]) -> list[dict[str, str]]:
    stable = measurements["stable_null"]
    pullbacks = measurements["pullback"]
    records = measurements["records"]
    loops = measurements["comparison_dynamics"]
    wedge = measurements["relational_wedge"]
    signalling = measurements["no_signalling"]
    laws = wedge["laws"]
    return [
        {
            "id": "C1",
            "text": f"The multi-boundary null descent takes {stable['strict_rounds']} strict rounds and reduces the cut null dimension from {stable['present_cut_dimension']} to {stable['stable_cut_dimension']}.",
        },
        {
            "id": "C2",
            "text": f"The heterogeneous pullback check covers {pullbacks['reached_basis_pairs_checked']} reached basis pairs and agrees with the direct common-boundary cross terms in every case.",
        },
        {
            "id": "C3",
            "text": f"The reconvergent screen probability is {records['interference']['reconvergent_coherent_p0']} coherently and {records['interference']['reconvergent_decohered_p0']} after the alternatives are recorded.",
        },
        {
            "id": "C4",
            "text": f"The physical tag control changes the path-zero probability from {records['quantum_eraser']['tagged_path0']} to {records['quantum_eraser']['erased_path0']} when the tag is lawfully erased.",
        },
        {
            "id": "C5",
            "text": f"The partial-overlap fixture has exact absolute shift {records['interference']['partial_difference']}, equal to overlap times coefficient {records['interference']['partial_difference_over_mu']} in this fixture.",
        },
        {
            "id": "C6",
            "text": f"The same-fact comparison diagram has {loops['comparison']['routes']} agreeing routes, while the physical loop moves the exact screen probability from {loops['dynamics']['flat_screen_probability']} to {loops['dynamics']['nonflat_screen_probability']}.",
        },
        {
            "id": "C7",
            "text": f"The two relational branches use carrier dimensions {wedge['carrier_dimensions'][0]} and {wedge['carrier_dimensions'][1]}, and one record-only lookup cannot reconstruct both graph-computed transports.",
        },
        {
            "id": "C8",
            "text": f"The rival laws predict held-out screen pairs {laws[0]['heldout_screen_probabilities']} and {laws[1]['heldout_screen_probabilities']}; therefore the law is not selected by these constraints.",
        },
        {
            "id": "C9",
            "text": f"Both complete Alice growth instruments leave the fixed Bob marginal at {signalling['z_bob']}, while the registered amplifier moves it to {signalling['amplifier_bob']}.",
        },
        {
            "id": "C10",
            "text": f"The machine-selected primary outcome is {primary['label']}.",
        },
    ]


def render_paper(payload: Mapping[str, object], gate_count: int | None = None) -> str:
    measurements = payload["measurements"]
    primary = payload["primary"]
    provenance = payload["provenance"]
    count = gate_count if gate_count is not None else payload.get("gate_summary", {}).get("total", 0)
    claims = "\n".join(f"- **{item['id']}.** {item['text']}" for item in payload["exact_claims"])
    laws = measurements["relational_wedge"]["laws"]
    return f"""# Contextual pullbacks and permanent records

Status: **GREEN-UNREVIEWED CANDIDATE**.  This paper is generated from the
sealed PPR result object.  It is not terminal until the separately authorized
hostile process is completed.

## Result

The finite construction succeeds at the comparison problem but does not select
the dynamics.  On every dynamically reached subspace in the registered arena,
the operational cross-carrier comparison is the Gram pullback of the law's own
continuations into a common future boundary.  Present invisibility is not
enough for gauge: the physical quotient is the greatest null family stable
under every registered continuation.  Durable records are likewise not
declared direct-sum tags; they are the distinctions that remain recoverable
through all licensed futures.

The resulting primary classification is
`{primary['label']}`.  Two complete, nonfactorizing, nonclassical relational
laws satisfy the same construction and nevertheless disagree on a calibrated
held-out screen.  Paper 3 therefore constructs a local contextual-pullback and
permanence architecture, not the unique joint successor law and not the
record-generated fixed point sought by the strongest outcome.

{payload['exact_claims'][9]['text']}

## The idea without technical language

Imagine that the world can redraw part of its own wiring while an event is
happening.  Two possible histories may then pass through differently shaped
wiring diagrams.  Asking whether their hidden intermediate states are "the
same" is premature.  The operational question is simpler: can both histories
flow into a later situation where the same test can be made?  If they can, the
two routes themselves determine how they are compared.  No extra ruler between
the intermediate diagrams is needed.

Some differences are invisible now but become visible after another event.
Those are dormant physical differences, not gauge.  A difference may be
discarded only when every future operation allowed by the model remains blind
to it.  The same distinction separates a real record from a temporary tag: a
real record remains available; a temporary tag can be erased and the histories
can interfere again.

This repairs a conceptual gap, but it does not answer which event happens next
or with what fundamental strength.  The tests admit two different laws, and
their later predictions differ.  The theory has found the right type of object
on which a law must live; it has not yet found the principle that chooses the
law.

## 1. Ontological commitments

The primitive kinematic objects in this unit are finite relational
configurations and typed complete histories connecting them.  The catalogue of
possible configurations is fixed as part of the model, but the realized
relation carrier changes from one successor to another.  A physical history is
individuated by that relational event algebra; it is not an arbitrary Kraus
decomposition of a reduced quantum channel.

At a boundary, two syntactic directions represent the same physical state only
when no licensed preparation, continuation, spectator, or readout can ever
distinguish them.  Quotienting by this continuation-stable null family gives
the physical boundary space at the registered finite grammar.  Actualization—
the assertion that one complete recorded successor occurs—remains a separate
postulate.

## 2. Representation is not event ontology

An exact rational rotation of two Kraus operators leaves the unconditioned
dephasing channel unchanged while changing the outcome-resolved instrument.
That is representation freedom only when no calibrated record keeps the
outcome labels.  It is not permission to rotate together two histories whose
relation graphs describe different events.  Conversely, splitting one history
coefficient into two pieces and recombining it leaves the coarse class operator
exactly unchanged.

This is the necessary middle position: neither every operator decomposition nor
every syntactic spelling is ontology.  Records and the independently typed
relational event algebra decide what survives the quotient.

## 3. The continuation-stable quotient

{payload['exact_claims'][0]['text']}

One direction is invisible at the current cut and becomes visible only after
the second continuation.  Another remains invisible through every registered
context.  Promoting the present kernel directly to gauge therefore fails.  The
descending multi-boundary construction removes precisely the delayed-reactive
direction and certifies that every licensed continuation descends to the
quotient.

This result is grammar-relative.  Adding a genuinely new future interaction
can shrink the null family; Paper 3 does not turn a finite continuation census
into an all-possible-physics theorem.

## 4. Cross-carrier comparison by future context

{payload['exact_claims'][1]['text']}

One branch stays two-dimensional while the other grows through a
three-dimensional carrier.  Their comparison is not a free identification of
the intermediate carriers.  For continuations `U_alpha` and `U_beta` into one
common boundary, every observable cross term factors through
`U_alpha^dagger U_beta` on the reached quotient subspaces.  Halving that
pullback changes a direct cross term and fails.  A direction missed by the
one-step growth map but seen by the future continuation provides the matching
negative control: "unfed once" is not "permanently gauge."

The pullback is contextual.  A different admitted future probe can provide a
different comparison functional.  Consistency requires those functionals to
agree wherever the histories assert the same complete boundary fact; it does
not require a context-free map between arbitrary geometries.

## 5. Records, erasers, and interference

The record test follows the v12 support criterion.  It computes which
intermediate alternatives are co-live after the first leg and which are later
co-merged.  A record exists exactly when the future co-merge partition keeps
every co-live pair separated.  The append-only continuation passes; the eraser
fails.  This is stronger than demanding that one preferred coordinate block be
preserved.

{payload['exact_claims'][2]['text']}

{payload['exact_claims'][3]['text']}

{payload['exact_claims'][4]['text']}

The exhaustive four-element census independently realizes a unique
nontrivial finest partition, a unique trivial partition, and a case with two
maximal partitions.  Thus uniqueness is measured rather than smuggled in.
Interference redistributes probability between recorded screen outcomes: the
outcome cross operators are nonzero and sum to zero.  In the one-outcome
control total probability is one in both descriptions, but a later sensitive
probe distinguishes coherent probability
`{measurements['records']['interference']['one_outcome_later_coherent']}` from
the incoherent value
`{measurements['records']['interference']['one_outcome_later_decoherent']}`.

## 6. Comparison flatness is not dynamical flatness

{payload['exact_claims'][5]['text']}

The first loop is a dictionary diagram: three routes claim to identify the
same boundary fact, so they must commute on the quotient and remain covariant
under independent boundary-frame changes.  A sign change on the direct closing
edge fails this test.

The second loop consists of physically different propagation routes.  Its
nontrivial holonomy is allowed to move an interference probability while the
transport remains unitary.  This is a finite curvature-sensitive transport
observable.  Calling it spacetime curvature or gravity would require a metric
interpretation, covariance, a continuum regime, and a calibrated
stress-energy/geometry response that this unit does not supply.

## 7. A genuine relational rewrite, but no selected law

{payload['exact_claims'][6]['text']}

The later probe is computed uniformly by composing the edge transports on each
output graph.  Relabelling vertices, adding an idle spectator, and composing a
disjoint edge leave the required content unchanged.  Erasing the graph while
keeping only the common record label loses the distinction between the two
probe transports.  Geometry is therefore doing operational work in this
fixture rather than serving as a copied classical control bit.

Each matter row changes the weights assigned to the two graph histories, and
each registered weight matrix has nonzero determinant.  The resulting
matter-to-rewrite-to-probe chain is nonfactorizing in this exact sense.  It is
still only a finite relational back-response witness, not Einstein
backreaction.

{payload['exact_claims'][7]['text']}

For reference, the exact law rows are:

- `{laws[0]['name']}`: determinant `{laws[0]['determinant']}`, held-out
  probabilities `{laws[0]['heldout_screen_probabilities']}`;
- `{laws[1]['name']}`: determinant `{laws[1]['determinant']}`, held-out
  probabilities `{laws[1]['heldout_screen_probabilities']}`.

Their disagreement is empirical at the fixture, not gauge.  Nothing in the
registered safety and composition surface chooses between them.

## 8. Quantum and signalling checks

The reconvergent class operator is unitary and its screen interference is
nonzero.  The matching Bell control has pure joint state and mixed reduced
state, so this channel is not entanglement breaking.  The positive arena is
therefore not forced into a classical record-at-every-step theory.

{payload['exact_claims'][8]['text']}

This is the unconditional fixed-Bob theorem only.  It proves that arbitrary
finite growth on Alice's output carrier cannot change Bob's unconditioned
marginal when Alice's operation is complete on every input.  It does not yet
settle conditional steering, reconvergence after growth, or what counts as
Bob's algebra when the relation carrier itself changes.

## 9. Exact result bindings

The following generated sentences are the paper's machine-bound numerical
claims.  Each labelled sentence C1--C10 appears exactly once in the relevant
section above; this index records their identifiers without duplicating them:

`C1, C2, C3, C4, C5, C6, C7, C8, C9, C10`.

The scorer reports {count}/{count} exact gates before artifact promotion.
Every clean artifact is rendered from one sealed payload; all registered
mutants must fail without moving an output path.

## 10. What is proved, what is not

At the registered finite arena, the following are constructed:

- a relational event algebra distinct from Kraus presentation freedom;
- a greatest continuation-stable null family and descended quotient maps;
- context-indexed cross-carrier pullbacks on dynamically reached subspaces;
- a record availability test that distinguishes permanence from erasure;
- separate same-fact comparison and physical-transport loop types;
- a nonclassical relational rewrite whose output graph changes a later probe;
- fixed-Bob unconditional no-signalling from all-input completeness.

The following remain missing:

- a principle selecting one history-weight and interaction law;
- permanence under a generative, rather than finitely enumerated, future law;
- a preferred all-scale event algebra or configuration catalogue;
- conditional steering and changing-factorization no-signalling;
- an account of actualization;
- continuum and Lorentz recovery, metric gravity, Einstein dynamics, QFT,
  vacuum and excitation structure, particle species, constants, or a measured
  deviation from established physics.

The ontological advance is consequently narrower but real: comparison need not
be an extra free object once the law and its future contexts exist.  The open
freedom has moved into the interaction/weight law and the generative scope of
its records.  That is where the next theory-building step must act.

## Reproducibility and provenance

- scorer SHA-256: `{provenance['source_sha256']}`;
- fixture SHA-256: `{provenance['fixture_sha256']}`;
- generic core SHA-256: `{provenance['core_sha256']}`;
- pin SHA-256: `{provenance['pin_sha256']}`;
- immutable base commit: `{provenance['base_commit']}`;
- arithmetic: `{provenance['arithmetic']}`.

The physical fixture contains no expected verdict or result fields.  The
primary label is parsed from the frozen pin and chosen independently by two
numeric classifiers.  The unrelated untracked v15 SCOUT-T paths are outside
the PPR read and write set.

## Relation to prior mathematical work

The quotient-by-null construction is structurally close to Hilbert-space
representations of strongly positive decoherence functionals, while the
complete-history viewpoint follows the consistent-histories idea that the
decoherence functional supplies the geometry on histories.  Dilation and
network-composition results provide mathematical precedents for treating
intermediate realizations as representation while retaining calibrated
instruments and compositional interfaces.  Those precedents do not select the
ISP event algebra or its weights.

- David Craig, *The Geometry of Consistency: Decohering Histories in
  Generalized Quantum Theory*, [arXiv:quant-ph/9704031](https://arxiv.org/abs/quant-ph/9704031).
- Stan Gudder, *Hilbert Space Representations of Decoherence Functionals and
  Quantum Measures*, [arXiv:1011.1694](https://arxiv.org/abs/1011.1694).
- Dennis Kretschmann, Dirk Schlingemann, and Reinhard Werner, *The
  Information-Disturbance Tradeoff and the Continuity of Stinespring's
  Representation*, [arXiv:quant-ph/0605009](https://arxiv.org/abs/quant-ph/0605009).
- Giulio Chiribella, Giacomo Mauro D'Ariano, and Paolo Perinotti,
  *Theoretical framework for quantum networks*,
  [arXiv:0904.4483](https://arxiv.org/abs/0904.4483).
"""


def render_output(payload: Mapping[str, object], paper_sha: str) -> str:
    lines = [
        "PPR — CONTEXTUAL PULLBACKS AND PERMANENT RECORDS",
        f"PRIMARY {payload['primary']['label']}",
        f"OUTCOME_INDEX {payload['primary']['index']}",
        f"COMPARATOR_INDEX {payload['primary']['comparator_index']}",
        f"GATES {payload['gate_summary']['passed']}/{payload['gate_summary']['total']}",
        f"SOURCE_SHA256 {payload['provenance']['source_sha256']}",
        f"FIXTURE_SHA256 {payload['provenance']['fixture_sha256']}",
        f"PAPER_SHA256 {paper_sha}",
    ]
    for section, value in payload["measurements"].items():
        lines.append(f"MEASUREMENT {section} {canonical_json(value)}")
    for row in payload["gates"]:
        lines.append(f"GATE {row['name']} PASS {canonical_json(row['detail'])}")
    lines.append("LIMITATIONS " + canonical_json(payload["limitations"]))
    return "\n".join(lines) + "\n"


def build_artifacts(payload: Mapping[str, object], tamper_after_seal: bool) -> tuple[str, str, str]:
    manifest = seal_mapping(payload)
    if set(manifest) != set(payload):
        raise GateFailure("PPR-SEAL-TOTALITY")
    if any(
        hashlib.sha256(canonical_json(payload[key]).encode("utf-8")).hexdigest() != digest
        for key, digest in manifest.items()
    ):
        raise GateFailure("PPR-SEAL-CONTENT")
    paper = render_paper(payload)
    paper_sha = hashlib.sha256(paper.encode("utf-8")).hexdigest()
    output = render_output(payload, paper_sha)
    output_sha = hashlib.sha256(output.encode("utf-8")).hexdigest()
    if tamper_after_seal:
        paper = paper + "\npost-seal mutation\n"
    if hashlib.sha256(paper.encode("utf-8")).hexdigest() != paper_sha:
        raise GateFailure("PPR-POST-SEAL-IMMUTABILITY")
    if render_paper(payload) != paper or render_output(payload, paper_sha) != output:
        raise GateFailure("PPR-RENDER-RECOMPUTE")
    promotion = {
        "payload_manifest_total": True,
        "payload_seals_recomputed": True,
        "paper_recomputed": True,
        "output_recomputed": True,
        "all_checks_before_write": True,
    }
    receipt = {
        "schema": "ppr-receipt-v1",
        "payload": payload,
        "payload_seals": manifest,
        "artifact_sha256": {"paper": paper_sha, "output": output_sha},
        "promotion": promotion,
        "promotion_sha256": hashlib.sha256(canonical_json(promotion).encode("utf-8")).hexdigest(),
    }
    receipt_text = json.dumps(receipt, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    return output, receipt_text, paper


def write_artifacts(paths: Sequence[Path], values: Sequence[str]) -> None:
    for path in paths:
        if path.exists():
            raise FileExistsError(f"refusing to overwrite existing artifact: {path}")
    for path in paths:
        path.parent.mkdir(parents=True, exist_ok=True)
    for path, value in zip(paths, values):
        path.write_text(value, encoding="utf-8")


def run(mutant: str | None) -> tuple[dict[str, object], tuple[str, str, str]]:
    raw_fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    fixture = apply_mutation(raw_fixture, mutant)
    payload, _ = analyse(fixture, mutant)
    controls = fixture.get("mutation_controls", {})
    artifacts = build_artifacts(payload, bool(controls.get("tamper_after_seal", False)))
    return payload, artifacts


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--receipt", type=Path, default=DEFAULT_RECEIPT)
    parser.add_argument("--paper", type=Path, default=DEFAULT_PAPER)
    parser.add_argument("--mutant", choices=MUTANTS)
    parser.add_argument("--selftest", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    paths = (args.output.resolve(), args.receipt.resolve(), args.paper.resolve())
    if len(set(paths)) != 3:
        print("artifact paths must be distinct", file=sys.stderr)
        return 2
    if args.selftest:
        before = tuple(path.exists() for path in paths)
        try:
            run("anchor-corrupt")
        except GateFailure:
            after = tuple(path.exists() for path in paths)
            if before == after:
                print("SELFTEST PASS anchor corruption refused before write")
                return 0
        print("SELFTEST FAIL", file=sys.stderr)
        return 1
    if any(path.exists() for path in paths):
        print("refusing to overwrite an existing artifact", file=sys.stderr)
        return 2
    try:
        payload, artifacts = run(args.mutant)
    except (GateFailure, AssertionError, ValueError) as error:
        print(f"REFUSED {error}", file=sys.stderr)
        return 1
    if args.mutant is not None:
        print(f"MUTANT SURVIVED {args.mutant}", file=sys.stderr)
        return 3
    write_artifacts(paths, artifacts)
    print(
        f"PASS {payload['primary']['label']} "
        f"{payload['gate_summary']['passed']}/{payload['gate_summary']['total']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
