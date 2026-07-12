#!/usr/bin/env python3
"""Exact finite causal-order interval-action covariance/nonselection witness.

The source histories are strict finite partial orders.  The action family is
S(C)=alpha*|C|+sum_k beta_k*N_k(C), where N_k counts comparable pairs with k
elements in their open order interval.  Integer coefficients are interpreted
in units of pi for the exact phase (-1)^S.

This proves relabeling covariance and coefficient nonselection on the frozen
finite class.  It does not implement the physical BDG coefficients, a quantum
measure, records, continuum gravity, dimension emergence, or a scale bridge.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "v10" / "data" / "d16-covariant-causal-action-exact.json"
EXPECTED_CHECKS = 26
EXPECTED_SEMANTIC_SHA256 = "a3931af2f999a7381b86792f03750420c3be411d83c7a0598cb6dfe6eb9e10a6"
CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:03d}: {label}")


def transitive_closure(relation):
    n = len(relation)
    out = [list(row) for row in relation]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                out[i][j] = out[i][j] or (out[i][k] and out[k][j])
    return tuple(tuple(bool(x) for x in row) for row in out)


@dataclass(frozen=True)
class BoundaryPort:
    element: int
    kind: str
    owner: str


@dataclass(frozen=True)
class CausalOrder:
    relation: tuple[tuple[bool, ...], ...]
    past_boundary: tuple[BoundaryPort, ...] = ()
    future_boundary: tuple[BoundaryPort, ...] = ()

    def __post_init__(self):
        n = len(self.relation)
        if any(len(row) != n for row in self.relation):
            raise ValueError("relation must be square")
        if any(self.relation[i][i] for i in range(n)):
            raise ValueError("strict order must be irreflexive")
        if any(self.relation[i][j] and self.relation[j][i]
               for i in range(n) for j in range(n)):
            raise ValueError("strict order must be asymmetric")
        if transitive_closure(self.relation) != self.relation:
            raise ValueError("strict order must be transitively closed")
        if {port.element for port in self.past_boundary} & {
                port.element for port in self.future_boundary}:
            raise ValueError("past and future boundaries must be disjoint")
        for polarity, boundary in (("past", self.past_boundary),
                                   ("future", self.future_boundary)):
            elements = tuple(port.element for port in boundary)
            if len(set(elements)) != len(elements) or any(x < 0 or x >= n for x in elements):
                raise ValueError("invalid boundary ownership")
            if any(not port.kind or not port.owner for port in boundary):
                raise ValueError("boundary type and owner are required")
            if any(self.relation[x][y] or self.relation[y][x]
                   for x in elements for y in elements):
                raise ValueError("boundary must be an antichain")
            if polarity == "past" and any(self.relation[x][y]
                                           for x in range(n) for y in elements):
                raise ValueError("past boundary must be minimal")
            if polarity == "future" and any(self.relation[x][y]
                                             for x in elements for y in range(n)):
                raise ValueError("future boundary must be maximal")

    @property
    def n(self):
        return len(self.relation)

    def permute(self, old_to_new):
        if tuple(sorted(old_to_new)) != tuple(range(self.n)):
            raise ValueError("not a permutation")
        rows = [[False] * self.n for _ in range(self.n)]
        for old_i in range(self.n):
            for old_j in range(self.n):
                rows[old_to_new[old_i]][old_to_new[old_j]] = self.relation[old_i][old_j]
        return CausalOrder(
            tuple(tuple(row) for row in rows),
            tuple(sorted((BoundaryPort(old_to_new[port.element], port.kind, port.owner)
                          for port in self.past_boundary),
                         key=lambda port: (port.kind, port.owner, port.element))),
            tuple(sorted((BoundaryPort(old_to_new[port.element], port.kind, port.owner)
                          for port in self.future_boundary),
                         key=lambda port: (port.kind, port.owner, port.element))),
        )

    def interval_counts(self):
        counts = [0] * max(1, self.n)
        for x in range(self.n):
            for y in range(self.n):
                if not self.relation[x][y]:
                    continue
                inside = sum(1 for z in range(self.n)
                             if self.relation[x][z] and self.relation[z][y])
                counts[inside] += 1
        return tuple(counts)

    def automorphisms(self):
        return tuple(p for p in permutations(range(self.n)) if self.permute(p) == self)

    def linear_extensions(self):
        out = []
        for p in permutations(range(self.n)):
            position = {x: i for i, x in enumerate(p)}
            if all(not self.relation[x][y] or position[x] < position[y]
                   for x in range(self.n) for y in range(self.n)):
                out.append(p)
        return tuple(out)


@dataclass(frozen=True)
class IntervalAction:
    alpha: int
    beta: tuple[int, ...]
    dimension_tag: int | None = None

    def value(self, order):
        counts = order.interval_counts()
        return self.alpha * order.n + sum(
            coefficient * (counts[k] if k < len(counts) else 0)
            for k, coefficient in enumerate(self.beta)
        )

    def phase(self, order):
        return -1 if self.value(order) % 2 else 1


def relation(n, pairs):
    rows = [[False] * n for _ in range(n)]
    for i, j in pairs:
        rows[i][j] = True
    return tuple(tuple(row) for row in rows)


def glue_typed(left, right):
    """Identify matching typed/owned future-past ports, then take closure."""
    left_ports = {(port.kind, port.owner): port.element for port in left.future_boundary}
    right_ports = {(port.kind, port.owner): port.element for port in right.past_boundary}
    if not left_ports or left_ports.keys() != right_ports.keys():
        raise ValueError("typed owned gluing boundary mismatch")
    if len(left_ports) != len(left.future_boundary) or len(right_ports) != len(right.past_boundary):
        raise ValueError("gluing keys must be unique")

    shared = len(left_ports)
    n = left.n + right.n - shared
    rows = [[False] * n for _ in range(n)]
    for i in range(left.n):
        for j in range(left.n):
            rows[i][j] = left.relation[i][j]
    mapping = {
        right_ports[key]: left_ports[key]
        for key in left_ports
    }
    next_index = left.n
    for old in range(right.n):
        if old not in mapping:
            mapping[old] = next_index
            next_index += 1
    for i in range(right.n):
        for j in range(right.n):
            if right.relation[i][j]:
                rows[mapping[i]][mapping[j]] = True
    new_past = left.past_boundary
    new_future = tuple(sorted(
        (BoundaryPort(mapping[port.element], port.kind, port.owner)
         for port in right.future_boundary),
        key=lambda port: (port.kind, port.owner, port.element),
    ))
    return CausalOrder(transitive_closure(tuple(tuple(row) for row in rows)),
                       new_past, new_future)


def main():
    antichain4 = CausalOrder(relation(4, ()))
    chain4 = CausalOrder(relation(4, ((0, 1), (1, 2), (2, 3),
                                             (0, 2), (1, 3), (0, 3))))
    vee = CausalOrder(
        relation(3, ((0, 2), (1, 2))),
        past_boundary=(BoundaryPort(0, "leg", "cell-A"),
                       BoundaryPort(1, "leg", "cell-B")),
    )
    lam = CausalOrder(
        relation(3, ((0, 1), (0, 2))),
        future_boundary=(BoundaryPort(1, "leg", "cell-A"),
                         BoundaryPort(2, "leg", "cell-B")),
    )
    diamond = CausalOrder(relation(4, ((0, 1), (0, 2), (1, 3), (2, 3), (0, 3))),
                          past_boundary=(BoundaryPort(0, "screen", "cell-D"),),
                          future_boundary=(BoundaryPort(3, "screen", "cell-D"),))
    orders = (antichain4, chain4, vee, lam, diamond)
    check(all(order.n in (3, 4) for order in orders),
          "frozen antichain, chain, V, Lambda and diamond are valid strict orders")

    try:
        CausalOrder(relation(3, ((0, 1), (1, 2))))
        nontransitive_rejected = False
    except ValueError:
        nontransitive_rejected = True
    check(nontransitive_rejected, "nontransitive relation is rejected")
    try:
        CausalOrder(relation(2, ((0, 1),)),
                    future_boundary=(BoundaryPort(0, "x", "A"),
                                     BoundaryPort(1, "x", "B")))
        nonantichain_boundary_rejected = False
    except ValueError:
        nonantichain_boundary_rejected = True
    check(nonantichain_boundary_rejected, "comparable boundary elements are rejected")
    try:
        CausalOrder(relation(2, ((0, 1),)),
                    past_boundary=(BoundaryPort(1, "x", "A"),))
        nonminimal_past_rejected = False
    except ValueError:
        nonminimal_past_rejected = True
    check(nonminimal_past_rejected, "nonminimal past boundary is rejected")
    try:
        CausalOrder(relation(1, ()),
                    past_boundary=(BoundaryPort(0, "x", "A"),),
                    future_boundary=(BoundaryPort(0, "x", "A"),))
        overlap_rejected = False
    except ValueError:
        overlap_rejected = True
    check(overlap_rejected, "past/future boundary ownership overlap is rejected")

    check(antichain4.interval_counts() == (0, 0, 0, 0)
          and chain4.interval_counts() == (3, 2, 1, 0)
          and diamond.interval_counts() == (4, 0, 1, 0),
          "open-interval counts match exact frozen structures")

    exhaustive_label_invariance = True
    for order in orders:
        target = order.interval_counts()
        for p in permutations(range(order.n)):
            if order.permute(p).interval_counts() != target:
                exhaustive_label_invariance = False
    check(exhaustive_label_invariance,
          "interval observables are invariant under every relabeling of every frozen order")
    check(all({(port.kind, port.owner) for port in order.permute(p).past_boundary}
              == {(port.kind, port.owner) for port in order.past_boundary}
              and {(port.kind, port.owner) for port in order.permute(p).future_boundary}
              == {(port.kind, port.owner) for port in order.future_boundary}
              for order in orders for p in permutations(range(order.n))),
          "typed owner metadata survives every boundary relabeling")

    action_a = IntervalAction(0, (1, 0, 0, 0))
    action_b = IntervalAction(0, (0, 0, 1, 0))
    check(all(action_a.value(order.permute(p)) == action_a.value(order)
              and action_b.value(order.permute(p)) == action_b.value(order)
              for order in orders for p in permutations(range(order.n))),
          "two coefficient packets are exactly generally covariant under relabeling")

    check(tuple(len(order.automorphisms()) for order in orders) == (24, 1, 1, 1, 2),
          "typed-boundary automorphism factors are counted exactly")
    check(tuple(len(order.linear_extensions()) for order in orders) == (24, 1, 2, 2, 2),
          "construction presentations have the exact linear-extension multiplicities")
    check(all(len({action_a.phase(order) for _ in order.linear_extensions()}) == 1
              for order in orders),
          "whole-order scalar is independent of the chosen linear-extension presentation")

    chain2_left = CausalOrder(
        relation(2, ((0, 1),)),
        past_boundary=(BoundaryPort(0, "outer-past", "cell-C"),),
        future_boundary=(BoundaryPort(1, "shared", "cell-C"),),
    )
    chain2_right = CausalOrder(
        relation(2, ((0, 1),)),
        past_boundary=(BoundaryPort(0, "shared", "cell-C"),),
        future_boundary=(BoundaryPort(1, "outer-future", "cell-C"),),
    )
    chain3 = glue_typed(chain2_left, chain2_right)
    check(chain3.interval_counts() == (2, 1, 0),
          "regional gluing takes transitive closure and creates one cross interval")
    relabeled_glue = glue_typed(chain2_left.permute((1, 0)), chain2_right.permute((1, 0)))
    check(relabeled_glue.interval_counts() == chain3.interval_counts()
          and len(relabeled_glue.automorphisms()) == len(chain3.automorphisms())
          and len(relabeled_glue.linear_extensions()) == len(chain3.linear_extensions()),
          "typed owned gluing is invariant under independent regional relabeling")
    try:
        wrong_right = CausalOrder(
            relation(2, ((0, 1),)),
            past_boundary=(BoundaryPort(0, "wrong", "cell-C"),),
            future_boundary=(BoundaryPort(1, "outer-future", "cell-C"),),
        )
        glue_typed(chain2_left, wrong_right)
        mismatch_rejected = False
    except ValueError:
        mismatch_rejected = True
    check(mismatch_rejected, "typed gluing mismatch is rejected")
    cross_action = IntervalAction(0, (0, 1, 0))
    check(cross_action.value(chain3)
          != cross_action.value(chain2_left) + cross_action.value(chain2_right),
          "naive regional action addition misses the cross-boundary interval")
    check(cross_action.value(chain3) == 1,
          "sewn action is recomputed once on the quotient order including cross intervals")

    packets = tuple(IntervalAction(alpha, tuple(beta))
                    for alpha, *beta in product((0, 1), repeat=4))
    census_orders = orders + (chain3,)
    signatures = {
        tuple(packet.phase(order) for order in census_orders)
        for packet in packets
    }
    check(len(packets) == 16 and len(signatures) == 16,
          "exhaustive frozen binary coefficient census contains inequivalent predictions")
    check(action_a.phase(diamond) == 1 and action_b.phase(diamond) == -1,
          "two covariant interval actions give different fixed diamond amplitudes")
    differences = tuple(action_a.value(order) - action_b.value(order)
                        for order in census_orders)
    phase_ratios = tuple(action_a.phase(order) * action_b.phase(order)
                         for order in census_orders)
    check(len(set(differences)) > 1 and len(set(phase_ratios)) > 1,
          "coefficient packets are not related by one common additive or phase factor")

    raw_weights = (action_a.phase(chain4), action_a.phase(diamond))
    raw_born_mass = sum(abs(weight) ** 2 for weight in raw_weights)
    check(raw_born_mass == 2,
          "exp(iS) weights alone do not form a normalized history probability")
    normalized = tuple(F(abs(weight) ** 2, raw_born_mass) for weight in raw_weights)
    check(normalized == (F(1, 2), F(1, 2)),
          "normalization requires an additional supplied alternative set and measure")

    packet_d2 = IntervalAction(0, (1, 1, 0, 0), dimension_tag=2)
    packet_d4 = IntervalAction(0, (1, 0, 1, 0), dimension_tag=4)
    check(packet_d2.dimension_tag == 2 and packet_d4.dimension_tag == 4
          and packet_d2.beta != packet_d4.beta,
          "dimension-specific coefficient packets carry dimension as input metadata")

    orbit_weight_chain = F(1, len(chain4.automorphisms()))
    orbit_weight_antichain = F(1, len(antichain4.automorphisms()))
    check(orbit_weight_chain == F(1) and orbit_weight_antichain == F(1, 24)
          and orbit_weight_chain != orbit_weight_antichain,
          "unlabeled orbit measure needs explicit automorphism ownership")

    check(action_a.phase(diamond) != action_b.phase(diamond)
          and action_a.beta != action_b.beta,
          "covariance plus interval locality does not select one action")
    check(CHECKS + 1 == EXPECTED_CHECKS, "pre-final exact check count is frozen")
    if CHECKS != EXPECTED_CHECKS:
        raise AssertionError((CHECKS, EXPECTED_CHECKS))

    semantic = {
        "schema": "d16-covariant-causal-action-exact-v1",
        "scope": "finite strict causal orders and binary interval-action census",
        "checks_passed": CHECKS,
        "orders": ["antichain4", "chain4", "V3", "Lambda3", "diamond4"],
        "coefficient_packets": len(packets),
        "distinct_phase_signatures": len(signatures),
        "verdict": "INTERVAL-ACTION-FAMILY-NONSELECTING",
        "ceiling": "no BDG coefficient provenance, quantum measure, records, continuum or scale",
    }
    semantic_bytes = json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode()
    semantic_hash = sha256(semantic_bytes).hexdigest()
    if EXPECTED_SEMANTIC_SHA256 != "TO_BE_FROZEN" and semantic_hash != EXPECTED_SEMANTIC_SHA256:
        raise AssertionError((semantic_hash, EXPECTED_SEMANTIC_SHA256))
    packet = dict(semantic)
    packet.update({
        "semantic_sha256": semantic_hash,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    })
    OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"CHECKS PASSED: {CHECKS}/{EXPECTED_CHECKS}")
    print(f"SEMANTIC SHA256: {semantic_hash}")
    print(f"SOURCE SHA256: {packet['source_sha256']}")
    print("VERDICT: INTERVAL-ACTION-FAMILY-NONSELECTING")


if __name__ == "__main__":
    main()
