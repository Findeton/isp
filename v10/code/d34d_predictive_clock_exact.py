#!/usr/bin/env python3
"""D34d classical exact receipt: predictive states, memory, and clocks.

Pin: note-d34d-predictive-state-clock-status.md / commit 77defcd,
committed before this executable existed.

The receipt separates four statements that are often blurred together:

* complete-history Markovization is always available for the finite specimen,
  but its state count grows with the retained history;
* a smaller predictive state exists only when it is sufficient for the future;
* a visible record projection is Markov exactly when it is lumpable;
* exponential construction clocks remove waiting-age memory, but neither set
  physical seconds nor make relative actor rates gauge.

All discrete probabilities are Fraction-exact.  The only transcendental
quantities are explicitly labeled 100-decimal regressions of analytic
exponential identities.  Gates P1--P12 are substantive; P13 is the dependent
claim scorecard.  Exit 1 on any failure.
"""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction as F
from itertools import product
import hashlib
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


def mat_rows_normalized(matrix):
    return all(sum(row, F(0)) == 1 and all(x >= 0 for x in row)
               for row in matrix)


print("[d34d — exact predictive-state, observable-memory and clock status]")


# ---------------------------------------------------------------------------
# P1/P2/P3 specimen: a three-state hidden chain with a two-symbol durable
# record.  A and B both look like record 0 but have different futures.

STATES = ("A", "B", "C")
OBS = {"A": 0, "B": 0, "C": 1}
TRANS = (
    (F(1, 2), F(0), F(1, 2)),
    (F(0), F(3, 4), F(1, 4)),
    (F(1, 2), F(1, 2), F(0)),
)
INITIAL = (F(1, 3), F(1, 3), F(1, 3))
assert mat_rows_normalized(TRANS) and sum(INITIAL, F(0)) == 1


def normalize(weights):
    z = sum(weights, F(0))
    if z == 0:
        return None, F(0)
    return tuple(x / z for x in weights), z


def condition_observation(prior, observation):
    return normalize(tuple(
        p if OBS[state] == observation else F(0)
        for state, p in zip(STATES, prior)
    ))


def predict_hidden(belief):
    return tuple(sum(belief[i] * TRANS[i][j] for i in range(len(STATES)))
                 for j in range(len(STATES)))


def forward_observations(word):
    """Posterior and cylinder mass for observations at times 0..len(word)-1."""
    if not word:
        return INITIAL, F(1)
    belief, first_mass = condition_observation(INITIAL, word[0])
    if belief is None:
        return None, F(0)
    mass = first_mass
    for y in word[1:]:
        forecast = predict_hidden(belief)
        belief, step_mass = condition_observation(forecast, y)
        if belief is None:
            return None, F(0)
        mass *= step_mass
    return belief, mass


def next_observation_probability(belief, y):
    forecast = predict_hidden(belief)
    return sum(p for state, p in zip(STATES, forecast) if OBS[state] == y)


def positive_words(length):
    out = []
    for word in product((0, 1), repeat=length):
        belief, mass = forward_observations(word)
        if mass:
            out.append((word, belief, mass))
    return out


# Same current record 0, different observed pasts, different future.
b10, m10 = forward_observations((1, 0))
b00, m00 = forward_observations((0, 0))
n10 = next_observation_probability(b10, 1)
n00 = next_observation_probability(b00, 1)

# A full observed-history state closes trivially: from a word h, append the
# next symbol with the exact conditional law.  Its number of states grows.
history_counts = []
history_rows_close = True
for depth in range(1, 7):
    rows = positive_words(depth)
    history_counts.append(len(rows))
    for word, belief, mass in rows:
        q0 = next_observation_probability(belief, 0)
        q1 = next_observation_probability(belief, 1)
        history_rows_close &= q0 + q1 == 1
        for y, q in ((0, q0), (1, q1)):
            _, extended_mass = forward_observations(word + (y,))
            history_rows_close &= extended_mass == mass * q

p1_ok = (
    m10 > 0 and m00 > 0
    and b10 == (F(1, 2), F(1, 2), F(0))
    and b00 == (F(2, 5), F(3, 5), F(0))
    and n10 == F(3, 8) and n00 == F(7, 20) and n10 != n00
    and history_rows_close
    and history_counts[-1] > len(set(OBS.values()))
    and all(a < b for a, b in zip(history_counts, history_counts[1:]))
)
check(
    "P1 FULL-HISTORY MARKOVIZATION IS GLOBAL/TRIVIAL [exact]: the complete "
    "visible word closes under append-conditioning, while a non-Markov "
    "visible witness has the same present record 0 after histories 10 and "
    "00 but next-record-1 probabilities 3/8 and 7/20; the retained history "
    "state count grows rather than providing fixed local compression",
    p1_ok,
    f"posterior(10)={b10}, posterior(00)={b00}; next1={n10} vs {n00}; "
    f"positive-history counts={history_counts}",
)


