#!/usr/bin/env python3
"""D34e exact receipt: predictive record-DAG boundaries for chosen D34b.

Pin: note-d34e-predictive-record-dag-boundary.md / commit 3c983d0,
committed before this executable existed.

The receipt keeps three passive query branches separate:

* C: coarse A-wire kind/time/carrier records;
* L: the same local wire process with typed incident-actor roles;
* F: full persistent ancestor sub-DAGs of future A records.

Discrete probabilities and generator coefficients are Fraction-exact.  The
only transcendental values are explicitly labeled 100-decimal evaluations of
analytic exponential/Poisson identities.  Finite enumeration is bounded and
does not replace the analytic generator partition carried by the pin.  No
timed controlled D34b-D34c quantum process or v9 predictive factorization is
invented.  Exit 1 on any failed gate.
"""

from collections import Counter, defaultdict, deque
import copy
from decimal import Decimal, getcontext
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, permutations
import hashlib
import math
from pathlib import Path
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


def ftext(x):
    return str(x) if x.denominator != 1 else str(x.numerator)


def dfrac(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


print("[d34e — exact predictive record-DAG boundary]")


# ---------------------------------------------------------------------------
# E1: literal chosen D34b state, generator and embedded positive cylinders.

def seed_state(remote=False):
    neighbors = {"A": {"B"}, "B": {"A"}}
    if remote:
        neighbors.update({"P": {"Q"}, "Q": {"P"}})
    return {
        "actors": {
            name: {
                "ring": 0,
                "births": 0,
                "sealed": False,
                "carrier": 0,
            }
            for name in neighbors
        },
        "neighbors": neighbors,
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
        name for name, row in state["actors"].items() if not row["sealed"]
    ))


def d34b_rates(state):
    rows = []
    for y in active_actors(state):
        eligible = tuple(sorted(
            x for x in state["neighbors"][y]
            if not state["actors"][x]["sealed"]
        ))
        if not eligible:
            raise ValueError("chosen D34b requires at least one eligible neighbor")
        rows.append(("b", y, None, F(1, 4)))
        for x in eligible:
            rows.append(("i", y, x, F(1, 4 * len(eligible))))
        rows.append(("n", y, None, F(1, 2)))
    return tuple(rows)


def d34b_step(state, kind, y, target=None):
    out = copy_state(state)
    actor = out["actors"][y]
    if actor["sealed"]:
        raise ValueError("sealed initiator")
    actor["ring"] += 1
    eid = f"{y}#r{actor['ring']}"
    if kind == "b":
        actor["births"] += 1
        target = f"{y}/{actor['births']}"
        if target in out["actors"]:
            raise ValueError("duplicate child")
        out["actors"][target] = {
            "ring": 0, "births": 0, "sealed": False, "carrier": 0,
        }
        out["neighbors"][y].add(target)
        out["neighbors"][target] = {y}
        touched = (y, target)
    elif kind == "i":
        if (target not in out["neighbors"][y]
                or out["actors"][target]["sealed"]):
            raise ValueError("ineligible interaction")
        touched = (y, target)
        out["actors"][y]["carrier"] ^= 1
        out["actors"][target]["carrier"] ^= 1
    elif kind == "n":
        touched = (y,)
    else:
        raise ValueError(kind)
    predecessors = tuple(sorted(
        out["last"][name] for name in touched if name in out["last"]
    ))
    out["events"].append(
        (eid, kind, y, target, predecessors, tuple(touched))
    )
    for name in touched:
        out["last"][name] = eid
    return out


def event_rate(state, kind, y, target=None):
    return next(rate for k, yy, x, rate in d34b_rates(state)
                if (k, yy, x) == (kind, y, target))


def embedded_step(state, kind, y, target=None):
    probability = event_rate(state, kind, y, target) / len(active_actors(state))
    return d34b_step(state, kind, y, target), probability


def state_key(state):
    actors = tuple(sorted(
        (name, row["ring"], row["births"], row["sealed"], row["carrier"])
        for name, row in state["actors"].items()
    ))
    neighbors = tuple(sorted(
        (name, tuple(sorted(xs))) for name, xs in state["neighbors"].items()
    ))
    events = tuple(sorted(repr(e) for e in state["events"]))
    last = tuple(sorted(state["last"].items()))
    return actors, neighbors, events, last


def enumerate_levels(depth):
    levels = [{state_key(seed_state()): (seed_state(), F(1))}]
    for _ in range(depth):
        nxt = {}
        for state, probability in levels[-1].values():
            k = len(active_actors(state))
            row_mass = sum(rate / k for *_, rate in d34b_rates(state))
            if row_mass != 1:
                raise AssertionError(row_mass)
            for kind, y, target, rate in d34b_rates(state):
                state2 = d34b_step(state, kind, y, target)
                p2 = probability * rate / k
                key = state_key(state2)
                if key in nxt:
                    nxt[key] = (nxt[key][0], nxt[key][1] + p2)
                else:
                    nxt[key] = (state2, p2)
        if sum((p for _, p in nxt.values()), F(0)) != 1:
            raise AssertionError("level not normalized")
        levels.append(nxt)
    return levels


levels = enumerate_levels(4)
level_counts = tuple(len(level) for level in levels)
law_rows_normalized = all(
    sum((rate for *_, rate in d34b_rates(state)), F(0))
    == len(active_actors(state))
    for level in levels for state, _ in level.values()
)
e1_ok = (
    level_counts[0] == 1
    and all(sum((p for _, p in level.values()), F(0)) == 1 for level in levels)
    and law_rows_normalized
)
check(
    "E1 CHOSEN D34b LAW / D(N=4) REACHABLE DOMAIN [Fraction-exact]: every "
    "actor row has total intensity one; embedded levels are normalized and "
    "retain typed adjacency, counters, carriers, tips and persistent events",
    e1_ok,
    f"reachable level counts={level_counts}",
)


# ---------------------------------------------------------------------------
# Boundary projections and the proposed coarse marked generator.

def wire_count(state, actor):
    return sum(actor in event[5] for event in state["events"])


def hist_from_degrees(degrees):
    return tuple(sorted(Counter(degrees).items()))


def hist_counter(hist):
    return Counter(dict(hist))


def hist_shift(hist, old_degree, new_degree):
    counts = hist_counter(hist)
    counts[old_degree] -= 1
    if counts[old_degree] == 0:
        del counts[old_degree]
    counts[new_degree] += 1
    return tuple(sorted(counts.items()))


def hist_add_one(hist):
    counts = hist_counter(hist)
    counts[1] += 1
    return tuple(sorted(counts.items()))


def boundary_dyn(state, actor="A"):
    degrees = [len(state["neighbors"][x]) for x in state["neighbors"][actor]]
    return state["actors"][actor]["carrier"], hist_from_degrees(degrees)


def boundary_scoped(state, actor="A"):
    carrier, hist = boundary_dyn(state, actor)
    return (
        carrier,
        hist,
        state["actors"][actor]["ring"],
        wire_count(state, actor),
    )


def row_output(kind, y, target, actor="A"):
    if y == actor:
        return {"b": "A-birth", "n": "A-idle", "i": "A-outgoing"}[kind]
    if kind == "i" and target == actor:
        return "incoming-to-A"
    return None


def coarse_output_mark(label, after):
    if len(after) == 4:
        return f"{label}:c{after[0]}:r{after[2]}:w{after[3]}"
    return f"{label}:c{after[0]}"


def global_projected_rows(state, actor="A", scoped=True):
    project = boundary_scoped if scoped else boundary_dyn
    before = project(state, actor)
    rows = Counter()
    for kind, y, target, rate in d34b_rates(state):
        after_state = d34b_step(state, kind, y, target)
        after = project(after_state, actor)
        label = row_output(kind, y, target, actor)
        if label is None and after == before:
            continue
        # Silent neighbor births update the carrier but emit no A-wire record.
        # The special None mark below is an internal CTMC transition, not an
        # observable tau symbol in Branch C.
        marked_label = coarse_output_mark(label, after) if label is not None else None
        rows[(marked_label, after)] += rate
    return rows


def boundary_formula_rows(boundary):
    scoped = len(boundary) == 4
    if scoped:
        carrier, hist, own_rings, wire_events = boundary
    else:
        carrier, hist = boundary
        own_rings = wire_events = None

    def pack(c, h, dr=0, dw=0):
        if scoped:
            return c, h, own_rings + dr, wire_events + dw
        return c, h

    rows = Counter()
    after_birth = pack(carrier, hist_add_one(hist), 1, 1)
    after_idle = pack(carrier, hist, 1, 1)
    after_outgoing = pack(1 - carrier, hist, 1, 1)
    rows[(coarse_output_mark("A-birth", after_birth), after_birth)] += F(1, 4)
    rows[(coarse_output_mark("A-idle", after_idle), after_idle)] += F(1, 2)
    rows[(coarse_output_mark("A-outgoing", after_outgoing), after_outgoing)] += F(1, 4)
    for degree, count in hist:
        shifted = hist_shift(hist, degree, degree + 1)
        rows[(None, pack(carrier, shifted))] += F(count, 4)
        after_incoming = pack(1 - carrier, hist, 0, 1)
        rows[(coarse_output_mark("incoming-to-A", after_incoming),
              after_incoming)] += F(count, 4 * degree)
    return rows


