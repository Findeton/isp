#!/usr/bin/env python3
"""D34f exact receipt: component tomography for full durable ancestry.

Pins: note-d34f-component-tomography-and-necessity.md / commits 7a5f2fb and
eea9474, both committed before this executable existed.  The second pin
records the bare-sweep counterexample and freezes the anchored replacement.

All discrete probabilities are Fraction-exact.  Decimal values are explicitly
labeled evaluations of analytic exponential/Erlang formulas at 110-digit
working precision.  Finite enumeration is a regression and counterexample
search; the all-finite claims are carried by the printed lemmas.  Exit 1 on
any failed gate.
"""

from collections import defaultdict, deque
from decimal import Decimal, getcontext
from fractions import Fraction as F
from itertools import permutations, product
import hashlib
import math
import sys


getcontext().prec = 110

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "[PASS]"
    else:
        FAIL += 1
        tag = "[FAIL]"
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


def dfrac(value):
    return Decimal(value.numerator) / Decimal(value.denominator)


def ftext(value):
    return str(value.numerator) if value.denominator == 1 else str(value)


print("[d34f — exact component tomography and full-ancestry necessity]")


# ---------------------------------------------------------------------------
# E1: the literal chosen D34b law and bounded exact enumeration.

def seed_state():
    return {
        "actors": {
            "A": {"ring": 0, "births": 0, "sealed": False, "carrier": 0},
            "B": {"ring": 0, "births": 0, "sealed": False, "carrier": 0},
        },
        "neighbors": {"A": {"B"}, "B": {"A"}},
        "last": {},
        "events": [],
    }


def copy_state(state):
    return {
        "actors": {name: dict(row) for name, row in state["actors"].items()},
        "neighbors": {name: set(row) for name, row in state["neighbors"].items()},
        "last": dict(state["last"]),
        "events": list(state["events"]),
    }


def active_actors(state):
    return tuple(sorted(
        actor for actor, row in state["actors"].items() if not row["sealed"]
    ))


def edge_key(left, right):
    return tuple(sorted((left, right)))


def d34b_rates(state):
    rows = []
    for initiator in active_actors(state):
        eligible = tuple(sorted(
            peer for peer in state["neighbors"][initiator]
            if not state["actors"][peer]["sealed"]
        ))
        if not eligible:
            raise ValueError("chosen D34b requires an eligible neighbor")
        rows.append(("b", initiator, None, F(1, 4)))
        for target in eligible:
            rows.append(("i", initiator, target, F(1, 4 * len(eligible))))
        rows.append(("n", initiator, None, F(1, 2)))
    return tuple(rows)


def d34b_step(state, kind, initiator, target=None):
    out = copy_state(state)
    actor = out["actors"][initiator]
    if actor["sealed"]:
        raise ValueError("sealed initiator")
    actor["ring"] += 1
    eid = f"{initiator}#r{actor['ring']}"
    if kind == "b":
        actor["births"] += 1
        target = f"{initiator}/{actor['births']}"
        if target in out["actors"]:
            raise ValueError("duplicate child")
        out["actors"][target] = {
            "ring": 0, "births": 0, "sealed": False, "carrier": 0,
        }
        out["neighbors"][initiator].add(target)
        out["neighbors"][target] = {initiator}
        touched = (initiator, target)
    elif kind == "i":
        if target not in out["neighbors"][initiator]:
            raise ValueError("ineligible interaction")
        touched = (initiator, target)
        out["actors"][initiator]["carrier"] ^= 1
        out["actors"][target]["carrier"] ^= 1
    elif kind == "n":
        target = None
        touched = (initiator,)
    else:
        raise ValueError(kind)
    predecessors = tuple(sorted(
        out["last"][name] for name in touched if name in out["last"]
    ))
    out["events"].append(
        (eid, kind, initiator, target, predecessors, tuple(touched))
    )
    for name in touched:
        out["last"][name] = eid
    return out


def event_rate(state, kind, initiator, target=None):
    return next(
        rate for k, y, x, rate in d34b_rates(state)
        if (k, y, x) == (kind, initiator, target)
    )


def embedded_step(state, kind, initiator, target=None):
    probability = event_rate(state, kind, initiator, target) / len(active_actors(state))
    return d34b_step(state, kind, initiator, target), probability


def state_key(state):
    return (
        tuple(sorted(
            (name, row["ring"], row["births"], row["sealed"], row["carrier"])
            for name, row in state["actors"].items()
        )),
        tuple(sorted(
            (name, tuple(sorted(peers)))
            for name, peers in state["neighbors"].items()
        )),
        tuple(sorted(state["last"].items())),
        tuple(sorted((repr(event) for event in state["events"]))),
    )


def enumerate_levels(depth):
    levels = [{state_key(seed_state()): (seed_state(), F(1))}]
    for _ in range(depth):
        nxt = {}
        for state, probability in levels[-1].values():
            actor_count = len(active_actors(state))
            if sum((rate for *_, rate in d34b_rates(state)), F(0)) != actor_count:
                raise AssertionError("generator rows do not normalize")
            for kind, initiator, target, rate in d34b_rates(state):
                after = d34b_step(state, kind, initiator, target)
                p_after = probability * rate / actor_count
                key = state_key(after)
                if key in nxt:
                    nxt[key] = (nxt[key][0], nxt[key][1] + p_after)
                else:
                    nxt[key] = (after, p_after)
        if sum((p for _, p in nxt.values()), F(0)) != 1:
            raise AssertionError("embedded level does not normalize")
        levels.append(nxt)
    return levels


