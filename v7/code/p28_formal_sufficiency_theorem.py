#!/usr/bin/env python3
"""
Paper 28 receipt: finite record-sufficiency theorem.

This receipt turns the record-sufficiency principle into exact finite
probability identities.

Let P and Q be laws on the committed record sigma-field, and let

    L = dQ/dP,
    S = E_P[L^2] = 1 + chi^2(Q || P).

Then:

  * hidden refinements with the same record pushforward give identical
    expectations for every record test;
  * Q(A) <= sqrt(S) sqrt(P(A)) for every record event A;
  * TV(Q,P) <= 1/2 sqrt(S - 1);
  * coarsening cannot increase chi-square second moment;
  * independent repetition multiplies second moments;
  * a coarse finite feature can miss a full record-sigma-field divergence.

All non-integer arithmetic uses mpmath with dps=140.
"""

from itertools import product
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=36):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def mpv(values):
    return [mp.mpf(v) for v in values]


def total(values):
    return mp.fsum(values)


def pushforward(law, fiber):
    out = {}
    for prob, record in zip(law, fiber):
        out[record] = out.get(record, mp.mpf("0")) + prob
    return [out[key] for key in sorted(out)]


def expectation(law, test):
    return mp.fsum(p * f for p, f in zip(law, test))


def second_moment(P, Q):
    return mp.fsum((q * q) / p for p, q in zip(P, Q) if q != 0)


def chi2(P, Q):
    return second_moment(P, Q) - 1


def tv(P, Q):
    return mp.mpf("0.5") * mp.fsum(abs(p - q) for p, q in zip(P, Q))


def events(n):
    for mask in range(1 << n):
        yield [i for i in range(n) if mask & (1 << i)]


def event_mass(law, event):
    return mp.fsum(law[i] for i in event)


def product_law_direct(law, repeats):
    out = []
    for indices in product(range(len(law)), repeat=repeats):
        prob = mp.mpf("1")
        for idx in indices:
            prob *= law[idx]
        out.append(prob)
    return out


print("=" * 80)
print("Paper 28 finite record-sufficiency theorem receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n=== Same hidden refinement pushforward ===")
hidden_P = mpv(["0.20", "0.30", "0.20", "0.10", "0.20"])
hidden_Q = mpv(["0.40", "0.10", "0.20", "0.25", "0.05"])
fiber = [0, 0, 1, 2, 2]
record_P = pushforward(hidden_P, fiber)
record_Q = pushforward(hidden_Q, fiber)
tests = [
    mpv(["1", "0", "0"]),
    mpv(["0", "1", "0"]),
    mpv(["0", "0", "1"]),
    mpv(["0", "1", "3"]),
    mpv(["-1", "4", "0.5"]),
]
gaps = [abs(expectation(record_P, test) - expectation(record_Q, test)) for test in tests]
print(f"record_P = {[fmt(x) for x in record_P]}")
print(f"record_Q = {[fmt(x) for x in record_Q]}")
print(f"max_record_test_gap = {fmt(max(gaps))}")

check(
    "same record pushforward gives identical record-test expectations",
    max(gaps) == 0 and record_P == record_Q,
    f"max_gap={fmt(max(gaps))}",
)

print("\n=== Second moment controls record events ===")
P = mpv(["0.50", "0.30", "0.20"])
Q = mpv(["0.40", "0.35", "0.25"])
S = second_moment(P, Q)
X2 = chi2(P, Q)
TV = tv(P, Q)
TV_bound = mp.mpf("0.5") * mp.sqrt(X2)
max_event_excess = mp.mpf("-inf")
worst_event = None
for event in events(len(P)):
    p_event = event_mass(P, event)
    q_event = event_mass(Q, event)
    bound = mp.sqrt(S) * mp.sqrt(p_event)
    excess = q_event - bound
    if excess > max_event_excess:
        max_event_excess = excess
        worst_event = tuple(event)

print(f"S = {fmt(S)}")
print(f"chi2 = {fmt(X2)}")
print(f"TV = {fmt(TV)}")
print(f"TV_bound = {fmt(TV_bound)}")
print(f"worst_event = {worst_event}, excess = {fmt(max_event_excess)}")

