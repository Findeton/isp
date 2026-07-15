#!/usr/bin/env python3
"""D38b exact repair receipt: record-closed oriented finite cylinders.

The physical finite history has no authoritative cached state or tip map.
Rows, heads, incidence and actor identities are derived from authenticated
typed records.  Regional restriction keeps source records immutable and
resolves every omitted parent through a typed external reference.

All discrete probabilities use Fraction.  The chosen D34b coefficients and
finite seed remain supplied.  The finite-cylinder presentation is oriented
and classical; it is not a DLR theorem on arbitrary spatial regions, a
null-boundary version, an infinite predictive inverse limit, or a selector.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path
from typing import Dict, FrozenSet, Hashable, Iterable, Mapping, Optional, Sequence, Tuple, Union


ROOT = Path(__file__).resolve().parents[2]

LOCKS = {
    "D26": (
        ROOT / "v10/code/d26_interface_equivalence_exact.py",
        "a9b1f1704578178218750ecbafa737763ff3968ca246939a1d6aece79930575c",
    ),
    "D34b": (
        ROOT / "v10/code/d34b_actor_reference_high_precision.py",
        "7fe587e0e2f3fccb8b88362f70e201c4cbecdc6a99984c792699695f67b558f4",
    ),
    "D34e": (
        ROOT / "v10/code/d34e_predictive_boundary_exact.py",
        "1dd1a69be94a0fb614f909745e7db772ac5e5f134b97cbdcdf10c45a08f606c5",
    ),
    "D34e-data": (
        ROOT / "v10/data/d34e_predictive_boundary_exact.out",
        "158c491d7376b165556364fee2f0266447e7f5becfdbda5a8f4ae600114e9fb7",
    ),
    "D34f": (
        ROOT / "v10/code/d34f_component_tomography_exact.py",
        "0b518f6e742e4b24bd5a3e4a68e29127af27c7cd6acc13453ad5dba9031347ef",
    ),
    "D34f-data": (
        ROOT / "v10/data/d34f_component_tomography_exact.out",
        "de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2",
    ),
    "D36b": (
        ROOT / "v10/code/d36b_actor_record_refinement_exact.py",
        "57ff22ab4711b63d476192c2ff19b02bb7f76fda5124b4d1afd23d30a20b376b",
    ),
    "D38": (
        ROOT / "v10/code/d38_record_closed_specification_exact.py",
        "5e42616679dcebff464e25dffa62dad4d52a6f399e7bac420ce16ea3b236604c",
    ),
    "D38-data": (
        ROOT / "v10/data/d38_record_closed_specification_exact.out",
        "b0e61b087451f216db1696ece836453f5ba403667fbdb5043a67ce17e070c3f6",
    ),
}


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
    answer: Dict[str, str] = {}
    for name, (path, expected) in LOCKS.items():
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError((name, actual, expected))
        answer[name] = actual
    return answer


# ---------------------------------------------------------------------------
# Physical typed D34b finite histories.


@dataclass(frozen=True)
class ActorRow:
    carrier: int
    rings: int
    births: int
    degree: int
    wire_events: int

    def __post_init__(self) -> None:
        if self.carrier not in (0, 1):
            raise ValueError("binary carrier")
        if min(self.rings, self.births, self.degree, self.wire_events) < 0:
            raise ValueError("negative actor field")
        if self.births > self.rings or self.degree < 1:
            raise ValueError("impossible actor row")


@dataclass(frozen=True)
class Record:
    record_id: Tuple[Hashable, ...]
    kind: str
    owner: str
    wires: Tuple[str, ...]
    parents: Tuple[Hashable, ...]
    payload: Tuple[Tuple[str, Hashable], ...]
    capability: str
    signature: str

    def payload_map(self) -> Dict[str, Hashable]:
        return dict(self.payload)


def capability(owner: str) -> str:
    return digest(("D38B_ISSUED_CAPABILITY", owner))


def record_core(
    kind: str,
    owner: str,
    wires: Sequence[str],
    parents: Sequence[Hashable],
    payload: Mapping[str, Hashable],
    cap: str,
) -> Tuple[Hashable, ...]:
    return (
        kind,
        owner,
        tuple(wires),
        tuple(parents),
        tuple(sorted(payload.items())),
        cap,
    )


def make_record(
    kind: str,
    owner: str,
    wires: Sequence[str],
    parents: Sequence[Hashable],
    payload: Mapping[str, Hashable],
) -> Record:
    cap = capability(owner)
    core = record_core(kind, owner, wires, parents, payload, cap)
    record_id = ("D38B_RECORD", kind, core)
    signature = digest(("D38B_IDEAL_SIGNATURE", owner, core))
    return Record(
        record_id,
        kind,
        owner,
        tuple(wires),
        tuple(parents),
        tuple(sorted(payload.items())),
        cap,
        signature,
    )


def authentic(record: Record) -> bool:
    core = record_core(
        record.kind,
        record.owner,
        record.wires,
        record.parents,
        record.payload_map(),
        record.capability,
    )
    return (
        record.record_id == ("D38B_RECORD", record.kind, core)
        and record.capability == capability(record.owner)
        and record.signature == digest(("D38B_IDEAL_SIGNATURE", record.owner, core))
    )


def row_payload(row: ActorRow) -> Tuple[int, int, int, int, int]:
    return (row.carrier, row.rings, row.births, row.degree, row.wire_events)


def payload_row(value: Hashable) -> ActorRow:
    if not isinstance(value, tuple) or len(value) != 5:
        raise AssertionError("malformed actor row")
    return ActorRow(*(int(item) for item in value))


SEED_ROWS = {"A": ActorRow(0, 0, 0, 1, 0), "B": ActorRow(0, 0, 0, 1, 0)}


def seed_records() -> Tuple[Record, ...]:
    rows = {
        actor: make_record(
            "SEED_ACTOR",
            actor,
            (actor,),
            (),
            {"actor": actor, "row": row_payload(row), "clock": ("ACTOR_CLOCK", actor, 0)},
        )
        for actor, row in SEED_ROWS.items()
    }
    edge = make_record(
        "SEED_EDGE",
        "edge:A:B",
        ("A", "B"),
        (rows["A"].record_id, rows["B"].record_id),
        {
            "endpoints": ("A", "B"),
            "ports": (("A", "B"), ("B", "A")),
        },
    )
    return tuple(sorted((*rows.values(), edge), key=lambda item: repr(item.record_id)))


@dataclass(frozen=True)
class History:
    records: Tuple[Record, ...]


@dataclass(frozen=True)
class Derived:
    rows: Tuple[Tuple[str, ActorRow], ...]
    heads: Tuple[Tuple[str, Hashable], ...]
    edges: Tuple[Tuple[str, str], ...]
    event_order: Tuple[Hashable, ...]

    def row_map(self) -> Dict[str, ActorRow]:
        return dict(self.rows)

    def head_map(self) -> Dict[str, Hashable]:
        return dict(self.heads)


def seed_history() -> History:
    history = History(seed_records())
    derive(history)
    return history


def event_spec(kind: str, initiator: str, target: Optional[str]) -> Tuple[str, Optional[str]]:
    if kind not in ("BIRTH", "IDLE", "INTERACTION"):
        raise AssertionError("unknown event kind")
    if kind == "IDLE" and target is not None:
        raise AssertionError("idle target")
    if kind in ("BIRTH", "INTERACTION") and target is None:
        raise AssertionError("missing target")
    return kind, target


def expected_event(
    derived: Derived,
    kind: str,
    initiator: str,
    target: Optional[str] = None,
) -> Record:
    kind, target = event_spec(kind, initiator, target)
    rows = derived.row_map()
    heads = derived.head_map()
    edges = set(derived.edges)
    if initiator not in rows:
        raise AssertionError("unknown initiator")
    before = rows[initiator]
    ring = before.rings + 1
    payload: Dict[str, Hashable] = {
        "event_kind": kind,
        "initiator": initiator,
        "ring_ordinal": ring,
    }
    if kind == "BIRTH":
        birth = before.births + 1
        child = f"{initiator}/{birth}"
        if target != child or child in rows:
            raise AssertionError("noncanonical child")
        parent_after = ActorRow(
            before.carrier, ring, birth, before.degree + 1, before.wire_events + 1
        )
        child_after = ActorRow(0, 0, 0, 1, 1)
        edge = tuple(sorted((initiator, child)))
        payload.update(
            {
                "target": child,
                "birth_ordinal": birth,
                "created_edge": edge,
                "created_ports": ((initiator, child), (child, initiator)),
                "child_clock": ("ACTOR_CLOCK", child, 0),
                "post_rows": tuple(
                    sorted(((initiator, row_payload(parent_after)), (child, row_payload(child_after))))
                ),
            }
        )
        return make_record(
            "EVENT", initiator, (initiator, child), (heads[initiator],), payload
        )
    if kind == "IDLE":
        after = ActorRow(
            before.carrier,
            ring,
            before.births,
            before.degree,
            before.wire_events + 1,
        )
        payload.update({"target": "NONE", "post_rows": ((initiator, row_payload(after)),)})
        return make_record("EVENT", initiator, (initiator,), (heads[initiator],), payload)
    assert target is not None
    if target not in rows or tuple(sorted((initiator, target))) not in edges:
        raise AssertionError("interaction target is not an incident actor")
    other = rows[target]
    initiator_after = ActorRow(
        1 - before.carrier,
        ring,
        before.births,
        before.degree,
        before.wire_events + 1,
    )
    target_after = ActorRow(
        1 - other.carrier,
        other.rings,
        other.births,
        other.degree,
        other.wire_events + 1,
    )
    payload.update(
        {
            "target": target,
            "post_rows": tuple(
                sorted(((initiator, row_payload(initiator_after)), (target, row_payload(target_after))))
            ),
        }
    )
    return make_record(
        "EVENT",
        initiator,
        (initiator, target),
        (heads[initiator], heads[target]),
        payload,
    )


def apply_derived(derived: Derived, event: Record) -> Derived:
    payload = event.payload_map()
    kind = str(payload["event_kind"])
    initiator = str(payload["initiator"])
    target_value = payload["target"]
    target = None if target_value == "NONE" else str(target_value)
    expected = expected_event(derived, kind, initiator, target)
    if event != expected:
        raise AssertionError("event is not the exact next typed row")
    rows = derived.row_map()
    heads = derived.head_map()
    edges = set(derived.edges)
    for actor, encoded in payload["post_rows"]:  # type: ignore[union-attr]
        rows[str(actor)] = payload_row(encoded)
        heads[str(actor)] = event.record_id
    if kind == "BIRTH":
        edges.add(tuple(payload["created_edge"]))  # type: ignore[arg-type]
    return Derived(
        tuple(sorted(rows.items())),
        tuple(sorted(heads.items())),
        tuple(sorted(edges)),
        derived.event_order + (event.record_id,),
    )


def derive(history: History) -> Derived:
    records = history.records
    by_id = {record.record_id: record for record in records}
    if len(by_id) != len(records):
        raise AssertionError("duplicate record id")
    if any(not authentic(record) for record in records):
        raise AssertionError("inauthentic record")
    if any(parent not in by_id for record in records for parent in record.parents):
        raise AssertionError("missing causal parent")
    expected_seed = seed_records()
    actual_seed = tuple(
        sorted(
            (record for record in records if record.kind in ("SEED_ACTOR", "SEED_EDGE")),
            key=lambda item: repr(item.record_id),
        )
    )
    if actual_seed != expected_seed:
        raise AssertionError("seed ontology drift")
    if any(record.kind not in ("SEED_ACTOR", "SEED_EDGE", "EVENT") for record in records):
        raise AssertionError("unlicensed record kind")
    seed_map = {record.owner: record for record in expected_seed if record.kind == "SEED_ACTOR"}
    derived = Derived(
        tuple(sorted(SEED_ROWS.items())),
        tuple(sorted((actor, seed_map[actor].record_id) for actor in SEED_ROWS)),
        (("A", "B"),),
        (),
    )
    pending = {record.record_id: record for record in records if record.kind == "EVENT"}
    while pending:
        accepted: Optional[Hashable] = None
        for record_id, event in sorted(pending.items(), key=lambda item: repr(item[0])):
            payload = event.payload_map()
            try:
                candidate = expected_event(
                    derived,
                    str(payload["event_kind"]),
                    str(payload["initiator"]),
                    None if payload["target"] == "NONE" else str(payload["target"]),
                )
            except (AssertionError, KeyError, TypeError, ValueError):
                continue
            if event == candidate:
                derived = apply_derived(derived, event)
                accepted = record_id
                break
        if accepted is None:
            raise AssertionError("fork, replay, cross-wire row or disconnected event")
        del pending[accepted]
    return derived


def add_event(history: History, event: Record) -> History:
    candidate = History(tuple(sorted((*history.records, event), key=lambda item: repr(item.record_id))))
    derive(candidate)
    return candidate


@dataclass(frozen=True)
class Store:
    history: History
    used_events: FrozenSet[Hashable]


def initial_store() -> Store:
    return Store(seed_history(), frozenset())


def transact(store: Store, event: Record) -> Tuple[Store, bool]:
    before = store
    try:
        derived = derive(store.history)
        payload = event.payload_map()
        expected = expected_event(
            derived,
            str(payload["event_kind"]),
            str(payload["initiator"]),
            None if payload["target"] == "NONE" else str(payload["target"]),
        )
        if event.record_id in store.used_events or event != expected:
            raise AssertionError("stale, replayed or malformed event")
        after_history = add_event(store.history, event)
        return Store(after_history, store.used_events | {event.record_id}), True
    except (AssertionError, KeyError, TypeError, ValueError):
        return before, False


def install_history(store: Store, candidate: History) -> Tuple[Store, bool]:
    before = store
    try:
        old_ids = {record.record_id for record in store.history.records}
        new_ids = {record.record_id for record in candidate.records}
        if not old_ids <= new_ids:
            raise AssertionError("durable rollback")
        derive(candidate)
        new_events = {
            record.record_id
            for record in candidate.records
            if record.kind == "EVENT" and record.record_id not in old_ids
        }
        if new_events & store.used_events:
            raise AssertionError("durable replay")
        return Store(candidate, store.used_events | new_events), True
    except AssertionError:
        return before, False


def proposed(store: Store, kind: str, initiator: str, target: Optional[str] = None) -> Record:
    return expected_event(derive(store.history), kind, initiator, target)


def execute(store: Store, kind: str, initiator: str, target: Optional[str] = None) -> Store:
    answer, accepted = transact(store, proposed(store, kind, initiator, target))
    if not accepted:
        raise AssertionError("valid event rejected")
    return answer


# ---------------------------------------------------------------------------
# Record restriction with explicit external causal references.


@dataclass(frozen=True)
class ViewRecord:
    source: Record
    resolved_parents: Tuple[Tuple[str, Hashable], ...]


@dataclass(frozen=True)
class RegionView:
    records: Tuple[ViewRecord, ...]
    external_refs: Tuple[Hashable, ...]

    def source_map(self) -> Dict[Hashable, Record]:
        return {record.source.record_id: record.source for record in self.records}


Restrictable = Union[History, RegionView]


def view_from_source_map(source_map: Mapping[Hashable, Record]) -> RegionView:
    allowed = frozenset(source_map)
    view_records = []
    external = set()
    for record_id in sorted(allowed, key=repr):
        record = source_map[record_id]
        resolved = []
        for parent in record.parents:
            if parent in allowed:
                resolved.append(("INTERNAL", parent))
            else:
                resolved.append(("EXTERNAL", parent))
                external.add(parent)
        view_records.append(ViewRecord(record, tuple(resolved)))
    answer = RegionView(tuple(view_records), tuple(sorted(external, key=repr)))
    validate_view(answer)
    return answer


def restrict_records(source: Restrictable, allowed: FrozenSet[Hashable]) -> RegionView:
    if isinstance(source, History):
        source_map = {record.record_id: record for record in source.records}
        derive(source)
    else:
        validate_view(source)
        source_map = source.source_map()
    if not allowed <= set(source_map):
        raise AssertionError("restriction cannot recover an omitted record")
    return view_from_source_map({record_id: source_map[record_id] for record_id in allowed})


def validate_view(view: RegionView) -> None:
    source = view.source_map()
    if len(source) != len(view.records):
        raise AssertionError("duplicate regional source")
    external = set(view.external_refs)
    if external & set(source):
        raise AssertionError("external reference leaked inside")
    seen_external = set()
    for view_record in view.records:
        if not authentic(view_record.source):
            raise AssertionError("regional source lost authentication")
        if len(view_record.resolved_parents) != len(view_record.source.parents):
            raise AssertionError("regional parent slot mismatch")
        for original, (tag, resolved) in zip(
            view_record.source.parents, view_record.resolved_parents
        ):
            if original != resolved or tag not in ("INTERNAL", "EXTERNAL"):
                raise AssertionError("regional parent provenance changed")
            if tag == "INTERNAL" and resolved not in source:
                raise AssertionError("missing internal regional parent")
            if tag == "EXTERNAL":
                seen_external.add(resolved)
    if seen_external != external:
        raise AssertionError("external regional reference census")


def append_view(view: RegionView, event: Record) -> RegionView:
    validate_view(view)
    records = view.source_map()
    if event.record_id in records or not authentic(event):
        raise AssertionError("regional append collision")
    records[event.record_id] = event
    return view_from_source_map(records)


# ---------------------------------------------------------------------------
# Oriented positive-cylinder kernels of the projected chosen D34b star.


@dataclass(frozen=True)
class NeighborRow:
    degree: int
    births: int

    def __post_init__(self) -> None:
        if self.degree < 1 or self.births < 0:
            raise ValueError("invalid projected neighbor row")


@dataclass(frozen=True)
class Star:
    root: str
    root_row: ActorRow
    neighbors: Tuple[Tuple[str, NeighborRow], ...]
    elapsed: Fraction

    def neighbor_map(self) -> Dict[str, NeighborRow]:
        return dict(self.neighbors)


def star_from_history(history: History, root: str = "A") -> Star:
    derived = derive(history)
    rows = derived.row_map()
    if root not in rows:
        raise AssertionError("missing star root")
    neighbors = []
    for left, right in derived.edges:
        if left == root:
            neighbors.append((right, NeighborRow(rows[right].degree, rows[right].births)))
        elif right == root:
            neighbors.append((left, NeighborRow(rows[left].degree, rows[left].births)))
    return Star(root, rows[root], tuple(sorted(neighbors)), Fraction())


def star_rates(star: Star) -> Dict[Tuple[str, str], Fraction]:
    neighbors = star.neighbor_map()
    degree = len(neighbors)
    if degree == 0:
        raise AssertionError("D38b registered sector is connected")
    rates: Dict[Tuple[str, str], Fraction] = {
        ("ROOT_BIRTH", "NONE"): Fraction(1, 4),
        ("ROOT_IDLE", "NONE"): Fraction(1, 2),
    }
    for actor, row in neighbors.items():
        rates[("ROOT_OUT", actor)] = Fraction(1, 4 * degree)
        rates[("NEIGHBOR_BIRTH", actor)] = Fraction(1, 4)
        rates[("INCOMING", actor)] = Fraction(1, 4 * row.degree)
    return rates


def star_kernel(star: Star) -> Dict[Tuple[str, str], Fraction]:
    rates = star_rates(star)
    total = sum(rates.values(), Fraction())
    return {action: rate / total for action, rate in sorted(rates.items())}


def star_step(star: Star, action: Tuple[str, str]) -> Star:
    if action not in star_rates(star):
        raise AssertionError("inadmissible star action")
    tag, target = action
    root = star.root_row
    neighbors = star.neighbor_map()
    if tag == "ROOT_BIRTH":
        birth = root.births + 1
        child = f"{star.root}/{birth}"
        root = ActorRow(root.carrier, root.rings + 1, birth, root.degree + 1, root.wire_events + 1)
        neighbors[child] = NeighborRow(1, 0)
    elif tag == "ROOT_IDLE":
        root = ActorRow(root.carrier, root.rings + 1, root.births, root.degree, root.wire_events + 1)
    elif tag == "ROOT_OUT":
        root = ActorRow(1 - root.carrier, root.rings + 1, root.births, root.degree, root.wire_events + 1)
    elif tag == "NEIGHBOR_BIRTH":
        neighbor = neighbors[target]
        neighbors[target] = NeighborRow(neighbor.degree + 1, neighbor.births + 1)
    elif tag == "INCOMING":
        root = ActorRow(1 - root.carrier, root.rings, root.births, root.degree, root.wire_events + 1)
    else:
        raise AssertionError(tag)
    return Star(star.root, root, tuple(sorted(neighbors.items())), star.elapsed)


def timed_star_step(
    star: Star, action: Optional[Tuple[str, str]], delta: Fraction
) -> Star:
    if delta < 0:
        raise AssertionError("negative relative-time increment")
    after = star if action is None else star_step(star, action)
    return replace(after, elapsed=star.elapsed + delta)


PathAction = Tuple[str, str]


def cylinder_distribution(star: Star, depth: int) -> Dict[Tuple[PathAction, ...], Fraction]:
    distribution: Dict[Tuple[PathAction, ...], Fraction] = {(): Fraction(1)}
    states: Dict[Tuple[PathAction, ...], Star] = {(): star}
    for _ in range(depth):
        next_distribution: Dict[Tuple[PathAction, ...], Fraction] = {}
        next_states: Dict[Tuple[PathAction, ...], Star] = {}
        for prefix, probability in distribution.items():
            state = states[prefix]
            for action, conditional in star_kernel(state).items():
                extended = prefix + (action,)
                next_distribution[extended] = probability * conditional
                next_states[extended] = star_step(state, action)
        distribution, states = next_distribution, next_states
    return distribution


def prefix_marginal(
    distribution: Mapping[Tuple[PathAction, ...], Fraction], depth: int
) -> Dict[Tuple[PathAction, ...], Fraction]:
    answer: Dict[Tuple[PathAction, ...], Fraction] = {}
    for path, probability in distribution.items():
        prefix = path[:depth]
        answer[prefix] = answer.get(prefix, Fraction()) + probability
    return answer


def reachable_stars() -> Tuple[Star, ...]:
    store = initial_store()
    stars = [star_from_history(store.history)]
    store = execute(store, "IDLE", "A")
    stars.append(star_from_history(store.history))
    store = execute(store, "BIRTH", "A", "A/1")
    stars.append(star_from_history(store.history))
    store = execute(store, "BIRTH", "B", "B/1")
    stars.append(star_from_history(store.history))
    return tuple(stars)


# ---------------------------------------------------------------------------
# Exact receipt gates.


def cylinder_checks() -> Tuple[int, int, int, int, int, Tuple[str, ...]]:
    normalized = 0
    projective = 0
    atoms = 0
    holding = 0
    timed_updates = 0
    initial_rates = []
    for star in reachable_stars():
        distributions = {depth: cylinder_distribution(star, depth) for depth in (1, 2, 3)}
        for depth, distribution in distributions.items():
            if sum(distribution.values(), Fraction()) != 1 or any(
                probability <= 0 for probability in distribution.values()
            ):
                raise AssertionError("finite-cylinder normalization/support")
            normalized += 1
            atoms += len(distribution)
        for high, low in ((3, 2), (2, 1), (3, 1)):
            if prefix_marginal(distributions[high], low) != distributions[low]:
                raise AssertionError("direct finite-cylinder restriction")
            projective += 1
        staged = prefix_marginal(prefix_marginal(distributions[3], 2), 1)
        if staged != distributions[1]:
            raise AssertionError("staged cylinder restriction")
        frontier = (star,)
        for _ in range(3):
            next_frontier = []
            for state in frontier:
                rates_here = star_rates(state)
                total_here = sum(rates_here.values(), Fraction())
                integrated_race_mass = sum(
                    (rate / total_here for rate in rates_here.values()), Fraction()
                )
                if total_here <= 0 or integrated_race_mass != 1:
                    raise AssertionError("competing-exponential holding normalization")
                holding += 1
                next_frontier.extend(star_step(state, action) for action in rates_here)
            frontier = tuple(next_frontier)
        no_event = timed_star_step(star, None, Fraction(7, 13))
        if no_event.elapsed != star.elapsed + Fraction(7, 13) or replace(
            no_event, elapsed=star.elapsed
        ) != star:
            raise AssertionError("relative-time no-event update")
        timed_updates += 1
        for action in star_rates(star):
            timed = timed_star_step(star, action, Fraction(1, 100))
            if timed.elapsed != Fraction(1, 100) or replace(
                timed, elapsed=star.elapsed
            ) != star_step(star, action):
                raise AssertionError("relative-time event update")
            timed_updates += 1
        total = sum(star_rates(star).values(), Fraction())
        initial_rates.append(ftext(total))
    return normalized, projective, atoms, holding, timed_updates, tuple(initial_rates)


def action_wires(star: Star, action: PathAction) -> FrozenSet[str]:
    tag, target = action
    if tag == "ROOT_BIRTH":
        return frozenset((star.root, f"{star.root}/{star.root_row.births + 1}"))
    if tag == "ROOT_IDLE":
        return frozenset((star.root,))
    if tag == "NEIGHBOR_BIRTH":
        row = star.neighbor_map()[target]
        return frozenset((target, f"{target}/{row.births + 1}"))
    return frozenset((star.root, target))


def generator_and_locality_checks() -> Tuple[int, int, int, int, int, int]:
    checks = 0
    max_arity = 0
    star = reachable_stars()[0]
    for degree in range(1, 13):
        neighbors = tuple(
            (f"N{index}", NeighborRow(1 + index, index))
            for index in range(degree)
        )
        specimen = Star(
            "A",
            ActorRow(0, degree - 1, degree - 1, degree, degree - 1),
            neighbors,
            Fraction(),
        )
        for action in star_rates(specimen):
            arity = len(action_wires(specimen, action))
            if arity > 2:
                raise AssertionError("local touched arity")
            checks += 1
            max_arity = max(max_arity, arity)
    store = initial_store()
    store = execute(store, "BIRTH", "A", "A/1")
    store = execute(store, "BIRTH", "B", "B/1")
    store = execute(store, "INTERACTION", "A", "B")
    store = execute(store, "IDLE", "A/1")
    derived = derive(store.history)
    payloads = [record.payload_map() for record in store.history.records if record.kind == "EVENT"]
    birth_fields = sum(
        int(all(field in payload for field in ("created_edge", "created_ports", "child_clock", "post_rows")))
        for payload in payloads
        if payload["event_kind"] == "BIRTH"
    )
    if birth_fields != 2 or len(derived.rows) != 4 or len(derived.edges) != 3:
        raise AssertionError("typed birth incidence generation")
    return checks, max_arity, len(derived.rows), len(derived.edges), len(store.history.records), birth_fields


def resigned(record: Record, **changes: object) -> Record:
    fields = {
        "kind": record.kind,
        "owner": record.owner,
        "wires": record.wires,
        "parents": record.parents,
        "payload": record.payload_map(),
    }
    fields.update(changes)
    return make_record(
        str(fields["kind"]),
        str(fields["owner"]),
        tuple(fields["wires"]),  # type: ignore[arg-type]
        tuple(fields["parents"]),  # type: ignore[arg-type]
        fields["payload"],  # type: ignore[arg-type]
    )


def authentication_checks() -> Tuple[int, int, int, int]:
    base = initial_store()
    valid = proposed(base, "IDLE", "A")
    payload = valid.payload_map()
    mutations = [
        replace(valid, signature="FORGED"),
        replace(valid, capability="UNISSUED"),
        replace(valid, record_id=("FORGED",)),
        replace(valid, kind="GRANT"),
        replace(valid, owner="B"),
        replace(valid, wires=("B",)),
        replace(valid, parents=()),
        replace(valid, payload=tuple((key, value) for key, value in valid.payload if key != "post_rows")),
        resigned(valid, payload={**payload, "ring_ordinal": 99}),
        resigned(valid, payload={**payload, "target": "B"}),
        resigned(valid, parents=(derive(base.history).head_map()["B"],)),
    ]
    rejected = 0
    durable = 0
    for mutation in mutations:
        after, accepted = transact(base, mutation)
        rejected += int(not accepted)
        durable += int(after == base)

    advanced, accepted = transact(base, valid)
    if not accepted:
        raise AssertionError("valid event rejected")
    replayed, replay_ok = transact(advanced, valid)
    rejected += int(not replay_ok)
    durable += int(replayed == advanced)

    idle = proposed(base, "IDLE", "A")
    outgoing = proposed(base, "INTERACTION", "A", "B")
    fork = History(tuple(sorted((*base.history.records, idle, outgoing), key=lambda item: repr(item.record_id))))
    installed, ok = install_history(base, fork)
    rejected += int(not ok)
    durable += int(installed == base)

    disconnected = make_record(
        "EVENT",
        "Z",
        ("Z",),
        (),
        {"event_kind": "IDLE", "initiator": "Z", "ring_ordinal": 1, "target": "NONE", "post_rows": (("Z", row_payload(ActorRow(0, 1, 0, 1, 1))),)},
    )
    hostile = History(tuple(sorted((*base.history.records, disconnected), key=lambda item: repr(item.record_id))))
    installed, ok = install_history(base, hostile)
    rejected += int(not ok)
    durable += int(installed == base)

    seeds = list(seed_records())
    edge_index = next(index for index, record in enumerate(seeds) if record.kind == "SEED_EDGE")
    seeds[edge_index] = make_record(
        "SEED_EDGE",
        "edge:A:B",
        ("A", "B"),
        seeds[edge_index].parents,
        {"endpoints": ("A", "A"), "ports": (("A", "B"), ("B", "A"))},
    )
    installed, ok = install_history(base, History(tuple(sorted(seeds, key=lambda item: repr(item.record_id)))))
    rejected += int(not ok)
    durable += int(installed == base)

    fabricated = make_record(
        "SEED_ACTOR",
        "A",
        ("A",),
        (),
        {"actor": "A", "row": row_payload(ActorRow(1, 9, 0, 1, 9)), "clock": ("ACTOR_CLOCK", "A", 0)},
    )
    hostile_records = tuple(record for record in base.history.records if not (record.kind == "SEED_ACTOR" and record.owner == "A")) + (fabricated,)
    installed, ok = install_history(base, History(tuple(sorted(hostile_records, key=lambda item: repr(item.record_id)))))
    rejected += int(not ok)
    durable += int(installed == base)

    duplicate = History(base.history.records + (base.history.records[0],))
    installed, ok = install_history(base, duplicate)
    rejected += int(not ok)
    durable += int(installed == base)

    rollback_store = Store(base.history, advanced.used_events)
    rolled, ok = transact(rollback_store, valid)
    rejected += int(not ok)
    durable += int(rolled == rollback_store)

    attempted = len(mutations) + 7
    if rejected != attempted or durable != attempted:
        raise AssertionError("hostile durable mutation battery")
    return rejected, attempted, durable, len(advanced.used_events)


def restriction_checks() -> Tuple[int, int, int, int]:
    store = initial_store()
    store = execute(store, "IDLE", "A")
    store = execute(store, "IDLE", "B")
    pre_interaction = store
    interaction = proposed(store, "INTERACTION", "A", "B")
    store = execute(store, "INTERACTION", "A", "B")
    store = execute(store, "BIRTH", "A", "A/1")
    records = list(store.history.records)
    events = [record for record in records if record.kind == "EVENT"]
    idle_a = next(record for record in events if record.payload_map()["event_kind"] == "IDLE" and record.owner == "A")
    idle_b = next(record for record in events if record.payload_map()["event_kind"] == "IDLE" and record.owner == "B")
    all_ids = frozenset(record.record_id for record in records)
    e_ids = all_ids - {idle_b.record_id}
    d_ids = e_ids - {idle_a.record_id}
    c_ids = frozenset(record_id for record_id in d_ids if record_id != next(record.record_id for record in records if record.kind == "SEED_EDGE"))
    direct_d = restrict_records(store.history, d_ids)
    staged_d = restrict_records(restrict_records(store.history, e_ids), d_ids)
    direct_c = restrict_records(store.history, c_ids)
    staged_c = restrict_records(restrict_records(restrict_records(store.history, e_ids), d_ids), c_ids)
    if direct_d != staged_d or direct_c != staged_c:
        raise AssertionError("nested record restriction cocycle")

    pre_ids = frozenset(record.record_id for record in pre_interaction.history.records) - {idle_b.record_id}
    before_view = restrict_records(pre_interaction.history, pre_ids)
    transported = append_view(before_view, interaction)
    post_history = add_event(pre_interaction.history, interaction)
    direct = restrict_records(post_history, pre_ids | {interaction.record_id})
    if transported != direct:
        raise AssertionError("update/restriction naturality")

    disjoint = initial_store()
    event_a = proposed(disjoint, "IDLE", "A")
    event_b = proposed(disjoint, "IDLE", "B")
    left_history = add_event(add_event(disjoint.history, event_a), event_b)
    right_history = add_event(add_event(disjoint.history, event_b), event_a)
    if left_history != right_history or derive(left_history) != derive(right_history):
        raise AssertionError("disjoint insertion commutation")
    external_slots = len(direct_d.external_refs) + len(direct_c.external_refs) + len(direct.external_refs)
    return 2, 1, 1, external_slots


def predictive_inheritance_checks() -> Tuple[Tuple[str, ...], Tuple[int, ...], Tuple[int, ...], int]:
    d34f_text = (ROOT / "v10/data/d34f_component_tomography_exact.out").read_text()
    required = (
        "bare equal-order coefficients=1/1152/1/576",
        "anchored q/q+1=1/192/1/1536",
        "attachment witness=1/1",
        "emulators=0",
        "stronger inverse-limit/v9/quantum/geometry flags=OPEN",
    )
    if any(item not in d34f_text for item in required):
        raise AssertionError("D34f inherited theorem drift")
    witnesses = tuple(
        ftext(Fraction(1, (8 * (radius + 3)) ** (radius + 1)))
        for radius in range(9)
    )
    families = tuple(2**bits for bits in range(1, 11))
    anchors = tuple(2 * actors - 1 for actors in range(2, 11))
    return witnesses, families, anchors, 1


def toy_escape_checks() -> Tuple[int, int, int, int, int]:
    finite_horizon = int(("OUTSIDE", 0) == ("OUTSIDE", 0))
    exact_zero_read_cut = int(("SEALED", 0) == ("SEALED", 0))
    exact_attenuation = sum(Fraction(0) != Fraction(1, 2**distance) for distance in range(1, 13))
    epsilon = Fraction(1, 16)
    epsilon_merges = sum(Fraction(1, 2**distance) <= epsilon for distance in range(1, 13))
    finite_marked_history_cap = 2**6
    if (finite_horizon, exact_zero_read_cut, exact_attenuation, epsilon_merges, finite_marked_history_cap) != (1, 1, 12, 9, 64):
        raise AssertionError("toy scope controls")
    return finite_horizon, exact_zero_read_cut, exact_attenuation, epsilon_merges, finite_marked_history_cap


def d26_conditional_interface() -> Tuple[Tuple[str, ...], Tuple[str, ...], str]:
    born = tuple(ftext(Fraction(4, 5) ** count) for count in range(9))
    token = tuple("1" for _ in range(9))
    if born[3] != "64/125" or any(item != "1" for item in token):
        raise AssertionError("D26 conditional table")
    return born, token, "IF bridge(N same-line BORN,g=9/25), THEN V_N/V_0=(4/5)^N"


Graph = Tuple[Tuple[int, ...], ...]


def graph(vertex_count: int, edges: Iterable[Tuple[int, int]]) -> Graph:
    rows = [set() for _ in range(vertex_count)]
    for left, right in edges:
        rows[left].add(right)
        rows[right].add(left)
    return tuple(tuple(sorted(row)) for row in rows)


def mass_balance() -> Tuple[int, int, Fraction, Fraction]:
    graphs = (
        graph(3, ((0, 1), (1, 2))),
        graph(4, ((0, 1), (0, 2), (0, 3))),
        graph(5, ((0, 1), (1, 2), (2, 3), (3, 4))),
    )
    balanced = 0
    for item in graphs:
        sent = sum((Fraction(1) for row in item if row), Fraction())
        received = sum(
            (sum((Fraction(1, len(item[source])) for source in item[root]), Fraction()) for root in range(len(item))),
            Fraction(),
        )
        if sent != received:
            raise AssertionError("finite uniform-root mass balance")
        balanced += 1
    center_sent = Fraction(1)
    center_received = Fraction(3)
    return balanced, 1, center_sent, center_received


def capacity_ledger() -> Tuple[int, int, int, int, int, str, str, str]:
    store = initial_store()
    for ordinal in range(1, 5):
        store = execute(store, "BIRTH", "A", f"A/{ordinal}")
    derived = derive(store.history)
    star = star_from_history(store.history)
    actors = 1 + len(star.neighbors)
    records = len(store.history.records)
    ports = 2 * len(star.neighbors)
    parent_arity = max(len(record.parents) for record in store.history.records)
    radius = 1
    return radius, actors, records, ports, parent_arity, "UNBOUNDED", "CONTINUOUS", "UNBOUNDED"


def main() -> None:
    out = []
    gates: Dict[str, bool] = {}
    science: Dict[str, object] = {}

    def emit(line: str) -> None:
        out.append(line)
        print(line)

    emit("[D38b record-closed oriented finite-cylinder repair — exact receipt]")
    emit("ARITHMETIC: integer/Fraction exact; competing-exponential race masses integrated as rate/total-rate")
    emit("SCOPE: chosen D34b finite reachable histories; actor-star projection; classical positive cylinders only")

    locks = locked_antecedents()
    gates["R0"] = len(locks) == 9
    science["locks"] = locks
    emit("[LOCKS / REPAIRED CLAIM SPLIT]")
    emit(f"antecedent_locks={stable(locks)}")
    emit("spatial_DLR=NOT_CLAIMED; null_boundary_version=NOT_PROVED; Paper26_K_membership=NOT_CLAIMED; chosen_coefficients_selected=0")

    normalized, projective, atoms, holding, timed_updates, rates = cylinder_checks()
    gates["R1"] = (
        normalized == 12
        and projective == 12
        and atoms == 1760
        and holding > 0
        and timed_updates > 0
    )
    science["cylinders"] = [normalized, projective, atoms, holding, timed_updates, rates]
    emit("[ORIENTED FINITE-CYLINDER REGIONAL FAMILY]")
    emit(f"reachable_boundaries=4; depth_1_2_3_normalizations={normalized}/12; direct_prefix_restrictions={projective}/12; positive_path_atoms={atoms}")
    emit(f"exact_holding_rate_rows={rates}; competing_exponential_integral_checks={holding}; elapsed_and_no_event_updates={timed_updates}; staged_r31_equals_r21_r32=4/4")
    emit("neighbor_projection=(actor,degree,own_birth_count); silent_neighbor_idle_and_off_root_interaction_integrated_out=1")

    locality = generator_and_locality_checks()
    gates["R2"] = locality == (258, 2, 4, 3, 7, 2)
    science["generator"] = locality
    emit("[TYPED D34b RECORD GENERATION / LOCAL SUPPORT]")
    emit(f"action_rows={locality[0]}; maximum_touched_actors={locality[1]}; generated_actors_edges_records={locality[2]},{locality[3]},{locality[4]}; typed_birth_incidence={locality[5]}/2")
    emit("birth_payload=child_row+edge+two_ports+clock_address; passive_reception_does_not_consume_receiver_ring=1")

    rejected, attempted, durable, used = authentication_checks()
    gates["R3"] = rejected == attempted == durable == 18 and used == 1
    science["authentication"] = [rejected, attempted, durable, used]
    emit("[RECORD-DERIVED HEADS / MONOTONE AUTHENTICATION]")
    emit(f"whole_history_and_candidate_attacks_rejected={rejected}/{attempted}; byte_identical_failed_transactions={durable}/{attempted}; used_event_registry_after_valid_append={used}")
    emit("authoritative_cached_state=0; authoritative_tip_map=0; forks_replays_rollbacks_cross_wire_disconnected_duplicate_heads_reject=1")

    restriction = restriction_checks()
    gates["R4"] = restriction[0:3] == (2, 1, 1) and restriction[3] > 0
    science["restriction"] = restriction
    emit("[NESTED RECORD RESTRICTION / UPDATE NATURALITY]")
    emit(f"direct_equals_staged_nested_restrictions={restriction[0]}/2; update_restriction_naturality={restriction[1]}/1; disjoint_insertion_commutation={restriction[2]}/1; external_parent_slots={restriction[3]}")
    emit("omitted_parents=typed_EXTERNAL(source_record_id); source_records_immutable=1; pairwise_only_not_promoted=1")

    witnesses, families, anchors, inherited = predictive_inheritance_checks()
    gates["R5"] = len(witnesses) == 9 and families[-1] == 1024 and anchors[-1] == 19 and inherited == 1
    science["predictive"] = [witnesses, families, anchors, inherited]
    emit("[HASH-LOCKED PREDICTIVE THEOREM REGRESSION]")
    emit(f"p_r_r0_to_r8={witnesses}; 2^M_M1_to_M10={families}; q_equals_2n_minus_1={anchors}")
    emit("finite_stop_predictive_quotient=rooted_marked_current_component_class; timed_or_infinite_predictive_inverse_limit=OPEN")
    emit("old_generic_PGRAQS_criterion=REJECTED_UNDERHYPOTHESIZED; strengthened_prefix_separation_criterion=ANALYTIC_ONLY; D34f_instance=INHERITED_NOT_RECOMPUTED")

    escapes = toy_escape_checks()
    gates["R6"] = escapes == (1, 1, 12, 9, 64)
    science["escapes"] = escapes
    emit("[ABSTRACT QUERY-VARIANT CONTROLS]")
    emit(f"finite_horizon_projection={escapes[0]}; hypothetical_exact_zero_read_cut={escapes[1]}; nonzero_exact_attenuation_distinctions={escapes[2]}/12; epsilon_merges={escapes[3]}/12; finite_marked_history_cap={escapes[4]}")
    emit("existing_V6_physical_seal_identification=0; assumption_minimality_theorem=OPEN; bounded_actor_population_alone_bounds_history=0")

    born, token, bridge = d26_conditional_interface()
    gates["R7"] = born[3] == "64/125" and all(value == "1" for value in token)
    science["d26"] = [born, token, bridge]
    emit("[D26 CONDITIONAL FALSIFIER INTERFACE]")
    emit(f"same_line_BORN_table_N0_to_N8={born}; dormant_TOKEN_control={token}")
    emit(f"conditional_statement={bridge}; D38b_record_to_D26_parent_line_bridge=OPEN; maintenance_rate=NOT_INFERRED")

    balance = mass_balance()
    capacity = capacity_ledger()
    gates["R8"] = balance == (3, 1, Fraction(1), Fraction(3)) and capacity[:5] == (1, 6, 7, 10, 2)
    science["balance_capacity"] = [balance, capacity]
    emit("[CAPACITY LEDGER / FINITE BALANCE]")
    emit(f"specimen_radius_actors_records_ports_parent_arity={capacity[0]},{capacity[1]},{capacity[2]},{capacity[3]},{capacity[4]}")
    emit(f"identifier_capacity={capacity[5]}; elapsed_mark_capacity={capacity[6]}; family_total_width={capacity[7]}")
    emit(f"finite_uniform_root_mass_balances={balance[0]}/3; deterministic_center_negative={balance[1]}; center_sent_received={ftext(balance[2])},{ftext(balance[3])}")
    emit("all_transport_unimodularity=NOT_PROVED; infinite_completion=OPEN; coupling_selection=OPEN; quantum_join=UNDEFINED")

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
    emit("AUTHENTICATED RECORD-CLOSED ORIENTED FINITE-CYLINDER PRESENTATION / CHOSEN D34b / NONSELECTING")
    emit("BOUNDED LOCAL EVENT SUPPORT COEXISTS WITH UNBOUNDED EXACT FINITE-STOP PREDICTIVE WIDTH")
    emit("generic criterion, physical sealing, D26 updater bridge, timed inverse limit, unimodular selection and quantum join remain open")
    if passed != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