def labeled_star_boundary(state, actor="A"):
    return (
        state["actors"][actor]["carrier"],
        state["actors"][actor]["ring"],
        state["actors"][actor]["births"],
        wire_count(state, actor),
        tuple(sorted(
            (neighbor, len(state["neighbors"][neighbor]),
             state["actors"][neighbor]["births"])
            for neighbor in state["neighbors"][actor]
        )),
    )


def global_labeled_rows(state, actor="A"):
    before = labeled_star_boundary(state, actor)
    rows = Counter()
    for kind, y, target, rate in d34b_rates(state):
        after_state = d34b_step(state, kind, y, target)
        after = labeled_star_boundary(after_state, actor)
        if y == actor:
            if kind == "b":
                new_neighbors = set(after_state["neighbors"][actor]) - set(
                    state["neighbors"][actor]
                )
                new_child = next(iter(new_neighbors))
                label = (
                    f"A-birth:{new_child}:c{after[0]}:r{after[1]}:w{after[3]}"
                )
            elif kind == "n":
                label = f"A-idle:c{after[0]}:r{after[1]}:w{after[3]}"
            else:
                label = (
                    f"A-outgoing:{target}:c{after[0]}:r{after[1]}:w{after[3]}"
                )
        elif kind == "i" and target == actor:
            label = f"incoming:{y}:c{after[0]}:r{after[1]}:w{after[3]}"
        else:
            label = None
        if label is None and after == before:
            continue
        rows[(label, after)] += rate
    return rows


def labeled_formula_rows(boundary, root="A"):
    carrier, a_rings, a_births, a_wire, neighbor_rows = boundary
    rows = Counter()
    new_child = f"{root}/{a_births + 1}"
    after_birth_neighbors = tuple(sorted((*neighbor_rows, (new_child, 1, 0))))
    after_birth = (
        carrier, a_rings + 1, a_births + 1, a_wire + 1,
        after_birth_neighbors,
    )
    rows[((
        f"A-birth:{new_child}:c{carrier}:r{a_rings + 1}:w{a_wire + 1}",
        after_birth,
    ))] += F(1, 4)
    after_idle = (
        carrier, a_rings + 1, a_births, a_wire + 1, neighbor_rows,
    )
    rows[((
        f"A-idle:c{carrier}:r{a_rings + 1}:w{a_wire + 1}", after_idle,
    ))] += F(1, 2)
    degree_a = len(neighbor_rows)
    for neighbor, degree, neighbor_births in neighbor_rows:
        rows[(
            f"A-outgoing:{neighbor}:c{1 - carrier}:r{a_rings + 1}:w{a_wire + 1}",
            (1 - carrier, a_rings + 1, a_births, a_wire + 1,
             neighbor_rows),
        )] += F(1, 4 * degree_a)
        shifted_rows = tuple(sorted(
            (name,
             d + 1 if name == neighbor else d,
             births + 1 if name == neighbor else births)
            for name, d, births in neighbor_rows
        ))
        rows[(
            None,
            (carrier, a_rings, a_births, a_wire, shifted_rows),
        )] += F(1, 4)
        rows[(
            f"incoming:{neighbor}:c{1 - carrier}:r{a_rings}:w{a_wire + 1}",
            (1 - carrier, a_rings, a_births, a_wire + 1,
             neighbor_rows),
        )] += F(1, 4 * degree)
    return rows


def rows_key(rows):
    return tuple(sorted(
        ((repr(key), value.numerator, value.denominator)
         for key, value in rows.items()),
        key=repr,
    ))


enumerated_states = [
    state for level in levels for state, _ in level.values()
]
projection_matches = all(
    global_projected_rows(state) == boundary_formula_rows(boundary_scoped(state))
    for state in enumerated_states
)
labeled_projection_matches = all(
    global_labeled_rows(state)
    == labeled_formula_rows(labeled_star_boundary(state))
    for state in enumerated_states
)

# Strong-lumpability regression: any two enumerated global states with the
# same boundary have exactly the same projected marked row.
boundary_row_keys = {}
lumpability_collisions = 0
for state in enumerated_states:
    boundary = boundary_scoped(state)
    key = rows_key(global_projected_rows(state))
    if boundary in boundary_row_keys:
        lumpability_collisions += 1
        if boundary_row_keys[boundary] != key:
            projection_matches = False
    else:
        boundary_row_keys[boundary] = key

e2_ok = (
    projection_matches and labeled_projection_matches
    and lumpability_collisions > 0
)
check(
    "E2 DISTRIBUTED HISTOGRAM / ROLE-LABELED STAR GENERATORS [exact finite "
    "regression + analytic row partitions]: full D34b rows project to the "
    "coarse degree histogram and separately to typed incident-actor rows, "
    "including elapsed-time gauge, A-own/A-wire counters, emitted carrier bit "
    "and source/target roles",
    e2_ok,
    f"states checked twice={len(enumerated_states)}; equal coarse-boundary "
    f"collisions={lumpability_collisions}",
)


# ---------------------------------------------------------------------------
# E3: B0 one-record obstruction and B1 instantaneous-rate obstruction.

o1_before = seed_state()
o1_after = d34b_step(o1_before, "b", "B")
o1_rate_before = event_rate(o1_before, "i", "B", "A")
o1_rate_after = event_rate(o1_after, "i", "B", "A")
o1_a_same = (
    o1_before["actors"]["A"] == o1_after["actors"]["A"]
    and o1_before["last"].get("A") == o1_after["last"].get("A")
)


def build_histogram_state(degrees):
    state = seed_state()
    mass = F(1)
    while len(state["neighbors"]["A"]) < len(degrees):
        before = set(state["actors"])
        state, p = embedded_step(state, "b", "A")
        mass *= p
        if len(set(state["actors"]) - before) != 1:
            raise AssertionError("birth did not create one child")
    neighbors = sorted(state["neighbors"]["A"])
    for actor, target_degree in zip(neighbors, degrees):
        while len(state["neighbors"][actor]) < target_degree:
            state, p = embedded_step(state, "b", actor)
            mass *= p
    return state, mass


hist_degrees_left = (2, 3, 6)
hist_degrees_right = (2, 4, 4)
hist_state_left, hist_mass_left = build_histogram_state(hist_degrees_left)
hist_state_right, hist_mass_right = build_histogram_state(hist_degrees_right)


def incoming_rate_from_hist(hist):
    return sum((F(count, 4 * degree) for degree, count in hist), F(0))


def incoming_rate_derivative(hist):
    # A birth adds a degree-one neighbor at rate 1/4.  Each degree-k neighbor
    # births at rate 1/4 and changes 1/(4k) to 1/[4(k+1)].
    return F(1, 16) - sum(
        (F(count, 16 * degree * (degree + 1)) for degree, count in hist),
        F(0),
    )


hist_left = boundary_dyn(hist_state_left)[1]
hist_right = boundary_dyn(hist_state_right)[1]
rate_left = incoming_rate_from_hist(hist_left)
rate_right = incoming_rate_from_hist(hist_right)
derivative_left = incoming_rate_derivative(hist_left)
derivative_right = incoming_rate_derivative(hist_right)
derivative_gap = derivative_right - derivative_left

e3_ok = (
    o1_rate_before == F(1, 4)
    and o1_rate_after == F(1, 8)
    and o1_a_same
    and hist_left == hist_from_degrees(hist_degrees_left)
    and hist_right == hist_from_degrees(hist_degrees_right)
    and rate_left == rate_right == F(1, 4)
    and derivative_left == F(61, 1344)
    and derivative_right == F(11, 240)
    and derivative_gap == F(1, 2240)
    and hist_mass_left > 0 and hist_mass_right > 0
)
check(
    "E3 B0/B1 EXACT OBSTRUCTIONS: one-record A misses B degree "
    "(1/4->1/8); reachable histograms {2,3,6} and {2,4,4} have the same "
    "A degree and current incoming rate 1/4 but different Lf, so the scalar "
    "rate summary is not recursively predictive",
    e3_ok,
    f"Lf={ftext(derivative_left)} vs {ftext(derivative_right)}; gap="
    f"{ftext(derivative_gap)}; positive past masses="
    f"{ftext(hist_mass_left)},{ftext(hist_mass_right)}",
)


# ---------------------------------------------------------------------------
# E4: coinductive strong boundary-transition bisimulation and stopping scope.

@lru_cache(maxsize=None)
def transition_bisimulation_signature(boundary, horizon):
    """Strong CTMC signature; None is internal, never an A-wire output."""
    if horizon == 0:
        return ()
    aggregated = Counter()
    for (label, after), rate in boundary_formula_rows(boundary).items():
        child_class = transition_bisimulation_signature(after, horizon - 1)
        aggregated[(label, child_class)] += rate
    return tuple(sorted([
        (label, rate.numerator, rate.denominator, child_class)
        for (label, child_class), rate in aggregated.items()
    ], key=repr))


synthetic_boundaries = []
for neighbor_count in range(1, 4):
    for degrees in combinations_with_replacement(range(1, 6), neighbor_count):
        hist = hist_from_degrees(degrees)
        for carrier in (0, 1):
            synthetic_boundaries.append((carrier, hist))

synthetic_predictive_counts = tuple(
    len({transition_bisimulation_signature(boundary, horizon)
         for boundary in synthetic_boundaries})
    for horizon in (1, 2, 3)
)
registered_boundaries = tuple(sorted(
    {boundary_scoped(state) for state in enumerated_states}, key=repr
))
registered_predictive_counts = tuple(
    len({transition_bisimulation_signature(boundary, horizon)
         for boundary in registered_boundaries})
    for horizon in (1, 2, 3)
)


