#!/usr/bin/env python3
"""
Paper 29 receipt: projection Ward tower.

This receipt checks the finite Einstein/Noether statement behind record
covariance:

    L_record o pi = E[L_hidden | pi].

It also checks the tower law for a further committed coarsening c:

    L_coarse o c = E[L_record | c].

Vertical hidden perturbations with zero fiber-mean change the hidden likelihood
and hidden second moment, but leave every record and coarse observable
unchanged.

All probabilities are exact Fractions.
"""

from collections import defaultdict
from fractions import Fraction
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def fmt_frac(x, digits=30):
    return mp.nstr(mp.mpf(x.numerator) / mp.mpf(x.denominator), digits)


def pushforward(law, mapping):
    out = defaultdict(Fraction)
    for atom, prob in law.items():
        out[mapping[atom]] += prob
    return dict(out)


def likelihood(Q, P):
    return {atom: Q[atom] / P[atom] for atom in P}


def second_moment(P, L):
    return sum(P[atom] * L[atom] * L[atom] for atom in P)


def conditional_likelihood(P, L, mapping):
    p_coarse = defaultdict(Fraction)
    q_coarse = defaultdict(Fraction)
    for atom, p in P.items():
        coarse = mapping[atom]
        p_coarse[coarse] += p
        q_coarse[coarse] += p * L[atom]
    return {
        atom: q_coarse[mapping[atom]] / p_coarse[mapping[atom]]
        for atom in P
    }


print("=" * 80)
print("Paper 29 projection Ward tower")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

hidden_atoms = tuple(range(12))
pi = {
    0: "A",
    1: "A",
    2: "A",
    3: "B",
    4: "B",
    5: "C",
    6: "C",
    7: "C",
    8: "C",
    9: "D",
    10: "D",
    11: "E",
}
coarse_of_record = {"A": "left", "B": "left", "C": "middle", "D": "right", "E": "right"}
coarse_of_hidden = {atom: coarse_of_record[pi[atom]] for atom in hidden_atoms}

P_hidden = {
    0: Fraction(1, 24),
    1: Fraction(1, 12),
    2: Fraction(1, 8),
    3: Fraction(1, 10),
    4: Fraction(1, 15),
    5: Fraction(1, 20),
    6: Fraction(1, 10),
    7: Fraction(1, 8),
    8: Fraction(1, 12),
    9: Fraction(1, 16),
    10: Fraction(1, 16),
    11: Fraction(3, 32),
}
total = sum(P_hidden.values())
P_hidden = {atom: prob / total for atom, prob in P_hidden.items()}

horizontal_record_factor = {
    "A": Fraction(3, 2),
    "B": Fraction(4, 5),
    "C": Fraction(6, 5),
    "D": Fraction(7, 10),
    "E": Fraction(9, 5),
}
vertical_raw = {
    0: Fraction(1, 3),
    1: Fraction(-1, 5),
    2: Fraction(0),
    3: Fraction(2, 7),
    4: Fraction(0),
    5: Fraction(-1, 6),
    6: Fraction(1, 8),
    7: Fraction(0),
    8: Fraction(1, 12),
    9: Fraction(-1, 9),
    10: Fraction(0),
    11: Fraction(0),
}

fiber_mean = defaultdict(Fraction)
fiber_mass = defaultdict(Fraction)
for atom, p in P_hidden.items():
    fiber_mean[pi[atom]] += p * vertical_raw[atom]
    fiber_mass[pi[atom]] += p
for record in fiber_mean:
    fiber_mean[record] /= fiber_mass[record]

vertical_centered = {
    atom: vertical_raw[atom] - fiber_mean[pi[atom]]
    for atom in hidden_atoms
}

epsilon = Fraction(1, 4)
L_hidden_horizontal = {
    atom: horizontal_record_factor[pi[atom]]
    for atom in hidden_atoms
}
normalizer_horizontal = sum(P_hidden[atom] * L_hidden_horizontal[atom] for atom in hidden_atoms)
L_hidden_horizontal = {
    atom: L_hidden_horizontal[atom] / normalizer_horizontal
    for atom in hidden_atoms
}

L_hidden_mixed = {
    atom: L_hidden_horizontal[atom] * (1 + epsilon * vertical_centered[atom])
    for atom in hidden_atoms
}
normalizer_mixed = sum(P_hidden[atom] * L_hidden_mixed[atom] for atom in hidden_atoms)
L_hidden_mixed = {atom: L_hidden_mixed[atom] / normalizer_mixed for atom in hidden_atoms}