check(
    "S equals 1 plus chi-square divergence",
    abs(S - (1 + X2)) < mp.mpf("1e-120"),
    f"S={fmt(S)} chi2={fmt(X2)}",
)
check(
    "Cauchy-Schwarz event bound holds for every finite record event",
    max_event_excess <= mp.mpf("1e-120"),
    f"worst_event={worst_event} excess={fmt(max_event_excess)}",
)
check(
    "total variation is bounded by the chi-square second moment",
    TV <= TV_bound,
    f"TV={fmt(TV)} bound={fmt(TV_bound)}",
)

print("\n=== Data processing under coarsening ===")
coarse_fiber = [0, 0, 1]
coarse_P = pushforward(P, coarse_fiber)
coarse_Q = pushforward(Q, coarse_fiber)
S_coarse = second_moment(coarse_P, coarse_Q)
print(f"S_full = {fmt(S)}")
print(f"S_coarse = {fmt(S_coarse)}")
check(
    "coarsening cannot increase chi-square second moment",
    S_coarse <= S + mp.mpf("1e-120"),
    f"S_coarse={fmt(S_coarse)} S_full={fmt(S)}",
)

print("\n=== Independent repetition ===")
product_errors = []
for repeats in range(1, 5):
    P_rep = product_law_direct(P, repeats)
    Q_rep = product_law_direct(Q, repeats)
    S_rep = second_moment(P_rep, Q_rep)
    expected = S ** repeats
    product_errors.append(abs(S_rep - expected))
    print(
        f"repeats={repeats} S_rep={fmt(S_rep)} "
        f"S^repeats={fmt(expected)} error={fmt(product_errors[-1])}"
    )
check(
    "independent repetition multiplies record second moments",
    max(product_errors) < mp.mpf("1e-110"),
    f"max_error={fmt(max(product_errors))}",
)

print("\n=== Bounded second moment gives contiguity-scale washout ===")
C = mp.mpf("4")
toy_rows = []
for n in [10, 100, 1000, 10000]:
    nmp = mp.mpf(n)
    p_event = 1 / (nmp * nmp)
    q_event = mp.sqrt(C) * mp.sqrt(p_event)
    Pn = [p_event, 1 - p_event]
    Qn = [q_event, 1 - q_event]
    Sn = second_moment(Pn, Qn)
    toy_rows.append((n, p_event, q_event, Sn))
    print(
        f"n={n} P(A_n)={fmt(p_event)} Q(A_n)={fmt(q_event)} "
        f"S_n={fmt(Sn)}"
    )
max_Sn = max(row[3] for row in toy_rows)
last_Q = toy_rows[-1][2]
first_Q = toy_rows[0][2]
check(
    "bounded second moment forces P-small events to become Q-small",
    max_Sn < mp.mpf("5") and last_Q < first_Q / 100,
    f"max_Sn={fmt(max_Sn)} Q_10={fmt(first_Q)} Q_10000={fmt(last_Q)}",
)

print("\n=== Finite coarse features can miss full record divergence ===")
divergence_rows = []
for n in [10, 100, 1000]:
    nmp = mp.mpf(n)
    p_event = 1 / (nmp ** 4)
    q_event = 1 / nmp
    Pn = [p_event, 1 - p_event]
    Qn = [q_event, 1 - q_event]
    S_full = second_moment(Pn, Qn)
    S_trivial_feature = second_moment([mp.mpf("1")], [mp.mpf("1")])
    divergence_rows.append((n, S_full, S_trivial_feature))
    print(
        f"n={n} full_S={fmt(S_full)} "
        f"trivial_feature_S={fmt(S_trivial_feature)}"
    )
check(
    "a coarse finite feature can hide a full sigma-field divergence",
    divergence_rows[-1][1] > 100 * divergence_rows[0][1]
    and all(row[2] == 1 for row in divergence_rows),
    f"S10={fmt(divergence_rows[0][1])} S1000={fmt(divergence_rows[-1][1])}",
)

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