def relevant_intensity(boundary):
    return sum(boundary_formula_rows(boundary).values(), F(0))


q_left = relevant_intensity((0, hist_left))
q_right = relevant_intensity((0, hist_right))
t_probe = Decimal("1.375")
survival_left = (-(dfrac(q_left) * t_probe)).exp()
survival_right = (-(dfrac(q_right) * t_probe)).exp()

counter_rows_integrated = True
for state in enumerated_states:
    before = boundary_scoped(state)
    for (label, after), _rate in global_projected_rows(state).items():
        delta = after[2] - before[2], after[3] - before[3]
        kind = label.split(":", 1)[0] if label is not None else None
        expected = (
            (1, 1) if kind in {"A-birth", "A-idle", "A-outgoing"}
            else (0, 1) if kind == "incoming-to-A"
            else (0, 0)
        )
        counter_rows_integrated &= delta == expected

# Time-translation gauge: the carrier clock starts at zero at the conditioning
# stop and future records carry elapsed increments.  The full boundary CTMC is
# time homogeneous.  Strong Markov at own-ring/wire-count hitting sets follows
# from the inherited nonexplosive pure-jump theorem; this executable gates the
# actual monotone count rows used by those hitting sets.
elapsed_origin = F(0)
elapsed_increment = F(11, 8)
b1_horizon_split = (
    transition_bisimulation_signature((0, hist_left), 1)
    == transition_bisimulation_signature((0, hist_right), 1)
    and transition_bisimulation_signature((0, hist_left), 2)
    != transition_bisimulation_signature((0, hist_right), 2)
)
e4_ok = (
    synthetic_predictive_counts == (106, 110, 110)
    and registered_predictive_counts == (111, 111, 111)
    and b1_horizon_split
    and q_left == q_right
    and survival_left == survival_right
    and counter_rows_integrated
    and elapsed_origin + elapsed_increment == F(11, 8)
)
check(
    "E4 STRONG BOUNDARY-TRANSITION BISIMULATION / RELATIVE-TIME STOPPING "
    "[exact + 100-decimal analytic regression]: non-silent marks contain the "
    "declared post carrier and own/wire counts; neighbor births are internal "
    "None rows; signatures use previous-horizon classes, never raw state. This "
    "is a sufficient-carrier stress test, not the weak/timed minimal quotient",
    e4_ok,
    f"registered states/classes={len(registered_boundaries)}/"
    f"{registered_predictive_counts}; synthetic stress classes="
    f"{synthetic_predictive_counts}; B1 H1-equal/H2-split={b1_horizon_split}; "
    f"q={ftext(q_left)}; next-boundary "
    f"survival(1.375)={survival_left:.40E}",
)


# ---------------------------------------------------------------------------
# E5: physical B3 schema and an updater that never re-reads global state.

def actor_row(state, actor):
    row = state["actors"][actor]
    return (
        row["carrier"], row["ring"], row["births"],
        len(state["neighbors"][actor]), wire_count(state, actor),
    )


def edge_key(a, b):
    return tuple(sorted((a, b)))


def b3_carrier(state, actor="A", elapsed=F(0)):
    root = state["actors"][actor]
    neighbors = {
        x: (len(state["neighbors"][x]), state["actors"][x]["births"])
        for x in state["neighbors"][actor]
    }
    edges = {edge_key(actor, x): edge_key(actor, x) for x in neighbors}
    ports = {
        (actor, edge_key(actor, x)): (actor, x, edge_key(actor, x))
        for x in neighbors
    }
    return {
        "root": actor,
        "elapsed": elapsed,
        "root_row": (
            root["carrier"], root["ring"], root["births"],
            wire_count(state, actor),
        ),
        "neighbors": neighbors,
        "ports": ports,
        "edges": edges,
    }


def b3_key(carrier):
    return (
        carrier["root"], carrier["elapsed"], carrier["root_row"],
        tuple(sorted(carrier["neighbors"].items())),
        tuple(sorted(carrier["ports"].items(), key=repr)),
        tuple(sorted(carrier["edges"].items(), key=repr)),
    )


def b3_event_view(carrier, kind, y, target):
    root = carrier["root"]
    if y == root:
        if kind == "b":
            return ("root-birth",)
        if kind == "n":
            return ("root-idle",)
        if kind == "i":
            return ("root-outgoing", target)
    if y in carrier["neighbors"] and kind == "b":
        return ("neighbor-birth", y)
    if y in carrier["neighbors"] and kind == "i" and target == root:
        return ("incoming", y)
    return None


def b3_update(carrier, delta_t, event_view):
    """Update using only old B3, an elapsed increment and a typed event."""
    out = {
        "root": carrier["root"],
        "elapsed": carrier["elapsed"] + delta_t,
        "root_row": carrier["root_row"],
        "neighbors": dict(carrier["neighbors"]),
        "ports": dict(carrier["ports"]),
        "edges": dict(carrier["edges"]),
    }
    if event_view is None:
        return out
    carrier_bit, rings, births, wire = out["root_row"]
    tag = event_view[0]
    if tag == "root-birth":
        child = f"{out['root']}/{births + 1}"
        edge = edge_key(out["root"], child)
        out["root_row"] = (carrier_bit, rings + 1, births + 1, wire + 1)
        out["neighbors"][child] = (1, 0)
        out["edges"][edge] = edge
        out["ports"][(out["root"], edge)] = (out["root"], child, edge)
    elif tag == "root-idle":
        out["root_row"] = (carrier_bit, rings + 1, births, wire + 1)
    elif tag == "root-outgoing":
        target = event_view[1]
        if target not in out["neighbors"]:
            raise ValueError("outgoing target absent from B3")
        out["root_row"] = (1 - carrier_bit, rings + 1, births, wire + 1)
    elif tag == "neighbor-birth":
        neighbor = event_view[1]
        degree, neighbor_births = out["neighbors"][neighbor]
        out["neighbors"][neighbor] = (degree + 1, neighbor_births + 1)
    elif tag == "incoming":
        neighbor = event_view[1]
        if neighbor not in out["neighbors"]:
            raise ValueError("incoming source absent from B3")
        out["root_row"] = (1 - carrier_bit, rings, births, wire + 1)
    else:
        raise ValueError(event_view)
    return out


def b3_to_b2(carrier):
    c, rings, _births, wire = carrier["root_row"]
    return c, hist_from_degrees(d for d, _ in carrier["neighbors"].values()), rings, wire


def b3_to_labeled(carrier):
    c, rings, births, wire = carrier["root_row"]
    rows = tuple(sorted(
        (name, degree, neighbor_births)
        for name, (degree, neighbor_births) in carrier["neighbors"].items()
    ))
    return c, rings, births, wire, rows


physical_update_checks = 0
physical_update_ok = True
for state_index, state in enumerate(enumerated_states):
    before = b3_carrier(state)
    physical_update_ok &= b3_to_b2(before) == boundary_scoped(state)
    physical_update_ok &= b3_to_labeled(before) == labeled_star_boundary(state)
    for row_index, (kind, y, target, _rate) in enumerate(d34b_rates(state)):
        delta = F(1 + ((state_index + row_index) % 7), 1000)
        view = b3_event_view(before, kind, y, target)
        updated = b3_update(before, delta, view)
        direct = b3_carrier(d34b_step(state, kind, y, target), elapsed=delta)
        physical_update_checks += 1
        physical_update_ok &= b3_key(updated) == b3_key(direct)

# A no-event update advances only elapsed time.  This is the relative-time
# coordinate required by the continuous branch; the next-boundary survival
# law is supplied by the generator in E4.
no_event_probe = b3_update(b3_carrier(seed_state()), F(7, 13), None)
physical_update_ok &= no_event_probe["elapsed"] == F(7, 13)

e5_ok = physical_update_ok and physical_update_checks > 30000
check(
    "E5 PHYSICAL B3 RECURSIVE UPDATER [Fraction-exact]: root-owned row and "
    "ports plus neighbor-owned degree/birth rows update from old B3, elapsed "
    "increment and one typed local/passive/silent event; direct full-state "
    "projection agrees and B3 maps explicitly to B2 and L",
    e5_ok,
    f"row updates={physical_update_checks}; no-event elapsed=7/13",
)


# ---------------------------------------------------------------------------
# E6: relabeling covariance and construction-order covariance are distinct.

def renamed_state(state, mapping):
    out = {
        "actors": {mapping[a]: dict(row) for a, row in state["actors"].items()},
        "neighbors": {
            mapping[a]: {mapping[x] for x in xs}
            for a, xs in state["neighbors"].items()
        },
        "last": {},
        "events": [],
    }
    eid_map = {
        event[0]: f"{mapping[event[2]]}#r{event[0].rsplit('#r', 1)[1]}"
        for event in state["events"]
    }
    for eid, kind, y, target, preds, touched in state["events"]:
        out["events"].append((
            eid_map[eid], kind, mapping[y],
            None if target is None else mapping[target],
            tuple(sorted(eid_map[p] for p in preds)),
            tuple(mapping[x] for x in touched),
        ))
    out["last"] = {mapping[a]: eid_map[eid] for a, eid in state["last"].items()}
    return out