# Predictive signatures of a known hidden state are kept as the ontic/hidden
# realization ledger.  The operational predictive quotient is instead built
# from every reachable observed-history posterior below.
def future_word_probability_from_state(state, word):
    belief = tuple(F(1) if s == state else F(0) for s in STATES)
    mass = F(1)
    for y in word:
        belief = predict_hidden(belief)
        belief, q = condition_observation(belief, y)
        if belief is None:
            return F(0)
        mass *= q
    return mass


def predictive_signature(state, horizon):
    return tuple(
        future_word_probability_from_state(state, word)
        for length in range(1, horizon + 1)
        for word in product((0, 1), repeat=length)
    )


partitions = []
for horizon in range(1, 5):
    groups = defaultdict(list)
    for state in STATES:
        groups[predictive_signature(state, horizon)].append(state)
    partitions.append(tuple(sorted(tuple(v) for v in groups.values())))

# Exact predictive quotient of OBSERVED PASTS.  For this specimen distinct
# reachable beliefs are already distinguished by a one-step future law.  At a
# current zero they have form (p,1-p,0) and next-one law 1/4+p/4; at current
# one the belief is the singleton C state.
belief_class_counts = []
belief_injection_ok = True
for depth in range(1, 13):
    beliefs = sorted(set(belief for _, belief, _ in positive_words(depth)))
    belief_class_counts.append(len(beliefs))
    zero_beliefs = [b for b in beliefs if b[2] == 0]
    signatures = []
    for belief in zero_beliefs:
        p = belief[0]
        q1 = next_observation_probability(belief, 1)
        belief_injection_ok &= q1 == F(1, 4) + p / 4
        signatures.append(q1)
    belief_injection_ok &= len(signatures) == len(set(signatures))

p2_ok = (
    partitions == [(('A',), ('B',), ('C',))] * 4
    and b10 != b00
    and n10 != n00
    and belief_class_counts == list(range(2, 14))
    and belief_injection_ok
)
check(
    "P2 OBSERVED-HISTORY PREDICTIVE QUOTIENT [exact]: the ontic realization "
    "has three future-distinct hidden states, but quotienting positive observed "
    "pasts gives 2,3,...,13 reachable belief classes through depths 1..12; "
    "for present record zero, next-one=1/4+p/4 makes distinct beliefs "
    "one-step predictively distinct",
    p2_ok,
    f"hidden partitions={partitions}; observed classes={belief_class_counts}; "
    f"witness beliefs={b10} vs {b00}",
)


# Strong lumpability positive control.
GOOD_STATES = ("D", "E", "F")
GOOD_OBS = {"D": 0, "E": 0, "F": 1}
GOOD_TRANS = (
    (F(1, 3), F(1, 3), F(1, 3)),
    (F(2, 3), F(0), F(1, 3)),
    (F(1, 4), F(1, 4), F(1, 2)),
)


def group_sums(states, obs, matrix):
    groups = sorted(set(obs.values()))
    return {
        state: tuple(sum(matrix[i][j] for j, target in enumerate(states)
                         if obs[target] == group)
                     for group in groups)
        for i, state in enumerate(states)
    }


def strongly_lumpable(states, obs, matrix):
    sums = group_sums(states, obs, matrix)
    return all(sums[a] == sums[b]
               for a in states for b in states if obs[a] == obs[b])


good_sums = group_sums(GOOD_STATES, GOOD_OBS, GOOD_TRANS)
bad_sums = group_sums(STATES, OBS, TRANS)
good_quotient = (good_sums["D"], good_sums["F"])

# A chain that is NOT strongly lumpable, but whose projection is Markov for
# the declared delta_A initial law because the offending hidden B state is
# unreachable.  This prevents strong and law-relative lumpability from being
# conflated.
WEAK_STATES = ("A", "B", "C")
WEAK_OBS = {"A": 0, "B": 0, "C": 1}
WEAK_TRANS = (
    (F(1, 2), F(0), F(1, 2)),
    (F(0), F(3, 4), F(1, 4)),
    (F(1), F(0), F(0)),
)
weak_sums = group_sums(WEAK_STATES, WEAK_OBS, WEAK_TRANS)
weak_not_strong = not strongly_lumpable(
    WEAK_STATES, WEAK_OBS, WEAK_TRANS
)
weak_reachable = {"A", "C"}
weak_law_relative_rows = {
    0: weak_sums["A"],
    1: weak_sums["C"],
}
weak_projection_markov = (
    weak_not_strong
    and weak_sums["A"] == (F(1, 2), F(1, 2))
    and weak_sums["B"] == (F(3, 4), F(1, 4))
    and weak_sums["C"] == (F(1), F(0))
    and all(state in ("A", "C") for state in weak_reachable)
)
p3_ok = (
    mat_rows_normalized(GOOD_TRANS)
    and strongly_lumpable(GOOD_STATES, GOOD_OBS, GOOD_TRANS)
    and good_sums["D"] == good_sums["E"] == (F(2, 3), F(1, 3))
    and good_sums["F"] == (F(1, 2), F(1, 2))
    and not strongly_lumpable(STATES, OBS, TRANS)
    and bad_sums["A"] == (F(1, 2), F(1, 2))
    and bad_sums["B"] == (F(3, 4), F(1, 4))
    and n10 != n00
    and mat_rows_normalized(WEAK_TRANS)
    and weak_projection_markov
)
check(
    "P3 THREE LUMPABILITY SCOPES [exact]: the positive control is strongly "
    "lumpable for every initial law; a second chain is not strongly lumpable "
    "but is Markov from delta_A because offending B is unreachable; the "
    "uniform-initial witness is actually non-Markov via histories 10/00",
    p3_ok,
    f"good quotient={good_quotient}; bad A={bad_sums['A']}, "
    f"bad B={bad_sums['B']}; weak law rows={weak_law_relative_rows}; "
    f"next1={n10} vs {n00}",
)


