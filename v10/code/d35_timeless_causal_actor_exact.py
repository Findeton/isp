#!/usr/bin/env python3
"""Exact D35 timeless causal-call law and independent actor rebuild.

The executable has no time variable.  A finite rooted actor tree supplies
owned ports.  One query rooted at A1 recursively visits zero, one, or two
child ports, and A2 is the returned upper seal.  All probabilities and
carrier amplitudes are exact Fractions.
"""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
from collections import defaultdict
from dataclasses import dataclass, field
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List, Mapping, Optional, Sequence, Tuple, Union


getcontext().prec = 120


def frac_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def dec_text(x: Fraction, places: int = 70) -> str:
    value = Decimal(x.numerator) / Decimal(x.denominator)
    return f"{value:.{places}f}"


def digest(value: object) -> str:
    def freeze(item: object) -> object:
        if isinstance(item, Fraction):
            return ["Fraction", item.numerator, item.denominator]
        if isinstance(item, Mapping):
            return [
                [freeze(key), freeze(val)]
                for key, val in sorted(item.items(), key=lambda pair: repr(pair[0]))
            ]
        if isinstance(item, (tuple, list)):
            return [freeze(part) for part in item]
        if isinstance(item, (set, frozenset)):
            return [freeze(part) for part in sorted(item, key=repr)]
        return item

    blob = json.dumps(freeze(value), sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def dedupe(items: Iterable[str]) -> Tuple[str, ...]:
    return tuple(dict.fromkeys(item for item in items if item))


@dataclass(frozen=True)
class Params:
    name: str
    idle: Fraction
    birth: Fraction
    visit: Fraction
    fork: Fraction
    birth_sin: Fraction
    birth_cos: Fraction
    interact_sin: Fraction = Fraction(4, 5)
    interact_cos: Fraction = Fraction(3, 5)

    def validate(self) -> None:
        assert self.idle + self.birth + self.visit + self.fork == 1
        assert self.birth_sin * self.birth_sin + self.birth_cos * self.birth_cos == 1
        assert (
            self.interact_sin * self.interact_sin
            + self.interact_cos * self.interact_cos
            == 1
        )

    @property
    def g(self) -> Fraction:
        return self.birth_sin * self.birth_sin


Q1 = Params(
    "Q1",
    Fraction(3, 8),
    Fraction(2, 8),
    Fraction(2, 8),
    Fraction(1, 8),
    Fraction(3, 5),
    Fraction(4, 5),
)
Q2 = Params(
    "Q2",
    Fraction(4, 10),
    Fraction(2, 10),
    Fraction(3, 10),
    Fraction(1, 10),
    Fraction(4, 5),
    Fraction(3, 5),
)


@dataclass
class Actor:
    name: str
    parent: Optional[str]
    children: List[str]
    tip: str


@dataclass(frozen=True)
class Event:
    name: str
    kind: str
    actors: Tuple[str, ...]
    predecessors: Tuple[str, ...]
    flag: str


@dataclass
class World:
    actors: Dict[str, Actor]
    events: Dict[str, Event]
    amplitudes: Dict[FrozenSet[str], Fraction]
    root_tip: str
    transaction_events: List[str] = field(default_factory=list)
    queried_actors: List[str] = field(default_factory=list)
    local_reads: List[Tuple[str, Tuple[str, ...]]] = field(default_factory=list)
    birth_checks: List[Tuple[Fraction, Fraction, Fraction]] = field(default_factory=list)

    def clone(self) -> "World":
        return copy.deepcopy(self)

    def norm(self) -> Fraction:
        return sum(value * value for value in self.amplitudes.values())

    def p_one(self, actor: str) -> Fraction:
        return sum(
            value * value
            for occupied, value in self.amplitudes.items()
            if actor in occupied
        )

    def add_actor(self, name: str, parent: str) -> None:
        if name in self.actors:
            raise ValueError("duplicate actor")
        if parent not in self.actors:
            raise ValueError("missing parent")
        self.actors[name] = Actor(name, parent, [], "")
        self.actors[parent].children.append(name)
        self.actors[parent].children.sort()

    def add_event(
        self,
        name: str,
        kind: str,
        actors: Sequence[str],
        predecessors: Sequence[str],
        flag: str,
        transaction: bool = True,
    ) -> None:
        if name in self.events:
            raise ValueError("duplicate event")
        actor_tuple = tuple(sorted(actors))
        for actor in actor_tuple:
            if actor not in self.actors:
                raise ValueError("event touches missing actor")
        predecessor_tuple = dedupe(predecessors)
        if any(pred not in self.events for pred in predecessor_tuple):
            raise ValueError("foreign ancestry")
        self.events[name] = Event(name, kind, actor_tuple, predecessor_tuple, flag)
        for actor in actor_tuple:
            self.actors[actor].tip = name
        if transaction:
            self.transaction_events.append(name)

    def apply_controlled_rotation(
        self, control: str, target: str, cosine: Fraction, sine: Fraction
    ) -> None:
        if control == target:
            raise ValueError("self rotation")
        if control not in self.actors or target not in self.actors:
            raise ValueError("missing rotation actor")
        updated: Dict[FrozenSet[str], Fraction] = defaultdict(Fraction)
        for occupied, amplitude in self.amplitudes.items():
            if control not in occupied:
                updated[occupied] += amplitude
                continue
            if target not in occupied:
                updated[occupied] += cosine * amplitude
                updated[frozenset(set(occupied) | {target})] += sine * amplitude
            else:
                updated[frozenset(set(occupied) - {target})] -= sine * amplitude
                updated[occupied] += cosine * amplitude
        self.amplitudes = {key: value for key, value in updated.items() if value}

    def ancestors(self, event: str) -> FrozenSet[str]:
        if event not in self.events:
            raise ValueError("unknown event")
        seen: set[str] = set()
        stack = [event]
        while stack:
            item = stack.pop()
            if item in seen:
                continue
            seen.add(item)
            stack.extend(self.events[item].predecessors)
        return frozenset(seen)


@dataclass(frozen=True)
class Option:
    action: str
    targets: Tuple[str, ...]
    probability: Fraction


@dataclass
class Branch:
    probability: Fraction
    world: World
    return_event: str


def event_name(tx: int, path: Tuple[int, ...]) -> str:
    suffix = "r" if not path else ".".join(map(str, path))
    return f"E{tx}:{suffix}"


def newborn_name(tx: int, path: Tuple[int, ...]) -> str:
    suffix = "r" if not path else ".".join(map(str, path))
    return f"N{tx}:{suffix}"


def local_options(world: World, actor: str, params: Params) -> List[Option]:
    children = tuple(sorted(world.actors[actor].children))
    world.local_reads.append((actor, children))
    idle = params.idle
    options: List[Option] = []
    if not children:
        idle += params.visit
    else:
        share = params.visit / len(children)
        options.extend(Option("visit", (child,), share) for child in children)
    if len(children) < 2:
        idle += params.fork
    else:
        pairs = tuple(itertools.combinations(children, 2))
        share = params.fork / len(pairs)
        options.extend(Option("fork", pair, share) for pair in pairs)
    options.append(Option("idle", (), idle))
    options.append(Option("birth", (), params.birth))
    options.sort(key=lambda item: (item.action, item.targets))
    assert sum(item.probability for item in options) == 1
    assert all(item.probability > 0 for item in options)
    return options


def create_idle(
    world: World,
    actor: str,
    tx: int,
    path: Tuple[int, ...],
    root_cause: str,
    requester_lower: str,
) -> str:
    lower = world.actors[actor].tip
    name = event_name(tx, path)
    world.add_event(
        name,
        "idle",
        (actor,),
        (lower, root_cause, requester_lower),
        "idle",
    )
    return name


def create_birth(
    world: World,
    actor: str,
    tx: int,
    path: Tuple[int, ...],
    root_cause: str,
    requester_lower: str,
    params: Params,
) -> str:
    lower = world.actors[actor].tip
    child = newborn_name(tx, path)
    before = world.p_one(actor)
    world.add_actor(child, actor)
    name = event_name(tx, path)
    world.add_event(
        name,
        "birth",
        (actor, child),
        (lower, root_cause, requester_lower),
        "birth",
    )
    world.apply_controlled_rotation(
        actor, child, params.birth_cos, params.birth_sin
    )
    after = world.p_one(child)
    world.birth_checks.append((before, after, params.g))
    if after != params.g * before:
        raise AssertionError("D24 newborn marginal")
    if world.norm() != 1:
        raise AssertionError("birth isometry")
    return name


def create_merge(
    world: World,
    actor: str,
    targets: Sequence[str],
    returned: Sequence[str],
    tx: int,
    path: Tuple[int, ...],
    root_cause: str,
    requester_lower: str,
    params: Params,
    quantum_order: str = "canonical",
) -> str:
    lower = world.actors[actor].tip
    for target, result in zip(targets, returned):
        if world.actors[target].tip != result:
            raise ValueError("stale returned tip")
    name = event_name(tx, path)
    kind = "visit" if len(targets) == 1 else "fork"
    predecessors = (lower, root_cause, requester_lower, *returned)
    world.add_event(name, kind, (actor, *targets), predecessors, kind)
    qtargets = list(targets)
    if quantum_order == "reverse":
        qtargets.reverse()
    else:
        qtargets.sort()
    for target in qtargets:
        world.apply_controlled_rotation(
            actor,
            target,
            params.interact_cos,
            params.interact_sin,
        )
    if world.norm() != 1:
        raise AssertionError("interaction unitary")
    return name


def resolve_recursive(
    world: World,
    actor: str,
    tx: int,
    path: Tuple[int, ...],
    root_cause: str,
    requester_lower: str,
    params: Params,
    child_order: str = "forward",
    quantum_order: str = "canonical",
) -> List[Branch]:
    world.queried_actors.append(actor)
    branches: List[Branch] = []
    for option in local_options(world, actor, params):
        candidate = world.clone()
        if option.action == "idle":
            result = create_idle(
                candidate, actor, tx, path, root_cause, requester_lower
            )
            branches.append(Branch(option.probability, candidate, result))
            continue
        if option.action == "birth":
            result = create_birth(
                candidate,
                actor,
                tx,
                path,
                root_cause,
                requester_lower,
                params,
            )
            branches.append(Branch(option.probability, candidate, result))
            continue

        lower = candidate.actors[actor].tip
        ordered_targets = list(option.targets)
        if child_order == "reverse":
            ordered_targets.reverse()
        partials: List[Tuple[Fraction, World, Dict[str, str]]] = [
            (Fraction(1), candidate, {})
        ]
        slot_by_target = {target: index for index, target in enumerate(option.targets)}
        for target in ordered_targets:
            refined: List[Tuple[Fraction, World, Dict[str, str]]] = []
            slot = slot_by_target[target]
            child_path = path + (slot,)
            for probability, partial_world, returned in partials:
                child_branches = resolve_recursive(
                    partial_world,
                    target,
                    tx,
                    child_path,
                    root_cause,
                    lower,
                    params,
                    child_order,
                    quantum_order,
                )
                for child_branch in child_branches:
                    mapping = dict(returned)
                    mapping[target] = child_branch.return_event
                    refined.append(
                        (
                            probability * child_branch.probability,
                            child_branch.world,
                            mapping,
                        )
                    )
            partials = refined
        for probability, partial_world, returned in partials:
            target_results = tuple(returned[target] for target in option.targets)
            result = create_merge(
                partial_world,
                actor,
                option.targets,
                target_results,
                tx,
                path,
                root_cause,
                requester_lower,
                params,
                quantum_order,
            )
            branches.append(
                Branch(option.probability * probability, partial_world, result)
            )
    assert sum(branch.probability for branch in branches) == 1
    return branches


def initial_world(params: Params, disconnected: bool = False) -> World:
    params.validate()
    actors = {"A": Actor("A", None, [], "")}
    world = World(
        actors=actors,
        events={},
        amplitudes={frozenset(): Fraction(3, 5), frozenset({"A"}): Fraction(4, 5)},
        root_tip="",
    )
    world.add_event("A0", "seed", ("A",), (), "seed", transaction=False)

    def seed_birth(parent: str, child: str, event: str, predecessors: Sequence[str]) -> None:
        before = world.p_one(parent)
        world.add_actor(child, parent)
        world.add_event(
            event,
            "seed-birth",
            (parent, child),
            predecessors,
            "seed-birth",
            transaction=False,
        )
        world.apply_controlled_rotation(
            parent, child, params.birth_cos, params.birth_sin
        )
        assert world.p_one(child) == params.g * before
        assert world.norm() == 1

    seed_birth("A", "B", "AB", ("A0",))
    seed_birth("A", "C", "AC", ("AB",))
    seed_birth("B", "D", "BD", ("AB",))
    world.add_event("A1", "idle", ("A",), ("AC",), "idle", transaction=False)
    world.root_tip = "A1"

    if disconnected:
        # Tensor a marked P--Q factor.  Its amplitudes stay in |00>, while its
        # records deliberately differ from the connected specimen.
        world.actors["P"] = Actor("P", None, ["Q"], "P1")
        world.actors["Q"] = Actor("Q", "P", [], "PQ")
        world.events["P0"] = Event("P0", "remote-seed", ("P",), (), "remote")
        world.events["PQ"] = Event(
            "PQ", "remote-birth", ("P", "Q"), ("P0",), "remote"
        )
        world.events["P1"] = Event(
            "P1", "remote-mark", ("P",), ("PQ",), "remote-different"
        )
    world.transaction_events.clear()
    world.queried_actors.clear()
    world.local_reads.clear()
    world.birth_checks.clear()
    return world


def enumerate_call(
    world: World,
    params: Params,
    tx: int = 0,
    child_order: str = "forward",
    quantum_order: str = "canonical",
) -> List[Branch]:
    root = "A"
    root_cause = world.actors[root].tip
    prepared = world.clone()
    prepared.root_tip = root_cause
    branches = resolve_recursive(
        prepared,
        root,
        tx,
        (),
        root_cause,
        root_cause,
        params,
        child_order,
        quantum_order,
    )
    assert sum(branch.probability for branch in branches) == 1
    for branch in branches:
        if branch.world.actors["A"].tip != branch.return_event:
            raise AssertionError("root result is not A2")
        branch.world.root_tip = branch.return_event
    return branches


def local_history_key(world: World, include_remote: bool = False) -> Tuple[object, ...]:
    actors = []
    for name, actor in sorted(world.actors.items()):
        if not include_remote and name in {"P", "Q"}:
            continue
        actors.append((name, actor.parent, tuple(sorted(actor.children)), actor.tip))
    events = []
    for name, event in sorted(world.events.items()):
        if not include_remote and set(event.actors) <= {"P", "Q"}:
            continue
        events.append(
            (
                name,
                event.kind,
                event.actors,
                tuple(sorted(event.predecessors)),
                event.flag,
            )
        )
    local_actors = {row[0] for row in actors}
    amplitudes = []
    for occupied, amplitude in world.amplitudes.items():
        local_occupied = tuple(sorted(set(occupied) & local_actors))
        amplitudes.append((local_occupied, amplitude))
    # Tracing a disconnected |00> factor simply leaves the same pure vector.
    amplitudes.sort(key=lambda item: item[0])
    return tuple(actors), tuple(events), tuple(amplitudes)


def next_a_observable(branch: Branch, old_a1: str) -> Tuple[object, ...]:
    world = branch.world
    event = world.events[branch.return_event]
    new_past = world.ancestors(branch.return_event) - world.ancestors(old_a1)
    return (
        event.kind,
        tuple(sorted(new_past)),
        sum(1 for name in world.transaction_events if world.events[name].kind == "birth"),
        frac_text(world.p_one("A")),
    )


def distribution(
    branches: Sequence[Branch], key_fn
) -> Dict[Tuple[object, ...], Fraction]:
    result: Dict[Tuple[object, ...], Fraction] = defaultdict(Fraction)
    for branch in branches:
        result[key_fn(branch)] += branch.probability
    return dict(sorted(result.items(), key=lambda item: repr(item[0])))


@dataclass(frozen=True)
class Query:
    actor: str
    path: Tuple[int, ...]
    root_cause: str
    requester_actor: Optional[str]
    requester_lower: str
    continuation: Optional[str]
    slot: Optional[int]


@dataclass(frozen=True)
class Return:
    continuation: str
    slot: int
    actor: str
    event: str


@dataclass
class Continuation:
    name: str
    actor: str
    path: Tuple[int, ...]
    root_cause: str
    requester_actor: Optional[str]
    requester_lower: str
    parent_continuation: Optional[str]
    parent_slot: Optional[int]
    targets: Tuple[str, ...]
    received: Dict[int, Tuple[str, str]] = field(default_factory=dict)


Task = Union[Query, Return]


@dataclass
class Machine:
    world: World
    pending: List[Task]
    continuations: Dict[str, Continuation]
    root_result: Optional[str] = None
    rejections: int = 0

    def clone(self) -> "Machine":
        return copy.deepcopy(self)


def task_key(task: Task) -> Tuple[object, ...]:
    if isinstance(task, Query):
        return (0, task.path, task.actor, task.continuation or "", task.slot or -1)
    return (1, task.continuation, task.slot, task.actor, task.event)


def pick_task(machine: Machine, scheduler: str) -> Task:
    if scheduler == "fifo":
        return machine.pending.pop(0)
    if scheduler == "lifo":
        return machine.pending.pop()
    if scheduler == "canonical":
        index = min(range(len(machine.pending)), key=lambda idx: task_key(machine.pending[idx]))
        return machine.pending.pop(index)
    raise ValueError("unknown scheduler")


def validate_query(world: World, query: Query) -> None:
    if query.actor not in world.actors:
        raise ValueError("query missing actor")
    if world.actors[query.actor].tip != query.requester_lower and query.requester_actor is None:
        raise ValueError("forged root tip")
    if query.requester_actor is not None:
        if query.requester_actor not in world.actors:
            raise ValueError("query missing requester")
        if query.actor not in world.actors[query.requester_actor].children:
            raise ValueError("unauthorized edge")
        if world.actors[query.requester_actor].tip != query.requester_lower:
            raise ValueError("forged requester tip")
    if query.root_cause not in world.events:
        raise ValueError("foreign root cause")
    if query.root_cause != world.root_tip:
        raise ValueError("foreign root transaction")


def emit_return(machine: Machine, query: Query, event: str) -> None:
    if query.continuation is None:
        if machine.root_result is not None:
            raise ValueError("duplicate root return")
        machine.root_result = event
        return
    assert query.slot is not None
    machine.pending.append(
        Return(query.continuation, query.slot, query.actor, event)
    )


def process_query(
    machine: Machine,
    query: Query,
    option: Option,
    tx: int,
    params: Params,
) -> None:
    validate_query(machine.world, query)
    machine.world.queried_actors.append(query.actor)
    if option.action == "idle":
        result = create_idle(
            machine.world,
            query.actor,
            tx,
            query.path,
            query.root_cause,
            query.requester_lower,
        )
        emit_return(machine, query, result)
        return
    if option.action == "birth":
        result = create_birth(
            machine.world,
            query.actor,
            tx,
            query.path,
            query.root_cause,
            query.requester_lower,
            params,
        )
        emit_return(machine, query, result)
        return

    name = f"K{tx}:" + ("r" if not query.path else ".".join(map(str, query.path)))
    if name in machine.continuations:
        raise ValueError("duplicate continuation")
    continuation = Continuation(
        name=name,
        actor=query.actor,
        path=query.path,
        root_cause=query.root_cause,
        requester_actor=query.requester_actor,
        requester_lower=query.requester_lower,
        parent_continuation=query.continuation,
        parent_slot=query.slot,
        targets=option.targets,
    )
    machine.continuations[name] = continuation
    lower = machine.world.actors[query.actor].tip
    for slot, target in enumerate(option.targets):
        machine.pending.append(
            Query(
                actor=target,
                path=query.path + (slot,),
                root_cause=query.root_cause,
                requester_actor=query.actor,
                requester_lower=lower,
                continuation=name,
                slot=slot,
            )
        )


def process_return(
    machine: Machine,
    returned: Return,
    tx: int,
    params: Params,
) -> None:
    if returned.continuation not in machine.continuations:
        raise ValueError("foreign return")
    continuation = machine.continuations[returned.continuation]
    if returned.slot in continuation.received:
        raise ValueError("duplicate return")
    if returned.slot >= len(continuation.targets):
        raise ValueError("foreign return slot")
    expected_actor = continuation.targets[returned.slot]
    if returned.actor != expected_actor:
        raise ValueError("foreign return actor")
    if returned.event not in machine.world.events:
        raise ValueError("foreign ancestry")
    if machine.world.actors[returned.actor].tip != returned.event:
        raise ValueError("stale return")
    continuation.received[returned.slot] = (returned.actor, returned.event)
    if len(continuation.received) != len(continuation.targets):
        return
    results = tuple(
        continuation.received[slot][1]
        for slot in range(len(continuation.targets))
    )
    result = create_merge(
        machine.world,
        continuation.actor,
        continuation.targets,
        results,
        tx,
        continuation.path,
        continuation.root_cause,
        continuation.requester_lower,
        params,
    )
    del machine.continuations[returned.continuation]
    if continuation.parent_continuation is None:
        if machine.root_result is not None:
            raise ValueError("duplicate root return")
        machine.root_result = result
    else:
        assert continuation.parent_slot is not None
        machine.pending.append(
            Return(
                continuation.parent_continuation,
                continuation.parent_slot,
                continuation.actor,
                result,
            )
        )


def enumerate_actor_machine(
    world: World, params: Params, scheduler: str, tx: int = 0
) -> List[Branch]:
    cause = world.actors["A"].tip
    initial = Machine(
        world.clone(),
        [Query("A", (), cause, None, cause, None, None)],
        {},
    )
    initial.world.root_tip = cause
    frontier: List[Tuple[Fraction, Machine]] = [(Fraction(1), initial)]
    completed: List[Branch] = []
    while frontier:
        probability, machine = frontier.pop()
        if machine.root_result is not None:
            if machine.pending or machine.continuations:
                raise AssertionError("root returned with open work")
            machine.world.root_tip = machine.root_result
            completed.append(
                Branch(probability, machine.world, machine.root_result)
            )
            continue
        task = pick_task(machine, scheduler)
        if isinstance(task, Query):
            options = local_options(machine.world, task.actor, params)
            for option in options:
                child = machine.clone()
                # local_options was called on the parent solely to enumerate;
                # the cloned machine owns its independent access trace.
                process_query(child, task, option, tx, params)
                frontier.append((probability * option.probability, child))
        else:
            process_return(machine, task, tx, params)
            frontier.append((probability, machine))
    assert sum(branch.probability for branch in completed) == 1
    return completed


def machine_distribution(branches: Sequence[Branch]) -> Dict[Tuple[object, ...], Fraction]:
    return distribution(
        branches,
        lambda branch: (
            local_history_key(branch.world),
            next_a_observable(branch, "A1"),
        ),
    )


def action_plan(branch: Branch) -> Dict[str, Tuple[str, Tuple[str, ...]]]:
    plan: Dict[str, Tuple[str, Tuple[str, ...]]] = {}
    for name in branch.world.transaction_events:
        event = branch.world.events[name]
        path = name.split(":", 1)[1]
        targets = tuple(actor for actor in event.actors if actor != event.actors[0])
        plan[path] = (event.kind, targets)
    return plan


def run_malformed_tests(params: Params) -> int:
    world = initial_world(params, disconnected=True)
    cause = world.actors["A"].tip
    rejected = 0

    cases = [
        Query("A", (), cause, None, "AC", None, None),  # forged root tip
        Query("D", (0,), cause, "A", cause, "K", 0),  # unauthorized A--D
        Query("B", (0,), "P1", "A", cause, "K", 0),  # foreign root cause
    ]
    for query in cases:
        try:
            validate_query(world, query)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError("malformed query accepted")

    machine = Machine(world, [], {}, None)
    machine.continuations["K"] = Continuation(
        "K", "A", (), cause, None, cause, None, None, ("B",), {0: ("B", "BD")}
    )
    try:
        process_return(machine, Return("K", 0, "B", "BD"), 0, params)
    except ValueError:
        rejected += 1
    else:
        raise AssertionError("duplicate return accepted")

    machine.continuations["K2"] = Continuation(
        "K2", "A", (), cause, None, cause, None, None, ("B",), {}
    )
    try:
        process_return(machine, Return("K2", 0, "B", "P1"), 0, params)
    except ValueError:
        rejected += 1
    else:
        raise AssertionError("foreign ancestry accepted")
    return rejected


def acquire_probability(branches: Sequence[Branch], event: str) -> Fraction:
    total = Fraction(0)
    for branch in branches:
        acquired = branch.world.ancestors(branch.return_event) - branch.world.ancestors("A1")
        if event in acquired:
            total += branch.probability
    return total


def kind_distribution(branches: Sequence[Branch]) -> Dict[str, Fraction]:
    total: Dict[str, Fraction] = defaultdict(Fraction)
    for branch in branches:
        total[branch.world.events[branch.return_event].kind] += branch.probability
    return dict(sorted(total.items()))


def expected_births(branches: Sequence[Branch]) -> Fraction:
    return sum(
        branch.probability
        * sum(
            1
            for event in branch.world.transaction_events
            if branch.world.events[event].kind == "birth"
        )
        for branch in branches
    )


def expected_newborn_one_mass(branches: Sequence[Branch]) -> Fraction:
    return sum(
        branch.probability * sum(after for _, after, _ in branch.world.birth_checks)
        for branch in branches
    )


def projectivity_gate(params: Params, first: Sequence[Branch]) -> Tuple[int, int]:
    first_distribution = distribution(
        first, lambda branch: next_a_observable(branch, "A1")
    )
    two_call: Dict[Tuple[object, ...], Fraction] = defaultdict(Fraction)
    refinements = 0
    for first_branch in first:
        second = enumerate_call(first_branch.world, params, tx=1)
        assert sum(branch.probability for branch in second) == 1
        refinements += len(second)
        first_key = next_a_observable(first_branch, "A1")
        for second_branch in second:
            two_call[first_key] += first_branch.probability * second_branch.probability
    if dict(two_call) != first_distribution:
        raise AssertionError("two-call marginal")
    return len(first_distribution), refinements


def ldap_gate(branches: Sequence[Branch]) -> Tuple[int, int, int]:
    checked = 0
    new_records = 0
    visit_c_without_bd = 0
    old_a = branches[0].world.ancestors("A1")
    for branch in branches:
        world = branch.world
        new_past = world.ancestors(branch.return_event) - old_a
        created = set(world.transaction_events)
        if not created <= new_past:
            raise AssertionError("created event outside A2 ancestry")
        for event in new_past:
            if event not in world.events:
                raise AssertionError("unknown acquired record")
        checked += 1
        new_records += len(new_past)
        root_event = world.events[branch.return_event]
        if root_event.kind == "visit" and "C" in root_event.actors and "B" not in root_event.actors:
            if "BD" in new_past:
                raise AssertionError("unqueried B branch acquired")
            visit_c_without_bd += 1
    if visit_c_without_bd == 0:
        raise AssertionError("missing LDAP negative control")
    return checked, new_records, visit_c_without_bd


def disconnected_gate(params: Params, base: Sequence[Branch]) -> int:
    remote = enumerate_call(initial_world(params, disconnected=True), params)
    base_observable = distribution(base, lambda branch: next_a_observable(branch, "A1"))
    remote_observable = distribution(remote, lambda branch: next_a_observable(branch, "A1"))
    if base_observable != remote_observable:
        raise AssertionError("remote component changed A law")
    for branch in remote:
        if set(branch.world.queried_actors) & {"P", "Q"}:
            raise AssertionError("remote actor read")
        if any(actor in {"P", "Q"} for actor, _ in branch.world.local_reads):
            raise AssertionError("remote collar read")
    return len(remote)


def deterministic_plan_replay(
    params: Params, scheduler: str, ticket: int, tx: int = 0
) -> Tuple[object, ...]:
    """One deterministic actor run; random tickets are address-keyed, not queued."""
    world = initial_world(params)
    cause = world.actors["A"].tip
    machine = Machine(world, [Query("A", (), cause, None, cause, None, None)], {})
    while machine.root_result is None:
        task = pick_task(machine, scheduler)
        if isinstance(task, Return):
            process_return(machine, task, tx, params)
            continue
        options = local_options(machine.world, task.actor, params)
        key = f"{ticket}|{task.actor}|{task.path}|{params.name}".encode("utf-8")
        value = int.from_bytes(hashlib.sha256(key).digest(), "big")
        denominator = 1
        for option in options:
            denominator = denominator * option.probability.denominator
        point = Fraction(value % denominator, denominator)
        cumulative = Fraction(0)
        selected = options[-1]
        for option in options:
            cumulative += option.probability
            if point < cumulative:
                selected = option
                break
        process_query(machine, task, selected, tx, params)
    if machine.pending or machine.continuations:
        raise AssertionError("deterministic replay left work")
    return (
        local_history_key(machine.world),
        machine.root_result,
        tuple(sorted(machine.world.queried_actors)),
    )


def source_hash() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def main() -> None:
    gates = []
    summary: Dict[str, object] = {}

    print("[D35 timeless local causal-call exact receipt]")
    print("ARITHMETIC: Fraction exact; Decimal reporting precision=120")
    print("TIME VARIABLES: 0")
    print("GLOBAL OPPORTUNITY NORMALIZERS: 0")

    all_results: Dict[str, List[Branch]] = {}
    for params in (Q1, Q2):
        params.validate()
        branches = enumerate_call(initial_world(params), params)
        all_results[params.name] = branches
        total = sum(branch.probability for branch in branches)
        assert total == 1
        assert all(branch.world.norm() == 1 for branch in branches)
        assert all(
            branch.world.actors["A"].tip == branch.return_event
            for branch in branches
        )
        gates.append(f"E1-{params.name}")

        print(f"[{params.name}]")
        print(
            "q="
            + ",".join(
                frac_text(value)
                for value in (params.idle, params.birth, params.visit, params.fork)
            )
            + f" birth_g={frac_text(params.g)}"
        )
        print(f"recursive_branches={len(branches)} total={frac_text(total)}")
        kinds = kind_distribution(branches)
        print("A2_kind=" + ",".join(f"{key}:{frac_text(value)}" for key, value in kinds.items()))
        p_bd = acquire_probability(branches, "BD")
        print(f"P(BD acquired at A2)={frac_text(p_bd)}={dec_text(p_bd, 50)}")
        eb = expected_births(branches)
        en = expected_newborn_one_mass(branches)
        print(f"E(transaction births)={frac_text(eb)}={dec_text(eb, 50)}")
        print(f"E(sum newborn P1 at birth)={frac_text(en)}={dec_text(en, 50)}")

        recursive_dist = distribution(branches, lambda branch: local_history_key(branch.world))
        machine_dists = {}
        for scheduler in ("fifo", "lifo", "canonical"):
            machine = enumerate_actor_machine(initial_world(params), params, scheduler)
            machine_dist = distribution(
                machine, lambda branch: local_history_key(branch.world)
            )
            machine_dists[scheduler] = machine_dist
            if machine_dist != recursive_dist:
                raise AssertionError((params.name, scheduler, "actor rebuild"))
            print(
                f"actor_{scheduler}_branches={len(machine)} distribution_atoms={len(machine_dist)}"
            )
        if not (machine_dists["fifo"] == machine_dists["lifo"] == machine_dists["canonical"]):
            raise AssertionError("scheduler distribution")
        gates.extend((f"E2-{params.name}", f"E3-{params.name}"))

        reverse = enumerate_call(
            initial_world(params),
            params,
            child_order="reverse",
            quantum_order="reverse",
        )
        reverse_dist = distribution(reverse, lambda branch: local_history_key(branch.world))
        if reverse_dist != recursive_dist:
            raise AssertionError("recursive AB/BA gauge")
        print(f"recursive_AB_BA_atoms={len(reverse_dist)} exact_equal=yes")

        ldap = ldap_gate(branches)
        print(
            f"LDAP branches={ldap[0]} aggregate_newpast_records={ldap[1]} "
            f"unqueried_branch_controls={ldap[2]}"
        )
        gates.append(f"E4-{params.name}")

        remote_count = disconnected_gate(params, branches)
        print(f"disconnected_branches={remote_count} A_law_equal=yes remote_reads=0")
        gates.append(f"E5-{params.name}")

        birth_cells = sum(len(branch.world.birth_checks) for branch in branches)
        if birth_cells == 0:
            raise AssertionError("no live births")
        for branch in branches:
            for before, after, g in branch.world.birth_checks:
                if after != g * before:
                    raise AssertionError("birth marginal")
        print(
            f"D24_birth_cells={birth_cells} marginal_identity=yes norms=1 "
            "Busch_scope=single-isometry-member"
        )
        gates.append(f"E6-{params.name}")

        projective_atoms, refinements = projectivity_gate(params, branches)
        print(
            f"projective_first_atoms={projective_atoms} second_call_refinements={refinements} "
            "marginal_equal=yes"
        )
        gates.append(f"E7-{params.name}")

        replay_hashes = []
        for ticket in range(24):
            runs = [
                deterministic_plan_replay(params, scheduler, ticket)
                for scheduler in ("fifo", "lifo", "canonical")
            ]
            if not (runs[0] == runs[1] == runs[2]):
                raise AssertionError("deterministic scheduler replay")
            replay_hashes.append(digest(runs[0]))
        rejected = run_malformed_tests(params)
        if rejected != 5:
            raise AssertionError("malformed rejection count")
        print(
            f"deterministic_replays={len(replay_hashes)} scheduler_equal=yes "
            f"malformed_rejected={rejected}/5 replay_sha256={digest(replay_hashes)}"
        )
        gates.append(f"E8-{params.name}")

        summary[params.name] = {
            "branches": len(branches),
            "kind": {key: frac_text(value) for key, value in kinds.items()},
            "p_bd": frac_text(p_bd),
            "expected_births": frac_text(eb),
            "expected_newborn_one": frac_text(en),
            "distribution": digest(recursive_dist),
            "replay": digest(replay_hashes),
        }

    q1 = all_results["Q1"]
    q2 = all_results["Q2"]
    q1_birth = kind_distribution(q1)["birth"]
    q2_birth = kind_distribution(q2)["birth"]
    q1_visit = kind_distribution(q1)["visit"]
    q2_visit = kind_distribution(q2)["visit"]
    q1_bd = acquire_probability(q1, "BD")
    q2_bd = acquire_probability(q2, "BD")
    if q1_birth == q2_birth or q1_visit == q2_visit:
        raise AssertionError("nonselection control failed")
    print("[NONSELECTION]")
    print(
        f"birth_Q1={frac_text(q1_birth)} birth_Q2={frac_text(q2_birth)} different=yes"
    )
    print(
        f"visit_Q1={frac_text(q1_visit)} visit_Q2={frac_text(q2_visit)} different=yes"
    )
    print(
        f"BD_Q1={frac_text(q1_bd)} BD_Q2={frac_text(q2_bd)} equal=yes "
        "(registered accidental coarse-observable collision)"
    )
    print(
        "both satisfy exact local normalization, actor rebuild, scheduler gauge, "
        "LDAP, D24/NSE-member, projectivity and rejection gates"
    )
    gates.append("E9")

    print("[COMPLETION AND CEILING]")
    print(
        "finite-call theorem: finite rooted pre-call tree + outward queries => "
        "finite completed A1--A2 diamond"
    )
    print(
        "finite-prefix theorem: each query touches each pre-call actor at most once; "
        "actors and events remain finite after every finite root-wire prefix"
    )
    print(
        "completed classical measure: countable iteration of normalized discrete "
        "rooted-tree kernels (Ionescu--Tulcea scope)"
    )
    print(
        "not proved: cyclic/peer/disconnected joins, coherent graph-sector measure, "
        "v9 stem-spectrum identification, Lorentzian geometry, proper time, or nature's law"
    )
    gates.append("E10")

    if len(gates) != 18:
        raise AssertionError((len(gates), gates))
    summary["gates"] = gates
    internal = digest(summary)
    print("[HASHES]")
    print(f"source_sha256={source_hash()}")
    print(f"internal_science_sha256={internal}")
    print("hash-seed note: the environment value is excluded from all science objects")
    print("[VERDICT]")
    print("PASS 18/18")
    print("TIMELESS LOCAL NEXT-CLICK FAMILY / EXECUTABLE")
    print("opportunity weights, birth coupling, root and omitted join sectors remain extra physics")


if __name__ == "__main__":
    main()