def renamed_b3(carrier, mapping):
    root = mapping[carrier["root"]]
    neighbors = {mapping[a]: row for a, row in carrier["neighbors"].items()}
    edges = {
        edge_key(mapping[a], mapping[b]): edge_key(mapping[a], mapping[b])
        for a, b in carrier["edges"]
    }
    ports = {}
    for (owner, edge), (_owner, peer, _edge) in carrier["ports"].items():
        new_edge = edge_key(mapping[edge[0]], mapping[edge[1]])
        ports[(mapping[owner], new_edge)] = (mapping[owner], mapping[peer], new_edge)
    return {
        "root": root,
        "elapsed": carrier["elapsed"],
        "root_row": carrier["root_row"],
        "neighbors": neighbors,
        "ports": ports,
        "edges": edges,
    }


def mapped_row(row, mapping):
    kind, y, target, rate = row
    return kind, mapping[y], None if target is None else mapping[target], rate


def transport_name(name, mapping):
    if name in mapping:
        return mapping[name]
    # Fresh Ulam children are transported functorially even though they are
    # not present in the pre-event mapping table.
    parents = sorted(mapping, key=len, reverse=True)
    for parent in parents:
        if name.startswith(parent + "/"):
            return mapping[parent] + name[len(parent):]
    raise KeyError(name)


def transport_labeled_boundary(boundary, mapping):
    carrier, rings, births, wire, rows = boundary
    return carrier, rings, births, wire, tuple(sorted(
        (transport_name(name, mapping), degree, neighbor_births)
        for name, degree, neighbor_births in rows
    ))


def transport_role_label(label, mapping):
    if label is None:
        return None
    parts = label.split(":")
    if parts[0] in {"A-birth", "A-outgoing", "incoming"}:
        parts[1] = transport_name(parts[1], mapping)
    return ":".join(parts)


def transport_labeled_rows(rows, mapping):
    out = Counter()
    for (label, after), rate in rows.items():
        out[(
            transport_role_label(label, mapping),
            transport_labeled_boundary(after, mapping),
        )] += rate
    return out


relabel_checks = 0
relabel_ok = True
role_output_checks = 0
role_output_ok = True
for state in enumerated_states:
    names = sorted(state["actors"])
    mapping = {
        name: ("R" if name == "A" else f"X{index}")
        for index, name in enumerate(names)
    }
    renamed_before = renamed_state(state, mapping)
    original_role_rows = global_labeled_rows(state, actor="A")
    renamed_role_rows = global_labeled_rows(renamed_before, actor=mapping["A"])
    transported_role_rows = transport_labeled_rows(original_role_rows, mapping)
    closed_renamed_rows = labeled_formula_rows(
        labeled_star_boundary(renamed_before, actor=mapping["A"]),
        root=mapping["A"],
    )
    role_output_checks += 1
    role_output_ok &= transported_role_rows == renamed_role_rows
    role_output_ok &= closed_renamed_rows == renamed_role_rows
    for row in d34b_rates(state):
        kind, y, target, rate = row
        after = d34b_step(state, kind, y, target)
        mapped = dict(mapping)
        if kind == "b":
            child = f"{y}/{state['actors'][y]['births'] + 1}"
            mapped[child] = f"{mapping[y]}/{state['actors'][y]['births'] + 1}"
        transported_after = renamed_state(after, mapped)
        mapped_kind, mapped_y, mapped_target, mapped_rate = mapped_row(row, mapping)
        stepped_after = d34b_step(
            renamed_before, mapped_kind, mapped_y, mapped_target
        )
        relabel_checks += 1
        relabel_ok &= rate == mapped_rate
        relabel_ok &= state_key(transported_after) == state_key(stepped_after)
        relabel_ok &= b3_key(b3_carrier(transported_after, mapped["A"])) == b3_key(
            renamed_b3(b3_carrier(after), mapped)
        )


def row_write_support(state, row):
    kind, y, target, _rate = row
    support = {y}
    if kind == "i":
        support.add(target)
    elif kind == "b":
        support.add(f"{y}/{state['actors'][y]['births'] + 1}")
    return frozenset(support)


swap_checks = 0
swap_ok = True
for state in enumerated_states:
    rows = d34b_rates(state)
    for left, right in combinations(rows, 2):
        if row_write_support(state, left) & row_write_support(state, right):
            continue
        lk, ly, lt, _ = left
        rk, ry, rt, _ = right
        left_then_right = d34b_step(d34b_step(state, lk, ly, lt), rk, ry, rt)
        right_then_left = d34b_step(d34b_step(state, rk, ry, rt), lk, ly, lt)
        swap_checks += 1
        swap_ok &= state_key(left_then_right) == state_key(right_then_left)
        swap_ok &= b3_key(b3_carrier(left_then_right)) == b3_key(
            b3_carrier(right_then_left)
        )

e6_ok = (
    relabel_ok and role_output_ok and swap_ok
    and relabel_checks > 30000 and role_output_checks == len(enumerated_states)
    and swap_checks > 100000
)
check(
    "E6 TWO COVARIANCE GATES [exact finite regression + disjoint-support "
    "lemma]: nominal actor/Ulam relabeling extends to fresh children and "
    "transports counter-bearing role outputs and fresh children; disjoint "
    "record-DAG updates commute up to that "
    "gauge at the same elapsed-time stop",
    e6_ok,
    f"relabel rows={relabel_checks}; role-output states={role_output_checks}; "
    f"disjoint swaps={swap_checks}",
)


# ---------------------------------------------------------------------------
# E7: typed regional composition with shared edges and owned endpoint ports.

def region_message(state, region):
    region = frozenset(region)
    owned = {actor: actor_row(state, actor) for actor in region}
    refs = {}
    edges = {}
    ports = {}
    for actor in region:
        for neighbor in state["neighbors"][actor]:
            edge = edge_key(actor, neighbor)
            edges[edge] = edge
            ports[(actor, edge)] = (actor, neighbor, edge)
            if neighbor not in region:
                refs[neighbor] = (
                    len(state["neighbors"][neighbor]),
                    state["actors"][neighbor]["births"],
                )
    owned_events = {
        event[0]: event for event in state["events"] if event[2] in region
    }
    event_refs = {
        event[0]: event for event in state["events"]
        if event[2] not in region and set(event[5]) & region
    }
    visible_ids = set(owned_events) | set(event_refs)
    predecessor_refs = {
        predecessor
        for event in (*owned_events.values(), *event_refs.values())
        for predecessor in event[4]
        if predecessor not in visible_ids
    }
    tips = {actor: state["last"].get(actor) for actor in region}
    return {
        "region": region, "owned": owned, "refs": refs,
        "ports": ports, "edges": edges,
        "owned_events": owned_events, "event_refs": event_refs,
        "predecessor_refs": predecessor_refs, "tips": tips,
    }


def message_key(message):
    return (
        tuple(sorted(message["region"])),
        tuple(sorted(message["owned"].items())),
        tuple(sorted(message["refs"].items())),
        tuple(sorted(message["ports"].items(), key=repr)),
        tuple(sorted(message["edges"].items(), key=repr)),
        tuple(sorted(message["owned_events"].items(), key=repr)),
        tuple(sorted(message["event_refs"].items(), key=repr)),
        tuple(sorted(message["predecessor_refs"])),
        tuple(sorted(message["tips"].items())),
    )


def validate_message(message):
    region = set(message["region"])
    if set(message["owned"]) != region or set(message["tips"]) != region:
        raise ValueError("owned actor/tip set differs from region")
    if set(message["refs"]) & region:
        raise ValueError("owned actor also appears as external reference")
    external_peers = set()
    for edge, endpoints in message["edges"].items():
        if edge != endpoints or len(edge) != 2 or not (set(edge) & region):
            raise ValueError("malformed or phantom shared edge")
        for owner in set(edge) & region:
            peer = edge[0] if edge[1] == owner else edge[1]
            port_key = (owner, edge)
            expected_port = (owner, peer, edge)
            if message["ports"].get(port_key) != expected_port:
                raise ValueError("missing or malformed owned endpoint port")
            if peer not in region:
                external_peers.add(peer)
    if set(message["refs"]) != external_peers:
        raise ValueError("external actor rows do not match crossing ports")
    for (owner, edge), (owner2, peer, edge2) in message["ports"].items():
        if owner not in region or owner != owner2 or edge != edge2:
            raise ValueError("phantom or multiply owned endpoint port")
        if message["edges"].get(edge) != edge or set(edge) != {owner, peer}:
            raise ValueError("port/edge endpoint mismatch")
    if set(message["owned_events"]) & set(message["event_refs"]):
        raise ValueError("event both owned and referenced")
    visible_events = {
        **message["event_refs"], **message["owned_events"],
    }
    for eid, event in message["owned_events"].items():
        if eid != event[0] or event[2] not in region:
            raise ValueError("event ownership is not its initiator")
    for eid, event in message["event_refs"].items():
        if eid != event[0] or event[2] in region or not (set(event[5]) & region):
            raise ValueError("invalid crossing event reference")
    expected_pred_refs = {
        predecessor
        for event in visible_events.values()
        for predecessor in event[4]
        if predecessor not in visible_events
    }
    if set(message["predecessor_refs"]) != expected_pred_refs:
        raise ValueError("opaque predecessor reference set mismatch")
    for actor, tip in message["tips"].items():
        if tip is not None and (
                tip not in visible_events or actor not in visible_events[tip][5]):
            raise ValueError("owned wire tip lacks its visible event")
    return True


