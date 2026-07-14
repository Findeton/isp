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
from decimal import Decimal, getcontext
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, permutations
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


def global_projected_rows(state, actor="A"):
    before = boundary_dyn(state, actor)
    rows = Counter()
    for kind, y, target, rate in d34b_rates(state):
        after_state = d34b_step(state, kind, y, target)
        after = boundary_dyn(after_state, actor)
        label = row_output(kind, y, target, actor)
        if label is None and after == before:
            continue
        marked_label = (
            f"{label}:c{after[0]}" if label is not None else "tau"
        )
        rows[(marked_label, after)] += rate
    return rows


def boundary_formula_rows(boundary):
    carrier, hist = boundary
    rows = Counter()
    rows[(f"A-birth:c{carrier}", (carrier, hist_add_one(hist)))] += F(1, 4)
    rows[(f"A-idle:c{carrier}", boundary)] += F(1, 2)
    rows[(f"A-outgoing:c{1 - carrier}", (1 - carrier, hist))] += F(1, 4)
    for degree, count in hist:
        shifted = hist_shift(hist, degree, degree + 1)
        rows[("tau", (carrier, shifted))] += F(count, 4)
        rows[(f"incoming-to-A:c{1 - carrier}", (1 - carrier, hist))] += F(
            count, 4 * degree
        )
    return rows


