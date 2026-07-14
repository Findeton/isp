#!/usr/bin/env python3
"""D35d terminal typed-identity companion.

The module hash-locks D35c, replaces raw storage names with disjoint typed
identity domains, validates root inputs before mutation, and upgrades the
disconnected source control to an isomorphic three-actor source gadget.
All inherited scientific kernels remain exact Fractions.
"""

from __future__ import annotations

import hashlib
import importlib.util
import sys
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, FrozenSet, Mapping, Optional, Sequence, Tuple


HERE = Path(__file__).resolve().parent
D35C_PATH = HERE / "d35c_local_specification_exact.py"
D35C_SHA256 = "50f1e710cc04de3576b24bd5e7414764f1dea1ebb86f0b0b5747d2b18109c765"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


if sha256(D35C_PATH.read_bytes()) != D35C_SHA256:
    raise RuntimeError("D35c source hash mismatch")
_SPEC = importlib.util.spec_from_file_location("d35c_locked", D35C_PATH)
assert _SPEC and _SPEC.loader
d35c = importlib.util.module_from_spec(_SPEC)
sys.modules["d35c_locked"] = d35c
_SPEC.loader.exec_module(d35c)


@dataclass(frozen=True, order=True)
class TypedId:
    domain: str
    coordinates: Tuple[object, ...]

    def __str__(self) -> str:
        return f"{self.domain}:{self.coordinates!r}"


Address = d35c.Address
Params = d35c.Params
Q1 = d35c.Q1
Q2 = d35c.Q2
Network = d35c.Network
NetBranch = d35c.NetBranch
LocalOption = d35c.LocalOption


_untyped_initial_network = d35c.initial_network
_unvalidated_start_root_call = d35c.start_root_call
_round3_closing_adversarial_gate = d35c.closing_adversarial_gate


def supplied_actor_id(display: object) -> TypedId:
    return TypedId("actor-supplied", (str(display),))


def supplied_event_id(display: object) -> TypedId:
    return TypedId("event-supplied", (str(display),))


def generated_actor_id(network: Network, path: Tuple[int, ...]) -> TypedId:
    return TypedId(
        "actor-generated",
        (network.namespace, network.current_tx, path),
    )


def generated_event_id(network: Network, path: Tuple[int, ...]) -> TypedId:
    return TypedId(
        "event-generated",
        (network.namespace, network.current_tx, path),
    )


def convert_supplied_storage_to_typed(network: Network) -> None:
    world = network.collector
    connected_names = set(network.name_to_address)
    actor_map = {
        name: (
            supplied_actor_id(name)
            if name in connected_names
            else TypedId("actor-disconnected-fixture", (str(name),))
        )
        for name in world.actors
    }
    event_map = {}
    for event, raw in world.events.items():
        connected = all(actor in connected_names for actor in raw.actors)
        domain = "event-supplied" if connected else "event-disconnected-fixture"
        event_map[event] = TypedId(domain, (str(event),))

    actors = {}
    for old, actor in world.actors.items():
        key = actor_map[old]
        actors[key] = d35c.prior.base.Actor(
            key,
            actor_map[actor.parent] if actor.parent is not None else None,
            sorted(actor_map[child] for child in actor.children),
            event_map[actor.tip],
        )
    events = {}
    for old, raw in world.events.items():
        key = event_map[old]
        events[key] = d35c.prior.base.Event(
            key,
            raw.kind,
            tuple(sorted(actor_map[actor] for actor in raw.actors)),
            tuple(event_map[pred] for pred in raw.predecessors),
            raw.flag,
        )
    amplitudes = {
        frozenset(actor_map[actor] for actor in occupied): amplitude
        for occupied, amplitude in world.amplitudes.items()
    }
    world.actors = actors
    world.events = events
    world.amplitudes = amplitudes
    world.root_tip = event_map[world.root_tip]
    world.transaction_events = [event_map[event] for event in world.transaction_events]
    world.queried_actors = [actor_map[actor] for actor in world.queried_actors]
    world.local_reads = [
        (actor_map[actor], tuple(actor_map[child] for child in children))
        for actor, children in world.local_reads
    ]

    for actor in network.actors.values():
        actor.name = actor_map[actor.name]
        actor.tip = event_map[actor.tip]
    network.name_to_address = {
        actor_map[name]: address for name, address in network.name_to_address.items()
    }
    network.root_actor = actor_map[network.root_actor]
    network.source_event = event_map[network.source_event]
    network.seed_payloads = {
        event_map[event]: payload for event, payload in network.seed_payloads.items()
    }


