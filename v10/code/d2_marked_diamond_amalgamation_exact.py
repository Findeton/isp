#!/usr/bin/env python3
"""D2 exact receipt: marked-support-skeleton amalgamation versus carrier birth.

The receipt uses only Python's standard library.  Every verdict is finite and
exact.  It distinguishes:

* canonical composition after a typed overlap span is supplied;
* selection of the overlap span itself;
* intersection/shadow versus contained-event restriction;
* pair-carrier birth versus higher-support filling.
"""

from __future__ import annotations

import ast
import sys
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Dict, FrozenSet, Hashable, Iterable, Mapping, Sequence, Tuple


Vertex = str
Support = FrozenSet[Vertex]
Edge = FrozenSet[Vertex]
MVertex = Hashable
Mark = Tuple[str, str]  # (port/interface type, stable provenance/ancestry)

CHECKS = 0
PASSED = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECKS, PASSED
    CHECKS += 1
    if not condition:
        raise AssertionError(f"{label}: {detail}")
    PASSED += 1
    suffix = f" ({detail})" if detail else ""
    print(f"PASS {CHECKS:02d}: {label}{suffix}")


def support_key(support: Support) -> Tuple[int, Tuple[Vertex, ...]]:
    return len(support), tuple(sorted(support))


@dataclass(frozen=True)
class SupportSystem:
    vertices: FrozenSet[Vertex]
    supports: FrozenSet[Support]

    @staticmethod
    def make(vertices: Iterable[Vertex], supports: Iterable[Iterable[Vertex]]) -> "SupportSystem":
        vertex_set = frozenset(vertices)
        support_set = frozenset(frozenset(support) for support in supports)
        if any(len(support) < 2 or not support <= vertex_set for support in support_set):
            raise ValueError("every support must contain at least two retained vertices")
        return SupportSystem(vertex_set, support_set)

    def restrict_intersection(self, keep: Iterable[Vertex]) -> "SupportSystem":
        kept = self.vertices & frozenset(keep)
        projected = {support & kept for support in self.supports if len(support & kept) >= 2}
        return SupportSystem.make(kept, projected)

    def restrict_contained(self, keep: Iterable[Vertex]) -> "SupportSystem":
        kept = self.vertices & frozenset(keep)
        return SupportSystem.make(kept, (support for support in self.supports if support <= kept))

    def relabel(self, mapping: Mapping[Vertex, Vertex]) -> "SupportSystem":
        if set(mapping) != set(self.vertices) or len(set(mapping.values())) != len(mapping):
            raise ValueError("relabeling must be a bijection on the vertex set")
        return SupportSystem.make(
            (mapping[vertex] for vertex in self.vertices),
            ({mapping[vertex] for vertex in support} for support in self.supports),
        )

    def canonical(self) -> tuple:
        return (
            tuple(sorted(self.vertices)),
            tuple(tuple(sorted(support)) for support in sorted(self.supports, key=support_key)),
        )


@dataclass(frozen=True)
class MarkedSystem:
    """Finite colored support hypergraph.

    This is the explicit support skeleton used by D2, not the entire stochastic
    law of a sealed holonomy diamond.
    """

    vertices: Tuple[MVertex, ...]
    supports: FrozenSet[FrozenSet[MVertex]]
    marks: Tuple[Tuple[MVertex, Mark], ...]

    @staticmethod
    def make(
        vertices: Iterable[MVertex],
        supports: Iterable[Iterable[MVertex]],
        marks: Mapping[MVertex, Mark],
    ) -> "MarkedSystem":
        vertex_tuple = tuple(vertices)
        if len(set(vertex_tuple)) != len(vertex_tuple):
            raise ValueError("vertices must be unique")
        vertex_set = frozenset(vertex_tuple)
        if set(marks) != set(vertex_set):
            raise ValueError("every vertex needs exactly one typed provenance mark")
        support_set = frozenset(frozenset(support) for support in supports)
        if any(len(support) < 2 or not support <= vertex_set for support in support_set):
            raise ValueError("invalid marked support")
        mark_tuple = tuple(sorted(marks.items(), key=lambda item: repr(item[0])))
        return MarkedSystem(vertex_tuple, support_set, mark_tuple)

    def mark_map(self) -> Dict[MVertex, Mark]:
        return dict(self.marks)