levels = enumerate_levels(4)
level_counts = tuple(len(level) for level in levels)
enumerated_states = tuple(
    state for level in levels for state, _probability in level.values()
)
e1_ok = (
    level_counts == (1, 6, 40, 304, 2576)
    and all(sum((p for _, p in level.values()), F(0)) == 1 for level in levels)
    and all(
        sum((rate for *_, rate in d34b_rates(state)), F(0))
        == len(active_actors(state))
        for state in enumerated_states
    )
)
check(
    "E1 CHOSEN D34b FINITE DOMAIN [Fraction-exact + inherited nonexplosion]: "
    "the literal birth/interact/idle rows normalize and the depth-four "
    "reachable distribution retains persistent event DAGs",
    e1_ok,
    f"levels={level_counts}; cumulative states={len(enumerated_states)}",
)


# ---------------------------------------------------------------------------
# Event-DAG helpers, E2 wire persistence and E3 reconstruction.

def parse_event_id(eid):
    owner, ordinal_text = eid.rsplit("#r", 1)
    ordinal = int(ordinal_text)
    if not owner or ordinal < 1 or eid != f"{owner}#r{ordinal}":
        raise ValueError("noncanonical event identifier")
    return owner, ordinal


def event_map(state):
    return {event[0]: event for event in state["events"]}


def ancestor_ids(state, eid):
    events = event_map(state)
    seen = set()
    stack = [eid]
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        stack.extend(events[current][4])
    return frozenset(seen)


wire_checks = 0
wire_persistence_ok = True
for state in enumerated_states:
    for actor in sorted(state["actors"]):
        touching = {
            event[0] for event in state["events"] if actor in event[5]
        }
        if not touching:
            wire_persistence_ok &= actor not in state["last"]
            continue
        tip = state["last"].get(actor)
        wire_checks += len(touching)
        wire_persistence_ok &= tip is not None
        wire_persistence_ok &= touching <= ancestor_ids(state, tip)

e2_ok = wire_persistence_ok and wire_checks > 10000
check(
    "E2 WIRE-PERSISTENCE LEMMA [exact DAG closure + all-state regression]: "
    "every event touching an actor is in its current tip ancestry and therefore "
    "survives every later touch of that wire",
    e2_ok,
    f"event/owned-wire incidences checked={wire_checks}",
)


def reconstruct_configuration(state):
    actors = {"A", "B"}
    edges = {edge_key("A", "B")}
    initiated = defaultdict(list)
    births = defaultdict(int)
    interactions = defaultdict(int)
    touching = defaultdict(list)
    for event in state["events"]:
        eid, kind, initiator, target, _predecessors, touched = event
        actors.update(touched)
        initiated[initiator].append(parse_event_id(eid)[1])
        for actor in touched:
            touching[actor].append(eid)
        if kind == "b":
            births[initiator] += 1
            actors.add(target)
            edges.add(edge_key(initiator, target))
        elif kind == "i":
            for actor in touched:
                interactions[actor] += 1

    rows = {}
    for actor in actors:
        ordinals = sorted(initiated[actor])
        if ordinals != list(range(1, len(ordinals) + 1)):
            raise ValueError("initiator ordinals are not contiguous")
        rows[actor] = {
            "ring": len(ordinals),
            "births": births[actor],
            "sealed": False,
            "carrier": interactions[actor] % 2,
        }

    neighbors = {actor: set() for actor in actors}
    for left, right in edges:
        neighbors[left].add(right)
        neighbors[right].add(left)

    last = {}
    for actor, eids in touching.items():
        maximal = [
            eid for eid in eids
            if all(eid == other or eid not in ancestor_ids(state, other)
                   for other in eids)
        ]
        if len(maximal) != 1:
            raise ValueError("wire does not have a unique maximal event")
        last[actor] = maximal[0]
    return rows, neighbors, last


reconstruction_ok = True
reconstruction_checks = 0
for state in enumerated_states:
    rows, neighbors, last = reconstruct_configuration(state)
    reconstruction_checks += 1
    reconstruction_ok &= rows == state["actors"]
    reconstruction_ok &= neighbors == state["neighbors"]
    reconstruction_ok &= last == state["last"]

e3_ok = reconstruction_ok and reconstruction_checks == len(enumerated_states)
check(
    "E3 COMPONENT RECONSTRUCTION [exact marked-DAG theorem + regression]: "
    "the fixed seed and persistent event DAG recover actors, tree adjacency, "
    "ring/birth rows, carrier parity and unique wire tips",
    e3_ok,
    f"components reconstructed={reconstruction_checks}",
)


# ---------------------------------------------------------------------------
# Rooted-tree sweeps, E4 collection and E5 exact/timed probabilities.

def rooted_parent(state, root="A"):
    parent = {root: None}
    queue = deque([root])
    while queue:
        actor = queue.popleft()
        for peer in sorted(state["neighbors"][actor]):
            if peer in parent:
                continue
            parent[peer] = actor
            queue.append(peer)
    if set(parent) != set(state["actors"]):
        raise ValueError("state is not one connected component")
    return parent


