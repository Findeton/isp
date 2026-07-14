#!/usr/bin/env python3
"""D35b capability-authenticated actor repair for the timeless call family.

This companion hash-locks the reviewed D35 recursive/quantum primitives and
rebuilds the message realization with actor-owned mailboxes and outstanding
calls.  Query routes, evidence payloads, typed legs and orthogonal event flags
are retained as physical provenance.  All probabilities and matrices are
exact Fractions; no time variable or global opportunity normalizer appears.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import itertools
import json
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List, Mapping, Optional, Sequence, Tuple, Union


getcontext().prec = 120
HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "d35_timeless_causal_actor_exact.py"
BASE_SHA256 = "06c997a195294991293fdedc9edce005a3f8ad1d23bfd8f73a5a08490163fa26"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


if sha256(BASE_PATH.read_bytes()) != BASE_SHA256:
    raise RuntimeError("D35 base source hash mismatch")
_SPEC = importlib.util.spec_from_file_location("d35_base_locked", BASE_PATH)
assert _SPEC and _SPEC.loader
base = importlib.util.module_from_spec(_SPEC)
sys.modules["d35_base_locked"] = base
_SPEC.loader.exec_module(base)


Params = base.Params
Q1 = base.Q1
Q2 = base.Q2


Address = Tuple[int, ...]


def freeze(value: object) -> object:
    if isinstance(value, Fraction):
        return ["Fraction", value.numerator, value.denominator]
    if isinstance(value, Mapping):
        return [
            [freeze(key), freeze(item)]
            for key, item in sorted(value.items(), key=lambda pair: repr(pair[0]))
        ]
    if isinstance(value, (tuple, list)):
        return [freeze(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [freeze(item) for item in sorted(value, key=repr)]
    return value


def digest(value: object) -> str:
    blob = json.dumps(freeze(value), separators=(",", ":"), sort_keys=True, default=str)
    return sha256(blob.encode("utf-8"))


def frac_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def dec_text(value: Fraction, places: int = 50) -> str:
    out = Decimal(value.numerator) / Decimal(value.denominator)
    return f"{out:.{places}f}"


def address_text(address: Address) -> str:
    return "root" if not address else ".".join(map(str, address))


def event_storage_id(namespace: str, tx: int, path: Tuple[int, ...]) -> str:
    suffix = "r" if not path else ".".join(map(str, path))
    return f"{namespace}::E{tx}:{suffix}"


def newborn_storage_id(namespace: str, tx: int, path: Tuple[int, ...]) -> str:
    suffix = "r" if not path else ".".join(map(str, path))
    return f"{namespace}::N{tx}:{suffix}"


def base_tx_tag(namespace: str, tx: int) -> str:
    return f"{namespace}::T{tx}"


@dataclass(frozen=True)
class Capability:
    cap_id: str
    namespace: str
    tx: int
    root_event: str
    requester_address: Optional[Address]
    requester_lower: str
    target_address: Address
    port: Optional[int]
    path: Tuple[int, ...]
    slot: Optional[int]
    parent_call: Optional[str]
    parent_cap: Optional[str]
    route: Tuple[Address, ...]
    payload: int
    signature: str


@dataclass(frozen=True)
class QueryEnvelope:
    capability: Capability


@dataclass(frozen=True)
class ReturnEnvelope:
    capability: Capability
    result_event: str
    result_actor: Address
    evidence_digest: str
    signature: str


Envelope = Union[QueryEnvelope, ReturnEnvelope]


@dataclass
class OwnedCall:
    call_id: str
    incoming: Capability
    action: str
    target_ports: Tuple[int, ...]
    child_caps: Dict[int, Capability]
    results: Dict[int, ReturnEnvelope] = field(default_factory=dict)


@dataclass
class LocalActor:
    name: str
    address: Address
    parent_address: Optional[Address]
    parent_port: Optional[int]
    children: Dict[int, Address]
    tip: str
    component: str
    mailbox: List[Envelope] = field(default_factory=list)
    outstanding: Dict[str, OwnedCall] = field(default_factory=dict)
    used_capabilities: set = field(default_factory=set)
    edge_keys: Dict[Address, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Provenance:
    event: str
    namespace: str
    tx: int
    event_address: Tuple[int, ...]
    initiator: Address
    target_legs: Tuple[Tuple[str, Address, int], ...]
    operation: str
    coupling: str
    capability: str
    route: Tuple[Address, ...]
    payload: int
    evidence_digest: str
    flag_factor: Tuple[object, ...]


@dataclass(frozen=True)
class TransferRecord:
    cap_id: str
    namespace: str
    tx: int
    requester: Optional[Address]
    target: Address
    port: Optional[int]
    root_event: str
    requester_lower: str
    parent_cap: Optional[str]
    route: Tuple[Address, ...]
    payload: int


@dataclass
class Network:
    namespace: str
    root_address: Address
    root_actor: str
    root_key: str
    actors: Dict[Address, LocalActor]
    name_to_address: Dict[str, Address]
    collector: base.World
    provenance: Dict[str, Provenance] = field(default_factory=dict)
    transfers: Dict[str, TransferRecord] = field(default_factory=dict)
    root_result: Optional[str] = None
    root_payload: int = 0
    current_tx: int = 0
    rejected: int = 0

    def clone(self) -> "Network":
        return copy.deepcopy(self)

    def actor(self, address: Address) -> LocalActor:
        return self.actors[address]

    def sync_tips(self, names: Iterable[str]) -> None:
        for name in names:
            address = self.name_to_address[name]
            self.actors[address].tip = self.collector.actors[name].tip

    def pending_count(self) -> int:
        return sum(len(actor.mailbox) for actor in self.actors.values())

    def outstanding_count(self) -> int:
        return sum(len(actor.outstanding) for actor in self.actors.values())


def edge_key(namespace: str, parent: Address, port: int, child: Address) -> str:
    return digest(("edge-key", namespace, parent, port, child))


def root_key(namespace: str) -> str:
    return digest(("root-key", namespace))


def cap_public(
    namespace: str,
    tx: int,
    root_event: str,
    requester_address: Optional[Address],
    requester_lower: str,
    target_address: Address,
    port: Optional[int],
    path: Tuple[int, ...],
    slot: Optional[int],
    parent_call: Optional[str],
    parent_cap: Optional[str],
    route: Tuple[Address, ...],
    payload: int,
) -> Tuple[object, ...]:
    return (
        namespace,
        tx,
        root_event,
        requester_address,
        requester_lower,
        target_address,
        port,
        path,
        slot,
        parent_call,
        parent_cap,
        route,
        payload,
    )


def make_capability(
    secret: str,
    namespace: str,
    tx: int,
    root_event: str,
    requester_address: Optional[Address],
    requester_lower: str,
    target_address: Address,
    port: Optional[int],
    path: Tuple[int, ...],
    slot: Optional[int],
    parent_call: Optional[str],
    parent_cap: Optional[str],
    route: Tuple[Address, ...],
    payload: int,
) -> Capability:
    public = cap_public(
        namespace,
        tx,
        root_event,
        requester_address,
        requester_lower,
        target_address,
        port,
        path,
        slot,
        parent_call,
        parent_cap,
        route,
        payload,
    )
    signature = digest(("query-signature", secret, public))
    cap_id = digest(("query-capability", public, signature))
    return Capability(
        cap_id,
        namespace,
        tx,
        root_event,
        requester_address,
        requester_lower,
        target_address,
        port,
        path,
        slot,
        parent_call,
        parent_cap,
        route,
        payload,
        signature,
    )


def return_signature(secret: str, capability: Capability, event: str, evidence: str) -> str:
    return digest(("return-signature", secret, capability.cap_id, event, evidence))


def renamed_base_world(params: Params, mapping: Mapping[str, str]) -> base.World:
    world = base.initial_world(params)
    actors: Dict[str, base.Actor] = {}
    for old, actor in world.actors.items():
        name = mapping[old]
        actors[name] = base.Actor(
            name,
            mapping[actor.parent] if actor.parent else None,
            [mapping[child] for child in actor.children],
            actor.tip,
        )
    events = {}
    for name, event in world.events.items():
        events[name] = base.Event(
            event.name,
            event.kind,
            tuple(sorted(mapping[actor] for actor in event.actors)),
            event.predecessors,
            event.flag,
        )
    amplitudes = {
        frozenset(mapping[actor] for actor in occupied): value
        for occupied, value in world.amplitudes.items()
    }
    return base.World(actors, events, amplitudes, world.root_tip)


def initial_network(
    params: Params,
    namespace: str = "ROOT-CAP-0",
    relabel: Optional[Mapping[str, str]] = None,
    remote_collision: bool = False,
    remote_payload: str = "remote-a",
) -> Network:
    mapping = dict(relabel or {"A": "A", "B": "B", "C": "C", "D": "D"})
    world = renamed_base_world(params, mapping)
    layout = {
        (): (mapping["A"], None, None, {0: (0,), 1: (1,)}),
        (0,): (mapping["B"], (), 0, {0: (0, 0)}),
        (1,): (mapping["C"], (), 1, {}),
        (0, 0): (mapping["D"], (0,), 0, {}),
    }
    actors = {}
    names = {}
    for address, (name, parent, parent_port, children) in layout.items():
        actors[address] = LocalActor(
            name,
            address,
            parent,
            parent_port,
            dict(children),
            world.actors[name].tip,
            namespace,
        )
        names[name] = address
    for address, actor in actors.items():
        if actor.parent_address is not None:
            assert actor.parent_port is not None
            key = edge_key(namespace, actor.parent_address, actor.parent_port, address)
            actor.edge_keys[actor.parent_address] = key
            actors[actor.parent_address].edge_keys[address] = key

    if remote_collision:
        # The display text collides deliberately; the storage key is scoped to
        # the remote namespace and therefore cannot alter the root component.
        display = event_storage_id(namespace, 0, ())
        storage = "REMOTE-CAP-X::" + display
        world.actors["REMOTE-X"] = base.Actor("REMOTE-X", None, [], storage)
        world.events[storage] = base.Event(
            storage,
            "remote-display-collision",
            ("REMOTE-X",),
            (),
            remote_payload + "|display=" + display,
        )
        # The disconnected carrier is a fixed |0> factor and does not alter
        # the connected pure vector representation.

    network = Network(
        namespace,
        (),
        mapping["A"],
        root_key(namespace),
        actors,
        names,
        world,
    )
    return network


@dataclass(frozen=True)
class LocalOption:
    action: str
    target_ports: Tuple[int, ...]
    probability: Fraction


def local_options(actor: LocalActor, params: Params) -> List[LocalOption]:
    ports = tuple(sorted(actor.children))
    idle = params.idle
    options: List[LocalOption] = []
    if ports:
        share = params.visit / len(ports)
        options.extend(LocalOption("visit", (port,), share) for port in ports)
    else:
        idle += params.visit
    if len(ports) >= 2:
        pairs = tuple(itertools.combinations(ports, 2))
        share = params.fork / len(pairs)
        options.extend(LocalOption("fork", pair, share) for pair in pairs)
    else:
        idle += params.fork
    options.extend(
        (LocalOption("idle", (), idle), LocalOption("birth", (), params.birth))
    )
    options.sort(key=lambda item: (item.action, item.target_ports))
    assert sum(option.probability for option in options) == 1
    return options


def query_secret(network: Network, capability: Capability) -> str:
    if capability.requester_address is None:
        return network.root_key
    target = network.actor(capability.target_address)
    if capability.requester_address not in target.edge_keys:
        raise ValueError("missing owned-edge key")
    return target.edge_keys[capability.requester_address]


def validate_route(network: Network, route: Tuple[Address, ...], target: Address) -> None:
    if not route or route[0] != network.root_address or route[-1] != target:
        raise ValueError("malformed route endpoints")
    for parent, child in zip(route, route[1:]):
        actor = network.actor(parent)
        if child not in actor.children.values():
            raise ValueError("nonlocal route hop")


def validate_query(network: Network, address: Address, envelope: QueryEnvelope) -> None:
    cap = envelope.capability
    actor = network.actor(address)
    if address != cap.target_address:
        raise ValueError("wrong query target")
    if cap.namespace != network.namespace or cap.tx != network.current_tx:
        raise ValueError("wrong component/transaction")
    if cap.root_event != network.collector.root_tip:
        raise ValueError("wrong root event")
    if cap.payload not in (0, 1) or cap.payload != network.root_payload:
        raise ValueError("malformed evidence payload")
    if cap.cap_id in actor.used_capabilities:
        raise ValueError("query capability replay")
    validate_route(network, cap.route, address)
    secret = query_secret(network, cap)
    public = cap_public(
        cap.namespace,
        cap.tx,
        cap.root_event,
        cap.requester_address,
        cap.requester_lower,
        cap.target_address,
        cap.port,
        cap.path,
        cap.slot,
        cap.parent_call,
        cap.parent_cap,
        cap.route,
        cap.payload,
    )
    if cap.signature != digest(("query-signature", secret, public)):
        raise ValueError("invalid query capability")
    if cap.cap_id != digest(("query-capability", public, cap.signature)):
        raise ValueError("invalid query identifier")
    if cap.requester_address is None:
        if address != network.root_address or cap.path or cap.slot is not None:
            raise ValueError("non-root top-level query")
        if cap.requester_lower != actor.tip or cap.parent_call is not None:
            raise ValueError("malformed root query")
    else:
        if cap.port is None or cap.slot is None or cap.parent_call is None:
            raise ValueError("incomplete child query")
        requester = network.actor(cap.requester_address)
        if requester.children.get(cap.port) != address:
            raise ValueError("unauthorized child port")
        if requester.tip != cap.requester_lower:
            raise ValueError("stale requester tip")


def transfer_record(cap: Capability) -> TransferRecord:
    return TransferRecord(
        cap.cap_id,
        cap.namespace,
        cap.tx,
        cap.requester_address,
        cap.target_address,
        cap.port,
        cap.root_event,
        cap.requester_lower,
        cap.parent_cap,
        cap.route,
        cap.payload,
    )


def validate_typed_event(
    network: Network,
    initiator: Address,
    operation: str,
    target_ports: Tuple[int, ...],
) -> Tuple[Tuple[str, Address, int], ...]:
    actor = network.actor(initiator)
    expected = {"idle": 0, "birth": 1, "visit": 1, "fork": 2}
    if operation not in expected:
        raise ValueError("unknown event operation")
    if len(target_ports) != expected[operation]:
        raise ValueError("wrong event arity")
    if len(set(target_ports)) != len(target_ports):
        raise ValueError("duplicate event leg")
    legs = []
    if operation == "birth":
        # The newborn port is allocated by the caller and is not yet present.
        if not target_ports or target_ports[0] in actor.children:
            raise ValueError("malformed birth port")
        legs.append(("newborn-target", (), target_ports[0]))
    else:
        for port in target_ports:
            if port not in actor.children:
                raise ValueError("unowned event leg")
            role = "interaction-target"
            legs.append((role, actor.children[port], port))
    return tuple(legs)


def record_provenance(
    network: Network,
    event: str,
    cap: Capability,
    initiator: Address,
    operation: str,
    legs: Tuple[Tuple[str, Address, int], ...],
    coupling: Fraction,
    child_evidence: Sequence[str] = (),
) -> Provenance:
    evidence = digest(
        (
            "evidence",
            cap.payload,
            cap.route,
            initiator,
            operation,
            legs,
            tuple(child_evidence),
        )
    )
    flag = (
        "orthogonal-event-factor",
        network.namespace,
        network.current_tx,
        cap.path,
        operation,
        tuple((role, address, port) for role, address, port in legs),
    )
    prov = Provenance(
        event,
        network.namespace,
        network.current_tx,
        cap.path,
        initiator,
        legs,
        operation,
        frac_text(coupling),
        cap.cap_id,
        cap.route,
        cap.payload,
        evidence,
        flag,
    )
    if event in network.provenance:
        raise ValueError("duplicate provenance")
    network.provenance[event] = prov
    return prov


def issue_return(network: Network, address: Address, cap: Capability, event: str) -> None:
    if event not in network.provenance:
        raise ValueError("return lacks event provenance")
    prov = network.provenance[event]
    if prov.capability != cap.cap_id or prov.initiator != address:
        raise ValueError("event not produced by query")
    if cap.requester_address is None:
        if address != network.root_address:
            raise ValueError("non-root result")
        if network.root_result is not None:
            raise ValueError("duplicate root result")
        network.root_result = event
        return
    secret = query_secret(network, cap)
    signature = return_signature(secret, cap, event, prov.evidence_digest)
    network.actor(cap.requester_address).mailbox.append(
        ReturnEnvelope(cap, event, address, prov.evidence_digest, signature)
    )


def create_local_idle(network: Network, cap: Capability) -> str:
    address = cap.target_address
    actor = network.actor(address)
    validate_typed_event(network, address, "idle", ())
    tag = base_tx_tag(network.namespace, network.current_tx)
    event = base.create_idle(
        network.collector,
        actor.name,
        tag,
        cap.path,
        cap.root_event,
        cap.requester_lower,
    )
    network.sync_tips((actor.name,))
    record_provenance(network, event, cap, address, "idle", (), Fraction(0))
    return event


def create_local_birth(network: Network, cap: Capability, params: Params) -> str:
    address = cap.target_address
    actor = network.actor(address)
    port = 0 if not actor.children else max(actor.children) + 1
    validate_typed_event(network, address, "birth", (port,))
    tag = base_tx_tag(network.namespace, network.current_tx)
    child_name = base.newborn_name(tag, cap.path)
    event = base.create_birth(
        network.collector,
        actor.name,
        tag,
        cap.path,
        cap.root_event,
        cap.requester_lower,
        params,
    )
    child_address = address + (port,)
    if child_address in network.actors:
        raise ValueError("duplicate newborn address")
    actor.children[port] = child_address
    child = LocalActor(
        child_name,
        child_address,
        address,
        port,
        {},
        event,
        network.namespace,
    )
    key = edge_key(network.namespace, address, port, child_address)
    actor.edge_keys[child_address] = key
    child.edge_keys[address] = key
    network.actors[child_address] = child
    network.name_to_address[child_name] = child_address
    network.sync_tips((actor.name, child_name))
    legs = (("newborn-target", child_address, port),)
    record_provenance(network, event, cap, address, "birth", legs, params.g)
    return event


def create_local_merge(
    network: Network,
    call: OwnedCall,
    params: Params,
) -> str:
    cap = call.incoming
    address = cap.target_address
    actor = network.actor(address)
    legs = validate_typed_event(network, address, call.action, call.target_ports)
    targets = tuple(network.actor(actor.children[port]).name for port in call.target_ports)
    returned = tuple(call.results[slot].result_event for slot in range(len(targets)))
    tag = base_tx_tag(network.namespace, network.current_tx)
    event = base.create_merge(
        network.collector,
        actor.name,
        targets,
        returned,
        tag,
        cap.path,
        cap.root_event,
        cap.requester_lower,
        params,
    )
    network.sync_tips((actor.name, *targets))
    coupling = params.interact_sin * params.interact_sin
    record_provenance(
        network,
        event,
        cap,
        address,
        call.action,
        legs,
        coupling,
        tuple(call.results[slot].evidence_digest for slot in range(len(targets))),
    )
    return event


def process_query(
    network: Network,
    address: Address,
    envelope: QueryEnvelope,
    option: LocalOption,
    params: Params,
) -> None:
    validate_query(network, address, envelope)
    cap = envelope.capability
    actor = network.actor(address)
    # Validation is complete before any immutable mutation.
    actor.used_capabilities.add(cap.cap_id)
    network.transfers[cap.cap_id] = transfer_record(cap)
    if option.action == "idle":
        event = create_local_idle(network, cap)
        issue_return(network, address, cap, event)
        return
    if option.action == "birth":
        event = create_local_birth(network, cap, params)
        issue_return(network, address, cap, event)
        return

    validate_typed_event(network, address, option.action, option.target_ports)
    call_id = digest(
        ("owned-call", network.namespace, network.current_tx, address, cap.path, cap.cap_id)
    )
    if call_id in actor.outstanding:
        raise ValueError("duplicate owned call")
    child_caps = {}
    held_lower = actor.tip
    for slot, port in enumerate(option.target_ports):
        child_address = actor.children[port]
        secret = actor.edge_keys[child_address]
        child_cap = make_capability(
            secret,
            network.namespace,
            network.current_tx,
            cap.root_event,
            address,
            held_lower,
            child_address,
            port,
            cap.path + (slot,),
            slot,
            call_id,
            cap.cap_id,
            cap.route + (child_address,),
            cap.payload,
        )
        child_caps[slot] = child_cap
    call = OwnedCall(call_id, cap, option.action, option.target_ports, child_caps)
    actor.outstanding[call_id] = call
    for slot in sorted(child_caps):
        child_cap = child_caps[slot]
        network.actor(child_cap.target_address).mailbox.append(QueryEnvelope(child_cap))


def validate_return(
    network: Network,
    address: Address,
    envelope: ReturnEnvelope,
) -> OwnedCall:
    cap = envelope.capability
    actor = network.actor(address)
    if cap.requester_address != address or cap.parent_call is None or cap.slot is None:
        raise ValueError("return addressed to wrong actor")
    if cap.parent_call not in actor.outstanding:
        raise ValueError("return for missing call")
    call = actor.outstanding[cap.parent_call]
    if cap.slot not in call.child_caps or call.child_caps[cap.slot].cap_id != cap.cap_id:
        raise ValueError("return capability mismatch")
    if cap.slot in call.results:
        raise ValueError("duplicate return slot")
    if envelope.result_actor != cap.target_address:
        raise ValueError("return actor mismatch")
    child = network.actor(cap.target_address)
    if child.tip != envelope.result_event:
        raise ValueError("stale return result")
    if envelope.result_event not in network.provenance:
        raise ValueError("return event lacks provenance")
    prov = network.provenance[envelope.result_event]
    if prov.capability != cap.cap_id or prov.initiator != cap.target_address:
        raise ValueError("return event not produced by issued query")
    if prov.evidence_digest != envelope.evidence_digest:
        raise ValueError("return evidence mismatch")
    secret = actor.edge_keys[cap.target_address]
    expected = return_signature(secret, cap, envelope.result_event, envelope.evidence_digest)
    if envelope.signature != expected:
        raise ValueError("invalid return signature")
    return call


def process_return(
    network: Network,
    address: Address,
    envelope: ReturnEnvelope,
    params: Params,
) -> None:
    call = validate_return(network, address, envelope)
    assert envelope.capability.slot is not None
    call.results[envelope.capability.slot] = envelope
    if len(call.results) != len(call.child_caps):
        return
    event = create_local_merge(network, call, params)
    del network.actor(address).outstanding[call.call_id]
    issue_return(network, address, call.incoming, event)


def envelope_key(envelope: Envelope) -> Tuple[object, ...]:
    if isinstance(envelope, QueryEnvelope):
        cap = envelope.capability
        return (0, cap.target_address, cap.path, cap.cap_id)
    cap = envelope.capability
    return (1, cap.requester_address, cap.path, envelope.result_event, cap.cap_id)


def pop_envelope(network: Network, scheduler: str) -> Tuple[Address, Envelope]:
    ready = [address for address, actor in network.actors.items() if actor.mailbox]
    if not ready:
        raise ValueError("no deliverable mailbox")
    candidates = [
        (address, index, envelope)
        for address in ready
        for index, envelope in enumerate(network.actor(address).mailbox)
    ]
    if scheduler == "fifo":
        address, index, envelope = min(candidates, key=lambda row: (row[0], row[1]))
    elif scheduler == "lifo":
        address, index, envelope = max(candidates, key=lambda row: (row[0], row[1]))
    elif scheduler == "canonical":
        address, index, envelope = min(candidates, key=lambda row: envelope_key(row[2]))
    else:
        raise ValueError("unknown serializer")
    network.actor(address).mailbox.pop(index)
    return address, envelope


def start_root_call(network: Network, tx: int, payload: int) -> None:
    if network.pending_count() or network.outstanding_count() or network.root_result is not None:
        raise ValueError("root call started with live work")
    root = network.actor(network.root_address)
    network.current_tx = tx
    network.root_payload = payload
    network.collector.root_tip = root.tip
    cap = make_capability(
        network.root_key,
        network.namespace,
        tx,
        root.tip,
        None,
        root.tip,
        network.root_address,
        None,
        (),
        None,
        None,
        None,
        (network.root_address,),
        payload,
    )
    root.mailbox.append(QueryEnvelope(cap))


@dataclass
class NetBranch:
    probability: Fraction
    network: Network


def enumerate_network(
    initial: Network,
    params: Params,
    scheduler: str,
    tx: int = 0,
    payload: int = 0,
) -> List[NetBranch]:
    network = initial.clone()
    start_root_call(network, tx, payload)
    frontier: List[Tuple[Fraction, Network]] = [(Fraction(1), network)]
    completed: List[NetBranch] = []
    while frontier:
        probability, state = frontier.pop()
        if state.root_result is not None:
            if state.pending_count() or state.outstanding_count():
                raise AssertionError("root returned with live actor work")
            if state.actor(state.root_address).tip != state.root_result:
                raise AssertionError("root result is not A2")
            state.collector.root_tip = state.root_result
            completed.append(NetBranch(probability, state))
            continue
        address, envelope = pop_envelope(state, scheduler)
        if isinstance(envelope, QueryEnvelope):
            options = local_options(state.actor(address), params)
            for option in options:
                child = state.clone()
                process_query(child, address, envelope, option, params)
                frontier.append((probability * option.probability, child))
        else:
            process_return(state, address, envelope, params)
            frontier.append((probability, state))
    assert sum(branch.probability for branch in completed) == 1
    return completed


def reset_for_next_call(network: Network) -> Network:
    state = network.clone()
    state.root_result = None
    state.collector.transaction_events.clear()
    state.collector.queried_actors.clear()
    state.collector.local_reads.clear()
    state.collector.birth_checks.clear()
    return state


def physical_event_id(network: Network, event: str) -> Tuple[object, ...]:
    if event in network.provenance:
        prov = network.provenance[event]
        return ("transaction", prov.tx, prov.event_address)
    return ("seed", event)


def physical_key(network: Network, include_remote: bool = False) -> Tuple[object, ...]:
    actor_rows = []
    for address, actor in sorted(network.actors.items()):
        actor_rows.append(
            (
                address,
                actor.parent_address,
                actor.parent_port,
                tuple(sorted(actor.children.items())),
                physical_event_id(network, actor.tip),
            )
        )
    event_rows = []
    for event, prov in sorted(network.provenance.items(), key=lambda item: (item[1].tx, item[1].event_address)):
        raw = network.collector.events[event]
        event_rows.append(
            (
                physical_event_id(network, event),
                prov.initiator,
                prov.target_legs,
                prov.operation,
                prov.coupling,
                prov.route,
                prov.payload,
                prov.evidence_digest,
                prov.flag_factor,
                tuple(sorted(physical_event_id(network, pred) for pred in raw.predecessors)),
            )
        )
    amplitudes = []
    for occupied, amplitude in network.collector.amplitudes.items():
        addresses = tuple(
            sorted(network.name_to_address[name] for name in occupied if name in network.name_to_address)
        )
        amplitudes.append((addresses, amplitude))
    amplitudes.sort(key=lambda row: row[0])
    transfer_rows = tuple(
        sorted(
            [
                (
                transfer.tx,
                transfer.requester,
                transfer.target,
                transfer.port,
                transfer.route,
                transfer.payload,
                )
                for transfer in network.transfers.values()
            ],
            key=repr,
        )
    )
    remote = ()
    if include_remote:
        remote = tuple(
            sorted(
                (name, event.kind, event.flag)
                for name, event in network.collector.events.items()
                if set(event.actors) == {"REMOTE-X"}
            )
        )
    return tuple(actor_rows), tuple(event_rows), tuple(amplitudes), transfer_rows, remote


def distribution(branches: Sequence[NetBranch]) -> Dict[Tuple[object, ...], Fraction]:
    result: Dict[Tuple[object, ...], Fraction] = defaultdict(Fraction)
    for branch in branches:
        result[physical_key(branch.network)] += branch.probability
    return dict(sorted(result.items(), key=lambda item: repr(item[0])))


def root_kind_distribution(branches: Sequence[NetBranch]) -> Dict[str, Fraction]:
    result: Dict[str, Fraction] = defaultdict(Fraction)
    for branch in branches:
        prov = branch.network.provenance[branch.network.root_result]
        result[prov.operation] += branch.probability
    return dict(sorted(result.items()))


def acquired(network: Network, old_root: str) -> FrozenSet[str]:
    assert network.root_result
    return network.collector.ancestors(network.root_result) - network.collector.ancestors(old_root)


def route_payload_gate(branches: Sequence[NetBranch], old_root: str) -> Tuple[int, int]:
    routes = 0
    negative = 0
    for branch in branches:
        network = branch.network
        new_past = acquired(network, old_root)
        for event, prov in network.provenance.items():
            if prov.tx != network.current_tx:
                continue
            if event not in new_past:
                raise AssertionError("transaction event outside A2 ancestry")
            validate_route(network, prov.route, prov.initiator)
            if prov.payload != network.root_payload:
                raise AssertionError("payload not carried")
            cap = network.transfers[prov.capability]
            if cap.route != prov.route or cap.payload != prov.payload:
                raise AssertionError("route transfer mismatch")
            routes += 1
        root_prov = network.provenance[network.root_result]
        if root_prov.operation == "visit" and root_prov.target_legs[0][1] == (1,):
            if "BD" in new_past:
                raise AssertionError("unqueried B evidence acquired")
            negative += 1
    if not negative:
        raise AssertionError("missing unqueried-route negative")
    return routes, negative


def matrix_identity(size: int) -> List[List[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def transpose(matrix: Sequence[Sequence[Fraction]]) -> List[List[Fraction]]:
    return [list(row) for row in zip(*matrix)]


def matmul(
    left: Sequence[Sequence[Fraction]], right: Sequence[Sequence[Fraction]]
) -> List[List[Fraction]]:
    rt = transpose(right)
    return [
        [sum(a * b for a, b in zip(row, column)) for column in rt]
        for row in left
    ]


def controlled_rotation(cosine: Fraction, sine: Fraction) -> List[List[Fraction]]:
    # basis 00,01,10,11 (control first)
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, cosine, -sine],
        [0, 0, sine, cosine],
    ]


def birth_isometry(cosine: Fraction, sine: Fraction) -> List[List[Fraction]]:
    # columns are images of parent |0>,|1> with fresh child |0>.
    return [
        [1, 0],
        [0, 0],
        [0, cosine],
        [0, sine],
    ]


def apply_crot_basis(
    basis: Tuple[int, ...], control: int, target: int, cosine: Fraction, sine: Fraction
) -> Dict[Tuple[int, ...], Fraction]:
    if basis[control] == 0:
        return {basis: Fraction(1)}
    flipped = list(basis)
    if basis[target] == 0:
        flipped[target] = 1
        return {basis: cosine, tuple(flipped): sine}
    flipped[target] = 0
    return {tuple(flipped): -sine, basis: cosine}


def fork_unitary(cosine: Fraction, sine: Fraction) -> List[List[Fraction]]:
    bases = tuple(itertools.product((0, 1), repeat=3))
    index = {basis: i for i, basis in enumerate(bases)}
    matrix = [[Fraction(0) for _ in bases] for _ in bases]
    for column, basis in enumerate(bases):
        first = apply_crot_basis(basis, 0, 1, cosine, sine)
        total: Dict[Tuple[int, ...], Fraction] = defaultdict(Fraction)
        for mid, amplitude in first.items():
            for out, factor in apply_crot_basis(mid, 0, 2, cosine, sine).items():
                total[out] += amplitude * factor
        for out, amplitude in total.items():
            matrix[index[out]][column] = amplitude
    return matrix


def flagged_operator_gate(params: Params) -> Tuple[int, int, int]:
    idle = matrix_identity(2)
    birth = birth_isometry(params.birth_cos, params.birth_sin)
    visit = controlled_rotation(params.interact_cos, params.interact_sin)
    fork = fork_unitary(params.interact_cos, params.interact_sin)
    checks = (
        matmul(transpose(idle), idle) == matrix_identity(2),
        matmul(transpose(birth), birth) == matrix_identity(2),
        matmul(transpose(visit), visit) == matrix_identity(4),
        matmul(transpose(fork), fork) == matrix_identity(8),
    )
    if not all(checks):
        raise AssertionError("elementary isometry gate")
    options = local_options(initial_network(params).actor(()), params)
    if sum(option.probability for option in options) != 1:
        raise AssertionError("instrument completeness")
    flags = {
        (option.action, option.target_ports)
        for option in options
    }
    if len(flags) != len(options):
        raise AssertionError("nonorthogonal local flag labels")
    # In the direct-sum representation distinct flag labels are orthogonal by
    # construction and each V^dag V=I, hence sum q V^dag V=I exactly.
    return len(checks), len(options), len(flags)


def full_projectivity(params: Params, first: Sequence[NetBranch]) -> Tuple[int, int, int, int]:
    first_dist = distribution(first)
    marginal: Dict[Tuple[object, ...], Fraction] = defaultdict(Fraction)
    coarse = set()
    refinements = 0
    persistence = 0
    for branch in first:
        first_key = physical_key(branch.network)
        first_prov = copy.deepcopy(branch.network.provenance)
        old_root = branch.network.root_result
        assert old_root
        coarse.add((branch.network.provenance[old_root].operation, tuple(sorted(acquired(branch.network, "A1")))))
        seed = reset_for_next_call(branch.network)
        second = enumerate_network(seed, params, "canonical", tx=1, payload=1)
        refinements += len(second)
        for next_branch in second:
            if any(next_branch.network.provenance.get(key) != value for key, value in first_prov.items()):
                raise AssertionError("old event factor mutation")
            if old_root not in next_branch.network.collector.ancestors(next_branch.network.root_result):
                raise AssertionError("root wire persistence")
            persistence += 1
            marginal[first_key] += branch.probability * next_branch.probability
    if dict(marginal) != first_dist:
        raise AssertionError("full first-cylinder projectivity")
    return len(first_dist), len(coarse), refinements, persistence


def deterministic_choice(
    actor: LocalActor, cap: Capability, params: Params, ticket: int
) -> LocalOption:
    options = local_options(actor, params)
    denominator = 1
    for option in options:
        denominator *= option.probability.denominator
    point = Fraction(
        int(digest(("choice", ticket, actor.address, cap.tx, cap.path)), 16) % denominator,
        denominator,
    )
    cumulative = Fraction(0)
    for option in options:
        cumulative += option.probability
        if point < cumulative:
            return option
    return options[-1]


def deterministic_call(
    initial: Network,
    params: Params,
    scheduler: str,
    tx: int,
    payload: int,
    ticket: int,
) -> Network:
    network = initial.clone()
    start_root_call(network, tx, payload)
    while network.root_result is None:
        address, envelope = pop_envelope(network, scheduler)
        if isinstance(envelope, QueryEnvelope):
            option = deterministic_choice(network.actor(address), envelope.capability, params, ticket)
            process_query(network, address, envelope, option, params)
        else:
            process_return(network, address, envelope, params)
    if network.pending_count() or network.outstanding_count():
        raise AssertionError("deterministic call left live work")
    network.collector.root_tip = network.root_result
    return network


def multi_call_replay(params: Params, scheduler: str, calls: int = 8) -> Network:
    network = initial_network(params)
    for tx in range(calls):
        if tx:
            network = reset_for_next_call(network)
        network = deterministic_call(network, params, scheduler, tx, tx % 2, 707)
    return network


def mutate_before_after(network: Network) -> Tuple[object, ...]:
    return (
        physical_key(network, include_remote=True),
        network.pending_count(),
        network.outstanding_count(),
        tuple((address, tuple(actor.mailbox), tuple(sorted(actor.outstanding))) for address, actor in sorted(network.actors.items())),
    )


def adversarial_gate(params: Params) -> Tuple[int, int]:
    rejected = 0
    unchanged = 0

    def expect_reject(network: Network, address: Address, envelope: Envelope, handler: str) -> None:
        nonlocal rejected, unchanged
        before = mutate_before_after(network)
        try:
            if handler == "query":
                assert isinstance(envelope, QueryEnvelope)
                process_query(network, address, envelope, LocalOption("idle", (), Fraction(1)), params)
            else:
                assert isinstance(envelope, ReturnEnvelope)
                process_return(network, address, envelope, params)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError("adversarial envelope accepted")
        if mutate_before_after(network) == before:
            unchanged += 1
        else:
            raise AssertionError("rejection mutated immutable state")

    # B1-A: syntactically local but unsigned/unissued A->B query.
    n1 = initial_network(params)
    n1.current_tx = 91
    n1.root_payload = 0
    n1.collector.root_tip = "A1"
    bad = make_capability(
        "wrong-secret",
        n1.namespace,
        91,
        "A1",
        (),
        "A1",
        (0,),
        0,
        (0,),
        0,
        "missing",
        "missing-parent",
        ((), (0,)),
        0,
    )
    expect_reject(n1, (0,), QueryEnvelope(bad), "query")

    # B1-B: requester-free B root impersonation.
    n2 = initial_network(params)
    n2.current_tx = 92
    n2.root_payload = 0
    n2.collector.root_tip = "A1"
    fake_root = make_capability(
        n2.root_key,
        n2.namespace,
        92,
        "A1",
        None,
        "BD",
        (0,),
        None,
        (),
        None,
        None,
        None,
        ((0,),),
        0,
    )
    expect_reject(n2, (0,), QueryEnvelope(fake_root), "query")

    # Prepare a genuine root->B issued call, but do not execute B.
    n3 = initial_network(params)
    start_root_call(n3, 93, 0)
    address, root_query = pop_envelope(n3, "canonical")
    assert address == () and isinstance(root_query, QueryEnvelope)
    visit_b = next(option for option in local_options(n3.actor(()), params) if option.action == "visit" and option.target_ports == (0,))
    process_query(n3, (), root_query, visit_b, params)
    call = next(iter(n3.actor(()).outstanding.values()))
    child_cap = call.child_caps[0]
    secret = n3.actor(()).edge_keys[(0,)]
    # B1-C: old BD tip impersonates a return from the unexecuted query.
    forged = ReturnEnvelope(
        child_cap,
        "BD",
        (0,),
        "forged-evidence",
        return_signature(secret, child_cap, "BD", "forged-evidence"),
    )
    expect_reject(n3, (), forged, "return")

    # Negative slot / cross-continuation replay.
    wrong_slot_cap = copy.copy(child_cap)
    object.__setattr__(wrong_slot_cap, "slot", -1)
    forged_slot = ReturnEnvelope(wrong_slot_cap, "BD", (0,), "x", "bad")
    expect_reject(n3, (), forged_slot, "return")

    missing_cap = copy.copy(child_cap)
    object.__setattr__(missing_cap, "parent_call", "other-call")
    forged_call = ReturnEnvelope(missing_cap, "BD", (0,), "x", "bad")
    expect_reject(n3, (), forged_call, "return")

    # Malformed direct merges fail before calling the base mutator.
    n4 = initial_network(params)
    before = mutate_before_after(n4)
    for operation, ports in (("fork", (0, 0)), ("visit", (9,)), ("idle", (0,)), ("birth", (0,))):
        try:
            validate_typed_event(n4, (), operation, ports)
        except ValueError:
            rejected += 1
            if mutate_before_after(n4) == before:
                unchanged += 1
        else:
            raise AssertionError("malformed typed event accepted")
    return rejected, unchanged


def source_hash() -> str:
    return sha256(Path(__file__).read_bytes())


def main() -> None:
    gates: List[str] = []
    science: Dict[str, object] = {}
    print("[D35b capability-authenticated actor repair]")
    print(f"base_source_sha256={BASE_SHA256}")
    print("ARITHMETIC: Fraction exact; Decimal precision=120")
    print("TIME VARIABLES: 0")
    print("GLOBAL OPPORTUNITY NORMALIZERS: 0")

    for params in (Q1, Q2):
        params.validate()
        print(f"[{params.name}]")
        schedulers = {}
        for scheduler in ("fifo", "lifo", "canonical"):
            branches = enumerate_network(initial_network(params), params, scheduler, payload=0)
            schedulers[scheduler] = branches
            print(
                f"actor_owned_{scheduler}_branches={len(branches)} "
                f"atoms={len(distribution(branches))} total={frac_text(sum(b.probability for b in branches))}"
            )
        dists = {key: distribution(value) for key, value in schedulers.items()}
        if not (dists["fifo"] == dists["lifo"] == dists["canonical"]):
            raise AssertionError("actor scheduler distribution")
        branches = schedulers["canonical"]
        kinds = root_kind_distribution(branches)
        print("A2_kind=" + ",".join(f"{key}:{frac_text(value)}" for key, value in kinds.items()))
        gates.append(f"A1-{params.name}")

        routes, negatives = route_payload_gate(branches, "A1")
        payload_one = enumerate_network(initial_network(params), params, "canonical", payload=1)
        if any(branch.network.provenance[branch.network.root_result].payload != 1 for branch in payload_one):
            raise AssertionError("source intervention failed")
        if any(branch.network.provenance[branch.network.root_result].payload != 0 for branch in branches):
            raise AssertionError("source-zero intervention failed")
        print(
            f"authenticated_routes={routes} unqueried_route_controls={negatives} "
            "do_source_0_to_A2=0 do_source_1_to_A2=1"
        )
        gates.append(f"A2-{params.name}")

        remote = enumerate_network(
            initial_network(params, remote_collision=True, remote_payload="arbitrary-REMOTE-content"),
            params,
            "canonical",
        )
        if distribution(remote) != dists["canonical"]:
            raise AssertionError("disconnected scoped-identity invariance")
        print(
            f"remote_collision_display={event_storage_id('ROOT-CAP-0',0,())} "
            "scoped_storage=yes A_distribution_equal=yes remote_reads=0"
        )
        gates.append(f"A3-{params.name}")

        relabel = {"A": "R", "B": "Y", "C": "X", "D": "Z"}
        renamed = enumerate_network(
            initial_network(params, relabel=relabel), params, "canonical"
        )
        if distribution(renamed) != dists["canonical"]:
            raise AssertionError("alpha-relabeling covariance")
        print(f"alpha_relabel_atoms={len(distribution(renamed))} quotient_equal=yes")
        gates.append(f"A4-{params.name}")

        full_atoms, coarse_atoms, refinements, persistence = full_projectivity(params, branches)
        print(
            f"full_first_atoms={full_atoms} coarse_first_atoms={coarse_atoms} "
            f"second_refinements={refinements} persistence_checks={persistence} full_marginal_equal=yes"
        )
        gates.append(f"A5-{params.name}")

        op_checks, option_count, flag_count = flagged_operator_gate(params)
        branch_flags = [
            tuple(sorted(prov.flag_factor for prov in branch.network.provenance.values()))
            for branch in branches
        ]
        if len(set(branch_flags)) != len(branch_flags):
            raise AssertionError("completed histories lack orthogonal flag separation")
        print(
            f"operator_isometries={op_checks}/4 local_options={option_count} "
            f"orthogonal_local_flags={flag_count} completed_flag_histories={len(set(branch_flags))} "
            "sum_q_VdagV=I"
        )
        gates.append(f"A6-{params.name}")

        rejected, unchanged = adversarial_gate(params)
        if rejected != 9 or unchanged != 9:
            raise AssertionError(("adversarial count", rejected, unchanged))
        print(f"malformed_capability_or_event_rejected={rejected}/9 pre_mutation_unchanged={unchanged}/9")
        gates.append(f"A7-{params.name}")

        grown_checks = 0
        for first in branches:
            seed = reset_for_next_call(first.network)
            reference = enumerate_network(seed, params, "canonical", tx=1, payload=1)
            ref_dist = distribution(reference)
            for scheduler in ("fifo", "lifo"):
                if distribution(enumerate_network(seed, params, scheduler, tx=1, payload=1)) != ref_dist:
                    raise AssertionError("grown actor scheduler")
                grown_checks += 1
        replays = [multi_call_replay(params, scheduler) for scheduler in ("fifo", "lifo", "canonical")]
        if not (physical_key(replays[0]) == physical_key(replays[1]) == physical_key(replays[2])):
            raise AssertionError("multi-call serializer replay")
        print(
            f"grown_second_call_scheduler_checks={grown_checks} "
            f"multi_call_replay=8 calls actors={len(replays[0].actors)} events={len(replays[0].collector.events)} exact_equal=yes"
        )
        gates.append(f"A8-{params.name}")

        science[params.name] = {
            "distribution": digest(dists["canonical"]),
            "kinds": {key: frac_text(value) for key, value in kinds.items()},
            "routes": routes,
            "full_atoms": full_atoms,
            "refinements": refinements,
            "multi": digest(physical_key(replays[0])),
        }

    q1 = root_kind_distribution(enumerate_network(initial_network(Q1), Q1, "canonical"))
    q2 = root_kind_distribution(enumerate_network(initial_network(Q2), Q2, "canonical"))
    if q1["birth"] == q2["birth"] or q1["visit"] == q2["visit"]:
        raise AssertionError("nonselection disappeared")
    print("[NONSELECTION]")
    print(
        f"birth_Q1={frac_text(q1['birth'])} birth_Q2={frac_text(q2['birth'])}; "
        f"visit_Q1={frac_text(q1['visit'])} visit_Q2={frac_text(q2['visit'])}"
    )
    gates.append("A9")

    print("[SCOPE]")
    print(
        "proved: capability-authenticated actor-owned rooted nested-call classical history family; "
        "structural+declared classical payload acquisition; flagged direct-sum Busch instrument compatibility"
    )
    print(
        "open: cycles, peers, mutually initiating/overlapping calls, disconnected joins, coherent graph-sector sum, "
        "root/capability/q/g derivation, v9 spectrum map, spacetime, proper time, nature's law"
    )
    gates.append("A10")

    if len(gates) != 18:
        raise AssertionError((len(gates), gates))
    science["gates"] = gates
    print("[HASHES]")
    print(f"source_sha256={source_hash()}")
    print(f"internal_science_sha256={digest(science)}")
    print("[VERDICT]")
    print("PASS 18/18")
    print("TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE")
    print("opportunity weights, coupling, root/ownership and omitted sectors remain extra physics")


if __name__ == "__main__":
    main()