def valid_homomorphism(
    source: MarkedSystem,
    target: MarkedSystem,
    mapping: Mapping[MVertex, MVertex],
    *,
    injective: bool = False,
) -> bool:
    """Color-preserving weak hypergraph homomorphism.

    A collapsed support may become a singleton.  Every image retaining at
    least two vertices must be a target support.  Allowing noninjective general
    morphisms makes finite coproducts/pushouts satisfy their universal
    properties; D2 interface legs are separately required to be injective.
    """
    if set(mapping) != set(source.vertices):
        return False
    if any(image not in target.vertices for image in mapping.values()):
        return False
    if injective and len(set(mapping.values())) != len(mapping):
        return False
    source_marks = source.mark_map()
    target_marks = target.mark_map()
    if any(source_marks[vertex] != target_marks[mapping[vertex]] for vertex in source.vertices):
        return False
    for support in source.supports:
        image = frozenset(mapping[vertex] for vertex in support)
        if len(image) >= 2 and image not in target.supports:
            return False
    return True


@dataclass(frozen=True)
class MarkedPushout:
    object: MarkedSystem
    left_injection: Tuple[Tuple[MVertex, MVertex], ...]
    right_injection: Tuple[Tuple[MVertex, MVertex], ...]

    def left_map(self) -> Dict[MVertex, MVertex]:
        return dict(self.left_injection)

    def right_map(self) -> Dict[MVertex, MVertex]:
        return dict(self.right_injection)


def marked_pushout(
    interface: MarkedSystem,
    left: MarkedSystem,
    right: MarkedSystem,
    leg_left: Mapping[MVertex, MVertex],
    leg_right: Mapping[MVertex, MVertex],
) -> MarkedPushout:
    """Pushout in finite marked support systems and weak homomorphisms."""
    if not valid_homomorphism(interface, left, leg_left, injective=True):
        raise ValueError("left interface leg is not an injective marked homomorphism")
    if not valid_homomorphism(interface, right, leg_right, injective=True):
        raise ValueError("right interface leg is not an injective marked homomorphism")

    tagged_left = [("L", vertex) for vertex in left.vertices]
    tagged_right = [("R", vertex) for vertex in right.vertices]
    uf = UnionFind(tagged_left + tagged_right)
    for vertex in interface.vertices:
        uf.union(("L", leg_left[vertex]), ("R", leg_right[vertex]))

    blocks: Dict[tuple, set[tuple]] = {}
    for item in tagged_left + tagged_right:
        blocks.setdefault(uf.find(item), set()).add(item)
    quotient_vertices = tuple(
        sorted((frozenset(block) for block in blocks.values()), key=repr)
    )
    item_to_block = {
        item: block
        for block in quotient_vertices
        for item in block
    }
    left_injection = {vertex: item_to_block[("L", vertex)] for vertex in left.vertices}
    right_injection = {vertex: item_to_block[("R", vertex)] for vertex in right.vertices}

    supports = set()
    for system, injection in ((left, left_injection), (right, right_injection)):
        for support in system.supports:
            image = frozenset(injection[vertex] for vertex in support)
            if len(image) >= 2:
                supports.add(image)

    marks: Dict[MVertex, Mark] = {}
    left_marks = left.mark_map()
    right_marks = right.mark_map()
    for vertex, image in left_injection.items():
        marks[image] = left_marks[vertex]
    for vertex, image in right_injection.items():
        mark = right_marks[vertex]
        if image in marks and marks[image] != mark:
            raise AssertionError("validated legs produced inconsistent quotient marks")
        marks[image] = mark

    pushout_object = MarkedSystem.make(quotient_vertices, supports, marks)
    if not valid_homomorphism(left, pushout_object, left_injection):
        raise AssertionError("left canonical map is not a morphism")
    if not valid_homomorphism(right, pushout_object, right_injection):
        raise AssertionError("right canonical map is not a morphism")
    return MarkedPushout(
        pushout_object,
        tuple(sorted(left_injection.items(), key=lambda item: repr(item[0]))),
        tuple(sorted(right_injection.items(), key=lambda item: repr(item[0]))),
    )


def factor_cocone(
    pushout: MarkedPushout,
    left: MarkedSystem,
    right: MarkedSystem,
    target: MarkedSystem,
    cocone_left: Mapping[MVertex, MVertex],
    cocone_right: Mapping[MVertex, MVertex],
) -> Dict[MVertex, MVertex]:
    """Construct the unique mediator from a compatible cocone."""
    if not valid_homomorphism(left, target, cocone_left):
        raise ValueError("invalid left cocone map")
    if not valid_homomorphism(right, target, cocone_right):
        raise ValueError("invalid right cocone map")
    values: Dict[MVertex, MVertex] = {}
    for vertex, image in pushout.left_map().items():
        values[image] = cocone_left[vertex]
    for vertex, image in pushout.right_map().items():
        candidate = cocone_right[vertex]
        if image in values and values[image] != candidate:
            raise ValueError("cocone does not agree on the interface")
        values[image] = candidate
    if not valid_homomorphism(pushout.object, target, values):
        raise AssertionError("universal mediator is not a marked homomorphism")
    return values