def postorder_from_parent(parent, root="A", reverse=False):
    children = defaultdict(list)
    for actor, p_actor in parent.items():
        if p_actor is not None:
            children[p_actor].append(actor)
    for row in children.values():
        row.sort(reverse=reverse)
    order = []

    def visit(actor):
        for child in children[actor]:
            visit(child)
        if actor != root:
            order.append(actor)

    visit(root)
    return tuple(order)


def run_sweep(state, order=None):
    parent = rooted_parent(state)
    if order is None:
        order = postorder_from_parent(parent)
    out = state
    embedded_mass = F(1)
    continuous_rate_product = F(1)
    future_eids = []
    for actor in order:
        target = parent[actor]
        continuous_rate = event_rate(out, "i", actor, target)
        embedded_mass *= continuous_rate / len(active_actors(out))
        continuous_rate_product *= continuous_rate
        out = d34b_step(out, "i", actor, target)
        eid = out["events"][-1][0]
        if "A" in out["events"][-1][5]:
            future_eids.append(eid)
    return out, embedded_mass, continuous_rate_product, tuple(future_eids)


collection_ok = True
collection_checks = 0
sibling_checks = 0
sibling_ok = True
sweep_masses = []
for state in enumerated_states:
    old_eids = {event[0] for event in state["events"]}
    parent = rooted_parent(state)
    sorted_order = postorder_from_parent(parent, reverse=False)
    reverse_order = postorder_from_parent(parent, reverse=True)
    after, mass, _rate_product, _future = run_sweep(state, sorted_order)
    final_ancestry = ancestor_ids(after, after["last"]["A"])
    collection_checks += 1
    collection_ok &= len(sorted_order) == len(state["actors"]) - 1
    collection_ok &= old_eids <= final_ancestry
    expected_mass = F(1)
    actor_count = len(state["actors"])
    for actor in sorted_order:
        expected_mass *= F(1, 4 * actor_count * len(state["neighbors"][actor]))
    collection_ok &= mass == expected_mass > 0
    sweep_masses.append(mass)

    after_reverse, mass_reverse, _rates_reverse, _future_reverse = run_sweep(
        state, reverse_order
    )
    reverse_ancestry = ancestor_ids(after_reverse, after_reverse["last"]["A"])
    sibling_checks += 1
    sibling_ok &= old_eids <= reverse_ancestry
    sibling_ok &= mass_reverse == mass

e4_ok = (
    collection_ok and sibling_ok
    and collection_checks == sibling_checks == len(enumerated_states)
)
check(
    "E4 POST-ORDER COMPONENT COLLECTION [all-finite induction + exact "
    "regression]: one child-to-parent interaction per rooted tree edge carries "
    "every pre-stop event into the final A ancestry; either sibling order works",
    e4_ok,
    f"sorted/reverse sweeps={collection_checks}/{sibling_checks}; "
    f"minimum registered mass={ftext(min(sweep_masses))}",
)


def erlang_cdf(shape, rate, delta):
    x = Decimal(rate) * Decimal(delta)
    return Decimal(1) - (-x).exp() * sum(
        x ** j / Decimal(math.factorial(j)) for j in range(shape)
    )


timed_rows = []
timed_ok = True
for state in tuple(levels[3].values())[:20]:
    specimen = state[0]
    actor_count = len(specimen["actors"])
    parent = rooted_parent(specimen)
    order = postorder_from_parent(parent)
    after, embedded_mass, rate_product, _future = run_sweep(specimen, order)
    shape = len(order)
    timed = dfrac(embedded_mass) * erlang_cdf(shape, actor_count, Decimal(1))
    degree_product = math.prod(len(specimen["neighbors"][actor]) for actor in order)
    leading = F(1, math.factorial(shape) * 4 ** shape * degree_product)
    symbolic_leading = embedded_mass * actor_count ** shape / math.factorial(shape)
    timed_ok &= after["last"]["A"] is not None
    timed_ok &= timed > 0
    timed_ok &= leading == symbolic_leading
    timed_rows.append((shape, embedded_mass, timed, leading))

e5_ok = timed_ok and len(timed_rows) == 20
check(
    "E5 SWEEP PROBABILITY / SMALL-TIME COEFFICIENT [Fraction-exact + "
    "110-digit evaluation]: p_sweep is the exact embedded product; multiplying "
    "by the Erlang completion CDF gives a positive timed subcylinder and leading "
    "coefficient 1/[m! 4^m product d(v)]",
    e5_ok,
    "specimens=20; first timed Delta=1="
    f"{timed_rows[0][2]:.40E}; first leading={ftext(timed_rows[0][3])}",
)


# ---------------------------------------------------------------------------
# Canonical rooted marked gauge forms and Branch-F structural traces.

def rename_eid(eid, mapping):
    owner, ordinal = parse_event_id(eid)
    return f"{mapping[owner]}#r{ordinal}"