def compose_messages(left, right):
    validate_message(left)
    validate_message(right)
    if left["region"] & right["region"]:
        raise ValueError("composition receipt uses disjoint owned regions")
    region = left["region"] | right["region"]
    owned = dict(left["owned"])
    owned.update(right["owned"])
    refs = {}
    for source in (left["refs"], right["refs"]):
        for actor, row in source.items():
            if actor in refs and refs[actor] != row:
                raise ValueError("inconsistent duplicate boundary reference")
            refs[actor] = row
    for actor, row in owned.items():
        if actor in refs:
            if refs[actor] != (row[3], row[2]):
                raise ValueError("owned/reference row mismatch")
            del refs[actor]
    ports = dict(left["ports"])
    for key, value in right["ports"].items():
        if key in ports and ports[key] != value:
            raise ValueError("inconsistent duplicate owned port")
        if key in ports:
            raise ValueError("port has more than one owner")
        ports[key] = value
    edges = dict(left["edges"])
    for key, value in right["edges"].items():
        if key in edges and edges[key] != value:
            raise ValueError("inconsistent duplicate shared edge")
        edges[key] = value
    for (owner, edge), (owner2, peer, edge2) in ports.items():
        if owner != owner2 or edge != edge2 or edges.get(edge) != edge:
            raise ValueError("port/edge typing failure")
        if set(edge) != {owner, peer}:
            raise ValueError("port endpoints disagree with shared edge")
    owned_events = dict(left["owned_events"])
    for eid, event in right["owned_events"].items():
        if eid in owned_events:
            raise ValueError("event has duplicate initiator ownership")
        owned_events[eid] = event
    event_refs = {}
    for source in (left["event_refs"], right["event_refs"]):
        for eid, event in source.items():
            if eid in event_refs and event_refs[eid] != event:
                raise ValueError("inconsistent crossing event content")
            event_refs[eid] = event
    for eid, event in owned_events.items():
        if eid in event_refs:
            if event_refs[eid] != event:
                raise ValueError("owned/referenced event content mismatch")
            del event_refs[eid]
    tips = dict(left["tips"])
    for actor, tip in right["tips"].items():
        if actor in tips:
            raise ValueError("wire tip has duplicate owner")
        tips[actor] = tip
    visible_events = {**event_refs, **owned_events}
    predecessor_refs = {
        predecessor
        for event in visible_events.values()
        for predecessor in event[4]
        if predecessor not in visible_events
    }
    out = {
        "region": region,
        "owned": owned,
        "refs": refs,
        "ports": ports,
        "edges": edges,
        "owned_events": owned_events,
        "event_refs": event_refs,
        "predecessor_refs": predecessor_refs,
        "tips": tips,
    }
    validate_message(out)
    return out


composition_checks = 0
composition_ok = True
for state in enumerated_states:
    names = tuple(sorted(state["actors"]))
    # Every disjoint nonempty singleton pair and every singleton/complement
    # pair are registered; the arbitrary-region identity is the same typed-set
    # union theorem and is not inferred statistically from these regressions.
    regions = [
        frozenset(region)
        for size in range(1, len(names))
        for region in combinations(names, size)
    ]
    region_pairs = [
        (left, right)
        for index, left in enumerate(regions)
        for right in regions[index + 1:]
        if left.isdisjoint(right)
    ]
    for left_region, right_region in region_pairs:
        direct = region_message(state, set(left_region) | set(right_region))
        for first_region, second_region in (
                (left_region, right_region), (right_region, left_region)):
            first = region_message(state, first_region)
            second = region_message(state, second_region)
            composed = compose_messages(first, second)
            composition_checks += 1
            composition_ok &= message_key(composed) == message_key(direct)

# Fail closed on malformed messages and inconsistent shared metadata.
corruption_results = []
corrupt_state = seed_state()
left = region_message(corrupt_state, {"A"})
right = region_message(corrupt_state, {"B"})
shared_edge = edge_key("A", "B")
corruptions = []
missing_port = copy.deepcopy(left)
del missing_port["ports"][("A", shared_edge)]
corruptions.append((missing_port, right))
phantom = copy.deepcopy(left)
phantom_edge = edge_key("A", "Z")
phantom["edges"][phantom_edge] = phantom_edge
phantom["ports"][("Z", phantom_edge)] = ("Z", "A", phantom_edge)
corruptions.append((phantom, right))
bad_reference = copy.deepcopy(left)
bad_reference["refs"]["B"] = (99, 99)
corruptions.append((bad_reference, right))
bad_edge = copy.deepcopy(right)
bad_edge["edges"][shared_edge] = ("A", "CORRUPT")
corruptions.append((left, bad_edge))

event_state = d34b_step(seed_state(), "i", "B", "A")
event_left = region_message(event_state, {"A"})
event_right = region_message(event_state, {"B"})
event_id = event_state["events"][-1][0]
bad_event = copy.deepcopy(event_right)
row = list(bad_event["owned_events"][event_id])
row[1] = "n"
bad_event["owned_events"][event_id] = tuple(row)
corruptions.append((event_left, bad_event))
duplicate_event_owner = copy.deepcopy(event_left)
duplicate_event_owner["owned_events"][event_id] = event_left["event_refs"][event_id]
del duplicate_event_owner["event_refs"][event_id]
corruptions.append((duplicate_event_owner, event_right))

for bad_left, bad_right in corruptions:
    rejected = False
    try:
        compose_messages(bad_left, bad_right)
    except ValueError:
        rejected = True
    corruption_results.append(rejected)

corruption_rejected = all(corruption_results) and len(corruption_results) == 6
e7_ok = composition_ok and corruption_rejected and composition_checks > 150000
check(
    "E7 TYPED COMPOSITION / OWNERSHIP [exact + set-union lemma]: actor rows "
    "endpoint ports, persistent events and wire tips have exactly one owner; "
    "shared graph/event references are validated; composition equals direct "
    "regional projection and six malformed-message attacks are rejected",
    e7_ok,
    f"registered region pairs={composition_checks}; corruptions rejected="
    f"{sum(corruption_results)}/{len(corruption_results)}",
)


# ---------------------------------------------------------------------------
# E8: capacity and all-future coarse-carrier theorem hypotheses.

T_width = Decimal(1)
poisson_probs = []
poisson_weights_exact = []
for births in range(21):
    probability = (-(T_width / Decimal(4))).exp()
    probability *= (T_width / Decimal(4)) ** births
    probability /= Decimal(math.factorial(births))
    poisson_probs.append(probability)
    poisson_weights_exact.append(F(1, 4) ** births / math.factorial(births))

poisson_recurrence = all(
    poisson_weights_exact[m + 1] / poisson_weights_exact[m]
    == F(1, 4 * (m + 1))
    for m in range(20)
)
capacity_ledger = {
    "graph radius": 1,
    "actor/reference count": "1+d_A; d_A external rows",
    "owned A-side endpoint ports": "d_A; unbounded support",
    "shared incident edges": "d_A; unbounded support",
    "root carrier bit": "1 bit",
    "neighbor degree bits": "sum_x ceil(log2(degree(x)+1))",
    "neighbor birth-ordinal bits": "sum_x ceil(log2(births(x)+1))",
    "A own/birth/wire counter bits": "sum ceil(log2(counter+1))",
    "nominal identifier bits": "UTF-8 reference receipt; encoding-dependent",
    "port/edge handle bits": "4*d_A*ceil(log2(d_A+1)) in reference table",
    "elapsed time": "one relative continuous coordinate; ideal precision uncalibrated",
    "renewal ages": "absent only for chosen exponential law",
    "bounded alternative/minimality": "OPEN; only this B3 is proved unbounded",
}

capacity_probe_state = max(
    enumerated_states, key=lambda s: len(s["neighbors"]["A"])
)
capacity_probe = b3_carrier(capacity_probe_state)
probe_degree = len(capacity_probe["neighbors"])
probe_degree_bits = sum(
    max(1, degree.bit_length())
    for degree, _births in capacity_probe["neighbors"].values()
)
probe_neighbor_birth_bits = sum(
    max(1, births.bit_length())
    for _degree, births in capacity_probe["neighbors"].values()
)
probe_counter_bits = sum(
    max(1, value.bit_length()) for value in capacity_probe["root_row"][1:]
)
probe_identifier_bits = sum(
    8 * len(name.encode("utf-8"))
    for name in (capacity_probe["root"], *capacity_probe["neighbors"])
)
probe_handle_width = max(1, probe_degree.bit_length())
probe_port_edge_handle_bits = 4 * probe_degree * probe_handle_width
capacity_formulas_ok = (
    len(capacity_probe["ports"]) == probe_degree
    and len(capacity_probe["edges"]) == probe_degree
    and len(capacity_probe["neighbors"]) == probe_degree
    and probe_degree_bits >= probe_degree
    and probe_neighbor_birth_bits >= probe_degree
    and probe_counter_bits >= 3
    and probe_identifier_bits > 0
    and probe_port_edge_handle_bits >= 4 * probe_degree
)