def all_maps(source: MarkedSystem, target: MarkedSystem) -> Iterable[Dict[MVertex, MVertex]]:
    for images in product(target.vertices, repeat=len(source.vertices)):
        yield dict(zip(source.vertices, images))


def universal_cocone_audit(
    interface: MarkedSystem,
    left: MarkedSystem,
    right: MarkedSystem,
    leg_left: Mapping[MVertex, MVertex],
    leg_right: Mapping[MVertex, MVertex],
    target: MarkedSystem,
) -> Tuple[int, bool]:
    """Exhaust every valid cocone into one finite target and test factorization."""
    pushout = marked_pushout(interface, left, right, leg_left, leg_right)
    cocones = 0
    for cocone_left in all_maps(left, target):
        if not valid_homomorphism(left, target, cocone_left):
            continue
        for cocone_right in all_maps(right, target):
            if not valid_homomorphism(right, target, cocone_right):
                continue
            if any(cocone_left[leg_left[v]] != cocone_right[leg_right[v]] for v in interface.vertices):
                continue
            cocones += 1
            mediator = factor_cocone(pushout, left, right, target, cocone_left, cocone_right)
            factorizations = []
            for candidate in all_maps(pushout.object, target):
                if not valid_homomorphism(pushout.object, target, candidate):
                    continue
                if all(candidate[pushout.left_map()[v]] == cocone_left[v] for v in left.vertices) and all(
                    candidate[pushout.right_map()[v]] == cocone_right[v] for v in right.vertices
                ):
                    factorizations.append(candidate)
            if len(factorizations) != 1 or factorizations[0] != mediator:
                return cocones, False
    return cocones, cocones > 0


def marked_signature(system: MarkedSystem) -> tuple:
    """Canonical finite marked-support signature by exhaustive vertex order."""
    vertices = system.vertices
    marks = system.mark_map()
    candidates = []
    for order in permutations(vertices):
        index = {vertex: position for position, vertex in enumerate(order)}
        mark_code = tuple(marks[vertex] for vertex in order)
        support_code = tuple(
            sorted(tuple(sorted(index[vertex] for vertex in support)) for support in system.supports)
        )
        candidates.append((mark_code, support_code))
    return min(candidates, key=repr)


def union_amalgam(left: SupportSystem, right: SupportSystem) -> SupportSystem:
    """Pushout for already-identified shared labels: transported support union."""
    return SupportSystem.make(left.vertices | right.vertices, left.supports | right.supports)


class UnionFind:
    def __init__(self, items: Iterable[tuple]):
        self.parent = {item: item for item in items}

    def find(self, item: tuple) -> tuple:
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]

    def union(self, left: tuple, right: tuple) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left != root_right:
            first, second = sorted((root_left, root_right), key=repr)
            self.parent[second] = first


def graph_pushout(
    a_vertices: Sequence[Vertex],
    a_edges: Sequence[Sequence[Vertex]],
    b_vertices: Sequence[Vertex],
    b_edges: Sequence[Sequence[Vertex]],
    identifications: Sequence[Tuple[Vertex, Vertex]],
) -> Tuple[int, FrozenSet[FrozenSet[int]]]:
    """Finite graph pushout of a supplied interface span."""
    if any(a not in a_vertices or b not in b_vertices for a, b in identifications):
        raise ValueError("interface identification leaves an input graph")
    if len({a for a, _ in identifications}) != len(identifications) or len({b for _, b in identifications}) != len(identifications):
        raise ValueError("interface legs must be injective")
    tagged_a = [("A", vertex) for vertex in a_vertices]
    tagged_b = [("B", vertex) for vertex in b_vertices]
    uf = UnionFind(tagged_a + tagged_b)
    for a_vertex, b_vertex in identifications:
        uf.union(("A", a_vertex), ("B", b_vertex))

    roots = sorted({uf.find(item) for item in tagged_a + tagged_b}, key=repr)
    root_index = {root: index for index, root in enumerate(roots)}

    def image(side: str, edge: Sequence[Vertex]) -> FrozenSet[int]:
        return frozenset(root_index[uf.find((side, vertex))] for vertex in edge)

    edges = {
        image("A", edge) for edge in a_edges
    } | {
        image("B", edge) for edge in b_edges
    }
    return len(roots), frozenset(edge for edge in edges if len(edge) == 2)


