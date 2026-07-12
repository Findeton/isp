#!/usr/bin/env python3
"""Exact integrated D17 causal-growth/action/memory/record witness.

This closes the integration opening left by the first D17 executable.  Every
probability-cylinder node is an actual causal order.  An explicit supplied
owned extension grammar, local carried-memory boundary, and D14 record network
connect the causal tree to the projective visible histories.  Two positive
kernels remain possible for the same action, so this is still a nonselection
theorem rather than a derivation of nature's law.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations
import json
from pathlib import Path

from d13_finite_kernel_no_go_exact import (
    Q2, ZERO, ONE, ROOT_HALF, matrix, mv, inner, dagger, mul, add, eye,
)
from d14_action_record_bridge_exact import (
    Port, Obj, Mor, compose, ravel, unravel,
)
from d16_covariant_causal_action_exact import BoundaryPort, CausalOrder, IntervalAction, relation


ROOT = Path(__file__).resolve().parents[2]
D14 = Path(__file__).with_name("d14_action_record_bridge_exact.py")
D16 = Path(__file__).with_name("d16_covariant_causal_action_exact.py")
D17 = Path(__file__).with_name("d17_causal_action_measure_nonselection_exact.py")
OUT = ROOT / "v10" / "data" / "d17-integrated-causal-history-exact.json"
EXPECTED_D14_SHA256 = "e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425"
EXPECTED_D16_SHA256 = "861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37"
EXPECTED_D17_SHA256 = "305f532548db3734ed6d92896f98ea9803fbcc86a5786a402cfb6cff8a847d42"
EXPECTED_CHECKS = 40
EXPECTED_SEMANTIC_SHA256 = "bf465b07380b96350afb929ba661fe4309b002cfcb5142b9a495876b22a92987"
CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:03d}: {label}")


def pairs(order):
    return tuple((i, j) for i in range(order.n) for j in range(order.n)
                 if order.relation[i][j])


def order_key(order):
    return order.relation


def carrier_key(carrier):
    return tuple((port.kind, port.dim, port.sealed, port.owner, port.record_id)
                 for port in carrier.ports)


def canonical_typed_key(order, element_owners):
    """Unlabeled order key including element-owner types."""
    if len(element_owners) != order.n:
        raise ValueError("element-owner arity mismatch")
    candidates = []
    for old_to_new in permutations(range(order.n)):
        relabeled = order.permute(old_to_new)
        owners = [None] * order.n
        for old, new in enumerate(old_to_new):
            owners[new] = element_owners[old]
        flat = tuple(int(value) for row in relabeled.relation for value in row)
        past = tuple((port.element, port.kind, port.owner)
                     for port in relabeled.past_boundary)
        future = tuple((port.element, port.kind, port.owner)
                       for port in relabeled.future_boundary)
        candidates.append((flat, past, future, tuple(owners)))
    return min(candidates)


def collar_key(collar):
    return collar.owner, collar.memory, carrier_key(collar.carrier)


def typed_presentation_key(order, element_owners):
    if len(element_owners) != order.n:
        raise ValueError("element-owner arity mismatch")
    flat = tuple(int(value) for row in order.relation for value in row)
    past = tuple((port.element, port.kind, port.owner) for port in order.past_boundary)
    future = tuple((port.element, port.kind, port.owner) for port in order.future_boundary)
    return flat, past, future, tuple(element_owners)


def canonical_typed_edge_key(parent, child):
    """Canonicalize an extension jointly, preserving the marked old embedding."""
    if child.order.n != parent.order.n + 1:
        raise ValueError("edge arity mismatch")
    n = parent.order.n
    candidates = []
    for old_to_new in permutations(range(n)):
        parent_order = parent.order.permute(old_to_new)
        child_order = child.order.permute(tuple(old_to_new) + (n,))
        parent_owners = [None] * n
        child_owners = [None] * (n + 1)
        for old, new in enumerate(old_to_new):
            parent_owners[new] = parent.element_owners[old]
            child_owners[new] = child.element_owners[old]
        child_owners[n] = child.element_owners[n]
        candidates.append((typed_presentation_key(parent_order, tuple(parent_owners)),
                           collar_key(parent.collar),
                           typed_presentation_key(child_order, tuple(child_owners)),
                           collar_key(child.collar)))
    return min(candidates)


def actual_precursor(parent, child):
    new = parent.n
    return tuple(i for i in range(parent.n) if child.relation[i][new])


def is_one_element_extension(parent, child):
    if child.n != parent.n + 1:
        return False
    return all(child.relation[i][j] == parent.relation[i][j]
               for i in range(parent.n) for j in range(parent.n))


def add_maximal(parent):
    n = parent.n
    return CausalOrder(relation(n + 1, pairs(parent) + tuple((i, n) for i in range(n))))


def append_carrier_type(source, record_id, owner="history-cell"):
    return source.tensor(Obj((Port(f"visible-{record_id}", 2, sealed=True,
                                   owner=owner, record_id=record_id),
                              Port(f"live-collar-{record_id}", 2, owner=owner))))


@dataclass(frozen=True)
class Collar:
    owner: str
    memory: int | None
    carrier: Obj


@dataclass(frozen=True)
class GrowthNode:
    marks: tuple[int, ...]
    order: CausalOrder
    element_owners: tuple[str, ...]
    collar: Collar


class GrowthGrammar:
    """Owned one-element extensions with an explicit finite declared grammar."""

    def __init__(self, declared_edges):
        self.declared_edges = frozenset(declared_edges)

    def admit(self, parent, child, requested_owner, join_entitlement=(), declared=True):
        if requested_owner != parent.collar.owner:
            raise ValueError("extension does not own the live collar")
        if child.collar.owner != requested_owner:
            raise ValueError("child collar owner mismatch")
        if not is_one_element_extension(parent.order, child.order):
            raise ValueError("not an induced one-element extension")
        new = parent.order.n
        if len(parent.element_owners) != parent.order.n or len(child.element_owners) != child.order.n:
            raise ValueError("element-owner arity mismatch")
        if child.element_owners[:new] != parent.element_owners:
            raise ValueError("old element ownership changed")
        if child.element_owners[new] != requested_owner:
            raise ValueError("new element owner mismatch")
        if parent.collar.memory is None:
            if child.collar.memory != child.marks[-1]:
                raise ValueError("first branch was not installed in boundary memory")
        elif child.collar.memory != parent.collar.memory:
            raise ValueError("carried boundary memory changed silently")
        depth = len(child.marks)
        expected_carrier = (append_carrier_type(parent.collar.carrier, ("X", "Y", "Z")[depth - 1],
                                                requested_owner)
                            if depth <= 3 else parent.collar.carrier)
        if child.collar.carrier != expected_carrier:
            raise ValueError("child D14 boundary carrier mismatch")
        if any(child.order.relation[new][old] for old in range(parent.order.n)):
            # This supplied filtration permits explicit past insertions.  That
            # is not by itself a proof of gauge equivalence among filtrations.
            pass
        touched_elements = tuple(i for i in range(parent.order.n)
                                 if child.order.relation[i][new] or child.order.relation[new][i])
        touched = frozenset(parent.element_owners[i] for i in touched_elements)
        if len(touched) > 1 and touched != frozenset(join_entitlement):
            raise ValueError("cross-component join lacks entitlement")
        edge = (parent.marks, child.marks, canonical_typed_edge_key(parent, child))
        if declared and edge not in self.declared_edges:
            raise ValueError("extension is valid but absent from supplied Ext(C)")
        return True

    def ext(self, parent, nodes):
        children = tuple(node for node in nodes
                         if len(node.marks) == len(parent.marks) + 1
                         and node.marks[:-1] == parent.marks)
        for child in children:
            self.admit(parent, child, parent.collar.owner)
        return children


def causal_nodes(max_depth=6, owner="history-cell"):
    if max_depth < 3:
        raise ValueError("the integrated X,Y,Z packet requires depth at least three")
    memory_obj = Obj((Port("causal-boundary-memory", 2, owner=owner),))
    carrier_x = append_carrier_type(memory_obj, "X", owner)
    carrier_y = append_carrier_type(carrier_x, "Y", owner)
    carrier_z = append_carrier_type(carrier_y, "Z", owner)
    root = GrowthNode((), CausalOrder(relation(1, ())), (owner,),
                      Collar(owner, None, memory_obj))
    chain2 = CausalOrder(relation(2, ((0, 1),)))
    anti2 = CausalOrder(relation(2, ()))
    chain3 = CausalOrder(relation(3, ((0, 1), (1, 2), (0, 2))))
    vee3 = CausalOrder(relation(3, ((0, 2), (1, 2))))
    chain4 = CausalOrder(relation(4, ((0, 1), (1, 2), (2, 3),
                                             (0, 2), (1, 3), (0, 3))))
    # This labeling is the standard diamond permuted by old->new (3,0,1,2).
    # Its first three elements are exactly vee3; element 3 is inserted below.
    diamond4 = CausalOrder(relation(4, ((0, 2), (1, 2),
                                               (3, 0), (3, 1), (3, 2))))
    nodes = [root,
             GrowthNode((0,), chain2, (owner,) * 2, Collar(owner, 0, carrier_x)),
             GrowthNode((1,), anti2, (owner,) * 2, Collar(owner, 1, carrier_x)),
             GrowthNode((0, 0), chain3, (owner,) * 3, Collar(owner, 0, carrier_y)),
             GrowthNode((1, 0), vee3, (owner,) * 3, Collar(owner, 1, carrier_y)),
             GrowthNode((0, 0, 0), chain4, (owner,) * 4, Collar(owner, 0, carrier_z)),
             GrowthNode((1, 0, 1), diamond4, (owner,) * 4, Collar(owner, 1, carrier_z))]
    for depth in range(4, max_depth + 1):
        prior = tuple(node for node in nodes if len(node.marks) == depth - 1)
        for parent in prior:
            nodes.append(GrowthNode(parent.marks + (0,), add_maximal(parent.order),
                                    parent.element_owners + (owner,),
                                    Collar(owner, parent.collar.memory, parent.collar.carrier)))
    edges = tuple((parent.marks, child.marks, canonical_typed_edge_key(parent, child))
                  for parent in nodes for child in nodes
                  if len(child.marks) == len(parent.marks) + 1
                  and child.marks[:-1] == parent.marks)
    return tuple(nodes), GrowthGrammar(edges)


def causal_tower(nodes, grammar, weight0, weight1, max_depth=6):
    if weight0 <= 0 or weight1 <= 0 or weight0 + weight1 != 1:
        raise ValueError("branch kernel must have positive normalized support")
    root = next(node for node in nodes if node.marks == ())
    frontier = grammar.ext(root, nodes)
    table = {node.marks: (weight0 if node.marks == (0,) else weight1)
             for node in frontier}
    tower = {1: table}
    for depth in range(2, max_depth + 1):
        next_table = {}
        for parent_marks, probability in tower[depth - 1].items():
            parent = next(node for node in nodes if node.marks == parent_marks)
            children = grammar.ext(parent, nodes)
            if len(children) != 1:
                raise ValueError("supplied continuation is not deterministic")
            next_table[children[0].marks] = probability
        tower[depth] = next_table
    return tower


def is_projective_binary(tower):
    if not tower or tuple(sorted(tower)) != tuple(range(1, max(tower) + 1)):
        return False
    for depth, table in tower.items():
        if not table or sum(table.values()) != 1:
            return False
        if any(len(history) != depth or any(bit not in (0, 1) for bit in history)
               or probability < 0 for history, probability in table.items()):
            return False
    for depth in range(1, max(tower)):
        for parent, probability in tower[depth].items():
            if sum(value for child, value in tower[depth + 1].items()
                   if child[:-1] == parent) != probability:
                return False
    return True


def append_local_record(source, source_bit, record_id, owner="history-cell"):
    record = Port(f"visible-{record_id}", 2, sealed=True, owner=owner,
                  record_id=record_id)
    collar = Port(f"live-collar-{record_id}", 2, owner=owner)
    target = source.tensor(Obj((record, collar)))
    rows = [[0 for _ in range(source.dim)] for _ in range(target.dim)]
    source_dims = tuple(port.dim for port in source.ports)
    target_dims = tuple(port.dim for port in target.ports)
    for index in range(source.dim):
        labels = unravel(index, source_dims)
        bit = labels[source_bit] if isinstance(source_bit, int) else int(source_bit)
        out = labels + (bit, 1)
        rows[ravel(out, target_dims)][index] = 1
    return Mor(f"commit-{record_id}", source, target, matrix(rows))


def local_record_network(base=None):
    owner = "history-cell"
    if base is None:
        base = Obj((Port("causal-boundary-memory", 2, owner=owner),))
    commit_x = append_local_record(base, 0, "X", owner)
    commit_y = append_local_record(commit_x.target, "0", "Y", owner)
    commit_z = append_local_record(commit_y.target, 0, "Z", owner)
    return (commit_x, compose(commit_y, commit_x),
            compose(commit_z, compose(commit_y, commit_x)), commit_z)


def reset_boundary_memory(source):
    """CPTP reset of the first local memory port, preserving sealed records."""
    dims = tuple(port.dim for port in source.ports)
    out = []
    for old_memory in (0, 1):
        rows = [[0 for _ in range(source.dim)] for _ in range(source.dim)]
        for index in range(source.dim):
            labels = list(unravel(index, dims))
            if labels[0] != old_memory:
                continue
            labels[0] = 0
            rows[ravel(tuple(labels), dims)][index] = 1
        out.append(Mor(f"reset-memory-from-{old_memory}", source, source, matrix(rows)))
    return tuple(out)


def record_table(network, amplitudes, depth):
    out = mv(network.amp, amplitudes)
    dims = tuple(port.dim for port in network.target.ports)
    record_positions = tuple(i for i, port in enumerate(network.target.ports) if port.sealed)
    table = {}
    for index, amp in enumerate(out):
        if amp == ZERO:
            continue
        labels = unravel(index, dims)
        history = tuple(labels[pos] for pos in record_positions[:depth])
        table[history] = table.get(history, Q2()) + amp.norm2()
    return table


def record_table_after_reset(net2, commit_z, amplitudes):
    state = mv(net2.amp, amplitudes)
    table = {}
    dims = tuple(port.dim for port in commit_z.target.ports)
    record_positions = tuple(i for i, port in enumerate(commit_z.target.ports) if port.sealed)
    for reset in reset_boundary_memory(net2.target):
        out = mv(commit_z.amp, mv(reset.amp, state))
        for index, amp in enumerate(out):
            if amp == ZERO:
                continue
            labels = unravel(index, dims)
            history = tuple(labels[pos] for pos in record_positions)
            table[history] = table.get(history, Q2()) + amp.norm2()
    return table


def main():
    hashes = tuple(sha256(path.read_bytes()).hexdigest() for path in (D14, D16, D17))
    check(hashes == (EXPECTED_D14_SHA256, EXPECTED_D16_SHA256, EXPECTED_D17_SHA256),
          "reviewed D14/D16/D17 dependencies are hash-pinned")

    nodes, grammar = causal_nodes(6)
    by_marks = {node.marks: node for node in nodes}
    check(len(nodes) == 13 and len(by_marks) == len(nodes),
          "one root and two actual causal nodes at every visible depth one through six")
    check(tuple(node.marks for node in grammar.ext(by_marks[()], nodes)) == ((0,), (1,)),
          "Ext(root) is the supplied two-branch causal grammar")
    check(all(len(grammar.ext(by_marks[marks], nodes)) == 1
              for marks in by_marks if marks and len(marks) < 6),
          "every admitted non-root cylinder has one supplied causal continuation")
    check(all(is_one_element_extension(by_marks[marks[:-1]].order, node.order)
              for marks, node in by_marks.items() if marks),
          "every probability-cylinder edge is an induced one-element causal extension")
    check(pairs(by_marks[(1, 0)].order) == ((0, 2), (1, 2))
          and is_one_element_extension(by_marks[(1, 0)].order,
                                       by_marks[(1, 0, 1)].order),
          "the relabeled diamond supplies the previously missing V3-to-size4 edge")
    check(all(by_marks[marks].collar.memory == marks[0]
              for marks in by_marks if marks),
          "the first branch bit is carried by every later owned boundary collar")

    undeclared = GrowthNode((0, 1),
                            CausalOrder(relation(3, ((0, 1),))),
                            ("history-cell",) * 3,
                            Collar("history-cell", 0,
                                   by_marks[(0, 0)].collar.carrier))
    try:
        grammar.admit(by_marks[(0,)], undeclared, "history-cell")
        undeclared_rejected = False
    except ValueError:
        undeclared_rejected = True
    check(undeclared_rejected, "valid but undeclared one-element extension rejects")
    try:
        grammar.admit(by_marks[(0,)], by_marks[(0, 0)], "foreign-cell")
        unowned_rejected = False
    except ValueError:
        unowned_rejected = True
    check(unowned_rejected, "extension by a nonowner rejects")

    forged_owner = GrowthNode(by_marks[(0, 0)].marks, by_marks[(0, 0)].order,
                              ("history-cell", "history-cell", "foreign-cell"),
                              by_marks[(0, 0)].collar)
    forged_collar = GrowthNode(by_marks[(0, 0)].marks, by_marks[(0, 0)].order,
                               by_marks[(0, 0)].element_owners,
                               Collar("foreign-cell", 0, by_marks[(0, 0)].collar.carrier))
    forged_memory = GrowthNode(by_marks[(0, 0)].marks, by_marks[(0, 0)].order,
                               by_marks[(0, 0)].element_owners,
                               Collar("history-cell", 1, by_marks[(0, 0)].collar.carrier))
    forged_results = []
    for forged in (forged_owner, forged_collar, forged_memory):
        try:
            grammar.admit(by_marks[(0,)], forged, "history-cell")
            forged_results.append(False)
        except ValueError:
            forged_results.append(True)
    check(all(forged_results),
          "forged new-element owner, child collar owner and carried memory all reject")

    relabeled_parent = GrowthNode(by_marks[(0,)].marks,
                                  by_marks[(0,)].order.permute((1, 0)),
                                  by_marks[(0,)].element_owners,
                                  by_marks[(0,)].collar)
    relabeled_child = GrowthNode(by_marks[(0, 0)].marks,
                                 by_marks[(0, 0)].order.permute((1, 0, 2)),
                                 by_marks[(0, 0)].element_owners,
                                 by_marks[(0, 0)].collar)
    check(grammar.admit(relabeled_parent, relabeled_child, "history-cell"),
          "a consistently relabeled declared embedding is admitted by the joint typed key")

    new_minimum_chain = GrowthNode(
        by_marks[(0, 0)].marks,
        CausalOrder(relation(3, ((0, 1), (2, 0), (2, 1)))),
        by_marks[(0, 0)].element_owners,
        by_marks[(0, 0)].collar)
    try:
        grammar.admit(by_marks[(0,)], new_minimum_chain, "history-cell")
        embedding_bypass_rejected = False
    except ValueError:
        embedding_bypass_rejected = True
    check(embedding_bypass_rejected,
          "abstractly isomorphic child with an undeclared parent embedding rejects")

    foreign_boundary_order = CausalOrder(
        by_marks[(0, 0)].order.relation,
        future_boundary=(BoundaryPort(2, "leg", "foreign-cell"),))
    foreign_boundary_child = GrowthNode(
        by_marks[(0, 0)].marks, foreign_boundary_order,
        by_marks[(0, 0)].element_owners, by_marks[(0, 0)].collar)
    try:
        grammar.admit(by_marks[(0,)], foreign_boundary_child, "history-cell")
        boundary_bypass_rejected = False
    except ValueError:
        boundary_bypass_rejected = True
    check(boundary_bypass_rejected,
          "forged D16 past/future boundary metadata cannot reuse a declared edge")

    two_owner_parent = GrowthNode((), CausalOrder(relation(2, ())),
                                  ("A", "B"), Collar("A", None, Obj((Port("m", 2, owner="A"),))))
    joined = GrowthNode((0,), CausalOrder(relation(3, ((2, 0), (2, 1)))),
                        ("A", "B", "A"),
                        Collar("A", 0, append_carrier_type(two_owner_parent.collar.carrier,
                                                           "X", "A")))
    open_grammar = GrowthGrammar(())
    try:
        open_grammar.admit(two_owner_parent, joined, "A", declared=False)
        join_rejected = False
    except ValueError:
        join_rejected = True
    check(join_rejected and open_grammar.admit(two_owner_parent, joined, "A",
                                               join_entitlement=("A", "B"), declared=False),
          "cross-component join rejects without and passes with exact entitlement")

    fixed_action = IntervalAction(0, (1, 0, 0, 0, 0, 0, 0))
    action_values = {marks: fixed_action.value(node.order) for marks, node in by_marks.items()}
    action_phases = {marks: fixed_action.phase(node.order) for marks, node in by_marks.items()}
    check(action_phases[(0, 0, 0)] == -1 and action_phases[(1, 0, 1)] == 1,
          "one fixed interval action evaluates to opposite phases on the integrated size4 leaves")
    check(set(action_values) == set(by_marks),
          "the fixed action is evaluated on every causal cylinder node")

    equal = causal_tower(nodes, grammar, F(1, 2), F(1, 2), 6)
    second = causal_tower(nodes, grammar, F(9, 25), F(16, 25), 6)
    orbit = causal_tower(nodes, grammar, F(2, 3), F(1, 3), 6)
    check(is_projective_binary(equal) and is_projective_binary(second)
          and is_projective_binary(orbit),
          "equal, positive-envelope and inverse-orbit causal towers are projective")
    check(equal[3] == {(0, 0, 0): F(1, 2), (1, 0, 1): F(1, 2)}
          and second[3] == {(0, 0, 0): F(9, 25), (1, 0, 1): F(16, 25)},
          "the actual size4 causal leaves carry both supplied positive kernels")
    check(equal[6] != second[6] and second[6] != orbit[6],
          "same action and grammar admit inequivalent all-depth supplied kernels")
    check(equal[3][(1, 0, 1)] / equal[2][(1, 0)] == 1
          and F(0) / equal[2][(0, 0)] == 0,
          "integrated causal tower has the visible non-Markov conditionals one and zero")

    net1, net2, net3, commit_z = local_record_network(by_marks[()].collar.carrier)
    check(net1.target == by_marks[(0,)].collar.carrier
          and net2.target == by_marks[(0, 0)].collar.carrier
          and net3.target == by_marks[(0, 0, 0)].collar.carrier,
          "causal-node collars are the actual successive D14 network boundary types")
    check(all(port.owner == "history-cell" for port in net3.source.ports + net3.target.ports),
          "memory, sealed records and emitted collars have one explicit local owner")
    check(inner(mv(net3.amp, (ONE, ZERO)), mv(net3.amp, (ZERO, ONE))) == ZERO,
          "the owner-local three-record network is isometric on its two basis branches")
    check(mul(dagger(net3.amp), net3.amp) == eye(2),
          "the full owner-local three-commit network is exactly isometric")
    equal_amplitudes = (-ROOT_HALF, ROOT_HALF)
    second_amplitudes = (-ONE * F(3, 5), ONE * F(4, 5))
    check(record_table(net1, equal_amplitudes, 1)
          == {(0,): Q2.make(F(1, 2)), (1,): Q2.make(F(1, 2))},
          "first local commit copies the causal branch into sealed X")
    check(record_table(net2, equal_amplitudes, 2)
          == {(0, 0): Q2.make(F(1, 2)), (1, 0): Q2.make(F(1, 2))},
          "second local commit seals fixed Y=0 while carrying memory")
    check(record_table(net3, equal_amplitudes, 3)
          == {(0, 0, 0): Q2.make(F(1, 2)), (1, 0, 1): Q2.make(F(1, 2))},
          "third local commit reveals carried memory as Z on the causal leaves")
    check(record_table(net3, second_amplitudes, 3)
          == {(0, 0, 0): Q2.make(F(9, 25)), (1, 0, 1): Q2.make(F(16, 25))},
          "the second positive kernel propagates through the same local memory network")
    check(record_table_after_reset(net2, commit_z, equal_amplitudes)
          == {(0, 0, 0): Q2.make(F(1, 2)), (1, 0, 0): Q2.make(F(1, 2))},
          "owner-local CPTP memory reset changes both later causal records to Z=0")
    reset = reset_boundary_memory(net2.target)
    check(add(mul(dagger(reset[0].amp), reset[0].amp),
              mul(dagger(reset[1].amp), reset[1].amp)) == eye(net2.target.dim),
          "integrated owner-local memory reset is exactly CPTP complete")
    normal_record_map = {path: path for path in equal[3]}
    reset_record_map = dict(normal_record_map)
    reset_record_map[(1, 0, 1)] = (1, 0, 0)
    check(normal_record_map[(1, 0, 1)] != reset_record_map[(1, 0, 1)]
          and by_marks[(1, 0, 1)].order == by_marks[(1, 0, 1)].order,
          "causal path labels and intervention-dependent visible record labels are separate maps")
    orbit_amplitudes = (-ONE, ROOT_HALF)
    orbit_raw = record_table(net3, orbit_amplitudes, 3)
    orbit_total = sum(orbit_raw.values(), Q2())
    check(tuple(orbit_raw[key] / orbit_total for key in ((0, 0, 0), (1, 0, 1)))
          == (Q2.make(F(2, 3)), Q2.make(F(1, 3))),
          "inverse-automorphism orbit weights reach the integrated causal tower records")

    chain4, diamond4 = by_marks[(0, 0, 0)].order, by_marks[(1, 0, 1)].order
    labeled_counts = (24 // len(chain4.automorphisms()),
                      24 // len(diamond4.automorphisms()))
    labeled_mass = tuple(F(count, 24) for count in labeled_counts)
    labeled_total = sum(labeled_mass)
    check(tuple(mass / labeled_total for mass in labeled_mass) == (F(2, 3), F(1, 3)),
          "uniform labeled mass descends to normalized inverse-automorphism orbit mass")

    check(all(any(port.kind.startswith("live-collar") for port in net.target.ports)
              for net in (net1, net2, net3)),
          "every local record commit emits a typed live collar")
    check(tuple(port.record_id for port in net3.target.ports if port.sealed)
          == ("X", "Y", "Z"),
          "all earlier records survive exactly in the final protected future algebra")

    try:
        causal_nodes(2)
        short_rejected = False
    except ValueError:
        short_rejected = True
    check(short_rejected and not is_projective_binary({})
          and not is_projective_binary({2: {(0, 0): F(1)}}),
          "short-depth, empty and non-unit-start validator controls reject cleanly")
    malformed = {1: {(2,): F(1)}, 2: {(2, 0): F(1)}}
    check(not is_projective_binary(malformed), "nonbinary history alphabet rejects cleanly")
    independent = {1: {(0,): F(1, 2), (1,): F(1, 2)},
                   2: {(0, 0): F(1), (1, 0): F(0)}}
    check(not is_projective_binary(independent),
          "independent per-depth normalization still fails causal projectivity")

    check(action_phases[(0, 0, 0)] == -1 and action_phases[(1, 0, 1)] == 1
          and equal != second and equal != orbit,
          "fixed action plus integrated local grammar still does not select the kernel")
    check(CHECKS + 1 == EXPECTED_CHECKS, "pre-final exact check count is frozen")
    if CHECKS != EXPECTED_CHECKS:
        raise AssertionError((CHECKS, EXPECTED_CHECKS))

    semantic = {
        "schema": "d17-integrated-causal-history-exact-v1",
        "scope": "owned finite causal extensions and local records; supplied kernels",
        "checks_passed": CHECKS,
        "causal_depths": [1, 2, 3, 4, 5, 6],
        "kernels": ["equal", "positive-envelope", "inverse-orbit"],
        "verdict": "INTEGRATED-CAUSAL-HISTORY-KERNEL-NONSELECTION",
        "ceiling": "extension grammar, kernel and record commit supplied, not action-derived",
    }
    semantic_bytes = json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode()
    semantic_hash = sha256(semantic_bytes).hexdigest()
    if EXPECTED_SEMANTIC_SHA256 != "TO_BE_FROZEN" and semantic_hash != EXPECTED_SEMANTIC_SHA256:
        raise AssertionError((semantic_hash, EXPECTED_SEMANTIC_SHA256))
    packet = dict(semantic)
    packet.update({
        "semantic_sha256": semantic_hash,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "d14_dependency_sha256": hashes[0],
        "d16_dependency_sha256": hashes[1],
        "d17_dependency_sha256": hashes[2],
    })
    OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"CHECKS PASSED: {CHECKS}/{EXPECTED_CHECKS}")
    print(f"SEMANTIC SHA256: {semantic_hash}")
    print(f"SOURCE SHA256: {packet['source_sha256']}")
    print("VERDICT: INTEGRATED-CAUSAL-HISTORY-KERNEL-NONSELECTION")


if __name__ == "__main__":
    main()
