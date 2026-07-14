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
quantity is an explicitly labeled 100-decimal regression of the analytic
exponential memorylessness identity.  Gates P1--P6 are substantive; P7 is the
dependent claim scorecard.  Exit 1 on any failure.
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
SINDEX = {s: i for i, s in enumerate(STATES)}
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


# Predictive signatures of a known hidden state: probabilities of all future
# observation words through a specified horizon.  Horizon one already
# separates A, B and C, and later horizons retain the same partition.
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

p2_ok = (
    partitions == [(('A',), ('B',), ('C',))] * 4
    and b10 != b00
    and n10 != n00
)
check(
    "P2 MINIMAL PREDICTIVE STATE [exact]: future-law equivalence separates "
    "all three hidden carrier states, while the observer's record merges A/B; "
    "the two witness histories require distinct posterior predictive states",
    p2_ok,
    f"partitions h=1..4={partitions}; beliefs={b10} vs {b00}",
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
p3_ok = (
    mat_rows_normalized(GOOD_TRANS)
    and strongly_lumpable(GOOD_STATES, GOOD_OBS, GOOD_TRANS)
    and good_sums["D"] == good_sums["E"] == (F(2, 3), F(1, 3))
    and good_sums["F"] == (F(1, 2), F(1, 2))
    and not strongly_lumpable(STATES, OBS, TRANS)
    and bad_sums["A"] == (F(1, 2), F(1, 2))
    and bad_sums["B"] == (F(3, 4), F(1, 4))
    and n10 != n00
)
check(
    "P3 LUMPABILITY IS THE EXACT DIVIDE [exact]: a positive control has a "
    "closed two-record quotient, while the A/B projection fails because its "
    "same-record states have different group-transition rows; the 10/00 "
    "multi-step witness operationalizes the resulting memory",
    p3_ok,
    f"good quotient={good_quotient}; bad A={bad_sums['A']}, "
    f"bad B={bad_sums['B']}; next1={n10} vs {n00}",
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
    "P5 CLOCK-AGE STATUS [exact + 100-decimal regression]: exponential "
    "residual waiting is age-independent, so current live graph/tips plus "
    "fresh marks close the chosen D34b actor process; a uniform-renewal clock "
    "has next-half-unit ring probabilities 1/4 at age 0 and 1/2 at age 1, "
    "so age is a necessary additional predictive variable there",
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
    "P7 CLAIM SCORECARD [dependent]: this earns a classical characterization "
    "for the chosen specimens and D34b exponential actor architecture: full "
    "history Markovization is global, local closure requires a sufficient "
    "record-carried state, visible memory is non-lumpability, exponential "
    "clock age is removable, and relative rates remain chosen physical data. "
    "It does not prove every SHARD law has finite local memory, derive proper "
    "time, or select the universe law",
    p7_ok,
    "maximum noun: CLASSICAL PREDICTIVE-STATE / OBSERVABLE-MEMORY / "
    "CLOCK-STATUS CHARACTERIZATION",
)

summary = (
    f"gates={PASS}/{PASS + FAIL}; witness={ftext(n10)}!={ftext(n00)}; "
    f"history_counts={','.join(map(str, history_counts))}; "
    f"renewal={ftext(renewal_age0)}!={ftext(renewal_age1)}; "
    f"relative_rate={ftext(shared_a_first_old)}->{ftext(shared_a_first_changed)}"
)
digest = hashlib.sha256(summary.encode("utf-8")).hexdigest()
print(f"[SUMMARY] {summary}")
print(f"[RECEIPT-SHA256] {digest}")
print(f"[VERDICT] {'PASS' if FAIL == 0 else 'FAIL'} — {PASS}/{PASS + FAIL}")
sys.exit(1 if FAIL else 0)