def add_isomorphic_disconnected_source_gadget(network: Network, bit: int) -> None:
    if bit not in (0, 1):
        raise ValueError("disconnected source bit")
    world = network.collector
    u = TypedId("actor-control", ("u",))
    v = TypedId("actor-control", ("v",))
    w = TypedId("actor-control", ("w",))
    e0 = TypedId("event-control", ("u0",))
    e1 = TypedId("event-control", ("uv",))
    e2 = TypedId("event-control", ("vw",))
    e3 = TypedId("event-control", ("w-source-seal",))
    for actor in (u, v, w):
        if actor in world.actors:
            raise ValueError("duplicate control actor")
    world.actors[u] = d35c.prior.base.Actor(u, None, [v], e1)
    world.actors[v] = d35c.prior.base.Actor(v, u, [w], e2)
    world.actors[w] = d35c.prior.base.Actor(w, v, [], e3)
    world.events[e0] = d35c.prior.base.Event(e0, "seed", (u,), (), "seed")
    world.events[e1] = d35c.prior.base.Event(
        e1, "seed-birth", (u, v), (e0,), "seed-birth"
    )
    world.events[e2] = d35c.prior.base.Event(
        e2, "seed-birth", (v, w), (e1,), "seed-birth"
    )
    world.events[e3] = d35c.prior.base.Event(
        e3,
        "source-seal",
        (w,),
        (e2,),
        ("bounded-source-bit", bit),
    )
    network.control_source_event = e3


def initial_network(
    params: Params,
    namespace: str = "ROOT-CAP-0",
    relabel: Optional[Mapping[str, str]] = None,
    source_bit: int = 0,
    event_relabel: Optional[Mapping[str, str]] = None,
    remote_collision: bool = False,
    remote_payload: str = "remote-a",
    disconnected_source_bit: Optional[int] = None,
) -> Network:
    network = _untyped_initial_network(
        params,
        namespace=namespace,
        relabel=relabel,
        source_bit=source_bit,
        event_relabel=event_relabel,
        remote_collision=remote_collision,
        remote_payload=remote_payload,
    )
    convert_supplied_storage_to_typed(network)
    if disconnected_source_bit is not None:
        add_isomorphic_disconnected_source_gadget(network, disconnected_source_bit)
    return network


def event_storage_name(network: Network, cap: d35c.prior.Capability) -> TypedId:
    return generated_event_id(network, cap.path)


def prevalidate_event_and_option(
    network: Network,
    address: Address,
    cap: d35c.prior.Capability,
    option: LocalOption,
    params: Params,
) -> None:
    actor = network.actor(address)
    if option not in d35c.prior.local_options(actor, params):
        raise ValueError("option not in actor local menu")
    if option.action == "idle":
        d35c.prior.validate_typed_event(network, address, "idle", ())
    elif option.action == "birth":
        port = 0 if not actor.children else max(actor.children) + 1
        d35c.prior.validate_typed_event(network, address, "birth", (port,))
        child_address = address + (port,)
        child_name = generated_actor_id(network, cap.path)
        if child_address in network.actors or child_name in network.name_to_address:
            raise ValueError("duplicate newborn")
    else:
        d35c.prior.validate_typed_event(
            network, address, option.action, option.target_ports
        )
    if event_storage_name(network, cap) in network.collector.events:
        raise ValueError("duplicate generated event identity")