# The analytic theorem is the row partition in note section 6: for arbitrary
# finite D34b state, only A rows and births/interactions of A-neighbors can
# alter (c,h); each contribution depends on (c,h) exactly as printed.  The
# parent D34b nonexplosion theorem supplies uniqueness of the projected marked
# pure-jump law.  The finite regression above is deliberately not the proof.
analytic_partition_hypotheses = (
    projection_matches and labeled_projection_matches
    and counter_rows_integrated
    and all(rate > 0 for boundary in synthetic_boundaries
            for rate in boundary_formula_rows(boundary).values())
    and e5_ok and e6_ok and e7_ok
    and capacity_formulas_ok
    and len(capacity_ledger) == 13
)
e8_ok = (
    analytic_partition_hypotheses
    and all(probability > 0 for probability in poisson_probs)
    and poisson_recurrence
)
check(
    "E8 BRANCH C/L ALL-FUTURE B3 + CAPACITY LEDGER [analytic generator "
    "partition + inherited D34b nonexplosion]: the physical distributed star "
    "screens and updates recursively at relative-time and count stops; this "
    "B3 has unbounded port/identifier/integer width, while a different bounded "
    "physical carrier and minimality remain open",
    e8_ok,
    f"Poisson(T=1,m=20)={poisson_probs[-1]:.32E}; capacity fields="
    f"{len(capacity_ledger)}; probe d/root-bit/degree-bits/neighbor-birth-bits/"
    f"counter-bits/id-bits/port-edge-handle-bits={probe_degree}/1/"
    f"{probe_degree_bits}/{probe_neighbor_birth_bits}/{probe_counter_bits}/"
    f"{probe_identifier_bits}/{probe_port_edge_handle_bits}",
)


# ---------------------------------------------------------------------------
# E9: every complete fixed actor-graph radius loses full durable ancestry.

def actor_distances(state, root):
    distances = {root: 0}
    queue = deque([root])
    while queue:
        actor = queue.popleft()
        for neighbor in state["neighbors"][actor]:
            if neighbor not in distances:
                distances[neighbor] = distances[actor] + 1
                queue.append(neighbor)
    return distances


def complete_radius_carrier(state, root, radius):
    """Complete records owned by actors in a closed actor-graph ball.

    Outside predecessor and actor identifiers remain opaque.  Following them
    recursively would no longer be a radius-r carrier.
    """
    distances = actor_distances(state, root)
    inside = {actor for actor, distance in distances.items() if distance <= radius}
    owned = tuple(sorted(
        (actor,
         tuple(sorted(state["actors"][actor].items())),
         state["last"].get(actor),
         wire_count(state, actor))
        for actor in inside
    ))
    ports = tuple(sorted(
        (actor, neighbor, edge_key(actor, neighbor), neighbor not in inside)
        for actor in inside for neighbor in state["neighbors"][actor]
    ))
    # Every event on an owned wire is complete, including a crossing event.
    # Predecessor ids whose events are not owned are retained opaquely inside
    # the complete event tuple but are not dereferenced.
    owned_events = tuple(sorted(
        (event for event in state["events"] if set(event[5]) & inside),
        key=repr,
    ))
    return tuple(sorted(inside)), owned, ports, owned_events


def event_ancestry(state, final_eid):
    event_map = {event[0]: event for event in state["events"]}
    seen = set()
    stack = [final_eid]
    while stack:
        eid = stack.pop()
        if eid in seen:
            continue
        seen.add(eid)
        stack.extend(event_map[eid][4])
    return tuple(sorted((event_map[eid] for eid in seen), key=repr))


def branch_f_event(state, path, pre_stop_ordinal):
    """Inspect one endpoint event fixed at the conditioning stop.

    The selector is the structural remote role path[-1] plus its wire ordinal;
    it never follows the remote actor's later moving tip.
    """
    ancestry = event_ancestry(state, state["last"][path[0]])
    event_map = {event[0]: event for event in ancestry}
    selected_id = f"{path[-1]}#r{pre_stop_ordinal}"
    selected = event_map.get(selected_id)
    inward_chain_present = all(
        any(
            event[1] == "i" and event[2] == path[index]
            and event[3] == path[index - 1]
            for event in ancestry
        )
        for index in range(1, len(path))
    )
    return (
        inward_chain_present and selected is not None
        and selected[2] == path[-1] and selected[1] == "n"
    )


def propagate_inward(state, path):
    out = state
    mass = F(1)
    for index in range(len(path) - 1, 0, -1):
        child = path[index]
        parent = path[index - 1]
        mass *= event_rate(out, "i", child, parent) / len(active_actors(out))
        out = d34b_step(out, "i", child, parent)
    return out, mass


def grow_chain_branch(radius):
    state = seed_state()
    history_mass = F(1)
    path = ["A", "B"]
    while len(path) - 1 < radius + 1:
        parent = path[-1]
        before = set(state["actors"])
        state, p = embedded_step(state, "b", parent)
        history_mass *= p
        child = next(iter(set(state["actors"]) - before))
        path.append(child)
    distant = path[-1]
    before = set(state["actors"])
    state, p = embedded_step(state, "b", distant)
    history_mass *= p
    leaf = next(iter(set(state["actors"]) - before))

    idle_branch, p_idle = embedded_step(state, "n", distant)
    interact_branch, p_interact = embedded_step(state, "i", distant, leaf)
    idle_mass = history_mass * p_idle
    interact_mass = history_mass * p_interact
    idle_branch_eid = idle_branch["last"][distant]
    interact_branch_eid = interact_branch["last"][distant]
    pre_stop_ordinal = idle_branch["actors"][distant]["ring"]
    if pre_stop_ordinal != interact_branch["actors"][distant]["ring"]:
        raise AssertionError("paired endpoint ordinals differ")

    idle_carrier = complete_radius_carrier(idle_branch, "A", radius)
    interact_carrier = complete_radius_carrier(interact_branch, "A", radius)
    if idle_carrier != interact_carrier:
        raise AssertionError("complete branch carrier leaked outside record")
    if idle_branch_eid != interact_branch_eid:
        raise AssertionError("paired branches must share nominal endpoint role")

    if complete_radius_carrier(idle_branch, "A", radius) != complete_radius_carrier(
            interact_branch, "A", radius):
        raise AssertionError("branch leaked inside registered radius")

    idle_future, future_mass = propagate_inward(idle_branch, path)
    interact_future, other_future_mass = propagate_inward(interact_branch, path)
    if future_mass != other_future_mass:
        raise AssertionError("paired propagation masses differ")

    final_idle = idle_future["last"]["A"]
    final_interact = interact_future["last"]["A"]
    ancestry_idle = event_ancestry(idle_future, final_idle)
    ancestry_interact = event_ancestry(interact_future, final_interact)
    record_idle = next(event for event in ancestry_idle if event[0] == idle_branch_eid)
    record_interact = next(
        event for event in ancestry_interact if event[0] == interact_branch_eid
    )
    expected_mass = F(1, 8 * (radius + 3)) ** (radius + 1)

    # Optional timed subcylinder lower bound for Delta=1.  During this exact
    # path there are m=r+3 component clocks and no births; the first r+1 rings
    # complete with an Erlang(shape=r+1, rate=m) factor.
    m = Decimal(radius + 3)
    shape = radius + 1
    erlang_cdf = Decimal(1) - (-m).exp() * sum(
        (m ** j) / Decimal(math.factorial(j)) for j in range(shape)
    )
    timed_lower = dfrac(expected_mass) * erlang_cdf

    query_idle = branch_f_event(idle_future, path, pre_stop_ordinal)
    query_interact = branch_f_event(interact_future, path, pre_stop_ordinal)

    # Hostile moving-tip battery.  Later endpoint/unrelated events may alter
    # the immediate tip but cannot change the selected pre-stop ordinal.
    interloper_sequences = (
        (("n", distant, None),),
        (("i", distant, leaf),),
        (("n", "A", None),),
        (("n", distant, None), ("i", distant, leaf),
         ("n", distant, None), ("n", distant, None)),
    )
    interloper_results = []
    selected_interact_record = next(
        event for event in interact_branch["events"]
        if event[0] == interact_branch_eid
    )
    selected_record_immutable = True
    for sequence in interloper_sequences:
        idle_interposed = idle_branch
        interact_interposed = interact_branch
        for kind, initiator, target in sequence:
            idle_interposed = d34b_step(idle_interposed, kind, initiator, target)
            interact_interposed = d34b_step(
                interact_interposed, kind, initiator, target
            )
        idle_interposed, _ = propagate_inward(idle_interposed, path)
        interact_interposed, _ = propagate_inward(interact_interposed, path)
        interloper_results.append((
            branch_f_event(idle_interposed, path, pre_stop_ordinal),
            branch_f_event(interact_interposed, path, pre_stop_ordinal),
        ))
        current_selected = next(
            event for event in interact_interposed["events"]
            if event[0] == interact_branch_eid
        )
        selected_record_immutable &= current_selected == selected_interact_record

    # Gauge regression: transport the final graph and structural path together.
    mapping = {
        actor: ("R" if actor == "A" else f"Y{index}")
        for index, actor in enumerate(sorted(idle_future["actors"]))
    }
    query_gauge = branch_f_event(
        renamed_state(idle_future, mapping), [mapping[a] for a in path],
        pre_stop_ordinal,
    ) == query_idle

    return {
        "radius": radius,
        "complete_carrier_equal": idle_carrier == interact_carrier,
        "idle_past_mass": idle_mass,
        "interact_past_mass": interact_mass,
        "embedded_lower": future_mass,
        "expected_mass": expected_mass,
        "timed_lower_Delta1": timed_lower,
        "idle_kind": record_idle[1],
        "interact_kind": record_interact[1],
        "query_idle": query_idle,
        "query_interact": query_interact,
        "selector_same": (
            idle_branch_eid == interact_branch_eid
            == f"{distant}#r{pre_stop_ordinal}"
        ),
        "immutable_zero": (
            record_interact[1] == "i" and selected_record_immutable
            and all(idle_value and not interact_value
                    for idle_value, interact_value in interloper_results)
        ),
        "interloper_checks": len(interloper_results),
        "query_gauge": query_gauge,
        "ancestry_distinct": ancestry_idle != ancestry_interact,
    }


