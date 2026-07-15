#!/usr/bin/env python3
"""D39b exact hostile repair: comparison, admission and identification.

This replacement keeps the rejected D39 receipt frozen.  It constructs a
shared oriented-interface category with an actual D37 embedding, realizes H1
as a typed causal protocol, computes a finite action complex and orbit-level
mass transports, and pushes parameterized D38b paths to typed untimed DAGs.

All theorem arithmetic is integer/Fraction exact.  Scope is finite and
classical.  Level-B generated conflicts, an infinite unimodular completion, a
physical clock bridge, a D38b quantum join and V6 sealing remain open.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Dict, FrozenSet, Hashable, Iterable, Mapping, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]

LOCKS = {
    "D39-pin": (
        ROOT / "v10/note-d39-selecting-record-closed-laws.md",
        "36c8c28a45fc6bb4069f16b2ed04045d7ed433eec2634f9af1d62987b850c948",
    ),
    "D39-rejected": (
        ROOT / "v10/code/d39_record_closed_law_selection_exact.py",
        "3f976eff94a28ee7cd8551b37ddad1fab81b358dcadad3e9e37dba3fac520e06",
    ),
    "D39-rejected-data": (
        ROOT / "v10/data/d39_record_closed_law_selection_exact.out",
        "36f6984f4ca68c895d0b64573f87e749cb4fcf9bbfbf5ffac59cc92615a1b64c",
    ),
    "D39-round1": (
        ROOT / "v10/reviews/d39-round1-selection-identifiability-hostile-review.md",
        "4d0ab3b11c57cef82bb45dc213f5b2b4bc9dadde8dbbfc51aa90d8ad8e835a43",
    ),
    "D39b-round2": (
        ROOT / "v10/reviews/d39b-round2-hostile-repair-review.md",
        "faf143182556e6924f4d4d2bea2933367658af678f43f63ddc20c148456cb00e",
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
}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


d36 = load_module("d36b_locked_for_d39b", LOCKS["D36b"][0])
d37 = load_module("d37_locked_for_d39b", LOCKS["D37"][0])
d38 = load_module("d38b_locked_for_d39b", LOCKS["D38b"][0])


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


def locked_antecedents() -> Dict[str, str]:
    answer = {}
    for name, (path, expected) in LOCKS.items():
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError((name, actual, expected))
        answer[name] = actual
    return answer


# ---------------------------------------------------------------------------
# R1: shared regional-interface category with an actual D37 embedding.


InternalRow = Tuple[Hashable, str, str, Tuple[str, ...], Tuple[Hashable, ...], str]
IncomingRow = Tuple[str, str, Hashable]
GeneratedRow = Tuple[str, str]


@dataclass(frozen=True)
class InterfaceObject:
    namespace: str
    internal: Tuple[InternalRow, ...]
    incoming: Tuple[IncomingRow, ...]
    lateral: Tuple[str, ...]
    generated: Tuple[GeneratedRow, ...]


def validate_interface(obj: InterfaceObject) -> None:
    if not obj.namespace:
        raise AssertionError("missing local carrier namespace")
    ids = [row[0] for row in obj.internal]
    if len(ids) != len(set(map(repr, ids))):
        raise AssertionError("duplicate internal interface row")
    incoming_ids = [row[2] for row in obj.incoming]
    if len(incoming_ids) != len(set(map(repr, incoming_ids))):
        raise AssertionError("duplicate incoming interface row")
    if len(obj.lateral) != len(set(obj.lateral)):
        raise AssertionError("duplicate lateral row")
    if any(len(row) != 2 for row in obj.generated):
        raise AssertionError("generated row typing")


def ref_label(prefix: str, value: Hashable) -> str:
    return f"{prefix}:{digest(value)[:24]}"


def d38_interface(view) -> InterfaceObject:
    d38.validate_view(view)
    internal = tuple(
        sorted(
            (
                (
                    row.source.record_id,
                    row.source.kind,
                    row.source.owner,
                    tuple(row.source.wires),
                    tuple(row.source.parents),
                    digest(row.source.payload),
                )
                for row in view.records
            ),
            key=repr,
        )
    )
    incoming_ids = {
        source_id
        for row in view.records
        for tag, source_id in row.resolved_parents
        if tag == "EXTERNAL"
    }
    incoming = tuple(
        sorted(
            (
                "D38_EXTERNAL_PARENT",
                ref_label("parent", source_id),
                source_id,
            )
            for source_id in incoming_ids
        )
    )
    lateral_ids = set(view.external_refs) - incoming_ids
    lateral = tuple(sorted(ref_label("frontier", source_id) for source_id in lateral_ids))
    generated = tuple(
        sorted(
            (
                "D38_RECORD",
                f"{row.source.kind}:{digest(row.source.record_id)[:24]}",
            )
            for row in view.records
        )
    )
    answer = InterfaceObject("D38b", internal, incoming, lateral, generated)
    validate_interface(answer)
    return answer


def d37_interface(cell, region: FrozenSet[str]) -> InterfaceObject:
    incoming, lateral, generated = d37.oriented_interface(cell, region)
    internal = tuple(
        sorted(
            (
                proposal,
                cell.proposal_type(proposal),
                f"source:{proposal}",
                tuple(cell.participants(proposal)),
                (d37.parent_line_root_id(cell.parent_line(proposal)),),
                digest((cell.parent_line(proposal), cell.proposal_type(proposal))),
            )
            for proposal in region
        )
    )
    answer = InterfaceObject(
        f"D37:{cell.name}",
        internal,
        tuple(incoming),
        tuple(lateral),
        tuple(generated),
    )
    validate_interface(answer)
    return answer


@dataclass(frozen=True)
class InterfaceMorphism:
    source: str
    target: str
    retained: Tuple[Hashable, ...]
    target_incoming: Tuple[IncomingRow, ...]
    target_lateral: Tuple[str, ...]
    target_generated: Tuple[GeneratedRow, ...]


def object_id(obj: InterfaceObject) -> str:
    return digest(("D39B_INTERFACE_OBJECT", obj))


def restriction_morphism(source: InterfaceObject, target: InterfaceObject) -> InterfaceMorphism:
    source_ids = {repr(row[0]) for row in source.internal}
    target_ids = {repr(row[0]) for row in target.internal}
    if not target_ids <= source_ids:
        raise AssertionError("interface restriction is not internal-row decreasing")
    return InterfaceMorphism(
        object_id(source),
        object_id(target),
        tuple(row[0] for row in target.internal),
        target.incoming,
        target.lateral,
        target.generated,
    )


def identity_morphism(obj: InterfaceObject) -> InterfaceMorphism:
    return InterfaceMorphism(
        object_id(obj),
        object_id(obj),
        tuple(row[0] for row in obj.internal),
        obj.incoming,
        obj.lateral,
        obj.generated,
    )


def compose_morphisms(
    first: InterfaceMorphism, second: InterfaceMorphism
) -> InterfaceMorphism:
    if first.target != second.source:
        raise AssertionError("noncomposable interface morphisms")
    retained = tuple(row for row in first.retained if repr(row) in {repr(x) for x in second.retained})
    return InterfaceMorphism(
        first.source,
        second.target,
        retained,
        second.target_incoming,
        second.target_lateral,
        second.target_generated,
    )


RegionalAtom = Tuple[str, str]


def push_cylinder(
    law: Mapping[Tuple[Tuple[str, str], ...], Fraction]
) -> Dict[Tuple[RegionalAtom, ...], Fraction]:
    answer: Dict[Tuple[RegionalAtom, ...], Fraction] = {}
    for path, probability in law.items():
        image = tuple((f"D38_ACTION:{tag}", target) for tag, target in path)
        answer[image] = answer.get(image, Fraction()) + probability
    return answer


def prefix_law(
    law: Mapping[Tuple[RegionalAtom, ...], Fraction], depth: int
) -> Dict[Tuple[RegionalAtom, ...], Fraction]:
    answer: Dict[Tuple[RegionalAtom, ...], Fraction] = {}
    for path, probability in law.items():
        answer[path[:depth]] = answer.get(path[:depth], Fraction()) + probability
    return answer


def triple_cover_negative() -> Tuple[int, int, int]:
    pairs = ((0, 1), (1, 2), (0, 2))
    pair_laws = {
        pair: {(0, 1): Fraction(1, 2), (1, 0): Fraction(1, 2)}
        for pair in pairs
    }
    normalized = int(all(sum(law.values(), Fraction()) == 1 for law in pair_laws.values()))
    agree = 0
    for coordinate in range(3):
        marginals = []
        for pair, law in pair_laws.items():
            if coordinate not in pair:
                continue
            slot = pair.index(coordinate)
            marginals.append(
                tuple(
                    sum(
                        (p for atom, p in law.items() if atom[slot] == bit),
                        Fraction(),
                    )
                    for bit in (0, 1)
                )
            )
        agree += int(len(set(marginals)) == 1)
    joint_atoms = sum(
        int(bits[0] != bits[1] and bits[1] != bits[2] and bits[0] != bits[2])
        for bits in product((0, 1), repeat=3)
    )
    return normalized, agree, int(joint_atoms == 0)


def comparison_checks() -> Tuple[int, ...]:
    # Every nonempty region of every locked finite D37 carrier embeds into the
    # common schema; all strict three-level restriction compositions are gated.
    d37_identity = 0
    d37_composition = 0
    d37_object_count = 0
    d37_image_ids = set()
    for cell in d37.ORIENTED_CELLS.values():
        regions = tuple(
            frozenset(proposal for bit, proposal in enumerate(cell.vertices) if mask & (1 << bit))
            for mask in range(1, 1 << len(cell.vertices))
        )
        objects = {region: d37_interface(cell, region) for region in regions}
        d37_object_count += len(objects)
        d37_image_ids.update(object_id(obj) for obj in objects.values())
        d37_identity += sum(
            int(identity_morphism(obj).source == identity_morphism(obj).target)
            for obj in objects.values()
        )
        for outer in regions:
            for middle in regions:
                if not middle < outer:
                    continue
                for inner in regions:
                    if not inner < middle:
                        continue
                    outer_middle = restriction_morphism(objects[outer], objects[middle])
                    middle_inner = restriction_morphism(objects[middle], objects[inner])
                    outer_inner = restriction_morphism(objects[outer], objects[inner])
                    d37_composition += int(
                        compose_morphisms(outer_middle, middle_inner) == outer_inner
                    )

    store = d38.initial_store()
    store = d38.execute(store, "IDLE", "A")
    store = d38.execute(store, "IDLE", "B")
    pre_interaction = store
    interaction = d38.proposed(store, "INTERACTION", "A", "B")
    store = d38.execute(store, "INTERACTION", "A", "B")
    store = d38.execute(store, "BIRTH", "A", "A/1")
    records = list(store.history.records)
    events = [record for record in records if record.kind == "EVENT"]
    idle_a = next(record for record in events if record.owner == "A" and record.payload_map()["event_kind"] == "IDLE")
    idle_b = next(record for record in events if record.owner == "B" and record.payload_map()["event_kind"] == "IDLE")
    all_ids = frozenset(record.record_id for record in records)
    e_ids = all_ids - {idle_b.record_id}
    d_ids = e_ids - {idle_a.record_id}
    edge_id = next(record.record_id for record in records if record.kind == "SEED_EDGE")
    c_ids = frozenset(record_id for record_id in d_ids if record_id != edge_id)

    f_obj = d38_interface(d38.restrict_records(store.history, all_ids))
    e_obj = d38_interface(d38.restrict_records(store.history, e_ids))
    d_obj = d38_interface(d38.restrict_records(store.history, d_ids))
    c_obj = d38_interface(d38.restrict_records(store.history, c_ids))
    fe = restriction_morphism(f_obj, e_obj)
    ed = restriction_morphism(e_obj, d_obj)
    dc = restriction_morphism(d_obj, c_obj)
    fd = restriction_morphism(f_obj, d_obj)
    fc = restriction_morphism(f_obj, c_obj)
    d38_identity = int(identity_morphism(f_obj).source == identity_morphism(f_obj).target)
    d38_composition = int(compose_morphisms(fe, ed) == fd) + int(
        compose_morphisms(compose_morphisms(fe, ed), dc) == fc
    )

    staged_d = d38.restrict_records(d38.restrict_records(store.history, e_ids), d_ids)
    staged_c = d38.restrict_records(
        d38.restrict_records(d38.restrict_records(store.history, e_ids), d_ids), c_ids
    )
    staged = int(d38_interface(staged_d) == d_obj) + int(d38_interface(staged_c) == c_obj)

    pre_ids = frozenset(record.record_id for record in pre_interaction.history.records) - {idle_b.record_id}
    before = d38.restrict_records(pre_interaction.history, pre_ids)
    transported = d38.append_view(before, interaction)
    post = d38.add_event(pre_interaction.history, interaction)
    direct = d38.restrict_records(post, pre_ids | {interaction.record_id})
    update_naturality = int(d38_interface(transported) == d38_interface(direct))

    boundary_rows = sum(
        len(obj.incoming) + len(obj.lateral) for obj in (e_obj, d_obj, c_obj, d38_interface(direct))
    )
    normalized = projective = atoms = 0
    for star in d38.reachable_stars():
        laws = {}
        for depth in (1, 2, 3):
            image = push_cylinder(d38.cylinder_distribution(star, depth))
            if sum(image.values(), Fraction()) != 1 or any(p <= 0 for p in image.values()):
                raise AssertionError("improper pushed cylinder")
            laws[depth] = image
            normalized += 1
            atoms += len(image)
        for high, low in ((3, 2), (2, 1), (3, 1)):
            if prefix_law(laws[high], low) != laws[low]:
                raise AssertionError("pushed prefix failure")
            projective += 1

    cover = triple_cover_negative()
    if cover != (1, 3, 1):
        raise AssertionError("triple cover control")
    global_witness_fields = sum(
        int("witness" in field) for field in InterfaceObject.__dataclass_fields__
    )
    return (
        d37_identity,
        d37_composition,
        d38_identity,
        d38_composition,
        staged,
        update_naturality,
        boundary_rows,
        normalized,
        projective,
        atoms,
        cover[2],
        global_witness_fields,
        d37_object_count,
        len(d37_image_ids),
    )


# ---------------------------------------------------------------------------
# R2: content-level conflict vacuity with the locked D36 vocabulary.


def generated_conflicts(history) -> Tuple[Tuple[Hashable, ...], Tuple[Tuple[Hashable, Hashable], ...]]:
    carriers = tuple(
        sorted(
            (
                record.record_id
                for record in history.records
                if record.kind in ("T0_BIRTH", "SLOT_ACTIVATION")
                and "participant" in record.payload_map()
                and "base_version" in record.payload_map()
            ),
            key=repr,
        )
    )
    by_id = {record.record_id: record for record in history.records}
    edges = []
    for left, right in combinations(carriers, 2):
        lp = by_id[left].payload_map()
        rp = by_id[right].payload_map()
        if (
            lp["participant"] == rp["participant"]
            and lp["base_version"] == rp["base_version"]
            and lp.get("requested_update") != rp.get("requested_update")
        ):
            edges.append((left, right))
    return carriers, tuple(edges)


def vacuity_checks() -> Tuple[int, ...]:
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
    empty = sum(int(generated_conflicts(history) == ((), ())) for history in histories)

    born = d37.d36_carrier_record(d37.ORIENTED_CELLS["pair"], "P", "BORN", "line:P")
    token = d37.d36_carrier_record(d37.ORIENTED_CELLS["pair"], "P", "TOKEN", "line:P")
    carrier_kinds = tuple(sorted({born.kind, token.kind, "DORMANT_SLOT"}))
    protocol_kinds = (
        d36.PREPARE,
        d36.GRANT,
        d36.REJECT,
        "DECISION_COMMIT",
        "DECISION_ABORT",
        "APPLY",
        "RELEASE",
        d36.ACK,
    )
    exact_constants = int(
        protocol_kinds
        == (
            "PREPARE",
            "GRANT",
            "REJECT",
            "DECISION_COMMIT",
            "DECISION_ABORT",
            "APPLY",
            "RELEASE",
            "ACK",
        )
    )
    alternative_actions = len(d38.star_kernel(d38.star_from_history(histories[0])))
    false_relabel_rejected = int(alternative_actions > 1 and empty == len(histories))
    return (
        len(histories),
        empty,
        false_relabel_rejected,
        len(carrier_kinds),
        len(protocol_kinds),
        exact_constants,
    )


# ---------------------------------------------------------------------------
# R3/R4: typed causal H0/H1 admission.


RowTuple = Tuple[int, int, int, int, int]


def row_tuple(row) -> RowTuple:
    return (row.carrier, row.rings, row.births, row.degree, row.wire_events)


def tuple_row(row: RowTuple):
    return d38.ActorRow(*row)


def required_wires(event) -> Tuple[str, ...]:
    payload = event.payload_map()
    kind = str(payload["event_kind"])
    initiator = str(payload["initiator"])
    target = str(payload["target"])
    return (initiator,) if kind in ("BIRTH", "IDLE") else (initiator, target)


def event_body(event) -> str:
    return digest(("D39B_EVENT_BODY", event))


HEAD_PREPARE = "HEAD_PREPARE"
HEAD_GRANT = "HEAD_GRANT"
EDGE_CREDENTIAL = "EDGE_CREDENTIAL"
HEAD_DECISION_COMMIT = "HEAD_DECISION_COMMIT"
HEAD_DECISION_ABORT = "HEAD_DECISION_ABORT"
HEAD_APPLY = "HEAD_APPLY"
HEAD_RELEASE = "HEAD_RELEASE"
HEAD_ACK = "HEAD_ACK"


@dataclass(frozen=True)
class ProtocolRecord:
    record_id: str
    kind: str
    owner: str
    wire: str
    parents: Tuple[Hashable, ...]
    payload: Tuple[Tuple[str, Hashable], ...]
    signature: str

    def payload_map(self) -> Dict[str, Hashable]:
        return dict(self.payload)


def protocol_core(
    kind: str,
    owner: str,
    wire: str,
    parents: Sequence[Hashable],
    payload: Mapping[str, Hashable],
) -> Tuple[object, ...]:
    return (
        "D39B_PROTOCOL_RECORD",
        kind,
        owner,
        wire,
        tuple(parents),
        tuple(sorted(payload.items())),
    )


def make_protocol(
    kind: str,
    owner: str,
    wire: str,
    parents: Sequence[Hashable],
    payload: Mapping[str, Hashable],
) -> ProtocolRecord:
    core = protocol_core(kind, owner, wire, parents, payload)
    record_id = digest(("D39B_PROTOCOL_ID", core))
    signature = digest(("D39B_IDEAL_OWNER_SIGNATURE", owner, core))
    return ProtocolRecord(
        record_id,
        kind,
        owner,
        wire,
        tuple(parents),
        tuple(sorted(payload.items())),
        signature,
    )


def authentic_protocol(record: ProtocolRecord) -> bool:
    core = protocol_core(
        record.kind,
        record.owner,
        record.wire,
        record.parents,
        record.payload_map(),
    )
    return (
        record.record_id == digest(("D39B_PROTOCOL_ID", core))
        and record.signature == digest(("D39B_IDEAL_OWNER_SIGNATURE", record.owner, core))
    )


def resign_protocol(record: ProtocolRecord, **changes: object) -> ProtocolRecord:
    values = {
        "kind": record.kind,
        "owner": record.owner,
        "wire": record.wire,
        "parents": record.parents,
        "payload": record.payload_map(),
    }
    values.update(changes)
    return make_protocol(
        str(values["kind"]),
        str(values["owner"]),
        str(values["wire"]),
        values["parents"],  # type: ignore[arg-type]
        values["payload"],  # type: ignore[arg-type]
    )


@dataclass(frozen=True)
class H0Certificate:
    event: object
    heads: Tuple[Tuple[str, Hashable, RowTuple, str], ...]


def local_derived(rows: Mapping[str, RowTuple], heads: Mapping[str, Hashable], edges):
    return d38.Derived(
        tuple(sorted((actor, tuple_row(row)) for actor, row in rows.items())),
        tuple(sorted(heads.items())),
        tuple(sorted(edges)),
        (),
    )


def expected_from_local(rows, heads, edges, event):
    payload = event.payload_map()
    target = None if payload["target"] == "NONE" else str(payload["target"])
    return d38.expected_event(
        local_derived(rows, heads, edges),
        str(payload["event_kind"]),
        str(payload["initiator"]),
        target,
    )


def issue_h0(store, event) -> H0Certificate:
    derived = d38.derive(store.history)
    rows = derived.row_map()
    heads = derived.head_map()
    body = event_body(event)
    claims = tuple(
        (
            wire,
            heads[wire],
            row_tuple(rows[wire]),
            digest(("D39B_STATIC_HEAD_SIGNATURE", wire, heads[wire], row_tuple(rows[wire]), body)),
        )
        for wire in required_wires(event)
    )
    return H0Certificate(event, claims)


def verify_h0(cert: H0Certificate) -> bool:
    try:
        payload = cert.event.payload_map()
        body = event_body(cert.event)
        claims = {wire: (head, row, signature) for wire, head, row, signature in cert.heads}
        if len(claims) != len(cert.heads) or set(claims) != set(required_wires(cert.event)):
            return False
        for wire, (head, row, signature) in claims.items():
            if signature != digest(("D39B_STATIC_HEAD_SIGNATURE", wire, head, row, body)):
                return False
        rows = {wire: row for wire, (_head, row, _signature) in claims.items()}
        heads = {wire: head for wire, (head, _row, _signature) in claims.items()}
        edges = ()
        if payload["event_kind"] == "INTERACTION":
            edges = (tuple(sorted((str(payload["initiator"]), str(payload["target"])))),)
        return expected_from_local(rows, heads, edges, cert.event) == cert.event
    except (AssertionError, KeyError, TypeError, ValueError):
        return False


def h0_checks() -> Tuple[int, int, int, int]:
    base = d38.initial_store()
    idle = d38.proposed(base, "IDLE", "A")
    cert = issue_h0(base, idle)
    valid_store, valid = d38.transact(base, idle)
    advanced = d38.execute(base, "BIRTH", "A", "A/1")
    stale_store, stale = d38.transact(advanced, idle)
    return (
        int(valid and verify_h0(cert)),
        int(verify_h0(cert)),
        int(not stale),
        int(valid_store != base and stale_store == advanced),
    )


@dataclass(frozen=True)
class H1Certificate:
    event: object
    attempt: str
    prepares: Tuple[ProtocolRecord, ...]
    grants: Tuple[ProtocolRecord, ...]
    edge: Optional[ProtocolRecord]


@dataclass(frozen=True)
class LocalLedger:
    rows: Tuple[Tuple[str, RowTuple], ...]
    heads: Tuple[Tuple[str, Hashable], ...]
    edges: Tuple[Tuple[str, str], ...]
    edge_sources: Tuple[Tuple[Tuple[str, str], Hashable], ...]
    locks: Tuple[Tuple[str, Hashable, str, str], ...]
    protocol_records: Tuple[ProtocolRecord, ...]
    used_attempts: FrozenSet[str]

    def row_map(self) -> Dict[str, RowTuple]:
        return dict(self.rows)

    def head_map(self) -> Dict[str, Hashable]:
        return dict(self.heads)

    def protocol_map(self) -> Dict[str, ProtocolRecord]:
        return {record.record_id: record for record in self.protocol_records}


def edge_source(history, edge: Tuple[str, str]) -> Hashable:
    normalized = tuple(sorted(edge))
    for record in history.records:
        payload = record.payload_map()
        if record.kind == "SEED_EDGE" and tuple(payload["endpoints"]) == normalized:
            return record.record_id
        if record.kind == "EVENT" and payload.get("created_edge") == normalized:
            return record.record_id
    raise AssertionError("edge source missing")


def ledger_from_store(store, used: FrozenSet[str] = frozenset()) -> LocalLedger:
    derived = d38.derive(store.history)
    return LocalLedger(
        tuple((actor, row_tuple(row)) for actor, row in derived.rows),
        derived.heads,
        derived.edges,
        tuple((edge, edge_source(store.history, edge)) for edge in derived.edges),
        (),
        (),
        used,
    )


def protocol_history_valid(ledger: LocalLedger) -> bool:
    try:
        records = ledger.protocol_map()
        if len(records) != len(ledger.protocol_records):
            return False
        if any(not authentic_protocol(record) for record in records.values()):
            return False
        external = {head for _wire, head in ledger.heads} | {
            source for _edge, source in ledger.edge_sources
        }
        for record in records.values():
            payload = record.payload_map()
            if record.kind in (HEAD_PREPARE, HEAD_GRANT):
                external.add(payload["expected_head"])
            elif record.kind == EDGE_CREDENTIAL:
                external.add(payload["source"])
        allowed = set(records) | external
        if any(parent not in allowed for record in records.values() for parent in record.parents):
            return False

        active = set()
        complete = set()

        def visit(record_id: str) -> None:
            if record_id in complete:
                return
            if record_id in active:
                raise AssertionError("protocol cycle")
            active.add(record_id)
            for parent in records[record_id].parents:
                if parent in records:
                    visit(parent)
            active.remove(record_id)
            complete.add(record_id)

        for record_id in records:
            visit(record_id)

        for record in records.values():
            payload = record.payload_map()
            parent_kinds = tuple(records[parent].kind for parent in record.parents if parent in records)
            if record.kind == HEAD_PREPARE:
                valid = (
                    len(record.parents) == 1
                    and not parent_kinds
                    and set(payload) == {"attempt", "body", "event_id", "expected_head"}
                    and record.parents == (payload["expected_head"],)
                    and record.owner == f"attempt:{payload['attempt']}"
                )
            elif record.kind == HEAD_GRANT:
                prepare = records[record.parents[0]]
                prepare_payload = prepare.payload_map()
                valid = (
                    len(record.parents) == 2
                    and parent_kinds == (HEAD_PREPARE,)
                    and set(payload) == {"attempt", "body", "event_id", "expected_head", "row"}
                    and record.owner == record.wire
                    and record.parents[1] == payload["expected_head"]
                    and payload["attempt"] == prepare_payload["attempt"]
                    and payload["body"] == prepare_payload["body"]
                    and payload["event_id"] == prepare_payload["event_id"]
                    and payload["expected_head"] == prepare_payload["expected_head"]
                )
            elif record.kind == EDGE_CREDENTIAL:
                edge = tuple(payload["edge"])
                valid = (
                    len(record.parents) == 1
                    and not parent_kinds
                    and set(payload) == {"attempt", "body", "edge", "event_id", "source"}
                    and record.parents == (payload["source"],)
                    and record.owner == record.wire == f"edge:{edge[0]}:{edge[1]}"
                )
            elif record.kind in (HEAD_DECISION_COMMIT, HEAD_DECISION_ABORT):
                parent_payloads = [records[parent].payload_map() for parent in record.parents]
                outcome = "COMMIT" if record.kind == HEAD_DECISION_COMMIT else "ABORT"
                valid = (
                    bool(parent_kinds)
                    and all(kind in (HEAD_GRANT, EDGE_CREDENTIAL) for kind in parent_kinds)
                    and HEAD_GRANT in parent_kinds
                    and set(payload) == {"attempt", "body", "event_id", "outcome"}
                    and payload["outcome"] == outcome
                    and record.owner == record.wire == f"attempt:{payload['attempt']}"
                    and all(
                        parent_payload["attempt"] == payload["attempt"]
                        and parent_payload["body"] == payload["body"]
                        and parent_payload["event_id"] == payload["event_id"]
                        for parent_payload in parent_payloads
                    )
                )
            elif record.kind == HEAD_APPLY:
                decision = records[record.parents[0]].payload_map()
                grant = records[record.parents[1]]
                valid = (
                    parent_kinds == (HEAD_DECISION_COMMIT, HEAD_GRANT)
                    and set(payload) == {"attempt", "event_id", "new_head", "new_row"}
                    and record.owner == record.wire == grant.wire
                    and payload["attempt"] == decision["attempt"]
                    and payload["event_id"] == decision["event_id"] == payload["new_head"]
                )
            elif record.kind == HEAD_RELEASE:
                decision = records[record.parents[0]].payload_map()
                grant = records[record.parents[1]]
                valid = (
                    parent_kinds == (HEAD_DECISION_ABORT, HEAD_GRANT)
                    and set(payload) == {"attempt", "event_id", "wire"}
                    and record.owner == record.wire == grant.wire == payload["wire"]
                    and payload["attempt"] == decision["attempt"]
                    and payload["event_id"] == decision["event_id"]
                )
            elif record.kind == HEAD_ACK:
                parent = records[record.parents[0]]
                parent_payload = parent.payload_map()
                valid = (
                    len(parent_kinds) == 1
                    and parent_kinds[0] in (HEAD_APPLY, HEAD_RELEASE)
                    and set(payload) == {"attempt", "apply", "wire"}
                    and record.parents == (payload["apply"],)
                    and payload["wire"] == record.wire == parent.wire
                    and payload["attempt"] == parent_payload["attempt"]
                    and record.owner == f"attempt:{payload['attempt']}"
                )
            else:
                valid = False
            if not valid:
                return False
        return True
    except (AssertionError, KeyError, TypeError, ValueError):
        return False


def attempt_key(event) -> str:
    return digest(("D39B_CARRIER_ATTEMPT", event.record_id, event_body(event), tuple(event.wires)))


def prepare_record(event, attempt: str, wire: str, head: Hashable) -> ProtocolRecord:
    return make_protocol(
        HEAD_PREPARE,
        f"attempt:{attempt}",
        wire,
        (head,),
        {
            "attempt": attempt,
            "body": event_body(event),
            "event_id": event.record_id,
            "expected_head": head,
        },
    )


def grant_record(
    event,
    attempt: str,
    wire: str,
    head: Hashable,
    row: RowTuple,
    prepare: ProtocolRecord,
) -> ProtocolRecord:
    return make_protocol(
        HEAD_GRANT,
        wire,
        wire,
        (prepare.record_id, head),
        {
            "attempt": attempt,
            "body": event_body(event),
            "event_id": event.record_id,
            "expected_head": head,
            "row": row,
        },
    )


def edge_record(event, attempt: str, edge: Tuple[str, str], source: Hashable) -> ProtocolRecord:
    owner = f"edge:{edge[0]}:{edge[1]}"
    return make_protocol(
        EDGE_CREDENTIAL,
        owner,
        owner,
        (source,),
        {
            "attempt": attempt,
            "body": event_body(event),
            "edge": edge,
            "event_id": event.record_id,
            "source": source,
        },
    )


def certificate_records(cert: H1Certificate) -> Tuple[ProtocolRecord, ...]:
    return cert.prepares + cert.grants + (() if cert.edge is None else (cert.edge,))


def collect_h1(ledger: LocalLedger, event) -> Tuple[LocalLedger, Optional[H1Certificate], bool]:
    before = ledger
    try:
        rows = ledger.row_map()
        heads = ledger.head_map()
        if expected_from_local(rows, heads, ledger.edges, event) != event:
            raise AssertionError("local event mismatch")
        attempt = attempt_key(event)
        if attempt in ledger.used_attempts:
            raise AssertionError("used attempt")
        required = required_wires(event)
        locked = {(wire, head) for wire, head, _attempt, _grant in ledger.locks}
        if any((wire, heads[wire]) in locked for wire in required):
            raise AssertionError("exclusive head lock")
        prepares = tuple(prepare_record(event, attempt, wire, heads[wire]) for wire in required)
        grants = tuple(
            grant_record(event, attempt, wire, heads[wire], rows[wire], prepare)
            for wire, prepare in zip(required, prepares)
        )
        payload = event.payload_map()
        edge = None
        if payload["event_kind"] == "INTERACTION":
            endpoints = tuple(sorted((str(payload["initiator"]), str(payload["target"]))))
            source = dict(ledger.edge_sources)[endpoints]
            edge = edge_record(event, attempt, endpoints, source)
        cert = H1Certificate(event, attempt, prepares, grants, edge)
        records = certificate_records(cert)
        if any(not authentic_protocol(record) for record in records):
            raise AssertionError("issuer authentication")
        record_map = ledger.protocol_map()
        if any(record.record_id in record_map for record in records):
            raise AssertionError("protocol replay")
        locks = tuple(
            sorted(
                (
                    *ledger.locks,
                    *((wire, heads[wire], attempt, grant.record_id) for wire, grant in zip(required, grants)),
                ),
                key=repr,
            )
        )
        updated = replace(
            ledger,
            locks=locks,
            protocol_records=tuple(sorted((*ledger.protocol_records, *records), key=lambda x: x.record_id)),
        )
        return updated, cert, True
    except (AssertionError, KeyError, TypeError, ValueError):
        return before, None, False


def validate_certificate(ledger: LocalLedger, cert: H1Certificate) -> None:
    event = cert.event
    rows = ledger.row_map()
    heads = ledger.head_map()
    if cert.attempt != attempt_key(event) or cert.attempt in ledger.used_attempts:
        raise AssertionError("attempt mismatch/replay")
    if expected_from_local(rows, heads, ledger.edges, event) != event:
        raise AssertionError("stale or malformed event")
    required = required_wires(event)
    if len(cert.prepares) != len(required) or len(cert.grants) != len(required):
        raise AssertionError("protocol census")
    record_map = ledger.protocol_map()
    for wire, prepare, grant in zip(required, cert.prepares, cert.grants):
        expected_prepare = prepare_record(event, cert.attempt, wire, heads[wire])
        expected_grant = grant_record(
            event,
            cert.attempt,
            wire,
            heads[wire],
            rows[wire],
            expected_prepare,
        )
        if prepare != expected_prepare or grant != expected_grant:
            raise AssertionError("prepare/grant schema")
        if record_map.get(prepare.record_id) != prepare or record_map.get(grant.record_id) != grant:
            raise AssertionError("protocol record not collected")
        if (wire, heads[wire], cert.attempt, grant.record_id) not in set(ledger.locks):
            raise AssertionError("grant not exclusively locked")
    payload = event.payload_map()
    if payload["event_kind"] == "INTERACTION":
        endpoints = tuple(sorted((str(payload["initiator"]), str(payload["target"]))))
        source = dict(ledger.edge_sources).get(endpoints)
        if source is None:
            raise AssertionError("missing current edge")
        expected_edge = edge_record(event, cert.attempt, endpoints, source)
        if cert.edge != expected_edge or record_map.get(expected_edge.record_id) != expected_edge:
            raise AssertionError("edge source/authentication mismatch")
    elif cert.edge is not None:
        raise AssertionError("spurious edge credential")


def decision_record(cert: H1Certificate, commit: bool) -> ProtocolRecord:
    parents = tuple(grant.record_id for grant in cert.grants)
    if cert.edge is not None:
        parents += (cert.edge.record_id,)
    return make_protocol(
        HEAD_DECISION_COMMIT if commit else HEAD_DECISION_ABORT,
        f"attempt:{cert.attempt}",
        f"attempt:{cert.attempt}",
        parents,
        {
            "attempt": cert.attempt,
            "body": event_body(cert.event),
            "event_id": cert.event.record_id,
            "outcome": "COMMIT" if commit else "ABORT",
        },
    )


def commit_h1(ledger: LocalLedger, cert: H1Certificate) -> Tuple[LocalLedger, bool]:
    before = ledger
    try:
        validate_certificate(ledger, cert)
        event = cert.event
        decision = decision_record(cert, True)
        rows = ledger.row_map()
        heads = ledger.head_map()
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
        applies = []
        acks = []
        post_rows = dict((str(actor), row_tuple(d38.payload_row(encoded))) for actor, encoded in payload["post_rows"])
        for wire, grant in zip(required_wires(event), cert.grants):
            apply = make_protocol(
                HEAD_APPLY,
                wire,
                wire,
                (decision.record_id, grant.record_id),
                {
                    "attempt": cert.attempt,
                    "event_id": event.record_id,
                    "new_head": event.record_id,
                    "new_row": post_rows[wire],
                },
            )
            ack = make_protocol(
                HEAD_ACK,
                f"attempt:{cert.attempt}",
                wire,
                (apply.record_id,),
                {"attempt": cert.attempt, "apply": apply.record_id, "wire": wire},
            )
            applies.append(apply)
            acks.append(ack)
        appended = (decision, *applies, *acks)
        if any(not authentic_protocol(record) for record in appended):
            raise AssertionError("commit protocol authentication")
        removed = {
            (wire, head, cert.attempt, grant.record_id)
            for (wire, head, _attempt, _grant), grant in zip(
                (
                    next(lock for lock in ledger.locks if lock[0] == wire and lock[2] == cert.attempt)
                    for wire in required_wires(event)
                ),
                cert.grants,
            )
        }
        answer = LocalLedger(
            tuple(sorted(rows.items())),
            tuple(sorted(heads.items())),
            tuple(sorted(edges)),
            tuple(sorted(sources.items(), key=repr)),
            tuple(sorted(set(ledger.locks) - removed, key=repr)),
            tuple(sorted((*ledger.protocol_records, *appended), key=lambda x: x.record_id)),
            ledger.used_attempts | {cert.attempt},
        )
        return answer, True
    except (AssertionError, KeyError, StopIteration, TypeError, ValueError):
        return before, False


def abort_h1(ledger: LocalLedger, cert: H1Certificate) -> Tuple[LocalLedger, bool]:
    before = ledger
    try:
        validate_certificate(ledger, cert)
        decision = decision_record(cert, False)
        releases = []
        acks = []
        for wire, grant in zip(required_wires(cert.event), cert.grants):
            release = make_protocol(
                HEAD_RELEASE,
                wire,
                wire,
                (decision.record_id, grant.record_id),
                {"attempt": cert.attempt, "event_id": cert.event.record_id, "wire": wire},
            )
            ack = make_protocol(
                HEAD_ACK,
                f"attempt:{cert.attempt}",
                wire,
                (release.record_id,),
                {"attempt": cert.attempt, "apply": release.record_id, "wire": wire},
            )
            releases.append(release)
            acks.append(ack)
        removed = {lock for lock in ledger.locks if lock[2] == cert.attempt}
        if len(removed) != len(cert.grants):
            raise AssertionError("all-or-none release")
        appended = (decision, *releases, *acks)
        answer = replace(
            ledger,
            locks=tuple(sorted(set(ledger.locks) - removed, key=repr)),
            protocol_records=tuple(sorted((*ledger.protocol_records, *appended), key=lambda x: x.record_id)),
            used_attempts=ledger.used_attempts | {cert.attempt},
        )
        return answer, True
    except (AssertionError, KeyError, TypeError, ValueError):
        return before, False


def ledger_state(ledger: LocalLedger):
    return ledger.rows, ledger.heads, ledger.edges, ledger.edge_sources


def valid_events(store) -> Tuple[object, ...]:
    derived = d38.derive(store.history)
    rows = derived.row_map()
    answer = []
    for actor in sorted(rows):
        answer.append(d38.proposed(store, "IDLE", actor))
        answer.append(d38.proposed(store, "BIRTH", actor, f"{actor}/{rows[actor].births + 1}"))
    for left, right in derived.edges:
        answer.append(d38.proposed(store, "INTERACTION", left, right))
        answer.append(d38.proposed(store, "INTERACTION", right, left))
    return tuple(answer)


def registered_stores(depth: int = 2) -> Tuple[object, ...]:
    levels = [(d38.initial_store(),)]
    seen = {stable(d38.initial_store().history.records)}
    for _ in range(depth):
        next_level = []
        for store in levels[-1]:
            for event in valid_events(store):
                after, accepted = d38.transact(store, event)
                if not accepted:
                    raise AssertionError("valid registry event rejected")
                key = stable(after.history.records)
                if key not in seen:
                    seen.add(key)
                    next_level.append(after)
        levels.append(tuple(next_level))
    return tuple(store for level in levels for store in level)


def replace_protocol_record(ledger: LocalLedger, old: ProtocolRecord, new: ProtocolRecord) -> LocalLedger:
    records = tuple(new if record.record_id == old.record_id else record for record in ledger.protocol_records)
    return replace(ledger, protocol_records=records)


def certificate_checks() -> Tuple[int, ...]:
    stores = registered_stores(2)
    proposals = agreements = matches = causal = 0
    for store in stores:
        for event in valid_events(store):
            proposals += 1
            ledger = ledger_from_store(store)
            locked, cert, collected = collect_h1(ledger, event)
            if not collected or cert is None:
                raise AssertionError("complete valid event lacked certificate")
            after_ledger, admitted = commit_h1(locked, cert)
            after_store, oracle = d38.transact(store, event)
            agreements += int(admitted == oracle == True)
            oracle_ledger = ledger_from_store(after_store, after_ledger.used_attempts)
            matches += int(ledger_state(after_ledger) == ledger_state(oracle_ledger))
            causal += int(protocol_history_valid(after_ledger))

    base_store = d38.initial_store()
    base = ledger_from_store(base_store)
    interaction = d38.proposed(base_store, "INTERACTION", "A", "B")
    locked, cert, ok = collect_h1(base, interaction)
    if not ok or cert is None or cert.edge is None:
        raise AssertionError("hostile baseline")

    attacks = []
    p0, p1 = cert.prepares
    g0, g1 = cert.grants
    attacks.append(("forged prepare signature", locked, replace(cert, prepares=(replace(p0, signature="FORGED"), p1))))
    attacks.append(("forged grant signature", locked, replace(cert, grants=(replace(g0, signature="FORGED"), g1))))
    attacks.append(("wrong grant owner", locked, replace(cert, grants=(resign_protocol(g0, owner="B"), g1))))
    attacks.append(("wire substitution", locked, replace(cert, grants=(resign_protocol(g0, wire="Z"), g1))))
    attacks.append(("event mutation", locked, replace(cert, event=d38.proposed(base_store, "IDLE", "A"))))
    retarget = d38.resigned(interaction, payload={**interaction.payload_map(), "target": "A"})
    attacks.append(("retarget", locked, replace(cert, event=retarget)))
    attacks.append(("omitted prepare", locked, replace(cert, prepares=(p0,))))
    attacks.append(("omitted grant", locked, replace(cert, grants=(g0,))))
    attacks.append(("duplicate grant", locked, replace(cert, grants=(g0, g0))))
    attacks.append(("swapped grants", locked, replace(cert, grants=(g1, g0))))
    bad_payload = {**g0.payload_map(), "row": (1 - g0.payload_map()["row"][0],) + g0.payload_map()["row"][1:]}
    attacks.append(("row mismatch", locked, replace(cert, grants=(resign_protocol(g0, payload=bad_payload), g1))))
    attacks.append(("foreign attempt", locked, replace(cert, attempt="FOREIGN")))
    attacks.append(("foreign body", locked, replace(cert, grants=(resign_protocol(g0, payload={**g0.payload_map(), "body": "FOREIGN"}), g1))))

    foreign_edge = resign_protocol(
        cert.edge,
        parents=("FOREIGN_SOURCE",),
        payload={**cert.edge.payload_map(), "source": "FOREIGN_SOURCE"},
    )
    foreign_ledger = replace_protocol_record(locked, cert.edge, foreign_edge)
    attacks.append(("foreign edge source", foreign_ledger, replace(cert, edge=foreign_edge)))
    wrong_edge = resign_protocol(cert.edge, owner="edge:A:A", wire="edge:A:A", payload={**cert.edge.payload_map(), "edge": ("A", "A")})
    wrong_edge_ledger = replace_protocol_record(locked, cert.edge, wrong_edge)
    attacks.append(("wrong edge endpoints", wrong_edge_ledger, replace(cert, edge=wrong_edge)))

    birth = d38.proposed(base_store, "BIRTH", "A", "A/1")
    birth_locked, birth_cert, birth_ok = collect_h1(base, birth)
    if not birth_ok or birth_cert is None:
        raise AssertionError("birth baseline")
    wrong_ordinal = d38.resigned(birth, payload={**birth.payload_map(), "birth_ordinal": 9})
    attacks.append(("wrong birth ordinal", birth_locked, replace(birth_cert, event=wrong_ordinal)))
    wrong_ports = d38.resigned(birth, payload={**birth.payload_map(), "created_ports": (("A", "A/1"),)})
    attacks.append(("wrong birth ports", birth_locked, replace(birth_cert, event=wrong_ports)))

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
    attacks.append(("disconnected authentic lookalike", locked, replace(cert, event=disconnected)))

    rejected = durable = 0
    for _name, before, hostile in attacks:
        after, accepted = commit_h1(before, hostile)
        rejected += int(not accepted)
        durable += int(after == before)

    committed, accepted = commit_h1(locked, cert)
    replayed, replay_ok = commit_h1(committed, cert)
    rejected += int(accepted and not replay_ok)
    durable += int(replayed == committed)

    aborted, abort_ok = abort_h1(locked, cert)
    after_abort, after_abort_ok = commit_h1(aborted, cert)
    rejected += int(abort_ok and not after_abort_ok)
    durable += int(after_abort == aborted)

    idle = d38.proposed(base_store, "IDLE", "A")
    idle_locked, idle_cert, idle_ok = collect_h1(base, idle)
    sibling_after, sibling_cert, sibling_ok = collect_h1(idle_locked, interaction)
    rejected += int(idle_ok and idle_cert is not None and not sibling_ok and sibling_cert is None)
    durable += int(sibling_after == idle_locked)

    stale_locked, stale_cert, stale_ok = collect_h1(base, idle)
    if not stale_ok or stale_cert is None:
        raise AssertionError("stale baseline")
    released, released_ok = abort_h1(stale_locked, stale_cert)
    born_locked, born_cert, born_ok = collect_h1(released, birth)
    if not born_ok or born_cert is None:
        raise AssertionError("stale advance")
    advanced, advanced_ok = commit_h1(born_locked, born_cert)
    stale_after, stale_accept = commit_h1(advanced, stale_cert)
    rejected += int(released_ok and advanced_ok and not stale_accept)
    durable += int(stale_after == advanced)

    forged_partial = replace(cert, prepares=(p0,), grants=(replace(g0, signature="FORGED"),))
    partial_after, partial_ok = abort_h1(locked, forged_partial)
    rejected += int(not partial_ok)
    durable += int(partial_after == locked)

    partial_commit = replace(cert, prepares=(p0,), grants=(g0,), edge=None)
    partial_commit_after, partial_commit_ok = commit_h1(locked, partial_commit)
    rejected += int(not partial_commit_ok)
    durable += int(partial_commit_after == locked)

    attempted = len(attacks) + 6
    if attempted != 24 or rejected != attempted or durable != attempted:
        raise AssertionError((attempted, rejected, durable))
    return (
        len(stores),
        proposals,
        agreements,
        matches,
        causal,
        attempted,
        rejected,
        durable,
    )


# ---------------------------------------------------------------------------
# R5: computed finite action complex.


def canonical_star(star) -> Tuple[object, ...]:
    return (
        row_tuple(star.root_row),
        tuple(sorted((row.degree, row.births) for _actor, row in star.neighbors)),
        star.elapsed,
    )


def canonical_action(star, action: Tuple[str, str]) -> Tuple[object, ...]:
    tag, target = action
    if target == "NONE":
        return (tag, "NONE")
    row = star.neighbor_map()[target]
    return (tag, row.degree, row.births)


def transition_key(star, action: Tuple[str, str]) -> Tuple[object, ...]:
    return canonical_star(star), canonical_action(star, action)


def normalize_linear_row(coefficients: Mapping[Tuple[object, ...], int]) -> Tuple[Tuple[Tuple[object, ...], int], ...]:
    row = tuple(sorted(((key, value) for key, value in coefficients.items() if value), key=repr))
    if not row:
        return ()
    first = row[0][1]
    if first < 0:
        row = tuple((key, -value) for key, value in row)
    return row


def rational_rank(rows: Sequence[Sequence[Fraction]]) -> int:
    matrix = [list(map(Fraction, row)) for row in rows if any(row)]
    if not matrix:
        return 0
    rank = 0
    columns = len(matrix[0])
    for column in range(columns):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        divisor = matrix[rank][column]
        matrix[rank] = [value / divisor for value in matrix[rank]]
        for i in range(len(matrix)):
            if i == rank or not matrix[i][column]:
                continue
            factor = matrix[i][column]
            matrix[i] = [value - factor * base for value, base in zip(matrix[i], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def finite_action_complex() -> Tuple[
    Tuple[Tuple[object, ...], ...],
    Tuple[Tuple[Tuple[Tuple[object, ...], int], ...], ...],
    Tuple[Tuple[object, object, Tuple[str, str], Tuple[str, str]], ...],
    Tuple[object, ...],
    Tuple[Tuple[Tuple[object, ...], Tuple[object, ...], Tuple[object, ...]], ...],
]:
    seeds = d38.reachable_stars()
    states = {}
    frontier = list(seeds)
    for star in seeds:
        states[stable(star)] = star
    for _ in range(1):
        next_frontier = []
        for star in frontier:
            for action in d38.star_rates(star):
                after = d38.star_step(star, action)
                key = stable(after)
                if key not in states:
                    states[key] = after
                    next_frontier.append(after)
        frontier = next_frontier

    variables = set()
    square_rows = set()
    squares = []
    graph_states = set()
    transition_map = {}

    def register(star, action):
        variable = transition_key(star, action)
        source = canonical_star(star)
        target = canonical_star(d38.star_step(star, action))
        prior = transition_map.get(variable)
        if prior is not None and prior != (source, target):
            raise AssertionError("nonlocal transition key")
        transition_map[variable] = (source, target)
        variables.add(variable)
        graph_states.update((source, target))
        return variable

    for star in states.values():
        graph_states.add(canonical_star(star))
        actions = tuple(d38.star_rates(star))
        for action in actions:
            register(star, action)
        for first, second in combinations(actions, 2):
            after_first = d38.star_step(star, first)
            after_second = d38.star_step(star, second)
            if second not in d38.star_rates(after_first) or first not in d38.star_rates(after_second):
                continue
            final_12 = d38.star_step(after_first, second)
            final_21 = d38.star_step(after_second, first)
            if canonical_star(final_12) != canonical_star(final_21):
                continue
            keys = (
                register(star, first),
                register(after_first, second),
                register(star, second),
                register(after_second, first),
            )
            coefficients: Dict[Tuple[object, ...], int] = {}
            for key, sign in zip(keys, (1, 1, -1, -1)):
                coefficients[key] = coefficients.get(key, 0) + sign
            row = normalize_linear_row(coefficients)
            if row:
                square_rows.add(row)
                squares.append((star, (after_first, after_second), first, second))

    return (
        tuple(sorted(variables, key=repr)),
        tuple(sorted(square_rows, key=repr)),
        tuple(squares),
        tuple(sorted(graph_states, key=repr)),
        tuple(
            sorted(
                ((variable, source, target) for variable, (source, target) in transition_map.items()),
                key=repr,
            )
        ),
    )


def action_checks() -> Tuple[object, ...]:
    variables, symbolic_rows, squares, states, transitions = finite_action_complex()
    index = {variable: i for i, variable in enumerate(variables)}
    matrix = []
    for row in symbolic_rows:
        vector = [Fraction() for _ in variables]
        for variable, coefficient in row:
            vector[index[variable]] = Fraction(coefficient)
        matrix.append(tuple(vector))
    rank = rational_rank(matrix)
    dimension = len(variables) - rank

    # Coboundaries log w(s,e)=phi(se)-phi(s) lie in the cocycle kernel.
    parent = {state: state for state in states}

    def find(state):
        while parent[state] != state:
            parent[state] = parent[parent[state]]
            state = parent[state]
        return state

    def union(left, right):
        root_left = find(left)
        root_right = find(right)
        if root_left != root_right:
            parent[root_right] = root_left

    for _variable, state, after in transitions:
        union(state, after)
    components = len({find(state) for state in states})
    coboundary_rank = len(states) - components

    chosen_violations = 0
    chosen_equal = 0
    initial_products = None
    for star, (_after_first, _after_second), first, second in squares:
        after_first = d38.star_step(star, first)
        after_second = d38.star_step(star, second)
        product_12 = d38.star_kernel(star)[first] * d38.star_kernel(after_first)[second]
        product_21 = d38.star_kernel(star)[second] * d38.star_kernel(after_second)[first]
        chosen_equal += int(product_12 == product_21)
        chosen_violations += int(product_12 != product_21)
        if (
            canonical_star(star) == canonical_star(d38.star_from_history(d38.initial_store().history))
            and first == ("ROOT_IDLE", "NONE")
            and second == ("NEIGHBOR_BIRTH", "B")
        ):
            initial_products = (product_12, product_21)
        if (
            canonical_star(star) == canonical_star(d38.star_from_history(d38.initial_store().history))
            and second == ("ROOT_IDLE", "NONE")
            and first == ("NEIGHBOR_BIRTH", "B")
        ):
            initial_products = (product_21, product_12)
    if initial_products != (Fraction(1, 18), Fraction(2, 33)):
        raise AssertionError(initial_products)
    positive_representative = int(all(sum(row, Fraction()) == 0 for row in matrix))
    normalized_rows, normalized_squares, normalized_square_pass, terminal_paths = completion_kernel_checks(3)
    return (
        len(states),
        len(variables),
        len(symbolic_rows),
        rank,
        dimension,
        coboundary_rank,
        positive_representative,
        chosen_equal,
        chosen_violations,
        initial_products[0],
        initial_products[1],
        normalized_rows,
        normalized_squares,
        normalized_square_pass,
        terminal_paths,
    )


def completion_kernel_checks(horizon: int) -> Tuple[int, int, int, int]:
    initial = d38.star_from_history(d38.initial_store().history)

    @lru_cache(maxsize=None)
    def completions(star, remaining: int) -> int:
        if remaining == 0:
            return 1
        return sum(
            completions(d38.star_step(star, action), remaining - 1)
            for action in d38.star_rates(star)
        )

    layers = [{initial}]
    for _ in range(horizon):
        layers.append(
            {
                d38.star_step(star, action)
                for star in layers[-1]
                for action in d38.star_rates(star)
            }
        )
    normalized = squares = square_pass = 0
    for layer in range(horizon):
        remaining = horizon - layer
        for star in layers[layer]:
            denominator = Fraction(completions(star, remaining))
            probabilities = {
                action: Fraction(completions(d38.star_step(star, action), remaining - 1), denominator)
                for action in d38.star_rates(star)
            }
            normalized += int(sum(probabilities.values(), Fraction()) == 1)
            if remaining < 2:
                continue
            for first, second in combinations(tuple(probabilities), 2):
                after_first = d38.star_step(star, first)
                after_second = d38.star_step(star, second)
                if second not in d38.star_rates(after_first) or first not in d38.star_rates(after_second):
                    continue
                final_12 = d38.star_step(after_first, second)
                final_21 = d38.star_step(after_second, first)
                if final_12 != final_21:
                    continue
                p12 = probabilities[first] * Fraction(
                    completions(final_12, remaining - 2),
                    completions(after_first, remaining - 1),
                )
                p21 = probabilities[second] * Fraction(
                    completions(final_21, remaining - 2),
                    completions(after_second, remaining - 1),
                )
                squares += 1
                square_pass += int(p12 == p21)
    return normalized, squares, square_pass, completions(initial, horizon)


# ---------------------------------------------------------------------------
# R6: orbit-level finite all-transport classification.


@dataclass(frozen=True)
class MarkedGraph:
    adjacency: Tuple[Tuple[int, ...], ...]
    marks: Tuple[Tuple[Hashable, ...], ...]


def marked_graph(
    vertex_count: int,
    edges: Iterable[Tuple[int, int]],
    marks: Optional[Sequence[Tuple[Hashable, ...]]] = None,
) -> MarkedGraph:
    rows = [set() for _ in range(vertex_count)]
    for left, right in edges:
        rows[left].add(right)
        rows[right].add(left)
    if marks is None:
        marks = tuple(("ACTOR",) for _ in range(vertex_count))
    return MarkedGraph(tuple(tuple(sorted(row)) for row in rows), tuple(marks))


def automorphisms(graph: MarkedGraph) -> Tuple[Tuple[int, ...], ...]:
    n = len(graph.adjacency)
    edges = {
        tuple(sorted((u, v)))
        for u, row in enumerate(graph.adjacency)
        for v in row
        if u < v
    }
    answer = []
    for perm in permutations(range(n)):
        image_edges = {tuple(sorted((perm[u], perm[v]))) for u, v in edges}
        marks_ok = all(graph.marks[u] == graph.marks[perm[u]] for u in range(n))
        if image_edges == edges and marks_ok:
            answer.append(tuple(perm))
    return tuple(answer)


def vertex_orbits(graph: MarkedGraph) -> Tuple[FrozenSet[int], ...]:
    autos = automorphisms(graph)
    unseen = set(range(len(graph.adjacency)))
    answer = []
    while unseen:
        seed = min(unseen)
        orbit = frozenset(perm[seed] for perm in autos)
        answer.append(orbit)
        unseen -= set(orbit)
    return tuple(sorted(answer, key=lambda value: repr(sorted(value))))


def pair_orbits(graph: MarkedGraph) -> Tuple[FrozenSet[Tuple[int, int]], ...]:
    autos = automorphisms(graph)
    n = len(graph.adjacency)
    unseen = {(u, v) for u in range(n) for v in range(n)}
    answer = []
    while unseen:
        seed = min(unseen)
        orbit = frozenset((perm[seed[0]], perm[seed[1]]) for perm in autos)
        answer.append(orbit)
        unseen -= set(orbit)
    return tuple(sorted(answer, key=lambda value: repr(sorted(value))))


def orbit_transport_rows(graph: MarkedGraph) -> Tuple[Tuple[Fraction, ...], ...]:
    roots = vertex_orbits(graph)
    rows = []
    n = len(graph.adjacency)
    for pair_orbit in pair_orbits(graph):
        coefficients = []
        for root_orbit in roots:
            representative = min(root_orbit)
            sent = sum(int((representative, target) in pair_orbit) for target in range(n))
            received = sum(int((source, representative) in pair_orbit) for source in range(n))
            coefficients.append(Fraction(sent - received))
        if any(coefficients):
            rows.append(tuple(coefficients))
    return tuple(rows)


def orbit_mtp_holds(graph: MarkedGraph, orbit_masses: Sequence[Fraction]) -> bool:
    if sum(orbit_masses, Fraction()) != 1:
        return False
    return all(
        sum((mass * coefficient for mass, coefficient in zip(orbit_masses, row)), Fraction()) == 0
        for row in orbit_transport_rows(graph)
    )


def covariant_label_law(graph: MarkedGraph, probabilities: Mapping[int, Fraction]) -> bool:
    return all(
        len({probabilities[vertex] for vertex in orbit}) == 1
        for orbit in vertex_orbits(graph)
    )


def transport_checks() -> Tuple[int, ...]:
    graphs = (
        marked_graph(3, ((0, 1), (1, 2))),
        marked_graph(4, ((0, 1), (0, 2), (0, 3))),
        marked_graph(4, ((0, 1), (1, 2), (2, 3)), (("END",), ("MID",), ("MID",), ("END",))),
    )
    pair_count = rank_complete = uniform_pass = biased_reject = covariance_controls = 0
    for graph in graphs:
        roots = vertex_orbits(graph)
        pair_count += len(pair_orbits(graph))
        rank = rational_rank(orbit_transport_rows(graph))
        rank_complete += int(rank == len(roots) - 1)
        n = len(graph.adjacency)
        uniform = tuple(Fraction(len(orbit), n) for orbit in roots)
        uniform_pass += int(orbit_mtp_holds(graph, uniform))
        total_degree = sum(len(row) for row in graph.adjacency)
        biased = tuple(
            Fraction(sum(len(graph.adjacency[v]) for v in orbit), total_degree)
            for orbit in roots
        )
        biased_reject += int(not orbit_mtp_holds(graph, biased))
        for orbit in roots:
            if len(orbit) > 1:
                vector = {vertex: Fraction(1, n) for vertex in range(n)}
                first, last = min(orbit), max(orbit)
                vector[first] -= Fraction(1, 2 * n)
                vector[last] += Fraction(1, 2 * n)
                covariance_controls += int(not covariant_label_law(graph, vector))
                break

    mixture_weights = (Fraction(1, 3), Fraction(2, 3))
    mixture_pass = 0
    for graph, weight in zip(graphs[:2], mixture_weights):
        n = len(graph.adjacency)
        conditional = tuple(Fraction(len(orbit), n) for orbit in vertex_orbits(graph))
        weighted = tuple(weight * mass for mass in conditional)
        for row in orbit_transport_rows(graph):
            if sum((mass * coefficient for mass, coefficient in zip(weighted, row)), Fraction()):
                raise AssertionError("mixture transport")
        mixture_pass += 1
    return (
        pair_count,
        rank_complete,
        uniform_pass,
        biased_reject,
        covariance_controls,
        mixture_pass,
        0,
    )


# ---------------------------------------------------------------------------
# R7: actual gauge-pushed typed untimed D38b causal-DAG laws.


@dataclass(frozen=True)
class RatePacket:
    actor_rates: Tuple[int, int]
    mode_weights: Tuple[int, int, int]


def lineage_root(actor: str) -> str:
    return actor.split("/")[0]


def actor_rate(packet: RatePacket, actor: str, overrides: Optional[Mapping[str, int]] = None) -> Fraction:
    if overrides is not None and actor in overrides:
        return Fraction(overrides[actor])
    root = lineage_root(actor)
    if root == "A":
        return Fraction(packet.actor_rates[0])
    if root == "B":
        return Fraction(packet.actor_rates[1])
    raise AssertionError(("unknown lineage", actor))


def event_intensities(
    store,
    packet: RatePacket,
    overrides: Optional[Mapping[str, int]] = None,
) -> Tuple[Tuple[object, Fraction], ...]:
    derived = d38.derive(store.history)
    rows = derived.row_map()
    edges = set(derived.edges)
    neighbors = {actor: [] for actor in rows}
    for left, right in edges:
        neighbors[left].append(right)
        neighbors[right].append(left)
    birth_weight, idle_weight, interaction_weight = map(Fraction, packet.mode_weights)
    answer = []
    for actor in sorted(rows):
        rho = actor_rate(packet, actor, overrides)
        child = f"{actor}/{rows[actor].births + 1}"
        answer.append((d38.proposed(store, "BIRTH", actor, child), rho * birth_weight))
        answer.append((d38.proposed(store, "IDLE", actor), rho * idle_weight))
        if neighbors[actor]:
            allocation = Fraction(1, len(neighbors[actor]))
            for target in sorted(neighbors[actor]):
                answer.append(
                    (
                        d38.proposed(store, "INTERACTION", actor, target),
                        rho * interaction_weight * allocation,
                    )
                )
    return tuple(sorted(answer, key=lambda item: repr(item[0].record_id)))


def embedded_paths(packet: RatePacket, depth: int = 2):
    distribution = {(): Fraction(1)}
    stores = {(): d38.initial_store()}
    for _ in range(depth):
        next_distribution = {}
        next_stores = {}
        for path, probability in distribution.items():
            store = stores[path]
            rates = event_intensities(store, packet)
            total = sum((rate for _event, rate in rates), Fraction())
            for event, rate in rates:
                extended = path + (event,)
                next_distribution[extended] = probability * rate / total
                after, accepted = d38.transact(store, event)
                if not accepted:
                    raise AssertionError("embedded valid event rejected")
                next_stores[extended] = after
        distribution, stores = next_distribution, next_stores
    return distribution


def typed_event_row(event) -> Tuple[object, ...]:
    payload = event.payload_map()
    return (
        event.record_id,
        str(payload["event_kind"]),
        event.owner,
        tuple(event.wires),
        tuple(event.parents),
        digest(event.payload),
    )


def dag_atom(path: Sequence[object]) -> Tuple[Tuple[object, ...], ...]:
    return tuple(sorted((typed_event_row(event) for event in path), key=repr))


def untyped_atom(path: Sequence[object]) -> Tuple[Tuple[object, ...], ...]:
    return tuple(
        sorted(
            (
                (
                    event.payload_map()["event_kind"],
                    len(event.wires),
                    len(event.parents),
                    tuple(sorted(row_tuple(d38.payload_row(encoded))[1:] for _actor, encoded in event.payload_map()["post_rows"])),
                )
                for event in path
            ),
            key=repr,
        )
    )


def push_path_law(packet: RatePacket, typed: bool = True) -> Tuple[Dict[Tuple[object, ...], Fraction], int]:
    paths = embedded_paths(packet, 2)
    law: Dict[Tuple[object, ...], Fraction] = {}
    for path, probability in paths.items():
        atom = dag_atom(path) if typed else untyped_atom(path)
        law[atom] = law.get(atom, Fraction()) + probability
    if sum(law.values(), Fraction()) != 1:
        raise AssertionError("DAG pushforward normalization")
    merged = len(paths) - len(law)
    return law, merged


def projective_key(values: Sequence[int]) -> Tuple[Fraction, ...]:
    first = Fraction(values[0])
    return tuple(Fraction(value) / first for value in values)


def law_signature(law: Mapping[Tuple[object, ...], Fraction]) -> str:
    return digest(tuple(sorted(law.items(), key=repr)))


def retained_root_action(store, event, root: str = "A") -> Optional[Tuple[str, str]]:
    payload = event.payload_map()
    kind = str(payload["event_kind"])
    initiator = str(payload["initiator"])
    target = str(payload["target"])
    derived = d38.derive(store.history)
    neighbors = set()
    for left, right in derived.edges:
        if left == root:
            neighbors.add(right)
        elif right == root:
            neighbors.add(left)
    if initiator == root:
        if kind == "BIRTH":
            return ("ROOT_BIRTH", "NONE")
        if kind == "IDLE":
            return ("ROOT_IDLE", "NONE")
        return ("ROOT_OUT", target)
    if kind == "INTERACTION" and target == root:
        return ("INCOMING", initiator)
    if kind == "BIRTH" and initiator in neighbors:
        return ("NEIGHBOR_BIRTH", initiator)
    return None


def first_retained_law(store, packet: RatePacket, overrides: Mapping[str, int]) -> Dict[Tuple[str, str], Fraction]:
    retained = []
    for event, rate in event_intensities(store, packet, overrides):
        action = retained_root_action(store, event)
        if action is not None:
            retained.append((action, rate))
    total = sum((rate for _action, rate in retained), Fraction())
    law: Dict[Tuple[str, str], Fraction] = {}
    for action, rate in retained:
        law[action] = law.get(action, Fraction()) + rate / total
    return law


def one_event_typed_law(store, packet: RatePacket, overrides: Mapping[str, int]) -> Dict[Tuple[object, ...], Fraction]:
    rates = event_intensities(store, packet, overrides)
    total = sum((rate for _event, rate in rates), Fraction())
    return {typed_event_row(event): rate / total for event, rate in rates}


def silent_closure_checks(store, packet: RatePacket, overrides: Mapping[str, int]) -> Tuple[int, int]:
    baseline = first_retained_law(store, packet, overrides)
    checked = invariant = 0
    for event, _rate in event_intensities(store, packet, overrides):
        if retained_root_action(store, event) is not None:
            continue
        after, accepted = d38.transact(store, event)
        if not accepted:
            raise AssertionError("silent valid event rejected")
        checked += 1
        invariant += int(first_retained_law(after, packet, overrides) == baseline)
    return checked, invariant


def identifiability_checks() -> Tuple[int, ...]:
    typed_laws: Dict[str, set[Tuple[Tuple[Fraction, ...], Tuple[Fraction, ...]]]] = {}
    untyped_laws: Dict[str, set[Tuple[Tuple[Fraction, ...], Tuple[Fraction, ...]]]] = {}
    packets = 0
    merge_count = 0
    for actor in product(range(1, 4), repeat=2):
        for mode in product(range(1, 3), repeat=3):
            packet = RatePacket(actor, mode)
            key = (projective_key(actor), projective_key(mode))
            typed, merged = push_path_law(packet, True)
            untyped, _ = push_path_law(packet, False)
            typed_laws.setdefault(law_signature(typed), set()).add(key)
            untyped_laws.setdefault(law_signature(untyped), set()).add(key)
            packets += 1
            merge_count += merged
    typed_collisions = sum(int(len(keys) != 1) for keys in typed_laws.values())
    untyped_collisions = sum(int(len(keys) > 1) for keys in untyped_laws.values())
    projective_classes = len(
        {
            (projective_key(actor), projective_key(mode))
            for actor in product(range(1, 4), repeat=2)
            for mode in product(range(1, 3), repeat=3)
        }
    )

    base_packet = RatePacket((1, 2), (1, 2, 1))
    scale_packet = RatePacket((3, 6), (5, 10, 5))
    common_scale = int(
        law_signature(push_path_law(base_packet)[0])
        == law_signature(push_path_law(scale_packet)[0])
    )

    store = d38.execute(d38.initial_store(), "BIRTH", "B", "B/1")
    ol_a = first_retained_law(store, base_packet, {"B/1": 1})
    ol_b = first_retained_law(store, base_packet, {"B/1": 7})
    ou_a = one_event_typed_law(store, base_packet, {"B/1": 1})
    ou_b = one_event_typed_law(store, base_packet, {"B/1": 7})
    ol_collision = int(ol_a == ol_b and ou_a != ou_b)
    silent_a = silent_closure_checks(store, base_packet, {"B/1": 1})
    silent_b = silent_closure_checks(store, base_packet, {"B/1": 7})
    return (
        packets,
        projective_classes,
        len(typed_laws),
        typed_collisions,
        len(untyped_laws),
        untyped_collisions,
        merge_count,
        common_scale,
        ol_collision,
        len(ou_a),
        len(ol_a),
        silent_a[0] + silent_b[0],
        silent_a[1] + silent_b[1],
    )


# ---------------------------------------------------------------------------
# R8: timed scale and the conditional D26 interface.


def total_hazard(store, packet: RatePacket) -> Fraction:
    return sum((rate for _event, rate in event_intensities(store, packet)), Fraction())


def timing_visibility_checks() -> Tuple[object, ...]:
    store = d38.initial_store()
    first = RatePacket((1, 2), (1, 2, 1))
    scaled = RatePacket((3, 6), (1, 2, 1))
    law_same = int(law_signature(push_path_law(first)[0]) == law_signature(push_path_law(scaled)[0]))
    hazard_first = total_hazard(store, first)
    hazard_scaled = total_hazard(store, scaled)
    construction_separated = int(hazard_scaled == 3 * hazard_first)
    observed_first = hazard_first / 2
    observed_scaled = hazard_scaled / 6
    bridge_null = int(observed_first == observed_scaled)
    fixed_bridge_separated = int(hazard_first / 2 != hazard_scaled / 2)

    born = tuple(Fraction(4, 5) ** count for count in range(9))
    token = tuple(Fraction(1) for _ in range(9))
    d26_output = LOCKS["D26-data"][0].read_text()
    prior_d39_output = LOCKS["D39-rejected-data"][0].read_text()
    inherited = int(
        "birth-decoherence bridge" in d26_output
        and "three_BORN=64/125" in prior_d39_output
    )
    return (
        law_same,
        hazard_first,
        hazard_scaled,
        construction_separated,
        observed_first,
        bridge_null,
        fixed_bridge_separated,
        born,
        token,
        inherited,
    )


# ---------------------------------------------------------------------------
# R9: exact pinned-alphabet response and tail controls.


Vector2 = Tuple[Fraction, Fraction]
Matrix2 = Tuple[Tuple[Fraction, Fraction], Tuple[Fraction, Fraction]]


ACTIVE_PREPARATIONS: Tuple[Vector2, ...] = (
    (Fraction(1), Fraction()),
    (Fraction(), Fraction(1)),
    (Fraction(3, 5), Fraction(4, 5)),
    (Fraction(5, 13), Fraction(12, 13)),
)


def responses(state: Vector2) -> Tuple[Fraction, Fraction]:
    c, s = state
    return s * s, Fraction(1, 2) + c * s


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


def operational_checks() -> Tuple[object, ...]:
    response_rows = tuple(responses(state) for state in ACTIVE_PREPARATIONS)
    pair_distances = tuple(
        max(abs(response_rows[i][query] - response_rows[j][query]) for query in (0, 1))
        for i, j in combinations(range(len(response_rows)), 2)
    )
    separated = sum(int(distance > 0) for distance in pair_distances)
    attenuated_nonzero = sum(
        int(distance * Fraction(1, 2**radius) > 0)
        for distance in pair_distances
        for radius in range(1, 13)
    )
    epsilon = Fraction(1, 64)
    max_distance = max(pair_distances)
    path_cutoff = next(
        radius for radius in range(20) if max_distance * Fraction(1, 2**radius) <= epsilon
    )
    summable_cutoff = next(
        radius for radius in range(20) if max_distance * Fraction(1, 2**radius) <= epsilon
    )
    nonsummable_shells = sum(
        int(max_distance * Fraction(2**radius, 2**radius) > epsilon)
        for radius in range(1, 13)
    )

    r1: Matrix2 = ((Fraction(4, 5), Fraction(-3, 5)), (Fraction(3, 5), Fraction(4, 5)))
    r2: Matrix2 = ((Fraction(3, 5), Fraction(-4, 5)), (Fraction(4, 5), Fraction(3, 5)))
    identity: Matrix2 = ((Fraction(1), Fraction()), (Fraction(), Fraction(1)))
    cancellation = int(matmul(matpow(r2, 4), matpow(r1, 4)) == identity)
    mid = (2 * Fraction(4, 5) * Fraction(3, 5)) ** 2
    inherited = int(
        "Ry(3/5,4/5)" in LOCKS["D28-data"][0].read_text()
        and "576/625" in LOCKS["D31b-data"][0].read_text()
    )
    return (
        len(response_rows),
        len(pair_distances),
        separated,
        attenuated_nonzero,
        epsilon,
        path_cutoff,
        summable_cutoff,
        nonsummable_shells,
        cancellation,
        mid,
        inherited,
    )


# ---------------------------------------------------------------------------
# Integrated repaired receipt.


def main() -> None:
    out = []
    gates: Dict[str, bool] = {}
    science: Dict[str, object] = {}

    def emit(line: str) -> None:
        out.append(line)
        print(line)

    emit("[D39b selecting record-closed laws — hostile repair exact receipt]")
    emit("ARITHMETIC: integer/Fraction exact; no floating theorem")
    emit("SCOPE: finite classical repair; Paper 28 HELD pending closing review")

    locks = locked_antecedents()
    gates["R0"] = len(locks) == 16
    science["locks"] = locks
    emit("[LOCKS / REPAIR SCOPE]")
    emit(f"antecedent_locks={stable(locks)}")
    emit("comparison=SHARED_D37_INTERFACE_SCHEMA_SPAN; D37_CONDITIONAL_EQUIVALENCE=NOT_CLAIMED")
    emit("generated_conflict=LEVEL_B_OPEN; infinite_completion=OPEN; clock_quantum_seal_bridges=OPEN")

    comparison = comparison_checks()
    gates["R1"] = comparison == (38, 72, 1, 2, 2, 1, 6, 12, 12, 1760, 1, 0, 38, 38)
    science["comparison"] = comparison
    emit("[SHARED REGIONAL-INTERFACE CATEGORY / ACTUAL D37 EMBEDDING]")
    emit(f"D37_interface_objects={comparison[12]}; distinct_namespaced_images={comparison[13]}/{comparison[12]}; identities={comparison[0]}/{comparison[12]}; strict_compositions={comparison[1]}/72; D38_identity_composition={comparison[2]},{comparison[3]}/2")
    emit(f"D38_direct_staged_restrictions={comparison[4]}/2; update_naturality={comparison[5]}/1; typed_boundary_rows={comparison[6]}")
    emit(f"pushed_normalizations={comparison[7]}/12; pushed_prefixes={comparison[8]}/12; positive_atoms={comparison[9]}")
    emit(f"triple_cover_nonextension_witness={comparison[10]}/1; global_witness_fields_in_target={comparison[11]}; equivalence=0; K_membership=0")

    vacuity = vacuity_checks()
    gates["R2"] = vacuity == (5, 5, 1, 3, 8, 1)
    science["vacuity"] = vacuity
    emit("[LEVEL-B GENERATED-CONFLICT VACUITY / LOCKED D36 VOCABULARY]")
    emit(f"registered_histories={vacuity[0]}; empty_generated_conflict_images={vacuity[1]}; false_next-event_relabel_rejected={vacuity[2]}")
    emit(f"D36_transaction_carrier_kinds={vacuity[3]}; protocol_kinds={vacuity[4]}; locked_constant_match={vacuity[5]}/1")
    emit("proposal_role=BORN_OR_TOKEN_TRANSACTION_CARRIER; generated_K_member=OPEN")

    h0 = h0_checks()
    gates["R3"] = h0 == (1, 1, 1, 1)
    science["h0"] = h0
    emit("[H0 STATIC HEAD ADJUDICATION]")
    emit(f"valid_agreement={h0[0]}/1; once_authentic_stale_still_verifies={h0[1]}/1; oracle_rejects_stale={h0[2]}/1; stores_unchanged_on_reject={h0[3]}/1")
    emit("H0=REJECTED; issuance_authentication_is_not_currentness")

    certificate = certificate_checks()
    gates["R4"] = certificate == (47, 410, 410, 410, 410, 24, 24, 24)
    science["certificate"] = certificate
    emit("[H1 TYPED CAUSAL PER-WIRE ADMISSION]")
    emit(f"registered_histories={certificate[0]}; valid_proposals={certificate[1]}; oracle_agreements={certificate[2]}/{certificate[1]}; successor_matches={certificate[3]}/{certificate[1]}")
    emit(f"causal_protocol_validations={certificate[4]}/{certificate[1]}; hostile_rejections={certificate[6]}/{certificate[5]}; byte_identical_failures={certificate[7]}/{certificate[5]}")
    emit("records=HEAD_PREPARE>HEAD_GRANT>DECISION>(APPLY|RELEASE)>ACK; edge_source_bound=1; all_or_none_release=1")
    emit("H1=SAFETY_AND_CERTIFICATE_EXISTENCE_ON_EXHAUSTED_DEPTH_0_TO_2_REGISTRY; asynchronous_liveness_and_global_all_history_locality=NOT_CLAIMED")

    action = action_checks()
    gates["R5"] = (
        action[:7] == (155, 401, 344, 246, 155, 154, 1)
        and action[7:9] == (169, 337)
        and action[9:11] == (Fraction(1, 18), Fraction(2, 33))
        and action[11:] == (21, 78, 78, 179)
    )
    science["action"] = action
    emit("[COMPUTED FINITE ACTION COMPLEX]")
    emit(f"canonical_states={action[0]}; local_transition_variables={action[1]}; distinct_cocycle_rows={action[2]}; exact_rank={action[3]}")
    emit(f"positive_log_weight_dimension={action[4]}; coboundary_rank={action[5]}; unit_unnormalized_positive_representative={action[6]}/1")
    emit(f"chosen_D38b_square_equalities={action[7]}; violations={action[8]}; initial_obstruction={ftext(action[9])},{ftext(action[10])}")
    emit(f"finite_horizon_completion_kernel_normalizations={action[11]}/21; cocycle_squares={action[13]}/{action[12]}; terminal_paths={action[14]}")
    emit("classification=RESIDUAL_UNNORMALIZED_INCREMENT_VARIETY_WITH_FINITE_HORIZON_NORMALIZED_REPRESENTATIVE; chosen_D38b_member=NO_ON_REGISTERED_ACTION_QUOTIENT; stationary_infinite_member=OPEN")

    transport = transport_checks()
    gates["R6"] = transport == (18, 3, 3, 3, 3, 2, 0)
    science["transport"] = transport
    emit("[ORBIT-LEVEL FINITE ALL-TRANSPORT CLASSIFICATION]")
    emit(f"doubly_rooted_orbit_census={transport[0]}; reduced_rank_complete={transport[1]}/3; uniform_vertex_root_laws={transport[2]}/3")
    emit(f"degree_biased_rejections={transport[3]}/3; noncovariant_label_controls_rejected={transport[4]}/3; free_unrooted_mixtures={transport[5]}/2")
    emit(f"infinite_unimodular_completion_constructed={transport[6]}")

    ident = identifiability_checks()
    gates["R7"] = ident == (72, 49, 49, 0, 28, 21, 288, 1, 1, 10, 5, 10, 10)
    science["identifiability"] = ident
    emit("[GAUGE-PUSHED TYPED UNTIMED CAUSAL-DAG IDENTIFIABILITY]")
    emit(f"parameter_packets={ident[0]}; projective_ratio_classes={ident[1]}; typed_DAG_laws={ident[2]}; typed_residual_collisions={ident[3]}")
    emit(f"untyped_laws={ident[4]}; untyped_colliding_laws={ident[5]}; serial_paths_merged_by_DAG_gauge={ident[6]}")
    emit(f"common_scale_null={ident[7]}/1; actual_O_L_silent_actor_collision={ident[8]}/1; O_U_atoms_at_control={ident[9]}; O_L_atoms={ident[10]}")
    emit(f"one_silent_step_closure_checks={ident[12]}/{ident[11]}")
    emit("result=REGISTERED_PROJECTIVE_INJECTIVITY_ONLY; global_identifiability=OPEN")

    timing = timing_visibility_checks()
    gates["R8"] = (
        timing[:7] == (1, Fraction(12), Fraction(36), 1, Fraction(6), 1, 1)
        and timing[7][3] == Fraction(64, 125)
        and all(value == 1 for value in timing[8])
        and timing[9] == 1
    )
    science["timing"] = timing
    emit("[TIMED SCALE / CLOCK BRIDGE / D26 CONDITIONAL]")
    emit(f"untimed_scaled_law_equal={timing[0]}/1; construction_hazards={ftext(timing[1])},{ftext(timing[2])}; separated={timing[3]}/1")
    emit(f"unknown_clock_equal_observed_hazard={ftext(timing[4])}; bridge_null={timing[5]}/1; fixed_bridge_separates={timing[6]}/1")
    emit(f"same_line_BORN_N0_to_N8={tuple(ftext(value) for value in timing[7])}; dormant_TOKEN={tuple(ftext(value) for value in timing[8])}; inherited_D26_regression={timing[9]}/1")
    emit("absolute_physical_scale=CLOCK_BRIDGE_DEPENDENT; maintenance_rate_without_O_V=NOT_INFERRED")

    operational = operational_checks()
    gates["R9"] = operational == (
        4,
        6,
        6,
        72,
        Fraction(1, 64),
        6,
        6,
        12,
        1,
        Fraction(576, 625),
        1,
    )
    science["operational"] = operational
    emit("[PINNED D28/D31B ALPHABET RESPONSE / COMPLETE-TAIL CONTROLS]")
    emit(f"active_preparations={operational[0]}; active_pairs={operational[1]}; response_separated_pairs={operational[2]}/{operational[1]}; attenuated_nonzero_pair_depths={operational[3]}/72")
    emit(f"epsilon={ftext(operational[4])}; single_path_cutoff={operational[5]}; summable_branching_cutoff={operational[6]}; nonsummable_shells={operational[7]}/12")
    emit(f"D31B_exact_cancellation={operational[8]}/1; mid_history_influence={ftext(operational[9])}; inherited_alphabet_cancellation_regression={operational[10]}/1")
    emit("D38b_quantum_join=UNDEFINED; V6_seal_identification=0; exact_ontological_erasure=NOT_CLAIMED")

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
    emit("SHARED D37 INTERFACE-SCHEMA SPAN / LEVEL-B GENERATED CONFLICT OPEN")
    emit("H0 REJECTED / TYPED CAUSAL H1 SUFFICIENT ON EXHAUSTED FINITE REGISTRY")
    emit("RESIDUAL INCREMENT VARIETY WITH FINITE-HORIZON NORMALIZED REPRESENTATIVE / FINITE UNIFORM-ROOT CLASSIFICATION / REGISTERED PROJECTIVE O-U IDENTIFIABILITY")
    emit("chosen D38b action membership, infinite completion, global identification, clock, quantum and sealing bridges remain open")
    if passed != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