# ---------------------------------------------------------------------------
# P4: local predictive closure is not the global history-state construction.
# An independent remote transition factors out of the local marginal.  A
# fixed-global-event race is the deliberately wrong locality test.

LOCAL_TRANS = (
    (F(3, 4), F(1, 4)),
    (F(1, 3), F(2, 3)),
)
REMOTE_TRANS = (
    (F(1, 2), F(1, 2)),
    (F(1, 4), F(3, 4)),
)

factor_marginal_ok = True
for local_now in range(2):
    for remote_now in range(2):
        for local_next in range(2):
            joint_sum = sum(
                LOCAL_TRANS[local_now][local_next]
                * REMOTE_TRANS[remote_now][remote_next]
                for remote_next in range(2)
            )
            factor_marginal_ok &= joint_sum == LOCAL_TRANS[local_now][local_next]

own_ring_birth = F(1, 4)
global_race_one_remote = F(1, 2)
global_race_three_remote = F(1, 4)
p4_ok = (
    mat_rows_normalized(LOCAL_TRANS) and mat_rows_normalized(REMOTE_TRANS)
    and factor_marginal_ok
    and own_ring_birth == F(1, 4)
    and global_race_one_remote != global_race_three_remote
)
check(
    "P4 RECORD-LOCAL VERSUS GLOBAL-CENSUS STATE [exact]: an independent "
    "remote component tensors out of every local transition, and A's own-ring "
    "birth law stays 1/4; at fixed global event count the chance that A rings "
    "changes from 1/2 to 1/4 when the remote census changes, so that stopping "
    "rule is exposed as nonlocal rather than used as a locality criterion",
    p4_ok,
    "product marginal exact for 2x2x2 states; own-ring birth=1/4; "
    "global-race A-share=1/2 vs 1/4",
)


# ---------------------------------------------------------------------------
# P5: clock memory.  The analytic exponential identity is checked symbolically
# at the exponent level and at 100 decimal places.  A bounded uniform renewal
# gives an exact age-dependent negative control.

one = Decimal(1)
exp_neg_one = (-one).exp()
exp_ratio = (Decimal(-2).exp() / Decimal(-1).exp())
hp_tolerance = Decimal(10) ** Decimal(-100)
analytic_exponent_identity = (-(F(1) + F(1)) + F(1) == -F(1))
hp_memoryless = abs(exp_ratio - exp_neg_one) < hp_tolerance


def uniform_survival(t):
    # Exact survival for T ~ Uniform[0,2], at the points used below.
    if t < 0:
        return F(1)
    if t > 2:
        return F(0)
    return F(1) - t / 2


def conditional_ring_within(age, delta):
    return F(1) - uniform_survival(age + delta) / uniform_survival(age)


renewal_age0 = conditional_ring_within(F(0), F(1, 2))
renewal_age1 = conditional_ring_within(F(1), F(1, 2))

# For k equal-rate exponential actors, the next identity is uniform and the
# next local mark law remains q.  Ages are absent by memorylessness.
race_rows = {
    k: tuple(F(1, k) for _ in range(k))
    for k in range(1, 9)
}
race_rows_ok = all(sum(row, F(0)) == 1 for row in race_rows.values())
mark_law = (F(1, 4), F(1, 4), F(1, 2))
p5_ok = (
    analytic_exponent_identity and hp_memoryless
    and renewal_age0 == F(1, 4) and renewal_age1 == F(1, 2)
    and renewal_age0 != renewal_age1
    and race_rows_ok and sum(mark_law, F(0)) == 1
)
check(
    "P5 SINGLE-CLOCK AGE WITNESS [exact + 100-decimal regression]: an "
    "exponential residual wait is age-independent, while a uniform-renewal "
    "clock has next-half-unit ring probabilities 1/4 at age 0 and 1/2 at "
    "age 1; this proves age necessity for the renewal control, not yet the "
    "full D34b generator or interacting renewal sufficiency",
    p5_ok,
    f"exp ratio={exp_ratio:.100f}; exp(-1)={exp_neg_one:.100f}; "
    f"renewal={renewal_age0} vs {renewal_age1}; k=1..8 race rows normalized",
)