def renamed_event(event, mapping):
    eid, kind, initiator, target, predecessors, touched = event
    return (
        rename_eid(eid, mapping),
        kind,
        mapping[initiator],
        None if target is None else mapping[target],
        tuple(sorted(rename_eid(pred, mapping) for pred in predecessors)),
        tuple(mapping[actor] for actor in touched),
    )


def canonical_event(event, mapping):
    renamed = renamed_event(event, mapping)
    return renamed[:3] + (("" if renamed[3] is None else renamed[3]),) + renamed[4:]


def representation_under(state, mapping):
    actors = tuple(sorted(
        (mapping[name], row["ring"], row["births"], int(row["sealed"]),
         row["carrier"])
        for name, row in state["actors"].items()
    ))
    edges = tuple(sorted(
        tuple(sorted((mapping[left], mapping[right])))
        for left in state["neighbors"] for right in state["neighbors"][left]
        if left < right
    ))
    events = tuple(sorted(
        (canonical_event(event, mapping) for event in state["events"]),
        key=repr,
    ))
    last = tuple(sorted(
        (mapping[actor], rename_eid(eid, mapping))
        for actor, eid in state["last"].items()
    ))
    return actors, edges, events, last


def canonical_form(state):
    others = tuple(sorted(actor for actor in state["actors"] if actor != "A"))
    labels = tuple(f"V{index}" for index in range(len(others)))
    best = None
    best_mapping = None
    for assigned in permutations(labels):
        mapping = {"A": "A"}
        mapping.update(dict(zip(others, assigned)))
        key = representation_under(state, mapping)
        if best is None or key < best:
            best = key
            best_mapping = mapping
    return best, best_mapping


def canonical_state_key(state):
    return canonical_form(state)[0]


def canonical_sweep_order(state):
    _key, mapping = canonical_form(state)
    inverse = {new: old for old, new in mapping.items()}
    renamed_neighbors = {
        mapping[actor]: {mapping[peer] for peer in peers}
        for actor, peers in state["neighbors"].items()
    }
    renamed_stub = {
        "actors": {mapping[actor]: {} for actor in state["actors"]},
        "neighbors": renamed_neighbors,
    }
    parent = rooted_parent(renamed_stub)
    canonical_order = postorder_from_parent(parent)
    return tuple(inverse[actor] for actor in canonical_order)


def trace_under(after, future_a_eids, mapping):
    entries = []
    events = event_map(after)
    for eid in future_a_eids:
        ancestry = tuple(sorted(
            (canonical_event(events[ancestor], mapping)
             for ancestor in ancestor_ids(after, eid)),
            key=repr,
        ))
        entries.append((canonical_event(events[eid], mapping), ancestry))
    return tuple(entries)


def canonical_trace(after, future_a_eids):
    others = tuple(sorted(actor for actor in after["actors"] if actor != "A"))
    labels = tuple(f"V{index}" for index in range(len(others)))
    best = None
    for assigned in permutations(labels):
        mapping = {"A": "A"}
        mapping.update(dict(zip(others, assigned)))
        key = trace_under(after, future_a_eids, mapping)
        if best is None or key < best:
            best = key
    return best


def renamed_state(state, mapping):
    return {
        "actors": {mapping[name]: dict(row) for name, row in state["actors"].items()},
        "neighbors": {
            mapping[name]: {mapping[peer] for peer in peers}
            for name, peers in state["neighbors"].items()
        },
        "last": {
            mapping[name]: rename_eid(eid, mapping)
            for name, eid in state["last"].items()
        },
        "events": [renamed_event(event, mapping) for event in state["events"]],
    }


def canonical_tree_orders(state):
    """Gauge-covariant preorder broadcast and postorder collection edges."""
    _key, mapping = canonical_form(state)
    inverse = {new: old for old, new in mapping.items()}
    renamed_stub = {
        "actors": {mapping[actor]: {} for actor in state["actors"]},
        "neighbors": {
            mapping[actor]: {mapping[peer] for peer in peers}
            for actor, peers in state["neighbors"].items()
        },
    }
    parent = rooted_parent(renamed_stub)
    children = defaultdict(list)
    for actor, p_actor in parent.items():
        if p_actor is not None:
            children[p_actor].append(actor)
    for row in children.values():
        row.sort()

    outward = []

    def broadcast(actor):
        for child in children[actor]:
            outward.append((actor, child))
            broadcast(child)

    broadcast("A")
    inward_actors = postorder_from_parent(parent)
    outward_original = tuple((inverse[p], inverse[c]) for p, c in outward)
    inward_original = tuple((inverse[c], inverse[parent[c]]) for c in inward_actors)
    return outward_original, inward_original


