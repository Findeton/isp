#!/usr/bin/env python3
"""
Paper 28 receipt: sector promotion from likelihood residue.

If a hidden refinement changes the committed record pushforward from P to Q,
then the minimal binary-experiment statistic is the likelihood ratio

    L = dQ/dP.

In record-law language, a nontrivial/divergent likelihood field is not an
allowed invisible hidden variable.  It is the object that must be promoted to
an explicit record mark, action, or sector.  This receipt checks that claim in
finite probability spaces:

  * if the record pushforward is unchanged, there is no record residue;
  * if the pushforward changes, L represents every Q-expectation by a
    P-expectation;
  * grouping by exact L-levels is sufficient for the binary distinction;
  * a threshold sector captures a definite part of the chi-square residue;
  * log-likelihood actions add under independent composition;
  * repetition amplifies nontrivial residue.

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


def second_moment(P, Q):
    return mp.fsum((q * q) / p for p, q in zip(P, Q) if q != 0)


def chi2(P, Q):
    return second_moment(P, Q) - 1


def tv(P, Q):
    return mp.mpf("0.5") * mp.fsum(abs(p - q) for p, q in zip(P, Q))


def expectation(law, test):
    return mp.fsum(p * f for p, f in zip(law, test))


def pushforward_by_key(P, Q, keys):
    grouped = {}
    for p, q, key in zip(P, Q, keys):
        if key not in grouped:
            grouped[key] = [mp.mpf("0"), mp.mpf("0")]
        grouped[key][0] += p
        grouped[key][1] += q
    sorted_keys = sorted(grouped)
    return [grouped[key][0] for key in sorted_keys], [grouped[key][1] for key in sorted_keys]


def product_law(law, repeats):
    out = []
    for indices in product(range(len(law)), repeat=repeats):
        prob = mp.mpf("1")
        for idx in indices:
            prob *= law[idx]
        out.append(prob)
    return out


print("=" * 80)
print("Paper 28 sector-promotion likelihood receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n=== No pushforward change means no record sector ===")
P_same = mpv(["0.50", "0.20", "0.30"])
Q_same = mpv(["0.50", "0.20", "0.30"])
L_same = [q / p for p, q in zip(P_same, Q_same)]
S_same = second_moment(P_same, Q_same)
print(f"L_same = {[fmt(x) for x in L_same]}")
print(f"S_same = {fmt(S_same)}")
check(
    "unchanged record pushforward has zero chi-square residue",
    S_same == 1 and all(L == 1 for L in L_same),
    f"S={fmt(S_same)}",
)

print("\n=== A nontrivial residue is represented by L=dQ/dP ===")
P = mpv(["0.20", "0.30", "0.10", "0.40"])
L = mpv(["0.50", "0.50", "2.00", "1.375"])
Q = [p * l for p, l in zip(P, L)]
S = second_moment(P, Q)
X2 = chi2(P, Q)
TV = tv(P, Q)
EL = expectation(P, L)
tests = [
    mpv(["1", "0", "0", "0"]),
    mpv(["0", "1", "0", "0"]),
    mpv(["0", "0", "1", "0"]),
    mpv(["0", "0", "0", "1"]),
    mpv(["-1", "3", "0.25", "2"]),
    mpv(["4", "-0.5", "1", "0"]),
]
representation_gaps = [
    abs(expectation(Q, test) - expectation(P, [l * f for l, f in zip(L, test)]))
    for test in tests
]
print(f"P = {[fmt(x) for x in P]}")
print(f"Q = {[fmt(x) for x in Q]}")
print(f"L = {[fmt(x) for x in L]}")
print(f"E_P[L] = {fmt(EL)}")
print(f"S = {fmt(S)}")
print(f"chi2 = {fmt(X2)}")
print(f"TV = {fmt(TV)}")
print(f"max_representation_gap = {fmt(max(representation_gaps))}")

check(
    "nontrivial pushforward has positive chi-square residue",
    X2 > 0 and TV > 0 and abs(EL - 1) < mp.mpf("1e-120"),
    f"chi2={fmt(X2)} TV={fmt(TV)} E_P[L]={fmt(EL)}",
)
check(
    "likelihood ratio represents every tested Q-expectation on records",
    max(representation_gaps) < mp.mpf("1e-120"),
    f"max_gap={fmt(max(representation_gaps))}",
)

print("\n=== Exact L-level grouping is sufficient for the binary residue ===")
level_keys = [fmt(l, 20) for l in L]
P_level, Q_level = pushforward_by_key(P, Q, level_keys)
S_level = second_moment(P_level, Q_level)
print(f"P_level = {[fmt(x) for x in P_level]}")
print(f"Q_level = {[fmt(x) for x in Q_level]}")
print(f"S_level = {fmt(S_level)}")
check(
    "grouping records by exact likelihood level preserves chi-square",
    abs(S_level - S) < mp.mpf("1e-120"),
    f"S_level={fmt(S_level)} S={fmt(S)}",
)

print("\n=== A promoted threshold sector captures definite residue ===")
threshold_keys = [1 if l > 1 else 0 for l in L]
P_thresh, Q_thresh = pushforward_by_key(P, Q, threshold_keys)
S_thresh = second_moment(P_thresh, Q_thresh)
captured_fraction = chi2(P_thresh, Q_thresh) / X2
print(f"P_threshold = {[fmt(x) for x in P_thresh]}")
print(f"Q_threshold = {[fmt(x) for x in Q_thresh]}")
print(f"S_threshold = {fmt(S_thresh)}")
print(f"captured_chi2_fraction = {fmt(captured_fraction)}")
check(
    "a simple likelihood-threshold sector captures most of this residue",
    captured_fraction > mp.mpf("0.85"),
    f"fraction={fmt(captured_fraction)}",
)

print("\n=== Conditional neutrality inside an L-level ===")
low_level_indices = [i for i, l in enumerate(L) if l == mp.mpf("0.50")]
P_low_total = mp.fsum(P[i] for i in low_level_indices)
Q_low_total = mp.fsum(Q[i] for i in low_level_indices)
conditional_gaps = []
for i in low_level_indices:
    conditional_gaps.append(abs(P[i] / P_low_total - Q[i] / Q_low_total))
print(f"low_level_indices = {low_level_indices}")
print(f"max_conditional_gap = {fmt(max(conditional_gaps))}")
check(
    "within an exact likelihood level, hidden atom labels add no binary residue",
    max(conditional_gaps) < mp.mpf("1e-120"),
    f"max_gap={fmt(max(conditional_gaps))}",
)

print("\n=== Action additivity and repeated amplification ===")
max_action_error = mp.mpf("0")
for i, j in product(range(len(P)), repeat=2):
    product_L = (Q[i] * Q[j]) / (P[i] * P[j])
    action_product = mp.log(product_L)
    action_sum = mp.log(L[i]) + mp.log(L[j])
    max_action_error = max(max_action_error, abs(action_product - action_sum))
print(f"max_log_likelihood_additivity_error = {fmt(max_action_error)}")
check(
    "log-likelihood action is additive under independent composition",
    max_action_error < mp.mpf("1e-120"),
    f"max_error={fmt(max_action_error)}",
)

amplification_errors = []
for repeats in [1, 2, 3, 4]:
    P_rep = product_law(P, repeats)
    Q_rep = product_law(Q, repeats)
    S_rep = second_moment(P_rep, Q_rep)
    expected = S ** repeats
    amplification_errors.append(abs(S_rep - expected))
    print(
        f"repeats={repeats} S_rep={fmt(S_rep)} "
        f"S^repeats={fmt(expected)}"
    )
check(
    "nontrivial residue amplifies by second-moment multiplication",
    S > 1 and max(amplification_errors) < mp.mpf("1e-110"),
    f"S={fmt(S)} max_error={fmt(max(amplification_errors))}",
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