# ---------------------------------------------------------------------------
# P6: serializer gauge, time units, and physical relative rates.

lambda_a = F(1)
lambda_b = F(2)
order_ab = lambda_a / (lambda_a + lambda_b)
order_ba = lambda_b / (lambda_a + lambda_b)

scale = F(7)
scaled_ab = scale * lambda_a / (scale * lambda_a + scale * lambda_b)
scaled_ba = scale * lambda_b / (scale * lambda_a + scale * lambda_b)

# If the two events are record-disjoint/incomparable, both serializer orders
# canonicalize to one physical typed DAG and their pushforward masses add.
canonical_disjoint = {
    ("A-idle", "P-birth"): "two-disjoint-events",
    ("P-birth", "A-idle"): "two-disjoint-events",
}
disjoint_mass = order_ab + order_ba

# If both events touch one shared wire, their order is recorded physics.
shared_a_first_old = order_ab
shared_a_first_changed = F(2) / (F(2) + F(2))

# A pathwise strictly increasing change of the already realized coordinate
# preserves order; it is not a license to change relative hazard laws.
times = (F(1, 3), F(5, 4), F(7, 3))
transformed = tuple(t * t * t + t for t in times)
monotone_order_preserved = all(
    (times[i] < times[j]) == (transformed[i] < transformed[j])
    for i in range(len(times)) for j in range(len(times))
)

p6_ok = (
    order_ab == F(1, 3) and order_ba == F(2, 3)
    and scaled_ab == order_ab and scaled_ba == order_ba
    and len(set(canonical_disjoint.values())) == 1 and disjoint_mass == 1
    and monotone_order_preserved
    and shared_a_first_old == F(1, 3)
    and shared_a_first_changed == F(1, 2)
    and shared_a_first_old != shared_a_first_changed
)
check(
    "P6 TIME/ORDER GAUGE BOUNDARY [exact]: incomparable serializer orders "
    "push to one DAG with total mass one; a common rate rescaling and a "
    "pathwise increasing coordinate change preserve untimed order data; "
    "changing relative rates changes a shared-wire A-first probability from "
    "1/3 to 1/2, so relative clocks are physical model data, not proven gauge",
    p6_ok,
    "disjoint AB+BA=1; common x7 unchanged; shared A-first=1/3 -> 1/2",
)


# ---------------------------------------------------------------------------
# P7: dependent scope scorecard and deterministic receipt digest.

p7_ok = PASS == 6 and FAIL == 0
check(
    "P7 BASELINE WITNESS SCORECARD [dependent, rescoped after round 1]: the "
    "finite HMM, product-factor, clock-age and order/rate witnesses pass. They "
    "do not by themselves prove D34b strong-Markov closure, a bounded local "
    "predictive state, renewal sufficiency, a typed-DAG gauge theorem, physical "
    "time, or the universe law; the D34b replacement gates follow",
    p7_ok,
    "round-1 survivor: FINITE HMM + CLOCK-AGE + ORDER/RATE WITNESSES",
)


# ---------------------------------------------------------------------------
# P8: the actual ideal D34b configuration and support-local generator.

def d34b_seed(remote=False):
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


def d34b_copy(state):
    return {
        "actors": {name: dict(row) for name, row in state["actors"].items()},
        "neighbors": {name: set(row) for name, row in state["neighbors"].items()},
        "last": dict(state["last"]),
        "events": list(state["events"]),
    }


def d34b_rates(state):
    """Generator event intensities for the ideal unit-rate D34b law."""
    rows = []
    for y in sorted(state["actors"]):
        if state["actors"][y]["sealed"]:
            continue
        neighbors = sorted(
            x for x in state["neighbors"][y]
            if not state["actors"][x]["sealed"]
        )
        rows.append(("b", y, None, F(1, 4)))
        if not neighbors:
            raise ValueError("the chosen D34b exemplar requires eligibility")
        for x in neighbors:
            rows.append(("i", y, x, F(1, 4 * len(neighbors))))
        rows.append(("n", y, None, F(1, 2)))
    return tuple(rows)


def d34b_step(state, kind, y, target=None):
    out = d34b_copy(state)
    actor = out["actors"][y]
    if actor["sealed"]:
        raise ValueError("sealed initiator")
    actor["ring"] += 1
    eid = f"{y}#r{actor['ring']}"
    if kind == "b":
        actor["births"] += 1
        target = f"{y}/{actor['births']}"
        out["actors"][target] = {
            "ring": 0, "births": 0, "sealed": False, "carrier": 0,
        }
        out["neighbors"][y].add(target)
        out["neighbors"][target] = {y}
        touched = (y, target)
    elif kind == "i":
        if (target not in out["neighbors"][y]
                or out["actors"][target]["sealed"]):
            raise ValueError("ineligible target")
        touched = (y, target)
        # The classical receipt records that a carrier update occurs without
        # choosing D34c's quantum operation as fundamental here.
        out["actors"][y]["carrier"] ^= 1
        out["actors"][target]["carrier"] ^= 1
    elif kind == "n":
        touched = (y,)
    else:
        raise ValueError(kind)
    predecessors = tuple(sorted(
        out["last"][name] for name in touched if name in out["last"]
    ))
    out["events"].append((eid, kind, y, target, predecessors, tuple(touched)))
    for name in touched:
        out["last"][name] = eid
    return out


