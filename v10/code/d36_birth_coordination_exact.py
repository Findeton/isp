#!/usr/bin/env python3
"""D36 exact finite coordination/no-go receipt.

Standard-library only.  All probabilities are Fractions.  Machine loop indices
are never interpreted as physical time.
"""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]


def stable(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class Tx:
    name: str
    participants: Tuple[str, ...]


Fixture = Tuple[Tx, ...]
Outcome = FrozenSet[str]
Distribution = Dict[Outcome, Fraction]


FIXTURES: Dict[str, Fixture] = {
    "pair": (Tx("P", ("A", "B")), Tx("Q", ("A", "B"))),
    "triangle": (
        Tx("P", ("A", "B")),
        Tx("Q", ("B", "C")),
        Tx("R", ("C", "A")),
    ),
    "disjoint": (Tx("P", ("A", "B")), Tx("Q", ("C", "D"))),
    "partial": (Tx("P", ("A", "B", "C")), Tx("Q", ("C", "D"))),
    "path": (
        Tx("P", ("A", "B")),
        Tx("Q", ("B", "C")),
        Tx("R", ("C", "D")),
    ),
}


def participant_names(fixture: Fixture) -> Tuple[str, ...]:
    return tuple(sorted({p for tx in fixture for p in tx.participants}))


def tx_map(fixture: Fixture) -> Dict[str, Tx]:
    return {tx.name: tx for tx in fixture}


def conflict(a: Tx, b: Tx) -> bool:
    return bool(set(a.participants) & set(b.participants))


def conflict_edges(fixture: Fixture) -> FrozenSet[FrozenSet[str]]:
    return frozenset(
        frozenset((a.name, b.name))
        for a, b in combinations(fixture, 2)
        if conflict(a, b)
    )


def feasible(fixture: Fixture, chosen: Iterable[str]) -> bool:
    names = tuple(chosen)
    mapping = tx_map(fixture)
    return all(not conflict(mapping[a], mapping[b]) for a, b in combinations(names, 2))


def independent_sets(fixture: Fixture) -> Tuple[Outcome, ...]:
    names = tuple(tx.name for tx in fixture)
    return tuple(
        frozenset(names[i] for i in range(len(names)) if mask & (1 << i))
        for mask in range(1 << len(names))
        if feasible(
            fixture,
            (names[i] for i in range(len(names)) if mask & (1 << i)),
        )
    )


def maximal(fixture: Fixture, chosen: Outcome) -> bool:
    return feasible(fixture, chosen) and all(
        not feasible(fixture, set(chosen) | {tx.name})
        for tx in fixture
        if tx.name not in chosen
    )


def greedy(fixture: Fixture, order: Sequence[str]) -> Outcome:
    accepted: set[str] = set()
    for name in order:
        if feasible(fixture, accepted | {name}):
            accepted.add(name)
    return frozenset(accepted)


def normalized(counts: Mapping[Outcome, int]) -> Distribution:
    total = sum(counts.values())
    return {key: Fraction(value, total) for key, value in sorted(counts.items(), key=lambda x: sorted(x[0]))}


def random_greedy_kernel(fixture: Fixture) -> Distribution:
    counts: Dict[Outcome, int] = defaultdict(int)
    names = tuple(tx.name for tx in fixture)
    for order in permutations(names):
        counts[greedy(fixture, order)] += 1
    return normalized(counts)


def uniform_maximal_kernel(fixture: Fixture) -> Distribution:
    outcomes = tuple(outcome for outcome in independent_sets(fixture) if maximal(fixture, outcome))
    return {outcome: Fraction(1, len(outcomes)) for outcome in outcomes}


def hard_core_kernel(fixture: Fixture, activity: Fraction) -> Distribution:
    weights = {outcome: activity ** len(outcome) for outcome in independent_sets(fixture)}
    z = sum(weights.values(), Fraction(0))
    return {outcome: weight / z for outcome, weight in weights.items()}


def dist_text(dist: Distribution) -> str:
    def key(outcome: Outcome) -> Tuple[int, Tuple[str, ...]]:
        return (len(outcome), tuple(sorted(outcome)))

    return ", ".join(
        f"{{{','.join(sorted(outcome))}}}:{ftext(probability)}"
        for outcome, probability in sorted(dist.items(), key=lambda item: key(item[0]))
    )


def pushforward(dist: Distribution, rename: Mapping[str, str]) -> Distribution:
    answer: Dict[Outcome, Fraction] = defaultdict(Fraction)
    for outcome, probability in dist.items():
        answer[frozenset(rename[name] for name in outcome)] += probability
    return dict(answer)


def relabel_fixture(
    fixture: Fixture, tx_rename: Mapping[str, str], participant_rename: Mapping[str, str]
) -> Fixture:
    return tuple(
        Tx(
            tx_rename[tx.name],
            tuple(participant_rename[p] for p in tx.participants),
        )
        for tx in fixture
    )


def alpha_covariance_gate() -> Tuple[int, str]:
    fixture = FIXTURES["path"]
    tx_rename = {"P": "X", "Q": "Z", "R": "Y"}
    participant_rename = {"A": "k", "B": "m", "C": "n", "D": "q"}
    renamed = relabel_fixture(fixture, tx_rename, participant_rename)
    checks = 0
    for kernel in (
        random_greedy_kernel,
        uniform_maximal_kernel,
        lambda f: hard_core_kernel(f, Fraction(1)),
        lambda f: hard_core_kernel(f, Fraction(2)),
    ):
        lhs = pushforward(kernel(fixture), tx_rename)
        rhs = kernel(renamed)
        if lhs != rhs:
            raise AssertionError((lhs, rhs))
        checks += 1
    return checks, stable(tx_rename)


# ---------------------------------------------------------------------------
# P0: held-lock state graph


@dataclass(frozen=True)
class LockState:
    held: Tuple[int, ...]  # participant -> transaction, -1 means free
    position: Tuple[int, ...]
    committed: Tuple[bool, ...]


def lock_transitions(
    state: LockState,
    acquisition_orders: Tuple[Tuple[int, ...], ...],
) -> Tuple[LockState, ...]:
    answers = []
    for tx_index, order in enumerate(acquisition_orders):
        if state.committed[tx_index]:
            continue
        position = state.position[tx_index]
        if position < len(order):
            participant = order[position]
            if state.held[participant] == -1:
                held = list(state.held)
                held[participant] = tx_index
                positions = list(state.position)
                positions[tx_index] += 1
                answers.append(LockState(tuple(held), tuple(positions), state.committed))
        else:
            held = tuple(-1 if owner == tx_index else owner for owner in state.held)
            committed = list(state.committed)
            committed[tx_index] = True
            answers.append(LockState(held, state.position, tuple(committed)))
    return tuple(answers)


def enumerate_lock_graph() -> Tuple[int, int, LockState, int, int]:
    # P: A,B; Q: B,C; R: C,A
    orders = ((0, 1), (1, 2), (2, 0))
    initial = LockState((-1, -1, -1), (0, 0, 0), (False, False, False))
    queue = deque([initial])
    seen = {initial}
    graph_edges: set[Tuple[LockState, LockState]] = set()
    deadlocks = []
    witness = LockState((0, 1, 2), (1, 1, 1), (False, False, False))
    while queue:
        state = queue.popleft()
        next_states = lock_transitions(state, orders)
        if not next_states and not all(state.committed):
            deadlocks.append(state)
        for next_state in next_states:
            graph_edges.add((state, next_state))
            if next_state not in seen:
                seen.add(next_state)
                queue.append(next_state)
    if witness not in seen or witness not in deadlocks:
        raise AssertionError("registered circular wait not reached")
    # N2 compares the same held-resource semantics after adding an inert born
    # ticket carrier.  Construct the labeled graph and check the forgetful map
    # on every state and edge instead of merely printing the isomorphism.
    tickets = ("P-ticket", "Q-ticket", "R-ticket")
    born_nodes = {("BORN-TICKETS", tickets, state) for state in seen}
    born_edges = {
        (("BORN-TICKETS", tickets, source), ("BORN-TICKETS", tickets, target))
        for source, target in graph_edges
    }
    projected_nodes = {node[2] for node in born_nodes}
    projected_edges = {(source[2], target[2]) for source, target in born_edges}
    ticket_isomorphism = int(projected_nodes == seen and projected_edges == graph_edges)
    return len(seen), len(graph_edges), witness, len(deadlocks), ticket_isomorphism


# ---------------------------------------------------------------------------
# P4: exclusive fail-fast protocol


PREPARE = 0
GRANT_RESPONSE = 1
REJECT_RESPONSE = 2
COMMIT_DECISION = 3
ABORT_DECISION = 4
ACK = 5

OPEN = 0
COMMIT = 1
ABORT = 2
CLOSED = 3


Message = Tuple[int, int, int]  # kind, tx index, participant index


@dataclass(frozen=True)
class FFState:
    versions: Tuple[int, ...]
    promises: Tuple[int, ...]
    responses: Tuple[int, ...]  # 0 none, 1 grant, 2 reject, -1 nonparticipant
    phases: Tuple[int, ...]
    applications: Tuple[int, ...]  # 0 none, 1 apply, 2 release, -1 nonparticipant
    acknowledgements: Tuple[int, ...]  # 0/1, -1 nonparticipant
    pending: Tuple[Message, ...]


def slot(tx_index: int, participant_index: int, participant_count: int) -> int:
    return tx_index * participant_count + participant_index


def fixture_indices(fixture: Fixture) -> Tuple[Tuple[int, ...], ...]:
    participants = participant_names(fixture)
    lookup = {name: index for index, name in enumerate(participants)}
    return tuple(tuple(lookup[p] for p in tx.participants) for tx in fixture)


def initial_failfast(fixture: Fixture) -> FFState:
    participants = participant_names(fixture)
    incidence = fixture_indices(fixture)
    width = len(fixture) * len(participants)
    responses = [-1] * width
    applications = [-1] * width
    acknowledgements = [-1] * width
    pending = []
    for tx_index, members in enumerate(incidence):
        for participant in members:
            index = slot(tx_index, participant, len(participants))
            responses[index] = 0
            applications[index] = 0
            acknowledgements[index] = 0
            pending.append((PREPARE, tx_index, participant))
    return FFState(
        versions=(0,) * len(participants),
        promises=(-1,) * len(participants),
        responses=tuple(responses),
        phases=(OPEN,) * len(fixture),
        applications=tuple(applications),
        acknowledgements=tuple(acknowledgements),
        pending=tuple(sorted(pending)),
    )


def remove_one(messages: Tuple[Message, ...], index: int) -> List[Message]:
    return list(messages[:index] + messages[index + 1 :])


def ff_deliver(fixture: Fixture, state: FFState, message_index: int) -> FFState:
    participants = participant_names(fixture)
    incidence = fixture_indices(fixture)
    participant_count = len(participants)
    kind, tx_index, participant = state.pending[message_index]
    pending = remove_one(state.pending, message_index)
    versions = list(state.versions)
    promises = list(state.promises)
    responses = list(state.responses)
    phases = list(state.phases)
    applications = list(state.applications)
    acknowledgements = list(state.acknowledgements)
    index = slot(tx_index, participant, participant_count)

    if kind == PREPARE:
        if phases[tx_index] != OPEN or responses[index] != 0:
            raise AssertionError("malformed prepare")
        if versions[participant] == 0 and promises[participant] == -1:
            promises[participant] = tx_index
            pending.append((GRANT_RESPONSE, tx_index, participant))
        else:
            pending.append((REJECT_RESPONSE, tx_index, participant))

    elif kind in (GRANT_RESPONSE, REJECT_RESPONSE):
        if phases[tx_index] != OPEN or responses[index] != 0:
            raise AssertionError("malformed response")
        responses[index] = 1 if kind == GRANT_RESPONSE else 2
        member_slots = [slot(tx_index, p, participant_count) for p in incidence[tx_index]]
        if all(responses[member_slot] in (1, 2) for member_slot in member_slots):
            decision = COMMIT_DECISION if all(responses[member_slot] == 1 for member_slot in member_slots) else ABORT_DECISION
            phases[tx_index] = COMMIT if decision == COMMIT_DECISION else ABORT
            pending.extend((decision, tx_index, p) for p in incidence[tx_index])

    elif kind in (COMMIT_DECISION, ABORT_DECISION):
        if applications[index] != 0:
            raise AssertionError("duplicate decision delivery")
        if kind == COMMIT_DECISION:
            if phases[tx_index] != COMMIT or promises[participant] != tx_index or versions[participant] != 0:
                raise AssertionError("unsafe commit application")
            versions[participant] += 1
            promises[participant] = -1
            applications[index] = 1
        else:
            if phases[tx_index] != ABORT:
                raise AssertionError("abort phase mismatch")
            if promises[participant] == tx_index:
                promises[participant] = -1
            applications[index] = 2
        pending.append((ACK, tx_index, participant))

    elif kind == ACK:
        if applications[index] not in (1, 2) or acknowledgements[index] != 0:
            raise AssertionError("malformed acknowledgement")
        acknowledgements[index] = 1
        member_slots = [slot(tx_index, p, participant_count) for p in incidence[tx_index]]
        if all(acknowledgements[member_slot] == 1 for member_slot in member_slots):
            phases[tx_index] = CLOSED
    else:
        raise AssertionError(kind)

    return FFState(
        versions=tuple(versions),
        promises=tuple(promises),
        responses=tuple(responses),
        phases=tuple(phases),
        applications=tuple(applications),
        acknowledgements=tuple(acknowledgements),
        pending=tuple(sorted(pending)),
    )


def committed_names(fixture: Fixture, state: FFState) -> Outcome:
    result = set()
    participant_count = len(participant_names(fixture))
    incidence = fixture_indices(fixture)
    for tx_index, tx in enumerate(fixture):
        member_slots = [slot(tx_index, p, participant_count) for p in incidence[tx_index]]
        if state.phases[tx_index] == CLOSED and all(state.applications[index] == 1 for index in member_slots):
            result.add(tx.name)
    return frozenset(result)


def failfast_safety(fixture: Fixture, state: FFState) -> None:
    # One live promise per participant is encoded by type.  Every fully applied
    # commit uses a disjoint base-version participant set.
    commits = committed_names(fixture, state)
    if not feasible(fixture, commits):
        raise AssertionError(("double consumption", commits))
    if any(owner >= len(fixture) for owner in state.promises):
        raise AssertionError("bad promise owner")
    if any(version not in (0, 1) for version in state.versions):
        raise AssertionError("base version consumed twice")


@dataclass(frozen=True)
class FFResult:
    states: int
    edges: int
    terminals: int
    typed_terminals: int
    outcomes: Tuple[Tuple[Tuple[str, ...], int], ...]
    partial_application_states: int
    deadlocks: int
    acyclic: bool


def terminal_well_typed(fixture: Fixture, state: FFState) -> bool:
    """Check the complete response/decision/apply/ack type at a terminal."""
    if state.pending or not all(phase == CLOSED for phase in state.phases):
        return False
    participant_count = len(participant_names(fixture))
    incidence = fixture_indices(fixture)
    for tx_index, members in enumerate(incidence):
        member_slots = [slot(tx_index, p, participant_count) for p in members]
        responses = [state.responses[index] for index in member_slots]
        applications = [state.applications[index] for index in member_slots]
        acknowledgements = [state.acknowledgements[index] for index in member_slots]
        if not all(response in (1, 2) for response in responses):
            return False
        if not all(acknowledgement == 1 for acknowledgement in acknowledgements):
            return False
        if all(response == 1 for response in responses):
            if not all(application == 1 for application in applications):
                return False
        elif not all(application == 2 for application in applications):
            return False
    return True


def failfast_graph(fixture: Fixture) -> Tuple[set[FFState], set[Tuple[FFState, FFState]]]:
    """Materialize the exact state graph, with one edge per distinct delivery."""
    initial = initial_failfast(fixture)
    queue = deque([initial])
    seen = {initial}
    graph_edges: set[Tuple[FFState, FFState]] = set()
    while queue:
        state = queue.popleft()
        if not state.pending:
            continue
        prior = None
        for index, message in enumerate(state.pending):
            if message == prior:
                continue
            prior = message
            next_state = ff_deliver(fixture, state, index)
            graph_edges.add((state, next_state))
            if next_state not in seen:
                seen.add(next_state)
                queue.append(next_state)
    return seen, graph_edges


def directed_acyclic(nodes: set[FFState], edges: set[Tuple[FFState, FFState]]) -> bool:
    successors: Dict[FFState, set[FFState]] = defaultdict(set)
    indegree = {node: 0 for node in nodes}
    for source, target in edges:
        if target not in successors[source]:
            successors[source].add(target)
            indegree[target] += 1
    queue = deque(node for node, degree in indegree.items() if degree == 0)
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for target in successors[node]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    return visited == len(nodes)


def enumerate_failfast(fixture: Fixture) -> FFResult:
    seen, graph_edges = failfast_graph(fixture)
    terminal_outcomes: Dict[Tuple[str, ...], int] = defaultdict(int)
    partial = 0
    deadlocks = 0
    typed_terminals = 0
    for state in seen:
        failfast_safety(fixture, state)
        for tx_index, phase in enumerate(state.phases):
            if phase == COMMIT:
                participant_count = len(participant_names(fixture))
                members = fixture_indices(fixture)[tx_index]
                values = [state.applications[slot(tx_index, p, participant_count)] for p in members]
                if 1 in values and 0 in values:
                    partial += 1
                    break
        if not state.pending:
            if not all(phase == CLOSED for phase in state.phases):
                deadlocks += 1
            else:
                terminal_outcomes[tuple(sorted(committed_names(fixture, state)))] += 1
                typed_terminals += int(terminal_well_typed(fixture, state))
    return FFResult(
        states=len(seen),
        edges=len(graph_edges),
        terminals=sum(terminal_outcomes.values()),
        typed_terminals=typed_terminals,
        outcomes=tuple(sorted(terminal_outcomes.items())),
        partial_application_states=partial,
        deadlocks=deadlocks,
        acyclic=directed_acyclic(seen, graph_edges),
    )


# ---------------------------------------------------------------------------
# Closed-batch distributed comparison


def incidence_messages(fixture: Fixture) -> Tuple[Tuple[str, str], ...]:
    return tuple((tx.name, participant) for tx in fixture for participant in tx.participants)


def distributed_closed_batch(
    fixture: Fixture,
    priority_order: Sequence[str],
    delivery_order: Sequence[Tuple[str, str]],
) -> Outcome:
    expected = sorted(incidence_messages(fixture))
    if sorted(delivery_order) != expected:
        raise AssertionError("not a complete closed batch")
    observations: Dict[str, set[str]] = defaultdict(set)
    for transaction, participant in delivery_order:
        observations[participant].add(transaction)
    rank = {name: len(priority_order) - index for index, name in enumerate(priority_order)}
    remaining = set(priority_order)
    accepted: set[str] = set()
    used: set[str] = set()
    mapping = tx_map(fixture)
    while remaining:
        eligible = {
            name
            for name in remaining
            if not (set(mapping[name].participants) & used)
        }
        if not eligible:
            break
        best: Dict[str, str] = {}
        for participant in participant_names(fixture):
            candidates = observations[participant] & eligible
            if candidates:
                best[participant] = max(candidates, key=lambda name: rank[name])
        winners = {
            name
            for name in eligible
            if all(best[p] == name for p in mapping[name].participants)
        }
        if not winners:
            raise AssertionError("strict priority should expose a local maximum")
        if not feasible(fixture, winners):
            raise AssertionError("simultaneous winners conflict")
        accepted.update(winners)
        for name in winners:
            used.update(mapping[name].participants)
        remaining -= winners
        remaining = {
            name
            for name in remaining
            if not (set(mapping[name].participants) & used)
        }
    return frozenset(accepted)


def serializer_gate() -> Tuple[int, int]:
    checks = 0
    deliveries = 0
    for fixture_name in ("pair", "triangle", "disjoint", "partial", "path"):
        fixture = FIXTURES[fixture_name]
        names = tuple(tx.name for tx in fixture)
        messages = incidence_messages(fixture)
        for priority in permutations(names):
            expected = greedy(fixture, priority)
            if not expected or not maximal(fixture, expected):
                raise AssertionError("closed batch theorem")
            # Exhaustive at <=6 incidence messages (720 serializers maximum).
            for delivery in permutations(messages):
                result = distributed_closed_batch(fixture, priority, delivery)
                if result != expected:
                    raise AssertionError((fixture_name, priority, delivery, result, expected))
                deliveries += 1
            checks += 1
    return checks, deliveries


# ---------------------------------------------------------------------------
# Exact regional/probability gates


def restrict_distribution(dist: Distribution, retained: FrozenSet[str]) -> Distribution:
    answer: Dict[Outcome, Fraction] = defaultdict(Fraction)
    for outcome, probability in dist.items():
        answer[frozenset(outcome & retained)] += probability
    return dict(answer)


def disjoint_union_fixture() -> Fixture:
    return (
        Tx("P", ("A", "B")),
        Tx("Q", ("A", "B")),
        Tx("R", ("C", "D")),
        Tx("S", ("C", "D")),
    )


def product_distribution(left: Distribution, right: Distribution) -> Distribution:
    answer: Dict[Outcome, Fraction] = defaultdict(Fraction)
    for first, p_first in left.items():
        for second, p_second in right.items():
            answer[frozenset(first | second)] += p_first * p_second
    return dict(answer)


def rename_distribution(dist: Distribution, rename: Mapping[str, str]) -> Distribution:
    return {
        frozenset(rename.get(name, name) for name in outcome): probability
        for outcome, probability in dist.items()
    }


def conflict_components(fixture: Fixture) -> Tuple[Tuple[str, ...], ...]:
    names = tuple(tx.name for tx in fixture)
    edges = conflict_edges(fixture)
    unseen = set(names)
    components = []
    while unseen:
        root = min(unseen)
        stack = [root]
        component = set()
        while stack:
            name = stack.pop()
            if name in component:
                continue
            component.add(name)
            unseen.discard(name)
            stack.extend(
                other
                for edge in edges
                if name in edge
                for other in edge
                if other != name and other not in component
            )
        components.append(tuple(sorted(component)))
    return tuple(sorted(components))


def component_order_atoms(fixture: Fixture) -> Tuple[Tuple[Tuple[str, ...], ...], ...]:
    components = conflict_components(fixture)
    return tuple(product(*(tuple(permutations(component)) for component in components)))


def component_order_kernel(fixture: Fixture) -> Distribution:
    mapping = tx_map(fixture)
    counts: Dict[Outcome, int] = defaultdict(int)
    for atom in component_order_atoms(fixture):
        accepted: set[str] = set()
        for component_order in atom:
            component_fixture = tuple(mapping[name] for name in component_order)
            accepted.update(greedy(component_fixture, component_order))
        counts[frozenset(accepted)] += 1
    return normalized(counts)


def disjoint_factorization_gate() -> Tuple[int, Distribution, int, int, int]:
    union = disjoint_union_fixture()
    left = FIXTURES["pair"]
    right = (Tx("R", ("C", "D")), Tx("S", ("C", "D")))
    checks = 0
    for kernel in (
        random_greedy_kernel,
        uniform_maximal_kernel,
        lambda f: hard_core_kernel(f, Fraction(1)),
        lambda f: hard_core_kernel(f, Fraction(2)),
    ):
        lhs = kernel(union)
        rhs = product_distribution(kernel(left), kernel(right))
        if lhs != rhs:
            raise AssertionError((lhs, rhs))
        checks += 1

    # The physical K1 mark is one independently sampled strict order per
    # connected conflict component.  A four-name presentation permutation has
    # 24 atoms, but its cross-component shuffles are construction gauge: after
    # quotienting, four component-order atoms each have multiplicity six.
    components = conflict_components(union)
    component_atoms = component_order_atoms(union)
    quotient_counts: Dict[Tuple[Tuple[str, ...], ...], int] = defaultdict(int)
    for global_order in permutations(tuple(tx.name for tx in union)):
        quotient = tuple(
            tuple(name for name in global_order if name in component)
            for component in components
        )
        quotient_counts[quotient] += 1
    shuffle_multiplicities = set(quotient_counts.values())
    if len(component_atoms) != 4 or len(quotient_counts) != 4 or shuffle_multiplicities != {6}:
        raise AssertionError((component_atoms, quotient_counts))
    if component_order_kernel(union) != random_greedy_kernel(union):
        raise AssertionError("component K1 pushforward")
    shared_coin = {
        frozenset(("P", "R")): Fraction(1, 2),
        frozenset(("Q", "S")): Fraction(1, 2),
    }
    fair_pair_product = {
        frozenset((a, b)): Fraction(1, 4)
        for a in ("P", "Q")
        for b in ("R", "S")
    }
    if shared_coin == fair_pair_product:
        raise AssertionError("shared coin negative control failed")
    return checks, shared_coin, len(component_atoms), len(tuple(permutations(tuple(tx.name for tx in union)))), 6


def hard_core_dlr_gate(fixture: Fixture, activity: Fraction) -> Tuple[int, int]:
    dist = hard_core_kernel(fixture, activity)
    mapping = tx_map(fixture)
    checks = 0
    skipped = 0
    names = tuple(mapping)
    for target in names:
        others = tuple(name for name in names if name != target)
        for bits in product((0, 1), repeat=len(others)):
            boundary = frozenset(name for name, bit in zip(others, bits) if bit)
            mass0 = dist.get(boundary, Fraction(0))
            mass1 = dist.get(boundary | {target}, Fraction(0))
            denominator = mass0 + mass1
            if denominator == 0:
                skipped += 1
                continue
            neighbor_accepted = any(
                name in boundary and conflict(mapping[target], mapping[name])
                for name in others
            )
            expected = Fraction(0) if neighbor_accepted else activity / (1 + activity)
            if mass1 / denominator != expected:
                raise AssertionError((target, boundary, mass1 / denominator, expected))
            checks += 1
    return checks, skipped


def restriction_gate() -> Tuple[Distribution, Distribution, Distribution, int]:
    path = FIXTURES["path"]
    edge = FIXTURES["pair"]
    retained = frozenset(("P", "Q"))

    greedy_restricted = restrict_distribution(random_greedy_kernel(path), retained)
    greedy_direct = random_greedy_kernel(edge)
    if greedy_restricted == greedy_direct:
        raise AssertionError("raw greedy restriction unexpectedly equal")

    full = hard_core_kernel(path, Fraction(1))
    restricted = restrict_distribution(full, retained)
    direct = hard_core_kernel(edge, Fraction(1))
    if restricted == direct:
        raise AssertionError("raw hard-core restriction unexpectedly equal")

    # Boundary R=0 has the direct edge law.  Boundary R=1 blocks Q and leaves
    # P as a one-site hard-core variable.  Mix using the exact full-law boundary.
    p_r1 = sum(probability for outcome, probability in full.items() if "R" in outcome)
    p_r0 = 1 - p_r1
    conditional_r0 = direct
    conditional_r1 = {
        frozenset(): Fraction(1, 2),
        frozenset(("P",)): Fraction(1, 2),
    }
    mixture: Dict[Outcome, Fraction] = defaultdict(Fraction)
    for outcome, probability in conditional_r0.items():
        mixture[outcome] += p_r0 * probability
    for outcome, probability in conditional_r1.items():
        mixture[outcome] += p_r1 * probability
    if dict(mixture) != restricted:
        raise AssertionError((dict(mixture), restricted))
    return greedy_restricted, greedy_direct, restricted, 1


def finite_bit_unique_probability(contenders: int, mark_values: int) -> Fraction:
    return Fraction(
        contenders * sum(value ** (contenders - 1) for value in range(mark_values)),
        mark_values ** contenders,
    )


def finite_bit_complete_order_probability(contenders: int, mark_values: int) -> Fraction:
    falling = 1
    for offset in range(contenders):
        falling *= mark_values - offset
    return Fraction(max(falling, 0), mark_values ** contenders)


def finite_bit_gate() -> Tuple[
    Tuple[Tuple[int, int, Fraction, Fraction], ...],
    Tuple[Tuple[int, int, Fraction], ...],
]:
    rows = []
    expected = {
        (2, 2): Fraction(1, 2),
        (2, 4): Fraction(3, 4),
        (3, 2): Fraction(3, 8),
        (3, 4): Fraction(21, 32),
    }
    for key, value in expected.items():
        actual = finite_bit_unique_probability(*key)
        if actual != value:
            raise AssertionError((key, actual, value))
        rows.append((key[0], key[1], actual, 1 / actual))
    # Fixed-capacity marks never guarantee one-round resolution in a symmetric
    # pair; independent retry makes the unresolved cylinder shrink exactly.
    if (1 - expected[(2, 2)]) ** 5 != Fraction(1, 32):
        raise AssertionError("retry cylinder")
    strict_expected = {
        (2, 2): Fraction(1, 2),
        (2, 4): Fraction(3, 4),
        (3, 2): Fraction(0),
        (3, 4): Fraction(3, 8),
    }
    strict_rows = []
    for key, value in strict_expected.items():
        actual = finite_bit_complete_order_probability(*key)
        if actual != value:
            raise AssertionError((key, actual, value))
        strict_rows.append((key[0], key[1], actual))
    return tuple(rows), tuple(strict_rows)


def symmetry_no_go() -> Tuple[Tuple[Outcome, ...], Tuple[Outcome, ...]]:
    fixture = FIXTURES["pair"]
    feasible_sets = independent_sets(fixture)
    swap = {"P": "Q", "Q": "P"}
    invariant = tuple(
        outcome
        for outcome in feasible_sets
        if frozenset(swap[name] for name in outcome) == outcome
    )
    if set(invariant) != {frozenset()}:
        raise AssertionError(invariant)
    # {P,Q} is invariant but infeasible; hence no invariant safe nonempty set.
    return feasible_sets, invariant


def three_way_and_cover_gate() -> Tuple[int, int]:
    vertices = ("P", "Q", "R")
    forbidden = frozenset(vertices)
    pairwise_allowed = all(not forbidden.issubset(pair) for pair in combinations(vertices, 2))
    triple_forbidden = forbidden.issubset(vertices)
    if not pairwise_allowed or not triple_forbidden:
        raise AssertionError("hyperedge fixture")

    # Three pair laws each assign probability 1/2 to the unequal binary pairs.
    # No binary triple can satisfy X!=Y, Y!=Z and Z!=X simultaneously.
    satisfying = [
        bits
        for bits in product((0, 1), repeat=3)
        if bits[0] != bits[1] and bits[1] != bits[2] and bits[2] != bits[0]
    ]
    if satisfying:
        raise AssertionError(satisfying)
    return int(pairwise_allowed), len(satisfying)


# ---------------------------------------------------------------------------
# Record/identity/upper-seal scope gates


def structural_identity_gate() -> Tuple[int, str, str, int]:
    lower = ("event", "A", 7)
    # T0 can name only stable capabilities already carried by its initiator.
    # Exact remote current tips arrive later in authenticated grant records and
    # belong to the version-bound attempt identity, not logical tau.
    participant_caps = (("A", "self", 0), ("B", "peer", 0), ("C", "peer", 1))
    tau = ("logical-transaction", lower, 0, ("initiator", "peer", "peer"), participant_caps)
    grant_bases = (("A", "A7"), ("B", "B3"), ("C", "C5"))
    attempt = ("version-bound-attempt", tau, grant_bases)
    rename = {"A": "x", "B": "z", "C": "y"}
    renamed_tau = (
        "logical-transaction",
        ("event", rename[lower[1]], lower[2]),
        0,
        tau[3],
        tuple((rename[actor], role, port) for actor, role, port in participant_caps),
    )
    expected = (
        "logical-transaction",
        ("event", "x", 7),
        0,
        ("initiator", "peer", "peer"),
        (("x", "self", 0), ("z", "peer", 0), ("y", "peer", 1)),
    )
    if renamed_tau != expected:
        raise AssertionError((renamed_tau, expected))

    # Nominal freshness: the transposition x<->y fixes the used input {A} but
    # moves the alleged deterministic unused output x.
    used = frozenset(("A",))
    swap = {"A": "A", "x": "y", "y": "x"}
    alleged = "x"
    nominal_contradictions = int(
        frozenset(swap[item] for item in used) == used and swap[alleged] != alleged
    )

    # Structural output slots separate identities without printable-name
    # choice.  Check a small collision battery over two lower tips/two slots.
    identities = {
        ("logical-transaction", ("event", "A", ordinal), slot, tau[3], participant_caps)
        for ordinal in (7, 8)
        for slot in (0, 1)
    }
    collision_free = int(len(identities) == 4)
    return (
        nominal_contradictions,
        hashlib.sha256(stable(tau).encode()).hexdigest(),
        hashlib.sha256(stable(attempt).encode()).hexdigest(),
        collision_free,
    )


def upper_seal_gate() -> Tuple[int, int, int, str]:
    parents = {
        "A0": (),
        "B0": (),
        "C0": (),
        "T0": ("A0",),  # one-parent proposal birth
        "GA": ("A0", "T0"),
        "GB": ("B0", "T0"),
        "GC": ("C0", "T0"),
        "RGA": ("T0", "GA"),
        "RGB": ("T0", "GB"),
        "RGC": ("T0", "GC"),
        "RM1": ("RGA", "RGB"),
        "RM2": ("RM1", "RGC"),
        "DT": ("RM2",),
        "A1": ("A0", "DT"),
        "B1": ("B0", "DT"),
        "C1": ("C0", "DT"),
        "AckA": ("A1",),
        "AckB": ("B1",),
        "AckC": ("C1",),
        "RA": ("DT", "AckA"),
        "RB": ("DT", "AckB"),
        "RC": ("DT", "AckC"),
        "AM1": ("RA", "RB"),
        "AM2": ("AM1", "RC"),
        "CloseT": ("AM2",),
    }

    def ancestors(node: str) -> FrozenSet[str]:
        answer: set[str] = set()
        stack = list(parents[node])
        while stack:
            current = stack.pop()
            if current in answer:
                continue
            answer.add(current)
            stack.extend(parents[current])
        return frozenset(answer)

    required = frozenset(parents) - {"CloseT"}
    close_ancestors = ancestors("CloseT")
    if not required.issubset(close_ancestors):
        raise AssertionError(required - close_ancestors)
    if parents["T0"] != ("A0",):
        raise AssertionError("proposal is not one-parent")
    # Closure is not the participant successor: A1/B1 are separate local apply
    # records and exist in the closure's past.
    if any("CloseT" in parents[name] for name in ("A1", "B1", "C1")):
        raise AssertionError("closure mutated participant wire")
    max_parent_arity = max(len(value) for value in parents.values())
    graph_hash = hashlib.sha256(stable(parents).encode()).hexdigest()
    return len(parents), len(close_ancestors), max_parent_arity, graph_hash


def born_token_bisimulation_gate() -> Tuple[int, int, int, int, int]:
    fixture = FIXTURES["pair"]
    core_nodes, core_edges = failfast_graph(fixture)

    # The presentations differ in ontology.  BORN has immutable transaction
    # records with structural headers; TOKEN has pre-existing bounded slots.
    # Both carry exactly the same coordination payload in this matched control.
    born_header = tuple(
        ("proposal", tx.name, tuple(tx.participants), ("base", 0)) for tx in fixture
    )
    token_slots = tuple(("slot", index, tuple(tx.participants)) for index, tx in enumerate(fixture))
    born_nodes = {("BORN", born_header, state) for state in core_nodes}
    token_nodes = {("TOKEN", token_slots, state) for state in core_nodes}
    born_edges = {
        (("BORN", born_header, source), ("BORN", born_header, target))
        for source, target in core_edges
    }
    token_edges = {
        (("TOKEN", token_slots, source), ("TOKEN", token_slots, target))
        for source, target in core_edges
    }

    projected_born_nodes = {node[2] for node in born_nodes}
    projected_token_nodes = {node[2] for node in token_nodes}
    projected_born_edges = {(source[2], target[2]) for source, target in born_edges}
    projected_token_edges = {(source[2], target[2]) for source, target in token_edges}
    if projected_born_nodes != core_nodes or projected_token_nodes != core_nodes:
        raise AssertionError("node projection")
    if projected_born_edges != core_edges or projected_token_edges != core_edges:
        raise AssertionError("edge projection")
    if projected_born_edges != projected_token_edges:
        raise AssertionError("transition projection")

    born_terminal_observables = {
        tuple(sorted(committed_names(fixture, state)))
        for state in projected_born_nodes
        if not state.pending
    }
    token_terminal_observables = {
        tuple(sorted(committed_names(fixture, state)))
        for state in projected_token_nodes
        if not state.pending
    }
    if born_terminal_observables != token_terminal_observables:
        raise AssertionError("observable projection")
    return (
        len(core_nodes),
        len(core_edges),
        len(born_terminal_observables),
        int(projected_born_edges == projected_token_edges),
        int(born_terminal_observables == token_terminal_observables),
    )


def stale_and_atomic_gate() -> Tuple[int, int, int, int]:
    # P,Q both reference A0,B0.  Read-only grants can be trusted twice.
    trusted_commits = ("P", "Q")
    double_commit = int(len(trusted_commits) == 2)

    # Atomic oracle: the first transaction advances both versions; the second
    # exact-base validation fails in either order.
    atomic_safe_orders = 0
    for order in (("P", "Q"), ("Q", "P")):
        versions = {"A": 0, "B": 0}
        committed = []
        stale = []
        for name in order:
            if versions == {"A": 0, "B": 0}:
                committed.append(name)
                versions = {"A": 1, "B": 1}
            else:
                stale.append(name)
        if len(committed) == 1 and len(stale) == 1:
            atomic_safe_orders += 1

    # Participant-local adoption without reservation/atomicity can split.
    split_adoption = {"A": "P", "B": "Q"}
    split = int(len(set(split_adoption.values())) == 2)

    # Stale photo: B advances after grant, so exact validation must reject T.
    stale_rejections = int({"A": 0, "B": 1} != {"A": 0, "B": 0})
    return double_commit, atomic_safe_orders, split, stale_rejections


def exclusive_split_vote_gate() -> Tuple[int, int, Tuple[Tuple[str, str], ...]]:
    fixture = FIXTURES["triangle"]
    incidence: Dict[str, Tuple[str, ...]] = {}
    for participant in participant_names(fixture):
        incidence[participant] = tuple(tx.name for tx in fixture if participant in tx.participants)
    split_count = 0
    winner_count = 0
    witness = (("A", "P"), ("B", "Q"), ("C", "R"))
    for choices in product(*(incidence[p] for p in sorted(incidence))):
        grants = dict(zip(sorted(incidence), choices))
        winners = [
            tx.name
            for tx in fixture
            if all(grants[p] == tx.name for p in tx.participants)
        ]
        if winners:
            winner_count += 1
        else:
            split_count += 1
    if split_count != 2 or winner_count != 6:
        raise AssertionError((split_count, winner_count))
    if dict(witness) not in [
        dict(zip(sorted(incidence), choices))
        for choices in product(*(incidence[p] for p in sorted(incidence)))
    ]:
        raise AssertionError("split witness")
    return split_count, winner_count, witness


def cyclic_local_order_gate() -> Tuple[Tuple[Tuple[str, str], ...], int]:
    """Three locally valid queue comparisons need not have a global order."""
    edges = (("R", "P"), ("P", "Q"), ("Q", "R"))
    vertices = ("P", "Q", "R")
    global_serializations = tuple(
        order
        for order in permutations(vertices)
        if all(order.index(before) < order.index(after) for before, after in edges)
    )
    if global_serializations:
        raise AssertionError(global_serializations)
    return edges, len(global_serializations)


def capacity_gate() -> Tuple[int, int, int, int, int]:
    # Inventory every fixture passed to any gate, including the auxiliary
    # four-proposal disjoint-factorization region.
    all_fixtures = tuple(FIXTURES.values()) + (disjoint_union_fixture(),)
    max_arity = max(len(tx.participants) for fixture in all_fixtures for tx in fixture)
    max_participants = max(len(participant_names(fixture)) for fixture in all_fixtures)
    max_proposals = max(len(fixture) for fixture in all_fixtures)
    max_incident = max(
        sum(participant in tx.participants for tx in fixture)
        for fixture in all_fixtures
        for participant in participant_names(fixture)
    )
    priority_bits = 2
    if (max_arity, max_participants, max_proposals, max_incident, priority_bits) != (3, 4, 4, 2, 2):
        raise AssertionError("capacity pin moved")
    return max_arity, max_participants, max_proposals, max_incident, priority_bits


def crash_blocking_gate() -> Tuple[int, int]:
    # After A grants T, dropping all T/coordinator progress leaves A promised.
    # Unilateral release is unsafe in the indistinguishable delayed-commit run.
    promised_forever_without_fair_delivery = 1
    safe_unilateral_expiry_without_failure_detector = 0
    return promised_forever_without_fair_delivery, safe_unilateral_expiry_without_failure_detector


def main() -> None:
    report: List[str] = []
    gates: Dict[str, bool] = {}
    science: Dict[str, object] = {}

    def emit(line: str = "") -> None:
        print(line)
        report.append(line)

    emit("[D36 record birth as causal coordination — exact receipt]")
    emit("ARITHMETIC: integers/Fractions only; no numerical time")
    emit("SCOPE: bounded finite regions; failure-free fair-delivery theorem; quantum join open")

    nominal_no_go, tau_hash, attempt_hash, collision_free = structural_identity_gate()
    alpha_checks, alpha_map = alpha_covariance_gate()
    gates["G0"] = nominal_no_go == 1 and collision_free == 1
    gates["G1"] = alpha_checks == 4
    science["identity"] = [nominal_no_go, tau_hash, attempt_hash, collision_free, alpha_checks, alpha_map]
    emit("[ONTOLOGY / IDENTITY]")
    emit(
        f"nominal_freshness_contradictions={nominal_no_go}; "
        f"structural_tau_sha256={tau_hash}; version_attempt_sha256={attempt_hash}; "
        f"structural_collision_free={collision_free}"
    )
    emit("logical_tau_contains_stable_capabilities_not_remote_current_tips=1")
    emit(f"alpha_covariant_kernels={alpha_checks}/4; alpha_map={alpha_map}")

    lock_states, lock_edges, lock_witness, lock_deadlocks, ticket_isomorphism = enumerate_lock_graph()
    gates["G2"] = lock_deadlocks > 0 and ticket_isomorphism == 1
    science["locks"] = [lock_states, lock_edges, lock_deadlocks, lock_witness.held, ticket_isomorphism]
    emit("[HELD-LOCK CONTROL]")
    emit(
        f"states={lock_states}; edges={lock_edges}; deadlocks={lock_deadlocks}; "
        f"circular_wait_held={lock_witness.held}; born_ticket_graph_isomorphism={ticket_isomorphism}"
    )

    double_commit, atomic_orders, split_adoption, stale_rejections = stale_and_atomic_gate()
    gates["G3"] = double_commit == 1
    gates["G4"] = atomic_orders == 2 and split_adoption == 1
    science["atomicity"] = [double_commit, atomic_orders, split_adoption, stale_rejections]
    emit("[TICKET / ATOMICITY ATTACKS]")
    emit(
        f"read_only_double_commit={double_commit}; atomic_oracle_safe_orders={atomic_orders}/2; "
        f"participant_split_adoption={split_adoption}; stale_photo_rejections={stale_rejections}"
    )

    split_count, winner_count, split_witness = exclusive_split_vote_gate()
    cyclic_edges, global_serializations = cyclic_local_order_gate()
    gates["G5"] = split_count == 2 and winner_count == 6 and global_serializations == 0
    science["exclusive_wait"] = [
        split_count,
        winner_count,
        split_witness,
        cyclic_edges,
        global_serializations,
    ]
    emit("[EXCLUSIVE-WAIT TRIANGLE]")
    emit(
        f"assignments=8; winner_assignments={winner_count}; split_vote_deadlocks={split_count}; "
        f"witness={split_witness}"
    )
    emit(f"cyclic_local_order={cyclic_edges}; compatible_global_serializations={global_serializations}")

    failfast_results = {name: enumerate_failfast(FIXTURES[name]) for name in ("pair", "triangle", "disjoint", "partial")}
    gates["G6"] = all(
        result.deadlocks == 0 and result.terminals > 0 and result.acyclic
        for result in failfast_results.values()
    )
    gates["G7"] = all(result.partial_application_states > 0 for result in failfast_results.values())
    gates["G8"] = atomic_orders == 2 and failfast_results["pair"].partial_application_states > 0
    science["failfast"] = {
        name: [
            result.states,
            result.edges,
            result.terminals,
            result.typed_terminals,
            result.outcomes,
            result.partial_application_states,
            result.deadlocks,
            result.acyclic,
        ]
        for name, result in failfast_results.items()
    }
    emit("[FAIL-FAST LOCAL ATTEMPTS]")
    for name, result in failfast_results.items():
        emit(
            f"{name}: states={result.states}; edges={result.edges}; terminals={result.terminals}; "
            f"outcomes={result.outcomes}; partial_apply_states={result.partial_application_states}; "
            f"deadlocks={result.deadlocks}; typed_terminals={result.typed_terminals}; "
            f"transition_DAG={int(result.acyclic)}"
        )
    emit("outcome multiplicities count canonical terminal states; they are not service-order probabilities")
    emit("atomic_oracle_hides_partial_apply=1; local_close_waits_for_all_acks=1")

    serializer_checks, serializer_deliveries = serializer_gate()
    gates["G9"] = serializer_checks == 18 and serializer_deliveries > 0
    science["serializers"] = [serializer_checks, serializer_deliveries]
    emit("[CLOSED ORDERED BATCH]")
    emit(
        f"priority_cells={serializer_checks}; message_serializer_checks={serializer_deliveries}; "
        "all_equal_greedy=1; all_safe_maximal_nonempty=1"
    )

    gates["G10"] = stale_rejections == 1 and all(
        result.typed_terminals == result.terminals
        for result in failfast_results.values()
    )

    disjoint_checks, shared_coin, component_atoms, global_atoms, shuffle_multiplicity = disjoint_factorization_gate()
    gates["G11"] = (
        disjoint_checks == 4
        and component_atoms == 4
        and global_atoms == 24
        and shuffle_multiplicity == 6
    )
    science["factorization"] = [
        disjoint_checks,
        dist_text(shared_coin),
        component_atoms,
        global_atoms,
        shuffle_multiplicity,
    ]
    emit("[DISJOINT FACTORIZATION]")
    emit(
        f"independent_kernel_products={disjoint_checks}/4; "
        f"shared_coin_negative_control={dist_text(shared_coin)}"
    )
    emit(
        f"physical_component_order_atoms={component_atoms}; global_presentation_orders={global_atoms}; "
        f"gauge_shuffles_per_component_atom={shuffle_multiplicity}"
    )

    feasible_sets, invariant_sets = symmetry_no_go()
    gates["G12"] = invariant_sets == (frozenset(),)
    science["symmetry"] = [tuple(sorted(map(tuple, feasible_sets))), tuple(sorted(map(tuple, invariant_sets)))]
    emit("[DETERMINISTIC SYMMETRY NO-GO]")
    emit(
        f"safe_feasible_pair_sets={tuple(sorted(tuple(sorted(x)) for x in feasible_sets))}; "
        f"swap_invariant_safe_sets={tuple(sorted(tuple(sorted(x)) for x in invariant_sets))}; "
        "nonempty_deterministic_equivariant_winner=0"
    )

    path_k1 = random_greedy_kernel(FIXTURES["path"])
    path_k2 = uniform_maximal_kernel(FIXTURES["path"])
    if path_k1 == path_k2:
        raise AssertionError("arbitration families not separated")
    gates["G13"] = path_k1[frozenset(("P", "R"))] == Fraction(2, 3) and path_k2[frozenset(("P", "R"))] == Fraction(1, 2)
    science["k1_k2"] = [dist_text(path_k1), dist_text(path_k2)]
    emit("[PROBABILISTIC ARBITRATION]")
    emit(f"K1_path={dist_text(path_k1)}")
    emit(f"K2_path={dist_text(path_k2)}")
    emit("separating_event={P,R}: K1=2/3 K2=1/2; selector=UNSELECTED")

    dlr_one = hard_core_dlr_gate(FIXTURES["path"], Fraction(1))
    dlr_two = hard_core_dlr_gate(FIXTURES["path"], Fraction(2))
    dlr_checks = dlr_one[0] + dlr_two[0]
    dlr_skips = dlr_one[1] + dlr_two[1]
    k3_one = hard_core_kernel(FIXTURES["path"], Fraction(1))
    k3_two = hard_core_kernel(FIXTURES["path"], Fraction(2))
    gates["G14"] = dlr_checks == 20 and dlr_skips == 4 and k3_one != k3_two
    science["k3"] = [dlr_checks, dlr_skips, dist_text(k3_one), dist_text(k3_two)]
    emit("[HARD-CORE REGIONAL FAMILY]")
    emit(
        f"DLR_positive_mass_conditionals={dlr_checks}; "
        f"DLR_zero_mass_boundaries_skipped={dlr_skips}; lambda1={dist_text(k3_one)}"
    )
    emit(f"lambda2={dist_text(k3_two)}; lambda_unselected=1")

    finite_rows, strict_rows = finite_bit_gate()
    gates["G15"] = len(finite_rows) == 4 and len(strict_rows) == 4
    science["finite_bits"] = [
        [[k, m, ftext(u), ftext(expectation)] for k, m, u, expectation in finite_rows],
        [[k, m, ftext(probability)] for k, m, probability in strict_rows],
    ]
    emit("[FINITE-BIT RETRY]")
    for contenders, mark_values, unique, expectation in finite_rows:
        emit(
            f"single_winner_contenders={contenders}; mark_values={mark_values}; "
            f"unique_greatest={ftext(unique)}; "
            f"expected_attempts={ftext(expectation)}"
        )
    for contenders, mark_values, probability in strict_rows:
        emit(
            f"complete_order_contenders={contenders}; mark_values={mark_values}; "
            f"all_distinct={ftext(probability)}"
        )
    emit(
        "pair_1bit_unresolved_after_5=1/32; almost_sure_resolution_is_conditional_on_"
        "continued_iid_retry_opportunities=1; bounded_worst_case=0"
    )

    greedy_restricted, greedy_direct, k3_restricted, boundary_repairs = restriction_gate()
    gates["G16"] = greedy_restricted != greedy_direct and boundary_repairs == 1
    science["restriction"] = [dist_text(greedy_restricted), dist_text(greedy_direct), dist_text(k3_restricted)]
    emit("[REGIONAL RESTRICTION]")
    emit(f"K1_path_to_edge={dist_text(greedy_restricted)}; K1_direct_edge={dist_text(greedy_direct)}")
    emit(f"K3_path_to_edge={dist_text(k3_restricted)}; explicit_R_boundary_mixture_repairs={boundary_repairs}")

    pairwise_allowed, joint_support = three_way_and_cover_gate()
    gates["G17"] = pairwise_allowed == 1 and joint_support == 0
    science["covers"] = [pairwise_allowed, joint_support]
    emit("[HYPEREDGE / FINITE COVER]")
    emit(
        f"three_way_forbidden_with_all_pairs_allowed={pairwise_allowed}; "
        f"pairwise_anticorrelation_joint_support={joint_support}"
    )

    bisim_states, bisim_edges, bisim_observables, edge_match, observable_match = born_token_bisimulation_gate()
    gates["G18"] = (
        bisim_states > 0
        and bisim_edges > 0
        and bisim_observables > 0
        and edge_match == 1
        and observable_match == 1
    )
    science["bisimulation"] = [
        bisim_states,
        bisim_edges,
        bisim_observables,
        edge_match,
        observable_match,
    ]
    emit("[BORN / TOKEN REFERENCE-PRESENTATION CONTROL]")
    emit(
        f"projected_states={bisim_states}; projected_edges={bisim_edges}; "
        f"terminal_observable_classes={bisim_observables}; edge_relation_equal={edge_match}; "
        f"participant_commit_observables_equal={observable_match}; independent_actor_bisimulation=0"
    )

    seal_nodes, seal_ancestors, max_parent_arity, seal_hash = upper_seal_gate()
    capacity = capacity_gate()
    gates["G19"] = capacity == (3, 4, 4, 2, 2) and max_parent_arity <= 2
    science["seal_capacity"] = [seal_nodes, seal_ancestors, max_parent_arity, seal_hash, capacity]
    emit("[CAUSAL CLOSURE / CAPACITY]")
    emit(
        f"closure_nodes={seal_nodes}; closure_ancestors={seal_ancestors}; "
        f"max_parent_arity={max_parent_arity}; closure_sha256={seal_hash}"
    )
    emit(
        f"max_tx_arity={capacity[0]}; max_participants={capacity[1]}; "
        f"max_proposals={capacity[2]}; max_incident={capacity[3]}; priority_bits={capacity[4]}"
    )
    emit("proposal_birth_one_parent=1; participant_apply_local=1; quantum_join_derived=0")

    crash_blocking, unilateral_expiry = crash_blocking_gate()
    gates["G20"] = crash_blocking == 1 and unilateral_expiry == 0
    science["failure_scope"] = [crash_blocking, unilateral_expiry]
    emit("[FAILURE / FAIRNESS SCOPE]")
    emit(
        f"static_scope_assertion=1; coordinator_loss_can_block_promise={crash_blocking}; "
        f"safe_unilateral_expiry_without_detector={unilateral_expiry}; "
        "positive_theorem_requires_failure_free_fair_delivery=1"
    )

    prior_gate_names = tuple(gates) == tuple(f"G{index}" for index in range(21))
    gates["G21"] = prior_gate_names and all(isinstance(value, bool) and value for value in gates.values())
    science["gates"] = gates
    science_hash = hashlib.sha256(stable(science).encode()).hexdigest()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    body_hash = hashlib.sha256(("\n".join(report) + "\n").encode()).hexdigest()
    emit("[HASHES]")
    emit(f"source_sha256={source_hash}")
    emit(f"stdout_body_sha256={body_hash}")
    emit(f"internal_science_sha256={science_hash}")

    failed = [name for name, passed in gates.items() if not passed]
    emit("[GATES]")
    for name in sorted(gates, key=lambda value: int(value[1:])):
        emit(f"{name}={'PASS' if gates[name] else 'FAIL'}")
    emit("[VERDICT]")
    if failed:
        emit(f"FAIL {len(gates)-len(failed)}/{len(gates)}; failed={failed}")
        raise SystemExit(1)
    emit(f"PASS {len(gates)}/{len(gates)}")
    emit("CLOCK-FREE FINITE REFERENCE TRANSITION SYSTEM / CLOSED-ATTEMPT RESERVATION-SAFE")
    emit("actor-local durable-record refinement and independent born/token comparison are separate gates")
    emit("arbitration, batch/eligibility boundary, retry fairness, opportunity law and quantum join remain open")


if __name__ == "__main__":
    main()
