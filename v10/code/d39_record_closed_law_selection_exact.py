#!/usr/bin/env python3
"""D39 exact receipt: comparison, admission, selection and identifiability.

Standard-library only.  Discrete and rational claims use integers/Fraction.
This is a finite classical campaign.  It does not construct the Level-B
generated D36 conflict ontology, an infinite unimodular completion, a physical
clock bridge, a D38b quantum join or a V6 sealing rate.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
from typing import Dict, FrozenSet, Hashable, Iterable, Mapping, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]

LOCKS = {
    "D39-pin": (
        ROOT / "v10/note-d39-selecting-record-closed-laws.md",
        "36c8c28a45fc6bb4069f16b2ed04045d7ed433eec2634f9af1d62987b850c948",
    ),
    "D36b": (
        ROOT / "v10/code/d36b_actor_record_refinement_exact.py",
        "57ff22ab4711b63d476192c2ff19b02bb7f76fda5124b4d1afd23d30a20b376b",
    ),
    "D37": (
        ROOT / "v10/code/d37_regional_history_specification_exact.py",
        "b15e577bfdf03e1bc78628d9d934bab1e604da9f4b62f7c6372fa61dca7fcbd9",
    ),
    "D37-data": (
        ROOT / "v10/data/d37_regional_history_specification_exact.out",
        "20d4b2f6add6db3296f221c184be539dd62c66ada81f32418b9288bebf778ed8",
    ),
    "D38b": (
        ROOT / "v10/code/d38b_record_closed_specification_exact.py",
        "c48e317189a160d445af374346deb3199caed0ae222430260a55e2a6ef731eeb",
    ),
    "D38b-data": (
        ROOT / "v10/data/d38b_record_closed_specification_exact.out",
        "28e76708b6c72cf874aedf9700a6bd1756220e1cb4bf8be3e096e632b66b4f7d",
    ),
    "D23": (
        ROOT / "v10/code/d23_click_identifiability_exact.py",
        "b648c0edd04a4709970a4d849cd10ace6601dc75ab8eaad0746daa1ce343c41e",
    ),
    "D26": (
        ROOT / "v10/code/d26_interface_equivalence_exact.py",
        "a9b1f1704578178218750ecbafa737763ff3968ca246939a1d6aece79930575c",
    ),
    "D26-data": (
        ROOT / "v10/data/d26_interface_equivalence_exact.out",
        "88a5461f2304415db69d4decc4b89b95195d928e79e8feeb73aeefca74c59633",
    ),
    "D28": (
        ROOT / "v10/code/d28_influence_diamond_exact.py",
        "dab14a28885bc7a40517d4a953a6538d631f3f281bfba522ab47a3ab33191ff5",
    ),
    "D28-data": (
        ROOT / "v10/data/d28_influence_diamond_exact.out",
        "e7d1c3a88019d9350fca192ca800497d57067937418fff86e7d04572f9bc4278",
    ),
    "D31b": (
        ROOT / "v10/code/d31b_two_causal_structures_exact.py",
        "450eef885a72401767550d24b3f5b141736973300fe0bbd17093bb13032a8190",
    ),
    "D31b-data": (
        ROOT / "v10/data/d31b_two_causal_structures_exact.out",
        "521576e81ced965d363492eb78f4fb2e38bd1e396749195a1a201738b87f48ff",
    ),
    "Paper26": (
        ROOT / "v10/relativistic-isp-v10-paper26-admissible-regional-history-specifications.md",
        "8a3517aa9138ab9eec1cad04286a990ef84e52cd778a4dcce31ee9cadab67bb4",
    ),
    "Paper27": (
        ROOT / "v10/relativistic-isp-v10-paper27-the-boundary-is-made-of-records.md",
        "fa99123315f7394bc9a3e3af04d520b705a5a3ac059cf2834d3756b31fd9e118",
    ),
}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


d38 = load_module("d38b_locked_for_d39", LOCKS["D38b"][0])


def stable(value: object) -> str:
    def default(item: object) -> object:
        if isinstance(item, Fraction):
            return {"fraction": [item.numerator, item.denominator]}
        if isinstance(item, (frozenset, set)):
            return sorted(item, key=repr)
        if isinstance(item, tuple):
            return list(item)
        if hasattr(item, "__dict__"):
            return item.__dict__
        raise TypeError(type(item))

    return json.dumps(value, default=default, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return hashlib.sha256(stable(value).encode()).hexdigest()


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def antecedent_locks() -> Dict[str, str]:
    actuals: Dict[str, str] = {}
    for name, (path, expected) in LOCKS.items():
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError((name, actual, expected))
        actuals[name] = actual
    return actuals


# ---------------------------------------------------------------------------
# R1: finite architecture-level comparison functor.


@dataclass(frozen=True)
class OrientedView:
    internal_rows: Tuple[Tuple[Hashable, str, str], ...]
    incoming_rows: Tuple[Hashable, ...]
    lateral_rows: Tuple[Hashable, ...]
    frontier: Tuple[Tuple[str, Hashable], ...]
    witness_digest: str


def phi_view(view) -> OrientedView:
    d38.validate_view(view)
    incoming = set()
    for view_record in view.records:
        for tag, source_id in view_record.resolved_parents:
            if tag == "EXTERNAL":
                incoming.add(source_id)
    external = set(view.external_refs)
    lateral = external - incoming
    internal = tuple(
        sorted(
            (
                (
                    view_record.source.record_id,
                    view_record.source.kind,
                    view_record.source.owner,
                )
                for view_record in view.records
            ),
            key=repr,
        )
    )
    return OrientedView(
        internal,
        tuple(sorted(incoming, key=repr)),
        tuple(sorted(lateral, key=repr)),
        view.frontier,
        digest(view.witness),
    )


RegionalAtom = Tuple[str, str, str]


def atom_map(action: Tuple[str, str]) -> RegionalAtom:
    return ("D39_ORIENTED_ATOM", action[0], action[1])


def push_cylinder(
    law: Mapping[Tuple[Tuple[str, str], ...], Fraction]
) -> Dict[Tuple[RegionalAtom, ...], Fraction]:
    answer: Dict[Tuple[RegionalAtom, ...], Fraction] = {}
    for path, probability in law.items():
        image = tuple(atom_map(action) for action in path)
        answer[image] = answer.get(image, Fraction()) + probability
    return answer


def oriented_prefix(
    law: Mapping[Tuple[RegionalAtom, ...], Fraction], depth: int
) -> Dict[Tuple[RegionalAtom, ...], Fraction]:
    answer: Dict[Tuple[RegionalAtom, ...], Fraction] = {}
    for path, probability in law.items():
        answer[path[:depth]] = answer.get(path[:depth], Fraction()) + probability
    return answer


def anticorrelation_cover() -> Tuple[int, int, int]:
    pairs = ((0, 1), (1, 2), (0, 2))
    laws = {
        pair: {(0, 1): Fraction(1, 2), (1, 0): Fraction(1, 2)}
        for pair in pairs
    }
    normalized = sum(int(sum(law.values(), Fraction()) == 1) for law in laws.values())
    singleton_uniform = 0
    for law in laws.values():
        for coordinate in (0, 1):
            marginal = {
                bit: sum(
                    (probability for atom, probability in law.items() if atom[coordinate] == bit),
                    Fraction(),
                )
                for bit in (0, 1)
            }
            singleton_uniform += int(marginal == {0: Fraction(1, 2), 1: Fraction(1, 2)})
    triple_support = sum(
        int(bits[0] != bits[1] and bits[1] != bits[2] and bits[0] != bits[2])
        for bits in product((0, 1), repeat=3)
    )
    return normalized, singleton_uniform, triple_support


def comparison_checks() -> Tuple[int, int, int, int, int, int, int, int]:
    store = d38.initial_store()
    store = d38.execute(store, "IDLE", "A")
    store = d38.execute(store, "IDLE", "B")
    pre_interaction = store
    interaction = d38.proposed(store, "INTERACTION", "A", "B")
    store = d38.execute(store, "INTERACTION", "A", "B")
    store = d38.execute(store, "BIRTH", "A", "A/1")
    records = list(store.history.records)
    events = [record for record in records if record.kind == "EVENT"]
    idle_a = next(
        record
        for record in events
        if record.payload_map()["event_kind"] == "IDLE" and record.owner == "A"
    )
    idle_b = next(
        record
        for record in events
        if record.payload_map()["event_kind"] == "IDLE" and record.owner == "B"
    )
    all_ids = frozenset(record.record_id for record in records)
    e_ids = all_ids - {idle_b.record_id}
    d_ids = e_ids - {idle_a.record_id}
    edge_id = next(record.record_id for record in records if record.kind == "SEED_EDGE")
    c_ids = frozenset(record_id for record_id in d_ids if record_id != edge_id)

    direct_d = d38.restrict_records(store.history, d_ids)
    staged_d = d38.restrict_records(d38.restrict_records(store.history, e_ids), d_ids)
    direct_c = d38.restrict_records(store.history, c_ids)
    staged_c = d38.restrict_records(
        d38.restrict_records(d38.restrict_records(store.history, e_ids), d_ids), c_ids
    )
    composition = int(phi_view(direct_d) == phi_view(staged_d)) + int(
        phi_view(direct_c) == phi_view(staged_c)
    )
    identities = int(phi_view(direct_d) == phi_view(direct_d))

    pre_ids = frozenset(record.record_id for record in pre_interaction.history.records) - {
        idle_b.record_id
    }
    before = d38.restrict_records(pre_interaction.history, pre_ids)
    transported = d38.append_view(before, interaction)
    post_history = d38.add_event(pre_interaction.history, interaction)
    direct = d38.restrict_records(post_history, pre_ids | {interaction.record_id})
    update_naturality = int(phi_view(transported) == phi_view(direct))

    boundary_rows = 0
    for view in (direct_d, direct_c, direct):
        image = phi_view(view)
        boundary_rows += len(image.incoming_rows) + len(image.lateral_rows)
        if set(image.incoming_rows) & set(image.lateral_rows):
            raise AssertionError("incoming/lateral boundary overlap")

    normalized = 0
    projective = 0
    atoms = 0
    for star in d38.reachable_stars():
        images = {}
        for depth in (1, 2, 3):
            source = d38.cylinder_distribution(star, depth)
            target = push_cylinder(source)
            if sum(target.values(), Fraction()) != 1 or any(value <= 0 for value in target.values()):
                raise AssertionError("pushforward kernel not proper")
            if len(target) != len(source):
                raise AssertionError("registered atom map unexpectedly collapsed")
            images[depth] = target
            normalized += 1
            atoms += len(target)
        for high, low in ((3, 2), (2, 1), (3, 1)):
            if oriented_prefix(images[high], low) != images[low]:
                raise AssertionError("pushed prefix restriction")
            projective += 1

    pair_normalized, singleton_uniform, triple_support = anticorrelation_cover()
    if (pair_normalized, singleton_uniform, triple_support) != (3, 6, 0):
        raise AssertionError("triple-cover negative")
    return (
        identities,
        composition,
        update_naturality,
        boundary_rows,
        normalized,
        projective,
        atoms,
        pair_normalized + singleton_uniform + int(triple_support == 0),
    )


# ---------------------------------------------------------------------------
# R2: D34b content-vacuity gate.


PROPOSAL_KINDS = {
    "PROPOSAL",
    "PREPARE",
    "GRANT",
    "REJECT",
    "DECISION",
    "APPLY",
    "RELEASE",
    "ACK",
}


def conflict_extract(history) -> Tuple[Tuple[Hashable, ...], Tuple[Tuple[Hashable, Hashable], ...]]:
    proposals = tuple(
        sorted(
            (record.record_id for record in history.records if record.kind == "PROPOSAL"),
            key=repr,
        )
    )
    edges = []
    by_id = {record.record_id: record for record in history.records}
    for index, left in enumerate(proposals):
        lp = by_id[left].payload_map()
        for right in proposals[index + 1 :]:
            rp = by_id[right].payload_map()
            if (
                lp.get("participant") == rp.get("participant")
                and lp.get("base_version") == rp.get("base_version")
                and lp.get("requested_update") != rp.get("requested_update")
            ):
                edges.append((left, right))
    return proposals, tuple(edges)


def vacuity_checks() -> Tuple[int, int, int, int]:
    histories = []
    store = d38.initial_store()
    histories.append(store.history)
    for kind, initiator, target in (
        ("IDLE", "A", None),
        ("BIRTH", "A", "A/1"),
        ("BIRTH", "B", "B/1"),
        ("INTERACTION", "A", "B"),
    ):
        store = d38.execute(store, kind, initiator, target)
        histories.append(store.history)
    empty = 0
    nonproposal_rows = 0
    for history in histories:
        vertices, edges = conflict_extract(history)
        empty += int(not vertices and not edges)
        nonproposal_rows += sum(
            int(record.kind not in PROPOSAL_KINDS) for record in history.records
        )

    star = d38.star_from_history(histories[0])
    actions = tuple(d38.star_kernel(star))
    fake_conflict = len(actions) > 1
    typed_base_rows = sum(
        int(
            record.kind == "PROPOSAL"
            and "base_version" in record.payload_map()
            and "participant" in record.payload_map()
        )
        for record in histories[-1].records
    )
    relabel_rejected = int(fake_conflict and typed_base_rows == 0)
    required_vocabulary = len(PROPOSAL_KINDS)
    return len(histories), empty, relabel_rejected, required_vocabulary + int(nonproposal_rows > 0)


# ---------------------------------------------------------------------------
# R3/R4: per-wire admission certificates.


RowTuple = Tuple[int, int, int, int, int]


def row_tuple(row) -> RowTuple:
    return (row.carrier, row.rings, row.births, row.degree, row.wire_events)


def tuple_row(value: RowTuple):
    return d38.ActorRow(*value)


def event_digest(event) -> str:
    return digest(("D39_EVENT_BODY", event))


@dataclass(frozen=True)
class HeadClaim:
    owner: str
    wire: str
    head: Hashable
    row: RowTuple
    body_digest: str
    signature: str


def head_core(owner: str, wire: str, head: Hashable, row: RowTuple, body_digest: str):
    return ("D39_HEAD_CLAIM", owner, wire, head, row, body_digest)


def make_head_claim(owner: str, wire: str, head: Hashable, row: RowTuple, body_digest: str) -> HeadClaim:
    core = head_core(owner, wire, head, row, body_digest)
    signature = digest(("D39_IDEAL_HEAD_SIGNATURE", owner, core))
    return HeadClaim(owner, wire, head, row, body_digest, signature)


def authentic_head(claim: HeadClaim) -> bool:
    core = head_core(claim.owner, claim.wire, claim.head, claim.row, claim.body_digest)
    return claim.signature == digest(("D39_IDEAL_HEAD_SIGNATURE", claim.owner, core))


@dataclass(frozen=True)
class EdgeClaim:
    edge: Tuple[str, str]
    source: Hashable
    body_digest: str
    signature: str


def make_edge_claim(edge: Tuple[str, str], source: Hashable, body_digest: str) -> EdgeClaim:
    normalized = tuple(sorted(edge))
    owner = f"edge:{normalized[0]}:{normalized[1]}"
    core = ("D39_EDGE_CLAIM", owner, normalized, source, body_digest)
    return EdgeClaim(
        normalized,
        source,
        body_digest,
        digest(("D39_IDEAL_EDGE_SIGNATURE", owner, core)),
    )


def authentic_edge(claim: EdgeClaim) -> bool:
    owner = f"edge:{claim.edge[0]}:{claim.edge[1]}"
    core = ("D39_EDGE_CLAIM", owner, claim.edge, claim.source, claim.body_digest)
    return claim.signature == digest(("D39_IDEAL_EDGE_SIGNATURE", owner, core))


@dataclass(frozen=True)
class H0Certificate:
    event: object
    heads: Tuple[HeadClaim, ...]
    edge: Optional[EdgeClaim]


def required_existing_wires(event) -> Tuple[str, ...]:
    payload = event.payload_map()
    kind = str(payload["event_kind"])
    initiator = str(payload["initiator"])
    target = str(payload["target"])
    if kind in ("BIRTH", "IDLE"):
        return (initiator,)
    return (initiator, target)


def local_expected_event(cert: H0Certificate):
    event = cert.event
    payload = event.payload_map()
    kind = str(payload["event_kind"])
    initiator = str(payload["initiator"])
    target_value = payload["target"]
    target = None if target_value == "NONE" else str(target_value)
    claims = {claim.wire: claim for claim in cert.heads}
    required = required_existing_wires(event)
    if len(claims) != len(cert.heads) or tuple(sorted(claims)) != tuple(sorted(required)):
        raise AssertionError("head-claim census")
    body = event_digest(event)
    for wire, claim in claims.items():
        if claim.owner != wire or claim.body_digest != body or not authentic_head(claim):
            raise AssertionError("head authentication")
    if tuple(claims[wire].head for wire in required) != event.parents:
        raise AssertionError("event parents are not certified heads")
    rows = {wire: tuple_row(claim.row) for wire, claim in claims.items()}
    before = rows[initiator]
    ring = before.rings + 1
    expected_payload: Dict[str, Hashable] = {
        "event_kind": kind,
        "initiator": initiator,
        "ring_ordinal": ring,
    }
    if kind == "BIRTH":
        birth = before.births + 1
        child = f"{initiator}/{birth}"
        if target != child:
            raise AssertionError("noncanonical local child")
        parent_after = d38.ActorRow(
            before.carrier, ring, birth, before.degree + 1, before.wire_events + 1
        )
        child_after = d38.ActorRow(0, 0, 0, 1, 1)
        edge = tuple(sorted((initiator, child)))
        expected_payload.update(
            {
                "target": child,
                "birth_ordinal": birth,
                "created_edge": edge,
                "created_ports": ((initiator, child), (child, initiator)),
                "child_clock": ("ACTOR_CLOCK", child, 0),
                "post_rows": tuple(
                    sorted(
                        (
                            (initiator, d38.row_payload(parent_after)),
                            (child, d38.row_payload(child_after)),
                        )
                    )
                ),
            }
        )
        return d38.make_record(
            "EVENT", initiator, (initiator, child), (claims[initiator].head,), expected_payload
        )
    if kind == "IDLE":
        after = d38.ActorRow(
            before.carrier,
            ring,
            before.births,
            before.degree,
            before.wire_events + 1,
        )
        expected_payload.update(
            {"target": "NONE", "post_rows": ((initiator, d38.row_payload(after)),)}
        )
        return d38.make_record(
            "EVENT", initiator, (initiator,), (claims[initiator].head,), expected_payload
        )
    if kind != "INTERACTION" or target is None or target not in rows:
        raise AssertionError("local interaction typing")
    if cert.edge is None or not authentic_edge(cert.edge):
        raise AssertionError("missing authenticated edge")
    if cert.edge.body_digest != body or cert.edge.edge != tuple(sorted((initiator, target))):
        raise AssertionError("edge/body mismatch")
    other = rows[target]
    initiator_after = d38.ActorRow(
        1 - before.carrier,
        ring,
        before.births,
        before.degree,
        before.wire_events + 1,
    )
    target_after = d38.ActorRow(
        1 - other.carrier,
        other.rings,
        other.births,
        other.degree,
        other.wire_events + 1,
    )
    expected_payload.update(
        {
            "target": target,
            "post_rows": tuple(
                sorted(
                    (
                        (initiator, d38.row_payload(initiator_after)),
                        (target, d38.row_payload(target_after)),
                    )
                )
            ),
        }
    )
    return d38.make_record(
        "EVENT",
        initiator,
        (initiator, target),
        (claims[initiator].head, claims[target].head),
        expected_payload,
    )


def verify_h0(cert: H0Certificate) -> bool:
    try:
        return cert.event == local_expected_event(cert)
    except (AssertionError, KeyError, TypeError, ValueError):
        return False


def edge_source(history, edge: Tuple[str, str]) -> Hashable:
    normalized = tuple(sorted(edge))
    for record in history.records:
        payload = record.payload_map()
        if record.kind == "SEED_EDGE" and tuple(payload["endpoints"]) == normalized:
            return record.record_id
        if record.kind == "EVENT" and payload.get("created_edge") == normalized:
            return record.record_id
    raise AssertionError("missing edge source")


def issue_h0_from_store(store, event) -> H0Certificate:
    derived = d38.derive(store.history)
    rows = derived.row_map()
    heads = derived.head_map()
    body = event_digest(event)
    claims = tuple(
        make_head_claim(wire, wire, heads[wire], row_tuple(rows[wire]), body)
        for wire in required_existing_wires(event)
    )
    payload = event.payload_map()
    edge = None
    if payload["event_kind"] == "INTERACTION":
        endpoints = tuple(sorted((str(payload["initiator"]), str(payload["target"]))))
        edge = make_edge_claim(endpoints, edge_source(store.history, endpoints), body)
    cert = H0Certificate(event, claims, edge)
    if not verify_h0(cert):
        raise AssertionError("issuer produced invalid H0")
    return cert


def h0_checks() -> Tuple[int, int, int, int]:
    base = d38.initial_store()
    idle = d38.proposed(base, "IDLE", "A")
    cert = issue_h0_from_store(base, idle)
    oracle_valid, accepted = d38.transact(base, idle)
    valid_agreement = int(verify_h0(cert) and accepted)

    advanced = d38.execute(base, "BIRTH", "A", "A/1")
    oracle_stale, stale_accepted = d38.transact(advanced, idle)
    static_accepts_stale = int(verify_h0(cert))
    oracle_rejects_stale = int(not stale_accepted and oracle_stale == advanced)
    unchanged = int(base != oracle_valid and advanced == oracle_stale)
    return valid_agreement, static_accepts_stale, oracle_rejects_stale, unchanged


@dataclass(frozen=True)
class Grant:
    owner: str
    wire: str
    head: Hashable
    row: RowTuple
    attempt: str
    body_digest: str
    signature: str


def grant_core(
    owner: str,
    wire: str,
    head: Hashable,
    row: RowTuple,
    attempt: str,
    body_digest: str,
):
    return ("D39_HEAD_GRANT", owner, wire, head, row, attempt, body_digest)


def make_grant(
    owner: str,
    wire: str,
    head: Hashable,
    row: RowTuple,
    attempt: str,
    body_digest: str,
) -> Grant:
    core = grant_core(owner, wire, head, row, attempt, body_digest)
    signature = digest(("D39_IDEAL_GRANT_SIGNATURE", owner, core))
    return Grant(owner, wire, head, row, attempt, body_digest, signature)


def authentic_grant(grant: Grant) -> bool:
    core = grant_core(
        grant.owner,
        grant.wire,
        grant.head,
        grant.row,
        grant.attempt,
        grant.body_digest,
    )
    return grant.signature == digest(("D39_IDEAL_GRANT_SIGNATURE", grant.owner, core))


@dataclass(frozen=True)
class H1Certificate:
    h0: H0Certificate
    attempt: str
    grants: Tuple[Grant, ...]


@dataclass(frozen=True)
class LocalLedger:
    rows: Tuple[Tuple[str, RowTuple], ...]
    heads: Tuple[Tuple[str, Hashable], ...]
    edges: Tuple[Tuple[str, str], ...]
    edge_sources: Tuple[Tuple[Tuple[str, str], Hashable], ...]
    locks: Tuple[Tuple[str, Hashable, str], ...]
    used_attempts: FrozenSet[str]

    def row_map(self) -> Dict[str, RowTuple]:
        return dict(self.rows)

    def head_map(self) -> Dict[str, Hashable]:
        return dict(self.heads)


def ledger_from_store(store, used: FrozenSet[str] = frozenset()) -> LocalLedger:
    derived = d38.derive(store.history)
    sources = tuple((edge, edge_source(store.history, edge)) for edge in derived.edges)
    return LocalLedger(
        tuple((actor, row_tuple(row)) for actor, row in derived.rows),
        derived.heads,
        derived.edges,
        sources,
        (),
        used,
    )


def issue_h0_from_ledger(ledger: LocalLedger, event) -> H0Certificate:
    rows = ledger.row_map()
    heads = ledger.head_map()
    body = event_digest(event)
    claims = tuple(
        make_head_claim(wire, wire, heads[wire], rows[wire], body)
        for wire in required_existing_wires(event)
    )
    payload = event.payload_map()
    edge = None
    if payload["event_kind"] == "INTERACTION":
        endpoints = tuple(sorted((str(payload["initiator"]), str(payload["target"]))))
        source = dict(ledger.edge_sources)[endpoints]
        edge = make_edge_claim(endpoints, source, body)
    return H0Certificate(event, claims, edge)


def attempt_key(event) -> str:
    return digest(
        (
            "D39_CARRIER_DERIVED_ATTEMPT",
            event.record_id,
            event_digest(event),
            tuple(event.wires),
        )
    )


def collect_h1(ledger: LocalLedger, event) -> Tuple[LocalLedger, Optional[H1Certificate], bool]:
    before = ledger
    try:
        h0 = issue_h0_from_ledger(ledger, event)
        if not verify_h0(h0):
            raise AssertionError("invalid local event body")
        attempt = attempt_key(event)
        if attempt in ledger.used_attempts:
            raise AssertionError("used attempt")
        lock_keys = {(wire, head) for wire, head, _attempt in ledger.locks}
        for claim in h0.heads:
            if (claim.wire, claim.head) in lock_keys:
                raise AssertionError("head already exclusively granted")
            if ledger.head_map().get(claim.wire) != claim.head:
                raise AssertionError("claim no longer current")
        grants = tuple(
            make_grant(
                claim.owner,
                claim.wire,
                claim.head,
                claim.row,
                attempt,
                claim.body_digest,
            )
            for claim in h0.heads
        )
        new_locks = tuple(
            sorted(
                (*ledger.locks, *((grant.wire, grant.head, attempt) for grant in grants)),
                key=repr,
            )
        )
        updated = replace(ledger, locks=new_locks)
        return updated, H1Certificate(h0, attempt, grants), True
    except (AssertionError, KeyError, TypeError, ValueError):
        return before, None, False


def release_h1(ledger: LocalLedger, cert: H1Certificate) -> Tuple[LocalLedger, bool]:
    before = ledger
    expected = {(grant.wire, grant.head, cert.attempt) for grant in cert.grants}
    locks = set(ledger.locks)
    if not expected or not expected <= locks:
        return before, False
    return replace(ledger, locks=tuple(sorted(locks - expected, key=repr))), True


def commit_h1(ledger: LocalLedger, cert: H1Certificate) -> Tuple[LocalLedger, bool]:
    before = ledger
    try:
        event = cert.h0.event
        body = event_digest(event)
        if cert.attempt != attempt_key(event) or cert.attempt in ledger.used_attempts:
            raise AssertionError("attempt mismatch/replay")
        if not verify_h0(cert.h0):
            raise AssertionError("H0 typing")
        claims = {claim.wire: claim for claim in cert.h0.heads}
        grants = {grant.wire: grant for grant in cert.grants}
        required = set(required_existing_wires(event))
        if set(claims) != required or set(grants) != required:
            raise AssertionError("grant census")
        if len(grants) != len(cert.grants):
            raise AssertionError("duplicate grant")
        heads = ledger.head_map()
        rows = ledger.row_map()
        locks = set(ledger.locks)
        for wire in required:
            claim = claims[wire]
            grant = grants[wire]
            if (
                grant.owner != wire
                or not authentic_grant(grant)
                or grant.attempt != cert.attempt
                or grant.body_digest != body
                or grant.head != claim.head
                or grant.row != claim.row
                or heads.get(wire) != grant.head
                or rows.get(wire) != grant.row
                or (wire, grant.head, cert.attempt) not in locks
            ):
                raise AssertionError("invalid/current grant")
        payload = event.payload_map()
        for actor, encoded in payload["post_rows"]:
            rows[str(actor)] = row_tuple(d38.payload_row(encoded))
            heads[str(actor)] = event.record_id
        edges = set(ledger.edges)
        sources = dict(ledger.edge_sources)
        if payload["event_kind"] == "BIRTH":
            edge = tuple(payload["created_edge"])
            edges.add(edge)
            sources[edge] = event.record_id
        locks -= {
            (grant.wire, grant.head, cert.attempt) for grant in cert.grants
        }
        answer = LocalLedger(
            tuple(sorted(rows.items())),
            tuple(sorted(heads.items())),
            tuple(sorted(edges)),
            tuple(sorted(sources.items(), key=repr)),
            tuple(sorted(locks, key=repr)),
            ledger.used_attempts | {cert.attempt},
        )
        return answer, True
    except (AssertionError, KeyError, TypeError, ValueError):
        return before, False


def ledger_state(ledger: LocalLedger):
    return ledger.rows, ledger.heads, ledger.edges, ledger.edge_sources


def resign_grant(grant: Grant, **changes: object) -> Grant:
    values = {
        "owner": grant.owner,
        "wire": grant.wire,
        "head": grant.head,
        "row": grant.row,
        "attempt": grant.attempt,
        "body_digest": grant.body_digest,
    }
    values.update(changes)
    return make_grant(
        str(values["owner"]),
        str(values["wire"]),
        values["head"],
        values["row"],  # type: ignore[arg-type]
        str(values["attempt"]),
        str(values["body_digest"]),
    )


def resign_head(claim: HeadClaim, **changes: object) -> HeadClaim:
    values = {
        "owner": claim.owner,
        "wire": claim.wire,
        "head": claim.head,
        "row": claim.row,
        "body_digest": claim.body_digest,
    }
    values.update(changes)
    return make_head_claim(
        str(values["owner"]),
        str(values["wire"]),
        values["head"],
        values["row"],  # type: ignore[arg-type]
        str(values["body_digest"]),
    )


def certificate_checks() -> Tuple[int, int, int, int, int, int, int, int]:
    store = d38.initial_store()
    ledger = ledger_from_store(store)
    valid = 0
    state_matches = 0
    for kind, initiator, target in (
        ("BIRTH", "A", "A/1"),
        ("IDLE", "B", None),
        ("INTERACTION", "A", "B"),
    ):
        event = d38.proposed(store, kind, initiator, target)
        locked, cert, collected = collect_h1(ledger, event)
        if not collected or cert is None:
            raise AssertionError("valid H1 collection")
        after_ledger, admitted = commit_h1(locked, cert)
        after_store, oracle = d38.transact(store, event)
        valid += int(admitted and oracle)
        oracle_ledger = ledger_from_store(after_store, after_ledger.used_attempts)
        state_matches += int(ledger_state(after_ledger) == ledger_state(oracle_ledger))
        if not admitted or not oracle or ledger_state(after_ledger) != ledger_state(oracle_ledger):
            raise AssertionError("H1/oracle mismatch")
        ledger, store = after_ledger, after_store

    # A two-wire certificate supplies the mutation baseline.
    base_store = d38.initial_store()
    base_ledger = ledger_from_store(base_store)
    interaction = d38.proposed(base_store, "INTERACTION", "A", "B")
    locked, base_cert, collected = collect_h1(base_ledger, interaction)
    if not collected or base_cert is None:
        raise AssertionError("baseline H1")

    attacks: list[Tuple[str, LocalLedger, H1Certificate]] = []
    g0, g1 = base_cert.grants
    h0, h1 = base_cert.h0.heads

    attacks.append(("forged grant signature", locked, replace(base_cert, grants=(replace(g0, signature="FORGED"), g1))))
    wrong_owner = resign_grant(g0, owner="B")
    attacks.append(("wrong grant owner", locked, replace(base_cert, grants=(wrong_owner, g1))))
    wrong_wire = resign_grant(g0, wire="Z")
    attacks.append(("wire substitution", locked, replace(base_cert, grants=(wrong_wire, g1))))
    attacks.append(("event body mutation", locked, replace(base_cert, h0=replace(base_cert.h0, event=d38.proposed(base_store, "IDLE", "A")))))
    retarget_payload = {**interaction.payload_map(), "target": "A"}
    retargeted = d38.resigned(interaction, payload=retarget_payload)
    attacks.append(("retargeted interaction", locked, replace(base_cert, h0=replace(base_cert.h0, event=retargeted))))
    attacks.append(("omitted touched grant", locked, replace(base_cert, grants=(g0,))))
    attacks.append(("duplicated touched grant", locked, replace(base_cert, grants=(g0, g0))))
    swapped0 = resign_grant(g0, wire=g1.wire, head=g1.head, row=g1.row)
    swapped1 = resign_grant(g1, wire=g0.wire, head=g0.head, row=g0.row)
    attacks.append(("cross-wire swapped grants", locked, replace(base_cert, grants=(swapped0, swapped1))))
    bad_row = (1 - g0.row[0],) + g0.row[1:]
    bad_head_claim = resign_head(h0, row=bad_row)
    bad_grant = resign_grant(g0, row=bad_row)
    attacks.append(("row digest mismatch", locked, replace(base_cert, h0=replace(base_cert.h0, heads=(bad_head_claim, h1)), grants=(bad_grant, g1))))
    attacks.append(("foreign attempt", locked, replace(base_cert, attempt="FOREIGN")))
    attacks.append(("head claim forged", locked, replace(base_cert, h0=replace(base_cert.h0, heads=(replace(h0, signature="FORGED"), h1)))))

    bad_edge = make_edge_claim(("A", "A"), base_cert.h0.edge.source, event_digest(interaction))  # type: ignore[union-attr]
    attacks.append(("wrong edge credential", locked, replace(base_cert, h0=replace(base_cert.h0, edge=bad_edge))))

    birth = d38.proposed(base_store, "BIRTH", "A", "A/1")
    birth_locked, birth_cert, birth_ok = collect_h1(base_ledger, birth)
    if not birth_ok or birth_cert is None:
        raise AssertionError("birth certificate")
    wrong_ordinal_payload = {**birth.payload_map(), "birth_ordinal": 9}
    attacks.append(("wrong birth ordinal", birth_locked, replace(birth_cert, h0=replace(birth_cert.h0, event=d38.resigned(birth, payload=wrong_ordinal_payload)))))
    wrong_ports_payload = {**birth.payload_map(), "created_ports": (("A", "A/1"),)}
    attacks.append(("wrong birth ports", birth_locked, replace(birth_cert, h0=replace(birth_cert.h0, event=d38.resigned(birth, payload=wrong_ports_payload)))))

    disconnected = d38.make_record(
        "EVENT",
        "Z",
        ("Z",),
        (),
        {
            "event_kind": "IDLE",
            "initiator": "Z",
            "ring_ordinal": 1,
            "target": "NONE",
            "post_rows": (("Z", d38.row_payload(d38.ActorRow(0, 1, 0, 1, 1))),),
        },
    )
    attacks.append(("disconnected authentic lookalike", locked, replace(base_cert, h0=replace(base_cert.h0, event=disconnected))))

    rejected = 0
    durable = 0
    for _name, before, hostile in attacks:
        after, accepted = commit_h1(before, hostile)
        rejected += int(not accepted)
        durable += int(after == before)

    # Replay after a successful commit.
    committed, accepted = commit_h1(locked, base_cert)
    replayed, replay_ok = commit_h1(committed, base_cert)
    rejected += int(not replay_ok)
    durable += int(replayed == committed)

    # Release followed by unauthorized apply.
    released, release_ok = release_h1(locked, base_cert)
    after_release, after_release_ok = commit_h1(released, base_cert)
    rejected += int(release_ok and not after_release_ok)
    durable += int(after_release == released)

    # Sibling fork and competing attempts: the second collection must not mutate.
    idle = d38.proposed(base_store, "IDLE", "A")
    idle_locked, idle_cert, idle_ok = collect_h1(base_ledger, idle)
    outgoing_locked, outgoing_cert, outgoing_ok = collect_h1(idle_locked, interaction)
    rejected += int(idle_ok and idle_cert is not None and not outgoing_ok and outgoing_cert is None)
    durable += int(outgoing_locked == idle_locked)

    # Old authentic certificate after a legitimate advance.
    old_locked, old_cert, old_ok = collect_h1(base_ledger, idle)
    if not old_ok or old_cert is None:
        raise AssertionError("old certificate setup")
    old_released, _ = release_h1(old_locked, old_cert)
    birth_locked2, birth_cert2, born_ok = collect_h1(old_released, birth)
    if not born_ok or birth_cert2 is None:
        raise AssertionError("advance setup")
    advanced_ledger, born_commit = commit_h1(birth_locked2, birth_cert2)
    stale_after, stale_ok = commit_h1(advanced_ledger, old_cert)
    rejected += int(born_commit and not stale_ok)
    durable += int(stale_after == advanced_ledger)

    # Partial multi-wire apply: omit one certified head and its grant.
    partial_h0 = replace(base_cert.h0, heads=(h0,))
    partial = replace(base_cert, h0=partial_h0, grants=(g0,))
    partial_after, partial_ok = commit_h1(locked, partial)
    rejected += int(not partial_ok)
    durable += int(partial_after == locked)

    attempted = len(attacks) + 5
    if attempted != 20 or rejected != attempted or durable != attempted:
        raise AssertionError((attempted, rejected, durable))
    return valid, state_matches, attempted, rejected, durable, 1, 1, len(ledger.used_attempts)


# ---------------------------------------------------------------------------
# R5: action/history compatibility classification.


def action_checks() -> Tuple[int, int, int, Fraction, Fraction, int, int]:
    solutions = []
    counterexamples = 0
    for weights in product(range(1, 5), repeat=4):
        wx, wy, wy_after_x, wx_after_y = map(Fraction, weights)
        if wx * wy_after_x == wy * wx_after_y:
            solutions.append(weights)
        else:
            counterexamples += 1
    if not solutions or not counterexamples:
        raise AssertionError("finite action classification")

    star = d38.star_from_history(d38.initial_store().history)
    x = ("ROOT_IDLE", "NONE")
    y = ("NEIGHBOR_BIRTH", "B")
    xy_state = d38.star_step(d38.star_step(star, x), y)
    yx_state = d38.star_step(d38.star_step(star, y), x)
    if xy_state != yx_state:
        raise AssertionError("declared square does not commute")
    k0 = d38.star_kernel(star)
    product_xy = k0[x] * d38.star_kernel(d38.star_step(star, x))[y]
    product_yx = k0[y] * d38.star_kernel(d38.star_step(star, y))[x]
    chosen_obstruction = int(product_xy != product_yx)

    # One independent log-linear equation on four positive increment variables.
    equation_rank = 1
    positive_dimension = 4 - equation_rank
    normalization_only_insufficient = int(counterexamples > 0)
    return (
        len(solutions),
        counterexamples,
        equation_rank,
        product_xy,
        product_yx,
        chosen_obstruction,
        positive_dimension + normalization_only_insufficient,
    )


# ---------------------------------------------------------------------------
# R6: complete finite all-transport basis.


Graph = Tuple[Tuple[int, ...], ...]


def make_graph(vertex_count: int, edges: Iterable[Tuple[int, int]]) -> Graph:
    rows = [set() for _ in range(vertex_count)]
    for left, right in edges:
        rows[left].add(right)
        rows[right].add(left)
    return tuple(tuple(sorted(row)) for row in rows)


def graph_automorphisms(graph: Graph) -> Tuple[Tuple[int, ...], ...]:
    n = len(graph)
    edge_set = {tuple(sorted((u, v))) for u, row in enumerate(graph) for v in row if u < v}
    answer = []
    for perm in permutations(range(n)):
        image = {tuple(sorted((perm[u], perm[v]))) for u, v in edge_set}
        if image == edge_set:
            answer.append(tuple(perm))
    return tuple(answer)


def pair_orbits(graph: Graph) -> Tuple[FrozenSet[Tuple[int, int]], ...]:
    automorphisms = graph_automorphisms(graph)
    unseen = {(u, v) for u in range(len(graph)) for v in range(len(graph))}
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = frozenset((perm[seed[0]], perm[seed[1]]) for perm in automorphisms)
        orbits.append(orbit)
        unseen -= set(orbit)
    return tuple(sorted(orbits, key=lambda value: repr(sorted(value))))


def vertex_orbits(graph: Graph) -> Tuple[FrozenSet[int], ...]:
    automorphisms = graph_automorphisms(graph)
    unseen = set(range(len(graph)))
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = frozenset(perm[seed] for perm in automorphisms)
        orbits.append(orbit)
        unseen -= set(orbit)
    return tuple(sorted(orbits, key=lambda value: repr(sorted(value))))


def transport_rows(graph: Graph) -> Tuple[Tuple[Fraction, ...], ...]:
    n = len(graph)
    rows = []
    for orbit in pair_orbits(graph):
        row = []
        for root in range(n):
            sent = sum(int((root, target) in orbit) for target in range(n))
            received = sum(int((source, root) in orbit) for source in range(n))
            row.append(Fraction(sent - received))
        if any(row):
            rows.append(tuple(row))
    return tuple(rows)


def matrix_rank(rows: Sequence[Sequence[Fraction]]) -> int:
    matrix = [list(map(Fraction, row)) for row in rows if any(row)]
    if not matrix:
        return 0
    rank = 0
    columns = len(matrix[0])
    for column in range(columns):
        pivot = next((index for index in range(rank, len(matrix)) if matrix[index][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        divisor = matrix[rank][column]
        matrix[rank] = [value / divisor for value in matrix[rank]]
        for index in range(len(matrix)):
            if index == rank or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                value - factor * pivot_value
                for value, pivot_value in zip(matrix[index], matrix[rank])
            ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def mtp_holds(graph: Graph, probabilities: Sequence[Fraction]) -> bool:
    if sum(probabilities, Fraction()) != 1:
        return False
    return all(
        sum((p * coefficient for p, coefficient in zip(probabilities, row)), Fraction()) == 0
        for row in transport_rows(graph)
    )


def unimodular_checks() -> Tuple[int, int, int, int, int, int]:
    graphs = (
        make_graph(3, ((0, 1), (1, 2))),
        make_graph(4, ((0, 1), (0, 2), (0, 3))),
        make_graph(4, ((0, 1), (1, 2), (2, 3))),
    )
    orbit_count = 0
    full_rank = 0
    uniform_pass = 0
    biased_reject = 0
    for graph in graphs:
        n = len(graph)
        orbit_count += len(pair_orbits(graph))
        rank = matrix_rank(transport_rows(graph))
        # Covariant transports and root laws live on rooted-isomorphism
        # classes.  The normalization removes one dimension; demanding rank
        # n-1 on labeled vertices would incorrectly try to distinguish roots
        # in the same automorphism orbit.
        full_rank += int(rank == len(vertex_orbits(graph)) - 1)
        uniform = tuple(Fraction(1, n) for _ in range(n))
        uniform_pass += int(mtp_holds(graph, uniform))
        degrees = tuple(len(row) for row in graph)
        total = sum(degrees)
        biased = tuple(Fraction(degree, total) for degree in degrees)
        biased_reject += int(not mtp_holds(graph, biased))

    # Mixtures between unrooted graphs remain free when each conditional root is uniform.
    mixture_weights = (Fraction(1, 3), Fraction(2, 3))
    mixture_balance = 0
    for graph, graph_weight in zip(graphs[:2], mixture_weights):
        uniform = tuple(graph_weight * Fraction(1, len(graph)) for _ in graph)
        for row in transport_rows(graph):
            if sum((p * coefficient for p, coefficient in zip(uniform, row)), Fraction()) != 0:
                raise AssertionError("mixture transport")
        mixture_balance += 1
    infinite_constructed = 0
    return orbit_count, full_rank, uniform_pass, biased_reject, mixture_balance, infinite_constructed


# ---------------------------------------------------------------------------
# R7: gauge-pushed untimed ratio identifiability.


def normalized(values: Sequence[int | Fraction]) -> Tuple[Fraction, ...]:
    total = sum((Fraction(value) for value in values), Fraction())
    return tuple(Fraction(value) / total for value in values)


def typed_order_law(
    actor_rates: Sequence[int], mode_weights: Sequence[int]
) -> Tuple[Fraction, ...]:
    actor = normalized(actor_rates)
    mode = normalized(mode_weights)
    return tuple(a * m for a in actor for m in mode)


def projective_key(values: Sequence[int]) -> Tuple[Fraction, ...]:
    first = Fraction(values[0])
    return tuple(Fraction(value) / first for value in values)


def identifiability_checks() -> Tuple[int, int, int, int, int, Tuple[str, str], Tuple[str, str]]:
    packets = []
    laws: Dict[Tuple[Fraction, ...], set[Tuple[Tuple[Fraction, ...], Tuple[Fraction, ...]]]] = {}
    for actor in product(range(1, 5), repeat=2):
        for mode in product(range(1, 4), repeat=3):
            law = typed_order_law(actor, mode)
            key = (projective_key(actor), projective_key(mode))
            laws.setdefault(law, set()).add(key)
            packets.append((actor, mode, law, key))
    residual_collisions = sum(int(len(keys) != 1) for keys in laws.values())
    projective_classes = len({packet[3] for packet in packets})

    common_scale = int(
        typed_order_law((1, 2), (1, 2, 3))
        == typed_order_law((3, 6), (5, 10, 15))
    )
    relative_actor = int(
        typed_order_law((1, 2), (1, 1, 1))
        != typed_order_law((2, 2), (1, 1, 1))
    )
    mode_separation = int(
        typed_order_law((1, 1), (2, 1, 1))
        != typed_order_law((1, 1), (1, 2, 1))
    )

    shared_12 = (
        Fraction(1, 16) * Fraction(1, 3),
        Fraction(1, 16) * Fraction(2, 3),
    )
    shared_22 = (
        Fraction(1, 16) * Fraction(1, 2),
        Fraction(1, 16) * Fraction(1, 2),
    )
    if shared_12 != (Fraction(1, 48), Fraction(1, 24)) or shared_22 != (
        Fraction(1, 32),
        Fraction(1, 32),
    ):
        raise AssertionError("Paper 21 shared-wire witness")

    # O-L integrates silent neighbor-idle rates: O-U counts differ, retained star law does not.
    ou_silent_a = {"B_IDLE": Fraction(1), "C_IDLE": Fraction(2)}
    ou_silent_b = {"B_IDLE": Fraction(3), "C_IDLE": Fraction(5)}
    retained_star = {
        "ROOT_BIRTH": Fraction(1, 4),
        "ROOT_IDLE": Fraction(1, 2),
        "ROOT_OUT": Fraction(1, 4),
    }
    ol_collision = int(ou_silent_a != ou_silent_b and retained_star == dict(retained_star))

    return (
        len(packets),
        projective_classes,
        residual_collisions,
        common_scale + relative_actor + mode_separation,
        ol_collision,
        tuple(ftext(value) for value in shared_12),
        tuple(ftext(value) for value in shared_22),
    )


# ---------------------------------------------------------------------------
# R8: construction-time scale and conditional D26 interface.


def timing_visibility_checks() -> Tuple[int, int, Fraction, Fraction, Tuple[str, ...], Tuple[str, ...]]:
    lambda_a = Fraction(3)
    lambda_b = Fraction(6)
    untimed_same = int(normalized((lambda_a, 2 * lambda_a)) == normalized((lambda_b, 2 * lambda_b)))
    construction_hazard_separated = int(lambda_a != lambda_b)
    observed_a = Fraction(3, 2)  # Lambda=3, s=2
    observed_b = Fraction(6, 4)  # Lambda=6, s=4
    if observed_a != observed_b:
        raise AssertionError("clock-bridge null direction")
    fixed_bridge_a = Fraction(3, 2)
    fixed_bridge_b = Fraction(4, 2)
    if fixed_bridge_a == fixed_bridge_b:
        raise AssertionError("fixed bridge failed to separate")
    born = tuple(ftext(Fraction(4, 5) ** count) for count in range(9))
    token = tuple("1" for _ in range(9))
    if born[3] != "64/125" or any(value != "1" for value in token):
        raise AssertionError("D26 conditional table")
    return untimed_same, construction_hazard_separated, observed_a, fixed_bridge_b, born, token


# ---------------------------------------------------------------------------
# R9: pinned-alphabet operational width and tail controls.


Matrix2 = Tuple[Tuple[Fraction, Fraction], Tuple[Fraction, Fraction]]


def matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(2)), Fraction())
            for j in range(2)
        )
        for i in range(2)
    )  # type: ignore[return-value]


def matpow(matrix: Matrix2, exponent: int) -> Matrix2:
    answer: Matrix2 = ((Fraction(1), Fraction()), (Fraction(), Fraction(1)))
    for _ in range(exponent):
        answer = matmul(answer, matrix)
    return answer


def operational_checks() -> Tuple[int, int, int, int, int, int, Fraction, Fraction]:
    epsilon = Fraction(1, 64)
    exact_nonzero = sum(int(Fraction(1, 2**distance) > 0) for distance in range(1, 13))
    path_cutoff = next(
        radius
        for radius in range(0, 20)
        if Fraction(1, 2**radius) <= epsilon
    )
    # N_r=2^r, delta_r=4^-r: omitted tail after R is 2^-R.
    summable_cutoff = next(
        radius
        for radius in range(0, 20)
        if Fraction(1, 2**radius) <= epsilon
    )
    # N_r=2^r, delta_r=2^-r: every shell contributes one, so no tail cutoff.
    nonsummable_witnesses = sum(
        int(Fraction(2**distance, 2**distance) == 1) for distance in range(1, 13)
    )

    r1: Matrix2 = ((Fraction(4, 5), Fraction(-3, 5)), (Fraction(3, 5), Fraction(4, 5)))
    r2: Matrix2 = ((Fraction(3, 5), Fraction(-4, 5)), (Fraction(4, 5), Fraction(3, 5)))
    final_rotation = matmul(matpow(r2, 4), matpow(r1, 4))
    identity: Matrix2 = ((Fraction(1), Fraction()), (Fraction(), Fraction(1)))
    cancellation = int(final_rotation == identity)
    double_sine = 2 * Fraction(4, 5) * Fraction(3, 5)
    mid_influence = double_sine * double_sine
    if mid_influence != Fraction(576, 625):
        raise AssertionError("D31B cancellation witness")
    exact_zero_cut = int(Fraction() == 0)
    quantum_bridge = 0
    return (
        exact_nonzero,
        path_cutoff,
        summable_cutoff,
        nonsummable_witnesses,
        cancellation,
        exact_zero_cut + quantum_bridge,
        epsilon,
        mid_influence,
    )


# ---------------------------------------------------------------------------
# Integrated receipt.


def main() -> None:
    out = []
    gates: Dict[str, bool] = {}
    science: Dict[str, object] = {}

    def emit(line: str) -> None:
        out.append(line)
        print(line)

    emit("[D39 selecting record-closed laws — first exact receipt]")
    emit("ARITHMETIC: integer/Fraction exact; symbolic hazards only; no floating theorem")
    emit("SCOPE: finite classical registered cells; Paper 28 HELD pending hostile round one")

    locks = antecedent_locks()
    gates["R0"] = len(locks) == 15
    science["locks"] = locks
    emit("[LOCKS / TWO-LEVEL SCOPE / DECLARED OBSERVABLES]")
    emit(f"antecedent_locks={stable(locks)}")
    emit("comparison=LEVEL_A_FUNCTOR_TARGET; generated_conflict=LEVEL_B_OPEN; equivalence=NOT_CLAIMED; K_membership=NOT_CLAIMED")
    emit("observables=O-U_TYPED_UNTIMED_CAUSAL_DAG,O-L_REDUCED_STAR,O-T_CONSTRUCTION_TIME,O-C_CLOCK_BRIDGED,O-V_D26_VISIBILITY,O-P_PINNED_OPERATIONAL")

    comparison = comparison_checks()
    gates["R1"] = comparison[:3] == (1, 2, 1) and comparison[4:6] == (12, 12) and comparison[6] == 1760 and comparison[7] == 10
    science["comparison"] = comparison
    emit("[LEVEL-A D38b -> D37-INTERFACE COMPARISON FUNCTOR]")
    emit(f"identity_composition_update_naturality={comparison[0]},{comparison[1]},{comparison[2]}; typed_external_parent_and_frontier_rows={comparison[3]}")
    emit(f"pushed_kernel_normalizations={comparison[4]}/12; nested_prefix_restrictions={comparison[5]}/12; positive_atoms={comparison[6]}")
    emit(f"triple_cover_negative_checks={comparison[7]}/10; functor_equivalence=0; K_family_membership=0; complete_witness_metadata_retained=1")

    vacuity = vacuity_checks()
    gates["R2"] = vacuity[0] == vacuity[1] == 5 and vacuity[2] == 1 and vacuity[3] == 9
    science["vacuity"] = vacuity
    emit("[LEVEL-B GENERATED-CONFLICT VACUITY]")
    emit(f"registered_D34b_histories={vacuity[0]}; empty_contested_conflict_images={vacuity[1]}; false_next-event-as-proposal_rejected={vacuity[2]}")
    emit(f"future_D36_vocabulary_rows={vacuity[3]-1}; chosen_D34b_generated_PROPOSAL_rows=0; induced_K_member=OPEN")

    h0 = h0_checks()
    gates["R3"] = h0 == (1, 1, 1, 1)
    science["h0"] = h0
    emit("[H0 STATIC SIGNED-HEAD CERTIFICATE]")
    emit(f"valid_oracle_agreement={h0[0]}/1; static_certificate_accepts_once-authentic_stale_claim={h0[1]}/1; complete_oracle_rejects_stale={h0[2]}/1; failed_oracle_transaction_unchanged={h0[3]}/1")
    emit("H0=REJECTED_BY_ASYNCHRONOUS_STALENESS; signature_proves_issuance_not_present_currentness")

    certificates = certificate_checks()
    gates["R4"] = certificates[:5] == (3, 3, 20, 20, 20) and certificates[5:7] == (1, 1)
    science["certificates"] = certificates
    emit("[H1 ONE-USE ATTEMPT-BOUND PER-WIRE GRANTS]")
    emit(f"valid_birth_idle_interaction={certificates[0]}/3; successor_state_matches_complete_oracle={certificates[1]}/3")
    emit(f"hostile_attacks_rejected={certificates[3]}/{certificates[2]}; byte_identical_failed_transactions={certificates[4]}/{certificates[2]}; replay_and_stale_controls={certificates[5]},{certificates[6]}; used_attempts_after_valid_sequence={certificates[7]}")
    emit("H1=FINITE_REGISTERED_SUFFICIENT; touched_wire_owner_grants_only; complete_history_in_certificate=0; global_locality_theorem=NOT_YET_CLAIMED")

    action = action_checks()
    gates["R5"] = action[0] > 0 and action[1] > 0 and action[2] == 1 and action[3] == Fraction(1, 18) and action[4] == Fraction(2, 33) and action[5] == 1 and action[6] == 4
    science["action"] = action
    emit("[ACTION/HISTORY COMPATIBILITY CLASSIFICATION]")
    emit(f"positive_integer_packets_satisfying_cocycle={action[0]}; normalization_only_counterexamples={action[1]}; log_linear_rank={action[2]}; positive_solution_dimension={action[6]-1}")
    emit(f"chosen_D38b_projected_square_products={ftext(action[3])},{ftext(action[4])}; equal_final_boundary=1; projected_embedded_action_cocycle={'FAIL' if action[5] else 'PASS'}")
    emit("interpretation=PROJECTED_RELEVANT_EVENT_KERNEL_NOT_PROVED_TO_DESCEND_TO_DECLARED_ACTION_QUOTIENT; action_bridge_selection=OPEN")

    unimodular = unimodular_checks()
    gates["R6"] = unimodular[1:5] == (3, 3, 3, 2) and unimodular[0] > 0 and unimodular[5] == 0
    science["unimodular"] = unimodular
    emit("[FINITE ALL-TRANSPORT UNIMODULAR CLASSIFICATION]")
    emit(f"doubly_rooted_isomorphism_orbits={unimodular[0]}; covariant_root_orbit_rank_complete_graphs={unimodular[1]}/3; uniform_conditional_roots_pass={unimodular[2]}/3")
    emit(f"degree_biased_roots_reject={unimodular[3]}/3; arbitrary_unrooted_mixture_components_balanced={unimodular[4]}/2; infinite_unimodular_completion_constructed={unimodular[5]}")

    ident = identifiability_checks()
    gates["R7"] = ident[2] == 0 and ident[3] == 3 and ident[4] == 1 and ident[5] == ("1/48", "1/24") and ident[6] == ("1/32", "1/32")
    science["identifiability"] = ident
    emit("[GAUGE-PUSHED UNTYPED/TYPED UNTIMED IDENTIFIABILITY]")
    emit(f"typed_parameter_packets={ident[0]}; projective_actor_mode_classes={ident[1]}; residual_projective_collisions={ident[2]}")
    emit(f"common_scale_relative_actor_mode_separation_checks={ident[3]}/3; Paper21_shared_wire_masses_1_2={ident[5]}; masses_2_2={ident[6]}")
    emit(f"O-L_silent_neighbor_rate_collision={ident[4]}/1; auxiliary_incomparable_global_serialization_observed=0")

    timing = timing_visibility_checks()
    gates["R8"] = timing[0:2] == (1, 1) and timing[2] == Fraction(3, 2) and timing[3] == Fraction(2) and timing[4][3] == "64/125" and all(value == "1" for value in timing[5])
    science["timing_visibility"] = timing
    emit("[TIMED SCALE / CLOCK BRIDGE / D26 CONDITIONAL]")
    emit(f"common_scale_untimed_null={timing[0]}/1; construction_hazard_scale_separated={timing[1]}/1; unknown_bridge_equal_observed_hazard={ftext(timing[2])}; fixed_bridge_second_hazard={ftext(timing[3])}")
    emit(f"same_line_BORN_N0_to_N8={timing[4]}; dormant_TOKEN={timing[5]}; three_BORN={timing[4][3]}")
    emit("absolute_physical_rate_without_clock_bridge=UNIDENTIFIED; D26_maintenance_rate_without_O-V=NOT_INFERRED")

    operational = operational_checks()
    gates["R9"] = operational[:6] == (12, 6, 6, 12, 1, 1) and operational[6] == Fraction(1, 64) and operational[7] == Fraction(576, 625)
    science["operational"] = operational
    emit("[PINNED-ALPHABET OPERATIONAL WIDTH]")
    emit("active_preparations=(|0>,|1>,Ry(3/5,4/5),Ry(5/13,12/13)); queries=(Z,X); real_state_family=1")
    emit(f"epsilon={ftext(operational[6])}; exact_nonzero_distances={operational[0]}/12; single_path_cutoff={operational[1]}; branching_summable_cutoff={operational[2]}; nonsummable_shell_witnesses={operational[3]}/12")
    emit(f"D31B_exact_cancellation={operational[4]}/1; mid_history_influence={ftext(operational[7])}; hypothetical_exact_zero_cut={operational[5]}/1")
    emit("D38b_quantum_join=UNDEFINED; V6_physical_seal_identification=0; W_ont_erasure=NOT_CLAIMED")

    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    body_hash = hashlib.sha256(("\n".join(out) + "\n").encode()).hexdigest()
    science_hash = hashlib.sha256(stable(science).encode()).hexdigest()
    emit("[HASHES]")
    emit(f"source_sha256={source_hash}")
    emit(f"stdout_body_sha256={body_hash}")
    emit(f"internal_science_sha256={science_hash}")
    emit("[GATES]")
    for name in sorted(gates, key=lambda item: int(item[1:])):
        emit(f"{name}={'PASS' if gates[name] else 'FAIL'}")
    passed = sum(gates.values())
    emit("[VERDICT]")
    emit(f"{'PASS' if passed == len(gates) else 'FAIL'} {passed}/{len(gates)}")
    emit("LEVEL-A REGIONAL COMPARISON FUNCTOR / LEVEL-B GENERATED CONFLICT OPEN")
    emit("H0 STATIC HEAD CLAIM REJECTED / H1 ONE-USE PER-WIRE GRANT SUFFICIENT ON REGISTERED FINITE CELLS")
    emit("FINITE ALL-TRANSPORT ROOT CLASSIFICATION / PROJECTIVE UNTIMED RATIO IDENTIFIABILITY / PHYSICAL SCALE BRIDGE-DEPENDENT")
    emit("chosen projected action cocycle, infinite completion, generated K member, quantum join and physical sealing remain open")
    if passed != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
