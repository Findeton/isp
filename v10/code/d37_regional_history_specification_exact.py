#!/usr/bin/env python3
"""D37 exact finite regional-history specification receipt.

Standard-library only.  Every probability is a Fraction.  Enumeration order is
never interpreted as physical time or as an arbitration mark.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Callable, Dict, FrozenSet, Hashable, Iterable, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
D36B_PATH = ROOT / "v10" / "code" / "d36b_actor_record_refinement_exact.py"
D36B_SHA256 = "57ff22ab4711b63d476192c2ff19b02bb7f76fda5124b4d1afd23d30a20b376b"

if hashlib.sha256(D36B_PATH.read_bytes()).hexdigest() != D36B_SHA256:
    raise RuntimeError("D36b actor adapter source hash mismatch")
_D36B_SPEC = importlib.util.spec_from_file_location("d36b_adapter_locked", D36B_PATH)
assert _D36B_SPEC and _D36B_SPEC.loader
d36b = importlib.util.module_from_spec(_D36B_SPEC)
sys.modules["d36b_adapter_locked"] = d36b
_D36B_SPEC.loader.exec_module(d36b)


def stable(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=repr)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(value: object) -> str:
    return hashlib.sha256(stable(value).encode()).hexdigest()


def canonical_id(kind: str, *fields: Hashable) -> Tuple[Hashable, ...]:
    """Injective theorem-level identity on finite typed content.

    SHA-256 remains a receipt/serialization checksum only.  The tagged tuple
    itself is the mathematical record identity, so countably many distinct
    finite contents do not collide by construction.
    """
    return ("D37_CANONICAL_ID", kind, fields)


def injective_actor_index(kind: str, label: str) -> int:
    """Inject finite UTF-8 structural labels into arbitrary-precision N."""
    payload = stable(("D37_ACTOR_INDEX", kind, label)).encode()
    return int.from_bytes(b"\x01" + payload, "big")


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
    parent_lines: Tuple[Tuple[str, str], ...]
    proposal_types: Tuple[Tuple[str, str], ...]

    def __post_init__(self) -> None:
        vertices = self.vertices
        if len(set(vertices)) != len(vertices):
            raise ValueError("duplicate oriented proposal")
        if set(dict(self.parent_lines)) != set(vertices):
            raise ValueError("parent-line domain")
        if set(dict(self.proposal_types)) != set(vertices):
            raise ValueError("proposal-type domain")
        if any(not participants for _, participants in self.proposals):
            raise ValueError("proposal without participants")
        if any(kind != "TRANSACTION_OPPORTUNITY" for _, kind in self.proposal_types):
            raise ValueError("unsupported opportunity type")

    @property
    def vertices(self) -> Tuple[str, ...]:
        return tuple(name for name, _ in self.proposals)

    def participants(self, proposal: str) -> Tuple[str, ...]:
        return dict(self.proposals)[proposal]

    def parent_line(self, proposal: str) -> str:
        return dict(self.parent_lines)[proposal]

    def proposal_type(self, proposal: str) -> str:
        return dict(self.proposal_types)[proposal]


def oriented_cell(
    name: str,
    proposals: Sequence[Tuple[str, Sequence[str]]],
    parent_lines: Mapping[str, str] | None = None,
) -> OrientedCell:
    normalized = tuple((proposal, tuple(participants)) for proposal, participants in proposals)
    vertices = tuple(proposal for proposal, _ in normalized)
    lines = {
        proposal: (
            parent_lines[proposal]
            if parent_lines is not None
            else f"line:{proposal}"
        )
        for proposal in vertices
    }
    return OrientedCell(
        name,
        normalized,
        tuple((proposal, lines[proposal]) for proposal in vertices),
        tuple((proposal, "TRANSACTION_OPPORTUNITY") for proposal in vertices),
    )


ORIENTED_CELLS: Dict[str, OrientedCell] = {
    "pair": oriented_cell("pair", (("P", ("A", "B")), ("Q", ("A", "B")))),
    "path": oriented_cell(
        "path",
        (("P", ("A", "B")), ("Q", ("B", "C")), ("R", ("C", "D"))),
    ),
    "triangle": oriented_cell(
        "triangle",
        (("P", ("A", "B")), ("Q", ("B", "C")), ("R", ("C", "A"))),
    ),
    "d36_disjoint": oriented_cell(
        "d36_disjoint",
        (("P", ("A", "B")), ("Q", ("C", "D"))),
    ),
    "partial": oriented_cell(
        "partial",
        (("P", ("A", "B", "C")), ("Q", ("C", "D"))),
    ),
    "two_pairs": oriented_cell(
        "two_pairs",
        (
            ("P", ("A", "B")),
            ("Q", ("A", "B")),
            ("R", ("C", "D")),
            ("S", ("C", "D")),
        ),
    ),
}


BASE_RECORD = "BASE_RECORD"
OPPORTUNITY_PARENT = "OPPORTUNITY_PARENT"
DORMANT_TOKEN = "DORMANT_TOKEN"
MODE_CLICK = "MODE_CLICK"
BORN_CARRIER = "BORN_CARRIER"
TOKEN_ACTIVATION = "TOKEN_ACTIVATION"
PRIORITY_CLICK = "PRIORITY_CLICK"
SELECTION_CLICK = "SELECTION_CLICK"
D36_PREPARE = "D36_PREPARE"


def base_record_id(participant: str) -> Tuple[Hashable, ...]:
    return canonical_id(BASE_RECORD, participant, 0)


def opportunity_parent_id(
    proposal: str,
    parent_line: str,
    proposal_type: str,
    predecessor: Hashable = "",
) -> Tuple[Hashable, ...]:
    return canonical_id(
        OPPORTUNITY_PARENT,
        proposal,
        parent_line,
        proposal_type,
        predecessor,
    )


def dormant_token_id(proposal: str, parent_line: str) -> Tuple[Hashable, ...]:
    return canonical_id(DORMANT_TOKEN, proposal, parent_line, "coherence-neutral")


def graph_from_cell(cell: OrientedCell) -> Graph:
    edges = []
    for (left, left_participants), (right, right_participants) in combinations(cell.proposals, 2):
        if set(left_participants) & set(right_participants):
            edges.append((left, right))
    return graph(cell.name, cell.vertices, edges)


def oriented_interface(
    cell: OrientedCell,
    region: FrozenSet[str],
) -> Tuple[Tuple[Tuple[str, str, str], ...], Tuple[str, ...], Tuple[Tuple[str, str], ...]]:
    inside_participants = {
        participant
        for proposal in region
        for participant in cell.participants(proposal)
    }
    incoming = tuple(sorted(
        [
            (BASE_RECORD, participant, base_record_id(participant))
            for participant in inside_participants
        ]
        + [
            (
                OPPORTUNITY_PARENT,
                proposal,
                opportunity_parent_id(
                    proposal,
                    cell.parent_line(proposal),
                    cell.proposal_type(proposal),
                ),
            )
            for proposal in region
        ]
    ))
    outside = set(cell.vertices) - region
    lateral = tuple(sorted(
        proposal
        for proposal in outside
        if inside_participants & set(cell.participants(proposal))
    ))
    generated = tuple(sorted(
        [(MODE_CLICK, proposal) for proposal in region]
        + [(SELECTION_CLICK, proposal) for proposal in region]
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
        tuple(
            (
                proposal_rename[proposal],
                (
                    f"line:{proposal_rename[proposal]}"
                    if line == f"line:{proposal}"
                    else f"renamed:{line}"
                ),
            )
            for proposal, line in cell.parent_lines
        ),
        tuple(
            (proposal_rename[proposal], proposal_type)
            for proposal, proposal_type in cell.proposal_types
        ),
    )


def push_oriented_interface(
    interface: Tuple[Tuple[Tuple[str, str, str], ...], Tuple[str, ...], Tuple[Tuple[str, str], ...]],
    proposal_rename: Mapping[str, str],
    participant_rename: Mapping[str, str],
    renamed_cell: OrientedCell,
) -> Tuple[Tuple[Tuple[str, str, str], ...], Tuple[str, ...], Tuple[Tuple[str, str], ...]]:
    incoming, lateral, generated = interface
    pushed_incoming = tuple(sorted(
        (
            kind,
            participant_rename[role],
            base_record_id(participant_rename[role]),
        )
        if kind == BASE_RECORD
        else (
            kind,
            proposal_rename[role],
            opportunity_parent_id(
                proposal_rename[role],
                renamed_cell.parent_line(proposal_rename[role]),
                renamed_cell.proposal_type(proposal_rename[role]),
            ),
        )
        for kind, role, _ in incoming
    ))
    pushed_lateral = tuple(sorted(proposal_rename[value] for value in lateral))
    pushed_generated = tuple(sorted((tag, proposal_rename[value]) for tag, value in generated))
    return pushed_incoming, pushed_lateral, pushed_generated


def interface_content_valid(
    cell: OrientedCell,
    region: FrozenSet[str],
    interface: Tuple[Tuple[Tuple[str, str, str], ...], Tuple[str, ...], Tuple[Tuple[str, str], ...]],
) -> bool:
    incoming, lateral, generated = interface
    participants = {
        participant
        for proposal in region
        for participant in cell.participants(proposal)
    }
    base_rows = tuple(row for row in incoming if row[0] == BASE_RECORD)
    parent_rows = tuple(row for row in incoming if row[0] == OPPORTUNITY_PARENT)
    base_ok = {
        (role, record_id) for _, role, record_id in base_rows
    } == {
        (participant, base_record_id(participant)) for participant in participants
    }
    parent_ok = {
        (role, record_id) for _, role, record_id in parent_rows
    } == {
        (
            proposal,
            opportunity_parent_id(
                proposal,
                cell.parent_line(proposal),
                cell.proposal_type(proposal),
            ),
        )
        for proposal in region
    }
    distinct_parent_ids = len({record_id for _, _, record_id in parent_rows}) == len(region)
    actual_lateral = {
        proposal
        for proposal in set(cell.vertices) - region
        if participants & set(cell.participants(proposal))
    }
    generated_ok = set(generated) == (
        {(MODE_CLICK, proposal) for proposal in region}
        | {(SELECTION_CLICK, proposal) for proposal in region}
    )
    return (
        base_ok
        and parent_ok
        and distinct_parent_ids
        and set(lateral) == actual_lateral
        and generated_ok
        and len(incoming) == len(participants) + len(region)
    )


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
    ratio_edges = set()
    for selected in dist:
        for vertex in g.vertices:
            if vertex in selected:
                continue
            candidate = selected | {vertex}
            if candidate not in dist:
                continue
            if dist[candidate] / dist[selected] != activity:
                raise AssertionError((g.name, selected, candidate, "single-flip ratio"))
            ratio_edges.add((selected, candidate))

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
    return len(ratio_edges), len(reconstructed), tuple(sorted(ftext(x) for x in odds))


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
class CausalEvent:
    event_id: Hashable
    kind: str
    proposal: str
    owner: str
    wire: str
    parents: Tuple[Hashable, ...]
    payload: Tuple[Tuple[str, object], ...]

    def payload_map(self) -> Dict[str, object]:
        return dict(self.payload)


def event_id(
    kind: str,
    proposal: str,
    owner: str,
    wire: str,
    parents: Tuple[Hashable, ...],
    payload: Tuple[Tuple[str, object], ...],
) -> Tuple[Hashable, ...]:
    return canonical_id("CAUSAL_EVENT", kind, proposal, owner, wire, parents, payload)


def event(
    kind: str,
    proposal: str,
    owner: str,
    wire: str,
    parents: Sequence[Hashable],
    payload: Mapping[str, object],
) -> CausalEvent:
    normalized_parents = tuple(parents)
    normalized_payload = tuple(sorted(payload.items()))
    return CausalEvent(
        event_id(kind, proposal, owner, wire, normalized_parents, normalized_payload),
        kind,
        proposal,
        owner,
        wire,
        normalized_parents,
        normalized_payload,
    )


def base_event(participant: str) -> CausalEvent:
    return CausalEvent(
        base_record_id(participant),
        BASE_RECORD,
        "",
        f"participant:{participant}",
        f"participant:{participant}",
        (),
        (("participant", participant), ("version", "0")),
    )


def opportunity_parent_event(
    cell: OrientedCell,
    proposal: str,
    parent_line: str,
    predecessor: Hashable = "",
    shared_line: bool = False,
) -> CausalEvent:
    proposal_type = cell.proposal_type(proposal)
    return CausalEvent(
        opportunity_parent_id(proposal, parent_line, proposal_type, predecessor),
        OPPORTUNITY_PARENT,
        proposal,
        f"source:{proposal}",
        f"parent-line:{parent_line}" if shared_line else f"proposal:{proposal}",
        (predecessor,) if predecessor else (),
        (("parent_line", parent_line), ("proposal_type", proposal_type)),
    )


def dormant_token_event(proposal: str, parent_line: str) -> CausalEvent:
    return CausalEvent(
        dormant_token_id(proposal, parent_line),
        DORMANT_TOKEN,
        proposal,
        f"token:{proposal}",
        f"token:{proposal}",
        (),
        (("control", "coherence-neutral"), ("parent_line", parent_line)),
    )


def event_body_digest(
    cell: OrientedCell,
    proposal: str,
) -> str:
    bases = tuple(
        (participant, base_record_id(participant))
        for participant in cell.participants(proposal)
    )
    return d36b.digest(("d37-d36-body", proposal, cell.participants(proposal), bases))


def structural_actor_index(kind: str, label: str) -> int:
    return injective_actor_index(kind, label)


def d36_carrier_record(
    cell: OrientedCell,
    proposal: str,
    mode: str,
    parent_line: str,
) -> object:
    """Build the exact D36b carrier record used by the downstream envelope."""
    tx_index = structural_actor_index("T", proposal)
    initiator = cell.participants(proposal)[0]
    initiator_index = structural_actor_index("P", initiator)
    seed = d36b.make_record("P", initiator_index, "SEED", (), (initiator, 0))
    payload = (
        "d37-regional-adapter",
        proposal,
        parent_line,
        event_body_digest(cell, proposal),
    )
    if mode == "BORN":
        return d36b.make_record(
            "T",
            tx_index,
            "T0_BIRTH",
            (seed.record_id,),
            payload,
        )
    if mode == "TOKEN":
        slot = d36b.make_record(
            "T",
            tx_index,
            "DORMANT_SLOT",
            (),
            ("d37-regional-adapter", proposal, parent_line),
        )
        return d36b.make_record(
            "T",
            tx_index,
            "SLOT_ACTIVATION",
            (slot.record_id, seed.record_id),
            payload,
        )
    raise AssertionError(("D36 carrier mode", mode))


def d36_prepare_adapter(
    cell: OrientedCell,
    proposal: str,
    participant: str,
    mode: str,
    parent_line: str,
) -> Tuple[object, object, object]:
    """Return an exact D36b Record/Envelope/ParticipantActor acceptance cell."""
    tx_index = structural_actor_index("T", proposal)
    participant_index = structural_actor_index("P", participant)
    evidence = d36_carrier_record(cell, proposal, mode, parent_line)
    body_digest = event_body_digest(cell, proposal)
    attempt_id = d36b.structural_attempt_id(evidence, body_digest)
    capability = d36b.capability_id(tx_index, participant_index, participant)
    envelope = d36b.signed_envelope(
        d36b.PREPARE,
        "T",
        tx_index,
        "P",
        participant_index,
        tx_index,
        participant_index,
        body_digest,
        0,
        capability,
        attempt_id,
        "",
        evidence,
        0,
    )
    seed = d36b.make_record("P", participant_index, "SEED", (), (participant, 0))
    actor = d36b.ParticipantActor(
        participant,
        0,
        seed.record_id,
        seed.record_id,
        "",
        (),
        (),
        (capability,),
        (),
        (),
        (envelope,),
    )
    if not d36b.participant_accepts_prepare(actor, envelope):
        raise AssertionError("D36 participant rejected regional PREPARE adapter")
    return evidence, envelope, actor


def build_typed_history(
    cell: OrientedCell,
    modes: Mapping[str, str],
    selected: Selected,
    priority_orders: Sequence[Sequence[str]] | None = None,
) -> Tuple[CausalEvent, ...]:
    if set(modes) != set(cell.vertices) or any(mode not in MODES for mode in modes.values()):
        raise AssertionError("typed mode domain")
    g = graph_from_cell(cell)
    if not feasible(g, selected):
        raise AssertionError("typed selected conflict")
    if any(modes[proposal] == "NO_BIRTH" for proposal in selected):
        raise AssertionError("selected absent opportunity")

    answer: Dict[Hashable, CausalEvent] = {}

    def append(record: CausalEvent) -> CausalEvent:
        if record.event_id in answer and answer[record.event_id] != record:
            raise AssertionError("causal event collision")
        answer[record.event_id] = record
        return record

    participants = sorted({
        participant
        for proposal in cell.vertices
        for participant in cell.participants(proposal)
    })
    bases = {participant: append(base_event(participant)) for participant in participants}

    line_counts = Counter(cell.parent_line(proposal) for proposal in cell.vertices)
    line_predecessor: Dict[str, Hashable] = {}

    priority_for: Dict[str, CausalEvent] = {}
    if priority_orders is not None:
        for raw_order in priority_orders:
            order = tuple(raw_order)
            component = tuple(sorted(order))
            priority = append(event(
                PRIORITY_CLICK,
                "",
                f"arbitration-component:{','.join(component)}",
                f"priority:{','.join(component)}",
                (),
                {
                    "component": ",".join(component),
                    "order": ",".join(order),
                },
            ))
            for proposal in component:
                if proposal in priority_for:
                    raise AssertionError("duplicate priority component")
                priority_for[proposal] = priority
        if set(priority_for) != set(cell.vertices):
            raise AssertionError("priority component coverage")

    for proposal in cell.vertices:
        mode = modes[proposal]
        parent_line = cell.parent_line(proposal)
        parent = append(opportunity_parent_event(
            cell,
            proposal,
            parent_line,
            line_predecessor.get(parent_line, ""),
            line_counts[parent_line] > 1,
        ))
        token = append(dormant_token_event(proposal, parent_line)) if mode == "TOKEN" else None
        mode_parents = (
            (parent.event_id, token.event_id)
            if token is not None
            else (parent.event_id,)
        )
        mode_click = append(event(
            MODE_CLICK,
            proposal,
            f"opportunity:{proposal}",
            f"proposal:{proposal}",
            mode_parents,
            {
                "mode": mode,
                "parent_line": parent_line,
                "source_parent": parent.event_id,
                "token_support": token.event_id if token is not None else "",
            },
        ))

        carrier: CausalEvent | None = None
        body_digest = event_body_digest(cell, proposal)
        attempt = ""
        if mode != "NO_BIRTH":
            carrier_kind = BORN_CARRIER if mode == "BORN" else TOKEN_ACTIVATION
            d36_evidence = d36_carrier_record(cell, proposal, mode, parent_line)
            d36_attempt = d36b.structural_attempt_id(d36_evidence, body_digest)
            carrier = append(event(
                carrier_kind,
                proposal,
                f"transaction:{proposal}",
                f"proposal:{proposal}",
                (mode_click.event_id,),
                {
                    "body_digest": body_digest,
                    "d36_attempt_id": d36_attempt,
                    "d36_evidence_kind": d36_evidence.kind,
                    "d36_evidence_record_id": d36_evidence.record_id,
                    "mode": mode,
                    "parent_line": parent_line,
                    "source_parent": parent.event_id,
                    "token_control": "coherence-neutral" if mode == "TOKEN" else "not-token",
                },
            ))
            attempt = d36_attempt

        if line_counts[parent_line] > 1:
            line_predecessor[parent_line] = (
                carrier.event_id if carrier is not None else mode_click.event_id
            )

        selection_parents = [carrier.event_id if carrier is not None else mode_click.event_id]
        if proposal in priority_for:
            selection_parents.append(priority_for[proposal].event_id)
        selection = append(event(
            SELECTION_CLICK,
            proposal,
            f"arbitration:{proposal}",
            f"proposal:{proposal}",
            tuple(selection_parents),
            {
                "attempt_id": attempt,
                "mode": mode,
                "selected": "1" if proposal in selected else "0",
            },
        ))

        if proposal in selected:
            if carrier is None:
                raise AssertionError("prepare without carrier")
            for participant in cell.participants(proposal):
                base = bases[participant]
                evidence, envelope, _actor = d36_prepare_adapter(
                    cell,
                    proposal,
                    participant,
                    mode,
                    parent_line,
                )
                if envelope.attempt_id != attempt or evidence.record_id != d36_evidence.record_id:
                    raise AssertionError("D36 adapter/carrier mismatch")
                prepare_fields = {
                    "application_code": envelope.application_code,
                    "attempt_id": envelope.attempt_id,
                    "base_record": base.event_id,
                    "base_version": envelope.base_version,
                    "body_digest": envelope.body_digest,
                    "capability": envelope.capability,
                    "carrier_event_id": carrier.event_id,
                    "d36_evidence_kind": evidence.kind,
                    "evidence_record_id": evidence.record_id,
                    "kind": envelope.kind,
                    "participant_index": envelope.participant_index,
                    "response_record_id": envelope.response_record_id,
                    "sender_index": envelope.sender_index,
                    "sender_kind": envelope.sender_kind,
                    "selected_click": selection.event_id,
                    "signature": envelope.signature,
                    "target_index": envelope.target_index,
                    "target_kind": envelope.target_kind,
                    "tx_index": envelope.tx_index,
                }
                append(event(
                    D36_PREPARE,
                    proposal,
                    f"transaction:{proposal}",
                    f"transport:{proposal}->{participant}",
                    (selection.event_id, base.event_id),
                    prepare_fields,
                ))

    result = tuple(sorted(answer.values(), key=lambda record: record.event_id))
    validate_typed_history(cell, result)
    return result


def causal_ancestors(
    event_key: Hashable,
    by_id: Mapping[Hashable, CausalEvent],
    cache: Dict[Hashable, FrozenSet[Hashable]],
    active: FrozenSet[Hashable] = frozenset(),
) -> FrozenSet[Hashable]:
    if event_key in cache:
        return cache[event_key]
    if event_key in active:
        raise AssertionError("causal cycle")
    answer: set[Hashable] = set()
    for parent in by_id[event_key].parents:
        answer.add(parent)
        answer.update(causal_ancestors(parent, by_id, cache, active | {event_key}))
    cache[event_key] = frozenset(answer)
    return cache[event_key]


def validate_typed_history(cell: OrientedCell, records: Sequence[CausalEvent]) -> None:
    by_id = {record.event_id: record for record in records}
    if len(by_id) != len(records):
        raise AssertionError("duplicate causal event ID")
    if any(len(record.parents) > 2 for record in records):
        raise AssertionError("causal parent bound")
    if any(parent not in by_id for record in records for parent in record.parents):
        raise AssertionError("missing causal parent")

    cache: Dict[Hashable, FrozenSet[Hashable]] = {}
    for record in records:
        causal_ancestors(record.event_id, by_id, cache)

    for record in records:
        payload = record.payload_map()
        if len(payload) != len(record.payload):
            raise AssertionError("duplicate causal payload key")
        parents = tuple(by_id[parent] for parent in record.parents)
        if record.kind == BASE_RECORD:
            participant = payload.get("participant", "")
            if (
                record.parents
                or record.proposal
                or set(payload) != {"participant", "version"}
                or payload["version"] != "0"
                or record.owner != f"participant:{participant}"
                or record.wire != f"participant:{participant}"
                or record.event_id != base_record_id(participant)
            ):
                raise AssertionError("base record legality")
        elif record.kind == OPPORTUNITY_PARENT:
            declared_line = cell.parent_line(record.proposal) if record.proposal in cell.vertices else ""
            line_proposals = tuple(
                proposal
                for proposal in cell.vertices
                if cell.parent_line(proposal) == declared_line
            )
            line_index = line_proposals.index(record.proposal) if record.proposal in line_proposals else -1
            expected_predecessor: Hashable = ""
            if line_index > 0:
                previous_proposal = line_proposals[line_index - 1]
                previous = next(
                    candidate
                    for candidate in records
                    if candidate.proposal == previous_proposal
                    and candidate.kind
                    in (BORN_CARRIER, TOKEN_ACTIVATION, MODE_CLICK)
                    and (
                        candidate.kind != MODE_CLICK
                        or not any(
                            other.proposal == previous_proposal
                            and other.kind in (BORN_CARRIER, TOKEN_ACTIVATION)
                            for other in records
                        )
                    )
                )
                expected_predecessor = previous.event_id
            if (
                record.proposal not in cell.vertices
                or set(payload) != {"parent_line", "proposal_type"}
                or record.owner != f"source:{record.proposal}"
                or payload["parent_line"] != declared_line
                or record.parents != ((expected_predecessor,) if expected_predecessor else ())
                or record.wire
                != (
                    f"parent-line:{declared_line}"
                    if len(line_proposals) > 1
                    else f"proposal:{record.proposal}"
                )
            ):
                raise AssertionError("opportunity parent legality")
            expected = opportunity_parent_id(
                record.proposal,
                payload["parent_line"],
                payload["proposal_type"],
                expected_predecessor,
            )
            if record.event_id != expected or payload["proposal_type"] != cell.proposal_type(record.proposal):
                raise AssertionError("opportunity parent identity")
        elif record.kind == DORMANT_TOKEN:
            if (
                record.parents
                or record.proposal not in cell.vertices
                or set(payload) != {"control", "parent_line"}
                or payload.get("control") != "coherence-neutral"
                or record.owner != f"token:{record.proposal}"
                or record.wire != f"token:{record.proposal}"
                or record.event_id
                != dormant_token_id(record.proposal, payload["parent_line"])
            ):
                raise AssertionError("dormant token legality")
        elif record.kind == MODE_CLICK:
            opportunity_parents = [parent for parent in parents if parent.kind == OPPORTUNITY_PARENT]
            token_parents = [parent for parent in parents if parent.kind == DORMANT_TOKEN]
            if (
                len(opportunity_parents) != 1
                or len(opportunity_parents) + len(token_parents) != len(parents)
                or set(payload)
                != {"mode", "parent_line", "source_parent", "token_support"}
                or record.owner != f"opportunity:{record.proposal}"
                or record.wire != f"proposal:{record.proposal}"
            ):
                raise AssertionError("mode parent legality")
            opportunity = opportunity_parents[0]
            if (
                opportunity.proposal != record.proposal
                or payload["mode"] not in MODES
                or payload["parent_line"] != opportunity.payload_map()["parent_line"]
                or payload["source_parent"] != opportunity.event_id
            ):
                raise AssertionError("mode payload legality")
            if payload["mode"] == "TOKEN":
                if (
                    len(token_parents) != 1
                    or token_parents[0].proposal != record.proposal
                    or token_parents[0].payload_map()["parent_line"] != payload["parent_line"]
                    or payload["token_support"] != token_parents[0].event_id
                ):
                    raise AssertionError("TOKEN support ancestry")
            elif token_parents or payload["token_support"]:
                raise AssertionError("non-TOKEN dormant support")
        elif record.kind in (BORN_CARRIER, TOKEN_ACTIVATION):
            if (
                len(parents) != 1
                or parents[0].kind != MODE_CLICK
                or parents[0].proposal != record.proposal
                or set(payload)
                != {
                    "body_digest",
                    "d36_attempt_id",
                    "d36_evidence_kind",
                    "d36_evidence_record_id",
                    "mode",
                    "parent_line",
                    "source_parent",
                    "token_control",
                }
                or record.owner != f"transaction:{record.proposal}"
                or record.wire != f"proposal:{record.proposal}"
            ):
                raise AssertionError("carrier parent legality")
            expected_mode = "BORN" if record.kind == BORN_CARRIER else "TOKEN"
            mode_payload = parents[0].payload_map()
            d36_evidence = d36_carrier_record(
                cell,
                record.proposal,
                expected_mode,
                payload["parent_line"],
            )
            d36_attempt = d36b.structural_attempt_id(
                d36_evidence,
                payload["body_digest"],
            )
            if (
                payload["mode"] != expected_mode
                or mode_payload["mode"] != expected_mode
                or payload["body_digest"] != event_body_digest(cell, record.proposal)
                or payload["parent_line"] != mode_payload["parent_line"]
                or payload["source_parent"] != mode_payload["source_parent"]
                or payload["d36_evidence_kind"] != d36_evidence.kind
                or payload["d36_evidence_record_id"] != d36_evidence.record_id
                or payload["d36_attempt_id"] != d36_attempt
                or payload["token_control"]
                != ("coherence-neutral" if expected_mode == "TOKEN" else "not-token")
            ):
                raise AssertionError("carrier mode legality")
            expected_id = event_id(
                record.kind,
                record.proposal,
                record.owner,
                record.wire,
                record.parents,
                record.payload,
            )
            if record.event_id != expected_id:
                raise AssertionError("carrier immutable identity")
        elif record.kind == PRIORITY_CLICK:
            if record.parents or record.proposal or set(payload) != {"component", "order"}:
                raise AssertionError("priority click root legality")
            component = tuple(payload.get("component", "").split(","))
            order = tuple(payload.get("order", "").split(","))
            if (
                not component
                or tuple(sorted(component)) != component
                or len(set(component)) != len(component)
                or len(set(order)) != len(order)
                or set(order) != set(component)
                or component not in connected_components(graph_from_cell(cell))
                or record.owner != f"arbitration-component:{','.join(component)}"
                or record.wire != f"priority:{','.join(component)}"
            ):
                raise AssertionError("priority click component/order legality")
        elif record.kind == SELECTION_CLICK:
            priority_parents = [parent for parent in parents if parent.kind == PRIORITY_CLICK]
            main_parents = [parent for parent in parents if parent.kind != PRIORITY_CLICK]
            if (
                len(main_parents) != 1
                or len(priority_parents) > 1
                or main_parents[0].proposal != record.proposal
                or set(payload) != {"attempt_id", "mode", "selected"}
                or payload["selected"] not in ("0", "1")
                or record.owner != f"arbitration:{record.proposal}"
                or record.wire != f"proposal:{record.proposal}"
            ):
                raise AssertionError("selection parent legality")
            mode = payload["mode"]
            allowed_parent = MODE_CLICK if mode == "NO_BIRTH" else (
                BORN_CARRIER if mode == "BORN" else TOKEN_ACTIVATION
            )
            if main_parents[0].kind != allowed_parent:
                raise AssertionError("selection mode ancestry")
            if mode != main_parents[0].payload_map()["mode"]:
                raise AssertionError("selection mode payload")
            expected_attempt = (
                ""
                if mode == "NO_BIRTH"
                else main_parents[0].payload_map()["d36_attempt_id"]
            )
            if payload["attempt_id"] != expected_attempt:
                raise AssertionError("selection attempt identity")
            if priority_parents:
                order = tuple(priority_parents[0].payload_map()["order"].split(","))
                if record.proposal not in order:
                    raise AssertionError("selection priority ancestry")
            if mode == "NO_BIRTH" and payload["selected"] != "0":
                raise AssertionError("selected no-birth")
        elif record.kind == D36_PREPARE:
            if (
                len(parents) != 2
                or set(payload)
                != {
                    "application_code",
                    "attempt_id",
                    "base_record",
                    "base_version",
                    "body_digest",
                    "capability",
                    "carrier_event_id",
                    "d36_evidence_kind",
                    "evidence_record_id",
                    "kind",
                    "participant_index",
                    "response_record_id",
                    "sender_index",
                    "sender_kind",
                    "selected_click",
                    "signature",
                    "target_index",
                    "target_kind",
                    "tx_index",
                }
            ):
                raise AssertionError("prepare parent count")
            selection = next((parent for parent in parents if parent.kind == SELECTION_CLICK), None)
            base = next((parent for parent in parents if parent.kind == BASE_RECORD), None)
            if selection is None or base is None or selection.payload_map()["selected"] != "1":
                raise AssertionError("prepare evidence ancestry")
            participant_names = sorted({
                name
                for proposal in cell.vertices
                for name in cell.participants(proposal)
            })
            participant_index = payload["participant_index"]
            participant_matches = [
                name
                for name in participant_names
                if structural_actor_index("P", name) == participant_index
            ]
            if not isinstance(participant_index, int) or len(participant_matches) != 1:
                raise AssertionError("prepare participant index")
            participant = participant_matches[0]
            tx_index = structural_actor_index("T", record.proposal)
            if base.event_id != base_record_id(participant) or payload["base_record"] != base.event_id:
                raise AssertionError("prepare base binding")
            carrier_candidates = [
                by_id[ancestor]
                for ancestor in cache[selection.event_id]
                if by_id[ancestor].kind in (BORN_CARRIER, TOKEN_ACTIVATION)
            ]
            if len(carrier_candidates) != 1:
                raise AssertionError("prepare carrier ancestry")
            carrier = carrier_candidates[0]
            mode = carrier.payload_map()["mode"]
            evidence, envelope, actor = d36_prepare_adapter(
                cell,
                record.proposal,
                participant,
                mode,
                carrier.payload_map()["parent_line"],
            )
            expected_attempt = envelope.attempt_id
            if (
                payload["carrier_event_id"] != carrier.event_id
                or payload["d36_evidence_kind"] != evidence.kind
                or payload["evidence_record_id"] != evidence.record_id
                or record.proposal != selection.proposal
                or record.owner != f"transaction:{record.proposal}"
                or record.wire != f"transport:{record.proposal}->{participant}"
                or payload["selected_click"] != selection.event_id
                or payload["kind"] != envelope.kind
                or payload["sender_kind"] != envelope.sender_kind
                or payload["sender_index"] != envelope.sender_index
                or payload["target_kind"] != envelope.target_kind
                or payload["target_index"] != envelope.target_index
                or payload["tx_index"] != envelope.tx_index
                or payload["participant_index"] != envelope.participant_index
                or payload["response_record_id"] != envelope.response_record_id
                or payload["application_code"] != envelope.application_code
                or payload["base_version"] != envelope.base_version
                or payload["body_digest"] != envelope.body_digest
                or payload["body_digest"] != carrier.payload_map()["body_digest"]
                or payload["body_digest"] != event_body_digest(cell, record.proposal)
                or payload["attempt_id"] != expected_attempt
                or selection.payload_map()["attempt_id"] != expected_attempt
                or participant not in cell.participants(record.proposal)
                or payload["capability"] != envelope.capability
                or payload["signature"] != envelope.signature
                or not d36b.participant_accepts_prepare(actor, envelope)
            ):
                raise AssertionError("prepare structural attempt binding")
        else:
            raise AssertionError(("unknown causal event type", record.kind))

        if record.kind not in (BASE_RECORD, OPPORTUNITY_PARENT, DORMANT_TOKEN):
            expected_id = event_id(
                record.kind,
                record.proposal,
                record.owner,
                record.wire,
                record.parents,
                record.payload,
            )
            if record.event_id != expected_id:
                raise AssertionError("immutable event identity")

    for left, right in combinations(records, 2):
        if left.wire != right.wire:
            continue
        if left.event_id not in cache[right.event_id] and right.event_id not in cache[left.event_id]:
            raise AssertionError(("same-wire incomparability", left.wire, left.kind, right.kind))

    mode_records = [record for record in records if record.kind == MODE_CLICK]
    selection_records = [record for record in records if record.kind == SELECTION_CLICK]
    modes = {record.proposal: record.payload_map()["mode"] for record in mode_records}
    selections = {
        record.proposal: record.payload_map()["selected"] == "1"
        for record in selection_records
    }
    if set(modes) != set(cell.vertices) or set(selections) != set(cell.vertices):
        raise AssertionError("mode/selection click coverage")
    if len(mode_records) != len(cell.vertices) or len(selection_records) != len(cell.vertices):
        raise AssertionError("duplicate mode/selection click")
    participants = {
        participant
        for proposal in cell.vertices
        for participant in cell.participants(proposal)
    }
    if {
        record.payload_map()["participant"]
        for record in records
        if record.kind == BASE_RECORD
    } != participants:
        raise AssertionError("participant base coverage")
    opportunity_records = [record for record in records if record.kind == OPPORTUNITY_PARENT]
    if (
        len(opportunity_records) != len(cell.vertices)
        or {record.proposal for record in opportunity_records} != set(cell.vertices)
    ):
        raise AssertionError("opportunity parent coverage")
    dormant_records = [record for record in records if record.kind == DORMANT_TOKEN]
    if (
        len(dormant_records) != sum(mode == "TOKEN" for mode in modes.values())
        or {record.proposal for record in dormant_records}
        != {proposal for proposal, mode in modes.items() if mode == "TOKEN"}
    ):
        raise AssertionError("dormant token coverage")
    carrier_records = [
        record
        for record in records
        if record.kind in (BORN_CARRIER, TOKEN_ACTIVATION)
    ]
    if (
        len(carrier_records) != sum(mode != "NO_BIRTH" for mode in modes.values())
        or {record.proposal for record in carrier_records}
        != {proposal for proposal, mode in modes.items() if mode != "NO_BIRTH"}
    ):
        raise AssertionError("carrier coverage")
    selected = frozenset(proposal for proposal, value in selections.items() if value)
    if not feasible(graph_from_cell(cell), selected):
        raise AssertionError("typed arbitration feasibility")
    priority_records = [record for record in records if record.kind == PRIORITY_CLICK]
    if priority_records:
        priority_orders = tuple(
            tuple(record.payload_map()["order"].split(","))
            for record in sorted(
                priority_records,
                key=lambda item: item.payload_map()["component"],
            )
        )
        priority_components = tuple(
            tuple(record.payload_map()["component"].split(","))
            for record in sorted(
                priority_records,
                key=lambda item: item.payload_map()["component"],
            )
        )
        if (
            priority_components != connected_components(graph_from_cell(cell))
            or selected != greedy(graph_from_cell(cell), priority_orders)
            or any(
                len(
                    [
                        parent
                        for parent in by_id[selection.event_id].parents
                        if by_id[parent].kind == PRIORITY_CLICK
                    ]
                )
                != 1
                for selection in selection_records
            )
        ):
            raise AssertionError("recorded priority arbitration law")
    prepare_counts = Counter(
        record.proposal for record in records if record.kind == D36_PREPARE
    )
    for proposal in cell.vertices:
        expected = len(cell.participants(proposal)) if proposal in selected else 0
        if prepare_counts[proposal] != expected:
            raise AssertionError("D36 prepare coverage")


def topological_orders(records: Sequence[CausalEvent]) -> Tuple[Tuple[str, ...], ...]:
    by_id = {record.event_id: record for record in records}
    answer: list[Tuple[str, ...]] = []

    def visit(prefix: Tuple[str, ...], remaining: FrozenSet[str]) -> None:
        if not remaining:
            answer.append(prefix)
            return
        done = set(prefix)
        available = sorted(
            key for key in remaining if set(by_id[key].parents) <= done
        )
        if not available:
            raise AssertionError("topological extension dead end")
        for key in available:
            visit(prefix + (key,), remaining - {key})

    visit((), frozenset(by_id))
    return tuple(answer)


def replay_history(records: Sequence[CausalEvent], order: Sequence[str]) -> str:
    by_id = {record.event_id: record for record in records}
    if set(order) != set(by_id) or len(order) != len(by_id):
        raise AssertionError("linear extension domain")
    seen: set[str] = set()
    for key in order:
        if not set(by_id[key].parents) <= seen:
            raise AssertionError("linear extension violates parent order")
        seen.add(key)
    return digest(tuple(sorted(
        (
            record.event_id,
            record.kind,
            record.proposal,
            record.owner,
            record.wire,
            record.parents,
            record.payload,
        )
        for record in records
    )))


def linear_extension_covariance() -> Tuple[int, int, str]:
    cell = oriented_cell("single", (("P", ("A", "B")),))
    records = build_typed_history(cell, {"P": "BORN"}, frozenset(("P",)))
    orders = topological_orders(records)
    digests = {replay_history(records, order) for order in orders}
    if len(orders) <= 1 or len(digests) != 1:
        raise AssertionError("D33 linear-extension covariance")
    by_id = {record.event_id: record for record in records}
    cache: Dict[str, FrozenSet[str]] = {}
    for record in records:
        causal_ancestors(record.event_id, by_id, cache)
    comparable_same_wire = sum(
        1
        for left, right in combinations(records, 2)
        if left.wire == right.wire
        and (left.event_id in cache[right.event_id] or right.event_id in cache[left.event_id])
    )
    return len(orders), comparable_same_wire, next(iter(digests))


def restrict_typed_history(
    records: Sequence[CausalEvent],
    proposals: FrozenSet[str],
    participants: FrozenSet[str],
) -> Tuple[CausalEvent, ...]:
    return tuple(sorted(
        (
            record
            for record in records
            if record.proposal in proposals
            or (
                record.kind == PRIORITY_CLICK
                and set(record.payload_map()["component"].split(",")) <= proposals
            )
            or (
                record.kind == BASE_RECORD
                and record.payload_map()["participant"] in participants
            )
        ),
        key=lambda record: record.event_id,
    ))


def causal_disjoint_restriction_checks() -> Tuple[int, int, int, int]:
    full_cell = ORIENTED_CELLS["two_pairs"]
    full_modes = {"P": "BORN", "Q": "TOKEN", "R": "BORN", "S": "NO_BIRTH"}
    full = build_typed_history(full_cell, full_modes, frozenset(("P", "R")))

    left_cell = oriented_cell("left", (("P", ("A", "B")), ("Q", ("A", "B"))))
    left = build_typed_history(
        left_cell,
        {"P": "BORN", "Q": "TOKEN"},
        frozenset(("P",)),
    )
    right_cell = oriented_cell("right", (("R", ("C", "D")), ("S", ("C", "D"))))
    right = build_typed_history(
        right_cell,
        {"R": "BORN", "S": "NO_BIRTH"},
        frozenset(("R",)),
    )

    left_restriction = restrict_typed_history(
        full,
        frozenset(("P", "Q")),
        frozenset(("A", "B")),
    )
    right_restriction = restrict_typed_history(
        full,
        frozenset(("R", "S")),
        frozenset(("C", "D")),
    )
    if left_restriction != left or right_restriction != right:
        raise AssertionError("D34 causal anti-dilution")
    return 2, len(full), len(left), len(right)


def line_shadow(
    records: Sequence[CausalEvent],
    parent_line: str,
    coherence: Fraction,
) -> Fraction:
    born = sum(
        record.kind == BORN_CARRIER
        and record.payload_map()["parent_line"] == parent_line
        for record in records
    )
    return coherence ** born


def typed_mode_history_checks(
    dist: "ModeDistribution",
    cell: OrientedCell,
) -> Tuple[int, int, int, int]:
    histories = 0
    events = 0
    prepares = 0
    dormant_tokens = 0
    for atom in dist:
        records = build_typed_history(cell, atom.mode_map(), atom.selected)
        histories += 1
        events += len(records)
        prepares += sum(record.kind == D36_PREPARE for record in records)
        dormant_tokens += sum(record.kind == DORMANT_TOKEN for record in records)
    return histories, events, prepares, dormant_tokens


def typed_legality_negative_checks() -> int:
    rejected = 0

    def require_rejection(action: Callable[[], object]) -> None:
        nonlocal rejected
        try:
            action()
        except AssertionError:
            rejected += 1
            return
        raise AssertionError("typed illegality admitted")

    single = oriented_cell("single-negative", (("P", ("A", "B")),))
    born_selected = build_typed_history(single, {"P": "BORN"}, frozenset(("P",)))
    require_rejection(lambda: validate_typed_history(
        single,
        tuple(record for record in born_selected if record.kind != OPPORTUNITY_PARENT),
    ))

    opportunity = next(record for record in born_selected if record.kind == OPPORTUNITY_PARENT)
    sibling_mode = event(
        MODE_CLICK,
        "P",
        "opportunity:P",
        "proposal:P",
        (opportunity.event_id,),
        {
            "mode": "NO_BIRTH",
            "parent_line": opportunity.payload_map()["parent_line"],
            "source_parent": opportunity.event_id,
            "token_support": "",
        },
    )
    require_rejection(lambda: validate_typed_history(single, born_selected + (sibling_mode,)))

    born_rejected = build_typed_history(single, {"P": "BORN"}, frozenset())
    selection = next(record for record in born_rejected if record.kind == SELECTION_CLICK)
    forged_selection = event(
        SELECTION_CLICK,
        selection.proposal,
        selection.owner,
        selection.wire,
        selection.parents,
        {"attempt_id": "forged", "mode": "BORN", "selected": "0"},
    )
    require_rejection(lambda: validate_typed_history(
        single,
        tuple(forged_selection if record == selection else record for record in born_rejected),
    ))

    prepare = next(record for record in born_selected if record.kind == D36_PREPARE)
    forged_prepare_payload = prepare.payload_map()
    forged_prepare_payload["signature"] = "FORGED"
    forged_prepare = event(
        prepare.kind,
        prepare.proposal,
        prepare.owner,
        prepare.wire,
        prepare.parents,
        forged_prepare_payload,
    )
    require_rejection(lambda: validate_typed_history(
        single,
        tuple(forged_prepare if record == prepare else record for record in born_selected),
    ))

    path = ORIENTED_CELLS["path"]
    require_rejection(lambda: build_typed_history(
        path,
        {proposal: "TOKEN" for proposal in path.vertices},
        frozenset(("Q",)),
        priority_orders=(("P", "Q", "R"),),
    ))
    pair = ORIENTED_CELLS["pair"]
    require_rejection(lambda: build_typed_history(
        pair,
        {proposal: "BORN" for proposal in pair.vertices},
        frozenset(pair.vertices),
    ))

    no_birth = build_typed_history(
        path,
        {proposal: "NO_BIRTH" for proposal in path.vertices},
        frozenset(),
    )
    q_parent = next(
        record
        for record in no_birth
        if record.kind == OPPORTUNITY_PARENT and record.proposal == "Q"
    )
    p_token = dormant_token_event("P", path.parent_line("P"))
    cross_token_mode = event(
        MODE_CLICK,
        "Q",
        "opportunity:Q",
        "proposal:Q",
        (q_parent.event_id, p_token.event_id),
        {
            "mode": "TOKEN",
            "parent_line": q_parent.payload_map()["parent_line"],
            "source_parent": q_parent.event_id,
            "token_support": p_token.event_id,
        },
    )
    require_rejection(lambda: validate_typed_history(
        path,
        (cross_token_mode, p_token) + no_birth,
    ))
    return rejected


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


def typed_visibility_expectation_for_vertex(
    dist: ModeDistribution,
    cell: OrientedCell,
    vertex: str,
    coherence: Fraction,
) -> Fraction:
    parent_line = cell.parent_line(vertex)
    return sum(
        probability
        * line_shadow(
            build_typed_history(cell, atom.mode_map(), atom.selected),
            parent_line,
            coherence,
        )
        for atom, probability in dist.items()
    )


def visibility_checks() -> Tuple[Fraction, Fraction, Fraction, Fraction, int]:
    coupling = Fraction(9, 25)
    coherence = Fraction(4, 5)
    if coherence * coherence != 1 - coupling:
        raise AssertionError("Pythagorean coupling")
    equal_mode = {mode: Fraction(1, 3) for mode in MODES}
    histories = tuple(product(MODES, repeat=3))
    base_cell = ORIENTED_CELLS["path"]
    shared_line = {proposal: "probe:shared-parent-line" for proposal in base_cell.vertices}
    cell = oriented_cell(
        "path-shared-parent-line",
        base_cell.proposals,
        shared_line,
    )
    expected = Fraction(0)
    history_checks = 0
    for history in histories:
        modes = dict(zip(cell.vertices, history))
        records = build_typed_history(cell, modes, frozenset())
        by_id = {record.event_id: record for record in records}
        cache: Dict[Hashable, FrozenSet[Hashable]] = {}
        for record in records:
            causal_ancestors(record.event_id, by_id, cache)
        born_records = [record for record in records if record.kind == BORN_CARRIER]
        if any(
            left.event_id not in cache[right.event_id]
            and right.event_id not in cache[left.event_id]
            for left, right in combinations(born_records, 2)
        ):
            raise AssertionError("same-parent-line births are not causally comparable")
        shadow = line_shadow(records, "probe:shared-parent-line", coherence)
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
            renamed_cell,
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


def typed_binary_history_checks(
    dist: BinaryDistribution,
    cell: OrientedCell,
) -> Tuple[int, int, int, int]:
    histories = 0
    events = 0
    prepares = 0
    dormant_tokens = 0
    modes = {proposal: "TOKEN" for proposal in cell.vertices}
    for selected in dist:
        records = build_typed_history(cell, modes, selected)
        histories += 1
        events += len(records)
        prepares += sum(record.kind == D36_PREPARE for record in records)
        dormant_tokens += sum(record.kind == DORMANT_TOKEN for record in records)
    return histories, events, prepares, dormant_tokens


def typed_priority_history_checks(
    dist: PriorityDistribution,
    cell: OrientedCell,
) -> Tuple[int, int, int, int, int]:
    histories = 0
    events = 0
    prepares = 0
    dormant_tokens = 0
    priority_clicks = 0
    modes = {proposal: "TOKEN" for proposal in cell.vertices}
    for atom in dist:
        records = build_typed_history(
            cell,
            modes,
            atom.selected,
            priority_orders=atom.orders,
        )
        histories += 1
        events += len(records)
        prepares += sum(record.kind == D36_PREPARE for record in records)
        dormant_tokens += sum(record.kind == DORMANT_TOKEN for record in records)
        priority_clicks += sum(record.kind == PRIORITY_CLICK for record in records)
    return histories, events, prepares, dormant_tokens, priority_clicks


def canonical_identity_checks() -> Tuple[int, int, int]:
    bases = {base_record_id(f"participant:{index}") for index in range(1000)}
    parents = {
        opportunity_parent_id(
            f"proposal:{index}",
            f"line:{index}",
            "TRANSACTION_OPPORTUNITY",
        )
        for index in range(1000)
    }
    actors = {
        structural_actor_index("P", f"participant:{index}")
        for index in range(1000)
    }
    if not all(
        isinstance(identifier, tuple)
        and identifier[:2] == ("D37_CANONICAL_ID", BASE_RECORD)
        for identifier in bases
    ):
        raise AssertionError("theorem-level base IDs are not canonical tuples")
    if not all(index >= 0 for index in actors):
        raise AssertionError("injective actor index range")
    return len(bases), len(parents), len(actors)


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
    emit("SCOPE: supplied typed parent/wire opportunity carriers over pairwise conflict graphs; countable completion requires the stated proof")

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
    interface_content_checks = 0
    typed_history_cells = 0
    typed_event_total = 0
    typed_prepare_total = 0
    for name, cell in ORIENTED_CELLS.items():
        orientation_valid &= graph_from_cell(cell) == GRAPHS[name]
        for region in regions(GRAPHS[name]):
            interface = oriented_interface(cell, region)
            if not interface_content_valid(cell, region, interface):
                raise AssertionError((name, region, "typed interface content"))
            interface_content_checks += 1
            orientation_rows.append((name, tuple(sorted(region)), interface))
        selected: set[str] = set()
        for proposal in cell.vertices:
            if not (neighbors(GRAPHS[name], proposal) & selected):
                selected.add(proposal)
        typed_history = build_typed_history(
            cell,
            {proposal: "BORN" for proposal in cell.vertices},
            frozenset(selected),
        )
        typed_history_cells += 1
        typed_event_total += len(typed_history)
        typed_prepare_total += sum(record.kind == D36_PREPARE for record in typed_history)
    typed_illegal_rejections = typed_legality_negative_checks()
    canonical_ids = canonical_identity_checks()
    orientation_hash = hashlib.sha256(stable(orientation_rows).encode()).hexdigest()
    gates["S0"] = (
        vertex_total == 28
        and edge_total == 19
        and region_total == 196
        and len(orientation_rows) == 38
        and interface_content_checks == 38
        and orientation_valid
        and typed_history_cells == 6
        and typed_event_total == 104
        and typed_prepare_total == 19
        and typed_illegal_rejections == 7
        and canonical_ids == (1000, 1000, 1000)
        and automorphisms
        == {
            "d36_disjoint": 2,
            "pair": 2,
            "partial": 2,
            "path": 2,
            "path5": 2,
            "path7": 2,
            "triangle": 6,
            "two_pairs": 8,
        }
    )
    science["objects"] = [
        vertex_total,
        edge_total,
        region_total,
        automorphisms,
        orientation_hash,
        interface_content_checks,
        typed_history_cells,
        typed_event_total,
        typed_prepare_total,
        typed_illegal_rejections,
        canonical_ids,
    ]
    emit("[REGISTERED TYPED OPPORTUNITY CARRIERS]")
    emit(f"graphs={len(registered)}; vertices={vertex_total}; conflict_edges={edge_total}; nonempty_regions={region_total}")
    emit(f"automorphism_counts={stable(automorphisms)}; oriented_interface_rows={len(orientation_rows)}; orientation_sha256={orientation_hash}")
    emit(f"interface_content_checks={interface_content_checks}/38; typed_causal_histories={typed_history_cells}/6; typed_events={typed_event_total}; signed_D36_prepare_records={typed_prepare_total}")
    emit(f"typed_illegal_histories_rejected={typed_illegal_rejections}/7; missing_parent=1; duplicate_mode=1; forged_attempt=1; forged_signature=1; wrong_priority=1; conflict=1; cross_TOKEN=1")
    emit(f"canonical_tuple_ID_controls={canonical_ids}; SHA256_role=serialization_checksum_only; actor_indices=injective_arbitrary_precision")
    emit("distinct_parent_record_ids=1; explicit_parent_lines=1; explicit_event_types=1; causal_parent_bound=2; structural_labels_not_physical_slots=1")

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
    gates["S1"] = (
        k3_conditionals == 508
        and k3_towers == 7098
        and k3_mixtures == 138
        and k3_factor
    )
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
    gates["S2"] = (
        forcing_ratio_checks == 30
        and forcing_states == 25
        and contextual_odds == ("2", "4")
    )
    science["forcing"] = [forcing_ratio_checks, forcing_states, contextual_odds]
    emit("[SAFE-SUPPORT FIXED-ODDS FORCING]")
    emit(f"exact_single_flip_probability_ratios={forcing_ratio_checks}; reconstructed_states={forcing_states}; global_weight_reconstruction=1")
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
    gates["S3"] = (
        k2_conditionals == 188
        and k2_boundaries == 165
        and k2_towers == 1224
        and raw_k2[0] != raw_k2[1]
    )
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
    typed_k1 = typed_priority_history_checks(path_priority, ORIENTED_CELLS["path"])
    one_hop_witness = find_k1_one_hop_counterexample()
    gates["S4"] = (
        path_k1[frozenset(("Q",))] == Fraction(1, 3)
        and path_k1[frozenset(("P", "R"))] == Fraction(2, 3)
        and path_k2[frozenset(("Q",))] == Fraction(1, 2)
        and raw_k1[0] != raw_k1[1]
        and priority_towers == 35
        and complete_click_atoms == len(path_priority) == 6
        and typed_k1 == (6, 140, 20, 18, 6)
        and bool(one_hop_witness)
    )
    science["k1"] = [
        dist_signature(path_k1),
        priority_towers,
        complete_click_atoms,
        typed_k1,
        one_hop_witness,
    ]
    emit("[K1 RECORDED-PRIORITY LIFT]")
    emit(f"path_K1={binary_text(path_k1)}; path_K2={binary_text(path_k2)}; marked_atoms={len(path_priority)}")
    emit(f"path_to_edge_raw={binary_text(raw_k1[0])}; direct_edge={binary_text(raw_k1[1])}; finite_marked_DLR_towers={priority_towers}")
    emit(f"recorded_priority_and_all_outcomes={complete_click_atoms}/{len(path_priority)}; one_hop_output_counterexample={stable(one_hop_witness)}")
    emit(f"typed_priority_histories={typed_k1[0]}; typed_events={typed_k1[1]}; signed_exact_D36_prepare_records={typed_k1[2]}; dormant_TOKEN_records={typed_k1[3]}; recorded_priority_clicks={typed_k1[4]}")
    emit("K1_typed_scope=complete-carrier-atoms-only; proper-region-parent-closed-transport=NOT_PROVED")
    emit("K1_infinite_quasilocal_completion=NOT_PROVED; finite_probability_boundary_class=recorded_component_priority+exterior_outcomes")

    pairwise_overlap, triple_support, pair_atoms = anticorrelation_cover()
    path_k3_cover = cover_checks(GRAPHS["path"].vertices, hard_core(GRAPHS["path"], Fraction(2)), binary_projection)
    path_k2_cover = cover_checks(GRAPHS["path"].vertices, path_k2, binary_projection)
    path_k1_cover = cover_checks(GRAPHS["path"].vertices, path_priority, priority_projection)
    cover_total = path_k3_cover + path_k2_cover + path_k1_cover
    gates["S5"] = (
        cover_total == 99
        and path_k3_cover == path_k2_cover == path_k1_cover == 33
        and pairwise_overlap == 1
        and triple_support == 0
        and pair_atoms == 6
    )
    science["covers"] = [cover_total, path_k3_cover, path_k2_cover, path_k1_cover, pairwise_overlap, triple_support]
    emit("[THREE-PATH MARGINAL DESCENT]")
    emit(f"global_joint_path_overlap_checks={cover_total}; K3={path_k3_cover}; K2={path_k2_cover}; K1_marked={path_k1_cover}")
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
    (
        typed_mode_histories,
        typed_mode_events,
        typed_mode_prepares,
        typed_dormant_tokens,
    ) = typed_mode_history_checks(
        equal_dist,
        ORIENTED_CELLS["path"],
    )
    gates["S6"] = (
        mode_conditionals == 166
        and mode_one_sites == 134
        and mode_towers == 238
        and mode_atoms == 186
        and swap_checks == len(equal_dist) == 93
        and mode_cover == 33
        and typed_mode_histories == 93
        and typed_mode_events == 1683
        and typed_mode_prepares == 156
        and typed_dormant_tokens == 106
        and birth_marginal == {
            "NO_BIRTH": Fraction(25, 93),
            "TOKEN": Fraction(34, 93),
            "BORN": Fraction(34, 93),
        }
        and arbitration_marginal == Fraction(6, 31)
    )
    science["modes"] = [
        mode_conditionals,
        mode_one_sites,
        mode_towers,
        mode_atoms,
        swap_checks,
        mode_cover,
        birth_marginal,
        arbitration_marginal,
        joint_q_visibility,
        typed_mode_histories,
        typed_mode_events,
        typed_mode_prepares,
        typed_dormant_tokens,
    ]
    emit("[JOINT BIRTH / ARBITRATION FUNCTIONAL]")
    emit(f"intrinsic_conditionals={mode_conditionals}; one_site_conditionals={mode_one_sites}; nested_DLR_towers={mode_towers}; atoms={mode_atoms}")
    emit(f"BORN_TOKEN_exchange_atoms_at_symmetric_point={swap_checks}; three_path_cover_checks={mode_cover}; Q_mode_marginal={stable({k:ftext(v) for k,v in sorted(birth_marginal.items())})}")
    emit(f"Q_selected_marginal={ftext(arbitration_marginal)}; Q_D26_expected_factor={ftext(joint_q_visibility)}; q_birth_and_arbitration_from_same_table=1; weights_selected=0")
    emit(f"typed_history_atoms={typed_mode_histories}; typed_events={typed_mode_events}; dormant_TOKEN_records={typed_dormant_tokens}; signed_exact_D36_prepare_records={typed_mode_prepares}")

    coupling, coherence, all_born_shadow, expected_shadow, visibility_history_checks = visibility_checks()
    typed_joint_q_visibility = typed_visibility_expectation_for_vertex(
        equal_dist,
        ORIENTED_CELLS["path"],
        "Q",
        coherence,
    )
    typed_k3 = typed_binary_history_checks(
        hard_core(GRAPHS["path"], Fraction(2)),
        ORIENTED_CELLS["path"],
    )
    typed_k2 = typed_binary_history_checks(path_k2, ORIENTED_CELLS["path"])
    gates["S7"] = (
        coherence * coherence == 1 - coupling
        and all_born_shadow == Fraction(64, 125)
        and expected_shadow == Fraction(2744, 3375)
        and joint_q_visibility == Fraction(431, 465)
        and typed_joint_q_visibility == joint_q_visibility
        and visibility_history_checks == 27
        and complete_click_atoms == len(path_priority)
        and typed_k3 == (5, 105, 10, 15)
        and typed_k2 == (2, 44, 6, 6)
        and typed_k1 == (6, 140, 20, 18, 6)
    )
    science["visibility"] = [
        coupling,
        coherence,
        all_born_shadow,
        expected_shadow,
        visibility_history_checks,
        typed_joint_q_visibility,
        typed_k3,
        typed_k2,
        typed_k1,
    ]
    emit("[D26 VISIBILITY / CLICK SOURCE]")
    emit(f"g={ftext(coupling)}; sqrt_1_minus_g={ftext(coherence)}; three_same_line_BORN_shadow={ftext(all_born_shadow)}")
    emit(f"equal_mode_three_opportunity_expected_shadow={ftext(expected_shadow)}; joint_Q_expected_factor={ftext(joint_q_visibility)}; typed_parent_line_history_checks={visibility_history_checks}; TOKEN_NO_BIRTH_factor=1")
    emit("D26_parent_line_declared_and_causally_chained=1; comparable_same_line_BORN=1; coherence_neutral_TOKEN_control=1; universal_rate_from_visibility=0; hidden_service_order_randomness=0")
    emit("[TYPED CLICK / PREPARE ADAPTERS]")
    emit(f"K3_histories_events_prepares_tokens={typed_k3}; K2_histories_events_prepares_tokens={typed_k2}")
    emit(f"K1_histories_events_prepares_tokens_priority_clicks={typed_k1}; exact_D36_attempt_key=evidence_record_id+body_digest; signed_PREPARE_parent_bound=2")
    emit(f"D36_participant_accepts_PREPARE=K3:{typed_k3[2]},K2:{typed_k2[2]},K1:{typed_k1[2]},joint:{typed_mode_prepares}; locked_D36b_sha256={D36B_SHA256}")

    covariance = covariance_checks()
    anti_sizes = anti_dilution_checks()
    linear_extensions, same_wire_pairs, linear_extension_digest = linear_extension_covariance()
    causal_restrictions, full_causal_events, left_causal_events, right_causal_events = (
        causal_disjoint_restriction_checks()
    )
    gates["S8"] = (
        covariance == 6
        and anti_sizes == (9, 4, 4, 441)
        and linear_extensions == 70
        and same_wire_pairs == 6
        and linear_extension_digest
        == "00023ba8f09b771b2e2a748f9944a43829eb48ca3845a18b8cfdb9a795e67881"
        and causal_restrictions == 2
        and (full_causal_events, left_causal_events, right_causal_events) == (24, 13, 11)
    )
    science["covariance"] = [
        covariance,
        anti_sizes,
        linear_extensions,
        same_wire_pairs,
        linear_extension_digest,
        causal_restrictions,
        full_causal_events,
        left_causal_events,
        right_causal_events,
    ]
    emit("[COVARIANCE / ANTI-DILUTION]")
    emit(f"relabel_covariance_families={covariance}/6; disconnected_local_factorizations=4/4; atom_counts={anti_sizes}")
    emit(f"D33_linear_extension_serializations={linear_extensions}; same_wire_comparable_pairs={same_wire_pairs}; canonical_DAG_digest={linear_extension_digest}")
    emit(f"D34_causal_restrictions={causal_restrictions}/2; typed_event_counts=full:{full_causal_events},left:{left_causal_events},right:{right_causal_events}")
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
    emit("CLASSICAL TYPED CAUSAL REGIONAL SPECIFICATION / SUPPLIED OPPORTUNITY CARRIER / FAMILY NOT SELECTOR")
    emit("K3 fixed-odds forcing survives; K2 progress survives; K1 is a finite marked probability lift with full-carrier typed atoms only")
    emit("countable completion proof, selected couplings, generated typed opportunity carrier and quantum lift remain separate claims")
    if passed != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