def graph_signature(graph: Tuple[int, FrozenSet[FrozenSet[int]]]) -> Tuple[int, str]:
    """Canonical unlabeled simple-graph signature by exhaustive relabeling."""
    n, edges = graph
    pairs = tuple(combinations(range(n), 2))
    candidates = []
    for perm in permutations(range(n)):
        transported = {
            frozenset((perm[left], perm[right])) for left, right in (tuple(edge) for edge in edges)
        }
        candidates.append("".join("1" if frozenset(pair) in transported else "0" for pair in pairs))
    return n, min(candidates) if candidates else ""


def edge_masks() -> Tuple[Tuple[int, int], ...]:
    return ((0, 1), (0, 2), (1, 2))


EDGES3 = edge_masks()


def permute_edge_mask(mask: int, perm: Tuple[int, int, int]) -> int:
    edge_to_bit = {frozenset(edge): bit for bit, edge in enumerate(EDGES3)}
    out = 0
    for bit, edge in enumerate(EDGES3):
        if mask & (1 << bit):
            transported = frozenset((perm[edge[0]], perm[edge[1]]))
            out |= 1 << edge_to_bit[transported]
    return out


def pair_closure_census() -> Tuple[int, int, Tuple[int, ...]]:
    """Enumerate every extensive deterministic edge closure through n=3.

    The n=2 law is fixed by extensivity plus refusal to join two isolated
    vertices, hence identity.  Restriction naturality tests every 2-subset.
    """
    options = [tuple(output for output in range(8) if output | mask == output) for mask in range(8)]
    total = 0
    passing = []
    perms = tuple(permutations(range(3)))
    for outputs in product(*options):
        total += 1
        if any(outputs[outputs[mask]] != outputs[mask] for mask in range(8)):
            continue
        if any(
            permute_edge_mask(outputs[mask], perm) != outputs[permute_edge_mask(mask, perm)]
            for mask in range(8)
            for perm in perms
        ):
            continue
        natural = True
        for mask in range(8):
            for bit in range(3):
                input_pair = 1 if mask & (1 << bit) else 0
                output_pair = 1 if outputs[mask] & (1 << bit) else 0
                if output_pair != input_pair:  # the n=2 closure is identity
                    natural = False
        if not natural:
            continue
        passing.append(outputs)
    return total, len(passing), passing[0]


def hyperedge_fill_census_intersection() -> Tuple[int, Tuple[Tuple[int, ...], ...]]:
    """Enumerate 3-support fill predicates above the fixed pair identity law."""
    total = 0
    passing = []
    perms = tuple(permutations(range(3)))
    for additions in product((0, 1), repeat=8):
        total += 1
        if any(additions[mask] != additions[permute_edge_mask(mask, perm)] for mask in range(8) for perm in perms):
            continue
        natural = True
        for mask in range(8):
            if not additions[mask]:
                continue
            # Under intersection projection, a filled triple casts every pair
            # shadow.  Pair naturality therefore requires all three faces.
            if mask != 0b111:
                natural = False
        if not natural:
            continue
        passing.append(additions)
    return total, tuple(passing)


def hyperedge_fill_census_contained() -> Tuple[Tuple[Tuple[int, ...], ...], Tuple[Tuple[int, ...], ...]]:
    """Covariant monotone contained-natural rules refusing the empty graph.

    Contained-event naturality is automatic for a new triple because every
    proper restriction discards it.  The second return additionally refuses
    adding a triple when the pair graph is not connected on all three vertices.
    """
    perms = tuple(permutations(range(3)))
    passing = []
    component_refusing = []
    for additions in product((0, 1), repeat=8):
        if additions[0]:
            continue
        if any(additions[mask] != additions[permute_edge_mask(mask, perm)] for mask in range(8) for perm in perms):
            continue
        if any(
            additions[small] and not additions[large]
            for small in range(8)
            for large in range(8)
            if small | large == large
        ):
            continue
        rule = tuple(additions)
        passing.append(rule)
        if all(not additions[mask] or is_connected_pair_mask(mask) for mask in range(8)):
            component_refusing.append(rule)
    return tuple(passing), tuple(component_refusing)


def invariant_pair_families() -> Tuple[FrozenSet[int], ...]:
    perms = tuple(permutations(range(3)))
    families = []
    for mask in range(8):
        if all(permute_edge_mask(mask, perm) == mask for perm in perms):
            families.append(frozenset(bit for bit in range(3) if mask & (1 << bit)))
    return tuple(families)