radius_witnesses = tuple(grow_chain_branch(radius) for radius in range(4))
e9_ok = all(
    row["complete_carrier_equal"]
    and row["idle_past_mass"] > 0
    and row["interact_past_mass"] > 0
    and row["embedded_lower"] == row["expected_mass"] > 0
    and row["timed_lower_Delta1"] > 0
    and row["idle_kind"] == "n"
    and row["interact_kind"] == "i"
    and row["query_idle"]
    and not row["query_interact"]
    and row["selector_same"]
    and row["immutable_zero"]
    and row["interloper_checks"] == 4
    and row["query_gauge"]
    and row["ancestry_distinct"]
    for row in radius_witnesses
)
check(
    "E9 BRANCH F COMPLETE-RADIUS NO-GO [Fraction-exact specimens + all-r "
    "analytic chain]: complete C_r carriers agree; one common structural, "
    "gauge-invariant future event pins the pre-stop remote wire ordinal; its "
    "idle-branch probability is at least p_r>0 and its interaction-branch "
    "probability remains zero through moving-tip interlopers by immutability",
    e9_ok,
    "embedded lower bounds=" + ",".join(
        f"r{row['radius']}:{ftext(row['embedded_lower'])}"
        for row in radius_witnesses
    ) + "; timed Delta=1 minima=" + ",".join(
        f"{row['timed_lower_Delta1']:.6E}" for row in radius_witnesses
    ),
)


# ---------------------------------------------------------------------------
# E10: disconnected control and exact component ceiling.

def a_local_rows(state):
    return tuple(
        (kind, y, target, rate)
        for kind, y, target, rate in d34b_rates(state)
        if y == "A" or (kind == "i" and target == "A")
    )


remote_rows_equal = a_local_rows(seed_state()) == a_local_rows(seed_state(remote=True))
component_of_a = set(actor_distances(seed_state(remote=True), "A"))
remote_disjoint = component_of_a == {"A", "B"}


def component_restriction(state, root="A"):
    component = set(actor_distances(state, root))
    actors = tuple(sorted(
        (a, tuple(sorted(state["actors"][a].items()))) for a in component
    ))
    neighbors = tuple(sorted(
        (a, tuple(sorted(state["neighbors"][a] & component))) for a in component
    ))
    events = tuple(sorted(
        (event for event in state["events"] if event[2] in component), key=repr
    ))
    last = tuple(sorted(
        (a, state["last"].get(a)) for a in component
    ))
    return actors, neighbors, events, last


def component_path(state, operations, root="A"):
    out = state
    mass = F(1)
    for kind, y, target in operations:
        component_size = len(actor_distances(out, root))
        mass *= event_rate(out, kind, y, target) / component_size
        out = d34b_step(out, kind, y, target)
    return out, mass


component_operations = (
    ("b", "A", None),
    ("b", "B", None),
    ("i", "B", "A"),
    ("n", "A", None),
)
component_plain, component_mass_plain = component_path(
    seed_state(), component_operations
)
component_remote, component_mass_remote = component_path(
    seed_state(remote=True), component_operations
)
multistep_remote_invariant = (
    component_mass_plain == component_mass_remote
    and component_restriction(component_plain)
    == component_restriction(component_remote)
)

# Exact hypotheses of the pinned D34b product theorem: actor clock rows sum to
# one; every birth stays in the initiator's component, every interaction uses
# an existing edge, and idle joins nothing.  Thus disconnected factors remain
# independent at continuous construction time and component-local stops.
no_component_joining = all(
    kind != "i" or target in state["neighbors"][y]
    for state in enumerated_states
    for kind, y, target, _rate in d34b_rates(state)
)
unique_event_ownership = all(
    len({event[0] for event in state["events"]}) == len(state["events"])
    and all(event[2] in event[5] for event in state["events"])
    for state in enumerated_states
)
component_upper_bound_fields = (
    "actors/counters/carriers",
    "typed adjacency/eligibility",
    "wire tips",
    "persistent event records",
)
component_carrier_gates = {
    "screening": no_component_joining and law_rows_normalized,
    "recursive closure": no_component_joining,
    "covariance": e6_ok,
    "typed composition": e7_ok and unique_event_ownership,
    "capacity bounded": False,
    "whole component necessary": False,
}
e10_ok = (
    remote_rows_equal and remote_disjoint and multistep_remote_invariant
    and all(component_carrier_gates[key] for key in (
        "screening", "recursive closure", "covariance", "typed composition"
    ))
    and not component_carrier_gates["capacity bounded"]
    and not component_carrier_gates["whole component necessary"]
    and len(component_upper_bound_fields) == 4
)
check(
    "E10 WHOLE-COMPONENT SUFFICIENT GROWING UPPER BOUND / DISCONNECTED "
    "CONTROL [exact regression + pinned product theorem]: no law row joins "
    "components; adding P--Q leaves the A-component continuous/local-stop law "
    "and a multi-step component cylinder invariant; necessity is not claimed",
    e10_ok,
    f"A component={sorted(component_of_a)}; path mass="
    f"{ftext(component_mass_plain)}; upper-bound fields="
    f"{len(component_upper_bound_fields)}",
)


# ---------------------------------------------------------------------------
# E11: finite labeled-prefix map and the profinite ceiling.

def transitive_relations(events):
    index = {event[0]: i for i, event in enumerate(events)}
    ancestors = [set() for _ in events]
    for i, event in enumerate(events):
        for predecessor in event[4]:
            j = index[predecessor]
            ancestors[i].add(j)
            ancestors[i].update(ancestors[j])
    return {(j, i) for i, row in enumerate(ancestors) for j in row}


def unmarked_poset_key(events):
    n = len(events)
    relations = transitive_relations(events)
    encodings = []
    for order in permutations(range(n)):
        bits = tuple(
            1 if (order[i], order[j]) in relations else 0
            for i in range(n) for j in range(n)
        )
        encodings.append(bits)
    return n, min(encodings) if encodings else ()


def enumerate_paths(depth):
    paths = [(seed_state(), F(1))]
    for _ in range(depth):
        nxt = []
        for state, probability in paths:
            k = len(active_actors(state))
            for kind, y, target, rate in d34b_rates(state):
                nxt.append((
                    d34b_step(state, kind, y, target),
                    probability * rate / k,
                ))
        paths = nxt
    return paths


paths3 = enumerate_paths(3)
paths4 = enumerate_paths(4)
push3 = defaultdict(F)
push4_to3 = defaultdict(F)
push4 = defaultdict(F)
for state, probability in paths3:
    push3[unmarked_poset_key(state["events"])] += probability
for state, probability in paths4:
    push4[unmarked_poset_key(state["events"])] += probability
    push4_to3[unmarked_poset_key(state["events"][:3])] += probability

finite_pushforward_ok = (
    sum(push3.values(), F(0)) == 1
    and sum(push4.values(), F(0)) == 1
    and dict(push4_to3) == dict(push3)
)
finite_dag_integrity = all(
    all(
        set(event[4]) <= {prior[0] for prior in state["events"][:index]}
        for index, event in enumerate(state["events"])
    )
    and all(i != j for i, j in transitive_relations(state["events"]))
    for state in enumerated_states
)

# Finite warning only: one idle and one interaction both forget to the one-point
# order, yet retain different A carrier marks and give different carrier output
# after the same next A-idle.  This does not assert equality of their posterior
# measures on the completed v9 spectrum.
one_idle = d34b_step(seed_state(), "n", "A")
one_interact = d34b_step(seed_state(), "i", "A", "B")
finite_shadow_equal = (
    unmarked_poset_key(one_idle["events"])
    == unmarked_poset_key(one_interact["events"])
)
marked_output_differs = (
    d34b_step(one_idle, "n", "A")["actors"]["A"]["carrier"]
    != d34b_step(one_interact, "n", "A")["actors"]["A"]["carrier"]
)

e11_ok = (
    finite_pushforward_ok
    and finite_dag_integrity
    and finite_shadow_equal
    and marked_output_differs
)
check(
    "E11 FINITE LABELED-TRUNCATION/UNMARKED PUSHFORWARD + STEM CEILING "
    "[exact]: (u3 o r4->3)_* mu4=(u3)_* mu3 pathwise before marks are "
    "forgotten; there is no asserted unmarked 4->3 restriction; a one-point "
    "shadow does not determine marked output and no v9 posterior theorem is "
    "claimed",
    e11_ok,
    f"path counts d3/d4={len(paths3)}/{len(paths4)}; unmarked classes="
    f"{len(push3)}/{len(push4)}",
)


# ---------------------------------------------------------------------------
# E12: quantum/process branch refusal is a typed dependency result.

accepted_d34c_output = Path(__file__).resolve().parents[1] / "data" / (
    "d34c_nse_quantum_history_exact.out"
)
accepted_d34c_sha = (
    hashlib.sha256(accepted_d34c_output.read_bytes()).hexdigest()
    if accepted_d34c_output.exists() else None
)
controlled_process_input = None
instrument_kernel_input = None
quantum_inputs = {
    "finite D34c strongly-positive typed-DAG family": (
        accepted_d34c_sha
        == "9ce73a693b41f765eff163749ef769ca0cb4ce856ead66d690a63a20331a731a"
    ),
    "auxiliary P,E causal-break negative control": True,
    "timed controlled D34b-D34c process family": controlled_process_input,
    "licensed all-instrument kernels P(r|I,h)": instrument_kernel_input,
}
quantum_refusal = (
    quantum_inputs["finite D34c strongly-positive typed-DAG family"]
    and quantum_inputs["auxiliary P,E causal-break negative control"]
    and quantum_inputs["timed controlled D34b-D34c process family"] is None
    and quantum_inputs["licensed all-instrument kernels P(r|I,h)"] is None
)
assigned_quantum_widths = ()
e12_ok = quantum_refusal and assigned_quantum_widths == ()
check(
    "E12 INTRINSIC QUANTUM D34e BRANCH — REFUSAL/UNDEFINED [pinned typed "
    "dependency]: accepted finite D34c output is hash-verified, but no timed "
    "controlled D34b-D34c process or all-instrument kernels are supplied; no "
    "SHARD d_carrier, d_op or chi_cut is assigned",
    e12_ok,
    f"D34c output SHA={accepted_d34c_sha}; missing controlled process and "
    "instrument kernels; widths=unassigned",
)