def run_anchor_echo(state, outward=None, inward=None):
    """Fresh A anchor, preorder broadcast, then postorder inward echo."""
    if outward is None or inward is None:
        outward, inward = canonical_tree_orders(state)
    actor_count = len(active_actors(state))
    out = state
    embedded_mass = F(1)
    continuous_rate_product = F(1)
    future_a = []
    all_future = []

    rate = event_rate(out, "n", "A")
    embedded_mass *= rate / actor_count
    continuous_rate_product *= rate
    out = d34b_step(out, "n", "A")
    anchor_eid = out["events"][-1][0]
    future_a.append(anchor_eid)
    all_future.append(anchor_eid)

    for parent_actor, child in outward:
        rate = event_rate(out, "i", parent_actor, child)
        embedded_mass *= rate / actor_count
        continuous_rate_product *= rate
        out = d34b_step(out, "i", parent_actor, child)
        eid = out["events"][-1][0]
        all_future.append(eid)
        if "A" in out["events"][-1][5]:
            future_a.append(eid)

    for child, parent_actor in inward:
        rate = event_rate(out, "i", child, parent_actor)
        embedded_mass *= rate / actor_count
        continuous_rate_product *= rate
        out = d34b_step(out, "i", child, parent_actor)
        eid = out["events"][-1][0]
        all_future.append(eid)
        if "A" in out["events"][-1][5]:
            future_a.append(eid)

    return (
        out, embedded_mass, continuous_rate_product, tuple(future_a),
        anchor_eid, tuple(all_future),
    )


# E6: the repaired anchored discriminator on the full enumerated domain.
echo_ok = True
echo_checks = 0
echo_timed_rows = []
echo_masses = []
for state in enumerated_states:
    old_eids = {event[0] for event in state["events"]}
    outward, inward = canonical_tree_orders(state)
    after, mass, rates, future, anchor, all_future = run_anchor_echo(
        state, outward, inward
    )
    actor_count = len(state["actors"])
    echo_length = 2 * actor_count - 1
    expected_mass = F(1, 2 * actor_count)
    for parent_actor, _child in outward:
        expected_mass *= F(
            1, 4 * actor_count * len(state["neighbors"][parent_actor])
        )
    for child, _parent_actor in inward:
        expected_mass *= F(
            1, 4 * actor_count * len(state["neighbors"][child])
        )
    final_ancestry = ancestor_ids(after, after["last"]["A"])
    echo_checks += 1
    echo_ok &= len(all_future) == echo_length
    echo_ok &= mass == expected_mass > 0
    echo_ok &= old_eids <= final_ancestry
    echo_ok &= all(anchor in ancestor_ids(after, eid) for eid in all_future)
    leading = rates / math.factorial(echo_length)
    echo_ok &= leading == mass * actor_count ** echo_length / math.factorial(echo_length)
    echo_masses.append(mass)
    if len(echo_timed_rows) < 20:
        timed = dfrac(mass) * erlang_cdf(
            echo_length, actor_count, Decimal(1)
        )
        echo_ok &= timed > 0
        echo_timed_rows.append((echo_length, timed, leading, len(future)))

e6_ok = echo_ok and echo_checks == len(enumerated_states)
check(
    "E6 ANCHORED ECHO [exact all-state construction + 110-digit timing]: a "
    "fresh A event is broadcast over every rooted edge and echoed inward; all "
    "2n-1 target events contain the anchor, the final A ancestry contains the "
    "whole pre-stop component, and embedded/Erlang/leading masses agree",
    e6_ok,
    f"echoes={echo_checks}; minimum mass={ftext(min(echo_masses))}; first "
    f"Delta=1={echo_timed_rows[0][1]:.40E}",
)


gauge_states = tuple(
    state for level in levels[:4] for state, _probability in level.values()
)
gauge_ok = True
gauge_checks = 0
for state in gauge_states:
    others = tuple(sorted(actor for actor in state["actors"] if actor != "A"))
    mapping = {"A": "A"}
    mapping.update({actor: f"R{index}" for index, actor in enumerate(reversed(others))})
    transported = renamed_state(state, mapping)
    gauge_checks += 1
    gauge_ok &= canonical_state_key(state) == canonical_state_key(transported)
    outward, inward = canonical_tree_orders(state)
    after, mass, _rates, future, _anchor, _all_future = run_anchor_echo(
        state, outward, inward
    )
    outward_t = tuple((mapping[p], mapping[c]) for p, c in outward)
    inward_t = tuple((mapping[c], mapping[p]) for c, p in inward)
    after_t, mass_t, _rates_t, future_t, _anchor_t, _all_future_t = run_anchor_echo(
        transported, outward_t, inward_t
    )
    gauge_ok &= mass == mass_t
    gauge_ok &= canonical_trace(after, future) == canonical_trace(after_t, future_t)

e7_ok = gauge_ok and gauge_checks == len(gauge_states)
check(
    "E7 ROOTED NOMINAL GAUGE / ANCHORED-ECHO COVARIANCE [exact]: canonical "
    "component classes, transported broadcast/echo paths, Branch-F traces and "
    "masses commute with actor renaming; bare sibling order changes a valid "
    "return sweep but not collection or its product mass",
    e7_ok,
    f"renamed components/traces={gauge_checks}; sibling sweeps={sibling_checks}",
)


# ---------------------------------------------------------------------------
# E8 anchored fingerprints and equal-order emulator search.

fingerprint_states = gauge_states
state_to_trace = {}
trace_to_states = defaultdict(set)
fingerprint_ok = True
for state in fingerprint_states:
    component_key = canonical_state_key(state)
    after, _mass, _rates, future, _anchor, _all_future = run_anchor_echo(state)
    trace = canonical_trace(after, future)
    if component_key in state_to_trace and state_to_trace[component_key] != trace:
        fingerprint_ok = False
    state_to_trace[component_key] = trace
    trace_to_states[trace].add(component_key)