def is_connected_pair_mask(mask: int) -> bool:
    if mask == 0:
        return False
    adjacency = {vertex: set() for vertex in range(3)}
    active = set()
    for bit, (left, right) in enumerate(EDGES3):
        if mask & (1 << bit):
            adjacency[left].add(right)
            adjacency[right].add(left)
            active.update((left, right))
    if active != {0, 1, 2}:
        return False
    reached = {0}
    stack = [0]
    while stack:
        vertex = stack.pop()
        for neighbor in adjacency[vertex] - reached:
            reached.add(neighbor)
            stack.append(neighbor)
    return reached == {0, 1, 2}


def project_three_state_to_pair(mask: int, triple: bool, bit: int, semantics: str) -> int:
    edge_present = bool(mask & (1 << bit))
    if semantics == "intersection":
        return int(edge_present or triple)
    if semantics == "contained":
        return int(edge_present)
    raise ValueError("unknown restriction semantics")


def contained_connected_fill_audit() -> Tuple[bool, bool, bool, bool, bool]:
    """Audit the rule: add a triple iff its three-vertex pair graph is connected."""
    perms = tuple(permutations(range(3)))
    covariance = all(
        is_connected_pair_mask(mask) == is_connected_pair_mask(permute_edge_mask(mask, perm))
        for mask in range(8)
        for perm in perms
    )
    monotone = all(
        not is_connected_pair_mask(small) or is_connected_pair_mask(large)
        for small in range(8)
        for large in range(8)
        if small | large == large
    )
    disconnected_component_refusal = all(not is_connected_pair_mask(mask) or mask != 0 for mask in range(8))
    # Contained-event restriction discards the triple on every proper subset,
    # so the pair output is exactly the unchanged input pair.
    contained_natural = all(
        project_three_state_to_pair(mask, is_connected_pair_mask(mask), bit, "contained")
        == project_three_state_to_pair(mask, False, bit, "contained")
        for mask in range(8)
        for bit in range(3)
    )
    # Intersection projection casts every pair shadow from the new triple.  A
    # connected two-edge path is therefore a counterexample.
    intersection_failure = any(
        project_three_state_to_pair(mask, is_connected_pair_mask(mask), bit, "intersection")
        != project_three_state_to_pair(mask, False, bit, "intersection")
        for mask in range(8)
        for bit in range(3)
    )
    return covariance, monotone, disconnected_component_refusal, contained_natural, intersection_failure


def standard_library_import_audit(source: Path) -> Tuple[str, ...]:
    tree = ast.parse(source.read_text(encoding="utf-8"))
    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".")[0])
    nonstdlib = sorted(root for root in roots if root != "__future__" and root not in sys.stdlib_module_names)
    return tuple(nonstdlib)


def stochastic_symmetric_pair_audit() -> Tuple[bool, bool, Fraction]:
    """Uniform one-pair kernel is covariant but fails strong restriction.

    S3-covariance forces the three pair probabilities to be equal.  Exact
    normalization then gives 1/3.  Restriction to any named pair sees that edge
    with probability 1/3, whereas the edgeless two-record axiom requires zero.
    """
    weights = (Fraction(1, 3),) * 3
    covariance = all(
        weights[bit]
        == weights[(permute_edge_mask(1 << bit, perm)).bit_length() - 1]
        for bit in range(3)
        for perm in permutations(range(3))
    )
    normalization = sum(weights, Fraction(0)) == 1
    restricted_edge_probability = weights[0]
    strong_projectivity = restricted_edge_probability == 0
    return covariance and normalization, strong_projectivity, restricted_edge_probability