Q_hidden_horizontal = {
    atom: P_hidden[atom] * L_hidden_horizontal[atom]
    for atom in hidden_atoms
}
Q_hidden_mixed = {
    atom: P_hidden[atom] * L_hidden_mixed[atom]
    for atom in hidden_atoms
}

P_record = pushforward(P_hidden, pi)
Q_record_horizontal = pushforward(Q_hidden_horizontal, pi)
Q_record_mixed = pushforward(Q_hidden_mixed, pi)

P_coarse = pushforward(P_hidden, coarse_of_hidden)
Q_coarse_horizontal = pushforward(Q_hidden_horizontal, coarse_of_hidden)
Q_coarse_mixed = pushforward(Q_hidden_mixed, coarse_of_hidden)

L_record = likelihood(Q_record_horizontal, P_record)
L_record_mixed = likelihood(Q_record_mixed, P_record)
L_coarse = likelihood(Q_coarse_horizontal, P_coarse)
L_coarse_mixed = likelihood(Q_coarse_mixed, P_coarse)

record_pullback_from_hidden = conditional_likelihood(P_hidden, L_hidden_mixed, pi)
coarse_pullback_from_record = conditional_likelihood(
    P_record, L_record, coarse_of_record
)

S_hidden_horizontal = second_moment(P_hidden, L_hidden_horizontal)
S_hidden_mixed = second_moment(P_hidden, L_hidden_mixed)
S_record = second_moment(P_record, L_record)
S_coarse = second_moment(P_coarse, L_coarse)

record_gap = max(abs(L_record_mixed[record] - L_record[record]) for record in P_record)
coarse_gap = max(abs(L_coarse_mixed[coarse] - L_coarse[coarse]) for coarse in P_coarse)
ward_gap = max(
    abs(record_pullback_from_hidden[atom] - L_record_mixed[pi[atom]])
    for atom in hidden_atoms
)
tower_gap = max(
    abs(coarse_pullback_from_record[record] - L_coarse[coarse_of_record[record]])
    for record in P_record
)

print(f"record atoms={len(P_record)} coarse atoms={len(P_coarse)} hidden atoms={len(P_hidden)}")
print(f"S_hidden_horizontal={fmt_frac(S_hidden_horizontal, 30)}")
print(f"S_hidden_mixed={fmt_frac(S_hidden_mixed, 30)}")
print(f"S_record={fmt_frac(S_record, 30)}")
print(f"S_coarse={fmt_frac(S_coarse, 30)}")
print(f"record_gap_after_vertical={fmt_frac(record_gap, 30)}")
print(f"coarse_gap_after_vertical={fmt_frac(coarse_gap, 30)}")
print(f"ward_gap={fmt_frac(ward_gap, 30)}")
print(f"tower_gap={fmt_frac(tower_gap, 30)}")

check(
    "vertical hidden perturbation changes hidden second moment",
    S_hidden_mixed != S_hidden_horizontal,
    f"horizontal={fmt_frac(S_hidden_horizontal, 20)} mixed={fmt_frac(S_hidden_mixed, 20)}",
)
check(
    "vertical hidden perturbation leaves record law unchanged",
    record_gap == 0 and coarse_gap == 0,
    f"record_gap={fmt_frac(record_gap, 20)} coarse_gap={fmt_frac(coarse_gap, 20)}",
)
check(
    "record Ward identity holds",
    ward_gap == 0,
    f"ward_gap={fmt_frac(ward_gap, 20)}",
)
check(
    "coarse tower identity holds",
    tower_gap == 0,
    f"tower_gap={fmt_frac(tower_gap, 20)}",
)
check(
    "second moments decrease under projection",
    S_hidden_mixed >= S_record >= S_coarse,
    f"S_hidden={fmt_frac(S_hidden_mixed, 20)} S_record={fmt_frac(S_record, 20)} S_coarse={fmt_frac(S_coarse, 20)}",
)

print("\n=== Ward tower status ===")
print(
    "The exact finite tower says hidden likelihood has a unique record-visible "
    "representative, and that representative has a unique coarsened "
    "representative.  Vertical hidden bookkeeping can inflate hidden second "
    "moments, but it has zero record charge."
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