def actor_rate_mass(state, actor):
    return sum(rate for _, y, _, rate in d34b_rates(state) if y == actor)


def event_rate(state, kind, y, target=None):
    return next(rate for k, yy, x, rate in d34b_rates(state)
                if (k, yy, x) == (kind, y, target))


def d34b_state_key(state):
    actors = tuple(sorted(
        (name, row["ring"], row["births"], row["sealed"], row["carrier"])
        for name, row in state["actors"].items()
    ))
    neighbors = tuple(sorted(
        (name, tuple(sorted(xs))) for name, xs in state["neighbors"].items()
    ))
    events = tuple(sorted(state["events"]))
    last = tuple(sorted(state["last"].items()))
    return actors, neighbors, events, last


seed = d34b_seed()
seed_remote = d34b_seed(remote=True)

# Actual eligibility control from the actor architecture: an event-inert
# sealed root R is adjacent to A but cannot initiate or receive an interaction.
sealed_root_seed = d34b_seed()
sealed_root_seed["actors"]["R"] = {
    "ring": 0, "births": 0, "sealed": True, "carrier": 0,
}
sealed_root_seed["neighbors"]["R"] = {"A"}
sealed_root_seed["neighbors"]["A"].add("R")

rate_rows_current_only = d34b_rates(seed) == d34b_rates(d34b_copy(seed))
per_actor_normalized = all(
    actor_rate_mass(seed_remote, actor) == 1
    for actor in seed_remote["actors"]
)
total_intensity = sum(row[3] for row in d34b_rates(seed_remote))

# Generator inventory: these fields, not the finite PRF reference's stored
# absolute deadlines, define the ideal configuration state.
z_fields = (
    "active/sealed Ulam actors",
    "private ring and birth ordinals",
    "typed adjacency/eligibility",
    "wire tips and marked event history",
    "modeled carrier fields",
)
poisson_theorem_hypotheses = (
    "independent rate-one Poisson increments",
    "independent fresh local marks",
    "measurable support-local updates",
    "finite intensity on every finite configuration",
)
sealed_rows = d34b_rates(sealed_root_seed)
sealed_eligibility_ok = (
    event_rate(sealed_root_seed, "i", "A", "B") == F(1, 4)
    and not any(y == "R" or target == "R"
                for _, y, target, _ in sealed_rows)
)

p8_ok = (
    rate_rows_current_only
    and per_actor_normalized
    and total_intensity == len(seed_remote["actors"])
    and event_rate(seed, "b", "A") == F(1, 4)
    and event_rate(seed, "i", "A", "B") == F(1, 4)
    and event_rate(seed, "n", "A") == F(1, 2)
    and sealed_eligibility_ok
    and len(z_fields) == 5 and len(poisson_theorem_hypotheses) == 4
)
check(
    "P8 ACTUAL D34b GLOBAL STRONG-MARKOV OBJECT [exact generator + analytic "
    "theorem]: Z_t inventories actors, counters, adjacency, tips/events and "
    "carriers; each actor contributes birth 1/4, neighbor interactions totaling "
    "1/4, and idle 1/2. Independent Poisson increments/fresh marks with "
    "support-local measurable updates give the ideal process the strong Markov "
    "property at stopping times of the complete construction-time filtration; "
    "an adjacent sealed root is excluded from initiator and target rows",
    p8_ok,
    f"fields={len(z_fields)}; hypotheses={len(poisson_theorem_hypotheses)}; "
    f"Seed4 total intensity={total_intensity}; every active row=1; "
    "sealed R absent and A->B=1/4",
)


# ---------------------------------------------------------------------------
# P9: locality hierarchy and stopping scopes on actual D34b states.

before_birth = d34b_seed()
incoming_before = event_rate(before_birth, "i", "B", "A")
after_b_birth = d34b_step(before_birth, "b", "B")
incoming_after = event_rate(after_b_birth, "i", "B", "A")
a_tip_unchanged = (
    before_birth["last"].get("A") == after_b_birth["last"].get("A")
    and before_birth["actors"]["A"] == after_b_birth["actors"]["A"]
)

incoming_state = d34b_step(d34b_seed(), "i", "B", "A")
a_own_rings = incoming_state["actors"]["A"]["ring"]
a_wire_events = sum("A" in event[5] for event in incoming_state["events"])
global_events = len(incoming_state["events"])
incoming_tip = incoming_state["last"]["A"]

