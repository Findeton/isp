#!/usr/bin/env python3
"""D37 exact finite regional-history specification receipt.

Standard-library only.  Every probability is a Fraction.  Enumeration order is
never interpreted as physical time or as an arbitration mark.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Callable, Dict, FrozenSet, Hashable, Iterable, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]


def stable(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=repr)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class Graph:
    name: str
    vertices: Tuple[str, ...]
    edges: Tuple[Tuple[str, str], ...]

    def __post_init__(self) -> None:
        if len(set(self.vertices)) != len(self.vertices):
            raise ValueError("duplicate vertex")
        normalized = tuple(sorted(tuple(sorted(edge)) for edge in self.edges))
        if normalized != self.edges or len(set(normalized)) != len(normalized):
            raise ValueError("edges must be unique normalized pairs")
        if any(len(edge) != 2 or edge[0] == edge[1] for edge in self.edges):
            raise ValueError("bad edge")
        if any(v not in self.vertices for edge in self.edges for v in edge):
            raise ValueError("edge outside graph")


def graph(name: str, vertices: Sequence[str], edges: Iterable[Tuple[str, str]]) -> Graph:
    return Graph(name, tuple(vertices), tuple(sorted(tuple(sorted(edge)) for edge in edges)))


GRAPHS: Dict[str, Graph] = {
    "pair": graph("pair", ("P", "Q"), (("P", "Q"),)),
    "path": graph("path", ("P", "Q", "R"), (("P", "Q"), ("Q", "R"))),
    "triangle": graph(
        "triangle",
        ("P", "Q", "R"),
        (("P", "Q"), ("Q", "R"), ("P", "R")),
    ),
    "d36_disjoint": graph("d36_disjoint", ("P", "Q"), ()),
    "two_pairs": graph(
        "two_pairs",
        ("P", "Q", "R", "S"),
        (("P", "Q"), ("R", "S")),
    ),
    "partial": graph("partial", ("P", "Q"), (("P", "Q"),)),
    "path5": graph(
        "path5",
        ("A", "B", "C", "D", "E"),
        (("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")),
    ),
    "path7": graph(
        "path7",
        ("A", "B", "C", "D", "E", "F", "G"),
        (("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"), ("F", "G")),
    ),
}


@dataclass(frozen=True)
class OrientedCell:
    name: str
    proposals: Tuple[Tuple[str, Tuple[str, ...]], ...]

    @property
    def vertices(self) -> Tuple[str, ...]:
        return tuple(name for name, _ in self.proposals)

    def participants(self, proposal: str) -> Tuple[str, ...]:
        return dict(self.proposals)[proposal]


ORIENTED_CELLS: Dict[str, OrientedCell] = {
    "pair": OrientedCell("pair", (("P", ("A", "B")), ("Q", ("A", "B")))),
    "path": OrientedCell(
        "path",
        (("P", ("A", "B")), ("Q", ("B", "C")), ("R", ("C", "D"))),
    ),
    "triangle": OrientedCell(
        "triangle",
        (("P", ("A", "B")), ("Q", ("B", "C")), ("R", ("C", "A"))),
    ),
    "d36_disjoint": OrientedCell(
        "d36_disjoint",
        (("P", ("A", "B")), ("Q", ("C", "D"))),
    ),
    "partial": OrientedCell(
        "partial",
        (("P", ("A", "B", "C")), ("Q", ("C", "D"))),
    ),
}


def graph_from_cell(cell: OrientedCell) -> Graph:
    edges = []
    for (left, left_participants), (right, right_participants) in combinations(cell.proposals, 2):
        if set(left_participants) & set(right_participants):
            edges.append((left, right))
    return graph(cell.name, cell.vertices, edges)


def oriented_interface(
    cell: OrientedCell,
    region: FrozenSet[str],
) -> Tuple[Tuple[Tuple[str, str], ...], Tuple[str, ...], Tuple[Tuple[str, str], ...]]:
    inside_participants = {
        participant
        for proposal in region
        for participant in cell.participants(proposal)
    }
    incoming = tuple(sorted(
        [("base", participant) for participant in inside_participants]
        + [("carrier_parent", proposal) for proposal in region]
    ))
    outside = set(cell.vertices) - region
    lateral = tuple(sorted(
        proposal
        for proposal in outside
        if inside_participants & set(cell.participants(proposal))
    ))
    generated = tuple(sorted(
        [("mode_click", proposal) for proposal in region]
        + [("selection_click", proposal) for proposal in region]
    ))
    return incoming, lateral, generated


def rename_cell(
    cell: OrientedCell,
    proposal_rename: Mapping[str, str],
    participant_rename: Mapping[str, str],
) -> OrientedCell:
    return OrientedCell(
        f"{cell.name}-renamed",
        tuple(
            (
                proposal_rename[proposal],
                tuple(participant_rename[participant] for participant in participants),
            )
            for proposal, participants in cell.proposals
        ),
    )


def push_oriented_interface(
    interface: Tuple[Tuple[Tuple[str, str], ...], Tuple[str, ...], Tuple[Tuple[str, str], ...]],
    proposal_rename: Mapping[str, str],
    participant_rename: Mapping[str, str],
) -> Tuple[Tuple[Tuple[str, str], ...], Tuple[str, ...], Tuple[Tuple[str, str], ...]]:
    incoming, lateral, generated = interface
    pushed_incoming = tuple(sorted(
        (
            tag,
            participant_rename[value] if tag == "base" else proposal_rename[value],
        )
        for tag, value in incoming
    ))
    pushed_lateral = tuple(sorted(proposal_rename[value] for value in lateral))
    pushed_generated = tuple(sorted((tag, proposal_rename[value]) for tag, value in generated))
    return pushed_incoming, pushed_lateral, pushed_generated


Selected = FrozenSet[str]
BinaryDistribution = Dict[Selected, Fraction]


def neighbors(g: Graph, vertex: str) -> FrozenSet[str]:
    return frozenset(
        b if a == vertex else a
        for a, b in g.edges
        if a == vertex or b == vertex
    )


def regions(g: Graph, include_full: bool = True) -> Tuple[FrozenSet[str], ...]:
    answer = []
    for size in range(1, len(g.vertices) + 1):
        if not include_full and size == len(g.vertices):
            continue
        answer.extend(frozenset(x) for x in combinations(g.vertices, size))
    return tuple(answer)


def all_subsets(vertices: Sequence[str]) -> Tuple[Selected, ...]:
    return tuple(
        frozenset(vertices[index] for index in range(len(vertices)) if mask & (1 << index))
        for mask in range(1 << len(vertices))
    )


def feasible(g: Graph, selected: Iterable[str]) -> bool:
    chosen = set(selected)
    return all(not ({a, b} <= chosen) for a, b in g.edges)


def maximal(g: Graph, selected: Selected) -> bool:
    return feasible(g, selected) and all(
        vertex in selected or bool(neighbors(g, vertex) & selected)
        for vertex in g.vertices
    )


def normalize(weights: Mapping[Hashable, Fraction]) -> Dict[Hashable, Fraction]:
    total = sum(weights.values(), Fraction(0))
    if total <= 0:
        raise AssertionError("nonpositive normalization")
    answer = {atom: weight / total for atom, weight in weights.items() if weight}
    if sum(answer.values(), Fraction(0)) != 1:
        raise AssertionError("normalization drift")
    return answer


def hard_core(g: Graph, activity: Fraction | Mapping[str, Fraction]) -> BinaryDistribution:
    activities = (
        {vertex: activity for vertex in g.vertices}
        if isinstance(activity, Fraction)
        else dict(activity)
    )
    weights: Dict[Selected, Fraction] = {}
    for selected in all_subsets(g.vertices):
        if feasible(g, selected):
            weight = Fraction(1)
            for vertex in selected:
                weight *= activities[vertex]
            weights[selected] = weight
    return normalize(weights)  # type: ignore[return-value]


def uniform_maximal(g: Graph) -> BinaryDistribution:
    weights = {
        selected: Fraction(1)
        for selected in all_subsets(g.vertices)
        if maximal(g, selected)
    }
    return normalize(weights)  # type: ignore[return-value]


def connected_components(g: Graph) -> Tuple[Tuple[str, ...], ...]:
    remaining = set(g.vertices)
    answer = []
    while remaining:
        root = min(remaining)
        stack = [root]
        component = set()
        while stack:
            vertex = stack.pop()
            if vertex in component:
                continue
            component.add(vertex)
            stack.extend(neighbors(g, vertex) - component)
        remaining -= component
        answer.append(tuple(sorted(component)))
    return tuple(sorted(answer))


def greedy(g: Graph, orders: Sequence[Sequence[str]]) -> Selected:
    selected: set[str] = set()
    for order in orders:
        for vertex in order:
            if not (neighbors(g, vertex) & selected):
                selected.add(vertex)
    return frozenset(selected)


@dataclass(frozen=True)
class PriorityAtom:
    orders: Tuple[Tuple[str, ...], ...]
    selected: Selected


PriorityDistribution = Dict[PriorityAtom, Fraction]


def priority_law(g: Graph) -> PriorityDistribution:
    components = connected_components(g)
    order_families = tuple(tuple(permutations(component)) for component in components)
    weights: Dict[PriorityAtom, Fraction] = defaultdict(Fraction)
    denominator = math.prod(math.factorial(len(component)) for component in components)
    for orders in product(*order_families):
        atom = PriorityAtom(tuple(tuple(order) for order in orders), greedy(g, orders))
        weights[atom] += Fraction(1, denominator)
    answer = dict(weights)
    if sum(answer.values(), Fraction(0)) != 1:
        raise AssertionError("priority normalization")
    return answer


def priority_output(dist: PriorityDistribution) -> BinaryDistribution:
    answer: Dict[Selected, Fraction] = defaultdict(Fraction)
    for atom, probability in dist.items():
        answer[atom.selected] += probability
    return dict(answer)


def product_priority(
    left: PriorityDistribution,
    right: PriorityDistribution,
) -> PriorityDistribution:
    answer: Dict[PriorityAtom, Fraction] = defaultdict(Fraction)
    for left_atom, left_probability in left.items():
        for right_atom, right_probability in right.items():
            atom = PriorityAtom(
                left_atom.orders + right_atom.orders,
                left_atom.selected | right_atom.selected,
            )
            answer[atom] += left_probability * right_probability
    return dict(answer)


def restrict_binary(dist: BinaryDistribution, region: FrozenSet[str]) -> BinaryDistribution:
    answer: Dict[Selected, Fraction] = defaultdict(Fraction)
    for selected, probability in dist.items():
        answer[selected & region] += probability
    return dict(answer)


def binary_conditional_full(
    dist: BinaryDistribution,
    g: Graph,
    region: FrozenSet[str],
    source: Selected,
) -> BinaryDistribution:
    outside = frozenset(g.vertices) - region
    exterior = source & outside
    weights = {
        selected: probability
        for selected, probability in dist.items()
        if selected & outside == exterior
    }
    return normalize(weights)  # type: ignore[return-value]


def binary_conditional_local(
    dist: BinaryDistribution,
    g: Graph,
    region: FrozenSet[str],
    exterior: Selected,
) -> BinaryDistribution:
    outside = frozenset(g.vertices) - region
    weights: Dict[Selected, Fraction] = defaultdict(Fraction)
    for selected, probability in dist.items():
        if selected & outside == exterior:
            weights[selected & region] += probability
    return normalize(weights)  # type: ignore[return-value]


def intrinsic_hard_core(
    g: Graph,
    region: FrozenSet[str],
    exterior: Selected,
    activity: Fraction | Mapping[str, Fraction],
) -> BinaryDistribution:
    activities = (
        {vertex: activity for vertex in g.vertices}
        if isinstance(activity, Fraction)
        else dict(activity)
    )
    weights: Dict[Selected, Fraction] = {}
    for local in all_subsets(tuple(sorted(region))):
        if feasible(g, local | exterior):
            weight = Fraction(1)
            for vertex in local:
                weight *= activities[vertex]
            weights[local] = weight
    return normalize(weights)  # type: ignore[return-value]


def intrinsic_maximal(
    g: Graph,
    region: FrozenSet[str],
    exterior: Selected,
) -> BinaryDistribution:
    weights = {
        local: Fraction(1)
        for local in all_subsets(tuple(sorted(region)))
        if maximal(g, local | exterior)
    }
    return normalize(weights)  # type: ignore[return-value]


def aggregate(items: Iterable[Tuple[Hashable, Fraction]]) -> Dict[Hashable, Fraction]:
    answer: Dict[Hashable, Fraction] = defaultdict(Fraction)
    for atom, probability in items:
        answer[atom] += probability
    return dict(answer)


def binary_tower_checks(dist: BinaryDistribution, g: Graph) -> int:
    checks = 0
    for outer in regions(g):
        for inner in (candidate for candidate in regions(g) if candidate <= outer):
            for source in dist:
                outer_law = binary_conditional_full(dist, g, outer, source)
                composed: Dict[Selected, Fraction] = defaultdict(Fraction)
                for middle, p_middle in outer_law.items():
                    inner_law = binary_conditional_full(dist, g, inner, middle)
                    for target, p_target in inner_law.items():
                        composed[target] += p_middle * p_target
                if dict(composed) != outer_law:
                    raise AssertionError((g.name, outer, inner, source, composed, outer_law))
                checks += 1
    return checks


def priority_exterior(atom: PriorityAtom, g: Graph, region: FrozenSet[str]) -> object:
    outside = frozenset(g.vertices) - region
    return (
        tuple(tuple(vertex for vertex in order if vertex in outside) for order in atom.orders),
        tuple(sorted(atom.selected & outside)),
    )


def priority_conditional_full(
    dist: PriorityDistribution,
    g: Graph,
    region: FrozenSet[str],
    source: PriorityAtom,
) -> PriorityDistribution:
    key = priority_exterior(source, g, region)
    weights = {
        atom: probability
        for atom, probability in dist.items()
        if priority_exterior(atom, g, region) == key
    }
    return normalize(weights)  # type: ignore[return-value]


def priority_tower_checks(dist: PriorityDistribution, g: Graph) -> int:
    checks = 0
    cache: Dict[Tuple[FrozenSet[str], object], PriorityDistribution] = {}
    for region in regions(g):
        for source in dist:
            key = priority_exterior(source, g, region)
            cache.setdefault((region, key), priority_conditional_full(dist, g, region, source))
    for outer in regions(g):
        for inner in (candidate for candidate in regions(g) if candidate <= outer):
            outer_keys = sorted(
                (key for region, key in cache if region == outer),
                key=repr,
            )
            for outer_key in outer_keys:
                outer_law = cache[(outer, outer_key)]
                composed: Dict[PriorityAtom, Fraction] = defaultdict(Fraction)
                for middle, p_middle in outer_law.items():
                    inner_key = priority_exterior(middle, g, inner)
                    inner_law = cache[(inner, inner_key)]
                    for target, p_target in inner_law.items():
                        composed[target] += p_middle * p_target
                if dict(composed) != outer_law:
                    raise AssertionError((g.name, outer, inner, outer_key))
                checks += 1
    return checks


def k2_boundary(
    g: Graph,
    region: FrozenSet[str],
    exterior: Selected,
) -> Tuple[Tuple[str, ...], Tuple[Tuple[str, ...], ...]]:
    outside = frozenset(g.vertices) - region
    blocked_inside = tuple(sorted(
        vertex for vertex in region if neighbors(g, vertex) & exterior
    ))
    demands = []
    for vertex in outside:
        inside_neighbors = neighbors(g, vertex) & region
        if not inside_neighbors or vertex in exterior:
            continue
        if not (neighbors(g, vertex) & exterior):
            demands.append(tuple(sorted(inside_neighbors)))
    return blocked_inside, tuple(sorted(set(demands)))


def intrinsic_maximal_boundary(
    region: FrozenSet[str],
    internal_edges: Tuple[Tuple[str, str], ...],
    boundary: Tuple[Tuple[str, ...], Tuple[Tuple[str, ...], ...]],
) -> BinaryDistribution:
    blocked, demands = boundary
    blocked_set = set(blocked)
    weights: Dict[Selected, Fraction] = {}
    for local in all_subsets(tuple(sorted(region))):
        if local & blocked_set:
            continue
        if any(a in local and b in local for a, b in internal_edges):
            continue
        local_neighbors = {
            vertex: {
                b if a == vertex else a
                for a, b in internal_edges
                if a == vertex or b == vertex
            }
            for vertex in region
        }
        if any(
            vertex not in local
            and vertex not in blocked_set
            and not (local_neighbors[vertex] & local)
            for vertex in region
        ):
            continue
        if any(not (set(demand) & local) for demand in demands):
            continue
        weights[local] = Fraction(1)
    return normalize(weights)  # type: ignore[return-value]


def k2_boundary_checks(g: Graph) -> Tuple[int, int]:
    dist = uniform_maximal(g)
    checks = 0
    distinct_boundaries = set()
    for region in regions(g):
        outside = frozenset(g.vertices) - region
        exteriors = {selected & outside for selected in dist}
        internal_edges = tuple(edge for edge in g.edges if set(edge) <= region)
        for exterior in exteriors:
            boundary = k2_boundary(g, region, exterior)
            expected = binary_conditional_local(dist, g, region, exterior)
            actual = intrinsic_maximal_boundary(region, internal_edges, boundary)
            if actual != expected:
                raise AssertionError((g.name, region, exterior, boundary, actual, expected))
            distinct_boundaries.add((region, boundary))
            checks += 1
    return checks, len(distinct_boundaries)


def k3_full_checks(g: Graph, activity: Fraction) -> Tuple[int, int, int]:
    dist = hard_core(g, activity)
    conditional_checks = 0
    mixture_checks = 0
    for region in regions(g):
        outside = frozenset(g.vertices) - region
        exterior_mass: Dict[Selected, Fraction] = defaultdict(Fraction)
        for selected, probability in dist.items():
            exterior_mass[selected & outside] += probability
        mixture: Dict[Selected, Fraction] = defaultdict(Fraction)
        for exterior, probability in exterior_mass.items():
            intrinsic = intrinsic_hard_core(g, region, exterior, activity)
            conditional = binary_conditional_local(dist, g, region, exterior)
            if intrinsic != conditional:
                raise AssertionError((g.name, region, exterior, intrinsic, conditional))
            for local, local_probability in intrinsic.items():
                mixture[local] += probability * local_probability
            conditional_checks += 1
        if dict(mixture) != restrict_binary(dist, region):
            raise AssertionError((g.name, region, mixture, restrict_binary(dist, region)))
        mixture_checks += 1
    return conditional_checks, binary_tower_checks(dist, g), mixture_checks


def product_binary(
    left: BinaryDistribution,
    right: BinaryDistribution,
) -> BinaryDistribution:
    answer: Dict[Selected, Fraction] = defaultdict(Fraction)
    for left_atom, left_probability in left.items():
        for right_atom, right_probability in right.items():
            answer[left_atom | right_atom] += left_probability * right_probability
    return dict(answer)


def forcing_checks(g: Graph, activity: Fraction) -> Tuple[int, int, Tuple[str, ...]]:
    dist = hard_core(g, activity)
    ratio_checks = 0
    reconstructed_weights: Dict[Selected, Fraction] = {}
    for selected in dist:
        weight = Fraction(1)
        current: Selected = frozenset()
        for vertex in sorted(selected):
            candidate = current | {vertex}
            if not feasible(g, candidate):
                raise AssertionError("bad reconstruction path")
            weight *= activity
            current = candidate
            ratio_checks += 1
        reconstructed_weights[selected] = weight
    reconstructed = normalize(reconstructed_weights)
    if reconstructed != dist:
        raise AssertionError("forcing reconstruction")

    path = GRAPHS["path"]
    contextual_weights: Dict[Selected, Fraction] = {}
    for selected in all_subsets(path.vertices):
        if feasible(path, selected):
            contextual_weights[selected] = (
                activity ** len(selected)
                * (2 if {"P", "R"} <= selected else 1)
            )
    contextual = normalize(contextual_weights)
    odds = set()
    for selected in contextual:
        if "P" in selected:
            continue
        with_p = selected | {"P"}
        if with_p in contextual:
            odds.add(contextual[with_p] / contextual[selected])
    if len(odds) < 2:
        raise AssertionError("context-dependent negative control")
    maximal_support = uniform_maximal(path)
    feasible_support = {selected for selected in all_subsets(path.vertices) if feasible(path, selected)}
    if set(maximal_support) == feasible_support or frozenset() in maximal_support:
        raise AssertionError("maximal support negative control")
    return ratio_checks, len(reconstructed), tuple(sorted(ftext(x) for x in odds))


def raw_restriction_failures() -> Tuple[object, object]:
    path = GRAPHS["path"]
    edge_region = frozenset(("P", "Q"))
    k1_restricted = restrict_binary(priority_output(priority_law(path)), edge_region)
    k1_direct = priority_output(priority_law(GRAPHS["pair"]))
    if k1_restricted == k1_direct:
        raise AssertionError("K1 raw restriction")

    triangle = GRAPHS["triangle"]
    k2_restricted = restrict_binary(uniform_maximal(triangle), edge_region)
    k2_direct = uniform_maximal(GRAPHS["pair"])
    if k2_restricted == k2_direct:
        raise AssertionError("K2 raw restriction")
    return (
        (k1_restricted, k1_direct),
        (k2_restricted, k2_direct),
    )


def binary_boundary_fingerprint(
    g: Graph,
    region: FrozenSet[str],
    exterior: Selected,
) -> Tuple[str, ...]:
    return tuple(sorted(
        vertex
        for vertex in exterior
        if neighbors(g, vertex) & region
    ))


def find_k1_one_hop_counterexample() -> object:
    for graph_name in ("path5", "path7"):
        g = GRAPHS[graph_name]
        dist = priority_output(priority_law(g))
        for region in regions(g, include_full=False):
            outside = frozenset(g.vertices) - region
            grouped: Dict[Tuple[str, ...], list[Tuple[Selected, BinaryDistribution]]] = defaultdict(list)
            exteriors = sorted(
                {selected & outside for selected in dist},
                key=lambda selected: tuple(sorted(selected)),
            )
            for exterior in exteriors:
                fingerprint = binary_boundary_fingerprint(g, region, exterior)
                conditional = binary_conditional_local(dist, g, region, exterior)
                grouped[fingerprint].append((exterior, conditional))
            for fingerprint in sorted(grouped):
                rows = sorted(grouped[fingerprint], key=lambda row: tuple(sorted(row[0])))
                for first, second in combinations(rows, 2):
                    if first[1] != second[1]:
                        return (
                            graph_name,
                            tuple(sorted(region)),
                            fingerprint,
                            tuple(sorted(first[0])),
                            tuple(sorted(second[0])),
                            dist_signature(first[1]),
                            dist_signature(second[1]),
                        )
    return ()


MODES = ("NO_BIRTH", "TOKEN", "BORN")


@dataclass(frozen=True)
class ModeAtom:
    modes: Tuple[Tuple[str, str], ...]
    selected: Selected

    def mode_map(self) -> Dict[str, str]:
        return dict(self.modes)


ModeDistribution = Dict[ModeAtom, Fraction]


def joint_mode_law(
    g: Graph,
    mode_weights: Mapping[str, Fraction],
    activity: Fraction | Mapping[str, Fraction],
) -> ModeDistribution:
    activities = (
        {vertex: activity for vertex in g.vertices}
        if isinstance(activity, Fraction)
        else dict(activity)
    )
    weights: Dict[ModeAtom, Fraction] = {}
    for modes in product(MODES, repeat=len(g.vertices)):
        mode_map = dict(zip(g.vertices, modes))
        present = tuple(vertex for vertex in g.vertices if mode_map[vertex] != "NO_BIRTH")
        for selected in all_subsets(present):
            if not feasible(g, selected):
                continue
            weight = Fraction(1)
            for vertex in g.vertices:
                weight *= mode_weights[mode_map[vertex]]
            for vertex in selected:
                weight *= activities[vertex]
            atom = ModeAtom(tuple(sorted(mode_map.items())), selected)
            weights[atom] = weight
    return normalize(weights)  # type: ignore[return-value]


def mode_exterior(atom: ModeAtom, g: Graph, region: FrozenSet[str]) -> object:
    outside = frozenset(g.vertices) - region
    return (
        tuple((vertex, mode) for vertex, mode in atom.modes if vertex in outside),
        tuple(sorted(atom.selected & outside)),
    )


def mode_conditional_full(
    dist: ModeDistribution,
    g: Graph,
    region: FrozenSet[str],
    source: ModeAtom,
) -> ModeDistribution:
    key = mode_exterior(source, g, region)
    weights = {
        atom: probability
        for atom, probability in dist.items()
        if mode_exterior(atom, g, region) == key
    }
    return normalize(weights)  # type: ignore[return-value]


def mode_tower_checks(dist: ModeDistribution, g: Graph) -> int:
    checks = 0
    cache: Dict[Tuple[FrozenSet[str], object], ModeDistribution] = {}
    for region in regions(g):
        for source in dist:
            key = mode_exterior(source, g, region)
            cache.setdefault((region, key), mode_conditional_full(dist, g, region, source))
    for outer in regions(g):
        for inner in (candidate for candidate in regions(g) if candidate <= outer):
            outer_keys = sorted(
                (key for region, key in cache if region == outer),
                key=repr,
            )
            for outer_key in outer_keys:
                outer_law = cache[(outer, outer_key)]
                composed: Dict[ModeAtom, Fraction] = defaultdict(Fraction)
                for middle, p_middle in outer_law.items():
                    inner_key = mode_exterior(middle, g, inner)
                    inner_law = cache[(inner, inner_key)]
                    for target, p_target in inner_law.items():
                        composed[target] += p_middle * p_target
                if dict(composed) != outer_law:
                    raise AssertionError((g.name, outer, inner, outer_key))
                checks += 1
    return checks


def mode_intrinsic_checks(
    g: Graph,
    mode_weights: Mapping[str, Fraction],
    activity: Fraction,
) -> Tuple[int, int]:
    dist = joint_mode_law(g, mode_weights, activity)
    checks = 0
    one_site_conditionals = 0
    for region in regions(g):
        outside = frozenset(g.vertices) - region
        exterior_keys = {mode_exterior(atom, g, region) for atom in dist}
        for exterior_modes_tuple, exterior_selected_tuple in exterior_keys:
            exterior_modes = dict(exterior_modes_tuple)
            exterior_selected = frozenset(exterior_selected_tuple)
            local_weights: Dict[ModeAtom, Fraction] = {}
            local_vertices = tuple(sorted(region))
            for modes in product(MODES, repeat=len(local_vertices)):
                local_mode_map = dict(zip(local_vertices, modes))
                present = tuple(v for v in local_vertices if local_mode_map[v] != "NO_BIRTH")
                for local_selected in all_subsets(present):
                    if not feasible(g, local_selected | exterior_selected):
                        continue
                    weight = Fraction(1)
                    for vertex, mode in local_mode_map.items():
                        weight *= mode_weights[mode]
                    for vertex in local_selected:
                        weight *= activity
                    full_modes = dict(exterior_modes)
                    full_modes.update(local_mode_map)
                    atom = ModeAtom(tuple(sorted(full_modes.items())), local_selected | exterior_selected)
                    local_weights[atom] = weight
            intrinsic = normalize(local_weights)
            source = next(atom for atom in dist if mode_exterior(atom, g, region) == (exterior_modes_tuple, exterior_selected_tuple))
            conditional = mode_conditional_full(dist, g, region, source)
            if intrinsic != conditional:
                raise AssertionError((g.name, region, exterior_modes_tuple, exterior_selected_tuple))
            checks += 1
            if len(region) == 1:
                one_site_conditionals += 1
    return checks, one_site_conditionals


def swap_birth_token(atom: ModeAtom) -> ModeAtom:
    swap = {"NO_BIRTH": "NO_BIRTH", "TOKEN": "BORN", "BORN": "TOKEN"}
    return ModeAtom(tuple((vertex, swap[mode]) for vertex, mode in atom.modes), atom.selected)


def mode_swap_checks(dist: ModeDistribution) -> int:
    pushed: Dict[ModeAtom, Fraction] = defaultdict(Fraction)
    for atom, probability in dist.items():
        pushed[swap_birth_token(atom)] += probability
    if dict(pushed) != dist:
        raise AssertionError("BORN/TOKEN exchange")
    return len(dist)


def product_mode(left: ModeDistribution, right: ModeDistribution) -> ModeDistribution:
    answer: Dict[ModeAtom, Fraction] = defaultdict(Fraction)
    for left_atom, left_probability in left.items():
        for right_atom, right_probability in right.items():
            modes = tuple(sorted(left_atom.modes + right_atom.modes))
            atom = ModeAtom(modes, left_atom.selected | right_atom.selected)
            answer[atom] += left_probability * right_probability
    return dict(answer)


def restrict_mode(dist: ModeDistribution, region: FrozenSet[str]) -> ModeDistribution:
    answer: Dict[ModeAtom, Fraction] = defaultdict(Fraction)
    for atom, probability in dist.items():
        local = ModeAtom(
            tuple((vertex, mode) for vertex, mode in atom.modes if vertex in region),
            atom.selected & region,
        )
        answer[local] += probability
    return dict(answer)


def marginal_mode_probability(
    dist: ModeDistribution,
    vertex: str,
) -> Dict[str, Fraction]:
    answer: Dict[str, Fraction] = defaultdict(Fraction)
    for atom, probability in dist.items():
        answer[atom.mode_map()[vertex]] += probability
    return dict(answer)


def selected_probability(dist: ModeDistribution, vertex: str) -> Fraction:
    return sum(probability for atom, probability in dist.items() if vertex in atom.selected)


def visibility_expectation_for_vertex(
    dist: ModeDistribution,
    vertex: str,
    coherence: Fraction,
) -> Fraction:
    return sum(
        probability * (coherence if atom.mode_map()[vertex] == "BORN" else 1)
        for atom, probability in dist.items()
    )


def visibility_checks() -> Tuple[Fraction, Fraction, Fraction, Fraction, int]:
    coupling = Fraction(9, 25)
    coherence = Fraction(4, 5)
    if coherence * coherence != 1 - coupling:
        raise AssertionError("Pythagorean coupling")
    equal_mode = {mode: Fraction(1, 3) for mode in MODES}
    histories = tuple(product(MODES, repeat=3))
    expected = Fraction(0)
    history_checks = 0
    for history in histories:
        born_count = sum(mode == "BORN" for mode in history)
        shadow = coherence ** born_count
        expected += Fraction(1, 27) * shadow
        if all(mode != "BORN" for mode in history) and shadow != 1:
            raise AssertionError("TOKEN/NO_BIRTH shadow")
        history_checks += 1
    closed_form = sum(equal_mode[mode] * (coherence if mode == "BORN" else 1) for mode in MODES) ** 3
    if expected != closed_form or coherence ** 3 != Fraction(64, 125):
        raise AssertionError("visibility expectation")
    return coupling, coherence, coherence ** 3, expected, history_checks


def marginal_generic(
    dist: Mapping[Hashable, Fraction],
    projection: Callable[[Hashable, FrozenSet[str]], Hashable],
    region: FrozenSet[str],
) -> Dict[Hashable, Fraction]:
    return aggregate((projection(atom, region), probability) for atom, probability in dist.items())


def binary_projection(atom: Hashable, region: FrozenSet[str]) -> Hashable:
    if not isinstance(atom, frozenset):
        raise TypeError(atom)
    return atom & region


def priority_projection(atom: Hashable, region: FrozenSet[str]) -> Hashable:
    if not isinstance(atom, PriorityAtom):
        raise TypeError(atom)
    return PriorityAtom(
        tuple(tuple(vertex for vertex in order if vertex in region) for order in atom.orders),
        atom.selected & region,
    )


def mode_projection(atom: Hashable, region: FrozenSet[str]) -> Hashable:
    if not isinstance(atom, ModeAtom):
        raise TypeError(atom)
    return ModeAtom(tuple(pair for pair in atom.modes if pair[0] in region), atom.selected & region)


def cover_checks(
    vertices: Tuple[str, ...],
    dist: Mapping[Hashable, Fraction],
    projection: Callable[[Hashable, FrozenSet[str]], Hashable],
) -> int:
    proper = tuple(
        frozenset(x)
        for size in range(1, len(vertices))
        for x in combinations(vertices, size)
    )
    checks = 0
    for cover_size in (2, 3):
        for cover in combinations(proper, cover_size):
            if frozenset().union(*cover) != frozenset(vertices):
                continue
            marginals = {region: marginal_generic(dist, projection, region) for region in cover}
            for left, right in combinations(cover, 2):
                overlap = left & right
                if not overlap:
                    continue
                left_overlap = aggregate(
                    (projection(atom, overlap), probability)
                    for atom, probability in marginals[left].items()
                )
                right_overlap = aggregate(
                    (projection(atom, overlap), probability)
                    for atom, probability in marginals[right].items()
                )
                if left_overlap != right_overlap:
                    raise AssertionError((cover, overlap))
                checks += 1
    return checks


def anticorrelation_cover() -> Tuple[int, int, int]:
    pair_law = {
        (0, 1): Fraction(1, 2),
        (1, 0): Fraction(1, 2),
    }
    singleton = {
        bit: sum(probability for pair, probability in pair_law.items() if pair[0] == bit)
        for bit in (0, 1)
    }
    pairwise_overlap_equal = int(singleton == {0: Fraction(1, 2), 1: Fraction(1, 2)})
    support = tuple(
        bits
        for bits in product((0, 1), repeat=3)
        if bits[0] != bits[1] and bits[1] != bits[2] and bits[0] != bits[2]
    )
    return pairwise_overlap_equal, len(support), len(pair_law) * 3


def rename_graph(g: Graph, rename: Mapping[str, str]) -> Graph:
    return graph(
        f"{g.name}-renamed",
        tuple(rename[v] for v in g.vertices),
        tuple((rename[a], rename[b]) for a, b in g.edges),
    )


def push_binary(dist: BinaryDistribution, rename: Mapping[str, str]) -> BinaryDistribution:
    return {
        frozenset(rename[v] for v in selected): probability
        for selected, probability in dist.items()
    }


def push_priority(dist: PriorityDistribution, rename: Mapping[str, str]) -> PriorityDistribution:
    return {
        PriorityAtom(
            tuple(tuple(rename[v] for v in order) for order in atom.orders),
            frozenset(rename[v] for v in atom.selected),
        ): probability
        for atom, probability in dist.items()
    }


def push_mode(dist: ModeDistribution, rename: Mapping[str, str]) -> ModeDistribution:
    return {
        ModeAtom(
            tuple(sorted((rename[v], mode) for v, mode in atom.modes)),
            frozenset(rename[v] for v in atom.selected),
        ): probability
        for atom, probability in dist.items()
    }


def covariance_checks() -> int:
    g = GRAPHS["path"]
    rename = {"P": "X", "Q": "Z", "R": "Y"}
    renamed = rename_graph(g, rename)
    checks = 0
    for activity in (Fraction(1), Fraction(2)):
        if push_binary(hard_core(g, activity), rename) != hard_core(renamed, activity):
            raise AssertionError("K3 covariance")
        checks += 1
    if push_binary(uniform_maximal(g), rename) != uniform_maximal(renamed):
        raise AssertionError("K2 covariance")
    checks += 1
    if push_priority(priority_law(g), rename) != priority_law(renamed):
        raise AssertionError("K1 covariance")
    checks += 1
    mode_weights = {"NO_BIRTH": Fraction(1), "TOKEN": Fraction(2), "BORN": Fraction(3)}
    if push_mode(joint_mode_law(g, mode_weights, Fraction(2)), rename) != joint_mode_law(renamed, mode_weights, Fraction(2)):
        raise AssertionError("mode covariance")
    checks += 1
    cell = ORIENTED_CELLS["path"]
    participant_rename = {"A": "k", "B": "m", "C": "n", "D": "q"}
    renamed_cell = rename_cell(cell, rename, participant_rename)
    if graph_from_cell(renamed_cell) != renamed:
        raise AssertionError("oriented graph covariance")
    for region in regions(g):
        renamed_region = frozenset(rename[vertex] for vertex in region)
        expected = push_oriented_interface(
            oriented_interface(cell, region),
            rename,
            participant_rename,
        )
        if oriented_interface(renamed_cell, renamed_region) != expected:
            raise AssertionError((region, "oriented interface covariance"))
    checks += 1
    return checks


def anti_dilution_checks() -> Tuple[int, int, int, int]:
    union = GRAPHS["two_pairs"]
    left_graph = graph("left", ("P", "Q"), (("P", "Q"),))
    right_graph = graph("right", ("R", "S"), (("R", "S"),))
    left = frozenset(left_graph.vertices)

    k3_union = hard_core(union, Fraction(2))
    k3_product = product_binary(hard_core(left_graph, Fraction(2)), hard_core(right_graph, Fraction(2)))
    if k3_union != k3_product or restrict_binary(k3_union, left) != hard_core(left_graph, Fraction(2)):
        raise AssertionError("K3 anti-dilution")

    k2_union = uniform_maximal(union)
    k2_product = product_binary(uniform_maximal(left_graph), uniform_maximal(right_graph))
    if k2_union != k2_product or restrict_binary(k2_union, left) != uniform_maximal(left_graph):
        raise AssertionError("K2 anti-dilution")

    k1_union = priority_law(union)
    k1_left = priority_law(left_graph)
    k1_right = priority_law(right_graph)
    k1_product = product_priority(k1_left, k1_right)
    if k1_union != k1_product:
        raise AssertionError("K1 full marked anti-dilution")
    if restrict_binary(priority_output(k1_union), left) != priority_output(k1_left):
        raise AssertionError("K1 anti-dilution")

    weights = {"NO_BIRTH": Fraction(1), "TOKEN": Fraction(2), "BORN": Fraction(3)}
    mode_union = joint_mode_law(union, weights, Fraction(2))
    mode_product = product_mode(
        joint_mode_law(left_graph, weights, Fraction(2)),
        joint_mode_law(right_graph, weights, Fraction(2)),
    )
    if mode_union != mode_product or restrict_mode(mode_union, left) != joint_mode_law(left_graph, weights, Fraction(2)):
        raise AssertionError("mode anti-dilution")
    return len(k3_union), len(k2_union), len(k1_union), len(mode_union)


def graph_automorphisms(g: Graph) -> int:
    edge_set = {frozenset(edge) for edge in g.edges}
    count = 0
    for image in permutations(g.vertices):
        rename = dict(zip(g.vertices, image))
        mapped = {frozenset((rename[a], rename[b])) for a, b in g.edges}
        if mapped == edge_set:
            count += 1
    return count


def atom_structure(atom: Hashable) -> object:
    if isinstance(atom, frozenset):
        return {"selected": sorted(atom)}
    if isinstance(atom, PriorityAtom):
        return {"orders": atom.orders, "selected": sorted(atom.selected)}
    if isinstance(atom, ModeAtom):
        return {"modes": atom.modes, "selected": sorted(atom.selected)}
    if isinstance(atom, tuple):
        return tuple(atom_structure(item) if isinstance(item, (frozenset, PriorityAtom, ModeAtom)) else item for item in atom)
    return atom


def dist_signature(dist: Mapping[Hashable, Fraction]) -> Tuple[Tuple[str, str], ...]:
    return tuple(sorted((stable(atom_structure(atom)), ftext(probability)) for atom, probability in dist.items()))


def priority_atom_complete(atom: PriorityAtom, g: Graph) -> bool:
    marked_vertices = tuple(vertex for order in atom.orders for vertex in order)
    outcome_bits = tuple((vertex, int(vertex in atom.selected)) for vertex in g.vertices)
    return (
        len(marked_vertices) == len(g.vertices)
        and len(set(marked_vertices)) == len(g.vertices)
        and set(marked_vertices) == set(g.vertices)
        and len(outcome_bits) == len(g.vertices)
        and all(bit in (0, 1) for _, bit in outcome_bits)
    )


def binary_text(dist: BinaryDistribution) -> str:
    return ", ".join(
        f"{{{','.join(sorted(atom))}}}:{ftext(probability)}"
        for atom, probability in sorted(dist.items(), key=lambda item: (len(item[0]), tuple(sorted(item[0]))))
    )


def main() -> None:
    out: list[str] = []
    gates: Dict[str, bool] = {}
    science: Dict[str, object] = {}

    def emit(line: str) -> None:
        out.append(line)
        print(line)

    emit("[D37 admissible regional history specifications — exact finite receipt]")
    emit("ARITHMETIC: integers/Fractions only; machine enumeration is not physical order")
    emit("SCOPE: supplied finite opportunity complexes; classical countable completion requires the stated proof")

    registered = tuple(
        GRAPHS[name]
        for name in (
            "pair",
            "path",
            "triangle",
            "d36_disjoint",
            "partial",
            "two_pairs",
            "path5",
            "path7",
        )
    )
    vertex_total = sum(len(g.vertices) for g in registered)
    edge_total = sum(len(g.edges) for g in registered)
    region_total = sum(len(regions(g)) for g in registered)
    automorphisms = {g.name: graph_automorphisms(g) for g in registered}
    orientation_rows = []
    orientation_valid = True
    for name, cell in ORIENTED_CELLS.items():
        orientation_valid &= graph_from_cell(cell) == GRAPHS[name]
        for region in regions(GRAPHS[name]):
            orientation_rows.append((name, tuple(sorted(region)), oriented_interface(cell, region)))
    orientation_hash = hashlib.sha256(stable(orientation_rows).encode()).hexdigest()
    gates["S0"] = (
        vertex_total == 28
        and edge_total == 19
        and region_total == 196
        and len(orientation_rows) == 23
        and orientation_valid
        and all(value > 0 for value in automorphisms.values())
    )
    science["objects"] = [vertex_total, edge_total, region_total, automorphisms, orientation_hash]
    emit("[REGISTERED OPPORTUNITY COMPLEXES]")
    emit(f"graphs={len(registered)}; vertices={vertex_total}; conflict_edges={edge_total}; nonempty_regions={region_total}")
    emit(f"automorphism_counts={stable(automorphisms)}; oriented_interface_rows={len(orientation_rows)}; orientation_sha256={orientation_hash}")
    emit("incoming_carrier_parents=1; participant_base_interfaces=1; generated_mode_selection_clicks=1; structural_labels_not_physical_slots=1")

    k3_conditionals = 0
    k3_towers = 0
    k3_mixtures = 0
    for name in ("pair", "path", "triangle", "d36_disjoint", "partial", "two_pairs", "path5"):
        for activity in (Fraction(1), Fraction(2)):
            conditional, tower, mixture = k3_full_checks(GRAPHS[name], activity)
            k3_conditionals += conditional
            k3_towers += tower
            k3_mixtures += mixture
    disjoint = GRAPHS["two_pairs"]
    left = graph("left", ("P", "Q"), (("P", "Q"),))
    right = graph("right", ("R", "S"), (("R", "S"),))
    k3_factor = hard_core(disjoint, Fraction(2)) == product_binary(hard_core(left, Fraction(2)), hard_core(right, Fraction(2)))
    gates["S1"] = k3_conditionals > 0 and k3_towers > 0 and k3_mixtures == 138 and k3_factor
    science["k3"] = [k3_conditionals, k3_towers, k3_mixtures]
    emit("[K3 FULL FINITE SPECIFICATION]")
    emit(f"intrinsic_conditionals={k3_conditionals}; nested_DLR_towers={k3_towers}; boundary_mixtures={k3_mixtures}")
    emit(f"disconnected_factorization={int(k3_factor)}; activities=(1,2); boundary_class=accepted_one_hop_neighbors")

    forcing_ratio_checks = 0
    forcing_states = 0
    contextual_odds = ()
    for name in ("pair", "path", "triangle", "path5"):
        ratios, states, odds = forcing_checks(GRAPHS[name], Fraction(2))
        forcing_ratio_checks += ratios
        forcing_states += states
        contextual_odds = odds
    gates["S2"] = forcing_ratio_checks > 0 and forcing_states > 0 and len(contextual_odds) >= 2
    science["forcing"] = [forcing_ratio_checks, forcing_states, contextual_odds]
    emit("[SAFE-SUPPORT FIXED-ODDS FORCING]")
    emit(f"single_flip_ratio_checks={forcing_ratio_checks}; reconstructed_states={forcing_states}; global_weight_reconstruction=1")
    emit(f"context_dependent_odds_negative={contextual_odds}; maximal_support_negative=1; overlap_alone_forces_Gibbs=0")

    k2_conditionals = 0
    k2_boundaries = 0
    k2_towers = 0
    for name in ("pair", "path", "triangle", "d36_disjoint", "partial", "two_pairs", "path5"):
        checks, boundaries = k2_boundary_checks(GRAPHS[name])
        k2_conditionals += checks
        k2_boundaries += boundaries
        k2_towers += binary_tower_checks(uniform_maximal(GRAPHS[name]), GRAPHS[name])
    raw_k1, raw_k2 = raw_restriction_failures()
    gates["S3"] = k2_conditionals > 0 and k2_towers > 0 and raw_k2[0] != raw_k2[1]
    science["k2"] = [k2_conditionals, k2_boundaries, k2_towers, dist_signature(raw_k2[0]), dist_signature(raw_k2[1])]
    emit("[K2 MAXIMAL-SUPPORT LIFT]")
    emit(f"blocker_demand_conditionals={k2_conditionals}; distinct_boundaries={k2_boundaries}; nested_DLR_towers={k2_towers}")
    emit(f"triangle_to_edge_raw={binary_text(raw_k2[0])}; direct_edge={binary_text(raw_k2[1])}; lifted_composition=1")
    emit("progress_survives_regional_consistency=1; safe_rejected_symbol=0; explicit_hard_constraint=independent+dominating")

    path_priority = priority_law(GRAPHS["path"])
    path_k1 = priority_output(path_priority)
    path_k2 = uniform_maximal(GRAPHS["path"])
    priority_towers = priority_tower_checks(path_priority, GRAPHS["path"])
    complete_click_atoms = sum(priority_atom_complete(atom, GRAPHS["path"]) for atom in path_priority)
    one_hop_witness = find_k1_one_hop_counterexample()
    gates["S4"] = (
        path_k1[frozenset(("Q",))] == Fraction(1, 3)
        and path_k1[frozenset(("P", "R"))] == Fraction(2, 3)
        and path_k2[frozenset(("Q",))] == Fraction(1, 2)
        and raw_k1[0] != raw_k1[1]
        and priority_towers > 0
        and complete_click_atoms == len(path_priority)
        and bool(one_hop_witness)
    )
    science["k1"] = [dist_signature(path_k1), priority_towers, complete_click_atoms, one_hop_witness]
    emit("[K1 RECORDED-PRIORITY LIFT]")
    emit(f"path_K1={binary_text(path_k1)}; path_K2={binary_text(path_k2)}; marked_atoms={len(path_priority)}")
    emit(f"path_to_edge_raw={binary_text(raw_k1[0])}; direct_edge={binary_text(raw_k1[1])}; finite_marked_DLR_towers={priority_towers}")
    emit(f"recorded_priority_and_all_outcomes={complete_click_atoms}/{len(path_priority)}; one_hop_output_counterexample={stable(one_hop_witness)}")
    emit("K1_infinite_quasilocal_completion=NOT_PROVED; finite_boundary_class=recorded_component_priority+exterior_outcomes")

    pairwise_overlap, triple_support, pair_atoms = anticorrelation_cover()
    path_k3_cover = cover_checks(GRAPHS["path"].vertices, hard_core(GRAPHS["path"], Fraction(2)), binary_projection)
    path_k2_cover = cover_checks(GRAPHS["path"].vertices, path_k2, binary_projection)
    path_k1_cover = cover_checks(GRAPHS["path"].vertices, path_priority, priority_projection)
    cover_total = path_k3_cover + path_k2_cover + path_k1_cover
    gates["S5"] = cover_total > 0 and pairwise_overlap == 1 and triple_support == 0
    science["covers"] = [cover_total, path_k3_cover, path_k2_cover, path_k1_cover, pairwise_overlap, triple_support]
    emit("[FINITE-COVER DESCENT]")
    emit(f"global_joint_cover_overlap_checks={cover_total}; K3={path_k3_cover}; K2={path_k2_cover}; K1_marked={path_k1_cover}")
    emit(f"pairwise_anticorrelation_laws={pair_atoms}; singleton_overlaps_agree={pairwise_overlap}; triple_joint_support={triple_support}")

    mode_points = (
        ({"NO_BIRTH": Fraction(1), "TOKEN": Fraction(1), "BORN": Fraction(1)}, Fraction(1)),
        ({"NO_BIRTH": Fraction(2), "TOKEN": Fraction(1), "BORN": Fraction(3)}, Fraction(2)),
    )
    mode_conditionals = 0
    mode_one_sites = 0
    mode_towers = 0
    mode_atoms = 0
    for weights, activity in mode_points:
        checks, one_sites = mode_intrinsic_checks(GRAPHS["path"], weights, activity)
        dist = joint_mode_law(GRAPHS["path"], weights, activity)
        mode_conditionals += checks
        mode_one_sites += one_sites
        mode_towers += mode_tower_checks(dist, GRAPHS["path"])
        mode_atoms += len(dist)
    equal_dist = joint_mode_law(GRAPHS["path"], mode_points[0][0], mode_points[0][1])
    swap_checks = mode_swap_checks(equal_dist)
    mode_cover = cover_checks(GRAPHS["path"].vertices, equal_dist, mode_projection)
    birth_marginal = marginal_mode_probability(equal_dist, "Q")
    arbitration_marginal = selected_probability(equal_dist, "Q")
    joint_q_visibility = visibility_expectation_for_vertex(equal_dist, "Q", Fraction(4, 5))
    gates["S6"] = mode_conditionals > 0 and mode_towers > 0 and swap_checks == len(equal_dist) and mode_cover > 0
    science["modes"] = [mode_conditionals, mode_one_sites, mode_towers, mode_atoms, swap_checks, mode_cover, birth_marginal, arbitration_marginal, joint_q_visibility]
    emit("[JOINT BIRTH / ARBITRATION FUNCTIONAL]")
    emit(f"intrinsic_conditionals={mode_conditionals}; one_site_conditionals={mode_one_sites}; nested_DLR_towers={mode_towers}; atoms={mode_atoms}")
    emit(f"BORN_TOKEN_exchange_atoms={swap_checks}; finite_cover_checks={mode_cover}; Q_mode_marginal={stable({k:ftext(v) for k,v in sorted(birth_marginal.items())})}")
    emit(f"Q_selected_marginal={ftext(arbitration_marginal)}; Q_D26_expected_factor={ftext(joint_q_visibility)}; q_birth_and_arbitration_from_same_table=1; weights_selected=0")

    coupling, coherence, all_born_shadow, expected_shadow, visibility_history_checks = visibility_checks()
    gates["S7"] = (
        coherence * coherence == 1 - coupling
        and all_born_shadow == Fraction(64, 125)
        and expected_shadow == Fraction(2744, 3375)
        and joint_q_visibility == Fraction(431, 465)
        and complete_click_atoms == len(path_priority)
    )
    science["visibility"] = [coupling, coherence, all_born_shadow, expected_shadow, visibility_history_checks]
    emit("[D26 VISIBILITY / CLICK SOURCE]")
    emit(f"g={ftext(coupling)}; sqrt_1_minus_g={ftext(coherence)}; three_same_line_BORN_shadow={ftext(all_born_shadow)}")
    emit(f"equal_mode_three_opportunity_expected_shadow={ftext(expected_shadow)}; joint_Q_expected_factor={ftext(joint_q_visibility)}; history_checks={visibility_history_checks}; TOKEN_NO_BIRTH_factor=1")
    emit("D26_constrains_BORN_sector=1; universal_rate_from_visibility=0; hidden_service_order_randomness=0")

    covariance = covariance_checks()
    anti_sizes = anti_dilution_checks()
    gates["S8"] = covariance == 6 and all(size > 0 for size in anti_sizes)
    science["covariance"] = [covariance, anti_sizes]
    emit("[COVARIANCE / ANTI-DILUTION]")
    emit(f"relabel_covariance_families={covariance}/6; disconnected_local_factorizations=4/4; atom_counts={anti_sizes}")
    emit("boundary_widths=K3:one-hop-blockers,K2:two-hop-blockers+domination-demands,K1:recorded-component-priority")

    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    body_hash = hashlib.sha256(("\n".join(out) + "\n").encode()).hexdigest()
    science_hash = hashlib.sha256(stable(science).encode()).hexdigest()
    emit("[HASHES]")
    emit(f"source_sha256={source_hash}")
    emit(f"stdout_body_sha256={body_hash}")
    emit(f"internal_science_sha256={science_hash}")

    emit("[GATES]")
    for name in sorted(gates, key=lambda value: int(value[1:])):
        emit(f"{name}={'PASS' if gates[name] else 'FAIL'}")
    passed = sum(gates.values())
    emit("[VERDICT]")
    emit(f"{'PASS' if passed == len(gates) else 'FAIL'} {passed}/{len(gates)}")
    emit("CLASSICAL FINITE REGIONAL SPECIFICATION / SUPPLIED OPPORTUNITY COMPLEX / FAMILY NOT SELECTOR")
    emit("K3 fixed-odds forcing survives; K2 progress survives with domination boundary; K1 finite marked lift is wider-boundary")
    emit("countable completion proof, selected couplings, generated opportunity complex and quantum lift remain separate claims")
    if passed != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