def create_idle(network: Network, cap: d35c.prior.Capability) -> TypedId:
    address = cap.target_address
    actor = network.actor(address)
    world = network.collector
    event = generated_event_id(network, cap.path)
    lower = world.actors[actor.name].tip
    world.add_event(
        event,
        "idle",
        (actor.name,),
        (lower, cap.root_event, cap.requester_lower),
        "idle",
    )
    network.sync_tips((actor.name,))
    d35c.record_event(
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


def create_birth(network: Network, cap: d35c.prior.Capability, params: Params) -> TypedId:
    address = cap.target_address
    actor = network.actor(address)
    world = network.collector
    port = 0 if not actor.children else max(actor.children) + 1
    child_address = address + (port,)
    child_name = generated_actor_id(network, cap.path)
    event = generated_event_id(network, cap.path)
    lower = world.actors[actor.name].tip
    before = world.p_one(actor.name)
    world.add_actor(child_name, actor.name)
    world.add_event(
        event,
        "birth",
        (actor.name, child_name),
        (lower, cap.root_event, cap.requester_lower),
        "birth",
    )
    world.apply_controlled_rotation(
        actor.name, child_name, params.birth_cos, params.birth_sin
    )
    after = world.p_one(child_name)
    world.birth_checks.append((before, after, params.g))
    if after != params.g * before or world.norm() != 1:
        raise AssertionError("D24 typed birth")

    actor.children[port] = child_address
    child = d35c.prior.LocalActor(
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
    key = d35c.prior.edge_key(network.namespace, address, port, child_address)
    actor.edge_keys[child_address] = key
    child.edge_keys[address] = key
    network.actors[child_address] = child
    network.name_to_address[child_name] = child_address
    network.sync_tips((actor.name, child_name))
    legs = (("newborn-target", child_address, port),)
    d35c.record_event(
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


def create_merge(
    network: Network,
    call: d35c.prior.OwnedCall,
    params: Params,
) -> TypedId:
    cap = call.incoming
    address = cap.target_address
    actor = network.actor(address)
    world = network.collector
    legs = d35c.prior.validate_typed_event(
        network, address, call.action, call.target_ports
    )
    target_actors = tuple(network.actor(actor.children[port]) for port in call.target_ports)
    targets = tuple(target.name for target in target_actors)
    returned = tuple(call.results[slot].result_event for slot in range(len(targets)))
    for target, result in zip(targets, returned):
        if world.actors[target].tip != result:
            raise ValueError("stale returned tip")
    child_bits = tuple(call.results[slot].output_bit for slot in range(len(targets)))
    child_sources = tuple(call.results[slot].output_sources for slot in range(len(targets)))
    output_bit = max((actor.evidence_bit, *child_bits))
    output_sources = frozenset().union(actor.evidence_sources, *child_sources)
    event = generated_event_id(network, cap.path)
    lower = world.actors[actor.name].tip
    world.add_event(
        event,
        call.action,
        (actor.name, *targets),
        (lower, cap.root_event, cap.requester_lower, *returned),
        call.action,
    )
    for target in sorted(targets):
        world.apply_controlled_rotation(
            actor.name,
            target,
            params.interact_cos,
            params.interact_sin,
        )
    if world.norm() != 1:
        raise AssertionError("typed interaction unitary")
    network.sync_tips((actor.name, *targets))
    coupling = params.interact_sin * params.interact_sin
    d35c.record_event(
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
    for target in target_actors:
        target.evidence_bit = output_bit
        target.evidence_sources = output_sources
    return event


def start_root_call(network: Network, request_payload: int = 0) -> int:
    if request_payload not in (0, 1):
        raise ValueError("root request payload must be a bit")
    return _unvalidated_start_root_call(network, request_payload)


def closing_adversarial_gate(params: Params) -> Tuple[int, int, int]:
    rejected, unchanged, queued = _round3_closing_adversarial_gate(params)
    network = initial_network(params)
    before = d35c.state_snapshot(network)
    try:
        start_root_call(network, 2)
    except ValueError:
        rejected += 1
    else:
        raise AssertionError("non-bit root input accepted")
    unchanged += int(d35c.state_snapshot(network) == before)
    return rejected, unchanged, queued


def source_reach_probability(params: Params) -> Fraction:
    branches = d35c.enumerate_network(initial_network(params, source_bit=1), params, "canonical")
    return sum(
        (
            branch.probability
            for branch in branches
            if (0, 0) in branch.network.output_sources[branch.network.root_result]
        ),
        Fraction(0),
    )


def remote_evidence_gate(params: Params) -> Tuple[int, int, int, int, Fraction]:
    reached, blocked, _old_disconnected, hops = _round3_remote_evidence_gate(params)
    remote0 = d35c.enumerate_network(
        initial_network(params, source_bit=0, disconnected_source_bit=0),
        params,
        "canonical",
    )
    remote1 = d35c.enumerate_network(
        initial_network(params, source_bit=0, disconnected_source_bit=1),
        params,
        "canonical",
    )
    disconnected_equal = int(
        d35c.root_observable_distribution(remote0)
        == d35c.root_observable_distribution(remote1)
    )
    if not disconnected_equal:
        raise AssertionError("isomorphic disconnected source leaked")
    return reached, blocked, disconnected_equal, hops, source_reach_probability(params)


def typed_collision_gate(params: Params) -> Tuple[int, int, int, int]:
    event_map_next = {
        "A0": "EROOT-CAP-0::T1:r",
        "AB": "event-b",
        "AC": "event-c",
        "BD": "event-d",
        "A1": "event-a1",
        "D-source-seal": "event-source",
    }
    next_first = d35c.enumerate_network(
        initial_network(params, event_relabel=event_map_next), params, "canonical"
    )
    atoms, refinements, persistence = d35c.full_projectivity(params, next_first)

    event_map_late = dict(event_map_next)
    event_map_late["A0"] = "EROOT-CAP-0::T5:r"
    late = initial_network(params, event_relabel=event_map_late)
    for call in range(6):
        if call:
            late = d35c.reset_for_next_call(late)
        late = d35c.deterministic_call(late, params, "canonical", 2903)
    if late.actor(()).call_ordinal != 6:
        raise AssertionError("late typed collision continuation")

    actor_map = {
        "A": "actor-a",
        "B": "actor-b",
        "C": "actor-c",
        "D": "NROOT-CAP-0::T0:r",
    }
    actor_collision = d35c.enumerate_network(
        initial_network(params, relabel=actor_map), params, "canonical"
    )
    if len(actor_collision) != 16 or sum(b.probability for b in actor_collision) != 1:
        raise AssertionError("typed actor collision")
    return atoms, refinements, persistence, late.actor(()).call_ordinal


_round3_remote_evidence_gate = d35c.remote_evidence_gate

# Install the typed terminal realization into the reviewed D35c algorithms.
d35c.initial_network = initial_network
d35c.event_storage_name = event_storage_name
d35c.prevalidate_event_and_option = prevalidate_event_and_option
d35c.create_idle = create_idle
d35c.create_birth = create_birth
d35c.create_merge = create_merge
d35c.start_root_call = start_root_call
d35c.closing_adversarial_gate = closing_adversarial_gate
d35c.remote_evidence_gate = remote_evidence_gate


def source_hash() -> str:
    return sha256(Path(__file__).read_bytes())


def main() -> None:
    gates = []
    science: Dict[str, object] = {}
    print("[D35d typed-identity terminal companion]")
    print(f"prior_source_sha256={D35C_SHA256}")
    print("ARITHMETIC: Fraction exact")
    print("DURATION/RATE/NUMERICAL-PROPER-TIME VARIABLES: 0")
    print("root call ordinal: actor-owned causal successor label, not elapsed time")
    print("GLOBAL OPPORTUNITY NORMALIZERS: 0")
    print("IDENTITY DOMAINS: supplied/generated actor/event/control are disjoint types")

    for params in (Q1, Q2):
        print(f"[{params.name}]")
        runs = {
            scheduler: d35c.enumerate_network(initial_network(params), params, scheduler)
            for scheduler in ("fifo", "lifo", "canonical")
        }
        distributions = {
            scheduler: d35c.distribution(branches)
            for scheduler, branches in runs.items()
        }
        if not (
            distributions["fifo"]
            == distributions["lifo"]
            == distributions["canonical"]
        ):
            raise AssertionError("typed scheduler distribution")
        branches = runs["canonical"]
        kinds = d35c.root_kind_distribution(branches)
        print(
            f"serializers=fifo:{len(runs['fifo'])},lifo:{len(runs['lifo'])},canonical:{len(branches)} "
            f"atoms={len(distributions['canonical'])} total={d35c.frac_text(sum(b.probability for b in branches))}"
        )
        print("A2_kind=" + ",".join(f"{key}:{d35c.frac_text(value)}" for key, value in kinds.items()))
        gates.append(f"T1-{params.name}")

        seed_map = {
            "A0": "s0",
            "AB": "s1",
            "AC": "s2",
            "BD": "s3",
            "A1": "s4",
            "D-source-seal": "s5",
        }
        actor_map = {"A": "R", "B": "Y", "C": "X", "D": "Z"}
        renamed = d35c.enumerate_network(
            initial_network(params, relabel=actor_map, event_relabel=seed_map),
            params,
            "canonical",
        )
        if d35c.distribution(renamed) != distributions["canonical"]:
            raise AssertionError("typed ordinary alpha quotient")
        alpha_atoms, alpha_refinements, alpha_persistence = d35c.full_projectivity(params, renamed)
        print(
            f"ordinary_actor_event_alpha={len(d35c.distribution(renamed))} equal=yes "
            f"renamed_projectivity={alpha_atoms}/{alpha_refinements}/{alpha_persistence}"
        )
        gates.append(f"T2-{params.name}")

        collision = typed_collision_gate(params)
        print(
            f"typed_display_collision_projectivity={collision[0]}/{collision[1]}/{collision[2]} "
            f"late_collision_calls={collision[3]}/6 newborn_display_collision=pass"
        )
        gates.append(f"T3-{params.name}")

        atoms, refinements, persistence = d35c.full_projectivity(params, branches)
        print(
            f"full_first_atoms={atoms} second_refinements={refinements} "
            f"event_payload_persistence={persistence} marginal_equal=yes"
        )
        gates.append(f"T4-{params.name}")

        instrument = d35c.common_flagged_instrument(params)
        print(
            f"common_input_dim={instrument[1]} direct_sum_output_dim={instrument[2]} "
            f"alternatives={instrument[0]} bounded_outcome_rank={instrument[4]} "
            f"cross_zero={instrument[3]}/10 weighted_identity=yes"
        )
        gates.append(f"T5-{params.name}")

        rejected, unchanged, queued = closing_adversarial_gate(params)
        inherited = d35c.prior.adversarial_gate(params)
        if (rejected, unchanged, queued) != (6, 6, 1) or inherited != (9, 9):
            raise AssertionError("terminal rejection battery")
        print(
            f"closing_rejections={rejected}/6 whole_state_unchanged={unchanged}/6 "
            f"rejected_queued={queued}/1 inherited={inherited[0]}/{inherited[1]}"
        )
        gates.append(f"T6-{params.name}")

        reached, blocked, disconnected, hops, reach_probability = remote_evidence_gate(params)
        print(
            f"D_queried_histories={reached} D_unqueried_histories={blocked} "
            f"P_D_reaches_A2={d35c.frac_text(reach_probability)} return_hops={hops} "
            f"isomorphic_disconnected_projection_equal={disconnected}"
        )
        gates.append(f"T7-{params.name}")

        grown = 0
        for branch in branches:
            seed = d35c.reset_for_next_call(branch.network)
            reference = d35c.distribution(
                d35c.enumerate_network(seed, params, "canonical")
            )
            for scheduler in ("fifo", "lifo"):
                if d35c.distribution(
                    d35c.enumerate_network(seed, params, scheduler)
                ) != reference:
                    raise AssertionError("typed grown scheduler")
                grown += 1
        replays = [
            d35c.multi_call_replay(params, scheduler)
            for scheduler in ("fifo", "lifo", "canonical")
        ]
        if not (
            d35c.physical_key(replays[0])
            == d35c.physical_key(replays[1])
            == d35c.physical_key(replays[2])
        ):
            raise AssertionError("typed multi-call replay")
        print(
            f"grown_scheduler_checks={grown} multi_call_replay=8 "
            f"root_owned_ordinal={replays[0].actor(()).call_ordinal} exact_equal=yes"
        )
        gates.append(f"T8-{params.name}")

        science[params.name] = {
            "distribution": d35c.digest(distributions["canonical"]),
            "kinds": {key: d35c.frac_text(value) for key, value in kinds.items()},
            "alpha": (alpha_atoms, alpha_refinements, alpha_persistence),
            "collision": collision,
            "projectivity": (atoms, refinements, persistence),
            "instrument": instrument,
            "evidence": (
                reached,
                blocked,
                disconnected,
                hops,
                d35c.frac_text(reach_probability),
            ),
            "multi": d35c.digest(d35c.physical_key(replays[0])),
        }

    q1 = d35c.root_kind_distribution(
        d35c.enumerate_network(initial_network(Q1), Q1, "canonical")
    )
    q2 = d35c.root_kind_distribution(
        d35c.enumerate_network(initial_network(Q2), Q2, "canonical")
    )
    print("[NONSELECTION]")
    print(
        f"birth_Q1={d35c.frac_text(q1['birth'])} birth_Q2={d35c.frac_text(q2['birth'])}; "
        f"visit_Q1={d35c.frac_text(q1['visit'])} visit_Q2={d35c.frac_text(q2['visit'])}; "
        "reach_Q1=1/16 reach_Q2=3/40"
    )
    gates.append("T9")

    print("[SCOPE]")
    print(
        "proved: typed alpha-safe supplied A-rooted laminar nested-call family; "
        "logical actor protocol; D-origin bounded evidence; common-input CQ instrument"
    )
    print(
        "open: overlapping/root-free diamond specification; peer/cycle/join sectors; "
        "Q/g/root selection; coherent graph support; v9 bridge; spacetime; nature's law"
    )
    gates.append("T10")

    if len(gates) != 18:
        raise AssertionError((len(gates), gates))
    science["gates"] = gates
    print("[HASHES]")
    print(f"source_sha256={source_hash()}")
    print(f"internal_science_sha256={d35c.digest(science)}")
    print("[VERDICT]")
    print("PASS 18/18")
    print("TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE")
    print("not a root-free universe law; q, g, root and overlap law remain unselected")


if __name__ == "__main__":
    main()