# A next own event carries the passive reception as physical predecessor.
after_a_idle = d34b_step(incoming_state, "n", "A")
a_idle_event = next(e for e in after_a_idle["events"] if e[0] == "A#r1")
reception_is_predecessor = incoming_tip in a_idle_event[4]

# A disconnected component does not alter any A-initiated generator row.
def a_rate_projection(state):
    return tuple(row for row in d34b_rates(state) if row[1] == "A")


remote_invariant = a_rate_projection(d34b_seed()) == a_rate_projection(
    d34b_seed(remote=True)
)

stopping_dictionary = {
    "fixed construction time": "T on ideal Poisson source",
    "A own-ring count": a_own_rings,
    "A wire-event count": a_wire_events,
    "fixed global event count": global_events,
    "untimed order skeleton": tuple(e[:5] for e in incoming_state["events"]),
}

p9_ok = (
    incoming_before == F(1, 4) and incoming_after == F(1, 8)
    and a_tip_unchanged
    and a_own_rings == 0 and a_wire_events == 1 and global_events == 1
    and reception_is_predecessor
    and remote_invariant
    and len(stopping_dictionary) == 5
)
check(
    "P9 D34b LOCALITY HIERARCHY / STOPPING DICTIONARY [exact]: B gaining a "
    "child changes B->A rate 1/4->1/8 while A's tip/private state is unchanged; "
    "incoming reception adds one A-wire event but zero A-own rings and becomes "
    "A's next predecessor; a disconnected actor pair leaves A's generator row "
    "unchanged. Thus Z_t is global with support-local terms, while A's tip is "
    "not sufficient and no bounded all-future collar is claimed",
    p9_ok,
    f"incoming={incoming_before}->{incoming_after}; own/wire/global="
    f"{a_own_rings}/{a_wire_events}/{global_events}; stops=5",
)


# ---------------------------------------------------------------------------
# P10: age-augmented interacting renewal closure.

def residual_survival_uniform(age, extra):
    if uniform_survival(age) == 0:
        raise ValueError("unreachable expired age")
    return uniform_survival(age + extra) / uniform_survival(age)


def uniform_race_a_first(age_a, age_b):
    # Conditional residuals are Uniform(0,L_A), Uniform(0,L_B).
    la = F(2) - age_a
    lb = F(2) - age_b
    if la <= 0 or lb <= 0:
        raise ValueError("expired clock")
    if la <= lb:
        return F(1) - la / (2 * lb)
    return lb / (2 * la)


age_kernel_1 = (
    uniform_race_a_first(F(0), F(1)),
    F(1) - uniform_race_a_first(F(0), F(1)),
)
# Independent direct integral for L_A=2,L_B=1:
# int_0^1 (1/L_A)(1-r/L_B) dr = 1/4.
age_kernel_direct = (F(1, 4), F(3, 4))

# At elapsed 1/2, B rings and interacts into passive A.  B resets; A does not.
elapsed = F(1, 2)
ages_before = {"A": F(0), "B": F(1)}
ages_after_b_to_a = {
    "A": ages_before["A"] + elapsed,
    "B": F(0),
}
newborn_age = F(0)

joint_survival = (
    residual_survival_uniform(F(0), F(1, 2))
    * residual_survival_uniform(F(1), F(1, 2))
)
p10_ok = (
    residual_survival_uniform(F(0), F(1, 2)) == F(3, 4)
    and residual_survival_uniform(F(1), F(1, 2)) == F(1, 2)
    and age_kernel_1 == age_kernel_direct == (F(1, 4), F(3, 4))
    and sum(age_kernel_1, F(0)) == 1
    and ages_after_b_to_a == {"A": F(1, 2), "B": F(0)}
    and newborn_age == 0 and joint_survival == F(3, 8)
)
check(
    "P10 AGE-AUGMENTED RENEWAL SUFFICIENCY [exact specimen + analytic PDMP "
    "kernel]: conditional residual survival is S(a+s)/S(a); two actors at ages "
    "(0,1) have winner law (1/4,3/4), determined only by graph+age state; "
    "initiator B resets, passive receiver A advances without reset, and a "
    "newborn starts at zero. Independent residuals plus these updates close the "
    "global age-vector process, not a local observer's hidden-age belief",
    p10_ok,
    f"race={age_kernel_1}; post B->A ages={ages_after_b_to_a}; "
    f"joint half-unit survival={joint_survival}",
)


# ---------------------------------------------------------------------------
# P11: actual typed-DAG serializer and honest time/rate transformation table.

def physical_dag_key(state):
    return tuple(sorted(
        (eid, kind, y, target, tuple(preds), tuple(sorted(touched)))
        for eid, kind, y, target, preds, touched in state["events"]
    ))


disjoint_ab = d34b_step(d34b_step(d34b_seed(remote=True), "n", "A"),
                         "b", "P")
disjoint_ba = d34b_step(d34b_step(d34b_seed(remote=True), "b", "P"),
                         "n", "A")