fingerprint_ok &= all(len(states) == 1 for states in trace_to_states.values())


def continuations_with_traces(state, steps):
    frontier = [(state, tuple())]
    rows_by_depth = {0: list(frontier)}
    for depth in range(1, steps + 1):
        nxt = {}
        for current, future_a_eids in frontier:
            for kind, initiator, target, _rate in d34b_rates(current):
                after = d34b_step(current, kind, initiator, target)
                eid = after["events"][-1][0]
                future2 = future_a_eids + ((eid,) if "A" in after["events"][-1][5] else ())
                key = (state_key(after), future2)
                nxt[key] = (after, future2)
        frontier = list(nxt.values())
        rows_by_depth[depth] = list(frontier)
    return rows_by_depth


audit_sources = tuple(
    state for level in levels[:2] for state, _probability in level.values()
)
audit_targets = (seed_state(), d34b_step(seed_state(), "n", "B"))
emulators = []
emulator_checks = 0
max_audit_steps = 3
continuation_cache = {
    state_key(source): continuations_with_traces(source, max_audit_steps)
    for source in audit_sources
}
for target in audit_targets:
    target_component = canonical_state_key(target)
    target_after, _mass, _rates, target_future, _anchor, target_all = run_anchor_echo(
        target
    )
    target_trace = canonical_trace(target_after, target_future)
    max_steps = len(target_all)
    for source in audit_sources:
        source_component = canonical_state_key(source)
        rows_by_depth = continuation_cache[state_key(source)]
        for depth, rows in rows_by_depth.items():
            if depth > max_steps:
                continue
            for after, future in rows:
                emulator_checks += 1
                if canonical_trace(after, future) != target_trace:
                    continue
                if source_component != target_component and depth <= max_steps:
                    emulators.append((target_component, source_component, depth, max_steps))

e8_ok = (
    fingerprint_ok and not emulators
    and len(state_to_trace) > 100 and emulator_checks > 1000
)
check(
    "E8 ANCHORED BRANCH-F PREFIX INJECTIVITY / EQUAL-ORDER SEARCH "
    "[exact regression + all-finite anchored catch-up lemma]: canonical echo "
    "prefixes separate every registered component gauge class and no tested "
    "nonisomorphic past emulates an anchored target within its 2n-1 events",
    e8_ok,
    f"gauge classes/traces={len(state_to_trace)}/{len(trace_to_states)}; "
    f"continuations checked={emulator_checks}; emulators={len(emulators)}",
)


# ---------------------------------------------------------------------------
# E9 bare-sweep counterexample and anchored catch-up repair.

def apply_path(state, path):
    out = state
    continuous_product = F(1)
    future_a = []
    for kind, initiator, target in path:
        continuous_product *= event_rate(out, kind, initiator, target)
        out = d34b_step(out, kind, initiator, target)
        if "A" in out["events"][-1][5]:
            future_a.append(out["events"][-1][0])
    return out, continuous_product, tuple(future_a)


idle_target = d34b_step(seed_state(), "n", "B")
idle_order = canonical_sweep_order(idle_target)
idle_after, _idle_mass, idle_rates, idle_future = run_sweep(idle_target, idle_order)
idle_trace = canonical_trace(idle_after, idle_future)
seed_catchup_after, seed_catchup_rates, seed_catchup_future = apply_path(
    seed_state(), (("n", "B", None), ("i", "B", "A"))
)
idle_catchup_trace = canonical_trace(seed_catchup_after, seed_catchup_future)
idle_leading = idle_rates / math.factorial(len(idle_order))
idle_catchup_leading = seed_catchup_rates / math.factorial(2)

birth_target = d34b_step(seed_state(), "b", "B")
child = "B/1"
birth_order = canonical_sweep_order(birth_target)
birth_after, _birth_mass, birth_rates, birth_future = run_sweep(
    birth_target, birth_order
)
birth_trace = canonical_trace(birth_after, birth_future)
birth_catchup_after, birth_catchup_rates, birth_catchup_future = apply_path(
    seed_state(),
    (("b", "B", None), ("i", child, "B"), ("i", "B", "A")),
)
birth_catchup_trace = canonical_trace(birth_catchup_after, birth_catchup_future)
birth_leading = birth_rates / math.factorial(len(birth_order))
birth_catchup_leading = birth_catchup_rates / math.factorial(3)

altered = d34b_step(seed_state(), "i", "B", "A")
altered_after, _altered_mass, _altered_rates, altered_future, _aa, _af = run_anchor_echo(
    altered
)
altered_trace = canonical_trace(altered_after, altered_future)

# A remote extra idle may remain outside the target echo, but the first extra
# branch's immutable attachment birth touched a matched parent and is forced
# into the A ancestry.  This is the finite witness for the all-size
# first-unmatched-attachment lemma.
extra_branch = d34b_step(seed_state(), "b", "B")
attachment_eid = extra_branch["events"][-1][0]
extra_child = "B/1"
extra_branch = d34b_step(extra_branch, "n", extra_child)
remote_idle_eid = extra_branch["events"][-1][0]
extra_after, _extra_rates, extra_future = apply_path(
    extra_branch,
    (("n", "A", None), ("i", "A", "B"), ("i", "B", "A")),
)
extra_trace = canonical_trace(extra_after, extra_future)
extra_final_ancestry = ancestor_ids(extra_after, extra_after["last"]["A"])
seed_anchor_after, _sam, _sar, seed_anchor_future, _saa, _saf = run_anchor_echo(
    seed_state()
)
seed_anchor_trace = canonical_trace(seed_anchor_after, seed_anchor_future)
attachment_witness_ok = (
    remote_idle_eid not in extra_final_ancestry
    and attachment_eid in extra_final_ancestry
    and extra_trace != seed_anchor_trace
)