# ---------------------------------------------------------------------------
# E13: executable first-applicable branch verdicts and claim ceiling.

OUTCOMES = (
    "REFUSAL/UNDEFINED",
    "ALL-FUTURE BOUNDED-CARRIER PASS",
    "ALL-FUTURE GROWING-CARRIER PASS",
    "WHOLE-COMPONENT ONLY",
    "GLOBAL ONLY",
    "NO EXACT REALIZATION IN THE DECLARED CARRIER CLASS",
    "CANDIDATE-CLASS OBSTRUCTION",
    "FINITE-DOMAIN ONLY",
)
CAPACITY_BOUNDED = "BOUNDED_PROVED"
CAPACITY_UNBOUNDED = "UNBOUNDED_PROVED"
CAPACITY_UNKNOWN = "UNKNOWN"


def decide_branch(branch):
    """Paper-21 section-10.8, in frozen first-applicable order."""
    core = all(branch[key] for key in (
        "screening", "closure", "covariance", "composition"
    ))
    capacity_missing_for_pass = (
        core and branch["capacity_status"] == CAPACITY_UNKNOWN
    )
    # Each row predicate is independent.  Selection, not predicate mutation,
    # implements Paper 21's first-applicable priority.
    raw = (
        not branch["required_inputs"] or capacity_missing_for_pass,
        core and branch["capacity_status"] == CAPACITY_BOUNDED,
        core and branch["capacity_status"] == CAPACITY_UNBOUNDED,
        branch["whole_necessary"],
        branch["global_necessary"],
        branch["universal_exclusion"],
        branch["candidate_obstruction"],
        branch["finite_domain"],
    )
    selected_index = next((index for index, value in enumerate(raw) if value), None)
    if selected_index is None:
        raise AssertionError(f"no Paper-21 outcome for {branch['scope']}")
    # The emitted row is one-hot even when several independent later
    # predicates are true; collision tests below exercise that priority.
    one_hot = tuple(index == selected_index for index in range(len(OUTCOMES)))
    if sum(one_hot) != 1 or any(raw[index] for index in range(selected_index)):
        raise AssertionError("first-applicable outcome failure")
    return OUTCOMES[selected_index], raw, one_hot


def branch(scope, **flags):
    base = {
        "scope": scope,
        "required_inputs": True,
        "screening": False,
        "closure": False,
        "covariance": False,
        "composition": False,
        "capacity_status": CAPACITY_UNKNOWN,
        "whole_necessary": False,
        "global_necessary": False,
        "universal_exclusion": False,
        "candidate_obstruction": False,
        "finite_domain": False,
        "nse": "not applicable: no physical deletion/compression",
    }
    base.update(flags)
    return base


branches = {
    "C coarse A-wire / B3": branch(
        "(mu_D34b,A,Q_C,passive,S_elapsed/count,C_B3)",
        screening=e8_ok, closure=e5_ok, covariance=e6_ok,
        composition=e7_ok, capacity_status=CAPACITY_UNBOUNDED,
    ),
    "L role-labeled A-wire / B3": branch(
        "(mu_D34b,A,Q_L,passive,S_elapsed/count,C_B3)",
        screening=e8_ok, closure=e5_ok, covariance=e6_ok,
        composition=e7_ok, capacity_status=CAPACITY_UNBOUNDED,
    ),
    "F full ancestry / complete radius family": branch(
        "(mu_D34b,A,Q_F,passive,S_A-wire,{C_r:r finite})",
        universal_exclusion=e9_ok,
    ),
    "F full ancestry / whole component": branch(
        "(mu_D34b,A,Q_F,passive,S_continuous/local,C_component)",
        screening=e10_ok, closure=e10_ok, covariance=e6_ok,
        composition=component_carrier_gates["typed composition"],
        capacity_status=CAPACITY_UNBOUNDED,
    ),
    "v9 stem posterior factor": branch(
        "(mu_D34b,A,Q_C/L/F,passive,S_online,C_Xstem-posterior)",
        required_inputs=False, finite_domain=e11_ok,
    ),
    "intrinsic quantum": branch(
        "(mu_controlled,A,Q_instruments,I,S,C_quantum)",
        required_inputs=False,
    ),
}
branch_decisions = {name: decide_branch(value) for name, value in branches.items()}
branch_verdicts = {name: result[0] for name, result in branch_decisions.items()}

# Exercise every row of the decision machine, independently of the scientific
# branches, so a hard-coded verdict dictionary cannot pass this gate.
decision_unit_cases = (
    (branch("row1", required_inputs=False), OUTCOMES[0]),
    (branch("row2", screening=True, closure=True, covariance=True,
            composition=True, capacity_status=CAPACITY_BOUNDED), OUTCOMES[1]),
    (branch("row3", screening=True, closure=True, covariance=True,
            composition=True, capacity_status=CAPACITY_UNBOUNDED), OUTCOMES[2]),
    (branch("row4", whole_necessary=True), OUTCOMES[3]),
    (branch("row5", global_necessary=True), OUTCOMES[4]),
    (branch("row6", universal_exclusion=True), OUTCOMES[5]),
    (branch("row7", candidate_obstruction=True), OUTCOMES[6]),
    (branch("row8", finite_domain=True), OUTCOMES[7]),
)
decision_collision_cases = (
    (branch("row1-over-row8", required_inputs=False, finite_domain=True),
     OUTCOMES[0]),
    (branch("row2-over-row4", screening=True, closure=True, covariance=True,
            composition=True, capacity_status=CAPACITY_BOUNDED,
            whole_necessary=True), OUTCOMES[1]),
    (branch("row3-over-row7", screening=True, closure=True, covariance=True,
            composition=True, capacity_status=CAPACITY_UNBOUNDED,
            candidate_obstruction=True), OUTCOMES[2]),
    (branch("row4-over-row5", whole_necessary=True, global_necessary=True),
     OUTCOMES[3]),
    (branch("row6-over-row7", universal_exclusion=True,
            candidate_obstruction=True), OUTCOMES[5]),
    (branch("capacity-unknown-refuses", screening=True, closure=True,
            covariance=True, composition=True,
            capacity_status=CAPACITY_UNKNOWN), OUTCOMES[0]),
)
decision_machine_ok = all(
    decide_branch(specimen)[0] == expected
    for specimen, expected in (*decision_unit_cases, *decision_collision_cases)
)

expected_verdicts = {
    "C coarse A-wire / B3": OUTCOMES[2],
    "L role-labeled A-wire / B3": OUTCOMES[2],
    "F full ancestry / complete radius family": OUTCOMES[5],
    "F full ancestry / whole component": OUTCOMES[2],
    "v9 stem posterior factor": OUTCOMES[0],
    "intrinsic quantum": OUTCOMES[0],
}
e13_ok = (
    PASS == 12 and FAIL == 0
    and decision_machine_ok
    and branch_verdicts == expected_verdicts
    and all(sum(result[2]) == 1 for result in branch_decisions.values())
)
check(
    "E13 EXECUTABLE FIRST-APPLICABLE SCORECARD: every branch carries its "
    "(mu,A,Q,I,S,C), all eight Paper-21 rows and six predicate collisions are "
    "tested in priority order, and bounded/unbounded/unknown capacity is typed; "
    "B4 is sufficient/growing but not "
    "necessary, while complete finite-radius C_r is universally excluded",
    e13_ok,
    "; ".join(f"{name}={verdict}" for name, verdict in branch_verdicts.items()),
)


summary = (
    f"gates={PASS}/{PASS + FAIL}; levels={','.join(map(str, level_counts))}; "
    f"states={len(enumerated_states)}; collisions={lumpability_collisions}; "
    f"rate_gap={ftext(derivative_gap)}; "
    f"strong_classes={','.join(map(str, registered_predictive_counts))}; "
    f"synthetic={','.join(map(str, synthetic_predictive_counts))}; "
    f"b3_updates={physical_update_checks}; swaps={swap_checks}; "
    f"composition={composition_checks}; corruptions={sum(corruption_results)}/"
    f"{len(corruption_results)}; "
    f"radius_lower={','.join(ftext(row['embedded_lower']) for row in radius_witnesses)}; "
    f"interlopers={sum(row['interloper_checks'] for row in radius_witnesses)}; "
    f"prefix_classes={len(push3)},{len(push4)}; quantum=REFUSAL"
)
digest = hashlib.sha256(summary.encode("utf-8")).hexdigest()
print(f"[SUMMARY] {summary}")
print(f"[RECEIPT-SHA256] {digest}")
print(f"[VERDICT] {'PASS' if FAIL == 0 else 'FAIL'} — {PASS}/{PASS + FAIL}")
sys.exit(1 if FAIL else 0)