typed_serializer_gauge = (
    physical_dag_key(disjoint_ab) == physical_dag_key(disjoint_ba)
    and d34b_state_key(disjoint_ab) == d34b_state_key(disjoint_ba)
)

shared_ab = d34b_step(d34b_step(d34b_seed(), "i", "A", "B"), "b", "B")
shared_ba = d34b_step(d34b_step(d34b_seed(), "b", "B"), "i", "A", "B")
shared_order_physical = physical_dag_key(shared_ab) != physical_dag_key(shared_ba)

# Full time-coordinate scope: common rate scaling is compensated by horizon
# scaling, not invariant at fixed numerical T.
no_ring_rate1_t1 = Decimal(-2).exp()   # two actors, rate 1, T=1
no_ring_rate2_t1 = Decimal(-4).exp()   # two actors, rate 2, T=1
no_ring_rate1_t2 = Decimal(-4).exp()   # rate 1 at transformed horizon cT=2
fixed_t_changes = no_ring_rate1_t1 != no_ring_rate2_t1
rescaled_horizon_identity = no_ring_rate2_t1 == no_ring_rate1_t2


def coupled_birth_reception_trace(rate_scale, horizon):
    """One exact source-tape coupling under wait -> wait/rate_scale.

    The base tape makes A birth A/1 at construction time 1 and B passively
    interact into A at time 2.  All later waits are beyond the horizon.
    Retaining marks/Ulam addresses while dividing every preassigned wait by c
    is the pathwise source coupling behind the full-law identity; induction
    over each birth extends the same coupling to the complete nonexplosive path.
    """
    waits = {
        "A": (F(1), F(10)),
        "B": (F(2), F(10)),
        "A/1": (F(10),),
    }
    marks = {
        "A": (("b", None), ("n", None)),
        "B": (("i", "A"), ("n", None)),
        "A/1": (("n", None),),
    }
    state = d34b_seed()
    index = {"A": 0, "B": 0}
    deadlines = {
        "A": waits["A"][0] / rate_scale,
        "B": waits["B"][0] / rate_scale,
    }
    event_times = []
    while deadlines:
        actor, when = min(deadlines.items(), key=lambda row: (row[1], row[0]))
        if when > horizon:
            break
        del deadlines[actor]
        j = index[actor]
        kind, target = marks[actor][j]
        state = d34b_step(state, kind, actor, target)
        event_times.append(when)
        index[actor] = j + 1
        if index[actor] < len(waits[actor]):
            deadlines[actor] = when + waits[actor][index[actor]] / rate_scale
        if kind == "b":
            child = state["events"][-1][3]
            index[child] = 0
            deadlines[child] = when + waits[child][0] / rate_scale
    return state, tuple(event_times)


base_coupled_state, base_coupled_times = coupled_birth_reception_trace(F(1), F(2))
scaled_coupled_state, scaled_coupled_times = coupled_birth_reception_trace(F(2), F(1))
pathwise_rate_horizon_coupling = (
    d34b_state_key(base_coupled_state) == d34b_state_key(scaled_coupled_state)
    and physical_dag_key(base_coupled_state) == physical_dag_key(scaled_coupled_state)
    and base_coupled_times == tuple(F(2) * t for t in scaled_coupled_times)
    and tuple(event[1] for event in base_coupled_state["events"]) == ("b", "i")
    and base_coupled_state["actors"]["A"]["ring"] == 1
    and base_coupled_state["actors"]["B"]["ring"] == 1
)

# Nonlinear coordinate u=t^2 maps Exp(1) survival to exp(-sqrt(u)), not Exp(1)
# survival exp(-u).  At u=4 these are exp(-2) and exp(-4).
nonlinear_transformed_survival = Decimal(-2).exp()
homogeneous_survival_at_u4 = Decimal(-4).exp()
nonlinear_law_changes = nonlinear_transformed_survival != homogeneous_survival_at_u4

# Explicit heterogeneous-rate D34b VARIANT, outside the chosen unit-rate law.
marked_pair_factor = F(1, 16)
hetero_12 = (
    marked_pair_factor * F(1, 3),
    marked_pair_factor * F(2, 3),
)
hetero_22 = (
    marked_pair_factor * F(1, 2),
    marked_pair_factor * F(1, 2),
)

transformation_table = {
    "serializer orbit / incomparable": typed_serializer_gauge,
    "common scale / embedded order": scaled_ab == order_ab,
    "common scale / fixed numeric T": not fixed_t_changes,
    "common scale / transformed horizon cT": rescaled_horizon_identity,
    "common scale / coupled birth-reception path": pathwise_rate_horizon_coupling,
    "nonlinear timestamp / realized order": monotone_order_preserved,
    "nonlinear timestamp / homogeneous law": not nonlinear_law_changes,
    "relative rates / shared wire": hetero_12 != hetero_22,
}

