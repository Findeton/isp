#!/usr/bin/env python3
"""
Paper 29 receipt: projection-sufficiency invariant.

This receipt is deliberately finite and exact.  It tests the algebraic rule
that replaces the failed search for a single numerical matching-envelope
constant:

    only the likelihood residue that survives projection to committed records
    can belong to the click law.

Let pi: H -> R be a hidden lift of a finite committed record space.  A hidden
law may change conditionals inside the fibers of pi, or it may change the
record pushforward.  Record tests can only see the latter.  Equivalently, the
physical likelihood ratio is the conditional expectation of the hidden ratio
on the record sigma-field.

All finite probabilities are exact Fractions.  Decimal reporting uses mpmath
with dps=140.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def fmt_frac(x, digits=36):
    return mp.nstr(mp.mpf(x.numerator) / mp.mpf(x.denominator), digits)


def fmt_dict(dct, digits=18):
    return {key: fmt_frac(value, digits) for key, value in dct.items()}


def pushforward(law, fiber):
    out = defaultdict(Fraction)
    for prob, record in zip(law, fiber):
        out[record] += prob
    return dict(sorted(out.items()))


def second_moment(P, Q):
    return sum((Q[key] * Q[key]) / P[key] for key in P if Q[key] != 0)


def hidden_second_moment(P, Q):
    return sum((q * q) / p for p, q in zip(P, Q) if q != 0)


def expectation(law, values):
    return sum(law[key] * values[key] for key in law)


def lifted_expectation(law, fiber, values):
    return sum(prob * values[record] for prob, record in zip(law, fiber))


def all_record_events(records):
    keys = list(records)
    for size in range(len(keys) + 1):
        for event in combinations(keys, size):
            yield set(event)


def event_mass(law, event):
    return sum(prob for key, prob in law.items() if key in event)


def conditional_from_template(record_law, template_hidden, fiber):
    """Use template_hidden conditionals inside each record fiber."""
    template_record = pushforward(template_hidden, fiber)
    out = []
    for prob, record in zip(template_hidden, fiber):
        out.append(record_law[record] * prob / template_record[record])
    return out


def group_by_likelihood(P, Q):
    groups = defaultdict(lambda: {"P": Fraction(0), "Q": Fraction(0)})
    for record in P:
        level = Q[record] / P[record]
        groups[level]["P"] += P[record]
        groups[level]["Q"] += Q[record]
    return dict(groups)


print("=" * 80)
print("Paper 29 projection-sufficiency invariant")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

fiber = ["A", "A", "B", "B", "B", "C", "C", "D"]
hidden_P = [
    Fraction(1, 12),
    Fraction(2, 12),
    Fraction(1, 12),
    Fraction(1, 12),
    Fraction(3, 12),
    Fraction(2, 12),
    Fraction(1, 12),
    Fraction(1, 12),
]

# Same record pushforward, different hidden conditionals.
hidden_bookkeeping_Q = [
    Fraction(2, 12),
    Fraction(1, 12),
    Fraction(3, 12),
    Fraction(1, 12),
    Fraction(1, 12),
    Fraction(1, 12),
    Fraction(2, 12),
    Fraction(1, 12),
]

record_P = pushforward(hidden_P, fiber)
record_bookkeeping_Q = pushforward(hidden_bookkeeping_Q, fiber)

print("\n=== Hidden bookkeeping change ===")
print(f"record_P = {fmt_dict(record_P)}")
print(f"record_bookkeeping_Q = {fmt_dict(record_bookkeeping_Q)}")

test_fields = [
    {"A": Fraction(1), "B": Fraction(0), "C": Fraction(0), "D": Fraction(0)},
    {"A": Fraction(-2), "B": Fraction(3), "C": Fraction(1), "D": Fraction(5)},
    {"A": Fraction(7, 3), "B": Fraction(-1, 2), "C": Fraction(4), "D": Fraction(-9)},
]
test_gaps = [
    abs(expectation(record_P, f) - expectation(record_bookkeeping_Q, f))
    for f in test_fields
]
S_book_record = second_moment(record_P, record_bookkeeping_Q)
S_book_hidden = hidden_second_moment(hidden_P, hidden_bookkeeping_Q)
print(f"S_record = {fmt_frac(S_book_record)}")
print(f"S_hidden = {fmt_frac(S_book_hidden)}")
print(f"max_record_test_gap = {max(test_gaps)}")

check(
    "hidden bookkeeping with the same pushforward is invisible to record tests",
    record_P == record_bookkeeping_Q and max(test_gaps) == 0,
    f"S_record={fmt_frac(S_book_record)} S_hidden={fmt_frac(S_book_hidden)}",
)
check(
    "projection erases hidden-only chi-square residue",
    S_book_record == 1 and S_book_hidden > S_book_record,
    f"gap={fmt_frac(S_book_hidden - S_book_record)}",
)

print("\n=== Record-visible likelihood tilt ===")
likelihood = {
    "A": Fraction(1, 2),
    "B": Fraction(6, 5),
    "C": Fraction(1, 2),
    "D": Fraction(3, 1),
}
record_tilt_Q = {key: record_P[key] * likelihood[key] for key in record_P}
hidden_tilt_Q = [prob * likelihood[record] for prob, record in zip(hidden_P, fiber)]
tilt_push = pushforward(hidden_tilt_Q, fiber)
S_tilt_record = second_moment(record_P, record_tilt_Q)
S_tilt_hidden = hidden_second_moment(hidden_P, hidden_tilt_Q)
print(f"record_tilt_Q = {fmt_dict(record_tilt_Q)}")
print(f"S_record = {fmt_frac(S_tilt_record)}")
print(f"S_hidden = {fmt_frac(S_tilt_hidden)}")

lifted_gaps = [
    abs(lifted_expectation(hidden_tilt_Q, fiber, f) - expectation(record_tilt_Q, f))
    for f in test_fields
]
check(
    "fiber-measurable likelihood has equal hidden and record second moments",
    tilt_push == record_tilt_Q and S_tilt_hidden == S_tilt_record,
    f"S={fmt_frac(S_tilt_record)}",
)
check(
    "lifted hidden law and record pushforward agree on every record test",
    max(lifted_gaps) == 0,
    f"max_lifted_gap={max(lifted_gaps)}",
)

print("\n=== Mixed hidden residue plus record-visible tilt ===")
hidden_mixed_Q = conditional_from_template(record_tilt_Q, hidden_bookkeeping_Q, fiber)
mixed_push = pushforward(hidden_mixed_Q, fiber)
S_mixed_record = second_moment(record_P, mixed_push)
S_mixed_hidden = hidden_second_moment(hidden_P, hidden_mixed_Q)
print(f"S_record = {fmt_frac(S_mixed_record)}")
print(f"S_hidden = {fmt_frac(S_mixed_hidden)}")
check(
    "projection keeps only the record-visible part of a mixed hidden lift",
    mixed_push == record_tilt_Q and S_mixed_record == S_tilt_record,
    f"hidden_gap={fmt_frac(S_mixed_hidden - S_mixed_record)}",
)
check(
    "data processing is strict when non-record conditionals are changed",
    S_mixed_hidden > S_mixed_record,
    f"S_hidden={fmt_frac(S_mixed_hidden)} S_record={fmt_frac(S_mixed_record)}",
)

print("\n=== Canonical likelihood sector ===")
groups = group_by_likelihood(record_P, record_tilt_Q)
group_P = {level: mass["P"] for level, mass in groups.items()}
group_Q = {level: mass["Q"] for level, mass in groups.items()}
S_group = second_moment(group_P, group_Q)
for level, masses in sorted(groups.items(), key=lambda item: item[0]):
    print(
        f"L={fmt_frac(level, 18)} P_level={fmt_frac(masses['P'], 18)} "
        f"Q_level={fmt_frac(masses['Q'], 18)}"
    )
check(
    "grouping by exact likelihood level preserves record chi-square",
    S_group == S_tilt_record,
    f"S_group={fmt_frac(S_group)} S_record={fmt_frac(S_tilt_record)}",
)

max_event_excess = Fraction(-10**9, 1)
worst_event = None
for event in all_record_events(record_P):
    p = event_mass(record_P, event)
    q = event_mass(record_tilt_Q, event)
    # Compare q^2 <= S p exactly to avoid square roots.
    excess = q * q - S_tilt_record * p
    if excess > max_event_excess:
        max_event_excess = excess
        worst_event = tuple(sorted(event))
check(
    "record second moment controls every finite record event",
    max_event_excess <= 0,
    f"worst_event={worst_event} max(q^2-Sp)={fmt_frac(max_event_excess)}",
)

print("\n=== Invariant status ===")
print(
    "The physical residue of a hidden lift is the projected likelihood field "
    "L_R=dQ_R/dP_R.  Conditional changes inside hidden fibers are invisible to "
    "record tests.  If such changes are claimed to matter, they must be "
    "promoted to committed records; otherwise they are representation-only."
)

print("\n" + "=" * 80)
failed = False
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
    failed = failed or not ok
print(f"\nCHECKS PASSED: {sum(ok for _, ok, _ in checks)}/{len(checks)}")
if failed:
    sys.exit(1)
print("DONE.")
