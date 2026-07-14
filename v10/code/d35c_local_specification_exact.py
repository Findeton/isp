#!/usr/bin/env python3
"""D35c closing companion: issued actors, remote evidence and CQ instrument.

This executable hash-locks D35b, preserves its exact rooted nested-call
kernel, and closes the second hostile round without modifying the rejected
artifact.  It uses exact Fraction arithmetic and no duration, rate, numerical
proper time or global opportunity normalizer.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import itertools
import json
import sys
from collections import defaultdict
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List, Mapping, Optional, Sequence, Tuple


HERE = Path(__file__).resolve().parent
PRIOR_PATH = HERE / "d35b_capability_actor_exact.py"
PRIOR_SHA256 = "fa6d69e6d6b85620d19da8e80899dba4a3a5f976fb6e0b3fcfb7b1224a253c4d"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


if sha256(PRIOR_PATH.read_bytes()) != PRIOR_SHA256:
    raise RuntimeError("D35b source hash mismatch")
_SPEC = importlib.util.spec_from_file_location("d35b_locked", PRIOR_PATH)
assert _SPEC and _SPEC.loader
prior = importlib.util.module_from_spec(_SPEC)
sys.modules["d35b_locked"] = prior
_SPEC.loader.exec_module(prior)


Address = prior.Address
Params = prior.Params
Q1 = prior.Q1
Q2 = prior.Q2
LocalOption = prior.LocalOption
QueryEnvelope = prior.QueryEnvelope
ReturnEnvelope = prior.ReturnEnvelope
Envelope = prior.Envelope
Network = prior.Network
NetBranch = prior.NetBranch


@dataclass(frozen=True)
class CarriedReturnEnvelope:
    capability: prior.Capability
    result_event: str
    result_actor: Address
    evidence_digest: str
    signature: str
    output_bit: int
    output_sources: FrozenSet[Address]


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


def install_actor_fields(network: Network) -> None:
    for address, actor in network.actors.items():
        actor.issued_incoming = set()
        actor.call_ordinal = 0 if address == network.root_address else None
        actor.evidence_bit = 0
        actor.evidence_sources = frozenset()
    network.output_payloads = {}
    network.output_sources = {}
    network.local_outcomes = {}
    network.structural_alternatives = {}
    network.seed_payloads = {}
    network.call_lowers = {}


def add_connected_source_seal(network: Network, bit: int) -> None:
    if bit not in (0, 1):
        raise ValueError("source bit")
    address = (0, 0)
    actor = network.actor(address)
    old_tip = actor.tip
    event = "D-source-seal"
    if event in network.collector.events:
        raise ValueError("duplicate source seal")
    network.collector.events[event] = prior.base.Event(
        event,
        "source-seal",
        (actor.name,),
        (old_tip,),
        ("bounded-source-bit", bit),
    )
    network.collector.actors[actor.name].tip = event
    actor.tip = event
    actor.evidence_bit = bit
    actor.evidence_sources = frozenset({address}) if bit else frozenset()
    network.seed_payloads[event] = bit
    network.source_event = event


def rename_seed_events(network: Network, mapping: Mapping[str, str]) -> None:
    if network.provenance:
        raise ValueError("rename only before generated events")
    if set(mapping) != set(network.collector.events):
        raise ValueError("rename must cover complete seed event DAG")
    if len(set(mapping.values())) != len(mapping):
        raise ValueError("noninjective event rename")
    events = {}
    for old, raw in network.collector.events.items():
        new = mapping[old]
        events[new] = prior.base.Event(
            new,
            raw.kind,
            raw.actors,
            tuple(mapping[pred] for pred in raw.predecessors),
            raw.flag,
        )
    network.collector.events = events
    for actor in network.collector.actors.values():
        actor.tip = mapping[actor.tip]
    for actor in network.actors.values():
        actor.tip = mapping[actor.tip]
    network.collector.root_tip = mapping[network.collector.root_tip]
    network.seed_payloads = {
        mapping[event]: payload for event, payload in network.seed_payloads.items()
    }
    network.source_event = mapping[network.source_event]


def initial_network(
    params: Params,
    namespace: str = "ROOT-CAP-0",
    relabel: Optional[Mapping[str, str]] = None,
    source_bit: int = 0,
    event_relabel: Optional[Mapping[str, str]] = None,
    remote_collision: bool = False,
    remote_payload: str = "remote-a",
) -> Network:
    network = prior.initial_network(
        params,
        namespace=namespace,
        relabel=relabel,
        remote_collision=remote_collision,
        remote_payload=remote_payload,
    )
    install_actor_fields(network)
    add_connected_source_seal(network, source_bit)
    if event_relabel is not None:
        rename_seed_events(network, event_relabel)
    network.current_tx = -1
    network.root_payload = 0
    return network


def enqueue_query(network: Network, cap: prior.Capability) -> None:
    actor = network.actor(cap.target_address)
    if cap.cap_id in actor.issued_incoming or cap.cap_id in actor.used_capabilities:
        raise ValueError("duplicate issued capability")
    actor.issued_incoming.add(cap.cap_id)
    actor.mailbox.append(QueryEnvelope(cap))


def validate_query(network: Network, address: Address, envelope: QueryEnvelope) -> None:
    actor = network.actor(address)
    cap = envelope.capability
    if cap.cap_id not in actor.issued_incoming:
        raise ValueError("query was not issued to target actor")
    prior.validate_query(network, address, envelope)


def event_storage_name(network: Network, cap: prior.Capability) -> str:
    tag = prior.base_tx_tag(network.namespace, network.current_tx)
    return prior.base.event_name(tag, cap.path)


def prevalidate_event_and_option(
    network: Network,
    address: Address,
    cap: prior.Capability,
    option: LocalOption,
    params: Params,
) -> None:
    actor = network.actor(address)
    if option not in prior.local_options(actor, params):
        raise ValueError("option not in actor local menu")
    if option.action == "idle":
        prior.validate_typed_event(network, address, "idle", ())
    elif option.action == "birth":
        port = 0 if not actor.children else max(actor.children) + 1
        prior.validate_typed_event(network, address, "birth", (port,))
        child_address = address + (port,)
        tag = prior.base_tx_tag(network.namespace, network.current_tx)
        child_name = prior.base.newborn_name(tag, cap.path)
        if child_address in network.actors or child_name in network.name_to_address:
            raise ValueError("duplicate newborn")
    else:
        prior.validate_typed_event(network, address, option.action, option.target_ports)
    if event_storage_name(network, cap) in network.collector.events:
        raise ValueError("duplicate generated event identity")


def record_event(
    network: Network,
    event: str,
    cap: prior.Capability,
    initiator: Address,
    operation: str,
    legs: Tuple[Tuple[str, Address, int], ...],
    coupling: Fraction,
    output_bit: int,
    output_sources: FrozenSet[Address],
    child_evidence: Sequence[str] = (),
) -> prior.Provenance:
    prov = prior.record_provenance(
        network,
        event,
        cap,
        initiator,
        operation,
        legs,
        coupling,
        child_evidence,
    )
    evidence = digest(
        (
            "durable-evidence-output",
            prov.evidence_digest,
            output_bit,
            tuple(sorted(output_sources)),
        )
    )
    prov = replace(prov, evidence_digest=evidence)
    network.provenance[event] = prov
    network.output_payloads[event] = output_bit
    network.output_sources[event] = output_sources
    network.local_outcomes[event] = operation
    network.structural_alternatives[event] = (
        operation,
        tuple((role, port) for role, _target, port in legs),
    )
    return prov


def create_idle(network: Network, cap: prior.Capability) -> str:
    address = cap.target_address
    actor = network.actor(address)
    tag = prior.base_tx_tag(network.namespace, network.current_tx)
    event = prior.base.create_idle(
        network.collector,
        actor.name,
        tag,
        cap.path,
        cap.root_event,
        cap.requester_lower,
    )
    network.sync_tips((actor.name,))
    record_event(
        network,
        event,
        cap,
        address,
        "idle",
        (),
        Fraction(0),
        actor.evidence_bit,
        actor.evidence_sources,
    )
    return event


def create_birth(network: Network, cap: prior.Capability, params: Params) -> str:
    address = cap.target_address
    actor = network.actor(address)
    port = 0 if not actor.children else max(actor.children) + 1
    tag = prior.base_tx_tag(network.namespace, network.current_tx)
    child_name = prior.base.newborn_name(tag, cap.path)
    event = prior.base.create_birth(
        network.collector,
        actor.name,
        tag,
        cap.path,
        cap.root_event,
        cap.requester_lower,
        params,
    )
    child_address = address + (port,)
    actor.children[port] = child_address
    child = prior.LocalActor(
        child_name,
        child_address,
        address,
        port,
        {},
        event,
        network.namespace,
    )
    child.issued_incoming = set()
    child.call_ordinal = None
    child.evidence_bit = actor.evidence_bit
    child.evidence_sources = actor.evidence_sources
    key = prior.edge_key(network.namespace, address, port, child_address)
    actor.edge_keys[child_address] = key
    child.edge_keys[address] = key
    network.actors[child_address] = child
    network.name_to_address[child_name] = child_address
    network.sync_tips((actor.name, child_name))
    legs = (("newborn-target", child_address, port),)
    record_event(
        network,
        event,
        cap,
        address,
        "birth",
        legs,
        params.g,
        actor.evidence_bit,
        actor.evidence_sources,
    )
    return event


def create_merge(network: Network, call: prior.OwnedCall, params: Params) -> str:
    cap = call.incoming
    address = cap.target_address
    actor = network.actor(address)
    legs = prior.validate_typed_event(
        network, address, call.action, call.target_ports
    )
    targets = tuple(network.actor(actor.children[port]).name for port in call.target_ports)
    returned = tuple(call.results[slot].result_event for slot in range(len(targets)))
    child_bits = tuple(call.results[slot].output_bit for slot in range(len(targets)))
    child_sources = tuple(call.results[slot].output_sources for slot in range(len(targets)))
    output_bit = max((actor.evidence_bit, *child_bits))
    output_sources = frozenset().union(actor.evidence_sources, *child_sources)
    tag = prior.base_tx_tag(network.namespace, network.current_tx)
    event = prior.base.create_merge(
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
    record_event(
        network,
        event,
        cap,
        address,
        call.action,
        legs,
        coupling,
        output_bit,
        output_sources,
        tuple(call.results[slot].evidence_digest for slot in range(len(targets))),
    )
    actor.evidence_bit = output_bit
    actor.evidence_sources = output_sources
    for port in call.target_ports:
        target = network.actor(actor.children[port])
        target.evidence_bit = output_bit
        target.evidence_sources = output_sources
    return event


def issue_return(network: Network, address: Address, cap: prior.Capability, event: str) -> None:
    if event not in network.provenance:
        raise ValueError("return lacks event provenance")
    prov = network.provenance[event]
    if prov.capability != cap.cap_id or prov.initiator != address:
        raise ValueError("event not produced by query")
    if cap.requester_address is None:
        if address != network.root_address or network.root_result is not None:
            raise ValueError("malformed root result")
        network.root_result = event
        return
    secret = prior.query_secret(network, cap)
    signature = prior.return_signature(secret, cap, event, prov.evidence_digest)
    network.actor(cap.requester_address).mailbox.append(
        CarriedReturnEnvelope(
            cap,
            event,
            address,
            prov.evidence_digest,
            signature,
            network.output_payloads[event],
            network.output_sources[event],
        )
    )


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
    prevalidate_event_and_option(network, address, cap, option, params)

    # All capability, option, typed-leg and identity checks precede mutation.
    actor.issued_incoming.remove(cap.cap_id)
    actor.used_capabilities.add(cap.cap_id)
    network.transfers[cap.cap_id] = prior.transfer_record(cap)

    if option.action == "idle":
        event = create_idle(network, cap)
        issue_return(network, address, cap, event)
        return
    if option.action == "birth":
        event = create_birth(network, cap, params)
        issue_return(network, address, cap, event)
        return

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
        child_cap = prior.make_capability(
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
    actor.outstanding[call_id] = prior.OwnedCall(
        call_id, cap, option.action, option.target_ports, child_caps
    )
    for slot in sorted(child_caps):
        enqueue_query(network, child_caps[slot])


def process_return(
    network: Network,
    address: Address,
    envelope: CarriedReturnEnvelope,
    params: Params,
) -> None:
    call = prior.validate_return(network, address, envelope)
    if envelope.output_bit != network.output_payloads[envelope.result_event]:
        raise ValueError("return payload mismatch")
    if envelope.output_sources != network.output_sources[envelope.result_event]:
        raise ValueError("return source-set mismatch")
    assert envelope.capability.slot is not None
    if len(call.results) + 1 == len(call.child_caps):
        if event_storage_name(network, call.incoming) in network.collector.events:
            raise ValueError("duplicate merge identity")
    call.results[envelope.capability.slot] = envelope
    if len(call.results) != len(call.child_caps):
        return
    event = create_merge(network, call, params)
    del network.actor(address).outstanding[call.call_id]
    issue_return(network, address, call.incoming, event)


def peek_envelope(network: Network, scheduler: str) -> Tuple[Address, int, Envelope]:
    candidates = [
        (address, index, envelope)
        for address, actor in network.actors.items()
        for index, envelope in enumerate(actor.mailbox)
    ]
    if not candidates:
        raise ValueError("no deliverable mailbox")
    if scheduler == "fifo":
        return min(candidates, key=lambda row: (row[0], row[1]))
    if scheduler == "lifo":
        return max(candidates, key=lambda row: (row[0], row[1]))
    if scheduler == "canonical":
        return min(candidates, key=lambda row: prior.envelope_key(row[2]))
    raise ValueError("unknown serializer")


def acknowledge(network: Network, address: Address, index: int, envelope: Envelope) -> None:
    if network.actor(address).mailbox[index] != envelope:
        raise ValueError("mailbox changed before acknowledgement")
    network.actor(address).mailbox.pop(index)


def start_root_call(network: Network, request_payload: int = 0) -> int:
    if network.pending_count() or network.outstanding_count() or network.root_result is not None:
        raise ValueError("root call started with live work")
    root = network.actor(network.root_address)
    if root.issued_incoming:
        raise ValueError("root has stale issued capability")
    tx = root.call_ordinal
    if not isinstance(tx, int) or tx < 0:
        raise ValueError("root causal ordinal")
    network.current_tx = tx
    network.root_payload = request_payload
    network.collector.root_tip = root.tip
    network.call_lowers[tx] = root.tip
    cap = prior.make_capability(
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
        request_payload,
    )
    enqueue_query(network, cap)
    root.call_ordinal += 1
    return tx


def enumerate_network(
    initial: Network,
    params: Params,
    scheduler: str,
    request_payload: int = 0,
) -> List[NetBranch]:
    network = initial.clone()
    start_root_call(network, request_payload)
    frontier: List[Tuple[Fraction, Network]] = [(Fraction(1), network)]
    completed: List[NetBranch] = []
    while frontier:
        probability, state = frontier.pop()
        if state.root_result is not None:
            if state.pending_count() or state.outstanding_count():
                raise AssertionError("root returned with live work")
            state.collector.root_tip = state.root_result
            completed.append(NetBranch(probability, state))
            continue
        address, index, envelope = peek_envelope(state, scheduler)
        if isinstance(envelope, QueryEnvelope):
            for option in prior.local_options(state.actor(address), params):
                child = state.clone()
                process_query(child, address, envelope, option, params)
                acknowledge(child, address, index, envelope)
                frontier.append((probability * option.probability, child))
        else:
            process_return(state, address, envelope, params)
            acknowledge(state, address, index, envelope)
            frontier.append((probability, state))
    if sum(branch.probability for branch in completed) != 1:
        raise AssertionError("normalization")
    return completed


def reset_for_next_call(network: Network) -> Network:
    state = network.clone()
    state.root_result = None
    state.collector.transaction_events.clear()
    state.collector.queried_actors.clear()
    state.collector.local_reads.clear()
    state.collector.birth_checks.clear()
    return state


def seed_event_id(
    network: Network,
    event: str,
    memo: Optional[Dict[str, Tuple[object, ...]]] = None,
    ignore_source_value: bool = False,
) -> Tuple[object, ...]:
    cache = memo if memo is not None else {}
    if event in cache:
        return cache[event]
    raw = network.collector.events[event]
    actors = tuple(sorted(network.name_to_address[name] for name in raw.actors))
    flag = raw.flag
    if ignore_source_value and raw.kind == "source-seal":
        flag = "bounded-source-bit"
    predecessors = tuple(
        sorted(
            [
                (
                seed_event_id(network, pred, cache, ignore_source_value)
                if pred not in network.provenance
                else physical_event_id(network, pred, ignore_source_value=ignore_source_value)
                )
                for pred in raw.predecessors
            ],
            key=repr,
        )
    )
    result = ("seed-structural", raw.kind, actors, flag, predecessors)
    cache[event] = result
    return result


def physical_event_id(
    network: Network,
    event: str,
    ignore_source_value: bool = False,
) -> Tuple[object, ...]:
    if event in network.provenance:
        prov = network.provenance[event]
        return ("transaction", prov.tx, prov.event_address)
    return seed_event_id(network, event, ignore_source_value=ignore_source_value)


def physical_key(
    network: Network,
    ignore_source_value: bool = False,
    ignore_generated_evidence: bool = False,
) -> Tuple[object, ...]:
    actor_rows = []
    for address, actor in sorted(network.actors.items()):
        evidence = None if ignore_generated_evidence else (
            actor.evidence_bit,
            tuple(sorted(actor.evidence_sources)),
        )
        actor_rows.append(
            (
                address,
                actor.parent_address,
                actor.parent_port,
                tuple(sorted(actor.children.items())),
                physical_event_id(network, actor.tip, ignore_source_value),
                evidence,
                actor.call_ordinal,
            )
        )
    event_rows = []
    for event, prov in sorted(
        network.provenance.items(), key=lambda item: (item[1].tx, item[1].event_address)
    ):
        raw = network.collector.events[event]
        evidence = None if ignore_generated_evidence else (
            network.output_payloads[event],
            tuple(sorted(network.output_sources[event])),
            prov.evidence_digest,
        )
        event_rows.append(
            (
                physical_event_id(network, event, ignore_source_value),
                prov.initiator,
                prov.target_legs,
                prov.operation,
                prov.coupling,
                prov.route,
                network.local_outcomes[event],
                network.structural_alternatives[event],
                evidence,
                tuple(
                    sorted(
                        (
                            physical_event_id(network, pred, ignore_source_value)
                            for pred in raw.predecessors
                        ),
                        key=repr,
                    )
                ),
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
    return tuple(actor_rows), tuple(event_rows), tuple(amplitudes), transfer_rows


def distribution(
    branches: Sequence[NetBranch],
    ignore_source_value: bool = False,
    ignore_generated_evidence: bool = False,
) -> Dict[Tuple[object, ...], Fraction]:
    result: Dict[Tuple[object, ...], Fraction] = defaultdict(Fraction)
    for branch in branches:
        result[
            physical_key(branch.network, ignore_source_value, ignore_generated_evidence)
        ] += branch.probability
    return dict(sorted(result.items(), key=lambda item: repr(item[0])))


def root_kind_distribution(branches: Sequence[NetBranch]) -> Dict[str, Fraction]:
    return prior.root_kind_distribution(branches)


def full_projectivity(params: Params, first: Sequence[NetBranch]) -> Tuple[int, int, int]:
    first_dist = distribution(first)
    marginal: Dict[Tuple[object, ...], Fraction] = defaultdict(Fraction)
    refinements = 0
    persistence = 0
    for branch in first:
        key = physical_key(branch.network)
        old_prov = copy.deepcopy(branch.network.provenance)
        old_payloads = copy.deepcopy(branch.network.output_payloads)
        old_result = branch.network.root_result
        assert old_result
        seed = reset_for_next_call(branch.network)
        second = enumerate_network(seed, params, "canonical")
        refinements += len(second)
        for refined in second:
            if any(refined.network.provenance.get(event) != prov for event, prov in old_prov.items()):
                raise AssertionError("old provenance mutation")
            if any(refined.network.output_payloads.get(event) != value for event, value in old_payloads.items()):
                raise AssertionError("old payload mutation")
            if old_result not in refined.network.collector.ancestors(refined.network.root_result):
                raise AssertionError("root wire persistence")
            marginal[key] += branch.probability * refined.probability
            persistence += 1
    if dict(marginal) != first_dist:
        raise AssertionError("full projectivity")
    return len(first_dist), refinements, persistence


def matrix_zero(rows: int, columns: int) -> List[List[Fraction]]:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def embedded_rotation(n: int, control: int, target: int, c: Fraction, s: Fraction) -> List[List[Fraction]]:
    bases = tuple(itertools.product((0, 1), repeat=n))
    index = {basis: i for i, basis in enumerate(bases)}
    matrix = matrix_zero(len(bases), len(bases))
    for column, basis in enumerate(bases):
        for out, amplitude in prior.apply_crot_basis(basis, control, target, c, s).items():
            matrix[index[out]][column] = amplitude
    return matrix


def embedded_fork(n: int, control: int, targets: Tuple[int, int], c: Fraction, s: Fraction) -> List[List[Fraction]]:
    bases = tuple(itertools.product((0, 1), repeat=n))
    index = {basis: i for i, basis in enumerate(bases)}
    matrix = matrix_zero(len(bases), len(bases))
    for column, basis in enumerate(bases):
        partial = {basis: Fraction(1)}
        for target in targets:
            total: Dict[Tuple[int, ...], Fraction] = defaultdict(Fraction)
            for current, amplitude in partial.items():
                for out, factor in prior.apply_crot_basis(current, control, target, c, s).items():
                    total[out] += amplitude * factor
            partial = total
        for out, amplitude in partial.items():
            matrix[index[out]][column] = amplitude
    return matrix


def embedded_birth(n: int, control: int, c: Fraction, s: Fraction) -> List[List[Fraction]]:
    inputs = tuple(itertools.product((0, 1), repeat=n))
    outputs = tuple(itertools.product((0, 1), repeat=n + 1))
    index = {basis: i for i, basis in enumerate(outputs)}
    matrix = matrix_zero(len(outputs), len(inputs))
    for column, basis in enumerate(inputs):
        if basis[control] == 0:
            matrix[index[basis + (0,)]][column] = 1
        else:
            matrix[index[basis + (0,)]][column] = c
            matrix[index[basis + (1,)]][column] = s
    return matrix


def inject_block(matrix: Sequence[Sequence[Fraction]], offset: int, rows: int) -> List[List[Fraction]]:
    out = matrix_zero(rows, len(matrix[0]))
    for i, row in enumerate(matrix):
        out[offset + i] = list(row)
    return out


def common_flagged_instrument(params: Params) -> Tuple[int, int, int, int, int]:
    root = initial_network(params).actor(())
    options = prior.local_options(root, params)
    matrices = []
    for option in options:
        if option.action == "idle":
            matrix = prior.matrix_identity(8)
        elif option.action == "birth":
            matrix = embedded_birth(3, 0, params.birth_cos, params.birth_sin)
        elif option.action == "visit":
            matrix = embedded_rotation(
                3, 0, option.target_ports[0] + 1, params.interact_cos, params.interact_sin
            )
        elif option.action == "fork":
            matrix = embedded_fork(
                3,
                0,
                tuple(port + 1 for port in option.target_ports),
                params.interact_cos,
                params.interact_sin,
            )
        else:
            raise AssertionError(option)
        if prior.matmul(prior.transpose(matrix), matrix) != prior.matrix_identity(8):
            raise AssertionError("common-input isometry")
        matrices.append(matrix)

    total_rows = sum(len(matrix) for matrix in matrices)
    flagged = []
    offset = 0
    for matrix in matrices:
        flagged.append(inject_block(matrix, offset, total_rows))
        offset += len(matrix)
    cross = 0
    zero = matrix_zero(8, 8)
    for i, left in enumerate(flagged):
        for right in flagged[i + 1 :]:
            if prior.matmul(prior.transpose(left), right) != zero:
                raise AssertionError("flag ranges overlap")
            cross += 1
    weighted = matrix_zero(8, 8)
    for option, matrix in zip(options, flagged):
        gram = prior.matmul(prior.transpose(matrix), matrix)
        for i in range(8):
            for j in range(8):
                weighted[i][j] += option.probability * gram[i][j]
    if weighted != prior.matrix_identity(8):
        raise AssertionError("instrument completeness")
    local_rank = len({option.action for option in options})
    return len(options), 8, total_rows, cross, local_rank


def state_snapshot(network: Network) -> str:
    rows = []
    for address, actor in sorted(network.actors.items()):
        rows.append(
            (
                address,
                actor.tip,
                tuple(actor.mailbox),
                tuple(sorted(actor.outstanding)),
                tuple(sorted(actor.issued_incoming)),
                tuple(sorted(actor.used_capabilities)),
                actor.call_ordinal,
            )
        )
    return digest(
        (
            physical_key(network),
            rows,
            network.current_tx,
            network.root_result,
            network.call_lowers,
        )
    )


def closing_adversarial_gate(params: Params) -> Tuple[int, int, int]:
    rejected = 0
    unchanged = 0

    # A structurally valid-looking child query was never issued to B.
    network = initial_network(params)
    start_root_call(network)
    root = network.actor(())
    b = network.actor((0,))
    fake = prior.make_capability(
        prior.edge_key(network.namespace, (), 0, (0,)),
        network.namespace,
        network.current_tx,
        network.collector.root_tip,
        (),
        root.tip,
        (0,),
        0,
        (7, 7),
        7,
        "not-an-open-call",
        "not-an-issued-parent",
        ((), (0,)),
        0,
    )
    before = state_snapshot(network)
    try:
        process_query(network, (0,), QueryEnvelope(fake), LocalOption("idle", (), params.idle), params)
    except ValueError:
        rejected += 1
    else:
        raise AssertionError("unissued query accepted")
    unchanged += int(state_snapshot(network) == before)

    # Genuine root capability plus malformed/non-menu local choices.
    for option in (
        LocalOption("visit", (9,), Fraction(1)),
        LocalOption("fork", (0, 0), Fraction(1)),
        LocalOption("idle", (), Fraction(1)),
    ):
        candidate = initial_network(params)
        start_root_call(candidate)
        address, _index, envelope = peek_envelope(candidate, "canonical")
        assert isinstance(envelope, QueryEnvelope)
        before = state_snapshot(candidate)
        try:
            process_query(candidate, address, envelope, option, params)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError("malformed option accepted")
        unchanged += int(state_snapshot(candidate) == before)

    # Peek/process/ack semantics: a rejected envelope remains queued.
    candidate = initial_network(params)
    start_root_call(candidate)
    address, index, envelope = peek_envelope(candidate, "canonical")
    assert isinstance(envelope, QueryEnvelope)
    before = state_snapshot(candidate)
    try:
        process_query(
            candidate,
            address,
            envelope,
            LocalOption("fork", (0, 0), Fraction(1)),
            params,
        )
    except ValueError:
        rejected += 1
    else:
        raise AssertionError("service accepted malformed option")
    unchanged += int(state_snapshot(candidate) == before)
    queued = int(candidate.actor(address).mailbox[index] == envelope)
    return rejected, unchanged, queued


def root_observable(branch: NetBranch) -> Tuple[object, ...]:
    network = branch.network
    result = network.root_result
    assert result
    prov = network.provenance[result]
    return (
        prov.operation,
        tuple((role, address, port) for role, address, port in prov.target_legs),
        network.output_payloads[result],
        tuple(sorted(network.output_sources[result])),
    )


def root_observable_distribution(branches: Sequence[NetBranch]) -> Dict[Tuple[object, ...], Fraction]:
    result: Dict[Tuple[object, ...], Fraction] = defaultdict(Fraction)
    for branch in branches:
        result[root_observable(branch)] += branch.probability
    return dict(sorted(result.items(), key=lambda item: repr(item[0])))


def remote_evidence_gate(params: Params) -> Tuple[int, int, int, int]:
    zero = enumerate_network(initial_network(params, source_bit=0), params, "canonical")
    one = enumerate_network(initial_network(params, source_bit=1), params, "canonical")
    zero_by_structure = {
        physical_key(branch.network, True, True): branch for branch in zero
    }
    one_by_structure = {
        physical_key(branch.network, True, True): branch for branch in one
    }
    if set(zero_by_structure) != set(one_by_structure):
        raise AssertionError("source intervention changed structural support")
    reached = 0
    blocked = 0
    hop_checks = 0
    for key, branch0 in zero_by_structure.items():
        branch1 = one_by_structure[key]
        if branch0.probability != branch1.probability:
            raise AssertionError("source intervention changed opportunity weights")
        net0, net1 = branch0.network, branch1.network
        root0, root1 = net0.root_result, net1.root_result
        assert root0 and root1
        d_queried = any(prov.initiator == (0, 0) for prov in net1.provenance.values())
        if d_queried:
            reached += 1
            if net0.output_payloads[root0] != 0 or net1.output_payloads[root1] != 1:
                raise AssertionError("queried D source did not reach A2")
            if (0, 0) not in net1.output_sources[root1]:
                raise AssertionError("A2 lacks D source identity")
            d_events = [event for event, prov in net1.provenance.items() if prov.initiator == (0, 0)]
            if not all(net1.provenance[event].route == ((), (0,), (0, 0)) for event in d_events):
                raise AssertionError("D source route")
            hop_checks += len(d_events) + 2
        else:
            blocked += 1
            if net0.output_payloads[root0] != net1.output_payloads[root1]:
                raise AssertionError("unqueried D source leaked")
            if (0, 0) in net1.output_sources[root1]:
                raise AssertionError("unqueried D source identity leaked")

    remote0 = enumerate_network(
        initial_network(params, source_bit=0, remote_collision=True, remote_payload="remote-source=0"),
        params,
        "canonical",
    )
    remote1 = enumerate_network(
        initial_network(params, source_bit=0, remote_collision=True, remote_payload="remote-source=1"),
        params,
        "canonical",
    )
    disconnected_equal = int(
        root_observable_distribution(remote0) == root_observable_distribution(remote1)
    )
    if not disconnected_equal or not reached or not blocked:
        raise AssertionError("remote evidence controls")
    return reached, blocked, disconnected_equal, hop_checks


def deterministic_choice(actor: prior.LocalActor, cap: prior.Capability, params: Params, ticket: int) -> LocalOption:
    return prior.deterministic_choice(actor, cap, params, ticket)


def deterministic_call(network: Network, params: Params, scheduler: str, ticket: int) -> Network:
    state = network.clone()
    start_root_call(state)
    while state.root_result is None:
        address, index, envelope = peek_envelope(state, scheduler)
        if isinstance(envelope, QueryEnvelope):
            option = deterministic_choice(state.actor(address), envelope.capability, params, ticket)
            process_query(state, address, envelope, option, params)
        else:
            process_return(state, address, envelope, params)
        acknowledge(state, address, index, envelope)
    if state.pending_count() or state.outstanding_count():
        raise AssertionError("live work after deterministic call")
    state.collector.root_tip = state.root_result
    return state


def multi_call_replay(params: Params, scheduler: str, calls: int = 8) -> Network:
    network = initial_network(params)
    for call in range(calls):
        if call:
            network = reset_for_next_call(network)
        network = deterministic_call(network, params, scheduler, 1707)
    return network


def source_hash() -> str:
    return sha256(Path(__file__).read_bytes())


def main() -> None:
    gates: List[str] = []
    science: Dict[str, object] = {}
    print("[D35c exact closing companion]")
    print(f"prior_source_sha256={PRIOR_SHA256}")
    print("ARITHMETIC: Fraction exact")
    print("DURATION/RATE/NUMERICAL-PROPER-TIME VARIABLES: 0")
    print("root call ordinal: actor-owned causal successor label, not elapsed time")
    print("GLOBAL OPPORTUNITY NORMALIZERS: 0")
    print("SHARED JOINT AUDIT: persistent event DAG + exact entangled carrier vector")

    for params in (Q1, Q2):
        print(f"[{params.name}]")
        runs = {
            scheduler: enumerate_network(initial_network(params), params, scheduler)
            for scheduler in ("fifo", "lifo", "canonical")
        }
        dists = {scheduler: distribution(branches) for scheduler, branches in runs.items()}
        if not (dists["fifo"] == dists["lifo"] == dists["canonical"]):
            raise AssertionError("scheduler distribution")
        branches = runs["canonical"]
        print(
            "actor_serializers="
            + ",".join(
                f"{scheduler}:{len(value)}" for scheduler, value in runs.items()
            )
            + f" atoms={len(dists['canonical'])} total={frac_text(sum(b.probability for b in branches))}"
        )
        kinds = root_kind_distribution(branches)
        print("A2_kind=" + ",".join(f"{key}:{frac_text(value)}" for key, value in kinds.items()))
        gates.append(f"C1-{params.name}")

        seed_map = {
            "A0": "s0",
            "AB": "s1",
            "AC": "s2",
            "BD": "s3",
            "A1": "s4",
            "D-source-seal": "s5",
        }
        relabel = {"A": "R", "B": "Y", "C": "X", "D": "Z"}
        renamed = enumerate_network(
            initial_network(params, relabel=relabel, event_relabel=seed_map),
            params,
            "canonical",
        )
        if distribution(renamed) != dists["canonical"]:
            raise AssertionError("complete actor/event alpha quotient")
        alpha_atoms, alpha_refinements, alpha_persistence = full_projectivity(params, renamed)
        print(
            f"actor_event_alpha_atoms={len(distribution(renamed))} equal=yes "
            f"renamed_projectivity={alpha_atoms}/{alpha_refinements}/{alpha_persistence}"
        )
        gates.append(f"C2-{params.name}")

        atoms, refinements, persistence = full_projectivity(params, branches)
        print(
            f"full_first_atoms={atoms} second_refinements={refinements} "
            f"event_payload_persistence={persistence} marginal_equal=yes"
        )
        gates.append(f"C3-{params.name}")

        alternatives, input_dim, output_dim, cross, local_rank = common_flagged_instrument(params)
        print(
            f"common_input_dim={input_dim} direct_sum_output_dim={output_dim} "
            f"structural_alternatives={alternatives} bounded_local_outcome_rank={local_rank} "
            f"cross_range_zero={cross}/10 weighted_gram_identity=yes"
        )
        gates.append(f"C4-{params.name}")

        rejected, unchanged, queued = closing_adversarial_gate(params)
        inherited_rejected, inherited_unchanged = prior.adversarial_gate(params)
        if (rejected, unchanged, queued) != (5, 5, 1):
            raise AssertionError("closing adversarial gate")
        if (inherited_rejected, inherited_unchanged) != (9, 9):
            raise AssertionError("inherited adversarial regression")
        print(
            f"closing_rejections={rejected}/5 whole_state_unchanged={unchanged}/5 "
            f"rejected_envelope_still_queued={queued}/1 inherited={inherited_rejected}/{inherited_unchanged}"
        )
        gates.append(f"C5-{params.name}")

        reached, blocked, disconnected, hops = remote_evidence_gate(params)
        print(
            f"D_source_queried_histories={reached} unqueried_histories={blocked} "
            f"authenticated_return_hop_checks={hops} disconnected_projection_equal={disconnected} "
            "do_D0_to_D1_changes_A2_iff_queried=yes"
        )
        gates.append(f"C6-{params.name}")

        grown_checks = 0
        for branch in branches:
            seed = reset_for_next_call(branch.network)
            reference = distribution(enumerate_network(seed, params, "canonical"))
            for scheduler in ("fifo", "lifo"):
                if distribution(enumerate_network(seed, params, scheduler)) != reference:
                    raise AssertionError("grown scheduler")
                grown_checks += 1
        replays = [multi_call_replay(params, scheduler) for scheduler in ("fifo", "lifo", "canonical")]
        if not (physical_key(replays[0]) == physical_key(replays[1]) == physical_key(replays[2])):
            raise AssertionError("multi-call replay")
        root_ordinal = replays[0].actor(()).call_ordinal
        if root_ordinal != 8:
            raise AssertionError("root-owned call ordinal")
        print(
            f"grown_scheduler_checks={grown_checks} multi_call_replay=8 "
            f"root_owned_causal_ordinal={root_ordinal} exact_equal=yes"
        )
        gates.append(f"C7-{params.name}")

        science[params.name] = {
            "distribution": digest(dists["canonical"]),
            "kinds": {key: frac_text(value) for key, value in kinds.items()},
            "projectivity": (atoms, refinements, persistence),
            "alpha": digest(distribution(renamed)),
            "instrument": (alternatives, input_dim, output_dim, cross, local_rank),
            "evidence": (reached, blocked, disconnected, hops),
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
    gates.append("C8")

    print("[SCOPE]")
    print(
        "proved: supplied A-rooted laminar nested-call history family; logical actor mailboxes; "
        "structural CAP plus D-origin carried bit; common-input classical-output CQ instrument"
    )
    print(
        "shared representation: one persistent event DAG and exact joint entangled carrier vector; "
        "not OS processes and not a distributed quantum-state storage theorem"
    )
    print(
        "open: root-free initiator law; overlapping peers/cycles/joins; diamond-specification overlap; "
        "Q/g/root/ownership derivation; coherent graph-sector sum; v9 bridge; spacetime; nature's law"
    )
    gates.append("C9")

    if len(gates) != 16:
        raise AssertionError((len(gates), gates))
    science["gates"] = gates
    print("[HASHES]")
    print(f"source_sha256={source_hash()}")
    print(f"internal_science_sha256={digest(science)}")
    print("[VERDICT]")
    print("PASS 16/16")
    print("TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE")
    print("not a root-free universe law; opportunity weights and birth coupling remain unselected")


if __name__ == "__main__":
    main()