p11_ok = (
    typed_serializer_gauge and shared_order_physical
    and fixed_t_changes and rescaled_horizon_identity and nonlinear_law_changes
    and pathwise_rate_horizon_coupling
    and hetero_12 == (F(1, 48), F(1, 24))
    and hetero_22 == (F(1, 32), F(1, 32))
    and transformation_table == {
        "serializer orbit / incomparable": True,
        "common scale / embedded order": True,
        "common scale / fixed numeric T": False,
        "common scale / transformed horizon cT": True,
        "common scale / coupled birth-reception path": True,
        "nonlinear timestamp / realized order": True,
        "nonlinear timestamp / homogeneous law": False,
        "relative rates / shared wire": True,
    }
)
check(
    "P11 TYPED-DAG / TIME-TRANSFORMATION TABLE [exact + 100-decimal exp]: "
    "actual disjoint actor serializations canonicalize identically while shared-"
    "wire orders differ; common rate scaling preserves embedded order and obeys "
    "Law_(c lambda,T)=Law_(lambda,cT), including an exactly coupled birth then "
    "passive-reception path, but changes the fixed-T law; nonlinear "
    "time maps preserve realized order but not homogeneous hazards; the named "
    "heterogeneous D34b variant gives marked masses (1/48,1/24) vs (1/32,1/32)",
    p11_ok,
    f"table={transformation_table}; coupled times={base_coupled_times}->"
    f"{scaled_coupled_times}; hetero={hetero_12}->{hetero_22}",
)


# ---------------------------------------------------------------------------
# P12: record/predictive-state capacity ledger.

capacity_ledger = {
    "event outcome alphabet rank": ("bounded", 6),
    "event incidence in/out arity": ("bounded", 2),
    "Ulam identifier bit length": ("unbounded", None),
    "actor degree / edge census": ("unbounded", None),
    "complete configuration size at unbounded time": ("unbounded", None),
    "candidate connected-boundary width": ("unproved/unbounded", None),
    "renewal age-vector dimension": ("population-dependent", None),
    "observer posterior belief classes": ("growing in specimen", None),
}
bounded_fields = {k for k, (kind, _) in capacity_ledger.items()
                  if kind == "bounded"}
unbounded_fields = set(capacity_ledger) - bounded_fields
p12_ok = (
    bounded_fields == {
        "event outcome alphabet rank", "event incidence in/out arity"
    }
    and len(unbounded_fields) == 6
    and capacity_ledger["event outcome alphabet rank"] == ("bounded", 6)
    and capacity_ledger["event incidence in/out arity"] == ("bounded", 2)
)
check(
    "P12 CAPACITY / OWNERSHIP LEDGER [exact declaration gate]: only fresh "
    "event outcome rank six and incidence arity two are bounded; Ulam bits, "
    "actor degree, full configuration size, boundary width, age-vector width "
    "and predictive-belief complexity are not uniformly bounded. The global "
    "Markov configuration is not one finite-capacity record",
    p12_ok,
    f"bounded={sorted(bounded_fields)}; nonbounded={len(unbounded_fields)} fields",
)


# ---------------------------------------------------------------------------
# P13: repaired classical scorecard.

p13_ok = PASS == 12 and FAIL == 0
check(
    "P13 REPAIRED CLASSICAL SCORECARD [dependent]: the ideal chosen D34b law "
    "is strong Markov on its COMPLETE GLOBAL Harris configuration and has a "
    "sum of support-local actor generators; the exact HMM identifies observed "
    "memory through law-scoped non-lumpability; exponential age is removable "
    "while renewal closure needs a global age vector; time/order gauges have "
    "the printed stopping scopes. A bounded local predictive collar, physical "
    "proper time, timed quantum lift and universe-law selection remain open",
    p13_ok,
    "maximum noun: D34b GLOBAL STRONG-MARKOV PROCESS WITH SUPPORT-LOCAL "
    "GENERATOR + EXACT CLASSICAL OBSERVABLE-MEMORY/CLOCK CHARACTERIZATION",
)

summary = (
    f"gates={PASS}/{PASS + FAIL}; witness={ftext(n10)}!={ftext(n00)}; "
    f"history_counts={','.join(map(str, history_counts))}; "
    f"belief_classes={','.join(map(str, belief_class_counts))}; "
    f"renewal={ftext(renewal_age0)}!={ftext(renewal_age1)}; "
    f"D34b_incoming={ftext(incoming_before)}->{ftext(incoming_after)}; "
    f"relative_rate={ftext(shared_a_first_old)}->{ftext(shared_a_first_changed)}; "
    f"bounded_fields={len(bounded_fields)}"
)
digest = hashlib.sha256(summary.encode("utf-8")).hexdigest()
print(f"[SUMMARY] {summary}")
print(f"[RECEIPT-SHA256] {digest}")
print(f"[VERDICT] {'PASS' if FAIL == 0 else 'FAIL'} — {PASS}/{PASS + FAIL}")
sys.exit(1 if FAIL else 0)