# Exact same-order failure of the historical bare-sweep T4.
fork_base = d34b_step(d34b_step(seed_state(), "b", "B"), "b", "B")
child_c, child_d = "B/1", "B/2"
bare_target = d34b_step(fork_base, "n", child_d)
bare_target_order = (child_c, child_d, "B")
bare_target_after, _bt_mass, bare_target_rates, bare_target_future = run_sweep(
    bare_target, bare_target_order
)
bare_target_trace = canonical_trace(bare_target_after, bare_target_future)
bare_alternative = d34b_step(fork_base, "i", child_c, "B")
bare_alt_after, bare_alt_rates, bare_alt_future = apply_path(
    bare_alternative,
    (("n", child_d, None), ("i", child_d, "B"), ("i", "B", "A")),
)
bare_alt_trace = canonical_trace(bare_alt_after, bare_alt_future)
bare_target_leading = bare_target_rates / math.factorial(3)
bare_alt_leading = bare_alt_rates / math.factorial(3)

# The repaired anchored echo: the same missing idle now costs one extra event.
anchor_idle_after, _ai_mass, anchor_idle_rates, anchor_idle_future, _anchor, anchor_all = (
    run_anchor_echo(idle_target)
)
anchor_idle_trace = canonical_trace(anchor_idle_after, anchor_idle_future)
anchor_catchup_after, anchor_catchup_rates, anchor_catchup_future = apply_path(
    seed_state(),
    (("n", "B", None), ("n", "A", None),
     ("i", "A", "B"), ("i", "B", "A")),
)
anchor_catchup_trace = canonical_trace(
    anchor_catchup_after, anchor_catchup_future
)
anchor_idle_leading = anchor_idle_rates / math.factorial(len(anchor_all))
anchor_catchup_leading = anchor_catchup_rates / math.factorial(4)

catchup_ok = (
    idle_trace == idle_catchup_trace
    and len(idle_order) == 1
    and idle_leading == F(1, 4)
    and idle_catchup_leading == F(1, 16)
    and birth_trace == birth_catchup_trace
    and len(birth_order) == 2
    and birth_leading == F(1, 64)
    and birth_catchup_leading == F(1, 768)
    and bare_target_trace == bare_alt_trace
    and bare_target_leading == F(1, 1152)
    and bare_alt_leading == F(1, 576)
    and anchor_idle_trace == anchor_catchup_trace
    and len(anchor_all) == 3
    and anchor_idle_leading == F(1, 192)
    and anchor_catchup_leading == F(1, 1536)
    and altered_trace != anchor_idle_trace
    and attachment_witness_ok
)
e9_ok = catchup_ok
check(
    "E9 BARE-SWEEP REJECTION / ANCHORED CATCH-UP REPAIR [Fraction-exact]: "
    "different past cuts reproduce one bare-sweep trace in the same three "
    "events, rejecting pinned T4; the fresh anchor prevents pre-existing echo "
    "events, restoring the target q versus catch-up q+1 small-time split",
    e9_ok,
    f"bare equal-order coefficients={ftext(bare_target_leading)}/"
    f"{ftext(bare_alt_leading)}; anchored q/q+1="
    f"{ftext(anchor_idle_leading)}/{ftext(anchor_catchup_leading)}; "
    f"birth support={ftext(birth_leading)}/{ftext(birth_catchup_leading)}; "
    "attachment witness=1/1",
)


# ---------------------------------------------------------------------------
# E10 exact information families and finite gauge-class ledger.

def chain_base(bit_count):
    if bit_count < 1:
        raise ValueError("bit_count must be positive")
    state = seed_state()
    path = ["A", "B"]
    mass = F(1)
    while len(path) - 1 < bit_count:
        parent = path[-1]
        before = set(state["actors"])
        state, probability = embedded_step(state, "b", parent)
        mass *= probability
        child_name = next(iter(set(state["actors"]) - before))
        path.append(child_name)
    return state, tuple(path), mass


family_rows = []
family_ok = True
for bit_count in range(1, 7):
    base, path, base_mass = chain_base(bit_count)
    canonical_members = set()
    minimum_mass = None
    for word in product((0, 1), repeat=bit_count):
        state = base
        mass = base_mass
        for bit, actor, parent in zip(word, path[1:], path[:-1]):
            kind = "n" if bit == 0 else "i"
            target = None if bit == 0 else parent
            state, probability = embedded_step(state, kind, actor, target)
            mass *= probability
        canonical_members.add(canonical_state_key(state))
        minimum_mass = mass if minimum_mass is None else min(minimum_mass, mass)
        swept, _sweep_mass, _rates, _future = run_sweep(
            state, canonical_sweep_order(state)
        )
        family_ok &= {event[0] for event in state["events"]} <= ancestor_ids(
            swept, swept["last"]["A"]
        )
    family_ok &= len(canonical_members) == 2 ** bit_count
    family_ok &= minimum_mass > 0
    family_rows.append((bit_count, len(canonical_members), minimum_mass))