def main() -> None:
    global CHECKS, PASSED
    CHECKS = 0
    PASSED = 0

    source = Path(__file__).resolve()
    check("G0 source resides under v10/code", source.parent.name == "code" and source.parent.parent.name == "v10")
    check("G0b source imports only the Python standard library", standard_library_import_audit(source) == ())

    mark_i = ("collar", "shared:I")
    marked_i = MarkedSystem.make(("i",), (), {"i": mark_i})
    marked_a = MarkedSystem.make(
        ("a", "i"),
        (("a", "i"),),
        {"a": ("out", "lineage:A"), "i": mark_i},
    )
    marked_b = MarkedSystem.make(
        ("i", "b"),
        (("i", "b"),),
        {"i": mark_i, "b": ("out", "lineage:B")},
    )
    marked_ab = marked_pushout(marked_i, marked_a, marked_b, {"i": "i"}, {"i": "i"})
    check(
        "T1 typed interface legs produce a marked support-conserving pushout",
        len(marked_ab.object.vertices) == 3
        and len(marked_ab.object.supports) == 2
        and valid_homomorphism(marked_a, marked_ab.object, marked_ab.left_map(), injective=True)
        and valid_homomorphism(marked_b, marked_ab.object, marked_ab.right_map(), injective=True),
    )

    target_vertices = ("a0", "a1", "i0", "i1", "b0", "b1")
    target_marks = {
        "a0": ("out", "lineage:A"),
        "a1": ("out", "lineage:A"),
        "i0": mark_i,
        "i1": mark_i,
        "b0": ("out", "lineage:B"),
        "b1": ("out", "lineage:B"),
    }
    target_supports = tuple(combinations(target_vertices, 2))
    universal_target = MarkedSystem.make(target_vertices, target_supports, target_marks)
    cocone_count, universal_ok = universal_cocone_audit(
        marked_i,
        marked_a,
        marked_b,
        {"i": "i"},
        {"i": "i"},
        universal_target,
    )
    check(
        "T2 every valid cocone into the finite audit target factors uniquely",
        universal_ok and cocone_count == 8,
        f"cocones={cocone_count}",
    )

    # True iterated typed pushouts for A <- I -> B <- J -> C.
    mark_j = ("collar", "shared:J")
    chain_a = marked_a
    chain_b = MarkedSystem.make(
        ("i", "b"),
        (("i", "b"),),
        {"i": mark_i, "b": mark_j},
    )
    chain_c = MarkedSystem.make(
        ("b", "c"),
        (("b", "c"),),
        {"b": mark_j, "c": ("out", "lineage:C")},
    )
    marked_j = MarkedSystem.make(("j",), (), {"j": mark_j})
    push_ab = marked_pushout(marked_i, chain_a, chain_b, {"i": "i"}, {"i": "i"})
    push_ab_c = marked_pushout(
        marked_j,
        push_ab.object,
        chain_c,
        {"j": push_ab.right_map()["b"]},
        {"j": "b"},
    )
    push_bc = marked_pushout(marked_j, chain_b, chain_c, {"j": "b"}, {"j": "b"})
    push_a_bc = marked_pushout(
        marked_i,
        chain_a,
        push_bc.object,
        {"i": "i"},
        {"i": push_bc.left_map()["i"]},
    )
    check(
        "T3 true iterated typed pushouts are construction-order gauge up to marked isomorphism",
        marked_signature(push_ab_c.object) == marked_signature(push_a_bc.object),
    )

    bare_mark = ("collar", "bare")
    bare_i = MarkedSystem.make(("k1", "k2"), (), {"k1": bare_mark, "k2": bare_mark})
    bare_a = MarkedSystem.make(
        ("x", "i1", "i2"),
        (("x", "i1"),),
        {"x": ("out", "X"), "i1": bare_mark, "i2": bare_mark},
    )
    bare_b = MarkedSystem.make(
        ("y", "j1", "j2"),
        (("y", "j1"),),
        {"y": ("out", "Y"), "j1": bare_mark, "j2": bare_mark},
    )
    typed_aligned = marked_pushout(
        bare_i,
        bare_a,
        bare_b,
        {"k1": "i1", "k2": "i2"},
        {"k1": "j1", "k2": "j2"},
    )
    typed_crossed = marked_pushout(
        bare_i,
        bare_a,
        bare_b,
        {"k1": "i1", "k2": "i2"},
        {"k1": "j2", "k2": "j1"},
    )
    check(
        "T4 indistinguishable interface marks permit nonisomorphic typed pushouts",
        marked_signature(typed_aligned.object) != marked_signature(typed_crossed.object),
    )

    red, blue = ("collar", "red"), ("collar", "blue")
    typed_i = MarkedSystem.make(("k1", "k2"), (), {"k1": red, "k2": blue})
    typed_a = MarkedSystem.make(
        ("x", "i1", "i2"),
        (("x", "i1"),),
        {"x": ("out", "X"), "i1": red, "i2": blue},
    )
    typed_b = MarkedSystem.make(
        ("y", "j1", "j2"),
        (("y", "j1"),),
        {"y": ("out", "Y"), "j1": red, "j2": blue},
    )
    typed_ok = marked_pushout(
        typed_i,
        typed_a,
        typed_b,
        {"k1": "i1", "k2": "i2"},
        {"k1": "j1", "k2": "j2"},
    )
    crossed_rejected = False
    try:
        marked_pushout(
            typed_i,
            typed_a,
            typed_b,
            {"k1": "i1", "k2": "i2"},
            {"k1": "j2", "k2": "j1"},
        )
    except ValueError:
        crossed_rejected = True
    check(
        "T5 typed provenance can make one interface matching admissible and reject the other",
        len(typed_ok.object.vertices) == 4 and crossed_rejected,
    )

    root_interface = MarkedSystem.make(("r",), (), {"r": ("ancestry", "root:R1")})
    root_left = MarkedSystem.make(("p",), (), {"p": ("ancestry", "root:R1")})
    root_right_same = MarkedSystem.make(("q",), (), {"q": ("ancestry", "root:R1")})
    root_right_other = MarkedSystem.make(("q",), (), {"q": ("ancestry", "root:R2")})
    same_root_valid = valid_homomorphism(root_interface, root_left, {"r": "p"}, injective=True) and valid_homomorphism(
        root_interface, root_right_same, {"r": "q"}, injective=True
    )
    other_root_valid = valid_homomorphism(root_interface, root_right_other, {"r": "q"}, injective=True)
    check("T6 ancestry provenance is load-bearing in interface admissibility", same_root_valid and not other_root_valid)

    empty_i = MarkedSystem.make((), (), {})
    point_mark = ("out", "symmetric:point")
    point_left = MarkedSystem.make(("u",), (), {"u": point_mark})
    point_right = MarkedSystem.make(("v",), (), {"v": point_mark})
    point_target = MarkedSystem.make(("w",), (), {"w": point_mark})
    empty_cocones, empty_universal = universal_cocone_audit(
        empty_i,
        point_left,
        point_right,
        {},
        {},
        point_target,
    )
    check(
        "T7 empty-interface coproduct has the universal mediator in the homomorphism category",
        empty_universal and empty_cocones == 1,
        f"cocones={empty_cocones}",
    )

    a = SupportSystem.make({"a", "i"}, ({"a", "i"},))
    b = SupportSystem.make({"i", "b"}, ({"i", "b"},))
    glued = union_amalgam(a, b)
    check(
        "G1 fixed shared-label span has the canonical support-union amalgam",
        glued.canonical()
        == SupportSystem.make({"a", "i", "b"}, ({"a", "i"}, {"i", "b"})).canonical(),
    )
    check("G2 overlap gluing invents neither exclusive pair nor triple", frozenset({"a", "b"}) not in glued.supports and frozenset({"a", "i", "b"}) not in glued.supports)

    disjoint = union_amalgam(SupportSystem.make({"a"}, ()), SupportSystem.make({"b"}, ()))
    check("G3 empty-interface pushout is a disconnected coproduct", disjoint.supports == frozenset())

    relabel = {"a": "z", "i": "x", "b": "y"}
    transported_after = glued.relabel(relabel)
    transported_before = union_amalgam(a.relabel({"a": "z", "i": "x"}), b.relabel({"i": "x", "b": "y"}))
    check("G4 fixed-span amalgamation is exactly relabeling covariant", transported_after == transported_before)

    c = SupportSystem.make({"b", "c"}, ({"b", "c"},))
    left_first = union_amalgam(union_amalgam(a, b), c)
    right_first = union_amalgam(a, union_amalgam(b, c))
    check("G5 compatible serial amalgam presentations are construction-order gauge", left_first == right_first)

    a_vertices = ("x", "i1", "i2")
    b_vertices = ("y", "j1", "j2")
    a_edges = (("x", "i1"),)
    b_edges = (("y", "j1"),)
    aligned = graph_pushout(a_vertices, a_edges, b_vertices, b_edges, (("i1", "j1"), ("i2", "j2")))
    crossed = graph_pushout(a_vertices, a_edges, b_vertices, b_edges, (("i1", "j2"), ("i2", "j1")))
    check(
        "G6 two legal bare-interface maps yield nonisomorphic pushouts",
        graph_signature(aligned) != graph_signature(crossed),
        f"aligned={graph_signature(aligned)} crossed={graph_signature(crossed)}",
    )
    swapped = graph_pushout(b_vertices, b_edges, a_vertices, a_edges, (("j1", "i1"), ("j2", "i2")))
    check("G7 a fixed interface diagram is symmetric up to pushout isomorphism", graph_signature(aligned) == graph_signature(swapped))
    noninjective_rejected = False
    try:
        graph_pushout(a_vertices, a_edges, b_vertices, b_edges, (("i1", "j1"), ("i2", "j1")))
    except ValueError:
        noninjective_rejected = True
    check("G7b bare graph helper rejects noninjective interface legs", noninjective_rejected)

    total_pair, passing_pair, pair_rule = pair_closure_census()
    check("G8 exhaustive extensive pair-closure census has expected size", total_pair == 4096)
    check(
        "G9 covariance + idempotence + all restrictions + edgeless-pair refusal force identity",
        passing_pair == 1 and pair_rule == tuple(range(8)),
        f"passing={passing_pair}",
    )

    total_fill, fill_rules = hyperedge_fill_census_intersection()
    check("G10 exhaustive three-support predicate census has expected size", total_fill == 256)
    expected_fill_rules = {
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 1),
    }
    check(
        "G11 intersection projectivity leaves two higher-support laws",
        set(fill_rules) == expected_fill_rules,
        f"passing={len(fill_rules)} rules={fill_rules}",
    )

    # Contained-event restriction discards a triple on every proper subset.
    # Thus both clique-only filling and connected-chain filling are natural;
    # the latter fails intersection/shadow naturality when one face is absent.
    connected_masks = tuple(mask for mask in range(8) if is_connected_pair_mask(mask))
    check("G12 connected three-vertex pair masks are exactly the three paths plus triangle", connected_masks == (3, 5, 6, 7))
    connected_audit = contained_connected_fill_audit()
    check(
        "G13 connected-chain fill is covariant, monotone, component-refusing, and contained-natural",
        connected_audit[:4] == (True, True, True, True),
    )
    check(
        "G14 the same connected-chain fill fails intersection/shadow naturality",
        connected_audit[4],
    )
    always_fill = tuple(1 for _ in range(8))
    perms3 = tuple(permutations(range(3)))
    always_fill_covariant = all(
        always_fill[mask] == always_fill[permute_edge_mask(mask, perm)]
        for mask in range(8)
        for perm in perms3
    )
    always_fill_monotone = all(
        not always_fill[small] or always_fill[large]
        for small in range(8)
        for large in range(8)
        if small | large == large
    )
    always_fill_contained_natural = all(
        project_three_state_to_pair(mask, True, bit, "contained")
        == project_three_state_to_pair(mask, False, bit, "contained")
        for mask in range(8)
        for bit in range(3)
    )
    always_fill_edgeless_refusal = not bool(always_fill[0])
    check(
        "G15 contained restriction alone permits empty-to-triple filling but edgeless refusal rejects it",
        always_fill_covariant
        and always_fill_monotone
        and always_fill_contained_natural
        and not always_fill_edgeless_refusal,
    )
    contained_rules, component_rules = hyperedge_fill_census_contained()
    check(
        "G15b contained projectivity + covariance + monotonicity + empty refusal leave four fill laws",
        len(contained_rules) == 4,
        f"passing={len(contained_rules)}",
    )
    check(
        "G15c refusing joins to an isolated component still leaves three contained fill laws",
        len(component_rules) == 3,
        f"passing={len(component_rules)}",
    )

    invariant = invariant_pair_families()
    check("G16 the symmetric three-port history has only empty/all-pair invariant families", invariant == (frozenset(), frozenset({0, 1, 2})))
    check("G17 no deterministic covariant selector can choose exactly one symmetric pair", all(len(family) != 1 for family in invariant))
    stochastic_covariant, stochastic_projective, pair_probability = stochastic_symmetric_pair_audit()
    check(
        "G17b uniform one-pair stochastic choice is exactly covariant",
        stochastic_covariant and pair_probability == Fraction(1, 3),
    )
    check(
        "G17c uniform stochastic pair choice fails strong restriction plus two-record refusal",
        not stochastic_projective,
        f"restricted_pair_probability={pair_probability}",
    )

    root = SupportSystem.make({"r", "a", "b"}, ({"r", "a", "b"},))
    pair_shadow = root.restrict_intersection({"a", "b"})
    pair_event = root.restrict_contained({"a", "b"})
    check("G18 intersection restriction carries an inherited common-root pair shadow", pair_shadow.supports == frozenset({frozenset({"a", "b"})}))
    check("G19 contained-event restriction drops the irreducible common-root event", pair_event.supports == frozenset())

    print()
    print(f"RECEIPT: {PASSED}/{CHECKS} exact checks passed")
    print("POSITIVE: a supplied typed overlap span has a canonical marked-support amalgam")
    print("REFUSAL: ordinary pushout/coproduct gluing creates no primitive cross-carrier")
    print("REFUSAL: the universal property does not select the interface embeddings")
    print("THEOREM: strong restriction plus edgeless-pair refusal forbids first pair-carrier birth")
    print("FAMILY: higher-support filling remains nonunique and depends on restriction ontology")
    print("SYMMETRY: deterministic one-pair choice fails; uniform stochastic choice fails strong projectivity")
    print("VERDICT: CONDITIONAL-COMPOSITION + CARRIER-BIRTH-REFUSAL UNDER THE FROZEN AXIOMS")


if __name__ == "__main__":
    main()