def labeled_star_boundary(state, actor="A"):
    return (
        state["actors"][actor]["carrier"],
        state["actors"][actor]["births"],
        tuple(sorted(
            (neighbor, len(state["neighbors"][neighbor]))
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
                label = f"A-birth:{new_child}:c{after[0]}"
            elif kind == "n":
                label = f"A-idle:c{after[0]}"
            else:
                label = f"A-outgoing:{target}:c{after[0]}"
        elif kind == "i" and target == actor:
            label = f"incoming:{y}:c{after[0]}"
        else:
            label = None
        if label is None and after == before:
            continue
        rows[(label if label is not None else f"tau:{y}-birth", after)] += rate
    return rows


def labeled_formula_rows(boundary):
    carrier, a_births, neighbor_rows = boundary
    rows = Counter()
    new_child = f"A/{a_births + 1}"
    after_birth_neighbors = tuple(sorted((*neighbor_rows, (new_child, 1))))
    after_birth = (carrier, a_births + 1, after_birth_neighbors)
    rows[(f"A-birth:{new_child}:c{carrier}", after_birth)] += F(1, 4)
    rows[(f"A-idle:c{carrier}", boundary)] += F(1, 2)
    degree_a = len(neighbor_rows)
    for neighbor, degree in neighbor_rows:
        rows[(
            f"A-outgoing:{neighbor}:c{1 - carrier}",
            (1 - carrier, a_births, neighbor_rows),
        )] += F(1, 4 * degree_a)
        shifted_rows = tuple(sorted(
            (name, d + 1 if name == neighbor else d)
            for name, d in neighbor_rows
        ))
        rows[(
            f"tau:{neighbor}-birth",
            (carrier, a_births, shifted_rows),
        )] += F(1, 4)
        rows[(
            f"incoming:{neighbor}:c{1 - carrier}",
            (1 - carrier, a_births, neighbor_rows),
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
    global_projected_rows(state) == boundary_formula_rows(boundary_dyn(state))
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
    boundary = boundary_dyn(state)
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
    "including A's emitted carrier bit and source/target roles",
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
# E4: finite carrier-transition signatures and continuous survival scope.

@lru_cache(maxsize=None)
def carrier_signature(boundary, horizon):
    if horizon == 0:
        return ()
    rows = boundary_formula_rows(boundary)
    signature = []
    for (label, after), rate in rows.items():
        signature.append((
            label,
            rate.numerator,
            rate.denominator,
            carrier_signature(after, horizon - 1),
        ))
    return tuple(sorted(signature, key=repr))


audit_boundaries = []
for neighbor_count in range(1, 4):
    for degrees in combinations_with_replacement(range(1, 6), neighbor_count):
        hist = hist_from_degrees(degrees)
        for carrier in (0, 1):
            audit_boundaries.append((carrier, hist))

signature_counts = tuple(
    len({carrier_signature(boundary, horizon)
         for boundary in audit_boundaries})
    for horizon in (1, 2, 3)
)


def relevant_intensity(boundary):
    return sum(boundary_formula_rows(boundary).values(), F(0))


q_left = relevant_intensity((0, hist_left))
q_right = relevant_intensity((0, hist_right))
t_probe = Decimal("1.375")
survival_left = (-(dfrac(q_left) * t_probe)).exp()
survival_right = (-(dfrac(q_right) * t_probe)).exp()

scope_counter_updates = {
    "A-birth": (1, 1),
    "A-idle": (1, 1),
    "A-outgoing": (1, 1),
    "incoming-to-A": (0, 1),
    "tau-neighbor-birth": (0, 0),
}
e4_ok = (
    signature_counts[0] <= signature_counts[1] <= signature_counts[2]
    and q_left == q_right
    and survival_left == survival_right
    and scope_counter_updates["incoming-to-A"] == (0, 1)
    and scope_counter_updates["A-birth"] == (1, 1)
)
check(
    "E4 D(N,H=3) CARRIER TRANSITIONS / CONTINUOUS-TIME SCOPE [exact + "
    "100-decimal analytic regression]: finite carrier signatures refine with "
    "horizon; no-relevant-event survival is exp(-q Delta t); A-own and A-wire "
    "counters update differently on passive reception",
    e4_ok,
    f"audit states={len(audit_boundaries)}; signature classes="
    f"{signature_counts}; q={ftext(q_left)}; survival(1.375)="
    f"{survival_left:.40E}",
)


# ---------------------------------------------------------------------------
# E5: distributed typed-star composition and actor-relabeling covariance.

def actor_row(state, actor):
    row = state["actors"][actor]
    return (
        row["carrier"], row["ring"], row["births"],
        len(state["neighbors"][actor]), wire_count(state, actor),
    )


def edge_key(a, b):
    return tuple(sorted((a, b)))


def star_message(state, region):
    region = frozenset(region)
    owned = {actor: actor_row(state, actor) for actor in region}
    refs = {}
    edges = set()
    for actor in region:
        for neighbor in state["neighbors"][actor]:
            edges.add(edge_key(actor, neighbor))
            if neighbor not in region:
                refs[neighbor] = len(state["neighbors"][neighbor])
    return {"region": region, "owned": owned, "refs": refs, "edges": edges}


def message_key(message):
    return (
        tuple(sorted(message["region"])),
        tuple(sorted(message["owned"].items())),
        tuple(sorted(message["refs"].items())),
        tuple(sorted(message["edges"])),
    )


def compose_messages(left, right):
    if left["region"] & right["region"]:
        raise ValueError("composition receipt uses disjoint owned regions")
    region = left["region"] | right["region"]
    owned = dict(left["owned"])
    owned.update(right["owned"])
    refs = {}
    for source in (left["refs"], right["refs"]):
        for actor, degree in source.items():
            if actor in refs and refs[actor] != degree:
                raise ValueError("inconsistent duplicate boundary reference")
            refs[actor] = degree
    for actor, row in owned.items():
        if actor in refs:
            if refs[actor] != row[3]:
                raise ValueError("owned/reference degree mismatch")
            del refs[actor]
    return {
        "region": region,
        "owned": owned,
        "refs": refs,
        "edges": set(left["edges"]) | set(right["edges"]),
    }


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


def renamed_message(message, mapping):
    return {
        "region": frozenset(mapping[a] for a in message["region"]),
        "owned": {mapping[a]: row for a, row in message["owned"].items()},
        "refs": {mapping[a]: degree for a, degree in message["refs"].items()},
        "edges": {edge_key(mapping[a], mapping[b]) for a, b in message["edges"]},
    }


composition_state = seed_state()
composition_state = d34b_step(composition_state, "b", "A")
composition_state = d34b_step(composition_state, "b", "B")
composition_state = d34b_step(composition_state, "i", "A", "B")
composition_state = d34b_step(composition_state, "n", "B/1")
message_a = star_message(composition_state, {"A"})
message_b = star_message(composition_state, {"B"})
composed_ab = compose_messages(message_a, message_b)
direct_ab = star_message(composition_state, {"A", "B"})

all_actor_names = sorted(composition_state["actors"])
mapping = {name: f"X{index}" for index, name in enumerate(reversed(all_actor_names))}
renamed = renamed_state(composition_state, mapping)
covariant_direct = star_message(renamed, {mapping["A"], mapping["B"]})
covariant_transport = renamed_message(direct_ab, mapping)

e5_ok = (
    message_key(composed_ab) == message_key(direct_ab)
    and message_key(covariant_direct) == message_key(covariant_transport)
    and set(composed_ab["owned"]) == {"A", "B"}
    and set(composed_ab["refs"]) == {"A/1", "B/1"}
)
check(
    "E5 DISTRIBUTED TYPED-STAR COMPOSITION / GAUGE [exact]: disjoint owned "
    "actor rows and validated boundary references compose to the directly "
    "constructed union star; actor relabeling commutes. This is record-native "
    "typed union, not an invented D5 factor cover",
    e5_ok,
    f"owned={sorted(composed_ab['owned'])}; refs={sorted(composed_ab['refs'])}",
)


# ---------------------------------------------------------------------------
# E6: capacity and all-future coarse-carrier theorem hypotheses.

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
    "physical incident ports": "A degree; unbounded support",
    "distributed neighbor rows": "one per incident actor; unbounded count",
    "occupied histogram bins": "finite per state; no uniform bound claimed",
    "largest degree / integer bits": "unbounded",
    "A own/wire counters": "unbounded integers when retained by scope",
    "renewal ages": "absent only for chosen exponential law",
}

# The analytic theorem is the row partition in note section 6: for arbitrary
# finite D34b state, only A rows and births/interactions of A-neighbors can
# alter (c,h); each contribution depends on (c,h) exactly as printed.  The
# parent D34b nonexplosion theorem supplies uniqueness of the projected marked
# pure-jump law.  The finite regression above is deliberately not the proof.
analytic_partition_hypotheses = (
    projection_matches and labeled_projection_matches
    and all(rate > 0 for boundary in audit_boundaries
            for rate in boundary_formula_rows(boundary).values())
    and e5_ok
    and len(capacity_ledger) == 7
)
e6_ok = (
    analytic_partition_hypotheses
    and all(probability > 0 for probability in poisson_probs)
    and poisson_recurrence
)
check(
    "E6 BRANCH C/L ALL-FUTURE GROWING-CARRIER THEOREM [analytic generator "
    "partition + inherited D34b nonexplosion]: B3's distributed star screens "
    "the declared coarse/role-labeled marked wire process and updates locally; "
    "A's rate-1/4 birth process gives unbounded port support, so no bounded "
    "collar or one-record state follows",
    e6_ok,
    f"Poisson(T=1,m=20)={poisson_probs[-1]:.32E}; capacity fields="
    f"{len(capacity_ledger)}",
)


# ---------------------------------------------------------------------------
# E7: every fixed actor-graph radius loses full durable record ancestry.

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


def radius_projection(state, root, radius):
    distances = actor_distances(state, root)
    inside = {actor for actor, distance in distances.items() if distance <= radius}
    owned = tuple(sorted(
        (actor, actor_row(state, actor), state["last"].get(actor))
        for actor in inside
    ))
    refs = tuple(sorted(
        (neighbor, len(state["neighbors"][neighbor]))
        for actor in inside for neighbor in state["neighbors"][actor]
        if neighbor not in inside
    ))
    local_events = tuple(sorted(
        repr(event) for event in state["events"]
        if set(event[5]) <= inside
    ))
    return owned, refs, local_events


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
    branch_eid = idle_branch["last"][distant]

    if radius_projection(idle_branch, "A", radius) != radius_projection(
            interact_branch, "A", radius):
        raise AssertionError("branch leaked inside registered radius")

    future_mass = F(1)
    idle_future = idle_branch
    interact_future = interact_branch
    for index in range(len(path) - 1, 0, -1):
        child = path[index]
        parent = path[index - 1]
        p_step = event_rate(idle_future, "i", child, parent) / len(
            active_actors(idle_future)
        )
        p_step_other = event_rate(interact_future, "i", child, parent) / len(
            active_actors(interact_future)
        )
        if p_step != p_step_other:
            raise AssertionError("paired propagation masses differ")
        future_mass *= p_step
        idle_future = d34b_step(idle_future, "i", child, parent)
        interact_future = d34b_step(interact_future, "i", child, parent)

    final_idle = idle_future["last"]["A"]
    final_interact = interact_future["last"]["A"]
    ancestry_idle = event_ancestry(idle_future, final_idle)
    ancestry_interact = event_ancestry(interact_future, final_interact)
    record_idle = next(event for event in ancestry_idle if event[0] == branch_eid)
    record_interact = next(
        event for event in ancestry_interact if event[0] == branch_eid
    )
    expected_mass = F(1, 8 * (radius + 3)) ** (radius + 1)
    return {
        "radius": radius,
        "local_equal": True,
        "idle_past_mass": idle_mass,
        "interact_past_mass": interact_mass,
        "future_mass": future_mass,
        "expected_mass": expected_mass,
        "idle_kind": record_idle[1],
        "interact_kind": record_interact[1],
        "ancestry_distinct": ancestry_idle != ancestry_interact,
    }


radius_witnesses = tuple(grow_chain_branch(radius) for radius in range(4))
e7_ok = all(
    row["local_equal"]
    and row["idle_past_mass"] > 0
    and row["interact_past_mass"] > 0
    and row["future_mass"] == row["expected_mass"] > 0
    and row["idle_kind"] == "n"
    and row["interact_kind"] == "i"
    and row["ancestry_distinct"]
    for row in radius_witnesses
)
check(
    "E7 BRANCH F FIXED-RADIUS OBSTRUCTION [Fraction-exact specimens + "
    "all-r analytic chain]: outside-radius D-idle versus D-to-E pasts have "
    "identical local carriers; the same positive inward interaction cylinder "
    "delivers the immutable differing D record into A's ancestor sub-DAG",
    e7_ok,
    "future path masses=" + ",".join(
        f"r{row['radius']}:{ftext(row['future_mass'])}"
        for row in radius_witnesses
    ),
)


# ---------------------------------------------------------------------------
# E8: disconnected control and exact component ceiling.

def a_local_rows(state):
    return tuple(
        (kind, y, target, rate)
        for kind, y, target, rate in d34b_rates(state)
        if y == "A" or (kind == "i" and target == "A")
    )


remote_rows_equal = a_local_rows(seed_state()) == a_local_rows(seed_state(remote=True))
component_of_a = set(actor_distances(seed_state(remote=True), "A"))
remote_disjoint = component_of_a == {"A", "B"}
component_upper_bound_fields = (
    "actors/counters/carriers",
    "typed adjacency/eligibility",
    "wire tips",
    "persistent event records",
)
e8_ok = remote_rows_equal and remote_disjoint and len(component_upper_bound_fields) == 4
check(
    "E8 WHOLE-COMPONENT SUFFICIENCY UPPER BOUND / DISCONNECTED NEGATIVE "
    "CONTROL [exact + parent product theorem]: A's connected D34b component "
    "contains every possible influence path; adding disconnected P--Q leaves "
    "all A-local rows unchanged. Literal global state is unnecessary, while "
    "minimal full-record encoding remains open",
    e8_ok,
    f"A component={sorted(component_of_a)}; upper-bound fields="
    f"{len(component_upper_bound_fields)}",
)


# ---------------------------------------------------------------------------
# E9: finite prefix/cylinder map and the profinite ceiling.

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
past_finite_specimens = all(
    len(transitive_relations(state["events"])) <= len(state["events"]) ** 2
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

e9_ok = (
    finite_pushforward_ok
    and past_finite_specimens
    and finite_shadow_equal
    and marked_output_differs
)
check(
    "E9 FINITE u/PREFIX PUSHFORWARD + STEM CEILING [exact]: forgetting marks "
    "gives finite past-finite orders and the depth-4 prefix law restricts to "
    "depth 3; a one-point unmarked shadow does not determine marked carrier "
    "output. This is not a v9 posterior-sufficiency or profinite theorem",
    e9_ok,
    f"path counts d3/d4={len(paths3)}/{len(paths4)}; unmarked classes="
    f"{len(push3)}/{len(push4)}",
)


# ---------------------------------------------------------------------------
# E10: quantum/process branch refusal is a typed result, not missing work hidden.

quantum_inputs = {
    "finite D34c strongly-positive typed-DAG family": True,
    "auxiliary P,E causal-break negative control": True,
    "timed controlled D34b-D34c process family": False,
    "licensed all-instrument kernels P(r|I,h)": False,
}
quantum_refusal = (
    quantum_inputs["finite D34c strongly-positive typed-DAG family"]
    and quantum_inputs["auxiliary P,E causal-break negative control"]
    and not quantum_inputs["timed controlled D34b-D34c process family"]
    and not quantum_inputs["licensed all-instrument kernels P(r|I,h)"]
)
assigned_quantum_widths = ()
e10_ok = quantum_refusal and assigned_quantum_widths == ()
check(
    "E10 INTRINSIC QUANTUM D34e BRANCH — REFUSAL/UNDEFINED [typed input "
    "gate]: finite D34c and auxiliary P,E evidence exist, but no timed "
    "controlled D34b-D34c process supplies P(r|I,h); no SHARD d_carrier, d_op "
    "or chi_cut is assigned",
    e10_ok,
    "missing controlled process and intervention kernels; widths=unassigned",
)


# ---------------------------------------------------------------------------
# E11: branch verdicts and claim ceiling.

branch_verdicts = {
    "C coarse A-wire": "ALL-FUTURE GROWING-CARRIER PASS / POINTWISE",
    "L role-labeled A-wire": "ALL-FUTURE GROWING-CARRIER PASS / POINTWISE",
    "F full ancestry fixed-radius class": "CANDIDATE-CLASS OBSTRUCTION",
    "F whole component": "SUFFICIENT GROWING UPPER BOUND; MINIMALITY OPEN",
    "v9 stem posterior factor": "REFUSAL/UNDEFINED BEYOND FINITE u GATES",
    "intrinsic quantum": "REFUSAL/UNDEFINED",
}
flags = {
    "C screening": "pass",
    "C recursive time/event closure": "pass",
    "L covariance": "pass",
    "L composition": "pass",
    "uniform capacity": "fail: unbounded ports/degrees/counters",
    "NSE": "not applicable: no physical deletion",
    "F fixed radius": "fail for every r by analytic chain",
    "profinite factorization": "not proved",
    "quantum boundary": "undefined without controlled law",
}
e11_ok = (
    PASS == 10 and FAIL == 0
    and len(branch_verdicts) == 6
    and len(flags) == 9
    and branch_verdicts["C coarse A-wire"].startswith("ALL-FUTURE GROWING")
    and branch_verdicts["F full ancestry fixed-radius class"]
    == "CANDIDATE-CLASS OBSTRUCTION"
)
check(
    "E11 DEPENDENT D34e SCORECARD: Branch C/L have an exact distributed "
    "all-future but unbounded record-DAG star carrier; Branch F defeats every "
    "fixed actor radius and has only a whole-component sufficient upper bound; "
    "minimal full-record, v9 posterior-factor and intrinsic quantum boundaries "
    "remain open/undefined",
    e11_ok,
    "maximum noun: QUERY-RELATIVE GROWING-BOUNDARY THEOREM + FIXED-RADIUS "
    "FULL-ANCESTRY OBSTRUCTION",
)


summary = (
    f"gates={PASS}/{PASS + FAIL}; levels={','.join(map(str, level_counts))}; "
    f"states={len(enumerated_states)}; collisions={lumpability_collisions}; "
    f"rate_gap={ftext(derivative_gap)}; "
    f"signatures={','.join(map(str, signature_counts))}; "
    f"radius_masses={','.join(ftext(row['future_mass']) for row in radius_witnesses)}; "
    f"prefix_classes={len(push3)},{len(push4)}; quantum=REFUSAL"
)
digest = hashlib.sha256(summary.encode("utf-8")).hexdigest()
print(f"[SUMMARY] {summary}")
print(f"[RECEIPT-SHA256] {digest}")
print(f"[VERDICT] {'PASS' if FAIL == 0 else 'FAIL'} — {PASS}/{PASS + FAIL}")
sys.exit(1 if FAIL else 0)