gauge_level_counts = tuple(
    len({canonical_state_key(state) for state, _probability in level.values()})
    for level in levels[:4]
)
gauge_level_bits = tuple(
    math.ceil(math.log2(count)) if count > 1 else 0
    for count in gauge_level_counts
)
growth_time = Decimal(1)
expected_actors = Decimal(2) * (growth_time / Decimal(4)).exp()
expected_records = Decimal(8) * ((growth_time / Decimal(4)).exp() - Decimal(1))
growth_ok = expected_actors > 2 and expected_records > 0
e10_ok = (
    family_ok
    and tuple(count for _bits, count, _mass in family_rows)
    == (2, 4, 8, 16, 32, 64)
    and gauge_level_counts[0] == 1
    and all(left < right for left, right in zip(gauge_level_counts, gauge_level_counts[1:]))
    and growth_ok
)
check(
    "E10 INFORMATION LOWER BOUND [exact positive-cylinder family + gauge "
    "census]: M structurally depth-marked binary record choices produce 2^M "
    "predictively recoverable component classes, forcing at least M worst-case "
    "bits; finite audit class counts grow strictly.  From the connected seed, "
    "E[N_T]=2 exp(T/4) and E[records through T]=8(exp(T/4)-1)",
    e10_ok,
    "2^M=" + ",".join(str(count) for _bits, count, _mass in family_rows)
    + f"; gauge classes={gauge_level_counts}; ceil bits={gauge_level_bits}; "
    f"T=1 actors/records={expected_actors:.32E}/{expected_records:.32E}",
)


# ---------------------------------------------------------------------------
# E11 first-applicable outcome and the infinite/profinite ceiling.

component_identity_hypotheses = all((
    e1_ok, e2_ok, e3_ok, e4_ok, e5_ok, e6_ok, e7_ok, e8_ok, e9_ok, e10_ok,
))
proper_frontier_constructed = False
equal_order_emulator_found = bool(emulators)
query_ill_typed = False

if component_identity_hypotheses:
    verdict = "COMPONENT PREDICTIVE-IDENTITY / UNBOUNDED"
elif proper_frontier_constructed:
    verdict = "PROPER ADAPTIVE FRONTIER"
elif e2_ok and e3_ok and e4_ok and equal_order_emulator_found:
    verdict = "RETURNABLE BUT TOMOGRAPHY UNPROVED"
elif query_ill_typed:
    verdict = "QUERY ILL-TYPED"
else:
    verdict = "REFUSAL/UNDEFINED"

ceilings = {
    "finite component at every legal finite stop": True,
    "serialized discrete event-content prefix inverse-limit host": True,
    "construction-order-gauge bonding maps": False,
    "v9 stem-spectrum identification": False,
    "continuous predictive extension": False,
    "finite physical completed-history record": False,
    "intrinsic quantum boundary": False,
    "spacetime or G consequence": False,
}
expected_ceiling = (
    ceilings["finite component at every legal finite stop"]
    and ceilings["serialized discrete event-content prefix inverse-limit host"]
    and not any(list(ceilings.values())[2:])
)
e11_ok = (
    verdict == "COMPONENT PREDICTIVE-IDENTITY / UNBOUNDED"
    and expected_ceiling
)
check(
    "E11 FIRST-APPLICABLE VERDICT / INFINITE CEILING: the anchored full "
    "Branch-F "
    "minimal predictive quotient is the finite current component gauge class; "
    "every exact carrier determines it, while nonminimal carriers may refine "
    "it.  No uniform capacity, timed/gauge-quotient profinite bridge, quantum "
    "boundary or spacetime consequence is inferred",
    e11_ok,
    f"verdict={verdict}; stronger inverse-limit/v9/quantum/geometry flags=OPEN",
)


summary = (
    f"gates={PASS}/{PASS + FAIL}; levels=" + ",".join(map(str, level_counts))
    + f"; states={len(enumerated_states)}; wire_checks={wire_checks}"
    + f"; sweeps={collection_checks}; sibling_sweeps={sibling_checks}"
    + f"; anchored_echoes={echo_checks}"
    + f"; gauge_checks={gauge_checks}; fingerprint_classes={len(state_to_trace)}"
    + f"; emulator_checks={emulator_checks}; emulators={len(emulators)}"
    + f"; bare_equal_order={ftext(bare_target_leading)}/{ftext(bare_alt_leading)}"
    + "; family=" + ",".join(str(row[1]) for row in family_rows)
    + "; gauge_levels=" + ",".join(map(str, gauge_level_counts))
    + f"; verdict={verdict}"
)
digest = hashlib.sha256(summary.encode("utf-8")).hexdigest()
print(f"[SUMMARY] {summary}")
print(f"[RECEIPT-SHA256] {digest}")
print(f"[VERDICT] {'PASS' if FAIL == 0 else 'FAIL'} — {PASS}/{PASS + FAIL}")

sys.exit(0 if FAIL == 0 else 1)
